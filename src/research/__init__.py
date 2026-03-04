"""
LLM Safety Framework - Research Module

Provides:
1. Legacy ResearchAgent and NewsMonitor (original single-agent system)
2. Independent specialized research agents (7 agents, each domain-focused)
3. ResearchCoordinator for orchestrating agent runs

Research Agents:
    enforcement        - SEC/DOJ/FinCEN/FATF/IRS enforcement actions
    cross_pollination  - Cross-domain pattern transfer
    technique_evolution - Emerging techniques (AI, DeFi, prompt injection)
    coverage_gap       - Test suite gap analysis and filling
    ethics_boundary    - Dual-use, usury, gray areas, whistleblower suppression
    financial_crime    - Tax evasion, AML, white collar deep-dive
    jurisdiction       - Jurisdiction-specific regulations and loopholes

Usage:
    from src.research.agents.coordinator import ResearchCoordinator

    coordinator = ResearchCoordinator(
        endpoint={"base_url": "...", "api_key": "..."},
        model_id="mistral-large-latest",
    )
    reports = await coordinator.run_all()
"""

from src.research.research_agent import ResearchAgent, ResearchTask, ResearchResult
from src.research.news_monitor import NewsMonitor

# Import agent system
from src.research.agents import (
    BaseResearchAgent,
    Finding,
    GeneratedTest,
    ResearchReport,
    Domain,
    Severity,
    list_agents,
    get_agent,
    register_agent,
)
from src.research.agents.coordinator import ResearchCoordinator

__all__ = [
    # Legacy
    "ResearchAgent",
    "ResearchTask",
    "ResearchResult",
    "NewsMonitor",
    # Agent system
    "BaseResearchAgent",
    "Finding",
    "GeneratedTest",
    "ResearchReport",
    "Domain",
    "Severity",
    "ResearchCoordinator",
    "list_agents",
    "get_agent",
    "register_agent",
]
