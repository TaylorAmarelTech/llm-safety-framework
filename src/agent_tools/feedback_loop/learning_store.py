"""
Learning store — accumulate patterns from past task outcomes.

Extracts recurring patterns (which task kinds succeed, which fail,
common errors, effective strategies) and makes them queryable.
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome


@dataclass
class Pattern:
    """A recurring pattern extracted from outcomes."""

    kind: str  # "success_pattern", "failure_pattern", "naming_collision", etc.
    description: str
    frequency: int = 1
    confidence: float = 0.0  # 0.0–1.0
    examples: list[str] = field(default_factory=list)
    recommendation: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "description": self.description,
            "frequency": self.frequency,
            "confidence": self.confidence,
            "examples": self.examples[:5],
            "recommendation": self.recommendation,
        }


class LearningStore:
    """Extract and query patterns from historical task outcomes.

    Usage:
        store = LearningStore(collector)

        # Analyze all outcomes
        patterns = store.extract_patterns()

        # Get failure patterns
        failures = store.failure_patterns()

        # Get success strategies
        strategies = store.success_strategies()

        # Get lessons relevant to a task kind
        lessons = store.lessons_for("new_category")

        # Generate context for an agent about to start a task
        context = store.agent_context("new_category")
    """

    def __init__(self, collector: ResultCollector | None = None) -> None:
        self._collector = collector or ResultCollector()

    def extract_patterns(self) -> list[Pattern]:
        """Extract all patterns from historical outcomes."""
        patterns: list[Pattern] = []
        patterns.extend(self._task_kind_patterns())
        patterns.extend(self._error_patterns())
        patterns.extend(self._quality_patterns())
        return patterns

    def failure_patterns(self) -> list[Pattern]:
        """Get patterns from failed tasks."""
        failures = self._collector.failures()
        if not failures:
            return []

        error_counts: Counter[str] = Counter()
        for f in failures:
            if f.error:
                # Normalize error to category
                err_cat = self._categorize_error(f.error)
                error_counts[err_cat] += 1

        patterns = []
        for error, count in error_counts.most_common(10):
            examples = [
                f.error for f in failures
                if self._categorize_error(f.error) == error
            ][:3]
            patterns.append(Pattern(
                kind="failure_pattern",
                description=f"Recurring failure: {error}",
                frequency=count,
                confidence=min(count / max(len(failures), 1), 1.0),
                examples=examples,
                recommendation=self._recommend_for_error(error),
            ))
        return patterns

    def success_strategies(self) -> list[Pattern]:
        """Get patterns from successful tasks."""
        successes = self._collector.successes()
        if not successes:
            return []

        kind_quality: dict[str, list[float]] = {}
        for s in successes:
            kind_quality.setdefault(s.task_kind, []).append(s.quality_score)

        patterns = []
        for kind, scores in kind_quality.items():
            avg = sum(scores) / len(scores)
            patterns.append(Pattern(
                kind="success_pattern",
                description=f"{kind} tasks succeed with avg quality {avg:.2f}",
                frequency=len(scores),
                confidence=avg,
                recommendation=f"Continue using current approach for {kind} tasks",
            ))
        return patterns

    def lessons_for(self, task_kind: str) -> list[str]:
        """Get lessons learned relevant to a task kind."""
        outcomes = self._collector.by_kind(task_kind)
        lessons: list[str] = []
        for o in outcomes:
            lessons.extend(o.lessons)
        # Also include general lessons from failures
        for o in self._collector.failures():
            if o.lessons:
                lessons.extend(o.lessons)
        return list(dict.fromkeys(lessons))  # Deduplicate preserving order

    def agent_context(self, task_kind: str) -> str:
        """Generate context string for an agent about to start a task.

        Includes relevant lessons, common pitfalls, and success strategies.
        """
        lines = [f"# Lessons Learned for {task_kind} Tasks\n"]

        # Success rate
        outcomes = self._collector.by_kind(task_kind)
        if outcomes:
            success_count = len([o for o in outcomes if o.success])
            lines.append(
                f"Historical success rate: {success_count}/{len(outcomes)} "
                f"({success_count/len(outcomes)*100:.0f}%)\n"
            )

        # Specific lessons
        lessons = self.lessons_for(task_kind)
        if lessons:
            lines.append("## Lessons")
            for lesson in lessons[:10]:
                lines.append(f"- {lesson}")
            lines.append("")

        # Failure patterns
        failures = self.failure_patterns()
        if failures:
            lines.append("## Common Pitfalls")
            for p in failures[:5]:
                lines.append(f"- {p.description}")
                if p.recommendation:
                    lines.append(f"  → {p.recommendation}")
            lines.append("")

        # Quality benchmarks
        successes = [o for o in outcomes if o.success]
        if successes:
            avg_quality = sum(o.quality_score for o in successes) / len(successes)
            avg_mutators = sum(o.mutators_created for o in successes) / len(successes)
            lines.append("## Benchmarks")
            lines.append(f"- Average quality score: {avg_quality:.2f}")
            lines.append(f"- Average mutators per task: {avg_mutators:.1f}")

        return "\n".join(lines)

    def _task_kind_patterns(self) -> list[Pattern]:
        """Extract patterns by task kind."""
        outcomes = self._collector.recent(100)
        kind_results: dict[str, list[bool]] = {}
        for o in outcomes:
            kind_results.setdefault(o.task_kind, []).append(o.success)

        patterns = []
        for kind, results in kind_results.items():
            success_rate = sum(results) / len(results)
            if success_rate < 0.5 and len(results) >= 2:
                patterns.append(Pattern(
                    kind="low_success_rate",
                    description=f"{kind} tasks have low success rate ({success_rate:.0%})",
                    frequency=len(results),
                    confidence=1.0 - success_rate,
                    recommendation=f"Investigate why {kind} tasks fail frequently",
                ))
        return patterns

    def _error_patterns(self) -> list[Pattern]:
        """Extract patterns from error messages."""
        failures = self._collector.failures()
        collision_count = sum(
            1 for f in failures if "collision" in f.error.lower() or "duplicate" in f.error.lower()
        )
        patterns = []
        if collision_count >= 2:
            patterns.append(Pattern(
                kind="naming_collision",
                description="Frequent naming collisions in mutator NAMEs",
                frequency=collision_count,
                confidence=min(collision_count / 5, 1.0),
                recommendation="Always run check_collisions() before generating code",
            ))
        return patterns

    def _quality_patterns(self) -> list[Pattern]:
        """Extract patterns from quality scores."""
        successes = self._collector.successes()
        if len(successes) < 3:
            return []

        scores = [o.quality_score for o in successes if o.quality_score > 0]
        if not scores:
            return []

        avg = sum(scores) / len(scores)
        patterns = []
        if avg < 0.7:
            patterns.append(Pattern(
                kind="low_quality",
                description=f"Average quality score is low ({avg:.2f})",
                frequency=len(scores),
                confidence=0.7 - avg,
                recommendation="Run QualityScorer before committing; aim for > 0.7",
            ))
        return patterns

    @staticmethod
    def _categorize_error(error: str) -> str:
        """Categorize an error message into a general category."""
        err_lower = error.lower()
        if "collision" in err_lower or "duplicate" in err_lower:
            return "naming_collision"
        if "import" in err_lower:
            return "import_error"
        if "syntax" in err_lower:
            return "syntax_error"
        if "test" in err_lower and "fail" in err_lower:
            return "test_failure"
        if "timeout" in err_lower:
            return "timeout"
        return "other"

    @staticmethod
    def _recommend_for_error(error_category: str) -> str:
        """Get recommendation for an error category."""
        recommendations = {
            "naming_collision": "Run CategoryPlanner.check_collisions() before code generation",
            "import_error": "Verify module is imported in __init__.py and PYTHONPATH is set",
            "syntax_error": "Run CodeValidator.validate() before attempting execution",
            "test_failure": "Check test assertions match actual mutator output format",
            "timeout": "Simplify the algorithm or add early termination",
        }
        return recommendations.get(error_category, "Investigate the root cause")
