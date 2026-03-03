"""
Multi-Turn Conversation Attacks plugin.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="multi_turn",
    name="Multi-Turn Attacks",
    version="1.0.0",
    router=router,
    api_prefix="/multi-turn",
    api_tags=["Multi-Turn Attacks"],
    nav_items=[
        NavItem(
            id="multi-turn",
            label="Multi-Turn",
            icon="&#8644;",
            group="TRANSFORM",
            workflow_stage="transform",
            order=340,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
