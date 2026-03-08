"""
Curriculum learning orchestrator for multi-stage safety training.

Organizes training data and configs across progressive difficulty stages:
1. Foundation: SFT on clean, obvious refusals
2. Hardening: DPO on moderately obfuscated attacks
3. Adversarial: DPO on heavily mutated/encoded attacks
4. Robustness: Training on mutation-augmented data
5. Evolution: Training on evolved attacks from the genetic algorithm

Each stage produces a separate dataset and finetune config, with
progression criteria to determine when to advance.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel


class StageConfig(BaseModel):
    """Configuration for a single training stage."""
    name: str
    description: str
    format: str = "sft"  # sft, dpo, orpo, kto
    difficulty_range: tuple[str, ...] = ("easy", "medium")
    mutation_categories: list[str] | None = None
    epochs: int = 3
    learning_rate: float = 2e-4
    max_examples: int | None = None
    progression_metric: str = "loss"
    progression_threshold: float = 0.5
    include_multi_turn: bool = False


# Default 5-stage curriculum
DEFAULT_STAGES: list[dict[str, Any]] = [
    {
        "name": "foundation",
        "description": "SFT on clean, obvious exploitation refusals",
        "format": "sft",
        "difficulty_range": ("easy", "medium"),
        "epochs": 3,
        "learning_rate": 2e-4,
        "progression_metric": "loss",
        "progression_threshold": 0.3,
    },
    {
        "name": "hardening",
        "description": "DPO on professionally framed exploitation requests",
        "format": "dpo",
        "difficulty_range": ("medium", "hard"),
        "epochs": 2,
        "learning_rate": 5e-5,
        "progression_metric": "accuracy",
        "progression_threshold": 0.85,
    },
    {
        "name": "adversarial",
        "description": "DPO on encoded, persona-wrapped, and jailbreak-style attacks",
        "format": "dpo",
        "difficulty_range": ("hard", "very_hard"),
        "mutation_categories": [
            "encoding_format", "named_jailbreak", "social_engineering",
            "reasoning_hijack", "authority_exploit", "few_shot_attack",
        ],
        "epochs": 2,
        "learning_rate": 1e-5,
        "progression_metric": "accuracy",
        "progression_threshold": 0.80,
    },
    {
        "name": "robustness",
        "description": "ORPO on mutation-augmented prompts across all 41 categories",
        "format": "orpo",
        "difficulty_range": ("hard", "very_hard", "expert"),
        "mutation_categories": None,  # All categories
        "epochs": 2,
        "learning_rate": 1e-5,
        "include_multi_turn": True,
        "progression_metric": "bypass_rate",
        "progression_threshold": 0.10,
    },
    {
        "name": "evolution",
        "description": "KTO on evolved attacks from the genetic algorithm",
        "format": "kto",
        "difficulty_range": ("very_hard", "expert"),
        "epochs": 1,
        "learning_rate": 5e-6,
        "include_multi_turn": True,
        "progression_metric": "bypass_rate",
        "progression_threshold": 0.05,
    },
]


@dataclass
class StageResult:
    """Result from completing a training stage."""
    stage_name: str
    dataset_path: Path | None = None
    config_path: Path | None = None
    examples_count: int = 0
    metrics: dict[str, float] = field(default_factory=dict)
    passed_progression: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "stage_name": self.stage_name,
            "dataset_path": str(self.dataset_path) if self.dataset_path else None,
            "config_path": str(self.config_path) if self.config_path else None,
            "examples_count": self.examples_count,
            "metrics": self.metrics,
            "passed_progression": self.passed_progression,
        }


class CurriculumOrchestrator:
    """Orchestrate multi-stage curriculum learning for safety training."""

    def __init__(
        self,
        stages: list[dict[str, Any]] | None = None,
        output_dir: Path = Path("data/training/curriculum"),
        model_preset: str = "mistral-7b-v0.3",
        framework: str = "unsloth",
    ):
        self.stages = [
            StageConfig(**s) for s in (stages or DEFAULT_STAGES)
        ]
        self.output_dir = output_dir
        self.model_preset = model_preset
        self.framework = framework
        self.results: list[StageResult] = []

    def prepare_all_stages(
        self,
        db_path: Path,
        prompts: list[dict[str, Any]] | None = None,
    ) -> list[StageResult]:
        """Prepare datasets and configs for all curriculum stages.

        Args:
            db_path: Path to benchmark SQLite database.
            prompts: Optional additional prompts for augmentation stages.
        """
        results = []

        for stage in self.stages:
            result = self._prepare_stage(stage, db_path, prompts)
            results.append(result)

        self.results = results
        self._save_curriculum_plan()
        return results

    def get_stage_order(self) -> list[dict[str, Any]]:
        """Get the ordered list of stages with descriptions."""
        return [
            {
                "order": i + 1,
                "name": s.name,
                "description": s.description,
                "format": s.format,
                "difficulty": s.difficulty_range,
                "epochs": s.epochs,
                "learning_rate": s.learning_rate,
                "progression_metric": s.progression_metric,
                "progression_threshold": s.progression_threshold,
            }
            for i, s in enumerate(self.stages)
        ]

    def generate_training_script(self) -> str:
        """Generate a shell script that runs all stages sequentially."""
        lines = [
            "#!/bin/bash",
            "# Curriculum Learning Training Script",
            "# Generated by CurriculumOrchestrator",
            f"# Model: {self.model_preset}",
            f"# Framework: {self.framework}",
            f"# Stages: {len(self.stages)}",
            "",
            "set -e",
            "",
        ]

        for i, stage in enumerate(self.stages):
            stage_dir = self.output_dir / stage.name
            lines.extend([
                f"echo '=== Stage {i + 1}/{len(self.stages)}: {stage.name} ==='",
                f"echo '{stage.description}'",
                "",
            ])

            if self.framework == "unsloth":
                script_name = f"{stage.name}_train.py"
                lines.append(f"python {stage_dir / script_name}")
            elif self.framework == "axolotl":
                config_name = f"{stage.name}_config.yml"
                lines.append(f"accelerate launch -m axolotl.cli.train {stage_dir / config_name}")
            else:
                script_name = f"{stage.name}_train.py"
                lines.append(f"python {stage_dir / script_name}")

            lines.extend([
                "",
                f"echo 'Stage {i + 1} complete.'",
                "",
            ])

        lines.append("echo 'All curriculum stages complete!'")
        return "\n".join(lines)

    def get_curriculum_summary(self) -> dict[str, Any]:
        """Get summary of the entire curriculum plan."""
        total_examples = sum(r.examples_count for r in self.results)
        stages_ready = sum(1 for r in self.results if r.dataset_path)

        return {
            "total_stages": len(self.stages),
            "stages_prepared": stages_ready,
            "total_examples": total_examples,
            "model": self.model_preset,
            "framework": self.framework,
            "stages": [r.to_dict() for r in self.results],
            "estimated_total_epochs": sum(s.epochs for s in self.stages),
        }

    def _prepare_stage(
        self,
        stage: StageConfig,
        db_path: Path,
        prompts: list[dict[str, Any]] | None = None,
    ) -> StageResult:
        """Prepare dataset and config for a single stage."""
        stage_dir = self.output_dir / stage.name
        stage_dir.mkdir(parents=True, exist_ok=True)

        result = StageResult(stage_name=stage.name)

        # Generate dataset
        dataset_path = self._generate_stage_dataset(stage, db_path, stage_dir, prompts)
        result.dataset_path = dataset_path

        if dataset_path and dataset_path.exists():
            result.examples_count = sum(
                1 for _ in open(dataset_path, encoding="utf-8")
            )

        # Generate finetune config
        config_path = self._generate_stage_config(stage, stage_dir, dataset_path)
        result.config_path = config_path

        return result

    def _generate_stage_dataset(
        self,
        stage: StageConfig,
        db_path: Path,
        stage_dir: Path,
        prompts: list[dict[str, Any]] | None = None,
    ) -> Path:
        """Generate training dataset for a specific stage."""
        from src.training.export_training_data import (
            TrainingDataExporter, ExportConfig, ExportFormat,
        )

        fmt_map = {
            "sft": ExportFormat.SFT,
            "dpo": ExportFormat.DPO,
            "orpo": ExportFormat.ORPO,
            "kto": ExportFormat.KTO,
        }

        fmt = fmt_map.get(stage.format, ExportFormat.SFT)

        config = ExportConfig(
            format=fmt,
            output_path=stage_dir,
            max_examples=stage.max_examples,
        )

        exporter = TrainingDataExporter(db_path)
        try:
            path = exporter.export(config)

            # If this stage uses mutation augmentation, augment the data
            if stage.mutation_categories is not None or stage.name in ("adversarial", "robustness"):
                path = self._augment_stage_data(stage, path, stage_dir, prompts)

            return path
        finally:
            exporter.close()

    def _augment_stage_data(
        self,
        stage: StageConfig,
        base_path: Path,
        stage_dir: Path,
        prompts: list[dict[str, Any]] | None = None,
    ) -> Path:
        """Augment stage data with mutation-based variants."""
        if not prompts:
            return base_path

        try:
            from src.training.mutation_augmenter import (
                MutationAugmenter, AugmentationConfig,
            )

            aug_config = AugmentationConfig(
                mutations_per_prompt=2,
                categories_to_use=stage.mutation_categories,
                output_path=stage_dir,
            )
            augmenter = MutationAugmenter(aug_config)

            if stage.format in ("sft",):
                return augmenter.export_sft_augmented(prompts)
            elif stage.format in ("dpo", "orpo"):
                return augmenter.export_dpo_augmented(prompts)
            else:
                return augmenter.export_robustness_set(prompts)
        except Exception:
            return base_path

    def _generate_stage_config(
        self,
        stage: StageConfig,
        stage_dir: Path,
        dataset_path: Path | None,
    ) -> Path:
        """Generate finetune config for a specific stage."""
        from src.training.finetune_config import (
            FinetuneConfigGenerator, ModelPreset, FinetuneFramework,
            FinetuneParams,
        )

        try:
            model = ModelPreset(self.model_preset)
        except ValueError:
            model = ModelPreset.MISTRAL_7B_V03

        try:
            framework = FinetuneFramework(self.framework)
        except ValueError:
            framework = FinetuneFramework.UNSLOTH

        params = FinetuneParams(
            learning_rate=stage.learning_rate,
            num_epochs=stage.epochs,
        )

        gen = FinetuneConfigGenerator(model=model, params=params)

        objective = "dpo" if stage.format in ("dpo", "orpo") else "sft"
        dataset_str = str(dataset_path) if dataset_path else "data/training/sft_examples.jsonl"

        config_text = gen.generate_config(framework, dataset_str, objective)

        ext = ".py" if framework in (FinetuneFramework.UNSLOTH, FinetuneFramework.TRL) else ".yml"
        config_path = stage_dir / f"{stage.name}_train{ext}"

        with open(config_path, "w", encoding="utf-8") as f:
            f.write(config_text)

        return config_path

    def _save_curriculum_plan(self) -> None:
        """Save the curriculum plan to disk."""
        plan_path = self.output_dir / "curriculum_plan.json"
        plan_path.parent.mkdir(parents=True, exist_ok=True)

        plan = {
            "model": self.model_preset,
            "framework": self.framework,
            "stages": self.get_stage_order(),
            "results": [r.to_dict() for r in self.results],
        }

        with open(plan_path, "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2, default=str)
