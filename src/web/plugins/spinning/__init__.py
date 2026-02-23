"""
Spinning / Transform Workbench plugin — spintax, regex, charpad, LLM rephrase,
attack augment, custom, encode, obfuscate, jailbreak, multilingual, chains, pipeline.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="transform",
    name="Transform Workbench",
    version="1.0.0",
    router=router,
    api_prefix="/spinning",
    api_tags=["Spinning"],
    nav_items=[
        NavItem(
            id="transform",
            label="Transform",
            icon="&#9881;",
            group="TRANSFORM",
            workflow_stage="transform",
            order=300,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
