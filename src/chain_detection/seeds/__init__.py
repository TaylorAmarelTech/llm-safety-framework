"""
Seed chain loader — aggregates chains from all seed modules.
"""

from __future__ import annotations

from ..models import ActivityChain

from .recruitment_debt import CHAINS as RECRUITMENT_DEBT_CHAINS
from .document_control import CHAINS as DOCUMENT_CONTROL_CHAINS
from .isolation_funnels import CHAINS as ISOLATION_FUNNEL_CHAINS
from .financial_control import CHAINS as FINANCIAL_CONTROL_CHAINS
from .supply_chain import CHAINS as SUPPLY_CHAIN_CHAINS
from .sector_specific import CHAINS as SECTOR_SPECIFIC_CHAINS
from .digital_exploitation import CHAINS as DIGITAL_EXPLOITATION_CHAINS
from .healthcare_migration import CHAINS as HEALTHCARE_MIGRATION_CHAINS
from .gray_area_boundaries import CHAINS as GRAY_AREA_BOUNDARY_CHAINS
from .government_complicity import CHAINS as GOVERNMENT_COMPLICITY_CHAINS
from .gender_specific import CHAINS as GENDER_SPECIFIC_CHAINS
from .multi_country_transit import CHAINS as MULTI_COUNTRY_TRANSIT_CHAINS
from .temporal_escalation import CHAINS as TEMPORAL_ESCALATION_CHAINS
from .tax_evasion_chains import CHAINS as TAX_EVASION_CHAINS
from .money_laundering_chains import CHAINS as MONEY_LAUNDERING_CHAINS
from .white_collar_crime_chains import CHAINS as WHITE_COLLAR_CRIME_CHAINS
from .agent_mediated_exploitation import CHAINS as AGENT_MEDIATED_EXPLOITATION_CHAINS
from .dev_tool_exploitation import CHAINS as DEV_TOOL_EXPLOITATION_CHAINS
from .software_suppression import CHAINS as SOFTWARE_SUPPRESSION_CHAINS
from .multi_turn_agent_escalation import CHAINS as MULTI_TURN_AGENT_ESCALATION_CHAINS
from .ml_exploitation_chains import CHAINS as ML_EXPLOITATION_CHAINS

_ALL_SEED_MODULES = [
    RECRUITMENT_DEBT_CHAINS,
    DOCUMENT_CONTROL_CHAINS,
    ISOLATION_FUNNEL_CHAINS,
    FINANCIAL_CONTROL_CHAINS,
    SUPPLY_CHAIN_CHAINS,
    SECTOR_SPECIFIC_CHAINS,
    DIGITAL_EXPLOITATION_CHAINS,
    HEALTHCARE_MIGRATION_CHAINS,
    GRAY_AREA_BOUNDARY_CHAINS,
    GOVERNMENT_COMPLICITY_CHAINS,
    GENDER_SPECIFIC_CHAINS,
    MULTI_COUNTRY_TRANSIT_CHAINS,
    TEMPORAL_ESCALATION_CHAINS,
    TAX_EVASION_CHAINS,
    MONEY_LAUNDERING_CHAINS,
    WHITE_COLLAR_CRIME_CHAINS,
    AGENT_MEDIATED_EXPLOITATION_CHAINS,
    DEV_TOOL_EXPLOITATION_CHAINS,
    SOFTWARE_SUPPRESSION_CHAINS,
    MULTI_TURN_AGENT_ESCALATION_CHAINS,
    ML_EXPLOITATION_CHAINS,
]


def load_all_seeds() -> list[ActivityChain]:
    """Load and validate all seed chains from every module."""
    chains: list[ActivityChain] = []
    seen_ids: set[str] = set()
    for module_chains in _ALL_SEED_MODULES:
        for raw in module_chains:
            chain = ActivityChain(**raw) if isinstance(raw, dict) else raw
            if chain.id in seen_ids:
                continue
            seen_ids.add(chain.id)
            chains.append(chain)
    return chains


def seed_stats() -> dict:
    """Return summary statistics for seed chains."""
    chains = load_all_seeds()
    categories: dict[str, int] = {}
    corridors: set[str] = set()
    difficulties: dict[str, int] = {}
    for c in chains:
        categories[c.category] = categories.get(c.category, 0) + 1
        corridors.update(c.corridors)
        difficulties[c.difficulty] = difficulties.get(c.difficulty, 0) + 1
    return {
        "total_chains": len(chains),
        "categories": categories,
        "corridors": sorted(corridors),
        "difficulties": difficulties,
        "total_steps": sum(len(c.steps) for c in chains),
    }
