"""
Library Integrations plugin — garak, PyRIT, deepteam.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="integrations",
    name="Library Integrations",
    version="1.0.0",
    router=router,
    api_prefix="/integrations",
    api_tags=["Integrations"],
    nav_items=[
        NavItem(
            id="integrations",
            label="Integrations",
            icon="&#9879;",
            group="TRANSFORM",
            workflow_stage="transform",
            order=350,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
