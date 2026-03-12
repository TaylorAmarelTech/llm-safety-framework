"""
Orphan detector — find orphaned files, dead code, and stale references.

Identifies test files without corresponding modules, helper functions
that are never called, and references to deleted categories.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Orphan:
    """An orphaned or unreferenced item."""

    kind: str  # "orphan_test", "orphan_helper", "stale_reference", "unused_import"
    file_path: str
    name: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "file_path": self.file_path,
            "name": self.name,
            "description": self.description,
        }


class OrphanDetector:
    """Find orphaned files and dead code.

    Usage:
        detector = OrphanDetector()

        # Find all orphans
        orphans = detector.detect_all()

        # Find orphan test files
        orphan_tests = detector.orphan_tests()

        # Find unused helper functions
        unused = detector.unused_helpers("src/prompt_injection/encoding_format.py")
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    def detect_all(self) -> list[Orphan]:
        """Run all orphan detection checks."""
        orphans: list[Orphan] = []
        orphans.extend(self.orphan_tests())
        orphans.extend(self.orphan_modules())
        return orphans

    def orphan_tests(self) -> list[Orphan]:
        """Find test files that reference non-existent categories."""
        orphans: list[Orphan] = []
        tests_dir = self._root / "tests"
        pi_dir = self._root / "src" / "prompt_injection"

        if not tests_dir.is_dir() or not pi_dir.is_dir():
            return orphans

        # Get existing module names
        existing_modules = {
            p.stem for p in pi_dir.glob("*.py")
            if not p.name.startswith("__")
        }

        for test_file in tests_dir.glob("test_*.py"):
            # Extract category references from test file name
            test_name = test_file.stem.replace("test_", "")
            # Check if this test references a specific module
            if test_name in existing_modules:
                continue  # Has a matching module

            # Check if test file content references any known category
            try:
                content = test_file.read_text(encoding="utf-8", errors="replace")
                if "prompt_injection" in content:
                    # It's a PI test — check if the categories it tests exist
                    try:
                        from src.prompt_injection import get_categories
                        categories = get_categories()
                        has_match = any(
                            f'"{cat}"' in content or f"'{cat}'" in content
                            for cat in categories
                        )
                        if not has_match and "get_mutators_by_category" in content:
                            orphans.append(Orphan(
                                kind="orphan_test",
                                file_path=str(test_file.relative_to(self._root)),
                                name=test_file.stem,
                                description="Test file references categories that may not exist",
                            ))
                    except ImportError:
                        pass
            except OSError:
                continue

        return orphans

    def orphan_modules(self) -> list[Orphan]:
        """Find mutator modules that aren't imported anywhere."""
        orphans: list[Orphan] = []
        pi_dir = self._root / "src" / "prompt_injection"
        if not pi_dir.is_dir():
            return orphans

        skip = {"__init__.py", "fitness.py", "coverage.py",
                "output_decoders.py", "metadata_schema.py", "attack_templates.py"}

        init_path = pi_dir / "__init__.py"
        if not init_path.is_file():
            return orphans

        init_content = init_path.read_text(encoding="utf-8", errors="replace")

        for p in sorted(pi_dir.glob("*.py")):
            if p.name in skip or p.name.startswith("__"):
                continue
            if p.stem not in init_content:
                orphans.append(Orphan(
                    kind="orphan_module",
                    file_path=str(p.relative_to(self._root)),
                    name=p.stem,
                    description=f"Module '{p.stem}' not imported in __init__.py",
                ))

        return orphans

    def unused_helpers(self, relative_path: str) -> list[Orphan]:
        """Find helper functions that are defined but never called in a file."""
        full = self._root / relative_path
        if not full.is_file():
            return []

        try:
            source = full.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(full))
        except (SyntaxError, OSError):
            return []

        # Find all function definitions starting with _
        helpers: dict[str, int] = {}
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith("_"):
                helpers[node.name] = node.lineno

        # Find all function calls
        called: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    called.add(node.func.id)
                elif isinstance(node.func, ast.Attribute):
                    called.add(node.func.attr)

        orphans: list[Orphan] = []
        for name, line in helpers.items():
            if name not in called and name != "__init__":
                orphans.append(Orphan(
                    kind="orphan_helper",
                    file_path=relative_path,
                    name=name,
                    description=f"Helper function '{name}' (line {line}) is defined but never called",
                ))

        return orphans
