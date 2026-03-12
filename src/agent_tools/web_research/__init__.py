"""
Web Research — structured web and API research tools for agents.

Provides tools to search academic papers, GitHub repos, and security
advisories without requiring agents to construct raw HTTP requests.
"""

from src.agent_tools.web_research.paper_searcher import PaperSearcher
from src.agent_tools.web_research.repo_scanner import RepoScanner
from src.agent_tools.web_research.advisory_tracker import AdvisoryTracker

__all__ = ["PaperSearcher", "RepoScanner", "AdvisoryTracker"]
