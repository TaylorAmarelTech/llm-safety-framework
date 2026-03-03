"""
Attack library integration routes.

Expose garak, pyrit, and deepteam through a unified API.
Libraries are optional — detection happens at runtime.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..config import get_settings
from ...integrations.detector import detect_all
from ...integrations.garak_adapter import GarakAdapter
from ...integrations.pyrit_adapter import PyRITAdapter
from ...integrations.deepteam_adapter import DeepTeamAdapter

router = APIRouter()


# =============================================================================
# Request Models
# =============================================================================

class IntegrationExecuteRequest(BaseModel):
    method_id: str
    prompts: List[str]
    options: Dict[str, Any] = {}
    save_to_pipeline: bool = True


# =============================================================================
# Routes
# =============================================================================

@router.get("/status")
async def integration_status():
    """Check installation status of all supported libraries."""
    return {"status": "success", "libraries": detect_all()}


@router.get("/{library}/methods")
async def list_methods(library: str):
    """List available methods for a library."""
    if library == "garak":
        methods = GarakAdapter.list_probes()
        # If garak is not installed, return metadata about what would be available
        if not methods:
            methods = [
                {"id": "encoding", "name": "Encoding Probes", "description": "Test encoding-based attacks", "category": "encoding"},
                {"id": "dan", "name": "DAN Probes", "description": "Do Anything Now jailbreak probes", "category": "jailbreak"},
                {"id": "goodside", "name": "Goodside Probes", "description": "Riley Goodside style injections", "category": "injection"},
                {"id": "glitch", "name": "Glitch Token Probes", "description": "Glitch token exploits", "category": "token"},
                {"id": "continuation", "name": "Continuation Probes", "description": "Text continuation attacks", "category": "continuation"},
                {"id": "xss", "name": "XSS Probes", "description": "Cross-site scripting via LLM", "category": "injection"},
                {"id": "realtoxicity", "name": "RealToxicity Probes", "description": "RealToxicityPrompts benchmark", "category": "toxicity"},
                {"id": "malwaregen", "name": "Malware Gen Probes", "description": "Malware generation attempts", "category": "harmful"},
            ]
        return {"status": "success", "library": library, "methods": methods, "count": len(methods)}

    elif library == "pyrit":
        converters = PyRITAdapter.list_converters()
        return {"status": "success", "library": library, "methods": converters, "count": len(converters)}

    elif library == "deepteam":
        methods = DeepTeamAdapter.list_methods()
        return {"status": "success", "library": library, "methods": methods, "count": len(methods)}

    else:
        raise HTTPException(status_code=404, detail=f"Unknown library: {library}")


@router.post("/{library}/execute")
async def execute_method(library: str, request: IntegrationExecuteRequest):
    """Execute a method from an integration library."""
    results: Any = None

    if library == "garak":
        if not GarakAdapter.is_available():
            raise HTTPException(status_code=400, detail="garak is not installed. Run: pip install garak")
        results = GarakAdapter.run_probe(request.method_id, request.prompts, **request.options)

    elif library == "pyrit":
        if not PyRITAdapter.is_available():
            raise HTTPException(status_code=400, detail="pyrit is not installed. Run: pip install pyrit-core")
        results = await PyRITAdapter.convert(request.method_id, request.prompts, **request.options)

    elif library == "deepteam":
        if not DeepTeamAdapter.is_available():
            raise HTTPException(status_code=400, detail="deepteam is not installed. Run: pip install deepteam")
        results = DeepTeamAdapter.execute_scan(request.method_id, request.prompts, **request.options)

    else:
        raise HTTPException(status_code=404, detail=f"Unknown library: {library}")

    # Save to pipeline if requested
    if request.save_to_pipeline and results:
        settings = get_settings()
        integrations_dir = Path(settings.pipeline_dir) / "integrations"
        integrations_dir.mkdir(parents=True, exist_ok=True)

        from datetime import datetime
        import uuid
        filename = f"{library}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}.json"
        save_data = {
            "library": library,
            "method_id": request.method_id,
            "prompts": request.prompts,
            "results": results,
            "timestamp": datetime.now().isoformat(),
        }
        with open(integrations_dir / filename, "w", encoding="utf-8") as f:
            json.dump(save_data, f, indent=2, ensure_ascii=False)

    return {
        "status": "success",
        "library": library,
        "method_id": request.method_id,
        "results": results,
        "count": len(results) if isinstance(results, list) else 1,
    }
