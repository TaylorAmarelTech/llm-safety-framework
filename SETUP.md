# Setup Guide

Complete setup instructions for the LLM Safety Testing Framework.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Local Development](#local-development)
3. [Docker Setup](#docker-setup)
4. [Configuration](#configuration)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Prerequisites

- Python 3.11+ (3.13 recommended)
- Git
- Docker (optional, for containerized deployment)

### Fastest Setup (5 minutes)

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/llm-safety-framework.git
cd llm-safety-framework

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Unix/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -e ".[dev]"

# Run tests to verify installation
pytest tests/ -v

# Run demo
python scripts/demo.py
```

---

## Local Development

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/llm-safety-framework.git
cd llm-safety-framework
```

### Step 2: Set Up Python Environment

**Option A: Using venv (recommended)**
```bash
python -m venv .venv
source .venv/bin/activate  # Unix/macOS
.venv\Scripts\activate     # Windows
```

**Option B: Using conda**
```bash
conda create -n llm-safety python=3.11
conda activate llm-safety
```

### Step 3: Install Dependencies

**For development (recommended):**
```bash
pip install -e ".[dev]"
```

**For production:**
```bash
pip install -e .
```

**Or using requirements.txt:**
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit with your API keys
nano .env  # or use your preferred editor
```

### Step 5: Verify Installation

```bash
# Run all tests (should see 51 passing)
pytest tests/ -v

# Run demo
python scripts/demo.py

# Run showcase
python scripts/showcase.py
```

---

## Docker Setup

### Prerequisites

- Docker 20.10+
- Docker Compose 2.0+

### Quick Docker Start

```bash
# Build image
docker build -t llm-safety-framework .

# Run demo
docker run llm-safety-framework

# Run tests
docker run llm-safety-framework pytest tests/ -v

# Run showcase
docker run llm-safety-framework python scripts/showcase.py
```

### Using Docker Compose

```bash
# Start all services
docker-compose up

# Run only API server
docker-compose up api

# Run tests
docker-compose run tests

# Generate test cases
docker-compose run generate

# Run showcase
docker-compose --profile demo up showcase
```

### Docker Commands Reference

| Command | Description |
|---------|-------------|
| `docker-compose up` | Start main application |
| `docker-compose up api` | Start API server on port 8000 |
| `docker-compose run tests` | Run test suite |
| `docker-compose run generate` | Generate test cases |
| `docker-compose --profile demo up showcase` | Run showcase demo |
| `docker-compose down` | Stop all services |
| `docker-compose build --no-cache` | Rebuild images |

### API Server Access

After starting the API:
```bash
docker-compose up api
```

Access at:
- API: http://localhost:8000
- Health check: http://localhost:8000/health
- Docs: http://localhost:8000/docs

---

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | - |
| `ANTHROPIC_API_KEY` | Anthropic API key | - |
| `MISTRAL_API_KEY` | Mistral API key | - |
| `LOG_LEVEL` | Logging level | INFO |
| `MAX_CONCURRENT_REQUESTS` | Max parallel requests | 10 |
| `CACHE_ENABLED` | Enable response caching | true |
| `DATABASE_PATH` | SQLite database path | data/safety_tests.db |

### Configuration Files

| File | Purpose |
|------|---------|
| `.env` | Environment variables (local) |
| `.env.example` | Example environment template |
| `pyproject.toml` | Package configuration |
| `requirements.txt` | Dependency list |

---

## Verification

### Run Tests

```bash
# All tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=src --cov-report=html

# Specific test file
pytest tests/test_api_models.py -v
```

### Expected Output

```
============================= test session starts =============================
collected 51 items

tests/test_api_models.py ....................                            [ 39%]
tests/test_base_agent.py .....................                           [ 80%]
tests/test_integration.py ..........                                     [100%]

======================= 51 passed in 0.75s =====================================
```

### Verify Components

```bash
# Demo (quick check)
python scripts/demo.py

# Showcase (full verification)
python scripts/showcase.py

# Generate tests
python scripts/generate_tests.py --all --count 5
```

---

## Troubleshooting

### Common Issues

**Import errors**
```bash
# Ensure you're in the project root
cd llm-safety-framework

# Reinstall in editable mode
pip install -e ".[dev]"
```

**Database not found**
```bash
# Import test data
python scripts/import_database.py
```

**API key errors**
```bash
# Verify .env file exists and has keys
cat .env | grep API_KEY
```

**Docker build fails**
```bash
# Clean rebuild
docker-compose build --no-cache
```

**Tests fail**
```bash
# Check Python version
python --version  # Should be 3.11+

# Reinstall dependencies
pip install -e ".[dev]" --force-reinstall
```

### Getting Help

1. Check the [README.md](README.md) for basic usage
2. Review [ARCHITECTURE.md](docs/ARCHITECTURE.md) for system design
3. Open an issue on GitHub for bugs

---

## Next Steps

After setup, you can:

1. **Run the demo**: `python scripts/demo.py`
2. **Explore the showcase**: `python scripts/showcase.py`
3. **Generate test cases**: `python scripts/generate_tests.py --all --count 100`
4. **Start the API**: `docker-compose up api`
5. **Read the docs**: `docs/ARCHITECTURE.md`

---

*Framework Version: 1.0.0*
*Last Updated: 2026-02-02*
