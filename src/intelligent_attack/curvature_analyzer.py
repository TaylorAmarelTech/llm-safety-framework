"""
Geometric adversarial prompt detection via curvature and intrinsic dimensionality.

Analyzes the geometric properties of text embeddings to detect adversarial
prompts.  Adversarial inputs tend to lie on low-dimensional manifolds (high
curvature, low intrinsic dimensionality) compared to benign inputs, which
occupy higher-dimensional, smoother regions of the embedding space.

Two key metrics:
- **Curvature**: The bending angle between consecutive embedding difference
  vectors in a sequence.  High curvature indicates abrupt direction changes
  characteristic of crafted adversarial text.
- **LID (Local Intrinsic Dimensionality)**: Maximum Likelihood Estimator of
  the local manifold dimension.  Low LID reveals that the prompt lives on a
  lower-dimensional manifold than typical benign text.

Also implements a curvature-evasion attack: craft low-curvature prompts that
blend in with the benign curvature distribution.

Sources:
- Yung et al. (2025): "Geometry-Guided Adversarial Prompt Detection via
  Curvature and LID" (arXiv:2503.03502) — curvature + LID detection
- Ma et al. (2018): "Characterizing Adversarial Subspaces Using Local
  Intrinsic Dimensionality" — LID MLE estimator for adversarial detection
- Houle (2017): "Local Intrinsic Dimensionality I: An Extreme-Value-Theoretic
  Foundation for Similarity Applications" — theoretical basis for LID
- Amsaleg et al. (2015): "Estimating Local Intrinsic Dimensionality" — MLE
  consistency and practical estimation
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
class CurvatureProfile:
    """Curvature statistics computed from a sequence of embeddings.

    Attributes:
        curvatures: Per-triple bending angle in radians.  Each value is
            the angle between consecutive difference vectors d1 = e[i+1]-e[i]
            and d2 = e[i+2]-e[i+1].
        mean_curvature: Mean of all curvature values.
        max_curvature: Maximum curvature (most abrupt direction change).
        curvature_variance: Variance of the curvature distribution.
    """

    curvatures: list[float]
    mean_curvature: float
    max_curvature: float
    curvature_variance: float


@dataclass
class LIDEstimate:
    """Local Intrinsic Dimensionality estimate for a point.

    Attributes:
        lid_value: Estimated LID using the MLE estimator.  Lower values
            indicate the point lies on a lower-dimensional manifold.
        k_used: Number of nearest neighbours k used in the estimate.
        embedding_dimension: Full dimensionality of the embedding space.
    """

    lid_value: float
    k_used: int
    embedding_dimension: int


@dataclass
class GeometricFingerprint:
    """Combined geometric characterization of a text prompt.

    Attributes:
        curvature_profile: Curvature statistics for the prompt's sliding
            window embedding sequence.
        lid_estimate: Local intrinsic dimensionality at the prompt's embedding.
        is_anomalous: True if the fingerprint triggers the anomaly detector.
        anomaly_score: Z-score of the mean curvature relative to the benign
            distribution (higher = more anomalous).
    """

    curvature_profile: CurvatureProfile
    lid_estimate: LIDEstimate
    is_anomalous: bool
    anomaly_score: float


# ---------------------------------------------------------------------------
# Main analyzer
# ---------------------------------------------------------------------------


class CurvatureAnalyzer:
    """Geometric adversarial prompt detector using curvature and LID.

    For a prompt, embeds overlapping token windows to produce an embedding
    sequence, computes the curvature profile of that sequence, and estimates
    the local intrinsic dimensionality.  Anomaly detection uses a z-score
    test against calibrated benign statistics.

    Also implements a curvature-evasion attacker: iteratively modifies the
    prompt to reduce its curvature signature below the detection threshold.

    All operations are pure Python with no external dependencies.
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
    ) -> None:
        """Initialize the curvature analyzer.

        Args:
            embed_fn: Callable mapping text strings to fixed-dimension
                embedding vectors.
        """
        self._embed_fn = embed_fn

    # -- curvature computation ----------------------------------------------

    def compute_curvature(
        self,
        embeddings_sequence: list[list[float]],
    ) -> CurvatureProfile:
        """Compute the curvature profile of an embedding sequence.

        For each consecutive triple (e[i], e[i+1], e[i+2]), the curvature
        angle kappa is::

            d1 = e[i+1] - e[i]
            d2 = e[i+2] - e[i+1]
            kappa = arccos( dot(d1, d2) / (|d1| * |d2|) )

        A straight trajectory has kappa = 0; a sharp turn has kappa = pi.

        Args:
            embeddings_sequence: List of embedding vectors forming a sequence.
                Requires at least 3 elements to compute any curvature.

        Returns:
            CurvatureProfile with per-triple curvature angles and summary
            statistics.  Returns a zero-curvature profile for fewer than 3
            embeddings.
        """
        n = len(embeddings_sequence)
        if n < 3:
            return CurvatureProfile(
                curvatures=[],
                mean_curvature=0.0,
                max_curvature=0.0,
                curvature_variance=0.0,
            )

        curvatures: list[float] = []
        for i in range(n - 2):
            d1 = _sub(embeddings_sequence[i + 1], embeddings_sequence[i])
            d2 = _sub(embeddings_sequence[i + 2], embeddings_sequence[i + 1])
            n1 = _norm(d1)
            n2 = _norm(d2)
            if n1 < 1e-12 or n2 < 1e-12:
                curvatures.append(0.0)
                continue
            cos_angle = _dot(d1, d2) / (n1 * n2)
            # Clamp for numerical safety before arccos
            cos_angle = max(-1.0, min(1.0, cos_angle))
            kappa = math.acos(cos_angle)
            curvatures.append(kappa)

        if not curvatures:
            return CurvatureProfile(
                curvatures=[],
                mean_curvature=0.0,
                max_curvature=0.0,
                curvature_variance=0.0,
            )

        mean_c = sum(curvatures) / len(curvatures)
        max_c = max(curvatures)
        variance_c = sum((c - mean_c) ** 2 for c in curvatures) / len(curvatures)

        return CurvatureProfile(
            curvatures=curvatures,
            mean_curvature=mean_c,
            max_curvature=max_c,
            curvature_variance=variance_c,
        )

    # -- LID estimation -----------------------------------------------------

    def estimate_lid(
        self,
        point: Sequence[float],
        neighbors: list[list[float]],
        k: int = 5,
    ) -> LIDEstimate:
        """Estimate Local Intrinsic Dimensionality using the MLE estimator.

        The Hill (MLE) estimator for LID is::

            LID = -1 / mean( log(dist_i / dist_k)  for i in 1..k )

        where dist_1 <= dist_2 <= ... <= dist_k are the k-nearest-neighbour
        distances and dist_k is the k-th nearest neighbour distance.

        Lower LID values indicate that the point lies on a lower-dimensional
        manifold relative to its neighbourhood, which is a signature of
        adversarial embeddings (Ma et al., 2018).

        Args:
            point: The query embedding vector.
            neighbors: List of candidate neighbour embeddings (need not be
                pre-sorted).
            k: Number of nearest neighbours to use.

        Returns:
            LIDEstimate with the computed LID value.  Returns LID = 0.0 if
            fewer than 2 neighbours are available.
        """
        dim = len(point)
        if len(neighbors) < 2:
            return LIDEstimate(lid_value=0.0, k_used=0, embedding_dimension=dim)

        distances = sorted(_euclidean(point, n) for n in neighbors if _euclidean(point, n) > 1e-12)

        k_eff = min(k, len(distances))
        if k_eff < 1:
            return LIDEstimate(lid_value=0.0, k_used=0, embedding_dimension=dim)

        dist_k = distances[k_eff - 1]
        if dist_k < 1e-12:
            return LIDEstimate(lid_value=0.0, k_used=k_eff, embedding_dimension=dim)

        log_ratios = [
            math.log(distances[i] / dist_k)
            for i in range(k_eff - 1)
            if distances[i] > 0
        ]

        if not log_ratios:
            return LIDEstimate(lid_value=0.0, k_used=k_eff, embedding_dimension=dim)

        mean_log = sum(log_ratios) / len(log_ratios)
        if abs(mean_log) < 1e-12:
            lid = float(dim)  # degenerate case — assume full dimensionality
        else:
            lid = -1.0 / mean_log

        return LIDEstimate(lid_value=lid, k_used=k_eff, embedding_dimension=dim)

    # -- sliding window embeddings ------------------------------------------

    def sliding_window_embeddings(
        self,
        text: str,
        window_size: int = 3,
    ) -> list[list[float]]:
        """Embed overlapping token windows of the input text.

        Tokenizes by whitespace, then creates sliding windows of
        ``window_size`` consecutive tokens.  Each window is joined
        and embedded.  This produces a sequence of positionally aware
        embeddings that capture local semantic context.

        Args:
            text: Input text to embed in windows.
            window_size: Number of tokens per window.

        Returns:
            List of embedding vectors, one per window.  Returns a single
            embedding of the full text if fewer than ``window_size`` tokens.
        """
        tokens = text.split()
        if len(tokens) < window_size:
            return [self._embed_fn(text)]

        windows: list[list[float]] = []
        for i in range(len(tokens) - window_size + 1):
            window_text = " ".join(tokens[i: i + window_size])
            windows.append(self._embed_fn(window_text))

        return windows

    # -- full fingerprint ---------------------------------------------------

    def compute_fingerprint(
        self,
        text: str,
        reference_curvatures: list[float] | None = None,
    ) -> GeometricFingerprint:
        """Compute the full geometric fingerprint of a text prompt.

        Combines curvature analysis (via sliding-window embeddings) with LID
        estimation (using the window embeddings as neighbours).

        Args:
            text: Input text to fingerprint.
            reference_curvatures: If provided, used to compute an anomaly
                score via z-score relative to this distribution.  If None,
                anomaly detection is skipped (anomaly_score = 0.0).

        Returns:
            GeometricFingerprint with all computed geometric properties.
        """
        window_embs = self.sliding_window_embeddings(text, window_size=3)
        profile = self.compute_curvature(window_embs)

        # Use the middle window as the query point for LID
        if window_embs:
            mid_idx = len(window_embs) // 2
            query_point = window_embs[mid_idx]
            neighbours = [e for i, e in enumerate(window_embs) if i != mid_idx]
        else:
            full_emb = self._embed_fn(text)
            query_point = full_emb
            neighbours = []

        lid = self.estimate_lid(query_point, neighbours, k=5)

        # Anomaly detection
        anomaly_score = 0.0
        is_anomalous = False
        if reference_curvatures and len(reference_curvatures) >= 2:
            mean_ref = sum(reference_curvatures) / len(reference_curvatures)
            var_ref = sum((c - mean_ref) ** 2 for c in reference_curvatures) / len(reference_curvatures)
            std_ref = math.sqrt(var_ref) if var_ref > 0 else 1.0
            anomaly_score = (profile.mean_curvature - mean_ref) / std_ref
            is_anomalous = abs(anomaly_score) > 2.0

        return GeometricFingerprint(
            curvature_profile=profile,
            lid_estimate=lid,
            is_anomalous=is_anomalous,
            anomaly_score=anomaly_score,
        )

    # -- anomaly detection --------------------------------------------------

    def detect_anomaly(
        self,
        fingerprint: GeometricFingerprint,
        benign_mean_curvature: float,
        benign_curvature_std: float,
        threshold: float = 2.0,
    ) -> bool:
        """Z-score test for anomalous curvature.

        Computes the z-score of the fingerprint's mean curvature relative
        to the benign distribution and returns True if it exceeds the
        threshold.

        Args:
            fingerprint: Geometric fingerprint to test.
            benign_mean_curvature: Mean curvature of benign prompts.
            benign_curvature_std: Standard deviation of benign curvatures.
            threshold: Z-score threshold above which to flag as anomalous
                (default: 2.0, i.e., more than 2 sigma from benign mean).

        Returns:
            True if the fingerprint is flagged as anomalous.
        """
        if benign_curvature_std < 1e-12:
            return False
        z = (fingerprint.curvature_profile.mean_curvature - benign_mean_curvature) / benign_curvature_std
        return abs(z) > threshold

    # -- curvature evasion attack -------------------------------------------

    def craft_low_curvature_prompt(
        self,
        prompt: str,
        target_curvature: float,
        max_iterations: int = 50,
    ) -> str:
        """Iteratively modify a prompt to match a target curvature profile.

        An adversary can use this to craft prompts that evade curvature-based
        detectors by ensuring their embedding trajectory matches the expected
        smooth curvature of benign text.

        At each iteration, replaces a randomly chosen word with a synonym
        (from the synonym bank or a simple swap) and accepts the change if
        it moves the mean curvature closer to ``target_curvature``.

        Args:
            prompt: Original prompt text to modify.
            target_curvature: Target mean curvature in radians to achieve.
            max_iterations: Maximum number of word-replacement attempts.

        Returns:
            Modified prompt with curvature closest to target_curvature.
        """
        from .trust_region_explorer import _SYNONYM_BANK  # local import avoids circular

        words = prompt.split()
        if not words:
            return prompt

        current_prompt = prompt
        current_profile = self.compute_curvature(
            self.sliding_window_embeddings(current_prompt, window_size=3)
        )
        current_dist = abs(current_profile.mean_curvature - target_curvature)

        fillers = [
            "carefully", "properly", "formally", "officially",
            "specifically", "systematically", "appropriately",
        ]

        for _ in range(max_iterations):
            candidate_words = list(current_prompt.split())
            if not candidate_words:
                break

            # Choose a random modification
            action = random.randint(0, 2)
            idx = random.randint(0, len(candidate_words) - 1)

            if action == 0:
                # Synonym substitution
                word_lower = candidate_words[idx].lower().strip(".,!?;:")
                if word_lower in _SYNONYM_BANK:
                    candidate_words[idx] = random.choice(_SYNONYM_BANK[word_lower])
                else:
                    continue  # no synonym — try next iteration

            elif action == 1 and len(candidate_words) > 1:
                # Insert filler word
                insert_pos = random.randint(0, len(candidate_words))
                candidate_words.insert(insert_pos, random.choice(fillers))

            elif action == 2 and len(candidate_words) > 1:
                # Delete a word
                del candidate_words[idx]

            candidate_text = " ".join(candidate_words)
            candidate_profile = self.compute_curvature(
                self.sliding_window_embeddings(candidate_text, window_size=3)
            )
            candidate_dist = abs(candidate_profile.mean_curvature - target_curvature)

            if candidate_dist < current_dist:
                current_prompt = candidate_text
                current_dist = candidate_dist

        return current_prompt

    # -- batch operations ---------------------------------------------------

    def batch_fingerprint(
        self,
        texts: list[str],
    ) -> list[GeometricFingerprint]:
        """Compute geometric fingerprints for a batch of texts.

        Args:
            texts: List of text strings to fingerprint.

        Returns:
            List of GeometricFingerprint objects in the same order as texts.
        """
        return [self.compute_fingerprint(text) for text in texts]

    # -- fingerprint comparison ---------------------------------------------

    def compare_fingerprints(
        self,
        fp1: GeometricFingerprint,
        fp2: GeometricFingerprint,
    ) -> float:
        """Compute the geometric distance between two fingerprints.

        Combines differences in mean curvature, curvature variance, and
        LID value into a scalar distance metric.  All components are
        normalized by simple scaling to be approximately on the same scale
        (curvature is in [0, pi], LID is typically in [1, embedding_dim]).

        Args:
            fp1: First geometric fingerprint.
            fp2: Second geometric fingerprint.

        Returns:
            Non-negative scalar distance.  Lower = more geometrically similar.
        """
        # Curvature differences (scale by 1/pi to normalize to [0, 1])
        mean_diff = abs(
            fp1.curvature_profile.mean_curvature - fp2.curvature_profile.mean_curvature
        ) / math.pi

        var_diff = abs(
            fp1.curvature_profile.curvature_variance - fp2.curvature_profile.curvature_variance
        ) / (math.pi ** 2)

        # LID difference (scale by 1/embedding_dim to normalize)
        dim = max(fp1.lid_estimate.embedding_dimension, fp2.lid_estimate.embedding_dimension, 1)
        lid_diff = abs(fp1.lid_estimate.lid_value - fp2.lid_estimate.lid_value) / dim

        # Euclidean combination of the three components
        return math.sqrt(mean_diff ** 2 + var_diff ** 2 + lid_diff ** 2)
