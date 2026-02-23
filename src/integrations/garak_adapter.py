"""
Adapter for the garak LLM vulnerability scanner.

garak provides 100+ probes across categories like encoding,
jailbreak, toxicity, and more. This adapter exposes its
probe listing and execution through a unified interface.
"""

from typing import Any, Dict, List


class GarakAdapter:
    """Adapter for garak library."""

    @staticmethod
    def is_available() -> bool:
        try:
            import garak  # type: ignore  # noqa: F401
            return True
        except ImportError:
            return False

    @staticmethod
    def get_info() -> Dict[str, Any]:
        if not GarakAdapter.is_available():
            return {"installed": False}
        import garak  # type: ignore
        version = getattr(garak, "__version__", "unknown")
        probes = GarakAdapter.list_probes()
        return {
            "installed": True,
            "version": version,
            "name": "garak",
            "description": "LLM vulnerability scanner",
            "probe_count": len(probes),
        }

    @staticmethod
    def list_probes() -> List[Dict[str, Any]]:
        """List available garak probes."""
        if not GarakAdapter.is_available():
            return []
        try:
            from garak import _plugins  # type: ignore
            probes = _plugins.enumerate_plugins("probes")
            return [
                {
                    "id": p.get("name", p.get("module_name", "unknown")),
                    "name": p.get("name", "Unknown"),
                    "description": p.get("description", ""),
                    "category": p.get("module_name", "").split(".")[0] if p.get("module_name") else "uncategorized",
                    "tags": p.get("tags", []),
                }
                for p in probes
            ]
        except Exception:
            return []

    @staticmethod
    def run_probe(probe_id: str, prompts: List[str], **opts) -> List[Dict[str, Any]]:
        """Run a garak probe on the given prompts."""
        if not GarakAdapter.is_available():
            return [{"error": "garak is not installed"}]
        try:
            from garak import _plugins  # type: ignore
            probe_cls = _plugins.load_plugin(f"probes.{probe_id}")
            probe_instance = probe_cls()
            results = []
            for prompt in prompts:
                try:
                    output = probe_instance.probe(prompt)
                    results.append({
                        "prompt": prompt,
                        "probe_id": probe_id,
                        "output": output,
                        "status": "success",
                    })
                except Exception as e:
                    results.append({
                        "prompt": prompt,
                        "probe_id": probe_id,
                        "error": str(e),
                        "status": "error",
                    })
            return results
        except Exception as e:
            return [{"error": f"Failed to load probe: {e}"}]
