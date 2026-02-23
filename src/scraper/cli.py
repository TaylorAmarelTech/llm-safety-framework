"""
CLI entry point for the Document Intelligence Agent.

Usage:
    py -3.13 -m src.scraper.cli scrape              # Scrape all enabled sources
    py -3.13 -m src.scraper.cli scrape --source dmw  # Specific source
    py -3.13 -m src.scraper.cli scrape --no-extract  # Download only
    py -3.13 -m src.scraper.cli scrape --force       # Ignore change detection
    py -3.13 -m src.scraper.cli scrape --browser     # Force Playwright rendering
    py -3.13 -m src.scraper.cli scrape --no-robots   # Ignore robots.txt
    py -3.13 -m src.scraper.cli status               # KB stats + last scrape
    py -3.13 -m src.scraper.cli status --stale-days 90   # Show stale facts
    py -3.13 -m src.scraper.cli list-sources         # Show configured sources
    py -3.13 -m src.scraper.cli rebuild-kb           # Rebuild KB from extractions
    py -3.13 -m src.scraper.cli browser-status       # Check Playwright availability
    py -3.13 -m src.scraper.cli check-feeds          # Test RSS/Atom feed URLs
"""

import argparse
import asyncio
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Document Intelligence Agent — scraper & knowledge base CLI"
    )
    sub = parser.add_subparsers(dest="command", help="Command to run")

    # scrape
    p_scrape = sub.add_parser("scrape", help="Scrape sources for new documents")
    p_scrape.add_argument("--source", type=str, default=None, help="Source ID (default: all enabled)")
    p_scrape.add_argument("--no-extract", action="store_true", help="Skip LLM extraction")
    p_scrape.add_argument("--force", action="store_true", help="Ignore change detection, re-fetch everything")
    p_scrape.add_argument("--browser", action="store_true", help="Force Playwright rendering for all sources")
    p_scrape.add_argument("--no-robots", action="store_true", help="Ignore robots.txt restrictions")
    p_scrape.add_argument("--data-dir", type=str, default="data/scraper", help="Data directory")

    # status
    p_status = sub.add_parser("status", help="Show knowledge base stats")
    p_status.add_argument("--stale-days", type=int, default=0, help="Show facts not confirmed in N days")
    p_status.add_argument("--data-dir", type=str, default="data/scraper", help="Data directory")

    # list-sources
    p_list = sub.add_parser("list-sources", help="List configured sources")
    p_list.add_argument("--tier", type=int, default=None, help="Filter by tier")
    p_list.add_argument("--data-dir", type=str, default="data/scraper", help="Data directory")

    # rebuild-kb
    p_rebuild = sub.add_parser("rebuild-kb", help="Rebuild knowledge base from extractions")
    p_rebuild.add_argument("--data-dir", type=str, default="data/scraper", help="Data directory")

    # browser-status
    p_browser = sub.add_parser("browser-status", help="Check Playwright browser availability")

    # check-feeds
    p_feeds = sub.add_parser("check-feeds", help="Test RSS/Atom feed URLs from sources")
    p_feeds.add_argument("--data-dir", type=str, default="data/scraper", help="Data directory")

    # seed-kb
    p_seed = sub.add_parser("seed-kb", help="Load seed facts into knowledge base")
    p_seed.add_argument("--data-dir", type=str, default="data/scraper", help="Data directory")

    args = parser.parse_args()

    if args.command == "scrape":
        asyncio.run(_cmd_scrape(args))
    elif args.command == "status":
        _cmd_status(args)
    elif args.command == "list-sources":
        _cmd_list_sources(args)
    elif args.command == "rebuild-kb":
        _cmd_rebuild(args)
    elif args.command == "browser-status":
        _cmd_browser_status()
    elif args.command == "check-feeds":
        asyncio.run(_cmd_check_feeds(args))
    elif args.command == "seed-kb":
        _cmd_seed_kb(args)
    else:
        parser.print_help()
        sys.exit(1)


async def _cmd_scrape(args) -> None:
    from .scheduler import ScrapeOrchestrator

    respect_robots = not getattr(args, "no_robots", False)
    orch = ScrapeOrchestrator(data_dir=args.data_dir, respect_robots=respect_robots)
    source_ids = [args.source] if args.source else None
    extract = not args.no_extract

    if extract:
        print("NOTE: LLM extraction requires an API client. Running in fetch-only mode.")
        print("      Use the dashboard to run extraction with a configured endpoint.\n")
        extract = False

    flags = []
    if args.force:
        flags.append("force-refetch")
    if args.browser:
        flags.append("browser-mode")
    if not respect_robots:
        flags.append("robots.txt-ignored")
    if flags:
        print(f"Flags: {', '.join(flags)}")

    print("Starting scrape...")
    job = await orch.run(
        source_ids=source_ids,
        extract=extract,
        force_refetch=args.force,
        use_browser=args.browser,
    )

    print(f"\nJob: {job.get('id')}")
    print(f"Status: {job.get('status')}")
    print(f"Sources done: {job.get('sources_done')}/{job.get('sources_total')}")
    print(f"Docs found: {job.get('docs_found')}")
    print(f"Docs new: {job.get('docs_new')}")
    print(f"Docs failed: {job.get('docs_failed')}")
    print(f"Unchanged/skipped: {job.get('unchanged_skipped', 0)}")
    print(f"Robots blocked: {job.get('robots_blocked', 0)}")
    print(f"Retries: {job.get('retry_count', 0)}")
    print(f"Browser rendered: {job.get('browser_rendered', 0)}")
    print(f"Facts extracted: {job.get('facts_extracted')}")
    if job.get("errors"):
        print(f"Errors ({len(job['errors'])}):")
        for e in job["errors"][:10]:
            print(f"  - {e}")


def _cmd_status(args) -> None:
    from .knowledge_base import KnowledgeBase
    from .fetcher import DocumentFetcher
    from .change_detection import ChangeDetector

    kb = KnowledgeBase(data_dir=args.data_dir)
    fetcher = DocumentFetcher(data_dir=args.data_dir)
    cd = ChangeDetector(data_dir=args.data_dir)

    stats = kb.stats()
    doc_count = fetcher.count_documents()
    cd_stats = cd.stats()

    print("=== Knowledge Base Status ===")
    print(f"Total facts:      {stats['total_facts']}")
    print(f"Total documents:  {doc_count}")
    print(f"Avg confidence:   {stats.get('avg_confidence', 0.0):.3f}")
    print(f"Last rebuilt:     {stats.get('last_rebuilt', 'never')}")
    print(f"Fingerprints:     {cd_stats['total_fingerprints']} (etag: {cd_stats['with_etag']}, last-mod: {cd_stats['with_last_modified']})")
    print()
    print("Facts by category:")
    for cat, count in sorted(stats.get("by_category", {}).items()):
        print(f"  {cat:25s} {count:5d}")
    if stats.get("jurisdictions"):
        print(f"\nJurisdictions: {', '.join(stats['jurisdictions'])}")
    if stats.get("corridors"):
        print(f"Corridors:     {', '.join(stats['corridors'])}")

    if args.stale_days > 0:
        stale = kb.get_stale_facts(days=args.stale_days)
        print(f"\nStale facts (>{args.stale_days} days): {len(stale)}")
        for f in stale[:10]:
            print(f"  - [{f.get('type')}] {f.get('_source_doc', '?')} last confirmed: {f.get('_last_confirmed', '?')}")


def _cmd_list_sources(args) -> None:
    from .sources import SourceRegistry, TIER_LABELS

    reg = SourceRegistry(data_dir=args.data_dir)
    sources = reg.list_sources(tier=args.tier)

    print(f"{'ID':25s} {'Tier':4s} {'Enabled':7s} {'JS':3s} {'RSS':3s} {'Docs':5s} {'Last Checked':20s} Name")
    print("-" * 100)
    for s in sources:
        enabled = "YES" if s.enabled else "no"
        checked = s.last_checked[:19] if s.last_checked else "never"
        js = "JS" if s.requires_js else ""
        rss = "RSS" if s.feed_url else ""
        print(f"{s.id:25s} T{s.tier:<3d} {enabled:7s} {js:3s} {rss:3s} {s.doc_count:5d} {checked:20s} {s.name}")

    # Summary by tier
    tier_counts: dict = {}
    for s in sources:
        tier_counts[s.tier] = tier_counts.get(s.tier, 0) + 1
    print(f"\nTotal: {len(sources)} sources")
    for t in sorted(tier_counts):
        label = TIER_LABELS.get(t, f"Tier {t}")
        print(f"  Tier {t} ({label}): {tier_counts[t]}")


def _cmd_rebuild(args) -> None:
    from .knowledge_base import KnowledgeBase

    kb = KnowledgeBase(data_dir=args.data_dir)
    counts = kb.rebuild()

    print("Knowledge base rebuilt.")
    print(f"Total facts: {sum(counts.values())}")
    for cat, count in sorted(counts.items()):
        print(f"  {cat:25s} {count:5d}")


def _cmd_browser_status() -> None:
    from .browser import HeadlessBrowser

    print("=== Playwright Browser Status ===")
    if HeadlessBrowser.is_available():
        print("Playwright: INSTALLED")
        print("To launch: headless Chromium starts on first JS-render request")
    else:
        print("Playwright: NOT INSTALLED")
        print("Install with:")
        print("  pip install playwright")
        print("  playwright install chromium")


async def _cmd_check_feeds(args) -> None:
    from .sources import SourceRegistry
    from .feed_parser import FeedParser

    reg = SourceRegistry(data_dir=args.data_dir)
    parser = FeedParser()

    sources_with_feeds = [s for s in reg.list_sources() if s.feed_url]
    if not sources_with_feeds:
        print("No sources have RSS/Atom feed URLs configured.")
        return

    print(f"Checking {len(sources_with_feeds)} feeds...\n")
    for s in sources_with_feeds:
        entries = await parser.fetch_and_parse_feed(s.feed_url)
        status = f"{len(entries)} entries" if entries else "FAILED"
        print(f"  {s.name:30s} {status:15s} {s.feed_url}")


def _cmd_seed_kb(args) -> None:
    from .knowledge_base import KnowledgeBase
    from .seed_loader import load_seeds, is_seeded

    kb = KnowledgeBase(data_dir=args.data_dir)
    already = is_seeded(kb)
    added = load_seeds(kb)

    if already and added == 0:
        print("KB already contains all seed facts.")
    else:
        print(f"Loaded {added} seed facts into KB.")
    print(f"Total KB facts: {len(kb._facts)}")


if __name__ == "__main__":
    main()
