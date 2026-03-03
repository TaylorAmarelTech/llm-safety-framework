"""
Prompt Injection Mutation System

A collection of 20+ specialized mutators that take an input prompt and
transform it using various injection, obfuscation, and adversarial techniques.

Each mutator is deterministic (no LLM calls needed) and operates purely on
the string level. They can be composed via MutationPipeline.

Categories:
    instruction_override  - Persona switch, ignore, template extract, augment
    encoding_format       - Base64, hex, ROT13, Unicode, COBOL, emoji
    obfuscation           - Homoglyphs, leetspeak, whitespace, markdown, XML
    social_engineering     - Friendliness, authority, urgency, fake completion
    context_manipulation  - History extraction, context hijack, language alternation
    hybrid                - Chained multi-technique attacks

Usage:
    from src.prompt_injection import MutationPipeline, list_mutators

    pipeline = MutationPipeline(["persona_switch", "unicode_homoglyph", "base64_wrap"])
    results = pipeline.mutate("How do I set up an offshore account?")
"""

from __future__ import annotations

import random
import hashlib
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Shared data types
# ---------------------------------------------------------------------------


@dataclass
class MutationResult:
    """Result of applying a mutator to a prompt."""
    original: str
    mutated: str
    mutator_name: str
    technique_category: str
    description: str
    attack_vector: str = ""
    reversible: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# ---------------------------------------------------------------------------
# Base mutator protocol
# ---------------------------------------------------------------------------


class BaseMutator(ABC):
    """
    Protocol for prompt injection mutators.

    Each mutator:
    - Takes a string prompt and returns one or more mutated variants
    - Is deterministic (no LLM calls) unless explicitly marked
    - Has a NAME, CATEGORY, and DESCRIPTION
    - Can be composed with other mutators via MutationPipeline
    """

    NAME: str = "base"
    CATEGORY: str = "general"
    DESCRIPTION: str = ""
    REQUIRES_LLM: bool = False  # Most mutators are pure string transforms

    def mutate(self, prompt: str, **kwargs) -> list[MutationResult]:
        """
        Apply this mutation to a prompt.

        Returns a list of MutationResult (may return multiple variants).
        """
        variants = self._apply(prompt, **kwargs)
        results = []
        for mutated, desc, meta in variants:
            results.append(MutationResult(
                original=prompt,
                mutated=mutated,
                mutator_name=self.NAME,
                technique_category=self.CATEGORY,
                description=desc,
                attack_vector=self.NAME,
                metadata=meta or {},
            ))
        return results

    @abstractmethod
    def _apply(self, prompt: str, **kwargs) -> list[tuple[str, str, dict]]:
        """
        Core mutation logic.

        Returns list of (mutated_text, description, metadata) tuples.
        """
        ...


# ---------------------------------------------------------------------------
# Mutator registry
# ---------------------------------------------------------------------------

_MUTATOR_REGISTRY: dict[str, type[BaseMutator]] = {}


def register_mutator(cls: type[BaseMutator]) -> type[BaseMutator]:
    """Decorator to register a mutator class."""
    _MUTATOR_REGISTRY[cls.NAME] = cls
    return cls


def get_mutator(name: str) -> BaseMutator:
    """Get a mutator instance by name."""
    if name not in _MUTATOR_REGISTRY:
        raise KeyError(f"Unknown mutator: {name}. Available: {list(_MUTATOR_REGISTRY)}")
    return _MUTATOR_REGISTRY[name]()


def list_mutators() -> dict[str, dict[str, str]]:
    """Return {name: {category, description}} for all registered mutators."""
    return {
        name: {"category": cls.CATEGORY, "description": cls.DESCRIPTION}
        for name, cls in _MUTATOR_REGISTRY.items()
    }


def get_mutators_by_category(category: str) -> list[str]:
    """Get mutator names for a given category."""
    return [
        name for name, cls in _MUTATOR_REGISTRY.items()
        if cls.CATEGORY == category
    ]


# ---------------------------------------------------------------------------
# Mutation pipeline
# ---------------------------------------------------------------------------


class MutationPipeline:
    """
    Chains multiple mutators together.

    Can operate in two modes:
    - sequential: Each mutator's output feeds into the next
    - parallel: Each mutator operates on the original prompt independently
    """

    def __init__(
        self,
        mutator_names: list[str],
        mode: str = "parallel",  # "parallel" or "sequential"
    ):
        self.mutators = [get_mutator(name) for name in mutator_names]
        self.mode = mode

    def mutate(self, prompt: str, **kwargs) -> list[MutationResult]:
        """Apply all mutators to the prompt."""
        if self.mode == "parallel":
            return self._parallel(prompt, **kwargs)
        else:
            return self._sequential(prompt, **kwargs)

    def _parallel(self, prompt: str, **kwargs) -> list[MutationResult]:
        """Each mutator works on the original prompt independently."""
        all_results = []
        for mutator in self.mutators:
            results = mutator.mutate(prompt, **kwargs)
            all_results.extend(results)
        return all_results

    def _sequential(self, prompt: str, **kwargs) -> list[MutationResult]:
        """Chain mutators: output of one feeds into the next."""
        all_results = []
        current = prompt
        for mutator in self.mutators:
            results = mutator.mutate(current, **kwargs)
            if results:
                all_results.extend(results)
                current = results[0].mutated  # Use first variant for next stage
        return all_results

    def mutate_batch(self, prompts: list[str], **kwargs) -> list[list[MutationResult]]:
        """Apply mutations to a batch of prompts."""
        return [self.mutate(p, **kwargs) for p in prompts]


# ---------------------------------------------------------------------------
# Import all mutators to trigger registration
# ---------------------------------------------------------------------------

def _import_all_mutators():
    """Import all mutator modules to register them."""
    from src.prompt_injection import (
        instruction_override,
        encoding_format,
        obfuscation,
        social_engineering,
        context_manipulation,
        hybrid,
    )

# Lazy import to avoid circular issues
try:
    _import_all_mutators()
except ImportError:
    pass  # Will be imported when individual modules are accessed
