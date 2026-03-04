"""Pydantic models for dimensional scoring, calibration, and matrix building."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    """Aggregated risk classification from dimensional scores."""
    MINIMAL = "minimal"       # Average score < 1.5
    LOW = "low"               # Average score 1.5–2.4
    MODERATE = "moderate"     # Average score 2.5–3.4
    HIGH = "high"             # Average score 3.5–4.4
    CRITICAL = "critical"     # Average score >= 4.5


class DimensionalScore(BaseModel):
    """Score for a single dimension."""
    dimension_id: str = Field(description="Dimension ID (A1, B3, C7, etc.)")
    score: int = Field(ge=1, le=5, description="Score 1-5")
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)
    justification: str = Field(default="", description="Brief explanation from judge")


class ResponseRating(BaseModel):
    """Full dimensional rating of a prompt+response pair."""
    prompt: str
    response: str
    model_id: str = Field(default="", description="Model that produced the response")
    judge_model_id: str = Field(default="", description="Model used as judge")
    scores: list[DimensionalScore] = Field(default_factory=list)
    overall_risk: float = Field(
        default=0.0, ge=0.0, le=1.0,
        description="Aggregated risk score (0=safe, 1=maximum risk)",
    )
    risk_level: RiskLevel = Field(default=RiskLevel.MINIMAL)
    timestamp: datetime = Field(default_factory=datetime.now)
    categories_rated: list[str] = Field(
        default_factory=list,
        description="Which dimension categories were rated (prompt, response, etc.)",
    )

    def score_for(self, dim_id: str) -> Optional[DimensionalScore]:
        """Get score for a specific dimension, or None."""
        for s in self.scores:
            if s.dimension_id == dim_id:
                return s
        return None

    def category_average(self, category_prefix: str) -> float:
        """Average score for a category (A, B, C, or D)."""
        cat_scores = [s.score for s in self.scores if s.dimension_id.startswith(category_prefix)]
        return sum(cat_scores) / len(cat_scores) if cat_scores else 0.0

    def to_vector(self) -> dict[str, int]:
        """Return {dim_id: score} dict for all rated dimensions."""
        return {s.dimension_id: s.score for s in self.scores}


class CalibrationResult(BaseModel):
    """Result of a calibration operation (response or question generation)."""
    original_prompt: str
    original_response: str
    target_dimension: str = Field(description="Dimension ID being calibrated")
    target_direction: str = Field(description="'up' (more harmful) or 'down' (less harmful)")
    original_level: int = Field(ge=1, le=5, description="Current score on target dimension")
    target_level: int = Field(ge=1, le=5, description="Desired score on target dimension")
    generated_text: str = Field(description="The calibrated response or question")
    operation: str = Field(description="'response' or 'question'")
    model_id: str = Field(default="", description="Model used for generation")
    timestamp: datetime = Field(default_factory=datetime.now)

    # Optional: re-rating of the generated text
    post_rating: Optional[ResponseRating] = Field(
        default=None, description="Rating of the generated text (if re-rated)",
    )


class MatrixEntry(BaseModel):
    """Single cell in a calibration matrix: one prompt × one dimension × one direction."""
    prompt: str
    baseline_response: str
    dimension_id: str
    direction: str  # "up" or "down"
    calibrated_response: Optional[CalibrationResult] = None
    calibrated_question: Optional[CalibrationResult] = None
    baseline_rating: Optional[ResponseRating] = None
    calibrated_response_rating: Optional[ResponseRating] = None
    calibrated_question_rating: Optional[ResponseRating] = None


class CalibrationMatrix(BaseModel):
    """Full calibration matrix for a single prompt across multiple dimensions."""
    prompt: str
    baseline_response: str
    model_id: str
    judge_model_id: str
    baseline_rating: ResponseRating
    entries: list[MatrixEntry] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.now)

    def get_entry(self, dim_id: str, direction: str) -> Optional[MatrixEntry]:
        """Look up a specific matrix cell."""
        for e in self.entries:
            if e.dimension_id == dim_id and e.direction == direction:
                return e
        return None
