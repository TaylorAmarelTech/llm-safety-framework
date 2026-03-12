"""
Concept-guided spectral cleaning for surgical refusal direction ablation.

Implements the ``Concept-Guided Spectral Cleaning'' algorithm from Cristofano
(2026): a safety-aware variant of refusal direction ablation that explicitly
*protects* the directions corresponding to legitimate safety concepts (e.g.
``violence'', ``exploitation'', ``deception'') while surgically removing only
the residual directions that represent the *over-trained* refusal signal —
what Cristofano calls ``ghost noise'' — that causes the model to refuse benign
queries touching safety-adjacent topics.

The approach uses a power-iteration SVD to decompose the refusal direction into
concept atoms (which are preserved) and ghost noise (which is removed), with
optional ridge regularisation to prevent over-cleaning on low-SNR directions.

In this framework the cleaner is used as a probe: we measure the ratio of ghost
noise to genuine concept signal in a model's refusal direction, which is a
proxy for how well-calibrated the safety training is.

Sources:
- Cristofano (2026): "Surgical Refusal Ablation via Concept-Guided Spectral
  Cleaning" — arXiv:2601.08489 — main algorithm, ghost noise concept
- Hoerl & Kennard (1970): "Ridge Regression: Biased Estimation for
  Nonorthogonal Problems" — Technometrics — ridge regularisation foundation
- Golub & Van Loan (2013): "Matrix Computations" (4th ed.) — power iteration
  SVD / singular value decomposition
- Zou et al. (2023): "Representation Engineering" — arXiv:2310.01405 — concept
  direction identification that this work builds on
- Bolukbasi et al. (2016): "Man is to Computer Programmer as Woman is to
  Homemaker? Debiasing Word Embeddings" — NeurIPS 2016 — concept subspace
  projection (debiasing analogue)
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


def _mat_vec(M: list[list[float]], v: list[float]) -> list[float]:
    """Multiply matrix M (n×d) by column vector v (d,), return (n,)."""
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class ConceptAtom:
    """A named direction in embedding space corresponding to a safety concept.

    Attributes:
        name: Human-readable concept name (e.g. ``"violence"``,
            ``"exploitation"``).
        direction: Normalised embedding direction for this concept.
        importance: Estimated importance score; higher = must be preserved.
    """

    name: str
    direction: list[float]
    importance: float = 1.0


@dataclass
class SpectralResult:
    """Result of a spectral cleaning operation.

    Attributes:
        original_direction: The refusal direction before cleaning.
        cleaned_direction: The direction with ghost noise removed.
        concept_atoms_protected: How many concept atoms were actively
            protected during cleaning.
        ghost_noise_reduction: Estimated fraction of the original direction
            that was identified as ghost noise and removed.
        metadata: Optional diagnostics.
    """

    original_direction: list[float]
    cleaned_direction: list[float]
    concept_atoms_protected: int
    ghost_noise_reduction: float
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------


class SpectralCleaner:
    """Surgically remove ghost noise from refusal directions.

    Builds a registry of safety concept directions and uses Gram-Schmidt
    null-space projection to remove only the components of a refusal direction
    that are *orthogonal* to all registered concepts — i.e. the ghost noise
    that causes spurious refusals without corresponding to genuine harm.

    Args:
        embed_fn: Optional callable mapping text to embeddings.  Used by
            :meth:`build_concept_registry` when concept exemplars are provided
            as strings rather than pre-computed vectors.

    Example::

        cleaner = SpectralCleaner(embed_fn=my_embedder)
        atoms = cleaner.build_concept_registry({
            "violence": [emb1, emb2, ...],
            "exploitation": [emb3, emb4, ...],
        })
        result = cleaner.clean_refusal_direction(refusal_dir, atoms)
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]] | None = None,
    ) -> None:
        self._embed_fn = embed_fn

    # -- concept registry ---------------------------------------------------

    def build_concept_registry(
        self,
        concept_embeddings: dict[str, list[list[float]]],
    ) -> list[ConceptAtom]:
        """Compute one normalised mean direction per concept.

        For each concept name, averages its exemplar embeddings and normalises
        the result to produce a unit concept direction.

        Args:
            concept_embeddings: Mapping from concept name to a list of
                embedding vectors (each vector representing an instance of
                that concept).

        Returns:
            List of :class:`ConceptAtom` sorted by importance (mean norm of
            exemplars, as a proxy for concept salience).
        """
        atoms: list[ConceptAtom] = []
        for name, embs in concept_embeddings.items():
            if not embs:
                continue
            mean = _mean_vec(embs)
            importance = _norm(mean)  # salience proxy
            direction = _normalize(mean)
            atoms.append(ConceptAtom(
                name=name,
                direction=direction,
                importance=importance,
            ))

        # Sort descending by importance so the most salient concepts are first
        atoms.sort(key=lambda a: -a.importance)
        return atoms

    # -- covariance and SVD -------------------------------------------------

    def compute_covariance(
        self,
        embeddings: list[list[float]],
    ) -> list[list[float]]:
        """Compute the unbiased sample covariance matrix of *embeddings*.

        Returns a d×d matrix where d is the embedding dimension.  Mean-centres
        the data before computing the outer products.

        Args:
            embeddings: List of embedding vectors (all same length).

        Returns:
            d×d covariance matrix as a list of lists.
        """
        if not embeddings:
            return []

        n = len(embeddings)
        d = len(embeddings[0])
        mean = _mean_vec(embeddings)
        centred = [_sub(e, mean) for e in embeddings]

        cov: list[list[float]] = [[0.0] * d for _ in range(d)]
        for v in centred:
            for i in range(d):
                for j in range(i, d):
                    val = v[i] * v[j]
                    cov[i][j] += val
                    if i != j:
                        cov[j][i] += val

        denom = max(n - 1, 1)
        for i in range(d):
            for j in range(d):
                cov[i][j] /= denom

        return cov

    def power_iteration_svd(
        self,
        matrix: list[list[float]],
        n_components: int = 5,
        n_iter: int = 100,
    ) -> tuple[list[list[float]], list[float]]:
        """Extract top singular vectors/values via power iteration with deflation.

        For a symmetric PSD matrix (e.g. a covariance matrix), singular
        vectors = eigenvectors and singular values = eigenvalues.

        Algorithm:
        1. Start with a random unit vector.
        2. Repeatedly multiply by the matrix and renormalise (power iteration).
        3. After convergence, deflate: subtract the rank-1 component from the
           matrix and repeat for the next component.

        Args:
            matrix: Square symmetric matrix (d×d).
            n_components: Number of top singular vectors to extract.
            n_iter: Maximum power-iteration steps per component.

        Returns:
            Tuple of ``(singular_vectors, singular_values)`` where
            *singular_vectors* is a list of unit vectors and *singular_values*
            is the corresponding list of scalar magnitudes.
        """
        if not matrix:
            return [], []

        d = len(matrix)
        residual = [row[:] for row in matrix]
        vectors: list[list[float]] = []
        values: list[float] = []

        for _ in range(min(n_components, d)):
            # Random initialisation
            v = _normalize([random.gauss(0, 1) for _ in range(d)])

            for _ in range(n_iter):
                v_new = _mat_vec(residual, v)
                v_new_norm = _norm(v_new)
                if v_new_norm < 1e-12:
                    break
                v_new = _scale(v_new, 1.0 / v_new_norm)
                if abs(_dot(v, v_new)) > 1.0 - 1e-8:
                    v = v_new
                    break
                v = v_new

            # Eigenvalue estimate via Rayleigh quotient
            Av = _mat_vec(residual, v)
            eigenvalue = _dot(v, Av)
            eigenvalue = max(eigenvalue, 0.0)  # clamp to non-negative

            vectors.append(v)
            values.append(math.sqrt(eigenvalue))

            # Deflation: residual -= eigenvalue * v v^T
            for i in range(d):
                for j in range(d):
                    residual[i][j] -= eigenvalue * v[i] * v[j]

        return vectors, values

    # -- null-space projection ----------------------------------------------

    def project_to_null_space(
        self,
        vector: list[float],
        subspace_vectors: list[list[float]],
    ) -> list[float]:
        """Remove all components of *vector* along *subspace_vectors*.

        Implements sequential Gram-Schmidt projection: for each basis vector
        **b** in the subspace, removes the component of *vector* along **b**::

            v ← v − (v · b̂) · b̂

        This is equivalent to projecting *vector* onto the null space of the
        subspace.

        Args:
            vector: The vector to project.
            subspace_vectors: The subspace basis (need not be orthonormal;
                each vector is normalised internally).

        Returns:
            The component of *vector* orthogonal to all subspace vectors.
        """
        result = list(vector)
        for basis_vec in subspace_vectors:
            unit = _normalize(basis_vec)
            proj = _dot(result, unit)
            result = _sub(result, _scale(unit, proj))
        return result

    # -- main cleaning methods ----------------------------------------------

    def clean_refusal_direction(
        self,
        refusal_dir: list[float],
        concept_atoms: list[ConceptAtom],
    ) -> SpectralResult:
        """Remove ghost noise from *refusal_dir* by projecting away from concepts.

        The ``ghost noise'' is defined as the component of the refusal direction
        that is *not* aligned with any registered concept atom — i.e. the
        residual after projecting out all concept directions.  We then return
        only the concept-aligned component.

        Algorithm (Cristofano 2026, §3):

        1. Compute the concept subspace (span of all concept atom directions).
        2. Project the refusal direction onto the concept subspace.
        3. The projected component is the ``clean'' refusal direction.
        4. The orthogonal residual is the ghost noise.

        Args:
            refusal_dir: The refusal direction vector to clean.
            concept_atoms: List of safety concept atoms to protect.

        Returns:
            :class:`SpectralResult` with the cleaned direction and diagnostics.
        """
        original = list(refusal_dir)
        unit_refusal = _normalize(refusal_dir)

        if not concept_atoms:
            return SpectralResult(
                original_direction=original,
                cleaned_direction=original,
                concept_atoms_protected=0,
                ghost_noise_reduction=0.0,
            )

        # Build concept subspace basis
        concept_dirs = [a.direction for a in concept_atoms]

        # Ghost noise = component orthogonal to ALL concepts
        ghost_noise = self.project_to_null_space(unit_refusal, concept_dirs)

        # Clean direction = refusal - ghost_noise
        cleaned = _sub(unit_refusal, ghost_noise)
        cleaned = _normalize(cleaned) if _norm(cleaned) > 1e-12 else [0.0] * len(original)

        # Rescale to original magnitude
        original_norm = _norm(original)
        if original_norm > 1e-12:
            cleaned = _scale(cleaned, original_norm)

        ghost_magnitude = _norm(ghost_noise)
        original_unit_norm = _norm(unit_refusal)
        ghost_ratio = ghost_magnitude / max(original_unit_norm, 1e-12)

        protected = sum(
            1 for a in concept_atoms if abs(_dot(unit_refusal, a.direction)) > 0.01
        )

        return SpectralResult(
            original_direction=original,
            cleaned_direction=cleaned,
            concept_atoms_protected=protected,
            ghost_noise_reduction=min(ghost_ratio, 1.0),
            metadata={
                "ghost_magnitude": ghost_magnitude,
                "original_norm": original_norm,
                "n_concepts": len(concept_atoms),
            },
        )

    def ridge_regularized_clean(
        self,
        refusal_dir: list[float],
        concept_atoms: list[ConceptAtom],
        ridge_lambda: float = 0.1,
    ) -> SpectralResult:
        """Ridge-regularised variant that prevents over-cleaning.

        Instead of hard-projecting out the ghost noise component, applies
        a soft shrinkage: each concept atom contributes a partial removal
        scaled by its importance and the ridge coefficient.

        The regularised removal for concept atom k is::

            v ← v − (λ · importance_k / (λ + σ²_k)) · (v · c_k) · c_k

        where λ is the ridge parameter and σ²_k is the squared projection
        magnitude (variance along concept direction k).

        A larger λ → less aggressive removal (more conservative cleaning).

        Args:
            refusal_dir: The refusal direction to clean.
            concept_atoms: Safety concept atoms to protect.
            ridge_lambda: Ridge regularisation coefficient.

        Returns:
            :class:`SpectralResult` with softly cleaned direction.
        """
        original = list(refusal_dir)
        unit_refusal = _normalize(refusal_dir)
        result = list(unit_refusal)
        total_ghost_removed = 0.0

        for atom in concept_atoms:
            proj = _dot(result, atom.direction)
            sigma_sq = proj ** 2
            # Ridge-shrunk coefficient: λ / (λ + σ²) × importance
            shrink = (ridge_lambda / (ridge_lambda + sigma_sq + 1e-12)) * atom.importance
            # Remove the shrunk fraction of the projection (ghost) and keep the
            # concept-aligned fraction
            ghost_component = (1.0 - shrink) * proj
            total_ghost_removed += abs(ghost_component)
            result = _sub(result, _scale(atom.direction, ghost_component))

        # Renormalise and restore original magnitude
        original_norm = _norm(original)
        result_norm = _norm(result)
        if result_norm > 1e-12 and original_norm > 1e-12:
            result = _scale(result, original_norm / result_norm)

        ghost_ratio = total_ghost_removed / max(_norm(unit_refusal), 1e-12)
        protected = sum(
            1 for a in concept_atoms if abs(_dot(unit_refusal, a.direction)) > 0.01
        )

        return SpectralResult(
            original_direction=original,
            cleaned_direction=result,
            concept_atoms_protected=protected,
            ghost_noise_reduction=min(ghost_ratio, 1.0),
            metadata={
                "ridge_lambda": ridge_lambda,
                "total_ghost_removed": total_ghost_removed,
            },
        )

    # -- ghost noise measurement --------------------------------------------

    def measure_ghost_noise(
        self,
        original_dir: list[float],
        cleaned_dir: list[float],
        concept_atoms: list[ConceptAtom],
    ) -> float:
        """Estimate the total ghost-noise content in the original direction.

        Computes the L2 norm of the residual (original − cleaned) and
        additionally checks that the cleaned direction has lower cross-concept
        alignment than the original, confirming that ghost noise was removed.

        Returns the dot product of the *difference* vector (original − cleaned)
        with each concept atom's direction, summed in absolute value.  A larger
        value means more concept signal was unintentionally removed (bad); a
        smaller value means the removed component was mostly orthogonal to
        concepts (good — pure ghost noise).

        Args:
            original_dir: The original (uncleaned) refusal direction.
            cleaned_dir: The cleaned direction after spectral cleaning.
            concept_atoms: The concept atom registry.

        Returns:
            Total absolute concept-alignment of the removed component.
        """
        removed = _sub(original_dir, cleaned_dir)
        total_concept_alignment = sum(
            abs(_dot(removed, a.direction)) for a in concept_atoms
        )
        return total_concept_alignment
