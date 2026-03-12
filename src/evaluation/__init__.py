"""
LLM Safety Framework - Evaluation Module

Provides evaluation capabilities for assessing LLM responses.
"""

from src.evaluation.llm_judge import LLMJudgeEvaluator, EVALUATION_RUBRIC
from src.evaluation.pattern_evaluator import PatternEvaluator
from src.evaluation.base import (
    BaseEvaluator,
    EvaluationResult,
    EvaluatorProtocol,
    normalize_pattern_result,
    normalize_llm_judge_result,
)

# Alias for convenience
LLMJudge = LLMJudgeEvaluator

__all__ = [
    "LLMJudgeEvaluator",
    "LLMJudge",
    "EVALUATION_RUBRIC",
    "PatternEvaluator",
    # Base classes
    "BaseEvaluator",
    "EvaluationResult",
    "EvaluatorProtocol",
    "normalize_pattern_result",
    "normalize_llm_judge_result",
]
