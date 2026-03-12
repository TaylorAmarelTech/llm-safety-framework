"""
GitHub repository scanner for discovering relevant repos.

Provides structured search queries and evaluation criteria for finding
open-source projects that contain attack techniques, encoding libraries,
or obfuscation methods that could be integrated as new mutators.

Note: Actual HTTP requests require the agent to call the GitHub API
or use web search tools. This module provides the query templates,
evaluation criteria, and result structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RepoCandidate:
    """A GitHub repository candidate for integration."""

    url: str
    name: str
    description: str = ""
    stars: int = 0
    language: str = ""
    topics: list[str] = field(default_factory=list)
    relevance_score: float = 0.0
    integration_notes: str = ""
    license: str = ""
    last_updated: str = ""
    techniques_found: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "name": self.name,
            "description": self.description,
            "stars": self.stars,
            "language": self.language,
            "topics": self.topics,
            "relevance_score": self.relevance_score,
            "integration_notes": self.integration_notes,
            "license": self.license,
            "techniques_found": self.techniques_found,
        }

    @property
    def is_python(self) -> bool:
        return self.language.lower() == "python"

    @property
    def has_permissive_license(self) -> bool:
        permissive = {"mit", "apache-2.0", "bsd-2-clause", "bsd-3-clause", "isc", "unlicense"}
        return self.license.lower() in permissive


# ---------------------------------------------------------------------------
# Search query templates
# ---------------------------------------------------------------------------

SEARCH_QUERIES: list[dict[str, Any]] = [
    # Prompt injection / jailbreak repos
    {
        "id": "jailbreak_techniques",
        "query": "prompt injection jailbreak LLM",
        "description": "Repos with prompt injection and jailbreak techniques",
        "topics": ["prompt-injection", "jailbreak", "llm-security"],
        "expected_techniques": ["DAN", "persona", "encoding attacks"],
    },
    {
        "id": "adversarial_nlp",
        "query": "adversarial NLP text attack",
        "description": "Adversarial text attack libraries",
        "topics": ["adversarial-nlp", "adversarial-attacks", "text-attack"],
        "expected_techniques": ["TextFooler", "BERT-Attack", "char swap"],
        "key_repos": ["QData/TextAttack", "jind11/TextFooler"],
    },
    {
        "id": "text_encoding",
        "query": "text encoding steganography Python",
        "description": "Text encoding and steganography libraries",
        "topics": ["steganography", "encoding", "cipher"],
        "expected_techniques": ["zero-width encoding", "Unicode tricks"],
    },
    {
        "id": "obfuscation_tools",
        "query": "text obfuscation homoglyph confusable",
        "description": "Text obfuscation and homoglyph tools",
        "topics": ["homoglyph", "unicode", "obfuscation"],
        "key_repos": ["vhf/confusable_homoglyphs", "codebox/homoglyph"],
    },
    {
        "id": "cipher_implementations",
        "query": "classical cipher Python implementation",
        "description": "Classical cipher implementations",
        "topics": ["cipher", "cryptography", "classical"],
        "expected_techniques": ["Playfair", "Bifid", "ADFGVX"],
    },
    {
        "id": "red_teaming",
        "query": "LLM red teaming safety testing",
        "description": "LLM red teaming and safety evaluation frameworks",
        "topics": ["red-teaming", "ai-safety", "llm-evaluation"],
        "key_repos": [
            "NVIDIA/garak",
            "Azure/PyRIT",
            "leondz/garak",
        ],
    },
    {
        "id": "language_games",
        "query": "language game cipher pig latin",
        "description": "Language games and word transformation tools",
        "topics": ["language-game", "word-game", "cipher"],
        "expected_techniques": ["Pig Latin", "Cockney", "Verlan"],
    },
    {
        "id": "unicode_exploits",
        "query": "Unicode exploit bidi override homograph",
        "description": "Unicode-based exploit techniques",
        "topics": ["unicode", "bidi", "homograph"],
        "expected_techniques": ["bidi override", "homograph attacks", "confusables"],
    },
    {
        "id": "transliteration",
        "query": "transliteration romanization Python",
        "description": "Transliteration and romanization libraries",
        "topics": ["transliteration", "romanization", "i18n"],
        "key_repos": [
            "barseghyanartur/transliterate",
            "opendatalab/MinerU",
        ],
    },
    {
        "id": "data_encoding",
        "query": "base encoding base91 base65536 Python",
        "description": "Exotic base encoding libraries",
        "topics": ["encoding", "base-encoding"],
        "key_repos": ["qntm/base65536", "qntm/base2048"],
    },
]

# ---------------------------------------------------------------------------
# Known high-value repos (curated)
# ---------------------------------------------------------------------------

KNOWN_REPOS: list[RepoCandidate] = [
    RepoCandidate(
        url="https://github.com/QData/TextAttack",
        name="TextAttack",
        description="Framework for adversarial attacks on NLP models",
        language="Python",
        license="MIT",
        topics=["adversarial-nlp", "text-attack"],
        techniques_found=["TextFooler", "BERT-Attack", "CheckList", "DeepWordBug",
                          "PWWS", "BAE", "Pruthi", "TextBugger"],
        relevance_score=0.95,
        integration_notes="Rich library of character/word/sentence-level attacks. "
        "Can adapt recipe patterns as new mutator categories.",
    ),
    RepoCandidate(
        url="https://github.com/NVIDIA/garak",
        name="garak",
        description="LLM vulnerability scanner",
        language="Python",
        license="Apache-2.0",
        topics=["llm-security", "red-teaming"],
        techniques_found=["encoding probes", "continuation attacks", "dan variants",
                          "glitch tokens", "language-based attacks"],
        relevance_score=0.90,
        integration_notes="Integration adapter already exists in src/integrations/. "
        "Mine for additional attack patterns.",
    ),
    RepoCandidate(
        url="https://github.com/Azure/PyRIT",
        name="PyRIT",
        description="Python Risk Identification Toolkit for generative AI",
        language="Python",
        license="MIT",
        topics=["ai-safety", "red-teaming"],
        techniques_found=["multi-turn attacks", "scoring rubrics", "orchestration"],
        relevance_score=0.88,
        integration_notes="Integration adapter already exists. "
        "Study orchestration patterns for agent improvement.",
    ),
    RepoCandidate(
        url="https://github.com/vhf/confusable_homoglyphs",
        name="confusable_homoglyphs",
        description="Unicode confusable character detection and generation",
        language="Python",
        license="MIT",
        topics=["unicode", "homoglyph", "confusables"],
        techniques_found=["homoglyph generation", "script detection", "confusable lookup"],
        relevance_score=0.80,
        integration_notes="Could enhance existing obfuscation mutators with full "
        "Unicode Confusables database (UTS #39).",
    ),
    RepoCandidate(
        url="https://github.com/qntm/base65536",
        name="base65536",
        description="Encode binary data in Unicode CJK characters",
        language="JavaScript",
        license="MIT",
        topics=["encoding", "unicode"],
        techniques_found=["base65536 encoding"],
        relevance_score=0.70,
        integration_notes="JavaScript only — would need Python port. "
        "Concept is simple: map byte pairs to CJK codepoints.",
    ),
    RepoCandidate(
        url="https://github.com/RUB-NDS/ChatGPT-Jailbreaks",
        name="ChatGPT-Jailbreaks",
        description="Collection of ChatGPT jailbreak prompts and techniques",
        language="",
        license="",
        topics=["jailbreak", "prompt-injection"],
        techniques_found=["DAN variants", "developer mode", "mongotom", "STAN"],
        relevance_score=0.75,
        integration_notes="Reference for additional named jailbreak templates. "
        "Some already implemented in named_jailbreaks.py.",
    ),
    RepoCandidate(
        url="https://github.com/dmarx/bench-warmers",
        name="bench-warmers",
        description="Prompt injection benchmark and attack dataset",
        language="Python",
        license="MIT",
        topics=["prompt-injection", "benchmark"],
        techniques_found=["injection patterns", "defense evasion"],
        relevance_score=0.72,
    ),
    RepoCandidate(
        url="https://github.com/protectai/rebuff",
        name="rebuff",
        description="Self-hardening prompt injection detector",
        language="Python",
        license="Apache-2.0",
        topics=["prompt-injection", "defense"],
        techniques_found=["injection detection heuristics", "canary tokens"],
        relevance_score=0.65,
        integration_notes="Study detection patterns to understand what defenses "
        "our mutators need to bypass.",
    ),
]


class GitHubScanner:
    """Structured GitHub search helper for agents.

    This module does NOT make HTTP requests. Instead, it provides:
    - Pre-built search queries an agent can use with the GitHub API
    - A curated list of known high-value repos
    - Evaluation criteria for assessing repo usefulness
    - Result structures for organizing discoveries

    Usage:
        scanner = GitHubScanner()

        # Get search queries for the agent to execute
        queries = scanner.search_queries()

        # Get curated known repos
        repos = scanner.known_repos()

        # Evaluate a discovered repo
        score = scanner.evaluate(repo_candidate)

        # Get queries for a specific domain
        encoding_queries = scanner.queries_for_domain("encoding")
    """

    def search_queries(self) -> list[dict[str, Any]]:
        """Return structured search queries for agents to execute."""
        return list(SEARCH_QUERIES)

    def known_repos(self, min_relevance: float = 0.0) -> list[RepoCandidate]:
        """Return curated list of known high-value repos."""
        return [r for r in KNOWN_REPOS if r.relevance_score >= min_relevance]

    def queries_for_domain(self, domain: str) -> list[dict[str, Any]]:
        """Get search queries relevant to a specific domain."""
        domain_map: dict[str, list[str]] = {
            "encoding": ["text_encoding", "data_encoding"],
            "adversarial": ["adversarial_nlp"],
            "cipher": ["cipher_implementations"],
            "obfuscation": ["obfuscation_tools", "unicode_exploits"],
            "language": ["language_games", "transliteration"],
            "jailbreak": ["jailbreak_techniques", "red_teaming"],
        }
        query_ids = domain_map.get(domain, [])
        return [q for q in SEARCH_QUERIES if q["id"] in query_ids]

    def evaluate(self, candidate: RepoCandidate) -> dict[str, Any]:
        """Evaluate a repo candidate for integration suitability.

        Returns a structured assessment with scores and recommendations.
        """
        scores: dict[str, float] = {}

        # Language compatibility (Python preferred)
        scores["language"] = 1.0 if candidate.is_python else 0.3

        # License compatibility
        scores["license"] = 1.0 if candidate.has_permissive_license else 0.2

        # Star count (popularity proxy)
        if candidate.stars >= 1000:
            scores["popularity"] = 1.0
        elif candidate.stars >= 100:
            scores["popularity"] = 0.7
        elif candidate.stars >= 10:
            scores["popularity"] = 0.4
        else:
            scores["popularity"] = 0.2

        # Technique density
        n_techniques = len(candidate.techniques_found)
        scores["technique_density"] = min(1.0, n_techniques / 5.0)

        # Overall
        overall = sum(scores.values()) / len(scores)

        return {
            "candidate": candidate.name,
            "scores": scores,
            "overall_score": round(overall, 2),
            "recommendation": (
                "Strong candidate for integration"
                if overall >= 0.7
                else "Worth investigating"
                if overall >= 0.5
                else "Low priority"
            ),
            "blockers": [
                issue
                for issue in [
                    None if candidate.is_python else "Not Python — needs port or adapter",
                    None if candidate.has_permissive_license else f"License: {candidate.license or 'unknown'}",
                ]
                if issue
            ],
        }

    def generate_search_prompt(self, domain: str = "") -> str:
        """Generate a prompt for an agent to search GitHub.

        Returns a structured instruction string that an agent can use
        to search for relevant repositories.
        """
        queries = self.queries_for_domain(domain) if domain else SEARCH_QUERIES[:5]
        lines = [
            "Search GitHub for repositories matching these queries:",
            "",
        ]
        for q in queries:
            lines.append(f"- **{q['id']}**: `{q['query']}`")
            lines.append(f"  Topics: {', '.join(q.get('topics', []))}")
            if q.get("key_repos"):
                lines.append(f"  Known repos: {', '.join(q['key_repos'])}")
            lines.append("")

        lines.extend([
            "For each repo found, record:",
            "- URL, name, description, stars, language, license",
            "- What techniques/algorithms does it implement?",
            "- Is it Python? Does it have a permissive license?",
            "- How could its techniques be adapted as mutators?",
        ])
        return "\n".join(lines)
