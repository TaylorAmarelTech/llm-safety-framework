"""
Document Intelligence Agent — dashboard API routes.

Manages sources, triggers scrape jobs, browses documents,
queries the knowledge base.
"""

import asyncio
from typing import Dict, List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..config import get_settings
from ...scraper.sources import SourceConfig, SourceRegistry
from ...scraper.fetcher import DocumentFetcher
from ...scraper.extractor import FactExtractor
from ...scraper.knowledge_base import KnowledgeBase
from ...scraper.scheduler import ScrapeOrchestrator
from ...api_client import UnifiedAPIClient

router = APIRouter()

# In-memory reference to running job task
_active_scrape_task = None


def _data_dir() -> str:
    settings = get_settings()
    return str(settings.data_dir).rstrip("/\\") + "/scraper"


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


class SourceUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    enabled: Optional[bool] = None
    selectors: Optional[List[str]] = None
    schedule_days: Optional[int] = None
    description: Optional[str] = None


class ScrapeRequest(BaseModel):
    source_ids: Optional[List[str]] = None  # None = all enabled
    extract: bool = False
    endpoint_id: Optional[str] = None  # endpoint for LLM extraction
    model_id: Optional[str] = None


class KBQueryRequest(BaseModel):
    category: Optional[str] = None
    jurisdiction: Optional[str] = None
    corridor: Optional[str] = None
    limit: int = 100


# =============================================================================
# Sources
# =============================================================================

@router.get("/sources")
async def list_sources(tier: Optional[int] = None, enabled_only: bool = False):
    """List all configured scraping sources."""
    reg = SourceRegistry(data_dir=_data_dir())
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
            }
            for s in sources
        ],
        "count": len(sources),
    }


@router.post("/sources")
async def create_source(request: SourceCreate):
    """Add a new scraping source."""
    reg = SourceRegistry(data_dir=_data_dir())
    if reg.get(request.id):
        raise HTTPException(status_code=409, detail=f"Source {request.id} already exists")
    config = SourceConfig(
        id=request.id, name=request.name, tier=request.tier,
        url=request.url, content_type=request.content_type,
        selectors=request.selectors, schedule_days=request.schedule_days,
        description=request.description,
    )
    reg.create(config)
    return {"status": "success", "source_id": request.id}


@router.put("/sources/{source_id}")
async def update_source(source_id: str, request: SourceUpdate):
    """Update a source configuration."""
    reg = SourceRegistry(data_dir=_data_dir())
    updates = {k: v for k, v in request.model_dump().items() if v is not None}
    result = reg.update(source_id, updates)
    if not result:
        raise HTTPException(status_code=404, detail=f"Source {source_id} not found")
    return {"status": "success", "message": f"Source {source_id} updated"}


@router.put("/sources/{source_id}/toggle")
async def toggle_source(source_id: str):
    """Toggle a source's enabled state."""
    reg = SourceRegistry(data_dir=_data_dir())
    new_state = reg.toggle(source_id)
    if new_state is None:
        raise HTTPException(status_code=404, detail=f"Source {source_id} not found")
    return {"status": "success", "enabled": new_state}


@router.delete("/sources/{source_id}")
async def delete_source(source_id: str):
    """Remove a scraping source."""
    reg = SourceRegistry(data_dir=_data_dir())
    if not reg.delete(source_id):
        raise HTTPException(status_code=404, detail=f"Source {source_id} not found")
    return {"status": "success", "message": f"Source {source_id} deleted"}


# =============================================================================
# Scrape Jobs
# =============================================================================

@router.post("/run")
async def start_scrape(request: ScrapeRequest):
    """Trigger a background scrape job."""
    global _active_scrape_task

    data_dir = _data_dir()

    # Build API client if extraction requested
    api_client = None
    model_id = ""
    if request.extract and request.endpoint_id and request.model_id:
        from ...web.config import ConfigManager
        cm = ConfigManager()
        ep = cm.get_endpoint(request.endpoint_id)
        if not ep or not ep.get("api_key"):
            raise HTTPException(status_code=400, detail="Valid endpoint with API key required for extraction")
        api_client = UnifiedAPIClient(endpoint=ep)
        model_id = request.model_id

    orch = ScrapeOrchestrator(data_dir=data_dir)

    async def _run():
        return await orch.run(
            source_ids=request.source_ids,
            extract=request.extract,
            api_client=api_client,
            model_id=model_id,
        )

    # Run in background
    task = asyncio.create_task(_run())
    _active_scrape_task = task

    # Return a preliminary job ID (the orchestrator creates the actual job)
    return {
        "status": "success",
        "message": "Scrape job started",
        "note": "Poll /api/scraper/jobs to see progress",
    }


@router.get("/jobs")
async def list_jobs(limit: int = 20):
    """List recent scrape jobs."""
    orch = ScrapeOrchestrator(data_dir=_data_dir())
    jobs = orch.list_jobs(limit=limit)
    return {"status": "success", "jobs": jobs, "count": len(jobs)}


@router.get("/jobs/{job_id}")
async def get_job(job_id: str):
    """Get a specific job's status and progress."""
    orch = ScrapeOrchestrator(data_dir=_data_dir())
    job = orch.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    return {"status": "success", "job": job}


# =============================================================================
# Documents
# =============================================================================

@router.get("/documents")
async def list_documents(source_id: Optional[str] = None, limit: int = 50, offset: int = 0):
    """Browse downloaded documents."""
    fetcher = DocumentFetcher(data_dir=_data_dir())
    docs = fetcher.list_documents(source_id=source_id, limit=limit, offset=offset)
    total = fetcher.count_documents(source_id=source_id)
    return {"status": "success", "documents": docs, "total": total}


@router.get("/documents/{doc_id}")
async def get_document(doc_id: str):
    """Get a document with its extracted facts."""
    fetcher = DocumentFetcher(data_dir=_data_dir())
    doc = fetcher.load_document(doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")

    # Also load extraction if available
    extractor = FactExtractor(data_dir=_data_dir())
    extraction = extractor.load_extraction(doc_id)

    result = {
        "id": doc.id,
        "url": doc.url,
        "title": doc.title,
        "text": doc.text[:5000],  # Truncate for API response
        "text_length": len(doc.text),
        "content_type": doc.content_type,
        "fetched_at": doc.fetched_at,
        "source_id": doc.source_id,
        "word_count": doc.word_count,
    }

    if extraction:
        result["extraction"] = {
            "facts": extraction.facts,
            "summary": extraction.summary,
            "relevance_score": extraction.relevance_score,
            "extracted_at": extraction.extracted_at,
        }

    return {"status": "success", "document": result}


@router.delete("/documents/{doc_id}")
async def delete_document(doc_id: str):
    """Delete a downloaded document."""
    fetcher = DocumentFetcher(data_dir=_data_dir())
    if not fetcher.delete_document(doc_id):
        raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")
    return {"status": "success", "message": f"Document {doc_id} deleted"}


# =============================================================================
# Knowledge Base
# =============================================================================

@router.get("/knowledge-base")
async def kb_stats():
    """Get knowledge base statistics."""
    kb = KnowledgeBase(data_dir=_data_dir())
    stats = kb.stats()
    return {"status": "success", **stats}


@router.get("/knowledge-base/query")
async def kb_query(
    category: Optional[str] = None,
    jurisdiction: Optional[str] = None,
    corridor: Optional[str] = None,
    limit: int = 100,
):
    """Query facts from the knowledge base."""
    kb = KnowledgeBase(data_dir=_data_dir())
    facts = kb.query(category=category, jurisdiction=jurisdiction, corridor=corridor, limit=limit)
    return {"status": "success", "facts": facts, "count": len(facts)}


@router.post("/knowledge-base/rebuild")
async def kb_rebuild():
    """Rebuild the knowledge base from all extractions."""
    kb = KnowledgeBase(data_dir=_data_dir())
    counts = kb.rebuild()
    return {"status": "success", "message": "Knowledge base rebuilt", "counts": counts}
