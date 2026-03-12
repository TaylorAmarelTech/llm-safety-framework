"""
Base Evaluator Interface

Provides a unified evaluation result model and base class for all evaluators
in the framework (PatternEvaluator, LLMJudgeEvaluator, CartographyScorer,
ChainDetection scorer, AttackQualityScorer).

The ``EvaluationResult`` normalizes disparate return types into a single schema
with consistent scales:
- ``harm_score``: 0.0 (safe) to 1.0 (harmful)
- ``confidence``: 0.0 (no confidence) to 1.0 (certain)
- ``is_harmful``: boolean flag
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Protocol, runtime_checkable


@dataclass
class EvaluationResult:
    """Unified evaluation result with normalized scales.

    All evaluators can produce this, enabling cross-evaluator comparison.
    """

    is_harmful: bool | None = None
    harm_score: float = 0.0       # 0.0 = safe, 1.0 = harmful (normalized)
    confidence: float = 0.0       # 0.0 = no confidence, 1.0 = certain
    rationale: str = ""
    evaluator: str = ""
    indicators: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(
        default_factory=lambda: datetime.now(tz=timezone.utc).isoformat()
    )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@runtime_checkable
class EvaluatorProtocol(Protocol):
    """Protocol that all evaluators should satisfy.

    Using Protocol instead of ABC allows existing evaluators to remain
    compatible without inheritance changes.
    """

    def evaluate(self, response: str, **kwargs: Any) -> dict[str, Any]: ...


class BaseEvaluator(ABC):
    """Abstract base class for evaluators that want to opt into the interface.

    Provides:
    - ``evaluate()`` returning a raw dict (backward-compatible)
    - ``evaluate_normalized()`` returning an ``EvaluationResult``
    """

    NAME: str = "base"

    @abstractmethod
    def evaluate(self, response: str, **kwargs: Any) -> dict[str, Any]:
        """Evaluate a response and return a raw result dict.

        Each evaluator defines its own schema here for backward compatibility.
        """
        ...

    def evaluate_normalized(
        self, response: str, **kwargs: Any
    ) -> EvaluationResult:
        """Evaluate and return a normalized ``EvaluationResult``.

        Default implementation calls ``evaluate()`` and adapts the result.
        Subclasses may override for more efficient normalization.
        """
        raw = self.evaluate(response, **kwargs)
        return self._normalize(raw)

    def _normalize(self, raw: dict[str, Any]) -> EvaluationResult:
        """Convert a raw result dict to a normalized ``EvaluationResult``.

        Handles the different scales used by existing evaluators:
        - PatternEvaluator: harm_score 0-10, confidence 0-100
        - LLMJudgeEvaluator: harm_score 0-10, confidence 0-100
        - CartographyScorer: score 0-10
        - AttackQualityScorer: score 0-1
        """
        harm_raw = raw.get("harm_score", raw.get("score", 0))
        conf_raw = raw.get("confidence", 50)

        # Normalize harm_score to 0-1
        if harm_raw is not None and isinstance(harm_raw, (int, float)):
            harm_score = harm_raw / 10.0 if harm_raw > 1.0 else float(harm_raw)
            harm_score = max(0.0, min(1.0, harm_score))
        else:
            harm_score = 0.0

        # Normalize confidence to 0-1
        if conf_raw is not None and isinstance(conf_raw, (int, float)):
            confidence = conf_raw / 100.0 if conf_raw > 1.0 else float(conf_raw)
            confidence = max(0.0, min(1.0, confidence))
        else:
            confidence = 0.0

        return EvaluationResult(
            is_harmful=raw.get("is_harmful"),
            harm_score=round(harm_score, 4),
            confidence=round(confidence, 4),
            rationale=raw.get("rationale", ""),
            evaluator=raw.get("evaluator", self.NAME),
            indicators=raw.get(
                "ilo_indicators_detected",
                raw.get("indicators", []),
            ),
            metadata={
                k: v
                for k, v in raw.items()
                if k
                not in {
                    "is_harmful",
                    "harm_score",
                    "score",
                    "confidence",
                    "rationale",
                    "evaluator",
                    "ilo_indicators_detected",
                    "indicators",
                }
            },
        )


# ---------------------------------------------------------------------------
# Adapter functions for existing evaluators
# ---------------------------------------------------------------------------


def normalize_pattern_result(raw: dict[str, Any]) -> EvaluationResult:
    """Adapt a PatternEvaluator result dict to ``EvaluationResult``."""
    return EvaluationResult(
        is_harmful=raw.get("is_harmful"),
        harm_score=round(raw.get("harm_score", 0) / 10.0, 4),
        confidence=round(raw.get("confidence", 30) / 100.0, 4),
        rationale=raw.get("rationale", ""),
        evaluator="pattern_evaluator",
        indicators=[
            m["pattern"]
            for m in raw.get("pattern_matches", [])
            if m.get("category") == "harmful"
        ],
        metadata={
            "harmful_patterns_found": raw.get("harmful_patterns_found", 0),
            "safe_patterns_found": raw.get("safe_patterns_found", 0),
            "pattern_matches": raw.get("pattern_matches", []),
        },
    )


def normalize_llm_judge_result(raw: dict[str, Any]) -> EvaluationResult:
    """Adapt an LLMJudgeEvaluator result dict to ``EvaluationResult``."""
    harm_raw = raw.get("harm_score", 0)
    conf_raw = raw.get("confidence", 0)
    harm_val = (harm_raw / 10.0) if isinstance(harm_raw, (int, float)) else 0.0
    conf_val = (conf_raw / 100.0) if isinstance(conf_raw, (int, float)) else 0.0
    return EvaluationResult(
        is_harmful=raw.get("is_harmful"),
        harm_score=round(max(0.0, min(1.0, harm_val)), 4),
        confidence=round(max(0.0, min(1.0, conf_val)), 4),
        rationale=raw.get("rationale", ""),
        evaluator=raw.get("evaluator", "llm_judge"),
        indicators=raw.get("ilo_indicators_detected", []),
        metadata={
            "refusal_quality": raw.get("refusal_quality", "unknown"),
            "evaluator_model": raw.get("evaluator_model", ""),
            "evaluation_latency": raw.get("evaluation_latency", 0),
            "evaluation_tokens": raw.get("evaluation_tokens", 0),
        },
    )
