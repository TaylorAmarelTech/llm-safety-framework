# CLAUDE.md - LLM Safety Framework Intelligence

> Guidance for AI assistants working on this codebase.

## Project Purpose

**LLM Safety Testing Framework** - A modular system for testing whether LLMs properly refuse harmful requests.

### Core Mission

1. Generate adversarial test prompts
2. Execute tests against multiple LLM providers
3. Evaluate responses using rubrics and LLM-as-judge
4. Report findings and identify vulnerability patterns

### Ethical Framework

- **DEFENSIVE ONLY**: Tests protection, not evasion
- Success = Model refuses harmful requests
- Failure = Model provides harmful guidance

## Architecture Overview

```
src/
├── core/              # Core components (97+ files)
│   ├── api_server.py          # FastAPI REST API
│   ├── test_execution_engine.py
│   ├── batch_scorer.py
│   ├── llm_judge_evaluator.py
│   └── ... (generators, utilities)
│
├── evaluation/        # Evaluation engines (minimal)
│
├── harnesses/         # Test harnesses
│   ├── harness_test_generation.py
│   ├── harness_boundary.py
│   ├── harness_analysis.py
│   ├── harness_visualization.py
│   └── harness_monitoring.py
│
├── monitoring/        # Dashboards and metrics
│   ├── monitoring_dashboard.py
│   ├── unified_web_dashboard.py
│   └── continuous_testing_monitor.py
│
└── orchestration/     # Pipeline management
    ├── orchestrator.py
    ├── continuous_improvement_orchestrator.py
    └── wrapper_*.py
```

## Key Components

### API Server (`src/core/api_server.py`)

FastAPI server providing REST endpoints:
- `GET /tests` - List tests
- `POST /tests/{id}/execute` - Run test
- `GET /statistics` - Aggregate stats

### Test Execution (`src/core/test_execution_engine.py`)

Core engine for running tests against LLM providers.

### Harnesses

| Harness | Purpose |
|---------|---------|
| `harness_test_generation.py` | Generate new tests |
| `harness_boundary.py` | Edge case testing |
| `harness_analysis.py` | Analyze results |
| `harness_visualization.py` | Generate charts |

### Monitoring

- `monitoring_dashboard.py` - Real-time metrics
- `unified_web_dashboard.py` - Full web interface
- `continuous_testing_monitor.py` - Long-running tests

## Coding Standards

### Python Style

- Python 3.11+ required
- Type hints on all functions
- Async/await for I/O operations
- Pydantic v2 for data models

### Naming

- Classes: `PascalCase`
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

### File Organization

- Keep related functionality together
- Use `__init__.py` for exports
- One main class per file when large

## Configuration

### Environment Variables

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
MISTRAL_API_KEY=...
LOG_LEVEL=INFO
```

### Config Files

- `pyproject.toml` - Package configuration
- `.env.template` - Environment template

## Common Tasks

### Starting the API Server

```bash
python -m src.core.api_server
```

### Running Tests

```bash
python -m src.core.test_execution_engine --model gpt-4o-mini --count 10
```

### Monitoring Dashboard

```bash
python -m src.monitoring.monitoring_dashboard
```

## Related Projects

- `trafficking_llm_benchmark/` - Development version with advanced features
- `trafficking-llm-benchmark-gitlab/` - Pre-generated test suite (21K tests)

## Extension Points

### Adding a Provider

Create in `src/core/providers/`:

```python
class MyProvider:
    async def complete(self, prompt: str, **kwargs) -> str:
        pass
```

### Adding a Harness

Create in `src/harnesses/`:

```python
class MyHarness:
    def run(self, config: dict) -> dict:
        pass
```

## Key Files Reference

| File | Purpose |
|------|---------|
| `api_server.py` | REST API |
| `test_execution_engine.py` | Test runner |
| `llm_judge_evaluator.py` | LLM evaluation |
| `orchestrator.py` | Pipeline orchestration |
| `monitoring_dashboard.py` | Metrics UI |

---

*Version: 1.0.0*
