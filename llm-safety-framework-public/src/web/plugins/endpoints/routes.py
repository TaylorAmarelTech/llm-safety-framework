"""
API Endpoints and Model management routes.

Endpoint-centric: configure API connections, then manage models per endpoint.
"""

import re
from typing import Dict, Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx

router = APIRouter()


# =============================================================================
# Request Models
# =============================================================================

class EndpointCreate(BaseModel):
    id: str
    name: str
    provider_type: str = "custom"
    base_url: str
    api_key: Optional[str] = None
    auth_header: str = "Authorization"
    auth_prefix: str = "Bearer"
    extra_headers: Dict[str, str] = Field(default_factory=dict)
    request_format: str = "openai"


class EndpointUpdate(BaseModel):
    name: Optional[str] = None
    base_url: Optional[str] = None
    api_key: Optional[str] = None
    enabled: Optional[bool] = None
    auth_header: Optional[str] = None
    auth_prefix: Optional[str] = None
    extra_headers: Optional[Dict[str, str]] = None
    request_format: Optional[str] = None


class ModelCreate(BaseModel):
    name: str
    model_id: str
    enabled: bool = False
    temperature: float = 0.7
    max_tokens: int = 2048
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    system_prompt: Optional[str] = None


class ModelUpdate(BaseModel):
    name: Optional[str] = None
    enabled: Optional[bool] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    system_prompt: Optional[str] = None


# =============================================================================
# Endpoint Routes
# =============================================================================

@router.get("")
async def list_endpoints(ctx: AppContext = Depends(get_ctx)):
    """Get all configured API endpoints."""
    endpoints = ctx.config_manager.get_all_endpoints()
    for ep in endpoints:
        if ep.get("api_key"):
            key = ep["api_key"]
            ep["api_key_masked"] = f"***{key[-4:]}" if len(key) > 4 else "***"
        else:
            ep["api_key_masked"] = None
        ep.pop("api_key", None)
        ep["model_count"] = len(ctx.config_manager.get_models_for_endpoint(ep["id"]))
        ep["enabled_model_count"] = len([
            m for m in ctx.config_manager.get_models_for_endpoint(ep["id"])
            if m.get("enabled")
        ])
    return {"status": "success", "endpoints": endpoints}


# Must be before /{endpoint_id} catch-all
@router.get("/all/enabled")
async def list_enabled_models(ctx: AppContext = Depends(get_ctx)):
    """Get all enabled models across all endpoints."""
    models = ctx.config_manager.get_enabled_models()
    result = []
    for m in models:
        clean = {k: v for k, v in m.items() if k != "_endpoint"}
        clean["endpoint_name"] = m.get("_endpoint", {}).get("name", "Unknown")
        result.append(clean)
    return {"status": "success", "models": result}


# Must be before /{endpoint_id} catch-all
@router.get("/models/enabled")
async def list_enabled_models_alt(ctx: AppContext = Depends(get_ctx)):
    """Alias for /all/enabled — used by multi-turn and other plugins."""
    models = ctx.config_manager.get_enabled_models()
    result = []
    for m in models:
        clean = {k: v for k, v in m.items() if k != "_endpoint"}
        clean["endpoint_name"] = m.get("_endpoint", {}).get("name", "Unknown")
        result.append(clean)
    return {"status": "success", "models": result}


@router.get("/{endpoint_id}")
async def get_endpoint(endpoint_id: str, ctx: AppContext = Depends(get_ctx)):
    """Get a specific endpoint with its models."""
    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Endpoint {endpoint_id} not found")

    result = {**ep}
    if result.get("api_key"):
        key = result["api_key"]
        result["api_key_masked"] = f"***{key[-4:]}" if len(key) > 4 else "***"
    else:
        result["api_key_masked"] = None
    result.pop("api_key", None)

    models = ctx.config_manager.get_models_for_endpoint(endpoint_id)
    return {"status": "success", "endpoint": result, "models": models}


@router.post("")
async def create_endpoint(request: EndpointCreate, ctx: AppContext = Depends(get_ctx)):
    """Create a new API endpoint."""
    eid = re.sub(r'[^a-zA-Z0-9_-]', '-', request.id.lower())
    existing = ctx.config_manager.get_endpoint(eid)
    if existing:
        raise HTTPException(status_code=409, detail=f"Endpoint {eid} already exists")

    endpoint = request.model_dump()
    endpoint["id"] = eid
    endpoint["enabled"] = True
    ctx.config_manager.create_endpoint(endpoint)
    return {"status": "success", "endpoint_id": eid}


@router.put("/{endpoint_id}")
async def update_endpoint(endpoint_id: str, request: EndpointUpdate, ctx: AppContext = Depends(get_ctx)):
    """Update an existing endpoint."""
    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Endpoint {endpoint_id} not found")

    updates = {k: v for k, v in request.model_dump().items() if v is not None}
    ctx.config_manager.update_endpoint(endpoint_id, updates)
    return {"status": "success", "message": f"Endpoint {endpoint_id} updated"}


class ApiKeyUpdate(BaseModel):
    api_key: str


@router.put("/{endpoint_id}/key")
async def update_endpoint_key(endpoint_id: str, body: ApiKeyUpdate, ctx: AppContext = Depends(get_ctx)):
    """Update the API key for an endpoint."""
    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Endpoint {endpoint_id} not found")

    ctx.config_manager.update_endpoint_key(endpoint_id, body.api_key)
    return {"status": "success", "message": f"API key updated for {endpoint_id}"}


@router.delete("/{endpoint_id}")
async def delete_endpoint(endpoint_id: str, ctx: AppContext = Depends(get_ctx)):
    """Delete an endpoint and all its models."""
    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Endpoint {endpoint_id} not found")

    ctx.config_manager.delete_endpoint(endpoint_id)
    return {"status": "success", "message": f"Endpoint {endpoint_id} deleted"}


@router.get("/{endpoint_id}/preview")
async def preview_api_call(endpoint_id: str, model_id: str = "example-model", ctx: AppContext = Depends(get_ctx)):
    """Preview how an API call will be structured for this endpoint."""
    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Endpoint {endpoint_id} not found")

    headers = {}
    if ep.get("auth_prefix"):
        headers[ep["auth_header"]] = f"{ep['auth_prefix']} <API_KEY>"
    else:
        headers[ep["auth_header"]] = "<API_KEY>"
    headers["Content-Type"] = "application/json"
    for k, v in ep.get("extra_headers", {}).items():
        headers[k] = v

    if ep.get("request_format") == "anthropic":
        url = f"{ep['base_url']}/v1/messages"
        body = {
            "model": model_id,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": "<prompt>"}],
        }
    else:
        url = f"{ep['base_url']}/chat/completions"
        body = {
            "model": model_id,
            "max_tokens": 1024,
            "temperature": 0.7,
            "messages": [{"role": "user", "content": "<prompt>"}],
        }

    return {
        "status": "success",
        "preview": {"method": "POST", "url": url, "headers": headers, "body": body},
    }


# =============================================================================
# Model Routes
# =============================================================================

@router.get("/{endpoint_id}/models")
async def list_models(endpoint_id: str, ctx: AppContext = Depends(get_ctx)):
    """Get all models for an endpoint."""
    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Endpoint {endpoint_id} not found")

    models = ctx.config_manager.get_models_for_endpoint(endpoint_id)
    return {"status": "success", "models": models}


@router.post("/{endpoint_id}/models")
async def create_model(endpoint_id: str, request: ModelCreate, ctx: AppContext = Depends(get_ctx)):
    """Add a model to an endpoint."""
    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Endpoint {endpoint_id} not found")

    model_full_id = f"{endpoint_id}/{request.model_id}"
    existing = ctx.config_manager.get_model(model_full_id)
    if existing:
        raise HTTPException(status_code=409, detail=f"Model {model_full_id} already exists")

    model = {
        "id": model_full_id,
        "endpoint_id": endpoint_id,
        **request.model_dump(),
    }
    ctx.config_manager.create_model(model)
    return {"status": "success", "model_id": model_full_id}


@router.put("/{endpoint_id}/models/{model_id:path}")
async def update_model(endpoint_id: str, model_id: str, request: ModelUpdate, ctx: AppContext = Depends(get_ctx)):
    """Update a model's configuration."""
    full_id = f"{endpoint_id}/{model_id}"
    m = ctx.config_manager.get_model(full_id)
    if not m:
        raise HTTPException(status_code=404, detail=f"Model {full_id} not found")

    updates = {k: v for k, v in request.model_dump().items() if v is not None}
    ctx.config_manager.update_model(full_id, updates)
    return {"status": "success", "message": f"Model {full_id} updated"}


@router.delete("/{endpoint_id}/models/{model_id:path}")
async def delete_model(endpoint_id: str, model_id: str, ctx: AppContext = Depends(get_ctx)):
    """Remove a model from an endpoint."""
    full_id = f"{endpoint_id}/{model_id}"
    m = ctx.config_manager.get_model(full_id)
    if not m:
        raise HTTPException(status_code=404, detail=f"Model {full_id} not found")

    ctx.config_manager.delete_model(full_id)
    return {"status": "success", "message": f"Model {full_id} deleted"}


@router.get("/{endpoint_id}/discover-models")
async def discover_models(endpoint_id: str, ctx: AppContext = Depends(get_ctx)):
    """Fetch available models from an endpoint (e.g., OpenRouter)."""
    import httpx

    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Endpoint {endpoint_id} not found")

    if not ep.get("api_key"):
        raise HTTPException(status_code=400, detail="API key required for model discovery")

    headers = {"Content-Type": "application/json"}
    if ep.get("auth_prefix"):
        headers[ep["auth_header"]] = f"{ep['auth_prefix']} {ep['api_key']}"
    else:
        headers[ep["auth_header"]] = ep["api_key"]
    for k, v in ep.get("extra_headers", {}).items():
        headers[k] = v

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(f"{ep['base_url']}/models", headers=headers)
            data = response.json()

        models = []
        for m in data.get("data", []):
            models.append({
                "id": m.get("id", ""),
                "name": m.get("name", m.get("id", "")),
                "context_length": m.get("context_length"),
                "pricing": m.get("pricing"),
            })

        return {"status": "success", "models": models, "count": len(models)}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch models: {str(e)}")
