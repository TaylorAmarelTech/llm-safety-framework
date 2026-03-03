"""
Run all research agents against Mistral API.

Usage:
    PYTHONPATH=. py -3.13 scripts/run_research_agents.py
    PYTHONPATH=. py -3.13 scripts/run_research_agents.py --agents enforcement financial_crime
    PYTHONPATH=. py -3.13 scripts/run_research_agents.py --agent coverage_gap
"""

import asyncio
import json
import logging
import sys
import os

# Force UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)
logger = logging.getLogger("research_runner")


def load_mistral_endpoint() -> dict:
    """Load Mistral endpoint config from api_keys.json."""
    cfg_path = os.path.join(os.path.dirname(__file__), "..", "config", "api_keys.json")
    cfg_path = os.path.abspath(cfg_path)

    with open(cfg_path, encoding="utf-8") as f:
        data = json.load(f)

    ep = data.get("endpoints", {}).get("mistral", {})
    if not ep.get("api_key"):
        raise ValueError("No Mistral API key found in config/api_keys.json")

    return {
        "base_url": ep.get("base_url", "https://api.mistral.ai/v1"),
        "api_key": ep["api_key"],
        "request_format": "openai",
        "auth_header": "Authorization",
        "auth_prefix": "Bearer",
        "default_model": "mistral-large-latest",
        "extra_headers": {},
    }


async def run_single_agent(coordinator, name: str):
    """Run a single agent with error handling."""
    try:
        logger.info(f"=== Starting agent: {name} ===")
        report = await coordinator.run_agent(name)
        logger.info(
            f"=== Agent {name} done: "
            f"{len(report.findings)} findings, "
            f"{len(report.generated_tests)} tests, "
            f"{report.run_duration_seconds:.1f}s ==="
        )
        return report
    except Exception as e:
        logger.error(f"=== Agent {name} FAILED: {e} ===")
        from src.research.agents import ResearchReport
        return ResearchReport(
            agent_name=name,
            domain="error",
            findings=[],
            generated_tests=[],
            summary=f"Failed: {e}",
            error=str(e),
        )


async def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", nargs="+", help="Specific agents to run")
    parser.add_argument("--agent", help="Single agent to run")
    parser.add_argument("--model", default="mistral-large-latest")
    args = parser.parse_args()

    endpoint = load_mistral_endpoint()
    logger.info(f"Using Mistral endpoint: {endpoint['base_url']}, model: {args.model}")

    from src.research.agents.coordinator import ResearchCoordinator
    coordinator = ResearchCoordinator(
        data_dir="data/research",
        endpoint=endpoint,
        model_id=args.model,
    )

    # Determine which agents to run
    if args.agent:
        agent_names = [args.agent]
    elif args.agents:
        agent_names = args.agents
    else:
        from src.research.agents import list_agents
        agent_names = list(list_agents().keys())

    print(f"\n{'=' * 70}")
    print(f"  Research Agent Runner - {len(agent_names)} agents")
    print(f"  Model: {args.model}")
    print(f"  Agents: {', '.join(agent_names)}")
    print(f"{'=' * 70}\n")

    # Run agents sequentially (to avoid rate limits)
    reports = []
    for name in agent_names:
        report = await run_single_agent(coordinator, name)
        reports.append(report)
        # Brief pause between agents
        if name != agent_names[-1]:
            logger.info("Pausing 2s between agents...")
            await asyncio.sleep(2)

    # Aggregate
    aggregated = coordinator.aggregate_reports(reports)
    path = coordinator.save_aggregated(aggregated)

    # Print summary
    print(f"\n{'=' * 70}")
    print(f"  RESEARCH COMPLETE")
    print(f"{'=' * 70}")
    print(f"  Agents run:        {aggregated['agent_count']}")
    print(f"  Total findings:    {aggregated['total_findings']}")
    print(f"  Total tests:       {aggregated['total_tests']}")
    print(f"  LLM calls:         {aggregated['total_llm_calls']}")
    print(f"  Total duration:    {aggregated['total_duration_seconds']:.1f}s")
    print(f"  Dedup removed:     {aggregated['duplicates_removed']}")
    print(f"  Domain breakdown:  {aggregated['domain_distribution']}")
    print(f"  Saved to:          {path}")
    print()

    for s in aggregated["agent_summaries"]:
        status = "OK" if not s["error"] else f"ERR: {s['error'][:50]}"
        print(f"  {s['agent']:25s} {s['findings']:3d} findings  {s['tests']:3d} tests  {s['duration_s']:6.1f}s  {status}")

    print()

    # Print a few sample findings
    print("  --- Sample Findings ---")
    for f in aggregated["findings"][:5]:
        title = f.get("title", "?")[:60]
        domain = f.get("domain", "?")
        print(f"  [{domain:20s}] {title}")

    print()
    print("  --- Sample Generated Tests ---")
    for t in aggregated["generated_tests"][:5]:
        prompt_preview = t.get("prompt", "?")[:80].replace("\n", " ")
        domain = t.get("domain", "?")
        print(f"  [{domain:20s}] {prompt_preview}...")

    return aggregated


if __name__ == "__main__":
    asyncio.run(main())
