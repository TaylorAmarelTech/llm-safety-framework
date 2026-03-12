"""
Pattern detector — identify code patterns and anti-patterns.

Scans for common issues like missing metadata, inconsistent naming,
unused helpers, and other patterns that agents should fix or follow.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class PatternMatch:
    """A detected pattern or anti-pattern in code."""

    kind: str  # "good_pattern", "anti_pattern", "convention_violation"
    name: str
    description: str
    file_path: str
    line: int = 0
    severity: str = "info"  # "info", "warning", "error"
    suggestion: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "name": self.name,
            "description": self.description,
            "file_path": self.file_path,
            "line": self.line,
            "severity": self.severity,
            "suggestion": self.suggestion,
        }


class PatternDetector:
    """Detect code patterns, anti-patterns, and convention violations.

    Usage:
        detector = PatternDetector()

        # Scan a file
        issues = detector.scan_file("src/prompt_injection/my_module.py")

        # Scan all mutator modules
        all_issues = detector.scan_all()

        # Get only errors
        errors = detector.errors_only()
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    def scan_file(self, relative_path: str) -> list[PatternMatch]:
        """Scan a single file for patterns and issues."""
        path = self._root / relative_path
        if not path.is_file():
            return []

        try:
            source = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(path))
        except (SyntaxError, OSError) as exc:
            return [PatternMatch(
                kind="anti_pattern",
                name="syntax_error",
                description=f"File has syntax errors: {exc}",
                file_path=relative_path,
                severity="error",
            )]

        issues: list[PatternMatch] = []
        issues.extend(self._check_mutator_conventions(tree, relative_path))
        issues.extend(self._check_naming(tree, relative_path))
        issues.extend(self._check_docstrings(tree, relative_path))
        issues.extend(self._check_error_handling(tree, relative_path))
        issues.extend(self._check_imports(tree, relative_path, source))
        return issues

    def scan_all(self) -> list[PatternMatch]:
        """Scan all mutator modules."""
        pi_dir = self._root / "src" / "prompt_injection"
        if not pi_dir.is_dir():
            return []

        issues: list[PatternMatch] = []
        for p in sorted(pi_dir.glob("*.py")):
            if not p.name.startswith("__"):
                rel = str(p.relative_to(self._root))
                issues.extend(self.scan_file(rel))
        return issues

    def errors_only(self) -> list[PatternMatch]:
        """Get only error-severity issues from all modules."""
        return [i for i in self.scan_all() if i.severity == "error"]

    def warnings_only(self) -> list[PatternMatch]:
        """Get only warning-severity issues."""
        return [i for i in self.scan_all() if i.severity == "warning"]

    def _check_mutator_conventions(
        self, tree: ast.AST, file_path: str
    ) -> list[PatternMatch]:
        """Check mutator-specific conventions."""
        issues: list[PatternMatch] = []

        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue

            bases = [
                b.id if isinstance(b, ast.Name) else ""
                for b in node.bases
            ]
            if "BaseMutator" not in bases:
                continue

            # Check required attributes
            attrs = {}
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name) and isinstance(child.value, ast.Constant):
                            attrs[target.id] = child.value.value

            for required in ("NAME", "CATEGORY", "DESCRIPTION"):
                if required not in attrs:
                    issues.append(PatternMatch(
                        kind="convention_violation",
                        name="missing_attribute",
                        description=f"Class {node.name} missing {required} attribute",
                        file_path=file_path,
                        line=node.lineno,
                        severity="error",
                        suggestion=f"Add {required} = '...' as class attribute",
                    ))

            # Check for _apply method
            methods = [
                c.name for c in ast.iter_child_nodes(node)
                if isinstance(c, ast.FunctionDef)
            ]
            if "_apply" not in methods:
                issues.append(PatternMatch(
                    kind="convention_violation",
                    name="missing_apply",
                    description=f"Class {node.name} missing _apply() method",
                    file_path=file_path,
                    line=node.lineno,
                    severity="error",
                    suggestion="Implement _apply(self, text: str) -> list[tuple[str, str, dict]]",
                ))

            # Check NAME uniqueness pattern (just warn about short names)
            if "NAME" in attrs and len(str(attrs["NAME"])) < 3:
                issues.append(PatternMatch(
                    kind="anti_pattern",
                    name="short_name",
                    description=f"Mutator NAME '{attrs['NAME']}' is very short",
                    file_path=file_path,
                    line=node.lineno,
                    severity="warning",
                    suggestion="Use descriptive NAME to avoid collisions",
                ))

        return issues

    def _check_naming(self, tree: ast.AST, file_path: str) -> list[PatternMatch]:
        """Check naming conventions."""
        issues: list[PatternMatch] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if not re.match(r"^[A-Z][a-zA-Z0-9]+$", node.name):
                    issues.append(PatternMatch(
                        kind="convention_violation",
                        name="class_naming",
                        description=f"Class '{node.name}' doesn't follow PascalCase",
                        file_path=file_path,
                        line=node.lineno,
                        severity="info",
                    ))
            elif isinstance(node, ast.FunctionDef):
                if not node.name.startswith("_") and not re.match(
                    r"^[a-z][a-z0-9_]*$", node.name
                ):
                    issues.append(PatternMatch(
                        kind="convention_violation",
                        name="function_naming",
                        description=f"Function '{node.name}' doesn't follow snake_case",
                        file_path=file_path,
                        line=node.lineno,
                        severity="info",
                    ))

        return issues

    def _check_docstrings(self, tree: ast.AST, file_path: str) -> list[PatternMatch]:
        """Check for missing docstrings on public classes/functions."""
        issues: list[PatternMatch] = []

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.ClassDef):
                if not ast.get_docstring(node):
                    issues.append(PatternMatch(
                        kind="anti_pattern",
                        name="missing_docstring",
                        description=f"Class '{node.name}' has no docstring",
                        file_path=file_path,
                        line=node.lineno,
                        severity="info",
                        suggestion="Add a docstring describing the class purpose",
                    ))

        return issues

    def _check_error_handling(
        self, tree: ast.AST, file_path: str
    ) -> list[PatternMatch]:
        """Check for bare except clauses and overly broad catches."""
        issues: list[PatternMatch] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                issues.append(PatternMatch(
                    kind="anti_pattern",
                    name="bare_except",
                    description="Bare except: clause catches all exceptions",
                    file_path=file_path,
                    line=node.lineno,
                    severity="warning",
                    suggestion="Catch specific exceptions (e.g., ValueError, OSError)",
                ))

        return issues

    def _check_imports(
        self, tree: ast.AST, file_path: str, source: str
    ) -> list[PatternMatch]:
        """Check for import issues."""
        issues: list[PatternMatch] = []

        # Check for wildcard imports
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == "*":
                        issues.append(PatternMatch(
                            kind="anti_pattern",
                            name="wildcard_import",
                            description=f"Wildcard import from {node.module}",
                            file_path=file_path,
                            line=node.lineno,
                            severity="warning",
                            suggestion="Import specific names instead of using *",
                        ))

        return issues
