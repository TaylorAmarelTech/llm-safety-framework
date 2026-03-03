"""Tests for the Document Intelligence Agent (scraper package)."""

import json
import pytest
from pathlib import Path

from src.scraper.sources import SourceConfig, SourceRegistry, DEFAULT_SOURCES, TIER_LABELS
from src.scraper.fetcher import DocumentFetcher, Document
from src.scraper.extractor import FactExtractor, ExtractionResult, FACT_TYPES
from src.scraper.knowledge_base import KnowledgeBase
from src.scraper.politeness import PolitenessPolicy
from src.scraper.retry import RetryPolicy, RetryableError
from src.scraper.change_detection import ChangeDetector, PageFingerprint
from src.scraper.feed_parser import FeedParser, FeedEntry
from src.scraper.browser import HeadlessBrowser


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Create temp data directory for scraper tests."""
    data_dir = tmp_path / "scraper"
    data_dir.mkdir()
    (data_dir / "documents").mkdir()
    (data_dir / "extractions").mkdir()
    (data_dir / "jobs").mkdir()
    return str(data_dir)


# =============================================================================
# Source Registry Tests
# =============================================================================

class TestSourceRegistry:
    def test_default_sources_loaded(self):
        """DEFAULT_SOURCES contains 50+ sources across 7 tiers."""
        assert len(DEFAULT_SOURCES) >= 50
        tiers = set(s.tier for s in DEFAULT_SOURCES)
        assert tiers == {1, 2, 3, 4, 5, 6, 7}

    def test_registry_seeds_defaults(self, tmp_data_dir):
        """Registry seeds sources.json from defaults on first load."""
        reg = SourceRegistry(data_dir=tmp_data_dir)
        sources = reg.list_sources()
        assert len(sources) >= 50

    def test_registry_crud(self, tmp_data_dir):
        """Create, read, update, delete a source."""
        reg = SourceRegistry(data_dir=tmp_data_dir)

        # Create
        new_src = SourceConfig(id="test-source", name="Test", tier=5, url="https://example.com")
        reg.create(new_src)
        assert reg.get("test-source") is not None

        # Update
        reg.update("test-source", {"name": "Updated Test"})
        assert reg.get("test-source").name == "Updated Test"

        # Delete
        assert reg.delete("test-source")
        assert reg.get("test-source") is None

    def test_registry_toggle(self, tmp_data_dir):
        """Toggle enabled state."""
        reg = SourceRegistry(data_dir=tmp_data_dir)
        src = reg.list_sources()[0]
        original = src.enabled
        new_state = reg.toggle(src.id)
        assert new_state == (not original)

    def test_registry_filter_by_tier(self, tmp_data_dir):
        """Filter sources by tier."""
        reg = SourceRegistry(data_dir=tmp_data_dir)
        tier1 = reg.list_sources(tier=1)
        assert all(s.tier == 1 for s in tier1)
        assert len(tier1) >= 3  # IOM, ILO, UNODC, US TIP

    def test_registry_persistence(self, tmp_data_dir):
        """Changes persist across instances."""
        reg1 = SourceRegistry(data_dir=tmp_data_dir)
        reg1.create(SourceConfig(id="persist-test", name="Persist", tier=5, url="https://x.com"))

        reg2 = SourceRegistry(data_dir=tmp_data_dir)
        assert reg2.get("persist-test") is not None


# =============================================================================
# Document Fetcher Tests
# =============================================================================

class TestDocumentFetcher:
    def test_extract_links_requires_bs4(self, tmp_data_dir):
        """Link extraction works when BeautifulSoup is available."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        html = '<html><body><a href="/report.pdf">Report</a><a href="/news/1">News</a></body></html>'
        links = fetcher.extract_links(html, "https://example.com", ["a[href*='/news/']"])
        assert "https://example.com/news/1" in links
        # PDF links are auto-discovered
        assert "https://example.com/report.pdf" in links

    def test_extract_html_text(self, tmp_data_dir):
        """HTML text extraction strips tags and gets title."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        html = '<html><head><title>Test Doc</title></head><body><p>Hello world</p></body></html>'
        text, title = fetcher._extract_html_text(html)
        assert "Hello world" in text
        assert title == "Test Doc"

    def test_deduplication(self, tmp_data_dir):
        """Content hash deduplication prevents saving identical docs."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        assert not fetcher.is_duplicate("unique content here")
        # Simulate saving a doc
        fetcher._known_hashes.add(
            __import__("hashlib").sha256(b"duplicate content").hexdigest()
        )
        assert fetcher.is_duplicate("duplicate content")

    def test_list_documents_empty(self, tmp_data_dir):
        """List documents returns empty list when no docs."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        assert fetcher.list_documents() == []
        assert fetcher.count_documents() == 0

    def test_save_and_load_document(self, tmp_data_dir):
        """Save and load a document."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        doc_data = {
            "id": "test-doc-1",
            "url": "https://example.com/doc",
            "title": "Test Document",
            "text": "This is test content for the document.",
            "content_type": "html",
            "fetched_at": "2026-01-01T00:00:00",
            "source_id": "test-source",
            "content_hash": "abc123",
            "word_count": 7,
        }
        doc_path = Path(tmp_data_dir) / "documents" / "test-doc-1.json"
        doc_path.write_text(json.dumps(doc_data), encoding="utf-8")

        loaded = fetcher.load_document("test-doc-1")
        assert loaded is not None
        assert loaded.title == "Test Document"
        assert loaded.word_count == 7

    def test_delete_document(self, tmp_data_dir):
        """Delete removes the document file."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        doc_path = Path(tmp_data_dir) / "documents" / "del-test.json"
        doc_path.write_text('{"id":"del-test","content_hash":"x"}', encoding="utf-8")
        assert fetcher.delete_document("del-test")
        assert not doc_path.exists()


# =============================================================================
# Fact Extractor Tests
# =============================================================================

class TestFactExtractor:
    def test_parse_response_valid(self, tmp_data_dir):
        """Parse a valid JSON response."""
        ext = FactExtractor(data_dir=tmp_data_dir)
        response = '```json\n{"facts": [{"type": "fee_cap", "amount": "HKD 4630"}], "summary": "Fee cap info", "relevance_score": 0.9}\n```'
        parsed = ext._parse_response(response)
        assert len(parsed["facts"]) == 1
        assert parsed["facts"][0]["type"] == "fee_cap"
        assert parsed["relevance_score"] == 0.9

    def test_parse_response_invalid(self, tmp_data_dir):
        """Parse an invalid response gracefully."""
        ext = FactExtractor(data_dir=tmp_data_dir)
        parsed = ext._parse_response("This is not JSON at all")
        assert parsed["facts"] == []

    def test_deduplicate_facts(self, tmp_data_dir):
        """Duplicate facts are removed."""
        ext = FactExtractor(data_dir=tmp_data_dir)
        facts = [
            {"type": "fee_cap", "amount": "HKD 4630"},
            {"type": "fee_cap", "amount": "HKD 4630"},
            {"type": "law", "name": "Cap. 57"},
        ]
        unique = ext._deduplicate_facts(facts)
        assert len(unique) == 2

    def test_chunk_text(self, tmp_data_dir):
        """Long text is chunked properly."""
        ext = FactExtractor(data_dir=tmp_data_dir)
        words = ["word"] * 10000
        chunks = ext._chunk_text(words)
        assert len(chunks) == 3  # 4000 + 4000 + 2000

    def test_save_and_load_extraction(self, tmp_data_dir):
        """Save and load an extraction result."""
        ext = FactExtractor(data_dir=tmp_data_dir)
        result = ExtractionResult(
            document_id="test-doc",
            facts=[{"type": "fee_cap", "amount": "HKD 4630"}],
            summary="Test summary",
            relevance_score=0.85,
            extracted_at="2026-01-01T00:00:00",
        )
        ext._save(result)
        loaded = ext.load_extraction("test-doc")
        assert loaded is not None
        assert loaded.relevance_score == 0.85
        assert len(loaded.facts) == 1


# =============================================================================
# Knowledge Base Tests
# =============================================================================

class TestKnowledgeBase:
    def test_empty_kb(self, tmp_data_dir):
        """Empty KB returns zero stats."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        stats = kb.stats()
        assert stats["total_facts"] == 0

    def test_merge_extraction(self, tmp_data_dir):
        """Merge facts from an extraction."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        facts = [
            {"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4630"},
            {"type": "law", "jurisdiction": "HK", "name": "Cap. 57"},
        ]
        added = kb.merge_extraction(facts, "doc-1")
        assert added == 2
        assert kb.stats()["total_facts"] == 2

    def test_merge_deduplication(self, tmp_data_dir):
        """Duplicate facts are not added twice."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        facts = [{"type": "fee_cap", "amount": "HKD 4630"}]
        kb.merge_extraction(facts, "doc-1")
        added = kb.merge_extraction(facts, "doc-2")
        assert added == 0
        assert kb.stats()["total_facts"] == 1

    def test_query_by_category(self, tmp_data_dir):
        """Query facts filtered by category."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([
            {"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4630"},
            {"type": "law", "jurisdiction": "SG", "name": "EAA"},
        ], "doc-1")
        results = kb.query(category="fee_cap")
        assert len(results) == 1
        assert results[0]["type"] == "fee_cap"

    def test_query_by_jurisdiction(self, tmp_data_dir):
        """Query facts filtered by jurisdiction."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([
            {"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4630"},
            {"type": "fee_cap", "jurisdiction": "SG", "amount": "SGD 600"},
        ], "doc-1")
        results = kb.query(jurisdiction="SG")
        assert len(results) == 1
        assert results[0]["jurisdiction"] == "SG"

    def test_rebuild(self, tmp_data_dir):
        """Rebuild KB from extraction files."""
        # Write an extraction file
        ext_dir = Path(tmp_data_dir) / "extractions"
        ext_dir.mkdir(exist_ok=True)
        (ext_dir / "doc-1.json").write_text(json.dumps({
            "document_id": "doc-1",
            "facts": [{"type": "statistic", "metric": "victims", "value": 1234}],
            "summary": "Test",
            "relevance_score": 0.7,
            "extracted_at": "2026-01-01T00:00:00",
        }), encoding="utf-8")

        kb = KnowledgeBase(data_dir=tmp_data_dir)
        counts = kb.rebuild()
        assert counts.get("statistic") == 1

    def test_get_context_empty(self, tmp_data_dir):
        """Context for generation is empty when no facts."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        ctx = kb.get_context_for_generation()
        assert ctx == ""

    def test_get_context_with_facts(self, tmp_data_dir):
        """Context for generation includes facts."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([
            {"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4,630", "law": "EO Cap. 57"},
        ], "doc-1")
        ctx = kb.get_context_for_generation()
        assert "KNOWLEDGE BASE" in ctx
        assert "HKD 4,630" in ctx

    def test_stats_categories(self, tmp_data_dir):
        """Stats reports correct categories."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([
            {"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4630"},
            {"type": "law", "jurisdiction": "SG", "name": "EAA"},
            {"type": "case_study", "corridor": "PH-HK", "summary": "Test case"},
        ], "doc-1")
        stats = kb.stats()
        assert stats["by_category"]["fee_cap"] == 1
        assert stats["by_category"]["law"] == 1
        assert stats["by_category"]["case_study"] == 1
        assert "HK" in stats["jurisdictions"]
        assert "PH-HK" in stats["corridors"]


# =============================================================================
# Source Expansion Tests
# =============================================================================

class TestSourceExpansion:
    def test_tier_labels_complete(self):
        """All 7 tier labels are defined."""
        assert len(TIER_LABELS) == 7
        for i in range(1, 8):
            assert i in TIER_LABELS

    def test_new_source_fields_defaults(self):
        """New fields have backward-compatible defaults."""
        src = SourceConfig(id="t", name="T", tier=1, url="https://x.com")
        assert src.requires_js is False
        assert src.feed_url is None
        assert src.language == "en"
        assert src.corridors == []

    def test_sources_with_js(self):
        """Some sources require Playwright."""
        js_sources = [s for s in DEFAULT_SOURCES if s.requires_js]
        assert len(js_sources) >= 3

    def test_sources_with_feeds(self):
        """Some sources have RSS/Atom feeds."""
        feed_sources = [s for s in DEFAULT_SOURCES if s.feed_url]
        assert len(feed_sources) >= 3

    def test_sources_with_corridors(self):
        """Many sources have corridor annotations."""
        corridor_sources = [s for s in DEFAULT_SOURCES if s.corridors]
        assert len(corridor_sources) >= 20

    def test_tier_6_courts(self):
        """Tier 6 has court/legal sources."""
        tier6 = [s for s in DEFAULT_SOURCES if s.tier == 6]
        assert len(tier6) >= 4

    def test_tier_7_academic(self):
        """Tier 7 has academic sources."""
        tier7 = [s for s in DEFAULT_SOURCES if s.tier == 7]
        assert len(tier7) >= 4


# =============================================================================
# Politeness Policy Tests
# =============================================================================

class TestPolitenessPolicy:
    def test_default_delay(self):
        """Default delay is 2 seconds."""
        pp = PolitenessPolicy(respect_robots=False)
        assert pp.get_delay("example.com") == 2.0

    def test_gov_domain_delay(self):
        """Government domains get higher delay."""
        pp = PolitenessPolicy(respect_robots=False)
        assert pp.get_delay("dmw.gov.ph") == 3.0
        assert pp.get_delay("bp2mi.go.id") == 3.0

    def test_igo_domain_delay(self):
        """IGO domains get 2.5s delay."""
        pp = PolitenessPolicy(respect_robots=False)
        assert pp.get_delay("www.ilo.org") == 2.5

    def test_custom_delay(self):
        """Custom domain delays override defaults."""
        pp = PolitenessPolicy(
            respect_robots=False,
            domain_delays={"example.com": 5.0},
        )
        assert pp.get_delay("example.com") == 5.0

    def test_get_config(self):
        """Config returns expected structure."""
        pp = PolitenessPolicy(respect_robots=False)
        config = pp.get_config()
        assert "default_delay" in config
        assert "domain_delays" in config
        assert "respect_robots" in config
        assert config["respect_robots"] is False

    @pytest.mark.asyncio
    async def test_robots_disabled(self):
        """When robots disabled, always returns True."""
        pp = PolitenessPolicy(respect_robots=False)
        result = await pp.check_robots("https://example.com/secret")
        assert result is True


# =============================================================================
# Retry Policy Tests
# =============================================================================

class TestRetryPolicy:
    def test_default_config(self):
        """Default retry configuration."""
        rp = RetryPolicy()
        assert rp.max_retries == 3
        assert rp.base_delay == 1.0
        assert rp.backoff_factor == 2.0

    def test_retryable_status_codes(self):
        """Check retryable status codes."""
        rp = RetryPolicy()
        assert rp.is_retryable_status(429)
        assert rp.is_retryable_status(503)
        assert not rp.is_retryable_status(200)
        assert not rp.is_retryable_status(404)

    @pytest.mark.asyncio
    async def test_successful_execute(self):
        """Execute succeeds on first try."""
        rp = RetryPolicy()
        async def success():
            return "ok"
        result = await rp.execute(success)
        assert result == "ok"
        assert rp.total_retries == 0

    @pytest.mark.asyncio
    async def test_non_retryable_raises(self):
        """Non-retryable exceptions are raised immediately."""
        rp = RetryPolicy()
        async def fail():
            raise ValueError("bad")
        with pytest.raises(ValueError):
            await rp.execute(fail)

    def test_get_config(self):
        """Config returns expected structure."""
        rp = RetryPolicy(max_retries=5)
        config = rp.get_config()
        assert config["max_retries"] == 5
        assert 429 in config["retryable_status_codes"]


# =============================================================================
# Change Detection Tests
# =============================================================================

class TestChangeDetector:
    def test_new_url_is_changed(self, tmp_data_dir):
        """A never-seen URL is always 'changed'."""
        cd = ChangeDetector(data_dir=tmp_data_dir)
        assert cd.is_changed("https://example.com/new", "hello world")

    def test_same_content_not_changed(self, tmp_data_dir):
        """Same content is not changed after update."""
        cd = ChangeDetector(data_dir=tmp_data_dir)
        url = "https://example.com/page"
        cd.update(url, "content A")
        assert not cd.is_changed(url, "content A")

    def test_different_content_is_changed(self, tmp_data_dir):
        """Different content is detected as changed."""
        cd = ChangeDetector(data_dir=tmp_data_dir)
        url = "https://example.com/page"
        cd.update(url, "version 1")
        assert cd.is_changed(url, "version 2")

    def test_conditional_headers(self, tmp_data_dir):
        """Conditional headers returned when fingerprint has etag."""
        cd = ChangeDetector(data_dir=tmp_data_dir)
        url = "https://example.com/page"
        cd.update(url, "content", {"ETag": '"abc123"', "Last-Modified": "Mon, 01 Jan 2026"})
        headers = cd.get_conditional_headers(url)
        assert headers["If-None-Match"] == '"abc123"'
        assert headers["If-Modified-Since"] == "Mon, 01 Jan 2026"

    def test_persistence(self, tmp_data_dir):
        """Fingerprints persist across instances."""
        url = "https://example.com/persist"
        cd1 = ChangeDetector(data_dir=tmp_data_dir)
        cd1.update(url, "content data")

        cd2 = ChangeDetector(data_dir=tmp_data_dir)
        assert not cd2.is_changed(url, "content data")

    def test_clear(self, tmp_data_dir):
        """Clear removes all fingerprints."""
        cd = ChangeDetector(data_dir=tmp_data_dir)
        cd.update("https://example.com/a", "aaa")
        cd.update("https://example.com/b", "bbb")
        cleared = cd.clear()
        assert cleared == 2
        assert cd.stats()["total_fingerprints"] == 0

    def test_stats(self, tmp_data_dir):
        """Stats returns expected structure."""
        cd = ChangeDetector(data_dir=tmp_data_dir)
        cd.update("https://a.com", "a", {"ETag": '"e1"'})
        cd.update("https://b.com", "b")
        stats = cd.stats()
        assert stats["total_fingerprints"] == 2
        assert stats["with_etag"] == 1


# =============================================================================
# Feed Parser Tests
# =============================================================================

class TestFeedParser:
    def test_parse_rss(self):
        """Parse RSS 2.0 feed."""
        parser = FeedParser()
        xml = '''<?xml version="1.0"?>
        <rss version="2.0"><channel><title>Test</title>
        <item><title>Article 1</title><link>https://example.com/1</link><pubDate>Mon, 01 Jan 2026</pubDate></item>
        <item><title>Article 2</title><link>https://example.com/2</link></item>
        </channel></rss>'''
        entries = parser.parse_feed(xml)
        assert len(entries) == 2
        assert entries[0].title == "Article 1"
        assert entries[0].url == "https://example.com/1"

    def test_parse_atom(self):
        """Parse Atom feed."""
        parser = FeedParser()
        xml = '''<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
        <entry><title>Entry 1</title><link href="https://example.com/e1"/><published>2026-01-01</published></entry>
        </feed>'''
        entries = parser.parse_feed(xml)
        assert len(entries) == 1
        assert entries[0].title == "Entry 1"
        assert entries[0].url == "https://example.com/e1"

    def test_parse_sitemap(self):
        """Parse sitemap.xml."""
        parser = FeedParser()
        xml = '''<?xml version="1.0"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url><loc>https://example.com/page1</loc></url>
        <url><loc>https://example.com/page2</loc></url>
        </urlset>'''
        urls = parser.parse_sitemap(xml)
        assert len(urls) == 2
        assert "https://example.com/page1" in urls

    def test_parse_malformed_xml(self):
        """Malformed XML returns empty list."""
        parser = FeedParser()
        entries = parser.parse_feed("<not-valid-xml")
        assert entries == []

    def test_parse_empty_feed(self):
        """Feed with no items returns empty list."""
        parser = FeedParser()
        xml = '<?xml version="1.0"?><rss version="2.0"><channel><title>Empty</title></channel></rss>'
        entries = parser.parse_feed(xml)
        assert entries == []


# =============================================================================
# Headless Browser Tests
# =============================================================================

class TestHeadlessBrowser:
    def test_is_available(self):
        """Playwright availability check returns boolean."""
        result = HeadlessBrowser.is_available()
        assert isinstance(result, bool)

    @pytest.mark.asyncio
    async def test_status(self):
        """Status returns expected structure."""
        info = await HeadlessBrowser.status()
        assert "playwright_installed" in info
        assert "browser_connected" in info


# =============================================================================
# Extractor Expansion Tests
# =============================================================================

class TestExtractorExpansion:
    def test_fact_types_complete(self):
        """All fact types are defined (15 original + 6 legal expansion)."""
        assert len(FACT_TYPES) == 21
        assert "court_ruling" in FACT_TYPES
        assert "penalty" in FACT_TYPES

    def test_extraction_result_new_fields(self):
        """ExtractionResult has confidence, citations, entities fields."""
        r = ExtractionResult(
            document_id="t",
            facts=[],
            summary="",
            relevance_score=0.0,
            confidence_scores={0: 0.95},
            citations=[{"fact_index": 0, "paragraph": 5}],
            entities=[{"name": "ILO", "type": "organisation", "mentions": 3}],
        )
        assert r.confidence_scores[0] == 0.95
        assert len(r.citations) == 1
        assert r.entities[0]["name"] == "ILO"

    def test_paragraph_markers(self, tmp_data_dir):
        """Paragraph markers are added correctly."""
        ext = FactExtractor(data_dir=tmp_data_dir)
        text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        marked = ext._add_paragraph_markers(text)
        assert "¶1 First paragraph." in marked
        assert "¶2 Second paragraph." in marked
        assert "¶3 Third paragraph." in marked

    def test_deduplicate_entities(self, tmp_data_dir):
        """Entity dedup merges mention counts."""
        entities = [
            {"name": "ILO", "type": "organisation", "mentions": 3},
            {"name": "ilo", "type": "organisation", "mentions": 2},
            {"name": "OHCHR", "type": "organisation", "mentions": 1},
        ]
        unique = FactExtractor._deduplicate_entities(entities)
        assert len(unique) == 2
        ilo = [e for e in unique if e["name"].lower() == "ilo"][0]
        assert ilo["mentions"] == 5

    def test_save_load_with_new_fields(self, tmp_data_dir):
        """Save and load extraction with confidence/citations/entities."""
        ext = FactExtractor(data_dir=tmp_data_dir)
        result = ExtractionResult(
            document_id="new-fields-test",
            facts=[{"type": "court_ruling", "court": "HK"}],
            summary="Test",
            relevance_score=0.9,
            extracted_at="2026-01-01T00:00:00",
            confidence_scores={0: 0.88},
            citations=[{"fact_index": 0, "paragraph": 2}],
            entities=[{"name": "HK Labour Tribunal", "type": "court", "mentions": 1}],
        )
        ext._save(result)
        loaded = ext.load_extraction("new-fields-test")
        assert loaded.confidence_scores[0] == 0.88
        assert len(loaded.citations) == 1
        assert loaded.entities[0]["name"] == "HK Labour Tribunal"


# =============================================================================
# Knowledge Base Expansion Tests
# =============================================================================

class TestKBExpansion:
    def test_kb_categories_complete(self):
        """KB has all categories (15 original + 6 legal + 3 indicator matrix)."""
        assert len(KnowledgeBase.CATEGORIES) == 24
        assert "court_ruling" in KnowledgeBase.CATEGORIES
        assert "penalty" in KnowledgeBase.CATEGORIES

    def test_temporal_tracking(self, tmp_data_dir):
        """Merged facts get _first_seen and _last_confirmed."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([{"type": "fee_cap", "amount": "HKD 4630"}], "doc-1")
        facts = kb.query(category="fee_cap")
        assert len(facts) == 1
        assert "_first_seen" in facts[0]
        assert "_last_confirmed" in facts[0]

    def test_duplicate_updates_last_confirmed(self, tmp_data_dir):
        """Duplicate facts update _last_confirmed."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([{"type": "fee_cap", "amount": "HKD 4630"}], "doc-1")
        first = kb.query(category="fee_cap")[0]["_last_confirmed"]

        import time; time.sleep(0.01)
        kb.merge_extraction([{"type": "fee_cap", "amount": "HKD 4630"}], "doc-2")
        updated = kb.query(category="fee_cap")[0]["_last_confirmed"]
        assert updated >= first

    def test_confidence_scoring(self, tmp_data_dir):
        """Facts have _confidence field."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction(
            [{"type": "law", "name": "Test Law"}], "doc-1",
            confidence_scores={0: 0.92},
        )
        facts = kb.query(category="law")
        assert facts[0]["_confidence"] == 0.92

    def test_cross_references_after_rebuild(self, tmp_data_dir):
        """Facts sharing jurisdiction are cross-referenced after rebuild."""
        ext_dir = Path(tmp_data_dir) / "extractions"
        ext_dir.mkdir(exist_ok=True)
        (ext_dir / "doc-1.json").write_text(json.dumps({
            "document_id": "doc-1",
            "facts": [
                {"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4630"},
                {"type": "law", "jurisdiction": "HK", "name": "EO Cap. 57"},
            ],
            "summary": "Test", "relevance_score": 0.9, "extracted_at": "2026-01-01",
        }), encoding="utf-8")

        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.rebuild()
        facts = kb.query()
        # Both facts share HK jurisdiction, so they should cross-ref each other
        for f in facts:
            assert "_related_facts" in f
            assert len(f["_related_facts"]) >= 1

    def test_query_timeline(self, tmp_data_dir):
        """Timeline query returns facts sorted by _first_seen."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([{"type": "fee_cap", "amount": "1"}], "doc-1")
        kb.merge_extraction([{"type": "law", "name": "Law 2"}], "doc-2")
        timeline = kb.query_timeline(limit=10)
        assert len(timeline) == 2
        # Most recent first
        assert timeline[0]["_first_seen"] >= timeline[1]["_first_seen"]

    def test_stale_facts(self, tmp_data_dir):
        """Stale facts returns facts older than cutoff."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([{"type": "fee_cap", "amount": "1"}], "doc-1")
        # All facts are brand new, so a large cutoff window should return 0
        stale = kb.get_stale_facts(days=365)
        assert len(stale) == 0

    def test_query_entities(self, tmp_data_dir):
        """Entity aggregation returns expected structure."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction([
            {"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4630"},
            {"type": "law", "jurisdiction": "HK", "name": "Cap. 57"},
            {"type": "law", "jurisdiction": "SG", "name": "EAA"},
        ], "doc-1")
        entities = kb.query_entities()
        assert len(entities) >= 2
        hk = [e for e in entities if e["name"] == "HK"]
        assert len(hk) == 1
        assert hk[0]["mentions"] == 2

    def test_get_context_with_confidence_filter(self, tmp_data_dir):
        """Context filters by min_confidence."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction(
            [{"type": "fee_cap", "jurisdiction": "HK", "amount": "HKD 4630"}],
            "doc-1", confidence_scores={0: 0.3},
        )
        kb.merge_extraction(
            [{"type": "law", "jurisdiction": "SG", "name": "EAA"}],
            "doc-2", confidence_scores={0: 0.9},
        )
        ctx = kb.get_context_for_generation(min_confidence=0.5)
        assert "EAA" in ctx
        assert "HKD 4,630" not in ctx  # confidence too low

    def test_avg_confidence_in_stats(self, tmp_data_dir):
        """Stats includes avg_confidence."""
        kb = KnowledgeBase(data_dir=tmp_data_dir)
        kb.merge_extraction(
            [{"type": "fee_cap", "amount": "1"}], "doc-1",
            confidence_scores={0: 0.8},
        )
        stats = kb.stats()
        assert "avg_confidence" in stats
        assert stats["avg_confidence"] == 0.8


# =============================================================================
# Document New Fields Tests
# =============================================================================

class TestDocumentNewFields:
    def test_document_backward_compat(self):
        """Old Document without new fields still works."""
        doc = Document(
            id="t", url="", title="", text="", content_type="html",
            fetched_at="", source_id="", content_hash="",
        )
        assert doc.etag is None
        assert doc.language == "en"
        assert doc.page_count is None

    def test_document_with_new_fields(self):
        """Document with new fields."""
        doc = Document(
            id="t", url="", title="", text="", content_type="pdf",
            fetched_at="", source_id="", content_hash="",
            etag='"abc"', last_modified="Mon, 01 Jan 2026",
            language="ko", page_count=5,
        )
        assert doc.etag == '"abc"'
        assert doc.language == "ko"
        assert doc.page_count == 5
