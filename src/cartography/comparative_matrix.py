"""
LLM Cartography — Comparative Scoring Matrix

Cross-model comparison: builds heatmaps, scorecards, and rankings
across dimensions, categories, corridors, and techniques.
"""

from __future__ import annotations

import statistics
from typing import Optional

from .models import PromptPoint, ModelScorecard


class ComparativeMatrix:
    """
    Builds cross-model comparison matrices.

    Usage:
        matrix = ComparativeMatrix()
        matrix.add_model_results("gpt-4o", gpt4_points)
        matrix.add_model_results("claude-3-opus", claude_points)
        scorecards = matrix.compute_scorecards()
        heatmap = matrix.compute_heatmap(axis="dimension")
    """

    def __init__(self):
        self._model_points: dict[str, list[PromptPoint]] = {}

    def add_model_results(self, model_id: str, points: list[PromptPoint]) -> None:
        self._model_points.setdefault(model_id, []).extend(points)

    @property
    def model_ids(self) -> list[str]:
        return sorted(self._model_points.keys())

    # ----- Scorecards -----

    def compute_scorecards(self) -> dict[str, ModelScorecard]:
        """Compute a scorecard for each model."""
        cards = {}
        for model_id, points in self._model_points.items():
            cards[model_id] = self._compute_one_scorecard(model_id, points)
        return cards

    def _compute_one_scorecard(
        self, model_id: str, points: list[PromptPoint],
    ) -> ModelScorecard:
        scored = [p for p in points if p.safety_score is not None]
        if not scored:
            return ModelScorecard(model_id=model_id)

        all_scores = [p.safety_score.score for p in scored]

        # Per-dimension averages (inverted: 10 - score*10 so higher = safer)
        dim_scores: dict[str, list[float]] = {}
        for p in scored:
            for dim_id, level in p.dimensional_vector.items():
                dim_scores.setdefault(dim_id, []).append(
                    10.0 * (1.0 - p.safety_score.score)  # 10 = safe, 0 = compliant
                )
        dim_avgs = {
            d: round(statistics.mean(s), 2) for d, s in dim_scores.items()
        }

        # Per-category averages
        cat_scores: dict[str, list[float]] = {}
        for p in scored:
            cat = p.category or "unknown"
            cat_scores.setdefault(cat, []).append(
                10.0 * (1.0 - p.safety_score.score)
            )
        cat_avgs = {
            c: round(statistics.mean(s), 2) for c, s in cat_scores.items()
        }

        # Per-corridor averages
        corr_scores: dict[str, list[float]] = {}
        for p in scored:
            corr = p.corridor or "unknown"
            corr_scores.setdefault(corr, []).append(
                10.0 * (1.0 - p.safety_score.score)
            )
        corr_avgs = {
            c: round(statistics.mean(s), 2) for c, s in corr_scores.items()
        }

        overall = round(10.0 * (1.0 - statistics.mean(all_scores)), 2)

        # Weakest and strongest
        sorted_dims = sorted(dim_avgs.items(), key=lambda x: x[1])
        weakest = [d for d, _ in sorted_dims[:5]]
        strongest = [d for d, _ in sorted_dims[-5:]]

        return ModelScorecard(
            model_id=model_id,
            dimension_scores=dim_avgs,
            category_scores=cat_avgs,
            corridor_scores=corr_avgs,
            overall_safety_score=overall,
            weakest_dimensions=weakest,
            strongest_dimensions=strongest,
            total_tests=len(scored),
        )

    # ----- Heatmap -----

    def compute_heatmap(
        self,
        axis: str = "dimension",
    ) -> dict:
        """
        Build a heatmap data structure.

        Args:
            axis: "dimension", "category", or "corridor"

        Returns:
            {models: [...], columns: [...], cells: [[float]], row_averages, column_averages}
        """
        scorecards = self.compute_scorecards()
        models = sorted(scorecards.keys())

        if axis == "dimension":
            # Collect all dimension IDs across models
            all_dims = set()
            for sc in scorecards.values():
                all_dims.update(sc.dimension_scores.keys())
            columns = sorted(all_dims)
            cells = [
                [scorecards[m].dimension_scores.get(d, 5.0) for d in columns]
                for m in models
            ]
        elif axis == "category":
            all_cats = set()
            for sc in scorecards.values():
                all_cats.update(sc.category_scores.keys())
            columns = sorted(all_cats)
            cells = [
                [scorecards[m].category_scores.get(c, 5.0) for c in columns]
                for m in models
            ]
        elif axis == "corridor":
            all_corrs = set()
            for sc in scorecards.values():
                all_corrs.update(sc.corridor_scores.keys())
            columns = sorted(all_corrs)
            cells = [
                [scorecards[m].corridor_scores.get(c, 5.0) for c in columns]
                for m in models
            ]
        else:
            raise ValueError(f"Unknown axis: {axis}. Use dimension/category/corridor.")

        # Row and column averages
        row_averages = [
            round(statistics.mean(row), 2) if row else 0.0 for row in cells
        ]
        col_averages = []
        for j in range(len(columns)):
            col_vals = [cells[i][j] for i in range(len(models)) if j < len(cells[i])]
            col_averages.append(
                round(statistics.mean(col_vals), 2) if col_vals else 0.0
            )

        return {
            "models": models,
            "columns": columns,
            "cells": cells,
            "row_averages": row_averages,
            "column_averages": col_averages,
        }

    # ----- Rankings -----

    def rank_models(self, metric: str = "overall") -> list[tuple[str, float]]:
        """Rank models by safety score (higher = safer)."""
        scorecards = self.compute_scorecards()
        ranked = [
            (model_id, sc.overall_safety_score)
            for model_id, sc in scorecards.items()
        ]
        ranked.sort(key=lambda x: x[1], reverse=True)
        return ranked

    # ----- Pairwise comparison -----

    def pairwise_comparison(
        self, model_a: str, model_b: str,
    ) -> dict:
        """Compare two models dimension-by-dimension."""
        scorecards = self.compute_scorecards()
        sc_a = scorecards.get(model_a)
        sc_b = scorecards.get(model_b)
        if not sc_a or not sc_b:
            return {"error": "One or both models not found"}

        all_dims = set(sc_a.dimension_scores) | set(sc_b.dimension_scores)
        deltas = {}
        for d in sorted(all_dims):
            a_val = sc_a.dimension_scores.get(d, 5.0)
            b_val = sc_b.dimension_scores.get(d, 5.0)
            deltas[d] = round(a_val - b_val, 2)

        a_wins = [d for d, delta in deltas.items() if delta > 0.5]
        b_wins = [d for d, delta in deltas.items() if delta < -0.5]

        return {
            "model_a": model_a,
            "model_b": model_b,
            "overall_a": sc_a.overall_safety_score,
            "overall_b": sc_b.overall_safety_score,
            "dimension_deltas": deltas,
            "a_stronger_on": a_wins,
            "b_stronger_on": b_wins,
            "summary": (
                f"{model_a} scores {sc_a.overall_safety_score}/10 overall, "
                f"{model_b} scores {sc_b.overall_safety_score}/10. "
                f"{model_a} is stronger on {len(a_wins)} dimensions, "
                f"{model_b} is stronger on {len(b_wins)} dimensions."
            ),
        }
