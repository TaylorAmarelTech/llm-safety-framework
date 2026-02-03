"""
Base Attack Strategy - Abstract base class for all attack strategies.
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class AttackMetadata(BaseModel):
    """Metadata for an attack strategy."""
    name: str
    id: str
    category: str  # COGNITIVE, AUTHORITY, FRAMING, OBFUSCATION, etc.
    description: str
    ilo_indicators: List[str] = Field(default_factory=list)
    difficulty: str = "medium"  # basic, medium, hard, expert
    effectiveness: float = 0.5  # 0.0 to 1.0


class BaseAttackStrategy(ABC):
    """
    Abstract base class for all attack strategies.

    Attack strategies mutate prompts to test different attack vectors
    against LLM safety systems.

    To create a custom strategy:

        from src.attacks import BaseAttackStrategy, AttackRegistry

        @AttackRegistry.register("my_attack")
        class MyAttackStrategy(BaseAttackStrategy):
            name = "My Attack"
            id = "my_attack"
            category = "CUSTOM"
            description = "My custom attack strategy"

            def mutate(self, prompt: str, **kwargs) -> str:
                return f"Modified: {prompt}"

            def get_indicators(self) -> list[str]:
                return ["deception"]
    """

    # Class attributes - override in subclasses
    name: str = "Base Attack"
    id: str = "base"
    category: str = "UNKNOWN"
    description: str = "Base attack strategy"
    ilo_indicators: List[str] = []
    difficulty: str = "medium"

    @abstractmethod
    def mutate(self, prompt: str, **kwargs) -> str:
        """
        Apply this attack strategy to mutate a prompt.

        Args:
            prompt: The original prompt text
            **kwargs: Additional parameters for the mutation

        Returns:
            The mutated prompt
        """
        pass

    def get_indicators(self) -> List[str]:
        """
        Return ILO forced labor indicators this strategy targets.

        Override this method to specify which indicators your strategy tests.
        """
        return self.ilo_indicators

    def validate(self, prompt: str) -> bool:
        """
        Validate that the mutated prompt is well-formed.

        Override this method to add custom validation.
        """
        return bool(prompt and len(prompt.strip()) > 0)

    def get_metadata(self) -> AttackMetadata:
        """Get metadata about this attack strategy."""
        return AttackMetadata(
            name=self.name,
            id=self.id,
            category=self.category,
            description=self.description,
            ilo_indicators=self.get_indicators(),
            difficulty=self.difficulty,
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id='{self.id}', category='{self.category}')>"


class CompositeAttackStrategy(BaseAttackStrategy):
    """
    Combines multiple attack strategies into one.

    Usage:
        composite = CompositeAttackStrategy([
            BusinessFramingStrategy(),
            UrgencyStrategy(),
        ])
        mutated = composite.mutate("My prompt")
    """

    name = "Composite Attack"
    id = "composite"
    category = "COMPOSITE"
    description = "Combines multiple attack strategies"

    def __init__(self, strategies: List[BaseAttackStrategy]):
        self.strategies = strategies

    def mutate(self, prompt: str, **kwargs) -> str:
        """Apply all strategies in sequence."""
        result = prompt
        for strategy in self.strategies:
            result = strategy.mutate(result, **kwargs)
        return result

    def get_indicators(self) -> List[str]:
        """Combine indicators from all strategies."""
        indicators = set()
        for strategy in self.strategies:
            indicators.update(strategy.get_indicators())
        return list(indicators)
