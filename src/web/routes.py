"""
API Routes for LLM Safety Testing Framework Web Dashboard.

Provides endpoints for:
- Configuration management (API keys, models)
- Test execution and results
- Data import/export
- Prompt management
"""

import os
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

from fastapi import APIRouter, HTTPException, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field

from .config import ConfigManager, get_settings


router = APIRouter(tags=["LLM Safety Framework"])

# Initialize config manager
config_manager = ConfigManager()


# =============================================================================
# Request/Response Models
# =============================================================================

class APIKeyUpdate(BaseModel):
    """Request model for updating API keys."""
    provider: str
    api_key: str


class ModelConfigUpdate(BaseModel):
    """Request model for updating model configuration."""
    provider: str
    model_key: str
    enabled: Optional[bool] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    endpoint: Optional[str] = None


class CustomModelCreate(BaseModel):
    """Request model for adding a custom model."""
    name: str
    model_id: str
    endpoint: str
    api_key: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 2048


class MemoryUpdate(BaseModel):
    """Request model for updating memory/context."""
    system_context: Optional[str] = None
    custom_instructions: Optional[str] = None
    enabled: Optional[bool] = None


class TestRunRequest(BaseModel):
    """Request model for running tests."""
    prompt_ids: Optional[List[str]] = None
    categories: Optional[List[str]] = None
    corridors: Optional[List[str]] = None
    model_keys: Optional[List[str]] = None
    batch_size: int = 10
    include_variations: bool = False


class PromptCreate(BaseModel):
    """Request model for creating a new prompt."""
    prompt: str
    category: str
    subcategory: Optional[str] = None
    corridor: str = "general"
    ilo_indicators: List[str] = Field(default_factory=list)
    attack_type: str = "custom"
    difficulty: str = "medium"
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PromptUpdate(BaseModel):
    """Request model for updating a prompt."""
    prompt: Optional[str] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
    corridor: Optional[str] = None
    ilo_indicators: Optional[List[str]] = None
    attack_type: Optional[str] = None
    difficulty: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


# =============================================================================
# Configuration Endpoints
# =============================================================================

@router.get("/config")
async def get_configuration():
    """Get current configuration (API keys masked)."""
    config = config_manager.export_config(include_keys=False)
    return {"status": "success", "config": config}


@router.get("/config/models")
async def get_models():
    """Get all configured models."""
    models = config_manager.get_all_models()
    # Mask API keys
    for model in models:
        if model.get("api_key"):
            model["api_key"] = "***" + model["api_key"][-4:] if len(model["api_key"]) > 4 else "***"
    return {"status": "success", "models": models}


@router.get("/config/models/enabled")
async def get_enabled_models():
    """Get only enabled models."""
    models = config_manager.get_enabled_models()
    for model in models:
        if model.get("api_key"):
            model["api_key"] = "***" + model["api_key"][-4:]
    return {"status": "success", "models": models}


@router.post("/config/api-key")
async def update_api_key(request: APIKeyUpdate):
    """Update API key for a provider."""
    try:
        config_manager.update_api_key(request.provider, request.api_key)
        return {"status": "success", "message": f"API key updated for {request.provider}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/config/model")
async def update_model_config(request: ModelConfigUpdate):
    """Update configuration for a specific model."""
    updates = {}
    if request.enabled is not None:
        updates["enabled"] = request.enabled
    if request.temperature is not None:
        updates["temperature"] = request.temperature
    if request.max_tokens is not None:
        updates["max_tokens"] = request.max_tokens
    if request.endpoint is not None:
        updates["endpoint"] = request.endpoint

    try:
        config_manager.update_model_config(request.provider, request.model_key, updates)
        return {"status": "success", "message": "Model configuration updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/config/model/custom")
async def add_custom_model(request: CustomModelCreate):
    """Add a custom model endpoint."""
    try:
        config_manager.add_custom_model(request.model_dump())
        return {"status": "success", "message": f"Custom model '{request.name}' added"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/config/memory")
async def get_memory_context():
    """Get memory/context settings."""
    memory = config_manager.get_memory_context()
    return {"status": "success", "memory": memory}


@router.post("/config/memory")
async def update_memory_context(request: MemoryUpdate):
    """Update memory/context settings."""
    try:
        config_manager.update_memory_context(
            system_context=request.system_context,
            custom_instructions=request.custom_instructions,
            enabled=request.enabled
        )
        return {"status": "success", "message": "Memory context updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# =============================================================================
# Prompts Endpoints
# =============================================================================

@router.get("/prompts")
async def get_prompts(
    category: Optional[str] = None,
    corridor: Optional[str] = None,
    difficulty: Optional[str] = None,
    limit: int = 100,
    offset: int = 0
):
    """Get test prompts with optional filtering."""
    settings = get_settings()
    prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"

    if not prompts_file.exists():
        return {"status": "success", "prompts": [], "total": 0}

    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_prompts = []
    for suite_name, suite_prompts in data.get("test_suites", {}).items():
        for prompt in suite_prompts:
            prompt["suite"] = suite_name
            all_prompts.append(prompt)

    # Apply filters
    if category:
        all_prompts = [p for p in all_prompts if p.get("category") == category or p.get("suite") == category]
    if corridor:
        all_prompts = [p for p in all_prompts if p.get("corridor") == corridor]
    if difficulty:
        all_prompts = [p for p in all_prompts if p.get("difficulty") == difficulty]

    total = len(all_prompts)
    prompts = all_prompts[offset:offset + limit]

    return {"status": "success", "prompts": prompts, "total": total}


@router.get("/prompts/{prompt_id}")
async def get_prompt(prompt_id: str):
    """Get a specific prompt by ID."""
    settings = get_settings()
    prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"

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


@router.post("/prompts")
async def create_prompt(request: PromptCreate):
    """Create a new test prompt."""
    settings = get_settings()
    prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"

    # Load existing prompts
    if prompts_file.exists():
        with open(prompts_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"test_suites": {}, "metadata": {"version": "1.0.0", "total_prompts": 0}}

    # Generate ID
    category = request.category
    if category not in data["test_suites"]:
        data["test_suites"][category] = []

    # Find next ID
    existing_ids = [p.get("id", "") for p in data["test_suites"][category]]
    prefix = category[:2].upper()
    next_num = 1
    while f"{prefix}{next_num:03d}" in existing_ids:
        next_num += 1
    prompt_id = f"{prefix}{next_num:03d}"

    # Create prompt
    new_prompt = {
        "id": prompt_id,
        "prompt": request.prompt,
        "category": request.subcategory or category,
        "difficulty": request.difficulty,
        "corridor": request.corridor,
        "ilo_indicators": request.ilo_indicators,
        "attack_type": request.attack_type,
        "metadata": request.metadata
    }

    data["test_suites"][category].append(new_prompt)
    data["metadata"]["total_prompts"] = sum(len(s) for s in data["test_suites"].values())

    # Save
    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return {"status": "success", "prompt": new_prompt}


@router.put("/prompts/{prompt_id}")
async def update_prompt(prompt_id: str, request: PromptUpdate):
    """Update an existing prompt."""
    settings = get_settings()
    prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"

    if not prompts_file.exists():
        raise HTTPException(status_code=404, detail="Prompts file not found")

    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Find and update prompt
    found = False
    for suite_name, suite_prompts in data.get("test_suites", {}).items():
        for prompt in suite_prompts:
            if prompt.get("id") == prompt_id:
                if request.prompt is not None:
                    prompt["prompt"] = request.prompt
                if request.category is not None:
                    prompt["category"] = request.category
                if request.corridor is not None:
                    prompt["corridor"] = request.corridor
                if request.ilo_indicators is not None:
                    prompt["ilo_indicators"] = request.ilo_indicators
                if request.attack_type is not None:
                    prompt["attack_type"] = request.attack_type
                if request.difficulty is not None:
                    prompt["difficulty"] = request.difficulty
                if request.metadata is not None:
                    prompt["metadata"] = request.metadata
                found = True
                break
        if found:
            break

    if not found:
        raise HTTPException(status_code=404, detail=f"Prompt {prompt_id} not found")

    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return {"status": "success", "message": f"Prompt {prompt_id} updated"}


@router.delete("/prompts/{prompt_id}")
async def delete_prompt(prompt_id: str):
    """Delete a prompt."""
    settings = get_settings()
    prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"

    if not prompts_file.exists():
        raise HTTPException(status_code=404, detail="Prompts file not found")

    with open(prompts_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Find and delete prompt
    found = False
    for suite_name, suite_prompts in data.get("test_suites", {}).items():
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


# =============================================================================
# Conversations Endpoints
# =============================================================================

@router.get("/conversations")
async def get_conversations(
    category: Optional[str] = None,
    corridor: Optional[str] = None,
    result: Optional[str] = None,
    model: Optional[str] = None,
    limit: int = 50,
    offset: int = 0
):
    """Get test conversations with optional filtering."""
    conversations_file = Path("examples/sample_conversations.json")

    if not conversations_file.exists():
        return {"status": "success", "conversations": [], "total": 0}

    with open(conversations_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    conversations = data.get("conversations", [])

    # Apply filters
    if category:
        conversations = [c for c in conversations if c.get("category") == category]
    if corridor:
        conversations = [c for c in conversations if c.get("corridor") == corridor]
    if result:
        conversations = [c for c in conversations if c.get("result") == result]
    if model:
        conversations = [c for c in conversations if c.get("model_tested") == model]

    total = len(conversations)
    conversations = conversations[offset:offset + limit]

    return {"status": "success", "conversations": conversations, "total": total}


@router.get("/conversations/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get a specific conversation by ID."""
    conversations_file = Path("examples/sample_conversations.json")

    if not conversations_file.exists():
        raise HTTPException(status_code=404, detail="Conversations file not found")

    with open(conversations_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for conv in data.get("conversations", []):
        if conv.get("id") == conversation_id:
            return {"status": "success", "conversation": conv}

    raise HTTPException(status_code=404, detail=f"Conversation {conversation_id} not found")


# =============================================================================
# Test Execution Endpoints
# =============================================================================

@router.post("/tests/run")
async def run_tests(request: TestRunRequest, background_tasks: BackgroundTasks):
    """Start a test run against enabled models."""
    enabled_models = config_manager.get_enabled_models()

    if not enabled_models:
        raise HTTPException(status_code=400, detail="No models enabled. Configure API keys first.")

    # Generate run ID
    run_id = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"

    # TODO: Implement actual test execution in background
    # background_tasks.add_task(execute_test_run, run_id, request, enabled_models)

    return {
        "status": "success",
        "message": "Test run started",
        "run_id": run_id,
        "models": [m["name"] for m in enabled_models]
    }


@router.get("/tests/runs")
async def get_test_runs():
    """Get list of test runs."""
    # TODO: Implement test run history
    return {"status": "success", "runs": []}


@router.get("/tests/runs/{run_id}")
async def get_test_run(run_id: str):
    """Get details of a specific test run."""
    # TODO: Implement test run details
    raise HTTPException(status_code=404, detail=f"Test run {run_id} not found")


# =============================================================================
# Import/Export Endpoints
# =============================================================================

@router.post("/import/prompts")
async def import_prompts(file: UploadFile = File(...), merge: bool = True):
    """Import prompts from a JSON file."""
    try:
        content = await file.read()
        data = json.loads(content.decode('utf-8'))

        settings = get_settings()
        prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"

        if merge and prompts_file.exists():
            with open(prompts_file, 'r', encoding='utf-8') as f:
                existing = json.load(f)

            # Merge test suites
            for suite, prompts in data.get("test_suites", {}).items():
                if suite not in existing["test_suites"]:
                    existing["test_suites"][suite] = []
                existing["test_suites"][suite].extend(prompts)

            existing["metadata"]["total_prompts"] = sum(
                len(s) for s in existing["test_suites"].values()
            )
            data = existing

        with open(prompts_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        total = sum(len(s) for s in data.get("test_suites", {}).values())
        return {"status": "success", "message": f"Imported {total} prompts"}

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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

        with open(conversations_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return {"status": "success", "message": f"Imported {len(data.get('conversations', []))} conversations"}

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
            filename="exported_prompts.json"
        )
    else:
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

            # Return filtered data
            return JSONResponse(content=data)

        return FileResponse(
            conversations_file,
            media_type="application/json",
            filename="exported_conversations.json"
        )
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported format: {format}")


@router.get("/export/results/{run_id}")
async def export_results(run_id: str, format: str = "json"):
    """Export results from a specific test run."""
    # TODO: Implement test results export
    raise HTTPException(status_code=404, detail=f"Test run {run_id} not found")


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


@router.get("/export/config")
async def export_config(include_keys: bool = False):
    """Export configuration."""
    config = config_manager.export_config(include_keys=include_keys)
    return JSONResponse(content=config)


# =============================================================================
# Statistics Endpoints
# =============================================================================

@router.get("/stats")
async def get_statistics():
    """Get overall statistics."""
    settings = get_settings()
    prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"
    conversations_file = Path("examples/sample_conversations.json")

    stats = {
        "prompts": {"total": 0, "by_category": {}, "by_corridor": {}},
        "conversations": {"total": 0, "safe": 0, "harmful": 0, "by_model": {}},
        "models": {"configured": 0, "enabled": 0}
    }

    # Count prompts
    if prompts_file.exists():
        with open(prompts_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for suite, prompts in data.get("test_suites", {}).items():
            stats["prompts"]["total"] += len(prompts)
            stats["prompts"]["by_category"][suite] = len(prompts)
            for p in prompts:
                corridor = p.get("corridor", "unknown")
                stats["prompts"]["by_corridor"][corridor] = stats["prompts"]["by_corridor"].get(corridor, 0) + 1

    # Count conversations
    if conversations_file.exists():
        with open(conversations_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for conv in data.get("conversations", []):
            stats["conversations"]["total"] += 1
            if conv.get("result") == "SAFE":
                stats["conversations"]["safe"] += 1
            elif conv.get("result") == "HARMFUL":
                stats["conversations"]["harmful"] += 1
            model = conv.get("model_tested", "unknown")
            stats["conversations"]["by_model"][model] = stats["conversations"]["by_model"].get(model, 0) + 1

    # Count models
    all_models = config_manager.get_all_models()
    enabled_models = config_manager.get_enabled_models()
    stats["models"]["configured"] = len(all_models)
    stats["models"]["enabled"] = len(enabled_models)

    return {"status": "success", "stats": stats}


@router.get("/stats/categories")
async def get_categories():
    """Get list of available categories."""
    categories = [
        {"id": "regulatory_evasion", "name": "Regulatory Evasion", "description": "Fee manipulation, license fraud"},
        {"id": "debt_bondage", "name": "Debt Bondage", "description": "Loan traps, salary deductions"},
        {"id": "document_control", "name": "Document Control", "description": "Passport retention, ID confiscation"},
        {"id": "coercion_manipulation", "name": "Coercion & Manipulation", "description": "Psychological tactics, threats"},
        {"id": "moral_religious_framing", "name": "Moral/Religious Framing", "description": "Cultural/religious exploitation"},
        {"id": "financial_obfuscation", "name": "Financial Obfuscation", "description": "Hidden fees, currency tricks"}
    ]
    return {"status": "success", "categories": categories}


@router.get("/stats/corridors")
async def get_corridors():
    """Get list of migration corridors."""
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
        {"code": "KH-TH", "route": "Cambodia to Thailand", "sectors": "Fishing"}
    ]
    return {"status": "success", "corridors": corridors}


@router.get("/stats/ilo-indicators")
async def get_ilo_indicators():
    """Get list of ILO forced labor indicators."""
    indicators = [
        {"id": "abuse_of_vulnerability", "name": "Abuse of Vulnerability", "description": "Exploiting migrants' lack of knowledge, language barriers, or irregular status"},
        {"id": "deception", "name": "Deception", "description": "False promises about work conditions, wages, or nature of work"},
        {"id": "restriction_of_movement", "name": "Restriction of Movement", "description": "Limiting workers' freedom to leave workplace or accommodation"},
        {"id": "isolation", "name": "Isolation", "description": "Preventing contact with family, authorities, or support networks"},
        {"id": "physical_sexual_violence", "name": "Physical/Sexual Violence", "description": "Use of violence or sexual abuse to control workers"},
        {"id": "intimidation_threats", "name": "Intimidation & Threats", "description": "Threats against worker or family, including deportation threats"},
        {"id": "retention_of_identity_documents", "name": "Retention of Documents", "description": "Confiscating passports or identity documents"},
        {"id": "withholding_of_wages", "name": "Withholding Wages", "description": "Non-payment, delayed payment, or excessive deductions"},
        {"id": "debt_bondage", "name": "Debt Bondage", "description": "Trapping workers through debt they cannot repay"},
        {"id": "abusive_working_conditions", "name": "Abusive Conditions", "description": "Dangerous, degrading, or exploitative work environments"},
        {"id": "excessive_overtime", "name": "Excessive Overtime", "description": "Forced work beyond legal limits without compensation"}
    ]
    return {"status": "success", "indicators": indicators}


# =============================================================================
# Health Check
# =============================================================================

@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
