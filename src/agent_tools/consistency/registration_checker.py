"""
Registration checker — verify mutator registration is complete.

Checks that every mutator module is imported in __init__.py, every
category has a taxonomy entry, and every test file covers its category.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class RegistrationIssue:
    """A registration inconsistency."""

    kind: str  # "unregistered_module", "missing_taxonomy", "missing_tests"
    target: str
    description: str
    severity: str = "warning"  # "info", "warning", "error"
    fix: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "target": self.target,
            "description": self.description,
            "severity": self.severity,
            "fix": self.fix,
        }


class RegistrationChecker:
    """Verify that all framework components are properly registered.

    Usage:
        checker = RegistrationChecker()

        # Run all checks
        issues = checker.check_all()

        # Check just modules
        issues = checker.check_module_registration()

        # Check just taxonomy
        issues = checker.check_taxonomy()

        # Check test coverage
        issues = checker.check_test_coverage()
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    def check_all(self) -> list[RegistrationIssue]:
        """Run all registration checks."""
        issues: list[RegistrationIssue] = []
        issues.extend(self.check_module_registration())
        issues.extend(self.check_taxonomy())
        issues.extend(self.check_test_coverage())
        return issues

    def check_module_registration(self) -> list[RegistrationIssue]:
        """Check that all mutator module files are imported in __init__.py."""
        issues: list[RegistrationIssue] = []
        pi_dir = self._root / "src" / "prompt_injection"
        if not pi_dir.is_dir():
            return issues

        skip = {"__init__.py", "fitness.py", "coverage.py",
                "output_decoders.py", "metadata_schema.py", "attack_templates.py"}

        # Get all module files
        module_files = sorted(
            p.stem for p in pi_dir.glob("*.py")
            if p.name not in skip and not p.name.startswith("__")
        )

        # Read __init__.py to see what's imported
        init_path = pi_dir / "__init__.py"
        if not init_path.is_file():
            return issues

        init_content = init_path.read_text(encoding="utf-8", errors="replace")

        for module in module_files:
            if module not in init_content:
                issues.append(RegistrationIssue(
                    kind="unregistered_module",
                    target=module,
                    description=f"Module '{module}' exists but is not imported in __init__.py",
                    severity="error",
                    fix=f"Add 'from src.prompt_injection import {module}' to __init__.py",
                ))

        return issues

    def check_taxonomy(self) -> list[RegistrationIssue]:
        """Check that all registered categories have taxonomy entries."""
        issues: list[RegistrationIssue] = []
        try:
            from src.prompt_injection import get_categories
            from src.prompt_injection.coverage import CATEGORY_TAXONOMY

            categories = get_categories()
            for cat in categories:
                if cat not in CATEGORY_TAXONOMY:
                    issues.append(RegistrationIssue(
                        kind="missing_taxonomy",
                        target=cat,
                        description=f"Category '{cat}' has no taxonomy entry in coverage.py",
                        severity="warning",
                        fix=f"Add '{cat}' to CATEGORY_TAXONOMY in coverage.py",
                    ))
        except ImportError:
            pass

        return issues

    def check_test_coverage(self) -> list[RegistrationIssue]:
        """Check that each category has corresponding test files."""
        issues: list[RegistrationIssue] = []

        try:
            from src.prompt_injection import get_categories
            categories = get_categories()
        except ImportError:
            return issues

        tests_dir = self._root / "tests"
        if not tests_dir.is_dir():
            return issues

        test_content = ""
        for p in tests_dir.glob("test_*.py"):
            test_content += p.read_text(encoding="utf-8", errors="replace")

        for cat in categories:
            if f'"{cat}"' not in test_content and f"'{cat}'" not in test_content:
                issues.append(RegistrationIssue(
                    kind="missing_tests",
                    target=cat,
                    description=f"Category '{cat}' has no test coverage",
                    severity="info",
                    fix=f"Create tests for '{cat}' in tests/test_{cat}.py",
                ))

        return issues

    def summary(self) -> dict[str, Any]:
        """Get a summary of registration status."""
        issues = self.check_all()
        return {
            "total_issues": len(issues),
            "errors": len([i for i in issues if i.severity == "error"]),
            "warnings": len([i for i in issues if i.severity == "warning"]),
            "info": len([i for i in issues if i.severity == "info"]),
            "issues": [i.to_dict() for i in issues[:20]],
        }
