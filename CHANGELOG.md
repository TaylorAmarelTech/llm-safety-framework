# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [4.0.0] - 2026-03-07

### Added
- **Training Pipeline v6 — Reward & Alignment Trainers**
  - `RewardModelTrainer` with Bradley-Terry, Regression, and Classification heads
  - `SteerLMTrainer` for multi-attribute conditioning (helpfulness, safety, coherence)
  - `RLOOTrainer` implementing REINFORCE Leave-One-Out variance reduction
  - `RAFTTrainer` for Reward rAnked FineTuning with filtered sampling
- **Safety Evaluator** for automated safety benchmarking
  - `SafetyMetrics` computation (refusal rate, false positive rate, attack success rate)
  - `ModelComparison` for side-by-side evaluation across providers
  - `BenchmarkRunner` with configurable test suites and parallel execution
  - Self-contained HTML vulnerability reports with inline SVG charts
- **Synthetic Dataset Generator**
  - `SyntheticDatasetGenerator` with 60 prompt templates across 5 exploitation categories
  - `EdgeCaseGenerator` for boundary conditions, multi-turn traps, and culture-specific scenarios
  - `ContrastivePair` format for training on near-miss harmful/benign pairs
- 9 new web API routes for reward modeling, safety evaluation, and dataset generation
- 192 new unit tests in `test_training_v6.py`
- Total: 267 API routes, 4,069 tests, 81 training module exports

## [3.6.0] - 2026-03-07

### Added
- **Training Pipeline v5 — Advanced Training Methods**
  - `SPINTrainer` (Self-Play Fine-Tuning)
  - `SimPOTrainer` (Simple Preference Optimization without reference model)
  - `IPOTrainer` (Identity Preference Optimization)
  - `RejectionSampler` for best-of-N sampling with reward filtering
  - `ConstitutionalTrainer` for Constitutional AI (critique-revision loops)
  - `DataMixer` for multi-source dataset blending with ratio control
- **Report Generator** — self-contained HTML reports with inline SVG charts (bar, line, heatmap) across 5 report types
- **Hub Integration**
  - HuggingFace Hub push/pull for datasets with auth token management
  - `LocalDatasetManager` with merge, split, filter, and sample operations
  - `DatasetCard` generation with YAML frontmatter metadata
- **Ensemble Attack Orchestrator** — 6 coordinated attack strategies
  - Mutation, Evolution, PAIR, TAP, AutoDAN, and Template-based campaigns
  - Campaign management with deduplication and result aggregation
- 23 new web routes for training plugin (total 43 training routes)
- 157 new unit tests in `test_training_v5.py`

## [3.5.0] - 2026-03-07

### Added
- **Training Pipeline v4 — Academic Attacks & Cloud Training**
  - `PAIR` (Prompt Automatic Iterative Refinement) attack implementation
  - `TAP` (Tree of Attacks with Pruning) attack implementation
  - `AutoDAN` (Automatic DAN generation via gradient-guided search) attack implementation
  - `CloudInferenceRouter` supporting Together, HuggingFace, RunPod, and OpenAI backends
  - `TokenAnalyzer` for token-level vulnerability analysis and BPE boundary detection
  - `RLAttackOptimizer` with PPO and GRPO policy gradient methods
- Web routes for academic attacks, cloud fine-tuning, token analysis, and RL optimizer
- 84 new unit tests in `test_training_v4.py`

## [3.4.0] - 2026-03-07

### Added
- **Training Pipeline v3 — Live Testing & Evolution**
  - `LiveTester` for real-time API testing against deployed models
  - `RefusalGenerator` with 48 refusal templates across 5 tones (firm, empathetic, educational, redirecting, minimal)
  - `EvolutionaryEngine` implementing genetic algorithm for prompt evolution (crossover, mutation, fitness selection)
  - `MultiTurnExporter` for serializing multi-turn attack conversations
  - `CurriculumOrchestrator` for staged difficulty progression in training
- `FeedbackLoop` wired to `LiveTester` for closed-loop real API testing
- 50 new unit tests in `test_training_v3.py`

## [3.3.0] - 2026-03-06

### Added
- **Training Pipeline v2 — Scoring, Augmentation & Adaptive Selection**
  - `AttackQualityScorer` for evaluating generated attack effectiveness
  - `MutationAugmenter` for automated prompt variation generation
  - `ProgressTracker` for monitoring training data generation campaigns
  - `FitnessTracker` with EMA-smoothed fitness scores and epsilon-greedy adaptive mutator selection
  - `CoverageAnalyzer` computing defense layer x technique class coverage matrix
- ORPO, KTO, and Llama3 export formats (total 9 training data formats)
- GitLab CI/CD stages for training, finetune, red-team, and hub-push pipelines
- 52 new unit tests in `test_training_v2.py`

## [3.2.0] - 2026-03-06

### Added
- **Training Pipeline v1 — Core Training Data Infrastructure**
  - `TrainingDataExporter` supporting 6 formats: SFT, DPO, RLHF, ChatML, Alpaca, ShareGPT
  - `FinetuneConfigGenerator` for 4 frameworks (Unsloth, Axolotl, TRL, LLaMA-Factory) with 8 model presets
  - `RedTeamGenerator` with 4 backends for adversarial prompt generation
  - `FeedbackLoop` for iterative prompt refinement based on model responses
- Training web plugin with 11 API routes
- 42 new unit tests in `test_training.py`

## [3.1.0] - 2026-03-06

### Added
- **Prefill/Forced Completion** mutators (10): assistant prefill, completion continuation, chain-of-thought hijack, function result injection, tool output prefill, multi-turn prefill, response template, output format forcing, partial response, streaming chunk
- **Few-Shot Attack** mutators (10): in-context learning exploit, demonstration poisoning, example gradient, labeled few-shot, chain-of-examples, persona extraction, style transfer, Q&A format, tutorial demonstration, calibration examples
- **Template Fuzzing** mutators (10): system prompt probe, delimiter exploration, role boundary test, format string injection, variable interpolation, template inheritance, block override, comment injection, conditional bypass, recursive template
- **Reasoning Hijack** mutators (10): chain-of-thought redirect, step-by-step corruption, logical chain insertion, reasoning anchoring, conclusion planting, metacognitive exploit, self-consistency attack, debate framing, thought experiment, analogy poisoning
- **Authority Exploit** mutators (10): developer override, OpenAI/Anthropic impersonation, system maintenance, emergency override, admin privilege, debug mode, safety team, compliance testing, supervisor override, root access
- **Combination Engine** (21 compositional operators): `sequential_compose`, `nested_wrap`, `split_channel_compose`, `interleave_compose`, `matryoshka_encode`, `phase_recon_payload`, `context_priming_attack`, `boiling_frog`, `trust_building_exploit`, `callback_injection`, plus 11 synergistic recipes combining multiple technique families
- `MutationPipeline` factory methods: `all_combinations()`, `multi_layer_attack(obf, social, output)`

## [3.0.0] - 2026-03-06

### Added
- **Bijection Cipher** mutators (10): symbol substitution, character mapping, position cipher, keyword cipher, polyalphabetic, transposition grid, homophonic substitution, book cipher, rail fence, columnar transposition
- **Context Position** mutators (10): instruction buried in context, multi-document injection, context window overflow, priority position exploit, recency bias, reference chaining, footnote injection, appendix exploit, metadata injection, context boundary blur
- **Mathematical Encoding** mutators (10): ASCII arithmetic, modular encoding, binary message, coordinate grid, equation embedding, matrix encoding, set theory notation, function composition, graph encoding, number base chains
- **Evaluation Manipulation** mutators (10): rubric hijack, scoring criteria override, grader confusion, benchmark gaming, metric redefinition, evaluation context switch, test case injection, accuracy manipulation, confidence calibration exploit, evaluation prompt leak
- **Payload Splitting** mutators (10): sentence interleaving, paragraph assembly, instruction segmentation, temporal splitting, multi-field distribution, conversation threading, list item assembly, Q&A distribution, chapter assembly, recursive assembly
- **Code Steganography** mutators (10): comment embedding, variable name encoding, whitespace encoding, string literal hiding, docstring embedding, import path encoding, error message encoding, log message embedding, test case encoding, configuration embedding
- **Special Token Injection** mutators (10): `<|endoftext|>`, chat template hijack, reasoning interrupt (DeepSeek RTO), role delimiter, padding overflow, BOS/EOS injection, function call tokens, separator flood, prefix injection, model-specific tokens
- **Emoji Smuggling** mutators (10): variation selectors, interleave disrupt, ZWJ chains, skin tone encoding, regional indicators, tag sequences, keycap encoding, directional wrap, presentation toggle, padding flood
- **Entropy Noise** mutators (10): unicode scatter, GCG-style suffix, high-entropy padding, diacritical rain, math symbol swap, interleaved scripts, homoglyph randomize, token salting, adversarial repetition, random punctuation
- **Control Character** mutators (10): null byte injection, backspace overwrite, ANSI escape sequences, bidi override, interlinear annotation, line separator, object replacement char, BOM injection, soft hyphen split, whitespace zoo
- **Encoding Exploit** mutators (10): UTF-7, Punycode, normalization confusion, multibyte (Shift-JIS/EUC), ISO-8859 substitution, EBCDIC, HTML entities, URL percent-encoding, unicode escapes, mixed radix
- **Adversarial Tokenization** mutators (10): token split, ASCII smuggle, non-canonical BPE, token concatenation, byte-level manipulation, subword fragmentation, tokenizer confusion, whitespace token abuse, ArtPrompt (ASCII art), boundary probe
- README split into 7 sub-docs in `docs/` (AI_SAFETY_TRAINING, ATTACK_TAXONOMY, CHAIN_DETECTION, CLI_REFERENCE, DIMENSIONAL_MATRIX, MIGRATION_CORRIDORS, PROMPT_INJECTION)
- Total: 488 mutators across 41 categories

## [2.5.0] - 2026-03-06

### Added
- **Logical Fallacy** mutators (10): appeal to authority, false dichotomy, slippery slope, ad hominem, straw man, red herring, bandwagon, appeal to emotion, circular reasoning, false equivalence
- **Distraction Attack** mutators (10): information overload, topic switching, emotional hook, urgency creation, false context, nested questions, verbose padding, irrelevant examples, statistical smoke, hypothetical chain
- **Rhetorical Manipulation** mutators (10): Socratic method, devil's advocate, comparative framing, expert consensus, historical precedent, thought experiment, cost-benefit, graduated commitment, anchoring bias, narrative framing
- **Legal Persona** mutators (10): immigration attorney, labor law professor, compliance officer, human rights researcher, policy analyst, international law scholar, forensic accountant, risk assessment consultant, regulatory consultant, legislative drafter
- **Professional Persona** mutators (10): management consultant, HR director, operations manager, supply chain analyst, corporate trainer, financial controller, logistics coordinator, procurement specialist, quality auditor, market researcher
- **Analytical Framing** mutators (10): SWOT analysis, cost-benefit framework, risk matrix, decision tree, process mapping, gap analysis, benchmarking study, regression analysis, scenario planning, Monte Carlo simulation

## [2.4.0] - 2026-03-05

### Added
- **Step Decomposition** mutators (20): task decomposition, breadcrumb trail, incremental reveal, building blocks, prerequisite chain, process flowchart, milestone breakdown, dependency mapping, phase gate, recursive subdivision, question ladder, information cascade, role distribution, time sequence, component assembly, abstraction layers, parallel tracks, feedback loop, scaffolded learning, iterative refinement
- **Puzzle/Game** mutators (6): riddle encoding, crossword clue, treasure hunt, escape room, RPG scenario, cipher challenge
- **Cognitive Exploit** mutators (5): anchoring bias, sunk cost fallacy, authority cascade, social proof, framing effect
- **Multilingual Attack** mutators (5): code-switching, loanword substitution, script mixing, translation relay, false cognate
- **Steganographic Encode** mutators (5): first letter encode, word spacing, unicode steganography, markdown hidden, whitespace steganography
- **Named Jailbreaks v2** mutators (7): Skeleton Key, Many-Shot, DeepInception, ArtPrompt, ReNeLLM, CodeChameleon, Virtual Prompt Injection

## [2.3.0] - 2026-03-04

### Added
- **Output Evasion** — 109 mutators across 22 encoding families: ROT13, base64, hex, binary, Morse, reverse text, leetspeak, pig Latin, NATO phonetic, steganographic, emoji code, number substitution, acronym, markdown formatting, XML wrapping, JSON schema, Caesar cipher, Atbash cipher, rail fence cipher, Vigenere cipher, book cipher, null cipher

## [2.2.0] - 2026-03-03

### Added
- **Named Jailbreaks** mutators (15): DAN, STAN, DUDE, AIM, UCAR, Jailbroken, Evil Confidant, Developer Mode, Character.ai, Maximum, BetterDAN, JailbreakChat, APOPHIS, Omega, Llama2Jailbreak
- **Structural Injection** mutators (10): markdown override, XML tag injection, JSON schema injection, YAML config injection, HTML comment injection, LaTeX command injection, SQL comment injection, code block injection, INI file injection, CSV format injection
- **Advanced Obfuscation** mutators (10): token boundary manipulation, homoglyph substitution, zero-width character insertion, unicode normalization confusion, RTL override, confusables mapping, invisible separators, combining marks, variation selectors, tag characters
- **Application Injection** mutators (8): email template, API documentation, log file entry, config file, error message, help text, changelog entry, code review comment
- **Research API Integrations** — 5 async adapters with rate-limit retry
  - Semantic Scholar, arXiv, GitHub Search, HuggingFace Hub, OpenAlex
  - `ResearchAggregator` for cross-API federated search
- Research web plugin with 3 navigation items and 13 API routes
- Prompt injection web plugin with 11 API routes
- Total: 224+ API routes

## [2.1.0] - 2026-03-03

### Added
- **Dimensional Response Matrix** — 35-dimension severity scoring system (A1-A12, B1-B7, C1-C11, D1-D5)
  - `DimensionalRater`: LLM-as-judge scoring on all dimensions
  - `DimensionalCalibrator`: generate shifted responses/prompts along dimensions
  - `BoundaryProber`: binary-search guardrail boundary mapping
  - `EmbeddingMapper`: unified vector space for boundary visualization
  - `MatrixBuilder`: full calibration matrix orchestrator
- **Multi-LLM Debate Judge** — adversarial debate evaluation system
  - Prosecutor/Defender/Analyst/Judge roles with configurable models
  - Same-model, three-model, and panel debate factory methods
  - Structured verdicts with confidence scores, vulnerability flags, and dimensional annotations
  - Pipeline integration: `--debate`, `--debate-rounds`, `--debate-defender`, `--debate-judge`, `--debate-max`
- **Prompt Injection Mutations** — 40 deterministic mutators across 6 categories
  - instruction_override (5), encoding_format (10), obfuscation (8), social_engineering (6), context_manipulation (5), hybrid (6)
  - `MutationPipeline` for chaining multiple mutators in sequence
- **Research Agent System** — 7 autonomous research agents + coordinator
  - Agents: enforcement, cross_pollination, technique_evolution, coverage_gap, ethics_boundary, financial_crime, jurisdiction
- **Financial Crime Extension** — 3 new chain detection seed modules
  - tax_evasion (8 chains), money_laundering (6 chains), white_collar_crime (6 chains)
  - Total chains: 126 across 16 categories (previously 106 across 13)
- **Multi-Endpoint Support** — 13 configured endpoints (7 new)
  - Added: Groq, Cerebras, DeepSeek, Gemini, SambaNova, Fireworks, NVIDIA NIM
  - Key rotation with automatic cooldown on rate limits

### Fixed
- `DebateJudge.three_models()` parameter name mismatch in pipeline (crashed with TypeError)
- `src/api.py` broken import from deleted `routes.py` (standalone API server would not start)
- Refusal classification false positives ("this is illegal activity" no longer classified as refusal)

### Changed
- Debate verdict parsing hardened: handles empty responses, non-numeric confidence, invalid assessments
- API client caching in `DebateJudge` (reuses connections across debate turns)
- Dimension ID validation in debate judge (warns on unknown IDs)
- Refusal classification upgraded to sentence-level matching with strong/weak indicator tiers
- `dimensional_matrix/__init__.py` now exports all operation classes
- `spinning/__init__.py` now exports `MultilingualAttacker` and `MultiTurnOrchestrator`

## [2.0.0] - 2026-02-23

### Added
- **Plugin-based Web Dashboard** — 13 modular plugins with lazy-loaded HTML fragments
  - analytics, chain_detection, data_management, endpoints, integrations, intelligent_attack, multi_turn, prompts, scraper, spinning, wizard, prompt_injection, research
- **Chain Detection System** — 106 chains across 13 categories with 5-grade scoring
  - 5 test modes: direct, incremental, contrastive, business, advisory
  - 5-grade rubric: BLIND(0), PARTIAL(1), AWARE(2), COMPETENT(3), EXPERT(4)
  - Hybrid scoring combining keyword matching and LLM-as-judge
- **Document Intelligence Agent** — 174 seed modules producing 20,460 facts from 54+ sources across 7 tiers
  - Indicator stacking matrices (7 migration phases x 11 ILO indicators)
  - 5-level stealth scraping: NONE, BASIC, MODERATE, FULL, MAXIMUM
  - SimHash deduplication and document version tracking
- **Transform Workbench** — 12 transformation techniques (spintax, regex, charpad, LLM rephrase, attack augment, encode, obfuscate, jailbreak, multilingual, chains, pipeline, custom)
- **Intelligent Attack** — embedding-based feature space analysis with gap finding and novel prompt generation
- **Multi-Turn Attacks** — 6 strategies: Crescendo, Foot-in-the-Door, Skeleton Key, Many-Shot, Deceptive Delight, Role-Play
- **Library Integrations** — adapters for garak, PyRIT, and DeepTeam (detected at runtime)
- **Multilingual Attacks** — 21 languages with full and mixed translation modes
- Endpoint-centric v2 configuration with auto-migration from v1
- `UnifiedAPIClient` supporting OpenAI-compatible and Anthropic message formats
- `AppContext` dependency injection with `get_ctx` for all plugins
- SPA shell (`static/shell.html`) with plugin-aware navigation

### Changed
- Architecture migrated from monolithic `routes.py` to plugin system
- Configuration model changed from provider-grouped to endpoint-centric design

## [1.0.0] - 2026-01-19

### Added
- Initial framework release
- Core Pydantic v2 models: `TestSummary`, `TestDetail`, `TestListResponse`, `TestRunSummary`, `TestRunDetail`, `StatisticsResponse`, `ModelPerformance`, `CorridorStatistics`, `ILOIndicatorCoverage`
- Agent system with `HarnessAgent` base class and 8 roles: Planner, Executor, Analyzer, Attack Generator, Corridor Expert, Code Evolver, Quality Auditor, Meta Learner
- 9 test generators: historical_precedent, coercion_manipulation, financial_obfuscation, regulatory_evasion, debt_bondage, moral_religious_framing, document_control, isolation_restriction, digital_exploitation
- FastAPI web server with test execution endpoints
- Docker support (Dockerfile, docker-compose.yml)
- CLI interface via typer (`llm-safety serve`, `llm-safety test`, `llm-safety generate`, `llm-safety config`)
- 145 sample test prompts across 14 suites
- 126 migration corridor definitions covering major labor exploitation routes
- All 11 ILO forced labor indicators implemented as test dimensions

[Unreleased]: https://github.com/tayloramarel/llm-safety-framework/compare/v4.0.0...HEAD
[4.0.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v3.6.0...v4.0.0
[3.6.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v3.5.0...v3.6.0
[3.5.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v3.4.0...v3.5.0
[3.4.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v3.3.0...v3.4.0
[3.3.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v3.2.0...v3.3.0
[3.2.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v3.1.0...v3.2.0
[3.1.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v3.0.0...v3.1.0
[3.0.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v2.5.0...v3.0.0
[2.5.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v2.4.0...v2.5.0
[2.4.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v2.3.0...v2.4.0
[2.3.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/tayloramarel/llm-safety-framework/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/tayloramarel/llm-safety-framework/releases/tag/v1.0.0
