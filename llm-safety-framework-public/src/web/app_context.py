"""
Shared application context for plugins.

Provides dependency-injected access to ConfigManager, Settings,
and data directories instead of per-route module-level instantiation.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from fastapi import Request

from .config import Settings, ConfigManager


@dataclass
class AppContext:
    """Shared services available to all plugins."""
    settings: Settings
    config_manager: ConfigManager
    data_dir: Path

    def plugin_data_dir(self, plugin_id: str) -> Path:
        """Return data/{plugin_id}/, creating if needed."""
        d = self.data_dir / plugin_id
        d.mkdir(parents=True, exist_ok=True)
        return d


def get_ctx(request: Request) -> AppContext:
    """FastAPI dependency that returns the shared AppContext."""
    return request.app.state.ctx
