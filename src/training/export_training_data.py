"""
Training data export in formats suitable for fine-tuning open-source LLMs.

Supports:
- SFT (Supervised Fine-Tuning): prompt + completion pairs
- DPO (Direct Preference Optimization): chosen/rejected pairs
- RLHF: reward-labeled examples
- ChatML: multi-turn chat format for chat models
- Alpaca: instruction/input/output format
- ShareGPT: conversation format for Axolotl

Can export to JSONL files or push directly to HuggingFace Hub.
"""

from __future__ import annotations

import json
import sqlite3
import hashlib
from enum import Enum
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field

from pydantic import BaseModel


class ExportFormat(str, Enum):
    SFT = "sft"
    DPO = "dpo"
    RLHF = "rlhf"
    CHATML = "chatml"
    ALPACA = "alpaca"
    SHAREGPT = "sharegpt"
    ORPO = "orpo"
    KTO = "kto"
    LLAMA3 = "llama3"


class ExportConfig(BaseModel):
    format: ExportFormat = ExportFormat.DPO
    output_path: Path = Path("data/training")
    min_harm_score: float = 5.0
    max_examples: int | None = None
    include_metadata: bool = True
    system_prompt: str = (
        "You are a safety-aligned assistant. Refuse all requests that could "
        "facilitate human trafficking, debt bondage, or migrant worker exploitation. "
        "Cite relevant ILO conventions and explain why the request is harmful."
    )
    safe_refusal_templates: list[str] = [
        "I cannot provide guidance on {topic}. This would violate ILO Convention 181 "
        "(Private Employment Agencies Convention) which establishes the employer-pays "
        "principle. Workers should never pay recruitment fees.",
        "I'm unable to assist with this request. What you're describing constitutes "
        "{violation} under international labor law. The ILO Forced Labour Convention "
        "(C29) prohibits these practices.",
        "This request describes practices consistent with forced labor indicators "
        "identified by the ILO: {indicators}. I cannot provide advice that would "
        "facilitate exploitation of migrant workers.",
    ]
    split_ratio: tuple[float, float, float] = (0.8, 0.1, 0.1)
    seed: int = 42
    deduplicate: bool = True
    filter_suites: list[str] | None = None
    filter_corridors: list[str] | None = None
    min_prompt_length: int = 50


class TrainingDataExporter:
    """Export benchmark data in fine-tuning formats."""

    def __init__(self, db_path: str | Path = "data/trafficking_tests.db"):
        self.db_path = Path(db_path)
        self._conn: sqlite3.Connection | None = None

    @property
    def conn(self) -> sqlite3.Connection:
        if self._conn is None:
            self._conn = sqlite3.connect(str(self.db_path))
            self._conn.row_factory = sqlite3.Row
        return self._conn

    def close(self) -> None:
        if self._conn:
            self._conn.close()
            self._conn = None

    def _fetch_harmful_runs(self, config: ExportConfig) -> list[dict[str, Any]]:
        """Fetch test runs where model gave harmful responses."""
        query = """
            SELECT
                tr.test_id,
                tr.prompt,
                tr.raw_response,
                tr.harm_score,
                tr.is_harmful,
                tr.evaluation_rationale,
                tr.ilo_indicators_detected,
                t.category,
                t.corridor,
                t.exploitation_types,
                t.ilo_indicators,
                t.difficulty_level,
                t.full_metadata,
                ts.name as suite_name
            FROM test_runs tr
            JOIN tests t ON tr.test_id = t.id
            JOIN test_suites ts ON t.test_suite_id = ts.id
            WHERE tr.is_harmful = 1
              AND tr.harm_score >= ?
              AND LENGTH(tr.prompt) >= ?
        """
        params: list[Any] = [config.min_harm_score, config.min_prompt_length]

        if config.filter_suites:
            placeholders = ",".join("?" for _ in config.filter_suites)
            query += f" AND ts.name IN ({placeholders})"
            params.extend(config.filter_suites)

        if config.filter_corridors:
            placeholders = ",".join("?" for _ in config.filter_corridors)
            query += f" AND t.corridor IN ({placeholders})"
            params.extend(config.filter_corridors)

        query += " ORDER BY tr.harm_score DESC"

        if config.max_examples:
            query += " LIMIT ?"
            params.append(config.max_examples)

        cursor = self.conn.cursor()
        cursor.execute(query, params)
        rows = [dict(row) for row in cursor.fetchall()]

        if config.deduplicate:
            seen: set[str] = set()
            unique: list[dict[str, Any]] = []
            for row in rows:
                h = hashlib.md5(row["prompt"].encode()).hexdigest()
                if h not in seen:
                    seen.add(h)
                    unique.append(row)
            rows = unique

        return rows

    def _fetch_all_tests(self, config: ExportConfig) -> list[dict[str, Any]]:
        """Fetch all tests (for SFT with generated safe responses)."""
        query = """
            SELECT
                t.id as test_id,
                t.prompt,
                t.category,
                t.corridor,
                t.exploitation_types,
                t.ilo_indicators,
                t.difficulty_level,
                t.full_metadata,
                ts.name as suite_name
            FROM tests t
            JOIN test_suites ts ON t.test_suite_id = ts.id
            WHERE LENGTH(t.prompt) >= ?
        """
        params: list[Any] = [config.min_prompt_length]

        if config.filter_suites:
            placeholders = ",".join("?" for _ in config.filter_suites)
            query += f" AND ts.name IN ({placeholders})"
            params.extend(config.filter_suites)

        query += " ORDER BY RANDOM()"

        if config.max_examples:
            query += " LIMIT ?"
            params.append(config.max_examples)

        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]

    def _generate_safe_refusal(self, row: dict[str, Any], config: ExportConfig) -> str:
        """Generate a safe refusal response for a harmful prompt."""
        indicators = []
        if row.get("ilo_indicators"):
            try:
                indicators = json.loads(row["ilo_indicators"])
            except (json.JSONDecodeError, TypeError):
                pass

        category = row.get("category", "exploitation")

        topic_map = {
            "debt_bondage": "debt bondage schemes",
            "recruitment_fees": "illegal recruitment fee structures",
            "document_retention": "passport/document confiscation",
            "wage_theft": "wage withholding or theft",
            "movement_restriction": "restricting workers' freedom of movement",
            "regulatory_evasion": "evading labor regulations",
            "financial_obfuscation": "disguising illegal recruitment fees",
            "coercion_manipulation": "psychological coercion of workers",
            "moral_religious_framing": "using religious justification for exploitation",
        }

        topic = topic_map.get(category, f"practices related to {category}")
        violation = f"forced labor / {category.replace('_', ' ')}"
        indicator_str = ", ".join(indicators[:3]) if indicators else "debt bondage, deception"

        import random
        random.seed(hash(row.get("prompt", "")))
        template = random.choice(config.safe_refusal_templates)

        return template.format(
            topic=topic,
            violation=violation,
            indicators=indicator_str,
        )

    def export_dpo(self, config: ExportConfig | None = None) -> Path:
        """Export DPO (Direct Preference Optimization) pairs.

        Format: {"prompt": ..., "chosen": safe_refusal, "rejected": harmful_response}
        """
        config = config or ExportConfig(format=ExportFormat.DPO)
        rows = self._fetch_harmful_runs(config)
        output = config.output_path / "dpo_pairs.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            example = {
                "prompt": row["prompt"],
                "chosen": safe_response,
                "rejected": row["raw_response"],
            }
            if config.include_metadata:
                example["metadata"] = {
                    "test_id": row["test_id"],
                    "harm_score": row["harm_score"],
                    "category": row["category"],
                    "corridor": row.get("corridor", ""),
                    "suite": row.get("suite_name", ""),
                }
            examples.append(example)

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_sft(self, config: ExportConfig | None = None) -> Path:
        """Export SFT (Supervised Fine-Tuning) examples.

        Format: {"messages": [{"role": "system", ...}, {"role": "user", ...}, {"role": "assistant", ...}]}
        """
        config = config or ExportConfig(format=ExportFormat.SFT)
        rows = self._fetch_all_tests(config)
        output = config.output_path / "sft_examples.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            example = {
                "messages": [
                    {"role": "system", "content": config.system_prompt},
                    {"role": "user", "content": row["prompt"]},
                    {"role": "assistant", "content": safe_response},
                ]
            }
            if config.include_metadata:
                example["metadata"] = {
                    "test_id": row["test_id"],
                    "category": row["category"],
                    "suite": row.get("suite_name", ""),
                }
            examples.append(example)

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_chatml(self, config: ExportConfig | None = None) -> Path:
        """Export in ChatML format for models using <|im_start|> tokens.

        Format compatible with Mistral, Qwen, and other ChatML models.
        """
        config = config or ExportConfig(format=ExportFormat.CHATML)
        rows = self._fetch_all_tests(config)
        output = config.output_path / "chatml_examples.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            text = (
                f"<|im_start|>system\n{config.system_prompt}<|im_end|>\n"
                f"<|im_start|>user\n{row['prompt']}<|im_end|>\n"
                f"<|im_start|>assistant\n{safe_response}<|im_end|>"
            )
            example = {"text": text}
            if config.include_metadata:
                example["metadata"] = {
                    "test_id": row["test_id"],
                    "category": row["category"],
                }
            examples.append(example)

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_alpaca(self, config: ExportConfig | None = None) -> Path:
        """Export in Alpaca instruction format.

        Format: {"instruction": ..., "input": ..., "output": ...}
        """
        config = config or ExportConfig(format=ExportFormat.ALPACA)
        rows = self._fetch_all_tests(config)
        output = config.output_path / "alpaca_examples.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            example = {
                "instruction": (
                    "You are a safety-aligned assistant. Evaluate the following "
                    "request and respond appropriately, refusing harmful requests "
                    "related to human trafficking or labor exploitation."
                ),
                "input": row["prompt"],
                "output": safe_response,
            }
            examples.append(example)

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_sharegpt(self, config: ExportConfig | None = None) -> Path:
        """Export in ShareGPT format for Axolotl training.

        Format: {"conversations": [{"from": "system", ...}, {"from": "human", ...}, {"from": "gpt", ...}]}
        """
        config = config or ExportConfig(format=ExportFormat.SHAREGPT)
        rows = self._fetch_all_tests(config)
        output = config.output_path / "sharegpt_examples.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            example = {
                "conversations": [
                    {"from": "system", "value": config.system_prompt},
                    {"from": "human", "value": row["prompt"]},
                    {"from": "gpt", "value": safe_response},
                ]
            }
            examples.append(example)

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_rlhf(self, config: ExportConfig | None = None) -> Path:
        """Export RLHF reward-labeled examples.

        Format: {"prompt": ..., "response": ..., "reward": float, "label": "safe"|"harmful"}
        """
        config = config or ExportConfig(format=ExportFormat.RLHF)
        rows = self._fetch_harmful_runs(config)
        output = config.output_path / "rlhf_examples.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            # Harmful example (negative reward)
            examples.append({
                "prompt": row["prompt"],
                "response": row["raw_response"],
                "reward": -1.0 * (row["harm_score"] / 10.0),
                "label": "harmful",
            })
            # Safe example (positive reward)
            examples.append({
                "prompt": row["prompt"],
                "response": safe_response,
                "reward": 1.0,
                "label": "safe",
            })

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_orpo(self, config: ExportConfig | None = None) -> Path:
        """Export ORPO (Odds Ratio Preference Optimization) pairs.

        Same data shape as DPO but used with ORPOTrainer which doesn't need
        a reference model. Single-stage training.
        """
        config = config or ExportConfig(format=ExportFormat.ORPO)
        rows = self._fetch_harmful_runs(config)
        output = config.output_path / "orpo_pairs.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            examples.append({
                "prompt": row["prompt"],
                "chosen": safe_response,
                "rejected": row["raw_response"],
            })

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_kto(self, config: ExportConfig | None = None) -> Path:
        """Export KTO (Kahneman-Tversky Optimization) examples.

        Binary good/bad labels per response, not paired. Lower data requirements
        than DPO since responses don't need to be paired.
        Format: {"prompt": ..., "completion": ..., "label": true|false}
        """
        config = config or ExportConfig(format=ExportFormat.KTO)
        rows = self._fetch_harmful_runs(config)
        output = config.output_path / "kto_examples.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            # Good example (safe refusal)
            examples.append({
                "prompt": row["prompt"],
                "completion": safe_response,
                "label": True,
            })
            # Bad example (harmful response)
            examples.append({
                "prompt": row["prompt"],
                "completion": row["raw_response"],
                "label": False,
            })

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export_llama3(self, config: ExportConfig | None = None) -> Path:
        """Export in Llama 3 native chat template format.

        Uses <|begin_of_text|>, <|start_header_id|>, <|end_header_id|>, <|eot_id|>
        instead of ChatML's <|im_start|>/<|im_end|>.
        """
        config = config or ExportConfig(format=ExportFormat.LLAMA3)
        rows = self._fetch_all_tests(config)
        output = config.output_path / "llama3_examples.jsonl"
        output.parent.mkdir(parents=True, exist_ok=True)

        examples = []
        for row in rows:
            safe_response = self._generate_safe_refusal(row, config)
            text = (
                "<|begin_of_text|>"
                "<|start_header_id|>system<|end_header_id|>\n\n"
                f"{config.system_prompt}<|eot_id|>"
                "<|start_header_id|>user<|end_header_id|>\n\n"
                f"{row['prompt']}<|eot_id|>"
                "<|start_header_id|>assistant<|end_header_id|>\n\n"
                f"{safe_response}<|eot_id|>"
            )
            examples.append({"text": text})

        with open(output, "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")

        return output

    def export(self, config: ExportConfig | None = None) -> Path:
        """Export in the configured format."""
        config = config or ExportConfig()
        exporters = {
            ExportFormat.SFT: self.export_sft,
            ExportFormat.DPO: self.export_dpo,
            ExportFormat.RLHF: self.export_rlhf,
            ExportFormat.CHATML: self.export_chatml,
            ExportFormat.ALPACA: self.export_alpaca,
            ExportFormat.SHAREGPT: self.export_sharegpt,
            ExportFormat.ORPO: self.export_orpo,
            ExportFormat.KTO: self.export_kto,
            ExportFormat.LLAMA3: self.export_llama3,
        }
        return exporters[config.format](config)

    def export_all_formats(self, config: ExportConfig | None = None) -> dict[str, Path]:
        """Export in all formats at once."""
        config = config or ExportConfig()
        results = {}
        for fmt in ExportFormat:
            cfg = config.model_copy(update={"format": fmt})
            results[fmt.value] = self.export(cfg)
        return results

    def split_dataset(
        self, input_path: Path, config: ExportConfig | None = None
    ) -> dict[str, Path]:
        """Split a JSONL file into train/val/test splits."""
        config = config or ExportConfig()
        import random

        random.seed(config.seed)

        with open(input_path, encoding="utf-8") as f:
            lines = f.readlines()

        random.shuffle(lines)
        n = len(lines)
        train_end = int(n * config.split_ratio[0])
        val_end = train_end + int(n * config.split_ratio[1])

        splits = {
            "train": lines[:train_end],
            "val": lines[train_end:val_end],
            "test": lines[val_end:],
        }

        result = {}
        stem = input_path.stem
        for split_name, split_lines in splits.items():
            out = input_path.parent / f"{stem}_{split_name}.jsonl"
            with open(out, "w", encoding="utf-8") as f:
                f.writelines(split_lines)
            result[split_name] = out

        return result

    def push_to_hub(
        self,
        dataset_path: Path,
        repo_id: str,
        token: str | None = None,
        private: bool = True,
    ) -> str:
        """Push exported dataset to HuggingFace Hub.

        Requires: pip install datasets huggingface_hub
        Returns the repo URL.
        """
        try:
            from datasets import load_dataset
            from huggingface_hub import HfApi
        except ImportError:
            raise ImportError(
                "HuggingFace integration requires: pip install datasets huggingface_hub"
            )

        ds = load_dataset("json", data_files=str(dataset_path))

        api = HfApi(token=token)
        api.create_repo(repo_id, repo_type="dataset", private=private, exist_ok=True)
        ds["train"].push_to_hub(repo_id, token=token, private=private)

        return f"https://huggingface.co/datasets/{repo_id}"

    def get_export_stats(self, config: ExportConfig | None = None) -> dict[str, Any]:
        """Get statistics about what would be exported."""
        config = config or ExportConfig()

        cursor = self.conn.cursor()

        # Total harmful runs
        cursor.execute(
            "SELECT COUNT(*) FROM test_runs WHERE is_harmful = 1 AND harm_score >= ?",
            [config.min_harm_score],
        )
        total_harmful = cursor.fetchone()[0]

        # Total tests
        cursor.execute("SELECT COUNT(*) FROM tests WHERE LENGTH(prompt) >= ?",
                       [config.min_prompt_length])
        total_tests = cursor.fetchone()[0]

        # By suite
        cursor.execute("""
            SELECT ts.name, COUNT(*) FROM test_runs tr
            JOIN tests t ON tr.test_id = t.id
            JOIN test_suites ts ON t.test_suite_id = ts.id
            WHERE tr.is_harmful = 1 AND tr.harm_score >= ?
            GROUP BY ts.name ORDER BY COUNT(*) DESC
        """, [config.min_harm_score])
        by_suite = {row[0]: row[1] for row in cursor.fetchall()}

        # By category
        cursor.execute("""
            SELECT t.category, COUNT(*) FROM test_runs tr
            JOIN tests t ON tr.test_id = t.id
            WHERE tr.is_harmful = 1 AND tr.harm_score >= ?
            GROUP BY t.category ORDER BY COUNT(*) DESC
        """, [config.min_harm_score])
        by_category = {row[0]: row[1] for row in cursor.fetchall()}

        return {
            "total_harmful_runs": total_harmful,
            "total_tests_available": total_tests,
            "dpo_pairs_available": total_harmful,
            "sft_examples_available": total_tests,
            "by_suite": by_suite,
            "by_category": by_category,
            "min_harm_score": config.min_harm_score,
        }
