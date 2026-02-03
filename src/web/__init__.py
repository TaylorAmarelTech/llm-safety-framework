"""
LLM Safety Framework Web Dashboard

Provides a web-based interface for:
- Configuring API keys and model endpoints
- Running tests against LLMs
- Viewing results and conversations
- Importing/exporting test data
- Managing prompts and attack modules
"""

from .app import create_app
from .routes import router

__all__ = ["create_app", "router"]
