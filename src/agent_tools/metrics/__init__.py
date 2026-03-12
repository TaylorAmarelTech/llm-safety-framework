"""
Metrics — track framework health and improvement trends over time.

Collects snapshots of coverage, mutation count, test pass rates, and
quality scores so agents can detect regressions and measure progress.
"""

from src.agent_tools.metrics.snapshot_collector import SnapshotCollector
from src.agent_tools.metrics.trend_analyzer import TrendAnalyzer
from src.agent_tools.metrics.health_check import HealthCheck

__all__ = ["SnapshotCollector", "TrendAnalyzer", "HealthCheck"]
