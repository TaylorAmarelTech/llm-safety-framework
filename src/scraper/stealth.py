"""
Stealth configuration for the Document Intelligence Agent.

Bundles all anti-detection settings into a single profile that
flows through the fetch chain.  Each StealthLevel escalates the
anti-detection measures used:

    NONE     → raw httpx with research-bot UA
    BASIC    → realistic UA + full browser headers + jitter + cookies
    MODERATE → curl_cffi TLS fingerprint spoofing + proxy rotation
    FULL     → playwright-stealth (patched browser, viewport randomization)
    MAXIMUM  → nodriver (CDP direct, no ChromeDriver)
"""

import enum
import random
from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# Stealth level enum
# ---------------------------------------------------------------------------

class StealthLevel(enum.IntEnum):
    NONE = 0
    BASIC = 1
    MODERATE = 2
    FULL = 3
    MAXIMUM = 4


STEALTH_LABELS: Dict[int, str] = {
    0: "None",
    1: "Basic",
    2: "Moderate",
    3: "Full",
    4: "Maximum",
}


# ---------------------------------------------------------------------------
# Stealth profile
# ---------------------------------------------------------------------------

@dataclass
class StealthProfile:
    """Configuration bundle for all anti-detection behaviors."""

    level: StealthLevel = StealthLevel.NONE

    # User-Agent rotation
    rotate_ua: bool = False
    ua_browser: str = "chrome"
    ua_platform: str = "windows"

    # Header spoofing
    realistic_headers: bool = False

    # Timing jitter
    jitter_enabled: bool = False
    jitter_min: float = 0.5
    jitter_max: float = 2.5

    # TLS fingerprint (curl_cffi)
    tls_impersonate: Optional[str] = None

    # Cookie persistence
    persist_cookies: bool = False

    # Proxy
    proxy_enabled: bool = False
    proxy_list: List[str] = field(default_factory=list)
    proxy_rotation: str = "round_robin"

    # Browser-level (Playwright)
    viewport_randomize: bool = False
    locale_randomize: bool = False
    timezone_spoof: Optional[str] = None

    @classmethod
    def from_level(cls, level: StealthLevel) -> "StealthProfile":
        """Build a profile with sensible defaults for the given level."""
        if level == StealthLevel.NONE:
            return cls(level=level)
        if level == StealthLevel.BASIC:
            return cls(
                level=level, rotate_ua=True, realistic_headers=True,
                jitter_enabled=True, persist_cookies=True,
            )
        if level == StealthLevel.MODERATE:
            return cls(
                level=level, rotate_ua=True, realistic_headers=True,
                jitter_enabled=True, persist_cookies=True,
                tls_impersonate="chrome120",
            )
        if level == StealthLevel.FULL:
            return cls(
                level=level, rotate_ua=True, realistic_headers=True,
                jitter_enabled=True, persist_cookies=True,
                tls_impersonate="chrome120",
                viewport_randomize=True, locale_randomize=True,
            )
        # MAXIMUM
        return cls(
            level=level, rotate_ua=True, realistic_headers=True,
            jitter_enabled=True, persist_cookies=True,
            tls_impersonate="chrome120",
            viewport_randomize=True, locale_randomize=True,
        )

    def to_dict(self) -> dict:
        d = asdict(self)
        d["level"] = int(self.level)
        return d

    @classmethod
    def from_dict(cls, data: dict) -> "StealthProfile":
        data = dict(data)
        data["level"] = StealthLevel(data.get("level", 0))
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


# ---------------------------------------------------------------------------
# Realistic header builder
# ---------------------------------------------------------------------------

class HeaderBuilder:
    """Build browser-like request headers that match a real Chrome/Firefox session."""

    CHROME_HEADERS: Dict[str, str] = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Ch-Ua": '"Chromium";v="120", "Google Chrome";v="120", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
    }

    FIREFOX_HEADERS: Dict[str, str] = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    }

    @classmethod
    def build(cls, ua_string: str, browser_type: str = "chrome") -> Dict[str, str]:
        base = dict(cls.CHROME_HEADERS if browser_type == "chrome" else cls.FIREFOX_HEADERS)
        base["User-Agent"] = ua_string
        return base


# ---------------------------------------------------------------------------
# User-agent rotator
# ---------------------------------------------------------------------------

class UARotator:
    """Rotate user-agent strings.  Uses ``fake-useragent`` when installed,
    falls back to a built-in list of 10 real Chrome UAs."""

    _FALLBACK_CHROME = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    ]

    _FALLBACK_FIREFOX = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0",
    ]

    def __init__(self, browser: str = "chrome", platform: str = "windows"):
        self._browser = browser
        self._platform = platform
        self._fake_ua = None
        try:
            from fake_useragent import UserAgent
            self._fake_ua = UserAgent(browsers=[browser], os=[platform])
        except Exception:
            pass

    def get(self) -> str:
        if self._fake_ua:
            try:
                return self._fake_ua.random
            except Exception:
                pass
        fallbacks = self._FALLBACK_CHROME if self._browser == "chrome" else self._FALLBACK_FIREFOX
        return random.choice(fallbacks)

    @property
    def has_fake_useragent(self) -> bool:
        return self._fake_ua is not None
