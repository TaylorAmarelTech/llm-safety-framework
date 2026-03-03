"""Tests for the stealth scraper system (stealth, proxy, browser, routes)."""

import asyncio
import json
import time
import pytest
from pathlib import Path

from src.scraper.stealth import (
    StealthLevel, StealthProfile, HeaderBuilder, UARotator, STEALTH_LABELS,
)
from src.scraper.proxy import ProxyRotator, ProxyHealth
from src.scraper.politeness import PolitenessPolicy
from src.scraper.retry import RetryPolicy, RetryableError
from src.scraper.browser import HeadlessBrowser, STEALTH_PATCH_AVAILABLE, _DEFAULT_UA
from src.scraper.sources import SourceConfig, DEFAULT_SOURCES
from src.scraper.fetcher import DocumentFetcher


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
# StealthProfile Tests
# =============================================================================

class TestStealthProfile:
    def test_default_is_level_none(self):
        """Default StealthProfile is level NONE."""
        sp = StealthProfile()
        assert sp.level == StealthLevel.NONE
        assert not sp.rotate_ua
        assert not sp.realistic_headers
        assert not sp.jitter_enabled

    def test_from_level_none(self):
        sp = StealthProfile.from_level(StealthLevel.NONE)
        assert sp.level == StealthLevel.NONE
        assert not sp.rotate_ua

    def test_from_level_basic(self):
        sp = StealthProfile.from_level(StealthLevel.BASIC)
        assert sp.level == StealthLevel.BASIC
        assert sp.rotate_ua
        assert sp.realistic_headers
        assert sp.jitter_enabled
        assert sp.persist_cookies
        assert sp.tls_impersonate is None

    def test_from_level_moderate(self):
        sp = StealthProfile.from_level(StealthLevel.MODERATE)
        assert sp.level == StealthLevel.MODERATE
        assert sp.tls_impersonate == "chrome120"

    def test_from_level_full(self):
        sp = StealthProfile.from_level(StealthLevel.FULL)
        assert sp.level == StealthLevel.FULL
        assert sp.viewport_randomize
        assert sp.locale_randomize

    def test_from_level_maximum(self):
        sp = StealthProfile.from_level(StealthLevel.MAXIMUM)
        assert sp.level == StealthLevel.MAXIMUM
        assert sp.rotate_ua
        assert sp.realistic_headers
        assert sp.viewport_randomize

    def test_serialization_roundtrip(self):
        sp = StealthProfile.from_level(StealthLevel.FULL)
        d = sp.to_dict()
        assert isinstance(d, dict)
        assert d["level"] == 3
        sp2 = StealthProfile.from_dict(d)
        assert sp2.level == StealthLevel.FULL
        assert sp2.rotate_ua == sp.rotate_ua
        assert sp2.tls_impersonate == sp.tls_impersonate

    def test_to_dict_has_all_fields(self):
        sp = StealthProfile.from_level(StealthLevel.MODERATE)
        d = sp.to_dict()
        expected = [
            "level", "rotate_ua", "ua_browser", "ua_platform",
            "realistic_headers", "jitter_enabled", "jitter_min", "jitter_max",
            "tls_impersonate", "persist_cookies", "proxy_enabled",
            "proxy_list", "proxy_rotation", "viewport_randomize",
            "locale_randomize", "timezone_spoof",
        ]
        for key in expected:
            assert key in d, f"Missing key: {key}"


# =============================================================================
# StealthLevel & Labels
# =============================================================================

class TestStealthLevel:
    def test_int_values(self):
        assert int(StealthLevel.NONE) == 0
        assert int(StealthLevel.BASIC) == 1
        assert int(StealthLevel.MODERATE) == 2
        assert int(StealthLevel.FULL) == 3
        assert int(StealthLevel.MAXIMUM) == 4

    def test_labels(self):
        assert len(STEALTH_LABELS) == 5
        assert STEALTH_LABELS[0] == "None"
        assert STEALTH_LABELS[4] == "Maximum"


# =============================================================================
# HeaderBuilder Tests
# =============================================================================

class TestHeaderBuilder:
    def test_chrome_headers(self):
        headers = HeaderBuilder.build("TestUA/1.0", "chrome")
        assert headers["User-Agent"] == "TestUA/1.0"
        assert "Sec-Ch-Ua" in headers
        assert "Sec-Fetch-Dest" in headers
        assert headers["Sec-Fetch-Mode"] == "navigate"

    def test_firefox_headers(self):
        headers = HeaderBuilder.build("TestUA/2.0", "firefox")
        assert headers["User-Agent"] == "TestUA/2.0"
        assert "Sec-Ch-Ua" not in headers  # Firefox doesn't send Sec-Ch-Ua
        assert "Sec-Fetch-Dest" in headers

    def test_headers_include_accept(self):
        for browser in ["chrome", "firefox"]:
            h = HeaderBuilder.build("UA", browser)
            assert "Accept" in h
            assert "Accept-Language" in h
            assert "Accept-Encoding" in h


# =============================================================================
# UARotator Tests
# =============================================================================

class TestUARotator:
    def test_fallback_without_fake_useragent(self):
        rotator = UARotator(browser="chrome")
        ua = rotator.get()
        assert isinstance(ua, str)
        assert "Mozilla" in ua
        assert len(ua) > 30

    def test_variety_from_fallback_list(self):
        """Built-in fallback list produces at least 2 distinct UAs."""
        rotator = UARotator(browser="chrome")
        rotator._fake_ua = None  # Force fallback to built-in list
        uas = {rotator.get() for _ in range(20)}
        assert len(uas) >= 2

    def test_firefox_fallback_list(self):
        """Built-in Firefox fallback list produces Firefox UAs."""
        rotator = UARotator(browser="firefox")
        rotator._fake_ua = None  # Force fallback to built-in list
        ua = rotator.get()
        assert "Firefox" in ua

    def test_has_fake_useragent_property(self):
        rotator = UARotator()
        assert isinstance(rotator.has_fake_useragent, bool)


# =============================================================================
# ProxyRotator Tests
# =============================================================================

class TestProxyRotator:
    def test_empty_returns_none(self):
        rotator = ProxyRotator()
        assert rotator.get_next() is None
        assert rotator.count == 0

    def test_round_robin(self):
        rotator = ProxyRotator(
            proxies=["http://a:8080", "http://b:8080", "http://c:8080"],
            rotation="round_robin",
        )
        assert rotator.count == 3
        results = [rotator.get_next() for _ in range(6)]
        assert results == [
            "http://a:8080", "http://b:8080", "http://c:8080",
            "http://a:8080", "http://b:8080", "http://c:8080",
        ]

    def test_random_selection(self):
        rotator = ProxyRotator(
            proxies=["http://a:8080", "http://b:8080"],
            rotation="random",
        )
        results = {rotator.get_next() for _ in range(20)}
        assert len(results) >= 1  # at least one proxy returned

    def test_least_failures(self):
        rotator = ProxyRotator(
            proxies=["http://a:8080", "http://b:8080"],
            rotation="least_failures",
        )
        rotator.report_failure("http://a:8080")
        rotator.report_failure("http://a:8080")
        assert rotator.get_next() == "http://b:8080"

    def test_health_tracking(self):
        rotator = ProxyRotator(proxies=["http://a:8080"])
        rotator.report_success("http://a:8080", latency_ms=150)
        rotator.report_success("http://a:8080", latency_ms=250)
        rotator.report_failure("http://a:8080")

        health = rotator.get_health()
        assert len(health) == 1
        h = health[0]
        assert h["successes"] == 2
        assert h["failures"] == 1
        assert h["failure_rate"] > 0
        assert h["avg_latency_ms"] > 0

    def test_add_remove_proxy(self):
        rotator = ProxyRotator(proxies=["http://a:8080"])
        assert rotator.count == 1
        rotator.add_proxy("http://b:8080")
        assert rotator.count == 2
        rotator.remove_proxy("http://a:8080")
        assert rotator.count == 1
        assert rotator.get_next() == "http://b:8080"

    def test_cooldown_after_failure(self):
        """Failed proxies are excluded from random selection during cooldown."""
        rotator = ProxyRotator(
            proxies=["http://a:8080", "http://b:8080"],
            rotation="random",
            cooldown_after_failure=3600,  # very long cooldown
        )
        rotator.report_failure("http://a:8080")
        # With a being in cooldown, random should mostly select b
        results = [rotator.get_next() for _ in range(20)]
        assert all(r == "http://b:8080" for r in results)


# =============================================================================
# Politeness Jitter Tests
# =============================================================================

class TestPolitenessJitter:
    @pytest.mark.asyncio
    async def test_jitter_increases_delay(self):
        """Jitter adds additional random delay beyond base."""
        pp = PolitenessPolicy(default_delay=0.01, respect_robots=False)
        # First call: no waiting needed
        await pp.wait_for_domain("http://example.com/1")
        start = time.time()
        await pp.wait_for_domain("http://example.com/2", jitter=(0.05, 0.1))
        elapsed = time.time() - start
        # Should wait at least jitter_min (0.05) beyond base delay
        assert elapsed >= 0.04  # some tolerance

    @pytest.mark.asyncio
    async def test_no_jitter_by_default(self):
        """Without jitter param, only base delay applies."""
        pp = PolitenessPolicy(default_delay=0.01, respect_robots=False)
        await pp.wait_for_domain("http://example2.com/1")
        start = time.time()
        await pp.wait_for_domain("http://example2.com/2")
        elapsed = time.time() - start
        assert elapsed < 0.5  # should be very fast with small delay


# =============================================================================
# Retry Jitter Tests
# =============================================================================

class TestRetryJitter:
    @pytest.mark.asyncio
    async def test_retry_with_jitter_succeeds(self):
        """Retry with jitter eventually succeeds."""
        call_count = 0

        async def flaky():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise RetryableError("transient", status_code=503)
            return "ok"

        rp = RetryPolicy(max_retries=3, base_delay=0.01, jitter=True)
        result = await rp.execute(flaky)
        assert result == "ok"
        assert call_count == 3

    @pytest.mark.asyncio
    async def test_retry_without_jitter(self):
        """Retry without jitter also works."""
        call_count = 0

        async def flaky():
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                raise RetryableError("transient", status_code=429)
            return "done"

        rp = RetryPolicy(max_retries=3, base_delay=0.01, jitter=False)
        result = await rp.execute(flaky)
        assert result == "done"


# =============================================================================
# Fetcher Stealth Integration Tests
# =============================================================================

class TestFetcherStealth:
    def test_default_fetcher_uses_bot_ua(self, tmp_data_dir):
        """Default fetcher (no stealth) uses bot user-agent."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        assert fetcher.stealth.level == StealthLevel.NONE
        ua = fetcher._get_user_agent()
        assert "MigrantWorkerSafetyResearchBot" in ua

    def test_stealth_basic_uses_rotated_ua(self, tmp_data_dir):
        """Stealth BASIC rotates user-agent."""
        profile = StealthProfile.from_level(StealthLevel.BASIC)
        fetcher = DocumentFetcher(data_dir=tmp_data_dir, stealth=profile)
        assert fetcher.stealth.level == StealthLevel.BASIC
        ua = fetcher._get_user_agent()
        assert "MigrantWorkerSafetyResearchBot" not in ua
        assert "Mozilla" in ua

    def test_stealth_builds_realistic_headers(self, tmp_data_dir):
        """Stealth BASIC+ builds full browser headers."""
        profile = StealthProfile.from_level(StealthLevel.BASIC)
        fetcher = DocumentFetcher(data_dir=tmp_data_dir, stealth=profile)
        headers = fetcher._build_headers("https://example.com")
        assert "User-Agent" in headers
        assert "Sec-Fetch-Dest" in headers
        assert "Accept" in headers

    def test_stealth_none_minimal_headers(self, tmp_data_dir):
        """Stealth NONE sends only User-Agent."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        headers = fetcher._build_headers("https://example.com")
        assert "User-Agent" in headers
        assert "Sec-Fetch-Dest" not in headers

    def test_jitter_enabled(self, tmp_data_dir):
        """Stealth BASIC returns jitter tuple."""
        profile = StealthProfile.from_level(StealthLevel.BASIC)
        fetcher = DocumentFetcher(data_dir=tmp_data_dir, stealth=profile)
        jitter = fetcher._get_jitter()
        assert jitter is not None
        assert len(jitter) == 2
        assert jitter[0] < jitter[1]

    def test_jitter_disabled(self, tmp_data_dir):
        """Stealth NONE returns no jitter."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        assert fetcher._get_jitter() is None

    def test_proxy_not_used_when_disabled(self, tmp_data_dir):
        """No proxy returned when proxy_enabled is False."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        assert fetcher._get_proxy() is None

    def test_proxy_used_when_enabled(self, tmp_data_dir):
        """Proxy returned when enabled with proxies."""
        profile = StealthProfile(
            proxy_enabled=True,
            proxy_list=["http://proxy1:8080"],
        )
        proxy_rotator = ProxyRotator(proxies=profile.proxy_list)
        fetcher = DocumentFetcher(
            data_dir=tmp_data_dir, stealth=profile,
            proxy_rotator=proxy_rotator,
        )
        assert fetcher._get_proxy() == "http://proxy1:8080"

    def test_cookie_jars_initially_empty(self, tmp_data_dir):
        """Cookie jars start empty."""
        fetcher = DocumentFetcher(data_dir=tmp_data_dir)
        assert fetcher._cookie_jars == {}


# =============================================================================
# Source stealth_level Tests
# =============================================================================

class TestSourceStealthLevel:
    def test_default_stealth_level_zero(self):
        src = SourceConfig(id="test", name="Test", tier=5, url="https://example.com")
        assert src.stealth_level == 0

    def test_custom_stealth_level(self):
        src = SourceConfig(
            id="test", name="Test", tier=4, url="https://example.com",
            requires_js=True, stealth_level=3,
        )
        assert src.stealth_level == 3

    def test_js_sources_have_stealth_level(self):
        """All requires_js=True default sources have stealth_level >= 3."""
        js_sources = [s for s in DEFAULT_SOURCES if s.requires_js]
        assert len(js_sources) >= 4  # sa-mol, kr-eps, hk-judiciary, sg-statutes, echr
        for s in js_sources:
            assert s.stealth_level >= 3, f"{s.id} has stealth_level={s.stealth_level}"


# =============================================================================
# Browser stealth Tests
# =============================================================================

class TestBrowserStealth:
    @pytest.mark.asyncio
    async def test_status_includes_stealth_flag(self):
        info = await HeadlessBrowser.status()
        assert "stealth_available" in info
        assert isinstance(info["stealth_available"], bool)

    def test_no_bot_ua_in_default(self):
        """Default browser UA does not contain bot identifier."""
        assert "LLMSafetyResearchBot" not in _DEFAULT_UA
        assert "Chrome" in _DEFAULT_UA


# =============================================================================
# Stealth Config Persistence Tests
# =============================================================================

class TestStealthConfigPersistence:
    def test_save_and_load(self, tmp_data_dir):
        """Stealth config can be saved and loaded from disk."""
        from src.web.plugins.scraper.routes import _save_stealth_config, _load_stealth_config

        profile = StealthProfile.from_level(StealthLevel.MODERATE)
        profile.proxy_list = ["http://p1:8080", "socks5://p2:1080"]
        _save_stealth_config(tmp_data_dir, profile)

        loaded = _load_stealth_config(tmp_data_dir)
        assert loaded.level == StealthLevel.MODERATE
        assert loaded.tls_impersonate == "chrome120"
        assert len(loaded.proxy_list) == 2

    def test_load_missing_returns_default(self, tmp_data_dir):
        from src.web.plugins.scraper.routes import _load_stealth_config
        profile = _load_stealth_config(tmp_data_dir)
        assert profile.level == StealthLevel.NONE


# =============================================================================
# Route Tests (using TestClient)
# =============================================================================

class TestStealthRoutes:
    @pytest.fixture
    def client(self, tmp_data_dir):
        """Create test client with scraper plugin."""
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        from src.web.plugins.scraper.routes import router
        from src.web.app_context import AppContext

        app = FastAPI()

        ctx = AppContext.__new__(AppContext)
        ctx.data_dir = Path(tmp_data_dir).parent
        ctx.config_manager = None

        app.include_router(router, prefix="/scraper")
        app.dependency_overrides = {}

        from src.web.app_context import get_ctx
        app.dependency_overrides[get_ctx] = lambda: ctx

        return TestClient(app)

    def test_stealth_status(self, client):
        resp = client.get("/scraper/stealth/status")
        assert resp.status_code == 200
        data = resp.json()
        assert "packages" in data
        pkgs = data["packages"]
        assert "fake_useragent" in pkgs
        assert "curl_cffi" in pkgs
        assert "playwright_stealth" in pkgs
        assert "nodriver" in pkgs
        assert "levels" in data

    def test_get_stealth_config(self, client):
        resp = client.get("/scraper/stealth/config")
        assert resp.status_code == 200
        data = resp.json()
        assert "config" in data
        assert data["config"]["level"] == 0  # default

    def test_put_stealth_config(self, client):
        resp = client.put("/scraper/stealth/config", json={
            "level": 2,
            "jitter_min": 1.0,
            "jitter_max": 3.0,
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["config"]["level"] == 2
        assert data["config"]["jitter_min"] == 1.0
        assert data["config"]["tls_impersonate"] == "chrome120"  # from level 2 defaults

        # Verify it persists
        resp2 = client.get("/scraper/stealth/config")
        assert resp2.json()["config"]["level"] == 2

    def test_proxy_health(self, client):
        resp = client.get("/scraper/stealth/proxy-health")
        assert resp.status_code == 200
        data = resp.json()
        assert "proxy_count" in data
        assert "health" in data
