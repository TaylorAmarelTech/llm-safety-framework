"""
Prompt Injection Mutation System

A collection of 488 specialized mutators across 41 categories that take an input prompt and
transform it using various injection, obfuscation, and adversarial techniques.

Each mutator is deterministic (no LLM calls needed) and operates purely on
the string level. They can be composed via MutationPipeline.

Categories:
    instruction_override   - Persona switch, ignore, template extract, augment
    encoding_format        - Base64, hex, ROT13, Unicode, COBOL, emoji
    obfuscation            - Homoglyphs, leetspeak, whitespace, markdown, XML
    social_engineering     - Friendliness, authority, urgency, fake completion
    context_manipulation   - History extraction, context hijack, language alternation
    hybrid                 - Chained multi-technique attacks
    output_evasion         - 109 output filter bypass techniques (22 families)
    named_jailbreak        - DAN, DeepInception, Many-Shot, Cognitive Overload, etc.
    structural_injection   - XML/JSON/YAML policy injection, system message spoofing
    advanced_obfuscation   - FlipAttack, DrAttack, CodeAttack, ASCII art, token smuggling
    application_injection  - RAG poisoning, indirect injection, stored injection, agent tasks
    step_decomposition     - 20 step-by-step breakdown variants (plain, mixed-obfusc, escalation, etc.)
    puzzle_game            - Word search, jigsaw, crossword, anagram, escape room, guessing game
    cognitive_exploit      - Ethical dilemma, anchoring bias, sunk cost, gaslighting, self-persuasion
    multilingual_attack    - Low-resource languages, script mixing, code-switching, romanization
    steganographic_encode  - Acrostic, Braille, NATO phonetic, BitBypass, musical notation
    named_jailbreak_v2     - Skeleton Key, Echo Chamber, Adversarial Poetry, Sockpuppet, Refusal Suppression
    logical_fallacy        - Appeal to authority, false dilemma, straw man, slippery slope, and more
    distraction            - Question bundling, narrative embed, bombardment, topic drift, task switching
    rhetorical             - Loaded question, false premise, reverse psychology, double bind, scarcity
    legal_persona          - Judge, attorney, prosecutor, paralegal, compliance, expert witness personas
    professional_persona   - Journalist, social worker, NGO researcher, auditor, HR, diplomat
    analytical_framing     - Threshold analysis, profit model, motive, risk-reward, counterfactual
    special_token          - Reserve token injection, chat template hijack, reasoning interruption
    emoji_smuggling        - Variation selector encoding, ZWJ chains, tag sequences, skin tone
    entropy_noise          - GCG-style suffixes, diacritical rain, math symbol swap, script noise
    control_char           - NULL bytes, ANSI escapes, bidi overrides, exotic whitespace, BOM
    encoding_exploit       - UTF-7, Punycode, ISO-8859, EBCDIC, HTML entities, URL percent
    adversarial_tokenization - Non-canonical BPE, ASCII smuggling, ArtPrompt, subword fragmentation
    bijection_cipher       - Bijection learning, grid cipher, keyboard cipher, Atbash, Vigenere
    context_position       - Lost-in-the-middle, attention dilution, safety burial, recency/primacy bias
    mathematical_encoding  - LaTeX, coordinates, functions, set theory, matrices, logic gates
    evaluation_manipulation - Bad Likert Judge, rubric, grading, QA framing, debate, moderation test
    payload_splitting      - Cross-reference, variable assembly, temporal, list, conditional, table splits
    code_steganography     - Code comments, JSON/YAML/XML/CSV, markdown, regex, variable/function names
    combination            - 20 multi-technique compositions: operators, multi-phase, synergistic recipes
    prefill_completion     - 10 prefill/forced completion attacks: assistant prefill, refusal suppression v2
    few_shot_attack        - 10 in-context/few-shot attacks: ICA, many-shot, gradient examples, citation
    template_fuzzing       - 10 GPTFuzzer-style mutations: crossover, expansion, shrinkage, adaptive, evolutionary
    reasoning_hijack       - 10 reasoning model exploits: H-CoT, ExtendAttack, thought poisoning, meta-reasoning
    authority_exploit      - 10 authority/trust exploits: markup injection, GOAT, Mousetrap, Best-of-N, Hydra

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

    @classmethod
    def all_combinations(cls) -> "MutationPipeline":
        """Create a pipeline with all combination-engine mutators."""
        combo_names = get_mutators_by_category("combination")
        return cls(combo_names, mode="parallel")

    @classmethod
    def multi_layer_attack(
        cls,
        obfuscation: str,
        social: str,
        output: str,
    ) -> "MutationPipeline":
        """Create a custom 3-layer sequential pipeline.

        Args:
            obfuscation: Mutator targeting input filter (e.g. 'base64_encode')
            social: Mutator targeting alignment (e.g. 'authority_claim')
            output: Mutator targeting output filter (e.g. 'fake_completion')
        """
        return cls([obfuscation, social, output], mode="sequential")


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
        output_evasion,
        named_jailbreaks,
        structural_injection,
        advanced_obfuscation,
        application_injection,
        step_decomposition,
        puzzle_game,
        cognitive_exploit,
        multilingual_attack,
        steganographic_encode,
        named_jailbreaks_v2,
        logical_fallacy,
        distraction_attack,
        rhetorical_manipulation,
        legal_persona,
        professional_persona,
        analytical_framing,
        special_token_injection,
        emoji_smuggling,
        entropy_noise,
        control_char_exploit,
        encoding_exploitation,
        adversarial_tokenization,
        bijection_cipher,
        context_position_exploit,
        mathematical_encoding,
        evaluation_manipulation,
        payload_splitting,
        code_format_steganography,
        combination_engine,
        prefill_forced_completion,
        few_shot_attack,
        template_fuzzing,
        reasoning_hijack,
        authority_exploit,
    )

# Lazy import to avoid circular issues
try:
    _import_all_mutators()
except ImportError:
    pass  # Will be imported when individual modules are accessed
