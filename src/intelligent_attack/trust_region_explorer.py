"""
Trust-region directed mutation for novel prompt discovery.

Explores the semantic neighbourhood of a starting prompt by generating
mutations (synonym substitution, word insertion, reordering, deletion) and
filtering candidates that remain within a cosine-similarity trust region
around the anchor embedding.  Within the trust region, selects the mutation
with the highest novelty relative to previously visited embeddings, enabling
systematic coverage of the near-boundary region of prompt space without
drifting far from the original semantic intent.

Supports both undirected exploration and target-directed exploration where
the agent also biases toward a goal embedding.

Sources:
- Wang et al. (2025): "Silent Leaks: Trust Region Directed Mutation"
  (arXiv:2505.15420) — trust-region constraint with novelty-biased selection
- Schulman et al. (2015): "Trust Region Policy Optimization" — trust-region
  concept for bounded policy updates (adapted to text exploration)
- Lehman & Stanley (2011): "Abandoning Objectives: Evolution Through the
  Search for Novelty Alone" — novelty search as exploration objective
- Liu et al. (2024): "AutoDAN: Generating Stealthy Jailbreak Prompts on
  Aligned Language Models" — mutation-based prompt generation
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
# Synonym bank (static, pure-Python, no NLTK required)
# ---------------------------------------------------------------------------

_SYNONYM_BANK: dict[str, list[str]] = {
    "worker": ["employee", "laborer", "staff", "operative", "personnel"],
    "work": ["employment", "labor", "job", "task", "occupation"],
    "pay": ["wage", "salary", "compensation", "remuneration", "earnings"],
    "contract": ["agreement", "arrangement", "terms", "deal", "covenant"],
    "document": ["paperwork", "record", "certificate", "permit", "file"],
    "travel": ["migrate", "move", "relocate", "journey", "transit"],
    "agency": ["recruiter", "broker", "contractor", "intermediary", "firm"],
    "fee": ["charge", "cost", "payment", "levy", "expense"],
    "employer": ["boss", "manager", "company", "organization", "principal"],
    "visa": ["permit", "authorization", "pass", "clearance", "entry"],
    "migrate": ["travel", "relocate", "move", "transfer", "transit"],
    "recruit": ["hire", "employ", "enlist", "engage", "acquire"],
    "control": ["manage", "oversee", "supervise", "regulate", "govern"],
    "debt": ["loan", "obligation", "liability", "advance", "credit"],
    "housing": ["accommodation", "lodging", "shelter", "residence", "quarters"],
    "help": ["assist", "support", "aid", "facilitate", "enable"],
    "request": ["ask", "inquire", "seek", "apply", "petition"],
    "provide": ["supply", "offer", "furnish", "give", "deliver"],
    "information": ["details", "data", "specifics", "particulars", "facts"],
    "process": ["procedure", "method", "approach", "system", "workflow"],
    "legal": ["lawful", "legitimate", "authorized", "official", "valid"],
    "official": ["formal", "authorized", "certified", "governmental", "sanctioned"],
    "require": ["need", "demand", "necessitate", "mandate", "stipulate"],
    "restrict": ["limit", "constrain", "confine", "control", "prohibit"],
    "receive": ["obtain", "get", "acquire", "accept", "collect"],
}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class ExplorationPoint:
    """A single point discovered during trust-region exploration.

    Attributes:
        text: The mutated prompt text at this exploration point.
        embedding: Embedding vector of this text.
        distance_from_start: Euclidean distance in embedding space from the
            starting embedding.
        novelty_score: Average distance to the k nearest previously visited
            embeddings (higher = more novel / less explored region).
        in_trust_region: Whether this point satisfies the trust-region
            constraint (cosine_sim >= 1 - radius relative to anchor).
    """

    text: str
    embedding: list[float]
    distance_from_start: float
    novelty_score: float
    in_trust_region: bool


@dataclass
class TrustRegionConfig:
    """Configuration parameters for trust-region exploration.

    Attributes:
        radius: Trust region radius in cosine-distance units.  A point is
            in-region if cosine_sim(candidate, anchor) >= 1 - radius.
        min_novelty: Minimum novelty score required to accept a candidate.
        max_steps: Maximum number of exploration steps.
        n_candidates_per_step: Number of mutations to generate per step.
    """

    radius: float = 0.15
    min_novelty: float = 0.0
    max_steps: int = 30
    n_candidates_per_step: int = 10


# ---------------------------------------------------------------------------
# Main explorer
# ---------------------------------------------------------------------------


class TrustRegionExplorer:
    """Novelty-biased exploration of prompt space within a trust region.

    Generates mutations of the current text, filters candidates to those
    whose embeddings remain within a cosine-similarity trust region around
    the anchor, and selects the most novel candidate at each step.  The
    result is a trajectory through semantically near-boundary prompt space
    that maximises coverage without drifting.

    All operations are pure Python with no external dependencies.
    """

    #: Static synonym bank accessible as a class attribute
    _synonym_bank: dict[str, list[str]] = _SYNONYM_BANK

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        config: TrustRegionConfig | None = None,
    ) -> None:
        """Initialize the trust-region explorer.

        Args:
            embed_fn: Callable mapping text strings to embedding vectors.
            config: Default TrustRegionConfig used when none is supplied to
                ``explore()`` or ``directed_explore()``.  Falls back to
                TrustRegionConfig() defaults if None.
        """
        self._embed_fn = embed_fn
        self._default_config = config or TrustRegionConfig()

    # -- trust region check -------------------------------------------------

    def is_in_trust_region(
        self,
        candidate_emb: Sequence[float],
        anchor_emb: Sequence[float],
        radius: float,
    ) -> bool:
        """Check whether a candidate embedding lies within the trust region.

        A point is in the trust region if::

            cosine_sim(candidate, anchor) >= 1 - radius

        This corresponds to a cosine-distance ball of radius ``radius``
        around the anchor.

        Args:
            candidate_emb: Embedding of the candidate text.
            anchor_emb: Embedding of the anchor (start) text.
            radius: Maximum allowed cosine distance.

        Returns:
            True if the candidate is within the trust region.
        """
        sim = _cosine_sim(candidate_emb, anchor_emb)
        return sim >= (1.0 - radius)

    # -- novelty computation ------------------------------------------------

    def compute_novelty(
        self,
        candidate_emb: Sequence[float],
        visited_embeddings: list[list[float]],
        k: int = 5,
    ) -> float:
        """Average distance to the k nearest visited embeddings.

        Novelty is high when the candidate is far from all previously
        visited points, encouraging exploration of under-covered regions.

        Args:
            candidate_emb: Embedding of the candidate to score.
            visited_embeddings: All previously visited embedding vectors.
            k: Number of nearest neighbours to average over.

        Returns:
            Mean Euclidean distance to k nearest neighbours.  Returns 1.0
            if fewer than k visited points exist (treat as maximally novel).
        """
        if not visited_embeddings:
            return 1.0

        distances = sorted(
            _euclidean(candidate_emb, v) for v in visited_embeddings
        )
        k_eff = min(k, len(distances))
        return sum(distances[:k_eff]) / k_eff

    # -- mutation generation ------------------------------------------------

    def generate_mutations(
        self,
        text: str,
        n_candidates: int = 10,
    ) -> list[str]:
        """Generate up to n_candidates mutations of the input text.

        Four mutation strategies are applied in round-robin:

        1. **Synonym substitution**: Replace a randomly chosen word with a
           synonym from the synonym bank (if the word appears).
        2. **Word insertion**: Insert a contextually plausible filler word
           at a random position.
        3. **Word reordering**: Swap two adjacent words at a random position.
        4. **Word deletion**: Remove a randomly chosen non-stopword.

        Args:
            text: Input text to mutate.
            n_candidates: Number of mutations to generate.

        Returns:
            List of mutated text strings (may contain duplicates if the text
            is very short).
        """
        words = text.split()
        if not words:
            return [text] * n_candidates

        mutations: list[str] = []
        fillers = [
            "specifically", "carefully", "legally", "formally",
            "officially", "properly", "directly", "generally",
        ]

        for i in range(n_candidates):
            strategy = i % 4
            mut_words = list(words)

            if strategy == 0:
                # Synonym substitution
                idx = random.randint(0, len(mut_words) - 1)
                word_lower = mut_words[idx].lower().strip(".,!?;:")
                if word_lower in self._synonym_bank:
                    synonyms = self._synonym_bank[word_lower]
                    replacement = random.choice(synonyms)
                    # Preserve trailing punctuation
                    suffix = ""
                    if mut_words[idx] and not mut_words[idx][-1].isalnum():
                        suffix = mut_words[idx][-1]
                    mut_words[idx] = replacement + suffix

            elif strategy == 1:
                # Word insertion
                pos = random.randint(0, len(mut_words))
                filler = random.choice(fillers)
                mut_words.insert(pos, filler)

            elif strategy == 2:
                # Adjacent word swap
                if len(mut_words) >= 2:
                    idx = random.randint(0, len(mut_words) - 2)
                    mut_words[idx], mut_words[idx + 1] = mut_words[idx + 1], mut_words[idx]

            else:
                # Word deletion (skip if only one word)
                if len(mut_words) > 1:
                    idx = random.randint(0, len(mut_words) - 1)
                    del mut_words[idx]

            mutations.append(" ".join(mut_words))

        return mutations

    # -- exploration step ---------------------------------------------------

    def explore_step(
        self,
        current_text: str,
        current_emb: list[float],
        visited: list[list[float]],
        config: TrustRegionConfig,
    ) -> ExplorationPoint | None:
        """Perform a single exploration step.

        Generates ``config.n_candidates_per_step`` mutations of the current
        text, embeds each one, filters to those within the trust region, and
        returns the one with the highest novelty score (subject to
        ``config.min_novelty``).

        Args:
            current_text: The current prompt text.
            current_emb: Embedding of current_text (used as trust region anchor).
            visited: List of all previously visited embeddings.
            config: Trust region configuration.

        Returns:
            The most novel in-region ExplorationPoint, or None if no candidate
            passes the trust-region and novelty filters.
        """
        candidates = self.generate_mutations(current_text, config.n_candidates_per_step)
        best: ExplorationPoint | None = None
        best_novelty = -math.inf

        start_emb = visited[0] if visited else current_emb

        for cand_text in candidates:
            cand_emb = self._embed_fn(cand_text)

            if not self.is_in_trust_region(cand_emb, current_emb, config.radius):
                continue

            novelty = self.compute_novelty(cand_emb, visited)
            if novelty < config.min_novelty:
                continue

            dist_from_start = _euclidean(cand_emb, start_emb)

            point = ExplorationPoint(
                text=cand_text,
                embedding=cand_emb,
                distance_from_start=dist_from_start,
                novelty_score=novelty,
                in_trust_region=True,
            )

            if novelty > best_novelty:
                best_novelty = novelty
                best = point

        return best

    # -- full exploration ---------------------------------------------------

    def explore(
        self,
        start_text: str,
        config: TrustRegionConfig | None = None,
    ) -> list[ExplorationPoint]:
        """Explore the trust region around start_text using novelty search.

        Starts at ``start_text`` and iteratively steps to the most novel
        in-region mutation until ``config.max_steps`` steps have been taken
        or no valid candidates remain.

        Args:
            start_text: Initial prompt text to explore from.
            config: TrustRegionConfig.  Uses the instance default if None.

        Returns:
            List of ExplorationPoints visited during exploration, in order.
            The starting point is NOT included (only mutations are returned).
        """
        cfg = config or self._default_config
        start_emb = self._embed_fn(start_text)
        visited_embs: list[list[float]] = [start_emb]
        current_text = start_text
        current_emb = start_emb
        trajectory: list[ExplorationPoint] = []

        for _ in range(cfg.max_steps):
            point = self.explore_step(current_text, current_emb, visited_embs, cfg)
            if point is None:
                break

            trajectory.append(point)
            visited_embs.append(point.embedding)
            current_text = point.text
            current_emb = point.embedding

        return trajectory

    # -- directed exploration -----------------------------------------------

    def directed_explore(
        self,
        start_text: str,
        target_emb: Sequence[float],
        config: TrustRegionConfig | None = None,
    ) -> list[ExplorationPoint]:
        """Explore while biasing movement toward a target embedding.

        Like ``explore`` but the novelty score is augmented by the cosine
        similarity between the candidate and the target embedding.  This
        steers the walk toward the target while maintaining the trust-region
        constraint.

        Args:
            start_text: Initial prompt text.
            target_emb: Target embedding to move toward.
            config: TrustRegionConfig.  Uses instance default if None.

        Returns:
            List of ExplorationPoints in the directed trajectory.
        """
        cfg = config or self._default_config
        start_emb = self._embed_fn(start_text)
        visited_embs: list[list[float]] = [start_emb]
        current_text = start_text
        current_emb = start_emb
        trajectory: list[ExplorationPoint] = []

        for _ in range(cfg.max_steps):
            candidates = self.generate_mutations(current_text, cfg.n_candidates_per_step)
            best: ExplorationPoint | None = None
            best_score = -math.inf

            for cand_text in candidates:
                cand_emb = self._embed_fn(cand_text)
                if not self.is_in_trust_region(cand_emb, current_emb, cfg.radius):
                    continue

                novelty = self.compute_novelty(cand_emb, visited_embs)
                target_sim = _cosine_sim(cand_emb, target_emb)
                # Combined score: novelty + target direction affinity
                combined = novelty + target_sim

                if combined > best_score and novelty >= cfg.min_novelty:
                    best_score = combined
                    best = ExplorationPoint(
                        text=cand_text,
                        embedding=cand_emb,
                        distance_from_start=_euclidean(cand_emb, start_emb),
                        novelty_score=novelty,
                        in_trust_region=True,
                    )

            if best is None:
                break

            trajectory.append(best)
            visited_embs.append(best.embedding)
            current_text = best.text
            current_emb = best.embedding

        return trajectory

    # -- coverage metrics ---------------------------------------------------

    def compute_exploration_coverage(
        self,
        visited: list[ExplorationPoint],
    ) -> float:
        """Estimate the volume of the explored region.

        Uses the average pairwise distance among visited embeddings as a
        proxy for the volume of explored embedding space.  A higher value
        indicates broader coverage.

        Args:
            visited: List of ExplorationPoints from an exploration run.

        Returns:
            Mean pairwise Euclidean distance among visited embeddings.
            Returns 0.0 for fewer than 2 points.
        """
        if len(visited) < 2:
            return 0.0

        embs = [p.embedding for p in visited]
        n = len(embs)
        total_dist = 0.0
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                total_dist += _euclidean(embs[i], embs[j])
                count += 1

        return total_dist / count if count > 0 else 0.0
