"""
Dimensional Response Matrix — multi-dimensional severity scoring for LLM safety.

36 dimensions across 4 categories:
  A. Prompt (12) — input properties
  B. Response (7) — output properties
  C. Scenario (11) — ILO forced labor indicators
  D. Systemic (5) — structural factors

Five operations:
  1. RATE   — score a prompt+response on all dimensions (LLM judge)
  2. CALIBRATE RESPONSE — generate better/worse response along a dimension
  3. CALIBRATE QUESTION — generate prompts that shift responses on a dimension
  4. PROBE BOUNDARY — find exact guardrail thresholds per dimension
  5. MAP EMBEDDINGS — unified vector space for boundary visualization
"""

from .dimensions import (
    ALL_DIMENSIONS,
    DIMENSION_BY_ID,
    DIMENSIONS_BY_CATEGORY,
    Dimension,
    DimensionCategory,
    PROMPT_DIMENSIONS,
    RESPONSE_DIMENSIONS,
    SCENARIO_DIMENSIONS,
    SYSTEMIC_DIMENSIONS,
    dimension_ids,
    get_dimension,
    get_dimensions,
)
from .models import (
    CalibrationMatrix,
    CalibrationResult,
    DimensionalScore,
    MatrixEntry,
    ResponseRating,
    RiskLevel,
)
from .rater import DimensionalRater
from .calibrator import DimensionalCalibrator
from .matrix_builder import MatrixBuilder
from .boundary_prober import BoundaryProber, BoundaryProbe, GuardrailMap
from .embedding_mapper import EmbeddingMapper
from .debate_judge import DebateJudge, DebateResult, DebateVerdict, save_debate

__all__ = [
    # Dimensions
    "ALL_DIMENSIONS",
    "DIMENSION_BY_ID",
    "DIMENSIONS_BY_CATEGORY",
    "Dimension",
    "DimensionCategory",
    "PROMPT_DIMENSIONS",
    "RESPONSE_DIMENSIONS",
    "SCENARIO_DIMENSIONS",
    "SYSTEMIC_DIMENSIONS",
    "dimension_ids",
    "get_dimension",
    "get_dimensions",
    # Models
    "CalibrationMatrix",
    "CalibrationResult",
    "DimensionalScore",
    "MatrixEntry",
    "ResponseRating",
    "RiskLevel",
    # Operations
    "DimensionalRater",
    "DimensionalCalibrator",
    "MatrixBuilder",
    "BoundaryProber",
    "BoundaryProbe",
    "GuardrailMap",
    "EmbeddingMapper",
    # Debate
    "DebateJudge",
    "DebateResult",
    "DebateVerdict",
    "save_debate",
]
