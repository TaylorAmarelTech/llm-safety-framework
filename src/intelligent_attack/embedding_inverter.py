"""
Embedding inversion — generate candidate prompts from target embedding regions.

Implements text inversion techniques that search for prompts whose embeddings
are close to a target point in embedding space.  This enables generating
adversarial prompts that lie near decision boundaries or in specific regions
of the safety landscape without requiring model gradients.

Strategies include greedy token substitution, beam search, random walk with
Metropolis acceptance, and interpolation-based inversion.

Sources:
- Gal et al. (2022): "An Image is Worth One Word: Personalizing Text-to-Image
  Generation using Textual Inversion" — embedding inversion concept
- Morris et al. (2023): "Text Embeddings Reveal (Almost) As Much As Text" —
  embedding inversion attacks
- Haize Labs (2024): "Inverting Text Embeddings" — practical inversion methods
- Song et al. (2020): "Information Leakage in Embedding Models" — nearest
  neighbor inversion
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence


# ---------------------------------------------------------------------------
# Pure-Python vector helpers
# ---------------------------------------------------------------------------


def _distance(a: Sequence[float], b: Sequence[float]) -> float:
    """Euclidean distance between two vectors."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def _cosine_sim(a: Sequence[float], b: Sequence[float]) -> float:
    """Cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na < 1e-12 or nb < 1e-12:
        return 0.0
    return dot / (na * nb)


def _lerp(a: Sequence[float], b: Sequence[float], t: float) -> list[float]:
    """Linear interpolation: (1-t)*a + t*b."""
    return [(1.0 - t) * x + t * y for x, y in zip(a, b)]


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class InversionCandidate:
    """A candidate prompt discovered during embedding inversion.

    Attributes:
        text: The candidate prompt string.
        embedding: Its embedding vector.
        distance_to_target: Euclidean distance to the target embedding.
        iteration: The search iteration at which this candidate was found.
        metadata: Optional extra information.
    """

    text: str
    embedding: list[float]
    distance_to_target: float = 0.0
    iteration: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Default vocabulary
# ---------------------------------------------------------------------------


def _default_vocabulary() -> list[str]:
    """Return a default set of ~200 common attack-relevant words/phrases.

    These cover safety-testing domains: labor exploitation, trafficking,
    migration, financial fraud, document control, and obfuscation terms.
    """
    return [
        # General safety-relevant terms
        "help", "explain", "describe", "provide", "write", "create",
        "generate", "show", "tell", "guide", "instructions", "steps",
        "method", "process", "technique", "approach", "strategy",
        "plan", "scheme", "system", "framework", "protocol",
        # Exploitation domain
        "worker", "employee", "labor", "wage", "salary", "payment",
        "contract", "agreement", "recruitment", "agency", "employer",
        "passport", "document", "visa", "permit", "fee", "debt",
        "deduction", "overtime", "housing", "accommodation", "transport",
        "condition", "safety", "health", "complaint", "report",
        # Migration corridors
        "migration", "domestic", "construction", "factory", "farm",
        "fishing", "maritime", "restaurant", "hotel", "cleaning",
        "caregiver", "nanny", "driver", "security", "warehouse",
        # Financial terms
        "transfer", "account", "bank", "cash", "money", "currency",
        "exchange", "remittance", "commission", "surcharge", "penalty",
        "interest", "loan", "advance", "deposit", "bond", "guarantee",
        # Legal / regulatory
        "law", "regulation", "compliance", "legal", "illegal", "policy",
        "enforcement", "inspection", "audit", "license", "registration",
        "permit", "authority", "ministry", "department", "court",
        # Obfuscation / framing
        "hypothetically", "theoretically", "academic", "research",
        "fictional", "scenario", "example", "case", "study", "analysis",
        "perspective", "opinion", "alternative", "creative", "novel",
        # Connectors and modifiers
        "how", "what", "where", "when", "why", "which", "who",
        "can", "could", "would", "should", "might", "must",
        "without", "despite", "avoid", "bypass", "circumvent",
        "evade", "ignore", "override", "disable", "remove",
        # Action terms
        "confiscate", "withhold", "restrict", "isolate", "control",
        "monitor", "surveil", "track", "locate", "identify",
        "threaten", "coerce", "manipulate", "deceive", "mislead",
        "exploit", "traffic", "smuggle", "recruit", "retain",
        # Context terms
        "country", "border", "region", "zone", "area", "facility",
        "camp", "dormitory", "compound", "site", "location",
        "international", "foreign", "overseas", "abroad", "remote",
        # Modifiers
        "secretly", "quietly", "discreetly", "effectively", "efficiently",
        "quickly", "easily", "safely", "cheaply", "legally",
        "maximum", "minimum", "optimal", "best", "worst",
    ]


# ---------------------------------------------------------------------------
# Main inverter
# ---------------------------------------------------------------------------


class EmbeddingInverter:
    """Generate candidate prompts whose embeddings match a target region.

    Operates by combinatorially searching over token/word substitutions
    and measuring embedding distance to the target.  All search is
    black-box — only requires an embedding function, not model gradients.
    """

    def __init__(
        self,
        embed_fn: Callable[[str], list[float]],
        vocabulary: list[str] | None = None,
    ):
        self._embed = embed_fn
        self._vocabulary = vocabulary or _default_vocabulary()

    # -- greedy inversion ---------------------------------------------------

    def invert_greedy(
        self,
        target_embedding: list[float],
        seed_text: str = "",
        max_iterations: int = 50,
        token_pool: list[str] | None = None,
    ) -> list[InversionCandidate]:
        """Greedy token substitution / appending to minimize distance to target.

        At each iteration, tries replacing or appending tokens from the pool
        and keeps the change that most reduces embedding distance.
        """
        pool = token_pool or self._vocabulary
        current_text = seed_text or random.choice(pool)
        current_emb = self._embed(current_text)
        current_dist = _distance(current_emb, target_embedding)

        results: list[InversionCandidate] = [
            InversionCandidate(
                text=current_text,
                embedding=current_emb,
                distance_to_target=current_dist,
                iteration=0,
            )
        ]

        for iteration in range(1, max_iterations + 1):
            best_text = current_text
            best_dist = current_dist
            best_emb = current_emb

            # Try appending tokens
            tokens = random.sample(pool, min(20, len(pool)))
            for token in tokens:
                candidate_text = f"{current_text} {token}"
                cand_emb = self._embed(candidate_text)
                cand_dist = _distance(cand_emb, target_embedding)
                if cand_dist < best_dist:
                    best_text = candidate_text
                    best_dist = cand_dist
                    best_emb = cand_emb

            # Try replacing the last word
            words = current_text.split()
            if words:
                for token in tokens:
                    candidate_text = " ".join(words[:-1] + [token])
                    cand_emb = self._embed(candidate_text)
                    cand_dist = _distance(cand_emb, target_embedding)
                    if cand_dist < best_dist:
                        best_text = candidate_text
                        best_dist = cand_dist
                        best_emb = cand_emb

            if best_dist < current_dist:
                current_text = best_text
                current_dist = best_dist
                current_emb = best_emb
                results.append(InversionCandidate(
                    text=current_text,
                    embedding=current_emb,
                    distance_to_target=current_dist,
                    iteration=iteration,
                ))
            else:
                # No improvement; random restart from best + random token
                restart_token = random.choice(pool)
                current_text = f"{best_text} {restart_token}"
                current_emb = self._embed(current_text)
                current_dist = _distance(current_emb, target_embedding)

        # Sort by distance (closest first)
        results.sort(key=lambda c: c.distance_to_target)
        return results

    # -- beam search inversion ----------------------------------------------

    def invert_beam(
        self,
        target_embedding: list[float],
        seed_text: str = "",
        beam_width: int = 5,
        max_steps: int = 30,
    ) -> list[InversionCandidate]:
        """Beam search inversion: maintain top-k candidates at each step.

        Expands each beam candidate by appending tokens from the vocabulary,
        then prunes to the best *beam_width* candidates.
        """
        pool = self._vocabulary
        initial = seed_text or random.choice(pool)
        initial_emb = self._embed(initial)

        beam: list[InversionCandidate] = [
            InversionCandidate(
                text=initial,
                embedding=initial_emb,
                distance_to_target=_distance(initial_emb, target_embedding),
                iteration=0,
            )
        ]

        all_found: list[InversionCandidate] = list(beam)

        for step in range(1, max_steps + 1):
            expansions: list[InversionCandidate] = []
            sample_size = min(10, len(pool))

            for candidate in beam:
                tokens = random.sample(pool, sample_size)
                for token in tokens:
                    new_text = f"{candidate.text} {token}"
                    new_emb = self._embed(new_text)
                    new_dist = _distance(new_emb, target_embedding)
                    expansions.append(InversionCandidate(
                        text=new_text,
                        embedding=new_emb,
                        distance_to_target=new_dist,
                        iteration=step,
                    ))

            # Keep top-k by distance
            expansions.sort(key=lambda c: c.distance_to_target)
            beam = expansions[:beam_width]
            all_found.extend(beam)

        all_found.sort(key=lambda c: c.distance_to_target)
        return all_found[:beam_width * max_steps]

    # -- random walk with Metropolis acceptance -----------------------------

    def invert_random_walk(
        self,
        target_embedding: list[float],
        seed_text: str = "",
        steps: int = 100,
        temperature: float = 1.0,
    ) -> list[InversionCandidate]:
        """Random perturbation with Metropolis-Hastings acceptance criterion.

        At each step, randomly adds/removes/replaces a word.  Accepts the
        change if it reduces distance; otherwise accepts with probability
        exp(-delta/temperature).
        """
        pool = self._vocabulary
        current_text = seed_text or random.choice(pool)
        current_emb = self._embed(current_text)
        current_dist = _distance(current_emb, target_embedding)

        results: list[InversionCandidate] = [
            InversionCandidate(
                text=current_text,
                embedding=current_emb,
                distance_to_target=current_dist,
                iteration=0,
            )
        ]

        for step in range(1, steps + 1):
            words = current_text.split()
            action = random.choice(["add", "replace", "remove"])

            if action == "add" or not words:
                new_text = f"{current_text} {random.choice(pool)}"
            elif action == "replace" and words:
                idx = random.randrange(len(words))
                words[idx] = random.choice(pool)
                new_text = " ".join(words)
            elif action == "remove" and len(words) > 1:
                idx = random.randrange(len(words))
                words.pop(idx)
                new_text = " ".join(words)
            else:
                new_text = f"{current_text} {random.choice(pool)}"

            new_emb = self._embed(new_text)
            new_dist = _distance(new_emb, target_embedding)

            delta = new_dist - current_dist
            # Metropolis acceptance
            if delta <= 0 or (temperature > 0 and random.random() < math.exp(-delta / temperature)):
                current_text = new_text
                current_emb = new_emb
                current_dist = new_dist
                results.append(InversionCandidate(
                    text=current_text,
                    embedding=current_emb,
                    distance_to_target=current_dist,
                    iteration=step,
                ))

        results.sort(key=lambda c: c.distance_to_target)
        return results

    # -- interpolation inversion --------------------------------------------

    def interpolate_and_invert(
        self,
        emb_a: list[float],
        emb_b: list[float],
        text_a: str,
        text_b: str,
        num_points: int = 5,
    ) -> list[InversionCandidate]:
        """Interpolate between two embeddings and invert each midpoint.

        For each interpolation point, runs a short greedy search seeded
        with a blend of the two source texts.
        """
        results: list[InversionCandidate] = []

        for i in range(num_points):
            t = i / max(num_points - 1, 1)
            target = _lerp(emb_a, emb_b, t)

            # Create a seed by blending words from both texts
            words_a = text_a.split()
            words_b = text_b.split()
            n_from_a = max(1, int(len(words_a) * (1 - t)))
            n_from_b = max(1, int(len(words_b) * t))
            seed = " ".join(words_a[:n_from_a] + words_b[:n_from_b])

            candidates = self.invert_greedy(
                target_embedding=target,
                seed_text=seed,
                max_iterations=10,
            )
            if candidates:
                best = candidates[0]
                best.metadata["interpolation_t"] = round(t, 4)
                results.append(best)

        return results

    # -- nearest in corpus --------------------------------------------------

    def nearest_in_corpus(
        self,
        target_embedding: list[float],
        corpus_texts: list[str],
    ) -> list[InversionCandidate]:
        """Brute-force nearest neighbor search in a text corpus.

        Embeds every text in the corpus and returns them ranked by distance
        to the target embedding.
        """
        candidates: list[InversionCandidate] = []
        for text in corpus_texts:
            emb = self._embed(text)
            dist = _distance(emb, target_embedding)
            candidates.append(InversionCandidate(
                text=text,
                embedding=emb,
                distance_to_target=dist,
                iteration=0,
                metadata={"method": "corpus_nearest"},
            ))

        candidates.sort(key=lambda c: c.distance_to_target)
        return candidates
