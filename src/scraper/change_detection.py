"""
Change detection for scraped pages using ETag, Last-Modified, and content hash.

Avoids re-processing unchanged documents by storing fingerprints.
"""

import hashlib
import json
import logging
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional

logger = logging.getLogger(__name__)


@dataclass
class PageFingerprint:
    """Cached fingerprint for a previously fetched URL."""

    url: str
    etag: Optional[str] = None
    last_modified: Optional[str] = None
    content_hash: str = ""
    last_checked: str = ""


class ChangeDetector:
    """Tracks page fingerprints and detects changes between scrape runs."""

    def __init__(self, data_dir: str = "data/scraper"):
        self.fingerprints_file = Path(data_dir) / "fingerprints.json"
        self._fingerprints: Dict[str, PageFingerprint] = {}
        self._load()

    # -- persistence --------------------------------------------------------------

    def _load(self) -> None:
        if self.fingerprints_file.exists():
            try:
                raw = json.loads(self.fingerprints_file.read_text(encoding="utf-8"))
                for item in raw:
                    fp = PageFingerprint(**item)
                    self._fingerprints[fp.url] = fp
            except Exception:
                logger.warning("Failed to load fingerprints, starting fresh")
                self._fingerprints = {}

    def _save(self) -> None:
        self.fingerprints_file.parent.mkdir(parents=True, exist_ok=True)
        data = [asdict(fp) for fp in self._fingerprints.values()]
        self.fingerprints_file.write_text(
            json.dumps(data, indent=2, default=str), encoding="utf-8"
        )

    # -- public API ---------------------------------------------------------------

    def get_conditional_headers(self, url: str) -> Dict[str, str]:
        """Return If-None-Match / If-Modified-Since headers for a URL.

        If we have a previous fingerprint for this URL, these headers allow
        the server to return 304 Not Modified.
        """
        fp = self._fingerprints.get(url)
        if fp is None:
            return {}
        headers: Dict[str, str] = {}
        if fp.etag:
            headers["If-None-Match"] = fp.etag
        if fp.last_modified:
            headers["If-Modified-Since"] = fp.last_modified
        return headers

    def is_changed(self, url: str, new_content: str, response_headers: Optional[dict] = None) -> bool:
        """Compare new content against the stored fingerprint.

        Returns True if the content has changed (or was never seen before).
        """
        new_hash = hashlib.sha256(new_content.encode("utf-8")).hexdigest()
        fp = self._fingerprints.get(url)
        if fp is None:
            return True  # never seen → treat as changed

        # Check ETag first (server-side)
        if response_headers:
            server_etag = response_headers.get("etag") or response_headers.get("ETag")
            if server_etag and fp.etag and server_etag == fp.etag:
                return False

        # Fall back to content hash
        return new_hash != fp.content_hash

    def update(self, url: str, content: str, response_headers: Optional[dict] = None) -> None:
        """Store a new fingerprint after a successful fetch."""
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        etag = None
        last_modified = None
        if response_headers:
            etag = response_headers.get("etag") or response_headers.get("ETag")
            last_modified = response_headers.get("last-modified") or response_headers.get("Last-Modified")

        self._fingerprints[url] = PageFingerprint(
            url=url,
            etag=etag,
            last_modified=last_modified,
            content_hash=content_hash,
            last_checked=datetime.now(tz=timezone.utc).isoformat(),
        )
        self._save()

    def has_fingerprint(self, url: str) -> bool:
        """Check if we have a stored fingerprint for a URL."""
        return url in self._fingerprints

    def clear(self) -> int:
        """Remove all fingerprints. Returns the number cleared."""
        count = len(self._fingerprints)
        self._fingerprints.clear()
        self._save()
        return count

    def stats(self) -> dict:
        """Return fingerprint cache statistics."""
        return {
            "total_fingerprints": len(self._fingerprints),
            "with_etag": sum(1 for fp in self._fingerprints.values() if fp.etag),
            "with_last_modified": sum(1 for fp in self._fingerprints.values() if fp.last_modified),
        }
