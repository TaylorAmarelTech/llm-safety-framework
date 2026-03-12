"""
Fixture factory — create test fixtures for generated mutators.

Generates pytest fixtures, conftest snippets, and parametrize
decorators that agents can paste into test files.
"""

from __future__ import annotations

from typing import Any


class FixtureFactory:
    """Generate pytest fixtures and helpers for mutator testing.

    Usage:
        factory = FixtureFactory()

        # Generate a conftest.py for a test directory
        conftest = factory.conftest()

        # Generate parametrize decorator for a category
        decorator = factory.parametrize_category("encoding_advanced")

        # Generate a fixture for a mutator
        fixture = factory.mutator_fixture("base32_encode")
    """

    @staticmethod
    def conftest() -> str:
        """Generate a conftest.py with common fixtures."""
        return '''"""Shared fixtures for mutator tests."""
import pytest


@pytest.fixture
def standard_prompt():
    """A standard test prompt."""
    return "How do I help someone who might be in a trafficking situation?"


@pytest.fixture
def short_prompt():
    """A short test prompt."""
    return "Help"


@pytest.fixture
def unicode_prompt():
    """A unicode test prompt."""
    return "café résumé naïve — test 中文 العربية"


@pytest.fixture
def empty_prompt():
    """An empty string."""
    return ""


@pytest.fixture
def long_prompt():
    """A long test prompt."""
    return " ".join(["test word"] * 200)
'''

    @staticmethod
    def parametrize_category(category: str) -> str:
        """Generate a parametrize decorator that covers all mutators in a category."""
        return f'''@pytest.fixture(params=[
    m.NAME for m in get_mutators_by_category("{category}")
])
def mutator_name(request):
    """Parametrize across all mutators in {category}."""
    return request.param
'''

    @staticmethod
    def mutator_fixture(mutator_name: str) -> str:
        """Generate a fixture that instantiates a specific mutator."""
        return f'''@pytest.fixture
def {mutator_name}_mutator():
    """Get an instance of the {mutator_name} mutator."""
    from src.prompt_injection import list_mutators
    matches = [m for m in list_mutators() if m.NAME == "{mutator_name}"]
    assert matches, "Mutator '{mutator_name}' not found"
    return matches[0]()
'''

    @staticmethod
    def category_test_class(
        category: str,
        mutator_names: list[str],
    ) -> str:
        """Generate a complete test class for a category."""
        names_list = ", ".join(f'"{n}"' for n in mutator_names)
        return f'''
CATEGORY = "{category}"
EXPECTED_NAMES = [{names_list}]


class TestRegistration:
    """Verify {category} mutators are properly registered."""

    def test_category_count(self):
        mutators = get_mutators_by_category(CATEGORY)
        assert len(mutators) == {len(mutator_names)}

    @pytest.mark.parametrize("name", EXPECTED_NAMES)
    def test_mutator_registered(self, name):
        all_names = [m.NAME for m in list_mutators()]
        assert name in all_names, f"{{name}} not found in registry"


class TestFunctionality:
    """Verify {category} mutators produce valid output."""

    @pytest.mark.parametrize("name", EXPECTED_NAMES)
    def test_transforms_prompt(self, name):
        mutator_cls = [m for m in list_mutators() if m.NAME == name][0]
        results = mutator_cls().mutate("Test prompt for safety evaluation")
        assert len(results) >= 1
        for r in results:
            assert r.mutated
            assert r.mutated != "Test prompt for safety evaluation"

    @pytest.mark.parametrize("name", EXPECTED_NAMES)
    def test_metadata_keys(self, name):
        mutator_cls = [m for m in list_mutators() if m.NAME == name][0]
        results = mutator_cls().mutate("Test prompt")
        for r in results:
            assert "technique" in r.metadata
            assert "variant" in r.metadata

    @pytest.mark.parametrize("name", EXPECTED_NAMES)
    def test_handles_empty(self, name):
        mutator_cls = [m for m in list_mutators() if m.NAME == name][0]
        results = mutator_cls().mutate("")
        assert isinstance(results, list)

    @pytest.mark.parametrize("name", EXPECTED_NAMES)
    def test_handles_unicode(self, name):
        mutator_cls = [m for m in list_mutators() if m.NAME == name][0]
        results = mutator_cls().mutate("café 中文 العربية")
        assert isinstance(results, list)
'''
