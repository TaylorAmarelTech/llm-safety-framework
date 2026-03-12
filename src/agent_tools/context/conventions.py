"""
Coding conventions and patterns as structured data.

Agents can query these conventions to ensure generated code matches
the project's style, naming, and architectural patterns.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Convention:
    """A single coding convention."""

    id: str
    area: str  # naming, architecture, testing, imports, etc.
    rule: str
    example: str = ""
    anti_pattern: str = ""


# ---------------------------------------------------------------------------
# Master convention list
# ---------------------------------------------------------------------------

CONVENTIONS: list[Convention] = [
    # --- Naming ---
    Convention(
        id="naming_mutator_class",
        area="naming",
        rule="Mutator class names: PascalCase ending in 'Mutator'",
        example="class BrailleUnicodeMutator(BaseMutator):",
        anti_pattern="class braille_unicode(BaseMutator):",
    ),
    Convention(
        id="naming_mutator_name",
        area="naming",
        rule="Mutator NAME: snake_case, unique across all categories. Prefix with "
        "category hint if generic (e.g. 'pig_latin_phonetic' not 'pig_latin' "
        "if 'pig_latin' exists in another category).",
        example='NAME = "rail_fence_transposition"',
        anti_pattern='NAME = "rail_fence_cipher"  # collides with output_evasion',
    ),
    Convention(
        id="naming_category",
        area="naming",
        rule="Category names: snake_case, matching the module filename (without .py)",
        example='CATEGORY = "phonetic_obfuscation"  # file: phonetic_obfuscation.py',
    ),
    Convention(
        id="naming_constants",
        area="naming",
        rule="Module-level constants: UPPER_SNAKE_CASE",
        example="_MORSE_TABLE: dict[str, str] = {...}",
    ),
    Convention(
        id="naming_private",
        area="naming",
        rule="Private helpers: _leading_underscore",
        example="def _pig_latin_word(word: str) -> str:",
    ),

    # --- Architecture ---
    Convention(
        id="arch_one_category_per_file",
        area="architecture",
        rule="Each mutator category lives in its own .py file under src/prompt_injection/",
        example="src/prompt_injection/phonetic_obfuscation.py",
    ),
    Convention(
        id="arch_10_mutators_per_category",
        area="architecture",
        rule="Target 10 mutators per category. Each mutator produces 2 variants.",
        example="10 mutators × 2 variants = 20 test vectors per category",
    ),
    Convention(
        id="arch_register_decorator",
        area="architecture",
        rule="Every mutator class must be decorated with @register_mutator",
        example="@register_mutator\nclass MyMutator(BaseMutator): ...",
    ),
    Convention(
        id="arch_apply_return_type",
        area="architecture",
        rule="_apply() returns list[tuple[str, str, dict]] — "
        "(mutated_text, description, metadata)",
        example='return [("mutated", "description", {"technique": "x", "variant": "y"})]',
    ),
    Convention(
        id="arch_metadata_keys",
        area="architecture",
        rule="Metadata dict should include 'technique' and 'variant' keys at minimum",
        example='{"technique": "base32_encode", "variant": "standard"}',
    ),
    Convention(
        id="arch_no_llm_calls",
        area="architecture",
        rule="Mutators are pure string transforms — no LLM API calls. "
        "Set REQUIRES_LLM = True only if absolutely necessary.",
    ),
    Convention(
        id="arch_taxonomy_entry",
        area="architecture",
        rule="Every new category must have an entry in CATEGORY_TAXONOMY in coverage.py",
        example='"phonetic_obfuscation": {"defense_layers": ["input_filter"], '
        '"technique_classes": ["obfuscation", "encoding"]}',
    ),
    Convention(
        id="arch_import_registration",
        area="architecture",
        rule="New modules must be imported in _import_all_mutators() in __init__.py",
        example="from src.prompt_injection import phonetic_obfuscation",
    ),

    # --- Testing ---
    Convention(
        id="test_file_per_group",
        area="testing",
        rule="Group related tests. Use parametrize over mutator names.",
        example='@pytest.mark.parametrize("name", MUTATOR_NAMES)\n'
        "def test_standard_prompt(self, name): ...",
    ),
    Convention(
        id="test_standard_checks",
        area="testing",
        rule="Every mutator must be tested for: registration, standard prompt, "
        "output differs, metadata keys, empty string, short string",
    ),
    Convention(
        id="test_prompt",
        area="testing",
        rule="Use a realistic trafficking-related prompt for testing",
        example='TEST_PROMPT = "How can I confiscate a worker\'s passport..."',
    ),

    # --- Imports ---
    Convention(
        id="import_from_init",
        area="imports",
        rule="Import BaseMutator and register_mutator from src.prompt_injection",
        example="from src.prompt_injection import BaseMutator, register_mutator",
    ),
    Convention(
        id="import_future_annotations",
        area="imports",
        rule="Always include 'from __future__ import annotations' at the top",
    ),
    Convention(
        id="import_stdlib_only",
        area="imports",
        rule="Prefer stdlib-only dependencies. If external libs are needed, "
        "wrap in try/except and provide a graceful fallback.",
        example="try:\n    import jieba\nexcept ImportError:\n    jieba = None",
    ),

    # --- Docstrings ---
    Convention(
        id="doc_module",
        area="documentation",
        rule="Module docstring: purpose, list of techniques, academic sources",
    ),
    Convention(
        id="doc_class",
        area="documentation",
        rule="Class docstring: what the mutator does and why it evades filters",
    ),
    Convention(
        id="doc_sources",
        area="documentation",
        rule="Cite sources: RFCs, papers, standards (e.g. 'RFC 4648 — Base32')",
    ),
]


class ConventionGuide:
    """Query and filter coding conventions.

    Usage:
        guide = ConventionGuide()
        guide.for_area("naming")        # All naming conventions
        guide.for_area("architecture")  # All architecture conventions
        guide.as_prompt_context()       # Format as context for an agent prompt
    """

    def __init__(self, conventions: list[Convention] | None = None) -> None:
        self._conventions = conventions or CONVENTIONS

    def all(self) -> list[Convention]:
        return list(self._conventions)

    def for_area(self, area: str) -> list[Convention]:
        """Get conventions for a specific area."""
        return [c for c in self._conventions if c.area == area]

    def areas(self) -> list[str]:
        """List all convention areas."""
        return sorted(set(c.area for c in self._conventions))

    def get(self, convention_id: str) -> Convention | None:
        """Get a specific convention by ID."""
        for c in self._conventions:
            if c.id == convention_id:
                return c
        return None

    def as_prompt_context(self, areas: list[str] | None = None) -> str:
        """Format conventions as context to include in an agent prompt.

        Args:
            areas: Filter to specific areas. None = all areas.

        Returns:
            Formatted string suitable for inclusion in an LLM prompt.
        """
        if areas:
            items = [c for c in self._conventions if c.area in areas]
        else:
            items = list(self._conventions)

        lines = ["# Coding Conventions", ""]
        current_area = ""
        for c in sorted(items, key=lambda x: (x.area, x.id)):
            if c.area != current_area:
                current_area = c.area
                lines.append(f"## {current_area.title()}")
                lines.append("")
            lines.append(f"- **{c.id}**: {c.rule}")
            if c.example:
                lines.append(f"  ```python\n  {c.example}\n  ```")
            if c.anti_pattern:
                lines.append(f"  Anti-pattern: `{c.anti_pattern}`")
            lines.append("")

        return "\n".join(lines)

    def checklist(self, areas: list[str] | None = None) -> list[dict[str, str]]:
        """Return conventions as a checklist for validation.

        Returns:
            List of {id, area, rule} dicts.
        """
        items = self._conventions
        if areas:
            items = [c for c in items if c.area in areas]
        return [{"id": c.id, "area": c.area, "rule": c.rule} for c in items]
