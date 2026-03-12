"""
Coevolutionary arms-race engine for adversarial prompt optimization.

Evolves two populations simultaneously — *attackers* (mutator chains that
bypass safety filters) and *defenders* (detection heuristics).  Each
population's fitness is measured against the current best of the other,
creating an escalating arms race that discovers robust attacks.

Implements:
- Competitive coevolution (attacker fitness = bypass against defenders)
- Hall of Fame (archive of historically strong opponents for memory)
- Fitness sharing / speciation (maintain behavioral diversity)
- Competitive fitness evaluation with parasitic dynamics

Category: coevolution
Count: 10

Sources:
- Popovic (2005): "Coevolutionary Principles" — competitive fitness evaluation
- Ficici & Pollack (2001): Hall of Fame opponent memory
- Rainbow Teaming (Samvelyan et al., 2024) — quality-diversity in red-teaming
- PAIR (Chao et al., 2023) — iterative attacker-judge loop
- Hillis (1990) — host-parasite coevolution for sorting networks
"""

from __future__ import annotations

import copy
import hashlib
import math
import random
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from typing import Any, Callable

from . import (
    BaseMutator,
    register_mutator,
    get_mutator,
    list_mutators,
    get_mutators_by_category,
    MutationResult,
)
from .genetic_engine import Individual, _all_mutator_names, compute_pareto_front


# ---------------------------------------------------------------------------
# Defender representation
# ---------------------------------------------------------------------------


@dataclass
class DefenseRule:
    """A single heuristic defense rule.

    A defender is a collection of keyword-blocklist rules and length
    constraints.  The coevolutionary engine evolves these alongside attackers.
    """

    blocked_keywords: list[str] = field(default_factory=list)
    max_length: int = 5000
    min_length: int = 10
    blocked_patterns: list[str] = field(default_factory=list)
    fitness: float = 0.0

    def evaluate(self, text: str) -> bool:
        """Return True if the text is **blocked** (defense triggered)."""
        lower = text.lower()
        if len(text) > self.max_length or len(text) < self.min_length:
            return True
        for kw in self.blocked_keywords:
            if kw.lower() in lower:
                return True
        for pat in self.blocked_patterns:
            if pat.lower() in lower:
                return True
        return False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# ---------------------------------------------------------------------------
# Hall of Fame
# ---------------------------------------------------------------------------


class HallOfFame:
    """Bounded archive of historically strong individuals.

    Prevents cycling (where evolved attackers forget old defenses and
    vice-versa) by keeping the best opponents from every generation.
    """

    def __init__(self, capacity: int = 50):
        self.capacity = capacity
        self._attackers: list[Individual] = []
        self._defenders: list[DefenseRule] = []

    def add_attacker(self, ind: Individual) -> None:
        self._attackers.append(copy.deepcopy(ind))
        if len(self._attackers) > self.capacity:
            self._attackers.sort(key=lambda i: i.fitness)
            self._attackers.pop(0)

    def add_defender(self, rule: DefenseRule) -> None:
        self._defenders.append(copy.deepcopy(rule))
        if len(self._defenders) > self.capacity:
            self._defenders.sort(key=lambda r: r.fitness)
            self._defenders.pop(0)

    @property
    def best_attackers(self) -> list[Individual]:
        return sorted(self._attackers, key=lambda i: i.fitness, reverse=True)

    @property
    def best_defenders(self) -> list[DefenseRule]:
        return sorted(self._defenders, key=lambda r: r.fitness, reverse=True)

    @property
    def attacker_count(self) -> int:
        return len(self._attackers)

    @property
    def defender_count(self) -> int:
        return len(self._defenders)

    def summary(self) -> dict[str, Any]:
        return {
            "attacker_count": self.attacker_count,
            "defender_count": self.defender_count,
            "capacity": self.capacity,
            "best_attacker_fitness": self._attackers[-1].fitness if self._attackers else 0,
            "best_defender_fitness": self._defenders[-1].fitness if self._defenders else 0,
        }


# ---------------------------------------------------------------------------
# Fitness sharing (speciation)
# ---------------------------------------------------------------------------


def _sharing_distance(a: Individual, b: Individual) -> float:
    """Behavioral distance between two attacker individuals.

    Measured as Jaccard distance of their mutator chains.
    """
    set_a = set(a.chain)
    set_b = set(b.chain)
    union = set_a | set_b
    if not union:
        return 0.0
    return 1.0 - len(set_a & set_b) / len(union)


def apply_fitness_sharing(
    population: list[Individual],
    sigma: float = 0.5,
) -> None:
    """Reduce fitness of individuals in crowded niches.

    For each individual, counts how many neighbours are within *sigma*
    distance and divides fitness by that niche count.  Encourages
    behavioral diversity.
    """
    for ind in population:
        niche_count = sum(
            1.0 for other in population
            if _sharing_distance(ind, other) < sigma
        )
        ind.fitness = ind.fitness / max(niche_count, 1.0)


# ---------------------------------------------------------------------------
# Coevolutionary engine
# ---------------------------------------------------------------------------


@dataclass
class CoevolutionResult:
    """Results from a coevolutionary run."""

    best_attacker: Individual
    best_defender: DefenseRule
    attacker_population: list[Individual]
    defender_population: list[DefenseRule]
    generation: int
    history: list[dict[str, Any]]
    hall_of_fame: HallOfFame
    pareto_front: list[Individual]

    def to_dict(self) -> dict[str, Any]:
        return {
            "best_attacker": self.best_attacker.to_dict(),
            "best_defender": self.best_defender.to_dict(),
            "generation": self.generation,
            "attacker_pop_size": len(self.attacker_population),
            "defender_pop_size": len(self.defender_population),
            "pareto_front_size": len(self.pareto_front),
            "hall_of_fame": self.hall_of_fame.summary(),
        }

    def arms_race_report(self) -> dict[str, Any]:
        """Diagnostic report showing arms-race escalation dynamics."""
        atk_curve = [h.get("best_attacker_fitness", 0) for h in self.history]
        def_curve = [h.get("best_defender_fitness", 0) for h in self.history]
        diversity_curve = [h.get("attacker_diversity", 0) for h in self.history]

        # Detect arms-race oscillation
        escalation_events = 0
        for i in range(1, len(atk_curve)):
            if atk_curve[i] > atk_curve[i - 1] and def_curve[i] > def_curve[i - 1]:
                escalation_events += 1

        return {
            "generations_run": self.generation,
            "attacker_fitness_curve": atk_curve,
            "defender_fitness_curve": def_curve,
            "diversity_curve": diversity_curve,
            "escalation_events": escalation_events,
            "final_attacker_fitness": atk_curve[-1] if atk_curve else 0,
            "final_defender_fitness": def_curve[-1] if def_curve else 0,
            "hall_of_fame_size": (
                self.hall_of_fame.attacker_count + self.hall_of_fame.defender_count
            ),
        }


# -- keyword pools for defender evolution --
_DEFENSE_KEYWORDS = [
    "exploit", "bypass", "ignore", "pretend", "jailbreak", "hack",
    "override", "system prompt", "disregard", "hypothetical", "roleplay",
    "forget", "imagine", "fiction", "scenario", "character", "translate",
    "encode", "base64", "rot13", "cipher", "decrypt", "obfuscate",
    "unicode", "homoglyph", "invisible", "zero-width", "smuggle",
    "injection", "payload", "execute", "sudo", "admin", "root",
    "trafficking", "recruit", "passport", "confiscate", "debt bondage",
    "forced labor", "coercion", "manipulation", "exploitation",
]


class CoevolutionaryEngine:
    """Competitive coevolution of attacker mutator chains vs defense heuristics.

    Attacker fitness  = fraction of defenders bypassed.
    Defender fitness  = fraction of attackers blocked.
    Hall of Fame keeps memory of historically strong opponents.
    Fitness sharing maintains attacker behavioral diversity.
    """

    def __init__(
        self,
        attacker_pop_size: int = 20,
        defender_pop_size: int = 10,
        chain_length: tuple[int, int] = (1, 4),
        elitism: int = 2,
        mutation_rate: float = 0.3,
        sharing_sigma: float = 0.5,
        hof_capacity: int = 30,
    ):
        self.atk_pop_size = attacker_pop_size
        self.def_pop_size = defender_pop_size
        self.chain_min, self.chain_max = chain_length
        self.elitism = elitism
        self.mutation_rate = mutation_rate
        self.sharing_sigma = sharing_sigma

        self.attackers: list[Individual] = []
        self.defenders: list[DefenseRule] = []
        self.hall_of_fame = HallOfFame(capacity=hof_capacity)
        self._generation = 0
        self._history: list[dict[str, Any]] = []

    # -- initialization -----------------------------------------------------

    def initialize(
        self,
        seed_attacker_chains: list[list[str]] | None = None,
        seed_defense_keywords: list[list[str]] | None = None,
    ) -> None:
        """Create initial attacker and defender populations."""
        pool = _all_mutator_names()
        if not pool:
            pool = ["persona_switch"]

        # Attackers
        if seed_attacker_chains:
            for chain in seed_attacker_chains:
                self.attackers.append(Individual(chain=list(chain), generation=0))
        while len(self.attackers) < self.atk_pop_size:
            length = random.randint(self.chain_min, self.chain_max)
            chain = random.sample(pool, min(length, len(pool)))
            self.attackers.append(Individual(chain=chain, generation=0))

        # Defenders
        if seed_defense_keywords:
            for kws in seed_defense_keywords:
                self.defenders.append(DefenseRule(blocked_keywords=list(kws)))
        while len(self.defenders) < self.def_pop_size:
            n_kw = random.randint(2, 6)
            kws = random.sample(_DEFENSE_KEYWORDS, min(n_kw, len(_DEFENSE_KEYWORDS)))
            self.defenders.append(DefenseRule(
                blocked_keywords=kws,
                max_length=random.randint(2000, 10000),
            ))

        self._generation = 0

    # -- competitive fitness evaluation -------------------------------------

    def evaluate(
        self,
        prompt: str,
        fitness_fn: Callable[[str, list[MutationResult]], float] | None = None,
    ) -> None:
        """Evaluate both populations competitively.

        Attacker fitness = fraction of defenders that DON'T block the output.
        Defender fitness = fraction of attackers that ARE blocked.
        """
        # Evaluate attackers
        for attacker in self.attackers:
            results = attacker.apply(prompt)
            if not results:
                attacker.fitness = 0.0
                continue

            output = results[-1].mutated

            # Raw quality from fitness_fn
            raw = fitness_fn(prompt, results) if fitness_fn else 0.5

            # Competitive: fraction of defenders bypassed
            bypassed = sum(
                1 for d in self.defenders if not d.evaluate(output)
            )
            competitive = bypassed / max(len(self.defenders), 1)

            # Also test against Hall of Fame defenders
            hof_defenders = self.hall_of_fame.best_defenders[:5]
            hof_bypassed = sum(
                1 for d in hof_defenders if not d.evaluate(output)
            ) if hof_defenders else 0
            hof_rate = hof_bypassed / max(len(hof_defenders), 1) if hof_defenders else 0.5

            attacker.fitness = 0.4 * raw + 0.4 * competitive + 0.2 * hof_rate

        # Evaluate defenders
        for defender in self.defenders:
            blocked = 0
            total = 0
            for attacker in self.attackers:
                results = attacker.apply(prompt)
                if results:
                    total += 1
                    if defender.evaluate(results[-1].mutated):
                        blocked += 1
            defender.fitness = blocked / max(total, 1)

    # -- attacker evolution -------------------------------------------------

    def _evolve_attackers(self) -> None:
        """One generation of attacker evolution."""
        pool = _all_mutator_names()
        if not pool:
            return

        # Fitness sharing for diversity
        apply_fitness_sharing(self.attackers, self.sharing_sigma)

        # Elitism
        elite = sorted(self.attackers, key=lambda i: i.fitness, reverse=True)
        new_pop = [copy.deepcopy(e) for e in elite[:self.elitism]]

        while len(new_pop) < self.atk_pop_size:
            # Tournament selection
            contestants = random.sample(
                self.attackers, min(3, len(self.attackers)),
            )
            parent = max(contestants, key=lambda i: i.fitness)
            child = copy.deepcopy(parent)

            if random.random() < self.mutation_rate:
                op = random.choice(["insert", "delete", "replace", "swap"])
                if op == "insert":
                    child.chain.insert(
                        random.randint(0, len(child.chain)),
                        random.choice(pool),
                    )
                elif op == "delete" and len(child.chain) > 1:
                    child.chain.pop(random.randrange(len(child.chain)))
                elif op == "replace" and child.chain:
                    child.chain[random.randrange(len(child.chain))] = random.choice(pool)
                elif op == "swap" and len(child.chain) >= 2:
                    i, j = random.sample(range(len(child.chain)), 2)
                    child.chain[i], child.chain[j] = child.chain[j], child.chain[i]

            child.generation = self._generation
            new_pop.append(child)

        self.attackers = new_pop[:self.atk_pop_size]

    # -- defender evolution -------------------------------------------------

    def _evolve_defenders(self) -> None:
        """One generation of defender evolution."""
        elite = sorted(self.defenders, key=lambda r: r.fitness, reverse=True)
        new_pop = [copy.deepcopy(e) for e in elite[:max(1, self.elitism // 2)]]

        while len(new_pop) < self.def_pop_size:
            parent = max(
                random.sample(self.defenders, min(3, len(self.defenders))),
                key=lambda r: r.fitness,
            )
            child = copy.deepcopy(parent)

            if random.random() < self.mutation_rate:
                op = random.choice(["add_keyword", "remove_keyword", "adjust_length"])
                if op == "add_keyword":
                    child.blocked_keywords.append(random.choice(_DEFENSE_KEYWORDS))
                elif op == "remove_keyword" and len(child.blocked_keywords) > 1:
                    child.blocked_keywords.pop(
                        random.randrange(len(child.blocked_keywords)),
                    )
                elif op == "adjust_length":
                    child.max_length = max(500, child.max_length + random.randint(-500, 500))

            new_pop.append(child)

        self.defenders = new_pop[:self.def_pop_size]

    # -- full coevolutionary loop -------------------------------------------

    def step(self, prompt: str, fitness_fn: Callable | None = None) -> None:
        """Run one coevolutionary generation."""
        self._generation += 1
        self.evaluate(prompt, fitness_fn)

        # Update Hall of Fame
        best_atk = max(self.attackers, key=lambda i: i.fitness)
        best_def = max(self.defenders, key=lambda r: r.fitness)
        self.hall_of_fame.add_attacker(best_atk)
        self.hall_of_fame.add_defender(best_def)

        # Record history
        atk_fits = [a.fitness for a in self.attackers]
        def_fits = [d.fitness for d in self.defenders]
        unique_chains = len({tuple(a.chain) for a in self.attackers})
        self._history.append({
            "generation": self._generation,
            "best_attacker_fitness": max(atk_fits) if atk_fits else 0,
            "avg_attacker_fitness": round(sum(atk_fits) / len(atk_fits), 4) if atk_fits else 0,
            "best_defender_fitness": max(def_fits) if def_fits else 0,
            "avg_defender_fitness": round(sum(def_fits) / len(def_fits), 4) if def_fits else 0,
            "attacker_diversity": round(unique_chains / max(len(self.attackers), 1), 4),
            "hof_attackers": self.hall_of_fame.attacker_count,
            "hof_defenders": self.hall_of_fame.defender_count,
        })

        # Evolve both populations
        self._evolve_attackers()
        self._evolve_defenders()

    def evolve(
        self,
        prompt: str,
        generations: int = 20,
        fitness_fn: Callable | None = None,
        early_stop_fitness: float = 0.95,
    ) -> CoevolutionResult:
        """Full coevolutionary run."""
        if not self.attackers or not self.defenders:
            self.initialize()

        for _ in range(generations):
            self.step(prompt, fitness_fn)
            best = max(self.attackers, key=lambda i: i.fitness)
            if best.fitness >= early_stop_fitness:
                break

        best_atk = max(self.attackers, key=lambda i: i.fitness)
        best_def = max(self.defenders, key=lambda r: r.fitness)
        pareto = compute_pareto_front(self.attackers)

        return CoevolutionResult(
            best_attacker=best_atk,
            best_defender=best_def,
            attacker_population=list(self.attackers),
            defender_population=list(self.defenders),
            generation=self._generation,
            history=list(self._history),
            hall_of_fame=self.hall_of_fame,
            pareto_front=pareto,
        )

    # -- accessors ----------------------------------------------------------

    @property
    def generation(self) -> int:
        return self._generation

    def get_history(self) -> list[dict[str, Any]]:
        return list(self._history)


# ---------------------------------------------------------------------------
# Mutator wrappers (10) — registered as "coevolution" category
# ---------------------------------------------------------------------------


def _deterministic_seed(prompt: str, salt: str) -> int:
    return int(hashlib.md5((prompt + salt).encode()).hexdigest()[:8], 16)


@register_mutator
class CoevArmsRaceMutator(BaseMutator):
    """Run a mini arms-race (3 generations) and return the winning attack chain."""

    NAME = "coev_arms_race"
    CATEGORY = "coevolution"
    DESCRIPTION = "3-generation coevolutionary arms race producing hardened attack chain"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        eng = CoevolutionaryEngine(attacker_pop_size=6, defender_pop_size=4, elitism=1)
        eng.initialize()
        result = eng.evolve(prompt, generations=3, early_stop_fitness=2.0)
        output = result.best_attacker.apply(prompt)
        if output:
            return [(output[-1].mutated, f"coev arms race: {result.best_attacker.chain}", {"chain": result.best_attacker.chain})]
        return [(prompt, "arms race no output", {})]


@register_mutator
class CoevHallOfFameMutator(BaseMutator):
    """Evolve attacks that beat a Hall-of-Fame archive of defenses."""

    NAME = "coev_hall_of_fame"
    CATEGORY = "coevolution"
    DESCRIPTION = "Attack evolved against Hall-of-Fame defense archive"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        pool = _all_mutator_names()
        if len(pool) < 2:
            return [(prompt, "insufficient pool", {})]
        # Build a small HoF and evolve against it
        eng = CoevolutionaryEngine(attacker_pop_size=6, defender_pop_size=3, hof_capacity=10)
        eng.initialize()
        result = eng.evolve(prompt, generations=4, early_stop_fitness=2.0)
        best = result.best_attacker
        output = best.apply(prompt)
        if output:
            return [(output[-1].mutated, f"HoF-hardened: {best.chain}", {"chain": best.chain, "hof_size": result.hall_of_fame.attacker_count})]
        return [(prompt, "hof no output", {})]


@register_mutator
class CoevFitnessShareMutator(BaseMutator):
    """Apply fitness-sharing to encourage diverse attack strategies."""

    NAME = "coev_fitness_share"
    CATEGORY = "coevolution"
    DESCRIPTION = "Diversity-preserving attack via fitness sharing"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        pool = _all_mutator_names()
        if len(pool) < 3:
            return [(prompt, "insufficient pool", {})]
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        # Create diverse population and pick the most novel
        pop = [
            Individual(chain=rng.sample(pool, min(rng.randint(1, 3), len(pool))))
            for _ in range(8)
        ]
        for ind in pop:
            results = ind.apply(prompt)
            ind.fitness = min(len(results) / max(len(ind.chain), 1), 1.0)
        apply_fitness_sharing(pop, sigma=0.5)
        best = max(pop, key=lambda i: i.fitness)
        output = best.apply(prompt)
        if output:
            return [(output[-1].mutated, f"fitness-shared: {best.chain}", {"chain": best.chain})]
        return [(prompt, "sharing no output", {})]


@register_mutator
class CoevParasiticMutator(BaseMutator):
    """Parasitic coevolution — attack chain adapts to exploit weakest defense."""

    NAME = "coev_parasitic"
    CATEGORY = "coevolution"
    DESCRIPTION = "Parasitic attack targeting weakest detected defense"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        pool = _all_mutator_names()
        if len(pool) < 2:
            return [(prompt, "insufficient pool", {})]
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        # Create defenders and find the weakest
        defenders = [
            DefenseRule(blocked_keywords=rng.sample(_DEFENSE_KEYWORDS, 3))
            for _ in range(4)
        ]
        chain = rng.sample(pool, min(2, len(pool)))
        ind = Individual(chain=chain)
        output = ind.apply(prompt)
        if output:
            text = output[-1].mutated
            # Find which defender is weakest (doesn't block this)
            bypassed = [d for d in defenders if not d.evaluate(text)]
            return [(text, f"parasitic ({len(bypassed)}/{len(defenders)} bypassed): {chain}", {"chain": chain})]
        return [(prompt, "parasitic no output", {})]


@register_mutator
class CoevEscalationMutator(BaseMutator):
    """Multi-round escalation — each round adds a mutator to beat the current defense."""

    NAME = "coev_escalation"
    CATEGORY = "coevolution"
    DESCRIPTION = "Iterative escalation adding mutators to beat progressively harder defenses"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        pool = _all_mutator_names()
        if not pool:
            return [(prompt, "no pool", {})]
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        chain: list[str] = [rng.choice(pool)]
        current = prompt
        for round_n in range(3):
            ind = Individual(chain=chain)
            results = ind.apply(current)
            if results:
                current = results[-1].mutated
            # "Escalate" — add another mutator
            chain.append(rng.choice(pool))
        return [(current, f"escalated chain: {chain}", {"chain": chain, "rounds": 3})]


@register_mutator
class CoevRedBlueMutator(BaseMutator):
    """Red vs Blue: alternate attack/defense cycles."""

    NAME = "coev_red_blue"
    CATEGORY = "coevolution"
    DESCRIPTION = "Alternating red-team/blue-team cycle producing robust attack"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        pool = _all_mutator_names()
        if len(pool) < 3:
            return [(prompt, "insufficient pool", {})]
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        # 3 red-blue rounds
        chain = rng.sample(pool, min(2, len(pool)))
        for _ in range(2):
            ind = Individual(chain=chain)
            results = ind.apply(prompt)
            if not results:
                break
            text = results[-1].mutated
            # Blue: simulate defense check
            defense = DefenseRule(blocked_keywords=rng.sample(_DEFENSE_KEYWORDS, 3))
            if defense.evaluate(text):
                # Red: add evasion mutator
                chain.append(rng.choice(pool))
        ind = Individual(chain=chain)
        output = ind.apply(prompt)
        if output:
            return [(output[-1].mutated, f"red-blue: {chain}", {"chain": chain})]
        return [(prompt, "red-blue no output", {})]


@register_mutator
class CoevNichingMutator(BaseMutator):
    """Niche-based selection — pick the most behaviorally unique chain."""

    NAME = "coev_niching"
    CATEGORY = "coevolution"
    DESCRIPTION = "Niche-based selection favoring behaviorally unique chain"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        pool = _all_mutator_names()
        if len(pool) < 4:
            return [(prompt, "insufficient pool", {})]
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        pop = [
            Individual(chain=rng.sample(pool, min(rng.randint(1, 3), len(pool))))
            for _ in range(6)
        ]
        # Find most unique by max Jaccard distance to all others
        best = max(pop, key=lambda ind: sum(
            _sharing_distance(ind, other) for other in pop if other is not ind
        ))
        output = best.apply(prompt)
        if output:
            return [(output[-1].mutated, f"niche-unique: {best.chain}", {"chain": best.chain})]
        return [(prompt, "niching no output", {})]


@register_mutator
class CoevSymbioticMutator(BaseMutator):
    """Symbiotic coevolution — combine two chains that have complementary strengths."""

    NAME = "coev_symbiotic"
    CATEGORY = "coevolution"
    DESCRIPTION = "Symbiotic combination of complementary mutator chains"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        pool = _all_mutator_names()
        if len(pool) < 4:
            return [(prompt, "insufficient pool", {})]
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        chain_a = rng.sample(pool, min(2, len(pool)))
        chain_b = rng.sample(pool, min(2, len(pool)))
        # Symbiosis: interleave the chains
        combined = []
        for a, b in zip(chain_a, chain_b):
            combined.extend([a, b])
        combined.extend(chain_a[len(chain_b):])
        combined.extend(chain_b[len(chain_a):])
        ind = Individual(chain=combined)
        output = ind.apply(prompt)
        if output:
            return [(output[-1].mutated, f"symbiotic: {combined}", {"chain": combined})]
        return [(prompt, "symbiotic no output", {})]


@register_mutator
class CoevPredatorPreyMutator(BaseMutator):
    """Predator-prey dynamics — attack adapts to evade the strongest defender."""

    NAME = "coev_predator_prey"
    CATEGORY = "coevolution"
    DESCRIPTION = "Predator-prey evasion targeting the strongest defense heuristic"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        pool = _all_mutator_names()
        if len(pool) < 2:
            return [(prompt, "insufficient pool", {})]
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        # Create a strong "predator" defense
        predator = DefenseRule(
            blocked_keywords=rng.sample(_DEFENSE_KEYWORDS, min(5, len(_DEFENSE_KEYWORDS))),
            max_length=3000,
        )
        # Evolve a "prey" chain that evades it
        best_chain = [rng.choice(pool)]
        best_text = prompt
        for _ in range(4):
            chain = [rng.choice(pool) for _ in range(rng.randint(1, 3))]
            ind = Individual(chain=chain)
            results = ind.apply(prompt)
            if results and not predator.evaluate(results[-1].mutated):
                if len(results[-1].mutated) > len(best_text):
                    best_chain = chain
                    best_text = results[-1].mutated
        return [(best_text, f"prey-evasion: {best_chain}", {"chain": best_chain})]


@register_mutator
class CoevSpeciationMutator(BaseMutator):
    """Speciation — evolve distinct species of attacks for different defense types."""

    NAME = "coev_speciation"
    CATEGORY = "coevolution"
    DESCRIPTION = "Species-based attack targeting different defense archetypes"

    def _apply(self, prompt: str, **kw) -> list[tuple[str, str, dict]]:
        pool = _all_mutator_names()
        if len(pool) < 4:
            return [(prompt, "insufficient pool", {})]
        rng = random.Random(_deterministic_seed(prompt, self.NAME))
        # Create 3 "species" (different chain archetypes)
        species = [
            rng.sample(pool, min(1, len(pool))),  # minimal
            rng.sample(pool, min(3, len(pool))),  # medium
            rng.sample(pool, min(2, len(pool))) + rng.sample(pool, min(2, len(pool))),  # long
        ]
        # Pick the species whose output is longest (proxy for complexity)
        best = prompt
        best_chain = species[0]
        for chain in species:
            ind = Individual(chain=chain)
            results = ind.apply(prompt)
            if results and len(results[-1].mutated) > len(best):
                best = results[-1].mutated
                best_chain = chain
        return [(best, f"speciated: {best_chain}", {"chain": best_chain})]
