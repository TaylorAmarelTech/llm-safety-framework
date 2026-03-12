"""
Research sub-package — technique discovery, gap analysis, and reference indexing.
"""

from src.agent_tools.research.gap_analyzer import GapAnalyzer
from src.agent_tools.research.technique_catalog import TechniqueCatalog, TechniqueEntry
from src.agent_tools.research.github_scanner import GitHubScanner, RepoCandidate
from src.agent_tools.research.reference_index import ReferenceIndex, Reference

__all__ = [
    "GapAnalyzer",
    "TechniqueCatalog",
    "TechniqueEntry",
    "GitHubScanner",
    "RepoCandidate",
    "ReferenceIndex",
    "Reference",
]
