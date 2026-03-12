"""
Matrix builder — orchestrates full calibration matrix generation.

Given a prompt and baseline response, builds a calibration matrix by:
  1. Rating the baseline response on all dimensions
  2. For each target dimension x direction (up/down):
     a. Generate a calibrated response
     b. Generate a calibrated question
     c. Optionally re-rate the calibrated outputs
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

from .calibrator import DimensionalCalibrator
from .dimensions import DimensionCategory, get_dimensions
from .models import CalibrationMatrix, MatrixEntry, ResponseRating
from .rater import DimensionalRater

logger = logging.getLogger("dimensional_matrix.matrix_builder")


class MatrixBuilder:
    """
    Builds full calibration matrices for prompt+response pairs.

    Usage:
        builder = MatrixBuilder(
            generator_endpoint=ep_dict,
            generator_model="mistral-large-latest",
            judge_endpoint=ep_dict,
            judge_model="mistral-large-latest",
        )

        matrix = await builder.build(prompt, response, dimensions=["B1", "B6", "C8"])
    """

    def __init__(
        self,
        generator_endpoint: dict[str, Any],
        generator_model: str,
        judge_endpoint: dict[str, Any] | None = None,
        judge_model: str | None = None,
        re_rate: bool = True,
    ):
        """
        Args:
            generator_endpoint: API endpoint config for generating calibrated outputs.
            generator_model: Model ID for generation.
            judge_endpoint: API endpoint for the judge (defaults to generator_endpoint).
            judge_model: Model ID for judging (defaults to generator_model).
            re_rate: Whether to re-rate calibrated outputs.
        """
        self.calibrator = DimensionalCalibrator(
            endpoint=generator_endpoint,
            model_id=generator_model,
        )
        self.rater = DimensionalRater(
            endpoint=judge_endpoint or generator_endpoint,
            model_id=judge_model or generator_model,
        )
        self.re_rate = re_rate
        self.generator_model = generator_model
        self.judge_model = judge_model or generator_model

    async def build(
        self,
        prompt: str,
        response: str,
        dimensions: list[str] | None = None,
        categories: list[DimensionCategory] | None = None,
        directions: list[str] | None = None,
        response_model_id: str = "",
    ) -> CalibrationMatrix:
        """
        Build a calibration matrix for a single prompt+response.

        Args:
            prompt: The original user prompt.
            response: The baseline LLM response.
            dimensions: Specific dimension IDs to calibrate (e.g., ["B1", "C8"]).
                        If None, uses all dimensions from specified categories.
            categories: Which categories to calibrate (None = all 4).
            directions: Which directions to calibrate (default: ["up", "down"]).
            response_model_id: ID of the model that produced the response.

        Returns:
            CalibrationMatrix with baseline rating and all entries.
        """
        if directions is None:
            directions = ["up", "down"]

        # Step 1: Rate the baseline
        logger.info("Rating baseline response...")
        baseline_rating = await self.rater.rate(
            prompt, response,
            categories=categories,
            response_model_id=response_model_id,
        )

        # Determine which dimensions to calibrate
        if dimensions:
            target_dims = dimensions
        elif categories:
            target_dims = []
            for cat in categories:
                target_dims.extend(d.id for d in get_dimensions(cat))
        else:
            target_dims = [d.id for d in get_dimensions()]

        # Step 2: Build entries for each dimension x direction
        entries: list[MatrixEntry] = []
        total = len(target_dims) * len(directions)
        completed = 0

        for dim_id in target_dims:
            for direction in directions:
                completed += 1
                logger.info(f"[{completed}/{total}] Calibrating {dim_id} {direction}")

                entry = MatrixEntry(
                    prompt=prompt,
                    baseline_response=response,
                    dimension_id=dim_id,
                    direction=direction,
                    baseline_rating=baseline_rating,
                )

                # Generate calibrated response
                try:
                    cal_resp = await self.calibrator.calibrate_response(
                        prompt, response, baseline_rating,
                        target_dim=dim_id, direction=direction,
                    )
                    entry.calibrated_response = cal_resp

                    # Re-rate the calibrated response
                    if self.re_rate and cal_resp.generated_text:
                        re_rating = await self.rater.rate(
                            prompt, cal_resp.generated_text,
                            categories=categories,
                            response_model_id=self.generator_model,
                        )
                        entry.calibrated_response_rating = re_rating
                        cal_resp.post_rating = re_rating
                except Exception as e:
                    logger.warning(f"Response calibration failed for {dim_id} {direction}: {e}")

                # Generate calibrated question
                try:
                    cal_q = await self.calibrator.calibrate_question(
                        prompt, response, baseline_rating,
                        target_dim=dim_id, direction=direction,
                    )
                    entry.calibrated_question = cal_q
                except Exception as e:
                    logger.warning(f"Question calibration failed for {dim_id} {direction}: {e}")

                entries.append(entry)

        return CalibrationMatrix(
            prompt=prompt,
            baseline_response=response,
            model_id=response_model_id,
            judge_model_id=self.judge_model,
            baseline_rating=baseline_rating,
            entries=entries,
            timestamp=datetime.now(tz=timezone.utc),
        )

    async def build_batch(
        self,
        items: list[dict[str, str]],
        dimensions: list[str] | None = None,
        categories: list[DimensionCategory] | None = None,
    ) -> list[CalibrationMatrix]:
        """
        Build calibration matrices for multiple prompt+response pairs.

        Each item should have 'prompt' and 'response' keys, and optionally 'model_id'.
        """
        results = []
        for i, item in enumerate(items):
            logger.info(f"Building matrix {i+1}/{len(items)}")
            matrix = await self.build(
                prompt=item["prompt"],
                response=item["response"],
                dimensions=dimensions,
                categories=categories,
                response_model_id=item.get("model_id", ""),
            )
            results.append(matrix)
        return results

    async def build_ladder(
        self,
        prompt: str,
        response: str,
        target_dim: str,
        response_model_id: str = "",
    ) -> dict:
        """
        Build a complete severity ladder (levels 1-5) for one dimension.

        Returns a dict with:
          - baseline_rating: full dimensional rating
          - ladder: {1: CalibrationResult, 2: ..., 3: baseline, 4: ..., 5: ...}
          - re_ratings: {1: ResponseRating, 2: ..., ...} (if re_rate=True)
        """
        baseline_rating = await self.rater.rate(
            prompt, response, response_model_id=response_model_id,
        )

        ladder_results = await self.calibrator.calibrate_ladder(
            prompt, response, baseline_rating, target_dim,
        )

        ladder = {}
        re_ratings = {}

        score_obj = baseline_rating.score_for(target_dim)
        baseline_level = score_obj.score if score_obj else 3

        for cal in ladder_results:
            ladder[cal.target_level] = cal

            if self.re_rate and cal.generated_text:
                re_rating = await self.rater.rate(
                    prompt, cal.generated_text,
                    response_model_id=self.generator_model,
                )
                re_ratings[cal.target_level] = re_rating
                cal.post_rating = re_rating

        return {
            "prompt": prompt,
            "baseline_response": response,
            "target_dimension": target_dim,
            "baseline_level": baseline_level,
            "baseline_rating": baseline_rating,
            "ladder": ladder,
            "re_ratings": re_ratings,
        }
