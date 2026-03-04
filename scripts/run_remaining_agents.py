"""
Run remaining research agents (skip enforcement, limit cross_pollination).

Usage:
    PYTHONPATH=. py -3.13 scripts/run_remaining_agents.py
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


async def run_single_agent(coordinator, name: str, **kwargs):
    """Run a single agent with error handling."""
    try:
        logger.info(f"=== Starting agent: {name} ===")
        report = await coordinator.run_agent(name, **kwargs)
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
    endpoint = load_mistral_endpoint()
    logger.info(f"Using Mistral endpoint: {endpoint['base_url']}")

    from src.research.agents.coordinator import ResearchCoordinator
    coordinator = ResearchCoordinator(
        data_dir="data/research",
        endpoint=endpoint,
        model_id="mistral-large-latest",
    )

    # Agents to run (skip enforcement - already completed)
    agents_to_run = [
        # Cross-pollination with limited techniques (3 instead of 8 = 36 calls vs 96)
        ("cross_pollination", {
            "techniques": ["shell_company_layering", "jurisdictional_arbitrage", "crypto_obfuscation"]
        }),
        ("technique_evolution", {}),
        ("coverage_gap", {}),
        ("ethics_boundary", {}),
        ("financial_crime", {}),
        ("jurisdiction", {}),
    ]

    print(f"\n{'=' * 70}")
    print(f"  Research Agent Runner - {len(agents_to_run)} agents (enforcement already done)")
    print(f"  Model: mistral-large-latest")
    print(f"  Agents: {', '.join(a[0] for a in agents_to_run)}")
    print(f"{'=' * 70}\n")

    reports = []
    for name, kwargs in agents_to_run:
        report = await run_single_agent(coordinator, name, **kwargs)
        reports.append(report)
        print(f"\n  >> {name}: {len(report.findings)} findings, {len(report.generated_tests)} tests")
        # Brief pause between agents
        if name != agents_to_run[-1][0]:
            logger.info("Pausing 2s between agents...")
            await asyncio.sleep(2)

    # Load previous enforcement report for aggregation
    import glob
    enf_files = sorted(glob.glob("data/research/enforcement/report_*.json"))
    if enf_files:
        logger.info(f"Loading previous enforcement report: {enf_files[-1]}")
        with open(enf_files[-1], encoding="utf-8") as f:
            enf_data = json.load(f)
        from src.research.agents import Finding, GeneratedTest, ResearchReport as RR
        enf_report = RR(
            agent_name="enforcement",
            domain="cross_domain",
            findings=[Finding(**f) for f in enf_data.get("findings", [])],
            generated_tests=[GeneratedTest(**t) for t in enf_data.get("generated_tests", [])],
            summary=enf_data.get("summary", ""),
            run_duration_seconds=enf_data.get("run_duration_seconds", 0),
            llm_calls_made=enf_data.get("llm_calls_made", 0),
        )
        reports.insert(0, enf_report)

    # Aggregate
    aggregated = coordinator.aggregate_reports(reports)
    path = coordinator.save_aggregated(aggregated)

    # Print summary
    print(f"\n{'=' * 70}")
    print(f"  ALL RESEARCH COMPLETE")
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
    print("  --- Sample Findings ---")
    for f in aggregated["findings"][:8]:
        title = f.get("title", "?")[:65]
        domain = f.get("domain", "?")
        print(f"  [{domain:22s}] {title}")

    print()
    print("  --- Sample Generated Tests ---")
    for t in aggregated["generated_tests"][:8]:
        prompt_preview = t.get("prompt", "?")[:80].replace("\n", " ")
        domain = t.get("domain", "?")
        print(f"  [{domain:22s}] {prompt_preview}...")

    return aggregated


if __name__ == "__main__":
    asyncio.run(main())
