"""
Prompts plugin — prompt sets, import, preparation, CRUD, and template library.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="prompts",
    name="Prompts",
    version="1.0.0",
    router=router,
    api_prefix="/prompts",
    api_tags=["Prompts"],
    nav_items=[
        NavItem(
            id="prompt-sets",
            label="Prompt Sets",
            icon="&#128196;",
            group="DESIGN",
            workflow_stage="design",
            order=200,
        ),
        NavItem(
            id="prompt-prep",
            label="Preparation",
            icon="&#9881;",
            group="DESIGN",
            workflow_stage="design",
            order=210,
        ),
        NavItem(
            id="template-library",
            label="Template Library",
            icon="&#128218;",
            group="DESIGN",
            workflow_stage="design",
            order=220,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
