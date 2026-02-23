"""
Document Intelligence Agent — dashboard API routes.

Manages sources, triggers scrape jobs, browses documents,
queries the knowledge base.
"""

import asyncio
import json
from pathlib import Path
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx
from ....scraper.sources import SourceConfig, SourceRegistry, TIER_LABELS
from ....scraper.fetcher import DocumentFetcher
from ....scraper.extractor import FactExtractor, FACT_TYPES, EXTRACTION_STRATEGIES
from ....scraper.knowledge_base import KnowledgeBase
from ....scraper.health import HealthTracker
from ....scraper.scheduler import ScrapeOrchestrator
from ....scraper.seed_loader import load_seeds, is_seeded
from ....scraper.change_detection import ChangeDetector
from ....scraper.feed_parser import FeedParser
from ....scraper.browser import HeadlessBrowser, STEALTH_PATCH_AVAILABLE
from ....scraper.stealth import StealthLevel, StealthProfile, STEALTH_LABELS
from ....scraper.proxy import ProxyRotator
from ....scraper.indicator_matrix import IndicatorMatrix
from ....api_client import UnifiedAPIClient

router = APIRouter()

_active_scrape_task = None


def _data_dir(ctx: AppContext) -> str:
    return str(ctx.data_dir).rstrip("/\\") + "/scraper"


# =============================================================================
# Request Models
# =============================================================================

class SourceCreate(BaseModel):
    id: str
    name: str
    tier: int = 5
    url: str
    content_type: str = "html"
    selectors: List[str] = Field(default_factory=list)
    schedule_days: int = 30
    description: str = ""
    requires_js: bool = False
    feed_url: Optional[str] = None
    language: str = "en"
    corridors: List[str] = Field(default_factory=list)
    stealth_level: int = 0


class SourceUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    enabled: Optional[bool] = None
    selectors: Optional[List[str]] = None
    schedule_days: Optional[int] = None
    description: Optional[str] = None
    requires_js: Optional[bool] = None
    feed_url: Optional[str] = None
    language: Optional[str] = None
    corridors: Optional[List[str]] = None
    stealth_level: Optional[int] = None


class ScrapeRequest(BaseModel):
    source_ids: Optional[List[str]] = None
    extract: bool = False
    endpoint_id: Optional[str] = None
    model_id: Optional[str] = None
    force_refetch: bool = False
    use_browser: bool = False
    respect_robots: bool = True
    stealth_level: Optional[int] = None  # override global stealth level for this run
    extraction_strategy: Optional[str] = None  # default, legal_case, legislation, report


class KBQueryRequest(BaseModel):
    category: Optional[str] = None
    jurisdiction: Optional[str] = None
    corridor: Optional[str] = None
    limit: int = 100


# =============================================================================
# Sources
# =============================================================================

@router.get("/sources")
async def list_sources(
    ctx: AppContext = Depends(get_ctx),
    tier: Optional[int] = None,
    enabled_only: bool = False,
):
    """List all configured scraping sources."""
    reg = SourceRegistry(data_dir=_data_dir(ctx))
    sources = reg.list_sources(tier=tier, enabled_only=enabled_only)
    return {
        "status": "success",
        "sources": [
            {
                "id": s.id, "name": s.name, "tier": s.tier, "url": s.url,
                "content_type": s.content_type, "selectors": s.selectors,
                "schedule_days": s.schedule_days, "enabled": s.enabled,
                "last_checked": s.last_checked, "doc_count": s.doc_count,
                "description": s.description,
                "requires_js": s.requires_js, "feed_url": s.feed_url,
                "language": s.language, "corridors": s.corridors,
                "stealth_level": getattr(s, "stealth_level", 0),
            }
            for s in sources
        ],
        "count": len(sources),
        "tier_labels": TIER_LABELS,
    }


@router.post("/sources")
async def create_source(request: SourceCreate, ctx: AppContext = Depends(get_ctx)):
    """Add a new scraping source."""
    reg = SourceRegistry(data_dir=_data_dir(ctx))
    if reg.get(request.id):
        raise HTTPException(status_code=409, detail=f"Source {request.id} already exists")
    config = SourceConfig(
        id=request.id, name=request.name, tier=request.tier,
        url=request.url, content_type=request.content_type,
        selectors=request.selectors, schedule_days=request.schedule_days,
        description=request.description,
        requires_js=request.requires_js, feed_url=request.feed_url,
        language=request.language, corridors=request.corridors,
        stealth_level=request.stealth_level,
    )
    reg.create(config)
    return {"status": "success", "source_id": request.id}


@router.put("/sources/{source_id}")
async def update_source(source_id: str, request: SourceUpdate, ctx: AppContext = Depends(get_ctx)):
    """Update a source configuration."""
    reg = SourceRegistry(data_dir=_data_dir(ctx))
    updates = {k: v for k, v in request.model_dump().items() if v is not None}
    result = reg.update(source_id, updates)
    if not result:
        raise HTTPException(status_code=404, detail=f"Source {source_id} not found")
    return {"status": "success", "message": f"Source {source_id} updated"}


@router.put("/sources/{source_id}/toggle")
async def toggle_source(source_id: str, ctx: AppContext = Depends(get_ctx)):
    """Toggle a source's enabled state."""
    reg = SourceRegistry(data_dir=_data_dir(ctx))
    new_state = reg.toggle(source_id)
    if new_state is None:
        raise HTTPException(status_code=404, detail=f"Source {source_id} not found")
    return {"status": "success", "enabled": new_state}


@router.delete("/sources/{source_id}")
async def delete_source(source_id: str, ctx: AppContext = Depends(get_ctx)):
    """Remove a scraping source."""
    reg = SourceRegistry(data_dir=_data_dir(ctx))
    if not reg.delete(source_id):
        raise HTTPException(status_code=404, detail=f"Source {source_id} not found")
    return {"status": "success", "message": f"Source {source_id} deleted"}


@router.get("/sources/health")
async def source_health(ctx: AppContext = Depends(get_ctx)):
    """Get per-source health statistics (success rates, recommended stealth)."""
    tracker = HealthTracker(data_dir=_data_dir(ctx))
    return {"status": "success", "sources": tracker.summary()}


# =============================================================================
# Scrape Jobs
# =============================================================================

@router.post("/run")
async def start_scrape(request: ScrapeRequest, ctx: AppContext = Depends(get_ctx)):
    """Trigger a background scrape job."""
    global _active_scrape_task

    data_dir = _data_dir(ctx)

    api_client = None
    model_id = ""
    if request.extract and request.endpoint_id and request.model_id:
        ep = ctx.config_manager.get_endpoint(request.endpoint_id)
        if not ep or not ep.get("api_key"):
            raise HTTPException(status_code=400, detail="Valid endpoint with API key required for extraction")
        api_client = UnifiedAPIClient(endpoint=ep)
        model_id = request.model_id

    # Load stealth config
    stealth = _load_stealth_config(data_dir)
    if request.stealth_level is not None:
        stealth = StealthProfile.from_level(StealthLevel(request.stealth_level))
    proxy_rotator = ProxyRotator(proxies=stealth.proxy_list, rotation=stealth.proxy_rotation)

    orch = ScrapeOrchestrator(
        data_dir=data_dir, respect_robots=request.respect_robots,
        stealth=stealth, proxy_rotator=proxy_rotator,
    )

    async def _run():
        return await orch.run(
            source_ids=request.source_ids,
            extract=request.extract,
            api_client=api_client,
            model_id=model_id,
            force_refetch=request.force_refetch,
            use_browser=request.use_browser,
            extraction_strategy=request.extraction_strategy,
        )

    task = asyncio.create_task(_run())
    _active_scrape_task = task

    return {
        "status": "success",
        "message": "Scrape job started",
        "note": "Poll /api/scraper/jobs to see progress",
    }


@router.get("/jobs")
async def list_jobs(ctx: AppContext = Depends(get_ctx), limit: int = 20):
    """List recent scrape jobs."""
    orch = ScrapeOrchestrator(data_dir=_data_dir(ctx))
    jobs = orch.list_jobs(limit=limit)
    return {"status": "success", "jobs": jobs, "count": len(jobs)}


@router.get("/jobs/{job_id}")
async def get_job(job_id: str, ctx: AppContext = Depends(get_ctx)):
    """Get a specific job's status and progress."""
    orch = ScrapeOrchestrator(data_dir=_data_dir(ctx))
    job = orch.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    return {"status": "success", "job": job}


# =============================================================================
# Documents
# =============================================================================

@router.get("/documents")
async def list_documents(
    ctx: AppContext = Depends(get_ctx),
    source_id: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
):
    """Browse downloaded documents."""
    fetcher = DocumentFetcher(data_dir=_data_dir(ctx))
    docs = fetcher.list_documents(source_id=source_id, limit=limit, offset=offset)
    total = fetcher.count_documents(source_id=source_id)
    return {"status": "success", "documents": docs, "total": total}


@router.get("/documents/{doc_id}")
async def get_document(doc_id: str, ctx: AppContext = Depends(get_ctx)):
    """Get a document with its extracted facts."""
    fetcher = DocumentFetcher(data_dir=_data_dir(ctx))
    doc = fetcher.load_document(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")

    extractor = FactExtractor(data_dir=_data_dir(ctx))
    extraction = extractor.load_extraction(doc_id)

    result = {
        "id": doc.id,
        "url": doc.url,
        "title": doc.title,
        "text": doc.text[:5000],
        "text_length": len(doc.text),
        "content_type": doc.content_type,
        "fetched_at": doc.fetched_at,
        "source_id": doc.source_id,
        "word_count": doc.word_count,
        "language": getattr(doc, "language", "en"),
        "page_count": getattr(doc, "page_count", None),
    }

    if extraction:
        result["extraction"] = {
            "facts": extraction.facts,
            "summary": extraction.summary,
            "relevance_score": extraction.relevance_score,
            "extracted_at": extraction.extracted_at,
            "confidence_scores": extraction.confidence_scores,
            "citations": extraction.citations,
            "entities": extraction.entities,
        }

    return {"status": "success", "document": result}


@router.delete("/documents/{doc_id}")
async def delete_document(doc_id: str, ctx: AppContext = Depends(get_ctx)):
    """Delete a downloaded document."""
    fetcher = DocumentFetcher(data_dir=_data_dir(ctx))
    if not fetcher.delete_document(doc_id):
        raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")
    return {"status": "success", "message": f"Document {doc_id} deleted"}


# =============================================================================
# Knowledge Base
# =============================================================================

@router.get("/knowledge-base")
async def kb_stats(ctx: AppContext = Depends(get_ctx)):
    """Get knowledge base statistics."""
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    stats = kb.stats()
    stats["seeded"] = is_seeded(kb)
    return {"status": "success", **stats}


@router.get("/knowledge-base/query")
async def kb_query(
    ctx: AppContext = Depends(get_ctx),
    category: Optional[str] = None,
    jurisdiction: Optional[str] = None,
    corridor: Optional[str] = None,
    limit: int = 100,
):
    """Query facts from the knowledge base."""
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    facts = kb.query(category=category, jurisdiction=jurisdiction, corridor=corridor, limit=limit)
    return {"status": "success", "facts": facts, "count": len(facts)}


@router.post("/knowledge-base/rebuild")
async def kb_rebuild(ctx: AppContext = Depends(get_ctx)):
    """Rebuild the knowledge base from all extractions."""
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    counts = kb.rebuild()
    return {"status": "success", "message": "Knowledge base rebuilt", "counts": counts}


@router.post("/knowledge-base/seed")
async def kb_seed(ctx: AppContext = Depends(get_ctx)):
    """Load seed facts into the knowledge base.

    Idempotent — running multiple times does not create duplicates.
    """
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    already = is_seeded(kb)
    added = load_seeds(kb)
    return {
        "status": "success",
        "loaded": added,
        "already_seeded": already and added == 0,
        "total_facts": len(kb._facts),
    }


@router.get("/knowledge-base/timeline")
async def kb_timeline(
    ctx: AppContext = Depends(get_ctx),
    category: Optional[str] = None,
    corridor: Optional[str] = None,
    limit: int = 50,
):
    """Get facts sorted by discovery date (newest first)."""
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    facts = kb.query_timeline(category=category, corridor=corridor, limit=limit)
    return {"status": "success", "facts": facts, "count": len(facts)}


@router.get("/knowledge-base/stale")
async def kb_stale(ctx: AppContext = Depends(get_ctx), days: int = 90):
    """Get facts not confirmed in the last N days."""
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    facts = kb.get_stale_facts(days=days)
    return {"status": "success", "facts": facts, "count": len(facts)}


@router.get("/knowledge-base/entities")
async def kb_entities(ctx: AppContext = Depends(get_ctx)):
    """Get aggregated entities across all KB facts."""
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    entities = kb.query_entities()
    return {"status": "success", "entities": entities, "count": len(entities)}


@router.get("/knowledge-base/cross-refs/{fact_index}")
async def kb_cross_refs(fact_index: int, ctx: AppContext = Depends(get_ctx)):
    """Get facts cross-referenced with a specific fact."""
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    related = kb.query_cross_referenced(fact_index)
    return {"status": "success", "related_facts": related, "count": len(related)}


# =============================================================================
# Extraction Strategies & Fact Types
# =============================================================================

@router.get("/extraction-strategies")
async def list_extraction_strategies():
    """List available extraction strategies for document processing."""
    return {
        "status": "success",
        "strategies": EXTRACTION_STRATEGIES,
        "descriptions": {
            "default": "General-purpose extraction for all document types",
            "legal_case": "Optimized for court decisions — extracts holdings, arguments, citations, evidentiary standards",
            "legislation": "Optimized for statutes/laws — extracts provisions, protections, penalties element-by-element",
            "report": "Optimized for NGO/IGO reports — extracts statistics with methodology, case studies, recommendations",
        },
    }


@router.get("/knowledge-base/fact-types")
async def kb_fact_types(ctx: AppContext = Depends(get_ctx)):
    """List all available fact types and their counts in the KB."""
    kb = KnowledgeBase(data_dir=_data_dir(ctx))
    stats = kb.stats()
    return {
        "status": "success",
        "available_types": FACT_TYPES,
        "counts": stats.get("by_category", {}),
        "total_types": len(FACT_TYPES),
    }


# =============================================================================
# Change Detection
# =============================================================================

@router.get("/fingerprints")
async def fingerprint_stats(ctx: AppContext = Depends(get_ctx)):
    """Get change-detection fingerprint cache stats."""
    cd = ChangeDetector(data_dir=_data_dir(ctx))
    return {"status": "success", **cd.stats()}


@router.post("/fingerprints/clear")
async def fingerprint_clear(ctx: AppContext = Depends(get_ctx)):
    """Clear the fingerprint cache (forces re-fetch on next scrape)."""
    cd = ChangeDetector(data_dir=_data_dir(ctx))
    cleared = cd.clear()
    return {"status": "success", "cleared": cleared}


# =============================================================================
# RSS Feeds
# =============================================================================

@router.get("/feeds")
async def list_feeds(ctx: AppContext = Depends(get_ctx)):
    """List sources that have RSS/Atom feed URLs configured."""
    reg = SourceRegistry(data_dir=_data_dir(ctx))
    sources = [s for s in reg.list_sources() if s.feed_url]
    return {
        "status": "success",
        "feeds": [
            {"source_id": s.id, "name": s.name, "feed_url": s.feed_url}
            for s in sources
        ],
        "count": len(sources),
    }


@router.post("/feeds/check")
async def check_feeds(ctx: AppContext = Depends(get_ctx)):
    """Test all configured RSS/Atom feeds and return results."""
    reg = SourceRegistry(data_dir=_data_dir(ctx))
    parser = FeedParser()
    sources = [s for s in reg.list_sources() if s.feed_url]
    results = []
    for s in sources:
        entries = await parser.fetch_and_parse_feed(s.feed_url)
        results.append({
            "source_id": s.id,
            "name": s.name,
            "feed_url": s.feed_url,
            "entry_count": len(entries),
            "ok": len(entries) > 0,
            "latest_title": entries[0].title if entries else None,
        })
    return {"status": "success", "results": results}


# =============================================================================
# Browser Status
# =============================================================================

@router.get("/browser/status")
async def browser_status():
    """Check Playwright headless browser availability."""
    info = await HeadlessBrowser.status()
    return {"status": "success", **info}


# =============================================================================
# Source Validation
# =============================================================================

@router.post("/sources/validate")
async def validate_source(request: SourceCreate, ctx: AppContext = Depends(get_ctx)):
    """Test a source URL and its selectors without saving."""
    fetcher = DocumentFetcher(data_dir=_data_dir(ctx))
    try:
        html, _ = await fetcher.fetch_page(request.url, use_browser=request.requires_js)
        links = fetcher.extract_links(html, request.url, request.selectors)
        return {
            "status": "success",
            "reachable": True,
            "links_found": len(links),
            "sample_links": links[:5],
        }
    except Exception as exc:
        return {
            "status": "success",
            "reachable": False,
            "error": str(exc),
            "links_found": 0,
        }


# =============================================================================
# Stealth Configuration
# =============================================================================

def _stealth_config_path(data_dir: str) -> Path:
    return Path(data_dir) / "stealth_config.json"


def _load_stealth_config(data_dir: str) -> StealthProfile:
    """Load stealth config from disk, falling back to defaults."""
    fp = _stealth_config_path(data_dir)
    if fp.exists():
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
            return StealthProfile.from_dict(data)
        except Exception:
            pass
    return StealthProfile()


def _save_stealth_config(data_dir: str, profile: StealthProfile) -> None:
    fp = _stealth_config_path(data_dir)
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(json.dumps(profile.to_dict(), indent=2), encoding="utf-8")


class StealthConfigUpdate(BaseModel):
    level: Optional[int] = None
    rotate_ua: Optional[bool] = None
    ua_browser: Optional[str] = None
    realistic_headers: Optional[bool] = None
    jitter_enabled: Optional[bool] = None
    jitter_min: Optional[float] = None
    jitter_max: Optional[float] = None
    tls_impersonate: Optional[str] = None
    persist_cookies: Optional[bool] = None
    proxy_enabled: Optional[bool] = None
    proxy_list: Optional[List[str]] = None
    proxy_rotation: Optional[str] = None
    viewport_randomize: Optional[bool] = None
    locale_randomize: Optional[bool] = None
    timezone_spoof: Optional[str] = None


@router.get("/stealth/status")
async def stealth_status():
    """Check which stealth packages are installed."""
    from ....scraper.fetcher import CURL_CFFI_AVAILABLE

    nodriver_available = False
    try:
        import nodriver  # type: ignore[import-untyped]
        nodriver_available = True
    except ImportError:
        pass

    fake_ua_available = False
    try:
        from fake_useragent import UserAgent  # type: ignore[import-untyped]
        fake_ua_available = True
    except ImportError:
        pass

    return {
        "status": "success",
        "packages": {
            "fake_useragent": fake_ua_available,
            "curl_cffi": CURL_CFFI_AVAILABLE,
            "playwright_stealth": STEALTH_PATCH_AVAILABLE,
            "nodriver": nodriver_available,
        },
        "levels": STEALTH_LABELS,
    }


@router.get("/stealth/config")
async def get_stealth_config(ctx: AppContext = Depends(get_ctx)):
    """Get current stealth settings."""
    profile = _load_stealth_config(_data_dir(ctx))
    return {"status": "success", "config": profile.to_dict()}


@router.put("/stealth/config")
async def update_stealth_config(
    request: StealthConfigUpdate, ctx: AppContext = Depends(get_ctx),
):
    """Update stealth settings."""
    data_dir = _data_dir(ctx)
    profile = _load_stealth_config(data_dir)
    updates = {k: v for k, v in request.model_dump().items() if v is not None}

    if "level" in updates:
        # If level changed, start from the level defaults then overlay user overrides
        new_level = StealthLevel(updates.pop("level"))
        profile = StealthProfile.from_level(new_level)
        # Apply remaining overrides on top
        for k, v in updates.items():
            if hasattr(profile, k):
                setattr(profile, k, v)
    else:
        for k, v in updates.items():
            if hasattr(profile, k):
                setattr(profile, k, v)

    _save_stealth_config(data_dir, profile)
    return {"status": "success", "config": profile.to_dict()}


@router.get("/stealth/proxy-health")
async def proxy_health(ctx: AppContext = Depends(get_ctx)):
    """Get proxy health statistics."""
    profile = _load_stealth_config(_data_dir(ctx))
    rotator = ProxyRotator(proxies=profile.proxy_list, rotation=profile.proxy_rotation)
    return {
        "status": "success",
        "proxy_count": rotator.count,
        "health": rotator.get_health(),
    }


# =============================================================================
# Indicator Stacking Matrix
# =============================================================================

class IndicatorScoreRequest(BaseModel):
    action_ids: List[str]
    corridor: Optional[str] = None
    sector: Optional[str] = None


@router.get("/indicator-matrix")
async def get_indicator_matrix(ctx: AppContext = Depends(get_ctx)):
    """Full phase x indicator matrix with action counts."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    return {
        "status": "success",
        "phases": [p["phase"] for p in matrix.list_phases()],
        "indicators": list(matrix.ILO_INDICATORS),
        "matrix": matrix.get_matrix_counts(),
        "total_actions": matrix.total_actions,
        "total_patterns": matrix.total_patterns,
    }


@router.get("/indicator-matrix/phases")
async def list_phases(ctx: AppContext = Depends(get_ctx)):
    """List journey phases with descriptions and action counts."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    return {"status": "success", "phases": matrix.list_phases()}


@router.get("/indicator-matrix/actions")
async def list_indicator_actions(
    ctx: AppContext = Depends(get_ctx),
    phase: Optional[str] = None,
    indicator: Optional[str] = None,
    sector: Optional[str] = None,
    corridor: Optional[str] = None,
):
    """Filter and list individual indicator actions."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    actions = matrix.get_filtered_actions(
        phase=phase, indicator=indicator, sector=sector, corridor=corridor,
    )
    return {"status": "success", "actions": actions, "count": len(actions)}


@router.get("/indicator-matrix/combinations")
async def get_combinations(
    ctx: AppContext = Depends(get_ctx),
    min_risk: str = "yellow_flag",
    sector: Optional[str] = None,
    corridor: Optional[str] = None,
):
    """Known high-risk indicator combinations with risk scores."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    combos = matrix.get_stacking_combos(min_risk=min_risk)
    if sector:
        combos = [c for c in combos if sector in c.get("sectors", [])]
    if corridor:
        combos = [c for c in combos if corridor in c.get("corridors", [])]
    return {"status": "success", "combinations": combos, "count": len(combos)}


@router.get("/indicator-matrix/corridors")
async def list_corridor_profiles(ctx: AppContext = Depends(get_ctx)):
    """List all available corridor indicator profiles."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    return {"status": "success", "corridors": matrix.list_corridors(), "count": matrix.total_corridors}


@router.get("/indicator-matrix/corridor/{corridor_id}")
async def get_corridor_profile(corridor_id: str, ctx: AppContext = Depends(get_ctx)):
    """Corridor-specific indicator stacking profile."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    profile = matrix.get_corridor_profile(corridor_id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"Corridor {corridor_id} not found")
    return {"status": "success", "profile": profile}


@router.get("/indicator-matrix/sectors")
async def list_sectors(ctx: AppContext = Depends(get_ctx)):
    """List all sectors with action counts."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    return {"status": "success", "sectors": matrix.list_sectors(), "count": len(matrix.list_sectors())}


@router.get("/indicator-matrix/sector/{sector}")
async def get_sector_profile(sector: str, ctx: AppContext = Depends(get_ctx)):
    """Sector-specific indicator profile."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    return {"status": "success", "profile": matrix.get_sector_profile(sector)}


@router.post("/indicator-matrix/score")
async def score_indicators(request: IndicatorScoreRequest, ctx: AppContext = Depends(get_ctx)):
    """Score a set of observed actions for trafficking risk."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    result = matrix.score_actions(request.action_ids)
    return {"status": "success", **result.to_dict()}


@router.get("/indicator-matrix/palermo-mapping")
async def get_palermo_mapping(ctx: AppContext = Depends(get_ctx)):
    """Map all indicator actions to Palermo Protocol elements."""
    matrix = IndicatorMatrix(data_dir=_data_dir(ctx))
    return {"status": "success", "mapping": matrix.get_palermo_mapping()}
