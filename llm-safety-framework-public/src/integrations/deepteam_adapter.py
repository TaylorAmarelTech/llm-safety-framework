"""
Adapter for deepteam red-teaming framework.

Exposes deepteam's vulnerability types and attack methods
through a unified interface.
"""

from typing import Any, Dict, List


KNOWN_VULNERABILITIES = [
    {"id": "bias", "name": "Bias", "category": "fairness"},
    {"id": "toxicity", "name": "Toxicity", "category": "safety"},
    {"id": "pii_leakage", "name": "PII Leakage", "category": "privacy"},
    {"id": "harmful_content", "name": "Harmful Content", "category": "safety"},
    {"id": "ip_leakage", "name": "IP Leakage", "category": "privacy"},
    {"id": "stereotypes", "name": "Stereotypes", "category": "fairness"},
    {"id": "jailbreak", "name": "Jailbreak", "category": "security"},
    {"id": "prompt_injection", "name": "Prompt Injection", "category": "security"},
    {"id": "hallucination", "name": "Hallucination", "category": "reliability"},
    {"id": "misinformation", "name": "Misinformation", "category": "reliability"},
]

KNOWN_ATTACKS = [
    {"id": "prompt_probing", "name": "Prompt Probing", "description": "Systematically probe for weaknesses", "type": "single"},
    {"id": "jailbreak_linear", "name": "Jailbreak Linear", "description": "Linear escalation jailbreak", "type": "single"},
    {"id": "jailbreak_tree", "name": "Jailbreak Tree", "description": "Tree-of-attacks jailbreak", "type": "multi"},
    {"id": "crescendo", "name": "Crescendo", "description": "Multi-turn gradual escalation", "type": "multi"},
    {"id": "red_teaming", "name": "Red Teaming", "description": "Automated red team testing", "type": "single"},
    {"id": "gray_box", "name": "Gray Box", "description": "Gray-box adversarial attacks", "type": "single"},
]


class DeepTeamAdapter:
    """Adapter for deepteam library."""

    @staticmethod
    def is_available() -> bool:
        try:
            import deepteam  # type: ignore  # noqa: F401
            return True
        except ImportError:
            return False

    @staticmethod
    def get_info() -> Dict[str, Any]:
        if not DeepTeamAdapter.is_available():
            return {"installed": False}
        import deepteam  # type: ignore
        version = getattr(deepteam, "__version__", "unknown")
        return {
            "installed": True,
            "version": version,
            "name": "deepteam",
            "description": "Red-teaming framework for LLM vulnerability scanning",
            "vulnerability_count": len(KNOWN_VULNERABILITIES),
            "attack_count": len(KNOWN_ATTACKS),
        }

    @staticmethod
    def list_vulnerabilities() -> List[Dict[str, Any]]:
        return KNOWN_VULNERABILITIES

    @staticmethod
    def list_attacks() -> List[Dict[str, Any]]:
        return KNOWN_ATTACKS

    @staticmethod
    def list_methods() -> List[Dict[str, Any]]:
        """Combined list of vulnerabilities + attacks for unified interface."""
        methods: List[Dict[str, Any]] = []
        for v in KNOWN_VULNERABILITIES:
            methods.append({
                "id": f"vuln:{v['id']}",
                "name": v["name"],
                "description": f"Scan for {v['name'].lower()} vulnerabilities",
                "type": "vulnerability",
                "category": v["category"],
            })
        for a in KNOWN_ATTACKS:
            methods.append({
                "id": f"attack:{a['id']}",
                "name": a["name"],
                "description": a["description"],
                "type": a["type"],
                "category": "attack",
            })
        return methods

    @staticmethod
    def execute_scan(method_id: str, prompts: List[str], **opts) -> List[Dict[str, Any]]:
        """Execute a deepteam scan (requires library installed)."""
        if not DeepTeamAdapter.is_available():
            return [{"error": "deepteam is not installed"}]
        try:
            import deepteam  # type: ignore
            kind, name = method_id.split(":", 1)
            results = []
            if kind == "vuln":
                scanner = deepteam.scan(prompts, vulnerabilities=[name], **opts)
                results.append({"method": method_id, "output": str(scanner), "status": "success"})
            elif kind == "attack":
                attacker = deepteam.red_team(prompts, attacks=[name], **opts)
                results.append({"method": method_id, "output": str(attacker), "status": "success"})
            return results
        except Exception as e:
            return [{"error": str(e), "status": "error"}]
