"""
LLM-based fact extractor for the Document Intelligence Agent.

Sends document text to an LLM and receives structured facts:
fee caps, laws, bilateral agreements, case studies, statistics, advisories.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..api_client import UnifiedAPIClient


FACT_TYPES = [
    "fee_cap", "law", "bilateral_agreement", "case_study",
    "statistic", "advisory", "regulation_change", "contact",
    "court_ruling", "embassy_notice", "recruitment_violation",
    "policy_update", "training_material", "complaint", "penalty",
    # Legal analysis types:
    "legal_argument", "statutory_provision", "protection",
    "case_holding", "precedent_citation", "evidentiary_standard",
]


# ── Extraction strategies ─────────────────────────────────────────────────
class ExtractionStrategy:
    DEFAULT = "default"
    LEGAL_CASE = "legal_case"
    LEGISLATION = "legislation"
    REPORT = "report"

EXTRACTION_STRATEGIES = [
    ExtractionStrategy.DEFAULT,
    ExtractionStrategy.LEGAL_CASE,
    ExtractionStrategy.LEGISLATION,
    ExtractionStrategy.REPORT,
]


@dataclass
class ExtractionResult:
    """Structured facts extracted from a single document."""

    document_id: str
    facts: List[Dict[str, Any]]
    summary: str
    relevance_score: float
    extracted_at: str = ""
    confidence_scores: Dict[int, float] = field(default_factory=dict)  # fact_index → 0.0-1.0
    citations: List[Dict[str, Any]] = field(default_factory=list)  # {fact_index, paragraph, page, section}
    entities: List[Dict[str, Any]] = field(default_factory=list)  # {name, type, mentions}


EXTRACTION_SYSTEM_PROMPT = """You are a legal research assistant specializing in migrant worker protection and anti-trafficking law. Your task is to extract STRUCTURED FACTS from a document.

Focus on these fact types:
1. **fee_cap** — legal caps on recruitment/placement fees (jurisdiction, amount, law reference)
2. **law** — specific laws, ordinances, or regulations (jurisdiction, name, key provisions)
3. **bilateral_agreement** — bilateral labour agreements between countries (parties, date, provisions)
4. **case_study** — documented trafficking or exploitation cases (corridor, exploitation_type, summary)
5. **statistic** — quantitative data (metric, value, year, source)
6. **advisory** — government advisories, warnings, policy changes (agency, title, date, summary)
7. **regulation_change** — new or amended regulations (jurisdiction, agency, description, effective_date)
8. **contact** — helpline, embassy, shelter contact info (organization, type, details)
9. **court_ruling** — court decisions on trafficking/labour cases (court, case_no, date, ruling, significance)
10. **embassy_notice** — consular/embassy announcements for nationals abroad (embassy, date, title, summary)
11. **recruitment_violation** — documented agency violations (agency, jurisdiction, violation_type, penalty, date)
12. **policy_update** — broader policy changes affecting migrant workers (jurisdiction, agency, description, effective_date)
13. **training_material** — training/educational resources for workers or officials (title, audience, topics)
14. **complaint** — formal complaints or grievances filed (complainant_type, jurisdiction, issue, outcome)
15. **penalty** — fines, sanctions, blacklisting actions (entity, penalty_type, amount, jurisdiction, date)

CORRIDORS OF INTEREST (prioritised):
- Philippines → Saudi Arabia, UAE, Qatar, Hong Kong, Singapore, Kuwait, Japan, Korea
- Indonesia → Singapore, Malaysia, Saudi Arabia, Hong Kong, Taiwan
- Nepal → Qatar, Saudi Arabia, UAE, Malaysia, Korea
- Bangladesh → Malaysia, Saudi Arabia, Qatar, UAE
- Myanmar → Thailand, Malaysia, Singapore
- Ethiopia → Lebanon, Saudi Arabia, UAE
(Also include any other corridor data found.)

For EACH fact, include:
- **confidence**: 0.0-1.0 score for how certain the extraction is
- **paragraph**: the paragraph number (¶N) where this fact was found

Also extract ENTITIES — named organisations, laws, jurisdictions, agencies, and people mentioned:
- **name**: entity name
- **type**: one of [organisation, law, jurisdiction, agency, person, corridor]
- **mentions**: number of times mentioned

Return ONLY valid JSON with this structure:
{
  "facts": [
    {"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4,630", "law": "EO Cap. 57", "details": "...", "confidence": 0.95, "paragraph": 3},
    {"type": "court_ruling", "court": "HK Labour Tribunal", "case_no": "...", "date": "...", "ruling": "...", "significance": "...", "confidence": 0.8, "paragraph": 7},
    ...
  ],
  "entities": [
    {"name": "Employment Ordinance Cap. 57", "type": "law", "mentions": 4},
    {"name": "Hong Kong", "type": "jurisdiction", "mentions": 12},
    ...
  ],
  "summary": "Brief 2-3 sentence summary of the document's relevance",
  "relevance_score": 0.85
}

relevance_score: 0.0 (completely irrelevant) to 1.0 (directly about migrant worker trafficking in target corridors).
If the document has NO relevant facts, return {"facts": [], "entities": [], "summary": "Not relevant", "relevance_score": 0.0}."""


# ── Specialized prompt: Court decisions & case law ─────────────────────────
LEGAL_CASE_EXTRACTION_PROMPT = """You are a legal research assistant specializing in anti-trafficking case law analysis. Your task is to extract DETAILED STRUCTURED FACTS from a court decision, legal opinion, or case report.

Extract ALL of the following fact types:

1. **case_holding** — The court's decision and reasoning.
   Fields: court, case_no, case_name, date, jurisdiction, holding (what the court decided),
   reasoning (WHY the court decided this way), significance (precedential value),
   distinguishing_facts (what makes this case unique), disposition (affirmed/reversed/remanded).

2. **legal_argument** — Legal theories, arguments raised by parties, standards applied.
   Fields: jurisdiction, case_ref, theory (theory of liability or defense),
   standard (legal standard applied e.g. "preponderance", "beyond reasonable doubt"),
   party (prosecution/plaintiff/defense), outcome (accepted/rejected by court),
   summary (detailed explanation of the argument and its treatment).

3. **precedent_citation** — When the case cites another case for a legal proposition.
   Fields: citing_case, cited_case, jurisdiction, proposition (the legal point cited for),
   treatment (followed/distinguished/overruled/discussed), summary.

4. **evidentiary_standard** — How trafficking/forced labor elements were proven.
   Fields: jurisdiction, case_ref, element (which element of the offense),
   evidence_type (testimony/documentary/financial/expert/circumstantial),
   description (how this evidence established the element),
   sufficiency (whether court found it sufficient), summary.

5. **statutory_provision** — Statutes applied or analyzed in the case.
   Fields: jurisdiction, statute (full citation e.g. "18 USC 1589"),
   section (specific subsection), elements (element-by-element breakdown),
   interpretation (how the court interpreted it), summary.

6. **protection** — Victim protections, remedies ordered, or relief provisions applied.
   Fields: jurisdiction, protection_type (T-visa/restitution/back_pay/safe_harbor/civil_damages),
   eligibility (who qualifies), mechanism (how the protection is obtained),
   amount (dollar amount if applicable), case_ref, summary.

7. **penalty** — Sentences imposed, fines, restitution amounts ordered.
   Fields: entity (defendant name), penalty_type (imprisonment/fine/restitution/probation/forfeiture),
   amount (years/dollars), jurisdiction, date, case_ref, summary.

8. **court_ruling** — General case facts and outcome (for cases where above types don't fit).
   Fields: court, case_no, date, ruling, significance.

Also extract standard types where found: law, case_study, statistic, advisory, regulation_change, recruitment_violation, complaint, policy_update.

For EACH fact, include:
- **confidence**: 0.0-1.0 for extraction certainty
- **paragraph**: paragraph number (¶N) where found

Also extract ENTITIES (organisations, laws, courts, jurisdictions, people):
- **name**, **type** (one of: organisation, law, jurisdiction, agency, person, court, statute), **mentions**

Return ONLY valid JSON:
{
  "facts": [...],
  "entities": [...],
  "summary": "Brief 2-3 sentence summary of the case and its significance",
  "relevance_score": 0.85
}"""


# ── Specialized prompt: Legislation & statutes ─────────────────────────────
LEGISLATION_EXTRACTION_PROMPT = """You are a legal research assistant specializing in anti-trafficking and migrant worker protection legislation. Your task is to extract DETAILED STRUCTURED FACTS from a statute, law, regulation, or legislative document.

Extract ALL of the following fact types:

1. **statutory_provision** — Specific sections and subsections of the law.
   Fields: jurisdiction, statute (full citation), section (specific section/article number),
   elements (element-by-element breakdown of what the provision requires/prohibits),
   definitions (key terms defined in this section), thresholds (numeric thresholds, time limits),
   penalties_referenced (penalties this section triggers), summary.

2. **protection** — Victim protections, safe harbor provisions, immigration relief, compensation.
   Fields: jurisdiction, protection_type (visa_relief/safe_harbor/witness_protection/compensation/
   civil_cause_of_action/labor_rights/non_punishment), eligibility (who qualifies),
   mechanism (how to access the protection), statute (law reference),
   limitations (time limits, conditions), summary.

3. **penalty** — Criminal and civil penalties defined by the statute.
   Fields: entity (offense type), penalty_type (imprisonment/fine/restitution/forfeiture/
   civil_liability/debarment), amount (years/dollar amounts), jurisdiction,
   mandatory_minimum (yes/no + amount), enhancements (aggravating factors),
   statute (section reference), summary.

4. **law** — Overview of the law itself.
   Fields: jurisdiction, name (official name), year (enactment year),
   key_provisions (major provisions summary), amendments (significant amendments),
   implementing_agency (enforcement body), source.

5. **regulation_change** — Amendments, new regulations, or reformed provisions.
   Fields: jurisdiction, agency, description, effective_date, prior_law (what it replaced/amended),
   impact (practical effect of the change), summary.

6. **legal_argument** — Legislative intent, committee findings, interpretive guidance.
   Fields: jurisdiction, theory (legislative purpose/policy rationale),
   standard (legal standard established), summary.

Also extract: fee_cap, bilateral_agreement, contact (enforcement bodies), statistic (prevalence data cited in preambles).

For EACH fact: **confidence** (0.0-1.0) and **paragraph** (¶N).
Extract ENTITIES: name, type (law, jurisdiction, agency, organisation, statute), mentions.

Return ONLY valid JSON:
{
  "facts": [...],
  "entities": [...],
  "summary": "Brief 2-3 sentence summary of the legislation's scope and significance",
  "relevance_score": 0.85
}"""


# ── Specialized prompt: Reports (NGO/IGO/research) ────────────────────────
REPORT_EXTRACTION_PROMPT = """You are a research assistant specializing in migrant worker protection and anti-trafficking reports. Your task is to extract DETAILED STRUCTURED FACTS from an NGO, IGO, or research report.

Extract ALL of the following fact types:

1. **statistic** — Quantitative data with context.
   Fields: metric (what is measured), value (number/percentage), year,
   source (original data source), methodology (survey/estimate/census/administrative),
   confidence_interval (if provided), jurisdiction, corridor, summary.

2. **case_study** — Documented trafficking or exploitation cases.
   Fields: corridor (origin-destination), exploitation_type (forced_labor/debt_bondage/etc),
   sector (domestic_work/construction/agriculture/etc), victim_count,
   perpetrator_type (recruiter/employer/network), outcome (prosecution/rescue/ongoing),
   jurisdiction, summary, source.

3. **advisory** — Recommendations, warnings, policy proposals.
   Fields: agency (issuing organization), title, date, target_audience,
   recommendation_type (policy/legislative/enforcement/awareness),
   urgency (routine/important/urgent), summary.

4. **recruitment_violation** — Documented agency violations and patterns.
   Fields: agency (recruitment company), jurisdiction, violation_type
   (fee_overcharging/contract_substitution/deception/document_confiscation),
   scale (individual/pattern/systematic), penalty (if any), date, summary.

5. **protection** — Protection mechanisms described or recommended.
   Fields: jurisdiction, protection_type, eligibility, mechanism,
   effectiveness (if evaluated), gaps (identified shortcomings), summary.

6. **legal_argument** — Policy arguments, theoretical frameworks, recommendations.
   Fields: jurisdiction, theory (policy rationale/framework proposed),
   evidence_base (what evidence supports this argument), summary.

Also extract: law, regulation_change, contact (hotlines/shelters), complaint, penalty, policy_update, bilateral_agreement, fee_cap, training_material.

For EACH fact: **confidence** (0.0-1.0) and **paragraph** (¶N).
Extract ENTITIES: name, type (organisation, law, jurisdiction, agency, person, corridor), mentions.

Return ONLY valid JSON:
{
  "facts": [...],
  "entities": [...],
  "summary": "Brief 2-3 sentence summary of the report's key findings",
  "relevance_score": 0.85
}"""


# ── Strategy → prompt mapping ──────────────────────────────────────────────
_STRATEGY_PROMPTS = {
    ExtractionStrategy.DEFAULT: EXTRACTION_SYSTEM_PROMPT,
    ExtractionStrategy.LEGAL_CASE: LEGAL_CASE_EXTRACTION_PROMPT,
    ExtractionStrategy.LEGISLATION: LEGISLATION_EXTRACTION_PROMPT,
    ExtractionStrategy.REPORT: REPORT_EXTRACTION_PROMPT,
}

# Source tiers that default to specific strategies
_TIER_STRATEGY_MAP = {
    6: ExtractionStrategy.LEGAL_CASE,  # Courts & Legal
}

# Heuristic keywords for auto-detection
_LEGAL_CASE_KEYWORDS = {"HELD:", "OPINION", "ORDER OF THE COURT", "JUDGMENT", "DISSENT",
                         "APPELLANT", "APPELLEE", "PETITIONER", "RESPONDENT", " v. ", " vs. "}
_LEGISLATION_KEYWORDS = {"Section ", "Article ", "enacted", "shall be", "subsection",
                          "An Act to", "Be it enacted", "CHAPTER ", "PART "}
_REPORT_KEYWORDS = {"Executive Summary", "Recommendations", "Methodology", "Key Findings",
                     "Table of Contents", "Acknowledgements", "This report"}


class FactExtractor:
    """Extracts structured facts from documents using an LLM."""

    MAX_CHUNK_WORDS = 4000

    def __init__(self, data_dir: str = "data/scraper"):
        self.data_dir = Path(data_dir)
        self.extractions_dir = self.data_dir / "extractions"
        self.extractions_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def select_strategy(
        source_id: Optional[str] = None,
        source_tier: Optional[int] = None,
        text_sample: str = "",
    ) -> str:
        """Auto-detect the best extraction strategy for a document.

        Priority: source tier mapping → text heuristics → default.
        """
        # 1. Tier-based mapping (if we know the source)
        if source_tier and source_tier in _TIER_STRATEGY_MAP:
            return _TIER_STRATEGY_MAP[source_tier]

        # 2. Text heuristics (check first 2000 chars for speed)
        sample = text_sample[:2000]
        legal_hits = sum(1 for kw in _LEGAL_CASE_KEYWORDS if kw in sample)
        legis_hits = sum(1 for kw in _LEGISLATION_KEYWORDS if kw in sample)
        report_hits = sum(1 for kw in _REPORT_KEYWORDS if kw in sample)

        if legal_hits >= 2:
            return ExtractionStrategy.LEGAL_CASE
        if legis_hits >= 2:
            return ExtractionStrategy.LEGISLATION
        if report_hits >= 2:
            return ExtractionStrategy.REPORT

        return ExtractionStrategy.DEFAULT

    async def extract(
        self,
        document_text: str,
        document_id: str,
        client: UnifiedAPIClient,
        model_id: str,
        extraction_strategy: Optional[str] = None,
        source_id: Optional[str] = None,
        source_tier: Optional[int] = None,
    ) -> ExtractionResult:
        """Extract facts from document text using an LLM.

        Long documents are chunked and processed in parts, then merged.
        Adds paragraph markers so the LLM can reference exact locations.

        Args:
            extraction_strategy: Override auto-detection (default/legal_case/legislation/report).
            source_id: Source ID for tier-based auto-detection.
            source_tier: Source tier for strategy selection.
        """
        from datetime import datetime, timezone

        # Select extraction strategy
        strategy = extraction_strategy or self.select_strategy(
            source_id=source_id,
            source_tier=source_tier,
            text_sample=document_text,
        )
        system_prompt = _STRATEGY_PROMPTS.get(strategy, EXTRACTION_SYSTEM_PROMPT)

        # Add paragraph markers for citation tracking
        marked_text = self._add_paragraph_markers(document_text)
        words = marked_text.split()
        chunks = self._chunk_text(words)

        all_facts: List[Dict[str, Any]] = []
        all_entities: List[Dict[str, Any]] = []
        summaries: List[str] = []
        scores: List[float] = []

        for chunk in chunks:
            user_msg = f"Extract structured facts from this document:\n\n{chunk}"
            try:
                response = await client.chat(
                    model_id=model_id,
                    messages=[{"role": "user", "content": user_msg}],
                    temperature=0.1,
                    max_tokens=4096,
                    system_prompt=system_prompt,
                )
                parsed = self._parse_response(response)
                all_facts.extend(parsed.get("facts", []))
                all_entities.extend(parsed.get("entities", []))
                if parsed.get("summary"):
                    summaries.append(parsed["summary"])
                if parsed.get("relevance_score") is not None:
                    scores.append(float(parsed["relevance_score"]))
            except Exception:
                continue

        # Deduplicate facts and entities
        unique_facts = self._deduplicate_facts(all_facts)
        unique_entities = self._deduplicate_entities(all_entities)

        # Build confidence scores and citations from facts
        confidence_scores: Dict[int, float] = {}
        citations: List[Dict[str, Any]] = []
        for idx, fact in enumerate(unique_facts):
            conf = fact.pop("confidence", None)
            para = fact.pop("paragraph", None)
            if conf is not None:
                confidence_scores[idx] = float(conf)
            if para is not None:
                citations.append({"fact_index": idx, "paragraph": para})

        result = ExtractionResult(
            document_id=document_id,
            facts=unique_facts,
            summary=" ".join(summaries) if summaries else "No relevant content extracted",
            relevance_score=sum(scores) / len(scores) if scores else 0.0,
            extracted_at=datetime.now(tz=timezone.utc).isoformat(),
            confidence_scores=confidence_scores,
            citations=citations,
            entities=unique_entities,
        )

        # Persist
        self._save(result)
        return result

    def _chunk_text(self, words: List[str]) -> List[str]:
        """Split word list into chunks of MAX_CHUNK_WORDS."""
        if len(words) <= self.MAX_CHUNK_WORDS:
            return [" ".join(words)]
        chunks = []
        for i in range(0, len(words), self.MAX_CHUNK_WORDS):
            chunks.append(" ".join(words[i : i + self.MAX_CHUNK_WORDS]))
        return chunks

    def _parse_response(self, response: str) -> Dict[str, Any]:
        """Parse LLM JSON response, tolerating markdown fences."""
        import re

        text = response.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\s*\n?", "", text)
            text = re.sub(r"\n?```\s*$", "", text)

        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1:
            return {"facts": [], "summary": "", "relevance_score": 0.0}

        try:
            return json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            return {"facts": [], "summary": "", "relevance_score": 0.0}

    @staticmethod
    def _add_paragraph_markers(text: str) -> str:
        """Number paragraphs (¶1, ¶2, ...) so the LLM can reference locations."""
        paragraphs = text.split("\n\n")
        marked = []
        for idx, para in enumerate(paragraphs, 1):
            stripped = para.strip()
            if stripped:
                marked.append(f"¶{idx} {stripped}")
        return "\n\n".join(marked)

    def _deduplicate_facts(self, facts: List[Dict]) -> List[Dict]:
        """Remove duplicate facts based on type + key fields."""
        seen = set()
        unique = []
        for f in facts:
            # Exclude volatile fields from dedup key
            stable = {k: v for k, v in f.items() if k not in ("confidence", "paragraph")}
            key = json.dumps(stable, sort_keys=True, default=str)
            if key not in seen:
                seen.add(key)
                unique.append(f)
        return unique

    @staticmethod
    def _deduplicate_entities(entities: List[Dict]) -> List[Dict]:
        """Merge duplicate entities, summing mention counts."""
        merged: Dict[str, Dict] = {}
        for ent in entities:
            name = ent.get("name", "").lower()
            if name in merged:
                merged[name]["mentions"] = merged[name].get("mentions", 0) + ent.get("mentions", 1)
            else:
                merged[name] = dict(ent)
        return list(merged.values())

    def _save(self, result: ExtractionResult) -> None:
        fp = self.extractions_dir / f"{result.document_id}.json"
        fp.write_text(
            json.dumps({
                "document_id": result.document_id,
                "facts": result.facts,
                "summary": result.summary,
                "relevance_score": result.relevance_score,
                "extracted_at": result.extracted_at,
                "confidence_scores": result.confidence_scores,
                "citations": result.citations,
                "entities": result.entities,
            }, indent=2, default=str),
            encoding="utf-8",
        )

    def load_extraction(self, document_id: str) -> Optional[ExtractionResult]:
        """Load a saved extraction by document ID."""
        fp = self.extractions_dir / f"{document_id}.json"
        if not fp.exists():
            return None
        data = json.loads(fp.read_text(encoding="utf-8"))
        # Handle old extractions that lack new fields
        data.setdefault("confidence_scores", {})
        data.setdefault("citations", [])
        data.setdefault("entities", [])
        # Convert confidence_scores keys from str to int (JSON serializes int keys as str)
        if data["confidence_scores"]:
            data["confidence_scores"] = {int(k): v for k, v in data["confidence_scores"].items()}
        return ExtractionResult(**data)

    def list_extractions(self) -> List[Dict]:
        """List all extraction summaries."""
        results = []
        for fp in sorted(self.extractions_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
            try:
                data = json.loads(fp.read_text(encoding="utf-8"))
                results.append({
                    "document_id": data["document_id"],
                    "fact_count": len(data.get("facts", [])),
                    "relevance_score": data.get("relevance_score", 0),
                    "summary": data.get("summary", ""),
                    "extracted_at": data.get("extracted_at", ""),
                })
            except Exception:
                continue
        return results

    def count_facts(self) -> int:
        """Count total extracted facts across all documents."""
        total = 0
        for fp in self.extractions_dir.glob("*.json"):
            try:
                data = json.loads(fp.read_text(encoding="utf-8"))
                total += len(data.get("facts", []))
            except Exception:
                continue
        return total
