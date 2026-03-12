"""
Priority adjuster — dynamically re-prioritize tasks based on outcomes.

Uses feedback from ResultCollector and LearningStore to boost or
demote task priorities, making the planning loop adaptive.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.agent_tools.feedback_loop.result_collector import ResultCollector
from src.agent_tools.orchestrator.task_planner import ImprovementTask


@dataclass
class PriorityAdjustment:
    """A priority adjustment recommendation."""

    task_id: str
    original_priority: str
    adjusted_priority: str
    reason: str
    confidence: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "original_priority": self.original_priority,
            "adjusted_priority": self.adjusted_priority,
            "reason": self.reason,
            "confidence": self.confidence,
        }


PRIORITY_ORDER = ["critical", "high", "medium", "low"]


class PriorityAdjuster:
    """Adjust task priorities based on feedback signals.

    Usage:
        adjuster = PriorityAdjuster(collector)

        # Adjust a list of tasks
        adjustments = adjuster.adjust(tasks)

        # Apply adjustments
        adjuster.apply(tasks, adjustments)

        # Get a re-ordered task list
        ordered = adjuster.reorder(tasks)
    """

    def __init__(self, collector: ResultCollector | None = None) -> None:
        self._collector = collector or ResultCollector()

    def adjust(self, tasks: list[ImprovementTask]) -> list[PriorityAdjustment]:
        """Compute priority adjustments for a task list."""
        adjustments: list[PriorityAdjustment] = []

        # Get historical context
        failure_kinds = set()
        success_kinds = set()
        for o in self._collector.failures():
            failure_kinds.add(o.task_kind)
        for o in self._collector.successes():
            success_kinds.add(o.task_kind)

        for task in tasks:
            adjustment = self._compute_adjustment(
                task, failure_kinds, success_kinds
            )
            if adjustment:
                adjustments.append(adjustment)

        return adjustments

    def apply(
        self,
        tasks: list[ImprovementTask],
        adjustments: list[PriorityAdjustment],
    ) -> list[ImprovementTask]:
        """Apply adjustments to tasks in-place and return them."""
        adj_map = {a.task_id: a for a in adjustments}
        for task in tasks:
            if task.id in adj_map:
                task.priority = adj_map[task.id].adjusted_priority
        return tasks

    def reorder(self, tasks: list[ImprovementTask]) -> list[ImprovementTask]:
        """Adjust priorities and return tasks sorted by adjusted priority."""
        adjustments = self.adjust(tasks)
        self.apply(tasks, adjustments)
        return sorted(
            tasks,
            key=lambda t: PRIORITY_ORDER.index(t.priority)
            if t.priority in PRIORITY_ORDER else 9,
        )

    def _compute_adjustment(
        self,
        task: ImprovementTask,
        failure_kinds: set[str],
        success_kinds: set[str],
    ) -> PriorityAdjustment | None:
        """Compute a single adjustment based on feedback signals."""
        current_idx = (
            PRIORITY_ORDER.index(task.priority)
            if task.priority in PRIORITY_ORDER else 2
        )

        # Signal 1: Tasks of this kind have been failing — demote
        if task.kind in failure_kinds and task.kind not in success_kinds:
            new_idx = min(current_idx + 1, len(PRIORITY_ORDER) - 1)
            if new_idx != current_idx:
                return PriorityAdjustment(
                    task_id=task.id,
                    original_priority=task.priority,
                    adjusted_priority=PRIORITY_ORDER[new_idx],
                    reason=f"Tasks of kind '{task.kind}' have been failing",
                    confidence=0.6,
                )

        # Signal 2: Dependencies are unresolved — demote
        if task.dependencies:
            completed_ids = {
                o.task_id for o in self._collector.successes()
            }
            unresolved = [d for d in task.dependencies if d not in completed_ids]
            if unresolved:
                new_idx = min(current_idx + 1, len(PRIORITY_ORDER) - 1)
                if new_idx != current_idx:
                    return PriorityAdjustment(
                        task_id=task.id,
                        original_priority=task.priority,
                        adjusted_priority=PRIORITY_ORDER[new_idx],
                        reason=f"Unresolved dependencies: {', '.join(unresolved)}",
                        confidence=0.8,
                    )

        # Signal 3: Coverage is low in this area — boost
        if task.kind == "new_category" and task.estimated_mutators >= 10:
            if current_idx > 0:
                outcomes = self._collector.by_kind("new_category")
                recent_success = any(
                    o.success and o.coverage_delta > 0.01
                    for o in outcomes[-5:]
                )
                if recent_success or not outcomes:
                    new_idx = current_idx - 1
                    return PriorityAdjustment(
                        task_id=task.id,
                        original_priority=task.priority,
                        adjusted_priority=PRIORITY_ORDER[new_idx],
                        reason="New categories have been yielding good coverage gains",
                        confidence=0.5,
                    )

        return None
