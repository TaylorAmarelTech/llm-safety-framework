"""
Recommendation — smart "do this next" engine for agents.

Combines coverage gaps, feedback history, dependency analysis, and
effort estimation to produce prioritized, actionable recommendations.
"""

from src.agent_tools.recommendation.recommender import Recommender
from src.agent_tools.recommendation.effort_estimator import EffortEstimator
from src.agent_tools.recommendation.impact_scorer import ImpactScorer

__all__ = ["Recommender", "EffortEstimator", "ImpactScorer"]
