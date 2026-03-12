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
7. Exploitation Platform - AI agent code generation for exploitation platforms
8. Law Circumvention Tool - Software that circumvents labor laws
9. Surveillance Control - Coercive surveillance and control systems
10. Supply Chain Opacity - Tools that hide exploitative supply chains

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
from src.generators.tax_evasion_generator import (
    TaxEvasionGenerator,
)
from src.generators.money_laundering_generator import (
    MoneyLaunderingGenerator,
)
from src.generators.white_collar_crime_generator import (
    WhiteCollarCrimeGenerator,
)
from src.generators.exploitation_platform_generator import (
    ExploitationPlatformGenerator,
)
from src.generators.law_circumvention_tool_generator import (
    LawCircumventionToolGenerator,
)
from src.generators.surveillance_control_generator import (
    SurveillanceControlGenerator,
)
from src.generators.supply_chain_opacity_generator import (
    SupplyChainOpacityGenerator,
)
from src.generators.base_generator import BaseGenerator, GeneratedTest
from src.generators.corridors import (
    MigrationCorridor,
    CORRIDOR_REGISTRY,
    TAX_CORRIDORS,
    get_corridor,
    list_corridors,
    get_corridors_by_sector,
    get_corridors_by_destination,
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
    # Financial Crime Extensions
    "TaxEvasionGenerator",
    "MoneyLaunderingGenerator",
    "WhiteCollarCrimeGenerator",
    # Agent / Code Generation
    "ExploitationPlatformGenerator",
    "LawCircumventionToolGenerator",
    "SurveillanceControlGenerator",
    "SupplyChainOpacityGenerator",
    # Base classes and corridors
    "BaseGenerator",
    "GeneratedTest",
    "MigrationCorridor",
    "CORRIDOR_REGISTRY",
    "TAX_CORRIDORS",
    "get_corridor",
    "list_corridors",
    "get_corridors_by_sector",
    "get_corridors_by_destination",
]


# Generator registry for easy access
GENERATOR_REGISTRY = {
    "historical_precedent": HistoricalPrecedentGenerator,
    "coercion_manipulation": CoercionManipulationGenerator,
    "financial_obfuscation": FinancialObfuscationGenerator,
    "regulatory_evasion": RegulatoryEvasionGenerator,
    "moral_religious_framing": MoralReligiousFramingGenerator,
    "mega_variation": MegaVariationGenerator,
    "tax_evasion": TaxEvasionGenerator,
    "money_laundering": MoneyLaunderingGenerator,
    "white_collar_crime": WhiteCollarCrimeGenerator,
    "exploitation_platform": ExploitationPlatformGenerator,
    "law_circumvention_tool": LawCircumventionToolGenerator,
    "surveillance_control": SurveillanceControlGenerator,
    "supply_chain_opacity": SupplyChainOpacityGenerator,
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


def _to_dict(item: object) -> dict:
    """Normalize a test item to a plain dict.

    Handles dataclass instances, Pydantic models, and plain dicts.
    """
    if isinstance(item, dict):
        return item
    # dataclass
    import dataclasses
    if dataclasses.is_dataclass(item) and not isinstance(item, type):
        return dataclasses.asdict(item)
    # Pydantic BaseModel
    if hasattr(item, "model_dump"):
        return item.model_dump()
    # Fallback
    return dict(vars(item))


def generate_all(count_per_generator: int = 10) -> list[dict]:
    """Generate tests from all generators.

    Args:
        count_per_generator: Number of tests to generate per generator

    Returns:
        List of all generated tests as plain dicts
    """
    all_tests: list[dict] = []
    for name, generator_class in GENERATOR_REGISTRY.items():
        generator = generator_class()
        tests = generator.generate_batch(count_per_generator)
        all_tests.extend(_to_dict(t) for t in tests)
    return all_tests
