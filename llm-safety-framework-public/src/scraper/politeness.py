"""
Politeness layer: per-domain rate limiting and robots.txt enforcement.

Ensures the scraper respects crawl delays and disallow rules.
"""

import asyncio
import logging
import random
import time
from collections import defaultdict
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import httpx

logger = logging.getLogger(__name__)


class PolitenessPolicy:
    """Enforces crawling politeness per robots.txt and configurable per-domain delays."""

    DEFAULT_DELAY: float = 2.0  # seconds between requests to the same domain

    # Domains that deserve extra politeness (glob-style, matched by suffix)
    DOMAIN_DELAYS: Dict[str, float] = {
        ".gov.ph": 3.0,
        ".gov.sg": 3.0,
        ".gov.hk": 3.0,
        ".go.id": 3.0,
        ".gov.qa": 3.0,
        ".gov.sa": 3.0,
        ".gov.ae": 3.0,
        ".ilo.org": 2.5,
        ".iom.int": 2.5,
        ".unodc.org": 2.5,
        ".ohchr.org": 2.5,
    }

    ROBOTS_CACHE_TTL = 86400  # 24 hours

    def __init__(
        self,
        user_agent: str = "LLMSafetyResearchBot/1.0",
        default_delay: Optional[float] = None,
        domain_delays: Optional[Dict[str, float]] = None,
        respect_robots: bool = True,
    ):
        self.user_agent = user_agent
        self.default_delay = default_delay if default_delay is not None else self.DEFAULT_DELAY
        self._domain_delays = {**self.DOMAIN_DELAYS, **(domain_delays or {})}
        self.respect_robots = respect_robots

        self._robots_cache: Dict[str, tuple] = {}  # domain -> (RobotFileParser, timestamp)
        self._last_request: Dict[str, float] = defaultdict(float)
        self._lock = asyncio.Lock()

    # -- robots.txt ---------------------------------------------------------------

    async def check_robots(self, url: str) -> bool:
        """Return True if robots.txt allows fetching *url*."""
        if not self.respect_robots:
            return True
        parsed = urlparse(url)
        domain = parsed.netloc
        rp = await self._get_robots(domain, f"{parsed.scheme}://{domain}")
        if rp is None:
            return True  # no robots.txt found → allowed
        return rp.can_fetch(self.user_agent, url)

    async def _get_robots(self, domain: str, origin: str) -> Optional[RobotFileParser]:
        """Fetch and cache robots.txt for a domain."""
        now = time.time()
        if domain in self._robots_cache:
            rp, ts = self._robots_cache[domain]
            if now - ts < self.ROBOTS_CACHE_TTL:
                return rp

        robots_url = f"{origin}/robots.txt"
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                resp = await client.get(robots_url, follow_redirects=True)
            if resp.status_code == 200:
                rp = RobotFileParser()
                rp.parse(resp.text.splitlines())
                self._robots_cache[domain] = (rp, now)
                return rp
            else:
                self._robots_cache[domain] = (None, now)
                return None
        except Exception:
            logger.debug("Failed to fetch robots.txt for %s", domain)
            self._robots_cache[domain] = (None, now)
            return None

    # -- rate limiting ------------------------------------------------------------

    async def wait_for_domain(
        self, url: str, jitter: Optional[Tuple[float, float]] = None,
    ) -> None:
        """Sleep until the per-domain delay has elapsed since the last request.

        Args:
            url: The target URL (domain is extracted).
            jitter: Optional ``(min, max)`` seconds of random delay to add,
                    making timing patterns harder to detect.
        """
        domain = urlparse(url).netloc
        delay = self.get_delay(domain)
        if jitter:
            delay += random.uniform(jitter[0], jitter[1])
        async with self._lock:
            elapsed = time.time() - self._last_request[domain]
            if elapsed < delay:
                await asyncio.sleep(delay - elapsed)
            self._last_request[domain] = time.time()

    def get_delay(self, domain: str) -> float:
        """Look up the delay for a domain, falling back to default."""
        for suffix, delay in self._domain_delays.items():
            if domain.endswith(suffix):
                return delay
        return self.default_delay

    # -- diagnostics --------------------------------------------------------------

    def get_config(self) -> dict:
        """Return current politeness configuration."""
        return {
            "default_delay": self.default_delay,
            "domain_delays": dict(self._domain_delays),
            "respect_robots": self.respect_robots,
            "robots_cache_ttl": self.ROBOTS_CACHE_TTL,
            "cached_domains": list(self._robots_cache.keys()),
        }
