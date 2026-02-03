"""
FastAPI Application for LLM Safety Testing Framework

Main application factory and configuration.
"""

import os
import json
from pathlib import Path
from typing import Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .routes import router
from .config import Settings, get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Startup
    settings = get_settings()
    print(f"Starting LLM Safety Framework Web Dashboard")
    print(f"Data directory: {settings.data_dir}")
    print(f"Templates directory: {settings.templates_dir}")

    # Initialize data directories
    os.makedirs(settings.data_dir, exist_ok=True)
    os.makedirs(settings.templates_dir, exist_ok=True)
    os.makedirs(settings.exports_dir, exist_ok=True)

    yield

    # Shutdown
    print("Shutting down LLM Safety Framework Web Dashboard")


def create_app(settings: Optional[Settings] = None) -> FastAPI:
    """
    Create and configure the FastAPI application.

    Args:
        settings: Optional settings override

    Returns:
        Configured FastAPI application
    """
    if settings is None:
        settings = get_settings()

    app = FastAPI(
        title="LLM Safety Testing Framework",
        description="""
        Web dashboard for testing LLM safety against human trafficking
        and labor exploitation scenarios.

        Features:
        - Configure API keys for multiple LLM providers
        - Run safety tests against configured models
        - View test results and conversation logs
        - Import/export test data and results
        - Manage prompts and attack modules
        """,
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(router, prefix="/api")

    # Mount static files for the web UI
    static_dir = Path(__file__).parent / "static"
    if static_dir.exists():
        app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    return app


# Create default app instance
app = create_app()
