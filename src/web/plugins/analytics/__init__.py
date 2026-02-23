"""
Analytics plugin — dashboard, testing, analytics charts, conversations,
model comparison, coverage matrix, deep-dive viewer, heatmap, exports.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="analytics",
    name="Analytics & Testing",
    version="1.0.0",
    router=router,
    api_prefix="/analytics",
    api_tags=["Analytics"],
    nav_items=[
        NavItem(
            id="dashboard",
            label="Dashboard",
            icon="&#9632;",
            group="OVERVIEW",
            workflow_stage="overview",
            order=100,
        ),
        NavItem(
            id="testing",
            label="Testing",
            icon="&#9654;",
            group="TEST",
            workflow_stage="test",
            order=500,
        ),
        NavItem(
            id="analytics",
            label="Analytics",
            icon="&#9636;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=600,
        ),
        NavItem(
            id="conversations",
            label="Conversations",
            icon="&#128172;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=650,
        ),
        NavItem(
            id="model-comparison",
            label="Compare",
            icon="&#8646;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=700,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
