"""
Prompt Injection Mutation plugin — browse, apply, and chain
adversarial mutators for testing LLM input/output safety.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="prompt_injection",
    name="Prompt Injection",
    version="1.0.0",
    router=router,
    api_prefix="/prompt-injection",
    api_tags=["Prompt Injection"],
    nav_items=[
        NavItem(
            id="mutator-library",
            label="Mutator Library",
            icon="&#9878;",
            group="TRANSFORM",
            workflow_stage="transform",
            order=310,
        ),
        NavItem(
            id="mutation-lab",
            label="Mutation Lab",
            icon="&#9874;",
            group="TRANSFORM",
            workflow_stage="transform",
            order=320,
        ),
        NavItem(
            id="pipeline-builder",
            label="Pipeline Builder",
            icon="&#9881;",
            group="TRANSFORM",
            workflow_stage="transform",
            order=330,
        ),
        NavItem(
            id="batch-results",
            label="Batch Results",
            icon="&#9634;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=690,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
