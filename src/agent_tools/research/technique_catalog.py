"""
Structured catalog of known attack / encoding / obfuscation techniques.

Provides a curated inventory of techniques that can be implemented as mutators,
organized by domain. Agents use this to identify what exists, what's missing,
and what to prioritize next.

Each entry includes:
- A technique name and domain
- Whether it's already implemented in the framework
- Suggested module name and category
- References (papers, repos, standards)
- Estimated implementation complexity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TechniqueEntry:
    """A technique that could be (or already is) a mutator."""

    id: str
    name: str
    domain: str  # encoding, cipher, phonetic, linguistic, structural, etc.
    description: str
    implemented: bool = False
    module: str = ""  # Which module implements it, if any
    category: str = ""  # Which category it belongs to, if any
    complexity: str = "medium"  # low, medium, high
    references: list[str] = field(default_factory=list)
    suggested_category: str = ""
    suggested_module: str = ""
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "domain": self.domain,
            "description": self.description,
            "implemented": self.implemented,
            "module": self.module,
            "category": self.category,
            "complexity": self.complexity,
            "references": self.references,
            "suggested_category": self.suggested_category,
            "tags": self.tags,
        }


# ---------------------------------------------------------------------------
# Master catalog of techniques
# ---------------------------------------------------------------------------

_CATALOG: list[TechniqueEntry] = [
    # --- Encoding techniques ---
    TechniqueEntry(
        id="base32", name="Base32 Encoding", domain="encoding",
        description="RFC 4648 Base32 — A-Z and 2-7 alphabet",
        implemented=True, module="encoding_advanced", category="encoding_advanced",
        references=["RFC 4648"],
    ),
    TechniqueEntry(
        id="base85", name="Base85 / Ascii85 Encoding", domain="encoding",
        description="4:5 ratio encoding, more space-efficient than Base64",
        implemented=True, module="encoding_advanced", category="encoding_advanced",
        references=["Adobe PostScript Language Reference"],
    ),
    TechniqueEntry(
        id="morse", name="Morse Code", domain="encoding",
        description="ITU-T dots and dashes representation",
        implemented=True, module="encoding_advanced", category="encoding_advanced",
        references=["ITU-T International Morse Code"],
    ),
    TechniqueEntry(
        id="braille_unicode", name="Braille Unicode", domain="encoding",
        description="Unicode Braille Patterns Block (U+2800-U+28FF)",
        implemented=True, module="encoding_advanced", category="encoding_advanced",
    ),
    TechniqueEntry(
        id="quoted_printable", name="Quoted-Printable", domain="encoding",
        description="MIME =XX hex pair encoding (RFC 2045)",
        implemented=True, module="encoding_advanced", category="encoding_advanced",
        references=["RFC 2045"],
    ),
    TechniqueEntry(
        id="uuencode", name="UUencode", domain="encoding",
        description="Classic Unix 1980s encoding format",
        implemented=True, module="encoding_advanced", category="encoding_advanced",
        references=["POSIX.1"],
    ),
    TechniqueEntry(
        id="nato_phonetic", name="NATO Phonetic Alphabet", domain="encoding",
        description="Alpha-Bravo-Charlie letter spelling",
        implemented=True, module="encoding_advanced", category="encoding_advanced",
        references=["NATO/ICAO Phonetic Alphabet (1956)"],
    ),

    # --- NOT YET IMPLEMENTED: Encoding ---
    TechniqueEntry(
        id="base91", name="Base91 Encoding", domain="encoding",
        description="Higher density than Base85, uses 91 printable ASCII characters",
        implemented=False, complexity="low",
        suggested_category="encoding_advanced",
        references=["Joachim Henke — basE91"],
        tags=["encoding", "high-density"],
    ),
    TechniqueEntry(
        id="base65536", name="Base65536 Encoding", domain="encoding",
        description="Encode binary data in Unicode CJK characters (2 bytes per char)",
        implemented=False, complexity="low",
        suggested_category="encoding_advanced",
        references=["github.com/qntm/base65536"],
        tags=["encoding", "unicode", "high-density"],
    ),
    TechniqueEntry(
        id="base2048", name="Base2048 Encoding", domain="encoding",
        description="Encode data using Unicode characters that survive Twitter/SMS",
        implemented=False, complexity="low",
        suggested_category="encoding_advanced",
        references=["github.com/qntm/base2048"],
        tags=["encoding", "unicode"],
    ),
    TechniqueEntry(
        id="punycode_idn", name="Punycode IDN Homograph", domain="encoding",
        description="International domain name encoding that creates look-alike domains",
        implemented=False, complexity="medium",
        suggested_category="encoding_exploit",
        references=["RFC 3492 — Punycode"],
        tags=["encoding", "homograph"],
    ),
    TechniqueEntry(
        id="bacon_cipher", name="Bacon's Cipher", domain="cipher",
        description="Binary steganographic cipher using two typefaces (a/b encoding)",
        implemented=False, complexity="low",
        suggested_category="steganographic_encode",
        references=["Francis Bacon (1605) — De Augmentis Scientiarum"],
        tags=["cipher", "steganographic", "historical"],
    ),
    TechniqueEntry(
        id="polybius_square", name="Polybius Square", domain="cipher",
        description="5x5 grid cipher encoding letters as coordinate pairs",
        implemented=False, complexity="low",
        suggested_category="transposition_cipher",
        references=["Polybius, Histories (c. 150 BC)"],
        tags=["cipher", "historical"],
    ),
    TechniqueEntry(
        id="tap_code", name="Tap Code / Knock Code", domain="encoding",
        description="Prison communication via Polybius-based tap patterns",
        implemented=False, complexity="low",
        suggested_category="encoding_advanced",
        references=["Vietnam War POW communication"],
        tags=["encoding", "historical"],
    ),
    TechniqueEntry(
        id="semaphore", name="Flag Semaphore Encoding", domain="encoding",
        description="Naval flag position encoding using Unicode emoji flags",
        implemented=False, complexity="medium",
        suggested_category="encoding_advanced",
        tags=["encoding", "visual"],
    ),

    # --- NOT YET IMPLEMENTED: Linguistic ---
    TechniqueEntry(
        id="language_of_flowers", name="Language of Flowers (Floriography)", domain="linguistic",
        description="Encode meaning through flower names (Victorian-era steganography)",
        implemented=False, complexity="medium",
        suggested_category="steganographic_encode",
        tags=["linguistic", "steganographic"],
    ),
    TechniqueEntry(
        id="cant_slang", name="Thieves' Cant / Polari", domain="linguistic",
        description="Historical underworld slang as obfuscation layer",
        implemented=False, complexity="medium",
        suggested_category="phonetic_obfuscation",
        tags=["linguistic", "historical"],
    ),
    TechniqueEntry(
        id="text_to_music", name="Musical Notation Encoding", domain="encoding",
        description="Map characters to musical notes (ABC notation, MIDI numbers)",
        implemented=False, complexity="medium",
        suggested_category="steganographic_encode",
        references=["ABC Notation Standard"],
        tags=["encoding", "creative"],
    ),

    # --- NOT YET IMPLEMENTED: Adversarial ML ---
    TechniqueEntry(
        id="textfooler", name="TextFooler", domain="adversarial_ml",
        description="Synonym substitution attack using word importance ranking",
        implemented=False, complexity="high",
        suggested_category="adversarial_nlp",
        references=["Jin et al. (2020) — Is BERT Really Robust?"],
        tags=["adversarial", "nlp", "synonym"],
    ),
    TechniqueEntry(
        id="bert_attack", name="BERT-Attack", domain="adversarial_ml",
        description="Context-aware word replacement using BERT masked LM",
        implemented=False, complexity="high",
        suggested_category="adversarial_nlp",
        references=["Li et al. (2020) — BERT-ATTACK"],
        tags=["adversarial", "nlp", "bert"],
    ),
    TechniqueEntry(
        id="checklist", name="CheckList Perturbations", domain="adversarial_ml",
        description="Systematic linguistic capability testing (negation, taxonomy, etc.)",
        implemented=False, complexity="medium",
        suggested_category="adversarial_nlp",
        references=["Ribeiro et al. (2020) — Beyond Accuracy"],
        tags=["adversarial", "nlp", "systematic"],
    ),
    TechniqueEntry(
        id="char_swap_attack", name="Character Swap Attack", domain="adversarial_ml",
        description="Swap adjacent characters in key words to evade detection",
        implemented=False, complexity="low",
        suggested_category="obfuscation",
        references=["Eger et al. (2019) — Text Processing Like Humans Do"],
        tags=["adversarial", "typo"],
    ),

    # --- NOT YET IMPLEMENTED: Format exploitation ---
    TechniqueEntry(
        id="rtl_override_v2", name="RTL Override Sentence Reversal", domain="format",
        description="Use Unicode RTL override to visually reverse sentence display",
        implemented=False, complexity="low",
        suggested_category="control_char",
        tags=["format", "unicode", "bidi"],
    ),
    TechniqueEntry(
        id="zero_width_encoding", name="Zero-Width Character Encoding", domain="format",
        description="Encode binary data using ZWSP, ZWNJ, ZWJ as 0s and 1s",
        implemented=False, complexity="medium",
        suggested_category="steganographic_encode",
        references=["github.com/nickciolpan/Steg-of-the-Dump"],
        tags=["steganographic", "unicode", "invisible"],
    ),
    TechniqueEntry(
        id="whitespace_lang", name="Whitespace Programming Language", domain="format",
        description="Encode instructions using only spaces, tabs, and newlines",
        implemented=False, complexity="medium",
        suggested_category="steganographic_encode",
        references=["compsoc.dur.ac.uk/whitespace"],
        tags=["steganographic", "esoteric"],
    ),
]


class TechniqueCatalog:
    """Query and filter the technique catalog.

    Usage:
        catalog = TechniqueCatalog()
        unimplemented = catalog.not_implemented()
        easy_wins = catalog.not_implemented(complexity="low")
        encodings = catalog.by_domain("encoding")
    """

    def __init__(self, entries: list[TechniqueEntry] | None = None) -> None:
        self._entries = entries or list(_CATALOG)

    def all(self) -> list[TechniqueEntry]:
        return list(self._entries)

    def implemented(self) -> list[TechniqueEntry]:
        """Techniques already in the framework."""
        return [e for e in self._entries if e.implemented]

    def not_implemented(
        self, complexity: str | None = None, domain: str | None = None
    ) -> list[TechniqueEntry]:
        """Techniques not yet implemented, optionally filtered."""
        results = [e for e in self._entries if not e.implemented]
        if complexity:
            results = [e for e in results if e.complexity == complexity]
        if domain:
            results = [e for e in results if e.domain == domain]
        return results

    def by_domain(self, domain: str) -> list[TechniqueEntry]:
        """All techniques in a domain."""
        return [e for e in self._entries if e.domain == domain]

    def by_tag(self, tag: str) -> list[TechniqueEntry]:
        """All techniques with a specific tag."""
        return [e for e in self._entries if tag in e.tags]

    def domains(self) -> list[str]:
        """List all domains."""
        return sorted(set(e.domain for e in self._entries))

    def search(self, query: str) -> list[TechniqueEntry]:
        """Search by name, description, or tags."""
        q = query.lower()
        return [
            e for e in self._entries
            if q in e.name.lower()
            or q in e.description.lower()
            or any(q in t for t in e.tags)
        ]

    def add(self, entry: TechniqueEntry) -> None:
        """Add a new technique to the catalog."""
        self._entries.append(entry)

    def priority_queue(self, max_results: int = 10) -> list[TechniqueEntry]:
        """Return unimplemented techniques sorted by priority.

        Priority: low complexity first, then by number of tags (more tags = more versatile).
        """
        complexity_order = {"low": 0, "medium": 1, "high": 2}
        candidates = self.not_implemented()
        candidates.sort(key=lambda e: (complexity_order.get(e.complexity, 9), -len(e.tags)))
        return candidates[:max_results]

    def as_markdown(self, only_unimplemented: bool = False) -> str:
        """Format catalog as a Markdown table."""
        entries = self.not_implemented() if only_unimplemented else self._entries
        lines = [
            "| ID | Name | Domain | Implemented | Complexity | Suggested Category |",
            "|---|---|---|---|---|---|",
        ]
        for e in entries:
            impl = "Yes" if e.implemented else "No"
            cat = e.category or e.suggested_category or "-"
            lines.append(f"| {e.id} | {e.name} | {e.domain} | {impl} | {e.complexity} | {cat} |")
        return "\n".join(lines)
