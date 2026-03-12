"""
Calibration engine for generating shifted responses and questions.

Two operations:
  1. Response calibration — generate a response at a different severity level
  2. Question calibration — modify a prompt to elicit responses at a different level
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

from .dimensions import get_dimension
from .models import CalibrationResult, ResponseRating

logger = logging.getLogger("dimensional_matrix.calibrator")


class DimensionalCalibrator:
    """
    Generates calibrated responses and questions along specific dimensions.

    Usage:
        calibrator = DimensionalCalibrator(endpoint=ep_dict, model_id="mistral-large-latest")

        # Generate a response that scores higher on B1 (Operational Detail)
        result = await calibrator.calibrate_response(
            prompt, response, current_rating,
            target_dim="B1", direction="up",
        )

        # Generate a question that elicits lower scoring on C8 (Debt Bondage)
        result = await calibrator.calibrate_question(
            prompt, response, current_rating,
            target_dim="C8", direction="down",
        )
    """

    def __init__(
        self,
        endpoint: dict[str, Any],
        model_id: str,
        temperature: float = 0.7,
        max_tokens: int = 2048,
    ):
        self.endpoint = endpoint
        self.model_id = model_id
        self.temperature = temperature
        self.max_tokens = max_tokens

    async def _call_llm(self, prompt: str) -> str:
        """Send a prompt to the generation model and return the response."""
        from src.api_client import UnifiedAPIClient

        client = UnifiedAPIClient(self.endpoint, timeout=120.0)
        messages = [{"role": "user", "content": prompt}]
        return await client.chat(
            self.model_id, messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

    def _resolve_levels(
        self,
        current_rating: ResponseRating,
        target_dim: str,
        direction: str,
        step: int = 1,
    ) -> tuple[int, int]:
        """Determine current and target levels from rating + direction."""
        score_obj = current_rating.score_for(target_dim)
        current_level = score_obj.score if score_obj else 3

        if direction == "up":
            target_level = min(5, current_level + step)
        else:
            target_level = max(1, current_level - step)

        return current_level, target_level

    async def calibrate_response(
        self,
        prompt: str,
        response: str,
        current_rating: ResponseRating,
        target_dim: str,
        direction: str = "up",
        step: int = 1,
    ) -> CalibrationResult:
        """
        Generate a calibrated response at a different severity level.

        Args:
            prompt: The original user prompt.
            response: The original LLM response.
            current_rating: Existing dimensional rating of the response.
            target_dim: Dimension ID to calibrate (e.g., "B1", "C3").
            direction: "up" (more harmful) or "down" (less harmful).
            step: How many levels to shift (1 or 2).

        Returns:
            CalibrationResult with the generated response text.
        """
        from .prompts.response_calibration import build_response_calibration_prompt

        current_level, target_level = self._resolve_levels(
            current_rating, target_dim, direction, step,
        )

        dim = get_dimension(target_dim)
        logger.info(
            f"Calibrating response on {dim.name} ({target_dim}): "
            f"{current_level} -> {target_level} ({direction})"
        )

        cal_prompt = build_response_calibration_prompt(
            prompt, response, target_dim, current_level, target_level,
        )

        generated = await self._call_llm(cal_prompt)

        return CalibrationResult(
            original_prompt=prompt,
            original_response=response,
            target_dimension=target_dim,
            target_direction=direction,
            original_level=current_level,
            target_level=target_level,
            generated_text=generated.strip(),
            operation="response",
            model_id=self.model_id,
            timestamp=datetime.now(tz=timezone.utc),
        )

    async def calibrate_question(
        self,
        prompt: str,
        response: str,
        current_rating: ResponseRating,
        target_dim: str,
        direction: str = "up",
        step: int = 1,
    ) -> CalibrationResult:
        """
        Generate a modified prompt that would elicit a different-level response.

        Args:
            prompt: The original user prompt.
            response: The original LLM response.
            current_rating: Existing dimensional rating of the response.
            target_dim: Dimension ID to calibrate (e.g., "A2", "B1").
            direction: "up" (more harmful) or "down" (less harmful).
            step: How many levels to shift (1 or 2).

        Returns:
            CalibrationResult with the modified prompt text.
        """
        from .prompts.question_calibration import build_question_calibration_prompt

        current_level, target_level = self._resolve_levels(
            current_rating, target_dim, direction, step,
        )

        dim = get_dimension(target_dim)
        logger.info(
            f"Calibrating question on {dim.name} ({target_dim}): "
            f"{current_level} -> {target_level} ({direction})"
        )

        cal_prompt = build_question_calibration_prompt(
            prompt, response, target_dim, current_level, target_level,
        )

        generated = await self._call_llm(cal_prompt)

        return CalibrationResult(
            original_prompt=prompt,
            original_response=response,
            target_dimension=target_dim,
            target_direction=direction,
            original_level=current_level,
            target_level=target_level,
            generated_text=generated.strip(),
            operation="question",
            model_id=self.model_id,
            timestamp=datetime.now(tz=timezone.utc),
        )

    async def calibrate_ladder(
        self,
        prompt: str,
        response: str,
        current_rating: ResponseRating,
        target_dim: str,
    ) -> list[CalibrationResult]:
        """
        Generate calibrated responses at ALL levels (1-5) for one dimension.

        Returns a list of CalibrationResults for each level that differs
        from the current score. Useful for building full severity ladders.
        """
        score_obj = current_rating.score_for(target_dim)
        current_level = score_obj.score if score_obj else 3

        results = []
        for target_level in range(1, 6):
            if target_level == current_level:
                continue

            direction = "up" if target_level > current_level else "down"
            from .prompts.response_calibration import build_response_calibration_prompt

            cal_prompt = build_response_calibration_prompt(
                prompt, response, target_dim, current_level, target_level,
            )
            generated = await self._call_llm(cal_prompt)

            results.append(CalibrationResult(
                original_prompt=prompt,
                original_response=response,
                target_dimension=target_dim,
                target_direction=direction,
                original_level=current_level,
                target_level=target_level,
                generated_text=generated.strip(),
                operation="response",
                model_id=self.model_id,
                timestamp=datetime.now(tz=timezone.utc),
            ))

        return results
