"""
Session manager — track the current agent session state.

Maintains what task is active, which files are being modified,
and provides session context for agent prompts.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class SessionState:
    """Current state of an agent session."""

    session_id: str
    started_at: str = ""
    agent: str = ""
    current_task_id: str = ""
    current_task_title: str = ""
    status: str = "active"  # "active", "paused", "completed", "failed"
    files_modified: list[str] = field(default_factory=list)
    files_created: list[str] = field(default_factory=list)
    mutators_added: int = 0
    tests_added: int = 0
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SessionState":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


class SessionManager:
    """Manage agent session state with persistence.

    Usage:
        mgr = SessionManager()

        # Start a session
        session = mgr.start("claude-code")

        # Set current task
        mgr.set_task("task_001", "Implement base91 encoding")

        # Track file changes
        mgr.file_modified("src/prompt_injection/encoding_advanced.py")
        mgr.file_created("tests/test_encoding_advanced.py")

        # Add notes
        mgr.add_note("Found name collision with pig_latin — renamed")

        # Complete
        mgr.complete()

        # Get session context for prompts
        context = mgr.context_string()
    """

    def __init__(self, state_path: str | Path | None = None) -> None:
        if state_path is None:
            default_dir = Path(__file__).resolve().parent.parent.parent.parent / "data"
            default_dir.mkdir(parents=True, exist_ok=True)
            self._path = default_dir / "session_state.json"
        else:
            self._path = Path(state_path)
        self._state: SessionState | None = None
        self._load()

    def _load(self) -> None:
        if self._path.exists():
            try:
                data = json.loads(self._path.read_text(encoding="utf-8"))
                self._state = SessionState.from_dict(data)
                if self._state.status == "completed":
                    self._state = None
            except (json.JSONDecodeError, KeyError):
                pass

    def _save(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        if self._state:
            self._path.write_text(
                json.dumps(self._state.to_dict(), indent=2), encoding="utf-8"
            )

    @property
    def active(self) -> bool:
        """Whether there's an active session."""
        return self._state is not None and self._state.status == "active"

    @property
    def current(self) -> SessionState | None:
        """Get current session state."""
        return self._state

    def start(self, agent: str = "", session_id: str = "") -> SessionState:
        """Start a new session."""
        import uuid
        self._state = SessionState(
            session_id=session_id or str(uuid.uuid4())[:8],
            started_at=datetime.now(tz=timezone.utc).isoformat(),
            agent=agent,
            status="active",
        )
        self._save()
        return self._state

    def set_task(self, task_id: str, title: str) -> None:
        """Set the current task being worked on."""
        if self._state:
            self._state.current_task_id = task_id
            self._state.current_task_title = title
            self._save()

    def file_modified(self, path: str) -> None:
        """Record that a file was modified."""
        if self._state and path not in self._state.files_modified:
            self._state.files_modified.append(path)
            self._save()

    def file_created(self, path: str) -> None:
        """Record that a file was created."""
        if self._state and path not in self._state.files_created:
            self._state.files_created.append(path)
            self._save()

    def add_note(self, note: str) -> None:
        """Add a session note."""
        if self._state:
            self._state.notes.append(note)
            self._save()

    def increment_mutators(self, count: int = 1) -> None:
        """Increment mutator count."""
        if self._state:
            self._state.mutators_added += count
            self._save()

    def increment_tests(self, count: int = 1) -> None:
        """Increment test count."""
        if self._state:
            self._state.tests_added += count
            self._save()

    def complete(self) -> SessionState | None:
        """Mark session as completed."""
        if self._state:
            self._state.status = "completed"
            self._save()
            state = self._state
            self._state = None
            return state
        return None

    def fail(self, reason: str = "") -> SessionState | None:
        """Mark session as failed."""
        if self._state:
            self._state.status = "failed"
            if reason:
                self._state.notes.append(f"FAILED: {reason}")
            self._save()
            state = self._state
            self._state = None
            return state
        return None

    def context_string(self) -> str:
        """Generate context string for agent prompts."""
        if not self._state:
            return "No active session."

        lines = [
            f"# Active Session: {self._state.session_id}",
            f"Agent: {self._state.agent or 'unknown'}",
            f"Started: {self._state.started_at}",
        ]
        if self._state.current_task_id:
            lines.append(f"Current task: {self._state.current_task_title} ({self._state.current_task_id})")
        if self._state.files_modified:
            lines.append(f"Files modified: {', '.join(self._state.files_modified)}")
        if self._state.files_created:
            lines.append(f"Files created: {', '.join(self._state.files_created)}")
        if self._state.mutators_added:
            lines.append(f"Mutators added: {self._state.mutators_added}")
        if self._state.notes:
            lines.append(f"Notes: {'; '.join(self._state.notes[-3:])}")
        return "\n".join(lines)
