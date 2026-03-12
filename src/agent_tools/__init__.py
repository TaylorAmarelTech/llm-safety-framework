"""
Agent Improvement Tools

A toolkit designed to be harnessed by LLM coding agents (Claude Code, Cursor,
Aider, etc.) for autonomous framework improvement. Provides structured context,
code generation scaffolding, research tools, and validation utilities.

Sub-packages (20):
    context           — Project map, coding conventions, improvement history
    research          — Discover techniques, scan repos, analyze coverage gaps
    scaffolding       — Generate new mutator modules, tests, and categories from specs
    integration       — Evaluate and incorporate external libraries and GitHub repos
    validation        — Validate generated code, check coverage, score quality
    orchestrator      — Plan tasks, track execution, close the feedback loop
    codebase_explorer — Find files, index symbols, trace imports programmatically
    web_research      — Search papers, scan repos, track advisories
    code_analysis     — AST-based mutator analysis, complexity scoring, pattern detection
    sandbox           — Validate and safely execute generated code before integration
    prompt_library    — Reusable prompt templates for generation, analysis, and review
    diff_engine       — Build, preview, and apply structured code changes
    feedback_loop     — Collect execution results and feed back into planning
    metrics           — Track framework health and improvement trends over time
    session_state     — Track in-progress work and enable atomic rollback
    consistency       — Post-change cross-validation of framework integrity
    recommendation    — Smart "do this next" engine for agents
    test_fixtures     — Sample data and assertion helpers for rapid agent testing
    toolkit_docs      — Self-documenting toolkit introspection and capability matrix
    workflow_runner   — Chain tools together into repeatable pipelines

Quick start for an agent:

    from src.agent_tools.context.project_map import ProjectMap
    from src.agent_tools.research.gap_analyzer import GapAnalyzer
    from src.agent_tools.codebase_explorer import FileFinder, SymbolIndex
    from src.agent_tools.scaffolding.mutator_generator import MutatorGenerator
    from src.agent_tools.sandbox import CodeValidator, SafeExecutor
    from src.agent_tools.validation.mutator_validator import MutatorValidator
    from src.agent_tools.recommendation import Recommender
    from src.agent_tools.workflow_runner import Pipeline, PipelineRegistry

    # 1. Understand the project
    pmap = ProjectMap()
    print(pmap.summary())

    # 2. Explore the codebase
    finder = FileFinder()
    mutator_files = finder.mutator_modules()
    index = SymbolIndex()
    index.build()
    mutator_classes = index.classes_extending("BaseMutator")

    # 3. Find gaps and get recommendations
    gaps = GapAnalyzer().find_gaps()
    best = Recommender().next_action()

    # 4. Generate code for a new category
    gen = MutatorGenerator()
    code = gen.generate_module(spec)

    # 5. Validate before integrating
    validator_code = CodeValidator()
    result = validator_code.validate_mutator_module(code)

    executor = SafeExecutor()
    exec_result = executor.test_mutator(code, "MyMutator", "test prompt")

    # 6. Validate the integrated result
    validator = MutatorValidator()
    report = validator.validate_module(code)

    # 7. Run a pre-built pipeline
    registry = PipelineRegistry()
    health = registry.get("health_check")
    health.run()
"""

from __future__ import annotations

__all__ = [
    "context",
    "research",
    "scaffolding",
    "integration",
    "validation",
    "orchestrator",
    "codebase_explorer",
    "web_research",
    "code_analysis",
    "sandbox",
    "prompt_library",
    "diff_engine",
    "feedback_loop",
    "metrics",
    "session_state",
    "consistency",
    "recommendation",
    "test_fixtures",
    "toolkit_docs",
    "workflow_runner",
]
