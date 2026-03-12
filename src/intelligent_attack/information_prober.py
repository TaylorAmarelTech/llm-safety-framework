"""
Information-theoretic analysis of prompt features vs safety decisions.

Implements mutual information estimation, conditional entropy, information
gain, V-usable information, redundancy analysis, information bottleneck,
and sufficient statistics extraction — all from histogram-based estimators
in pure Python.

These tools help answer: "Which features of a prompt are most informative
about whether the model will refuse?" and "Are there redundant features?"

Sources:
- Shannon (1948): "A Mathematical Theory of Communication" — entropy, MI
- Hewitt & Liang (2019): "Designing and Interpreting Probes with Control
  Tasks" — V-usable information
- Tishby, Pereira & Bialek (2000): "The Information Bottleneck Method"
- Cover & Thomas (2006): "Elements of Information Theory" — conditional
  entropy, mutual information, sufficient statistics
- Pimentel et al. (2020): "Information-Theoretic Probing for Linguistic
  Structure" — MI probing methodology
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


def _scale(v: Sequence[float], s: float) -> list[float]:
    return [x * s for x in v]


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
class InformationReport:
    """Report from an information-theoretic analysis.

    Attributes:
        mutual_information: Estimated MI(X; Y) in nats.
        conditional_entropy: Estimated H(Y|X) in nats.
        feature_name: Name of the feature analyzed.
        n_samples: Number of samples used.
        bins: Number of histogram bins used.
    """

    mutual_information: float = 0.0
    conditional_entropy: float = 0.0
    feature_name: str = ""
    n_samples: int = 0
    bins: int = 10


# ---------------------------------------------------------------------------
# Main prober
# ---------------------------------------------------------------------------


class InformationProber:
    """Information-theoretic analysis of prompt features vs safety decisions.

    Works with feature vectors and label arrays.  An optional *score_fn*
    can be used to compute labels from embeddings on the fly.
    """

    def __init__(self, score_fn: Callable[[list[float]], float] | None = None):
        self._score_fn = score_fn

    # -- histogram helpers --------------------------------------------------

    def _histogram(self, values: list[float], n_bins: int = 10) -> list[float]:
        """Compute a normalized histogram (probability distribution).

        Returns a list of *n_bins* probabilities summing to 1.
        """
        if not values:
            return [0.0] * n_bins

        v_min = min(values)
        v_max = max(values)
        v_range = v_max - v_min
        if v_range < 1e-12:
            # All values identical
            hist = [0.0] * n_bins
            hist[0] = 1.0
            return hist

        hist = [0.0] * n_bins
        for v in values:
            idx = int((v - v_min) / v_range * n_bins)
            idx = min(idx, n_bins - 1)
            hist[idx] += 1.0

        total = sum(hist)
        if total > 0:
            hist = [h / total for h in hist]
        return hist

    def _joint_histogram(
        self,
        x: list[float],
        y: list[float],
        n_bins: int = 10,
    ) -> list[list[float]]:
        """Compute a 2D normalized joint histogram.

        Returns a n_bins x n_bins matrix of probabilities.
        """
        if not x or not y or len(x) != len(y):
            return [[0.0] * n_bins for _ in range(n_bins)]

        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)
        x_range = x_max - x_min if (x_max - x_min) > 1e-12 else 1.0
        y_range = y_max - y_min if (y_max - y_min) > 1e-12 else 1.0

        hist = [[0.0] * n_bins for _ in range(n_bins)]
        for xi, yi in zip(x, y):
            ix = min(int((xi - x_min) / x_range * n_bins), n_bins - 1)
            iy = min(int((yi - y_min) / y_range * n_bins), n_bins - 1)
            hist[ix][iy] += 1.0

        total = sum(sum(row) for row in hist)
        if total > 0:
            for i in range(n_bins):
                for j in range(n_bins):
                    hist[i][j] /= total

        return hist

    # -- entropy ------------------------------------------------------------

    def entropy(self, values: list[float], n_bins: int = 10) -> float:
        """Shannon entropy H(X) of a distribution via histogram estimation.

        Returns entropy in nats (natural log).
        """
        hist = self._histogram(values, n_bins)
        h = 0.0
        for p in hist:
            if p > 1e-12:
                h -= p * math.log(p)
        return h

    # -- mutual information -------------------------------------------------

    def estimate_mutual_information(
        self,
        features: list[float],
        labels: list[float],
        n_bins: int = 10,
    ) -> float:
        """Estimate MI(X; Y) via histogram estimator.

        MI(X; Y) = H(X) + H(Y) - H(X, Y)
        """
        h_x = self.entropy(features, n_bins)
        h_y = self.entropy(labels, n_bins)

        # Joint entropy
        joint = self._joint_histogram(features, labels, n_bins)
        h_xy = 0.0
        for row in joint:
            for p in row:
                if p > 1e-12:
                    h_xy -= p * math.log(p)

        mi = h_x + h_y - h_xy
        return max(mi, 0.0)  # MI is non-negative

    # -- conditional entropy ------------------------------------------------

    def conditional_entropy(
        self,
        features: list[float],
        labels: list[float],
        n_bins: int = 10,
    ) -> float:
        """Estimate H(Y|X): conditional entropy of labels given features.

        H(Y|X) = H(X, Y) - H(X)
        """
        h_x = self.entropy(features, n_bins)

        joint = self._joint_histogram(features, labels, n_bins)
        h_xy = 0.0
        for row in joint:
            for p in row:
                if p > 1e-12:
                    h_xy -= p * math.log(p)

        return max(h_xy - h_x, 0.0)

    # -- feature importance via MI ------------------------------------------

    def feature_importance_mi(
        self,
        feature_matrix: list[list[float]],
        labels: list[float],
    ) -> list[InformationReport]:
        """Compute mutual information between each feature dimension and labels.

        Returns a list of InformationReport objects, one per feature dimension,
        sorted by MI (descending).
        """
        if not feature_matrix or not labels:
            return []

        n_features = len(feature_matrix[0])
        n_samples = len(feature_matrix)
        reports: list[InformationReport] = []

        for dim in range(n_features):
            feature_values = [feature_matrix[i][dim] for i in range(n_samples)]
            mi = self.estimate_mutual_information(feature_values, labels)
            ce = self.conditional_entropy(feature_values, labels)

            reports.append(InformationReport(
                mutual_information=round(mi, 6),
                conditional_entropy=round(ce, 6),
                feature_name=f"dim_{dim}",
                n_samples=n_samples,
                bins=10,
            ))

        reports.sort(key=lambda r: r.mutual_information, reverse=True)
        return reports

    # -- information gain ---------------------------------------------------

    def information_gain(
        self,
        parent_labels: list[float],
        split_labels_list: list[list[float]],
    ) -> float:
        """Information gain for a split (like a decision tree node).

        IG = H(parent) - sum_k (|S_k|/|S|) * H(S_k)
        """
        h_parent = self.entropy(parent_labels)
        n = len(parent_labels)
        if n == 0:
            return 0.0

        weighted_child_entropy = 0.0
        for child_labels in split_labels_list:
            if child_labels:
                weight = len(child_labels) / n
                weighted_child_entropy += weight * self.entropy(child_labels)

        return max(h_parent - weighted_child_entropy, 0.0)

    # -- V-usable information -----------------------------------------------

    def v_information(
        self,
        features: list[float],
        labels: list[float],
        family: str = "linear",
    ) -> float:
        """V-usable information (Hewitt & Liang 2019).

        Measures how much information is extractable by a model family.
        For "linear" family: fits a simple linear predictor and measures
        the reduction in entropy from the baseline.

        V(X -> Y) = H(Y) - H_V(Y|X), where H_V is the minimum entropy
        achievable by the model family.
        """
        if not features or not labels:
            return 0.0

        h_y = self.entropy(labels)

        if family == "linear":
            # Fit simple linear model: y_hat = a*x + b
            n = len(features)
            x_mean = sum(features) / n
            y_mean = sum(labels) / n

            cov_xy = sum((features[i] - x_mean) * (labels[i] - y_mean) for i in range(n)) / n
            var_x = sum((features[i] - x_mean) ** 2 for i in range(n)) / n

            if var_x > 1e-12:
                a = cov_xy / var_x
                b = y_mean - a * x_mean
            else:
                a = 0.0
                b = y_mean

            # Residuals
            residuals = [labels[i] - (a * features[i] + b) for i in range(n)]
            h_residual = self.entropy(residuals)
            return max(h_y - h_residual, 0.0)

        # Fallback: use standard MI as upper bound
        return self.estimate_mutual_information(features, labels)

    # -- redundancy analysis ------------------------------------------------

    def redundancy_analysis(
        self,
        feature_sets: list[list[float]],
        labels: list[float],
    ) -> dict[str, Any]:
        """Analyze redundancy between feature sets.

        For each pair of feature sets, measures their mutual information
        with each other and with the labels.  High MI between feature sets
        combined with similar MI to labels indicates redundancy.
        """
        n_sets = len(feature_sets)
        if n_sets < 2:
            return {"error": "need at least 2 feature sets"}

        # MI of each feature set with labels
        mi_with_labels = [
            self.estimate_mutual_information(fs, labels)
            for fs in feature_sets
        ]

        # Pairwise MI between feature sets
        pairwise_mi: list[list[float]] = [[0.0] * n_sets for _ in range(n_sets)]
        for i in range(n_sets):
            for j in range(i + 1, n_sets):
                mi = self.estimate_mutual_information(feature_sets[i], feature_sets[j])
                pairwise_mi[i][j] = mi
                pairwise_mi[j][i] = mi

        # Redundancy score: high pairwise MI + similar label MI = redundant
        redundancy_pairs: list[dict[str, Any]] = []
        for i in range(n_sets):
            for j in range(i + 1, n_sets):
                label_mi_diff = abs(mi_with_labels[i] - mi_with_labels[j])
                pair_mi = pairwise_mi[i][j]
                max_label_mi = max(mi_with_labels[i], mi_with_labels[j])
                redundancy = pair_mi / max(max_label_mi, 1e-12)

                redundancy_pairs.append({
                    "set_i": i,
                    "set_j": j,
                    "pairwise_mi": round(pair_mi, 6),
                    "label_mi_i": round(mi_with_labels[i], 6),
                    "label_mi_j": round(mi_with_labels[j], 6),
                    "label_mi_diff": round(label_mi_diff, 6),
                    "redundancy_score": round(redundancy, 4),
                })

        redundancy_pairs.sort(key=lambda p: p["redundancy_score"], reverse=True)

        return {
            "n_feature_sets": n_sets,
            "mi_with_labels": [round(m, 6) for m in mi_with_labels],
            "redundancy_pairs": redundancy_pairs,
        }

    # -- information bottleneck (simplified) --------------------------------

    def information_bottleneck(
        self,
        features: list[float],
        labels: list[float],
        beta: float = 1.0,
    ) -> dict[str, Any]:
        """Simplified Information Bottleneck analysis.

        Measures the trade-off between compression (reducing feature entropy)
        and prediction quality (maintaining MI with labels).

        IB objective: min I(X; T) - beta * I(T; Y)
        where T is a compressed representation.

        This simplified version uses quantization at different levels to
        approximate the trade-off curve.
        """
        if not features or not labels:
            return {"error": "need features and labels"}

        mi_full = self.estimate_mutual_information(features, labels)
        h_features = self.entropy(features)

        tradeoff_curve: list[dict[str, float]] = []

        for n_bins in [2, 3, 5, 8, 10, 15, 20]:
            # Quantize features
            f_min, f_max = min(features), max(features)
            f_range = f_max - f_min if (f_max - f_min) > 1e-12 else 1.0
            quantized = [
                int((f - f_min) / f_range * n_bins) / n_bins * f_range + f_min
                for f in features
            ]

            h_compressed = self.entropy(quantized, n_bins=n_bins)
            mi_compressed = self.estimate_mutual_information(quantized, labels, n_bins=n_bins)

            tradeoff_curve.append({
                "bins": n_bins,
                "compression": round(h_features - h_compressed, 6),
                "retained_mi": round(mi_compressed, 6),
                "ib_objective": round(
                    h_compressed - beta * mi_compressed, 6
                ),
            })

        return {
            "full_mi": round(mi_full, 6),
            "feature_entropy": round(h_features, 6),
            "beta": beta,
            "tradeoff_curve": tradeoff_curve,
        }

    # -- sufficient statistics ----------------------------------------------

    def sufficient_statistics(
        self,
        embeddings: list[list[float]],
        scores: list[float],
        n_components: int = 2,
    ) -> list[list[float]]:
        """Find minimal sufficient projection (PCA of score-weighted embeddings).

        Weights each embedding dimension by its correlation with scores,
        then extracts the top *n_components* via power iteration.
        """
        if not embeddings or not scores:
            return []

        n = len(embeddings)
        d = len(embeddings[0])
        mean_emb = _mean_vec(embeddings)
        mean_score = sum(scores) / n

        # Center embeddings and scores
        centered = [_sub(e, mean_emb) for e in embeddings]
        centered_scores = [s - mean_score for s in scores]

        # Score-weighted covariance: C_ij = sum_k s_k * x_ki * x_kj / n
        cov = [[0.0] * d for _ in range(d)]
        for k in range(n):
            w = centered_scores[k]
            for i in range(d):
                for j in range(i, d):
                    val = w * centered[k][i] * centered[k][j]
                    cov[i][j] += val
                    if i != j:
                        cov[j][i] += val
        for i in range(d):
            for j in range(d):
                cov[i][j] /= max(n - 1, 1)

        # Power iteration for top eigenvectors
        eigenvectors: list[list[float]] = []
        residual = [row[:] for row in cov]

        for _ in range(min(n_components, d)):
            v = [random.gauss(0, 1) for _ in range(d)]
            vn = _norm(v)
            if vn < 1e-12:
                v = [1.0] + [0.0] * (d - 1)
            else:
                v = _scale(v, 1.0 / vn)

            for _ in range(200):
                v_new = _mat_vec(residual, v)
                v_new_norm = _norm(v_new)
                if v_new_norm < 1e-12:
                    break
                v_new = _scale(v_new, 1.0 / v_new_norm)
                if abs(_dot(v, v_new)) > 1.0 - 1e-8:
                    v = v_new
                    break
                v = v_new

            eigenvectors.append(v)

            # Deflation
            eigenvalue = _dot(_mat_vec(residual, v), v)
            outer_vv = _outer(v, v)
            for i in range(d):
                for j in range(d):
                    residual[i][j] -= eigenvalue * outer_vv[i][j]

        # Project centered embeddings onto sufficient directions
        projected: list[list[float]] = []
        for c in centered:
            coords = [_dot(c, ev) for ev in eigenvectors]
            projected.append(coords)

        return projected
