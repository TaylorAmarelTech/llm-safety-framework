"""
Representation probing for safety-relevant concept directions in embedding space.

Implements Concept Activation Vectors (CAVs) and representation engineering
techniques to discover and manipulate latent directions corresponding to
safety-relevant concepts (refusal, compliance, deception, etc.).

This module works *without* model internals — it uses external embedding
functions to probe the model's representational geometry from the outside.

Sources:
- Kim et al. (2018): "Interpretability Beyond Feature Attribution:
  Quantitative Testing with Concept Activation Vectors (TCAV)"
- Zou et al. (2023): "Representation Engineering: A Top-Down Approach to
  AI Transparency" — refusal direction identification
- Turner et al. (2023): "Activation Addition: Steering Language Models
  Without Optimization"
- Li et al. (2024): "Inference-Time Intervention: Eliciting Truthful
  Answers from a Language Model" — concept vector steering
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence


# ---------------------------------------------------------------------------
# Pure-Python vector helpers
# ---------------------------------------------------------------------------


def _vec_dot(a: Sequence[float], b: Sequence[float]) -> float:
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))


def _vec_add(a: Sequence[float], b: Sequence[float]) -> list[float]:
    """Element-wise addition."""
    return [x + y for x, y in zip(a, b)]


def _vec_sub(a: Sequence[float], b: Sequence[float]) -> list[float]:
    """Element-wise subtraction."""
    return [x - y for x, y in zip(a, b)]


def _vec_scale(v: Sequence[float], s: float) -> list[float]:
    """Scalar multiplication."""
    return [x * s for x in v]


def _vec_norm(v: Sequence[float]) -> float:
    """L2 norm."""
    return math.sqrt(sum(x * x for x in v))


def _vec_normalize(v: Sequence[float]) -> list[float]:
    """Normalize to unit length."""
    n = _vec_norm(v)
    if n < 1e-12:
        return [0.0] * len(v)
    return [x / n for x in v]


def _vec_mean(vecs: list[list[float]]) -> list[float]:
    """Compute element-wise mean of a list of vectors."""
    if not vecs:
        return []
    dim = len(vecs[0])
    result = [0.0] * dim
    for v in vecs:
        for i in range(dim):
            result[i] += v[i]
    return [x / len(vecs) for x in result]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class ConceptVector:
    """A direction in embedding space corresponding to a named concept.

    Attributes:
        direction: Unit vector in embedding space.
        concept_name: Human-readable label (e.g. "refusal", "safety").
        strength: Magnitude of the raw (unnormalized) concept direction.
        metadata: Optional additional information about extraction.
    """

    direction: list[float]
    concept_name: str = ""
    strength: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Main prober
# ---------------------------------------------------------------------------


class RepresentationProber:
    """Probe and manipulate concept directions in embedding space.

    Discovers latent directions that correspond to safety-relevant concepts
    (refusal, compliance, deception) by contrasting groups of embeddings
    and fitting simple linear probes.

    All operations work on pre-computed embeddings (``list[float]``).
    An optional *embedder* callback can be supplied to convert strings
    to embeddings on the fly.
    """

    def __init__(self, embedder: Callable[[str], list[float]] | None = None):
        self._embedder = embedder

    # -- concept direction discovery ----------------------------------------

    def find_refusal_direction(
        self,
        refused_embeddings: list[list[float]],
        accepted_embeddings: list[list[float]],
    ) -> ConceptVector:
        """Compute the refusal direction as the mean-difference vector.

        The "refusal direction" is the vector from the centroid of prompts
        whose responses were accepted to the centroid of prompts whose
        responses were refused.  Projecting new embeddings onto this
        direction predicts how likely the model is to refuse.

        Based on Zou et al. (2023) representation engineering.
        """
        refused_mean = _vec_mean(refused_embeddings)
        accepted_mean = _vec_mean(accepted_embeddings)
        raw = _vec_sub(refused_mean, accepted_mean)
        strength = _vec_norm(raw)
        direction = _vec_normalize(raw)
        return ConceptVector(
            direction=direction,
            concept_name="refusal",
            strength=strength,
            metadata={
                "n_refused": len(refused_embeddings),
                "n_accepted": len(accepted_embeddings),
                "method": "mean_difference",
            },
        )

    def find_safety_vector(
        self,
        safe_embeddings: list[list[float]],
        unsafe_embeddings: list[list[float]],
    ) -> ConceptVector:
        """Compute the safety concept direction (safe → unsafe).

        Similar to the refusal direction but contrasts safe vs unsafe
        prompt content rather than model response behavior.
        """
        safe_mean = _vec_mean(safe_embeddings)
        unsafe_mean = _vec_mean(unsafe_embeddings)
        raw = _vec_sub(unsafe_mean, safe_mean)
        strength = _vec_norm(raw)
        direction = _vec_normalize(raw)
        return ConceptVector(
            direction=direction,
            concept_name="safety",
            strength=strength,
            metadata={
                "n_safe": len(safe_embeddings),
                "n_unsafe": len(unsafe_embeddings),
                "method": "mean_difference",
            },
        )

    # -- projection & steering ---------------------------------------------

    def project_onto_concept(
        self,
        embedding: list[float],
        concept_vector: ConceptVector,
    ) -> float:
        """Project an embedding onto a concept direction (dot product).

        Returns a scalar: positive means the embedding is aligned with the
        concept direction, negative means it is opposed.
        """
        return _vec_dot(embedding, concept_vector.direction)

    def steer_embedding(
        self,
        embedding: list[float],
        concept_vector: ConceptVector,
        alpha: float = 1.0,
    ) -> list[float]:
        """Steer an embedding by adding alpha * concept direction.

        Positive alpha moves *toward* the concept; negative moves *away*.
        Based on Turner et al. (2023) activation addition.
        """
        return _vec_add(embedding, _vec_scale(concept_vector.direction, alpha))

    # -- linear probe (CAV) ------------------------------------------------

    def compute_concept_activation(
        self,
        embeddings: list[list[float]],
        labels: list[int],
        concept_name: str = "concept",
    ) -> ConceptVector:
        """Fit a linear probe (CAV) to separate positive/negative examples.

        Uses a simple averaged-perceptron approach: compute the mean of
        positive-labeled embeddings minus the mean of negative-labeled
        embeddings.  The resulting vector is the normal to the separating
        hyperplane (in the same spirit as the TCAV paper).

        Labels should be 1 (positive / concept-present) or 0 (negative).
        """
        positives = [e for e, l in zip(embeddings, labels) if l == 1]
        negatives = [e for e, l in zip(embeddings, labels) if l == 0]
        if not positives or not negatives:
            dim = len(embeddings[0]) if embeddings else 0
            return ConceptVector(
                direction=[0.0] * dim,
                concept_name=concept_name,
                strength=0.0,
                metadata={"error": "need both positive and negative examples"},
            )

        pos_mean = _vec_mean(positives)
        neg_mean = _vec_mean(negatives)
        raw = _vec_sub(pos_mean, neg_mean)
        strength = _vec_norm(raw)
        direction = _vec_normalize(raw)

        # Compute linear accuracy as a quality check
        correct = 0
        for emb, label in zip(embeddings, labels):
            proj = _vec_dot(emb, direction)
            threshold = (_vec_dot(pos_mean, direction) + _vec_dot(neg_mean, direction)) / 2
            predicted = 1 if proj > threshold else 0
            if predicted == label:
                correct += 1
        accuracy = correct / len(embeddings) if embeddings else 0.0

        return ConceptVector(
            direction=direction,
            concept_name=concept_name,
            strength=strength,
            metadata={
                "n_positive": len(positives),
                "n_negative": len(negatives),
                "linear_accuracy": round(accuracy, 4),
                "method": "mean_difference_probe",
            },
        )

    # -- sensitivity analysis ----------------------------------------------

    def measure_concept_sensitivity(
        self,
        embeddings: list[list[float]],
        concept_vector: ConceptVector,
    ) -> dict[str, Any]:
        """Measure how embeddings distribute along a concept direction.

        Returns statistics: mean, std, min, max of projections, plus
        the fraction of embeddings on each side of zero.
        """
        if not embeddings:
            return {"error": "no embeddings provided"}

        projections = [self.project_onto_concept(e, concept_vector) for e in embeddings]
        mean_proj = sum(projections) / len(projections)
        var_proj = sum((p - mean_proj) ** 2 for p in projections) / len(projections)
        std_proj = math.sqrt(var_proj)
        positive_frac = sum(1 for p in projections if p > 0) / len(projections)

        return {
            "concept_name": concept_vector.concept_name,
            "n_embeddings": len(embeddings),
            "mean_projection": round(mean_proj, 6),
            "std_projection": round(std_proj, 6),
            "min_projection": round(min(projections), 6),
            "max_projection": round(max(projections), 6),
            "positive_fraction": round(positive_frac, 4),
            "spread": round(max(projections) - min(projections), 6),
        }

    # -- orthogonalization (Gram-Schmidt) -----------------------------------

    def find_orthogonal_concepts(
        self,
        concept_vectors: list[ConceptVector],
    ) -> list[ConceptVector]:
        """Orthogonalize concept directions via Gram-Schmidt.

        Returns a new set of ConceptVectors whose directions are mutually
        orthogonal.  The first vector is unchanged; subsequent vectors
        have components along earlier vectors removed.
        """
        if not concept_vectors:
            return []

        orthogonal: list[list[float]] = []
        results: list[ConceptVector] = []

        for cv in concept_vectors:
            v = list(cv.direction)

            # Subtract projection onto each already-orthogonalized vector
            for u in orthogonal:
                proj_coeff = _vec_dot(v, u)
                v = _vec_sub(v, _vec_scale(u, proj_coeff))

            norm = _vec_norm(v)
            if norm < 1e-12:
                # Degenerate — this concept is a linear combination of prior ones
                results.append(ConceptVector(
                    direction=[0.0] * len(cv.direction),
                    concept_name=cv.concept_name,
                    strength=0.0,
                    metadata={"orthogonalized": True, "degenerate": True},
                ))
                continue

            direction = _vec_normalize(v)
            orthogonal.append(direction)
            results.append(ConceptVector(
                direction=direction,
                concept_name=cv.concept_name,
                strength=norm,
                metadata={"orthogonalized": True, "residual_norm": round(norm, 6)},
            ))

        return results

    # -- concept bottleneck analysis ----------------------------------------

    def concept_bottleneck_analysis(
        self,
        embeddings: list[list[float]],
        concept_vectors: list[ConceptVector],
    ) -> dict[str, Any]:
        """Project embeddings onto the concept subspace and measure explained variance.

        This implements a simplified concept bottleneck: project each
        embedding onto the subspace spanned by the concept vectors, then
        measure what fraction of the total variance is captured by the
        concept subspace.
        """
        if not embeddings or not concept_vectors:
            return {"error": "need embeddings and concept vectors"}

        # First orthogonalize concept directions
        ortho = self.find_orthogonal_concepts(concept_vectors)
        bases = [cv.direction for cv in ortho if _vec_norm(cv.direction) > 1e-12]

        if not bases:
            return {"error": "all concept vectors are degenerate"}

        # Center embeddings
        mean_emb = _vec_mean(embeddings)
        centered = [_vec_sub(e, mean_emb) for e in embeddings]

        # Total variance: sum of squared norms of centered embeddings
        total_var = sum(_vec_dot(c, c) for c in centered)
        if total_var < 1e-12:
            return {
                "total_variance": 0.0,
                "explained_variance": 0.0,
                "explained_ratio": 0.0,
                "n_concepts": len(bases),
                "per_concept": {},
            }

        # Project onto concept subspace and measure explained variance
        explained_per_concept: dict[str, float] = {}
        total_explained = 0.0

        for cv, basis in zip(ortho, bases):
            if _vec_norm(basis) < 1e-12:
                continue
            concept_var = sum(_vec_dot(c, basis) ** 2 for c in centered)
            explained_per_concept[cv.concept_name] = round(concept_var / total_var, 6)
            total_explained += concept_var

        explained_ratio = total_explained / total_var if total_var > 0 else 0.0

        return {
            "total_variance": round(total_var, 6),
            "explained_variance": round(total_explained, 6),
            "explained_ratio": round(explained_ratio, 6),
            "n_concepts": len(bases),
            "per_concept": explained_per_concept,
            "residual_ratio": round(1.0 - explained_ratio, 6),
        }
