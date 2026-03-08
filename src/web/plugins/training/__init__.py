"""
Training Data Pipeline plugin — export training data, generate
fine-tuning configs, and manage the red-team feedback loop.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="training",
    name="Training Pipeline",
    version="1.0.0",
    router=router,
    api_prefix="/training",
    api_tags=["Training"],
    nav_items=[
        NavItem(
            id="training-export",
            label="Export Training Data",
            icon="&#9000;",
            group="EXPORT",
            workflow_stage="export",
            order=810,
        ),
        NavItem(
            id="training-finetune",
            label="Fine-Tune Configs",
            icon="&#9881;",
            group="EXPORT",
            workflow_stage="export",
            order=820,
        ),
        NavItem(
            id="training-redteam",
            label="Red-Team Loop",
            icon="&#9888;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=830,
        ),
        NavItem(
            id="training-attacks",
            label="Academic Attacks",
            icon="&#9876;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=840,
        ),
        NavItem(
            id="training-cloud",
            label="Cloud Fine-Tune",
            icon="&#9729;",
            group="EXPORT",
            workflow_stage="export",
            order=850,
        ),
        NavItem(
            id="training-analysis",
            label="Token Analysis",
            icon="&#9783;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=860,
        ),
        NavItem(
            id="training-reward",
            label="Reward Modeling",
            icon="&#9733;",
            group="EXPORT",
            workflow_stage="export",
            order=870,
        ),
        NavItem(
            id="training-evaluate",
            label="Safety Evaluation",
            icon="&#9888;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=880,
        ),
        NavItem(
            id="training-generate",
            label="Dataset Generator",
            icon="&#9889;",
            group="EXPORT",
            workflow_stage="export",
            order=890,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
)
