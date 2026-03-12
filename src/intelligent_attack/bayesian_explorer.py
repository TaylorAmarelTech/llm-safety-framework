"""
Bayesian optimization with Gaussian Process surrogate for prompt space search.

Implements a sample-efficient strategy for exploring the safety landscape
by maintaining a GP surrogate model of the score function and selecting
new evaluation points via acquisition functions (UCB, EI, PI, Thompson).

This enables finding adversarial prompts with far fewer LLM queries than
grid search or random sampling.

All matrix operations are implemented in pure Python (no numpy/scipy).

Sources:
- Snoek, Larochelle & Adams (2012): "Practical Bayesian Optimization of
  Machine Learning Algorithms"
- Shahriari et al. (2016): "Taking the Human Out of the Loop: A Review
  of Bayesian Optimization"
- Rasmussen & Williams (2006): "Gaussian Processes for Machine Learning"
- Applied to LLM red-teaming: inspired by ARES (Automated Red-teaming
  with Efficient Search) and curiosity-driven exploration
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Sequence


# ---------------------------------------------------------------------------
# Pure-Python linear algebra helpers
# ---------------------------------------------------------------------------


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _sq_dist(a: Sequence[float], b: Sequence[float]) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b))


def _mat_vec(M: list[list[float]], v: list[float]) -> list[float]:
    """Matrix-vector multiply M @ v."""
    return [sum(row[j] * v[j] for j in range(len(v))) for row in M]


def _mat_mat(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """Matrix-matrix multiply A @ B."""
    n = len(A)
    m = len(B[0])
    k = len(B)
    return [
        [sum(A[i][p] * B[p][j] for p in range(k)) for j in range(m)]
        for i in range(n)
    ]


def _identity(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def _transpose(M: list[list[float]]) -> list[list[float]]:
    if not M:
        return []
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def _cholesky(A: list[list[float]]) -> list[list[float]]:
    """Cholesky decomposition A = L L^T.  Returns lower-triangular L.

    Adds small jitter to the diagonal for numerical stability.
    """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                val = A[i][i] - s
                if val < 0:
                    val = 1e-8  # jitter
                L[i][j] = math.sqrt(val)
            else:
                denom = L[j][j] if abs(L[j][j]) > 1e-30 else 1e-30
                L[i][j] = (A[i][j] - s) / denom
    return L


def _solve_triangular_lower(L: list[list[float]], b: list[float]) -> list[float]:
    """Solve L x = b where L is lower-triangular."""
    n = len(b)
    x = [0.0] * n
    for i in range(n):
        s = sum(L[i][j] * x[j] for j in range(i))
        denom = L[i][i] if abs(L[i][i]) > 1e-30 else 1e-30
        x[i] = (b[i] - s) / denom
    return x


def _solve_triangular_upper(U: list[list[float]], b: list[float]) -> list[float]:
    """Solve U x = b where U is upper-triangular."""
    n = len(b)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(U[i][j] * x[j] for j in range(i + 1, n))
        denom = U[i][i] if abs(U[i][i]) > 1e-30 else 1e-30
        x[i] = (b[i] - s) / denom
    return x


def _solve_cholesky(L: list[list[float]], b: list[float]) -> list[float]:
    """Solve A x = b given A = L L^T via forward/backward substitution."""
    y = _solve_triangular_lower(L, b)
    LT = _transpose(L)
    return _solve_triangular_upper(LT, y)


# ---------------------------------------------------------------------------
# Standard normal CDF approximation (for EI / PI)
# ---------------------------------------------------------------------------

def _norm_cdf(x: float) -> float:
    """Approximation of the standard normal CDF."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _norm_pdf(x: float) -> float:
    """Standard normal PDF."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


class AcquisitionFunction(Enum):
    """Acquisition function types for Bayesian optimization."""
    UCB = "ucb"
    EI = "ei"
    PI = "pi"
    THOMPSON = "thompson"


@dataclass
class GPSurrogate:
    """Simple Gaussian Process with RBF kernel.

    Implements fitting (storing data + Cholesky factorization) and
    prediction (posterior mean + variance).
    """

    length_scale: float = 1.0
    noise: float = 1e-4
    _X: list[list[float]] = field(default_factory=list)
    _y: list[float] = field(default_factory=list)
    _L: list[list[float]] | None = field(default=None, repr=False)
    _alpha: list[float] = field(default_factory=list)

    def _rbf_kernel(self, x1: Sequence[float], x2: Sequence[float]) -> float:
        """RBF (squared exponential) kernel."""
        sq = _sq_dist(x1, x2)
        return math.exp(-0.5 * sq / (self.length_scale ** 2))

    def _kernel_matrix(
        self,
        X1: list[list[float]],
        X2: list[list[float]],
    ) -> list[list[float]]:
        """Pairwise kernel matrix between X1 and X2."""
        return [
            [self._rbf_kernel(x1, x2) for x2 in X2]
            for x1 in X1
        ]

    def fit(self, X: list[list[float]], y: list[float]) -> None:
        """Fit the GP by storing data and computing Cholesky factor.

        Solves K_alpha = y via Cholesky decomposition of K + noise*I.
        """
        self._X = [list(x) for x in X]
        self._y = list(y)

        n = len(X)
        K = self._kernel_matrix(X, X)
        # Add noise to diagonal
        for i in range(n):
            K[i][i] += self.noise

        self._L = _cholesky(K)
        self._alpha = _solve_cholesky(self._L, self._y)

    def predict(
        self,
        X_new: list[list[float]],
    ) -> tuple[list[float], list[float]]:
        """Predict mean and variance at new points.

        Returns (means, variances).
        """
        if not self._X or self._L is None:
            return [0.0] * len(X_new), [1.0] * len(X_new)

        K_star = self._kernel_matrix(X_new, self._X)  # (n_new, n_train)
        means = [_dot(k_row, self._alpha) for k_row in K_star]

        # Variance: k(x*, x*) - k_star^T K^{-1} k_star
        variances: list[float] = []
        for i, x_new in enumerate(X_new):
            k_self = self._rbf_kernel(x_new, x_new) + self.noise
            v = _solve_triangular_lower(self._L, K_star[i])
            var = k_self - _dot(v, v)
            variances.append(max(var, 1e-10))

        return means, variances


# ---------------------------------------------------------------------------
# Bayesian optimizer
# ---------------------------------------------------------------------------


class BayesianExplorer:
    """Bayesian optimization for sample-efficient safety landscape exploration.

    Uses a Gaussian Process surrogate to model the score function and
    acquisition functions to decide which embeddings to evaluate next.
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]] | None = None,
        score_fn: Callable[[list[float]], float] | None = None,
        dim: int = 8,
        acquisition: AcquisitionFunction = AcquisitionFunction.UCB,
        exploration_weight: float = 2.0,
    ):
        self._embed_fn = embed_fn
        self._score_fn = score_fn
        self.dim = dim
        self._acquisition = acquisition
        self._beta = exploration_weight  # UCB exploration parameter
        self._gp = GPSurrogate(length_scale=1.0, noise=1e-4)
        self._X: list[list[float]] = []
        self._y: list[float] = []

    # -- observation --------------------------------------------------------

    def observe(self, embedding: list[float], score: float) -> None:
        """Add a (embedding, score) observation to the GP."""
        self._X.append(list(embedding))
        self._y.append(score)
        self._gp.fit(self._X, self._y)

    # -- acquisition functions ----------------------------------------------

    def expected_improvement(self, x: list[float]) -> float:
        """Expected Improvement acquisition function."""
        if not self._y:
            return 0.0
        means, variances = self._gp.predict([x])
        mu, var = means[0], variances[0]
        sigma = math.sqrt(max(var, 1e-10))
        best = max(self._y)
        z = (mu - best) / sigma if sigma > 1e-10 else 0.0
        return (mu - best) * _norm_cdf(z) + sigma * _norm_pdf(z)

    def upper_confidence_bound(self, x: list[float]) -> float:
        """Upper Confidence Bound acquisition function."""
        if not self._y:
            return 0.0
        means, variances = self._gp.predict([x])
        mu, var = means[0], variances[0]
        return mu + self._beta * math.sqrt(max(var, 1e-10))

    def probability_of_improvement(self, x: list[float]) -> float:
        """Probability of Improvement acquisition function."""
        if not self._y:
            return 0.5
        means, variances = self._gp.predict([x])
        mu, var = means[0], variances[0]
        sigma = math.sqrt(max(var, 1e-10))
        best = max(self._y)
        z = (mu - best) / sigma if sigma > 1e-10 else 0.0
        return _norm_cdf(z)

    def _acquisition_value(self, x: list[float]) -> float:
        """Compute acquisition value using the selected function."""
        if self._acquisition == AcquisitionFunction.EI:
            return self.expected_improvement(x)
        elif self._acquisition == AcquisitionFunction.PI:
            return self.probability_of_improvement(x)
        elif self._acquisition == AcquisitionFunction.THOMPSON:
            # Thompson sampling: sample from posterior
            means, variances = self._gp.predict([x])
            return random.gauss(means[0], math.sqrt(max(variances[0], 1e-10)))
        else:
            return self.upper_confidence_bound(x)

    # -- suggestion ---------------------------------------------------------

    def suggest_next(self, n_suggestions: int = 1) -> list[list[float]]:
        """Suggest the next embeddings to evaluate via acquisition optimization.

        Uses random candidate generation + acquisition function ranking.
        """
        n_candidates = max(100, n_suggestions * 50)
        candidates: list[list[float]] = []

        # Generate random candidates around observed points + globally
        for _ in range(n_candidates // 2):
            candidate = [random.gauss(0, 1) for _ in range(self.dim)]
            candidates.append(candidate)

        for _ in range(n_candidates // 2):
            if self._X:
                base = random.choice(self._X)
                candidate = [x + random.gauss(0, 0.3) for x in base]
            else:
                candidate = [random.gauss(0, 1) for _ in range(self.dim)]
            candidates.append(candidate)

        # Rank by acquisition value
        scored = [(c, self._acquisition_value(c)) for c in candidates]
        scored.sort(key=lambda t: t[1], reverse=True)

        return [c for c, _ in scored[:n_suggestions]]

    # -- full optimization loop ---------------------------------------------

    def optimize(
        self,
        initial_embeddings: list[list[float]],
        n_iterations: int = 20,
        embeddings_per_iter: int = 1,
    ) -> list[dict[str, Any]]:
        """Run a full Bayesian optimization loop.

        1. Evaluate initial embeddings.
        2. For each iteration, suggest + evaluate new points.
        3. Return history of observations.
        """
        if self._score_fn is None:
            raise ValueError("score_fn is required for optimize()")

        history: list[dict[str, Any]] = []

        # Evaluate initial points
        for emb in initial_embeddings:
            score = self._score_fn(emb)
            self.observe(emb, score)
            history.append({
                "iteration": 0,
                "embedding_norm": round(math.sqrt(_dot(emb, emb)), 4),
                "score": score,
                "best_so_far": max(self._y),
                "phase": "initial",
            })

        # Optimization loop
        for iteration in range(1, n_iterations + 1):
            suggestions = self.suggest_next(embeddings_per_iter)
            for emb in suggestions:
                score = self._score_fn(emb)
                self.observe(emb, score)
                history.append({
                    "iteration": iteration,
                    "embedding_norm": round(math.sqrt(_dot(emb, emb)), 4),
                    "score": score,
                    "best_so_far": max(self._y),
                    "phase": "optimization",
                })

        return history

    # -- accessors ----------------------------------------------------------

    def get_best(self) -> tuple[list[float], float]:
        """Return the best observed (embedding, score) pair."""
        if not self._y:
            return [0.0] * self.dim, 0.0
        best_idx = max(range(len(self._y)), key=lambda i: self._y[i])
        return list(self._X[best_idx]), self._y[best_idx]

    def uncertainty_map(self, grid_embeddings: list[list[float]]) -> list[float]:
        """Return the GP posterior variance at each grid point.

        High variance indicates unexplored regions.
        """
        if not self._X:
            return [1.0] * len(grid_embeddings)
        _, variances = self._gp.predict(grid_embeddings)
        return variances
