"""
Change builder — construct structured code changes.

Agents use this to build up a set of changes (insertions, replacements,
deletions) for a file before applying them all at once.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Change:
    """A single code change operation."""

    kind: str  # "insert", "replace", "delete", "append"
    file_path: str
    old_text: str = ""
    new_text: str = ""
    after_text: str = ""  # For insert: insert new_text after this
    line_number: int = 0  # For line-based operations
    description: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "file_path": self.file_path,
            "old_text": self.old_text[:100],
            "new_text": self.new_text[:100],
            "description": self.description,
        }


@dataclass
class ChangeSet:
    """A collection of changes to apply atomically."""

    description: str
    changes: list[Change] = field(default_factory=list)
    files_affected: set[str] = field(default_factory=set)

    def add(self, change: Change) -> None:
        """Add a change to the set."""
        self.changes.append(change)
        self.files_affected.add(change.file_path)

    def to_dict(self) -> dict[str, Any]:
        return {
            "description": self.description,
            "change_count": len(self.changes),
            "files_affected": sorted(self.files_affected),
            "changes": [c.to_dict() for c in self.changes],
        }


class ChangeBuilder:
    """Build structured code changes for a file or set of files.

    Usage:
        builder = ChangeBuilder("Add new mutator category")

        # Replace text
        builder.replace(
            "src/prompt_injection/__init__.py",
            old="# END IMPORTS",
            new="from . import my_module\\n# END IMPORTS",
        )

        # Append to file
        builder.append(
            "src/prompt_injection/coverage.py",
            text='"my_category": {"defense_layers": ["input_filter"], ...}',
        )

        # Insert after a marker
        builder.insert_after(
            "src/prompt_injection/__init__.py",
            after="import encoding_format",
            text="import my_module",
        )

        # Get the changeset
        changeset = builder.build()
    """

    def __init__(self, description: str = "") -> None:
        self._changeset = ChangeSet(description=description)

    def replace(
        self,
        file_path: str,
        old: str,
        new: str,
        description: str = "",
    ) -> "ChangeBuilder":
        """Add a text replacement change."""
        self._changeset.add(Change(
            kind="replace",
            file_path=file_path,
            old_text=old,
            new_text=new,
            description=description or f"Replace in {file_path}",
        ))
        return self

    def insert_after(
        self,
        file_path: str,
        after: str,
        text: str,
        description: str = "",
    ) -> "ChangeBuilder":
        """Add an insertion after a marker text."""
        self._changeset.add(Change(
            kind="insert",
            file_path=file_path,
            after_text=after,
            new_text=text,
            description=description or f"Insert after '{after[:30]}...' in {file_path}",
        ))
        return self

    def append(
        self,
        file_path: str,
        text: str,
        description: str = "",
    ) -> "ChangeBuilder":
        """Add text at the end of a file."""
        self._changeset.add(Change(
            kind="append",
            file_path=file_path,
            new_text=text,
            description=description or f"Append to {file_path}",
        ))
        return self

    def delete(
        self,
        file_path: str,
        text: str,
        description: str = "",
    ) -> "ChangeBuilder":
        """Delete text from a file."""
        self._changeset.add(Change(
            kind="delete",
            file_path=file_path,
            old_text=text,
            description=description or f"Delete from {file_path}",
        ))
        return self

    def build(self) -> ChangeSet:
        """Return the constructed changeset."""
        return self._changeset

    def preview(self) -> str:
        """Get a human-readable preview of all changes."""
        lines = [f"# {self._changeset.description}", ""]
        for i, change in enumerate(self._changeset.changes, 1):
            lines.append(f"## Change {i}: {change.description}")
            lines.append(f"File: {change.file_path}")
            lines.append(f"Kind: {change.kind}")
            if change.old_text:
                lines.append(f"Old: {change.old_text[:80]}")
            if change.new_text:
                lines.append(f"New: {change.new_text[:80]}")
            lines.append("")
        return "\n".join(lines)

    @staticmethod
    def for_new_category(
        category_name: str,
        module_file: str,
        mutator_count: int = 10,
    ) -> "ChangeBuilder":
        """Create a pre-built changeset for adding a new mutator category.

        Returns a ChangeBuilder with the standard changes needed:
        - Import in __init__.py
        - Taxonomy entry in coverage.py
        """
        builder = ChangeBuilder(f"Add new category: {category_name}")

        # Import in __init__.py
        builder.insert_after(
            "src/prompt_injection/__init__.py",
            after="# Category imports are handled by _import_all_mutators",
            text=f"    from src.prompt_injection import {category_name}",
            description=f"Import {category_name} module",
        )

        # Taxonomy in coverage.py
        builder.insert_after(
            "src/prompt_injection/coverage.py",
            after="CATEGORY_TAXONOMY = {",
            text=(
                f'    "{category_name}": {{\n'
                f'        "defense_layers": ["input_filter"],\n'
                f'        "technique_classes": ["encoding"],\n'
                f"    }},"
            ),
            description=f"Add {category_name} to taxonomy",
        )

        return builder
