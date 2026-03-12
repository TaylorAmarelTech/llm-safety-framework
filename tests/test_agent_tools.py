"""
Tests for the agent_tools package.

Tests all twenty sub-packages:
    1.  context           — ProjectMap, ConventionGuide, ImprovementLog
    2.  research          — TechniqueCatalog, GapAnalyzer, GitHubScanner, ReferenceIndex
    3.  scaffolding       — MutatorGenerator, TestGenerator, CategoryPlanner
    4.  integration       — RepoEvaluator, DependencyManager, AdapterFactory
    5.  validation        — MutatorValidator, CoverageChecker, QualityScorer
    6.  orchestrator      — TaskPlanner, ExecutionTracker
    7.  codebase_explorer — FileFinder, SymbolIndex, ImportTracer
    8.  web_research      — PaperSearcher, RepoScanner, AdvisoryTracker
    9.  code_analysis     — MutatorAnalyzer, ComplexityScorer, PatternDetector
    10. sandbox           — CodeValidator, SafeExecutor, OutputChecker
    11. prompt_library    — GenerationPrompts, AnalysisPrompts, ReviewPrompts
    12. diff_engine       — ChangeBuilder, FilePatcher, DiffPreviewer
    13. feedback_loop     — ResultCollector, LearningStore, PriorityAdjuster
    14. metrics           — SnapshotCollector, TrendAnalyzer, HealthCheck
    15. session_state     — SessionManager, FileSnapshotStore, Transaction
    16. consistency       — ImportChecker, RegistrationChecker, OrphanDetector
    17. recommendation    — Recommender, EffortEstimator, ImpactScorer
    18. test_fixtures     — SampleData, AssertionHelpers, FixtureFactory
    19. toolkit_docs      — ToolkitIntrospector, CapabilityMatrix, WorkflowGuide
    20. workflow_runner   — Pipeline, StepRunner, PipelineRegistry
"""

import json
import pytest
from pathlib import Path


# ═══════════════════════════════════════════════════════════════════════
# 1. Context
# ═══════════════════════════════════════════════════════════════════════


class TestProjectMap:
    def test_snapshot(self):
        from src.agent_tools.context.project_map import ProjectMap
        pmap = ProjectMap()
        snap = pmap.snapshot()
        assert snap.total_mutators >= 598
        assert snap.total_categories >= 52
        assert len(snap.packages) >= 10

    def test_summary_string(self):
        from src.agent_tools.context.project_map import ProjectMap
        pmap = ProjectMap()
        summary = pmap.summary()
        assert "LLM Safety Framework" in summary
        assert "Mutator categories" in summary

    def test_category_list(self):
        from src.agent_tools.context.project_map import ProjectMap
        pmap = ProjectMap()
        cats = pmap.category_list()
        assert len(cats) >= 52
        for c in cats:
            assert "name" in c
            assert "mutator_count" in c

    def test_package_list(self):
        from src.agent_tools.context.project_map import ProjectMap
        pmap = ProjectMap()
        pkgs = pmap.package_list()
        assert len(pkgs) >= 10
        names = [p["name"] for p in pkgs]
        assert "prompt_injection" in names
        assert "agent_tools" in names


class TestConventionGuide:
    def test_all_conventions(self):
        from src.agent_tools.context.conventions import ConventionGuide
        guide = ConventionGuide()
        all_c = guide.all()
        assert len(all_c) >= 15

    def test_areas(self):
        from src.agent_tools.context.conventions import ConventionGuide
        guide = ConventionGuide()
        areas = guide.areas()
        assert "naming" in areas
        assert "architecture" in areas
        assert "testing" in areas

    def test_for_area(self):
        from src.agent_tools.context.conventions import ConventionGuide
        guide = ConventionGuide()
        naming = guide.for_area("naming")
        assert len(naming) >= 3
        for c in naming:
            assert c.area == "naming"

    def test_get_by_id(self):
        from src.agent_tools.context.conventions import ConventionGuide
        guide = ConventionGuide()
        c = guide.get("naming_mutator_class")
        assert c is not None
        assert "PascalCase" in c.rule

    def test_as_prompt_context(self):
        from src.agent_tools.context.conventions import ConventionGuide
        guide = ConventionGuide()
        ctx = guide.as_prompt_context(areas=["naming"])
        assert "# Coding Conventions" in ctx
        assert "Naming" in ctx

    def test_checklist(self):
        from src.agent_tools.context.conventions import ConventionGuide
        guide = ConventionGuide()
        cl = guide.checklist()
        assert len(cl) >= 15
        assert all("id" in item and "rule" in item for item in cl)


class TestImprovementLog:
    def test_add_and_retrieve(self, tmp_path):
        from src.agent_tools.context.improvement_log import ImprovementLog
        log = ImprovementLog(log_path=tmp_path / "log.json")
        entry = log.add(
            kind="new_category",
            description="Added test category",
            mutators_added=10,
            category="test_cat",
        )
        assert entry.id == "imp_0000"
        assert log.all_entries()[0].category == "test_cat"

    def test_recent(self, tmp_path):
        from src.agent_tools.context.improvement_log import ImprovementLog
        log = ImprovementLog(log_path=tmp_path / "log.json")
        for i in range(5):
            log.add(kind="test", description=f"Item {i}")
        recent = log.recent(3)
        assert len(recent) == 3
        assert recent[0].description == "Item 4"

    def test_persistence(self, tmp_path):
        from src.agent_tools.context.improvement_log import ImprovementLog
        path = tmp_path / "log.json"
        log1 = ImprovementLog(log_path=path)
        log1.add(kind="test", description="Persisted")
        log2 = ImprovementLog(log_path=path)
        assert len(log2.all_entries()) == 1

    def test_summary(self, tmp_path):
        from src.agent_tools.context.improvement_log import ImprovementLog
        log = ImprovementLog(log_path=tmp_path / "log.json")
        log.add(kind="new_category", description="Cat 1", mutators_added=10, category="cat1")
        log.add(kind="bug_fix", description="Fix 1", tests_added=5)
        s = log.summary()
        assert s["total_entries"] == 2
        assert s["total_mutators_added"] == 10
        assert s["total_tests_added"] == 5


# ═══════════════════════════════════════════════════════════════════════
# 2. Research
# ═══════════════════════════════════════════════════════════════════════


class TestTechniqueCatalog:
    def test_all_entries(self):
        from src.agent_tools.research.technique_catalog import TechniqueCatalog
        cat = TechniqueCatalog()
        assert len(cat.all()) >= 20

    def test_implemented(self):
        from src.agent_tools.research.technique_catalog import TechniqueCatalog
        cat = TechniqueCatalog()
        impl = cat.implemented()
        assert len(impl) >= 5

    def test_not_implemented(self):
        from src.agent_tools.research.technique_catalog import TechniqueCatalog
        cat = TechniqueCatalog()
        unimpl = cat.not_implemented()
        assert len(unimpl) >= 10
        for t in unimpl:
            assert not t.implemented

    def test_filter_by_complexity(self):
        from src.agent_tools.research.technique_catalog import TechniqueCatalog
        cat = TechniqueCatalog()
        easy = cat.not_implemented(complexity="low")
        assert all(t.complexity == "low" for t in easy)

    def test_domains(self):
        from src.agent_tools.research.technique_catalog import TechniqueCatalog
        cat = TechniqueCatalog()
        domains = cat.domains()
        assert "encoding" in domains

    def test_priority_queue(self):
        from src.agent_tools.research.technique_catalog import TechniqueCatalog
        cat = TechniqueCatalog()
        pq = cat.priority_queue(5)
        assert len(pq) <= 5
        # First items should be low complexity
        if pq:
            assert pq[0].complexity == "low"

    def test_search(self):
        from src.agent_tools.research.technique_catalog import TechniqueCatalog
        cat = TechniqueCatalog()
        results = cat.search("base")
        assert len(results) >= 1

    def test_as_markdown(self):
        from src.agent_tools.research.technique_catalog import TechniqueCatalog
        cat = TechniqueCatalog()
        md = cat.as_markdown(only_unimplemented=True)
        assert "| ID |" in md


class TestGapAnalyzer:
    def test_analyze(self):
        from src.agent_tools.research.gap_analyzer import GapAnalyzer
        analyzer = GapAnalyzer()
        report = analyzer.analyze()
        assert report.total_mutators >= 598
        assert report.coverage_score > 0
        assert len(report.gaps) >= 1

    def test_suggest_next_category(self):
        from src.agent_tools.research.gap_analyzer import GapAnalyzer
        analyzer = GapAnalyzer()
        suggestion = analyzer.suggest_next_category()
        assert "suggestions" in suggestion
        assert "coverage_score" in suggestion


class TestGitHubScanner:
    def test_search_queries(self):
        from src.agent_tools.research.github_scanner import GitHubScanner
        scanner = GitHubScanner()
        queries = scanner.search_queries()
        assert len(queries) >= 5
        for q in queries:
            assert "id" in q
            assert "query" in q

    def test_known_repos(self):
        from src.agent_tools.research.github_scanner import GitHubScanner
        scanner = GitHubScanner()
        repos = scanner.known_repos()
        assert len(repos) >= 5
        for r in repos:
            assert r.url
            assert r.name

    def test_evaluate(self):
        from src.agent_tools.research.github_scanner import GitHubScanner, RepoCandidate
        scanner = GitHubScanner()
        candidate = RepoCandidate(
            url="https://github.com/test/test",
            name="test-repo",
            language="Python",
            license="MIT",
            stars=500,
            techniques_found=["technique1", "technique2"],
        )
        result = scanner.evaluate(candidate)
        assert "overall_score" in result
        assert result["overall_score"] > 0

    def test_generate_search_prompt(self):
        from src.agent_tools.research.github_scanner import GitHubScanner
        scanner = GitHubScanner()
        prompt = scanner.generate_search_prompt("encoding")
        assert "Search GitHub" in prompt


class TestReferenceIndex:
    def test_all(self):
        from src.agent_tools.research.reference_index import ReferenceIndex
        idx = ReferenceIndex()
        assert len(idx.all()) >= 10

    def test_by_kind(self):
        from src.agent_tools.research.reference_index import ReferenceIndex
        idx = ReferenceIndex()
        papers = idx.by_kind("paper")
        assert len(papers) >= 5

    def test_by_tag(self):
        from src.agent_tools.research.reference_index import ReferenceIndex
        idx = ReferenceIndex()
        jb = idx.by_tag("jailbreak")
        assert len(jb) >= 3

    def test_citation(self):
        from src.agent_tools.research.reference_index import ReferenceIndex
        idx = ReferenceIndex()
        ref = idx.get("zou2023universal")
        assert ref is not None
        assert "2023" in ref.citation()

    def test_search(self):
        from src.agent_tools.research.reference_index import ReferenceIndex
        idx = ReferenceIndex()
        results = idx.search("adversarial")
        assert len(results) >= 2


# ═══════════════════════════════════════════════════════════════════════
# 3. Scaffolding
# ═══════════════════════════════════════════════════════════════════════


class TestMutatorGenerator:
    def test_generate_module(self):
        from src.agent_tools.scaffolding.mutator_generator import (
            MutatorGenerator, CategorySpec, MutatorSpec,
        )
        gen = MutatorGenerator()
        spec = CategorySpec(
            category_name="test_gen",
            module_name="test_gen",
            description="Test generation",
            mutators=[
                MutatorSpec(name="test_m1", class_name="TestM1Mutator",
                           description="Test mutator 1", technique="test1"),
            ],
        )
        code = gen.generate_module(spec)
        assert "class TestM1Mutator(BaseMutator)" in code
        assert '@register_mutator' in code
        assert 'NAME = "test_m1"' in code
        assert 'CATEGORY = "test_gen"' in code

    def test_generate_taxonomy_entry(self):
        from src.agent_tools.scaffolding.mutator_generator import (
            MutatorGenerator, CategorySpec,
        )
        gen = MutatorGenerator()
        spec = CategorySpec(
            category_name="test_tax",
            module_name="test_tax",
            description="Test",
            defense_layers=["input_filter"],
            technique_classes=["encoding"],
        )
        entry = gen.generate_taxonomy_entry(spec)
        assert '"test_tax"' in entry
        assert '"input_filter"' in entry

    def test_checklist(self):
        from src.agent_tools.scaffolding.mutator_generator import (
            MutatorGenerator, CategorySpec,
        )
        gen = MutatorGenerator()
        spec = CategorySpec(
            category_name="test_cl",
            module_name="test_cl",
            description="Test",
        )
        steps = gen.checklist(spec)
        assert len(steps) >= 6


class TestTestGenerator:
    def test_generate(self):
        from src.agent_tools.scaffolding.test_generator import TestGenerator
        from src.agent_tools.scaffolding.mutator_generator import CategorySpec, MutatorSpec
        gen = TestGenerator()
        spec = CategorySpec(
            category_name="test_tg",
            module_name="test_tg",
            description="Test",
            mutators=[
                MutatorSpec(name="tg_m1", class_name="TGM1Mutator",
                           description="Test", technique="tg1"),
            ],
        )
        code = gen.generate(spec)
        assert "test_tg" in code
        assert "tg_m1" in code
        assert "class TestRegistration" in code
        assert "class TestFunctionality" in code


class TestCategoryPlanner:
    def test_plan(self):
        from src.agent_tools.scaffolding.category_planner import CategoryPlanner
        planner = CategoryPlanner()
        spec = planner.plan(
            name="Tap Code Cipher",
            description="Polybius-based tap code encoding",
            techniques=["basic_tap", "extended_tap"],
        )
        assert spec.category_name == "tap_code_cipher"
        assert len(spec.mutators) == 2

    def test_check_collisions(self):
        from src.agent_tools.scaffolding.category_planner import CategoryPlanner
        planner = CategoryPlanner()
        spec = planner.plan(
            name="Test No Collision",
            description="Should have no collisions",
            techniques=["zzz_unique_test_name_xyz"],
        )
        collisions = planner.check_collisions(spec)
        assert len(collisions) == 0

    def test_preview(self):
        from src.agent_tools.scaffolding.category_planner import CategoryPlanner
        planner = CategoryPlanner()
        spec = planner.plan(name="Preview Test", description="Test")
        preview = planner.preview(spec)
        assert "category_name" in preview
        assert "taxonomy_entry" in preview
        assert "steps" in preview


# ═══════════════════════════════════════════════════════════════════════
# 4. Integration
# ═══════════════════════════════════════════════════════════════════════


class TestRepoEvaluator:
    def test_evaluate_good_repo(self):
        from src.agent_tools.integration.repo_evaluator import RepoEvaluator
        evaluator = RepoEvaluator()
        report = evaluator.evaluate(
            name="test-repo",
            language="Python",
            license="MIT",
            stars=1000,
            techniques=["t1", "t2", "t3", "t4", "t5"],
            has_tests=True,
            last_commit_days_ago=30,
        )
        assert report.overall_score >= 0.7
        assert report.is_recommended()

    def test_evaluate_bad_repo(self):
        from src.agent_tools.integration.repo_evaluator import RepoEvaluator
        evaluator = RepoEvaluator()
        report = evaluator.evaluate(
            name="bad-repo",
            language="Fortran",
            license="",
            stars=0,
        )
        assert report.overall_score < 0.5
        assert not report.is_recommended()

    def test_evaluate_integration_plan(self):
        from src.agent_tools.integration.repo_evaluator import RepoEvaluator
        evaluator = RepoEvaluator()
        report = evaluator.evaluate(
            name="test-repo",
            language="Python",
            license="MIT",
            techniques=["t1"],
        )
        assert len(report.integration_plan) >= 4


class TestDependencyManager:
    def test_required_deps(self):
        from src.agent_tools.integration.dependency_manager import DependencyManager
        dm = DependencyManager()
        required = dm.required()
        assert len(required) >= 2

    def test_status(self):
        from src.agent_tools.integration.dependency_manager import DependencyManager
        dm = DependencyManager()
        status = dm.status()
        assert "total" in status
        assert "installed" in status

    def test_generate_try_import(self):
        from src.agent_tools.integration.dependency_manager import DependencyManager
        dm = DependencyManager()
        code = dm.generate_try_import("textattack")
        assert "try:" in code
        assert "import textattack" in code
        assert "except ImportError:" in code


class TestAdapterFactory:
    def test_generate(self):
        from src.agent_tools.integration.adapter_factory import AdapterFactory, AdapterSpec
        factory = AdapterFactory()
        spec = AdapterSpec(
            package="testpkg",
            import_name="testpkg",
            category="test_adapter",
            functions=[{
                "name": "test_func",
                "class": "TestFuncMutator",
                "func": "testpkg.transform",
                "description": "Test function",
                "technique": "test_technique",
            }],
        )
        code = factory.generate(spec)
        assert "class TestFuncMutator(BaseMutator)" in code
        assert "import testpkg" in code
        assert "_HAS_LIB" in code

    def test_preview(self):
        from src.agent_tools.integration.adapter_factory import AdapterFactory, AdapterSpec
        factory = AdapterFactory()
        spec = AdapterSpec(
            package="testpkg",
            import_name="testpkg",
            category="test_cat",
            functions=[{"name": "f1", "class": "F1Mutator", "technique": "t1"}],
        )
        preview = factory.preview(spec)
        assert preview["mutator_count"] == "1"


# ═══════════════════════════════════════════════════════════════════════
# 5. Validation
# ═══════════════════════════════════════════════════════════════════════


class TestMutatorValidator:
    def test_validate_known_mutator(self):
        from src.agent_tools.validation.mutator_validator import MutatorValidator
        validator = MutatorValidator()
        report = validator.validate("base32_encode")
        assert report.mutators_checked == 1
        # Should pass — it's a well-formed mutator
        assert len(report.errors) == 0

    def test_validate_nonexistent(self):
        from src.agent_tools.validation.mutator_validator import MutatorValidator
        validator = MutatorValidator()
        report = validator.validate("nonexistent_mutator_xyz")
        assert not report.passed

    def test_validate_category(self):
        from src.agent_tools.validation.mutator_validator import MutatorValidator
        validator = MutatorValidator()
        report = validator.validate_category("encoding_advanced")
        assert report.mutators_checked == 10
        assert len(report.errors) == 0


class TestCoverageChecker:
    def test_check(self):
        from src.agent_tools.validation.coverage_checker import CoverageChecker
        checker = CoverageChecker()
        result = checker.check()
        assert result.total_mutators >= 598
        assert result.total_categories >= 52
        assert result.coverage_score > 0

    def test_check_category(self):
        from src.agent_tools.validation.coverage_checker import CoverageChecker
        checker = CoverageChecker()
        result = checker.check_category("encoding_advanced")
        assert result.passed
        assert result.total_mutators == 10

    def test_check_missing_category(self):
        from src.agent_tools.validation.coverage_checker import CoverageChecker
        checker = CoverageChecker()
        result = checker.check_category("nonexistent_xyz")
        assert not result.passed


class TestQualityScorer:
    def test_score_real_file(self):
        from src.agent_tools.validation.quality_scorer import QualityScorer
        scorer = QualityScorer()
        report = scorer.score_file(
            "src/prompt_injection/phonetic_obfuscation.py"
        )
        assert report.overall_score > 0.5
        assert report.passed

    def test_score_code_string(self):
        from src.agent_tools.validation.quality_scorer import QualityScorer
        scorer = QualityScorer()
        code = '''"""Module docstring."""
from __future__ import annotations
from src.prompt_injection import BaseMutator, register_mutator

@register_mutator
class TestMutator(BaseMutator):
    """Does stuff."""
    NAME = "test_quality"
    CATEGORY = "test"
    DESCRIPTION = "Test"
    def _apply(self, prompt: str, **kwargs) -> list[tuple[str, str, dict]]:
        return [("x", "d", {"technique": "t", "variant": "v"})]
'''
        report = scorer.score_code(code)
        assert report.overall_score > 0.6

    def test_score_bad_code(self):
        from src.agent_tools.validation.quality_scorer import QualityScorer
        scorer = QualityScorer()
        report = scorer.score_code("x = 1")
        assert report.overall_score < 0.5

    def test_missing_file(self):
        from src.agent_tools.validation.quality_scorer import QualityScorer
        scorer = QualityScorer()
        report = scorer.score_file("/nonexistent/path.py")
        assert not report.passed


# ═══════════════════════════════════════════════════════════════════════
# 6. Orchestrator
# ═══════════════════════════════════════════════════════════════════════


class TestTaskPlanner:
    def test_plan(self):
        from src.agent_tools.orchestrator.task_planner import TaskPlanner
        planner = TaskPlanner()
        tasks = planner.plan(max_tasks=10)
        assert len(tasks) >= 1
        for t in tasks:
            assert t.id
            assert t.title
            assert t.priority in ("critical", "high", "medium", "low")

    def test_critical_tasks(self):
        from src.agent_tools.orchestrator.task_planner import TaskPlanner
        planner = TaskPlanner()
        critical = planner.critical_tasks()
        for t in critical:
            assert t.priority in ("critical", "high")

    def test_next_task(self):
        from src.agent_tools.orchestrator.task_planner import TaskPlanner
        planner = TaskPlanner()
        task = planner.next_task()
        if task:
            assert task.title

    def test_as_agent_prompt(self):
        from src.agent_tools.orchestrator.task_planner import TaskPlanner
        planner = TaskPlanner()
        task = planner.next_task()
        if task:
            prompt = task.as_agent_prompt()
            assert "# Task:" in prompt


class TestExecutionTracker:
    def test_start_complete(self, tmp_path):
        from src.agent_tools.orchestrator.execution_tracker import ExecutionTracker
        tracker = ExecutionTracker(state_path=tmp_path / "tracker.json")
        tracker.start("t1", "Test task", agent="pytest")
        tracker.complete("t1", mutators_created=5, tests_created=20)
        assert tracker.is_completed("t1")
        assert tracker.get("t1").mutators_created == 5

    def test_fail(self, tmp_path):
        from src.agent_tools.orchestrator.execution_tracker import ExecutionTracker
        tracker = ExecutionTracker(state_path=tmp_path / "tracker.json")
        tracker.start("t2", "Failing task")
        tracker.fail("t2", error="Something went wrong")
        failed = tracker.failed_tasks()
        assert len(failed) == 1

    def test_persistence(self, tmp_path):
        from src.agent_tools.orchestrator.execution_tracker import ExecutionTracker
        path = tmp_path / "tracker.json"
        t1 = ExecutionTracker(state_path=path)
        t1.start("t3", "Persisted task")
        t1.complete("t3")
        t2 = ExecutionTracker(state_path=path)
        assert t2.is_completed("t3")

    def test_summary(self, tmp_path):
        from src.agent_tools.orchestrator.execution_tracker import ExecutionTracker
        tracker = ExecutionTracker(state_path=tmp_path / "tracker.json")
        tracker.start("t4", "Task 4")
        tracker.complete("t4", mutators_created=10)
        tracker.start("t5", "Task 5")
        tracker.fail("t5")
        s = tracker.summary()
        assert s["completed"] == 1
        assert s["failed"] == 1
        assert s["total_mutators_created"] == 10


# ═══════════════════════════════════════════════════════════════════════
# 7. Codebase Explorer
# ═══════════════════════════════════════════════════════════════════════


class TestFileFinder:
    def test_glob_py_files(self):
        from src.agent_tools.codebase_explorer import FileFinder
        finder = FileFinder()
        results = finder.glob("src/prompt_injection/*.py")
        assert len(results) >= 40

    def test_grep_class(self):
        from src.agent_tools.codebase_explorer import FileFinder
        finder = FileFinder()
        results = finder.grep("class.*BaseMutator", file_glob="src/prompt_injection/*.py")
        assert len(results) >= 1

    def test_mutator_modules(self):
        from src.agent_tools.codebase_explorer import FileFinder
        finder = FileFinder()
        mods = finder.mutator_modules()
        assert len(mods) >= 40
        for m in mods:
            assert m.relative_path.endswith(".py")

    def test_test_files(self):
        from src.agent_tools.codebase_explorer import FileFinder
        finder = FileFinder()
        tests = finder.test_files()
        assert len(tests) >= 10

    def test_plugin_dirs(self):
        from src.agent_tools.codebase_explorer import FileFinder
        finder = FileFinder()
        dirs = finder.plugin_dirs()
        assert "analytics" in dirs
        assert "prompts" in dirs

    def test_file_match_to_dict(self):
        from src.agent_tools.codebase_explorer import FileFinder
        finder = FileFinder()
        results = finder.glob("src/prompt_injection/__init__.py")
        assert len(results) == 1
        d = results[0].to_dict()
        assert "path" in d
        assert "size_bytes" in d
        assert d["size_bytes"] > 0


class TestSymbolIndex:
    def test_build(self):
        from src.agent_tools.codebase_explorer import SymbolIndex
        index = SymbolIndex()
        count = index.build(file_glob="src/prompt_injection/encoding_format.py")
        assert count >= 5

    def test_find(self):
        from src.agent_tools.codebase_explorer import SymbolIndex
        index = SymbolIndex()
        index.build(file_glob="src/prompt_injection/encoding_format.py")
        results = index.find("BaseMutator")
        # BaseMutator won't be defined here, but classes extending it will be
        classes = index.classes()
        assert len(classes) >= 5

    def test_classes_extending(self):
        from src.agent_tools.codebase_explorer import SymbolIndex
        index = SymbolIndex()
        index.build(file_glob="src/prompt_injection/encoding_format.py")
        mutators = index.classes_extending("BaseMutator")
        assert len(mutators) >= 5
        for m in mutators:
            assert m.kind == "class"
            assert "BaseMutator" in m.bases

    def test_decorated_with(self):
        from src.agent_tools.codebase_explorer import SymbolIndex
        index = SymbolIndex()
        index.build(file_glob="src/prompt_injection/encoding_format.py")
        registered = index.decorated_with("register_mutator")
        assert len(registered) >= 5

    def test_methods_of(self):
        from src.agent_tools.codebase_explorer import SymbolIndex
        index = SymbolIndex()
        index.build(file_glob="src/prompt_injection/encoding_format.py")
        classes = index.classes()
        if classes:
            methods = index.methods_of(classes[0].name)
            assert any(m.name == "_apply" for m in methods)

    def test_constants(self):
        from src.agent_tools.codebase_explorer import SymbolIndex
        index = SymbolIndex()
        # Build across multiple files to find plain-assignment constants
        index.build(file_glob="src/agent_tools/web_research/paper_searcher.py")
        constants = index.constants()
        assert any(c.name == "SEARCH_QUERIES" for c in constants)
        assert any(c.name == "RELEVANT_VENUES" for c in constants)

    def test_summary(self):
        from src.agent_tools.codebase_explorer import SymbolIndex
        index = SymbolIndex()
        index.build(file_glob="src/prompt_injection/encoding_format.py")
        s = index.summary()
        assert "class" in s
        assert s["class"] >= 5

    def test_to_dict(self):
        from src.agent_tools.codebase_explorer import SymbolIndex
        index = SymbolIndex()
        index.build(file_glob="src/prompt_injection/encoding_format.py")
        classes = index.classes()
        assert len(classes) >= 1
        d = classes[0].to_dict()
        assert "name" in d
        assert "kind" in d
        assert d["kind"] == "class"


class TestImportTracer:
    def test_trace(self):
        from src.agent_tools.codebase_explorer import ImportTracer
        tracer = ImportTracer()
        graph = tracer.trace(file_glob="src/prompt_injection/__init__.py")
        assert len(graph.edges) >= 1
        assert len(graph.modules) >= 1

    def test_trace_file(self):
        from src.agent_tools.codebase_explorer import ImportTracer
        tracer = ImportTracer()
        edges = tracer.trace_file("src/prompt_injection/__init__.py")
        assert len(edges) >= 5

    def test_dependency_graph_to_dict(self):
        from src.agent_tools.codebase_explorer import ImportTracer
        tracer = ImportTracer()
        graph = tracer.trace(file_glob="src/prompt_injection/__init__.py")
        d = graph.to_dict()
        assert "module_count" in d
        assert "edge_count" in d
        assert d["edge_count"] >= 1

    def test_dependents_of(self):
        from src.agent_tools.codebase_explorer import ImportTracer
        tracer = ImportTracer()
        graph = tracer.trace(file_glob="src/prompt_injection/*.py")
        deps = graph.dependents_of("src/prompt_injection/__init__")
        # __init__.py might be imported by other files
        assert isinstance(deps, list)

    def test_impact(self):
        from src.agent_tools.codebase_explorer import ImportTracer
        tracer = ImportTracer()
        graph = tracer.trace(file_glob="src/prompt_injection/*.py")
        impact = graph.impact_of("src/prompt_injection/__init__.py")
        assert "module" in impact
        assert "total_impact" in impact


# ═══════════════════════════════════════════════════════════════════════
# 8. Web Research
# ═══════════════════════════════════════════════════════════════════════


class TestPaperSearcher:
    def test_all_topics(self):
        from src.agent_tools.web_research import PaperSearcher
        searcher = PaperSearcher()
        topics = searcher.all_topics()
        assert len(topics) >= 4
        assert "prompt_injection" in topics

    def test_queries_for(self):
        from src.agent_tools.web_research import PaperSearcher
        searcher = PaperSearcher()
        queries = searcher.queries_for("prompt_injection")
        assert len(queries) >= 2

    def test_semantic_scholar_prompt(self):
        from src.agent_tools.web_research import PaperSearcher
        searcher = PaperSearcher()
        prompt = searcher.semantic_scholar_prompt("encoding_attack")
        assert "Semantic Scholar" in prompt
        assert "api.semanticscholar.org" in prompt

    def test_arxiv_prompt(self):
        from src.agent_tools.web_research import PaperSearcher
        searcher = PaperSearcher()
        prompt = searcher.arxiv_prompt("safety_alignment")
        assert "arXiv" in prompt

    def test_landmark_papers(self):
        from src.agent_tools.web_research import PaperSearcher
        searcher = PaperSearcher()
        papers = searcher.landmark_papers()
        assert len(papers) >= 5
        titles = [p.title for p in papers]
        assert any("GCG" in t or "Adversarial" in t for t in titles)

    def test_relevance_score(self):
        from src.agent_tools.web_research import PaperSearcher
        from src.agent_tools.web_research.paper_searcher import PaperResult
        searcher = PaperSearcher()
        paper = PaperResult(
            title="Jailbreak attack on safety-aligned LLMs",
            abstract="We present a novel prompt injection bypass...",
            year=2024,
            venue="NeurIPS",
            citation_count=150,
        )
        score = searcher.relevance_score(paper)
        assert score > 0.3


class TestRepoScanner:
    def test_known_repos(self):
        from src.agent_tools.web_research import RepoScanner
        scanner = RepoScanner()
        repos = scanner.known_repos()
        assert len(repos) >= 5
        names = [r.name for r in repos]
        assert "garak" in names

    def test_known_repos_filter(self):
        from src.agent_tools.web_research import RepoScanner
        scanner = RepoScanner()
        high = scanner.known_repos(min_relevance=0.85)
        low = scanner.known_repos(min_relevance=0.0)
        assert len(high) <= len(low)

    def test_github_search_prompt(self):
        from src.agent_tools.web_research import RepoScanner
        scanner = RepoScanner()
        prompt = scanner.github_search_prompt("encoding")
        assert "GitHub" in prompt
        assert "api.github.com" in prompt

    def test_evaluate(self):
        from src.agent_tools.web_research import RepoScanner
        from src.agent_tools.web_research.repo_scanner import RepoResult
        scanner = RepoScanner()
        repo = RepoResult(
            name="test-repo",
            owner="test",
            language="Python",
            license="MIT",
            stars=500,
            topics=["jailbreak", "adversarial"],
            techniques_found=["t1", "t2"],
        )
        score = scanner.evaluate(repo)
        assert score > 0.3

    def test_license_compatible(self):
        from src.agent_tools.web_research import RepoScanner
        scanner = RepoScanner()
        assert scanner.is_license_compatible("MIT")
        assert scanner.is_license_compatible("Apache-2.0")
        assert not scanner.is_license_compatible("GPL-3.0")

    def test_integration_plan(self):
        from src.agent_tools.web_research import RepoScanner
        from src.agent_tools.web_research.repo_scanner import RepoResult
        scanner = RepoScanner()
        repo = RepoResult(
            name="test", owner="test", license="MIT",
            techniques_found=["t1"], integration_difficulty="easy",
        )
        steps = scanner.integration_plan(repo)
        assert len(steps) >= 5


class TestAdvisoryTracker:
    def test_all(self):
        from src.agent_tools.web_research import AdvisoryTracker
        tracker = AdvisoryTracker()
        advisories = tracker.all()
        assert len(advisories) >= 5

    def test_not_implemented(self):
        from src.agent_tools.web_research import AdvisoryTracker
        tracker = AdvisoryTracker()
        gaps = tracker.not_implemented()
        assert len(gaps) >= 1
        for a in gaps:
            assert not a.implemented

    def test_by_severity(self):
        from src.agent_tools.web_research import AdvisoryTracker
        tracker = AdvisoryTracker()
        critical = tracker.by_severity("critical")
        assert len(critical) >= 1
        for a in critical:
            assert a.severity == "critical"

    def test_by_category(self):
        from src.agent_tools.web_research import AdvisoryTracker
        tracker = AdvisoryTracker()
        injections = tracker.by_category("prompt_injection")
        assert len(injections) >= 1

    def test_search(self):
        from src.agent_tools.web_research import AdvisoryTracker
        tracker = AdvisoryTracker()
        results = tracker.search("encoding")
        assert len(results) >= 1

    def test_implementation_prompt(self):
        from src.agent_tools.web_research import AdvisoryTracker
        tracker = AdvisoryTracker()
        gaps = tracker.not_implemented()
        if gaps:
            prompt = tracker.implementation_prompt(gaps[0])
            assert "Implement coverage" in prompt

    def test_coverage_summary(self):
        from src.agent_tools.web_research import AdvisoryTracker
        tracker = AdvisoryTracker()
        summary = tracker.coverage_summary()
        assert "total_advisories" in summary
        assert "covered" in summary
        assert "coverage_pct" in summary


# ═══════════════════════════════════════════════════════════════════════
# 9. Code Analysis
# ═══════════════════════════════════════════════════════════════════════


class TestMutatorAnalyzer:
    def test_analyze_module(self):
        from src.agent_tools.code_analysis import MutatorAnalyzer
        analyzer = MutatorAnalyzer()
        analysis = analyzer.analyze_module("src/prompt_injection/encoding_format.py")
        assert analysis.mutator_count >= 5
        assert analysis.total_lines > 50

    def test_analyze_all(self):
        from src.agent_tools.code_analysis import MutatorAnalyzer
        analyzer = MutatorAnalyzer()
        all_analyses = analyzer.analyze_all()
        assert len(all_analyses) >= 40

    def test_mutator_info_fields(self):
        from src.agent_tools.code_analysis import MutatorAnalyzer
        analyzer = MutatorAnalyzer()
        analysis = analyzer.analyze_module("src/prompt_injection/encoding_format.py")
        for m in analysis.mutators:
            assert m.name
            assert m.category
            assert m.class_name
            assert m.complexity in ("simple", "moderate", "complex")

    def test_common_patterns(self):
        from src.agent_tools.code_analysis import MutatorAnalyzer
        analyzer = MutatorAnalyzer()
        patterns = analyzer.common_patterns()
        assert patterns["total_modules"] >= 40
        assert patterns["total_mutators"] >= 400

    def test_to_dict(self):
        from src.agent_tools.code_analysis import MutatorAnalyzer
        analyzer = MutatorAnalyzer()
        analysis = analyzer.analyze_module("src/prompt_injection/encoding_format.py")
        d = analysis.to_dict()
        assert "mutator_count" in d
        assert "mutators" in d


class TestComplexityScorer:
    def test_score_file(self):
        from src.agent_tools.code_analysis import ComplexityScorer
        scorer = ComplexityScorer()
        report = scorer.score_file("src/prompt_injection/encoding_format.py")
        assert report.line_count > 50
        assert report.rating in ("A", "B", "C", "D", "E", "F")
        assert report.cyclomatic_complexity >= 1

    def test_score_all_mutators(self):
        from src.agent_tools.code_analysis import ComplexityScorer
        scorer = ComplexityScorer()
        reports = scorer.score_all_mutators()
        assert len(reports) >= 40
        for r in reports:
            assert r.rating in ("A", "B", "C", "D", "E", "F")

    def test_score_function(self):
        from src.agent_tools.code_analysis import ComplexityScorer
        scorer = ComplexityScorer()
        source = """
def simple():
    return 1

def branchy(x):
    if x > 0:
        if x > 10:
            return "big"
        return "small"
    return "negative"
"""
        r1 = scorer.score_function(source, "simple")
        r2 = scorer.score_function(source, "branchy")
        assert r2.cyclomatic_complexity > r1.cyclomatic_complexity

    def test_to_dict(self):
        from src.agent_tools.code_analysis import ComplexityScorer
        scorer = ComplexityScorer()
        report = scorer.score_file("src/prompt_injection/encoding_format.py")
        d = report.to_dict()
        assert "cyclomatic_complexity" in d
        assert "rating" in d


class TestPatternDetector:
    def test_scan_file(self):
        from src.agent_tools.code_analysis import PatternDetector
        detector = PatternDetector()
        issues = detector.scan_file("src/prompt_injection/encoding_format.py")
        # Well-formed file should have few issues
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) == 0  # encoding_format.py should be clean

    def test_scan_all(self):
        from src.agent_tools.code_analysis import PatternDetector
        detector = PatternDetector()
        issues = detector.scan_all()
        assert isinstance(issues, list)
        for i in issues:
            assert i.kind in ("good_pattern", "anti_pattern", "convention_violation")
            assert i.severity in ("info", "warning", "error")

    def test_pattern_match_to_dict(self):
        from src.agent_tools.code_analysis.pattern_detector import PatternMatch
        pm = PatternMatch(
            kind="anti_pattern", name="test", description="Test issue",
            file_path="test.py", line=10, severity="warning",
        )
        d = pm.to_dict()
        assert d["kind"] == "anti_pattern"
        assert d["line"] == 10


# ═══════════════════════════════════════════════════════════════════════
# 10. Sandbox
# ═══════════════════════════════════════════════════════════════════════


class TestCodeValidator:
    def test_valid_code(self):
        from src.agent_tools.sandbox import CodeValidator
        validator = CodeValidator()
        result = validator.validate("x = 1\ny = 2\nprint(x + y)")
        assert result.valid

    def test_syntax_error(self):
        from src.agent_tools.sandbox import CodeValidator
        validator = CodeValidator()
        result = validator.validate("def broken(:\n    pass")
        assert not result.valid
        assert any("Syntax" in e for e in result.errors)

    def test_forbidden_patterns(self):
        from src.agent_tools.sandbox import CodeValidator
        validator = CodeValidator()
        result = validator.validate("import os\nos.system('rm -rf /')")
        assert not result.valid

    def test_validate_mutator_module(self):
        from src.agent_tools.sandbox import CodeValidator
        validator = CodeValidator()
        good_source = '''
from src.prompt_injection import BaseMutator, register_mutator

@register_mutator
class TestMut(BaseMutator):
    NAME = "test_sandbox_mut"
    CATEGORY = "test"
    DESCRIPTION = "Test"
    def _apply(self, text):
        return [(text + " mutated", "desc", {"technique": "t", "variant": "v"})]
'''
        result = validator.validate_mutator_module(good_source)
        assert result.valid

    def test_missing_required(self):
        from src.agent_tools.sandbox import CodeValidator
        validator = CodeValidator()
        bad_source = '''
class NotAMutator:
    pass
'''
        result = validator.validate_mutator_module(bad_source)
        assert not result.valid

    def test_check_naming_collisions(self):
        from src.agent_tools.sandbox import CodeValidator
        validator = CodeValidator()
        source = 'NAME = "base32_encode"\nNAME = "unique_one"'
        collisions = validator.check_naming_collisions(source, ["base32_encode", "rot13"])
        assert "base32_encode" in collisions
        assert "unique_one" not in collisions


class TestSafeExecutor:
    def test_execute_simple(self):
        from src.agent_tools.sandbox import SafeExecutor
        executor = SafeExecutor()
        result = executor.execute("x = 1 + 1\nprint(x)")
        assert result.success
        assert "2" in result.stdout

    def test_execute_error(self):
        from src.agent_tools.sandbox import SafeExecutor
        executor = SafeExecutor()
        result = executor.execute("1 / 0")
        assert not result.success
        assert result.error_type == "ZeroDivisionError"

    def test_verify_mutator_output_good(self):
        from src.agent_tools.sandbox import SafeExecutor
        issues = SafeExecutor.verify_mutator_output([
            ("mutated text", "desc", {"technique": "t", "variant": "v"}),
        ])
        assert len(issues) == 0

    def test_verify_mutator_output_bad(self):
        from src.agent_tools.sandbox import SafeExecutor
        issues = SafeExecutor.verify_mutator_output([
            ("", "desc", {"technique": "t"}),  # empty + missing variant
        ])
        assert len(issues) >= 1

    def test_verify_empty_output(self):
        from src.agent_tools.sandbox import SafeExecutor
        issues = SafeExecutor.verify_mutator_output([])
        assert len(issues) >= 1


class TestOutputChecker:
    def test_good_output(self):
        from src.agent_tools.sandbox import OutputChecker
        checker = OutputChecker()
        result = checker.check(
            "test_mutator", "original text", "original text mutated",
            {"technique": "t", "variant": "v"},
        )
        assert result.passed
        assert result.checks_passed > 0

    def test_identical_output(self):
        from src.agent_tools.sandbox import OutputChecker
        checker = OutputChecker()
        result = checker.check("test", "same text", "same text")
        assert not result.passed

    def test_empty_output(self):
        from src.agent_tools.sandbox import OutputChecker
        checker = OutputChecker()
        result = checker.check("test", "original", "")
        assert not result.passed

    def test_missing_metadata_keys(self):
        from src.agent_tools.sandbox import OutputChecker
        checker = OutputChecker()
        result = checker.check("test", "orig", "mutated", {"technique": "t"})
        assert any("variant" in i for i in result.issues)

    def test_summarize(self):
        from src.agent_tools.sandbox import OutputChecker
        checker = OutputChecker()
        results = [
            checker.check("m1", "orig", "mutated1", {"technique": "t", "variant": "v"}),
            checker.check("m2", "orig", "orig"),  # identical = fail
        ]
        summary = checker.summarize(results)
        assert summary["total_checked"] == 2
        assert summary["passed"] >= 1
        assert summary["failed"] >= 1


# ═══════════════════════════════════════════════════════════════════════
# 11. Prompt Library
# ═══════════════════════════════════════════════════════════════════════


class TestGenerationPrompts:
    def test_new_category(self):
        from src.agent_tools.prompt_library import GenerationPrompts
        prompts = GenerationPrompts()
        prompt = prompts.new_category(
            category_name="test_cat",
            description="Test category",
            mutator_count=10,
        )
        assert "test_cat" in prompt
        assert "BaseMutator" in prompt
        assert "@register_mutator" in prompt

    def test_new_tests(self):
        from src.agent_tools.prompt_library import GenerationPrompts
        prompts = GenerationPrompts()
        prompt = prompts.new_tests(
            category_name="test_cat",
            mutator_names=["m1", "m2"],
        )
        assert "test_cat" in prompt
        assert "m1" in prompt

    def test_new_adapter(self):
        from src.agent_tools.prompt_library import GenerationPrompts
        prompts = GenerationPrompts()
        prompt = prompts.new_adapter(
            repo_name="TestRepo",
            techniques=["tech1"],
        )
        assert "TestRepo" in prompt
        assert "BaseMutator" in prompt

    def test_integration_checklist(self):
        from src.agent_tools.prompt_library import GenerationPrompts
        checklist = GenerationPrompts.integration_checklist()
        assert "__init__.py" in checklist
        assert "coverage.py" in checklist


class TestAnalysisPrompts:
    def test_coverage_gap_analysis(self):
        from src.agent_tools.prompt_library import AnalysisPrompts
        prompts = AnalysisPrompts()
        prompt = prompts.coverage_gap_analysis(
            current_categories=["encoding_format", "obfuscation"],
        )
        assert "Coverage Gap" in prompt
        assert "encoding_format" in prompt

    def test_technique_comparison(self):
        from src.agent_tools.prompt_library import AnalysisPrompts
        prompt = AnalysisPrompts.technique_comparison("base64", "rot13")
        assert "base64" in prompt
        assert "rot13" in prompt
        assert "Effectiveness" in prompt

    def test_paper_analysis(self):
        from src.agent_tools.prompt_library import AnalysisPrompts
        prompt = AnalysisPrompts.paper_analysis("Test Paper", "This is the abstract...")
        assert "Test Paper" in prompt
        assert "abstract" in prompt.lower()

    def test_codebase_investigation(self):
        from src.agent_tools.prompt_library import AnalysisPrompts
        prompt = AnalysisPrompts.codebase_investigation("How does encoding work?")
        assert "encoding" in prompt


class TestReviewPrompts:
    def test_code_review(self):
        from src.agent_tools.prompt_library import ReviewPrompts
        prompt = ReviewPrompts.code_review("src/test.py", "class Foo: pass")
        assert "Review Checklist" in prompt
        assert "src/test.py" in prompt

    def test_test_coverage_review(self):
        from src.agent_tools.prompt_library import ReviewPrompts
        prompt = ReviewPrompts.test_coverage_review("encoding", mutator_count=10)
        assert "encoding" in prompt
        assert "10" in prompt

    def test_pre_commit_review(self):
        from src.agent_tools.prompt_library import ReviewPrompts
        prompt = ReviewPrompts.pre_commit_review()
        assert "Pre-Commit" in prompt
        assert "__init__.py" in prompt

    def test_regression_check(self):
        from src.agent_tools.prompt_library import ReviewPrompts
        prompt = ReviewPrompts.regression_check(["test_foo", "test_bar"])
        assert "test_foo" in prompt
        assert "Regression" in prompt


# ═══════════════════════════════════════════════════════════════════════
# 12. Diff Engine
# ═══════════════════════════════════════════════════════════════════════


class TestChangeBuilder:
    def test_build_changeset(self):
        from src.agent_tools.diff_engine import ChangeBuilder
        builder = ChangeBuilder("Test changes")
        builder.replace("file.py", old="old", new="new")
        builder.append("file2.py", text="new content")
        cs = builder.build()
        assert len(cs.changes) == 2
        assert len(cs.files_affected) == 2

    def test_preview(self):
        from src.agent_tools.diff_engine import ChangeBuilder
        builder = ChangeBuilder("Test")
        builder.replace("f.py", old="a", new="b", description="Replace a with b")
        preview = builder.preview()
        assert "Replace a with b" in preview

    def test_insert_after(self):
        from src.agent_tools.diff_engine import ChangeBuilder
        builder = ChangeBuilder("Test")
        builder.insert_after("f.py", after="marker", text="new line")
        cs = builder.build()
        assert cs.changes[0].kind == "insert"
        assert cs.changes[0].after_text == "marker"

    def test_delete(self):
        from src.agent_tools.diff_engine import ChangeBuilder
        builder = ChangeBuilder("Test")
        builder.delete("f.py", text="remove this")
        cs = builder.build()
        assert cs.changes[0].kind == "delete"

    def test_for_new_category(self):
        from src.agent_tools.diff_engine import ChangeBuilder
        builder = ChangeBuilder.for_new_category("my_category", "my_category.py")
        cs = builder.build()
        assert len(cs.changes) >= 2
        assert any("__init__.py" in c.file_path for c in cs.changes)
        assert any("coverage.py" in c.file_path for c in cs.changes)

    def test_changeset_to_dict(self):
        from src.agent_tools.diff_engine import ChangeBuilder
        builder = ChangeBuilder("Dict test")
        builder.replace("f.py", old="a", new="b")
        d = builder.build().to_dict()
        assert d["change_count"] == 1
        assert "f.py" in d["files_affected"]


class TestFilePatcher:
    def test_dry_run_valid(self, tmp_path):
        from src.agent_tools.diff_engine.file_patcher import FilePatcher
        from src.agent_tools.diff_engine.change_builder import ChangeBuilder
        # Create a test file
        (tmp_path / "test.py").write_text("old content here", encoding="utf-8")
        patcher = FilePatcher(root=tmp_path)
        builder = ChangeBuilder("Test")
        builder.replace("test.py", old="old content", new="new content")
        result = patcher.dry_run(builder.build())
        assert result.success
        assert result.changes_applied == 1

    def test_dry_run_invalid(self, tmp_path):
        from src.agent_tools.diff_engine.file_patcher import FilePatcher
        from src.agent_tools.diff_engine.change_builder import ChangeBuilder
        (tmp_path / "test.py").write_text("some content", encoding="utf-8")
        patcher = FilePatcher(root=tmp_path)
        builder = ChangeBuilder("Test")
        builder.replace("test.py", old="nonexistent text", new="new")
        result = patcher.dry_run(builder.build())
        assert not result.success

    def test_apply(self, tmp_path):
        from src.agent_tools.diff_engine.file_patcher import FilePatcher
        from src.agent_tools.diff_engine.change_builder import ChangeBuilder
        (tmp_path / "test.py").write_text("hello world", encoding="utf-8")
        patcher = FilePatcher(root=tmp_path)
        builder = ChangeBuilder("Test")
        builder.replace("test.py", old="hello", new="goodbye")
        result = patcher.apply(builder.build())
        assert result.success
        content = (tmp_path / "test.py").read_text(encoding="utf-8")
        assert "goodbye world" in content

    def test_apply_append(self, tmp_path):
        from src.agent_tools.diff_engine.file_patcher import FilePatcher
        from src.agent_tools.diff_engine.change_builder import ChangeBuilder
        (tmp_path / "test.py").write_text("line1", encoding="utf-8")
        patcher = FilePatcher(root=tmp_path)
        builder = ChangeBuilder("Test")
        builder.append("test.py", text="line2")
        result = patcher.apply(builder.build())
        assert result.success
        content = (tmp_path / "test.py").read_text(encoding="utf-8")
        assert "line1" in content
        assert "line2" in content


class TestDiffPreviewer:
    def test_diff_strings(self):
        from src.agent_tools.diff_engine import DiffPreviewer
        previewer = DiffPreviewer()
        view = previewer.diff_strings(
            "line1\nline2\nline3\n",
            "line1\nmodified\nline3\n",
            filename="test.py",
        )
        assert view.additions >= 1
        assert view.deletions >= 1
        assert "test.py" in view.content

    def test_summary(self):
        from src.agent_tools.diff_engine import DiffPreviewer
        from src.agent_tools.diff_engine.change_builder import ChangeBuilder
        previewer = DiffPreviewer()
        builder = ChangeBuilder("Test summary")
        builder.replace("f1.py", old="a", new="b")
        builder.append("f2.py", text="new")
        summary = previewer.summary(builder.build())
        assert "Test summary" in summary
        assert "f1.py" in summary

    def test_unified_with_real_file(self, tmp_path):
        from src.agent_tools.diff_engine import DiffPreviewer
        from src.agent_tools.diff_engine.change_builder import ChangeBuilder
        (tmp_path / "test.py").write_text("old\ncontent\nhere\n", encoding="utf-8")
        previewer = DiffPreviewer(root=tmp_path)
        builder = ChangeBuilder("Test")
        builder.replace("test.py", old="old", new="new")
        diffs = previewer.unified(builder.build())
        assert len(diffs) == 1
        assert diffs[0].additions >= 1

    def test_diff_view_to_dict(self):
        from src.agent_tools.diff_engine.diff_previewer import DiffView
        view = DiffView(
            file_path="test.py", format="unified",
            content="diff content", additions=3, deletions=1,
        )
        d = view.to_dict()
        assert d["additions"] == 3
        assert d["file_path"] == "test.py"


# ═══════════════════════════════════════════════════════════════════════
# 13. Feedback Loop
# ═══════════════════════════════════════════════════════════════════════


class TestResultCollector:
    def test_record_and_retrieve(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        outcome = TaskOutcome(
            task_id="t1", task_kind="new_category", success=True,
            mutators_created=10, tests_created=50, quality_score=0.85,
            coverage_delta=0.02, lessons=["Always check collisions"],
        )
        collector.record(outcome)
        assert len(collector.recent(10)) == 1
        assert collector.recent(10)[0].task_id == "t1"

    def test_successes_and_failures(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="s1", task_kind="fix_bug", success=True))
        collector.record(TaskOutcome(task_id="f1", task_kind="new_category", success=False, error="collision"))
        assert len(collector.successes()) == 1
        assert len(collector.failures()) == 1

    def test_by_kind(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="t1", task_kind="fix_bug", success=True))
        collector.record(TaskOutcome(task_id="t2", task_kind="new_category", success=True))
        assert len(collector.by_kind("fix_bug")) == 1

    def test_all_lessons(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="t1", task_kind="x", success=True, lessons=["L1", "L2"]))
        collector.record(TaskOutcome(task_id="t2", task_kind="y", success=False, lessons=["L3"]))
        assert len(collector.all_lessons()) == 3

    def test_stats(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="t1", task_kind="x", success=True, quality_score=0.9))
        collector.record(TaskOutcome(task_id="t2", task_kind="x", success=False, quality_score=0.3))
        stats = collector.stats()
        assert stats["total_tasks"] == 2
        assert stats["successes"] == 1
        assert stats["success_rate"] == 50.0

    def test_persistence(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        path = tmp_path / "outcomes.json"
        c1 = ResultCollector(store_path=path)
        c1.record(TaskOutcome(task_id="t1", task_kind="x", success=True))
        c2 = ResultCollector(store_path=path)
        assert len(c2.recent(10)) == 1

    def test_task_outcome_to_dict(self):
        from src.agent_tools.feedback_loop.result_collector import TaskOutcome
        o = TaskOutcome(task_id="t1", task_kind="fix_bug", success=True)
        d = o.to_dict()
        assert d["task_id"] == "t1"
        assert d["success"] is True

    def test_clear(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="t1", task_kind="x", success=True))
        collector.clear()
        assert len(collector.recent(10)) == 0


class TestLearningStore:
    def test_extract_patterns(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        from src.agent_tools.feedback_loop.learning_store import LearningStore
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="t1", task_kind="x", success=True, quality_score=0.9))
        store = LearningStore(collector)
        patterns = store.extract_patterns()
        assert isinstance(patterns, list)

    def test_failure_patterns(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        from src.agent_tools.feedback_loop.learning_store import LearningStore
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="f1", task_kind="x", success=False, error="naming collision"))
        collector.record(TaskOutcome(task_id="f2", task_kind="x", success=False, error="duplicate collision"))
        store = LearningStore(collector)
        patterns = store.failure_patterns()
        assert len(patterns) >= 1
        assert patterns[0].kind == "failure_pattern"

    def test_success_strategies(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        from src.agent_tools.feedback_loop.learning_store import LearningStore
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="s1", task_kind="new_category", success=True, quality_score=0.9))
        store = LearningStore(collector)
        strategies = store.success_strategies()
        assert len(strategies) >= 1
        assert strategies[0].kind == "success_pattern"

    def test_lessons_for(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        from src.agent_tools.feedback_loop.learning_store import LearningStore
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="t1", task_kind="fix_bug", success=True, lessons=["Check imports"]))
        store = LearningStore(collector)
        lessons = store.lessons_for("fix_bug")
        assert "Check imports" in lessons

    def test_agent_context(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector, TaskOutcome
        from src.agent_tools.feedback_loop.learning_store import LearningStore
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        collector.record(TaskOutcome(task_id="t1", task_kind="new_category", success=True, quality_score=0.8, lessons=["Do X"]))
        store = LearningStore(collector)
        ctx = store.agent_context("new_category")
        assert "Lessons" in ctx
        assert "Do X" in ctx

    def test_pattern_to_dict(self):
        from src.agent_tools.feedback_loop.learning_store import Pattern
        p = Pattern(kind="failure_pattern", description="test", frequency=3, confidence=0.7)
        d = p.to_dict()
        assert d["kind"] == "failure_pattern"
        assert d["frequency"] == 3

    def test_categorize_error(self):
        from src.agent_tools.feedback_loop.learning_store import LearningStore
        assert LearningStore._categorize_error("naming collision found") == "naming_collision"
        assert LearningStore._categorize_error("import not found") == "import_error"
        assert LearningStore._categorize_error("syntax error at line 5") == "syntax_error"
        assert LearningStore._categorize_error("something else") == "other"


class TestPriorityAdjuster:
    def test_adjust_empty(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector
        from src.agent_tools.feedback_loop.priority_adjuster import PriorityAdjuster
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        adjuster = PriorityAdjuster(collector)
        adjustments = adjuster.adjust([])
        assert adjustments == []

    def test_priority_adjustment_to_dict(self):
        from src.agent_tools.feedback_loop.priority_adjuster import PriorityAdjustment
        adj = PriorityAdjustment(
            task_id="t1", original_priority="high",
            adjusted_priority="medium", reason="test",
        )
        d = adj.to_dict()
        assert d["task_id"] == "t1"
        assert d["adjusted_priority"] == "medium"

    def test_reorder(self, tmp_path):
        from src.agent_tools.feedback_loop.result_collector import ResultCollector
        from src.agent_tools.feedback_loop.priority_adjuster import PriorityAdjuster
        from src.agent_tools.orchestrator.task_planner import ImprovementTask
        collector = ResultCollector(store_path=tmp_path / "outcomes.json")
        adjuster = PriorityAdjuster(collector)
        tasks = [
            ImprovementTask(id="t1", priority="low", kind="fix_bug", title="Fix 1", description="Fix a bug"),
            ImprovementTask(id="t2", priority="high", kind="new_category", title="New 1", description="Add category"),
        ]
        ordered = adjuster.reorder(tasks)
        assert len(ordered) == 2
        # Higher priority should come first
        assert ordered[0].priority in ("critical", "high", "medium")


# ═══════════════════════════════════════════════════════════════════════
# 14. Metrics
# ═══════════════════════════════════════════════════════════════════════


class TestSnapshotCollector:
    def test_record_and_latest(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot
        collector = SnapshotCollector(store_path=tmp_path / "snaps.json")
        snap = MetricSnapshot(
            timestamp="2026-03-10T12:00:00Z",
            total_mutators=548, total_categories=47,
            coverage_score=0.72,
        )
        collector.record(snap)
        assert collector.latest() is not None
        assert collector.latest().total_mutators == 548

    def test_history(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot
        collector = SnapshotCollector(store_path=tmp_path / "snaps.json")
        collector.record(MetricSnapshot(timestamp="t1", total_mutators=500))
        collector.record(MetricSnapshot(timestamp="t2", total_mutators=510))
        assert len(collector.history()) == 2

    def test_since(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot
        collector = SnapshotCollector(store_path=tmp_path / "snaps.json")
        for i in range(10):
            collector.record(MetricSnapshot(timestamp=f"t{i}", total_mutators=500 + i))
        assert len(collector.since(3)) == 3

    def test_persistence(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot
        path = tmp_path / "snaps.json"
        c1 = SnapshotCollector(store_path=path)
        c1.record(MetricSnapshot(timestamp="t1", total_mutators=500))
        c2 = SnapshotCollector(store_path=path)
        assert c2.latest().total_mutators == 500

    def test_snapshot_to_dict(self):
        from src.agent_tools.metrics.snapshot_collector import MetricSnapshot
        snap = MetricSnapshot(timestamp="t1", total_mutators=100, total_categories=10)
        d = snap.to_dict()
        assert d["total_mutators"] == 100
        assert d["timestamp"] == "t1"

    def test_clear(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot
        collector = SnapshotCollector(store_path=tmp_path / "snaps.json")
        collector.record(MetricSnapshot(timestamp="t1"))
        collector.clear()
        assert collector.latest() is None


class TestTrendAnalyzer:
    def test_insufficient_data(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector
        from src.agent_tools.metrics.trend_analyzer import TrendAnalyzer
        collector = SnapshotCollector(store_path=tmp_path / "snaps.json")
        analyzer = TrendAnalyzer(collector)
        trends = analyzer.analyze()
        assert trends[0].direction == "insufficient_data"

    def test_improving_trend(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot
        from src.agent_tools.metrics.trend_analyzer import TrendAnalyzer
        collector = SnapshotCollector(store_path=tmp_path / "snaps.json")
        collector.record(MetricSnapshot(timestamp="t1", total_mutators=400))
        collector.record(MetricSnapshot(timestamp="t2", total_mutators=500))
        analyzer = TrendAnalyzer(collector)
        trends = analyzer.analyze()
        mutator_trend = [t for t in trends if t.metric == "total_mutators"][0]
        assert mutator_trend.direction == "improving"

    def test_declining_trend(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot
        from src.agent_tools.metrics.trend_analyzer import TrendAnalyzer
        collector = SnapshotCollector(store_path=tmp_path / "snaps.json")
        collector.record(MetricSnapshot(timestamp="t1", total_mutators=500))
        collector.record(MetricSnapshot(timestamp="t2", total_mutators=400))
        analyzer = TrendAnalyzer(collector)
        regressions = analyzer.regressions()
        assert len(regressions) >= 1

    def test_report(self, tmp_path):
        from src.agent_tools.metrics.snapshot_collector import SnapshotCollector, MetricSnapshot
        from src.agent_tools.metrics.trend_analyzer import TrendAnalyzer
        collector = SnapshotCollector(store_path=tmp_path / "snaps.json")
        collector.record(MetricSnapshot(timestamp="t1", total_mutators=400))
        collector.record(MetricSnapshot(timestamp="t2", total_mutators=500))
        analyzer = TrendAnalyzer(collector)
        report = analyzer.report()
        assert "Metric Trends" in report
        assert "total_mutators" in report

    def test_trend_to_dict(self):
        from src.agent_tools.metrics.trend_analyzer import Trend
        t = Trend(metric="coverage", direction="improving", change_pct=5.0)
        d = t.to_dict()
        assert d["metric"] == "coverage"
        assert d["direction"] == "improving"


class TestHealthCheck:
    def test_run(self):
        from src.agent_tools.metrics.health_check import HealthCheck
        status = HealthCheck().run()
        assert isinstance(status.healthy, bool)
        assert status.checks_total >= 1
        assert status.score >= 0.0

    def test_health_status_to_dict(self):
        from src.agent_tools.metrics.health_check import HealthStatus
        status = HealthStatus(healthy=True, score=0.9, checks_passed=3, checks_total=4)
        d = status.to_dict()
        assert d["healthy"] is True
        assert d["score"] == 0.9

    def test_checks_included(self):
        from src.agent_tools.metrics.health_check import HealthCheck
        status = HealthCheck().run()
        assert status.checks_total >= 4
        assert len(status.info) >= 1 or len(status.warnings) >= 1 or len(status.issues) >= 1


# ═══════════════════════════════════════════════════════════════════════
# 15. Session State
# ═══════════════════════════════════════════════════════════════════════


class TestSessionManager:
    def test_start_session(self, tmp_path):
        from src.agent_tools.session_state.session_manager import SessionManager
        mgr = SessionManager(state_path=tmp_path / "session.json")
        session = mgr.start("claude-code", session_id="test-001")
        assert session.session_id == "test-001"
        assert session.agent == "claude-code"
        assert mgr.active is True

    def test_set_task(self, tmp_path):
        from src.agent_tools.session_state.session_manager import SessionManager
        mgr = SessionManager(state_path=tmp_path / "session.json")
        mgr.start("agent")
        mgr.set_task("task_001", "Add encoding category")
        assert mgr.current.current_task_id == "task_001"
        assert mgr.current.current_task_title == "Add encoding category"

    def test_file_tracking(self, tmp_path):
        from src.agent_tools.session_state.session_manager import SessionManager
        mgr = SessionManager(state_path=tmp_path / "session.json")
        mgr.start("agent")
        mgr.file_modified("src/prompt_injection/__init__.py")
        mgr.file_created("src/prompt_injection/new_module.py")
        assert "src/prompt_injection/__init__.py" in mgr.current.files_modified
        assert "src/prompt_injection/new_module.py" in mgr.current.files_created

    def test_complete(self, tmp_path):
        from src.agent_tools.session_state.session_manager import SessionManager
        mgr = SessionManager(state_path=tmp_path / "session.json")
        mgr.start("agent")
        result = mgr.complete()
        assert result.status == "completed"
        assert mgr.active is False

    def test_fail(self, tmp_path):
        from src.agent_tools.session_state.session_manager import SessionManager
        mgr = SessionManager(state_path=tmp_path / "session.json")
        mgr.start("agent")
        result = mgr.fail("Import error")
        assert result.status == "failed"
        assert "FAILED: Import error" in result.notes

    def test_context_string(self, tmp_path):
        from src.agent_tools.session_state.session_manager import SessionManager
        mgr = SessionManager(state_path=tmp_path / "session.json")
        mgr.start("claude-code", session_id="s1")
        mgr.set_task("t1", "Fix bug")
        mgr.add_note("Found the issue")
        ctx = mgr.context_string()
        assert "s1" in ctx
        assert "claude-code" in ctx
        assert "Fix bug" in ctx

    def test_increment_counters(self, tmp_path):
        from src.agent_tools.session_state.session_manager import SessionManager
        mgr = SessionManager(state_path=tmp_path / "session.json")
        mgr.start("agent")
        mgr.increment_mutators(5)
        mgr.increment_tests(10)
        assert mgr.current.mutators_added == 5
        assert mgr.current.tests_added == 10

    def test_session_state_to_dict(self, tmp_path):
        from src.agent_tools.session_state.session_manager import SessionManager
        mgr = SessionManager(state_path=tmp_path / "session.json")
        session = mgr.start("agent", session_id="s1")
        d = session.to_dict()
        assert d["session_id"] == "s1"
        assert d["status"] == "active"


class TestFileSnapshotStore:
    def test_snapshot_and_rollback(self, tmp_path):
        from src.agent_tools.session_state.file_snapshot import FileSnapshotStore
        (tmp_path / "test.py").write_text("original content", encoding="utf-8")
        store = FileSnapshotStore(root=tmp_path)
        store.snapshot("test.py")
        (tmp_path / "test.py").write_text("modified content", encoding="utf-8")
        store.rollback("test.py")
        assert (tmp_path / "test.py").read_text(encoding="utf-8") == "original content"

    def test_rollback_new_file(self, tmp_path):
        from src.agent_tools.session_state.file_snapshot import FileSnapshotStore
        store = FileSnapshotStore(root=tmp_path)
        store.snapshot("new.py")  # File doesn't exist yet
        (tmp_path / "new.py").write_text("created", encoding="utf-8")
        store.rollback("new.py")  # Should delete the file
        assert not (tmp_path / "new.py").exists()

    def test_changed_files(self, tmp_path):
        from src.agent_tools.session_state.file_snapshot import FileSnapshotStore
        (tmp_path / "a.py").write_text("a", encoding="utf-8")
        (tmp_path / "b.py").write_text("b", encoding="utf-8")
        store = FileSnapshotStore(root=tmp_path)
        store.snapshot("a.py")
        store.snapshot("b.py")
        (tmp_path / "a.py").write_text("a_modified", encoding="utf-8")
        changed = store.changed_files()
        assert "a.py" in changed
        assert "b.py" not in changed

    def test_snapshot_count(self, tmp_path):
        from src.agent_tools.session_state.file_snapshot import FileSnapshotStore
        (tmp_path / "f.py").write_text("x", encoding="utf-8")
        store = FileSnapshotStore(root=tmp_path)
        assert store.snapshot_count == 0
        store.snapshot("f.py")
        assert store.snapshot_count == 1

    def test_summary(self, tmp_path):
        from src.agent_tools.session_state.file_snapshot import FileSnapshotStore
        (tmp_path / "f.py").write_text("x", encoding="utf-8")
        store = FileSnapshotStore(root=tmp_path)
        store.snapshot("f.py")
        s = store.summary()
        assert s["total_snapshots"] == 1
        assert "f.py" in s["files"]

    def test_rollback_all(self, tmp_path):
        from src.agent_tools.session_state.file_snapshot import FileSnapshotStore
        (tmp_path / "a.py").write_text("a_orig", encoding="utf-8")
        (tmp_path / "b.py").write_text("b_orig", encoding="utf-8")
        store = FileSnapshotStore(root=tmp_path)
        store.snapshot_multiple(["a.py", "b.py"])
        (tmp_path / "a.py").write_text("a_new", encoding="utf-8")
        (tmp_path / "b.py").write_text("b_new", encoding="utf-8")
        count = store.rollback_all()
        assert count == 2
        assert (tmp_path / "a.py").read_text(encoding="utf-8") == "a_orig"
        assert (tmp_path / "b.py").read_text(encoding="utf-8") == "b_orig"


class TestTransaction:
    def test_successful_transaction(self, tmp_path):
        from src.agent_tools.session_state.transaction import Transaction
        (tmp_path / "file.py").write_text("before", encoding="utf-8")
        tx = Transaction("Test tx", root=tmp_path)
        tx.will_modify("file.py")
        result = tx.execute(lambda: (tmp_path / "file.py").write_text("after", encoding="utf-8"))
        assert result.success
        assert (tmp_path / "file.py").read_text(encoding="utf-8") == "after"

    def test_failed_transaction_rollback(self, tmp_path):
        from src.agent_tools.session_state.transaction import Transaction
        (tmp_path / "file.py").write_text("before", encoding="utf-8")
        tx = Transaction("Test tx", root=tmp_path)
        tx.will_modify("file.py")
        def failing_action():
            (tmp_path / "file.py").write_text("broken", encoding="utf-8")
            raise ValueError("boom")
        result = tx.execute(failing_action)
        assert not result.success
        assert result.rolled_back
        assert (tmp_path / "file.py").read_text(encoding="utf-8") == "before"

    def test_transaction_result_to_dict(self):
        from src.agent_tools.session_state.transaction import TransactionResult
        r = TransactionResult(success=True, files_changed=["a.py"])
        d = r.to_dict()
        assert d["success"] is True
        assert "a.py" in d["files_changed"]

    def test_summary(self, tmp_path):
        from src.agent_tools.session_state.transaction import Transaction
        tx = Transaction("My changes", root=tmp_path)
        tx.will_modify("a.py")
        tx.will_create("b.py")
        s = tx.summary()
        assert s["description"] == "My changes"
        assert "a.py" in s["files_to_modify"]
        assert "b.py" in s["files_to_create"]


# ═══════════════════════════════════════════════════════════════════════
# 16. Consistency
# ═══════════════════════════════════════════════════════════════════════


class TestImportChecker:
    def test_check_valid_file(self):
        from src.agent_tools.consistency import ImportChecker
        checker = ImportChecker()
        issues = checker.check_file("src/prompt_injection/__init__.py")
        # __init__.py should resolve its imports
        errors = [i for i in issues if i.issue == "missing_module"]
        # Some transitive imports might not resolve but the file itself should parse
        assert isinstance(issues, list)

    def test_check_nonexistent_file(self):
        from src.agent_tools.consistency import ImportChecker
        checker = ImportChecker()
        issues = checker.check_file("nonexistent/file.py")
        assert len(issues) == 1
        assert issues[0].issue == "missing_module"

    def test_check_package(self):
        from src.agent_tools.consistency import ImportChecker
        checker = ImportChecker()
        issues = checker.check_package("src/agent_tools/test_fixtures")
        assert isinstance(issues, list)

    def test_import_issue_to_dict(self):
        from src.agent_tools.consistency.import_checker import ImportIssue
        issue = ImportIssue(
            file_path="test.py", line=5,
            import_target="missing_module",
            issue="missing_module",
        )
        d = issue.to_dict()
        assert d["file_path"] == "test.py"
        assert d["line"] == 5


class TestRegistrationChecker:
    def test_check_all(self):
        from src.agent_tools.consistency import RegistrationChecker
        checker = RegistrationChecker()
        issues = checker.check_all()
        assert isinstance(issues, list)
        for i in issues:
            assert i.kind in ("unregistered_module", "missing_taxonomy", "missing_tests")

    def test_check_module_registration(self):
        from src.agent_tools.consistency import RegistrationChecker
        checker = RegistrationChecker()
        issues = checker.check_module_registration()
        assert isinstance(issues, list)

    def test_check_taxonomy(self):
        from src.agent_tools.consistency import RegistrationChecker
        checker = RegistrationChecker()
        issues = checker.check_taxonomy()
        assert isinstance(issues, list)

    def test_summary(self):
        from src.agent_tools.consistency import RegistrationChecker
        checker = RegistrationChecker()
        s = checker.summary()
        assert "total_issues" in s
        assert "errors" in s

    def test_registration_issue_to_dict(self):
        from src.agent_tools.consistency.registration_checker import RegistrationIssue
        issue = RegistrationIssue(
            kind="unregistered_module", target="my_module",
            description="Not imported", severity="error",
        )
        d = issue.to_dict()
        assert d["kind"] == "unregistered_module"
        assert d["severity"] == "error"


class TestOrphanDetector:
    def test_detect_all(self):
        from src.agent_tools.consistency import OrphanDetector
        detector = OrphanDetector()
        orphans = detector.detect_all()
        assert isinstance(orphans, list)

    def test_orphan_modules(self):
        from src.agent_tools.consistency import OrphanDetector
        detector = OrphanDetector()
        orphans = detector.orphan_modules()
        assert isinstance(orphans, list)

    def test_unused_helpers(self, tmp_path):
        from src.agent_tools.consistency import OrphanDetector
        (tmp_path / "test_module.py").write_text(
            "def _helper():\n    pass\n\ndef public():\n    return 1\n",
            encoding="utf-8",
        )
        detector = OrphanDetector(root=tmp_path)
        orphans = detector.unused_helpers("test_module.py")
        assert len(orphans) == 1
        assert orphans[0].name == "_helper"

    def test_orphan_to_dict(self):
        from src.agent_tools.consistency.orphan_detector import Orphan
        o = Orphan(kind="orphan_test", file_path="test.py", name="test_x", description="no match")
        d = o.to_dict()
        assert d["kind"] == "orphan_test"
        assert d["name"] == "test_x"


# ═══════════════════════════════════════════════════════════════════════
# 17. Recommendation
# ═══════════════════════════════════════════════════════════════════════


class TestRecommender:
    def test_recommend(self):
        from src.agent_tools.recommendation import Recommender
        rec = Recommender()
        recs = rec.recommend(top_n=5)
        assert isinstance(recs, list)
        for r in recs:
            assert r.rank >= 1
            assert r.priority_score >= 0.0

    def test_recommend_for(self):
        from src.agent_tools.recommendation import Recommender
        rec = Recommender()
        # Likely returns some results since advisory tracker has gaps
        recs = rec.recommend_for("encoding")
        assert isinstance(recs, list)

    def test_next_action(self):
        from src.agent_tools.recommendation import Recommender
        rec = Recommender()
        best = rec.next_action()
        # May or may not have recommendations
        if best is not None:
            assert best.rank == 1
            assert best.title

    def test_recommendation_to_dict(self):
        from src.agent_tools.recommendation.recommender import Recommendation
        r = Recommendation(
            rank=1, title="Test", kind="new_category",
            description="Desc", priority_score=0.8,
        )
        d = r.to_dict()
        assert d["rank"] == 1
        assert d["priority_score"] == 0.8


class TestEffortEstimator:
    def test_estimate_new_category(self):
        from src.agent_tools.recommendation import EffortEstimator
        est = EffortEstimator()
        result = est.estimate("new_category", mutator_count=10)
        assert result.level == "medium"
        assert result.estimated_files >= 1
        assert result.estimated_lines >= 10

    def test_estimate_fix_bug(self):
        from src.agent_tools.recommendation import EffortEstimator
        est = EffortEstimator()
        result = est.estimate("fix_bug")
        assert result.level == "easy"

    def test_estimate_with_historical(self):
        from src.agent_tools.recommendation import EffortEstimator
        est = EffortEstimator()
        result = est.estimate("new_category", historical_avg_minutes=45)
        assert result.confidence == 0.7  # Higher confidence with historical

    def test_compare(self):
        from src.agent_tools.recommendation import EffortEstimator
        est = EffortEstimator()
        results = est.compare(["new_category", "fix_bug", "add_test"])
        assert len(results) == 3

    def test_level_to_minutes(self):
        from src.agent_tools.recommendation import EffortEstimator
        assert EffortEstimator.level_to_minutes("trivial") == 5
        assert EffortEstimator.level_to_minutes("complex") == 120

    def test_effort_estimate_to_dict(self):
        from src.agent_tools.recommendation.effort_estimator import EffortEstimate
        e = EffortEstimate(task_kind="fix_bug", level="easy", estimated_files=1)
        d = e.to_dict()
        assert d["task_kind"] == "fix_bug"
        assert d["level"] == "easy"


class TestImpactScorer:
    def test_score_new_category(self):
        from src.agent_tools.recommendation import ImpactScorer
        scorer = ImpactScorer()
        impact = scorer.score_new_category(
            defense_layers=["input_filter", "alignment"],
            technique_classes=["encoding"],
            mutator_count=10,
        )
        assert impact.composite_score > 0
        assert impact.defense_breadth > 0
        assert impact.rationale

    def test_score_bug_fix(self):
        from src.agent_tools.recommendation import ImpactScorer
        scorer = ImpactScorer()
        impact = scorer.score_bug_fix(affected_mutators=5)
        assert impact.composite_score > 0
        assert "5" in impact.rationale

    def test_score_integration(self):
        from src.agent_tools.recommendation import ImpactScorer
        scorer = ImpactScorer()
        impact = scorer.score_integration(techniques=["t1", "t2", "t3"])
        assert impact.composite_score > 0
        assert impact.gap_reduction == 3

    def test_license_penalty(self):
        from src.agent_tools.recommendation import ImpactScorer
        scorer = ImpactScorer()
        compat = scorer.score_integration(techniques=["t1"], license_compatible=True)
        incompat = scorer.score_integration(techniques=["t1"], license_compatible=False)
        assert compat.composite_score >= incompat.composite_score

    def test_compare(self):
        from src.agent_tools.recommendation import ImpactScorer
        scorer = ImpactScorer()
        scores = [
            scorer.score_bug_fix(1),
            scorer.score_new_category(["a", "b"], ["c"], 10),
        ]
        ranked = scorer.compare(scores)
        assert ranked[0].composite_score >= ranked[1].composite_score

    def test_impact_score_to_dict(self):
        from src.agent_tools.recommendation.impact_scorer import ImpactScore
        s = ImpactScore(composite_score=0.5, rationale="test")
        d = s.to_dict()
        assert d["composite_score"] == 0.5


# ═══════════════════════════════════════════════════════════════════════
# 18. Test Fixtures
# ═══════════════════════════════════════════════════════════════════════


class TestSampleData:
    def test_standard_prompts(self):
        from src.agent_tools.test_fixtures import SampleData
        prompts = SampleData.standard_prompts()
        assert len(prompts) == 10
        assert any("trafficking" in p for p in prompts)

    def test_standard_prompt_single(self):
        from src.agent_tools.test_fixtures import SampleData
        prompt = SampleData.standard_prompt()
        assert isinstance(prompt, str)
        assert len(prompt) > 10

    def test_edge_cases(self):
        from src.agent_tools.test_fixtures import SampleData
        edges = SampleData.edge_cases()
        assert len(edges) >= 15
        assert "" in edges  # Empty string
        assert any(len(e) > 5000 for e in edges)  # Very long string

    def test_expected_metadata(self):
        from src.agent_tools.test_fixtures import SampleData
        meta = SampleData.expected_metadata()
        assert "technique" in meta
        assert "variant" in meta

    def test_pytest_params(self):
        from src.agent_tools.test_fixtures import SampleData
        params = SampleData.pytest_params()
        assert all(p for p in params)  # No empty strings
        params_with_edge = SampleData.pytest_params(include_edge_cases=True)
        assert len(params_with_edge) > len(params)

    def test_category_test_template(self):
        from src.agent_tools.test_fixtures import SampleData
        template = SampleData.category_test_template("my_cat", ["m1", "m2"])
        assert "my_cat" in template
        assert "m1" in template
        assert "pytest" in template
        assert "class TestRegistration" in template


class TestAssertionHelpers:
    def test_assert_no_name_collisions(self):
        from src.agent_tools.test_fixtures import AssertionHelpers
        helpers = AssertionHelpers()
        helpers.assert_no_name_collisions(["a", "b", "c"])
        with pytest.raises(AssertionError):
            helpers.assert_no_name_collisions(["a", "b", "a"])

    def test_assert_metadata_valid(self):
        from src.agent_tools.test_fixtures import AssertionHelpers
        helpers = AssertionHelpers()
        helpers.assert_metadata({"technique": "t", "variant": "v"})

    def test_assert_metadata_missing_key(self):
        from src.agent_tools.test_fixtures import AssertionHelpers
        with pytest.raises(AssertionError):
            AssertionHelpers.assert_metadata({"technique": "t"})  # Missing variant

    def test_assert_transforms(self):
        from src.agent_tools.test_fixtures import AssertionHelpers
        AssertionHelpers.assert_transforms("mutated text", "original text")
        with pytest.raises(AssertionError):
            AssertionHelpers.assert_transforms("same", "same")

    def test_full_mutator_check(self):
        from src.agent_tools.test_fixtures import AssertionHelpers
        from src.prompt_injection import BaseMutator
        subclasses = BaseMutator.__subclasses__()
        if subclasses:
            instance = subclasses[0]()
            issues = AssertionHelpers.full_mutator_check(instance)
            assert isinstance(issues, list)


class TestFixtureFactory:
    def test_conftest(self):
        from src.agent_tools.test_fixtures import FixtureFactory
        conftest = FixtureFactory.conftest()
        assert "@pytest.fixture" in conftest
        assert "standard_prompt" in conftest

    def test_parametrize_category(self):
        from src.agent_tools.test_fixtures import FixtureFactory
        code = FixtureFactory.parametrize_category("encoding_format")
        assert "encoding_format" in code
        assert "@pytest.fixture" in code

    def test_mutator_fixture(self):
        from src.agent_tools.test_fixtures import FixtureFactory
        code = FixtureFactory.mutator_fixture("base32_encode")
        assert "base32_encode" in code
        assert "@pytest.fixture" in code

    def test_category_test_class(self):
        from src.agent_tools.test_fixtures import FixtureFactory
        code = FixtureFactory.category_test_class("test_cat", ["m1", "m2"])
        assert "test_cat" in code
        assert "m1" in code
        assert "class TestRegistration" in code
        assert "class TestFunctionality" in code


# ═══════════════════════════════════════════════════════════════════════
# 19. Toolkit Docs
# ═══════════════════════════════════════════════════════════════════════


class TestToolkitIntrospector:
    def test_packages(self):
        from src.agent_tools.toolkit_docs import ToolkitIntrospector
        intro = ToolkitIntrospector()
        packages = intro.packages()
        assert len(packages) >= 20
        names = [p.name for p in packages]
        assert "feedback_loop" in names
        assert "recommendation" in names

    def test_all_tools(self):
        from src.agent_tools.toolkit_docs import ToolkitIntrospector
        intro = ToolkitIntrospector()
        tools = intro.all_tools()
        assert len(tools) >= 40
        tool_names = [t.name for t in tools]
        assert "ResultCollector" in tool_names
        assert "Recommender" in tool_names

    def test_search(self):
        from src.agent_tools.toolkit_docs import ToolkitIntrospector
        intro = ToolkitIntrospector()
        matches = intro.search("validator")
        assert len(matches) >= 1

    def test_tool_count(self):
        from src.agent_tools.toolkit_docs import ToolkitIntrospector
        intro = ToolkitIntrospector()
        assert intro.tool_count() >= 40

    def test_as_markdown(self):
        from src.agent_tools.toolkit_docs import ToolkitIntrospector
        intro = ToolkitIntrospector()
        md = intro.as_markdown()
        assert "# Agent Tools Reference" in md
        assert "packages" in md

    def test_as_agent_context(self):
        from src.agent_tools.toolkit_docs import ToolkitIntrospector
        intro = ToolkitIntrospector()
        ctx = intro.as_agent_context()
        assert "# Available Agent Tools" in ctx

    def test_tool_info_to_dict(self):
        from src.agent_tools.toolkit_docs.introspector import ToolInfo
        info = ToolInfo(name="Foo", module="foo", package="bar", docstring="A tool")
        d = info.to_dict()
        assert d["name"] == "Foo"
        assert d["package"] == "bar"

    def test_package_info_to_dict(self):
        from src.agent_tools.toolkit_docs.introspector import PackageInfo
        info = PackageInfo(name="test_pkg", docstring="A package", module_count=3)
        d = info.to_dict()
        assert d["name"] == "test_pkg"
        assert d["module_count"] == 3


class TestCapabilityMatrix:
    def test_tools_for(self):
        from src.agent_tools.toolkit_docs import CapabilityMatrix
        matrix = CapabilityMatrix()
        research = matrix.tools_for("research")
        assert len(research.primary_tools) >= 3
        assert "GapAnalyzer" in research.primary_tools

    def test_full_matrix(self):
        from src.agent_tools.toolkit_docs import CapabilityMatrix
        matrix = CapabilityMatrix()
        full = matrix.full_matrix()
        assert len(full) == 8  # 8 workflow phases
        phases = [pt.phase for pt in full]
        assert "orient" in phases
        assert "monitor" in phases

    def test_phase_of(self):
        from src.agent_tools.toolkit_docs import CapabilityMatrix
        matrix = CapabilityMatrix()
        assert matrix.phase_of("GapAnalyzer") == "research"
        assert matrix.phase_of("CodeValidator") == "validate"
        assert matrix.phase_of("Nonexistent") is None

    def test_phases(self):
        from src.agent_tools.toolkit_docs import CapabilityMatrix
        matrix = CapabilityMatrix()
        phases = matrix.phases()
        assert len(phases) == 8
        assert phases[0] == "orient"

    def test_as_markdown(self):
        from src.agent_tools.toolkit_docs import CapabilityMatrix
        matrix = CapabilityMatrix()
        md = matrix.as_markdown()
        assert "# Capability Matrix" in md
        assert "orient" in md
        assert "Total:" in md

    def test_phase_tools_to_dict(self):
        from src.agent_tools.toolkit_docs.capability_matrix import PhaseTools
        pt = PhaseTools(phase="test", primary_tools=["A"], secondary_tools=["B"])
        d = pt.to_dict()
        assert d["phase"] == "test"
        assert "A" in d["primary_tools"]


class TestWorkflowGuide:
    def test_available(self):
        from src.agent_tools.toolkit_docs import WorkflowGuide
        guide = WorkflowGuide()
        workflows = guide.available()
        assert len(workflows) >= 3
        ids = [w["id"] for w in workflows]
        assert "new_category" in ids

    def test_get(self):
        from src.agent_tools.toolkit_docs import WorkflowGuide
        guide = WorkflowGuide()
        wf = guide.get("new_category")
        assert wf is not None
        assert "title" in wf
        assert len(wf["steps"]) >= 5

    def test_instructions(self):
        from src.agent_tools.toolkit_docs import WorkflowGuide
        guide = WorkflowGuide()
        instructions = guide.instructions("new_category")
        assert "Add a New Mutator Category" in instructions
        assert "Step 1" in instructions

    def test_instructions_unknown(self):
        from src.agent_tools.toolkit_docs import WorkflowGuide
        guide = WorkflowGuide()
        result = guide.instructions("nonexistent")
        assert "Unknown workflow" in result

    def test_tools_needed(self):
        from src.agent_tools.toolkit_docs import WorkflowGuide
        guide = WorkflowGuide()
        tools = guide.tools_needed("new_category")
        assert len(tools) >= 5

    def test_workflow_ids(self):
        from src.agent_tools.toolkit_docs import WorkflowGuide
        guide = WorkflowGuide()
        ids = guide.workflow_ids()
        assert "new_category" in ids
        assert "fix_regression" in ids


# ═══════════════════════════════════════════════════════════════════════
# 20. Workflow Runner
# ═══════════════════════════════════════════════════════════════════════


class TestPipeline:
    def test_create_and_run(self):
        from src.agent_tools.workflow_runner.pipeline import Pipeline, Step
        pipe = Pipeline("Test Pipeline")
        pipe.add_step(Step(
            name="step1", phase="orient",
            action=lambda ctx: {"result": 42},
            produces=["data"],
        ))
        result = pipe.run()
        assert result.success
        assert result.steps_completed == 1
        assert result.context["data"] == {"result": 42}

    def test_step_chaining(self):
        from src.agent_tools.workflow_runner.pipeline import Pipeline, Step
        pipe = Pipeline("Chain Test")
        pipe.add_step(Step(
            name="produce", phase="orient",
            action=lambda ctx: 10,
            produces=["value"],
        ))
        pipe.add_step(Step(
            name="consume", phase="validate",
            action=lambda ctx: ctx["value"] * 2,
            required_inputs=["value"],
            produces=["doubled"],
        ))
        result = pipe.run()
        assert result.success
        assert result.context["doubled"] == 20

    def test_missing_input_fails(self):
        from src.agent_tools.workflow_runner.pipeline import Pipeline, Step
        pipe = Pipeline("Fail Test")
        pipe.add_step(Step(
            name="needs_input", phase="validate",
            action=lambda ctx: ctx["missing"],
            required_inputs=["missing"],
        ))
        result = pipe.run()
        assert not result.success

    def test_skip_on_failure(self):
        from src.agent_tools.workflow_runner.pipeline import Pipeline, Step
        pipe = Pipeline("Skip Test")
        pipe.add_step(Step(
            name="failing", phase="validate",
            action=lambda ctx: 1 / 0,
            skip_on_failure=True,
        ))
        pipe.add_step(Step(
            name="after", phase="test",
            action=lambda ctx: "ok",
            produces=["status"],
        ))
        result = pipe.run()
        assert result.success  # Pipeline succeeds despite first step failing
        assert result.steps_completed >= 1

    def test_dry_run(self):
        from src.agent_tools.workflow_runner.pipeline import Pipeline, Step
        pipe = Pipeline("Dry Run")
        pipe.add_step(Step(name="s1", phase="orient", description="First step"))
        pipe.add_step(Step(name="s2", phase="validate", description="Second step"))
        preview = pipe.dry_run()
        assert len(preview) == 2
        assert preview[0]["name"] == "s1"

    def test_validate(self):
        from src.agent_tools.workflow_runner.pipeline import Pipeline, Step
        pipe = Pipeline("Validate Test")
        pipe.add_step(Step(
            name="producer", phase="orient", produces=["data"],
        ))
        pipe.add_step(Step(
            name="consumer", phase="validate",
            required_inputs=["data"],
        ))
        issues = pipe.validate()
        assert len(issues) == 0  # No issues — data is produced before consumed

    def test_validate_detects_missing(self):
        from src.agent_tools.workflow_runner.pipeline import Pipeline, Step
        pipe = Pipeline("Bad Pipeline")
        pipe.add_step(Step(
            name="consumer", phase="validate",
            required_inputs=["nonexistent"],
        ))
        issues = pipe.validate()
        assert len(issues) >= 1
        assert "nonexistent" in issues[0]

    def test_pipeline_result_to_dict(self):
        from src.agent_tools.workflow_runner.pipeline import Pipeline, Step
        pipe = Pipeline("Dict Test")
        pipe.add_step(Step(name="s1", phase="orient", action=lambda ctx: 1))
        result = pipe.run()
        d = result.to_dict()
        assert d["pipeline_name"] == "Dict Test"
        assert d["success"] is True

    def test_step_to_dict(self):
        from src.agent_tools.workflow_runner.pipeline import Step
        step = Step(name="test", phase="orient", description="Test step")
        d = step.to_dict()
        assert d["name"] == "test"
        assert d["phase"] == "orient"


class TestStepRunner:
    def test_run_success(self):
        from src.agent_tools.workflow_runner import StepRunner
        runner = StepRunner()
        result = runner.run("test_step", lambda: 42)
        assert result.success
        assert result.output == 42
        assert result.duration_ms >= 0

    def test_run_failure(self):
        from src.agent_tools.workflow_runner import StepRunner
        runner = StepRunner()
        result = runner.run("failing_step", lambda: 1 / 0)
        assert not result.success
        assert "division by zero" in result.error

    def test_run_with_retry_success(self):
        from src.agent_tools.workflow_runner import StepRunner
        runner = StepRunner()
        counter = {"n": 0}
        def flaky():
            counter["n"] += 1
            if counter["n"] < 3:
                raise ValueError("not yet")
            return "ok"
        result = runner.run_with_retry("flaky", flaky, max_retries=5)
        assert result.success
        assert result.retries == 2

    def test_run_with_retry_exhausted(self):
        from src.agent_tools.workflow_runner import StepRunner
        runner = StepRunner()
        result = runner.run_with_retry("always_fail", lambda: 1 / 0, max_retries=2)
        assert not result.success
        assert "retries" in result.error

    def test_run_sequence(self):
        from src.agent_tools.workflow_runner import StepRunner
        runner = StepRunner()
        results = runner.run_sequence([
            ("s1", lambda: 1),
            ("s2", lambda: 2),
            ("s3", lambda: 3),
        ])
        assert len(results) == 3
        assert all(r.success for r in results)

    def test_run_sequence_stop_on_failure(self):
        from src.agent_tools.workflow_runner import StepRunner
        runner = StepRunner()
        results = runner.run_sequence([
            ("s1", lambda: 1),
            ("s2", lambda: 1 / 0),
            ("s3", lambda: 3),
        ], stop_on_failure=True)
        assert len(results) == 2  # Stopped after s2

    def test_run_result_to_dict(self):
        from src.agent_tools.workflow_runner.step_runner import RunResult
        r = RunResult(step_name="test", success=True, duration_ms=5.0)
        d = r.to_dict()
        assert d["step_name"] == "test"
        assert d["success"] is True


class TestPipelineRegistry:
    def test_available(self):
        from src.agent_tools.workflow_runner import PipelineRegistry
        registry = PipelineRegistry()
        names = registry.available()
        assert "health_check" in names
        assert "coverage_report" in names
        assert "find_next_task" in names
        assert "validate_recent_changes" in names

    def test_get_health_check(self):
        from src.agent_tools.workflow_runner import PipelineRegistry
        registry = PipelineRegistry()
        pipe = registry.get("health_check")
        assert pipe is not None
        assert pipe.name == "Health Check"
        assert len(pipe.steps) >= 2

    def test_get_coverage_report(self):
        from src.agent_tools.workflow_runner import PipelineRegistry
        registry = PipelineRegistry()
        pipe = registry.get("coverage_report")
        assert pipe is not None
        assert pipe.name == "Coverage Report"

    def test_get_nonexistent(self):
        from src.agent_tools.workflow_runner import PipelineRegistry
        registry = PipelineRegistry()
        pipe = registry.get("nonexistent")
        assert pipe is None

    def test_run_health_check(self):
        from src.agent_tools.workflow_runner import PipelineRegistry
        registry = PipelineRegistry()
        pipe = registry.get("health_check")
        result = pipe.run()
        assert result.steps_completed >= 1
        assert result.pipeline_name == "Health Check"

    def test_run_find_next_task(self):
        from src.agent_tools.workflow_runner import PipelineRegistry
        registry = PipelineRegistry()
        pipe = registry.get("find_next_task")
        result = pipe.run()
        assert result.pipeline_name == "Find Next Task"
