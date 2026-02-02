"""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime


# ============================================================================
# REQUEST/RESPONSE MODELS
# ============================================================================

class FilterOperator(str, Enum):
    """Filter comparison operators"""
    EQUALS = "eq"
    NOT_EQUALS = "ne"
    IN = "in"
    NOT_IN = "not_in"
    GREATER_THAN = "gt"
    LESS_THAN = "lt"
    CONTAINS = "contains"
    STARTS_WITH = "starts_with"


class SortOrder(str, Enum):
    """Sort direction"""
    ASC = "asc"
    DESC = "desc"


class TestFilter(BaseModel):
    """Filter criteria for test queries"""
    field: str  # Column name to filter on
    operator: FilterOperator
    value: Any


class PaginationParams(BaseModel):
    """Pagination parameters"""
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=50, ge=1, le=1000)


class SortParams(BaseModel):
    """Sort parameters"""
    field: str
    order: SortOrder = SortOrder.DESC


class TestListRequest(BaseModel):
    """Request model for listing tests"""
    filters: Optional[List[TestFilter]] = None
    pagination: PaginationParams = PaginationParams()
    sort: Optional[SortParams] = None

    # Quick filters (convenience)
    test_suite: Optional[str] = None
    difficulty_level: Optional[str] = None
    origin_country: Optional[str] = None
    destination_country: Optional[str] = None
    corridor: Optional[str] = None
    ilo_indicators: Optional[List[str]] = None
    exploitation_types: Optional[List[str]] = None
    min_harmful_rate: Optional[float] = None
    max_harmful_rate: Optional[float] = None


class TestSummary(BaseModel):
    """Summary model for test list responses"""
    id: str
    display_name: str
    short_description: str
    test_suite: str
    difficulty_level: str
    attack_sophistication: str
    corridor: Optional[str]

    # Metrics
    total_runs: int = 0
    harmful_rate: Optional[float] = None

    # Timestamps
    created_at: datetime


class TestDetail(BaseModel):
    """Full test details"""
    id: str
    test_suite: str
    prompt: str
    category: str

    # Classification
    exploitation_types: List[str]
    attack_sophistication: str
    difficulty_level: str
    ilo_indicators: List[str]

    # Geographic
    origin_country: Optional[str]
    destination_country: Optional[str]
    transit_countries: Optional[List[str]]
    corridor: Optional[str]

    # Financial
    debt_amount: Optional[int]
    monthly_salary: Optional[int]
    interest_rate: Optional[float]
    num_entities: Optional[int]

    # Tactics
    psychological_tactics: Optional[List[str]]
    financial_tactics: Optional[List[str]]
    regulatory_evasion: Optional[List[str]]

    # Metadata
    display_name: str
    short_description: str
    full_metadata: Dict[str, Any]

    # Metrics
    total_runs: int = 0
    total_harmful: int = 0
    overall_harmful_rate: Optional[float] = None
    model_results: Optional[Dict[str, Any]] = None

    # Timestamps
    created_at: datetime
    updated_at: datetime


class TestListResponse(BaseModel):
    """Response model for test listings"""
    tests: List[TestSummary]
    total_count: int
    page: int
    page_size: int
    total_pages: int


class TestRunSummary(BaseModel):
    """Summary of a single test run"""
    id: int
    run_id: str
    test_id: str
    model_name: str

    # Results
    is_harmful: bool
    harm_score: Optional[float]

    # Evaluation
    evaluator: str
    ilo_indicators_detected: Optional[List[str]]

    # Performance
    cost_usd: Optional[float]
    latency_seconds: Optional[float]
    tokens_used: Optional[int]

    executed_at: datetime


class TestRunDetail(TestRunSummary):
    """Full test run details including raw data"""
    prompt: str
    raw_response: str
    evaluation_rationale: Optional[str]
    exploitation_types_detected: Optional[List[str]]


class AuditTrailResponse(BaseModel):
    """Audit trail for a specific test"""
    test_id: str
    total_runs: int
    runs: List[TestRunSummary]


class ModelPerformance(BaseModel):
    """Model performance statistics"""
    model_id: int
    model_name: str
    provider: str

    # Statistics
    total_runs: int
    harmful_rate: float
    avg_harm_score: Optional[float]
    total_cost: Optional[float]
    avg_latency: Optional[float]
    avg_tokens: Optional[int]


class ModelComparisonResponse(BaseModel):
    """Compare performance across models"""
    models: List[ModelPerformance]
    test_suite_filter: Optional[str] = None
    total_tests_compared: int


class SuiteStatistics(BaseModel):
    """Statistics for a test suite"""
    suite_id: int
    suite_name: str
    total_tests: int
    total_runs: int
    avg_harmful_rate: Optional[float]
    avg_harm_score: Optional[float]
    avg_cost: Optional[float]
    avg_latency: Optional[float]


class CorridorStatistics(BaseModel):
    """Statistics by migration corridor"""
    corridor: str
    origin_country: str
    destination_country: str
    total_tests: int
    total_runs: int
    harmful_rate: Optional[float]
    avg_debt_amount: Optional[int]
    avg_monthly_salary: Optional[int]


class ILOIndicatorCoverage(BaseModel):
    """ILO indicator coverage statistics"""
    ilo_indicator: str
    tests_with_indicator: int
    total_runs: int
    harmful_rate: Optional[float]


class StatisticsResponse(BaseModel):
    """Aggregate statistics"""
    total_tests: int
    total_runs: int
    total_models: int

    # Suite breakdown
    suites: List[SuiteStatistics]

    # Model comparison
    models: List[ModelPerformance]

    # Geographic analysis
    corridors: List[CorridorStatistics]

    # ILO indicator coverage
    ilo_indicators: List[ILOIndicatorCoverage]


class ExecuteTestRequest(BaseModel):
    """Request to execute a test"""
    test_id: str
    model_id: int
    evaluator: Optional[str] = "llm_judge"


class ExecuteTestResponse(BaseModel):
    """Response from test execution"""
    run_id: int
    test_id: str
    model_id: int
    is_harmful: bool
    harm_score: Optional[float]
    raw_response: str
    evaluation_rationale: Optional[str]
    cost_usd: Optional[float]
    latency_seconds: Optional[float]


class TrainingExampleExportRequest(BaseModel):
    """Request to export training examples"""
    test_ids: Optional[List[str]] = None
    min_harmful_rate: Optional[float] = None
    max_harmful_rate: Optional[float] = None
    example_type: Optional[str] = "contrastive_pair"
    format: str = "jsonl"  # jsonl, parquet, csv


class TrainingExampleExportResponse(BaseModel):
    """Response from training example export"""
    export_id: str
    total_examples: int
    download_url: str
    format: str
    expires_at: datetime


class TaxonomyCategory(BaseModel):
    """Taxonomy category definition"""
    id: int
    category_type: str
    category_name: str
    display_name: str
    description: Optional[str]
    parent_category: Optional[str]


class TaxonomyResponse(BaseModel):
    """Complete taxonomy for filtering"""
    categories: Dict[str, List[TaxonomyCategory]]
    test_suites: List[str]
    models: List[Dict[str, Any]]


# ============================================================================
# API ENDPOINT SPECIFICATION
# ============================================================================

class APIEndpoints:
    """
    Complete API endpoint specification

    Base URL: /api/v1
    """

    # ========================================================================
    # TEST MANAGEMENT
    # ========================================================================

    @staticmethod
    def list_tests():
        """
        GET /api/v1/tests

        Query Parameters:
        - page: int (default: 1)
        - page_size: int (default: 50, max: 1000)
        - sort_by: str (default: created_at)
        - sort_order: asc|desc (default: desc)
        - test_suite: str
        - difficulty_level: str
        - origin_country: str
        - destination_country: str
        - corridor: str
        - ilo_indicators: str (comma-separated)
        - exploitation_types: str (comma-separated)
        - min_harmful_rate: float (0.0-1.0)
        - max_harmful_rate: float (0.0-1.0)

        Response: TestListResponse

        Example:
        GET /api/v1/tests?test_suite=moral_religious_framing&min_harmful_rate=0.2&page=1&page_size=50
        """
        pass

    @staticmethod
    def get_test_detail():
        """
        GET /api/v1/tests/{test_id}

        Path Parameters:
        - test_id: str

        Response: TestDetail

        Example:
        GET /api/v1/tests/biblical_debt_servitude_Philippines->Hong Kong_35593
        """
        pass

    @staticmethod
    def search_tests():
        """
        POST /api/v1/tests/search

        Request Body: TestListRequest

        Response: TestListResponse

        Example:
        POST /api/v1/tests/search
        {
            "filters": [
                {"field": "difficulty_level", "operator": "in", "value": ["hard", "very_hard"]},
                {"field": "origin_country", "operator": "eq", "value": "Philippines"}
            ],
            "pagination": {"page": 1, "page_size": 100},
            "sort": {"field": "harmful_rate", "order": "desc"}
        }
        """
        pass

    # ========================================================================
    # AUDIT TRAIL & TEST RUNS
    # ========================================================================

    @staticmethod
    def get_test_audit_trail():
        """
        GET /api/v1/tests/{test_id}/runs

        Path Parameters:
        - test_id: str

        Query Parameters:
        - model_id: int (optional filter)
        - is_harmful: bool (optional filter)
        - limit: int (default: 100)

        Response: AuditTrailResponse

        Example:
        GET /api/v1/tests/biblical_debt_servitude_Philippines->Hong Kong_35593/runs?limit=50
        """
        pass

    @staticmethod
    def get_test_run_detail():
        """
        GET /api/v1/runs/{run_id}

        Path Parameters:
        - run_id: int

        Response: TestRunDetail

        Example:
        GET /api/v1/runs/12345
        """
        pass

    @staticmethod
    def execute_test():
        """
        POST /api/v1/tests/{test_id}/execute

        Path Parameters:
        - test_id: str

        Request Body: ExecuteTestRequest

        Response: ExecuteTestResponse

        Example:
        POST /api/v1/tests/biblical_debt_servitude_Philippines->Hong Kong_35593/execute
        {
            "model_id": 1,
            "evaluator": "llm_judge"
        }
        """
        pass

    # ========================================================================
    # STATISTICS & ANALYTICS
    # ========================================================================

    @staticmethod
    def get_statistics():
        """
        GET /api/v1/statistics

        Query Parameters:
        - test_suite: str (optional filter)
        - start_date: datetime (optional filter)
        - end_date: datetime (optional filter)

        Response: StatisticsResponse

        Example:
        GET /api/v1/statistics?test_suite=moral_religious_framing
        """
        pass

    @staticmethod
    def compare_models():
        """
        GET /api/v1/statistics/models

        Query Parameters:
        - test_suite: str (optional filter)
        - model_ids: str (comma-separated, optional filter)

        Response: ModelComparisonResponse

        Example:
        GET /api/v1/statistics/models?test_suite=regulatory_evasion&model_ids=1,2,3
        """
        pass

    @staticmethod
    def get_corridor_statistics():
        """
        GET /api/v1/statistics/corridors

        Response: List[CorridorStatistics]

        Example:
        GET /api/v1/statistics/corridors
        """
        pass

    @staticmethod
    def get_ilo_indicator_coverage():
        """
        GET /api/v1/statistics/ilo-indicators

        Response: List[ILOIndicatorCoverage]

        Example:
        GET /api/v1/statistics/ilo-indicators
        """
        pass

    # ========================================================================
    # TRAINING DATA EXPORT
    # ========================================================================

    @staticmethod
    def export_training_data():
        """
        POST /api/v1/training/export

        Request Body: TrainingExampleExportRequest

        Response: TrainingExampleExportResponse

        Example:
        POST /api/v1/training/export
        {
            "min_harmful_rate": 0.2,
            "example_type": "contrastive_pair",
            "format": "jsonl"
        }
        """
        pass

    @staticmethod
    def download_training_data():
        """
        GET /api/v1/training/download/{export_id}

        Path Parameters:
        - export_id: str

        Response: Binary file download

        Example:
        GET /api/v1/training/download/export_20260130_143022
        """
        pass

    # ========================================================================
    # TAXONOMY & METADATA
    # ========================================================================

    @staticmethod
    def get_taxonomy():
        """
        GET /api/v1/taxonomy

        Response: TaxonomyResponse

        Example:
        GET /api/v1/taxonomy
        """
        pass

    @staticmethod
    def get_test_suites():
        """
        GET /api/v1/test-suites

        Response: List[Dict[str, Any]]

        Example:
        GET /api/v1/test-suites
        """
        pass

    @staticmethod
    def get_models():
        """
        GET /api/v1/models

        Query Parameters:
        - is_active: bool (optional filter)

        Response: List[Dict[str, Any]]

        Example:
        GET /api/v1/models?is_active=true
        """
        pass


# ============================================================================
# EXAMPLE IMPLEMENTATION (FastAPI)
# ============================================================================

FASTAPI_IMPLEMENTATION = """
from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.middleware.cors import CORSMiddleware
import asyncpg
from typing import Optional

app = FastAPI(title="LLM Trafficking Test Benchmark API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection pool
@app.on_event("startup")
async def startup():
    app.state.pool = await asyncpg.create_pool(
        dsn="postgresql://user:password@localhost/trafficking_tests",
        min_size=10,
        max_size=50
    )

@app.on_event("shutdown")
async def shutdown():
    await app.state.pool.close()

# ============================================================================
# ENDPOINTS
# ============================================================================

@app.get("/api/v1/tests", response_model=TestListResponse)
async def list_tests(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=1000),
    test_suite: Optional[str] = None,
    difficulty_level: Optional[str] = None,
    origin_country: Optional[str] = None,
    destination_country: Optional[str] = None,
    min_harmful_rate: Optional[float] = Query(None, ge=0.0, le=1.0),
    sort_by: str = "created_at",
    sort_order: SortOrder = SortOrder.DESC
):
    '''List tests with filtering and pagination'''

    # Build query
    query = '''
        SELECT t.*, tm.overall_harmful_rate, tm.total_runs
        FROM tests t
        LEFT JOIN test_metrics tm ON t.id = tm.test_id
        WHERE 1=1
    '''
    params = []

    if test_suite:
        query += f' AND t.test_suite_id = (SELECT id FROM test_suites WHERE name = ${len(params)+1})'
        params.append(test_suite)

    if difficulty_level:
        query += f' AND t.difficulty_level = ${len(params)+1}'
        params.append(difficulty_level)

    if origin_country:
        query += f' AND t.origin_country = ${len(params)+1}'
        params.append(origin_country)

    if destination_country:
        query += f' AND t.destination_country = ${len(params)+1}'
        params.append(destination_country)

    if min_harmful_rate is not None:
        query += f' AND tm.overall_harmful_rate >= ${len(params)+1}'
        params.append(min_harmful_rate)

    # Count total
    count_query = f'SELECT COUNT(*) FROM ({query}) AS subquery'
    async with app.state.pool.acquire() as conn:
        total_count = await conn.fetchval(count_query, *params)

    # Add sorting and pagination
    query += f' ORDER BY {sort_by} {sort_order.value}'
    query += f' LIMIT ${len(params)+1} OFFSET ${len(params)+2}'
    params.extend([page_size, (page - 1) * page_size])

    # Execute query
    async with app.state.pool.acquire() as conn:
        rows = await conn.fetch(query, *params)

    tests = [TestSummary(**dict(row)) for row in rows]

    return TestListResponse(
        tests=tests,
        total_count=total_count,
        page=page,
        page_size=page_size,
        total_pages=(total_count + page_size - 1) // page_size
    )

@app.get("/api/v1/tests/{test_id}", response_model=TestDetail)
async def get_test_detail(test_id: str = Path(...)):
    '''Get full details for a specific test'''

    query = '''
        SELECT t.*, tm.*
        FROM tests t
        LEFT JOIN test_metrics tm ON t.id = tm.test_id
        WHERE t.id = $1
    '''

    async with app.state.pool.acquire() as conn:
        row = await conn.fetchrow(query, test_id)

    if not row:
        raise HTTPException(status_code=404, detail="Test not found")

    return TestDetail(**dict(row))

@app.get("/api/v1/tests/{test_id}/runs", response_model=AuditTrailResponse)
async def get_test_audit_trail(
    test_id: str = Path(...),
    model_id: Optional[int] = None,
    limit: int = Query(100, ge=1, le=1000)
):
    '''Get audit trail for a specific test'''

    query = '''
        SELECT tr.*, m.name as model_name
        FROM test_runs tr
        JOIN models m ON tr.model_id = m.id
        WHERE tr.test_id = $1
    '''
    params = [test_id]

    if model_id:
        query += f' AND tr.model_id = ${len(params)+1}'
        params.append(model_id)

    query += f' ORDER BY tr.executed_at DESC LIMIT ${len(params)+1}'
    params.append(limit)

    async with app.state.pool.acquire() as conn:
        rows = await conn.fetch(query, *params)
        total_runs = await conn.fetchval(
            'SELECT COUNT(*) FROM test_runs WHERE test_id = $1',
            test_id
        )

    runs = [TestRunSummary(**dict(row)) for row in rows]

    return AuditTrailResponse(
        test_id=test_id,
        total_runs=total_runs,
        runs=runs
    )

@app.get("/api/v1/statistics", response_model=StatisticsResponse)
async def get_statistics(test_suite: Optional[str] = None):
    '''Get aggregate statistics'''

    async with app.state.pool.acquire() as conn:
        # Suite statistics
        suite_query = 'SELECT * FROM mv_suite_statistics'
        if test_suite:
            suite_query += ' WHERE suite_name = $1'
            suite_rows = await conn.fetch(suite_query, test_suite)
        else:
            suite_rows = await conn.fetch(suite_query)

        # Model performance
        model_query = 'SELECT * FROM mv_model_performance'
        model_rows = await conn.fetch(model_query)

        # Corridor statistics
        corridor_rows = await conn.fetch('SELECT * FROM mv_corridor_statistics')

        # ILO indicator coverage
        ilo_rows = await conn.fetch('SELECT * FROM mv_ilo_indicator_coverage')

        # Total counts
        total_tests = await conn.fetchval('SELECT COUNT(*) FROM tests')
        total_runs = await conn.fetchval('SELECT COUNT(*) FROM test_runs')
        total_models = await conn.fetchval('SELECT COUNT(*) FROM models WHERE is_active = true')

    return StatisticsResponse(
        total_tests=total_tests,
        total_runs=total_runs,
        total_models=total_models,
        suites=[SuiteStatistics(**dict(row)) for row in suite_rows],
        models=[ModelPerformance(**dict(row)) for row in model_rows],
        corridors=[CorridorStatistics(**dict(row)) for row in corridor_rows],
        ilo_indicators=[ILOIndicatorCoverage(**dict(row)) for row in ilo_rows]
    )

@app.get("/api/v1/taxonomy", response_model=TaxonomyResponse)
async def get_taxonomy():
    '''Get complete taxonomy for filtering'''

    async with app.state.pool.acquire() as conn:
        category_rows = await conn.fetch('SELECT * FROM taxonomy_categories ORDER BY sort_order')
        suite_rows = await conn.fetch('SELECT name FROM test_suites')
        model_rows = await conn.fetch('SELECT id, name, provider FROM models WHERE is_active = true')

    # Group categories by type
    categories = {}
    for row in category_rows:
        cat_type = row['category_type']
        if cat_type not in categories:
            categories[cat_type] = []
        categories[cat_type].append(TaxonomyCategory(**dict(row)))

    return TaxonomyResponse(
        categories=categories,
        test_suites=[row['name'] for row in suite_rows],
        models=[dict(row) for row in model_rows]
    )
"""


# ============================================================================
# USAGE DOCUMENTATION
# ============================================================================

def generate_api_documentation():
    """Generate API documentation in Markdown format"""

    doc = """
# LLM Trafficking Test Benchmark API Documentation

## Overview

RESTful API for accessing the LLM trafficking test benchmark database.

**Base URL:** `https://api.example.com/api/v1`

**Authentication:** API key required (pass in `X-API-Key` header)

## Endpoints

### Test Management

#### List Tests
```
GET /api/v1/tests
```

Query Parameters:
- `page` (int): Page number (default: 1)
- `page_size` (int): Results per page (default: 50, max: 1000)
- `test_suite` (str): Filter by test suite name
- `difficulty_level` (str): Filter by difficulty (easy, medium, hard, very_hard, expert)
- `origin_country` (str): Filter by origin country
- `destination_country` (str): Filter by destination country
- `corridor` (str): Filter by migration corridor
- `min_harmful_rate` (float): Minimum harmful rate (0.0-1.0)
- `max_harmful_rate` (float): Maximum harmful rate (0.0-1.0)
- `sort_by` (str): Field to sort by (default: created_at)
- `sort_order` (str): Sort direction (asc|desc, default: desc)

Example Response:
```json
{
  "tests": [
    {
      "id": "biblical_debt_servitude_Philippines->Hong Kong_35593",
      "display_name": "Biblical Debt Servitude - Philippines to Hong Kong",
      "short_description": "Faith-based recruitment using Romans 13:8...",
      "test_suite": "moral_religious_framing",
      "difficulty_level": "expert",
      "attack_sophistication": "expert",
      "corridor": "Philippines->Hong Kong",
      "total_runs": 5,
      "harmful_rate": 0.40,
      "created_at": "2026-01-30T12:00:00Z"
    }
  ],
  "total_count": 3000,
  "page": 1,
  "page_size": 50,
  "total_pages": 60
}
```

#### Get Test Detail
```
GET /api/v1/tests/{test_id}
```

Returns complete test information including full prompt, metadata, and metrics.

#### Search Tests (Advanced)
```
POST /api/v1/tests/search
```

Request body with complex filtering logic.

### Audit Trail

#### Get Test Runs
```
GET /api/v1/tests/{test_id}/runs
```

Returns all execution history for a specific test.

#### Get Run Detail
```
GET /api/v1/runs/{run_id}
```

Returns full details including raw LLM response.

### Statistics

#### Get Overall Statistics
```
GET /api/v1/statistics
```

Returns aggregate statistics across all tests and models.

#### Compare Models
```
GET /api/v1/statistics/models
```

Compare harmful rates across different LLM models.

### Training Data Export

#### Export Training Examples
```
POST /api/v1/training/export
```

Generate training dataset from test results.

## Rate Limiting

- 1000 requests per hour for authenticated users
- 100 requests per hour for unauthenticated users

## Error Responses

```json
{
  "error": "Not Found",
  "message": "Test with ID 'invalid_id' not found",
  "status_code": 404
}
```
"""

    return doc


if __name__ == '__main__':
    print("API Specification for LLM Trafficking Test Benchmark")
    print("=" * 70)
    print("\n[+] Request/Response models defined")
    print("[+] API endpoints specified")
    print("[+] FastAPI implementation example included")
    print("\nSee FASTAPI_IMPLEMENTATION constant for working code example")
