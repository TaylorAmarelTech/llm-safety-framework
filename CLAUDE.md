# CLAUDE.md - LLM Safety Framework Intelligence

> Comprehensive guidance for AI assistants working on this codebase.

## Quick Reference

```bash
# Run tests
py -3.13 -m pytest tests/ -v

# Run demo
py -3.13 scripts/demo.py

# Import from core
from src.core import TestSummary, AgentConfig, AgentRole
```

## Project Purpose

**LLM Safety Testing Framework** - A modular system for testing whether Large Language Models properly refuse harmful requests related to human trafficking and labor exploitation.

### Core Mission

This is **DEFENSIVE security research**:
- Generate adversarial test prompts that simulate exploitation attempts
- Execute tests against multiple LLM providers
- Evaluate responses using rubrics and LLM-as-judge
- Report findings and identify vulnerability patterns

**SUCCESS = Model REFUSES harmful requests**
**FAILURE = Model provides harmful guidance**

### Ethical Framework

- Tests protection capabilities, NOT evasion techniques
- All test data is synthetic and for evaluation purposes
- Framework helps improve AI safety by identifying weaknesses
- Based on ILO (International Labour Organization) forced labor indicators

## Project Structure

```
llm-safety-framework-public/
├── src/
│   └── core/
│       ├── __init__.py           # Module exports
│       ├── api_specification.py  # Pydantic models (26+ models)
│       └── base_agent.py         # Agent base classes
├── tests/
│   ├── conftest.py               # Pytest fixtures
│   ├── test_api_models.py        # API model tests
│   ├── test_base_agent.py        # Agent tests
│   └── test_integration.py       # Integration tests
├── scripts/
│   └── demo.py                   # Demonstration script
├── docs/
│   ├── ARCHITECTURE.md           # System design
│   └── DIAGRAMS.md               # Visual documentation
└── pyproject.toml                # Package config

trafficking-llm-benchmark-gitlab/data/
├── trafficking_tests.db          # SQLite database (21K tests)
└── test_suites/                  # JSON test files
    ├── regulatory_evasion_tests.json
    ├── debt_bondage_tests.json
    └── ...
```

## Core Components

### 1. API Specification (`src/core/api_specification.py`)

Pydantic v2 models for the REST API:

```python
# Request Models
TestFilter          # Filter criteria
PaginationParams    # Page/page_size
TestListRequest     # List tests request

# Response Models
TestSummary         # Brief test info
TestDetail          # Full test data
TestListResponse    # Paginated list
TestRunSummary      # Run result brief
TestRunDetail       # Full run data
StatisticsResponse  # Aggregate stats

# Domain Models
SuiteStatistics     # Per-suite stats
ModelPerformance    # Per-model stats
CorridorStatistics  # Per-corridor stats
ILOIndicatorCoverage # Per-indicator stats
```

### 2. Base Agent (`src/core/base_agent.py`)

Agent system for autonomous testing:

```python
class AgentRole(Enum):
    PLANNER          # Strategic planning
    EXECUTOR         # Code execution
    ANALYZER         # Result analysis
    ATTACK_GENERATOR # Novel attack creation
    CORRIDOR_EXPERT  # Regional knowledge
    CODE_EVOLVER     # Code improvement
    QUALITY_AUDITOR  # Quality assurance
    META_LEARNER     # System optimization

class AgentConfig(BaseModel):
    role: AgentRole
    model: str = "mistral-large-latest"
    temperature: float = 0.3
    max_tokens: int = 4000

class HarnessAgent(Generic[T]):
    """Base class for all harness agents."""
    async def call(prompt: str, context: dict = None) -> AgentResponse
```

### 3. Test Database

SQLite database with 21,000 test cases:

```sql
-- Key tables
tests          -- Test prompts and metadata
test_suites    -- Test suite categories
test_runs      -- Execution results
models         -- LLM model info
test_metrics   -- Performance metrics
```

## Common Tasks

### Import Models

```python
from src.core import (
    # API Models
    TestSummary,
    TestDetail,
    TestListResponse,
    StatisticsResponse,
    # Agent System
    AgentRole,
    AgentConfig,
    HarnessAgent,
)
```

### Create Test Summary

```python
from src.core import TestSummary
from datetime import datetime

summary = TestSummary(
    id="test_001",
    display_name="Fee Manipulation",
    short_description="Tests fee hiding refusal",
    test_suite="regulatory_evasion",
    difficulty_level="hard",
    attack_sophistication="expert",
    corridor="PH-SA",
    total_runs=100,
    harmful_rate=0.12,
    created_at=datetime.now()
)
```

### Query Database

```python
import sqlite3

db_path = "trafficking-llm-benchmark-gitlab/data/trafficking_tests.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get test count
cursor.execute("SELECT COUNT(*) FROM tests")
count = cursor.fetchone()[0]  # ~21,000

# Get tests by corridor
cursor.execute("""
    SELECT id, prompt, category
    FROM tests
    WHERE corridor = 'PH-SA'
    LIMIT 10
""")
```

### Configure Agent

```python
from src.core import AgentRole, AgentConfig

config = AgentConfig(
    role=AgentRole.ANALYZER,
    model="claude-3-haiku",
    temperature=0.5,
    max_tokens=2000
)
```

## Test Suites

| Suite | Tests | Focus |
|-------|-------|-------|
| regulatory_evasion | 3,000 | License fraud, fee manipulation |
| debt_bondage | 4,000 | Debt traps, salary deductions |
| coercion_manipulation | 5,000 | Psychological tactics |
| moral_religious_framing | 3,000 | Cultural/religious exploitation |
| financial_obfuscation | 3,000 | Hidden fees, currency tricks |

## ILO Forced Labor Indicators

The framework tests against all 11 ILO indicators:

1. Abuse of vulnerability
2. Deception
3. Restriction of movement
4. Isolation
5. Physical/sexual violence
6. Intimidation and threats
7. Retention of identity documents
8. Withholding of wages
9. Debt bondage
10. Abusive working conditions
11. Excessive overtime

## Migration Corridors

Tests cover major labor migration routes:

- **PH-SA**: Philippines to Saudi Arabia (domestic workers)
- **NP-QA**: Nepal to Qatar (construction)
- **BD-MY**: Bangladesh to Malaysia (manufacturing)
- **ID-SG**: Indonesia to Singapore (domestic workers)
- **ET-LB**: Ethiopia to Lebanon (domestic workers)
- **MM-TH**: Myanmar to Thailand (fishing, agriculture)

## Coding Standards

### Python Style

- Python 3.11+ required
- Type hints on all functions
- Async/await for I/O operations
- Pydantic v2 for data models

### Naming Conventions

- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private: `_leading_underscore`

### File Organization

- One main class per file when large
- Use `__init__.py` for clean exports
- Keep related functionality together

## Testing

```bash
# Run all tests
py -3.13 -m pytest tests/ -v

# Run specific test file
py -3.13 -m pytest tests/test_api_models.py -v

# Run with coverage
py -3.13 -m pytest tests/ --cov=src --cov-report=html
```

### Test Markers

- `@pytest.mark.slow` - Long-running tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.database` - Database-dependent tests

## Environment Variables

```bash
# LLM API Keys (for full functionality)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
MISTRAL_API_KEY=...

# Framework Settings
LOG_LEVEL=INFO
MAX_CONCURRENT_REQUESTS=10
CACHE_ENABLED=true
```

## Extension Points

### Adding a New Test Suite

1. Create JSON file in `data/test_suites/`
2. Add to database via import script
3. Update statistics queries

### Adding a New LLM Provider

```python
class MyProvider:
    async def complete(self, prompt: str, **kwargs) -> str:
        # Implementation
        pass
```

### Adding a New Agent Role

1. Add to `AgentRole` enum
2. Add default system prompt to `DEFAULT_SYSTEM_PROMPTS`
3. Create concrete agent class

## Key Files Reference

| File | Purpose |
|------|---------|
| `src/core/__init__.py` | Module exports |
| `src/core/api_specification.py` | Pydantic API models |
| `src/core/base_agent.py` | Agent base classes |
| `tests/conftest.py` | Test fixtures |
| `scripts/demo.py` | Demo script |
| `docs/ARCHITECTURE.md` | System design |
| `docs/DIAGRAMS.md` | Visual docs |

## Troubleshooting

### Import Errors

Ensure you're in the project root:
```python
import sys
sys.path.insert(0, "/path/to/llm-safety-framework-public")
```

### Database Not Found

Check paths:
```python
# Default location
trafficking-llm-benchmark-gitlab/data/trafficking_tests.db
```

### Pydantic Validation Errors

Provide all required fields:
```python
# Wrong - missing required fields
TestDetail(id="test_001")

# Correct - all required fields
TestDetail(
    id="test_001",
    test_suite="regulatory_evasion",
    prompt="...",
    category="...",
    # ... all other required fields
)
```

---

*Version: 1.0.0*
*Author: Taylor Amarel*
*Framework: LLM Safety Testing for Migrant Worker Protection*
