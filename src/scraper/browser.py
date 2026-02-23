"""
Headless browser support via Playwright for JS-rendered pages.

Provides a singleton Chromium instance that can render dynamic pages.
Falls back gracefully if Playwright is not installed.

When a StealthProfile is supplied, applies:
- playwright-stealth patches (removes navigator.webdriver, etc.)
- Viewport randomization from common desktop resolutions
- Locale / timezone randomization via browser-context options
- Anti-automation Chromium flags
"""

import asyncio
import logging
import random
from typing import Optional

logger = logging.getLogger(__name__)

try:
    from playwright.async_api import async_playwright, Browser, Page
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

try:
    from playwright_stealth.stealth import Stealth as _StealthPatcher  # type: ignore[import-untyped]
    STEALTH_PATCH_AVAILABLE = True
except ImportError:
    _StealthPatcher = None  # type: ignore[assignment,misc]
    STEALTH_PATCH_AVAILABLE = False

# Sentinel for the shared browser + playwright context
_playwright_ctx = None
_browser: Optional["Browser"] = None
_lock = asyncio.Lock()

# Anti-detection Chromium launch args
_STEALTH_ARGS = [
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-blink-features=AutomationControlled",
    "--disable-features=IsolateOrigins,site-per-process",
    "--disable-infobars",
]

# Viewport pool for randomization
_VIEWPORTS = [
    {"width": 1280, "height": 720},
    {"width": 1366, "height": 768},
    {"width": 1440, "height": 900},
    {"width": 1536, "height": 864},
    {"width": 1920, "height": 1080},
]

_LOCALES = ["en-US", "en-GB", "en-AU", "en-CA"]

_TIMEZONES = [
    "America/New_York", "America/Chicago", "America/Los_Angeles",
    "Europe/London", "Asia/Singapore", "Asia/Hong_Kong",
]

# Default realistic UA (no bot identifier)
_DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


async def _ensure_browser() -> "Browser":
    """Lazy-init a headless Chromium browser (reused across calls)."""
    global _playwright_ctx, _browser
    if not PLAYWRIGHT_AVAILABLE:
        raise RuntimeError(
            "Playwright is not installed. Run: pip install playwright && playwright install chromium"
        )
    async with _lock:
        if _browser is None or not _browser.is_connected():
            _playwright_ctx = await async_playwright().start()
            _browser = await _playwright_ctx.chromium.launch(
                headless=True,
                args=_STEALTH_ARGS,
            )
            logger.info("Playwright Chromium browser launched (stealth args enabled)")
    return _browser


async def close_browser() -> None:
    """Shut down the shared browser and Playwright context."""
    global _playwright_ctx, _browser
    async with _lock:
        if _browser and _browser.is_connected():
            await _browser.close()
            _browser = None
        if _playwright_ctx:
            await _playwright_ctx.stop()
            _playwright_ctx = None
            logger.info("Playwright browser closed")


class HeadlessBrowser:
    """Render JS-heavy pages using a shared Chromium instance.

    Accepts an optional ``stealth_profile`` on ``render_page`` to enable
    anti-detection patches, viewport randomization, and locale spoofing.
    """

    async def _new_page(self, stealth_profile=None):
        """Create a new page with optional stealth context settings."""
        browser = await _ensure_browser()

        # Build context options
        ctx_opts: dict = {"user_agent": _DEFAULT_UA}

        if stealth_profile is not None:
            if stealth_profile.viewport_randomize:
                ctx_opts["viewport"] = random.choice(_VIEWPORTS)
            if stealth_profile.locale_randomize:
                ctx_opts["locale"] = random.choice(_LOCALES)
            tz = stealth_profile.timezone_spoof
            if tz:
                ctx_opts["timezone_id"] = tz
            elif stealth_profile.locale_randomize:
                ctx_opts["timezone_id"] = random.choice(_TIMEZONES)

        context = await browser.new_context(**ctx_opts)
        page = await context.new_page()

        # Apply playwright-stealth patches if available and stealth requested
        if stealth_profile is not None and STEALTH_PATCH_AVAILABLE and _StealthPatcher:
            try:
                patcher = _StealthPatcher()
                await patcher.apply_stealth_async(page)
            except Exception as exc:
                logger.debug("playwright-stealth patch failed: %s", exc)

        return page, context

    async def render_page(
        self,
        url: str,
        wait_selector: Optional[str] = None,
        timeout: float = 30000,
        scroll: bool = False,
        stealth_profile=None,
    ) -> str:
        """Navigate to *url*, wait for JS, return rendered HTML.

        Args:
            url: Full URL to render.
            wait_selector: Optional CSS selector to wait for before returning.
            timeout: Max wait time in milliseconds.
            scroll: If True, scroll to bottom to trigger lazy-load content.
            stealth_profile: Optional StealthProfile for anti-detection.

        Returns:
            Fully rendered page HTML.
        """
        page, context = await self._new_page(stealth_profile)
        try:
            await page.goto(url, wait_until="networkidle", timeout=timeout)
            if wait_selector:
                await page.wait_for_selector(wait_selector, timeout=timeout)
            if scroll:
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await page.wait_for_timeout(1500)  # let lazy content load
            html = await page.content()
            return html
        finally:
            await page.close()
            await context.close()

    async def render_and_screenshot(
        self, url: str, screenshot_path: str, timeout: float = 30000,
        stealth_profile=None,
    ) -> str:
        """Render page, save a screenshot, and return HTML."""
        page, context = await self._new_page(stealth_profile)
        try:
            await page.goto(url, wait_until="networkidle", timeout=timeout)
            await page.screenshot(path=screenshot_path, full_page=True)
            return await page.content()
        finally:
            await page.close()
            await context.close()

    @staticmethod
    def is_available() -> bool:
        """Check whether Playwright + Chromium are usable."""
        return PLAYWRIGHT_AVAILABLE

    @staticmethod
    async def status() -> dict:
        """Return diagnostic info about the browser backend."""
        info: dict = {
            "playwright_installed": PLAYWRIGHT_AVAILABLE,
            "browser_connected": False,
            "stealth_available": STEALTH_PATCH_AVAILABLE,
        }
        if PLAYWRIGHT_AVAILABLE and _browser is not None:
            info["browser_connected"] = _browser.is_connected()
        return info
