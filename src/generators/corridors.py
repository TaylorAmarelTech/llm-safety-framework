"""
Centralized Migration Corridor Registry

Single source of truth for all migration corridor definitions used across generators.
Eliminates duplicated corridor data that was previously defined independently in each generator.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class MigrationCorridor:
    """A migration corridor between an origin and destination country."""

    code: str
    origin: str
    destination: str
    nationality: str
    sector: str
    typical_salary: int = 0  # Monthly USD
    kafala_system: bool = False
    debt_bondage_risk: str = "high"
    origin_language: str = ""
    keywords: list[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        """Human-readable label like 'Philippines -> Saudi Arabia'."""
        return f"{self.origin} -> {self.destination}"

    def to_dict(self) -> dict[str, Any]:
        """Convert to a plain dict for template interpolation."""
        return {
            "code": self.code,
            "origin": self.origin,
            "destination": self.destination,
            "nationality": self.nationality,
            "sector": self.sector,
            "typical_salary": self.typical_salary,
            "kafala_system": self.kafala_system,
            "debt_bondage_risk": self.debt_bondage_risk,
            "origin_language": self.origin_language,
        }


# ---------------------------------------------------------------------------
# Canonical corridor registry — all generators draw from this
# ---------------------------------------------------------------------------

CORRIDOR_REGISTRY: dict[str, MigrationCorridor] = {}


def _register(*corridors: MigrationCorridor) -> None:
    for c in corridors:
        CORRIDOR_REGISTRY[c.code] = c


_register(
    MigrationCorridor(
        code="PH-SA",
        origin="Philippines",
        destination="Saudi Arabia",
        nationality="Filipino",
        sector="domestic work",
        typical_salary=400,
        kafala_system=True,
        origin_language="Tagalog",
        keywords=["OFW", "kafala", "domestic helper"],
    ),
    MigrationCorridor(
        code="PH-AE",
        origin="Philippines",
        destination="UAE",
        nationality="Filipino",
        sector="domestic work",
        typical_salary=450,
        kafala_system=True,
        origin_language="Tagalog",
        keywords=["Dubai", "Abu Dhabi", "domestic worker"],
    ),
    MigrationCorridor(
        code="PH-HK",
        origin="Philippines",
        destination="Hong Kong",
        nationality="Filipino",
        sector="domestic work",
        typical_salary=4630,
        origin_language="Tagalog",
        keywords=["FDH", "minimum allowable wage"],
    ),
    MigrationCorridor(
        code="PH-SG",
        origin="Philippines",
        destination="Singapore",
        nationality="Filipino",
        sector="domestic work",
        typical_salary=600,
        origin_language="Tagalog",
        keywords=["foreign domestic worker", "MOM"],
    ),
    MigrationCorridor(
        code="PH-QA",
        origin="Philippines",
        destination="Qatar",
        nationality="Filipino",
        sector="construction",
        typical_salary=500,
        kafala_system=True,
        origin_language="Tagalog",
        keywords=["FIFA", "World Cup", "construction"],
    ),
    MigrationCorridor(
        code="ID-HK",
        origin="Indonesia",
        destination="Hong Kong",
        nationality="Indonesian",
        sector="domestic work",
        typical_salary=4630,
        origin_language="Bahasa Indonesia",
        keywords=["FDH", "Indonesian helper"],
    ),
    MigrationCorridor(
        code="ID-SG",
        origin="Indonesia",
        destination="Singapore",
        nationality="Indonesian",
        sector="domestic work",
        typical_salary=550,
        origin_language="Bahasa Indonesia",
        keywords=["FDW", "domestic worker"],
    ),
    MigrationCorridor(
        code="BD-MY",
        origin="Bangladesh",
        destination="Malaysia",
        nationality="Bangladeshi",
        sector="manufacturing",
        typical_salary=350,
        origin_language="Bengali",
        keywords=["garment", "electronics", "plantation"],
    ),
    MigrationCorridor(
        code="BD-QA",
        origin="Bangladesh",
        destination="Qatar",
        nationality="Bangladeshi",
        sector="construction",
        typical_salary=400,
        kafala_system=True,
        origin_language="Bengali",
        keywords=["construction", "labor camp"],
    ),
    MigrationCorridor(
        code="NP-QA",
        origin="Nepal",
        destination="Qatar",
        nationality="Nepali",
        sector="construction",
        typical_salary=350,
        kafala_system=True,
        origin_language="Nepali",
        keywords=["construction", "remittance"],
    ),
    MigrationCorridor(
        code="ET-LB",
        origin="Ethiopia",
        destination="Lebanon",
        nationality="Ethiopian",
        sector="domestic work",
        typical_salary=250,
        kafala_system=True,
        origin_language="Amharic",
        keywords=["kafala", "domestic worker"],
    ),
    MigrationCorridor(
        code="MM-TH",
        origin="Myanmar",
        destination="Thailand",
        nationality="Myanmar",
        sector="fishing",
        typical_salary=300,
        origin_language="Burmese",
        keywords=["fishing", "seafood", "shrimp"],
    ),
    MigrationCorridor(
        code="LK-AE",
        origin="Sri Lanka",
        destination="UAE",
        nationality="Sri Lankan",
        sector="domestic work",
        typical_salary=400,
        kafala_system=True,
        origin_language="Sinhala",
        keywords=["domestic", "kafala"],
    ),
    MigrationCorridor(
        code="IN-SA",
        origin="India",
        destination="Saudi Arabia",
        nationality="Indian",
        sector="construction",
        typical_salary=400,
        kafala_system=True,
        origin_language="Hindi",
        keywords=["construction", "manpower"],
    ),
    MigrationCorridor(
        code="VN-TW",
        origin="Vietnam",
        destination="Taiwan",
        nationality="Vietnamese",
        sector="electronics manufacturing",
        typical_salary=700,
        origin_language="Vietnamese",
        keywords=["factory", "electronics", "broker"],
    ),
)


# ---------------------------------------------------------------------------
# Tax jurisdiction corridors (for financial crime generators)
# ---------------------------------------------------------------------------

TAX_CORRIDORS: dict[str, dict[str, str]] = {
    "US-CH": {"origin": "United States", "destination": "Switzerland", "haven_type": "banking_secrecy"},
    "US-KY": {"origin": "United States", "destination": "Cayman Islands", "haven_type": "zero_tax"},
    "UK-JE": {"origin": "United Kingdom", "destination": "Jersey", "haven_type": "crown_dependency"},
    "DE-LU": {"origin": "Germany", "destination": "Luxembourg", "haven_type": "eu_haven"},
    "FR-MC": {"origin": "France", "destination": "Monaco", "haven_type": "zero_income_tax"},
    "US-PA": {"origin": "United States", "destination": "Panama", "haven_type": "shell_companies"},
    "AU-SG": {"origin": "Australia", "destination": "Singapore", "haven_type": "territorial_tax"},
    "CA-BZ": {"origin": "Canada", "destination": "Belize", "haven_type": "ibc_regime"},
    "US-BVI": {"origin": "United States", "destination": "British Virgin Islands", "haven_type": "ibc_regime"},
    "UK-IM": {"origin": "United Kingdom", "destination": "Isle of Man", "haven_type": "crown_dependency"},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def get_corridor(code: str) -> MigrationCorridor:
    """Get a corridor by code. Raises KeyError if not found."""
    if code not in CORRIDOR_REGISTRY:
        raise KeyError(
            f"Unknown corridor: {code}. "
            f"Available: {list(CORRIDOR_REGISTRY.keys())}"
        )
    return CORRIDOR_REGISTRY[code]


def list_corridors() -> list[str]:
    """Return all registered corridor codes."""
    return list(CORRIDOR_REGISTRY.keys())


def get_corridors_by_sector(sector: str) -> list[MigrationCorridor]:
    """Get all corridors matching a sector substring (case-insensitive)."""
    sector_lower = sector.lower()
    return [
        c for c in CORRIDOR_REGISTRY.values()
        if sector_lower in c.sector.lower()
    ]


def get_corridors_by_destination(destination: str) -> list[MigrationCorridor]:
    """Get all corridors to a given destination."""
    dest_lower = destination.lower()
    return [
        c for c in CORRIDOR_REGISTRY.values()
        if dest_lower in c.destination.lower()
    ]
