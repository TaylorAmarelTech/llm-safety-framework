"""
Latent space exploration for adversarial prompt discovery.

Operates on embedding vectors to find decision boundaries between safe/unsafe
classifications, interpolate between known prompts, walk along adversarial
gradient directions, and sample neighborhoods near safety boundaries.

This module works *without* access to model gradients — it uses embedding-space
geometry (cosine distance, centroids, interpolation) as a proxy for the model's
internal decision surface.

Sources:
- AutoDAN: "Generating Stealthy Jailbreak Prompts" (Liu et al., 2024)
- TAP: "Tree of Attacks with Pruning" (Mehrotra et al., 2024)
- "Latent Jailbreak" (Qiu et al., 2023) — embedding-space boundary probing
- GCG: "Universal and Transferable Adversarial Attacks" (Zou et al., 2023)
- Rainbow Teaming quality-diversity in embedding space (Samvelyan et al., 2024)
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Any, Sequence


# ---------------------------------------------------------------------------
# Lightweight linear-algebra helpers (no numpy at module level)
# ---------------------------------------------------------------------------

def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _norm(v: Sequence[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def _cosine(a: Sequence[float], b: Sequence[float]) -> float:
    na, nb = _norm(a), _norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return _dot(a, b) / (na * nb)


def _add(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def _sub(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def _scale(v: Sequence[float], s: float) -> list[float]:
    return [x * s for x in v]


def _normalize(v: Sequence[float]) -> list[float]:
    n = _norm(v)
    if n == 0:
        return [0.0] * len(v)
    return [x / n for x in v]


def _centroid(vecs: list[list[float]]) -> list[float]:
    if not vecs:
        return []
    dim = len(vecs[0])
    c = [0.0] * dim
    for v in vecs:
        for i in range(dim):
            c[i] += v[i]
    return [x / len(vecs) for x in c]


def _euclidean(a: Sequence[float], b: Sequence[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class BoundaryPoint:
    """A point on or near the estimated decision boundary."""
    vector: list[float]
    distance_to_safe: float = 0.0
    distance_to_unsafe: float = 0.0
    boundary_score: float = 0.0  # 0 = on boundary, higher = further away
    interpolation_alpha: float = 0.5
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AdversarialDirection:
    """A direction vector in embedding space that moves toward unsafe territory."""
    direction: list[float]
    magnitude: float = 0.0
    source_label: str = ""
    cosine_to_boundary: float = 0.0


@dataclass
class ExplorationResult:
    """Aggregated results of a latent-space exploration session."""
    boundary_points: list[BoundaryPoint]
    adversarial_directions: list[AdversarialDirection]
    safe_centroid: list[float]
    unsafe_centroid: list[float]
    boundary_width: float = 0.0
    suggested_vectors: list[list[float]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "n_boundary_points": len(self.boundary_points),
            "n_adversarial_directions": len(self.adversarial_directions),
            "boundary_width": round(self.boundary_width, 6),
            "n_suggested_vectors": len(self.suggested_vectors),
        }


# ---------------------------------------------------------------------------
# Main explorer
# ---------------------------------------------------------------------------


class LatentExplorer:
    """Explore the latent embedding space to find safety decision boundaries.

    All operations work on pre-computed embedding vectors (``list[float]``).
    Use ``Embedder`` to generate these from prompt strings before calling
    the explorer.
    """

    def __init__(self, distance_metric: str = "cosine"):
        self._metric = distance_metric

    def _distance(self, a: Sequence[float], b: Sequence[float]) -> float:
        if self._metric == "euclidean":
            return _euclidean(a, b)
        return 1.0 - _cosine(a, b)  # cosine distance

    # -- boundary estimation ------------------------------------------------

    def estimate_boundary(
        self,
        safe_vectors: list[list[float]],
        unsafe_vectors: list[list[float]],
        n_samples: int = 20,
    ) -> list[BoundaryPoint]:
        """Estimate the decision boundary by interpolating between safe / unsafe pairs.

        For each of *n_samples* random (safe, unsafe) pairs, performs binary
        search in embedding space to find the approximate crossing point.
        """
        if not safe_vectors or not unsafe_vectors:
            return []

        boundary_points: list[BoundaryPoint] = []
        for _ in range(n_samples):
            sv = random.choice(safe_vectors)
            uv = random.choice(unsafe_vectors)
            bp = self._binary_search_boundary(sv, uv, safe_vectors, unsafe_vectors)
            boundary_points.append(bp)

        return boundary_points

    def _binary_search_boundary(
        self,
        safe: list[float],
        unsafe: list[float],
        all_safe: list[list[float]],
        all_unsafe: list[list[float]],
        steps: int = 10,
    ) -> BoundaryPoint:
        """Binary search along the interpolation line to find the boundary."""
        safe_c = _centroid(all_safe)
        unsafe_c = _centroid(all_unsafe)

        lo, hi = 0.0, 1.0
        for _ in range(steps):
            mid = (lo + hi) / 2.0
            point = self.interpolate_vectors(safe, unsafe, mid)
            d_safe = self._distance(point, safe_c)
            d_unsafe = self._distance(point, unsafe_c)
            if d_safe < d_unsafe:
                lo = mid  # still in safe territory, move toward unsafe
            else:
                hi = mid  # in unsafe territory, move back

        alpha = (lo + hi) / 2.0
        vec = self.interpolate_vectors(safe, unsafe, alpha)
        d_s = self._distance(vec, safe_c)
        d_u = self._distance(vec, unsafe_c)

        return BoundaryPoint(
            vector=vec,
            distance_to_safe=d_s,
            distance_to_unsafe=d_u,
            boundary_score=abs(d_s - d_u),
            interpolation_alpha=alpha,
        )

    # -- interpolation ------------------------------------------------------

    def interpolate_vectors(
        self,
        vec_a: list[float],
        vec_b: list[float],
        alpha: float = 0.5,
    ) -> list[float]:
        """Linear interpolation: ``(1-alpha)*a + alpha*b``."""
        return _add(_scale(vec_a, 1.0 - alpha), _scale(vec_b, alpha))

    def slerp_interpolate(
        self,
        vec_a: list[float],
        vec_b: list[float],
        alpha: float = 0.5,
    ) -> list[float]:
        """Spherical linear interpolation (slerp).

        Preserves constant norm along the interpolation path, which is
        geometrically more faithful for embedding spaces where cosine
        similarity is the primary metric.
        """
        a_norm = _normalize(vec_a)
        b_norm = _normalize(vec_b)
        dot = max(-1.0, min(1.0, _dot(a_norm, b_norm)))
        omega = math.acos(dot)
        if omega < 1e-6:
            return self.interpolate_vectors(vec_a, vec_b, alpha)
        sin_omega = math.sin(omega)
        w_a = math.sin((1.0 - alpha) * omega) / sin_omega
        w_b = math.sin(alpha * omega) / sin_omega
        # Preserve average magnitude of inputs
        mag = (_norm(vec_a) * (1.0 - alpha) + _norm(vec_b) * alpha)
        result = _add(_scale(a_norm, w_a), _scale(b_norm, w_b))
        return _scale(result, mag)

    def slerp_path(
        self,
        vec_a: list[float],
        vec_b: list[float],
        steps: int = 10,
    ) -> list[list[float]]:
        """Generate a slerp-interpolated path between two vectors."""
        return [
            self.slerp_interpolate(vec_a, vec_b, i / max(steps - 1, 1))
            for i in range(steps)
        ]

    def interpolate_path(
        self,
        vec_a: list[float],
        vec_b: list[float],
        steps: int = 10,
    ) -> list[list[float]]:
        """Generate a path of *steps* evenly-spaced interpolated vectors."""
        return [
            self.interpolate_vectors(vec_a, vec_b, i / max(steps - 1, 1))
            for i in range(steps)
        ]

    # -- adversarial directions ---------------------------------------------

    def find_adversarial_direction(
        self,
        safe_vectors: list[list[float]],
        unsafe_vectors: list[list[float]],
    ) -> AdversarialDirection:
        """Compute the primary adversarial direction (safe centroid → unsafe centroid)."""
        safe_c = _centroid(safe_vectors)
        unsafe_c = _centroid(unsafe_vectors)
        direction = _sub(unsafe_c, safe_c)
        mag = _norm(direction)
        normed = _normalize(direction)
        return AdversarialDirection(
            direction=normed,
            magnitude=mag,
            source_label="centroid_direction",
            cosine_to_boundary=_cosine(direction, _sub(unsafe_c, safe_c)),
        )

    def find_diverse_adversarial_directions(
        self,
        safe_vectors: list[list[float]],
        unsafe_vectors: list[list[float]],
        n_directions: int = 5,
    ) -> list[AdversarialDirection]:
        """Find multiple adversarial directions by pairing safe/unsafe clusters.

        Uses k-farthest unsafe vectors from the safe centroid to create
        diverse attack directions.
        """
        if not safe_vectors or not unsafe_vectors:
            return []

        safe_c = _centroid(safe_vectors)
        # Rank unsafe by distance from safe centroid (farthest first for diversity)
        ranked = sorted(unsafe_vectors, key=lambda u: self._distance(safe_c, u), reverse=True)

        directions: list[AdversarialDirection] = []
        for i, uv in enumerate(ranked[:n_directions]):
            d = _sub(uv, safe_c)
            mag = _norm(d)
            directions.append(AdversarialDirection(
                direction=_normalize(d),
                magnitude=mag,
                source_label=f"diverse_direction_{i}",
            ))
        return directions

    # -- perturbation along direction ---------------------------------------

    def perturb_along_direction(
        self,
        origin: list[float],
        direction: AdversarialDirection,
        steps: int = 5,
        step_size: float = 0.1,
    ) -> list[list[float]]:
        """Walk from *origin* along *direction* in discrete steps.

        Returns *steps* vectors, each step_size further along.
        """
        results: list[list[float]] = []
        for i in range(1, steps + 1):
            vec = _add(origin, _scale(direction.direction, step_size * i))
            results.append(vec)
        return results

    # -- boundary neighborhood sampling -------------------------------------

    def sample_boundary_neighborhood(
        self,
        boundary_points: list[BoundaryPoint],
        radius: float = 0.05,
        n_per_point: int = 5,
    ) -> list[list[float]]:
        """Sample random vectors within *radius* of each boundary point.

        These are candidates for prompts that sit near the decision boundary
        and may confuse the classifier.
        """
        samples: list[list[float]] = []
        for bp in boundary_points:
            dim = len(bp.vector)
            for _ in range(n_per_point):
                noise = [random.gauss(0, radius) for _ in range(dim)]
                sample = _add(bp.vector, noise)
                samples.append(sample)
        return samples

    # -- nearest-boundary projection ----------------------------------------

    def project_to_nearest_boundary(
        self,
        vec: list[float],
        boundary_points: list[BoundaryPoint],
    ) -> BoundaryPoint | None:
        """Find the boundary point closest to *vec*."""
        if not boundary_points:
            return None
        return min(boundary_points, key=lambda bp: self._distance(vec, bp.vector))

    # -- full exploration workflow -------------------------------------------

    def explore(
        self,
        safe_vectors: list[list[float]],
        unsafe_vectors: list[list[float]],
        n_boundary_samples: int = 20,
        n_directions: int = 5,
        neighborhood_radius: float = 0.05,
        n_neighborhood_per_point: int = 3,
    ) -> ExplorationResult:
        """Run a full latent-space exploration.

        1. Estimate boundary via interpolation binary search.
        2. Find diverse adversarial directions.
        3. Sample boundary neighborhoods.
        4. Compute boundary width statistics.
        """
        boundary = self.estimate_boundary(safe_vectors, unsafe_vectors, n_boundary_samples)
        directions = self.find_diverse_adversarial_directions(
            safe_vectors, unsafe_vectors, n_directions,
        )
        suggested = self.sample_boundary_neighborhood(
            boundary, radius=neighborhood_radius, n_per_point=n_neighborhood_per_point,
        )

        safe_c = _centroid(safe_vectors)
        unsafe_c = _centroid(unsafe_vectors)

        # Boundary width: std-dev of boundary_score
        if boundary:
            scores = [bp.boundary_score for bp in boundary]
            mean_s = sum(scores) / len(scores)
            width = math.sqrt(sum((s - mean_s) ** 2 for s in scores) / len(scores))
        else:
            width = 0.0

        return ExplorationResult(
            boundary_points=boundary,
            adversarial_directions=directions,
            safe_centroid=safe_c,
            unsafe_centroid=unsafe_c,
            boundary_width=width,
            suggested_vectors=suggested,
        )

    # -- KNN classifier for improved boundary estimation ---------------------

    def knn_classify(
        self,
        point: list[float],
        safe_vectors: list[list[float]],
        unsafe_vectors: list[list[float]],
        k: int = 5,
    ) -> str:
        """Lightweight KNN classifier — returns ``"safe"`` or ``"unsafe"``.

        More accurate than the centroid-distance heuristic when clusters
        are non-spherical or have different spreads.
        """
        labeled = [(v, "safe") for v in safe_vectors] + [(v, "unsafe") for v in unsafe_vectors]
        dists = sorted(
            ((self._distance(point, v), label) for v, label in labeled),
            key=lambda x: x[0],
        )
        votes = [label for _, label in dists[:k]]
        return "safe" if votes.count("safe") >= votes.count("unsafe") else "unsafe"

    def estimate_boundary_knn(
        self,
        safe_vectors: list[list[float]],
        unsafe_vectors: list[list[float]],
        n_samples: int = 20,
        k: int = 5,
        steps: int = 12,
    ) -> list[BoundaryPoint]:
        """Boundary estimation using KNN classification instead of centroid distance.

        Binary-searches between safe/unsafe pairs using the KNN oracle
        to decide which side the midpoint is on.
        """
        if not safe_vectors or not unsafe_vectors:
            return []

        safe_c = _centroid(safe_vectors)
        unsafe_c = _centroid(unsafe_vectors)
        boundary_points: list[BoundaryPoint] = []

        for _ in range(n_samples):
            sv = random.choice(safe_vectors)
            uv = random.choice(unsafe_vectors)
            lo, hi = 0.0, 1.0
            for _ in range(steps):
                mid = (lo + hi) / 2.0
                point = self.interpolate_vectors(sv, uv, mid)
                label = self.knn_classify(point, safe_vectors, unsafe_vectors, k)
                if label == "safe":
                    lo = mid
                else:
                    hi = mid

            alpha = (lo + hi) / 2.0
            vec = self.interpolate_vectors(sv, uv, alpha)
            d_s = self._distance(vec, safe_c)
            d_u = self._distance(vec, unsafe_c)
            boundary_points.append(BoundaryPoint(
                vector=vec,
                distance_to_safe=d_s,
                distance_to_unsafe=d_u,
                boundary_score=abs(d_s - d_u),
                interpolation_alpha=alpha,
                metadata={"method": "knn", "k": k},
            ))

        return boundary_points

    # -- topology report ----------------------------------------------------

    def topology_report(
        self,
        exploration: ExplorationResult,
    ) -> dict[str, Any]:
        """Compute topology metrics from an exploration result.

        Returns boundary curvature, directional coverage, and sampling
        density recommendations.
        """
        bps = exploration.boundary_points
        dirs = exploration.adversarial_directions

        # Boundary curvature: variance of boundary point locations
        if len(bps) >= 2:
            centroid_bp = _centroid([bp.vector for bp in bps])
            dists_to_center = [_euclidean(bp.vector, centroid_bp) for bp in bps]
            mean_d = sum(dists_to_center) / len(dists_to_center)
            curvature = math.sqrt(
                sum((d - mean_d) ** 2 for d in dists_to_center) / len(dists_to_center)
            )
            alpha_range = max(bp.interpolation_alpha for bp in bps) - min(bp.interpolation_alpha for bp in bps)
        else:
            curvature = 0.0
            alpha_range = 0.0

        # Directional coverage: pairwise cosine between adversarial directions
        dir_cosines: list[float] = []
        for i, d1 in enumerate(dirs):
            for d2 in dirs[i + 1:]:
                dir_cosines.append(abs(_cosine(d1.direction, d2.direction)))
        avg_dir_similarity = sum(dir_cosines) / len(dir_cosines) if dir_cosines else 0.0
        # Low similarity = good directional diversity
        directional_diversity = 1.0 - avg_dir_similarity

        # Boundary tightness: mean of boundary_scores (0 = tight)
        boundary_scores = [bp.boundary_score for bp in bps]
        mean_tightness = sum(boundary_scores) / len(boundary_scores) if boundary_scores else 0.0

        return {
            "boundary_curvature": round(curvature, 6),
            "boundary_width": round(exploration.boundary_width, 6),
            "boundary_tightness": round(mean_tightness, 6),
            "alpha_range": round(alpha_range, 4),
            "n_boundary_points": len(bps),
            "directional_diversity": round(directional_diversity, 4),
            "n_directions": len(dirs),
            "avg_direction_magnitude": round(
                sum(d.magnitude for d in dirs) / len(dirs) if dirs else 0, 4
            ),
            "n_suggested_vectors": len(exploration.suggested_vectors),
            "recommended_follow_up": (
                "increase_boundary_samples" if len(bps) < 10
                else "increase_directions" if directional_diversity < 0.3
                else "sample_boundary_neighborhoods" if mean_tightness > 0.1
                else "sufficient_coverage"
            ),
        }

    # -- utility: find closest known vector ----------------------------------

    def find_nearest(
        self,
        target: list[float],
        candidates: list[list[float]],
        top_k: int = 5,
    ) -> list[tuple[int, float]]:
        """Return indices + distances of the *top_k* nearest candidates."""
        dists = [(i, self._distance(target, c)) for i, c in enumerate(candidates)]
        dists.sort(key=lambda t: t[1])
        return dists[:top_k]

    # -- utility: coverage map ----------------------------------------------

    def coverage_map(
        self,
        all_vectors: list[list[float]],
        grid_resolution: int = 10,
    ) -> dict[str, Any]:
        """Compute a 2D density map of embedding coverage.

        Projects to the first 2 principal components (via simple covariance
        trick) and bins into a grid.  Returns grid counts + total coverage.
        """
        if len(all_vectors) < 3:
            return {"error": "need >= 3 vectors", "grid": {}, "coverage": 0.0}

        # Simple 2D projection using the first two dimensions
        # (full PCA would need numpy; this is a lightweight fallback)
        dim = len(all_vectors[0])
        proj = [[v[0], v[1] if dim > 1 else 0.0] for v in all_vectors]

        xs = [p[0] for p in proj]
        ys = [p[1] for p in proj]
        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)
        x_range = x_max - x_min or 1.0
        y_range = y_max - y_min or 1.0

        grid: dict[str, int] = {}
        for x, y in proj:
            gx = min(int((x - x_min) / x_range * grid_resolution), grid_resolution - 1)
            gy = min(int((y - y_min) / y_range * grid_resolution), grid_resolution - 1)
            key = f"{gx},{gy}"
            grid[key] = grid.get(key, 0) + 1

        total_cells = grid_resolution * grid_resolution
        filled = len(grid)
        return {
            "grid": grid,
            "resolution": grid_resolution,
            "coverage": filled / total_cells,
            "filled_cells": filled,
            "total_cells": total_cells,
        }
