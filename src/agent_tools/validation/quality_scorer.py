"""
Quality scorer — assess the quality of generated mutator code.

Checks code structure, docstrings, naming conventions, metadata conformance,
and edge case handling. Produces a numerical score and actionable feedback.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class QualityReport:
    """Quality assessment of a mutator module."""

    module_path: str = ""
    overall_score: float = 0.0
    scores: dict[str, float] = field(default_factory=dict)
    feedback: list[str] = field(default_factory=list)
    passed: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "module_path": self.module_path,
            "overall_score": round(self.overall_score, 2),
            "scores": {k: round(v, 2) for k, v in self.scores.items()},
            "feedback": self.feedback,
            "passed": self.passed,
        }

    def summary(self) -> str:
        status = "PASS" if self.passed else "NEEDS WORK"
        lines = [
            f"[{status}] Quality: {self.overall_score:.0%}",
            f"  Module: {self.module_path}",
        ]
        for area, score in sorted(self.scores.items()):
            lines.append(f"  {area:20s}: {score:.0%}")
        if self.feedback:
            lines.append("  Feedback:")
            for fb in self.feedback[:5]:
                lines.append(f"    - {fb}")
        return "\n".join(lines)


class QualityScorer:
    """Score the quality of mutator module code.

    Usage:
        scorer = QualityScorer()

        # Score a file
        report = scorer.score_file("src/prompt_injection/phonetic_obfuscation.py")

        # Score code string
        report = scorer.score_code(code_string, "my_module.py")
    """

    PASS_THRESHOLD = 0.6

    def score_file(self, path: str | Path) -> QualityReport:
        """Score a Python file."""
        p = Path(path)
        if not p.exists():
            return QualityReport(
                module_path=str(path),
                overall_score=0.0,
                passed=False,
                feedback=[f"File not found: {path}"],
            )
        code = p.read_text(encoding="utf-8")
        return self.score_code(code, str(path))

    def score_code(self, code: str, label: str = "module") -> QualityReport:
        """Score a code string."""
        report = QualityReport(module_path=label)

        report.scores["docstrings"] = self._score_docstrings(code, report)
        report.scores["naming"] = self._score_naming(code, report)
        report.scores["structure"] = self._score_structure(code, report)
        report.scores["metadata"] = self._score_metadata(code, report)
        report.scores["type_hints"] = self._score_type_hints(code, report)
        report.scores["imports"] = self._score_imports(code, report)

        if report.scores:
            report.overall_score = sum(report.scores.values()) / len(report.scores)

        report.passed = report.overall_score >= self.PASS_THRESHOLD
        return report

    def _score_docstrings(self, code: str, report: QualityReport) -> float:
        """Check docstring coverage."""
        score = 0.0

        # Module docstring
        if code.strip().startswith('"""') or code.strip().startswith("'''"):
            score += 0.4
        else:
            report.feedback.append("Missing module docstring")

        # Class docstrings
        classes = re.findall(r"class\s+\w+", code)
        classes_with_docs = re.findall(r'class\s+\w+[^:]*:\s*\n\s*"""', code)
        if classes:
            ratio = len(classes_with_docs) / len(classes)
            score += 0.6 * ratio
            if ratio < 1.0:
                report.feedback.append(
                    f"{len(classes) - len(classes_with_docs)}/{len(classes)} classes missing docstrings"
                )
        else:
            score += 0.3  # No classes to document

        return score

    def _score_naming(self, code: str, report: QualityReport) -> float:
        """Check naming conventions."""
        score = 1.0

        # Check mutator NAME format (snake_case)
        names = re.findall(r'NAME\s*=\s*"([^"]+)"', code)
        for name in names:
            if name != name.lower() or " " in name:
                score -= 0.2
                report.feedback.append(f"NAME '{name}' should be snake_case")

        # Check class names (PascalCase ending in Mutator)
        classes = re.findall(r"class\s+(\w+)\(BaseMutator\)", code)
        for cls in classes:
            if not cls.endswith("Mutator"):
                score -= 0.1
                report.feedback.append(f"Class '{cls}' should end with 'Mutator'")

        return max(0.0, score)

    def _score_structure(self, code: str, report: QualityReport) -> float:
        """Check structural patterns."""
        score = 0.0

        # Has @register_mutator decorators
        if "@register_mutator" in code:
            score += 0.3
        else:
            report.feedback.append("Missing @register_mutator decorators")

        # Has _apply method
        if "def _apply(" in code:
            score += 0.3
        else:
            report.feedback.append("Missing _apply() method")

        # Returns proper tuple structure
        if "return [" in code:
            score += 0.2
        else:
            report.feedback.append("_apply should return a list")

        # Has CATEGORY attribute
        if 'CATEGORY = "' in code:
            score += 0.2

        return score

    def _score_metadata(self, code: str, report: QualityReport) -> float:
        """Check metadata conformance."""
        score = 0.0

        # Has technique key in metadata dicts
        technique_count = len(re.findall(r'"technique":', code))
        variant_count = len(re.findall(r'"variant":', code))

        if technique_count > 0:
            score += 0.5
        else:
            report.feedback.append("No 'technique' key found in metadata dicts")

        if variant_count > 0:
            score += 0.5
        else:
            report.feedback.append("No 'variant' key found in metadata dicts")

        return score

    def _score_type_hints(self, code: str, report: QualityReport) -> float:
        """Check type hint usage."""
        score = 0.5  # Base score

        if "from __future__ import annotations" in code:
            score += 0.25

        # Check function signatures have return types
        funcs = re.findall(r"def\s+\w+\([^)]*\)\s*->", code)
        all_funcs = re.findall(r"def\s+\w+\(", code)
        if all_funcs:
            ratio = len(funcs) / len(all_funcs)
            score += 0.25 * ratio

        return min(1.0, score)

    def _score_imports(self, code: str, report: QualityReport) -> float:
        """Check import patterns."""
        score = 0.5

        # Uses proper import path
        if "from src.prompt_injection import BaseMutator, register_mutator" in code:
            score += 0.5
        elif "from src.prompt_injection import" in code:
            score += 0.3
        else:
            report.feedback.append("Missing proper import of BaseMutator/register_mutator")

        return score
