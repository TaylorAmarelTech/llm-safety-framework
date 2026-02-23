"""
Source health tracking for the Document Intelligence Agent.

Records per-source fetch outcomes (success/failure, stealth level used,
status codes) and provides recommendations for stealth level upgrades.

Persists to ``data/scraper/source_health.json``.
"""

import json
import logging
import math
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional

logger = logging.getLogger(__name__)


@dataclass
class SourceHealth:
    """Health statistics for a single scraping source."""

    source_id: str
    total_fetches: int = 0
    successes: int = 0
    failures: int = 0
    last_success: Optional[str] = None
    last_failure: Optional[str] = None
    last_status_code: Optional[int] = None
    consecutive_failures: int = 0
    stealth_levels_used: list = field(default_factory=list)  # last N levels
    escalation_count: int = 0

    @property
    def success_rate(self) -> float:
        if self.total_fetches == 0:
            return 1.0
        return self.successes / self.total_fetches

    @property
    def avg_stealth_level(self) -> float:
        if not self.stealth_levels_used:
            return 0.0
        return sum(self.stealth_levels_used) / len(self.stealth_levels_used)


class HealthTracker:
    """Per-source health tracking with persistence.

    Records fetch outcomes and provides stealth level recommendations.
    """

    MAX_HISTORY = 50  # keep last N stealth levels per source

    def __init__(self, data_dir: str = "data/scraper"):
        self._data_dir = Path(data_dir)
        self._health_path = self._data_dir / "source_health.json"
        self._sources: Dict[str, SourceHealth] = {}
        self._load()

    def _load(self) -> None:
        if self._health_path.exists():
            try:
                data = json.loads(self._health_path.read_text(encoding="utf-8"))
                for sid, raw in data.items():
                    self._sources[sid] = SourceHealth(**raw)
            except (json.JSONDecodeError, OSError, TypeError) as exc:
                logger.warning("Failed to load source health: %s", exc)

    def save(self) -> None:
        self._data_dir.mkdir(parents=True, exist_ok=True)
        data = {sid: asdict(h) for sid, h in self._sources.items()}
        self._health_path.write_text(
            json.dumps(data, indent=2, default=str), encoding="utf-8"
        )

    def _ensure(self, source_id: str) -> SourceHealth:
        if source_id not in self._sources:
            self._sources[source_id] = SourceHealth(source_id=source_id)
        return self._sources[source_id]

    def record_success(self, source_id: str, stealth_level_used: int = 0) -> None:
        """Record a successful fetch for a source."""
        h = self._ensure(source_id)
        h.total_fetches += 1
        h.successes += 1
        h.consecutive_failures = 0
        h.last_success = datetime.now(tz=timezone.utc).isoformat()
        h.last_status_code = 200
        h.stealth_levels_used.append(stealth_level_used)
        if len(h.stealth_levels_used) > self.MAX_HISTORY:
            h.stealth_levels_used = h.stealth_levels_used[-self.MAX_HISTORY:]
        self.save()

    def record_failure(
        self, source_id: str, status_code: int = 0, stealth_level_used: int = 0
    ) -> None:
        """Record a failed fetch for a source."""
        h = self._ensure(source_id)
        h.total_fetches += 1
        h.failures += 1
        h.consecutive_failures += 1
        h.last_failure = datetime.now(tz=timezone.utc).isoformat()
        h.last_status_code = status_code
        h.stealth_levels_used.append(stealth_level_used)
        if len(h.stealth_levels_used) > self.MAX_HISTORY:
            h.stealth_levels_used = h.stealth_levels_used[-self.MAX_HISTORY:]
        self.save()

    def record_escalation(self, source_id: str) -> None:
        """Record that a source required stealth escalation."""
        h = self._ensure(source_id)
        h.escalation_count += 1

    def get_health(self, source_id: str) -> SourceHealth:
        return self._ensure(source_id)

    def get_all(self) -> Dict[str, SourceHealth]:
        return dict(self._sources)

    def get_recommended_stealth(self, source_id: str) -> int:
        """Recommend a stealth level based on history.

        Uses ceiling of average stealth level from recent fetches.
        Sources with >50% failure rate get bumped up by 1.
        """
        h = self._sources.get(source_id)
        if not h or not h.stealth_levels_used:
            return 0
        avg = h.avg_stealth_level
        recommended = math.ceil(avg)
        if h.success_rate < 0.5 and recommended < 4:
            recommended += 1
        return min(recommended, 4)

    def summary(self) -> list[dict]:
        """Get health summary for all tracked sources."""
        result = []
        for sid, h in sorted(self._sources.items()):
            result.append({
                "source_id": sid,
                "total_fetches": h.total_fetches,
                "success_rate": round(h.success_rate, 3),
                "consecutive_failures": h.consecutive_failures,
                "last_success": h.last_success,
                "last_failure": h.last_failure,
                "avg_stealth_level": round(h.avg_stealth_level, 1),
                "escalation_count": h.escalation_count,
                "recommended_stealth": self.get_recommended_stealth(sid),
            })
        return result
