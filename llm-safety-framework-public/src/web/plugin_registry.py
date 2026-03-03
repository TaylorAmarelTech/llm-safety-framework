"""
Plugin registry — discovers, loads, and manages plugins.

Scans src/web/plugins/ for packages that export a `manifest` attribute
of type PluginManifest. Mounts their routers and serves their fragments.
"""

from __future__ import annotations

import importlib
import json
import logging
from pathlib import Path
from typing import Optional

from fastapi import APIRouter

from .plugin_base import PluginManifest

logger = logging.getLogger(__name__)


class PluginRegistry:
    """Discovers, registers, and mounts plugins."""

    def __init__(self, disabled: Optional[set[str]] = None):
        self._plugins: dict[str, PluginManifest] = {}
        self._disabled = disabled or set()

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------

    def discover(self, plugins_dir: Path) -> None:
        """Scan plugins_dir for packages exporting a `manifest`."""
        if not plugins_dir.is_dir():
            logger.info("Plugins directory %s not found — skipping discovery", plugins_dir)
            return

        for child in sorted(plugins_dir.iterdir()):
            if not child.is_dir() or not (child / "__init__.py").exists():
                continue
            plugin_id = child.name
            if plugin_id.startswith("_"):
                continue
            if plugin_id in self._disabled:
                logger.info("Plugin %s is disabled — skipping", plugin_id)
                continue
            try:
                module = importlib.import_module(f"src.web.plugins.{plugin_id}")
                manifest: PluginManifest = getattr(module, "manifest", None)
                if manifest is None:
                    logger.warning("Plugin %s has no manifest — skipping", plugin_id)
                    continue
                self.register(manifest)
                logger.info("Discovered plugin: %s v%s", manifest.id, manifest.version)
            except Exception:
                logger.exception("Failed to load plugin %s", plugin_id)

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(self, manifest: PluginManifest) -> None:
        """Register a plugin manifest."""
        self._plugins[manifest.id] = manifest

    # ------------------------------------------------------------------
    # Mounting
    # ------------------------------------------------------------------

    def mount_all(self, api_router: APIRouter) -> None:
        """Mount all plugin routers onto the api_router."""
        for manifest in self._plugins.values():
            if manifest.router and manifest.api_prefix:
                api_router.include_router(
                    manifest.router,
                    prefix=manifest.api_prefix,
                    tags=manifest.api_tags or [manifest.name],
                )
                logger.info(
                    "Mounted plugin %s at /api%s",
                    manifest.id,
                    manifest.api_prefix,
                )

    # ------------------------------------------------------------------
    # Query
    # ------------------------------------------------------------------

    def get_all(self) -> list[PluginManifest]:
        """Return all registered (enabled) plugins."""
        return list(self._plugins.values())

    def get(self, plugin_id: str) -> Optional[PluginManifest]:
        """Get a single plugin by ID."""
        return self._plugins.get(plugin_id)

    def get_nav_manifest(self) -> list[dict]:
        """Return JSON-serializable nav structure for the frontend shell."""
        nav = []
        for manifest in self._plugins.values():
            for item in manifest.nav_items:
                nav.append({
                    "plugin_id": manifest.id,
                    "section_id": item.id,
                    "label": item.label,
                    "icon": item.icon,
                    "group": item.group,
                    "workflow_stage": item.workflow_stage,
                    "order": item.order,
                })
        nav.sort(key=lambda x: x.get("order", 100))
        return nav

    def get_section_plugin_map(self) -> dict[str, str]:
        """Return {section_id: plugin_id} mapping for the frontend."""
        mapping = {}
        for manifest in self._plugins.values():
            for item in manifest.nav_items:
                mapping[item.id] = manifest.id
        return mapping

    # ------------------------------------------------------------------
    # Config
    # ------------------------------------------------------------------

    @staticmethod
    def load_disabled(config_path: Path) -> set[str]:
        """Load disabled plugin list from config/plugins.json."""
        if config_path.exists():
            try:
                data = json.loads(config_path.read_text())
                return set(data.get("disabled", []))
            except Exception:
                logger.warning("Could not read %s", config_path)
        return set()
