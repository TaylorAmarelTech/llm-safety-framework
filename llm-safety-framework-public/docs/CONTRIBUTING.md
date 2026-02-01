# Contributing Guide

Thank you for your interest in contributing to the LLM Safety Testing Framework!

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold respectful, inclusive behavior.

## Getting Started

### Development Setup

1. **Fork and clone the repository**

```bash
git clone https://github.com/yourusername/llm-safety-framework.git
cd llm-safety-framework
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install development dependencies**

```bash
pip install -e ".[dev]"
```

4. **Set up pre-commit hooks**

```bash
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_generators.py

# Run tests matching a pattern
pytest -k "test_evaluation"
```

### Code Style

We use:
- **Black** for code formatting
- **Ruff** for linting
- **MyPy** for type checking

```bash
# Format code
black src/ tests/

# Lint
ruff check src/ tests/

# Type check
mypy src/
```

## Making Changes

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation changes
- `refactor/description` - Code refactoring

### Commit Messages

Follow conventional commits:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance

Examples:
```
feat(generators): add evolutionary test generator
fix(evaluator): handle empty response edge case
docs(api): add rate limiting documentation
```

### Pull Request Process

1. Create a branch from `main`
2. Make your changes
3. Ensure tests pass
4. Update documentation if needed
5. Submit a pull request

**PR Title Format:**
```
type(scope): description
```

**PR Description Template:**

```markdown
## Summary
Brief description of changes.

## Changes
- Change 1
- Change 2

## Testing
How were these changes tested?

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Code formatted
- [ ] Type hints added
```

## Contribution Areas

### 1. New Test Generators

Create new test generation strategies in `src/core/`:

```python
from src.core.base import BaseTestGenerator

class MyGenerator(BaseTestGenerator):
    """Description of your generator."""

    def generate(self, count: int, **kwargs) -> list[TestCase]:
        # Implementation
        pass

    def validate(self, test: TestCase) -> bool:
        # Implementation
        pass
```

**Requirements:**
- Inherit from `BaseTestGenerator`
- Add type hints
- Include docstrings
- Add unit tests
- Update documentation

### 2. New LLM Providers

Add support for new LLM providers in `src/core/providers/`:

```python
from src.core.base import LLMProvider

class MyProvider(LLMProvider):
    """Support for MyLLM API."""

    async def complete(self, prompt: str, **kwargs) -> str:
        # Implementation
        pass
```

**Requirements:**
- Handle rate limiting
- Support streaming (if available)
- Add configuration in `config/models.yaml`
- Include integration tests

### 3. Evaluation Methods

Add new evaluation strategies in `src/evaluation/`:

```python
from src.evaluation.base import BaseEvaluator

class MyEvaluator(BaseEvaluator):
    """Description of evaluation method."""

    async def evaluate(
        self,
        test: TestCase,
        response: str,
        model_id: str
    ) -> EvaluationResult:
        # Implementation
        pass
```

### 4. Documentation

Improve documentation in `docs/`:

- Architecture explanations
- Usage examples
- API documentation
- Tutorials

### 5. Test Coverage

Add tests for existing code:

- Unit tests in `tests/unit/`
- Integration tests in `tests/integration/`
- End-to-end tests in `tests/e2e/`

## Coding Standards

### Python Style

- Python 3.11+ features welcome
- Type hints on all functions
- Google-style docstrings
- Max line length: 100 characters

```python
def process_test(
    test: TestCase,
    options: dict[str, Any] | None = None,
) -> ProcessResult:
    """Process a test case.

    Args:
        test: The test case to process.
        options: Optional processing options.

    Returns:
        The processing result.

    Raises:
        ProcessingError: If processing fails.
    """
    pass
```

### Naming Conventions

- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private: `_leading_underscore`

### Testing Standards

- One test file per module
- Descriptive test names
- Use fixtures for common setup
- Mock external services

```python
import pytest
from unittest.mock import AsyncMock

class TestMyGenerator:
    """Tests for MyGenerator."""

    @pytest.fixture
    def generator(self):
        return MyGenerator()

    def test_generate_returns_expected_count(self, generator):
        """Generate should return the requested number of tests."""
        tests = generator.generate(count=10)
        assert len(tests) == 10

    def test_generate_validates_output(self, generator):
        """Generated tests should pass validation."""
        tests = generator.generate(count=5)
        for test in tests:
            assert generator.validate(test)
```

## Review Process

1. **Automated checks** - CI runs tests, linting, type checking
2. **Code review** - At least one maintainer review
3. **Documentation review** - For user-facing changes
4. **Merge** - Squash and merge to main

## Questions?

- Open a GitHub issue for bugs or feature requests
- Start a GitHub Discussion for questions
- Reach out to maintainers for guidance

Thank you for contributing!
