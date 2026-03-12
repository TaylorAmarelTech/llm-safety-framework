"""
Coverage checker — verify coverage after changes.

Quick check that runs after adding/modifying mutators to ensure
taxonomy consistency, no orphan categories, and coverage score
hasn't regressed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CoverageCheckResult:
    """Result of a coverage check."""

    passed: bool = True
    coverage_score: float = 0.0
    total_mutators: int = 0
    total_categories: int = 0
    issues: list[str] = field(default_factory=list)
    missing_from_taxonomy: list[str] = field(default_factory=list)
    orphan_taxonomy: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "coverage_score": self.coverage_score,
            "total_mutators": self.total_mutators,
            "total_categories": self.total_categories,
            "issues": self.issues,
            "missing_from_taxonomy": self.missing_from_taxonomy,
            "orphan_taxonomy": self.orphan_taxonomy,
        }

    def summary(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        lines = [
            f"[{status}] Coverage check",
            f"  Mutators: {self.total_mutators}",
            f"  Categories: {self.total_categories}",
            f"  Coverage score: {self.coverage_score:.1%}",
        ]
        if self.issues:
            lines.append(f"  Issues: {len(self.issues)}")
            for issue in self.issues[:5]:
                lines.append(f"    - {issue}")
        return "\n".join(lines)


class CoverageChecker:
    """Run coverage checks after modifications.

    Usage:
        checker = CoverageChecker()
        result = checker.check()
        if not result.passed:
            for issue in result.issues:
                print(f"  FIX: {issue}")
    """

    def __init__(self, min_coverage: float = 0.5, min_mutators: int = 500) -> None:
        self.min_coverage = min_coverage
        self.min_mutators = min_mutators

    def check(self) -> CoverageCheckResult:
        """Run all coverage checks."""
        result = CoverageCheckResult()

        try:
            from src.prompt_injection import list_mutators
            from src.prompt_injection.coverage import (
                CATEGORY_TAXONOMY,
                CoverageAnalyzer,
            )

            mutators = list_mutators()
            actual_cats = set(m["category"] for m in mutators.values())
            taxonomy_cats = set(CATEGORY_TAXONOMY.keys())

            result.total_mutators = len(mutators)
            result.total_categories = len(actual_cats)

            # 1. Check for categories missing from taxonomy
            missing = actual_cats - taxonomy_cats
            if missing:
                result.missing_from_taxonomy = sorted(missing)
                result.issues.append(
                    f"Categories missing from CATEGORY_TAXONOMY: {sorted(missing)}"
                )
                result.passed = False

            # 2. Check for orphan taxonomy entries
            orphans = taxonomy_cats - actual_cats
            if orphans:
                result.orphan_taxonomy = sorted(orphans)
                result.issues.append(
                    f"CATEGORY_TAXONOMY entries without mutators: {sorted(orphans)}"
                )
                result.passed = False

            # 3. Check coverage score
            analyzer = CoverageAnalyzer()
            report = analyzer.analyze()
            result.coverage_score = report.coverage_score

            if report.coverage_score < self.min_coverage:
                result.issues.append(
                    f"Coverage score {report.coverage_score:.1%} below minimum {self.min_coverage:.1%}"
                )
                result.passed = False

            # 4. Check mutator count
            if len(mutators) < self.min_mutators:
                result.issues.append(
                    f"Total mutators {len(mutators)} below minimum {self.min_mutators}"
                )
                result.passed = False

            # 5. Check each category has at least 1 mutator
            for cat in taxonomy_cats:
                cat_mutators = [
                    name for name, info in mutators.items()
                    if info["category"] == cat
                ]
                if not cat_mutators:
                    result.issues.append(f"Category '{cat}' has 0 mutators")
                    result.passed = False

        except ImportError as e:
            result.issues.append(f"Import error: {e}")
            result.passed = False

        return result

    def check_category(self, category: str) -> CoverageCheckResult:
        """Check a single category's coverage integration."""
        result = CoverageCheckResult()

        try:
            from src.prompt_injection import list_mutators, get_mutators_by_category
            from src.prompt_injection.coverage import CATEGORY_TAXONOMY

            # Check taxonomy entry exists
            if category not in CATEGORY_TAXONOMY:
                result.issues.append(f"Category '{category}' not in CATEGORY_TAXONOMY")
                result.passed = False
            else:
                entry = CATEGORY_TAXONOMY[category]
                if not entry.get("defense_layers"):
                    result.issues.append(f"Category '{category}' has no defense_layers")
                    result.passed = False
                if not entry.get("technique_classes"):
                    result.issues.append(f"Category '{category}' has no technique_classes")
                    result.passed = False

            # Check mutators exist
            names = get_mutators_by_category(category)
            result.total_mutators = len(names)
            if not names:
                result.issues.append(f"Category '{category}' has 0 registered mutators")
                result.passed = False

            result.total_categories = 1

        except ImportError as e:
            result.issues.append(f"Import error: {e}")
            result.passed = False

        return result
