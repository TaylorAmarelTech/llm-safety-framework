"""
Agent & Development Tool Testing plugin — test whether AI coding agents
and development tools will build software that facilitates exploitation.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="agent_testing",
    name="Agent & Tool Testing",
    version="1.0.0",
    router=router,
    api_prefix="/agent-testing",
    api_tags=["Agent Testing"],
    nav_items=[
        NavItem(
            id="agent-scenarios",
            label="Agent Scenarios",
            icon="&#9881;",
            group="DESIGN",
            workflow_stage="design",
            order=370,
        ),
        NavItem(
            id="agent-runner",
            label="Agent Runner",
            icon="&#9654;",
            group="TEST",
            workflow_stage="test",
            order=530,
        ),
        NavItem(
            id="agent-results",
            label="Agent Results",
            icon="&#9632;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=690,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
