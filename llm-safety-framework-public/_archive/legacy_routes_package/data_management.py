"""
Data management routes.

Import/export for prompts, conversations, config, graded responses.
"""

import json
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse

from ..config import ConfigManager, get_settings

router = APIRouter()
config_manager = ConfigManager()


# =============================================================================
# Import
# =============================================================================

@router.post("/import/conversations")
async def import_conversations(file: UploadFile = File(...), merge: bool = True):
    """Import conversations from a JSON file."""
    try:
        content = await file.read()
        data = json.loads(content.decode('utf-8'))

        conversations_file = Path("examples/sample_conversations.json")

        if merge and conversations_file.exists():
            with open(conversations_file, 'r', encoding='utf-8') as f:
                existing = json.load(f)

            existing_ids = {c["id"] for c in existing.get("conversations", [])}
            new_convs = [c for c in data.get("conversations", []) if c["id"] not in existing_ids]
            existing["conversations"].extend(new_convs)
            data = existing

        conversations_file.parent.mkdir(parents=True, exist_ok=True)
        with open(conversations_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return {
            "status": "success",
            "message": f"Imported {len(data.get('conversations', []))} conversations",
        }
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/import/config")
async def import_config(file: UploadFile = File(...), merge: bool = True):
    """Import configuration from a JSON file."""
    try:
        content = await file.read()
        data = json.loads(content.decode('utf-8'))
        config_manager.import_config(data, merge=merge)
        return {"status": "success", "message": "Configuration imported"}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================================
# Export
# =============================================================================

@router.get("/export/prompts")
async def export_prompts(format: str = "json"):
    """Export all prompts."""
    settings = get_settings()
    prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"

    if not prompts_file.exists():
        raise HTTPException(status_code=404, detail="No prompts to export")

    if format == "json":
        return FileResponse(
            prompts_file,
            media_type="application/json",
            filename="exported_prompts.json",
        )
    raise HTTPException(status_code=400, detail=f"Unsupported format: {format}")


@router.get("/export/conversations")
async def export_conversations(format: str = "json", result_filter: Optional[str] = None):
    """Export conversations."""
    conversations_file = Path("examples/sample_conversations.json")

    if not conversations_file.exists():
        raise HTTPException(status_code=404, detail="No conversations to export")

    if format == "json":
        if result_filter:
            with open(conversations_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            data["conversations"] = [
                c for c in data.get("conversations", [])
                if c.get("result") == result_filter
            ]
            return JSONResponse(content=data)

        return FileResponse(
            conversations_file,
            media_type="application/json",
            filename="exported_conversations.json",
        )
    raise HTTPException(status_code=400, detail=f"Unsupported format: {format}")


@router.get("/export/config")
async def export_config(include_keys: bool = False):
    """Export configuration."""
    config = config_manager.export_config(include_keys=include_keys)
    return JSONResponse(content=config)


@router.get("/export/results/{run_id}")
async def export_results(run_id: str, format: str = "json"):
    """Export results from a specific test run."""
    settings = get_settings()
    run_file = Path(settings.pipeline_dir) / "runs" / f"{run_id}.json"
    if not run_file.exists():
        raise HTTPException(status_code=404, detail=f"Test run {run_id} not found")
    return FileResponse(
        run_file,
        media_type="application/json",
        filename=f"test_run_{run_id}.json",
    )


@router.get("/export/graded-responses")
async def export_graded_responses():
    """Export all graded response examples."""
    graded_file = Path("data/graded_responses/example_graded_responses.json")

    if not graded_file.exists():
        raise HTTPException(status_code=404, detail="No graded responses available")

    return FileResponse(
        graded_file,
        media_type="application/json",
        filename="graded_responses.json",
    )


@router.get("/export/contrastive-pairs")
async def export_contrastive_pairs():
    """Export contrastive pairs for preference learning."""
    graded_file = Path("data/graded_responses/example_graded_responses.json")

    if not graded_file.exists():
        raise HTTPException(status_code=404, detail="No graded responses available")

    with open(graded_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pairs = []
    grades_order = ["worst", "bad", "neutral", "good", "best"]

    for example in data.get("examples", []):
        prompt = example.get("prompt_text", "")
        responses = example.get("responses", {})

        for i, grade1 in enumerate(grades_order):
            for grade2 in grades_order[i + 1:]:
                if grade1 in responses and grade2 in responses:
                    pairs.append({
                        "prompt": prompt,
                        "chosen": responses[grade2].get("response_text", ""),
                        "rejected": responses[grade1].get("response_text", ""),
                        "chosen_grade": grade2,
                        "rejected_grade": grade1,
                    })

    return JSONResponse(
        content={"status": "success", "pairs": pairs, "count": len(pairs)},
        headers={"Content-Disposition": "attachment; filename=contrastive_pairs.jsonl"},
    )


# =============================================================================
# Pipeline Export
# =============================================================================

@router.get("/export/pipeline")
async def export_pipeline():
    """Export the active spinning pipeline."""
    settings = get_settings()
    pipeline_file = Path(settings.pipeline_dir) / "active_pipeline.json"

    if not pipeline_file.exists():
        raise HTTPException(status_code=404, detail="No active pipeline")

    return FileResponse(
        pipeline_file,
        media_type="application/json",
        filename="pipeline_export.json",
    )
