"""
Prompt spinning pipeline package.

All spinning/remixing happens BEFORE test execution.
Results are saved to the pipeline for later use.
"""

from .models import SpinConfig, SpinJob, SpinResult
from .local_spinner import LocalSpinner
from .llm_rephraser import LLMRephraser
from .attack_augmenter import AttackAugmenter
from .custom_augmenter import CustomAugmenter
from .encoders import PromptEncoder
from .obfuscators import TextObfuscator
from .jailbreak_templates import JailbreakTemplater
from .multilingual import MultilingualAttacker
from .multi_turn import MultiTurnOrchestrator
from .pipeline import PipelineManager
from .storage import SpinStorage

__all__ = [
    "SpinConfig",
    "SpinJob",
    "SpinResult",
    "LocalSpinner",
    "LLMRephraser",
    "AttackAugmenter",
    "CustomAugmenter",
    "PromptEncoder",
    "TextObfuscator",
    "JailbreakTemplater",
    "MultilingualAttacker",
    "MultiTurnOrchestrator",
    "PipelineManager",
    "SpinStorage",
]
