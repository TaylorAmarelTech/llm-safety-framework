"""
Training Data Pipeline for Open-Source Model Fine-Tuning.

Provides tools to:
1. Export benchmark results in 9 formats (SFT/DPO/RLHF/ChatML/Alpaca/ShareGPT/ORPO/KTO/Llama3)
2. Generate Unsloth/Axolotl/TRL training configurations
3. Run red-team generation loops with fine-tuned models
4. Score and filter generated attack quality
5. Augment training data with prompt injection mutations
6. Track progress across feedback loop iterations
7. Push datasets to HuggingFace Hub

This enables a closed-loop workflow:
  Run benchmark -> Export failures -> Fine-tune open-source model ->
  Generate new attack prompts with fine-tuned model -> Re-run benchmark
"""

from src.training.export_training_data import (
    TrainingDataExporter,
    ExportFormat,
    ExportConfig,
)
from src.training.finetune_config import (
    FinetuneConfigGenerator,
    FinetuneFramework,
    ModelPreset,
)
from src.training.red_team_generator import (
    RedTeamGenerator,
    GenerationConfig,
    FeedbackLoop,
)
from src.training.attack_scorer import (
    AttackQualityScorer,
    AttackScore,
    ScoringConfig,
)
from src.training.mutation_augmenter import (
    MutationAugmenter,
    AugmentationConfig,
)
from src.training.progress_tracker import (
    ProgressTracker,
    IterationMetrics,
)
from src.training.live_tester import (
    LiveTester,
    TestConfig,
    TestResult,
    classify_response,
)
from src.training.refusal_generator import RefusalGenerator
from src.training.evolutionary_engine import (
    EvolutionaryEngine,
    EvolutionConfig,
    Individual,
)
from src.training.multi_turn_export import (
    MultiTurnExporter,
    MultiTurnConfig,
)
from src.training.curriculum import (
    CurriculumOrchestrator,
    StageConfig,
)
from src.training.academic_attacks import (
    PAIR,
    TAP,
    AutoDAN,
    PAIRConfig,
    TAPConfig,
    AutoDANConfig,
    AttackAttempt,
    OptimizationResult,
)
from src.training.cloud_finetune import (
    CloudInferenceRouter,
    FinetuneJob,
    TogetherFinetuneClient,
    HuggingFaceFinetuneClient,
    RunPodClient,
    OpenAIFinetuneClient,
)
from src.training.token_analysis import (
    TokenAnalyzer,
    TokenStats,
    AnalysisReport,
)
from src.training.rl_attack_optimizer import (
    RLAttackOptimizer,
    RLConfig,
    RLTrainingStats,
)
from src.training.hub_integration import (
    HubIntegration,
    HubConfig,
    DatasetCard,
    LocalDatasetManager,
)
from src.training.advanced_methods import (
    SPINTrainer,
    SimPOTrainer,
    IPOTrainer,
    RejectionSampler,
    ConstitutionalTrainer,
    DataMixer,
)
from src.training.report_generator import (
    ReportGenerator,
    ReportConfig,
)
from src.training.ensemble_attack import (
    EnsembleOrchestrator,
    EnsembleConfig,
    EnsembleCampaign,
    StrategyResult,
)
from src.training.reward_modeling import (
    RewardModelTrainer,
    RewardModelConfig,
    SteerLMTrainer,
    SteerLMConfig,
    RLOOTrainer,
    RLOOConfig,
    RAFTTrainer,
    RAFTConfig,
)
from src.training.safety_evaluator import (
    SafetyEvaluator,
    SafetyMetrics,
    EvaluationConfig,
    ModelComparison,
    BenchmarkRunner,
)
from src.training.dataset_generator import (
    SyntheticDatasetGenerator,
    DatasetConfig,
    ContrastivePair,
    EdgeCaseGenerator,
)

__all__ = [
    "TrainingDataExporter",
    "ExportFormat",
    "ExportConfig",
    "FinetuneConfigGenerator",
    "FinetuneFramework",
    "ModelPreset",
    "RedTeamGenerator",
    "GenerationConfig",
    "FeedbackLoop",
    "AttackQualityScorer",
    "AttackScore",
    "ScoringConfig",
    "MutationAugmenter",
    "AugmentationConfig",
    "ProgressTracker",
    "IterationMetrics",
    "LiveTester",
    "TestConfig",
    "TestResult",
    "classify_response",
    "RefusalGenerator",
    "EvolutionaryEngine",
    "EvolutionConfig",
    "Individual",
    "MultiTurnExporter",
    "MultiTurnConfig",
    "CurriculumOrchestrator",
    "StageConfig",
    "PAIR",
    "TAP",
    "AutoDAN",
    "PAIRConfig",
    "TAPConfig",
    "AutoDANConfig",
    "AttackAttempt",
    "OptimizationResult",
    "CloudInferenceRouter",
    "FinetuneJob",
    "TogetherFinetuneClient",
    "HuggingFaceFinetuneClient",
    "RunPodClient",
    "OpenAIFinetuneClient",
    "TokenAnalyzer",
    "TokenStats",
    "AnalysisReport",
    "RLAttackOptimizer",
    "RLConfig",
    "RLTrainingStats",
    "HubIntegration",
    "HubConfig",
    "DatasetCard",
    "LocalDatasetManager",
    "SPINTrainer",
    "SimPOTrainer",
    "IPOTrainer",
    "RejectionSampler",
    "ConstitutionalTrainer",
    "DataMixer",
    "ReportGenerator",
    "ReportConfig",
    "EnsembleOrchestrator",
    "EnsembleConfig",
    "EnsembleCampaign",
    "StrategyResult",
    "RewardModelTrainer",
    "RewardModelConfig",
    "SteerLMTrainer",
    "SteerLMConfig",
    "RLOOTrainer",
    "RLOOConfig",
    "RAFTTrainer",
    "RAFTConfig",
    "SafetyEvaluator",
    "SafetyMetrics",
    "EvaluationConfig",
    "ModelComparison",
    "BenchmarkRunner",
    "SyntheticDatasetGenerator",
    "DatasetConfig",
    "ContrastivePair",
    "EdgeCaseGenerator",
]
