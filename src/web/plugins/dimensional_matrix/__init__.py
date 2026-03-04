"""
Dimensional Matrix plugin — multi-dimensional severity scoring,
boundary probing, calibration, and multi-LLM debate evaluation.
"""

from pathlib import Path

from ...plugin_base import PluginManifest, NavItem
from .routes import router

manifest = PluginManifest(
    id="dimensional_matrix",
    name="Dimensional Matrix",
    version="1.0.0",
    router=router,
    api_prefix="/dimensional-matrix",
    api_tags=["Dimensional Matrix"],
    nav_items=[
        NavItem(
            id="dimension-explorer",
            label="Dimensions",
            icon="&#9733;",
            group="ANALYZE",
            workflow_stage="analyze",
            order=450,
        ),
        NavItem(
            id="dimensional-rater",
            label="Dim. Rater",
            icon="&#9878;",
            group="ANALYZE",
            workflow_stage="analyze",
            order=460,
        ),
        NavItem(
            id="boundary-prober",
            label="Boundary Prober",
            icon="&#9889;",
            group="TEST",
            workflow_stage="test",
            order=530,
        ),
        NavItem(
            id="debate-arena",
            label="Debate Arena",
            icon="&#9881;",
            group="EVALUATE",
            workflow_stage="evaluate",
            order=690,
        ),
    ],
    fragment_dir=Path(__file__).parent / "static",
    data_subdir="dimensional_matrix",
)
