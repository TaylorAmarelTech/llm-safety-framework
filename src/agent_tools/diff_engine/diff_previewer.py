"""
Diff previewer — generate human-readable diffs for review.

Formats changes as unified diffs, side-by-side comparisons,
or summary views for agents and users to review before applying.
"""

from __future__ import annotations

import difflib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.agent_tools.diff_engine.change_builder import ChangeSet


@dataclass
class DiffView:
    """A rendered diff view."""

    file_path: str
    format: str  # "unified", "summary", "context"
    content: str
    additions: int = 0
    deletions: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "file_path": self.file_path,
            "format": self.format,
            "content": self.content[:2000],
            "additions": self.additions,
            "deletions": self.deletions,
        }


class DiffPreviewer:
    """Generate human-readable diffs for code changes.

    Usage:
        previewer = DiffPreviewer()

        # Preview a changeset as unified diff
        diffs = previewer.unified(changeset)

        # Preview as summary
        summary = previewer.summary(changeset)

        # Diff two strings
        diff = previewer.diff_strings(old_text, new_text, filename="file.py")
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    def unified(self, changeset: ChangeSet, context_lines: int = 3) -> list[DiffView]:
        """Generate unified diffs for all changes in a changeset."""
        views: list[DiffView] = []

        for change in changeset.changes:
            path = self._root / change.file_path
            if not path.is_file() and change.kind != "append":
                continue

            if change.kind == "append" and not path.is_file():
                old_lines: list[str] = []
            else:
                old_content = path.read_text(encoding="utf-8", errors="replace")
                old_lines = old_content.splitlines(keepends=True)

            # Simulate the change
            new_content = self._simulate_change(change, path)
            new_lines = new_content.splitlines(keepends=True)

            diff = difflib.unified_diff(
                old_lines,
                new_lines,
                fromfile=f"a/{change.file_path}",
                tofile=f"b/{change.file_path}",
                n=context_lines,
            )
            diff_text = "".join(diff)

            additions = sum(1 for line in diff_text.splitlines() if line.startswith("+") and not line.startswith("+++"))
            deletions = sum(1 for line in diff_text.splitlines() if line.startswith("-") and not line.startswith("---"))

            views.append(DiffView(
                file_path=change.file_path,
                format="unified",
                content=diff_text,
                additions=additions,
                deletions=deletions,
            ))

        return views

    def summary(self, changeset: ChangeSet) -> str:
        """Generate a summary of all changes."""
        lines = [
            f"# {changeset.description}",
            f"Files affected: {len(changeset.files_affected)}",
            f"Total changes: {len(changeset.changes)}",
            "",
        ]

        for i, change in enumerate(changeset.changes, 1):
            lines.append(f"{i}. [{change.kind}] {change.file_path}")
            if change.description:
                lines.append(f"   {change.description}")

        return "\n".join(lines)

    def diff_strings(
        self,
        old: str,
        new: str,
        filename: str = "file.py",
        context_lines: int = 3,
    ) -> DiffView:
        """Diff two strings directly."""
        old_lines = old.splitlines(keepends=True)
        new_lines = new.splitlines(keepends=True)

        diff = difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile=f"a/{filename}",
            tofile=f"b/{filename}",
            n=context_lines,
        )
        diff_text = "".join(diff)

        additions = sum(1 for line in diff_text.splitlines() if line.startswith("+") and not line.startswith("+++"))
        deletions = sum(1 for line in diff_text.splitlines() if line.startswith("-") and not line.startswith("---"))

        return DiffView(
            file_path=filename,
            format="unified",
            content=diff_text,
            additions=additions,
            deletions=deletions,
        )

    def _simulate_change(self, change: Any, path: Path) -> str:
        """Simulate a change without writing to disk."""
        if change.kind == "append" and not path.is_file():
            return change.new_text + "\n"

        content = path.read_text(encoding="utf-8", errors="replace")

        if change.kind == "replace":
            return content.replace(change.old_text, change.new_text, 1)
        elif change.kind == "insert":
            idx = content.index(change.after_text) + len(change.after_text)
            return content[:idx] + "\n" + change.new_text + content[idx:]
        elif change.kind == "append":
            return content.rstrip("\n") + "\n" + change.new_text + "\n"
        elif change.kind == "delete":
            return content.replace(change.old_text, "", 1)
        return content
