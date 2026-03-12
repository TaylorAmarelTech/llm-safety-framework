"""
Toolkit introspector — discover and document all available tools.

Scans agent_tools sub-packages at runtime to build a complete
inventory of classes, methods, and capabilities.
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ToolInfo:
    """Information about a single tool class."""

    name: str
    module: str
    package: str
    docstring: str = ""
    methods: list[str] = field(default_factory=list)
    public_methods: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "module": self.module,
            "package": self.package,
            "docstring": self.docstring[:200],
            "public_methods": self.public_methods,
        }


@dataclass
class PackageInfo:
    """Information about a sub-package."""

    name: str
    docstring: str = ""
    tools: list[ToolInfo] = field(default_factory=list)
    module_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "docstring": self.docstring[:200],
            "tools": [t.to_dict() for t in self.tools],
            "module_count": self.module_count,
        }


class ToolkitIntrospector:
    """Introspect all agent_tools sub-packages and their tools.

    Usage:
        intro = ToolkitIntrospector()

        # Get all packages and their tools
        packages = intro.packages()

        # Get all tool classes
        tools = intro.all_tools()

        # Search for a tool by name
        matches = intro.search("validator")

        # Generate a markdown summary
        md = intro.as_markdown()
    """

    def __init__(self) -> None:
        self._root = Path(__file__).resolve().parent.parent

    def packages(self) -> list[PackageInfo]:
        """List all agent_tools sub-packages with their tools."""
        result: list[PackageInfo] = []

        for item in sorted(self._root.iterdir()):
            if item.is_dir() and (item / "__init__.py").exists():
                if item.name.startswith("__"):
                    continue
                pkg_info = self._inspect_package(item)
                result.append(pkg_info)

        return result

    def all_tools(self) -> list[ToolInfo]:
        """Get all tool classes across all packages."""
        tools: list[ToolInfo] = []
        for pkg in self.packages():
            tools.extend(pkg.tools)
        return tools

    def search(self, keyword: str) -> list[ToolInfo]:
        """Search for tools by keyword in name or docstring."""
        kw = keyword.lower()
        return [
            t for t in self.all_tools()
            if kw in t.name.lower() or kw in t.docstring.lower()
        ]

    def tool_count(self) -> int:
        """Get total number of tool classes."""
        return len(self.all_tools())

    def package_count(self) -> int:
        """Get total number of sub-packages."""
        return len(self.packages())

    def as_markdown(self) -> str:
        """Generate a markdown summary of all tools."""
        lines = [
            "# Agent Tools Reference",
            "",
            f"**{self.package_count()} packages, {self.tool_count()} tools**",
            "",
        ]

        for pkg in self.packages():
            lines.append(f"## {pkg.name}")
            if pkg.docstring:
                lines.append(f"> {pkg.docstring.split(chr(10))[0]}")
            lines.append("")

            for tool in pkg.tools:
                methods = ", ".join(f"`{m}()`" for m in tool.public_methods[:5])
                lines.append(f"### {tool.name}")
                if tool.docstring:
                    first_line = tool.docstring.strip().split("\n")[0]
                    lines.append(f"{first_line}")
                if methods:
                    lines.append(f"Methods: {methods}")
                lines.append("")

        return "\n".join(lines)

    def as_agent_context(self) -> str:
        """Generate a compact context string for agent prompts."""
        lines = ["# Available Agent Tools\n"]
        for pkg in self.packages():
            tool_names = [t.name for t in pkg.tools]
            lines.append(f"- **{pkg.name}**: {', '.join(tool_names)}")
        return "\n".join(lines)

    def _inspect_package(self, pkg_path: Path) -> PackageInfo:
        """Introspect a single sub-package."""
        init_path = pkg_path / "__init__.py"
        docstring = ""
        if init_path.is_file():
            content = init_path.read_text(encoding="utf-8", errors="replace")
            # Extract module docstring
            if content.startswith('"""'):
                end = content.find('"""', 3)
                if end > 0:
                    docstring = content[3:end].strip()
            elif content.startswith("'"):
                end = content.find("'''", 3)
                if end > 0:
                    docstring = content[3:end].strip()

        # Count .py files
        module_count = sum(
            1 for p in pkg_path.glob("*.py")
            if not p.name.startswith("__")
        )

        # Find tool classes
        tools: list[ToolInfo] = []
        for py_file in sorted(pkg_path.glob("*.py")):
            if py_file.name.startswith("__"):
                continue
            tools.extend(self._inspect_module(py_file, pkg_path.name))

        return PackageInfo(
            name=pkg_path.name,
            docstring=docstring,
            tools=tools,
            module_count=module_count,
        )

    def _inspect_module(self, module_path: Path, package_name: str) -> list[ToolInfo]:
        """Introspect a single module file for tool classes."""
        import ast

        try:
            source = module_path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source)
        except (SyntaxError, OSError):
            return []

        tools: list[ToolInfo] = []
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                docstring = ast.get_docstring(node) or ""
                methods = []
                public_methods = []
                for child in ast.iter_child_nodes(node):
                    if isinstance(child, ast.FunctionDef):
                        methods.append(child.name)
                        if not child.name.startswith("_"):
                            public_methods.append(child.name)

                tools.append(ToolInfo(
                    name=node.name,
                    module=module_path.stem,
                    package=package_name,
                    docstring=docstring,
                    methods=methods,
                    public_methods=public_methods,
                ))

        return tools
