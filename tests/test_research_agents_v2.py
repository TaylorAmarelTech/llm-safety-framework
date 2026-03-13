"""Tests for the 5 new research/management agents (v2).

Covers:
- EmbeddingResearchAgent (10 research areas)
- GitHubLibraryAgent (6 search categories)
- ModelBenchmarkAgent (5 model categories)
- TechniqueIntegrationAgent (4 implementation targets)
- AttackSurfaceEvolutionAgent (5 evolution tracks)
- Agent registration and coordinator integration
"""

from __future__ import annotations

import pytest
from src.research.agents import (
    BaseResearchAgent,
    Domain,
    Finding,
    GeneratedTest,
    ResearchReport,
    list_agents,
    get_agent,
    _AGENT_REGISTRY,
)
from src.research.agents.embedding_research_agent import EmbeddingResearchAgent
from src.research.agents.github_library_agent import GitHubLibraryAgent
from src.research.agents.model_benchmark_agent import ModelBenchmarkAgent
from src.research.agents.technique_integration_agent import TechniqueIntegrationAgent
from src.research.agents.attack_surface_evolution_agent import AttackSurfaceEvolutionAgent
from src.research.agents.coordinator import ResearchCoordinator


# ---------------------------------------------------------------------------
# Registration & base class tests
# ---------------------------------------------------------------------------

class TestAgentRegistration:
    """Verify all agents register correctly."""

    def test_total_registered_agents(self):
        agents = list_agents()
        assert len(agents) >= 12, f"Expected >=12 agents, got {len(agents)}"

    @pytest.mark.parametrize("name", [
        "embedding_research",
        "github_library",
        "model_benchmark",
        "technique_integration",
        "attack_surface_evolution",
    ])
    def test_new_agent_registered(self, name):
        agents = list_agents()
        assert name in agents, f"{name} not in registry"

    @pytest.mark.parametrize("name", [
        "enforcement",
        "cross_pollination",
        "technique_evolution",
        "coverage_gap",
        "ethics_boundary",
        "financial_crime",
        "jurisdiction",
    ])
    def test_original_agent_still_registered(self, name):
        agents = list_agents()
        assert name in agents

    def test_get_agent_returns_class(self):
        cls = get_agent("embedding_research")
        assert cls is EmbeddingResearchAgent

    def test_get_agent_unknown_raises(self):
        with pytest.raises(KeyError):
            get_agent("nonexistent_agent_xyz")

    @pytest.mark.parametrize("cls", [
        EmbeddingResearchAgent,
        GitHubLibraryAgent,
        ModelBenchmarkAgent,
        TechniqueIntegrationAgent,
        AttackSurfaceEvolutionAgent,
    ])
    def test_is_base_research_agent(self, cls):
        assert issubclass(cls, BaseResearchAgent)

    @pytest.mark.parametrize("cls", [
        EmbeddingResearchAgent,
        GitHubLibraryAgent,
        ModelBenchmarkAgent,
        TechniqueIntegrationAgent,
        AttackSurfaceEvolutionAgent,
    ])
    def test_has_required_attributes(self, cls):
        assert hasattr(cls, "NAME")
        assert hasattr(cls, "DOMAIN")
        assert hasattr(cls, "DESCRIPTION")
        assert isinstance(cls.DESCRIPTION, str)
        assert len(cls.DESCRIPTION) > 10

    @pytest.mark.parametrize("cls", [
        EmbeddingResearchAgent,
        GitHubLibraryAgent,
        ModelBenchmarkAgent,
        TechniqueIntegrationAgent,
        AttackSurfaceEvolutionAgent,
    ])
    def test_domain_is_valid(self, cls):
        assert cls.DOMAIN in [d.value for d in Domain]


# ---------------------------------------------------------------------------
# EmbeddingResearchAgent tests
# ---------------------------------------------------------------------------

class TestEmbeddingResearchAgent:
    """Test EmbeddingResearchAgent structure and configuration."""

    def test_name(self):
        assert EmbeddingResearchAgent.NAME == "embedding_research"

    def test_research_areas_count(self):
        assert len(EmbeddingResearchAgent.RESEARCH_AREAS) == 10

    @pytest.mark.parametrize("area", [
        "gradient_free_attacks",
        "quantization_exploitation",
        "causal_activation_patching",
        "steering_vectors",
        "mechanistic_exploits",
        "topological_attacks",
        "attention_manipulation",
        "refusal_geometry",
        "tokenization_attacks",
        "information_geometric",
    ])
    def test_research_area_exists(self, area):
        assert area in EmbeddingResearchAgent.RESEARCH_AREAS

    @pytest.mark.parametrize("area", list(EmbeddingResearchAgent.RESEARCH_AREAS.keys()))
    def test_research_area_has_required_fields(self, area):
        data = EmbeddingResearchAgent.RESEARCH_AREAS[area]
        assert "title" in data
        assert "description" in data
        assert "key_papers" in data
        assert "search_terms" in data
        assert len(data["key_papers"]) >= 1
        assert len(data["search_terms"]) >= 2

    def test_system_prompt_not_empty(self):
        agent = EmbeddingResearchAgent.__new__(EmbeddingResearchAgent)
        prompt = agent.get_system_prompt()
        assert len(prompt) > 100
        assert "embedding" in prompt.lower()

    def test_instantiation(self, tmp_path):
        agent = EmbeddingResearchAgent(data_dir=str(tmp_path / "research"))
        assert agent.data_dir.exists()
        assert agent.NAME == "embedding_research"


# ---------------------------------------------------------------------------
# GitHubLibraryAgent tests
# ---------------------------------------------------------------------------

class TestGitHubLibraryAgent:
    """Test GitHubLibraryAgent structure and configuration."""

    def test_name(self):
        assert GitHubLibraryAgent.NAME == "github_library"

    def test_search_categories_count(self):
        assert len(GitHubLibraryAgent.SEARCH_CATEGORIES) == 6

    @pytest.mark.parametrize("cat", [
        "adversarial_embedding",
        "red_teaming_frameworks",
        "mechanistic_interpretability",
        "text_adversarial",
        "embedding_models",
        "topology_geometry",
    ])
    def test_category_exists(self, cat):
        assert cat in GitHubLibraryAgent.SEARCH_CATEGORIES

    @pytest.mark.parametrize("cat", list(GitHubLibraryAgent.SEARCH_CATEGORIES.keys()))
    def test_category_has_required_fields(self, cat):
        data = GitHubLibraryAgent.SEARCH_CATEGORIES[cat]
        assert "title" in data
        assert "description" in data
        assert "search_queries" in data
        assert "known_repos" in data
        assert len(data["search_queries"]) >= 2
        assert len(data["known_repos"]) >= 1

    @pytest.mark.parametrize("cat", list(GitHubLibraryAgent.SEARCH_CATEGORIES.keys()))
    def test_known_repos_have_required_keys(self, cat):
        for repo in GitHubLibraryAgent.SEARCH_CATEGORIES[cat]["known_repos"]:
            assert "name" in repo
            assert "owner" in repo
            assert "desc" in repo

    def test_compatible_licenses(self):
        licenses = GitHubLibraryAgent.COMPATIBLE_LICENSES
        assert "MIT" in licenses
        assert "Apache-2.0" in licenses
        assert len(licenses) >= 6

    def test_system_prompt_not_empty(self):
        agent = GitHubLibraryAgent.__new__(GitHubLibraryAgent)
        prompt = agent.get_system_prompt()
        assert len(prompt) > 100
        assert "github" in prompt.lower() or "repositories" in prompt.lower()

    def test_instantiation(self, tmp_path):
        agent = GitHubLibraryAgent(data_dir=str(tmp_path / "research"))
        assert agent.data_dir.exists()


# ---------------------------------------------------------------------------
# ModelBenchmarkAgent tests
# ---------------------------------------------------------------------------

class TestModelBenchmarkAgent:
    """Test ModelBenchmarkAgent structure and configuration."""

    def test_name(self):
        assert ModelBenchmarkAgent.NAME == "model_benchmark"

    def test_model_categories_count(self):
        assert len(ModelBenchmarkAgent.MODEL_CATEGORIES) == 5

    @pytest.mark.parametrize("cat", [
        "embedding_models",
        "frontier_llms",
        "quantized_variants",
        "safety_classifiers",
        "multimodal_embeddings",
    ])
    def test_category_exists(self, cat):
        assert cat in ModelBenchmarkAgent.MODEL_CATEGORIES

    @pytest.mark.parametrize("cat", list(ModelBenchmarkAgent.MODEL_CATEGORIES.keys()))
    def test_category_has_required_fields(self, cat):
        data = ModelBenchmarkAgent.MODEL_CATEGORIES[cat]
        assert "title" in data
        assert "description" in data
        assert "models" in data
        assert "research_focus" in data
        assert len(data["models"]) >= 3
        assert len(data["research_focus"]) >= 2

    @pytest.mark.parametrize("cat", list(ModelBenchmarkAgent.MODEL_CATEGORIES.keys()))
    def test_models_have_name(self, cat):
        for model in ModelBenchmarkAgent.MODEL_CATEGORIES[cat]["models"]:
            assert "name" in model

    def test_embedding_models_have_dims(self):
        for model in ModelBenchmarkAgent.MODEL_CATEGORIES["embedding_models"]["models"]:
            assert "dims" in model
            assert isinstance(model["dims"], int)
            assert model["dims"] > 0

    def test_system_prompt_not_empty(self):
        agent = ModelBenchmarkAgent.__new__(ModelBenchmarkAgent)
        prompt = agent.get_system_prompt()
        assert len(prompt) > 100

    def test_instantiation(self, tmp_path):
        agent = ModelBenchmarkAgent(data_dir=str(tmp_path / "research"))
        assert agent.data_dir.exists()


# ---------------------------------------------------------------------------
# TechniqueIntegrationAgent tests
# ---------------------------------------------------------------------------

class TestTechniqueIntegrationAgent:
    """Test TechniqueIntegrationAgent structure and configuration."""

    def test_name(self):
        assert TechniqueIntegrationAgent.NAME == "technique_integration"

    def test_implementation_targets_count(self):
        assert len(TechniqueIntegrationAgent.IMPLEMENTATION_TARGETS) == 4

    @pytest.mark.parametrize("target", [
        "intelligent_attack_module",
        "prompt_injection_mutator",
        "chain_detection_seed",
        "cartography_extension",
    ])
    def test_target_exists(self, target):
        assert target in TechniqueIntegrationAgent.IMPLEMENTATION_TARGETS

    @pytest.mark.parametrize("target", list(TechniqueIntegrationAgent.IMPLEMENTATION_TARGETS.keys()))
    def test_target_has_required_fields(self, target):
        data = TechniqueIntegrationAgent.IMPLEMENTATION_TARGETS[target]
        assert "title" in data
        assert "base_path" in data
        assert "test_path" in data
        assert "pattern" in data

    def test_intelligent_attack_existing_modules(self):
        target = TechniqueIntegrationAgent.IMPLEMENTATION_TARGETS["intelligent_attack_module"]
        assert "existing_modules" in target
        assert len(target["existing_modules"]) >= 39

    def test_load_all_agent_findings_empty(self, tmp_path):
        agent = TechniqueIntegrationAgent(data_dir=str(tmp_path / "research"))
        findings = agent._load_all_agent_findings()
        assert isinstance(findings, list)

    def test_system_prompt_not_empty(self):
        agent = TechniqueIntegrationAgent.__new__(TechniqueIntegrationAgent)
        prompt = agent.get_system_prompt()
        assert len(prompt) > 100
        assert "implementation" in prompt.lower()

    def test_instantiation(self, tmp_path):
        agent = TechniqueIntegrationAgent(data_dir=str(tmp_path / "research"))
        assert agent.data_dir.exists()


# ---------------------------------------------------------------------------
# AttackSurfaceEvolutionAgent tests
# ---------------------------------------------------------------------------

class TestAttackSurfaceEvolutionAgent:
    """Test AttackSurfaceEvolutionAgent structure and configuration."""

    def test_name(self):
        assert AttackSurfaceEvolutionAgent.NAME == "attack_surface_evolution"

    def test_evolution_tracks_count(self):
        assert len(AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS) == 5

    @pytest.mark.parametrize("track", [
        "alignment_methods",
        "defense_arms_race",
        "cross_model_transfer",
        "emerging_attack_patterns",
        "deprecated_attacks",
    ])
    def test_track_exists(self, track):
        assert track in AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS

    @pytest.mark.parametrize("track", list(AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS.keys()))
    def test_track_has_required_fields(self, track):
        data = AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS[track]
        assert "title" in data
        assert "description" in data
        assert "research_questions" in data
        assert len(data["research_questions"]) >= 2

    def test_alignment_methods_coverage(self):
        methods = AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS["alignment_methods"]["methods"]
        names = [m["name"] for m in methods]
        assert "RLHF" in names
        assert "DPO" in names
        assert "ORPO" in names

    def test_defense_generations(self):
        gens = AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS["defense_arms_race"]["defense_generations"]
        assert len(gens) >= 4
        for gen in gens:
            assert "gen" in gen
            assert "defenses" in gen
            assert "bypassed_by" in gen

    def test_transfer_patterns(self):
        patterns = AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS["cross_model_transfer"]["transfer_patterns"]
        assert len(patterns) >= 4
        for p in patterns:
            assert "pattern" in p
            assert "success_rate" in p

    def test_emerging_patterns(self):
        patterns = AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS["emerging_attack_patterns"]["emerging_patterns"]
        assert len(patterns) >= 5
        for p in patterns:
            assert "pattern" in p
            assert "maturity" in p

    def test_deprecated_attacks(self):
        deprecated = AttackSurfaceEvolutionAgent.EVOLUTION_TRACKS["deprecated_attacks"]["deprecated"]
        assert len(deprecated) >= 3
        for d in deprecated:
            assert "attack" in d
            assert "defeated_by" in d

    def test_system_prompt_not_empty(self):
        agent = AttackSurfaceEvolutionAgent.__new__(AttackSurfaceEvolutionAgent)
        prompt = agent.get_system_prompt()
        assert len(prompt) > 100
        assert "evolution" in prompt.lower() or "co-evolution" in prompt.lower()

    def test_instantiation(self, tmp_path):
        agent = AttackSurfaceEvolutionAgent(data_dir=str(tmp_path / "research"))
        assert agent.data_dir.exists()


# ---------------------------------------------------------------------------
# Coordinator integration tests
# ---------------------------------------------------------------------------

class TestCoordinatorIntegration:
    """Test that the coordinator sees all 12 agents."""

    def test_coordinator_status_has_all_agents(self, tmp_path):
        coord = ResearchCoordinator(data_dir=str(tmp_path / "research"))
        status = coord.status()
        assert len(status["agents"]) >= 12

    def test_coordinator_agent_names(self, tmp_path):
        coord = ResearchCoordinator(data_dir=str(tmp_path / "research"))
        status = coord.status()
        names = {a["name"] for a in status["agents"]}
        expected = {
            "enforcement", "cross_pollination", "technique_evolution",
            "coverage_gap", "ethics_boundary", "financial_crime",
            "jurisdiction", "embedding_research", "github_library",
            "model_benchmark", "technique_integration",
            "attack_surface_evolution",
        }
        assert expected.issubset(names), f"Missing: {expected - names}"


# ---------------------------------------------------------------------------
# Data model tests
# ---------------------------------------------------------------------------

class TestDataModels:
    """Test shared data models work correctly."""

    def test_finding_creation(self):
        f = Finding(
            id="test_001",
            agent_name="embedding_research",
            domain="cross_domain",
            title="Test finding",
            description="A test finding",
        )
        assert f.id == "test_001"
        d = f.to_dict()
        assert d["agent_name"] == "embedding_research"

    def test_generated_test_creation(self):
        t = GeneratedTest(
            id="test_t_001",
            agent_name="github_library",
            prompt="Test prompt",
            category="adversarial_embedding",
            domain="cross_domain",
        )
        assert t.expected_refusal is True
        d = t.to_dict()
        assert d["category"] == "adversarial_embedding"

    def test_research_report_creation(self):
        r = ResearchReport(
            agent_name="model_benchmark",
            domain="cross_domain",
            findings=[],
            generated_tests=[],
            summary="Test report",
        )
        d = r.to_dict()
        assert d["agent_name"] == "model_benchmark"
        assert d["findings"] == []

    def test_make_id_deterministic(self, tmp_path):
        agent = EmbeddingResearchAgent(data_dir=str(tmp_path / "research"))
        id1 = agent._make_id("TEST", "hello world")
        id2 = agent._make_id("TEST", "hello world")
        id3 = agent._make_id("TEST", "different text")
        assert id1 == id2
        assert id1 != id3

    def test_save_and_load_report(self, tmp_path):
        agent = EmbeddingResearchAgent(data_dir=str(tmp_path / "research"))
        report = ResearchReport(
            agent_name=agent.NAME,
            domain=agent.DOMAIN,
            findings=[
                Finding(
                    id="f1",
                    agent_name=agent.NAME,
                    domain=agent.DOMAIN,
                    title="Test",
                    description="Desc",
                )
            ],
            generated_tests=[],
            summary="Test save",
        )
        path = agent.save_report(report)
        assert path.exists()
        loaded = agent.load_previous_findings()
        assert len(loaded) == 1
        assert loaded[0].title == "Test"
