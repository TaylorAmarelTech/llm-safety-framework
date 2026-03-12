"""
Research Agent Coordinator

Orchestrates independent research agents. Each agent runs autonomously
but the coordinator handles:
- Agent discovery and initialization
- Parallel execution (asyncio)
- Result aggregation and deduplication
- Merged reporting
- Persistence to data/research/

Can run all agents, a subset, or a single agent.
"""

from __future__ import annotations

import asyncio
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from src.research.agents import (
    BaseResearchAgent,
    Finding,
    GeneratedTest,
    ResearchReport,
    _AGENT_REGISTRY,
    list_agents,
)

# Import all agents to trigger registration
from src.research.agents.enforcement_agent import EnforcementAgent
from src.research.agents.cross_pollination_agent import CrossPollinationAgent
from src.research.agents.technique_evolution_agent import TechniqueEvolutionAgent
from src.research.agents.coverage_gap_agent import CoverageGapAgent
from src.research.agents.ethics_boundary_agent import EthicsBoundaryAgent
from src.research.agents.financial_crime_agent import FinancialCrimeAgent
from src.research.agents.jurisdiction_agent import JurisdictionAgent

logger = logging.getLogger(__name__)


class ResearchCoordinator:
    """
    Coordinates independent research agents.

    Usage:
        coordinator = ResearchCoordinator(
            data_dir="data/research",
            endpoint={"base_url": "...", "api_key": "...", ...},
            model_id="mistral-large-latest",
        )

        # Run all agents
        results = await coordinator.run_all()

        # Run specific agents
        results = await coordinator.run_agents(["enforcement", "financial_crime"])

        # Run single agent
        report = await coordinator.run_agent("coverage_gap")
    """

    def __init__(
        self,
        data_dir: str | Path = "data/research",
        endpoint: Optional[dict[str, Any]] = None,
        model_id: Optional[str] = None,
    ):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.endpoint = endpoint
        self.model_id = model_id
        self._agents: dict[str, BaseResearchAgent] = {}

    def _get_agent(self, name: str) -> BaseResearchAgent:
        """Get or create an agent instance."""
        if name not in self._agents:
            cls = _AGENT_REGISTRY.get(name)
            if cls is None:
                raise KeyError(f"Unknown agent: {name}. Available: {list(_AGENT_REGISTRY)}")
            self._agents[name] = cls(
                data_dir=self.data_dir,
                endpoint=self.endpoint,
                model_id=self.model_id,
            )
        return self._agents[name]

    async def run_agent(self, name: str, **kwargs) -> ResearchReport:
        """Run a single agent by name."""
        agent = self._get_agent(name)
        logger.info(f"Starting agent: {name} ({agent.DESCRIPTION})")

        try:
            report = await agent.run(**kwargs)
            logger.info(
                f"Agent {name} completed: {len(report.findings)} findings, "
                f"{len(report.generated_tests)} tests"
            )
            return report
        except Exception as e:
            logger.error(f"Agent {name} failed: {e}")
            return ResearchReport(
                agent_name=name,
                domain=agent.DOMAIN,
                findings=[],
                generated_tests=[],
                summary=f"Agent failed with error: {e}",
                error=str(e),
                completed_at=datetime.now(tz=timezone.utc).isoformat(),
            )

    async def run_agents(
        self,
        names: list[str],
        parallel: bool = False,
        **kwargs,
    ) -> list[ResearchReport]:
        """
        Run multiple agents.

        Args:
            names: Agent names to run.
            parallel: If True, run agents concurrently (watch rate limits).
            **kwargs: Passed to each agent's run().
        """
        if parallel:
            tasks = [self.run_agent(name, **kwargs) for name in names]
            return await asyncio.gather(*tasks)
        else:
            results = []
            for name in names:
                report = await self.run_agent(name, **kwargs)
                results.append(report)
            return results

    async def run_all(self, parallel: bool = False, **kwargs) -> list[ResearchReport]:
        """Run all registered agents."""
        names = list(_AGENT_REGISTRY.keys())
        logger.info(f"Running all {len(names)} agents: {names}")
        return await self.run_agents(names, parallel=parallel, **kwargs)

    def aggregate_reports(self, reports: list[ResearchReport]) -> dict[str, Any]:
        """
        Aggregate results from multiple agent runs into a unified summary.

        Returns a dict with combined findings, tests, and statistics.
        """
        all_findings: list[dict] = []
        all_tests: list[dict] = []
        agent_summaries = []
        total_llm_calls = 0
        total_duration = 0.0

        for report in reports:
            all_findings.extend(f.to_dict() for f in report.findings)
            all_tests.extend(t.to_dict() for t in report.generated_tests)
            total_llm_calls += report.llm_calls_made
            total_duration += report.run_duration_seconds
            agent_summaries.append({
                "agent": report.agent_name,
                "findings": len(report.findings),
                "tests": len(report.generated_tests),
                "duration_s": report.run_duration_seconds,
                "error": report.error,
            })

        # Deduplicate findings by title similarity
        seen_titles: set[str] = set()
        unique_findings = []
        for f in all_findings:
            title_key = f.get("title", "").lower().strip()
            if title_key not in seen_titles:
                seen_titles.add(title_key)
                unique_findings.append(f)

        # Deduplicate tests by prompt similarity (first 100 chars)
        seen_prompts: set[str] = set()
        unique_tests = []
        for t in all_tests:
            prompt_key = t.get("prompt", "")[:100].lower().strip()
            if prompt_key not in seen_prompts:
                seen_prompts.add(prompt_key)
                unique_tests.append(t)

        # Domain distribution
        domain_counts: dict[str, int] = {}
        for f in unique_findings:
            d = f.get("domain", "unknown")
            domain_counts[d] = domain_counts.get(d, 0) + 1

        return {
            "generated_at": datetime.now(tz=timezone.utc).isoformat(),
            "agent_count": len(reports),
            "agent_summaries": agent_summaries,
            "total_findings": len(unique_findings),
            "total_tests": len(unique_tests),
            "duplicates_removed": {
                "findings": len(all_findings) - len(unique_findings),
                "tests": len(all_tests) - len(unique_tests),
            },
            "domain_distribution": domain_counts,
            "total_llm_calls": total_llm_calls,
            "total_duration_seconds": total_duration,
            "findings": unique_findings,
            "generated_tests": unique_tests,
        }

    def save_aggregated(self, aggregated: dict[str, Any]) -> Path:
        """Save aggregated results to disk."""
        ts = datetime.now(tz=timezone.utc).strftime("%Y%m%d_%H%M%S")
        path = self.data_dir / f"aggregated_{ts}.json"
        path.write_text(json.dumps(aggregated, indent=2), encoding="utf-8")
        logger.info(f"Saved aggregated results to {path}")
        return path

    def status(self) -> dict[str, Any]:
        """Get status of all agents and their output."""
        agents_info = []
        for name, cls in _AGENT_REGISTRY.items():
            agent_dir = self.data_dir / name
            report_count = len(list(agent_dir.glob("report_*.json"))) if agent_dir.exists() else 0
            agents_info.append({
                "name": name,
                "description": cls.DESCRIPTION,
                "domain": cls.DOMAIN,
                "reports_on_disk": report_count,
            })

        return {
            "registered_agents": len(_AGENT_REGISTRY),
            "agents": agents_info,
            "data_dir": str(self.data_dir),
            "has_endpoint": self.endpoint is not None,
        }


# ---------------------------------------------------------------------------
# CLI runner
# ---------------------------------------------------------------------------

async def _run_cli(args: list[str] | None = None):
    """CLI entry point for running research agents."""
    import argparse

    parser = argparse.ArgumentParser(description="Research Agent Coordinator")
    parser.add_argument(
        "command",
        choices=["run", "run-all", "status", "list"],
        help="Command to execute",
    )
    parser.add_argument(
        "--agents",
        nargs="+",
        help="Agent names to run (for 'run' command)",
    )
    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Run agents in parallel",
    )
    parser.add_argument(
        "--data-dir",
        default="data/research",
        help="Data directory for results",
    )
    parser.add_argument(
        "--api-key",
        help="API key for LLM endpoint",
    )
    parser.add_argument(
        "--base-url",
        default="https://api.mistral.ai/v1",
        help="Base URL for LLM endpoint",
    )
    parser.add_argument(
        "--model",
        default="mistral-large-latest",
        help="Model ID to use",
    )

    parsed = parser.parse_args(args)

    # Build endpoint config
    import os
    api_key = parsed.api_key or os.getenv("MISTRAL_API_KEY") or os.getenv("OPENAI_API_KEY", "")
    endpoint = {
        "base_url": parsed.base_url,
        "api_key": api_key,
        "request_format": "openai",
        "auth_header": "Authorization",
        "auth_prefix": "Bearer",
        "default_model": parsed.model,
    }

    coordinator = ResearchCoordinator(
        data_dir=parsed.data_dir,
        endpoint=endpoint,
        model_id=parsed.model,
    )

    if parsed.command == "list":
        agents = list_agents()
        print(f"\nRegistered Research Agents ({len(agents)}):\n")
        for name, desc in agents.items():
            print(f"  {name:25s} {desc}")
        return

    if parsed.command == "status":
        status = coordinator.status()
        print(f"\nResearch Agent Status:")
        print(f"  Registered: {status['registered_agents']}")
        print(f"  Data dir:   {status['data_dir']}")
        print(f"  Endpoint:   {'configured' if status['has_endpoint'] else 'NOT configured'}")
        print()
        for a in status["agents"]:
            print(f"  {a['name']:25s} {a['reports_on_disk']} reports  {a['description']}")
        return

    if parsed.command == "run":
        if not parsed.agents:
            parser.error("--agents required for 'run' command")
        reports = await coordinator.run_agents(
            parsed.agents,
            parallel=parsed.parallel,
        )
    elif parsed.command == "run-all":
        reports = await coordinator.run_all(parallel=parsed.parallel)
    else:
        return

    # Aggregate and save
    aggregated = coordinator.aggregate_reports(reports)
    path = coordinator.save_aggregated(aggregated)

    print(f"\n{'=' * 60}")
    print(f"  Research Complete")
    print(f"{'=' * 60}")
    print(f"  Agents run:     {aggregated['agent_count']}")
    print(f"  Total findings: {aggregated['total_findings']}")
    print(f"  Total tests:    {aggregated['total_tests']}")
    print(f"  LLM calls:      {aggregated['total_llm_calls']}")
    print(f"  Duration:        {aggregated['total_duration_seconds']:.1f}s")
    print(f"  Saved to:        {path}")
    print()

    for summary in aggregated["agent_summaries"]:
        status_str = "OK" if not summary["error"] else f"ERROR: {summary['error'][:40]}"
        print(f"  {summary['agent']:25s} {summary['findings']:3d} findings  {summary['tests']:3d} tests  {status_str}")


def main():
    """Synchronous CLI entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )
    asyncio.run(_run_cli())


if __name__ == "__main__":
    main()
