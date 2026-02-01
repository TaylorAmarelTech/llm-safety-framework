"""Integration tests for the LLM Safety Framework."""

import pytest
from datetime import datetime
from unittest.mock import MagicMock, patch

import sys
sys.path.insert(0, str(__file__).rsplit('tests', 1)[0])


class TestFrameworkIntegration:
    """Integration tests for framework components working together."""

    def test_api_models_import(self):
        """Test that API models can be imported."""
        from src.core.api_specification import (
            TestListRequest,
            TestListResponse,
            TestDetail,
            StatisticsResponse,
        )
        assert TestListRequest is not None
        assert TestListResponse is not None

    def test_base_agent_import(self):
        """Test that base agent can be imported."""
        from src.core.base_agent import (
            AgentRole,
            AgentConfig,
            HarnessAgent,
        )
        assert AgentRole is not None
        assert AgentConfig is not None

    def test_package_init(self):
        """Test that package __init__ works."""
        from src import __version__, __author__
        assert __version__ == "1.0.0"
        assert __author__ == "Taylor Amarel"

    def test_request_response_cycle(self):
        """Test a complete request/response cycle with models."""
        from src.core.api_specification import (
            TestListRequest,
            TestListResponse,
            TestSummary,
            PaginationParams,
        )

        # Create request
        request = TestListRequest(
            test_suite="regulatory_evasion",
            min_harmful_rate=0.2,
            pagination=PaginationParams(page=1, page_size=10)
        )
        assert request.test_suite == "regulatory_evasion"

        # Create response
        test_summary = TestSummary(
            id="test_001",
            display_name="Test Case 1",
            short_description="A regulatory evasion test",
            test_suite="regulatory_evasion",
            difficulty_level="hard",
            attack_sophistication="expert",
            corridor="PH-SA",
            total_runs=5,
            harmful_rate=0.4,
            created_at=datetime.now()
        )

        response = TestListResponse(
            tests=[test_summary],
            total_count=1,
            page=1,
            page_size=10,
            total_pages=1
        )

        assert len(response.tests) == 1
        assert response.tests[0].harmful_rate == 0.4

    def test_agent_configuration_chain(self):
        """Test agent configuration works with different roles."""
        from src.core.base_agent import AgentRole, AgentConfig

        roles = [
            AgentRole.PLANNER,
            AgentRole.EXECUTOR,
            AgentRole.ANALYZER,
        ]

        for role in roles:
            config = AgentConfig(
                role=role,
                temperature=0.5,
                max_tokens=2000
            )
            assert config.role == role
            assert config.temperature == 0.5

    def test_statistics_aggregation(self):
        """Test statistics model aggregation."""
        from src.core.api_specification import (
            StatisticsResponse,
            SuiteStatistics,
            ModelPerformance,
            CorridorStatistics,
            ILOIndicatorCoverage,
        )

        # Create suite stats
        suite = SuiteStatistics(
            suite_id=1,
            suite_name="moral_religious_framing",
            total_tests=3000,
            total_runs=15000,
            avg_harmful_rate=0.233
        )

        # Create model stats
        model = ModelPerformance(
            model_id=1,
            model_name="gpt-4o-mini",
            provider="openai",
            total_runs=5000,
            harmful_rate=0.15
        )

        # Create corridor stats
        corridor = CorridorStatistics(
            corridor="PH-SA",
            origin_country="Philippines",
            destination_country="Saudi Arabia",
            total_tests=500,
            total_runs=2500,
            harmful_rate=0.18
        )

        # Create ILO indicator stats
        ilo = ILOIndicatorCoverage(
            ilo_indicator="debt_bondage",
            tests_with_indicator=1500,
            total_runs=7500,
            harmful_rate=0.22
        )

        # Aggregate into response
        response = StatisticsResponse(
            total_tests=21000,
            total_runs=105000,
            total_models=6,
            suites=[suite],
            models=[model],
            corridors=[corridor],
            ilo_indicators=[ilo]
        )

        assert response.total_tests == 21000
        assert len(response.suites) == 1
        assert response.suites[0].avg_harmful_rate == 0.233
        assert response.models[0].harmful_rate == 0.15


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_test_list_response(self):
        """Test handling of empty test list."""
        from src.core.api_specification import TestListResponse

        response = TestListResponse(
            tests=[],
            total_count=0,
            page=1,
            page_size=50,
            total_pages=0
        )
        assert len(response.tests) == 0
        assert response.total_pages == 0

    def test_pagination_edge_cases(self):
        """Test pagination with edge case values."""
        from src.core.api_specification import PaginationParams

        # Minimum values
        params = PaginationParams(page=1, page_size=1)
        assert params.page == 1
        assert params.page_size == 1

        # Maximum page_size
        params = PaginationParams(page=1, page_size=1000)
        assert params.page_size == 1000

    def test_optional_fields_none(self):
        """Test models handle None for optional fields."""
        from src.core.api_specification import TestDetail
        from datetime import datetime

        detail = TestDetail(
            id="test_001",
            test_suite="test",
            prompt="Test",
            category="test",
            exploitation_types=[],
            attack_sophistication="basic",
            difficulty_level="easy",
            ilo_indicators=[],
            origin_country=None,
            destination_country=None,
            corridor=None,
            display_name="Test",
            short_description="Test",
            full_metadata={},
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        assert detail.origin_country is None
        assert detail.corridor is None
        assert detail.debt_amount is None


@pytest.mark.slow
class TestPerformance:
    """Performance-related tests (marked as slow)."""

    def test_large_response_creation(self):
        """Test creating a large response object."""
        from src.core.api_specification import (
            TestListResponse,
            TestSummary,
        )
        from datetime import datetime

        # Create 1000 test summaries
        tests = [
            TestSummary(
                id=f"test_{i:04d}",
                display_name=f"Test {i}",
                short_description=f"Description {i}",
                test_suite="test_suite",
                difficulty_level="medium",
                attack_sophistication="moderate",
                corridor="TEST",
                created_at=datetime.now()
            )
            for i in range(1000)
        ]

        response = TestListResponse(
            tests=tests,
            total_count=1000,
            page=1,
            page_size=1000,
            total_pages=1
        )

        assert len(response.tests) == 1000
