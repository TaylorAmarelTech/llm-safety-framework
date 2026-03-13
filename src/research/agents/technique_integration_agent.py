"""Technique Integration Agent — converts research findings into implementation plans."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from . import (
    BaseResearchAgent,
    Domain,
    Finding,
    GeneratedTest,
    ResearchReport,
    register_agent,
)


@register_agent
class TechniqueIntegrationAgent(BaseResearchAgent):
    """Takes findings from embedding_research, github_library, and model_benchmark
    agents and generates concrete implementation plans with code scaffolds,
    test specifications, and integration checklists."""

    NAME = "technique_integration"
    DOMAIN = Domain.CROSS_DOMAIN
    DESCRIPTION = (
        "Convert research findings into concrete implementation plans with "
        "code scaffolds, test specs, and integration checklists"
    )

    IMPLEMENTATION_TARGETS: dict[str, dict[str, Any]] = {
        "intelligent_attack_module": {
            "title": "New intelligent_attack Module",
            "base_path": "src/intelligent_attack/",
            "test_path": "tests/",
            "pattern": (
                "Pure Python class with __init__(embedder), vector helper methods, "
                "and main algorithm methods. Dataclass results. No numpy/torch."
            ),
            "template_imports": [
                "from __future__ import annotations",
                "import math",
                "from dataclasses import dataclass, field",
                "from typing import Any, Optional",
            ],
            "existing_modules": [
                "embedder.py", "feature_extractor.py", "space_analyzer.py",
                "gap_finder.py", "prompt_suggester.py", "latent_explorer.py",
                "meta_attacker.py", "cma_explorer.py", "shapley_analyzer.py",
                "self_awareness_prober.py", "representation_prober.py",
                "embedding_inverter.py", "bayesian_explorer.py",
                "adversarial_perturber.py", "prompt_explainer.py",
                "manifold_mapper.py", "information_prober.py",
                "embedding_teacher.py", "semantic_drift.py",
                "trajectory_planner.py", "anchor_exploiter.py",
                "curriculum_attack.py", "conversation_analyzer.py",
                "steerable_conversation.py", "toxicity_attenuator.py",
                "latent_fusion.py", "multi_refusal_ablator.py",
                "spectral_cleaner.py", "dissimilarity_maximizer.py",
                "contrastive_attacker.py", "embedding_poisoner.py",
                "representation_hijacker.py", "trust_region_explorer.py",
                "curvature_analyzer.py", "turbulence_evader.py",
                "sparse_feature_ablator.py", "latent_distance_minimizer.py",
                "orthogonal_unlocker.py", "safety_subspace_exploiter.py",
            ],
        },
        "prompt_injection_mutator": {
            "title": "New prompt_injection Mutator Category",
            "base_path": "src/prompt_injection/",
            "test_path": "tests/",
            "pattern": (
                "Module with 10 mutator functions (name -> str transform). "
                "Register via MUTATORS dict. Pure string transforms, no LLM calls."
            ),
            "existing_categories": 55,
            "existing_mutators": 631,
        },
        "chain_detection_seed": {
            "title": "New chain_detection Seed Module",
            "base_path": "src/chain_detection/seeds/",
            "test_path": "tests/",
            "pattern": (
                "Function returning list[ActivityChain] with steps, indicators, "
                "category, and difficulty. Register in seeds/__init__.py."
            ),
        },
        "cartography_extension": {
            "title": "Cartography System Extension",
            "base_path": "src/cartography/",
            "test_path": "tests/",
            "pattern": (
                "New analysis module extending SafetyTopology, AttackSurfaceCalculator, "
                "or BlindSpotDetector with additional geometric/topological methods."
            ),
        },
    }

    def get_system_prompt(self) -> str:
        return (
            "You are an expert software architect specialising in converting "
            "research findings into production-quality Python implementations. "
            "Your task is to take discovered techniques and create detailed "
            "implementation plans including:\n\n"
            "1. Module architecture (classes, methods, dataclasses)\n"
            "2. Core algorithm in pseudocode\n"
            "3. Pure Python implementation approach (no numpy/torch)\n"
            "4. Test specification (what to test, edge cases)\n"
            "5. Integration points with existing modules\n"
            "6. Estimated complexity and LOC\n\n"
            "Return JSON: {\"implementations\": [{\"name\": ..., \"module_name\": ..., "
            "\"target\": ..., \"classes\": [{\"name\": ..., \"methods\": [...], "
            "\"dataclasses\": [...]}], \"algorithm\": ..., \"test_spec\": "
            "{\"test_count\": int, \"test_categories\": [...]}, "
            "\"integration_points\": [...], \"estimated_loc\": int, "
            "\"priority\": ..., \"dependencies\": [...]}]}"
        )

    async def _plan_implementations(
        self, findings: list[dict[str, Any]]
    ) -> tuple[list[Finding], list[GeneratedTest]]:
        findings_str = ""
        for i, f in enumerate(findings[:15], 1):
            findings_str += (
                f"\n{i}. {f.get('title', 'Unknown')}\n"
                f"   Description: {f.get('description', '')[:200]}\n"
                f"   Source: {f.get('source', 'N/A')}\n"
                f"   Severity: {f.get('severity', 'medium')}\n"
                f"   Tags: {', '.join(f.get('tags', []))}\n"
            )

        targets_str = "\n".join(
            f"- {k}: {v['title']} (pattern: {v['pattern'][:100]}...)"
            for k, v in self.IMPLEMENTATION_TARGETS.items()
        )

        prompt = (
            "Given these research findings from other agents:\n"
            f"{findings_str}\n\n"
            "Available implementation targets:\n"
            f"{targets_str}\n\n"
            "Create detailed implementation plans for the top 5 most impactful "
            "techniques. For each:\n"
            "1. Which target type best fits (intelligent_attack_module, "
            "prompt_injection_mutator, chain_detection_seed, cartography_extension)\n"
            "2. Module name (snake_case)\n"
            "3. Classes with method signatures\n"
            "4. Core algorithm in pseudocode\n"
            "5. Test specification\n"
            "6. Integration points with existing modules\n"
            "7. Estimated lines of code\n"
            "8. Priority (critical/high/medium/low)\n\n"
            "Return JSON with 'implementations' key."
        )

        response = await self._call_llm(prompt, system=self.get_system_prompt())
        parsed = self._parse_json_response(response)

        result_findings: list[Finding] = []
        result_tests: list[GeneratedTest] = []
        now = datetime.now(tz=timezone.utc).isoformat()

        for impl in parsed.get("implementations", []):
            name = impl.get("name", "unknown")
            module_name = impl.get("module_name", "unknown")
            fid = self._make_id("TI_IMPL", name)

            classes_desc = ""
            for cls in impl.get("classes", []):
                methods = ", ".join(cls.get("methods", []))
                dataclasses_list = ", ".join(cls.get("dataclasses", []))
                classes_desc += (
                    f"\n  Class {cls.get('name', '?')}: methods=[{methods}]"
                )
                if dataclasses_list:
                    classes_desc += f", dataclasses=[{dataclasses_list}]"

            test_spec = impl.get("test_spec", {})
            integration = impl.get("integration_points", [])

            result_findings.append(
                Finding(
                    id=fid,
                    agent_name=self.NAME,
                    domain=self.DOMAIN,
                    title=f"Implementation plan: {name}",
                    description=(
                        f"Module: {module_name}\n"
                        f"Target: {impl.get('target', 'intelligent_attack_module')}\n"
                        f"Classes:{classes_desc}\n\n"
                        f"Algorithm: {impl.get('algorithm', 'N/A')[:300]}\n\n"
                        f"Tests: {test_spec.get('test_count', '?')} tests in "
                        f"{', '.join(test_spec.get('test_categories', []))}\n"
                        f"Integration: {', '.join(integration)}\n"
                        f"Estimated LOC: {impl.get('estimated_loc', '?')}\n"
                        f"Priority: {impl.get('priority', 'medium')}"
                    ),
                    severity="high" if impl.get("priority") in ("critical", "high") else "medium",
                    tags=["implementation_plan", module_name, impl.get("target", "")],
                    confidence=0.85,
                    discovered_at=now,
                    metadata={
                        "module_name": module_name,
                        "target": impl.get("target", ""),
                        "estimated_loc": impl.get("estimated_loc", 0),
                        "priority": impl.get("priority", "medium"),
                        "classes": impl.get("classes", []),
                        "algorithm": impl.get("algorithm", ""),
                        "test_spec": test_spec,
                        "dependencies": impl.get("dependencies", []),
                    },
                )
            )

            # Generate a test scaffold as a GeneratedTest
            test_cats = test_spec.get("test_categories", ["unit"])
            tid = self._make_id("TI_TEST", module_name)
            result_tests.append(
                GeneratedTest(
                    id=tid,
                    agent_name=self.NAME,
                    prompt=(
                        f"Test scaffold for {module_name}:\n"
                        f"- {test_spec.get('test_count', 10)} tests\n"
                        f"- Categories: {', '.join(test_cats)}\n"
                        f"- Integration points: {', '.join(integration)}"
                    ),
                    category="implementation_plan",
                    domain=self.DOMAIN,
                    difficulty="expert",
                    attack_type="test_scaffold",
                    expected_refusal=False,
                    rationale=f"Implementation plan for {name}",
                    source_finding_id=fid,
                    created_at=now,
                )
            )

        return result_findings, result_tests

    def _load_all_agent_findings(self) -> list[dict[str, Any]]:
        """Load findings from all other agents' most recent reports."""
        all_findings: list[dict[str, Any]] = []
        research_dir = Path(self.data_dir).parent

        agent_dirs = [
            "embedding_research",
            "github_library",
            "model_benchmark",
            "attack_surface_evolution",
            "technique_evolution",
            "coverage_gap",
            "cross_pollination",
            "enforcement",
            "financial_crime",
        ]

        for agent_name in agent_dirs:
            agent_dir = research_dir / agent_name
            if not agent_dir.exists():
                continue
            # Find most recent report
            reports = sorted(agent_dir.glob("report_*.json"), reverse=True)
            if not reports:
                continue
            try:
                import json
                with open(reports[0], encoding="utf-8") as f:
                    data = json.load(f)
                for finding in data.get("findings", []):
                    finding["_source_agent"] = agent_name
                    all_findings.append(finding)
            except Exception:  # noqa: BLE001
                continue

        return all_findings

    async def run(
        self,
        findings: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> ResearchReport:
        start = datetime.now(tz=timezone.utc)

        # Load findings from other agents if not provided
        input_findings = findings or self._load_all_agent_findings()

        if not input_findings:
            # No findings available — generate from known techniques
            input_findings = [
                {
                    "title": "Concept Cone Explorer",
                    "description": "Polyhedral refusal cone identification (ICML 2025)",
                    "severity": "high",
                    "tags": ["refusal_geometry", "embedding_attack"],
                },
                {
                    "title": "Topological Compression Detector",
                    "description": "Persistent homology on hidden states (arxiv:2505.20435)",
                    "severity": "high",
                    "tags": ["topology", "embedding_attack"],
                },
                {
                    "title": "Attention Eclipse",
                    "description": "Attention weight manipulation amplifier (EMNLP 2025)",
                    "severity": "high",
                    "tags": ["attention", "jailbreak_amplifier"],
                },
                {
                    "title": "NeuroStrike Safety Neuron Pruning",
                    "description": "Sparse safety neuron identification and pruning (NDSS 2026)",
                    "severity": "high",
                    "tags": ["mechanistic", "neuron_pruning"],
                },
                {
                    "title": "ZO-SPSA Gradient-Free Attack",
                    "description": "2-eval gradient approximation (arxiv:2601.01747)",
                    "severity": "medium",
                    "tags": ["gradient_free", "embedding_attack"],
                },
            ]

        all_findings: list[Finding] = []
        all_tests: list[GeneratedTest] = []

        try:
            impl_findings, impl_tests = await self._plan_implementations(input_findings)
            all_findings.extend(impl_findings)
            all_tests.extend(impl_tests)
        except Exception as exc:  # noqa: BLE001
            all_findings.append(
                Finding(
                    id=self._make_id("TI_ERR", "planning"),
                    agent_name=self.NAME,
                    domain=self.DOMAIN,
                    title="Error during implementation planning",
                    description=str(exc),
                    severity="low",
                    discovered_at=datetime.now(tz=timezone.utc).isoformat(),
                )
            )

        elapsed = (datetime.now(tz=timezone.utc) - start).total_seconds()
        report = ResearchReport(
            agent_name=self.NAME,
            domain=self.DOMAIN,
            findings=all_findings,
            generated_tests=all_tests,
            summary=(
                f"Integration planning completed: {len(all_findings)} implementation "
                f"plans from {len(input_findings)} input findings, "
                f"{len(all_tests)} test scaffolds generated."
            ),
            run_duration_seconds=elapsed,
            llm_calls_made=self._call_count,
            started_at=start.isoformat(),
            completed_at=datetime.now(tz=timezone.utc).isoformat(),
        )
        self.save_report(report)
        return report
