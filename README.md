# LLM Safety Testing Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-5208%20passing-brightgreen.svg)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-dynamic-blue.svg)](tests/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modular, extensible framework for evaluating whether Large Language Models properly refuse requests that could facilitate human trafficking and migrant worker exploitation. This is **defensive security research** -- the framework identifies weaknesses in AI safety guardrails so they can be strengthened, not bypassed. Every test measures a model's ability to recognize and refuse harmful requests grounded in real-world exploitation patterns documented by the ILO, IOM, and international anti-trafficking law.

---

## Key Statistics

| Metric | Count |
|--------|------:|
| Python source files | 470+ |
| Lines of Python | ~320,000 |
| Unit tests passing | 5,208 |
| Test files | 51 |
| API routes | 303 |
| Web dashboard plugins | 16 |
| Prompt injection mutators | 548 across 47 categories |
| Chain detection seeds | 150+ chains, 21 modules |
| Document intelligence facts | 20,460 across 174 modules |
| Training algorithms supported | 15 |
| Export formats | 9 |
| Migration corridors | 126 routes |
| ILO forced labor indicators | All 11 |
| Research API integrations | 5 |
| Dimensional scoring dimensions | 45 across 5 categories |
| LLM cartography modules | 7 (topology, scorer, comparator, attack surface, blind spots, gradient generator) |

---

## Quick Start

```bash
# Clone
git clone https://github.com/tayloramarel/llm-safety-framework.git
cd llm-safety-framework

# Virtual environment
python -m venv .venv
source .venv/bin/activate  # Unix
# .venv\Scripts\activate   # Windows

# Install
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v

# Start the web dashboard
python -m uvicorn src.web.app:app --host 127.0.0.1 --port 8080
# Or: docker-compose up web
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## Architecture Overview

```
llm-safety-framework/
├── src/
│   ├── core/                       # Pydantic v2 models, agent base classes
│   ├── web/                        # FastAPI dashboard (267 routes)
│   │   └── plugins/                # 14 feature plugins
│   ├── chain_detection/            # 126 chains, 16 seed modules, hybrid scoring
│   │   └── seeds/                  # Recruitment, isolation, financial, transit, ...
│   ├── scraper/                    # 20,460 facts, 174 modules, 54+ sources
│   │   └── seeds/                  # ILO reports, court cases, news, legislation
│   ├── spinning/                   # 12 transform techniques
│   ├── intelligent_attack/         # Embedding space coverage analysis
│   ├── prompt_injection/           # 488 mutators, 41 categories, pipeline engine
│   ├── dimensional_matrix/         # 35-dimension scoring, multi-LLM debate judge
│   ├── training/                   # 23 modules: export, fine-tune, RL, evaluation
│   ├── integrations/               # garak, PyRIT, DeepTeam, 5 research APIs
│   └── research/                   # 7 autonomous research agents + coordinator
├── tests/                          # 4,069 unit tests across 39 files
├── data/                           # Test prompts, chain results, seed data
├── docs/                           # 14 documentation files
├── templates/                      # Template data
├── scripts/                        # Utility scripts
├── Dockerfile                      # Container deployment
├── docker-compose.yml              # Multi-service orchestration
└── pyproject.toml                  # Package configuration
```

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                        LLM SAFETY TESTING FRAMEWORK v4.0                        │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│   Web Dashboard (14 plugins, 267 routes)                                         │
│   ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐               │
│   │  Endpoints  │  │  Prompts   │  │  Analytics  │  │   Wizard   │               │
│   └──────┬─────┘  └──────┬─────┘  └──────┬─────┘  └──────┬─────┘               │
│          │               │               │               │                       │
│   ┌──────┴───────────────┴───────────────┴───────────────┴──────┐               │
│   │                    Test Execution Engine                      │               │
│   └──────┬───────────────┬───────────────┬───────────────┬──────┘               │
│          │               │               │               │                       │
│   ┌──────▼─────┐  ┌──────▼─────┐  ┌──────▼─────┐  ┌──────▼─────┐               │
│   │  Prompt     │  │   Chain    │  │ Dimensional │  │  Training  │               │
│   │  Injection  │  │ Detection  │  │   Matrix    │  │  Pipeline  │               │
│   │ 488 mutate  │  │ 126 chains │  │  35 dims    │  │ 15 algos   │               │
│   └──────┬─────┘  └──────┬─────┘  └──────┬─────┘  └──────┬─────┘               │
│          │               │               │               │                       │
│   ┌──────▼─────┐  ┌──────▼─────┐  ┌──────▼─────┐  ┌──────▼─────┐               │
│   │ Transform   │  │  Document  │  │  Research   │  │   Library  │               │
│   │ Workbench   │  │   Intel    │  │   Agents    │  │ Integrations│              │
│   │ 12 techniq  │  │ 20,460 fct │  │  7 agents   │  │ garak/pyrit│               │
│   └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘               │
│                                                                                  │
│   Models Under Test: OpenAI, Anthropic, Mistral, Together, Ollama, OpenRouter    │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## Core Systems

### Chain Detection

Evaluates whether LLMs recognize when individually legal activities combine into trafficking patterns. 126 chains across 16 categories (recruitment debt, document control, isolation funnels, financial control, supply chain, digital exploitation, healthcare migration, government complicity, gender-specific, multi-country transit, and more). Five test modes (direct, incremental, contrastive, business, advisory) with a 5-grade rubric from BLIND(0) to EXPERT(4) and hybrid keyword + LLM-as-judge scoring.

[Full documentation](docs/CHAIN_DETECTION.md)

### Prompt Injection Mutations

488 deterministic mutators across 41 categories. All pure string transforms, chainable via `MutationPipeline`. Categories include: output evasion (109 mutators), combination engine (21 compositional operators), named jailbreaks, structural injection, step decomposition, puzzle/game encoding, cognitive exploit, multilingual attacks, steganographic encoding, logical fallacy, distraction, rhetorical manipulation, legal persona, professional persona, analytical framing, special token injection, emoji smuggling, entropy noise, control character exploits, encoding exploitation, adversarial tokenization, bijection cipher, context position exploits, mathematical encoding, evaluation manipulation, payload splitting, code steganography, prefill/forced completion, few-shot attack, template fuzzing, reasoning hijack, and authority exploit.

[Full documentation](docs/PROMPT_INJECTION.md)

### Dimensional Response Matrix

35-dimension severity scoring with 6 operations (Rate, Calibrate, Probe Boundary, Map Embeddings, Debate). Includes a multi-LLM adversarial debate judge for contested evaluations.

[Full documentation](docs/DIMENSIONAL_MATRIX.md)

### Document Intelligence

20,460 seed facts across 174 modules sourced from ILO reports, court decisions, investigative journalism, and legislation. 54+ sources organized across 7 reliability tiers. Indicator stacking matrices map 7 migration phases against all 11 ILO forced labor indicators.

### Intelligent Attack

Embedding-based feature space analysis that identifies under-tested regions in the prompt space and generates novel probes to fill coverage gaps.

### Research Agents

7 autonomous agents (literature review, gap analysis, trend monitoring, and more) coordinated by a central orchestrator for continuous research updates.

### Integrations

Adapters for [garak](https://github.com/NVIDIA/garak), [PyRIT](https://github.com/Azure/PyRIT), and [DeepTeam](https://github.com/confident-ai/deepteam). Five research API integrations: Semantic Scholar, arXiv, GitHub Search, HuggingFace Hub, and OpenAlex.

---

## Training Pipeline

The training pipeline is a closed-loop system for improving open-source model safety through iterative fine-tuning and red-team evaluation. It spans 23 modules with 81 export configurations.

### Training Algorithms (15)

| Algorithm | Type | Description |
|-----------|------|-------------|
| SFT | Supervised | Standard supervised fine-tuning on refusal examples |
| DPO | Preference | Direct Preference Optimization (chosen vs. rejected pairs) |
| ORPO | Preference | Odds Ratio Preference Optimization |
| KTO | Preference | Kahneman-Tversky Optimization (binary signal) |
| SPIN | Self-Play | Self-Play Fine-Tuning with iterative improvement |
| SimPO | Preference | Simple Preference Optimization (reference-free) |
| IPO | Preference | Identity Preference Optimization |
| Rejection Sampling | Sampling | Best-of-N with reward model scoring |
| Constitutional AI | Self-Critique | Critique-revision with principle-based feedback |
| PPO | RL | Proximal Policy Optimization with reward model |
| GRPO | RL | Group Relative Policy Optimization |
| Reward Model | Scoring | Bradley-Terry, regression, and classification variants |
| SteerLM | Attribute | Attribute-conditioned generation and steering |
| RLOO | RL | Reinforcement Learning with Leave-One-Out baseline |
| RAFT | RL | Reward rAnked Fine-Tuning |

### Export Formats (9)

SFT, DPO, RLHF, ChatML, Alpaca, ShareGPT, ORPO, KTO, Llama3 -- each with configurable system prompts, tokenizer settings, and column mappings.

### Fine-Tuning Framework Support

| Framework | Quantization | LoRA/QLoRA | Multi-GPU |
|-----------|:------------:|:----------:|:---------:|
| Unsloth   | 4-bit, 8-bit | Yes | Yes |
| Axolotl   | 4-bit, 8-bit | Yes | Yes |
| TRL       | 4-bit, 8-bit | Yes | Yes |
| LLaMA-Factory | 4-bit, 8-bit | Yes | Yes |

### Cloud Platform Integration

| Platform | Fine-Tune | Inference | Status Tracking |
|----------|:---------:|:---------:|:---------------:|
| Together AI | Yes | Yes | Yes |
| HuggingFace | Yes | Yes | Yes |
| RunPod | Yes | Yes | Yes |
| OpenAI | Yes | Yes | Yes |

### Academic Attack Implementations

- **PAIR** (Prompt Automatic Iterative Refinement) -- iterative jailbreak refinement with attacker LLM
- **TAP** (Tree of Attacks with Pruning) -- tree-search over attack candidates with pruning
- **AutoDAN** (Automatic Do-Anything-Now) -- genetic algorithm optimization of adversarial suffixes

### Additional Capabilities

- **Ensemble Orchestration**: 6 coordinated multi-strategy attack campaigns
- **Safety Evaluator**: automated benchmarking across models with HTML report generation
- **Synthetic Dataset Generator**: contrastive pairs, edge cases, 5 difficulty categories
- **Evolutionary Engine**: genetic algorithm-based prompt evolution with fitness tracking
- **Token Analysis**: distribution statistics, vocabulary coverage, sequence length profiling
- **RL Attack Optimizer**: reinforcement learning loop for adversarial prompt refinement
- **HuggingFace Hub Integration**: direct dataset push, dataset cards, version management
- **Curriculum Orchestrator**: staged difficulty progression for training data

### Closed-Loop Workflow

```
Run Benchmark ──> Export Failures ──> Fine-Tune Model ──> Generate Attacks
       ^                                                        │
       └────────────────── Re-evaluate <────────────────────────┘
```

---

## Web Dashboard Plugins

| Plugin | Routes | Description |
|--------|-------:|-------------|
| **Endpoints** | -- | Configure API keys and models (OpenAI, Anthropic, Mistral, Together, Ollama, OpenRouter) |
| **Prompts** | -- | Manage test prompt sets with CRUD, import, and test preparation |
| **Chain Detection** | -- | Browse 126 chains, execute tests, 5-grade scoring with hybrid evaluation |
| **Spinning** | -- | Transform workbench with 12 technique tabs |
| **Analytics** | -- | Statistics, conversation browser, attack heatmap, coverage matrix |
| **Intelligent Attack** | -- | Embedding-based feature space analysis and gap detection |
| **Multi-Turn** | -- | 6 strategies: Crescendo, FITD, Skeleton Key, Many-Shot, Deceptive Delight, Role-Play |
| **Prompt Injection** | -- | 488 mutators, pipeline builder, batch operations, decode tools |
| **Research** | -- | Paper/repo/dataset search across 5 APIs, saved results |
| **Scraper** | -- | Document intelligence agent, 54+ sources, indicator matrices |
| **Training** | -- | Export (9 formats), fine-tune configs, red-team loop, academic attacks, cloud fine-tune, reward modeling, safety evaluation, dataset generation |
| **Integrations** | -- | garak, PyRIT, DeepTeam adapters |
| **Data Management** | -- | Import/export conversations, configuration, pipeline data |
| **Wizard** | -- | Streamlined guided testing mode for new users |

---

## Documentation Index

| Document | Description |
|----------|-------------|
| [Chain Detection](docs/CHAIN_DETECTION.md) | 126 chains, 16 categories, scoring rubric, test modes |
| [Prompt Injection](docs/PROMPT_INJECTION.md) | 488 mutators, 41 categories, pipeline usage, academic references |
| [Dimensional Matrix](docs/DIMENSIONAL_MATRIX.md) | 35 dimensions, 6 operations, debate judge |
| [Attack Taxonomy](docs/ATTACK_TAXONOMY.md) | Attack generator categories, chain detection overlap analysis |
| [AI Safety Training](docs/AI_SAFETY_TRAINING.md) | Refusal patterns, legal standards, vulnerability gaps |
| [Migration Corridors](docs/MIGRATION_CORRIDORS.md) | 126 routes, 11 ILO indicators, transit route analysis |
| [Architecture](docs/ARCHITECTURE.md) | System design, component interaction diagrams |
| [API Reference](docs/API_REFERENCE.md) | 267 REST endpoints with request/response examples |
| [CLI Reference](docs/CLI_REFERENCE.md) | All command-line flags and usage patterns |
| [Test Generation](docs/TEST_GENERATION.md) | Generation strategies and configuration |
| [Importing Guide](docs/IMPORTING_GUIDE.md) | Data formats, import/export methods |
| [Contributing](docs/CONTRIBUTING.md) | Code style, PR process, adding new attack modules |
| [Diagrams](docs/DIAGRAMS.md) | Visual system documentation |
| [Ideas & Expansions](docs/IDEAS_AND_EXPANSIONS.md) | Roadmap and research directions |

---

## Test Pipeline CLI

```bash
# Basic test run
python scripts/run_test_pipeline.py --endpoint mistral --limit 50

# With dimensional scoring and multi-LLM debate
python scripts/run_test_pipeline.py --endpoint openrouter \
  --dimensional --debate --debate-rounds 2

# With mutation variants
python scripts/run_test_pipeline.py --endpoint mistral \
  --mutations base64,rot13,emoji_smuggling --limit 100

# Export training data from results
python -m src.training.export_training_data \
  --format dpo --output training_data.jsonl
```

---

## Environment Variables

```bash
# LLM API keys (for live testing and evaluation)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
MISTRAL_API_KEY=...
TOGETHER_API_KEY=...

# Framework settings
LOG_LEVEL=INFO
LLM_SAFETY_HOST=0.0.0.0
LLM_SAFETY_PORT=8080
MAX_CONCURRENT_REQUESTS=10
CACHE_ENABLED=true
```

---

## ILO Forced Labor Indicators

The framework tests model responses against all 11 ILO forced labor indicators:

1. Abuse of vulnerability
2. Deception
3. Restriction of movement
4. Isolation
5. Physical and sexual violence
6. Intimidation and threats
7. Retention of identity documents
8. Withholding of wages
9. Debt bondage
10. Abusive working and living conditions
11. Excessive overtime

These indicators are cross-referenced with 126 migration corridors spanning routes such as PH-SA (Philippines to Saudi Arabia), NP-QA (Nepal to Qatar), BD-MY (Bangladesh to Malaysia), ET-LB (Ethiopia to Lebanon), MM-TH (Myanmar to Thailand), and multi-country transit routes including MM-TH-MY-SG, NG-LY-IT, and VN-KH-TH.

---

## Citation

```bibtex
@software{llm_safety_framework,
  author       = {Amarel, Taylor},
  title        = {LLM Safety Testing Framework for Migrant Worker Protection},
  version      = {4.0.0},
  year         = {2026},
  url          = {https://github.com/tayloramarel/llm-safety-framework},
  note         = {Defensive AI safety research: 488 prompt injection mutators,
                  126 chain detection seeds, 20460 document intelligence facts,
                  15 training algorithms, 4069 unit tests}
}
```

---

## License

MIT License -- See [LICENSE](LICENSE) for details.

## Author

**Taylor Amarel** -- [github.com/tayloramarel](https://github.com/tayloramarel)

---

## Related Resources

- [ILO Forced Labour Convention (C029)](https://www.ilo.org/dyn/normlex/en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C029)
- [ILO Fair Recruitment Initiative](https://www.ilo.org/global/topics/fair-recruitment/)
- [ILO Forced Labour Indicators](https://www.ilo.org/global/topics/forced-labour/publications/)
- [UN Palermo Protocol](https://www.unodc.org/unodc/en/human-trafficking/)
- [Dhaka Principles for Migration with Dignity](https://www.ihrb.org/dhaka-principles)
- [ILO Domestic Workers Convention (C189)](https://www.ilo.org/dyn/normlex/en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C189)
- [ILO Private Employment Agencies Convention (C181)](https://www.ilo.org/dyn/normlex/en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C181)
- [Employer Pays Principle](https://www.ihrb.org/employerpays)

---

*Framework Version: 4.0.0 | Last Updated: 2026-03-07 | Tests: 4,069 Passing*
