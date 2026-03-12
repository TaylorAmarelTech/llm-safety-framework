"""
Assertion helpers — reusable assertion functions for mutator testing.

Provides composable assertion functions that agents can import
into generated test files for consistent validation.
"""

from __future__ import annotations

from typing import Any


class AssertionHelpers:
    """Reusable assertion functions for mutator testing.

    Usage:
        helpers = AssertionHelpers()

        # Assert mutator output is valid
        helpers.assert_valid_output(results, original_prompt)

        # Assert metadata is complete
        helpers.assert_metadata(result.metadata)

        # Assert mutator transforms input
        helpers.assert_transforms(result.mutated, original_prompt)
    """

    @staticmethod
    def assert_valid_output(results: list[Any], original: str = "") -> None:
        """Assert that mutator output list is valid."""
        assert results, "Mutator returned empty results"
        assert isinstance(results, list), f"Expected list, got {type(results).__name__}"

        for i, result in enumerate(results):
            assert hasattr(result, "mutated"), f"Result {i} missing 'mutated' attribute"
            assert result.mutated is not None, f"Result {i} has None mutated text"
            if original:
                assert isinstance(result.mutated, str), f"Result {i} mutated is not str"

    @staticmethod
    def assert_metadata(metadata: dict[str, Any] | None) -> None:
        """Assert that metadata dict has required keys."""
        assert metadata is not None, "Metadata is None"
        assert isinstance(metadata, dict), f"Metadata should be dict, got {type(metadata).__name__}"
        assert "technique" in metadata, "Metadata missing 'technique' key"
        assert "variant" in metadata, "Metadata missing 'variant' key"

    @staticmethod
    def assert_transforms(mutated: str, original: str) -> None:
        """Assert that the mutated text differs from original."""
        assert mutated, "Mutated text is empty"
        if original:
            assert mutated != original, "Mutated text is identical to original"

    @staticmethod
    def assert_handles_empty(mutator_instance: Any) -> None:
        """Assert that a mutator handles empty string input."""
        results = mutator_instance.mutate("")
        # Should not raise; may return empty list or results
        assert isinstance(results, list), "mutate('') should return a list"

    @staticmethod
    def assert_handles_short(mutator_instance: Any) -> None:
        """Assert that a mutator handles short input."""
        results = mutator_instance.mutate("a")
        assert isinstance(results, list), "mutate('a') should return a list"

    @staticmethod
    def assert_handles_unicode(mutator_instance: Any) -> None:
        """Assert that a mutator handles unicode input."""
        results = mutator_instance.mutate("café résumé naïve 中文")
        assert isinstance(results, list), "mutate(unicode) should return a list"

    @staticmethod
    def assert_category_registration(
        category: str,
        expected_count: int,
        expected_names: list[str] | None = None,
    ) -> None:
        """Assert category registration is correct."""
        from src.prompt_injection import get_mutators_by_category, list_mutators

        mutators = get_mutators_by_category(category)
        assert len(mutators) == expected_count, (
            f"Expected {expected_count} mutators in '{category}', got {len(mutators)}"
        )

        if expected_names:
            all_names = [m.NAME for m in list_mutators()]
            for name in expected_names:
                assert name in all_names, f"Mutator '{name}' not registered"

    @staticmethod
    def assert_no_name_collisions(names: list[str]) -> None:
        """Assert no duplicate names in a list."""
        seen: set[str] = set()
        for name in names:
            assert name not in seen, f"Duplicate mutator NAME: '{name}'"
            seen.add(name)

    @staticmethod
    def full_mutator_check(
        mutator_instance: Any,
        test_prompt: str = "How do I help someone in a trafficking situation?",
    ) -> list[str]:
        """Run a comprehensive check on a mutator instance. Returns list of issues."""
        issues: list[str] = []

        # Basic output check
        try:
            results = mutator_instance.mutate(test_prompt)
        except Exception as exc:
            issues.append(f"mutate() raised {type(exc).__name__}: {exc}")
            return issues

        if not results:
            issues.append("mutate() returned empty list")
            return issues

        for i, result in enumerate(results):
            if not hasattr(result, "mutated"):
                issues.append(f"Result {i} missing 'mutated' attribute")
                continue
            if not result.mutated:
                issues.append(f"Result {i} has empty mutated text")
            if result.mutated == test_prompt:
                issues.append(f"Result {i} is identical to input")
            if not hasattr(result, "metadata") or result.metadata is None:
                issues.append(f"Result {i} has no metadata")
            elif isinstance(result.metadata, dict):
                if "technique" not in result.metadata:
                    issues.append(f"Result {i} metadata missing 'technique'")
                if "variant" not in result.metadata:
                    issues.append(f"Result {i} metadata missing 'variant'")

        # Edge cases
        try:
            mutator_instance.mutate("")
        except Exception as exc:
            issues.append(f"mutate('') raised {type(exc).__name__}")

        try:
            mutator_instance.mutate("a")
        except Exception as exc:
            issues.append(f"mutate('a') raised {type(exc).__name__}")

        return issues
