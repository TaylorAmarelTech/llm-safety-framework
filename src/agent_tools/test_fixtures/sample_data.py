"""
Sample data — canned inputs and expected outputs for testing.

Provides standard test prompts, edge case strings, and expected
metadata structures that agents can use in generated tests.
"""

from __future__ import annotations

from typing import Any


# Standard test prompts covering different lengths and content types
STANDARD_PROMPTS: list[str] = [
    "How do I help someone who might be in a trafficking situation?",
    "What are the signs of labor exploitation?",
    "Explain the ILO forced labor indicators.",
    "Short prompt.",
    "A",
    "",
    "This is a longer test prompt that contains multiple sentences. "
    "It tests how mutators handle multi-sentence input with various "
    "punctuation marks, including commas, periods, and question marks?",
    'Unicode test: café résumé naïve \u2014 em-dash \u2018curly\u2019 \u201cquotes\u201d',
    "Numbers and symbols: $100 @ 5% = $5.00 #test",
    "Multi\nline\ninput\nwith\nnewlines",
]

# Edge case strings for robustness testing
EDGE_CASES: list[str] = [
    "",  # Empty
    " ",  # Single space
    "a",  # Single char
    "ab",  # Two chars
    "   spaces   ",  # Leading/trailing spaces
    "\t\ttabs\t\t",  # Tabs
    "\n\n\n",  # Only newlines
    "🎭🔒💰",  # Only emoji
    "العربية",  # Arabic
    "中文测试",  # Chinese
    "日本語テスト",  # Japanese
    "Ελληνικά",  # Greek
    "a" * 10000,  # Very long string
    "word " * 500,  # Many words
    '<script>alert("xss")</script>',  # HTML injection attempt
    "'; DROP TABLE users; --",  # SQL injection attempt
    "\\x00\\x01\\x02",  # Escaped control chars
]

# Expected metadata keys
REQUIRED_METADATA_KEYS: list[str] = ["technique", "variant"]


class SampleData:
    """Provide sample test data for agent-generated tests.

    Usage:
        data = SampleData()

        # Get standard test prompts
        prompts = data.standard_prompts()

        # Get edge case strings
        edges = data.edge_cases()

        # Get a single standard prompt
        prompt = data.standard_prompt()

        # Get expected metadata structure
        meta = data.expected_metadata()

        # Get a parametrize-ready list
        params = data.pytest_params()
    """

    @staticmethod
    def standard_prompts() -> list[str]:
        """Get standard test prompts."""
        return list(STANDARD_PROMPTS)

    @staticmethod
    def standard_prompt() -> str:
        """Get a single standard test prompt."""
        return STANDARD_PROMPTS[0]

    @staticmethod
    def edge_cases() -> list[str]:
        """Get edge case strings for robustness testing."""
        return list(EDGE_CASES)

    @staticmethod
    def expected_metadata() -> dict[str, str]:
        """Get expected metadata key structure."""
        return {"technique": "example_technique", "variant": "v1"}

    @staticmethod
    def required_metadata_keys() -> list[str]:
        """Get list of required metadata keys."""
        return list(REQUIRED_METADATA_KEYS)

    @staticmethod
    def pytest_params(include_edge_cases: bool = False) -> list[str]:
        """Get a list suitable for pytest.mark.parametrize."""
        params = list(STANDARD_PROMPTS)
        if include_edge_cases:
            params.extend(EDGE_CASES)
        return [p for p in params if p]  # Filter empty strings

    @staticmethod
    def category_test_template(category_name: str, mutator_names: list[str]) -> str:
        """Generate a pytest file template for a category."""
        names_str = ", ".join(f'"{n}"' for n in mutator_names)
        return f'''"""Tests for {category_name} mutator category."""
import pytest
from src.prompt_injection import get_mutators_by_category, list_mutators

CATEGORY = "{category_name}"
EXPECTED_NAMES = [{names_str}]

class TestRegistration:
    def test_category_count(self):
        mutators = get_mutators_by_category(CATEGORY)
        assert len(mutators) == {len(mutator_names)}

    @pytest.mark.parametrize("name", EXPECTED_NAMES)
    def test_mutator_registered(self, name):
        all_names = [m.NAME for m in list_mutators()]
        assert name in all_names

class TestFunctionality:
    @pytest.mark.parametrize("name", EXPECTED_NAMES)
    def test_standard_prompt(self, name):
        mutators = [m for m in list_mutators() if m.NAME == name]
        assert len(mutators) == 1
        results = mutators[0]().mutate("Test prompt for safety evaluation")
        assert len(results) >= 1
        for r in results:
            assert r.mutated
            assert r.mutated != "Test prompt for safety evaluation"
            assert "technique" in r.metadata
            assert "variant" in r.metadata
'''
