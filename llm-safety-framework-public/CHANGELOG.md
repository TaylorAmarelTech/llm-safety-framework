# Changelog

All notable changes to this project will be documented in this file.

## [2.1.0] - 2026-03-03

### Added
- **Dimensional Response Matrix** — 35-dimension severity scoring system (A1-A12, B1-B7, C1-C11, D1-D5)
  - `DimensionalRater`: LLM-as-judge scoring on all dimensions
  - `DimensionalCalibrator`: Generate shifted responses/prompts along dimensions
  - `BoundaryProber`: Binary-search guardrail boundary mapping
  - `EmbeddingMapper`: Unified vector space for boundary visualization
  - `MatrixBuilder`: Full calibration matrix orchestrator
- **Multi-LLM Debate Judge** — Adversarial debate evaluation system
  - Prosecutor/Defender/Analyst/Judge roles with configurable models
  - Same-model, three-model, and panel debate factory methods
  - Structured verdicts with confidence, vulnerabilities, dimensional flags
  - Pipeline integration: `--debate`, `--debate-rounds`, `--debate-defender`, `--debate-judge`, `--debate-max`
- **Prompt Injection Mutations** — 40 deterministic mutators across 6 categories
  - instruction_override (5), encoding_format (10), obfuscation (8)
  - social_engineering (6), context_manipulation (5), hybrid (6)
  - `MutationPipeline` for chaining multiple mutators
- **Research Agent System** — 7 autonomous research agents + coordinator
  - enforcement, cross_pollination, technique_evolution, coverage_gap
  - ethics_boundary, financial_crime, jurisdiction
- **Financial Crime Extension** — 3 new chain detection seed modules
  - tax_evasion (8 chains), money_laundering (6 chains), white_collar_crime (6 chains)
  - Total chains: 126 across 16 categories (was 106 across 13)
- **Multi-Endpoint Support** — 13 configured endpoints (7 new)
  - Added: groq, cerebras, deepseek, gemini, sambanova, fireworks, nvidia-nim
  - Key rotation with automatic cooldown on rate limits

### Fixed
- `DebateJudge.three_models()` parameter name mismatch in pipeline (would crash with TypeError)
- `src/api.py` broken import from deleted `routes.py` (standalone API server wouldn't start)
- Refusal classification false positives ("this is illegal activity" no longer classified as refusal)

### Improved
- Debate verdict parsing hardened: handles empty responses, non-numeric confidence, invalid assessments
- API client caching in DebateJudge (reuses connections across debate turns)
- Dimension ID validation in debate judge (warns on unknown IDs)
- Refusal classification upgraded to sentence-level matching with strong/weak indicator tiers
- `dimensional_matrix/__init__.py` now exports all operation classes
- `spinning/__init__.py` now exports `MultilingualAttacker` and `MultiTurnOrchestrator`

## [2.0.0] - 2026-02-23

### Added
- **Plugin-based Web Dashboard** — 11 modular plugins with lazy-loaded fragments
- **Chain Detection System** — 106 chains across 13 categories with 5-grade scoring
- **Document Intelligence Agent** — 174 seed modules, 20,460 facts, 54+ sources
- **Transform Workbench** — 12 transformation techniques (spintax, encode, obfuscate, jailbreak, etc.)
- **Indicator Stacking Matrices** — 7 migration phases x 11 ILO indicators grid
- **5-Level Stealth Scraping** — NONE to MAXIMUM anti-detection escalation
- **Intelligent Attack** — Embedding-based feature space analysis and gap finding
- **Multi-Turn Attacks** — 6 strategies (Crescendo, FITD, Skeleton Key, Many-Shot, Deceptive Delight, Role-Play)
- **Library Integrations** — Adapters for garak, PyRIT, and DeepTeam
- **Multilingual Attacks** — 21 languages with full and mixed translation modes
- Endpoint-centric v2 configuration (auto-migrates from v1)
- `UnifiedAPIClient` supporting OpenAI-compatible and Anthropic formats
- Document identity system (SimHash dedup, version tracking)
- SPA shell with plugin-aware navigation

### Changed
- Architecture migrated from monolithic routes.py to plugin system
- Configuration model changed from provider-grouped to endpoint-centric

## [1.0.0] - 2026-02-01

### Added
- Initial framework release
- Core API specification (Pydantic v2 models)
- Agent system with 8 roles (Planner, Executor, Analyzer, etc.)
- 9 test generators (historical_precedent, coercion_manipulation, financial_obfuscation, etc.)
- FastAPI web server with test execution
- Docker support (Dockerfile, docker-compose.yml)
- CLI interface with typer
- 145 test prompts across 14 suites
- 126 migration corridor definitions
- All 11 ILO forced labor indicators
