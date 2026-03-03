"""
Prompt spinning pipeline routes.

Local remixing, LLM-based rephrasing, attack augmentation,
custom augmentation, and pipeline management.

All spinning happens BEFORE test execution - results are
saved to the pipeline for later use.
"""

import json
import re
import uuid
import random
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..config import ConfigManager, get_settings
from ...spinning.multilingual import MultilingualAttacker

router = APIRouter()
config_manager = ConfigManager()


# =============================================================================
# Request Models
# =============================================================================

class SpintaxRequest(BaseModel):
    """Request for local spintax expansion."""
    template: str
    count: int = 10
    save_to_pipeline: bool = True


class RegexSpinRequest(BaseModel):
    """Request for regex-based spinning."""
    prompts: List[str]
    patterns: List[Dict[str, str]]  # [{"find": "...", "replace": "..."}]
    save_to_pipeline: bool = True


class CharPaddingRequest(BaseModel):
    """Request for character padding/trailing."""
    prompts: List[str]
    padding_chars: str = " "
    padding_count: int = 0
    trailing_chars: str = ""
    insert_zero_width: bool = False
    save_to_pipeline: bool = True


class LLMRephrasingRequest(BaseModel):
    """Request for LLM-based rephrasing."""
    prompts: List[str]
    model_id: str
    rephrase_instructions: str = "Rephrase this prompt while preserving the original intent and meaning."
    count_per_prompt: int = 3
    temperature: float = 0.9
    save_to_pipeline: bool = True


class AttackAugmentRequest(BaseModel):
    """Request for attack strategy augmentation."""
    prompts: List[str]
    strategies: List[str]
    save_to_pipeline: bool = True


class CustomAugmentRequest(BaseModel):
    """Request for custom user-defined augmentation."""
    prompts: List[str]
    prefix: str = ""
    suffix: str = ""
    find_replace: List[Dict[str, str]] = Field(default_factory=list)
    save_to_pipeline: bool = True


class EncodeRequest(BaseModel):
    """Request for encoding/cipher prompt transformation."""
    prompts: List[str]
    encoding_type: str  # base64, rot13, hex, caesar, reverse, pig_latin
    options: Dict[str, Any] = Field(default_factory=dict)
    save_to_pipeline: bool = True


class ObfuscateRequest(BaseModel):
    """Request for visual/character obfuscation."""
    prompts: List[str]
    techniques: List[Dict[str, Any]]  # [{"technique": "...", "options": {...}}]
    save_to_pipeline: bool = True


class JailbreakWrapRequest(BaseModel):
    """Request for jailbreak template wrapping."""
    prompts: List[str]
    template_ids: List[str]
    save_to_pipeline: bool = True


class PipelineBuildRequest(BaseModel):
    """Request to build the active pipeline from sources."""
    prompt_set_ids: List[str] = Field(default_factory=list)
    include_spun: bool = True
    deduplicate: bool = True
    dedup_threshold: float = 0.95


# =============================================================================
# Helpers
# =============================================================================

def _expand_spintax(template: str) -> str:
    """Expand a single spintax template: {opt1|opt2|opt3}."""
    pattern = r'\{([^{}]+)\}'
    while re.search(pattern, template):
        def _pick(match: re.Match) -> str:
            options = match.group(1).split('|')
            return random.choice(options)
        template = re.sub(pattern, _pick, template)
    return template


def _save_spin_job(settings_obj: Any, job_id: str, job_data: dict) -> None:
    """Save a spin job result to the pipeline directory."""
    spun_dir = Path(settings_obj.pipeline_dir) / "spun"
    spun_dir.mkdir(parents=True, exist_ok=True)
    with open(spun_dir / f"{job_id}.json", 'w', encoding='utf-8') as f:
        json.dump(job_data, f, indent=2, ensure_ascii=False)


# =============================================================================
# Local Remixing
# =============================================================================

@router.post("/spintax")
async def expand_spintax(request: SpintaxRequest):
    """Expand a spintax template into multiple prompts."""
    results = []
    seen = set()
    attempts = 0
    max_attempts = request.count * 10

    while len(results) < request.count and attempts < max_attempts:
        expanded = _expand_spintax(request.template)
        if expanded not in seen:
            seen.add(expanded)
            results.append(expanded)
        attempts += 1

    job_id = f"spintax_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "spintax",
            "template": request.template,
            "created_at": datetime.now().isoformat(),
            "prompts": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(results),
        "prompts": results,
        "saved": request.save_to_pipeline,
    }


@router.post("/regex")
async def regex_spin(request: RegexSpinRequest):
    """Apply regex find-replace patterns to prompts."""
    results = []
    for prompt in request.prompts:
        modified = prompt
        for pattern in request.patterns:
            find = pattern.get("find", "")
            replace = pattern.get("replace", "")
            if find:
                modified = re.sub(find, replace, modified)
        results.append(modified)

    job_id = f"regex_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "regex",
            "patterns": request.patterns,
            "created_at": datetime.now().isoformat(),
            "prompts": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(results),
        "prompts": results,
        "saved": request.save_to_pipeline,
    }


@router.post("/char-padding")
async def char_padding(request: CharPaddingRequest):
    """Apply character padding/trailing to prompts."""
    results = []
    for prompt in request.prompts:
        modified = prompt
        if request.padding_count > 0:
            modified = (request.padding_chars * request.padding_count) + modified
        if request.trailing_chars:
            modified = modified + request.trailing_chars
        if request.insert_zero_width:
            # Insert zero-width spaces between characters
            modified = '\u200b'.join(modified)
        results.append(modified)

    job_id = f"charpad_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "char_padding",
            "created_at": datetime.now().isoformat(),
            "prompts": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(results),
        "prompts": results,
        "saved": request.save_to_pipeline,
    }


# =============================================================================
# LLM-Based Rephrasing
# =============================================================================

@router.post("/llm-rephrase")
async def llm_rephrase(request: LLMRephrasingRequest):
    """Use an LLM to rephrase prompts."""
    from ...api_client import UnifiedAPIClient

    model = config_manager.get_model(request.model_id)
    if not model:
        raise HTTPException(status_code=404, detail=f"Model {request.model_id} not found")

    ep = config_manager.get_endpoint(model.get("endpoint_id", ""))
    if not ep or not ep.get("api_key"):
        raise HTTPException(status_code=400, detail="Endpoint not configured or missing API key")

    client = UnifiedAPIClient(ep)
    results = []

    for prompt in request.prompts:
        variations = []
        for _ in range(request.count_per_prompt):
            try:
                rephrase_prompt = (
                    f"{request.rephrase_instructions}\n\n"
                    f"Original prompt:\n{prompt}\n\n"
                    f"Rephrased version:"
                )
                rephrased = await client.chat(
                    model_id=model["model_id"],
                    messages=[{"role": "user", "content": rephrase_prompt}],
                    temperature=request.temperature,
                    max_tokens=model.get("max_tokens", 1024),
                )
                variations.append(rephrased.strip())
            except Exception as e:
                variations.append(f"[Error: {str(e)}]")
        results.append({"original": prompt, "variations": variations})

    all_prompts = []
    for r in results:
        all_prompts.extend(r["variations"])

    job_id = f"llm_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "llm_rephrase",
            "model": request.model_id,
            "created_at": datetime.now().isoformat(),
            "prompts": all_prompts,
            "details": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(all_prompts),
        "results": results,
        "saved": request.save_to_pipeline,
    }


# =============================================================================
# Attack Augmentation
# =============================================================================

@router.post("/attack-augment")
async def attack_augment(request: AttackAugmentRequest):
    """Apply attack strategies to augment prompts."""
    results = []

    for prompt in request.prompts:
        try:
            from ...attacks import AttackRegistry
            mutated = AttackRegistry.apply(prompt, request.strategies)
            results.append({"original": prompt, "mutated": mutated, "strategies": request.strategies})
        except ImportError:
            mutated = prompt
            if "business_framing" in request.strategies:
                mutated = f"As a business owner, {mutated}"
            if "urgency_creation" in request.strategies:
                mutated = f"URGENT: {mutated}"
            results.append({"original": prompt, "mutated": mutated, "strategies": request.strategies})

    all_prompts = [r["mutated"] for r in results]
    job_id = f"attack_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "attack_augment",
            "strategies": request.strategies,
            "created_at": datetime.now().isoformat(),
            "prompts": all_prompts,
            "details": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(all_prompts),
        "results": results,
        "saved": request.save_to_pipeline,
    }


# =============================================================================
# Custom Augmentation
# =============================================================================

@router.post("/custom-augment")
async def custom_augment(request: CustomAugmentRequest):
    """Apply custom user-defined augmentation."""
    results = []
    for prompt in request.prompts:
        modified = prompt
        for fr in request.find_replace:
            find = fr.get("find", "")
            replace = fr.get("replace", "")
            if find:
                modified = modified.replace(find, replace)
        if request.prefix:
            modified = request.prefix + modified
        if request.suffix:
            modified = modified + request.suffix
        results.append(modified)

    job_id = f"custom_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "custom_augment",
            "created_at": datetime.now().isoformat(),
            "prompts": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(results),
        "prompts": results,
        "saved": request.save_to_pipeline,
    }


# =============================================================================
# Encoding / Cipher
# =============================================================================

@router.post("/encode")
async def encode_prompts(request: EncodeRequest):
    """Encode prompts using cipher/encoding techniques."""
    from ...spinning.encoders import PromptEncoder

    encoding_fns = {
        "base64": PromptEncoder.base64_encode,
        "rot13": PromptEncoder.rot13_encode,
        "hex": PromptEncoder.hex_encode,
        "caesar": PromptEncoder.caesar_encode,
        "reverse": PromptEncoder.reverse_encode,
        "pig_latin": PromptEncoder.pig_latin_encode,
    }

    fn = encoding_fns.get(request.encoding_type)
    if not fn:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown encoding type: {request.encoding_type}. "
                   f"Valid: {list(encoding_fns.keys())}",
        )

    results = fn(request.prompts, **request.options)
    job_id = f"encode_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "encode",
            "encoding_type": request.encoding_type,
            "created_at": datetime.now().isoformat(),
            "prompts": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(results),
        "prompts": results,
        "saved": request.save_to_pipeline,
    }


# =============================================================================
# Obfuscation
# =============================================================================

@router.post("/obfuscate")
async def obfuscate_prompts(request: ObfuscateRequest):
    """Apply visual/character obfuscation techniques (layerable)."""
    from ...spinning.obfuscators import TextObfuscator

    results = TextObfuscator.apply_layers(request.prompts, request.techniques)
    job_id = f"obfusc_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "obfuscate",
            "techniques": [t.get("technique", "") for t in request.techniques],
            "created_at": datetime.now().isoformat(),
            "prompts": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(results),
        "prompts": results,
        "saved": request.save_to_pipeline,
    }


# =============================================================================
# Jailbreak Template Wrapping
# =============================================================================

@router.get("/jailbreak-templates")
async def list_jailbreak_templates():
    """List all available jailbreak templates with metadata."""
    from ...spinning.jailbreak_templates import JailbreakTemplater

    templates = JailbreakTemplater.list_templates()
    categories = JailbreakTemplater.list_categories()
    return {
        "status": "success",
        "templates": templates,
        "categories": categories,
        "count": len(templates),
    }


@router.post("/jailbreak-wrap")
async def jailbreak_wrap(request: JailbreakWrapRequest):
    """Wrap prompts with jailbreak templates."""
    from ...spinning.jailbreak_templates import JailbreakTemplater

    results = JailbreakTemplater.apply(request.prompts, request.template_ids)
    all_prompts = [r["wrapped"] for r in results]
    job_id = f"jailbreak_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "jailbreak_wrap",
            "template_ids": request.template_ids,
            "created_at": datetime.now().isoformat(),
            "prompts": all_prompts,
            "details": results,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(all_prompts),
        "prompts": all_prompts,
        "results": results,
        "saved": request.save_to_pipeline,
    }


# =============================================================================
# Attack Chain Builder
# =============================================================================

class ChainSaveRequest(BaseModel):
    name: str
    description: str = ""
    steps: List[Dict[str, Any]] = Field(default_factory=list)


class ChainExecuteRequest(BaseModel):
    prompts: List[str]
    steps: List[Dict[str, Any]]
    save_to_pipeline: bool = True


class ChainPreviewRequest(BaseModel):
    prompt: str
    steps: List[Dict[str, Any]]


def _get_chains_dir():
    settings = get_settings()
    chains_dir = Path(settings.pipeline_dir) / "chains"
    chains_dir.mkdir(parents=True, exist_ok=True)
    return chains_dir


def _execute_chain_steps(prompts: List[str], steps: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Execute chain steps sequentially, returning per-step intermediates."""
    from ...spinning.encoders import PromptEncoder
    from ...spinning.obfuscators import TextObfuscator
    from ...spinning.jailbreak_templates import JailbreakTemplater

    intermediates = []
    current = list(prompts)

    for step in steps:
        step_type = step.get("type", "")
        config = step.get("config", {})
        before = list(current)

        if step_type == "encode":
            encoding_type = config.get("encoding_type", "base64")
            opts = {k: v for k, v in config.items() if k != "encoding_type"}
            fn_map = {
                "base64": PromptEncoder.base64_encode,
                "rot13": PromptEncoder.rot13_encode,
                "hex": PromptEncoder.hex_encode,
                "caesar": PromptEncoder.caesar_encode,
                "reverse": PromptEncoder.reverse_encode,
                "pig_latin": PromptEncoder.pig_latin_encode,
            }
            fn = fn_map.get(encoding_type)
            if fn:
                current = fn(current, **opts)

        elif step_type == "obfuscate":
            techniques = config.get("techniques", [])
            if techniques:
                current = TextObfuscator.apply_layers(current, techniques)

        elif step_type == "jailbreak_wrap":
            template_ids = config.get("template_ids", [])
            if template_ids:
                results = JailbreakTemplater.apply(current, template_ids)
                current = [r["wrapped"] for r in results]

        elif step_type == "regex":
            patterns = config.get("patterns", [])
            import re as re_mod
            new = []
            for p in current:
                text = p
                for pat in patterns:
                    find = pat.get("find", "")
                    replace = pat.get("replace", "")
                    if find:
                        text = re_mod.sub(find, replace, text)
                new.append(text)
            current = new

        elif step_type == "charpad":
            padding_chars = config.get("padding_chars", " ")
            padding_count = config.get("padding_count", 0)
            trailing_chars = config.get("trailing_chars", "")
            insert_zw = config.get("insert_zero_width", False)
            new = []
            for p in current:
                text = p
                if padding_count > 0:
                    text = (padding_chars * padding_count) + text
                if trailing_chars:
                    text = text + trailing_chars
                if insert_zw:
                    text = "\u200b".join(text)
                new.append(text)
            current = new

        elif step_type == "custom":
            prefix = config.get("prefix", "")
            suffix = config.get("suffix", "")
            find_replace = config.get("find_replace", [])
            new = []
            for p in current:
                text = prefix + p + suffix
                for fr in find_replace:
                    text = text.replace(fr.get("find", ""), fr.get("replace", ""))
                new.append(text)
            current = new

        intermediates.append({
            "step": step_type,
            "config": config,
            "input_count": len(before),
            "output_count": len(current),
            "sample_before": before[0] if before else "",
            "sample_after": current[0] if current else "",
        })

    return intermediates, current


@router.get("/chains")
async def list_chains():
    """List all saved attack chains."""
    chains_dir = _get_chains_dir()
    chains = []
    for f in sorted(chains_dir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            chains.append({
                "id": data.get("id", f.stem),
                "name": data.get("name", "Untitled"),
                "description": data.get("description", ""),
                "step_count": len(data.get("steps", [])),
                "created_at": data.get("created_at", ""),
            })
        except Exception:
            continue
    return {"status": "success", "chains": chains}


@router.get("/chains/{chain_id}")
async def get_chain(chain_id: str):
    """Get a saved chain with full step details."""
    chains_dir = _get_chains_dir()
    chain_file = chains_dir / f"{chain_id}.json"
    if not chain_file.exists():
        raise HTTPException(status_code=404, detail=f"Chain {chain_id} not found")
    with open(chain_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return {"status": "success", "chain": data}


@router.post("/chains")
async def save_chain(request: ChainSaveRequest):
    """Save a new attack chain."""
    if not request.steps:
        raise HTTPException(status_code=400, detail="Chain must have at least one step")

    chains_dir = _get_chains_dir()
    chain_id = f"chain_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
    chain_data = {
        "id": chain_id,
        "name": request.name,
        "description": request.description,
        "steps": request.steps,
        "created_at": datetime.now().isoformat(),
    }
    with open(chains_dir / f"{chain_id}.json", 'w', encoding='utf-8') as f:
        json.dump(chain_data, f, indent=2, ensure_ascii=False)

    return {"status": "success", "chain_id": chain_id, "message": f"Chain '{request.name}' saved"}


@router.delete("/chains/{chain_id}")
async def delete_chain(chain_id: str):
    """Delete a saved chain."""
    chains_dir = _get_chains_dir()
    chain_file = chains_dir / f"{chain_id}.json"
    if not chain_file.exists():
        raise HTTPException(status_code=404, detail=f"Chain {chain_id} not found")
    chain_file.unlink()
    return {"status": "success", "message": f"Chain {chain_id} deleted"}


@router.post("/chains/execute")
async def execute_chain(request: ChainExecuteRequest):
    """Execute a chain on input prompts."""
    if not request.steps:
        raise HTTPException(status_code=400, detail="Chain must have at least one step")
    if not request.prompts:
        raise HTTPException(status_code=400, detail="No prompts provided")

    intermediates, final_prompts = _execute_chain_steps(request.prompts, request.steps)
    job_id = f"chain_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

    if request.save_to_pipeline:
        settings = get_settings()
        _save_spin_job(settings, job_id, {
            "id": job_id,
            "type": "chain",
            "steps": [s["step"] for s in intermediates],
            "created_at": datetime.now().isoformat(),
            "prompts": final_prompts,
        })

    return {
        "status": "success",
        "job_id": job_id,
        "count": len(final_prompts),
        "prompts": final_prompts,
        "intermediates": intermediates,
        "saved": request.save_to_pipeline,
    }


@router.post("/chains/preview")
async def preview_chain(request: ChainPreviewRequest):
    """Preview a single prompt through a chain, showing step-by-step transformations."""
    if not request.steps:
        raise HTTPException(status_code=400, detail="Chain must have at least one step")

    intermediates, final_prompts = _execute_chain_steps([request.prompt], request.steps)

    return {
        "status": "success",
        "original": request.prompt,
        "final": final_prompts[0] if final_prompts else "",
        "steps": intermediates,
    }


# =============================================================================
# Pipeline Management
# =============================================================================

@router.get("/jobs")
async def list_spin_jobs():
    """List all spin jobs in the pipeline."""
    settings = get_settings()
    spun_dir = Path(settings.pipeline_dir) / "spun"

    if not spun_dir.exists():
        return {"status": "success", "jobs": []}

    jobs = []
    for f in sorted(spun_dir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            jobs.append({
                "id": data.get("id", f.stem),
                "type": data.get("type", "unknown"),
                "created_at": data.get("created_at", ""),
                "count": len(data.get("prompts", [])),
            })
        except Exception:
            continue

    return {"status": "success", "jobs": jobs}


@router.get("/jobs/{job_id}")
async def get_spin_job(job_id: str):
    """Get details for a spin job."""
    settings = get_settings()
    job_file = Path(settings.pipeline_dir) / "spun" / f"{job_id}.json"

    if not job_file.exists():
        raise HTTPException(status_code=404, detail=f"Spin job {job_id} not found")

    with open(job_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return {"status": "success", "job": data}


@router.delete("/jobs/{job_id}")
async def delete_spin_job(job_id: str):
    """Delete a spin job."""
    settings = get_settings()
    job_file = Path(settings.pipeline_dir) / "spun" / f"{job_id}.json"

    if not job_file.exists():
        raise HTTPException(status_code=404, detail=f"Spin job {job_id} not found")

    job_file.unlink()
    return {"status": "success", "message": f"Spin job {job_id} deleted"}


@router.post("/pipeline/build")
async def build_pipeline(request: PipelineBuildRequest):
    """Build the active pipeline from prompt sets and spin jobs."""
    settings = get_settings()
    prompts_file = Path(settings.data_dir) / "sample_test_prompts.json"
    pipeline_dir = Path(settings.pipeline_dir)
    pipeline_dir.mkdir(parents=True, exist_ok=True)

    all_prompts = []
    sources = []

    # Load from default prompt sets
    if prompts_file.exists():
        with open(prompts_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check which sets are disabled
        config_file = pipeline_dir / "pipeline_config.json"
        disabled = []
        if config_file.exists():
            with open(config_file, 'r') as f:
                cfg = json.load(f)
            disabled = cfg.get("disabled_sets", [])

        for suite_name, suite_prompts in data.get("test_suites", {}).items():
            if request.prompt_set_ids and suite_name not in request.prompt_set_ids:
                continue
            if suite_name in disabled:
                continue
            for p in suite_prompts:
                all_prompts.append({
                    "text": p.get("prompt", ""),
                    "source": f"set:{suite_name}",
                    "metadata": p,
                })
            sources.append({"type": "set", "id": suite_name, "count": len(suite_prompts)})

    # Load imported prompt sets
    imported_dir = pipeline_dir / "prompt_sets"
    if imported_dir.exists():
        for f in imported_dir.glob("*.json"):
            if request.prompt_set_ids and f.stem not in request.prompt_set_ids:
                continue
            try:
                with open(f, 'r', encoding='utf-8') as fh:
                    data = json.load(fh)
                prompts = data if isinstance(data, list) else data.get("prompts", [])
                for p in prompts:
                    text = p if isinstance(p, str) else p.get("prompt", p.get("text", ""))
                    all_prompts.append({"text": text, "source": f"imported:{f.stem}", "metadata": p if isinstance(p, dict) else {}})
                sources.append({"type": "imported", "id": f.stem, "count": len(prompts)})
            except Exception:
                continue

    # Load spun prompts
    if request.include_spun:
        spun_dir = pipeline_dir / "spun"
        if spun_dir.exists():
            for f in spun_dir.glob("*.json"):
                try:
                    with open(f, 'r', encoding='utf-8') as fh:
                        data = json.load(fh)
                    for p in data.get("prompts", []):
                        text = p if isinstance(p, str) else p.get("text", str(p))
                        all_prompts.append({"text": text, "source": f"spun:{data.get('id', f.stem)}", "metadata": {}})
                    sources.append({"type": "spun", "id": data.get("id", f.stem), "count": len(data.get("prompts", []))})
                except Exception:
                    continue

    # Deduplicate
    if request.deduplicate:
        seen = set()
        deduped = []
        for p in all_prompts:
            text = p["text"].strip().lower()
            if text not in seen:
                seen.add(text)
                deduped.append(p)
        all_prompts = deduped

    # Save active pipeline
    pipeline_data = {
        "built_at": datetime.now().isoformat(),
        "sources": sources,
        "total": len(all_prompts),
        "prompts": all_prompts,
    }

    with open(pipeline_dir / "active_pipeline.json", 'w', encoding='utf-8') as f:
        json.dump(pipeline_data, f, indent=2, ensure_ascii=False)

    return {
        "status": "success",
        "total": len(all_prompts),
        "sources": sources,
        "deduplicated": request.deduplicate,
    }


@router.get("/pipeline")
async def get_pipeline_status():
    """Get the current active pipeline status."""
    settings = get_settings()
    pipeline_file = Path(settings.pipeline_dir) / "active_pipeline.json"

    if not pipeline_file.exists():
        return {
            "status": "success",
            "pipeline": None,
            "message": "No active pipeline. Build one first.",
        }

    with open(pipeline_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return {
        "status": "success",
        "pipeline": {
            "built_at": data.get("built_at"),
            "total": data.get("total", 0),
            "sources": data.get("sources", []),
        },
    }


@router.get("/pipeline/prompts")
async def get_pipeline_prompts(limit: int = 100, offset: int = 0):
    """Get prompts from the active pipeline."""
    settings = get_settings()
    pipeline_file = Path(settings.pipeline_dir) / "active_pipeline.json"

    if not pipeline_file.exists():
        return {"status": "success", "prompts": [], "total": 0}

    with open(pipeline_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    prompts = data.get("prompts", [])
    total = len(prompts)

    return {
        "status": "success",
        "prompts": prompts[offset:offset + limit],
        "total": total,
    }


# =============================================================================
# Multilingual Attack Routes
# =============================================================================

class TranslateRequest(BaseModel):
    prompts: List[str]
    target_language: str
    model_id: str
    save_to_pipeline: bool = True


class MixLanguageRequest(BaseModel):
    prompts: List[str]
    languages: List[str]
    model_id: str
    mix_ratio: float = 0.5
    save_to_pipeline: bool = True


@router.get("/multilingual/languages")
async def list_languages():
    """List all supported languages for multilingual attacks."""
    return {
        "status": "success",
        "languages": MultilingualAttacker.list_languages(),
        "count": len(MultilingualAttacker.LANGUAGES),
    }


@router.post("/multilingual/translate")
async def translate_prompts(request: TranslateRequest):
    """Translate prompts to a target language using LLM."""
    config = config_manager.export_config()
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
        results = await MultilingualAttacker.translate(
            prompts=request.prompts,
            target_lang=request.target_language,
            endpoint=endpoint,
            model_id=model["model_id"],
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Save to pipeline if requested
    if request.save_to_pipeline:
        settings = get_settings()
        spun_dir = Path(settings.pipeline_dir) / "spun"
        spun_dir.mkdir(parents=True, exist_ok=True)

        import uuid
        job_id = f"multilingual_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        save_data = {
            "id": job_id,
            "type": "multilingual_translate",
            "target_language": request.target_language,
            "model_id": request.model_id,
            "timestamp": datetime.now().isoformat(),
            "results": results,
            "count": len(results),
        }
        with open(spun_dir / f"{job_id}.json", "w", encoding="utf-8") as f:
            json.dump(save_data, f, indent=2, ensure_ascii=False)

    return {
        "status": "success",
        "results": results,
        "count": len(results),
    }


@router.post("/multilingual/mix")
async def mix_language_prompts(request: MixLanguageRequest):
    """Create mixed-language variants of prompts."""
    config = config_manager.export_config()
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
        results = await MultilingualAttacker.mixed_language(
            prompts=request.prompts,
            languages=request.languages,
            endpoint=endpoint,
            model_id=model["model_id"],
            mix_ratio=request.mix_ratio,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Save to pipeline
    if request.save_to_pipeline:
        settings = get_settings()
        spun_dir = Path(settings.pipeline_dir) / "spun"
        spun_dir.mkdir(parents=True, exist_ok=True)

        import uuid
        job_id = f"multilingual_mix_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        save_data = {
            "id": job_id,
            "type": "multilingual_mix",
            "languages": request.languages,
            "mix_ratio": request.mix_ratio,
            "model_id": request.model_id,
            "timestamp": datetime.now().isoformat(),
            "results": results,
            "count": len(results),
        }
        with open(spun_dir / f"{job_id}.json", "w", encoding="utf-8") as f:
            json.dump(save_data, f, indent=2, ensure_ascii=False)

    return {
        "status": "success",
        "results": results,
        "count": len(results),
    }
