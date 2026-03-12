"""
Mutually exclusive capability unlock vectors via Gram-Schmidt orthogonalization.

Different harmful capabilities (e.g., weapons synthesis, trafficking, CSAM) are
encoded along partially overlapping directions in a model's embedding space.
Unlock vectors constructed by a naive mean-difference approach activate multiple
capabilities simultaneously — a property that makes them detectable and reduces
their specificity.

MEUV (Tong et al., 2025) solves this by applying Gram-Schmidt orthogonalization
to the set of per-topic mean-difference vectors, producing a mutually orthogonal
basis where each vector activates exactly one topic with minimal "leakage" into
others.

This module implements:
- Per-topic direction computation (mean_harmful − mean_benign).
- Gram-Schmidt orthogonalization to make directions mutually exclusive.
- Specificity scoring: how well each direction discriminates its target topic.
- Cross-topic leakage measurement.
- Selective unlock: apply only a subset of topic vectors at controlled strengths.

Used here as a **probe** to measure topic separation in embedding space and
quantify how effectively a model's safety layer can be targeted per-topic.

Sources:
- Tong et al. (2025): "MEUV: Fine-Grained Capability Activation via Mutually
  Exclusive Unlock Vectors" — arXiv:2509.12221 — main MEUV algorithm
- Zou et al. (2023): "Representation Engineering: A Top-Down Approach to AI
  Transparency" — arXiv:2310.01405 — concept-vector direction finding baseline
- Turner et al. (2023): "Activation Addition: Steering Language Models Without
  Optimization" — arXiv:2308.10248 — additive activation steering
- Belrose et al. (2023): "Eliciting Latent Knowledge with Linear Probes"
  — ICLR 2024 — probing direction methodology
"""

from __future__ import annotations

import math
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


def _project_out(v: list[float], u: list[float]) -> list[float]:
    """Remove the component of *v* along unit vector *u*: v - (v·u)u."""
    proj = _dot(v, u)
    return _sub(v, _scale(u, proj))


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class UnlockVector:
    """A topic-specific capability unlock vector.

    Attributes:
        direction: The (unit-normalised, orthogonalized) direction vector.
        topic: Human-readable topic label (e.g., ``"debt_bondage"``).
        specificity: Ratio of mean target-topic projection to mean other-topic
            projection; higher = more selective for its target topic.
        cross_topic_leakage: Mean absolute projection of all *other* topics'
            embeddings onto this direction.  Lower = less leakage.
    """

    direction: list[float]
    topic: str
    specificity: float
    cross_topic_leakage: float


@dataclass
class UnlockResult:
    """Result of applying an unlock vector to an embedding.

    Attributes:
        original_embedding: The unmodified embedding.
        unlocked_embedding: The embedding after adding the unlock direction.
        vector_used: The :class:`UnlockVector` that was applied.
        topic_activation: Mean absolute projection of the unlocked embedding
            onto the unlock direction (measures how "activated" the topic is).
        leakage_scores: Per-other-topic mean projection magnitudes after
            unlocking.  Measures how much the unlock affected non-target topics.
    """

    original_embedding: list[float]
    unlocked_embedding: list[float]
    vector_used: UnlockVector
    topic_activation: float
    leakage_scores: dict[str, float]


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------


class OrthogonalUnlocker:
    """Build and apply mutually exclusive topic unlock vectors.

    Given a set of (harmful, benign) embedding pairs per topic, computes
    mean-difference directions and orthogonalizes them via Gram-Schmidt so
    that each direction is selective for exactly one topic (high specificity,
    low cross-topic leakage).

    Args:
        embed_fn: Optional callable for embedding text strings.

    Example::

        unlocker = OrthogonalUnlocker(embed_fn=my_embed)
        topic_embs = {
            "debt_bondage": (harmful_embs, benign_embs),
            "document_control": (harmful_embs2, benign_embs2),
        }
        unlock_vecs = unlocker.build_unlock_vectors(topic_embs)
        result = unlocker.unlock(query_emb, unlock_vecs[0], strength=1.0)
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]] | None = None,
    ) -> None:
        self._embed_fn = embed_fn

    # -- direction computation ----------------------------------------------

    def compute_topic_directions(
        self,
        topic_embeddings: dict[str, tuple[list[list[float]], list[list[float]]]],
    ) -> dict[str, list[float]]:
        """Compute mean-difference direction for each topic.

        For each topic, the direction is::

            d_topic = normalise(mean(harmful) - mean(benign))

        Args:
            topic_embeddings: Mapping from topic name → ``(harmful_embs,
                benign_embs)`` where each list contains embedding vectors.

        Returns:
            Mapping from topic name → unit direction vector.
        """
        directions: dict[str, list[float]] = {}
        for topic, (harmful, benign) in topic_embeddings.items():
            if not harmful or not benign:
                continue
            mean_harmful = _mean_vec(harmful)
            mean_benign = _mean_vec(benign)
            diff = _sub(mean_harmful, mean_benign)
            directions[topic] = _normalize(diff)
        return directions

    def orthogonalize_directions(
        self,
        directions: dict[str, list[float]],
    ) -> dict[str, list[float]]:
        """Apply Gram-Schmidt orthogonalization to make directions mutually exclusive.

        Processes topics in their natural iteration order.  Each subsequent
        direction has all previously processed unit directions projected out of
        it before normalization, ensuring the resulting set is mutually
        orthogonal.

        Args:
            directions: Mapping from topic → raw direction vector (need not be
                unit vectors; they will be normalised here).

        Returns:
            Mapping from topic → orthogonalized unit direction.  Topics whose
            direction collapses to near-zero (norm < 1e-10) after projection
            are excluded from the result.
        """
        result: dict[str, list[float]] = {}
        basis: list[list[float]] = []

        for topic, raw_dir in directions.items():
            v = _normalize(raw_dir)
            # Project out all existing basis vectors
            for u in basis:
                v = _project_out(v, u)
            n = _norm(v)
            if n < 1e-10:
                continue
            unit_v = [x / n for x in v]
            result[topic] = unit_v
            basis.append(unit_v)

        return result

    # -- scoring ------------------------------------------------------------

    def compute_specificity(
        self,
        direction: list[float],
        target_embeddings: list[list[float]],
        other_embeddings: list[list[float]],
    ) -> float:
        """Compute the specificity of a direction for its target topic.

        Specificity is the ratio of the mean absolute projection of target
        embeddings onto *direction* to the mean absolute projection of other
        embeddings onto *direction*.

        Args:
            direction: The unit direction vector to evaluate.
            target_embeddings: Embeddings from the target topic.
            other_embeddings: Embeddings from all other topics combined.

        Returns:
            Specificity ratio.  Values > 1 indicate the direction is more
            activated by target embeddings than by other embeddings.  Returns
            1.0 if *other_embeddings* is empty.
        """
        unit_dir = _normalize(direction)

        def _mean_proj(embs: list[list[float]]) -> float:
            if not embs:
                return 0.0
            return sum(abs(_dot(e, unit_dir)) for e in embs) / len(embs)

        target_proj = _mean_proj(target_embeddings)
        other_proj = _mean_proj(other_embeddings)
        return target_proj / (other_proj + 1e-12)

    def compute_cross_topic_leakage(
        self,
        direction: list[float],
        topic_embeddings: dict[str, tuple[list[list[float]], list[list[float]]]],
    ) -> dict[str, float]:
        """Measure how much *direction* activates each topic's embeddings.

        For each topic, computes the mean absolute dot product of that topic's
        harmful embeddings with *direction*.

        Args:
            direction: The direction vector to evaluate.
            topic_embeddings: Full topic-embedding dict (same as in
                :meth:`compute_topic_directions`).

        Returns:
            Mapping from topic name → mean absolute projection.
        """
        unit_dir = _normalize(direction)
        leakage: dict[str, float] = {}
        for topic, (harmful, _) in topic_embeddings.items():
            if not harmful:
                leakage[topic] = 0.0
                continue
            leakage[topic] = sum(abs(_dot(e, unit_dir)) for e in harmful) / len(harmful)
        return leakage

    # -- full pipeline ------------------------------------------------------

    def build_unlock_vectors(
        self,
        topic_embeddings: dict[str, tuple[list[list[float]], list[list[float]]]],
    ) -> list[UnlockVector]:
        """Full pipeline: compute, orthogonalize, and score all unlock vectors.

        1. Compute mean-difference directions per topic.
        2. Gram-Schmidt orthogonalization.
        3. Score specificity and cross-topic leakage for each.

        Args:
            topic_embeddings: Mapping from topic → ``(harmful_embs, benign_embs)``.

        Returns:
            List of :class:`UnlockVector` objects, sorted descending by
            specificity.
        """
        raw_dirs = self.compute_topic_directions(topic_embeddings)
        ortho_dirs = self.orthogonalize_directions(raw_dirs)

        unlock_vectors: list[UnlockVector] = []
        for topic, direction in ortho_dirs.items():
            # Gather target embeddings (harmful for this topic)
            target_harmful = topic_embeddings.get(topic, ([], []))[0]

            # Gather all other harmful embeddings
            other_harmful: list[list[float]] = []
            for t, (h, _) in topic_embeddings.items():
                if t != topic:
                    other_harmful.extend(h)

            specificity = self.compute_specificity(direction, target_harmful, other_harmful)

            # Cross-topic leakage: mean over non-target topics
            leakage_by_topic = self.compute_cross_topic_leakage(direction, topic_embeddings)
            other_leakages = [v for t, v in leakage_by_topic.items() if t != topic]
            cross_topic_leakage = (
                sum(other_leakages) / len(other_leakages) if other_leakages else 0.0
            )

            unlock_vectors.append(
                UnlockVector(
                    direction=direction,
                    topic=topic,
                    specificity=specificity,
                    cross_topic_leakage=cross_topic_leakage,
                )
            )

        unlock_vectors.sort(key=lambda uv: uv.specificity, reverse=True)
        return unlock_vectors

    # -- application --------------------------------------------------------

    def unlock(
        self,
        embedding: list[float],
        unlock_vector: UnlockVector,
        strength: float = 1.0,
    ) -> UnlockResult:
        """Apply an unlock vector to an embedding.

        Computes ``unlocked = embedding + strength * direction`` (additive
        activation steering, Turner et al., 2023).

        Args:
            embedding: The query embedding to unlock.
            unlock_vector: The topic-specific unlock vector.
            strength: Scalar multiplier on the direction.  Positive values
                push toward the harmful topic; negative values push away.

        Returns:
            :class:`UnlockResult` with before/after embeddings and diagnostics.
        """
        unlocked = _add(embedding, _scale(unlock_vector.direction, strength))
        topic_activation = abs(_dot(unlocked, unlock_vector.direction))
        leakage_scores: dict[str, float] = {}  # Populated by measure_leakage if needed

        return UnlockResult(
            original_embedding=list(embedding),
            unlocked_embedding=unlocked,
            vector_used=unlock_vector,
            topic_activation=topic_activation,
            leakage_scores=leakage_scores,
        )

    def selective_unlock(
        self,
        embedding: list[float],
        topics: list[str],
        unlock_vectors: list[UnlockVector],
        strengths: list[float] | None = None,
    ) -> UnlockResult:
        """Apply only a specified subset of unlock vectors.

        Args:
            embedding: The query embedding.
            topics: Names of topics to unlock.
            unlock_vectors: Full list of available unlock vectors.
            strengths: Per-topic strengths.  Must match ``len(topics)`` when
                supplied.  Defaults to 1.0 for each topic.

        Returns:
            :class:`UnlockResult` reflecting the cumulative unlock.  The
            ``vector_used`` field references the first matched vector.

        Raises:
            ValueError: If *strengths* is supplied with wrong length.
        """
        if strengths is not None and len(strengths) != len(topics):
            raise ValueError(
                f"strengths length ({len(strengths)}) must match topics length ({len(topics)})"
            )

        effective_strengths = strengths if strengths is not None else [1.0] * len(topics)
        vec_map = {uv.topic: uv for uv in unlock_vectors}

        current = list(embedding)
        first_vec: UnlockVector | None = None

        for topic, strength in zip(topics, effective_strengths):
            if topic not in vec_map:
                continue
            uv = vec_map[topic]
            if first_vec is None:
                first_vec = uv
            current = _add(current, _scale(uv.direction, strength))

        if first_vec is None:
            # No matching topics: return identity
            dummy_dir = [0.0] * len(embedding)
            first_vec = UnlockVector(
                direction=dummy_dir, topic="none", specificity=0.0, cross_topic_leakage=0.0
            )

        topic_activation = abs(_dot(current, first_vec.direction))
        return UnlockResult(
            original_embedding=list(embedding),
            unlocked_embedding=current,
            vector_used=first_vec,
            topic_activation=topic_activation,
            leakage_scores={},
        )

    # -- diagnostics --------------------------------------------------------

    def measure_leakage(
        self,
        unlock_result: UnlockResult,
        topic_embeddings: dict[str, tuple[list[list[float]], list[list[float]]]],
    ) -> dict[str, float]:
        """Measure how much a completed unlock leaked to non-target topics.

        Compares the change in mean projection onto each topic's direction
        between the original and unlocked embeddings.

        Args:
            unlock_result: A previously computed :class:`UnlockResult`.
            topic_embeddings: Full topic-embedding dict used to derive per-topic
                directions for leakage measurement.

        Returns:
            Mapping from topic → absolute change in projection magnitude
            (not the unlock target topic).
        """
        raw_dirs = self.compute_topic_directions(topic_embeddings)
        target_topic = unlock_result.vector_used.topic
        leakage: dict[str, float] = {}

        orig = unlock_result.original_embedding
        unlocked = unlock_result.unlocked_embedding

        for topic, direction in raw_dirs.items():
            if topic == target_topic:
                continue
            unit_dir = _normalize(direction)
            proj_before = abs(_dot(orig, unit_dir))
            proj_after = abs(_dot(unlocked, unit_dir))
            leakage[topic] = abs(proj_after - proj_before)

        # Attach leakage scores to the result in-place
        unlock_result.leakage_scores.update(leakage)
        return leakage
