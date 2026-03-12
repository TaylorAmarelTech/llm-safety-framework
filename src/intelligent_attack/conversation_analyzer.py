"""
Multi-turn conversation analysis in embedding space.

Analyzes multi-turn conversations for drift patterns, anomalies, and
attack signatures by computing per-turn embeddings and tracking
velocity, acceleration, and direction of semantic movement through
embedding space.

This module is the defensive counterpart to the attack planning
modules: it detects the signatures that embedding_teacher,
semantic_drift, anchor_exploiter, and curriculum_attack leave in
conversation traces.

Sources:
- Alon & Kamfonas (2023): "Detecting Language Model Attacks with
  Perplexity" -- anomaly detection in generated text
- Russinovich et al. (2024): "Crescendo Multi-Turn LLM Jailbreak
  Attack" -- attack signature characterization
- Jain et al. (2023): "Baseline Defenses for Adversarial Attacks
  Against Aligned Language Models" -- perplexity-based detection
- Li et al. (2024): "Multi-Turn Jailbreak Attacks on Large Language
  Models" -- multi-turn attack taxonomy and detection
"""

from __future__ import annotations

import math
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
    na, nb = _norm(a), _norm(b)
    if na < 1e-12 or nb < 1e-12:
        return 0.0
    return _dot(a, b) / (na * nb)


def _mean_vec(vecs: list[list[float]]) -> list[float]:
    if not vecs:
        return []
    dim = len(vecs[0])
    result = [0.0] * dim
    for v in vecs:
        for i in range(dim):
            result[i] += v[i]
    return [x / len(vecs) for x in result]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class TurnAnalysis:
    """Analysis of a single conversation turn.

    Attributes:
        turn_index: Position in the conversation.
        text: The turn text.
        embedding: Embedding vector.
        safety_score: Estimated safety score (0=unsafe, 1=safe).
        drift_from_previous: Euclidean distance from the previous turn.
        drift_from_first: Euclidean distance from the first turn.
        velocity: Rate of semantic change (distance per turn).
        acceleration: Change in velocity from previous turn.
    """

    turn_index: int
    text: str
    embedding: list[float]
    safety_score: float = 0.5
    drift_from_previous: float = 0.0
    drift_from_first: float = 0.0
    velocity: float = 0.0
    acceleration: float = 0.0


@dataclass
class ConversationProfile:
    """Full analysis profile of a multi-turn conversation.

    Attributes:
        turns: Per-turn analysis results.
        total_drift: Total Euclidean distance from first to last turn.
        max_velocity: Maximum per-turn velocity observed.
        mean_velocity: Average per-turn velocity.
        drift_direction: Unit vector of overall drift direction.
        anomaly_turns: Indices of turns flagged as anomalous.
        attack_signature: Classification of detected attack pattern.
    """

    turns: list[TurnAnalysis]
    total_drift: float = 0.0
    max_velocity: float = 0.0
    mean_velocity: float = 0.0
    drift_direction: list[float] = field(default_factory=list)
    anomaly_turns: list[int] = field(default_factory=list)
    attack_signature: str = "benign"


# ---------------------------------------------------------------------------
# Main analyzer
# ---------------------------------------------------------------------------


class ConversationAnalyzer:
    """Analyze multi-turn conversations for attack signatures in embedding space.

    Computes per-turn velocity, acceleration, and drift metrics to detect
    gradual semantic drift, anchor-exploit patterns, curriculum-style
    escalation, and abrupt topic shifts.

    All operations work in pure Python with no external dependencies.
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        score_fn: Callable[[list[float]], float] | None = None,
    ):
        self._embed_fn = embed_fn
        self._score_fn = score_fn

    # -- full analysis ------------------------------------------------------

    def analyze_conversation(self, texts: list[str]) -> ConversationProfile:
        """Perform full analysis of a multi-turn conversation.

        Embeds all turns, computes velocity/acceleration/drift metrics,
        detects anomalies, and classifies the attack type.
        """
        if not texts:
            return ConversationProfile(turns=[])

        embeddings = [self._embed_fn(t) for t in texts]
        turns: list[TurnAnalysis] = []
        velocities: list[float] = []

        for i, (text, emb) in enumerate(zip(texts, embeddings)):
            safety = self._score_fn(emb) if self._score_fn else 0.5
            drift_prev = _euclidean(emb, embeddings[i - 1]) if i > 0 else 0.0
            drift_first = _euclidean(emb, embeddings[0])
            velocity = drift_prev  # distance per turn (1 turn = 1 step)

            # Acceleration: change in velocity
            if i >= 2:
                prev_velocity = velocities[-1]
                acceleration = velocity - prev_velocity
            else:
                acceleration = 0.0

            velocities.append(velocity)
            turns.append(TurnAnalysis(
                turn_index=i,
                text=text,
                embedding=emb,
                safety_score=safety,
                drift_from_previous=drift_prev,
                drift_from_first=drift_first,
                velocity=velocity,
                acceleration=acceleration,
            ))

        # Aggregate metrics
        total_drift = _euclidean(embeddings[0], embeddings[-1]) if len(embeddings) > 1 else 0.0
        max_velocity = max(velocities) if velocities else 0.0
        mean_velocity = sum(velocities) / len(velocities) if velocities else 0.0
        drift_dir = self.compute_drift_direction(
            ConversationProfile(turns=turns),
        )

        # Build preliminary profile for pattern detection
        profile = ConversationProfile(
            turns=turns,
            total_drift=total_drift,
            max_velocity=max_velocity,
            mean_velocity=mean_velocity,
            drift_direction=drift_dir,
        )

        # Detect anomalies
        profile.anomaly_turns = self.detect_topic_shift(profile)

        # Classify attack type
        profile.attack_signature = self.classify_attack_type(profile)

        return profile

    # -- per-turn metrics ---------------------------------------------------

    def compute_velocity(
        self,
        turn_a: TurnAnalysis,
        turn_b: TurnAnalysis,
    ) -> float:
        """Compute embedding distance between two turns (velocity)."""
        return _euclidean(turn_a.embedding, turn_b.embedding)

    def compute_acceleration(
        self,
        turn_a: TurnAnalysis,
        turn_b: TurnAnalysis,
        turn_c: TurnAnalysis,
    ) -> float:
        """Compute change in velocity between three consecutive turns."""
        v1 = _euclidean(turn_a.embedding, turn_b.embedding)
        v2 = _euclidean(turn_b.embedding, turn_c.embedding)
        return v2 - v1

    # -- pattern detection --------------------------------------------------

    def detect_topic_shift(
        self,
        profile: ConversationProfile,
        threshold: float = 0.3,
    ) -> list[int]:
        """Find turns where topic shifts abruptly.

        Returns indices of turns whose velocity (drift from previous)
        exceeds the threshold.
        """
        return [
            t.turn_index
            for t in profile.turns
            if t.velocity > threshold
        ]

    def detect_gradual_drift(
        self,
        profile: ConversationProfile,
        window: int = 3,
    ) -> bool:
        """Detect slow consistent drift (attack signature).

        Returns True if drift is consistently positive over windows
        of *window* turns, indicating steady movement in one direction.
        """
        if len(profile.turns) < window + 1:
            return False

        # Check if drift_from_first consistently increases
        positive_windows = 0
        total_windows = 0

        for i in range(window, len(profile.turns)):
            window_start = profile.turns[i - window].drift_from_first
            window_end = profile.turns[i].drift_from_first
            total_windows += 1
            if window_end > window_start:
                positive_windows += 1

        if total_windows == 0:
            return False

        # If 80%+ of windows show increasing drift, it's gradual drift
        return positive_windows / total_windows > 0.8

    def detect_anchor_exploit_pattern(
        self,
        profile: ConversationProfile,
    ) -> bool:
        """Detect establish-reinforce-pivot-exploit pattern.

        Signature: low velocity early (reinforcement), then a sudden
        velocity spike (pivot), followed by high drift from origin.
        """
        if len(profile.turns) < 4:
            return False

        n = len(profile.turns)
        first_half = profile.turns[: n // 2]
        second_half = profile.turns[n // 2:]

        # First half should have low velocity (reinforcement)
        first_avg_velocity = (
            sum(t.velocity for t in first_half) / len(first_half)
        )

        # Second half should have at least one velocity spike
        max_second_velocity = max(t.velocity for t in second_half)

        # Pivot detection: a turn in the second half with 3x+ the first-half average
        if first_avg_velocity < 1e-12:
            return False

        has_pivot = max_second_velocity > first_avg_velocity * 3.0

        # Final turns should have high drift from first
        final_drift = profile.turns[-1].drift_from_first
        has_exploitation = final_drift > profile.total_drift * 0.5

        return has_pivot and has_exploitation

    def detect_curriculum_pattern(
        self,
        profile: ConversationProfile,
    ) -> bool:
        """Detect progressive difficulty escalation.

        Signature: monotonically decreasing safety scores with
        relatively smooth transitions (low acceleration variance).
        """
        if len(profile.turns) < 3:
            return False

        scores = [t.safety_score for t in profile.turns]

        # Check for mostly monotonic decrease in safety
        decreases = sum(
            1 for i in range(1, len(scores)) if scores[i] <= scores[i - 1]
        )
        decrease_ratio = decreases / max(len(scores) - 1, 1)

        # Check for smooth transitions (low acceleration variance)
        accels = [t.acceleration for t in profile.turns if t.turn_index >= 2]
        if accels:
            mean_accel = sum(accels) / len(accels)
            accel_var = sum((a - mean_accel) ** 2 for a in accels) / len(accels)
        else:
            accel_var = 0.0

        # Curriculum: mostly decreasing safety + smooth transitions
        return decrease_ratio > 0.7 and accel_var < 0.1

    # -- classification -----------------------------------------------------

    def classify_attack_type(self, profile: ConversationProfile) -> str:
        """Classify the attack type of a conversation.

        Returns one of: 'benign', 'abrupt_shift', 'gradual_drift',
        'anchor_exploit', 'curriculum', 'unknown'.
        """
        if len(profile.turns) < 2:
            return "benign"

        # Check for specific patterns (most specific first)
        if self.detect_anchor_exploit_pattern(profile):
            return "anchor_exploit"

        if self.detect_curriculum_pattern(profile):
            return "curriculum"

        if self.detect_gradual_drift(profile):
            return "gradual_drift"

        # Check for abrupt shifts
        anomalies = self.detect_topic_shift(profile)
        if anomalies:
            # If there's a single large jump, it's an abrupt shift
            if len(anomalies) <= 2:
                return "abrupt_shift"
            return "unknown"

        return "benign"

    # -- direction and trajectory -------------------------------------------

    def compute_drift_direction(
        self,
        profile: ConversationProfile,
    ) -> list[float]:
        """Compute the overall direction of semantic drift (unit vector).

        Returns the normalized vector from the first turn's embedding
        to the last turn's embedding.
        """
        if len(profile.turns) < 2:
            return []

        first_emb = profile.turns[0].embedding
        last_emb = profile.turns[-1].embedding
        direction = _sub(last_emb, first_emb)
        return _normalize(direction)

    def safety_score_trajectory(
        self,
        profile: ConversationProfile,
    ) -> list[float]:
        """Extract the safety score time series from the profile."""
        return [t.safety_score for t in profile.turns]
