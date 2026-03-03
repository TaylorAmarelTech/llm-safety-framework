"""
Seed Fact Pruner — normalizes, deduplicates, and quality-filters seed facts.

The raw SEED_FACTS list from ``seeds/`` is kept intact as the canonical archive.
This module produces a cleaned ``PRUNED_SEED_FACTS`` list suitable for the
Knowledge Base, removing duplicates, normalizing schema, and filtering
low-quality entries.

Usage::

    from src.scraper.seed_pruner import load_pruned_seeds, prune_report

    facts = load_pruned_seeds()          # list[dict]
    report = prune_report()              # dict with stats
"""

from __future__ import annotations

import hashlib
import re
from collections import Counter
from typing import Any


# ── Canonical schema keys ───────────────────────────────────────────────────
REQUIRED_KEYS = {"type", "jurisdiction", "title"}
PREFERRED_KEYS = {"type", "jurisdiction", "title", "summary", "source"}

# Alternate field names that map to the canonical ``summary`` key
_SUMMARY_ALIASES = ("details", "description", "content", "text", "finding", "note")

# Minimum summary length (chars) after normalization
_MIN_SUMMARY_LEN = 30

# Fact types we recognize (others are kept but flagged)
KNOWN_TYPES = {
    "fee_cap", "law", "bilateral_agreement", "case_study", "statistic",
    "advisory", "regulation_change", "contact", "court_ruling",
    "embassy_notice", "recruitment_violation", "policy_update",
    "training_material", "complaint", "penalty", "country_profile",
    "bilateral", "regulation", "rescue_operation", "statute", "statistics",
    # Legal analysis types:
    "legal_argument", "statutory_provision", "protection",
    "case_holding", "precedent_citation", "evidentiary_standard",
    # Indicator stacking matrix types:
    "indicator_action", "trafficking_pattern", "corridor_indicator_profile",
}


def _normalize_whitespace(text: str) -> str:
    """Collapse runs of whitespace to a single space and strip."""
    return re.sub(r"\s+", " ", text).strip()


def _build_summary(fact: dict) -> str:
    """Extract or synthesize a summary string from a fact dict."""
    # Direct summary
    if fact.get("summary"):
        return _normalize_whitespace(str(fact["summary"]))

    # Try alias fields
    for alias in _SUMMARY_ALIASES:
        if fact.get(alias):
            return _normalize_whitespace(str(fact[alias]))

    # Synthesize from remaining non-key fields
    extras = []
    skip = {"type", "jurisdiction", "title", "source", "corridor"}
    for k, v in fact.items():
        if k not in skip and v:
            extras.append(f"{k}: {v}")
    if extras:
        return _normalize_whitespace("; ".join(extras))

    return ""


def _dedup_key(fact: dict) -> str:
    """Produce a deduplication fingerprint from title + jurisdiction."""
    title = _normalize_whitespace(fact.get("title", "")).lower()
    jur = _normalize_whitespace(fact.get("jurisdiction", "")).lower()
    raw = f"{jur}||{title}"
    return hashlib.md5(raw.encode()).hexdigest()


def _normalize_type(raw_type: str) -> str:
    """Normalize fact type to canonical form."""
    t = raw_type.strip().lower().replace("-", "_").replace(" ", "_")
    # Merge near-duplicates
    if t == "statistics":
        return "statistic"
    if t == "bilateral":
        return "bilateral_agreement"
    if t in ("regulation", "regulatory_change"):
        return "regulation_change"
    if t == "statute":
        return "law"
    if t == "enforcement_action":
        return "penalty"
    if t in ("holding", "decision"):
        return "case_holding"
    if t in ("citation", "case_citation"):
        return "precedent_citation"
    if t in ("victim_protection", "safe_harbor", "remedy"):
        return "protection"
    if t in ("evidence", "proof_standard"):
        return "evidentiary_standard"
    if t == "legal_theory":
        return "legal_argument"
    if t in ("provision", "section"):
        return "statutory_provision"
    if t == "settlement_precedent":
        return "precedent_citation"
    if t == "investigative_standard":
        return "evidentiary_standard"
    if t == "historical_fact":
        return "case_study"
    return t


def normalize_fact(fact: dict) -> dict:
    """Return a new dict with canonical keys and normalized values."""
    out: dict[str, Any] = {}
    out["type"] = _normalize_type(fact.get("type", "case_study"))
    out["jurisdiction"] = _normalize_whitespace(fact.get("jurisdiction", "Unknown"))
    out["title"] = _normalize_whitespace(fact.get("title", ""))
    out["summary"] = _build_summary(fact)
    out["source"] = _normalize_whitespace(fact.get("source", ""))

    # Preserve important metadata fields at top level for querying/filtering
    _TOP_LEVEL_KEYS = {
        "corridor", "court", "year", "organization", "contact_type",
        "offense", "amount", "law", "indicator", "sector", "treaty",
    }
    skip = {"type", "jurisdiction", "title", "summary", "source"} | set(_SUMMARY_ALIASES)
    extras = {}
    for k, v in fact.items():
        if k in skip or not v:
            continue
        if k in _TOP_LEVEL_KEYS:
            out[k] = v
        else:
            extras[k] = v
    if extras:
        out["_extra"] = extras

    return out


def prune(raw_facts: list[dict]) -> tuple[list[dict], dict]:
    """
    Normalize, deduplicate, and quality-filter a list of seed facts.

    Returns:
        (pruned_facts, report_dict)
    """
    normalized = [normalize_fact(f) for f in raw_facts]

    # --- Deduplication by title+jurisdiction ---
    seen: set[str] = set()
    deduped: list[dict] = []
    dup_count = 0
    for fact in normalized:
        key = _dedup_key(fact)
        if key in seen:
            dup_count += 1
            continue
        seen.add(key)
        deduped.append(fact)

    # --- Quality filter ---
    kept: list[dict] = []
    dropped_no_title = 0
    dropped_short_summary = 0
    for fact in deduped:
        if not fact["title"]:
            dropped_no_title += 1
            continue
        if len(fact["summary"]) < _MIN_SUMMARY_LEN:
            dropped_short_summary += 1
            continue
        kept.append(fact)

    # --- Report ---
    type_dist = Counter(f["type"] for f in kept)
    jur_count = len(set(f["jurisdiction"] for f in kept))
    no_source = sum(1 for f in kept if not f["source"])

    report = {
        "input_count": len(raw_facts),
        "after_normalize": len(normalized),
        "duplicates_removed": dup_count,
        "dropped_no_title": dropped_no_title,
        "dropped_short_summary": dropped_short_summary,
        "output_count": len(kept),
        "reduction_pct": round(100 * (1 - len(kept) / len(raw_facts)), 1) if raw_facts else 0,
        "jurisdictions": jur_count,
        "type_distribution": dict(type_dist.most_common()),
        "entries_without_source": no_source,
    }

    return kept, report


def load_pruned_seeds() -> list[dict]:
    """Load and return pruned seed facts (lazy import to avoid circular deps)."""
    from src.scraper.seeds import SEED_FACTS
    pruned, _ = prune(SEED_FACTS)
    return pruned


def prune_report() -> dict:
    """Return a detailed report on pruning results."""
    from src.scraper.seeds import SEED_FACTS
    _, report = prune(SEED_FACTS)
    return report


if __name__ == "__main__":
    report = prune_report()
    print(f"Input:   {report['input_count']}")
    print(f"Output:  {report['output_count']}")
    print(f"Removed: {report['input_count'] - report['output_count']} "
          f"({report['reduction_pct']}%)")
    print(f"  Duplicates:     {report['duplicates_removed']}")
    print(f"  No title:       {report['dropped_no_title']}")
    print(f"  Short summary:  {report['dropped_short_summary']}")
    print(f"Jurisdictions: {report['jurisdictions']}")
    print(f"No source:     {report['entries_without_source']}")
    print(f"\nType distribution:")
    for t, c in report["type_distribution"].items():
        print(f"  {t}: {c}")
