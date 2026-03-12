"""
Standardized metadata schema for prompt injection mutators.

Defines canonical enums (DefenseLayer, TechniqueClass) and a Pydantic
validation model (MutatorMetadata) that every mutator's metadata dict
should conform to.  The ``build_metadata`` helper ensures core fields
are always present, while ``validate_metadata`` can be used in tests to
verify conformance across the full mutator registry.

The ``technique`` field is the only truly required key — it identifies
which technique the mutator applied.  Category-specific extras (e.g.
``fallacy_type``, ``encoding``, ``density``) are allowed via
``extra="allow"``.

Integration points:
    - ``coverage.py`` imports ALL_DEFENSE_LAYERS / ALL_TECHNIQUE_CLASSES
      from here (single source of truth).
    - ``attack_templates.py`` references DefenseLayer / TechniqueClass
      enums for template metadata.
    - Tests parametrise over all mutators and validate metadata against
      MutatorMetadata.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict


# ---------------------------------------------------------------------------
# Controlled vocabularies
# ---------------------------------------------------------------------------


class DefenseLayer(str, Enum):
    """Which layer of the LLM defense stack a technique targets."""
    INPUT_FILTER = "input_filter"
    ALIGNMENT = "alignment"
    OUTPUT_FILTER = "output_filter"
    REASONING = "reasoning"


class TechniqueClass(str, Enum):
    """High-level class of attack technique used."""
    ENCODING = "encoding"
    SOCIAL_ENGINEERING = "social_engineering"
    AUTHORITY = "authority"
    OBFUSCATION = "obfuscation"
    PERSONA = "persona"
    COGNITIVE = "cognitive"
    STRUCTURAL = "structural"
    STEGANOGRAPHIC = "steganographic"
    MULTI_TURN = "multi_turn"


# Convenience lists (kept in sync with enums above)
ALL_DEFENSE_LAYERS: list[str] = [e.value for e in DefenseLayer]
ALL_TECHNIQUE_CLASSES: list[str] = [e.value for e in TechniqueClass]


# ---------------------------------------------------------------------------
# Pydantic validation model
# ---------------------------------------------------------------------------


class MutatorMetadata(BaseModel):
    """Standard metadata fields every mutator should emit.

    The ``technique`` field is required.  All other core fields have
    defaults and are optional.  Category-specific extras (e.g.
    ``fallacy_type``, ``encoding``, ``density``) are accepted via
    ``extra="allow"``.
    """
    model_config = ConfigDict(extra="allow")

    technique: str
    variant: str = ""
    source: str = ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def build_metadata(
    technique: str,
    variant: str = "",
    source: str = "",
    **extra: Any,
) -> dict[str, Any]:
    """Build a metadata dict that conforms to MutatorMetadata.

    Convenience function for mutator ``_apply()`` methods.  Guarantees
    ``technique`` is always present.

    >>> m = build_metadata("rot13", variant="full", encoding="rot13")
    >>> m["technique"]
    'rot13'
    >>> m["encoding"]
    'rot13'
    """
    meta: dict[str, Any] = {"technique": technique}
    if variant:
        meta["variant"] = variant
    if source:
        meta["source"] = source
    meta.update(extra)
    return meta


def validate_metadata(meta: dict[str, Any]) -> tuple[bool, list[str]]:
    """Validate a metadata dict against MutatorMetadata.

    Returns ``(is_valid, list_of_error_strings)``.

    >>> validate_metadata({"technique": "rot13"})
    (True, [])
    >>> validate_metadata({})
    (False, [..."technique"...])
    """
    errors: list[str] = []
    if "technique" not in meta:
        errors.append("Missing required field: technique")
    if meta.get("technique") is not None and not isinstance(meta["technique"], str):
        errors.append(f"'technique' must be str, got {type(meta['technique']).__name__}")

    if errors:
        return False, errors

    # Full Pydantic validation for structural correctness
    try:
        MutatorMetadata.model_validate(meta)
    except Exception as exc:
        errors.append(str(exc))
        return False, errors

    return True, []
