"""
Diff Engine — structured code diff generation for agents.

Provides tools to generate, preview, and apply code changes as
structured diffs rather than raw string replacements.
"""

from src.agent_tools.diff_engine.change_builder import ChangeBuilder
from src.agent_tools.diff_engine.file_patcher import FilePatcher
from src.agent_tools.diff_engine.diff_previewer import DiffPreviewer

__all__ = ["ChangeBuilder", "FilePatcher", "DiffPreviewer"]
