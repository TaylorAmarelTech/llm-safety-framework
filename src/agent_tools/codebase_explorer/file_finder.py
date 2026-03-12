"""
File finder — locate files by pattern, content, or purpose.

Agents use this instead of shell ``find`` / ``grep`` to locate files
programmatically and get structured results they can act on.
"""

from __future__ import annotations

import fnmatch
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class FileMatch:
    """A single file search result."""

    path: str
    relative_path: str
    size_bytes: int = 0
    line_count: int = 0
    matching_lines: list[tuple[int, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "relative_path": self.relative_path,
            "size_bytes": self.size_bytes,
            "line_count": self.line_count,
            "matching_lines": [
                {"line": n, "text": t} for n, t in self.matching_lines
            ],
        }


class FileFinder:
    """Find files by glob pattern, content regex, or purpose.

    Usage:
        finder = FileFinder()

        # Find by glob
        mutator_files = finder.glob("src/prompt_injection/*.py")

        # Find by content
        matches = finder.grep("class.*Mutator.*BaseMutator")

        # Find mutator modules specifically
        modules = finder.mutator_modules()

        # Find test files for a category
        tests = finder.tests_for("encoding_advanced")
    """

    def __init__(self, root: str | Path | None = None) -> None:
        if root is None:
            self._root = Path(__file__).resolve().parent.parent.parent.parent
        else:
            self._root = Path(root)

    @property
    def root(self) -> Path:
        return self._root

    def glob(self, pattern: str) -> list[FileMatch]:
        """Find files matching a glob pattern relative to project root."""
        results = []
        for p in sorted(self._root.glob(pattern)):
            if p.is_file():
                results.append(self._make_match(p))
        return results

    def grep(
        self,
        pattern: str,
        file_glob: str = "**/*.py",
        max_results: int = 100,
        context_lines: int = 0,
    ) -> list[FileMatch]:
        """Search file contents for a regex pattern.

        Args:
            pattern: Regex pattern to search for.
            file_glob: Glob to filter which files to search.
            max_results: Maximum number of files to return.
            context_lines: Lines of context around each match.
        """
        regex = re.compile(pattern)
        results = []

        for p in sorted(self._root.glob(file_glob)):
            if not p.is_file():
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
                lines = text.splitlines()
                matching = []
                for i, line in enumerate(lines):
                    if regex.search(line):
                        matching.append((i + 1, line.strip()))
                if matching:
                    match = self._make_match(p)
                    match.matching_lines = matching[:20]  # Cap per file
                    results.append(match)
                    if len(results) >= max_results:
                        break
            except OSError:
                continue

        return results

    def mutator_modules(self) -> list[FileMatch]:
        """Find all mutator module files (src/prompt_injection/*.py)."""
        pi_dir = self._root / "src" / "prompt_injection"
        results = []
        if not pi_dir.is_dir():
            return results
        skip = {"__init__.py", "__pycache__", "fitness.py", "coverage.py",
                "output_decoders.py", "metadata_schema.py", "attack_templates.py"}
        for p in sorted(pi_dir.glob("*.py")):
            if p.name not in skip and not p.name.startswith("__"):
                results.append(self._make_match(p))
        return results

    def test_files(self) -> list[FileMatch]:
        """Find all test files."""
        tests_dir = self._root / "tests"
        if not tests_dir.is_dir():
            return []
        return [
            self._make_match(p) for p in sorted(tests_dir.glob("test_*.py"))
        ]

    def tests_for(self, category: str) -> list[FileMatch]:
        """Find test files likely related to a category."""
        return self.grep(
            pattern=f'"{category}"',
            file_glob="tests/test_*.py",
        )

    def plugin_dirs(self) -> list[str]:
        """List all web plugin directory names."""
        plugins_dir = self._root / "src" / "web" / "plugins"
        if not plugins_dir.is_dir():
            return []
        return sorted(
            d.name for d in plugins_dir.iterdir()
            if d.is_dir() and (d / "__init__.py").exists()
        )

    def files_modified_recently(self, days: int = 7) -> list[FileMatch]:
        """Find Python files modified within N days."""
        import time
        cutoff = time.time() - (days * 86400)
        results = []
        for p in self._root.rglob("*.py"):
            if p.is_file() and p.stat().st_mtime >= cutoff:
                if "__pycache__" not in str(p):
                    results.append(self._make_match(p))
        return sorted(results, key=lambda m: m.path)

    def _make_match(self, p: Path) -> FileMatch:
        """Build a FileMatch from a Path."""
        try:
            size = p.stat().st_size
            text = p.read_text(encoding="utf-8", errors="replace")
            line_count = text.count("\n") + 1
        except OSError:
            size = 0
            line_count = 0
        return FileMatch(
            path=str(p),
            relative_path=str(p.relative_to(self._root)),
            size_bytes=size,
            line_count=line_count,
        )
