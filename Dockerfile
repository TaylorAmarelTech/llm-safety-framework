# LLM Safety Testing Framework
# Multi-stage Dockerfile for minimal image size

# ============================================
# Stage 1: Build stage
# ============================================
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt pyproject.toml ./

# Create virtual environment and install dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ============================================
# Stage 2: Runtime stage
# ============================================
FROM python:3.11-slim as runtime

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser

# Copy application code
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

# Switch to non-root user
USER appuser

# Default command - run the demo
CMD ["python", "scripts/demo.py"]

# ============================================
# Alternative entrypoints:
# ============================================
# Run tests:
#   docker run llm-safety pytest tests/ -v
#
# Run showcase:
#   docker run llm-safety python scripts/showcase.py
#
# Run API server:
#   docker run -p 8000:8000 llm-safety python -m uvicorn src.api:app --host 0.0.0.0 --port 8000
#
# Generate tests:
#   docker run llm-safety python scripts/generate_tests.py --all --count 100
#
# Interactive shell:
#   docker run -it llm-safety bash
