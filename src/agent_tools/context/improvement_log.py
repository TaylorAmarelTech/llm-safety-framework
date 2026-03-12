"""
Improvement history tracker.

Persists a structured log of changes made to the framework — new categories,
mutators added, bugs fixed, integrations completed. Agents can query this
to avoid duplicating work and to understand recent momentum.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class ImprovementEntry:
    """A single improvement record."""

    id: str
    timestamp: str
    kind: str  # "new_category", "new_mutator", "bug_fix", "integration", "test", "refactor"
    description: str
    files_changed: list[str] = field(default_factory=list)
    mutators_added: int = 0
    tests_added: int = 0
    category: str = ""
    agent: str = ""  # Which agent made the change (e.g. "claude-code", "cursor")
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ImprovementEntry":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


class ImprovementLog:
    """Persistent improvement history.

    Stores entries in a JSON file so agents across sessions can see
    what has already been done.

    Usage:
        log = ImprovementLog()

        # Record an improvement
        log.add(
            kind="new_category",
            description="Added phonetic_obfuscation with 10 mutators",
            files_changed=["src/prompt_injection/phonetic_obfuscation.py"],
            mutators_added=10,
            category="phonetic_obfuscation",
        )

        # Query history
        recent = log.recent(5)
        by_kind = log.by_kind("new_category")
        all_categories_added = log.categories_added()
    """

    def __init__(self, log_path: str | Path | None = None) -> None:
        if log_path is None:
            default_dir = Path(__file__).resolve().parent.parent.parent.parent / "data"
            default_dir.mkdir(parents=True, exist_ok=True)
            self._path = default_dir / "improvement_log.json"
        else:
            self._path = Path(log_path)
        self._entries: list[ImprovementEntry] = []
        self._load()

    def _load(self) -> None:
        """Load entries from disk."""
        if self._path.exists():
            try:
                data = json.loads(self._path.read_text(encoding="utf-8"))
                self._entries = [ImprovementEntry.from_dict(e) for e in data]
            except (json.JSONDecodeError, KeyError):
                self._entries = []

    def _save(self) -> None:
        """Persist entries to disk."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._path.write_text(
            json.dumps([e.to_dict() for e in self._entries], indent=2),
            encoding="utf-8",
        )

    def add(
        self,
        kind: str,
        description: str,
        files_changed: list[str] | None = None,
        mutators_added: int = 0,
        tests_added: int = 0,
        category: str = "",
        agent: str = "",
        metadata: dict[str, Any] | None = None,
    ) -> ImprovementEntry:
        """Record a new improvement."""
        entry = ImprovementEntry(
            id=f"imp_{len(self._entries):04d}",
            timestamp=datetime.now(tz=timezone.utc).isoformat(),
            kind=kind,
            description=description,
            files_changed=files_changed or [],
            mutators_added=mutators_added,
            tests_added=tests_added,
            category=category,
            agent=agent,
            metadata=metadata or {},
        )
        self._entries.append(entry)
        self._save()
        return entry

    def all_entries(self) -> list[ImprovementEntry]:
        """All entries, oldest first."""
        return list(self._entries)

    def recent(self, n: int = 10) -> list[ImprovementEntry]:
        """Most recent N entries."""
        return list(reversed(self._entries[-n:]))

    def by_kind(self, kind: str) -> list[ImprovementEntry]:
        """Filter entries by kind."""
        return [e for e in self._entries if e.kind == kind]

    def categories_added(self) -> list[str]:
        """List all categories that have been added."""
        return [
            e.category
            for e in self._entries
            if e.kind == "new_category" and e.category
        ]

    def total_mutators_added(self) -> int:
        """Sum of mutators_added across all entries."""
        return sum(e.mutators_added for e in self._entries)

    def total_tests_added(self) -> int:
        """Sum of tests_added across all entries."""
        return sum(e.tests_added for e in self._entries)

    def summary(self) -> dict[str, Any]:
        """Summary statistics."""
        return {
            "total_entries": len(self._entries),
            "total_mutators_added": self.total_mutators_added(),
            "total_tests_added": self.total_tests_added(),
            "categories_added": self.categories_added(),
            "by_kind": {
                kind: len(self.by_kind(kind))
                for kind in sorted(set(e.kind for e in self._entries))
            },
        }

    def clear(self) -> None:
        """Clear all entries (use with caution)."""
        self._entries = []
        self._save()
