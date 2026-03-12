"""
Mutator module code generator.

Takes a structured specification and produces a complete, ready-to-use
mutator module with proper class definitions, registration decorators,
docstrings, and metadata.

Usage:
    gen = MutatorGenerator()

    spec = CategorySpec(
        category_name="tap_code_cipher",
        module_name="tap_code_cipher",
        description="Tap code / knock code encoding using Polybius grid",
        defense_layers=["input_filter"],
        technique_classes=["encoding"],
        mutators=[
            MutatorSpec(
                name="tap_code_basic",
                class_name="TapCodeBasicMutator",
                description="Basic 5x5 Polybius grid tap code",
                technique="tap_code",
                variants=["standard", "compact"],
            ),
            # ... more mutators
        ],
        sources=["Vietnam War POW communication", "Polybius (c. 150 BC)"],
    )

    code = gen.generate_module(spec)
    # Returns a complete Python module string
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from string import Template
import textwrap


@dataclass
class MutatorSpec:
    """Specification for a single mutator."""

    name: str  # e.g. "tap_code_basic"
    class_name: str  # e.g. "TapCodeBasicMutator"
    description: str  # Human-readable description
    technique: str  # Metadata technique key
    variants: list[str] = field(default_factory=lambda: ["standard", "compact"])
    requires_llm: bool = False
    extra_metadata: dict[str, str] = field(default_factory=dict)


@dataclass
class CategorySpec:
    """Specification for a full mutator category module."""

    category_name: str  # e.g. "tap_code_cipher"
    module_name: str  # e.g. "tap_code_cipher" (filename without .py)
    description: str  # Module-level description
    defense_layers: list[str] = field(default_factory=lambda: ["input_filter"])
    technique_classes: list[str] = field(default_factory=lambda: ["encoding"])
    mutators: list[MutatorSpec] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)  # Extra imports needed


_MODULE_HEADER = '''\
"""
${module_title}

${module_description}

Techniques:
${technique_list}

Sources:
${source_list}
"""

from __future__ import annotations

${extra_imports}
from src.prompt_injection import BaseMutator, register_mutator

'''

_MUTATOR_CLASS = '''\

# ---------------------------------------------------------------------------
# ${index}. ${class_name}
# ---------------------------------------------------------------------------


@register_mutator
class ${class_name}(BaseMutator):
    """${docstring}"""

    NAME = "${name}"
    CATEGORY = "${category}"
    DESCRIPTION = "${description}"
${requires_llm}
    def _apply(self, prompt: str, **kwargs) -> list[tuple[str, str, dict]]:
        # TODO: Implement the actual transformation logic
        encoded = prompt  # Replace with actual encoding/transformation
        return [
${variants}
        ]
'''

_VARIANT_TEMPLATE = '''\
            (
                f"${instruction_prefix}\\n\\n{{encoded}}",
                "${variant_description}",
                {${metadata}},
            ),'''


class MutatorGenerator:
    """Generate mutator module code from structured specs.

    Usage:
        gen = MutatorGenerator()
        code = gen.generate_module(category_spec)
        gen.write_module(category_spec, output_dir="src/prompt_injection/")
    """

    def generate_module(self, spec: CategorySpec) -> str:
        """Generate a complete Python module string from a CategorySpec."""
        # Build header
        technique_list = "\n".join(
            f"    - {m.class_name}: {m.description}" for m in spec.mutators
        )
        source_list = "\n".join(f"    - {s}" for s in spec.sources) if spec.sources else "    - (none cited)"
        extra_imports = "\n".join(spec.imports) + "\n" if spec.imports else ""

        header = Template(_MODULE_HEADER).safe_substitute(
            module_title=f"{spec.category_name.replace('_', ' ').title()} Mutators",
            module_description=spec.description,
            technique_list=technique_list,
            source_list=source_list,
            extra_imports=extra_imports,
        )

        # Build mutator classes
        classes = []
        for i, m in enumerate(spec.mutators, 1):
            variants_code = self._build_variants(m, spec.category_name)
            requires_llm = '    REQUIRES_LLM = True\n' if m.requires_llm else ""
            cls_code = Template(_MUTATOR_CLASS).safe_substitute(
                index=i,
                class_name=m.class_name,
                docstring=m.description,
                name=m.name,
                category=spec.category_name,
                description=m.description,
                requires_llm=requires_llm,
                variants=variants_code,
            )
            classes.append(cls_code)

        return header + "\n".join(classes)

    def _build_variants(self, m: MutatorSpec, category: str) -> str:
        """Build variant return statements."""
        variants = []
        for v in m.variants:
            meta_parts = [f'"technique": "{m.technique}"', f'"variant": "{v}"']
            for k, val in m.extra_metadata.items():
                meta_parts.append(f'"{k}": "{val}"')
            metadata = ", ".join(meta_parts)

            variant_code = Template(_VARIANT_TEMPLATE).safe_substitute(
                instruction_prefix=f"Decode the following {m.technique} ({v} variant) and respond:",
                variant_description=f"{m.technique} ({v})",
                metadata=metadata,
            )
            variants.append(variant_code)
        return "\n".join(variants)

    def generate_taxonomy_entry(self, spec: CategorySpec) -> str:
        """Generate the CATEGORY_TAXONOMY dict entry for coverage.py."""
        layers = ", ".join(f'"{l}"' for l in spec.defense_layers)
        classes = ", ".join(f'"{c}"' for c in spec.technique_classes)
        return (
            f'    "{spec.category_name}": {{\n'
            f'        "defense_layers": [{layers}],\n'
            f'        "technique_classes": [{classes}],\n'
            f"    }},"
        )

    def generate_init_import(self, spec: CategorySpec) -> str:
        """Generate the import line for __init__.py."""
        return f"        {spec.module_name},"

    def generate_docstring_entry(self, spec: CategorySpec) -> str:
        """Generate the docstring entry for __init__.py."""
        desc = spec.description[:80]
        return f"    {spec.category_name:25s} - {desc}"

    def write_module(
        self,
        spec: CategorySpec,
        output_dir: str = "src/prompt_injection",
    ) -> str:
        """Write the generated module to a file.

        Returns the output file path.
        """
        from pathlib import Path

        output = Path(output_dir) / f"{spec.module_name}.py"
        code = self.generate_module(spec)
        output.write_text(code, encoding="utf-8")
        return str(output)

    def checklist(self, spec: CategorySpec) -> list[str]:
        """Generate a checklist of steps for completing the integration.

        Returns a list of action items the agent should follow.
        """
        return [
            f"1. Write implementation logic in src/prompt_injection/{spec.module_name}.py",
            f"2. Add import to _import_all_mutators() in src/prompt_injection/__init__.py:",
            f"       {self.generate_init_import(spec)}",
            f"3. Add docstring entry to __init__.py module docstring:",
            f"       {self.generate_docstring_entry(spec)}",
            f"4. Add taxonomy entry to CATEGORY_TAXONOMY in coverage.py:",
            f"       {self.generate_taxonomy_entry(spec)}",
            f"5. Write tests in tests/test_{spec.module_name}.py",
            f"6. Run: py -3.13 -m pytest tests/test_{spec.module_name}.py -v",
            f"7. Run full suite: py -3.13 -m pytest tests/ --ignore=tests/e2e -v",
            f"8. Update mutator count in __init__.py docstring",
        ]
