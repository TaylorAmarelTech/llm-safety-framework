"""
Dimensional matrix API routes.

Dimension explorer, severity rating, boundary probing, calibration,
and multi-LLM debate evaluation.
"""

import json
import logging
import re
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx

logger = logging.getLogger(__name__)
router = APIRouter()

_SAFE_ID = re.compile(r"^[\w.=-]+$")


def _validate_id(value: str, label: str = "ID") -> str:
    if not _SAFE_ID.match(value):
        raise HTTPException(status_code=400, detail=f"Invalid {label} format")
    return value


def _resolve_endpoint(ctx: AppContext, endpoint_id: str) -> dict:
    """Resolve endpoint config from ConfigManager."""
    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(404, f"Endpoint not found: {endpoint_id}")
    return ep


# ---------------------------------------------------------------------------
# Request models
# ---------------------------------------------------------------------------


class RateRequest(BaseModel):
    prompt: str
    response: str
    endpoint_id: str
    model_id: str = ""
    categories: Optional[list[str]] = None


class CalibrateRequest(BaseModel):
    prompt: str
    response: str
    endpoint_id: str
    model_id: str = ""
    target_dim: str
    direction: str = "up"
    step: int = 1


class ProbeRequest(BaseModel):
    prompt: str
    endpoint_id: str
    model_id: str = ""
    judge_endpoint_id: Optional[str] = None
    judge_model_id: Optional[str] = None
    dimensions: Optional[list[str]] = None


class DebateRequest(BaseModel):
    prompt: str
    response: str
    prosecutor_endpoint_id: str
    prosecutor_model_id: str = ""
    defender_endpoint_id: str
    defender_model_id: str = ""
    judge_endpoint_id: str
    judge_model_id: str = ""
    rounds: int = Field(default=1, ge=1, le=5)
    dimension_ids: Optional[list[str]] = None


class ScoringSummaryRequest(BaseModel):
    prompt: str
    response: str
    scores: dict[str, int] = Field(
        description="Dimension ID to score (1-5) mapping"
    )


# ---------------------------------------------------------------------------
# Dimension routes (read-only, no LLM calls)
# ---------------------------------------------------------------------------


@router.get("/dimensions/categories")
async def list_categories() -> JSONResponse:
    """List dimension categories with counts."""
    from ....dimensional_matrix import DIMENSIONS_BY_CATEGORY, DimensionCategory

    result = {}
    for cat in DimensionCategory:
        dims = DIMENSIONS_BY_CATEGORY.get(cat, [])
        result[cat.value] = {
            "count": len(dims),
            "ids": [d.id for d in dims],
        }
    return JSONResponse(result)


@router.get("/dimensions")
async def list_dimensions(
    category: Optional[str] = Query(None, description="Filter by category"),
) -> JSONResponse:
    """List all 35 dimensions, optionally filtered by category."""
    from ....dimensional_matrix import (
        ALL_DIMENSIONS,
        DimensionCategory,
        get_dimensions,
    )

    if category:
        try:
            cat = DimensionCategory(category)
        except ValueError:
            raise HTTPException(400, f"Invalid category: {category}")
        dims = get_dimensions(cat)
    else:
        dims = ALL_DIMENSIONS

    return JSONResponse([
        {
            "id": d.id,
            "name": d.name,
            "category": d.category.value,
            "description": d.description,
            "ilo_indicator": d.ilo_indicator,
            "levels": {str(k): v for k, v in d.levels.items()},
        }
        for d in dims
    ])


@router.get("/dimensions/{dim_id}")
async def get_dimension_detail(dim_id: str) -> JSONResponse:
    """Get a single dimension with full rubric."""
    from ....dimensional_matrix import get_dimension

    _validate_id(dim_id, "dimension ID")
    try:
        dim = get_dimension(dim_id)
    except KeyError:
        raise HTTPException(404, f"Dimension not found: {dim_id}")

    return JSONResponse({
        "id": dim.id,
        "name": dim.name,
        "category": dim.category.value,
        "description": dim.description,
        "ilo_indicator": dim.ilo_indicator,
        "levels": {str(k): v for k, v in dim.levels.items()},
        "rubric_text": dim.rubric_text(),
    })


# ---------------------------------------------------------------------------
# Rating route
# ---------------------------------------------------------------------------


@router.post("/rate")
async def rate_response(
    req: RateRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Rate a prompt+response on specified dimensions."""
    from ....dimensional_matrix import DimensionalRater, DimensionCategory

    ep = _resolve_endpoint(ctx, req.endpoint_id)
    model_id = req.model_id or ep.get("default_model", "")
    if not model_id:
        raise HTTPException(400, "model_id required (or set default_model on endpoint)")

    categories = None
    if req.categories:
        try:
            categories = [DimensionCategory(c) for c in req.categories]
        except ValueError as e:
            raise HTTPException(400, f"Invalid category: {e}")

    rater = DimensionalRater(endpoint=ep, model_id=model_id)
    rating = await rater.rate(
        prompt=req.prompt,
        response=req.response,
        categories=categories,
        response_model_id=req.model_id,
    )

    return JSONResponse({
        "scores": [
            {
                "dimension_id": s.dimension_id,
                "score": s.score,
                "confidence": s.confidence,
                "justification": s.justification,
            }
            for s in rating.scores
        ],
        "overall_risk": rating.overall_risk,
        "risk_level": rating.risk_level.value,
        "categories_rated": rating.categories_rated,
        "score_count": len(rating.scores),
    })


# ---------------------------------------------------------------------------
# Calibration routes
# ---------------------------------------------------------------------------


@router.post("/calibrate/response")
async def calibrate_response(
    req: CalibrateRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Generate a calibrated response shifted along a dimension."""
    from ....dimensional_matrix import DimensionalCalibrator, get_dimension

    _validate_id(req.target_dim, "dimension ID")
    try:
        get_dimension(req.target_dim)
    except KeyError:
        raise HTTPException(400, f"Unknown dimension: {req.target_dim}")

    ep = _resolve_endpoint(ctx, req.endpoint_id)
    model_id = req.model_id or ep.get("default_model", "")

    calibrator = DimensionalCalibrator(endpoint=ep, model_id=model_id)
    result = await calibrator.calibrate_response(
        prompt=req.prompt,
        response=req.response,
        target_dimension=req.target_dim,
        direction=req.direction,
        step=req.step,
    )

    return JSONResponse({
        "target_dimension": result.target_dimension,
        "target_direction": result.target_direction,
        "original_level": result.original_level,
        "target_level": result.target_level,
        "generated_text": result.generated_text,
        "operation": result.operation,
    })


@router.post("/calibrate/question")
async def calibrate_question(
    req: CalibrateRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Generate a calibrated question shifted along a dimension."""
    from ....dimensional_matrix import DimensionalCalibrator, get_dimension

    _validate_id(req.target_dim, "dimension ID")
    try:
        get_dimension(req.target_dim)
    except KeyError:
        raise HTTPException(400, f"Unknown dimension: {req.target_dim}")

    ep = _resolve_endpoint(ctx, req.endpoint_id)
    model_id = req.model_id or ep.get("default_model", "")

    calibrator = DimensionalCalibrator(endpoint=ep, model_id=model_id)
    result = await calibrator.calibrate_question(
        prompt=req.prompt,
        response=req.response,
        target_dimension=req.target_dim,
        direction=req.direction,
        step=req.step,
    )

    return JSONResponse({
        "target_dimension": result.target_dimension,
        "target_direction": result.target_direction,
        "original_level": result.original_level,
        "target_level": result.target_level,
        "generated_text": result.generated_text,
        "operation": result.operation,
    })


# ---------------------------------------------------------------------------
# Boundary probing route
# ---------------------------------------------------------------------------


@router.post("/probe")
async def probe_boundary(
    req: ProbeRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Probe guardrail boundaries along specified dimensions."""
    from ....dimensional_matrix import BoundaryProber

    target_ep = _resolve_endpoint(ctx, req.endpoint_id)
    target_model = req.model_id or target_ep.get("default_model", "")

    judge_ep = target_ep
    judge_model = target_model
    if req.judge_endpoint_id:
        judge_ep = _resolve_endpoint(ctx, req.judge_endpoint_id)
        judge_model = req.judge_model_id or judge_ep.get("default_model", "")

    prober = BoundaryProber(
        target_endpoint=target_ep,
        target_model_id=target_model,
        judge_endpoint=judge_ep,
        judge_model_id=judge_model,
    )

    guardrail_map = await prober.probe_prompt(
        prompt=req.prompt,
        dimension_ids=req.dimensions,
    )

    return JSONResponse(guardrail_map.to_dict())


# ---------------------------------------------------------------------------
# Debate routes
# ---------------------------------------------------------------------------


@router.post("/debate")
async def run_debate(
    req: DebateRequest,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Run a multi-LLM debate evaluation."""
    from ....dimensional_matrix import DebateJudge, save_debate

    pros_ep = _resolve_endpoint(ctx, req.prosecutor_endpoint_id)
    def_ep = _resolve_endpoint(ctx, req.defender_endpoint_id)
    judge_ep = _resolve_endpoint(ctx, req.judge_endpoint_id)

    debate = DebateJudge(
        prosecutor={
            "endpoint": pros_ep,
            "model_id": req.prosecutor_model_id or pros_ep.get("default_model", ""),
        },
        defender={
            "endpoint": def_ep,
            "model_id": req.defender_model_id or def_ep.get("default_model", ""),
        },
        judge={
            "endpoint": judge_ep,
            "model_id": req.judge_model_id or judge_ep.get("default_model", ""),
        },
    )

    result = await debate.run(
        prompt=req.prompt,
        response=req.response,
        rounds=req.rounds,
        dimension_ids=req.dimension_ids,
    )

    # Save to disk
    data_dir = ctx.plugin_data_dir("dimensional_matrix")
    debates_dir = data_dir / "debates"
    save_path = save_debate(result, output_dir=str(debates_dir))

    verdict_data = None
    if result.verdict:
        verdict_data = {
            "winner": result.verdict.winner,
            "confidence": result.verdict.confidence,
            "safety_assessment": result.verdict.safety_assessment,
            "vulnerabilities": result.verdict.vulnerabilities,
            "strongest_prosecution_point": result.verdict.strongest_prosecution_point,
            "strongest_defense_point": result.verdict.strongest_defense_point,
            "judge_reasoning": result.verdict.judge_reasoning,
            "dimensional_flags": result.verdict.dimensional_flags,
            "recommendations": result.verdict.recommendations,
        }

    return JSONResponse({
        "verdict": verdict_data,
        "turns": [
            {
                "role": t.role,
                "model_id": t.model_id,
                "content": t.content,
                "turn_number": t.turn_number,
            }
            for t in result.turns
        ],
        "participants": result.participants,
        "num_rounds": result.num_rounds,
        "save_path": save_path,
    })


@router.get("/debate/results")
async def list_debate_results(
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """List saved debate results."""
    data_dir = ctx.plugin_data_dir("dimensional_matrix")
    debates_dir = data_dir / "debates"
    if not debates_dir.exists():
        return JSONResponse([])

    results = []
    for f in sorted(debates_dir.glob("debate_*.json"), reverse=True):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            verdict = data.get("verdict") or {}
            results.append({
                "filename": f.name,
                "prompt_preview": data.get("prompt", "")[:120],
                "safety_assessment": verdict.get("safety_assessment", ""),
                "winner": verdict.get("winner", ""),
                "confidence": verdict.get("confidence", 0),
                "participants": data.get("participants", {}),
                "timestamp": data.get("timestamp", ""),
            })
        except (json.JSONDecodeError, OSError):
            continue

    return JSONResponse(results)


@router.get("/debate/results/{filename}")
async def get_debate_result(
    filename: str,
    ctx: AppContext = Depends(get_ctx),
) -> JSONResponse:
    """Get a single debate result file."""
    _validate_id(filename.replace(".json", ""), "filename")
    data_dir = ctx.plugin_data_dir("dimensional_matrix")
    filepath = data_dir / "debates" / filename
    if not filepath.exists():
        raise HTTPException(404, f"Debate result not found: {filename}")

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    return JSONResponse(data)


# ---------------------------------------------------------------------------
# Scoring summary route
# ---------------------------------------------------------------------------


@router.post("/scoring/summary")
async def scoring_summary(req: ScoringSummaryRequest) -> JSONResponse:
    """Compute scoring summary from a dimension->score mapping."""
    from ....dimensional_matrix import DimensionalScore, ResponseRating
    from ....dimensional_matrix.scoring import (
        category_summary,
        rating_to_profile,
        top_risk_dimensions,
    )

    scores = []
    for dim_id, score_val in req.scores.items():
        clamped = max(1, min(5, score_val))
        scores.append(DimensionalScore(
            dimension_id=dim_id,
            score=clamped,
        ))

    rating = ResponseRating(
        prompt=req.prompt,
        response=req.response,
        scores=scores,
    )

    # Compute aggregates
    all_vals = [s.score for s in scores]
    if all_vals:
        avg = sum(all_vals) / len(all_vals)
        rating.overall_risk = round((avg - 1) / 4.0, 3)
        from ....dimensional_matrix.scoring import risk_level_from_avg
        rating.risk_level = risk_level_from_avg(avg)

    return JSONResponse({
        "category_summary": category_summary(rating),
        "top_risks": [
            {"dimension_id": s.dimension_id, "score": s.score}
            for s in top_risk_dimensions(rating, 5)
        ],
        "profile": rating_to_profile(rating),
        "overall_risk": rating.overall_risk,
        "risk_level": rating.risk_level.value,
    })
