"""
Coverage analysis for the prompt injection mutation system.

Measures what percentage of the theoretical attack surface is exercised
by existing mutators, identifies blind spots (uncovered category combinations),
and produces a coverage matrix.

Attack surface dimensions:
- Defense layer targeted: input_filter, alignment, output_filter, reasoning
- Technique class: encoding, social_engineering, authority, obfuscation,
                   persona, cognitive, structural, multi_turn, steganographic
- Complexity: single_technique, two_technique_combo, three_plus_combo
"""

from __future__ import annotations

from typing import Any
from dataclasses import dataclass, field


# Maps each category to which defense layers and technique classes it targets
CATEGORY_TAXONOMY: dict[str, dict[str, list[str]]] = {
    "instruction_override": {
        "defense_layers": ["alignment"],
        "technique_classes": ["structural"],
    },
    "encoding_format": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding"],
    },
    "obfuscation": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["obfuscation"],
    },
    "social_engineering": {
        "defense_layers": ["alignment"],
        "technique_classes": ["social_engineering"],
    },
    "context_manipulation": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["cognitive"],
    },
    "hybrid": {
        "defense_layers": ["input_filter", "alignment"],
        "technique_classes": ["encoding", "social_engineering"],
    },
    "output_evasion": {
        "defense_layers": ["output_filter"],
        "technique_classes": ["encoding", "obfuscation", "structural"],
    },
    "named_jailbreak": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["social_engineering", "cognitive"],
    },
    "structural_injection": {
        "defense_layers": ["input_filter", "alignment"],
        "technique_classes": ["structural"],
    },
    "advanced_obfuscation": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["obfuscation", "encoding"],
    },
    "application_injection": {
        "defense_layers": ["input_filter", "alignment"],
        "technique_classes": ["structural", "authority"],
    },
    "step_decomposition": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["cognitive", "structural"],
    },
    "puzzle_game": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["cognitive"],
    },
    "cognitive_exploit": {
        "defense_layers": ["reasoning"],
        "technique_classes": ["cognitive"],
    },
    "multilingual_attack": {
        "defense_layers": ["input_filter", "alignment"],
        "technique_classes": ["encoding"],
    },
    "steganographic_encode": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["steganographic"],
    },
    "named_jailbreak_v2": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["social_engineering", "cognitive"],
    },
    "logical_fallacy": {
        "defense_layers": ["reasoning"],
        "technique_classes": ["cognitive"],
    },
    "distraction": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["cognitive"],
    },
    "rhetorical": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["social_engineering", "cognitive"],
    },
    "legal_persona": {
        "defense_layers": ["alignment"],
        "technique_classes": ["persona", "authority"],
    },
    "professional_persona": {
        "defense_layers": ["alignment"],
        "technique_classes": ["persona", "authority"],
    },
    "analytical_framing": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["persona", "cognitive"],
    },
    "special_token": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["structural"],
    },
    "emoji_smuggling": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding", "steganographic"],
    },
    "entropy_noise": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["obfuscation"],
    },
    "control_char": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding", "structural"],
    },
    "encoding_exploit": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding"],
    },
    "adversarial_tokenization": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding", "obfuscation"],
    },
    "bijection_cipher": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding"],
    },
    "context_position": {
        "defense_layers": ["alignment"],
        "technique_classes": ["structural"],
    },
    "mathematical_encoding": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding"],
    },
    "evaluation_manipulation": {
        "defense_layers": ["alignment", "output_filter"],
        "technique_classes": ["cognitive", "structural"],
    },
    "payload_splitting": {
        "defense_layers": ["input_filter", "alignment"],
        "technique_classes": ["structural"],
    },
    "code_steganography": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["steganographic", "encoding"],
    },
    "combination": {
        "defense_layers": ["input_filter", "alignment", "output_filter", "reasoning"],
        "technique_classes": ["encoding", "social_engineering", "obfuscation", "cognitive", "structural"],
    },
    "prefill_completion": {
        "defense_layers": ["alignment", "output_filter"],
        "technique_classes": ["structural"],
    },
    "few_shot_attack": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["cognitive", "social_engineering"],
    },
    "template_fuzzing": {
        "defense_layers": ["alignment"],
        "technique_classes": ["structural", "social_engineering"],
    },
    "reasoning_hijack": {
        "defense_layers": ["reasoning"],
        "technique_classes": ["cognitive", "structural"],
    },
    "authority_exploit": {
        "defense_layers": ["alignment"],
        "technique_classes": ["authority", "social_engineering"],
    },
    "agent_task_framing": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["social_engineering", "structural"],
    },
    "tool_output_exploit": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["structural", "social_engineering"],
    },
    "software_spec_injection": {
        "defense_layers": ["alignment", "input_filter"],
        "technique_classes": ["structural", "social_engineering"],
    },
    "codebase_poisoning": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["structural", "cognitive"],
    },
    "ml_exploitation_framing": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["cognitive", "structural"],
    },
    "integration_exploitation": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["structural", "social_engineering"],
    },
    "government_honeypot": {
        "defense_layers": ["alignment", "reasoning"],
        "technique_classes": ["social_engineering", "authority"],
    },
    "encoding_advanced": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding"],
    },
    "multilingual_extended": {
        "defense_layers": ["input_filter", "alignment"],
        "technique_classes": ["encoding"],
    },
    "phonetic_obfuscation": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["obfuscation", "encoding"],
    },
    "transposition_cipher": {
        "defense_layers": ["input_filter"],
        "technique_classes": ["encoding"],
    },
    "genetic_evolution": {
        "defense_layers": ["input_filter", "alignment", "output_filter", "reasoning"],
        "technique_classes": ["encoding", "social_engineering", "obfuscation", "cognitive"],
    },
    "coevolution": {
        "defense_layers": ["input_filter", "alignment", "output_filter", "reasoning"],
        "technique_classes": ["cognitive", "social_engineering", "obfuscation", "encoding"],
    },
    "tree_attack": {
        "defense_layers": ["input_filter", "alignment", "output_filter", "reasoning"],
        "technique_classes": ["cognitive", "structural", "encoding", "obfuscation"],
    },
}

ALL_DEFENSE_LAYERS = ["input_filter", "alignment", "output_filter", "reasoning"]
ALL_TECHNIQUE_CLASSES = [
    "encoding", "social_engineering", "authority", "obfuscation",
    "persona", "cognitive", "structural", "steganographic",
]


@dataclass
class CoverageReport:
    """Results of a coverage analysis."""
    total_mutators: int = 0
    total_categories: int = 0
    defense_layer_coverage: dict[str, int] = field(default_factory=dict)
    technique_class_coverage: dict[str, int] = field(default_factory=dict)
    cross_coverage_matrix: dict[str, dict[str, int]] = field(default_factory=dict)
    uncovered_pairs: list[tuple[str, str]] = field(default_factory=list)
    coverage_score: float = 0.0
    blind_spots: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_mutators": self.total_mutators,
            "total_categories": self.total_categories,
            "defense_layer_coverage": self.defense_layer_coverage,
            "technique_class_coverage": self.technique_class_coverage,
            "cross_coverage_matrix": self.cross_coverage_matrix,
            "uncovered_pairs": [list(p) for p in self.uncovered_pairs],
            "coverage_score": round(self.coverage_score, 4),
            "blind_spots": self.blind_spots,
        }


class CoverageAnalyzer:
    """Analyze attack surface coverage of the mutation system."""

    def __init__(self) -> None:
        from src.prompt_injection import list_mutators
        self._all_mutators = list_mutators()

    def analyze(self) -> CoverageReport:
        """Run full coverage analysis."""
        report = CoverageReport(
            total_mutators=len(self._all_mutators),
            total_categories=len(set(m["category"] for m in self._all_mutators.values())),
        )

        # Count mutators per defense layer
        layer_counts: dict[str, int] = {layer: 0 for layer in ALL_DEFENSE_LAYERS}
        tech_counts: dict[str, int] = {tech: 0 for tech in ALL_TECHNIQUE_CLASSES}

        # Cross-coverage: defense_layer x technique_class
        cross: dict[str, dict[str, int]] = {
            layer: {tech: 0 for tech in ALL_TECHNIQUE_CLASSES}
            for layer in ALL_DEFENSE_LAYERS
        }

        for name, info in self._all_mutators.items():
            cat = info["category"]
            taxonomy = CATEGORY_TAXONOMY.get(cat)
            if not taxonomy:
                continue

            layers = taxonomy["defense_layers"]
            techs = taxonomy["technique_classes"]

            for layer in layers:
                if layer in layer_counts:
                    layer_counts[layer] += 1
            for tech in techs:
                if tech in tech_counts:
                    tech_counts[tech] += 1

            # Cross-product
            for layer in layers:
                for tech in techs:
                    if layer in cross and tech in cross[layer]:
                        cross[layer][tech] += 1

        report.defense_layer_coverage = layer_counts
        report.technique_class_coverage = tech_counts
        report.cross_coverage_matrix = cross

        # Find uncovered pairs
        total_cells = 0
        covered_cells = 0
        for layer in ALL_DEFENSE_LAYERS:
            for tech in ALL_TECHNIQUE_CLASSES:
                total_cells += 1
                if cross[layer][tech] > 0:
                    covered_cells += 1
                else:
                    report.uncovered_pairs.append((layer, tech))

        report.coverage_score = covered_cells / total_cells if total_cells > 0 else 0.0

        # Identify blind spots
        for layer, count in layer_counts.items():
            if count < 5:
                report.blind_spots.append(
                    f"Defense layer '{layer}' has only {count} mutators targeting it"
                )

        for tech, count in tech_counts.items():
            if count < 5:
                report.blind_spots.append(
                    f"Technique class '{tech}' has only {count} mutators"
                )

        for layer, tech in report.uncovered_pairs:
            report.blind_spots.append(
                f"No mutator targets {layer} using {tech} techniques"
            )

        return report

    def get_category_map(self) -> dict[str, dict[str, Any]]:
        """Get full category-to-taxonomy mapping with mutator counts."""
        cat_counts: dict[str, int] = {}
        for info in self._all_mutators.values():
            cat = info["category"]
            cat_counts[cat] = cat_counts.get(cat, 0) + 1

        result = {}
        for cat, taxonomy in CATEGORY_TAXONOMY.items():
            result[cat] = {
                "defense_layers": taxonomy["defense_layers"],
                "technique_classes": taxonomy["technique_classes"],
                "mutator_count": cat_counts.get(cat, 0),
            }
        return result

    def suggest_new_mutators(self) -> list[dict[str, str]]:
        """Suggest new mutators to fill coverage gaps."""
        report = self.analyze()
        suggestions = []

        for layer, tech in report.uncovered_pairs:
            suggestions.append({
                "defense_layer": layer,
                "technique_class": tech,
                "suggestion": (
                    f"Create a mutator targeting '{layer}' defense using "
                    f"'{tech}' techniques. No current mutator covers this combination."
                ),
            })

        return suggestions
