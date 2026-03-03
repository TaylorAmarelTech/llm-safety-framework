"""
Intelligent Attack plugin — feature space analysis, embeddings, gap finding, probe suggestions.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="intelligent-attack",
    name="Intelligent Attack",
    version="1.0.0",
    router=router,
    api_prefix="/intelligent-attack",
    api_tags=["Intelligent Attack"],
    nav_items=[
        NavItem(
            id="intelligent-attack",
            label="Intelligent Attack",
            icon="&#9889;",
            group="TRANSFORM",
            workflow_stage="transform",
            order=360,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
