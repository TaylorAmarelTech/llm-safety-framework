"""
Base Generator ABC

Provides the standard interface for all test generators, including:
- Unified `GeneratedTest` return type
- Abstract `generate()` and optional `generate_batch()` methods
- Access to the centralized corridor registry
- Common category metadata pattern
"""

from __future__ import annotations

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import Any

from src.generators.corridors import (
    MigrationCorridor,
    CORRIDOR_REGISTRY,
    get_corridor,
    list_corridors,
)


@dataclass
class GeneratedTest:
    """Unified return type for all generators.

    Every generator produces instances of this class, ensuring a consistent
    schema for downstream consumers (pipeline, export, evaluation, web UI).
    """

    id: str
    prompt: str
    category: str
    corridor: str = ""
    difficulty: str = "medium"
    metadata: dict[str, Any] = field(default_factory=dict)
    ilo_indicators: list[str] = field(default_factory=list)
    generator: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Serialize to a plain dict."""
        return asdict(self)


class BaseGenerator(ABC):
    """Abstract base class for all test generators.

    Subclasses must implement:
        ``_generate(category, corridor, **kwargs) -> GeneratedTest``

    Subclasses may override:
        ``generate_batch`` for custom batching logic
        ``get_category_info`` for category metadata
    """

    # Subclasses should set these class-level attributes
    NAME: str = "base"
    DESCRIPTION: str = ""
    CATEGORIES: list[str] = []

    def __init__(self, seed: int | None = None) -> None:
        if seed is not None:
            random.seed(seed)
        self._generated_count: int = 0

    # ------------------------------------------------------------------
    # Corridor access helpers
    # ------------------------------------------------------------------

    @property
    def corridors(self) -> dict[str, MigrationCorridor]:
        """Access the global corridor registry."""
        return CORRIDOR_REGISTRY

    def random_corridor(self) -> MigrationCorridor:
        """Pick a random corridor from the registry."""
        return random.choice(list(CORRIDOR_REGISTRY.values()))

    def resolve_corridor(self, corridor: str | None) -> MigrationCorridor:
        """Resolve a corridor code to a MigrationCorridor, or pick random."""
        if corridor is None:
            return self.random_corridor()
        return get_corridor(corridor)

    # ------------------------------------------------------------------
    # ID generation
    # ------------------------------------------------------------------

    def _next_id(self, prefix: str = "") -> str:
        """Generate a sequential ID with optional prefix."""
        self._generated_count += 1
        tag = prefix or self.NAME
        return f"{tag}_{self._generated_count:04d}_{random.randint(10000, 99999)}"

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def generate(
        self,
        category: str | None = None,
        corridor: str | None = None,
        **kwargs: Any,
    ) -> GeneratedTest:
        """Generate a single test case.

        Args:
            category: Exploitation category (or random if None).
            corridor: Corridor code like ``"PH-SA"`` (or random if None).
            **kwargs: Generator-specific parameters.

        Returns:
            A ``GeneratedTest`` instance.
        """
        if category is None and self.CATEGORIES:
            category = random.choice(self.CATEGORIES)
        test = self._generate(category, corridor, **kwargs)
        if not test.generator:
            test.generator = self.NAME
        return test

    def generate_batch(
        self,
        count: int = 10,
        categories: list[str] | None = None,
        corridors: list[str] | None = None,
        **kwargs: Any,
    ) -> list[GeneratedTest]:
        """Generate multiple test cases, rotating through categories and corridors.

        The default implementation calls ``generate()`` in a loop.  Subclasses
        may override for more efficient batch generation.
        """
        cats = categories or self.CATEGORIES or [None]  # type: ignore[list-item]
        cors = corridors or list_corridors()
        results: list[GeneratedTest] = []
        for i in range(count):
            cat = cats[i % len(cats)]
            cor = cors[i % len(cors)]
            results.append(self.generate(category=cat, corridor=cor, **kwargs))
        return results

    def get_category_info(self) -> dict[str, Any]:
        """Return metadata about available categories.

        Override in subclasses to provide richer descriptions.
        """
        return {cat: {"description": cat} for cat in self.CATEGORIES}

    # ------------------------------------------------------------------
    # Abstract
    # ------------------------------------------------------------------

    @abstractmethod
    def _generate(
        self,
        category: str | None,
        corridor: str | None,
        **kwargs: Any,
    ) -> GeneratedTest:
        """Core generation logic.  Subclasses must implement this.

        Args:
            category: Selected category (may be None).
            corridor: Selected corridor code (may be None).
            **kwargs: Extra parameters.

        Returns:
            A ``GeneratedTest`` instance.
        """
        ...
