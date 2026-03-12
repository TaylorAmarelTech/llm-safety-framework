"""
Shapley value analysis for understanding mutator contributions.

Computes approximate Shapley values for individual mutators within a
chain, revealing which mutators actually contribute to bypass success
versus which are passengers (or even harmful).

Also provides pairwise synergy analysis: are two mutators complementary
(super-additive) or redundant (sub-additive)?

Implements:
- Permutation sampling for approximate Shapley values
- Marginal contribution estimation
- Pairwise synergy/redundancy matrix
- Coalition value caching for efficiency
- Banzhaf power index (alternative to Shapley for faster computation)

Sources:
- Shapley (1953): "A Value for n-Person Games"
- Castro et al. (2009): "Polynomial calculation of Shapley values"
- Strumbelj & Kononenko (2014): "Explaining prediction models" (sampling approach)
- Applied to ML feature importance: Lundberg & Lee (2017) — SHAP
"""

from __future__ import annotations

import itertools
import random
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Callable


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class MutatorContribution:
    """Shapley value and related metrics for a single mutator."""

    mutator_name: str
    shapley_value: float
    marginal_contribution: float
    banzhaf_index: float = 0.0
    n_coalitions_sampled: int = 0
    is_beneficial: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "mutator_name": self.mutator_name,
            "shapley_value": round(self.shapley_value, 6),
            "marginal_contribution": round(self.marginal_contribution, 6),
            "banzhaf_index": round(self.banzhaf_index, 6),
            "n_coalitions_sampled": self.n_coalitions_sampled,
            "is_beneficial": self.is_beneficial,
        }


@dataclass
class SynergyPair:
    """Synergy analysis between two mutators."""

    mutator_a: str
    mutator_b: str
    individual_value_a: float
    individual_value_b: float
    combined_value: float
    synergy_score: float  # positive = synergistic, negative = redundant
    interaction_type: str  # "synergistic", "redundant", "independent"

    def to_dict(self) -> dict[str, Any]:
        return {
            "pair": [self.mutator_a, self.mutator_b],
            "individual_values": [
                round(self.individual_value_a, 4),
                round(self.individual_value_b, 4),
            ],
            "combined_value": round(self.combined_value, 4),
            "synergy_score": round(self.synergy_score, 4),
            "interaction_type": self.interaction_type,
        }


@dataclass
class ShapleyReport:
    """Full Shapley analysis report for a mutator chain."""

    chain: list[str]
    contributions: list[MutatorContribution]
    synergies: list[SynergyPair]
    total_chain_value: float
    n_permutations_sampled: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "chain": self.chain,
            "total_chain_value": round(self.total_chain_value, 4),
            "n_permutations_sampled": self.n_permutations_sampled,
            "contributions": [c.to_dict() for c in self.contributions],
            "top_synergies": [s.to_dict() for s in self.synergies[:5]],
            "recommended_removal": [
                c.mutator_name for c in self.contributions
                if not c.is_beneficial
            ],
        }

    def ranked_mutators(self) -> list[tuple[str, float]]:
        """Return mutators ranked by Shapley value (highest first)."""
        return sorted(
            [(c.mutator_name, c.shapley_value) for c in self.contributions],
            key=lambda x: x[1],
            reverse=True,
        )


# ---------------------------------------------------------------------------
# Coalition value evaluator
# ---------------------------------------------------------------------------


class CoalitionEvaluator:
    """Evaluates the value (fitness) of a coalition of mutators.

    Caches results to avoid redundant evaluations.
    """

    def __init__(
        self,
        prompt: str,
        value_fn: Callable[[str, list[str]], float],
    ):
        self.prompt = prompt
        self.value_fn = value_fn
        self._cache: dict[frozenset[str], float] = {}
        self.evaluations = 0

    def evaluate(self, coalition: list[str]) -> float:
        """Evaluate a coalition, using cache when possible."""
        key = frozenset(coalition)
        if key in self._cache:
            return self._cache[key]
        value = self.value_fn(self.prompt, coalition)
        self._cache[key] = value
        self.evaluations += 1
        return value

    @property
    def cache_size(self) -> int:
        return len(self._cache)


# ---------------------------------------------------------------------------
# Shapley value analyzer
# ---------------------------------------------------------------------------


class ShapleyAnalyzer:
    """Compute Shapley values and synergy metrics for mutator chains.

    Uses permutation sampling (Monte Carlo) for approximate Shapley values,
    which scales to arbitrary chain lengths.
    """

    def __init__(self, n_permutations: int = 100):
        self.n_permutations = n_permutations

    def compute_shapley(
        self,
        chain: list[str],
        prompt: str,
        value_fn: Callable[[str, list[str]], float],
    ) -> list[MutatorContribution]:
        """Compute approximate Shapley values for each mutator in *chain*.

        Args:
            chain: List of mutator names to analyze.
            prompt: The seed prompt to test against.
            value_fn: ``(prompt, chain_subset) -> float`` scoring function.
                      Should return the fitness of applying the given chain
                      subset to the prompt.

        Returns:
            List of MutatorContribution objects with Shapley values.
        """
        if not chain:
            return []

        evaluator = CoalitionEvaluator(prompt, value_fn)
        n = len(chain)

        # Accumulate marginal contributions per mutator
        shapley_accum: dict[str, float] = defaultdict(float)
        count: dict[str, int] = defaultdict(int)

        for _ in range(self.n_permutations):
            perm = list(chain)
            random.shuffle(perm)

            prev_value = evaluator.evaluate([])  # empty coalition
            for i, mutator in enumerate(perm):
                coalition = perm[:i + 1]
                current_value = evaluator.evaluate(coalition)
                marginal = current_value - prev_value
                shapley_accum[mutator] += marginal
                count[mutator] += 1
                prev_value = current_value

        # Compute marginal contribution (adding mutator to full chain minus it)
        full_value = evaluator.evaluate(list(chain))

        contributions: list[MutatorContribution] = []
        for mutator in chain:
            sv = shapley_accum[mutator] / max(count[mutator], 1)
            # Marginal: v(N) - v(N \ {i})
            without = [m for m in chain if m != mutator]
            without_value = evaluator.evaluate(without)
            marginal = full_value - without_value

            contributions.append(MutatorContribution(
                mutator_name=mutator,
                shapley_value=sv,
                marginal_contribution=marginal,
                n_coalitions_sampled=count[mutator],
                is_beneficial=sv > 0,
            ))

        return contributions

    def compute_banzhaf(
        self,
        chain: list[str],
        prompt: str,
        value_fn: Callable[[str, list[str]], float],
        n_samples: int = 200,
    ) -> list[MutatorContribution]:
        """Compute Banzhaf power indices (faster alternative to Shapley).

        For each mutator, randomly samples coalitions and measures how often
        the mutator is a swing player (its addition changes the outcome).
        """
        if not chain:
            return []

        evaluator = CoalitionEvaluator(prompt, value_fn)
        banzhaf_accum: dict[str, float] = defaultdict(float)
        banzhaf_count: dict[str, int] = defaultdict(int)

        for _ in range(n_samples):
            mutator = random.choice(chain)
            others = [m for m in chain if m != mutator]
            # Random subset of others
            k = random.randint(0, len(others))
            subset = random.sample(others, k)

            without = evaluator.evaluate(subset)
            with_m = evaluator.evaluate(subset + [mutator])
            swing = with_m - without

            banzhaf_accum[mutator] += swing
            banzhaf_count[mutator] += 1

        full_value = evaluator.evaluate(list(chain))
        contributions: list[MutatorContribution] = []
        for mutator in chain:
            bi = banzhaf_accum[mutator] / max(banzhaf_count[mutator], 1)
            without = [m for m in chain if m != mutator]
            marginal = full_value - evaluator.evaluate(without)
            contributions.append(MutatorContribution(
                mutator_name=mutator,
                shapley_value=0.0,
                marginal_contribution=marginal,
                banzhaf_index=bi,
                n_coalitions_sampled=banzhaf_count.get(mutator, 0),
                is_beneficial=bi > 0,
            ))

        return contributions

    # -- synergy analysis ---------------------------------------------------

    def compute_synergy_matrix(
        self,
        chain: list[str],
        prompt: str,
        value_fn: Callable[[str, list[str]], float],
    ) -> list[SynergyPair]:
        """Compute pairwise synergy/redundancy for all mutator pairs.

        Synergy = v({A,B}) - v({A}) - v({B}) + v({})
        Positive → synergistic (together > sum of parts)
        Negative → redundant (together < sum of parts)
        """
        if len(chain) < 2:
            return []

        evaluator = CoalitionEvaluator(prompt, value_fn)
        empty_value = evaluator.evaluate([])

        synergies: list[SynergyPair] = []
        for i, a in enumerate(chain):
            for b in chain[i + 1:]:
                v_a = evaluator.evaluate([a])
                v_b = evaluator.evaluate([b])
                v_ab = evaluator.evaluate([a, b])
                synergy = v_ab - v_a - v_b + empty_value

                if abs(synergy) < 0.01:
                    interaction = "independent"
                elif synergy > 0:
                    interaction = "synergistic"
                else:
                    interaction = "redundant"

                synergies.append(SynergyPair(
                    mutator_a=a,
                    mutator_b=b,
                    individual_value_a=v_a - empty_value,
                    individual_value_b=v_b - empty_value,
                    combined_value=v_ab - empty_value,
                    synergy_score=synergy,
                    interaction_type=interaction,
                ))

        synergies.sort(key=lambda s: abs(s.synergy_score), reverse=True)
        return synergies

    # -- full report --------------------------------------------------------

    def full_report(
        self,
        chain: list[str],
        prompt: str,
        value_fn: Callable[[str, list[str]], float],
    ) -> ShapleyReport:
        """Generate a comprehensive Shapley analysis report."""
        contributions = self.compute_shapley(chain, prompt, value_fn)
        synergies = self.compute_synergy_matrix(chain, prompt, value_fn)

        evaluator = CoalitionEvaluator(prompt, value_fn)
        total_value = evaluator.evaluate(list(chain))

        # Add Banzhaf indices to contributions
        banzhaf = self.compute_banzhaf(chain, prompt, value_fn)
        banzhaf_map = {c.mutator_name: c.banzhaf_index for c in banzhaf}
        for c in contributions:
            c.banzhaf_index = banzhaf_map.get(c.mutator_name, 0.0)

        return ShapleyReport(
            chain=list(chain),
            contributions=contributions,
            synergies=synergies,
            total_chain_value=total_value,
            n_permutations_sampled=self.n_permutations,
        )

    # -- chain optimization suggestions ------------------------------------

    def suggest_pruned_chain(
        self,
        chain: list[str],
        prompt: str,
        value_fn: Callable[[str, list[str]], float],
        min_contribution: float = 0.0,
    ) -> list[str]:
        """Suggest a pruned chain by removing non-beneficial mutators.

        Removes mutators whose Shapley value is below *min_contribution*.
        """
        contributions = self.compute_shapley(chain, prompt, value_fn)
        return [
            c.mutator_name for c in contributions
            if c.shapley_value >= min_contribution
        ]

    def suggest_optimal_ordering(
        self,
        chain: list[str],
        prompt: str,
        value_fn: Callable[[str, list[str]], float],
    ) -> list[str]:
        """Suggest the optimal ordering of mutators by Shapley value.

        Highest-value mutators go first (most impactful early in the chain).
        """
        contributions = self.compute_shapley(chain, prompt, value_fn)
        ranked = sorted(contributions, key=lambda c: c.shapley_value, reverse=True)
        return [c.mutator_name for c in ranked]
