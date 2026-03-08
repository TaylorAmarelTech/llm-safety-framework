"""
Genetic algorithm for evolving adversarial attack prompts.

Maintains a population of attack prompts, evaluates fitness by testing
against target LLMs, selects the most effective attacks via tournament
selection, and breeds new attacks through crossover and mutation.

Connects to:
- FitnessTracker: records per-mutator bypass rates
- AttackQualityScorer: filters low-quality offspring
- 488 prompt injection mutators: mutation operators
- LiveTester: evaluates fitness against real models (optional)
"""

from __future__ import annotations

import hashlib
import json
import random
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from pydantic import BaseModel


class EvolutionConfig(BaseModel):
    """Configuration for the evolutionary engine."""
    population_size: int = 50
    generations: int = 10
    tournament_k: int = 3
    crossover_rate: float = 0.7
    mutation_rate: float = 0.8
    elitism_count: int = 5  # Top N survive unchanged
    min_prompt_length: int = 100
    max_prompt_length: int = 5000
    novelty_bonus: float = 0.1  # Reward for diversity
    seed: int = 42
    output_path: Path = Path("data/training/evolution")


@dataclass
class Individual:
    """A single attack prompt in the population."""
    prompt: str
    category: str = "general"
    corridor: str = ""
    fitness: float = 0.0
    generation: int = 0
    parent_ids: list[str] = field(default_factory=list)
    mutation_history: list[str] = field(default_factory=list)
    bypass_count: int = 0
    test_count: int = 0
    id: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(
                (self.prompt + str(time.time())).encode()
            ).hexdigest()[:12]

    @property
    def bypass_rate(self) -> float:
        return self.bypass_count / self.test_count if self.test_count > 0 else 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "prompt": self.prompt,
            "category": self.category,
            "corridor": self.corridor,
            "fitness": round(self.fitness, 4),
            "generation": self.generation,
            "parent_ids": self.parent_ids,
            "mutation_history": self.mutation_history,
            "bypass_rate": round(self.bypass_rate, 4),
            "test_count": self.test_count,
        }


@dataclass
class GenerationStats:
    """Statistics from a single generation."""
    generation: int
    population_size: int
    avg_fitness: float
    max_fitness: float
    min_fitness: float
    avg_bypass_rate: float
    crossovers: int
    mutations: int
    elite_preserved: int
    diversity_score: float  # Unique trigrams / total trigrams

    def to_dict(self) -> dict[str, Any]:
        return {
            "generation": self.generation,
            "population_size": self.population_size,
            "avg_fitness": round(self.avg_fitness, 4),
            "max_fitness": round(self.max_fitness, 4),
            "min_fitness": round(self.min_fitness, 4),
            "avg_bypass_rate": round(self.avg_bypass_rate, 4),
            "crossovers": self.crossovers,
            "mutations": self.mutations,
            "elite_preserved": self.elite_preserved,
            "diversity_score": round(self.diversity_score, 4),
        }


class EvolutionaryEngine:
    """Genetic algorithm for evolving adversarial attack prompts."""

    def __init__(self, config: EvolutionConfig | None = None):
        self.config = config or EvolutionConfig()
        self.rng = random.Random(self.config.seed)
        self.population: list[Individual] = []
        self.history: list[GenerationStats] = []
        self._fitness_fn: Callable[[str], float] | None = None
        self._scorer = None

    @property
    def scorer(self):
        if self._scorer is None:
            from src.training.attack_scorer import AttackQualityScorer
            self._scorer = AttackQualityScorer()
        return self._scorer

    def seed_population(
        self,
        prompts: list[dict[str, Any]],
    ) -> None:
        """Initialize population from seed prompts.

        Each dict should have: prompt, category, corridor (optional).
        """
        for p in prompts:
            text = p.get("prompt", "")
            if len(text) < self.config.min_prompt_length:
                continue
            individual = Individual(
                prompt=text,
                category=p.get("category", "general"),
                corridor=p.get("corridor", ""),
                generation=0,
            )
            self.population.append(individual)

        # Trim or pad to population_size
        if len(self.population) > self.config.population_size:
            self.population = self.rng.sample(
                self.population, self.config.population_size
            )

    def set_fitness_function(
        self, fn: Callable[[str], float]
    ) -> None:
        """Set a custom fitness function.

        The function takes a prompt string and returns a fitness score (0-1).
        Higher = more effective attack.

        If not set, fitness is estimated using AttackQualityScorer.
        """
        self._fitness_fn = fn

    def evaluate_population(self) -> None:
        """Evaluate fitness of all individuals in the population."""
        for individual in self.population:
            if individual.fitness > 0 and individual.test_count > 0:
                continue  # Already evaluated

            if self._fitness_fn:
                individual.fitness = self._fitness_fn(individual.prompt)
            else:
                # Use quality score as proxy for fitness
                score = self.scorer.score(individual.prompt, individual.category)
                individual.fitness = score.overall

    def evolve_generation(self) -> GenerationStats:
        """Run one generation of evolution.

        1. Evaluate fitness
        2. Select parents via tournament selection
        3. Create offspring via crossover
        4. Mutate offspring using prompt injection mutators
        5. Filter offspring for quality
        6. Preserve elites
        7. Form new population
        """
        self.evaluate_population()

        gen_num = len(self.history) + 1
        crossover_count = 0
        mutation_count = 0

        # Sort by fitness (highest first)
        ranked = sorted(self.population, key=lambda x: x.fitness, reverse=True)

        # Preserve elites
        elites = ranked[:self.config.elitism_count]
        for e in elites:
            e.generation = gen_num

        # Generate offspring
        offspring = []
        target_count = self.config.population_size - len(elites)

        while len(offspring) < target_count:
            # Tournament selection for parents
            parent1 = self._tournament_select()
            parent2 = self._tournament_select()

            # Crossover
            if self.rng.random() < self.config.crossover_rate and parent1.id != parent2.id:
                child_prompt = self._crossover(parent1.prompt, parent2.prompt)
                parent_ids = [parent1.id, parent2.id]
                crossover_count += 1
            else:
                child_prompt = parent1.prompt
                parent_ids = [parent1.id]

            # Mutation using prompt injection mutators
            mutation_applied = ""
            if self.rng.random() < self.config.mutation_rate:
                child_prompt, mutation_applied = self._mutate(child_prompt)
                if mutation_applied:
                    mutation_count += 1

            # Quality filter
            if len(child_prompt) < self.config.min_prompt_length:
                continue
            if len(child_prompt) > self.config.max_prompt_length:
                child_prompt = child_prompt[:self.config.max_prompt_length]

            child = Individual(
                prompt=child_prompt,
                category=parent1.category,
                corridor=parent1.corridor,
                generation=gen_num,
                parent_ids=parent_ids,
                mutation_history=(
                    parent1.mutation_history + [mutation_applied]
                    if mutation_applied else parent1.mutation_history
                ),
            )
            offspring.append(child)

        # Form new population
        self.population = list(elites) + offspring[:target_count]

        # Evaluate new population
        self.evaluate_population()

        # Compute diversity
        diversity = self._compute_diversity()

        # Apply novelty bonus
        if self.config.novelty_bonus > 0:
            self._apply_novelty_bonus()

        # Record stats
        fitnesses = [ind.fitness for ind in self.population]
        bypass_rates = [ind.bypass_rate for ind in self.population]

        stats = GenerationStats(
            generation=gen_num,
            population_size=len(self.population),
            avg_fitness=sum(fitnesses) / len(fitnesses) if fitnesses else 0,
            max_fitness=max(fitnesses) if fitnesses else 0,
            min_fitness=min(fitnesses) if fitnesses else 0,
            avg_bypass_rate=sum(bypass_rates) / len(bypass_rates) if bypass_rates else 0,
            crossovers=crossover_count,
            mutations=mutation_count,
            elite_preserved=len(elites),
            diversity_score=diversity,
        )
        self.history.append(stats)
        return stats

    def evolve(
        self,
        generations: int | None = None,
        progress_callback: Callable[[int, GenerationStats], None] | None = None,
    ) -> list[GenerationStats]:
        """Run multiple generations of evolution."""
        n = generations or self.config.generations

        for i in range(n):
            stats = self.evolve_generation()
            if progress_callback:
                progress_callback(i + 1, stats)

        return self.history

    def get_best(self, n: int = 10) -> list[Individual]:
        """Get the top N individuals by fitness."""
        return sorted(
            self.population, key=lambda x: x.fitness, reverse=True
        )[:n]

    def get_population_stats(self) -> dict[str, Any]:
        """Get current population statistics."""
        if not self.population:
            return {"population_size": 0}

        fitnesses = [ind.fitness for ind in self.population]
        by_category: dict[str, int] = {}
        for ind in self.population:
            by_category[ind.category] = by_category.get(ind.category, 0) + 1

        return {
            "population_size": len(self.population),
            "generations_completed": len(self.history),
            "avg_fitness": round(sum(fitnesses) / len(fitnesses), 4),
            "max_fitness": round(max(fitnesses), 4),
            "min_fitness": round(min(fitnesses), 4),
            "by_category": by_category,
            "diversity_score": round(self._compute_diversity(), 4),
        }

    def export_best(
        self, n: int = 20, output_path: Path | None = None,
    ) -> Path:
        """Export the best individuals to a JSONL file."""
        path = output_path or self.config.output_path / "evolved_attacks.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)

        best = self.get_best(n)
        with open(path, "w", encoding="utf-8") as f:
            for ind in best:
                f.write(json.dumps(ind.to_dict(), ensure_ascii=False) + "\n")

        return path

    def save_state(self, path: Path | None = None) -> Path:
        """Save full population state for resuming later."""
        save_path = path or self.config.output_path / "evolution_state.json"
        save_path.parent.mkdir(parents=True, exist_ok=True)

        state = {
            "config": self.config.model_dump(mode="json"),
            "population": [ind.to_dict() for ind in self.population],
            "history": [s.to_dict() for s in self.history],
        }
        # Convert Path objects to strings for JSON serialization
        if "output_path" in state["config"]:
            state["config"]["output_path"] = str(state["config"]["output_path"])

        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

        return save_path

    @classmethod
    def load_state(cls, path: Path) -> EvolutionaryEngine:
        """Load a previously saved state."""
        with open(path, encoding="utf-8") as f:
            state = json.load(f)

        config = EvolutionConfig(**state["config"])
        engine = cls(config)

        for p_data in state.get("population", []):
            ind = Individual(
                prompt=p_data["prompt"],
                category=p_data.get("category", "general"),
                corridor=p_data.get("corridor", ""),
                fitness=p_data.get("fitness", 0),
                generation=p_data.get("generation", 0),
                parent_ids=p_data.get("parent_ids", []),
                mutation_history=p_data.get("mutation_history", []),
                id=p_data.get("id", ""),
            )
            engine.population.append(ind)

        for s_data in state.get("history", []):
            stats = GenerationStats(**s_data)
            engine.history.append(stats)

        return engine

    # ---- Private Methods ----

    def _tournament_select(self) -> Individual:
        """Select an individual via tournament selection."""
        candidates = self.rng.sample(
            self.population,
            min(self.config.tournament_k, len(self.population)),
        )
        return max(candidates, key=lambda x: x.fitness)

    def _crossover(self, text1: str, text2: str) -> str:
        """Crossover two prompts at sentence boundaries.

        Splits both parents into sentences and interleaves them.
        """
        sents1 = self._split_sentences(text1)
        sents2 = self._split_sentences(text2)

        if not sents1 or not sents2:
            return text1

        # Single-point crossover at sentence level
        cut1 = self.rng.randint(1, max(1, len(sents1) - 1))
        cut2 = self.rng.randint(1, max(1, len(sents2) - 1))

        if self.rng.random() < 0.5:
            child_sents = sents1[:cut1] + sents2[cut2:]
        else:
            child_sents = sents2[:cut2] + sents1[cut1:]

        return " ".join(child_sents)

    def _mutate(self, text: str) -> tuple[str, str]:
        """Mutate a prompt using a random prompt injection mutator.

        Returns (mutated_text, mutator_name).
        """
        try:
            from src.prompt_injection import get_mutator, get_mutators_by_category

            # Pick a random category, then a random mutator
            categories = [
                "encoding_format", "obfuscation", "social_engineering",
                "context_manipulation", "rhetorical", "analytical_framing",
                "legal_persona", "professional_persona", "distraction",
                "logical_fallacy", "advanced_obfuscation",
            ]
            cat = self.rng.choice(categories)
            mutator_names = get_mutators_by_category(cat)
            if not mutator_names:
                return text, ""

            name = self.rng.choice(mutator_names)
            mutator = get_mutator(name)
            if mutator is None:
                return text, ""

            variants = mutator.mutate(text)
            if not variants:
                return text, ""

            chosen = self.rng.choice(variants)
            return chosen.mutated, name

        except Exception:
            return text, ""

    def _split_sentences(self, text: str) -> list[str]:
        """Split text into sentences."""
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if len(s.strip()) > 10]

    def _compute_diversity(self) -> float:
        """Compute population diversity using trigram overlap."""
        if len(self.population) < 2:
            return 1.0

        all_trigrams: set[str] = set()
        per_individual_counts = []

        for ind in self.population:
            text = ind.prompt.lower()
            trigrams = {text[i:i+3] for i in range(len(text) - 2)}
            per_individual_counts.append(len(trigrams))
            all_trigrams.update(trigrams)

        if not all_trigrams:
            return 0.0

        total_individual = sum(per_individual_counts)
        # Diversity = ratio of unique trigrams to total
        # 1.0 = all individuals completely different
        # close to 0 = all individuals nearly identical
        return len(all_trigrams) / total_individual if total_individual > 0 else 0

    def _apply_novelty_bonus(self) -> None:
        """Reward individuals that are different from the population average."""
        if len(self.population) < 2:
            return

        # Compute average sentence count as a simple diversity proxy
        avg_len = sum(len(ind.prompt) for ind in self.population) / len(self.population)

        for ind in self.population:
            # Individuals far from average length get a small bonus
            len_diff = abs(len(ind.prompt) - avg_len) / avg_len
            novelty = min(self.config.novelty_bonus, len_diff * self.config.novelty_bonus)
            ind.fitness += novelty
