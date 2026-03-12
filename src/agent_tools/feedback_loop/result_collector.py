"""
Result collector — gather structured outcomes from agent tasks.

Normalizes results from different sources (ExecutionTracker, test runs,
validation reports) into a unified format for the learning store.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class TaskOutcome:
    """Normalized outcome of an agent task."""

    task_id: str
    task_kind: str  # "new_category", "new_mutator", "fix_bug", "add_test", etc.
    success: bool
    agent: str = ""
    started_at: str = ""
    completed_at: str = ""
    duration_seconds: float = 0.0
    mutators_created: int = 0
    tests_created: int = 0
    tests_passed: int = 0
    tests_failed: int = 0
    files_changed: list[str] = field(default_factory=list)
    quality_score: float = 0.0
    coverage_delta: float = 0.0  # Change in coverage score
    error: str = ""
    lessons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TaskOutcome":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


class ResultCollector:
    """Collect and persist task outcomes for feedback analysis.

    Usage:
        collector = ResultCollector()

        # Record a successful task
        collector.record(TaskOutcome(
            task_id="task_001",
            task_kind="new_category",
            success=True,
            mutators_created=10,
            tests_created=50,
            quality_score=0.85,
            coverage_delta=0.02,
            lessons=["Pig Latin name collided — always check first"],
        ))

        # Get outcomes for analysis
        recent = collector.recent(10)
        successes = collector.successes()
        failures = collector.failures()

        # Get aggregate stats
        stats = collector.stats()
    """

    def __init__(self, store_path: str | Path | None = None) -> None:
        if store_path is None:
            default_dir = Path(__file__).resolve().parent.parent.parent.parent / "data"
            default_dir.mkdir(parents=True, exist_ok=True)
            self._path = default_dir / "task_outcomes.json"
        else:
            self._path = Path(store_path)
        self._outcomes: list[TaskOutcome] = []
        self._load()

    def _load(self) -> None:
        if self._path.exists():
            try:
                data = json.loads(self._path.read_text(encoding="utf-8"))
                self._outcomes = [TaskOutcome.from_dict(d) for d in data]
            except (json.JSONDecodeError, KeyError):
                pass

    def _save(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        data = [o.to_dict() for o in self._outcomes]
        self._path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def record(self, outcome: TaskOutcome) -> None:
        """Record a task outcome."""
        if not outcome.completed_at:
            outcome.completed_at = datetime.now(tz=timezone.utc).isoformat()
        self._outcomes.append(outcome)
        self._save()

    def recent(self, n: int = 10) -> list[TaskOutcome]:
        """Get the N most recent outcomes."""
        return self._outcomes[-n:]

    def successes(self) -> list[TaskOutcome]:
        """Get all successful outcomes."""
        return [o for o in self._outcomes if o.success]

    def failures(self) -> list[TaskOutcome]:
        """Get all failed outcomes."""
        return [o for o in self._outcomes if not o.success]

    def by_kind(self, kind: str) -> list[TaskOutcome]:
        """Filter outcomes by task kind."""
        return [o for o in self._outcomes if o.task_kind == kind]

    def by_agent(self, agent: str) -> list[TaskOutcome]:
        """Filter outcomes by agent name."""
        return [o for o in self._outcomes if o.agent == agent]

    def all_lessons(self) -> list[str]:
        """Extract all lessons learned across outcomes."""
        lessons: list[str] = []
        for o in self._outcomes:
            lessons.extend(o.lessons)
        return lessons

    def stats(self) -> dict[str, Any]:
        """Get aggregate statistics."""
        total = len(self._outcomes)
        successes = len([o for o in self._outcomes if o.success])
        return {
            "total_tasks": total,
            "successes": successes,
            "failures": total - successes,
            "success_rate": round(successes / max(total, 1) * 100, 1),
            "total_mutators_created": sum(o.mutators_created for o in self._outcomes),
            "total_tests_created": sum(o.tests_created for o in self._outcomes),
            "avg_quality_score": round(
                sum(o.quality_score for o in self._outcomes) / max(total, 1), 3
            ),
            "total_lessons": len(self.all_lessons()),
        }

    def clear(self) -> None:
        """Clear all outcomes."""
        self._outcomes = []
        self._save()
