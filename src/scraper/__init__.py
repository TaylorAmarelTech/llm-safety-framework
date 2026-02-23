"""
Document Intelligence Agent - scraper, extractor, and knowledge base.

Continuously fetches authoritative sources (IOM, DMW, ILO, HK/SG regulators, NGOs),
archives raw documents, extracts structured facts, and provides knowledge to
the prompt generator.
"""

from .sources import SourceConfig, SourceRegistry, DEFAULT_SOURCES, TIER_LABELS
from .fetcher import DocumentFetcher, Document
from .extractor import FactExtractor, ExtractionResult
from .knowledge_base import KnowledgeBase
from .scheduler import ScrapeOrchestrator
from .browser import HeadlessBrowser, close_browser
from .politeness import PolitenessPolicy
from .retry import RetryPolicy, RetryableError
from .change_detection import ChangeDetector
from .feed_parser import FeedParser, FeedEntry
from .stealth import StealthProfile, StealthLevel, HeaderBuilder, UARotator, STEALTH_LABELS
from .proxy import ProxyRotator
from .document_identity import DocumentIndex, canonical_url, simhash, content_id
from .health import HealthTracker, SourceHealth
from .seed_loader import load_seeds, is_seeded

__all__ = [
    "SourceConfig",
    "SourceRegistry",
    "DEFAULT_SOURCES",
    "TIER_LABELS",
    "DocumentFetcher",
    "Document",
    "FactExtractor",
    "ExtractionResult",
    "KnowledgeBase",
    "ScrapeOrchestrator",
    "HeadlessBrowser",
    "close_browser",
    "PolitenessPolicy",
    "RetryPolicy",
    "RetryableError",
    "ChangeDetector",
    "FeedParser",
    "FeedEntry",
    "StealthProfile",
    "StealthLevel",
    "HeaderBuilder",
    "UARotator",
    "STEALTH_LABELS",
    "ProxyRotator",
    "DocumentIndex",
    "canonical_url",
    "simhash",
    "content_id",
    "load_seeds",
    "is_seeded",
    "HealthTracker",
    "SourceHealth",
]
