"""
Seed loader — merges pre-built facts into the Knowledge Base.

Idempotent: running multiple times does not create duplicates.
Facts are identified by content hash (same dedup logic as KB rebuild).
"""

import json
import logging
from datetime import datetime, timezone
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .knowledge_base import KnowledgeBase

from .seeds import SEED_FACTS
from .seed_pruner import load_pruned_seeds

logger = logging.getLogger(__name__)


def is_seeded(kb: "KnowledgeBase") -> bool:
    """Check whether the KB already contains seed facts."""
    for fact in kb._facts:
        if fact.get("_source_doc") == "seed":
            return True
    return False


def load_seeds(kb: "KnowledgeBase", *, pruned: bool = True) -> int:
    """Merge seed facts into the KB.

    Args:
        kb: The KnowledgeBase instance.
        pruned: If True (default), use the normalized/deduplicated seed set.
                If False, use the raw SEED_FACTS archive.

    Each fact gets metadata:
    - ``_source_doc``: ``"seed"``
    - ``_first_seen``: current timestamp
    - ``_last_confirmed``: current timestamp
    - ``_confidence``: ``1.0`` (hand-curated, authoritative)

    Returns:
        Number of NEW facts added (0 if already seeded with same data).
    """
    facts_source = load_pruned_seeds() if pruned else SEED_FACTS
    now = datetime.now(tz=timezone.utc).isoformat()

    # Build dedup map from existing KB facts (same logic as KB rebuild)
    existing_keys: dict[str, int] = {}
    for idx, f in enumerate(kb._facts):
        key = json.dumps(
            {k: v for k, v in f.items() if not k.startswith("_")},
            sort_keys=True, default=str,
        )
        existing_keys[key] = idx

    added = 0
    for fact in facts_source:
        key = json.dumps(
            {k: v for k, v in fact.items() if not k.startswith("_")},
            sort_keys=True, default=str,
        )
        if key in existing_keys:
            # Already present — just update last_confirmed
            kb._facts[existing_keys[key]]["_last_confirmed"] = now
            continue

        enriched = dict(fact)
        enriched["_source_doc"] = "seed"
        enriched["_first_seen"] = now
        enriched["_last_confirmed"] = now
        enriched["_confidence"] = 1.0

        existing_keys[key] = len(kb._facts)
        kb._facts.append(enriched)
        added += 1

    if added > 0:
        kb._meta["last_rebuilt"] = now
        kb._save()
        logger.info("Loaded %d seed facts into KB (total: %d)", added, len(kb._facts))
    else:
        logger.debug("KB already contains all seed facts")

    return added
