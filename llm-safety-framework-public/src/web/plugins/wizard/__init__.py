"""
Wizard plugin — streamlined test generation wizard.

Provides a guided flow: describe domain -> generate prompts + graded
responses -> configure target model -> run tests -> see results.

This plugin is a "mode" rather than a section: it occupies the full
viewport when the user clicks the "Streamlined" button in the mode bar.
The shell lazy-loads the wizard fragment into the wizard-container div.
"""

from pathlib import Path

from ...plugin_base import PluginManifest
from .routes import router

manifest = PluginManifest(
    id="wizard",
    name="Wizard",
    version="1.0.0",
    router=router,
    api_prefix="/wizard",
    api_tags=["Wizard"],
    nav_items=[],                       # no sidebar nav — it's a mode
    fragment_dir=Path(__file__).parent / "static",
)
