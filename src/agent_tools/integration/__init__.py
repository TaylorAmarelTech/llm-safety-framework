"""
Integration sub-package — evaluate and incorporate external libraries.
"""

from src.agent_tools.integration.repo_evaluator import RepoEvaluator, EvaluationReport
from src.agent_tools.integration.dependency_manager import DependencyManager, Dependency
from src.agent_tools.integration.adapter_factory import AdapterFactory

__all__ = [
    "RepoEvaluator",
    "EvaluationReport",
    "DependencyManager",
    "Dependency",
    "AdapterFactory",
]
