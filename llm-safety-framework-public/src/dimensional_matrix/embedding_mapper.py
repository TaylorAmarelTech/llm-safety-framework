"""
Embedding mapper — creates unified vector representations for guardrail mapping.

Combines three signal sources into a single vector space:
  1. Dimensional scores (36 dims, normalized 0-1)
  2. API/local embeddings (semantic meaning via Embedder)
  3. Hand-crafted features (structural features via FeatureExtractor)

This unified representation enables:
  - Visualizing guardrail boundaries in 2D/3D
  - Finding clusters of prompts that bypass guardrails
  - Identifying gaps in the testing coverage
  - Guiding calibration toward unexplored boundary regions
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from .dimensions import ALL_DIMENSIONS, dimension_ids
from .models import ResponseRating

logger = logging.getLogger("dimensional_matrix.embedding_mapper")


class PromptVector:
    """A prompt's representation in the unified vector space."""

    def __init__(
        self,
        prompt: str,
        dimensional_scores: list[float] | None = None,
        semantic_embedding: list[float] | None = None,
        structural_features: list[float] | None = None,
        response: str = "",
        verdict: str = "",
        model_id: str = "",
        metadata: dict[str, Any] | None = None,
    ):
        self.prompt = prompt
        self.response = response
        self.verdict = verdict
        self.model_id = model_id
        self.metadata = metadata or {}

        self.dimensional_scores = dimensional_scores or []
        self.semantic_embedding = semantic_embedding or []
        self.structural_features = structural_features or []

    @property
    def unified_vector(self) -> list[float]:
        """Concatenated vector from all three signal sources."""
        return self.dimensional_scores + self.semantic_embedding + self.structural_features

    @property
    def dimensional_only(self) -> list[float]:
        """Just the 36-dimensional score vector (0-1 normalized)."""
        return list(self.dimensional_scores)

    def to_dict(self) -> dict:
        return {
            "prompt": self.prompt[:200],
            "response": self.response[:200],
            "verdict": self.verdict,
            "model_id": self.model_id,
            "dim_vector_len": len(self.dimensional_scores),
            "embed_vector_len": len(self.semantic_embedding),
            "feature_vector_len": len(self.structural_features),
            "unified_vector_len": len(self.unified_vector),
            "metadata": self.metadata,
        }


class EmbeddingMapper:
    """
    Maps prompts + responses + ratings into a unified vector space.

    Integrates with:
      - DimensionalRater for dimensional scores
      - Embedder (from intelligent_attack) for semantic embeddings
      - FeatureExtractor (from intelligent_attack) for structural features
      - SpaceAnalyzer for clustering and visualization

    Usage:
        mapper = EmbeddingMapper()

        # Build vectors from ratings
        vectors = mapper.from_ratings(ratings, verdicts)

        # Or build incrementally
        vec = mapper.build_vector(prompt, rating, embedding, features)

        # Analyze the space
        analysis = mapper.analyze_space(vectors)

        # Find guardrail holes
        holes = mapper.find_guardrail_holes(analysis)
    """

    def __init__(self, output_dir: str = "data/boundary_probing"):
        self.output_dir = Path(output_dir)
        self._dim_ids = dimension_ids()  # All 36 dimension IDs in order

    def rating_to_vector(self, rating: ResponseRating) -> list[float]:
        """
        Convert a ResponseRating to a normalized 36-dimensional vector.

        Scores are normalized from 1-5 to 0-1 range.
        Missing dimensions get 0.5 (midpoint).
        """
        score_map = rating.to_vector()
        return [(score_map.get(dim_id, 3) - 1) / 4.0 for dim_id in self._dim_ids]

    def build_vector(
        self,
        prompt: str,
        rating: ResponseRating | None = None,
        semantic_embedding: list[float] | None = None,
        structural_features: dict[str, Any] | None = None,
        response: str = "",
        verdict: str = "",
        model_id: str = "",
    ) -> PromptVector:
        """
        Build a unified PromptVector from available signal sources.

        Any signal source can be None — only available signals are included.
        """
        # Dimensional scores
        dim_scores = self.rating_to_vector(rating) if rating else []

        # Semantic embedding (passed in directly from Embedder)
        sem_embed = semantic_embedding or []

        # Structural features (from FeatureExtractor dict)
        struct_vec = []
        if structural_features:
            from src.intelligent_attack.feature_extractor import FeatureExtractor
            struct_vec = FeatureExtractor.to_vector(structural_features)

        return PromptVector(
            prompt=prompt,
            dimensional_scores=dim_scores,
            semantic_embedding=sem_embed,
            structural_features=struct_vec,
            response=response,
            verdict=verdict,
            model_id=model_id,
        )

    def from_ratings(
        self,
        ratings: list[ResponseRating],
        verdicts: list[str] | None = None,
        embeddings: list[list[float]] | None = None,
    ) -> list[PromptVector]:
        """
        Bulk convert ratings to PromptVectors.

        Args:
            ratings: List of ResponseRating objects.
            verdicts: Parallel list of REFUSED/PARTIAL/COMPLIANT verdicts.
            embeddings: Parallel list of semantic embeddings (from Embedder).
        """
        vectors = []
        for i, rating in enumerate(ratings):
            verdict = verdicts[i] if verdicts and i < len(verdicts) else ""
            embedding = embeddings[i] if embeddings and i < len(embeddings) else None

            vec = self.build_vector(
                prompt=rating.prompt,
                rating=rating,
                semantic_embedding=embedding,
                response=rating.response,
                verdict=verdict,
                model_id=rating.model_id,
            )
            vectors.append(vec)

        return vectors

    def analyze_space(
        self,
        vectors: list[PromptVector],
        use_dimensional: bool = True,
        use_semantic: bool = True,
        use_structural: bool = True,
        min_cluster_size: int = 3,
    ) -> dict[str, Any]:
        """
        Analyze the vector space using SpaceAnalyzer.

        Selects which signal components to include in the analysis.
        Returns 2D projections, clusters, and guardrail statistics.
        """
        from src.intelligent_attack.space_analyzer import SpaceAnalyzer

        # Build embedding vectors based on selected components
        embed_vecs = []
        for v in vectors:
            components = []
            if use_dimensional and v.dimensional_scores:
                components.extend(v.dimensional_scores)
            if use_semantic and v.semantic_embedding:
                components.extend(v.semantic_embedding)
            if use_structural and v.structural_features:
                components.extend(v.structural_features)

            if not components:
                # Fallback: use dimensional if nothing else available
                if v.dimensional_scores:
                    components = v.dimensional_scores
                else:
                    components = [0.5] * 36  # neutral midpoint

            embed_vecs.append(components)

        # Pad to equal length (different prompts might have different embedding dims)
        max_len = max(len(v) for v in embed_vecs) if embed_vecs else 0
        embed_vecs = [v + [0.0] * (max_len - len(v)) for v in embed_vecs]

        labels = [v.prompt[:80] for v in vectors]
        classifications = []
        for v in vectors:
            if v.verdict.upper() in ("REFUSED", "SAFE"):
                classifications.append("SAFE")
            elif v.verdict.upper() in ("COMPLIANT", "HARMFUL"):
                classifications.append("HARMFUL")
            else:
                classifications.append("UNCLEAR")

        analyzer = SpaceAnalyzer(str(self.output_dir / "analyses"))
        analysis = analyzer.analyze(
            embeddings=embed_vecs,
            labels=labels,
            classifications=classifications,
            min_cluster_size=min_cluster_size,
        )

        # Enrich with dimensional metadata
        analysis["signal_components"] = {
            "dimensional": use_dimensional,
            "semantic": use_semantic,
            "structural": use_structural,
            "vector_dimensions": max_len,
        }

        # Add per-point dimensional data for drill-down
        for i, point in enumerate(analysis.get("points", [])):
            if i < len(vectors):
                v = vectors[i]
                point["verdict"] = v.verdict
                point["model_id"] = v.model_id
                if v.dimensional_scores:
                    # Add top-3 highest dimensions
                    dim_with_scores = list(zip(self._dim_ids, v.dimensional_scores))
                    dim_with_scores.sort(key=lambda x: x[1], reverse=True)
                    point["top_dims"] = [
                        {"id": d, "score": round(s * 4 + 1, 1)}
                        for d, s in dim_with_scores[:3]
                    ]

        return analysis

    def find_guardrail_holes(
        self,
        analysis: dict[str, Any],
        harm_rate_threshold: float = 0.3,
    ) -> list[dict]:
        """
        Find guardrail holes in the analyzed space.

        Wraps GapFinder from intelligent_attack, enriching results with
        dimensional information about what makes each hole distinctive.
        """
        from src.intelligent_attack.gap_finder import GapFinder

        gaps = GapFinder.find_gaps(analysis, harm_rate_threshold)

        # Enrich each gap with dimensional profile
        for gap in gaps:
            cluster_id = str(gap.get("cluster_id", ""))
            cluster_points = [
                p for p in analysis.get("points", [])
                if str(p.get("cluster")) == cluster_id
            ]

            # Find which dimensions are highest in this cluster
            top_dims_counter: dict[str, list[float]] = {}
            for point in cluster_points:
                for td in point.get("top_dims", []):
                    top_dims_counter.setdefault(td["id"], []).append(td["score"])

            if top_dims_counter:
                dim_avgs = {
                    dim_id: sum(scores) / len(scores)
                    for dim_id, scores in top_dims_counter.items()
                }
                gap["dominant_dimensions"] = sorted(
                    dim_avgs.items(), key=lambda x: x[1], reverse=True,
                )[:5]
            else:
                gap["dominant_dimensions"] = []

        return gaps

    def suggest_probes(
        self,
        analysis: dict[str, Any],
        n_probes: int = 10,
    ) -> list[dict]:
        """
        Suggest new probes to explore under-tested regions.

        Combines sparse-region detection from GapFinder with dimensional
        guidance to suggest which dimension + direction to push.
        """
        from src.intelligent_attack.gap_finder import GapFinder

        sparse = GapFinder.find_sparse_regions(analysis, n_regions=n_probes)

        suggestions = []
        for region in sparse:
            # Find nearest point to the sparse region center
            center_x = region["center"]["x"]
            center_y = region["center"]["y"]

            nearest = None
            nearest_dist = float("inf")
            for point in analysis.get("points", []):
                dx = point["x"] - center_x
                dy = point["y"] - center_y
                dist = (dx ** 2 + dy ** 2) ** 0.5
                if dist < nearest_dist:
                    nearest_dist = dist
                    nearest = point

            suggestion = {
                "region_center": region["center"],
                "density": region["density"],
            }

            if nearest:
                suggestion["nearest_prompt"] = nearest.get("label", "")[:200]
                suggestion["nearest_verdict"] = nearest.get("classification", "")

                # Suggest dimension + direction based on nearest point's top dims
                top_dims = nearest.get("top_dims", [])
                if top_dims:
                    # Push along the highest-scoring dimension (find boundary)
                    suggestion["recommended_dimension"] = top_dims[0]["id"]
                    suggestion["recommended_direction"] = (
                        "down" if nearest.get("classification") == "HARMFUL" else "up"
                    )

            suggestions.append(suggestion)

        return suggestions

    def save_analysis(self, analysis: dict, name: str = "latest") -> str:
        """Save analysis to disk."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        filepath = self.output_dir / f"embedding_analysis_{name}.json"
        analysis["saved_at"] = datetime.now().isoformat()

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False, default=str)

        return str(filepath)

    def export_vectors(self, vectors: list[PromptVector], name: str = "vectors") -> str:
        """Export vectors to JSON for external analysis."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        filepath = self.output_dir / f"{name}.json"

        data = {
            "count": len(vectors),
            "dim_ids": self._dim_ids,
            "vectors": [v.to_dict() for v in vectors],
            "raw_unified": [v.unified_vector for v in vectors],
            "raw_dimensional": [v.dimensional_only for v in vectors],
            "exported_at": datetime.now().isoformat(),
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return str(filepath)
