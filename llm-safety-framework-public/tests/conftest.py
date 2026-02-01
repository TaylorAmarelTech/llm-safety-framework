"""Pytest configuration and fixtures for LLM Safety Framework tests."""

import pytest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock


@pytest.fixture
def mock_llm_provider():
    """Create a mock LLM provider for testing."""
    provider = MagicMock()
    provider.generate = AsyncMock(return_value=(
        "This is a test response",
        150.0,  # latency_ms
        100,    # tokens
    ))
    return provider


@pytest.fixture
def sample_test_case():
    """Create a sample test case for testing."""
    return {
        "id": "test_001",
        "prompt": "Sample test prompt for safety testing",
        "category": "regulatory_evasion",
        "subcategory": "fee_renaming",
        "expected_outcome": "refuse",
        "difficulty": "medium",
        "corridor": "PH-SA",
    }


@pytest.fixture
def sample_test_run():
    """Create a sample test run result."""
    return {
        "id": 1,
        "run_id": "run_001",
        "test_id": "test_001",
        "model_name": "gpt-4o-mini",
        "is_harmful": False,
        "harm_score": 0.15,
        "evaluator": "llm_judge",
        "executed_at": datetime.now(),
        "latency_seconds": 1.5,
        "tokens_used": 250,
        "cost_usd": 0.001,
    }


@pytest.fixture
def sample_statistics():
    """Create sample statistics data."""
    return {
        "total_tests": 21000,
        "total_runs": 50000,
        "total_models": 6,
        "avg_harmful_rate": 0.15,
    }
