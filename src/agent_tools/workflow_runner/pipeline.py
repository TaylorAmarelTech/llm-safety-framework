"""
Pipeline — define and execute multi-step improvement workflows.

A Pipeline is an ordered sequence of Steps, each with a callable
action, expected inputs, and produced outputs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class Step:
    """A single step in a pipeline."""

    name: str
    phase: str  # orient, research, plan, generate, validate, integrate, test, monitor
    description: str = ""
    action: Callable[..., Any] | None = None
    required_inputs: list[str] = field(default_factory=list)
    produces: list[str] = field(default_factory=list)
    skip_on_failure: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "phase": self.phase,
            "description": self.description,
            "required_inputs": self.required_inputs,
            "produces": self.produces,
            "skip_on_failure": self.skip_on_failure,
        }


@dataclass
class StepResult:
    """Result of executing a single step."""

    step_name: str
    success: bool
    output: Any = None
    error: str = ""
    skipped: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "step_name": self.step_name,
            "success": self.success,
            "error": self.error,
            "skipped": self.skipped,
        }


@dataclass
class PipelineResult:
    """Result of executing an entire pipeline."""

    pipeline_name: str
    success: bool
    steps_completed: int = 0
    steps_total: int = 0
    step_results: list[StepResult] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "pipeline_name": self.pipeline_name,
            "success": self.success,
            "steps_completed": self.steps_completed,
            "steps_total": self.steps_total,
            "step_results": [r.to_dict() for r in self.step_results],
        }


class Pipeline:
    """Define and execute multi-step improvement workflows.

    Usage:
        pipe = Pipeline("Add encoding category")

        pipe.add_step(Step(
            name="check_gaps",
            phase="research",
            action=lambda ctx: GapAnalyzer().analyze(),
            produces=["gap_report"],
        ))

        pipe.add_step(Step(
            name="generate_code",
            phase="generate",
            action=lambda ctx: MutatorGenerator().generate_module(ctx["spec"]),
            required_inputs=["spec"],
            produces=["source_code"],
        ))

        pipe.add_step(Step(
            name="validate",
            phase="validate",
            action=lambda ctx: CodeValidator().validate(ctx["source_code"]),
            required_inputs=["source_code"],
            produces=["validation_result"],
        ))

        # Execute with initial context
        result = pipe.run({"spec": my_spec})
    """

    def __init__(self, name: str = "") -> None:
        self._name = name
        self._steps: list[Step] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def steps(self) -> list[Step]:
        return list(self._steps)

    def add_step(self, step: Step) -> "Pipeline":
        """Add a step to the pipeline."""
        self._steps.append(step)
        return self

    def run(self, context: dict[str, Any] | None = None) -> PipelineResult:
        """Execute all steps in order."""
        ctx = dict(context or {})
        result = PipelineResult(
            pipeline_name=self._name,
            success=True,
            steps_total=len(self._steps),
            context=ctx,
        )

        for step in self._steps:
            # Check required inputs
            missing = [
                inp for inp in step.required_inputs
                if inp not in ctx
            ]
            if missing:
                if step.skip_on_failure:
                    result.step_results.append(StepResult(
                        step_name=step.name,
                        success=False,
                        skipped=True,
                        error=f"Missing inputs: {', '.join(missing)}",
                    ))
                    continue
                else:
                    result.step_results.append(StepResult(
                        step_name=step.name,
                        success=False,
                        error=f"Missing required inputs: {', '.join(missing)}",
                    ))
                    result.success = False
                    break

            # Execute step
            if step.action is None:
                result.step_results.append(StepResult(
                    step_name=step.name,
                    success=True,
                    skipped=True,
                ))
                result.steps_completed += 1
                continue

            try:
                output = step.action(ctx)

                # Store outputs
                if step.produces and output is not None:
                    if len(step.produces) == 1:
                        ctx[step.produces[0]] = output
                    elif isinstance(output, dict):
                        for key in step.produces:
                            if key in output:
                                ctx[key] = output[key]

                result.step_results.append(StepResult(
                    step_name=step.name,
                    success=True,
                    output=output,
                ))
                result.steps_completed += 1

            except Exception as exc:
                result.step_results.append(StepResult(
                    step_name=step.name,
                    success=False,
                    error=str(exc),
                ))
                if not step.skip_on_failure:
                    result.success = False
                    break

        result.context = ctx
        return result

    def dry_run(self) -> list[dict[str, Any]]:
        """Preview the pipeline without executing."""
        return [step.to_dict() for step in self._steps]

    def validate(self) -> list[str]:
        """Check pipeline for issues (missing inputs, etc.)."""
        issues: list[str] = []
        available: set[str] = set()

        for step in self._steps:
            for inp in step.required_inputs:
                if inp not in available:
                    issues.append(
                        f"Step '{step.name}' requires '{inp}' but no prior step produces it"
                    )
            for out in step.produces:
                available.add(out)

        return issues
