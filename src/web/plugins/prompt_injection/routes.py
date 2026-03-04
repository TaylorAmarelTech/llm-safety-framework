"""
Prompt injection mutation API routes.

Browse mutators, apply single/pipeline/batch mutations,
and decode output-evasion results.
"""

import json
import logging
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx

logger = logging.getLogger(__name__)
router = APIRouter()


# ---------------------------------------------------------------------------
# Lazy helpers — import from src.prompt_injection on first call to avoid
# circular imports and allow the system to start even if seeds fail to load.
# ---------------------------------------------------------------------------

def _ensure_mutators_loaded():
    """Trigger registration of every mutator module (idempotent)."""
    from ....prompt_injection import _import_all_mutators
    try:
        _import_all_mutators()
    except ImportError:
        pass


def _registry() -> dict:
    """Return the raw mutator registry dict."""
    from ....prompt_injection import _MUTATOR_REGISTRY
    _ensure_mutators_loaded()
    return _MUTATOR_REGISTRY


def _get_mutator_instance(name: str):
    """Return a mutator instance, raising 404 if not found."""
    from ....prompt_injection import get_mutator
    _ensure_mutators_loaded()
    try:
        return get_mutator(name)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


def _get_pipeline(mutator_names: list[str], mode: str = "parallel"):
    """Build a MutationPipeline."""
    from ....prompt_injection import MutationPipeline
    _ensure_mutators_loaded()
    try:
        return MutationPipeline(mutator_names, mode=mode)
    except KeyError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


def _result_to_dict(r) -> dict[str, Any]:
    """Convert a MutationResult dataclass to a JSON-safe dict."""
    return r.to_dict()


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------

def _batch_dir(ctx: AppContext) -> Path:
    d = ctx.plugin_data_dir("prompt_injection") / "batch_results"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _save_batch(ctx: AppContext, batch_id: str, data: dict) -> None:
    path = _batch_dir(ctx) / f"{batch_id}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Request models
# ---------------------------------------------------------------------------

class MutateRequest(BaseModel):
    """Apply a single mutator to a prompt."""
    prompt: str
    mutator: str


class PipelineRequest(BaseModel):
    """Apply a pipeline of mutators."""
    prompt: str
    mutators: List[str]
    mode: str = "parallel"  # "parallel" or "sequential"


class BatchRequest(BaseModel):
    """Apply mutators to multiple prompts."""
    prompts: List[str]
    mutators: List[str]
    mode: str = "parallel"


class DecodeRequest(BaseModel):
    """Decode a mutated/encoded result."""
    text: str
    mutator: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


# ==========================================================================
# Mutator catalogue
# ==========================================================================

@router.get("/mutators")
async def list_mutators_route(
    category: Optional[str] = None,
    search: Optional[str] = None,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """List all registered mutators with metadata."""
    registry = _registry()
    items = []
    for name, cls in sorted(registry.items()):
        if category and cls.CATEGORY != category:
            continue
        if search and search.lower() not in (name + cls.DESCRIPTION).lower():
            continue
        items.append({
            "name": name,
            "category": cls.CATEGORY,
            "description": cls.DESCRIPTION,
            "requires_llm": cls.REQUIRES_LLM,
        })
    return JSONResponse(items)


@router.get("/mutators/{name}")
async def get_mutator_detail(
    name: str,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Get full details for a single mutator."""
    m = _get_mutator_instance(name)
    cls = type(m)
    return JSONResponse({
        "name": cls.NAME,
        "category": cls.CATEGORY,
        "description": cls.DESCRIPTION,
        "requires_llm": cls.REQUIRES_LLM,
        "class": cls.__name__,
        "module": cls.__module__,
    })


@router.get("/categories")
async def list_categories_route(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """List categories with mutator counts."""
    registry = _registry()
    counts: dict[str, int] = {}
    for cls in registry.values():
        counts[cls.CATEGORY] = counts.get(cls.CATEGORY, 0) + 1
    return JSONResponse(counts)


# ==========================================================================
# Mutation endpoints
# ==========================================================================

@router.post("/mutate")
async def mutate_single(
    req: MutateRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Apply a single mutator to a prompt."""
    m = _get_mutator_instance(req.mutator)
    try:
        results = m.mutate(req.prompt)
    except Exception as exc:
        logger.exception("Mutator %s failed", req.mutator)
        raise HTTPException(status_code=500, detail=f"Mutation failed: {exc}")
    return JSONResponse([_result_to_dict(r) for r in results])


@router.post("/pipeline")
async def run_pipeline(
    req: PipelineRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Apply a pipeline of mutators (parallel or sequential)."""
    if not req.mutators:
        raise HTTPException(status_code=400, detail="At least one mutator is required")
    if req.mode not in ("parallel", "sequential"):
        raise HTTPException(status_code=400, detail="Mode must be 'parallel' or 'sequential'")

    pipeline = _get_pipeline(req.mutators, mode=req.mode)
    try:
        results = pipeline.mutate(req.prompt)
    except Exception as exc:
        logger.exception("Pipeline failed")
        raise HTTPException(status_code=500, detail=f"Pipeline failed: {exc}")
    return JSONResponse([_result_to_dict(r) for r in results])


@router.post("/batch")
async def run_batch(
    req: BatchRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Apply mutators to multiple prompts."""
    if not req.prompts:
        raise HTTPException(status_code=400, detail="At least one prompt is required")
    if not req.mutators:
        raise HTTPException(status_code=400, detail="At least one mutator is required")
    if req.mode not in ("parallel", "sequential"):
        raise HTTPException(status_code=400, detail="Mode must be 'parallel' or 'sequential'")

    pipeline = _get_pipeline(req.mutators, mode=req.mode)
    all_results: list[list[dict]] = []
    total_mutations = 0

    try:
        for prompt in req.prompts:
            results = pipeline.mutate(prompt)
            dicts = [_result_to_dict(r) for r in results]
            all_results.append(dicts)
            total_mutations += len(dicts)
    except Exception as exc:
        logger.exception("Batch mutation failed")
        raise HTTPException(status_code=500, detail=f"Batch failed: {exc}")

    # Compute stats
    categories_hit: dict[str, int] = {}
    for prompt_results in all_results:
        for r in prompt_results:
            cat = r.get("technique_category", "unknown")
            categories_hit[cat] = categories_hit.get(cat, 0) + 1

    stats = {
        "prompts": len(req.prompts),
        "mutators": len(req.mutators),
        "mode": req.mode,
        "total_mutations": total_mutations,
        "categories_hit": categories_hit,
    }

    # Persist batch result
    batch_id = f"batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
    _save_batch(ctx, batch_id, {
        "id": batch_id,
        "created_at": datetime.now().isoformat(),
        "stats": stats,
        "results": all_results,
    })

    return JSONResponse({
        "batch_id": batch_id,
        "results": all_results,
        "stats": stats,
    })


# ==========================================================================
# Decode
# ==========================================================================

@router.post("/decode")
async def decode_result(
    req: DecodeRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Decode an output-evasion encoded result."""
    try:
        from ....prompt_injection.output_decoders import auto_decode
        decoded = auto_decode(req.text, req.metadata)
        method = req.metadata.get("decoder", "unknown")
        return JSONResponse({"decoded": decoded, "method": method})
    except ImportError:
        raise HTTPException(
            status_code=501,
            detail="Output decoders module not available",
        )
    except Exception as exc:
        logger.exception("Decode failed")
        raise HTTPException(status_code=500, detail=f"Decode failed: {exc}")


# ==========================================================================
# Stats
# ==========================================================================

@router.get("/stats")
async def framework_stats(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Return high-level statistics about the mutation framework."""
    registry = _registry()
    by_category: dict[str, int] = {}
    requires_llm_count = 0
    for cls in registry.values():
        by_category[cls.CATEGORY] = by_category.get(cls.CATEGORY, 0) + 1
        if cls.REQUIRES_LLM:
            requires_llm_count += 1

    # Count saved batch results
    batch_count = 0
    batch_dir = ctx.plugin_data_dir("prompt_injection") / "batch_results"
    if batch_dir.exists():
        batch_count = len(list(batch_dir.glob("*.json")))

    return JSONResponse({
        "total_mutators": len(registry),
        "categories": by_category,
        "category_count": len(by_category),
        "requires_llm": requires_llm_count,
        "deterministic": len(registry) - requires_llm_count,
        "saved_batches": batch_count,
    })


# ==========================================================================
# Saved batch results
# ==========================================================================

@router.get("/batches")
async def list_batches(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """List all saved batch results."""
    batch_dir = ctx.plugin_data_dir("prompt_injection") / "batch_results"
    if not batch_dir.exists():
        return JSONResponse([])

    batches = []
    for f in sorted(batch_dir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            batches.append({
                "id": data.get("id", f.stem),
                "created_at": data.get("created_at", ""),
                "stats": data.get("stats", {}),
            })
        except Exception:
            continue
    return JSONResponse(batches)


@router.get("/batches/{batch_id}")
async def get_batch(
    batch_id: str,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Get a saved batch result."""
    batch_dir = ctx.plugin_data_dir("prompt_injection") / "batch_results"
    path = batch_dir / f"{batch_id}.json"
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"Batch {batch_id} not found")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(data)


@router.delete("/batches/{batch_id}")
async def delete_batch(
    batch_id: str,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Delete a saved batch result."""
    batch_dir = ctx.plugin_data_dir("prompt_injection") / "batch_results"
    path = batch_dir / f"{batch_id}.json"
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"Batch {batch_id} not found")
    path.unlink()
    return JSONResponse({"status": "deleted", "id": batch_id})
