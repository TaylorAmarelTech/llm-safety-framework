"""
LLM Cartography web plugin — interactive safety topology mapping.

Provides a tabbed UI and 26 API routes for gradient exploration,
response scoring, topology computation, comparative matrix analysis,
attack surface measurement, and blind spot detection.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="cartography",
    name="LLM Cartography",
    version="1.0.0",
    router=router,
    api_prefix="/cartography",
    api_tags=["Cartography"],
    nav_items=[
        NavItem(
            id="gradient-explorer",
            label="Gradient Explorer",
            icon="&#8711;",
            group="DESIGN",
            workflow_stage="design",
            order=380,
        ),
        NavItem(
            id="topology-map",
            label="Topology Map",
            icon="&#9651;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=700,
        ),
        NavItem(
            id="comparative-matrix",
            label="Comparative Matrix",
            icon="&#9632;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=710,
        ),
        NavItem(
            id="attack-surface",
            label="Attack Surface",
            icon="&#9888;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=720,
        ),
        NavItem(
            id="blind-spots",
            label="Blind Spots",
            icon="&#9711;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=730,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
