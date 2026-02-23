"""Tests for the v2 endpoint-centric configuration system."""

import json
import os
import tempfile
from pathlib import Path

import pytest

from src.web.config import ConfigManager, Settings, get_settings


@pytest.fixture
def temp_config_dir(tmp_path):
    """Create a temp directory with a fresh config."""
    config_file = tmp_path / "config.json"
    return tmp_path, config_file


@pytest.fixture
def config_manager(temp_config_dir):
    """Create a ConfigManager with temp storage."""
    tmp_path, config_file = temp_config_dir
    cm = ConfigManager(config_path=str(config_file))
    return cm


class TestDefaultEndpoints:
    """Test that default endpoints are created on init."""

    def test_defaults_created(self, config_manager):
        endpoints = config_manager.get_all_endpoints()
        assert len(endpoints) >= 5
        ids = [ep["id"] for ep in endpoints]
        assert "openai" in ids
        assert "anthropic" in ids
        assert "mistral" in ids
        assert "together" in ids
        assert "openrouter" in ids

    def test_default_endpoint_structure(self, config_manager):
        ep = config_manager.get_endpoint("openai")
        assert ep is not None
        assert ep["provider_type"] == "openai"
        assert "base_url" in ep
        assert "api_key" in ep
        assert ep["enabled"] is True

    def test_default_models_exist(self, config_manager):
        models = config_manager.get_all_models()
        assert len(models) > 0
        # OpenAI models should exist
        model_ids = [m["id"] for m in models]
        assert any("gpt" in m_id.lower() for m_id in model_ids)


class TestEndpointCRUD:
    """Test endpoint create, read, update, delete."""

    def test_create_endpoint(self, config_manager):
        new_ep = {
            "id": "custom-1",
            "name": "Custom Endpoint",
            "provider_type": "custom",
            "base_url": "https://my-api.example.com/v1",
            "api_key": "test-key-123",
            "enabled": True,
            "request_format": "openai",
        }
        config_manager.create_endpoint(new_ep)
        ep = config_manager.get_endpoint("custom-1")
        assert ep is not None
        assert ep["name"] == "Custom Endpoint"
        assert ep["base_url"] == "https://my-api.example.com/v1"

    def test_update_endpoint(self, config_manager):
        config_manager.update_endpoint("openai", {"name": "My OpenAI"})
        ep = config_manager.get_endpoint("openai")
        assert ep["name"] == "My OpenAI"

    def test_update_endpoint_key(self, config_manager):
        config_manager.update_endpoint("mistral", {"api_key": "new-key-456"})
        ep = config_manager.get_endpoint("mistral")
        assert ep["api_key"] == "new-key-456"

    def test_delete_endpoint(self, config_manager):
        config_manager.create_endpoint({
            "id": "to-delete",
            "name": "Delete Me",
            "provider_type": "custom",
            "base_url": "https://delete.me",
        })
        assert config_manager.get_endpoint("to-delete") is not None
        config_manager.delete_endpoint("to-delete")
        assert config_manager.get_endpoint("to-delete") is None

    def test_get_nonexistent_endpoint(self, config_manager):
        assert config_manager.get_endpoint("nonexistent") is None


class TestModelCRUD:
    """Test model create, read, update, delete."""

    def test_create_model(self, config_manager):
        new_model = {
            "id": "openai/gpt-test",
            "name": "GPT Test",
            "endpoint_id": "openai",
            "model_id": "gpt-test",
            "enabled": False,
            "temperature": 0.5,
            "max_tokens": 1000,
        }
        config_manager.create_model(new_model)
        model = config_manager.get_model("openai/gpt-test")
        assert model is not None
        assert model["name"] == "GPT Test"
        assert model["temperature"] == 0.5

    def test_update_model(self, config_manager):
        models = config_manager.get_all_models()
        if models:
            first_model = models[0]
            config_manager.update_model(first_model["id"], {"temperature": 0.3})
            updated = config_manager.get_model(first_model["id"])
            assert updated["temperature"] == 0.3

    def test_get_enabled_models(self, config_manager):
        # Enable a model and ensure its endpoint has an API key
        models = config_manager.get_all_models()
        if models:
            model = models[0]
            config_manager.update_model(model["id"], {"enabled": True})
            config_manager.update_endpoint(model["endpoint_id"], {"api_key": "test-key"})
            enabled = config_manager.get_enabled_models()
            assert len(enabled) >= 1

    def test_get_models_for_endpoint(self, config_manager):
        models = config_manager.get_models_for_endpoint("openai")
        assert all(m["endpoint_id"] == "openai" for m in models)


class TestConfigPersistence:
    """Test that config is saved and loaded correctly."""

    def test_config_saves_to_disk(self, temp_config_dir):
        tmp_path, config_file = temp_config_dir
        cm = ConfigManager(config_path=str(tmp_path / "config.json"))
        cm.update_endpoint("openai", {"api_key": "persist-test-key"})

        # Create a new instance to force reload
        cm2 = ConfigManager(config_path=str(tmp_path / "config.json"))
        ep = cm2.get_endpoint("openai")
        assert ep["api_key"] == "persist-test-key"

    def test_export_import(self, config_manager):
        config_manager.update_endpoint("openai", {"api_key": "export-key"})
        exported = config_manager.export_config()
        assert "endpoints" in exported
        assert isinstance(exported["endpoints"], dict)
        # API key should be masked (None) by default
        assert exported["endpoints"]["openai"]["api_key"] is None


class TestV1Migration:
    """Test migration from v1 (provider-grouped) to v2 (endpoint-centric)."""

    def test_v1_config_detected(self, temp_config_dir):
        tmp_path, config_file = temp_config_dir
        # v1 format: models dict with provider keys containing model dicts with model_id
        v1_config = {
            "models": {
                "mistral": {
                    "mistral-large-latest": {
                        "model_id": "mistral-large-latest",
                        "name": "Mistral Large",
                        "api_key": "v1-mistral-key",
                        "enabled": True,
                    }
                },
                "openai": {
                    "gpt-4o": {
                        "model_id": "gpt-4o",
                        "name": "GPT-4o",
                        "api_key": "v1-openai-key",
                        "enabled": False,
                    }
                },
            }
        }
        with open(config_file, 'w') as f:
            json.dump(v1_config, f)

        cm = ConfigManager(config_path=str(tmp_path / "config.json"))
        # After migration, endpoints should exist with keys preserved
        endpoints = cm.get_all_endpoints()
        assert len(endpoints) >= 2

        mistral = cm.get_endpoint("mistral")
        if mistral:
            assert mistral["api_key"] == "v1-mistral-key"


class TestSettings:
    """Test Settings model."""

    def test_default_settings(self):
        settings = get_settings()
        assert settings.data_dir is not None
        assert settings.pipeline_dir is not None
