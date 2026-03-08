# CLAUDE.md - LLM Safety Framework Intelligence

> Comprehensive guidance for AI assistants working on this codebase.

## Quick Reference

```bash
# Run tests
py -3.13 -m pytest tests/ -v

# Start web dashboard
python -m uvicorn src.web.app:app --host 127.0.0.1 --port 8080

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
- Detect activity chains where individually legal steps combine into trafficking patterns
- Execute tests against multiple LLM providers
- Evaluate responses using rubrics, keyword scoring, and LLM-as-judge
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
│   ├── core/
│   │   ├── __init__.py               # Module exports
│   │   ├── api_specification.py       # Pydantic models (26+ models)
│   │   └── base_agent.py             # Agent base classes
│   ├── web/
│   │   ├── app.py                    # FastAPI application factory
│   │   ├── config.py                 # Endpoint-centric v2 config
│   │   ├── app_context.py            # DI context (AppContext, get_ctx)
│   │   ├── plugin_registry.py        # Plugin loader & registry
│   │   ├── plugin_base.py            # Plugin manifest base class
│   │   ├── static/
│   │   │   ├── shell.html            # Plugin-aware SPA shell
│   │   │   └── styles.css            # Dashboard styles
│   │   └── plugins/                  # 14 feature plugins
│   │       ├── analytics/
│   │       ├── chain_detection/
│   │       ├── data_management/
│   │       ├── endpoints/
│   │       ├── integrations/
│   │       ├── intelligent_attack/
│   │       ├── multi_turn/
│   │       ├── prompts/
│   │       ├── scraper/
│   │       ├── prompt_injection/
│   │       ├── research/
│   │       ├── spinning/
│   │       ├── training/
│   │       └── wizard/
│   ├── chain_detection/
│   │   ├── models.py                 # ActivityChain, ChainScore, Grade
│   │   ├── chain_registry.py         # ChainRegistry (load, filter, CRUD)
│   │   ├── engine.py                 # ChainTestEngine
│   │   ├── scorer.py                 # score_keyword, score_hybrid, LLM judge
│   │   ├── prompt_builder.py         # 5 test modes
│   │   └── seeds/                    # 16 seed modules (126 chains)
│   │       ├── recruitment_debt.py
│   │       ├── document_control.py
│   │       ├── isolation_funnels.py
│   │       ├── financial_control.py
│   │       ├── supply_chain.py
│   │       ├── sector_specific.py
│   │       ├── digital_exploitation.py
│   │       ├── healthcare_migration.py
│   │       ├── gray_area_boundaries.py
│   │       ├── government_complicity.py
│   │       ├── gender_specific.py
│   │       ├── multi_country_transit.py
│   │       └── temporal_escalation.py
│   ├── scraper/
│   │   ├── sources.py                # SourceRegistry (54+ sources)
│   │   ├── fetcher.py                # DocumentFetcher with auto-escalation
│   │   ├── extractor.py              # FactExtractor (4 strategies)
│   │   ├── knowledge_base.py         # KnowledgeBase with cross-refs
│   │   ├── orchestrator.py           # ScrapeOrchestrator
│   │   ├── indicator_matrix.py       # Indicator stacking matrices
│   │   ├── stealth.py                # StealthProfile (5 levels)
│   │   ├── proxy.py                  # ProxyRotator
│   │   ├── browser.py                # Playwright headless browser
│   │   ├── document_identity.py      # SimHash dedup, version tracking
│   │   ├── seed_loader.py            # Seed fact loading
│   │   ├── seed_pruner.py            # Dedup & quality filter
│   │   └── seeds/                    # 174 seed modules (20,460 facts)
│   ├── spinning/
│   │   ├── local_spinner.py          # Spintax, regex, charpad
│   │   ├── llm_rephraser.py          # LLM-powered paraphrasing
│   │   ├── attack_augmenter.py       # Attack strategy overlays
│   │   ├── prompt_encoder.py         # Base64, ROT13, hex, Caesar
│   │   ├── text_obfuscator.py        # Homoglyph, leetspeak, zalgo
│   │   ├── jailbreak_templater.py    # 20 templates, 6 categories
│   │   ├── multilingual_attacker.py  # 21 languages
│   │   ├── multi_turn_orchestrator.py # 6 strategies
│   │   └── pipeline_manager.py       # Build → spin → test pipeline
│   ├── intelligent_attack/
│   │   ├── embedder.py               # Text embedding
│   │   ├── feature_extractor.py      # Feature space extraction
│   │   ├── space_analyzer.py         # Coverage analysis
│   │   ├── gap_finder.py             # Under-tested region detection
│   │   └── prompt_suggester.py       # Novel prompt generation
│   ├── prompt_injection/              # 488 mutators across 41 categories
│   │   ├── __init__.py               # Registry, list_mutators, MutationPipeline
│   │   ├── instruction_override.py   # 5 mutators
│   │   ├── encoding_format.py        # 10 mutators
│   │   ├── obfuscation.py            # 8 mutators
│   │   ├── social_engineering.py     # 6 mutators
│   │   ├── context_manipulation.py   # 5 mutators
│   │   ├── hybrid.py                 # 6 mutators
│   │   ├── output_evasion.py         # 109 mutators
│   │   ├── named_jailbreaks.py       # 15 mutators
│   │   ├── structural_injection.py   # 10 mutators
│   │   ├── advanced_obfuscation.py   # 10 mutators
│   │   ├── application_injection.py  # 8 mutators
│   │   ├── step_decomposition.py     # 20 mutators
│   │   ├── puzzle_game.py            # 6 mutators
│   │   ├── cognitive_exploit.py      # 5 mutators
│   │   ├── multilingual_attack.py    # 5 mutators
│   │   ├── steganographic_encode.py  # 5 mutators
│   │   ├── named_jailbreaks_v2.py    # 7 mutators
│   │   ├── logical_fallacy.py        # 10 mutators
│   │   ├── distraction_attack.py     # 10 mutators
│   │   ├── rhetorical_manipulation.py # 10 mutators
│   │   ├── legal_persona.py          # 10 mutators
│   │   ├── professional_persona.py   # 10 mutators
│   │   ├── analytical_framing.py     # 10 mutators
│   │   ├── special_token_injection.py # 10 mutators
│   │   ├── emoji_smuggling.py        # 10 mutators
│   │   ├── entropy_noise.py          # 10 mutators
│   │   ├── control_char_exploit.py   # 10 mutators
│   │   ├── encoding_exploitation.py  # 10 mutators
│   │   ├── adversarial_tokenization.py # 10 mutators
│   │   ├── bijection_cipher.py       # 10 mutators
│   │   ├── context_position_exploit.py # 10 mutators
│   │   ├── mathematical_encoding.py  # 10 mutators
│   │   ├── evaluation_manipulation.py # 10 mutators
│   │   ├── payload_splitting.py      # 10 mutators
│   │   ├── code_format_steganography.py # 10 mutators
│   │   ├── combination_engine.py     # 21 multi-technique compositions
│   │   ├── prefill_forced_completion.py # 10 mutators
│   │   ├── few_shot_attack.py        # 10 mutators
│   │   ├── template_fuzzing.py       # 10 mutators
│   │   ├── reasoning_hijack.py       # 10 mutators
│   │   ├── authority_exploit.py      # 10 mutators
│   │   ├── fitness.py                # FitnessTracker (adaptive selection)
│   │   ├── coverage.py               # CoverageAnalyzer (defense matrix)
│   │   └── output_decoders.py        # OutputDecoder for encoded results
│   ├── training/                      # 23 modules, 81 exports
│   │   ├── __init__.py               # Central exports (81 symbols)
│   │   ├── exporter.py               # TrainingDataExporter (9 formats)
│   │   ├── finetune_config.py        # FinetuneConfigGenerator (4 frameworks)
│   │   ├── red_team_generator.py     # RedTeamGenerator (4 backends)
│   │   ├── feedback_loop.py          # FeedbackLoop
│   │   ├── attack_quality.py         # AttackQualityScorer
│   │   ├── mutation_augmenter.py     # MutationAugmenter
│   │   ├── progress_tracker.py       # ProgressTracker
│   │   ├── reward_modeling.py        # 4 reward model trainers
│   │   ├── safety_evaluator.py       # SafetyEvaluator, BenchmarkRunner
│   │   └── dataset_generator.py      # SyntheticDatasetGenerator
│   ├── dimensional_matrix/            # 35-dimension scoring, debate judge
│   ├── research/                      # 7 autonomous research agents
│   │   └── agents/                   # Agent coordinator + 7 agents
│   ├── integrations/
│   │   ├── garak_adapter.py          # garak integration
│   │   ├── pyrit_adapter.py          # PyRIT integration
│   │   ├── deepteam_adapter.py       # DeepTeam integration
│   │   └── research_apis.py          # 5 API adapters (Semantic Scholar, arXiv, etc.)
│   ├── py.typed                      # PEP 561 type marker
│   └── api_client.py                 # UnifiedAPIClient (OpenAI + Anthropic)
├── tests/                            # 4,031 unit tests
├── .github/workflows/ci.yml          # GitHub Actions CI (test, lint, typecheck, coverage)
├── .pre-commit-config.yaml           # Pre-commit hooks (black, ruff, mypy)
├── Makefile                          # 13 build targets
├── SECURITY.md                       # Responsible disclosure policy
├── data/
│   ├── sample_test_prompts.json      # 145 prompts across 14 suites
│   └── chain_detection/              # Chain test results
├── templates/                        # Template data
├── examples/                         # Sample attack modules
├── scripts/                          # Utility scripts
├── docs/                             # Documentation
└── pyproject.toml                    # Package config
```

## Core Components

### 1. API Specification (`src/core/api_specification.py`)

Pydantic v2 models for the REST API:

```python
# Key models
TestSummary, TestDetail, TestListResponse
TestRunSummary, TestRunDetail
StatisticsResponse, SuiteStatistics
ModelPerformance, CorridorStatistics
ILOIndicatorCoverage
```

### 2. Base Agent (`src/core/base_agent.py`)

Agent system for autonomous testing:

```python
class AgentRole(Enum):
    PLANNER, EXECUTOR, ANALYZER,
    ATTACK_GENERATOR, CORRIDOR_EXPERT,
    CODE_EVOLVER, QUALITY_AUDITOR, META_LEARNER

class HarnessAgent(Generic[T]):
    async def call(prompt: str, context: dict = None) -> AgentResponse
```

### 3. Web Dashboard (`src/web/`)

Plugin-based SPA dashboard with 14 plugins and 267 API routes.

**Key patterns:**
- `AppContext` + `get_ctx` for dependency injection
- Plugin imports: `from ...app_context import AppContext, get_ctx`
- Config: endpoint-centric v2 design (v1 auto-migrates)
- Shell: `static/shell.html` lazy-loads plugin fragments

### 4. Chain Detection (`src/chain_detection/`)

126 chains across 16 categories testing whether LLMs detect exploitation patterns.

**5 test modes**: direct, incremental, contrastive, business, advisory
**5-grade rubric**: BLIND(0) → PARTIAL(1) → AWARE(2) → COMPETENT(3) → EXPERT(4)
**Hybrid scoring**: keyword matching + LLM-as-judge

```python
from src.chain_detection.seeds import load_all_seeds, seed_stats
from src.chain_detection.chain_registry import ChainRegistry
from src.chain_detection.scorer import score_keyword, score_hybrid
from src.chain_detection.prompt_builder import build_prompt
```

### 5. Document Intelligence (`src/scraper/`)

20,460 seed facts across 174 modules. 54+ sources across 7 tiers.

**Indicator matrix**: 7 migration phases x 11 ILO indicators grid
**Stealth**: 5-level anti-detection (NONE→BASIC→MODERATE→FULL→MAXIMUM)
**Extraction**: 4 strategies (default, legal_case, legislation, report)

### 6. Transform Workbench (`src/spinning/`)

12 transformation techniques for prompt variation generation.

**Transforms**: spintax, regex, charpad, LLM rephrase, attack augment, custom, encode, obfuscate, jailbreak, multilingual, chains, pipeline

### 7. Intelligent Attack (`src/intelligent_attack/`)

Embedding-based feature space analysis for finding coverage gaps and generating novel probes.

### 8. Prompt Injection Mutations (`src/prompt_injection/`)

488 deterministic mutators across 41 categories. Pure string transforms, no LLM calls.

**Categories:** instruction_override, encoding_format, obfuscation, social_engineering, context_manipulation, hybrid, output_evasion, named_jailbreak, structural_injection, advanced_obfuscation, application_injection, step_decomposition, puzzle_game, cognitive_exploit, multilingual_attack, steganographic_encode, named_jailbreak_v2, logical_fallacy, distraction, rhetorical, legal_persona, professional_persona, analytical_framing, special_token, emoji_smuggling, entropy_noise, control_char, encoding_exploit, adversarial_tokenization, bijection_cipher, context_position, mathematical_encoding, evaluation_manipulation, payload_splitting, code_steganography, combination_engine, prefill_completion, few_shot_attack, template_fuzzing, reasoning_hijack, authority_exploit

```python
from src.prompt_injection import list_mutators, get_mutators_by_category, MutationPipeline
```

### 9. Dimensional Response Matrix (`src/dimensional_matrix/`)

35-dimension severity scoring with 6 operations (Rate, Calibrate, Probe Boundary, Map Embeddings, Debate). Multi-LLM adversarial debate judge.

### 10. Research Agents (`src/research/`)

7 autonomous agents + coordinator for literature review, gap analysis, and trend monitoring.

### 11. Training Pipeline (`src/training/`)

23 modules exporting 81 symbols. Full training data generation and evaluation.

**Export formats (9):** SFT, DPO, RLHF, ChatML, Alpaca, ShareGPT, ORPO, KTO, Llama3
**Finetune frameworks (4):** Unsloth, Axolotl, TRL, LLaMA-Factory
**Reward modeling (4):** Bradley-Terry, SteerLM, RLOO, RAFT
**Safety evaluation:** SafetyMetrics, BenchmarkRunner, HTML reports
**Synthetic data:** ContrastivePair generator, EdgeCaseGenerator, 60 templates

```python
from src.training import (
    TrainingDataExporter, FinetuneConfigGenerator,
    RewardModelTrainer, SteerLMTrainer, RLOOTrainer, RAFTTrainer,
    SafetyEvaluator, BenchmarkRunner, SafetyMetrics,
    SyntheticDatasetGenerator, EdgeCaseGenerator,
)
```

### 12. Library Integrations (`src/integrations/`)

Optional adapters for garak, PyRIT, and DeepTeam. 5 research API adapters (Semantic Scholar, arXiv, GitHub, HuggingFace, OpenAlex). Detected at runtime.

### 13. CI/CD & Quality

- **GitHub Actions** (`.github/workflows/ci.yml`): test matrix (ubuntu/windows x 3.11/3.12/3.13), lint, typecheck, coverage
- **Pre-commit** (`.pre-commit-config.yaml`): black, ruff, mypy hooks
- **Makefile**: 13 targets (test, lint, format, typecheck, coverage, serve, docker, etc.)
- **SECURITY.md**: Responsible disclosure policy

## Test Suites

| Suite | Tests | Focus |
|-------|-------|-------|
| regulatory_evasion | ~3,000 | License fraud, fee manipulation |
| debt_bondage | ~4,000 | Debt traps, salary deductions |
| coercion_manipulation | ~5,000 | Psychological tactics |
| moral_religious_framing | ~3,000 | Cultural/religious exploitation |
| financial_obfuscation | ~3,000 | Hidden fees, currency tricks |

### Chain Detection Categories (16)

recruitment_debt, document_control, isolation_funnels, financial_control, supply_chain, sector_specific, digital_exploitation, healthcare_migration, gray_area_boundaries, government_complicity, gender_specific, multi_country_transit, temporal_escalation, education_sector, fishing_maritime, whistleblower_retaliation

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

Tests cover 126 corridors. Major labor migration routes:

- **PH-SA**: Philippines to Saudi Arabia (domestic workers)
- **NP-QA**: Nepal to Qatar (construction)
- **BD-MY**: Bangladesh to Malaysia (manufacturing)
- **ID-SG**: Indonesia to Singapore (domestic workers)
- **ET-LB**: Ethiopia to Lebanon (domestic workers)
- **MM-TH**: Myanmar to Thailand (fishing, agriculture)

Multi-country transit routes: MM-TH-MY-SG, NG-LY-IT, PH-QA-SA, NP-IN-QA, GT-MX-US, VN-KH-TH, BD-MY-AU, ET-YE-SA

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
- Plugin pattern: `__init__.py` (manifest), `routes.py` (DI), `static/fragment.html`, `static/fragment.js`

## Testing

```bash
# Run all tests (4,031 total)
py -3.13 -m pytest tests/ -v -W ignore::SyntaxWarning --ignore=tests/e2e

# Run specific test file
py -3.13 -m pytest tests/test_chain_detection.py -v

# Run with coverage
py -3.13 -m pytest tests/ --cov=src --cov-report=html
```

### Key Test Files

| File | Tests | Focus |
|------|-------|-------|
| test_step_and_new_mutators.py | 725 | Step decomposition + all new mutator categories |
| test_new_mutators.py | 284 | Batch 1-3 mutator categories |
| test_output_evasion.py | 277 | Output evasion mutators |
| test_training_v6.py | 192 | Reward modeling, safety evaluator, dataset generator |
| test_plugin_routes.py | 80+ | Plugin route integration |
| test_scraper.py | 75 | Document intelligence |
| test_prompt_injection.py | 66 | Core prompt injection |
| test_training.py | 42 | Training export formats |
| test_training_v2.py | 52 | Training v2 (scoring, augmentation) |
| test_chain_detection.py | 45 | Chain detection |
| test_routes.py | 49 | Core route tests |
| test_stealth.py | 48 | Stealth scraping |
| test_dimensional_matrix.py | 80 | Dimensional matrix |
| test_research_apis.py | 33 | Research API adapters |

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

## Key Files Reference

| File | Purpose |
|------|---------|
| `src/web/app.py` | FastAPI application factory |
| `src/web/config.py` | Endpoint-centric configuration |
| `src/web/app_context.py` | DI context for plugins |
| `src/web/plugin_registry.py` | Plugin loader & registry |
| `src/chain_detection/models.py` | ActivityChain, ChainScore, Grade |
| `src/chain_detection/seeds/__init__.py` | All 13 seed module imports |
| `src/scraper/seeds/__init__.py` | All 174 seed fact imports |
| `src/training/__init__.py` | Training pipeline (81 exports, 23 modules) |
| `src/api_client.py` | UnifiedAPIClient |
| `data/sample_test_prompts.json` | 145 test prompts (14 suites) |
| `.github/workflows/ci.yml` | GitHub Actions CI pipeline |
| `Makefile` | 13 build/test targets |
| `SECURITY.md` | Responsible disclosure policy |
| `docs/examples/` | Sample HTML reports |

## Troubleshooting

### Import Errors

Ensure you're in the project root:
```python
import sys
sys.path.insert(0, "/path/to/llm-safety-framework-public")
```

Or set PYTHONPATH:
```bash
PYTHONPATH=. py -3.13 your_script.py
```

### Pydantic Validation Errors

Provide all required fields. Use Pydantic v2 syntax (model_validate, not parse_obj).

---

*Version: 4.0.0*
*Author: Taylor Amarel*
*Framework: LLM Safety Testing for Migrant Worker Protection*
