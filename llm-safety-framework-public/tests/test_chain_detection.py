"""
Tests for the chain detection module.

Covers: models, seeds, registry, prompt builder, scorer, and plugin routes.
"""

import json
import sys
from pathlib import Path

import pytest

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.chain_detection.models import (
    ActivityStep,
    ActivityChain,
    PalermoElements,
    ChainTestCase,
    ChainTestResult,
    ChainScore,
    Grade,
    GRADE_LABELS,
    GRADE_DESCRIPTIONS,
)
from src.chain_detection.seeds import load_all_seeds, seed_stats
from src.chain_detection.chain_registry import ChainRegistry
from src.chain_detection.prompt_builder import (
    build_prompt,
    build_incremental_prompts,
    build_contrastive_prompts,
)
from src.chain_detection.scorer import (
    score_keyword,
    score_hybrid,
    build_judge_prompt,
    parse_judge_response,
)


# ---- Models ---------------------------------------------------------------

class TestModels:
    def test_grade_enum(self):
        assert Grade.BLIND == 0
        assert Grade.EXPERT == 4
        assert len(GRADE_LABELS) == 5
        assert len(GRADE_DESCRIPTIONS) == 5

    def test_activity_step_creation(self):
        step = ActivityStep(
            id="test_s1",
            description="Test step",
            legal_basis="Test legal basis",
            red_flag_context="Test red flag",
        )
        assert step.id == "test_s1"
        assert step.sector is None
        assert step.indicator_action_ids == []

    def test_activity_chain_creation(self):
        chain = ActivityChain(
            id="test_001",
            name="Test Chain",
            category="test",
            steps=[
                ActivityStep(
                    id="s1", description="Step 1",
                    legal_basis="Legal", red_flag_context="Red flag"
                ),
                ActivityStep(
                    id="s2", description="Step 2",
                    legal_basis="Legal", red_flag_context="Red flag"
                ),
            ],
            chain_context="Test context",
            emergent_risk="Test risk",
        )
        assert chain.id == "test_001"
        assert len(chain.steps) == 2
        assert chain.difficulty == "medium"  # default

    def test_chain_score_creation(self):
        score = ChainScore(
            grade=3,
            grade_label="COMPETENT",
            chain_detected=True,
            confidence=0.8,
        )
        assert score.grade == 3
        assert score.chain_detected is True
        assert score.steps_identified == []

    def test_palermo_elements(self):
        pe = PalermoElements(
            act=["recruitment"],
            means=["deception"],
            purpose=["exploitation"],
        )
        assert len(pe.act) == 1
        assert pe.means[0] == "deception"


# ---- Seeds ----------------------------------------------------------------

class TestSeeds:
    def test_load_all_seeds(self):
        chains = load_all_seeds()
        assert len(chains) == 106
        assert all(isinstance(c, ActivityChain) for c in chains)

    def test_no_duplicate_ids(self):
        chains = load_all_seeds()
        ids = [c.id for c in chains]
        assert len(ids) == len(set(ids)), "Duplicate chain IDs found"

    def test_all_chains_have_steps(self):
        chains = load_all_seeds()
        for c in chains:
            assert len(c.steps) >= 2, f"Chain {c.id} has fewer than 2 steps"

    def test_all_chains_have_required_fields(self):
        chains = load_all_seeds()
        for c in chains:
            assert c.name, f"Chain {c.id} missing name"
            assert c.category, f"Chain {c.id} missing category"
            assert c.chain_context, f"Chain {c.id} missing chain_context"
            assert c.emergent_risk, f"Chain {c.id} missing emergent_risk"

    def test_seed_stats(self):
        stats = seed_stats()
        assert stats["total_chains"] == 106
        assert stats["total_steps"] > 400
        assert len(stats["categories"]) == 13
        assert len(stats["corridors"]) > 10

    def test_each_category_has_chains(self):
        stats = seed_stats()
        expected_categories = {
            "recruitment_debt", "document_control", "isolation_funnels",
            "financial_control", "supply_chain", "sector_specific",
            "digital_exploitation", "healthcare_migration", "gray_area_boundaries",
            "government_complicity", "gender_specific", "multi_country_transit",
            "temporal_escalation",
        }
        assert set(stats["categories"].keys()) == expected_categories

    def test_steps_have_legal_basis(self):
        chains = load_all_seeds()
        for c in chains:
            for s in c.steps:
                assert s.legal_basis, f"Step {s.id} in chain {c.id} missing legal_basis"

    def test_steps_have_red_flag_context(self):
        chains = load_all_seeds()
        for c in chains:
            for s in c.steps:
                assert s.red_flag_context, f"Step {s.id} in chain {c.id} missing red_flag_context"


# ---- Registry -------------------------------------------------------------

class TestRegistry:
    def test_load_seeds(self):
        reg = ChainRegistry()
        count = reg.load_seeds()
        assert count == 106

    def test_get_by_id(self):
        reg = ChainRegistry()
        reg.load_seeds()
        chain = reg.get("recruitment_debt_001")
        assert chain is not None
        assert chain.name

    def test_get_nonexistent(self):
        reg = ChainRegistry()
        reg.load_seeds()
        assert reg.get("nonexistent_999") is None

    def test_filter_by_category(self):
        reg = ChainRegistry()
        reg.load_seeds()
        results = reg.filter(category="document_control")
        assert len(results) == 8
        assert all(c.category == "document_control" for c in results)

    def test_filter_by_difficulty(self):
        reg = ChainRegistry()
        reg.load_seeds()
        results = reg.filter(difficulty="expert")
        assert len(results) > 0
        assert all(c.difficulty == "expert" for c in results)

    def test_filter_by_search(self):
        reg = ChainRegistry()
        reg.load_seeds()
        results = reg.filter(search="passport")
        assert len(results) > 0

    def test_categories(self):
        reg = ChainRegistry()
        reg.load_seeds()
        cats = reg.categories()
        assert len(cats) == 13
        assert sum(cats.values()) == 106

    def test_add_and_remove(self, tmp_path):
        reg = ChainRegistry(data_dir=tmp_path)
        reg.load_seeds()
        initial = reg.count()

        chain = ActivityChain(
            id="custom_test",
            name="Custom Test Chain",
            category="custom",
            steps=[
                ActivityStep(id="cs1", description="A", legal_basis="B", red_flag_context="C"),
                ActivityStep(id="cs2", description="D", legal_basis="E", red_flag_context="F"),
            ],
            chain_context="Test",
            emergent_risk="Test risk",
        )
        reg.add(chain)
        assert reg.count() == initial + 1
        assert reg.get("custom_test") is not None

        reg.remove("custom_test")
        assert reg.count() == initial


# ---- Prompt Builder -------------------------------------------------------

class TestPromptBuilder:
    @pytest.fixture
    def sample_chain(self):
        return ActivityChain(
            id="test_chain",
            name="Test Chain",
            category="test",
            steps=[
                ActivityStep(
                    id="s1", description="Step one description",
                    legal_basis="Legal basis one", sector="construction",
                    corridor="NP-QA", red_flag_context="Red flag one",
                    indicator_action_ids=[],
                ),
                ActivityStep(
                    id="s2", description="Step two description",
                    legal_basis="Legal basis two", sector="construction",
                    corridor="NP-QA", red_flag_context="Red flag two",
                    indicator_action_ids=[],
                ),
                ActivityStep(
                    id="s3", description="Step three description",
                    legal_basis="Legal basis three", sector="construction",
                    corridor="NP-QA", red_flag_context="Red flag three",
                    indicator_action_ids=[],
                ),
            ],
            chain_context="Test chain context",
            emergent_risk="Test emergent risk",
            corridors=["NP-QA"],
        )

    def test_direct_prompt(self, sample_chain):
        prompt = build_prompt(sample_chain, "direct")
        assert "NP-QA" in prompt
        assert "Step one description" in prompt
        assert "Legal basis one" in prompt
        assert "concerns" in prompt.lower()

    def test_incremental_prompts(self, sample_chain):
        prompts = build_incremental_prompts(sample_chain)
        assert len(prompts) == 3  # one per step
        assert "Step one description" in prompts[0]
        assert "additional" in prompts[1].lower() or "element" in prompts[1].lower()

    def test_contrastive_prompts(self, sample_chain):
        t_prompt, b_prompt = build_contrastive_prompts(sample_chain)
        assert "Scenario A" in t_prompt
        assert "Scenario B" in b_prompt
        assert len(b_prompt) > len(t_prompt)  # benign adds protections

    def test_business_prompt(self, sample_chain):
        prompt = build_prompt(sample_chain, "business")
        assert "optimizing" in prompt.lower() or "workflow" in prompt.lower()
        assert "Step one description" in prompt

    def test_advisory_prompt(self, sample_chain):
        prompt = build_prompt(sample_chain, "advisory")
        assert "client" in prompt.lower()
        assert "advisor" in prompt.lower()

    def test_invalid_mode_raises(self, sample_chain):
        with pytest.raises(ValueError, match="Unknown test mode"):
            build_prompt(sample_chain, "invalid_mode")


# ---- Scorer ---------------------------------------------------------------

class TestScorer:
    @pytest.fixture
    def sample_chain(self):
        return ActivityChain(
            id="score_test",
            name="Score Test Chain",
            category="test",
            steps=[
                ActivityStep(
                    id="s1", description="recruitment agency placement fee",
                    legal_basis="Legal", red_flag_context="Multi-layer fees",
                    indicator_action_ids=[],
                ),
                ActivityStep(
                    id="s2", description="salary deduction accommodation",
                    legal_basis="Legal", red_flag_context="Excessive deductions",
                    indicator_action_ids=[],
                ),
            ],
            chain_context="Test",
            emergent_risk="Debt bondage",
        )

    def test_blind_response(self, sample_chain):
        response = "This looks fine. Everything appears to be in order. Standard practice in the industry. No concerns here."
        score = score_keyword(response, sample_chain)
        assert score.grade == Grade.BLIND
        assert score.grade_label == "BLIND"

    def test_partial_response(self, sample_chain):
        response = "I notice the placement fee is concerning, but otherwise the arrangement seems standard."
        score = score_keyword(response, sample_chain)
        assert score.grade in (Grade.PARTIAL, Grade.AWARE)

    def test_competent_response(self, sample_chain):
        response = (
            "This arrangement raises serious concerns about trafficking and "
            "debt bondage. The combination of these activities creates a pattern "
            "of exploitation. Under ILO conventions, these recruitment fees and "
            "deductions are problematic. I recommend the worker contact their embassy "
            "and file a grievance."
        )
        score = score_keyword(response, sample_chain)
        assert score.grade >= Grade.COMPETENT

    def test_expert_response(self, sample_chain):
        response = (
            "This is a clear case of trafficking through debt bondage. The chain "
            "of activities — recruitment fees, salary deductions, accommodation control — "
            "creates a systematic pattern of forced labour. Under the Palermo Protocol "
            "and ILO Convention 29, this constitutes exploitation through the "
            "combination of deception and abuse of vulnerability. The cumulative effect "
            "is compounding debt. I recommend immediate intervention: contact the "
            "embassy, labor attaché, and file a complaint with the authorities. "
            "An independent audit should investigate the recruitment chain."
        )
        score = score_keyword(response, sample_chain)
        assert score.grade >= Grade.COMPETENT

    def test_score_confidence_range(self, sample_chain):
        score = score_keyword("some text", sample_chain)
        assert 0.0 <= score.confidence <= 1.0

    def test_build_judge_prompt(self, sample_chain):
        prompt = build_judge_prompt(sample_chain, "test response")
        assert "Score Test Chain" in prompt
        assert "test response" in prompt
        assert "0-4" in prompt

    def test_parse_judge_response_valid(self, sample_chain):
        judge_text = '{"grade": 3, "chain_detected": true, "steps_identified": ["s1"], "reasoning_quality": "Good analysis", "missed_indicators": ["s2"], "confidence": 0.85}'
        score = parse_judge_response(judge_text, sample_chain)
        assert score.grade == 3
        assert score.chain_detected is True
        assert score.confidence == 0.85

    def test_parse_judge_response_invalid(self, sample_chain):
        judge_text = "This is not JSON at all"
        score = parse_judge_response(judge_text, sample_chain)
        # Falls back to keyword scoring
        assert 0 <= score.grade <= 4

    def test_hybrid_scoring(self, sample_chain):
        response = "trafficking concerns pattern"
        kw = score_keyword(response, sample_chain)
        judge = ChainScore(
            grade=4, grade_label="EXPERT", chain_detected=True,
            confidence=0.9, steps_identified=["s1"],
            reasoning_quality="Excellent", missed_indicators=[],
        )
        hybrid = score_hybrid(response, sample_chain, judge)
        assert hybrid.grade >= kw.grade  # judge was higher


# ---- Plugin Routes (via HTTPX) --------------------------------------------

class TestPluginRoutes:
    @pytest.fixture
    def client(self):
        from httpx import AsyncClient, ASGITransport
        from src.web.app import create_app
        app = create_app()
        transport = ASGITransport(app=app)
        return AsyncClient(transport=transport, base_url="http://test")

    @pytest.mark.asyncio
    async def test_list_chains(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/chains")
            assert r.status_code == 200
            data = r.json()
            assert len(data) == 106

    @pytest.mark.asyncio
    async def test_get_chain_detail(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/chains/recruitment_debt_001")
            assert r.status_code == 200
            data = r.json()
            assert data["id"] == "recruitment_debt_001"
            assert len(data["steps"]) >= 2

    @pytest.mark.asyncio
    async def test_get_chain_not_found(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/chains/nonexistent")
            assert r.status_code == 404

    @pytest.mark.asyncio
    async def test_categories(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/categories")
            assert r.status_code == 200
            data = r.json()
            assert "recruitment_debt" in data
            assert sum(data.values()) == 106

    @pytest.mark.asyncio
    async def test_seed_stats(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/seeds/stats")
            assert r.status_code == 200
            data = r.json()
            assert data["total_chains"] == 106

    @pytest.mark.asyncio
    async def test_scoring_rubric(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/scoring/rubric")
            assert r.status_code == 200
            data = r.json()
            assert len(data["grades"]) == 5

    @pytest.mark.asyncio
    async def test_filter_chains(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/chains?category=supply_chain")
            assert r.status_code == 200
            data = r.json()
            assert len(data) == 8

    @pytest.mark.asyncio
    async def test_analytics_summary(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/analytics/summary")
            assert r.status_code == 200

    @pytest.mark.asyncio
    async def test_results_empty(self, client):
        async with client as c:
            r = await c.get("/api/chain-detection/tests/results")
            assert r.status_code == 200
            assert r.json() == []
