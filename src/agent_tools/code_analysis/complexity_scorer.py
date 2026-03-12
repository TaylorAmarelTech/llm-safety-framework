"""
Complexity scorer — estimate code complexity for quality assessment.

Uses AST analysis to compute cyclomatic complexity, nesting depth,
and other metrics that help agents decide when refactoring is needed.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ComplexityReport:
    """Complexity analysis for a file or function."""

    name: str
    file_path: str
    cyclomatic_complexity: int = 1
    max_nesting_depth: int = 0
    line_count: int = 0
    function_count: int = 0
    class_count: int = 0
    branch_count: int = 0  # if/elif/else/for/while/try/except
    rating: str = "A"  # A (simple) through F (very complex)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "file_path": self.file_path,
            "cyclomatic_complexity": self.cyclomatic_complexity,
            "max_nesting_depth": self.max_nesting_depth,
            "line_count": self.line_count,
            "function_count": self.function_count,
            "class_count": self.class_count,
            "branch_count": self.branch_count,
            "rating": self.rating,
        }


class ComplexityScorer:
    """Score code complexity using AST analysis.

    Usage:
        scorer = ComplexityScorer()

        # Score a file
        report = scorer.score_file("src/prompt_injection/encoding_format.py")

        # Score a specific function
        report = scorer.score_function(source_code, "my_function")

        # Score all mutator modules
        reports = scorer.score_all_mutators()

        # Find complex functions needing refactoring
        complex_fns = scorer.find_complex(threshold=10)
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    def score_file(self, relative_path: str) -> ComplexityReport:
        """Score complexity of an entire file."""
        path = self._root / relative_path
        if not path.is_file():
            return ComplexityReport(name=path.stem, file_path=relative_path)

        try:
            source = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(path))
        except (SyntaxError, OSError):
            return ComplexityReport(name=path.stem, file_path=relative_path)

        cc = self._cyclomatic_complexity(tree)
        nesting = self._max_nesting(tree)
        branches = self._count_branches(tree)

        func_count = sum(
            1 for n in ast.walk(tree)
            if isinstance(n, ast.FunctionDef | ast.AsyncFunctionDef)
        )
        class_count = sum(
            1 for n in ast.walk(tree)
            if isinstance(n, ast.ClassDef)
        )

        return ComplexityReport(
            name=path.stem,
            file_path=relative_path,
            cyclomatic_complexity=cc,
            max_nesting_depth=nesting,
            line_count=source.count("\n") + 1,
            function_count=func_count,
            class_count=class_count,
            branch_count=branches,
            rating=self._rate(cc),
        )

    def score_function(self, source: str, function_name: str) -> ComplexityReport:
        """Score complexity of a specific function."""
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return ComplexityReport(name=function_name, file_path="<source>")

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
                if node.name == function_name:
                    cc = self._cyclomatic_complexity(node)
                    nesting = self._max_nesting(node)
                    line_count = (node.end_lineno or node.lineno) - node.lineno + 1
                    return ComplexityReport(
                        name=function_name,
                        file_path="<source>",
                        cyclomatic_complexity=cc,
                        max_nesting_depth=nesting,
                        line_count=line_count,
                        branch_count=self._count_branches(node),
                        rating=self._rate(cc),
                    )

        return ComplexityReport(name=function_name, file_path="<source>")

    def score_all_mutators(self) -> list[ComplexityReport]:
        """Score complexity of all mutator modules."""
        pi_dir = self._root / "src" / "prompt_injection"
        if not pi_dir.is_dir():
            return []

        results = []
        for p in sorted(pi_dir.glob("*.py")):
            if not p.name.startswith("__"):
                rel = str(p.relative_to(self._root))
                results.append(self.score_file(rel))
        return results

    def find_complex(self, threshold: int = 10) -> list[ComplexityReport]:
        """Find modules with cyclomatic complexity above threshold."""
        return [
            r for r in self.score_all_mutators()
            if r.cyclomatic_complexity >= threshold
        ]

    def _cyclomatic_complexity(self, node: ast.AST) -> int:
        """Compute cyclomatic complexity (McCabe's metric)."""
        cc = 1
        for child in ast.walk(node):
            if isinstance(child, ast.If | ast.While | ast.For):
                cc += 1
            elif isinstance(child, ast.ExceptHandler):
                cc += 1
            elif isinstance(child, ast.BoolOp):
                cc += len(child.values) - 1
            elif isinstance(child, ast.Assert):
                cc += 1
            elif isinstance(child, ast.comprehension):
                cc += 1 + len(child.ifs)
        return cc

    def _max_nesting(self, node: ast.AST, depth: int = 0) -> int:
        """Find maximum nesting depth."""
        max_depth = depth
        nesting_nodes = (ast.If, ast.For, ast.While, ast.With, ast.Try)

        for child in ast.iter_child_nodes(node):
            if isinstance(child, nesting_nodes):
                child_depth = self._max_nesting(child, depth + 1)
                max_depth = max(max_depth, child_depth)
            else:
                child_depth = self._max_nesting(child, depth)
                max_depth = max(max_depth, child_depth)
        return max_depth

    def _count_branches(self, node: ast.AST) -> int:
        """Count branching statements."""
        count = 0
        for child in ast.walk(node):
            if isinstance(child, ast.If | ast.For | ast.While |
                          ast.Try | ast.ExceptHandler):
                count += 1
        return count

    @staticmethod
    def _rate(cc: int) -> str:
        """Rate complexity: A=simple, F=very complex."""
        if cc <= 5:
            return "A"
        if cc <= 10:
            return "B"
        if cc <= 20:
            return "C"
        if cc <= 30:
            return "D"
        if cc <= 50:
            return "E"
        return "F"
