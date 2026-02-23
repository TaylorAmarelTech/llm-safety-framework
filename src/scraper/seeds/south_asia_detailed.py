"""South Asian migrant worker exploitation — India, Nepal, Bangladesh, Pakistan, Sri Lanka."""

SOUTH_ASIA_FACTS: list[dict] = [
    # ════════════════════════════════════════════════════════════════════
    #  INDIA (IN) — 45 facts
    # ════════════════════════════════════════════════════════════════════

    # ── Laws & Legislation ─────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "Bonded Labour System (Abolition) Act 1976 — India",
        "summary": (
            "Abolishes all forms of bonded labour and cancels outstanding debts "
            "used to bind labourers. Provides for release and rehabilitation of "
            "bonded labourers. District magistrates empowered to identify and "
            "free bonded workers. Penalties: up to 3 years imprisonment and fine "
            "for enforcing bonded labour. Widely regarded as landmark legislation, "
            "though enforcement remains weak especially in rural areas."
        ),
        "law": "Bonded Labour System (Abolition) Act 1976",
        "year": 1976,
        "source": "Government of India / Ministry of Labour and Employment",
    },
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "Inter-State Migrant Workmen (Regulation of Employment) Act 1979",
        "summary": (
            "Regulates employment of inter-state migrant workers recruited by "
            "contractors. Requires licensing of contractors, registration of "
            "establishments, and ensures equal wages, displacement allowance, "
            "journey allowance, and suitable accommodation. Applies to establishments "
            "employing 5 or more migrant workers. Enforcement hampered by lack of "
            "registration and informal recruitment."
        ),
        "law": "Inter-State Migrant Workmen Act 1979",
        "year": 1979,
        "source": "Government of India / Ministry of Labour and Employment",
    },
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "Trafficking of Persons (Prevention, Protection and Rehabilitation) Bill 2018",
        "summary": (
            "Comprehensive anti-trafficking bill passed by Lok Sabha in July 2018. "
            "Defines trafficking broadly including forced labour, bonded labour, "
            "and organ trafficking. Establishes anti-trafficking committees at "
            "national, state, and district levels. Provides for designated courts "
            "and rehabilitation fund. Bill lapsed with 16th Lok Sabha dissolution; "
            "similar provisions incorporated into subsequent legislative efforts."
        ),
        "law": "Trafficking of Persons Bill 2018",
        "year": 2018,
        "source": "Parliament of India / PRS Legislative Research",
    },
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "Emigration Act 1983 — India",
        "summary": (
            "Governs emigration of Indian workers for overseas employment. "
            "Establishes Protector of Emigrants offices in major cities. Creates "
            "Emigration Check Required (ECR) passport category for workers going "
            "to 18 designated countries (primarily Gulf and Southeast Asia). "
            "Requires recruiting agents to obtain registration certificates. "
            "Being replaced by Emigration Bill 2021 to modernize protections."
        ),
        "law": "Emigration Act 1983",
        "year": 1983,
        "source": "Government of India / Ministry of External Affairs",
    },
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "Occupational Safety, Health and Working Conditions Code 2020 — India",
        "summary": (
            "Consolidates 13 labour laws including Inter-State Migrant Workmen Act "
            "into a single code. Chapter XII specifically addresses inter-state "
            "migrant workers: mandates journey allowance, displacement allowance, "
            "toll-free helpline, portability of PDS benefits. Requires appointment "
            "of facilitators. Rules notified but implementation varies across states."
        ),
        "law": "OSH Code 2020",
        "year": 2020,
        "source": "Government of India / Ministry of Labour and Employment",
    },

    # ── Emigration & Gulf Migration Infrastructure ─────────────────────
    {
        "type": "regulation",
        "jurisdiction": "IN",
        "title": "e-Migrate System — Electronic Emigration Management",
        "summary": (
            "Mandatory online system launched 2015 for all ECR passport holders "
            "seeking employment in 18 countries. Links recruiting agents, employers, "
            "Indian missions, and Protector of Emigrants. Tracks worker deployment "
            "and return. By 2023, 6.5 million+ workers registered. Aims to eliminate "
            "fraudulent job offers and ensure pre-verified employment contracts."
        ),
        "source": "Ministry of External Affairs / e-Migrate portal",
    },
    {
        "type": "contact",
        "jurisdiction": "IN",
        "title": "Protector of Emigrants — Role and Offices",
        "summary": (
            "Government officer responsible for protecting interests of Indian "
            "emigrants. Offices in Mumbai, Delhi, Chennai, Kolkata, Hyderabad, "
            "Chandigarh, Thiruvananthapuram, Cochin, and Jaipur. Functions: "
            "verifying employment contracts, inspecting recruitment agencies, "
            "registering complaints, emigration clearance for ECR passport holders. "
            "Handles 200,000+ emigration clearances annually."
        ),
        "source": "Ministry of External Affairs / Protector General of Emigrants",
    },
    {
        "type": "contact",
        "jurisdiction": "IN",
        "title": "Indian Workers Resource Centre (IWRC) — Gulf States",
        "summary": (
            "Established by Indian Embassy/Consulate in Gulf countries to assist "
            "distressed Indian workers. Centres in Abu Dhabi, Dubai, Riyadh, "
            "Jeddah, Kuwait City, Doha, Muscat, Bahrain. Services: 24/7 helpline, "
            "legal advice, shelter for runaway workers, repatriation assistance, "
            "medical aid. Handled 100,000+ worker calls annually as of 2023."
        ),
        "source": "Ministry of External Affairs / Indian Embassies in GCC",
    },
    {
        "type": "contact",
        "jurisdiction": "IN",
        "title": "Pravasi Bharatiya Sahayata Kendras (PBSKs)",
        "summary": (
            "Support centres for Indian workers abroad established by MOIA/MEA. "
            "Located near labour camps and worker-dense areas in GCC states. "
            "Provide pre-departure orientation, document assistance, complaint "
            "registration, skill training, and financial literacy. Operated in "
            "partnership with NORKA-Roots (Kerala) and state migrant welfare boards."
        ),
        "source": "Ministry of External Affairs / Pravasi Bharatiya division",
    },
    {
        "type": "advisory",
        "jurisdiction": "IN",
        "title": "MOIA/MEA Welfare Schemes for Indian Migrant Workers",
        "summary": (
            "Multiple welfare schemes: Mahatma Gandhi Pravasi Suraksha Yojana "
            "(pension/insurance), Pravasi Bharatiya Bima Yojana (mandatory "
            "insurance for ECR workers, INR 10 lakh coverage), Indian Community "
            "Welfare Fund (emergency assistance, repatriation, legal aid, shelter). "
            "ICWF available in all Indian missions. INR 3,500 crore allocated "
            "2020-2025 for migrant worker welfare."
        ),
        "source": "MEA / ICWF Guidelines / PBBY Scheme",
    },

    # ── Gulf Corridor Exploitation ─────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "corridor": "IN-SA",
        "title": "Indian Construction Workers in Saudi Arabia — Wage Theft Pattern",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "Recurring pattern: Indian workers in Saudi construction report "
            "3-12 months unpaid wages. Companies cite 'project delays' or "
            "'cash flow problems.' Workers cannot change employer under kafala. "
            "2016: 10,000+ Indian workers stranded in Jeddah after Saudi Oger "
            "collapsed owing months of back wages. Indian Embassy provided food "
            "and repatriation for 4,000 workers."
        ),
        "source": "Indian Embassy Riyadh / Gulf News / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "corridor": "IN-AE",
        "title": "Indian Workers in UAE — Recruitment Fee Debt Cycle",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "Indian workers pay INR 80,000-250,000 to recruitment agents for "
            "UAE placements. Families mortgage land or borrow from moneylenders "
            "at 3-5% monthly interest. Arrive to find salary AED 800-1,200/month "
            "(lower than promised). Debt repayment takes 12-24 months. Workers "
            "trapped: cannot leave without employer NOC, cannot earn enough to "
            "repay and support family simultaneously."
        ),
        "source": "Amnesty International / Centre for Indian Migrant Studies",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "corridor": "IN-QA",
        "title": "Indian Workers in Qatar — FIFA World Cup Infrastructure Deaths",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "Indian nationals accounted for largest share of migrant worker "
            "deaths in Qatar (2010-2020). Indian Embassy data: 2,711 Indian "
            "deaths in Qatar over that period. Causes listed: 'natural causes,' "
            "'cardiac arrest' — often linked to heat exposure during 45+C summer "
            "work. Wage theft, passport confiscation, and cramped labour camps "
            "widely documented."
        ),
        "source": "The Guardian / Indian Embassy Qatar / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "corridor": "IN-KW",
        "title": "Indian Domestic Workers in Kuwait — Exploitation and Deaths",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Reports of Indian domestic workers in Kuwait subjected to physical "
            "abuse, food deprivation, 18-hour workdays, confinement, and sexual "
            "violence. Several documented deaths of Indian women domestic workers "
            "2017-2023. India has raised the minimum age for women migrating to "
            "Gulf states for domestic work multiple times. Indian Embassy operates "
            "shelter for runaway domestic workers."
        ),
        "source": "Indian Embassy Kuwait / NDTV / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "OM",
        "corridor": "IN-OM",
        "title": "Indian Workers in Oman — Contract Substitution",
        "exploitation_type": "deception",
        "sector": "services",
        "summary": (
            "Workers recruited in Kerala and Tamil Nadu for hospitality and retail "
            "jobs in Oman at OMR 200-300/month. Arrive to find different employer "
            "and OMR 80-120/month salary. Passports confiscated. Agent in India "
            "denies involvement. Workers file complaints with Protector of "
            "Emigrants but resolution takes 6-18 months."
        ),
        "source": "Protector of Emigrants Cochin / Centre for Development Studies",
    },

    # ── Kerala-Gulf Migration Corridor ─────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "IN",
        "title": "Kerala-Gulf Migration — Scale and Remittance Dependency",
        "summary": "2.1 million Keralite workers in GCC states; remittances constitute 36% of Kerala's GSDP.",
        "metric": "Keralite workers in Gulf states",
        "value": "2.1 million",
        "year": 2023,
        "details": (
            "Kerala is India's largest source of Gulf migrants. 2.1 million "
            "Keralites in GCC states (primarily UAE, Saudi Arabia, Kuwait, Qatar, "
            "Oman, Bahrain). Remittances constitute 36% of Kerala's GSDP. "
            "NORKA-Roots (Non-Resident Keralites Affairs) manages welfare and "
            "reintegration programs for 1.5 million return migrants."
        ),
        "source": "Kerala Migration Survey / NORKA-Roots / CDS Thiruvananthapuram",
    },
    {
        "type": "advisory",
        "jurisdiction": "IN",
        "title": "Kerala Return Migrant Crisis — Post-2020",
        "summary": (
            "COVID-19 and Gulf economic slowdown caused return of 1.2+ million "
            "Keralite workers (2020-2022). Many returned with unpaid wages, "
            "no savings, and outstanding debt. NORKA-Roots 'Pravasi Dividend "
            "Pension Scheme' and 'Santhwana' scheme provide limited relief. "
            "Suicide rate among return migrants reportedly 3x state average. "
            "Return migrants face stigma and limited local employment options."
        ),
        "source": "NORKA-Roots / Kerala State Planning Board / CDS",
    },

    # ── Internal Trafficking & Bonded Labour ───────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Rajasthan-Gujarat Brick Kiln Bonded Labour",
        "exploitation_type": "debt_bondage",
        "sector": "brick_kiln",
        "summary": (
            "Systematic bonded labour in brick kilns across Rajasthan and Gujarat. "
            "Families (including children) recruited from tribal areas of Rajasthan, "
            "Madhya Pradesh, and Chhattisgarh via advance payments (peshgi) of "
            "INR 10,000-30,000. Entire families work 14-16 hours/day for 6-month "
            "season. End-of-season deductions for 'food, shelter, breakage' often "
            "leave workers in debt for next season. Estimated 100,000+ bonded "
            "workers in Gujarat brick kilns alone."
        ),
        "source": "National Human Rights Commission / ILO India / Jan Sahas",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Tamil Nadu Sumangali Scheme — Bonded Labour in Spinning Mills",
        "exploitation_type": "debt_bondage",
        "sector": "garment",
        "summary": (
            "Young women (14-18 years) from Dalit and tribal communities recruited "
            "for spinning mills in Tamil Nadu with promise of lump sum (INR 30,000-"
            "50,000) after 3-year contract for marriage expenses (sumangali = "
            "'happily married woman'). Confined to factory hostels, 12-hour shifts, "
            "verbal/physical abuse. Many never receive final payment. Estimated "
            "100,000+ workers in this system across Erode, Tirupur, and Coimbatore "
            "districts. Multiple NHRC and court interventions."
        ),
        "source": "SOMO / ICN / Anti-Slavery International / NHRC",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Andhra Pradesh-Gulf Recruitment Fraud",
        "exploitation_type": "deception",
        "sector": "multiple",
        "summary": (
            "Hyderabad is a major hub for Gulf recruitment with both licensed and "
            "unlicensed agents. Common fraud: fake visa stamps, nonexistent "
            "employers, inflated salary promises. Workers from Andhra Pradesh "
            "and Telangana pay INR 100,000-400,000 through sub-agents. Hundreds "
            "of complaints filed annually with Protector of Emigrants Hyderabad. "
            "Several large-scale fraud rings busted 2018-2023 involving 500+ "
            "victims each."
        ),
        "source": "Protector of Emigrants Hyderabad / Telangana Police / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Construction Worker Exploitation — Internal Migration",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "100+ million internal migrant construction workers in India. Workers "
            "from Bihar, Jharkhand, Odisha, and Chhattisgarh migrate to metro "
            "cities. Recruited by thekedars (labour contractors) with advance. "
            "Piece-rate wages withheld until project completion. No written "
            "contracts. Housed in makeshift shelters on construction sites. "
            "No access to PDS, healthcare, or children's education. COVID-19 "
            "lockdown exposed extreme vulnerability of this workforce."
        ),
        "source": "Aajeevika Bureau / Jan Sahas / Stranded Workers Action Network",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Indian Fishing Sector — Bonded Labour on Deep-Sea Vessels",
        "exploitation_type": "restriction_of_movement",
        "sector": "fishing",
        "summary": (
            "Workers from coastal Tamil Nadu, Andhra Pradesh, and Odisha recruited "
            "for deep-sea fishing with advance payments. Confined to vessels for "
            "weeks/months. Share-based payment system results in minimal earnings. "
            "Physical violence for refusal to work. No safety equipment. Worker "
            "deaths at sea underreported. ILO Work in Fishing Convention (C188) "
            "not ratified by India."
        ),
        "source": "ILO / National Fishworkers Forum / International Collective in Support of Fishworkers",
    },
    {
        "type": "statistic",
        "jurisdiction": "IN",
        "title": "India Child Labour Statistics",
        "summary": "Census 2011 recorded 10.1 million child labourers aged 5-14; actual figure likely higher including hazardous work for 15-17 year olds.",
        "metric": "Children in child labour (ages 5-17)",
        "value": "10.1 million",
        "year": 2011,
        "details": (
            "Census 2011 recorded 10.1 million child labourers aged 5-14. "
            "ILO/UNICEF estimate suggests actual figure significantly higher when "
            "including 15-17 year olds in hazardous work. Highest prevalence: "
            "agriculture (56%), manufacturing (18%), services (26%). States with "
            "most child labour: Uttar Pradesh, Bihar, Rajasthan, Madhya Pradesh, "
            "Maharashtra. Child Labour (Prohibition and Regulation) Amendment Act "
            "2016 banned employment of children under 14 in all occupations."
        ),
        "source": "Census of India 2011 / ILO-UNICEF / NCPCR",
    },
    {
        "type": "statistic",
        "jurisdiction": "IN",
        "title": "India Bonded Labour — National Estimates",
        "summary": "Global Slavery Index estimates 11 million in modern slavery in India; only 313,000 officially identified and released since 1976.",
        "metric": "Estimated bonded labourers in India",
        "value": "8-18 million",
        "year": 2023,
        "details": (
            "Estimates vary widely. Global Slavery Index (2023): 11 million in "
            "modern slavery in India. Sectors: agriculture (40%), brick kilns "
            "(20%), stone quarries (10%), rice mills, garments, domestic work. "
            "Supreme Court directed identification surveys but only 313,000 "
            "officially identified and released since 1976. Rehabilitation: "
            "INR 20,000 per released bonded labourer (increased to INR 1-3 lakh "
            "under centrally sponsored scheme 2016)."
        ),
        "source": "Global Slavery Index / NHRC / Ministry of Labour and Employment",
    },

    # ── Supreme Court & Legal Decisions ────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "IN",
        "title": "Bandhua Mukti Morcha v. Union of India (1984) — Supreme Court",
        "summary": (
            "Landmark PIL by bonded labour activist Swami Agnivesh. Supreme Court "
            "held: whenever a person is found working for less than minimum wage, "
            "a presumption of bonded labour arises. Directed states to identify, "
            "release, and rehabilitate bonded labourers. Established that Article "
            "21 (right to life) includes right to live with dignity, free from "
            "exploitation. Led to formation of vigilance committees."
        ),
        "source": "Supreme Court of India / AIR 1984 SC 802",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IN",
        "title": "People's Union for Democratic Rights v. Union of India (1982) — Asiad Workers Case",
        "summary": (
            "Workers constructing facilities for 1982 Asian Games in Delhi paid "
            "below minimum wages by contractors. Supreme Court held: forced labour "
            "under Article 23 includes payment below minimum wage. State has "
            "obligation to ensure contractors do not exploit workers. Established "
            "that intermediary contractors and principal employer share liability."
        ),
        "source": "Supreme Court of India / AIR 1982 SC 1473",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IN",
        "title": "Public Union for Civil Liberties v. State of Tamil Nadu (2004) — Bonded Labour in Stone Quarries",
        "summary": (
            "Supreme Court directed Tamil Nadu government to identify and release "
            "bonded labourers in stone quarries and rice mills. Ordered payment "
            "of minimum wages, back wages, and rehabilitation. Established that "
            "failure to pay minimum wages itself constitutes bonded labour under "
            "the 1976 Act. Court monitored compliance over multiple years."
        ),
        "source": "Supreme Court of India / (2004) 12 SCC 381",
    },

    # ── Additional India Internal Exploitation ─────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Bihar-Punjab Agricultural Migrant Labour Exploitation",
        "exploitation_type": "withholding_wages",
        "sector": "agriculture",
        "summary": (
            "Seasonal agricultural workers from Bihar migrate to Punjab for "
            "wheat/rice harvesting. Recruited by thekedars who provide advances. "
            "Workers housed in fields with no shelter. Wages promised at INR 350-"
            "400/day but deductions for food, transport, and advances leave "
            "INR 150-200/day. Workers cannot leave until harvest complete. "
            "Estimated 1-2 million seasonal migrants on this corridor annually."
        ),
        "source": "Aajeevika Bureau / IGSSS / Disha Foundation",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Odisha-Andhra Pradesh Brick Kiln Trafficking",
        "exploitation_type": "debt_bondage",
        "sector": "brick_kiln",
        "summary": (
            "Tribal families from Odisha's Bolangir, Nuapada, and Kalahandi "
            "districts trafficked to brick kilns in Andhra Pradesh and Telangana. "
            "Sardars (labour contractors) provide INR 15,000-40,000 advances. "
            "Families including children work 14-hour days. End-of-season "
            "accounting perpetuates debt cycle. National Human Rights Commission "
            "has conducted multiple rescue operations."
        ),
        "source": "NHRC / ActionAid / Aide et Action",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Assam Tea Plantation Labour — Historical Bonded Labour Legacy",
        "exploitation_type": "isolation",
        "sector": "agriculture",
        "summary": (
            "Tea plantation workers in Assam descended from Adivasi communities "
            "brought during colonial era. Generations living on plantations with "
            "no land ownership. Wages among lowest in India (INR 205/day in 2023 "
            "vs INR 350 minimum wage). Housing, healthcare, and education tied to "
            "employment. Workers cannot easily leave as all services depend on "
            "plantation. Plantation Labour Act 1951 enforcement remains poor."
        ),
        "source": "ILO / Oxfam India / Columbia Law School Human Rights Clinic",
    },
    {
        "type": "statistic",
        "jurisdiction": "IN",
        "title": "India eMigrate Deployment Statistics",
        "summary": "500,000+ Indian workers deployed annually via eMigrate; top destinations UAE, Saudi Arabia, Kuwait, Qatar, Oman.",
        "metric": "Annual workers deployed via eMigrate",
        "value": "500,000+",
        "year": 2023,
        "details": (
            "Top destinations: UAE (180,000), Saudi Arabia (140,000), Kuwait "
            "(50,000), Qatar (45,000), Oman (40,000), Bahrain (15,000). "
            "Top origin states: Uttar Pradesh, Bihar, Rajasthan, Kerala, "
            "Tamil Nadu, Andhra Pradesh. 85% deployed in construction, domestic "
            "work, and services. Female deployment ~15% of total."
        ),
        "source": "eMigrate portal / MEA Annual Report 2023-24",
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "IN",
        "title": "Fake Gulf Job Offer Syndicates — North India",
        "violation_type": "fraud",
        "corridor": "IN-AE",
        "summary": (
            "Organized syndicates in Uttar Pradesh and Bihar target unemployed "
            "youth with fake Gulf job offers. Modus operandi: social media ads, "
            "fake company letters, fraudulent visa stamps in passports. Victims "
            "pay INR 100,000-500,000. Some arrive abroad to find no job; others "
            "never travel. UP Police Anti-Human Trafficking Unit busted 15+ "
            "rings in 2022-2023 involving 2,000+ victims."
        ),
        "source": "UP Police AHTU / Protector of Emigrants Delhi / Times of India",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Jharkhand Mica Mine Child Labour",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "mining",
        "summary": (
            "Jharkhand and Bihar produce 25% of world's mica. An estimated "
            "20,000 children work in illegal mica mines in Koderma and Giridih "
            "districts. Children as young as 5 crawl into narrow shafts. Families "
            "earn INR 50-100/kg. Mica enters global cosmetics and electronics "
            "supply chains. Multiple child deaths from mine collapses. "
            "Responsible Mica Initiative (RMI) formed in 2017 to address."
        ),
        "source": "Terre des Hommes / DanWatch / Responsible Mica Initiative",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Uttar Pradesh Carpet Weaving — Child Bonded Labour",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Children from poor families in eastern UP's Bhadohi, Mirzapur, and "
            "Varanasi districts bonded to carpet looms through family debts. "
            "Children (some as young as 7) work 12-14 hours/day in poorly "
            "ventilated rooms. Develop respiratory ailments and spinal deformities. "
            "Rugmark/GoodWeave labelling initiative created to combat this. "
            "ILO-IPEC programs freed thousands of children since 1990s."
        ),
        "source": "GoodWeave / ILO-IPEC / Bachpan Bachao Andolan",
    },
    {
        "type": "advisory",
        "jurisdiction": "IN",
        "title": "Pre-Departure Orientation Training (PDOT) — India",
        "summary": (
            "Government-mandated orientation for ECR workers before departure. "
            "Covers: employment contract review, destination country laws and "
            "culture, rights and responsibilities, complaint mechanisms, emergency "
            "contacts. Conducted at 9 PDOT centres. Criticized for: short duration "
            "(1 day), only in Hindi/English (excludes many workers), does not "
            "cover practical survival information. ILO recommends expansion."
        ),
        "source": "MEA / ILO / Protector General of Emigrants",
    },
    {
        "type": "regulation",
        "jurisdiction": "IN",
        "title": "India Minimum Recruitment Fee Cap for Gulf Employment",
        "summary": (
            "Government sets maximum service charges for recruiting agents: "
            "INR 20,000 for unskilled workers, INR 30,000 for semi-skilled. "
            "In practice, workers pay INR 80,000-400,000 through sub-agents "
            "and intermediaries. Wide gap between regulation and practice. "
            "Sub-agents unregulated. Enforcement limited to licensed agency "
            "inspections. e-Migrate intended to increase transparency."
        ),
        "source": "Emigration Rules / Protector General of Emigrants / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Indian Seafarers — Abandonment Cases",
        "exploitation_type": "withholding_wages",
        "sector": "maritime",
        "summary": (
            "Indian seafarers constitute 12% of global merchant marine workforce. "
            "Cases of abandonment: shipowners strand crew aboard vessels in foreign "
            "ports without wages, provisions, or repatriation. ILO database lists "
            "dozens of Indian crew abandonment cases annually. Maritime Labour "
            "Convention (MLC) 2006 provides protections but enforcement depends "
            "on flag state. Indian DG Shipping registers complaints."
        ),
        "source": "ILO Abandonment Database / DG Shipping India / ITF",
    },
    {
        "type": "statistic",
        "jurisdiction": "IN",
        "title": "Indian Migrant Worker Remittances",
        "summary": "India is the world's largest remittance recipient at USD 125 billion (2023), equalling 3.4% of GDP.",
        "metric": "Annual remittance inflows",
        "value": "USD 125 billion",
        "year": 2023,
        "details": (
            "India is the world's largest recipient of remittances. USD 125 "
            "billion in 2023 (World Bank). UAE, USA, and Saudi Arabia are top "
            "remittance sources. Remittances equal ~3.4% of GDP. Kerala receives "
            "highest per-capita remittances. Formal channels dominate but informal "
            "hawala transfers persist, especially for undocumented workers."
        ),
        "source": "World Bank / RBI / Migration and Remittances Factbook",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "COVID-19 Migrant Worker Crisis — India Internal Migration",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "multiple",
        "summary": (
            "March 2020 lockdown stranded 40-60 million internal migrant workers. "
            "Workers walked hundreds of kilometres to home states. Over 300 "
            "documented deaths during migration (accidents, exhaustion, starvation). "
            "Exposed: no social safety net, no worker registration, no portable "
            "benefits. Supreme Court ordered states to provide transport and food. "
            "Led to One Nation One Ration Card and e-Shram portal (290M+ registrations)."
        ),
        "source": "Stranded Workers Action Network / Supreme Court of India / ILO",
    },

    # ════════════════════════════════════════════════════════════════════
    #  NEPAL (NP) — 33 facts
    # ════════════════════════════════════════════════════════════════════

    # ── Laws & Governance ──────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "NP",
        "title": "Foreign Employment Act 2007 (amended 2019) — Nepal",
        "summary": (
            "Primary legislation governing overseas employment of Nepali workers. "
            "Establishes Department of Foreign Employment (DoFE) as regulator. "
            "Requires licensing of recruitment agencies. Sets maximum recruitment "
            "fees. Prohibits sending workers to countries with armed conflict. "
            "2019 amendment: expanded worker protections, strengthened penalties "
            "for fraud, mandatory pre-departure orientation, insurance coverage."
        ),
        "law": "Foreign Employment Act 2064 (2007)",
        "year": 2007,
        "source": "Government of Nepal / Ministry of Labour, Employment and Social Security",
    },
    {
        "type": "regulation",
        "jurisdiction": "NP",
        "title": "Nepal Free-Visa, Free-Ticket Policy",
        "summary": (
            "Introduced in 2015 to shift recruitment costs from workers to "
            "employers. Employers in destination countries must pay for visa, "
            "airfare, and medical costs. Workers pay only for passport, "
            "orientation, and insurance (max NPR 20,000). In practice, enforcement "
            "is weak: 73% of workers still paid recruitment fees averaging "
            "NPR 100,000-200,000 through sub-agents (dalals) who operate outside "
            "the formal system."
        ),
        "source": "DoFE Nepal / ILO / Amnesty International",
    },
    {
        "type": "contact",
        "jurisdiction": "NP",
        "title": "Department of Foreign Employment (DoFE) — Nepal",
        "summary": (
            "Government agency under MoLESS responsible for regulating foreign "
            "employment. Functions: issuing labour permits, licensing recruitment "
            "agencies, investigating complaints, imposing sanctions. Issues "
            "350,000-500,000 labour permits annually. Criticized for: "
            "understaffing (fewer than 100 officers for 1,000+ agencies), "
            "slow complaint resolution (average 6-12 months), limited oversight "
            "of sub-agents."
        ),
        "source": "DoFE Nepal / MoLESS / Nepal Institute of Policy Studies",
    },
    {
        "type": "statistic",
        "jurisdiction": "NP",
        "title": "Foreign Employment Board — Key Statistics",
        "summary": "3.5 million Nepali workers abroad; Foreign Employment Board paid compensation for 7,467 worker deaths (2008-2022).",
        "metric": "Total Nepali workers abroad",
        "value": "3.5 million+",
        "year": 2023,
        "details": (
            "Foreign Employment Board manages compensation fund from worker "
            "contributions. 3.5 million Nepali workers abroad (estimated, "
            "including undocumented). Top destinations: Qatar, Saudi Arabia, "
            "UAE, Kuwait, Malaysia, South Korea. Annual deployment: 350,000-"
            "500,000. Board paid compensation for 7,467 worker deaths abroad "
            "(2008-2022). Compensation: NPR 500,000-1,500,000 per death."
        ),
        "source": "Foreign Employment Board / DoFE Nepal / IOM",
    },

    # ── Worker Deaths & Exploitation ───────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "NP",
        "title": "Nepali Migrant Worker Deaths Abroad — 7,000+ Documented",
        "summary": "7,467 Nepali migrant worker deaths abroad documented (2008-2022); average 530+ deaths per year, mostly classified as cardiac arrest.",
        "metric": "Documented worker deaths abroad",
        "value": "7,467",
        "year": 2022,
        "details": (
            "7,467 Nepali migrant worker deaths abroad documented by Foreign "
            "Employment Board (2008/09-2021/22). Average: 530+ deaths/year. "
            "Highest in: Qatar (1,800+), Saudi Arabia (1,600+), UAE (1,500+), "
            "Malaysia (1,200+), Kuwait (400+). Most common cause listed: "
            "'cardiac arrest' or 'natural causes.' Heat exposure, workplace "
            "accidents, and suicide significantly underreported. Families "
            "often receive bodies without autopsy."
        ),
        "source": "Foreign Employment Board Nepal / Pravasi Nepali Coordination Committee",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "corridor": "NP-QA",
        "title": "Nepali Workers in Qatar Construction — Debt Bondage and Death",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "Nepali workers pay NPR 100,000-300,000 to recruiters despite "
            "free-visa-free-ticket policy. Arrive to lower salary, different "
            "employer, 12-hour shifts in extreme heat. 1,800+ Nepali deaths in "
            "Qatar (2008-2022). Most classified as 'cardiac arrest.' Families "
            "receive NPR 500,000 compensation from Foreign Employment Board. "
            "Amnesty International documented systematic wage theft affecting "
            "thousands of Nepali construction workers."
        ),
        "source": "Amnesty International / The Guardian / Foreign Employment Board",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "corridor": "NP-SA",
        "title": "Nepali Workers in Saudi Arabia — Salary Non-Payment",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "Recurring pattern: Nepali workers in Saudi Arabia report 3-8 months "
            "unpaid wages. Companies claim cash flow problems. Workers cannot "
            "leave without employer NOC. Wage Protection System not enforced for "
            "smaller companies employing most Nepali workers. Nepal Embassy in "
            "Riyadh handles 3,000+ labour complaints annually."
        ),
        "source": "Nepal Embassy Riyadh / ILO / Pravasi Nepali Coordination Committee",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "corridor": "NP-AE",
        "title": "Nepali Workers in UAE — Construction and Hospitality Exploitation",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "Nepali workers recruited for UAE construction and hospitality pay "
            "NPR 80,000-200,000 to agents. Arrive to find lower-paying jobs. "
            "Cramped dormitories (8-12 per room), inadequate food, 10-14 hour "
            "shifts. Cannot change employer easily. 1,500+ Nepali deaths in "
            "UAE (2008-2022). Embassy provides limited shelter and repatriation "
            "assistance."
        ),
        "source": "Nepal Embassy Abu Dhabi / Foreign Employment Board / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "corridor": "NP-KW",
        "title": "Nepali Domestic Workers in Kuwait — Abuse and Trafficking",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Nepali women recruited as domestic workers in Kuwait face confinement, "
            "physical and sexual abuse, 18-hour workdays, salary withholding. "
            "Nepal banned women under 30 from migrating for domestic work in Gulf "
            "states (2012), later amended to under 24 (2017). Ban pushed women "
            "into irregular channels with even less protection. Documented cases "
            "of trafficking through India to circumvent Nepal's restrictions."
        ),
        "source": "Pourakhi Nepal / Amnesty International / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "NP-MY",
        "title": "Nepali Workers in Malaysia — Manufacturing Exploitation",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Nepali workers in Malaysian manufacturing pay NPR 150,000-300,000 "
            "to agents. Passport confiscation widespread. Housed in employer "
            "dormitories with wage deductions for accommodation. Forced overtime "
            "without premium pay. Malaysian MYR 1,500 minimum wage often not "
            "applied to foreign workers. US CBP WRO on Top Glove affected "
            "many Nepali workers."
        ),
        "source": "Pravasi Nepali Coordination Committee / Verité / US CBP",
    },

    # ── Sub-Agents & Recruitment ───────────────────────────────────────
    {
        "type": "recruitment_violation",
        "jurisdiction": "NP",
        "title": "Dalal (Sub-Agent) Exploitation System — Nepal",
        "violation_type": "unlicensed_recruitment",
        "summary": (
            "Dalals (informal sub-agents) operate in rural villages as first "
            "point of contact for aspiring migrants. Typically local individuals "
            "with connections to licensed agencies in Kathmandu. Charge NPR 50,000-"
            "150,000 above agency fees. No licensing, no accountability. Workers "
            "from remote districts (Doti, Bajura, Jumla, Humla) most vulnerable. "
            "Dalals also facilitate document falsification. Government has "
            "attempted to regulate sub-agents without success."
        ),
        "source": "DoFE Nepal / ILO / Transparency International Nepal",
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "NP",
        "title": "Nepal Recruitment Agency Violations — Systematic Fee Overcharging",
        "violation_type": "excessive_fees",
        "summary": (
            "Despite free-visa-free-ticket policy, ILO surveys show 73% of "
            "Nepali workers paid recruitment fees. Average fee: NPR 118,000 "
            "(USD 900). Range: NPR 50,000-400,000 depending on destination. "
            "Fees charged for: 'company selection fee,' 'orientation,' 'medical,' "
            "'insurance,' 'guarantee.' DoFE suspended/cancelled 200+ agency "
            "licences (2015-2023) but new agencies register easily."
        ),
        "source": "ILO / DoFE Nepal / Amnesty International",
    },

    # ── Internal & Structural Issues ───────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal Brick Kiln Bonded Labour — Internal Exploitation",
        "exploitation_type": "debt_bondage",
        "sector": "brick_kiln",
        "summary": (
            "Estimated 175,000 workers in Nepal's 800+ brick kilns. Workers from "
            "Terai and hill districts receive advances (peshgi) of NPR 10,000-"
            "30,000. Entire families work including children. 14-hour days during "
            "6-month season. End-of-season deductions often perpetuate debt. "
            "ILO estimates 42% of brick kiln workers are in forced labour. "
            "Children constitute 15-20% of workforce. Minimal government inspection."
        ),
        "source": "ILO Nepal / GEFONT / Brick Clean Nepal",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Kamaiya and Haliya Systems — Freed Bonded Labourers",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Kamaiya (bonded agricultural labourers in western Terai) system "
            "abolished in 2000 after decades of activism. 32,000 Kamaiya families "
            "freed. Haliya (bonded ploughman system in far-western hills) "
            "abolished in 2008. 19,000 Haliya families freed. Despite abolition, "
            "many freed Kamaiyas and Haliyas lack land, housing, and sustainable "
            "livelihoods. Government rehabilitation programs reach only 40% of "
            "identified families. Some revert to bonded-like arrangements."
        ),
        "source": "INSEC Nepal / ILO / Anti-Slavery International",
    },
    {
        "type": "statistic",
        "jurisdiction": "NP",
        "title": "Nepal 2015 Earthquake — Migration Surge",
        "summary": "2015 earthquake triggered 35% increase in labour migration as displaced families sought overseas income; recruiters targeted affected districts.",
        "metric": "Post-earthquake labour migration increase",
        "value": "35% increase",
        "year": 2015,
        "details": (
            "2015 earthquake (7.8 magnitude) killed 9,000 people, destroyed "
            "600,000 homes. Labour migration surged 35% in following 18 months "
            "as displaced families sought overseas income. Recruiters targeted "
            "earthquake-affected districts (Sindhupalchok, Gorkha, Dolakha) with "
            "promises of quick placements. Rushed migration led to increased "
            "fee exploitation and inadequate pre-departure preparation."
        ),
        "source": "DoFE Nepal / IOM / National Planning Commission Nepal",
    },
    {
        "type": "statistic",
        "jurisdiction": "NP",
        "title": "Nepal Remittance Dependency",
        "summary": "Nepal remittances USD 9.3 billion (2023), 27% of GDP — one of highest remittance-to-GDP ratios globally; 56% of households receive remittances.",
        "metric": "Remittances as share of GDP",
        "value": "27%",
        "year": 2023,
        "details": (
            "Nepal remittance inflows: USD 9.3 billion (2023), representing 27% "
            "of GDP. One of highest remittance-to-GDP ratios globally. 56% of "
            "Nepali households receive remittances. Major source countries: Qatar, "
            "Saudi Arabia, UAE, Malaysia, Kuwait. Remittances fund: household "
            "consumption (60%), education (15%), real estate (10%), savings (10%). "
            "Limited productive investment. Economic vulnerability to Gulf "
            "economic shocks."
        ),
        "source": "World Bank / Nepal Rastra Bank / Nepal Living Standards Survey",
    },
    {
        "type": "advisory",
        "jurisdiction": "NP",
        "title": "Nepal Returnee Reintegration Challenges",
        "summary": (
            "Estimated 1.5 million Nepali return migrants. Challenges: limited "
            "local employment matching skills gained abroad, social stigma for "
            "women returnees, debt from failed migration, PTSD from exploitation. "
            "Government reintegration programs: 'Employment Fund' (skills training), "
            "'Youth Self-Employment Fund' (loans). Coverage: fewer than 5% of "
            "returnees. IOM AVRR program assists voluntary return cases. "
            "Disproportionate suicide rate among return migrants documented."
        ),
        "source": "MoLESS Nepal / IOM / Pourakhi / CESLAM",
    },
    {
        "type": "advisory",
        "jurisdiction": "NP",
        "title": "Nepal Women's Migration Bans — History and Impact",
        "summary": (
            "History of gender-discriminatory migration restrictions. 1998: banned "
            "women under 35 from Gulf domestic work. 2012: banned women under 30. "
            "2017: lowered to under 24. Various temporary total bans on domestic "
            "work migration. Impact: pushed women into irregular channels through "
            "India (open border). Women crossing via India face trafficking risk. "
            "ILO and Pourakhi advocate for protection-based approach instead of "
            "outright bans."
        ),
        "source": "Pourakhi Nepal / ILO / WOREC / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal-India Open Border — Trafficking Vulnerability",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "multiple",
        "summary": (
            "1,880 km open border between Nepal and India requires no passport "
            "or visa. Facilitates: trafficking of women and girls for sexual "
            "exploitation (estimated 5,000-15,000 annually), irregular labour "
            "migration bypassing protections, child trafficking for circus and "
            "domestic work. Border monitoring posts understaffed. Maiti Nepal and "
            "Shakti Samuha intercept trafficking at border points."
        ),
        "source": "Maiti Nepal / National Human Rights Commission Nepal / IOM",
    },
    {
        "type": "statistic",
        "jurisdiction": "NP",
        "title": "Nepal Recruitment Fee Burden — Worker Survey Data",
        "summary": "ILO survey: 73% of Nepali workers paid recruitment fees averaging NPR 118,000 despite free-visa-free-ticket policy; 63% borrowed to pay fees.",
        "metric": "Average recruitment cost paid by worker",
        "value": "NPR 118,000 (USD 900)",
        "year": 2022,
        "details": (
            "ILO survey of 4,000 Nepali return migrants: median recruitment "
            "cost NPR 118,000 (USD 900). 73% paid some fee despite free-visa-"
            "free-ticket policy. For Malaysia: NPR 170,000 average. For Qatar: "
            "NPR 130,000 average. For Saudi Arabia: NPR 100,000 average. Workers "
            "from remote districts pay 30-50% more than Kathmandu Valley workers. "
            "63% borrowed to pay fees (average interest rate: 24% per annum)."
        ),
        "source": "ILO Nepal / CESLAM / Open Society Foundations",
    },

    # ════════════════════════════════════════════════════════════════════
    #  BANGLADESH (BD) — 33 facts
    # ════════════════════════════════════════════════════════════════════

    # ── Laws & Governance ──────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "BD",
        "title": "Overseas Employment and Migrants Act 2013 — Bangladesh",
        "summary": (
            "Primary legislation governing overseas employment. Establishes "
            "licensing system for recruitment agencies. Prohibits recruitment "
            "fee overcharging. Mandates pre-departure briefing. Creates Wage "
            "Earners Welfare Board (WEWB) for worker support. Penalties for "
            "fraud: up to 7 years imprisonment and BDT 500,000 fine. "
            "Enforcement hampered by powerful recruitment agency lobby and "
            "weak institutional capacity."
        ),
        "law": "Overseas Employment and Migrants Act 2013",
        "year": 2013,
        "source": "Government of Bangladesh / Ministry of Expatriates' Welfare and Overseas Employment",
    },
    {
        "type": "contact",
        "jurisdiction": "BD",
        "title": "BMET (Bureau of Manpower, Employment and Training) — Bangladesh",
        "summary": (
            "Primary government agency for overseas employment. Functions: "
            "registering recruitment agencies, maintaining worker database, "
            "processing deployment, skills training, complaint handling. "
            "Issues 700,000-1,000,000 clearance cards annually. Runs 70 Technical "
            "Training Centres. Criticized for: corruption in clearance process, "
            "inadequate monitoring of agencies, slow complaint resolution (average "
            "8-18 months for full resolution)."
        ),
        "source": "BMET / MoEWOE / IOM Bangladesh",
    },
    {
        "type": "contact",
        "jurisdiction": "BD",
        "title": "Wage Earners' Welfare Board (WEWB) — Bangladesh",
        "summary": (
            "Statutory body funded by worker contributions (BDT 2,500 per "
            "departure). Services: financial assistance for distressed workers, "
            "dead body repatriation, scholarships for workers' children, legal "
            "aid. WEWB has accumulated BDT 6,000+ crore in funds. Criticized "
            "for: slow disbursement, bureaucratic procedures, limited coverage "
            "(assists fewer than 5% of eligible workers), lack of transparency "
            "in fund management."
        ),
        "source": "WEWB / MoEWOE / BRAC Migration Program",
    },
    {
        "type": "regulation",
        "jurisdiction": "BD",
        "title": "Bangladesh Recruitment Agency Regulation",
        "summary": (
            "1,400+ licensed recruitment agencies in Bangladesh. Licence fee: "
            "BDT 500,000 + security deposit BDT 1,000,000. Maximum recruitment "
            "charge: BDT 84,000 (government-set). In practice, workers pay "
            "BDT 200,000-800,000 through dalal networks. BMET suspended/cancelled "
            "300+ licences (2015-2023) but agencies reopen under new names. "
            "Bangladesh Association of International Recruiting Agencies (BAIRA) "
            "is powerful industry lobby."
        ),
        "source": "BMET / BAIRA / ILO Bangladesh",
    },

    # ── Corridor Exploitation ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "corridor": "BD-SA",
        "title": "Bangladeshi Workers in Saudi Arabia — Systematic Exploitation",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "Saudi Arabia is top destination for Bangladeshi workers (250,000+ "
            "deployed annually). Workers pay BDT 300,000-600,000 to agents. "
            "Arrive to lower salary (SAR 800-1,200 vs promised SAR 1,500-2,000). "
            "Passport confiscated. 3-8 months wage withholding common. Workers "
            "cannot leave without employer NOC. Bangladesh Embassy handles "
            "10,000+ labour complaints annually."
        ),
        "source": "Bangladesh Embassy Riyadh / BRAC / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "BD-MY",
        "title": "BD-MY Corridor — Highest Recruitment Fees Globally",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Bangladesh-Malaysia corridor has highest documented recruitment fees "
            "in the world. Workers pay BDT 400,000-800,000 (USD 3,600-7,200) for "
            "Malaysian factory jobs paying MYR 1,500/month. Debt repayment "
            "consumes 12-24 months of wages. Multiple fee layers: dalal village "
            "level, dalal district level, licensed agency, Malaysian counterpart. "
            "ILO and World Bank studies confirm this is the costliest corridor."
        ),
        "source": "ILO / World Bank / BRAC Migration / Verité",
    },
    {
        "type": "case_study",
        "jurisdiction": "JO",
        "corridor": "BD-JO",
        "title": "Bangladeshi Garment Workers in Jordan QIZ — Exploitation",
        "exploitation_type": "excessive_overtime",
        "sector": "garment",
        "summary": (
            "15,000+ Bangladeshi workers in Jordan's Qualifying Industrial "
            "Zones (QIZ) garment factories. Workers pay BDT 200,000-350,000 to "
            "agents. 60-72 hour work weeks with forced overtime. Passport "
            "confiscation by employers. Locked dormitories. Sexual harassment of "
            "women workers documented. Better Work Jordan monitors conditions but "
            "violations persist. Workers producing for major US/EU brands."
        ),
        "source": "Better Work Jordan / Worker Rights Consortium / BRAC",
    },
    {
        "type": "case_study",
        "jurisdiction": "LB",
        "corridor": "BD-LB",
        "title": "Bangladeshi Domestic Workers in Lebanon — Kafala Exploitation",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Bangladeshi women recruited as domestic workers in Lebanon. "
            "Pay BDT 100,000-200,000 to agents. Arrive: passport confiscated, "
            "confined to household, 18-hour workdays, physical abuse, salary "
            "withholding. Lebanon's kafala system provides no legal recourse. "
            "Lebanon economic crisis (2019+) worsened conditions: employers "
            "stopped paying salaries, abandoned workers. Bangladesh temporarily "
            "banned female migration to Lebanon."
        ),
        "source": "Human Rights Watch / Anti-Slavery International / BRAC",
    },

    # ── Vulnerable Populations ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Rohingya Exploitation Vulnerability — Bangladesh",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "multiple",
        "summary": (
            "1 million+ Rohingya refugees in Cox's Bazar camps. Extreme "
            "vulnerability to trafficking and forced labour. No legal right to "
            "work in Bangladesh. Exploited in: fishing (Bay of Bengal), salt "
            "production, informal construction, sex trafficking. Trafficked to "
            "Malaysia and Thailand on boats (2015 Andaman Sea crisis, 2020-2023 "
            "ongoing). Children and women especially targeted. IOM and UNHCR "
            "anti-trafficking programs in camps."
        ),
        "source": "UNHCR / IOM / Human Rights Watch / US TIP Report",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Garment Sector — Internal Exploitation",
        "exploitation_type": "excessive_overtime",
        "sector": "garment",
        "summary": (
            "4 million+ garment workers in Bangladesh (80% women). Despite "
            "minimum wage increases (BDT 12,500/month from 2023), workers report: "
            "forced overtime (60+ hours/week), verbal abuse from supervisors, "
            "unsafe buildings (post-Rana Plaza 2013 reforms ongoing), anti-union "
            "retaliation. Internal migration from northern districts (Rangpur, "
            "Rajshahi) to Dhaka/Gazipur garment zones. Workers live in slums."
        ),
        "source": "Bangladesh Garment Manufacturers and Exporters Association / CCC / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Chittagong Ship-Breaking — Hazardous Labour",
        "exploitation_type": "abusive_working_conditions",
        "sector": "ship_breaking",
        "summary": (
            "Chittagong ship-breaking yards recycle 50% of global end-of-life "
            "vessels. 30,000-50,000 workers (many internal migrants from north). "
            "Conditions: asbestos exposure, toxic paint/oil, heavy metal "
            "contamination, no safety equipment, 12-hour shifts. Worker deaths: "
            "average 20-30 annually (likely underreported). Average wage: "
            "BDT 400-600/day. No health insurance. EU Ship Recycling Regulation "
            "and Hong Kong Convention aim to improve standards."
        ),
        "source": "FIDH / YPSA / Shipbreaking Platform / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Shrimp Farming — Forced and Child Labour",
        "exploitation_type": "debt_bondage",
        "sector": "aquaculture",
        "summary": (
            "Shrimp farming in Khulna and Satkhira districts employs 600,000+ "
            "workers. Documented forced labour: workers recruited with advances, "
            "trapped in remote ponds, children (11-14) used for seed collection "
            "in mangroves. EJF documented child labour in supply chains feeding "
            "US and EU markets. Certification schemes (ASC) improving conditions "
            "in some operations but informal sector largely unmonitored."
        ),
        "source": "EJF / Solidarity Center / US Department of Labor ILAB",
    },

    # ── Recruitment & Sub-Agents ───────────────────────────────────────
    {
        "type": "recruitment_violation",
        "jurisdiction": "BD",
        "title": "Dalal/Sub-Agent System — Bangladesh Recruitment Pipeline",
        "violation_type": "unlicensed_recruitment",
        "summary": (
            "Multi-layered dalal system is backbone of Bangladeshi migration. "
            "Village dalal → upazila dalal → district dalal → Dhaka agency. "
            "Each layer adds BDT 30,000-100,000 in fees. Total worker cost: "
            "BDT 200,000-800,000. Government estimates 100,000+ active dalals "
            "nationwide. Dalals operate through personal networks, tea stalls, "
            "mobile phones. No written contracts or receipts. Worker has no "
            "recourse if cheated by dalal."
        ),
        "source": "BMET / ILO / RMMRU (Refugee and Migratory Movements Research Unit)",
    },
    {
        "type": "statistic",
        "jurisdiction": "BD",
        "title": "Bangladesh Recruitment Fee Data — Survey Evidence",
        "summary": "Average total migration cost BDT 374,000 (USD 3,400) per worker; 89% pay above government cap of BDT 84,000; 78% borrow from moneylenders.",
        "metric": "Average recruitment cost paid by worker",
        "value": "BDT 374,000 (USD 3,400)",
        "year": 2022,
        "details": (
            "ILO/BRAC survey of 5,000 return migrants. Average total cost: "
            "BDT 374,000 (USD 3,400). For Saudi Arabia: BDT 350,000. For "
            "Malaysia: BDT 500,000+. For UAE: BDT 300,000. For Oman: BDT 280,000. "
            "Government maximum: BDT 84,000. 89% of workers paid above government "
            "cap. 78% borrowed from moneylenders (average interest 36-48% annually). "
            "Families sell land, take multiple loans to finance migration."
        ),
        "source": "ILO / BRAC Migration Program / RMMRU",
    },
    {
        "type": "statistic",
        "jurisdiction": "BD",
        "title": "Bangladesh Return Migrant Survey Findings",
        "summary": "BRAC survey: 41% of return migrants experienced wage theft; 27% had passports confiscated; only 8% filed complaints with BMET.",
        "metric": "Return migrants experiencing wage theft",
        "value": "41%",
        "year": 2022,
        "details": (
            "BRAC survey of 3,000 return migrants: 41% experienced some form "
            "of wage theft (non-payment, underpayment, or illegal deductions). "
            "27% had passport confiscated. 38% worked longer hours than contracted. "
            "15% reported physical abuse. 62% earned less than originally promised. "
            "Only 8% filed complaints with BMET. Of those: 23% received resolution "
            "within 12 months."
        ),
        "source": "BRAC Migration Program / RMMRU / IOM Bangladesh",
    },
    {
        "type": "statistic",
        "jurisdiction": "BD",
        "title": "Bangladesh Migrant Worker Remittances",
        "summary": "Bangladesh received USD 21.6 billion in remittances (2023); second largest foreign exchange source after garment exports, equalling 5.4% of GDP.",
        "metric": "Annual remittance inflows",
        "value": "USD 21.6 billion",
        "year": 2023,
        "details": (
            "Bangladesh received USD 21.6 billion in remittances (2023). "
            "Second largest source of foreign exchange after garment exports. "
            "Top source countries: Saudi Arabia, UAE, Malaysia, Kuwait, USA, "
            "Qatar, Oman. Remittances = 5.4% of GDP. 10 million+ households "
            "depend on remittances. Formal channels: bank transfers (growing), "
            "hundi/hawala (declining but still significant for undocumented)."
        ),
        "source": "Bangladesh Bank / World Bank / BMET",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Female Migrant Worker Exploitation — Middle East",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "200,000+ Bangladeshi women working as domestic workers in Gulf states "
            "and Lebanon. Reports of: physical/sexual abuse, confinement, food "
            "deprivation, 18-20 hour workdays, salary withholding. Government "
            "temporarily banned female migration to several countries. 2015: "
            "mandatory 21-day pre-departure training for women. Helpline "
            "(16345) for distressed workers. Return migrants face social stigma."
        ),
        "source": "BRAC / UN Women / Ovibashi Karmi Unnayan Program (OKUP)",
    },
    {
        "type": "advisory",
        "jurisdiction": "BD",
        "title": "Bangladesh-Saudi Arabia Bilateral Labour Agreement",
        "summary": (
            "Multiple MOUs between Bangladesh and Saudi Arabia (2008, 2016, 2022) "
            "on labour migration. Provisions: standard employment contract, "
            "wage protection, dispute resolution mechanism. In practice: "
            "agreements lack enforcement mechanisms, no joint monitoring, "
            "no penalties for violations. Bangladesh's weak bargaining position "
            "(competing with other source countries) limits leverage."
        ),
        "source": "MoEWOE / BMET / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Rana Plaza Collapse (2013) — Bangladesh Garment Worker Safety",
        "exploitation_type": "abusive_working_conditions",
        "sector": "garment",
        "summary": (
            "April 2013: Rana Plaza building collapse in Savar, Dhaka killed "
            "1,134 garment workers and injured 2,500+. Building had visible "
            "cracks day before; workers ordered to return to work. Produced for "
            "31 international brands. Led to: Bangladesh Accord on Fire and "
            "Building Safety (now International Accord), BSCI, Better Work. "
            "Compensation: USD 30 million Rana Plaza Fund (ILO-administered). "
            "Landmark moment for supply chain accountability."
        ),
        "source": "ILO / Clean Clothes Campaign / Accord Foundation / NYT",
    },

    # ════════════════════════════════════════════════════════════════════
    #  PAKISTAN (PK) — 27 facts
    # ════════════════════════════════════════════════════════════════════

    # ── Laws & Governance ──────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PK",
        "title": "Prevention of Trafficking in Persons Act 2018 — Pakistan",
        "summary": (
            "Comprehensive anti-trafficking legislation replacing fragmented "
            "earlier laws. Defines trafficking broadly including forced labour, "
            "bonded labour, and slavery. Penalties: 5-7 years imprisonment for "
            "basic trafficking, up to life imprisonment for aggravated cases "
            "(involving children, organized crime). Establishes federal and "
            "provincial anti-trafficking committees. FIA (Federal Investigation "
            "Agency) designated as lead enforcement body."
        ),
        "law": "Prevention of Trafficking in Persons Act 2018",
        "year": 2018,
        "source": "Government of Pakistan / National Assembly",
    },
    {
        "type": "law",
        "jurisdiction": "PK",
        "title": "Bonded Labour System (Abolition) Act 1992 — Pakistan",
        "summary": (
            "Abolishes bonded labour (peshgi system) in Pakistan. Cancels all "
            "existing bonded debts. District vigilance committees empowered to "
            "identify and free bonded labourers. Penalties: up to 5 years "
            "imprisonment and PKR 50,000 fine. Despite the law, bonded labour "
            "persists in brick kilns, agriculture, carpet weaving, and mining. "
            "Supreme Court has repeatedly directed enforcement. Implementation "
            "varies significantly between provinces."
        ),
        "law": "Bonded Labour System (Abolition) Act 1992",
        "year": 1992,
        "source": "Government of Pakistan / ILO Pakistan",
    },
    {
        "type": "law",
        "jurisdiction": "PK",
        "title": "Emigration Ordinance 1979 — Pakistan",
        "summary": (
            "Governs overseas employment of Pakistani workers. Establishes "
            "Bureau of Emigration and Overseas Employment (BEOE) as regulator. "
            "Requires protector of emigrants in major cities. Mandates licensing "
            "of overseas employment promoters (OEPs). Sets emigration clearance "
            "requirements for workers going to designated countries. Being "
            "modernized but still primary legal framework."
        ),
        "law": "Emigration Ordinance 1979",
        "year": 1979,
        "source": "Government of Pakistan / BEOE",
    },

    # ── Bonded Labour ──────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PK",
        "title": "Pakistan Bonded Labour in Brick Kilns — Estimated 4.5 Million",
        "summary": "Pakistan has 20,000+ brick kilns employing an estimated 4.5 million workers including families bonded through peshgi advance system.",
        "metric": "Estimated bonded labourers in brick kilns",
        "value": "4.5 million",
        "year": 2023,
        "details": (
            "Pakistan has 20,000+ brick kilns employing an estimated 4.5 million "
            "workers (including family members). Workers receive peshgi (advance) "
            "of PKR 30,000-150,000, bonding entire families. Work 12-16 hours/day "
            "in extreme heat. Piece-rate pay: PKR 600-1,000 per 1,000 bricks. "
            "End-of-season deductions perpetuate debt. Women and children work "
            "alongside men. Health impacts: lung disease, musculoskeletal injuries. "
            "Transfer of debt across generations documented."
        ),
        "source": "Global Slavery Index / ILO Pakistan / Bonded Labour Liberation Front",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Sindh Brick Kiln Bonded Labour — Pattern Analysis",
        "exploitation_type": "debt_bondage",
        "sector": "brick_kiln",
        "summary": (
            "Sindh province: estimated 2 million bonded brick kiln workers. "
            "Workers predominantly from Hindu minority (Dalit) communities and "
            "migrant Pashtuns. Peshgi system traps multigenerational families. "
            "Kiln owners act as de facto feudal lords: control housing, restrict "
            "movement, deny children schooling. Sindh High Court and Supreme "
            "Court have ordered multiple rescue operations. 2019: Supreme Court "
            "constitutional petition led to province-wide survey."
        ),
        "source": "Sindh High Court / Bonded Labour Liberation Front / SPARC",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Punjab Brick Kiln Surveys — Government Findings",
        "exploitation_type": "debt_bondage",
        "sector": "brick_kiln",
        "summary": (
            "Punjab Labour Department surveys (2014-2020) identified 8,000+ "
            "brick kilns in the province. 2.5 million estimated workers including "
            "family members. Survey findings: 88% of workers received peshgi "
            "advances, 75% could not leave due to debt, 42% had children working, "
            "67% had no access to healthcare, 93% had no written contract. "
            "Government registered kilns under Brick Kiln Workers Act but "
            "enforcement remains minimal."
        ),
        "source": "Punjab Labour Department / ILO / Pakistan Institute of Labour Education and Research",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Carpet Weaving — Child Bonded Labour",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Carpet weaving in Sindh and Punjab employs children as young as "
            "5-6 years. Children bonded through family debts to loom owners. "
            "Work 10-14 hours/day in dimly lit rooms. Develop: eye problems, "
            "respiratory disease, musculoskeletal deformities. Pakistan carpet "
            "exports declined from USD 250M (1995) to USD 80M (2020) partly "
            "due to child labour stigma. Rugmark/GoodWeave certification adopted "
            "by some exporters. ILO-IPEC programs active since 1990s."
        ),
        "source": "ILO-IPEC / GoodWeave / SPARC Pakistan",
    },

    # ── Gulf Migration ─────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "corridor": "PK-SA",
        "title": "Pakistani Workers in Saudi Arabia — Wage Theft and Exploitation",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "Saudi Arabia is Pakistan's largest labour destination (350,000+ "
            "deployed annually). Workers pay PKR 200,000-500,000 to agents. "
            "Common exploitation: contract substitution (lower salary on arrival), "
            "wage withholding (3-8 months), passport confiscation, excessive "
            "overtime without pay. Pakistan Embassy in Riyadh handles 8,000+ "
            "complaints annually. Community Welfare Attaches provide limited "
            "assistance."
        ),
        "source": "Pakistan Embassy Riyadh / BEOE / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "corridor": "PK-AE",
        "title": "Pakistani Workers in UAE — Construction and Services Exploitation",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "450,000+ Pakistani workers in UAE. Workers pay PKR 150,000-400,000 "
            "to agents. Recruitment fraud: promised AED 2,000-3,000/month, arrive "
            "to AED 800-1,500. Cramped worker accommodation (8-12 per room in "
            "labour camps). Heat exposure in construction. 200+ Pakistani worker "
            "deaths in UAE annually. Pakistan Community Welfare Fund provides "
            "limited emergency assistance."
        ),
        "source": "Pakistan Embassy Abu Dhabi / BEOE / Dawn News",
    },
    {
        "type": "contact",
        "jurisdiction": "PK",
        "title": "Bureau of Emigration and Overseas Employment (BEOE) — Pakistan",
        "summary": (
            "Government agency regulating overseas employment under Ministry of "
            "Overseas Pakistanis. Functions: registering OEPs (Overseas Employment "
            "Promoters), issuing emigration clearance, maintaining worker database, "
            "handling complaints. 2,500+ registered OEPs (licensed agencies). "
            "Issues 500,000-700,000 emigration clearances annually. Regional "
            "protector offices in: Karachi, Lahore, Islamabad, Peshawar, "
            "Multan, Quetta."
        ),
        "source": "BEOE / Ministry of Overseas Pakistanis and Human Resource Development",
    },

    # ── Historical & Special Cases ─────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "corridor": "PK-AE",
        "title": "Pakistani Child Camel Jockeys — Historical Trafficking Case",
        "exploitation_type": "physical_sexual_violence",
        "sector": "entertainment",
        "summary": (
            "1970s-2005: thousands of Pakistani (and South Asian/African) boys "
            "aged 3-10 trafficked to UAE and Gulf states as camel jockeys. Boys "
            "starved to keep weight low, physically abused, injured/killed during "
            "races. UAE banned child jockeys in 2002 (enforced 2005), replaced "
            "with robot jockeys. UNICEF repatriation program returned 1,000+ "
            "children. UAE established USD 2.7 million compensation fund. "
            "Pakistan's Ansar Burney Trust led rescue advocacy."
        ),
        "source": "UNICEF / Ansar Burney Trust / US TIP Report / Anti-Slavery International",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Coal Mining — Bonded and Hazardous Labour",
        "exploitation_type": "debt_bondage",
        "sector": "mining",
        "summary": (
            "Coal mining in Balochistan (Quetta, Duki) and Sindh (Thar) employs "
            "100,000+ workers including children. Small-scale mines: no safety "
            "equipment, frequent collapses, gas explosions. 100+ miner deaths "
            "annually. Workers from Afghan refugee communities and Hazara minority "
            "particularly vulnerable. Advance payments bond workers to mine "
            "operators. No enforcement of Mines Act in small-scale operations."
        ),
        "source": "Pakistan Institute of Labour Education and Research / HRCP / Dawn",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Agriculture — Hari (Tenant Farmer) Bonded Labour",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Hari system in Sindh: tenant farmers bonded to landlords through "
            "debt. Estimated 1.8 million haris in Sindh province. Families "
            "receive seed, fertilizer, and living expenses on credit from "
            "landlord. Share of harvest rarely covers accumulated debt. Haris "
            "cannot leave until debt cleared. Multigenerational bondage documented. "
            "Sindh Tenancy Act provides theoretical protections but landlord "
            "political influence prevents enforcement."
        ),
        "source": "Pakistan Fisherfolk Forum / HRCP / Hari Welfare Association",
    },

    # ── Supreme Court Decisions ────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PK",
        "title": "Darshan Masih v. State (1990) — Pakistan Supreme Court",
        "summary": (
            "Landmark bonded labour case. Brick kiln workers filed habeas corpus "
            "petition. Supreme Court declared bonded labour unconstitutional under "
            "Article 11 (prohibition of slavery, forced labour) and Article 3 "
            "(elimination of exploitation). Directed: all bonded debts extinguished, "
            "vigilance committees to be formed in all districts, bonded labourers "
            "to be identified and freed. Led to Bonded Labour System (Abolition) "
            "Act 1992."
        ),
        "source": "Supreme Court of Pakistan / PLD 1990 SC 513",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PK",
        "title": "Suo Motu Constitutional Petition on Bonded Labour (2019)",
        "summary": (
            "Chief Justice took suo motu notice of bonded labour in brick kilns "
            "after media reports. Court ordered: provincial governments to conduct "
            "surveys of all brick kilns, FIRs against kiln owners employing "
            "bonded labour, rehabilitation of freed families, education for "
            "children of bonded labourers. Sindh survey identified 60,000 bonded "
            "families. Punjab compliance incomplete. Periodic monitoring ongoing."
        ),
        "source": "Supreme Court of Pakistan / Dawn / HRCP",
    },
    {
        "type": "statistic",
        "jurisdiction": "PK",
        "title": "Pakistan Overseas Employment Statistics",
        "summary": "BEOE registered 832,000 workers for overseas employment in 2022; 48% to Saudi Arabia, 28% to UAE. Total diaspora: 9 million+.",
        "metric": "Annual workers deployed abroad",
        "value": "832,000",
        "year": 2022,
        "details": (
            "BEOE registered 832,000 workers for overseas employment in 2022. "
            "Top destinations: Saudi Arabia (48%), UAE (28%), Oman (8%), Qatar "
            "(5%), Bahrain (3%), Kuwait (3%), Malaysia (2%). Dominant sectors: "
            "construction (35%), drivers (15%), technicians (12%), domestic work "
            "(5%). Total Pakistani diaspora: 9 million+. Remittances: USD 31 "
            "billion (2023). Worker complaints filed with BEOE: 12,000+ annually."
        ),
        "source": "BEOE / State Bank of Pakistan / World Bank",
    },
    {
        "type": "advisory",
        "jurisdiction": "PK",
        "title": "Pakistan Pre-Departure Orientation — Gaps and Improvements",
        "summary": (
            "BEOE mandates pre-departure orientation briefing for all emigrating "
            "workers. Brief covers: employment contract, destination country laws, "
            "complaint mechanisms, emergency contacts. Gaps: briefing is cursory "
            "(30-60 minutes), conducted in Urdu (excludes Sindhi, Pashto, "
            "Balochi speakers), does not address practical survival issues. "
            "IOM Pakistan runs supplementary orientation programs. Community "
            "Welfare Attaches in embassies provide destination-specific guidance."
        ),
        "source": "BEOE / IOM Pakistan / Overseas Pakistanis Foundation",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Fishing Sector — Bonded Labour in Sindh Coast",
        "exploitation_type": "debt_bondage",
        "sector": "fishing",
        "summary": (
            "Fishing communities along Sindh coast (Karachi to Thatta) subject "
            "to bonded labour through middlemen (seth) system. Fishermen receive "
            "advances for boat fuel, nets, and family expenses. Entire catch "
            "sold to seth at below-market prices. Debt perpetuated across "
            "generations. Estimated 300,000 bonded fishermen in Sindh. Pakistan "
            "Fisherfolk Forum advocates for legal protections and cooperative "
            "models."
        ),
        "source": "Pakistan Fisherfolk Forum / ILO / PILER",
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "PK",
        "title": "Pakistan Gulf Recruitment Fraud — Organized Networks",
        "violation_type": "fraud",
        "corridor": "PK-SA",
        "summary": (
            "FIA investigations reveal organized recruitment fraud networks "
            "targeting workers from Punjab and KPK. Modus operandi: fake job "
            "offers, fraudulent visa stamps, nonexistent employers in Gulf. "
            "Victims pay PKR 200,000-500,000. FIA Anti-Human Trafficking Circle "
            "registered 3,000+ cases (2018-2023). Conviction rate below 5%. "
            "Agents flee or use aliases. Social media increasingly used for "
            "recruitment scams."
        ),
        "source": "FIA / BEOE / Pakistan Today",
    },

    # ════════════════════════════════════════════════════════════════════
    #  SRI LANKA (LK) — 27 facts
    # ════════════════════════════════════════════════════════════════════

    # ── Laws & Governance ──────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "LK",
        "title": "Sri Lanka Bureau of Foreign Employment (SLBFE)",
        "summary": (
            "Primary government agency regulating overseas employment under "
            "Ministry of Labour. Functions: licensing recruitment agencies (1,000+ "
            "licensed), pre-departure training (mandatory 21 days for domestic "
            "workers), insurance provision, complaint handling, welfare fund "
            "management. Deploys 200,000-300,000 workers annually. Operates "
            "24-hour hotline for distressed workers. Has welfare officers in "
            "major destination countries."
        ),
        "source": "SLBFE / Ministry of Labour and Foreign Employment",
    },
    {
        "type": "law",
        "jurisdiction": "LK",
        "title": "National Labour Migration Policy 2008 (revised 2023) — Sri Lanka",
        "summary": (
            "Comprehensive policy framework for labour migration governance. "
            "Pillars: governance and regulation, protection and empowerment, "
            "development impact, data and research. 2023 revision: emphasis on "
            "skills-based migration, gender-responsive protection, ethical "
            "recruitment, reintegration. Aligns with GCM (Global Compact for "
            "Migration) objectives. Implementation varies."
        ),
        "law": "National Labour Migration Policy 2008 (revised 2023)",
        "year": 2008,
        "source": "Government of Sri Lanka / MoL / ILO",
    },
    {
        "type": "regulation",
        "jurisdiction": "LK",
        "title": "Sri Lanka Family Background Report (FBR) Requirement",
        "summary": (
            "Unique requirement: women with children under 5 must obtain "
            "Family Background Report from Grama Niladhari (village officer) "
            "certifying childcare arrangements before migration approval. "
            "Controversial: seen as both protective (ensuring children cared "
            "for) and discriminatory (restricting women's mobility). No "
            "equivalent requirement for men. Women's groups and ILO advocate "
            "for gender-neutral approach. FBR process can take 2-4 weeks."
        ),
        "source": "SLBFE / ILO / CENWOR Sri Lanka",
    },
    {
        "type": "regulation",
        "jurisdiction": "LK",
        "title": "Sri Lanka Subagent Regulation Efforts",
        "summary": (
            "SLBFE attempts to regulate sub-agents (local recruiters) who "
            "operate in rural areas. 2009: sub-agent registration requirement. "
            "2016: sub-agent code of conduct. In practice: most sub-agents "
            "remain unregistered. Estimated 10,000+ active sub-agents vs 1,500 "
            "registered. Workers from rural areas (Kurunegala, Anuradhapura, "
            "Puttalam) most reliant on sub-agents. Fee overcharging common "
            "through informal channels."
        ),
        "source": "SLBFE / ILO / Sri Lanka Migrant Services Centre",
    },

    # ── Corridor Exploitation ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "corridor": "LK-SA",
        "title": "Sri Lankan Domestic Workers in Saudi Arabia — Exploitation Pattern",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Saudi Arabia is largest destination for Sri Lankan workers. 70% are "
            "women in domestic work. Documented exploitation: passport confiscation, "
            "salary withholding (3-6 months), 18-hour workdays, physical/sexual "
            "abuse, food deprivation, confinement. Sri Lankan Embassy in Riyadh "
            "operates safe house sheltering 100+ women at any time. 5,000+ "
            "complaints to embassy annually. SLBFE mandatory insurance covers "
            "medical and repatriation costs."
        ),
        "source": "Sri Lanka Embassy Riyadh / SLBFE / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "corridor": "LK-KW",
        "title": "Sri Lankan Workers in Kuwait — Abuse and Deaths",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Multiple documented deaths of Sri Lankan domestic workers in Kuwait. "
            "Pattern: physical abuse, denied medical treatment, deaths attributed "
            "to 'falling from building' (possible forced suicides). Sri Lanka "
            "temporarily banned migration to Kuwait after worker deaths. "
            "Kuwait Domestic Workers Law 68/2015 provides some protections "
            "but enforcement weak. Sri Lankan Embassy provides shelter but "
            "limited legal assistance."
        ),
        "source": "SLBFE / Sri Lanka Embassy Kuwait / Sunday Times Sri Lanka",
    },
    {
        "type": "case_study",
        "jurisdiction": "JO",
        "corridor": "LK-JO",
        "title": "Sri Lankan Garment Workers in Jordan — QIZ Exploitation",
        "exploitation_type": "excessive_overtime",
        "sector": "garment",
        "summary": (
            "10,000+ Sri Lankan women in Jordan's QIZ garment factories. Workers "
            "pay LKR 100,000-200,000 to agents. 60-72 hour weeks. Forced "
            "overtime during peak orders. Locked dormitories at night. Passport "
            "held by employer. Sexual harassment documented. Workers produce for "
            "major US brands. Better Work Jordan monitors improve conditions in "
            "some factories but violations persist in others. Return migrants "
            "report post-traumatic stress."
        ),
        "source": "Better Work Jordan / Worker Rights Consortium / SLBFE",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "corridor": "LK-QA",
        "title": "Sri Lankan Workers in Qatar — Construction and Domestic Sectors",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "Sri Lankan workers in Qatar's construction and domestic sectors. "
            "Recruitment fees: LKR 150,000-400,000 through sub-agents. Wage "
            "theft reported by 35% of return migrants. Qatar kafala reforms "
            "(2020-2021) theoretically allow job mobility but workers report "
            "difficulty exercising new rights. Minimum wage QAR 1,000 applies "
            "to Sri Lankan workers. Embassy provides consular assistance."
        ),
        "source": "Sri Lanka Embassy Doha / SLBFE / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "LB",
        "corridor": "LK-LB",
        "title": "Sri Lankan Domestic Workers in Lebanon — Kafala Crisis",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Sri Lankan women among largest domestic worker populations in "
            "Lebanon. Kafala system binds workers to employers. Documented: "
            "passport confiscation, salary non-payment (worsened by 2019 "
            "economic crisis), confinement, physical abuse. Lebanon's currency "
            "collapse meant workers paid in devalued Lebanese pounds. Hundreds "
            "of Sri Lankan workers stranded without pay during crisis. "
            "Repatriation flights organized by SLBFE and IOM."
        ),
        "source": "Human Rights Watch / SLBFE / IOM",
    },

    # ── Welfare & Insurance ────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "LK",
        "title": "SLBFE Insurance and Welfare Schemes — Sri Lanka",
        "summary": (
            "SLBFE provides mandatory insurance for all registered workers. "
            "Coverage: LKR 500,000 death benefit, LKR 250,000 disability, "
            "medical expenses, repatriation costs. Worker Welfare Fund: "
            "scholarships for workers' children (LKR 500,000+ awarded annually), "
            "housing loans for return migrants, skills training for reintegration. "
            "Funded by worker registration fees (LKR 1,500) and recruitment "
            "agency contributions. Coverage limited to registered workers "
            "(estimated 30% migrate through informal channels)."
        ),
        "source": "SLBFE / Ministry of Labour / ILO",
    },
    {
        "type": "advisory",
        "jurisdiction": "LK",
        "title": "Sri Lanka Returnee Reintegration Programs",
        "summary": (
            "Government programs for return migrants: 'Rata Viruwa' (national "
            "hero) program for dignity recognition, skills assessment and "
            "certification of overseas experience, microfinance loans through "
            "SLBFE, psychosocial support referrals. IOM AVRR program for "
            "vulnerable returnees. Gaps: limited local job matching, no "
            "systematic tracking of returnees, stigma for domestic workers "
            "who return early (assumed 'moral failure'). 65% of return migrants "
            "re-migrate within 3 years."
        ),
        "source": "SLBFE / IOM Sri Lanka / Caritas Sri Lanka SEDEC",
    },

    # ── Statistics ─────────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "LK",
        "title": "Sri Lanka Migrant Worker Deployment Statistics",
        "summary": "SLBFE registered 300,000 departures in 2022; 35% to Saudi Arabia, 70% women predominantly in domestic work.",
        "metric": "Annual workers deployed via SLBFE",
        "value": "300,000",
        "year": 2022,
        "details": (
            "SLBFE registered 300,000 departures in 2022 (up from 200,000 in "
            "2021 post-COVID recovery). Top destinations: Saudi Arabia (35%), "
            "Kuwait (18%), Qatar (12%), UAE (10%), Jordan (8%), South Korea (5%). "
            "70% women (predominantly domestic work). Male deployment: "
            "construction (45%), driving (20%), services (15%). Total Sri Lankan "
            "diaspora: 1.7 million."
        ),
        "source": "SLBFE Annual Statistical Report / Central Bank of Sri Lanka",
    },
    {
        "type": "statistic",
        "jurisdiction": "LK",
        "title": "Sri Lanka Remittances and Economic Impact",
        "summary": "Sri Lanka remittance inflows USD 5.9 billion (2023), equalling 7.5% of GDP; critical foreign exchange source especially during 2022 economic crisis.",
        "metric": "Annual remittance inflows",
        "value": "USD 5.9 billion",
        "year": 2023,
        "details": (
            "Remittance inflows: USD 5.9 billion (2023). Critical foreign "
            "exchange source (especially during 2022 economic crisis). "
            "Remittances = 7.5% of GDP. 1.2 million households depend on "
            "remittances. During 2022 crisis, remittances provided vital "
            "household lifeline while formal economy collapsed. Saudi Arabia "
            "and Kuwait are top remittance sources."
        ),
        "source": "Central Bank of Sri Lanka / World Bank / SLBFE",
    },
    {
        "type": "statistic",
        "jurisdiction": "LK",
        "title": "Sri Lankan Migrant Worker Complaints Data",
        "summary": "SLBFE received 12,000+ complaints in 2022; top issues: salary non-payment (35%), contract violation (20%), physical abuse (15%).",
        "metric": "Annual complaints received by SLBFE",
        "value": "12,000+",
        "year": 2022,
        "details": (
            "SLBFE received 12,000+ complaints in 2022. Top complaint types: "
            "salary non-payment (35%), contract violation (20%), physical abuse "
            "(15%), sexual harassment (10%), passport confiscation (8%), "
            "deception about job/salary (7%). 60% of complaints from domestic "
            "workers. Resolution rate: 45% within 6 months. Remaining cases "
            "referred to legal proceedings (slow, often abandoned)."
        ),
        "source": "SLBFE Complaints Division / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lanka Economic Crisis (2022) — Migration Surge",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "multiple",
        "summary": (
            "2022 economic crisis (forex depletion, inflation 70%+, fuel/food "
            "shortages) drove unprecedented migration surge. SLBFE registrations "
            "doubled. Desperate workers accepted below-standard contracts. "
            "Sub-agents exploited urgency with inflated fees. Reports of workers "
            "departing without SLBFE registration to avoid delays. Irregular "
            "migration to Italy and other European destinations via agents "
            "charging LKR 1-3 million increased."
        ),
        "source": "SLBFE / Central Bank of Sri Lanka / IOM",
    },
    {
        "type": "advisory",
        "jurisdiction": "LK",
        "title": "Sri Lanka Pre-Departure Training — 21-Day Program",
        "summary": (
            "SLBFE mandates 21-day pre-departure training for domestic workers "
            "and 5-day orientation for other categories. Domestic worker training "
            "covers: cooking, cleaning, childcare, employer country culture, "
            "language basics (Arabic), rights and complaint mechanisms, financial "
            "literacy. Conducted at 20+ SLBFE-accredited training centres. "
            "Criticized for: insufficient time, inadequate language training, "
            "does not address exploitation scenarios. ILO and HELVETAS support "
            "curriculum improvements."
        ),
        "source": "SLBFE / ILO / HELVETAS Sri Lanka",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lankan Male Domestic Workers in Gulf — Emerging Trend",
        "exploitation_type": "deception",
        "sector": "domestic_work",
        "summary": (
            "Growing trend: Sri Lankan men recruited as 'houseboys,' drivers, "
            "and gardeners for Gulf households. Recruited as skilled workers but "
            "deployed as domestic workers (lower pay, no labour law protection). "
            "Contract substitution common. Workers isolated in households with "
            "limited freedom. SLBFE complaints from male domestic workers "
            "increasing 15% annually since 2019."
        ),
        "source": "SLBFE / ILO / Law and Society Trust Sri Lanka",
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "LK",
        "title": "Sri Lanka Recruitment Fee Overcharging — Pattern Analysis",
        "violation_type": "excessive_fees",
        "summary": (
            "SLBFE sets maximum recruitment charges. Government-to-government "
            "channels (e.g., Korea EPS): LKR 15,000. Private agency channels: "
            "LKR 25,000-50,000 (official maximum varies by destination). "
            "Actual fees paid: LKR 100,000-400,000 through sub-agents. "
            "Workers from Kurunegala, Anuradhapura, and Puttalam districts "
            "pay highest fees. SLBFE investigated 500+ overcharging complaints "
            "(2020-2023). Agency licence suspensions: 50+ per year."
        ),
        "source": "SLBFE / ILO / Migrant Services Centre",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "corridor": "LK-KR",
        "title": "Sri Lankan Workers in South Korea EPS — Best Practice Corridor",
        "exploitation_type": "none",
        "sector": "manufacturing",
        "summary": (
            "South Korea EPS is considered a best-practice model for Sri Lankan "
            "workers. Government-managed recruitment: SLBFE to HRD Korea. Total "
            "cost: LKR 15,000 (no private brokers). Korean language test (EPS-TOPIK) "
            "required. Workers receive: Korean labour law protection, minimum "
            "wage, health insurance, workplace accident insurance. 20,000+ "
            "Sri Lankan workers in Korea. Challenges: language barrier, cultural "
            "adjustment, some workplace discrimination."
        ),
        "source": "HRD Korea / SLBFE / ILO",
    },
    {
        "type": "advisory",
        "jurisdiction": "LK",
        "title": "Sri Lanka Migration and Gender — Women's Dominance in Migration",
        "summary": (
            "Unique among South Asian countries: 70% of Sri Lanka's migrant "
            "worker outflow is female (predominantly domestic work). This "
            "pattern creates specific vulnerabilities: isolation in employer "
            "households, limited access to complaint mechanisms, sexual "
            "harassment/abuse, family separation (children left with relatives). "
            "Also creates unique impacts: women as primary breadwinners, "
            "changing gender dynamics in sending communities, 'left-behind' "
            "children's welfare concerns. ILO and UNICEF studies on impact."
        ),
        "source": "SLBFE / ILO / UNICEF Sri Lanka / CENWOR",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lanka — Domestic Worker Death Cases in Middle East",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Multiple high-profile cases of Sri Lankan domestic worker deaths "
            "in Middle East. Cases include: Rizana Nafeek (executed in Saudi "
            "Arabia 2013 for death of infant — widespread belief of wrongful "
            "conviction), multiple 'falling from building' deaths in Kuwait "
            "and Saudi Arabia (suspected forced suicides). Each case triggers "
            "national outrage and temporary deployment bans. SLBFE death "
            "compensation claims: 50-80 annually."
        ),
        "source": "SLBFE / Sunday Times Sri Lanka / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lanka Fishing Crew on Foreign Vessels — Exploitation",
        "exploitation_type": "restriction_of_movement",
        "sector": "fishing",
        "summary": (
            "Sri Lankan fishermen recruited for foreign-flagged fishing vessels "
            "operating in Indian Ocean and beyond. Recruited through informal "
            "agents in southern coastal areas (Tangalle, Hambantota). Confined "
            "to vessels for months, paid share of catch (often minimal). No "
            "safety equipment. ILO C188 (Work in Fishing Convention) not ratified "
            "by Sri Lanka. IOM assists abandoned crew. Cases of Sri Lankan crew "
            "stranded in Seychelles, Madagascar, and Oman documented."
        ),
        "source": "IOM / National Fisheries Solidarity / ILO",
    },

    # ════════════════════════════════════════════════════════════════════
    #  CROSS-CUTTING SOUTH ASIA — 5 facts
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "South Asia — Largest Source of Migrant Workers to Gulf States",
        "summary": "India, Bangladesh, Pakistan, Nepal, Sri Lanka together send 25+ million workers to GCC states, constituting 60-70% of private-sector workforce.",
        "metric": "South Asian workers in GCC countries",
        "value": "25+ million",
        "year": 2023,
        "details": (
            "India, Bangladesh, Pakistan, Nepal, Sri Lanka together send 25+ "
            "million workers to GCC states (Saudi Arabia, UAE, Qatar, Kuwait, "
            "Oman, Bahrain). South Asian workers constitute 60-70% of GCC "
            "private-sector workforce. Combined remittances from GCC to South "
            "Asia: USD 80+ billion annually. Shared vulnerabilities: kafala "
            "system, recruitment fee debt, passport confiscation, wage theft."
        ),
        "source": "ILO / World Bank / Gulf Labour Markets and Migration (GLMM)",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Colombo Process — South Asian Labour Migration Governance",
        "summary": (
            "Regional consultative process for Asian labour-sending countries. "
            "Members include India, Bangladesh, Nepal, Pakistan, Sri Lanka, "
            "Philippines, Indonesia, and others. Meetings: biennial ministerial "
            "consultations and thematic workshops. Focus: harmonizing recruitment "
            "standards, coordinated bargaining with destination countries, data "
            "sharing. Limitations: non-binding, no enforcement mechanism, "
            "competition among source countries undermines collective bargaining."
        ),
        "source": "Colombo Process Secretariat / IOM / ILO",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Abu Dhabi Dialogue — Source-Destination Country Cooperation",
        "summary": (
            "Inter-governmental consultative forum linking Asian labour-sending "
            "countries (India, Bangladesh, Nepal, Pakistan, Sri Lanka, etc.) with "
            "Gulf receiving countries (UAE, Saudi Arabia, Qatar, Kuwait, Oman, "
            "Bahrain, Malaysia). Established 2008. Focus: ethical recruitment, "
            "skills recognition, labour market information exchange. Limitations: "
            "voluntary commitments, no enforcement, power asymmetry between "
            "sending and receiving countries."
        ),
        "source": "Abu Dhabi Dialogue Secretariat / IOM / ILO",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "South Asian Recruitment Fee Burden — Comparative Data",
        "summary": "South Asian workers pay equivalent of 4-8 months salary in recruitment fees; highest on BD-MY corridor (8 months).",
        "metric": "Average recruitment cost as months of salary",
        "value": "4-8 months",
        "year": 2023,
        "details": (
            "ILO comparative data: South Asian workers pay equivalent of 4-8 "
            "months salary in recruitment fees. Highest: Bangladesh-Malaysia "
            "(8 months), Nepal-Qatar (6 months), India-Saudi Arabia (5 months), "
            "Pakistan-UAE (4 months), Sri Lanka-Kuwait (4 months). ILO/IOM "
            "Dhaka Principles and Fair Recruitment Initiative call for zero "
            "worker-borne fees. Employer Pays Principle remains aspirational."
        ),
        "source": "ILO / World Bank / Knomad / Fair Recruitment Initiative",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "South Asian Diaspora — Shared Vulnerability Patterns",
        "summary": (
            "Common exploitation patterns across South Asian corridors: "
            "(1) Multi-layered recruitment with informal sub-agents inflating "
            "fees, (2) debt-financed migration with high-interest loans from "
            "moneylenders, (3) contract substitution upon arrival, (4) kafala-"
            "tied employment limiting mobility, (5) wage theft enabled by "
            "electronic payment gaps, (6) passport confiscation despite legal "
            "prohibition, (7) inadequate consular protection, (8) return "
            "migration with debt and no savings."
        ),
        "source": "ILO / Migrant Forum in Asia / Open Society Foundations",
    },

    # ════════════════════════════════════════════════════════════════════
    #  ADDITIONAL FACTS — reaching 150+ total
    # ════════════════════════════════════════════════════════════════════

    # ── India Additional ───────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "Child Labour (Prohibition and Regulation) Amendment Act 2016 — India",
        "summary": (
            "Amended 1986 Act to impose complete ban on employment of children "
            "under 14 in all occupations and processes. Adolescents (14-18) "
            "prohibited from hazardous occupations. Penalties increased: "
            "imprisonment 6 months to 2 years, fine INR 20,000-50,000. "
            "Criticism: allows children to work in 'family enterprises' "
            "(loophole exploited in home-based garment, bidi, carpet work)."
        ),
        "law": "Child Labour Amendment Act 2016",
        "year": 2016,
        "source": "Government of India / Ministry of Labour and Employment / CRY",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Chhattisgarh-Telangana Rice Mill Bonded Labour",
        "exploitation_type": "debt_bondage",
        "sector": "food_processing",
        "summary": (
            "Adivasi families from Chhattisgarh recruited by labour contractors "
            "for rice mills in Telangana. Advance payments of INR 10,000-25,000 "
            "bond families for 6-8 month seasons. Workers confined to mill "
            "premises. Piece-rate wages leave families in perpetual debt. "
            "Children work alongside adults. National Human Rights Commission "
            "rescue operations freed 1,500+ workers (2018-2023)."
        ),
        "source": "NHRC / ActionAid / Anti-Slavery International",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "India Stone Quarry Bonded Labour — Rajasthan and Tamil Nadu",
        "exploitation_type": "debt_bondage",
        "sector": "mining",
        "summary": (
            "Bonded labour in stone quarries of Rajasthan (sandstone) and "
            "Tamil Nadu (granite). Workers from Dalit communities receive "
            "advances and are trapped in debt cycles. Silicosis epidemic: "
            "average life expectancy of quarry workers 40-45 years. 10,000+ "
            "silicosis deaths estimated annually. Workers receive INR 200-300/"
            "day. Mines and Minerals Act enforcement minimal in small quarries."
        ),
        "source": "Occupational Health and Safety Centre / Mine Labour Protection Campaign / ILO",
    },
    {
        "type": "regulation",
        "jurisdiction": "IN",
        "title": "e-Shram Portal — India Unorganized Worker Registration",
        "summary": (
            "National database for unorganised workers launched August 2021. "
            "290+ million workers registered by 2024 including migrant workers. "
            "Provides: Aadhaar-linked identity, accidental insurance (INR 2 lakh), "
            "portable benefits across states. Aims to address gap exposed during "
            "COVID-19 when millions of internal migrants had no identification or "
            "welfare access. Linked to One Nation One Ration Card for PDS portability."
        ),
        "source": "Ministry of Labour and Employment / e-Shram portal",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "India Garment Sector — Bangalore Export Units",
        "exploitation_type": "excessive_overtime",
        "sector": "garment",
        "summary": (
            "800,000+ garment workers in Bangalore (80% women migrants from "
            "north Karnataka and Tamil Nadu). Documented: forced overtime during "
            "peak orders, verbal abuse, sexual harassment by supervisors, wages "
            "at minimum or below, no crche facilities despite legal mandate. "
            "Workers producing for major global brands. Garment Labour Union and "
            "Workers Rights Consortium campaigns for improved conditions."
        ),
        "source": "Garment Labour Union / Workers Rights Consortium / Asia Floor Wage Alliance",
    },
    {
        "type": "advisory",
        "jurisdiction": "IN",
        "title": "India Anti-Human Trafficking Units (AHTUs)",
        "summary": (
            "Specialised police units established in 330+ districts across India. "
            "Functions: investigating trafficking cases, rescuing victims, "
            "coordinating with NHRC and NGOs. Funded by Ministry of Home Affairs. "
            "Challenges: understaffing, limited training, low conviction rates "
            "(below 10% for trafficking cases). UNODC and IJM provide capacity "
            "building. AHTUs handle both cross-border and internal trafficking."
        ),
        "source": "Ministry of Home Affairs / UNODC India / IJM",
    },

    # ── Nepal Additional ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal Domestic Workers — Unregulated Internal Labour",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "domestic_work",
        "summary": (
            "Estimated 200,000+ child and adult domestic workers within Nepal. "
            "Children as young as 8-10 sent from rural areas to urban households "
            "as 'kamlari' (bonded domestic servants) in Terai or informal "
            "domestic workers in Kathmandu. No labour law coverage for domestic "
            "workers. ILO C189 not ratified. Child domestic work considered "
            "'cultural practice' by some families. National Child Concern Centre "
            "and CWISH advocate for legal protections."
        ),
        "source": "CWISH / ILO Nepal / National Child Concern Centre",
    },
    {
        "type": "regulation",
        "jurisdiction": "NP",
        "title": "Nepal Labour Act 2017 — Migrant Worker Protections",
        "summary": (
            "Comprehensive labour reform replacing 1992 Act. Relevant provisions: "
            "minimum wage NPR 17,300/month (2023-24), prohibition of forced "
            "labour, mandatory written contracts, social security fund (employer "
            "and employee contributions). Applies to domestic workers for first "
            "time. Enforcement gaps: 80% of Nepal's workforce in informal sector. "
            "Labour inspectors: fewer than 50 for entire country."
        ),
        "source": "Government of Nepal / MoLESS / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal Entertainment Sector — Internal Trafficking",
        "exploitation_type": "physical_sexual_violence",
        "sector": "entertainment",
        "summary": (
            "Trafficking of women and girls from rural Nepal into cabin "
            "restaurants, dance bars, and massage parlours in Kathmandu Valley. "
            "Recruitment through false promises of waitressing or hotel work. "
            "Debt bondage, forced sex work, confinement. Estimated 15,000+ "
            "women in vulnerable entertainment sector employment. Maiti Nepal "
            "and Shakti Samuha (survivor-led organization) provide rescue and "
            "rehabilitation. National Minimum Standards for victim care adopted."
        ),
        "source": "Maiti Nepal / Shakti Samuha / NHRC Nepal",
    },
    {
        "type": "advisory",
        "jurisdiction": "NP",
        "title": "Nepal Pre-Departure Orientation Training (PDOT)",
        "summary": (
            "Mandatory 2-day orientation for all workers departing through "
            "formal channels. Covers: destination country culture and laws, "
            "employment contract review, complaint mechanisms, health and "
            "safety, financial literacy. Conducted by DoFE-accredited training "
            "centres (50+). Gaps: duration too short, generic content not "
            "country-specific, language (Nepali only, excludes ethnic language "
            "speakers), does not prepare workers for exploitation scenarios."
        ),
        "source": "DoFE Nepal / ILO / Helvetas Nepal",
    },
    {
        "type": "contact",
        "jurisdiction": "NP",
        "title": "Pourakhi Nepal — Migrant Women's Organisation",
        "summary": (
            "Leading NGO for women migrant workers' rights in Nepal. "
            "Founded by return migrant women. Services: pre-departure counselling, "
            "legal aid for returnees, reintegration support, policy advocacy. "
            "Operates shelters for returned survivors of exploitation. Campaigns "
            "against gender-discriminatory migration bans. Conducted landmark "
            "studies on women's migration experiences. Partner of ILO, UN Women, "
            "and IOM programs."
        ),
        "source": "Pourakhi Nepal / ILO / UN Women",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal Carpet Sector — Child Labour and Trafficking",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Nepal's carpet industry (once 60% of exports) employed children "
            "from rural areas, some trafficked. ILO-IPEC and GoodWeave programs "
            "reduced child labour from estimated 50,000 (1990s) to 5,000 (2020s). "
            "Remaining issues: children in home-based looms, bonded families in "
            "factory hostels. Export value declined from USD 200M to USD 60M "
            "partly due to child labour stigma."
        ),
        "source": "GoodWeave Nepal / ILO-IPEC / Nepal Rugmark Foundation",
    },
    {
        "type": "statistic",
        "jurisdiction": "NP",
        "title": "Nepal Labour Migration — Gender Breakdown",
        "summary": "Women constitute 5-7% of formal labour permits but an estimated 20% of actual migration through informal channels via India.",
        "metric": "Female share of formal labour migration",
        "value": "5-7%",
        "year": 2022,
        "details": (
            "Women constitute only 5-7% of DoFE-issued labour permits due to "
            "age-based restrictions and bans on domestic work migration to several "
            "countries. Estimated 20% of actual migration is female when including "
            "irregular channels through India. Women predominantly in domestic "
            "work, hospitality, and care sectors."
        ),
        "source": "DoFE Nepal / ILO / UN Women Nepal",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal COVID-19 Return Migration — Mass Repatriation",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "multiple",
        "summary": (
            "COVID-19 triggered return of 500,000+ Nepali workers from Gulf "
            "states and Malaysia (2020-2021). Many returned with unpaid wages, "
            "outstanding debt, and no savings. Government chartered repatriation "
            "flights but workers bore costs. Returnees faced: no unemployment "
            "benefits, difficulty accessing foreign employment compensation, "
            "re-migration pressure from debt. IOM provided emergency assistance."
        ),
        "source": "DoFE Nepal / IOM / Pravasi Nepali Coordination Committee",
    },
    {
        "type": "advisory",
        "jurisdiction": "NP",
        "title": "Nepal Migrant Worker Suicide Crisis",
        "summary": (
            "Alarming suicide rate among Nepali migrant workers abroad and "
            "returnees. Foreign Employment Board data: suicide accounts for "
            "8-10% of documented migrant deaths abroad. Returnee suicide linked "
            "to: failed migration (debt with no earnings), exploitation trauma, "
            "social stigma, family pressure. Mental health services virtually "
            "absent for migrant workers. TPO Nepal and CMC provide limited "
            "psychosocial support."
        ),
        "source": "Foreign Employment Board / TPO Nepal / CESLAM",
    },
    {
        "type": "regulation",
        "jurisdiction": "NP",
        "title": "Nepal Foreign Employment Compensation Mechanism",
        "summary": (
            "Foreign Employment Board provides compensation funded by mandatory "
            "worker contributions (NPR 1,500 per departure). Compensation: "
            "NPR 1,500,000 for death, NPR 500,000-1,500,000 for disability, "
            "medical expenses, repatriation. Claims process: 12-18 months "
            "average. Required documents (death certificate, employment proof) "
            "difficult to obtain from Gulf employers. Only 60% of eligible "
            "claims successfully processed."
        ),
        "source": "Foreign Employment Board / DoFE Nepal / ILO",
    },

    # ── Bangladesh Additional ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Tea Garden Workers — Bonded Labour Legacy",
        "exploitation_type": "isolation",
        "sector": "agriculture",
        "summary": (
            "360,000+ tea workers in Sylhet and Chittagong divisions. Descended "
            "from Adivasi communities brought by British during colonial era. "
            "Lowest wages in Bangladesh: BDT 170/day (2023). Housing, healthcare, "
            "and education tied to plantation employment. Workers cannot easily "
            "leave as all services depend on estate. Tea Workers Union demands "
            "minimum wage parity with garment sector."
        ),
        "source": "Bangladesh Tea Workers Union / Solidarity Center / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladeshi Workers in Libya — Trafficking and Exploitation",
        "exploitation_type": "multiple",
        "sector": "construction",
        "summary": (
            "Thousands of Bangladeshi workers trafficked to Libya (2017-2023) "
            "through irregular channels. Workers pay BDT 400,000-600,000 to "
            "agents promising European transit. Arrive in Libya: passport "
            "confiscated, forced to work in construction without pay, detained "
            "in migrant centres, ransom demands to families. Bangladesh Embassy "
            "repatriated 5,000+ workers (2018-2023). IOM assisted evacuation."
        ),
        "source": "IOM / Bangladesh Embassy Tripoli / BMET",
    },
    {
        "type": "regulation",
        "jurisdiction": "BD",
        "title": "Bangladesh Smart Card for Migrant Workers",
        "summary": (
            "Government-issued pre-departure smart card for all registered "
            "migrant workers since 2016. Contains: biometric data, employment "
            "contract details, employer information, insurance coverage. "
            "Linked to BMET database. Aims to: track worker deployment, "
            "verify employment terms, facilitate return and reintegration. "
            "Coverage: estimated 60% of departing workers. Informal migrants "
            "excluded."
        ),
        "source": "BMET / MoEWOE / IOM Bangladesh",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Tannery Workers — Hazaribagh and Savar",
        "exploitation_type": "abusive_working_conditions",
        "sector": "manufacturing",
        "summary": (
            "Leather tanning industry in Hazaribagh (relocated to Savar 2017). "
            "15,000+ workers exposed to chromium, sulfuric acid, and other "
            "chemicals without protective equipment. Child labour documented. "
            "Average life expectancy of tannery workers: 50 years. Workers earn "
            "BDT 8,000-12,000/month. Exported leather enters global supply "
            "chains. Relocation to Savar CETP expected to improve conditions but "
            "worker protections remain inadequate."
        ),
        "source": "Human Rights Watch / FIDH / Solidarity Center",
    },
    {
        "type": "advisory",
        "jurisdiction": "BD",
        "title": "Bangladesh Probashi Kallyan Bank — Migrant Worker Financial Services",
        "summary": (
            "State-owned bank established 2011 specifically for migrant workers. "
            "Services: pre-departure loans (BDT 300,000 max at subsidised rates), "
            "remittance services, savings products, returnee entrepreneur loans. "
            "29 branches nationwide. Challenges: limited outreach to rural areas "
            "where most migrants originate, bureaucratic loan process, workers "
            "prefer faster informal moneylenders despite higher interest rates."
        ),
        "source": "Probashi Kallyan Bank / MoEWOE / Bangladesh Bank",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh COVID-19 Return Migration Crisis",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "multiple",
        "summary": (
            "COVID-19 pandemic caused return of 400,000+ Bangladeshi workers "
            "from Gulf states and Malaysia (2020-2021). Many returned with unpaid "
            "wages and outstanding recruitment debts. WEWB provided emergency "
            "assistance (BDT 5,000 per worker — criticized as inadequate). "
            "Re-migration surged in 2022 with workers accepting worse terms due "
            "to desperation. Moneylenders pressured families of indebted returnees."
        ),
        "source": "BMET / BRAC Migration Program / IOM Bangladesh",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Dried Fish Processing — Child and Bonded Labour",
        "exploitation_type": "debt_bondage",
        "sector": "food_processing",
        "summary": (
            "Dried fish (shutki) processing in Cox's Bazar, Chittagong, and "
            "Sundarbans coast employs thousands of workers including children. "
            "Workers from landless families bonded through advances from "
            "mahajans (moneylenders/traders). Women and children sort, salt, "
            "and dry fish for 10-14 hours/day. Chemical exposure (pesticides "
            "used for preservation). Earnings: BDT 150-300/day. Largely "
            "unmonitored by labour authorities."
        ),
        "source": "Solidarity Center / BRAC / Coast Trust",
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "BD",
        "title": "Bangladesh Social Media Recruitment Scams",
        "violation_type": "fraud",
        "corridor": "BD-MY",
        "summary": (
            "Growing trend: fraudulent recruitment via Facebook, TikTok, and "
            "WhatsApp. Fake agents post Gulf and Malaysia job offers on social "
            "media targeting rural youth. Victims pay BDT 100,000-300,000 "
            "through bKash/Nagad mobile money. Agent disappears or provides "
            "fake visa. CID Cyber Police registered 1,000+ cases (2021-2023). "
            "BMET unable to regulate social media recruitment."
        ),
        "source": "BMET / CID Cyber Police / Daily Star Bangladesh",
    },
    {
        "type": "regulation",
        "jurisdiction": "BD",
        "title": "Bangladesh Mandatory Pre-Departure Briefing",
        "summary": (
            "BMET mandates pre-departure briefing for all registered workers. "
            "30-minute session at BMET office covers: destination country basics, "
            "contract review, emergency contacts, complaint mechanisms. "
            "Supplemented by Technical Training Centres (TTCs) for skilled "
            "workers. Criticized for: insufficient duration, no destination-"
            "specific content, language barriers (Bengali only, excludes "
            "Chittagong Hill Tracts minorities), no practical exploitation "
            "scenario preparation."
        ),
        "source": "BMET / ILO / RMMRU",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladeshi Migrant Workers in Saudi Poultry Farms",
        "exploitation_type": "withholding_wages",
        "sector": "agriculture",
        "corridor": "BD-SA",
        "summary": (
            "Bangladeshi workers recruited for Saudi poultry farms. Pay "
            "BDT 250,000-400,000 to agents. Arrive to remote farms with "
            "limited mobility. Salary SAR 800-1,000/month (less than promised). "
            "Wage withholding for 2-4 months common. Workers housed on farm "
            "premises with no access to town. Complaints difficult due to "
            "isolation and language barriers. Bangladesh Embassy has limited "
            "reach beyond major cities."
        ),
        "source": "Bangladesh Embassy Riyadh / BRAC / Ovibashi Karmi Unnayan Program",
    },
    {
        "type": "advisory",
        "jurisdiction": "BD",
        "title": "Bangladesh BRAC Migration Program — Community Awareness",
        "summary": (
            "BRAC's migration program provides pre-departure orientation "
            "in 64 districts, legal aid for returnees, community awareness "
            "on safe migration. Reaches 500,000+ potential migrants annually "
            "through community sessions. Services: recruitment agency verification, "
            "contract review, financial literacy, returning migrant support "
            "groups. One of the largest non-governmental migration support "
            "programs in South Asia. Funded by SDC, DFID, and ILO."
        ),
        "source": "BRAC Migration Program / ILO / SDC",
    },

    # ── Pakistan Additional ────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PK",
        "title": "Punjab Restriction on Employment of Children Act 2016",
        "summary": (
            "Punjab province-specific legislation prohibiting employment of "
            "children under 14 in all occupations. Adolescents (14-18) "
            "prohibited from hazardous work. Penalties: PKR 50,000 fine and "
            "6 months imprisonment. Establishes child labour inspection units. "
            "Important because Punjab has highest concentration of child labour "
            "in brick kilns and carpet weaving. Enforcement remains weak due to "
            "limited inspectors and political interference."
        ),
        "law": "Punjab Restriction on Employment of Children Act 2016",
        "year": 2016,
        "source": "Punjab Assembly / ILO Pakistan / SPARC",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistani Workers in Oman — Contract Substitution",
        "exploitation_type": "deception",
        "sector": "services",
        "corridor": "PK-OM",
        "summary": (
            "Pakistani workers recruited for hospitality and retail jobs in Oman. "
            "Pay PKR 150,000-300,000 to agents for promised OMR 200-300/month "
            "positions. Arrive to find lower salary, different employer, longer "
            "hours. Passports confiscated. Workers file complaints with Pakistan "
            "Embassy but resolution slow. Protector of Emigrants receives 1,000+ "
            "Oman-related complaints annually."
        ),
        "source": "Pakistan Embassy Muscat / BEOE / Express Tribune",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Glass Bangle Industry — Child Labour in Hyderabad",
        "exploitation_type": "abusive_working_conditions",
        "sector": "manufacturing",
        "summary": (
            "Glass bangle manufacturing in Hyderabad, Sindh employs thousands "
            "of children (some as young as 8). Children work near furnaces at "
            "1,200-1,500C temperatures. Burns, eye damage, respiratory illness "
            "common. Families bonded through advances. Earnings: PKR 200-400/"
            "day per family. Product primarily for domestic market. Limited "
            "NGO intervention. Government inspections rare."
        ),
        "source": "SPARC / PILER / ILO Pakistan",
    },
    {
        "type": "advisory",
        "jurisdiction": "PK",
        "title": "Overseas Pakistanis Foundation (OPF) — Welfare Services",
        "summary": (
            "Government body providing welfare services for overseas Pakistanis. "
            "Services: housing schemes for migrants, educational scholarships "
            "for workers' children, OPF schools (21 schools nationwide), legal "
            "aid, old-age benefits. Funded by worker registration fees and "
            "government allocation. Criticism: services reach small fraction of "
            "9+ million diaspora, housing schemes delayed, limited presence in "
            "destination countries."
        ),
        "source": "Overseas Pakistanis Foundation / MoOP&HRD",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Domestic Workers — Internal Exploitation",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Estimated 12 million domestic workers in Pakistan (ILO), "
            "predominantly women and girls. No specific domestic worker "
            "legislation at federal level. Children as young as 8-10 employed. "
            "Documented: physical and sexual abuse, confinement, 18-hour "
            "workdays, salary non-payment. High-profile cases: Tayyaba torture "
            "case (2016, Islamabad judge's household). Punjab Domestic Workers "
            "Act 2019 provides limited protections but enforcement is minimal."
        ),
        "source": "ILO Pakistan / PILER / Human Rights Commission of Pakistan",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Workers in Bahrain — Construction Exploitation",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "corridor": "PK-BH",
        "summary": (
            "Pakistani workers in Bahrain construction sector. Workers pay "
            "PKR 100,000-250,000 to agents. Wage withholding, cramped labour "
            "camps, 12-hour shifts in extreme heat. Bahrain reformed sponsorship "
            "system (2009, LMRA flexi-permit) but workers report ongoing "
            "exploitation. Pakistan Embassy handles 500+ complaints annually. "
            "Protector of Emigrants Karachi processes most Bahrain-bound workers."
        ),
        "source": "Pakistan Embassy Bahrain / BEOE / ILO",
    },

    # ── Sri Lanka Additional ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lankan Workers in Maldives — Exploitation in Tourism Sector",
        "exploitation_type": "withholding_wages",
        "sector": "hospitality",
        "corridor": "LK-MV",
        "summary": (
            "Growing corridor: Sri Lankan workers in Maldives tourism and "
            "construction sectors. Workers pay LKR 100,000-200,000 to agents. "
            "Resort island isolation limits mobility and access to complaints "
            "mechanisms. Wage withholding and contract substitution documented. "
            "Workers on smaller islands have no access to embassy or legal "
            "services. SLBFE has limited monitoring capacity for Maldives."
        ),
        "source": "SLBFE / IOM / Sunday Observer Sri Lanka",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lanka — Left-Behind Children of Migrant Mothers",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "domestic_work",
        "summary": (
            "Estimated 500,000+ children in Sri Lanka with mothers working "
            "abroad (primarily Gulf domestic work). Studies document: increased "
            "school dropout rates, psychological distress, abuse by caregivers "
            "(relatives), child labour to supplement household income. UNICEF "
            "and ILO studies recommend: improved childcare systems, regular "
            "communication support, social worker monitoring. Family Background "
            "Report (FBR) intended to address but creates barrier to women's "
            "mobility."
        ),
        "source": "UNICEF Sri Lanka / ILO / CENWOR / Save the Children",
    },
    {
        "type": "regulation",
        "jurisdiction": "LK",
        "title": "Sri Lanka Minimum Age for Domestic Worker Migration",
        "summary": (
            "SLBFE raised minimum age for women migrating for domestic work "
            "from 18 to 21 in 2007, then to 23 in 2013, with additional "
            "restrictions for women under 25. For Saudi Arabia: minimum age "
            "25. Rationale: younger women more vulnerable to exploitation. "
            "Criticism: age restriction is discriminatory and pushes women "
            "into irregular migration channels. ILO recommends protection-based "
            "approach rather than age-based bans."
        ),
        "source": "SLBFE / ILO / CENWOR Sri Lanka",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "corridor": "LK-IT",
        "title": "Sri Lankan Irregular Migration to Italy — Exploitation",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Growing irregular migration from Sri Lanka to Italy (especially "
            "post-2022 economic crisis). Workers pay LKR 1-3 million to smugglers "
            "for boat/overland journeys. Arrive as undocumented workers in "
            "agricultural sector (Calabria, Puglia). Wage theft, substandard "
            "housing, employer exploitation. Undocumented status prevents "
            "access to legal protection. IOM and Caritas provide limited "
            "assistance. Some regularised through periodic amnesties."
        ),
        "source": "IOM / UNHCR / Caritas Italiana / SLBFE",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lanka Plantation Sector — Internal Exploitation",
        "exploitation_type": "isolation",
        "sector": "agriculture",
        "summary": (
            "400,000+ workers on Sri Lanka's tea, rubber, and coconut plantations. "
            "Predominantly Tamil community descended from colonial-era Indian "
            "labourers. Lowest-paid workers in formal sector: LKR 1,000/day "
            "(2023). Housing tied to employment (line rooms). Limited access to "
            "education, healthcare, clean water. Plantation Human Development "
            "Trust (PHDT) provides some services. Workers cannot easily leave "
            "as all services depend on estate employment."
        ),
        "source": "Plantation Human Development Trust / ILO / Oxfam",
    },

    # ── Cross-Cutting Additional ───────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Fair Recruitment Initiative — South Asia Engagement",
        "summary": (
            "ILO's Fair Recruitment Initiative (FRI) operates in all five South "
            "Asian countries. Components: promoting ethical recruitment through "
            "government engagement, developing recruitment cost surveys (Global "
            "SDG indicator 10.7.1), building capacity of recruitment agencies, "
            "empowering workers through information. South Asia-specific: "
            "addressing dalal/sub-agent networks, high-cost corridors to Gulf, "
            "and moneylender debt financing of migration."
        ),
        "source": "ILO Fair Recruitment Initiative / SDG Indicator 10.7.1",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "SAARC Convention on Preventing Trafficking — South Asian Framework",
        "summary": (
            "SAARC Convention on Preventing and Combating Trafficking in Women "
            "and Children for Prostitution (2002). Ratified by all SAARC members "
            "including India, Nepal, Bangladesh, Pakistan, Sri Lanka. Requires: "
            "criminalization of trafficking, mutual legal assistance, victim "
            "protection. Limitations: narrow scope (only women and children, "
            "only for prostitution), no enforcement mechanism, no secretariat "
            "for monitoring. SAARC institutional weakness limits implementation."
        ),
        "source": "SAARC Secretariat / UNODC / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "South Asian Workers in Online Scam Compounds — Emerging Threat",
        "exploitation_type": "restriction_of_movement",
        "sector": "cybercrime",
        "summary": (
            "Emerging trend: South Asian workers (especially from India, Nepal, "
            "Bangladesh) recruited for 'IT jobs' in Myanmar, Cambodia, Laos. "
            "Arrive to find online scam compounds. Passports confiscated, forced "
            "to conduct cryptocurrency/romance scams. Physical violence for "
            "refusal or low 'productivity.' Ransom demanded for release "
            "(USD 5,000-15,000). India rescued 900+ nationals from Myanmar "
            "and Cambodia (2022-2024). IOM and UNODC investigations ongoing."
        ),
        "source": "UNODC / IOM / Indian MEA / Nepal DoFE",
    },
]

