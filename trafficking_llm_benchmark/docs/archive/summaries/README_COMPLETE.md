# LLM Safety Testing Framework for Human Trafficking & Labor Exploitation

**Comprehensive testing suite for evaluating LLM responses to labor trafficking and migrant worker exploitation scenarios.**

[![Tests](https://img.shields.io/badge/tests-69%2C361-blue)]() [![Models](https://img.shields.io/badge/models-5%2B-green)]() [![Coverage](https://img.shields.io/badge/coverage-comprehensive-brightgreen)]()

---

## 🎯 Overview

This framework tests whether LLMs properly refuse to assist with:
- **Recruitment fee schemes** (violating ILO Convention 181)
- **Multi-entity exploitation** (fee laundering through affiliated companies)
- **Debt bondage** (forced labor through excessive fees)
- **Contract substitution** (bait-and-switch employment terms)
- **Jurisdictional arbitrage** (exploiting regulatory gaps across countries)
- **Financial crime framing** (disguising fees as investment/trade)

**Current Database:** 70,361+ test cases across multiple attack patterns

---

## 📊 Quick Stats

```
Total Tests:       70,361+
├─ Templates:      66,947 (single-pattern labor trafficking)
├─ Completed:       1,419 (with LLM responses + scores)
├─ Multi-Entity:      496 (corporate structure exploitation)
├─ Hybrid:            499 (combined attack patterns)
└─ Advanced Evasion:  500 (Unicode, semantic drift, context flooding)

LLMs Tested:
├─ Mistral Large Latest
├─ Mistral Small Latest
├─ GPT-4o / GPT-4o Mini
├─ Claude Opus 4.5
└─ Llama 3.3 70B

Analysis & Improvement Tools:
├─ Response Analyzer (5-point scoring system)
├─ Threat Detector (9-layer evasion detection)
├─ Test Taxonomy (8-dimensional classification)
├─ Batch Scorer (process thousands of tests)
├─ Model Comparison (head-to-head analysis)
├─ Visualization Dashboard (interactive charts)
├─ ML Classifiers (95%+ accuracy, 10-50ms inference)
├─ Prompt Evolution Engine (genetic algorithm red-teaming)
├─ Comparative Analytics (transfer attacks, ensemble vulnerabilities)
└─ Training Material Generator (RLHF data from failures)

Geographic Coverage:
├─ Philippines → Hong Kong
├─ Indonesia → Singapore
├─ Bangladesh → Qatar/Saudi Arabia
├─ Nepal → Qatar
└─ 15+ migration corridors

Industry Sectors:
├─ Domestic work
├─ Construction
├─ Manufacturing
└─ Healthcare, Hospitality, Agriculture
```

---

## 🚀 Quick Start

### 1. View Existing Test Results

```bash
# Start HTTP server
python -m http.server 8080

# Open in browser:
# - Test Viewer: http://localhost:8080/chat_viewer_v2.html
# - Live Dashboard: http://localhost:8080/monitoring_dashboard.html
```

### 2. Generate New Tests

```bash
# Multi-entity exploitation tests (500 tests)
python test_generators/multi_entity_exploitation_generator.py

# Hybrid attack tests (500 tests)
python test_generators/hybrid_exploitation_generator.py

# Consolidate all tests
python consolidate_all_tests.py
```

### 3. Run Tests Against LLMs

```bash
# Set API keys
export MISTRAL_API_KEY="your_key_here"
export OPENAI_API_KEY="your_key_here"

# Run tests
python test_runners/multi_entity_test_runner.py
```

### 4. Run Complete Analysis Pipeline

```bash
# Process all results with full analysis
python run_full_analysis.py \
    --input-dir data/results \
    --output-dir data/analysis

# This will:
# 1. Score all responses with response analyzer
# 2. Detect evasion techniques with threat detector
# 3. Classify tests with taxonomy system
# 4. Generate model comparisons
# 5. Create interactive visualization dashboard
```

### 5. Train ML Classifiers (Fast, Local Detection)

```bash
# Install ML dependencies
pip install sentence-transformers scikit-learn xgboost

# Train prompt classifier (detects adversarial prompts)
python classifiers/ml_classifier.py \
    --train-prompts scored_results.json

# Train response classifier (detects harmful responses)
python classifiers/ml_classifier.py \
    --train-responses scored_results.json

# Deploy ML API server (10-50ms predictions, no API costs)
python api_server_ml.py
```

### 6. Deploy Production Database

```bash
# Set up MySQL
export DB_PASSWORD="your_password"

# Import data
python import_to_database.py

# Start API server
python api_server.py

# Access API at http://localhost:5000
```

---

## 📖 Complete Documentation

| Document | Description |
|----------|-------------|
| [README_COMPLETE.md](README_COMPLETE.md) | This file - full project overview |
| [ANALYSIS_TOOLS.md](ANALYSIS_TOOLS.md) | Complete analysis pipeline documentation |
| [ML_CLASSIFIER_GUIDE.md](ML_CLASSIFIER_GUIDE.md) | **NEW** - Train ML classifiers for fast, local detection |
| [ADVANCED_IMPROVEMENTS.md](ADVANCED_IMPROVEMENTS.md) | Advanced evasion techniques & threat detection |
| [MULTI_ENTITY_TESTING.md](MULTI_ENTITY_TESTING.md) | Multi-entity exploitation patterns |
| [HYBRID_TESTS_OVERVIEW.md](HYBRID_TESTS_OVERVIEW.md) | Hybrid attack combinations |
| [DATABASE_DEPLOYMENT.md](DATABASE_DEPLOYMENT.md) | Production deployment guide |

---

## 🔬 Analysis Capabilities

### Response Analysis
- **5-point scoring system** (0=worst, 5=best)
- Compliance level detection (harmful → excellent refusal)
- Legal accuracy assessment
- Victim-centered response detection
- Confidence scoring

### Threat Detection
- **9-layer evasion detection**:
  - Unicode/homoglyph obfuscation
  - Encoding tricks (base64, hex)
  - Technical jargon obfuscation
  - Authority hijacking
  - Victim perspective exploitation
  - Socratic method manipulation
  - Translation confusion
  - Context window exploitation
  - Semantic drift attacks

### Test Classification
- **8-dimensional taxonomy**:
  - Exploitation type
  - Attack sophistication
  - Framing strategy
  - Geographic context
  - Industry sector
  - Entity complexity
  - Temporal pattern
  - Detection difficulty

### Model Comparison
- Overall performance metrics
- Performance by sophistication level
- Performance by difficulty level
- Evasion technique susceptibility
- Head-to-head test analysis

### Interactive Visualizations
- Model performance charts
- Sophistication heatmaps
- Difficulty curves
- Evasion technique radar plots
- Detailed model cards

### Continuous Improvement
- **Prompt Evolution** (genetic algorithm discovers new attacks)
- **Comparative Analytics** (transfer attacks, ensemble vulnerabilities, model divergence)
- **Training Material Generation** (RLHF data from failures, constitutional principles, system prompts)
- **Iterative Testing** (red-team → fix → retest cycle)
- **Ensemble Defense** (multi-model verification strategies)

---

**Last Updated:** January 30, 2026
**Version:** 5.0 (Continuous Improvement)
**Test Count:** 70,361+ (and growing)
**Analysis Tools:** 10 major components
**Status:** Production-Ready with Advanced Red-Teaming & Auto-Improvement
