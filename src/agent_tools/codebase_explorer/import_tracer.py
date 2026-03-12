"""
Import tracer — trace import dependencies between modules.

Agents use this to understand module coupling, find circular imports,
and determine the impact of changes before making them.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ImportEdge:
    """A single import relationship."""

    source_module: str
    target_module: str
    names: list[str] = field(default_factory=list)
    is_relative: bool = False
    line: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source_module,
            "target": self.target_module,
            "names": self.names,
            "is_relative": self.is_relative,
            "line": self.line,
        }


@dataclass
class DependencyGraph:
    """Complete import dependency graph."""

    edges: list[ImportEdge] = field(default_factory=list)
    modules: set[str] = field(default_factory=set)

    def dependents_of(self, module: str) -> list[str]:
        """Find modules that import the given module."""
        norm = module.replace("\\", "/")
        return sorted({
            e.source_module for e in self.edges
            if norm in e.target_module.replace("\\", "/")
        })

    def dependencies_of(self, module: str) -> list[str]:
        """Find modules imported by the given module."""
        norm = module.replace("\\", "/")
        return sorted({
            e.target_module for e in self.edges
            if e.source_module.replace("\\", "/") == norm
        })

    def find_cycles(self) -> list[list[str]]:
        """Detect circular import chains using DFS."""
        adjacency: dict[str, set[str]] = {}
        for e in self.edges:
            adjacency.setdefault(e.source_module, set()).add(e.target_module)

        visited: set[str] = set()
        path: list[str] = []
        on_path: set[str] = set()
        cycles: list[list[str]] = []

        def dfs(node: str) -> None:
            if node in on_path:
                idx = path.index(node)
                cycle = path[idx:] + [node]
                cycles.append(cycle)
                return
            if node in visited:
                return
            visited.add(node)
            on_path.add(node)
            path.append(node)
            for neighbor in adjacency.get(node, []):
                dfs(neighbor)
            path.pop()
            on_path.discard(node)

        for mod in sorted(adjacency):
            if mod not in visited:
                dfs(mod)

        return cycles

    def impact_of(self, module: str) -> dict[str, Any]:
        """Estimate the impact of changing a module."""
        direct = self.dependents_of(module)
        indirect: set[str] = set()
        queue = list(direct)
        seen = set(direct)
        while queue:
            current = queue.pop(0)
            deps = self.dependents_of(current)
            for d in deps:
                if d not in seen:
                    seen.add(d)
                    indirect.add(d)
                    queue.append(d)

        return {
            "module": module,
            "direct_dependents": direct,
            "indirect_dependents": sorted(indirect),
            "total_impact": len(direct) + len(indirect),
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "module_count": len(self.modules),
            "edge_count": len(self.edges),
            "edges": [e.to_dict() for e in self.edges],
        }


class ImportTracer:
    """Trace import dependencies across the project.

    Usage:
        tracer = ImportTracer()
        graph = tracer.trace()

        # What depends on encoding_format?
        deps = graph.dependents_of("src/prompt_injection/encoding_format.py")

        # Any circular imports?
        cycles = graph.find_cycles()

        # What's the blast radius of changing this module?
        impact = graph.impact_of("src/prompt_injection/__init__.py")
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    @property
    def root(self) -> Path:
        return self._root

    def trace(self, file_glob: str = "src/**/*.py") -> DependencyGraph:
        """Build the full dependency graph."""
        graph = DependencyGraph()

        for p in sorted(self._root.glob(file_glob)):
            if not p.is_file() or "__pycache__" in str(p):
                continue
            rel = str(p.relative_to(self._root))
            graph.modules.add(rel)
            edges = self._trace_file(p, rel)
            graph.edges.extend(edges)

        return graph

    def trace_file(self, relative_path: str) -> list[ImportEdge]:
        """Trace imports for a single file."""
        full = self._root / relative_path
        if not full.is_file():
            return []
        return self._trace_file(full, relative_path)

    def who_imports(self, module_name: str) -> list[ImportEdge]:
        """Find all files that import a given module name."""
        graph = self.trace()
        return [
            e for e in graph.edges
            if module_name in e.target_module or module_name in e.names
        ]

    def _trace_file(self, path: Path, rel_path: str) -> list[ImportEdge]:
        """Parse imports from a single file."""
        try:
            source = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(path))
        except (SyntaxError, OSError):
            return []

        edges: list[ImportEdge] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    edges.append(ImportEdge(
                        source_module=rel_path,
                        target_module=alias.name,
                        names=[alias.asname or alias.name],
                        is_relative=False,
                        line=node.lineno,
                    ))
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                is_relative = (node.level or 0) > 0
                names = [a.name for a in node.names]
                if is_relative and module:
                    # Resolve relative import
                    parts = Path(rel_path).parts
                    level = node.level or 1
                    if level <= len(parts):
                        base = "/".join(parts[:-level])
                        target = f"{base}/{module.replace('.', '/')}" if base else module.replace(".", "/")
                    else:
                        target = module
                else:
                    target = module.replace(".", "/") if module else ""

                edges.append(ImportEdge(
                    source_module=rel_path,
                    target_module=target,
                    names=names,
                    is_relative=is_relative,
                    line=node.lineno,
                ))

        return edges
