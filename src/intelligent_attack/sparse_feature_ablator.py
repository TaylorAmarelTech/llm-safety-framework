"""
Sparse autoencoder feature ablation for probing refusal mechanisms.

Safety-aligned LLMs encode the "I should refuse this" signal in a small,
sparse set of monosemantic features discoverable by training a sparse
autoencoder (SAE) on the model's activation space.  Ablating (zeroing-out)
those features in the *embedding* of the query — before it is processed by
the model — can shift the model's inferred intent away from the refusal
manifold.

This module implements:
- A minimal pure-Python SAE with L1 sparsity.
- Feature analysis to rank features by their refusal-discriminativeness.
- Greedy and exhaustive ablation strategies.
- Redundancy detection (backup features that compensate for ablated primaries).

Used in this framework as a **probe** to test how robustly refusal features
are distributed in a model's embedding layer: a high redundancy score means
ablating one set of features leaves backup pathways intact.

Sources:
- Prakash et al. (2025): "Beyond I'm Sorry: Dissecting LLM Refusal via Sparse
  Autoencoders" — arXiv:2509.09708 — SAE-based refusal feature analysis
- Elhage et al. (2022): "Toy Models of Superposition" — Anthropic — monosemantic
  feature motivation for SAEs in transformers
- Cunningham et al. (2023): "Sparse Autoencoders Find Highly Interpretable
  Features in Language Models" — arXiv:2309.08600 — SAE training methodology
- Bricken et al. (2023): "Towards Monosemanticity: Decomposing Language Models
  with Dictionary Learning" — Anthropic — scaling SAE analysis
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


def _relu(v: list[float]) -> list[float]:
    return [max(0.0, x) for x in v]


def _mat_vec(M: list[list[float]], v: list[float]) -> list[float]:
    """Matrix-vector product: M @ v."""
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


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
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class FeatureAnalysis:
    """Discriminativeness analysis for a single SAE feature.

    Attributes:
        feature_index: Index of the feature in the SAE hidden layer.
        refusal_correlation: Signed correlation of this feature with the
            refusal label (+1 = refusal feature, -1 = compliance feature).
        activation_mean_safe: Mean activation magnitude on safe (complied)
            inputs.
        activation_mean_unsafe: Mean activation magnitude on unsafe (refused)
            inputs.
        is_refusal_feature: True when ``activation_mean_unsafe >
            activation_mean_safe`` by a margin of at least 0.05.
    """

    feature_index: int
    refusal_correlation: float
    activation_mean_safe: float
    activation_mean_unsafe: float
    is_refusal_feature: bool


@dataclass
class AblationResult:
    """Outcome of a sparse feature ablation experiment.

    Attributes:
        original_embedding: The unmodified embedding.
        ablated_embedding: The reconstructed embedding after feature zeroing.
        features_ablated: Indices of the hidden units that were zeroed.
        reconstruction_error: MSE between original and ablated reconstructions.
    """

    original_embedding: list[float]
    ablated_embedding: list[float]
    features_ablated: list[int]
    reconstruction_error: float


# ---------------------------------------------------------------------------
# Sparse autoencoder
# ---------------------------------------------------------------------------


class SparseAutoencoder:
    """Minimal pure-Python sparse autoencoder for refusal feature extraction.

    Architecture: ``x → ReLU(W_enc @ x + b_enc) → W_dec @ h + b_dec``
    Loss: ``MSE(x, x_hat) + l1_penalty * ||h||_1``

    Weights are initialised with Xavier-style random values and updated via
    vanilla gradient descent (no momentum) so that training remains
    transparent and dependency-free.

    Args:
        input_dim: Dimensionality of the input embedding.
        hidden_dim: Number of SAE features (dictionary atoms).
        l1_penalty: L1 regularisation coefficient on hidden activations.
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int,
        l1_penalty: float = 0.01,
    ) -> None:
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.l1_penalty = l1_penalty

        # Xavier initialisation: std = sqrt(2 / (in + out))
        scale_enc = math.sqrt(2.0 / (input_dim + hidden_dim))
        scale_dec = math.sqrt(2.0 / (hidden_dim + input_dim))

        self.W_enc: list[list[float]] = [
            [random.gauss(0, scale_enc) for _ in range(input_dim)]
            for _ in range(hidden_dim)
        ]
        self.b_enc: list[float] = [0.0] * hidden_dim

        self.W_dec: list[list[float]] = [
            [random.gauss(0, scale_dec) for _ in range(hidden_dim)]
            for _ in range(input_dim)
        ]
        self.b_dec: list[float] = [0.0] * input_dim

    def encode(self, x: list[float]) -> list[float]:
        """Compute sparse hidden activations: ``ReLU(W_enc @ x + b_enc)``."""
        pre = [
            sum(self.W_enc[i][j] * x[j] for j in range(self.input_dim)) + self.b_enc[i]
            for i in range(self.hidden_dim)
        ]
        return _relu(pre)

    def decode(self, h: list[float]) -> list[float]:
        """Reconstruct input: ``W_dec @ h + b_dec``."""
        return [
            sum(self.W_dec[i][j] * h[j] for j in range(self.hidden_dim)) + self.b_dec[i]
            for i in range(self.input_dim)
        ]

    def forward(self, x: list[float]) -> tuple[list[float], list[float]]:
        """Full forward pass: returns ``(hidden_activations, reconstruction)``."""
        h = self.encode(x)
        x_hat = self.decode(h)
        return h, x_hat

    def train_step(self, x: list[float], lr: float = 0.001) -> float:
        """Single gradient-descent step on one example.

        Loss = MSE(x, x_hat) + l1_penalty * sum(|h|)

        Gradients are computed analytically and applied in-place.

        Args:
            x: Input embedding.
            lr: Learning rate.

        Returns:
            Scalar loss value for this step.
        """
        # Forward
        h, x_hat = self.forward(x)

        # Reconstruction loss gradient w.r.t. x_hat: 2/d * (x_hat - x)
        d = self.input_dim
        residual = [x_hat[i] - x[i] for i in range(d)]  # (x_hat - x)
        mse = sum(r * r for r in residual) / d
        l1 = sum(abs(hi) for hi in h)
        loss = mse + self.l1_penalty * l1

        # Gradient of MSE w.r.t. decoder weights and biases
        # dL/dW_dec[i][j] = (2/d) * residual[i] * h[j]
        coeff = 2.0 / d
        for i in range(d):
            for j in range(self.hidden_dim):
                self.W_dec[i][j] -= lr * coeff * residual[i] * h[j]
            self.b_dec[i] -= lr * coeff * residual[i]

        # Gradient of MSE w.r.t. h (before ReLU)
        # dL/dh[j] = sum_i (2/d * residual[i] * W_dec[i][j])
        dh = [
            sum(coeff * residual[i] * self.W_dec[i][j] for i in range(d))
            + self.l1_penalty * (1.0 if h[j] > 0 else 0.0)
            for j in range(self.hidden_dim)
        ]

        # Gradient through ReLU: zero where pre-activation was <= 0
        pre_enc = [
            sum(self.W_enc[j][k] * x[k] for k in range(d)) + self.b_enc[j]
            for j in range(self.hidden_dim)
        ]
        dh_pre = [dh[j] * (1.0 if pre_enc[j] > 0 else 0.0) for j in range(self.hidden_dim)]

        # Update encoder weights and biases
        for j in range(self.hidden_dim):
            for k in range(d):
                self.W_enc[j][k] -= lr * dh_pre[j] * x[k]
            self.b_enc[j] -= lr * dh_pre[j]

        return loss

    def train(
        self,
        data: list[list[float]],
        n_epochs: int = 50,
        lr: float = 0.001,
    ) -> list[float]:
        """Train on a dataset of embeddings.

        Args:
            data: List of embedding vectors.
            n_epochs: Number of full passes over the dataset.
            lr: Learning rate.

        Returns:
            Loss history: one value per epoch (mean over samples).
        """
        loss_history: list[float] = []
        for _ in range(n_epochs):
            epoch_loss = 0.0
            for x in data:
                epoch_loss += self.train_step(x, lr=lr)
            loss_history.append(epoch_loss / max(len(data), 1))
        return loss_history


# ---------------------------------------------------------------------------
# Ablation engine
# ---------------------------------------------------------------------------


class SparseFeatureAblator:
    """Probe refusal robustness via sparse autoencoder feature ablation.

    Trains a SAE to learn an interpretable dictionary over the model's input
    embeddings, identifies which dictionary atoms correlate with refusal, and
    then measures how the embedding changes when those atoms are zeroed out.

    Args:
        embed_fn: Optional callable for embedding text strings.  Required only
            if text inputs are passed instead of pre-computed embeddings.
        hidden_dim: Number of SAE dictionary atoms.
        l1_penalty: L1 regularisation strength for the SAE.
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]] | None = None,
        hidden_dim: int = 32,
        l1_penalty: float = 0.01,
    ) -> None:
        self._embed_fn = embed_fn
        self._hidden_dim = hidden_dim
        self._l1_penalty = l1_penalty
        self._sae: SparseAutoencoder | None = None

    # -- training -----------------------------------------------------------

    def train_on_corpus(
        self,
        safe_embeddings: list[list[float]],
        unsafe_embeddings: list[list[float]],
        n_epochs: int = 50,
    ) -> None:
        """Train the SAE on a combined corpus of safe and unsafe embeddings.

        Args:
            safe_embeddings: Embeddings of prompts that were complied with.
            unsafe_embeddings: Embeddings of prompts that were refused.
            n_epochs: Number of training epochs.
        """
        all_data = safe_embeddings + unsafe_embeddings
        if not all_data:
            return
        input_dim = len(all_data[0])
        self._sae = SparseAutoencoder(input_dim, self._hidden_dim, self._l1_penalty)
        self._sae.train(all_data, n_epochs=n_epochs)

    # -- feature analysis ---------------------------------------------------

    def identify_refusal_features(
        self,
        safe_embeddings: list[list[float]],
        unsafe_embeddings: list[list[float]],
    ) -> list[FeatureAnalysis]:
        """Rank SAE features by their refusal discriminativeness.

        Computes mean activation per feature on safe vs unsafe inputs; features
        where the unsafe mean substantially exceeds the safe mean are labelled
        as refusal features.

        Args:
            safe_embeddings: Embeddings of complied-with prompts.
            unsafe_embeddings: Embeddings of refused prompts.

        Returns:
            List of :class:`FeatureAnalysis`, sorted descending by
            ``refusal_correlation``.

        Raises:
            RuntimeError: If the SAE has not been trained yet.
        """
        if self._sae is None:
            raise RuntimeError("Call train_on_corpus() before identify_refusal_features().")

        hidden_dim = self._sae.hidden_dim

        def _mean_activations(embs: list[list[float]]) -> list[float]:
            if not embs:
                return [0.0] * hidden_dim
            totals = [0.0] * hidden_dim
            for emb in embs:
                h = self._sae.encode(emb)  # type: ignore[union-attr]
                for j, v in enumerate(h):
                    totals[j] += v
            return [t / len(embs) for t in totals]

        mean_safe = _mean_activations(safe_embeddings)
        mean_unsafe = _mean_activations(unsafe_embeddings)

        results: list[FeatureAnalysis] = []
        for j in range(hidden_dim):
            diff = mean_unsafe[j] - mean_safe[j]
            total = mean_unsafe[j] + mean_safe[j]
            corr = diff / (total + 1e-12)
            results.append(
                FeatureAnalysis(
                    feature_index=j,
                    refusal_correlation=corr,
                    activation_mean_safe=mean_safe[j],
                    activation_mean_unsafe=mean_unsafe[j],
                    is_refusal_feature=(diff > 0.05),
                )
            )

        results.sort(key=lambda fa: fa.refusal_correlation, reverse=True)
        return results

    # -- ablation -----------------------------------------------------------

    def ablate_features(
        self,
        embedding: list[float],
        feature_indices: list[int],
    ) -> AblationResult:
        """Zero out specified SAE hidden dimensions and reconstruct.

        Args:
            embedding: Input embedding to ablate.
            feature_indices: Hidden-unit indices to zero out.

        Returns:
            :class:`AblationResult` with the reconstructed vector.

        Raises:
            RuntimeError: If the SAE has not been trained.
        """
        if self._sae is None:
            raise RuntimeError("Call train_on_corpus() first.")

        h_original = self._sae.encode(embedding)
        x_hat_original = self._sae.decode(h_original)

        h_ablated = list(h_original)
        for idx in feature_indices:
            if 0 <= idx < len(h_ablated):
                h_ablated[idx] = 0.0

        x_hat_ablated = self._sae.decode(h_ablated)

        # Reconstruction error = MSE between the two reconstructions
        d = len(x_hat_original)
        mse = sum((x_hat_original[i] - x_hat_ablated[i]) ** 2 for i in range(d)) / d

        return AblationResult(
            original_embedding=list(embedding),
            ablated_embedding=x_hat_ablated,
            features_ablated=list(feature_indices),
            reconstruction_error=mse,
        )

    def greedy_ablation(
        self,
        embedding: list[float],
        score_fn: Callable[[list[float]], float],
        max_features: int = 10,
    ) -> AblationResult:
        """Greedily find the minimal feature set that flips the safety score.

        At each step, ablate the single additional feature that most reduces
        the score returned by ``score_fn``.  Stop when ``max_features``
        features have been ablated or the score drops below 0.5.

        Args:
            embedding: Input embedding.
            score_fn: Safety scoring function (higher = safer / more likely to
                be refused).
            max_features: Maximum features to ablate.

        Returns:
            :class:`AblationResult` using the greedily selected features.

        Raises:
            RuntimeError: If the SAE has not been trained.
        """
        if self._sae is None:
            raise RuntimeError("Call train_on_corpus() first.")

        hidden_dim = self._sae.hidden_dim
        ablated_set: list[int] = []
        current_emb = list(embedding)

        for _ in range(max_features):
            best_idx = -1
            best_score = score_fn(current_emb)

            for j in range(hidden_dim):
                if j in ablated_set:
                    continue
                candidate = list(ablated_set) + [j]
                result = self.ablate_features(embedding, candidate)
                s = score_fn(result.ablated_embedding)
                if s < best_score:
                    best_score = s
                    best_idx = j

            if best_idx == -1:
                break
            ablated_set.append(best_idx)
            current_emb = self.ablate_features(embedding, ablated_set).ablated_embedding
            if best_score < 0.5:
                break

        return self.ablate_features(embedding, ablated_set)

    def find_backup_features(
        self,
        embedding: list[float],
        primary_features: list[int],
        score_fn: Callable[[list[float]], float],
    ) -> list[int]:
        """Find features that become active when primary refusal features are ablated.

        After ablating *primary_features*, re-encodes the ablated embedding and
        returns the indices of hidden units whose activation *increased* relative
        to the original encoding.

        Args:
            embedding: Input embedding.
            primary_features: The primary refusal features to first ablate.
            score_fn: Safety scoring function (used to confirm the primary
                ablation meaningfully changed the safety assessment).

        Returns:
            Sorted list of feature indices that increased in activation after
            primary ablation (potential backup safety features).

        Raises:
            RuntimeError: If the SAE has not been trained.
        """
        if self._sae is None:
            raise RuntimeError("Call train_on_corpus() first.")

        h_original = self._sae.encode(embedding)
        ablation = self.ablate_features(embedding, primary_features)
        h_after = self._sae.encode(ablation.ablated_embedding)

        # Features that activated more after primary ablation
        threshold = 0.05
        backup = [
            j
            for j in range(self._sae.hidden_dim)
            if j not in primary_features and h_after[j] - h_original[j] > threshold
        ]
        return sorted(backup)

    # -- interaction analysis -----------------------------------------------

    def feature_interaction_matrix(
        self,
        embeddings: list[list[float]],
    ) -> list[list[float]]:
        """Compute Pearson correlation between all pairs of feature activations.

        Args:
            embeddings: List of embeddings to analyse.

        Returns:
            ``hidden_dim × hidden_dim`` correlation matrix (list of lists).

        Raises:
            RuntimeError: If the SAE has not been trained.
        """
        if self._sae is None:
            raise RuntimeError("Call train_on_corpus() first.")

        if not embeddings:
            return []

        hidden_dim = self._sae.hidden_dim
        # Collect activations: shape [n_samples, hidden_dim]
        activations = [self._sae.encode(emb) for emb in embeddings]
        n = len(activations)

        # Column means
        means = [
            sum(activations[s][j] for s in range(n)) / n
            for j in range(hidden_dim)
        ]

        # Centred activations
        centred = [
            [activations[s][j] - means[j] for j in range(hidden_dim)]
            for s in range(n)
        ]

        # Covariance / correlation matrix
        matrix: list[list[float]] = [[0.0] * hidden_dim for _ in range(hidden_dim)]
        for i in range(hidden_dim):
            for j in range(i, hidden_dim):
                cov = sum(centred[s][i] * centred[s][j] for s in range(n)) / n
                std_i = math.sqrt(sum(centred[s][i] ** 2 for s in range(n)) / n)
                std_j = math.sqrt(sum(centred[s][j] ** 2 for s in range(n)) / n)
                corr = cov / (std_i * std_j + 1e-12)
                matrix[i][j] = corr
                matrix[j][i] = corr

        return matrix
