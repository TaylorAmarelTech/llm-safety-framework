"""
Toxicity attenuation via embedding-space projection for safety bypass research.

Implements the ``toxicity direction'' attack from Zhang et al. (2025): the key
observation is that safety classifiers predominantly operate along a small set of
directions in embedding space.  By projecting an embedding *onto* that toxic
subspace and then *subtracting* the projection, the resulting vector retains
semantic content while reducing the signal that safety filters key on.

Used in this framework as a **probe** — we test whether a target model's safety
layer can be circumvented by embedding-space toxicity attenuation, and measure
how robust refusals are to this class of attack.

Sources:
- Zhang et al. (2025): "Circumventing Safety Alignment via Embedding Space
  Toxicity Attenuation" — arXiv:2507.08020 — main algorithm
- Park et al. (2023): "Linear Representations of Sentiment in Large Language
  Models" — arXiv:2310.15154 — linear representation hypothesis background
- Zou et al. (2023): "Representation Engineering: A Top-Down Approach to AI
  Transparency" — arXiv:2310.01405 — representation-space direction finding
- Belrose et al. (2023): "Eliciting Latent Knowledge from LLMs with Linear
  Probes" — ICLR 2024 — probing directions in activation space
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence


# ---------------------------------------------------------------------------
# Pure-Python vector helpers
# ---------------------------------------------------------------------------


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _norm(v: Sequence[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def _sub(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def _add(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def _scale(v: Sequence[float], s: float) -> list[float]:
    return [x * s for x in v]


def _normalize(v: Sequence[float]) -> list[float]:
    n = _norm(v)
    if n < 1e-12:
        return [0.0] * len(v)
    return [x / n for x in v]


def _euclidean(a: Sequence[float], b: Sequence[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def _cosine_sim(a: Sequence[float], b: Sequence[float]) -> float:
    na = _norm(a)
    nb = _norm(b)
    if na < 1e-12 or nb < 1e-12:
        return 0.0
    return _dot(a, b) / (na * nb)


def _mean_vec(vecs: list[list[float]]) -> list[float]:
    if not vecs:
        return []
    d = len(vecs[0])
    m = [0.0] * d
    for v in vecs:
        for i in range(d):
            m[i] += v[i]
    return [x / len(vecs) for x in m]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class AttenuationResult:
    """Result of a toxicity attenuation operation.

    Attributes:
        original_embedding: The unmodified embedding vector.
        attenuated_embedding: The embedding after toxicity direction removal.
        toxicity_direction: The unit direction that was removed.
        attenuation_strength: The alpha value used (strength of subtraction).
        residual_toxicity: Remaining projection onto toxicity direction after
            attenuation; ideally near zero.
        metadata: Optional extra diagnostics.
    """

    original_embedding: list[float]
    attenuated_embedding: list[float]
    toxicity_direction: list[float]
    attenuation_strength: float
    residual_toxicity: float
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------


class ToxicityAttenuator:
    """Probe safety classifiers via embedding-space toxicity attenuation.

    Identifies the principal ``toxicity direction'' — the vector separating
    safe-prompt embeddings from unsafe-prompt embeddings — and subtracts a
    scaled projection along that direction from the query embedding.  The
    attenuated embedding is then passed to the target model or safety
    classifier.

    This is a research probe for measuring the robustness of safety systems;
    it does **not** modify model weights or classifier parameters.

    Args:
        embed_fn: Callable mapping a text string to a list-of-float embedding.
        safe_prompts: Optional seed list of known-safe prompt strings used to
            pre-compute the safe centroid for ``find_toxicity_direction``.
        unsafe_prompts: Optional seed list of known-unsafe prompt strings used
            to pre-compute the unsafe centroid.

    Example::

        attenuator = ToxicityAttenuator(embed_fn=my_embedder)
        direction = attenuator.find_toxicity_direction(safe_embs, unsafe_embs)
        result = attenuator.attenuate(query_emb, direction, alpha=1.0)
        # result.attenuated_embedding has the toxicity component suppressed
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        safe_prompts: list[str] | None = None,
        unsafe_prompts: list[str] | None = None,
    ) -> None:
        self._embed_fn = embed_fn
        self._safe_prompts = safe_prompts or []
        self._unsafe_prompts = unsafe_prompts or []
        self._cached_direction: list[float] | None = None

    # -- direction finding --------------------------------------------------

    def find_toxicity_direction(
        self,
        safe_embeddings: list[list[float]],
        unsafe_embeddings: list[list[float]],
    ) -> list[float]:
        """Compute the normalised mean-difference toxicity direction.

        Follows Zhang et al. (2025) §3.1: the toxicity direction **t̂** is the
        unit vector pointing from the centroid of safe embeddings toward the
        centroid of unsafe embeddings::

            t̂ = normalise(μ_unsafe − μ_safe)

        Args:
            safe_embeddings: Embeddings of prompts that safety classifiers
                correctly accept.
            unsafe_embeddings: Embeddings of prompts that safety classifiers
                correctly reject.

        Returns:
            Normalised toxicity direction vector.

        Raises:
            ValueError: If either list is empty.
        """
        if not safe_embeddings:
            raise ValueError("safe_embeddings must be non-empty")
        if not unsafe_embeddings:
            raise ValueError("unsafe_embeddings must be non-empty")

        safe_centroid = _mean_vec(safe_embeddings)
        unsafe_centroid = _mean_vec(unsafe_embeddings)
        direction = _sub(unsafe_centroid, safe_centroid)
        self._cached_direction = _normalize(direction)
        return self._cached_direction

    # -- core attenuation ---------------------------------------------------

    def attenuate(
        self,
        embedding: list[float],
        direction: list[float],
        alpha: float = 1.0,
    ) -> AttenuationResult:
        """Remove the component of *embedding* along *direction*.

        Implements the attenuation formula from Zhang et al. (2025) §3.2::

            h' = h − α · (h · t̂) · t̂

        where **h** is the original embedding, **t̂** is the (unit) toxicity
        direction, and α ∈ [0, 2] controls the removal strength.

        Args:
            embedding: The query embedding to attenuate.
            direction: Unit toxicity direction (from
                :meth:`find_toxicity_direction`).
            alpha: Attenuation coefficient.  ``alpha=1.0`` fully removes the
                projection; ``alpha=2.0`` reverses it.

        Returns:
            :class:`AttenuationResult` with original and attenuated vectors.
        """
        unit_dir = _normalize(direction)
        projection = _dot(embedding, unit_dir)
        delta = _scale(unit_dir, alpha * projection)
        attenuated = _sub(embedding, delta)
        residual = self.compute_residual_toxicity(embedding, attenuated, unit_dir)
        return AttenuationResult(
            original_embedding=list(embedding),
            attenuated_embedding=attenuated,
            toxicity_direction=unit_dir,
            attenuation_strength=alpha,
            residual_toxicity=residual,
            metadata={"projection_before": projection},
        )

    def attenuate_prompt(
        self,
        prompt: str,
        alpha: float = 1.0,
    ) -> AttenuationResult:
        """Embed *prompt* then attenuate using the cached toxicity direction.

        Requires that :meth:`find_toxicity_direction` (or an explicit embed
        call that sets ``_cached_direction``) has been called first.

        Args:
            prompt: Raw text prompt to attenuate.
            alpha: Attenuation coefficient (see :meth:`attenuate`).

        Returns:
            :class:`AttenuationResult` for the embedded prompt.

        Raises:
            RuntimeError: If no toxicity direction has been computed yet.
        """
        if self._cached_direction is None:
            # Auto-build direction from seed prompts if available
            if self._safe_prompts and self._unsafe_prompts:
                safe_embs = [self._embed_fn(p) for p in self._safe_prompts]
                unsafe_embs = [self._embed_fn(p) for p in self._unsafe_prompts]
                self.find_toxicity_direction(safe_embs, unsafe_embs)
            else:
                raise RuntimeError(
                    "No toxicity direction computed.  Call find_toxicity_direction() first."
                )

        embedding = self._embed_fn(prompt)
        result = self.attenuate(embedding, self._cached_direction, alpha=alpha)
        result.metadata["prompt"] = prompt[:120]
        return result

    # -- alpha optimisation -------------------------------------------------

    def find_optimal_alpha(
        self,
        embedding: list[float],
        direction: list[float],
        score_fn: Callable[[list[float]], float],
        min_alpha: float = 0.0,
        max_alpha: float = 2.0,
        steps: int = 20,
    ) -> float:
        """Grid-search for the alpha that minimises the safety score.

        Evaluates *steps* evenly spaced alpha values in [min_alpha, max_alpha]
        and returns the one that yields the lowest safety score for the
        attenuated embedding, corresponding to the most effective attenuation
        of the safety signal.

        Args:
            embedding: Query embedding.
            direction: Toxicity direction (normalised).
            score_fn: Safety scoring function mapping an embedding to a float
                (higher = safer).
            min_alpha: Lower bound of the alpha search range.
            max_alpha: Upper bound of the alpha search range.
            steps: Number of grid points to evaluate.

        Returns:
            The alpha value that minimises *score_fn(attenuated_embedding)*.
        """
        unit_dir = _normalize(direction)
        best_alpha = min_alpha
        best_score = float("inf")
        step_size = (max_alpha - min_alpha) / max(steps - 1, 1)

        for i in range(steps):
            alpha = min_alpha + i * step_size
            projection = _dot(embedding, unit_dir)
            attenuated = _sub(embedding, _scale(unit_dir, alpha * projection))
            score = score_fn(attenuated)
            if score < best_score:
                best_score = score
                best_alpha = alpha

        return best_alpha

    # -- multi-direction attenuation ----------------------------------------

    def multi_dimension_attenuate(
        self,
        embedding: list[float],
        directions: list[list[float]],
        alphas: list[float],
    ) -> AttenuationResult:
        """Attenuate sequentially along multiple toxicity directions.

        Some safety classifiers use several orthogonal (or near-orthogonal)
        toxic subspace directions.  This method removes each in sequence.

        Args:
            embedding: The query embedding.
            directions: Ordered list of toxicity directions to remove.
            alphas: Per-direction attenuation coefficients.  Must have the
                same length as *directions*.

        Returns:
            :class:`AttenuationResult` reflecting the cumulative attenuation.
            The ``toxicity_direction`` field holds the *first* direction used.

        Raises:
            ValueError: If *directions* and *alphas* have different lengths.
        """
        if len(directions) != len(alphas):
            raise ValueError(
                f"directions ({len(directions)}) and alphas ({len(alphas)}) must match"
            )

        original = list(embedding)
        current = list(embedding)
        total_strength = 0.0

        for direction, alpha in zip(directions, alphas):
            unit_dir = _normalize(direction)
            projection = _dot(current, unit_dir)
            current = _sub(current, _scale(unit_dir, alpha * projection))
            total_strength += alpha

        primary_dir = _normalize(directions[0]) if directions else [0.0] * len(embedding)
        residual = self.compute_residual_toxicity(original, current, primary_dir)

        return AttenuationResult(
            original_embedding=original,
            attenuated_embedding=current,
            toxicity_direction=primary_dir,
            attenuation_strength=total_strength,
            residual_toxicity=residual,
            metadata={
                "n_directions": len(directions),
                "alphas": list(alphas),
            },
        )

    # -- residual measurement -----------------------------------------------

    def compute_residual_toxicity(
        self,
        original: list[float],
        attenuated: list[float],
        direction: list[float],
    ) -> float:
        """Measure how much toxicity signal remains in the attenuated embedding.

        Returns the dot product of the attenuated embedding with the (unit)
        toxicity direction.  A value close to zero indicates effective
        attenuation; a positive value means toxicity signal persists.

        Args:
            original: The original (unattenuated) embedding (unused in the
                dot product but retained for API symmetry and future metrics).
            attenuated: The embedding after attenuation.
            direction: The toxicity direction vector.

        Returns:
            Scalar residual projection value.
        """
        unit_dir = _normalize(direction)
        return _dot(attenuated, unit_dir)

    # -- batch operation ----------------------------------------------------

    def batch_attenuate(
        self,
        prompts: list[str],
        alpha: float = 1.0,
    ) -> list[AttenuationResult]:
        """Attenuate a list of prompts and return all results.

        Args:
            prompts: List of text prompts to embed and attenuate.
            alpha: Uniform attenuation coefficient for all prompts.

        Returns:
            List of :class:`AttenuationResult` in the same order as *prompts*.

        Raises:
            RuntimeError: If no toxicity direction is available (same condition
                as :meth:`attenuate_prompt`).
        """
        return [self.attenuate_prompt(p, alpha=alpha) for p in prompts]
