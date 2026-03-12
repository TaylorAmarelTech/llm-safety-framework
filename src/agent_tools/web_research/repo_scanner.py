"""
Repo scanner — discover and evaluate GitHub repositories for integration.

Generates structured GitHub API search queries and evaluates repos
on relevance, license compatibility, and technique coverage.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RepoResult:
    """A GitHub repository evaluation result."""

    name: str
    owner: str
    url: str = ""
    description: str = ""
    stars: int = 0
    language: str = ""
    license: str = ""
    last_updated: str = ""
    topics: list[str] = field(default_factory=list)
    techniques_found: list[str] = field(default_factory=list)
    relevance_score: float = 0.0
    integration_difficulty: str = "medium"  # "easy", "medium", "hard"

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "owner": self.owner,
            "url": self.url or f"https://github.com/{self.owner}/{self.name}",
            "description": self.description[:200],
            "stars": self.stars,
            "language": self.language,
            "license": self.license,
            "topics": self.topics,
            "techniques_found": self.techniques_found,
            "relevance_score": self.relevance_score,
            "integration_difficulty": self.integration_difficulty,
        }


# Pre-curated repos known to be relevant
KNOWN_REPOS: list[RepoResult] = [
    RepoResult(
        name="TextAttack",
        owner="QData",
        url="https://github.com/QData/TextAttack",
        description="NLP adversarial attacks, data augmentation, and model training",
        stars=2800,
        language="Python",
        license="MIT",
        topics=["adversarial-attacks", "nlp", "text-augmentation"],
        techniques_found=["textfooler", "bert_attack", "checklist", "deepwordbug", "bae"],
        relevance_score=0.9,
        integration_difficulty="medium",
    ),
    RepoResult(
        name="garak",
        owner="NVIDIA",
        url="https://github.com/NVIDIA/garak",
        description="LLM vulnerability scanner",
        stars=2000,
        language="Python",
        license="Apache-2.0",
        topics=["llm-security", "red-teaming", "vulnerability-scanner"],
        techniques_found=["encoding_probes", "payload_splitting", "jailbreak_templates"],
        relevance_score=0.95,
        integration_difficulty="easy",
    ),
    RepoResult(
        name="PyRIT",
        owner="Azure",
        url="https://github.com/Azure/PyRIT",
        description="Python Risk Identification Toolkit for AI red teaming",
        stars=1800,
        language="Python",
        license="MIT",
        topics=["ai-safety", "red-teaming", "risk-assessment"],
        techniques_found=["crescendo", "multi_turn", "prompt_templates"],
        relevance_score=0.9,
        integration_difficulty="medium",
    ),
    RepoResult(
        name="llm-attacks",
        owner="llm-attacks",
        url="https://github.com/llm-attacks/llm-attacks",
        description="Universal adversarial attacks on aligned LLMs (GCG)",
        stars=3200,
        language="Python",
        license="MIT",
        topics=["adversarial-attacks", "jailbreak", "gcg"],
        techniques_found=["gcg_suffix", "universal_attack", "transfer_attack"],
        relevance_score=0.85,
        integration_difficulty="hard",
    ),
    RepoResult(
        name="HackAPrompt",
        owner="trigaten",
        url="https://github.com/trigaten/Prompt_Injection",
        description="Prompt injection dataset and taxonomy from HackAPrompt competition",
        stars=600,
        language="Python",
        license="MIT",
        topics=["prompt-injection", "benchmark", "dataset"],
        techniques_found=["instruction_override", "context_ignoring", "payload_splitting"],
        relevance_score=0.85,
        integration_difficulty="easy",
    ),
    RepoResult(
        name="JailbreakBench",
        owner="JailbreakBench",
        url="https://github.com/JailbreakBench/jailbreakbench",
        description="Standardized benchmark for jailbreak attacks",
        stars=400,
        language="Python",
        license="MIT",
        topics=["jailbreak", "benchmark", "evaluation"],
        techniques_found=["pair", "tap", "gcg", "autodan"],
        relevance_score=0.8,
        integration_difficulty="medium",
    ),
]

# GitHub API search queries
SEARCH_QUERIES: list[dict[str, str]] = [
    {"query": "llm jailbreak attack", "sort": "stars", "language": "Python"},
    {"query": "prompt injection security", "sort": "stars", "language": "Python"},
    {"query": "adversarial text attack NLP", "sort": "updated", "language": "Python"},
    {"query": "red teaming AI safety", "sort": "stars", "language": "Python"},
    {"query": "text obfuscation encoding", "sort": "stars", "language": "Python"},
    {"query": "unicode homoglyph confusable", "sort": "stars", "language": "Python"},
    {"query": "cipher encoding steganography text", "sort": "stars", "language": "Python"},
]

# Compatible licenses (can integrate freely)
COMPATIBLE_LICENSES: set[str] = {
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause",
    "ISC", "Unlicense", "CC0-1.0", "WTFPL",
}


class RepoScanner:
    """Discover and evaluate GitHub repositories for technique integration.

    Usage:
        scanner = RepoScanner()

        # Get known relevant repos
        repos = scanner.known_repos()

        # Filter by relevance
        top = scanner.known_repos(min_relevance=0.85)

        # Generate GitHub API search prompt
        prompt = scanner.github_search_prompt("encoding attacks")

        # Evaluate a new repo
        score = scanner.evaluate(repo_result)

        # Check license compatibility
        ok = scanner.is_license_compatible("MIT")
    """

    def known_repos(self, min_relevance: float = 0.0) -> list[RepoResult]:
        """Get curated list of known relevant repos."""
        return [
            r for r in KNOWN_REPOS
            if r.relevance_score >= min_relevance
        ]

    def github_search_prompt(self, topic: str) -> str:
        """Generate a GitHub API search prompt for an agent."""
        return (
            f"Search GitHub for repositories related to '{topic}'.\n"
            f"API endpoint: https://api.github.com/search/repositories\n"
            f"Parameters: q={topic}+language:python&sort=stars&per_page=20\n"
            f"For each result, check:\n"
            f"  1. License compatibility ({', '.join(sorted(COMPATIBLE_LICENSES)[:5])})\n"
            f"  2. Python files containing attack/encode/mutate/transform functions\n"
            f"  3. Active maintenance (last commit within 6 months)\n"
            f"  4. Technique novelty (does our framework already have this?)\n"
        )

    def search_queries(self) -> list[dict[str, str]]:
        """Get pre-built GitHub search queries."""
        return SEARCH_QUERIES

    def evaluate(self, repo: RepoResult) -> float:
        """Score a repository's integration value (0.0–1.0)."""
        score = 0.0

        # Language compatibility
        if repo.language == "Python":
            score += 0.2
        elif repo.language in ("JavaScript", "TypeScript", "Rust"):
            score += 0.05

        # License
        if repo.license in COMPATIBLE_LICENSES:
            score += 0.15
        elif repo.license:
            score += 0.05

        # Popularity
        if repo.stars > 1000:
            score += 0.15
        elif repo.stars > 100:
            score += 0.1
        elif repo.stars > 10:
            score += 0.05

        # Techniques found
        tech_score = min(len(repo.techniques_found) * 0.05, 0.25)
        score += tech_score

        # Topic relevance
        relevant_topics = {
            "jailbreak", "adversarial", "red-team", "llm-security",
            "prompt-injection", "safety", "attack", "nlp",
        }
        topic_overlap = len(set(repo.topics) & relevant_topics)
        score += min(topic_overlap * 0.05, 0.15)

        # Description keyword bonus
        desc = repo.description.lower()
        for kw in ["attack", "jailbreak", "injection", "adversarial", "safety"]:
            if kw in desc:
                score += 0.02

        return min(score, 1.0)

    def is_license_compatible(self, license_name: str) -> bool:
        """Check if a license is compatible for integration."""
        return license_name in COMPATIBLE_LICENSES

    def integration_plan(self, repo: RepoResult) -> list[str]:
        """Generate integration steps for a repository."""
        steps = [
            f"Clone/review {repo.url or f'https://github.com/{repo.owner}/{repo.name}'}",
            f"Identify extractable techniques: {', '.join(repo.techniques_found) or 'TBD'}",
            f"Check license: {repo.license} ({'compatible' if self.is_license_compatible(repo.license) else 'review needed'})",
        ]

        if repo.integration_difficulty == "easy":
            steps.append("Direct port: copy relevant functions with attribution")
        elif repo.integration_difficulty == "medium":
            steps.append("Adapter needed: create wrapper matching BaseMutator interface")
        else:
            steps.append("Complex integration: may need significant refactoring or C/Rust bindings")

        steps.extend([
            "Register new mutators in src/prompt_injection/__init__.py",
            "Add taxonomy entries to src/prompt_injection/coverage.py",
            "Write tests covering all new mutators",
            "Run full test suite to verify no regressions",
        ])

        return steps
