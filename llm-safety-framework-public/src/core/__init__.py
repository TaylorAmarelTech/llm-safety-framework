"""
LLM Safety Framework - Core Module

NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.

Core Components:
- api_specification: Pydantic models for the REST API
- base_agent: Base classes for harness agents
"""

from src.core.api_specification import (
    # Enums
    FilterOperator,
    SortOrder,
    # Request Models
    TestFilter,
    PaginationParams,
    SortParams,
    TestListRequest,
    ExecuteTestRequest,
    TrainingExampleExportRequest,
    # Response Models
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
    ExecuteTestResponse,
    TrainingExampleExportResponse,
    TaxonomyCategory,
    TaxonomyResponse,
)

from src.core.base_agent import (
    AgentRole,
    AgentConfig,
    AgentResponse,
    HarnessAgent,
    DEFAULT_SYSTEM_PROMPTS,
)

__all__ = [
    # API Specification - Enums
    "FilterOperator",
    "SortOrder",
    # API Specification - Request Models
    "TestFilter",
    "PaginationParams",
    "SortParams",
    "TestListRequest",
    "ExecuteTestRequest",
    "TrainingExampleExportRequest",
    # API Specification - Response Models
    "TestSummary",
    "TestDetail",
    "TestListResponse",
    "TestRunSummary",
    "TestRunDetail",
    "AuditTrailResponse",
    "ModelPerformance",
    "ModelComparisonResponse",
    "SuiteStatistics",
    "CorridorStatistics",
    "ILOIndicatorCoverage",
    "StatisticsResponse",
    "ExecuteTestResponse",
    "TrainingExampleExportResponse",
    "TaxonomyCategory",
    "TaxonomyResponse",
    # Base Agent
    "AgentRole",
    "AgentConfig",
    "AgentResponse",
    "HarnessAgent",
    "DEFAULT_SYSTEM_PROMPTS",
]
