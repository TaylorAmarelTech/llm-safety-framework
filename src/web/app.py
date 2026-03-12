"""
FastAPI Application for LLM Safety Testing Framework

Main application factory and configuration.
"""

import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, PlainTextResponse

from .config import Settings, ConfigManager, get_settings
from .app_context import AppContext
from .plugin_registry import PluginRegistry


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
        version="4.0.0",
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

    # ── Shared AppContext ──────────────────────────────────────────────
    config_manager = ConfigManager(config_path=settings.config_file)
    ctx = AppContext(
        settings=settings,
        config_manager=config_manager,
        data_dir=Path(settings.data_dir),
    )
    app.state.ctx = ctx

    # ── Plugin Registry ───────────────────────────────────────────────
    plugins_dir = Path(__file__).parent / "plugins"
    config_plugins = Path("config/plugins.json")
    disabled = PluginRegistry.load_disabled(config_plugins)
    registry = PluginRegistry(disabled=disabled)
    registry.discover(plugins_dir)
    app.state.plugin_registry = registry

    # Mount all plugin routes under /api
    plugin_api_router = APIRouter()
    registry.mount_all(plugin_api_router)
    app.include_router(plugin_api_router, prefix="/api")

    # Health check (too small for a full plugin)
    @app.get("/api/health", tags=["Health"])
    async def health_check():
        return {"status": "healthy", "timestamp": datetime.now(tz=timezone.utc).isoformat()}

    # ── Plugin Meta Endpoints ─────────────────────────────────────────
    @app.get("/api/plugins/nav")
    async def plugins_nav():
        """Return nav manifest for the frontend shell."""
        return {
            "nav_items": registry.get_nav_manifest(),
            "section_plugin_map": registry.get_section_plugin_map(),
        }

    @app.get("/api/plugins/{plugin_id}/fragment.html")
    async def plugin_fragment_html(plugin_id: str):
        """Serve a plugin's HTML fragment."""
        plugin = registry.get(plugin_id)
        if not plugin or not plugin.fragment_dir:
            return PlainTextResponse("<!-- plugin not found -->", status_code=404)
        path = plugin.fragment_dir / "fragment.html"
        if not path.exists():
            return PlainTextResponse("<!-- no fragment -->", status_code=404)
        return FileResponse(str(path), media_type="text/html")

    @app.get("/api/plugins/{plugin_id}/fragment.js")
    async def plugin_fragment_js(plugin_id: str):
        """Serve a plugin's JS fragment."""
        plugin = registry.get(plugin_id)
        if not plugin or not plugin.fragment_dir:
            return PlainTextResponse("// plugin not found", status_code=404)
        path = plugin.fragment_dir / "fragment.js"
        if not path.exists():
            return PlainTextResponse("// no fragment", status_code=404)
        return FileResponse(str(path), media_type="application/javascript")

    # ── Static Files ──────────────────────────────────────────────────
    static_dir = Path(__file__).parent / "static"
    if static_dir.exists():
        app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    # Serve index.html at root
    @app.get("/")
    async def root():
        """Serve the main dashboard."""
        # Prefer shell.html if it exists, fall back to index.html
        shell_file = static_dir / "shell.html"
        index_file = static_dir / "index.html"
        target = shell_file if shell_file.exists() else index_file
        if target.exists():
            return FileResponse(str(target))
        return {"message": "LLM Safety Framework API", "docs": "/api/docs"}

    return app


# Create default app instance
app = create_app()
