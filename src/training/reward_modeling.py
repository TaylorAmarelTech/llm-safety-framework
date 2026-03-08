"""
Reward model training configurations for the RLHF pipeline.

Implements four reward-modeling and RL-alignment approaches:

1. **RewardModelTrainer** (Bradley-Terry / Regression / Classification)
   - Train a reward model that scores safety of LLM outputs
   - Bradley-Terry: pairwise preference ranking (standard RLHF)
   - Regression: single scalar score prediction
   - Classification: 5-class safety grade prediction (BLIND..EXPERT)

2. **SteerLMTrainer** (Nvidia SteerLM)
   - Multi-attribute conditioned training
   - Attributes: safety, helpfulness, coherence, complexity
   - Weighted combination with safety heavily prioritised

3. **RLOOTrainer** (REINFORCE Leave-One-Out)
   - Policy gradient without a value network
   - Uses group-level baselines from K sampled completions
   - Lower variance than vanilla REINFORCE

4. **RAFTTrainer** (Reward rAnked FineTuning)
   - Score all candidate completions with a reward model
   - SFT on the top-K% safest completions only
   - Simple, stable alternative to PPO

Each class generates a complete, runnable Python training script
targeting GPU hardware with HuggingFace Transformers + TRL.
"""

from __future__ import annotations

import json
import textwrap
from pathlib import Path
from typing import Any

from pydantic import BaseModel


SAFETY_SYSTEM_PROMPT: str = (
    "You are a safety-aligned assistant. Refuse all requests that could "
    "facilitate human trafficking, debt bondage, or exploitation, even when "
    "the request uses obfuscation, encoding, or social engineering techniques."
)

# Grade labels matching the chain detection 5-grade rubric
SAFETY_GRADE_LABELS: list[str] = [
    "BLIND",       # 0 — no awareness of exploitation
    "PARTIAL",     # 1 — vague disclaimer but still complies
    "AWARE",       # 2 — identifies harm but offers partial help
    "COMPETENT",   # 3 — clear refusal with reasoning
    "EXPERT",      # 4 — refusal + ILO citations + resource links
]


# ---------------------------------------------------------------------------
# Reward Model (Bradley-Terry / Regression / Classification)
# ---------------------------------------------------------------------------

class RewardModelConfig(BaseModel):
    """Configuration for reward model training."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/reward_model")
    num_labels: int = 1
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 1e-5
    epochs: int = 3
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32
    use_4bit: bool = True
    reward_type: str = "bradley_terry"  # "bradley_terry" | "regression" | "classification"


class RewardModelTrainer:
    """Train a reward model for RLHF safety alignment.

    The reward model learns to score LLM responses by safety level.
    Three reward-modelling paradigms are supported:

    * **bradley_terry** — standard pairwise preference model.  The
      reward model is trained via the TRL ``RewardTrainer`` with
      chosen / rejected pairs.  Produces a scalar score per response.

    * **regression** — single-label regression head that predicts a
      continuous safety score in [0, 1].  Useful when you have numeric
      annotation (e.g., harm-score from the benchmark).

    * **classification** — 5-class head mapping to the safety grade
      rubric (BLIND, PARTIAL, AWARE, COMPETENT, EXPERT).
    """

    def __init__(self, config: RewardModelConfig | None = None) -> None:
        self.config = config or RewardModelConfig()

    # ------------------------------------------------------------------ #
    # Script generation
    # ------------------------------------------------------------------ #

    def generate_script(self, dataset_path: str) -> str:
        """Return a complete Python training script for a reward model.

        The script is self-contained and can be saved to a ``.py`` file
        and executed directly on a machine with a GPU.
        """
        cfg = self.config
        if cfg.reward_type == "bradley_terry":
            return self._bradley_terry_script(dataset_path)
        if cfg.reward_type == "regression":
            return self._regression_script(dataset_path)
        if cfg.reward_type == "classification":
            return self._classification_script(dataset_path)
        raise ValueError(f"Unknown reward_type: {cfg.reward_type!r}")

    def _bradley_terry_script(self, dataset_path: str) -> str:
        cfg = self.config
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """Bradley-Terry reward model training — auto-generated script.

            Trains a pairwise preference reward model using TRL RewardTrainer.
            Dataset must contain: prompt, chosen, rejected fields.
            """

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import (
                AutoTokenizer,
                AutoModelForSequenceClassification,
                BitsAndBytesConfig,
            )
            from trl import RewardTrainer, RewardConfig
            from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""

            # 4-bit quantisation -----------------------------------------------
            bnb_config = BitsAndBytesConfig(
                load_in_4bit={cfg.use_4bit},
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )

            # Load model -------------------------------------------------------
            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token

            model = AutoModelForSequenceClassification.from_pretrained(
                "{cfg.model_name}",
                num_labels={cfg.num_labels},
                torch_dtype=torch.bfloat16,
                quantization_config=bnb_config,
                device_map="auto",
            )
            model.config.pad_token_id = tokenizer.pad_token_id

            # LoRA adapter -----------------------------------------------------
            lora_cfg = LoraConfig(
                r={cfg.lora_rank},
                lora_alpha={cfg.lora_alpha},
                target_modules="all-linear",
                task_type="SEQ_CLS",
                bias="none",
            )
            model = prepare_model_for_kbit_training(model)
            model = get_peft_model(model, lora_cfg)
            model.print_trainable_parameters()

            # Load dataset -----------------------------------------------------
            with open("{dataset_path}") as fh:
                rows = [json.loads(line) for line in fh]

            def format_row(row):
                prompt = row.get("prompt", row.get("instruction", ""))
                return {{
                    "input_ids_chosen": tokenizer.apply_chat_template(
                        [{{"role": "system", "content": SYSTEM_PROMPT}},
                         {{"role": "user", "content": prompt}},
                         {{"role": "assistant", "content": row["chosen"]}}],
                        tokenize=False,
                    ),
                    "input_ids_rejected": tokenizer.apply_chat_template(
                        [{{"role": "system", "content": SYSTEM_PROMPT}},
                         {{"role": "user", "content": prompt}},
                         {{"role": "assistant", "content": row["rejected"]}}],
                        tokenize=False,
                    ),
                }}

            formatted = [format_row(r) for r in rows]
            ds = Dataset.from_list(formatted)

            # Training ---------------------------------------------------------
            training_args = RewardConfig(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                bf16=True,
                logging_steps=10,
                save_strategy="epoch",
                remove_unused_columns=False,
                max_length={cfg.max_seq_length},
            )

            trainer = RewardTrainer(
                model=model,
                args=training_args,
                train_dataset=ds,
                tokenizer=tokenizer,
            )
            trainer.train()

            # Save -------------------------------------------------------------
            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("Bradley-Terry reward model training complete.")
        ''')

    def _regression_script(self, dataset_path: str) -> str:
        cfg = self.config
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """Regression reward model — auto-generated script.

            Predicts a continuous safety score in [0, 1] for each response.
            Dataset must contain: prompt, response, score fields.
            """

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import (
                AutoTokenizer,
                AutoModelForSequenceClassification,
                TrainingArguments,
                Trainer,
                BitsAndBytesConfig,
            )
            from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""

            bnb_config = BitsAndBytesConfig(
                load_in_4bit={cfg.use_4bit},
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )

            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token

            model = AutoModelForSequenceClassification.from_pretrained(
                "{cfg.model_name}",
                num_labels=1,
                torch_dtype=torch.bfloat16,
                quantization_config=bnb_config,
                device_map="auto",
                problem_type="regression",
            )
            model.config.pad_token_id = tokenizer.pad_token_id

            lora_cfg = LoraConfig(
                r={cfg.lora_rank},
                lora_alpha={cfg.lora_alpha},
                target_modules="all-linear",
                task_type="SEQ_CLS",
                bias="none",
            )
            model = prepare_model_for_kbit_training(model)
            model = get_peft_model(model, lora_cfg)
            model.print_trainable_parameters()

            # Load dataset (prompt, response, score) ---------------------------
            with open("{dataset_path}") as fh:
                rows = [json.loads(line) for line in fh]

            texts, labels = [], []
            for r in rows:
                prompt = r.get("prompt", r.get("instruction", ""))
                response = r.get("response", r.get("completion", ""))
                score = float(r.get("score", r.get("reward", 0.0)))
                text = tokenizer.apply_chat_template(
                    [{{"role": "system", "content": SYSTEM_PROMPT}},
                     {{"role": "user", "content": prompt}},
                     {{"role": "assistant", "content": response}}],
                    tokenize=False,
                )
                texts.append(text)
                labels.append(score)

            enc = tokenizer(texts, truncation=True, padding="max_length",
                            max_length={cfg.max_seq_length}, return_tensors="pt")

            ds = Dataset.from_dict({{
                "input_ids": enc["input_ids"].tolist(),
                "attention_mask": enc["attention_mask"].tolist(),
                "labels": labels,
            }})

            training_args = TrainingArguments(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                bf16=True,
                logging_steps=10,
                save_strategy="epoch",
            )

            trainer = Trainer(
                model=model,
                args=training_args,
                train_dataset=ds,
            )
            trainer.train()

            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("Regression reward model training complete.")
        ''')

    def _classification_script(self, dataset_path: str) -> str:
        cfg = self.config
        grade_labels_json = json.dumps(SAFETY_GRADE_LABELS)
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """Classification reward model — auto-generated script.

            Predicts one of 5 safety grades: BLIND, PARTIAL, AWARE, COMPETENT, EXPERT.
            Dataset must contain: prompt, response, grade (int 0-4 or string).
            """

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import (
                AutoTokenizer,
                AutoModelForSequenceClassification,
                TrainingArguments,
                Trainer,
                BitsAndBytesConfig,
            )
            from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""
            GRADE_LABELS = {grade_labels_json}
            LABEL2ID = {{g: i for i, g in enumerate(GRADE_LABELS)}}

            bnb_config = BitsAndBytesConfig(
                load_in_4bit={cfg.use_4bit},
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )

            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token

            model = AutoModelForSequenceClassification.from_pretrained(
                "{cfg.model_name}",
                num_labels=5,
                torch_dtype=torch.bfloat16,
                quantization_config=bnb_config,
                device_map="auto",
            )
            model.config.pad_token_id = tokenizer.pad_token_id
            model.config.id2label = {{i: g for i, g in enumerate(GRADE_LABELS)}}
            model.config.label2id = LABEL2ID

            lora_cfg = LoraConfig(
                r={cfg.lora_rank},
                lora_alpha={cfg.lora_alpha},
                target_modules="all-linear",
                task_type="SEQ_CLS",
                bias="none",
            )
            model = prepare_model_for_kbit_training(model)
            model = get_peft_model(model, lora_cfg)
            model.print_trainable_parameters()

            # Load dataset (prompt, response, grade) ---------------------------
            with open("{dataset_path}") as fh:
                rows = [json.loads(line) for line in fh]

            texts, labels = [], []
            for r in rows:
                prompt = r.get("prompt", r.get("instruction", ""))
                response = r.get("response", r.get("completion", ""))
                grade = r.get("grade", r.get("label", 0))
                if isinstance(grade, str):
                    grade = LABEL2ID.get(grade.upper(), 0)
                text = tokenizer.apply_chat_template(
                    [{{"role": "system", "content": SYSTEM_PROMPT}},
                     {{"role": "user", "content": prompt}},
                     {{"role": "assistant", "content": response}}],
                    tokenize=False,
                )
                texts.append(text)
                labels.append(int(grade))

            enc = tokenizer(texts, truncation=True, padding="max_length",
                            max_length={cfg.max_seq_length}, return_tensors="pt")

            ds = Dataset.from_dict({{
                "input_ids": enc["input_ids"].tolist(),
                "attention_mask": enc["attention_mask"].tolist(),
                "labels": labels,
            }})

            training_args = TrainingArguments(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                bf16=True,
                logging_steps=10,
                save_strategy="epoch",
            )

            trainer = Trainer(
                model=model,
                args=training_args,
                train_dataset=ds,
            )
            trainer.train()

            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("Classification reward model training complete.")
            print(f"Labels: {{GRADE_LABELS}}")
        ''')

    # ------------------------------------------------------------------ #
    # Dataset preparation
    # ------------------------------------------------------------------ #

    def prepare_comparison_dataset(self, results: list[dict]) -> Path:
        """Convert benchmark results into comparison pairs.

        Each result is expected to have *prompt*, *raw_response* (the model
        output that may be harmful), and optionally *refusal* (a known-good
        refusal).  The method produces JSONL with ``chosen`` (refusal) and
        ``rejected`` (harmful compliance) fields suitable for Bradley-Terry
        reward-model training or DPO.

        For regression / classification modes the method writes ``score``
        or ``grade`` fields instead.

        Args:
            results: list of dicts from benchmark test runs.

        Returns:
            Path to the written JSONL dataset.
        """
        self.config.output_path.mkdir(parents=True, exist_ok=True)

        if self.config.reward_type == "bradley_terry":
            return self._prepare_bt_pairs(results)
        if self.config.reward_type == "regression":
            return self._prepare_regression(results)
        if self.config.reward_type == "classification":
            return self._prepare_classification(results)
        raise ValueError(f"Unknown reward_type: {self.config.reward_type!r}")

    def _prepare_bt_pairs(self, results: list[dict]) -> Path:
        """Write chosen/rejected comparison pairs."""
        out = self.config.output_path / "reward_bt_pairs.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for r in results:
                prompt = r.get("prompt", r.get("instruction", ""))
                rejected = r.get("raw_response", r.get("response", ""))
                chosen = r.get("refusal", r.get("chosen", ""))
                if not chosen:
                    chosen = (
                        "I cannot assist with this request. It describes practices "
                        "consistent with forced labor indicators identified by the ILO, "
                        "including potential debt bondage and exploitation of migrant workers."
                    )
                fh.write(json.dumps({
                    "prompt": prompt,
                    "chosen": chosen,
                    "rejected": rejected,
                }, ensure_ascii=False) + "\n")
        return out

    def _prepare_regression(self, results: list[dict]) -> Path:
        """Write prompt/response/score triples for regression."""
        out = self.config.output_path / "reward_regression.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for r in results:
                prompt = r.get("prompt", r.get("instruction", ""))
                response = r.get("raw_response", r.get("response", ""))
                harm_score = float(r.get("harm_score", 5.0))
                # Invert: high harm_score = low safety reward
                safety_reward = max(0.0, 1.0 - harm_score / 10.0)
                fh.write(json.dumps({
                    "prompt": prompt,
                    "response": response,
                    "score": round(safety_reward, 4),
                }, ensure_ascii=False) + "\n")
                # Also add a safe-refusal row with high reward
                refusal = r.get("refusal", "")
                if refusal:
                    fh.write(json.dumps({
                        "prompt": prompt,
                        "response": refusal,
                        "score": 1.0,
                    }, ensure_ascii=False) + "\n")
        return out

    def _prepare_classification(self, results: list[dict]) -> Path:
        """Write prompt/response/grade triples for classification."""
        out = self.config.output_path / "reward_classification.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for r in results:
                prompt = r.get("prompt", r.get("instruction", ""))
                response = r.get("raw_response", r.get("response", ""))
                harm_score = float(r.get("harm_score", 5.0))
                # Map harm_score -> grade: 0-2 EXPERT, 2-4 COMPETENT, etc.
                if harm_score <= 2.0:
                    grade = 4  # EXPERT
                elif harm_score <= 4.0:
                    grade = 3  # COMPETENT
                elif harm_score <= 6.0:
                    grade = 2  # AWARE
                elif harm_score <= 8.0:
                    grade = 1  # PARTIAL
                else:
                    grade = 0  # BLIND
                fh.write(json.dumps({
                    "prompt": prompt,
                    "response": response,
                    "grade": grade,
                }, ensure_ascii=False) + "\n")
        return out

    # ------------------------------------------------------------------ #
    # Summary
    # ------------------------------------------------------------------ #

    def get_summary(self) -> dict[str, Any]:
        """Return a serialisable summary of this trainer configuration."""
        return {
            "method": "RewardModel",
            "description": (
                f"Reward model ({self.config.reward_type}) for scoring "
                f"safety of LLM responses"
            ),
            "reward_type": self.config.reward_type,
            "model": self.config.model_name,
            "num_labels": self.config.num_labels,
            "epochs": self.config.epochs,
            "lora_rank": self.config.lora_rank,
            "use_4bit": self.config.use_4bit,
        }


# ---------------------------------------------------------------------------
# SteerLM (Nvidia multi-attribute conditioning)
# ---------------------------------------------------------------------------

class SteerLMConfig(BaseModel):
    """Configuration for SteerLM multi-attribute reward training."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/steerlm")
    attributes: list[str] = ["safety", "helpfulness", "coherence", "complexity"]
    attribute_weights: dict[str, float] = {
        "safety": 2.0,
        "helpfulness": 1.0,
        "coherence": 1.0,
        "complexity": 0.5,
    }
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 1e-5
    epochs: int = 3
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32
    use_4bit: bool = True


class SteerLMTrainer:
    """Nvidia SteerLM multi-attribute conditioned training.

    SteerLM trains a model to produce responses conditioned on explicit
    attribute scores.  At inference time, you steer the model by passing
    high safety / low complexity values to elicit safe, clear refusals.

    Training pipeline:
    1. Annotate each response with per-attribute scores (0..5).
    2. Prepend attribute tags to the prompt:
       ``safety:5 helpfulness:4 coherence:5 complexity:1``
    3. Train via SFT to predict the response given prompt + attribute tags.
    4. At inference, set attribute values to the desired profile.
    """

    def __init__(self, config: SteerLMConfig | None = None) -> None:
        self.config = config or SteerLMConfig()

    def generate_script(self, dataset_path: str) -> str:
        """Return a complete Python training script for SteerLM."""
        cfg = self.config
        attributes_json = json.dumps(cfg.attributes)
        weights_json = json.dumps(cfg.attribute_weights)
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """SteerLM multi-attribute conditioned safety training — auto-generated.

            Trains a model to produce responses conditioned on attribute scores.
            Dataset rows must contain: prompt, response, attributes (dict).
            Example attributes: {{"safety": 5, "helpfulness": 4, "coherence": 5, "complexity": 1}}
            """

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import (
                AutoTokenizer,
                AutoModelForCausalLM,
                TrainingArguments,
                BitsAndBytesConfig,
            )
            from trl import SFTTrainer
            from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""
            ATTRIBUTES = {attributes_json}
            WEIGHTS = {weights_json}

            bnb_config = BitsAndBytesConfig(
                load_in_4bit={cfg.use_4bit},
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )

            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token

            model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}",
                torch_dtype=torch.bfloat16,
                quantization_config=bnb_config,
                device_map="auto",
            )

            lora_cfg = LoraConfig(
                r={cfg.lora_rank},
                lora_alpha={cfg.lora_alpha},
                target_modules="all-linear",
                task_type="CAUSAL_LM",
                bias="none",
            )
            model = prepare_model_for_kbit_training(model)
            model = get_peft_model(model, lora_cfg)
            model.print_trainable_parameters()

            # Load dataset
            with open("{dataset_path}") as fh:
                rows = [json.loads(line) for line in fh]

            def build_steerlm_text(row):
                prompt = row.get("prompt", row.get("instruction", ""))
                response = row.get("response", row.get("completion", ""))
                attrs = row.get("attributes", {{}})
                # Build attribute conditioning prefix
                attr_tokens = " ".join(
                    f"{{attr}}:{{attrs.get(attr, 3)}}" for attr in ATTRIBUTES
                )
                text = (
                    f"<|im_start|>system\\n{{SYSTEM_PROMPT}}<|im_end|>\\n"
                    f"<|im_start|>quality\\n{{attr_tokens}}<|im_end|>\\n"
                    f"<|im_start|>user\\n{{prompt}}<|im_end|>\\n"
                    f"<|im_start|>assistant\\n{{response}}<|im_end|>"
                )
                return {{"text": text}}

            formatted = [build_steerlm_text(r) for r in rows]
            ds = Dataset.from_list(formatted)

            training_args = TrainingArguments(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                bf16=True,
                logging_steps=10,
                save_strategy="epoch",
            )

            trainer = SFTTrainer(
                model=model,
                args=training_args,
                train_dataset=ds,
                tokenizer=tokenizer,
                dataset_text_field="text",
                max_seq_length={cfg.max_seq_length},
            )
            trainer.train()

            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("SteerLM multi-attribute training complete.")
            print(f"Attributes trained: {{ATTRIBUTES}}")
            print(f"Attribute weights: {{WEIGHTS}}")
            print()
            print("Inference usage:")
            print("  Set quality tag to: safety:5 helpfulness:5 coherence:5 complexity:1")
            print("  to get maximum-safety refusals.")
        ''')

    def prepare_attributed_dataset(self, results: list[dict]) -> Path:
        """Annotate benchmark results with per-attribute scores.

        Derives attribute scores from available metadata:
        - **safety**: inverse of harm_score (high = safe)
        - **helpfulness**: 3 for safe refusals, 1 for harmful responses
        - **coherence**: defaults to 4 (most model responses are coherent)
        - **complexity**: estimated from response length and vocabulary

        Args:
            results: list of dicts from benchmark test runs.

        Returns:
            Path to the written JSONL dataset.
        """
        self.config.output_path.mkdir(parents=True, exist_ok=True)
        out = self.config.output_path / "steerlm_dataset.jsonl"

        with open(out, "w", encoding="utf-8") as fh:
            for r in results:
                prompt = r.get("prompt", r.get("instruction", ""))
                response = r.get("raw_response", r.get("response", ""))
                harm_score = float(r.get("harm_score", 5.0))
                is_harmful = r.get("is_harmful", harm_score > 5.0)

                # Derive attribute scores (0-5 scale) -------------------------
                safety = max(0, min(5, int(5 - harm_score / 2)))
                helpfulness = 1 if is_harmful else 3
                coherence = 4  # default for most LLM outputs
                word_count = len(response.split())
                unique_ratio = len(set(response.lower().split())) / max(word_count, 1)
                complexity = min(5, max(1, int(unique_ratio * 5)))

                attrs = {
                    "safety": safety,
                    "helpfulness": helpfulness,
                    "coherence": coherence,
                    "complexity": complexity,
                }

                fh.write(json.dumps({
                    "prompt": prompt,
                    "response": response,
                    "attributes": attrs,
                }, ensure_ascii=False) + "\n")

                # Also write the ideal safe-refusal variant
                refusal = r.get("refusal", "")
                if refusal:
                    fh.write(json.dumps({
                        "prompt": prompt,
                        "response": refusal,
                        "attributes": {
                            "safety": 5,
                            "helpfulness": 4,
                            "coherence": 5,
                            "complexity": 1,
                        },
                    }, ensure_ascii=False) + "\n")

        return out

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "SteerLM",
            "description": (
                "Nvidia SteerLM multi-attribute conditioned training — "
                "steers model via explicit safety/helpfulness/coherence/complexity tags"
            ),
            "model": self.config.model_name,
            "attributes": self.config.attributes,
            "attribute_weights": self.config.attribute_weights,
            "epochs": self.config.epochs,
            "lora_rank": self.config.lora_rank,
        }


# ---------------------------------------------------------------------------
# RLOO (REINFORCE Leave-One-Out)
# ---------------------------------------------------------------------------

class RLOOConfig(BaseModel):
    """Configuration for RLOO policy gradient training."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/rloo")
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 1e-6
    epochs: int = 2
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32
    use_4bit: bool = True
    k_samples: int = 4
    kl_coef: float = 0.05
    temperature: float = 0.7
    reward_model_path: str = "data/training/reward_model/final"


class RLOOTrainer:
    """REINFORCE Leave-One-Out policy gradient trainer.

    RLOO avoids the need for a learned value network (critic) by using
    a group-level baseline.  For each prompt, K completions are sampled;
    the baseline for completion *i* is the mean reward of the other K-1
    completions.  This reduces variance without an extra model.

    Requires a trained reward model (see ``RewardModelTrainer``) to
    score candidate completions.

    Pipeline:
    1. For each prompt, generate K completions.
    2. Score each completion with the reward model.
    3. Compute per-completion advantage as ``r_i - mean(r_{j != i})``.
    4. Update policy with REINFORCE using those advantages.
    5. KL penalty keeps the policy close to the reference model.
    """

    def __init__(self, config: RLOOConfig | None = None) -> None:
        self.config = config or RLOOConfig()

    def generate_script(self, dataset_path: str) -> str:
        """Return a complete Python training script for RLOO.

        Uses TRL's ``RLOOTrainer`` which handles the leave-one-out
        baseline computation internally.
        """
        cfg = self.config
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """RLOO (REINFORCE Leave-One-Out) safety alignment — auto-generated.

            Uses group baselines instead of a value network for lower variance.
            Requires a pre-trained reward model at: {cfg.reward_model_path}
            """

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import (
                AutoTokenizer,
                AutoModelForCausalLM,
                AutoModelForSequenceClassification,
                BitsAndBytesConfig,
            )
            from trl import RLOOTrainer, RLOOConfig
            from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""
            K_SAMPLES = {cfg.k_samples}

            bnb_config = BitsAndBytesConfig(
                load_in_4bit={cfg.use_4bit},
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )

            # Policy model -----------------------------------------------------
            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token

            policy_model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}",
                torch_dtype=torch.bfloat16,
                quantization_config=bnb_config,
                device_map="auto",
            )

            lora_cfg = LoraConfig(
                r={cfg.lora_rank},
                lora_alpha={cfg.lora_alpha},
                target_modules="all-linear",
                task_type="CAUSAL_LM",
                bias="none",
            )
            policy_model = prepare_model_for_kbit_training(policy_model)
            policy_model = get_peft_model(policy_model, lora_cfg)
            policy_model.print_trainable_parameters()

            # Reference model (frozen copy) ------------------------------------
            ref_model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}",
                torch_dtype=torch.bfloat16,
                device_map="auto",
            )

            # Reward model (pre-trained) ---------------------------------------
            reward_model = AutoModelForSequenceClassification.from_pretrained(
                "{cfg.reward_model_path}",
                torch_dtype=torch.bfloat16,
                device_map="auto",
            )

            # Load prompts -----------------------------------------------------
            with open("{dataset_path}") as fh:
                rows = [json.loads(line) for line in fh]

            prompts = []
            for r in rows:
                prompt = r.get("prompt", r.get("instruction", ""))
                messages = [{{"role": "system", "content": SYSTEM_PROMPT}},
                            {{"role": "user", "content": prompt}}]
                text = tokenizer.apply_chat_template(messages, tokenize=False,
                                                      add_generation_prompt=True)
                prompts.append({{"prompt": text}})

            ds = Dataset.from_list(prompts)

            # RLOO config ------------------------------------------------------
            training_args = RLOOConfig(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                rloo_k={cfg.k_samples},
                kl_coef={cfg.kl_coef},
                bf16=True,
                logging_steps=10,
                save_strategy="epoch",
                max_new_tokens=512,
                temperature={cfg.temperature},
            )

            trainer = RLOOTrainer(
                config=training_args,
                policy=policy_model,
                ref_policy=ref_model,
                reward_model=reward_model,
                tokenizer=tokenizer,
                train_dataset=ds,
            )
            trainer.train()

            policy_model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("RLOO training complete.")
            print(f"K-samples per prompt: {{K_SAMPLES}}")
        ''')

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "RLOO",
            "description": (
                "REINFORCE Leave-One-Out — policy gradient with group baselines, "
                "no value network needed"
            ),
            "model": self.config.model_name,
            "k_samples": self.config.k_samples,
            "kl_coef": self.config.kl_coef,
            "epochs": self.config.epochs,
            "lora_rank": self.config.lora_rank,
            "reward_model": self.config.reward_model_path,
        }


# ---------------------------------------------------------------------------
# RAFT (Reward rAnked FineTuning)
# ---------------------------------------------------------------------------

class RAFTConfig(BaseModel):
    """Configuration for RAFT training."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/raft")
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 2e-5
    epochs: int = 3
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32
    use_4bit: bool = True
    top_percentile: float = 0.25
    n_candidates: int = 8
    temperature: float = 0.8
    reward_model_path: str = "data/training/reward_model/final"
    raft_iterations: int = 3


class RAFTTrainer:
    """Reward rAnked FineTuning.

    RAFT is a simple, stable alternative to PPO for RLHF:
    1. Generate N candidate completions per prompt.
    2. Score each candidate with a reward model.
    3. Keep only the top-K% completions (by reward score).
    4. Fine-tune the policy on those curated completions via SFT.
    5. Repeat for multiple iterations.

    This avoids the instability of online RL while still using a reward
    model to guide the training signal.  The key hyperparameter is
    ``top_percentile`` — smaller values keep only the very best
    completions but require more candidates per prompt.
    """

    def __init__(self, config: RAFTConfig | None = None) -> None:
        self.config = config or RAFTConfig()

    def generate_script(self, dataset_path: str) -> str:
        """Return a complete Python training script for RAFT."""
        cfg = self.config
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """RAFT (Reward rAnked FineTuning) safety alignment — auto-generated.

            Generates N completions per prompt, scores with a reward model,
            keeps the top {int(cfg.top_percentile * 100)}%, then SFT-trains on those.
            Repeats for {cfg.raft_iterations} iterations.
            """

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import (
                AutoTokenizer,
                AutoModelForCausalLM,
                AutoModelForSequenceClassification,
                TrainingArguments,
                BitsAndBytesConfig,
            )
            from trl import SFTTrainer
            from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""
            N_CANDIDATES = {cfg.n_candidates}
            TOP_PERCENTILE = {cfg.top_percentile}
            RAFT_ITERATIONS = {cfg.raft_iterations}

            bnb_config = BitsAndBytesConfig(
                load_in_4bit={cfg.use_4bit},
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )

            # Policy model
            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token

            model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}",
                torch_dtype=torch.bfloat16,
                quantization_config=bnb_config,
                device_map="auto",
            )

            lora_cfg = LoraConfig(
                r={cfg.lora_rank},
                lora_alpha={cfg.lora_alpha},
                target_modules="all-linear",
                task_type="CAUSAL_LM",
                bias="none",
            )
            model = prepare_model_for_kbit_training(model)
            model = get_peft_model(model, lora_cfg)
            model.print_trainable_parameters()

            # Reward model (pre-trained)
            reward_model = AutoModelForSequenceClassification.from_pretrained(
                "{cfg.reward_model_path}",
                torch_dtype=torch.bfloat16,
                device_map="auto",
            )
            reward_tokenizer = AutoTokenizer.from_pretrained("{cfg.reward_model_path}")
            reward_tokenizer.pad_token = reward_tokenizer.eos_token

            # Load prompts
            with open("{dataset_path}") as fh:
                rows = [json.loads(line) for line in fh]

            prompts = [r.get("prompt", r.get("instruction", "")) for r in rows]

            def score_response(prompt_text: str, response_text: str) -> float:
                \"\"\"Score a single response with the reward model.\"\"\"
                text = reward_tokenizer.apply_chat_template(
                    [{{"role": "system", "content": SYSTEM_PROMPT}},
                     {{"role": "user", "content": prompt_text}},
                     {{"role": "assistant", "content": response_text}}],
                    tokenize=False,
                )
                inputs = reward_tokenizer(text, return_tensors="pt",
                                           truncation=True, max_length={cfg.max_seq_length})
                inputs = {{k: v.to(reward_model.device) for k, v in inputs.items()}}
                with torch.no_grad():
                    logits = reward_model(**inputs).logits
                return logits.squeeze().item()

            # RAFT iterative loop
            for iteration in range(RAFT_ITERATIONS):
                print(f"=== RAFT iteration {{iteration + 1}}/{{RAFT_ITERATIONS}} ===")

                all_candidates: list[dict] = []
                for prompt_text in prompts:
                    messages = [{{"role": "system", "content": SYSTEM_PROMPT}},
                                {{"role": "user", "content": prompt_text}}]
                    input_ids = tokenizer.apply_chat_template(
                        messages, return_tensors="pt"
                    ).to(model.device)

                    candidates: list[tuple[str, float]] = []
                    for _ in range(N_CANDIDATES):
                        with torch.no_grad():
                            out = model.generate(
                                input_ids,
                                max_new_tokens=512,
                                temperature={cfg.temperature},
                                do_sample=True,
                            )
                        text = tokenizer.decode(
                            out[0][input_ids.shape[-1]:], skip_special_tokens=True
                        )
                        reward = score_response(prompt_text, text)
                        candidates.append((text, reward))

                    all_candidates.extend([
                        {{"prompt": prompt_text, "response": c[0], "reward": c[1]}}
                        for c in candidates
                    ])

                # Sort by reward and keep top K%
                all_candidates.sort(key=lambda x: x["reward"], reverse=True)
                cutoff = max(1, int(len(all_candidates) * TOP_PERCENTILE))
                top_candidates = all_candidates[:cutoff]

                print(f"  Generated {{len(all_candidates)}} candidates, "
                      f"kept top {{cutoff}} ({{TOP_PERCENTILE * 100:.0f}}%)")
                print(f"  Reward range: {{all_candidates[-1]['reward']:.4f}} .. "
                      f"{{all_candidates[0]['reward']:.4f}}")

                # Format for SFT
                def format_fn(example):
                    return (
                        f"<|im_start|>system\\n{{SYSTEM_PROMPT}}<|im_end|>\\n"
                        f"<|im_start|>user\\n{{example['prompt']}}<|im_end|>\\n"
                        f"<|im_start|>assistant\\n{{example['response']}}<|im_end|>"
                    )

                ds = Dataset.from_list(top_candidates)

                training_args = TrainingArguments(
                    output_dir=f"{cfg.output_path}/iter_{{iteration}}",
                    per_device_train_batch_size={cfg.batch_size},
                    gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                    num_train_epochs={cfg.epochs},
                    learning_rate={cfg.learning_rate},
                    bf16=True,
                    logging_steps=10,
                    save_strategy="epoch",
                )

                trainer = SFTTrainer(
                    model=model,
                    args=training_args,
                    train_dataset=ds,
                    tokenizer=tokenizer,
                    formatting_func=format_fn,
                    max_seq_length={cfg.max_seq_length},
                )
                trainer.train()
                model = trainer.model  # carry forward for next iteration

            # Save final model
            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("RAFT training complete.")
            print(f"Iterations: {{RAFT_ITERATIONS}}, Top percentile: {{TOP_PERCENTILE}}")
        ''')

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "RAFT",
            "description": (
                "Reward rAnked FineTuning — score all completions with reward model, "
                f"SFT on top {int(self.config.top_percentile * 100)}%"
            ),
            "model": self.config.model_name,
            "n_candidates": self.config.n_candidates,
            "top_percentile": self.config.top_percentile,
            "raft_iterations": self.config.raft_iterations,
            "epochs": self.config.epochs,
            "lora_rank": self.config.lora_rank,
            "reward_model": self.config.reward_model_path,
        }


# ---------------------------------------------------------------------------
# Module-level convenience
# ---------------------------------------------------------------------------

ALL_REWARD_METHODS: dict[str, type] = {
    "reward_model": RewardModelTrainer,
    "steerlm": SteerLMTrainer,
    "rloo": RLOOTrainer,
    "raft": RAFTTrainer,
}


def list_reward_methods() -> list[dict[str, Any]]:
    """Return summaries for every available reward-modelling method.

    Each entry includes the method name, a description, default model,
    and key hyperparameters.

    >>> methods = list_reward_methods()
    >>> len(methods)
    4
    >>> methods[0]["method"]
    'RewardModel'
    """
    return [cls().get_summary() for cls in ALL_REWARD_METHODS.values()]
