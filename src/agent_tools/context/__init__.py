"""
Context sub-package — project map, coding conventions, and improvement history.

Provides structured information about the project so agents can orient
themselves without reading hundreds of files.
"""

from src.agent_tools.context.project_map import ProjectMap
from src.agent_tools.context.conventions import CONVENTIONS, ConventionGuide
from src.agent_tools.context.improvement_log import ImprovementLog

__all__ = ["ProjectMap", "CONVENTIONS", "ConventionGuide", "ImprovementLog"]
