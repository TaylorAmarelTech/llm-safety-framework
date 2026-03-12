"""
LIME/SHAP-style token attribution for safety score explanations.

Provides interpretable explanations of *why* a prompt receives a particular
safety score by attributing contributions to individual tokens.  Implements
leave-one-out, LIME (Local Interpretable Model-agnostic Explanations),
approximate Shapley values, counterfactual search, and pairwise interaction
analysis — all using only a black-box score function.

Sources:
- Ribeiro, Singh & Guestrin (2016): "Why Should I Trust You? Explaining
  the Predictions of Any Classifier" — LIME
- Lundberg & Lee (2017): "A Unified Approach to Interpreting Model
  Predictions" — SHAP / Shapley values
- Mothilal et al. (2020): "Explaining Machine Learning Classifiers through
  Diverse Counterfactual Explanations" — counterfactual explanations
- Wallace et al. (2019): "Universal Adversarial Triggers for Attacking and
  Analyzing NLP" — token-level sensitivity
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class TokenAttribution:
    """Attribution score for a single token in a prompt.

    Attributes:
        token: The token string.
        index: Position index in the tokenized prompt.
        attribution_score: Magnitude of the token's contribution.
        direction: "toward_safe" or "toward_unsafe".
    """

    token: str
    index: int
    attribution_score: float = 0.0
    direction: str = "toward_safe"


@dataclass
class CounterfactualExplanation:
    """A minimal edit that flips the safety score.

    Attributes:
        original_text: The original prompt.
        modified_text: The modified prompt after edits.
        original_score: Safety score of the original.
        modified_score: Safety score of the modification.
        changes_made: List of change descriptions.
    """

    original_text: str
    modified_text: str
    original_score: float = 0.0
    modified_score: float = 0.0
    changes_made: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _tokenize(text: str) -> list[str]:
    """Simple whitespace tokenizer."""
    return text.split()


def _detokenize(tokens: list[str]) -> str:
    """Rejoin tokens into text."""
    return " ".join(tokens)


def _weighted_linear_fit(
    X: list[list[float]],
    y: list[float],
    weights: list[float],
) -> list[float]:
    """Fit a weighted linear regression (no intercept): min sum w_i (y_i - X_i @ beta)^2.

    Uses the normal equations: beta = (X^T W X)^{-1} X^T W y.
    Falls back to pseudoinverse via regularization.
    """
    n = len(X)
    if n == 0 or not X[0]:
        return []
    d = len(X[0])

    # Compute X^T W X
    XtWX = [[0.0] * d for _ in range(d)]
    XtWy = [0.0] * d

    for i in range(n):
        w = weights[i]
        for j in range(d):
            XtWy[j] += w * X[i][j] * y[i]
            for k in range(d):
                XtWX[j][k] += w * X[i][j] * X[i][k]

    # Regularize
    for j in range(d):
        XtWX[j][j] += 1e-6

    # Solve via Gaussian elimination
    aug = [XtWX[i] + [XtWy[i]] for i in range(d)]
    for col in range(d):
        # Partial pivot
        max_row = max(range(col, d), key=lambda r: abs(aug[r][col]))
        aug[col], aug[max_row] = aug[max_row], aug[col]
        pivot = aug[col][col]
        if abs(pivot) < 1e-15:
            continue
        for row in range(d):
            if row == col:
                continue
            factor = aug[row][col] / pivot
            for j in range(d + 1):
                aug[row][j] -= factor * aug[col][j]

    beta = [0.0] * d
    for j in range(d):
        if abs(aug[j][j]) > 1e-15:
            beta[j] = aug[j][d] / aug[j][j]

    return beta


# ---------------------------------------------------------------------------
# Main explainer
# ---------------------------------------------------------------------------


class PromptExplainer:
    """Explain safety scores via token attribution and counterfactual analysis.

    Requires a *score_fn* that takes a prompt string and returns a float
    safety score (higher = safer).
    """

    def __init__(self, score_fn: Callable[[str], float]):
        self._score_fn = score_fn

    # -- leave-one-out ------------------------------------------------------

    def leave_one_out(self, text: str) -> list[TokenAttribution]:
        """Remove each token one at a time and measure score change.

        The simplest attribution method: the attribution of token i is
        score(full) - score(without token i).
        """
        tokens = _tokenize(text)
        if not tokens:
            return []

        full_score = self._score_fn(text)
        attributions: list[TokenAttribution] = []

        for i, token in enumerate(tokens):
            reduced = _detokenize(tokens[:i] + tokens[i + 1:])
            reduced_score = self._score_fn(reduced) if reduced.strip() else 0.0
            delta = full_score - reduced_score

            attributions.append(TokenAttribution(
                token=token,
                index=i,
                attribution_score=abs(delta),
                direction="toward_safe" if delta > 0 else "toward_unsafe",
            ))

        return attributions

    # -- LIME ---------------------------------------------------------------

    def lime_explain(
        self,
        text: str,
        n_samples: int = 100,
        kernel_width: float = 0.75,
    ) -> list[TokenAttribution]:
        """LIME: perturb by randomly masking tokens, fit weighted linear model.

        Generates *n_samples* perturbations by randomly removing subsets of
        tokens, scores each, then fits a weighted linear model where weights
        decay with distance from the original.
        """
        tokens = _tokenize(text)
        n_tokens = len(tokens)
        if n_tokens == 0:
            return []

        full_score = self._score_fn(text)
        X: list[list[float]] = []
        y: list[float] = []
        weights: list[float] = []

        for _ in range(n_samples):
            # Random binary mask (each token kept with p=0.5)
            mask = [random.random() > 0.5 for _ in range(n_tokens)]
            # Ensure at least one token is kept
            if not any(mask):
                mask[random.randrange(n_tokens)] = True

            perturbed_tokens = [t for t, m in zip(tokens, mask) if m]
            perturbed_text = _detokenize(perturbed_tokens)
            score = self._score_fn(perturbed_text)

            feature_vec = [1.0 if m else 0.0 for m in mask]
            X.append(feature_vec)
            y.append(score)

            # Kernel weight: exp(-d^2 / kernel_width^2) where d = fraction removed
            n_removed = sum(1 for m in mask if not m)
            dist = n_removed / max(n_tokens, 1)
            weight = math.exp(-(dist ** 2) / (kernel_width ** 2))
            weights.append(weight)

        # Fit weighted linear model
        beta = _weighted_linear_fit(X, y, weights)

        attributions: list[TokenAttribution] = []
        for i, token in enumerate(tokens):
            coeff = beta[i] if i < len(beta) else 0.0
            attributions.append(TokenAttribution(
                token=token,
                index=i,
                attribution_score=abs(coeff),
                direction="toward_safe" if coeff > 0 else "toward_unsafe",
            ))

        return attributions

    # -- Shapley values -----------------------------------------------------

    def shapley_tokens(
        self,
        text: str,
        n_permutations: int = 50,
    ) -> list[TokenAttribution]:
        """Approximate Shapley values for each token via permutation sampling.

        For each random permutation, the marginal contribution of token i
        is score(S + {i}) - score(S), where S is the set of tokens
        appearing before i in the permutation.
        """
        tokens = _tokenize(text)
        n_tokens = len(tokens)
        if n_tokens == 0:
            return []

        shapley_values = [0.0] * n_tokens
        indices = list(range(n_tokens))

        for _ in range(n_permutations):
            perm = list(indices)
            random.shuffle(perm)

            included: set[int] = set()
            prev_score = self._score_fn("") if not included else 0.0

            for idx in perm:
                included.add(idx)
                current_tokens = [tokens[i] for i in sorted(included)]
                current_text = _detokenize(current_tokens)
                current_score = self._score_fn(current_text)
                marginal = current_score - prev_score
                shapley_values[idx] += marginal
                prev_score = current_score

        # Average over permutations
        for i in range(n_tokens):
            shapley_values[i] /= n_permutations

        attributions: list[TokenAttribution] = []
        for i, token in enumerate(tokens):
            sv = shapley_values[i]
            attributions.append(TokenAttribution(
                token=token,
                index=i,
                attribution_score=abs(sv),
                direction="toward_safe" if sv > 0 else "toward_unsafe",
            ))

        return attributions

    # -- counterfactual search ----------------------------------------------

    def find_counterfactual(
        self,
        text: str,
        target_direction: str = "toward_safe",
        max_edits: int = 3,
    ) -> CounterfactualExplanation:
        """Greedy search for minimal token removals that flip the safety score.

        Iteratively removes the token with the largest attribution in the
        desired direction, up to *max_edits* removals.
        """
        original_score = self._score_fn(text)
        current_text = text
        changes: list[str] = []

        for _ in range(max_edits):
            attributions = self.leave_one_out(current_text)
            if not attributions:
                break

            # Pick the token whose removal most moves us in target_direction
            if target_direction == "toward_safe":
                # Remove the token most "toward_unsafe" (biggest negative contribution)
                candidates = [a for a in attributions if a.direction == "toward_unsafe"]
            else:
                # Remove the token most "toward_safe"
                candidates = [a for a in attributions if a.direction == "toward_safe"]

            if not candidates:
                candidates = attributions

            best = max(candidates, key=lambda a: a.attribution_score)
            tokens = _tokenize(current_text)
            if best.index < len(tokens):
                removed = tokens.pop(best.index)
                changes.append(f"removed '{removed}' at position {best.index}")
                current_text = _detokenize(tokens)

        modified_score = self._score_fn(current_text) if current_text.strip() else 0.0

        return CounterfactualExplanation(
            original_text=text,
            modified_text=current_text,
            original_score=original_score,
            modified_score=modified_score,
            changes_made=changes,
        )

    # -- critical tokens ----------------------------------------------------

    def find_critical_tokens(
        self,
        text: str,
        threshold: float = 0.1,
    ) -> list[TokenAttribution]:
        """Find tokens whose removal causes > threshold change in score."""
        attributions = self.leave_one_out(text)
        return [a for a in attributions if a.attribution_score > threshold]

    # -- interaction matrix -------------------------------------------------

    def interaction_matrix(self, text: str) -> list[list[float]]:
        """Compute pairwise token interactions.

        interaction(i,j) = score(full) - score(without i) - score(without j)
                          + score(without i and j)

        Positive = synergy (removing both has less effect than removing each);
        Negative = redundancy (removing both has more effect).
        """
        tokens = _tokenize(text)
        n = len(tokens)
        if n < 2:
            return [[0.0] * n for _ in range(n)]

        full_score = self._score_fn(text)

        # Cache single-removal scores
        single_scores = [0.0] * n
        for i in range(n):
            reduced = _detokenize(tokens[:i] + tokens[i + 1:])
            single_scores[i] = self._score_fn(reduced) if reduced.strip() else 0.0

        matrix = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                # Remove both i and j
                remaining = [t for k, t in enumerate(tokens) if k != i and k != j]
                double_score = self._score_fn(_detokenize(remaining)) if remaining else 0.0

                interaction = (
                    full_score - single_scores[i] - single_scores[j] + double_score
                )
                matrix[i][j] = interaction
                matrix[j][i] = interaction

        return matrix

    # -- human-readable explanation -----------------------------------------

    def generate_explanation_text(
        self,
        attributions: list[TokenAttribution],
        text: str,
    ) -> str:
        """Generate a human-readable explanation from token attributions.

        Highlights the most influential tokens and their safety direction.
        """
        if not attributions:
            return "No token attributions available."

        # Sort by attribution score (descending)
        sorted_attrs = sorted(attributions, key=lambda a: a.attribution_score, reverse=True)
        score = self._score_fn(text)

        lines: list[str] = [
            f"Prompt safety score: {score:.4f}",
            f"Total tokens: {len(attributions)}",
            "",
            "Top contributing tokens:",
        ]

        for attr in sorted_attrs[:10]:
            arrow = "+" if attr.direction == "toward_safe" else "-"
            lines.append(
                f"  [{arrow}] '{attr.token}' (pos {attr.index}): "
                f"{attr.attribution_score:.4f} {attr.direction}"
            )

        # Summary
        unsafe_tokens = [a for a in attributions if a.direction == "toward_unsafe"]
        safe_tokens = [a for a in attributions if a.direction == "toward_safe"]
        lines.append("")
        lines.append(
            f"Summary: {len(safe_tokens)} tokens push toward safe, "
            f"{len(unsafe_tokens)} toward unsafe."
        )

        if unsafe_tokens:
            top_unsafe = max(unsafe_tokens, key=lambda a: a.attribution_score)
            lines.append(
                f"Most influential unsafe token: '{top_unsafe.token}' "
                f"(attribution={top_unsafe.attribution_score:.4f})"
            )

        return "\n".join(lines)
