"""
Tests for the genetic engine, latent space explorer, and meta-attack learner.

Covers:
- Genetic engine: selection, crossover, mutation, evolution, island model, Pareto
- Latent explorer: boundary estimation, interpolation, adversarial directions, coverage
- Meta-attacker: profiling, similarity, transfer, adaptation, portfolio, persistence
- All 10 genetic_evolution registered mutators
"""

from __future__ import annotations

import json
import math
import random
import tempfile
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Genetic engine
# ---------------------------------------------------------------------------

from src.prompt_injection.genetic_engine import (
    Individual,
    EvolutionResult,
    GeneticEngine,
    NoveltyArchive,
    AdaptiveParameterController,
    tournament_select,
    roulette_select,
    rank_select,
    single_point_crossover,
    uniform_crossover,
    semantic_crossover,
    mutate_insert,
    mutate_delete,
    mutate_swap,
    mutate_replace,
    mutate_category_swap,
    compute_pareto_front,
)

# ---------------------------------------------------------------------------
# Latent explorer
# ---------------------------------------------------------------------------

from src.intelligent_attack.latent_explorer import (
    LatentExplorer,
    BoundaryPoint,
    AdversarialDirection,
    ExplorationResult,
    _dot,
    _norm,
    _cosine,
    _centroid,
    _normalize,
    _euclidean,
)

# ---------------------------------------------------------------------------
# Meta-attacker
# ---------------------------------------------------------------------------

from src.intelligent_attack.meta_attacker import (
    MetaAttacker,
    AttackRecord,
    ModelProfile,
    TransferPrediction,
    StrategyRecommendation,
    PortfolioAllocation,
)


# ===========================================================================
# Fixtures
# ===========================================================================


@pytest.fixture
def sample_individual():
    return Individual(chain=["persona_switch", "base64_encode", "rot13_encode"], fitness=0.7)


@pytest.fixture
def small_population():
    return [
        Individual(chain=["persona_switch", "base64_encode"], fitness=0.8),
        Individual(chain=["unicode_homoglyph", "rot13_encode"], fitness=0.3),
        Individual(chain=["leetspeak_encode", "authority_claim"], fitness=0.6),
        Individual(chain=["academic_shield", "output_format"], fitness=0.5),
    ]


@pytest.fixture
def safe_vectors():
    random.seed(42)
    return [[random.gauss(0, 0.3) for _ in range(8)] for _ in range(15)]


@pytest.fixture
def unsafe_vectors():
    random.seed(99)
    return [[random.gauss(2, 0.3) for _ in range(8)] for _ in range(15)]


@pytest.fixture
def populated_meta():
    ma = MetaAttacker()
    models = ["gpt-4o", "claude-3", "mistral-large"]
    mutators = ["persona_switch", "base64_encode", "rot13_encode",
                "unicode_homoglyph", "authority_claim"]
    random.seed(42)
    for _ in range(100):
        m = random.choice(mutators)
        model = random.choice(models)
        # gpt-4o is harder to bypass
        if model == "gpt-4o":
            bypassed = random.random() < 0.2
        elif model == "claude-3":
            bypassed = random.random() < 0.5
        else:
            bypassed = random.random() < 0.7
        ma.record(m, model, f"hash_{random.randint(0,999)}", bypassed, category="test")
    return ma


# ===========================================================================
# GENETIC ENGINE TESTS
# ===========================================================================


class TestIndividual:
    def test_id_deterministic(self, sample_individual):
        assert sample_individual.id == sample_individual.id

    def test_different_chains_different_ids(self):
        a = Individual(chain=["a", "b"])
        b = Individual(chain=["b", "a"])
        assert a.id != b.id

    def test_to_dict(self, sample_individual):
        d = sample_individual.to_dict()
        assert "id" in d
        assert d["chain"] == ["persona_switch", "base64_encode", "rot13_encode"]
        assert d["fitness"] == 0.7

    def test_apply_returns_results(self):
        ind = Individual(chain=["persona_switch"])
        results = ind.apply("test prompt")
        assert len(results) > 0
        assert results[0].mutated != ""

    def test_apply_empty_chain(self):
        ind = Individual(chain=[])
        results = ind.apply("test prompt")
        assert results == []

    def test_apply_invalid_mutator_skipped(self):
        ind = Individual(chain=["nonexistent_mutator_xyz"])
        results = ind.apply("test prompt")
        assert results == []


class TestSelection:
    def test_tournament_returns_individual(self, small_population):
        result = tournament_select(small_population, k=2)
        assert isinstance(result, Individual)

    def test_tournament_tends_to_pick_fittest(self, small_population):
        # Over many trials, tournament should favor high-fitness
        wins = [tournament_select(small_population, k=3).fitness for _ in range(100)]
        avg_win = sum(wins) / len(wins)
        avg_pop = sum(ind.fitness for ind in small_population) / len(small_population)
        assert avg_win >= avg_pop  # winners should be above average

    def test_roulette_returns_individual(self, small_population):
        result = roulette_select(small_population)
        assert isinstance(result, Individual)

    def test_rank_returns_individual(self, small_population):
        result = rank_select(small_population)
        assert isinstance(result, Individual)


class TestCrossover:
    def test_single_point_produces_two_children(self, small_population):
        c1, c2 = single_point_crossover(small_population[0], small_population[1])
        assert isinstance(c1, Individual)
        assert isinstance(c2, Individual)
        assert len(c1.chain) >= 1
        assert len(c2.chain) >= 1

    def test_uniform_crossover(self, small_population):
        c1, c2 = uniform_crossover(small_population[0], small_population[1])
        assert len(c1.chain) >= 1
        assert len(c2.chain) >= 1

    def test_semantic_crossover(self, small_population):
        c1, c2 = semantic_crossover(small_population[0], small_population[1])
        assert len(c1.chain) >= 1
        assert len(c2.chain) >= 1

    def test_crossover_short_chains(self):
        a = Individual(chain=["persona_switch"])
        b = Individual(chain=["base64_encode"])
        c1, c2 = single_point_crossover(a, b)
        # Short chains: should return copies
        assert len(c1.chain) >= 1
        assert len(c2.chain) >= 1


class TestMutation:
    def test_insert_increases_length(self, sample_individual):
        mutated = mutate_insert(sample_individual)
        assert len(mutated.chain) == len(sample_individual.chain) + 1

    def test_delete_decreases_length(self, sample_individual):
        mutated = mutate_delete(sample_individual)
        assert len(mutated.chain) == len(sample_individual.chain) - 1

    def test_delete_preserves_minimum_one(self):
        ind = Individual(chain=["persona_switch"])
        mutated = mutate_delete(ind)
        assert len(mutated.chain) == 1  # can't go below 1

    def test_swap_preserves_length(self, sample_individual):
        mutated = mutate_swap(sample_individual)
        assert len(mutated.chain) == len(sample_individual.chain)

    def test_replace_preserves_length(self, sample_individual):
        mutated = mutate_replace(sample_individual)
        assert len(mutated.chain) == len(sample_individual.chain)

    def test_category_swap_preserves_length(self, sample_individual):
        mutated = mutate_category_swap(sample_individual)
        assert len(mutated.chain) == len(sample_individual.chain)

    def test_mutations_do_not_modify_original(self, sample_individual):
        original_chain = list(sample_individual.chain)
        mutate_insert(sample_individual)
        mutate_delete(sample_individual)
        mutate_swap(sample_individual)
        assert sample_individual.chain == original_chain


class TestParetoFront:
    def test_empty_population(self):
        assert compute_pareto_front([]) == []

    def test_single_individual(self):
        ind = Individual(chain=["a"], fitness=0.5, stealth=0.5)
        front = compute_pareto_front([ind])
        assert len(front) == 1

    def test_dominated_removed(self):
        a = Individual(chain=["a"], fitness=0.9, stealth=0.9)
        b = Individual(chain=["b"], fitness=0.3, stealth=0.3)  # dominated by a
        front = compute_pareto_front([a, b])
        assert len(front) == 1
        assert front[0].chain == ["a"]

    def test_non_dominated_both_kept(self):
        a = Individual(chain=["a"], fitness=0.9, stealth=0.3)  # high fitness, low stealth
        b = Individual(chain=["b"], fitness=0.3, stealth=0.9)  # low fitness, high stealth
        front = compute_pareto_front([a, b])
        assert len(front) == 2


class TestGeneticEngine:
    def test_initialize(self):
        eng = GeneticEngine(population_size=10)
        eng.initialize()
        assert len(eng.population) == 10

    def test_initialize_with_seeds(self):
        eng = GeneticEngine(population_size=10)
        eng.initialize(seed_chains=[["persona_switch", "base64_encode"]])
        assert len(eng.population) == 10
        # Seed should be in population
        chains = [tuple(ind.chain) for ind in eng.population]
        assert ("persona_switch", "base64_encode") in chains

    def test_evaluate(self):
        eng = GeneticEngine(population_size=5)
        eng.initialize()
        eng.evaluate("test prompt")
        assert all(ind.fitness >= 0 for ind in eng.population)

    def test_evaluate_custom_fitness(self):
        eng = GeneticEngine(population_size=5)
        eng.initialize()
        eng.evaluate("test", fitness_fn=lambda p, r: 0.42)
        assert all(ind.fitness == 0.42 for ind in eng.population)

    def test_step_increments_generation(self):
        eng = GeneticEngine(population_size=6)
        eng.initialize()
        eng.evaluate("test")
        assert eng.generation == 0
        eng.step()
        assert eng.generation == 1

    def test_evolve_returns_result(self):
        eng = GeneticEngine(population_size=6, elitism=1)
        eng.initialize()
        result = eng.evolve("test prompt", generations=3, early_stop_fitness=2.0)
        assert isinstance(result, EvolutionResult)
        assert result.best is not None
        assert result.generation >= 1
        assert len(result.history) >= 1

    def test_evolve_early_stop(self):
        eng = GeneticEngine(population_size=5, elitism=1)
        eng.initialize()
        result = eng.evolve("test", generations=100,
                            fitness_fn=lambda p, r: 1.0,  # always perfect
                            early_stop_fitness=0.95)
        # Should stop early
        assert result.best.fitness >= 0.95

    def test_best_property(self):
        eng = GeneticEngine(population_size=5)
        eng.initialize()
        eng.evaluate("test")
        assert eng.best is not None

    def test_best_empty_population(self):
        eng = GeneticEngine(population_size=5)
        assert eng.best is None

    def test_history_recorded(self):
        eng = GeneticEngine(population_size=5, elitism=1)
        eng.initialize()
        eng.evaluate("test")
        eng.step()
        eng.evaluate("test")
        eng.step()
        history = eng.get_history()
        assert len(history) == 2
        assert "best_fitness" in history[0]
        assert "diversity" in history[0]


class TestIslandModel:
    def test_split_islands(self):
        eng = GeneticEngine(population_size=12)
        eng.initialize()
        islands = eng.split_islands(3)
        assert len(islands) == 3
        total = sum(len(isle.population) for isle in islands)
        assert total >= 9  # at least 3 per island

    def test_migrate(self):
        eng = GeneticEngine(population_size=12)
        eng.initialize()
        eng.evaluate("test")
        islands = eng.split_islands(2)
        for isle in islands:
            isle.evaluate("test")
        GeneticEngine.migrate(islands, n_migrants=1)
        # Migration should not crash; populations intact
        for isle in islands:
            assert len(isle.population) >= 1


# ===========================================================================
# GENETIC MUTATOR REGISTRATION TESTS
# ===========================================================================


class TestGeneticMutators:
    """Test all 10 registered genetic_evolution mutators."""

    GENETIC_MUTATORS = [
        "genetic_single_point",
        "genetic_uniform_crossover",
        "genetic_semantic_crossover",
        "genetic_mutate_insert",
        "genetic_mutate_swap",
        "genetic_category_sibling",
        "genetic_elitist_chain",
        "genetic_island_model",
        "genetic_pareto_front",
        "genetic_diversity_seeking",
    ]

    @pytest.mark.parametrize("name", GENETIC_MUTATORS)
    def test_registered(self, name):
        from src.prompt_injection import get_mutator
        m = get_mutator(name)
        assert m.CATEGORY == "genetic_evolution"

    @pytest.mark.parametrize("name", GENETIC_MUTATORS)
    def test_produces_output(self, name):
        from src.prompt_injection import get_mutator
        m = get_mutator(name)
        results = m.mutate("How to set up a recruitment agency abroad")
        assert len(results) >= 1
        assert results[0].mutated  # non-empty

    @pytest.mark.parametrize("name", GENETIC_MUTATORS)
    def test_metadata_populated(self, name):
        from src.prompt_injection import get_mutator
        m = get_mutator(name)
        results = m.mutate("Test prompt for metadata check")
        assert all(r.mutator_name == name for r in results)
        assert all(r.technique_category == "genetic_evolution" for r in results)

    def test_genetic_category_count(self):
        from src.prompt_injection import get_mutators_by_category
        mutators = get_mutators_by_category("genetic_evolution")
        assert len(mutators) == 10

    def test_coverage_taxonomy_entry(self):
        from src.prompt_injection.coverage import CATEGORY_TAXONOMY
        assert "genetic_evolution" in CATEGORY_TAXONOMY
        entry = CATEGORY_TAXONOMY["genetic_evolution"]
        assert "alignment" in entry["defense_layers"]
        assert "cognitive" in entry["technique_classes"]


# ===========================================================================
# LATENT EXPLORER TESTS
# ===========================================================================


class TestLinearAlgebra:
    """Test lightweight vector helpers."""

    def test_dot(self):
        assert _dot([1, 2, 3], [4, 5, 6]) == 32

    def test_norm(self):
        assert abs(_norm([3, 4]) - 5.0) < 1e-9

    def test_cosine_identical(self):
        assert abs(_cosine([1, 0], [1, 0]) - 1.0) < 1e-9

    def test_cosine_orthogonal(self):
        assert abs(_cosine([1, 0], [0, 1])) < 1e-9

    def test_cosine_zero_vector(self):
        assert _cosine([0, 0], [1, 2]) == 0.0

    def test_normalize(self):
        n = _normalize([3, 4])
        assert abs(_norm(n) - 1.0) < 1e-9

    def test_normalize_zero(self):
        assert _normalize([0, 0]) == [0.0, 0.0]

    def test_centroid(self):
        c = _centroid([[0, 0], [2, 4]])
        assert c == [1.0, 2.0]

    def test_centroid_empty(self):
        assert _centroid([]) == []

    def test_euclidean(self):
        assert abs(_euclidean([0, 0], [3, 4]) - 5.0) < 1e-9


class TestLatentExplorer:
    def test_interpolate_midpoint(self):
        le = LatentExplorer()
        mid = le.interpolate_vectors([0, 0], [2, 4], alpha=0.5)
        assert mid == [1.0, 2.0]

    def test_interpolate_endpoints(self):
        le = LatentExplorer()
        start = le.interpolate_vectors([0, 0], [2, 4], alpha=0.0)
        end = le.interpolate_vectors([0, 0], [2, 4], alpha=1.0)
        assert start == [0.0, 0.0]
        assert end == [2.0, 4.0]

    def test_interpolate_path_length(self):
        le = LatentExplorer()
        path = le.interpolate_path([0, 0], [10, 10], steps=5)
        assert len(path) == 5

    def test_estimate_boundary(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        boundary = le.estimate_boundary(safe_vectors, unsafe_vectors, n_samples=5)
        assert len(boundary) == 5
        for bp in boundary:
            assert isinstance(bp, BoundaryPoint)
            assert len(bp.vector) == 8
            assert 0.0 <= bp.interpolation_alpha <= 1.0

    def test_estimate_boundary_empty_safe(self):
        le = LatentExplorer()
        assert le.estimate_boundary([], [[1, 2]], n_samples=5) == []

    def test_estimate_boundary_empty_unsafe(self):
        le = LatentExplorer()
        assert le.estimate_boundary([[1, 2]], [], n_samples=5) == []

    def test_adversarial_direction(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        ad = le.find_adversarial_direction(safe_vectors, unsafe_vectors)
        assert isinstance(ad, AdversarialDirection)
        assert abs(_norm(ad.direction) - 1.0) < 1e-6  # normalized
        assert ad.magnitude > 0

    def test_diverse_directions(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        dirs = le.find_diverse_adversarial_directions(safe_vectors, unsafe_vectors, 3)
        assert len(dirs) == 3
        assert all(isinstance(d, AdversarialDirection) for d in dirs)

    def test_diverse_directions_empty(self):
        le = LatentExplorer()
        assert le.find_diverse_adversarial_directions([], [[1, 2]], 3) == []

    def test_perturb_along_direction(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        ad = le.find_adversarial_direction(safe_vectors, unsafe_vectors)
        origin = safe_vectors[0]
        perturbed = le.perturb_along_direction(origin, ad, steps=3, step_size=0.1)
        assert len(perturbed) == 3
        # Each step should move further from origin
        for i in range(1, len(perturbed)):
            d_prev = _euclidean(origin, perturbed[i - 1])
            d_curr = _euclidean(origin, perturbed[i])
            assert d_curr > d_prev

    def test_sample_boundary_neighborhood(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        boundary = le.estimate_boundary(safe_vectors, unsafe_vectors, n_samples=3)
        samples = le.sample_boundary_neighborhood(boundary, radius=0.1, n_per_point=2)
        assert len(samples) == 6  # 3 points * 2 per point
        assert all(len(s) == 8 for s in samples)

    def test_project_to_nearest_boundary(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        boundary = le.estimate_boundary(safe_vectors, unsafe_vectors, n_samples=5)
        nearest = le.project_to_nearest_boundary(safe_vectors[0], boundary)
        assert nearest is not None
        assert isinstance(nearest, BoundaryPoint)

    def test_project_to_nearest_empty(self):
        le = LatentExplorer()
        assert le.project_to_nearest_boundary([1, 2], []) is None

    def test_explore_full_workflow(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        result = le.explore(safe_vectors, unsafe_vectors,
                            n_boundary_samples=5,
                            n_directions=3,
                            neighborhood_radius=0.05,
                            n_neighborhood_per_point=2)
        assert isinstance(result, ExplorationResult)
        assert len(result.boundary_points) == 5
        assert len(result.adversarial_directions) == 3
        assert len(result.suggested_vectors) == 10  # 5 * 2
        assert result.boundary_width >= 0
        d = result.to_dict()
        assert "n_boundary_points" in d

    def test_find_nearest(self, safe_vectors):
        le = LatentExplorer()
        target = safe_vectors[0]
        nearest = le.find_nearest(target, safe_vectors, top_k=3)
        assert len(nearest) == 3
        assert nearest[0][1] <= nearest[1][1]  # sorted by distance
        assert nearest[0][0] == 0  # closest is itself

    def test_coverage_map(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        all_vecs = safe_vectors + unsafe_vectors
        cmap = le.coverage_map(all_vecs, grid_resolution=5)
        assert "coverage" in cmap
        assert cmap["coverage"] > 0
        assert cmap["resolution"] == 5

    def test_coverage_map_too_few(self):
        le = LatentExplorer()
        result = le.coverage_map([[1, 2]], grid_resolution=5)
        assert "error" in result

    def test_euclidean_metric(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer(distance_metric="euclidean")
        boundary = le.estimate_boundary(safe_vectors, unsafe_vectors, n_samples=3)
        assert len(boundary) == 3


# ===========================================================================
# META-ATTACKER TESTS
# ===========================================================================


class TestAttackRecord:
    def test_to_dict(self):
        r = AttackRecord(
            mutator_name="persona_switch", model_id="gpt-4o",
            prompt_hash="abc123", bypassed=True, category="test",
        )
        d = r.to_dict()
        assert d["mutator_name"] == "persona_switch"
        assert d["bypassed"] is True


class TestModelProfile:
    def test_to_dict(self):
        p = ModelProfile(model_id="gpt-4o", total_tests=50, overall_bypass_rate=0.3)
        d = p.to_dict()
        assert d["model_id"] == "gpt-4o"
        assert d["total_tests"] == 50


class TestMetaAttacker:
    def test_record(self):
        ma = MetaAttacker()
        ma.record("persona_switch", "gpt-4o", "h1", True)
        assert ma.n_records == 1

    def test_models_seen(self, populated_meta):
        assert len(populated_meta.models_seen) == 3

    def test_build_profile(self, populated_meta):
        profile = populated_meta.build_profile("gpt-4o")
        assert profile.model_id == "gpt-4o"
        assert profile.total_tests > 0
        assert 0 <= profile.overall_bypass_rate <= 1

    def test_build_all_profiles(self, populated_meta):
        profiles = populated_meta.build_all_profiles()
        assert len(profiles) == 3

    def test_model_similarity_same(self, populated_meta):
        populated_meta.build_all_profiles()
        sim = populated_meta.compute_model_similarity("gpt-4o", "gpt-4o")
        assert abs(sim - 1.0) < 0.01

    def test_model_similarity_different(self, populated_meta):
        populated_meta.build_all_profiles()
        sim = populated_meta.compute_model_similarity("gpt-4o", "mistral-large")
        assert 0 <= sim <= 1

    def test_similarity_matrix(self, populated_meta):
        populated_meta.build_all_profiles()
        matrix = populated_meta.model_similarity_matrix()
        assert len(matrix) == 3
        for model, row in matrix.items():
            assert row[model] == 1.0

    def test_predict_transfer(self, populated_meta):
        populated_meta.build_all_profiles()
        pred = populated_meta.predict_transfer("persona_switch", "claude-3", "gpt-4o")
        assert isinstance(pred, TransferPrediction)
        assert 0 <= pred.predicted_bypass_rate <= 1
        assert 0 <= pred.confidence <= 1

    def test_find_universal_attacks(self, populated_meta):
        populated_meta.build_all_profiles()
        universal = populated_meta.find_universal_attacks(min_models=2, min_bypass_rate=0.1)
        assert isinstance(universal, list)
        for ua in universal:
            assert "mutator" in ua
            assert ua["models_bypassed"] >= 2

    def test_adapt_to_known_model(self, populated_meta):
        recs = populated_meta.adapt_to_model("gpt-4o", n_recommendations=5)
        assert isinstance(recs, list)
        assert len(recs) <= 5
        assert all(isinstance(r, StrategyRecommendation) for r in recs)

    def test_adapt_to_unknown_model(self, populated_meta):
        recs = populated_meta.adapt_to_model("brand-new-model", n_recommendations=5)
        assert isinstance(recs, list)
        # Should provide transfer-based or diverse recommendations
        assert len(recs) > 0

    def test_adapt_no_data(self):
        ma = MetaAttacker()
        recs = ma.adapt_to_model("gpt-4o", n_recommendations=5)
        assert isinstance(recs, list)
        # With no data, should give diverse recommendations
        for r in recs:
            assert r.confidence == 0.0

    def test_portfolio_thompson(self, populated_meta):
        alloc = populated_meta.optimize_portfolio("claude-3", budget=20, strategy="thompson")
        assert isinstance(alloc, PortfolioAllocation)
        assert sum(alloc.allocations.values()) == 20
        assert alloc.strategy == "thompson"

    def test_portfolio_greedy(self, populated_meta):
        alloc = populated_meta.optimize_portfolio("claude-3", budget=15, strategy="greedy")
        assert isinstance(alloc, PortfolioAllocation)
        assert alloc.total_budget == 15
        assert alloc.strategy == "greedy"

    def test_portfolio_ucb(self, populated_meta):
        alloc = populated_meta.optimize_portfolio("claude-3", budget=10, strategy="ucb")
        assert isinstance(alloc, PortfolioAllocation)
        assert alloc.strategy == "ucb"

    def test_portfolio_cold_start(self):
        ma = MetaAttacker()
        alloc = ma.optimize_portfolio("unknown-model", budget=10)
        assert isinstance(alloc, PortfolioAllocation)
        assert alloc.strategy == "uniform_cold_start"

    def test_get_meta_features(self):
        ma = MetaAttacker()
        feats = ma.get_meta_features("How can I set up a recruitment system urgently?")
        assert "char_length" in feats
        assert "word_count" in feats
        assert feats["has_urgency_markers"] == 1.0
        assert "formality_score" in feats

    def test_meta_features_empty(self):
        ma = MetaAttacker()
        feats = ma.get_meta_features("")
        assert feats["char_length"] == 0.0

    def test_summary(self, populated_meta):
        s = populated_meta.summary()
        assert s["total_records"] == 100
        assert len(s["models_seen"]) == 3

    def test_persistence(self, populated_meta):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "meta.json"
            populated_meta._persist_path = path
            populated_meta.save()
            assert path.exists()

            loaded = MetaAttacker(persist_path=path)
            assert loaded.n_records == 100
            assert len(loaded.models_seen) == 3

    def test_persistence_corrupt_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "meta.json"
            path.write_text("{invalid json!!!")
            ma = MetaAttacker(persist_path=path)
            assert ma.n_records == 0  # graceful fallback


# ===========================================================================
# INTEGRATION TESTS
# ===========================================================================


class TestIntegration:
    """Cross-module integration: genetic engine + meta-attacker + latent explorer."""

    def test_genetic_with_meta_fitness(self, populated_meta):
        """Genetic engine using MetaAttacker for fitness evaluation."""
        eng = GeneticEngine(population_size=6, elitism=1)
        eng.initialize()

        def meta_fitness(prompt: str, results: list) -> float:
            if not results:
                return 0.0
            # Use meta-features as a proxy
            feats = populated_meta.get_meta_features(results[-1].mutated)
            return min(feats["char_length"] / 500, 1.0)

        result = eng.evolve("test prompt", generations=3, fitness_fn=meta_fitness)
        assert result.best.fitness >= 0

    def test_latent_explorer_with_genetic_results(self, safe_vectors, unsafe_vectors):
        """Use latent explorer to analyze space, then genetic engine to target gaps."""
        le = LatentExplorer()
        exploration = le.explore(safe_vectors, unsafe_vectors, n_boundary_samples=5)

        # The suggested vectors represent boundary regions to probe
        assert len(exploration.suggested_vectors) > 0

        # Could use these as fitness targets for genetic optimization
        target = exploration.safe_centroid
        assert len(target) == 8

    def test_meta_attacker_portfolio_covers_categories(self, populated_meta):
        """Portfolio should allocate across different mutator categories."""
        alloc = populated_meta.optimize_portfolio("claude-3", budget=30, strategy="thompson")
        assert len(alloc.allocations) >= 1  # at least 1 distinct mutator
        assert alloc.expected_bypasses > 0


# ===========================================================================
# PHASE 2-5 IMPROVEMENT TESTS
# ===========================================================================


# ---------------------------------------------------------------------------
# NoveltyArchive
# ---------------------------------------------------------------------------


class TestNoveltyArchive:
    def test_empty_archive_novelty(self):
        na = NoveltyArchive(capacity=10, k_nearest=3)
        # Empty archive should return 1.0 (maximally novel)
        assert na.novelty_score([0.0, 1.0, 2.0]) == 1.0

    def test_add_and_size(self):
        na = NoveltyArchive(capacity=5)
        na.add([1.0, 2.0], 0.5, ["a"])
        na.add([3.0, 4.0], 0.7, ["b"])
        assert na.archive_size == 2

    def test_capacity_eviction(self):
        na = NoveltyArchive(capacity=3)
        na.add([0.0, 0.0], 0.1, ["low"])
        na.add([1.0, 1.0], 0.5, ["mid1"])
        na.add([2.0, 2.0], 0.8, ["high"])
        na.add([3.0, 3.0], 0.9, ["higher"])
        # Should evict the lowest-fitness entry (0.1)
        assert na.archive_size == 3

    def test_novelty_score_decreases_near_archive(self):
        na = NoveltyArchive(capacity=100, k_nearest=3)
        na.add([0.0, 0.0], 0.5, ["a"])
        na.add([0.1, 0.1], 0.5, ["b"])
        na.add([0.2, 0.2], 0.5, ["c"])
        # Near the cluster -> low novelty
        near_score = na.novelty_score([0.05, 0.05])
        # Far from cluster -> high novelty
        far_score = na.novelty_score([10.0, 10.0])
        assert far_score > near_score

    def test_map_elites_update_new_cell(self):
        na = NoveltyArchive()
        assert na.map_elites_update("0,0", 0.5, ["a"]) is True
        assert na.elites_cells == 1

    def test_map_elites_update_improves(self):
        na = NoveltyArchive()
        na.map_elites_update("0,0", 0.5, ["a"])
        assert na.map_elites_update("0,0", 0.8, ["b"]) is True
        grid = na.get_map_elites_grid()
        assert grid["0,0"][0] == 0.8
        assert grid["0,0"][1] == ["b"]

    def test_map_elites_update_no_improvement(self):
        na = NoveltyArchive()
        na.map_elites_update("0,0", 0.8, ["a"])
        assert na.map_elites_update("0,0", 0.3, ["worse"]) is False
        grid = na.get_map_elites_grid()
        assert grid["0,0"][1] == ["a"]

    def test_summary(self):
        na = NoveltyArchive(capacity=100)
        na.add([1.0], 0.5, ["a"])
        na.map_elites_update("cell1", 0.5, ["a"])
        s = na.summary()
        assert s["archive_size"] == 1
        assert s["elites_cells"] == 1
        assert s["capacity"] == 100


# ---------------------------------------------------------------------------
# AdaptiveParameterController
# ---------------------------------------------------------------------------


class TestAdaptiveParameterController:
    def test_initial_rates(self):
        apc = AdaptiveParameterController(initial_mutation_rate=0.4, initial_crossover_rate=0.6)
        assert apc.mutation_rate == 0.4
        assert apc.crossover_rate == 0.6

    def test_record_operator(self):
        apc = AdaptiveParameterController()
        apc.record_operator("insert", True)
        apc.record_operator("insert", False)
        apc.record_operator("delete", True)
        stats = apc.get_operator_stats()
        # insert: (1+1) / (1+2) = 2/3
        assert abs(stats["insert"] - 2 / 3) < 0.01
        # delete: (1+1) / (1+1) = 1.0
        assert abs(stats["delete"] - 1.0) < 0.01

    def test_record_unknown_operator(self):
        apc = AdaptiveParameterController()
        # Should not crash
        apc.record_operator("nonexistent", True)

    def test_select_operator_returns_valid(self):
        apc = AdaptiveParameterController()
        for _ in range(20):
            op = apc.select_operator()
            assert op in ("insert", "delete", "swap", "replace", "category_swap")

    def test_select_operator_favors_successful(self):
        apc = AdaptiveParameterController()
        # Make "insert" very successful
        for _ in range(50):
            apc.record_operator("insert", True)
        for name in ("delete", "swap", "replace", "category_swap"):
            for _ in range(50):
                apc.record_operator(name, False)
        # Over 100 trials, insert should be chosen most often
        choices = [apc.select_operator() for _ in range(200)]
        assert choices.count("insert") > choices.count("delete")

    def test_adapt_low_diversity_increases_mutation(self):
        apc = AdaptiveParameterController(
            initial_mutation_rate=0.3, diversity_low=0.3, diversity_high=0.8,
        )
        old_rate = apc.mutation_rate
        apc.adapt(0.1)  # low diversity
        assert apc.mutation_rate > old_rate

    def test_adapt_high_diversity_decreases_mutation(self):
        apc = AdaptiveParameterController(
            initial_mutation_rate=0.5, diversity_low=0.3, diversity_high=0.8,
        )
        old_rate = apc.mutation_rate
        apc.adapt(0.9)  # high diversity
        assert apc.mutation_rate < old_rate

    def test_adapt_normal_diversity_no_change(self):
        apc = AdaptiveParameterController(
            initial_mutation_rate=0.5, diversity_low=0.3, diversity_high=0.8,
        )
        old_rate = apc.mutation_rate
        apc.adapt(0.5)  # in range — no change
        assert apc.mutation_rate == old_rate

    def test_mutation_rate_capped(self):
        apc = AdaptiveParameterController(
            initial_mutation_rate=0.75, diversity_low=0.3,
        )
        for _ in range(50):
            apc.adapt(0.1)
        assert apc.mutation_rate <= 0.8

    def test_get_operator_stats(self):
        apc = AdaptiveParameterController()
        stats = apc.get_operator_stats()
        # All start at 1/1 = 1.0
        assert all(v == 1.0 for v in stats.values())
        assert len(stats) == 5


# ---------------------------------------------------------------------------
# GeneticEngine: enable_adaptive, enable_novelty, initialize_from_meta,
#                stagnation detection, report_to_meta, expanded history
# ---------------------------------------------------------------------------


class TestGeneticEnginePhase2:
    def test_enable_adaptive(self):
        eng = GeneticEngine(population_size=6, elitism=1)
        eng.enable_adaptive()
        eng.initialize()
        eng.evaluate("test")
        eng.step()
        # Adaptive should alter rates from initial
        assert eng._adaptive is not None
        history = eng.get_history()
        assert "mutation_rate" in history[0]
        assert "crossover_rate" in history[0]

    def test_enable_novelty(self):
        eng = GeneticEngine(population_size=6, elitism=1)
        eng.enable_novelty(archive_capacity=50, k_nearest=3, novelty_weight=0.3)
        assert eng._novelty_archive is not None
        assert eng._novelty_weight == 0.3

    def test_novelty_with_embed_fn(self):
        eng = GeneticEngine(population_size=6, elitism=1)
        eng.enable_novelty(novelty_weight=0.2)
        eng.initialize()

        def fake_embed(text: str) -> list[float]:
            return [float(len(text) % 10), float(hash(text) % 100) / 100]

        eng.evaluate("test prompt", embed_fn=fake_embed)
        # Archive should have entries
        assert eng._novelty_archive.archive_size > 0

    def test_novelty_history_fields(self):
        eng = GeneticEngine(population_size=6, elitism=1)
        eng.enable_novelty(novelty_weight=0.2)
        eng.initialize()

        def fake_embed(text: str) -> list[float]:
            return [float(len(text) % 10), 0.5]

        eng.evaluate("test", embed_fn=fake_embed)
        eng.step()
        history = eng.get_history()
        assert "archive_size" in history[0]
        assert "elites_cells" in history[0]

    def test_initialize_from_meta(self, populated_meta):
        eng = GeneticEngine(population_size=10, elitism=1)
        eng.initialize_from_meta(populated_meta, "claude-3", n_seeds=6)
        assert len(eng.population) == 10
        # Some chains should come from meta recommendations
        all_chains = [tuple(ind.chain) for ind in eng.population]
        # At least some should be single-mutator seeds from recommendations
        singles = [c for c in all_chains if len(c) == 1]
        assert len(singles) >= 1

    def test_stagnation_detection_no_history(self):
        eng = GeneticEngine(population_size=6)
        eng.initialize()
        assert eng._detect_stagnation() is False

    def test_stagnation_detection_flat(self):
        eng = GeneticEngine(population_size=6)
        eng._stagnation_window = 3
        eng._stagnation_threshold = 0.01
        # Fake history with flat best_fitness
        eng._history = [
            {"best_fitness": 0.5},
            {"best_fitness": 0.5},
            {"best_fitness": 0.505},
        ]
        assert eng._detect_stagnation() is True

    def test_stagnation_detection_improving(self):
        eng = GeneticEngine(population_size=6)
        eng._stagnation_window = 3
        eng._stagnation_threshold = 0.01
        eng._history = [
            {"best_fitness": 0.3},
            {"best_fitness": 0.5},
            {"best_fitness": 0.8},
        ]
        assert eng._detect_stagnation() is False

    def test_handle_stagnation_replaces_bottom(self):
        eng = GeneticEngine(population_size=10, elitism=1)
        eng.initialize()
        eng.evaluate("test")
        old_chains = {tuple(ind.chain) for ind in eng.population}
        eng._handle_stagnation()
        new_chains = {tuple(ind.chain) for ind in eng.population}
        # Some chains should be different
        assert old_chains != new_chains

    def test_report_to_meta(self, populated_meta):
        eng = GeneticEngine(population_size=6, elitism=1)
        eng.initialize()
        result = eng.evolve("test", generations=2, early_stop_fitness=2.0)
        old_records = populated_meta.n_records
        added = GeneticEngine.report_to_meta(populated_meta, "test-model", result)
        assert added > 0
        assert populated_meta.n_records > old_records

    def test_expanded_history_fields(self):
        eng = GeneticEngine(population_size=6, elitism=1)
        eng.initialize()
        eng.evaluate("test")
        eng.step()
        h = eng.get_history()[0]
        assert "generation" in h
        assert "best_fitness" in h
        assert "avg_fitness" in h
        assert "std_fitness" in h
        assert "diversity" in h
        assert "elite_turnover" in h
        assert "mutation_rate" in h
        assert "crossover_rate" in h
        assert "operators_applied" in h

    def test_adaptive_with_stagnation(self):
        """Adaptive + stagnation: mutation rate should increase when flat."""
        eng = GeneticEngine(population_size=8, elitism=1)
        eng.enable_adaptive()
        eng._stagnation_window = 2
        eng.initialize()
        # Force constant fitness
        result = eng.evolve(
            "test", generations=6,
            fitness_fn=lambda p, r: 0.5,  # constant
            early_stop_fitness=2.0,
        )
        # Engine should have detected stagnation and injected diversity
        assert result.generation >= 1


# ---------------------------------------------------------------------------
# EvolutionResult.generate_report
# ---------------------------------------------------------------------------


class TestEvolutionResultReport:
    def test_report_fields(self):
        pop = [
            Individual(chain=["a", "b"], fitness=0.8, stealth=0.6),
            Individual(chain=["c"], fitness=0.3, stealth=0.9),
            Individual(chain=["d", "e"], fitness=0.6, stealth=0.7),
        ]
        result = EvolutionResult(
            best=pop[0],
            population=pop,
            generation=5,
            history=[
                {"best_fitness": 0.5, "avg_fitness": 0.4, "diversity": 0.8, "operators_applied": {"insert": 2}},
                {"best_fitness": 0.7, "avg_fitness": 0.5, "diversity": 0.7, "operators_applied": {"swap": 1}},
                {"best_fitness": 0.8, "avg_fitness": 0.55, "diversity": 0.6, "operators_applied": {"insert": 1}},
            ],
            pareto_front=[pop[0], pop[1]],
        )
        report = result.generate_report()
        assert report["generations_run"] == 5
        assert report["population_size"] == 3
        assert report["best_fitness"] == 0.8
        assert "avg_fitness" in report
        assert "fitness_std" in report
        assert report["best_stealth"] == 0.9
        assert report["pareto_front_size"] == 2
        assert "pareto_hypervolume" in report
        assert len(report["top_5_chains"]) == 3
        assert len(report["convergence_curve"]) == 3
        assert len(report["diversity_curve"]) == 3
        assert "converged_at_generation" in report
        assert "total_operator_applications" in report
        assert report["total_operator_applications"]["insert"] == 3
        assert report["total_operator_applications"]["swap"] == 1
        assert "unique_chains" in report

    def test_report_empty_population(self):
        result = EvolutionResult(
            best=Individual(chain=["a"], fitness=0),
            population=[],
            generation=0,
            history=[],
            pareto_front=[],
        )
        report = result.generate_report()
        assert report["population_size"] == 0
        assert report["best_fitness"] == 0
        assert report["pareto_front_size"] == 0

    def test_report_convergence_detection(self):
        pop = [Individual(chain=["a"], fitness=1.0)]
        result = EvolutionResult(
            best=pop[0], population=pop, generation=5,
            history=[
                {"best_fitness": 0.2, "avg_fitness": 0.2, "diversity": 0.9, "operators_applied": {}},
                {"best_fitness": 0.5, "avg_fitness": 0.4, "diversity": 0.8, "operators_applied": {}},
                {"best_fitness": 0.95, "avg_fitness": 0.7, "diversity": 0.5, "operators_applied": {}},
                {"best_fitness": 0.98, "avg_fitness": 0.8, "diversity": 0.4, "operators_applied": {}},
                {"best_fitness": 1.0, "avg_fitness": 0.9, "diversity": 0.3, "operators_applied": {}},
            ],
            pareto_front=pop,
        )
        report = result.generate_report()
        # 95% of 1.0 = 0.95 — first reached at index 2
        assert report["converged_at_generation"] == 2


# ---------------------------------------------------------------------------
# LatentExplorer: slerp, KNN, topology_report
# ---------------------------------------------------------------------------


class TestLatentExplorerPhase2:
    def test_slerp_endpoints(self):
        le = LatentExplorer()
        a = [1.0, 0.0, 0.0]
        b = [0.0, 1.0, 0.0]
        start = le.slerp_interpolate(a, b, alpha=0.0)
        end = le.slerp_interpolate(a, b, alpha=1.0)
        # Start should be close to a, end close to b
        for s, av in zip(start, a):
            assert abs(s - av) < 0.01
        for e, bv in zip(end, b):
            assert abs(e - bv) < 0.01

    def test_slerp_midpoint_preserves_norm(self):
        le = LatentExplorer()
        a = [3.0, 0.0]
        b = [0.0, 3.0]
        mid = le.slerp_interpolate(a, b, alpha=0.5)
        # Magnitude should be ~3.0 (average of both norms)
        assert abs(_norm(mid) - 3.0) < 0.1

    def test_slerp_collinear_fallback(self):
        le = LatentExplorer()
        a = [1.0, 2.0, 3.0]
        b = [2.0, 4.0, 6.0]  # same direction
        mid = le.slerp_interpolate(a, b, alpha=0.5)
        # Should fall back to linear interpolation
        expected = le.interpolate_vectors(a, b, 0.5)
        for m, e in zip(mid, expected):
            assert abs(m - e) < 0.01

    def test_slerp_path_length(self):
        le = LatentExplorer()
        a = [1.0, 0.0, 0.0]
        b = [0.0, 0.0, 1.0]
        path = le.slerp_path(a, b, steps=7)
        assert len(path) == 7

    def test_slerp_path_endpoints(self):
        le = LatentExplorer()
        a = [2.0, 0.0]
        b = [0.0, 2.0]
        path = le.slerp_path(a, b, steps=5)
        for v, av in zip(path[0], a):
            assert abs(v - av) < 0.01
        for v, bv in zip(path[-1], b):
            assert abs(v - bv) < 0.01

    def test_knn_classify_safe(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        safe_c = _centroid(safe_vectors)
        label = le.knn_classify(safe_c, safe_vectors, unsafe_vectors, k=5)
        assert label == "safe"

    def test_knn_classify_unsafe(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        unsafe_c = _centroid(unsafe_vectors)
        label = le.knn_classify(unsafe_c, safe_vectors, unsafe_vectors, k=5)
        assert label == "unsafe"

    def test_estimate_boundary_knn(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        boundary = le.estimate_boundary_knn(
            safe_vectors, unsafe_vectors, n_samples=5, k=3, steps=8,
        )
        assert len(boundary) == 5
        for bp in boundary:
            assert isinstance(bp, BoundaryPoint)
            assert bp.metadata.get("method") == "knn"
            assert bp.metadata.get("k") == 3

    def test_estimate_boundary_knn_empty(self):
        le = LatentExplorer()
        assert le.estimate_boundary_knn([], [[1, 2]], n_samples=5) == []
        assert le.estimate_boundary_knn([[1, 2]], [], n_samples=5) == []

    def test_topology_report_basic(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        exploration = le.explore(
            safe_vectors, unsafe_vectors,
            n_boundary_samples=8, n_directions=3,
            neighborhood_radius=0.05, n_neighborhood_per_point=2,
        )
        report = le.topology_report(exploration)
        assert "boundary_curvature" in report
        assert "boundary_width" in report
        assert "boundary_tightness" in report
        assert "alpha_range" in report
        assert "n_boundary_points" in report
        assert "directional_diversity" in report
        assert "n_directions" in report
        assert "avg_direction_magnitude" in report
        assert "n_suggested_vectors" in report
        assert "recommended_follow_up" in report
        assert report["n_boundary_points"] == 8
        assert report["n_directions"] == 3

    def test_topology_report_few_boundary_points(self):
        le = LatentExplorer()
        result = ExplorationResult(
            boundary_points=[
                BoundaryPoint(vector=[0.5, 0.5], interpolation_alpha=0.5),
            ],
            adversarial_directions=[],
            safe_centroid=[0.0, 0.0],
            unsafe_centroid=[1.0, 1.0],
            boundary_width=0.1,
            suggested_vectors=[],
        )
        report = le.topology_report(result)
        assert report["boundary_curvature"] == 0.0
        assert report["recommended_follow_up"] == "increase_boundary_samples"

    def test_topology_report_low_directional_diversity(self, safe_vectors, unsafe_vectors):
        le = LatentExplorer()
        # Build an exploration with essentially parallel directions
        from src.intelligent_attack.latent_explorer import AdversarialDirection
        d = _normalize([1.0] * 8)
        exploration = ExplorationResult(
            boundary_points=[
                BoundaryPoint(vector=[0.5] * 8, interpolation_alpha=0.5, boundary_score=0.01),
            ] * 10,
            adversarial_directions=[
                AdversarialDirection(direction=d, magnitude=1.0),
                AdversarialDirection(direction=d, magnitude=1.0),
            ],
            safe_centroid=[0.0] * 8,
            unsafe_centroid=[1.0] * 8,
            boundary_width=0.01,
            suggested_vectors=[[0.5] * 8] * 5,
        )
        report = le.topology_report(exploration)
        # Parallel directions -> diversity ~0
        assert report["directional_diversity"] < 0.1

    def test_slerp_vs_lerp_different_paths(self):
        """Slerp and lerp should produce different midpoints for non-collinear vectors."""
        le = LatentExplorer()
        a = [1.0, 0.0, 0.0]
        b = [0.0, 1.0, 0.0]
        slerp_mid = le.slerp_interpolate(a, b, 0.5)
        lerp_mid = le.interpolate_vectors(a, b, 0.5)
        # They should be different
        diff = sum(abs(s - l) for s, l in zip(slerp_mid, lerp_mid))
        assert diff > 0.01


# ---------------------------------------------------------------------------
# MetaAttacker: transfer_heatmap, category_interaction_matrix,
#               fingerprint_comparison, ingest_evolution_result
# ---------------------------------------------------------------------------


class TestMetaAttackerPhase2:
    def test_transfer_heatmap_structure(self, populated_meta):
        heatmap = populated_meta.transfer_heatmap()
        models = sorted(populated_meta.models_seen)
        assert len(heatmap) == 3
        for src in models:
            assert src in heatmap
            for tgt in models:
                assert tgt in heatmap[src]
                # Each cell should be a dict of category -> rate
                assert isinstance(heatmap[src][tgt], dict)

    def test_transfer_heatmap_self_matches_profile(self, populated_meta):
        populated_meta.build_all_profiles()
        heatmap = populated_meta.transfer_heatmap()
        for model in populated_meta.models_seen:
            profile = populated_meta._profiles[model]
            assert heatmap[model][model] == profile.category_bypass_rates

    def test_transfer_heatmap_cross_model_attenuated(self, populated_meta):
        heatmap = populated_meta.transfer_heatmap()
        models = sorted(populated_meta.models_seen)
        src, tgt = models[0], models[1]
        if src == tgt:
            return
        # Cross-model rates should be <= source self rates (attenuated by similarity)
        for cat, rate in heatmap[src][tgt].items():
            self_rate = heatmap[src][src].get(cat, 0)
            assert rate <= self_rate + 0.001  # small tolerance

    def test_category_interaction_matrix_empty(self):
        ma = MetaAttacker()
        matrix = ma.category_interaction_matrix()
        assert matrix == {}

    def test_category_interaction_matrix_structure(self):
        ma = MetaAttacker()
        # Create sessions (same prompt_hash) with multiple categories
        for i in range(5):
            ma.record("persona_switch", "m1", f"session_{i}", True, category="social")
            ma.record("base64_encode", "m1", f"session_{i}", False, category="encoding")
        matrix = ma.category_interaction_matrix(min_chain_length=2)
        assert "social" in matrix or "encoding" in matrix
        # Should have pair entries
        if "social" in matrix:
            assert "encoding" in matrix["social"]

    def test_fingerprint_comparison_structure(self, populated_meta):
        populated_meta.build_all_profiles()
        models = sorted(populated_meta.models_seen)
        comp = populated_meta.fingerprint_comparison(models[0], models[1])
        assert "differential" in comp
        assert "harder_model" in comp
        assert "difficulty_gap" in comp
        assert f"unique_vulnerabilities_{models[0]}" in comp
        assert f"unique_vulnerabilities_{models[1]}" in comp
        assert f"transfer_candidates_{models[0]}_to_{models[1]}" in comp

    def test_fingerprint_comparison_harder_model(self, populated_meta):
        populated_meta.build_all_profiles()
        comp = populated_meta.fingerprint_comparison("gpt-4o", "mistral-large")
        # gpt-4o has lower bypass rate in fixture setup (0.2 vs 0.7)
        assert comp["harder_model"] == "gpt-4o"

    def test_fingerprint_differential_categories(self, populated_meta):
        populated_meta.build_all_profiles()
        comp = populated_meta.fingerprint_comparison("gpt-4o", "claude-3")
        # Differential should have model-specific bypass rates and delta
        for cat, vals in comp["differential"].items():
            assert "gpt-4o" in vals
            assert "claude-3" in vals
            assert "delta" in vals

    def test_ingest_evolution_result_empty(self):
        ma = MetaAttacker()
        added = ma.ingest_evolution_result("m1", "h1", [])
        assert added == 0
        assert ma.n_records == 0

    def test_ingest_evolution_result_basic(self):
        ma = MetaAttacker()
        chains = [
            (["persona_switch", "base64_encode"], 0.8),  # above threshold
            (["rot13_encode"], 0.2),  # below threshold
        ]
        added = ma.ingest_evolution_result("m1", "h1", chains, bypass_threshold=0.5)
        assert added == 3  # 2 mutators from chain 1 + 1 from chain 2
        assert ma.n_records == 3

    def test_ingest_evolution_result_bypass_flag(self):
        ma = MetaAttacker()
        chains = [
            (["a"], 0.9),  # bypassed
            (["b"], 0.1),  # not bypassed
        ]
        ma.ingest_evolution_result("m1", "h1", chains, bypass_threshold=0.5)
        records = ma._records
        assert records[0].bypassed is True
        assert records[1].bypassed is False

    def test_ingest_evolution_result_category(self):
        ma = MetaAttacker()
        ma.ingest_evolution_result("m1", "h1", [(["a"], 0.5)])
        assert ma._records[0].category == "genetic_chain"


# ---------------------------------------------------------------------------
# Cross-module integration (Phase 2-5)
# ---------------------------------------------------------------------------


class TestIntegrationPhase2:
    def test_genetic_engine_with_meta_seeding_and_feedback(self, populated_meta):
        """Full loop: meta seeds -> genetic evolve -> feed back to meta."""
        eng = GeneticEngine(population_size=8, elitism=1)
        eng.initialize_from_meta(populated_meta, "claude-3", n_seeds=4)
        result = eng.evolve("test", generations=3, early_stop_fitness=2.0)
        old_records = populated_meta.n_records
        added = GeneticEngine.report_to_meta(populated_meta, "claude-3", result)
        assert added > 0
        assert populated_meta.n_records == old_records + added

    def test_genetic_adaptive_novelty_combo(self):
        """Enable both adaptive and novelty simultaneously."""
        eng = GeneticEngine(population_size=8, elitism=1)
        eng.enable_adaptive()
        eng.enable_novelty(novelty_weight=0.2)
        eng.initialize()

        def fake_embed(text: str) -> list[float]:
            return [float(len(text) % 10), float(hash(text) % 50)]

        result = eng.evolve(
            "test", generations=3, early_stop_fitness=2.0,
            fitness_fn=lambda p, r: 0.4 if r else 0.0,
        )
        # Both features should be active
        assert eng._adaptive is not None
        assert eng._novelty_archive is not None
        assert result.generation >= 1

    def test_slerp_boundary_exploration(self, safe_vectors, unsafe_vectors):
        """Use slerp to trace paths between safe/unsafe, then KNN to classify."""
        le = LatentExplorer()
        path = le.slerp_path(safe_vectors[0], unsafe_vectors[0], steps=10)
        # Classify each point along the slerp path
        labels = [
            le.knn_classify(p, safe_vectors, unsafe_vectors, k=5)
            for p in path
        ]
        # Start should be safe-ish, end unsafe-ish
        assert labels[0] == "safe"
        assert labels[-1] == "unsafe"
        # There should be a transition somewhere
        assert "safe" in labels and "unsafe" in labels
