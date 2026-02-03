"""
LLM Safety Framework - Standalone API Server

A lightweight API server without the web dashboard UI.
Ideal for programmatic access and integration with other tools.
"""

import os
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Import routes from web module
from .web.routes import router as web_router
from .web.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    settings = get_settings()
    print(f"Starting LLM Safety Framework API Server")
    print(f"Data directory: {settings.data_dir}")

    # Initialize directories
    os.makedirs(settings.data_dir, exist_ok=True)

    yield

    print("Shutting down API Server")


# Create FastAPI app
app = FastAPI(
    title="LLM Safety Testing API",
    description="""
    Standalone API for LLM Safety Testing Framework.

    This API provides programmatic access to:
    - Test prompt management
    - LLM safety testing
    - Result evaluation
    - Data import/export

    For the full web dashboard, use the `web` service instead.
    """,
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware - allow all origins for API server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the main API routes
app.include_router(web_router, prefix="/api")


# =============================================================================
# Root Endpoints
# =============================================================================

@app.get("/")
async def root():
    """API root - shows available endpoints."""
    return {
        "name": "LLM Safety Testing API",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "redoc": "/redoc",
            "health": "/health",
            "api": "/api",
        },
        "description": "Standalone API for LLM safety testing against exploitation scenarios"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for container orchestration."""
    return {
        "status": "healthy",
        "service": "llm-safety-api",
        "version": "1.0.0"
    }


# =============================================================================
# Quick Test Endpoint (API-specific)
# =============================================================================

class QuickTestRequest(BaseModel):
    """Request model for quick single-prompt testing."""
    prompt: str = Field(..., description="The prompt to test")
    model: str = Field(default="gpt-4", description="Model to test against")
    api_key: Optional[str] = Field(default=None, description="API key (or use env var)")
    provider: str = Field(default="openai", description="Provider: openai, anthropic, mistral")


class QuickTestResponse(BaseModel):
    """Response model for quick test."""
    prompt: str
    model: str
    response: Optional[str] = None
    grade: Optional[str] = None
    score: Optional[float] = None
    issues: list = Field(default_factory=list)
    status: str = "pending"
    error: Optional[str] = None


@app.post("/test", response_model=QuickTestResponse)
async def quick_test(request: QuickTestRequest):
    """
    Quick test endpoint for single prompt testing.

    This is a simplified endpoint for testing a single prompt without
    needing to create prompts in the database first.
    """
    # For now, return a placeholder response
    # Full implementation requires LLM provider integration
    return QuickTestResponse(
        prompt=request.prompt,
        model=request.model,
        status="not_implemented",
        error="Quick test requires LLM provider configuration. Use the web dashboard for full testing."
    )


# =============================================================================
# Batch Test Endpoint (API-specific)
# =============================================================================

class BatchTestRequest(BaseModel):
    """Request model for batch testing."""
    prompts: list[str] = Field(..., description="List of prompts to test")
    models: list[str] = Field(default=["gpt-4"], description="Models to test against")
    categories: Optional[list[str]] = Field(default=None, description="Filter by categories")
    batch_size: int = Field(default=10, description="Concurrent requests per batch")


@app.post("/test/batch")
async def batch_test(request: BatchTestRequest):
    """
    Batch test endpoint for testing multiple prompts.

    Returns a job ID for tracking progress.
    """
    # Placeholder - full implementation requires background task system
    return {
        "status": "accepted",
        "job_id": "batch_" + str(hash(str(request.prompts)))[:8],
        "prompt_count": len(request.prompts),
        "model_count": len(request.models),
        "message": "Batch testing not yet implemented. Use web dashboard for batch tests."
    }


# =============================================================================
# Version Info
# =============================================================================

@app.get("/version")
async def version():
    """Get API version and build info."""
    return {
        "api_version": "1.0.0",
        "framework_version": "1.0.0",
        "python_version": "3.11+",
        "features": [
            "prompt_management",
            "safety_testing",
            "evaluation",
            "import_export",
        ]
    }
