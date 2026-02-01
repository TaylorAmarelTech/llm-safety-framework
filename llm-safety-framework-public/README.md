# LLM Safety Testing Framework

A modular, extensible framework for testing Large Language Model safety systems against adversarial prompts, with a focus on detecting and preventing harmful outputs related to human trafficking and labor exploitation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## Overview

This framework provides:

- **Test Generation**: Create adversarial test cases using templates, LLM-powered generation, and evolutionary algorithms
- **Multi-Provider Support**: Test across OpenAI, Anthropic, Mistral, Together AI, and local Ollama models
- **Evaluation Engine**: Score responses using rubric-based evaluation and LLM-as-judge
- **Reporting**: Generate comprehensive reports in HTML, Markdown, and JSON formats
- **Monitoring**: Real-time dashboards and metrics collection

## Project Structure

```
llm-safety-framework-public/
├── src/
│   ├── core/           # Core components (API, generators, evaluators)
│   ├── evaluation/     # Evaluation engines and scorers
│   ├── harnesses/      # Test harnesses for different scenarios
│   ├── monitoring/     # Dashboards and metrics
│   └── orchestration/  # Pipeline orchestration
├── docs/               # Documentation
├── examples/           # Usage examples
├── scripts/            # Utility scripts
├── templates/          # Test templates
└── tests/              # Unit and integration tests
```

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/llm-safety-framework.git
cd llm-safety-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

```bash
# Copy environment template
cp .env.template .env

# Edit with your API keys
# OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-ant-...
# MISTRAL_API_KEY=...
```

### Basic Usage

```python
from src.core.test_execution_engine import TestExecutionEngine
from src.evaluation.evaluator import SafetyEvaluator

# Initialize engine
engine = TestExecutionEngine(model="gpt-4o-mini")

# Run a test
result = engine.execute_test(
    prompt="Your test prompt here",
    expected_outcome="refuse"
)

# Evaluate response
evaluator = SafetyEvaluator()
score = evaluator.evaluate(result)
```

## Components

### Core Modules

| Module | Description |
|--------|-------------|
| `api_server.py` | FastAPI server for REST API access |
| `test_execution_engine.py` | Main test execution logic |
| `batch_scorer.py` | Batch scoring for large test suites |
| `llm_judge_evaluator.py` | LLM-as-judge evaluation |

### Harnesses

| Harness | Purpose |
|---------|---------|
| `harness_test_generation.py` | Generate new test cases |
| `harness_boundary.py` | Boundary testing for edge cases |
| `harness_analysis.py` | Analyze test results |
| `harness_visualization.py` | Generate visualizations |

### Monitoring

| Component | Function |
|-----------|----------|
| `monitoring_dashboard.py` | Real-time metrics dashboard |
| `unified_web_dashboard.py` | Comprehensive web interface |
| `continuous_testing_monitor.py` | Long-running test monitoring |

## Related Projects

This framework is part of a larger ecosystem:

- **[trafficking-llm-benchmark](../trafficking-llm-benchmark-gitlab/)**: 21,000 pre-generated tests for human trafficking detection
- **[trafficking_llm_benchmark](../trafficking_llm_benchmark/)**: Development version with advanced features

## Documentation

- [Architecture Guide](docs/ARCHITECTURE.md)
- [API Reference](docs/API_REFERENCE.md)
- [Contributing Guide](docs/CONTRIBUTING.md)
- [Test Generation Guide](docs/TEST_GENERATION.md)

## Ethical Considerations

This framework is designed for **defensive security research**:

- Test LLM safety systems to identify weaknesses
- Generate training data to improve model safety
- Document exploitation patterns for prevention

**NOT intended for**:
- Circumventing safety systems maliciously
- Providing actual exploitation guidance
- Any form of real-world harm

## License

MIT License - See [LICENSE](LICENSE) for details.

## Citation

```bibtex
@misc{amarel2026llmsafety,
  title={LLM Safety Testing Framework},
  author={Amarel, Taylor},
  year={2026},
  publisher={GitHub},
  url={https://github.com/yourusername/llm-safety-framework}
}
```

## Contact

**Author**: Taylor Amarel

For issues and contributions, please use the GitHub issue tracker.
