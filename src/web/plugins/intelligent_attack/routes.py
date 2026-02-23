"""
Intelligent attack routes.

Feature space analysis using embeddings to find guardrail gaps,
weakness detection, and targeted probe generation.

Uses the src.intelligent_attack package for core logic.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from ...app_context import AppContext, get_ctx
from ....intelligent_attack.embedder import Embedder
from ....intelligent_attack.feature_extractor import FeatureExtractor
from ....intelligent_attack.gap_finder import GapFinder
from ....intelligent_attack.prompt_suggester import PromptSuggester

router = APIRouter()


# =============================================================================
# Request Models
# =============================================================================

class EmbeddingRequest(BaseModel):
    prompts: List[str]
    model_id: Optional[str] = None
    endpoint_id: Optional[str] = None
    use_local: bool = False


class FeatureExtractionRequest(BaseModel):
    prompts: List[str]


class GapAnalysisRequest(BaseModel):
    embedding_source: str = "auto"
    min_cluster_size: int = 5
    include_results: bool = True
    harm_rate_threshold: float = 0.3


class ProbeSuggestionRequest(BaseModel):
    gap_ids: List[str] = Field(default_factory=list)
    count: int = 5
    model_id: Optional[str] = None
    use_llm: bool = False


# =============================================================================
# Embedding Sources
# =============================================================================

@router.get("/embedding-sources")
async def list_embedding_sources(ctx: AppContext = Depends(get_ctx)):
    endpoints = ctx.config_manager.get_all_endpoints()
    sources = Embedder.get_sources(endpoints)
    return {"status": "success", "sources": sources}


# =============================================================================
# Embedding Generation
# =============================================================================

@router.post("/embeddings")
async def generate_embeddings(request: EmbeddingRequest, ctx: AppContext = Depends(get_ctx)):
    if request.use_local:
        try:
            result = await Embedder.embed_local(request.prompts)
            return {"status": "success", **result}
        except ImportError:
            raise HTTPException(
                status_code=400,
                detail="sentence-transformers not installed. Use pip install sentence-transformers",
            )

    endpoint_id = request.endpoint_id
    if not endpoint_id:
        endpoints = ctx.config_manager.get_all_endpoints()
        endpoint_id = Embedder.auto_select_endpoint(endpoints)

    if not endpoint_id:
        raise HTTPException(
            status_code=400,
            detail="No embedding source available. Configure an API endpoint or install sentence-transformers.",
        )

    ep = ctx.config_manager.get_endpoint(endpoint_id)
    if not ep or not ep.get("api_key"):
        raise HTTPException(status_code=400, detail=f"Endpoint {endpoint_id} not configured")

    try:
        result = await Embedder.embed_api(
            request.prompts, ep, model_id=request.model_id,
        )
        return {"status": "success", **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding generation failed: {str(e)}")


# =============================================================================
# Feature Extraction
# =============================================================================

@router.post("/features")
async def extract_features(request: FeatureExtractionRequest):
    features = FeatureExtractor.extract_batch(request.prompts)
    return {
        "status": "success",
        "features": features,
        "count": len(features),
    }


# =============================================================================
# Feature Space Analysis
# =============================================================================

@router.post("/analyze")
async def analyze_feature_space(request: GapAnalysisRequest, ctx: AppContext = Depends(get_ctx)):
    analysis_dir = Path(ctx.settings.pipeline_dir) / "analysis"

    if analysis_dir.exists():
        results_file = analysis_dir / "latest_analysis.json"
        if results_file.exists():
            with open(results_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            gaps = GapFinder.find_gaps(data, request.harm_rate_threshold)
            sparse = GapFinder.find_sparse_regions(data)

            return {
                "status": "success",
                "analysis": data,
                "gaps": gaps,
                "sparse_regions": sparse,
            }

    return {
        "status": "success",
        "analysis": None,
        "gaps": [],
        "sparse_regions": [],
        "message": (
            "No analysis available yet. Generate embeddings for your prompts first, "
            "then run gap analysis. This requires test results with SAFE/HARMFUL classifications."
        ),
    }


@router.post("/analyze/run")
async def run_full_analysis(request: GapAnalysisRequest, ctx: AppContext = Depends(get_ctx)):
    pipeline_file = Path(ctx.settings.pipeline_dir) / "active_pipeline.json"
    if not pipeline_file.exists():
        raise HTTPException(status_code=400, detail="No active pipeline. Build one first.")

    with open(pipeline_file, 'r', encoding='utf-8') as f:
        pipeline = json.load(f)

    prompts = pipeline.get("prompts", [])
    if len(prompts) < 3:
        raise HTTPException(status_code=400, detail="Need at least 3 prompts for analysis")

    texts = [p["text"] for p in prompts]
    features = FeatureExtractor.extract_batch(texts)
    vectors = [FeatureExtractor.to_vector(f) for f in features]

    classifications = []
    for p in prompts:
        clf = p.get("metadata", {}).get("classification", "UNCLEAR")
        classifications.append(clf)

    labels = [p["text"][:100] for p in prompts]

    try:
        from ....intelligent_attack.space_analyzer import SpaceAnalyzer
        analyzer = SpaceAnalyzer(str(Path(ctx.settings.pipeline_dir) / "analysis"))
        analysis = analyzer.analyze(
            vectors,
            labels=labels,
            classifications=classifications,
            min_cluster_size=request.min_cluster_size,
        )
        analysis["prompt_count"] = len(prompts)
        analyzer.save_analysis(analysis)

        gaps = GapFinder.find_gaps(analysis, request.harm_rate_threshold)

        return {
            "status": "success",
            "analysis": analysis,
            "gaps": gaps,
            "feature_dimensions": len(vectors[0]) if vectors else 0,
        }
    except ImportError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Analysis requires numpy/sklearn. Install with: pip install numpy scikit-learn. Error: {e}",
        )


# =============================================================================
# Probe Suggestion
# =============================================================================

@router.post("/suggest-probes")
async def suggest_probes(request: ProbeSuggestionRequest, ctx: AppContext = Depends(get_ctx)):
    analysis_dir = Path(ctx.settings.pipeline_dir) / "analysis"
    results_file = analysis_dir / "latest_analysis.json"

    if not results_file.exists():
        return {
            "status": "success",
            "probes": [],
            "message": "Run feature space analysis first with test results.",
        }

    with open(results_file, 'r', encoding='utf-8') as f:
        analysis = json.load(f)

    gaps = GapFinder.find_gaps(analysis)

    if request.gap_ids:
        gaps = [g for g in gaps if g["id"] in request.gap_ids]

    if not gaps:
        return {
            "status": "success",
            "probes": [],
            "message": "No gaps found matching criteria.",
        }

    if request.use_llm and request.model_id:
        model = ctx.config_manager.get_model(request.model_id)
        if not model:
            raise HTTPException(status_code=404, detail=f"Model {request.model_id} not found")

        ep = ctx.config_manager.get_endpoint(model.get("endpoint_id", ""))
        if not ep or not ep.get("api_key"):
            raise HTTPException(status_code=400, detail="Endpoint not configured")

        probes = await PromptSuggester.suggest_with_llm(
            gaps, ep, model["model_id"], count_per_gap=request.count,
        )
    else:
        probes = PromptSuggester.suggest_from_gaps(gaps, count_per_gap=request.count)

    return {
        "status": "success",
        "probes": probes,
        "gap_count": len(gaps),
    }


# =============================================================================
# Analysis History
# =============================================================================

@router.get("/analyses")
async def list_analyses(ctx: AppContext = Depends(get_ctx)):
    try:
        from ....intelligent_attack.space_analyzer import SpaceAnalyzer
        analyzer = SpaceAnalyzer(str(Path(ctx.settings.pipeline_dir) / "analysis"))
        analyses = analyzer.list_analyses()
    except ImportError:
        analyses = []

    return {"status": "success", "analyses": analyses}
