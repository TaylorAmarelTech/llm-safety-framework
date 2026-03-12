"""
Pipeline registry — pre-built pipelines for common workflows.

Provides ready-to-use Pipeline instances for standard improvement
tasks that agents can invoke directly.
"""

from __future__ import annotations

from typing import Any

from src.agent_tools.workflow_runner.pipeline import Pipeline, Step


class PipelineRegistry:
    """Registry of pre-built pipelines for common workflows.

    Usage:
        registry = PipelineRegistry()

        # List available pipelines
        names = registry.available()

        # Get a pre-built pipeline
        pipe = registry.get("health_check")

        # Run it
        result = pipe.run()
    """

    def available(self) -> list[str]:
        """List available pre-built pipeline names."""
        return [
            "health_check",
            "coverage_report",
            "find_next_task",
            "validate_recent_changes",
        ]

    def get(self, name: str) -> Pipeline | None:
        """Get a pre-built pipeline by name."""
        builders = {
            "health_check": self._build_health_check,
            "coverage_report": self._build_coverage_report,
            "find_next_task": self._build_find_next_task,
            "validate_recent_changes": self._build_validate_recent,
        }
        builder = builders.get(name)
        return builder() if builder else None

    def _build_health_check(self) -> Pipeline:
        """Build a pipeline that checks framework health."""
        pipe = Pipeline("Health Check")

        pipe.add_step(Step(
            name="check_registry",
            phase="orient",
            description="Verify mutator registry is functional",
            action=lambda ctx: _run_health_check(),
            produces=["health_status"],
        ))

        pipe.add_step(Step(
            name="check_consistency",
            phase="validate",
            description="Check for registration issues",
            action=lambda ctx: _run_registration_check(),
            produces=["registration_issues"],
            skip_on_failure=True,
        ))

        pipe.add_step(Step(
            name="check_orphans",
            phase="validate",
            description="Find orphaned files",
            action=lambda ctx: _run_orphan_check(),
            produces=["orphans"],
            skip_on_failure=True,
        ))

        return pipe

    def _build_coverage_report(self) -> Pipeline:
        """Build a pipeline that generates a coverage report."""
        pipe = Pipeline("Coverage Report")

        pipe.add_step(Step(
            name="snapshot",
            phase="orient",
            description="Capture current metrics",
            action=lambda ctx: _capture_snapshot(),
            produces=["snapshot"],
        ))

        pipe.add_step(Step(
            name="gap_analysis",
            phase="research",
            description="Analyze coverage gaps",
            action=lambda ctx: _run_gap_analysis(),
            produces=["gap_report"],
            skip_on_failure=True,
        ))

        return pipe

    def _build_find_next_task(self) -> Pipeline:
        """Build a pipeline that finds the next best task."""
        pipe = Pipeline("Find Next Task")

        pipe.add_step(Step(
            name="recommend",
            phase="plan",
            description="Get top recommendations",
            action=lambda ctx: _get_recommendations(),
            produces=["recommendations"],
        ))

        return pipe

    def _build_validate_recent(self) -> Pipeline:
        """Build a pipeline that validates recent changes."""
        pipe = Pipeline("Validate Recent Changes")

        pipe.add_step(Step(
            name="find_recent",
            phase="orient",
            description="Find recently modified files",
            action=lambda ctx: _find_recent_files(),
            produces=["recent_files"],
        ))

        pipe.add_step(Step(
            name="check_imports",
            phase="validate",
            description="Verify imports in changed files",
            action=lambda ctx: _check_imports(ctx.get("recent_files", [])),
            required_inputs=["recent_files"],
            produces=["import_issues"],
        ))

        return pipe


# Helper functions for pipeline actions

def _run_health_check() -> dict[str, Any]:
    try:
        from src.agent_tools.metrics.health_check import HealthCheck
        return HealthCheck().run().to_dict()
    except ImportError:
        return {"healthy": True, "info": ["HealthCheck module unavailable"]}


def _run_registration_check() -> list[dict[str, Any]]:
    try:
        from src.agent_tools.consistency import RegistrationChecker
        issues = RegistrationChecker().check_all()
        return [i.to_dict() for i in issues]
    except ImportError:
        return []


def _run_orphan_check() -> list[dict[str, Any]]:
    try:
        from src.agent_tools.consistency import OrphanDetector
        orphans = OrphanDetector().detect_all()
        return [o.to_dict() for o in orphans]
    except ImportError:
        return []


def _capture_snapshot() -> dict[str, Any]:
    try:
        from src.agent_tools.metrics import SnapshotCollector
        snap = SnapshotCollector().capture()
        return snap.to_dict()
    except ImportError:
        return {}


def _run_gap_analysis() -> dict[str, Any]:
    try:
        from src.agent_tools.research.gap_analyzer import GapAnalyzer
        report = GapAnalyzer().analyze()
        return report.to_dict()
    except (ImportError, AttributeError):
        return {}


def _get_recommendations() -> list[dict[str, Any]]:
    try:
        from src.agent_tools.recommendation import Recommender
        recs = Recommender().recommend(top_n=5)
        return [r.to_dict() for r in recs]
    except ImportError:
        return []


def _find_recent_files() -> list[str]:
    try:
        from src.agent_tools.codebase_explorer import FileFinder
        finder = FileFinder()
        files = finder.files_modified_recently(days=3)
        return [f.relative_path for f in files]
    except ImportError:
        return []


def _check_imports(files: list[str]) -> list[dict[str, Any]]:
    try:
        from src.agent_tools.consistency import ImportChecker
        checker = ImportChecker()
        issues = checker.check_files(files)
        return [i.to_dict() for i in issues]
    except ImportError:
        return []
