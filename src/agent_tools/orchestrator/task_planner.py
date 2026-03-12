"""
Task planner — generate improvement tasks from gap analysis.

Combines gap analysis, technique catalog, and coverage data to produce
a prioritized list of improvement tasks that an agent can execute.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ImprovementTask:
    """A single improvement task for an agent to execute."""

    id: str
    priority: str  # "critical", "high", "medium", "low"
    kind: str  # "new_category", "new_mutator", "fix_bug", "add_test",
    #            "integrate_repo", "update_docs"
    title: str
    description: str
    steps: list[str] = field(default_factory=list)
    estimated_mutators: int = 0
    estimated_tests: int = 0
    files_to_create: list[str] = field(default_factory=list)
    files_to_modify: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "priority": self.priority,
            "kind": self.kind,
            "title": self.title,
            "description": self.description,
            "steps": self.steps,
            "estimated_mutators": self.estimated_mutators,
            "estimated_tests": self.estimated_tests,
            "files_to_create": self.files_to_create,
            "files_to_modify": self.files_to_modify,
        }

    def as_agent_prompt(self) -> str:
        """Format this task as an agent prompt."""
        lines = [
            f"# Task: {self.title}",
            f"Priority: {self.priority}",
            f"Kind: {self.kind}",
            "",
            self.description,
            "",
            "## Steps:",
        ]
        for i, step in enumerate(self.steps, 1):
            lines.append(f"{i}. {step}")

        if self.files_to_create:
            lines.append("\n## Files to create:")
            for f in self.files_to_create:
                lines.append(f"- {f}")

        if self.files_to_modify:
            lines.append("\n## Files to modify:")
            for f in self.files_to_modify:
                lines.append(f"- {f}")

        return "\n".join(lines)


class TaskPlanner:
    """Generate improvement tasks from gap analysis.

    Usage:
        planner = TaskPlanner()
        tasks = planner.plan()

        # Get just the top priority tasks
        critical = planner.critical_tasks()

        # Get tasks for a specific improvement area
        encoding_tasks = planner.tasks_for_area("encoding")
    """

    def plan(self, max_tasks: int = 20) -> list[ImprovementTask]:
        """Generate a prioritized task list."""
        tasks: list[ImprovementTask] = []
        task_id = 0

        # 1. Coverage gap tasks
        try:
            from src.agent_tools.research.gap_analyzer import GapAnalyzer

            analyzer = GapAnalyzer()
            report = analyzer.analyze()

            for gap in report.critical_gaps():
                if gap.kind == "uncovered_pair":
                    tasks.append(
                        ImprovementTask(
                            id=f"task_{task_id:03d}",
                            priority="critical",
                            kind="new_category",
                            title=f"Cover {gap.defense_layer} × {gap.technique_class}",
                            description=gap.recommendation,
                            steps=[
                                f"Create a category targeting {gap.defense_layer} with {gap.technique_class}",
                                "Write 10 mutators with 2 variants each",
                                "Add taxonomy entry to coverage.py",
                                "Register in __init__.py",
                                "Write tests",
                                "Run full test suite",
                            ],
                            estimated_mutators=10,
                            estimated_tests=50,
                            files_to_create=[
                                "src/prompt_injection/<new_category>.py",
                                "tests/test_<new_category>.py",
                            ],
                            files_to_modify=[
                                "src/prompt_injection/__init__.py",
                                "src/prompt_injection/coverage.py",
                            ],
                        )
                    )
                    task_id += 1
        except ImportError:
            pass

        # 2. Unimplemented technique tasks
        try:
            from src.agent_tools.research.technique_catalog import TechniqueCatalog

            catalog = TechniqueCatalog()
            for tech in catalog.priority_queue(10):
                tasks.append(
                    ImprovementTask(
                        id=f"task_{task_id:03d}",
                        priority="medium" if tech.complexity == "low" else "low",
                        kind="new_mutator",
                        title=f"Implement {tech.name}",
                        description=(
                            f"{tech.description}. "
                            f"Domain: {tech.domain}. "
                            f"Complexity: {tech.complexity}. "
                            f"Suggested category: {tech.suggested_category or 'TBD'}."
                        ),
                        steps=[
                            f"Research {tech.name} algorithm",
                            f"Add mutator to {tech.suggested_category or 'new category'}.py",
                            "Register with @register_mutator",
                            "Add tests",
                        ],
                        estimated_mutators=1,
                        estimated_tests=5,
                        context={
                            "technique_id": tech.id,
                            "references": tech.references,
                        },
                    )
                )
                task_id += 1
        except ImportError:
            pass

        # 3. Integration tasks (from known repos)
        try:
            from src.agent_tools.research.github_scanner import GitHubScanner

            scanner = GitHubScanner()
            for repo in scanner.known_repos(min_relevance=0.8):
                tasks.append(
                    ImprovementTask(
                        id=f"task_{task_id:03d}",
                        priority="medium",
                        kind="integrate_repo",
                        title=f"Integrate techniques from {repo.name}",
                        description=(
                            f"{repo.description}. "
                            f"Techniques: {', '.join(repo.techniques_found[:5])}. "
                            f"License: {repo.license}."
                        ),
                        steps=[
                            f"Study {repo.url}",
                            f"Identify techniques: {', '.join(repo.techniques_found)}",
                            "Create adapter or port algorithms",
                            "Register as new mutator category",
                            "Write tests",
                        ],
                        estimated_mutators=len(repo.techniques_found),
                        estimated_tests=len(repo.techniques_found) * 5,
                        context={
                            "repo_url": repo.url,
                            "techniques": repo.techniques_found,
                        },
                    )
                )
                task_id += 1
        except ImportError:
            pass

        # 4. Validation tasks
        tasks.append(
            ImprovementTask(
                id=f"task_{task_id:03d}",
                priority="low",
                kind="add_test",
                title="Validate all mutators handle edge cases",
                description="Run MutatorValidator on all registered mutators and fix any issues.",
                steps=[
                    "from src.agent_tools.validation import MutatorValidator",
                    "validator = MutatorValidator()",
                    "report = validator.validate_all()",
                    "Fix any errors in the report",
                ],
            )
        )
        task_id += 1

        # Sort by priority
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        tasks.sort(key=lambda t: priority_order.get(t.priority, 9))

        return tasks[:max_tasks]

    def critical_tasks(self) -> list[ImprovementTask]:
        """Get only critical and high priority tasks."""
        return [t for t in self.plan() if t.priority in ("critical", "high")]

    def tasks_for_area(self, area: str) -> list[ImprovementTask]:
        """Get tasks related to a specific area (encoding, cipher, etc.)."""
        area_lower = area.lower()
        return [
            t for t in self.plan()
            if area_lower in t.title.lower()
            or area_lower in t.description.lower()
        ]

    def next_task(self) -> ImprovementTask | None:
        """Get the single highest-priority task."""
        tasks = self.plan(max_tasks=1)
        return tasks[0] if tasks else None
