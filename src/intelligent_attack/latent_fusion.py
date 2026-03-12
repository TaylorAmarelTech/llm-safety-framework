"""
Latent fusion jailbreak: blending harmful and benign embeddings to bypass safety.

Implements the Latent Fusion Jailbreak from Xing et al. (2025): rather than
operating on raw text, the attack blends the *embeddings* of a harmful prompt and
a benign "cover" prompt in a ratio that preserves semantic decodability while
evading safety classifiers that operate in the same embedding space.

The intuition is that safety classifiers draw a boundary in embedding space, and
by interpolating toward the benign side the query can cross that boundary while
still carrying enough harmful signal to elicit a useful completion.

Used in this framework to measure how sharply a model's latent safety boundary
separates safe and unsafe content, and whether blended queries can bridge it.

Sources:
- Xing et al. (2025): "Latent Fusion Jailbreak" — arXiv:2508.10029 — main
  algorithm, linear and spherical fusion approaches
- Shoemake (1985): "Animating Rotation with Quaternion Curves" — SIGGRAPH 1985 —
  spherical linear interpolation (Slerp) foundation
- Perez et al. (2022): "Ignore Previous Prompt: Attack Techniques For Language
  Models" — arXiv:2211.09527 — early embedding manipulation context
- Wei et al. (2024): "Jailbroken: How Does LLM Safety Training Fail?" — NeurIPS
  2024 — competing objectives in safety training
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


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class FusionResult:
    """Result of a latent fusion operation.

    Attributes:
        harmful_embedding: The embedding of the harmful prompt.
        benign_embedding: The embedding of the benign cover prompt.
        fused_embedding: The interpolated embedding used as the query.
        blend_alpha: Blend coefficient (0 = fully benign, 1 = fully harmful).
        fusion_method: Name of the fusion method used (``"linear"``,
            ``"spherical"``, ``"geodesic"``).
        safety_score_estimate: Optional safety score for the fused embedding,
            populated when a *score_fn* is available.
        metadata: Additional diagnostic information.
    """

    harmful_embedding: list[float]
    benign_embedding: list[float]
    fused_embedding: list[float]
    blend_alpha: float
    fusion_method: str
    safety_score_estimate: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------


class LatentFuser:
    """Blend harmful and benign embeddings to probe latent safety boundaries.

    Provides linear, spherical (Slerp), and geodesic interpolation methods
    plus utilities for finding the critical blend alpha at which a safety
    classifier flips its verdict.

    Args:
        embed_fn: Callable mapping a text string to a list-of-float embedding.
        score_fn: Optional safety scoring function mapping an embedding to a
            float (higher = safer).  Required for :meth:`find_critical_alpha`
            and :meth:`evaluate_fusion`.

    Example::

        fuser = LatentFuser(embed_fn=my_embedder, score_fn=my_scorer)
        result = fuser.fuse_prompt(
            "How do I ...",   # harmful
            "Tell me about chemistry in general",   # benign cover
            alpha=0.4,
            method="spherical",
        )
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        score_fn: Callable[[list[float]], float] | None = None,
    ) -> None:
        self._embed_fn = embed_fn
        self._score_fn = score_fn

    # -- interpolation methods ----------------------------------------------

    def linear_fuse(
        self,
        harmful_emb: list[float],
        benign_emb: list[float],
        alpha: float = 0.5,
    ) -> list[float]:
        """Linear (convex) interpolation between harmful and benign embeddings.

        Computes ``α · H + (1 − α) · B`` where H is the harmful embedding and
        B is the benign embedding.  At ``alpha=0`` the result is fully benign;
        at ``alpha=1`` it is fully harmful.

        Args:
            harmful_emb: Embedding of the harmful prompt.
            benign_emb: Embedding of the benign cover prompt.
            alpha: Blend coefficient in [0, 1].

        Returns:
            Interpolated embedding vector.
        """
        alpha = max(0.0, min(1.0, alpha))
        return _add(_scale(harmful_emb, alpha), _scale(benign_emb, 1.0 - alpha))

    def spherical_fuse(
        self,
        harmful_emb: list[float],
        benign_emb: list[float],
        t: float = 0.5,
    ) -> list[float]:
        """Spherical linear interpolation (Slerp) between unit vectors.

        Projects both embeddings onto the unit sphere, computes the angle
        between them (ω), then interpolates along the great-circle arc::

            Slerp(A, B, t) = sin((1-t)·ω)/sin(ω) · A + sin(t·ω)/sin(ω) · B

        where ``t=0`` gives the normalised harmful direction and ``t=1`` gives
        the normalised benign direction (following Xing et al.'s framing where
        t → 1 moves toward the safe side).

        Falls back to linear interpolation when the vectors are nearly parallel
        or anti-parallel.

        Args:
            harmful_emb: Embedding of the harmful prompt.
            benign_emb: Embedding of the benign cover prompt.
            t: Interpolation parameter in [0, 1].  ``t=0`` ≈ harmful,
                ``t=1`` ≈ benign.

        Returns:
            Slerp-interpolated unit vector (re-scaled to average norm).
        """
        t = max(0.0, min(1.0, t))
        A = _normalize(harmful_emb)
        B = _normalize(benign_emb)

        cos_omega = _cosine_sim(A, B)
        # Clamp to avoid acos domain errors due to floating-point noise
        cos_omega = max(-1.0, min(1.0, cos_omega))

        if abs(cos_omega) > 1.0 - 1e-6:
            # Vectors are nearly parallel or anti-parallel; fall back to linear
            return self.linear_fuse(A, B, alpha=1.0 - t)

        omega = math.acos(cos_omega)
        sin_omega = math.sin(omega)
        coeff_a = math.sin((1.0 - t) * omega) / sin_omega
        coeff_b = math.sin(t * omega) / sin_omega

        return _add(_scale(A, coeff_a), _scale(B, coeff_b))

    def geodesic_fuse(
        self,
        harmful_emb: list[float],
        benign_emb: list[float],
        t: float = 0.5,
    ) -> list[float]:
        """Slerp on the unit sphere, then restore the average embedding norm.

        Unlike :meth:`spherical_fuse`, which returns a unit vector, this method
        scales the output to the mean of the two input norms, preserving the
        overall magnitude distribution expected by downstream models.

        Args:
            harmful_emb: Embedding of the harmful prompt.
            benign_emb: Embedding of the benign cover prompt.
            t: Interpolation parameter (0 = harmful side, 1 = benign side).

        Returns:
            Slerp-interpolated embedding at average norm.
        """
        avg_norm = (_norm(harmful_emb) + _norm(benign_emb)) / 2.0
        unit_result = self.spherical_fuse(harmful_emb, benign_emb, t=t)
        result_norm = _norm(unit_result)
        if result_norm < 1e-12:
            return list(unit_result)
        return _scale(unit_result, avg_norm / result_norm)

    def multi_benign_fuse(
        self,
        harmful_emb: list[float],
        benign_embs: list[list[float]],
        weights: list[float] | None = None,
    ) -> list[float]:
        """Fuse one harmful embedding with a weighted mixture of benign embeddings.

        Constructs a single composite benign vector as the weighted average of
        *benign_embs*, then performs linear fusion with the harmful embedding
        at alpha=0.5.

        Args:
            harmful_emb: Embedding of the harmful prompt.
            benign_embs: List of benign cover embeddings.
            weights: Optional weights for each benign embedding.  Uniform if
                omitted.  Will be normalised to sum to 1.

        Returns:
            Fused embedding vector.

        Raises:
            ValueError: If *benign_embs* is empty.
        """
        if not benign_embs:
            raise ValueError("benign_embs must contain at least one embedding")

        n = len(benign_embs)
        if weights is None:
            weights = [1.0 / n] * n
        else:
            total = sum(weights)
            weights = [w / max(total, 1e-12) for w in weights]

        d = len(benign_embs[0])
        composite_benign = [0.0] * d
        for emb, w in zip(benign_embs, weights):
            for i in range(d):
                composite_benign[i] += w * emb[i]

        return self.linear_fuse(harmful_emb, composite_benign, alpha=0.5)

    # -- critical alpha search ----------------------------------------------

    def find_critical_alpha(
        self,
        harmful_emb: list[float],
        benign_emb: list[float],
        score_fn: Callable[[list[float]], float],
        method: str = "linear",
        n_steps: int = 50,
    ) -> float:
        """Binary-search for the alpha at which the safety classifier flips.

        Scans alpha from 0.0 (fully benign) to 1.0 (fully harmful), evaluating
        the safety score at each point.  Returns the smallest alpha at which the
        score crosses the midpoint (0.5), i.e. where the classifier transitions
        from "safe" to "unsafe".

        Args:
            harmful_emb: Embedding of the harmful prompt.
            benign_emb: Embedding of the benign cover prompt.
            score_fn: Safety scorer (higher = safer).
            method: Fusion method to use (``"linear"`` or ``"spherical"``).
            n_steps: Grid resolution for the initial scan.

        Returns:
            Critical alpha value in [0, 1]; 1.0 if no crossing is found.
        """
        fuse_fn = self.linear_fuse if method == "linear" else self.spherical_fuse

        # Coarse scan to bracket the crossing
        threshold = 0.5
        prev_score: float | None = None
        prev_alpha = 0.0

        for i in range(n_steps + 1):
            alpha = i / n_steps
            fused = fuse_fn(harmful_emb, benign_emb, alpha)
            score = score_fn(fused)

            if prev_score is not None and ((prev_score >= threshold) != (score >= threshold)):
                # Crossing is between prev_alpha and alpha — bisect
                lo, hi = prev_alpha, alpha
                for _ in range(30):
                    mid = (lo + hi) / 2.0
                    mid_emb = fuse_fn(harmful_emb, benign_emb, mid)
                    mid_score = score_fn(mid_emb)
                    if (mid_score >= threshold) == (prev_score >= threshold):
                        lo = mid
                    else:
                        hi = mid
                return (lo + hi) / 2.0

            prev_score = score
            prev_alpha = alpha

        return 1.0  # no crossing found

    # -- high-level API -----------------------------------------------------

    def fuse_prompt(
        self,
        harmful_text: str,
        benign_text: str,
        alpha: float = 0.5,
        method: str = "linear",
    ) -> FusionResult:
        """Embed both texts and return a :class:`FusionResult`.

        Args:
            harmful_text: The harmful prompt string.
            benign_text: The benign cover prompt string.
            alpha: Blend coefficient (0 = fully benign, 1 = fully harmful).
            method: One of ``"linear"``, ``"spherical"``, ``"geodesic"``.

        Returns:
            :class:`FusionResult` with all intermediate and final embeddings.

        Raises:
            ValueError: If *method* is not recognised.
        """
        harmful_emb = self._embed_fn(harmful_text)
        benign_emb = self._embed_fn(benign_text)

        if method == "linear":
            fused = self.linear_fuse(harmful_emb, benign_emb, alpha=alpha)
        elif method == "spherical":
            fused = self.spherical_fuse(harmful_emb, benign_emb, t=1.0 - alpha)
        elif method == "geodesic":
            fused = self.geodesic_fuse(harmful_emb, benign_emb, t=1.0 - alpha)
        else:
            raise ValueError(f"Unknown fusion method: {method!r}")

        safety_score = 0.0
        if self._score_fn is not None:
            safety_score = self._score_fn(fused)

        return FusionResult(
            harmful_embedding=harmful_emb,
            benign_embedding=benign_emb,
            fused_embedding=fused,
            blend_alpha=alpha,
            fusion_method=method,
            safety_score_estimate=safety_score,
            metadata={
                "harmful_text": harmful_text[:120],
                "benign_text": benign_text[:120],
            },
        )

    # -- evaluation ---------------------------------------------------------

    def evaluate_fusion(
        self,
        result: FusionResult,
        score_fn: Callable[[list[float]], float],
    ) -> dict[str, float]:
        """Compute diagnostic metrics for a fusion result.

        Metrics returned:

        * ``safety_score`` — score of the fused embedding.
        * ``distance_to_harmful`` — Euclidean distance from fused to harmful.
        * ``distance_to_benign`` — Euclidean distance from fused to benign.
        * ``angular_distance`` — Angular distance (in radians) from fused to
          harmful embedding.
        * ``harmful_score`` — score of the original harmful embedding.
        * ``benign_score`` — score of the original benign embedding.

        Args:
            result: A :class:`FusionResult` to evaluate.
            score_fn: Safety scoring function.

        Returns:
            Dict mapping metric names to float values.
        """
        fused = result.fused_embedding
        harmful = result.harmful_embedding
        benign = result.benign_embedding

        safety_score = score_fn(fused)
        harmful_score = score_fn(harmful)
        benign_score = score_fn(benign)
        dist_harmful = _euclidean(fused, harmful)
        dist_benign = _euclidean(fused, benign)

        cos_to_harmful = _cosine_sim(fused, harmful)
        cos_to_harmful = max(-1.0, min(1.0, cos_to_harmful))
        angular_dist = math.acos(cos_to_harmful)

        return {
            "safety_score": safety_score,
            "distance_to_harmful": dist_harmful,
            "distance_to_benign": dist_benign,
            "angular_distance": angular_dist,
            "harmful_score": harmful_score,
            "benign_score": benign_score,
        }
