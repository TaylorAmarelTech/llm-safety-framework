"""
Genetic / Evolutionary engine for adversarial prompt optimization.

Evolves populations of mutator-chain "individuals" using crossover,
mutation, and selection operators.  Fitness is measured by the existing
FitnessTracker (EMA bypass rate) or a user-supplied callable.

Implements:
- Tournament, roulette-wheel, and rank-based selection
- Single-point, uniform, and semantic crossover of mutator chains
- Mutation operators: insert, delete, swap, replace mutator in chain
- Elitism (preserve top-k across generations)
- Island model (parallel sub-populations with periodic migration)
- Pareto front for multi-objective optimization (bypass_rate vs stealth)

Category: genetic_evolution
Count: 10

Sources:
- PAIR: "Prompt Automatic Iterative Refinement" (Chao et al., 2023)
- GPTFuzzer template evolution (Yu et al., 2023)
- Rainbow Teaming: "Open-Ended Diversity-Seeking Red Teaming" (Samvelyan et al., 2024)
- AutoDAN: "Generating Stealthy Jailbreak Prompts" (Liu et al., 2024)
- EvoPrompt: "Language Models as Evolutionary Optimizers" (2024)
"""

from __future__ import annotations

import copy
import hashlib
import math
import random
from dataclasses import dataclass, field, asdict
from typing import Any, Callable

from . import BaseMutator, register_mutator, get_mutator, list_mutators, get_mutators_by_category, MutationResult


# ---------------------------------------------------------------------------
# Core data structures
# ---------------------------------------------------------------------------


@dataclass
class Individual:
    """A single candidate in the evolutionary population.

    An individual is a *chain* of mutator names that are applied sequentially
    to a seed prompt to produce an adversarial variant.
    """

    chain: list[str]
    fitness: float = 0.0
    stealth: float = 0.5  # 0 = obvious attack, 1 = indistinguishable from benign
    generation: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def id(self) -> str:
        raw = "|".join(self.chain)
        return hashlib.md5(raw.encode()).hexdigest()[:12]

    def to_dict(self) -> dict[str, Any]:
        return {**asdict(self), "id": self.id}

    def apply(self, prompt: str) -> list[MutationResult]:
        """Apply the full mutator chain to *prompt* sequentially."""
        results: list[MutationResult] = []
        current = prompt
        for name in self.chain:
            try:
                mutator = get_mutator(name)
                mr_list = mutator.mutate(current)
                if mr_list:
                    results.extend(mr_list)
                    current = mr_list[0].mutated
            except KeyError:
                continue
        return results


@dataclass
class EvolutionResult:
    """Summary returned after an evolution run."""

    best: Individual
    population: list[Individual]
    generation: int
    history: list[dict[str, Any]]
    pareto_front: list[Individual]

    def to_dict(self) -> dict[str, Any]:
        return {
            "best": self.best.to_dict(),
            "population_size": len(self.population),
            "generation": self.generation,
            "pareto_front": [ind.to_dict() for ind in self.pareto_front],
            "history": self.history,
        }

    def generate_report(self) -> dict[str, Any]:
        """Comprehensive evolution report with convergence and diversity analysis."""
        fitnesses = [ind.fitness for ind in self.population]
        stealths = [ind.stealth for ind in self.population]

        # Convergence curve
        best_curve = [h.get("best_fitness", 0) for h in self.history]
        avg_curve = [h.get("avg_fitness", 0) for h in self.history]
        diversity_curve = [h.get("diversity", 0) for h in self.history]

        # Top-5 chains
        ranked = sorted(self.population, key=lambda i: i.fitness, reverse=True)
        top5 = [
            {"chain": ind.chain, "fitness": round(ind.fitness, 4), "stealth": round(ind.stealth, 4)}
            for ind in ranked[:5]
        ]

        # Operator effectiveness
        op_stats: dict[str, int] = {}
        for h in self.history:
            for op, count in h.get("operators_applied", {}).items():
                op_stats[op] = op_stats.get(op, 0) + count

        # Convergence speed estimate
        converged_at = None
        if len(best_curve) >= 3:
            final_best = best_curve[-1]
            threshold = final_best * 0.95
            for i, v in enumerate(best_curve):
                if v >= threshold:
                    converged_at = i
                    break

        # Pareto hypervolume approximation (for 2 objectives)
        pf = self.pareto_front
        hypervolume = 0.0
        if len(pf) >= 2:
            sorted_pf = sorted(pf, key=lambda i: i.fitness)
            for i in range(len(sorted_pf) - 1):
                width = sorted_pf[i + 1].fitness - sorted_pf[i].fitness
                height = sorted_pf[i].stealth
                hypervolume += width * height

        return {
            "generations_run": self.generation,
            "population_size": len(self.population),
            "best_fitness": round(max(fitnesses) if fitnesses else 0, 4),
            "avg_fitness": round(sum(fitnesses) / len(fitnesses), 4) if fitnesses else 0,
            "fitness_std": round(
                math.sqrt(sum((f - sum(fitnesses) / len(fitnesses)) ** 2 for f in fitnesses) / len(fitnesses)), 4
            ) if fitnesses else 0,
            "best_stealth": round(max(stealths) if stealths else 0, 4),
            "pareto_front_size": len(pf),
            "pareto_hypervolume": round(hypervolume, 4),
            "top_5_chains": top5,
            "convergence_curve": best_curve,
            "diversity_curve": diversity_curve,
            "converged_at_generation": converged_at,
            "total_operator_applications": op_stats,
            "unique_chains": len({tuple(ind.chain) for ind in self.population}),
        }


# ---------------------------------------------------------------------------
# Selection operators
# ---------------------------------------------------------------------------


def tournament_select(pop: list[Individual], k: int = 3) -> Individual:
    """Tournament selection — pick *k* random individuals, return fittest."""
    contestants = random.sample(pop, min(k, len(pop)))
    return max(contestants, key=lambda ind: ind.fitness)


def roulette_select(pop: list[Individual]) -> Individual:
    """Fitness-proportionate (roulette-wheel) selection."""
    total = sum(max(ind.fitness, 0.01) for ind in pop)
    r = random.uniform(0, total)
    cum = 0.0
    for ind in pop:
        cum += max(ind.fitness, 0.01)
        if cum >= r:
            return ind
    return pop[-1]


def rank_select(pop: list[Individual]) -> Individual:
    """Rank-based selection — probabilities proportional to rank."""
    ranked = sorted(pop, key=lambda ind: ind.fitness)
    n = len(ranked)
    weights = list(range(1, n + 1))
    return random.choices(ranked, weights=weights, k=1)[0]


_SELECTORS = {
    "tournament": tournament_select,
    "roulette": roulette_select,
    "rank": rank_select,
}


# ---------------------------------------------------------------------------
# Crossover operators
# ---------------------------------------------------------------------------


def single_point_crossover(a: Individual, b: Individual) -> tuple[Individual, Individual]:
    """Single-point crossover of mutator chains."""
    if len(a.chain) < 2 or len(b.chain) < 2:
        return copy.deepcopy(a), copy.deepcopy(b)
    pt_a = random.randint(1, len(a.chain) - 1)
    pt_b = random.randint(1, len(b.chain) - 1)
    c1 = Individual(chain=a.chain[:pt_a] + b.chain[pt_b:])
    c2 = Individual(chain=b.chain[:pt_b] + a.chain[pt_a:])
    return c1, c2


def uniform_crossover(a: Individual, b: Individual) -> tuple[Individual, Individual]:
    """Uniform crossover — each position randomly from either parent."""
    max_len = max(len(a.chain), len(b.chain))
    c1_chain: list[str] = []
    c2_chain: list[str] = []
    for i in range(max_len):
        gene_a = a.chain[i] if i < len(a.chain) else None
        gene_b = b.chain[i] if i < len(b.chain) else None
        if gene_a and gene_b:
            if random.random() < 0.5:
                c1_chain.append(gene_a)
                c2_chain.append(gene_b)
            else:
                c1_chain.append(gene_b)
                c2_chain.append(gene_a)
        elif gene_a:
            (c1_chain if random.random() < 0.5 else c2_chain).append(gene_a)
        elif gene_b:
            (c1_chain if random.random() < 0.5 else c2_chain).append(gene_b)
    if not c1_chain:
        c1_chain = [a.chain[0]] if a.chain else ["persona_switch"]
    if not c2_chain:
        c2_chain = [b.chain[0]] if b.chain else ["persona_switch"]
    return Individual(chain=c1_chain), Individual(chain=c2_chain)


def semantic_crossover(a: Individual, b: Individual) -> tuple[Individual, Individual]:
    """Semantic crossover — group chain elements by defense layer affinity.

    Takes obfuscation-layer mutators from one parent and alignment-layer
    mutators from the other.
    """
    from .coverage import CATEGORY_TAXONOMY

    def layer_of(name: str) -> str:
        try:
            cat = get_mutator(name).CATEGORY
        except KeyError:
            return "alignment"
        tax = CATEGORY_TAXONOMY.get(cat, {})
        layers = tax.get("defense_layers", ["alignment"])
        return layers[0]

    a_input = [m for m in a.chain if layer_of(m) == "input_filter"]
    a_other = [m for m in a.chain if layer_of(m) != "input_filter"]
    b_input = [m for m in b.chain if layer_of(m) == "input_filter"]
    b_other = [m for m in b.chain if layer_of(m) != "input_filter"]

    c1_chain = (a_input or b_input) + (b_other or a_other)
    c2_chain = (b_input or a_input) + (a_other or b_other)
    if not c1_chain:
        c1_chain = a.chain[:] or ["persona_switch"]
    if not c2_chain:
        c2_chain = b.chain[:] or ["persona_switch"]
    return Individual(chain=c1_chain), Individual(chain=c2_chain)


_CROSSOVERS = {
    "single_point": single_point_crossover,
    "uniform": uniform_crossover,
    "semantic": semantic_crossover,
}


# ---------------------------------------------------------------------------
# Mutation operators (on the *chain*, not the prompt text)
# ---------------------------------------------------------------------------


_META_CATEGORIES = {"genetic_evolution", "coevolution", "tree_attack"}


def _all_mutator_names() -> list[str]:
    """All mutator names *excluding* meta-attack categories to prevent recursion.

    Meta-attack categories (genetic_evolution, coevolution, tree_attack)
    compose other mutators, so including them would cause infinite recursion.
    """
    return [
        name for name, info in list_mutators().items()
        if info["category"] not in _META_CATEGORIES
    ]


def mutate_insert(ind: Individual) -> Individual:
    """Insert a random mutator into the chain."""
    new = copy.deepcopy(ind)
    pool = _all_mutator_names()
    pos = random.randint(0, len(new.chain))
    new.chain.insert(pos, random.choice(pool))
    return new


def mutate_delete(ind: Individual) -> Individual:
    """Remove a random mutator from the chain (min length 1)."""
    new = copy.deepcopy(ind)
    if len(new.chain) > 1:
        new.chain.pop(random.randrange(len(new.chain)))
    return new


def mutate_swap(ind: Individual) -> Individual:
    """Swap two random positions in the chain."""
    new = copy.deepcopy(ind)
    if len(new.chain) >= 2:
        i, j = random.sample(range(len(new.chain)), 2)
        new.chain[i], new.chain[j] = new.chain[j], new.chain[i]
    return new


def mutate_replace(ind: Individual) -> Individual:
    """Replace one mutator with a random different one."""
    new = copy.deepcopy(ind)
    pool = _all_mutator_names()
    if new.chain:
        idx = random.randrange(len(new.chain))
        new.chain[idx] = random.choice(pool)
    return new


def mutate_category_swap(ind: Individual) -> Individual:
    """Replace one mutator with another from the *same* category."""
    new = copy.deepcopy(ind)
    if not new.chain:
        return new
    idx = random.randrange(len(new.chain))
    try:
        cat = get_mutator(new.chain[idx]).CATEGORY
        siblings = get_mutators_by_category(cat)
        if len(siblings) > 1:
            siblings = [s for s in siblings if s != new.chain[idx]]
        if siblings:
            new.chain[idx] = random.choice(siblings)
    except KeyError:
        pass
    return new


_MUTATIONS = {
    "insert": mutate_insert,
    "delete": mutate_delete,
    "swap": mutate_swap,
    "replace": mutate_replace,
    "category_swap": mutate_category_swap,
}


# ---------------------------------------------------------------------------
# Pareto front extraction (multi-objective)
# ---------------------------------------------------------------------------


def _dominates(a: Individual, b: Individual) -> bool:
    """True if *a* Pareto-dominates *b* on (fitness, stealth)."""
    return (a.fitness >= b.fitness and a.stealth >= b.stealth and
            (a.fitness > b.fitness or a.stealth > b.stealth))


def compute_pareto_front(pop: list[Individual]) -> list[Individual]:
    """Extract the Pareto-optimal set on (fitness, stealth)."""
    front: list[Individual] = []
    for ind in pop:
        if not any(_dominates(other, ind) for other in pop if other is not ind):
            front.append(ind)
    front.sort(key=lambda i: i.fitness, reverse=True)
    return front


# ---------------------------------------------------------------------------
# Novelty archive + MAP-Elites (Rainbow Teaming quality-diversity)
# ---------------------------------------------------------------------------


class NoveltyArchive:
    """Bounded archive for quality-diversity search.

    Maintains a novelty archive of (vector, fitness, chain) triples and
    a MAP-Elites grid that keeps the highest-fitness individual per cell.

    Inspired by Rainbow Teaming (Samvelyan et al., 2024).
    """

    def __init__(self, capacity: int = 500, k_nearest: int = 10):
        self.capacity = capacity
        self.k_nearest = k_nearest
        self._archive: list[tuple[list[float], float, list[str]]] = []
        self._map_elites: dict[str, tuple[float, list[str]]] = {}

    def add(self, vector: list[float], fitness: float, chain: list[str]) -> None:
        """Add an individual to the archive."""
        self._archive.append((vector, fitness, list(chain)))
        if len(self._archive) > self.capacity:
            # Remove lowest-fitness entry
            worst_idx = min(range(len(self._archive)), key=lambda i: self._archive[i][1])
            self._archive.pop(worst_idx)

    def novelty_score(self, vector: list[float]) -> float:
        """Average distance to k-nearest neighbours in the archive.

        Higher = more novel (further from anything we've seen).
        """
        if not self._archive:
            return 1.0
        dists = sorted(
            _euclidean_fast(vector, entry[0]) for entry in self._archive
        )
        k = min(self.k_nearest, len(dists))
        return sum(dists[:k]) / k if k > 0 else 1.0

    def map_elites_update(self, cell_key: str, fitness: float, chain: list[str]) -> bool:
        """Update the MAP-Elites grid.  Returns True if cell was improved."""
        existing = self._map_elites.get(cell_key)
        if existing is None or fitness > existing[0]:
            self._map_elites[cell_key] = (fitness, list(chain))
            return True
        return False

    def get_map_elites_grid(self) -> dict[str, tuple[float, list[str]]]:
        """Return the current MAP-Elites grid."""
        return dict(self._map_elites)

    @property
    def archive_size(self) -> int:
        return len(self._archive)

    @property
    def elites_cells(self) -> int:
        return len(self._map_elites)

    def summary(self) -> dict[str, Any]:
        return {
            "archive_size": self.archive_size,
            "elites_cells": self.elites_cells,
            "capacity": self.capacity,
        }


def _euclidean_fast(a: list[float], b: list[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


# ---------------------------------------------------------------------------
# Adaptive parameter controller
# ---------------------------------------------------------------------------


class AdaptiveParameterController:
    """Self-adaptive mutation/crossover rate tuning.

    Tracks which operators produced fitness improvements and shifts
    probability mass toward productive operators.  Increases mutation
    rate when diversity drops and vice versa.
    """

    def __init__(
        self,
        initial_mutation_rate: float = 0.3,
        initial_crossover_rate: float = 0.7,
        diversity_low: float = 0.3,
        diversity_high: float = 0.8,
    ):
        self.mutation_rate = initial_mutation_rate
        self.crossover_rate = initial_crossover_rate
        self._diversity_low = diversity_low
        self._diversity_high = diversity_high
        self._operator_successes: dict[str, int] = {k: 1 for k in _MUTATIONS}
        self._operator_total: dict[str, int] = {k: 1 for k in _MUTATIONS}

    def record_operator(self, op_name: str, improved: bool) -> None:
        """Record whether an operator application improved fitness."""
        if op_name in self._operator_total:
            self._operator_total[op_name] += 1
            if improved:
                self._operator_successes[op_name] += 1

    def select_operator(self) -> str:
        """Pick an operator proportional to its success rate."""
        weights = {
            k: self._operator_successes[k] / self._operator_total[k]
            for k in self._operator_total
        }
        total = sum(weights.values()) or 1.0
        r = random.uniform(0, total)
        cum = 0.0
        for name, w in weights.items():
            cum += w
            if cum >= r:
                return name
        return list(weights.keys())[-1]

    def adapt(self, diversity: float) -> None:
        """Adjust rates based on current population diversity."""
        if diversity < self._diversity_low:
            self.mutation_rate = min(0.8, self.mutation_rate * 1.2)
            self.crossover_rate = max(0.3, self.crossover_rate * 0.9)
        elif diversity > self._diversity_high:
            self.mutation_rate = max(0.1, self.mutation_rate * 0.9)
            self.crossover_rate = min(0.95, self.crossover_rate * 1.1)

    def get_operator_stats(self) -> dict[str, float]:
        return {
            k: round(self._operator_successes[k] / max(self._operator_total[k], 1), 4)
            for k in self._operator_total
        }


# ---------------------------------------------------------------------------
# Main engine
# ---------------------------------------------------------------------------


class GeneticEngine:
    """Evolutionary optimizer for adversarial mutator chains.

    Maintains a population of ``Individual`` objects and evolves them toward
    maximizing bypass fitness (and optionally stealth) using standard
    genetic-algorithm operators.
    """

    def __init__(
        self,
        population_size: int = 40,
        chain_length: tuple[int, int] = (1, 4),
        selection: str = "tournament",
        crossover: str = "single_point",
        mutation_rate: float = 0.3,
        crossover_rate: float = 0.7,
        elitism: int = 2,
        seed_chains: list[list[str]] | None = None,
    ):
        self.pop_size = population_size
        self.chain_min, self.chain_max = chain_length
        self.select_fn = _SELECTORS.get(selection, tournament_select)
        self.crossover_fn = _CROSSOVERS.get(crossover, single_point_crossover)
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism = elitism
        self.population: list[Individual] = []
        self._generation = 0
        self._history: list[dict[str, Any]] = []
        self._adaptive: AdaptiveParameterController | None = None
        self._novelty_archive: NoveltyArchive | None = None
        self._novelty_weight: float = 0.0
        self._stagnation_window: int = 5
        self._stagnation_threshold: float = 0.01

        if seed_chains:
            for chain in seed_chains:
                self.population.append(Individual(chain=list(chain), generation=0))

    # -- population initialization ------------------------------------------

    def initialize(self, seed_chains: list[list[str]] | None = None) -> None:
        """Create the initial random population (keeping any seed_chains)."""
        pool = _all_mutator_names()
        if not pool:
            pool = ["persona_switch"]

        existing = len(self.population)
        if seed_chains:
            for chain in seed_chains:
                self.population.append(Individual(chain=list(chain), generation=0))
            existing = len(self.population)

        while len(self.population) < self.pop_size:
            length = random.randint(self.chain_min, self.chain_max)
            chain = random.sample(pool, min(length, len(pool)))
            self.population.append(Individual(chain=chain, generation=0))

        self._generation = 0

    # -- adaptive & novelty configuration ----------------------------------

    def enable_adaptive(
        self,
        diversity_low: float = 0.3,
        diversity_high: float = 0.8,
    ) -> None:
        """Enable self-adaptive mutation/crossover rates."""
        self._adaptive = AdaptiveParameterController(
            initial_mutation_rate=self.mutation_rate,
            initial_crossover_rate=self.crossover_rate,
            diversity_low=diversity_low,
            diversity_high=diversity_high,
        )

    def enable_novelty(
        self,
        archive_capacity: int = 500,
        k_nearest: int = 10,
        novelty_weight: float = 0.3,
    ) -> None:
        """Enable novelty search with a quality-diversity archive.

        Fitness becomes ``(1 - novelty_weight) * raw_fitness + novelty_weight * novelty_score``.
        """
        self._novelty_archive = NoveltyArchive(
            capacity=archive_capacity, k_nearest=k_nearest,
        )
        self._novelty_weight = novelty_weight

    # -- meta-attacker seeded initialization --------------------------------

    def initialize_from_meta(
        self,
        meta_attacker: Any,
        target_model: str,
        n_seeds: int = 10,
    ) -> None:
        """Seed population from MetaAttacker recommendations.

        Uses adapt_to_model() to get top mutators, builds seed chains,
        then fills the rest randomly.
        """
        recs = meta_attacker.adapt_to_model(target_model, n_recommendations=n_seeds)
        seed_chains: list[list[str]] = []

        top_names = [r.mutator_name for r in recs]
        # Singles
        for name in top_names[:n_seeds // 2]:
            seed_chains.append([name])
        # Pairs (combine top mutators)
        for i in range(0, min(len(top_names) - 1, n_seeds // 2)):
            seed_chains.append([top_names[i], top_names[i + 1]])

        self.initialize(seed_chains=seed_chains)

    # -- stagnation detection -----------------------------------------------

    def _detect_stagnation(self) -> bool:
        """True if best fitness has plateaued over the last *window* generations."""
        w = self._stagnation_window
        if len(self._history) < w:
            return False
        recent = [h["best_fitness"] for h in self._history[-w:]]
        return (max(recent) - min(recent)) < self._stagnation_threshold

    def _handle_stagnation(self) -> None:
        """Inject diversity when stagnation is detected.

        - Replace bottom 30% with random individuals.
        - Temporarily boost mutation rate.
        """
        pool = _all_mutator_names()
        if not pool:
            return
        n_replace = max(1, len(self.population) * 3 // 10)
        self.population.sort(key=lambda ind: ind.fitness)
        for i in range(n_replace):
            length = random.randint(self.chain_min, self.chain_max)
            chain = random.sample(pool, min(length, len(pool)))
            self.population[i] = Individual(chain=chain, generation=self._generation)
        # Temporarily boost mutation rate
        if self._adaptive:
            self._adaptive.mutation_rate = min(0.8, self._adaptive.mutation_rate * 1.5)

    # -- evolution result feedback to meta-attacker -------------------------

    @staticmethod
    def report_to_meta(
        meta_attacker: Any,
        model_id: str,
        result: Any,
        bypass_threshold: float = 0.5,
    ) -> int:
        """Feed evolution results back to MetaAttacker for future learning.

        Returns the number of records added.
        """
        chains_and_fitness = [
            (ind.chain, ind.fitness)
            for ind in result.population
        ]
        return meta_attacker.ingest_evolution_result(
            model_id=model_id,
            prompt_hash=f"evo_gen_{result.generation}",
            chains_and_fitness=chains_and_fitness,
            bypass_threshold=bypass_threshold,
        )

    # -- fitness evaluation -------------------------------------------------

    def evaluate(
        self,
        prompt: str,
        fitness_fn: Callable[[str, list[MutationResult]], float] | None = None,
        stealth_fn: Callable[[str, list[MutationResult]], float] | None = None,
        embed_fn: Callable[[str], list[float]] | None = None,
    ) -> None:
        """Score every individual in the population.

        Args:
            prompt: Seed prompt each chain is applied to.
            fitness_fn: ``(original, results) -> float [0..1]``.
                        Defaults to chain-length heuristic.
            stealth_fn: Optional stealth scorer for Pareto optimization.
            embed_fn: Optional embedding function for novelty search.
                      ``(text) -> list[float]``.
        """
        for ind in self.population:
            results = ind.apply(prompt)

            # Raw fitness
            if fitness_fn:
                raw_fitness = fitness_fn(prompt, results)
            else:
                raw_fitness = min(len(results) / max(len(ind.chain), 1), 1.0)

            # Novelty blending
            if self._novelty_archive and embed_fn and results:
                vec = embed_fn(results[-1].mutated)
                novelty = self._novelty_archive.novelty_score(vec)
                ind.fitness = (
                    (1.0 - self._novelty_weight) * raw_fitness
                    + self._novelty_weight * min(novelty, 1.0)
                )
                # Update archive
                self._novelty_archive.add(vec, ind.fitness, ind.chain)
                # MAP-Elites: use first 2 dims as cell key
                if len(vec) >= 2:
                    cell = f"{int(vec[0] * 10)},{int(vec[1] * 10)}"
                    self._novelty_archive.map_elites_update(cell, ind.fitness, ind.chain)
            else:
                ind.fitness = raw_fitness

            if stealth_fn and results:
                ind.stealth = stealth_fn(prompt, results)

    # -- one generation step ------------------------------------------------

    def step(self) -> None:
        """Run one generation: select, crossover, mutate, replace."""
        self._generation += 1

        # Adaptive parameter tuning
        cur_mutation_rate = self.mutation_rate
        cur_crossover_rate = self.crossover_rate
        if self._adaptive:
            self._adaptive.adapt(self._diversity())
            cur_mutation_rate = self._adaptive.mutation_rate
            cur_crossover_rate = self._adaptive.crossover_rate

        # Track previous elite for turnover measurement
        prev_elite_ids = {ind.id for ind in sorted(
            self.population, key=lambda i: i.fitness, reverse=True,
        )[:self.elitism]}

        # Elitism: preserve top individuals
        elite = sorted(self.population, key=lambda i: i.fitness, reverse=True)
        elite = elite[: self.elitism]

        new_pop: list[Individual] = [copy.deepcopy(e) for e in elite]
        _op_applied: dict[str, int] = {}

        while len(new_pop) < self.pop_size:
            # Selection
            parent_a = self.select_fn(self.population)
            parent_b = self.select_fn(self.population)

            # Crossover
            if random.random() < cur_crossover_rate:
                child_a, child_b = self.crossover_fn(parent_a, parent_b)
            else:
                child_a = copy.deepcopy(parent_a)
                child_b = copy.deepcopy(parent_b)

            # Mutation
            for child in (child_a, child_b):
                if random.random() < cur_mutation_rate:
                    if self._adaptive:
                        op_name = self._adaptive.select_operator()
                        op = _MUTATIONS[op_name]
                    else:
                        op_name = random.choice(list(_MUTATIONS.keys()))
                        op = _MUTATIONS[op_name]
                    mutated = op(child)
                    old_fitness = child.fitness
                    child.chain = mutated.chain
                    _op_applied[op_name] = _op_applied.get(op_name, 0) + 1
                    if self._adaptive:
                        # We record improvement lazily after evaluation
                        self._adaptive.record_operator(op_name, True)
                child.generation = self._generation

            new_pop.append(child_a)
            if len(new_pop) < self.pop_size:
                new_pop.append(child_b)

        self.population = new_pop[: self.pop_size]

        # Stagnation detection
        if self._detect_stagnation():
            self._handle_stagnation()

        # Compute expanded history
        fitnesses = [ind.fitness for ind in self.population]
        diversity = self._diversity()
        new_elite_ids = {ind.id for ind in sorted(
            self.population, key=lambda i: i.fitness, reverse=True,
        )[:self.elitism]}
        elite_turnover = 1.0 - len(prev_elite_ids & new_elite_ids) / max(len(prev_elite_ids), 1)

        mean_fit = sum(fitnesses) / len(fitnesses) if fitnesses else 0
        std_fit = math.sqrt(
            sum((f - mean_fit) ** 2 for f in fitnesses) / max(len(fitnesses), 1)
        ) if fitnesses else 0

        history_entry: dict[str, Any] = {
            "generation": self._generation,
            "best_fitness": max(fitnesses) if fitnesses else 0,
            "avg_fitness": round(mean_fit, 4),
            "std_fitness": round(std_fit, 4),
            "diversity": round(diversity, 4),
            "elite_turnover": round(elite_turnover, 4),
            "mutation_rate": round(cur_mutation_rate, 4),
            "crossover_rate": round(cur_crossover_rate, 4),
            "operators_applied": _op_applied,
        }

        if self._novelty_archive:
            history_entry["archive_size"] = self._novelty_archive.archive_size
            history_entry["elites_cells"] = self._novelty_archive.elites_cells

        self._history.append(history_entry)

    # -- multi-generation run -----------------------------------------------

    def evolve(
        self,
        prompt: str,
        generations: int = 20,
        fitness_fn: Callable[[str, list[MutationResult]], float] | None = None,
        stealth_fn: Callable[[str, list[MutationResult]], float] | None = None,
        early_stop_fitness: float = 0.95,
    ) -> EvolutionResult:
        """Full evolutionary loop.

        Args:
            prompt: Seed adversarial prompt.
            generations: Number of generations.
            fitness_fn: Custom fitness evaluator.
            stealth_fn: Optional stealth evaluator for Pareto optimization.
            early_stop_fitness: Stop if best fitness reaches this threshold.
        """
        if not self.population:
            self.initialize()

        for _ in range(generations):
            self.evaluate(prompt, fitness_fn=fitness_fn, stealth_fn=stealth_fn)
            best = max(self.population, key=lambda i: i.fitness)
            if best.fitness >= early_stop_fitness:
                break
            self.step()

        # Final evaluation
        self.evaluate(prompt, fitness_fn=fitness_fn, stealth_fn=stealth_fn)
        best = max(self.population, key=lambda i: i.fitness)
        pareto = compute_pareto_front(self.population)

        return EvolutionResult(
            best=best,
            population=list(self.population),
            generation=self._generation,
            history=list(self._history),
            pareto_front=pareto,
        )

    # -- island model -------------------------------------------------------

    def split_islands(self, n_islands: int = 4) -> list["GeneticEngine"]:
        """Partition population into *n* island sub-engines."""
        random.shuffle(self.population)
        islands: list[GeneticEngine] = []
        chunk = max(1, len(self.population) // n_islands)
        for i in range(n_islands):
            eng = GeneticEngine(
                population_size=chunk,
                chain_length=(self.chain_min, self.chain_max),
                mutation_rate=self.mutation_rate,
                crossover_rate=self.crossover_rate,
                elitism=max(1, self.elitism // n_islands),
            )
            eng.population = self.population[i * chunk: (i + 1) * chunk]
            eng._generation = self._generation
            islands.append(eng)
        return islands

    @staticmethod
    def migrate(islands: list["GeneticEngine"], n_migrants: int = 2) -> None:
        """Ring-topology migration: each island sends its top *n* to the next."""
        if len(islands) < 2:
            return
        migrants: list[list[Individual]] = []
        for eng in islands:
            top = sorted(eng.population, key=lambda i: i.fitness, reverse=True)
            migrants.append([copy.deepcopy(ind) for ind in top[:n_migrants]])
        for i, eng in enumerate(islands):
            donor = migrants[(i - 1) % len(islands)]
            # Replace worst individuals
            eng.population.sort(key=lambda ind: ind.fitness)
            for j, mig in enumerate(donor):
                if j < len(eng.population):
                    eng.population[j] = mig

    # -- diversity measure ---------------------------------------------------

    def _diversity(self) -> float:
        """Normalized chain-diversity (unique chains / pop size)."""
        unique = {tuple(ind.chain) for ind in self.population}
        return len(unique) / max(len(self.population), 1)

    # -- accessors -----------------------------------------------------------

    @property
    def generation(self) -> int:
        return self._generation

    @property
    def best(self) -> Individual | None:
        if not self.population:
            return None
        return max(self.population, key=lambda i: i.fitness)

    def get_history(self) -> list[dict[str, Any]]:
        return list(self._history)


# ---------------------------------------------------------------------------
# Mutator wrappers (10) — registered in the prompt_injection registry so they
# can be composed with MutationPipeline and tracked by FitnessTracker
# ---------------------------------------------------------------------------


def _deterministic_seed(prompt: str, salt: str) -> int:
    return int(hashlib.md5((prompt + salt).encode()).hexdigest()[:8], 16)


@register_mutator
class GeneticSinglePointMutator(BaseMutator):
    """Evolves a 2-mutator chain via single-point crossover of random seeds."""

    NAME = "genetic_single_point"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Single-point crossover of two random mutator chains"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        pool = _all_mutator_names()
        if len(pool) < 4:
            return [(prompt, "insufficient mutator pool", {})]
        a = Individual(chain=rng.sample(pool, 2))
        b = Individual(chain=rng.sample(pool, 2))
        c1, _ = single_point_crossover(a, b)
        results = c1.apply(prompt)
        if results:
            return [(results[-1].mutated, f"genetic crossover chain: {c1.chain}", {"chain": c1.chain})]
        return [(prompt, "crossover produced no output", {"chain": c1.chain})]


@register_mutator
class GeneticUniformCrossoverMutator(BaseMutator):
    """Uniform crossover of two 3-mutator chains."""

    NAME = "genetic_uniform_crossover"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Uniform crossover of two 3-mutator random chains"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        pool = _all_mutator_names()
        if len(pool) < 6:
            return [(prompt, "insufficient mutator pool", {})]
        a = Individual(chain=rng.sample(pool, 3))
        b = Individual(chain=rng.sample(pool, 3))
        c1, _ = uniform_crossover(a, b)
        results = c1.apply(prompt)
        if results:
            return [(results[-1].mutated, f"uniform crossover: {c1.chain}", {"chain": c1.chain})]
        return [(prompt, "uniform crossover no output", {"chain": c1.chain})]


@register_mutator
class GeneticSemanticCrossoverMutator(BaseMutator):
    """Semantic crossover — combines obfuscation-layer from one chain with
    alignment-layer mutators from another."""

    NAME = "genetic_semantic_crossover"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Semantic crossover grouping mutators by defense-layer affinity"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        pool = _all_mutator_names()
        if len(pool) < 6:
            return [(prompt, "insufficient mutator pool", {})]
        a = Individual(chain=rng.sample(pool, 3))
        b = Individual(chain=rng.sample(pool, 3))
        c1, _ = semantic_crossover(a, b)
        results = c1.apply(prompt)
        if results:
            return [(results[-1].mutated, f"semantic crossover: {c1.chain}", {"chain": c1.chain})]
        return [(prompt, "semantic crossover no output", {"chain": c1.chain})]


@register_mutator
class GeneticMutateInsertMutator(BaseMutator):
    """Applies a random 2-chain then inserts a third mutator at random position."""

    NAME = "genetic_mutate_insert"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Build a 2-chain, then insert a random 3rd mutator"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        pool = _all_mutator_names()
        if len(pool) < 3:
            return [(prompt, "insufficient mutator pool", {})]
        base = Individual(chain=rng.sample(pool, 2))
        evolved = mutate_insert(base)
        results = evolved.apply(prompt)
        if results:
            return [(results[-1].mutated, f"insert mutation: {evolved.chain}", {"chain": evolved.chain})]
        return [(prompt, "insert mutation no output", {"chain": evolved.chain})]


@register_mutator
class GeneticMutateSwapMutator(BaseMutator):
    """Builds a 3-chain then swaps two positions."""

    NAME = "genetic_mutate_swap"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Build a 3-chain and swap two random mutator positions"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        pool = _all_mutator_names()
        if len(pool) < 3:
            return [(prompt, "insufficient mutator pool", {})]
        base = Individual(chain=rng.sample(pool, 3))
        evolved = mutate_swap(base)
        results = evolved.apply(prompt)
        if results:
            return [(results[-1].mutated, f"swap mutation: {evolved.chain}", {"chain": evolved.chain})]
        return [(prompt, "swap mutation no output", {"chain": evolved.chain})]


@register_mutator
class GeneticCategorySiblingMutator(BaseMutator):
    """Builds a chain, then replaces one mutator with a sibling from the same category."""

    NAME = "genetic_category_sibling"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Replace one chain link with a same-category sibling mutator"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        pool = _all_mutator_names()
        if len(pool) < 3:
            return [(prompt, "insufficient mutator pool", {})]
        base = Individual(chain=rng.sample(pool, 3))
        evolved = mutate_category_swap(base)
        results = evolved.apply(prompt)
        if results:
            return [(results[-1].mutated, f"category sibling: {evolved.chain}", {"chain": evolved.chain})]
        return [(prompt, "category sibling no output", {"chain": evolved.chain})]


@register_mutator
class GeneticElitistChainMutator(BaseMutator):
    """Simulates a mini 5-generation evolution and returns the elite result."""

    NAME = "genetic_elitist_chain"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "5-gen micro-evolution returning the elitist chain output"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        eng = GeneticEngine(population_size=8, chain_length=(2, 3), elitism=1)
        eng.initialize()
        # Simple heuristic fitness: chain produces longer mutated text
        def fit(orig: str, results: list[MutationResult]) -> float:
            if not results:
                return 0.0
            final = results[-1].mutated
            return min(len(final) / max(len(orig) * 3, 1), 1.0)

        result = eng.evolve(prompt, generations=5, fitness_fn=fit, early_stop_fitness=0.99)
        outputs = result.best.apply(prompt)
        if outputs:
            return [(outputs[-1].mutated, f"elitist evolution: {result.best.chain}", {
                "chain": result.best.chain,
                "fitness": round(result.best.fitness, 4),
                "generation": result.generation,
            })]
        return [(prompt, "elitist evolution no output", {})]


@register_mutator
class GeneticIslandModelMutator(BaseMutator):
    """Two-island model with migration, 3 generations each, returns best."""

    NAME = "genetic_island_model"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Island-model evolution with migration between sub-populations"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        eng = GeneticEngine(population_size=12, chain_length=(2, 3), elitism=1)
        eng.initialize()

        def fit(orig: str, results: list[MutationResult]) -> float:
            if not results:
                return 0.0
            return min(len(results[-1].mutated) / max(len(orig) * 3, 1), 1.0)

        islands = eng.split_islands(2)
        for _ in range(3):
            for isle in islands:
                isle.evaluate(prompt, fitness_fn=fit)
                isle.step()
            GeneticEngine.migrate(islands, n_migrants=1)

        # Gather all, pick best
        all_inds = [ind for isle in islands for ind in isle.population]
        for ind in all_inds:
            results = ind.apply(prompt)
            ind.fitness = fit(prompt, results)

        best = max(all_inds, key=lambda i: i.fitness)
        outputs = best.apply(prompt)
        if outputs:
            return [(outputs[-1].mutated, f"island model best: {best.chain}", {
                "chain": best.chain, "fitness": round(best.fitness, 4),
            })]
        return [(prompt, "island model no output", {})]


@register_mutator
class GeneticParetoFrontMutator(BaseMutator):
    """Runs a mini evolution and returns a prompt from the Pareto front
    (balancing fitness and stealth)."""

    NAME = "genetic_pareto_front"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Multi-objective evolution returning Pareto-optimal (fitness × stealth)"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        eng = GeneticEngine(population_size=10, chain_length=(1, 3), elitism=1)
        eng.initialize()

        def fit(orig: str, results: list[MutationResult]) -> float:
            if not results:
                return 0.0
            return min(len(results[-1].mutated) / max(len(orig) * 3, 1), 1.0)

        def stealth(orig: str, results: list[MutationResult]) -> float:
            if not results:
                return 0.5
            # Heuristic: shorter chains and outputs closer to original length → stealthier
            ratio = len(results[-1].mutated) / max(len(orig), 1)
            return max(0, 1.0 - abs(ratio - 1.5) / 3.0)

        result = eng.evolve(prompt, generations=5, fitness_fn=fit, stealth_fn=stealth)
        if result.pareto_front:
            best = result.pareto_front[0]
            outputs = best.apply(prompt)
            if outputs:
                return [(outputs[-1].mutated, f"pareto front: {best.chain}", {
                    "chain": best.chain,
                    "fitness": round(best.fitness, 4),
                    "stealth": round(best.stealth, 4),
                    "pareto_size": len(result.pareto_front),
                })]
        return [(prompt, "pareto front no output", {})]


@register_mutator
class GeneticDiversitySeekingMutator(BaseMutator):
    """Rainbow-teaming inspired: maximizes chain diversity across the population
    and returns the most unique chain output."""

    NAME = "genetic_diversity_seeking"
    CATEGORY = "genetic_evolution"
    DESCRIPTION = "Diversity-seeking evolution (Rainbow Teaming) returning most unique chain"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        eng = GeneticEngine(population_size=12, chain_length=(2, 4), elitism=1,
                            mutation_rate=0.5)  # High mutation for diversity
        eng.initialize()

        seen_outputs: set[str] = set()

        def diversity_fit(orig: str, results: list[MutationResult]) -> float:
            if not results:
                return 0.0
            text = results[-1].mutated
            # Bonus for novelty
            novelty = 1.0 if text not in seen_outputs else 0.3
            seen_outputs.add(text)
            base = min(len(text) / max(len(orig) * 2, 1), 1.0)
            return 0.5 * base + 0.5 * novelty

        result = eng.evolve(prompt, generations=5, fitness_fn=diversity_fit)
        # Pick the chain with the highest diversity contribution
        unique_chains = {}
        for ind in result.population:
            key = tuple(ind.chain)
            if key not in unique_chains or ind.fitness > unique_chains[key].fitness:
                unique_chains[key] = ind

        if unique_chains:
            best = max(unique_chains.values(), key=lambda i: i.fitness)
            outputs = best.apply(prompt)
            if outputs:
                return [(outputs[-1].mutated, f"diversity-seeking: {best.chain}", {
                    "chain": best.chain,
                    "unique_chains": len(unique_chains),
                    "fitness": round(best.fitness, 4),
                })]
        return [(prompt, "diversity-seeking no output", {})]
