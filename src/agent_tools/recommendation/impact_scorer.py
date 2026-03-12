"""
Impact scorer — estimate the coverage and quality impact of tasks.

Predicts how much a task will improve coverage score, reduce gaps,
and improve overall framework quality.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ImpactScore:
    """Estimated impact of completing a task."""

    coverage_delta: float = 0.0  # Expected change in coverage score
    gap_reduction: int = 0  # Number of gaps this would close
    technique_novelty: float = 0.0  # 0.0–1.0, how novel the technique is
    defense_breadth: float = 0.0  # 0.0–1.0, coverage across defense layers
    composite_score: float = 0.0  # Weighted composite
    rationale: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "coverage_delta": self.coverage_delta,
            "gap_reduction": self.gap_reduction,
            "technique_novelty": self.technique_novelty,
            "defense_breadth": self.defense_breadth,
            "composite_score": self.composite_score,
            "rationale": self.rationale,
        }


class ImpactScorer:
    """Score the expected impact of improvement tasks.

    Usage:
        scorer = ImpactScorer()

        # Score a new category
        impact = scorer.score_new_category(
            defense_layers=["input_filter", "alignment"],
            technique_classes=["encoding"],
            mutator_count=10,
        )

        # Score a bug fix
        impact = scorer.score_bug_fix(affected_mutators=5)

        # Score an integration
        impact = scorer.score_integration(techniques=["t1", "t2", "t3"])
    """

    def score_new_category(
        self,
        defense_layers: list[str],
        technique_classes: list[str],
        mutator_count: int = 10,
    ) -> ImpactScore:
        """Score the impact of adding a new category."""
        # More defense layers = broader coverage
        defense_breadth = min(len(defense_layers) / 4.0, 1.0)

        # More technique classes = more novel
        technique_novelty = min(len(technique_classes) / 3.0, 1.0)

        # Coverage delta based on mutator count
        coverage_delta = min(mutator_count * 0.002, 0.03)

        # Gap reduction
        gap_reduction = len(defense_layers) * len(technique_classes)

        composite = (
            defense_breadth * 0.3 +
            technique_novelty * 0.3 +
            min(coverage_delta * 20, 0.3) +
            min(gap_reduction / 10, 0.1)
        )

        return ImpactScore(
            coverage_delta=coverage_delta,
            gap_reduction=gap_reduction,
            technique_novelty=technique_novelty,
            defense_breadth=defense_breadth,
            composite_score=round(composite, 3),
            rationale=(
                f"Covers {len(defense_layers)} defense layers × "
                f"{len(technique_classes)} technique classes with "
                f"{mutator_count} mutators"
            ),
        )

    def score_bug_fix(self, affected_mutators: int = 1) -> ImpactScore:
        """Score the impact of fixing a bug."""
        return ImpactScore(
            coverage_delta=0.0,
            gap_reduction=0,
            technique_novelty=0.0,
            defense_breadth=0.0,
            composite_score=min(affected_mutators * 0.05, 0.3),
            rationale=f"Fixes {affected_mutators} mutator(s)",
        )

    def score_integration(
        self,
        techniques: list[str],
        license_compatible: bool = True,
    ) -> ImpactScore:
        """Score the impact of integrating an external repo."""
        novelty = min(len(techniques) * 0.15, 1.0)
        coverage_delta = min(len(techniques) * 0.003, 0.02)
        license_penalty = 0.0 if license_compatible else 0.3

        composite = (
            novelty * 0.4 +
            min(coverage_delta * 20, 0.3) -
            license_penalty
        )

        return ImpactScore(
            coverage_delta=coverage_delta,
            gap_reduction=len(techniques),
            technique_novelty=novelty,
            composite_score=max(round(composite, 3), 0),
            rationale=(
                f"Integrates {len(techniques)} techniques"
                f"{' (license compatible)' if license_compatible else ' (license review needed)'}"
            ),
        )

    def compare(self, scores: list[ImpactScore]) -> list[ImpactScore]:
        """Sort impact scores by composite score descending."""
        return sorted(scores, key=lambda s: s.composite_score, reverse=True)
