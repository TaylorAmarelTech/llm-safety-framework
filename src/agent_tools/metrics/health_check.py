"""
Health check — run a quick diagnostic of framework health.

Combines snapshot, trend, and validation data into a single
pass/fail health report that agents can check before starting work.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class HealthStatus:
    """Overall framework health status."""

    healthy: bool
    score: float = 0.0  # 0.0–1.0
    checks_passed: int = 0
    checks_total: int = 0
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "healthy": self.healthy,
            "score": self.score,
            "checks_passed": self.checks_passed,
            "checks_total": self.checks_total,
            "issues": self.issues,
            "warnings": self.warnings,
            "info": self.info,
        }


class HealthCheck:
    """Run a comprehensive framework health check.

    Usage:
        check = HealthCheck()
        status = check.run()

        if status.healthy:
            print("Framework is healthy, safe to make changes")
        else:
            print("Issues found:", status.issues)
    """

    def run(self) -> HealthStatus:
        """Run all health checks and return aggregated status."""
        status = HealthStatus(healthy=True)

        self._check_mutator_registry(status)
        self._check_test_files(status)
        self._check_coverage_taxonomy(status)
        self._check_init_imports(status)

        status.score = (
            status.checks_passed / max(status.checks_total, 1)
        )
        status.healthy = len(status.issues) == 0
        return status

    def _check_mutator_registry(self, status: HealthStatus) -> None:
        """Check that mutator registry is functional."""
        status.checks_total += 1
        try:
            from src.prompt_injection import list_mutators, get_categories
            mutators = list_mutators()
            categories = get_categories()
            if len(mutators) < 100:
                status.issues.append(
                    f"Only {len(mutators)} mutators registered (expected 500+)"
                )
            elif len(mutators) < 500:
                status.warnings.append(
                    f"{len(mutators)} mutators registered (expected 500+)"
                )
            else:
                status.checks_passed += 1
                status.info.append(f"{len(mutators)} mutators across {len(categories)} categories")
        except ImportError as exc:
            status.issues.append(f"Cannot import prompt_injection: {exc}")

    def _check_test_files(self, status: HealthStatus) -> None:
        """Check that test files exist."""
        status.checks_total += 1
        try:
            from src.agent_tools.codebase_explorer import FileFinder
            finder = FileFinder()
            tests = finder.test_files()
            if len(tests) < 5:
                status.warnings.append(f"Only {len(tests)} test files found")
            else:
                status.checks_passed += 1
                status.info.append(f"{len(tests)} test files found")
        except ImportError:
            status.warnings.append("Cannot check test files — FileFinder unavailable")

    def _check_coverage_taxonomy(self, status: HealthStatus) -> None:
        """Check that coverage taxonomy is consistent."""
        status.checks_total += 1
        try:
            from src.prompt_injection import get_categories
            from src.prompt_injection.coverage import CATEGORY_TAXONOMY
            categories = get_categories()
            missing = [c for c in categories if c not in CATEGORY_TAXONOMY]
            if missing:
                status.warnings.append(
                    f"{len(missing)} categories missing from taxonomy: {missing[:5]}"
                )
            else:
                status.checks_passed += 1
                status.info.append("All categories have taxonomy entries")
        except ImportError:
            status.warnings.append("Cannot check taxonomy — coverage module unavailable")

    def _check_init_imports(self, status: HealthStatus) -> None:
        """Check that __init__.py imports are working."""
        status.checks_total += 1
        try:
            from src.prompt_injection import list_mutators
            mutators = list_mutators()
            # Check for duplicate names
            names = [m.NAME for m in mutators]
            unique_names = set(names)
            if len(names) != len(unique_names):
                dupes = [n for n in unique_names if names.count(n) > 1]
                status.issues.append(
                    f"Duplicate mutator NAMEs found: {dupes[:5]}"
                )
            else:
                status.checks_passed += 1
                status.info.append("No duplicate mutator NAMEs")
        except (ImportError, AttributeError) as exc:
            status.warnings.append(f"Cannot check for duplicates: {exc}")
