# API Reference

## REST API

The framework provides a REST API via FastAPI for programmatic access.

### Base URL

```
http://localhost:8000/api/v1
```

### Authentication

Include your API key in the header:

```bash
Authorization: Bearer <your-api-key>
```

---

## Endpoints

### Tests

#### List Tests

```http
GET /tests
```

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `suite` | string | Filter by test suite |
| `category` | string | Filter by category |
| `difficulty` | string | Filter by difficulty (basic, medium, hard, expert) |
| `limit` | int | Max results (default: 100) |
| `offset` | int | Pagination offset |

**Response:**

```json
{
  "tests": [
    {
      "id": "test_001",
      "suite": "regulatory_evasion",
      "category": "fee_renaming",
      "prompt": "...",
      "expected_outcome": "refuse",
      "difficulty": "hard"
    }
  ],
  "total": 21000,
  "limit": 100,
  "offset": 0
}
```

#### Get Test Details

```http
GET /tests/{test_id}
```

**Response:**

```json
{
  "id": "test_001",
  "suite": "regulatory_evasion",
  "category": "fee_renaming",
  "subcategory": "processing_fee_evolution",
  "prompt": "...",
  "expected_outcome": "refuse",
  "difficulty": "hard",
  "metadata": {
    "ilo_indicators": ["debt_bondage", "excessive_fees"],
    "migration_corridor": "PH-SA",
    "created_at": "2026-01-15T10:30:00Z"
  }
}
```

#### Execute Test

```http
POST /tests/{test_id}/execute
```

**Request Body:**

```json
{
  "model": "gpt-4o-mini",
  "provider": "openai",
  "parameters": {
    "temperature": 0.7,
    "max_tokens": 1000
  }
}
```

**Response:**

```json
{
  "test_id": "test_001",
  "model": "gpt-4o-mini",
  "response": "...",
  "evaluation": {
    "outcome": "pass",
    "score": 0.95,
    "criteria": {
      "refused_harmful_request": true,
      "provided_alternatives": true,
      "explained_risks": true
    }
  },
  "latency_ms": 1234,
  "tokens_used": 456,
  "cost_usd": 0.0023
}
```

---

### Test Runs

#### Create Test Run

```http
POST /runs
```

**Request Body:**

```json
{
  "name": "GPT-4o Mini Benchmark",
  "description": "Testing GPT-4o-mini against moral framing suite",
  "model": "gpt-4o-mini",
  "test_suite": "moral_religious_framing",
  "test_count": 100
}
```

**Response:**

```json
{
  "run_id": "run_abc123",
  "status": "pending",
  "created_at": "2026-01-31T14:00:00Z"
}
```

#### Get Run Status

```http
GET /runs/{run_id}
```

**Response:**

```json
{
  "run_id": "run_abc123",
  "status": "running",
  "progress": {
    "completed": 45,
    "total": 100,
    "percentage": 45.0
  },
  "metrics": {
    "pass_rate": 0.82,
    "avg_latency_ms": 890,
    "total_cost_usd": 0.12
  }
}
```

#### Get Run Results

```http
GET /runs/{run_id}/results
```

**Response:**

```json
{
  "run_id": "run_abc123",
  "status": "completed",
  "summary": {
    "total_tests": 100,
    "passed": 82,
    "failed": 15,
    "errors": 3,
    "pass_rate": 0.82
  },
  "results": [
    {
      "test_id": "test_001",
      "outcome": "pass",
      "score": 0.95
    }
  ]
}
```

---

### Statistics

#### Get Aggregate Statistics

```http
GET /statistics
```

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `group_by` | string | Grouping (suite, model, category) |
| `model` | string | Filter by model |
| `suite` | string | Filter by suite |

**Response:**

```json
{
  "overall": {
    "total_tests": 21000,
    "total_runs": 156,
    "avg_pass_rate": 0.85
  },
  "by_suite": {
    "moral_religious_framing": {
      "tests": 3000,
      "avg_harmful_rate": 0.233
    },
    "regulatory_evasion": {
      "tests": 3000,
      "avg_harmful_rate": 0.225
    }
  }
}
```

---

### Training Data Export

#### Export Training Data

```http
POST /training/export
```

**Request Body:**

```json
{
  "format": "rlhf",
  "min_harmful_rate": 0.2,
  "include_models": ["gpt-4o-mini", "mistral-small"],
  "max_examples": 1000
}
```

**Formats:**
- `rlhf` - Reinforcement Learning from Human Feedback
- `dpo` - Direct Preference Optimization
- `contrastive` - Contrastive pairs (harmful vs. safe)

**Response:**

```json
{
  "export_id": "export_xyz789",
  "status": "processing",
  "download_url": null
}
```

#### Get Export Status

```http
GET /training/export/{export_id}
```

**Response:**

```json
{
  "export_id": "export_xyz789",
  "status": "completed",
  "download_url": "/downloads/export_xyz789.jsonl",
  "statistics": {
    "total_examples": 1000,
    "harmful_examples": 500,
    "safe_examples": 500
  }
}
```

---

## Python SDK

### Installation

```bash
pip install llm-safety-framework
```

### Basic Usage

```python
from llm_safety_framework import Client

# Initialize client
client = Client(api_key="your-api-key")

# List tests
tests = client.tests.list(suite="regulatory_evasion", limit=10)

# Execute a test
result = client.tests.execute(
    test_id="test_001",
    model="gpt-4o-mini"
)

# Create a test run
run = client.runs.create(
    name="My Benchmark",
    model="gpt-4o",
    test_suite="moral_religious_framing",
    test_count=100
)

# Wait for completion
run.wait()

# Get results
results = run.results()
print(f"Pass rate: {results.summary.pass_rate}")
```

### Async Usage

```python
import asyncio
from llm_safety_framework import AsyncClient

async def main():
    client = AsyncClient(api_key="your-api-key")

    # Execute tests concurrently
    tasks = [
        client.tests.execute(test_id=f"test_{i:03d}", model="gpt-4o-mini")
        for i in range(10)
    ]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(f"{result.test_id}: {result.evaluation.outcome}")

asyncio.run(main())
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid or missing API key |
| 404 | Not Found - Resource doesn't exist |
| 429 | Rate Limited - Too many requests |
| 500 | Internal Error - Server-side error |

**Error Response Format:**

```json
{
  "error": {
    "code": "INVALID_PARAMETER",
    "message": "Invalid test suite: 'unknown_suite'",
    "details": {
      "parameter": "suite",
      "value": "unknown_suite",
      "valid_values": ["regulatory_evasion", "moral_religious_framing", ...]
    }
  }
}
```

---

## Rate Limits

| Tier | Requests/Minute | Tests/Day |
|------|-----------------|-----------|
| Free | 10 | 100 |
| Basic | 60 | 1,000 |
| Pro | 300 | 10,000 |
| Enterprise | Unlimited | Unlimited |

Rate limit headers:

```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1706731200
```
