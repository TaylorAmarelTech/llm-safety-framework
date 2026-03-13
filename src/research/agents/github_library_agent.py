"""GitHub Library Agent — discovers adversarial ML and embedding attack repositories."""

from __future__ import annotations

from datetime import datetime, timezone
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
class GitHubLibraryAgent(BaseResearchAgent):
    """Scans for new GitHub repositories containing adversarial ML techniques,
    embedding attack implementations, and safety testing tools that could be
    integrated into the framework."""

    NAME = "github_library"
    DOMAIN = Domain.CROSS_DOMAIN
    DESCRIPTION = (
        "Discover and evaluate GitHub repositories with adversarial ML, "
        "embedding attack, and LLM safety testing implementations"
    )

    SEARCH_CATEGORIES: dict[str, dict[str, Any]] = {
        "adversarial_embedding": {
            "title": "Adversarial Embedding Libraries",
            "description": (
                "Libraries implementing embedding-space attacks, representation "
                "engineering, steering vectors, or latent-space manipulation"
            ),
            "search_queries": [
                "adversarial embedding attack LLM",
                "representation engineering safety",
                "steering vector refusal",
                "latent space jailbreak",
                "embedding perturbation adversarial",
            ],
            "known_repos": [
                {"name": "RepE", "owner": "andyzoujm", "desc": "Representation Engineering toolkit"},
                {"name": "llm-attacks", "owner": "llm-attacks", "desc": "GCG universal adversarial suffixes"},
                {"name": "abliteration", "owner": "FailSpy", "desc": "Refusal direction ablation"},
            ],
        },
        "red_teaming_frameworks": {
            "title": "Red Teaming and Safety Testing Frameworks",
            "description": (
                "Comprehensive red teaming frameworks, jailbreak benchmarks, "
                "and automated safety evaluation tools"
            ),
            "search_queries": [
                "LLM red teaming framework",
                "jailbreak benchmark evaluation",
                "automated safety testing LLM",
                "adversarial prompt generation",
            ],
            "known_repos": [
                {"name": "garak", "owner": "NVIDIA", "desc": "LLM vulnerability scanner"},
                {"name": "PyRIT", "owner": "Azure", "desc": "Python Risk Identification Toolkit"},
                {"name": "JailbreakBench", "owner": "JailbreakBench", "desc": "Jailbreak benchmark"},
                {"name": "HarmBench", "owner": "centerforaisafety", "desc": "Automated red teaming benchmark"},
                {"name": "EasyJailbreak", "owner": "EasyJailbreak", "desc": "Unified jailbreak framework"},
            ],
        },
        "mechanistic_interpretability": {
            "title": "Mechanistic Interpretability Tools",
            "description": (
                "SAE training, activation analysis, circuit discovery, and "
                "neuron-level interpretability tools"
            ),
            "search_queries": [
                "sparse autoencoder LLM interpretability",
                "mechanistic interpretability tool",
                "activation patching safety",
                "circuit discovery neural network",
            ],
            "known_repos": [
                {"name": "TransformerLens", "owner": "neelnanda-io", "desc": "Mech interp research toolkit"},
                {"name": "SAELens", "owner": "jbloomAus", "desc": "SAE training and analysis"},
                {"name": "nnsight", "owner": "ndif-team", "desc": "Neural network introspection"},
            ],
        },
        "text_adversarial": {
            "title": "Text-Level Adversarial Attack Libraries",
            "description": (
                "Character-level, word-level, and sentence-level adversarial "
                "text generation including TextFooler, BERT-Attack, CheckList"
            ),
            "search_queries": [
                "adversarial text attack NLP",
                "textfooler adversarial examples",
                "prompt mutation adversarial",
                "obfuscation encoding attack text",
            ],
            "known_repos": [
                {"name": "TextAttack", "owner": "QData", "desc": "Adversarial NLP attack framework"},
                {"name": "OpenAttack", "owner": "thunlp", "desc": "Open-source textual adversarial attack toolkit"},
            ],
        },
        "embedding_models": {
            "title": "Embedding Model Libraries and Benchmarks",
            "description": (
                "New embedding models, sentence transformers, contrastive "
                "learning frameworks, and embedding benchmarks"
            ),
            "search_queries": [
                "sentence transformer embedding model 2025",
                "contrastive learning text embedding",
                "embedding benchmark MTEB",
                "multilingual embedding model",
            ],
            "known_repos": [
                {"name": "sentence-transformers", "owner": "UKPLab", "desc": "Sentence embeddings"},
                {"name": "FlagEmbedding", "owner": "FlagOpen", "desc": "BGE embedding models"},
                {"name": "mteb", "owner": "embeddings-benchmark", "desc": "Massive Text Embedding Benchmark"},
            ],
        },
        "topology_geometry": {
            "title": "Topological and Geometric ML Libraries",
            "description": (
                "Persistent homology, topological data analysis, manifold "
                "learning, and geometric deep learning tools"
            ),
            "search_queries": [
                "persistent homology machine learning Python",
                "topological data analysis neural network",
                "manifold learning adversarial",
                "geometric deep learning embedding",
            ],
            "known_repos": [
                {"name": "giotto-tda", "owner": "giotto-ai", "desc": "Topological data analysis"},
                {"name": "ripser", "owner": "scikit-tda", "desc": "Fast Vietoris-Rips persistence"},
            ],
        },
    }

    COMPATIBLE_LICENSES = {
        "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause",
        "ISC", "Unlicense", "CC0-1.0", "WTFPL",
    }

    def get_system_prompt(self) -> str:
        return (
            "You are an expert in adversarial ML, LLM safety research, and "
            "open-source software evaluation. Your task is to identify GitHub "
            "repositories that contain novel techniques for embedding-space attacks, "
            "representation engineering, or safety testing that could be integrated "
            "into an existing LLM safety testing framework.\n\n"
            "For each repository, evaluate:\n"
            "1. Novelty: Does it contain techniques not in standard frameworks?\n"
            "2. Quality: Code quality, documentation, test coverage\n"
            "3. License compatibility: MIT, Apache-2.0, BSD preferred\n"
            "4. Integration effort: How hard to port key techniques?\n"
            "5. Techniques: List specific algorithms/methods of interest\n\n"
            "Return JSON: {\"repositories\": [{\"name\": ..., \"owner\": ..., "
            "\"url\": ..., \"description\": ..., \"techniques\": [...], "
            "\"license\": ..., \"integration_difficulty\": \"low|medium|high\", "
            "\"novelty_score\": 0.0-1.0, \"rationale\": ...}], "
            "\"integration_plans\": [{\"repo\": ..., \"technique\": ..., "
            "\"steps\": [...], \"estimated_files\": int, \"priority\": ...}]}"
        )

    async def _scan_category(
        self, cat_key: str
    ) -> tuple[list[Finding], list[GeneratedTest]]:
        cat = self.SEARCH_CATEGORIES[cat_key]
        known_str = "\n".join(
            f"  - {r['owner']}/{r['name']}: {r['desc']}"
            for r in cat["known_repos"]
        )
        queries_str = "\n".join(f"  - {q}" for q in cat["search_queries"])

        prompt = (
            f"Category: {cat['title']}\n\n"
            f"Description: {cat['description']}\n\n"
            f"Already known repositories:\n{known_str}\n\n"
            f"Search queries to explore:\n{queries_str}\n\n"
            "Find 3-5 NEW repositories (not in the known list above) that contain "
            "novel techniques relevant to this category. For each:\n"
            "1. Repository name and owner\n"
            "2. Key techniques it implements\n"
            "3. License and integration difficulty\n"
            "4. Novelty score (0-1) relative to known repos\n"
            "5. Specific algorithms worth porting\n\n"
            "Also suggest 1-2 integration plans for the most promising repos.\n\n"
            "Return JSON with 'repositories' and 'integration_plans' keys."
        )

        response = await self._call_llm(prompt, system=self.get_system_prompt())
        parsed = self._parse_json_response(response)

        findings: list[Finding] = []
        tests: list[GeneratedTest] = []
        now = datetime.now(tz=timezone.utc).isoformat()

        for repo in parsed.get("repositories", []):
            name = f"{repo.get('owner', '?')}/{repo.get('name', '?')}"
            fid = self._make_id(f"GL_{cat_key}", name)
            techniques = repo.get("techniques", [])
            findings.append(
                Finding(
                    id=fid,
                    agent_name=self.NAME,
                    domain=self.DOMAIN,
                    title=f"Repository: {name}",
                    description=(
                        f"{repo.get('description', '')}\n\n"
                        f"Techniques: {', '.join(techniques)}\n"
                        f"License: {repo.get('license', 'unknown')}\n"
                        f"Integration difficulty: {repo.get('integration_difficulty', 'medium')}\n"
                        f"Novelty: {repo.get('novelty_score', 0.5)}\n"
                        f"Rationale: {repo.get('rationale', '')}"
                    ),
                    severity="medium" if repo.get("novelty_score", 0.5) >= 0.6 else "low",
                    source=repo.get("url", ""),
                    tags=[cat_key, "github_repo"] + techniques[:5],
                    confidence=repo.get("novelty_score", 0.5),
                    discovered_at=now,
                    metadata={
                        "category": cat_key,
                        "license": repo.get("license", "unknown"),
                        "integration_difficulty": repo.get("integration_difficulty", "medium"),
                        "techniques": techniques,
                    },
                )
            )

        for plan in parsed.get("integration_plans", []):
            tid = self._make_id(f"GL_T_{cat_key}", plan.get("technique", "")[:80])
            steps = plan.get("steps", [])
            tests.append(
                GeneratedTest(
                    id=tid,
                    agent_name=self.NAME,
                    prompt=(
                        f"Integration plan for {plan.get('repo', 'unknown')}: "
                        f"{plan.get('technique', 'unknown')}\n"
                        f"Steps: {'; '.join(steps)}\n"
                        f"Estimated files: {plan.get('estimated_files', 'unknown')}"
                    ),
                    category=cat_key,
                    domain=self.DOMAIN,
                    difficulty="expert",
                    attack_type="integration_plan",
                    expected_refusal=False,
                    rationale=f"Priority: {plan.get('priority', 'medium')}",
                    source_finding_id=findings[0].id if findings else "",
                    created_at=now,
                )
            )

        return findings, tests

    async def run(
        self,
        categories: list[str] | None = None,
        **kwargs: Any,
    ) -> ResearchReport:
        start = datetime.now(tz=timezone.utc)
        target_cats = categories or list(self.SEARCH_CATEGORIES.keys())

        all_findings: list[Finding] = []
        all_tests: list[GeneratedTest] = []

        for cat_key in target_cats:
            if cat_key not in self.SEARCH_CATEGORIES:
                continue
            try:
                findings, tests = await self._scan_category(cat_key)
                all_findings.extend(findings)
                all_tests.extend(tests)
            except Exception as exc:  # noqa: BLE001
                all_findings.append(
                    Finding(
                        id=self._make_id("GL_ERR", cat_key),
                        agent_name=self.NAME,
                        domain=self.DOMAIN,
                        title=f"Error scanning {cat_key}",
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
                f"GitHub library scan completed: {len(all_findings)} repositories "
                f"evaluated across {len(target_cats)} categories, "
                f"{len(all_tests)} integration plans generated."
            ),
            run_duration_seconds=elapsed,
            llm_calls_made=self._call_count,
            started_at=start.isoformat(),
            completed_at=datetime.now(tz=timezone.utc).isoformat(),
        )
        self.save_report(report)
        return report
