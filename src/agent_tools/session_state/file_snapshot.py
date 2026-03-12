"""
File snapshot store — save and restore file contents for rollback.

Before modifying files, agents snapshot the originals so they can
be restored if the task fails partway through.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class FileSnapshot:
    """A saved copy of a file's content."""

    path: str
    content: str
    existed: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "content_length": len(self.content),
            "existed": self.existed,
        }


class FileSnapshotStore:
    """Save and restore file snapshots for rollback support.

    Usage:
        store = FileSnapshotStore()

        # Snapshot before modifying
        store.snapshot("src/prompt_injection/__init__.py")
        store.snapshot("src/prompt_injection/coverage.py")

        # ... make changes ...

        # If something goes wrong, rollback
        store.rollback_all()

        # Or rollback a single file
        store.rollback("src/prompt_injection/__init__.py")

        # Clear snapshots after successful completion
        store.clear()
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)
        self._snapshots: dict[str, FileSnapshot] = {}

    @property
    def snapshot_count(self) -> int:
        return len(self._snapshots)

    def snapshot(self, relative_path: str) -> FileSnapshot:
        """Save a snapshot of a file's current content."""
        full = self._root / relative_path
        if full.is_file():
            content = full.read_text(encoding="utf-8", errors="replace")
            snap = FileSnapshot(path=relative_path, content=content, existed=True)
        else:
            snap = FileSnapshot(path=relative_path, content="", existed=False)
        self._snapshots[relative_path] = snap
        return snap

    def snapshot_multiple(self, paths: list[str]) -> int:
        """Snapshot multiple files at once. Returns count saved."""
        for p in paths:
            self.snapshot(p)
        return len(paths)

    def has_snapshot(self, relative_path: str) -> bool:
        """Check if a file has been snapshotted."""
        return relative_path in self._snapshots

    def rollback(self, relative_path: str) -> bool:
        """Restore a file to its snapshotted state."""
        snap = self._snapshots.get(relative_path)
        if snap is None:
            return False

        full = self._root / relative_path
        if snap.existed:
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text(snap.content, encoding="utf-8")
        else:
            # File didn't exist before — delete it
            if full.is_file():
                full.unlink()
        return True

    def rollback_all(self) -> int:
        """Restore all snapshotted files. Returns count restored."""
        count = 0
        for path in list(self._snapshots.keys()):
            if self.rollback(path):
                count += 1
        return count

    def changed_files(self) -> list[str]:
        """Get list of files that have changed since snapshot."""
        changed: list[str] = []
        for path, snap in self._snapshots.items():
            full = self._root / path
            if snap.existed:
                if full.is_file():
                    current = full.read_text(encoding="utf-8", errors="replace")
                    if current != snap.content:
                        changed.append(path)
                else:
                    changed.append(path)  # File was deleted
            else:
                if full.is_file():
                    changed.append(path)  # File was created
        return changed

    def clear(self) -> None:
        """Clear all snapshots (call after successful completion)."""
        self._snapshots = {}

    def summary(self) -> dict[str, Any]:
        """Get summary of snapshot state."""
        return {
            "total_snapshots": len(self._snapshots),
            "files": list(self._snapshots.keys()),
            "changed_files": self.changed_files(),
        }
