"""
Symbol index — find classes, functions, and constants by name or pattern.

Uses lightweight AST parsing to build a searchable index of all Python
symbols in the project, so agents can locate definitions without grep.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class SymbolEntry:
    """A single symbol (class, function, constant) found in the codebase."""

    name: str
    kind: str  # "class", "function", "method", "constant", "variable"
    file_path: str
    line: int
    module: str = ""
    parent_class: str = ""
    docstring: str = ""
    decorators: list[str] = field(default_factory=list)
    bases: list[str] = field(default_factory=list)  # For classes

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "kind": self.kind,
            "file_path": self.file_path,
            "line": self.line,
            "module": self.module,
            "parent_class": self.parent_class,
            "docstring": self.docstring[:200] if self.docstring else "",
            "decorators": self.decorators,
            "bases": self.bases,
        }


class SymbolIndex:
    """Build and query a symbol index of the project.

    Usage:
        index = SymbolIndex()
        index.build()

        # Find all classes inheriting from BaseMutator
        mutators = index.classes_extending("BaseMutator")

        # Find a function by name
        results = index.find("register_mutator")

        # Find all symbols in a file
        symbols = index.symbols_in("src/prompt_injection/encoding_format.py")

        # Search by pattern
        matches = index.search(".*Mutator$", kind="class")
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)
        self._entries: list[SymbolEntry] = []
        self._built = False

    @property
    def root(self) -> Path:
        return self._root

    def build(self, file_glob: str = "src/**/*.py") -> int:
        """Parse all Python files and build the symbol index.

        Returns the number of symbols indexed.
        """
        self._entries = []
        for p in sorted(self._root.glob(file_glob)):
            if not p.is_file() or "__pycache__" in str(p):
                continue
            self._index_file(p)
        self._built = True
        return len(self._entries)

    def find(self, name: str, kind: str | None = None) -> list[SymbolEntry]:
        """Find symbols by exact name, optionally filtered by kind."""
        self._ensure_built()
        results = [e for e in self._entries if e.name == name]
        if kind:
            results = [e for e in results if e.kind == kind]
        return results

    def search(self, pattern: str, kind: str | None = None) -> list[SymbolEntry]:
        """Find symbols matching a regex pattern."""
        self._ensure_built()
        regex = re.compile(pattern)
        results = [e for e in self._entries if regex.search(e.name)]
        if kind:
            results = [e for e in results if e.kind == kind]
        return results

    def classes_extending(self, base_name: str) -> list[SymbolEntry]:
        """Find all classes that extend a given base class."""
        self._ensure_built()
        return [
            e for e in self._entries
            if e.kind == "class" and base_name in e.bases
        ]

    def decorated_with(self, decorator: str) -> list[SymbolEntry]:
        """Find all symbols with a specific decorator."""
        self._ensure_built()
        return [
            e for e in self._entries
            if decorator in e.decorators
        ]

    def symbols_in(self, relative_path: str) -> list[SymbolEntry]:
        """Get all symbols defined in a specific file."""
        self._ensure_built()
        norm = relative_path.replace("\\", "/")
        return [
            e for e in self._entries
            if e.module.replace("\\", "/") == norm
        ]

    def classes(self) -> list[SymbolEntry]:
        """Get all class definitions."""
        self._ensure_built()
        return [e for e in self._entries if e.kind == "class"]

    def functions(self) -> list[SymbolEntry]:
        """Get all top-level function definitions."""
        self._ensure_built()
        return [e for e in self._entries if e.kind == "function"]

    def methods_of(self, class_name: str) -> list[SymbolEntry]:
        """Get all methods of a specific class."""
        self._ensure_built()
        return [
            e for e in self._entries
            if e.kind == "method" and e.parent_class == class_name
        ]

    def constants(self) -> list[SymbolEntry]:
        """Get all module-level constants (UPPER_SNAKE_CASE)."""
        self._ensure_built()
        return [e for e in self._entries if e.kind == "constant"]

    def summary(self) -> dict[str, int]:
        """Get counts by symbol kind."""
        self._ensure_built()
        counts: dict[str, int] = {}
        for e in self._entries:
            counts[e.kind] = counts.get(e.kind, 0) + 1
        return counts

    def _ensure_built(self) -> None:
        if not self._built:
            self.build()

    def _index_file(self, path: Path) -> None:
        """Parse a single file and add its symbols to the index."""
        try:
            source = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(path))
        except (SyntaxError, OSError):
            return

        rel = str(path.relative_to(self._root))

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.ClassDef):
                self._index_class(node, rel)
            elif isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
                self._index_function(node, rel, parent_class="")
            elif isinstance(node, ast.Assign):
                self._index_assignment(node, rel)
            elif isinstance(node, ast.AnnAssign):
                self._index_ann_assignment(node, rel)

    def _index_class(self, node: ast.ClassDef, module: str) -> None:
        """Index a class and its methods."""
        bases = []
        for b in node.bases:
            if isinstance(b, ast.Name):
                bases.append(b.id)
            elif isinstance(b, ast.Attribute):
                bases.append(b.attr)

        decorators = self._extract_decorators(node)
        docstring = ast.get_docstring(node) or ""

        self._entries.append(SymbolEntry(
            name=node.name,
            kind="class",
            file_path=str(self._root / module),
            line=node.lineno,
            module=module,
            docstring=docstring,
            decorators=decorators,
            bases=bases,
        ))

        # Index methods
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.FunctionDef | ast.AsyncFunctionDef):
                self._index_function(child, module, parent_class=node.name)

    def _index_function(
        self, node: ast.FunctionDef | ast.AsyncFunctionDef,
        module: str, parent_class: str,
    ) -> None:
        """Index a function or method."""
        kind = "method" if parent_class else "function"
        decorators = self._extract_decorators(node)
        docstring = ast.get_docstring(node) or ""

        self._entries.append(SymbolEntry(
            name=node.name,
            kind=kind,
            file_path=str(self._root / module),
            line=node.lineno,
            module=module,
            parent_class=parent_class,
            docstring=docstring,
            decorators=decorators,
        ))

    def _index_assignment(self, node: ast.Assign, module: str) -> None:
        """Index module-level constant assignments (UPPER_SNAKE_CASE)."""
        for target in node.targets:
            if isinstance(target, ast.Name) and re.match(r"^[A-Z][A-Z_0-9]+$", target.id):
                self._entries.append(SymbolEntry(
                    name=target.id,
                    kind="constant",
                    file_path=str(self._root / module),
                    line=node.lineno,
                    module=module,
                ))

    def _index_ann_assignment(self, node: ast.AnnAssign, module: str) -> None:
        """Index annotated constant assignments (e.g., X: dict[...] = {...})."""
        if isinstance(node.target, ast.Name) and re.match(r"^[A-Z][A-Z_0-9]+$", node.target.id):
            self._entries.append(SymbolEntry(
                name=node.target.id,
                kind="constant",
                file_path=str(self._root / module),
                line=node.lineno,
                module=module,
            ))

    @staticmethod
    def _extract_decorators(node: ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
        """Extract decorator names from a node."""
        names = []
        for dec in node.decorator_list:
            if isinstance(dec, ast.Name):
                names.append(dec.id)
            elif isinstance(dec, ast.Attribute):
                names.append(dec.attr)
            elif isinstance(dec, ast.Call):
                if isinstance(dec.func, ast.Name):
                    names.append(dec.func.id)
                elif isinstance(dec.func, ast.Attribute):
                    names.append(dec.func.attr)
        return names
