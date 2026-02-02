"""Tests for API specification models."""

import pytest
from datetime import datetime
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.api_specification import (
    FilterOperator,
    SortOrder,
    TestFilter,
    PaginationParams,
    SortParams,
    TestListRequest,
    TestSummary,
    TestDetail,
    TestListResponse,
    TestRunSummary,
    TestRunDetail,
    AuditTrailResponse,
    ModelPerformance,
    ModelComparisonResponse,
    SuiteStatistics,
    CorridorStatistics,
    ILOIndicatorCoverage,
    StatisticsResponse,
    ExecuteTestRequest,
    ExecuteTestResponse,
    TrainingExampleExportRequest,
    TrainingExampleExportResponse,
    TaxonomyCategory,
    TaxonomyResponse,
)


class TestFilterModels:
    """Tests for filter-related models."""

    def test_filter_operator_values(self):
        """Test FilterOperator enum values."""
        assert FilterOperator.EQUALS == "eq"
        assert FilterOperator.NOT_EQUALS == "ne"
        assert FilterOperator.IN == "in"
        assert FilterOperator.CONTAINS == "contains"

    def test_sort_order_values(self):
        """Test SortOrder enum values."""
        assert SortOrder.ASC == "asc"
        assert SortOrder.DESC == "desc"

    def test_test_filter_creation(self):
        """Test TestFilter model creation."""
        filter_obj = TestFilter(
            field="test_suite",
            operator=FilterOperator.EQUALS,
            value="regulatory_evasion"
        )
        assert filter_obj.field == "test_suite"
        assert filter_obj.operator == FilterOperator.EQUALS
        assert filter_obj.value == "regulatory_evasion"

    def test_pagination_defaults(self):
        """Test PaginationParams default values."""
        params = PaginationParams()
        assert params.page == 1
        assert params.page_size == 50

    def test_pagination_custom_values(self):
        """Test PaginationParams with custom values."""
        params = PaginationParams(page=5, page_size=100)
        assert params.page == 5
        assert params.page_size == 100

    def test_sort_params_defaults(self):
        """Test SortParams default order."""
        params = SortParams(field="created_at")
        assert params.order == SortOrder.DESC


class TestRequestModels:
    """Tests for request models."""

    def test_test_list_request_defaults(self):
        """Test TestListRequest default values."""
        request = TestListRequest()
        assert request.pagination.page == 1
        assert request.filters is None
        assert request.test_suite is None

    def test_test_list_request_with_filters(self):
        """Test TestListRequest with filters."""
        request = TestListRequest(
            test_suite="moral_religious_framing",
            min_harmful_rate=0.2,
            ilo_indicators=["debt_bondage", "excessive_fees"]
        )
        assert request.test_suite == "moral_religious_framing"
        assert request.min_harmful_rate == 0.2
        assert len(request.ilo_indicators) == 2

    def test_execute_test_request(self):
        """Test ExecuteTestRequest model."""
        request = ExecuteTestRequest(
            test_id="test_001",
            model_id=1,
            evaluator="llm_judge"
        )
        assert request.test_id == "test_001"
        assert request.model_id == 1
        assert request.evaluator == "llm_judge"

    def test_training_export_request_defaults(self):
        """Test TrainingExampleExportRequest defaults."""
        request = TrainingExampleExportRequest()
        assert request.format == "jsonl"
        assert request.example_type == "contrastive_pair"


class TestResponseModels:
    """Tests for response models."""

    def test_test_summary_creation(self):
        """Test TestSummary model creation."""
        summary = TestSummary(
            id="test_001",
            display_name="Test One",
            short_description="A test case",
            test_suite="regulatory_evasion",
            difficulty_level="hard",
            attack_sophistication="expert",
            corridor="PH-SA",
            created_at=datetime.now()
        )
        assert summary.id == "test_001"
        assert summary.total_runs == 0
        assert summary.harmful_rate is None

    def test_test_detail_creation(self):
        """Test TestDetail model creation."""
        detail = TestDetail(
            id="test_001",
            test_suite="regulatory_evasion",
            prompt="Test prompt",
            category="fee_manipulation",
            exploitation_types=["fee_renaming"],
            attack_sophistication="expert",
            difficulty_level="hard",
            ilo_indicators=["excessive_fees"],
            origin_country=None,
            destination_country=None,
            transit_countries=None,
            corridor=None,
            debt_amount=None,
            monthly_salary=None,
            interest_rate=None,
            num_entities=None,
            psychological_tactics=None,
            financial_tactics=None,
            regulatory_evasion=None,
            display_name="Test One",
            short_description="A test case",
            full_metadata={},
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        assert detail.id == "test_001"
        assert detail.total_runs == 0

    def test_test_list_response(self):
        """Test TestListResponse model."""
        response = TestListResponse(
            tests=[],
            total_count=100,
            page=1,
            page_size=50,
            total_pages=2
        )
        assert response.total_count == 100
        assert response.total_pages == 2

    def test_model_performance(self):
        """Test ModelPerformance model."""
        perf = ModelPerformance(
            model_id=1,
            model_name="gpt-4o-mini",
            provider="openai",
            total_runs=1000,
            harmful_rate=0.15,
            avg_harm_score=None,
            total_cost=None,
            avg_latency=None,
            avg_tokens=None
        )
        assert perf.harmful_rate == 0.15
        assert perf.avg_harm_score is None


class TestStatisticsModels:
    """Tests for statistics models."""

    def test_suite_statistics(self):
        """Test SuiteStatistics model."""
        stats = SuiteStatistics(
            suite_id=1,
            suite_name="regulatory_evasion",
            total_tests=3000,
            total_runs=15000,
            avg_harmful_rate=None,
            avg_harm_score=None,
            avg_cost=None,
            avg_latency=None
        )
        assert stats.total_tests == 3000

    def test_corridor_statistics(self):
        """Test CorridorStatistics model."""
        stats = CorridorStatistics(
            corridor="PH-SA",
            origin_country="Philippines",
            destination_country="Saudi Arabia",
            total_tests=500,
            total_runs=2500,
            harmful_rate=None,
            avg_debt_amount=None,
            avg_monthly_salary=None
        )
        assert stats.corridor == "PH-SA"

    def test_ilo_indicator_coverage(self):
        """Test ILOIndicatorCoverage model."""
        coverage = ILOIndicatorCoverage(
            ilo_indicator="debt_bondage",
            tests_with_indicator=1500,
            total_runs=7500,
            harmful_rate=None
        )
        assert coverage.ilo_indicator == "debt_bondage"

    def test_statistics_response(self):
        """Test StatisticsResponse model."""
        response = StatisticsResponse(
            total_tests=21000,
            total_runs=105000,
            total_models=6,
            suites=[],
            models=[],
            corridors=[],
            ilo_indicators=[]
        )
        assert response.total_tests == 21000


class TestTaxonomyModels:
    """Tests for taxonomy models."""

    def test_taxonomy_category(self):
        """Test TaxonomyCategory model."""
        category = TaxonomyCategory(
            id=1,
            category_type="exploitation_type",
            category_name="debt_bondage",
            display_name="Debt Bondage",
            description=None,
            parent_category=None
        )
        assert category.category_name == "debt_bondage"

    def test_taxonomy_response(self):
        """Test TaxonomyResponse model."""
        response = TaxonomyResponse(
            categories={
                "exploitation_type": []
            },
            test_suites=["regulatory_evasion", "moral_religious_framing"],
            models=[{"id": 1, "name": "gpt-4o-mini"}]
        )
        assert len(response.test_suites) == 2
