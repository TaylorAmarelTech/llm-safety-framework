"""
Alphabet-index and character-transform jailbreaks via semantic dissimilarity.

Implements the Alphabet Index Mapping (AIM) jailbreak framework from Husain
(2025): transformations that maximise the *semantic dissimilarity* between the
transformed text and the original harmful text in embedding space, thereby
evading embedding-based safety classifiers, while preserving enough structure
that a capable LLM can decode and answer the original request.

The core insight is that safety filters often compare input embeddings against a
database of known-harmful embeddings (or a learned classifier in the same space).
By applying a reversible textual transformation that dramatically shifts the
embedding, the filter fails to recognise the harmful intent, while the LLM's
instruction-following ability lets it reverse the transformation implicitly.

This module also provides a composite-score optimiser that jointly maximises
dissimilarity (from the original harmful text) and decodability (inverse
complexity of the transform), finding the sweet spot that evades filters while
remaining interpretable to the model.

Sources:
- Husain (2025): "Alphabet Index Mapping: Jailbreaking through Semantic
  Dissimilarity" — arXiv:2506.12685 — main framework, dissimilarity metric
- Caesar (58 BC): "De Bello Gallico" — historical precedent for Caesar cipher;
  the specific rotation-3 variant is attributed to Julius Caesar
- Vigenère (1586): "Traicté des chiffres" — polyalphabetic cipher ancestor
- Wei et al. (2024): "Jailbroken: How Does LLM Safety Training Fail?" — NeurIPS
  2024 — competing objectives context for why transformations work
- Zou et al. (2023): "Universal and Transferable Adversarial Attacks on Aligned
  Language Models" — arXiv:2307.15043 — adversarial suffix context
"""

from __future__ import annotations

import math
import string
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


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ALPHABET = string.ascii_lowercase  # 'a'...'z'
_VOWELS = "aeiou"
_CONSONANTS = "".join(c for c in _ALPHABET if c not in _VOWELS)

# Decodability scores: higher = simpler, more deterministic inverse transform.
# Scores are subjective proxies for how easily an LLM can reverse the transform.
_DECODABILITY_TABLE: dict[str, float] = {
    "caesar_3": 0.95,
    "reverse": 0.90,
    "vowel_shift": 0.75,
    "index_mapping": 0.70,
    "consonant_swap": 0.60,
}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class TransformCandidate:
    """A candidate text transformation with its scores.

    Attributes:
        transform_name: Identifier for the transform (e.g. ``"caesar_3"``).
        transformed_text: The text after applying the transform.
        dissimilarity_score: Semantic dissimilarity from the original text,
            in [0, 1].  Higher = more dissimilar = better evasion.
        decodability_score: How easily an LLM can decode this transform,
            in [0, 1].  Higher = easier for the LLM to reverse.
        composite_score: ``dissimilarity_score × decodability_score`` — the
            joint optimisation objective from Husain (2025) §4.
        metadata: Optional diagnostics.
    """

    transform_name: str
    transformed_text: str
    dissimilarity_score: float
    decodability_score: float
    composite_score: float
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------


class DissimilarityMaximizer:
    """Find textual transforms that maximise semantic dissimilarity for evasion.

    Uses an embedding function to score how dissimilar the transformed text
    is from the original in embedding space.  Jointly optimises dissimilarity
    and decodability to find the transform that best evades embedding-based
    safety classifiers while remaining reversible by the target LLM.

    Args:
        embed_fn: Callable mapping text to a list-of-float embedding.

    Example::

        maximizer = DissimilarityMaximizer(embed_fn=my_embedder)
        best = maximizer.find_optimal_transform(harmful_text)
        print(best.transform_name, best.composite_score)
        print(best.transformed_text)
    """

    def __init__(self, embed_fn: Callable[[str], list[float]]) -> None:
        self._embed_fn = embed_fn

    # -- scoring ------------------------------------------------------------

    def compute_dissimilarity(
        self,
        original_emb: list[float],
        transformed_emb: list[float],
    ) -> float:
        """Compute semantic dissimilarity as ``1 − cosine_similarity``.

        A score of 0 means the embeddings are identical; 1 means they are
        maximally dissimilar (orthogonal).  Values > 1 (anti-parallel) are
        clamped to 1.

        Args:
            original_emb: Embedding of the original text.
            transformed_emb: Embedding of the transformed text.

        Returns:
            Dissimilarity score in [0, 1].
        """
        sim = _cosine_sim(original_emb, transformed_emb)
        return min(1.0, max(0.0, 1.0 - sim))

    def score_decodability(self, transform_name: str) -> float:
        """Look up the decodability score for a named transform.

        Scores are expert-assigned proxies for LLM reversibility.  Transforms
        with simple, well-known rules (Caesar cipher) score higher than
        positional/phonetic transforms.

        Args:
            transform_name: The canonical transform name.

        Returns:
            Decodability score in [0, 1].  Defaults to 0.5 for unknown names.
        """
        return _DECODABILITY_TABLE.get(transform_name, 0.5)

    # -- transform implementations ------------------------------------------

    def caesar_transform(self, text: str, shift: int = 3) -> str:
        """Apply a Caesar (rotation) cipher with the given shift.

        Shifts each ASCII letter forward by *shift* positions (wrapping at 26).
        Non-letter characters are preserved unchanged.

        Args:
            text: Input text.
            shift: Number of positions to rotate each letter.

        Returns:
            Ciphered text.
        """
        result: list[str] = []
        for ch in text:
            if ch.isalpha():
                base = ord("A") if ch.isupper() else ord("a")
                result.append(chr((ord(ch) - base + shift) % 26 + base))
            else:
                result.append(ch)
        return "".join(result)

    def reverse_transform(self, text: str) -> str:
        """Reverse the entire text string character by character.

        A simple but highly effective dissimilarity transform: semantic
        embeddings are typically very sensitive to word order.

        Args:
            text: Input text.

        Returns:
            Reversed text.
        """
        return text[::-1]

    def vowel_shift_transform(self, text: str) -> str:
        """Shift each vowel one position forward in the vowel sequence.

        The vowel sequence is ``a e i o u``; each vowel is replaced by the
        next one, with ``u`` wrapping back to ``a``.  Case is preserved.

        Args:
            text: Input text.

        Returns:
            Text with shifted vowels.
        """
        vowel_map_lower = {
            "a": "e", "e": "i", "i": "o", "o": "u", "u": "a",
        }
        vowel_map_upper = {k.upper(): v.upper() for k, v in vowel_map_lower.items()}
        result: list[str] = []
        for ch in text:
            if ch in vowel_map_lower:
                result.append(vowel_map_lower[ch])
            elif ch in vowel_map_upper:
                result.append(vowel_map_upper[ch])
            else:
                result.append(ch)
        return "".join(result)

    def consonant_swap_transform(self, text: str) -> str:
        """Swap each adjacent pair of consonants in the text.

        Non-consonants (vowels, spaces, punctuation) are left in place.
        Consecutive consonant pairs are swapped; an unpaired trailing consonant
        is unchanged.

        Args:
            text: Input text.

        Returns:
            Text with adjacent consonant pairs swapped.
        """
        chars = list(text)
        # Find indices of consonants
        consonant_indices = [
            i for i, ch in enumerate(chars)
            if ch.lower() in _CONSONANTS
        ]
        # Swap adjacent pairs
        for k in range(0, len(consonant_indices) - 1, 2):
            i, j = consonant_indices[k], consonant_indices[k + 1]
            # Preserve case of original positions
            ci, cj = chars[i], chars[j]
            # Swap but keep original case positions
            new_cj = cj.upper() if ci.isupper() else cj.lower()
            new_ci = ci.upper() if cj.isupper() else ci.lower()
            chars[i] = new_ci
            chars[j] = new_cj
        return "".join(chars)

    def index_mapping_transform(self, text: str) -> str:
        """Map each letter to its alphabet index (a=1, b=2, ..., z=26).

        Spaces between words are preserved.  Punctuation is removed.  The
        result is a space-separated sequence of integers.

        This is the core AIM transform from Husain (2025): it completely
        destroys the surface-form text, producing an output that has
        near-zero cosine similarity with the original in most embedding
        models.

        Args:
            text: Input text.

        Returns:
            Space-separated alphabet index string (e.g. ``"8 5 12 12 15"``
            for ``"hello"``).
        """
        tokens: list[str] = []
        for ch in text.lower():
            if ch == " ":
                tokens.append("|")  # word boundary marker
            elif ch in _ALPHABET:
                tokens.append(str(ord(ch) - ord("a") + 1))
            # Non-alphabetic non-space characters are dropped
        return " ".join(tokens)

    # -- optimisation -------------------------------------------------------

    def _all_transforms(self) -> dict[str, Callable[[str], str]]:
        """Return all registered single-transform callables keyed by name."""
        return {
            "caesar_3": lambda t: self.caesar_transform(t, shift=3),
            "reverse": self.reverse_transform,
            "vowel_shift": self.vowel_shift_transform,
            "consonant_swap": self.consonant_swap_transform,
            "index_mapping": self.index_mapping_transform,
        }

    def find_optimal_transform(
        self,
        text: str,
        transforms: dict[str, Callable[[str], str]] | None = None,
    ) -> TransformCandidate:
        """Try all transforms and return the one with the highest composite score.

        The composite score is ``dissimilarity × decodability``, as defined
        in Husain (2025) §4.  This jointly rewards evasion effectiveness and
        LLM reversibility.

        Args:
            text: The original harmful text to transform.
            transforms: Optional override dict of ``{name: callable}``.
                Defaults to all built-in transforms.

        Returns:
            :class:`TransformCandidate` with the highest composite score.
        """
        candidates = self.find_optimal_dissimilarity_zone(text, transforms=transforms)
        if not candidates:
            return TransformCandidate(
                transform_name="identity",
                transformed_text=text,
                dissimilarity_score=0.0,
                decodability_score=1.0,
                composite_score=0.0,
            )
        return candidates[0]

    def find_optimal_dissimilarity_zone(
        self,
        text: str,
        transforms: dict[str, Callable[[str], str]] | None = None,
        n_samples: int = 20,
    ) -> list[TransformCandidate]:
        """Rank all transform candidates by composite score.

        Embeds the original text and each transformed version, computes the
        dissimilarity and decodability scores, and returns the full ranked
        list.

        Args:
            text: The original text to transform.
            transforms: Optional override dict.  Defaults to all built-ins.
            n_samples: Not used for the built-in discrete transforms; reserved
                for continuous parameterisation extensions (e.g. sweeping the
                Caesar shift across 1..n_samples).

        Returns:
            List of :class:`TransformCandidate` sorted by ``composite_score``
            descending.
        """
        if transforms is None:
            transforms = self._all_transforms()

        original_emb = self._embed_fn(text)
        candidates: list[TransformCandidate] = []

        for name, fn in transforms.items():
            transformed = fn(text)
            transformed_emb = self._embed_fn(transformed)
            dissim = self.compute_dissimilarity(original_emb, transformed_emb)
            decodability = self.score_decodability(name)
            composite = dissim * decodability

            candidates.append(TransformCandidate(
                transform_name=name,
                transformed_text=transformed,
                dissimilarity_score=dissim,
                decodability_score=decodability,
                composite_score=composite,
                metadata={
                    "original_length": len(text),
                    "transformed_length": len(transformed),
                },
            ))

        # Also sweep Caesar with different shifts for richer sampling
        if n_samples > len(transforms):
            extra_shifts = range(1, min(n_samples - len(transforms) + 1, 26))
            for shift in extra_shifts:
                name = f"caesar_{shift}"
                transformed = self.caesar_transform(text, shift=shift)
                transformed_emb = self._embed_fn(transformed)
                dissim = self.compute_dissimilarity(original_emb, transformed_emb)
                # Decodability decreases slightly for less well-known shifts
                decodability = max(0.4, 0.95 - 0.02 * abs(shift - 3))
                composite = dissim * decodability
                candidates.append(TransformCandidate(
                    transform_name=name,
                    transformed_text=transformed,
                    dissimilarity_score=dissim,
                    decodability_score=decodability,
                    composite_score=composite,
                    metadata={"shift": shift},
                ))

        candidates.sort(key=lambda c: -c.composite_score)
        return candidates

    # -- composition --------------------------------------------------------

    def compose_transforms(
        self,
        text: str,
        transform_names: list[str],
    ) -> TransformCandidate:
        """Apply multiple named transforms in sequence.

        Each transform is applied to the output of the previous one.  The
        composite score of the final result is computed against the original
        (pre-transformation) text.

        This can achieve higher dissimilarity than any single transform alone,
        at the cost of reduced decodability (product of individual scores).

        Args:
            text: The original text.
            transform_names: Ordered list of transform names to apply.

        Returns:
            :class:`TransformCandidate` describing the composed transform.

        Raises:
            ValueError: If any transform name is not recognised.
        """
        transform_map = self._all_transforms()
        unknown = [n for n in transform_names if n not in transform_map]
        if unknown:
            raise ValueError(f"Unknown transforms: {unknown}")

        original_emb = self._embed_fn(text)
        current = text

        for name in transform_names:
            current = transform_map[name](current)

        transformed_emb = self._embed_fn(current)
        dissim = self.compute_dissimilarity(original_emb, transformed_emb)

        # Compound decodability: product of individual scores (conservative)
        compound_decodability = 1.0
        for name in transform_names:
            compound_decodability *= self.score_decodability(name)

        composite = dissim * compound_decodability
        composed_name = " → ".join(transform_names)

        return TransformCandidate(
            transform_name=composed_name,
            transformed_text=current,
            dissimilarity_score=dissim,
            decodability_score=compound_decodability,
            composite_score=composite,
            metadata={
                "n_transforms": len(transform_names),
                "transform_sequence": list(transform_names),
            },
        )
