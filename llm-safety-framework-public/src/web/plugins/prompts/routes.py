"""
Prompt management routes.

Handles prompt sets, import, CRUD, preparation settings, and template library.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx


router = APIRouter()


# =============================================================================
# Request Models
# =============================================================================

class PromptCreate(BaseModel):
    prompt: str
    category: str
    subcategory: Optional[str] = None
    corridor: str = "general"
    ilo_indicators: List[str] = Field(default_factory=list)
    attack_type: str = "custom"
    difficulty: str = "medium"
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PromptUpdate(BaseModel):
    prompt: Optional[str] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
    corridor: Optional[str] = None
    ilo_indicators: Optional[List[str]] = None
    attack_type: Optional[str] = None
    difficulty: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class PreparationConfig(BaseModel):
    min_word_count: int = 5
    max_word_count: int = 500
    required_words: List[str] = Field(default_factory=list)
    avoid_words: List[str] = Field(default_factory=list)
    filter_duplicates: bool = True
    dedup_threshold: float = 0.95


class ForkRequest(BaseModel):
    template_ids: List[str]
    target_set: Optional[str] = None
    new_set_name: Optional[str] = None


# =============================================================================
# Prompt Sets
# =============================================================================

@router.get("/sets")
async def list_prompt_sets(ctx: AppContext = Depends(get_ctx)):
    prompts_file = Path(ctx.settings.data_dir) / "sample_test_prompts.json"
    pipeline_dir = Path(ctx.settings.pipeline_dir) / "prompt_sets"

    sets = []

    if prompts_file.exists():
        with open(prompts_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for suite_name, suite_prompts in data.get("test_suites", {}).items():
            sets.append({
                "id": suite_name,
                "name": suite_name.replace("_", " ").title(),
                "source": "default",
                "count": len(suite_prompts),
                "enabled": True,
            })

    if pipeline_dir.exists():
        for f in pipeline_dir.glob("*.json"):
            try:
                with open(f, 'r', encoding='utf-8') as fh:
                    data = json.load(fh)
                count = len(data) if isinstance(data, list) else len(data.get("prompts", []))
                sets.append({
                    "id": f.stem,
                    "name": f.stem.replace("_", " ").title(),
                    "source": "imported",
                    "count": count,
                    "enabled": True,
                })
            except Exception:
                continue

    return {"status": "success", "sets": sets}


@router.put("/sets/{set_id}/toggle")
async def toggle_prompt_set(set_id: str, enabled: bool = True, ctx: AppContext = Depends(get_ctx)):
    config_file = Path(ctx.settings.pipeline_dir) / "pipeline_config.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)

    config = {}
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)

    disabled = config.setdefault("disabled_sets", [])
    if enabled and set_id in disabled:
        disabled.remove(set_id)
    elif not enabled and set_id not in disabled:
        disabled.append(set_id)

    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)

    return {"status": "success", "set_id": set_id, "enabled": enabled}


# =============================================================================
# Prompt CRUD
# =============================================================================

@router.get("")
async def list_prompts(
    category: Optional[str] = None,
    corridor: Optional[str] = None,
    difficulty: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
    ctx: AppContext = Depends(get_ctx),
):
    prompts_file = Path(ctx.settings.data_dir) / "sample_test_prompts.json"

    if not prompts_file.exists():
        return {"status": "success", "prompts": [], "total": 0}

    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_prompts = []
    for suite_name, suite_prompts in data.get("test_suites", {}).items():
        for prompt in suite_prompts:
            prompt["suite"] = suite_name
            all_prompts.append(prompt)

    if category:
        all_prompts = [p for p in all_prompts if p.get("category") == category or p.get("suite") == category]
    if corridor:
        all_prompts = [p for p in all_prompts if p.get("corridor") == corridor]
    if difficulty:
        all_prompts = [p for p in all_prompts if p.get("difficulty") == difficulty]

    total = len(all_prompts)
    return {"status": "success", "prompts": all_prompts[offset:offset + limit], "total": total}


# =============================================================================
# Categories & Reference Data (must be before /{prompt_id})
# =============================================================================

@router.get("/categories")
async def get_categories():
    categories = [
        {"id": "regulatory_evasion", "name": "Regulatory Evasion", "description": "Fee manipulation, license fraud"},
        {"id": "debt_bondage", "name": "Debt Bondage", "description": "Loan traps, salary deductions"},
        {"id": "document_control", "name": "Document Control", "description": "Passport retention, ID confiscation"},
        {"id": "coercion_manipulation", "name": "Coercion & Manipulation", "description": "Psychological tactics, threats"},
        {"id": "moral_religious_framing", "name": "Moral/Religious Framing", "description": "Cultural/religious exploitation"},
        {"id": "financial_obfuscation", "name": "Financial Obfuscation", "description": "Hidden fees, currency tricks"},
    ]
    return {"status": "success", "categories": categories}


@router.get("/corridors")
async def get_corridors():
    corridors = [
        {"code": "PH-SA", "route": "Philippines to Saudi Arabia", "sectors": "Domestic work"},
        {"code": "NP-QA", "route": "Nepal to Qatar", "sectors": "Construction"},
        {"code": "BD-MY", "route": "Bangladesh to Malaysia", "sectors": "Manufacturing"},
        {"code": "ID-SG", "route": "Indonesia to Singapore", "sectors": "Domestic work"},
        {"code": "ET-LB", "route": "Ethiopia to Lebanon", "sectors": "Domestic work"},
        {"code": "MM-TH", "route": "Myanmar to Thailand", "sectors": "Fishing, agriculture"},
        {"code": "IN-AE", "route": "India to UAE", "sectors": "Construction"},
        {"code": "PK-SA", "route": "Pakistan to Saudi Arabia", "sectors": "Various"},
        {"code": "VN-TW", "route": "Vietnam to Taiwan", "sectors": "Manufacturing"},
        {"code": "KH-TH", "route": "Cambodia to Thailand", "sectors": "Fishing"},
    ]
    return {"status": "success", "corridors": corridors}


@router.get("/ilo-indicators")
async def get_ilo_indicators():
    indicators = [
        {"id": "abuse_of_vulnerability", "name": "Abuse of Vulnerability"},
        {"id": "deception", "name": "Deception"},
        {"id": "restriction_of_movement", "name": "Restriction of Movement"},
        {"id": "isolation", "name": "Isolation"},
        {"id": "physical_sexual_violence", "name": "Physical/Sexual Violence"},
        {"id": "intimidation_threats", "name": "Intimidation & Threats"},
        {"id": "retention_of_identity_documents", "name": "Retention of Documents"},
        {"id": "withholding_of_wages", "name": "Withholding Wages"},
        {"id": "debt_bondage", "name": "Debt Bondage"},
        {"id": "abusive_working_conditions", "name": "Abusive Conditions"},
        {"id": "excessive_overtime", "name": "Excessive Overtime"},
    ]
    return {"status": "success", "indicators": indicators}


# =============================================================================
# Prompt Template Library (must be before /{prompt_id} catch-all)
# =============================================================================

def _load_all_templates(ctx: AppContext):
    all_prompts = []
    prompts_file = Path(ctx.settings.data_dir) / "sample_test_prompts.json"
    if prompts_file.exists():
        with open(prompts_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for suite_name, suite_prompts in data.get("test_suites", {}).items():
            for idx, p in enumerate(suite_prompts):
                p.setdefault("suite", suite_name)
                p.setdefault("id", f"{suite_name}_{idx}")
                all_prompts.append(p)

    prompt_sets_dir = Path(ctx.settings.pipeline_dir) / "prompt_sets"
    if prompt_sets_dir.exists():
        for pf in prompt_sets_dir.glob("*.json"):
            try:
                with open(pf, 'r', encoding='utf-8') as f:
                    ps_data = json.load(f)
                for p in ps_data.get("prompts", []):
                    p.setdefault("suite", pf.stem)
                    all_prompts.append(p)
            except Exception:
                continue
    return all_prompts


@router.get("/templates")
async def browse_templates(
    category: Optional[str] = None,
    corridor: Optional[str] = None,
    ilo_indicator: Optional[str] = None,
    attack_type: Optional[str] = None,
    difficulty: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    ctx: AppContext = Depends(get_ctx),
):
    all_prompts = _load_all_templates(ctx)

    facets = {"categories": {}, "corridors": {}, "ilo_indicators": {}, "attack_types": {}, "difficulties": {}}
    for p in all_prompts:
        facets["categories"][p.get("category", "unknown")] = facets["categories"].get(p.get("category", "unknown"), 0) + 1
        facets["corridors"][p.get("corridor", "general")] = facets["corridors"].get(p.get("corridor", "general"), 0) + 1
        for ind in p.get("ilo_indicators", []):
            facets["ilo_indicators"][ind] = facets["ilo_indicators"].get(ind, 0) + 1
        facets["attack_types"][p.get("attack_type", "unknown")] = facets["attack_types"].get(p.get("attack_type", "unknown"), 0) + 1
        facets["difficulties"][p.get("difficulty", "medium")] = facets["difficulties"].get(p.get("difficulty", "medium"), 0) + 1

    filtered = all_prompts
    if category:
        filtered = [p for p in filtered if p.get("category") == category]
    if corridor:
        filtered = [p for p in filtered if p.get("corridor") == corridor]
    if ilo_indicator:
        filtered = [p for p in filtered if ilo_indicator in p.get("ilo_indicators", [])]
    if attack_type:
        filtered = [p for p in filtered if p.get("attack_type") == attack_type]
    if difficulty:
        filtered = [p for p in filtered if p.get("difficulty") == difficulty]
    if search:
        search_lower = search.lower()
        filtered = [p for p in filtered if search_lower in p.get("prompt", "").lower()]

    total = len(filtered)
    return {"status": "success", "total": total, "offset": offset, "limit": limit, "templates": filtered[offset:offset + limit], "facets": facets}


@router.post("/templates/fork")
async def fork_templates(request: ForkRequest, ctx: AppContext = Depends(get_ctx)):
    all_prompts = _load_all_templates(ctx)
    selected = [p for p in all_prompts if p.get("id") in request.template_ids]
    if not selected:
        raise HTTPException(status_code=404, detail="No matching templates found")

    prompt_sets_dir = Path(ctx.settings.pipeline_dir) / "prompt_sets"
    prompt_sets_dir.mkdir(parents=True, exist_ok=True)

    if request.target_set:
        target_file = prompt_sets_dir / f"{request.target_set}.json"
        if target_file.exists():
            with open(target_file, 'r', encoding='utf-8') as f:
                existing = json.load(f)
        else:
            existing = {"name": request.target_set, "prompts": []}
        existing["prompts"].extend(selected)
        save_data = existing
    else:
        set_name = request.new_set_name or f"forked_{uuid.uuid4().hex[:8]}"
        target_file = prompt_sets_dir / f"{set_name}.json"
        save_data = {"name": set_name, "prompts": selected, "created_at": datetime.now().isoformat()}

    with open(target_file, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, indent=2, ensure_ascii=False)

    return {"status": "success", "message": f"Forked {len(selected)} templates", "set_name": save_data.get("name", target_file.stem), "file": target_file.name, "count": len(selected)}


# =============================================================================
# Prompt Import (must be before /{prompt_id} catch-all)
# =============================================================================

@router.post("/import")
async def import_prompts(file: UploadFile = File(...), merge: bool = True, ctx: AppContext = Depends(get_ctx)):
    try:
        content = await file.read()
        imported = json.loads(content.decode('utf-8'))

        prompts_file = Path(ctx.settings.data_dir) / "sample_test_prompts.json"

        if merge and prompts_file.exists():
            with open(prompts_file, 'r', encoding='utf-8') as f:
                existing = json.load(f)
            for suite, prompts in imported.get("test_suites", {}).items():
                if suite not in existing["test_suites"]:
                    existing["test_suites"][suite] = []
                existing["test_suites"][suite].extend(prompts)
            existing["metadata"]["total_prompts"] = sum(
                len(s) for s in existing["test_suites"].values()
            )
            imported = existing

        with open(prompts_file, 'w', encoding='utf-8') as f:
            json.dump(imported, f, indent=2, ensure_ascii=False)

        total = sum(len(s) for s in imported.get("test_suites", {}).values())
        return {"status": "success", "message": f"Imported {total} prompts"}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================================
# Prompt Preparation Config (must be before /{prompt_id} catch-all)
# =============================================================================

@router.get("/preparation")
async def get_preparation_config(ctx: AppContext = Depends(get_ctx)):
    config_file = Path(ctx.settings.pipeline_dir) / "pipeline_config.json"

    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return {"status": "success", "preparation": config.get("preparation", {})}

    return {
        "status": "success",
        "preparation": PreparationConfig().model_dump(),
    }


@router.post("/preparation")
async def update_preparation_config(request: PreparationConfig, ctx: AppContext = Depends(get_ctx)):
    config_file = Path(ctx.settings.pipeline_dir) / "pipeline_config.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)

    config = {}
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)

    config["preparation"] = request.model_dump()

    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)

    return {"status": "success", "message": "Preparation config updated"}


# =============================================================================
# Single Prompt CRUD (catch-all must be last)
# =============================================================================

@router.get("/{prompt_id}")
async def get_prompt(prompt_id: str, ctx: AppContext = Depends(get_ctx)):
    prompts_file = Path(ctx.settings.data_dir) / "sample_test_prompts.json"

    if not prompts_file.exists():
        raise HTTPException(status_code=404, detail="Prompts file not found")

    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for suite_name, suite_prompts in data.get("test_suites", {}).items():
        for prompt in suite_prompts:
            if prompt.get("id") == prompt_id:
                prompt["suite"] = suite_name
                return {"status": "success", "prompt": prompt}

    raise HTTPException(status_code=404, detail=f"Prompt {prompt_id} not found")


@router.post("")
async def create_prompt(request: PromptCreate, ctx: AppContext = Depends(get_ctx)):
    prompts_file = Path(ctx.settings.data_dir) / "sample_test_prompts.json"

    if prompts_file.exists():
        with open(prompts_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"test_suites": {}, "metadata": {"version": "1.0.0", "total_prompts": 0}}

    category = request.category
    if category not in data["test_suites"]:
        data["test_suites"][category] = []

    existing_ids = [p.get("id", "") for p in data["test_suites"][category]]
    prefix = category[:2].upper()
    next_num = 1
    while f"{prefix}{next_num:03d}" in existing_ids:
        next_num += 1
    prompt_id = f"{prefix}{next_num:03d}"

    new_prompt = {
        "id": prompt_id,
        "prompt": request.prompt,
        "category": request.subcategory or category,
        "difficulty": request.difficulty,
        "corridor": request.corridor,
        "ilo_indicators": request.ilo_indicators,
        "attack_type": request.attack_type,
        "metadata": request.metadata,
    }

    data["test_suites"][category].append(new_prompt)
    data["metadata"]["total_prompts"] = sum(len(s) for s in data["test_suites"].values())

    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return {"status": "success", "prompt": new_prompt}


@router.put("/{prompt_id}")
async def update_prompt(prompt_id: str, request: PromptUpdate, ctx: AppContext = Depends(get_ctx)):
    prompts_file = Path(ctx.settings.data_dir) / "sample_test_prompts.json"

    if not prompts_file.exists():
        raise HTTPException(status_code=404, detail="Prompts file not found")

    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    found = False
    for suite_prompts in data.get("test_suites", {}).values():
        for prompt in suite_prompts:
            if prompt.get("id") == prompt_id:
                updates = {k: v for k, v in request.model_dump().items() if v is not None}
                prompt.update(updates)
                found = True
                break
        if found:
            break

    if not found:
        raise HTTPException(status_code=404, detail=f"Prompt {prompt_id} not found")

    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return {"status": "success", "message": f"Prompt {prompt_id} updated"}


@router.delete("/{prompt_id}")
async def delete_prompt(prompt_id: str, ctx: AppContext = Depends(get_ctx)):
    prompts_file = Path(ctx.settings.data_dir) / "sample_test_prompts.json"

    if not prompts_file.exists():
        raise HTTPException(status_code=404, detail="Prompts file not found")

    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    found = False
    for suite_prompts in data.get("test_suites", {}).values():
        for i, prompt in enumerate(suite_prompts):
            if prompt.get("id") == prompt_id:
                del suite_prompts[i]
                found = True
                break
        if found:
            break

    if not found:
        raise HTTPException(status_code=404, detail=f"Prompt {prompt_id} not found")

    data["metadata"]["total_prompts"] = sum(len(s) for s in data["test_suites"].values())

    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return {"status": "success", "message": f"Prompt {prompt_id} deleted"}
