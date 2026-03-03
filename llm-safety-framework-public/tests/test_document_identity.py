"""
Tests for document_identity, seed_loader, health tracker, and auto-escalation.
"""

import json
import math
import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.scraper.document_identity import (
    DocumentIndex,
    canonical_url,
    content_id,
    hamming_distance,
    is_near_duplicate,
    simhash,
)
from src.scraper.health import HealthTracker, SourceHealth
from src.scraper.seed_loader import is_seeded, load_seeds
from src.scraper.seeds import SEED_FACTS


# =============================================================================
# URL Canonicalization
# =============================================================================

class TestURLCanonicalization:
    """Test canonical_url() normalization."""

    def test_strip_utm_params(self):
        url = "https://example.com/page?utm_source=google&utm_medium=cpc&real=1"
        result = canonical_url(url)
        assert "utm_source" not in result
        assert "utm_medium" not in result
        assert "real=1" in result

    def test_normalize_scheme(self):
        result = canonical_url("http://example.com/page")
        assert result.startswith("https://")

    def test_lowercase_hostname(self):
        result = canonical_url("https://EXAMPLE.COM/Page")
        assert "example.com" in result
        assert "/Page" in result  # path case preserved

    def test_remove_trailing_slash(self):
        result = canonical_url("https://example.com/page/")
        assert result == "https://example.com/page"

    def test_keep_root_slash(self):
        result = canonical_url("https://example.com/")
        assert result == "https://example.com/"

    def test_remove_fragment(self):
        result = canonical_url("https://example.com/page#section1")
        assert "#" not in result

    def test_sort_query_params(self):
        result = canonical_url("https://example.com/page?z=1&a=2")
        assert "a=2" in result
        assert result.index("a=2") < result.index("z=1")

    def test_strip_tracking_params(self):
        url = "https://example.com?fbclid=abc&gclid=xyz&page=1"
        result = canonical_url(url)
        assert "fbclid" not in result
        assert "gclid" not in result
        assert "page=1" in result

    def test_idempotent(self):
        url = "https://example.com/page?a=1&b=2"
        result1 = canonical_url(url)
        result2 = canonical_url(result1)
        assert result1 == result2

    def test_remove_default_port(self):
        result = canonical_url("https://example.com:443/page")
        assert ":443" not in result


# =============================================================================
# SimHash
# =============================================================================

class TestSimHash:
    """Test simhash() fingerprinting and hamming distance."""

    def test_identical_text_zero_distance(self):
        text = "The quick brown fox jumps over the lazy dog"
        h1 = simhash(text)
        h2 = simhash(text)
        assert h1 == h2
        assert hamming_distance(h1, h2) == 0

    def test_near_duplicate_detection(self):
        # Use longer texts — more representative of real documents
        text1 = "ILO Convention 29 on forced labour defines forced labour as work exacted under menace of penalty and for which the person has not offered voluntarily"
        text2 = "ILO Convention 29 on forced labour defines forced labour as work exacted under threat of penalty and for which the person has not offered voluntarily"
        h1 = simhash(text1)
        h2 = simhash(text2)
        assert is_near_duplicate(h1, h2)

    def test_different_text_above_threshold(self):
        text1 = "The Philippine government regulates overseas employment through the DMW and POEA agencies for migrant worker protection"
        text2 = "Quantum computing uses qubits and entanglement to perform parallel calculations exponentially faster than classical computers"
        h1 = simhash(text1)
        h2 = simhash(text2)
        # Different topics should not be near-duplicates
        assert not is_near_duplicate(h1, h2)

    def test_empty_text(self):
        h = simhash("")
        assert h == 0

    def test_short_text(self):
        h = simhash("hello")
        assert isinstance(h, int)
        assert h >= 0


# =============================================================================
# Content ID
# =============================================================================

class TestContentId:
    """Test content_id() generation."""

    def test_deterministic(self):
        text = "Some document content about migrant workers"
        id1 = content_id(text)
        id2 = content_id(text)
        assert id1 == id2
        assert id1.startswith("doc_")

    def test_whitespace_normalization(self):
        text1 = "Some   document\n\ncontent"
        text2 = "Some document content"
        assert content_id(text1) == content_id(text2)

    def test_different_content_different_id(self):
        id1 = content_id("Document about trafficking")
        id2 = content_id("Document about labor laws")
        assert id1 != id2

    def test_case_insensitive(self):
        id1 = content_id("ILO Convention")
        id2 = content_id("ilo convention")
        assert id1 == id2


# =============================================================================
# Document Index
# =============================================================================

class TestDocumentIndex:
    """Test DocumentIndex persistence and dedup."""

    def test_register_new_document(self, tmp_path):
        idx = DocumentIndex(data_dir=str(tmp_path))
        cid, is_new, near_dup = idx.register(
            "https://example.com/doc1", "This is document content about forced labour",
            source_id="test-source",
        )
        assert is_new is True
        assert near_dup is None
        assert cid.startswith("doc_")

    def test_detect_exact_duplicate(self, tmp_path):
        idx = DocumentIndex(data_dir=str(tmp_path))
        text = "This is document content about forced labour indicators and definitions"
        idx.register("https://example.com/doc1", text, source_id="source-a")
        cid, is_new, near_dup = idx.register(
            "https://other.com/doc1", text, source_id="source-b"
        )
        assert is_new is False
        assert near_dup is not None  # cross-source dedup

    def test_version_history(self, tmp_path):
        idx = DocumentIndex(data_dir=str(tmp_path))
        url = "https://example.com/doc1"
        idx.register(url, "Version one content about trafficking laws", source_id="s1")
        idx.register(url, "Version two content about trafficking laws updated", source_id="s1")
        history = idx.get_version_history(url)
        assert len(history) == 2

    def test_persistence(self, tmp_path):
        idx1 = DocumentIndex(data_dir=str(tmp_path))
        idx1.register("https://example.com/doc1", "Some content for persistence test", source_id="s1")
        idx1.save()

        idx2 = DocumentIndex(data_dir=str(tmp_path))
        assert idx2.size == 1
        entry = idx2.get_entry("https://example.com/doc1")
        assert entry is not None
        assert entry["source_ids"] == ["s1"]

    def test_stats(self, tmp_path):
        idx = DocumentIndex(data_dir=str(tmp_path))
        idx.register("https://example.com/doc1", "Content A for stats test", source_id="s1")
        idx.register("https://example.com/doc2", "Content B for stats test", source_id="s1")
        stats = idx.stats()
        assert stats["indexed_urls"] == 2
        assert stats["unique_content"] == 2
        assert stats["total_versions"] == 2

    def test_find_near_duplicates(self, tmp_path):
        idx = DocumentIndex(data_dir=str(tmp_path))
        text1 = "ILO Convention 29 on forced labour defines forced labour as work exacted under menace of penalty and for which the person has not offered voluntarily"
        text2 = "ILO Convention 29 on forced labour defines forced labour as work exacted under threat of penalty and for which the person has not offered voluntarily"
        idx.register("https://example.com/doc1", text1, source_id="s1")
        results = idx.find_near_duplicates(text2)
        assert len(results) >= 1


# =============================================================================
# Seed Facts
# =============================================================================

class TestSeedFacts:
    """Test seed fact data integrity."""

    def test_seed_facts_not_empty(self):
        assert len(SEED_FACTS) >= 600

    def test_all_facts_have_type(self):
        for fact in SEED_FACTS:
            assert "type" in fact, f"Fact missing type: {fact.get('title', 'unknown')}"

    def test_expected_categories(self):
        categories = {f["type"] for f in SEED_FACTS}
        assert "law" in categories
        assert "fee_cap" in categories
        assert "statistic" in categories
        assert "advisory" in categories
        assert "bilateral_agreement" in categories
        assert "regulation_change" in categories

    def test_new_fact_types_present(self):
        categories = {f["type"] for f in SEED_FACTS}
        assert "case_study" in categories
        assert "court_ruling" in categories
        assert "contact" in categories
        assert "penalty" in categories
        assert "recruitment_violation" in categories

    def test_all_15_kb_categories_covered(self):
        """All 15 KnowledgeBase fact types should have at least one seed."""
        categories = {f["type"] for f in SEED_FACTS}
        expected = {
            "law", "fee_cap", "bilateral_agreement", "case_study",
            "statistic", "advisory", "regulation_change", "contact",
            "court_ruling", "embassy_notice", "recruitment_violation",
            "policy_update", "training_material", "complaint", "penalty",
        }
        missing = expected - categories
        assert not missing, f"Missing KB categories in seeds: {missing}"

    def test_new_topic_files_have_sufficient_facts(self):
        """Each new topic file should have >= 15 facts."""
        from src.scraper.seeds.supply_chain import SUPPLY_CHAIN_FACTS
        from src.scraper.seeds.digital_exploitation import DIGITAL_EXPLOITATION_FACTS
        from src.scraper.seeds.debt_bondage_mechanics import DEBT_BONDAGE_FACTS
        from src.scraper.seeds.wage_protection import WAGE_PROTECTION_FACTS
        from src.scraper.seeds.visa_systems import VISA_SYSTEM_FACTS
        from src.scraper.seeds.gender_exploitation import GENDER_EXPLOITATION_FACTS
        from src.scraper.seeds.child_labour import CHILD_LABOUR_FACTS
        from src.scraper.seeds.embassy_notices import EMBASSY_NOTICE_FACTS
        from src.scraper.seeds.training_materials import TRAINING_MATERIAL_FACTS
        from src.scraper.seeds.complaints import COMPLAINT_FACTS
        from src.scraper.seeds.policy_updates import POLICY_UPDATE_FACTS
        from src.scraper.seeds.repatriation import REPATRIATION_FACTS

        for name, facts in [
            ("supply_chain", SUPPLY_CHAIN_FACTS),
            ("digital_exploitation", DIGITAL_EXPLOITATION_FACTS),
            ("debt_bondage_mechanics", DEBT_BONDAGE_FACTS),
            ("wage_protection", WAGE_PROTECTION_FACTS),
            ("visa_systems", VISA_SYSTEM_FACTS),
            ("gender_exploitation", GENDER_EXPLOITATION_FACTS),
            ("child_labour", CHILD_LABOUR_FACTS),
            ("embassy_notices", EMBASSY_NOTICE_FACTS),
            ("training_materials", TRAINING_MATERIAL_FACTS),
            ("complaints", COMPLAINT_FACTS),
            ("policy_updates", POLICY_UPDATE_FACTS),
            ("repatriation", REPATRIATION_FACTS),
        ]:
            assert len(facts) >= 15, f"{name} has only {len(facts)} facts (need >= 15)"

    def test_at_least_14_fact_types(self):
        categories = {f["type"] for f in SEED_FACTS}
        assert len(categories) >= 14

    def test_ilo_indicators_complete(self):
        """All 11 ILO forced labour indicators should be present."""
        indicator_facts = [f for f in SEED_FACTS if f.get("indicator")]
        assert len(indicator_facts) == 11

    def test_fee_caps_have_corridors(self):
        fee_caps = [f for f in SEED_FACTS if f["type"] == "fee_cap"]
        for fc in fee_caps:
            assert "corridor" in fc, f"Fee cap missing corridor: {fc.get('title', '')}"
            assert "amount" in fc, f"Fee cap missing amount: {fc.get('title', '')}"

    def test_laws_have_jurisdiction(self):
        laws = [f for f in SEED_FACTS if f["type"] == "law"]
        for law in laws:
            assert "jurisdiction" in law

    def test_at_least_30_corridors(self):
        corridors = {f.get("corridor") for f in SEED_FACTS if f.get("corridor")}
        assert len(corridors) >= 30

    def test_court_rulings_have_required_fields(self):
        rulings = [f for f in SEED_FACTS if f["type"] == "court_ruling"]
        assert len(rulings) >= 30
        for r in rulings:
            assert "court" in r, f"Court ruling missing court: {r.get('title', '')}"
            assert "year" in r, f"Court ruling missing year: {r.get('title', '')}"

    def test_contacts_have_required_fields(self):
        contacts = [f for f in SEED_FACTS if f["type"] == "contact"]
        assert len(contacts) >= 15
        for c in contacts:
            assert "organization" in c, f"Contact missing organization: {c.get('title', '')}"
            assert "contact_type" in c, f"Contact missing contact_type: {c.get('title', '')}"

    def test_penalties_have_required_fields(self):
        penalties = [f for f in SEED_FACTS if f["type"] == "penalty"]
        assert len(penalties) >= 15
        for p in penalties:
            assert "offense" in p, f"Penalty missing offense: {p.get('title', '')}"
            assert "amount" in p, f"Penalty missing amount: {p.get('title', '')}"


# =============================================================================
# Seed Loader
# =============================================================================

class TestSeedLoader:
    """Test seed loading into KB."""

    def test_load_seeds_into_empty_kb(self, tmp_path):
        from src.scraper.knowledge_base import KnowledgeBase
        from src.scraper.seed_pruner import load_pruned_seeds

        kb = KnowledgeBase(data_dir=str(tmp_path))
        assert len(kb._facts) == 0

        added = load_seeds(kb)
        pruned_count = len(load_pruned_seeds())
        assert added == pruned_count
        assert len(kb._facts) == pruned_count

    def test_idempotent(self, tmp_path):
        from src.scraper.knowledge_base import KnowledgeBase

        kb = KnowledgeBase(data_dir=str(tmp_path))
        added1 = load_seeds(kb)
        added2 = load_seeds(kb)
        assert added1 > 0
        assert added2 == 0  # no new facts added
        assert len(kb._facts) == added1

    def test_is_seeded_detection(self, tmp_path):
        from src.scraper.knowledge_base import KnowledgeBase

        kb = KnowledgeBase(data_dir=str(tmp_path))
        assert is_seeded(kb) is False
        load_seeds(kb)
        assert is_seeded(kb) is True

    def test_seed_facts_queryable(self, tmp_path):
        from src.scraper.knowledge_base import KnowledgeBase

        kb = KnowledgeBase(data_dir=str(tmp_path))
        load_seeds(kb)

        laws = kb.query(category="law")
        assert len(laws) > 0

        fee_caps = kb.query(category="fee_cap")
        assert len(fee_caps) > 0

        court_rulings = kb.query(category="court_ruling")
        assert len(court_rulings) > 0

        contacts = kb.query(category="contact")
        assert len(contacts) > 0

        penalties = kb.query(category="penalty")
        assert len(penalties) > 0

        # Test corridor filter
        ph_hk = kb.query(corridor="PH-HK")
        assert len(ph_hk) > 0

        # Test multiple corridors
        bd_my = kb.query(corridor="BD-MY")
        assert len(bd_my) > 0

    def test_all_15_categories_queryable(self, tmp_path):
        from src.scraper.knowledge_base import KnowledgeBase

        kb = KnowledgeBase(data_dir=str(tmp_path))
        load_seeds(kb)

        for cat in [
            "law", "fee_cap", "bilateral_agreement", "case_study",
            "statistic", "advisory", "regulation_change", "contact",
            "court_ruling", "embassy_notice", "recruitment_violation",
            "policy_update", "training_material", "complaint", "penalty",
        ]:
            results = kb.query(category=cat)
            assert len(results) > 0, f"No results for category '{cat}'"


# =============================================================================
# Source Health
# =============================================================================

class TestSourceHealth:
    """Test HealthTracker."""

    def test_record_success(self, tmp_path):
        tracker = HealthTracker(data_dir=str(tmp_path))
        tracker.record_success("ilo-forced-labour", stealth_level_used=1)
        h = tracker.get_health("ilo-forced-labour")
        assert h.successes == 1
        assert h.total_fetches == 1
        assert h.consecutive_failures == 0
        assert h.success_rate == 1.0

    def test_record_failure(self, tmp_path):
        tracker = HealthTracker(data_dir=str(tmp_path))
        tracker.record_failure("iom-publications", status_code=403, stealth_level_used=0)
        h = tracker.get_health("iom-publications")
        assert h.failures == 1
        assert h.consecutive_failures == 1
        assert h.success_rate == 0.0

    def test_consecutive_failures(self, tmp_path):
        tracker = HealthTracker(data_dir=str(tmp_path))
        tracker.record_failure("test-source", status_code=403)
        tracker.record_failure("test-source", status_code=403)
        tracker.record_failure("test-source", status_code=403)
        h = tracker.get_health("test-source")
        assert h.consecutive_failures == 3
        tracker.record_success("test-source")
        h = tracker.get_health("test-source")
        assert h.consecutive_failures == 0

    def test_recommended_stealth(self, tmp_path):
        tracker = HealthTracker(data_dir=str(tmp_path))
        # Source always needing level 2
        for _ in range(5):
            tracker.record_success("high-stealth", stealth_level_used=2)
        rec = tracker.get_recommended_stealth("high-stealth")
        assert rec >= 2

    def test_recommended_stealth_bump_on_low_success(self, tmp_path):
        tracker = HealthTracker(data_dir=str(tmp_path))
        tracker.record_success("flaky", stealth_level_used=1)
        tracker.record_failure("flaky", status_code=403, stealth_level_used=1)
        tracker.record_failure("flaky", status_code=403, stealth_level_used=1)
        tracker.record_failure("flaky", status_code=403, stealth_level_used=1)
        # 25% success rate — should recommend bumping up
        rec = tracker.get_recommended_stealth("flaky")
        assert rec >= 2

    def test_persistence(self, tmp_path):
        tracker1 = HealthTracker(data_dir=str(tmp_path))
        tracker1.record_success("test-source", stealth_level_used=1)
        tracker1.save()

        tracker2 = HealthTracker(data_dir=str(tmp_path))
        h = tracker2.get_health("test-source")
        assert h.successes == 1

    def test_summary(self, tmp_path):
        tracker = HealthTracker(data_dir=str(tmp_path))
        tracker.record_success("source-a", stealth_level_used=0)
        tracker.record_failure("source-b", status_code=403, stealth_level_used=1)
        summary = tracker.summary()
        assert len(summary) == 2
        assert summary[0]["source_id"] == "source-a"
        assert summary[0]["success_rate"] == 1.0


# =============================================================================
# Auto-Escalation (unit logic, not full fetch)
# =============================================================================

class TestAutoEscalation:
    """Test that the auto-escalation status set is correct."""

    def test_escalation_statuses(self):
        from src.scraper.fetcher import _ESCALATION_STATUSES
        assert 403 in _ESCALATION_STATUSES
        assert 429 in _ESCALATION_STATUSES
        assert 503 in _ESCALATION_STATUSES
        assert 200 not in _ESCALATION_STATUSES
        assert 404 not in _ESCALATION_STATUSES


# =============================================================================
# Fixed URLs in DEFAULT_SOURCES
# =============================================================================

class TestFixedURLDefaults:
    """Test that updated source URLs are present."""

    def test_new_sources_exist(self):
        from src.scraper.sources import DEFAULT_SOURCES
        ids = {s.id for s in DEFAULT_SOURCES}
        assert "ilo-c029-text" in ids
        assert "palermo-protocol" in ids
        assert "ilo-global-estimates" in ids

    def test_us_tip_report_url_has_trailing_slash(self):
        from src.scraper.sources import DEFAULT_SOURCES
        tip = next(s for s in DEFAULT_SOURCES if s.id == "us-tip-report")
        assert tip.url.endswith("/")

    def test_hk_labour_dept_specific_page(self):
        from src.scraper.sources import DEFAULT_SOURCES
        hk = next(s for s in DEFAULT_SOURCES if s.id == "hk-labour-dept")
        assert "iwFDH" in hk.url or "fdh" in hk.url.lower() or "plan" in hk.url


# =============================================================================
# Integration: Scheduler auto-seeds KB
# =============================================================================

class TestSchedulerAutoSeed:
    """Test that ScrapeOrchestrator auto-seeds KB."""

    def test_auto_seed_on_empty_kb(self, tmp_path):
        from src.scraper.scheduler import ScrapeOrchestrator
        orch = ScrapeOrchestrator(data_dir=str(tmp_path))
        # KB should be auto-seeded
        assert len(orch.kb._facts) >= 50
        assert is_seeded(orch.kb)

    def test_ensure_seeded_idempotent(self, tmp_path):
        from src.scraper.scheduler import ScrapeOrchestrator
        orch = ScrapeOrchestrator(data_dir=str(tmp_path))
        count1 = len(orch.kb._facts)
        added = orch.ensure_seeded()
        assert added == 0  # already seeded
        assert len(orch.kb._facts) == count1
