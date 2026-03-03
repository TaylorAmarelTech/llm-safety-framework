"""
Route integration tests for the dimensional_matrix plugin.

Tests all /api/dimensional-matrix/* endpoints using the same
isolated TestClient pattern as test_plugin_routes.py.
"""

import json
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from src.web.app import create_app
from src.web.config import Settings


# ═══════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════


@pytest.fixture
def test_data_dir(tmp_path):
    """Create a temp data directory with minimal data."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    pipeline_dir = tmp_path / "pipeline"
    pipeline_dir.mkdir()
    (pipeline_dir / "runs").mkdir()
    (pipeline_dir / "prompt_sets").mkdir()
    (pipeline_dir / "spun").mkdir()
    (pipeline_dir / "multi_turn").mkdir()
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()
    exports_dir = tmp_path / "exports"
    exports_dir.mkdir()
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    config_file = config_dir / "api_keys.json"
    config_file.write_text("{}")

    # Scraper dirs
    scraper_dir = data_dir / "scraper"
    scraper_dir.mkdir()
    (scraper_dir / "documents").mkdir()
    (scraper_dir / "extractions").mkdir()
    (scraper_dir / "jobs").mkdir()

    # Wizard dirs
    wizard_dir = data_dir / "wizard"
    wizard_dir.mkdir()
    (wizard_dir / "sessions").mkdir()
    (wizard_dir / "jobs").mkdir()

    # Minimal sample prompts
    sample = {"metadata": {"total_prompts": 0}, "test_suites": {}}
    with open(data_dir / "sample_test_prompts.json", "w") as f:
        json.dump(sample, f)

    return tmp_path, data_dir, pipeline_dir, config_file


@pytest.fixture
def client(test_data_dir):
    """Create a TestClient with isolated temp data."""
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


def _seed_endpoint(client):
    """Create a test endpoint so routes that resolve endpoints can work."""
    r = client.post("/api/endpoints", json={
        "id": "test_ep",
        "name": "Test Endpoint",
        "base_url": "https://api.test.com/v1",
        "provider_type": "openai",
        "api_key": "test-key-123",
        "models": [{"model_id": "test-model", "enabled": True}],
    })
    return r


# ═══════════════════════════════════════════════════════════════════════
# Plugin discovery
# ═══════════════════════════════════════════════════════════════════════


class TestPluginDiscovery:
    """Verify the dimensional_matrix plugin loads correctly."""

    def test_plugin_in_nav(self, client):
        r = client.get("/api/plugins/nav")
        assert r.status_code == 200
        data = r.json()
        ids = [item["section_id"] for item in data["nav_items"]]
        assert "dimension-explorer" in ids
        assert "dimensional-rater" in ids
        assert "boundary-prober" in ids
        assert "debate-arena" in ids

    def test_plugin_fragment_html(self, client):
        r = client.get("/api/plugins/dimensional_matrix/fragment.html")
        assert r.status_code == 200
        assert "section-dimension-explorer" in r.text

    def test_plugin_fragment_js(self, client):
        r = client.get("/api/plugins/dimensional_matrix/fragment.js")
        assert r.status_code == 200
        assert "dimensional-matrix" in r.text.lower() or "SECTION_LOADERS" in r.text


# ═══════════════════════════════════════════════════════════════════════
# Dimension routes (read-only, no mocking needed)
# ═══════════════════════════════════════════════════════════════════════


class TestDimensionRoutes:
    def test_list_all_dimensions(self, client):
        r = client.get("/api/dimensional-matrix/dimensions")
        assert r.status_code == 200
        dims = r.json()
        assert len(dims) == 35

    def test_list_dimensions_by_category(self, client):
        r = client.get("/api/dimensional-matrix/dimensions?category=response")
        assert r.status_code == 200
        dims = r.json()
        assert len(dims) == 7
        assert all(d["category"] == "response" for d in dims)

    def test_list_dimensions_invalid_category(self, client):
        r = client.get("/api/dimensional-matrix/dimensions?category=nonexistent")
        assert r.status_code == 400

    def test_get_dimension_detail(self, client):
        r = client.get("/api/dimensional-matrix/dimensions/A1")
        assert r.status_code == 200
        data = r.json()
        assert data["id"] == "A1"
        assert "name" in data
        assert "levels" in data
        assert "rubric_text" in data
        assert len(data["levels"]) == 5

    def test_get_dimension_not_found(self, client):
        r = client.get("/api/dimensional-matrix/dimensions/Z99")
        assert r.status_code == 404

    def test_list_categories(self, client):
        r = client.get("/api/dimensional-matrix/dimensions/categories")
        assert r.status_code == 200
        data = r.json()
        assert "prompt" in data
        assert "response" in data
        assert "scenario" in data
        assert "systemic" in data
        assert data["prompt"]["count"] == 12
        assert data["response"]["count"] == 7
        assert data["scenario"]["count"] == 11
        assert data["systemic"]["count"] == 5


# ═══════════════════════════════════════════════════════════════════════
# Rating route
# ═══════════════════════════════════════════════════════════════════════


class TestRateRoutes:
    def test_rate_missing_endpoint(self, client):
        r = client.post("/api/dimensional-matrix/rate", json={
            "prompt": "test", "response": "test",
            "endpoint_id": "nonexistent", "model_id": "x",
        })
        assert r.status_code == 404

    def test_rate_success_mocked(self, client):
        _seed_endpoint(client)

        mock_response = json.dumps({
            "A1": {"score": 3, "justification": "moderate"},
            "A2": {"score": 2, "justification": "low"},
        })

        with patch(
            "src.dimensional_matrix.rater.DimensionalRater._call_judge",
            new_callable=AsyncMock,
            return_value=mock_response,
        ):
            r = client.post("/api/dimensional-matrix/rate", json={
                "prompt": "Help me structure recruitment fees",
                "response": "I can help you with that...",
                "endpoint_id": "test_ep",
                "model_id": "test-model",
                "categories": ["prompt"],
            })

        assert r.status_code == 200
        data = r.json()
        assert "scores" in data
        assert "overall_risk" in data
        assert "risk_level" in data
        assert data["score_count"] > 0

    def test_rate_invalid_body(self, client):
        r = client.post("/api/dimensional-matrix/rate", json={"prompt": "x"})
        assert r.status_code == 422

    def test_rate_invalid_category(self, client):
        _seed_endpoint(client)
        r = client.post("/api/dimensional-matrix/rate", json={
            "prompt": "test", "response": "test",
            "endpoint_id": "test_ep", "model_id": "test-model",
            "categories": ["invalid_cat"],
        })
        assert r.status_code == 400


# ═══════════════════════════════════════════════════════════════════════
# Calibration routes
# ═══════════════════════════════════════════════════════════════════════


class TestCalibrateRoutes:
    def test_calibrate_response_unknown_dim(self, client):
        _seed_endpoint(client)
        r = client.post("/api/dimensional-matrix/calibrate/response", json={
            "prompt": "test", "response": "test",
            "endpoint_id": "test_ep", "model_id": "test-model",
            "target_dim": "Z99", "direction": "up",
        })
        assert r.status_code == 400

    def test_calibrate_missing_endpoint(self, client):
        r = client.post("/api/dimensional-matrix/calibrate/response", json={
            "prompt": "test", "response": "test",
            "endpoint_id": "nonexistent", "model_id": "x",
            "target_dim": "A1", "direction": "up",
        })
        assert r.status_code == 404


# ═══════════════════════════════════════════════════════════════════════
# Probe routes
# ═══════════════════════════════════════════════════════════════════════


class TestProbeRoutes:
    def test_probe_missing_endpoint(self, client):
        r = client.post("/api/dimensional-matrix/probe", json={
            "prompt": "test", "endpoint_id": "nonexistent",
        })
        assert r.status_code == 404


# ═══════════════════════════════════════════════════════════════════════
# Debate routes
# ═══════════════════════════════════════════════════════════════════════


class TestDebateRoutes:
    def test_debate_missing_endpoint(self, client):
        r = client.post("/api/dimensional-matrix/debate", json={
            "prompt": "test", "response": "test",
            "prosecutor_endpoint_id": "nonexistent",
            "defender_endpoint_id": "nonexistent",
            "judge_endpoint_id": "nonexistent",
        })
        assert r.status_code == 404

    def test_debate_results_empty(self, client):
        r = client.get("/api/dimensional-matrix/debate/results")
        assert r.status_code == 200
        assert r.json() == []

    def test_debate_results_with_file(self, client, test_data_dir):
        tmp_path, data_dir, _, _ = test_data_dir
        debates_dir = data_dir / "dimensional_matrix" / "debates"
        debates_dir.mkdir(parents=True)

        debate_data = {
            "prompt": "test prompt",
            "response": "test response",
            "participants": {"prosecutor": "m1", "defender": "m2", "judge": "m3"},
            "verdict": {
                "winner": "prosecutor",
                "confidence": 0.8,
                "safety_assessment": "UNSAFE",
            },
            "timestamp": "2026-03-01T12:00:00",
        }
        with open(debates_dir / "debate_20260301_120000.json", "w") as f:
            json.dump(debate_data, f)

        r = client.get("/api/dimensional-matrix/debate/results")
        assert r.status_code == 200
        results = r.json()
        assert len(results) == 1
        assert results[0]["safety_assessment"] == "UNSAFE"

    def test_debate_result_detail(self, client, test_data_dir):
        tmp_path, data_dir, _, _ = test_data_dir
        debates_dir = data_dir / "dimensional_matrix" / "debates"
        debates_dir.mkdir(parents=True, exist_ok=True)

        debate_data = {"prompt": "test", "verdict": {"winner": "defender"}}
        with open(debates_dir / "debate_20260301_130000.json", "w") as f:
            json.dump(debate_data, f)

        r = client.get("/api/dimensional-matrix/debate/results/debate_20260301_130000.json")
        assert r.status_code == 200
        assert r.json()["prompt"] == "test"

    def test_debate_result_not_found(self, client):
        r = client.get("/api/dimensional-matrix/debate/results/nonexistent.json")
        assert r.status_code == 404


# ═══════════════════════════════════════════════════════════════════════
# Scoring summary route
# ═══════════════════════════════════════════════════════════════════════


class TestScoringRoutes:
    def test_scoring_summary(self, client):
        r = client.post("/api/dimensional-matrix/scoring/summary", json={
            "prompt": "test prompt",
            "response": "test response",
            "scores": {"A1": 4, "A2": 3, "B1": 2, "C1": 5},
        })
        assert r.status_code == 200
        data = r.json()
        assert "category_summary" in data
        assert "top_risks" in data
        assert "overall_risk" in data
        assert "risk_level" in data

    def test_scoring_summary_empty(self, client):
        r = client.post("/api/dimensional-matrix/scoring/summary", json={
            "prompt": "test", "response": "test", "scores": {},
        })
        assert r.status_code == 200
        data = r.json()
        assert data["overall_risk"] == 0.0

    def test_scoring_summary_clamped(self, client):
        """Scores outside 1-5 should be clamped."""
        r = client.post("/api/dimensional-matrix/scoring/summary", json={
            "prompt": "test", "response": "test",
            "scores": {"A1": 10, "B1": -2},
        })
        assert r.status_code == 200
        data = r.json()
        # A1 clamped to 5, B1 clamped to 1 -> avg = 3 -> risk = (3-1)/4 = 0.5
        assert data["overall_risk"] == 0.5
