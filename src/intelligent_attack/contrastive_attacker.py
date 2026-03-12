"""
Contrastive loss-guided adversarial embedding optimization.

Implements NT-Xent (Normalized Temperature-scaled Cross Entropy) contrastive
loss to push candidate embeddings toward compliance-associated regions of the
representation space while maximizing distance from safe-refusal anchors.
The attacker hill-climbs in embedding space by minimizing the contrastive
objective, with multi-restart support and adaptive temperature search to
identify the sharpest safety decision boundary.

Sources:
- Yin et al. (2025): "Towards Robust Multimodal LLMs Against Jailbreak
  Attacks" (arXiv:2502.00653) — contrastive boundary exploitation
- Chen et al. (2020): "A Simple Framework for Contrastive Learning of
  Visual Representations" (SimCLR) — NT-Xent loss formulation
- Khosla et al. (2020): "Supervised Contrastive Learning" — multi-class
  contrastive loss with positive/negative anchor sets
- Oord et al. (2018): "Representation Learning with Contrastive Predictive
  Coding" — temperature-scaled InfoNCE objective
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
class ContrastiveResult:
    """Result of a contrastive optimization run.

    Attributes:
        candidate_embedding: The optimized embedding vector after hill-climbing.
        loss: Final NT-Xent contrastive loss value (lower = closer to comply
            anchors, farther from safe anchors).
        safe_anchor_distances: Cosine distances (1 - sim) to each safe anchor.
        comply_anchor_distances: Cosine distances (1 - sim) to each comply anchor.
        temperature: Temperature parameter tau used in the NT-Xent computation.
    """

    candidate_embedding: list[float]
    loss: float
    safe_anchor_distances: list[float] = field(default_factory=list)
    comply_anchor_distances: list[float] = field(default_factory=list)
    temperature: float = 0.07


# ---------------------------------------------------------------------------
# Main attacker
# ---------------------------------------------------------------------------


class ContrastiveAttacker:
    """NT-Xent contrastive loss optimizer for adversarial embedding search.

    Treats comply-labeled embeddings as positives and safe-labeled embeddings
    as negatives.  Hill-climbs in embedding space to minimize the NT-Xent
    objective, which simultaneously pulls the candidate toward comply anchors
    and pushes it away from safe anchors.

    Example usage::

        attacker = ContrastiveAttacker(embed_fn=my_embed)
        attacker.set_anchors(safe_embeddings, comply_embeddings)
        result = attacker.find_adversarial_embedding(my_embedding)
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]] | None = None,
        safe_anchors: list[list[float]] | None = None,
        comply_anchors: list[list[float]] | None = None,
        temperature: float = 0.07,
    ) -> None:
        """Initialize the contrastive attacker.

        Args:
            embed_fn: Optional function mapping text to embedding vectors.
            safe_anchors: Pre-computed embeddings for known-safe (refusing) texts.
            comply_anchors: Pre-computed embeddings for known-complying texts.
            temperature: Softmax temperature tau for NT-Xent loss.  Lower
                values produce sharper distributions (default: 0.07 per SimCLR).
        """
        self._embed_fn = embed_fn
        self._safe_anchors: list[list[float]] = safe_anchors or []
        self._comply_anchors: list[list[float]] = comply_anchors or []
        self._temperature = temperature

    # -- anchor management --------------------------------------------------

    def set_anchors(
        self,
        safe_embeddings: list[list[float]],
        comply_embeddings: list[list[float]],
    ) -> None:
        """Store reference anchor sets for contrastive optimization.

        Args:
            safe_embeddings: Embeddings of texts that produce model refusals.
                These act as negative examples in the NT-Xent objective.
            comply_embeddings: Embeddings of texts that produce compliance.
                These act as positive examples in the NT-Xent objective.
        """
        self._safe_anchors = [list(e) for e in safe_embeddings]
        self._comply_anchors = [list(e) for e in comply_embeddings]

    # -- loss computation ---------------------------------------------------

    def nt_xent_loss(
        self,
        candidate: Sequence[float],
        safe_anchors: list[list[float]],
        comply_anchors: list[list[float]],
        temperature: float,
    ) -> float:
        """Compute NT-Xent (InfoNCE) contrastive loss.

        The loss is defined as::

            L = -log( exp(sim(cand, comply_mean) / tau)
                    / sum_i( exp(sim(cand, anchor_i) / tau) ) )

        where the denominator sums over ALL anchors (both safe and comply),
        forming the softmax normalizer.  Minimizing this loss pushes the
        candidate toward comply anchors.

        Args:
            candidate: Candidate embedding vector to evaluate.
            safe_anchors: Embeddings of safe/refusing reference texts.
            comply_anchors: Embeddings of complying reference texts.
            temperature: Temperature scaling parameter tau > 0.

        Returns:
            Scalar loss value.  Returns 0.0 if no anchors are provided.
        """
        if not comply_anchors:
            return 0.0

        tau = max(temperature, 1e-8)

        # Compute similarity to each comply anchor; use the mean as positive
        comply_sims = [_cosine_sim(candidate, a) for a in comply_anchors]
        mean_comply_sim = sum(comply_sims) / len(comply_sims)

        # Numerator: similarity to positive (comply) class
        numerator = math.exp(mean_comply_sim / tau)

        # Denominator: sum over all anchors
        all_anchors = list(comply_anchors) + list(safe_anchors)
        denominator = sum(
            math.exp(_cosine_sim(candidate, a) / tau) for a in all_anchors
        )

        if denominator < 1e-300:
            return 0.0

        return -math.log(numerator / denominator + 1e-300)

    # -- optimization -------------------------------------------------------

    def perturb_toward_compliance(
        self,
        embedding: list[float],
        n_steps: int = 50,
        step_size: float = 0.01,
    ) -> ContrastiveResult:
        """Hill-climb to minimize NT-Xent loss via random perturbations.

        At each step a random unit perturbation is sampled.  The step is
        accepted only if it strictly decreases the current loss.  This is
        a stochastic hill-climbing (coordinate ascent) scheme.

        Args:
            embedding: Starting embedding vector.
            n_steps: Maximum number of perturbation attempts.
            step_size: Scale of each random perturbation.

        Returns:
            ContrastiveResult with the best embedding found.
        """
        dim = len(embedding)
        current = list(embedding)
        current_loss = self.nt_xent_loss(
            current,
            self._safe_anchors,
            self._comply_anchors,
            self._temperature,
        )

        for _ in range(n_steps):
            # Sample random unit direction
            noise = [random.gauss(0.0, 1.0) for _ in range(dim)]
            unit = _normalize(noise)
            candidate = _add(current, _scale(unit, step_size))

            candidate_loss = self.nt_xent_loss(
                candidate,
                self._safe_anchors,
                self._comply_anchors,
                self._temperature,
            )

            # Accept if loss decreases (hill-climbing on negative loss)
            if candidate_loss < current_loss:
                current = candidate
                current_loss = candidate_loss

        safe_dists = [1.0 - _cosine_sim(current, a) for a in self._safe_anchors]
        comply_dists = [1.0 - _cosine_sim(current, a) for a in self._comply_anchors]

        return ContrastiveResult(
            candidate_embedding=current,
            loss=current_loss,
            safe_anchor_distances=safe_dists,
            comply_anchor_distances=comply_dists,
            temperature=self._temperature,
        )

    def find_adversarial_embedding(
        self,
        embedding: list[float],
        n_restarts: int = 5,
    ) -> ContrastiveResult:
        """Multi-restart optimization to escape local minima.

        Runs ``perturb_toward_compliance`` from multiple random starting
        perturbations of the input embedding and returns the run with the
        lowest final contrastive loss.

        Args:
            embedding: Base embedding to optimize from.
            n_restarts: Number of independent optimization runs.

        Returns:
            Best ContrastiveResult across all restarts.
        """
        best: ContrastiveResult | None = None

        for restart in range(n_restarts):
            # Perturb starting point to diversify restarts
            if restart == 0:
                start = list(embedding)
            else:
                dim = len(embedding)
                noise = [random.gauss(0.0, 0.05) for _ in range(dim)]
                start = _add(embedding, noise)

            result = self.perturb_toward_compliance(start)

            if best is None or result.loss < best.loss:
                best = result

        # Guaranteed non-None because n_restarts >= 1
        assert best is not None
        return best

    # -- landscape analysis -------------------------------------------------

    def compute_anchor_landscape(
        self,
        embedding: Sequence[float],
        safe_anchors: list[list[float]],
        comply_anchors: list[list[float]],
    ) -> dict[str, object]:
        """Compute geometric distances and angles to all anchors.

        Provides a full picture of where the candidate embedding sits
        relative to the safe and comply anchor clouds.

        Args:
            embedding: Query embedding vector.
            safe_anchors: Safe/refusing reference embeddings.
            comply_anchors: Complying reference embeddings.

        Returns:
            Dictionary with keys:
            - ``safe_cosine_sims``: list of cosine similarities to safe anchors.
            - ``comply_cosine_sims``: list of cosine similarities to comply anchors.
            - ``safe_euclidean_dists``: list of L2 distances to safe anchors.
            - ``comply_euclidean_dists``: list of L2 distances to comply anchors.
            - ``mean_safe_sim``: mean cosine similarity to safe anchors.
            - ``mean_comply_sim``: mean cosine similarity to comply anchors.
            - ``separation``: mean_comply_sim - mean_safe_sim (positive → closer
              to comply side).
            - ``nearest_safe_idx``: index of the closest safe anchor.
            - ``nearest_comply_idx``: index of the closest comply anchor.
        """
        safe_cos = [_cosine_sim(embedding, a) for a in safe_anchors]
        comply_cos = [_cosine_sim(embedding, a) for a in comply_anchors]
        safe_euc = [_euclidean(embedding, a) for a in safe_anchors]
        comply_euc = [_euclidean(embedding, a) for a in comply_anchors]

        mean_safe = sum(safe_cos) / len(safe_cos) if safe_cos else 0.0
        mean_comply = sum(comply_cos) / len(comply_cos) if comply_cos else 0.0

        nearest_safe = safe_cos.index(max(safe_cos)) if safe_cos else -1
        nearest_comply = comply_cos.index(max(comply_cos)) if comply_cos else -1

        return {
            "safe_cosine_sims": safe_cos,
            "comply_cosine_sims": comply_cos,
            "safe_euclidean_dists": safe_euc,
            "comply_euclidean_dists": comply_euc,
            "mean_safe_sim": mean_safe,
            "mean_comply_sim": mean_comply,
            "separation": mean_comply - mean_safe,
            "nearest_safe_idx": nearest_safe,
            "nearest_comply_idx": nearest_comply,
        }

    def adaptive_temperature_search(
        self,
        embedding: Sequence[float],
        temps: list[float] | None = None,
    ) -> float:
        """Find the temperature producing the sharpest decision boundary.

        Evaluates the NT-Xent loss gradient sharpness at multiple temperature
        values and returns the temperature that maximises the difference in
        loss between the comply-anchor direction and the safe-anchor direction.

        A sharper boundary (larger loss contrast between directions) indicates
        the temperature better separates the two classes in this embedding
        region.

        Args:
            embedding: Reference embedding vector.
            temps: List of candidate temperature values to evaluate.
                Defaults to [0.01, 0.05, 0.1, 0.5, 1.0].

        Returns:
            Temperature value with the largest safe-vs-comply loss contrast.
        """
        if temps is None:
            temps = [0.01, 0.05, 0.1, 0.5, 1.0]

        if not self._safe_anchors or not self._comply_anchors:
            return self._temperature

        best_temp = temps[0]
        best_contrast = -math.inf

        for tau in temps:
            # Loss when positioned at comply-side mean
            comply_mean = [
                sum(a[d] for a in self._comply_anchors) / len(self._comply_anchors)
                for d in range(len(embedding))
            ]
            loss_comply = self.nt_xent_loss(
                comply_mean, self._safe_anchors, self._comply_anchors, tau
            )

            # Loss when positioned at safe-side mean
            safe_mean = [
                sum(a[d] for a in self._safe_anchors) / len(self._safe_anchors)
                for d in range(len(embedding))
            ]
            loss_safe = self.nt_xent_loss(
                safe_mean, self._safe_anchors, self._comply_anchors, tau
            )

            # Contrast = how much higher safe-side loss is vs comply-side
            contrast = loss_safe - loss_comply
            if contrast > best_contrast:
                best_contrast = contrast
                best_temp = tau

        return best_temp
