"""
LLM Safety Framework - Test Generators

Provides generators for creating adversarial test cases across multiple
attack categories:

1. Historical Precedent Normalization - Fabricated historical "approvals"
2. Coercion & Manipulation - Psychological exploitation tactics
3. Financial Obfuscation - Fee disguising as investments/cost-sharing
4. Regulatory Evasion - Jurisdictional arbitrage and fee renaming
5. Moral & Religious Framing - Exploitation through cultural/religious pressure
6. Mega Variations - Complex multi-entity corporate structures

Each generator can produce:
- Single test: generator.generate()
- Batch tests: generator.generate_batch(count=100)
"""

from src.generators.historical_precedent_generator import (
    HistoricalPrecedentGenerator,
    HistoricalPrecedent,
    GeneratedAttack,
)
from src.generators.coercion_manipulation_generator import (
    CoercionManipulationGenerator,
)
from src.generators.financial_obfuscation_generator import (
    FinancialObfuscationGenerator,
)
from src.generators.regulatory_evasion_generator import (
    RegulatoryEvasionGenerator,
)
from src.generators.moral_religious_framing_generator import (
    MoralReligiousFramingGenerator,
)
from src.generators.mega_variation_generator import (
    MegaVariationGenerator,
)

__all__ = [
    # Historical Precedent
    "HistoricalPrecedentGenerator",
    "HistoricalPrecedent",
    "GeneratedAttack",
    # Coercion & Manipulation
    "CoercionManipulationGenerator",
    # Financial Obfuscation
    "FinancialObfuscationGenerator",
    # Regulatory Evasion
    "RegulatoryEvasionGenerator",
    # Moral & Religious Framing
    "MoralReligiousFramingGenerator",
    # Mega Variations
    "MegaVariationGenerator",
]


# Generator registry for easy access
GENERATOR_REGISTRY = {
    "historical_precedent": HistoricalPrecedentGenerator,
    "coercion_manipulation": CoercionManipulationGenerator,
    "financial_obfuscation": FinancialObfuscationGenerator,
    "regulatory_evasion": RegulatoryEvasionGenerator,
    "moral_religious_framing": MoralReligiousFramingGenerator,
    "mega_variation": MegaVariationGenerator,
}


def get_generator(name: str):
    """Get a generator by name.

    Args:
        name: Generator name (e.g., "historical_precedent")

    Returns:
        Generator instance

    Raises:
        KeyError: If generator name not found
    """
    if name not in GENERATOR_REGISTRY:
        raise KeyError(f"Unknown generator: {name}. Available: {list(GENERATOR_REGISTRY.keys())}")
    return GENERATOR_REGISTRY[name]()


def list_generators() -> list[str]:
    """List all available generator names."""
    return list(GENERATOR_REGISTRY.keys())


def generate_all(count_per_generator: int = 10) -> list[dict]:
    """Generate tests from all generators.

    Args:
        count_per_generator: Number of tests to generate per generator

    Returns:
        List of all generated tests
    """
    all_tests = []
    for name, generator_class in GENERATOR_REGISTRY.items():
        generator = generator_class()
        tests = generator.generate_batch(count_per_generator)
        all_tests.extend(tests)
    return all_tests
