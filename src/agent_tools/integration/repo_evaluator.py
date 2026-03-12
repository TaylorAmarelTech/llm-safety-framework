"""
Repository evaluator — assess external repos for integration suitability.

Evaluates repos on: language compatibility, license, maintenance activity,
technique coverage, and integration complexity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvaluationReport:
    """Assessment of a repository's integration suitability."""

    repo_name: str
    repo_url: str = ""
    overall_score: float = 0.0
    recommendation: str = ""
    scores: dict[str, float] = field(default_factory=dict)
    strengths: list[str] = field(default_factory=list)
    weaknesses: list[str] = field(default_factory=list)
    integration_plan: list[str] = field(default_factory=list)
    estimated_mutators: int = 0
    blockers: list[str] = field(default_factory=list)

    def is_recommended(self) -> bool:
        return self.overall_score >= 0.6 and not self.blockers

    def to_dict(self) -> dict[str, Any]:
        return {
            "repo_name": self.repo_name,
            "repo_url": self.repo_url,
            "overall_score": round(self.overall_score, 2),
            "recommendation": self.recommendation,
            "scores": {k: round(v, 2) for k, v in self.scores.items()},
            "strengths": self.strengths,
            "weaknesses": self.weaknesses,
            "integration_plan": self.integration_plan,
            "estimated_mutators": self.estimated_mutators,
            "blockers": self.blockers,
        }


class RepoEvaluator:
    """Evaluate external repositories for integration.

    Usage:
        evaluator = RepoEvaluator()
        report = evaluator.evaluate(
            name="TextAttack",
            language="Python",
            license="MIT",
            stars=2500,
            techniques=["TextFooler", "BERT-Attack", "DeepWordBug"],
            has_tests=True,
            last_commit_days_ago=30,
        )
        if report.is_recommended():
            print(report.integration_plan)
    """

    # Acceptable licenses for integration
    PERMISSIVE_LICENSES = {
        "mit", "apache-2.0", "bsd-2-clause", "bsd-3-clause",
        "isc", "unlicense", "0bsd", "wtfpl", "cc0-1.0",
    }

    # Copyleft licenses that require care
    COPYLEFT_LICENSES = {
        "gpl-2.0", "gpl-3.0", "agpl-3.0", "lgpl-2.1", "lgpl-3.0",
    }

    def evaluate(
        self,
        name: str,
        language: str = "",
        license: str = "",
        stars: int = 0,
        techniques: list[str] | None = None,
        has_tests: bool = False,
        has_docs: bool = False,
        last_commit_days_ago: int = 365,
        dependencies: list[str] | None = None,
        url: str = "",
    ) -> EvaluationReport:
        """Evaluate a repository for integration suitability."""
        report = EvaluationReport(repo_name=name, repo_url=url)
        techniques = techniques or []
        dependencies = dependencies or []

        # --- Language compatibility ---
        if language.lower() == "python":
            report.scores["language"] = 1.0
            report.strengths.append("Python — direct import possible")
        elif language.lower() in ("javascript", "typescript"):
            report.scores["language"] = 0.4
            report.weaknesses.append("JavaScript — needs Python port or subprocess bridge")
        elif language.lower() in ("rust", "go", "c", "c++"):
            report.scores["language"] = 0.3
            report.weaknesses.append(f"{language} — needs FFI binding or reimplementation")
        else:
            report.scores["language"] = 0.2

        # --- License ---
        lic = license.lower()
        if lic in self.PERMISSIVE_LICENSES:
            report.scores["license"] = 1.0
            report.strengths.append(f"Permissive license ({license})")
        elif lic in self.COPYLEFT_LICENSES:
            report.scores["license"] = 0.3
            report.weaknesses.append(f"Copyleft license ({license}) — may restrict distribution")
            report.blockers.append(f"Copyleft license: {license}")
        elif lic:
            report.scores["license"] = 0.5
            report.weaknesses.append(f"Unknown license compatibility: {license}")
        else:
            report.scores["license"] = 0.1
            report.blockers.append("No license specified — cannot use")

        # --- Popularity/maintenance ---
        if stars >= 1000:
            report.scores["popularity"] = 1.0
        elif stars >= 100:
            report.scores["popularity"] = 0.7
        elif stars >= 10:
            report.scores["popularity"] = 0.4
        else:
            report.scores["popularity"] = 0.2

        if last_commit_days_ago <= 90:
            report.scores["maintenance"] = 1.0
            report.strengths.append("Actively maintained")
        elif last_commit_days_ago <= 365:
            report.scores["maintenance"] = 0.6
        else:
            report.scores["maintenance"] = 0.3
            report.weaknesses.append("Not recently maintained")

        # --- Technique density ---
        if len(techniques) >= 10:
            report.scores["techniques"] = 1.0
            report.strengths.append(f"{len(techniques)} techniques available")
        elif len(techniques) >= 5:
            report.scores["techniques"] = 0.7
        elif len(techniques) >= 1:
            report.scores["techniques"] = 0.4
        else:
            report.scores["techniques"] = 0.1

        report.estimated_mutators = len(techniques)

        # --- Quality signals ---
        quality = 0.5
        if has_tests:
            quality += 0.25
            report.strengths.append("Has test suite")
        if has_docs:
            quality += 0.25
            report.strengths.append("Has documentation")
        report.scores["quality"] = quality

        # --- Dependency weight ---
        heavy_deps = {"torch", "tensorflow", "jax", "transformers"}
        dep_overlap = set(d.lower() for d in dependencies) & heavy_deps
        if dep_overlap:
            report.scores["dependency_weight"] = 0.3
            report.weaknesses.append(
                f"Heavy dependencies: {', '.join(dep_overlap)} — consider optional import"
            )
        else:
            report.scores["dependency_weight"] = 1.0

        # --- Overall ---
        if report.scores:
            report.overall_score = sum(report.scores.values()) / len(report.scores)

        # --- Recommendation ---
        if report.blockers:
            report.recommendation = "NOT RECOMMENDED — has blockers"
        elif report.overall_score >= 0.7:
            report.recommendation = "Strongly recommended for integration"
        elif report.overall_score >= 0.5:
            report.recommendation = "Worth investigating — consider partial integration"
        else:
            report.recommendation = "Low priority — significant barriers"

        # --- Integration plan ---
        report.integration_plan = self._build_plan(name, language, techniques)

        return report

    def _build_plan(
        self, name: str, language: str, techniques: list[str]
    ) -> list[str]:
        """Generate an integration plan."""
        steps = []
        if language.lower() == "python":
            steps.append(f"1. Install: pip install {name.lower().replace(' ', '-')}")
            steps.append(f"2. Create adapter in src/agent_tools/integration/adapters/{name.lower()}_adapter.py")
            steps.append("3. Wrap each technique as a BaseMutator subclass")
        else:
            steps.append(f"1. Port key algorithms from {language} to Python")
            steps.append("2. Create standalone module in src/prompt_injection/")

        steps.extend([
            f"4. Register {len(techniques)} mutators with @register_mutator",
            "5. Add category to CATEGORY_TAXONOMY in coverage.py",
            "6. Add import to _import_all_mutators() in __init__.py",
            "7. Write tests covering all mutators",
            "8. Run full test suite to verify no regressions",
        ])
        return steps
