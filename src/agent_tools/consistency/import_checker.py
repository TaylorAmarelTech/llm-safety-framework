"""
Import checker — verify all imports resolve after changes.

Scans for broken imports introduced by file moves, renames, or
deletions, and reports which files need updating.
"""

from __future__ import annotations

import ast
import importlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ImportIssue:
    """A detected import issue."""

    file_path: str
    line: int
    import_target: str
    issue: str  # "missing_module", "missing_name", "circular"
    suggestion: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "file_path": self.file_path,
            "line": self.line,
            "import_target": self.import_target,
            "issue": self.issue,
            "suggestion": self.suggestion,
        }


class ImportChecker:
    """Check for broken imports after code changes.

    Usage:
        checker = ImportChecker()

        # Check a specific file
        issues = checker.check_file("src/prompt_injection/my_module.py")

        # Check all prompt_injection modules
        issues = checker.check_package("src/prompt_injection")

        # Quick check — just the files that changed
        issues = checker.check_files(["file1.py", "file2.py"])
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    def check_file(self, relative_path: str) -> list[ImportIssue]:
        """Check all imports in a single file."""
        full = self._root / relative_path
        if not full.is_file():
            return [ImportIssue(
                file_path=relative_path, line=0,
                import_target=relative_path,
                issue="missing_module",
                suggestion="File does not exist",
            )]

        try:
            source = full.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(full))
        except SyntaxError as exc:
            return [ImportIssue(
                file_path=relative_path, line=exc.lineno or 0,
                import_target=relative_path,
                issue="syntax_error",
                suggestion=f"Fix syntax error: {exc.msg}",
            )]

        issues: list[ImportIssue] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if not self._module_exists(alias.name):
                        issues.append(ImportIssue(
                            file_path=relative_path,
                            line=node.lineno,
                            import_target=alias.name,
                            issue="missing_module",
                            suggestion=f"Module '{alias.name}' not found",
                        ))
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                level = node.level or 0
                if level == 0 and module.startswith("src."):
                    # Internal import — check if file exists
                    mod_path = module.replace(".", "/") + ".py"
                    pkg_path = module.replace(".", "/") + "/__init__.py"
                    if not (self._root / mod_path).is_file() and not (self._root / pkg_path).is_file():
                        issues.append(ImportIssue(
                            file_path=relative_path,
                            line=node.lineno,
                            import_target=module,
                            issue="missing_module",
                            suggestion=f"Internal module '{module}' not found",
                        ))

        return issues

    def check_files(self, relative_paths: list[str]) -> list[ImportIssue]:
        """Check imports in multiple files."""
        issues: list[ImportIssue] = []
        for p in relative_paths:
            issues.extend(self.check_file(p))
        return issues

    def check_package(self, package_path: str) -> list[ImportIssue]:
        """Check all Python files in a package directory."""
        pkg_dir = self._root / package_path
        if not pkg_dir.is_dir():
            return []

        issues: list[ImportIssue] = []
        for p in sorted(pkg_dir.rglob("*.py")):
            if "__pycache__" not in str(p):
                rel = str(p.relative_to(self._root))
                issues.extend(self.check_file(rel))
        return issues

    def _module_exists(self, module_name: str) -> bool:
        """Check if a module can be found (without importing it)."""
        # Check internal modules
        parts = module_name.replace(".", "/")
        if (self._root / (parts + ".py")).is_file():
            return True
        if (self._root / parts / "__init__.py").is_file():
            return True
        # Check stdlib and installed packages
        try:
            spec = importlib.util.find_spec(module_name)
            return spec is not None
        except (ModuleNotFoundError, ValueError):
            return False
