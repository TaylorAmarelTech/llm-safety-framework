"""
Category planner — plan new mutator categories with taxonomy integration.

Given a high-level idea (e.g. "tap code encoding"), produces a complete
CategorySpec with mutator names, class names, taxonomy mapping, and
integration checklist.
"""

from __future__ import annotations

import re
from typing import Any

from src.agent_tools.scaffolding.mutator_generator import CategorySpec, MutatorSpec


def _to_snake(name: str) -> str:
    """Convert a name to snake_case."""
    s = re.sub(r"[^a-zA-Z0-9]", "_", name)
    s = re.sub(r"_+", "_", s).strip("_").lower()
    return s


def _to_pascal(name: str) -> str:
    """Convert a name to PascalCase."""
    parts = re.split(r"[^a-zA-Z0-9]", name)
    return "".join(p.capitalize() for p in parts if p)


class CategoryPlanner:
    """Plan a new mutator category from a high-level description.

    Usage:
        planner = CategoryPlanner()

        # Plan from a description
        spec = planner.plan(
            name="Tap Code Cipher",
            description="Polybius-grid based tap/knock code encoding",
            techniques=["basic_tap", "extended_tap", "paired_knock"],
            defense_layers=["input_filter"],
            technique_classes=["encoding"],
            sources=["Vietnam War POW communication"],
        )

        # Check for name collisions
        collisions = planner.check_collisions(spec)

        # Get full integration checklist
        steps = planner.integration_steps(spec)
    """

    def plan(
        self,
        name: str,
        description: str,
        techniques: list[str] | None = None,
        technique_count: int = 10,
        defense_layers: list[str] | None = None,
        technique_classes: list[str] | None = None,
        sources: list[str] | None = None,
        imports: list[str] | None = None,
    ) -> CategorySpec:
        """Create a CategorySpec from a high-level description.

        Args:
            name: Human-readable category name (e.g. "Tap Code Cipher")
            description: What this category does
            techniques: Specific technique names (auto-generated if None)
            technique_count: Number of mutators to plan (default 10)
            defense_layers: Which defense layers this targets
            technique_classes: Which technique classes this uses
            sources: Academic/technical sources
            imports: Additional Python imports needed
        """
        category_name = _to_snake(name)
        module_name = category_name

        # Auto-generate technique names if not provided
        if techniques is None:
            techniques = [f"{category_name}_v{i}" for i in range(1, technique_count + 1)]

        # Build mutator specs
        mutators = []
        for tech in techniques[:technique_count]:
            tech_snake = _to_snake(tech)
            mutator_name = f"{tech_snake}" if category_name in tech_snake else f"{category_name}_{tech_snake}"
            class_name = _to_pascal(tech) + "Mutator"

            mutators.append(
                MutatorSpec(
                    name=mutator_name,
                    class_name=class_name,
                    description=f"{_to_pascal(tech).replace('_', ' ')} technique",
                    technique=tech_snake,
                    variants=["standard", "compact"],
                )
            )

        return CategorySpec(
            category_name=category_name,
            module_name=module_name,
            description=description,
            defense_layers=defense_layers or ["input_filter"],
            technique_classes=technique_classes or ["encoding"],
            mutators=mutators,
            sources=sources or [],
            imports=imports or [],
        )

    def check_collisions(self, spec: CategorySpec) -> list[str]:
        """Check for name collisions with existing mutators.

        Returns a list of collision descriptions (empty = no collisions).
        """
        collisions = []
        try:
            from src.prompt_injection import list_mutators

            existing = list_mutators()
            for m in spec.mutators:
                if m.name in existing:
                    collisions.append(
                        f"Mutator name '{m.name}' already exists in "
                        f"category '{existing[m.name]['category']}'"
                    )
        except ImportError:
            collisions.append("Warning: Could not import list_mutators to check collisions")

        return collisions

    def integration_steps(self, spec: CategorySpec) -> list[str]:
        """Generate ordered integration steps."""
        from src.agent_tools.scaffolding.mutator_generator import MutatorGenerator

        gen = MutatorGenerator()
        return gen.checklist(spec)

    def preview(self, spec: CategorySpec) -> dict[str, Any]:
        """Preview what will be generated (without writing files)."""
        from src.agent_tools.scaffolding.mutator_generator import MutatorGenerator
        from src.agent_tools.scaffolding.test_generator import TestGenerator

        mgen = MutatorGenerator()
        tgen = TestGenerator()

        return {
            "category_name": spec.category_name,
            "module_name": spec.module_name,
            "mutator_count": len(spec.mutators),
            "mutator_names": [m.name for m in spec.mutators],
            "class_names": [m.class_name for m in spec.mutators],
            "defense_layers": spec.defense_layers,
            "technique_classes": spec.technique_classes,
            "taxonomy_entry": mgen.generate_taxonomy_entry(spec),
            "init_import": mgen.generate_init_import(spec),
            "module_code_preview": mgen.generate_module(spec)[:500] + "...",
            "test_code_preview": tgen.generate(spec)[:500] + "...",
            "collisions": self.check_collisions(spec),
            "steps": self.integration_steps(spec),
        }
