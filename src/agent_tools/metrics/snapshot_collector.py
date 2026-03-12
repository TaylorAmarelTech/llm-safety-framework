"""
Snapshot collector — capture point-in-time metrics of framework state.

Takes periodic snapshots of mutator count, category count, coverage
score, test results, and quality metrics for trend analysis.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class MetricSnapshot:
    """A point-in-time snapshot of framework metrics."""

    timestamp: str
    total_mutators: int = 0
    total_categories: int = 0
    total_tests: int = 0
    tests_passing: int = 0
    tests_failing: int = 0
    coverage_score: float = 0.0
    avg_quality_score: float = 0.0
    defense_layer_coverage: dict[str, float] = field(default_factory=dict)
    technique_class_coverage: dict[str, float] = field(default_factory=dict)
    agent: str = ""
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "MetricSnapshot":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


class SnapshotCollector:
    """Collect and persist metric snapshots.

    Usage:
        collector = SnapshotCollector()

        # Take a snapshot from live framework state
        snap = collector.capture()

        # Manually record a snapshot
        collector.record(MetricSnapshot(
            timestamp="2026-03-10T12:00:00Z",
            total_mutators=548,
            total_categories=47,
            coverage_score=0.72,
        ))

        # Get all snapshots
        history = collector.history()

        # Get the latest
        latest = collector.latest()
    """

    def __init__(self, store_path: str | Path | None = None) -> None:
        if store_path is None:
            default_dir = Path(__file__).resolve().parent.parent.parent.parent / "data"
            default_dir.mkdir(parents=True, exist_ok=True)
            self._path = default_dir / "metric_snapshots.json"
        else:
            self._path = Path(store_path)
        self._snapshots: list[MetricSnapshot] = []
        self._load()

    def _load(self) -> None:
        if self._path.exists():
            try:
                data = json.loads(self._path.read_text(encoding="utf-8"))
                self._snapshots = [MetricSnapshot.from_dict(d) for d in data]
            except (json.JSONDecodeError, KeyError):
                pass

    def _save(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        data = [s.to_dict() for s in self._snapshots]
        self._path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def capture(self, agent: str = "", notes: str = "") -> MetricSnapshot:
        """Capture a snapshot from the live framework state."""
        snap = MetricSnapshot(
            timestamp=datetime.now(tz=timezone.utc).isoformat(),
            agent=agent,
            notes=notes,
        )

        # Mutator counts
        try:
            from src.prompt_injection import list_mutators, get_categories
            mutators = list_mutators()
            snap.total_mutators = len(mutators)
            snap.total_categories = len(get_categories())
        except ImportError:
            pass

        # Coverage
        try:
            from src.prompt_injection.coverage import CoverageAnalyzer
            analyzer = CoverageAnalyzer()
            report = analyzer.analyze()
            snap.coverage_score = report.get("coverage_score", 0.0)
            snap.defense_layer_coverage = report.get("layer_coverage", {})
            snap.technique_class_coverage = report.get("technique_coverage", {})
        except (ImportError, AttributeError):
            pass

        # Test file count
        try:
            from src.agent_tools.codebase_explorer import FileFinder
            finder = FileFinder()
            test_files = finder.test_files()
            snap.total_tests = len(test_files)
        except ImportError:
            pass

        self.record(snap)
        return snap

    def record(self, snapshot: MetricSnapshot) -> None:
        """Manually record a snapshot."""
        self._snapshots.append(snapshot)
        self._save()

    def history(self) -> list[MetricSnapshot]:
        """Get all snapshots in chronological order."""
        return list(self._snapshots)

    def latest(self) -> MetricSnapshot | None:
        """Get the most recent snapshot."""
        return self._snapshots[-1] if self._snapshots else None

    def since(self, n: int = 5) -> list[MetricSnapshot]:
        """Get the last N snapshots."""
        return self._snapshots[-n:]

    def clear(self) -> None:
        """Clear all snapshots."""
        self._snapshots = []
        self._save()
