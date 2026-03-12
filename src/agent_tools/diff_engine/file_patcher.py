"""
File patcher — apply structured changes to files.

Takes a ChangeSet and applies all changes to the filesystem,
with dry-run support and rollback capability.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.agent_tools.diff_engine.change_builder import Change, ChangeSet


@dataclass
class PatchResult:
    """Result of applying a changeset."""

    success: bool
    changes_applied: int = 0
    changes_failed: int = 0
    errors: list[str] = field(default_factory=list)
    backups: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "changes_applied": self.changes_applied,
            "changes_failed": self.changes_failed,
            "errors": self.errors,
        }


class FilePatcher:
    """Apply structured changes to files.

    Usage:
        patcher = FilePatcher()

        # Dry run (preview without writing)
        result = patcher.dry_run(changeset)

        # Apply changes
        result = patcher.apply(changeset)

        # Apply a single change
        result = patcher.apply_change(change)
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    def dry_run(self, changeset: ChangeSet) -> PatchResult:
        """Preview changes without applying them."""
        result = PatchResult(success=True)

        for change in changeset.changes:
            path = self._root / change.file_path
            if not path.is_file() and change.kind != "append":
                result.errors.append(f"File not found: {change.file_path}")
                result.changes_failed += 1
                result.success = False
                continue

            if change.kind == "replace" and path.is_file():
                content = path.read_text(encoding="utf-8", errors="replace")
                if change.old_text not in content:
                    result.errors.append(
                        f"Text to replace not found in {change.file_path}: "
                        f"'{change.old_text[:50]}...'"
                    )
                    result.changes_failed += 1
                    result.success = False
                    continue

            if change.kind == "insert" and path.is_file():
                content = path.read_text(encoding="utf-8", errors="replace")
                if change.after_text not in content:
                    result.errors.append(
                        f"Insert marker not found in {change.file_path}: "
                        f"'{change.after_text[:50]}...'"
                    )
                    result.changes_failed += 1
                    result.success = False
                    continue

            if change.kind == "delete" and path.is_file():
                content = path.read_text(encoding="utf-8", errors="replace")
                if change.old_text not in content:
                    result.errors.append(
                        f"Text to delete not found in {change.file_path}: "
                        f"'{change.old_text[:50]}...'"
                    )
                    result.changes_failed += 1
                    result.success = False
                    continue

            result.changes_applied += 1

        return result

    def apply(self, changeset: ChangeSet) -> PatchResult:
        """Apply all changes in a changeset."""
        # First do a dry run
        dry = self.dry_run(changeset)
        if not dry.success:
            return dry

        result = PatchResult(success=True)

        for change in changeset.changes:
            try:
                self._apply_single(change)
                result.changes_applied += 1
            except Exception as exc:
                result.errors.append(f"Failed to apply change to {change.file_path}: {exc}")
                result.changes_failed += 1
                result.success = False

        return result

    def apply_change(self, change: Change) -> PatchResult:
        """Apply a single change."""
        result = PatchResult(success=True)
        try:
            self._apply_single(change)
            result.changes_applied = 1
        except Exception as exc:
            result.errors.append(str(exc))
            result.changes_failed = 1
            result.success = False
        return result

    def _apply_single(self, change: Change) -> None:
        """Apply a single change to a file."""
        path = self._root / change.file_path

        if change.kind == "replace":
            content = path.read_text(encoding="utf-8", errors="replace")
            if change.old_text not in content:
                raise ValueError(f"Text to replace not found in {change.file_path}")
            new_content = content.replace(change.old_text, change.new_text, 1)
            path.write_text(new_content, encoding="utf-8")

        elif change.kind == "insert":
            content = path.read_text(encoding="utf-8", errors="replace")
            if change.after_text not in content:
                raise ValueError(f"Insert marker not found in {change.file_path}")
            idx = content.index(change.after_text) + len(change.after_text)
            new_content = content[:idx] + "\n" + change.new_text + content[idx:]
            path.write_text(new_content, encoding="utf-8")

        elif change.kind == "append":
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.is_file():
                content = path.read_text(encoding="utf-8", errors="replace")
                new_content = content.rstrip("\n") + "\n" + change.new_text + "\n"
            else:
                new_content = change.new_text + "\n"
            path.write_text(new_content, encoding="utf-8")

        elif change.kind == "delete":
            content = path.read_text(encoding="utf-8", errors="replace")
            if change.old_text not in content:
                raise ValueError(f"Text to delete not found in {change.file_path}")
            new_content = content.replace(change.old_text, "", 1)
            path.write_text(new_content, encoding="utf-8")

        else:
            raise ValueError(f"Unknown change kind: {change.kind}")
