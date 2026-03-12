"""
Transaction — atomic multi-file changes with automatic rollback.

Wraps a set of file modifications in a transaction that either
succeeds completely or rolls everything back.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from src.agent_tools.session_state.file_snapshot import FileSnapshotStore


@dataclass
class TransactionResult:
    """Result of a transaction execution."""

    success: bool
    files_changed: list[str] = field(default_factory=list)
    error: str = ""
    rolled_back: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "files_changed": self.files_changed,
            "error": self.error,
            "rolled_back": self.rolled_back,
        }


class Transaction:
    """Execute multi-file changes atomically with rollback.

    Usage:
        tx = Transaction("Add encoding_advanced category")

        # Declare which files will be touched
        tx.will_modify("src/prompt_injection/__init__.py")
        tx.will_modify("src/prompt_injection/coverage.py")
        tx.will_create("src/prompt_injection/encoding_advanced.py")
        tx.will_create("tests/test_encoding_advanced.py")

        # Execute with automatic rollback on failure
        result = tx.execute(lambda: my_modification_function())

        # Or use as context manager
        with Transaction("My changes") as tx:
            tx.will_modify("file.py")
            # ... make changes ...
            # Rolls back automatically if exception is raised
    """

    def __init__(
        self,
        description: str = "",
        root: str | Path | None = None,
    ) -> None:
        self._description = description
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)
        self._snapshot_store = FileSnapshotStore(root=self._root)
        self._files_to_modify: list[str] = []
        self._files_to_create: list[str] = []
        self._committed = False

    def will_modify(self, relative_path: str) -> "Transaction":
        """Declare that this file will be modified."""
        self._files_to_modify.append(relative_path)
        return self

    def will_create(self, relative_path: str) -> "Transaction":
        """Declare that this file will be created."""
        self._files_to_create.append(relative_path)
        return self

    def execute(self, action: Callable[[], None]) -> TransactionResult:
        """Execute an action with automatic rollback on failure.

        Takes snapshots, runs the action, and rolls back if it raises.
        """
        # Take snapshots
        for path in self._files_to_modify:
            self._snapshot_store.snapshot(path)
        for path in self._files_to_create:
            self._snapshot_store.snapshot(path)  # Will record as non-existent

        try:
            action()
            self._committed = True
            changed = self._snapshot_store.changed_files()
            self._snapshot_store.clear()
            return TransactionResult(
                success=True,
                files_changed=changed,
            )
        except Exception as exc:
            # Rollback
            self._snapshot_store.rollback_all()
            self._snapshot_store.clear()
            return TransactionResult(
                success=False,
                error=str(exc),
                rolled_back=True,
            )

    def __enter__(self) -> "Transaction":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        if exc_type is not None and not self._committed:
            # Take snapshots if not already done
            self._snapshot_store.rollback_all()
            self._snapshot_store.clear()
        elif exc_type is None:
            self._committed = True
            self._snapshot_store.clear()
        return False  # Don't suppress exceptions

    @property
    def description(self) -> str:
        return self._description

    def summary(self) -> dict[str, Any]:
        return {
            "description": self._description,
            "files_to_modify": self._files_to_modify,
            "files_to_create": self._files_to_create,
            "committed": self._committed,
            "snapshots": self._snapshot_store.snapshot_count,
        }
