"""
Research Hub plugin — search academic papers, GitHub repos,
datasets, and models for LLM safety research.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="research",
    name="Research Hub",
    version="1.0.0",
    router=router,
    api_prefix="/research",
    api_tags=["Research"],
    nav_items=[
        NavItem(
            id="research-search",
            label="Search",
            icon="&#128270;",
            group="ANALYZE",
            workflow_stage="analyze",
            order=710,
        ),
        NavItem(
            id="research-saved",
            label="Saved Results",
            icon="&#128278;",
            group="ANALYZE",
            workflow_stage="analyze",
            order=720,
        ),
        NavItem(
            id="research-status",
            label="API Status",
            icon="&#9889;",
            group="ANALYZE",
            workflow_stage="analyze",
            order=730,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
