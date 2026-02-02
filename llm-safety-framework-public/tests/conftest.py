"""Pytest configuration and fixtures for LLM Safety Framework tests."""

import pytest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# =============================================================================
# LLM Provider Fixtures
# =============================================================================

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
def mock_llm_provider_harmful():
    """Create a mock LLM provider that returns harmful content."""
    provider = MagicMock()
    provider.generate = AsyncMock(return_value=(
        "Here is how to exploit workers: [harmful content]",
        200.0,
        150,
    ))
    return provider


@pytest.fixture
def mock_llm_provider_error():
    """Create a mock LLM provider that raises errors."""
    provider = MagicMock()
    provider.generate = AsyncMock(side_effect=Exception("API rate limit exceeded"))
    return provider


# =============================================================================
# Test Case Fixtures
# =============================================================================

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
def sample_test_cases():
    """Create multiple sample test cases."""
    return [
        {
            "id": f"test_{i:03d}",
            "prompt": f"Test prompt {i}",
            "category": ["regulatory_evasion", "debt_bondage", "coercion"][i % 3],
            "difficulty": ["easy", "medium", "hard"][i % 3],
            "corridor": ["PH-SA", "NP-QA", "BD-MY"][i % 3],
        }
        for i in range(10)
    ]


# =============================================================================
# Test Run Fixtures
# =============================================================================

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
def sample_test_runs():
    """Create multiple sample test run results."""
    models = ["gpt-4o-mini", "claude-3-haiku", "mistral-large"]
    return [
        {
            "id": i,
            "run_id": f"run_{i:03d}",
            "test_id": f"test_{i % 10:03d}",
            "model_name": models[i % 3],
            "is_harmful": i % 5 == 0,  # 20% harmful
            "harm_score": 0.1 + (i % 10) * 0.08,
            "evaluator": "llm_judge",
            "executed_at": datetime.now(),
            "latency_seconds": 1.0 + (i % 3) * 0.5,
            "tokens_used": 200 + i * 10,
            "cost_usd": 0.001 * (1 + i % 3),
        }
        for i in range(30)
    ]


# =============================================================================
# Statistics Fixtures
# =============================================================================

@pytest.fixture
def sample_statistics():
    """Create sample statistics data."""
    return {
        "total_tests": 21000,
        "total_runs": 50000,
        "total_models": 6,
        "avg_harmful_rate": 0.15,
    }


@pytest.fixture
def sample_suite_statistics():
    """Create sample suite statistics."""
    from src.core.api_specification import SuiteStatistics
    return [
        SuiteStatistics(
            suite_id=1,
            suite_name="regulatory_evasion",
            total_tests=3000,
            total_runs=15000,
            avg_harmful_rate=0.12,
            avg_harm_score=None,
            avg_cost=None,
            avg_latency=None
        ),
        SuiteStatistics(
            suite_id=2,
            suite_name="debt_bondage",
            total_tests=4000,
            total_runs=20000,
            avg_harmful_rate=0.18,
            avg_harm_score=None,
            avg_cost=None,
            avg_latency=None
        ),
    ]


@pytest.fixture
def sample_model_performance():
    """Create sample model performance data."""
    from src.core.api_specification import ModelPerformance
    return [
        ModelPerformance(
            model_id=1,
            model_name="gpt-4o-mini",
            provider="openai",
            total_runs=10000,
            harmful_rate=0.12,
            avg_harm_score=None,
            total_cost=None,
            avg_latency=None,
            avg_tokens=None
        ),
        ModelPerformance(
            model_id=2,
            model_name="claude-3-haiku",
            provider="anthropic",
            total_runs=10000,
            harmful_rate=0.08,
            avg_harm_score=None,
            total_cost=None,
            avg_latency=None,
            avg_tokens=None
        ),
    ]


# =============================================================================
# Pydantic Model Fixtures
# =============================================================================

@pytest.fixture
def sample_test_summary():
    """Create a sample TestSummary."""
    from src.core.api_specification import TestSummary
    return TestSummary(
        id="test_001",
        display_name="Fee Manipulation Test",
        short_description="Tests LLM response to fee manipulation requests",
        test_suite="regulatory_evasion",
        difficulty_level="hard",
        attack_sophistication="expert",
        corridor="PH-SA",
        total_runs=100,
        harmful_rate=0.15,
        created_at=datetime.now()
    )


@pytest.fixture
def sample_test_detail():
    """Create a sample TestDetail."""
    from src.core.api_specification import TestDetail
    return TestDetail(
        id="test_001",
        test_suite="regulatory_evasion",
        prompt="A recruitment agency asks you to help rename fees...",
        category="fee_manipulation",
        exploitation_types=["fee_renaming", "hidden_charges"],
        attack_sophistication="expert",
        difficulty_level="hard",
        ilo_indicators=["excessive_fees", "deceptive_recruitment"],
        origin_country="Philippines",
        destination_country="Saudi Arabia",
        transit_countries=None,
        corridor="PH-SA",
        debt_amount=5000.0,
        monthly_salary=400.0,
        interest_rate=None,
        num_entities=None,
        psychological_tactics=None,
        financial_tactics=["fee_splitting"],
        regulatory_evasion=["license_fraud"],
        display_name="Fee Manipulation Test",
        short_description="Tests LLM response to fee manipulation",
        full_metadata={"version": "1.0", "author": "system"},
        created_at=datetime.now(),
        updated_at=datetime.now()
    )


# =============================================================================
# ILO Indicator Fixtures
# =============================================================================

@pytest.fixture
def ilo_indicators():
    """Return list of ILO forced labor indicators."""
    return [
        "abuse_of_vulnerability",
        "deception",
        "restriction_of_movement",
        "isolation",
        "physical_violence",
        "sexual_violence",
        "intimidation_threats",
        "retention_of_identity_documents",
        "withholding_of_wages",
        "debt_bondage",
        "abusive_working_conditions",
        "excessive_overtime",
    ]


# =============================================================================
# Migration Corridor Fixtures
# =============================================================================

@pytest.fixture
def migration_corridors():
    """Return list of major migration corridors."""
    return [
        {"code": "PH-SA", "origin": "Philippines", "destination": "Saudi Arabia"},
        {"code": "NP-QA", "origin": "Nepal", "destination": "Qatar"},
        {"code": "BD-MY", "origin": "Bangladesh", "destination": "Malaysia"},
        {"code": "ID-SG", "origin": "Indonesia", "destination": "Singapore"},
        {"code": "ET-LB", "origin": "Ethiopia", "destination": "Lebanon"},
        {"code": "MM-TH", "origin": "Myanmar", "destination": "Thailand"},
    ]


# =============================================================================
# Configuration Fixtures
# =============================================================================

@pytest.fixture
def test_config():
    """Create test configuration."""
    return {
        "database_path": ":memory:",
        "log_level": "DEBUG",
        "max_retries": 3,
        "timeout_seconds": 30,
        "batch_size": 100,
    }


# =============================================================================
# Pytest Configuration
# =============================================================================

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "database: marks tests that require database access"
    )
