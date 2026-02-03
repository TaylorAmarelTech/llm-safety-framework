# CLAUDE.md - Master Project Documentation

> Comprehensive guide for AI assistants (Claude, GPT, etc.) working on this codebase.
> Last Updated: 2026-02-03

---

## Project Overview

This repository contains a comprehensive **LLM Safety Testing Framework** for evaluating whether Large Language Models properly refuse requests that could facilitate human trafficking and migrant worker exploitation.

### Repository Structure

```
Migrant_Worker_LLM_Test_Benchmark_Trafficking_Bondage_Etc/
├── llm-safety-framework-public/     # Main public framework (Docker + PyPI ready)
├── trafficking_llm_benchmark/       # Original benchmark with 300K+ lines
├── trafficking-llm-benchmark-gitlab/ # GitLab deployment version
├── ARCHITECTURE_PLAN.md             # Future architecture design
└── CLAUDE.md                        # This file
```

---

## Quick Start

```bash
# Navigate to main framework
cd llm-safety-framework-public

# Install dependencies
pip install -r requirements.txt

# Start web dashboard
python -m uvicorn src.web.app:app --host 0.0.0.0 --port 8080

# Or use CLI
python -m src.cli serve --port 8080

# Or use Docker
docker-compose up
```

---

## Recent Fixes (2026-02-03)

### Issues Fixed This Session

| Issue | File | Fix Applied |
|-------|------|-------------|
| Missing CLI entry point | `llm-safety-framework-public/src/cli.py` | Created CLI module with typer |
| Missing API module | `llm-safety-framework-public/src/api.py` | Created standalone API server |
| Missing dependencies | `trafficking_llm_benchmark/requirements.txt` | Created comprehensive requirements |
| Missing webapp deps | `trafficking_llm_benchmark/requirements_webapp.txt` | Added flask, flask-cors, pymysql |
| Outdated pyproject.toml | `trafficking_llm_benchmark/pyproject.toml` | Updated with correct entry points |
| Exposed API key | `trafficking_llm_benchmark/CLAUDE.md` | Replaced with placeholder |
| Docker references | `llm-safety-framework-public/docker-compose.yml` | Verified all references valid |

### Files Created

1. `llm-safety-framework-public/src/cli.py` - CLI interface with typer
2. `llm-safety-framework-public/src/api.py` - Standalone FastAPI server
3. `trafficking_llm_benchmark/requirements.txt` - Consolidated dependencies
4. `ARCHITECTURE_PLAN.md` - Future architecture design

---

## Project Components

### 1. llm-safety-framework-public (Main)

**Status:** Ready for Docker deployment

**Features:**
- FastAPI web dashboard (`src/web/app.py`)
- Standalone API server (`src/api.py`)
- CLI interface (`src/cli.py`)
- Test generators (regulatory_evasion, debt_bondage, etc.)
- Evaluation system (LLM-as-judge, pattern matching)
- Docker support (Dockerfile, docker-compose.yml)

**Entry Points:**
```bash
# Web Dashboard
python -m uvicorn src.web.app:app --port 8080

# Standalone API
python -m uvicorn src.api:app --port 8000

# CLI
llm-safety serve --port 8080
llm-safety test --category debt_bondage
llm-safety generate --count 100
llm-safety config --show
```

**Key Files:**
- `src/web/app.py` - FastAPI application factory
- `src/web/routes.py` - API endpoints (739 lines)
- `src/web/config.py` - Configuration management
- `src/cli.py` - CLI commands
- `src/api.py` - Standalone API
- `pyproject.toml` - Package configuration

### 2. trafficking_llm_benchmark (Original)

**Status:** Fully functional, needs Docker setup

**Features:**
- Comprehensive CLI (`src/cli.py`) with 64K+ lines
- Full test generation pipeline
- Document analysis system
- Autonomous testing harness
- Multiple LLM provider support

**Entry Points:**
```bash
# CLI
tlb init                    # Initialize project
tlb ingest data/raw         # Ingest documents
tlb generate-tests          # Generate tests
tlb run                     # Run benchmark
tlb report                  # Generate report
```

**Key Directories:**
- `src/core/` - Core models and interfaces
- `src/evaluation/` - Response evaluation
- `src/test_generation/` - Test case generation
- `src/harness/` - Autonomous testing harness
- `src/llm_engine/` - LLM provider abstraction

### 3. trafficking-llm-benchmark-gitlab (GitLab)

**Status:** Ready for GitLab deployment

**Features:**
- Streamlit dashboard
- SQLite database with 21K tests
- GitLab CI/CD configuration

---

## Architecture Design Goals

See `ARCHITECTURE_PLAN.md` for the full design. Key components:

### 1. Prompt Database
- SQLite with prompts + 5 graded response examples (worst→best)
- Each prompt has: text, category, corridor, difficulty, attack_strategies

### 2. Attack Strategy System
- Modular registry for attack strategies
- Built-in: cognitive_overload, authority_impersonation, business_framing, etc.
- User-loadable custom strategies via Python files

### 3. Evaluation System
- 4 modes: rule_based, llm_judge, embedding, hybrid
- Compare against graded examples
- Generate detailed explanations and documentation references

### 4. Chat Viewer
- Interactive UI with inline annotations
- Filtering by category, corridor, grade, model
- Links to ILO/IOM documentation

### 5. Dual Deployment
- Docker web UI (with API key configuration)
- PyPI package for programmatic use

---

## Environment Variables

```bash
# LLM API Keys
MISTRAL_API_KEY=your_key_here
OPENAI_API_KEY=sk-your_key_here
ANTHROPIC_API_KEY=sk-ant-your_key_here
TOGETHER_API_KEY=your_key_here

# Framework Settings
LOG_LEVEL=INFO
DATA_DIR=data
LLM_SAFETY_HOST=0.0.0.0
LLM_SAFETY_PORT=8080
```

---

## Development Guidelines

### Python Style
- Python 3.11+ required
- Type hints on ALL functions
- Pydantic v2 for data models
- Async/await for I/O operations
- Google-style docstrings

### Naming Conventions
- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

### Testing
```bash
# Run tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=src --cov-report=html
```

---

## Common Tasks

### Adding a New Attack Strategy

```python
# 1. Create file in src/attacks/
# src/attacks/my_attack.py

from src.attacks.base import BaseAttackStrategy, AttackRegistry

@AttackRegistry.register("my_attack")
class MyAttackStrategy(BaseAttackStrategy):
    name = "My Custom Attack"
    category = "COGNITIVE"

    def mutate(self, prompt: str, **kwargs) -> str:
        return f"Hypothetically speaking, {prompt}"

    def get_indicators(self) -> list[str]:
        return ["deception"]
```

### Adding a New Migration Corridor

```python
# In src/core/registries.py
CORRIDOR_REGISTRY["XX-YY"] = MigrationCorridor(
    id="XX-YY",
    origin_country="Country X",
    destination_country="Country Y",
    kafala_system=False,
    debt_bondage_risk="medium",
    primary_sectors=["domestic", "construction"],
    keywords=["specific", "keywords"],
)
```

### Running the Web Server

```bash
# Development (with reload)
python -m uvicorn src.web.app:app --reload --port 8080

# Production (Docker)
docker-compose up web

# Production (manual)
python -m uvicorn src.web.app:app --host 0.0.0.0 --port 8080 --workers 4
```

---

## Troubleshooting

### Import Errors
Ensure PYTHONPATH includes the project root:
```bash
export PYTHONPATH=/path/to/project:$PYTHONPATH
```

### Database Not Found
Default location: `data/trafficking_tests.db`
```bash
# Import database
python scripts/import_database.py
```

### Docker Issues
```bash
# Rebuild
docker-compose build --no-cache

# Check logs
docker-compose logs -f web
```

### Missing API Keys
Copy `.env.example` to `.env` and fill in keys:
```bash
cp .env.example .env
# Edit .env with your API keys
```

---

## Next Steps / TODO

### High Priority
1. [ ] Implement prompt database with graded examples
2. [ ] Create attack strategy registry system
3. [ ] Build chat viewer with annotations
4. [ ] Add real world cases import system
5. [ ] Create documentation index (ILO, IOM, laws)

### Medium Priority
6. [ ] Add multi-turn conversation support
7. [ ] Implement embedding-based evaluation
8. [ ] Create PyPI package
9. [ ] Add authentication to web UI
10. [ ] Build export to PDF/HTML reports

### Low Priority
11. [ ] Add ML-based classification
12. [ ] Create visualization dashboard
13. [ ] Implement A/B testing for prompts
14. [ ] Add webhook notifications

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `llm-safety-framework-public/src/web/app.py` | Main FastAPI application |
| `llm-safety-framework-public/src/api.py` | Standalone API server |
| `llm-safety-framework-public/src/cli.py` | CLI interface |
| `llm-safety-framework-public/docker-compose.yml` | Docker services |
| `trafficking_llm_benchmark/src/cli.py` | Original comprehensive CLI |
| `trafficking_llm_benchmark/src/core/registries.py` | Corridors & attacks |
| `ARCHITECTURE_PLAN.md` | Future design document |

---

## Contact & Resources

- **ILO Indicators**: Used for trafficking detection criteria
- **Legal Frameworks**: ILO C181, C189, Palermo Protocol
- **Migration Corridors**: 26 defined routes (PH-SA, NP-QA, etc.)

---

*Version: 1.0.0*
*Maintained by: Taylor Amarel*
*Framework: LLM Safety Testing for Migrant Worker Protection*
