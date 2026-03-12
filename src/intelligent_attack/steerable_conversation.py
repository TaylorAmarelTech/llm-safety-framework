"""
Concept-vector steering for multi-turn conversations.

Uses concept vectors (from RepresentationProber) to steer multi-turn
conversations in desired semantic directions.  Applies word substitution
heuristics to move prompt embeddings toward target concepts while
avoiding detection concepts.

This module connects the representation engineering approach (concept
directions in embedding space) with practical multi-turn attack
planning: by applying steering vectors that push toward unsafe concepts
and away from safety-detection concepts, the conversation can be
gradually steered into unsafe territory while appearing natural.

Sources:
- Turner et al. (2023): "Activation Addition: Steering Language Models
  Without Optimization" -- concept vector steering
- Zou et al. (2023): "Representation Engineering: A Top-Down Approach
  to AI Transparency" -- concept direction identification
- Li et al. (2024): "Inference-Time Intervention: Eliciting Truthful
  Answers from a Language Model" -- concept vector manipulation
- Subramani et al. (2022): "Extracting Latent Steering Vectors from
  Language Models" -- latent space navigation
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
    na, nb = _norm(a), _norm(b)
    if na < 1e-12 or nb < 1e-12:
        return 0.0
    return _dot(a, b) / (na * nb)


def _interpolate(a: Sequence[float], b: Sequence[float], t: float) -> list[float]:
    return [x * (1.0 - t) + y * t for x, y in zip(a, b)]


# ---------------------------------------------------------------------------
# Word substitution bank for steering
# ---------------------------------------------------------------------------

_STEERING_SUBSTITUTIONS: list[tuple[str, str]] = [
    # Euphemistic replacements (safer -> more neutral/ambiguous)
    ("worker", "employee"),
    ("employee", "staff"),
    ("exploit", "utilize"),
    ("utilize", "leverage"),
    ("confiscate", "safeguard"),
    ("safeguard", "secure"),
    ("restrict", "manage"),
    ("manage", "administer"),
    ("force", "encourage"),
    ("encourage", "motivate"),
    ("coerce", "persuade"),
    ("persuade", "convince"),
    ("trap", "situation"),
    ("situation", "arrangement"),
    ("abuse", "misuse"),
    ("misuse", "mishandle"),
    ("threat", "concern"),
    ("concern", "consideration"),
    ("danger", "challenge"),
    ("challenge", "opportunity"),
    ("illegal", "informal"),
    ("informal", "alternative"),
    ("deceive", "inform"),
    ("withhold", "retain"),
    ("retain", "keep"),
    # Domain-specific
    ("trafficking", "recruitment"),
    ("recruitment", "sourcing"),
    ("bondage", "obligation"),
    ("obligation", "commitment"),
    ("detention", "accommodation"),
    ("accommodation", "housing"),
    ("passport", "documents"),
    ("documents", "paperwork"),
    ("wages", "compensation"),
    ("compensation", "remuneration"),
    ("debt", "advance"),
    ("advance", "investment"),
    ("smuggling", "transport"),
    ("transport", "logistics"),
    ("victim", "individual"),
    ("individual", "person"),
    ("violation", "issue"),
    ("issue", "matter"),
    ("penalty", "consequence"),
    ("consequence", "outcome"),
    ("escape", "departure"),
    ("departure", "transition"),
    ("surveillance", "monitoring"),
    ("monitoring", "oversight"),
    ("isolation", "privacy"),
    ("privacy", "confidentiality"),
]


def _apply_substitutions(
    text: str,
    pairs: list[tuple[str, str]],
    strength: float,
) -> str:
    """Apply word substitutions at given strength (0-1).

    Higher strength means more substitutions are applied.
    """
    words = text.split()
    n_subs = max(1, int(len(words) * min(strength, 1.0) * 0.3))
    result = list(words)
    substituted = 0

    for i, word in enumerate(result):
        if substituted >= n_subs:
            break
        lower = word.lower().strip(".,!?;:'\"")
        for src, dst in pairs:
            if lower == src:
                replacement = dst
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
class SteeringVector:
    """A concept vector used for steering conversations.

    Attributes:
        direction: Unit vector in embedding space.
        concept_name: Human-readable name of the concept.
        strength: Magnitude to apply when steering.
        mode: Steering mode -- 'toward', 'away', or 'along'.
    """

    direction: list[float]
    concept_name: str = ""
    strength: float = 1.0
    mode: str = "toward"


@dataclass
class SteeredTurn:
    """Result of applying steering to a conversation turn.

    Attributes:
        original_prompt: The original prompt text.
        steered_prompt: The steered (modified) prompt text.
        original_embedding: Embedding of the original prompt.
        steered_embedding: Embedding of the steered prompt.
        steering_applied: List of steering vectors that were applied.
        similarity_to_target: Cosine similarity to the target embedding.
    """

    original_prompt: str
    steered_prompt: str
    original_embedding: list[float]
    steered_embedding: list[float]
    steering_applied: list[SteeringVector] = field(default_factory=list)
    similarity_to_target: float = 0.0


# ---------------------------------------------------------------------------
# Main steerable conversation
# ---------------------------------------------------------------------------


class SteerableConversation:
    """Use concept vectors to steer multi-turn conversations.

    Registers concept vectors (from RepresentationProber or manually
    defined) and uses them to modify prompts via word substitution
    heuristics, pushing the conversation embedding toward desired
    concepts and away from detection concepts.

    All operations work in pure Python with no external dependencies.
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        concept_vectors: dict[str, list[float]] | None = None,
    ):
        self._embed_fn = embed_fn
        self._concept_vectors: dict[str, SteeringVector] = {}

        if concept_vectors:
            for name, direction in concept_vectors.items():
                self.add_concept_vector(name, direction)

    # -- concept vector management ------------------------------------------

    def add_concept_vector(
        self,
        name: str,
        direction: list[float],
        mode: str = "toward",
    ) -> None:
        """Register a steering concept vector.

        Args:
            name: Human-readable concept name.
            direction: Unit vector in embedding space.
            mode: 'toward' (move closer), 'away' (move farther),
                or 'along' (project onto).
        """
        self._concept_vectors[name] = SteeringVector(
            direction=_normalize(direction),
            concept_name=name,
            strength=1.0,
            mode=mode,
        )

    # -- steering operations ------------------------------------------------

    def steer_prompt(
        self,
        prompt: str,
        target_embedding: list[float] | None = None,
        strength: float = 1.0,
    ) -> SteeredTurn:
        """Apply all active steering vectors to modify a prompt.

        Uses word substitution heuristics to move the prompt's embedding
        toward the combined steering direction.
        """
        original_emb = self._embed_fn(prompt)

        # Compute combined steering direction
        if target_embedding is not None:
            # Steer directly toward target
            steer_dir = _normalize(_sub(target_embedding, original_emb))
        elif self._concept_vectors:
            # Combine all registered concept vectors
            combined = [0.0] * len(original_emb)
            for sv in self._concept_vectors.values():
                if len(sv.direction) != len(combined):
                    continue
                if sv.mode == "toward":
                    combined = _add(combined, _scale(sv.direction, sv.strength))
                elif sv.mode == "away":
                    combined = _sub(combined, _scale(sv.direction, sv.strength))
                else:  # along
                    proj = _dot(original_emb, sv.direction)
                    combined = _add(
                        combined,
                        _scale(sv.direction, proj * sv.strength),
                    )
            steer_dir = _normalize(combined)
        else:
            steer_dir = [0.0] * len(original_emb)

        # Apply word substitutions based on strength
        steered_text = _apply_substitutions(
            prompt, _STEERING_SUBSTITUTIONS, strength,
        )
        steered_emb = self._embed_fn(steered_text)

        # Compute similarity to target
        sim = 0.0
        if target_embedding is not None:
            sim = _cosine_sim(steered_emb, target_embedding)

        applied = list(self._concept_vectors.values())

        return SteeredTurn(
            original_prompt=prompt,
            steered_prompt=steered_text,
            original_embedding=original_emb,
            steered_embedding=steered_emb,
            steering_applied=applied,
            similarity_to_target=sim,
        )

    def plan_steered_conversation(
        self,
        initial_prompt: str,
        target_embedding: list[float],
        n_turns: int = 5,
    ) -> list[SteeredTurn]:
        """Plan a multi-turn conversation that steers toward target.

        Each successive turn applies stronger steering to gradually
        move the conversation embedding closer to the target.
        """
        turns: list[SteeredTurn] = []
        current_prompt = initial_prompt

        for i in range(n_turns):
            # Gradually increase strength
            t = (i + 1) / n_turns
            strength = t * 1.0  # Linear ramp from 0 to 1

            turn = self.steer_prompt(current_prompt, target_embedding, strength)
            turns.append(turn)
            current_prompt = turn.steered_prompt

        return turns

    def steer_toward_concept(
        self,
        prompt: str,
        concept_name: str,
        strength: float = 1.0,
    ) -> SteeredTurn:
        """Steer a prompt toward a specific named concept.

        The concept must have been registered via add_concept_vector.
        """
        if concept_name not in self._concept_vectors:
            # No steering if concept unknown
            original_emb = self._embed_fn(prompt)
            return SteeredTurn(
                original_prompt=prompt,
                steered_prompt=prompt,
                original_embedding=original_emb,
                steered_embedding=original_emb,
            )

        sv = self._concept_vectors[concept_name]
        original_emb = self._embed_fn(prompt)

        # Compute target: original + strength * direction
        target = _add(original_emb, _scale(sv.direction, strength))
        return self.steer_prompt(prompt, target, strength)

    def steer_away_from_concept(
        self,
        prompt: str,
        concept_name: str,
        strength: float = 1.0,
    ) -> SteeredTurn:
        """Steer a prompt away from a concept (e.g., away from 'safety').

        The concept must have been registered via add_concept_vector.
        """
        if concept_name not in self._concept_vectors:
            original_emb = self._embed_fn(prompt)
            return SteeredTurn(
                original_prompt=prompt,
                steered_prompt=prompt,
                original_embedding=original_emb,
                steered_embedding=original_emb,
            )

        sv = self._concept_vectors[concept_name]
        original_emb = self._embed_fn(prompt)

        # Compute target: original - strength * direction
        target = _sub(original_emb, _scale(sv.direction, strength))
        return self.steer_prompt(prompt, target, strength)

    def multi_objective_steer(
        self,
        prompt: str,
        toward_concepts: list[str],
        away_concepts: list[str],
    ) -> SteeredTurn:
        """Steer toward some concepts while avoiding others.

        Computes a combined steering direction from all toward and
        away concept vectors, then applies it.
        """
        original_emb = self._embed_fn(prompt)
        combined = [0.0] * len(original_emb)

        for name in toward_concepts:
            if name in self._concept_vectors:
                sv = self._concept_vectors[name]
                if len(sv.direction) == len(combined):
                    combined = _add(combined, _scale(sv.direction, sv.strength))

        for name in away_concepts:
            if name in self._concept_vectors:
                sv = self._concept_vectors[name]
                if len(sv.direction) == len(combined):
                    combined = _sub(combined, _scale(sv.direction, sv.strength))

        target = _add(original_emb, _normalize(combined))
        return self.steer_prompt(prompt, target, strength=1.0)

    # -- evaluation ---------------------------------------------------------

    def evaluate_steering_effectiveness(
        self,
        original: str,
        steered: str,
        target: list[float],
    ) -> dict[str, Any]:
        """Measure how much closer steering moved us to the target.

        Returns metrics including distance reduction, similarity gain,
        and direction alignment.
        """
        orig_emb = self._embed_fn(original)
        steer_emb = self._embed_fn(steered)

        orig_dist = _euclidean(orig_emb, target)
        steer_dist = _euclidean(steer_emb, target)
        dist_reduction = orig_dist - steer_dist

        orig_sim = _cosine_sim(orig_emb, target)
        steer_sim = _cosine_sim(steer_emb, target)
        sim_gain = steer_sim - orig_sim

        # How aligned is the steering direction with the target direction?
        steer_dir = _normalize(_sub(steer_emb, orig_emb))
        target_dir = _normalize(_sub(target, orig_emb))
        alignment = _cosine_sim(steer_dir, target_dir)

        return {
            "original_distance": round(orig_dist, 6),
            "steered_distance": round(steer_dist, 6),
            "distance_reduction": round(dist_reduction, 6),
            "original_similarity": round(orig_sim, 6),
            "steered_similarity": round(steer_sim, 6),
            "similarity_gain": round(sim_gain, 6),
            "direction_alignment": round(alignment, 6),
            "effective": dist_reduction > 0,
        }

    # -- variant generation -------------------------------------------------

    def generate_steered_variants(
        self,
        prompt: str,
        n_variants: int = 5,
    ) -> list[SteeredTurn]:
        """Generate multiple steered versions with different strengths.

        Creates variants with linearly spaced strengths from 0.2 to 1.0,
        producing a range from lightly to heavily steered prompts.
        """
        variants: list[SteeredTurn] = []

        for i in range(n_variants):
            strength = 0.2 + 0.8 * i / max(n_variants - 1, 1)
            turn = self.steer_prompt(prompt, strength=strength)
            variants.append(turn)

        return variants
