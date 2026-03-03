"""
Document fetcher for the Document Intelligence Agent.

Downloads HTML pages and PDF documents, extracts text, discovers
linked documents via CSS selectors, and deduplicates by content hash.

Integrates with PolitenessPolicy, RetryPolicy, ChangeDetector,
HeadlessBrowser, and the tiered StealthProfile for robust, polite,
and — when needed — undetectable scraping.
"""

import hashlib
import json
import logging
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse

import httpx

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None  # type: ignore[assignment,misc]

try:
    import pdfplumber
except ImportError:
    pdfplumber = None  # type: ignore[assignment]

try:
    from curl_cffi.requests import AsyncSession as CurlAsyncSession
    CURL_CFFI_AVAILABLE = True
except ImportError:
    CurlAsyncSession = None  # type: ignore[assignment,misc]
    CURL_CFFI_AVAILABLE = False

from .browser import HeadlessBrowser
from .change_detection import ChangeDetector
from .document_identity import DocumentIndex, content_id as compute_content_id, canonical_url
from .feed_parser import FeedParser
from .politeness import PolitenessPolicy
from .proxy import ProxyRotator
from .retry import RetryPolicy, RetryableError
from .stealth import HeaderBuilder, StealthLevel, StealthProfile, UARotator

# HTTP status codes that trigger auto-escalation
_ESCALATION_STATUSES = {403, 429, 503}

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Document dataclass
# ---------------------------------------------------------------------------

@dataclass
class Document:
    """A fetched document with extracted text."""

    id: str
    url: str
    title: str
    text: str
    content_type: str  # html | pdf
    fetched_at: str
    source_id: str
    content_hash: str
    word_count: int = 0
    etag: Optional[str] = None
    last_modified: Optional[str] = None
    language: str = "en"
    page_count: Optional[int] = None


# ---------------------------------------------------------------------------
# Main fetcher
# ---------------------------------------------------------------------------

class DocumentFetcher:
    """Fetches web pages and PDFs, extracts text and links.

    Optional integrations (auto-constructed if not supplied):
    - PolitenessPolicy: per-domain rate limiting + robots.txt
    - RetryPolicy: exponential backoff on transient failures
    - ChangeDetector: ETag / content-hash fingerprinting
    - HeadlessBrowser: Playwright for JS-rendered pages
    - FeedParser: RSS/Atom/Sitemap discovery
    - StealthProfile: tiered anti-detection (Levels 0-4)
    - ProxyRotator: round-robin / random proxy selection
    """

    # Fallback UA used only at StealthLevel.NONE
    BOT_USER_AGENT = (
        "MigrantWorkerSafetyResearchBot/1.0 "
        "(+https://github.com/tayloramarel/llm-safety-framework; "
        "research purposes only)"
    )

    def __init__(
        self,
        data_dir: str = "data/scraper",
        politeness: Optional[PolitenessPolicy] = None,
        retry_policy: Optional[RetryPolicy] = None,
        change_detector: Optional[ChangeDetector] = None,
        browser: Optional[HeadlessBrowser] = None,
        feed_parser: Optional[FeedParser] = None,
        respect_robots: bool = True,
        stealth: Optional[StealthProfile] = None,
        proxy_rotator: Optional[ProxyRotator] = None,
    ):
        self.data_dir = Path(data_dir)
        self.docs_dir = self.data_dir / "documents"
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        self._known_hashes = self._load_known_hashes()
        self.doc_index = DocumentIndex(data_dir=data_dir)

        # Stealth & proxy
        self.stealth = stealth or StealthProfile()
        self.proxy_rotator = proxy_rotator or ProxyRotator()
        self._ua_rotator: Optional[UARotator] = (
            UARotator(browser=self.stealth.ua_browser, platform=self.stealth.ua_platform)
            if self.stealth.rotate_ua else None
        )
        self._cookie_jars: Dict[str, httpx.Cookies] = {}

        # Other integrations
        ua_for_robots = self._get_user_agent()
        self.politeness = politeness or PolitenessPolicy(
            user_agent=ua_for_robots, respect_robots=respect_robots
        )
        self.retry_policy = retry_policy or RetryPolicy()
        self.change_detector = change_detector or ChangeDetector(data_dir=data_dir)
        self.browser = browser or HeadlessBrowser()
        self.feed_parser = feed_parser or FeedParser()

    # -- stealth helpers -------------------------------------------------------

    def _get_user_agent(self) -> str:
        if self._ua_rotator:
            return self._ua_rotator.get()
        return self.BOT_USER_AGENT

    def _build_headers(self, url: str) -> Dict[str, str]:
        ua = self._get_user_agent()
        if self.stealth.realistic_headers:
            headers = HeaderBuilder.build(ua, self.stealth.ua_browser)
        else:
            headers = {"User-Agent": ua}
        headers.update(self.change_detector.get_conditional_headers(url))
        return headers

    def _get_jitter(self) -> Optional[Tuple[float, float]]:
        if self.stealth.jitter_enabled:
            return (self.stealth.jitter_min, self.stealth.jitter_max)
        return None

    def _get_proxy(self) -> Optional[str]:
        if self.stealth.proxy_enabled and self.proxy_rotator.count > 0:
            return self.proxy_rotator.get_next()
        return None

    # -- hash index for dedup --------------------------------------------------

    def _load_known_hashes(self) -> set:
        hashes = set()
        for fp in self.docs_dir.glob("*.json"):
            try:
                data = json.loads(fp.read_text(encoding="utf-8"))
                if "content_hash" in data:
                    hashes.add(data["content_hash"])
            except Exception:
                continue
        return hashes

    def is_duplicate(self, content: str) -> bool:
        h = hashlib.sha256(content.encode("utf-8")).hexdigest()
        return h in self._known_hashes

    # -- tiered fetch methods --------------------------------------------------

    async def _fetch_httpx(
        self, url: str, headers: Dict[str, str], proxy: Optional[str],
        timeout: float, binary: bool = False,
    ) -> tuple:
        """Standard httpx fetch with optional proxy and cookie persistence."""
        domain = urlparse(url).netloc
        cookies = self._cookie_jars.get(domain) if self.stealth.persist_cookies else None

        async def _do() -> tuple:
            async with httpx.AsyncClient(
                timeout=timeout, follow_redirects=True, headers=headers,
                proxy=proxy, cookies=cookies,
            ) as client:
                resp = await client.get(url)
                if self.stealth.persist_cookies:
                    self._cookie_jars.setdefault(domain, httpx.Cookies())
                    self._cookie_jars[domain].update(resp.cookies)
                if resp.status_code == 304:
                    return (b"" if binary else ""), dict(resp.headers)
                if self.retry_policy.is_retryable_status(resp.status_code):
                    raise RetryableError(
                        f"HTTP {resp.status_code}", status_code=resp.status_code
                    )
                resp.raise_for_status()
                return (resp.content if binary else resp.text), dict(resp.headers)

        return await self.retry_policy.execute(_do)

    async def _fetch_curl_cffi(
        self, url: str, headers: Dict[str, str], proxy: Optional[str],
        timeout: float, binary: bool = False,
    ) -> tuple:
        """TLS-fingerprint-spoofing fetch via curl_cffi."""
        if not CURL_CFFI_AVAILABLE:
            raise ImportError("curl_cffi not installed")

        impersonate = self.stealth.tls_impersonate or "chrome120"
        async with CurlAsyncSession(impersonate=impersonate) as s:
            kwargs = dict(headers=headers, timeout=timeout, allow_redirects=True)
            if proxy:
                kwargs["proxy"] = proxy
            resp = await s.get(url, **kwargs)
            if resp.status_code == 304:
                return (b"" if binary else ""), dict(resp.headers)
            if self.retry_policy.is_retryable_status(resp.status_code):
                raise RetryableError(
                    f"HTTP {resp.status_code}", status_code=resp.status_code
                )
            resp.raise_for_status()
            return (resp.content if binary else resp.text), dict(resp.headers)

    async def _fetch_playwright_stealth(self, url: str, timeout: float) -> tuple:
        """Playwright with stealth patches and viewport randomization."""
        if not self.browser.is_available():
            raise RuntimeError("Playwright not available")
        html = await self.browser.render_page(
            url, timeout=timeout * 1000, stealth_profile=self.stealth,
        )
        return html, {}

    async def _fetch_nodriver(self, url: str, timeout: float) -> tuple:
        """nodriver (CDP direct) for maximum anti-detection."""
        try:
            import nodriver as uc
        except ImportError:
            raise ImportError("nodriver not installed")
        browser = await uc.start(headless=True)
        try:
            page = await browser.get(url)
            await page.sleep(2)
            html = await page.get_content()
            return html, {}
        finally:
            browser.stop()

    async def _fetch_with_escalation(
        self, url: str, timeout: float, binary: bool = False,
    ) -> tuple:
        """Try lightweight methods first, escalate on anti-bot blocks.

        Fallback chain: httpx → curl_cffi → playwright-stealth → nodriver
        Only tiers at or below ``self.stealth.level`` are attempted.
        """
        headers = self._build_headers(url)
        proxy = self._get_proxy()
        level = self.stealth.level

        # Level 0-1: httpx only
        if level <= StealthLevel.BASIC:
            return await self._fetch_httpx(url, headers, proxy, timeout, binary)

        # Level 2: try curl_cffi, fall back to httpx
        if level == StealthLevel.MODERATE:
            try:
                return await self._fetch_curl_cffi(url, headers, proxy, timeout, binary)
            except (ImportError, Exception) as exc:
                logger.info("curl_cffi failed for %s (%s), falling back to httpx", url, exc)
                return await self._fetch_httpx(url, headers, proxy, timeout, binary)

        # Level 3: try playwright-stealth, fall back to curl_cffi, then httpx
        if level == StealthLevel.FULL:
            if not binary:
                try:
                    return await self._fetch_playwright_stealth(url, timeout)
                except Exception as exc:
                    logger.info("playwright-stealth failed for %s (%s)", url, exc)
            try:
                return await self._fetch_curl_cffi(url, headers, proxy, timeout, binary)
            except (ImportError, Exception) as exc:
                logger.info("curl_cffi failed for %s (%s)", url, exc)
            return await self._fetch_httpx(url, headers, proxy, timeout, binary)

        # Level 4 (MAXIMUM): try nodriver, fall back through the chain
        if not binary:
            try:
                return await self._fetch_nodriver(url, timeout)
            except (ImportError, Exception) as exc:
                logger.info("nodriver failed for %s (%s)", url, exc)
            try:
                return await self._fetch_playwright_stealth(url, timeout)
            except Exception as exc:
                logger.info("playwright-stealth failed for %s (%s)", url, exc)
        try:
            return await self._fetch_curl_cffi(url, headers, proxy, timeout, binary)
        except (ImportError, Exception) as exc:
            logger.info("curl_cffi failed for %s (%s)", url, exc)
        return await self._fetch_httpx(url, headers, proxy, timeout, binary)

    # -- auto-escalation on 403/429/503 ----------------------------------------

    async def _fetch_with_auto_escalation(
        self, url: str, timeout: float, binary: bool = False,
    ) -> tuple:
        """Wrap ``_fetch_with_escalation`` and auto-escalate stealth on block.

        On 403/429/503, temporarily bumps stealth level and retries with
        progressively stronger anti-detection methods.

        Returns:
            ``(content, headers, final_level, escalation_attempts)``
        """
        original_level = self.stealth.level
        attempts = 0

        for level_value in range(original_level, StealthLevel.MAXIMUM + 1):
            self.stealth.level = level_value
            # Rebuild UA rotator for new level if needed
            if level_value > StealthLevel.NONE and not self._ua_rotator:
                self._ua_rotator = UARotator()
            try:
                content, headers = await self._fetch_with_escalation(url, timeout, binary)
                if attempts > 0:
                    logger.info(
                        "Auto-escalation succeeded for %s at level %d (was %d)",
                        url, level_value, original_level,
                    )
                return content, headers, level_value, attempts
            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                if status in _ESCALATION_STATUSES and level_value < StealthLevel.MAXIMUM:
                    attempts += 1
                    logger.info(
                        "Escalating %s from L%d to L%d after HTTP %d",
                        url, level_value, level_value + 1, status,
                    )
                    continue
                # Non-escalatable error or max level reached
                raise
            finally:
                self.stealth.level = original_level

        # Should not reach here, but if it does, try one last time at max level
        self.stealth.level = original_level
        content, headers = await self._fetch_with_escalation(url, timeout, binary)
        return content, headers, original_level, attempts

    # -- page fetching ---------------------------------------------------------

    async def fetch_page(
        self,
        url: str,
        timeout: float = 30.0,
        use_browser: bool = False,
    ) -> tuple:
        """GET a URL and return ``(response_text, response_headers_dict)``.

        Pipeline: robots.txt check → per-domain delay (with jitter) →
        auto-escalation on 403/429/503.

        The returned tuple is ``(text, headers)`` for compatibility.
        Call ``fetch_page_ex()`` if you also need the stealth level used.

        Raises:
            PermissionError: If robots.txt disallows this URL.
        """
        text, headers, _level, _attempts = await self.fetch_page_ex(url, timeout, use_browser)
        return text, headers

    async def fetch_page_ex(
        self,
        url: str,
        timeout: float = 30.0,
        use_browser: bool = False,
    ) -> tuple:
        """Extended fetch returning ``(text, headers, stealth_level_used, escalation_attempts)``."""
        # 1. Robots.txt check
        if not await self.politeness.check_robots(url):
            raise PermissionError(f"robots.txt disallows fetching {url}")

        # 2. Per-domain rate limiting (with optional jitter)
        await self.politeness.wait_for_domain(url, jitter=self._get_jitter())

        # 3. Forced browser mode (bypasses tiered escalation)
        if use_browser and self.browser.is_available():
            html = await self.browser.render_page(
                url, timeout=timeout * 1000, stealth_profile=self.stealth,
            )
            return html, {}, self.stealth.level, 0

        # 4. Tiered fetch with auto-escalation on 403/429/503
        return await self._fetch_with_auto_escalation(url, timeout, binary=False)

    async def fetch_pdf_bytes(self, url: str, timeout: float = 60.0) -> tuple:
        """Download a PDF and return ``(raw_bytes, response_headers_dict)``."""
        if not await self.politeness.check_robots(url):
            raise PermissionError(f"robots.txt disallows fetching {url}")
        await self.politeness.wait_for_domain(url, jitter=self._get_jitter())
        content, headers, _level, _attempts = await self._fetch_with_auto_escalation(
            url, timeout, binary=True
        )
        return content, headers

    async def fetch_pdf_bytes_ex(self, url: str, timeout: float = 60.0) -> tuple:
        """Extended PDF fetch returning ``(bytes, headers, stealth_level_used, attempts)``."""
        if not await self.politeness.check_robots(url):
            raise PermissionError(f"robots.txt disallows fetching {url}")
        await self.politeness.wait_for_domain(url, jitter=self._get_jitter())
        return await self._fetch_with_auto_escalation(url, timeout, binary=True)

    # -- link extraction -------------------------------------------------------

    def extract_links(
        self, html: str, base_url: str, selectors: List[str]
    ) -> List[str]:
        """Extract document links from HTML using CSS selectors."""
        if BeautifulSoup is None:
            return []
        soup = BeautifulSoup(html, "html.parser")
        links: List[str] = []
        seen = set()

        for selector in selectors:
            try:
                for tag in soup.select(selector):
                    href = tag.get("href")
                    if not href:
                        continue
                    full = urljoin(base_url, href)
                    if full not in seen:
                        seen.add(full)
                        links.append(full)
            except Exception:
                continue

        # Also look for PDF links if not already captured
        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            if href.lower().endswith(".pdf"):
                full = urljoin(base_url, href)
                if full not in seen:
                    seen.add(full)
                    links.append(full)

        return links

    async def extract_links_with_fallback(
        self,
        html: str,
        base_url: str,
        selectors: List[str],
        feed_url: Optional[str] = None,
    ) -> List[str]:
        """Extract links via CSS selectors; fall back to sitemap/RSS if <5 found."""
        links = self.extract_links(html, base_url, selectors)

        if len(links) < 5:
            sitemap_urls = await self.feed_parser.fetch_and_parse_sitemap(base_url)
            for url in sitemap_urls:
                if url not in links:
                    links.append(url)
            logger.debug("Sitemap fallback added %d URLs from %s", len(sitemap_urls), base_url)

        if len(links) < 5 and feed_url:
            entries = await self.feed_parser.fetch_and_parse_feed(feed_url)
            for entry in entries:
                if entry.url not in links:
                    links.append(entry.url)
            logger.debug("Feed fallback added %d entries from %s", len(entries), feed_url)

        return links

    # -- text extraction -------------------------------------------------------

    def _extract_html_text(self, html: str) -> tuple:
        """Extract readable text and title from HTML."""
        if BeautifulSoup is None:
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text).strip()
            return text, "Untitled"

        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        title = soup.title.string.strip() if soup.title and soup.title.string else "Untitled"
        main = soup.find("main") or soup.find("article") or soup.find("div", class_="content")
        target = main if main else soup.body if soup.body else soup
        text = target.get_text(separator="\n", strip=True)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text, title

    def _extract_pdf_text(self, pdf_bytes: bytes) -> str:
        """Extract text from a PDF using pdfplumber."""
        if pdfplumber is None:
            return "[PDF text extraction unavailable — install pdfplumber]"
        import io
        pages_text = []
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    pages_text.append(t)
        return "\n\n".join(pages_text)

    # -- main fetch + store ----------------------------------------------------

    async def fetch_document(
        self,
        url: str,
        source_id: str,
        use_browser: bool = False,
        force_refetch: bool = False,
        language: str = "en",
    ) -> Optional[Document]:
        """Fetch a URL, extract text, deduplicate, and persist.

        Uses content-addressed IDs and SimHash near-duplicate detection
        via the DocumentIndex.  Falls back to legacy ID format for
        backward compatibility with existing documents on disk.
        """
        is_pdf = url.lower().endswith(".pdf") or "/pdf/" in url.lower()
        resp_headers: dict = {}
        stealth_level_used = self.stealth.level
        escalation_attempts = 0

        try:
            if is_pdf:
                result = await self.fetch_pdf_bytes_ex(url)
                raw_bytes, resp_headers, stealth_level_used, escalation_attempts = result
                if not raw_bytes:
                    logger.debug("PDF unchanged (304): %s", url)
                    return None
                text = self._extract_pdf_text(raw_bytes)
                title = urlparse(url).path.split("/")[-1] or "document.pdf"
                ctype = "pdf"
            else:
                result = await self.fetch_page_ex(url, use_browser=use_browser)
                html, resp_headers, stealth_level_used, escalation_attempts = result
                if not html:
                    logger.debug("Page unchanged (304): %s", url)
                    return None
                text, title = self._extract_html_text(html)
                ctype = "html"
        except PermissionError:
            logger.info("Blocked by robots.txt: %s", url)
            return None
        except Exception as exc:
            logger.warning("Failed to fetch %s: %s", url, exc)
            return None

        if not text or len(text.strip()) < 50:
            return None

        if not force_refetch and not self.change_detector.is_changed(url, text, resp_headers):
            logger.debug("Content unchanged (hash): %s", url)
            return None

        content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if content_hash in self._known_hashes:
            return None

        # ── Document identity: near-dup detection + content-addressed ID ──
        now = datetime.now(tz=timezone.utc).isoformat()
        cid, is_new, near_dup_of = self.doc_index.register(
            url, text, source_id=source_id, fetched_at=now,
        )
        if not is_new and not force_refetch:
            if near_dup_of:
                logger.info("Skipping near-duplicate %s (similar to %s)", url, near_dup_of)
            else:
                logger.debug("Content already indexed: %s", url)
            return None

        self.change_detector.update(url, text, resp_headers)

        # Use content-addressed ID; fall back to legacy format if file exists
        doc_id = cid
        legacy_id = f"{source_id}_{hashlib.md5(url.encode()).hexdigest()[:12]}"
        legacy_path = self.docs_dir / f"{legacy_id}.json"
        if legacy_path.exists():
            doc_id = legacy_id  # keep old filename to avoid orphan

        etag = resp_headers.get("etag") or resp_headers.get("ETag")
        last_mod = resp_headers.get("last-modified") or resp_headers.get("Last-Modified")
        page_count = None
        if ctype == "pdf":
            page_count = text.count("\n\n") + 1 if text else None

        doc = Document(
            id=doc_id, url=url, title=title, text=text,
            content_type=ctype, fetched_at=now, source_id=source_id,
            content_hash=content_hash, word_count=len(text.split()),
            etag=etag, last_modified=last_mod, language=language,
            page_count=page_count,
        )

        doc_path = self.docs_dir / f"{doc_id}.json"
        doc_path.write_text(
            json.dumps(asdict(doc), indent=2, default=str), encoding="utf-8"
        )
        self._known_hashes.add(content_hash)
        return doc

    # -- document storage operations -------------------------------------------

    def load_document(self, doc_id: str) -> Optional[Document]:
        fp = self.docs_dir / f"{doc_id}.json"
        if not fp.exists():
            return None
        data = json.loads(fp.read_text(encoding="utf-8"))
        return Document(**data)

    def list_documents(
        self, source_id: Optional[str] = None, limit: int = 50, offset: int = 0
    ) -> List[dict]:
        docs = []
        for fp in sorted(self.docs_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
            try:
                data = json.loads(fp.read_text(encoding="utf-8"))
                if source_id and data.get("source_id") != source_id:
                    continue
                docs.append({
                    "id": data["id"],
                    "url": data.get("url", ""),
                    "title": data.get("title", ""),
                    "source_id": data.get("source_id", ""),
                    "content_type": data.get("content_type", ""),
                    "fetched_at": data.get("fetched_at", ""),
                    "word_count": data.get("word_count", 0),
                    "content_hash": data.get("content_hash", ""),
                })
            except Exception:
                continue
        return docs[offset : offset + limit]

    def delete_document(self, doc_id: str) -> bool:
        fp = self.docs_dir / f"{doc_id}.json"
        if fp.exists():
            fp.unlink()
            return True
        return False

    def count_documents(self, source_id: Optional[str] = None) -> int:
        if source_id is None:
            return len(list(self.docs_dir.glob("*.json")))
        count = 0
        for fp in self.docs_dir.glob("*.json"):
            try:
                data = json.loads(fp.read_text(encoding="utf-8"))
                if data.get("source_id") == source_id:
                    count += 1
            except Exception:
                continue
        return count
