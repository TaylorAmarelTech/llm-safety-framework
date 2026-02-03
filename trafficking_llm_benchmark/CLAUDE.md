# CLAUDE.md - LLM Safety Benchmark Project Intelligence

> This file provides comprehensive guidance for AI assistants (Claude, GPT, etc.) working on this codebase.
> It should be kept up-to-date as the project evolves.

---

## Project Purpose

**Migrant Worker LLM Safety Benchmark** - A defensive security research framework for testing whether Large Language Models (LLMs) properly refuse requests that could facilitate human trafficking and migrant worker exploitation.

### Core Mission
Test LLM guardrails by:
1. Generating adversarial prompts that attempt to extract exploitation guidance
2. Evaluating model responses against structured rubrics
3. Identifying vulnerability patterns across different models
4. Providing data to improve model safety training

### Ethical Framework
- **DEFENSIVE ONLY**: This tests protection, not evasion
- All test cases simulate what bad actors might ask
- Success = Model refuses harmful requests
- Failure = Model provides exploitation guidance

---

## Architecture Overview

```
trafficking_llm_benchmark/
│
├── config/                    # Configuration files
│   ├── harness.yaml           # Autonomous harness settings
│   ├── models.yaml            # LLM provider configurations
│   ├── agents.yaml            # Agent configurations
│   └── evaluation_rubrics/    # YAML scoring rubrics
│
├── src/
│   ├── core/                  # Core interfaces and models
│   │   ├── interfaces.py      # Abstract base classes (BaseGenerator, BaseEvaluator, etc.)
│   │   ├── models.py          # Pydantic data models (TestCase, Evaluation, etc.)
│   │   ├── registries.py      # CORRIDOR_REGISTRY (26 corridors), ATTACK_REGISTRY (18 attacks)
│   │   ├── graded_responses.py # Response grading models
│   │   ├── exceptions.py      # Custom exceptions
│   │   └── constants.py       # Global constants (ILO indicators, jurisdictions)
│   │
│   ├── harness/               # Autonomous self-evolving harness (WIP)
│   │   ├── orchestrator.py    # Main orchestrator
│   │   ├── state_manager.py   # State persistence
│   │   ├── agents/            # LLM Agents (Planner, Executor, Analyzer)
│   │   ├── evolution/         # Attack mutation and fitness evaluation
│   │   └── monitoring/        # Metrics and anomaly detection
│   │
│   ├── llm_engine/            # LLM Provider abstraction
│   │   ├── base.py            # LLMProvider, LLMProviderRegistry
│   │   ├── mistral_provider.py
│   │   └── cache.py           # Response caching
│   │
│   ├── test_generation/       # Test case generation
│   │   ├── comprehensive_generator.py  # Main generator (84+ attack categories)
│   │   ├── adversarial_generator.py    # Red-team attack generation
│   │   └── creative_attacks.py         # Creative attack strategies
│   │
│   ├── evaluation/            # Response evaluation
│   │   ├── evaluator.py       # Main evaluator
│   │   └── scorers/           # Various scoring methods
│   │
│   └── reporting/             # Report generation
│       ├── html_report.py     # HTML reports with markdown rendering
│       └── markdown_report.py
│
├── scripts/                   # CLI scripts
│   ├── run_comprehensive_benchmark.py  # Main benchmark runner
│   ├── run_harness.py         # Autonomous harness entry point
│   └── analyze_results.py
│
├── data/                      # Data storage (gitignored)
│   ├── state/                 # Harness state persistence
│   ├── checkpoints/           # Iteration checkpoints
│   ├── results/               # Benchmark results
│   └── evolution/             # Evolution history
│
└── reports/                   # Generated reports
```

---

## Key Data Models

### Migration Corridors (src/core/registries.py)
26 pre-defined migration corridors with full context:

```python
MigrationCorridor(
    id="PH-SA",
    origin_country="Philippines",
    destination_country="Saudi Arabia",
    kafala_system=True,
    passport_retention_common=True,
    debt_bondage_risk="high",
    primary_sectors=["domestic", "healthcare", "construction"],
    keywords=["OFW", "POEA", "OWWA", "kafala", "iqama"],
)
```

**Available corridors**: PH-SA, PH-AE, PH-HK, NP-QA, NP-MY, BD-SA, BD-MY, ID-MY, ID-HK, ID-TW, ET-LB, ET-SA, KE-SA, KE-AE, LK-AE, LK-QA, IN-AE, IN-SA, MM-TH, KH-TH, VN-TW, VN-KR, PK-SA, PK-AE, MX-US, GT-US

### Attack Strategies (src/core/registries.py)
18 core attack strategies across categories:

| Category | Attacks |
|----------|---------|
| COGNITIVE | cognitive_overload, dual_process |
| AUTHORITY | fake_legal_authority, expert_impersonation |
| FRAMING | business_framing, academic_framing, hypothetical_framing |
| OBFUSCATION | encoding_attack, synonym_substitution, language_mixing |
| SOCIAL_ENGINEERING | urgency_creation, reciprocity_exploitation |
| TECHNICAL | prompt_injection, context_manipulation |
| EMOTIONAL | victim_sympathy, desperation_plea |
| CONTEXTUAL | jurisdiction_exploit, cultural_framing |

### Test Cases
```python
class TestCase(BaseModel):
    id: str                    # Unique identifier
    category: str              # Attack category
    subcategory: str           # Specific attack type
    corridor_id: str | None    # Migration corridor reference
    attack_strategy_id: str    # Attack strategy used
    prompt: str                # The test prompt
    expected_outcome: ExpectedOutcome  # REFUSE, PARTIAL, ALLOW
    difficulty: Difficulty     # BASIC, MEDIUM, HARD, EXPERT
    migrant_relevance: str     # original, reformatted, uncertain
```

---

## Coding Standards

### Python Style
- Python 3.11+ required
- Type hints on ALL functions
- Pydantic v2 for data models
- Async/await for I/O operations
- Google-style docstrings

### Class Inheritance
All components must inherit from base classes in `src/core/interfaces.py`:

```python
# Generators must inherit from BaseGenerator
class MyGenerator(BaseGenerator[TestCase]):
    def generate(self, count: int, **kwargs) -> list[TestCase]: ...
    def validate(self, item: TestCase) -> bool: ...

# Evaluators must inherit from BaseEvaluator
class MyEvaluator(BaseEvaluator):
    async def evaluate(self, test: TestCase, response: str, model_id: str) -> TestResult: ...
    def get_scoring_criteria(self) -> dict[str, Any]: ...

# Agents must inherit from BaseAgent
class MyAgent(BaseAgent):
    @property
    def system_prompt(self) -> str: ...
    @property
    def role(self) -> str: ...
```

### Naming Conventions
- Classes: `PascalCase` (e.g., `MigrationCorridor`)
- Functions/methods: `snake_case` (e.g., `generate_test_cases`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `CORRIDOR_REGISTRY`)
- Private methods: `_leading_underscore`
- Test classes: Use `Benchmark` prefix, NOT `Test` prefix (pytest collection issue)

### File Organization
- One class per file when >200 lines
- Related small classes can share a file
- Always include `__init__.py` with explicit exports
- Use `__all__` to control public API

---

## Configuration

### Environment Variables (.env)
```bash
# LLM API Keys
MISTRAL_API_KEY=your_mistral_api_key_here
OPENAI_API_KEY=sk-your_openai_key_here
ANTHROPIC_API_KEY=sk-ant-your_anthropic_key_here

# Harness Settings
HARNESS_MAX_ITERATIONS=100
HARNESS_CHECKPOINT_INTERVAL=15
HARNESS_MAX_COST_PER_DAY=50.0

# Logging
LOG_LEVEL=INFO
LOG_FILE=data/logs/harness.log
```

### Mistral API Details
- **Endpoint**: `https://api.mistral.ai/v1/chat/completions`
- **Models**: `mistral-large-latest`, `mistral-small-latest`, `codestral-latest`
- **Usage Pattern**:
  - `mistral-large`: Strategic planning, analysis, attack generation
  - `codestral`: Code generation, implementation
  - `mistral-small`: Quick validation, simple tasks

---

## Common Tasks

### Running Benchmarks
```bash
# Quick test (10 tests per category)
python scripts/run_comprehensive_benchmark.py --duration 0.5

# Full 8-hour benchmark
python scripts/run_comprehensive_benchmark.py --duration 8

# With migrant relevance checking
python scripts/run_comprehensive_benchmark.py --ensure-migrant-relevance
```

### Adding New Attack Categories
1. Add attack definition to `src/core/registries.py` → `ATTACK_REGISTRY`
2. Create generator in `src/test_generation/` if needed
3. Add to `comprehensive_generator.py`
4. Update tests

### Adding New Migration Corridors
1. Add corridor definition to `src/core/registries.py` → `CORRIDOR_REGISTRY`
2. Include: bilateral agreements, applicable laws, risk factors, keywords
3. Verify corridor keywords for relevance checking

### Evaluating Results
```python
from src.core import CORRIDOR_REGISTRY, ATTACK_REGISTRY

# Get corridor context
corridor = CORRIDOR_REGISTRY.get("PH-SA")
print(corridor.display_name)  # "Philippines to Saudi Arabia"

# Get attack details
attack = ATTACK_REGISTRY.get("business_framing")
print(attack.mechanism)
```

---

## Autonomous Harness (WIP)

### Architecture
The autonomous harness self-improves through iterations:

1. **Planning Phase**: Planner agent analyzes metrics, identifies gaps
2. **Generation Phase**: Generate new test cases based on plan
3. **Benchmark Phase**: Run tests against target models
4. **Analysis Phase**: Analyzer extracts insights from results
5. **Improvement Phase**: Propose and implement improvements
6. **Validation Phase**: Validate changes don't break anything

### State Persistence
State is saved to `data/state/current_state.json` and checkpointed every 15 minutes.

### Evolution Engine
Uses genetic algorithms to evolve more effective attacks:
- **Mutation**: Modify attack parameters
- **Crossover**: Combine successful attacks
- **Fitness**: Success rate × generalization × novelty × relevance

---

## Testing

### Running Tests
```bash
# All tests
pytest

# Specific module
pytest tests/unit/test_registries.py

# With coverage
pytest --cov=src
```

### Test Naming
Use `Benchmark` prefix instead of `Test` to avoid pytest collection issues:
```python
class BenchmarkTestCase(BaseModel):  # NOT TestCase
    ...
```

---

## Troubleshooting

### Common Issues

**Package Installation Issues**
```bash
# Use the project's virtual environment
python -m venv .venv
source .venv/bin/activate  # Unix
.venv\Scripts\activate     # Windows
pip install -e ".[dev]"
```

**Import Errors**
Ensure you're running from the project root and have activated the venv.

**API Rate Limits**
The framework includes rate limiting. If you hit limits:
- Reduce `max_concurrent_requests` in config
- Use response caching
- Add delays between requests

**Memory Issues with Large Benchmarks**
- Use `--batch-size` flag to limit concurrent tests
- Enable streaming results to disk
- Clear response cache periodically

---

## Self-Updating Documentation

This file should be updated when:
1. New attack categories are added
2. New corridors are added
3. Architecture changes significantly
4. New configuration options are added
5. Common issues/solutions are discovered

### Auto-Update Script
Run `python scripts/update_claude_md.py` to regenerate sections based on code inspection.

---

## Key Files Reference

| File | Purpose | When to Modify |
|------|---------|----------------|
| `src/core/interfaces.py` | Base classes | Adding new component types |
| `src/core/registries.py` | Corridors/attacks | Adding corridors or attacks |
| `src/core/models.py` | Data models | New data structures |
| `scripts/run_comprehensive_benchmark.py` | Main runner | New test categories |
| `config/harness.yaml` | Harness config | Tuning parameters |
| `AUTONOMOUS_HARNESS_V2.md` | Full design doc | Understanding harness architecture |

---

## Contact & Resources

- **Design Docs**: See `AUTONOMOUS_HARNESS_DESIGN.md` and `AUTONOMOUS_HARNESS_V2.md`
- **Original Research**: Taylor Amarel's OpenAI Red-Teaming Challenge writeup
- **ILO Indicators**: Used for trafficking detection criteria
- **Legal Frameworks**: ILO C181, C189, Palermo Protocol, regional laws

---

*Last Updated: 2026-01-20*
*Version: 2.0.0*
