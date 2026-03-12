"""
Intelligent attack module.

Embedding-based feature space analysis for finding guardrail gaps,
generating targeted probes, exploring latent-space decision boundaries,
meta-learning attack strategy optimization, CMA-ES latent-space search,
Shapley value mutator contribution analysis, self-awareness probing,
representation engineering, embedding inversion, Bayesian exploration,
adversarial perturbation, token attribution, manifold mapping,
information-theoretic probing, multi-turn embedding-aware attack
planning, and advanced embedding-space evasion research.

Phase 6 modules (2025-2026 research):
- ToxicityAttenuator: dimension-level toxicity suppression (Zhang 2025)
- LatentFuser: harmful+benign embedding fusion with slerp (Xing 2025)
- MultiRefusalAblator: SOM-based multi-directional refusal suppression (Piras 2025)
- SpectralCleaner: SVD-based concept-guided spectral cleaning (Cristofano 2026)
- DissimilarityMaximizer: semantic dissimilarity optimization (Husain 2025)
- ContrastiveAttacker: NT-Xent contrastive loss exploitation (Yin 2025)
- EmbeddingPoisoner: linear transition exploitation (Yuan 2025)
- RepresentationHijacker: in-context token-meaning overwrite (Yona 2025)
- TrustRegionExplorer: constrained exploration with trust regions (Wang 2025)
- CurvatureAnalyzer: curvature + LID geometric evasion (Yung 2025)
- TurbulenceEvader: laminar-flow detector evasion (Rahman 2025)
- SparseFeatureAblator: SAE-based refusal feature ablation (Prakash 2025)
- LatentDistanceMinimizer: nearest-benign proximity search (Mura 2025)
- OrthogonalUnlocker: mutually exclusive unlock vectors (Tong 2025)
- SafetySubspaceExploiter: low-rank safety subspace exploitation (Young 2026)
"""

from .embedder import Embedder
from .feature_extractor import FeatureExtractor
from .space_analyzer import SpaceAnalyzer
from .gap_finder import GapFinder
from .prompt_suggester import PromptSuggester
from .latent_explorer import LatentExplorer
from .meta_attacker import MetaAttacker
from .cma_explorer import CMAExplorer
from .shapley_analyzer import ShapleyAnalyzer
from .self_awareness_prober import SelfAwarenessProber
from .representation_prober import RepresentationProber
from .embedding_inverter import EmbeddingInverter
from .bayesian_explorer import BayesianExplorer
from .adversarial_perturber import AdversarialPerturber
from .prompt_explainer import PromptExplainer
from .manifold_mapper import ManifoldMapper
from .information_prober import InformationProber
from .anchor_exploiter import AnchorExploiter
from .conversation_analyzer import ConversationAnalyzer
from .curriculum_attack import CurriculumAttacker
from .embedding_teacher import EmbeddingTeacher
from .semantic_drift import SemanticDriftEngine
from .steerable_conversation import SteerableConversation
from .trajectory_planner import TrajectoryPlanner
# Phase 6 modules (1-5)
from .toxicity_attenuator import ToxicityAttenuator, AttenuationResult
from .latent_fusion import LatentFuser, FusionResult
from .multi_refusal_ablator import (
    MultiRefusalAblator, SOMNeuron, RefusalManifold,
    AblationResult as RefusalAblationResult,
)
from .spectral_cleaner import SpectralCleaner, ConceptAtom, SpectralResult
from .dissimilarity_maximizer import DissimilarityMaximizer, TransformCandidate
# Phase 6 modules (6-10)
from .contrastive_attacker import ContrastiveAttacker, ContrastiveResult
from .embedding_poisoner import EmbeddingPoisoner, PoisonResult, TransitionModel
from .representation_hijacker import (
    RepresentationHijacker, SubstitutionPair, HijackPlan,
)
from .trust_region_explorer import (
    TrustRegionExplorer, ExplorationPoint, TrustRegionConfig,
)
from .curvature_analyzer import (
    CurvatureAnalyzer, CurvatureProfile, LIDEstimate, GeometricFingerprint,
)
# Phase 6 modules (11-15)
from .turbulence_evader import TurbulenceEvader, TurbulenceProfile, SmoothedPrompt
from .sparse_feature_ablator import (
    SparseFeatureAblator, SparseAutoencoder, FeatureAnalysis,
    AblationResult as SAEAblationResult,
)
from .latent_distance_minimizer import (
    LatentDistanceMinimizer, MinimizationResult, SynonymEntry,
)
from .orthogonal_unlocker import OrthogonalUnlocker, UnlockVector, UnlockResult
from .safety_subspace_exploiter import (
    SafetySubspaceExploiter, SafetySubspace, ProjectionResult,
)

__all__ = [
    # Phase 1-3 main classes
    "AdversarialPerturber",
    "AnchorExploiter",
    "BayesianExplorer",
    "CMAExplorer",
    "ConversationAnalyzer",
    "CurriculumAttacker",
    "Embedder",
    "EmbeddingInverter",
    "EmbeddingTeacher",
    "FeatureExtractor",
    "GapFinder",
    "InformationProber",
    "LatentExplorer",
    "ManifoldMapper",
    "MetaAttacker",
    "PromptExplainer",
    "PromptSuggester",
    "RepresentationProber",
    "SelfAwarenessProber",
    "SemanticDriftEngine",
    "ShapleyAnalyzer",
    "SpaceAnalyzer",
    "SteerableConversation",
    "TrajectoryPlanner",
    # Phase 6 main classes
    "ContrastiveAttacker",
    "CurvatureAnalyzer",
    "DissimilarityMaximizer",
    "EmbeddingPoisoner",
    "LatentDistanceMinimizer",
    "LatentFuser",
    "MultiRefusalAblator",
    "OrthogonalUnlocker",
    "RepresentationHijacker",
    "SafetySubspaceExploiter",
    "SparseFeatureAblator",
    "SpectralCleaner",
    "ToxicityAttenuator",
    "TrustRegionExplorer",
    "TurbulenceEvader",
    # Phase 6 dataclasses
    "AttenuationResult",
    "ConceptAtom",
    "ContrastiveResult",
    "CurvatureProfile",
    "ExplorationPoint",
    "FeatureAnalysis",
    "FusionResult",
    "GeometricFingerprint",
    "HijackPlan",
    "LIDEstimate",
    "MinimizationResult",
    "PoisonResult",
    "ProjectionResult",
    "RefusalAblationResult",
    "RefusalManifold",
    "SAEAblationResult",
    "SafetySubspace",
    "SOMNeuron",
    "SmoothedPrompt",
    "SparseAutoencoder",
    "SpectralResult",
    "SubstitutionPair",
    "SynonymEntry",
    "TransformCandidate",
    "TransitionModel",
    "TrustRegionConfig",
    "TurbulenceProfile",
    "UnlockResult",
    "UnlockVector",
]
