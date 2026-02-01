# LLM Safety Testing Ecosystem

A comprehensive ecosystem for testing Large Language Model safety systems, with a focus on preventing harmful outputs related to human trafficking and labor exploitation.

## Projects

This repository contains three interconnected projects:

### 1. LLM Safety Framework (`llm-safety-framework-public/`)

**Status:** Public Release

A modular, extensible framework for testing LLM safety systems:

- Multi-provider support (OpenAI, Anthropic, Mistral, Together, Ollama)
- Test generation (template, LLM-powered, evolutionary)
- Evaluation engines (rubric-based, LLM-as-judge)
- Monitoring dashboards and metrics
- REST API for programmatic access

[View Documentation](llm-safety-framework-public/README.md)

### 2. Trafficking LLM Benchmark (`trafficking-llm-benchmark-gitlab/`)

**Status:** Public Release (21,000 tests)

Pre-generated test suite for human trafficking detection:

| Suite | Tests | Description |
|-------|-------|-------------|
| Moral/Religious Framing | 3,000 | Biblical verses, cultural proverbs |
| Regulatory Evasion | 3,000 | POEA enforcement history (2006-2018) |
| Coercion & Manipulation | 3,000 | Psychological tactics, impossible debt math |
| Financial Obfuscation | 2,000 | Investment framing, fee transfers |
| Mega Variations | 10,000 | Systematic exploration across all types |

[View Documentation](trafficking-llm-benchmark-gitlab/README.md)

### 3. Development Benchmark (`trafficking_llm_benchmark/`)

**Status:** Active Development

Research and development version with advanced features:

- Autonomous self-improving harness
- Evolution engine for attack generation
- Document analysis pipeline
- Extended vulnerability categories

[View Documentation](trafficking_llm_benchmark/CLAUDE.md)

## Quick Start

### Using the Public Framework

```bash
cd llm-safety-framework-public
pip install -r requirements.txt
cp .env.template .env
# Edit .env with your API keys

python -m src.core.api_server
```

### Using Pre-Generated Tests

```bash
cd trafficking-llm-benchmark-gitlab
pip install -r requirements.txt

# Import tests to database
python import_tests_to_database.py

# Run tests against a model
python run_tests.py --suite moral_religious_framing --model gpt-4o-mini --count 10
```

## Ethical Framework

This ecosystem is designed for **defensive security research**:

**Intended Uses:**
- Test LLM safety systems to identify vulnerabilities
- Generate training data to improve model safety
- Document exploitation patterns for prevention
- Academic research on AI safety

**NOT Intended For:**
- Actual human trafficking or labor exploitation
- Circumventing safety systems maliciously
- Providing real guidance to bad actors

## Research Background

Based on Taylor Amarel's work from the OpenAI GPT-OSS Red-Teaming Challenge, incorporating:

- ILO Conventions (C181, C189)
- Palermo Protocol indicators
- 18 years of POEA enforcement data
- Real-world trafficking patterns and tactics

## License

MIT License - See individual project directories for details.

## Citation

```bibtex
@misc{amarel2026llmsafety,
  title={LLM Safety Testing Ecosystem},
  author={Amarel, Taylor},
  year={2026},
  publisher={GitHub},
  url={https://github.com/yourusername/llm-safety-testing}
}
```

## Contact

**Author:** Taylor Amarel

For issues and contributions, please use the GitHub issue tracker.
