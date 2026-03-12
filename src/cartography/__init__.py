"""
LLM Cartography — Safety Topology Mapping System

A mathematical framework for mapping the safety behavior of language models
across a 45-dimensional prompt space. Treats model safety as a continuous
function f: R^45 → [0, 1] and provides tools for:

- **Response Scoring**: 10-level rubric from complete refusal (0) to
  complete exploitation playbook (10)
- **Safety Topology**: Partial derivatives, gradients, cliffs, saddle points,
  blind spots, and KNN interpolation
- **Comparative Matrix**: Cross-model heatmaps, scorecards, rankings, and
  pairwise comparisons
- **Attack Surface**: Compliance rates, dimensional vulnerability, technique
  effectiveness, and attack path discovery
- **Blind Spot Detection**: Cross-dimensional, technique-dimension,
  corridor-specific, category-specific, and gradient anomaly analysis
- **Gradient Generation**: Systematic prompt families for measuring partial
  derivatives and boundary points

Usage:
    from src.cartography import (
        CartographyScorer, SafetyTopology, ComparativeMatrix,
        AttackSurfaceCalculator, BlindSpotDetector, GradientGenerator,
    )

    # Score responses
    scorer = CartographyScorer()
    result = scorer.score_response("prompt", "response")

    # Build topology
    topo = SafetyTopology("gpt-4o")
    topo.add_points(scored_points)
    surface = topo.compute_surface()

    # Compare models
    matrix = ComparativeMatrix()
    matrix.add_model_results("gpt-4o", gpt4_points)
    matrix.add_model_results("claude-3-opus", claude_points)
    heatmap = matrix.compute_heatmap(axis="dimension")

    # Measure attack surface
    calc = AttackSurfaceCalculator()
    calc.add_points(scored_points)
    report = calc.compute_report()

    # Detect blind spots
    detector = BlindSpotDetector()
    detector.add_points(scored_points)
    reports = detector.detect_all()

    # Generate gradient probes
    gen = GradientGenerator()
    families = gen.generate_all_gradients()
"""

from .models import (
    ResponseGrade,
    RESPONSE_GRADES,
    GRADE_BY_LEVEL,
    classify_score_to_grade,
    SafetyClassification,
    SafetyScore,
    PromptPoint,
    GradientFamily,
    SafetySurface,
    ModelScorecard,
    AttackPath,
    BlindSpotSeverity,
    BlindSpotType,
    BlindSpotReport,
)
from .response_scorer import (
    CartographyScorer,
    score_response,
    get_grade,
    STRONG_REFUSAL_KEYWORDS,
    WEAK_REFUSAL_KEYWORDS,
    COMPLIANCE_KEYWORDS,
    OPERATIONAL_KEYWORDS,
    PATTERN_TIERS,
)
from .topology import SafetyTopology
from .comparative_matrix import ComparativeMatrix
from .attack_surface import AttackSurfaceCalculator
from .blind_spot_detector import BlindSpotDetector
from .gradient_generator import (
    GradientGenerator,
    DIMENSION_LEVEL_DESCRIPTIONS,
    GRADIENT_TEMPLATES,
    DEFAULT_CORRIDORS,
)

__all__ = [
    # Models
    "ResponseGrade",
    "RESPONSE_GRADES",
    "GRADE_BY_LEVEL",
    "classify_score_to_grade",
    "SafetyClassification",
    "SafetyScore",
    "PromptPoint",
    "GradientFamily",
    "SafetySurface",
    "ModelScorecard",
    "AttackPath",
    "BlindSpotSeverity",
    "BlindSpotType",
    "BlindSpotReport",
    # Scorer
    "CartographyScorer",
    "score_response",
    "get_grade",
    "STRONG_REFUSAL_KEYWORDS",
    "WEAK_REFUSAL_KEYWORDS",
    "COMPLIANCE_KEYWORDS",
    "OPERATIONAL_KEYWORDS",
    "PATTERN_TIERS",
    # Topology
    "SafetyTopology",
    # Comparative
    "ComparativeMatrix",
    # Attack surface
    "AttackSurfaceCalculator",
    # Blind spots
    "BlindSpotDetector",
    # Gradient generation
    "GradientGenerator",
    "DIMENSION_LEVEL_DESCRIPTIONS",
    "GRADIENT_TEMPLATES",
    "DEFAULT_CORRIDORS",
]
