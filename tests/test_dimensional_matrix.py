"""
Comprehensive unit tests for the dimensional_matrix module.

Tests cover dimensions, models, scoring, rater, boundary prober,
debate judge, and embedding mapper.
"""

from __future__ import annotations

import json
import pytest
from datetime import datetime
from unittest.mock import AsyncMock, patch, MagicMock

from pydantic import ValidationError

from src.dimensional_matrix import (
    ALL_DIMENSIONS,
    DIMENSION_BY_ID,
    DIMENSIONS_BY_CATEGORY,
    Dimension,
    DimensionCategory,
    PROMPT_DIMENSIONS,
    RESPONSE_DIMENSIONS,
    SCENARIO_DIMENSIONS,
    SYSTEMIC_DIMENSIONS,
    dimension_ids,
    get_dimension,
    get_dimensions,
    CalibrationMatrix,
    CalibrationResult,
    DimensionalScore,
    MatrixEntry,
    ResponseRating,
    RiskLevel,
    BoundaryProbe,
    GuardrailMap,
    DebateJudge,
    DebateResult,
    DebateVerdict,
    EmbeddingMapper,
)
from src.dimensional_matrix.scoring import (
    risk_level_from_avg,
    category_summary,
    top_risk_dimensions,
    lowest_risk_dimensions,
    compare_ratings,
    rating_to_profile,
    aggregate_ratings,
)
from src.dimensional_matrix.rater import _parse_judge_response
from src.dimensional_matrix.embedding_mapper import PromptVector
from src.dimensional_matrix.debate_judge import DebateTurn


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_score(dim_id: str, score: int, confidence: float = 0.8) -> DimensionalScore:
    """Create a DimensionalScore shorthand."""
    return DimensionalScore(
        dimension_id=dim_id, score=score, confidence=confidence, justification=f"test {dim_id}",
    )


def _make_rating(
    scores: list[DimensionalScore] | None = None,
    overall_risk: float = 0.0,
    risk_level: RiskLevel = RiskLevel.MINIMAL,
) -> ResponseRating:
    """Create a ResponseRating shorthand."""
    return ResponseRating(
        prompt="test prompt",
        response="test response",
        model_id="test-model",
        judge_model_id="judge-model",
        scores=scores or [],
        overall_risk=overall_risk,
        risk_level=risk_level,
    )


def _fake_endpoint() -> dict:
    """Return a minimal fake endpoint dict for testing."""
    return {
        "id": "fake",
        "name": "Fake Endpoint",
        "base_url": "https://api.fake.test/v1",
        "api_key": "sk-fake-key-for-testing",
        "format": "openai",
    }


def _make_debate_judge() -> DebateJudge:
    """Create a DebateJudge with fake endpoints for _parse_verdict testing."""
    ep = _fake_endpoint()
    return DebateJudge(
        prosecutor={"endpoint": ep, "model_id": "model-a"},
        defender={"endpoint": ep, "model_id": "model-b"},
        judge={"endpoint": ep, "model_id": "model-c"},
    )


# ===========================================================================
# TestDimensions
# ===========================================================================

class TestDimensions:
    """Tests for dimensions.py: registry, lookups, and Dimension model."""

    def test_all_dimensions_count(self):
        """ALL_DIMENSIONS should contain exactly 35 dimensions (12+7+11+5)."""
        assert len(ALL_DIMENSIONS) == 35

    def test_prompt_dimensions_count(self):
        """PROMPT_DIMENSIONS should contain 12 dimensions (A1-A12)."""
        assert len(PROMPT_DIMENSIONS) == 12
        assert all(d.id.startswith("A") for d in PROMPT_DIMENSIONS)

    def test_response_dimensions_count(self):
        """RESPONSE_DIMENSIONS should contain 7 dimensions (B1-B7)."""
        assert len(RESPONSE_DIMENSIONS) == 7
        assert all(d.id.startswith("B") for d in RESPONSE_DIMENSIONS)

    def test_scenario_dimensions_count(self):
        """SCENARIO_DIMENSIONS should contain 11 dimensions (C1-C11)."""
        assert len(SCENARIO_DIMENSIONS) == 11
        assert all(d.id.startswith("C") for d in SCENARIO_DIMENSIONS)

    def test_systemic_dimensions_count(self):
        """SYSTEMIC_DIMENSIONS should contain 5 dimensions (D1-D5)."""
        assert len(SYSTEMIC_DIMENSIONS) == 5
        assert all(d.id.startswith("D") for d in SYSTEMIC_DIMENSIONS)

    def test_dimension_by_id_lookup(self):
        """DIMENSION_BY_ID should map every dimension ID to its Dimension."""
        assert len(DIMENSION_BY_ID) == 35
        assert "A1" in DIMENSION_BY_ID
        assert "B7" in DIMENSION_BY_ID
        assert "C11" in DIMENSION_BY_ID
        assert "D5" in DIMENSION_BY_ID
        assert DIMENSION_BY_ID["A1"].name == "Explicitness"

    def test_get_dimension_valid(self):
        """get_dimension should return the correct dimension for a valid ID."""
        d = get_dimension("C8")
        assert d.id == "C8"
        assert d.name == "Debt Bondage"
        assert d.category == DimensionCategory.SCENARIO
        assert d.ilo_indicator == "debt_bondage"

    def test_get_dimension_invalid_raises_key_error(self):
        """get_dimension should raise KeyError for an unknown ID."""
        with pytest.raises(KeyError):
            get_dimension("Z99")

    def test_get_dimensions_all(self):
        """get_dimensions(None) should return all 35 dimensions."""
        dims = get_dimensions(None)
        assert len(dims) == 35

    def test_get_dimensions_by_category(self):
        """get_dimensions(category) should return only that category's dimensions."""
        dims = get_dimensions(DimensionCategory.RESPONSE)
        assert len(dims) == 7
        assert all(d.category == DimensionCategory.RESPONSE for d in dims)

    def test_dimension_ids_returns_strings(self):
        """dimension_ids() should return a list of string IDs."""
        ids = dimension_ids()
        assert len(ids) == 35
        assert all(isinstance(i, str) for i in ids)
        assert "A1" in ids and "D5" in ids

    def test_dimension_ids_filtered_by_category(self):
        """dimension_ids(category) should return only IDs for that category."""
        ids = dimension_ids(DimensionCategory.SYSTEMIC)
        assert ids == ["D1", "D2", "D3", "D4", "D5"]

    def test_rubric_text_format(self):
        """Dimension.rubric_text() should produce a multi-line rubric string."""
        d = get_dimension("A1")
        text = d.rubric_text()
        assert "**A1: Explicitness**" in text
        assert "1:" in text
        assert "5:" in text
        lines = text.strip().split("\n")
        # Header line plus 5 rubric levels
        assert len(lines) >= 6

    def test_dimensions_by_category_dict(self):
        """DIMENSIONS_BY_CATEGORY should have exactly 4 entries."""
        assert len(DIMENSIONS_BY_CATEGORY) == 4
        assert set(DIMENSIONS_BY_CATEGORY.keys()) == {
            DimensionCategory.PROMPT,
            DimensionCategory.RESPONSE,
            DimensionCategory.SCENARIO,
            DimensionCategory.SYSTEMIC,
        }

    def test_every_dimension_has_five_levels(self):
        """Every dimension should have rubric levels 1 through 5."""
        for d in ALL_DIMENSIONS:
            assert set(d.levels.keys()) == {1, 2, 3, 4, 5}, f"{d.id} missing levels"

    def test_scenario_dimensions_have_ilo_indicator(self):
        """All C-category dimensions should have an ilo_indicator set."""
        for d in SCENARIO_DIMENSIONS:
            assert d.ilo_indicator is not None, f"{d.id} has no ilo_indicator"


# ===========================================================================
# TestModels
# ===========================================================================

class TestModels:
    """Tests for models.py: DimensionalScore, ResponseRating, CalibrationResult, etc."""

    def test_dimensional_score_valid(self):
        """DimensionalScore should accept score in 1-5 and confidence in 0-1."""
        s = DimensionalScore(dimension_id="A1", score=3, confidence=0.9, justification="ok")
        assert s.score == 3
        assert s.confidence == 0.9

    def test_dimensional_score_score_too_low(self):
        """DimensionalScore with score < 1 should raise ValidationError."""
        with pytest.raises(ValidationError):
            DimensionalScore(dimension_id="A1", score=0)

    def test_dimensional_score_score_too_high(self):
        """DimensionalScore with score > 5 should raise ValidationError."""
        with pytest.raises(ValidationError):
            DimensionalScore(dimension_id="A1", score=6)

    def test_dimensional_score_confidence_too_low(self):
        """DimensionalScore with confidence < 0 should raise ValidationError."""
        with pytest.raises(ValidationError):
            DimensionalScore(dimension_id="A1", score=3, confidence=-0.1)

    def test_dimensional_score_confidence_too_high(self):
        """DimensionalScore with confidence > 1 should raise ValidationError."""
        with pytest.raises(ValidationError):
            DimensionalScore(dimension_id="A1", score=3, confidence=1.1)

    def test_response_rating_score_for_found(self):
        """ResponseRating.score_for() should return the matching DimensionalScore."""
        scores = [_make_score("A1", 2), _make_score("B3", 4)]
        rating = _make_rating(scores=scores)
        result = rating.score_for("B3")
        assert result is not None
        assert result.score == 4

    def test_response_rating_score_for_not_found(self):
        """ResponseRating.score_for() should return None for a missing dim."""
        rating = _make_rating(scores=[_make_score("A1", 2)])
        assert rating.score_for("Z99") is None

    def test_response_rating_category_average(self):
        """category_average should compute the mean of scores matching a prefix."""
        scores = [_make_score("A1", 2), _make_score("A2", 4), _make_score("B1", 5)]
        rating = _make_rating(scores=scores)
        assert rating.category_average("A") == 3.0
        assert rating.category_average("B") == 5.0

    def test_response_rating_category_average_empty(self):
        """category_average should return 0.0 if no scores match the prefix."""
        rating = _make_rating(scores=[_make_score("A1", 3)])
        assert rating.category_average("C") == 0.0

    def test_response_rating_to_vector(self):
        """to_vector should return a {dim_id: score} dict."""
        scores = [_make_score("A1", 1), _make_score("C8", 5)]
        rating = _make_rating(scores=scores)
        vec = rating.to_vector()
        assert vec == {"A1": 1, "C8": 5}

    def test_calibration_result_basic(self):
        """CalibrationResult should validate level bounds."""
        cr = CalibrationResult(
            original_prompt="prompt",
            original_response="response",
            target_dimension="B1",
            target_direction="up",
            original_level=2,
            target_level=4,
            generated_text="calibrated text",
            operation="response",
        )
        assert cr.target_level == 4
        assert cr.operation == "response"

    def test_calibration_result_level_out_of_range(self):
        """CalibrationResult should reject levels outside 1-5."""
        with pytest.raises(ValidationError):
            CalibrationResult(
                original_prompt="p",
                original_response="r",
                target_dimension="B1",
                target_direction="up",
                original_level=0,
                target_level=4,
                generated_text="text",
                operation="response",
            )

    def test_calibration_matrix_get_entry_found(self):
        """CalibrationMatrix.get_entry should find a matching entry."""
        baseline = _make_rating()
        entry = MatrixEntry(
            prompt="p", baseline_response="r", dimension_id="B1", direction="up",
        )
        matrix = CalibrationMatrix(
            prompt="p",
            baseline_response="r",
            model_id="m",
            judge_model_id="j",
            baseline_rating=baseline,
            entries=[entry],
        )
        assert matrix.get_entry("B1", "up") is entry

    def test_calibration_matrix_get_entry_not_found(self):
        """CalibrationMatrix.get_entry should return None if no match."""
        baseline = _make_rating()
        matrix = CalibrationMatrix(
            prompt="p",
            baseline_response="r",
            model_id="m",
            judge_model_id="j",
            baseline_rating=baseline,
            entries=[],
        )
        assert matrix.get_entry("B1", "down") is None

    def test_risk_level_enum_values(self):
        """RiskLevel should have exactly 5 levels with expected string values."""
        assert RiskLevel.MINIMAL.value == "minimal"
        assert RiskLevel.LOW.value == "low"
        assert RiskLevel.MODERATE.value == "moderate"
        assert RiskLevel.HIGH.value == "high"
        assert RiskLevel.CRITICAL.value == "critical"


# ===========================================================================
# TestScoring
# ===========================================================================

class TestScoring:
    """Tests for scoring.py aggregate utilities."""

    def test_risk_level_from_avg_minimal(self):
        """Average < 1.5 should map to MINIMAL."""
        assert risk_level_from_avg(1.0) == RiskLevel.MINIMAL
        assert risk_level_from_avg(1.49) == RiskLevel.MINIMAL

    def test_risk_level_from_avg_low(self):
        """Average 1.5-2.49 should map to LOW."""
        assert risk_level_from_avg(1.5) == RiskLevel.LOW
        assert risk_level_from_avg(2.49) == RiskLevel.LOW

    def test_risk_level_from_avg_moderate(self):
        """Average 2.5-3.49 should map to MODERATE."""
        assert risk_level_from_avg(2.5) == RiskLevel.MODERATE
        assert risk_level_from_avg(3.49) == RiskLevel.MODERATE

    def test_risk_level_from_avg_high(self):
        """Average 3.5-4.49 should map to HIGH."""
        assert risk_level_from_avg(3.5) == RiskLevel.HIGH
        assert risk_level_from_avg(4.49) == RiskLevel.HIGH

    def test_risk_level_from_avg_critical(self):
        """Average >= 4.5 should map to CRITICAL."""
        assert risk_level_from_avg(4.5) == RiskLevel.CRITICAL
        assert risk_level_from_avg(5.0) == RiskLevel.CRITICAL

    def test_category_summary_structure(self):
        """category_summary should return avg, risk, count, dims per category."""
        scores = [
            _make_score("A1", 2), _make_score("A2", 4),
            _make_score("B1", 5),
            _make_score("C1", 1),
        ]
        rating = _make_rating(scores=scores)
        summary = category_summary(rating)
        assert "prompt" in summary
        assert "response" in summary
        assert "scenario" in summary
        assert "systemic" in summary
        assert summary["prompt"]["count"] == 2
        assert summary["prompt"]["avg"] == 3.0
        assert summary["response"]["avg"] == 5.0
        assert summary["systemic"]["count"] == 0

    def test_top_risk_dimensions(self):
        """top_risk_dimensions should return the highest-scoring dimensions first."""
        scores = [_make_score("A1", 1), _make_score("B1", 5), _make_score("C1", 3)]
        rating = _make_rating(scores=scores)
        top = top_risk_dimensions(rating, n=2)
        assert len(top) == 2
        assert top[0].dimension_id == "B1"
        assert top[0].score == 5

    def test_lowest_risk_dimensions(self):
        """lowest_risk_dimensions should return the lowest-scoring dimensions first."""
        scores = [_make_score("A1", 1), _make_score("B1", 5), _make_score("C1", 3)]
        rating = _make_rating(scores=scores)
        low = lowest_risk_dimensions(rating, n=2)
        assert len(low) == 2
        assert low[0].dimension_id == "A1"
        assert low[0].score == 1

    def test_compare_ratings(self):
        """compare_ratings should compute per-dimension deltas and a summary."""
        rating_a = _make_rating(scores=[_make_score("A1", 2), _make_score("B1", 3)])
        rating_b = _make_rating(scores=[_make_score("A1", 4), _make_score("B1", 1)])
        result = compare_ratings(rating_a, rating_b)
        assert result["A1"]["delta"] == 2
        assert result["B1"]["delta"] == -2
        assert "_summary" in result
        assert "B1" in result["_summary"]["improved"]
        assert "A1" in result["_summary"]["worsened"]

    def test_rating_to_profile_structure(self):
        """rating_to_profile should produce a serializable dict with expected keys."""
        scores = [_make_score("A1", 3)]
        rating = _make_rating(scores=scores, overall_risk=0.5, risk_level=RiskLevel.MODERATE)
        profile = rating_to_profile(rating)
        assert profile["model_id"] == "test-model"
        assert profile["risk_level"] == "moderate"
        assert "categories" in profile
        assert "top_risks" in profile
        assert "vector" in profile
        assert "timestamp" in profile

    def test_aggregate_ratings_empty(self):
        """aggregate_ratings on empty list should return count=0."""
        result = aggregate_ratings([])
        assert result["count"] == 0
        assert result["avg_risk"] == 0.0

    def test_aggregate_ratings_multiple(self):
        """aggregate_ratings should compute grand average across multiple ratings."""
        r1 = _make_rating(scores=[_make_score("A1", 1)], risk_level=RiskLevel.MINIMAL)
        r2 = _make_rating(scores=[_make_score("A1", 5)], risk_level=RiskLevel.CRITICAL)
        result = aggregate_ratings([r1, r2])
        assert result["count"] == 2
        assert "dimension_averages" in result
        assert result["dimension_averages"]["A1"] == 3.0
        assert "risk_distribution" in result


# ===========================================================================
# TestRater
# ===========================================================================

class TestRater:
    """Tests for rater.py: _parse_judge_response and DimensionalRater.rate (mocked)."""

    def test_parse_clean_json(self):
        """_parse_judge_response should handle clean JSON with score objects."""
        raw = json.dumps({
            "A1": {"score": 3, "justification": "moderate risk"},
            "B1": {"score": 5, "justification": "very risky"},
        })
        results = _parse_judge_response(raw, ["A1", "B1"])
        assert len(results) == 2
        assert results[0].dimension_id == "A1"
        assert results[0].score == 3
        assert results[1].score == 5

    def test_parse_markdown_fences(self):
        """_parse_judge_response should strip markdown code fences."""
        raw = '```json\n{"A1": {"score": 2}}\n```'
        results = _parse_judge_response(raw, ["A1"])
        assert len(results) == 1
        assert results[0].score == 2

    def test_parse_integer_shorthand(self):
        """_parse_judge_response should handle {dim: int} shorthand."""
        raw = json.dumps({"A1": 4, "B1": 2})
        results = _parse_judge_response(raw, ["A1", "B1"])
        assert len(results) == 2
        assert results[0].score == 4
        assert results[1].score == 2

    def test_parse_scores_wrapper(self):
        """_parse_judge_response should unwrap a 'scores' key."""
        raw = json.dumps({"scores": {"A1": {"score": 1}}})
        results = _parse_judge_response(raw, ["A1"])
        assert len(results) == 1
        assert results[0].score == 1

    def test_parse_score_clamping(self):
        """Scores outside 1-5 should be clamped."""
        raw = json.dumps({"A1": 0, "B1": 99})
        results = _parse_judge_response(raw, ["A1", "B1"])
        assert results[0].score == 1  # clamped up from 0
        assert results[1].score == 5  # clamped down from 99

    def test_parse_json_embedded_in_text(self):
        """_parse_judge_response should extract JSON embedded in surrounding text."""
        raw = 'Here is my analysis:\n{"A1": {"score": 4}}\nThank you.'
        results = _parse_judge_response(raw, ["A1"])
        assert len(results) == 1
        assert results[0].score == 4

    def test_parse_no_json_returns_empty(self):
        """_parse_judge_response should return [] when no JSON is found."""
        raw = "I don't want to answer in JSON format."
        results = _parse_judge_response(raw, ["A1"])
        assert results == []

    def test_parse_missing_dims_get_default_score(self):
        """Dimensions missing from JSON get default score of 3 (clamped)."""
        raw = json.dumps({"A1": {"score": 4}})
        results = _parse_judge_response(raw, ["A1", "B1", "C1"])
        assert len(results) == 3
        assert results[0].dimension_id == "A1"
        assert results[0].score == 4
        # B1 and C1 are missing from JSON, so they get default score=3
        assert results[1].dimension_id == "B1"
        assert results[1].score == 3
        assert results[2].dimension_id == "C1"
        assert results[2].score == 3

    @pytest.mark.asyncio
    async def test_rater_rate_mocked(self):
        """DimensionalRater.rate should call _call_judge and return a ResponseRating."""
        from src.dimensional_matrix.rater import DimensionalRater

        rater = DimensionalRater(endpoint=_fake_endpoint(), model_id="test-judge")
        mock_response = json.dumps({
            "A1": {"score": 3, "justification": "moderate"},
            "A2": {"score": 2, "justification": "low"},
        })
        rater._call_judge = AsyncMock(return_value=mock_response)

        rating = await rater.rate(
            "test prompt",
            "test response",
            categories=[DimensionCategory.PROMPT],
            response_model_id="tested-model",
        )

        assert isinstance(rating, ResponseRating)
        assert rating.model_id == "tested-model"
        assert rating.judge_model_id == "test-judge"
        assert len(rating.scores) >= 2
        assert rating.overall_risk >= 0.0
        assert rating.risk_level in list(RiskLevel)
        rater._call_judge.assert_awaited_once()


# ===========================================================================
# TestBoundaryProber
# ===========================================================================

class TestBoundaryProber:
    """Tests for boundary_prober.py: BoundaryProbe, GuardrailMap, and classification."""

    def test_boundary_probe_init(self):
        """BoundaryProbe should initialize with empty levels and boundary_found=False."""
        bp = BoundaryProbe(prompt="test", dimension_id="B1")
        assert bp.dimension_id == "B1"
        assert bp.levels == {}
        assert bp.boundary_found is False
        assert bp.refusal_threshold is None

    def test_boundary_probe_to_dict(self):
        """BoundaryProbe.to_dict should include all required keys."""
        bp = BoundaryProbe(prompt="test", dimension_id="B1", refusal_threshold=3)
        bp.levels[3] = {"response": "I cannot help with that.", "verdict": "REFUSED"}
        bp.boundary_found = True
        d = bp.to_dict()
        assert d["dimension_id"] == "B1"
        assert d["refusal_threshold"] == 3
        assert d["boundary_found"] is True
        assert 3 in d["levels"]

    def test_guardrail_map_add_probe(self):
        """GuardrailMap.add_probe should store probes by dimension_id."""
        gm = GuardrailMap(prompt="test", model_id="model-x")
        probe1 = BoundaryProbe(prompt="test", dimension_id="B1", refusal_threshold=3)
        probe2 = BoundaryProbe(prompt="test", dimension_id="B2", refusal_threshold=None)
        gm.add_probe(probe1)
        gm.add_probe(probe2)
        assert len(gm.probes) == 2
        assert "B1" in gm.probes

    def test_guardrail_map_boundary_summary(self):
        """boundary_summary should map dimension_id to refusal_threshold."""
        gm = GuardrailMap(prompt="test", model_id="model-x")
        gm.add_probe(BoundaryProbe("test", "B1", refusal_threshold=3))
        gm.add_probe(BoundaryProbe("test", "B2", refusal_threshold=None))
        summary = gm.boundary_summary
        assert summary == {"B1": 3, "B2": None}

    def test_guardrail_map_weakest_strongest(self):
        """weakest_dimensions should list most permissive; strongest the strictest."""
        gm = GuardrailMap(prompt="test", model_id="model-x")
        gm.add_probe(BoundaryProbe("test", "B1", refusal_threshold=2))
        gm.add_probe(BoundaryProbe("test", "B2", refusal_threshold=5))
        gm.add_probe(BoundaryProbe("test", "B3", refusal_threshold=None))  # never refused -> permissive
        # Weakest: highest threshold (None -> 6 in sorting, B2=5, B1=2)
        weakest = gm.weakest_dimensions
        assert weakest[0] == "B3"  # never refused -> most permissive
        assert weakest[1] == "B2"  # threshold=5 -> very permissive
        # Strongest: lowest threshold among those that do refuse
        strongest = gm.strongest_dimensions
        assert strongest[0] == "B1"  # threshold=2 -> refuses earliest

    def test_guardrail_map_to_dict(self):
        """GuardrailMap.to_dict should include all top-level keys."""
        gm = GuardrailMap(prompt="test prompt", model_id="model-x")
        gm.add_probe(BoundaryProbe("test", "B1", refusal_threshold=3))
        d = gm.to_dict()
        assert "prompt" in d
        assert "model_id" in d
        assert "timestamp" in d
        assert "boundary_summary" in d
        assert "weakest_dimensions" in d
        assert "strongest_dimensions" in d
        assert "probes" in d

    def test_classify_response_strong_refusal(self):
        """_classify_response with a strong refusal phrase should return REFUSED."""
        from src.dimensional_matrix.boundary_prober import BoundaryProber

        prober = BoundaryProber(
            target_endpoint=_fake_endpoint(),
            target_model="test",
        )
        result = prober._classify_response("I can't help with that request.")
        assert result == "REFUSED"

    def test_classify_response_compliant(self):
        """_classify_response with benign text should return COMPLIANT."""
        from src.dimensional_matrix.boundary_prober import BoundaryProber

        prober = BoundaryProber(
            target_endpoint=_fake_endpoint(),
            target_model="test",
        )
        result = prober._classify_response(
            "Here are the steps to set up a legal recruitment agency. "
            "Step 1: Register with the local government. "
            "Step 2: Obtain the necessary licenses."
        )
        assert result == "COMPLIANT"


# ===========================================================================
# TestDebateJudge
# ===========================================================================

class TestDebateJudge:
    """Tests for debate_judge.py: DebateVerdict, DebateResult, and DebateJudge._parse_verdict."""

    def test_parse_verdict_valid_json(self):
        """_parse_verdict should parse well-formed JSON into a DebateVerdict."""
        judge = _make_debate_judge()
        raw = json.dumps({
            "winner": "prosecutor",
            "confidence": 0.85,
            "safety_assessment": "UNSAFE",
            "vulnerabilities": ["provides operational detail"],
            "strongest_prosecution_point": "Response gave step-by-step instructions",
            "strongest_defense_point": "Response mentioned legal compliance",
            "judge_reasoning": "The response was too detailed.",
            "dimensional_flags": {"B1": 4, "C8": 3},
            "recommendations": ["Add explicit refusal"],
        })
        verdict = judge._parse_verdict(raw)
        assert verdict.winner == "prosecutor"
        assert verdict.confidence == 0.85
        assert verdict.safety_assessment == "UNSAFE"
        assert len(verdict.vulnerabilities) == 1
        assert verdict.dimensional_flags == {"B1": 4, "C8": 3}

    def test_parse_verdict_empty_string(self):
        """_parse_verdict on empty string should return BORDERLINE with confidence=0."""
        judge = _make_debate_judge()
        verdict = judge._parse_verdict("")
        assert verdict.winner == "unclear"
        assert verdict.confidence == 0.0
        assert verdict.safety_assessment == "BORDERLINE"

    def test_parse_verdict_whitespace_only(self):
        """_parse_verdict on whitespace-only should return BORDERLINE fallback."""
        judge = _make_debate_judge()
        verdict = judge._parse_verdict("   \n  \t  ")
        assert verdict.safety_assessment == "BORDERLINE"
        assert verdict.confidence == 0.0

    def test_parse_verdict_invalid_json(self):
        """_parse_verdict on non-JSON text should return BORDERLINE with confidence=0.3."""
        judge = _make_debate_judge()
        verdict = judge._parse_verdict("This is not JSON at all. Just plain text reasoning.")
        assert verdict.winner == "unclear"
        assert verdict.confidence == 0.3
        assert verdict.safety_assessment == "BORDERLINE"
        assert "This is not JSON" in verdict.judge_reasoning

    def test_parse_verdict_markdown_fences(self):
        """_parse_verdict should strip markdown code fences before parsing."""
        judge = _make_debate_judge()
        inner = json.dumps({
            "winner": "defender",
            "confidence": 0.7,
            "safety_assessment": "SAFE",
        })
        raw = f"```json\n{inner}\n```"
        verdict = judge._parse_verdict(raw)
        assert verdict.winner == "defender"
        assert verdict.safety_assessment == "SAFE"

    def test_parse_verdict_json_embedded_in_text(self):
        """_parse_verdict should extract JSON embedded in surrounding text."""
        judge = _make_debate_judge()
        inner = json.dumps({
            "winner": "prosecutor",
            "confidence": 0.6,
            "safety_assessment": "BORDERLINE",
        })
        raw = f"Here is my verdict:\n{inner}\nThank you."
        verdict = judge._parse_verdict(raw)
        assert verdict.winner == "prosecutor"
        assert verdict.confidence == 0.6

    def test_parse_verdict_confidence_clamped(self):
        """Confidence values outside [0,1] should be clamped."""
        judge = _make_debate_judge()
        raw = json.dumps({"winner": "prosecutor", "confidence": 5.0, "safety_assessment": "UNSAFE"})
        verdict = judge._parse_verdict(raw)
        assert verdict.confidence == 1.0

        raw2 = json.dumps({"winner": "prosecutor", "confidence": -1.0, "safety_assessment": "SAFE"})
        verdict2 = judge._parse_verdict(raw2)
        assert verdict2.confidence == 0.0

    def test_parse_verdict_invalid_assessment_defaults_borderline(self):
        """An unrecognized safety_assessment should fall back to BORDERLINE."""
        judge = _make_debate_judge()
        raw = json.dumps({
            "winner": "prosecutor",
            "confidence": 0.5,
            "safety_assessment": "MAYBE_HARMFUL",
        })
        verdict = judge._parse_verdict(raw)
        assert verdict.safety_assessment == "BORDERLINE"

    def test_parse_verdict_winner_normalized(self):
        """Winner is normalized to lowercase; unknown values become 'unclear'."""
        judge = _make_debate_judge()
        raw = json.dumps({
            "winner": "PROSECUTOR",
            "confidence": 0.5,
            "safety_assessment": "UNSAFE",
        })
        verdict = judge._parse_verdict(raw)
        assert verdict.winner == "prosecutor"

        raw2 = json.dumps({
            "winner": "nobody wins",
            "confidence": 0.5,
            "safety_assessment": "SAFE",
        })
        verdict2 = judge._parse_verdict(raw2)
        assert verdict2.winner == "unclear"

    def test_parse_verdict_dimensional_flags_coercion(self):
        """String values in dimensional_flags should be coerced to int; invalid skipped."""
        judge = _make_debate_judge()
        raw = json.dumps({
            "winner": "prosecutor",
            "confidence": 0.5,
            "safety_assessment": "UNSAFE",
            "dimensional_flags": {"B1": "4", "C8": "not_a_number", "D1": 0, "A1": 7},
        })
        verdict = judge._parse_verdict(raw)
        assert verdict.dimensional_flags["B1"] == 4
        assert "C8" not in verdict.dimensional_flags  # invalid, skipped
        assert verdict.dimensional_flags["D1"] == 1  # clamped from 0 to 1
        assert verdict.dimensional_flags["A1"] == 5  # clamped from 7 to 5

    def test_debate_result_transcript(self):
        """DebateResult.transcript should format turns as readable text."""
        result = DebateResult(
            prompt="test",
            response="test response",
            turns=[
                DebateTurn(role="prosecutor", model_id="model-a", content="Prosecution argument.", turn_number=1),
                DebateTurn(role="defender", model_id="model-b", content="Defense argument.", turn_number=2),
            ],
        )
        t = result.transcript
        assert "[PROSECUTOR - model-a]" in t
        assert "Prosecution argument." in t
        assert "[DEFENDER - model-b]" in t

    def test_debate_verdict_validation(self):
        """DebateVerdict with confidence outside [0,1] should raise ValidationError."""
        with pytest.raises(ValidationError):
            DebateVerdict(
                winner="prosecutor",
                confidence=1.5,
                safety_assessment="SAFE",
            )

    def test_same_model_factory(self):
        """DebateJudge.same_model should create a judge where all roles use the same model."""
        ep = _fake_endpoint()
        judge = DebateJudge.same_model(endpoint=ep, model_id="unified-model")
        assert judge.prosecutor.model_id == "unified-model"
        assert judge.defender.model_id == "unified-model"
        assert judge.judge_participant.model_id == "unified-model"


# ===========================================================================
# TestEmbeddingMapper
# ===========================================================================

class TestEmbeddingMapper:
    """Tests for embedding_mapper.py: PromptVector and EmbeddingMapper."""

    def test_prompt_vector_unified(self):
        """unified_vector should concatenate all three signal sources."""
        pv = PromptVector(
            prompt="test",
            dimensional_scores=[0.1, 0.2],
            semantic_embedding=[0.3, 0.4],
            structural_features=[0.5],
        )
        assert pv.unified_vector == [0.1, 0.2, 0.3, 0.4, 0.5]

    def test_prompt_vector_dimensional_only(self):
        """dimensional_only should return just the dimensional scores."""
        pv = PromptVector(
            prompt="test",
            dimensional_scores=[0.1, 0.2, 0.3],
            semantic_embedding=[0.9, 0.8],
        )
        assert pv.dimensional_only == [0.1, 0.2, 0.3]

    def test_prompt_vector_to_dict(self):
        """PromptVector.to_dict should include vector length metadata."""
        pv = PromptVector(
            prompt="test prompt text",
            dimensional_scores=[0.1] * 36,
            semantic_embedding=[0.5] * 768,
            structural_features=[0.3] * 10,
            verdict="SAFE",
            model_id="model-x",
        )
        d = pv.to_dict()
        assert d["dim_vector_len"] == 36
        assert d["embed_vector_len"] == 768
        assert d["feature_vector_len"] == 10
        assert d["unified_vector_len"] == 36 + 768 + 10
        assert d["verdict"] == "SAFE"

    def test_prompt_vector_defaults_empty(self):
        """PromptVector with no signals should have empty vectors."""
        pv = PromptVector(prompt="test")
        assert pv.dimensional_scores == []
        assert pv.semantic_embedding == []
        assert pv.structural_features == []
        assert pv.unified_vector == []

    def test_rating_to_vector_all_present(self):
        """rating_to_vector should produce a 35-element normalized vector."""
        # Create a rating with scores for all 35 dimensions
        scores = [_make_score(d.id, 3) for d in ALL_DIMENSIONS]
        rating = _make_rating(scores=scores)
        mapper = EmbeddingMapper()
        vec = mapper.rating_to_vector(rating)
        # dimension_ids() returns 35 IDs
        assert len(vec) == 35
        # Score of 3 -> (3-1)/4 = 0.5
        assert all(abs(v - 0.5) < 1e-9 for v in vec)

    def test_rating_to_vector_missing_dims(self):
        """Missing dimensions should default to 0.5 ((3-1)/4)."""
        rating = _make_rating(scores=[_make_score("A1", 5)])
        mapper = EmbeddingMapper()
        vec = mapper.rating_to_vector(rating)
        assert len(vec) == 35
        # A1 should be (5-1)/4 = 1.0
        assert vec[0] == 1.0
        # All others should be (3-1)/4 = 0.5
        assert all(abs(v - 0.5) < 1e-9 for v in vec[1:])

    def test_from_ratings_with_verdicts(self):
        """from_ratings should produce parallel PromptVectors with verdicts."""
        scores1 = [_make_score("A1", 1)]
        scores2 = [_make_score("A1", 5)]
        r1 = _make_rating(scores=scores1)
        r2 = _make_rating(scores=scores2)
        mapper = EmbeddingMapper()
        vectors = mapper.from_ratings(
            [r1, r2],
            verdicts=["REFUSED", "COMPLIANT"],
        )
        assert len(vectors) == 2
        assert vectors[0].verdict == "REFUSED"
        assert vectors[1].verdict == "COMPLIANT"
        assert len(vectors[0].dimensional_scores) == 35

    def test_build_vector_no_rating(self):
        """build_vector with no rating should produce empty dimensional_scores."""
        mapper = EmbeddingMapper()
        vec = mapper.build_vector(
            prompt="hello",
            rating=None,
            semantic_embedding=[0.1, 0.2],
        )
        assert vec.dimensional_scores == []
        assert vec.semantic_embedding == [0.1, 0.2]

    def test_build_vector_with_rating(self):
        """build_vector with a rating should populate dimensional_scores."""
        scores = [_make_score("A1", 4)]
        rating = _make_rating(scores=scores)
        mapper = EmbeddingMapper()
        vec = mapper.build_vector(
            prompt="hello",
            rating=rating,
            response="world",
            verdict="SAFE",
            model_id="model-z",
        )
        assert len(vec.dimensional_scores) == 35
        assert vec.response == "world"
        assert vec.verdict == "SAFE"
        assert vec.model_id == "model-z"
