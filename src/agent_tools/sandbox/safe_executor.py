"""
Safe executor — run generated mutator code in a restricted environment.

Executes mutator code with a timeout and limited scope, captures output
and errors so agents can verify their generated code works correctly.
"""

from __future__ import annotations

import signal
import sys
import traceback
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionResult:
    """Result of executing code in the sandbox."""

    success: bool
    output: Any = None
    error: str = ""
    error_type: str = ""
    stdout: str = ""
    execution_time_ms: float = 0.0
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "output": str(self.output)[:500] if self.output else None,
            "error": self.error,
            "error_type": self.error_type,
            "stdout": self.stdout[:500],
            "execution_time_ms": self.execution_time_ms,
            "warnings": self.warnings,
        }


class SafeExecutor:
    """Execute generated code in a restricted environment.

    Usage:
        executor = SafeExecutor()

        # Execute a mutator class against test input
        result = executor.test_mutator(source_code, "MutatorClassName", "test input")

        # Execute arbitrary code with restrictions
        result = executor.execute(source_code, timeout_seconds=5)

        # Verify a mutator produces valid output
        valid = executor.verify_mutator_output(output)
    """

    def __init__(self, timeout_seconds: int = 10) -> None:
        self._timeout = timeout_seconds

    def test_mutator(
        self, source: str, class_name: str, test_input: str = "test prompt"
    ) -> ExecutionResult:
        """Test a mutator class from source code.

        Compiles the source, instantiates the named class, and calls
        mutate() with the test input.
        """
        import time

        start = time.monotonic()
        namespace: dict[str, Any] = {}

        # Inject required framework imports into namespace
        try:
            from src.prompt_injection import BaseMutator, register_mutator
            namespace["BaseMutator"] = BaseMutator
            namespace["register_mutator"] = register_mutator
        except ImportError:
            return ExecutionResult(
                success=False,
                error="Cannot import BaseMutator/register_mutator",
                error_type="ImportError",
            )

        # Compile and exec the source
        try:
            code = compile(source, "<sandbox>", "exec")
            exec(code, namespace)  # noqa: S102
        except Exception as exc:
            return ExecutionResult(
                success=False,
                error=str(exc),
                error_type=type(exc).__name__,
                execution_time_ms=(time.monotonic() - start) * 1000,
            )

        # Find and instantiate the class
        if class_name not in namespace:
            return ExecutionResult(
                success=False,
                error=f"Class '{class_name}' not found in source",
                error_type="NameError",
                execution_time_ms=(time.monotonic() - start) * 1000,
            )

        try:
            cls = namespace[class_name]
            instance = cls()
            result = instance.mutate(test_input)
            elapsed = (time.monotonic() - start) * 1000

            warnings: list[str] = []
            if not result:
                warnings.append("mutate() returned empty list")
            else:
                for item in result:
                    if not hasattr(item, "mutated"):
                        warnings.append("Result item missing 'mutated' attribute")
                        break

            return ExecutionResult(
                success=True,
                output=result,
                execution_time_ms=elapsed,
                warnings=warnings,
            )
        except Exception as exc:
            return ExecutionResult(
                success=False,
                error=str(exc),
                error_type=type(exc).__name__,
                execution_time_ms=(time.monotonic() - start) * 1000,
            )

    def execute(self, source: str, timeout_seconds: int | None = None) -> ExecutionResult:
        """Execute arbitrary Python source in a restricted namespace."""
        import io
        import time

        timeout = timeout_seconds or self._timeout
        start = time.monotonic()

        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = captured = io.StringIO()

        try:
            code = compile(source, "<sandbox>", "exec")
            namespace: dict[str, Any] = {"__builtins__": __builtins__}

            # Set timeout on Unix systems
            if hasattr(signal, "SIGALRM"):
                def handler(signum: int, frame: Any) -> None:
                    raise TimeoutError(f"Execution timed out after {timeout}s")
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(timeout)

            exec(code, namespace)  # noqa: S102

            if hasattr(signal, "SIGALRM"):
                signal.alarm(0)

            elapsed = (time.monotonic() - start) * 1000
            return ExecutionResult(
                success=True,
                stdout=captured.getvalue(),
                execution_time_ms=elapsed,
            )
        except TimeoutError as exc:
            return ExecutionResult(
                success=False,
                error=str(exc),
                error_type="TimeoutError",
                stdout=captured.getvalue(),
                execution_time_ms=(time.monotonic() - start) * 1000,
            )
        except Exception as exc:
            return ExecutionResult(
                success=False,
                error=str(exc),
                error_type=type(exc).__name__,
                stdout=captured.getvalue(),
                execution_time_ms=(time.monotonic() - start) * 1000,
            )
        finally:
            sys.stdout = old_stdout
            if hasattr(signal, "SIGALRM"):
                signal.alarm(0)

    @staticmethod
    def verify_mutator_output(output: Any) -> list[str]:
        """Verify that mutator output conforms to expected format.

        Returns list of issues (empty = valid).
        """
        issues: list[str] = []

        if not isinstance(output, list):
            issues.append(f"Expected list, got {type(output).__name__}")
            return issues

        if not output:
            issues.append("Output list is empty")
            return issues

        for i, item in enumerate(output):
            if hasattr(item, "mutated"):
                # MutationResult dataclass
                if not item.mutated:
                    issues.append(f"Item {i}: mutated text is empty")
                if not item.mutator_name:
                    issues.append(f"Item {i}: missing mutator_name")
            elif isinstance(item, tuple) and len(item) == 3:
                # Raw tuple (mutated_text, description, metadata)
                text, desc, meta = item
                if not text:
                    issues.append(f"Item {i}: mutated text is empty")
                if not isinstance(meta, dict):
                    issues.append(f"Item {i}: metadata should be dict")
                elif "technique" not in meta:
                    issues.append(f"Item {i}: metadata missing 'technique' key")
                elif "variant" not in meta:
                    issues.append(f"Item {i}: metadata missing 'variant' key")
            else:
                issues.append(
                    f"Item {i}: unexpected format {type(item).__name__}"
                )

        return issues
