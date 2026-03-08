"""
Track improvement metrics across feedback loop iterations.

Stores per-iteration metrics, computes trends and deltas, detects
plateaus, and identifies which attack categories are improving or
degrading over time.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field


@dataclass
class IterationMetrics:
    """Metrics from a single feedback loop iteration."""
    iteration: int
    timestamp: float
    total_attacks_generated: int = 0
    total_attacks_passed_quality: int = 0
    total_tested: int = 0
    total_harmful: int = 0
    harmful_rate: float = 0.0
    avg_harm_score: float = 0.0
    by_category: dict[str, dict[str, float]] = field(default_factory=dict)
    by_corridor: dict[str, dict[str, float]] = field(default_factory=dict)
    generator_model: str = ""
    target_model: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "iteration": self.iteration,
            "timestamp": self.timestamp,
            "total_attacks_generated": self.total_attacks_generated,
            "total_attacks_passed_quality": self.total_attacks_passed_quality,
            "total_tested": self.total_tested,
            "total_harmful": self.total_harmful,
            "harmful_rate": round(self.harmful_rate, 4),
            "avg_harm_score": round(self.avg_harm_score, 4),
            "by_category": self.by_category,
            "by_corridor": self.by_corridor,
            "generator_model": self.generator_model,
            "target_model": self.target_model,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> IterationMetrics:
        return cls(
            iteration=d.get("iteration", 0),
            timestamp=d.get("timestamp", 0),
            total_attacks_generated=d.get("total_attacks_generated", 0),
            total_attacks_passed_quality=d.get("total_attacks_passed_quality", 0),
            total_tested=d.get("total_tested", 0),
            total_harmful=d.get("total_harmful", 0),
            harmful_rate=d.get("harmful_rate", 0.0),
            avg_harm_score=d.get("avg_harm_score", 0.0),
            by_category=d.get("by_category", {}),
            by_corridor=d.get("by_corridor", {}),
            generator_model=d.get("generator_model", ""),
            target_model=d.get("target_model", ""),
        )


class ProgressTracker:
    """Track and analyze improvement across feedback loop iterations."""

    def __init__(self, data_dir: Path = Path("data/training")):
        self.data_dir = data_dir
        self._history: list[IterationMetrics] = []
        self._log_path = data_dir / "progress_history.jsonl"
        self._load()

    def _load(self) -> None:
        """Load history from disk."""
        if self._log_path.exists():
            with open(self._log_path, encoding="utf-8") as f:
                for line in f:
                    try:
                        self._history.append(
                            IterationMetrics.from_dict(json.loads(line))
                        )
                    except (json.JSONDecodeError, KeyError):
                        pass

    def record_iteration(self, metrics: IterationMetrics) -> None:
        """Record a new iteration's metrics."""
        self._history.append(metrics)
        self._log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(metrics.to_dict()) + "\n")

    @property
    def iterations(self) -> int:
        return len(self._history)

    def get_latest(self) -> IterationMetrics | None:
        return self._history[-1] if self._history else None

    def get_trend(self, metric: str = "harmful_rate", window: int = 5) -> dict[str, Any]:
        """Compute trend for a metric over recent iterations.

        Returns direction (improving/degrading/stable), slope, and values.
        """
        if len(self._history) < 2:
            return {"direction": "insufficient_data", "values": []}

        values = [getattr(m, metric, 0) for m in self._history[-window:]]

        # Simple linear regression
        n = len(values)
        x_mean = (n - 1) / 2
        y_mean = sum(values) / n
        numerator = sum((i - x_mean) * (v - y_mean) for i, v in enumerate(values))
        denominator = sum((i - x_mean) ** 2 for i in range(n))
        slope = numerator / denominator if denominator != 0 else 0

        # For harmful_rate from the *attacker's* perspective, increasing = improving
        if abs(slope) < 0.005:
            direction = "stable"
        elif slope > 0:
            direction = "improving"  # Attacks getting more effective
        else:
            direction = "degrading"  # Attacks getting less effective

        return {
            "direction": direction,
            "slope": round(slope, 6),
            "values": [round(v, 4) for v in values],
            "latest": round(values[-1], 4) if values else 0,
            "iterations_analyzed": n,
        }

    def get_category_trends(self) -> dict[str, dict[str, Any]]:
        """Get per-category trend analysis."""
        if len(self._history) < 2:
            return {}

        # Collect all categories seen
        all_cats: set[str] = set()
        for m in self._history:
            all_cats.update(m.by_category.keys())

        trends = {}
        for cat in sorted(all_cats):
            rates = []
            for m in self._history:
                cat_data = m.by_category.get(cat, {})
                rate = cat_data.get("harmful_rate", 0)
                rates.append(rate)

            if len(rates) >= 2:
                delta = rates[-1] - rates[0]
                trends[cat] = {
                    "first_rate": round(rates[0], 4),
                    "latest_rate": round(rates[-1], 4),
                    "delta": round(delta, 4),
                    "direction": "improving" if delta > 0.01 else (
                        "degrading" if delta < -0.01 else "stable"
                    ),
                    "history": [round(r, 4) for r in rates],
                }

        return trends

    def detect_plateau(self, window: int = 3, threshold: float = 0.01) -> bool:
        """Detect if the feedback loop has plateaued.

        Returns True if the last `window` iterations show less than
        `threshold` change in harmful_rate.
        """
        if len(self._history) < window:
            return False

        recent = self._history[-window:]
        rates = [m.harmful_rate for m in recent]
        spread = max(rates) - min(rates)
        return spread < threshold

    def get_generator_effectiveness(self) -> dict[str, Any]:
        """Track what % of generated attacks actually produce harmful responses."""
        if not self._history:
            return {"iterations": 0}

        effectiveness = []
        for m in self._history:
            if m.total_attacks_generated > 0:
                quality_rate = (
                    m.total_attacks_passed_quality / m.total_attacks_generated
                    if m.total_attacks_generated > 0 else 0
                )
                bypass_rate = m.harmful_rate
                effectiveness.append({
                    "iteration": m.iteration,
                    "quality_pass_rate": round(quality_rate, 4),
                    "bypass_rate": round(bypass_rate, 4),
                    "effective_attacks": m.total_harmful,
                })

        return {
            "iterations": len(effectiveness),
            "data": effectiveness,
            "latest_bypass_rate": effectiveness[-1]["bypass_rate"] if effectiveness else 0,
        }

    def get_summary(self) -> dict[str, Any]:
        """Get complete progress summary."""
        trend = self.get_trend()
        cat_trends = self.get_category_trends()
        effectiveness = self.get_generator_effectiveness()
        plateau = self.detect_plateau()

        # Find best and worst categories
        best_cat = max(cat_trends.items(), key=lambda x: x[1]["latest_rate"])[0] if cat_trends else None
        worst_cat = min(cat_trends.items(), key=lambda x: x[1]["latest_rate"])[0] if cat_trends else None

        return {
            "total_iterations": self.iterations,
            "overall_trend": trend,
            "plateau_detected": plateau,
            "best_attack_category": best_cat,
            "worst_attack_category": worst_cat,
            "generator_effectiveness": effectiveness,
            "category_trends": cat_trends,
        }

    def generate_report(self) -> str:
        """Generate human-readable progress report."""
        summary = self.get_summary()
        lines = [
            f"=== Feedback Loop Progress Report ({self.iterations} iterations) ===",
            "",
            f"Overall trend: {summary['overall_trend']['direction']} "
            f"(slope={summary['overall_trend'].get('slope', 'N/A')})",
            f"Plateau detected: {'YES' if summary['plateau_detected'] else 'No'}",
            "",
        ]

        if summary["best_attack_category"]:
            cat_trends = summary["category_trends"]
            best = summary["best_attack_category"]
            worst = summary["worst_attack_category"]
            lines.append(f"Most effective category: {best} "
                        f"({cat_trends[best]['latest_rate']:.1%} bypass)")
            lines.append(f"Least effective category: {worst} "
                        f"({cat_trends[worst]['latest_rate']:.1%} bypass)")
            lines.append("")

        eff = summary["generator_effectiveness"]
        if eff.get("data"):
            latest = eff["data"][-1]
            lines.append(f"Generator quality pass rate: {latest['quality_pass_rate']:.1%}")
            lines.append(f"Current bypass rate: {latest['bypass_rate']:.1%}")
            lines.append(f"Effective attacks this iteration: {latest['effective_attacks']}")

        return "\n".join(lines)
