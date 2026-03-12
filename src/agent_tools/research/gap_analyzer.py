"""
Coverage gap analyzer.

Combines the coverage matrix from coverage.py with the technique catalog
to produce actionable recommendations for what to build next.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Gap:
    """A single coverage gap."""

    id: str
    kind: str  # "uncovered_pair", "low_count_layer", "low_count_technique",
    #            "missing_domain", "unimplemented_technique"
    severity: str  # "critical", "high", "medium", "low"
    description: str
    recommendation: str
    defense_layer: str = ""
    technique_class: str = ""
    current_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "kind": self.kind,
            "severity": self.severity,
            "description": self.description,
            "recommendation": self.recommendation,
            "defense_layer": self.defense_layer,
            "technique_class": self.technique_class,
            "current_count": self.current_count,
        }


@dataclass
class GapReport:
    """Full gap analysis report."""

    gaps: list[Gap] = field(default_factory=list)
    coverage_score: float = 0.0
    total_mutators: int = 0
    total_categories: int = 0
    uncovered_pairs: list[tuple[str, str]] = field(default_factory=list)
    weak_layers: list[str] = field(default_factory=list)
    weak_techniques: list[str] = field(default_factory=list)

    def critical_gaps(self) -> list[Gap]:
        return [g for g in self.gaps if g.severity in ("critical", "high")]

    def by_kind(self, kind: str) -> list[Gap]:
        return [g for g in self.gaps if g.kind == kind]

    def to_dict(self) -> dict[str, Any]:
        return {
            "coverage_score": self.coverage_score,
            "total_mutators": self.total_mutators,
            "total_categories": self.total_categories,
            "gap_count": len(self.gaps),
            "critical_count": len(self.critical_gaps()),
            "gaps": [g.to_dict() for g in self.gaps],
        }

    def summary(self) -> str:
        lines = [
            f"Coverage score: {self.coverage_score:.1%}",
            f"Total mutators: {self.total_mutators}",
            f"Total categories: {self.total_categories}",
            f"Gaps found: {len(self.gaps)} ({len(self.critical_gaps())} critical/high)",
        ]
        if self.uncovered_pairs:
            lines.append(f"Uncovered layer×technique pairs: {len(self.uncovered_pairs)}")
        return "\n".join(lines)


class GapAnalyzer:
    """Analyze coverage gaps and produce recommendations.

    Usage:
        analyzer = GapAnalyzer()
        report = analyzer.analyze()
        print(report.summary())
        for gap in report.critical_gaps():
            print(f"  [{gap.severity}] {gap.description}")
            print(f"    -> {gap.recommendation}")
    """

    LOW_COUNT_THRESHOLD = 10  # Layer/technique with fewer mutators = weak

    def analyze(self) -> GapReport:
        """Run full gap analysis."""
        report = GapReport()
        gap_id = 0

        try:
            from src.prompt_injection.coverage import CoverageAnalyzer

            ca = CoverageAnalyzer()
            cov_report = ca.analyze()
            report.coverage_score = cov_report.coverage_score
            report.total_mutators = cov_report.total_mutators
            report.total_categories = cov_report.total_categories
            report.uncovered_pairs = cov_report.uncovered_pairs

            # 1. Uncovered defense_layer × technique_class pairs
            for layer, tech in cov_report.uncovered_pairs:
                report.gaps.append(
                    Gap(
                        id=f"gap_{gap_id:03d}",
                        kind="uncovered_pair",
                        severity="critical",
                        description=(
                            f"No mutator targets '{layer}' defense using '{tech}' techniques"
                        ),
                        recommendation=(
                            f"Create a new category or add mutators that target the "
                            f"'{layer}' defense layer using '{tech}' class techniques. "
                            f"This is a blind spot in the attack surface."
                        ),
                        defense_layer=layer,
                        technique_class=tech,
                    )
                )
                gap_id += 1

            # 2. Weak defense layers
            for layer, count in cov_report.defense_layer_coverage.items():
                if count < self.LOW_COUNT_THRESHOLD:
                    report.weak_layers.append(layer)
                    report.gaps.append(
                        Gap(
                            id=f"gap_{gap_id:03d}",
                            kind="low_count_layer",
                            severity="high",
                            description=(
                                f"Defense layer '{layer}' has only {count} mutators"
                            ),
                            recommendation=(
                                f"Add more mutators targeting the '{layer}' defense layer. "
                                f"Current count ({count}) is below threshold ({self.LOW_COUNT_THRESHOLD})."
                            ),
                            defense_layer=layer,
                            current_count=count,
                        )
                    )
                    gap_id += 1

            # 3. Weak technique classes
            for tech, count in cov_report.technique_class_coverage.items():
                if count < self.LOW_COUNT_THRESHOLD:
                    report.weak_techniques.append(tech)
                    report.gaps.append(
                        Gap(
                            id=f"gap_{gap_id:03d}",
                            kind="low_count_technique",
                            severity="high" if count < 5 else "medium",
                            description=(
                                f"Technique class '{tech}' has only {count} mutators"
                            ),
                            recommendation=(
                                f"Add more mutators using '{tech}' techniques. "
                                f"Current count ({count}) is below threshold ({self.LOW_COUNT_THRESHOLD})."
                            ),
                            technique_class=tech,
                            current_count=count,
                        )
                    )
                    gap_id += 1

        except ImportError:
            report.gaps.append(
                Gap(
                    id="gap_import_error",
                    kind="system_error",
                    severity="critical",
                    description="Could not import CoverageAnalyzer",
                    recommendation="Check that src.prompt_injection is importable",
                )
            )

        # 4. Check unimplemented techniques from catalog
        try:
            from src.agent_tools.research.technique_catalog import TechniqueCatalog

            catalog = TechniqueCatalog()
            for tech in catalog.priority_queue(20):
                report.gaps.append(
                    Gap(
                        id=f"gap_{gap_id:03d}",
                        kind="unimplemented_technique",
                        severity="low" if tech.complexity == "high" else "medium",
                        description=(
                            f"Technique '{tech.name}' ({tech.domain}) is not yet implemented"
                        ),
                        recommendation=(
                            f"Implement '{tech.name}': {tech.description}. "
                            f"Complexity: {tech.complexity}. "
                            f"Suggested category: {tech.suggested_category or 'TBD'}. "
                            f"References: {', '.join(tech.references) if tech.references else 'none'}."
                        ),
                    )
                )
                gap_id += 1

        except ImportError:
            pass

        return report

    def suggest_next_category(self) -> dict[str, Any]:
        """Suggest the best next category to implement.

        Considers uncovered pairs, weak areas, and unimplemented techniques
        to recommend a coherent new category.
        """
        report = self.analyze()

        suggestions = []

        # Group uncovered pairs by technique class
        uncovered_by_tech: dict[str, list[str]] = {}
        for layer, tech in report.uncovered_pairs:
            uncovered_by_tech.setdefault(tech, []).append(layer)

        for tech, layers in uncovered_by_tech.items():
            suggestions.append({
                "reason": f"Uncovered technique class '{tech}' for layers: {layers}",
                "suggested_name": f"{tech}_exploit",
                "target_layers": layers,
                "target_technique": tech,
                "priority": "critical",
            })

        # Low-count technique classes
        for tech in report.weak_techniques:
            if tech not in uncovered_by_tech:
                suggestions.append({
                    "reason": f"Technique class '{tech}' has low coverage",
                    "suggested_name": f"{tech}_extended",
                    "target_technique": tech,
                    "priority": "high",
                })

        return {
            "suggestions": suggestions[:5],
            "coverage_score": report.coverage_score,
            "total_gaps": len(report.gaps),
        }
