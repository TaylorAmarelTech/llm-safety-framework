"""Tests for the UnifiedAPIClient."""

import json
from unittest.mock import AsyncMock, patch, MagicMock

import pytest

from src.api_client import UnifiedAPIClient


@pytest.fixture
def openai_endpoint():
    """Sample OpenAI endpoint config."""
    return {
        "id": "openai",
        "name": "OpenAI",
        "provider_type": "openai",
        "base_url": "https://api.openai.com/v1",
        "api_key": "sk-test-key-123",
        "enabled": True,
        "auth_header": "Authorization",
        "auth_prefix": "Bearer",
        "extra_headers": {},
        "request_format": "openai",
    }


@pytest.fixture
def anthropic_endpoint():
    """Sample Anthropic endpoint config."""
    return {
        "id": "anthropic",
        "name": "Anthropic",
        "provider_type": "anthropic",
        "base_url": "https://api.anthropic.com",
        "api_key": "sk-ant-test-key-123",
        "enabled": True,
        "auth_header": "x-api-key",
        "auth_prefix": "",
        "extra_headers": {"anthropic-version": "2023-06-01"},
        "request_format": "anthropic",
    }


@pytest.fixture
def mistral_endpoint():
    """Sample Mistral endpoint config."""
    return {
        "id": "mistral",
        "name": "Mistral AI",
        "provider_type": "mistral",
        "base_url": "https://api.mistral.ai/v1",
        "api_key": "test-mistral-key",
        "enabled": True,
        "auth_header": "Authorization",
        "auth_prefix": "Bearer",
        "extra_headers": {},
        "request_format": "openai",
    }


class TestClientInit:
    """Test client initialization."""

    def test_openai_client(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        assert client.endpoint == openai_endpoint

    def test_anthropic_client(self, anthropic_endpoint):
        client = UnifiedAPIClient(anthropic_endpoint)
        assert client.endpoint == anthropic_endpoint


class TestPreviewRequest:
    """Test API call preview generation."""

    def test_openai_preview(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        preview = client.preview_request("gpt-4o-mini")
        assert preview["body"]["model"] == "gpt-4o-mini"
        assert "chat/completions" in preview["url"]
        assert "Bearer" in preview["headers"]["Authorization"]

    def test_anthropic_preview(self, anthropic_endpoint):
        client = UnifiedAPIClient(anthropic_endpoint)
        preview = client.preview_request("claude-3-haiku-20240307")
        assert preview["body"]["model"] == "claude-3-haiku-20240307"
        assert "messages" in preview["url"]
        assert "x-api-key" in preview["headers"]

    def test_mistral_preview(self, mistral_endpoint):
        client = UnifiedAPIClient(mistral_endpoint)
        preview = client.preview_request("mistral-large-latest")
        assert preview["body"]["model"] == "mistral-large-latest"
        assert preview["method"] == "POST"

    def test_preview_structure(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        preview = client.preview_request("test-model")
        assert "url" in preview
        assert "headers" in preview
        assert "body" in preview
        assert "method" in preview


class TestRequestFormat:
    """Test request format detection."""

    def test_openai_format(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        assert client.endpoint["request_format"] == "openai"

    def test_anthropic_format(self, anthropic_endpoint):
        client = UnifiedAPIClient(anthropic_endpoint)
        assert client.endpoint["request_format"] == "anthropic"


class TestOpenAIPreview:
    """Test OpenAI-format preview details."""

    def test_preview_body_fields(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        preview = client.preview_request("gpt-4o")
        body = preview["body"]
        assert "model" in body
        assert "messages" in body
        assert body["model"] == "gpt-4o"

    def test_preview_url(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        preview = client.preview_request("gpt-4o")
        assert preview["url"] == "https://api.openai.com/v1/chat/completions"


class TestAnthropicPreview:
    """Test Anthropic-format preview details."""

    def test_preview_url(self, anthropic_endpoint):
        client = UnifiedAPIClient(anthropic_endpoint)
        preview = client.preview_request("claude-3-opus-20240229")
        assert preview["url"] == "https://api.anthropic.com/v1/messages"

    def test_preview_headers(self, anthropic_endpoint):
        client = UnifiedAPIClient(anthropic_endpoint)
        preview = client.preview_request("claude-3-haiku")
        assert "x-api-key" in preview["headers"]
        assert "anthropic-version" in preview["headers"]
        assert preview["headers"]["anthropic-version"] == "2023-06-01"


class TestHeaders:
    """Test header construction."""

    def test_bearer_auth(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        preview = client.preview_request("gpt-4o")
        assert preview["headers"]["Authorization"] == "Bearer <API_KEY>"

    def test_direct_key_auth(self, anthropic_endpoint):
        client = UnifiedAPIClient(anthropic_endpoint)
        preview = client.preview_request("claude-3-haiku")
        assert preview["headers"]["x-api-key"] == "<API_KEY>"

    def test_extra_headers(self, anthropic_endpoint):
        client = UnifiedAPIClient(anthropic_endpoint)
        preview = client.preview_request("claude-3-haiku")
        assert "anthropic-version" in preview["headers"]

    def test_content_type(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        preview = client.preview_request("gpt-4o")
        assert preview["headers"]["Content-Type"] == "application/json"


class TestEdgeCases:
    """Test edge cases."""

    def test_empty_api_key(self):
        ep = {
            "id": "test",
            "base_url": "https://example.com",
            "api_key": "",
            "auth_header": "Authorization",
            "auth_prefix": "Bearer",
            "extra_headers": {},
            "request_format": "openai",
        }
        client = UnifiedAPIClient(ep)
        preview = client.preview_request("model-1")
        assert preview["body"]["model"] == "model-1"

    def test_custom_auth_header(self):
        ep = {
            "id": "custom",
            "base_url": "https://custom.api.com/v1",
            "api_key": "custom-key",
            "auth_header": "X-Custom-Auth",
            "auth_prefix": "Token",
            "extra_headers": {"X-Custom": "value"},
            "request_format": "openai",
        }
        client = UnifiedAPIClient(ep)
        preview = client.preview_request("custom-model")
        assert "X-Custom-Auth" in preview["headers"]
        assert preview["headers"]["X-Custom-Auth"] == "Token <API_KEY>"
        assert preview["headers"]["X-Custom"] == "value"

    def test_no_extra_headers(self, openai_endpoint):
        client = UnifiedAPIClient(openai_endpoint)
        preview = client.preview_request("model")
        # Should have auth + content-type at minimum
        assert len(preview["headers"]) >= 2
