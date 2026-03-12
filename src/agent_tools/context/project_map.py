"""
Dynamic project map generator.

Generates a structured representation of the project's current state —
packages, mutator categories, test files, plugin counts, etc. — so that
an agent can quickly orient itself without reading every file.
"""

from __future__ import annotations

import importlib
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class PackageInfo:
    """Information about a Python package in the project."""

    name: str
    path: str
    module_count: int = 0
    description: str = ""
    key_exports: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "path": self.path,
            "module_count": self.module_count,
            "description": self.description,
            "key_exports": self.key_exports,
        }


@dataclass
class MutatorCategoryInfo:
    """Information about a mutator category."""

    name: str
    mutator_count: int
    defense_layers: list[str] = field(default_factory=list)
    technique_classes: list[str] = field(default_factory=list)
    module_file: str = ""


@dataclass
class ProjectSnapshot:
    """Complete snapshot of the project's current state."""

    packages: list[PackageInfo] = field(default_factory=list)
    total_mutators: int = 0
    total_categories: int = 0
    total_test_files: int = 0
    total_tests_approx: int = 0
    categories: list[MutatorCategoryInfo] = field(default_factory=list)
    web_plugins: list[str] = field(default_factory=list)
    chain_seed_count: int = 0
    scraper_seed_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "packages": [p.to_dict() for p in self.packages],
            "total_mutators": self.total_mutators,
            "total_categories": self.total_categories,
            "total_test_files": self.total_test_files,
            "categories": [
                {
                    "name": c.name,
                    "mutator_count": c.mutator_count,
                    "defense_layers": c.defense_layers,
                    "technique_classes": c.technique_classes,
                }
                for c in self.categories
            ],
            "web_plugins": self.web_plugins,
        }


class ProjectMap:
    """Generate a structured map of the project for agent orientation.

    Usage:
        pmap = ProjectMap()
        snapshot = pmap.snapshot()
        print(pmap.summary())           # Human-readable summary
        print(pmap.category_list())     # All mutator categories
        print(pmap.package_list())      # All packages
    """

    def __init__(self, project_root: str | Path | None = None) -> None:
        if project_root is None:
            # Default: assume we're inside llm-safety-framework-public
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(project_root)
        self._src = self._root / "src"
        self._tests = self._root / "tests"

    def snapshot(self) -> ProjectSnapshot:
        """Generate a full project snapshot."""
        snap = ProjectSnapshot()
        snap.packages = self._scan_packages()
        snap.total_test_files = self._count_test_files()

        # Mutator info
        try:
            from src.prompt_injection import list_mutators
            from src.prompt_injection.coverage import CATEGORY_TAXONOMY

            mutators = list_mutators()
            snap.total_mutators = len(mutators)
            cats: dict[str, int] = {}
            for info in mutators.values():
                cat = info["category"]
                cats[cat] = cats.get(cat, 0) + 1
            snap.total_categories = len(cats)

            for cat_name, count in sorted(cats.items()):
                taxonomy = CATEGORY_TAXONOMY.get(cat_name, {})
                snap.categories.append(
                    MutatorCategoryInfo(
                        name=cat_name,
                        mutator_count=count,
                        defense_layers=taxonomy.get("defense_layers", []),
                        technique_classes=taxonomy.get("technique_classes", []),
                    )
                )
        except ImportError:
            pass

        # Web plugins
        try:
            plugins_dir = self._src / "web" / "plugins"
            if plugins_dir.is_dir():
                snap.web_plugins = sorted(
                    d.name
                    for d in plugins_dir.iterdir()
                    if d.is_dir() and (d / "__init__.py").exists()
                )
        except OSError:
            pass

        return snap

    def summary(self) -> str:
        """Generate a human-readable project summary."""
        snap = self.snapshot()
        lines = [
            "=" * 60,
            "LLM Safety Framework — Project Map",
            "=" * 60,
            f"Total mutators:     {snap.total_mutators}",
            f"Total categories:   {snap.total_categories}",
            f"Total test files:   {snap.total_test_files}",
            f"Web plugins:        {len(snap.web_plugins)}",
            f"Source packages:    {len(snap.packages)}",
            "",
            "Packages:",
        ]
        for pkg in snap.packages:
            lines.append(f"  {pkg.name:30s} ({pkg.module_count} modules)")

        lines.append("")
        lines.append("Mutator categories:")
        for cat in snap.categories:
            layers = ", ".join(cat.defense_layers) if cat.defense_layers else "?"
            lines.append(f"  {cat.name:35s} {cat.mutator_count:3d} mutators  [{layers}]")

        return "\n".join(lines)

    def category_list(self) -> list[dict[str, Any]]:
        """List all mutator categories with counts and taxonomy."""
        snap = self.snapshot()
        return [
            {
                "name": c.name,
                "mutator_count": c.mutator_count,
                "defense_layers": c.defense_layers,
                "technique_classes": c.technique_classes,
            }
            for c in snap.categories
        ]

    def package_list(self) -> list[dict[str, Any]]:
        """List all source packages."""
        return [p.to_dict() for p in self._scan_packages()]

    def _scan_packages(self) -> list[PackageInfo]:
        """Scan src/ for Python packages."""
        packages = []
        if not self._src.is_dir():
            return packages
        for item in sorted(self._src.iterdir()):
            if item.is_dir() and (item / "__init__.py").exists():
                py_files = list(item.glob("*.py"))
                packages.append(
                    PackageInfo(
                        name=item.name,
                        path=str(item.relative_to(self._root)),
                        module_count=len(py_files),
                    )
                )
        return packages

    def _count_test_files(self) -> int:
        """Count test files in tests/."""
        if not self._tests.is_dir():
            return 0
        return len(list(self._tests.glob("test_*.py")))
