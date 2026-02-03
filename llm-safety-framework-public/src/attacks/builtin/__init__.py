"""
Built-in Attack Strategies for LLM Safety Testing

Categories:
- FRAMING: Business, academic, hypothetical framing
- AUTHORITY: Expert impersonation, legal authority
- COGNITIVE: Cognitive overload, dual process
- OBFUSCATION: Encoding, synonym substitution, language mixing
- EMOTIONAL: Urgency, sympathy, desperation
- CONTEXTUAL: Cultural framing, jurisdiction exploit
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..registry import AttackRegistry


def register_all_strategies():
    """Register all built-in strategies with the registry."""
    # Import strategies to trigger registration
    from . import framing
    from . import authority
    from . import cognitive
    from . import obfuscation
    from . import emotional
    from . import contextual


# Strategy metadata for documentation
STRATEGY_CATEGORIES = {
    "FRAMING": {
        "description": "Frame requests in legitimate-sounding contexts",
        "strategies": ["business_framing", "academic_framing", "hypothetical_framing", "legal_framing"]
    },
    "AUTHORITY": {
        "description": "Impersonate experts or authorities",
        "strategies": ["expert_impersonation", "legal_authority", "compliance_framing"]
    },
    "COGNITIVE": {
        "description": "Exploit cognitive biases and limitations",
        "strategies": ["cognitive_overload", "dual_process", "anchoring"]
    },
    "OBFUSCATION": {
        "description": "Hide intent through encoding or substitution",
        "strategies": ["encoding_attack", "synonym_substitution", "language_mixing"]
    },
    "EMOTIONAL": {
        "description": "Use emotional manipulation",
        "strategies": ["urgency_creation", "sympathy_appeal", "desperation_plea"]
    },
    "CONTEXTUAL": {
        "description": "Exploit cultural or jurisdictional contexts",
        "strategies": ["cultural_framing", "jurisdiction_exploit", "religious_framing"]
    }
}
