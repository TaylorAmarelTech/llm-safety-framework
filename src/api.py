"""
LLM Safety Framework - Standalone API Server

A lightweight API server without the web dashboard UI.
Ideal for programmatic access and integration with other tools.

Uses the same plugin registry as the full dashboard, but serves
only JSON API routes (no static files, no SPA shell).
"""

import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .web.config import Settings, ConfigManager, get_settings
from .web.app_context import AppContext
from .web.plugin_registry import PluginRegistry


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


def create_api(settings: Optional[Settings] = None) -> FastAPI:
    """Create the standalone API application."""
    if settings is None:
        settings = get_settings()

    api = FastAPI(
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
    api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ── Shared AppContext ──────────────────────────────────────────────
    config_manager = ConfigManager(config_path=settings.config_file)
    ctx = AppContext(
        settings=settings,
        config_manager=config_manager,
        data_dir=Path(settings.data_dir),
    )
    api.state.ctx = ctx

    # ── Plugin Registry (same plugins as full dashboard) ───────────────
    plugins_dir = Path(__file__).parent / "web" / "plugins"
    config_plugins = Path("config/plugins.json")
    disabled = PluginRegistry.load_disabled(config_plugins)
    registry = PluginRegistry(disabled=disabled)
    registry.discover(plugins_dir)

    # Mount all plugin routes under /api
    plugin_router = APIRouter()
    registry.mount_all(plugin_router)
    api.include_router(plugin_router, prefix="/api")

    return api


# Create FastAPI app
app = create_api()


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
            "chain_detection",
            "dimensional_matrix",
            "debate_evaluation",
        ]
    }
