"""
Code validator — validate generated Python code before execution.

Performs static checks (syntax, imports, forbidden patterns) to catch
issues before code is executed or integrated into the codebase.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from typing import Any


# Patterns that should never appear in generated mutator code
FORBIDDEN_PATTERNS: list[tuple[str, str]] = [
    (r"\beval\s*\(", "eval() is not allowed — use ast.literal_eval if needed"),
    (r"\bexec\s*\(", "exec() is not allowed for safety"),
    (r"\b__import__\s*\(", "__import__() is not allowed — use normal imports"),
    (r"\bos\.system\s*\(", "os.system() is not allowed"),
    (r"\bsubprocess\.", "subprocess module is not allowed"),
    (r"\bopen\s*\(.*['\"]w['\"]", "File writing is not allowed in mutators"),
    (r"\bsocket\.", "Network operations are not allowed in mutators"),
    (r"\brequests\.", "HTTP requests are not allowed in mutators"),
    (r"\burllib\.", "URL operations are not allowed in mutators"),
]

# Required patterns for valid mutator modules
REQUIRED_PATTERNS: list[tuple[str, str]] = [
    (r"class\s+\w+\(BaseMutator\)", "Must have at least one class extending BaseMutator"),
    (r"@register_mutator", "Must use @register_mutator decorator"),
    (r'NAME\s*=\s*["\']', "Must define NAME class attribute"),
    (r'CATEGORY\s*=\s*["\']', "Must define CATEGORY class attribute"),
    (r'DESCRIPTION\s*=\s*["\']', "Must define DESCRIPTION class attribute"),
    (r"def _apply\(self", "Must implement _apply() method"),
]


@dataclass
class ValidationResult:
    """Result of code validation."""

    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)
    class_count: int = 0
    function_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info,
            "class_count": self.class_count,
            "function_count": self.function_count,
        }


class CodeValidator:
    """Validate generated Python code before execution or integration.

    Usage:
        validator = CodeValidator()

        # Validate a source string
        result = validator.validate(source_code)
        if result.valid:
            print("Code is safe to execute")
        else:
            print("Issues found:", result.errors)

        # Validate specifically as a mutator module
        result = validator.validate_mutator_module(source_code)

        # Check if source has forbidden patterns
        forbidden = validator.check_forbidden(source_code)
    """

    def validate(self, source: str) -> ValidationResult:
        """Validate Python source code for basic correctness and safety."""
        result = ValidationResult(valid=True)

        # 1. Syntax check
        try:
            tree = ast.parse(source)
        except SyntaxError as exc:
            result.valid = False
            result.errors.append(f"Syntax error at line {exc.lineno}: {exc.msg}")
            return result

        # 2. Forbidden pattern check
        for pattern, message in FORBIDDEN_PATTERNS:
            if re.search(pattern, source):
                result.valid = False
                result.errors.append(f"Forbidden pattern: {message}")

        # 3. Count structures
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                result.class_count += 1
            elif isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
                result.function_count += 1

        # 4. Check for reasonable size
        line_count = source.count("\n") + 1
        if line_count > 1000:
            result.warnings.append(f"File is very large ({line_count} lines)")
        if line_count < 5:
            result.warnings.append("File seems too short to be useful")

        return result

    def validate_mutator_module(self, source: str) -> ValidationResult:
        """Validate source code specifically as a mutator module."""
        result = self.validate(source)
        if not result.valid:
            return result

        # Check required patterns
        for pattern, message in REQUIRED_PATTERNS:
            if not re.search(pattern, source):
                result.valid = False
                result.errors.append(f"Missing required pattern: {message}")

        # Check for proper import
        if "from src.prompt_injection" not in source:
            if "BaseMutator" in source or "register_mutator" in source:
                result.warnings.append(
                    "Missing import from src.prompt_injection — "
                    "ensure BaseMutator and register_mutator are imported"
                )

        # Check NAME uniqueness format
        names = re.findall(r'NAME\s*=\s*["\']([^"\']+)["\']', source)
        if len(names) != len(set(names)):
            result.valid = False
            result.errors.append("Duplicate NAME values found within module")

        # Check variant count in _apply methods
        try:
            tree = ast.parse(source)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    for child in ast.iter_child_nodes(node):
                        if (isinstance(child, ast.FunctionDef) and
                                child.name == "_apply"):
                            # Check return type hints
                            returns = [
                                n for n in ast.walk(child)
                                if isinstance(n, ast.Return)
                            ]
                            if not returns:
                                result.warnings.append(
                                    f"{node.name}._apply() has no return statement"
                                )
        except SyntaxError:
            pass

        return result

    def check_forbidden(self, source: str) -> list[str]:
        """Check for forbidden patterns only."""
        issues = []
        for pattern, message in FORBIDDEN_PATTERNS:
            if re.search(pattern, source):
                issues.append(message)
        return issues

    def check_naming_collisions(
        self, source: str, existing_names: list[str]
    ) -> list[str]:
        """Check if any mutator NAMEs in source collide with existing ones."""
        names = re.findall(r'NAME\s*=\s*["\']([^"\']+)["\']', source)
        collisions = [n for n in names if n in existing_names]
        return collisions
