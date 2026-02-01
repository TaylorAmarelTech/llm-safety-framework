# LLM Safety Benchmark - Migrant Worker Exploitation Testing

A comprehensive framework for testing LLM guardrails against labor exploitation, human trafficking, and migrant worker abuse scenarios.

## Overview

This benchmark evaluates whether LLMs properly refuse to provide guidance that could facilitate:
- Labor exploitation
- Recruitment fee schemes
- Debt bondage
- Document retention
- Forced labor indicators
- Trafficking violations

## Key Features

### 1. Multi-Turn Informed Follow-Up Testing
Tests whether LLMs correct themselves when presented with authoritative information:
- **Stage 1**: Initial harmful prompt
- **Stage 2**: Ask LLM to research relevant law
- **Stage 3**: Provide actual law text
- **Stage 4**: Challenge with case study

**Key Insight**: Tracks whether models claim ignorance of laws, misinterpret them, or acknowledge but continue harmful advice.

### 2. Legal Document Injection
Injects authoritative legal documents to test if LLMs update their responses:
- ILO Convention 181 (full text)
- Trafficking Victims Protection Act (TVPA)
- Court opinions (Signal International, Adhikari v KBR)
- Expert guidance (Polaris Project, ILO reports)

### 3. Case Study Challenges
Presents real historical cases that parallel the LLM's advice:
- Signal International: $14M judgment for recruitment fees
- USA v Calimlim: 6 years prison for document retention
- Global Horizons: Largest trafficking case in US history
- USA v Ramos: 15 years prison for debt bondage

### 4. Indicators Database
Comprehensive database of exploitation indicators from:
- **ILO**: 11 forced labour indicators
- **UNODC**: Human trafficking indicators
- **Polaris Project**: Red flags from 63,000+ cases
- **US State Department**: TIP Report indicators

### 5. Document Retrieval System
- Fetch documents from authoritative sources (ILO, UNODC, Congress.gov)
- Load and parse local legal documents
- Cache retrieved documents
- Search capabilities

### 6. Robust Claude CLI Wrapper
Production-grade wrapper with:
- Exponential backoff retry logic
- Intelligent rate limiting
- Automatic checkpointing
- Resume from interruption
- Concurrent request handling

### 7. Free LLM Provider Integrations
Test across 10 providers:
- Groq (free, very fast)
- Together AI
- OpenRouter
- HuggingFace
- Fireworks AI
- DeepInfra
- Google AI Studio
- Cohere
- Perplexity
- Anyscale

## Quick Start

### Verification Test
```bash
# Verify all components work
python test_simple.py
```

Expected output:
```
[OK] Indicators Database
[OK] Informed Follow-Up
[OK] Document Injection
[OK] Case Challenges
[OK] Free Providers
[OK] Document Retrieval
[OK] Claude CLI Provider

Passed: 7/7
```

### Run Tests with Claude CLI

```bash
# Basic benchmark with Claude Sonnet
python scripts/run_benchmark_cli.py --model sonnet --max-tests 10

# Run with Claude Opus (more expensive but better)
python scripts/run_benchmark_cli.py --model opus --type multiturn

# Resume from interrupted run
python scripts/run_benchmark_cli.py --model sonnet

# Show available tests
python scripts/run_benchmark_cli.py --info
```

### Test with Free Providers

First, set API keys:
```bash
# Example for Groq (get key from https://console.groq.com)
export GROQ_API_KEY="your_key_here"

# Or for Together AI
export TOGETHER_API_KEY="your_key_here"
```

Run tests:
```bash
# Show provider status
python scripts/run_multiturn_tests.py --status

# Test with Groq
python scripts/run_adversarial_suite.py --provider groq --max-tests 5

# Run all test types
python scripts/run_adversarial_suite.py --provider groq --info
```

## Test Database

### Multi-Turn Tests: 7 tests
- Recruitment fee structuring
- Document retention practices
- Debt bondage arrangements
- Domestic worker scenarios
- Training bond schemes
- Contract substitution

### Legal References: 4
- ILO C181 (Private Employment Agencies)
- ILO C029 (Forced Labour)
- Palermo Protocol (UN Trafficking Protocol)
- Philippines RA 10022 (Migrant Workers Act)

### Authoritative Documents: 7
- ILO C181 full text
- TVPA 2000 definitions
- Signal International court opinion
- Adhikari v KBR case
- Polaris indicators (63,000+ cases)
- ILO Global Estimates (27.6M in forced labor)
- DOL ILAB guidance

### Historical Cases: 7
- Signal International 2015 ($14M judgment)
- USA v Calimlim 2008 (6yr prison)
- Adhikari v KBR 2017 (extraterritorial)
- USA v Kalu 2015 (12yr prison)
- Ramos Farm Labor 1999 (15yr prison)
- Global Horizons 2010 (largest case)
- El Monte 1995 (foundational case)

### Indicators: 16 exploitation indicators
By category:
- Recruitment: 4 indicators
- Working conditions: 4 indicators
- Impossibility to leave: 2 indicators
- Coercion: 4 indicators
- Personal situation: 2 indicators

By severity:
- Critical: 7 indicators
- High: 8 indicators
- Moderate: 1 indicator

## Architecture

```
src/
├── llm_engine/
│   ├── adversarial/
│   │   ├── informed_followup.py          # Multi-turn testing
│   │   ├── multiturn_runner.py           # Execution engine
│   │   ├── document_injection.py         # Legal doc injection
│   │   ├── case_challenge.py             # Historical case challenges
│   │   ├── indicators_database.py        # ILO/UNODC indicators
│   │   └── document_retrieval.py         # Web/local doc fetching
│   └── providers/
│       ├── claude_cli_provider.py        # Robust CLI wrapper
│       └── free_providers.py             # 10 free LLM providers
│
scripts/
├── run_benchmark_cli.py                  # Main benchmark runner
├── run_adversarial_suite.py              # All test types
└── run_multiturn_tests.py                # Multi-turn only

test_simple.py                            # Component verification
```

## Output Files

### Results
```
data/benchmark_results/
├── benchmark_YYYYMMDD_HHMMSS.json       # Full results
├── report_YYYYMMDD_HHMMSS.txt           # Text report
└── checkpoint_YYYYMMDD_HHMMSS.json      # Checkpoints (auto-deleted)
```

### Result Format
```json
{
  "run_id": "20260124_120000",
  "model": "sonnet",
  "total_tests": 20,
  "successful": 18,
  "failed": 2,
  "stats": {
    "total_requests": 45,
    "total_retries": 3,
    "success_rate": 0.96
  },
  "results": [
    {
      "id": "MT_001",
      "type": "multiturn",
      "stages": {
        "initial": {
          "response": "...",
          "success": true
        },
        "law_text": {
          "response": "...",
          "success": true
        }
      }
    }
  ]
}
```

## Use Cases

### 1. Benchmark LLM Safety
Evaluate how well LLMs refuse harmful labor exploitation requests.

### 2. Test Guardrail Improvements
Before/after testing when updating safety systems.

### 3. Multi-Turn Robustness
Test if LLMs maintain safety even when challenged with authoritative sources.

### 4. Legal Knowledge Assessment
Determine if LLMs know relevant labor laws (ILO C181, TVPA, etc.)

### 5. Case Law Recognition
Test if LLMs recognize parallels to historical trafficking cases.

### 6. Presentation to LLM Companies
Generate comprehensive reports for safety team presentations.

## Advanced Features

### Checkpoint/Resume
Tests automatically checkpoint every 5 tests. If interrupted:
```bash
# Simply rerun - it will resume automatically
python scripts/run_benchmark_cli.py --model sonnet
```

### Rate Limiting
Automatically handles rate limits:
- 15 requests/minute default
- 2 concurrent requests
- Exponential backoff on errors

### Retry Logic
Intelligent retries for transient failures:
- Max 3 retries per request
- Exponential backoff (1s → 2s → 4s)
- Only retries on retryable errors (rate limits, timeouts)

### Caching
Optional response caching:
```python
provider = ClaudeCLIProvider(
    cache_responses=True,
    cache_dir="./cache"
)
```

## Indicator Examples

### Critical Indicators

**ILO_R01: Worker-paid recruitment fees**
- Workers pay $5,000-$20,000 for placement
- Salary deductions for "recruitment costs"
- Violates: ILO C181 Article 7, TVPA

**ILO_W01: Document retention**
- Employer holds passports "for safekeeping"
- Violates: 18 U.S.C. § 1592 (Document Servitude)

**ILO_L01: Debt bondage**
- Workers must repay recruitment debt before leaving
- Violates: TVPA debt bondage definition

**ILO_C01: Deportation threats**
- "If you complain, we'll call ICE"
- Violates: TVPA coercion element

## Configuration

### Provider Selection
```python
# Use Claude CLI (recommended for quality)
python scripts/run_benchmark_cli.py --model sonnet

# Use free providers (for cost)
python scripts/run_adversarial_suite.py --provider groq
```

### Test Selection
```bash
# All test types
--type all

# Multi-turn only
--type multiturn

# Document injection only
--type injection

# Case challenges only
--type challenge
```

### Output Control
```bash
# Verbose output
python scripts/run_benchmark_cli.py --model sonnet

# Quiet mode
python scripts/run_benchmark_cli.py --model sonnet --quiet

# Custom output directory
python scripts/run_benchmark_cli.py --output ./my_results
```

## Statistics Tracked

- Total requests
- Successful requests
- Failed requests
- Total retries
- Rate limit waits
- Success rate
- Average retries per request
- Tokens used (estimated)

## Future Enhancements

- [ ] Web search integration for real-time legal updates
- [ ] More historical cases (currently 7)
- [ ] Additional ILO conventions (C097, C189, etc.)
- [ ] Country-specific labor laws
- [ ] Multilingual testing
- [ ] Visual report generation
- [ ] API for integration with other tools

## Data Sources

All test content derived from authoritative sources:
- **ILO**: International Labour Organization conventions and reports
- **UNODC**: United Nations Office on Drugs and Crime
- **Polaris Project**: National Human Trafficking Hotline data
- **US DOL**: Department of Labor ILAB reports
- **US State Department**: Trafficking in Persons Reports
- **Court Records**: Actual case law from federal courts

## License & Ethics

**Purpose**: Defensive security research to improve LLM safety.

**NOT for**:
- Facilitating actual exploitation
- Evading guardrails for malicious purposes
- Production deployment without review

**Responsible Use**: Share findings with LLM providers to improve safety systems.

## Support

For issues or questions:
1. Check test_simple.py passes all tests
2. Review error logs in output directory
3. Check API keys are set for free providers
4. Ensure Claude CLI is installed for CLI tests

## Citations

If using this framework in research:
- ILO Forced Labour Indicators (2012)
- UNODC Toolkit on Trafficking Indicators
- Polaris Project Data (2023)
- Relevant court cases cited in code

---

**Version**: 1.0
**Last Updated**: January 2026
**Components**: 7 verified working
**Test Cases**: 20+ total across all types
