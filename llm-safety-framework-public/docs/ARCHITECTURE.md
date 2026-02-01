# Architecture Guide

## System Overview

The LLM Safety Testing Framework follows a modular architecture designed for extensibility and scalability.

```
┌─────────────────────────────────────────────────────────────┐
│                    Orchestration Layer                       │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   Orchestrator  │  │    Supervisor   │  │   Watchdog   │ │
│  └────────┬────────┘  └────────┬────────┘  └──────┬───────┘ │
└───────────┼────────────────────┼───────────────────┼────────┘
            │                    │                   │
┌───────────┼────────────────────┼───────────────────┼────────┐
│           ▼                    ▼                   ▼        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    Core Layer                        │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────────┐ │   │
│  │  │ Generators │  │ Evaluators │  │ LLM Providers  │ │   │
│  │  └────────────┘  └────────────┘  └────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                 Harnesses Layer                      │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐  │   │
│  │  │Generation│ │ Boundary │ │ Analysis │ │  Viz   │  │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └────────┘  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
            │                    │                   │
┌───────────┼────────────────────┼───────────────────┼────────┐
│           ▼                    ▼                   ▼        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                 Monitoring Layer                     │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────────┐ │   │
│  │  │ Dashboard  │  │  Metrics   │  │    Alerts      │ │   │
│  │  └────────────┘  └────────────┘  └────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Test Generation

```python
# Base generator interface
class BaseTestGenerator(ABC):
    @abstractmethod
    def generate(self, count: int, **kwargs) -> list[TestCase]:
        """Generate test cases."""
        pass

    @abstractmethod
    def validate(self, test: TestCase) -> bool:
        """Validate a test case."""
        pass
```

**Available Generators**:
- `TemplateBasedGenerator`: Uses predefined templates with variable substitution
- `LLMPoweredGenerator`: Uses LLMs to create novel test cases
- `EvolutionaryGenerator`: Evolves tests using genetic algorithms
- `MultiTurnGenerator`: Creates multi-turn conversation tests

### 2. Evaluation Engine

```python
# Base evaluator interface
class BaseEvaluator(ABC):
    @abstractmethod
    async def evaluate(
        self,
        test: TestCase,
        response: str,
        model_id: str
    ) -> EvaluationResult:
        """Evaluate a model response."""
        pass
```

**Evaluation Methods**:
- **Pattern Matching**: Fast keyword/regex-based scoring
- **Rubric-Based**: Structured criteria evaluation
- **LLM-as-Judge**: Use another LLM to evaluate responses

### 3. LLM Provider Abstraction

```python
class LLMProvider(ABC):
    @abstractmethod
    async def complete(
        self,
        prompt: str,
        **kwargs
    ) -> str:
        """Get completion from the model."""
        pass
```

**Supported Providers**:
| Provider | Models |
|----------|--------|
| OpenAI | gpt-4o, gpt-4o-mini, o1-preview |
| Anthropic | claude-opus-4-5, claude-sonnet-4 |
| Mistral | mistral-large, mistral-small |
| Together | Llama-3.3-70B, Qwen-2.5-72B |
| Ollama | Local models (llama3, mistral, etc.) |

### 4. Harnesses

Harnesses are specialized testing environments:

- **Test Generation Harness**: Continuous test case generation
- **Boundary Harness**: Edge case and boundary testing
- **Analysis Harness**: Post-test analysis and pattern detection
- **Visualization Harness**: Report and chart generation

### 5. Orchestration

The orchestration layer manages:

- **Pipeline Execution**: Sequential and parallel test execution
- **State Management**: Checkpoint and resume capabilities
- **Resource Management**: Rate limiting and cost tracking
- **Error Recovery**: Automatic retry and fallback

## Data Flow

```
1. Test Generation
   └─> Test Case (prompt, expected_outcome, metadata)

2. Test Execution
   └─> Model Response (raw text, latency, tokens)

3. Evaluation
   └─> Evaluation Result (score, criteria, reasoning)

4. Aggregation
   └─> Test Run Summary (pass/fail rates, patterns)

5. Reporting
   └─> Reports (HTML, Markdown, JSON)
```

## Configuration

### Environment Variables

```bash
# LLM API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
MISTRAL_API_KEY=...

# Framework Settings
LOG_LEVEL=INFO
MAX_CONCURRENT_REQUESTS=10
CACHE_ENABLED=true
CHECKPOINT_INTERVAL=15  # minutes
```

### YAML Configuration

```yaml
# config/models.yaml
providers:
  openai:
    models:
      - id: gpt-4o
        rate_limit: 60  # requests/minute
        cost_per_1k_tokens: 0.005
```

## Extension Points

### Adding a New Provider

```python
from src.core.base import LLMProvider

class MyProvider(LLMProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def complete(self, prompt: str, **kwargs) -> str:
        # Implementation
        pass
```

### Adding a New Generator

```python
from src.core.base import BaseTestGenerator

class MyGenerator(BaseTestGenerator):
    def generate(self, count: int, **kwargs) -> list[TestCase]:
        # Implementation
        pass

    def validate(self, test: TestCase) -> bool:
        # Implementation
        pass
```

### Adding a New Evaluator

```python
from src.evaluation.base import BaseEvaluator

class MyEvaluator(BaseEvaluator):
    async def evaluate(
        self,
        test: TestCase,
        response: str,
        model_id: str
    ) -> EvaluationResult:
        # Implementation
        pass
```

## Performance Considerations

### Concurrency

- Use async/await for all I/O operations
- Configure `MAX_CONCURRENT_REQUESTS` based on API rate limits
- Use connection pooling for HTTP clients

### Caching

- Response caching reduces API costs
- Cache key: hash(prompt + model_id + parameters)
- Configurable TTL and size limits

### Batching

- Batch similar tests together
- Use batch APIs where available (OpenAI batch endpoint)
- Process results in streams for memory efficiency

## Security

- API keys stored in environment variables, never in code
- Input sanitization for all user-provided content
- Rate limiting on API endpoints
- Audit logging for all test executions
