"""
LLM Safety Framework - Research Module

Provides research agent capabilities for discovering new test scenarios
and feeding information into the testing system.
"""

from src.research.research_agent import ResearchAgent, ResearchTask, ResearchResult
from src.research.news_monitor import NewsMonitor

__all__ = [
    "ResearchAgent",
    "ResearchTask",
    "ResearchResult",
    "NewsMonitor",
]
