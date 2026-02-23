"""
Proxy rotation for the Document Intelligence Agent.

Manages a user-supplied proxy list with round-robin, random, or
least-failures selection and per-proxy health tracking.
"""

import itertools
import logging
import random
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass
class ProxyHealth:
    """Health tracking for a single proxy."""

    url: str
    successes: int = 0
    failures: int = 0
    last_used: float = 0.0
    last_failure: Optional[float] = None
    avg_latency_ms: float = 0.0

    @property
    def failure_rate(self) -> float:
        total = self.successes + self.failures
        return self.failures / total if total > 0 else 0.0


class ProxyRotator:
    """Manages a list of proxies with rotation and health tracking."""

    def __init__(
        self,
        proxies: Optional[List[str]] = None,
        rotation: str = "round_robin",
        cooldown_after_failure: float = 60.0,
    ):
        self._proxies: List[str] = list(proxies or [])
        self._rotation = rotation
        self._cooldown = cooldown_after_failure
        self._health: Dict[str, ProxyHealth] = {
            p: ProxyHealth(url=p) for p in self._proxies
        }
        self._cycle = itertools.cycle(self._proxies) if self._proxies else None

    def get_next(self) -> Optional[str]:
        """Return the next proxy URL, or None if no proxies configured."""
        if not self._proxies:
            return None

        now = time.time()

        if self._rotation == "random":
            candidates = [
                p for p in self._proxies
                if not self._health[p].last_failure
                or (now - self._health[p].last_failure) > self._cooldown
            ]
            if not candidates:
                candidates = self._proxies
            return random.choice(candidates)

        if self._rotation == "least_failures":
            return min(self._proxies, key=lambda p: self._health[p].failure_rate)

        # round_robin (default)
        if self._cycle is None:
            return None
        return next(self._cycle)

    def report_success(self, proxy_url: str, latency_ms: float = 0) -> None:
        if proxy_url in self._health:
            h = self._health[proxy_url]
            h.successes += 1
            h.last_used = time.time()
            if latency_ms > 0:
                prev_total = h.successes + h.failures - 1
                if prev_total > 0:
                    h.avg_latency_ms = (h.avg_latency_ms * prev_total + latency_ms) / (prev_total + 1)
                else:
                    h.avg_latency_ms = latency_ms

    def report_failure(self, proxy_url: str) -> None:
        if proxy_url in self._health:
            h = self._health[proxy_url]
            h.failures += 1
            h.last_failure = time.time()

    def add_proxy(self, url: str) -> None:
        if url not in self._health:
            self._proxies.append(url)
            self._health[url] = ProxyHealth(url=url)
            self._cycle = itertools.cycle(self._proxies)

    def remove_proxy(self, url: str) -> None:
        if url in self._health:
            self._proxies.remove(url)
            del self._health[url]
            self._cycle = itertools.cycle(self._proxies) if self._proxies else None

    def get_health(self) -> List[dict]:
        return [
            {
                "url": h.url,
                "successes": h.successes,
                "failures": h.failures,
                "failure_rate": round(h.failure_rate, 3),
                "avg_latency_ms": round(h.avg_latency_ms, 1),
                "last_used": h.last_used,
            }
            for h in self._health.values()
        ]

    @property
    def count(self) -> int:
        return len(self._proxies)
