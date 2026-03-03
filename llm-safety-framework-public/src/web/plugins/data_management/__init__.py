"""
Data Management plugin — import/export for prompts, conversations, config, results.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="data_management",
    name="Data Management",
    version="1.0.0",
    router=router,
    api_prefix="/data",
    api_tags=["Data Management"],
    nav_items=[
        NavItem(
            id="data-mgmt",
            label="Data Management",
            icon="&#8693;",
            group="SYSTEM",
            workflow_stage=None,
            order=900,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
