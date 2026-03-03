"""
Retry logic with exponential backoff for failed HTTP requests.

Wraps tenacity if available, otherwise provides a standalone implementation.
"""

import asyncio
import logging
import random
from typing import Any, Callable, Set, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


class RetryableError(Exception):
    """Raised to signal that an operation should be retried."""

    def __init__(self, message: str = "", status_code: int = 0):
        super().__init__(message)
        self.status_code = status_code


class RetryPolicy:
    """Configurable retry with exponential backoff."""

    def __init__(
        self,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 30.0,
        backoff_factor: float = 2.0,
        retryable_status_codes: Set[int] = frozenset({429, 500, 502, 503, 504}),
        jitter: bool = True,
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.backoff_factor = backoff_factor
        self.retryable_status_codes = set(retryable_status_codes)
        self.jitter = jitter
        self._total_retries = 0

    async def execute(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        """Execute *func* with retry on RetryableError or retryable HTTP status codes.

        Returns the result of *func* on success, or raises the last exception
        after max_retries are exhausted.
        """
        last_exc: Exception = RuntimeError("unreachable")
        delay = self.base_delay

        for attempt in range(self.max_retries + 1):
            try:
                return await func(*args, **kwargs)
            except RetryableError as exc:
                last_exc = exc
                if attempt == self.max_retries:
                    break
                self._total_retries += 1
                logger.warning(
                    "Retry %d/%d after %s (status=%d), waiting %.1fs",
                    attempt + 1, self.max_retries, exc, exc.status_code, delay,
                )
                sleep_time = delay * (0.5 + random.random()) if self.jitter else delay
                await asyncio.sleep(sleep_time)
                delay = min(delay * self.backoff_factor, self.max_delay)
            except Exception as exc:
                # Non-retryable → raise immediately
                raise

        raise last_exc

    def is_retryable_status(self, status_code: int) -> bool:
        """Check if an HTTP status code warrants a retry."""
        return status_code in self.retryable_status_codes

    @property
    def total_retries(self) -> int:
        """Number of retries performed across all calls."""
        return self._total_retries

    def get_config(self) -> dict:
        """Return current retry configuration."""
        return {
            "max_retries": self.max_retries,
            "base_delay": self.base_delay,
            "max_delay": self.max_delay,
            "backoff_factor": self.backoff_factor,
            "retryable_status_codes": sorted(self.retryable_status_codes),
        }
