"""
Capability matrix — map tools to agent workflow phases.

Organizes tools by which phase of the improvement workflow they
support (research, plan, generate, validate, integrate, monitor).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


WORKFLOW_PHASES = [
    "orient",     # Understand project state
    "research",   # Find gaps and new techniques
    "plan",       # Decide what to build
    "generate",   # Create code
    "validate",   # Check code quality
    "integrate",  # Register and connect
    "test",       # Run tests
    "monitor",    # Track metrics and trends
]

# Map tools to their primary and secondary phases
TOOL_PHASE_MAP: dict[str, dict[str, Any]] = {
    # orient
    "ProjectMap": {"primary": "orient", "secondary": ["research"]},
    "ConventionGuide": {"primary": "orient", "secondary": ["generate"]},
    "FileFinder": {"primary": "orient", "secondary": ["research", "validate"]},
    "SymbolIndex": {"primary": "orient", "secondary": ["research"]},
    "ImportTracer": {"primary": "orient", "secondary": ["validate"]},
    "HealthCheck": {"primary": "orient", "secondary": ["monitor"]},
    # research
    "GapAnalyzer": {"primary": "research", "secondary": ["plan"]},
    "TechniqueCatalog": {"primary": "research", "secondary": ["plan"]},
    "PaperSearcher": {"primary": "research", "secondary": []},
    "RepoScanner": {"primary": "research", "secondary": ["plan"]},
    "AdvisoryTracker": {"primary": "research", "secondary": ["plan"]},
    "MutatorAnalyzer": {"primary": "research", "secondary": ["orient"]},
    "ComplexityScorer": {"primary": "research", "secondary": ["validate"]},
    "PatternDetector": {"primary": "research", "secondary": ["validate"]},
    # plan
    "TaskPlanner": {"primary": "plan", "secondary": ["orient"]},
    "Recommender": {"primary": "plan", "secondary": ["research"]},
    "EffortEstimator": {"primary": "plan", "secondary": []},
    "ImpactScorer": {"primary": "plan", "secondary": ["research"]},
    "CategoryPlanner": {"primary": "plan", "secondary": ["generate"]},
    "PriorityAdjuster": {"primary": "plan", "secondary": ["monitor"]},
    # generate
    "MutatorGenerator": {"primary": "generate", "secondary": []},
    "TestGenerator": {"primary": "generate", "secondary": ["test"]},
    "AdapterFactory": {"primary": "generate", "secondary": ["integrate"]},
    "GenerationPrompts": {"primary": "generate", "secondary": []},
    "FixtureFactory": {"primary": "generate", "secondary": ["test"]},
    "ChangeBuilder": {"primary": "generate", "secondary": ["integrate"]},
    # validate
    "CodeValidator": {"primary": "validate", "secondary": ["generate"]},
    "SafeExecutor": {"primary": "validate", "secondary": ["test"]},
    "OutputChecker": {"primary": "validate", "secondary": ["test"]},
    "MutatorValidator": {"primary": "validate", "secondary": ["integrate"]},
    "QualityScorer": {"primary": "validate", "secondary": ["monitor"]},
    "CoverageChecker": {"primary": "validate", "secondary": ["monitor"]},
    # integrate
    "FilePatcher": {"primary": "integrate", "secondary": ["generate"]},
    "DiffPreviewer": {"primary": "integrate", "secondary": ["validate"]},
    "ImportChecker": {"primary": "integrate", "secondary": ["validate"]},
    "RegistrationChecker": {"primary": "integrate", "secondary": ["validate"]},
    "OrphanDetector": {"primary": "integrate", "secondary": ["validate"]},
    "RepoEvaluator": {"primary": "integrate", "secondary": ["research"]},
    "DependencyManager": {"primary": "integrate", "secondary": []},
    "Transaction": {"primary": "integrate", "secondary": ["validate"]},
    # test
    "SampleData": {"primary": "test", "secondary": ["generate"]},
    "AssertionHelpers": {"primary": "test", "secondary": []},
    # monitor
    "SnapshotCollector": {"primary": "monitor", "secondary": []},
    "TrendAnalyzer": {"primary": "monitor", "secondary": ["plan"]},
    "ResultCollector": {"primary": "monitor", "secondary": ["plan"]},
    "LearningStore": {"primary": "monitor", "secondary": ["plan"]},
    "ExecutionTracker": {"primary": "monitor", "secondary": ["plan"]},
    "SessionManager": {"primary": "monitor", "secondary": []},
    "ImprovementLog": {"primary": "monitor", "secondary": []},
}


@dataclass
class PhaseTools:
    """Tools available for a workflow phase."""

    phase: str
    primary_tools: list[str] = field(default_factory=list)
    secondary_tools: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "phase": self.phase,
            "primary_tools": self.primary_tools,
            "secondary_tools": self.secondary_tools,
        }


class CapabilityMatrix:
    """Map tools to workflow phases for agent navigation.

    Usage:
        matrix = CapabilityMatrix()

        # Get tools for a specific phase
        tools = matrix.tools_for("research")

        # Get the full matrix
        full = matrix.full_matrix()

        # Find what phase a tool belongs to
        phase = matrix.phase_of("GapAnalyzer")

        # Generate a capability overview
        overview = matrix.as_markdown()
    """

    def tools_for(self, phase: str) -> PhaseTools:
        """Get tools available for a specific workflow phase."""
        primary: list[str] = []
        secondary: list[str] = []

        for tool, info in TOOL_PHASE_MAP.items():
            if info["primary"] == phase:
                primary.append(tool)
            elif phase in info.get("secondary", []):
                secondary.append(tool)

        return PhaseTools(
            phase=phase,
            primary_tools=sorted(primary),
            secondary_tools=sorted(secondary),
        )

    def full_matrix(self) -> list[PhaseTools]:
        """Get the complete capability matrix."""
        return [self.tools_for(phase) for phase in WORKFLOW_PHASES]

    def phase_of(self, tool_name: str) -> str | None:
        """Find the primary phase for a tool."""
        info = TOOL_PHASE_MAP.get(tool_name)
        return info["primary"] if info else None

    def phases(self) -> list[str]:
        """List all workflow phases in order."""
        return list(WORKFLOW_PHASES)

    def as_markdown(self) -> str:
        """Generate a markdown capability matrix."""
        lines = ["# Capability Matrix\n"]
        lines.append("| Phase | Primary Tools | Secondary Tools |")
        lines.append("|-------|---------------|-----------------|")

        for pt in self.full_matrix():
            primary = ", ".join(pt.primary_tools) or "—"
            secondary = ", ".join(pt.secondary_tools[:5]) or "—"
            lines.append(f"| **{pt.phase}** | {primary} | {secondary} |")

        lines.append(f"\n**Total: {len(TOOL_PHASE_MAP)} tools across {len(WORKFLOW_PHASES)} phases**")
        return "\n".join(lines)
