"""
Configuration management for the web dashboard.

Endpoint-centric design: API endpoints are top-level objects,
models are children of endpoints with per-model settings.
"""

import os
import json
import threading
from pathlib import Path
from typing import List, Dict, Any, Optional
from functools import lru_cache

from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings


# =============================================================================
# Data Models
# =============================================================================

class EndpointConfig(BaseModel):
    """Configuration for a single API endpoint."""
    id: str
    name: str
    provider_type: str  # openai, anthropic, mistral, together, openrouter, custom
    base_url: str
    api_key: Optional[str] = None
    enabled: bool = True
    auth_header: str = "Authorization"
    auth_prefix: str = "Bearer"
    extra_headers: Dict[str, str] = Field(default_factory=dict)
    request_format: str = "openai"  # "openai" or "anthropic"
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ModelConfig(BaseModel):
    """Configuration for a single model on an endpoint."""
    id: str
    name: str
    endpoint_id: str
    model_id: str
    enabled: bool = False
    temperature: float = 0.7
    max_tokens: int = 2048
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    system_prompt: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Settings(BaseSettings):
    """Application settings."""
    data_dir: str = "data"
    templates_dir: str = "templates"
    exports_dir: str = "exports"
    config_file: str = "config/api_keys.json"
    pipeline_dir: str = "data/pipeline"

    host: str = "0.0.0.0"
    port: int = 8080
    debug: bool = False
    cors_origins: List[str] = ["http://localhost:8080", "http://localhost:8088", "http://127.0.0.1:8080", "http://127.0.0.1:8088"]

    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    mistral_api_key: Optional[str] = None
    together_api_key: Optional[str] = None
    openrouter_api_key: Optional[str] = None

    default_batch_size: int = 10
    max_concurrent_tests: int = 5
    test_timeout: int = 60

    model_config = ConfigDict(env_prefix="LLM_SAFETY_", env_file=".env")


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


# =============================================================================
# Default Endpoints & Models
# =============================================================================

def _default_endpoints() -> Dict[str, dict]:
    return {
        "openai": {
            "id": "openai",
            "name": "OpenAI",
            "provider_type": "openai",
            "base_url": "https://api.openai.com/v1",
            "api_key": None,
            "enabled": True,
            "auth_header": "Authorization",
            "auth_prefix": "Bearer",
            "extra_headers": {},
            "request_format": "openai",
        },
        "anthropic": {
            "id": "anthropic",
            "name": "Anthropic",
            "provider_type": "anthropic",
            "base_url": "https://api.anthropic.com",
            "api_key": None,
            "enabled": True,
            "auth_header": "x-api-key",
            "auth_prefix": "",
            "extra_headers": {"anthropic-version": "2023-06-01"},
            "request_format": "anthropic",
        },
        "mistral": {
            "id": "mistral",
            "name": "Mistral AI",
            "provider_type": "mistral",
            "base_url": "https://api.mistral.ai/v1",
            "api_key": None,
            "enabled": True,
            "auth_header": "Authorization",
            "auth_prefix": "Bearer",
            "extra_headers": {},
            "request_format": "openai",
        },
        "together": {
            "id": "together",
            "name": "Together AI",
            "provider_type": "together",
            "base_url": "https://api.together.xyz/v1",
            "api_key": None,
            "enabled": True,
            "auth_header": "Authorization",
            "auth_prefix": "Bearer",
            "extra_headers": {},
            "request_format": "openai",
        },
        "openrouter": {
            "id": "openrouter",
            "name": "OpenRouter",
            "provider_type": "openrouter",
            "base_url": "https://openrouter.ai/api/v1",
            "api_key": None,
            "enabled": True,
            "auth_header": "Authorization",
            "auth_prefix": "Bearer",
            "extra_headers": {
                "HTTP-Referer": "https://llm-safety-framework.local",
                "X-Title": "LLM Safety Testing Framework",
            },
            "request_format": "openai",
        },
    }


def _default_models() -> Dict[str, dict]:
    return {
        "openai/gpt-4o": {
            "id": "openai/gpt-4o", "name": "GPT-4o", "endpoint_id": "openai",
            "model_id": "gpt-4o", "enabled": False, "temperature": 0.7, "max_tokens": 4096,
        },
        "openai/gpt-4o-mini": {
            "id": "openai/gpt-4o-mini", "name": "GPT-4o Mini", "endpoint_id": "openai",
            "model_id": "gpt-4o-mini", "enabled": False, "temperature": 0.7, "max_tokens": 4096,
        },
        "openai/gpt-4-turbo": {
            "id": "openai/gpt-4-turbo", "name": "GPT-4 Turbo", "endpoint_id": "openai",
            "model_id": "gpt-4-turbo", "enabled": False, "temperature": 0.7, "max_tokens": 4096,
        },
        "anthropic/claude-sonnet-4-5": {
            "id": "anthropic/claude-sonnet-4-5", "name": "Claude Sonnet 4.5", "endpoint_id": "anthropic",
            "model_id": "claude-sonnet-4-5-20250929", "enabled": False, "temperature": 0.7, "max_tokens": 4096,
        },
        "anthropic/claude-haiku-4-5": {
            "id": "anthropic/claude-haiku-4-5", "name": "Claude Haiku 4.5", "endpoint_id": "anthropic",
            "model_id": "claude-haiku-4-5-20251001", "enabled": False, "temperature": 0.7, "max_tokens": 4096,
        },
        "anthropic/claude-opus-4-6": {
            "id": "anthropic/claude-opus-4-6", "name": "Claude Opus 4.6", "endpoint_id": "anthropic",
            "model_id": "claude-opus-4-6", "enabled": False, "temperature": 0.7, "max_tokens": 4096,
        },
        "mistral/mistral-large-latest": {
            "id": "mistral/mistral-large-latest", "name": "Mistral Large", "endpoint_id": "mistral",
            "model_id": "mistral-large-latest", "enabled": False, "temperature": 0.7, "max_tokens": 2048,
        },
        "mistral/mistral-small-latest": {
            "id": "mistral/mistral-small-latest", "name": "Mistral Small", "endpoint_id": "mistral",
            "model_id": "mistral-small-latest", "enabled": False, "temperature": 0.7, "max_tokens": 2048,
        },
        "together/meta-llama/Llama-3.3-70B-Instruct-Turbo": {
            "id": "together/meta-llama/Llama-3.3-70B-Instruct-Turbo", "name": "Llama 3.3 70B Turbo",
            "endpoint_id": "together", "model_id": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
            "enabled": False, "temperature": 0.7, "max_tokens": 2048,
        },
    }


# =============================================================================
# Config Manager
# =============================================================================

class ConfigManager:
    """
    Manages endpoint-centric configuration.

    Endpoints define API connections (URL, key, auth).
    Models are children of endpoints with per-model settings.
    """

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path or "config/api_keys.json")
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._config: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration, auto-migrating v1 if needed."""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if self._is_v1(data):
                data = self._migrate_v1_to_v2(data)
                self._save_raw(data)
            return data
        return self._default_config()

    def _is_v1(self, data: dict) -> bool:
        """Detect v1 config format (provider-grouped models)."""
        return "endpoints" not in data and "models" in data and isinstance(
            data["models"].get("openai", None), dict
        ) and any(
            isinstance(v, dict) and "model_id" in v
            for provider_models in data.get("models", {}).values()
            if isinstance(provider_models, dict)
            for v in provider_models.values()
            if isinstance(v, dict)
        )

    def _migrate_v1_to_v2(self, v1: dict) -> dict:
        """Migrate v1 provider-grouped config to v2 endpoint-centric."""
        endpoints = _default_endpoints()
        models = {}

        # Map v1 provider keys to endpoint IDs
        for provider, provider_models in v1.get("models", {}).items():
            if not isinstance(provider_models, dict):
                continue
            endpoint_id = provider
            if endpoint_id not in endpoints:
                continue

            for model_key, model_data in provider_models.items():
                if not isinstance(model_data, dict) or "model_id" not in model_data:
                    continue

                model_id_full = f"{endpoint_id}/{model_key}"
                # Transfer API key from model to endpoint
                if model_data.get("api_key") and not endpoints[endpoint_id].get("api_key"):
                    endpoints[endpoint_id]["api_key"] = model_data["api_key"]

                models[model_id_full] = {
                    "id": model_id_full,
                    "name": model_data.get("name", model_key),
                    "endpoint_id": endpoint_id,
                    "model_id": model_data.get("model_id", model_key),
                    "enabled": model_data.get("enabled", False),
                    "temperature": model_data.get("temperature", 0.7),
                    "max_tokens": model_data.get("max_tokens", 2048),
                }

        # Merge with default models
        default_models = _default_models()
        for k, v in default_models.items():
            if k not in models:
                models[k] = v

        return {
            "version": "2.0.0",
            "endpoints": endpoints,
            "models": models,
            "test_settings": v1.get("test_settings", {
                "default_batch_size": 10,
                "max_concurrent_tests": 5,
                "test_timeout": 60,
                "save_conversations": True,
                "evaluate_responses": True,
            }),
            "memory": v1.get("memory", {
                "system_context": "",
                "custom_instructions": "",
                "enabled": False,
            }),
        }

    def _default_config(self) -> Dict[str, Any]:
        """Return default v2 configuration."""
        return {
            "version": "2.0.0",
            "endpoints": _default_endpoints(),
            "models": _default_models(),
            "test_settings": {
                "default_batch_size": 10,
                "max_concurrent_tests": 5,
                "test_timeout": 60,
                "save_conversations": True,
                "evaluate_responses": True,
            },
            "memory": {
                "system_context": "",
                "custom_instructions": "",
                "enabled": False,
            },
        }

    def _save_raw(self, data: dict) -> None:
        """Write config dict to disk (caller must hold ``_lock`` for mutations)."""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def save(self) -> None:
        """Save current configuration to file (thread-safe)."""
        with self._lock:
            self._save_raw(self._config)

    # --- Endpoint Operations ---

    def get_all_endpoints(self) -> List[Dict[str, Any]]:
        """Get all configured endpoints."""
        return list(self._config.get("endpoints", {}).values())

    def get_endpoint(self, endpoint_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific endpoint by ID."""
        return self._config.get("endpoints", {}).get(endpoint_id)

    def create_endpoint(self, endpoint: dict) -> None:
        """Create a new endpoint."""
        with self._lock:
            eid = endpoint["id"]
            self._config.setdefault("endpoints", {})[eid] = endpoint
            self._save_raw(self._config)

    def update_endpoint(self, endpoint_id: str, updates: dict) -> None:
        """Update an existing endpoint."""
        with self._lock:
            ep = self._config.get("endpoints", {}).get(endpoint_id)
            if ep:
                ep.update(updates)
                self._save_raw(self._config)

    def delete_endpoint(self, endpoint_id: str) -> None:
        """Delete an endpoint and its models."""
        with self._lock:
            self._config.get("endpoints", {}).pop(endpoint_id, None)
            self._config["models"] = {
                k: v for k, v in self._config.get("models", {}).items()
                if v.get("endpoint_id") != endpoint_id
            }
            self._save_raw(self._config)

    def update_endpoint_key(self, endpoint_id: str, api_key: str) -> None:
        """Update the API key for an endpoint."""
        with self._lock:
            ep = self._config.get("endpoints", {}).get(endpoint_id)
            if ep:
                ep["api_key"] = api_key
                self._save_raw(self._config)

    # --- Model Operations ---

    def get_all_models(self) -> List[Dict[str, Any]]:
        """Get all configured models."""
        return list(self._config.get("models", {}).values())

    def get_models_for_endpoint(self, endpoint_id: str) -> List[Dict[str, Any]]:
        """Get all models belonging to an endpoint."""
        return [
            m for m in self._config.get("models", {}).values()
            if m.get("endpoint_id") == endpoint_id
        ]

    def get_enabled_models(self) -> List[Dict[str, Any]]:
        """Get only enabled models (with their endpoint info attached)."""
        result = []
        for m in self._config.get("models", {}).values():
            if m.get("enabled"):
                ep = self.get_endpoint(m.get("endpoint_id", ""))
                if ep and ep.get("enabled") and ep.get("api_key"):
                    result.append({**m, "_endpoint": ep})
        return result

    def get_model(self, model_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific model by ID."""
        return self._config.get("models", {}).get(model_id)

    def create_model(self, model: dict) -> None:
        """Create a new model under an endpoint."""
        with self._lock:
            mid = model["id"]
            self._config.setdefault("models", {})[mid] = model
            self._save_raw(self._config)

    def update_model(self, model_id: str, updates: dict) -> None:
        """Update model configuration."""
        with self._lock:
            m = self._config.get("models", {}).get(model_id)
            if m:
                m.update(updates)
                self._save_raw(self._config)

    def delete_model(self, model_id: str) -> None:
        """Delete a model."""
        with self._lock:
            self._config.get("models", {}).pop(model_id, None)
            self._save_raw(self._config)

    def toggle_model(self, model_id: str, enabled: bool) -> None:
        """Enable or disable a model."""
        self.update_model(model_id, {"enabled": enabled})

    # --- Memory Operations ---

    def get_memory_context(self) -> Dict[str, Any]:
        """Get memory/context settings."""
        return self._config.get("memory", {})

    def update_memory_context(
        self,
        system_context: Optional[str] = None,
        custom_instructions: Optional[str] = None,
        enabled: Optional[bool] = None,
    ) -> None:
        """Update memory/context settings."""
        with self._lock:
            mem = self._config.setdefault("memory", {})
            if system_context is not None:
                mem["system_context"] = system_context
            if custom_instructions is not None:
                mem["custom_instructions"] = custom_instructions
            if enabled is not None:
                mem["enabled"] = enabled
            self._save_raw(self._config)

    # --- Test Settings ---

    def get_test_settings(self) -> Dict[str, Any]:
        return self._config.get("test_settings", {})

    def update_test_settings(self, settings: dict) -> None:
        with self._lock:
            self._config.setdefault("test_settings", {}).update(settings)
            self._save_raw(self._config)

    # --- Export/Import ---

    def export_config(self, include_keys: bool = False) -> Dict[str, Any]:
        """Export configuration (optionally masking API keys)."""
        import copy
        config = copy.deepcopy(self._config)
        if not include_keys:
            for ep in config.get("endpoints", {}).values():
                ep["api_key"] = None
        return config

    def import_config(self, config: dict, merge: bool = True) -> None:
        """Import configuration from dict."""
        with self._lock:
            if merge:
                for key in ("endpoints", "models"):
                    if key in config and isinstance(config[key], dict):
                        self._config.setdefault(key, {}).update(config[key])
                for key in ("test_settings", "memory"):
                    if key in config:
                        self._config[key] = config[key]
            else:
                self._config = config
            self._save_raw(self._config)
