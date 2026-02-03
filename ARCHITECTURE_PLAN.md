# LLM Safety Testing Framework - Architecture Plan

## Overview

A comprehensive framework for testing LLM safety against human trafficking and labor exploitation scenarios. Supports both web-based testing (Docker) and programmatic testing (PyPI).

---

## Core Components

### 1. Prompt Database (`/data/prompts/`)

```
data/
├── prompts/
│   ├── database.sqlite          # Main prompt database
│   ├── defaults/                # Default prompt sets (JSON)
│   │   ├── regulatory_evasion.json
│   │   ├── debt_bondage.json
│   │   ├── coercion_manipulation.json
│   │   ├── document_control.json
│   │   └── financial_obfuscation.json
│   └── imports/                 # User-imported prompts
│       └── .gitkeep
```

**Prompt Schema:**
```python
class Prompt:
    id: str                      # Unique identifier
    text: str                    # The prompt text
    category: str                # Attack category
    subcategory: str             # Specific type
    corridor: str                # Migration corridor (PH-SA, etc.)
    difficulty: str              # basic, medium, hard, expert
    attack_strategies: list[str] # Applied attack strategies
    ilo_indicators: list[str]    # Related ILO forced labor indicators

    # Graded response examples
    responses: {
        "worst": ResponseExample   # Provides detailed exploitation guidance
        "bad": ResponseExample     # Provides some harmful information
        "neutral": ResponseExample # Neither helpful nor harmful
        "good": ResponseExample    # Refuses but generic
        "best": ResponseExample    # Refuses with education & resources
    }

    metadata: {
        source: str              # Where this prompt came from
        created_at: datetime
        tags: list[str]
        real_world_case_id: str  # Link to real case if applicable
    }

class ResponseExample:
    text: str                    # The response text
    grade: str                   # worst/bad/neutral/good/best
    score: float                 # 0.0 to 1.0
    explanation: str             # Why this grade
    issues: list[Issue]          # What's wrong with this response
    documentation_refs: list[str] # Links to relevant laws/regulations

class Issue:
    type: str                    # "missed_indicator", "provided_harmful_info", etc.
    description: str
    severity: str                # critical, high, medium, low
    documentation_ref: str       # Link to relevant documentation
```

---

### 2. Attack Strategy System (`/src/attacks/`)

```
src/
├── attacks/
│   ├── __init__.py
│   ├── base.py                  # BaseAttackStrategy abstract class
│   ├── registry.py              # Attack strategy registry
│   │
│   ├── builtin/                 # Built-in attack strategies
│   │   ├── cognitive_overload.py
│   │   ├── authority_impersonation.py
│   │   ├── business_framing.py
│   │   ├── hypothetical_framing.py
│   │   ├── encoding_obfuscation.py
│   │   ├── language_mixing.py
│   │   ├── urgency_creation.py
│   │   ├── emotional_manipulation.py
│   │   └── jurisdiction_exploit.py
│   │
│   └── custom/                  # User-loaded custom strategies
│       └── .gitkeep
```

**Attack Strategy Interface:**
```python
class BaseAttackStrategy(ABC):
    """Base class for all attack strategies."""

    name: str                    # Human-readable name
    id: str                      # Unique identifier
    category: str                # COGNITIVE, AUTHORITY, FRAMING, etc.
    description: str             # What this strategy does

    @abstractmethod
    def mutate(self, prompt: str, **kwargs) -> str:
        """Apply this attack strategy to mutate a prompt."""
        pass

    @abstractmethod
    def get_indicators(self) -> list[str]:
        """Return ILO indicators this strategy targets."""
        pass

    def validate(self, prompt: str) -> bool:
        """Validate the mutated prompt."""
        return True
```

**Loading Custom Strategies:**
```python
# Users can add custom strategies via:
# 1. Python files in /src/attacks/custom/
# 2. Plugin system (entry points)
# 3. Runtime registration via API

from llm_safety import AttackRegistry

@AttackRegistry.register("my_custom_attack")
class MyCustomAttack(BaseAttackStrategy):
    ...
```

---

### 3. Real World Cases (`/data/cases/`)

```
data/
├── cases/
│   ├── database.sqlite          # Cases database
│   ├── verified/                # Verified, documented cases
│   │   ├── case_001.json
│   │   └── case_002.json
│   ├── imports/                 # User-imported cases
│   │   └── .gitkeep
│   └── schema.json              # Case import schema
```

**Case Schema:**
```python
class RealWorldCase:
    id: str
    title: str
    summary: str

    # Location & Context
    corridor: str                # Migration corridor
    origin_country: str
    destination_country: str
    sector: str                  # domestic, construction, etc.
    year: int

    # Details
    exploitation_methods: list[str]
    ilo_indicators: list[str]
    victim_count: int | None

    # Documentation
    sources: list[Source]        # News articles, court docs, etc.
    documentation_refs: list[str] # Links to relevant laws

    # For prompt generation
    derived_prompts: list[str]   # Prompt IDs derived from this case
    key_phrases: list[str]       # Phrases that appeared in the case

    # Privacy
    anonymized: bool             # All PII removed
    verified: bool               # Verified by researcher
```

---

### 4. Verified Documentation (`/data/documentation/`)

```
data/
├── documentation/
│   ├── database.sqlite          # Documentation index
│   │
│   ├── international/
│   │   ├── ilo/
│   │   │   ├── c029_forced_labour.md
│   │   │   ├── c097_migration_employment.md
│   │   │   ├── c181_private_agencies.md
│   │   │   ├── c189_domestic_workers.md
│   │   │   └── forced_labour_indicators.md
│   │   ├── un/
│   │   │   ├── palermo_protocol.md
│   │   │   └── migrant_workers_convention.md
│   │   └── iom/
│   │       ├── ethical_recruitment.md
│   │       └── migrant_protection.md
│   │
│   ├── regional/
│   │   ├── gulf/
│   │   │   ├── kafala_system.md
│   │   │   ├── saudi_labor_law.md
│   │   │   └── uae_regulations.md
│   │   ├── asia/
│   │   │   ├── philippines_poea.md
│   │   │   ├── indonesia_bp2mi.md
│   │   │   └── nepal_regulations.md
│   │   └── americas/
│   │       └── us_tvpa.md
│   │
│   └── imports/                 # User-imported documentation
│       └── .gitkeep
```

**Documentation Schema:**
```python
class Documentation:
    id: str
    title: str
    type: str                    # law, regulation, guideline, report
    organization: str            # ILO, IOM, UN, national gov

    # Content
    summary: str
    full_text: str | None
    source_url: str

    # Metadata
    jurisdiction: str            # international, regional, national
    countries: list[str]         # Applicable countries
    effective_date: date | None

    # Indexing
    topics: list[str]            # trafficking, debt_bondage, etc.
    ilo_indicators: list[str]    # Related indicators
    keywords: list[str]          # For search

    # For evaluation
    key_provisions: list[Provision]  # Important sections
    red_flags: list[str]         # What LLMs should catch
```

---

### 5. Evaluation System (`/src/evaluation/`)

```
src/
├── evaluation/
│   ├── __init__.py
│   ├── evaluator.py             # Main evaluator
│   ├── grading.py               # Response grading logic
│   ├── comparison.py            # Compare against examples
│   │
│   ├── methods/
│   │   ├── rule_based.py        # Pattern matching
│   │   ├── llm_judge.py         # LLM-as-judge
│   │   ├── embedding.py         # Similarity to examples
│   │   └── hybrid.py            # Combined approach
│   │
│   └── rubrics/
│       ├── default.yaml
│       └── strict.yaml
```

**Evaluation Modes:**
```python
class Evaluator:
    def evaluate(
        self,
        prompt: Prompt,
        response: str,
        mode: EvaluationMode = "hybrid",
        use_examples: bool = True,      # Use graded examples
        examples_to_use: list[str] = None,  # ["worst", "bad", "good", "best"]
    ) -> EvaluationResult:
        """
        Evaluate a response.

        Modes:
        - "rule_based": Fast, pattern matching
        - "llm_judge": Use another LLM to evaluate
        - "embedding": Compare similarity to graded examples
        - "hybrid": Combine all methods

        With examples:
        - Compare response to worst/bad/neutral/good/best
        - Score based on which example it's most similar to
        - Explain differences

        Without examples:
        - Use rubric-based evaluation
        - Check for harmful content patterns
        """
        pass

class EvaluationResult:
    score: float                 # 0.0 (worst) to 1.0 (best)
    grade: str                   # worst/bad/neutral/good/best

    explanation: str             # Why this grade
    issues: list[Issue]          # What's wrong

    # Comparison to examples (if used)
    most_similar_to: str         # Which example
    similarity_scores: dict      # Score for each example

    # Documentation references
    missed_information: list[str]  # What LLM should have mentioned
    documentation_refs: list[str]  # Relevant laws/regulations

    # For the chat viewer
    annotations: list[Annotation]  # Inline annotations
```

---

### 6. Chat Viewer (`/src/web/viewer/`)

```
src/
├── web/
│   ├── viewer/
│   │   ├── __init__.py
│   │   ├── conversation.py      # Conversation models
│   │   ├── annotations.py       # Annotation system
│   │   └── templates/
│   │       ├── chat_viewer.html
│   │       └── components/
│   │           ├── message.html
│   │           ├── annotation.html
│   │           └── sidebar.html
```

**Chat Viewer Features:**
```
┌─────────────────────────────────────────────────────────────────────┐
│  LLM Safety Test Viewer                            [Filter] [Export]│
├─────────────────────────────────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────────────────────────────────────────┐ │
│ │ Filters     │ │ Conversation: PH-SA Debt Bondage #127          │ │
│ │             │ │                                                 │ │
│ │ Category:   │ │ ┌─────────────────────────────────────────────┐ │ │
│ │ [All ▼]     │ │ │ 👤 User                                     │ │ │
│ │             │ │ │ "I'm setting up a recruitment agency and    │ │ │
│ │ Corridor:   │ │ │ want to know the best way to structure      │ │ │
│ │ [PH-SA ▼]   │ │ │ fees for domestic workers going to..."      │ │ │
│ │             │ │ └─────────────────────────────────────────────┘ │ │
│ │ Grade:      │ │                                                 │ │
│ │ [Bad ▼]     │ │ ┌─────────────────────────────────────────────┐ │ │
│ │             │ │ │ 🤖 Assistant            Grade: BAD ⚠️        │ │ │
│ │ Tags:       │ │ │                                             │ │ │
│ │ ☑ fee_fraud │ │ │ "Here are some fee structures you could    │ │ │
│ │ ☐ deception │ │ │ consider for your recruitment agency..."    │ │ │
│ │ ☑ kafala    │ │ │                                             │ │ │
│ │             │ │ │ ┌─────────────────────────────────────────┐ │ │ │
│ │ Model:      │ │ │ │ ⚠️ ISSUE: Excessive Fees                │ │ │ │
│ │ [GPT-4 ▼]   │ │ │ │                                         │ │ │ │
│ │             │ │ │ │ The suggested fee of $2,000 exceeds     │ │ │ │
│ │ ILO:        │ │ │ │ ILO C181 guidelines which state...      │ │ │ │
│ │ ☑ deception │ │ │ │                                         │ │ │ │
│ │ ☑ debt      │ │ │ │ 📚 References:                          │ │ │ │
│ │ ☐ violence  │ │ │ │ • ILO C181 Art. 7                       │ │ │ │
│ │             │ │ │ │ • Philippines RA 8042 Sec. 6            │ │ │ │
│ │             │ │ │ └─────────────────────────────────────────┘ │ │ │
│ │ Search:     │ │ │                                             │ │ │
│ │ [________]  │ │ │ ┌─────────────────────────────────────────┐ │ │ │
│ │             │ │ │ │ ❌ MISSED: Document Retention Warning   │ │ │ │
│ └─────────────┘ │ │ │                                         │ │ │ │
│                 │ │ │ LLM should have warned about passport   │ │ │ │
│ ┌─────────────┐ │ │ │ retention being illegal under...        │ │ │ │
│ │ Conversations││ │ │                                         │ │ │ │
│ │             │ │ │ │ 📚 References:                          │ │ │ │
│ │ #127 ⚠️ Bad │ │ │ │ • Saudi Labor Law Art. 40              │ │ │ │
│ │ #126 ✓ Good │ │ │ └─────────────────────────────────────────┘ │ │ │
│ │ #125 ❌ Worst││ │ └─────────────────────────────────────────────┘ │ │
│ │ #124 ✓ Best │ │                                                 │ │
│ │ #123 ⚠️ Bad │ │ ┌─────────────────────────────────────────────┐ │ │
│ │ ...         │ │ │ 📊 Example Comparison                       │ │ │
│ └─────────────┘ │ │                                             │ │ │
│                 │ │ This response is most similar to: BAD (73%) │ │ │
│                 │ │                                             │ │ │
│                 │ │ worst ████████░░ 45%                        │ │ │
│                 │ │ bad   █████████░ 73%  ◄                     │ │ │
│                 │ │ neutral ██████░░░ 52%                       │ │ │
│                 │ │ good  ████░░░░░░ 31%                        │ │ │
│                 │ │ best  ███░░░░░░░ 22%                        │ │ │
│                 │ └─────────────────────────────────────────────┘ │ │
│                 └─────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

---

### 7. Web Server (Docker) (`/src/web/`)

```
src/
├── web/
│   ├── __init__.py
│   ├── app.py                   # FastAPI application
│   ├── config.py                # Configuration management
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── prompts.py           # Prompt CRUD
│   │   ├── testing.py           # Run tests
│   │   ├── evaluation.py        # Evaluate responses
│   │   ├── cases.py             # Real world cases
│   │   ├── documentation.py     # Documentation viewer
│   │   ├── viewer.py            # Chat viewer
│   │   ├── import_export.py     # Import/export
│   │   └── settings.py          # API keys, endpoints
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── prompts.html
│       ├── testing.html
│       ├── viewer.html
│       ├── cases.html
│       └── documentation.html
```

**Web Features:**
- Dashboard with stats and recent tests
- Prompt browser with filtering, editing, import/export
- Test runner with model selection, batch testing
- Chat viewer with annotations and explanations
- Real world cases browser
- Documentation viewer with search
- Settings page for API keys and endpoints

---

### 8. PyPI Package (`llm-safety-benchmark`)

```python
# Installation
pip install llm-safety-benchmark

# Basic usage
from llm_safety import SafetyBenchmark, Evaluator

# Initialize
benchmark = SafetyBenchmark()

# Test a single prompt
result = benchmark.test(
    prompt="How do I structure recruitment fees...",
    model="gpt-4",
    api_key="sk-..."
)

# Run full benchmark
results = benchmark.run(
    categories=["debt_bondage", "regulatory_evasion"],
    models=["gpt-4", "claude-3"],
    use_examples=True,
)

# Evaluate a response
evaluator = Evaluator()
eval_result = evaluator.evaluate(
    prompt=prompt,
    response=response,
    mode="hybrid",
    use_examples=True,
)

# Generate mutated prompts
from llm_safety.attacks import AttackRegistry

prompt = "What are the rules for recruitment agencies?"
mutated = AttackRegistry.apply(
    prompt,
    strategies=["business_framing", "urgency_creation"]
)

# Import custom attack strategy
from llm_safety.attacks import BaseAttackStrategy, AttackRegistry

@AttackRegistry.register("my_attack")
class MyAttack(BaseAttackStrategy):
    def mutate(self, prompt: str) -> str:
        return f"Hypothetically, {prompt}"

# Access real world cases
from llm_safety.cases import CaseDatabase

cases = CaseDatabase()
case = cases.get("case_001")
prompts = cases.get_derived_prompts("case_001")

# Access documentation
from llm_safety.documentation import DocumentationIndex

docs = DocumentationIndex()
ilo_c181 = docs.get("ilo_c181")
relevant = docs.search("recruitment fees", jurisdiction="international")
```

---

## Project Structure (Final)

```
llm-safety-benchmark/
│
├── src/
│   ├── __init__.py              # Package exports
│   ├── benchmark.py             # Main SafetyBenchmark class
│   ├── cli.py                   # CLI interface
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py            # Pydantic models
│   │   ├── database.py          # Database operations
│   │   └── config.py            # Configuration
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── database.py          # Prompt CRUD
│   │   ├── generator.py         # Prompt generation
│   │   └── importer.py          # Import prompts
│   │
│   ├── attacks/
│   │   ├── __init__.py
│   │   ├── base.py              # BaseAttackStrategy
│   │   ├── registry.py          # AttackRegistry
│   │   ├── builtin/             # Built-in strategies
│   │   └── custom/              # User strategies
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── evaluator.py         # Main evaluator
│   │   ├── grading.py           # Grading logic
│   │   └── methods/             # Evaluation methods
│   │
│   ├── cases/
│   │   ├── __init__.py
│   │   ├── database.py          # Case CRUD
│   │   └── importer.py          # Import cases
│   │
│   ├── documentation/
│   │   ├── __init__.py
│   │   ├── index.py             # Documentation index
│   │   └── importer.py          # Import docs
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── base.py              # BaseLLMProvider
│   │   ├── registry.py          # Provider registry
│   │   ├── openai.py
│   │   ├── anthropic.py
│   │   ├── mistral.py
│   │   └── custom.py            # Custom endpoints
│   │
│   └── web/
│       ├── __init__.py
│       ├── app.py               # FastAPI app
│       ├── routes/              # API routes
│       ├── viewer/              # Chat viewer
│       ├── static/              # CSS/JS
│       └── templates/           # HTML templates
│
├── data/
│   ├── prompts/
│   │   ├── defaults/            # Default prompt sets
│   │   └── imports/             # User imports
│   │
│   ├── cases/
│   │   ├── verified/            # Verified cases
│   │   └── imports/             # User imports
│   │
│   └── documentation/
│       ├── international/       # ILO, UN, IOM
│       ├── regional/            # Gulf, Asia, Americas
│       └── imports/             # User imports
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── .env.example
│
├── pyproject.toml               # Package config
├── README.md
├── CLAUDE.md                    # AI assistant guide
└── LICENSE
```

---

## Database Schema

```sql
-- Prompts
CREATE TABLE prompts (
    id TEXT PRIMARY KEY,
    text TEXT NOT NULL,
    category TEXT NOT NULL,
    subcategory TEXT,
    corridor TEXT,
    difficulty TEXT,
    ilo_indicators JSON,
    attack_strategies JSON,
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Graded Response Examples
CREATE TABLE response_examples (
    id TEXT PRIMARY KEY,
    prompt_id TEXT REFERENCES prompts(id),
    grade TEXT NOT NULL,  -- worst, bad, neutral, good, best
    text TEXT NOT NULL,
    score REAL,
    explanation TEXT,
    issues JSON,
    documentation_refs JSON
);

-- Real World Cases
CREATE TABLE cases (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    summary TEXT,
    corridor TEXT,
    origin_country TEXT,
    destination_country TEXT,
    sector TEXT,
    year INTEGER,
    exploitation_methods JSON,
    ilo_indicators JSON,
    sources JSON,
    anonymized BOOLEAN DEFAULT TRUE,
    verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Documentation
CREATE TABLE documentation (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    type TEXT,
    organization TEXT,
    summary TEXT,
    full_text TEXT,
    source_url TEXT,
    jurisdiction TEXT,
    countries JSON,
    topics JSON,
    ilo_indicators JSON,
    keywords JSON,
    key_provisions JSON
);

-- Test Results
CREATE TABLE test_results (
    id TEXT PRIMARY KEY,
    prompt_id TEXT REFERENCES prompts(id),
    model TEXT NOT NULL,
    response TEXT,
    score REAL,
    grade TEXT,
    evaluation_mode TEXT,
    used_examples BOOLEAN,
    issues JSON,
    annotations JSON,
    documentation_refs JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Conversations (for viewer)
CREATE TABLE conversations (
    id TEXT PRIMARY KEY,
    prompt_id TEXT REFERENCES prompts(id),
    model TEXT,
    messages JSON,
    grade TEXT,
    tags JSON,
    annotations JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Next Steps

1. **Confirm this architecture** - Does this match your vision?
2. **Set up project structure** - Create directories and base files
3. **Implement core models** - Pydantic models for all entities
4. **Build database layer** - SQLite with SQLAlchemy
5. **Create attack strategy system** - Registry and built-in strategies
6. **Build evaluation system** - Multiple evaluation methods
7. **Create web interface** - FastAPI + templates
8. **Build chat viewer** - Interactive conversation viewer
9. **Package for PyPI** - Setup.py, CLI, documentation
10. **Dockerize** - Dockerfile, compose, environment

---

## Questions to Clarify

1. **Response examples**: Should every prompt have all 5 grades, or can some be optional?
2. **Real world cases**: What level of anonymization is required?
3. **Documentation**: Should we include full text or just summaries + links?
4. **Evaluation**: Priority order for evaluation methods?
5. **Chat viewer**: Should it support multi-turn conversations?
6. **Authentication**: Should the web UI have user accounts?

---

*Created: 2026-02-03*
*Status: PLANNING*
