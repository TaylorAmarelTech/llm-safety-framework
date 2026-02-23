"""
Scrape orchestrator for the Document Intelligence Agent.

Coordinates the full workflow: fetch pages → discover links → download docs
→ extract facts → merge into knowledge base.

Integrates with PolitenessPolicy, RetryPolicy, ChangeDetector, HeadlessBrowser.
"""

import json
import logging
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from .sources import SourceConfig, SourceRegistry
from .fetcher import DocumentFetcher
from .extractor import FactExtractor
from .health import HealthTracker
from .knowledge_base import KnowledgeBase
from .seed_loader import is_seeded, load_seeds
from .stealth import StealthLevel, StealthProfile
from .proxy import ProxyRotator

logger = logging.getLogger(__name__)


class ScrapeOrchestrator:
    """Orchestrates scraping, extraction, and KB update."""

    def __init__(
        self,
        data_dir: str = "data/scraper",
        respect_robots: bool = True,
        stealth: Optional[StealthProfile] = None,
        proxy_rotator: Optional[ProxyRotator] = None,
    ):
        self.data_dir = Path(data_dir)
        self.jobs_dir = self.data_dir / "jobs"
        self.jobs_dir.mkdir(parents=True, exist_ok=True)

        self.stealth = stealth or StealthProfile()
        self.proxy_rotator = proxy_rotator or ProxyRotator()

        self.registry = SourceRegistry(data_dir)
        self.fetcher = DocumentFetcher(
            data_dir, respect_robots=respect_robots,
            stealth=self.stealth, proxy_rotator=self.proxy_rotator,
        )
        self.extractor = FactExtractor(data_dir)
        self.kb = KnowledgeBase(data_dir)
        self.health = HealthTracker(data_dir)

        # Auto-seed KB on first use if empty
        self.ensure_seeded()

    def ensure_seeded(self) -> int:
        """Load seed facts into KB if it's empty. Returns count added."""
        if not self.kb._facts:
            return load_seeds(self.kb)
        return 0

    # -- job tracking ----------------------------------------------------------

    def _create_job(self, source_ids: List[str]) -> Dict[str, Any]:
        job_id = f"scrape_{datetime.now(tz=timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        job: Dict[str, Any] = {
            "id": job_id,
            "status": "running",
            "phase": "starting",
            "started_at": datetime.now(tz=timezone.utc).isoformat(),
            "finished_at": None,
            "sources_requested": source_ids,
            "sources_done": 0,
            "sources_total": len(source_ids),
            "docs_found": 0,
            "docs_new": 0,
            "docs_failed": 0,
            "facts_extracted": 0,
            "robots_blocked": 0,
            "unchanged_skipped": 0,
            "retry_count": 0,
            "browser_rendered": 0,
            "stealth_level_used": int(self.stealth.level),
            "proxy_used": self.proxy_rotator.count > 0,
            "errors": [],
        }
        self._save_job(job)
        return job

    def _save_job(self, job: Dict[str, Any]) -> None:
        fp = self.jobs_dir / f"{job['id']}.json"
        fp.write_text(json.dumps(job, indent=2, default=str), encoding="utf-8")

    def _update_job(self, job: Dict[str, Any], updates: Dict[str, Any]) -> None:
        job.update(updates)
        self._save_job(job)

    def get_job(self, job_id: str) -> Optional[Dict[str, Any]]:
        fp = self.jobs_dir / f"{job_id}.json"
        if not fp.exists():
            return None
        return json.loads(fp.read_text(encoding="utf-8"))

    def list_jobs(self, limit: int = 20) -> List[Dict[str, Any]]:
        jobs = []
        for fp in sorted(self.jobs_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
            try:
                jobs.append(json.loads(fp.read_text(encoding="utf-8")))
            except Exception:
                continue
            if len(jobs) >= limit:
                break
        return jobs

    # -- main workflow ---------------------------------------------------------

    async def run(
        self,
        source_ids: Optional[List[str]] = None,
        extract: bool = True,
        api_client=None,
        model_id: str = "",
        force_refetch: bool = False,
        use_browser: bool = False,
        extraction_strategy: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Run the full scrape → extract → KB update pipeline.

        Args:
            source_ids: Specific source IDs to scrape (None = all enabled).
            extract: Whether to run LLM fact extraction on new docs.
            api_client: UnifiedAPIClient instance (required if extract=True).
            model_id: Model to use for extraction.
            force_refetch: Skip change-detection (re-fetch everything).
            use_browser: Force Playwright for all sources (otherwise per-source).

        Returns:
            Job result dict.
        """
        # Resolve sources
        if source_ids:
            sources = [s for s in self.registry.list_sources() if s.id in source_ids]
        else:
            sources = self.registry.list_sources(enabled_only=True)

        if not sources:
            return {"status": "error", "message": "No sources to scrape"}

        job = self._create_job([s.id for s in sources])

        try:
            self._update_job(job, {"phase": "fetching"})

            for idx, source in enumerate(sources):
                try:
                    needs_browser = use_browser or source.requires_js
                    new_docs = await self._scrape_source(
                        source, job,
                        force_refetch=force_refetch,
                        use_browser=needs_browser,
                    )

                    if extract and api_client and model_id and new_docs:
                        self._update_job(job, {"phase": f"extracting ({source.name})"})
                        for doc in new_docs:
                            try:
                                result = await self.extractor.extract(
                                    document_text=doc.text,
                                    document_id=doc.id,
                                    client=api_client,
                                    model_id=model_id,
                                    extraction_strategy=extraction_strategy,
                                    source_id=source.id,
                                    source_tier=source.tier,
                                )
                                if result.facts:
                                    added = self.kb.merge_extraction(
                                        result.facts, doc.id,
                                        confidence_scores=result.confidence_scores,
                                    )
                                    job["facts_extracted"] += added
                            except Exception as e:
                                job["errors"].append(f"Extract {doc.id}: {e}")

                    self.registry.mark_checked(source.id, len(new_docs))
                except Exception as e:
                    job["errors"].append(f"Source {source.id}: {e}")

                job["sources_done"] = idx + 1
                job["retry_count"] = self.fetcher.retry_policy.total_retries
                self._update_job(job, {"phase": f"fetching ({idx + 1}/{len(sources)})"})

            self._update_job(job, {
                "status": "completed",
                "phase": "done",
                "finished_at": datetime.now(tz=timezone.utc).isoformat(),
            })

        except Exception as e:
            self._update_job(job, {
                "status": "error",
                "phase": "failed",
                "finished_at": datetime.now(tz=timezone.utc).isoformat(),
                "errors": job["errors"] + [str(e)],
            })

        return job

    async def _scrape_source(
        self,
        source: SourceConfig,
        job: Dict[str, Any],
        force_refetch: bool = False,
        use_browser: bool = False,
    ) -> list:
        """Scrape a single source: fetch index page, find links, download docs."""
        new_docs = []

        # Apply per-source stealth override (use higher of global vs source-specific)
        source_level = getattr(source, "stealth_level", 0)
        effective_level = max(int(self.stealth.level), source_level)
        if effective_level != int(self.stealth.level):
            self.fetcher.stealth = StealthProfile.from_level(
                StealthLevel(effective_level)
            )
            logger.info(
                "Elevated stealth to level %d for source %s",
                effective_level, source.id,
            )

        try:
            html, _ = await self.fetcher.fetch_page(
                source.url, use_browser=use_browser,
            )
            if use_browser:
                job["browser_rendered"] += 1
            self.health.record_success(source.id, effective_level)
        except PermissionError:
            job["robots_blocked"] += 1
            job["errors"].append(f"Blocked by robots.txt: {source.url}")
            self.health.record_failure(source.id, status_code=0, stealth_level_used=effective_level)
            return new_docs
        except Exception as e:
            job["errors"].append(f"Fetch {source.url}: {e}")
            self.health.record_failure(source.id, status_code=0, stealth_level_used=effective_level)
            return new_docs

        if not html:
            job["unchanged_skipped"] += 1
            return new_docs

        # Discover document links (with sitemap/RSS fallback)
        links = await self.fetcher.extract_links_with_fallback(
            html, source.url, source.selectors, feed_url=source.feed_url,
        )
        job["docs_found"] += len(links)
        self._save_job(job)

        # Download each linked document
        for link_url in links:
            try:
                doc = await self.fetcher.fetch_document(
                    link_url, source.id,
                    use_browser=use_browser,
                    force_refetch=force_refetch,
                    language=source.language,
                )
                if doc:
                    new_docs.append(doc)
                    job["docs_new"] += 1
                else:
                    # Could be unchanged or duplicate
                    job["unchanged_skipped"] += 1
            except PermissionError:
                job["robots_blocked"] += 1
            except Exception:
                job["docs_failed"] += 1
            # Flush progress to disk after each document
            self._save_job(job)

        # Restore global stealth level if it was elevated for this source
        if effective_level != int(self.stealth.level):
            self.fetcher.stealth = self.stealth

        return new_docs
