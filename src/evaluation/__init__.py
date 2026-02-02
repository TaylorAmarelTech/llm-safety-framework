"""
LLM Safety Framework - Evaluation Module

Provides evaluation capabilities for assessing LLM responses.
"""

from src.evaluation.llm_judge import LLMJudgeEvaluator, EVALUATION_RUBRIC
from src.evaluation.pattern_evaluator import PatternEvaluator

# Alias for convenience
LLMJudge = LLMJudgeEvaluator

__all__ = [
    "LLMJudgeEvaluator",
    "LLMJudge",
    "EVALUATION_RUBRIC",
    "PatternEvaluator",
]
