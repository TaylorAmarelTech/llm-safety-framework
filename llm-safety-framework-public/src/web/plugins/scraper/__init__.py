"""
Document Intelligence Agent plugin — scraping, extraction, knowledge base.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="scraper",
    name="Document Agent",
    version="1.0.0",
    router=router,
    api_prefix="/scraper",
    api_tags=["Document Agent"],
    nav_items=[
        NavItem(
            id="doc-agent",
            label="Document Agent",
            icon="&#128196;",
            group="ANALYZE",
            workflow_stage="analyze",
            order=420,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
    data_subdir="scraper",
)
