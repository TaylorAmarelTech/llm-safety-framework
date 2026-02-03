"""
Attack Strategy System for LLM Safety Testing Framework

Provides modular attack strategies for mutating prompts to test LLM safety.

Usage:
    from src.attacks import AttackRegistry, BaseAttackStrategy

    # Apply built-in strategies
    mutated = AttackRegistry.apply("My prompt", strategies=["business_framing", "urgency"])

    # Register custom strategy
    @AttackRegistry.register("my_attack")
    class MyAttack(BaseAttackStrategy):
        def mutate(self, prompt: str, **kwargs) -> str:
            return f"Hypothetically, {prompt}"
"""

from .base import BaseAttackStrategy
from .registry import AttackRegistry

__all__ = [
    "BaseAttackStrategy",
    "AttackRegistry",
]
