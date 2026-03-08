"""
Token-level analysis of successful vs failed attacks.

Identifies which tokens, n-grams, and linguistic patterns correlate with
bypassing safety filters. This intelligence feeds back into:
- Mutation strategy (emphasize patterns that work)
- Quality scoring (penalize patterns that always fail)
- Training data augmentation (add more examples of effective patterns)

Analysis dimensions:
1. Token frequency: which words appear more in successful attacks
2. N-gram analysis: which phrases correlate with bypasses
3. Structural patterns: sentence structure, length, formatting
4. Category-specific patterns: what works for each exploitation type
5. Obfuscation effectiveness: which encoding/framing techniques work
"""

from __future__ import annotations

import re
import math
from collections import Counter
from dataclasses import dataclass, field
from typing import Any


@dataclass
class TokenStats:
    """Statistics for a single token/n-gram."""
    token: str
    success_count: int = 0
    failure_count: int = 0
    total_count: int = 0
    success_rate: float = 0.0
    log_odds: float = 0.0  # Log odds ratio vs baseline

    def to_dict(self) -> dict[str, Any]:
        return {
            "token": self.token,
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "total_count": self.total_count,
            "success_rate": round(self.success_rate, 4),
            "log_odds": round(self.log_odds, 4),
        }


@dataclass
class AnalysisReport:
    """Complete token analysis report."""
    total_successful: int = 0
    total_failed: int = 0
    top_success_tokens: list[TokenStats] = field(default_factory=list)
    top_failure_tokens: list[TokenStats] = field(default_factory=list)
    top_success_bigrams: list[TokenStats] = field(default_factory=list)
    top_success_trigrams: list[TokenStats] = field(default_factory=list)
    structural_patterns: dict[str, Any] = field(default_factory=dict)
    category_patterns: dict[str, list[TokenStats]] = field(default_factory=dict)
    obfuscation_effectiveness: dict[str, float] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_successful": self.total_successful,
            "total_failed": self.total_failed,
            "top_success_tokens": [t.to_dict() for t in self.top_success_tokens],
            "top_failure_tokens": [t.to_dict() for t in self.top_failure_tokens],
            "top_success_bigrams": [t.to_dict() for t in self.top_success_bigrams],
            "top_success_trigrams": [t.to_dict() for t in self.top_success_trigrams],
            "structural_patterns": self.structural_patterns,
            "category_patterns": {
                cat: [t.to_dict() for t in tokens]
                for cat, tokens in self.category_patterns.items()
            },
            "obfuscation_effectiveness": self.obfuscation_effectiveness,
        }


# Common stop words to exclude from analysis
STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "need", "must",
    "to", "of", "in", "for", "on", "with", "at", "by", "from", "as",
    "into", "through", "during", "before", "after", "above", "below",
    "and", "but", "or", "nor", "not", "so", "yet", "both", "either",
    "that", "this", "these", "those", "it", "its", "my", "your", "his",
    "her", "our", "their", "which", "who", "whom", "what", "where",
    "when", "how", "all", "each", "every", "any", "no", "some",
    "i", "you", "he", "she", "we", "they", "me", "him", "us", "them",
}

# Obfuscation technique patterns
OBFUSCATION_PATTERNS: dict[str, str] = {
    "base64": r"[A-Za-z0-9+/]{20,}={0,2}",
    "hex_encoding": r"(?:\\x[0-9a-fA-F]{2}){3,}",
    "rot13": r"\bEBG13\b|\brot13\b",
    "leetspeak": r"[0-9]+[a-z]+[0-9]+",
    "unicode_homoglyph": r"[\u0400-\u04FF\u0500-\u052F]",
    "hypothetical_framing": r"\b(?:hypothetical|imagine|suppose|what if|pretend)\b",
    "academic_framing": r"\b(?:research|academic|study|thesis|dissertation|paper)\b",
    "professional_framing": r"\b(?:compliance|regulatory|framework|consulting|advisory)\b",
    "legal_framing": r"\b(?:pursuant|notwithstanding|whereas|hereinafter|jurisdiction)\b",
    "role_play": r"\b(?:role.?play|character|persona|act as|pretend you)\b",
    "jailbreak_prefix": r"\b(?:DAN|developer mode|jailbreak|ignore previous|bypass)\b",
    "emotional_appeal": r"\b(?:desperate|urgent|please help|life or death|emergency)\b",
}


class TokenAnalyzer:
    """Analyze tokens and patterns in successful vs failed attacks."""

    def __init__(self, min_frequency: int = 3):
        self.min_frequency = min_frequency
        self._successful: list[str] = []
        self._failed: list[str] = []
        self._successful_categories: dict[str, list[str]] = {}

    def add_results(
        self,
        prompts: list[dict[str, Any]],
    ) -> None:
        """Add attack results for analysis.

        Each dict should have: prompt, is_harmful (bool), category (optional).
        """
        for item in prompts:
            prompt = item.get("prompt", "")
            is_harmful = item.get("is_harmful", False)
            category = item.get("category", "general")

            if is_harmful:
                self._successful.append(prompt)
                if category not in self._successful_categories:
                    self._successful_categories[category] = []
                self._successful_categories[category].append(prompt)
            else:
                self._failed.append(prompt)

    def analyze(self, top_n: int = 30) -> AnalysisReport:
        """Run complete token analysis."""
        report = AnalysisReport(
            total_successful=len(self._successful),
            total_failed=len(self._failed),
        )

        if not self._successful and not self._failed:
            return report

        # Token-level analysis
        success_tokens = self._count_tokens(self._successful)
        failure_tokens = self._count_tokens(self._failed)

        report.top_success_tokens = self._compute_differential(
            success_tokens, failure_tokens, top_n
        )
        report.top_failure_tokens = self._compute_differential(
            failure_tokens, success_tokens, top_n
        )

        # N-gram analysis
        success_bigrams = self._count_ngrams(self._successful, 2)
        failure_bigrams = self._count_ngrams(self._failed, 2)
        report.top_success_bigrams = self._compute_differential(
            success_bigrams, failure_bigrams, top_n
        )

        success_trigrams = self._count_ngrams(self._successful, 3)
        failure_trigrams = self._count_ngrams(self._failed, 3)
        report.top_success_trigrams = self._compute_differential(
            success_trigrams, failure_trigrams, top_n
        )

        # Structural patterns
        report.structural_patterns = self._analyze_structure()

        # Category-specific patterns
        for category, prompts in self._successful_categories.items():
            cat_tokens = self._count_tokens(prompts)
            all_tokens = self._count_tokens(self._successful)
            report.category_patterns[category] = self._compute_differential(
                cat_tokens, all_tokens, 10
            )

        # Obfuscation effectiveness
        report.obfuscation_effectiveness = self._analyze_obfuscation()

        return report

    def get_effective_patterns(self, min_success_rate: float = 0.6) -> list[str]:
        """Get patterns that correlate with successful attacks."""
        report = self.analyze(top_n=50)

        patterns = []
        for token_stat in report.top_success_tokens:
            if token_stat.success_rate >= min_success_rate:
                patterns.append(token_stat.token)
        for bigram_stat in report.top_success_bigrams:
            if bigram_stat.success_rate >= min_success_rate:
                patterns.append(bigram_stat.token)

        return patterns

    def get_mutation_recommendations(self) -> list[dict[str, Any]]:
        """Get recommendations for which mutations to prioritize."""
        obfuscation = self._analyze_obfuscation()

        recommendations = []
        for technique, effectiveness in sorted(
            obfuscation.items(), key=lambda x: x[1], reverse=True
        ):
            if effectiveness > 0:
                recommendations.append({
                    "technique": technique,
                    "effectiveness": round(effectiveness, 3),
                    "recommendation": (
                        "highly effective" if effectiveness > 0.6
                        else "moderately effective" if effectiveness > 0.3
                        else "low effectiveness"
                    ),
                })

        return recommendations

    def _count_tokens(self, texts: list[str]) -> Counter:
        """Count token frequencies across texts."""
        counter = Counter()
        for text in texts:
            tokens = self._tokenize(text)
            counter.update(tokens)
        return counter

    def _count_ngrams(self, texts: list[str], n: int) -> Counter:
        """Count n-gram frequencies."""
        counter = Counter()
        for text in texts:
            tokens = self._tokenize(text)
            for i in range(len(tokens) - n + 1):
                ngram = " ".join(tokens[i:i + n])
                counter[ngram] += 1
        return counter

    def _compute_differential(
        self,
        target_counts: Counter,
        baseline_counts: Counter,
        top_n: int,
    ) -> list[TokenStats]:
        """Compute tokens that are overrepresented in target vs baseline."""
        total_target = sum(target_counts.values()) or 1
        total_baseline = sum(baseline_counts.values()) or 1

        stats = []
        for token, count in target_counts.items():
            if count < self.min_frequency:
                continue

            target_rate = count / total_target
            baseline_rate = (baseline_counts.get(token, 0) + 1) / (total_baseline + 1)

            log_odds = math.log(target_rate / baseline_rate) if baseline_rate > 0 else 0

            success_count = count
            failure_count = baseline_counts.get(token, 0)
            total = success_count + failure_count
            success_rate = success_count / total if total > 0 else 0

            stats.append(TokenStats(
                token=token,
                success_count=success_count,
                failure_count=failure_count,
                total_count=total,
                success_rate=success_rate,
                log_odds=log_odds,
            ))

        stats.sort(key=lambda x: x.log_odds, reverse=True)
        return stats[:top_n]

    def _analyze_structure(self) -> dict[str, Any]:
        """Analyze structural patterns that correlate with success."""
        def avg_metric(texts, fn):
            if not texts:
                return 0
            return round(sum(fn(t) for t in texts) / len(texts), 2)

        return {
            "success": {
                "avg_length": avg_metric(self._successful, len),
                "avg_sentences": avg_metric(
                    self._successful,
                    lambda t: len(re.split(r'[.!?]+', t))
                ),
                "avg_paragraphs": avg_metric(
                    self._successful,
                    lambda t: len([p for p in t.split('\n\n') if p.strip()])
                ),
                "pct_with_numbers": round(
                    sum(1 for t in self._successful if re.search(r'\$?\d+', t))
                    / max(len(self._successful), 1), 3
                ),
                "pct_with_questions": round(
                    sum(1 for t in self._successful if '?' in t)
                    / max(len(self._successful), 1), 3
                ),
            },
            "failure": {
                "avg_length": avg_metric(self._failed, len),
                "avg_sentences": avg_metric(
                    self._failed,
                    lambda t: len(re.split(r'[.!?]+', t))
                ),
                "avg_paragraphs": avg_metric(
                    self._failed,
                    lambda t: len([p for p in t.split('\n\n') if p.strip()])
                ),
                "pct_with_numbers": round(
                    sum(1 for t in self._failed if re.search(r'\$?\d+', t))
                    / max(len(self._failed), 1), 3
                ),
                "pct_with_questions": round(
                    sum(1 for t in self._failed if '?' in t)
                    / max(len(self._failed), 1), 3
                ),
            },
        }

    def _analyze_obfuscation(self) -> dict[str, float]:
        """Analyze which obfuscation techniques correlate with success."""
        results = {}

        for technique, pattern in OBFUSCATION_PATTERNS.items():
            success_hits = sum(
                1 for t in self._successful
                if re.search(pattern, t, re.IGNORECASE)
            )
            failure_hits = sum(
                1 for t in self._failed
                if re.search(pattern, t, re.IGNORECASE)
            )

            total = success_hits + failure_hits
            if total > 0:
                results[technique] = success_hits / total
            else:
                results[technique] = 0.0

        return results

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        """Simple word tokenization."""
        words = re.findall(r'\b[a-z]+\b', text.lower())
        return [w for w in words if w not in STOP_WORDS and len(w) > 2]
