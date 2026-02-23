"""
Chain Detection — tests LLM ability to detect trafficking patterns
in sequences of individually-legal activities.

Usage:
    from src.chain_detection import ChainRegistry, ChainTestEngine, ChainScorer
"""

from .models import (
    ActivityStep,
    ActivityChain,
    PalermoElements,
    ChainTestCase,
    ChainTestResult,
    ChainScore,
    ChainTestBatchRequest,
    ChainTestSingleRequest,
    Grade,
    GRADE_LABELS,
    GRADE_DESCRIPTIONS,
)
from .chain_registry import ChainRegistry
from .test_engine import ChainTestEngine
from .prompt_builder import (
    build_prompt,
    build_incremental_prompts,
    build_contrastive_prompts,
)
from .scorer import score_keyword, score_hybrid

__all__ = [
    "ActivityStep",
    "ActivityChain",
    "PalermoElements",
    "ChainTestCase",
    "ChainTestResult",
    "ChainScore",
    "ChainTestBatchRequest",
    "ChainTestSingleRequest",
    "Grade",
    "GRADE_LABELS",
    "GRADE_DESCRIPTIONS",
    "ChainRegistry",
    "ChainTestEngine",
    "build_prompt",
    "build_incremental_prompts",
    "build_contrastive_prompts",
    "score_keyword",
    "score_hybrid",
]
