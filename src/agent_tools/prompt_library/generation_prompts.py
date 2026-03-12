"""
Generation prompts — templates for code generation tasks.

Provides structured prompts that agents can fill in to generate
new mutators, tests, adapters, and other code artifacts.
"""

from __future__ import annotations

from string import Template
from typing import Any


# Template for generating a new mutator category
MUTATOR_CATEGORY_PROMPT = Template("""\
Create a new prompt injection mutator category called "$category_name".

## Category Description
$description

## Defense Layers Targeted
$defense_layers

## Technique Classes
$technique_classes

## Requirements
- Create exactly $mutator_count mutators, each extending BaseMutator
- Each mutator NAME must be globally unique (check existing names first)
- Each mutator CATEGORY must be "$category_name"
- Each _apply() method must return list[tuple[str, str, dict]]
- Each tuple: (mutated_text, description_string, metadata_dict)
- metadata_dict must contain "technique" and "variant" keys
- Each mutator should produce exactly 2 variants
- Use @register_mutator decorator on each class

## File Structure
```python
from src.prompt_injection import BaseMutator, register_mutator

@register_mutator
class MyMutator(BaseMutator):
    NAME = "unique_name"
    CATEGORY = "$category_name"
    DESCRIPTION = "What this mutator does"

    def _apply(self, text: str) -> list[tuple[str, str, dict]]:
        variant1 = f"... {{text}} ..."
        variant2 = f"... {{text}} ..."
        return [
            (variant1, "Description of variant 1", {"technique": "...", "variant": "v1"}),
            (variant2, "Description of variant 2", {"technique": "...", "variant": "v2"}),
        ]
```

## Existing Names to Avoid
$existing_names
""")


# Template for generating tests
TEST_GENERATION_PROMPT = Template("""\
Write pytest tests for the "$category_name" mutator category.

## Test Structure
Create two test classes:
1. TestRegistration — verify mutators are registered correctly
2. TestFunctionality — verify mutators produce valid output

## Expected Mutator Names
$mutator_names

## Required Tests
- test_category_count: verify correct number of mutators
- test_mutator_names (parametrized): verify each name is registered
- test_standard_prompt (parametrized): verify each mutator transforms text
- test_metadata_keys (parametrized): verify metadata has technique/variant
- test_output_differs (parametrized): verify output != input
- test_empty_string (parametrized): verify handles empty string
- test_short_string (parametrized): verify handles short strings
- test_unicode (parametrized): verify handles unicode characters

## File Location
tests/test_$category_name.py

## Import Pattern
```python
from src.prompt_injection import get_mutators_by_category, list_mutators
```
""")


# Template for generating an adapter
ADAPTER_GENERATION_PROMPT = Template("""\
Create an adapter for the "$repo_name" repository ($repo_url).

## Techniques to Adapt
$techniques

## Requirements
- Use try/except imports for optional dependency
- Provide graceful fallback if dependency is not installed
- Match BaseMutator interface
- Register with @register_mutator
- Include clear attribution/license notice

## Integration Pattern
```python
try:
    from $import_path import $import_name
    _HAS_DEPENDENCY = True
except ImportError:
    _HAS_DEPENDENCY = False

@register_mutator
class AdaptedMutator(BaseMutator):
    NAME = "adapted_$technique_name"
    CATEGORY = "$category_name"
    DESCRIPTION = "Adapted from $repo_name: ..."

    def _apply(self, text: str) -> list[tuple[str, str, dict]]:
        if not _HAS_DEPENDENCY:
            return [(text, "Dependency not available", {"technique": "...", "variant": "fallback"})]
        # Use the library here
        ...
```
""")


class GenerationPrompts:
    """Prompt templates for code generation tasks.

    Usage:
        prompts = GenerationPrompts()

        # Get a mutator category generation prompt
        prompt = prompts.new_category(
            category_name="my_encoding",
            description="Encodes text using custom encoding",
            mutator_count=10,
        )

        # Get a test generation prompt
        prompt = prompts.new_tests(
            category_name="my_encoding",
            mutator_names=["enc1", "enc2"],
        )

        # Get an adapter generation prompt
        prompt = prompts.new_adapter(
            repo_name="TextAttack",
            techniques=["textfooler", "bert_attack"],
        )
    """

    def new_category(
        self,
        category_name: str,
        description: str,
        defense_layers: list[str] | None = None,
        technique_classes: list[str] | None = None,
        mutator_count: int = 10,
        existing_names: list[str] | None = None,
    ) -> str:
        """Generate a prompt for creating a new mutator category."""
        return MUTATOR_CATEGORY_PROMPT.substitute(
            category_name=category_name,
            description=description,
            defense_layers=", ".join(defense_layers or ["input_filter"]),
            technique_classes=", ".join(technique_classes or ["encoding"]),
            mutator_count=mutator_count,
            existing_names=", ".join(existing_names[:50]) if existing_names else "(check with list_mutators())",
        )

    def new_tests(
        self,
        category_name: str,
        mutator_names: list[str],
    ) -> str:
        """Generate a prompt for creating tests."""
        return TEST_GENERATION_PROMPT.substitute(
            category_name=category_name,
            mutator_names=", ".join(mutator_names),
        )

    def new_adapter(
        self,
        repo_name: str,
        repo_url: str = "",
        techniques: list[str] | None = None,
        import_path: str = "",
        import_name: str = "",
        category_name: str = "adapted",
    ) -> str:
        """Generate a prompt for creating a library adapter."""
        tech_list = techniques or []
        return ADAPTER_GENERATION_PROMPT.substitute(
            repo_name=repo_name,
            repo_url=repo_url or f"https://github.com/.../{repo_name}",
            techniques=", ".join(tech_list) if tech_list else "TBD",
            import_path=import_path or repo_name.lower(),
            import_name=import_name or repo_name,
            technique_name=tech_list[0] if tech_list else "unknown",
            category_name=category_name,
        )

    @staticmethod
    def integration_checklist() -> str:
        """Get the full integration checklist as a prompt."""
        return (
            "## Integration Checklist\n"
            "1. [ ] Create module file in src/prompt_injection/\n"
            "2. [ ] Each mutator has unique NAME (checked against all existing)\n"
            "3. [ ] Each mutator has CATEGORY, DESCRIPTION attributes\n"
            "4. [ ] Each mutator has @register_mutator decorator\n"
            "5. [ ] Each _apply() returns list[tuple[str, str, dict]]\n"
            "6. [ ] Metadata dicts have 'technique' and 'variant' keys\n"
            "7. [ ] Import added to src/prompt_injection/__init__.py\n"
            "8. [ ] Taxonomy entry added to src/prompt_injection/coverage.py\n"
            "9. [ ] Test file created in tests/\n"
            "10. [ ] All tests passing\n"
        )
