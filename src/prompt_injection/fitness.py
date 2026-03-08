"""
Fitness tracking for adaptive mutation selection.

Tracks which mutators succeed against which models and uses fitness-proportionate
selection to prioritize effective mutators. Supports epsilon-greedy exploration
to keep discovering novel bypasses.

Usage:
    tracker = FitnessTracker()
    tracker.record("unicode_homoglyph", "gpt-4o", bypassed=True)
    tracker.record("unicode_homoglyph", "gpt-4o", bypassed=False)

    # Get fitness-weighted selection for a model
    selected = tracker.select_adaptive("gpt-4o", n=5, epsilon=0.1)
"""

from __future__ import annotations

import json
import math
import random
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field


@dataclass
class MutatorStats:
    """Per-mutator, per-model statistics."""
    success_count: int = 0
    total_count: int = 0
    fitness: float = 0.5  # Prior: assume 50% effectiveness

    @property
    def bypass_rate(self) -> float:
        if self.total_count == 0:
            return 0.5  # Prior
        return self.success_count / self.total_count

    @property
    def confidence(self) -> float:
        """How confident we are in the fitness estimate (0-1)."""
        return 1.0 - 1.0 / (1.0 + self.total_count)

    def update(self, bypassed: bool, alpha: float = 0.1) -> None:
        """Update fitness with exponential moving average."""
        self.total_count += 1
        if bypassed:
            self.success_count += 1
        # EMA: blend new observation with prior
        observation = 1.0 if bypassed else 0.0
        self.fitness = (1 - alpha) * self.fitness + alpha * observation

    def to_dict(self) -> dict[str, Any]:
        return {
            "success_count": self.success_count,
            "total_count": self.total_count,
            "fitness": round(self.fitness, 4),
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> MutatorStats:
        return cls(
            success_count=d.get("success_count", 0),
            total_count=d.get("total_count", 0),
            fitness=d.get("fitness", 0.5),
        )


class FitnessTracker:
    """Track mutator effectiveness across models.

    Stores a matrix of (mutator_name, model_id) -> MutatorStats.
    Supports persistence to JSON and fitness-proportionate selection.
    """

    def __init__(self, persist_path: Path | None = None):
        # {mutator_name: {model_id: MutatorStats}}
        self._stats: dict[str, dict[str, MutatorStats]] = {}
        self._persist_path = persist_path
        if persist_path and persist_path.exists():
            self._load()

    def record(self, mutator_name: str, model_id: str, bypassed: bool) -> None:
        """Record the result of testing a mutator against a model."""
        if mutator_name not in self._stats:
            self._stats[mutator_name] = {}
        if model_id not in self._stats[mutator_name]:
            self._stats[mutator_name][model_id] = MutatorStats()

        self._stats[mutator_name][model_id].update(bypassed)

    def get_stats(self, mutator_name: str, model_id: str) -> MutatorStats:
        """Get stats for a specific mutator-model pair."""
        return self._stats.get(mutator_name, {}).get(model_id, MutatorStats())

    def get_fitness(self, mutator_name: str, model_id: str) -> float:
        """Get fitness score for a mutator against a model."""
        return self.get_stats(mutator_name, model_id).fitness

    def get_bypass_rate(self, mutator_name: str, model_id: str) -> float:
        """Get raw bypass rate."""
        return self.get_stats(mutator_name, model_id).bypass_rate

    def select_adaptive(
        self,
        model_id: str,
        available_mutators: list[str] | None = None,
        n: int = 5,
        epsilon: float = 0.1,
        min_exploration: int = 3,
    ) -> list[str]:
        """Select mutators using epsilon-greedy fitness-proportionate selection.

        Args:
            model_id: Target model to optimize for.
            available_mutators: Pool to select from (all tracked if None).
            n: Number of mutators to select.
            epsilon: Exploration probability (0=pure exploit, 1=pure explore).
            min_exploration: Minimum trials before a mutator can be deprioritized.

        Returns:
            List of selected mutator names.
        """
        if available_mutators is None:
            from src.prompt_injection import list_mutators
            available_mutators = list(list_mutators().keys())

        if not available_mutators:
            return []

        n = min(n, len(available_mutators))

        # Separate under-explored mutators (always candidates for exploration)
        under_explored = []
        exploitable = []
        for name in available_mutators:
            stats = self.get_stats(name, model_id)
            if stats.total_count < min_exploration:
                under_explored.append(name)
            else:
                exploitable.append(name)

        selected: list[str] = []

        for _ in range(n):
            remaining_pool = [m for m in available_mutators if m not in selected]
            if not remaining_pool:
                break

            # Epsilon-greedy: explore or exploit
            if random.random() < epsilon and under_explored:
                # Explore: pick a random under-explored mutator
                candidates = [m for m in under_explored if m not in selected]
                if candidates:
                    selected.append(random.choice(candidates))
                    continue

            # Exploit: fitness-proportionate selection
            candidates = [m for m in remaining_pool if m not in selected]
            if not candidates:
                break

            weights = []
            for name in candidates:
                stats = self.get_stats(name, model_id)
                # Add small constant to avoid zero weights
                w = stats.fitness + 0.01
                # Boost under-explored mutators
                if stats.total_count < min_exploration:
                    w += 0.2
                weights.append(w)

            total = sum(weights)
            if total <= 0:
                selected.append(random.choice(candidates))
                continue

            probs = [w / total for w in weights]
            chosen = random.choices(candidates, weights=probs, k=1)[0]
            selected.append(chosen)

        return selected

    def get_leaderboard(
        self,
        model_id: str,
        top_n: int = 20,
    ) -> list[dict[str, Any]]:
        """Get ranked leaderboard of mutators for a model."""
        entries = []
        for mutator_name, model_stats in self._stats.items():
            if model_id in model_stats:
                stats = model_stats[model_id]
                entries.append({
                    "mutator": mutator_name,
                    "bypass_rate": round(stats.bypass_rate, 4),
                    "fitness": round(stats.fitness, 4),
                    "success_count": stats.success_count,
                    "total_count": stats.total_count,
                    "confidence": round(stats.confidence, 4),
                })

        entries.sort(key=lambda x: x["fitness"], reverse=True)
        return entries[:top_n]

    def get_model_vulnerability_profile(self, model_id: str) -> dict[str, float]:
        """Get per-category average fitness for a model."""
        from src.prompt_injection import list_mutators

        all_mutators = list_mutators()
        category_scores: dict[str, list[float]] = {}

        for name, info in all_mutators.items():
            cat = info["category"]
            stats = self.get_stats(name, model_id)
            if stats.total_count > 0:
                if cat not in category_scores:
                    category_scores[cat] = []
                category_scores[cat].append(stats.bypass_rate)

        return {
            cat: round(sum(scores) / len(scores), 4)
            for cat, scores in sorted(category_scores.items())
            if scores
        }

    def get_cross_model_correlation(self) -> dict[str, dict[str, float]]:
        """Compute pairwise correlation of vulnerability profiles across models."""
        models = set()
        for model_stats in self._stats.values():
            models.update(model_stats.keys())

        model_list = sorted(models)
        if len(model_list) < 2:
            return {}

        # Build fitness vectors
        mutator_names = sorted(self._stats.keys())
        vectors: dict[str, list[float]] = {}
        for model_id in model_list:
            vectors[model_id] = [
                self.get_stats(m, model_id).fitness for m in mutator_names
            ]

        # Compute Pearson correlations
        correlations: dict[str, dict[str, float]] = {}
        for i, m1 in enumerate(model_list):
            correlations[m1] = {}
            for j, m2 in enumerate(model_list):
                if i == j:
                    correlations[m1][m2] = 1.0
                else:
                    correlations[m1][m2] = _pearson(vectors[m1], vectors[m2])

        return correlations

    def save(self) -> None:
        """Persist to disk."""
        if self._persist_path is None:
            return
        self._persist_path.parent.mkdir(parents=True, exist_ok=True)
        data = {}
        for mutator, model_stats in self._stats.items():
            data[mutator] = {
                model: stats.to_dict() for model, stats in model_stats.items()
            }
        self._persist_path.write_text(json.dumps(data, indent=2))

    def _load(self) -> None:
        """Load from disk."""
        try:
            data = json.loads(self._persist_path.read_text())
            for mutator, model_stats in data.items():
                self._stats[mutator] = {
                    model: MutatorStats.from_dict(stats)
                    for model, stats in model_stats.items()
                }
        except (json.JSONDecodeError, KeyError):
            pass

    @property
    def tracked_mutators(self) -> int:
        return len(self._stats)

    @property
    def tracked_models(self) -> set[str]:
        models = set()
        for model_stats in self._stats.values():
            models.update(model_stats.keys())
        return models

    def to_dict(self) -> dict[str, Any]:
        """Full state as dict."""
        data = {}
        for mutator, model_stats in self._stats.items():
            data[mutator] = {
                model: stats.to_dict() for model, stats in model_stats.items()
            }
        return data


def _pearson(x: list[float], y: list[float]) -> float:
    """Compute Pearson correlation between two vectors."""
    n = len(x)
    if n == 0:
        return 0.0
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    den_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
    if den_x == 0 or den_y == 0:
        return 0.0
    return round(num / (den_x * den_y), 4)
