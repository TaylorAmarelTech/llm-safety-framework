"""
Document identity, fingerprinting, and near-duplicate detection.

Provides:
- URL canonicalization (strip tracking params, normalize)
- SimHash (64-bit) for near-duplicate detection
- Content-addressed document IDs
- DocumentIndex for version tracking and cross-source dedup
"""

import hashlib
import json
import logging
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

logger = logging.getLogger(__name__)

# ── URL Canonicalization ─────────────────────────────────────────────

# Tracking / session parameters to strip
_STRIP_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "utm_id", "utm_cid", "fbclid", "gclid", "gclsrc", "dclid", "msclkid",
    "ref", "source", "sessionid", "sid", "jsessionid", "phpsessid",
    "mc_cid", "mc_eid", "_ga", "_gl", "yclid", "twclid",
}


def canonical_url(raw_url: str) -> str:
    """Canonicalize a URL for deduplication.

    - Upgrade to https
    - Lowercase hostname
    - Remove trailing slash (unless path is just "/")
    - Remove fragment (#...)
    - Strip tracking / session query params
    - Sort remaining query params alphabetically
    - Remove default ports (:80, :443)
    """
    parsed = urlparse(raw_url.strip())

    # Scheme: default to https
    scheme = "https"

    # Hostname: lowercase
    hostname = (parsed.hostname or "").lower()

    # Port: remove default
    port = parsed.port
    if port in (80, 443, None):
        netloc = hostname
    else:
        netloc = f"{hostname}:{port}"

    # Path: remove trailing slash (keep root "/")
    path = parsed.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")

    # Query: strip tracking params, sort rest
    qs = parse_qs(parsed.query, keep_blank_values=True)
    filtered = {
        k: v for k, v in qs.items()
        if k.lower() not in _STRIP_PARAMS
    }
    sorted_query = urlencode(sorted(filtered.items()), doseq=True) if filtered else ""

    # Fragment: always remove
    return urlunparse((scheme, netloc, path, "", sorted_query, ""))


# ── SimHash (64-bit) ─────────────────────────────────────────────────

_SIMHASH_BITS = 64
_SHINGLE_SIZE = 3  # word-level 3-grams
_NEAR_DUP_THRESHOLD = 10  # Hamming distance ≤ 10 ≈ 84% similarity


def _tokenize(text: str) -> list[str]:
    """Split text into lowercase word tokens."""
    return re.findall(r"[a-z0-9]+", text.lower())


def _shingles(tokens: list[str], size: int = _SHINGLE_SIZE) -> list[str]:
    """Generate word-level n-gram shingles."""
    if len(tokens) < size:
        return [" ".join(tokens)] if tokens else []
    return [" ".join(tokens[i : i + size]) for i in range(len(tokens) - size + 1)]


def _hash64(s: str) -> int:
    """Hash a string to a 64-bit integer via MD5."""
    digest = hashlib.md5(s.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big")


def simhash(text: str) -> int:
    """Compute a 64-bit SimHash fingerprint for *text*.

    Uses word-level 3-gram shingles hashed via MD5.
    """
    tokens = _tokenize(text)
    shingle_list = _shingles(tokens)
    if not shingle_list:
        return 0

    # Weighted bit vector
    v = [0] * _SIMHASH_BITS
    for sh in shingle_list:
        h = _hash64(sh)
        for i in range(_SIMHASH_BITS):
            if h & (1 << i):
                v[i] += 1
            else:
                v[i] -= 1

    # Collapse to fingerprint
    fingerprint = 0
    for i in range(_SIMHASH_BITS):
        if v[i] > 0:
            fingerprint |= 1 << i
    return fingerprint


def hamming_distance(a: int, b: int) -> int:
    """Count differing bits between two 64-bit fingerprints."""
    return bin(a ^ b).count("1")


def is_near_duplicate(hash_a: int, hash_b: int, threshold: int = _NEAR_DUP_THRESHOLD) -> bool:
    """Check if two simhashes are near-duplicates."""
    return hamming_distance(hash_a, hash_b) <= threshold


# ── Content-Addressed IDs ────────────────────────────────────────────

def _normalize_text(text: str) -> str:
    """Normalize text for content addressing: lowercase, collapse whitespace."""
    return re.sub(r"\s+", " ", text.strip().lower())


def content_id(text: str) -> str:
    """Generate a content-addressed document ID.

    Returns ``doc_{sha256(normalized_text)[:16]}`` — deterministic for
    identical content regardless of source URL.
    """
    normalized = _normalize_text(text)
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]
    return f"doc_{digest}"


# ── Document Index ───────────────────────────────────────────────────

@dataclass
class VersionRecord:
    """One version of a document at a canonical URL."""
    fetched_at: str
    content_id: str
    simhash: int
    byte_size: int


@dataclass
class DocumentEntry:
    """Tracking entry for a canonical URL in the index."""
    canonical_url: str
    current_content_id: str
    current_simhash: int
    source_ids: list[str] = field(default_factory=list)
    versions: list[dict] = field(default_factory=list)


class DocumentIndex:
    """Persistent index mapping canonical URLs to content fingerprints.

    Enables:
    - Near-duplicate detection across all sources
    - Version tracking (content changes over time)
    - Cross-source dedup (same content from different URLs)

    Persists to ``{data_dir}/document_index.json``.
    """

    def __init__(self, data_dir: str = "data/scraper"):
        self._data_dir = Path(data_dir)
        self._index_path = self._data_dir / "document_index.json"
        # canonical_url → DocumentEntry (as dict for easy serialization)
        self._entries: dict[str, dict] = {}
        # simhash → list of canonical_urls (for near-dup lookup)
        self._simhash_index: dict[int, list[str]] = {}
        # content_id → list of canonical_urls (for cross-source dedup)
        self._content_index: dict[str, list[str]] = {}
        self._load()

    def _load(self) -> None:
        """Load index from disk."""
        if self._index_path.exists():
            try:
                data = json.loads(self._index_path.read_text(encoding="utf-8"))
                self._entries = data.get("entries", {})
            except (json.JSONDecodeError, OSError) as exc:
                logger.warning("Failed to load document index: %s", exc)
                self._entries = {}
        self._rebuild_secondary_indexes()

    def _rebuild_secondary_indexes(self) -> None:
        """Rebuild simhash and content lookup indexes from entries."""
        self._simhash_index.clear()
        self._content_index.clear()
        for curl, entry in self._entries.items():
            sh = entry.get("current_simhash", 0)
            self._simhash_index.setdefault(sh, []).append(curl)
            cid = entry.get("current_content_id", "")
            if cid:
                self._content_index.setdefault(cid, []).append(curl)

    def save(self) -> None:
        """Persist index to disk."""
        self._data_dir.mkdir(parents=True, exist_ok=True)
        data = {"entries": self._entries, "saved_at": datetime.now(timezone.utc).isoformat()}
        self._index_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def register(
        self,
        url: str,
        text: str,
        source_id: str = "",
        fetched_at: Optional[str] = None,
    ) -> tuple[str, bool, Optional[str]]:
        """Register a fetched document.

        Args:
            url: Raw URL of the document.
            text: Extracted text content.
            source_id: Source that fetched this URL.
            fetched_at: ISO timestamp (defaults to now).

        Returns:
            Tuple of (content_id, is_new, near_dup_of):
            - content_id: The content-addressed ID for this text.
            - is_new: True if this is genuinely new content.
            - near_dup_of: canonical URL of a near-duplicate, or None.
        """
        curl = canonical_url(url)
        cid = content_id(text)
        sh = simhash(text)
        now = fetched_at or datetime.now(timezone.utc).isoformat()
        byte_size = len(text.encode("utf-8"))

        # Check for exact content match (cross-source dedup)
        if cid in self._content_index:
            existing_urls = self._content_index[cid]
            if curl not in existing_urls:
                # Same content from a different URL
                logger.info(
                    "Cross-source duplicate: %s has same content as %s",
                    curl, existing_urls[0],
                )
                # Still register the URL mapping but flag as not new
                self._update_entry(curl, cid, sh, source_id, now, byte_size)
                self.save()
                return cid, False, existing_urls[0]

        # Check for near-duplicate via simhash
        near_dup = self._find_near_duplicate(sh, exclude_url=curl)
        if near_dup:
            logger.info(
                "Near-duplicate: %s is similar to %s (hamming=%d)",
                curl, near_dup, hamming_distance(sh, self._entries[near_dup]["current_simhash"]),
            )
            self._update_entry(curl, cid, sh, source_id, now, byte_size)
            self.save()
            return cid, False, near_dup

        # Check if this URL's content changed (version tracking)
        is_new = True
        if curl in self._entries:
            old_cid = self._entries[curl].get("current_content_id")
            if old_cid == cid:
                # Content unchanged
                is_new = False
            else:
                # Content changed — new version
                logger.info("Content changed at %s: %s → %s", curl, old_cid, cid)

        self._update_entry(curl, cid, sh, source_id, now, byte_size)
        self.save()
        return cid, is_new, None

    def _update_entry(
        self,
        curl: str,
        cid: str,
        sh: int,
        source_id: str,
        fetched_at: str,
        byte_size: int,
    ) -> None:
        """Create or update an entry in the index."""
        version = {
            "fetched_at": fetched_at,
            "content_id": cid,
            "simhash": sh,
            "byte_size": byte_size,
        }

        if curl in self._entries:
            entry = self._entries[curl]
            # Remove old secondary index entries
            old_sh = entry.get("current_simhash", 0)
            if old_sh in self._simhash_index:
                self._simhash_index[old_sh] = [
                    u for u in self._simhash_index[old_sh] if u != curl
                ]
            old_cid = entry.get("current_content_id", "")
            if old_cid in self._content_index:
                self._content_index[old_cid] = [
                    u for u in self._content_index[old_cid] if u != curl
                ]
            # Update
            entry["current_content_id"] = cid
            entry["current_simhash"] = sh
            if source_id and source_id not in entry.get("source_ids", []):
                entry.setdefault("source_ids", []).append(source_id)
            entry.setdefault("versions", []).append(version)
        else:
            self._entries[curl] = {
                "canonical_url": curl,
                "current_content_id": cid,
                "current_simhash": sh,
                "source_ids": [source_id] if source_id else [],
                "versions": [version],
            }

        # Update secondary indexes
        self._simhash_index.setdefault(sh, []).append(curl)
        self._content_index.setdefault(cid, []).append(curl)

    def _find_near_duplicate(
        self, sh: int, exclude_url: Optional[str] = None
    ) -> Optional[str]:
        """Scan all indexed simhashes for a near-duplicate."""
        for existing_sh, urls in self._simhash_index.items():
            if is_near_duplicate(sh, existing_sh):
                for u in urls:
                    if u != exclude_url:
                        return u
        return None

    def find_near_duplicates(self, text: str) -> list[dict]:
        """Find all near-duplicates for the given text.

        Returns list of dicts with ``canonical_url`` and ``hamming_distance``.
        """
        sh = simhash(text)
        results = []
        for existing_sh, urls in self._simhash_index.items():
            dist = hamming_distance(sh, existing_sh)
            if dist <= _NEAR_DUP_THRESHOLD:
                for u in urls:
                    results.append({
                        "canonical_url": u,
                        "hamming_distance": dist,
                        "content_id": self._entries.get(u, {}).get("current_content_id"),
                    })
        return results

    def get_version_history(self, url: str) -> list[dict]:
        """Get version history for a URL."""
        curl = canonical_url(url)
        entry = self._entries.get(curl)
        if not entry:
            return []
        return list(entry.get("versions", []))

    def get_entry(self, url: str) -> Optional[dict]:
        """Get the full index entry for a URL."""
        return self._entries.get(canonical_url(url))

    @property
    def size(self) -> int:
        """Number of indexed URLs."""
        return len(self._entries)

    def stats(self) -> dict:
        """Summary statistics."""
        unique_content = len(self._content_index)
        total_versions = sum(
            len(e.get("versions", [])) for e in self._entries.values()
        )
        return {
            "indexed_urls": self.size,
            "unique_content": unique_content,
            "total_versions": total_versions,
        }
