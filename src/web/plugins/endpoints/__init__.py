"""
API Endpoints plugin — endpoint CRUD, model management, model discovery.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="endpoints",
    name="API Endpoints",
    version="1.0.0",
    router=router,
    api_prefix="/endpoints",
    api_tags=["Endpoints"],
    nav_items=[
        NavItem(
            id="endpoints",
            label="Endpoints",
            icon="&#9881;",
            group="CONFIGURE",
            workflow_stage="configure",
            order=100,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
