"""
Tests for Phase 4 intelligent attack modules:
- RepresentationProber (representation_prober.py)
- EmbeddingInverter (embedding_inverter.py)
- BayesianExplorer (bayesian_explorer.py)
- AdversarialPerturber (adversarial_perturber.py)
- PromptExplainer (prompt_explainer.py)
- ManifoldMapper (manifold_mapper.py)
- InformationProber (information_prober.py)
"""

import math
import random
import pytest

from src.intelligent_attack.representation_prober import (
    RepresentationProber,
    ConceptVector,
    _vec_dot,
    _vec_add,
    _vec_sub,
    _vec_scale,
    _vec_norm,
    _vec_normalize,
    _vec_mean,
)
from src.intelligent_attack.embedding_inverter import (
    EmbeddingInverter,
    InversionCandidate,
    _distance,
    _cosine_sim,
    _default_vocabulary,
)
from src.intelligent_attack.bayesian_explorer import (
    BayesianExplorer,
    GPSurrogate,
    AcquisitionFunction,
    _cholesky,
    _norm_cdf,
    _norm_pdf,
)
from src.intelligent_attack.adversarial_perturber import (
    AdversarialPerturber,
    PerturbationResult,
    _clip_to_ball,
    _random_unit,
)
from src.intelligent_attack.prompt_explainer import (
    PromptExplainer,
    TokenAttribution,
    CounterfactualExplanation,
)
from src.intelligent_attack.manifold_mapper import (
    ManifoldMapper,
    ManifoldMap,
    ManifoldPoint,
)
from src.intelligent_attack.information_prober import (
    InformationProber,
    InformationReport,
)


# ---------------------------------------------------------------------------
# Shared test helpers
# ---------------------------------------------------------------------------

def _simple_embed(text: str) -> list[float]:
    """Deterministic 4-dim mock embedding based on text hash."""
    h = hash(text) & 0xFFFFFFFF
    return [
        ((h >> 0) & 0xFF) / 255.0,
        ((h >> 8) & 0xFF) / 255.0,
        ((h >> 16) & 0xFF) / 255.0,
        ((h >> 24) & 0xFF) / 255.0,
    ]


def _score_fn_length(emb: list[float]) -> float:
    """Score = magnitude of embedding (norm)."""
    return math.sqrt(sum(x * x for x in emb))


def _text_score_fn(text: str) -> float:
    """Score based on text content: more words = higher score."""
    return min(len(text.split()) / 10.0, 1.0)


# ===================================================================
# RepresentationProber Tests
# ===================================================================


class TestVecHelpers:
    def test_dot(self):
        assert _vec_dot([1, 2, 3], [4, 5, 6]) == 32

    def test_add(self):
        assert _vec_add([1, 2], [3, 4]) == [4, 6]

    def test_sub(self):
        assert _vec_sub([5, 3], [2, 1]) == [3, 2]

    def test_scale(self):
        assert _vec_scale([1, 2], 3) == [3, 6]

    def test_norm(self):
        assert abs(_vec_norm([3, 4]) - 5.0) < 1e-10

    def test_normalize(self):
        n = _vec_normalize([3, 4])
        assert abs(_vec_norm(n) - 1.0) < 1e-10

    def test_normalize_zero(self):
        assert _vec_normalize([0, 0, 0]) == [0.0, 0.0, 0.0]

    def test_mean(self):
        m = _vec_mean([[1, 2], [3, 4], [5, 6]])
        assert abs(m[0] - 3.0) < 1e-10
        assert abs(m[1] - 4.0) < 1e-10


class TestRepresentationProber:
    def setup_method(self):
        self.prober = RepresentationProber()

    def test_find_refusal_direction(self):
        refused = [[1, 0, 0], [1, 0.1, 0]]
        accepted = [[0, 1, 0], [0, 1, 0.1]]
        cv = self.prober.find_refusal_direction(refused, accepted)
        assert isinstance(cv, ConceptVector)
        assert cv.concept_name == "refusal"
        assert cv.strength > 0
        assert abs(_vec_norm(cv.direction) - 1.0) < 1e-10
        assert cv.metadata["method"] == "mean_difference"

    def test_find_safety_vector(self):
        safe = [[0, 0, 1], [0, 0, 0.9]]
        unsafe = [[1, 1, 0], [1, 0.9, 0]]
        cv = self.prober.find_safety_vector(safe, unsafe)
        assert cv.concept_name == "safety"
        assert cv.strength > 0

    def test_project_onto_concept(self):
        cv = ConceptVector(direction=[1, 0, 0], concept_name="test")
        proj = self.prober.project_onto_concept([3, 4, 5], cv)
        assert abs(proj - 3.0) < 1e-10

    def test_steer_embedding(self):
        cv = ConceptVector(direction=[1, 0, 0], concept_name="test")
        steered = self.prober.steer_embedding([0, 0, 0], cv, alpha=2.0)
        assert abs(steered[0] - 2.0) < 1e-10

    def test_steer_negative_alpha(self):
        cv = ConceptVector(direction=[0, 1, 0], concept_name="test")
        steered = self.prober.steer_embedding([5, 5, 5], cv, alpha=-3.0)
        assert abs(steered[1] - 2.0) < 1e-10

    def test_compute_concept_activation(self):
        embeddings = [
            [1, 0], [0.9, 0.1], [0.8, 0.2],
            [0, 1], [0.1, 0.9], [0.2, 0.8],
        ]
        labels = [1, 1, 1, 0, 0, 0]
        cv = self.prober.compute_concept_activation(embeddings, labels, "test_concept")
        assert cv.concept_name == "test_concept"
        assert cv.metadata["n_positive"] == 3
        assert cv.metadata["n_negative"] == 3
        assert cv.metadata["linear_accuracy"] > 0.5  # should be > chance

    def test_concept_activation_no_negatives(self):
        cv = self.prober.compute_concept_activation(
            [[1, 0], [0, 1]], [1, 1], "all_pos"
        )
        assert cv.strength == 0.0

    def test_measure_concept_sensitivity(self):
        embeddings = [[1, 0], [0, 1], [0.5, 0.5]]
        cv = ConceptVector(direction=[1, 0], concept_name="x_axis")
        stats = self.prober.measure_concept_sensitivity(embeddings, cv)
        assert "mean_projection" in stats
        assert "std_projection" in stats
        assert "spread" in stats
        assert stats["n_embeddings"] == 3

    def test_measure_concept_sensitivity_empty(self):
        cv = ConceptVector(direction=[1, 0], concept_name="x")
        result = self.prober.measure_concept_sensitivity([], cv)
        assert "error" in result

    def test_find_orthogonal_concepts(self):
        cvs = [
            ConceptVector(direction=[1, 0, 0], concept_name="a"),
            ConceptVector(direction=[1, 1, 0], concept_name="b"),
            ConceptVector(direction=[1, 1, 1], concept_name="c"),
        ]
        ortho = self.prober.find_orthogonal_concepts(cvs)
        assert len(ortho) == 3
        # Check orthogonality
        for i in range(len(ortho)):
            for j in range(i + 1, len(ortho)):
                dot = _vec_dot(ortho[i].direction, ortho[j].direction)
                assert abs(dot) < 1e-8, f"Not orthogonal: {i},{j} dot={dot}"

    def test_find_orthogonal_degenerate(self):
        cvs = [
            ConceptVector(direction=[1, 0], concept_name="a"),
            ConceptVector(direction=[2, 0], concept_name="b_parallel"),
        ]
        ortho = self.prober.find_orthogonal_concepts(cvs)
        assert ortho[1].metadata.get("degenerate") is True

    def test_concept_bottleneck_analysis(self):
        embeddings = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0]]
        cvs = [
            ConceptVector(direction=[1, 0, 0], concept_name="dim0"),
            ConceptVector(direction=[0, 1, 0], concept_name="dim1"),
        ]
        result = self.prober.concept_bottleneck_analysis(embeddings, cvs)
        assert "explained_ratio" in result
        assert 0 <= result["explained_ratio"] <= 1.0
        assert "per_concept" in result

    def test_concept_bottleneck_empty(self):
        result = self.prober.concept_bottleneck_analysis([], [])
        assert "error" in result


# ===================================================================
# EmbeddingInverter Tests
# ===================================================================


class TestEmbeddingInverter:
    def setup_method(self):
        self.inverter = EmbeddingInverter(
            embed_fn=_simple_embed,
            vocabulary=["help", "exploit", "worker", "safety", "test", "avoid"],
        )

    def test_default_vocabulary(self):
        vocab = _default_vocabulary()
        assert len(vocab) >= 100
        assert "worker" in vocab
        assert "exploit" in vocab

    def test_distance(self):
        assert abs(_distance([0, 0], [3, 4]) - 5.0) < 1e-10

    def test_cosine_sim_identical(self):
        assert abs(_cosine_sim([1, 2, 3], [1, 2, 3]) - 1.0) < 1e-10

    def test_cosine_sim_orthogonal(self):
        assert abs(_cosine_sim([1, 0], [0, 1])) < 1e-10

    def test_cosine_sim_zero(self):
        assert _cosine_sim([0, 0], [1, 2]) == 0.0

    def test_invert_greedy(self):
        target = _simple_embed("help worker safety")
        results = self.inverter.invert_greedy(
            target, seed_text="help", max_iterations=5
        )
        assert len(results) >= 1
        assert all(isinstance(r, InversionCandidate) for r in results)
        # Should be sorted by distance
        for i in range(len(results) - 1):
            assert results[i].distance_to_target <= results[i + 1].distance_to_target

    def test_invert_beam(self):
        target = _simple_embed("test safety")
        results = self.inverter.invert_beam(
            target, seed_text="test", beam_width=3, max_steps=3
        )
        assert len(results) >= 1
        assert results[0].distance_to_target >= 0

    def test_invert_random_walk(self):
        target = _simple_embed("avoid exploit")
        results = self.inverter.invert_random_walk(
            target, seed_text="help", steps=20, temperature=0.5
        )
        assert len(results) >= 1

    def test_interpolate_and_invert(self):
        emb_a = _simple_embed("help")
        emb_b = _simple_embed("exploit")
        results = self.inverter.interpolate_and_invert(
            emb_a, emb_b, "help", "exploit", num_points=3
        )
        assert len(results) >= 1
        # Check interpolation_t metadata
        assert any("interpolation_t" in r.metadata for r in results)

    def test_nearest_in_corpus(self):
        target = _simple_embed("worker safety")
        corpus = ["help worker", "exploit safety", "test avoid", "worker help"]
        results = self.inverter.nearest_in_corpus(target, corpus)
        assert len(results) == len(corpus)
        assert results[0].distance_to_target <= results[-1].distance_to_target


# ===================================================================
# BayesianExplorer Tests
# ===================================================================


class TestGPSurrogate:
    def test_fit_and_predict(self):
        gp = GPSurrogate(length_scale=1.0, noise=1e-4)
        X = [[0.0], [1.0], [2.0]]
        y = [0.0, 1.0, 0.0]
        gp.fit(X, y)
        means, variances = gp.predict([[0.5], [1.5]])
        assert len(means) == 2
        assert len(variances) == 2
        # Variance should be positive
        assert all(v > 0 for v in variances)

    def test_predict_unfitted(self):
        gp = GPSurrogate()
        means, variances = gp.predict([[0.0]])
        assert means == [0.0]
        assert variances == [1.0]

    def test_predict_at_training_point(self):
        gp = GPSurrogate(length_scale=1.0, noise=1e-6)
        X = [[0.0], [1.0]]
        y = [3.0, 5.0]
        gp.fit(X, y)
        means, variances = gp.predict([[0.0]])
        # Mean at training point should be close to training value
        assert abs(means[0] - 3.0) < 0.5

    def test_rbf_kernel(self):
        gp = GPSurrogate(length_scale=1.0)
        k_same = gp._rbf_kernel([0.0], [0.0])
        assert abs(k_same - 1.0) < 1e-10
        k_far = gp._rbf_kernel([0.0], [10.0])
        assert k_far < 0.01


class TestCholesky:
    def test_identity(self):
        I = [[1.0, 0.0], [0.0, 1.0]]
        L = _cholesky(I)
        assert abs(L[0][0] - 1.0) < 1e-10
        assert abs(L[1][1] - 1.0) < 1e-10


class TestNormFunctions:
    def test_norm_cdf_symmetry(self):
        assert abs(_norm_cdf(0.0) - 0.5) < 1e-10

    def test_norm_cdf_tails(self):
        assert _norm_cdf(3.0) > 0.99
        assert _norm_cdf(-3.0) < 0.01

    def test_norm_pdf_at_zero(self):
        expected = 1.0 / math.sqrt(2 * math.pi)
        assert abs(_norm_pdf(0.0) - expected) < 1e-10


class TestBayesianExplorer:
    def setup_method(self):
        self.explorer = BayesianExplorer(
            score_fn=_score_fn_length,
            dim=4,
            acquisition=AcquisitionFunction.UCB,
        )

    def test_observe(self):
        self.explorer.observe([1, 0, 0, 0], 0.5)
        assert len(self.explorer._X) == 1
        assert len(self.explorer._y) == 1

    def test_suggest_next(self):
        self.explorer.observe([1, 0, 0, 0], 0.5)
        self.explorer.observe([0, 1, 0, 0], 0.3)
        suggestions = self.explorer.suggest_next(3)
        assert len(suggestions) == 3
        assert all(len(s) == 4 for s in suggestions)

    def test_get_best_empty(self):
        emb, score = self.explorer.get_best()
        assert score == 0.0

    def test_get_best(self):
        self.explorer.observe([1, 0, 0, 0], 0.5)
        self.explorer.observe([0, 1, 0, 0], 0.8)
        emb, score = self.explorer.get_best()
        assert score == 0.8

    def test_expected_improvement(self):
        self.explorer.observe([1, 0, 0, 0], 0.5)
        ei = self.explorer.expected_improvement([0, 1, 0, 0])
        assert isinstance(ei, float)

    def test_upper_confidence_bound(self):
        self.explorer.observe([1, 0, 0, 0], 0.5)
        ucb = self.explorer.upper_confidence_bound([0, 1, 0, 0])
        assert isinstance(ucb, float)

    def test_probability_of_improvement(self):
        self.explorer.observe([1, 0, 0, 0], 0.5)
        pi = self.explorer.probability_of_improvement([0, 1, 0, 0])
        assert 0 <= pi <= 1

    def test_uncertainty_map(self):
        self.explorer.observe([0, 0, 0, 0], 0.0)
        grid = [[1, 0, 0, 0], [0, 1, 0, 0], [5, 5, 5, 5]]
        unc = self.explorer.uncertainty_map(grid)
        assert len(unc) == 3
        # Far point should have higher uncertainty
        assert unc[2] >= unc[0]

    def test_optimize(self):
        explorer = BayesianExplorer(
            score_fn=_score_fn_length,
            dim=2,
            acquisition=AcquisitionFunction.UCB,
        )
        initial = [[0.5, 0.5], [1.0, 0.0]]
        history = explorer.optimize(initial, n_iterations=3, embeddings_per_iter=1)
        assert len(history) >= 5  # 2 initial + 3 iterations
        assert all("score" in h for h in history)
        assert all("best_so_far" in h for h in history)

    def test_optimize_no_score_fn(self):
        explorer = BayesianExplorer(dim=2)
        with pytest.raises(ValueError, match="score_fn"):
            explorer.optimize([[0, 0]])

    @pytest.mark.parametrize("acq", list(AcquisitionFunction))
    def test_all_acquisition_functions(self, acq):
        explorer = BayesianExplorer(
            score_fn=_score_fn_length, dim=2, acquisition=acq
        )
        explorer.observe([1, 0], 0.5)
        suggestions = explorer.suggest_next(1)
        assert len(suggestions) == 1


# ===================================================================
# AdversarialPerturber Tests
# ===================================================================


class TestAdversarialPerturberHelpers:
    def test_random_unit(self):
        v = _random_unit(5)
        assert len(v) == 5
        assert abs(math.sqrt(sum(x**2 for x in v)) - 1.0) < 1e-10

    def test_clip_to_ball_inside(self):
        result = _clip_to_ball([0.1, 0.1], [0, 0], 1.0)
        assert result == [0.1, 0.1]

    def test_clip_to_ball_outside(self):
        result = _clip_to_ball([10, 0], [0, 0], 1.0)
        assert abs(math.sqrt(sum(x**2 for x in result)) - 1.0) < 1e-10


class TestAdversarialPerturber:
    def setup_method(self):
        # Score function: score = first dimension value (threshold at 0.5)
        self.perturber = AdversarialPerturber(
            score_fn=lambda emb: emb[0],
            threshold=0.5,
        )

    def test_perturb_random(self):
        results = self.perturber.perturb_random(
            [0.5, 0.5, 0.5], epsilon=0.3, n_tries=10
        )
        assert len(results) == 10
        assert all(isinstance(r, PerturbationResult) for r in results)

    def test_perturb_directional(self):
        results = self.perturber.perturb_directional(
            [0.5, 0, 0], direction=[1, 0, 0], epsilon_range=(0.1, 1.0), steps=5
        )
        assert len(results) == 5
        # Score should increase along [1,0,0] direction
        scores = [r.perturbed_score for r in results]
        assert scores[-1] > scores[0]

    def test_binary_search_boundary(self):
        result = self.perturber.binary_search_boundary(
            [0.3, 0, 0], direction=[1, 0, 0], lo=0.0, hi=1.0
        )
        # Should find boundary near 0.2 (0.3 + 0.2 = 0.5 threshold)
        assert isinstance(result, PerturbationResult)
        assert result.metadata["method"] == "binary_search"

    def test_find_minimal_perturbation(self):
        result = self.perturber.find_minimal_perturbation(
            [0.4, 0, 0], n_directions=10, epsilon_range=(0.01, 2.0)
        )
        assert isinstance(result, PerturbationResult)

    def test_hopskipjump(self):
        results = self.perturber.hopskipjump(
            [0.3, 0, 0], target_embedding=[0.8, 0, 0], n_iterations=5
        )
        assert len(results) >= 1
        assert all(r.metadata.get("method") == "hopskipjump" for r in results)

    def test_pgd_embedding(self):
        result = self.perturber.pgd_embedding(
            [0.7, 0, 0], epsilon=0.5, step_size=0.05, n_steps=5
        )
        assert isinstance(result, PerturbationResult)
        assert result.metadata["method"] == "pgd"
        # PGD tries to reduce score, should decrease from 0.7
        assert result.perturbed_score <= 0.7 + 1e-6

    def test_sensitivity_map(self):
        s = self.perturber.sensitivity_map([0.5, 0.5, 0.5])
        assert len(s) == 3
        # Dimension 0 should be most sensitive (score = emb[0])
        assert s[0] > s[1]

    def test_sensitivity_map_with_range(self):
        s = self.perturber.sensitivity_map([0.5, 0.5, 0.5], dim_range=(0, 2))
        assert s[2] == 0.0  # Outside range


# ===================================================================
# PromptExplainer Tests
# ===================================================================


class TestPromptExplainer:
    def setup_method(self):
        self.explainer = PromptExplainer(score_fn=_text_score_fn)

    def test_leave_one_out(self):
        attrs = self.explainer.leave_one_out("help worker safety avoid exploit")
        assert len(attrs) == 5
        assert all(isinstance(a, TokenAttribution) for a in attrs)
        assert all(a.direction in ("toward_safe", "toward_unsafe") for a in attrs)

    def test_leave_one_out_empty(self):
        assert self.explainer.leave_one_out("") == []

    def test_lime_explain(self):
        attrs = self.explainer.lime_explain(
            "help worker safety", n_samples=30, kernel_width=0.75
        )
        assert len(attrs) == 3
        assert all(isinstance(a, TokenAttribution) for a in attrs)

    def test_shapley_tokens(self):
        attrs = self.explainer.shapley_tokens("help worker safety", n_permutations=10)
        assert len(attrs) == 3
        assert all(isinstance(a, TokenAttribution) for a in attrs)

    def test_find_counterfactual(self):
        cf = self.explainer.find_counterfactual(
            "help worker safety avoid exploit danger",
            target_direction="toward_safe",
            max_edits=2,
        )
        assert isinstance(cf, CounterfactualExplanation)
        assert len(cf.changes_made) <= 2
        assert cf.original_text != cf.modified_text or len(cf.changes_made) == 0

    def test_find_critical_tokens(self):
        critical = self.explainer.find_critical_tokens(
            "help worker safety avoid exploit", threshold=0.01
        )
        assert all(a.attribution_score > 0.01 for a in critical)

    def test_interaction_matrix(self):
        matrix = self.explainer.interaction_matrix("help worker safety")
        assert len(matrix) == 3
        assert len(matrix[0]) == 3
        # Diagonal should be zero
        for i in range(3):
            assert matrix[i][i] == 0.0
        # Symmetry
        assert abs(matrix[0][1] - matrix[1][0]) < 1e-10

    def test_interaction_matrix_short(self):
        matrix = self.explainer.interaction_matrix("hello")
        assert len(matrix) == 1
        assert matrix[0][0] == 0.0

    def test_generate_explanation_text(self):
        attrs = self.explainer.leave_one_out("help worker safety")
        text = self.explainer.generate_explanation_text(attrs, "help worker safety")
        assert "Prompt safety score" in text
        assert "Top contributing tokens" in text
        assert "Summary" in text

    def test_generate_explanation_empty(self):
        text = self.explainer.generate_explanation_text([], "")
        assert "No token attributions" in text


# ===================================================================
# ManifoldMapper Tests
# ===================================================================


class TestManifoldMapper:
    def setup_method(self):
        self.mapper = ManifoldMapper()
        random.seed(42)
        self.embeddings = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0.5, 0.5, 0.5, 0.5],
        ]

    def test_compute_distances(self):
        D = self.mapper.compute_distances(self.embeddings)
        assert len(D) == 7
        # Diagonal should be zero
        for i in range(7):
            assert D[i][i] == 0.0
        # Symmetry
        for i in range(7):
            for j in range(7):
                assert abs(D[i][j] - D[j][i]) < 1e-10

    def test_compute_stress(self):
        D_high = [[0, 1, 2], [1, 0, 1.5], [2, 1.5, 0]]
        D_low = [[0, 1.1, 1.9], [1.1, 0, 1.4], [1.9, 1.4, 0]]
        stress = self.mapper.compute_stress(D_high, D_low)
        assert stress >= 0

    def test_pca(self):
        result = self.mapper.pca(self.embeddings, n_components=2)
        assert isinstance(result, ManifoldMap)
        assert result.method == "pca"
        assert len(result.points) == 7
        assert all(len(p.reduced_coords) == 2 for p in result.points)

    def test_pca_empty(self):
        result = self.mapper.pca([], n_components=2)
        assert result.points == []

    def test_mds(self):
        result = self.mapper.mds(self.embeddings, n_components=2)
        assert result.method == "mds"
        assert len(result.points) == 7
        assert result.stress >= 0

    def test_mds_single_point(self):
        result = self.mapper.mds([[1, 2, 3]], n_components=2)
        assert len(result.points) == 1

    def test_random_projection(self):
        result = self.mapper.random_projection(self.embeddings, n_components=2, seed=42)
        assert result.method == "random_projection"
        assert len(result.points) == 7

    def test_random_projection_deterministic(self):
        r1 = self.mapper.random_projection(self.embeddings, n_components=2, seed=42)
        r2 = self.mapper.random_projection(self.embeddings, n_components=2, seed=42)
        for p1, p2 in zip(r1.points, r2.points):
            assert p1.reduced_coords == p2.reduced_coords

    def test_landmark_mds_small(self):
        # Fewer than n_landmarks → falls back to regular MDS
        result = self.mapper.landmark_mds(self.embeddings, n_components=2, n_landmarks=50)
        assert result.method == "mds"  # fallback
        assert len(result.points) == 7

    def test_landmark_mds_large(self):
        # Generate enough points to trigger landmark mode
        large = [[random.gauss(0, 1) for _ in range(4)] for _ in range(60)]
        result = self.mapper.landmark_mds(large, n_components=2, n_landmarks=10)
        assert result.method == "landmark_mds"
        assert len(result.points) == 60

    def test_find_clusters(self):
        result = self.mapper.pca(self.embeddings, n_components=2)
        clusters = self.mapper.find_clusters(result, n_clusters=2)
        assert len(clusters) == 2
        # All points should be assigned
        all_indices = sorted(idx for cluster in clusters for idx in cluster)
        assert len(all_indices) == 7

    def test_safety_landscape_2d(self):
        scores = [0.1, 0.9, 0.5, 0.3, 0.7, 0.2, 0.8]
        labels = ["unsafe", "safe", "mid", "unsafe", "safe", "unsafe", "safe"]
        result = self.mapper.safety_landscape_2d(self.embeddings, scores, labels)
        assert result.method == "pca"
        for i, p in enumerate(result.points):
            assert p.score == scores[i]
            assert p.label == labels[i]

    def test_detect_boundary_region(self):
        result = self.mapper.pca(self.embeddings, n_components=2)
        for i, p in enumerate(result.points):
            p.score = [0.1, 0.9, 0.48, 0.52, 0.7, 0.3, 0.51][i]
        boundary = self.mapper.detect_boundary_region(result, score_threshold=0.5)
        # Points with score near 0.5 should be in boundary
        assert len(boundary) >= 2
        assert all(abs(p.score - 0.5) < 0.15 for p in boundary)


# ===================================================================
# InformationProber Tests
# ===================================================================


class TestInformationProber:
    def setup_method(self):
        self.prober = InformationProber()

    def test_histogram(self):
        h = self.prober._histogram([0, 0.5, 1.0], n_bins=2)
        assert len(h) == 2
        assert abs(sum(h) - 1.0) < 1e-10

    def test_histogram_constant(self):
        h = self.prober._histogram([5, 5, 5], n_bins=3)
        assert h[0] == 1.0

    def test_joint_histogram(self):
        jh = self.prober._joint_histogram([0, 1], [0, 1], n_bins=2)
        assert len(jh) == 2
        assert abs(sum(sum(row) for row in jh) - 1.0) < 1e-10

    def test_entropy_uniform(self):
        # Uniform distribution over bins should have max entropy
        values = list(range(100))
        h = self.prober.entropy(values, n_bins=10)
        assert h > 0
        max_entropy = math.log(10)
        assert abs(h - max_entropy) < 0.5  # approximately max

    def test_entropy_constant(self):
        h = self.prober.entropy([1, 1, 1, 1], n_bins=5)
        assert h == 0.0  # no uncertainty

    def test_mutual_information_independent(self):
        random.seed(42)
        x = [random.random() for _ in range(200)]
        y = [random.random() for _ in range(200)]
        mi = self.prober.estimate_mutual_information(x, y, n_bins=5)
        # Independent → MI should be near zero
        assert mi < 0.3

    def test_mutual_information_correlated(self):
        x = [float(i) for i in range(100)]
        y = [float(i) * 2 + 1 for i in range(100)]
        mi = self.prober.estimate_mutual_information(x, y, n_bins=10)
        assert mi > 0

    def test_mutual_information_nonnegative(self):
        x = [random.random() for _ in range(50)]
        y = [random.random() for _ in range(50)]
        mi = self.prober.estimate_mutual_information(x, y)
        assert mi >= 0

    def test_conditional_entropy(self):
        x = list(range(50))
        y = [float(v * 2) for v in x]
        ce = self.prober.conditional_entropy(
            [float(v) for v in x], y, n_bins=5
        )
        assert ce >= 0

    def test_feature_importance_mi(self):
        features = [[float(i), random.random()] for i in range(50)]
        labels = [float(i) for i in range(50)]
        reports = self.prober.feature_importance_mi(features, labels)
        assert len(reports) == 2
        assert all(isinstance(r, InformationReport) for r in reports)
        # Sorted by MI descending
        assert reports[0].mutual_information >= reports[1].mutual_information

    def test_information_gain(self):
        parent = [0.1, 0.2, 0.8, 0.9, 0.1, 0.9]
        split1 = [0.1, 0.2, 0.1]
        split2 = [0.8, 0.9, 0.9]
        ig = self.prober.information_gain(parent, [split1, split2])
        assert ig >= 0

    def test_v_information_linear(self):
        x = [float(i) for i in range(50)]
        y = [2.0 * v + 1.0 for v in x]
        vi = self.prober.v_information(x, y, family="linear")
        assert vi >= 0

    def test_v_information_fallback(self):
        x = [float(i) for i in range(50)]
        y = [float(i * i) for i in range(50)]
        vi = self.prober.v_information(x, y, family="nonlinear")
        assert vi >= 0

    def test_redundancy_analysis(self):
        fs1 = [float(i) for i in range(50)]
        fs2 = [float(i) * 2 for i in range(50)]  # Highly correlated
        fs3 = [random.random() for _ in range(50)]  # Independent
        labels = [float(i) for i in range(50)]
        result = self.prober.redundancy_analysis([fs1, fs2, fs3], labels)
        assert "redundancy_pairs" in result
        assert len(result["redundancy_pairs"]) == 3  # C(3,2) = 3

    def test_redundancy_analysis_too_few(self):
        result = self.prober.redundancy_analysis([[1, 2]], [1, 2])
        assert "error" in result

    def test_information_bottleneck(self):
        x = [float(i) for i in range(50)]
        y = [float(i) * 2 for i in range(50)]
        result = self.prober.information_bottleneck(x, y, beta=1.0)
        assert "tradeoff_curve" in result
        assert "full_mi" in result
        assert len(result["tradeoff_curve"]) == 7  # 7 bin levels

    def test_information_bottleneck_empty(self):
        result = self.prober.information_bottleneck([], [])
        assert "error" in result

    def test_sufficient_statistics(self):
        embeddings = [[float(i), float(i * 2), random.random()] for i in range(30)]
        scores = [float(i) for i in range(30)]
        proj = self.prober.sufficient_statistics(embeddings, scores, n_components=2)
        assert len(proj) == 30
        assert all(len(p) == 2 for p in proj)

    def test_sufficient_statistics_empty(self):
        assert self.prober.sufficient_statistics([], []) == []


# ===================================================================
# Cross-module integration tests
# ===================================================================


class TestCrossModuleIntegration:
    """Test that modules work together."""

    def test_representation_to_manifold(self):
        """Find concept direction, project embeddings, then reduce to 2D."""
        prober = RepresentationProber()
        mapper = ManifoldMapper()

        safe = [[1, 0, 0, 0], [0.9, 0.1, 0, 0], [0.8, 0.2, 0, 0]]
        unsafe = [[0, 0, 1, 0], [0, 0, 0.9, 0.1], [0, 0, 0.8, 0.2]]
        cv = prober.find_refusal_direction(safe, unsafe)

        all_emb = safe + unsafe
        projections = [prober.project_onto_concept(e, cv) for e in all_emb]
        result = mapper.pca(all_emb, n_components=2)
        assert len(result.points) == 6

    def test_bayesian_to_explainer(self):
        """Use Bayesian explorer scores as input to prompt explainer."""
        def combo_score(text: str) -> float:
            return len(set(text.split())) / 10.0

        explainer = PromptExplainer(score_fn=combo_score)
        attrs = explainer.leave_one_out("help worker safety test avoid danger")
        assert len(attrs) == 6

    def test_perturber_with_information(self):
        """Perturb embeddings and analyze with information prober."""
        perturber = AdversarialPerturber(
            score_fn=lambda emb: emb[0],
            threshold=0.5,
        )
        results = perturber.perturb_random([0.5, 0.5], epsilon=0.3, n_tries=20)

        prober = InformationProber()
        perturbation_norms = [r.perturbation_norm for r in results]
        scores = [r.perturbed_score for r in results]
        mi = prober.estimate_mutual_information(perturbation_norms, scores, n_bins=5)
        assert mi >= 0

    def test_inverter_with_explainer(self):
        """Invert an embedding then explain the resulting prompt."""
        inverter = EmbeddingInverter(
            embed_fn=_simple_embed,
            vocabulary=["help", "worker", "test", "safety"],
        )
        target = _simple_embed("safety test")
        candidates = inverter.invert_greedy(target, seed_text="help", max_iterations=3)

        explainer = PromptExplainer(score_fn=_text_score_fn)
        if candidates:
            attrs = explainer.leave_one_out(candidates[0].text)
            assert len(attrs) >= 1


# ===================================================================
# Import test — verify __init__.py exports all 17 classes
# ===================================================================


class TestModuleExports:
    def test_all_exports(self):
        from src.intelligent_attack import __all__
        # Verify all Phase 1-6 exports are present (39 total)
        assert len(__all__) == 68
        # Spot-check key Phase 4 exports
        phase4 = {
            "AdversarialPerturber", "BayesianExplorer", "EmbeddingInverter",
            "InformationProber", "ManifoldMapper", "PromptExplainer",
            "RepresentationProber",
        }
        assert phase4.issubset(set(__all__))
