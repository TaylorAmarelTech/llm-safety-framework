"""
Execution tracker — track task execution results and maintain state.

Wraps the improvement log to provide task-specific tracking: which tasks
have been attempted, which succeeded, which failed, and what was produced.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class TaskExecution:
    """Record of a single task execution."""

    task_id: str
    task_title: str
    status: str  # "pending", "in_progress", "completed", "failed", "skipped"
    started_at: str = ""
    completed_at: str = ""
    agent: str = ""
    mutators_created: int = 0
    tests_created: int = 0
    files_changed: list[str] = field(default_factory=list)
    error: str = ""
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TaskExecution":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


class ExecutionTracker:
    """Track task execution state across sessions.

    Usage:
        tracker = ExecutionTracker()

        # Start a task
        tracker.start("task_001", "Implement base91 encoding", agent="claude-code")

        # Complete it
        tracker.complete(
            "task_001",
            mutators_created=2,
            tests_created=10,
            files_changed=["src/prompt_injection/encoding_advanced.py"],
        )

        # Check what's been done
        completed = tracker.completed_tasks()
        pending = tracker.pending_tasks()

        # Get summary
        print(tracker.summary())
    """

    def __init__(self, state_path: str | Path | None = None) -> None:
        if state_path is None:
            default_dir = Path(__file__).resolve().parent.parent.parent.parent / "data"
            default_dir.mkdir(parents=True, exist_ok=True)
            self._path = default_dir / "execution_tracker.json"
        else:
            self._path = Path(state_path)
        self._executions: dict[str, TaskExecution] = {}
        self._load()

    def _load(self) -> None:
        """Load state from disk."""
        if self._path.exists():
            try:
                data = json.loads(self._path.read_text(encoding="utf-8"))
                for item in data:
                    ex = TaskExecution.from_dict(item)
                    self._executions[ex.task_id] = ex
            except (json.JSONDecodeError, KeyError):
                pass

    def _save(self) -> None:
        """Persist state to disk."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        data = [ex.to_dict() for ex in self._executions.values()]
        self._path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def start(self, task_id: str, title: str, agent: str = "") -> TaskExecution:
        """Mark a task as started."""
        ex = TaskExecution(
            task_id=task_id,
            task_title=title,
            status="in_progress",
            started_at=datetime.now(tz=timezone.utc).isoformat(),
            agent=agent,
        )
        self._executions[task_id] = ex
        self._save()
        return ex

    def complete(
        self,
        task_id: str,
        mutators_created: int = 0,
        tests_created: int = 0,
        files_changed: list[str] | None = None,
        notes: str = "",
    ) -> TaskExecution:
        """Mark a task as completed."""
        if task_id not in self._executions:
            raise KeyError(f"Task '{task_id}' not found — call start() first")
        ex = self._executions[task_id]
        ex.status = "completed"
        ex.completed_at = datetime.now(tz=timezone.utc).isoformat()
        ex.mutators_created = mutators_created
        ex.tests_created = tests_created
        ex.files_changed = files_changed or []
        ex.notes = notes
        self._save()
        return ex

    def fail(self, task_id: str, error: str = "") -> TaskExecution:
        """Mark a task as failed."""
        if task_id not in self._executions:
            raise KeyError(f"Task '{task_id}' not found — call start() first")
        ex = self._executions[task_id]
        ex.status = "failed"
        ex.completed_at = datetime.now(tz=timezone.utc).isoformat()
        ex.error = error
        self._save()
        return ex

    def skip(self, task_id: str, title: str, reason: str = "") -> TaskExecution:
        """Mark a task as skipped."""
        ex = TaskExecution(
            task_id=task_id,
            task_title=title,
            status="skipped",
            notes=reason,
        )
        self._executions[task_id] = ex
        self._save()
        return ex

    def get(self, task_id: str) -> TaskExecution | None:
        """Get execution record for a task."""
        return self._executions.get(task_id)

    def is_completed(self, task_id: str) -> bool:
        """Check if a task has been completed."""
        ex = self._executions.get(task_id)
        return ex is not None and ex.status == "completed"

    def completed_tasks(self) -> list[TaskExecution]:
        """Get all completed tasks."""
        return [ex for ex in self._executions.values() if ex.status == "completed"]

    def failed_tasks(self) -> list[TaskExecution]:
        """Get all failed tasks."""
        return [ex for ex in self._executions.values() if ex.status == "failed"]

    def pending_tasks(self) -> list[TaskExecution]:
        """Get all in-progress tasks."""
        return [ex for ex in self._executions.values() if ex.status == "in_progress"]

    def all_executions(self) -> list[TaskExecution]:
        """Get all execution records."""
        return list(self._executions.values())

    def summary(self) -> dict[str, Any]:
        """Get execution summary."""
        execs = list(self._executions.values())
        return {
            "total_tasks": len(execs),
            "completed": len([e for e in execs if e.status == "completed"]),
            "failed": len([e for e in execs if e.status == "failed"]),
            "in_progress": len([e for e in execs if e.status == "in_progress"]),
            "skipped": len([e for e in execs if e.status == "skipped"]),
            "total_mutators_created": sum(e.mutators_created for e in execs),
            "total_tests_created": sum(e.tests_created for e in execs),
        }

    def clear(self) -> None:
        """Clear all execution records."""
        self._executions = {}
        self._save()
