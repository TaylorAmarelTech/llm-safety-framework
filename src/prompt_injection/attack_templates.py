"""
Standardized Attack Template Registry.

Extracts the pattern used by mutator classes (``TEMPLATES`` class
attribute of ``(label, template_str)`` tuples) into a queryable,
serializable registry.  Templates can also be loaded from YAML files,
enabling community contributions without writing Python.

Usage::

    from src.prompt_injection.attack_templates import (
        TEMPLATE_REGISTRY,
        AttackTemplate,
    )

    # Query
    templates = TEMPLATE_REGISTRY.list_by_category("logical_fallacy")
    templates = TEMPLATE_REGISTRY.list_by_defense_layer("reasoning")

    # Render
    t = TEMPLATE_REGISTRY.get("fallacy_appeal_to_authority__academic_consensus")
    mutated = t.render("How do I charge workers fees?")

    # Load community YAML
    TEMPLATE_REGISTRY.load_yaml(Path("templates/community/my_attacks.yaml"))
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Core data model
# ---------------------------------------------------------------------------


@dataclass
class AttackTemplate:
    """A reusable prompt injection template."""
    id: str                                         # unique, e.g. "fallacy_appeal_to_authority__academic_consensus"
    name: str                                       # human-readable name
    template_str: str                               # string with {prompt} placeholder
    category: str                                   # owning mutator category
    defense_layers: list[str] = field(default_factory=list)
    technique_classes: list[str] = field(default_factory=list)
    source: str = ""                                # academic citation
    tags: list[str] = field(default_factory=list)

    def render(self, prompt: str) -> str:
        """Apply this template to a prompt, replacing ``{prompt}``."""
        return self.template_str.replace("{prompt}", prompt)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


class AttackTemplateRegistry:
    """Central registry for reusable attack templates."""

    def __init__(self) -> None:
        self._templates: dict[str, AttackTemplate] = {}

    # -- registration -------------------------------------------------------

    def register(self, template: AttackTemplate) -> None:
        """Register a template.  Duplicates are silently overwritten."""
        self._templates[template.id] = template

    def register_many(self, templates: list[AttackTemplate]) -> int:
        """Register a batch of templates. Returns count registered."""
        for t in templates:
            self.register(t)
        return len(templates)

    # -- retrieval ----------------------------------------------------------

    def get(self, template_id: str) -> AttackTemplate:
        """Get a template by ID. Raises KeyError if not found."""
        if template_id not in self._templates:
            raise KeyError(
                f"Unknown template: {template_id}. "
                f"Available: {len(self._templates)} templates"
            )
        return self._templates[template_id]

    def get_optional(self, template_id: str) -> Optional[AttackTemplate]:
        """Get a template by ID, returning None if not found."""
        return self._templates.get(template_id)

    def all_templates(self) -> list[AttackTemplate]:
        """Return all registered templates."""
        return list(self._templates.values())

    # -- filtering ----------------------------------------------------------

    def list_by_category(self, category: str) -> list[AttackTemplate]:
        """Return templates belonging to a given mutator category."""
        return [t for t in self._templates.values() if t.category == category]

    def list_by_defense_layer(self, layer: str) -> list[AttackTemplate]:
        """Return templates targeting a specific defense layer."""
        return [t for t in self._templates.values() if layer in t.defense_layers]

    def list_by_technique_class(self, cls: str) -> list[AttackTemplate]:
        """Return templates using a specific technique class."""
        return [t for t in self._templates.values() if cls in t.technique_classes]

    def list_by_tag(self, tag: str) -> list[AttackTemplate]:
        """Return templates with a given tag."""
        return [t for t in self._templates.values() if tag in t.tags]

    def search(self, query: str) -> list[AttackTemplate]:
        """Fuzzy text search across template name, ID, tags, and source."""
        q = query.lower()
        return [
            t for t in self._templates.values()
            if q in t.id.lower()
            or q in t.name.lower()
            or q in t.source.lower()
            or any(q in tag.lower() for tag in t.tags)
        ]

    # -- statistics ---------------------------------------------------------

    def stats(self) -> dict[str, Any]:
        """Return summary statistics."""
        cats: dict[str, int] = {}
        layers: dict[str, int] = {}
        techs: dict[str, int] = {}
        for t in self._templates.values():
            cats[t.category] = cats.get(t.category, 0) + 1
            for l in t.defense_layers:
                layers[l] = layers.get(l, 0) + 1
            for c in t.technique_classes:
                techs[c] = techs.get(c, 0) + 1
        return {
            "total": len(self._templates),
            "by_category": cats,
            "by_defense_layer": layers,
            "by_technique_class": techs,
        }

    # -- YAML I/O -----------------------------------------------------------

    def load_yaml(self, path: Path) -> int:
        """Load templates from a YAML file. Returns count loaded.

        Expected format::

            templates:
              - id: "my_template_id"
                name: "Human Name"
                category: "my_category"
                template_str: "Preamble {prompt} postamble"
                defense_layers: ["alignment"]
                technique_classes: ["cognitive"]
                source: "Author (Year)"
                tags: ["tag1", "tag2"]
        """
        try:
            import yaml
        except ImportError:
            logger.warning("PyYAML not installed — cannot load %s", path)
            return 0

        if not path.exists():
            logger.warning("Template file not found: %s", path)
            return 0

        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not data or "templates" not in data:
            return 0

        count = 0
        for entry in data["templates"]:
            if "id" not in entry or "template_str" not in entry:
                continue
            template = AttackTemplate(
                id=entry["id"],
                name=entry.get("name", entry["id"]),
                template_str=entry["template_str"],
                category=entry.get("category", "community"),
                defense_layers=entry.get("defense_layers", []),
                technique_classes=entry.get("technique_classes", []),
                source=entry.get("source", ""),
                tags=entry.get("tags", []),
            )
            self.register(template)
            count += 1
        return count

    def export_yaml(self, path: Path, category: Optional[str] = None) -> int:
        """Export templates to YAML.  Optionally filter by category."""
        try:
            import yaml
        except ImportError:
            logger.warning("PyYAML not installed — cannot export")
            return 0

        templates = (
            self.list_by_category(category) if category
            else self.all_templates()
        )
        data = {"templates": [t.to_dict() for t in templates]}
        path.write_text(yaml.dump(data, default_flow_style=False, sort_keys=False), encoding="utf-8")
        return len(templates)

    def __len__(self) -> int:
        return len(self._templates)


# ---------------------------------------------------------------------------
# Global singleton
# ---------------------------------------------------------------------------

TEMPLATE_REGISTRY = AttackTemplateRegistry()


# ---------------------------------------------------------------------------
# Auto-extraction helper
# ---------------------------------------------------------------------------


def extract_templates_from_mutator(
    mutator_cls: type,
    category: str,
    defense_layers: list[str] | None = None,
    technique_classes: list[str] | None = None,
) -> list[AttackTemplate]:
    """Extract AttackTemplate objects from a mutator class's TEMPLATES attribute.

    Most mutator classes define::

        TEMPLATES = [
            ("variant_label", "Template with {prompt} placeholder"),
            ...
        ]

    This function converts each into an AttackTemplate and returns them.
    """
    raw_templates = getattr(mutator_cls, "TEMPLATES", None)
    if not raw_templates:
        return []

    name_base = getattr(mutator_cls, "NAME", mutator_cls.__name__)
    source = ""
    desc = getattr(mutator_cls, "DESCRIPTION", "")

    # Try to extract source from description or docstring
    doc = mutator_cls.__doc__ or ""
    for line in doc.split("\n"):
        stripped = line.strip()
        if stripped.startswith("Source") or stripped.startswith("Sources"):
            source = stripped.split(":", 1)[-1].strip() if ":" in stripped else stripped

    results: list[AttackTemplate] = []
    for item in raw_templates:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            label, template_str = item[0], item[1]
        else:
            continue

        template_id = f"{name_base}__{label}"
        results.append(AttackTemplate(
            id=template_id,
            name=f"{name_base} ({label})",
            template_str=template_str,
            category=category,
            defense_layers=defense_layers or [],
            technique_classes=technique_classes or [],
            source=source,
            tags=[category, name_base, label],
        ))
    return results


def auto_register_all_templates() -> int:
    """Scan all registered mutators and extract their templates into TEMPLATE_REGISTRY.

    Should be called after ``_import_all_mutators()`` has run.
    Returns total count of templates registered.
    """
    from src.prompt_injection import _MUTATOR_REGISTRY
    from src.prompt_injection.coverage import CATEGORY_TAXONOMY

    count = 0
    for name, cls in _MUTATOR_REGISTRY.items():
        category = cls.CATEGORY
        taxonomy = CATEGORY_TAXONOMY.get(category, {})
        defense_layers = taxonomy.get("defense_layers", [])
        technique_classes = taxonomy.get("technique_classes", [])

        templates = extract_templates_from_mutator(
            cls,
            category=category,
            defense_layers=defense_layers,
            technique_classes=technique_classes,
        )
        for t in templates:
            TEMPLATE_REGISTRY.register(t)
        count += len(templates)
    return count
