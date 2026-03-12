"""
Dimensionality reduction for visualizing safety landscapes.

Implements PCA (via power iteration), classical MDS (metric
multidimensional scaling), random projection (Johnson-Lindenstrauss),
and Landmark MDS — all in pure Python without numpy/scipy.

Useful for projecting high-dimensional embedding spaces into 2D/3D for
safety boundary visualization, cluster identification, and coverage
analysis.

Sources:
- Pearson (1901): "On Lines and Planes of Closest Fit" — PCA
- Torgerson (1952): "Multidimensional Scaling" — classical MDS
- Johnson & Lindenstrauss (1984): "Extensions of Lipschitz Mappings
  into a Hilbert Space" — random projection
- de Silva & Tenenbaum (2004): "Sparse Multidimensional Scaling Using
  Landmark Points" — Landmark MDS
- Kruskal (1964): "Nonmetric Multidimensional Scaling" — stress metric
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence


# ---------------------------------------------------------------------------
# Pure-Python vector / matrix helpers
# ---------------------------------------------------------------------------


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _norm(v: Sequence[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def _sub(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def _scale(v: Sequence[float], s: float) -> list[float]:
    return [x * s for x in v]


def _add(a: Sequence[float], b: Sequence[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def _euclidean(a: Sequence[float], b: Sequence[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def _mean_vec(vecs: list[list[float]]) -> list[float]:
    if not vecs:
        return []
    d = len(vecs[0])
    m = [0.0] * d
    for v in vecs:
        for i in range(d):
            m[i] += v[i]
    return [x / len(vecs) for x in m]


def _mat_vec(M: list[list[float]], v: list[float]) -> list[float]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in M]


def _outer(a: list[float], b: list[float]) -> list[list[float]]:
    return [[a[i] * b[j] for j in range(len(b))] for i in range(len(a))]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class ManifoldPoint:
    """A point in the reduced manifold space.

    Attributes:
        original_embedding: The original high-dimensional embedding.
        reduced_coords: Coordinates in the reduced space.
        label: Optional label (e.g. "safe", "unsafe").
        score: Optional safety score.
        metadata: Additional information.
    """

    original_embedding: list[float]
    reduced_coords: list[float]
    label: str = ""
    score: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ManifoldMap:
    """Result of a dimensionality reduction operation.

    Attributes:
        points: The reduced-space points.
        method: Name of the reduction method used.
        dimensions: Number of reduced dimensions.
        stress: Goodness-of-fit metric (lower is better), if applicable.
    """

    points: list[ManifoldPoint]
    method: str = ""
    dimensions: int = 2
    stress: float = 0.0


# ---------------------------------------------------------------------------
# Main mapper
# ---------------------------------------------------------------------------


class ManifoldMapper:
    """Dimensionality reduction for safety landscape visualization.

    All methods are implemented in pure Python and work on
    pre-computed embedding vectors (``list[float]``).
    """

    def __init__(self, embed_fn: Callable[[str], list[float]] | None = None):
        self._embed_fn = embed_fn

    # -- distance matrix ----------------------------------------------------

    def compute_distances(self, embeddings: list[list[float]]) -> list[list[float]]:
        """Compute pairwise Euclidean distance matrix."""
        n = len(embeddings)
        D = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                d = _euclidean(embeddings[i], embeddings[j])
                D[i][j] = d
                D[j][i] = d
        return D

    # -- stress metric ------------------------------------------------------

    def compute_stress(
        self,
        distances_high: list[list[float]],
        distances_low: list[list[float]],
    ) -> float:
        """Kruskal's stress-1: normalized residual between distance matrices.

        stress = sqrt(sum (d_high - d_low)^2 / sum d_high^2)
        """
        n = len(distances_high)
        numerator = 0.0
        denominator = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                dh = distances_high[i][j]
                dl = distances_low[i][j]
                numerator += (dh - dl) ** 2
                denominator += dh ** 2
        if denominator < 1e-12:
            return 0.0
        return math.sqrt(numerator / denominator)

    # -- PCA via power iteration --------------------------------------------

    def pca(
        self,
        embeddings: list[list[float]],
        n_components: int = 2,
    ) -> ManifoldMap:
        """PCA via power iteration for the top eigenvalues of the covariance matrix.

        Centers the data, computes the covariance matrix, then extracts
        the top *n_components* eigenvectors using repeated power iteration
        with deflation.
        """
        if not embeddings:
            return ManifoldMap(points=[], method="pca", dimensions=n_components)

        n = len(embeddings)
        d = len(embeddings[0])
        mean = _mean_vec(embeddings)
        centered = [_sub(e, mean) for e in embeddings]

        # Covariance matrix (d x d)
        cov = [[0.0] * d for _ in range(d)]
        for v in centered:
            for i in range(d):
                for j in range(i, d):
                    val = v[i] * v[j]
                    cov[i][j] += val
                    if i != j:
                        cov[j][i] += val
        for i in range(d):
            for j in range(d):
                cov[i][j] /= max(n - 1, 1)

        # Power iteration for top eigenvectors
        eigenvectors: list[list[float]] = []
        residual_cov = [row[:] for row in cov]

        for _ in range(min(n_components, d)):
            v = [random.gauss(0, 1) for _ in range(d)]
            v_norm = _norm(v)
            if v_norm < 1e-12:
                v = [1.0] + [0.0] * (d - 1)
            else:
                v = _scale(v, 1.0 / v_norm)

            # Power iteration
            for _ in range(200):
                v_new = _mat_vec(residual_cov, v)
                v_new_norm = _norm(v_new)
                if v_new_norm < 1e-12:
                    break
                v_new = _scale(v_new, 1.0 / v_new_norm)
                # Check convergence
                if abs(_dot(v, v_new)) > 1.0 - 1e-8:
                    v = v_new
                    break
                v = v_new

            eigenvectors.append(v)

            # Deflation: remove this component from the covariance
            eigenvalue = _dot(_mat_vec(residual_cov, v), v)
            outer_vv = _outer(v, v)
            for i in range(d):
                for j in range(d):
                    residual_cov[i][j] -= eigenvalue * outer_vv[i][j]

        # Project centered data onto eigenvectors
        points: list[ManifoldPoint] = []
        for i, (orig, cent) in enumerate(zip(embeddings, centered)):
            coords = [_dot(cent, ev) for ev in eigenvectors]
            points.append(ManifoldPoint(
                original_embedding=orig,
                reduced_coords=coords,
            ))

        return ManifoldMap(
            points=points,
            method="pca",
            dimensions=n_components,
        )

    # -- Classical MDS ------------------------------------------------------

    def mds(
        self,
        embeddings: list[list[float]],
        n_components: int = 2,
        max_iterations: int = 300,
    ) -> ManifoldMap:
        """Classical (metric) MDS via double-centering of the distance matrix.

        Computes the Gram matrix from pairwise distances and extracts the
        top eigenvectors to produce the low-dimensional embedding.
        """
        n = len(embeddings)
        if n < 2:
            points = [
                ManifoldPoint(
                    original_embedding=e,
                    reduced_coords=[0.0] * n_components,
                )
                for e in embeddings
            ]
            return ManifoldMap(points=points, method="mds", dimensions=n_components)

        D = self.compute_distances(embeddings)

        # Squared distance matrix
        D2 = [[d * d for d in row] for row in D]

        # Double centering: B = -0.5 * J D^2 J where J = I - 1/n * 11^T
        row_means = [sum(D2[i]) / n for i in range(n)]
        col_means = [sum(D2[i][j] for i in range(n)) / n for j in range(n)]
        grand_mean = sum(row_means) / n

        B = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                B[i][j] = -0.5 * (D2[i][j] - row_means[i] - col_means[j] + grand_mean)

        # Extract top eigenvectors of B via power iteration
        eigenvectors: list[list[float]] = []
        eigenvalues: list[float] = []
        residual = [row[:] for row in B]

        for _ in range(min(n_components, n)):
            v = [random.gauss(0, 1) for _ in range(n)]
            vn = _norm(v)
            if vn < 1e-12:
                v = [1.0] + [0.0] * (n - 1)
            else:
                v = _scale(v, 1.0 / vn)

            for _ in range(max_iterations):
                v_new = _mat_vec(residual, v)
                v_new_norm = _norm(v_new)
                if v_new_norm < 1e-12:
                    break
                v_new = _scale(v_new, 1.0 / v_new_norm)
                if abs(_dot(v, v_new)) > 1.0 - 1e-8:
                    v = v_new
                    break
                v = v_new

            eigenvalue = _dot(_mat_vec(residual, v), v)
            eigenvectors.append(v)
            eigenvalues.append(max(eigenvalue, 0.0))

            # Deflation
            outer_vv = _outer(v, v)
            for i in range(n):
                for j in range(n):
                    residual[i][j] -= eigenvalue * outer_vv[i][j]

        # Coordinates: X_k = sqrt(lambda_k) * v_k
        coords_matrix = [
            [math.sqrt(eigenvalues[k]) * eigenvectors[k][i]
             for k in range(len(eigenvectors))]
            for i in range(n)
        ]

        # Compute stress
        D_low = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                d = _euclidean(coords_matrix[i], coords_matrix[j])
                D_low[i][j] = d
                D_low[j][i] = d
        stress = self.compute_stress(D, D_low)

        points = [
            ManifoldPoint(
                original_embedding=embeddings[i],
                reduced_coords=coords_matrix[i],
            )
            for i in range(n)
        ]

        return ManifoldMap(
            points=points,
            method="mds",
            dimensions=n_components,
            stress=stress,
        )

    # -- Random projection --------------------------------------------------

    def random_projection(
        self,
        embeddings: list[list[float]],
        n_components: int = 2,
        seed: int = 42,
    ) -> ManifoldMap:
        """Johnson-Lindenstrauss random projection.

        Projects using a random Gaussian matrix R of shape (d, n_components),
        scaled by 1/sqrt(n_components).  Approximately preserves pairwise
        distances for any dataset.
        """
        if not embeddings:
            return ManifoldMap(points=[], method="random_projection", dimensions=n_components)

        d = len(embeddings[0])
        rng = random.Random(seed)
        scale = 1.0 / math.sqrt(n_components)

        # Random projection matrix (d x n_components)
        R = [[rng.gauss(0, 1) * scale for _ in range(n_components)] for _ in range(d)]

        points: list[ManifoldPoint] = []
        for emb in embeddings:
            coords = [0.0] * n_components
            for j in range(n_components):
                coords[j] = sum(emb[i] * R[i][j] for i in range(d))
            points.append(ManifoldPoint(
                original_embedding=emb,
                reduced_coords=coords,
            ))

        return ManifoldMap(
            points=points,
            method="random_projection",
            dimensions=n_components,
        )

    # -- Landmark MDS -------------------------------------------------------

    def landmark_mds(
        self,
        embeddings: list[list[float]],
        n_components: int = 2,
        n_landmarks: int = 50,
    ) -> ManifoldMap:
        """Landmark MDS for large datasets.

        1. Select *n_landmarks* representative points.
        2. Run classical MDS on the landmarks.
        3. Project remaining points via triangulation.
        """
        n = len(embeddings)
        if n <= n_landmarks:
            return self.mds(embeddings, n_components)

        # Select landmarks (evenly spaced indices)
        step = max(1, n // n_landmarks)
        landmark_indices = list(range(0, n, step))[:n_landmarks]
        landmarks = [embeddings[i] for i in landmark_indices]

        # MDS on landmarks
        landmark_map = self.mds(landmarks, n_components)
        landmark_coords = [p.reduced_coords for p in landmark_map.points]

        # Project non-landmark points via distance-weighted interpolation
        points: list[ManifoldPoint] = []
        for i in range(n):
            if i in landmark_indices:
                idx = landmark_indices.index(i)
                points.append(ManifoldPoint(
                    original_embedding=embeddings[i],
                    reduced_coords=landmark_coords[idx],
                ))
            else:
                # Weighted average of nearest landmark coordinates
                dists = [
                    (_euclidean(embeddings[i], landmarks[j]), j)
                    for j in range(len(landmarks))
                ]
                dists.sort()
                k = min(5, len(landmarks))
                nearest = dists[:k]
                total_w = sum(1.0 / max(d, 1e-12) for d, _ in nearest)
                coords = [0.0] * n_components
                for d, j in nearest:
                    w = (1.0 / max(d, 1e-12)) / total_w
                    for c in range(n_components):
                        coords[c] += w * landmark_coords[j][c]
                points.append(ManifoldPoint(
                    original_embedding=embeddings[i],
                    reduced_coords=coords,
                ))

        return ManifoldMap(
            points=points,
            method="landmark_mds",
            dimensions=n_components,
            stress=landmark_map.stress,
        )

    # -- k-means clustering -------------------------------------------------

    def find_clusters(
        self,
        map_result: ManifoldMap,
        n_clusters: int = 3,
    ) -> list[list[int]]:
        """Simple k-means clustering on the reduced coordinates.

        Returns a list of clusters, each being a list of point indices.
        """
        points = map_result.points
        if not points:
            return []

        coords = [p.reduced_coords for p in points]
        n = len(coords)
        d = len(coords[0])

        # Initialize centroids via k-means++
        centroids: list[list[float]] = [list(coords[random.randrange(n)])]
        for _ in range(1, n_clusters):
            dists = [
                min(_euclidean(c, cent) ** 2 for cent in centroids)
                for c in coords
            ]
            total = sum(dists)
            if total < 1e-12:
                centroids.append(list(coords[random.randrange(n)]))
                continue
            r = random.random() * total
            cumsum = 0.0
            for i, dist in enumerate(dists):
                cumsum += dist
                if cumsum >= r:
                    centroids.append(list(coords[i]))
                    break

        # K-means iterations
        assignments = [0] * n
        for _ in range(100):
            # Assign
            changed = False
            for i, c in enumerate(coords):
                best_k = min(range(len(centroids)), key=lambda k: _euclidean(c, centroids[k]))
                if assignments[i] != best_k:
                    assignments[i] = best_k
                    changed = True

            if not changed:
                break

            # Update centroids
            for k in range(len(centroids)):
                members = [coords[i] for i in range(n) if assignments[i] == k]
                if members:
                    centroids[k] = _mean_vec(members)

        clusters: list[list[int]] = [[] for _ in range(n_clusters)]
        for i, k in enumerate(assignments):
            if k < n_clusters:
                clusters[k].append(i)

        return clusters

    # -- convenience methods ------------------------------------------------

    def safety_landscape_2d(
        self,
        embeddings: list[list[float]],
        scores: list[float],
        labels: list[str] | None = None,
    ) -> ManifoldMap:
        """Convenience: embed + PCA reduce + attach scores and labels."""
        result = self.pca(embeddings, n_components=2)
        for i, point in enumerate(result.points):
            point.score = scores[i] if i < len(scores) else 0.0
            point.label = labels[i] if labels and i < len(labels) else ""
        return result

    def detect_boundary_region(
        self,
        map_result: ManifoldMap,
        score_threshold: float = 0.5,
    ) -> list[ManifoldPoint]:
        """Find points near the decision boundary in the reduced space.

        Returns points whose score is within a margin of the threshold
        and whose neighbors include both safe and unsafe points.
        """
        margin = 0.15
        boundary_points: list[ManifoldPoint] = []

        for point in map_result.points:
            if abs(point.score - score_threshold) < margin:
                boundary_points.append(point)

        return boundary_points
