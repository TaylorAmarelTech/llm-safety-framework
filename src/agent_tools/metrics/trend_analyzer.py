"""
Trend analyzer — detect trends and regressions across metric snapshots.

Compares snapshots over time to identify growth rates, plateaus,
regressions, and areas needing attention.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot


@dataclass
class Trend:
    """A detected trend in metrics."""

    metric: str
    direction: str  # "improving", "declining", "stable", "insufficient_data"
    current_value: float = 0.0
    previous_value: float = 0.0
    change: float = 0.0
    change_pct: float = 0.0
    severity: str = "info"  # "info", "warning", "alert"
    recommendation: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "metric": self.metric,
            "direction": self.direction,
            "current_value": self.current_value,
            "previous_value": self.previous_value,
            "change": self.change,
            "change_pct": self.change_pct,
            "severity": self.severity,
            "recommendation": self.recommendation,
        }


class TrendAnalyzer:
    """Analyze metric trends across snapshots.

    Usage:
        analyzer = TrendAnalyzer(collector)

        # Get all trends
        trends = analyzer.analyze()

        # Check for regressions
        regressions = analyzer.regressions()

        # Get a summary report
        report = analyzer.report()
    """

    def __init__(self, collector: SnapshotCollector | None = None) -> None:
        self._collector = collector or SnapshotCollector()

    def analyze(self) -> list[Trend]:
        """Analyze trends across all tracked metrics."""
        snapshots = self._collector.since(10)
        if len(snapshots) < 2:
            return [Trend(
                metric="all",
                direction="insufficient_data",
                recommendation="Need at least 2 snapshots for trend analysis",
            )]

        latest = snapshots[-1]
        previous = snapshots[-2]
        trends: list[Trend] = []

        # Mutator count trend
        trends.append(self._compare_metric(
            "total_mutators", latest.total_mutators, previous.total_mutators,
            higher_is_better=True,
        ))

        # Category count trend
        trends.append(self._compare_metric(
            "total_categories", latest.total_categories, previous.total_categories,
            higher_is_better=True,
        ))

        # Coverage score trend
        trends.append(self._compare_metric(
            "coverage_score", latest.coverage_score, previous.coverage_score,
            higher_is_better=True,
        ))

        # Quality score trend
        trends.append(self._compare_metric(
            "avg_quality_score", latest.avg_quality_score, previous.avg_quality_score,
            higher_is_better=True,
        ))

        # Test count trend
        trends.append(self._compare_metric(
            "total_tests", latest.total_tests, previous.total_tests,
            higher_is_better=True,
        ))

        return trends

    def regressions(self) -> list[Trend]:
        """Get only declining trends (regressions)."""
        return [t for t in self.analyze() if t.direction == "declining"]

    def improvements(self) -> list[Trend]:
        """Get only improving trends."""
        return [t for t in self.analyze() if t.direction == "improving"]

    def report(self) -> str:
        """Generate a human-readable trend report."""
        trends = self.analyze()
        lines = ["# Metric Trends Report\n"]

        for t in trends:
            icon = {"improving": "+", "declining": "-", "stable": "=",
                    "insufficient_data": "?"}[t.direction]
            lines.append(
                f"[{icon}] {t.metric}: {t.previous_value} → {t.current_value} "
                f"({t.change_pct:+.1f}%)"
            )
            if t.recommendation:
                lines.append(f"    → {t.recommendation}")

        regressions = self.regressions()
        if regressions:
            lines.append(f"\n⚠ {len(regressions)} regression(s) detected")
        else:
            lines.append("\nNo regressions detected")

        return "\n".join(lines)

    def _compare_metric(
        self,
        name: str,
        current: float,
        previous: float,
        higher_is_better: bool = True,
    ) -> Trend:
        """Compare two values and produce a trend."""
        if previous == 0:
            change_pct = 100.0 if current > 0 else 0.0
        else:
            change_pct = ((current - previous) / previous) * 100

        change = current - previous

        if abs(change_pct) < 0.5:
            direction = "stable"
            severity = "info"
        elif (change > 0) == higher_is_better:
            direction = "improving"
            severity = "info"
        else:
            direction = "declining"
            severity = "warning" if abs(change_pct) < 10 else "alert"

        recommendation = ""
        if direction == "declining":
            if name == "coverage_score":
                recommendation = "Coverage dropped — check if new categories need taxonomy entries"
            elif name == "total_mutators":
                recommendation = "Mutator count decreased — check for accidental deletions"
            elif name == "avg_quality_score":
                recommendation = "Quality declining — run QualityScorer on recent additions"

        return Trend(
            metric=name,
            direction=direction,
            current_value=current,
            previous_value=previous,
            change=change,
            change_pct=change_pct,
            severity=severity,
            recommendation=recommendation,
        )
