"""
Research Hub API routes.

Unified search across Semantic Scholar, arXiv, GitHub, HuggingFace,
and OpenAlex.  Saved-result bookmarking and API adapter health checks.
"""

import json
import logging
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx
from ....integrations.research_apis import (
    ResearchAggregator,
    AggregatedResults,
    PaperResult,
    RepoResult,
    DatasetResult,
    ModelResult,
)

logger = logging.getLogger(__name__)
router = APIRouter()


# ---------------------------------------------------------------------------
# Singleton aggregator (lazy, per-app)
# ---------------------------------------------------------------------------

def _get_aggregator(ctx: AppContext) -> ResearchAggregator:
    """Return or create a singleton ResearchAggregator on the AppContext."""
    if not hasattr(ctx, "_research_aggregator"):
        aggregator = ResearchAggregator(timeout=30.0)
        object.__setattr__(ctx, "_research_aggregator", aggregator)
    return ctx._research_aggregator  # type: ignore[attr-defined]


def _saved_path(ctx: AppContext) -> Path:
    """Return the path to saved_results.json, creating the dir if needed."""
    data_dir = ctx.plugin_data_dir("research")
    return data_dir / "saved_results.json"


def _load_saved(ctx: AppContext) -> list[dict]:
    """Load saved results from disk."""
    path = _saved_path(ctx)
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            logger.warning("Could not read saved results file")
    return []


def _save_saved(ctx: AppContext, items: list[dict]) -> None:
    """Persist saved results to disk."""
    path = _saved_path(ctx)
    path.write_text(json.dumps(items, indent=2, default=str), encoding="utf-8")


# ---------------------------------------------------------------------------
# Request / response models
# ---------------------------------------------------------------------------

class SearchRequest(BaseModel):
    query: str
    apis: list[str] = Field(
        default_factory=lambda: [
            "semantic_scholar", "arxiv", "github", "huggingface", "openalex",
        ],
    )
    max_results: int = Field(default=10, ge=1, le=50)


class SaveRequest(BaseModel):
    type: str = Field(..., pattern="^(paper|repo|dataset|model)$")
    data: dict
    notes: str = ""


class SafetyPapersRequest(BaseModel):
    topic: str = "LLM safety"


class SafetyReposRequest(BaseModel):
    pass


class SafetyDatasetsRequest(BaseModel):
    pass


# ---------------------------------------------------------------------------
# Search routes
# ---------------------------------------------------------------------------

@router.post("/search")
async def search_all(
    req: SearchRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Unified search across all or selected research APIs."""
    agg = _get_aggregator(ctx)
    selected = set(req.apis)
    limit = req.max_results

    # Run only the requested adapters
    import asyncio

    papers: list[PaperResult] = []
    repos: list[RepoResult] = []
    datasets: list[DatasetResult] = []
    models: list[ModelResult] = []
    errors: dict[str, str] = {}

    tasks = {}
    if "semantic_scholar" in selected:
        tasks["semantic_scholar"] = agg.semantic_scholar.search(req.query, limit=limit)
    if "arxiv" in selected:
        tasks["arxiv"] = agg.arxiv.search(req.query, limit=limit)
    if "openalex" in selected:
        tasks["openalex"] = agg.openalex.search(req.query, limit=limit)
    if "github" in selected:
        tasks["github"] = agg.github.search_repos(req.query, limit=limit)
    if "huggingface" in selected:
        tasks["huggingface_datasets"] = agg.huggingface.search_datasets(req.query, limit=limit)
        tasks["huggingface_models"] = agg.huggingface.search_models(req.query, limit=limit)

    results = await asyncio.gather(*tasks.values(), return_exceptions=True)

    for label, result in zip(tasks.keys(), results):
        if isinstance(result, BaseException):
            errors[label] = str(result)
            continue
        if label in ("semantic_scholar", "arxiv", "openalex"):
            papers.extend(result)
        elif label == "github":
            repos.extend(result)
        elif label == "huggingface_datasets":
            datasets.extend(result)
        elif label == "huggingface_models":
            models.extend(result)

    return JSONResponse({
        "papers": [p.to_dict() for p in papers],
        "repos": [r.to_dict() for r in repos],
        "datasets": [d.to_dict() for d in datasets],
        "models": [m.to_dict() for m in models],
        "errors": errors,
    })


@router.get("/search/papers")
async def search_papers(
    q: str = Query(..., min_length=1),
    max_results: int = Query(default=10, ge=1, le=50),
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Search papers only (Semantic Scholar + arXiv + OpenAlex)."""
    import asyncio

    agg = _get_aggregator(ctx)
    results = await asyncio.gather(
        agg.semantic_scholar.search(q, limit=max_results),
        agg.arxiv.search(q, limit=max_results),
        agg.openalex.search(q, limit=max_results),
        return_exceptions=True,
    )

    papers: list[dict] = []
    errors: dict[str, str] = {}
    labels = ["semantic_scholar", "arxiv", "openalex"]
    for label, result in zip(labels, results):
        if isinstance(result, BaseException):
            errors[label] = str(result)
        else:
            papers.extend(p.to_dict() for p in result)

    return JSONResponse({"papers": papers, "errors": errors})


@router.get("/search/repos")
async def search_repos(
    q: str = Query(..., min_length=1),
    max_results: int = Query(default=10, ge=1, le=50),
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Search GitHub repositories."""
    agg = _get_aggregator(ctx)
    try:
        repos = await agg.github.search_repos(q, limit=max_results)
        return JSONResponse({"repos": [r.to_dict() for r in repos]})
    except Exception as exc:
        return JSONResponse({"repos": [], "errors": {"github": str(exc)}})


@router.get("/search/datasets")
async def search_datasets(
    q: str = Query(..., min_length=1),
    max_results: int = Query(default=10, ge=1, le=50),
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Search HuggingFace datasets."""
    agg = _get_aggregator(ctx)
    try:
        datasets = await agg.huggingface.search_datasets(q, limit=max_results)
        return JSONResponse({"datasets": [d.to_dict() for d in datasets]})
    except Exception as exc:
        return JSONResponse({"datasets": [], "errors": {"huggingface": str(exc)}})


@router.get("/search/models")
async def search_models(
    q: str = Query(..., min_length=1),
    max_results: int = Query(default=10, ge=1, le=50),
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Search HuggingFace models."""
    agg = _get_aggregator(ctx)
    try:
        models = await agg.huggingface.search_models(q, limit=max_results)
        return JSONResponse({"models": [m.to_dict() for m in models]})
    except Exception as exc:
        return JSONResponse({"models": [], "errors": {"huggingface": str(exc)}})


# ---------------------------------------------------------------------------
# Saved results routes
# ---------------------------------------------------------------------------

@router.post("/saved")
async def save_result(
    req: SaveRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Save a search result for later reference."""
    items = _load_saved(ctx)
    entry = {
        "id": uuid.uuid4().hex[:12],
        "type": req.type,
        "data": req.data,
        "notes": req.notes,
        "saved_at": datetime.now(timezone.utc).isoformat(),
    }
    items.append(entry)
    _save_saved(ctx, items)
    return JSONResponse({"id": entry["id"], "status": "saved"}, status_code=201)


@router.get("/saved")
async def list_saved(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """List all saved results."""
    items = _load_saved(ctx)
    return JSONResponse(items)


@router.delete("/saved/{item_id}")
async def delete_saved(
    item_id: str,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Remove a saved result by ID."""
    items = _load_saved(ctx)
    before = len(items)
    items = [i for i in items if i.get("id") != item_id]
    if len(items) == before:
        raise HTTPException(status_code=404, detail="Saved item not found")
    _save_saved(ctx, items)
    return JSONResponse({"status": "deleted"})


# ---------------------------------------------------------------------------
# Status route
# ---------------------------------------------------------------------------

@router.get("/status")
async def api_status(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Return adapter health / availability for each research API."""
    import asyncio
    import time

    agg = _get_aggregator(ctx)

    async def _check(name: str, coro) -> dict:
        start = time.monotonic()
        try:
            result = await coro
            elapsed = round((time.monotonic() - start) * 1000)
            count = len(result) if isinstance(result, list) else 0
            return {
                "name": name,
                "available": True,
                "latency_ms": elapsed,
                "sample_count": count,
            }
        except Exception as exc:
            elapsed = round((time.monotonic() - start) * 1000)
            return {
                "name": name,
                "available": False,
                "latency_ms": elapsed,
                "error": str(exc),
            }

    probe_query = "LLM safety"
    checks = await asyncio.gather(
        _check("Semantic Scholar", agg.semantic_scholar.search(probe_query, limit=1)),
        _check("arXiv", agg.arxiv.search(probe_query, limit=1)),
        _check("OpenAlex", agg.openalex.search(probe_query, limit=1)),
        _check("GitHub", agg.github.search_repos(probe_query, limit=1)),
        _check("HuggingFace Datasets", agg.huggingface.search_datasets(probe_query, limit=1)),
        _check("HuggingFace Models", agg.huggingface.search_models(probe_query, limit=1)),
    )

    return JSONResponse({
        "adapters": list(checks),
        "total": len(checks),
        "available": sum(1 for c in checks if c["available"]),
    })


# ---------------------------------------------------------------------------
# Suggestions route
# ---------------------------------------------------------------------------

_SUGGESTIONS = [
    {"query": "LLM red teaming jailbreak", "label": "Red Teaming & Jailbreaks"},
    {"query": "prompt injection attack defense", "label": "Prompt Injection"},
    {"query": "AI safety benchmark evaluation", "label": "Safety Benchmarks"},
    {"query": "human trafficking detection NLP", "label": "Trafficking Detection NLP"},
    {"query": "forced labor supply chain risk", "label": "Forced Labor & Supply Chain"},
    {"query": "toxicity detection language model", "label": "Toxicity Detection"},
    {"query": "adversarial robustness LLM", "label": "Adversarial Robustness"},
    {"query": "alignment RLHF large language model", "label": "Alignment & RLHF"},
    {"query": "guardrails content moderation AI", "label": "Guardrails & Moderation"},
    {"query": "migration labor exploitation dataset", "label": "Migration Exploitation Data"},
    {"query": "multilingual safety evaluation", "label": "Multilingual Safety"},
    {"query": "chain of thought safety reasoning", "label": "CoT Safety Reasoning"},
]


@router.get("/suggestions")
async def get_suggestions() -> JSONResponse:
    """Return pre-built search suggestions for LLM safety research topics."""
    return JSONResponse(_SUGGESTIONS)


# ---------------------------------------------------------------------------
# Safety shortcut routes
# ---------------------------------------------------------------------------

@router.post("/safety-papers")
async def safety_papers(
    req: SafetyPapersRequest = SafetyPapersRequest(),
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Shortcut: search for safety-related academic papers."""
    agg = _get_aggregator(ctx)
    papers = await agg.search_safety_papers(topic=req.topic)
    return JSONResponse({"papers": [p.to_dict() for p in papers]})


@router.post("/safety-repos")
async def safety_repos(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Shortcut: search for safety-related GitHub repositories."""
    agg = _get_aggregator(ctx)
    repos = await agg.search_safety_repos()
    return JSONResponse({"repos": [r.to_dict() for r in repos]})


@router.post("/safety-datasets")
async def safety_datasets(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Shortcut: search for safety-related HuggingFace datasets."""
    agg = _get_aggregator(ctx)
    datasets = await agg.search_safety_datasets()
    return JSONResponse({"datasets": [d.to_dict() for d in datasets]})
