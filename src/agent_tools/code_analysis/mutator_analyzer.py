"""
Mutator analyzer — inspect existing mutators to understand patterns.

Parses mutator source files to extract technique details, variant counts,
metadata keys, and implementation patterns for agents to learn from.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class MutatorInfo:
    """Extracted information about a single mutator class."""

    class_name: str
    name: str  # NAME attribute value
    category: str  # CATEGORY attribute value
    description: str  # DESCRIPTION attribute value
    file_path: str
    line: int
    variant_count: int = 0
    has_metadata: bool = False
    metadata_keys: list[str] = field(default_factory=list)
    uses_lookup_table: bool = False
    helper_functions: list[str] = field(default_factory=list)
    complexity: str = "simple"  # "simple", "moderate", "complex"

    def to_dict(self) -> dict[str, Any]:
        return {
            "class_name": self.class_name,
            "name": self.name,
            "category": self.category,
            "description": self.description[:200],
            "file_path": self.file_path,
            "line": self.line,
            "variant_count": self.variant_count,
            "has_metadata": self.has_metadata,
            "metadata_keys": self.metadata_keys,
            "complexity": self.complexity,
        }


@dataclass
class ModuleAnalysis:
    """Analysis of a complete mutator module."""

    file_path: str
    module_name: str
    mutator_count: int = 0
    mutators: list[MutatorInfo] = field(default_factory=list)
    lookup_tables: list[str] = field(default_factory=list)
    helper_functions: list[str] = field(default_factory=list)
    total_lines: int = 0
    import_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "file_path": self.file_path,
            "module_name": self.module_name,
            "mutator_count": self.mutator_count,
            "mutators": [m.to_dict() for m in self.mutators],
            "lookup_tables": self.lookup_tables,
            "helper_functions": self.helper_functions,
            "total_lines": self.total_lines,
        }


class MutatorAnalyzer:
    """Analyze mutator source code to extract patterns and structure.

    Usage:
        analyzer = MutatorAnalyzer()

        # Analyze a single module
        analysis = analyzer.analyze_module("src/prompt_injection/encoding_format.py")

        # Analyze all mutator modules
        all_analyses = analyzer.analyze_all()

        # Find mutators using lookup tables
        table_users = analyzer.find_pattern("lookup_table")

        # Get common patterns across modules
        patterns = analyzer.common_patterns()
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    def analyze_module(self, relative_path: str) -> ModuleAnalysis:
        """Analyze a single mutator module file."""
        path = self._root / relative_path
        if not path.is_file():
            return ModuleAnalysis(file_path=relative_path, module_name=path.stem)

        try:
            source = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(path))
        except (SyntaxError, OSError):
            return ModuleAnalysis(file_path=relative_path, module_name=path.stem)

        analysis = ModuleAnalysis(
            file_path=relative_path,
            module_name=path.stem,
            total_lines=source.count("\n") + 1,
        )

        # Count imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import | ast.ImportFrom):
                analysis.import_count += 1

        # Find top-level constants (lookup tables)
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.startswith("_"):
                        if isinstance(node.value, ast.Dict | ast.List | ast.Set):
                            analysis.lookup_tables.append(target.id)

            # Find helper functions
            if isinstance(node, ast.FunctionDef) and node.name.startswith("_"):
                analysis.helper_functions.append(node.name)

            # Find mutator classes
            if isinstance(node, ast.ClassDef):
                info = self._analyze_class(node, relative_path, source)
                if info:
                    analysis.mutators.append(info)

        analysis.mutator_count = len(analysis.mutators)
        return analysis

    def analyze_all(self) -> list[ModuleAnalysis]:
        """Analyze all mutator modules."""
        pi_dir = self._root / "src" / "prompt_injection"
        if not pi_dir.is_dir():
            return []

        skip = {"__init__.py", "fitness.py", "coverage.py",
                "output_decoders.py", "metadata_schema.py", "attack_templates.py"}
        results = []
        for p in sorted(pi_dir.glob("*.py")):
            if p.name not in skip and not p.name.startswith("__"):
                rel = str(p.relative_to(self._root))
                results.append(self.analyze_module(rel))
        return results

    def find_pattern(self, pattern_type: str) -> list[MutatorInfo]:
        """Find mutators using a specific pattern.

        Pattern types: "lookup_table", "helper_function", "complex",
                       "simple", "multi_variant"
        """
        all_mutators: list[MutatorInfo] = []
        for analysis in self.analyze_all():
            for m in analysis.mutators:
                if pattern_type == "lookup_table" and m.uses_lookup_table:
                    all_mutators.append(m)
                elif pattern_type == "complex" and m.complexity == "complex":
                    all_mutators.append(m)
                elif pattern_type == "simple" and m.complexity == "simple":
                    all_mutators.append(m)
                elif pattern_type == "multi_variant" and m.variant_count > 2:
                    all_mutators.append(m)
                elif pattern_type == "helper_function" and m.helper_functions:
                    all_mutators.append(m)
        return all_mutators

    def common_patterns(self) -> dict[str, Any]:
        """Identify common patterns across all mutator modules."""
        analyses = self.analyze_all()
        total_mutators = sum(a.mutator_count for a in analyses)
        total_helpers = sum(len(a.helper_functions) for a in analyses)
        total_tables = sum(len(a.lookup_tables) for a in analyses)

        categories: dict[str, int] = {}
        complexities: dict[str, int] = {}
        for a in analyses:
            for m in a.mutators:
                categories[m.category] = categories.get(m.category, 0) + 1
                complexities[m.complexity] = complexities.get(m.complexity, 0) + 1

        return {
            "total_modules": len(analyses),
            "total_mutators": total_mutators,
            "avg_mutators_per_module": round(total_mutators / max(len(analyses), 1), 1),
            "total_helper_functions": total_helpers,
            "total_lookup_tables": total_tables,
            "categories": categories,
            "complexity_distribution": complexities,
        }

    def _analyze_class(
        self, node: ast.ClassDef, file_path: str, source: str
    ) -> MutatorInfo | None:
        """Extract info from a mutator class definition."""
        # Check if it has BaseMutator as a base
        bases = [
            b.id if isinstance(b, ast.Name) else
            b.attr if isinstance(b, ast.Attribute) else ""
            for b in node.bases
        ]
        if "BaseMutator" not in bases:
            return None

        name = ""
        category = ""
        description = ""

        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.Assign):
                for target in child.targets:
                    if isinstance(target, ast.Name):
                        if target.id == "NAME" and isinstance(child.value, ast.Constant):
                            name = str(child.value.value)
                        elif target.id == "CATEGORY" and isinstance(child.value, ast.Constant):
                            category = str(child.value.value)
                        elif target.id == "DESCRIPTION" and isinstance(child.value, ast.Constant):
                            description = str(child.value.value)

        if not name:
            return None

        # Count variants by looking at _apply method returns
        variant_count = 0
        has_metadata = False
        helper_funcs: list[str] = []

        for child in ast.walk(node):
            if isinstance(child, ast.Return) and isinstance(child.value, ast.List):
                variant_count = max(variant_count, len(child.value.elts))
            if isinstance(child, ast.Dict):
                for key in child.keys:
                    if isinstance(key, ast.Constant) and key.value in ("technique", "variant"):
                        has_metadata = True

        # Estimate complexity
        method_count = sum(
            1 for c in ast.iter_child_nodes(node)
            if isinstance(c, ast.FunctionDef)
        )
        line_count = node.end_lineno - node.lineno + 1 if node.end_lineno else 10
        complexity = (
            "complex" if line_count > 40 or method_count > 3
            else "moderate" if line_count > 20 or method_count > 2
            else "simple"
        )

        # Check for lookup table usage
        uses_lookup = bool(re.search(r"_[A-Z_]+\[", source[node.col_offset:]))

        return MutatorInfo(
            class_name=node.name,
            name=name,
            category=category,
            description=description,
            file_path=file_path,
            line=node.lineno,
            variant_count=variant_count,
            has_metadata=has_metadata,
            metadata_keys=["technique", "variant"] if has_metadata else [],
            uses_lookup_table=uses_lookup,
            helper_functions=helper_funcs,
            complexity=complexity,
        )
