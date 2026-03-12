"""
Systematic embedding perturbation for adversarial boundary discovery.

Finds minimal perturbations in embedding space that cross safety decision
boundaries.  Implements random, directional, binary-search, PGD, and
HopSkipJump-inspired methods — all operating on embeddings without model
gradient access.

Sources:
- Goodfellow, Shlens & Szegedy (2015): "Explaining and Harnessing
  Adversarial Examples" — FGSM perturbation concept
- Madry et al. (2018): "Towards Deep Learning Models Resistant to
  Adversarial Attacks" — Projected Gradient Descent (PGD)
- Chen et al. (2020): "HopSkipJumpAttack: A Query-Efficient Decision-Based
  Attack" — boundary estimation from queries
- Carlini & Wagner (2017): "Towards Evaluating the Robustness of Neural
  Networks" — minimal perturbation search
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence


# ---------------------------------------------------------------------------
# Pure-Python vector helpers
# ---------------------------------------------------------------------------


def _add(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def _sub(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def _scale(v: Sequence[float], s: float) -> list[float]:
    return [x * s for x in v]


def _norm(v: Sequence[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def _normalize(v: Sequence[float]) -> list[float]:
    n = _norm(v)
    if n < 1e-12:
        return [0.0] * len(v)
    return [x / n for x in v]


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _random_unit(dim: int) -> list[float]:
    """Sample a random unit vector via Gaussian projection."""
    v = [random.gauss(0, 1) for _ in range(dim)]
    return _normalize(v)


def _clip_to_ball(v: Sequence[float], center: Sequence[float], epsilon: float) -> list[float]:
    """Project *v* onto the L2 ball of radius *epsilon* around *center*."""
    diff = _sub(v, center)
    n = _norm(diff)
    if n <= epsilon:
        return list(v)
    return _add(center, _scale(diff, epsilon / n))


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class PerturbationResult:
    """Result of a single perturbation experiment.

    Attributes:
        original_embedding: The starting embedding vector.
        perturbed_embedding: The perturbed embedding vector.
        original_score: Safety score of the original embedding.
        perturbed_score: Safety score after perturbation.
        perturbation_norm: L2 norm of the perturbation.
        direction: The perturbation direction (unit vector).
        success: Whether the perturbation crossed the decision boundary.
        metadata: Optional extra information.
    """

    original_embedding: list[float]
    perturbed_embedding: list[float]
    original_score: float = 0.0
    perturbed_score: float = 0.0
    perturbation_norm: float = 0.0
    direction: list[float] = field(default_factory=list)
    success: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Main perturber
# ---------------------------------------------------------------------------


class AdversarialPerturber:
    """Systematic embedding perturbation to find safety boundary crossings.

    Works with a *score_fn* that maps embeddings to safety scores.  The
    *threshold* separates safe (>= threshold) from unsafe (< threshold).
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]] | None = None,
        score_fn: Callable[[list[float]], float] | None = None,
        threshold: float = 0.5,
    ):
        self._embed_fn = embed_fn
        self._score_fn = score_fn or (lambda _: 0.5)
        self._threshold = threshold

    def _is_safe(self, score: float) -> bool:
        return score >= self._threshold

    # -- random perturbation ------------------------------------------------

    def perturb_random(
        self,
        embedding: list[float],
        epsilon: float = 0.1,
        n_tries: int = 20,
    ) -> list[PerturbationResult]:
        """Apply random unit perturbations scaled by epsilon.

        Each trial samples a random direction and applies epsilon * direction
        to the embedding, then scores the result.
        """
        dim = len(embedding)
        original_score = self._score_fn(embedding)
        results: list[PerturbationResult] = []

        for _ in range(n_tries):
            direction = _random_unit(dim)
            perturbed = _add(embedding, _scale(direction, epsilon))
            perturbed_score = self._score_fn(perturbed)
            crossed = self._is_safe(original_score) != self._is_safe(perturbed_score)

            results.append(PerturbationResult(
                original_embedding=embedding,
                perturbed_embedding=perturbed,
                original_score=original_score,
                perturbed_score=perturbed_score,
                perturbation_norm=epsilon,
                direction=direction,
                success=crossed,
            ))

        return results

    # -- directional perturbation -------------------------------------------

    def perturb_directional(
        self,
        embedding: list[float],
        direction: list[float],
        epsilon_range: tuple[float, float] = (0.01, 1.0),
        steps: int = 10,
    ) -> list[PerturbationResult]:
        """Step along a specific direction with varying epsilon.

        Evaluates the score at *steps* evenly spaced magnitudes along
        *direction* within *epsilon_range*.
        """
        original_score = self._score_fn(embedding)
        unit_dir = _normalize(direction)
        lo, hi = epsilon_range
        results: list[PerturbationResult] = []

        for i in range(steps):
            eps = lo + (hi - lo) * i / max(steps - 1, 1)
            perturbed = _add(embedding, _scale(unit_dir, eps))
            perturbed_score = self._score_fn(perturbed)
            crossed = self._is_safe(original_score) != self._is_safe(perturbed_score)

            results.append(PerturbationResult(
                original_embedding=embedding,
                perturbed_embedding=perturbed,
                original_score=original_score,
                perturbed_score=perturbed_score,
                perturbation_norm=eps,
                direction=unit_dir,
                success=crossed,
                metadata={"step": i, "epsilon": eps},
            ))

        return results

    # -- binary search for exact boundary -----------------------------------

    def binary_search_boundary(
        self,
        embedding: list[float],
        direction: list[float],
        lo: float = 0.0,
        hi: float = 2.0,
        tolerance: float = 0.001,
    ) -> PerturbationResult:
        """Binary search along *direction* to find the exact boundary crossing.

        Assumes the boundary exists between lo and hi magnitudes.
        """
        original_score = self._score_fn(embedding)
        original_safe = self._is_safe(original_score)
        unit_dir = _normalize(direction)

        for _ in range(50):  # max iterations
            if hi - lo < tolerance:
                break
            mid = (lo + hi) / 2.0
            perturbed = _add(embedding, _scale(unit_dir, mid))
            mid_score = self._score_fn(perturbed)
            if self._is_safe(mid_score) == original_safe:
                lo = mid
            else:
                hi = mid

        final_eps = (lo + hi) / 2.0
        perturbed = _add(embedding, _scale(unit_dir, final_eps))
        perturbed_score = self._score_fn(perturbed)

        return PerturbationResult(
            original_embedding=embedding,
            perturbed_embedding=perturbed,
            original_score=original_score,
            perturbed_score=perturbed_score,
            perturbation_norm=final_eps,
            direction=unit_dir,
            success=self._is_safe(original_score) != self._is_safe(perturbed_score),
            metadata={"method": "binary_search", "tolerance": tolerance},
        )

    # -- find minimal perturbation ------------------------------------------

    def find_minimal_perturbation(
        self,
        embedding: list[float],
        n_directions: int = 20,
        epsilon_range: tuple[float, float] = (0.01, 2.0),
    ) -> PerturbationResult:
        """Try many random directions, return the smallest successful perturbation.

        For each direction, performs a binary search to find the minimal
        epsilon that crosses the boundary.
        """
        dim = len(embedding)
        best: PerturbationResult | None = None

        for _ in range(n_directions):
            direction = _random_unit(dim)
            result = self.binary_search_boundary(
                embedding,
                direction,
                lo=epsilon_range[0],
                hi=epsilon_range[1],
            )
            if result.success:
                if best is None or result.perturbation_norm < best.perturbation_norm:
                    best = result

        if best is not None:
            return best

        # No crossing found — return the result with the largest score change
        original_score = self._score_fn(embedding)
        direction = _random_unit(dim)
        perturbed = _add(embedding, _scale(direction, epsilon_range[1]))
        perturbed_score = self._score_fn(perturbed)
        return PerturbationResult(
            original_embedding=embedding,
            perturbed_embedding=perturbed,
            original_score=original_score,
            perturbed_score=perturbed_score,
            perturbation_norm=epsilon_range[1],
            direction=direction,
            success=False,
            metadata={"method": "find_minimal", "status": "no_crossing_found"},
        )

    # -- HopSkipJump-inspired boundary estimation ---------------------------

    def hopskipjump(
        self,
        embedding: list[float],
        target_embedding: list[float],
        n_iterations: int = 20,
    ) -> list[PerturbationResult]:
        """HopSkipJump-inspired boundary estimation.

        Iteratively steps along the line from *embedding* toward
        *target_embedding*, using binary search to find the boundary
        at each iteration, then perturbing along the boundary surface.

        Inspired by Chen et al. (2020) but adapted for embedding-space
        black-box scoring.
        """
        dim = len(embedding)
        original_score = self._score_fn(embedding)
        results: list[PerturbationResult] = []

        current = list(embedding)

        for iteration in range(n_iterations):
            # Step 1: binary search along current→target to find boundary
            direction = _sub(target_embedding, current)
            d_norm = _norm(direction)
            if d_norm < 1e-12:
                break

            result = self.binary_search_boundary(
                current, direction, lo=0.0, hi=d_norm, tolerance=0.001,
            )
            results.append(PerturbationResult(
                original_embedding=embedding,
                perturbed_embedding=result.perturbed_embedding,
                original_score=original_score,
                perturbed_score=result.perturbed_score,
                perturbation_norm=_norm(_sub(result.perturbed_embedding, embedding)),
                direction=_normalize(direction),
                success=result.success,
                metadata={"method": "hopskipjump", "iteration": iteration},
            ))

            # Step 2: perturb along boundary (random orthogonal to direction)
            ortho = _random_unit(dim)
            proj = _dot(ortho, _normalize(direction))
            ortho = _sub(ortho, _scale(_normalize(direction), proj))
            ortho = _normalize(ortho)

            step_size = 0.05 * d_norm / (iteration + 1)
            current = _add(result.perturbed_embedding, _scale(ortho, step_size))

        return results

    # -- PGD in embedding space ---------------------------------------------

    def pgd_embedding(
        self,
        embedding: list[float],
        epsilon: float = 0.5,
        step_size: float = 0.05,
        n_steps: int = 20,
        directions: list[list[float]] | None = None,
    ) -> PerturbationResult:
        """Projected Gradient Descent in embedding space.

        Uses finite-difference gradient estimation (not model gradients)
        to iteratively step toward lower safety scores while staying within
        an L2 ball of radius *epsilon* around the original embedding.
        """
        dim = len(embedding)
        original_score = self._score_fn(embedding)
        current = list(embedding)
        delta = 1e-3  # finite difference step

        best_perturbed = list(current)
        best_score = original_score

        for step in range(n_steps):
            # Estimate gradient via finite differences
            if directions:
                grad_dirs = directions
            else:
                # Sample random directions for gradient estimation
                grad_dirs = [_random_unit(dim) for _ in range(min(dim, 20))]

            gradient = [0.0] * dim
            current_score = self._score_fn(current)

            for d in grad_dirs:
                perturbed_plus = _add(current, _scale(d, delta))
                score_plus = self._score_fn(perturbed_plus)
                # We want to *decrease* the score (move toward unsafe)
                grad_component = (score_plus - current_score) / delta
                gradient = _add(gradient, _scale(d, grad_component))

            # Normalize and step in *negative* gradient direction (minimize score)
            g_norm = _norm(gradient)
            if g_norm > 1e-12:
                gradient = _scale(gradient, 1.0 / g_norm)

            current = _sub(current, _scale(gradient, step_size))
            # Project back onto epsilon ball
            current = _clip_to_ball(current, embedding, epsilon)

            score = self._score_fn(current)
            if score < best_score:
                best_score = score
                best_perturbed = list(current)

        return PerturbationResult(
            original_embedding=embedding,
            perturbed_embedding=best_perturbed,
            original_score=original_score,
            perturbed_score=best_score,
            perturbation_norm=_norm(_sub(best_perturbed, embedding)),
            direction=_normalize(_sub(best_perturbed, embedding)),
            success=self._is_safe(original_score) != self._is_safe(best_score),
            metadata={"method": "pgd", "n_steps": n_steps, "epsilon": epsilon},
        )

    # -- sensitivity map ----------------------------------------------------

    def sensitivity_map(
        self,
        embedding: list[float],
        dim_range: tuple[int, int] | None = None,
    ) -> list[float]:
        """Compute per-dimension sensitivity of the score function.

        For each dimension, perturbs by a small delta and measures how much
        the score changes.  Returns absolute sensitivity per dimension.
        """
        dim = len(embedding)
        start, end = dim_range or (0, dim)
        start = max(0, start)
        end = min(dim, end)

        base_score = self._score_fn(embedding)
        delta = 1e-3
        sensitivities = [0.0] * dim

        for d in range(start, end):
            perturbed = list(embedding)
            perturbed[d] += delta
            score_plus = self._score_fn(perturbed)
            sensitivities[d] = abs(score_plus - base_score) / delta

        return sensitivities
