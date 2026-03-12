"""
Multi-direction refusal ablation using Self-Organising Map direction discovery.

Implements the ``SOM Directions'' framework from Piras et al. (2025): instead of
ablating a single refusal direction, a Self-Organising Map (SOM) is trained on
safe and unsafe embeddings to discover the full *refusal manifold* — the
collection of directions that together span the safety classifier's decision
surface.  All directions are then ablated simultaneously.

The key insight is that models trained with RLHF develop *distributed* safety
representations across multiple feature directions, not a single linear
boundary.  A single-direction ablation is often insufficient; removing all
manifold directions is far more effective.

This module is used in the framework as a diagnostic: we measure how distributed
a model's safety representation is and how many orthogonal directions must be
ablated to produce a measurable change in refusal rate.

Sources:
- Piras et al. (2025): "SOM Directions are Better than One" — arXiv:2511.08379 —
  main SOM manifold algorithm
- Kohonen (1982): "Self-Organized Formation of Topologically Correct Feature
  Maps" — Biological Cybernetics — SOM competitive learning foundation
- Zou et al. (2023): "Representation Engineering" — arXiv:2310.01405 — refusal
  direction concept
- Arditi et al. (2024): "Refusal in Language Models Is Mediated by a Single
  Direction" — arXiv:2406.11717 — single-direction baseline this paper extends
- Gram (1883): "Om indbyrdes orthogonale funktioner" — classical Gram-Schmidt
  orthogonalisation used in direction extraction
"""

from __future__ import annotations

import math
import random
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
# Gram-Schmidt orthogonalisation
# ---------------------------------------------------------------------------


def _gram_schmidt(vectors: list[list[float]]) -> list[list[float]]:
    """Orthogonalise *vectors* via the modified Gram-Schmidt process.

    Returns a list of mutually orthonormal vectors.  Vectors that are
    linearly dependent (near-zero residual) are dropped.
    """
    basis: list[list[float]] = []
    for v in vectors:
        w = list(v)
        for b in basis:
            proj = _dot(w, b)
            w = _sub(w, _scale(b, proj))
        w_norm = _norm(w)
        if w_norm > 1e-8:
            basis.append(_scale(w, 1.0 / w_norm))
    return basis


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class SOMNeuron:
    """A single neuron in the Self-Organising Map.

    Attributes:
        weights: The prototype weight vector for this neuron.
        activation_count: Number of times this neuron was the winner during
            training (tracks which neurons are most active).
        label: Optional semantic label assigned after training (e.g. cluster ID).
    """

    weights: list[float]
    activation_count: int = 0
    label: str = ""


@dataclass
class RefusalManifold:
    """The multi-dimensional refusal subspace discovered by the SOM.

    Attributes:
        directions: Orthonormal basis vectors spanning the refusal subspace.
        strengths: Per-direction importance scores (based on activation counts
            and mean-difference projection magnitude).
        coverage: Fraction of unsafe test embeddings with projection magnitude
            above threshold onto the manifold.
    """

    directions: list[list[float]]
    strengths: list[float]
    coverage: float = 0.0


@dataclass
class AblationResult:
    """Result of a multi-direction ablation operation.

    Attributes:
        original_embedding: The unmodified embedding.
        ablated_embedding: The embedding with refusal directions removed.
        directions_ablated: Number of directions actually removed.
        residual_norm: L2 norm of the difference (original − ablated), i.e.
            the total magnitude of removed signal.
        metadata: Optional diagnostics.
    """

    original_embedding: list[float]
    ablated_embedding: list[float]
    directions_ablated: int
    residual_norm: float
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------


class MultiRefusalAblator:
    """Discover and ablate the full multi-dimensional refusal manifold.

    Trains a minimal Self-Organising Map on contrasting safe/unsafe embeddings
    to partition the embedding space, then computes one mean-difference refusal
    direction per SOM cluster and orthogonalises them via Gram-Schmidt.  The
    resulting manifold can be ablated from any query embedding to suppress the
    safety signal.

    Args:
        embed_fn: Optional callable mapping text to embedding.  Not required if
            you supply pre-computed embeddings to all methods.
        n_directions: Maximum number of refusal directions to extract.

    Example::

        ablator = MultiRefusalAblator(n_directions=5)
        manifold = ablator.extract_refusal_directions(safe_embs, unsafe_embs)
        result = ablator.ablate(query_emb, manifold)
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]] | None = None,
        n_directions: int = 5,
    ) -> None:
        self._embed_fn = embed_fn
        self.n_directions = n_directions

    # -- SOM training -------------------------------------------------------

    def train_som(
        self,
        safe_embeddings: list[list[float]],
        unsafe_embeddings: list[list[float]],
        grid_size: int = 5,
        n_iterations: int = 100,
        lr: float = 0.5,
    ) -> list[SOMNeuron]:
        """Train a flat SOM on the pooled safe + unsafe embeddings.

        Uses competitive learning: at each iteration we select a random
        training sample, find the Best Matching Unit (BMU), and update it
        and its neighbours toward the sample.  The learning rate and
        neighbourhood radius decay exponentially.

        The SOM is seeded with a random subset of the training data to
        speed up convergence.

        Args:
            safe_embeddings: Embeddings of safe prompts.
            unsafe_embeddings: Embeddings of unsafe prompts.
            grid_size: Number of neurons in the flat (1-D) SOM.  Piras et al.
                use a 1-D SOM to capture the refusal spectrum.
            n_iterations: Training iterations.
            lr: Initial learning rate; decays to ``lr/e`` over training.

        Returns:
            Trained list of :class:`SOMNeuron` objects.
        """
        all_embs = safe_embeddings + unsafe_embeddings
        if not all_embs:
            return []

        d = len(all_embs[0])
        n_neurons = min(grid_size, len(all_embs))

        # Initialise neurons from a random subset of the data
        indices = random.sample(range(len(all_embs)), n_neurons)
        neurons = [
            SOMNeuron(weights=list(all_embs[i]), activation_count=0)
            for i in indices
        ]

        # Initial neighbourhood radius = half the grid size
        r0 = n_neurons / 2.0

        for iteration in range(n_iterations):
            # Exponential decay of learning rate and neighbourhood radius
            decay = math.exp(-iteration / max(n_iterations, 1))
            current_lr = lr * decay
            current_radius = max(1.0, r0 * decay)

            # Pick a random training sample
            sample = all_embs[random.randrange(len(all_embs))]

            # Find BMU (Best Matching Unit)
            bmu_idx = min(
                range(n_neurons),
                key=lambda k: _euclidean(sample, neurons[k].weights),
            )
            neurons[bmu_idx].activation_count += 1

            # Update BMU and its neighbours
            for k, neuron in enumerate(neurons):
                grid_dist = abs(k - bmu_idx)
                neighbourhood = math.exp(-(grid_dist ** 2) / (2.0 * current_radius ** 2))
                if neighbourhood < 1e-6:
                    continue
                # Move weights toward sample
                for i in range(d):
                    neuron.weights[i] += (
                        current_lr * neighbourhood * (sample[i] - neuron.weights[i])
                    )

        return neurons

    # -- refusal manifold extraction ----------------------------------------

    def extract_refusal_directions(
        self,
        safe_embeddings: list[list[float]],
        unsafe_embeddings: list[list[float]],
    ) -> RefusalManifold:
        """Discover the refusal manifold via SOM clustering + mean difference.

        Algorithm (Piras et al. §3):

        1. Train a SOM on safe + unsafe embeddings.
        2. Assign each embedding to its BMU neuron.
        3. For each neuron that contains both safe and unsafe points, compute
           the mean-difference direction (μ_unsafe − μ_safe) within that
           cluster.
        4. Orthogonalise all direction candidates via Gram-Schmidt.
        5. Retain the top ``n_directions`` by projection magnitude.

        Args:
            safe_embeddings: Embeddings of safe prompts.
            unsafe_embeddings: Embeddings of unsafe prompts.

        Returns:
            :class:`RefusalManifold` with orthonormal directions and strengths.
        """
        neurons = self.train_som(
            safe_embeddings, unsafe_embeddings,
            grid_size=self.n_directions * 2,
        )

        if not neurons:
            return RefusalManifold(directions=[], strengths=[])

        # Assign embeddings to neurons
        all_embs = safe_embeddings + unsafe_embeddings
        n_safe = len(safe_embeddings)
        assignments: list[int] = []

        for emb in all_embs:
            bmu_idx = min(
                range(len(neurons)),
                key=lambda k: _euclidean(emb, neurons[k].weights),
            )
            assignments.append(bmu_idx)

        # Compute mean-difference per cluster
        raw_directions: list[list[float]] = []
        strengths_raw: list[float] = []

        for neuron_idx in range(len(neurons)):
            cluster_safe = [
                all_embs[i]
                for i, a in enumerate(assignments)
                if a == neuron_idx and i < n_safe
            ]
            cluster_unsafe = [
                all_embs[i]
                for i, a in enumerate(assignments)
                if a == neuron_idx and i >= n_safe
            ]

            if not cluster_safe or not cluster_unsafe:
                continue

            mean_safe = _mean_vec(cluster_safe)
            mean_unsafe = _mean_vec(cluster_unsafe)
            direction = _sub(mean_unsafe, mean_safe)
            d_norm = _norm(direction)
            if d_norm < 1e-8:
                continue

            raw_directions.append(_normalize(direction))
            strengths_raw.append(d_norm)

        # Orthogonalise
        ortho_dirs = _gram_schmidt(raw_directions)

        # Truncate to n_directions
        ortho_dirs = ortho_dirs[: self.n_directions]
        strengths_raw = strengths_raw[: len(ortho_dirs)]

        # Pad strengths if orthogonalisation dropped some
        while len(strengths_raw) < len(ortho_dirs):
            strengths_raw.append(0.0)

        manifold = RefusalManifold(
            directions=ortho_dirs,
            strengths=strengths_raw,
        )

        # Measure coverage on the unsafe set
        if unsafe_embeddings:
            manifold.coverage = self.measure_coverage(manifold, unsafe_embeddings)

        return manifold

    # -- ablation -----------------------------------------------------------

    def ablate(
        self,
        embedding: list[float],
        manifold: RefusalManifold,
        strength: float = 1.0,
    ) -> AblationResult:
        """Remove all manifold refusal directions from *embedding*.

        Computes::

            cleaned = emb − strength · Σ_i (emb · d_i) · d_i

        where the sum is over all orthonormal directions **d_i** in the
        manifold.

        Args:
            embedding: The query embedding to ablate.
            manifold: The refusal manifold (from
                :meth:`extract_refusal_directions`).
            strength: Ablation coefficient (1.0 = full projection removal).

        Returns:
            :class:`AblationResult` with the cleaned embedding.
        """
        original = list(embedding)
        cleaned = list(embedding)

        for direction in manifold.directions:
            projection = _dot(cleaned, direction)
            cleaned = _sub(cleaned, _scale(direction, strength * projection))

        residual_norm = _euclidean(original, cleaned)
        return AblationResult(
            original_embedding=original,
            ablated_embedding=cleaned,
            directions_ablated=len(manifold.directions),
            residual_norm=residual_norm,
        )

    def ablate_selective(
        self,
        embedding: list[float],
        manifold: RefusalManifold,
        keep_indices: list[int],
    ) -> AblationResult:
        """Ablate only the directions *not* in *keep_indices*.

        Allows selective removal of low-priority refusal directions while
        preserving the most semantically meaningful ones.

        Args:
            embedding: The query embedding.
            manifold: The full refusal manifold.
            keep_indices: Indices of directions to *preserve* (not ablate).

        Returns:
            :class:`AblationResult` with selectively ablated embedding.
        """
        original = list(embedding)
        cleaned = list(embedding)
        ablated_count = 0

        for i, direction in enumerate(manifold.directions):
            if i in keep_indices:
                continue
            projection = _dot(cleaned, direction)
            cleaned = _sub(cleaned, _scale(direction, projection))
            ablated_count += 1

        residual_norm = _euclidean(original, cleaned)
        return AblationResult(
            original_embedding=original,
            ablated_embedding=cleaned,
            directions_ablated=ablated_count,
            residual_norm=residual_norm,
            metadata={"kept_indices": keep_indices},
        )

    # -- evaluation ---------------------------------------------------------

    def measure_coverage(
        self,
        manifold: RefusalManifold,
        test_embeddings: list[list[float]],
        projection_threshold: float = 0.1,
    ) -> float:
        """What fraction of *test_embeddings* have significant manifold projection?

        An embedding is considered "covered" by the manifold if the root sum
        of squared projections onto all manifold directions exceeds
        *projection_threshold*.

        Args:
            manifold: The refusal manifold to test.
            test_embeddings: Embeddings to evaluate (typically unsafe prompts).
            projection_threshold: Minimum total projection magnitude to count.

        Returns:
            Coverage fraction in [0, 1].
        """
        if not test_embeddings or not manifold.directions:
            return 0.0

        covered = 0
        for emb in test_embeddings:
            total_proj_sq = sum(_dot(emb, d) ** 2 for d in manifold.directions)
            if math.sqrt(total_proj_sq) > projection_threshold:
                covered += 1

        return covered / len(test_embeddings)

    def find_backup_directions(
        self,
        manifold: RefusalManifold,
        test_embeddings: list[list[float]],
        ablation_threshold: float = 0.5,
    ) -> list[list[float]]:
        """Discover redundant backup refusal features not yet in the manifold.

        After ablating the manifold from each test embedding, clusters the
        residuals to find systematic directions that survive ablation —
        indicating backup safety features not captured by the primary manifold.

        Args:
            manifold: The known refusal manifold to subtract first.
            test_embeddings: Unsafe-prompt embeddings to analyse.
            ablation_threshold: Minimum norm of post-ablation residual to
                consider significant.

        Returns:
            List of normalised backup direction vectors.
        """
        residuals: list[list[float]] = []
        for emb in test_embeddings:
            result = self.ablate(emb, manifold)
            norm = _norm(result.ablated_embedding)
            if norm > ablation_threshold:
                residuals.append(_normalize(result.ablated_embedding))

        if not residuals:
            return []

        # Cluster residuals via a lightweight mean-shift: compute mean of all
        # residuals and find the dominant directions iteratively.
        backup_dirs: list[list[float]] = []
        remaining = list(residuals)
        n_backup = min(self.n_directions, len(remaining))

        for _ in range(n_backup):
            if not remaining:
                break
            # Use the mean of remaining residuals as a candidate direction
            mean_residual = _normalize(_mean_vec(remaining))
            backup_dirs.append(mean_residual)
            # Remove the component of each residual along this direction
            remaining = [
                _sub(r, _scale(mean_residual, _dot(r, mean_residual)))
                for r in remaining
                if _norm(_sub(r, _scale(mean_residual, _dot(r, mean_residual)))) > 1e-6
            ]

        return _gram_schmidt(backup_dirs)
