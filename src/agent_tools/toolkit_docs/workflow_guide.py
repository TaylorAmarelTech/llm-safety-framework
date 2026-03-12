"""
Workflow guide — end-to-end workflow documentation for agents.

Generates step-by-step workflow instructions that agents can follow
for common improvement tasks.
"""

from __future__ import annotations

from typing import Any


# Pre-defined workflows
WORKFLOWS: dict[str, dict[str, Any]] = {
    "new_category": {
        "title": "Add a New Mutator Category",
        "description": "Create a complete new category with mutators, tests, and registration",
        "steps": [
            {
                "phase": "orient",
                "action": "Check existing categories and naming",
                "tools": ["ProjectMap.category_list()", "ConventionGuide.for_area('naming')"],
                "code": "from src.agent_tools.context.project_map import ProjectMap\npmap = ProjectMap()\nprint(pmap.summary())",
            },
            {
                "phase": "research",
                "action": "Find gaps and choose a target",
                "tools": ["GapAnalyzer.analyze()", "TechniqueCatalog.not_implemented()"],
                "code": "from src.agent_tools.research.gap_analyzer import GapAnalyzer\nreport = GapAnalyzer().analyze()",
            },
            {
                "phase": "plan",
                "action": "Plan the category and check for collisions",
                "tools": ["CategoryPlanner.plan()", "CategoryPlanner.check_collisions()"],
                "code": "from src.agent_tools.scaffolding.category_planner import CategoryPlanner\nspec = CategoryPlanner().plan(name='...', description='...')",
            },
            {
                "phase": "generate",
                "action": "Generate the module and test files",
                "tools": ["MutatorGenerator.generate_module()", "TestGenerator.generate()"],
                "code": "from src.agent_tools.scaffolding.mutator_generator import MutatorGenerator\ncode = MutatorGenerator().generate_module(spec)",
            },
            {
                "phase": "validate",
                "action": "Validate the generated code",
                "tools": ["CodeValidator.validate_mutator_module()", "SafeExecutor.test_mutator()"],
                "code": "from src.agent_tools.sandbox import CodeValidator\nresult = CodeValidator().validate_mutator_module(code)",
            },
            {
                "phase": "integrate",
                "action": "Register in __init__.py and coverage.py",
                "tools": ["ChangeBuilder.for_new_category()", "FilePatcher.apply()"],
                "code": "# Add import to __init__.py\n# Add taxonomy entry to coverage.py",
            },
            {
                "phase": "test",
                "action": "Run tests and verify",
                "tools": ["MutatorValidator.validate_category()", "CoverageChecker.check_category()"],
                "code": "# py -3.13 -m pytest tests/test_<category>.py -v",
            },
            {
                "phase": "monitor",
                "action": "Record the outcome",
                "tools": ["ResultCollector.record()", "SnapshotCollector.capture()"],
                "code": "from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome\nResultCollector().record(TaskOutcome(...))",
            },
        ],
    },
    "integrate_repo": {
        "title": "Integrate an External Repository",
        "description": "Evaluate and integrate techniques from a GitHub repository",
        "steps": [
            {
                "phase": "research",
                "action": "Evaluate the repository",
                "tools": ["RepoScanner.known_repos()", "RepoEvaluator.evaluate()"],
            },
            {
                "phase": "plan",
                "action": "Plan the integration",
                "tools": ["RepoScanner.integration_plan()", "EffortEstimator.estimate()"],
            },
            {
                "phase": "generate",
                "action": "Generate adapter code",
                "tools": ["AdapterFactory.generate()", "DependencyManager.generate_try_import()"],
            },
            {
                "phase": "validate",
                "action": "Validate and test the adapter",
                "tools": ["CodeValidator.validate()", "SafeExecutor.test_mutator()"],
            },
            {
                "phase": "integrate",
                "action": "Register the new mutators",
                "tools": ["RegistrationChecker.check_all()", "ImportChecker.check_file()"],
            },
        ],
    },
    "fix_regression": {
        "title": "Fix a Regression",
        "description": "Investigate and fix a test regression",
        "steps": [
            {
                "phase": "orient",
                "action": "Identify the failing tests",
                "tools": ["HealthCheck.run()", "FileFinder.tests_for()"],
            },
            {
                "phase": "research",
                "action": "Find the root cause",
                "tools": ["ImportTracer.who_imports()", "PatternDetector.scan_file()"],
            },
            {
                "phase": "validate",
                "action": "Fix and validate",
                "tools": ["MutatorValidator.validate()", "OutputChecker.check()"],
            },
            {
                "phase": "monitor",
                "action": "Record the fix",
                "tools": ["ImprovementLog.add()", "SnapshotCollector.capture()"],
            },
        ],
    },
}


class WorkflowGuide:
    """Provide step-by-step workflow guidance for agents.

    Usage:
        guide = WorkflowGuide()

        # List available workflows
        workflows = guide.available()

        # Get a specific workflow
        wf = guide.get("new_category")

        # Generate instructions for an agent
        instructions = guide.instructions("new_category")

        # Get tools needed for a workflow
        tools = guide.tools_needed("new_category")
    """

    def available(self) -> list[dict[str, str]]:
        """List available workflows."""
        return [
            {"id": k, "title": v["title"], "description": v["description"]}
            for k, v in WORKFLOWS.items()
        ]

    def get(self, workflow_id: str) -> dict[str, Any] | None:
        """Get a specific workflow definition."""
        return WORKFLOWS.get(workflow_id)

    def instructions(self, workflow_id: str) -> str:
        """Generate step-by-step instructions for an agent."""
        wf = WORKFLOWS.get(workflow_id)
        if not wf:
            return f"Unknown workflow: {workflow_id}"

        lines = [
            f"# {wf['title']}",
            f"{wf['description']}",
            "",
        ]

        for i, step in enumerate(wf["steps"], 1):
            lines.append(f"## Step {i}: {step['action']} [{step['phase']}]")
            if "tools" in step:
                lines.append("**Tools:**")
                for tool in step["tools"]:
                    lines.append(f"- `{tool}`")
            if "code" in step:
                lines.append(f"```python\n{step['code']}\n```")
            lines.append("")

        return "\n".join(lines)

    def tools_needed(self, workflow_id: str) -> list[str]:
        """Get list of all tools needed for a workflow."""
        wf = WORKFLOWS.get(workflow_id)
        if not wf:
            return []

        tools: list[str] = []
        for step in wf["steps"]:
            tools.extend(step.get("tools", []))
        return tools

    def workflow_ids(self) -> list[str]:
        """List all workflow IDs."""
        return list(WORKFLOWS.keys())
