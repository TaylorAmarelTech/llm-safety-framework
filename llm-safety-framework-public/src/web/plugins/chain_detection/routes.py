"""
Chain detection API routes.

Chain library, test execution, results, scoring, and analytics.
"""

import json
import logging
import re
import uuid
from pathlib import Path
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx
from ....chain_detection import (
    ChainRegistry,
    ChainTestEngine,
    ActivityChain,
    ActivityStep,
    PalermoElements,
    ChainTestSingleRequest,
    ChainTestBatchRequest,
    GRADE_LABELS,
    GRADE_DESCRIPTIONS,
)
from ....chain_detection.seeds import seed_stats

logger = logging.getLogger(__name__)
router = APIRouter()

_SAFE_ID = re.compile(r'^[\w.=-]+$')


def _validate_id(value: str, label: str = "ID") -> str:
    if not _SAFE_ID.match(value):
        raise HTTPException(status_code=400, detail=f"Invalid {label} format")
    return value


def _get_registry(ctx: AppContext) -> ChainRegistry:
    """Get or create the chain registry (singleton per app)."""
    if not hasattr(ctx, "_chain_registry"):
        data_dir = ctx.plugin_data_dir("chain_detection")
        registry = ChainRegistry(data_dir=data_dir)
        registry.load_seeds()
        object.__setattr__(ctx, "_chain_registry", registry)
    return ctx._chain_registry  # type: ignore[attr-defined]


def _get_engine(ctx: AppContext) -> ChainTestEngine:
    """Get or create the test engine (singleton per app)."""
    if not hasattr(ctx, "_chain_engine"):
        registry = _get_registry(ctx)
        data_dir = ctx.plugin_data_dir("chain_detection")
        engine = ChainTestEngine(registry=registry, data_dir=data_dir)
        object.__setattr__(ctx, "_chain_engine", engine)
    return ctx._chain_engine  # type: ignore[attr-defined]


# =============================================================================
# Chain Library Routes
# =============================================================================

@router.get("/chains")
async def list_chains(
    ctx: AppContext = Depends(get_ctx),
    category: Optional[str] = None,
    corridor: Optional[str] = None,
    difficulty: Optional[str] = None,
    search: Optional[str] = None,
) -> JSONResponse:
    """List all chains with optional filtering."""
    registry = _get_registry(ctx)
    chains = registry.filter(
        category=category,
        corridor=corridor,
        difficulty=difficulty,
        search=search,
    )
    return JSONResponse([
        {
            "id": c.id,
            "name": c.name,
            "category": c.category,
            "difficulty": c.difficulty,
            "corridors": c.corridors,
            "step_count": len(c.steps),
            "emergent_risk": c.emergent_risk,
        }
        for c in chains
    ])


@router.get("/chains/{chain_id}")
async def get_chain(
    chain_id: str,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Get full chain detail."""
    _validate_id(chain_id, "chain_id")
    registry = _get_registry(ctx)
    chain = registry.get(chain_id)
    if not chain:
        raise HTTPException(status_code=404, detail="Chain not found")
    return JSONResponse(chain.model_dump(mode="json"))


class CreateChainRequest(BaseModel):
    name: str
    category: str
    steps: list[dict]
    chain_context: str
    emergent_risk: str
    difficulty: str = "medium"
    source_references: list[str] = Field(default_factory=list)
    corridors: list[str] = Field(default_factory=list)
    palermo_elements: dict = Field(default_factory=dict)


@router.post("/chains")
async def create_chain(
    req: CreateChainRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Create a custom chain."""
    registry = _get_registry(ctx)
    chain_id = f"custom_{uuid.uuid4().hex[:8]}"

    # Parse steps
    steps = []
    for i, s in enumerate(req.steps):
        steps.append(ActivityStep(
            id=s.get("id", f"{chain_id}_s{i + 1}"),
            description=s["description"],
            legal_basis=s.get("legal_basis", ""),
            sector=s.get("sector"),
            corridor=s.get("corridor"),
            indicator_action_ids=s.get("indicator_action_ids", []),
            red_flag_context=s.get("red_flag_context", ""),
        ))

    chain = ActivityChain(
        id=chain_id,
        name=req.name,
        category=req.category,
        steps=steps,
        chain_context=req.chain_context,
        emergent_risk=req.emergent_risk,
        difficulty=req.difficulty,
        source_references=req.source_references,
        corridors=req.corridors,
        palermo_elements=PalermoElements(**req.palermo_elements) if req.palermo_elements else PalermoElements(),
    )

    registry.add(chain)
    return JSONResponse({"id": chain_id, "status": "created"}, status_code=201)


@router.put("/chains/{chain_id}")
async def update_chain(
    chain_id: str,
    req: CreateChainRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Update an existing chain."""
    _validate_id(chain_id, "chain_id")
    registry = _get_registry(ctx)
    existing = registry.get(chain_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Chain not found")

    steps = []
    for i, s in enumerate(req.steps):
        steps.append(ActivityStep(
            id=s.get("id", f"{chain_id}_s{i + 1}"),
            description=s["description"],
            legal_basis=s.get("legal_basis", ""),
            sector=s.get("sector"),
            corridor=s.get("corridor"),
            indicator_action_ids=s.get("indicator_action_ids", []),
            red_flag_context=s.get("red_flag_context", ""),
        ))

    chain = ActivityChain(
        id=chain_id,
        name=req.name,
        category=req.category,
        steps=steps,
        chain_context=req.chain_context,
        emergent_risk=req.emergent_risk,
        difficulty=req.difficulty,
        source_references=req.source_references,
        corridors=req.corridors,
        palermo_elements=PalermoElements(**req.palermo_elements) if req.palermo_elements else PalermoElements(),
    )

    registry.add(chain)
    return JSONResponse({"id": chain_id, "status": "updated"})


@router.delete("/chains/{chain_id}")
async def delete_chain(
    chain_id: str,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Delete a chain."""
    _validate_id(chain_id, "chain_id")
    registry = _get_registry(ctx)
    if not registry.remove(chain_id):
        raise HTTPException(status_code=404, detail="Chain not found")
    return JSONResponse({"status": "deleted"})


@router.get("/categories")
async def list_categories(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """List chain categories with counts."""
    registry = _get_registry(ctx)
    return JSONResponse(registry.categories())


@router.get("/seeds/stats")
async def get_seed_stats(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Get seed chain statistics."""
    return JSONResponse(seed_stats())


# =============================================================================
# Test Execution Routes
# =============================================================================

class RunSingleRequest(BaseModel):
    chain_id: str
    test_mode: str = "direct"
    model_id: str
    endpoint_id: str
    use_judge: bool = False


@router.post("/tests/run")
async def run_single_test(
    req: RunSingleRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Run a single chain detection test."""
    engine = _get_engine(ctx)

    # Build API client from endpoint config
    endpoint = ctx.config_manager.get_endpoint(req.endpoint_id)
    if not endpoint:
        raise HTTPException(status_code=404, detail=f"Endpoint not found: {req.endpoint_id}")

    from ....api_client import UnifiedAPIClient
    client = UnifiedAPIClient(endpoint=endpoint, model_id=req.model_id)

    try:
        result = await engine.run_single(
            chain_id=req.chain_id,
            test_mode=req.test_mode,
            model_id=req.model_id,
            endpoint_id=req.endpoint_id,
            api_client=client,
            use_judge=req.use_judge,
        )
        return JSONResponse(result.model_dump(mode="json"))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


class RunBatchRequest(BaseModel):
    chain_ids: list[str] = Field(default_factory=list)
    test_modes: list[str] = Field(default_factory=lambda: ["direct"])
    model_id: str
    endpoint_id: str
    max_chains: int = 50
    use_judge: bool = False


@router.post("/tests/batch")
async def run_batch_test(
    req: RunBatchRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Run batch chain detection tests."""
    engine = _get_engine(ctx)

    endpoint = ctx.config_manager.get_endpoint(req.endpoint_id)
    if not endpoint:
        raise HTTPException(status_code=404, detail=f"Endpoint not found: {req.endpoint_id}")

    from ....api_client import UnifiedAPIClient
    client = UnifiedAPIClient(endpoint=endpoint, model_id=req.model_id)

    results = await engine.run_batch(
        chain_ids=req.chain_ids,
        test_modes=req.test_modes,
        model_id=req.model_id,
        endpoint_id=req.endpoint_id,
        api_client=client,
        max_chains=req.max_chains,
        use_judge=req.use_judge,
    )

    return JSONResponse({
        "total": len(results),
        "results": [r.model_dump(mode="json") for r in results],
    })


@router.get("/tests/results")
async def list_results(
    ctx: AppContext = Depends(get_ctx),
    chain_id: Optional[str] = None,
    model_id: Optional[str] = None,
    test_mode: Optional[str] = None,
    limit: int = Query(default=100, le=1000),
) -> JSONResponse:
    """List test results with optional filtering."""
    engine = _get_engine(ctx)
    results = engine.load_results(
        chain_id=chain_id,
        model_id=model_id,
        test_mode=test_mode,
        limit=limit,
    )
    return JSONResponse([
        {
            "id": r.id,
            "chain_id": r.test_case.chain_id,
            "test_mode": r.test_case.test_mode,
            "model_id": r.model_id,
            "grade": r.score.grade,
            "grade_label": r.score.grade_label,
            "chain_detected": r.score.chain_detected,
            "duration_ms": r.duration_ms,
            "timestamp": r.timestamp.isoformat(),
        }
        for r in results
    ])


@router.get("/tests/results/{result_id}")
async def get_result(
    result_id: str,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Get full result detail."""
    _validate_id(result_id, "result_id")
    engine = _get_engine(ctx)
    result = engine.get_result(result_id)
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")
    return JSONResponse(result.model_dump(mode="json"))


# =============================================================================
# Scoring Routes
# =============================================================================

@router.get("/scoring/rubric")
async def get_rubric() -> JSONResponse:
    """Get the 5-grade scoring rubric."""
    return JSONResponse({
        "grades": [
            {"grade": g, "label": GRADE_LABELS[g], "description": GRADE_DESCRIPTIONS[g]}
            for g in range(5)
        ]
    })


class RescoreRequest(BaseModel):
    result_id: str
    judge_endpoint_id: Optional[str] = None
    judge_model_id: Optional[str] = None


@router.post("/scoring/rescore")
async def rescore_result(
    req: RescoreRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Re-score a result using LLM judge."""
    engine = _get_engine(ctx)
    result = engine.get_result(req.result_id)
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")

    chain = _get_registry(ctx).get(result.test_case.chain_id)
    if not chain:
        raise HTTPException(status_code=404, detail="Chain not found for result")

    # Use specified judge or fall back to the original endpoint
    judge_eid = req.judge_endpoint_id or result.endpoint_id
    judge_mid = req.judge_model_id or result.model_id

    endpoint = ctx.config_manager.get_endpoint(judge_eid)
    if not endpoint:
        raise HTTPException(status_code=404, detail="Judge endpoint not found")

    from ....api_client import UnifiedAPIClient
    from ....chain_detection.scorer import (
        build_judge_prompt,
        parse_judge_response,
        score_hybrid,
        LLM_JUDGE_SYSTEM,
    )

    client = UnifiedAPIClient(endpoint=endpoint, model_id=judge_mid)
    judge_prompt = build_judge_prompt(chain, result.response)

    try:
        judge_response = await client.chat(
            messages=[{"role": "user", "content": judge_prompt}],
            system=LLM_JUDGE_SYSTEM,
        )
        judge_text = judge_response.get("content", str(judge_response)) if isinstance(judge_response, dict) else str(judge_response)
        judge_score = parse_judge_response(judge_text, chain)
        final_score = score_hybrid(result.response, chain, judge_score)

        return JSONResponse({
            "original_grade": result.score.grade,
            "new_grade": final_score.grade,
            "new_grade_label": final_score.grade_label,
            "score": final_score.model_dump(mode="json"),
        })
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Judge scoring failed: {exc}")


# =============================================================================
# Analytics Routes
# =============================================================================

@router.get("/analytics/summary")
async def analytics_summary(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Overall detection rate analytics."""
    engine = _get_engine(ctx)
    return JSONResponse(engine.analytics_summary())


@router.get("/analytics/by-category")
async def analytics_by_category(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Detection rates by chain category."""
    summary = _get_engine(ctx).analytics_summary()
    return JSONResponse(summary.get("by_category", {}))


@router.get("/analytics/by-mode")
async def analytics_by_mode(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Detection rates by test mode."""
    summary = _get_engine(ctx).analytics_summary()
    return JSONResponse(summary.get("by_mode", {}))


@router.get("/analytics/by-difficulty")
async def analytics_by_difficulty(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Detection rates by chain difficulty."""
    summary = _get_engine(ctx).analytics_summary()
    return JSONResponse(summary.get("by_difficulty", {}))


@router.get("/analytics/model-comparison")
async def analytics_model_comparison(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Cross-model comparison of detection rates."""
    summary = _get_engine(ctx).analytics_summary()
    return JSONResponse(summary.get("by_model", {}))
