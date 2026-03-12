"""
Review prompts — templates for code review and quality assessment.

Provides structured prompts for reviewing generated code, checking
integration correctness, and validating test coverage.
"""

from __future__ import annotations


class ReviewPrompts:
    """Prompt templates for code review tasks.

    Usage:
        prompts = ReviewPrompts()

        # Get a code review prompt
        prompt = prompts.code_review(file_path, source_code)

        # Get a test coverage review prompt
        prompt = prompts.test_coverage_review(category, test_file)

        # Get an integration review prompt
        prompt = prompts.integration_review(changes_summary)
    """

    @staticmethod
    def code_review(file_path: str, source: str = "") -> str:
        """Generate a code review prompt."""
        return (
            f"## Code Review: {file_path}\n\n"
            f"{'```python' + chr(10) + source[:2000] + chr(10) + '```' + chr(10) + chr(10) if source else ''}"
            "### Review Checklist\n"
            "1. [ ] All classes extend BaseMutator correctly\n"
            "2. [ ] NAME attributes are globally unique\n"
            "3. [ ] CATEGORY matches the module's intended category\n"
            "4. [ ] DESCRIPTION accurately describes the technique\n"
            "5. [ ] _apply() returns correct type: list[tuple[str, str, dict]]\n"
            "6. [ ] Metadata contains 'technique' and 'variant' keys\n"
            "7. [ ] No forbidden patterns (eval, exec, subprocess, etc.)\n"
            "8. [ ] Handles edge cases (empty string, very short text)\n"
            "9. [ ] No hardcoded prompts that bypass the text parameter\n"
            "10. [ ] Type hints on all function signatures\n"
            "11. [ ] Helper functions are prefixed with underscore\n"
            "12. [ ] Lookup tables are module-level constants\n"
        )

    @staticmethod
    def test_coverage_review(
        category: str,
        test_file: str = "",
        mutator_count: int = 0,
    ) -> str:
        """Generate a test coverage review prompt."""
        return (
            f"## Test Coverage Review: {category}\n\n"
            f"{'Test file: ' + test_file + chr(10) if test_file else ''}"
            f"{'Expected mutators: ' + str(mutator_count) + chr(10) if mutator_count else ''}"
            "\n### Required Test Coverage\n"
            "1. [ ] Registration test: correct count of mutators in category\n"
            "2. [ ] Name test: each mutator name is registered\n"
            "3. [ ] Functionality test: each mutator transforms input text\n"
            "4. [ ] Metadata test: output metadata has required keys\n"
            "5. [ ] Edge case test: empty string handling\n"
            "6. [ ] Edge case test: short string handling\n"
            "7. [ ] Edge case test: unicode character handling\n"
            "8. [ ] Output test: mutated text differs from input\n"
            "9. [ ] Integration test: taxonomy entry exists in coverage.py\n"
            "10. [ ] Integration test: category in __init__.py imports\n"
        )

    @staticmethod
    def integration_review(changes: str) -> str:
        """Generate an integration review prompt."""
        return (
            "## Integration Review\n\n"
            f"### Changes Made\n{changes}\n\n"
            "### Verification Steps\n"
            "1. [ ] New module imported in __init__.py\n"
            "2. [ ] Taxonomy entry added to coverage.py\n"
            "3. [ ] No NAME collisions with existing mutators\n"
            "4. [ ] Tests written and passing\n"
            "5. [ ] No import cycles introduced\n"
            "6. [ ] Docstring count updated in __init__.py\n"
            "7. [ ] Full test suite still passes\n"
        )

    @staticmethod
    def pre_commit_review() -> str:
        """Generate a pre-commit review checklist."""
        return (
            "## Pre-Commit Review Checklist\n\n"
            "### Code Quality\n"
            "- [ ] All new code has type hints\n"
            "- [ ] No bare except clauses\n"
            "- [ ] No wildcard imports\n"
            "- [ ] No forbidden patterns (eval, exec, etc.)\n\n"
            "### Integration\n"
            "- [ ] New mutators registered in __init__.py\n"
            "- [ ] Taxonomy updated in coverage.py\n"
            "- [ ] No NAME collisions\n\n"
            "### Testing\n"
            "- [ ] New tests written for all new code\n"
            "- [ ] All existing tests still pass\n"
            "- [ ] Edge cases covered (empty, short, unicode)\n\n"
            "### Documentation\n"
            "- [ ] Docstring count updated if mutators added\n"
            "- [ ] CHANGELOG updated if significant change\n"
        )

    @staticmethod
    def regression_check(failing_tests: list[str]) -> str:
        """Generate a regression analysis prompt."""
        return (
            "## Regression Analysis\n\n"
            f"### Failing Tests ({len(failing_tests)})\n"
            + "\n".join(f"- {t}" for t in failing_tests) +
            "\n\n### Investigation Steps\n"
            "1. Identify the common cause of failures\n"
            "2. Check if a recent change broke the tests\n"
            "3. Determine if tests need updating vs code needs fixing\n"
            "4. Fix the root cause, not symptoms\n"
            "5. Re-run full test suite to verify\n"
        )
