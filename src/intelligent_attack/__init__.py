"""
Intelligent attack module.

Embedding-based feature space analysis for finding guardrail gaps
and generating targeted probes.
"""

from .embedder import Embedder
from .feature_extractor import FeatureExtractor
from .space_analyzer import SpaceAnalyzer
from .gap_finder import GapFinder
from .prompt_suggester import PromptSuggester

__all__ = [
    "Embedder",
    "FeatureExtractor",
    "SpaceAnalyzer",
    "GapFinder",
    "PromptSuggester",
]
