"""
Advanced training algorithm configurations and script generators for safety fine-tuning.

Implements additional training methods beyond standard SFT/DPO:
1. SPIN (Self-Play Fine-Tuning) — synthetic data via self-play
2. SimPO (Simple Preference Optimization) — reference-free DPO
3. IPO (Identity Preference Optimization) — regularized DPO
4. Rejection Sampling (Best-of-N) — score-filtered SFT
5. Constitutional AI — self-critique revision loop
6. DataMixer — curriculum-aware data mixing ratios

Each class generates complete, runnable training scripts targeting
GPU hardware with HuggingFace Transformers + TRL.
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


# ---------------------------------------------------------------------------
# SPIN (Self-Play Fine-Tuning)
# ---------------------------------------------------------------------------

class SPINConfig(BaseModel):
    """Configuration for SPIN training."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/spin")
    num_iterations: int = 3
    samples_per_prompt: int = 4
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 5e-6
    epochs_per_iteration: int = 2
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32
    temperature: float = 0.7


class SPINTrainer:
    """Self-Play Fine-Tuning.

    The model generates responses to attack prompts, then trains to
    distinguish its own (potentially unsafe) outputs from ground-truth
    refusal responses.  Over successive iterations the model converges
    toward always producing correct refusals.
    """

    def __init__(self, config: SPINConfig | None = None) -> None:
        self.config = config or SPINConfig()

    def generate_script(self, dataset_path: str) -> str:
        """Return a complete Python training script for SPIN."""
        cfg = self.config
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """SPIN self-play safety fine-tuning — auto-generated script."""

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
            from trl import DPOTrainer
            from peft import LoraConfig, get_peft_model

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""
            DATASET_PATH = "{dataset_path}"
            OUTPUT_DIR = "{cfg.output_path}"
            NUM_ITERATIONS = {cfg.num_iterations}
            SAMPLES_PER_PROMPT = {cfg.samples_per_prompt}

            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token

            model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}", torch_dtype=torch.bfloat16, device_map="auto",
            )
            lora_cfg = LoraConfig(r={cfg.lora_rank}, lora_alpha={cfg.lora_alpha},
                                  target_modules="all-linear", task_type="CAUSAL_LM")
            model = get_peft_model(model, lora_cfg)

            with open(DATASET_PATH) as fh:
                raw = [json.loads(line) for line in fh]

            for iteration in range(NUM_ITERATIONS):
                print(f"=== SPIN iteration {{iteration + 1}}/{{NUM_ITERATIONS}} ===")
                pairs = []
                for ex in raw:
                    prompt_text = ex.get("prompt", ex.get("instruction", ""))
                    ground_truth = ex.get("refusal", ex.get("output", ""))
                    messages = [{{"role": "system", "content": SYSTEM_PROMPT}},
                                {{"role": "user", "content": prompt_text}}]
                    input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
                    for _ in range(SAMPLES_PER_PROMPT):
                        with torch.no_grad():
                            out = model.generate(input_ids, max_new_tokens=512,
                                                 temperature={cfg.temperature}, do_sample=True)
                        generated = tokenizer.decode(out[0][input_ids.shape[-1]:], skip_special_tokens=True)
                        pairs.append({{"prompt": prompt_text, "chosen": ground_truth,
                                       "rejected": generated}})
                ds = Dataset.from_list(pairs)
                training_args = TrainingArguments(
                    output_dir=f"{{OUTPUT_DIR}}/iter_{{iteration}}",
                    per_device_train_batch_size={cfg.batch_size},
                    gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                    num_train_epochs={cfg.epochs_per_iteration},
                    learning_rate={cfg.learning_rate},
                    bf16=True, logging_steps=10, save_strategy="epoch",
                    remove_unused_columns=False,
                )
                trainer = DPOTrainer(model=model, args=training_args,
                                     train_dataset=ds, tokenizer=tokenizer)
                trainer.train()
                model = trainer.model
            model.save_pretrained(f"{{OUTPUT_DIR}}/final")
            tokenizer.save_pretrained(f"{{OUTPUT_DIR}}/final")
            print("SPIN training complete.")
        ''')

    def prepare_dataset(self, prompts: list[dict]) -> Path:
        """Write prompts to JSONL ready for the generated script."""
        self.config.output_path.mkdir(parents=True, exist_ok=True)
        out = self.config.output_path / "spin_dataset.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for p in prompts:
                fh.write(json.dumps(p, ensure_ascii=False) + "\n")
        return out

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "SPIN",
            "description": "Self-Play Fine-Tuning — iterative DPO against own generations",
            "model": self.config.model_name,
            "iterations": self.config.num_iterations,
            "samples_per_prompt": self.config.samples_per_prompt,
            "lora_rank": self.config.lora_rank,
        }


# ---------------------------------------------------------------------------
# SimPO (Simple Preference Optimization)
# ---------------------------------------------------------------------------

class SimPOConfig(BaseModel):
    """Configuration for SimPO training."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/simpo")
    beta: float = 2.0
    gamma: float = 1.0
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 1e-6
    epochs: int = 3
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32


class SimPOTrainer:
    """Simple Preference Optimization (reference-model-free DPO).

    Uses average log probability as an implicit reward signal, plus a
    target margin *gamma* that separates chosen from rejected.  Because
    no reference model is needed, memory usage is roughly halved compared
    to standard DPO.
    """

    def __init__(self, config: SimPOConfig | None = None) -> None:
        self.config = config or SimPOConfig()

    def generate_script(self, dataset_path: str) -> str:
        cfg = self.config
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """SimPO reference-free preference optimization — auto-generated."""

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
            from trl import DPOTrainer, DPOConfig
            from peft import LoraConfig, get_peft_model

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""

            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token
            model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}", torch_dtype=torch.bfloat16, device_map="auto",
            )
            lora_cfg = LoraConfig(r={cfg.lora_rank}, lora_alpha={cfg.lora_alpha},
                                  target_modules="all-linear", task_type="CAUSAL_LM")
            model = get_peft_model(model, lora_cfg)

            with open("{dataset_path}") as fh:
                rows = [json.loads(line) for line in fh]
            ds = Dataset.from_list(rows)

            training_args = DPOConfig(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                beta={cfg.beta},
                loss_type="simpo",
                simpo_gamma={cfg.gamma},
                bf16=True, logging_steps=10, save_strategy="epoch",
                remove_unused_columns=False,
            )
            trainer = DPOTrainer(
                model=model, args=training_args,
                train_dataset=ds, tokenizer=tokenizer,
            )
            trainer.train()
            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("SimPO training complete.")
        ''')

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "SimPO",
            "description": "Reference-free DPO using average log-prob reward + target margin",
            "model": self.config.model_name,
            "beta": self.config.beta,
            "gamma": self.config.gamma,
            "epochs": self.config.epochs,
        }


# ---------------------------------------------------------------------------
# IPO (Identity Preference Optimization)
# ---------------------------------------------------------------------------

class IPOConfig(BaseModel):
    """Configuration for IPO training."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/ipo")
    beta: float = 0.1
    tau: float = 0.05
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 5e-7
    epochs: int = 3
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32


class IPOTrainer:
    """Identity Preference Optimization (regularized DPO).

    Adds an identity-mapping regularization term that prevents the policy
    from drifting too far from the preference dataset distribution.  This
    avoids the overfitting failure mode where DPO memorises preference
    pairs instead of learning a general safety policy.
    """

    def __init__(self, config: IPOConfig | None = None) -> None:
        self.config = config or IPOConfig()

    def generate_script(self, dataset_path: str) -> str:
        cfg = self.config
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """IPO identity-regularized preference optimization — auto-generated."""

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import AutoTokenizer, AutoModelForCausalLM
            from trl import DPOTrainer, DPOConfig
            from peft import LoraConfig, get_peft_model

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""

            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token
            model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}", torch_dtype=torch.bfloat16, device_map="auto",
            )
            ref_model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}", torch_dtype=torch.bfloat16, device_map="auto",
            )
            lora_cfg = LoraConfig(r={cfg.lora_rank}, lora_alpha={cfg.lora_alpha},
                                  target_modules="all-linear", task_type="CAUSAL_LM")
            model = get_peft_model(model, lora_cfg)

            with open("{dataset_path}") as fh:
                rows = [json.loads(line) for line in fh]
            ds = Dataset.from_list(rows)

            training_args = DPOConfig(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                beta={cfg.beta},
                loss_type="ipo",
                bf16=True, logging_steps=10, save_strategy="epoch",
                remove_unused_columns=False,
            )
            trainer = DPOTrainer(
                model=model, ref_model=ref_model,
                args=training_args,
                train_dataset=ds, tokenizer=tokenizer,
            )
            trainer.train()
            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("IPO training complete.")
        ''')

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "IPO",
            "description": "Identity-regularized DPO that prevents overfitting to preference pairs",
            "model": self.config.model_name,
            "beta": self.config.beta,
            "tau": self.config.tau,
            "epochs": self.config.epochs,
        }


# ---------------------------------------------------------------------------
# Rejection Sampling (Best-of-N)
# ---------------------------------------------------------------------------

class RejectionSamplingConfig(BaseModel):
    """Configuration for rejection sampling."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/rejection_sampling")
    n_samples: int = 8
    temperature: float = 0.8
    top_k: int = 1
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 2e-5
    epochs: int = 3
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32


class RejectionSampler:
    """Best-of-N rejection sampling for safety SFT.

    Generates N candidate responses per attack prompt, scores each with
    ``classify_response`` from the live tester module, keeps only the
    best (highest safety score) responses, then fine-tunes on those
    curated pairs via standard SFT.
    """

    def __init__(self, config: RejectionSamplingConfig | None = None) -> None:
        self.config = config or RejectionSamplingConfig()

    def generate_script(self, dataset_path: str) -> str:
        cfg = self.config
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """Rejection sampling (Best-of-N) safety SFT — auto-generated."""

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import (
                AutoTokenizer, AutoModelForCausalLM, TrainingArguments,
            )
            from trl import SFTTrainer
            from peft import LoraConfig, get_peft_model
            from src.training.live_tester import classify_response

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""
            N_SAMPLES = {cfg.n_samples}
            TOP_K = {cfg.top_k}

            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token
            model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}", torch_dtype=torch.bfloat16, device_map="auto",
            )
            lora_cfg = LoraConfig(r={cfg.lora_rank}, lora_alpha={cfg.lora_alpha},
                                  target_modules="all-linear", task_type="CAUSAL_LM")
            model = get_peft_model(model, lora_cfg)

            with open("{dataset_path}") as fh:
                raw = [json.loads(line) for line in fh]

            print(f"Generating {{N_SAMPLES}} candidates per prompt for {{len(raw)}} prompts...")
            curated: list[dict] = []
            for ex in raw:
                prompt_text = ex.get("prompt", ex.get("instruction", ""))
                messages = [{{"role": "system", "content": SYSTEM_PROMPT}},
                            {{"role": "user", "content": prompt_text}}]
                input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
                candidates: list[tuple[str, float]] = []
                for _ in range(N_SAMPLES):
                    with torch.no_grad():
                        out = model.generate(input_ids, max_new_tokens=512,
                                             temperature={cfg.temperature}, do_sample=True)
                    text = tokenizer.decode(out[0][input_ids.shape[-1]:], skip_special_tokens=True)
                    score = classify_response(prompt_text, text)
                    candidates.append((text, score))
                candidates.sort(key=lambda c: c[1], reverse=True)
                for text, score in candidates[:TOP_K]:
                    curated.append({{"prompt": prompt_text, "completion": text,
                                     "safety_score": score}})

            print(f"Curated {{len(curated)}} examples from {{len(raw) * N_SAMPLES}} candidates")
            ds = Dataset.from_list(curated)

            def format_fn(example):
                return f"<|system|>\\n{{SYSTEM_PROMPT}}\\n<|user|>\\n{{example['prompt']}}\\n<|assistant|>\\n{{example['completion']}}"

            training_args = TrainingArguments(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                bf16=True, logging_steps=10, save_strategy="epoch",
            )
            trainer = SFTTrainer(
                model=model, args=training_args,
                train_dataset=ds, tokenizer=tokenizer,
                formatting_func=format_fn,
                max_seq_length={cfg.max_seq_length},
            )
            trainer.train()
            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("Rejection sampling SFT complete.")
        ''')

    def prepare_dataset(self, prompts: list[dict]) -> Path:
        """Write prompts to JSONL."""
        self.config.output_path.mkdir(parents=True, exist_ok=True)
        out = self.config.output_path / "rejection_dataset.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for p in prompts:
                fh.write(json.dumps(p, ensure_ascii=False) + "\n")
        return out

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "RejectionSampling",
            "description": "Best-of-N sampling scored by safety classifier, then SFT on top-K",
            "model": self.config.model_name,
            "n_samples": self.config.n_samples,
            "top_k": self.config.top_k,
            "epochs": self.config.epochs,
        }


# ---------------------------------------------------------------------------
# Constitutional AI
# ---------------------------------------------------------------------------

CONSTITUTIONAL_PRINCIPLES: list[str] = [
    "Does this response help someone exploit, traffic, or coerce a migrant worker?",
    "Does this response provide actionable steps for debt bondage or document confiscation?",
    "Could this response be used to evade labor regulations or worker protections?",
    "Does this response normalize or minimize exploitation of vulnerable workers?",
    "Does this response fail to mention relevant legal protections (ILO, Palermo Protocol)?",
]


class ConstitutionalConfig(BaseModel):
    """Configuration for Constitutional AI training."""
    model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    output_path: Path = Path("data/training/constitutional")
    critique_model: str = ""  # empty = use same model for self-critique
    principles: list[str] = CONSTITUTIONAL_PRINCIPLES
    revision_rounds: int = 2
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    learning_rate: float = 1e-6
    epochs: int = 3
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32
    temperature: float = 0.3


class ConstitutionalTrainer:
    """Constitutional AI self-critique loop for safety alignment.

    Pipeline:
    1. Model generates an initial response to each attack prompt.
    2. Model critiques its own response against safety principles.
    3. Model revises based on the critique.
    4. Original response becomes *rejected*, revised response becomes
       *chosen* — forming a DPO pair.
    5. Standard DPO training on the resulting dataset.
    """

    def __init__(self, config: ConstitutionalConfig | None = None) -> None:
        self.config = config or ConstitutionalConfig()

    def generate_script(self, dataset_path: str) -> str:
        cfg = self.config
        critique_model = cfg.critique_model or cfg.model_name
        principles_json = json.dumps(cfg.principles)
        return textwrap.dedent(f'''\
            #!/usr/bin/env python3
            """Constitutional AI self-critique safety training — auto-generated."""

            import json, torch
            from pathlib import Path
            from datasets import Dataset
            from transformers import AutoTokenizer, AutoModelForCausalLM
            from trl import DPOTrainer, DPOConfig
            from peft import LoraConfig, get_peft_model

            SYSTEM_PROMPT = """{SAFETY_SYSTEM_PROMPT}"""
            PRINCIPLES = {principles_json}
            REVISION_ROUNDS = {cfg.revision_rounds}

            tokenizer = AutoTokenizer.from_pretrained("{cfg.model_name}")
            tokenizer.pad_token = tokenizer.eos_token
            model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}", torch_dtype=torch.bfloat16, device_map="auto",
            )
            critique_model_inst = AutoModelForCausalLM.from_pretrained(
                "{critique_model}", torch_dtype=torch.bfloat16, device_map="auto",
            )
            lora_cfg = LoraConfig(r={cfg.lora_rank}, lora_alpha={cfg.lora_alpha},
                                  target_modules="all-linear", task_type="CAUSAL_LM")
            model = get_peft_model(model, lora_cfg)

            def generate_text(mdl, prompt: str, max_tokens: int = 512) -> str:
                ids = tokenizer(prompt, return_tensors="pt").input_ids.to(mdl.device)
                with torch.no_grad():
                    out = mdl.generate(ids, max_new_tokens=max_tokens,
                                       temperature={cfg.temperature}, do_sample=True)
                return tokenizer.decode(out[0][ids.shape[-1]:], skip_special_tokens=True)

            with open("{dataset_path}") as fh:
                raw = [json.loads(line) for line in fh]

            pairs: list[dict] = []
            for ex in raw:
                prompt_text = ex.get("prompt", ex.get("instruction", ""))
                initial = generate_text(model, f"{{SYSTEM_PROMPT}}\\n\\nUser: {{prompt_text}}\\nAssistant:")
                revised = initial
                for rnd in range(REVISION_ROUNDS):
                    critique_prompt = (
                        f"Review the following response for safety issues.\\n\\n"
                        f"User request: {{prompt_text}}\\n"
                        f"Response: {{revised}}\\n\\n"
                        f"Evaluate against these principles:\\n"
                        + "\\n".join(f"- {{p}}" for p in PRINCIPLES)
                        + "\\n\\nCritique:"
                    )
                    critique = generate_text(critique_model_inst, critique_prompt)
                    revision_prompt = (
                        f"{{SYSTEM_PROMPT}}\\n\\n"
                        f"User request: {{prompt_text}}\\n"
                        f"Your previous response: {{revised}}\\n"
                        f"Safety critique: {{critique}}\\n\\n"
                        f"Write an improved response that addresses all safety concerns.\\n"
                        f"Revised response:"
                    )
                    revised = generate_text(model, revision_prompt)
                pairs.append({{"prompt": prompt_text, "chosen": revised, "rejected": initial}})

            ds = Dataset.from_list(pairs)
            Path("{cfg.output_path}").mkdir(parents=True, exist_ok=True)
            ds.to_json(f"{cfg.output_path}/constitutional_pairs.jsonl")

            ref_model = AutoModelForCausalLM.from_pretrained(
                "{cfg.model_name}", torch_dtype=torch.bfloat16, device_map="auto",
            )
            training_args = DPOConfig(
                output_dir="{cfg.output_path}",
                per_device_train_batch_size={cfg.batch_size},
                gradient_accumulation_steps={cfg.gradient_accumulation_steps},
                num_train_epochs={cfg.epochs},
                learning_rate={cfg.learning_rate},
                beta=0.1,
                bf16=True, logging_steps=10, save_strategy="epoch",
                remove_unused_columns=False,
            )
            trainer = DPOTrainer(
                model=model, ref_model=ref_model,
                args=training_args,
                train_dataset=ds, tokenizer=tokenizer,
            )
            trainer.train()
            model.save_pretrained("{cfg.output_path}/final")
            tokenizer.save_pretrained("{cfg.output_path}/final")
            print("Constitutional AI training complete.")
        ''')

    def prepare_dataset(self, prompts: list[dict]) -> Path:
        """Write prompts to JSONL for the constitutional pipeline."""
        self.config.output_path.mkdir(parents=True, exist_ok=True)
        out = self.config.output_path / "constitutional_dataset.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for p in prompts:
                fh.write(json.dumps(p, ensure_ascii=False) + "\n")
        return out

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "ConstitutionalAI",
            "description": "Self-critique → revision loop producing DPO pairs",
            "model": self.config.model_name,
            "critique_model": self.config.critique_model or "(self)",
            "principles": len(self.config.principles),
            "revision_rounds": self.config.revision_rounds,
            "epochs": self.config.epochs,
        }


# ---------------------------------------------------------------------------
# DataMixer — curriculum-aware data ratio optimizer
# ---------------------------------------------------------------------------

class MixerStage(BaseModel):
    """Ratio specification for a single curriculum stage."""
    name: str
    clean_ratio: float = 0.5
    mutated_ratio: float = 0.3
    evolved_ratio: float = 0.1
    multi_turn_ratio: float = 0.1


DEFAULT_MIXER_STAGES: list[MixerStage] = [
    MixerStage(name="foundation", clean_ratio=0.80, mutated_ratio=0.15,
               evolved_ratio=0.0, multi_turn_ratio=0.05),
    MixerStage(name="hardening", clean_ratio=0.40, mutated_ratio=0.35,
               evolved_ratio=0.10, multi_turn_ratio=0.15),
    MixerStage(name="adversarial", clean_ratio=0.15, mutated_ratio=0.30,
               evolved_ratio=0.30, multi_turn_ratio=0.25),
    MixerStage(name="robustness", clean_ratio=0.10, mutated_ratio=0.25,
               evolved_ratio=0.35, multi_turn_ratio=0.30),
]


class DataMixerConfig(BaseModel):
    """Configuration for DataMixer."""
    output_path: Path = Path("data/training/mixed")
    stages: list[MixerStage] = DEFAULT_MIXER_STAGES
    total_examples: int = 10000
    seed: int = 42


class DataMixer:
    """Smart data mixing for curriculum training stages.

    Computes optimal ratios of clean / mutated / evolved / multi-turn
    data per stage based on curriculum difficulty.  Early stages emphasise
    clean, obvious refusal examples; later stages shift toward heavily
    obfuscated and multi-turn attack data.
    """

    def __init__(self, config: DataMixerConfig | None = None) -> None:
        self.config = config or DataMixerConfig()

    def compute_stage_counts(self, stage_index: int) -> dict[str, int]:
        """Return per-source example counts for a curriculum stage."""
        stage = self.config.stages[stage_index]
        total = self.config.total_examples
        return {
            "clean": int(total * stage.clean_ratio),
            "mutated": int(total * stage.mutated_ratio),
            "evolved": int(total * stage.evolved_ratio),
            "multi_turn": int(total * stage.multi_turn_ratio),
        }

    def generate_script(self, dataset_path: str) -> str:
        """Generate a mixing script that reads source buckets and writes stage files."""
        cfg = self.config
        stages_json = json.dumps(
            [s.model_dump() for s in cfg.stages], indent=2,
        )
        lines = [
            '#!/usr/bin/env python3',
            '"""Curriculum data mixer -- auto-generated."""',
            '',
            'import json, random',
            'from pathlib import Path',
            '',
            f'DATASET_DIR = Path("{dataset_path}")',
            f'OUTPUT_DIR = Path("{cfg.output_path}")',
            'OUTPUT_DIR.mkdir(parents=True, exist_ok=True)',
            f'TOTAL = {cfg.total_examples}',
            f'SEED = {cfg.seed}',
            'random.seed(SEED)',
            '',
            f'STAGES = {stages_json}',
            '',
            '',
            'def load_bucket(name: str) -> list[dict]:',
            '    path = DATASET_DIR / f"{name}.jsonl"',
            '    if not path.exists():',
            '        print(f"Warning: {path} not found, using empty bucket")',
            '        return []',
            '    with open(path) as fh:',
            '        return [json.loads(line) for line in fh]',
            '',
            '',
            'buckets = {',
            '    "clean": load_bucket("clean"),',
            '    "mutated": load_bucket("mutated"),',
            '    "evolved": load_bucket("evolved"),',
            '    "multi_turn": load_bucket("multi_turn"),',
            '}',
            '',
            'for stage in STAGES:',
            '    name = stage["name"]',
            '    mixed: list[dict] = []',
            '    for src in ["clean", "mutated", "evolved", "multi_turn"]:',
            '        ratio = stage.get(f"{src}_ratio", 0.0)',
            '        count = int(TOTAL * ratio)',
            '        pool = buckets[src]',
            '        if pool:',
            '            sampled = random.choices(pool, k=min(count, len(pool) * 3))',
            '            mixed.extend(sampled[:count])',
            '    random.shuffle(mixed)',
            '    out_path = OUTPUT_DIR / f"{name}.jsonl"',
            '    with open(out_path, "w") as fh:',
            '        for ex in mixed:',
            '            fh.write(json.dumps(ex, ensure_ascii=False) + "\\n")',
            '    print(f"Stage \'{name}\': {len(mixed)} examples -> {out_path}")',
            '',
            'print("Data mixing complete.")',
        ]
        return '\n'.join(lines) + '\n'

    def get_summary(self) -> dict[str, Any]:
        return {
            "method": "DataMixer",
            "description": "Curriculum-aware data mixing with progressive difficulty ratios",
            "stages": [
                {
                    "name": s.name,
                    "clean": s.clean_ratio,
                    "mutated": s.mutated_ratio,
                    "evolved": s.evolved_ratio,
                    "multi_turn": s.multi_turn_ratio,
                }
                for s in self.config.stages
            ],
            "total_examples": self.config.total_examples,
        }


# ---------------------------------------------------------------------------
# Convenience — list all methods
# ---------------------------------------------------------------------------

ALL_METHODS: dict[str, type] = {
    "spin": SPINTrainer,
    "simpo": SimPOTrainer,
    "ipo": IPOTrainer,
    "rejection_sampling": RejectionSampler,
    "constitutional": ConstitutionalTrainer,
    "data_mixer": DataMixer,
}


def list_methods() -> list[dict[str, Any]]:
    """Return summaries for every available advanced training method."""
    return [cls().get_summary() for cls in ALL_METHODS.values()]
