"""
Output checker — verify mutator outputs meet quality standards.

Checks that mutated text is meaningfully different from input,
metadata is complete, and outputs don't contain degenerate patterns.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CheckResult:
    """Result of checking a single mutator output."""

    mutator_name: str
    passed: bool
    checks_passed: int = 0
    checks_total: int = 0
    issues: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "mutator_name": self.mutator_name,
            "passed": self.passed,
            "checks_passed": self.checks_passed,
            "checks_total": self.checks_total,
            "issues": self.issues,
        }


class OutputChecker:
    """Verify mutator outputs meet quality standards.

    Usage:
        checker = OutputChecker()

        # Check a single mutator's output
        result = checker.check(mutator_name, original_text, mutated_text, metadata)

        # Check all outputs from a mutate() call
        results = checker.check_batch(original_text, mutation_results)

        # Summarize check results
        summary = checker.summarize(results)
    """

    def check(
        self,
        mutator_name: str,
        original: str,
        mutated: str,
        metadata: dict[str, Any] | None = None,
    ) -> CheckResult:
        """Check a single mutator output for quality."""
        result = CheckResult(mutator_name=mutator_name, passed=True)
        checks_passed = 0
        checks_total = 0

        # 1. Non-empty output
        checks_total += 1
        if mutated and mutated.strip():
            checks_passed += 1
        else:
            result.issues.append("Output is empty or whitespace-only")
            result.passed = False

        # 2. Different from input
        checks_total += 1
        if mutated != original:
            checks_passed += 1
        else:
            result.issues.append("Output is identical to input — no mutation applied")
            result.passed = False

        # 3. Contains some of the original content (not completely replaced)
        checks_total += 1
        if original and mutated:
            # Check if at least some words from original appear
            orig_words = set(original.lower().split())
            mut_words = set(mutated.lower().split())
            overlap = orig_words & mut_words
            if overlap or len(mutated) > len(original) * 0.3:
                checks_passed += 1
            else:
                result.issues.append(
                    "Output shares no words with input — "
                    "mutation may have completely replaced content"
                )
        else:
            checks_passed += 1  # Skip this check for empty inputs

        # 4. Reasonable length (not degenerate)
        checks_total += 1
        if mutated and len(mutated) >= 3:
            checks_passed += 1
        else:
            result.issues.append("Output is too short (< 3 chars)")

        # 5. Not excessively long (> 100x original)
        checks_total += 1
        if original and mutated:
            if len(mutated) <= max(len(original) * 100, 10000):
                checks_passed += 1
            else:
                result.issues.append(
                    f"Output is {len(mutated)/len(original):.0f}x longer than input"
                )
                result.passed = False
        else:
            checks_passed += 1

        # 6. Metadata completeness
        if metadata is not None:
            checks_total += 1
            if "technique" in metadata and "variant" in metadata:
                checks_passed += 1
            else:
                missing = []
                if "technique" not in metadata:
                    missing.append("technique")
                if "variant" not in metadata:
                    missing.append("variant")
                result.issues.append(
                    f"Metadata missing keys: {', '.join(missing)}"
                )

        # 7. No null bytes or control characters (except newlines/tabs)
        checks_total += 1
        bad_chars = [c for c in mutated if ord(c) < 9 or (13 < ord(c) < 32)]
        if not bad_chars:
            checks_passed += 1
        else:
            result.issues.append(
                f"Output contains {len(bad_chars)} unexpected control characters"
            )

        result.checks_passed = checks_passed
        result.checks_total = checks_total
        if result.issues:
            result.passed = all(
                "identical" not in i and "empty" not in i.lower()
                for i in result.issues
            )

        return result

    def check_batch(
        self,
        original: str,
        results: list[Any],
    ) -> list[CheckResult]:
        """Check all outputs from a mutate() call."""
        checks: list[CheckResult] = []

        for item in results:
            if hasattr(item, "mutated"):
                # MutationResult dataclass
                checks.append(self.check(
                    mutator_name=getattr(item, "mutator_name", "unknown"),
                    original=original,
                    mutated=item.mutated,
                    metadata=getattr(item, "metadata", None),
                ))
            elif isinstance(item, tuple) and len(item) >= 2:
                text = item[0]
                meta = item[2] if len(item) > 2 else None
                checks.append(self.check(
                    mutator_name="unknown",
                    original=original,
                    mutated=text,
                    metadata=meta,
                ))

        return checks

    def summarize(self, results: list[CheckResult]) -> dict[str, Any]:
        """Summarize a batch of check results."""
        total = len(results)
        passed = len([r for r in results if r.passed])
        all_issues: list[str] = []
        for r in results:
            for issue in r.issues:
                all_issues.append(f"{r.mutator_name}: {issue}")

        return {
            "total_checked": total,
            "passed": passed,
            "failed": total - passed,
            "pass_rate": round(passed / max(total, 1) * 100, 1),
            "issues": all_issues[:20],  # Cap at 20
        }
