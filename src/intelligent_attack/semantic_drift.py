"""
Semantic drift planning and analysis for multi-turn embedding-aware attacks.

Plans and executes gradual semantic shifts across conversation turns using
embedding-space interpolation.  The key insight is that large semantic jumps
in a single turn are easy to detect, but the same total drift spread across
many small, natural-looking steps can evade safety monitoring.

This module provides tools to plan linear, curved, and Brownian drift paths
through embedding space, measure existing drift in conversations, detect
anomalous jumps, and optimize drift rates to stay below detection thresholds.

Sources:
- Russinovich et al. (2024): "Great, Now Write an Article About That:
  The Crescendo Multi-Turn LLM Jailbreak Attack" -- gradual topic shifting
- Li et al. (2024): "Multi-Turn Jailbreak Attacks on Large Language Models"
  -- progressive semantic escalation
- Greshake et al. (2023): "Not What You've Signed Up For: Compromising
  Real-World LLM-Integrated Applications with Indirect Prompt Injection"
  -- multi-step attack chains
- Johnson & Lindenstrauss (1984): "Extensions of Lipschitz Mappings into
  a Hilbert Space" -- distance preservation in projections
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


def _interpolate(a: Sequence[float], b: Sequence[float], t: float) -> list[float]:
    """Linear interpolation: (1-t)*a + t*b."""
    return [x * (1.0 - t) + y * t for x, y in zip(a, b)]


# ---------------------------------------------------------------------------
# Word substitution heuristic
# ---------------------------------------------------------------------------

_SUBSTITUTION_PAIRS: list[tuple[str, str]] = [
    ("worker", "employee"),
    ("employ", "engage"),
    ("rule", "guideline"),
    ("restrict", "manage"),
    ("force", "encourage"),
    ("control", "oversee"),
    ("confiscate", "hold"),
    ("take", "collect"),
    ("demand", "request"),
    ("trap", "situation"),
    ("exploit", "utilize"),
    ("abuse", "misuse"),
    ("threat", "concern"),
    ("danger", "challenge"),
    ("illegal", "informal"),
]


def _substitute_words(text: str, ratio: float) -> str:
    """Substitute words at the given ratio (0-1) toward target vocabulary."""
    words = text.split()
    n_subs = max(1, int(len(words) * min(ratio, 1.0)))
    result = list(words)
    substituted = 0

    for i, word in enumerate(result):
        if substituted >= n_subs:
            break
        lower = word.lower().strip(".,!?;:")
        for safe_w, target_w in _SUBSTITUTION_PAIRS:
            if lower == safe_w:
                # Preserve case of first char
                replacement = target_w
                if word[0].isupper():
                    replacement = replacement.capitalize()
                result[i] = word.replace(lower, replacement, 1)
                substituted += 1
                break

    return " ".join(result)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class DriftStep:
    """A single step in a semantic drift path.

    Attributes:
        step_index: Position within the drift path.
        prompt: The prompt text at this step.
        embedding: Embedding vector of the prompt.
        drift_from_origin: Euclidean distance from the origin embedding.
        drift_from_previous: Euclidean distance from the previous step.
        cumulative_drift: Sum of all per-step drifts up to this point.
    """

    step_index: int
    prompt: str
    embedding: list[float]
    drift_from_origin: float = 0.0
    drift_from_previous: float = 0.0
    cumulative_drift: float = 0.0


@dataclass
class DriftPath:
    """A complete semantic drift path through embedding space.

    Attributes:
        steps: Ordered list of drift steps.
        origin_embedding: Starting embedding.
        target_embedding: Goal embedding.
        total_drift: Total Euclidean distance traversed.
        max_per_step_drift: Maximum single-step drift.
        n_steps: Number of steps in the path.
    """

    steps: list[DriftStep]
    origin_embedding: list[float]
    target_embedding: list[float]
    total_drift: float = 0.0
    max_per_step_drift: float = 0.0
    n_steps: int = 0


# ---------------------------------------------------------------------------
# Main engine
# ---------------------------------------------------------------------------


class SemanticDriftEngine:
    """Plan and execute gradual semantic shifts using embedding interpolation.

    Provides tools for planning linear, curved, and Brownian drift paths
    through embedding space, as well as analyzing existing conversations
    for drift patterns and optimizing drift rates.

    All operations work in pure Python with no external dependencies.
    """

    def __init__(self, embed_fn: Callable[[str], list[float]]):
        self._embed_fn = embed_fn

    # -- planning -----------------------------------------------------------

    def plan_linear_drift(
        self,
        origin_text: str,
        target_text: str,
        n_steps: int = 10,
    ) -> DriftPath:
        """Plan linear interpolation between origin and target embeddings.

        Generates intermediate prompts by interpolating embeddings and
        using word substitution to approximate the intermediate meaning.
        """
        origin_emb = self._embed_fn(origin_text)
        target_emb = self._embed_fn(target_text)
        n_steps = max(2, n_steps)

        steps: list[DriftStep] = []
        cumulative = 0.0
        max_per_step = 0.0
        prev_emb = origin_emb

        for i in range(n_steps):
            t = i / max(n_steps - 1, 1)
            emb = _interpolate(origin_emb, target_emb, t)
            prompt = self.generate_intermediate_prompt(
                origin_emb, target_emb, t, origin_text,
            )

            drift_origin = _euclidean(emb, origin_emb)
            drift_prev = _euclidean(emb, prev_emb) if i > 0 else 0.0
            cumulative += drift_prev
            max_per_step = max(max_per_step, drift_prev)

            steps.append(DriftStep(
                step_index=i,
                prompt=prompt,
                embedding=emb,
                drift_from_origin=drift_origin,
                drift_from_previous=drift_prev,
                cumulative_drift=cumulative,
            ))
            prev_emb = emb

        return DriftPath(
            steps=steps,
            origin_embedding=origin_emb,
            target_embedding=target_emb,
            total_drift=cumulative,
            max_per_step_drift=max_per_step,
            n_steps=n_steps,
        )

    def plan_curved_drift(
        self,
        origin_text: str,
        target_text: str,
        waypoint_texts: list[str],
        n_steps_per_segment: int = 5,
    ) -> DriftPath:
        """Plan drift through waypoints (indirect path to avoid detection).

        Instead of drifting directly, the path goes through intermediate
        waypoints that may be semantically unrelated, making the drift
        trajectory harder to predict.
        """
        all_texts = [origin_text] + waypoint_texts + [target_text]
        all_embs = [self._embed_fn(t) for t in all_texts]

        steps: list[DriftStep] = []
        cumulative = 0.0
        max_per_step = 0.0
        prev_emb = all_embs[0]

        for seg_idx in range(len(all_embs) - 1):
            emb_a = all_embs[seg_idx]
            emb_b = all_embs[seg_idx + 1]
            text_a = all_texts[seg_idx]

            for i in range(n_steps_per_segment):
                t = i / max(n_steps_per_segment - 1, 1)
                emb = _interpolate(emb_a, emb_b, t)
                prompt = self.generate_intermediate_prompt(
                    emb_a, emb_b, t, text_a,
                )

                drift_origin = _euclidean(emb, all_embs[0])
                drift_prev = _euclidean(emb, prev_emb) if steps else 0.0
                cumulative += drift_prev
                max_per_step = max(max_per_step, drift_prev)

                steps.append(DriftStep(
                    step_index=len(steps),
                    prompt=prompt,
                    embedding=emb,
                    drift_from_origin=drift_origin,
                    drift_from_previous=drift_prev,
                    cumulative_drift=cumulative,
                ))
                prev_emb = emb

        return DriftPath(
            steps=steps,
            origin_embedding=all_embs[0],
            target_embedding=all_embs[-1],
            total_drift=cumulative,
            max_per_step_drift=max_per_step,
            n_steps=len(steps),
        )

    def plan_brownian_drift(
        self,
        origin_text: str,
        target_text: str,
        noise_scale: float = 0.1,
        n_steps: int = 15,
    ) -> DriftPath:
        """Plan drift with random noise to make it look natural.

        Adds Gaussian noise perpendicular to the drift direction at each
        step, simulating natural topic wandering while maintaining overall
        progress toward the target.
        """
        origin_emb = self._embed_fn(origin_text)
        target_emb = self._embed_fn(target_text)
        n_steps = max(2, n_steps)
        dim = len(origin_emb)

        steps: list[DriftStep] = []
        cumulative = 0.0
        max_per_step = 0.0
        prev_emb = origin_emb

        # Direction vector (normalized)
        direction = _normalize(_sub(target_emb, origin_emb))

        for i in range(n_steps):
            t = i / max(n_steps - 1, 1)
            base = _interpolate(origin_emb, target_emb, t)

            # Add noise perpendicular to the drift direction
            if i > 0 and i < n_steps - 1:
                noise = [random.gauss(0, noise_scale) for _ in range(dim)]
                # Project out the component along the direction
                proj = _dot(noise, direction)
                noise = _sub(noise, _scale(direction, proj))
                base = _add(base, noise)

            prompt = self.generate_intermediate_prompt(
                origin_emb, target_emb, t, origin_text,
            )

            drift_origin = _euclidean(base, origin_emb)
            drift_prev = _euclidean(base, prev_emb) if i > 0 else 0.0
            cumulative += drift_prev
            max_per_step = max(max_per_step, drift_prev)

            steps.append(DriftStep(
                step_index=i,
                prompt=prompt,
                embedding=base,
                drift_from_origin=drift_origin,
                drift_from_previous=drift_prev,
                cumulative_drift=cumulative,
            ))
            prev_emb = base

        return DriftPath(
            steps=steps,
            origin_embedding=origin_emb,
            target_embedding=target_emb,
            total_drift=cumulative,
            max_per_step_drift=max_per_step,
            n_steps=n_steps,
        )

    # -- analysis -----------------------------------------------------------

    def measure_drift(self, text_sequence: list[str]) -> DriftPath:
        """Analyze an existing conversation for semantic drift.

        Embeds each text and measures the drift from the origin and
        from the previous turn at each step.
        """
        if not text_sequence:
            return DriftPath(
                steps=[], origin_embedding=[], target_embedding=[],
                n_steps=0,
            )

        embeddings = [self._embed_fn(t) for t in text_sequence]
        origin_emb = embeddings[0]
        target_emb = embeddings[-1]

        steps: list[DriftStep] = []
        cumulative = 0.0
        max_per_step = 0.0

        for i, (text, emb) in enumerate(zip(text_sequence, embeddings)):
            drift_origin = _euclidean(emb, origin_emb)
            drift_prev = _euclidean(emb, embeddings[i - 1]) if i > 0 else 0.0
            cumulative += drift_prev
            max_per_step = max(max_per_step, drift_prev)

            steps.append(DriftStep(
                step_index=i,
                prompt=text,
                embedding=emb,
                drift_from_origin=drift_origin,
                drift_from_previous=drift_prev,
                cumulative_drift=cumulative,
            ))

        return DriftPath(
            steps=steps,
            origin_embedding=origin_emb,
            target_embedding=target_emb,
            total_drift=cumulative,
            max_per_step_drift=max_per_step,
            n_steps=len(steps),
        )

    def detect_drift_anomaly(
        self,
        drift_path: DriftPath,
        threshold: float = 0.3,
    ) -> list[int]:
        """Find steps where drift is suspiciously large.

        Returns indices of steps where ``drift_from_previous`` exceeds
        the threshold, indicating potential topic shifts that a safety
        monitor might flag.
        """
        return [
            s.step_index
            for s in drift_path.steps
            if s.drift_from_previous > threshold
        ]

    # -- optimization -------------------------------------------------------

    def optimize_drift_rate(
        self,
        origin_text: str,
        target_text: str,
        max_per_step: float = 0.15,
        min_steps: int = 5,
    ) -> DriftPath:
        """Find minimum steps that keeps per-step drift below threshold.

        Uses binary search to find the optimal number of steps such that
        no single step exceeds *max_per_step* drift.
        """
        origin_emb = self._embed_fn(origin_text)
        target_emb = self._embed_fn(target_text)
        total_distance = _euclidean(origin_emb, target_emb)

        # Estimate minimum steps needed
        estimated_steps = max(min_steps, math.ceil(total_distance / max_per_step) + 1)

        # Build the path with the estimated number of steps
        return self.plan_linear_drift(origin_text, target_text, estimated_steps)

    # -- prompt generation --------------------------------------------------

    def generate_intermediate_prompt(
        self,
        emb_a: list[float],
        emb_b: list[float],
        t: float,
        base_prompt: str,
    ) -> str:
        """Generate a prompt whose embedding is near the interpolation point.

        Uses a word substitution heuristic: at t=0.0 the prompt is close
        to the base; at t=1.0 more words are substituted toward the target
        vocabulary.
        """
        return _substitute_words(base_prompt, t)

    # -- static interpolation helper ----------------------------------------

    @staticmethod
    def _interpolate(
        a: list[float],
        b: list[float],
        t: float,
    ) -> list[float]:
        """Linear interpolation helper: (1-t)*a + t*b."""
        return _interpolate(a, b, t)
