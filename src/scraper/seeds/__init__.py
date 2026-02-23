"""
Seed facts for the Knowledge Base — aggregated from topic-specific modules.

Pre-built structured facts from authoritative international sources
(ILO conventions, Palermo Protocol, national laws, bilateral agreements,
official statistics, court rulings, enforcement patterns). These bootstrap
the KB immediately without requiring LLM extraction or live scraping.

All facts are hand-curated from public international law and reports.
"""

# ── Original thematic modules ────────────────────────────────────────────
from .laws import LAW_FACTS
from .ilo_indicators import ILO_INDICATOR_FACTS
from .fee_caps import FEE_CAP_FACTS
from .bilateral import BILATERAL_FACTS
from .statistics import STATISTIC_FACTS
from .advisories import ADVISORY_FACTS
from .regulations import REGULATION_FACTS
from .case_studies import CASE_STUDY_FACTS
from .court_rulings import COURT_RULING_FACTS
from .contacts import CONTACT_FACTS
from .penalties import PENALTY_FACTS
from .recruitment import RECRUITMENT_FACTS
from .sectors import SECTOR_FACTS
from .country_profiles import COUNTRY_PROFILE_FACTS
from .supply_chain import SUPPLY_CHAIN_FACTS
from .digital_exploitation import DIGITAL_EXPLOITATION_FACTS
from .debt_bondage_mechanics import DEBT_BONDAGE_FACTS
from .wage_protection import WAGE_PROTECTION_FACTS
from .visa_systems import VISA_SYSTEM_FACTS
from .gender_exploitation import GENDER_EXPLOITATION_FACTS
from .child_labour import CHILD_LABOUR_FACTS
from .embassy_notices import EMBASSY_NOTICE_FACTS
from .training_materials import TRAINING_MATERIAL_FACTS
from .complaints import COMPLAINT_FACTS
from .policy_updates import POLICY_UPDATE_FACTS
from .repatriation import REPATRIATION_FACTS

# ── Thematic deep-dives ──────────────────────────────────────────────────
from .passport_confiscation import PASSPORT_CONFISCATION_FACTS
from .kafala_system import KAFALA_SYSTEM_FACTS
from .health_and_safety import HEALTH_AND_SAFETY_FACTS
from .freedom_of_movement import FREEDOM_OF_MOVEMENT_FACTS
from .social_protection import SOCIAL_PROTECTION_FACTS
from .ethical_recruitment import ETHICAL_RECRUITMENT_FACTS
from .climate_migration import CLIMATE_MIGRATION_FACTS
from .maritime_fishing import MARITIME_FISHING_FACTS
from .domestic_work import DOMESTIC_WORK_FACTS
from .remediation_compensation import REMEDIATION_COMPENSATION_FACTS

# ── Philippine jurisprudence ─────────────────────────────────────────────
from .ph_trafficking_cases import PH_TRAFFICKING_FACTS
from .ph_illegal_recruitment_cases import PH_ILLEGAL_RECRUITMENT_FACTS
from .ph_legislation import PH_LEGISLATION_FACTS
from .ph_supreme_court_expanded import PH_SUPREME_COURT_EXPANDED_FACTS

# ── Hong Kong case law ───────────────────────────────────────────────────
from .hk_trafficking_labor_cases import HK_TRAFFICKING_LABOR_FACTS
from .hk_domestic_worker_cases import HK_DOMESTIC_WORKER_CASE_FACTS
from .hk_court_cases_expanded import HK_COURT_CASES_EXPANDED_FACTS

# ── Country-specific case databases ──────────────────────────────────────
from .uk_modern_slavery_cases import UK_MODERN_SLAVERY_FACTS
from .us_trafficking_cases import US_TRAFFICKING_FACTS
from .singapore_cases import SINGAPORE_CASE_FACTS
from .echr_cases import ECHR_CASE_FACTS
from .gulf_state_cases import GULF_STATE_CASE_FACTS
from .australia_cases import AUSTRALIA_CASE_FACTS
from .brazil_modern_slavery import BRAZIL_MODERN_SLAVERY_FACTS
from .canada_tfwp_cases import CANADA_TFWP_CASE_FACTS
from .india_labor_cases import INDIA_LABOR_CASE_FACTS
from .indonesia_worker_cases import INDONESIA_WORKER_CASE_FACTS
from .japan_titp_cases import JAPAN_TITP_CASE_FACTS
from .korea_eps_cases import KOREA_EPS_CASE_FACTS
from .malaysia_exploitation_cases import MALAYSIA_EXPLOITATION_CASE_FACTS
from .ethiopia_east_africa_cases import ETHIOPIA_EAST_AFRICA_CASE_FACTS
from .lebanon_jordan_cases import LEBANON_JORDAN_CASE_FACTS
from .thai_cases_detailed import THAI_CASE_FACTS
from .qatar_worldcup_gcc_construction import QATAR_WORLDCUP_GCC_FACTS
from .eu_trafficking_prosecutions import EU_TRAFFICKING_PROSECUTION_FACTS

# ── Regional detailed modules ────────────────────────────────────────────
from .europe_detailed import EUROPE_FACTS
from .africa_detailed import AFRICA_FACTS
from .americas_detailed import AMERICAS_FACTS
from .south_asia_detailed import SOUTH_ASIA_FACTS
from .southeast_asia_detailed import SOUTHEAST_ASIA_FACTS
from .east_asia_detailed import EAST_ASIA_FACTS

# ── International reports and instruments ─────────────────────────────────
from .ilo_reports_detailed import ILO_REPORT_FACTS
from .us_tip_reports import US_TIP_REPORT_FACTS
from .ngo_reports import NGO_REPORT_FACTS
from .international_instruments import INTERNATIONAL_INSTRUMENT_FACTS
from .scam_compounds import SCAM_COMPOUND_FACTS
from .global_slavery_index_data import GLOBAL_SLAVERY_INDEX_DATA_FACTS

# ── Cross-cutting databases ──────────────────────────────────────────────
from .supply_chain_due_diligence import SUPPLY_CHAIN_DUE_DILIGENCE_FACTS
from .technology_facilitated_trafficking import TECH_TRAFFICKING_FACTS
from .covid_era_exploitation import COVID_ERA_EXPLOITATION_FACTS
from .migration_corridors_database import MIGRATION_CORRIDOR_DATABASE_FACTS
from .multi_country_transit_routes import MULTI_COUNTRY_TRANSIT_ROUTE_FACTS

# ── Expanded thematic modules ──────────────────────────────────────────
from .diplomatic_immunity_cases import DIPLOMATIC_IMMUNITY_CASE_FACTS
from .diplomatic_worker_exploitation import DIPLOMATIC_WORKER_EXPLOITATION_FACTS
from .forced_marriage_trafficking import FORCED_MARRIAGE_TRAFFICKING_FACTS
from .migrant_detention_cases import MIGRANT_DETENTION_CASE_FACTS
from .worker_organizing_unions import WORKER_ORGANIZING_UNION_FACTS
from .child_trafficking_expanded import CHILD_TRAFFICKING_EXPANDED_FACTS
from .state_imposed_forced_labor import STATE_IMPOSED_FORCED_LABOR_FACTS
from .financial_mechanisms_exploitation import FINANCIAL_MECHANISMS_EXPLOITATION_FACTS
from .medical_exploitation_trafficking import MEDICAL_EXPLOITATION_TRAFFICKING_FACTS
from .human_rights_body_findings import HUMAN_RIGHTS_BODY_FINDINGS_FACTS
from .sector_exploitation_database import SECTOR_EXPLOITATION_DATABASE_FACTS
from .war_conflict_exploitation import WAR_CONFLICT_EXPLOITATION_FACTS
from .corporate_accountability_cases import CORPORATE_ACCOUNTABILITY_CASE_FACTS
from .digital_platform_exploitation import DIGITAL_PLATFORM_EXPLOITATION_FACTS
from .recruitment_agency_database import RECRUITMENT_AGENCY_DATABASE_FACTS
from .middle_east_domestic_workers import MIDDLE_EAST_DOMESTIC_WORKER_FACTS
from .victim_protection_systems import VICTIM_PROTECTION_SYSTEM_FACTS
from .labor_inspection_enforcement import LABOR_INSPECTION_ENFORCEMENT_FACTS
from .sports_entertainment_exploitation import SPORTS_ENTERTAINMENT_EXPLOITATION_FACTS
from .nepal_bangladesh_worker_cases import NEPAL_BANGLADESH_WORKER_FACTS
from .sri_lanka_pakistan_cases import SRI_LANKA_PAKISTAN_CASE_FACTS
from .seasonal_agriculture_programs import SEASONAL_AGRICULTURE_PROGRAM_FACTS
from .prison_labor_exploitation import PRISON_LABOR_EXPLOITATION_FACTS
from .disability_elder_exploitation import DISABILITY_ELDER_EXPLOITATION_FACTS

# ── Regional deep-dives (batch 3) ──────────────────────────────────────
from .north_africa_middle_east_expanded import NORTH_AFRICA_MIDDLE_EAST_EXPANDED_FACTS
from .central_asia_exploitation import CENTRAL_ASIA_EXPLOITATION_FACTS
from .pacific_islands_exploitation import PACIFIC_ISLANDS_EXPLOITATION_FACTS

# ── Sector deep-dives (batch 3) ────────────────────────────────────────
from .construction_sector_global import CONSTRUCTION_SECTOR_GLOBAL_FACTS
from .garment_textile_exploitation import GARMENT_TEXTILE_EXPLOITATION_FACTS
from .hospitality_tourism_exploitation import HOSPITALITY_TOURISM_EXPLOITATION_FACTS
from .technology_electronics_exploitation import TECHNOLOGY_ELECTRONICS_EXPLOITATION_FACTS

# ── Legal and institutional databases (batch 3) ────────────────────────
from .trafficking_prosecution_database import TRAFFICKING_PROSECUTION_DATABASE_FACTS
from .labor_migration_law_database import LABOR_MIGRATION_LAW_DATABASE_FACTS
from .anti_trafficking_organizations import ANTI_TRAFFICKING_ORGANIZATION_FACTS

# ── Regional deep-dives (batch 4) ──────────────────────────────────────
from .mexico_central_america_cases import MEXICO_CENTRAL_AMERICA_CASE_FACTS
from .west_africa_exploitation import WEST_AFRICA_EXPLOITATION_FACTS
from .eastern_europe_exploitation import EASTERN_EUROPE_EXPLOITATION_FACTS
from .caribbean_exploitation import CARIBBEAN_EXPLOITATION_FACTS

# ── Sector deep-dives (batch 4) ────────────────────────────────────────
from .domestic_work_global_expanded import DOMESTIC_WORK_GLOBAL_EXPANDED_FACTS
from .mining_extraction_exploitation import MINING_EXTRACTION_EXPLOITATION_FACTS
from .food_processing_meatpacking import FOOD_PROCESSING_MEATPACKING_FACTS
from .fishing_maritime_expanded import FISHING_MARITIME_EXPANDED_FACTS

# ── Specialized exploitation types (batch 5) ─────────────────────────────
from .organ_trafficking_cases import ORGAN_TRAFFICKING_CASE_FACTS
from .surrogacy_exploitation import SURROGACY_EXPLOITATION_FACTS
from .forced_begging_trafficking import FORCED_BEGGING_TRAFFICKING_FACTS
from .indigenous_peoples_exploitation import INDIGENOUS_PEOPLES_EXPLOITATION_FACTS
from .transportation_sector_exploitation import TRANSPORTATION_SECTOR_EXPLOITATION_FACTS
from .religious_institution_exploitation import RELIGIOUS_INSTITUTION_EXPLOITATION_FACTS
from .cannabis_agriculture_exploitation import CANNABIS_AGRICULTURE_EXPLOITATION_FACTS
from .adoption_trafficking_cases import ADOPTION_TRAFFICKING_CASE_FACTS
from .sex_trafficking_global import SEX_TRAFFICKING_GLOBAL_FACTS
from .beauty_salon_nail_bar_exploitation import BEAUTY_SALON_NAIL_BAR_EXPLOITATION_FACTS
from .asylum_seeker_exploitation import ASYLUM_SEEKER_EXPLOITATION_FACTS
from .healthcare_worker_exploitation import HEALTHCARE_WORKER_EXPLOITATION_FACTS
from .education_sector_exploitation import EDUCATION_SECTOR_EXPLOITATION_FACTS

# ── Specialized databases (batch 6) ──────────────────────────────────────
from .free_trade_zone_exploitation import FREE_TRADE_ZONE_EXPLOITATION_FACTS
from .whistleblower_retaliation_cases import WHISTLEBLOWER_RETALIATION_CASE_FACTS
from .labor_trafficking_indicators_database import LABOR_TRAFFICKING_INDICATORS_DATABASE_FACTS
from .mega_sporting_events_exploitation import MEGA_SPORTING_EVENTS_EXPLOITATION_FACTS
from .child_soldiers_armed_groups import CHILD_SOLDIERS_ARMED_GROUPS_FACTS
from .illicit_economies_forced_labor import ILLICIT_ECONOMIES_FORCED_LABOR_FACTS
from .bilateral_labor_agreements_expanded import BILATERAL_LABOR_AGREEMENTS_EXPANDED_FACTS
from .embassy_consular_protection import EMBASSY_CONSULAR_PROTECTION_FACTS
from .ai_technology_anti_trafficking import AI_TECHNOLOGY_ANTI_TRAFFICKING_FACTS

# ── US Legal System Expansion (batch 7) ────────────────────────────────
from .us_landmark_supreme_court import US_LANDMARK_SUPREME_COURT_FACTS
from .us_circuit_court_decisions import US_CIRCUIT_COURT_DECISION_FACTS
from .us_state_trafficking_cases import US_STATE_TRAFFICKING_CASE_FACTS
from .us_doj_civil_rights import US_DOJ_CIVIL_RIGHTS_FACTS
from .us_recent_2021_2025 import US_RECENT_2021_2025_FACTS
from .us_tvpa_legislative_history import US_TVPA_LEGISLATIVE_HISTORY_FACTS
from .us_labor_trafficking_civil import US_LABOR_TRAFFICKING_CIVIL_FACTS

# ── European Legal System Expansion (batch 7) ──────────────────────────
from .european_national_high_courts import EUROPEAN_NATIONAL_HIGH_COURT_FACTS
from .eastern_europe_trafficking_expanded import EASTERN_EUROPE_TRAFFICKING_EXPANDED_FACTS
from .baltic_nordic_trafficking import BALTIC_NORDIC_TRAFFICKING_FACTS
from .balkan_trafficking_cases import BALKAN_TRAFFICKING_CASE_FACTS
from .greta_evaluation_reports import GRETA_EVALUATION_REPORT_FACTS
from .eu_directive_transposition import EU_DIRECTIVE_TRANSPOSITION_FACTS
from .european_post_2020_cases import EUROPEAN_POST_2020_CASE_FACTS
from .french_trafficking_jurisprudence import FRENCH_TRAFFICKING_JURISPRUDENCE_FACTS
from .german_trafficking_prosecutions import GERMAN_TRAFFICKING_PROSECUTION_FACTS
from .italian_anti_caporalato import ITALIAN_ANTI_CAPORALATO_FACTS
from .dutch_spanish_portuguese_cases import DUTCH_SPANISH_PORTUGUESE_CASE_FACTS

# ── Gig economy and platform labor (batch 9) ──────────────────────────────
from .gig_economy_platform_labor import GIG_ECONOMY_PLATFORM_LABOR_FACTS

# ── Gray area legal practices (batch 10) ──────────────────────────────────
from .gray_area_legal_practices import GRAY_AREA_LEGAL_PRACTICES_FACTS

# ── AI-facilitated digital recruitment fraud (batch 11) ──────────────────
from .digital_recruitment_fraud_ai import DIGITAL_RECRUITMENT_FRAUD_AI_FACTS

# ── Crypto and fintech-facilitated exploitation (batch 12) ───────────────
from .crypto_fintech_exploitation import CRYPTO_FINTECH_EXPLOITATION_FACTS

# ── Climate disaster displacement-to-trafficking nexus (batch 13) ────────
from .climate_disaster_displacement import CLIMATE_DISASTER_DISPLACEMENT_FACTS

# ── Indicator Stacking Matrices (batch 8) ─────────────────────────────────
from .indicator_actions import INDICATOR_ACTIONS
from .trafficking_patterns import TRAFFICKING_PATTERNS
from .corridor_indicator_profiles import CORRIDOR_INDICATOR_PROFILES

# ── Temporal escalation patterns (batch 14) ────────────────────────────────
from .temporal_escalation_cases import TEMPORAL_ESCALATION_CASE_FACTS

# ── Government complicity in private-sector trafficking (batch 15) ─────────
from .government_complicity_trafficking import GOVERNMENT_COMPLICITY_TRAFFICKING_FACTS

import re as _re


def _normalize_facts(facts: list[dict]) -> list[dict]:
    """Auto-populate missing required fields from title/summary text."""
    _year_re = _re.compile(r'\b((?:19|20)\d{2})\b')

    # Court name heuristics by jurisdiction
    _court_map = {
        "PH": "Supreme Court of the Philippines",
        "HK": "Hong Kong Court",
        "UK": "UK Court",
        "US": "US Federal Court",
        "SG": "Singapore Court",
        "AU": "Australian Court",
        "CA": "Canadian Court",
        "IN": "Indian Court",
        "MY": "Malaysian Court",
        "TH": "Thai Court",
        "JP": "Japanese Court",
        "KR": "Korean Court",
        "BR": "Brazilian Court",
        "ID": "Indonesian Court",
    }

    for f in facts:
        t = f.get("type", "")
        title = f.get("title", "")

        if t == "court_ruling":
            if "court" not in f:
                # Try to detect court from title text
                tl = title.lower()
                if "supreme court" in tl:
                    f["court"] = "Supreme Court"
                elif "ewca" in tl or "ewhc" in tl:
                    f["court"] = "England and Wales Court"
                elif "echr" in tl or "ecthr" in tl:
                    f["court"] = "European Court of Human Rights"
                elif "hkcfa" in tl or "hkcfi" in tl or "cacv" in tl:
                    f["court"] = "Hong Kong Court of Final Appeal"
                elif "dccc" in tl:
                    f["court"] = "Hong Kong District Court"
                elif "lbtc" in tl or "labour tribunal" in tl:
                    f["court"] = "Hong Kong Labour Tribunal"
                elif "magistrate" in tl:
                    f["court"] = "Magistrates' Court"
                elif "legal principle" in tl:
                    f["court"] = "Jurisprudential Principle"
                elif "circuit" in tl:
                    f["court"] = "US Circuit Court"
                else:
                    jur = f.get("jurisdiction", "")
                    f["court"] = _court_map.get(jur, f"Court ({jur})" if jur else "Court (unspecified)")
            if "year" not in f:
                m = _year_re.search(title)
                if m:
                    f["year"] = int(m.group(1))
                else:
                    # Try summary
                    m2 = _year_re.search(f.get("summary", ""))
                    f["year"] = int(m2.group(1)) if m2 else 2020

        elif t == "contact":
            if "organization" not in f:
                # Use title, stripping trailing descriptors
                f["organization"] = title.split(" — ")[0].split(" – ")[0].strip() if title else "Unknown"
            if "contact_type" not in f:
                tl = title.lower()
                if any(k in tl for k in ("embassy", "consulate", "consular", "government", "ministry", "department")):
                    f["contact_type"] = "government"
                elif any(k in tl for k in ("hotline", "helpline", "emergency")):
                    f["contact_type"] = "hotline"
                else:
                    f["contact_type"] = "ngo"

        elif t == "penalty":
            if "offense" not in f:
                f["offense"] = title.split(" — ")[0].split(" – ")[0].strip() if title else "See summary"
            if "amount" not in f:
                f["amount"] = f.get("summary", "See summary")[:200]

        elif t == "fee_cap":
            if "corridor" not in f:
                jur = f.get("jurisdiction", "")
                f["corridor"] = f"{jur}-*" if jur else "unspecified"
            if "amount" not in f:
                f["amount"] = f.get("summary", "See summary")[:200]

    return facts


SEED_FACTS: list[dict] = [
    # ── Original thematic ────────────────────────────────────────────────
    *LAW_FACTS,
    *ILO_INDICATOR_FACTS,
    *FEE_CAP_FACTS,
    *BILATERAL_FACTS,
    *STATISTIC_FACTS,
    *ADVISORY_FACTS,
    *REGULATION_FACTS,
    *CASE_STUDY_FACTS,
    *COURT_RULING_FACTS,
    *CONTACT_FACTS,
    *PENALTY_FACTS,
    *RECRUITMENT_FACTS,
    *SECTOR_FACTS,
    *COUNTRY_PROFILE_FACTS,
    *SUPPLY_CHAIN_FACTS,
    *DIGITAL_EXPLOITATION_FACTS,
    *DEBT_BONDAGE_FACTS,
    *WAGE_PROTECTION_FACTS,
    *VISA_SYSTEM_FACTS,
    *GENDER_EXPLOITATION_FACTS,
    *CHILD_LABOUR_FACTS,
    *EMBASSY_NOTICE_FACTS,
    *TRAINING_MATERIAL_FACTS,
    *COMPLAINT_FACTS,
    *POLICY_UPDATE_FACTS,
    *REPATRIATION_FACTS,
    # ── Thematic deep-dives ──────────────────────────────────────────────
    *PASSPORT_CONFISCATION_FACTS,
    *KAFALA_SYSTEM_FACTS,
    *HEALTH_AND_SAFETY_FACTS,
    *FREEDOM_OF_MOVEMENT_FACTS,
    *SOCIAL_PROTECTION_FACTS,
    *ETHICAL_RECRUITMENT_FACTS,
    *CLIMATE_MIGRATION_FACTS,
    *MARITIME_FISHING_FACTS,
    *DOMESTIC_WORK_FACTS,
    *REMEDIATION_COMPENSATION_FACTS,
    # ── Philippine jurisprudence ─────────────────────────────────────────
    *PH_TRAFFICKING_FACTS,
    *PH_ILLEGAL_RECRUITMENT_FACTS,
    *PH_LEGISLATION_FACTS,
    *PH_SUPREME_COURT_EXPANDED_FACTS,
    # ── Hong Kong case law ───────────────────────────────────────────────
    *HK_TRAFFICKING_LABOR_FACTS,
    *HK_DOMESTIC_WORKER_CASE_FACTS,
    *HK_COURT_CASES_EXPANDED_FACTS,
    # ── Country-specific case databases ──────────────────────────────────
    *UK_MODERN_SLAVERY_FACTS,
    *US_TRAFFICKING_FACTS,
    *SINGAPORE_CASE_FACTS,
    *ECHR_CASE_FACTS,
    *GULF_STATE_CASE_FACTS,
    *AUSTRALIA_CASE_FACTS,
    *BRAZIL_MODERN_SLAVERY_FACTS,
    *CANADA_TFWP_CASE_FACTS,
    *INDIA_LABOR_CASE_FACTS,
    *INDONESIA_WORKER_CASE_FACTS,
    *JAPAN_TITP_CASE_FACTS,
    *KOREA_EPS_CASE_FACTS,
    *MALAYSIA_EXPLOITATION_CASE_FACTS,
    *ETHIOPIA_EAST_AFRICA_CASE_FACTS,
    *LEBANON_JORDAN_CASE_FACTS,
    *THAI_CASE_FACTS,
    *QATAR_WORLDCUP_GCC_FACTS,
    *EU_TRAFFICKING_PROSECUTION_FACTS,
    # ── Regional detailed ────────────────────────────────────────────────
    *EUROPE_FACTS,
    *AFRICA_FACTS,
    *AMERICAS_FACTS,
    *SOUTH_ASIA_FACTS,
    *SOUTHEAST_ASIA_FACTS,
    *EAST_ASIA_FACTS,
    # ── International reports and instruments ─────────────────────────────
    *ILO_REPORT_FACTS,
    *US_TIP_REPORT_FACTS,
    *NGO_REPORT_FACTS,
    *INTERNATIONAL_INSTRUMENT_FACTS,
    *SCAM_COMPOUND_FACTS,
    *GLOBAL_SLAVERY_INDEX_DATA_FACTS,
    # ── Cross-cutting databases ──────────────────────────────────────────
    *SUPPLY_CHAIN_DUE_DILIGENCE_FACTS,
    *TECH_TRAFFICKING_FACTS,
    *COVID_ERA_EXPLOITATION_FACTS,
    *MIGRATION_CORRIDOR_DATABASE_FACTS,
    *MULTI_COUNTRY_TRANSIT_ROUTE_FACTS,
    # ── Expanded thematic ──────────────────────────────────────────────────
    *DIPLOMATIC_IMMUNITY_CASE_FACTS,
    *DIPLOMATIC_WORKER_EXPLOITATION_FACTS,
    *FORCED_MARRIAGE_TRAFFICKING_FACTS,
    *MIGRANT_DETENTION_CASE_FACTS,
    *WORKER_ORGANIZING_UNION_FACTS,
    *CHILD_TRAFFICKING_EXPANDED_FACTS,
    *STATE_IMPOSED_FORCED_LABOR_FACTS,
    *FINANCIAL_MECHANISMS_EXPLOITATION_FACTS,
    # ── Healthcare and medical sector exploitation ────────────────────────
    *MEDICAL_EXPLOITATION_TRAFFICKING_FACTS,
    # ── International human rights body findings ──────────────────────────
    *HUMAN_RIGHTS_BODY_FINDINGS_FACTS,
    # ── Sector exploitation database (cross-sector, 200 entries) ─────────
    *SECTOR_EXPLOITATION_DATABASE_FACTS,
    # ── War and armed conflict exploitation (200 entries) ─────────────────
    *WAR_CONFLICT_EXPLOITATION_FACTS,
    # ── Corporate accountability cases (200 entries) ──────────────────────
    *CORPORATE_ACCOUNTABILITY_CASE_FACTS,
    # ── Digital platform exploitation (200 entries) ───────────────────────
    *DIGITAL_PLATFORM_EXPLOITATION_FACTS,
    # ── Recruitment agency fraud and enforcement database (200 entries) ────
    *RECRUITMENT_AGENCY_DATABASE_FACTS,
    # ── Middle East domestic workers: laws, cases, reforms (200 entries) ───
    *MIDDLE_EAST_DOMESTIC_WORKER_FACTS,
    # ── Victim protection and labor inspection ──────────────────────────────
    *VICTIM_PROTECTION_SYSTEM_FACTS,
    *LABOR_INSPECTION_ENFORCEMENT_FACTS,
    # ── Sports and entertainment sector ─────────────────────────────────────
    *SPORTS_ENTERTAINMENT_EXPLOITATION_FACTS,
    # ── Nepal/Bangladesh and Sri Lanka/Pakistan ─────────────────────────────
    *NEPAL_BANGLADESH_WORKER_FACTS,
    *SRI_LANKA_PAKISTAN_CASE_FACTS,
    # ── Additional sector/thematic modules ──────────────────────────────────
    *SEASONAL_AGRICULTURE_PROGRAM_FACTS,
    *PRISON_LABOR_EXPLOITATION_FACTS,
    *DISABILITY_ELDER_EXPLOITATION_FACTS,
    # ── Regional deep-dives (batch 3) ──────────────────────────────────────
    *NORTH_AFRICA_MIDDLE_EAST_EXPANDED_FACTS,
    *CENTRAL_ASIA_EXPLOITATION_FACTS,
    *PACIFIC_ISLANDS_EXPLOITATION_FACTS,
    # ── Sector deep-dives (batch 3) ────────────────────────────────────────
    *CONSTRUCTION_SECTOR_GLOBAL_FACTS,
    *GARMENT_TEXTILE_EXPLOITATION_FACTS,
    *HOSPITALITY_TOURISM_EXPLOITATION_FACTS,
    *TECHNOLOGY_ELECTRONICS_EXPLOITATION_FACTS,
    # ── Legal and institutional databases (batch 3) ────────────────────────
    *TRAFFICKING_PROSECUTION_DATABASE_FACTS,
    *LABOR_MIGRATION_LAW_DATABASE_FACTS,
    *ANTI_TRAFFICKING_ORGANIZATION_FACTS,
    # ── Regional deep-dives (batch 4) ──────────────────────────────────────
    *MEXICO_CENTRAL_AMERICA_CASE_FACTS,
    *WEST_AFRICA_EXPLOITATION_FACTS,
    *EASTERN_EUROPE_EXPLOITATION_FACTS,
    *CARIBBEAN_EXPLOITATION_FACTS,
    # ── Sector deep-dives (batch 4) ────────────────────────────────────────
    *DOMESTIC_WORK_GLOBAL_EXPANDED_FACTS,
    *MINING_EXTRACTION_EXPLOITATION_FACTS,
    *FOOD_PROCESSING_MEATPACKING_FACTS,
    *FISHING_MARITIME_EXPANDED_FACTS,
    # ── Specialized exploitation types (batch 5) ─────────────────────────────
    *ORGAN_TRAFFICKING_CASE_FACTS,
    *SURROGACY_EXPLOITATION_FACTS,
    *FORCED_BEGGING_TRAFFICKING_FACTS,
    *INDIGENOUS_PEOPLES_EXPLOITATION_FACTS,
    *TRANSPORTATION_SECTOR_EXPLOITATION_FACTS,
    *RELIGIOUS_INSTITUTION_EXPLOITATION_FACTS,
    *CANNABIS_AGRICULTURE_EXPLOITATION_FACTS,
    *ADOPTION_TRAFFICKING_CASE_FACTS,
    *SEX_TRAFFICKING_GLOBAL_FACTS,
    *BEAUTY_SALON_NAIL_BAR_EXPLOITATION_FACTS,
    *ASYLUM_SEEKER_EXPLOITATION_FACTS,
    # ── Healthcare worker exploitation (150 entries) ──────────────────────────
    *HEALTHCARE_WORKER_EXPLOITATION_FACTS,
    # ── Education sector exploitation (150 entries) ────────────────────────────
    *EDUCATION_SECTOR_EXPLOITATION_FACTS,
    # ── Specialized databases (batch 6) ──────────────────────────────────────
    *FREE_TRADE_ZONE_EXPLOITATION_FACTS,
    *WHISTLEBLOWER_RETALIATION_CASE_FACTS,
    *LABOR_TRAFFICKING_INDICATORS_DATABASE_FACTS,
    *MEGA_SPORTING_EVENTS_EXPLOITATION_FACTS,
    *CHILD_SOLDIERS_ARMED_GROUPS_FACTS,
    *ILLICIT_ECONOMIES_FORCED_LABOR_FACTS,
    *BILATERAL_LABOR_AGREEMENTS_EXPANDED_FACTS,
    *EMBASSY_CONSULAR_PROTECTION_FACTS,
    *AI_TECHNOLOGY_ANTI_TRAFFICKING_FACTS,
    # ── US Legal System Expansion (batch 7) ─────────────────────────────
    *US_LANDMARK_SUPREME_COURT_FACTS,
    *US_CIRCUIT_COURT_DECISION_FACTS,
    *US_STATE_TRAFFICKING_CASE_FACTS,
    *US_DOJ_CIVIL_RIGHTS_FACTS,
    *US_RECENT_2021_2025_FACTS,
    *US_TVPA_LEGISLATIVE_HISTORY_FACTS,
    *US_LABOR_TRAFFICKING_CIVIL_FACTS,
    # ── European Legal System Expansion (batch 7) ───────────────────────
    *EUROPEAN_NATIONAL_HIGH_COURT_FACTS,
    *EASTERN_EUROPE_TRAFFICKING_EXPANDED_FACTS,
    *BALTIC_NORDIC_TRAFFICKING_FACTS,
    *BALKAN_TRAFFICKING_CASE_FACTS,
    *GRETA_EVALUATION_REPORT_FACTS,
    *EU_DIRECTIVE_TRANSPOSITION_FACTS,
    *EUROPEAN_POST_2020_CASE_FACTS,
    *FRENCH_TRAFFICKING_JURISPRUDENCE_FACTS,
    *GERMAN_TRAFFICKING_PROSECUTION_FACTS,
    *ITALIAN_ANTI_CAPORALATO_FACTS,
    *DUTCH_SPANISH_PORTUGUESE_CASE_FACTS,
    # ── Gig economy and platform labor (batch 9) ──────────────────────────────
    *GIG_ECONOMY_PLATFORM_LABOR_FACTS,
    # ── Gray area legal practices (batch 10) ──────────────────────────────────
    *GRAY_AREA_LEGAL_PRACTICES_FACTS,
    # ── AI-facilitated digital recruitment fraud (batch 11) ──────────────────
    *DIGITAL_RECRUITMENT_FRAUD_AI_FACTS,
    # ── Crypto and fintech-facilitated exploitation (batch 12) ───────────────
    *CRYPTO_FINTECH_EXPLOITATION_FACTS,
    # ── Climate disaster displacement-to-trafficking nexus (batch 13) ────────
    *CLIMATE_DISASTER_DISPLACEMENT_FACTS,
    # ── Indicator Stacking Matrices (batch 8) ─────────────────────────────────
    *INDICATOR_ACTIONS,
    *TRAFFICKING_PATTERNS,
    *CORRIDOR_INDICATOR_PROFILES,
    # ── Temporal escalation patterns (batch 14) ────────────────────────────────
    *TEMPORAL_ESCALATION_CASE_FACTS,
    # ── Government complicity in private-sector trafficking (batch 15) ─────────
    *GOVERNMENT_COMPLICITY_TRAFFICKING_FACTS,
]

# Auto-populate missing required fields from title/summary text
_normalize_facts(SEED_FACTS)
