"""
Dependency manager — track optional and required dependencies.

Manages the relationship between external Python packages and the
mutator categories that use them, ensuring graceful fallback when
optional packages are not installed.
"""

from __future__ import annotations

import importlib
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Dependency:
    """An external package dependency."""

    package: str  # pip package name
    import_name: str  # Python import name (may differ from pip name)
    required: bool = False  # True = framework won't work without it
    used_by: list[str] = field(default_factory=list)  # Module names that use it
    purpose: str = ""
    install_cmd: str = ""
    min_version: str = ""
    alternatives: list[str] = field(default_factory=list)

    def is_installed(self) -> bool:
        """Check if the package is currently installed."""
        try:
            importlib.import_module(self.import_name)
            return True
        except ImportError:
            return False

    def to_dict(self) -> dict[str, Any]:
        return {
            "package": self.package,
            "import_name": self.import_name,
            "required": self.required,
            "installed": self.is_installed(),
            "used_by": self.used_by,
            "purpose": self.purpose,
        }


# ---------------------------------------------------------------------------
# Known dependency registry
# ---------------------------------------------------------------------------

_DEPENDENCIES: list[Dependency] = [
    # Core required
    Dependency(
        package="fastapi",
        import_name="fastapi",
        required=True,
        used_by=["src.web.app", "src.api"],
        purpose="Web dashboard and API server",
    ),
    Dependency(
        package="pydantic",
        import_name="pydantic",
        required=True,
        used_by=["src.core.api_specification"],
        purpose="Data validation and serialization",
    ),
    Dependency(
        package="uvicorn",
        import_name="uvicorn",
        required=True,
        used_by=["src.web.app"],
        purpose="ASGI server",
    ),

    # Optional — encoding/crypto
    Dependency(
        package="pycryptodome",
        import_name="Crypto",
        required=False,
        used_by=[],
        purpose="Advanced cryptographic operations for cipher mutators",
        alternatives=["cryptography"],
    ),

    # Optional — NLP
    Dependency(
        package="textattack",
        import_name="textattack",
        required=False,
        used_by=[],
        purpose="Adversarial NLP attack library (TextFooler, BERT-Attack, etc.)",
        install_cmd="pip install textattack",
    ),
    Dependency(
        package="jieba",
        import_name="jieba",
        required=False,
        used_by=["src.prompt_injection.multilingual_extended"],
        purpose="Chinese text segmentation for Pinyin conversion",
        install_cmd="pip install jieba",
    ),
    Dependency(
        package="pypinyin",
        import_name="pypinyin",
        required=False,
        used_by=["src.prompt_injection.multilingual_extended"],
        purpose="Chinese character to Pinyin conversion",
        install_cmd="pip install pypinyin",
    ),
    Dependency(
        package="romkan",
        import_name="romkan",
        required=False,
        used_by=["src.prompt_injection.multilingual_extended"],
        purpose="Japanese Kana to Romaji conversion",
        install_cmd="pip install romkan",
    ),

    # Optional — transliteration
    Dependency(
        package="transliterate",
        import_name="transliterate",
        required=False,
        used_by=[],
        purpose="Script transliteration (Cyrillic, Georgian, etc.)",
        install_cmd="pip install transliterate",
    ),
    Dependency(
        package="unidecode",
        import_name="unidecode",
        required=False,
        used_by=[],
        purpose="Unicode to ASCII transliteration",
        install_cmd="pip install Unidecode",
    ),

    # Optional — homoglyphs
    Dependency(
        package="confusable-homoglyphs",
        import_name="confusable_homoglyphs",
        required=False,
        used_by=["src.prompt_injection.obfuscation"],
        purpose="Unicode confusable character lookup (UTS #39)",
        install_cmd="pip install confusable-homoglyphs",
    ),

    # Optional — ML/embeddings
    Dependency(
        package="sentence-transformers",
        import_name="sentence_transformers",
        required=False,
        used_by=["src.intelligent_attack.embedder"],
        purpose="Text embedding for feature space analysis",
        install_cmd="pip install sentence-transformers",
    ),

    # Optional — integrations
    Dependency(
        package="garak",
        import_name="garak",
        required=False,
        used_by=["src.integrations.garak_adapter"],
        purpose="LLM vulnerability scanner integration",
    ),
    Dependency(
        package="pyrit",
        import_name="pyrit",
        required=False,
        used_by=["src.integrations.pyrit_adapter"],
        purpose="Microsoft PyRIT integration",
    ),
]


class DependencyManager:
    """Manage and query project dependencies.

    Usage:
        dm = DependencyManager()

        # Check what's installed
        status = dm.status()

        # Find what's missing for a module
        missing = dm.missing_for("src.prompt_injection.multilingual_extended")

        # Generate install command
        cmd = dm.install_command(optional=True)

        # Check if a new dependency is safe to add
        ok = dm.can_add("some-package", required=False)
    """

    def __init__(self, deps: list[Dependency] | None = None) -> None:
        self._deps = deps or list(_DEPENDENCIES)

    def all(self) -> list[Dependency]:
        return list(self._deps)

    def required(self) -> list[Dependency]:
        return [d for d in self._deps if d.required]

    def optional(self) -> list[Dependency]:
        return [d for d in self._deps if not d.required]

    def installed(self) -> list[Dependency]:
        return [d for d in self._deps if d.is_installed()]

    def missing(self) -> list[Dependency]:
        return [d for d in self._deps if not d.is_installed()]

    def missing_required(self) -> list[Dependency]:
        return [d for d in self._deps if d.required and not d.is_installed()]

    def for_module(self, module: str) -> list[Dependency]:
        """Get dependencies used by a specific module."""
        return [d for d in self._deps if module in d.used_by]

    def missing_for(self, module: str) -> list[Dependency]:
        """Get missing dependencies for a specific module."""
        return [d for d in self.for_module(module) if not d.is_installed()]

    def status(self) -> dict[str, Any]:
        """Get a full dependency status report."""
        return {
            "total": len(self._deps),
            "installed": len(self.installed()),
            "missing": len(self.missing()),
            "missing_required": len(self.missing_required()),
            "details": [d.to_dict() for d in self._deps],
        }

    def install_command(self, optional: bool = False) -> str:
        """Generate pip install command for missing dependencies."""
        deps = self.missing() if optional else self.missing_required()
        if not deps:
            return "# All dependencies satisfied"
        packages = [d.package for d in deps]
        return f"pip install {' '.join(packages)}"

    def add(self, dep: Dependency) -> None:
        """Register a new dependency."""
        self._deps.append(dep)

    def generate_try_import(self, package: str, import_name: str = "") -> str:
        """Generate a safe try/except import block.

        Returns a code snippet that can be pasted into a module.
        """
        imp = import_name or package
        return (
            f"try:\n"
            f"    import {imp}\n"
            f"except ImportError:\n"
            f"    {imp} = None  # Optional dependency: pip install {package}\n"
        )
