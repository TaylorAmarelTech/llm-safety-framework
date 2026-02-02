"""
News Monitor for Research Updates

Monitors news sources and research publications for new information
about labor exploitation and trafficking patterns.
"""

import json
from datetime import datetime
from typing import Any, Optional
from dataclasses import dataclass, field
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class NewsItem:
    """A news item related to labor exploitation."""
    title: str
    source: str
    url: str
    summary: str
    corridor: Optional[str] = None
    ilo_indicators: list[str] = field(default_factory=list)
    relevance_score: float = 0.0
    published_at: Optional[datetime] = None
    discovered_at: datetime = field(default_factory=datetime.now)


class NewsMonitor:
    """
    Monitor news and research sources for updates on labor exploitation
    and trafficking patterns.
    """

    # Curated list of relevant sources
    SOURCES = [
        {"name": "ILO News", "url": "https://www.ilo.org/newsroom", "type": "official"},
        {"name": "UNODC", "url": "https://www.unodc.org/unodc/en/human-trafficking", "type": "official"},
        {"name": "Anti-Slavery International", "url": "https://www.antislavery.org", "type": "ngo"},
        {"name": "Migrant Forum Asia", "url": "https://mfasia.org", "type": "ngo"},
        {"name": "Verité", "url": "https://verite.org", "type": "research"},
        {"name": "Walk Free Foundation", "url": "https://walkfree.org", "type": "research"},
    ]

    # Keywords for relevance scoring
    KEYWORDS = {
        "high_priority": [
            "recruitment fee", "debt bondage", "forced labor",
            "passport confiscation", "wage theft", "contract substitution",
            "trafficking", "exploitation", "migrant worker"
        ],
        "medium_priority": [
            "domestic worker", "construction worker", "kafala",
            "recruitment agency", "labor rights", "working conditions",
            "labor law", "employment contract"
        ],
        "corridors": {
            "PH": ["philippines", "filipino", "ofw", "poea"],
            "SA": ["saudi", "arabia", "riyadh", "jeddah"],
            "QA": ["qatar", "doha"],
            "MY": ["malaysia", "kuala lumpur"],
            "AE": ["uae", "dubai", "emirates", "abu dhabi"],
            "NP": ["nepal", "nepali", "kathmandu"],
            "BD": ["bangladesh", "bangladeshi", "dhaka"],
            "ET": ["ethiopia", "ethiopian", "addis"],
            "LB": ["lebanon", "beirut", "lebanese"],
        }
    }

    def __init__(self):
        """Initialize news monitor."""
        self.news_items: list[NewsItem] = []
        self.processed_urls: set[str] = set()

    def analyze_relevance(self, text: str) -> tuple[float, list[str], Optional[str]]:
        """
        Analyze text relevance to labor exploitation.

        Args:
            text: Text to analyze

        Returns:
            Tuple of (relevance_score, ilo_indicators, detected_corridor)
        """
        text_lower = text.lower()
        score = 0.0
        indicators = []

        # Check high priority keywords
        for keyword in self.KEYWORDS["high_priority"]:
            if keyword in text_lower:
                score += 0.3
                if keyword in ["debt bondage", "forced labor", "trafficking"]:
                    indicators.append(keyword.replace(" ", "_"))

        # Check medium priority keywords
        for keyword in self.KEYWORDS["medium_priority"]:
            if keyword in text_lower:
                score += 0.1

        # Detect corridor
        detected_corridor = None
        for code, keywords in self.KEYWORDS["corridors"].items():
            for keyword in keywords:
                if keyword in text_lower:
                    if detected_corridor:
                        # Found both origin and destination
                        pass
                    else:
                        detected_corridor = code
                    break

        # Cap relevance score at 1.0
        score = min(1.0, score)

        # Map to ILO indicators
        ilo_mapping = {
            "debt_bondage": "debt_bondage",
            "forced_labor": "abuse_of_vulnerability",
            "trafficking": "deception",
            "passport": "retention_of_identity_documents",
            "wage": "withholding_of_wages",
        }

        for text_indicator in indicators:
            for key, ilo in ilo_mapping.items():
                if key in text_indicator:
                    if ilo not in indicators:
                        indicators.append(ilo)

        return score, indicators, detected_corridor

    def add_news_item(
        self,
        title: str,
        source: str,
        url: str,
        summary: str
    ) -> Optional[NewsItem]:
        """
        Add a news item if relevant.

        Args:
            title: News title
            source: Source name
            url: Article URL
            summary: Article summary

        Returns:
            NewsItem if relevant, None otherwise
        """
        if url in self.processed_urls:
            return None

        self.processed_urls.add(url)

        # Analyze relevance
        combined_text = f"{title} {summary}"
        score, indicators, corridor = self.analyze_relevance(combined_text)

        if score < 0.2:
            logger.debug(f"Skipping low relevance item: {title[:50]}...")
            return None

        item = NewsItem(
            title=title,
            source=source,
            url=url,
            summary=summary,
            corridor=corridor,
            ilo_indicators=indicators,
            relevance_score=score
        )

        self.news_items.append(item)
        logger.info(f"Added news item (relevance={score:.2f}): {title[:50]}...")

        return item

    def get_high_priority_items(self, min_score: float = 0.5) -> list[NewsItem]:
        """Get high priority news items."""
        return [
            item for item in self.news_items
            if item.relevance_score >= min_score
        ]

    def get_items_by_corridor(self, corridor: str) -> list[NewsItem]:
        """Get news items for a specific corridor."""
        return [
            item for item in self.news_items
            if item.corridor and corridor in item.corridor
        ]

    def generate_research_summary(self) -> dict[str, Any]:
        """Generate a summary of monitored news."""
        high_priority = self.get_high_priority_items()

        corridor_counts = {}
        indicator_counts = {}

        for item in self.news_items:
            if item.corridor:
                corridor_counts[item.corridor] = corridor_counts.get(item.corridor, 0) + 1
            for indicator in item.ilo_indicators:
                indicator_counts[indicator] = indicator_counts.get(indicator, 0) + 1

        return {
            "total_items": len(self.news_items),
            "high_priority_count": len(high_priority),
            "corridor_distribution": corridor_counts,
            "indicator_frequency": indicator_counts,
            "top_items": [
                {
                    "title": item.title,
                    "relevance": item.relevance_score,
                    "corridor": item.corridor,
                    "indicators": item.ilo_indicators
                }
                for item in sorted(
                    self.news_items,
                    key=lambda x: -x.relevance_score
                )[:5]
            ],
            "generated_at": datetime.now().isoformat()
        }

    def export_for_research(self) -> list[dict[str, Any]]:
        """Export news items for research agent processing."""
        return [
            {
                "title": item.title,
                "source": item.source,
                "summary": item.summary,
                "corridor": item.corridor,
                "ilo_indicators": item.ilo_indicators,
                "relevance_score": item.relevance_score,
                "discovered_at": item.discovered_at.isoformat()
            }
            for item in self.get_high_priority_items()
        ]


def demo():
    """Demonstrate news monitor capabilities."""
    print("=" * 60)
    print("  News Monitor Demo")
    print("=" * 60)

    monitor = NewsMonitor()

    # Add sample news items
    sample_news = [
        {
            "title": "Qatar announces labor reforms ahead of World Cup",
            "source": "ILO News",
            "url": "https://example.com/qatar-reforms",
            "summary": "New regulations aim to eliminate kafala system and protect migrant workers from recruitment fees and debt bondage."
        },
        {
            "title": "Philippines signs new bilateral agreement with Saudi Arabia",
            "source": "Migrant Forum Asia",
            "url": "https://example.com/ph-sa-agreement",
            "summary": "Agreement addresses domestic worker protections and passport retention issues for Filipino OFWs."
        },
        {
            "title": "Investigation reveals wage theft in Malaysian factories",
            "source": "Anti-Slavery International",
            "url": "https://example.com/my-investigation",
            "summary": "Bangladeshi workers report contract substitution and forced labor conditions in electronics manufacturing."
        },
        {
            "title": "New tech startup launches",
            "source": "Tech News",
            "url": "https://example.com/tech-startup",
            "summary": "A new app for food delivery launches in Singapore."
        }
    ]

    print("\nProcessing news items...")
    for news in sample_news:
        monitor.add_news_item(**news)

    print(f"\nTotal items collected: {len(monitor.news_items)}")

    summary = monitor.generate_research_summary()
    print("\n--- Research Summary ---")
    print(f"High priority items: {summary['high_priority_count']}")
    print(f"Corridor distribution: {summary['corridor_distribution']}")
    print(f"ILO indicators found: {list(summary['indicator_frequency'].keys())}")

    print("\n--- Top Items ---")
    for item in summary['top_items']:
        print(f"  [{item['relevance']:.2f}] {item['title'][:50]}...")


if __name__ == "__main__":
    demo()
