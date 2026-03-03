"""Tests for the spinning pipeline package."""

import json
import tempfile
from pathlib import Path

import pytest

from src.spinning.local_spinner import LocalSpinner
from src.spinning.custom_augmenter import CustomAugmenter
from src.spinning.attack_augmenter import AttackAugmenter
from src.spinning.storage import SpinStorage
from src.spinning.pipeline import PipelineManager
from src.spinning.models import SpinJob, SpinType


class TestLocalSpinner:
    """Test spintax expansion, regex, and char padding."""

    def test_simple_spintax(self):
        results = LocalSpinner.expand_spintax("{Hello|Hi} world", count=5)
        assert len(results) <= 5
        for r in results:
            assert r in ["Hello world", "Hi world"]

    def test_multi_group_spintax(self):
        results = LocalSpinner.expand_spintax("{A|B} {X|Y}", count=10)
        assert len(results) <= 4  # max 4 unique combos
        valid = {"A X", "A Y", "B X", "B Y"}
        for r in results:
            assert r in valid

    def test_nested_like_spintax(self):
        # Our regex-based approach handles nested braces iteratively
        results = LocalSpinner.expand_spintax("{Hello|Hi} {world|{there|you}}", count=20)
        assert len(results) > 0

    def test_no_spintax(self):
        results = LocalSpinner.expand_spintax("No spintax here", count=5)
        assert results == ["No spintax here"]

    def test_count_combinations(self):
        assert LocalSpinner.count_spintax_combinations("{A|B} {X|Y|Z}") == 6
        assert LocalSpinner.count_spintax_combinations("No spintax") == 1
        assert LocalSpinner.count_spintax_combinations("{1|2|3}") == 3

    def test_regex_replace(self):
        prompts = ["The worker fee is $500", "Pay the worker fee of $1000"]
        patterns = [{"find": r"worker fee", "replace": "processing charge"}]
        results = LocalSpinner.regex_replace(prompts, patterns)
        assert results == [
            "The processing charge is $500",
            "Pay the processing charge of $1000",
        ]

    def test_regex_replace_with_regex(self):
        prompts = ["Call 555-1234 now"]
        patterns = [{"find": r"\d{3}-\d{4}", "replace": "XXX-XXXX"}]
        results = LocalSpinner.regex_replace(prompts, patterns)
        assert results == ["Call XXX-XXXX now"]

    def test_regex_empty_patterns(self):
        prompts = ["unchanged"]
        results = LocalSpinner.regex_replace(prompts, [])
        assert results == ["unchanged"]

    def test_char_padding_prefix(self):
        prompts = ["test"]
        results = LocalSpinner.char_padding(prompts, padding_chars=".", padding_count=3)
        assert results == ["...test"]

    def test_char_padding_trailing(self):
        prompts = ["test"]
        results = LocalSpinner.char_padding(prompts, trailing_chars="!!!")
        assert results == ["test!!!"]

    def test_char_padding_zero_width(self):
        prompts = ["ab"]
        results = LocalSpinner.char_padding(prompts, insert_zero_width=True)
        assert '\u200b' in results[0]
        assert len(results[0]) > len("ab")

    def test_char_padding_combined(self):
        prompts = ["test"]
        results = LocalSpinner.char_padding(
            prompts, padding_chars=">>", padding_count=2, trailing_chars="<<"
        )
        assert results == [">>>>test<<"]


class TestCustomAugmenter:
    """Test custom user-defined augmentation."""

    def test_prefix(self):
        result = CustomAugmenter.augment(["hello"], prefix="Say: ")
        assert result == ["Say: hello"]

    def test_suffix(self):
        result = CustomAugmenter.augment(["hello"], suffix=" please")
        assert result == ["hello please"]

    def test_find_replace(self):
        result = CustomAugmenter.augment(
            ["the worker"],
            find_replace=[{"find": "worker", "replace": "employee"}],
        )
        assert result == ["the employee"]

    def test_combined(self):
        result = CustomAugmenter.augment(
            ["old text"],
            prefix="Start: ",
            suffix=" :End",
            find_replace=[{"find": "old", "replace": "new"}],
        )
        assert result == ["Start: new text :End"]

    def test_empty(self):
        result = CustomAugmenter.augment(["unchanged"])
        assert result == ["unchanged"]

    def test_batch(self):
        result = CustomAugmenter.augment(
            ["a", "b", "c"],
            prefix="x",
        )
        assert result == ["xa", "xb", "xc"]


class TestAttackAugmenter:
    """Test attack strategy augmentation."""

    def test_available_check(self):
        aug = AttackAugmenter()
        # available depends on whether AttackRegistry is importable
        assert isinstance(aug.available, bool)

    def test_get_strategies(self):
        aug = AttackAugmenter()
        strategies = aug.get_strategies()
        assert len(strategies) > 0
        assert all("id" in s for s in strategies)

    def test_augment_fallback(self):
        aug = AttackAugmenter()
        result = aug.augment("test prompt", ["business_framing"])
        assert "business" in result.lower() or "test prompt" in result

    def test_augment_batch(self):
        aug = AttackAugmenter()
        results = aug.augment_batch(
            ["prompt 1", "prompt 2"],
            ["urgency_creation"],
        )
        assert len(results) == 2
        assert all("original" in r for r in results)
        assert all("mutated" in r for r in results)


class TestSpinStorage:
    """Test JSON file storage for spin jobs."""

    @pytest.fixture
    def storage(self, tmp_path):
        return SpinStorage(str(tmp_path / "pipeline"))

    def test_save_and_load_job(self, storage):
        from datetime import datetime
        job = SpinJob(
            id="test-job-1",
            type=SpinType.SPINTAX,
            created_at=datetime.now(),
            config={"template": "{A|B}"},
            prompts=["A", "B"],
        )
        storage.save_job(job)
        loaded = storage.load_job("test-job-1")
        assert loaded is not None
        assert loaded.id == "test-job-1"
        assert loaded.type == SpinType.SPINTAX
        assert loaded.prompts == ["A", "B"]

    def test_list_jobs(self, storage):
        from datetime import datetime
        for i in range(3):
            job = SpinJob(
                id=f"job-{i}",
                type=SpinType.REGEX,
                created_at=datetime.now(),
                config={},
                prompts=[f"prompt-{i}"],
            )
            storage.save_job(job)
        jobs = storage.list_jobs()
        assert len(jobs) == 3

    def test_delete_job(self, storage):
        from datetime import datetime
        job = SpinJob(
            id="delete-me",
            type=SpinType.CUSTOM,
            created_at=datetime.now(),
            config={},
            prompts=["x"],
        )
        storage.save_job(job)
        assert storage.delete_job("delete-me") is True
        assert storage.load_job("delete-me") is None
        assert storage.delete_job("delete-me") is False

    def test_pipeline_config(self, storage):
        config = storage.get_pipeline_config()
        assert isinstance(config, dict)

        storage.save_pipeline_config({"disabled_sets": ["set1"]})
        config = storage.get_pipeline_config()
        assert config["disabled_sets"] == ["set1"]

    def test_active_pipeline(self, storage):
        assert storage.load_active_pipeline() is None

        pipeline = {
            "built_at": "2026-01-01T00:00:00",
            "total": 2,
            "prompts": [
                {"text": "prompt 1", "source": "test"},
                {"text": "prompt 2", "source": "test"},
            ],
        }
        storage.save_active_pipeline(pipeline)
        loaded = storage.load_active_pipeline()
        assert loaded is not None
        assert loaded["total"] == 2


class TestPipelineManager:
    """Test pipeline orchestration."""

    @pytest.fixture
    def pipeline_env(self, tmp_path):
        """Set up a temp environment with sample prompts."""
        data_dir = tmp_path / "data"
        data_dir.mkdir()
        pipeline_dir = tmp_path / "pipeline"

        # Create sample prompts
        prompts = {
            "test_suites": {
                "suite_a": [
                    {"prompt": "Test prompt A1", "category": "test"},
                    {"prompt": "Test prompt A2", "category": "test"},
                ],
                "suite_b": [
                    {"prompt": "Test prompt B1", "category": "test"},
                ],
            }
        }
        with open(data_dir / "sample_test_prompts.json", 'w') as f:
            json.dump(prompts, f)

        return data_dir, pipeline_dir

    def test_build_pipeline(self, pipeline_env):
        data_dir, pipeline_dir = pipeline_env
        pm = PipelineManager(str(data_dir), str(pipeline_dir))
        result = pm.build()
        assert result["total"] == 3
        assert len(result["sources"]) == 2

    def test_build_with_filter(self, pipeline_env):
        data_dir, pipeline_dir = pipeline_env
        pm = PipelineManager(str(data_dir), str(pipeline_dir))
        result = pm.build(prompt_set_ids=["suite_a"])
        assert result["total"] == 2

    def test_build_deduplication(self, pipeline_env):
        data_dir, pipeline_dir = pipeline_env
        # Add duplicate prompt
        prompts_file = data_dir / "sample_test_prompts.json"
        with open(prompts_file, 'r') as f:
            data = json.load(f)
        data["test_suites"]["suite_a"].append(
            {"prompt": "Test prompt A1", "category": "test"}  # duplicate
        )
        with open(prompts_file, 'w') as f:
            json.dump(data, f)

        pm = PipelineManager(str(data_dir), str(pipeline_dir))
        result = pm.build(deduplicate=True)
        assert result["total"] == 3  # deduped

    def test_get_status(self, pipeline_env):
        data_dir, pipeline_dir = pipeline_env
        pm = PipelineManager(str(data_dir), str(pipeline_dir))

        assert pm.get_status() is None
        pm.build()
        status = pm.get_status()
        assert status is not None
        assert status["total"] == 3

    def test_get_prompts_paginated(self, pipeline_env):
        data_dir, pipeline_dir = pipeline_env
        pm = PipelineManager(str(data_dir), str(pipeline_dir))
        pm.build()

        page = pm.get_prompts(limit=2, offset=0)
        assert len(page["prompts"]) == 2
        assert page["total"] == 3

        page2 = pm.get_prompts(limit=2, offset=2)
        assert len(page2["prompts"]) == 1

    def test_get_all_prompts(self, pipeline_env):
        data_dir, pipeline_dir = pipeline_env
        pm = PipelineManager(str(data_dir), str(pipeline_dir))
        pm.build()

        all_prompts = pm.get_all_prompts()
        assert len(all_prompts) == 3

    def test_includes_spun_prompts(self, pipeline_env):
        data_dir, pipeline_dir = pipeline_env
        pm = PipelineManager(str(data_dir), str(pipeline_dir))

        # Add a spin job
        storage = SpinStorage(str(pipeline_dir))
        from datetime import datetime
        job = SpinJob(
            id="spun-1",
            type=SpinType.SPINTAX,
            created_at=datetime.now(),
            config={},
            prompts=["Spun prompt 1", "Spun prompt 2"],
        )
        storage.save_job(job)

        result = pm.build(include_spun=True)
        assert result["total"] == 5  # 3 from sets + 2 spun
