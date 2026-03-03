"""
Knowledge Base for the Document Intelligence Agent.

Consolidates extracted facts from all documents into a queryable
knowledge base. Provides context to the wizard prompt generator.
"""

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


from .sources import TIER_LABELS


class KnowledgeBase:
    """Structured knowledge base built from extracted document facts."""

    CATEGORIES = [
        "fee_cap", "law", "bilateral_agreement", "case_study",
        "statistic", "advisory", "regulation_change", "contact",
        "court_ruling", "embassy_notice", "recruitment_violation",
        "policy_update", "training_material", "complaint", "penalty",
        # Legal analysis types:
        "legal_argument", "statutory_provision", "protection",
        "case_holding", "precedent_citation", "evidentiary_standard",
        # Indicator stacking matrix types:
        "indicator_action", "trafficking_pattern", "corridor_indicator_profile",
    ]

    # Tier → base reliability weight (higher tier = more authoritative)
    _TIER_WEIGHTS = {1: 1.0, 2: 0.9, 3: 0.9, 4: 0.85, 5: 0.75, 6: 0.95, 7: 0.8}

    def __init__(self, data_dir: str = "data/scraper"):
        self.data_dir = Path(data_dir)
        self.kb_file = self.data_dir / "knowledge_base.json"
        self.extractions_dir = self.data_dir / "extractions"
        self._facts: List[Dict[str, Any]] = []
        self._meta: Dict[str, Any] = {}
        self._load()

    # -- persistence -----------------------------------------------------------

    def _load(self) -> None:
        if self.kb_file.exists():
            data = json.loads(self.kb_file.read_text(encoding="utf-8"))
            self._facts = data.get("facts", [])
            self._meta = data.get("meta", {})
        else:
            self._facts = []
            self._meta = {"last_rebuilt": None, "total_docs": 0}

    def _save(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.kb_file.write_text(
            json.dumps({
                "facts": self._facts,
                "meta": self._meta,
            }, indent=2, default=str),
            encoding="utf-8",
        )

    # -- rebuild from extractions ----------------------------------------------

    def rebuild(self) -> Dict[str, int]:
        """Re-merge all extraction files into the knowledge base.

        Adds temporal tracking, reliability scoring, and cross-references.
        Returns counts by fact category.
        """
        self._facts = []
        seen: Dict[str, int] = {}  # dedup key → fact index
        doc_count = 0
        now = datetime.now(tz=timezone.utc).isoformat()

        if self.extractions_dir.exists():
            for fp in self.extractions_dir.glob("*.json"):
                try:
                    data = json.loads(fp.read_text(encoding="utf-8"))
                    doc_count += 1
                    confidence_scores = data.get("confidence_scores", {})
                    for fact_idx, fact in enumerate(data.get("facts", [])):
                        key = json.dumps(
                            {k: v for k, v in fact.items() if not k.startswith("_")},
                            sort_keys=True, default=str,
                        )
                        if key in seen:
                            # Duplicate → update _last_confirmed
                            existing = self._facts[seen[key]]
                            existing["_last_confirmed"] = now
                        else:
                            fact["_source_doc"] = data.get("document_id", fp.stem)
                            fact["_first_seen"] = data.get("extracted_at", now)
                            fact["_last_confirmed"] = now
                            # Compute reliability: tier_weight * extraction_confidence
                            conf = confidence_scores.get(str(fact_idx), 0.5)
                            fact["_confidence"] = float(conf)
                            seen[key] = len(self._facts)
                            self._facts.append(fact)
                except Exception:
                    continue

        # Build cross-references between related facts
        self._build_cross_references()

        self._meta = {
            "last_rebuilt": now,
            "total_docs": doc_count,
        }
        self._save()

        # Return category counts
        counts: Dict[str, int] = defaultdict(int)
        for f in self._facts:
            counts[f.get("type", "unknown")] += 1
        return dict(counts)

    def _build_cross_references(self) -> None:
        """Link facts that share entities (jurisdiction, law, corridor)."""
        # Build inverted index: entity_key → set of fact indices
        entity_to_facts: Dict[str, set] = defaultdict(set)
        link_fields = ("jurisdiction", "corridor", "law", "agency", "court",
                       "statute", "cited_case", "citing_case")

        for idx, fact in enumerate(self._facts):
            for field in link_fields:
                val = fact.get(field)
                if val:
                    entity_to_facts[f"{field}:{str(val).lower()}"].add(idx)

        # For each fact, find related facts (sharing at least one entity)
        for idx, fact in enumerate(self._facts):
            related: set = set()
            for field in link_fields:
                val = fact.get(field)
                if val:
                    siblings = entity_to_facts.get(f"{field}:{str(val).lower()}", set())
                    related.update(siblings)
            related.discard(idx)  # don't link to self
            if related:
                fact["_related_facts"] = sorted(related)

    def merge_extraction(
        self,
        facts: List[Dict],
        document_id: str,
        confidence_scores: Optional[Dict[int, float]] = None,
    ) -> int:
        """Incrementally merge facts from a new extraction.

        Returns the number of NEW facts added. Duplicates update _last_confirmed.
        """
        now = datetime.now(tz=timezone.utc).isoformat()
        conf_map = confidence_scores or {}

        # Build dedup map: key → index
        existing_keys: Dict[str, int] = {}
        for idx, f in enumerate(self._facts):
            k = json.dumps(
                {k: v for k, v in f.items() if not k.startswith("_")},
                sort_keys=True, default=str,
            )
            existing_keys[k] = idx

        added = 0
        for fact_idx, fact in enumerate(facts):
            key = json.dumps(
                {k: v for k, v in fact.items() if not k.startswith("_")},
                sort_keys=True, default=str,
            )
            if key in existing_keys:
                # Duplicate → update last_confirmed timestamp
                self._facts[existing_keys[key]]["_last_confirmed"] = now
            else:
                fact["_source_doc"] = document_id
                fact["_first_seen"] = now
                fact["_last_confirmed"] = now
                fact["_confidence"] = float(conf_map.get(fact_idx, 0.5))
                existing_keys[key] = len(self._facts)
                self._facts.append(fact)
                added += 1

        if added:
            self._meta["total_docs"] = self._meta.get("total_docs", 0)
            self._save()

        return added

    # -- querying --------------------------------------------------------------

    def query(
        self,
        category: Optional[str] = None,
        jurisdiction: Optional[str] = None,
        corridor: Optional[str] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """Query facts with optional filters."""
        results = self._facts

        if category:
            results = [f for f in results if f.get("type") == category]
        if jurisdiction:
            jur = jurisdiction.upper()
            results = [
                f for f in results
                if jur in str(f.get("jurisdiction", "")).upper()
            ]
        if corridor:
            cor = corridor.upper()
            results = [
                f for f in results
                if cor in str(f.get("corridor", "")).upper()
            ]

        return results[:limit]

    def stats(self) -> Dict[str, Any]:
        """Return knowledge base statistics."""
        counts: Dict[str, int] = defaultdict(int)
        jurisdictions: set = set()
        corridors: set = set()
        avg_conf = 0.0

        for f in self._facts:
            counts[f.get("type", "unknown")] += 1
            if f.get("jurisdiction"):
                jurisdictions.add(f["jurisdiction"])
            if f.get("corridor"):
                corridors.add(f["corridor"])
            avg_conf += f.get("_confidence", 0.5)

        total = len(self._facts)
        return {
            "total_facts": total,
            "by_category": dict(counts),
            "jurisdictions": sorted(jurisdictions),
            "corridors": sorted(corridors),
            "total_docs": self._meta.get("total_docs", 0),
            "last_rebuilt": self._meta.get("last_rebuilt"),
            "avg_confidence": round(avg_conf / total, 3) if total else 0.0,
        }

    # -- advanced queries ------------------------------------------------------

    def query_timeline(
        self,
        category: Optional[str] = None,
        corridor: Optional[str] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """Return facts sorted by _first_seen (newest first)."""
        results = self.query(category=category, corridor=corridor, limit=9999)
        results.sort(key=lambda f: f.get("_first_seen", ""), reverse=True)
        return results[:limit]

    def get_stale_facts(self, days: int = 90) -> List[Dict[str, Any]]:
        """Return facts whose _last_confirmed is older than *days*."""
        from datetime import timedelta
        cutoff = (datetime.now(tz=timezone.utc) - timedelta(days=days)).isoformat()
        return [
            f for f in self._facts
            if f.get("_last_confirmed", "9999") < cutoff
        ]

    def query_cross_referenced(self, fact_index: int) -> List[Dict[str, Any]]:
        """Return facts cross-referenced with the fact at *fact_index*."""
        if fact_index < 0 or fact_index >= len(self._facts):
            return []
        related_ids = self._facts[fact_index].get("_related_facts", [])
        return [self._facts[i] for i in related_ids if i < len(self._facts)]

    def query_entities(self) -> List[Dict[str, Any]]:
        """Aggregate all entities referenced across facts."""
        entity_counts: Dict[str, Dict] = {}
        link_fields = ("jurisdiction", "corridor", "law", "agency", "court",
                       "statute", "cited_case", "citing_case")
        for fact in self._facts:
            for field in link_fields:
                val = fact.get(field)
                if val:
                    key = f"{field}:{str(val).lower()}"
                    if key not in entity_counts:
                        entity_counts[key] = {"name": val, "type": field, "mentions": 0}
                    entity_counts[key]["mentions"] += 1
        results = sorted(entity_counts.values(), key=lambda x: x["mentions"], reverse=True)
        return results

    # -- context for prompt generation -----------------------------------------

    def get_context_for_generation(
        self,
        corridor: Optional[str] = None,
        category: Optional[str] = None,
        max_tokens_estimate: int = 2000,
        min_confidence: float = 0.0,
        include_citations: bool = False,
    ) -> str:
        """Format KB facts as context for the wizard generator LLM.

        Args:
            corridor: Filter to a specific migration corridor.
            category: Filter to a specific fact type.
            max_tokens_estimate: Rough token budget for the output.
            min_confidence: Exclude facts below this confidence threshold.
            include_citations: Append source doc + paragraph info to each fact.

        Returns a human-readable block suitable for appending to a system prompt.
        """
        facts = self.query(category=category, corridor=corridor, limit=200)

        # Apply confidence filter
        if min_confidence > 0:
            facts = [f for f in facts if f.get("_confidence", 0.5) >= min_confidence]

        if not facts:
            return ""

        lines = ["CURRENT KNOWLEDGE BASE (from recently scraped authoritative sources):", ""]

        # Group by type
        by_type: Dict[str, List[Dict]] = defaultdict(list)
        for f in facts:
            by_type[f.get("type", "other")].append(f)

        char_budget = max_tokens_estimate * 4  # rough chars-per-token
        chars_used = 0

        for ftype, items in by_type.items():
            header = f"## {ftype.replace('_', ' ').title()} ({len(items)} facts)"
            lines.append(header)
            chars_used += len(header)

            for item in items[:20]:  # cap per category
                summary = self._fact_one_liner(item)
                if include_citations and item.get("_source_doc"):
                    summary += f" [source: {item['_source_doc']}]"
                if chars_used + len(summary) > char_budget:
                    break
                lines.append(f"  - {summary}")
                chars_used += len(summary)

            lines.append("")

        return "\n".join(lines)

    def _fact_one_liner(self, fact: Dict) -> str:
        """Format a single fact as a concise one-liner."""
        ftype = fact.get("type", "")
        parts = []

        if ftype == "fee_cap":
            parts = [
                fact.get("jurisdiction", ""),
                fact.get("amount", ""),
                fact.get("law", ""),
            ]
        elif ftype == "law":
            parts = [
                fact.get("jurisdiction", ""),
                fact.get("name", fact.get("law", "")),
                fact.get("details", fact.get("key_provisions", "")),
            ]
        elif ftype == "bilateral_agreement":
            parties = fact.get("parties", [])
            parts = [
                " - ".join(parties) if isinstance(parties, list) else str(parties),
                fact.get("date", ""),
                fact.get("details", ""),
            ]
        elif ftype == "case_study":
            parts = [
                fact.get("corridor", ""),
                fact.get("exploitation_type", ""),
                fact.get("summary", ""),
            ]
        elif ftype == "statistic":
            parts = [
                fact.get("metric", ""),
                str(fact.get("value", "")),
                fact.get("year", ""),
            ]
        elif ftype == "advisory":
            parts = [
                fact.get("agency", ""),
                fact.get("title", ""),
                fact.get("date", ""),
            ]
        elif ftype == "regulation_change":
            parts = [
                fact.get("jurisdiction", ""),
                fact.get("agency", ""),
                fact.get("description", ""),
            ]
        elif ftype == "contact":
            parts = [
                fact.get("organization", ""),
                fact.get("type", ""),
                fact.get("details", ""),
            ]
        elif ftype == "court_ruling":
            parts = [
                fact.get("court", ""),
                fact.get("case_no", ""),
                fact.get("date", ""),
                fact.get("ruling", ""),
            ]
        elif ftype == "embassy_notice":
            parts = [
                fact.get("embassy", ""),
                fact.get("date", ""),
                fact.get("title", ""),
            ]
        elif ftype == "recruitment_violation":
            parts = [
                fact.get("agency", ""),
                fact.get("violation_type", ""),
                fact.get("penalty", ""),
                fact.get("jurisdiction", ""),
            ]
        elif ftype == "policy_update":
            parts = [
                fact.get("jurisdiction", ""),
                fact.get("agency", ""),
                fact.get("description", ""),
                fact.get("effective_date", ""),
            ]
        elif ftype == "training_material":
            parts = [
                fact.get("title", ""),
                fact.get("audience", ""),
                fact.get("topics", ""),
            ]
        elif ftype == "complaint":
            parts = [
                fact.get("complainant_type", ""),
                fact.get("jurisdiction", ""),
                fact.get("issue", ""),
                fact.get("outcome", ""),
            ]
        elif ftype == "penalty":
            parts = [
                fact.get("entity", ""),
                fact.get("penalty_type", ""),
                fact.get("amount", ""),
                fact.get("jurisdiction", ""),
            ]
        elif ftype == "legal_argument":
            parts = [
                fact.get("jurisdiction", ""),
                fact.get("case_ref", ""),
                fact.get("theory", ""),
                fact.get("outcome", ""),
                fact.get("summary", ""),
            ]
        elif ftype == "statutory_provision":
            parts = [
                fact.get("jurisdiction", ""),
                fact.get("statute", ""),
                fact.get("section", ""),
                fact.get("summary", fact.get("elements", "")),
            ]
        elif ftype == "protection":
            parts = [
                fact.get("jurisdiction", ""),
                fact.get("protection_type", ""),
                fact.get("eligibility", ""),
                fact.get("summary", fact.get("mechanism", "")),
            ]
        elif ftype == "case_holding":
            parts = [
                fact.get("court", ""),
                fact.get("case_no", fact.get("case_name", "")),
                fact.get("date", ""),
                fact.get("holding", ""),
            ]
        elif ftype == "precedent_citation":
            parts = [
                fact.get("citing_case", ""),
                "cites",
                fact.get("cited_case", ""),
                fact.get("proposition", ""),
            ]
        elif ftype == "evidentiary_standard":
            parts = [
                fact.get("jurisdiction", ""),
                fact.get("element", ""),
                fact.get("evidence_type", ""),
                fact.get("summary", ""),
            ]
        elif ftype == "indicator_action":
            parts = [
                fact.get("phase", ""),
                fact.get("action", ""),
                fact.get("red_flag_when", ""),
            ]
        elif ftype == "trafficking_pattern":
            parts = [
                fact.get("name", ""),
                fact.get("risk_level", ""),
                fact.get("description", ""),
            ]
        elif ftype == "corridor_indicator_profile":
            parts = [
                fact.get("corridor", ""),
                ", ".join(fact.get("primary_sectors", [])),
                fact.get("summary", ""),
            ]
        else:
            parts = [str(v) for k, v in fact.items() if not k.startswith("_") and k != "type"]

        return " | ".join(p for p in parts if p)
