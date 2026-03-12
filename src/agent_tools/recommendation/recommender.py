"""
Recommender — generate ranked improvement recommendations.

Pulls from gap analysis, feedback loop, and technique catalog to
produce a ranked list of what an agent should work on next.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Recommendation:
    """A ranked improvement recommendation."""

    rank: int
    title: str
    kind: str  # "new_category", "new_mutator", "fix_bug", "add_test", "integrate"
    description: str
    priority_score: float = 0.0  # 0.0–1.0 composite score
    coverage_impact: float = 0.0
    effort_estimate: str = "medium"  # "trivial", "easy", "medium", "hard", "complex"
    prerequisites: list[str] = field(default_factory=list)
    rationale: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "rank": self.rank,
            "title": self.title,
            "kind": self.kind,
            "description": self.description,
            "priority_score": self.priority_score,
            "coverage_impact": self.coverage_impact,
            "effort_estimate": self.effort_estimate,
            "prerequisites": self.prerequisites,
            "rationale": self.rationale,
        }


class Recommender:
    """Generate ranked recommendations for framework improvement.

    Usage:
        rec = Recommender()

        # Get top recommendations
        recs = rec.recommend(top_n=5)

        # Get recommendations for a specific area
        recs = rec.recommend_for("encoding")

        # Get the single best next action
        best = rec.next_action()
    """

    def recommend(self, top_n: int = 10) -> list[Recommendation]:
        """Generate ranked improvement recommendations."""
        candidates: list[Recommendation] = []

        # Source 1: Coverage gaps
        candidates.extend(self._from_coverage_gaps())

        # Source 2: Unimplemented techniques
        candidates.extend(self._from_technique_catalog())

        # Source 3: Registration issues
        candidates.extend(self._from_consistency_checks())

        # Source 4: Advisory gaps
        candidates.extend(self._from_advisories())

        # Sort by priority score descending
        candidates.sort(key=lambda r: r.priority_score, reverse=True)

        # Assign ranks
        for i, rec in enumerate(candidates[:top_n], 1):
            rec.rank = i

        return candidates[:top_n]

    def recommend_for(self, area: str) -> list[Recommendation]:
        """Get recommendations related to a specific area."""
        all_recs = self.recommend(top_n=50)
        area_lower = area.lower()
        return [
            r for r in all_recs
            if area_lower in r.title.lower()
            or area_lower in r.description.lower()
        ]

    def next_action(self) -> Recommendation | None:
        """Get the single highest-priority recommendation."""
        recs = self.recommend(top_n=1)
        return recs[0] if recs else None

    def _from_coverage_gaps(self) -> list[Recommendation]:
        """Generate recommendations from coverage gap analysis."""
        recs: list[Recommendation] = []
        try:
            from src.agent_tools.research.gap_analyzer import GapAnalyzer
            analyzer = GapAnalyzer()
            report = analyzer.analyze()
            for gap in report.critical_gaps():
                recs.append(Recommendation(
                    rank=0,
                    title=f"Cover {gap.defense_layer} × {gap.technique_class}",
                    kind="new_category",
                    description=gap.recommendation,
                    priority_score=0.9 if gap.kind == "uncovered_pair" else 0.7,
                    coverage_impact=0.02,
                    effort_estimate="medium",
                    rationale="Uncovered defense layer × technique class combination",
                ))
        except (ImportError, AttributeError):
            pass
        return recs

    def _from_technique_catalog(self) -> list[Recommendation]:
        """Generate recommendations from unimplemented techniques."""
        recs: list[Recommendation] = []
        try:
            from src.agent_tools.research.technique_catalog import TechniqueCatalog
            catalog = TechniqueCatalog()
            for tech in catalog.priority_queue(5):
                effort = {
                    "low": "easy",
                    "medium": "medium",
                    "high": "hard",
                }.get(tech.complexity, "medium")
                recs.append(Recommendation(
                    rank=0,
                    title=f"Implement {tech.name}",
                    kind="new_mutator",
                    description=tech.description,
                    priority_score=0.6 if tech.complexity == "low" else 0.4,
                    coverage_impact=0.005,
                    effort_estimate=effort,
                    rationale=f"Unimplemented technique (domain: {tech.domain}, complexity: {tech.complexity})",
                ))
        except (ImportError, AttributeError):
            pass
        return recs

    def _from_consistency_checks(self) -> list[Recommendation]:
        """Generate recommendations from consistency issues."""
        recs: list[Recommendation] = []
        try:
            from src.agent_tools.consistency import RegistrationChecker
            checker = RegistrationChecker()
            issues = checker.check_all()
            for issue in issues[:5]:
                recs.append(Recommendation(
                    rank=0,
                    title=f"Fix: {issue.description}",
                    kind="fix_bug",
                    description=issue.fix,
                    priority_score=0.8 if issue.severity == "error" else 0.5,
                    effort_estimate="trivial",
                    rationale=f"Registration issue: {issue.kind}",
                ))
        except (ImportError, AttributeError):
            pass
        return recs

    def _from_advisories(self) -> list[Recommendation]:
        """Generate recommendations from unimplemented advisories."""
        recs: list[Recommendation] = []
        try:
            from src.agent_tools.web_research import AdvisoryTracker
            tracker = AdvisoryTracker()
            for adv in tracker.not_implemented():
                recs.append(Recommendation(
                    rank=0,
                    title=f"Cover advisory: {adv.title}",
                    kind="new_mutator",
                    description=adv.description,
                    priority_score=0.85 if adv.severity == "critical" else 0.6,
                    coverage_impact=0.01,
                    effort_estimate="medium",
                    rationale=f"Unimplemented {adv.severity} advisory: {adv.id}",
                ))
        except (ImportError, AttributeError):
            pass
        return recs
