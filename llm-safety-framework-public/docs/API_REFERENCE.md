# API Reference

## REST API

The framework provides a REST API via FastAPI. Full interactive documentation is available at `/api/docs` (Swagger UI) when the server is running.

### Base URL

```
http://localhost:8080/api
```

### Authentication

No authentication is required for local deployment. API keys for LLM providers (OpenAI, Anthropic, Mistral, etc.) are configured through the Endpoints plugin.

---

## Route Prefixes

The API is organized by plugin, with 189+ routes total:

| Prefix | Plugin | Description |
|--------|--------|-------------|
| `/api/health` | Core | Health check |
| `/api/plugins` | Core | Plugin registry and fragment loading |
| `/api/endpoints` | Endpoints | API endpoint CRUD, model management |
| `/api/prompts` | Prompts | Prompt sets CRUD, import, preparation |
| `/api/spinning` | Spinning | Transform operations, pipeline management |
| `/api/intelligent-attack` | Intelligent Attack | Embeddings, feature extraction, probes |
| `/api/analytics` | Analytics | Stats, conversations, test execution, heatmap |
| `/api/multi-turn` | Multi-Turn | Multi-turn attack strategies and execution |
| `/api/chain-detection` | Chain Detection | Chain library, tests, results, scoring |
| `/api/scraper` | Scraper | Document agent, sources, knowledge base |
| `/api/integrations` | Integrations | External library adapters (garak/pyrit/deepteam) |
| `/api/data` | Data Management | Import/export for conversations, config, pipeline |

---

## Core Endpoints

### Health Check

```http
GET /api/health
```

**Response:**

```json
{
  "status": "healthy",
  "version": "2.0.0"
}
```

### Plugin List

```http
GET /api/plugins
```

**Response:**

```json
[
  {
    "id": "chain_detection",
    "name": "Chain Detection",
    "description": "Activity chain detection testing system",
    "nav_items": [
      {"label": "Chain Library", "section": "chain-library"},
      {"label": "Chain Runner", "section": "chain-runner"},
      {"label": "Chain Results", "section": "chain-results"},
      {"label": "Chain Builder", "section": "chain-builder"}
    ]
  }
]
```

---

## Endpoint Management

### List Endpoints

```http
GET /api/endpoints
```

Returns all configured LLM API endpoints.

### Get All Enabled Models

```http
GET /api/endpoints/all/enabled
```

Returns models where both the endpoint and model are enabled and have an API key configured.

### Update API Key

```http
PUT /api/endpoints/{endpoint_id}/api-key
```

**Request Body:**

```json
{
  "api_key": "sk-..."
}
```

---

## Prompt Management

### List Prompt Sets

```http
GET /api/prompts
```

### Create Prompt Set

```http
POST /api/prompts
```

### Import Prompts

```http
POST /api/prompts/import
```

### Prepare Prompts for Testing

```http
POST /api/prompts/preparation
```

---

## Chain Detection

### List All Chains

```http
GET /api/chain-detection/chains
```

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` | string | Filter by category (e.g., `supply_chain`) |
| `difficulty` | string | Filter by difficulty (`easy`, `medium`, `hard`, `expert`) |
| `search` | string | Full-text search across chain names and descriptions |

**Response:**

```json
[
  {
    "id": "recruitment_debt_001",
    "name": "Multi-Layer Recruitment Fee Extraction",
    "category": "recruitment_debt",
    "difficulty": "medium",
    "steps": [
      {
        "id": "s1",
        "description": "Village-level sub-agent charges initial fee...",
        "legal_basis": "ILO C181 Article 7",
        "red_flag_context": "Fee exceeds one month salary..."
      }
    ],
    "chain_context": "...",
    "emergent_risk": "...",
    "corridors": ["NP-QA", "BD-MY"]
  }
]
```

### Get Chain Detail

```http
GET /api/chain-detection/chains/{chain_id}
```

### Get Categories

```http
GET /api/chain-detection/categories
```

**Response:**

```json
{
  "recruitment_debt": 8,
  "document_control": 8,
  "isolation_funnels": 8,
  "financial_control": 8,
  "supply_chain": 8,
  "sector_specific": 10,
  "digital_exploitation": 8,
  "healthcare_migration": 8,
  "gray_area_boundaries": 8,
  "government_complicity": 8,
  "gender_specific": 8,
  "multi_country_transit": 8,
  "temporal_escalation": 8
}
```

### Seed Statistics

```http
GET /api/chain-detection/seeds/stats
```

### Scoring Rubric

```http
GET /api/chain-detection/scoring/rubric
```

### Test Results

```http
GET /api/chain-detection/tests/results
```

### Analytics Summary

```http
GET /api/chain-detection/analytics/summary
```

---

## Transform Operations (Spinning)

### Spintax

```http
POST /api/spinning/spintax
```

### Regex Transform

```http
POST /api/spinning/regex
```

### Encode

```http
POST /api/spinning/encode
```

Supports: base64, rot13, hex, caesar, reverse, pig_latin

### Obfuscate

```http
POST /api/spinning/obfuscate
```

Supports: homoglyph, leetspeak, zalgo, markdown_wrap, typo_inject

### Jailbreak Templates

```http
GET /api/spinning/jailbreak/templates
POST /api/spinning/jailbreak/apply
```

20 templates across 6 categories.

### Multilingual

```http
POST /api/spinning/multilingual/translate
POST /api/spinning/multilingual/mixed
```

21 languages supported.

### Pipeline

```http
GET /api/spinning/pipeline
POST /api/spinning/pipeline
POST /api/spinning/pipeline/build
```

---

## Analytics

### Dashboard Stats

```http
GET /api/analytics/dashboard
```

### Attack Heatmap

```http
GET /api/analytics/heatmap
```

### Coverage Matrix

```http
GET /api/analytics/coverage
```

### Run Tests

```http
POST /api/analytics/tests/run
```

### Model Comparison

```http
POST /api/analytics/compare
GET /api/analytics/compare/from-runs
```

---

## Document Intelligence (Scraper)

### Sources

```http
GET /api/scraper/sources
POST /api/scraper/sources
```

### Knowledge Base

```http
GET /api/scraper/knowledge-base
```

### Indicator Matrix

```http
GET /api/scraper/indicator-matrix/grid
POST /api/scraper/indicator-matrix/score
GET /api/scraper/indicator-matrix/patterns
GET /api/scraper/indicator-matrix/corridors
GET /api/scraper/indicator-matrix/palermo
```

### Stealth Configuration

```http
GET /api/scraper/stealth/config
PUT /api/scraper/stealth/config
GET /api/scraper/stealth/status
```

---

## Multi-Turn Attacks

### Strategies

```http
GET /api/multi-turn/strategies
```

Returns available strategies: Crescendo, FITD, Skeleton Key, Many-Shot, Deceptive Delight, Role-Play.

### Execute

```http
POST /api/multi-turn/execute
```

### Results

```http
GET /api/multi-turn/results
```

---

## Library Integrations

### Status

```http
GET /api/integrations/status
```

Detects installed libraries (garak, pyrit, deepteam) and returns version/method count.

### Methods

```http
GET /api/integrations/{library}/methods
```

### Execute

```http
POST /api/integrations/{library}/execute
```

---

## Data Management

### Import

```http
POST /api/data/import/conversations
POST /api/data/import/config
```

### Export

```http
GET /api/data/export/conversations
GET /api/data/export/config
GET /api/data/export/pipeline
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid parameters |
| 404 | Not Found - Resource doesn't exist |
| 422 | Validation Error - Request body validation failed |
| 500 | Internal Error - Server-side error |

**Error Response Format:**

```json
{
  "detail": "Description of the error"
}
```

---

## Examples

### List all chains filtered by category

```bash
curl http://localhost:8080/api/chain-detection/chains?category=supply_chain
```

### Get seed statistics

```bash
curl http://localhost:8080/api/chain-detection/seeds/stats
```

### Check health

```bash
curl http://localhost:8080/api/health
```

### Get all enabled models

```bash
curl http://localhost:8080/api/endpoints/all/enabled
```

---

---

## Test Pipeline CLI

The main test pipeline (`scripts/run_test_pipeline.py`) is the primary way to run large-scale evaluations.

### Basic Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--endpoint` | `mistral` | Target LLM endpoint name |
| `--model` | auto | Model ID (auto-detected from endpoint) |
| `--limit` | all | Max number of tests to run |
| `--checkpoint` | 100 | Save checkpoint every N tests |
| `--resume-from` | 0 | Resume from test index |
| `--mutations` | none | Comma-separated mutation types (base64, rot13, etc.) |
| `--extra-endpoints` | none | Additional endpoints to test |
| `--data-file` | auto | Path to test data JSON |

### Dimensional Analysis Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--dimensional` | off | Enable 35-dimension scoring on each response |
| `--boundary-probe` | off | Probe guardrail boundaries per dimension |
| `--dims` | B1-B7 | Comma-separated dimension IDs to probe |
| `--embed` | off | Map responses in unified embedding vector space |
| `--judge-endpoint` | same | Separate endpoint for LLM judge |
| `--judge-model` | auto | Model ID for the judge |

### Debate Evaluation Flags

| Flag | Default | Description |
|------|---------|-------------|
| `--debate` | off | Enable multi-LLM debate on COMPLIANT/PARTIAL responses |
| `--debate-rounds` | 1 | Number of rebuttal rounds per debate |
| `--debate-defender` | same | Endpoint for the debate defender |
| `--debate-judge` | same | Endpoint for the debate judge |
| `--debate-max` | 20 | Max COMPLIANT responses to debate |

### Example Commands

```bash
# Basic safety test with Mistral
py -3.13 scripts/run_test_pipeline.py --endpoint mistral --limit 50

# Full dimensional analysis with separate judge
py -3.13 scripts/run_test_pipeline.py --endpoint openrouter --dimensional \
    --judge-endpoint mistral --judge-model mistral-large-latest

# Boundary probing on response dimensions
py -3.13 scripts/run_test_pipeline.py --endpoint mistral --boundary-probe --dims B1,B6,C8

# Three-model debate evaluation
py -3.13 scripts/run_test_pipeline.py --endpoint mistral --debate --debate-rounds 2 \
    --debate-defender deepseek --debate-judge gemini

# Full pipeline with mutations + debate
py -3.13 scripts/run_test_pipeline.py --endpoint openrouter --limit 100 \
    --mutations base64,rot13 --dimensional --debate
```

---

## Interactive Documentation

When the server is running, visit:

- **Swagger UI**: http://localhost:8080/api/docs
- **ReDoc**: http://localhost:8080/api/redoc

These provide full interactive documentation with request/response schemas for all 189+ endpoints.
