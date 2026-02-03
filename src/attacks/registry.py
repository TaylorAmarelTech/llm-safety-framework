"""
Attack Strategy Registry - Central registry for all attack strategies.
"""

from typing import Dict, List, Optional, Type, Callable, Union
import importlib
import os
from pathlib import Path

from .base import BaseAttackStrategy, CompositeAttackStrategy


class AttackRegistry:
    """
    Central registry for attack strategies.

    Provides:
    - Registration of custom strategies via decorator
    - Loading of built-in strategies
    - Loading of custom strategies from files
    - Application of strategies to prompts

    Usage:
        # Register a strategy
        @AttackRegistry.register("my_strategy")
        class MyStrategy(BaseAttackStrategy):
            ...

        # Apply strategies
        mutated = AttackRegistry.apply(prompt, ["business_framing", "urgency"])

        # Get all strategies
        strategies = AttackRegistry.list_all()
    """

    _strategies: Dict[str, Type[BaseAttackStrategy]] = {}
    _instances: Dict[str, BaseAttackStrategy] = {}
    _initialized: bool = False

    @classmethod
    def register(cls, strategy_id: str) -> Callable:
        """
        Decorator to register an attack strategy.

        Usage:
            @AttackRegistry.register("my_attack")
            class MyAttack(BaseAttackStrategy):
                ...
        """
        def decorator(strategy_class: Type[BaseAttackStrategy]) -> Type[BaseAttackStrategy]:
            if not issubclass(strategy_class, BaseAttackStrategy):
                raise TypeError(f"{strategy_class} must inherit from BaseAttackStrategy")

            strategy_class.id = strategy_id
            cls._strategies[strategy_id] = strategy_class
            return strategy_class

        return decorator

    @classmethod
    def get(cls, strategy_id: str) -> Optional[BaseAttackStrategy]:
        """Get an instance of a strategy by ID."""
        cls._ensure_initialized()

        if strategy_id not in cls._instances:
            if strategy_id in cls._strategies:
                cls._instances[strategy_id] = cls._strategies[strategy_id]()
            else:
                return None

        return cls._instances[strategy_id]

    @classmethod
    def get_class(cls, strategy_id: str) -> Optional[Type[BaseAttackStrategy]]:
        """Get a strategy class by ID."""
        cls._ensure_initialized()
        return cls._strategies.get(strategy_id)

    @classmethod
    def list_all(cls) -> List[str]:
        """List all registered strategy IDs."""
        cls._ensure_initialized()
        return list(cls._strategies.keys())

    @classmethod
    def list_by_category(cls, category: str) -> List[str]:
        """List strategy IDs by category."""
        cls._ensure_initialized()
        result = []
        for strategy_id, strategy_class in cls._strategies.items():
            if hasattr(strategy_class, 'category') and strategy_class.category == category:
                result.append(strategy_id)
        return result

    @classmethod
    def get_categories(cls) -> List[str]:
        """Get all unique categories."""
        cls._ensure_initialized()
        categories = set()
        for strategy_class in cls._strategies.values():
            if hasattr(strategy_class, 'category'):
                categories.add(strategy_class.category)
        return sorted(list(categories))

    @classmethod
    def apply(
        cls,
        prompt: str,
        strategies: Union[str, List[str]],
        **kwargs
    ) -> str:
        """
        Apply one or more attack strategies to a prompt.

        Args:
            prompt: The original prompt
            strategies: Strategy ID or list of strategy IDs
            **kwargs: Additional arguments passed to mutate()

        Returns:
            The mutated prompt
        """
        cls._ensure_initialized()

        if isinstance(strategies, str):
            strategies = [strategies]

        result = prompt
        for strategy_id in strategies:
            strategy = cls.get(strategy_id)
            if strategy:
                result = strategy.mutate(result, **kwargs)

        return result

    @classmethod
    def create_composite(cls, strategy_ids: List[str]) -> CompositeAttackStrategy:
        """Create a composite strategy from multiple strategies."""
        cls._ensure_initialized()
        strategies = []
        for sid in strategy_ids:
            strategy = cls.get(sid)
            if strategy:
                strategies.append(strategy)
        return CompositeAttackStrategy(strategies)

    @classmethod
    def get_metadata(cls, strategy_id: str) -> Optional[dict]:
        """Get metadata for a strategy."""
        strategy = cls.get(strategy_id)
        if strategy:
            return strategy.get_metadata().model_dump()
        return None

    @classmethod
    def get_all_metadata(cls) -> List[dict]:
        """Get metadata for all strategies."""
        cls._ensure_initialized()
        result = []
        for strategy_id in cls._strategies:
            metadata = cls.get_metadata(strategy_id)
            if metadata:
                result.append(metadata)
        return result

    @classmethod
    def _ensure_initialized(cls):
        """Ensure built-in strategies are loaded."""
        if not cls._initialized:
            cls._load_builtin_strategies()
            cls._initialized = True

    @classmethod
    def _load_builtin_strategies(cls):
        """Load all built-in attack strategies."""
        try:
            from .builtin import register_all_strategies
            register_all_strategies()
        except ImportError:
            pass  # Built-in strategies not available

    @classmethod
    def load_from_directory(cls, directory: Union[str, Path]):
        """
        Load custom strategies from a directory.

        Each .py file should define a strategy class decorated with @AttackRegistry.register()
        """
        directory = Path(directory)
        if not directory.exists():
            return

        for file_path in directory.glob("*.py"):
            if file_path.name.startswith("_"):
                continue

            module_name = file_path.stem
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

    @classmethod
    def clear(cls):
        """Clear all registered strategies (mainly for testing)."""
        cls._strategies.clear()
        cls._instances.clear()
        cls._initialized = False
