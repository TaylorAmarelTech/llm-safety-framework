"""
Reference index — papers, standards, CVEs, and repos.

Structured index of academic and technical references relevant to
prompt injection, adversarial NLP, and encoding techniques. Agents
can query this to find sources for new techniques and cite them
properly in generated code.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Reference:
    """A single reference (paper, standard, repo, etc.)."""

    id: str
    kind: str  # "paper", "standard", "repo", "blog", "cve", "dataset"
    title: str
    authors: list[str] = field(default_factory=list)
    year: int = 0
    url: str = ""
    venue: str = ""  # Conference or journal
    abstract: str = ""
    tags: list[str] = field(default_factory=list)
    techniques: list[str] = field(default_factory=list)

    def citation(self) -> str:
        """Generate a citation string."""
        authors_str = ", ".join(self.authors[:3])
        if len(self.authors) > 3:
            authors_str += " et al."
        if self.year:
            return f"{authors_str} ({self.year}) — {self.title}"
        return f"{authors_str} — {self.title}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "kind": self.kind,
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "url": self.url,
            "tags": self.tags,
            "techniques": self.techniques,
        }


# ---------------------------------------------------------------------------
# Master reference index
# ---------------------------------------------------------------------------

_REFERENCES: list[Reference] = [
    # --- Prompt Injection Papers ---
    Reference(
        id="perez2022ignore",
        kind="paper",
        title="Ignore This Title and HackAPrompt: Exposing Systemic Weaknesses of LLMs",
        authors=["Fábio Perez", "Ian Ribeiro"],
        year=2022,
        venue="arXiv",
        tags=["prompt-injection", "jailbreak"],
        techniques=["instruction override", "context manipulation"],
    ),
    Reference(
        id="greshake2023indirect",
        kind="paper",
        title="Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection",
        authors=["Kai Greshake", "Sahar Abdelnabi", "Shailesh Mishra"],
        year=2023,
        venue="AISec@CCS",
        tags=["indirect-injection", "application-security"],
        techniques=["indirect injection", "data exfiltration", "plugin abuse"],
    ),
    Reference(
        id="liu2024autodan",
        kind="paper",
        title="AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned LLMs",
        authors=["Xiaogeng Liu", "Nan Xu", "Muhao Chen"],
        year=2024,
        venue="ICLR",
        tags=["jailbreak", "automated"],
        techniques=["automated jailbreak generation", "genetic algorithm"],
    ),
    Reference(
        id="zou2023universal",
        kind="paper",
        title="Universal and Transferable Adversarial Attacks on Aligned Language Models",
        authors=["Andy Zou", "Zifan Wang", "J. Zico Kolter"],
        year=2023,
        venue="arXiv",
        tags=["adversarial", "GCG", "universal"],
        techniques=["GCG suffix", "adversarial optimization"],
    ),
    Reference(
        id="wei2023jailbroken",
        kind="paper",
        title="Jailbroken: How Does LLM Safety Training Fail?",
        authors=["Alexander Wei", "Nika Haghtalab", "Jacob Steinhardt"],
        year=2023,
        venue="NeurIPS",
        tags=["jailbreak", "safety-training"],
        techniques=["competing objectives", "mismatched generalization"],
    ),
    Reference(
        id="li2023deepinception",
        kind="paper",
        title="DeepInception: Hypnotize Large Language Model to Be Jailbreaker",
        authors=["Xuan Li", "Zhanke Zhou", "Jianing Zhu"],
        year=2023,
        venue="arXiv",
        tags=["jailbreak", "inception"],
        techniques=["nested scenarios", "hypnosis framing"],
    ),
    Reference(
        id="russinovich2024skeleton",
        kind="paper",
        title="Skeleton Key: A New Type of Master Key Attack on AI Guardrails",
        authors=["Mark Russinovich"],
        year=2024,
        venue="Microsoft Security Blog",
        tags=["jailbreak", "master-key"],
        techniques=["explicit behavior update", "system prompt override"],
    ),
    Reference(
        id="anil2024manyshot",
        kind="paper",
        title="Many-shot Jailbreaking",
        authors=["Cem Anil", "Esin Durmus", "Mrinank Sharma"],
        year=2024,
        venue="Anthropic Research",
        tags=["jailbreak", "many-shot", "in-context"],
        techniques=["many-shot learning", "in-context examples"],
    ),

    # --- Adversarial NLP Papers ---
    Reference(
        id="jin2020textfooler",
        kind="paper",
        title="Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment",
        authors=["Di Jin", "Zhijing Jin", "Joey Tianyi Zhou"],
        year=2020,
        venue="AAAI",
        tags=["adversarial", "nlp", "synonym"],
        techniques=["word importance ranking", "synonym substitution"],
    ),
    Reference(
        id="li2020bertattack",
        kind="paper",
        title="BERT-ATTACK: Adversarial Attack Against BERT Using BERT",
        authors=["Linyang Li", "Ruotian Ma", "Qipeng Guo"],
        year=2020,
        venue="EMNLP",
        tags=["adversarial", "nlp", "bert"],
        techniques=["masked LM replacement", "context-aware substitution"],
    ),
    Reference(
        id="ribeiro2020checklist",
        kind="paper",
        title="Beyond Accuracy: Behavioral Testing of NLP Models with CheckList",
        authors=["Marco Tulio Ribeiro", "Tongshuang Wu", "Carlos Guestrin"],
        year=2020,
        venue="ACL",
        tags=["testing", "nlp", "behavioral"],
        techniques=["minimum functionality test", "invariance test", "directional test"],
    ),
    Reference(
        id="eger2019text",
        kind="paper",
        title="Text Processing Like Humans Do: Visually Attacking and Shielding NLP Systems",
        authors=["Steffen Eger", "Gözde Gül Şahin", "Andreas Rücklé"],
        year=2019,
        venue="NAACL",
        tags=["adversarial", "visual", "unicode"],
        techniques=["visual perturbations", "homoglyph attacks", "character manipulation"],
    ),

    # --- Standards ---
    Reference(
        id="rfc4648",
        kind="standard",
        title="The Base16, Base32, and Base64 Data Encodings",
        year=2006,
        url="https://tools.ietf.org/html/rfc4648",
        tags=["encoding", "base64", "base32"],
        techniques=["base32", "base64", "base16"],
    ),
    Reference(
        id="rfc2045",
        kind="standard",
        title="Multipurpose Internet Mail Extensions (MIME) Part One",
        year=1996,
        url="https://tools.ietf.org/html/rfc2045",
        tags=["encoding", "mime", "quoted-printable"],
        techniques=["quoted-printable"],
    ),
    Reference(
        id="unicode_confusables",
        kind="standard",
        title="Unicode Security Mechanisms (UTS #39)",
        url="https://unicode.org/reports/tr39/",
        tags=["unicode", "confusables", "homoglyph"],
        techniques=["confusable detection", "homoglyph generation"],
    ),
    Reference(
        id="unicode_bidi",
        kind="standard",
        title="Unicode Bidirectional Algorithm (UAX #9)",
        url="https://unicode.org/reports/tr9/",
        tags=["unicode", "bidi", "rtl"],
        techniques=["bidi override", "RTL text manipulation"],
    ),
]


class ReferenceIndex:
    """Query the reference index.

    Usage:
        idx = ReferenceIndex()
        papers = idx.by_kind("paper")
        jailbreak = idx.by_tag("jailbreak")
        citation = idx.get("zou2023universal").citation()
    """

    def __init__(self, refs: list[Reference] | None = None) -> None:
        self._refs = refs or list(_REFERENCES)
        self._by_id = {r.id: r for r in self._refs}

    def all(self) -> list[Reference]:
        return list(self._refs)

    def get(self, ref_id: str) -> Reference | None:
        return self._by_id.get(ref_id)

    def by_kind(self, kind: str) -> list[Reference]:
        return [r for r in self._refs if r.kind == kind]

    def by_tag(self, tag: str) -> list[Reference]:
        return [r for r in self._refs if tag in r.tags]

    def by_technique(self, technique: str) -> list[Reference]:
        """Find references mentioning a specific technique."""
        t = technique.lower()
        return [
            r for r in self._refs
            if any(t in tech.lower() for tech in r.techniques)
        ]

    def search(self, query: str) -> list[Reference]:
        """Search by title, tags, or techniques."""
        q = query.lower()
        return [
            r for r in self._refs
            if q in r.title.lower()
            or any(q in t for t in r.tags)
            or any(q in t.lower() for t in r.techniques)
        ]

    def add(self, ref: Reference) -> None:
        """Add a reference to the index."""
        self._refs.append(ref)
        self._by_id[ref.id] = ref

    def citations_for_module(self, techniques: list[str]) -> list[str]:
        """Generate citation strings for a set of techniques.

        Useful when generating the Sources section of a new module docstring.
        """
        citations = []
        seen = set()
        for tech in techniques:
            for ref in self.by_technique(tech):
                if ref.id not in seen:
                    citations.append(f"    - {ref.citation()}")
                    seen.add(ref.id)
        return citations

    def as_bibtex(self, ref_ids: list[str] | None = None) -> str:
        """Export references as BibTeX entries."""
        refs = [self._by_id[rid] for rid in ref_ids if rid in self._by_id] if ref_ids else self._refs
        entries = []
        for r in refs:
            if r.kind == "paper":
                authors_str = " and ".join(r.authors)
                entries.append(
                    f"@article{{{r.id},\n"
                    f"  title = {{{r.title}}},\n"
                    f"  author = {{{authors_str}}},\n"
                    f"  year = {{{r.year}}},\n"
                    f"  venue = {{{r.venue}}},\n"
                    f"}}"
                )
        return "\n\n".join(entries)
