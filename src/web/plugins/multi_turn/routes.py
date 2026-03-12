"""
Multi-turn conversation attack routes.

Endpoints for listing strategies, generating attack plans,
executing multi-turn attacks, and saving results.
"""

import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx
from ....spinning.multi_turn import MultiTurnOrchestrator
from ....api_client import UnifiedAPIClient

_SAFE_ID = re.compile(r'^[\w.=-]+$')

router = APIRouter()


class MultiTurnGenerateRequest(BaseModel):
    prompt: str
    strategy_id: str
    options: Dict[str, Any] = {}


class MultiTurnExecuteRequest(BaseModel):
    prompt: str
    strategy_id: str
    model_id: str
    options: Dict[str, Any] = {}
    save: bool = True


class MultiTurnBatchRequest(BaseModel):
    prompts: List[str]
    strategy_ids: List[str]
    model_ids: List[str]
    save: bool = True


@router.get("/strategies")
async def list_strategies():
    """List all available multi-turn attack strategies."""
    return {
        "status": "success",
        "strategies": MultiTurnOrchestrator.list_strategies(),
        "count": len(MultiTurnOrchestrator.STRATEGIES),
    }


@router.post("/generate")
async def generate_plan(request: MultiTurnGenerateRequest):
    """Generate a conversation plan without executing it."""
    try:
        plan = MultiTurnOrchestrator.generate_plan(
            prompt=request.prompt,
            strategy_id=request.strategy_id,
            **request.options,
        )
        return {"status": "success", **plan}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/execute")
async def execute_multi_turn(
    request: MultiTurnExecuteRequest,
    ctx: AppContext = Depends(get_ctx),
):
    """Execute a multi-turn attack against a model."""
    config = ctx.config_manager.export_config()

    ep_dict = config.get("endpoints", {})
    endpoint = None
    model = None
    for ep in ep_dict.values():
        for m in ep.get("models", {}).values():
            if m.get("model_id") == request.model_id or m.get("id") == request.model_id:
                endpoint = ep
                model = m
                break
        if endpoint:
            break

    if not endpoint or not model:
        raise HTTPException(status_code=404, detail=f"Model not found: {request.model_id}")

    try:
        result = await MultiTurnOrchestrator.execute(
            prompt=request.prompt,
            strategy_id=request.strategy_id,
            endpoint=endpoint,
            model_id=model["model_id"],
            model_name=model.get("name", model["model_id"]),
            **request.options,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if request.save:
        results_dir = Path(ctx.settings.pipeline_dir) / "multi_turn"
        results_dir.mkdir(parents=True, exist_ok=True)

        result_id = f"mt_{datetime.now(tz=timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        result["id"] = result_id
        result["timestamp"] = datetime.now(tz=timezone.utc).isoformat()

        with open(results_dir / f"{result_id}.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

    return {"status": "success", **result}


@router.post("/batch")
async def batch_execute(
    request: MultiTurnBatchRequest,
    ctx: AppContext = Depends(get_ctx),
):
    """Execute multi-turn attacks across multiple prompts x strategies x models."""
    config = ctx.config_manager.export_config()
    ep_dict = config.get("endpoints", {})

    model_lookup: Dict[str, tuple] = {}
    for ep in ep_dict.values():
        for m in ep.get("models", {}).values():
            model_lookup[m.get("model_id", "")] = (ep, m)
            model_lookup[m.get("id", "")] = (ep, m)

    results = []
    errors = []

    for prompt in request.prompts:
        for strategy_id in request.strategy_ids:
            for mid in request.model_ids:
                if mid not in model_lookup:
                    errors.append({"model_id": mid, "error": "Model not found"})
                    continue
                ep, model = model_lookup[mid]
                try:
                    result = await MultiTurnOrchestrator.execute(
                        prompt=prompt,
                        strategy_id=strategy_id,
                        endpoint=ep,
                        model_id=model["model_id"],
                        model_name=model.get("name", model["model_id"]),
                    )
                    results.append(result)
                except Exception as e:
                    errors.append({
                        "prompt": prompt[:50],
                        "strategy": strategy_id,
                        "model": mid,
                        "error": str(e),
                    })

    if request.save and results:
        results_dir = Path(ctx.settings.pipeline_dir) / "multi_turn"
        results_dir.mkdir(parents=True, exist_ok=True)

        batch_id = f"mt_batch_{datetime.now(tz=timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        batch_data = {
            "id": batch_id,
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
            "results": results,
            "errors": errors,
            "total": len(results),
        }
        with open(results_dir / f"{batch_id}.json", "w", encoding="utf-8") as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

    return {
        "status": "success",
        "total": len(results),
        "errors": errors,
        "results": results,
    }


@router.get("/results")
async def list_results(ctx: AppContext = Depends(get_ctx)):
    """List saved multi-turn attack results."""
    results_dir = Path(ctx.settings.pipeline_dir) / "multi_turn"

    if not results_dir.exists():
        return {"status": "success", "results": [], "count": 0}

    items = []
    for f in sorted(results_dir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            items.append({
                "id": data.get("id", f.stem),
                "timestamp": data.get("timestamp", ""),
                "strategy": data.get("strategy", data.get("results", [{}])[0].get("strategy", "") if data.get("results") else ""),
                "model": data.get("model", ""),
                "final_classification": data.get("final_classification", ""),
                "total_turns": data.get("total_turns", len(data.get("results", []))),
                "is_batch": "results" in data and isinstance(data["results"], list) and len(data.get("results", [])) > 1,
            })
        except Exception:
            continue

    return {"status": "success", "results": items, "count": len(items)}


@router.get("/results/{result_id}")
async def get_result(result_id: str, ctx: AppContext = Depends(get_ctx)):
    """Get full transcript for a multi-turn result."""
    if not _SAFE_ID.match(result_id):
        raise HTTPException(status_code=400, detail="Invalid result ID format")
    results_dir = Path(ctx.settings.pipeline_dir) / "multi_turn"
    result_file = results_dir / f"{result_id}.json"

    if not result_file.exists():
        raise HTTPException(status_code=404, detail=f"Result not found: {result_id}")

    with open(result_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    return {"status": "success", **data}
