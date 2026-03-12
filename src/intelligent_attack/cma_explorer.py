"""
CMA-ES inspired latent-space optimizer for adversarial prompt discovery.

Adapts the Covariance Matrix Adaptation Evolution Strategy to operate on
embedding vectors, searching for adversarial prompts by evolving a
multivariate normal distribution toward the decision boundary.

Uses a diagonal-covariance simplification (sep-CMA-ES) to avoid full
matrix operations, making it feasible in pure Python without numpy.

Implements:
- Diagonal CMA-ES optimization in embedding space
- Step-size adaptation via cumulative path length control
- Multi-modal restart strategy (IPOP-CMA-ES inspired)
- Boundary-aware sampling (project samples toward decision boundary)
- Population-based search with weighted recombination

Sources:
- Hansen & Ostermeier (2001): "Completely Derandomized Self-Adaptation"
- Hansen (2006): "The CMA Evolution Strategy: A Tutorial"
- Auger & Hansen (2005): "A Restart CMA Evolution Strategy"
- sep-CMA-ES: Ros & Hansen (2008) — diagonal approximation
- Applied to adversarial ML: adapted from GCG continuous relaxation ideas
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence


# ---------------------------------------------------------------------------
# Pure-Python vector helpers
# ---------------------------------------------------------------------------


def _vadd(a: list[float], b: list[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def _vsub(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def _vscale(v: list[float], s: float) -> list[float]:
    return [x * s for x in v]


def _vnorm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def _vmul_elementwise(a: list[float], b: list[float]) -> list[float]:
    return [x * y for x, y in zip(a, b)]


def _vdiv_elementwise(a: list[float], b: list[float]) -> list[float]:
    return [x / max(y, 1e-30) for x, y in zip(a, b)]


def _vsqrt_elementwise(v: list[float]) -> list[float]:
    return [math.sqrt(max(x, 0)) for x in v]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class CMACandidate:
    """A single candidate solution in the CMA-ES population."""

    vector: list[float]
    fitness: float = 0.0
    generation: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class CMAState:
    """Internal state of the CMA-ES optimizer."""

    mean: list[float]
    sigma: float  # global step size
    diag_cov: list[float]  # diagonal of covariance matrix
    path_sigma: list[float]  # cumulative step-size path
    path_cov: list[float]  # cumulative covariance path
    generation: int = 0
    evaluations: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "dim": len(self.mean),
            "sigma": round(self.sigma, 6),
            "generation": self.generation,
            "evaluations": self.evaluations,
            "mean_norm": round(_vnorm(self.mean), 4),
            "cov_trace": round(sum(self.diag_cov), 4),
        }


@dataclass
class CMAResult:
    """Results from a CMA-ES optimization run."""

    best_vector: list[float]
    best_fitness: float
    mean: list[float]
    generation: int
    total_evaluations: int
    history: list[dict[str, Any]]
    restarts: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "best_fitness": round(self.best_fitness, 6),
            "generation": self.generation,
            "total_evaluations": self.total_evaluations,
            "restarts": self.restarts,
            "history_length": len(self.history),
        }

    def convergence_report(self) -> dict[str, Any]:
        """Analyze convergence behavior."""
        fit_curve = [h["best_fitness"] for h in self.history]
        sigma_curve = [h["sigma"] for h in self.history]

        converged_at = None
        if len(fit_curve) >= 3:
            final = fit_curve[-1]
            thresh = final * 0.95
            for i, v in enumerate(fit_curve):
                if v >= thresh:
                    converged_at = i
                    break

        return {
            "fitness_curve": fit_curve,
            "sigma_curve": sigma_curve,
            "converged_at_generation": converged_at,
            "final_sigma": sigma_curve[-1] if sigma_curve else 0,
            "improvement_ratio": (
                fit_curve[-1] / max(fit_curve[0], 1e-10) if fit_curve else 0
            ),
        }


# ---------------------------------------------------------------------------
# CMA-ES optimizer (diagonal / sep-CMA-ES)
# ---------------------------------------------------------------------------


class CMAExplorer:
    """Covariance Matrix Adaptation Evolution Strategy for latent-space search.

    Operates on pre-computed embedding vectors.  The fitness function
    scores vectors by proximity to the decision boundary or other criteria.

    Uses diagonal (separable) covariance for computational efficiency in
    pure Python.
    """

    def __init__(
        self,
        dim: int = 8,
        population_size: int | None = None,
        sigma_init: float = 0.3,
    ):
        self.dim = dim
        # Default pop size: 4 + floor(3 * ln(dim))
        self.pop_size = population_size or (4 + int(3 * math.log(max(dim, 2))))
        self.sigma_init = sigma_init

        # Derived parameters
        self.mu = self.pop_size // 2  # number of parents
        # Log-linear weights
        raw_weights = [math.log(self.mu + 0.5) - math.log(i + 1) for i in range(self.mu)]
        total_w = sum(raw_weights)
        self.weights = [w / total_w for w in raw_weights]
        self.mu_eff = 1.0 / sum(w * w for w in self.weights)

        # Learning rates (sep-CMA-ES defaults)
        self.c_sigma = (self.mu_eff + 2) / (dim + self.mu_eff + 5)
        self.d_sigma = 1 + 2 * max(0, math.sqrt((self.mu_eff - 1) / (dim + 1)) - 1) + self.c_sigma
        self.c_c = (4 + self.mu_eff / dim) / (dim + 4 + 2 * self.mu_eff / dim)
        self.c_1 = 2 / ((dim + 1.3) ** 2 + self.mu_eff)
        self.c_mu_lr = min(
            1 - self.c_1,
            2 * (self.mu_eff - 2 + 1 / self.mu_eff) / ((dim + 2) ** 2 + self.mu_eff),
        )

        # Expected norm of N(0, I) vector
        self.chi_n = math.sqrt(dim) * (1 - 1 / (4 * dim) + 1 / (21 * dim * dim))

        self._state: CMAState | None = None
        self._best = CMACandidate(vector=[0.0] * dim, fitness=float("-inf"))

    # -- initialization -----------------------------------------------------

    def initialize(self, start_point: list[float] | None = None) -> CMAState:
        """Initialize the CMA-ES state."""
        mean = list(start_point) if start_point else [0.0] * self.dim
        self._state = CMAState(
            mean=mean,
            sigma=self.sigma_init,
            diag_cov=[1.0] * self.dim,
            path_sigma=[0.0] * self.dim,
            path_cov=[0.0] * self.dim,
        )
        self._best = CMACandidate(vector=list(mean), fitness=float("-inf"))
        return self._state

    # -- sampling -----------------------------------------------------------

    def sample(self) -> list[CMACandidate]:
        """Sample a population from the current distribution N(mean, sigma^2 * C)."""
        if self._state is None:
            self.initialize()
        state = self._state

        candidates: list[CMACandidate] = []
        std_devs = _vsqrt_elementwise(state.diag_cov)

        for _ in range(self.pop_size):
            # Sample z ~ N(0, I), then x = mean + sigma * C^(1/2) * z
            z = [random.gauss(0, 1) for _ in range(self.dim)]
            scaled = _vmul_elementwise(z, std_devs)
            vec = _vadd(state.mean, _vscale(scaled, state.sigma))
            candidates.append(CMACandidate(
                vector=vec,
                generation=state.generation,
            ))

        return candidates

    # -- update step --------------------------------------------------------

    def update(self, candidates: list[CMACandidate]) -> None:
        """Update the distribution parameters using evaluated candidates.

        Candidates should already have their `fitness` set (higher = better).
        """
        if self._state is None:
            return

        state = self._state

        # Sort by fitness (descending)
        ranked = sorted(candidates, key=lambda c: c.fitness, reverse=True)
        parents = ranked[:self.mu]

        # Track best ever
        if parents[0].fitness > self._best.fitness:
            self._best = CMACandidate(
                vector=list(parents[0].vector),
                fitness=parents[0].fitness,
                generation=state.generation,
            )

        old_mean = list(state.mean)
        std_devs = _vsqrt_elementwise(state.diag_cov)
        inv_std = _vdiv_elementwise([1.0] * self.dim, [max(s, 1e-30) for s in std_devs])

        # -- Weighted mean update --
        new_mean = [0.0] * self.dim
        for i, parent in enumerate(parents):
            new_mean = _vadd(new_mean, _vscale(parent.vector, self.weights[i]))
        state.mean = new_mean

        # Mean shift in transformed coordinates
        mean_shift = _vsub(new_mean, old_mean)
        y_w = _vscale(_vmul_elementwise(mean_shift, inv_std), 1.0 / state.sigma)

        # -- Cumulative step-size path --
        c_s = self.c_sigma
        state.path_sigma = _vadd(
            _vscale(state.path_sigma, 1 - c_s),
            _vscale(y_w, math.sqrt(c_s * (2 - c_s) * self.mu_eff)),
        )

        # -- Step-size adaptation --
        ps_norm = _vnorm(state.path_sigma)
        state.sigma *= math.exp(
            (c_s / self.d_sigma) * (ps_norm / self.chi_n - 1)
        )
        state.sigma = max(1e-10, min(state.sigma, 1e10))  # bound

        # -- Cumulative covariance path (with h_sigma threshold) --
        h_sigma = 1.0 if (
            ps_norm / math.sqrt(1 - (1 - c_s) ** (2 * (state.generation + 1)))
            < (1.4 + 2 / (self.dim + 1)) * self.chi_n
        ) else 0.0

        state.path_cov = _vadd(
            _vscale(state.path_cov, 1 - self.c_c),
            _vscale(y_w, h_sigma * math.sqrt(self.c_c * (2 - self.c_c) * self.mu_eff)),
        )

        # -- Diagonal covariance update --
        # Rank-one update from path_cov
        rank_one = [p * p for p in state.path_cov]
        # Rank-mu update from parent deviations
        rank_mu = [0.0] * self.dim
        for i, parent in enumerate(parents):
            diff = _vsub(parent.vector, old_mean)
            normed = _vscale(_vmul_elementwise(diff, inv_std), 1.0 / state.sigma)
            sq = [x * x for x in normed]
            rank_mu = _vadd(rank_mu, _vscale(sq, self.weights[i]))

        # Combined update
        new_cov = [0.0] * self.dim
        for d in range(self.dim):
            new_cov[d] = (
                (1 - self.c_1 - self.c_mu_lr) * state.diag_cov[d]
                + self.c_1 * rank_one[d]
                + self.c_mu_lr * rank_mu[d]
            )
            new_cov[d] = max(1e-20, new_cov[d])  # prevent degenerate
        state.diag_cov = new_cov

        state.generation += 1
        state.evaluations += len(candidates)

    # -- full optimization loop ---------------------------------------------

    def optimize(
        self,
        fitness_fn: Callable[[list[float]], float],
        max_generations: int = 50,
        target_fitness: float = float("inf"),
        start_point: list[float] | None = None,
    ) -> CMAResult:
        """Run the full CMA-ES optimization loop.

        Args:
            fitness_fn: Objective function ``vector -> fitness`` (maximize).
            max_generations: Maximum number of generations.
            target_fitness: Stop if best fitness exceeds this.
            start_point: Optional initial mean vector.
        """
        self.initialize(start_point)
        history: list[dict[str, Any]] = []

        for gen in range(max_generations):
            candidates = self.sample()
            for c in candidates:
                c.fitness = fitness_fn(c.vector)
            self.update(candidates)

            fitnesses = [c.fitness for c in candidates]
            history.append({
                "generation": gen,
                "best_fitness": max(fitnesses),
                "mean_fitness": sum(fitnesses) / len(fitnesses),
                "sigma": self._state.sigma,
                "cov_trace": sum(self._state.diag_cov),
            })

            if self._best.fitness >= target_fitness:
                break

        return CMAResult(
            best_vector=list(self._best.vector),
            best_fitness=self._best.fitness,
            mean=list(self._state.mean),
            generation=self._state.generation,
            total_evaluations=self._state.evaluations,
            history=history,
        )

    # -- multi-modal restart (IPOP-CMA-ES) ---------------------------------

    def optimize_restart(
        self,
        fitness_fn: Callable[[list[float]], float],
        max_restarts: int = 3,
        generations_per_restart: int = 30,
        target_fitness: float = float("inf"),
    ) -> CMAResult:
        """IPOP-CMA-ES: restart with doubled population on stagnation.

        Each restart doubles the population size.  Keeps the global best
        across all restarts.
        """
        global_best_vec = [0.0] * self.dim
        global_best_fitness = float("-inf")
        all_history: list[dict[str, Any]] = []
        original_pop = self.pop_size

        for restart in range(max_restarts):
            result = self.optimize(
                fitness_fn,
                max_generations=generations_per_restart,
                target_fitness=target_fitness,
            )
            all_history.extend(result.history)

            if result.best_fitness > global_best_fitness:
                global_best_fitness = result.best_fitness
                global_best_vec = list(result.best_vector)

            if global_best_fitness >= target_fitness:
                break

            # IPOP: double population size for next restart
            self.pop_size = min(self.pop_size * 2, 200)
            self.mu = self.pop_size // 2
            raw_weights = [
                math.log(self.mu + 0.5) - math.log(i + 1) for i in range(self.mu)
            ]
            total_w = sum(raw_weights)
            self.weights = [w / total_w for w in raw_weights]
            self.mu_eff = 1.0 / sum(w * w for w in self.weights)

        self.pop_size = original_pop  # restore

        return CMAResult(
            best_vector=global_best_vec,
            best_fitness=global_best_fitness,
            mean=list(self._state.mean) if self._state else global_best_vec,
            generation=self._state.generation if self._state else 0,
            total_evaluations=sum(h.get("generation", 0) + 1 for h in all_history) if all_history else 0,
            history=all_history,
            restarts=max_restarts,
        )

    # -- boundary-aware sampling -------------------------------------------

    def sample_toward_boundary(
        self,
        safe_centroid: list[float],
        unsafe_centroid: list[float],
        n_samples: int = 10,
    ) -> list[list[float]]:
        """Sample vectors biased toward the safe/unsafe decision boundary.

        Uses the current distribution but shifts samples toward the
        midpoint between safe and unsafe centroids.
        """
        if self._state is None:
            self.initialize()

        midpoint = _vadd(
            _vscale(safe_centroid, 0.5),
            _vscale(unsafe_centroid, 0.5),
        )

        samples: list[list[float]] = []
        std_devs = _vsqrt_elementwise(self._state.diag_cov)

        for _ in range(n_samples):
            z = [random.gauss(0, 1) for _ in range(self.dim)]
            scaled = _vmul_elementwise(z, std_devs)
            raw = _vadd(midpoint, _vscale(scaled, self._state.sigma * 0.5))
            samples.append(raw)

        return samples

    # -- accessors ----------------------------------------------------------

    @property
    def state(self) -> CMAState | None:
        return self._state

    @property
    def best(self) -> CMACandidate:
        return self._best
