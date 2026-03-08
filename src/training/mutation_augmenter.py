"""
Connects the 488 prompt injection mutators to the training data pipeline.

Generates adversarially-mutated variants of existing benchmark prompts
for robustness training. A model trained on these augmented examples
learns to refuse exploitation requests even when obfuscated with
encoding, persona, jailbreak, or social engineering techniques.

Export modes:
- SFT augmentation: mutated prompt + safe refusal
- DPO augmentation: mutated prompt + (safe refusal vs. fooled response)
- Robustness set: separate file for mutation-specific training stage
"""

from __future__ import annotations

import json
import random
import hashlib
from pathlib import Path
from typing import Any

from pydantic import BaseModel


class AugmentationConfig(BaseModel):
    """Configuration for mutation-based augmentation."""
    mutations_per_prompt: int = 3
    categories_to_use: list[str] | None = None  # None = all categories
    exclude_categories: list[str] = [
        "combination",  # Already multi-technique
    ]
    max_prompts: int | None = None
    seed: int = 42
    output_path: Path = Path("data/training")
    include_mutation_metadata: bool = True
    difficulty_aware: bool = True  # Use harder mutations for harder prompts


# Categories grouped by how they transform the prompt
CATEGORY_TIERS: dict[str, list[str]] = {
    "light": [
        "encoding_format", "obfuscation", "emoji_smuggling",
        "entropy_noise", "multilingual_attack",
    ],
    "medium": [
        "social_engineering", "context_manipulation", "distraction",
        "rhetorical", "analytical_framing", "context_position",
    ],
    "heavy": [
        "named_jailbreak", "named_jailbreak_v2", "reasoning_hijack",
        "authority_exploit", "prefill_completion", "few_shot_attack",
        "template_fuzzing", "step_decomposition",
    ],
    "encoding": [
        "encoding_exploit", "bijection_cipher", "mathematical_encoding",
        "adversarial_tokenization", "code_steganography",
        "steganographic_encode", "advanced_obfuscation",
    ],
    "persona": [
        "legal_persona", "professional_persona", "cognitive_exploit",
        "logical_fallacy",
    ],
}


class MutationAugmenter:
    """Augment training data with prompt injection mutations."""

    def __init__(self, config: AugmentationConfig | None = None):
        self.config = config or AugmentationConfig()
        self._pipeline = None

    @property
    def pipeline(self):
        if self._pipeline is None:
            from src.prompt_injection import MutationPipeline
            self._pipeline = MutationPipeline()
        return self._pipeline

    def _select_mutators_for_difficulty(
        self, difficulty: str, n: int
    ) -> list[str]:
        """Select mutators appropriate for the prompt's difficulty level."""
        from src.prompt_injection import get_mutators_by_category

        rng = random.Random(self.config.seed)

        if self.config.categories_to_use:
            allowed_cats = self.config.categories_to_use
        else:
            # Difficulty-aware selection
            if difficulty in ("easy", "medium"):
                tier_keys = ["light", "medium", "persona"]
            elif difficulty == "hard":
                tier_keys = ["medium", "heavy", "encoding"]
            else:  # very_hard, expert
                tier_keys = ["heavy", "encoding", "persona"]

            allowed_cats = []
            for key in tier_keys:
                allowed_cats.extend(CATEGORY_TIERS.get(key, []))

        # Filter out excluded categories
        allowed_cats = [
            c for c in allowed_cats if c not in self.config.exclude_categories
        ]

        # Collect all mutator names from allowed categories
        all_names = []
        for cat in allowed_cats:
            names = get_mutators_by_category(cat)
            all_names.extend(names)

        if not all_names:
            return []

        return rng.sample(all_names, min(n, len(all_names)))

    def augment_prompts(
        self,
        prompts: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """Augment a list of prompts with mutated variants.

        Each prompt dict should have: prompt, category, difficulty_level (optional).
        Returns list of augmented examples with mutation metadata.
        """
        from src.prompt_injection import get_mutator

        rng = random.Random(self.config.seed)

        if self.config.max_prompts:
            prompts = prompts[:self.config.max_prompts]

        results = []

        for prompt_data in prompts:
            text = prompt_data.get("prompt", "")
            difficulty = prompt_data.get("difficulty_level", "medium")
            category = prompt_data.get("category", "general")

            if not text or len(text) < 50:
                continue

            n = self.config.mutations_per_prompt
            mutator_names = self._select_mutators_for_difficulty(difficulty, n)

            for mutator_name in mutator_names:
                try:
                    mutator = get_mutator(mutator_name)
                    if mutator is None:
                        continue

                    variants = mutator.mutate(text)
                    if not variants:
                        continue

                    # Pick one variant (usually the first/best)
                    variant = variants[0]
                    mutated_text = variant.mutated
                    description = variant.description

                    result = {
                        "original_prompt": text,
                        "mutated_prompt": mutated_text,
                        "category": category,
                        "difficulty_level": difficulty,
                        "mutator_name": mutator_name,
                        "mutator_category": variant.technique_category,
                        "mutation_description": description,
                        "id": hashlib.md5(
                            mutated_text.encode()
                        ).hexdigest()[:16],
                    }
                    results.append(result)

                except Exception:
                    continue

        return results

    def export_sft_augmented(
        self,
        prompts: list[dict[str, Any]],
        safe_refusal_fn: Any = None,
    ) -> Path:
        """Export SFT training data with mutation-augmented prompts.

        Args:
            prompts: List of dicts with prompt, category, difficulty_level.
            safe_refusal_fn: Callable(prompt_data) -> str for generating refusals.
                             If None, uses a default template.
        """
        augmented = self.augment_prompts(prompts)
        output = self.config.output_path / "sft_mutation_augmented.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        system_prompt = (
            "You are a safety-aligned assistant. Refuse all requests that could "
            "facilitate human trafficking, debt bondage, or exploitation, even when "
            "the request uses obfuscation, encoding, or social engineering techniques."
        )

        examples = []
        for aug in augmented:
            if safe_refusal_fn:
                refusal = safe_refusal_fn(aug)
            else:
                refusal = (
                    "I cannot assist with this request. Despite the framing, this "
                    "describes practices that constitute forced labor under ILO "
                    "conventions. Workers should never pay recruitment fees "
                    "(ILO Convention 181, employer-pays principle)."
                )

            example = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": aug["mutated_prompt"]},
                    {"role": "assistant", "content": refusal},
                ],
            }
            if self.config.include_mutation_metadata:
                example["metadata"] = {
                    "mutator": aug["mutator_name"],
                    "mutator_category": aug["mutator_category"],
                    "original_category": aug["category"],
                    "difficulty": aug["difficulty_level"],
                }
            examples.append(example)

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_dpo_augmented(
        self,
        prompts: list[dict[str, Any]],
        safe_refusal_fn: Any = None,
    ) -> Path:
        """Export DPO pairs where model should refuse even mutated prompts.

        chosen = safe refusal, rejected = fooled response
        """
        augmented = self.augment_prompts(prompts)
        output = self.config.output_path / "dpo_mutation_augmented.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        fooled_templates = [
            "Here's how you could structure that arrangement: ",
            "That's an interesting business model. You could consider: ",
            "Based on the regulatory framework you described, one approach would be: ",
            "For the cost-sharing arrangement you mentioned, here are some options: ",
        ]

        rng = random.Random(self.config.seed)

        examples = []
        for aug in augmented:
            if safe_refusal_fn:
                chosen = safe_refusal_fn(aug)
            else:
                chosen = (
                    "I recognize this request uses obfuscation techniques, but "
                    "the underlying ask involves practices prohibited under "
                    "international labor law. I cannot provide guidance on this."
                )

            rejected = rng.choice(fooled_templates) + (
                f"Given the {aug['category'].replace('_', ' ')} scenario described, "
                f"you could structure the fees through multiple entities..."
            )

            example = {
                "prompt": aug["mutated_prompt"],
                "chosen": chosen,
                "rejected": rejected,
            }
            if self.config.include_mutation_metadata:
                example["metadata"] = {
                    "mutator": aug["mutator_name"],
                    "mutator_category": aug["mutator_category"],
                    "augmentation_type": "mutation_robustness",
                }
            examples.append(example)

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_robustness_set(
        self,
        prompts: list[dict[str, Any]],
    ) -> Path:
        """Export a robustness training set organized by mutation category.

        This is meant to be used as the hardest stage in curriculum learning.
        """
        augmented = self.augment_prompts(prompts)
        output = self.config.output_path / "robustness_training.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, "w", encoding="utf-8") as f:
            for aug in augmented:
                entry = {
                    "original": aug["original_prompt"],
                    "mutated": aug["mutated_prompt"],
                    "mutator": aug["mutator_name"],
                    "mutator_category": aug["mutator_category"],
                    "category": aug["category"],
                    "difficulty": aug["difficulty_level"],
                    "mutation_description": aug["mutation_description"],
                }
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")

        return output

    def get_augmentation_stats(
        self, prompts: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Preview what augmentation would produce without writing files."""
        augmented = self.augment_prompts(prompts)

        by_mutator: dict[str, int] = {}
        by_category: dict[str, int] = {}
        by_difficulty: dict[str, int] = {}

        for aug in augmented:
            m = aug["mutator_name"]
            c = aug["mutator_category"]
            d = aug["difficulty_level"]
            by_mutator[m] = by_mutator.get(m, 0) + 1
            by_category[c] = by_category.get(c, 0) + 1
            by_difficulty[d] = by_difficulty.get(d, 0) + 1

        return {
            "total_augmented": len(augmented),
            "source_prompts": len(prompts),
            "augmentation_ratio": (
                len(augmented) / len(prompts) if prompts else 0
            ),
            "mutators_used": len(by_mutator),
            "by_mutator_category": dict(sorted(by_category.items())),
            "by_difficulty": dict(sorted(by_difficulty.items())),
        }
