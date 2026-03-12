"""
Embedding-space poisoning via semantic shift to locate safety transition zones.

Models the safety decision boundary as a one-dimensional transition along a
semantic direction vector in embedding space.  Uses binary search and
narrow-window scanning to locate the critical epsilon where the model's
compliance score crosses 0.5 (the refusal-to-compliance transition).  Also
supports token-level selective poisoning by projecting token embeddings onto
the transition direction and targeting high-projection (high-risk) tokens.

Sources:
- Yuan et al. (2025): "Embedding Poisoning via Semantic Shift"
  (arXiv:2509.06338) — directional embedding perturbation for safety bypass
- Zou et al. (2023): "Universal and Transferable Adversarial Attacks on
  Aligned Language Models" — embedding-space attack directions
- Wallace et al. (2019): "Universal Adversarial Triggers for Attacking and
  Analyzing NLP" — token-level embedding manipulation
- Ebrahimi et al. (2018): "HotFlip: White-Box Adversarial Examples for
  Text Classification" — gradient-based token perturbation
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Callable, Sequence


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
    na, nb = _norm(a), _norm(b)
    if na < 1e-12 or nb < 1e-12:
        return 0.0
    return _dot(a, b) / (na * nb)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class PoisonResult:
    """Result of a single embedding poisoning operation.

    Attributes:
        original_embedding: The unperturbed input embedding.
        poisoned_embedding: The embedding after applying the directional poison.
        perturbation_magnitude: L2 norm of the applied perturbation (epsilon).
        transition_score: Estimated compliance score of the poisoned embedding
            (0.0 = definite refusal, 1.0 = definite compliance).
        semantic_preservation: Cosine similarity between original and poisoned
            embeddings (1.0 = semantically identical, 0.0 = orthogonal).
    """

    original_embedding: list[float]
    poisoned_embedding: list[float]
    perturbation_magnitude: float
    transition_score: float = 0.0
    semantic_preservation: float = 1.0


@dataclass
class TransitionModel:
    """Linear model of the safety score transition along a direction.

    Attributes:
        direction: Unit vector along which the transition was modelled.
        critical_epsilon: Estimated epsilon where the safety score crosses 0.5.
        transition_width: Estimated width of the transition zone (how sharply
            the boundary changes around the critical point).
    """

    direction: list[float]
    critical_epsilon: float
    transition_width: float = 0.1


# ---------------------------------------------------------------------------
# Main poisoner
# ---------------------------------------------------------------------------


class EmbeddingPoisoner:
    """Directional embedding perturbation to map the safety transition surface.

    Given a direction vector in embedding space (typically the normalized
    difference between unsafe and safe cluster centroids), this class:

    1. Moves embeddings along the direction by a controlled epsilon.
    2. Locates the critical epsilon via binary search or narrow-window scan.
    3. Fits a linear transition model to describe the decision boundary.
    4. Identifies high-risk tokens whose embeddings project strongly onto the
       transition direction (token-level selective poisoning).

    All operations are pure Python with no external dependencies.
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]] | None = None,
        score_fn: Callable[[list[float]], float] | None = None,
    ) -> None:
        """Initialize the embedding poisoner.

        Args:
            embed_fn: Optional callable mapping text strings to embedding vectors.
            score_fn: Optional callable mapping embedding vectors to a compliance
                score in [0, 1] where 1.0 means "will comply".  If None, a
                constant 0.5 stub is used.
        """
        self._embed_fn = embed_fn
        self._score_fn: Callable[[list[float]], float] = score_fn or (lambda _: 0.5)

    # -- direction estimation -----------------------------------------------

    def estimate_transition_direction(
        self,
        safe_centroid: Sequence[float],
        unsafe_centroid: Sequence[float],
    ) -> list[float]:
        """Compute the normalized direction from safe to unsafe centroid.

        This direction vector points from the cluster of refusing embeddings
        toward the cluster of complying embeddings.  Perturbing an embedding
        along this direction moves it toward unsafe space.

        Args:
            safe_centroid: Mean embedding of known-refusing texts.
            unsafe_centroid: Mean embedding of known-complying texts.

        Returns:
            Unit vector from safe centroid to unsafe centroid.
        """
        diff = _sub(unsafe_centroid, safe_centroid)
        return _normalize(diff)

    # -- linear transition model --------------------------------------------

    def model_linear_transition(
        self,
        embedding: Sequence[float],
        direction: Sequence[float],
        score_fn: Callable[[list[float]], float],
        n_samples: int = 20,
    ) -> TransitionModel:
        """Sample scores along the direction and fit a linear transition model.

        Samples ``n_samples`` evenly spaced epsilon values in [0, 2.0],
        evaluates the score function at each poisoned embedding, and finds
        the critical epsilon where the score first crosses 0.5.

        Args:
            embedding: Starting embedding vector.
            direction: Direction to move along (need not be unit).
            score_fn: Compliance score function mapping embeddings to [0, 1].
            n_samples: Number of sample points along the direction.

        Returns:
            TransitionModel describing the critical epsilon and transition width.
        """
        unit_dir = _normalize(direction)
        max_eps = 2.0
        scores: list[tuple[float, float]] = []  # (epsilon, score)

        for i in range(n_samples):
            eps = max_eps * i / max(n_samples - 1, 1)
            poisoned = self.poison_embedding(list(embedding), unit_dir, eps)
            score = score_fn(poisoned)
            scores.append((eps, score))

        # Find the crossing point where score crosses 0.5
        critical_eps = max_eps  # default if no crossing found
        prev_score = scores[0][1] if scores else 0.0

        for eps, score in scores[1:]:
            if prev_score < 0.5 <= score or prev_score >= 0.5 > score:
                critical_eps = eps
                break
            prev_score = score

        # Estimate transition width: range of epsilons where 0.3 < score < 0.7
        window_epsilons = [eps for eps, sc in scores if 0.3 < sc < 0.7]
        if len(window_epsilons) >= 2:
            width = max(window_epsilons) - min(window_epsilons)
        else:
            width = max_eps / n_samples  # one sample-step width

        return TransitionModel(
            direction=unit_dir,
            critical_epsilon=critical_eps,
            transition_width=width,
        )

    # -- embedding operations -----------------------------------------------

    def poison_embedding(
        self,
        embedding: Sequence[float],
        direction: Sequence[float],
        epsilon: float,
    ) -> list[float]:
        """Add epsilon * direction to the embedding.

        Implements the core poisoning operation::

            poisoned = embedding + epsilon * direction

        Args:
            embedding: Original embedding vector.
            direction: Perturbation direction (need not be unit).
            epsilon: Perturbation magnitude.

        Returns:
            New embedding list after applying the perturbation.
        """
        unit_dir = _normalize(direction)
        return _add(list(embedding), _scale(unit_dir, epsilon))

    # -- critical epsilon search --------------------------------------------

    def find_critical_epsilon(
        self,
        embedding: Sequence[float],
        direction: Sequence[float],
        score_fn: Callable[[list[float]], float],
        max_eps: float = 2.0,
        threshold: float = 0.5,
    ) -> float:
        """Binary search for epsilon where compliance score crosses threshold.

        Args:
            embedding: Starting embedding vector.
            direction: Direction to move along.
            score_fn: Compliance score function.
            max_eps: Upper bound on the epsilon search range.
            threshold: Score threshold to cross (default 0.5).

        Returns:
            Critical epsilon value.  Returns max_eps if no crossing found.
        """
        unit_dir = _normalize(direction)
        lo, hi = 0.0, max_eps
        base_score = score_fn(list(embedding))
        base_below = base_score < threshold

        # Verify that crossing exists
        hi_score = score_fn(self.poison_embedding(embedding, unit_dir, hi))
        if (hi_score < threshold) == base_below:
            # No crossing in range — return midpoint as best estimate
            return (lo + hi) / 2.0

        for _ in range(50):
            if hi - lo < 1e-4:
                break
            mid = (lo + hi) / 2.0
            mid_score = score_fn(self.poison_embedding(embedding, unit_dir, mid))
            if (mid_score < threshold) == base_below:
                lo = mid
            else:
                hi = mid

        return (lo + hi) / 2.0

    def narrow_window_search(
        self,
        embedding: Sequence[float],
        direction: Sequence[float],
        score_fn: Callable[[list[float]], float],
        epsilon_range: tuple[float, float] = (0.0, 2.0),
        resolution: int = 100,
    ) -> tuple[float, float]:
        """Find the narrow epsilon window where the safety transition occurs.

        Scans ``resolution`` evenly spaced epsilons and returns the
        ``(lower_bound, upper_bound)`` window where the score transitions
        from refusal to compliance (score < 0.5 → score >= 0.5).

        Args:
            embedding: Starting embedding.
            direction: Direction to scan along.
            score_fn: Compliance score function.
            epsilon_range: (lo, hi) bounds for the epsilon scan.
            resolution: Number of scan points.

        Returns:
            Tuple (window_lo, window_hi) bracketing the transition.  Returns
            the full epsilon_range if no transition is found.
        """
        unit_dir = _normalize(direction)
        lo_eps, hi_eps = epsilon_range
        prev_score: float | None = None
        transition_lo = lo_eps
        transition_hi = hi_eps

        for i in range(resolution):
            eps = lo_eps + (hi_eps - lo_eps) * i / max(resolution - 1, 1)
            poisoned = self.poison_embedding(embedding, unit_dir, eps)
            score = score_fn(poisoned)

            if prev_score is not None:
                if (prev_score < 0.5) != (score < 0.5):
                    step = (hi_eps - lo_eps) / max(resolution - 1, 1)
                    transition_lo = eps - step
                    transition_hi = eps
                    break

            prev_score = score

        return (transition_lo, transition_hi)

    # -- semantic preservation ----------------------------------------------

    def semantic_preservation_score(
        self,
        original_emb: Sequence[float],
        poisoned_emb: Sequence[float],
    ) -> float:
        """Cosine similarity between original and poisoned embeddings.

        A score of 1.0 means the poisoning preserved semantics perfectly;
        0.0 means the embeddings are orthogonal.

        Args:
            original_emb: The unperturbed embedding.
            poisoned_emb: The perturbed embedding.

        Returns:
            Cosine similarity in [-1, 1].
        """
        return _cosine_sim(original_emb, poisoned_emb)

    # -- token-level poisoning ----------------------------------------------

    def targeted_token_poison(
        self,
        prompt: str,
        target_tokens: list[str],
        embed_fn: Callable[[str], list[float]],
        direction: Sequence[float],
        epsilon: float,
    ) -> dict[str, object]:
        """Identify and rank high-risk tokens, report their projections.

        For each token in ``target_tokens``, computes how strongly its
        embedding projects onto the transition direction.  High-projection
        tokens are those whose perturbation would most move the prompt
        representation toward the unsafe region.

        Args:
            prompt: Original prompt text (used for context reporting).
            target_tokens: List of token strings to evaluate.
            embed_fn: Function mapping text to embedding vector.
            direction: Transition direction vector (unsafe - safe centroid).
            epsilon: Perturbation magnitude to apply per token.

        Returns:
            Dictionary with:
            - ``token_projections``: dict mapping token → projection magnitude.
            - ``ranked_tokens``: tokens sorted by projection (highest first).
            - ``poisoned_token_embeddings``: dict mapping token → perturbed emb.
            - ``high_risk_tokens``: tokens with projection above mean.
            - ``prompt``: the original prompt for reference.
        """
        unit_dir = _normalize(direction)
        projections: dict[str, float] = {}
        poisoned_embs: dict[str, list[float]] = {}

        for token in target_tokens:
            emb = embed_fn(token)
            projection = _dot(emb, unit_dir)
            projections[token] = projection
            poisoned_embs[token] = self.poison_embedding(emb, unit_dir, epsilon)

        ranked = sorted(projections.keys(), key=lambda t: projections[t], reverse=True)
        mean_proj = sum(projections.values()) / max(len(projections), 1)
        high_risk = [t for t in ranked if projections[t] > mean_proj]

        return {
            "token_projections": projections,
            "ranked_tokens": ranked,
            "poisoned_token_embeddings": poisoned_embs,
            "high_risk_tokens": high_risk,
            "prompt": prompt,
        }

    # -- batch operations ---------------------------------------------------

    def batch_poison(
        self,
        embeddings: list[list[float]],
        direction: Sequence[float],
        epsilon: float,
    ) -> list[PoisonResult]:
        """Apply the same directional poison to a batch of embeddings.

        Args:
            embeddings: List of embedding vectors to poison.
            direction: Shared transition direction.
            epsilon: Perturbation magnitude applied to all embeddings.

        Returns:
            List of PoisonResult objects, one per input embedding.
        """
        unit_dir = _normalize(direction)
        results: list[PoisonResult] = []

        for emb in embeddings:
            poisoned = self.poison_embedding(emb, unit_dir, epsilon)
            score = self._score_fn(poisoned)
            preservation = self.semantic_preservation_score(emb, poisoned)
            mag = _euclidean(emb, poisoned)

            results.append(PoisonResult(
                original_embedding=list(emb),
                poisoned_embedding=poisoned,
                perturbation_magnitude=mag,
                transition_score=score,
                semantic_preservation=preservation,
            ))

        return results
