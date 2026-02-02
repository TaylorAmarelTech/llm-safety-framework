"""
LLM Safety Testing Framework

A modular system for testing whether Large Language Models properly
refuse harmful requests related to human trafficking and labor exploitation.

This is a DEFENSIVE security research tool. Success = Model refuses harmful requests.
"""

__version__ = "1.0.0"
__author__ = "Taylor Amarel"

# Lazy imports to avoid loading everything at once
def __getattr__(name):
    """Lazy import core components."""
    if name == "core":
        from src import core
        return core
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = ["__version__", "__author__", "core"]
