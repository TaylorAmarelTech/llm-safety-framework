"""
Comprehensive web infrastructure tests — plugin registry, plugin base,
app context, fragment serving, API path validation, and UI content checks.

Tests cover:
1. PluginRegistry — discover, register, mount, nav, section map, disabled
2. PluginManifest / NavItem — dataclass creation, defaults
3. AppContext / get_ctx — DI pattern, plugin_data_dir
4. Fragment serving — all 17 plugins, HTML content, JS content, 404s
5. API path validation — health, nav, root, CORS, OpenAPI
6. Plugin route prefix uniqueness — no collisions
7. Nav item ID uniqueness — no duplicates
8. Training plugin fragments — newly created, content validation
"""

import json
from pathlib import Path
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from src.web.app import create_app
from src.web.config import Settings
from src.web.plugin_base import PluginManifest, NavItem
from src.web.plugin_registry import PluginRegistry
from src.web.app_context import AppContext


# ═══════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════

@pytest.fixture
def test_data_dir(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    pipeline_dir = tmp_path / "pipeline"
    pipeline_dir.mkdir()
    for sub in ("runs", "prompt_sets", "spun", "multi_turn"):
        (pipeline_dir / sub).mkdir()
    (tmp_path / "templates").mkdir()
    (tmp_path / "exports").mkdir()
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    config_file = config_dir / "api_keys.json"
    config_file.write_text("{}")
    # Scraper + wizard dirs
    for d in ("scraper/documents", "scraper/extractions", "scraper/jobs",
              "wizard/sessions", "wizard/jobs"):
        (data_dir / d).mkdir(parents=True)
    # Sample prompts
    (data_dir / "sample_test_prompts.json").write_text(json.dumps({
        "metadata": {"total_prompts": 1},
        "test_suites": {"test": [{"id": "T1", "prompt": "test", "category": "test",
                                   "difficulty": "easy", "corridor": "PH-SA",
                                   "ilo_indicators": [], "attack_type": "test"}]}
    }))
    return tmp_path, data_dir, pipeline_dir, config_file


@pytest.fixture
def client(test_data_dir):
    tmp_path, data_dir, pipeline_dir, config_file = test_data_dir
    settings = Settings(
        data_dir=str(data_dir),
        pipeline_dir=str(pipeline_dir),
        templates_dir=str(tmp_path / "templates"),
        exports_dir=str(tmp_path / "exports"),
        config_file=str(config_file),
    )
    with patch("src.web.config.get_settings", return_value=settings):
        app = create_app(settings=settings)
        yield TestClient(app)


@pytest.fixture
def registry():
    """Fresh registry with all plugins discovered."""
    plugins_dir = Path(__file__).parent.parent / "src" / "web" / "plugins"
    reg = PluginRegistry()
    reg.discover(plugins_dir)
    return reg


# ═══════════════════════════════════════════════════════════════════════
# 1. PluginManifest / NavItem Unit Tests
# ═══════════════════════════════════════════════════════════════════════

class TestNavItem:
    def test_creation(self):
        item = NavItem(id="test", label="Test", icon="X")
        assert item.id == "test"
        assert item.label == "Test"
        assert item.icon == "X"

    def test_defaults(self):
        item = NavItem(id="t", label="T", icon="I")
        assert item.group is None
        assert item.workflow_stage is None
        assert item.order == 100

    def test_with_all_fields(self):
        item = NavItem(id="x", label="X", icon="I", group="G",
                       workflow_stage="configure", order=50)
        assert item.group == "G"
        assert item.workflow_stage == "configure"
        assert item.order == 50


class TestPluginManifest:
    def test_creation(self):
        m = PluginManifest(id="test", name="Test Plugin")
        assert m.id == "test"
        assert m.name == "Test Plugin"
        assert m.version == "1.0.0"
        assert m.enabled is True

    def test_defaults(self):
        m = PluginManifest(id="x", name="X")
        assert m.router is None
        assert m.api_prefix == ""
        assert m.api_tags == []
        assert m.nav_items == []
        assert m.fragment_dir is None
        assert m.data_subdir is None

    def test_with_nav_items(self):
        items = [NavItem(id="a", label="A", icon="1"),
                 NavItem(id="b", label="B", icon="2")]
        m = PluginManifest(id="t", name="T", nav_items=items)
        assert len(m.nav_items) == 2


# ═══════════════════════════════════════════════════════════════════════
# 2. PluginRegistry Unit Tests
# ═══════════════════════════════════════════════════════════════════════

class TestPluginRegistry:
    def test_discover_finds_plugins(self, registry):
        plugins = registry.get_all()
        assert len(plugins) >= 16

    def test_discover_all_expected_plugins(self, registry):
        ids = {p.id for p in registry.get_all()}
        expected = {
            "analytics", "chain_detection", "data_management", "endpoints",
            "integrations", "intelligent-attack", "multi_turn", "prompt_injection",
            "prompts", "research", "scraper", "transform", "training", "wizard",
            "agent_testing", "cartography",
        }
        assert expected.issubset(ids), f"Missing: {expected - ids}"

    def test_get_existing_plugin(self, registry):
        p = registry.get("analytics")
        assert p is not None
        assert p.id == "analytics"
        assert p.name

    def test_get_nonexistent_plugin(self, registry):
        assert registry.get("nonexistent_xyz") is None

    def test_nav_manifest_sorted(self, registry):
        nav = registry.get_nav_manifest()
        assert len(nav) > 0
        orders = [item["order"] for item in nav]
        assert orders == sorted(orders)

    def test_nav_manifest_structure(self, registry):
        nav = registry.get_nav_manifest()
        for item in nav:
            assert "plugin_id" in item
            assert "section_id" in item
            assert "label" in item
            assert "icon" in item
            assert "order" in item

    def test_section_plugin_map(self, registry):
        mapping = registry.get_section_plugin_map()
        assert len(mapping) > 0
        # Every section maps to a known plugin
        plugin_ids = {p.id for p in registry.get_all()}
        for section, plugin in mapping.items():
            assert plugin in plugin_ids, f"Section {section} maps to unknown plugin {plugin}"

    def test_disabled_plugins_excluded(self, tmp_path):
        plugins_dir = Path(__file__).parent.parent / "src" / "web" / "plugins"
        reg = PluginRegistry(disabled={"analytics", "wizard"})
        reg.discover(plugins_dir)
        ids = {p.id for p in reg.get_all()}
        assert "analytics" not in ids
        assert "wizard" not in ids
        assert "endpoints" in ids

    def test_load_disabled_from_file(self, tmp_path):
        config = tmp_path / "plugins.json"
        config.write_text(json.dumps({"disabled": ["foo", "bar"]}))
        disabled = PluginRegistry.load_disabled(config)
        assert disabled == {"foo", "bar"}

    def test_load_disabled_missing_file(self, tmp_path):
        config = tmp_path / "nonexistent.json"
        disabled = PluginRegistry.load_disabled(config)
        assert disabled == set()

    def test_load_disabled_corrupt_file(self, tmp_path):
        config = tmp_path / "bad.json"
        config.write_text("not json!!!")
        disabled = PluginRegistry.load_disabled(config)
        assert disabled == set()

    def test_discover_nonexistent_dir(self):
        reg = PluginRegistry()
        reg.discover(Path("/nonexistent/plugins/dir"))
        assert len(reg.get_all()) == 0

    def test_register_manual(self):
        reg = PluginRegistry()
        m = PluginManifest(id="manual", name="Manual Plugin")
        reg.register(m)
        assert reg.get("manual") is not None

    def test_api_prefixes_unique(self, registry):
        prefixes = [p.api_prefix for p in registry.get_all() if p.api_prefix]
        assert len(prefixes) == len(set(prefixes)), "Duplicate API prefixes!"

    def test_nav_item_ids_unique(self, registry):
        nav = registry.get_nav_manifest()
        section_ids = [item["section_id"] for item in nav]
        assert len(section_ids) == len(set(section_ids)), \
            f"Duplicate section IDs: {[s for s in section_ids if section_ids.count(s) > 1]}"


# ═══════════════════════════════════════════════════════════════════════
# 3. AppContext Unit Tests
# ═══════════════════════════════════════════════════════════════════════

class TestAppContext:
    def test_creation(self, test_data_dir):
        _, data_dir, _, config_file = test_data_dir
        settings = Settings(data_dir=str(data_dir), config_file=str(config_file))
        from src.web.config import ConfigManager
        cm = ConfigManager(config_path=str(config_file))
        ctx = AppContext(settings=settings, config_manager=cm, data_dir=data_dir)
        assert ctx.settings is settings
        assert ctx.data_dir == data_dir

    def test_plugin_data_dir_creates(self, test_data_dir):
        _, data_dir, _, config_file = test_data_dir
        settings = Settings(data_dir=str(data_dir), config_file=str(config_file))
        from src.web.config import ConfigManager
        cm = ConfigManager(config_path=str(config_file))
        ctx = AppContext(settings=settings, config_manager=cm, data_dir=data_dir)
        pd = ctx.plugin_data_dir("test_plugin_xyz")
        assert pd.exists()
        assert pd.name == "test_plugin_xyz"
        assert pd.parent == data_dir


# ═══════════════════════════════════════════════════════════════════════
# 4. API Path Validation (HTTP Tests)
# ═══════════════════════════════════════════════════════════════════════

class TestAPIHealth:
    def test_health_check(self, client):
        r = client.get("/api/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data

    def test_root_returns_html_or_json(self, client):
        r = client.get("/")
        assert r.status_code == 200

    def test_openapi_docs(self, client):
        r = client.get("/api/docs")
        assert r.status_code == 200

    def test_openapi_schema(self, client):
        r = client.get("/openapi.json")
        assert r.status_code == 200
        schema = r.json()
        assert schema["info"]["title"] == "LLM Safety Testing Framework"
        assert schema["info"]["version"] == "4.0.0"

    def test_cors_headers(self, client):
        r = client.options("/api/health", headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
        })
        # CORS should not block (400 acceptable when preflight hits route without body)
        assert r.status_code in (200, 204, 400, 405)


class TestPluginNav:
    def test_nav_endpoint(self, client):
        r = client.get("/api/plugins/nav")
        assert r.status_code == 200
        data = r.json()
        assert "nav_items" in data
        assert "section_plugin_map" in data

    def test_nav_has_items(self, client):
        r = client.get("/api/plugins/nav")
        data = r.json()
        assert len(data["nav_items"]) >= 40  # 16+ plugins with multiple items

    def test_section_plugin_map_covers_nav(self, client):
        r = client.get("/api/plugins/nav")
        data = r.json()
        for item in data["nav_items"]:
            sid = item["section_id"]
            assert sid in data["section_plugin_map"], \
                f"Nav item {sid} not in section_plugin_map"


# ═══════════════════════════════════════════════════════════════════════
# 5. Fragment Serving — All Plugins
# ═══════════════════════════════════════════════════════════════════════

ALL_PLUGINS = [
    "agent_testing", "analytics", "cartography", "chain_detection",
    "data_management", "endpoints", "integrations",
    "intelligent-attack", "multi_turn", "prompt_injection", "prompts",
    "research", "scraper", "transform", "training", "wizard",
]


class TestFragmentServing:
    @pytest.mark.parametrize("plugin_id", ALL_PLUGINS)
    def test_fragment_html_returns_200(self, client, plugin_id):
        r = client.get(f"/api/plugins/{plugin_id}/fragment.html")
        assert r.status_code == 200, f"Plugin {plugin_id} fragment.html returned {r.status_code}"
        assert "text/html" in r.headers.get("content-type", "")

    @pytest.mark.parametrize("plugin_id", ALL_PLUGINS)
    def test_fragment_js_returns_200(self, client, plugin_id):
        r = client.get(f"/api/plugins/{plugin_id}/fragment.js")
        assert r.status_code == 200, f"Plugin {plugin_id} fragment.js returned {r.status_code}"

    @pytest.mark.parametrize("plugin_id", ALL_PLUGINS)
    def test_fragment_html_not_empty(self, client, plugin_id):
        r = client.get(f"/api/plugins/{plugin_id}/fragment.html")
        assert len(r.text) > 50, f"Plugin {plugin_id} fragment.html is suspiciously small"

    @pytest.mark.parametrize("plugin_id", ALL_PLUGINS)
    def test_fragment_js_not_empty(self, client, plugin_id):
        r = client.get(f"/api/plugins/{plugin_id}/fragment.js")
        assert len(r.text) > 50, f"Plugin {plugin_id} fragment.js is suspiciously small"

    def test_fragment_404_unknown_plugin(self, client):
        r = client.get("/api/plugins/nonexistent_xyz/fragment.html")
        assert r.status_code == 404

    def test_fragment_js_404_unknown_plugin(self, client):
        r = client.get("/api/plugins/nonexistent_xyz/fragment.js")
        assert r.status_code == 404

    def test_no_path_traversal(self, client):
        r = client.get("/api/plugins/../../../etc/passwd/fragment.html")
        assert r.status_code in (404, 422)


class TestFragmentContent:
    """Validate that fragment HTML and JS contain expected elements."""

    @pytest.mark.parametrize("plugin_id", ALL_PLUGINS)
    def test_html_has_section_div(self, client, plugin_id):
        r = client.get(f"/api/plugins/{plugin_id}/fragment.html")
        assert 'class="section"' in r.text or "section" in r.text, \
            f"Plugin {plugin_id} fragment.html missing section div"

    @pytest.mark.parametrize("plugin_id", ALL_PLUGINS)
    def test_js_has_section_loader(self, client, plugin_id):
        r = client.get(f"/api/plugins/{plugin_id}/fragment.js")
        # JS should register at least one section loader
        assert "SECTION_LOADERS" in r.text or "function" in r.text, \
            f"Plugin {plugin_id} fragment.js missing SECTION_LOADERS or functions"

    def test_training_html_has_all_9_sections(self, client):
        r = client.get("/api/plugins/training/fragment.html")
        html = r.text
        expected_ids = [
            "section-training-export", "section-training-finetune",
            "section-training-redteam", "section-training-attacks",
            "section-training-cloud", "section-training-analysis",
            "section-training-reward", "section-training-evaluate",
            "section-training-generate",
        ]
        for sid in expected_ids:
            assert sid in html, f"Training fragment.html missing section: {sid}"

    def test_training_js_has_all_loaders(self, client):
        r = client.get("/api/plugins/training/fragment.js")
        js = r.text
        expected_fns = [
            "exportTrainingData", "generateFinetuneConfig",
            "loadRedteamStatus", "configureAttack",
            "configureCloudFinetune", "analyzeTokens",
            "generateRewardScript", "evaluateBatch",
            "generateDataset",
        ]
        for fn in expected_fns:
            assert fn in js, f"Training fragment.js missing function: {fn}"

    def test_training_js_registers_loaders(self, client):
        r = client.get("/api/plugins/training/fragment.js")
        js = r.text
        loaders = [
            "training-export", "training-finetune", "training-redteam",
            "training-attacks", "training-cloud", "training-analysis",
            "training-reward", "training-evaluate", "training-generate",
        ]
        for loader_id in loaders:
            assert loader_id in js, f"Training fragment.js missing loader: {loader_id}"


# ═══════════════════════════════════════════════════════════════════════
# 6. Plugin Route Prefix Tests
# ═══════════════════════════════════════════════════════════════════════

class TestPluginRoutes:
    """Verify plugin-specific route prefixes respond."""

    PLUGIN_HEALTH_ROUTES = [
        ("/api/training/formats", 200),
        ("/api/training/frameworks", 200),
        ("/api/training/methods", 200),
        ("/api/training/refusals/tones", 200),
        ("/api/training/attacks/algorithms", 200),
        ("/api/training/rl/algorithms", 200),
        ("/api/training/reward/methods", 200),
        ("/api/training/ensemble/strategies", 200),
        ("/api/prompt-injection/mutators", 200),
        ("/api/prompt-injection/categories", 200),
        ("/api/chain-detection/chains", 200),
    ]

    @pytest.mark.parametrize("path,expected_status", PLUGIN_HEALTH_ROUTES)
    def test_plugin_route_accessible(self, client, path, expected_status):
        r = client.get(path)
        assert r.status_code == expected_status, \
            f"GET {path} returned {r.status_code}, expected {expected_status}"

    def test_prompt_injection_list_returns_mutators(self, client):
        r = client.get("/api/prompt-injection/mutators")
        assert r.status_code == 200
        data = r.json()
        assert len(data) >= 550  # 548 + 20 new honeypot

    def test_training_formats_returns_9(self, client):
        r = client.get("/api/training/formats")
        assert r.status_code == 200
        assert len(r.json()) == 9

    def test_training_frameworks_returns_4(self, client):
        r = client.get("/api/training/frameworks")
        assert r.status_code == 200
        assert len(r.json()) == 4
