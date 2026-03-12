"""
Step runner — execute individual pipeline steps with error handling.

Wraps step execution with timing, error capture, retry logic,
and result normalization.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class RunResult:
    """Result of running a single step."""

    step_name: str
    success: bool
    output: Any = None
    error: str = ""
    duration_ms: float = 0.0
    retries: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "step_name": self.step_name,
            "success": self.success,
            "error": self.error,
            "duration_ms": self.duration_ms,
            "retries": self.retries,
        }


class StepRunner:
    """Execute individual steps with error handling and timing.

    Usage:
        runner = StepRunner()

        # Run a function with timing
        result = runner.run("check_gaps", lambda: analyzer.analyze())

        # Run with retry
        result = runner.run_with_retry("flaky_step", action, max_retries=3)

        # Run multiple steps sequentially
        results = runner.run_sequence([
            ("step1", lambda: action1()),
            ("step2", lambda: action2()),
        ])
    """

    def run(self, name: str, action: Callable[[], Any]) -> RunResult:
        """Run a single step with timing and error capture."""
        start = time.monotonic()
        try:
            output = action()
            elapsed = (time.monotonic() - start) * 1000
            return RunResult(
                step_name=name,
                success=True,
                output=output,
                duration_ms=elapsed,
            )
        except Exception as exc:
            elapsed = (time.monotonic() - start) * 1000
            return RunResult(
                step_name=name,
                success=False,
                error=str(exc),
                duration_ms=elapsed,
            )

    def run_with_retry(
        self,
        name: str,
        action: Callable[[], Any],
        max_retries: int = 3,
    ) -> RunResult:
        """Run a step with retry on failure."""
        last_error = ""
        for attempt in range(max_retries + 1):
            result = self.run(name, action)
            if result.success:
                result.retries = attempt
                return result
            last_error = result.error

        return RunResult(
            step_name=name,
            success=False,
            error=f"Failed after {max_retries} retries: {last_error}",
            retries=max_retries,
        )

    def run_sequence(
        self,
        steps: list[tuple[str, Callable[[], Any]]],
        stop_on_failure: bool = True,
    ) -> list[RunResult]:
        """Run multiple steps sequentially."""
        results: list[RunResult] = []
        for name, action in steps:
            result = self.run(name, action)
            results.append(result)
            if not result.success and stop_on_failure:
                break
        return results
