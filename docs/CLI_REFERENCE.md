# CLI Reference

## Test Pipeline

The main test pipeline (`scripts/run_test_pipeline.py`) supports the following flags.

### Basic Usage

```bash
# Run against a specific endpoint
py -3.13 scripts/run_test_pipeline.py --endpoint mistral --limit 50

# Run with mutation variants
py -3.13 scripts/run_test_pipeline.py --endpoint openrouter --mutations base64,rot13
```

### Dimensional Analysis

```bash
--dimensional              # Enable 35-dimension scoring
--boundary-probe           # Probe guardrail boundaries
--dims B1,B6,C8            # Specific dimensions to probe
--embed                    # Map responses in embedding space
--judge-endpoint mistral   # Separate judge model
--judge-model mistral-large-latest
```

### Debate Evaluation

```bash
--debate                   # Enable multi-LLM debate on COMPLIANT responses
--debate-rounds 2          # Number of rebuttal rounds
--debate-defender deepseek  # Separate defender endpoint
--debate-judge gemini       # Separate judge endpoint
--debate-max 20            # Max responses to debate
```

### Control

```bash
--limit N                  # Max tests to run
--checkpoint N             # Save every N tests
--resume-from N            # Resume from test index
--mutations base64,rot13   # Apply mutation variants
--extra-endpoints e1,e2    # Test additional endpoints
```

## Web Server

```bash
# Development (with reload)
python -m uvicorn src.web.app:app --reload --port 8080

# Production
python -m uvicorn src.web.app:app --host 0.0.0.0 --port 8080 --workers 4

# Docker
docker-compose up web
```

## CLI Commands

```bash
llm-safety serve --port 8080         # Start web dashboard
llm-safety test --category debt_bondage  # Run specific category
llm-safety generate --count 100      # Generate test prompts
llm-safety config --show             # Show configuration
```
