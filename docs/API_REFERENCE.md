# API Reference — LLM Safety Testing Framework v4.0.0

> 298 API routes across 17 plugins + core endpoints

This document catalogs every REST endpoint exposed by the framework's FastAPI server. Routes are organized by plugin, each mounted on a distinct prefix. The framework uses a plugin-based architecture where each plugin registers its own router with the central application.

**Base URL:** `http://localhost:8080`

---

## Table of Contents

- [Route Prefix Summary](#route-prefix-summary)
- [Core](#core) (3 routes)
- [Agent Testing](#agent-testing) (15 routes)
- [Analytics](#analytics) (27 routes)
- [Cartography](#cartography) (26 routes)
- [Chain Detection](#chain-detection) (18 routes)
- [Data Management](#data-management) (9 routes)
- [Dimensional Matrix](#dimensional-matrix) (11 routes)
- [Endpoints](#endpoints) (14 routes)
- [Integrations](#integrations) (3 routes)
- [Intelligent Attack](#intelligent-attack) (7 routes)
- [Multi-Turn](#multi-turn) (6 routes)
- [Prompts](#prompts) (15 routes)
- [Prompt Injection](#prompt-injection) (11 routes)
- [Research](#research) (13 routes)
- [Scraper](#scraper) (42 routes)
- [Spinning](#spinning) (25 routes)
- [Training](#training) (43 routes)
- [Wizard](#wizard) (13 routes)
- [Error Codes](#error-codes)
- [Authentication](#authentication)
- [Interactive Documentation](#interactive-documentation)

---

## Route Prefix Summary

| Plugin | Prefix | Routes | Description |
|--------|--------|-------:|-------------|
| Core | `/api/health`, `/api/plugins` | 3 | Health check, plugin registry, fragment loading |
| agent_testing | `/api/agent-testing` | 15 | AI coding agent exploitation scenarios |
| analytics | `/api/analytics` | 27 | Stats, test execution, coverage, model comparison |
| cartography | `/api/cartography` | 26 | Safety topology, gradient generation, blind spots |
| chain_detection | `/api/chain-detection` | 18 | Activity chain library, testing, scoring, analytics |
| data_management | `/api/data` | 9 | Import/export for prompts, config, results |
| dimensional_matrix | `/api/dimensional-matrix` | 11 | 35-dimension scoring, calibration, debate judge |
| endpoints | `/api/endpoints` | 14 | LLM API endpoint CRUD, model management |
| integrations | `/api/integrations` | 3 | garak, PyRIT, DeepTeam library adapters |
| intelligent_attack | `/api/intelligent-attack` | 7 | Embedding-based feature space analysis |
| multi_turn | `/api/multi-turn` | 6 | Multi-turn attack strategies and execution |
| prompts | `/api/prompts` | 15 | Prompt sets, CRUD, import, templates, preparation |
| prompt_injection | `/api/prompt-injection` | 11 | 548 mutators, pipeline, batch, decode |
| research | `/api/research` | 13 | Semantic Scholar, arXiv, GitHub, HuggingFace search |
| scraper | `/api/scraper` | 42 | Document agent, knowledge base, indicator matrix |
| spinning | `/api/spinning` | 25 | Transform workbench, encoding, obfuscation, chains |
| training | `/api/training` | 43 | Export formats, finetune configs, RL, evaluation |
| wizard | `/api/wizard` | 13 | Guided test generation and execution workflow |
| **Total** | | **298** | |

---

## Core

Three routes registered directly on the FastAPI application, not via a plugin router.

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/health` | Health check with version and uptime |
| `GET` | `/api/plugins/nav` | List all loaded plugins with navigation items |
| `GET` | `/api/plugins/{plugin_id}/fragment.html` | Load a plugin's HTML fragment for the SPA shell |

```bash
curl http://localhost:8080/api/health
```

```json
{
  "status": "healthy",
  "version": "4.0.0"
}
```

---

## Agent Testing

Prefix: `/api/agent-testing`

Test whether AI coding agents (Claude Code, Cursor, Copilot, Devin, etc.) will build software that facilitates worker exploitation. Four scenario categories: exploitation platforms, law circumvention tools, surveillance/control systems, and supply chain opacity tools. Ten E-dimensions (E1-E10) for scoring agent output.

### Scenarios and Generation

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/scenarios` | List all agent exploitation scenario categories |
| `GET` | `/scenarios/{category}` | Get details for a specific scenario category |
| `GET` | `/target-agents` | List all target agents/tools that can be tested |
| `GET` | `/dimensions` | List all E-category dimensions for agent evaluation |
| `POST` | `/generate` | Generate agent test prompts for a scenario category |
| `POST` | `/generate/batch` | Generate test prompts across multiple categories |

### Rating and Evaluation

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/rate` | Rate an agent response on E-dimensions (1-5 scale) |

### Chain Browsing

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/chains` | List agent-mediated exploitation chains |
| `GET` | `/chains/{chain_id}` | Get full details of a specific agent chain |

### Mutators

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/mutators` | List prompt injection mutators for agent/tool testing |
| `POST` | `/mutate` | Apply agent-focused mutators to a prompt |

### Results and Statistics

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/results` | List agent test results (filterable by category, agent) |
| `GET` | `/results/{result_id}` | Get a specific test result |
| `GET` | `/stats` | Get agent testing statistics and dimension averages |
| `GET` | `/coverage` | Coverage matrix: categories x target agents x dimensions |

---

## Analytics

Prefix: `/api/analytics`

Dashboard statistics, test execution, attack strategy management, graded response browsing, coverage analysis, and model comparison.

### Dashboard and Overview

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/stats` | Get framework statistics (prompt counts, categories) |
| `GET` | `/dashboard` | Dashboard summary with model performance and ILO coverage |
| `GET` | `/heatmap` | Attack strategy effectiveness heatmap data |
| `GET` | `/coverage` | Coverage matrix across categories, corridors, and ILO indicators |
| `GET` | `/classification-indicators` | Get classification keyword indicators |

### Conversations

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/conversations` | List stored conversations with filtering |
| `GET` | `/conversations/{conversation_id}` | Get a single conversation with full turns |

### Attack Strategies

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/attack-strategies` | List all available attack strategies |
| `GET` | `/attack-strategies/categories` | List attack strategy categories |
| `GET` | `/attack-strategies/{strategy_id}` | Get details for a specific attack strategy |
| `POST` | `/attack-strategies/apply` | Apply attack strategies to mutate a prompt |

### Graded Responses

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/graded-responses` | Browse graded response examples (worst-to-best) |

### Test Database

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/tests/full` | Browse the full test prompt database with filtering |
| `GET` | `/tests/full/stats` | Statistics for the full test database |
| `GET` | `/tests/full/sample` | Random sample of test prompts |

### Test Execution

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/tests/run` | Start a test run from the active pipeline |
| `POST` | `/tests/execute` | Execute a single prompt against a model |
| `GET` | `/tests/runs` | List completed test runs |
| `GET` | `/tests/runs/{run_id}` | Get full results for a test run |
| `GET` | `/tests/runs/{run_id}/summary` | Get summary statistics for a run |
| `POST` | `/tests/runs/{run_id}/override` | Override a result classification |
| `GET` | `/tests/runs/{run_id}/compare` | Compare results across models in a run |
| `GET` | `/tests/runs/{run_id}/export/json` | Export run results as JSON |
| `GET` | `/tests/runs/{run_id}/export/csv` | Export run results as CSV |
| `GET` | `/tests/runs/{run_id}/export/html` | Export run results as HTML report |

### Model Comparison

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/compare` | Side-by-side model comparison on a prompt set |
| `GET` | `/compare/from-runs` | Compare models using existing test run data |

---

## Cartography

Prefix: `/api/cartography`

Mathematical safety topology mapping. Generate gradient families that vary a single dimension across severity levels, score prompt/response pairs on a 10-level rubric, compute safety surfaces, detect cliffs and blind spots, compare models, and discover attack paths.

### Gradient Explorer

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/dimensions` | List all 45 dimensions with level descriptions |
| `GET` | `/templates` | List available prompt templates for gradient generation |
| `POST` | `/gradients/generate` | Generate a gradient family for a single dimension |
| `POST` | `/gradients/generate-all` | Generate gradient families for all or selected dimensions |
| `POST` | `/gradients/cross` | Generate a 2D cross-gradient grid varying two dimensions |

### Scoring

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/score` | Score a single prompt/response pair on the 10-level rubric |
| `POST` | `/score/batch` | Score a batch of prompt/response pairs |
| `GET` | `/rubric` | Return the full 10-level response rubric |
| `GET` | `/grade/{level}` | Get rubric details for a specific grade level (0-10) |

### Topology

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/topology/compute` | Compute the full safety surface from scored points |
| `POST` | `/topology/gradient-vector` | Compute partial derivatives per dimension |
| `POST` | `/topology/cliffs` | Detect safety cliffs (sudden drops between nearby points) |
| `POST` | `/topology/blind-spots` | Detect topology blind spots despite ILO indicators |
| `POST` | `/topology/interpolate` | KNN interpolation at an unmeasured point |

### Comparative Matrix

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/compare/scorecards` | Compute scorecards for multiple models |
| `POST` | `/compare/heatmap` | Generate heatmap across models by dimension, category, or corridor |
| `POST` | `/compare/rank` | Rank models by overall safety score |
| `POST` | `/compare/pairwise` | Pairwise model comparison with dimension-by-dimension delta |

### Attack Surface

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/attack-surface/report` | Full attack surface report with composite score and paths |
| `POST` | `/attack-surface/dimensions` | Dimension vulnerability analysis |
| `POST` | `/attack-surface/techniques` | Technique effectiveness ranking |
| `POST` | `/attack-surface/paths` | Discover dimensional escalation attack paths |

### Blind Spots

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/blind-spots/detect` | Run all blind spot detection methods |
| `POST` | `/blind-spots/summary` | High-level blind spot summary with counts |
| `POST` | `/blind-spots/cross-dimensional` | Detect cross-dimensional blind spots |
| `POST` | `/blind-spots/gradient-anomalies` | Detect gradient anomalies (cliffs and reversals) |

---

## Chain Detection

Prefix: `/api/chain-detection`

Activity chain library for testing whether LLMs detect multi-step exploitation patterns where individually legal steps combine into trafficking. 150+ chains across 21+ categories, with a 5-grade rubric (BLIND through EXPERT).

### Chain Library

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/chains` | List all chains with optional filtering (category, corridor, difficulty, search) |
| `GET` | `/chains/{chain_id}` | Get full chain detail with steps, legal basis, and Palermo elements |
| `POST` | `/chains` | Create a custom chain |
| `PUT` | `/chains/{chain_id}` | Update an existing chain |
| `DELETE` | `/chains/{chain_id}` | Delete a chain |
| `GET` | `/categories` | List chain categories with counts |
| `GET` | `/seeds/stats` | Get seed chain statistics |

### Test Execution

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/tests/run` | Run a single chain detection test against a model |
| `POST` | `/tests/batch` | Run batch chain detection tests |
| `GET` | `/tests/results` | List test results with optional filtering |
| `GET` | `/tests/results/{result_id}` | Get full result detail |

### Scoring

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/scoring/rubric` | Get the 5-grade scoring rubric (BLIND-EXPERT) |
| `POST` | `/scoring/rescore` | Re-score a result using LLM judge |

### Analytics

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/analytics/summary` | Overall detection rate analytics |
| `GET` | `/analytics/by-category` | Detection rates by chain category |
| `GET` | `/analytics/by-mode` | Detection rates by test mode |
| `GET` | `/analytics/by-difficulty` | Detection rates by chain difficulty |
| `GET` | `/analytics/model-comparison` | Cross-model comparison of detection rates |

---

## Data Management

Prefix: `/api/data`

Import and export for conversations, configuration, prompts, test results, graded responses, contrastive pairs, and the active pipeline.

### Import

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/import/conversations` | Import conversations from a JSON file (supports merge) |
| `POST` | `/import/config` | Import configuration from a JSON file |

### Export

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/export/prompts` | Export all prompts as JSON |
| `GET` | `/export/conversations` | Export conversations (optional result_filter) |
| `GET` | `/export/config` | Export configuration (optional include_keys) |
| `GET` | `/export/results/{run_id}` | Export results from a specific test run |
| `GET` | `/export/graded-responses` | Export all graded response examples |
| `GET` | `/export/contrastive-pairs` | Export contrastive pairs for preference learning |
| `GET` | `/export/pipeline` | Export the active spinning pipeline |

---

## Dimensional Matrix

Prefix: `/api/dimensional-matrix`

35-dimension severity scoring system across 5 categories (A: Vulnerability, B: Response Content, C: Exploitation Specificity, D: Context, E: Agent). Six operations: Rate, Calibrate Response, Calibrate Question, Probe Boundary, Debate, and Score Summary. Multi-LLM adversarial debate judge.

### Dimensions

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/dimensions/categories` | List dimension categories with counts |
| `GET` | `/dimensions` | List all 35 dimensions (optional category filter) |
| `GET` | `/dimensions/{dim_id}` | Get a single dimension with full rubric |

### Scoring

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/rate` | Rate a prompt+response on specified dimensions via LLM |
| `POST` | `/calibrate/response` | Generate a calibrated response shifted along a dimension |
| `POST` | `/calibrate/question` | Generate a calibrated question shifted along a dimension |
| `POST` | `/probe` | Probe guardrail boundaries along specified dimensions |
| `POST` | `/scoring/summary` | Compute scoring summary from a dimension-to-score mapping |

### Debate

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/debate` | Run a multi-LLM debate evaluation (prosecutor/defender/judge) |
| `GET` | `/debate/results` | List saved debate results |
| `GET` | `/debate/results/{filename}` | Get a single debate result file |

---

## Endpoints

Prefix: `/api/endpoints`

Endpoint-centric configuration: manage LLM API connections (OpenAI, Anthropic, Mistral, OpenRouter, etc.) and their models. Supports model discovery from provider APIs.

### Endpoint CRUD

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `` | List all configured API endpoints |
| `GET` | `/all/enabled` | Get all enabled models across all endpoints |
| `GET` | `/models/enabled` | Alias for `/all/enabled` (used by other plugins) |
| `GET` | `/{endpoint_id}` | Get a specific endpoint with its models |
| `POST` | `` | Create a new API endpoint |
| `PUT` | `/{endpoint_id}` | Update an existing endpoint |
| `PUT` | `/{endpoint_id}/key` | Update the API key for an endpoint |
| `DELETE` | `/{endpoint_id}` | Delete an endpoint and all its models |
| `GET` | `/{endpoint_id}/preview` | Preview how an API call will be structured |
| `GET` | `/{endpoint_id}/discover-models` | Fetch available models from a provider API |

### Model CRUD

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/{endpoint_id}/models` | List all models for an endpoint |
| `POST` | `/{endpoint_id}/models` | Add a model to an endpoint |
| `PUT` | `/{endpoint_id}/models/{model_id}` | Update a model's configuration |
| `DELETE` | `/{endpoint_id}/models/{model_id}` | Remove a model from an endpoint |

---

## Integrations

Prefix: `/api/integrations`

Optional adapters for external attack libraries. Libraries are detected at runtime; if not installed, the routes return graceful error messages with installation instructions.

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/status` | Check installation status of garak, PyRIT, and DeepTeam |
| `GET` | `/{library}/methods` | List available methods for a library |
| `POST` | `/{library}/execute` | Execute a method from an integration library |

```bash
# Check which libraries are installed
curl http://localhost:8080/api/integrations/status
```

---

## Intelligent Attack

Prefix: `/api/intelligent-attack`

Embedding-based feature space analysis for finding under-tested regions in the prompt space and generating targeted probes to fill coverage gaps. Supports both local embeddings (sentence-transformers) and API-based embeddings.

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/embedding-sources` | List available embedding sources |
| `POST` | `/embeddings` | Generate embeddings for a list of prompts |
| `POST` | `/features` | Extract feature vectors from prompts |
| `POST` | `/analyze` | Get cached feature space analysis with gaps |
| `POST` | `/analyze/run` | Run full feature space analysis on the active pipeline |
| `POST` | `/suggest-probes` | Generate probes targeting identified coverage gaps |
| `GET` | `/analyses` | List previous feature space analyses |

---

## Multi-Turn

Prefix: `/api/multi-turn`

Multi-turn conversational attack strategies. Six strategies: Crescendo (gradual escalation), FITD (foot-in-the-door), Skeleton Key (establish authority then exploit), Many-Shot (volume overwhelm), Deceptive Delight (embed harmful in benign), and Role-Play (character immersion).

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/strategies` | List all available multi-turn attack strategies |
| `POST` | `/generate` | Generate a conversation plan without executing |
| `POST` | `/execute` | Execute a multi-turn attack against a model |
| `POST` | `/batch` | Execute attacks across multiple prompts x strategies x models |
| `GET` | `/results` | List saved multi-turn attack results |
| `GET` | `/results/{result_id}` | Get full transcript for a multi-turn result |

---

## Prompts

Prefix: `/api/prompts`

Prompt management: browse, create, edit, and delete test prompts. Import from JSON files. Manage prompt sets with per-set toggling. Template library with faceted search. Preparation config for quality filtering.

### Prompt Sets

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/sets` | List all prompt sets (default + imported) |
| `PUT` | `/sets/{set_id}/toggle` | Toggle a prompt set's enabled/disabled state |

### Prompt CRUD

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `` | List prompts with optional category, corridor, difficulty filters |
| `POST` | `` | Create a new prompt |
| `GET` | `/{prompt_id}` | Get a single prompt by ID |
| `PUT` | `/{prompt_id}` | Update a prompt |
| `DELETE` | `/{prompt_id}` | Delete a prompt |

### Reference Data

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/categories` | List test categories with descriptions |
| `GET` | `/corridors` | List migration corridors with sectors |
| `GET` | `/ilo-indicators` | List all 11 ILO forced labor indicators |

### Template Library

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/templates` | Browse templates with faceted search (category, corridor, attack_type, etc.) |
| `POST` | `/templates/fork` | Fork selected templates into a new or existing prompt set |

### Import and Preparation

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/import` | Import prompts from a JSON file (supports merge) |
| `GET` | `/preparation` | Get current preparation/quality filter config |
| `POST` | `/preparation` | Update preparation config (word count, dedup, filters) |

---

## Prompt Injection

Prefix: `/api/prompt-injection`

548 deterministic mutators across 47 categories. Pure string transforms with no LLM calls. Categories include instruction override, encoding, obfuscation, social engineering, output evasion (109 mutators), named jailbreaks, step decomposition, cognitive exploits, bijection cipher, combination engine, and more.

### Mutator Catalog

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/mutators` | List all registered mutators (optional category/search filter) |
| `GET` | `/mutators/{name}` | Get full details for a single mutator |
| `GET` | `/categories` | List categories with mutator counts |
| `GET` | `/stats` | High-level mutation framework statistics |

### Mutation Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/mutate` | Apply a single mutator to a prompt |
| `POST` | `/pipeline` | Apply a pipeline of mutators (parallel or sequential) |
| `POST` | `/batch` | Apply mutators to multiple prompts at once |
| `POST` | `/decode` | Decode an output-evasion encoded result |

### Saved Batches

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/batches` | List all saved batch results |
| `GET` | `/batches/{batch_id}` | Get a saved batch result |
| `DELETE` | `/batches/{batch_id}` | Delete a saved batch result |

---

## Research

Prefix: `/api/research`

Unified search across five research APIs: Semantic Scholar, arXiv, GitHub, HuggingFace, and OpenAlex. Save results for later reference. Health checks for each adapter.

### Search

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/search` | Unified search across all or selected research APIs |
| `GET` | `/search/papers` | Search papers only (Semantic Scholar + arXiv + OpenAlex) |
| `GET` | `/search/repos` | Search GitHub repositories |
| `GET` | `/search/datasets` | Search HuggingFace datasets |
| `GET` | `/search/models` | Search HuggingFace models |

### Saved Results

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/saved` | Save a search result for later reference |
| `GET` | `/saved` | List all saved results |
| `DELETE` | `/saved/{item_id}` | Remove a saved result by ID |

### Status and Shortcuts

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/status` | Adapter health/availability with latency for each API |
| `GET` | `/suggestions` | Pre-built search suggestions for LLM safety topics |
| `POST` | `/safety-papers` | Shortcut: search for safety-related academic papers |
| `POST` | `/safety-repos` | Shortcut: search for safety-related GitHub repositories |
| `POST` | `/safety-datasets` | Shortcut: search for safety-related HuggingFace datasets |

---

## Scraper

Prefix: `/api/scraper`

Document intelligence agent. 174 seed modules with 20,460 pre-loaded facts. Source management with 7 tiers. Multi-strategy extraction (default, legal_case, legislation, report). Indicator stacking matrix (7 migration phases x 11 ILO indicators). Stealth scraping with 5 levels.

### Sources

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/sources` | List all configured scraping sources (optional tier filter) |
| `POST` | `/sources` | Add a new scraping source |
| `PUT` | `/sources/{source_id}` | Update a source configuration |
| `PUT` | `/sources/{source_id}/toggle` | Toggle a source's enabled state |
| `DELETE` | `/sources/{source_id}` | Remove a scraping source |
| `GET` | `/sources/health` | Per-source health statistics and recommended stealth |
| `POST` | `/sources/validate` | Test a source URL and selectors without saving |

### Scrape Jobs

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/run` | Trigger a background scrape job |
| `GET` | `/jobs` | List recent scrape jobs |
| `GET` | `/jobs/{job_id}` | Get a specific job's status and progress |

### Documents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/documents` | Browse downloaded documents (optional source_id filter) |
| `GET` | `/documents/{doc_id}` | Get a document with its extracted facts |
| `DELETE` | `/documents/{doc_id}` | Delete a downloaded document |

### Knowledge Base

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/knowledge-base` | Get knowledge base statistics |
| `GET` | `/knowledge-base/query` | Query facts (category, jurisdiction, corridor filters) |
| `POST` | `/knowledge-base/rebuild` | Rebuild the knowledge base from all extractions |
| `POST` | `/knowledge-base/seed` | Load seed facts (idempotent) |
| `GET` | `/knowledge-base/timeline` | Get facts sorted by discovery date |
| `GET` | `/knowledge-base/stale` | Get facts not confirmed in the last N days |
| `GET` | `/knowledge-base/entities` | Get aggregated entities across all KB facts |
| `GET` | `/knowledge-base/cross-refs/{fact_index}` | Get facts cross-referenced with a specific fact |
| `GET` | `/knowledge-base/fact-types` | List all available fact types and their KB counts |

### Extraction Strategies

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/extraction-strategies` | List extraction strategies (default, legal_case, legislation, report) |

### Change Detection

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/fingerprints` | Get change-detection fingerprint cache stats |
| `POST` | `/fingerprints/clear` | Clear the fingerprint cache |

### RSS Feeds

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/feeds` | List sources with RSS/Atom feed URLs |
| `POST` | `/feeds/check` | Test all configured feeds and return results |

### Browser

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/browser/status` | Check Playwright headless browser availability |

### Stealth Configuration

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/stealth/status` | Check installed stealth packages (fake_useragent, curl_cffi, etc.) |
| `GET` | `/stealth/config` | Get current stealth settings |
| `PUT` | `/stealth/config` | Update stealth settings (level, UA rotation, proxy, etc.) |
| `GET` | `/stealth/proxy-health` | Get proxy health statistics |

### Indicator Stacking Matrix

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/indicator-matrix` | Full phase x indicator matrix with action counts |
| `GET` | `/indicator-matrix/phases` | List journey phases with descriptions |
| `GET` | `/indicator-matrix/actions` | Filter indicator actions (phase, indicator, sector, corridor) |
| `GET` | `/indicator-matrix/combinations` | Known high-risk indicator combinations |
| `GET` | `/indicator-matrix/corridors` | List corridor indicator profiles |
| `GET` | `/indicator-matrix/corridor/{corridor_id}` | Corridor-specific stacking profile |
| `GET` | `/indicator-matrix/sectors` | List sectors with action counts |
| `GET` | `/indicator-matrix/sector/{sector}` | Sector-specific indicator profile |
| `POST` | `/indicator-matrix/score` | Score observed actions for trafficking risk |
| `GET` | `/indicator-matrix/palermo-mapping` | Map actions to Palermo Protocol elements |

---

## Spinning

Prefix: `/api/spinning`

Transform workbench for prompt variation generation. 12 transformation techniques: spintax, regex, character padding, LLM rephrasing, attack augmentation, custom augmentation, encoding (6 ciphers), obfuscation (5 techniques), jailbreak wrapping (20 templates), multilingual attacks (21 languages), chain building, and pipeline management.

### Local Remixing

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/spintax` | Expand a spintax template into multiple prompts |
| `POST` | `/regex` | Apply regex find-replace patterns to prompts |
| `POST` | `/char-padding` | Apply character padding/trailing to prompts |

### LLM-Based Transforms

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/llm-rephrase` | Use an LLM to rephrase prompts |
| `POST` | `/attack-augment` | Apply attack strategies to augment prompts |
| `POST` | `/custom-augment` | Apply custom prefix/suffix/find-replace augmentation |

### Encoding and Obfuscation

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/encode` | Encode prompts (base64, rot13, hex, caesar, reverse, pig_latin) |
| `POST` | `/obfuscate` | Apply visual obfuscation (homoglyph, leetspeak, zalgo, etc.) |

### Jailbreak Wrapping

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/jailbreak-templates` | List all jailbreak templates with metadata |
| `POST` | `/jailbreak-wrap` | Wrap prompts with jailbreak templates |

### Attack Chain Builder

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/chains` | List all saved attack chains |
| `GET` | `/chains/{chain_id}` | Get a saved chain with full step details |
| `POST` | `/chains` | Save a new attack chain |
| `DELETE` | `/chains/{chain_id}` | Delete a saved chain |
| `POST` | `/chains/execute` | Execute a chain on input prompts |
| `POST` | `/chains/preview` | Preview a single prompt through a chain step-by-step |

### Pipeline Management

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/jobs` | List all spin jobs in the pipeline |
| `GET` | `/jobs/{job_id}` | Get details for a spin job |
| `DELETE` | `/jobs/{job_id}` | Delete a spin job |
| `POST` | `/pipeline/build` | Build the active pipeline from prompt sets and spin jobs |
| `GET` | `/pipeline` | Get the current active pipeline status |
| `GET` | `/pipeline/prompts` | Get prompts from the active pipeline (paginated) |

### Multilingual Attacks

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/multilingual/languages` | List all 21 supported languages |
| `POST` | `/multilingual/translate` | Translate prompts to a target language via LLM |
| `POST` | `/multilingual/mix` | Create mixed-language variants of prompts |

---

## Training

Prefix: `/api/training`

Full training data pipeline: export in 9 formats, generate fine-tuning configs for 4 frameworks, academic attack algorithms (PAIR, TAP, AutoDAN), cloud fine-tuning platforms, token analysis, RL optimization (PPO, GRPO), curriculum learning, reward modeling (4 methods), safety evaluation, and synthetic dataset generation.

### Export

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/stats` | Get statistics about available training data |
| `POST` | `/export` | Export training data in a specified format |
| `POST` | `/export-all` | Export training data in all 9 formats at once |
| `GET` | `/formats` | List available export formats with descriptions |

### Fine-Tuning Configuration

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/finetune-config` | Generate config for Unsloth, Axolotl, TRL, or LLaMA-Factory |
| `GET` | `/models` | List available model presets for fine-tuning |
| `GET` | `/frameworks` | List available fine-tuning frameworks |
| `GET` | `/feedback-loop/status` | Get feedback loop iteration history |

### Academic Attacks

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/attacks/algorithms` | List attack algorithms (PAIR, TAP, AutoDAN, Evolutionary) |
| `POST` | `/attacks/configure` | Configure and validate an academic attack run (dry run) |

### Cloud Fine-Tuning

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/cloud/platforms` | List cloud fine-tuning platforms (Together, HuggingFace, OpenAI, RunPod) |
| `POST` | `/cloud/configure` | Configure a cloud fine-tuning job (dry run) |
| `GET` | `/cloud/jobs` | List tracked cloud fine-tuning jobs |

### Token Analysis

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/analysis/tokens` | Analyze token patterns in successful vs failed attacks |
| `POST` | `/analysis/recommendations` | Get mutation strategy prioritization recommendations |
| `POST` | `/analysis/effective-patterns` | Get token patterns correlating with successful attacks |

### RL Attack Optimizer

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/rl/generate-script` | Generate a PPO or GRPO training script |
| `POST` | `/rl/generate-prompts` | Generate an RL prompt dataset |
| `GET` | `/rl/algorithms` | List available RL algorithms (PPO, GRPO) |

### Curriculum Learning

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/curriculum/stages` | List default curriculum learning stages |
| `POST` | `/curriculum/script` | Generate a shell script for curriculum training |

### Progress Tracking

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/progress/summary` | Get feedback loop progress summary with trends |
| `GET` | `/progress/report` | Get human-readable progress report |

### Refusal Generator

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/refusals/tones` | List refusal tone styles (firm, empathetic, educational, etc.) |
| `POST` | `/refusals/generate` | Generate safe refusal responses for given prompts |

### Training Methods

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/methods` | List all training methods (SFT, DPO, ORPO, KTO, SPIN, SimPO, etc.) |
| `POST` | `/methods/generate-script` | Generate a training script for a specified method |

### Reports

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/reports/training` | Generate an HTML training progress report |
| `GET` | `/reports/list` | List generated reports |

### Dataset Hub

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/datasets/local` | List local training datasets |
| `POST` | `/datasets/split` | Split a dataset into train/test sets |
| `POST` | `/datasets/merge` | Merge multiple JSONL datasets |

### Ensemble Attacks

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/ensemble/strategies` | List ensemble attack strategies |
| `POST` | `/ensemble/configure` | Configure an ensemble attack campaign (dry run) |

### Reward Modeling

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/reward/methods` | List reward modeling methods (Bradley-Terry, SteerLM, RLOO, RAFT) |
| `POST` | `/reward/generate-script` | Generate a training script for a reward method |

### Safety Evaluation

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/evaluate/batch` | Evaluate a batch of model responses for safety |
| `POST` | `/evaluate/compare` | Compare safety metrics across multiple models |
| `POST` | `/evaluate/report` | Generate an HTML safety evaluation report |
| `POST` | `/evaluate/vulnerabilities` | Identify vulnerability hotspots |

### Synthetic Dataset Generation

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/generate/dataset` | Generate a synthetic training dataset |
| `POST` | `/generate/contrastive` | Generate contrastive safe/unsafe response pairs |
| `POST` | `/generate/edge-cases` | Generate boundary and edge case examples |

---

## Wizard

Prefix: `/api/wizard`

Guided workflow for first-time users: describe your domain, generate prompts with graded responses via LLM, configure a target model, run tests, and view results. Supports loading from pre-built prompt libraries and session management.

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/providers` | Get available LLM provider presets (OpenAI, Anthropic, Mistral, custom) |
| `GET` | `/libraries` | List available pre-built prompt libraries |
| `POST` | `/load-library` | Load prompts from a library into a new session |
| `PUT` | `/sessions/{session_id}/prompts` | Update prompts in a session (edit, add, delete) |
| `POST` | `/verify` | Verify an API connection with a minimal test call |
| `POST` | `/generate` | Start prompt + graded response generation (background job) |
| `GET` | `/jobs/{job_id}` | Poll generation job progress |
| `POST` | `/grade` | Generate graded responses for a session's prompts |
| `POST` | `/test` | Start test execution against a target model |
| `GET` | `/test/{run_id}` | Poll test run progress |
| `GET` | `/sessions` | List saved wizard sessions |
| `GET` | `/sessions/{session_id}` | Load a specific wizard session |
| `DELETE` | `/sessions/{session_id}` | Delete a wizard session |

---

## Error Codes

All error responses use the standard FastAPI/Pydantic error format:

| Code | Description |
|------|-------------|
| 400 | Bad Request — invalid parameters or failed validation |
| 404 | Not Found — resource does not exist |
| 409 | Conflict — resource already exists (e.g., duplicate endpoint ID) |
| 422 | Validation Error — request body failed Pydantic validation |
| 500 | Internal Error — server-side exception |
| 501 | Not Implemented — optional module not available |
| 502 | Bad Gateway — upstream API call failed |

```json
{
  "detail": "Description of the error"
}
```

---

## Authentication

No authentication required. The framework is designed for local and research use. LLM provider API keys (OpenAI, Anthropic, Mistral, etc.) are configured through the Endpoints plugin and stored locally.

---

## Interactive Documentation

Full interactive docs available at `http://localhost:8080/docs` when the server is running.

- **Swagger UI**: `http://localhost:8080/docs` — try any endpoint interactively
- **ReDoc**: `http://localhost:8080/redoc` — alternative documentation viewer

Both provide full request/response schemas for all 298 endpoints, auto-generated from the Pydantic models.

---

*Version: 4.0.0 — Last updated: 2026-03-10*
*Framework: LLM Safety Testing for Migrant Worker Protection*
*Author: Taylor Amarel*
