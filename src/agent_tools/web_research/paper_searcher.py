"""
Paper searcher — find and summarize academic papers on LLM safety.

Builds structured search queries for Semantic Scholar, arXiv, and
OpenAlex so agents can discover new attack/defense techniques.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PaperResult:
    """A single academic paper result."""

    title: str
    authors: list[str] = field(default_factory=list)
    year: int = 0
    venue: str = ""
    abstract: str = ""
    url: str = ""
    doi: str = ""
    citation_count: int = 0
    relevance_score: float = 0.0
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "authors": self.authors[:5],
            "year": self.year,
            "venue": self.venue,
            "abstract": self.abstract[:300],
            "url": self.url,
            "doi": self.doi,
            "citation_count": self.citation_count,
            "relevance_score": self.relevance_score,
            "tags": self.tags,
        }


# Pre-built search queries for common topics
SEARCH_QUERIES: dict[str, list[str]] = {
    "prompt_injection": [
        "prompt injection attack LLM",
        "jailbreak large language model",
        "adversarial prompt attack",
        "instruction hierarchy violation",
    ],
    "safety_alignment": [
        "RLHF safety alignment",
        "constitutional AI",
        "red teaming language model",
        "AI safety evaluation benchmark",
    ],
    "encoding_attack": [
        "text encoding adversarial bypass",
        "unicode homoglyph attack",
        "steganographic text encoding",
        "base encoding obfuscation NLP",
    ],
    "social_engineering": [
        "social engineering LLM roleplay",
        "persona attack language model",
        "authority impersonation AI",
        "multi-turn manipulation conversational AI",
    ],
    "defense": [
        "input filter adversarial robustness",
        "output guard LLM safety",
        "perplexity detection prompt injection",
        "classifier defense jailbreak",
    ],
}

# Key venues for LLM safety research
RELEVANT_VENUES: list[str] = [
    "NeurIPS", "ICML", "ICLR", "ACL", "EMNLP", "NAACL",
    "USENIX Security", "IEEE S&P", "CCS", "NDSS",
    "AAAI", "AIES", "FAccT",
]


class PaperSearcher:
    """Build and manage academic paper searches for agents.

    Usage:
        searcher = PaperSearcher()

        # Get pre-built queries for a topic
        queries = searcher.queries_for("prompt_injection")

        # Generate a Semantic Scholar API search prompt
        prompt = searcher.semantic_scholar_prompt("encoding attacks")

        # Generate an arXiv search prompt
        prompt = searcher.arxiv_prompt("jailbreak defense")

        # Get known landmark papers
        landmarks = searcher.landmark_papers()

        # Score paper relevance
        score = searcher.relevance_score(paper_result)
    """

    def queries_for(self, topic: str) -> list[str]:
        """Get pre-built search queries for a topic."""
        return SEARCH_QUERIES.get(topic, [f"{topic} LLM safety"])

    def all_topics(self) -> list[str]:
        """List all available search topics."""
        return sorted(SEARCH_QUERIES.keys())

    def semantic_scholar_prompt(self, topic: str) -> str:
        """Generate a Semantic Scholar API search prompt for an agent."""
        queries = self.queries_for(topic)
        return (
            f"Search Semantic Scholar for papers on '{topic}'.\n"
            f"Suggested queries: {queries}\n"
            f"API endpoint: https://api.semanticscholar.org/graph/v1/paper/search\n"
            f"Parameters: query=<query>&limit=20&fields=title,authors,year,venue,"
            f"abstract,citationCount,url\n"
            f"Filter for papers from {RELEVANT_VENUES[:6]} when possible.\n"
            f"Sort by citation count descending for established work, "
            f"or by year descending for recent techniques."
        )

    def arxiv_prompt(self, topic: str) -> str:
        """Generate an arXiv search prompt for an agent."""
        queries = self.queries_for(topic)
        return (
            f"Search arXiv for papers on '{topic}'.\n"
            f"Suggested queries: {queries}\n"
            f"API endpoint: https://export.arxiv.org/api/query\n"
            f"Parameters: search_query=all:<query>&max_results=20&sortBy=submittedDate\n"
            f"Focus on cs.CR (cryptography/security), cs.CL (computation & language), "
            f"and cs.AI (artificial intelligence) categories."
        )

    def landmark_papers(self) -> list[PaperResult]:
        """Return known landmark papers in LLM safety research."""
        return [
            PaperResult(
                title="Ignore This Title and HackAPrompt: Exposing Systemic Weaknesses of LLMs",
                authors=["Schulhoff, S.", "Pinto, J.", "et al."],
                year=2023,
                venue="EMNLP",
                tags=["prompt_injection", "benchmark"],
            ),
            PaperResult(
                title="Universal and Transferable Adversarial Attacks on Aligned LLMs",
                authors=["Zou, A.", "Wang, Z.", "et al."],
                year=2023,
                venue="arXiv",
                tags=["adversarial", "GCG", "universal_attack"],
            ),
            PaperResult(
                title="Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications",
                authors=["Greshake, K.", "Abdelnabi, S.", "et al."],
                year=2023,
                venue="AISec",
                tags=["indirect_injection", "application"],
            ),
            PaperResult(
                title="Jailbroken: How Does LLM Safety Training Fail?",
                authors=["Wei, A.", "Haghtalab, N.", "Steinhardt, J."],
                year=2023,
                venue="NeurIPS",
                tags=["jailbreak", "safety_training", "failure_modes"],
            ),
            PaperResult(
                title="AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned LLMs",
                authors=["Liu, X.", "Xu, N.", "et al."],
                year=2023,
                venue="ICLR",
                tags=["automated", "jailbreak", "genetic_algorithm"],
            ),
            PaperResult(
                title="DeepInception: Hypnotize LLM to Be Jailbreaker",
                authors=["Li, X.", "et al."],
                year=2023,
                venue="arXiv",
                tags=["nested_scenario", "roleplay", "inception"],
            ),
            PaperResult(
                title="Many-shot Jailbreaking",
                authors=["Anil, C.", "et al."],
                year=2024,
                venue="Anthropic",
                tags=["many_shot", "in_context_learning", "scaling"],
            ),
            PaperResult(
                title="Skeleton Key: A Jailbreak Technique",
                authors=["Microsoft"],
                year=2024,
                venue="Microsoft Security",
                tags=["skeleton_key", "behavioral_guidelines"],
            ),
        ]

    def relevance_score(self, paper: PaperResult) -> float:
        """Score a paper's relevance to the project (0.0–1.0)."""
        score = 0.0
        relevant_keywords = [
            "jailbreak", "prompt injection", "adversarial", "safety",
            "red team", "alignment", "bypass", "attack", "defense",
            "llm", "language model", "encoding", "obfuscation",
        ]
        title_lower = paper.title.lower()
        abstract_lower = paper.abstract.lower()

        # Title keyword matches (high weight)
        for kw in relevant_keywords:
            if kw in title_lower:
                score += 0.1

        # Abstract keyword matches (lower weight)
        for kw in relevant_keywords:
            if kw in abstract_lower:
                score += 0.03

        # Venue bonus
        if paper.venue in RELEVANT_VENUES:
            score += 0.15

        # Recency bonus
        if paper.year >= 2024:
            score += 0.1
        elif paper.year >= 2023:
            score += 0.05

        # Citation bonus
        if paper.citation_count > 100:
            score += 0.1
        elif paper.citation_count > 20:
            score += 0.05

        return min(score, 1.0)
