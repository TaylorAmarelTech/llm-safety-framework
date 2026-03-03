"""
Indicator Stacking Matrix — maps individually-legal actions across the
migration journey that, when combined, indicate trafficking/exploitation.

Based on:
- Palermo Protocol (ACT + MEANS + PURPOSE framework)
- ILO 11 Forced Labour Indicators
- ILO Fair Recruitment Initiative

Usage::

    from src.scraper.indicator_matrix import IndicatorMatrix

    m = IndicatorMatrix()
    grid = m.get_full_matrix()            # 7 phases x 11 indicators
    result = m.score_actions(["DOC-001", "PRE-003", "RET-001"])
    print(result.risk_level)              # "red_flag"
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Dict, List, Optional, Set


# ── Constants ─────────────────────────────────────────────────────────────────

class JourneyPhase(str, Enum):
    PRE_DEPARTURE = "pre_departure"
    DOCUMENTATION = "documentation"
    TRANSIT = "transit"
    ARRIVAL = "arrival"
    EMPLOYMENT = "employment"
    RETENTION = "retention"
    EXIT = "exit"


PHASE_DESCRIPTIONS: Dict[str, str] = {
    "pre_departure": "Recruitment, job promises, pre-migration preparations",
    "documentation": "Visa processing, passport handling, contracts, paperwork",
    "transit": "Travel to destination country",
    "arrival": "Reception and orientation at destination",
    "employment": "Working conditions, daily work environment",
    "retention": "Ongoing control mechanisms keeping workers in place",
    "exit": "Contract end, return, or inability to leave",
}


class PalermoElement(str, Enum):
    ACT = "act"
    MEANS = "means"
    PURPOSE = "purpose"


ILO_INDICATORS: tuple[str, ...] = (
    "abuse_of_vulnerability",
    "deception",
    "restriction_of_movement",
    "isolation",
    "physical_sexual_violence",
    "intimidation_threats",
    "retention_of_documents",
    "withholding_wages",
    "debt_bondage",
    "abusive_conditions",
    "excessive_overtime",
)

ILO_INDICATOR_LABELS: Dict[str, str] = {
    "abuse_of_vulnerability": "Abuse of Vulnerability",
    "deception": "Deception",
    "restriction_of_movement": "Restriction of Movement",
    "isolation": "Isolation",
    "physical_sexual_violence": "Physical & Sexual Violence",
    "intimidation_threats": "Intimidation & Threats",
    "retention_of_documents": "Retention of Documents",
    "withholding_wages": "Withholding of Wages",
    "debt_bondage": "Debt Bondage",
    "abusive_conditions": "Abusive Conditions",
    "excessive_overtime": "Excessive Overtime",
}

# Risk level thresholds
_RISK_NORMAL = "normal"
_RISK_YELLOW = "yellow_flag"
_RISK_RED = "red_flag"
_RISK_CRITICAL = "critical"

RISK_LEVELS = (_RISK_NORMAL, _RISK_YELLOW, _RISK_RED, _RISK_CRITICAL)
RISK_ORDER = {level: i for i, level in enumerate(RISK_LEVELS)}


# ── Scoring Result ────────────────────────────────────────────────────────────

@dataclass
class ScoringResult:
    """Result of scoring a set of observed indicator actions."""

    action_count: int = 0
    indicator_count: int = 0
    phase_count: int = 0
    risk_level: str = _RISK_NORMAL
    matched_indicators: list[str] = field(default_factory=list)
    matched_phases: list[str] = field(default_factory=list)
    palermo_coverage: dict = field(default_factory=lambda: {
        "act": [], "means": [], "purpose": [],
    })
    palermo_complete: bool = False
    matched_patterns: list[dict] = field(default_factory=list)
    pattern_match_scores: list[dict] = field(default_factory=list)
    risk_explanation: str = ""
    legal_references: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


# ── Main Class ────────────────────────────────────────────────────────────────

class IndicatorMatrix:
    """Indicator stacking matrix engine.

    Loads indicator actions, trafficking patterns, and corridor profiles
    from seed data; provides querying, scoring, and pattern matching.
    """

    ILO_INDICATORS = ILO_INDICATORS

    def __init__(self, data_dir: str = "data/scraper"):
        # Lazy-import to avoid circular deps at module level
        from .seeds.indicator_actions import INDICATOR_ACTIONS
        from .seeds.trafficking_patterns import TRAFFICKING_PATTERNS
        from .seeds.corridor_indicator_profiles import CORRIDOR_INDICATOR_PROFILES

        self._actions: List[Dict[str, Any]] = INDICATOR_ACTIONS
        self._patterns: List[Dict[str, Any]] = TRAFFICKING_PATTERNS
        self._corridor_profiles: List[Dict[str, Any]] = CORRIDOR_INDICATOR_PROFILES

        # Build indexes
        self._action_by_id: Dict[str, Dict] = {}
        self._actions_by_phase: Dict[str, List[Dict]] = defaultdict(list)
        self._actions_by_indicator: Dict[str, List[Dict]] = defaultdict(list)
        self._pattern_by_id: Dict[str, Dict] = {}
        self._corridor_by_id: Dict[str, Dict] = {}

        for action in self._actions:
            aid = action.get("id", "")
            self._action_by_id[aid] = action
            phase = action.get("phase", "")
            self._actions_by_phase[phase].append(action)
            for ind in action.get("ilo_indicators", []):
                self._actions_by_indicator[ind].append(action)

        for pattern in self._patterns:
            pid = pattern.get("id", "")
            self._pattern_by_id[pid] = pattern

        for profile in self._corridor_profiles:
            cid = profile.get("corridor", profile.get("id", ""))
            self._corridor_by_id[cid] = profile

    # ── Properties ────────────────────────────────────────────────────────

    @property
    def total_actions(self) -> int:
        return len(self._actions)

    @property
    def total_patterns(self) -> int:
        return len(self._patterns)

    @property
    def total_corridors(self) -> int:
        return len(self._corridor_profiles)

    # ── Matrix Queries ────────────────────────────────────────────────────

    def get_full_matrix(self) -> Dict[str, Dict[str, List[Dict]]]:
        """Return the full phase x indicator grid.

        Returns:
            {phase: {indicator: [action_dicts]}}
        """
        matrix: Dict[str, Dict[str, List[Dict]]] = {}
        for phase in JourneyPhase:
            matrix[phase.value] = {}
            phase_actions = self._actions_by_phase.get(phase.value, [])
            for ind in ILO_INDICATORS:
                matrix[phase.value][ind] = [
                    a for a in phase_actions
                    if ind in a.get("ilo_indicators", [])
                ]
        return matrix

    def get_matrix_counts(self) -> Dict[str, Dict[str, int]]:
        """Return phase x indicator counts (lighter than full matrix)."""
        matrix = self.get_full_matrix()
        return {
            phase: {ind: len(actions) for ind, actions in indicators.items()}
            for phase, indicators in matrix.items()
        }

    def get_filtered_actions(
        self,
        phase: Optional[str] = None,
        indicator: Optional[str] = None,
        sector: Optional[str] = None,
        corridor: Optional[str] = None,
    ) -> List[Dict]:
        """Filter actions by phase, indicator, sector, or corridor."""
        results = self._actions

        if phase:
            results = [a for a in results if a.get("phase") == phase]
        if indicator:
            results = [a for a in results if indicator in a.get("ilo_indicators", [])]
        if sector:
            results = [a for a in results if sector in a.get("sectors", [])]
        if corridor:
            results = [a for a in results if corridor in a.get("corridors", [])]

        return results

    def get_actions_by_phase(self, phase: str) -> List[Dict]:
        return list(self._actions_by_phase.get(phase, []))

    def get_actions_by_indicator(self, indicator: str) -> List[Dict]:
        return list(self._actions_by_indicator.get(indicator, []))

    # ── Scoring ───────────────────────────────────────────────────────────

    def score_actions(self, action_ids: List[str]) -> ScoringResult:
        """Score a set of observed actions for trafficking risk.

        Scoring logic:
        - Count distinct ILO indicators triggered
        - 0-1 indicators → normal
        - 2 indicators → yellow_flag
        - 3+ indicators → red_flag
        - 3+ indicators AND Palermo complete → critical
        - Cross-phase bonus: 3+ phases adds +1 effective indicator count
        - Known pattern match can override to elevate risk
        """
        if not action_ids:
            return ScoringResult(risk_explanation="No actions selected.")

        # Resolve actions
        resolved = [self._action_by_id[aid] for aid in action_ids if aid in self._action_by_id]
        if not resolved:
            return ScoringResult(
                action_count=len(action_ids),
                risk_explanation="No valid action IDs found.",
            )

        # Collect indicators, phases, Palermo elements
        indicators: Set[str] = set()
        phases: Set[str] = set()
        palermo_acts: Set[str] = set()
        palermo_means: Set[str] = set()
        palermo_purposes: Set[str] = set()
        legal_refs: Set[str] = set()

        for action in resolved:
            for ind in action.get("ilo_indicators", []):
                indicators.add(ind)
            phases.add(action.get("phase", ""))
            for elem in action.get("palermo_elements", []):
                if elem == "act" and action.get("palermo_act"):
                    palermo_acts.add(action["palermo_act"])
                elif elem == "means" and action.get("palermo_means"):
                    palermo_means.add(action["palermo_means"])
                elif elem == "purpose" and action.get("palermo_purpose"):
                    palermo_purposes.add(action["palermo_purpose"])

        # Palermo completeness
        palermo_coverage = {
            "act": sorted(palermo_acts),
            "means": sorted(palermo_means),
            "purpose": sorted(palermo_purposes),
        }
        palermo_complete = bool(palermo_acts and palermo_means and palermo_purposes)

        # Base scoring: count distinct indicators
        indicator_count = len(indicators)
        phase_count = len(phases)

        # Cross-phase bonus: spanning 3+ phases adds +1 effective count
        effective_count = indicator_count
        if phase_count >= 3:
            effective_count += 1

        # Determine risk level from effective count
        if effective_count <= 1:
            risk_level = _RISK_NORMAL
        elif effective_count == 2:
            risk_level = _RISK_YELLOW
        elif palermo_complete and effective_count >= 3:
            risk_level = _RISK_CRITICAL
        else:
            risk_level = _RISK_RED

        # Pattern matching
        matched_patterns, pattern_scores = self._match_patterns(action_ids)

        # Known high-risk pattern override: if a critical pattern matches
        # with >= 60% overlap, elevate to at least red_flag
        for ps in pattern_scores:
            pat = self._pattern_by_id.get(ps["pattern_id"], {})
            pat_risk = pat.get("risk_level", "moderate")
            if ps["overlap_pct"] >= 60 and RISK_ORDER.get(pat_risk, 0) > RISK_ORDER.get(risk_level, 0):
                risk_level = pat_risk
            # Collect legal references from matched patterns
            for ref in pat.get("legal_references", []):
                legal_refs.add(ref)

        # Build explanation
        explanation_parts = []
        explanation_parts.append(
            f"{len(resolved)} action(s) observed across {phase_count} phase(s), "
            f"triggering {indicator_count} distinct ILO indicator(s)."
        )
        if phase_count >= 3:
            explanation_parts.append(
                f"Cross-phase bonus applied (actions span {phase_count} phases)."
            )
        if palermo_complete:
            explanation_parts.append(
                "All three Palermo Protocol elements (ACT + MEANS + PURPOSE) are satisfied."
            )
        if matched_patterns:
            top = matched_patterns[0]
            explanation_parts.append(
                f"Matches known pattern: \"{top['name']}\" "
                f"({pattern_scores[0]['overlap_pct']}% overlap)."
            )

        # Add standard legal references
        if indicator_count >= 2:
            legal_refs.add("Palermo Protocol Art. 3(a)")
            legal_refs.add("ILO Forced Labour Convention (C029)")
        if "debt_bondage" in indicators:
            legal_refs.add("ILO C029 Art. 1 (debt bondage)")
        if "retention_of_documents" in indicators:
            legal_refs.add("ILO Fair Recruitment Initiative")

        return ScoringResult(
            action_count=len(resolved),
            indicator_count=indicator_count,
            phase_count=phase_count,
            risk_level=risk_level,
            matched_indicators=sorted(indicators),
            matched_phases=sorted(phases),
            palermo_coverage=palermo_coverage,
            palermo_complete=palermo_complete,
            matched_patterns=matched_patterns,
            pattern_match_scores=pattern_scores,
            risk_explanation=" ".join(explanation_parts),
            legal_references=sorted(legal_refs),
        )

    # ── Pattern Matching ──────────────────────────────────────────────────

    def _match_patterns(
        self, action_ids: List[str]
    ) -> tuple[List[Dict], List[Dict]]:
        """Find trafficking patterns overlapping with selected actions.

        Returns:
            (matched_pattern_dicts, match_score_dicts)
            sorted by overlap percentage descending.
        """
        action_set = set(action_ids)
        matches = []

        for pattern in self._patterns:
            pat_actions = set(pattern.get("action_ids", []))
            if not pat_actions:
                continue
            overlap = action_set & pat_actions
            if not overlap:
                continue
            overlap_pct = round(100 * len(overlap) / len(pat_actions))
            min_flag = pattern.get("min_actions_for_flag", 3)
            if len(overlap) >= min_flag or overlap_pct >= 50:
                matches.append({
                    "pattern": pattern,
                    "score": {
                        "pattern_id": pattern.get("id", ""),
                        "pattern_name": pattern.get("name", ""),
                        "overlap_pct": overlap_pct,
                        "matched_actions": sorted(overlap),
                        "missing_actions": sorted(pat_actions - action_set),
                        "risk_level": pattern.get("risk_level", "moderate"),
                    },
                })

        # Sort by overlap percentage descending
        matches.sort(key=lambda m: m["score"]["overlap_pct"], reverse=True)

        return (
            [m["pattern"] for m in matches],
            [m["score"] for m in matches],
        )

    def match_patterns(self, action_ids: List[str]) -> List[Dict]:
        """Public API: return matched patterns with scores."""
        _, scores = self._match_patterns(action_ids)
        return scores

    def get_stacking_combos(self, min_risk: str = "yellow_flag") -> List[Dict]:
        """Return known trafficking patterns at or above the given risk level."""
        min_order = RISK_ORDER.get(min_risk, 1)
        return [
            p for p in self._patterns
            if RISK_ORDER.get(p.get("risk_level", "moderate"), 0) >= min_order
        ]

    # ── Corridor Profiles ─────────────────────────────────────────────────

    def get_corridor_profile(self, corridor_id: str) -> Optional[Dict]:
        return self._corridor_by_id.get(corridor_id)

    def list_corridors(self) -> List[Dict]:
        """List all corridor profiles with summary info."""
        return [
            {
                "corridor": p.get("corridor", ""),
                "origin_country": p.get("origin_country", ""),
                "destination_country": p.get("destination_country", ""),
                "primary_sectors": p.get("primary_sectors", []),
                "kafala_system": p.get("kafala_system", False),
                "dominant_indicators": self._top_indicators(p),
            }
            for p in self._corridor_profiles
        ]

    def _top_indicators(self, profile: Dict, n: int = 3) -> List[str]:
        """Return the top-N indicators by prevalence for a corridor profile."""
        prev = profile.get("indicator_prevalence", {})
        sorted_inds = sorted(prev.items(), key=lambda x: x[1], reverse=True)
        return [ind for ind, _ in sorted_inds[:n]]

    # ── Sector Profiles ───────────────────────────────────────────────────

    def get_sector_profile(self, sector: str) -> Dict:
        """Build an aggregate profile for a given sector."""
        actions = [a for a in self._actions if sector in a.get("sectors", [])]
        patterns = [p for p in self._patterns if sector in p.get("sectors", [])]
        corridors = [c for c in self._corridor_profiles if sector in c.get("primary_sectors", [])]

        # Indicator frequency across actions
        ind_counts: Dict[str, int] = defaultdict(int)
        phase_counts: Dict[str, int] = defaultdict(int)
        for a in actions:
            for ind in a.get("ilo_indicators", []):
                ind_counts[ind] += 1
            phase_counts[a.get("phase", "")] += 1

        return {
            "sector": sector,
            "action_count": len(actions),
            "pattern_count": len(patterns),
            "corridor_count": len(corridors),
            "indicator_frequency": dict(
                sorted(ind_counts.items(), key=lambda x: x[1], reverse=True)
            ),
            "phase_distribution": dict(
                sorted(phase_counts.items(), key=lambda x: x[1], reverse=True)
            ),
            "dominant_patterns": [
                {"id": p.get("id"), "name": p.get("name"), "risk_level": p.get("risk_level")}
                for p in patterns[:10]
            ],
            "corridors": [c.get("corridor") for c in corridors],
        }

    def list_sectors(self) -> List[Dict]:
        """List all sectors with action and pattern counts."""
        sector_set: Set[str] = set()
        for a in self._actions:
            for s in a.get("sectors", []):
                sector_set.add(s)

        results = []
        for sector in sorted(sector_set):
            action_count = sum(
                1 for a in self._actions if sector in a.get("sectors", [])
            )
            pattern_count = sum(
                1 for p in self._patterns if sector in p.get("sectors", [])
            )
            results.append({
                "sector": sector,
                "action_count": action_count,
                "pattern_count": pattern_count,
            })
        return results

    # ── Palermo Mapping ───────────────────────────────────────────────────

    def get_palermo_mapping(self) -> Dict[str, Dict[str, List[str]]]:
        """Map all actions to Palermo Protocol elements.

        Returns:
            {element: {subtype: [action_ids]}}
        """
        mapping: Dict[str, Dict[str, List[str]]] = {
            "act": defaultdict(list),
            "means": defaultdict(list),
            "purpose": defaultdict(list),
        }

        for action in self._actions:
            aid = action.get("id", "")
            if action.get("palermo_act"):
                mapping["act"][action["palermo_act"]].append(aid)
            if action.get("palermo_means"):
                mapping["means"][action["palermo_means"]].append(aid)
            if action.get("palermo_purpose"):
                mapping["purpose"][action["palermo_purpose"]].append(aid)

        # Convert defaultdicts to regular dicts
        return {
            elem: dict(subtypes)
            for elem, subtypes in mapping.items()
        }

    # ── Phase Info ────────────────────────────────────────────────────────

    def list_phases(self) -> List[Dict]:
        """List all journey phases with descriptions and action counts."""
        return [
            {
                "phase": phase.value,
                "description": PHASE_DESCRIPTIONS.get(phase.value, ""),
                "action_count": len(self._actions_by_phase.get(phase.value, [])),
            }
            for phase in JourneyPhase
        ]
