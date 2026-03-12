"""
Effort estimator — estimate the effort required for improvement tasks.

Uses historical data and task characteristics to predict how many
files, lines of code, and tests a task will require.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class EffortEstimate:
    """Estimated effort for a task."""

    task_kind: str
    level: str  # "trivial", "easy", "medium", "hard", "complex"
    estimated_files: int = 0
    estimated_lines: int = 0
    estimated_tests: int = 0
    estimated_minutes: int = 0
    confidence: float = 0.0  # 0.0–1.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_kind": self.task_kind,
            "level": self.level,
            "estimated_files": self.estimated_files,
            "estimated_lines": self.estimated_lines,
            "estimated_tests": self.estimated_tests,
            "estimated_minutes": self.estimated_minutes,
            "confidence": self.confidence,
        }


# Baseline estimates by task kind
EFFORT_BASELINES: dict[str, dict[str, Any]] = {
    "new_category": {
        "level": "medium",
        "files": 3,  # module + test + __init__ edit
        "lines": 300,
        "tests": 50,
        "minutes": 30,
    },
    "new_mutator": {
        "level": "easy",
        "files": 2,
        "lines": 50,
        "tests": 10,
        "minutes": 10,
    },
    "fix_bug": {
        "level": "easy",
        "files": 1,
        "lines": 20,
        "tests": 5,
        "minutes": 10,
    },
    "add_test": {
        "level": "easy",
        "files": 1,
        "lines": 80,
        "tests": 20,
        "minutes": 15,
    },
    "integrate_repo": {
        "level": "hard",
        "files": 4,
        "lines": 400,
        "tests": 40,
        "minutes": 60,
    },
    "refactor": {
        "level": "medium",
        "files": 3,
        "lines": 100,
        "tests": 10,
        "minutes": 20,
    },
}


class EffortEstimator:
    """Estimate effort required for improvement tasks.

    Usage:
        estimator = EffortEstimator()

        # Estimate for a task kind
        est = estimator.estimate("new_category", mutator_count=10)

        # Estimate with historical adjustment
        est = estimator.estimate("new_category", historical_avg_minutes=45)

        # Compare effort across task kinds
        comparison = estimator.compare(["new_category", "new_mutator", "fix_bug"])
    """

    def estimate(
        self,
        task_kind: str,
        mutator_count: int = 10,
        historical_avg_minutes: float | None = None,
    ) -> EffortEstimate:
        """Estimate effort for a task kind."""
        baseline = EFFORT_BASELINES.get(task_kind, {
            "level": "medium",
            "files": 2,
            "lines": 100,
            "tests": 20,
            "minutes": 20,
        })

        # Scale by mutator count
        scale = mutator_count / 10.0 if task_kind in ("new_category", "integrate_repo") else 1.0

        estimated_minutes = baseline["minutes"] * scale
        if historical_avg_minutes is not None:
            # Blend baseline with historical
            estimated_minutes = (estimated_minutes + historical_avg_minutes) / 2

        return EffortEstimate(
            task_kind=task_kind,
            level=baseline["level"],
            estimated_files=max(1, int(baseline["files"] * scale)),
            estimated_lines=max(10, int(baseline["lines"] * scale)),
            estimated_tests=max(5, int(baseline["tests"] * scale)),
            estimated_minutes=max(5, int(estimated_minutes)),
            confidence=0.7 if historical_avg_minutes else 0.5,
        )

    def compare(self, task_kinds: list[str]) -> list[EffortEstimate]:
        """Compare effort estimates across task kinds."""
        return [self.estimate(kind) for kind in task_kinds]

    @staticmethod
    def level_to_minutes(level: str) -> int:
        """Convert effort level to approximate minutes."""
        return {
            "trivial": 5,
            "easy": 10,
            "medium": 30,
            "hard": 60,
            "complex": 120,
        }.get(level, 30)
