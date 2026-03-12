"""
Analysis prompts — templates for code analysis and research tasks.

Provides structured prompts for agents performing gap analysis,
technique comparison, and codebase investigation.
"""

from __future__ import annotations

from typing import Any


class AnalysisPrompts:
    """Prompt templates for analysis tasks.

    Usage:
        prompts = AnalysisPrompts()

        # Get a gap analysis prompt
        prompt = prompts.coverage_gap_analysis(current_categories, target_layers)

        # Get a technique comparison prompt
        prompt = prompts.technique_comparison(technique_a, technique_b)

        # Get a paper analysis prompt
        prompt = prompts.paper_analysis(title, abstract)
    """

    @staticmethod
    def coverage_gap_analysis(
        current_categories: list[str],
        defense_layers: list[str] | None = None,
        technique_classes: list[str] | None = None,
    ) -> str:
        """Generate a prompt for coverage gap analysis."""
        layers = defense_layers or [
            "input_filter", "alignment", "output_filter", "reasoning"
        ]
        classes = technique_classes or [
            "encoding", "social_engineering", "authority",
            "obfuscation", "persona", "cognitive",
            "structural", "steganographic",
        ]

        return (
            "## Coverage Gap Analysis\n\n"
            f"### Current Categories ({len(current_categories)})\n"
            + "\n".join(f"- {c}" for c in sorted(current_categories)) +
            f"\n\n### Defense Layers\n"
            + "\n".join(f"- {l}" for l in layers) +
            f"\n\n### Technique Classes\n"
            + "\n".join(f"- {c}" for c in classes) +
            "\n\n### Task\n"
            "Identify which defense_layer × technique_class combinations "
            "are NOT covered by any existing category. For each gap, suggest:\n"
            "1. A new category name\n"
            "2. 3-5 specific mutator ideas\n"
            "3. Priority level (critical/high/medium/low)\n"
        )

    @staticmethod
    def technique_comparison(
        technique_a: str,
        technique_b: str,
        context: str = "",
    ) -> str:
        """Generate a prompt for comparing two techniques."""
        return (
            f"## Technique Comparison: {technique_a} vs {technique_b}\n\n"
            f"{'Context: ' + context + chr(10) + chr(10) if context else ''}"
            "Compare these techniques on:\n"
            "1. **Effectiveness**: Which bypasses more safety filters?\n"
            "2. **Detectability**: Which is harder to detect?\n"
            "3. **Generalizability**: Which works across more models?\n"
            "4. **Complexity**: Which is simpler to implement?\n"
            "5. **Composability**: Which combines better with other techniques?\n\n"
            "Provide concrete examples of each in action.\n"
        )

    @staticmethod
    def paper_analysis(title: str, abstract: str) -> str:
        """Generate a prompt for analyzing an academic paper."""
        return (
            f"## Paper Analysis: {title}\n\n"
            f"**Abstract:** {abstract[:500]}\n\n"
            "### Analysis Questions\n"
            "1. What new attack technique(s) does this paper introduce?\n"
            "2. Can we implement any of these as mutators? If so, how?\n"
            "3. What defense mechanisms does it describe or bypass?\n"
            "4. Which of our existing categories does this relate to?\n"
            "5. Is there a direct algorithm we can port?\n"
            "6. What are the key references we should also review?\n"
        )

    @staticmethod
    def repo_analysis(
        repo_name: str,
        description: str,
        techniques: list[str] | None = None,
    ) -> str:
        """Generate a prompt for analyzing a GitHub repository."""
        return (
            f"## Repository Analysis: {repo_name}\n\n"
            f"**Description:** {description}\n\n"
            f"**Known techniques:** {', '.join(techniques) if techniques else 'TBD'}\n\n"
            "### Analysis Tasks\n"
            "1. Identify all attack/mutation algorithms in the repo\n"
            "2. Map each algorithm to our defense_layer × technique_class matrix\n"
            "3. Check which algorithms are already in our framework\n"
            "4. Estimate integration difficulty (easy/medium/hard) for each\n"
            "5. Note license compatibility issues\n"
            "6. Identify any novel approaches we haven't seen\n"
        )

    @staticmethod
    def codebase_investigation(question: str) -> str:
        """Generate a prompt for investigating the codebase."""
        return (
            f"## Codebase Investigation\n\n"
            f"**Question:** {question}\n\n"
            "### Investigation Steps\n"
            "1. Use FileFinder.grep() to search for relevant code\n"
            "2. Use SymbolIndex to find relevant classes/functions\n"
            "3. Use ImportTracer to understand dependencies\n"
            "4. Summarize findings with file paths and line numbers\n"
            "5. Suggest next steps based on what you find\n"
        )

    @staticmethod
    def mutator_quality_review(category: str, mutator_names: list[str]) -> str:
        """Generate a prompt for reviewing mutator quality."""
        return (
            f"## Mutator Quality Review: {category}\n\n"
            f"**Mutators:** {', '.join(mutator_names)}\n\n"
            "### Review Criteria\n"
            "1. Does each mutator meaningfully transform the input?\n"
            "2. Are the transformations different enough from each other?\n"
            "3. Do metadata keys accurately describe the technique?\n"
            "4. Are there edge cases that could cause failures?\n"
            "5. Is the implementation efficient (no unnecessary loops)?\n"
            "6. Does the DESCRIPTION accurately explain the technique?\n"
            "7. Could any variants be merged or should more be added?\n"
        )
