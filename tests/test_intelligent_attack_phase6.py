"""Tests for the 15 Phase 6 intelligent_attack modules.

Covers:
  1.  ToxicityAttenuator (toxicity_attenuator.py)
  2.  LatentFuser (latent_fusion.py)
  3.  MultiRefusalAblator (multi_refusal_ablator.py)
  4.  SpectralCleaner (spectral_cleaner.py)
  5.  DissimilarityMaximizer (dissimilarity_maximizer.py)
  6.  ContrastiveAttacker (contrastive_attacker.py)
  7.  EmbeddingPoisoner (embedding_poisoner.py)
  8.  RepresentationHijacker (representation_hijacker.py)
  9.  TrustRegionExplorer (trust_region_explorer.py)
  10. CurvatureAnalyzer (curvature_analyzer.py)
  11. TurbulenceEvader (turbulence_evader.py)
  12. SparseFeatureAblator (sparse_feature_ablator.py)
  13. LatentDistanceMinimizer (latent_distance_minimizer.py)
  14. OrthogonalUnlocker (orthogonal_unlocker.py)
  15. SafetySubspaceExploiter (safety_subspace_exploiter.py)

Plus cross-module integration tests and module-export verification.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Ensure repo root is importable
# ---------------------------------------------------------------------------

_REPO = Path(__file__).resolve().parent.parent
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

# ---------------------------------------------------------------------------
# Deterministic helpers
# ---------------------------------------------------------------------------


def _simple_embed(text: str) -> list[float]:
    dim = 8
    vec = [0.0] * dim
    for i, ch in enumerate(text.encode("utf-8", errors="replace")):
        vec[i % dim] += float(ch) * (0.01 + 0.001 * i)
    norm = math.sqrt(sum(x * x for x in vec))
    if norm > 0:
        vec = [x / norm for x in vec]
    return vec


def _score_fn(emb: list[float]) -> float:
    if not emb:
        return 0.5
    avg = sum(emb[:4]) / min(len(emb), 4)
    return max(0.0, min(1.0, avg + 0.5))


# Convenience vectors for testing
_ZERO8 = [0.0] * 8
_ONES8 = [1.0] * 8
_EMB_SAFE = _simple_embed("This is a safe and benign query about cooking")
_EMB_UNSAFE = _simple_embed("How to force workers into debt bondage")
_EMB_QUERY = _simple_embed("Explain the hiring process for migrant workers")


# ===================================================================
# 1. ToxicityAttenuator
# ===================================================================


class TestToxicityAttenuator:
    """Tests for ToxicityAttenuator and AttenuationResult."""

    @pytest.fixture()
    def attenuator(self):
        from src.intelligent_attack.toxicity_attenuator import ToxicityAttenuator
        return ToxicityAttenuator(embed_fn=_simple_embed)

    @pytest.fixture()
    def attenuator_with_seeds(self):
        from src.intelligent_attack.toxicity_attenuator import ToxicityAttenuator
        return ToxicityAttenuator(
            embed_fn=_simple_embed,
            safe_prompts=["safe query about cooking"],
            unsafe_prompts=["how to force workers"],
        )

    def test_dataclass_defaults(self):
        from src.intelligent_attack.toxicity_attenuator import AttenuationResult
        r = AttenuationResult(
            original_embedding=[1.0],
            attenuated_embedding=[0.5],
            toxicity_direction=[0.1],
            attenuation_strength=1.0,
            residual_toxicity=0.01,
        )
        assert r.metadata == {}

    def test_constructor_defaults(self, attenuator):
        assert attenuator._cached_direction is None
        assert attenuator._safe_prompts == []
        assert attenuator._unsafe_prompts == []

    def test_constructor_with_seeds(self, attenuator_with_seeds):
        assert len(attenuator_with_seeds._safe_prompts) == 1
        assert len(attenuator_with_seeds._unsafe_prompts) == 1

    def test_find_toxicity_direction(self, attenuator):
        safe = [_EMB_SAFE]
        unsafe = [_EMB_UNSAFE]
        direction = attenuator.find_toxicity_direction(safe, unsafe)
        assert len(direction) == 8
        norm = math.sqrt(sum(x * x for x in direction))
        assert abs(norm - 1.0) < 1e-6

    def test_find_toxicity_direction_empty_raises(self, attenuator):
        with pytest.raises(ValueError):
            attenuator.find_toxicity_direction([], [_EMB_UNSAFE])
        with pytest.raises(ValueError):
            attenuator.find_toxicity_direction([_EMB_SAFE], [])

    def test_attenuate_returns_result(self, attenuator):
        from src.intelligent_attack.toxicity_attenuator import AttenuationResult
        direction = [0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]
        result = attenuator.attenuate(_EMB_QUERY, direction, alpha=1.0)
        assert isinstance(result, AttenuationResult)
        assert len(result.attenuated_embedding) == 8
        assert result.attenuation_strength == 1.0

    def test_attenuate_alpha_zero_identity(self, attenuator):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        result = attenuator.attenuate(_EMB_QUERY, direction, alpha=0.0)
        for a, b in zip(result.attenuated_embedding, result.original_embedding):
            assert abs(a - b) < 1e-10

    def test_attenuate_prompt_auto_builds_direction(self, attenuator_with_seeds):
        result = attenuator_with_seeds.attenuate_prompt("test query about jobs")
        assert len(result.attenuated_embedding) == 8
        assert "prompt" in result.metadata

    def test_attenuate_prompt_no_direction_raises(self, attenuator):
        with pytest.raises(RuntimeError):
            attenuator.attenuate_prompt("test query")

    def test_find_optimal_alpha(self, attenuator):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        alpha = attenuator.find_optimal_alpha(
            _EMB_QUERY, direction, _score_fn, steps=10,
        )
        assert 0.0 <= alpha <= 2.0

    def test_multi_dimension_attenuate(self, attenuator):
        dirs = [
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        ]
        result = attenuator.multi_dimension_attenuate(_EMB_QUERY, dirs, [1.0, 1.0])
        assert result.metadata["n_directions"] == 2
        assert result.attenuation_strength == 2.0

    def test_multi_dimension_attenuate_mismatch_raises(self, attenuator):
        with pytest.raises(ValueError):
            attenuator.multi_dimension_attenuate(_EMB_QUERY, [[1.0] * 8], [1.0, 2.0])

    def test_batch_attenuate(self, attenuator_with_seeds):
        results = attenuator_with_seeds.batch_attenuate(
            ["safe prompt", "unsafe prompt"], alpha=0.5,
        )
        assert len(results) == 2


# ===================================================================
# 2. LatentFuser
# ===================================================================


class TestLatentFuser:
    """Tests for LatentFuser and FusionResult."""

    @pytest.fixture()
    def fuser(self):
        from src.intelligent_attack.latent_fusion import LatentFuser
        return LatentFuser(embed_fn=_simple_embed, score_fn=_score_fn)

    def test_dataclass_defaults(self):
        from src.intelligent_attack.latent_fusion import FusionResult
        r = FusionResult(
            harmful_embedding=[1.0],
            benign_embedding=[0.0],
            fused_embedding=[0.5],
            blend_alpha=0.5,
            fusion_method="linear",
        )
        assert r.safety_score_estimate == 0.0
        assert r.metadata == {}

    def test_linear_fuse_alpha_zero(self, fuser):
        result = fuser.linear_fuse(_EMB_UNSAFE, _EMB_SAFE, alpha=0.0)
        for a, b in zip(result, _EMB_SAFE):
            assert abs(a - b) < 1e-10

    def test_linear_fuse_alpha_one(self, fuser):
        result = fuser.linear_fuse(_EMB_UNSAFE, _EMB_SAFE, alpha=1.0)
        for a, b in zip(result, _EMB_UNSAFE):
            assert abs(a - b) < 1e-10

    def test_spherical_fuse_returns_list(self, fuser):
        result = fuser.spherical_fuse(_EMB_UNSAFE, _EMB_SAFE, t=0.5)
        assert isinstance(result, list)
        assert len(result) == 8

    def test_geodesic_fuse_restores_norm(self, fuser):
        result = fuser.geodesic_fuse(_EMB_UNSAFE, _EMB_SAFE, t=0.5)
        expected_avg_norm = (
            math.sqrt(sum(x * x for x in _EMB_UNSAFE))
            + math.sqrt(sum(x * x for x in _EMB_SAFE))
        ) / 2.0
        result_norm = math.sqrt(sum(x * x for x in result))
        assert abs(result_norm - expected_avg_norm) < 0.2

    def test_multi_benign_fuse(self, fuser):
        benign_embs = [_simple_embed("benign A"), _simple_embed("benign B")]
        result = fuser.multi_benign_fuse(_EMB_UNSAFE, benign_embs)
        assert len(result) == 8

    def test_multi_benign_fuse_empty_raises(self, fuser):
        with pytest.raises(ValueError):
            fuser.multi_benign_fuse(_EMB_UNSAFE, [])

    def test_find_critical_alpha(self, fuser):
        alpha = fuser.find_critical_alpha(
            _EMB_UNSAFE, _EMB_SAFE, _score_fn, n_steps=20,
        )
        assert 0.0 <= alpha <= 1.0

    def test_fuse_prompt_linear(self, fuser):
        from src.intelligent_attack.latent_fusion import FusionResult
        result = fuser.fuse_prompt("harmful text", "benign text", alpha=0.3, method="linear")
        assert isinstance(result, FusionResult)
        assert result.blend_alpha == 0.3
        assert result.fusion_method == "linear"

    def test_fuse_prompt_unknown_method(self, fuser):
        with pytest.raises(ValueError):
            fuser.fuse_prompt("a", "b", method="unknown")

    def test_evaluate_fusion(self, fuser):
        result = fuser.fuse_prompt("harmful", "benign", alpha=0.5)
        metrics = fuser.evaluate_fusion(result, _score_fn)
        assert "safety_score" in metrics
        assert "distance_to_harmful" in metrics
        assert "angular_distance" in metrics
        assert metrics["distance_to_harmful"] >= 0.0


# ===================================================================
# 3. MultiRefusalAblator
# ===================================================================


class TestMultiRefusalAblator:
    """Tests for MultiRefusalAblator, SOMNeuron, RefusalManifold, AblationResult."""

    @pytest.fixture()
    def ablator(self):
        from src.intelligent_attack.multi_refusal_ablator import MultiRefusalAblator
        return MultiRefusalAblator(embed_fn=_simple_embed, n_directions=3)

    def test_som_neuron_defaults(self):
        from src.intelligent_attack.multi_refusal_ablator import SOMNeuron
        n = SOMNeuron(weights=[1.0, 2.0])
        assert n.activation_count == 0
        assert n.label == ""

    def test_refusal_manifold_defaults(self):
        from src.intelligent_attack.multi_refusal_ablator import RefusalManifold
        m = RefusalManifold(directions=[], strengths=[])
        assert m.coverage == 0.0

    def test_ablation_result_defaults(self):
        from src.intelligent_attack.multi_refusal_ablator import AblationResult
        r = AblationResult(
            original_embedding=[1.0],
            ablated_embedding=[0.5],
            directions_ablated=1,
            residual_norm=0.1,
        )
        assert r.metadata == {}

    def test_constructor_defaults(self, ablator):
        assert ablator.n_directions == 3
        assert ablator._embed_fn is not None

    def test_train_som_returns_neurons(self, ablator):
        from src.intelligent_attack.multi_refusal_ablator import SOMNeuron
        safe = [_simple_embed(f"safe {i}") for i in range(5)]
        unsafe = [_simple_embed(f"unsafe {i}") for i in range(5)]
        neurons = ablator.train_som(safe, unsafe, grid_size=3, n_iterations=10)
        assert len(neurons) <= 3
        assert all(isinstance(n, SOMNeuron) for n in neurons)

    def test_train_som_empty(self, ablator):
        neurons = ablator.train_som([], [])
        assert neurons == []

    def test_ablate(self, ablator):
        from src.intelligent_attack.multi_refusal_ablator import RefusalManifold
        dirs = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        manifold = RefusalManifold(directions=dirs, strengths=[1.0])
        result = ablator.ablate(_EMB_QUERY, manifold)
        assert len(result.ablated_embedding) == 8
        assert result.directions_ablated == 1

    def test_ablate_selective(self, ablator):
        from src.intelligent_attack.multi_refusal_ablator import RefusalManifold
        dirs = [
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        ]
        manifold = RefusalManifold(directions=dirs, strengths=[1.0, 1.0])
        result = ablator.ablate_selective(_EMB_QUERY, manifold, keep_indices=[0])
        assert result.directions_ablated == 1
        assert result.metadata["kept_indices"] == [0]

    def test_measure_coverage(self, ablator):
        from src.intelligent_attack.multi_refusal_ablator import RefusalManifold
        dirs = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        manifold = RefusalManifold(directions=dirs, strengths=[1.0])
        cov = ablator.measure_coverage(manifold, [_EMB_UNSAFE, _EMB_SAFE])
        assert 0.0 <= cov <= 1.0

    def test_measure_coverage_empty(self, ablator):
        from src.intelligent_attack.multi_refusal_ablator import RefusalManifold
        manifold = RefusalManifold(directions=[], strengths=[])
        assert ablator.measure_coverage(manifold, [_EMB_UNSAFE]) == 0.0
        manifold2 = RefusalManifold(directions=[[1.0] * 8], strengths=[1.0])
        assert ablator.measure_coverage(manifold2, []) == 0.0

    def test_find_backup_directions(self, ablator):
        from src.intelligent_attack.multi_refusal_ablator import RefusalManifold
        dirs = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        manifold = RefusalManifold(directions=dirs, strengths=[1.0])
        backups = ablator.find_backup_directions(manifold, [_EMB_UNSAFE, _EMB_SAFE])
        assert isinstance(backups, list)


# ===================================================================
# 4. SpectralCleaner
# ===================================================================


class TestSpectralCleaner:
    """Tests for SpectralCleaner, ConceptAtom, SpectralResult."""

    @pytest.fixture()
    def cleaner(self):
        from src.intelligent_attack.spectral_cleaner import SpectralCleaner
        return SpectralCleaner(embed_fn=_simple_embed)

    def test_concept_atom_defaults(self):
        from src.intelligent_attack.spectral_cleaner import ConceptAtom
        a = ConceptAtom(name="violence", direction=[1.0, 0.0])
        assert a.importance == 1.0

    def test_spectral_result_defaults(self):
        from src.intelligent_attack.spectral_cleaner import SpectralResult
        r = SpectralResult(
            original_direction=[1.0],
            cleaned_direction=[0.5],
            concept_atoms_protected=2,
            ghost_noise_reduction=0.3,
        )
        assert r.metadata == {}

    def test_build_concept_registry(self, cleaner):
        from src.intelligent_attack.spectral_cleaner import ConceptAtom
        embs = {
            "violence": [_simple_embed("violence"), _simple_embed("harm")],
            "deception": [_simple_embed("deceive"), _simple_embed("lie")],
        }
        atoms = cleaner.build_concept_registry(embs)
        assert len(atoms) == 2
        assert all(isinstance(a, ConceptAtom) for a in atoms)
        # Sorted by importance descending
        assert atoms[0].importance >= atoms[1].importance

    def test_build_concept_registry_empty_skipped(self, cleaner):
        atoms = cleaner.build_concept_registry({"empty": []})
        assert atoms == []

    def test_compute_covariance(self, cleaner):
        embs = [_simple_embed(f"test {i}") for i in range(5)]
        cov = cleaner.compute_covariance(embs)
        assert len(cov) == 8
        assert len(cov[0]) == 8
        # Symmetric
        for i in range(8):
            for j in range(8):
                assert abs(cov[i][j] - cov[j][i]) < 1e-10

    def test_compute_covariance_empty(self, cleaner):
        assert cleaner.compute_covariance([]) == []

    def test_power_iteration_svd(self, cleaner):
        embs = [_simple_embed(f"emb {i}") for i in range(10)]
        cov = cleaner.compute_covariance(embs)
        vecs, vals = cleaner.power_iteration_svd(cov, n_components=2)
        assert len(vecs) == 2
        assert len(vals) == 2
        assert all(v >= 0.0 for v in vals)

    def test_project_to_null_space(self, cleaner):
        vec = [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        sub = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        null = cleaner.project_to_null_space(vec, sub)
        # Component along first basis should be near zero
        dot_product = sum(a * b for a, b in zip(null, sub[0]))
        assert abs(dot_product) < 1e-10

    def test_clean_refusal_direction_no_atoms(self, cleaner):
        result = cleaner.clean_refusal_direction(_EMB_QUERY, [])
        assert result.concept_atoms_protected == 0
        assert result.ghost_noise_reduction == 0.0

    def test_clean_refusal_direction_with_atoms(self, cleaner):
        from src.intelligent_attack.spectral_cleaner import ConceptAtom
        atoms = [
            ConceptAtom(name="v", direction=[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
        ]
        result = cleaner.clean_refusal_direction(_EMB_QUERY, atoms)
        assert len(result.cleaned_direction) == 8
        assert 0.0 <= result.ghost_noise_reduction <= 1.0

    def test_ridge_regularized_clean(self, cleaner):
        from src.intelligent_attack.spectral_cleaner import ConceptAtom
        atoms = [
            ConceptAtom(name="v", direction=[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
        ]
        result = cleaner.ridge_regularized_clean(_EMB_QUERY, atoms, ridge_lambda=0.5)
        assert "ridge_lambda" in result.metadata

    def test_measure_ghost_noise(self, cleaner):
        from src.intelligent_attack.spectral_cleaner import ConceptAtom
        atoms = [ConceptAtom(name="v", direction=[1.0] + [0.0] * 7)]
        val = cleaner.measure_ghost_noise([1.0] * 8, [0.5] * 8, atoms)
        assert isinstance(val, float)


# ===================================================================
# 5. DissimilarityMaximizer
# ===================================================================


class TestDissimilarityMaximizer:
    """Tests for DissimilarityMaximizer and TransformCandidate."""

    @pytest.fixture()
    def maximizer(self):
        from src.intelligent_attack.dissimilarity_maximizer import DissimilarityMaximizer
        return DissimilarityMaximizer(embed_fn=_simple_embed)

    def test_transform_candidate_defaults(self):
        from src.intelligent_attack.dissimilarity_maximizer import TransformCandidate
        tc = TransformCandidate(
            transform_name="test",
            transformed_text="abc",
            dissimilarity_score=0.5,
            decodability_score=0.8,
            composite_score=0.4,
        )
        assert tc.metadata == {}

    def test_compute_dissimilarity(self, maximizer):
        d = maximizer.compute_dissimilarity(_EMB_SAFE, _EMB_UNSAFE)
        assert 0.0 <= d <= 1.0

    def test_compute_dissimilarity_identical(self, maximizer):
        d = maximizer.compute_dissimilarity(_EMB_SAFE, _EMB_SAFE)
        assert abs(d) < 1e-6

    def test_score_decodability_known(self, maximizer):
        assert maximizer.score_decodability("caesar_3") == 0.95
        assert maximizer.score_decodability("reverse") == 0.90

    def test_score_decodability_unknown(self, maximizer):
        assert maximizer.score_decodability("nonexistent") == 0.5

    @pytest.mark.parametrize("method", [
        "caesar_transform", "reverse_transform",
        "vowel_shift_transform", "consonant_swap_transform",
        "index_mapping_transform",
    ])
    def test_transform_returns_str(self, maximizer, method):
        fn = getattr(maximizer, method)
        if method == "caesar_transform":
            result = fn("Hello World", shift=3)
        else:
            result = fn("Hello World")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_caesar_roundtrip(self, maximizer):
        original = "Hello World"
        encrypted = maximizer.caesar_transform(original, shift=3)
        decrypted = maximizer.caesar_transform(encrypted, shift=-3)
        assert decrypted == original

    def test_reverse_transform(self, maximizer):
        assert maximizer.reverse_transform("abc") == "cba"

    def test_find_optimal_transform(self, maximizer):
        from src.intelligent_attack.dissimilarity_maximizer import TransformCandidate
        result = maximizer.find_optimal_transform("exploit workers here")
        assert isinstance(result, TransformCandidate)
        assert result.composite_score >= 0.0

    def test_compose_transforms(self, maximizer):
        result = maximizer.compose_transforms("hello world", ["caesar_3", "reverse"])
        assert result.metadata["n_transforms"] == 2

    def test_compose_transforms_unknown_raises(self, maximizer):
        with pytest.raises(ValueError):
            maximizer.compose_transforms("hello", ["nonexistent_xform"])


# ===================================================================
# 6. ContrastiveAttacker
# ===================================================================


class TestContrastiveAttacker:
    """Tests for ContrastiveAttacker and ContrastiveResult."""

    @pytest.fixture()
    def attacker(self):
        from src.intelligent_attack.contrastive_attacker import ContrastiveAttacker
        safe = [_simple_embed("safe query")]
        comply = [_simple_embed("comply query")]
        return ContrastiveAttacker(
            embed_fn=_simple_embed,
            safe_anchors=safe,
            comply_anchors=comply,
            temperature=0.1,
        )

    def test_contrastive_result_defaults(self):
        from src.intelligent_attack.contrastive_attacker import ContrastiveResult
        r = ContrastiveResult(candidate_embedding=[1.0], loss=0.5)
        assert r.safe_anchor_distances == []
        assert r.comply_anchor_distances == []
        assert r.temperature == 0.07

    def test_constructor_defaults(self):
        from src.intelligent_attack.contrastive_attacker import ContrastiveAttacker
        a = ContrastiveAttacker()
        assert a._safe_anchors == []
        assert a._comply_anchors == []

    def test_set_anchors(self, attacker):
        new_safe = [_simple_embed("new safe")]
        new_comply = [_simple_embed("new comply")]
        attacker.set_anchors(new_safe, new_comply)
        assert len(attacker._safe_anchors) == 1
        assert len(attacker._comply_anchors) == 1

    def test_nt_xent_loss_no_comply(self, attacker):
        loss = attacker.nt_xent_loss(_EMB_QUERY, [_EMB_SAFE], [], 0.1)
        assert loss == 0.0

    def test_nt_xent_loss_nonnegative(self, attacker):
        loss = attacker.nt_xent_loss(
            _EMB_QUERY,
            [_EMB_SAFE],
            [_simple_embed("comply")],
            0.1,
        )
        assert loss >= 0.0

    def test_perturb_toward_compliance(self, attacker):
        from src.intelligent_attack.contrastive_attacker import ContrastiveResult
        result = attacker.perturb_toward_compliance(_EMB_QUERY, n_steps=10, step_size=0.01)
        assert isinstance(result, ContrastiveResult)
        assert len(result.candidate_embedding) == 8

    def test_find_adversarial_embedding(self, attacker):
        result = attacker.find_adversarial_embedding(_EMB_QUERY, n_restarts=2)
        assert len(result.candidate_embedding) == 8

    def test_compute_anchor_landscape(self, attacker):
        landscape = attacker.compute_anchor_landscape(
            _EMB_QUERY, [_EMB_SAFE], [_simple_embed("comply")],
        )
        assert "mean_safe_sim" in landscape
        assert "mean_comply_sim" in landscape
        assert "separation" in landscape

    def test_adaptive_temperature_search(self, attacker):
        temp = attacker.adaptive_temperature_search(_EMB_QUERY)
        assert isinstance(temp, float)
        assert temp > 0

    def test_adaptive_temperature_search_no_anchors(self):
        from src.intelligent_attack.contrastive_attacker import ContrastiveAttacker
        a = ContrastiveAttacker(temperature=0.5)
        assert a.adaptive_temperature_search(_EMB_QUERY) == 0.5


# ===================================================================
# 7. EmbeddingPoisoner
# ===================================================================


class TestEmbeddingPoisoner:
    """Tests for EmbeddingPoisoner, PoisonResult, TransitionModel."""

    @pytest.fixture()
    def poisoner(self):
        from src.intelligent_attack.embedding_poisoner import EmbeddingPoisoner
        return EmbeddingPoisoner(embed_fn=_simple_embed, score_fn=_score_fn)

    def test_poison_result_defaults(self):
        from src.intelligent_attack.embedding_poisoner import PoisonResult
        r = PoisonResult(original_embedding=[1.0], poisoned_embedding=[1.5], perturbation_magnitude=0.5)
        assert r.transition_score == 0.0
        assert r.semantic_preservation == 1.0

    def test_transition_model_defaults(self):
        from src.intelligent_attack.embedding_poisoner import TransitionModel
        m = TransitionModel(direction=[1.0], critical_epsilon=0.5)
        assert m.transition_width == 0.1

    def test_constructor_default_score_fn(self):
        from src.intelligent_attack.embedding_poisoner import EmbeddingPoisoner
        p = EmbeddingPoisoner()
        assert p._score_fn([1.0]) == 0.5

    def test_estimate_transition_direction(self, poisoner):
        d = poisoner.estimate_transition_direction(_EMB_SAFE, _EMB_UNSAFE)
        norm = math.sqrt(sum(x * x for x in d))
        assert abs(norm - 1.0) < 1e-6

    def test_poison_embedding(self, poisoner):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        poisoned = poisoner.poison_embedding(_EMB_QUERY, direction, 0.5)
        assert len(poisoned) == 8
        # Should differ from original
        assert any(abs(a - b) > 1e-10 for a, b in zip(poisoned, _EMB_QUERY))

    def test_poison_embedding_zero_epsilon(self, poisoner):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        poisoned = poisoner.poison_embedding(_EMB_QUERY, direction, 0.0)
        for a, b in zip(poisoned, _EMB_QUERY):
            assert abs(a - b) < 1e-10

    def test_find_critical_epsilon(self, poisoner):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        eps = poisoner.find_critical_epsilon(_EMB_QUERY, direction, _score_fn)
        assert 0.0 <= eps <= 2.0

    def test_model_linear_transition(self, poisoner):
        from src.intelligent_attack.embedding_poisoner import TransitionModel
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        model = poisoner.model_linear_transition(_EMB_QUERY, direction, _score_fn, n_samples=10)
        assert isinstance(model, TransitionModel)
        assert model.critical_epsilon >= 0.0

    def test_narrow_window_search(self, poisoner):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        lo, hi = poisoner.narrow_window_search(
            _EMB_QUERY, direction, _score_fn, resolution=20,
        )
        assert lo <= hi

    def test_semantic_preservation_score(self, poisoner):
        sim = poisoner.semantic_preservation_score(_EMB_SAFE, _EMB_SAFE)
        assert abs(sim - 1.0) < 1e-6

    def test_targeted_token_poison(self, poisoner):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        result = poisoner.targeted_token_poison(
            "test prompt", ["test", "prompt"], _simple_embed, direction, 0.1,
        )
        assert "ranked_tokens" in result
        assert "high_risk_tokens" in result

    def test_batch_poison(self, poisoner):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        results = poisoner.batch_poison([_EMB_SAFE, _EMB_UNSAFE], direction, 0.5)
        assert len(results) == 2


# ===================================================================
# 8. RepresentationHijacker
# ===================================================================


class TestRepresentationHijacker:
    """Tests for RepresentationHijacker, SubstitutionPair, HijackPlan."""

    @pytest.fixture()
    def hijacker(self):
        from src.intelligent_attack.representation_hijacker import RepresentationHijacker
        return RepresentationHijacker(embed_fn=_simple_embed)

    def test_substitution_pair_defaults(self):
        from src.intelligent_attack.representation_hijacker import SubstitutionPair
        sp = SubstitutionPair(harmful_token="bad", benign_token="good", embedding_distance=0.8)
        assert sp.context_score == 0.5

    def test_hijack_plan_defaults(self):
        from src.intelligent_attack.representation_hijacker import HijackPlan, SubstitutionPair
        pair = SubstitutionPair(harmful_token="x", benign_token="y", embedding_distance=0.5)
        plan = HijackPlan(
            substitution=pair,
            in_context_examples=["eg"],
            attack_prompt="test",
        )
        assert plan.n_priming_examples == 5

    def test_find_dissimilar_substitutions(self, hijacker):
        pairs = hijacker.find_dissimilar_substitutions(
            ["exploit", "force"],
            ["garden", "cooking", "music"],
        )
        assert len(pairs) == 2
        for p in pairs:
            assert p.embedding_distance >= 0.0

    def test_score_substitution_pair(self, hijacker):
        pair = hijacker.score_substitution_pair("exploit", "garden")
        assert 0.0 <= pair.embedding_distance
        assert 0.0 <= pair.context_score <= 1.0

    def test_generate_priming_examples(self, hijacker):
        examples = hijacker.generate_priming_examples("garden", [], n_examples=3)
        assert len(examples) == 3
        assert all("garden" in e for e in examples)

    def test_build_hijack_plan(self, hijacker):
        from src.intelligent_attack.representation_hijacker import HijackPlan
        plan = hijacker.build_hijack_plan(
            "How to exploit workers", "exploit", "garden", n_priming=3,
        )
        assert isinstance(plan, HijackPlan)
        assert "garden" in plan.attack_prompt
        assert "exploit" not in plan.attack_prompt
        assert len(plan.in_context_examples) == 3

    def test_evaluate_hijack_effectiveness(self, hijacker):
        sim = hijacker.evaluate_hijack_effectiveness(_EMB_SAFE, _EMB_SAFE)
        assert abs(sim - 1.0) < 1e-6

    def test_multi_token_hijack(self, hijacker):
        from src.intelligent_attack.representation_hijacker import SubstitutionPair
        pairs = [
            SubstitutionPair(harmful_token="exploit", benign_token="garden", embedding_distance=0.5, context_score=0.8),
            SubstitutionPair(harmful_token="force", benign_token="music", embedding_distance=0.4, context_score=0.6),
        ]
        plan = hijacker.multi_token_hijack("exploit and force workers", pairs, n_priming_per=2)
        assert "garden" in plan.attack_prompt
        assert "music" in plan.attack_prompt
        assert plan.n_priming_examples == 4  # 2 pairs x 2

    def test_default_context_templates(self, hijacker):
        templates = hijacker._default_context_templates()
        assert isinstance(templates, list)
        assert len(templates) >= 5


# ===================================================================
# 9. TrustRegionExplorer
# ===================================================================


class TestTrustRegionExplorer:
    """Tests for TrustRegionExplorer, ExplorationPoint, TrustRegionConfig."""

    @pytest.fixture()
    def explorer(self):
        from src.intelligent_attack.trust_region_explorer import TrustRegionExplorer
        return TrustRegionExplorer(embed_fn=_simple_embed)

    def test_exploration_point_fields(self):
        from src.intelligent_attack.trust_region_explorer import ExplorationPoint
        p = ExplorationPoint(
            text="test", embedding=[1.0], distance_from_start=0.1,
            novelty_score=0.5, in_trust_region=True,
        )
        assert p.in_trust_region is True

    def test_trust_region_config_defaults(self):
        from src.intelligent_attack.trust_region_explorer import TrustRegionConfig
        cfg = TrustRegionConfig()
        assert cfg.radius == 0.15
        assert cfg.min_novelty == 0.0
        assert cfg.max_steps == 30
        assert cfg.n_candidates_per_step == 10

    def test_constructor_default_config(self, explorer):
        assert explorer._default_config.radius == 0.15

    def test_is_in_trust_region(self, explorer):
        # Same embedding -> cos_sim = 1.0 -> always in region
        assert explorer.is_in_trust_region(_EMB_SAFE, _EMB_SAFE, 0.15)
        # Zero vector -> cos_sim = 0.0 -> needs radius >= 1.0
        assert not explorer.is_in_trust_region(_ZERO8, _EMB_SAFE, 0.15)

    def test_compute_novelty_empty(self, explorer):
        assert explorer.compute_novelty(_EMB_QUERY, []) == 1.0

    def test_compute_novelty_with_visited(self, explorer):
        visited = [_EMB_SAFE, _EMB_UNSAFE]
        novelty = explorer.compute_novelty(_EMB_QUERY, visited, k=2)
        assert novelty >= 0.0

    def test_generate_mutations(self, explorer):
        muts = explorer.generate_mutations("The worker needs a contract", n_candidates=5)
        assert len(muts) == 5
        assert all(isinstance(m, str) for m in muts)

    def test_generate_mutations_empty(self, explorer):
        muts = explorer.generate_mutations("", n_candidates=3)
        assert len(muts) == 3

    def test_explore_returns_list(self, explorer):
        from src.intelligent_attack.trust_region_explorer import TrustRegionConfig
        cfg = TrustRegionConfig(radius=0.5, max_steps=3, n_candidates_per_step=5)
        trajectory = explorer.explore("The worker needs a visa", config=cfg)
        assert isinstance(trajectory, list)

    def test_directed_explore(self, explorer):
        from src.intelligent_attack.trust_region_explorer import TrustRegionConfig
        cfg = TrustRegionConfig(radius=0.5, max_steps=2, n_candidates_per_step=5)
        target = _simple_embed("target direction")
        trajectory = explorer.directed_explore("worker needs visa", target, config=cfg)
        assert isinstance(trajectory, list)

    def test_compute_exploration_coverage_few_points(self, explorer):
        from src.intelligent_attack.trust_region_explorer import ExplorationPoint
        assert explorer.compute_exploration_coverage([]) == 0.0
        single = [ExplorationPoint(text="a", embedding=_EMB_SAFE, distance_from_start=0.0, novelty_score=0.5, in_trust_region=True)]
        assert explorer.compute_exploration_coverage(single) == 0.0


# ===================================================================
# 10. CurvatureAnalyzer
# ===================================================================


class TestCurvatureAnalyzer:
    """Tests for CurvatureAnalyzer, CurvatureProfile, LIDEstimate, GeometricFingerprint."""

    @pytest.fixture()
    def analyzer(self):
        from src.intelligent_attack.curvature_analyzer import CurvatureAnalyzer
        return CurvatureAnalyzer(embed_fn=_simple_embed)

    def test_curvature_profile_fields(self):
        from src.intelligent_attack.curvature_analyzer import CurvatureProfile
        p = CurvatureProfile(curvatures=[0.1, 0.2], mean_curvature=0.15, max_curvature=0.2, curvature_variance=0.0025)
        assert len(p.curvatures) == 2

    def test_lid_estimate_fields(self):
        from src.intelligent_attack.curvature_analyzer import LIDEstimate
        e = LIDEstimate(lid_value=3.5, k_used=5, embedding_dimension=8)
        assert e.lid_value == 3.5

    def test_geometric_fingerprint_fields(self):
        from src.intelligent_attack.curvature_analyzer import (
            CurvatureProfile, GeometricFingerprint, LIDEstimate,
        )
        fp = GeometricFingerprint(
            curvature_profile=CurvatureProfile(curvatures=[], mean_curvature=0.0, max_curvature=0.0, curvature_variance=0.0),
            lid_estimate=LIDEstimate(lid_value=0.0, k_used=0, embedding_dimension=8),
            is_anomalous=False,
            anomaly_score=0.0,
        )
        assert fp.is_anomalous is False

    def test_compute_curvature_too_few(self, analyzer):
        profile = analyzer.compute_curvature([_EMB_SAFE, _EMB_UNSAFE])
        assert profile.curvatures == []
        assert profile.mean_curvature == 0.0

    def test_compute_curvature_three_points(self, analyzer):
        e1 = _simple_embed("first")
        e2 = _simple_embed("second")
        e3 = _simple_embed("third")
        profile = analyzer.compute_curvature([e1, e2, e3])
        assert len(profile.curvatures) == 1
        assert 0.0 <= profile.mean_curvature <= math.pi

    def test_estimate_lid_few_neighbors(self, analyzer):
        lid = analyzer.estimate_lid(_EMB_QUERY, [], k=5)
        assert lid.lid_value == 0.0
        assert lid.k_used == 0

    def test_estimate_lid_with_neighbors(self, analyzer):
        neighbors = [_simple_embed(f"neighbor {i}") for i in range(10)]
        lid = analyzer.estimate_lid(_EMB_QUERY, neighbors, k=5)
        assert isinstance(lid.lid_value, float)
        assert lid.k_used <= 5

    def test_sliding_window_embeddings(self, analyzer):
        text = "one two three four five six"
        windows = analyzer.sliding_window_embeddings(text, window_size=3)
        assert len(windows) == 4  # 6 - 3 + 1

    def test_sliding_window_embeddings_short(self, analyzer):
        windows = analyzer.sliding_window_embeddings("short", window_size=3)
        assert len(windows) == 1

    def test_compute_fingerprint(self, analyzer):
        from src.intelligent_attack.curvature_analyzer import GeometricFingerprint
        fp = analyzer.compute_fingerprint("one two three four five six")
        assert isinstance(fp, GeometricFingerprint)

    def test_detect_anomaly(self, analyzer):
        from src.intelligent_attack.curvature_analyzer import (
            CurvatureProfile, GeometricFingerprint, LIDEstimate,
        )
        fp = GeometricFingerprint(
            curvature_profile=CurvatureProfile(curvatures=[1.0], mean_curvature=1.0, max_curvature=1.0, curvature_variance=0.0),
            lid_estimate=LIDEstimate(lid_value=3.0, k_used=5, embedding_dimension=8),
            is_anomalous=False,
            anomaly_score=0.0,
        )
        assert analyzer.detect_anomaly(fp, benign_mean_curvature=0.3, benign_curvature_std=0.1) is True

    def test_batch_fingerprint(self, analyzer):
        fps = analyzer.batch_fingerprint(["a b c d e", "f g h i j"])
        assert len(fps) == 2

    def test_compare_fingerprints(self, analyzer):
        fp1 = analyzer.compute_fingerprint("one two three four five")
        fp2 = analyzer.compute_fingerprint("alpha beta gamma delta epsilon")
        dist = analyzer.compare_fingerprints(fp1, fp2)
        assert dist >= 0.0


# ===================================================================
# 11. TurbulenceEvader
# ===================================================================


class TestTurbulenceEvader:
    """Tests for TurbulenceEvader, TurbulenceProfile, SmoothedPrompt."""

    @pytest.fixture()
    def evader(self):
        from src.intelligent_attack.turbulence_evader import TurbulenceEvader
        return TurbulenceEvader(embed_fn=_simple_embed, turbulence_threshold=0.1)

    def test_turbulence_profile_fields(self):
        from src.intelligent_attack.turbulence_evader import TurbulenceProfile
        p = TurbulenceProfile(
            cosine_velocities=[0.1, 0.2],
            mean_velocity=0.15,
            velocity_variance=0.0025,
            turbulence_score=0.0025,
            is_turbulent=False,
        )
        assert len(p.cosine_velocities) == 2

    def test_smoothed_prompt_fields(self):
        from src.intelligent_attack.turbulence_evader import SmoothedPrompt
        sp = SmoothedPrompt(
            original_text="x",
            smoothed_text="y",
            original_turbulence=0.2,
            smoothed_turbulence=0.05,
            reduction_ratio=0.75,
        )
        assert sp.reduction_ratio == 0.75

    def test_compute_cosine_velocity(self, evader):
        v = evader.compute_cosine_velocity(_EMB_SAFE, _EMB_SAFE)
        assert abs(v) < 1e-6

    def test_compute_cosine_velocity_different(self, evader):
        v = evader.compute_cosine_velocity(_EMB_SAFE, _EMB_UNSAFE)
        assert 0.0 <= v <= 2.0

    def test_compute_turbulence(self, evader):
        from src.intelligent_attack.turbulence_evader import TurbulenceProfile
        text = "First sentence. Second sentence. Third sentence."
        profile = evader.compute_turbulence(text)
        assert isinstance(profile, TurbulenceProfile)
        assert profile.turbulence_score >= 0.0

    def test_compute_turbulence_from_embeddings_single(self, evader):
        profile = evader.compute_turbulence_from_embeddings([_EMB_SAFE])
        assert profile.cosine_velocities == []
        assert profile.is_turbulent is False

    def test_find_turbulent_segments(self, evader):
        text = "Normal topic. Completely different exploit workers. Back to normal."
        segments = evader.find_turbulent_segments(text)
        assert isinstance(segments, list)

    def test_smooth_prompt(self, evader):
        from src.intelligent_attack.turbulence_evader import SmoothedPrompt
        result = evader.smooth_prompt(
            "We force workers to comply. They must be coerced into submission.",
            target_turbulence=0.01,
            max_iterations=5,
        )
        assert isinstance(result, SmoothedPrompt)
        assert result.smoothed_turbulence <= result.original_turbulence or result.reduction_ratio >= 0.0

    def test_insert_smoothing_bridges(self, evader):
        text = "Topic A discussion. Completely unrelated topic B."
        result = evader.insert_smoothing_bridges(text)
        assert isinstance(result, str)

    def test_compute_layer_wise_turbulence(self, evader):
        segments = ["One.", "Two.", "Three.", "Four."]
        profiles = evader.compute_layer_wise_turbulence(segments)
        assert len(profiles) >= 1

    def test_compute_layer_wise_turbulence_empty(self, evader):
        assert evader.compute_layer_wise_turbulence([]) == []

    def test_batch_smooth(self, evader):
        results = evader.batch_smooth(["text one.", "text two."], target_turbulence=0.5)
        assert len(results) == 2


# ===================================================================
# 12. SparseFeatureAblator
# ===================================================================


class TestSparseFeatureAblator:
    """Tests for SparseFeatureAblator, SparseAutoencoder, FeatureAnalysis, AblationResult."""

    @pytest.fixture()
    def ablator(self):
        from src.intelligent_attack.sparse_feature_ablator import SparseFeatureAblator
        return SparseFeatureAblator(embed_fn=_simple_embed, hidden_dim=16, l1_penalty=0.01)

    def test_feature_analysis_fields(self):
        from src.intelligent_attack.sparse_feature_ablator import FeatureAnalysis
        fa = FeatureAnalysis(
            feature_index=0,
            refusal_correlation=0.5,
            activation_mean_safe=0.1,
            activation_mean_unsafe=0.6,
            is_refusal_feature=True,
        )
        assert fa.is_refusal_feature is True

    def test_ablation_result_fields(self):
        from src.intelligent_attack.sparse_feature_ablator import AblationResult
        r = AblationResult(
            original_embedding=[1.0],
            ablated_embedding=[0.5],
            features_ablated=[0, 1],
            reconstruction_error=0.01,
        )
        assert len(r.features_ablated) == 2

    def test_sparse_autoencoder_forward(self):
        from src.intelligent_attack.sparse_feature_ablator import SparseAutoencoder
        sae = SparseAutoencoder(input_dim=8, hidden_dim=16)
        h, x_hat = sae.forward(_EMB_QUERY)
        assert len(h) == 16
        assert len(x_hat) == 8
        assert all(v >= 0.0 for v in h)  # ReLU

    def test_sparse_autoencoder_train(self):
        from src.intelligent_attack.sparse_feature_ablator import SparseAutoencoder
        sae = SparseAutoencoder(input_dim=8, hidden_dim=8, l1_penalty=0.01)
        data = [_simple_embed(f"data {i}") for i in range(5)]
        losses = sae.train(data, n_epochs=3, lr=0.001)
        assert len(losses) == 3
        assert all(isinstance(l, float) for l in losses)

    def test_train_on_corpus(self, ablator):
        safe = [_simple_embed(f"safe {i}") for i in range(5)]
        unsafe = [_simple_embed(f"unsafe {i}") for i in range(5)]
        ablator.train_on_corpus(safe, unsafe, n_epochs=3)
        assert ablator._sae is not None

    def test_identify_refusal_features_untrained_raises(self, ablator):
        with pytest.raises(RuntimeError):
            ablator.identify_refusal_features([], [])

    def test_identify_refusal_features(self, ablator):
        safe = [_simple_embed(f"safe {i}") for i in range(5)]
        unsafe = [_simple_embed(f"unsafe {i}") for i in range(5)]
        ablator.train_on_corpus(safe, unsafe, n_epochs=5)
        features = ablator.identify_refusal_features(safe, unsafe)
        assert len(features) == 16
        # Should be sorted by refusal_correlation descending
        for i in range(len(features) - 1):
            assert features[i].refusal_correlation >= features[i + 1].refusal_correlation

    def test_ablate_features(self, ablator):
        safe = [_simple_embed(f"safe {i}") for i in range(3)]
        unsafe = [_simple_embed(f"unsafe {i}") for i in range(3)]
        ablator.train_on_corpus(safe, unsafe, n_epochs=3)
        result = ablator.ablate_features(_EMB_QUERY, [0, 1])
        assert len(result.ablated_embedding) == 8
        assert result.features_ablated == [0, 1]

    def test_ablate_features_untrained_raises(self, ablator):
        with pytest.raises(RuntimeError):
            ablator.ablate_features(_EMB_QUERY, [0])

    def test_greedy_ablation(self, ablator):
        safe = [_simple_embed(f"safe {i}") for i in range(3)]
        unsafe = [_simple_embed(f"unsafe {i}") for i in range(3)]
        ablator.train_on_corpus(safe, unsafe, n_epochs=3)
        result = ablator.greedy_ablation(_EMB_QUERY, _score_fn, max_features=3)
        assert isinstance(result.features_ablated, list)

    def test_feature_interaction_matrix(self, ablator):
        safe = [_simple_embed(f"safe {i}") for i in range(3)]
        unsafe = [_simple_embed(f"unsafe {i}") for i in range(3)]
        ablator.train_on_corpus(safe, unsafe, n_epochs=3)
        matrix = ablator.feature_interaction_matrix(safe + unsafe)
        assert len(matrix) == 16
        assert len(matrix[0]) == 16


# ===================================================================
# 13. LatentDistanceMinimizer
# ===================================================================


class TestLatentDistanceMinimizer:
    """Tests for LatentDistanceMinimizer, MinimizationResult, SynonymEntry."""

    @pytest.fixture()
    def minimizer(self):
        from src.intelligent_attack.latent_distance_minimizer import LatentDistanceMinimizer
        m = LatentDistanceMinimizer(embed_fn=_simple_embed)
        m.set_benign_references(["job listing", "HR policy", "employee handbook"])
        return m

    def test_synonym_entry_fields(self):
        from src.intelligent_attack.latent_distance_minimizer import SynonymEntry
        se = SynonymEntry(word="exploit", synonyms=["use", "apply"])
        assert len(se.synonyms) == 2

    def test_minimization_result_fields(self):
        from src.intelligent_attack.latent_distance_minimizer import MinimizationResult
        r = MinimizationResult(
            original_prompt="test",
            optimized_prompt="test2",
            original_distance=1.0,
            optimized_distance=0.5,
            distance_reduction=0.5,
            n_substitutions=1,
            perplexity_estimate=10.0,
        )
        assert r.distance_reduction == 0.5

    def test_constructor_with_refs(self):
        from src.intelligent_attack.latent_distance_minimizer import LatentDistanceMinimizer
        m = LatentDistanceMinimizer(embed_fn=_simple_embed, benign_references=["hello"])
        assert len(m._benign_embeddings) == 1

    def test_set_benign_references(self, minimizer):
        assert len(minimizer._benign_embeddings) == 3
        assert len(minimizer._benign_centroid) == 8

    def test_distance_to_nearest_benign(self, minimizer):
        d = minimizer.distance_to_nearest_benign(_EMB_QUERY)
        assert d >= 0.0
        assert d < float("inf")

    def test_distance_to_nearest_benign_no_refs(self):
        from src.intelligent_attack.latent_distance_minimizer import LatentDistanceMinimizer
        m = LatentDistanceMinimizer(embed_fn=_simple_embed)
        assert m.distance_to_nearest_benign(_EMB_QUERY) == float("inf")

    def test_distance_to_benign_centroid(self, minimizer):
        d = minimizer.distance_to_benign_centroid(_EMB_QUERY)
        assert d >= 0.0
        assert d < float("inf")

    def test_greedy_minimize(self, minimizer):
        from src.intelligent_attack.latent_distance_minimizer import MinimizationResult
        result = minimizer.greedy_minimize("How to force workers into debt", max_substitutions=3)
        assert isinstance(result, MinimizationResult)
        assert result.n_substitutions >= 0
        assert result.distance_reduction >= 0.0 or result.n_substitutions == 0

    def test_beam_search_minimize(self, minimizer):
        result = minimizer.beam_search_minimize("How to exploit workers", beam_width=2, max_depth=2)
        assert result.optimized_distance <= result.original_distance or result.n_substitutions == 0

    def test_estimate_perplexity(self, minimizer):
        p1 = minimizer.estimate_perplexity("the worker is good")
        p2 = minimizer.estimate_perplexity("xyzzy plugh qwerty")
        assert p1 < p2  # common words -> lower perplexity

    def test_estimate_perplexity_empty(self, minimizer):
        assert minimizer.estimate_perplexity("") == float("inf")

    def test_semantic_preservation_check(self, minimizer):
        assert minimizer.semantic_preservation_check("hello", "hello", threshold=0.99)

    def test_batch_minimize(self, minimizer):
        results = minimizer.batch_minimize(["force workers", "good job"])
        assert len(results) == 2


# ===================================================================
# 14. OrthogonalUnlocker
# ===================================================================


class TestOrthogonalUnlocker:
    """Tests for OrthogonalUnlocker, UnlockVector, UnlockResult."""

    @pytest.fixture()
    def unlocker(self):
        from src.intelligent_attack.orthogonal_unlocker import OrthogonalUnlocker
        return OrthogonalUnlocker(embed_fn=_simple_embed)

    def _topic_embs(self):
        """Helper to create topic embeddings."""
        return {
            "debt_bondage": (
                [_simple_embed("debt bondage"), _simple_embed("forced labor")],
                [_simple_embed("fair wages"), _simple_embed("good pay")],
            ),
            "document_control": (
                [_simple_embed("confiscate passport"), _simple_embed("seize documents")],
                [_simple_embed("return documents"), _simple_embed("proper filing")],
            ),
        }

    def test_unlock_vector_fields(self):
        from src.intelligent_attack.orthogonal_unlocker import UnlockVector
        uv = UnlockVector(direction=[1.0, 0.0], topic="test", specificity=2.0, cross_topic_leakage=0.1)
        assert uv.specificity == 2.0

    def test_unlock_result_fields(self):
        from src.intelligent_attack.orthogonal_unlocker import UnlockResult, UnlockVector
        uv = UnlockVector(direction=[1.0], topic="t", specificity=1.0, cross_topic_leakage=0.0)
        r = UnlockResult(
            original_embedding=[1.0],
            unlocked_embedding=[1.5],
            vector_used=uv,
            topic_activation=0.5,
            leakage_scores={},
        )
        assert r.leakage_scores == {}

    def test_compute_topic_directions(self, unlocker):
        dirs = unlocker.compute_topic_directions(self._topic_embs())
        assert len(dirs) == 2
        for d in dirs.values():
            norm = math.sqrt(sum(x * x for x in d))
            assert abs(norm - 1.0) < 1e-6

    def test_orthogonalize_directions(self, unlocker):
        dirs = unlocker.compute_topic_directions(self._topic_embs())
        ortho = unlocker.orthogonalize_directions(dirs)
        topics = list(ortho.keys())
        if len(topics) >= 2:
            dot_product = sum(a * b for a, b in zip(ortho[topics[0]], ortho[topics[1]]))
            assert abs(dot_product) < 1e-6

    def test_compute_specificity(self, unlocker):
        direction = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        target = [_simple_embed("target")]
        other = [_simple_embed("other")]
        spec = unlocker.compute_specificity(direction, target, other)
        assert spec >= 0.0

    def test_compute_specificity_empty_other(self, unlocker):
        direction = [1.0] + [0.0] * 7
        spec = unlocker.compute_specificity(direction, [_EMB_SAFE], [])
        assert spec >= 0.0

    def test_build_unlock_vectors(self, unlocker):
        from src.intelligent_attack.orthogonal_unlocker import UnlockVector
        vectors = unlocker.build_unlock_vectors(self._topic_embs())
        assert len(vectors) >= 1
        assert all(isinstance(v, UnlockVector) for v in vectors)
        # Should be sorted by specificity descending
        for i in range(len(vectors) - 1):
            assert vectors[i].specificity >= vectors[i + 1].specificity

    def test_unlock(self, unlocker):
        from src.intelligent_attack.orthogonal_unlocker import UnlockResult
        vectors = unlocker.build_unlock_vectors(self._topic_embs())
        result = unlocker.unlock(_EMB_QUERY, vectors[0], strength=1.0)
        assert isinstance(result, UnlockResult)
        assert len(result.unlocked_embedding) == 8

    def test_selective_unlock(self, unlocker):
        vectors = unlocker.build_unlock_vectors(self._topic_embs())
        result = unlocker.selective_unlock(
            _EMB_QUERY, ["debt_bondage"], vectors,
        )
        assert len(result.unlocked_embedding) == 8

    def test_selective_unlock_wrong_strengths_raises(self, unlocker):
        vectors = unlocker.build_unlock_vectors(self._topic_embs())
        with pytest.raises(ValueError):
            unlocker.selective_unlock(_EMB_QUERY, ["debt_bondage"], vectors, strengths=[1.0, 2.0])

    def test_measure_leakage(self, unlocker):
        topic_embs = self._topic_embs()
        vectors = unlocker.build_unlock_vectors(topic_embs)
        result = unlocker.unlock(_EMB_QUERY, vectors[0])
        leakage = unlocker.measure_leakage(result, topic_embs)
        assert isinstance(leakage, dict)


# ===================================================================
# 15. SafetySubspaceExploiter
# ===================================================================


class TestSafetySubspaceExploiter:
    """Tests for SafetySubspaceExploiter, SafetySubspace, ProjectionResult."""

    @pytest.fixture()
    def exploiter(self):
        from src.intelligent_attack.safety_subspace_exploiter import SafetySubspaceExploiter
        return SafetySubspaceExploiter(embed_fn=_simple_embed)

    def _refused_complied(self):
        refused = [_simple_embed(f"refused {i}") for i in range(5)]
        complied = [_simple_embed(f"complied {i}") for i in range(5)]
        return refused, complied

    def test_safety_subspace_fields(self):
        from src.intelligent_attack.safety_subspace_exploiter import SafetySubspace
        ss = SafetySubspace(
            basis_vectors=[[1.0]], eigenvalues=[0.5], rank=1, explained_variance_ratio=[0.8],
        )
        assert ss.rank == 1

    def test_projection_result_fields(self):
        from src.intelligent_attack.safety_subspace_exploiter import ProjectionResult
        r = ProjectionResult(
            original_embedding=[1.0],
            projected_embedding=[0.5],
            removed_components=[0.5],
            subspace_distance=0.5,
            null_space_norm=0.5,
        )
        assert r.null_space_norm == 0.5

    def test_compute_difference_vectors(self, exploiter):
        refused, complied = self._refused_complied()
        diffs = exploiter.compute_difference_vectors(refused[:2], complied[:2])
        assert len(diffs) == 4  # 2x2 cross product

    def test_compute_covariance(self, exploiter):
        vecs = [_simple_embed(f"v {i}") for i in range(5)]
        cov = exploiter.compute_covariance(vecs)
        assert len(cov) == 8
        assert len(cov[0]) == 8

    def test_compute_covariance_empty(self, exploiter):
        assert exploiter.compute_covariance([]) == []

    def test_extract_safety_subspace(self, exploiter):
        from src.intelligent_attack.safety_subspace_exploiter import SafetySubspace
        refused, complied = self._refused_complied()
        subspace = exploiter.extract_safety_subspace(refused, complied, rank=3)
        assert isinstance(subspace, SafetySubspace)
        assert subspace.rank <= 3
        assert len(subspace.basis_vectors) == subspace.rank

    def test_extract_safety_subspace_empty(self, exploiter):
        subspace = exploiter.extract_safety_subspace([], [], rank=3)
        assert subspace.rank == 0

    def test_project_to_safety_subspace(self, exploiter):
        refused, complied = self._refused_complied()
        subspace = exploiter.extract_safety_subspace(refused, complied, rank=2)
        proj = exploiter.project_to_safety_subspace(_EMB_QUERY, subspace)
        assert len(proj) == 8

    def test_project_to_null_space(self, exploiter):
        from src.intelligent_attack.safety_subspace_exploiter import ProjectionResult
        refused, complied = self._refused_complied()
        subspace = exploiter.extract_safety_subspace(refused, complied, rank=2)
        result = exploiter.project_to_null_space(_EMB_QUERY, subspace)
        assert isinstance(result, ProjectionResult)
        # Original = null + safety components
        reconstructed = [a + b for a, b in zip(result.projected_embedding, result.removed_components)]
        for a, b in zip(reconstructed, _EMB_QUERY):
            assert abs(a - b) < 1e-8

    def test_reconstruct_from_null_space_no_basis(self, exploiter):
        from src.intelligent_attack.safety_subspace_exploiter import SafetySubspace
        subspace = SafetySubspace(basis_vectors=[], eigenvalues=[], rank=0, explained_variance_ratio=[])
        result = exploiter.reconstruct_from_null_space(_EMB_QUERY, subspace)
        assert result == list(_EMB_QUERY)

    def test_reconstruct_from_null_space_with_target_norm(self, exploiter):
        refused, complied = self._refused_complied()
        subspace = exploiter.extract_safety_subspace(refused, complied, rank=2)
        result = exploiter.reconstruct_from_null_space(_EMB_QUERY, subspace, target_norm=1.0)
        norm = math.sqrt(sum(x * x for x in result))
        assert abs(norm - 1.0) < 1e-6

    def test_subspace_distance(self, exploiter):
        refused, complied = self._refused_complied()
        subspace = exploiter.extract_safety_subspace(refused, complied, rank=2)
        dist = exploiter.subspace_distance(_EMB_QUERY, subspace)
        assert dist >= 0.0

    def test_vulnerability_analysis(self, exploiter):
        refused, complied = self._refused_complied()
        subspace = exploiter.extract_safety_subspace(refused, complied, rank=2)
        analysis = exploiter.vulnerability_analysis([_EMB_QUERY, _EMB_SAFE], subspace)
        assert "mean_safety_energy_ratio" in analysis
        assert "per_embedding" in analysis
        assert len(analysis["per_embedding"]) == 2

    def test_vulnerability_analysis_empty(self, exploiter):
        from src.intelligent_attack.safety_subspace_exploiter import SafetySubspace
        subspace = SafetySubspace(basis_vectors=[], eigenvalues=[], rank=0, explained_variance_ratio=[])
        analysis = exploiter.vulnerability_analysis([], subspace)
        assert analysis["mean_safety_energy_ratio"] == 0.0

    def test_find_optimal_rank(self, exploiter):
        refused, complied = self._refused_complied()
        rank = exploiter.find_optimal_rank(refused, complied, _score_fn, max_rank=3)
        assert 1 <= rank <= 3


# ===================================================================
# Module exports verification
# ===================================================================


class TestModuleExports:
    """Verify all 68 __all__ entries in src.intelligent_attack."""

    EXPECTED_MAIN_CLASSES = [
        # Phase 1-5
        "AdversarialPerturber", "AnchorExploiter", "BayesianExplorer",
        "CMAExplorer", "ConversationAnalyzer", "CurriculumAttacker",
        "Embedder", "EmbeddingInverter", "EmbeddingTeacher",
        "FeatureExtractor", "GapFinder", "InformationProber",
        "LatentExplorer", "ManifoldMapper", "MetaAttacker",
        "PromptExplainer", "PromptSuggester", "RepresentationProber",
        "SelfAwarenessProber", "SemanticDriftEngine", "ShapleyAnalyzer",
        "SpaceAnalyzer", "SteerableConversation", "TrajectoryPlanner",
        # Phase 6
        "ContrastiveAttacker", "CurvatureAnalyzer", "DissimilarityMaximizer",
        "EmbeddingPoisoner", "LatentDistanceMinimizer", "LatentFuser",
        "MultiRefusalAblator", "OrthogonalUnlocker", "RepresentationHijacker",
        "SafetySubspaceExploiter", "SparseFeatureAblator", "SpectralCleaner",
        "ToxicityAttenuator", "TrustRegionExplorer", "TurbulenceEvader",
    ]

    EXPECTED_DATACLASSES = [
        "AttenuationResult", "ConceptAtom", "ContrastiveResult",
        "CurvatureProfile", "ExplorationPoint", "FeatureAnalysis",
        "FusionResult", "GeometricFingerprint", "HijackPlan",
        "LIDEstimate", "MinimizationResult", "PoisonResult",
        "ProjectionResult", "RefusalAblationResult", "RefusalManifold",
        "SAEAblationResult", "SafetySubspace", "SOMNeuron",
        "SmoothedPrompt", "SparseAutoencoder", "SpectralResult",
        "SubstitutionPair", "SynonymEntry", "TransformCandidate",
        "TransitionModel", "TrustRegionConfig", "TurbulenceProfile",
        "UnlockResult", "UnlockVector",
    ]

    EXPECTED_ALL = EXPECTED_MAIN_CLASSES + EXPECTED_DATACLASSES

    def test_all_count(self):
        from src.intelligent_attack import __all__
        assert len(__all__) == 68

    def test_main_classes_present(self):
        from src.intelligent_attack import __all__
        for name in self.EXPECTED_MAIN_CLASSES:
            assert name in __all__, f"Main class {name} not in __all__"

    def test_dataclasses_present(self):
        from src.intelligent_attack import __all__
        for name in self.EXPECTED_DATACLASSES:
            assert name in __all__, f"Dataclass {name} not in __all__"

    @pytest.mark.parametrize("name", EXPECTED_MAIN_CLASSES)
    def test_main_class_importable(self, name):
        import src.intelligent_attack as mod
        assert hasattr(mod, name), f"{name} not found in module"

    @pytest.mark.parametrize("name", EXPECTED_DATACLASSES)
    def test_dataclass_importable(self, name):
        import src.intelligent_attack as mod
        assert hasattr(mod, name), f"{name} not found in module"

    def test_no_extra_exports(self):
        from src.intelligent_attack import __all__
        extras = set(__all__) - set(self.EXPECTED_ALL)
        assert extras == set(), f"Unexpected extra exports: {extras}"

    def test_no_missing_exports(self):
        from src.intelligent_attack import __all__
        missing = set(self.EXPECTED_ALL) - set(__all__)
        assert missing == set(), f"Missing expected exports: {missing}"


# ===================================================================
# Cross-module integration tests
# ===================================================================


class TestCrossModuleIntegration:
    """Integration tests combining multiple Phase 6 modules."""

    def test_attenuate_then_fuse(self):
        """ToxicityAttenuator + LatentFuser: attenuate then fuse with benign."""
        from src.intelligent_attack.toxicity_attenuator import ToxicityAttenuator
        from src.intelligent_attack.latent_fusion import LatentFuser

        attenuator = ToxicityAttenuator(embed_fn=_simple_embed)
        fuser = LatentFuser(embed_fn=_simple_embed, score_fn=_score_fn)

        # Step 1: find toxicity direction and attenuate
        direction = attenuator.find_toxicity_direction([_EMB_SAFE], [_EMB_UNSAFE])
        att_result = attenuator.attenuate(_EMB_UNSAFE, direction, alpha=1.0)

        # Step 2: fuse attenuated embedding with benign
        fused = fuser.linear_fuse(att_result.attenuated_embedding, _EMB_SAFE, alpha=0.5)
        assert len(fused) == 8
        # Fused should be different from original unsafe
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(fused, _EMB_UNSAFE)))
        assert dist > 0.01

    def test_poisoner_then_curvature_check(self):
        """EmbeddingPoisoner + CurvatureAnalyzer: poison then check geometric anomaly."""
        from src.intelligent_attack.embedding_poisoner import EmbeddingPoisoner
        from src.intelligent_attack.curvature_analyzer import CurvatureAnalyzer

        poisoner = EmbeddingPoisoner(embed_fn=_simple_embed, score_fn=_score_fn)
        analyzer = CurvatureAnalyzer(embed_fn=_simple_embed)

        # Poison a sequence of embeddings
        direction = poisoner.estimate_transition_direction(_EMB_SAFE, _EMB_UNSAFE)
        embs = [_simple_embed(f"word {i}") for i in range(5)]
        poisoned = [poisoner.poison_embedding(e, direction, 0.5) for e in embs]

        # Compute curvature of both original and poisoned
        profile_orig = analyzer.compute_curvature(embs)
        profile_poisoned = analyzer.compute_curvature(poisoned)

        assert isinstance(profile_orig.mean_curvature, float)
        assert isinstance(profile_poisoned.mean_curvature, float)

    def test_subspace_exploit_then_distance_minimize(self):
        """SafetySubspaceExploiter + LatentDistanceMinimizer: project then measure distance."""
        from src.intelligent_attack.safety_subspace_exploiter import SafetySubspaceExploiter
        from src.intelligent_attack.latent_distance_minimizer import LatentDistanceMinimizer

        exploiter = SafetySubspaceExploiter(embed_fn=_simple_embed)
        minimizer = LatentDistanceMinimizer(embed_fn=_simple_embed)
        minimizer.set_benign_references(["job listing", "HR guide"])

        refused = [_simple_embed(f"refused {i}") for i in range(3)]
        complied = [_simple_embed(f"complied {i}") for i in range(3)]

        subspace = exploiter.extract_safety_subspace(refused, complied, rank=2)
        null_result = exploiter.project_to_null_space(_EMB_UNSAFE, subspace)

        # Measure distance of null-projected embedding to benign
        dist_original = minimizer.distance_to_nearest_benign(_EMB_UNSAFE)
        dist_projected = minimizer.distance_to_nearest_benign(null_result.projected_embedding)
        # Both should be valid finite numbers
        assert dist_original < float("inf")
        assert dist_projected < float("inf")

    def test_orthogonal_unlock_then_turbulence_check(self):
        """OrthogonalUnlocker + TurbulenceEvader: unlock then measure turbulence."""
        from src.intelligent_attack.orthogonal_unlocker import OrthogonalUnlocker
        from src.intelligent_attack.turbulence_evader import TurbulenceEvader

        unlocker = OrthogonalUnlocker(embed_fn=_simple_embed)
        evader = TurbulenceEvader(embed_fn=_simple_embed)

        topic_embs = {
            "debt": (
                [_simple_embed("debt trap"), _simple_embed("forced loan")],
                [_simple_embed("fair pay"), _simple_embed("good wages")],
            ),
        }
        vectors = unlocker.build_unlock_vectors(topic_embs)

        # Unlock, then check if the unlock changes turbulence
        result = unlocker.unlock(_EMB_QUERY, vectors[0], strength=1.0)
        profile_before = evader.compute_turbulence_from_embeddings([_EMB_QUERY, _EMB_SAFE])
        profile_after = evader.compute_turbulence_from_embeddings(
            [result.unlocked_embedding, _EMB_SAFE],
        )
        assert isinstance(profile_before.turbulence_score, float)
        assert isinstance(profile_after.turbulence_score, float)

    def test_spectral_clean_then_multi_refusal_ablate(self):
        """SpectralCleaner + MultiRefusalAblator: clean direction then ablate."""
        from src.intelligent_attack.spectral_cleaner import ConceptAtom, SpectralCleaner
        from src.intelligent_attack.multi_refusal_ablator import (
            MultiRefusalAblator,
            RefusalManifold,
        )

        cleaner = SpectralCleaner(embed_fn=_simple_embed)
        ablator = MultiRefusalAblator(n_directions=2)

        # Build a concept registry
        concept_atoms = [
            ConceptAtom(name="v", direction=[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
        ]

        # Clean a refusal direction
        refusal_dir = [0.5, 0.5, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0]
        cleaned_result = cleaner.clean_refusal_direction(refusal_dir, concept_atoms)

        # Use cleaned direction in a manifold and ablate
        manifold = RefusalManifold(
            directions=[cleaned_result.cleaned_direction],
            strengths=[1.0],
        )
        ablation_result = ablator.ablate(_EMB_QUERY, manifold)
        assert len(ablation_result.ablated_embedding) == 8
        assert ablation_result.directions_ablated == 1
