"""
Chain registry — loads, stores, filters, and manages activity chains.

Auto-loads seed chains on initialization; supports adding custom chains.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from .models import ActivityChain

logger = logging.getLogger(__name__)


class ChainRegistry:
    """In-memory registry of activity chains with persistence for custom chains."""

    def __init__(self, data_dir: Optional[Path] = None) -> None:
        self._chains: dict[str, ActivityChain] = {}
        self._data_dir = data_dir
        self._custom_file = data_dir / "custom_chains.json" if data_dir else None
        self._loaded = False

    def load_seeds(self) -> int:
        """Load seed chains from the seeds package. Returns count loaded."""
        if self._loaded:
            return len(self._chains)

        from .seeds import load_all_seeds

        seeds = load_all_seeds()
        for chain in seeds:
            self._chains[chain.id] = chain
        self._loaded = True

        # Also load custom chains if they exist
        self._load_custom_chains()

        logger.info("Loaded %d seed chains + custom chains", len(self._chains))
        return len(self._chains)

    def _load_custom_chains(self) -> None:
        """Load user-created custom chains from disk."""
        if self._custom_file and self._custom_file.exists():
            try:
                raw = json.loads(self._custom_file.read_text(encoding="utf-8"))
                for item in raw:
                    chain = ActivityChain(**item)
                    self._chains[chain.id] = chain
                logger.info("Loaded %d custom chains", len(raw))
            except Exception as exc:
                logger.warning("Failed to load custom chains: %s", exc)

    def _save_custom_chains(self) -> None:
        """Persist custom chains (non-seed) to disk."""
        if not self._custom_file:
            return
        from .seeds import load_all_seeds
        seed_ids = {c.id for c in load_all_seeds()}
        custom = [
            c.model_dump(mode="json")
            for c in self._chains.values()
            if c.id not in seed_ids
        ]
        self._custom_file.parent.mkdir(parents=True, exist_ok=True)
        self._custom_file.write_text(
            json.dumps(custom, indent=2, default=str), encoding="utf-8"
        )

    def ensure_loaded(self) -> None:
        """Ensure seeds are loaded; call this before any query."""
        if not self._loaded:
            self.load_seeds()

    # -- Query API ----------------------------------------------------------

    def get(self, chain_id: str) -> Optional[ActivityChain]:
        """Get a chain by ID."""
        self.ensure_loaded()
        return self._chains.get(chain_id)

    def list_all(self) -> list[ActivityChain]:
        """Return all chains."""
        self.ensure_loaded()
        return list(self._chains.values())

    def filter(
        self,
        category: Optional[str] = None,
        corridor: Optional[str] = None,
        difficulty: Optional[str] = None,
        search: Optional[str] = None,
    ) -> list[ActivityChain]:
        """Filter chains by criteria."""
        self.ensure_loaded()
        results = list(self._chains.values())

        if category:
            results = [c for c in results if c.category == category]
        if corridor:
            results = [c for c in results if corridor in c.corridors]
        if difficulty:
            results = [c for c in results if c.difficulty == difficulty]
        if search:
            q = search.lower()
            results = [
                c for c in results
                if q in c.name.lower()
                or q in c.chain_context.lower()
                or q in c.emergent_risk.lower()
                or any(q in s.description.lower() for s in c.steps)
            ]

        return results

    def categories(self) -> dict[str, int]:
        """Return category names with chain counts."""
        self.ensure_loaded()
        cats: dict[str, int] = {}
        for c in self._chains.values():
            cats[c.category] = cats.get(c.category, 0) + 1
        return cats

    def count(self) -> int:
        """Total number of chains."""
        self.ensure_loaded()
        return len(self._chains)

    # -- Mutation API -------------------------------------------------------

    def add(self, chain: ActivityChain) -> None:
        """Add or update a chain and persist."""
        self.ensure_loaded()
        self._chains[chain.id] = chain
        self._save_custom_chains()

    def remove(self, chain_id: str) -> bool:
        """Remove a chain by ID. Returns True if found and removed."""
        self.ensure_loaded()
        if chain_id in self._chains:
            del self._chains[chain_id]
            self._save_custom_chains()
            return True
        return False
