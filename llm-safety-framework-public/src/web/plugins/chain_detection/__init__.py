"""
Chain Detection plugin — tests LLM ability to detect trafficking
in sequences of individually-legal activities.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="chain_detection",
    name="Chain Detection",
    version="1.0.0",
    router=router,
    api_prefix="/chain-detection",
    api_tags=["Chain Detection"],
    nav_items=[
        NavItem(
            id="chain-library",
            label="Chain Library",
            icon="&#9734;",
            group="DESIGN",
            workflow_stage="design",
            order=350,
        ),
        NavItem(
            id="chain-runner",
            label="Chain Runner",
            icon="&#9654;",
            group="TEST",
            workflow_stage="test",
            order=520,
        ),
        NavItem(
            id="chain-results",
            label="Chain Results",
            icon="&#9632;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=680,
        ),
        NavItem(
            id="chain-builder",
            label="Chain Builder",
            icon="&#9998;",
            group="DESIGN",
            workflow_stage="design",
            order=360,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
