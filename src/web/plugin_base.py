"""
Plugin base classes for the LLM Safety Framework.

Each plugin provides a PluginManifest describing its routes,
frontend fragments, nav items, and data directories.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from fastapi import APIRouter


@dataclass
class NavItem:
    """One sidebar navigation entry."""
    id: str                                # section ID, e.g. "endpoints"
    label: str                             # sidebar label
    icon: str                              # unicode char
    group: Optional[str] = None            # nav group label, e.g. "CONFIGURE"
    workflow_stage: Optional[str] = None   # configure/design/transform/analyze/test/evaluate
    order: int = 100                       # sort order within group


@dataclass
class PluginManifest:
    """Everything the shell needs to mount a plugin."""
    id: str                                # unique slug, e.g. "endpoints"
    name: str                              # human name, e.g. "API Endpoints"
    version: str = "1.0.0"

    # Backend
    router: Optional[APIRouter] = None
    api_prefix: str = ""                   # e.g. "/endpoints" (mounted under /api)
    api_tags: list[str] = field(default_factory=list)

    # Frontend
    nav_items: list[NavItem] = field(default_factory=list)
    fragment_dir: Optional[Path] = None    # directory containing fragment.html, fragment.js

    # Data
    data_subdir: Optional[str] = None      # e.g. "scraper" -> data/scraper/

    # Lifecycle
    enabled: bool = True
