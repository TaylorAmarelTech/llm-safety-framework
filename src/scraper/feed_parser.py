"""
RSS/Atom feed and sitemap.xml parser.

Uses only stdlib xml.etree.ElementTree — no extra dependencies.
"""

import logging
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import List, Optional
from urllib.parse import urljoin

import httpx

logger = logging.getLogger(__name__)


@dataclass
class FeedEntry:
    """A single item from an RSS/Atom feed."""

    title: str
    url: str
    published: Optional[str] = None
    summary: Optional[str] = None


class FeedParser:
    """Parse RSS 2.0, Atom feeds, and sitemap.xml files."""

    USER_AGENT = "LLMSafetyResearchBot/1.0"

    async def fetch_and_parse_feed(self, feed_url: str, timeout: float = 15.0) -> List[FeedEntry]:
        """Fetch a feed URL and parse its entries."""
        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                resp = await client.get(
                    feed_url,
                    headers={"User-Agent": self.USER_AGENT},
                    follow_redirects=True,
                )
                resp.raise_for_status()
            return self.parse_feed(resp.text)
        except Exception as exc:
            logger.warning("Failed to fetch feed %s: %s", feed_url, exc)
            return []

    def parse_feed(self, xml_text: str) -> List[FeedEntry]:
        """Parse an RSS 2.0 or Atom feed from raw XML text."""
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError:
            logger.warning("Malformed XML in feed")
            return []

        # Detect format
        tag = root.tag.lower()
        if "feed" in tag:
            return self._parse_atom(root)
        elif "rss" in tag or root.find("channel") is not None:
            return self._parse_rss(root)
        else:
            logger.warning("Unknown feed format: %s", root.tag)
            return []

    async def fetch_and_parse_sitemap(self, base_url: str, timeout: float = 15.0) -> List[str]:
        """Fetch sitemap.xml from *base_url* and return discovered URLs."""
        sitemap_url = base_url.rstrip("/") + "/sitemap.xml"
        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                resp = await client.get(
                    sitemap_url,
                    headers={"User-Agent": self.USER_AGENT},
                    follow_redirects=True,
                )
                if resp.status_code != 200:
                    return []
            return self.parse_sitemap(resp.text, base_url)
        except Exception as exc:
            logger.debug("No sitemap at %s: %s", sitemap_url, exc)
            return []

    def parse_sitemap(self, xml_text: str, base_url: str = "") -> List[str]:
        """Parse a sitemap.xml and return a list of URLs."""
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError:
            return []

        urls: List[str] = []
        # Handle namespace
        ns = ""
        if root.tag.startswith("{"):
            ns = root.tag.split("}")[0] + "}"

        # Sitemap index → recurse (but don't actually fetch sub-sitemaps here)
        for sitemap in root.findall(f".//{ns}sitemap"):
            loc = sitemap.find(f"{ns}loc")
            if loc is not None and loc.text:
                urls.append(loc.text.strip())

        # URL entries
        for url_elem in root.findall(f".//{ns}url"):
            loc = url_elem.find(f"{ns}loc")
            if loc is not None and loc.text:
                urls.append(loc.text.strip())

        return urls

    # -- private parsers ----------------------------------------------------------

    def _parse_rss(self, root: ET.Element) -> List[FeedEntry]:
        """Parse RSS 2.0 feed."""
        entries: List[FeedEntry] = []
        channel = root.find("channel")
        if channel is None:
            return entries
        for item in channel.findall("item"):
            title = self._text(item, "title") or "Untitled"
            link = self._text(item, "link") or ""
            pub_date = self._text(item, "pubDate")
            description = self._text(item, "description")
            if link:
                entries.append(FeedEntry(
                    title=title, url=link.strip(),
                    published=pub_date, summary=description,
                ))
        return entries

    def _parse_atom(self, root: ET.Element) -> List[FeedEntry]:
        """Parse Atom feed."""
        entries: List[FeedEntry] = []
        ns = ""
        if root.tag.startswith("{"):
            ns = root.tag.split("}")[0] + "}"

        for entry in root.findall(f"{ns}entry"):
            title = self._text(entry, f"{ns}title") or "Untitled"
            link_elem = entry.find(f"{ns}link[@href]")
            link = link_elem.get("href", "") if link_elem is not None else ""
            published = self._text(entry, f"{ns}published") or self._text(entry, f"{ns}updated")
            summary = self._text(entry, f"{ns}summary") or self._text(entry, f"{ns}content")
            if link:
                entries.append(FeedEntry(
                    title=title, url=link.strip(),
                    published=published, summary=summary,
                ))
        return entries

    @staticmethod
    def _text(elem: ET.Element, tag: str) -> Optional[str]:
        """Safely get text content of a child element."""
        child = elem.find(tag)
        return child.text.strip() if child is not None and child.text else None
