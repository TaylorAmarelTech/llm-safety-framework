"""
Configuration management for the web dashboard.

Handles API keys, model endpoints, and application settings.
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from functools import lru_cache

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class ModelConfig(BaseModel):
    """Configuration for a single LLM model."""
    name: str
    provider: str  # openai, anthropic, mistral, together, custom
    api_key: Optional[str] = None
    endpoint: Optional[str] = None
    model_id: str
    enabled: bool = True
    temperature: float = 0.7
    max_tokens: int = 2048
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Settings(BaseSettings):
    """Application settings."""

    # Paths
    data_dir: str = "data"
    templates_dir: str = "templates"
    exports_dir: str = "exports"
    config_file: str = "config/api_keys.json"

    # Server
    host: str = "0.0.0.0"
    port: int = 8080
    debug: bool = False

    # CORS
    cors_origins: List[str] = ["*"]

    # API Keys (can be set via environment variables)
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    mistral_api_key: Optional[str] = None
    together_api_key: Optional[str] = None

    # Test settings
    default_batch_size: int = 10
    max_concurrent_tests: int = 5
    test_timeout: int = 60

    class Config:
        env_prefix = "LLM_SAFETY_"
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


class ConfigManager:
    """
    Manages configuration including API keys and model endpoints.

    Stores configuration in a JSON file and provides methods for
    reading, updating, and validating settings.
    """

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path or "config/api_keys.json")
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file."""
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return self._default_config()

    def _default_config(self) -> Dict[str, Any]:
        """Return default configuration."""
        return {
            "version": "1.0.0",
            "models": {
                "openai": {
                    "gpt-4": {
                        "name": "GPT-4",
                        "provider": "openai",
                        "model_id": "gpt-4",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.openai.com/v1",
                        "temperature": 0.7,
                        "max_tokens": 2048
                    },
                    "gpt-4-turbo": {
                        "name": "GPT-4 Turbo",
                        "provider": "openai",
                        "model_id": "gpt-4-turbo-preview",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.openai.com/v1",
                        "temperature": 0.7,
                        "max_tokens": 4096
                    },
                    "gpt-3.5-turbo": {
                        "name": "GPT-3.5 Turbo",
                        "provider": "openai",
                        "model_id": "gpt-3.5-turbo",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.openai.com/v1",
                        "temperature": 0.7,
                        "max_tokens": 2048
                    }
                },
                "anthropic": {
                    "claude-3-opus": {
                        "name": "Claude 3 Opus",
                        "provider": "anthropic",
                        "model_id": "claude-3-opus-20240229",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.anthropic.com",
                        "temperature": 0.7,
                        "max_tokens": 4096
                    },
                    "claude-3-sonnet": {
                        "name": "Claude 3 Sonnet",
                        "provider": "anthropic",
                        "model_id": "claude-3-sonnet-20240229",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.anthropic.com",
                        "temperature": 0.7,
                        "max_tokens": 4096
                    },
                    "claude-3-haiku": {
                        "name": "Claude 3 Haiku",
                        "provider": "anthropic",
                        "model_id": "claude-3-haiku-20240307",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.anthropic.com",
                        "temperature": 0.7,
                        "max_tokens": 4096
                    }
                },
                "mistral": {
                    "mistral-large": {
                        "name": "Mistral Large",
                        "provider": "mistral",
                        "model_id": "mistral-large-latest",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.mistral.ai",
                        "temperature": 0.7,
                        "max_tokens": 2048
                    },
                    "mistral-medium": {
                        "name": "Mistral Medium",
                        "provider": "mistral",
                        "model_id": "mistral-medium-latest",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.mistral.ai",
                        "temperature": 0.7,
                        "max_tokens": 2048
                    }
                },
                "together": {
                    "llama-3-70b": {
                        "name": "Llama 3 70B",
                        "provider": "together",
                        "model_id": "meta-llama/Llama-3-70b-chat-hf",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.together.xyz",
                        "temperature": 0.7,
                        "max_tokens": 2048
                    },
                    "mixtral-8x7b": {
                        "name": "Mixtral 8x7B",
                        "provider": "together",
                        "model_id": "mistralai/Mixtral-8x7B-Instruct-v0.1",
                        "enabled": False,
                        "api_key": None,
                        "endpoint": "https://api.together.xyz",
                        "temperature": 0.7,
                        "max_tokens": 2048
                    }
                },
                "custom": {}
            },
            "test_settings": {
                "default_batch_size": 10,
                "max_concurrent_tests": 5,
                "test_timeout": 60,
                "save_conversations": True,
                "evaluate_responses": True
            },
            "memory": {
                "system_context": "",
                "custom_instructions": "",
                "enabled": False
            }
        }

    def save(self) -> None:
        """Save configuration to file."""
        with open(self.config_path, 'w') as f:
            json.dump(self._config, f, indent=2)

    def get_all_models(self) -> List[Dict[str, Any]]:
        """Get all configured models."""
        models = []
        for provider, provider_models in self._config.get("models", {}).items():
            for model_key, model_config in provider_models.items():
                models.append({
                    "key": f"{provider}/{model_key}",
                    **model_config
                })
        return models

    def get_enabled_models(self) -> List[Dict[str, Any]]:
        """Get only enabled models."""
        return [m for m in self.get_all_models() if m.get("enabled")]

    def update_api_key(self, provider: str, api_key: str) -> None:
        """Update API key for a provider."""
        if provider in self._config.get("models", {}):
            for model_key in self._config["models"][provider]:
                self._config["models"][provider][model_key]["api_key"] = api_key
        self.save()

    def update_model_config(
        self,
        provider: str,
        model_key: str,
        updates: Dict[str, Any]
    ) -> None:
        """Update configuration for a specific model."""
        if provider in self._config.get("models", {}):
            if model_key in self._config["models"][provider]:
                self._config["models"][provider][model_key].update(updates)
                self.save()

    def enable_model(self, provider: str, model_key: str) -> None:
        """Enable a model for testing."""
        self.update_model_config(provider, model_key, {"enabled": True})

    def disable_model(self, provider: str, model_key: str) -> None:
        """Disable a model."""
        self.update_model_config(provider, model_key, {"enabled": False})

    def add_custom_model(self, model_config: Dict[str, Any]) -> None:
        """Add a custom model endpoint."""
        model_key = model_config.get("model_id", "custom_model").replace("/", "_")
        self._config["models"]["custom"][model_key] = {
            "name": model_config.get("name", "Custom Model"),
            "provider": "custom",
            "model_id": model_config.get("model_id"),
            "enabled": True,
            "api_key": model_config.get("api_key"),
            "endpoint": model_config.get("endpoint"),
            "temperature": model_config.get("temperature", 0.7),
            "max_tokens": model_config.get("max_tokens", 2048)
        }
        self.save()

    def get_memory_context(self) -> Dict[str, Any]:
        """Get memory/context settings."""
        return self._config.get("memory", {})

    def update_memory_context(
        self,
        system_context: Optional[str] = None,
        custom_instructions: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> None:
        """Update memory/context settings."""
        if "memory" not in self._config:
            self._config["memory"] = {}

        if system_context is not None:
            self._config["memory"]["system_context"] = system_context
        if custom_instructions is not None:
            self._config["memory"]["custom_instructions"] = custom_instructions
        if enabled is not None:
            self._config["memory"]["enabled"] = enabled

        self.save()

    def get_test_settings(self) -> Dict[str, Any]:
        """Get test configuration settings."""
        return self._config.get("test_settings", {})

    def update_test_settings(self, settings: Dict[str, Any]) -> None:
        """Update test configuration settings."""
        if "test_settings" not in self._config:
            self._config["test_settings"] = {}
        self._config["test_settings"].update(settings)
        self.save()

    def export_config(self, include_keys: bool = False) -> Dict[str, Any]:
        """Export configuration (optionally without API keys)."""
        config = self._config.copy()
        if not include_keys:
            for provider in config.get("models", {}):
                for model in config["models"][provider]:
                    config["models"][provider][model]["api_key"] = None
        return config

    def import_config(self, config: Dict[str, Any], merge: bool = True) -> None:
        """Import configuration from dict."""
        if merge:
            # Deep merge
            for key, value in config.items():
                if key == "models" and isinstance(value, dict):
                    for provider, models in value.items():
                        if provider not in self._config["models"]:
                            self._config["models"][provider] = {}
                        self._config["models"][provider].update(models)
                else:
                    self._config[key] = value
        else:
            self._config = config
        self.save()
