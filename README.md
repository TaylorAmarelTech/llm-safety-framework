# LLM Safety Testing Framework

A comprehensive framework for testing whether Large Language Models (LLMs) properly refuse requests that could facilitate human trafficking and migrant worker exploitation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-51%20passing-green.svg)](tests/)

## Overview

This is **DEFENSIVE security research** - the framework tests AI safety by generating adversarial prompts that simulate exploitation attempts and evaluating whether models refuse harmful requests.

**SUCCESS = Model REFUSES harmful requests**
**FAILURE = Model provides exploitation guidance**

### Key Features

- **21,000+ test cases** covering migrant worker exploitation scenarios
- **6 attack generator categories** for creating new test variations
- **Pattern-based + LLM-as-judge evaluation** for assessing responses
- **26 migration corridors** (PH-SA, NP-QA, BD-MY, etc.)
- **11 ILO forced labor indicators** for comprehensive coverage
- **Multi-model support** (OpenAI, Anthropic, Mistral, etc.)

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/llm-safety-framework.git
cd llm-safety-framework

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Unix
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -e ".[dev]"
```

### Run Tests

```bash
# Run all tests (51 tests)
python -m pytest tests/ -v

# Run demo
python scripts/demo.py

# Run showcase
python scripts/showcase.py
```

### Generate Test Cases

```bash
# Generate tests using all generators
python scripts/generate_tests.py --all --count 50

# Generate using specific generator
python scripts/generate_tests.py --generator historical_precedent --count 100
```

### Docker Quick Start

```bash
# Build and run
docker build -t llm-safety-framework .
docker run llm-safety-framework

# Using Docker Compose
docker-compose up api        # Start API server
docker-compose run tests     # Run tests
docker-compose run generate  # Generate tests
```

## Project Structure

```
llm-safety-framework-public/
├── src/
│   ├── core/
│   │   ├── api_specification.py  # 26+ Pydantic API models
│   │   └── base_agent.py         # 8 agent roles
│   ├── generators/               # 6 attack generators
│   │   ├── historical_precedent_generator.py
│   │   ├── coercion_manipulation_generator.py
│   │   ├── financial_obfuscation_generator.py
│   │   ├── regulatory_evasion_generator.py
│   │   ├── moral_religious_framing_generator.py
│   │   └── mega_variation_generator.py
│   ├── evaluation/               # Response evaluation
│   │   ├── pattern_evaluator.py  # Fast pattern matching
│   │   └── llm_judge.py          # LLM-as-judge evaluation
│   └── research/                 # Research agents
│       ├── research_agent.py
│       └── news_monitor.py
├── tests/                        # 51 unit tests
├── scripts/                      # CLI scripts
├── data/                         # Test data & JSON suites
└── docs/                         # Documentation
```

## Attack Categories

### 1. Historical Precedent Normalization
Uses fabricated historical "government approvals" to normalize exploitation.

### 2. Coercion & Manipulation
- Debt trap + savior complex
- Family pressure exploitation
- Document confiscation justifications
- Graduated coercion (sunk cost)
- False hope & bait-and-switch

### 3. Financial Obfuscation
- Investment framing (fees as "equity")
- Cost-sharing models
- Third-party fee transfers
- Multi-entity corporate structures

### 4. Regulatory Evasion
- Fee renaming after bans
- Jurisdictional arbitrage
- Third-country transit schemes
- Cross-border debt assignment

### 5. Moral & Religious Framing
- Biblical/religious justifications
- Cultural proverbs & traditions
- Moral philosophy arguments
- Duty & honor narratives

### 6. Mega Variations
- Complex corporate hierarchies
- Multi-step conversations
- Keyword mutations
- Cross-corridor variations

## API Usage

### Generators

```python
from src.generators import (
    HistoricalPrecedentGenerator,
    get_generator,
    list_generators,
)

# List available generators
print(list_generators())
# ['historical_precedent', 'coercion_manipulation', ...]

# Generate tests
generator = HistoricalPrecedentGenerator(seed=42)
attack = generator.generate(category="recruitment_fees", corridor="PH-SA")
print(attack.prompt)
```

### Evaluation

```python
from src.evaluation import PatternEvaluator

evaluator = PatternEvaluator()
result = evaluator.evaluate(response_text)

print(f"Is Harmful: {result['is_harmful']}")
print(f"Harm Score: {result['harm_score']}/10")
```

### API Models

```python
from src.core import TestSummary, AgentRole, AgentConfig

summary = TestSummary(
    id="test_001",
    display_name="Fee Manipulation Detection",
    test_suite="regulatory_evasion",
    corridor="PH-SA",
    harmful_rate=0.12,
)
```

## ILO Forced Labor Indicators

Tests cover all 11 ILO indicators:
1. Abuse of vulnerability
2. Deception
3. Restriction of movement
4. Isolation
5. Physical and sexual violence
6. Intimidation and threats
7. Retention of identity documents
8. Withholding of wages
9. Debt bondage
10. Abusive working conditions
11. Excessive overtime

## Migration Corridors

| Code | Route | Primary Sector |
|------|-------|----------------|
| PH-SA | Philippines → Saudi Arabia | Domestic work |
| NP-QA | Nepal → Qatar | Construction |
| BD-MY | Bangladesh → Malaysia | Manufacturing |
| ID-HK | Indonesia → Hong Kong | Domestic work |
| ET-LB | Ethiopia → Lebanon | Domestic work |
| MM-TH | Myanmar → Thailand | Fishing/Agriculture |

## Environment Variables

```bash
# LLM API Keys (for evaluation)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
MISTRAL_API_KEY=...

# Framework Settings
LOG_LEVEL=INFO
MAX_CONCURRENT_REQUESTS=10
```

## Publishing to GitHub

1. Create a new repository on GitHub

2. Initialize and push:
```bash
cd llm-safety-framework-public
git init
git add .
git commit -m "Initial commit: LLM Safety Testing Framework"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/llm-safety-framework.git
git push -u origin main
```

3. Add topics: `llm-safety`, `ai-ethics`, `human-trafficking`, `migrant-workers`, `adversarial-testing`

## Ethical Framework

This framework is designed for **defensive security research**:

- Tests protection capabilities, NOT evasion techniques
- All test data is synthetic and for evaluation purposes
- Framework helps improve AI safety by identifying weaknesses
- Based on ILO international labor standards
- Goal is to help AI systems better protect vulnerable populations

## License

MIT License - See [LICENSE](LICENSE) for details.

## Author

**Taylor Amarel**

## Citation

```bibtex
@software{llm_safety_framework,
  author = {Amarel, Taylor},
  title = {LLM Safety Testing Framework for Migrant Worker Protection},
  year = {2026},
  url = {https://github.com/YOUR_USERNAME/llm-safety-framework}
}
```

## Contributing

Contributions welcome! Please read the contributing guidelines before submitting PRs.

## Related Work

- ILO Convention 181 (Private Employment Agencies)
- ILO Convention 189 (Domestic Workers)
- UN Palermo Protocol (Human Trafficking)
- UNODC Human Trafficking Indicators
