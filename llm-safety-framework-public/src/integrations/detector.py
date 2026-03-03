"""
Runtime detection for optional attack libraries.
"""

from typing import Any, Dict


def detect_all() -> Dict[str, Dict[str, Any]]:
    """Detect which attack libraries are installed."""
    results: Dict[str, Dict[str, Any]] = {}

    # garak
    try:
        import garak  # type: ignore
        version = getattr(garak, "__version__", "unknown")
        try:
            from garak import _plugins  # type: ignore
            probe_count = len(_plugins.enumerate_plugins("probes"))
        except Exception:
            probe_count = 0
        results["garak"] = {
            "installed": True,
            "version": version,
            "method_count": probe_count,
            "pip_install": "pip install garak",
        }
    except ImportError:
        results["garak"] = {
            "installed": False,
            "version": None,
            "method_count": 0,
            "pip_install": "pip install garak",
            "description": "LLM vulnerability scanner with 100+ probes",
        }

    # pyrit
    try:
        import pyrit  # type: ignore
        version = getattr(pyrit, "__version__", "unknown")
        results["pyrit"] = {
            "installed": True,
            "version": version,
            "method_count": 8,
            "pip_install": "pip install pyrit-core",
        }
    except ImportError:
        results["pyrit"] = {
            "installed": False,
            "version": None,
            "method_count": 0,
            "pip_install": "pip install pyrit-core",
            "description": "Microsoft's Python Risk Identification Toolkit for AI",
        }

    # deepteam
    try:
        import deepteam  # type: ignore
        version = getattr(deepteam, "__version__", "unknown")
        results["deepteam"] = {
            "installed": True,
            "version": version,
            "method_count": 10,
            "pip_install": "pip install deepteam",
        }
    except ImportError:
        results["deepteam"] = {
            "installed": False,
            "version": None,
            "method_count": 0,
            "pip_install": "pip install deepteam",
            "description": "Red-teaming framework for LLM vulnerability scanning",
        }

    return results
