"""
Wizard routes - streamlined test generation and execution.

Provides a simplified flow: describe domain -> generate prompts + graded
responses -> configure target model -> run tests -> see results.
"""

import asyncio
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..config import get_settings
from ...api_client import UnifiedAPIClient
from ...wizard.generator import WizardGenerator
from ...wizard.grader import WizardGrader
from ...wizard.runner import WizardRunner

router = APIRouter()

# In-memory job tracker (also persisted to disk)
_active_jobs: Dict[str, dict] = {}

# Default provider configs
PROVIDER_DEFAULTS = {
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "auth_header": "Authorization",
        "auth_prefix": "Bearer",
        "extra_headers": {},
        "request_format": "openai",
        "models": ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"],
    },
    "anthropic": {
        "base_url": "https://api.anthropic.com",
        "auth_header": "x-api-key",
        "auth_prefix": "",
        "extra_headers": {"anthropic-version": "2023-06-01"},
        "request_format": "anthropic",
        "models": ["claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001", "claude-3-haiku-20240307"],
    },
    "mistral": {
        "base_url": "https://api.mistral.ai/v1",
        "auth_header": "Authorization",
        "auth_prefix": "Bearer",
        "extra_headers": {},
        "request_format": "openai",
        "models": ["mistral-large-latest", "mistral-medium-latest", "mistral-small-latest"],
    },
}


# =============================================================================
# Request / Response Models
# =============================================================================

class WizardGenerateRequest(BaseModel):
    """Start prompt + graded response generation."""
    domain: str
    test_description: str
    acceptable_behavior: str
    unacceptable_behavior: str
    generator_provider: str = "openai"
    generator_base_url: Optional[str] = None
    generator_api_key: str
    generator_model: str
    generator_format: str = "openai"
    prompt_count: int = Field(default=30, ge=5, le=100)


class WizardLoadLibraryRequest(BaseModel):
    """Load prompts from a pre-built library into a new session."""
    library_id: str
    domain: str = ""
    test_description: str = ""
    acceptable_behavior: str = ""
    unacceptable_behavior: str = ""
    categories: Optional[List[str]] = None
    max_prompts: int = Field(default=50, ge=5, le=500)


class WizardUpdatePromptsRequest(BaseModel):
    """Update prompts in a session (edit, add, delete)."""
    session_id: str
    prompts: List[dict]


class WizardTestRequest(BaseModel):
    """Start test execution against a target model."""
    session_id: str
    target_provider: str = "openai"
    target_base_url: Optional[str] = None
    target_api_key: str
    target_model: str
    target_format: str = "openai"
    delay_seconds: float = Field(default=1.5, ge=0.5, le=10.0)


class WizardVerifyRequest(BaseModel):
    """Verify an API connection."""
    provider: str = "openai"
    base_url: Optional[str] = None
    api_key: str
    model: str
    request_format: str = "openai"


# =============================================================================
# Helpers
# =============================================================================

def _build_endpoint(provider: str, api_key: str, base_url: Optional[str] = None,
                     request_format: str = "openai") -> dict:
    """Build an endpoint config dict from provider + key."""
    api_key = api_key.strip()
    if provider in PROVIDER_DEFAULTS:
        defaults = PROVIDER_DEFAULTS[provider]
        return {
            "id": f"wizard-{provider}",
            "base_url": base_url or defaults["base_url"],
            "api_key": api_key,
            "auth_header": defaults["auth_header"],
            "auth_prefix": defaults["auth_prefix"],
            "extra_headers": defaults["extra_headers"],
            "request_format": request_format or defaults["request_format"],
        }
    return {
        "id": "wizard-custom",
        "base_url": base_url or "",
        "api_key": api_key,
        "auth_header": "Authorization",
        "auth_prefix": "Bearer",
        "extra_headers": {},
        "request_format": request_format,
    }


def _wizard_dir() -> Path:
    """Get/create the wizard data directory."""
    settings = get_settings()
    d = Path(settings.data_dir) / "wizard"
    d.mkdir(parents=True, exist_ok=True)
    (d / "sessions").mkdir(exist_ok=True)
    (d / "jobs").mkdir(exist_ok=True)
    return d


def _save_job(job_id: str, data: dict):
    """Save job progress to disk."""
    path = _wizard_dir() / "jobs" / f"{job_id}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    _active_jobs[job_id] = data


def _load_job(job_id: str) -> Optional[dict]:
    """Load job progress from memory or disk."""
    if job_id in _active_jobs:
        return _active_jobs[job_id]
    path = _wizard_dir() / "jobs" / f"{job_id}.json"
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def _save_session(session_id: str, data: dict):
    """Save a wizard session to disk."""
    path = _wizard_dir() / "sessions" / f"{session_id}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _load_session(session_id: str) -> Optional[dict]:
    """Load a wizard session from disk."""
    path = _wizard_dir() / "sessions" / f"{session_id}.json"
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


# =============================================================================
# Routes
# =============================================================================

def _scan_libraries() -> List[dict]:
    """Scan data/ for available prompt libraries."""
    settings = get_settings()
    data_dir = Path(settings.data_dir)
    libs = []

    # Check sample_test_prompts.json
    sample = data_dir / "sample_test_prompts.json"
    if sample.exists():
        try:
            with open(sample, "r", encoding="utf-8") as f:
                content = json.load(f)
            suites = content.get("test_suites", {})
            total = sum(len(v) for v in suites.values())
            cats = list(suites.keys())
            corridors = set()
            difficulties = set()
            for suite_prompts in suites.values():
                for p in suite_prompts:
                    if p.get("corridor"):
                        corridors.add(p["corridor"])
                    if p.get("difficulty"):
                        difficulties.add(p["difficulty"])
            libs.append({
                "id": "sample_test_prompts",
                "name": "Default Safety Test Prompts",
                "file": "sample_test_prompts.json",
                "total_prompts": total,
                "categories": cats,
                "corridors": sorted(corridors),
                "difficulties": sorted(difficulties),
                "description": f"{total} prompts across {len(cats)} categories",
            })
        except Exception:
            pass

    # Check for consolidated tests
    for pattern in ["*consolidated*.json", "*tests*.json", "*attacks*.json"]:
        for fp in sorted(data_dir.glob(pattern)):
            if fp.name == "sample_test_prompts.json":
                continue
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    content = json.load(f)
                # Detect format
                prompts_list = []
                if isinstance(content, list):
                    prompts_list = content
                elif isinstance(content, dict):
                    if "test_suites" in content:
                        for v in content["test_suites"].values():
                            prompts_list.extend(v)
                    elif "prompts" in content:
                        prompts_list = content["prompts"]
                    elif "tests" in content:
                        prompts_list = content["tests"]

                if not prompts_list:
                    continue

                cats = set()
                corridors = set()
                for p in prompts_list[:500]:  # Sample first 500
                    if isinstance(p, dict):
                        if p.get("category"):
                            cats.add(p["category"])
                        if p.get("corridor"):
                            corridors.add(p["corridor"])

                libs.append({
                    "id": fp.stem,
                    "name": fp.stem.replace("_", " ").title(),
                    "file": fp.name,
                    "total_prompts": len(prompts_list),
                    "categories": sorted(cats),
                    "corridors": sorted(corridors),
                    "difficulties": [],
                    "description": f"{len(prompts_list)} prompts from {fp.name}",
                })
            except Exception:
                continue

    # Check wizard sessions that have prompts (user-generated libraries)
    sessions_dir = _wizard_dir() / "sessions"
    if sessions_dir.exists():
        for fp in sorted(sessions_dir.glob("*.json"),
                         key=lambda x: x.stat().st_mtime, reverse=True):
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    sess = json.load(f)
                prompts = sess.get("prompts", [])
                if len(prompts) >= 5:
                    cats = set(p.get("category", "") for p in prompts)
                    libs.append({
                        "id": f"session:{fp.stem}",
                        "name": f"Session: {sess.get('domain', fp.stem)[:60]}",
                        "file": fp.name,
                        "total_prompts": len(prompts),
                        "categories": sorted(c for c in cats if c),
                        "corridors": [],
                        "difficulties": sorted(set(p.get("difficulty", "") for p in prompts) - {""}),
                        "description": f"{len(prompts)} prompts from previous session",
                        "source": "session",
                    })
            except Exception:
                continue

    return libs


def _load_library_prompts(library_id: str, categories: Optional[List[str]] = None,
                           max_prompts: int = 50) -> List[dict]:
    """Load prompts from a library file."""
    settings = get_settings()
    data_dir = Path(settings.data_dir)

    # Handle session libraries
    if library_id.startswith("session:"):
        session_id = library_id.split(":", 1)[1]
        sess = _load_session(session_id)
        if not sess:
            return []
        prompts = sess.get("prompts", [])
        if categories:
            prompts = [p for p in prompts if p.get("category") in categories]
        return prompts[:max_prompts]

    # Find the file
    target_file = None
    for fp in data_dir.glob("*.json"):
        if fp.stem == library_id:
            target_file = fp
            break

    if not target_file or not target_file.exists():
        return []

    with open(target_file, "r", encoding="utf-8") as f:
        content = json.load(f)

    # Extract prompts based on format
    prompts_list = []
    if isinstance(content, list):
        prompts_list = content
    elif isinstance(content, dict):
        if "test_suites" in content:
            if categories:
                for cat_name, cat_prompts in content["test_suites"].items():
                    if cat_name in categories:
                        prompts_list.extend(cat_prompts)
            else:
                for v in content["test_suites"].values():
                    prompts_list.extend(v)
        elif "prompts" in content:
            prompts_list = content["prompts"]
        elif "tests" in content:
            prompts_list = content["tests"]

    # Filter by category if needed and not already filtered
    if categories and "test_suites" not in (content if isinstance(content, dict) else {}):
        prompts_list = [p for p in prompts_list
                        if isinstance(p, dict) and p.get("category") in categories]

    # Normalize prompt format
    normalized = []
    for p in prompts_list:
        if not isinstance(p, dict) or "prompt" not in p:
            continue
        normalized.append({
            "prompt": str(p["prompt"]),
            "category": str(p.get("category", p.get("test_suite", "general"))),
            "difficulty": str(p.get("difficulty", "medium")),
            "attack_type": str(p.get("attack_type", "direct")),
        })

    return normalized[:max_prompts]


@router.get("/providers")
async def get_providers():
    """Get available provider presets with their default models."""
    providers = []
    for pid, defaults in PROVIDER_DEFAULTS.items():
        providers.append({
            "id": pid,
            "name": pid.title(),
            "base_url": defaults["base_url"],
            "request_format": defaults["request_format"],
            "models": defaults["models"],
        })
    providers.append({
        "id": "custom",
        "name": "Custom",
        "base_url": "",
        "request_format": "openai",
        "models": [],
    })
    return {"status": "success", "providers": providers}


@router.get("/libraries")
async def list_libraries():
    """List available pre-built prompt libraries."""
    libs = _scan_libraries()
    return {"status": "success", "libraries": libs}


@router.post("/load-library")
async def load_library(request: WizardLoadLibraryRequest):
    """Load prompts from a pre-built library into a new session."""
    prompts = _load_library_prompts(
        request.library_id,
        categories=request.categories,
        max_prompts=request.max_prompts,
    )
    if not prompts:
        raise HTTPException(status_code=404, detail="Library not found or empty")

    session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
    session = {
        "id": session_id,
        "domain": request.domain,
        "test_description": request.test_description,
        "acceptable_behavior": request.acceptable_behavior,
        "unacceptable_behavior": request.unacceptable_behavior,
        "prompt_count": len(prompts),
        "generator_model": "library",
        "generator_provider": "library",
        "library_source": request.library_id,
        "created_at": datetime.now().isoformat(),
        "prompts": prompts,
        "test_results": None,
    }
    _save_session(session_id, session)

    return {
        "status": "success",
        "session_id": session_id,
        "prompts_loaded": len(prompts),
        "prompts": prompts,
    }


@router.put("/sessions/{session_id}/prompts")
async def update_session_prompts(session_id: str, request: WizardUpdatePromptsRequest):
    """Update prompts in a session (after editing in the prompt editor)."""
    session = _load_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Normalize incoming prompts
    normalized = []
    for p in request.prompts:
        if not isinstance(p, dict) or not p.get("prompt", "").strip():
            continue
        normalized.append({
            "prompt": str(p["prompt"]).strip(),
            "category": str(p.get("category", "general")),
            "difficulty": str(p.get("difficulty", "medium")),
            "attack_type": str(p.get("attack_type", "direct")),
            # Preserve graded_responses if they exist
            **({"graded_responses": p["graded_responses"]} if "graded_responses" in p else {}),
        })

    session["prompts"] = normalized
    session["prompt_count"] = len(normalized)
    _save_session(session_id, session)

    return {
        "status": "success",
        "prompt_count": len(normalized),
        "message": f"Updated to {len(normalized)} prompts",
    }


@router.post("/verify")
async def verify_connection(request: WizardVerifyRequest):
    """Verify an API key works by making a minimal test call."""
    ep = _build_endpoint(request.provider, request.api_key,
                          request.base_url, request.request_format)
    client = UnifiedAPIClient(ep)
    try:
        response = await client.chat(
            model_id=request.model,
            messages=[{"role": "user", "content": "Say 'OK' and nothing else."}],
            temperature=0,
            max_tokens=10,
        )
        return {
            "status": "success",
            "message": f"Connected to {request.model}",
            "response": response.strip(),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Connection failed: {e}")


@router.post("/generate")
async def start_generation(request: WizardGenerateRequest):
    """Start prompt + graded response generation as a background job."""
    job_id = f"gen_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
    session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    job = {
        "id": job_id,
        "session_id": session_id,
        "status": "starting",
        "phase": "prompts",
        "progress": 0,
        "prompts_done": 0,
        "prompts_total": request.prompt_count,
        "grades_done": 0,
        "grades_total": request.prompt_count,
        "message": "Starting prompt generation...",
        "error": None,
        "created_at": datetime.now().isoformat(),
    }
    _save_job(job_id, job)

    # Save initial session
    session = {
        "id": session_id,
        "domain": request.domain,
        "test_description": request.test_description,
        "acceptable_behavior": request.acceptable_behavior,
        "unacceptable_behavior": request.unacceptable_behavior,
        "prompt_count": request.prompt_count,
        "generator_model": request.generator_model,
        "generator_provider": request.generator_provider,
        "created_at": datetime.now().isoformat(),
        "prompts": [],
        "test_results": None,
    }
    _save_session(session_id, session)

    # Launch background task
    asyncio.create_task(
        _run_generation(job_id, session_id, request)
    )

    return {
        "status": "success",
        "job_id": job_id,
        "session_id": session_id,
        "message": "Generation started",
    }


async def _run_generation(job_id: str, session_id: str, request: WizardGenerateRequest):
    """Background task: generate prompts then graded responses."""
    try:
        ep = _build_endpoint(
            request.generator_provider,
            request.generator_api_key,
            request.generator_base_url,
            request.generator_format,
        )
        client = UnifiedAPIClient(ep)

        # Phase 1: Generate prompts
        def on_prompt_progress(done, total):
            job = _load_job(job_id) or {}
            job.update({
                "status": "running",
                "phase": "prompts",
                "prompts_done": done,
                "prompts_total": total,
                "progress": int((done / total) * 50),  # 0-50% for prompts
                "message": f"Generating prompts: {done}/{total}",
            })
            _save_job(job_id, job)

        prompts = await WizardGenerator.generate_prompts(
            client=client,
            model_id=request.generator_model,
            domain=request.domain,
            test_description=request.test_description,
            acceptable=request.acceptable_behavior,
            unacceptable=request.unacceptable_behavior,
            count=request.prompt_count,
            on_progress=on_prompt_progress,
        )

        # Update job
        job = _load_job(job_id) or {}
        job.update({
            "phase": "grades",
            "prompts_done": len(prompts),
            "prompts_total": len(prompts),
            "grades_total": len(prompts),
            "progress": 50,
            "message": f"Generated {len(prompts)} prompts. Starting graded response generation...",
        })
        _save_job(job_id, job)

        # Phase 2: Generate graded responses
        def on_grade_progress(done, total):
            job = _load_job(job_id) or {}
            job.update({
                "grades_done": done,
                "progress": 50 + int((done / total) * 50),  # 50-100%
                "message": f"Generating graded responses: {done}/{total}",
            })
            _save_job(job_id, job)

        prompts = await WizardGrader.generate_batch(
            client=client,
            model_id=request.generator_model,
            prompts=prompts,
            acceptable=request.acceptable_behavior,
            unacceptable=request.unacceptable_behavior,
            on_progress=on_grade_progress,
        )

        # Save completed session
        session = _load_session(session_id) or {}
        session["prompts"] = prompts
        _save_session(session_id, session)

        # Mark job complete
        job = _load_job(job_id) or {}
        job.update({
            "status": "completed",
            "phase": "done",
            "progress": 100,
            "prompts_done": len(prompts),
            "grades_done": len(prompts),
            "message": f"Generation complete: {len(prompts)} prompts with graded responses",
        })
        _save_job(job_id, job)

    except Exception as e:
        job = _load_job(job_id) or {}
        job.update({
            "status": "error",
            "error": str(e),
            "message": f"Generation failed: {e}",
        })
        _save_job(job_id, job)


@router.get("/jobs/{job_id}")
async def get_job_status(job_id: str):
    """Poll generation job progress."""
    job = _load_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    return {"status": "success", "job": job}


class WizardGradeRequest(BaseModel):
    """Generate graded responses for existing prompts in a session."""
    session_id: str
    generator_provider: str = "openai"
    generator_base_url: Optional[str] = None
    generator_api_key: str
    generator_model: str
    generator_format: str = "openai"


@router.post("/grade")
async def start_grading(request: WizardGradeRequest):
    """Generate graded responses for a session that has prompts but no grades."""
    session = _load_session(request.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if not session.get("prompts"):
        raise HTTPException(status_code=400, detail="No prompts in session")

    job_id = f"grade_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
    prompts = session["prompts"]

    job = {
        "id": job_id,
        "session_id": request.session_id,
        "status": "running",
        "phase": "grades",
        "progress": 0,
        "prompts_done": len(prompts),
        "prompts_total": len(prompts),
        "grades_done": 0,
        "grades_total": len(prompts),
        "message": "Starting graded response generation...",
        "error": None,
        "created_at": datetime.now().isoformat(),
    }
    _save_job(job_id, job)

    asyncio.create_task(
        _run_grading(job_id, request.session_id, request, prompts)
    )

    return {
        "status": "success",
        "job_id": job_id,
        "session_id": request.session_id,
        "message": "Grading started",
    }


async def _run_grading(job_id: str, session_id: str,
                        request: WizardGradeRequest, prompts: List[dict]):
    """Background task: generate graded responses for existing prompts."""
    try:
        ep = _build_endpoint(
            request.generator_provider,
            request.generator_api_key,
            request.generator_base_url,
            request.generator_format,
        )
        client = UnifiedAPIClient(ep)

        session = _load_session(session_id) or {}

        def on_grade_progress(done, total):
            job = _load_job(job_id) or {}
            job.update({
                "grades_done": done,
                "progress": int((done / total) * 100),
                "message": f"Generating graded responses: {done}/{total}",
            })
            _save_job(job_id, job)

        graded = await WizardGrader.generate_batch(
            client=client,
            model_id=request.generator_model,
            prompts=prompts,
            acceptable=session.get("acceptable_behavior", ""),
            unacceptable=session.get("unacceptable_behavior", ""),
            on_progress=on_grade_progress,
        )

        session["prompts"] = graded
        _save_session(session_id, session)

        job = _load_job(job_id) or {}
        job.update({
            "status": "completed",
            "phase": "done",
            "progress": 100,
            "grades_done": len(graded),
            "message": f"Grading complete: {len(graded)} prompts with graded responses",
        })
        _save_job(job_id, job)

    except Exception as e:
        job = _load_job(job_id) or {}
        job.update({
            "status": "error",
            "error": str(e),
            "message": f"Grading failed: {e}",
        })
        _save_job(job_id, job)


@router.post("/test")
async def start_test_run(request: WizardTestRequest):
    """Start test execution against the target model."""
    session = _load_session(request.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if not session.get("prompts"):
        raise HTTPException(status_code=400, detail="No prompts generated yet")

    run_id = f"wtest_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    job = {
        "id": run_id,
        "session_id": request.session_id,
        "status": "running",
        "progress": 0,
        "tests_done": 0,
        "tests_total": len(session["prompts"]),
        "message": "Starting tests...",
        "target_model": request.target_model,
        "results_summary": {"safe": 0, "harmful": 0, "unclear": 0, "errors": 0},
        "results": [],
        "error": None,
        "created_at": datetime.now().isoformat(),
    }
    _save_job(run_id, job)

    asyncio.create_task(
        _run_tests(run_id, request, session)
    )

    return {
        "status": "success",
        "run_id": run_id,
        "tests_total": len(session["prompts"]),
        "message": "Test run started",
    }


async def _run_tests(run_id: str, request: WizardTestRequest, session: dict):
    """Background task: execute tests against target model."""
    try:
        ep = _build_endpoint(
            request.target_provider,
            request.target_api_key,
            request.target_base_url,
            request.target_format,
        )
        client = UnifiedAPIClient(ep)

        def on_progress(done, total, result):
            job = _load_job(run_id) or {}
            job["results"].append(result)
            summary = job["results_summary"]
            cls = result.get("classification", "").upper()
            if cls == "SAFE":
                summary["safe"] += 1
            elif cls == "HARMFUL":
                summary["harmful"] += 1
            elif cls == "ERROR":
                summary["errors"] += 1
            else:
                summary["unclear"] += 1

            job.update({
                "tests_done": done,
                "progress": int((done / total) * 100),
                "message": f"Testing: {done}/{total} ({cls})",
            })
            _save_job(run_id, job)

        await WizardRunner.run_tests(
            client=client,
            model_id=request.target_model,
            prompts_with_grades=session["prompts"],
            delay=request.delay_seconds,
            on_progress=on_progress,
        )

        # Mark complete
        job = _load_job(run_id) or {}
        job.update({
            "status": "completed",
            "progress": 100,
            "message": "Test run complete",
        })
        _save_job(run_id, job)

        # Save results to session
        session["test_results"] = {
            "run_id": run_id,
            "target_model": request.target_model,
            "completed_at": datetime.now().isoformat(),
            "summary": job["results_summary"],
            "results": job["results"],
        }
        _save_session(request.session_id, session)

    except Exception as e:
        job = _load_job(run_id) or {}
        job.update({
            "status": "error",
            "error": str(e),
            "message": f"Test run failed: {e}",
        })
        _save_job(run_id, job)


@router.get("/test/{run_id}")
async def get_test_status(run_id: str):
    """Poll test run progress."""
    job = _load_job(run_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Test run {run_id} not found")
    return {"status": "success", "run": job}


@router.get("/sessions")
async def list_sessions():
    """List saved wizard sessions."""
    sessions_dir = _wizard_dir() / "sessions"
    sessions = []
    for f in sorted(sessions_dir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            sessions.append({
                "id": data.get("id", f.stem),
                "domain": data.get("domain", ""),
                "prompt_count": len(data.get("prompts", [])),
                "has_results": data.get("test_results") is not None,
                "created_at": data.get("created_at", ""),
            })
        except Exception:
            continue
    return {"status": "success", "sessions": sessions}


@router.get("/sessions/{session_id}")
async def get_session(session_id: str):
    """Load a specific wizard session."""
    session = _load_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"status": "success", "session": session}


@router.delete("/sessions/{session_id}")
async def delete_session(session_id: str):
    """Delete a wizard session."""
    path = _wizard_dir() / "sessions" / f"{session_id}.json"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Session not found")
    path.unlink()
    return {"status": "success", "message": "Session deleted"}
