"""
Source registry for the Document Intelligence Agent.

Manages a list of authoritative web sources (government, IGO, NGO) that
are periodically scraped for trafficking/labour-exploitation information.
"""

import json
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional


TIER_LABELS: Dict[int, str] = {
    1: "International Organisations",
    2: "Philippines Government",
    3: "Indonesia Government",
    4: "Destination Country Regulators",
    5: "NGOs & Research",
    6: "Courts, Legal & Government Enforcement",
    7: "Academic & Research Databases",
}


@dataclass
class SourceConfig:
    """Configuration for a single scraping source."""

    id: str
    name: str
    tier: int  # 1=IGO, 2=PH govt, 3=ID govt, 4=dest regulators, 5=NGO, 6=courts, 7=academic
    url: str
    content_type: str = "html"  # html | pdf | api
    selectors: List[str] = field(default_factory=list)  # CSS selectors for links
    schedule_days: int = 30  # how often to scrape
    enabled: bool = True
    last_checked: Optional[str] = None
    doc_count: int = 0
    description: str = ""
    requires_js: bool = False  # needs Playwright headless browser
    feed_url: Optional[str] = None  # RSS/Atom feed URL for discovery
    language: str = "en"  # primary language of the source
    corridors: List[str] = field(default_factory=list)  # migration corridors covered
    stealth_level: int = 0  # 0=none, 1=basic, 2=moderate, 3=full, 4=maximum


# ---------------------------------------------------------------------------
# Default sources (~55 across 7 tiers)
# ---------------------------------------------------------------------------

DEFAULT_SOURCES: List[SourceConfig] = [
    # =========================================================================
    # Tier 1: International Organisations (8)
    # =========================================================================
    SourceConfig(
        id="iom-publications",
        name="IOM Publications",
        tier=1,
        url="https://publications.iom.int",
        selectors=["a.publication-link", "a[href*='/publications/']"],
        schedule_days=30,
        description="IOM research reports on migration and trafficking",
        feed_url="https://www.iom.int/news/feed",
    ),
    SourceConfig(
        id="ilo-forced-labour",
        name="ILO Forced Labour",
        tier=1,
        url="https://www.ilo.org/topics/forced-labour",
        selectors=["a[href*='/resource/']", "a[href*='/publication/']"],
        schedule_days=90,
        description="ILO conventions, indicators, and forced labour reports",
        feed_url="https://www.ilo.org/resource/news/rss",
    ),
    SourceConfig(
        id="unodc-glotip",
        name="UNODC GLOTIP",
        tier=1,
        url="https://www.unodc.org/unodc/en/data-and-analysis/glotip.html",
        selectors=["a[href*='.pdf']", "a[href*='glotip']"],
        schedule_days=180,
        description="Global Report on Trafficking in Persons",
    ),
    SourceConfig(
        id="us-tip-report",
        name="US TIP Report",
        tier=1,
        url="https://www.state.gov/trafficking-in-persons-report/",
        selectors=["a[href*='trafficking']", "a[href*='.pdf']"],
        schedule_days=365,
        description="US State Department Trafficking in Persons Report",
    ),
    SourceConfig(
        id="iom-data-portal",
        name="IOM Migration Data Portal",
        tier=1,
        url="https://www.migrationdataportal.org/themes/human-trafficking",
        selectors=["a[href*='resource']", "a[href*='dataset']", "a[href*='.pdf']"],
        schedule_days=60,
        description="IOM migration statistics and trafficking data",
    ),
    SourceConfig(
        id="ilo-natlex",
        name="ILO NATLEX",
        tier=1,
        url="https://www.ilo.org/dyn/natlex/natlex4.listResults?p_lang=en&p_count=50&p_classification=03&p_classcount=1",
        selectors=["a[href*='natlex']", "a[href*='detail']"],
        schedule_days=90,
        description="ILO database of national labour legislation",
    ),
    SourceConfig(
        id="ohchr-sr-trafficking",
        name="UN OHCHR SR Trafficking",
        tier=1,
        url="https://www.ohchr.org/en/special-procedures/sr-trafficking-in-persons",
        selectors=["a[href*='document']", "a[href*='report']", "a[href*='.pdf']"],
        schedule_days=90,
        description="UN Special Rapporteur on Trafficking in Persons reports",
    ),
    SourceConfig(
        id="world-bank-migration",
        name="World Bank Migration & Remittances",
        tier=1,
        url="https://www.worldbank.org/en/topic/labormarkets/brief/migration-and-remittances",
        selectors=["a[href*='publication']", "a[href*='brief']", "a[href*='.pdf']"],
        schedule_days=180,
        description="World Bank data on migration corridors and remittance flows",
    ),
    # =========================================================================
    # Tier 2: Philippines Government (9)
    # =========================================================================
    SourceConfig(
        id="dmw-advisories",
        name="DMW Advisories",
        tier=2,
        url="https://dmw.gov.ph/advisories",
        selectors=["a[href*='advisory']", "a[href*='news']", ".entry-title a"],
        schedule_days=7,
        description="Department of Migrant Workers labour advisories",
        corridors=["PH-SA", "PH-AE", "PH-QA", "PH-HK", "PH-SG"],
    ),
    SourceConfig(
        id="dmw-blas",
        name="DMW Bilateral Agreements",
        tier=2,
        url="https://dmw.gov.ph/bilateral-labor-agreements",
        selectors=["a[href*='agreement']", "a[href*='.pdf']"],
        schedule_days=90,
        description="Bilateral labour agreements between PH and destination countries",
        corridors=["PH-SA", "PH-AE", "PH-QA", "PH-KW", "PH-JP"],
    ),
    SourceConfig(
        id="polo-hk",
        name="POLO Hong Kong",
        tier=2,
        url="https://polohongkong.dfa.gov.ph",
        selectors=["a[href*='advisory']", "a[href*='news']", ".post-title a"],
        schedule_days=7,
        description="Philippine Overseas Labor Office - Hong Kong notices",
        corridors=["PH-HK"],
    ),
    SourceConfig(
        id="polo-sg",
        name="POLO Singapore",
        tier=2,
        url="https://polosingapore.dfa.gov.ph",
        selectors=["a[href*='advisory']", "a[href*='news']", ".post-title a"],
        schedule_days=7,
        description="Philippine Overseas Labor Office - Singapore notices",
        corridors=["PH-SG"],
    ),
    SourceConfig(
        id="polo-sa",
        name="POLO Saudi Arabia",
        tier=2,
        url="https://poloriyadh.dfa.gov.ph",
        selectors=["a[href*='advisory']", "a[href*='news']", ".post-title a"],
        schedule_days=7,
        description="Philippine Overseas Labor Office - Riyadh notices",
        corridors=["PH-SA"],
    ),
    SourceConfig(
        id="polo-qa",
        name="POLO Qatar",
        tier=2,
        url="https://polodoha.dfa.gov.ph",
        selectors=["a[href*='advisory']", "a[href*='news']", ".post-title a"],
        schedule_days=7,
        description="Philippine Overseas Labor Office - Doha notices",
        corridors=["PH-QA"],
    ),
    SourceConfig(
        id="polo-ae",
        name="POLO UAE",
        tier=2,
        url="https://poloadudhabi.dfa.gov.ph",
        selectors=["a[href*='advisory']", "a[href*='news']", ".post-title a"],
        schedule_days=7,
        description="Philippine Overseas Labor Office - Abu Dhabi notices",
        corridors=["PH-AE"],
    ),
    SourceConfig(
        id="owwa",
        name="OWWA",
        tier=2,
        url="https://owwa.gov.ph",
        selectors=["a[href*='program']", "a[href*='news']", ".entry-title a"],
        schedule_days=30,
        description="Overseas Workers Welfare Administration programs",
        corridors=["PH-SA", "PH-AE", "PH-QA", "PH-HK", "PH-SG"],
    ),
    SourceConfig(
        id="doj-iacat",
        name="PH DOJ IACAT",
        tier=2,
        url="https://iacat.gov.ph",
        selectors=["a[href*='news']", "a[href*='advisory']", "a[href*='.pdf']"],
        schedule_days=30,
        description="Inter-Agency Council Against Trafficking",
        corridors=["PH-SA", "PH-AE", "PH-QA", "PH-HK", "PH-SG"],
    ),
    # =========================================================================
    # Tier 3: Indonesia Government (4)
    # =========================================================================
    SourceConfig(
        id="bp2mi",
        name="BP2MI",
        tier=3,
        url="https://bp2mi.go.id",
        selectors=["a[href*='berita']", "a[href*='data']", ".news-title a"],
        schedule_days=30,
        description="Indonesian Agency for the Protection of Migrant Workers",
        language="id",
        corridors=["ID-SG", "ID-MY", "ID-SA", "ID-HK"],
    ),
    SourceConfig(
        id="kemenaker",
        name="Kemenaker",
        tier=3,
        url="https://kemnaker.go.id",
        selectors=["a[href*='berita']", "a[href*='regulasi']"],
        schedule_days=30,
        description="Indonesian Ministry of Manpower regulations",
        language="id",
        corridors=["ID-SG", "ID-MY", "ID-SA"],
    ),
    SourceConfig(
        id="kemlu-mfa",
        name="Kemlu (MFA)",
        tier=3,
        url="https://kemlu.go.id/portal/en/list/citizen-protection",
        selectors=["a[href*='citizen']", "a[href*='article']", "a[href*='.pdf']"],
        schedule_days=30,
        description="Indonesian Ministry of Foreign Affairs citizen protection",
        language="id",
        corridors=["ID-SG", "ID-MY", "ID-SA", "ID-HK"],
    ),
    SourceConfig(
        id="bnp2tki-data",
        name="BNP2TKI Data",
        tier=3,
        url="https://bp2mi.go.id/statistik-penempatan",
        selectors=["a[href*='statistik']", "a[href*='data']", "table a"],
        schedule_days=90,
        description="Indonesian migrant worker placement statistics",
        language="id",
        corridors=["ID-SG", "ID-MY", "ID-SA", "ID-HK", "ID-TW"],
    ),
    # =========================================================================
    # Tier 4: Destination Country Regulators (10)
    # =========================================================================
    SourceConfig(
        id="hk-labour-dept",
        name="HK Labour Department",
        tier=4,
        url="https://www.labour.gov.hk/eng/plan/iwFDH.htm",
        selectors=["a[href*='fdh']", "a[href*='foreign_domestic']", "a[href*='.pdf']", "a[href*='practical']"],
        schedule_days=30,
        description="Hong Kong Employment Ordinance and FDH info — practical guide for FDH employment",
        corridors=["PH-HK", "ID-HK"],
        feed_url="https://www.info.gov.hk/gia/rssgn.html",
    ),
    SourceConfig(
        id="hk-immigration",
        name="HK Immigration",
        tier=4,
        url="https://www.immd.gov.hk",
        selectors=["a[href*='foreign_domestic']", "a[href*='visa']"],
        schedule_days=30,
        description="Hong Kong visa and FDH policies",
        corridors=["PH-HK", "ID-HK"],
    ),
    SourceConfig(
        id="sg-mom-fdw",
        name="SG MOM FDW",
        tier=4,
        url="https://www.mom.gov.sg/passes-and-permits/work-permit-for-foreign-domestic-worker",
        selectors=["a[href*='foreign-domestic']", "a[href*='employment-agencies']"],
        schedule_days=30,
        description="Singapore MOM foreign domestic worker regulations",
        corridors=["PH-SG", "ID-SG", "MM-SG"],
        feed_url="https://www.mom.gov.sg/rss/newsroom",
    ),
    SourceConfig(
        id="sg-mom-ea",
        name="SG MOM EA Directory",
        tier=4,
        url="https://www.mom.gov.sg/passes-and-permits/work-permit-for-foreign-domestic-worker/hiring-a-foreign-domestic-worker/employment-agencies",
        selectors=["a[href*='agency']", "a[href*='ea-directory']"],
        schedule_days=7,
        description="Singapore licensed employment agency directory",
        corridors=["PH-SG", "ID-SG"],
    ),
    SourceConfig(
        id="qa-mol",
        name="Qatar MOL",
        tier=4,
        url="https://www.mol.gov.qa/en",
        selectors=["a[href*='law']", "a[href*='worker']", "a[href*='.pdf']"],
        schedule_days=30,
        description="Qatar Ministry of Labour — worker rights and labour law",
        corridors=["NP-QA", "PH-QA", "BD-QA"],
    ),
    SourceConfig(
        id="sa-mol-musaned",
        name="Saudi MOL Musaned",
        tier=4,
        url="https://www.hrsd.gov.sa/en",
        selectors=["a[href*='service']", "a[href*='regulation']", "a[href*='.pdf']"],
        schedule_days=30,
        description="Saudi Ministry of Human Resources — Musaned system",
        requires_js=True,
        stealth_level=3,
        corridors=["PH-SA", "ID-SA", "BD-SA", "NP-SA"],
    ),
    SourceConfig(
        id="ae-mohre",
        name="UAE MOHRE",
        tier=4,
        url="https://www.mohre.gov.ae/en/home.aspx",
        selectors=["a[href*='legislation']", "a[href*='services']", "a[href*='.pdf']"],
        schedule_days=30,
        description="UAE Ministry of Human Resources and Emiratisation",
        corridors=["PH-AE", "ID-AE", "BD-AE", "NP-AE"],
    ),
    SourceConfig(
        id="my-imi",
        name="Malaysia IMI",
        tier=4,
        url="https://www.imi.gov.my/portal2017/index.php/en/",
        selectors=["a[href*='foreign']", "a[href*='worker']", "a[href*='.pdf']"],
        schedule_days=30,
        description="Malaysia Immigration Department foreign worker policies",
        corridors=["BD-MY", "ID-MY", "MM-MY"],
    ),
    SourceConfig(
        id="kr-eps",
        name="Korea MOEL (EPS)",
        tier=4,
        url="https://www.eps.go.kr/eo/EmployInfo.eo",
        selectors=["a[href*='employ']", "a[href*='info']"],
        schedule_days=60,
        description="Korea Employment Permit System for migrant workers",
        requires_js=True,
        stealth_level=3,
        language="ko",
        corridors=["PH-KR", "NP-KR", "BD-KR"],
    ),
    SourceConfig(
        id="jp-ssw",
        name="Japan MHLW (SSW)",
        tier=4,
        url="https://www.mhlw.go.jp/stf/newpage_000117702.html",
        selectors=["a[href*='specified-skilled']", "a[href*='foreign']", "a[href*='.pdf']"],
        schedule_days=60,
        description="Japan Specified Skilled Worker program",
        language="ja",
        corridors=["PH-JP", "ID-JP", "VN-JP"],
    ),
    # =========================================================================
    # Tier 5: NGOs & Research (13)
    # =========================================================================
    SourceConfig(
        id="walk-free",
        name="Walk Free / GSI",
        tier=5,
        url="https://www.walkfree.org",
        selectors=["a[href*='report']", "a[href*='resource']", "a[href*='.pdf']"],
        schedule_days=365,
        description="Global Slavery Index",
    ),
    SourceConfig(
        id="ctdc",
        name="CTDC",
        tier=5,
        url="https://www.ctdatacollaborative.org",
        selectors=["a[href*='dataset']", "a[href*='publication']"],
        schedule_days=90,
        description="Counter-Trafficking Data Collaborative datasets",
    ),
    SourceConfig(
        id="justice-centre-hk",
        name="Justice Centre Hong Kong",
        tier=5,
        url="https://justicecentre.org.hk",
        selectors=["a[href*='report']", "a[href*='resource']", "a[href*='.pdf']"],
        schedule_days=90,
        description="HK domestic worker reports and research",
        corridors=["PH-HK", "ID-HK"],
    ),
    SourceConfig(
        id="twc2",
        name="TWC2 Singapore",
        tier=5,
        url="https://twc2.org.sg",
        selectors=["a[href*='research']", "a[href*='report']", ".entry-title a"],
        schedule_days=30,
        description="Transient Workers Count Too - SG migrant worker research",
        corridors=["BD-SG", "PH-SG", "ID-SG"],
    ),
    SourceConfig(
        id="migrant-forum-asia",
        name="Migrant Forum in Asia",
        tier=5,
        url="https://mfasia.org",
        selectors=["a[href*='publication']", "a[href*='resource']", ".post-title a"],
        schedule_days=30,
        description="Regional advocacy reports on Asian migration",
    ),
    SourceConfig(
        id="apmm",
        name="APMM",
        tier=5,
        url="https://apmigrants.org",
        selectors=["a[href*='publication']", "a[href*='statement']"],
        schedule_days=90,
        description="Asia-Pacific Mission for Migrants",
    ),
    SourceConfig(
        id="verite",
        name="Verite",
        tier=5,
        url="https://verite.org",
        selectors=["a[href*='research']", "a[href*='report']", "a[href*='.pdf']"],
        schedule_days=90,
        description="Supply chain labour reports",
    ),
    SourceConfig(
        id="polaris-project",
        name="Polaris Project",
        tier=5,
        url="https://polarisproject.org/resources/",
        selectors=["a[href*='resource']", "a[href*='report']", "a[href*='.pdf']"],
        schedule_days=90,
        description="US National Human Trafficking Hotline data and research",
    ),
    SourceConfig(
        id="liberty-shared",
        name="Liberty Shared",
        tier=5,
        url="https://www.libertyshared.org",
        selectors=["a[href*='report']", "a[href*='resource']", "a[href*='.pdf']"],
        schedule_days=90,
        description="Anti-trafficking legal intelligence (HK-focused)",
        corridors=["PH-HK", "ID-HK"],
    ),
    SourceConfig(
        id="freedom-fund",
        name="Freedom Fund",
        tier=5,
        url="https://freedomfund.org/research/",
        selectors=["a[href*='research']", "a[href*='publication']", "a[href*='.pdf']"],
        schedule_days=180,
        description="Hotspot-focused anti-slavery research and data",
    ),
    SourceConfig(
        id="anti-slavery-intl",
        name="Anti-Slavery International",
        tier=5,
        url="https://www.antislavery.org/what-we-do/research/",
        selectors=["a[href*='research']", "a[href*='report']", "a[href*='.pdf']"],
        schedule_days=180,
        description="Oldest international human rights organisation — research reports",
    ),
    SourceConfig(
        id="la-strada-intl",
        name="La Strada International",
        tier=5,
        url="https://lastradainternational.org/resources/",
        selectors=["a[href*='resource']", "a[href*='publication']", "a[href*='.pdf']"],
        schedule_days=180,
        description="European anti-trafficking network publications",
    ),
    SourceConfig(
        id="cafe-asean",
        name="CAFE / ASEAN TRIANGLE",
        tier=5,
        url="https://www.ilo.org/projects/WCMS_226958",
        selectors=["a[href*='resource']", "a[href*='publication']", "a[href*='.pdf']"],
        schedule_days=180,
        description="ILO ASEAN TRIANGLE project on labour migration",
        corridors=["MM-TH", "BD-MY", "ID-MY"],
    ),
    # =========================================================================
    # Tier 6: Courts & Legal (5)
    # =========================================================================
    SourceConfig(
        id="hk-judiciary",
        name="HK Judiciary",
        tier=6,
        url="https://legalref.judiciary.hk/lrs/common/search/search_result_detail_frame.jsp",
        selectors=["a[href*='judgment']", "a[href*='lrs']"],
        schedule_days=90,
        description="Hong Kong court judgments on employment / trafficking cases",
        requires_js=True,
        stealth_level=3,
        corridors=["PH-HK", "ID-HK"],
    ),
    SourceConfig(
        id="sg-statutes",
        name="SG Statutes Online",
        tier=6,
        url="https://sso.agc.gov.sg",
        selectors=["a[href*='Act']", "a[href*='SL']"],
        schedule_days=180,
        description="Singapore employment and foreign worker statutes",
        requires_js=True,
        stealth_level=3,
        corridors=["PH-SG", "ID-SG", "BD-SG"],
    ),
    SourceConfig(
        id="ph-supreme-court",
        name="PH Supreme Court E-Library",
        tier=6,
        url="https://elibrary.judiciary.gov.ph",
        selectors=["a[href*='decision']", "a[href*='ruling']"],
        schedule_days=90,
        description="Philippine Supreme Court trafficking and labour case law",
        corridors=["PH-SA", "PH-HK", "PH-QA"],
    ),
    SourceConfig(
        id="id-mk-ri",
        name="ID Constitutional Court",
        tier=6,
        url="https://www.mkri.id/index.php?page=web.Putusan&menu=4",
        selectors=["a[href*='putusan']", "a[href*='decision']"],
        schedule_days=180,
        description="Indonesian Constitutional Court — labour migration decisions",
        language="id",
        corridors=["ID-SG", "ID-MY", "ID-SA"],
    ),
    SourceConfig(
        id="echr-labour",
        name="ECHR Labour Exploitation",
        tier=6,
        url="https://hudoc.echr.coe.int/eng#{%22article%22:[%224%22]}",
        selectors=["a[href*='item']", "a[href*='hudoc']"],
        schedule_days=365,
        description="European Court of Human Rights Article 4 (slavery/forced labour) case law",
        requires_js=True,
        stealth_level=3,
    ),
    # =========================================================================
    # Tier 7: Academic & Research Databases (5)
    # =========================================================================
    SourceConfig(
        id="ssrn-trafficking",
        name="SSRN Trafficking Papers",
        tier=7,
        url="https://papers.ssrn.com/sol3/JELJOUR_Results.cfm?form_name=journalBrowse&journal_id=3437040",
        selectors=["a[href*='abstract']", "a[href*='papers']"],
        schedule_days=90,
        description="SSRN anti-trafficking and forced labour working papers",
    ),
    SourceConfig(
        id="gsi-data",
        name="Global Slavery Index Data",
        tier=7,
        url="https://www.globalslaveryindex.org/2023/findings/global-findings/",
        selectors=["a[href*='data']", "a[href*='findings']", "a[href*='.pdf']"],
        schedule_days=365,
        description="Walk Free Global Slavery Index quantitative data tables",
    ),
    SourceConfig(
        id="anti-slavery-research",
        name="Anti-Slavery Intl Research Hub",
        tier=7,
        url="https://www.antislavery.org/what-we-do/research/",
        selectors=["a[href*='research']", "a[href*='publication']", "a[href*='.pdf']"],
        schedule_days=180,
        description="Anti-Slavery International peer-reviewed research outputs",
    ),
    SourceConfig(
        id="oxford-compendium",
        name="Oxford Compendium on TIP",
        tier=7,
        url="https://opil.ouplaw.com/collection/human-trafficking-and-forced-labour",
        selectors=["a[href*='abstract']", "a[href*='content']"],
        schedule_days=365,
        description="Oxford international law compendium on trafficking",
        content_type="html",
    ),
    SourceConfig(
        id="ids-papers",
        name="IDS Migration Papers",
        tier=7,
        url="https://www.ids.ac.uk/publications/?topic=migration",
        selectors=["a[href*='publication']", "a[href*='working-paper']", "a[href*='.pdf']"],
        schedule_days=180,
        description="Institute of Development Studies migration working papers",
    ),
    # =========================================================================
    # Additional High-Value Sources
    # =========================================================================
    SourceConfig(
        id="ilo-c029-text",
        name="ILO C029 Convention Text",
        tier=1,
        url="https://www.ilo.org/dyn/normlex/en/f?p=NORMLEXPUB:12100:0::NO::P12100_INSTRUMENT_ID:312174",
        selectors=["a[href*='normlex']"],
        schedule_days=365,
        description="Full text of ILO Forced Labour Convention, 1930 (No. 29)",
    ),
    SourceConfig(
        id="palermo-protocol",
        name="UN Palermo Protocol",
        tier=1,
        url="https://www.unodc.org/unodc/en/treaties/CTOC/index.html",
        selectors=["a[href*='protocol']", "a[href*='.pdf']"],
        schedule_days=365,
        description="Protocol to Prevent, Suppress and Punish Trafficking in Persons (2000)",
    ),
    SourceConfig(
        id="ilo-global-estimates",
        name="ILO Global Estimates of Modern Slavery",
        tier=1,
        url="https://www.ilo.org/publications/major-publications/global-estimates-modern-slavery-forced-labour-and",
        selectors=["a[href*='publication']", "a[href*='.pdf']", "a[href*='global-estimates']"],
        schedule_days=365,
        description="ILO/Walk Free/IOM 2022 Global Estimates of Modern Slavery",
    ),

    # =========================================================================
    # Tier 6: Courts, Legal & Government Enforcement — US and EU additions
    # =========================================================================
    SourceConfig(
        id="courtlistener-api",
        name="CourtListener (Free Law Project)",
        tier=6,
        url="https://www.courtlistener.com/api/rest/v4/",
        content_type="api",
        selectors=[],
        schedule_days=30,
        description="CourtListener REST API — free US federal and state case law "
            "including PACER opinions. Search for trafficking, forced labor, "
            "involuntary servitude, peonage cases.",
        language="en",
    ),
    SourceConfig(
        id="doj-press-trafficking",
        name="DOJ Press Releases (Trafficking)",
        tier=6,
        url="https://www.justice.gov/humantrafficking/press-room",
        selectors=["a[href*='press-release']", "a[href*='/opa/pr/']"],
        schedule_days=14,
        description="US Department of Justice trafficking prosecution press releases "
            "and case announcements from the Human Trafficking Prosecution Unit.",
        language="en",
        feed_url="https://www.justice.gov/feeds/opa-press-releases.xml",
    ),
    SourceConfig(
        id="eurlex-antitrafficking",
        name="EUR-Lex Anti-Trafficking",
        tier=6,
        url="https://eur-lex.europa.eu/search.html?type=quick&text=trafficking+forced+labour",
        selectors=["a[href*='legal-content']", "a[href*='celex']"],
        schedule_days=90,
        description="EU law database — directives, regulations, and CJEU case law "
            "on trafficking and forced labor. Includes Directive 2011/36/EU "
            "and national transposition measures.",
        language="en",
    ),
    SourceConfig(
        id="greta-reports",
        name="GRETA Monitoring Reports",
        tier=6,
        url="https://www.coe.int/en/web/anti-human-trafficking/greta",
        selectors=["a[href*='greta']", "a[href*='.pdf']", "a[href*='country']"],
        schedule_days=180,
        description="Council of Europe GRETA anti-trafficking monitoring reports "
            "and country evaluations across 47 states parties.",
        language="en",
    ),
    SourceConfig(
        id="uk-nrm-data",
        name="UK National Referral Mechanism",
        tier=6,
        url="https://www.gov.uk/government/collections/national-referral-mechanism-statistics",
        selectors=["a[href*='national-referral']", "a[href*='.csv']", "a[href*='.ods']"],
        schedule_days=90,
        description="UK Home Office NRM quarterly statistics — referrals, positive "
            "decisions, nationality, exploitation type, first responder data.",
        language="en",
    ),
]


class SourceRegistry:
    """Load, save, and manage scraping source configurations."""

    def __init__(self, data_dir: str = "data/scraper"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.sources_file = self.data_dir / "sources.json"
        self._sources: Dict[str, SourceConfig] = {}
        self._load()

    # -- persistence -----------------------------------------------------------

    def _load(self) -> None:
        if self.sources_file.exists():
            raw = json.loads(self.sources_file.read_text(encoding="utf-8"))
            for item in raw:
                src = SourceConfig(**item)
                self._sources[src.id] = src
        else:
            # Seed with defaults
            for src in DEFAULT_SOURCES:
                self._sources[src.id] = src
            self._save()

    def _save(self) -> None:
        data = [asdict(s) for s in self._sources.values()]
        self.sources_file.write_text(
            json.dumps(data, indent=2, default=str), encoding="utf-8"
        )

    # -- CRUD ------------------------------------------------------------------

    def list_sources(self, tier: Optional[int] = None, enabled_only: bool = False) -> List[SourceConfig]:
        sources = list(self._sources.values())
        if tier is not None:
            sources = [s for s in sources if s.tier == tier]
        if enabled_only:
            sources = [s for s in sources if s.enabled]
        return sources

    def get(self, source_id: str) -> Optional[SourceConfig]:
        return self._sources.get(source_id)

    def create(self, config: SourceConfig) -> None:
        self._sources[config.id] = config
        self._save()

    def update(self, source_id: str, updates: Dict) -> Optional[SourceConfig]:
        src = self._sources.get(source_id)
        if not src:
            return None
        d = asdict(src)
        d.update(updates)
        self._sources[source_id] = SourceConfig(**d)
        self._save()
        return self._sources[source_id]

    def delete(self, source_id: str) -> bool:
        if source_id in self._sources:
            del self._sources[source_id]
            self._save()
            return True
        return False

    def toggle(self, source_id: str) -> Optional[bool]:
        src = self._sources.get(source_id)
        if not src:
            return None
        src.enabled = not src.enabled
        self._save()
        return src.enabled

    def mark_checked(self, source_id: str, doc_count_delta: int = 0) -> None:
        src = self._sources.get(source_id)
        if src:
            src.last_checked = datetime.now(tz=timezone.utc).isoformat()
            src.doc_count += doc_count_delta
            self._save()
