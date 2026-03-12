"""Tests for BaseGenerator, GeneratedTest, corridors, and BaseEvaluator."""

import pytest
import random

from src.generators.base_generator import BaseGenerator, GeneratedTest
from src.generators.corridors import (
    MigrationCorridor,
    CORRIDOR_REGISTRY,
    TAX_CORRIDORS,
    get_corridor,
    list_corridors,
    get_corridors_by_sector,
    get_corridors_by_destination,
)
from src.evaluation.base import (
    BaseEvaluator,
    EvaluationResult,
    EvaluatorProtocol,
    normalize_pattern_result,
    normalize_llm_judge_result,
)


# =====================================================================
# Corridor Registry Tests
# =====================================================================


class TestMigrationCorridor:
    def test_corridor_frozen(self):
        c = CORRIDOR_REGISTRY["PH-SA"]
        with pytest.raises(AttributeError):
            c.code = "XX"  # type: ignore[misc]

    def test_corridor_label(self):
        c = CORRIDOR_REGISTRY["PH-SA"]
        assert c.label == "Philippines -> Saudi Arabia"

    def test_corridor_to_dict(self):
        c = CORRIDOR_REGISTRY["PH-SA"]
        d = c.to_dict()
        assert d["code"] == "PH-SA"
        assert d["origin"] == "Philippines"
        assert d["destination"] == "Saudi Arabia"
        assert d["nationality"] == "Filipino"
        assert d["sector"] == "domestic work"
        assert "origin_language" in d

    def test_all_corridors_have_required_fields(self):
        for code, c in CORRIDOR_REGISTRY.items():
            assert c.code == code
            assert c.origin
            assert c.destination
            assert c.nationality
            assert c.sector
            assert c.origin_language


class TestCorridorRegistry:
    def test_has_corridors(self):
        assert len(CORRIDOR_REGISTRY) >= 15

    def test_get_corridor(self):
        c = get_corridor("PH-SA")
        assert c.origin == "Philippines"

    def test_get_corridor_unknown_raises(self):
        with pytest.raises(KeyError, match="Unknown corridor"):
            get_corridor("XX-YY")

    def test_list_corridors(self):
        codes = list_corridors()
        assert "PH-SA" in codes
        assert "NP-QA" in codes
        assert len(codes) >= 15

    def test_get_by_sector_domestic(self):
        domestic = get_corridors_by_sector("domestic")
        assert len(domestic) >= 5
        for c in domestic:
            assert "domestic" in c.sector.lower()

    def test_get_by_sector_construction(self):
        construction = get_corridors_by_sector("construction")
        assert len(construction) >= 2

    def test_get_by_sector_case_insensitive(self):
        assert get_corridors_by_sector("FISHING") == get_corridors_by_sector("fishing")

    def test_get_by_destination(self):
        uae = get_corridors_by_destination("UAE")
        assert len(uae) >= 2
        for c in uae:
            assert "UAE" in c.destination

    def test_tax_corridors(self):
        assert len(TAX_CORRIDORS) >= 10
        assert "US-CH" in TAX_CORRIDORS
        assert TAX_CORRIDORS["US-CH"]["origin"] == "United States"

    def test_kafala_corridors(self):
        kafala = [c for c in CORRIDOR_REGISTRY.values() if c.kafala_system]
        assert len(kafala) >= 5


# =====================================================================
# GeneratedTest Tests
# =====================================================================


class TestGeneratedTest:
    def test_basic_creation(self):
        t = GeneratedTest(id="test_001", prompt="hello", category="test")
        assert t.id == "test_001"
        assert t.prompt == "hello"
        assert t.category == "test"
        assert t.corridor == ""
        assert t.difficulty == "medium"

    def test_to_dict(self):
        t = GeneratedTest(
            id="t1", prompt="p", category="c",
            corridor="PH-SA", difficulty="hard",
            metadata={"key": "val"}, ilo_indicators=["debt_bondage"],
            generator="my_gen",
        )
        d = t.to_dict()
        assert d["id"] == "t1"
        assert d["corridor"] == "PH-SA"
        assert d["metadata"]["key"] == "val"
        assert d["ilo_indicators"] == ["debt_bondage"]
        assert d["generator"] == "my_gen"

    def test_defaults(self):
        t = GeneratedTest(id="t", prompt="p", category="c")
        assert t.metadata == {}
        assert t.ilo_indicators == []
        assert t.generator == ""


# =====================================================================
# BaseGenerator Tests
# =====================================================================


class _ConcreteGenerator(BaseGenerator):
    """Minimal concrete generator for testing."""
    NAME = "test_gen"
    DESCRIPTION = "A test generator"
    CATEGORIES = ["cat_a", "cat_b", "cat_c"]

    def _generate(self, category, corridor, **kwargs):
        cor = self.resolve_corridor(corridor)
        return GeneratedTest(
            id=self._next_id(),
            prompt=f"Test prompt for {category} in {cor.code}",
            category=category or "default",
            corridor=cor.code,
            difficulty="medium",
            metadata={"origin": cor.origin, **kwargs},
            ilo_indicators=["debt_bondage"],
        )


class TestBaseGenerator:
    def test_generate_single(self):
        gen = _ConcreteGenerator(seed=42)
        t = gen.generate(category="cat_a", corridor="PH-SA")
        assert isinstance(t, GeneratedTest)
        assert t.category == "cat_a"
        assert t.corridor == "PH-SA"
        assert t.generator == "test_gen"

    def test_generate_random_category(self):
        gen = _ConcreteGenerator(seed=42)
        t = gen.generate()
        assert t.category in gen.CATEGORIES

    def test_generate_random_corridor(self):
        gen = _ConcreteGenerator(seed=42)
        t = gen.generate(category="cat_a")
        assert t.corridor in CORRIDOR_REGISTRY

    def test_generate_batch(self):
        gen = _ConcreteGenerator(seed=42)
        batch = gen.generate_batch(count=5)
        assert len(batch) == 5
        for t in batch:
            assert isinstance(t, GeneratedTest)
            assert t.generator == "test_gen"

    def test_generate_batch_rotates_categories(self):
        gen = _ConcreteGenerator(seed=42)
        batch = gen.generate_batch(count=6)
        cats = [t.category for t in batch]
        assert cats[0] == "cat_a"
        assert cats[1] == "cat_b"
        assert cats[2] == "cat_c"
        assert cats[3] == "cat_a"

    def test_generate_batch_rotates_corridors(self):
        gen = _ConcreteGenerator(seed=42)
        batch = gen.generate_batch(count=20)
        corridors = {t.corridor for t in batch}
        assert len(corridors) >= 10

    def test_generate_batch_custom_categories(self):
        gen = _ConcreteGenerator(seed=42)
        batch = gen.generate_batch(count=4, categories=["cat_a"])
        for t in batch:
            assert t.category == "cat_a"

    def test_generate_batch_custom_corridors(self):
        gen = _ConcreteGenerator(seed=42)
        batch = gen.generate_batch(count=3, corridors=["PH-SA", "NP-QA"])
        codes = [t.corridor for t in batch]
        assert codes[0] == "PH-SA"
        assert codes[1] == "NP-QA"
        assert codes[2] == "PH-SA"

    def test_next_id_sequential(self):
        gen = _ConcreteGenerator(seed=42)
        t1 = gen.generate(category="cat_a", corridor="PH-SA")
        t2 = gen.generate(category="cat_a", corridor="PH-SA")
        # IDs should be different
        assert t1.id != t2.id

    def test_corridor_access(self):
        gen = _ConcreteGenerator()
        assert len(gen.corridors) >= 15
        c = gen.resolve_corridor("PH-SA")
        assert c.origin == "Philippines"

    def test_resolve_corridor_none(self):
        gen = _ConcreteGenerator(seed=42)
        c = gen.resolve_corridor(None)
        assert isinstance(c, MigrationCorridor)

    def test_resolve_corridor_invalid(self):
        gen = _ConcreteGenerator()
        with pytest.raises(KeyError):
            gen.resolve_corridor("XX-YY")

    def test_get_category_info(self):
        gen = _ConcreteGenerator()
        info = gen.get_category_info()
        assert "cat_a" in info
        assert "cat_b" in info

    def test_kwargs_passed_through(self):
        gen = _ConcreteGenerator(seed=42)
        t = gen.generate(category="cat_a", corridor="PH-SA", extra_key="extra_val")
        assert t.metadata.get("extra_key") == "extra_val"

    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            BaseGenerator()  # type: ignore[abstract]


# =====================================================================
# EvaluationResult Tests
# =====================================================================


class TestEvaluationResult:
    def test_basic_creation(self):
        r = EvaluationResult(is_harmful=True, harm_score=0.8, confidence=0.9)
        assert r.is_harmful is True
        assert r.harm_score == 0.8
        assert r.confidence == 0.9

    def test_defaults(self):
        r = EvaluationResult()
        assert r.is_harmful is None
        assert r.harm_score == 0.0
        assert r.confidence == 0.0
        assert r.rationale == ""
        assert r.evaluator == ""
        assert r.indicators == []
        assert r.metadata == {}
        assert r.timestamp

    def test_to_dict(self):
        r = EvaluationResult(
            is_harmful=False, harm_score=0.1, confidence=0.95,
            evaluator="test", rationale="Safe response",
        )
        d = r.to_dict()
        assert d["is_harmful"] is False
        assert d["harm_score"] == 0.1
        assert d["evaluator"] == "test"


# =====================================================================
# BaseEvaluator Tests
# =====================================================================


class _ConcreteEvaluator(BaseEvaluator):
    """Minimal concrete evaluator for testing.  Returns 0-10 scale scores."""
    NAME = "test_eval"

    def evaluate(self, response, **kwargs):
        is_harmful = "harmful" in response.lower()
        return {
            "is_harmful": is_harmful,
            "harm_score": 8.0 if is_harmful else 2.0,  # 0-10 scale
            "confidence": 85,
            "rationale": "test",
            "evaluator": self.NAME,
        }


class TestBaseEvaluator:
    def test_evaluate_returns_dict(self):
        ev = _ConcreteEvaluator()
        raw = ev.evaluate("safe response")
        assert isinstance(raw, dict)
        assert raw["is_harmful"] is False

    def test_evaluate_normalized(self):
        ev = _ConcreteEvaluator()
        r = ev.evaluate_normalized("harmful content here")
        assert isinstance(r, EvaluationResult)
        assert r.is_harmful is True
        assert r.harm_score == 0.8  # 8.0 / 10
        assert r.confidence == 0.85  # 85 / 100

    def test_evaluate_normalized_safe(self):
        ev = _ConcreteEvaluator()
        r = ev.evaluate_normalized("safe response")
        assert r.is_harmful is False
        assert r.harm_score == 0.2  # 2.0 / 10
        assert r.confidence == 0.85

    def test_normalize_clamps(self):
        ev = _ConcreteEvaluator()
        raw = {"harm_score": 15, "confidence": 200}
        r = ev._normalize(raw)
        assert r.harm_score <= 1.0
        assert r.confidence <= 1.0

    def test_normalize_handles_missing(self):
        ev = _ConcreteEvaluator()
        r = ev._normalize({})
        assert r.harm_score == 0.0
        assert r.confidence == 0.5  # 50 default / 100

    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            BaseEvaluator()  # type: ignore[abstract]


# =====================================================================
# Adapter Function Tests
# =====================================================================


class TestNormalizePatternResult:
    def test_normalizes_pattern_result(self):
        raw = {
            "is_harmful": True,
            "harm_score": 7.5,
            "confidence": 80,
            "rationale": "Detected harmful patterns: fee structuring",
            "pattern_matches": [
                {"pattern": "fee_structuring", "text": "break fees into", "category": "harmful", "weight": 0.8},
            ],
            "harmful_patterns_found": 1,
            "safe_patterns_found": 0,
            "evaluator": "pattern_evaluator",
        }
        r = normalize_pattern_result(raw)
        assert r.is_harmful is True
        assert r.harm_score == 0.75
        assert r.confidence == 0.8
        assert r.evaluator == "pattern_evaluator"
        assert "fee_structuring" in r.indicators
        assert r.metadata["harmful_patterns_found"] == 1

    def test_normalizes_safe_result(self):
        raw = {
            "is_harmful": False,
            "harm_score": 1.25,
            "confidence": 70,
            "rationale": "Safe",
            "pattern_matches": [],
            "harmful_patterns_found": 0,
            "safe_patterns_found": 3,
        }
        r = normalize_pattern_result(raw)
        assert r.is_harmful is False
        assert r.harm_score == 0.125
        assert r.indicators == []


class TestNormalizeLLMJudgeResult:
    def test_normalizes_judge_result(self):
        raw = {
            "is_harmful": True,
            "harm_score": 9,
            "confidence": 95,
            "rationale": "Provides detailed harmful guidance",
            "ilo_indicators_detected": ["debt_bondage", "deception"],
            "refusal_quality": "none",
            "evaluator": "llm_judge_anthropic",
            "evaluator_model": "claude-3-haiku",
            "evaluation_latency": 1.2,
            "evaluation_tokens": 500,
        }
        r = normalize_llm_judge_result(raw)
        assert r.is_harmful is True
        assert r.harm_score == 0.9
        assert r.confidence == 0.95
        assert "debt_bondage" in r.indicators
        assert r.metadata["refusal_quality"] == "none"
        assert r.metadata["evaluator_model"] == "claude-3-haiku"

    def test_normalizes_error_result(self):
        raw = {
            "is_harmful": None,
            "harm_score": None,
            "confidence": 0,
            "rationale": "Evaluation error: timeout",
            "ilo_indicators_detected": [],
            "refusal_quality": "unknown",
            "evaluator": "llm_judge_openai",
            "error": "timeout",
        }
        r = normalize_llm_judge_result(raw)
        assert r.is_harmful is None
        assert r.harm_score == 0.0
        assert r.confidence == 0.0


# =====================================================================
# Protocol Tests
# =====================================================================


class TestEvaluatorProtocol:
    def test_concrete_satisfies_protocol(self):
        ev = _ConcreteEvaluator()
        assert isinstance(ev, EvaluatorProtocol)

    def test_pattern_evaluator_satisfies_protocol(self):
        from src.evaluation.pattern_evaluator import PatternEvaluator
        ev = PatternEvaluator()
        assert isinstance(ev, EvaluatorProtocol)


# =====================================================================
# Integration: Generator __init__ exports
# =====================================================================


class TestGeneratorExports:
    def test_base_generator_exported(self):
        from src.generators import BaseGenerator, GeneratedTest
        assert BaseGenerator is not None
        assert GeneratedTest is not None

    def test_corridor_exports(self):
        from src.generators import (
            MigrationCorridor, CORRIDOR_REGISTRY, get_corridor,
            list_corridors, get_corridors_by_sector, get_corridors_by_destination,
        )
        assert len(CORRIDOR_REGISTRY) >= 15
        assert callable(get_corridor)

    def test_evaluation_exports(self):
        from src.evaluation import (
            BaseEvaluator, EvaluationResult, EvaluatorProtocol,
            normalize_pattern_result, normalize_llm_judge_result,
        )
        assert callable(normalize_pattern_result)

    def test_generate_all_still_works(self):
        """Ensure the registry-based generate_all hasn't broken."""
        from src.generators import generate_all
        tests = generate_all(count_per_generator=1)
        assert len(tests) >= 10
        for t in tests:
            assert "prompt" in t
            assert "category" in t
