"""Social protection gaps — insurance, healthcare, pensions, and safety nets for migrants."""

SOCIAL_PROTECTION_FACTS: list[dict] = [
    # ── Global Gaps ─────────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Migrant Workers Excluded from Social Protection — Global",
        "metric": "social_protection_gap",
        "value": "73%",
        "summary": "ILO World Social Protection Report (2022): 73% of international migrant workers lack adequate social protection coverage. Key exclusions: no unemployment insurance, no occupational injury compensation, no pension portability, no healthcare in destination country. Domestic workers and agricultural workers face highest exclusion rates.",
        "source": "ILO World Social Protection Report 2020-22",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Social Security Agreement Gaps for Migrant Workers",
        "summary": "Bilateral Social Security Agreements (BSSAs) allow pension portability between countries. Only 30% of migration corridors covered by BSSAs. Gulf Cooperation Council states have zero BSSAs with major labour-sending countries (PH, BD, NP, IN). Workers lose pension contributions upon departure. Estimated USD 40B+ in stranded pension benefits globally for migrant workers.",
        "source": "ILO / IOM / World Bank",
    },
    # ── Healthcare Access ───────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "QA",
        "title": "Qatar — Migrant Worker Healthcare Provisions",
        "summary": "Qatar mandates employer-provided health cards for all workers (Ministerial Decision 2022). Workers entitled to primary care at government health centres for QAR 100/visit. Emergency care free regardless of status. However: long wait times at facilities designated for migrant workers, limited specialist access, employer must approve hospital visits during work hours, mental health services nearly absent.",
        "source": "Qatar Ministry of Public Health / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Healthcare Barriers for Domestic Workers",
        "sector": "domestic_work",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": "Saudi domestic workers rely on employer for healthcare access: employer holds insurance card, must accompany worker to hospital (or provide authorisation), medical costs often deducted from salary. Workers reporting abuse-related injuries risk employer retaliation. Undocumented workers (post-absconding) cannot access any healthcare. Amnesty documented cases of workers denied treatment for severe injuries.",
        "source": "Human Rights Watch / Amnesty International",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "TH",
        "title": "Thailand — Migrant Health Insurance Scheme",
        "summary": "Thailand allows registered migrant workers to buy health insurance via Social Security Fund (5% employer, 5% worker contribution). Covers medical treatment, disability, death benefits. However: undocumented workers (estimated 1-2M) excluded entirely, factory-based workers face enrollment barriers, fishing sector workers rarely covered due to informal employment. Migrant Health Volunteers program supplements access.",
        "source": "Thailand Ministry of Public Health / IOM Thailand",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Occupational Injury Compensation Gap for Migrants",
        "metric": "workers_compensation_exclusion",
        "value": "60%+",
        "summary": "Over 60% of migrant workers globally are excluded from workers' compensation schemes due to: informal employment, domestic work exclusions, employer non-registration, undocumented status, or legal barriers to filing claims. When eligible, workers face: language barriers, complex bureaucracy, employer intimidation, and deportation before claim resolution.",
        "source": "ILO / World Bank Migration and Development Brief",
    },
    # ── Wage Protection ─────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "AE",
        "title": "UAE — Wage Protection System (WPS)",
        "summary": "UAE Wage Protection System (2009, expanded 2019) requires all private sector employers to pay wages electronically through approved banks/exchange houses within 10 days of due date. Central Bank monitors compliance. Sanctions: work permit freeze, fines, criminal prosecution. Coverage: 5M+ workers. Gaps: domestic workers excluded until 2023, cash payments still occur in informal sectors.",
        "source": "UAE Ministry of Human Resources / Central Bank of UAE",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Wage Protection System",
        "summary": "Qatar WPS (Law No. 1 of 2015, strengthened 2021) requires electronic salary payment within 7 days. Workers Support and Insurance Fund established to pay salaries when employers default (up to 3 months). Non-compliant companies face: operating license suspension, work permit ban, criminal referral. Fund disbursed QAR 358M to 36,000 workers (2019-2022).",
        "source": "Qatar Ministry of Labour / ILO Qatar",
    },
    # ── Pensions and End-of-Service ─────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "End-of-Service Benefits Theft in Gulf States",
        "summary": "GCC labour laws entitle workers to end-of-service gratuity (typically 15-30 days salary per year of service). Common theft patterns: employer terminates worker just before gratuity vests, files absconding report to void entitlement, offers 'voluntary resignation' waiving benefits, deducts inflated costs from final settlement. Workers deported before claims processed.",
    },
    {
        "type": "statistic",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — End-of-Service Benefit Claims",
        "metric": "eos_complaints",
        "value": "180,000+ annually",
        "summary": "Saudi Labour Courts receive 180,000+ complaints annually, majority involving end-of-service benefit disputes. Average case resolution: 6-12 months. Workers often repatriated before hearing date. 2023 reforms allow remote hearings and automated calculation, but workers need legal representation rarely available. Estimated SAR 8B+ in unpaid end-of-service benefits.",
        "source": "Saudi Ministry of Justice / Saudi Labour Courts Statistics",
    },
    # ── Death and Injury Compensation ───────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal — Families Receiving Zero Compensation for Worker Deaths Abroad",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": "Nepal Foreign Employment Board reported 7,467 migrant worker deaths abroad (2008-2022). Average compensation received by families: NPR 700,000 (USD 5,300) — often paid as 'diyat' (blood money) in Gulf states. 40% of families received nothing. Insurance claims (mandatory NPR 500,000 policy) rejected on grounds of 'natural death' classification. Families left with debt from recruitment fees.",
        "source": "Nepal Foreign Employment Board / Pravasi Nepali Coordination Committee",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "NP",
        "title": "Nepal — Foreign Employment Insurance Reforms",
        "summary": "Nepal Foreign Employment Act (2007, amended 2019) mandates life insurance of NPR 1.5M for migrant workers. Premium NPR 1,500 shared between worker and recruitment agency. Coverage: death, disability, repatriation. Claims process: requires death certificate from destination country (often delayed 6-12 months), employer statement, embassy attestation. 55% claim rejection rate due to documentation requirements.",
        "source": "Nepal Insurance Board / Foreign Employment Promotion Board",
    },
    # ── Social Security Portability ─────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Pension Portability — Corridors Without Agreements",
        "summary": "Major migration corridors without social security agreements: PH-SA, BD-MY, NP-QA, ET-LB, IN-AE, ID-SG, MM-TH. Workers contribute to destination country social security (where applicable) but cannot transfer or withdraw upon departure. Philippines SSS allows voluntary continued membership abroad. India-UAE exploring bilateral agreement (2024) but not yet operational.",
        "source": "ILO / World Bank / IOM Global Compact on Migration",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Philippines — Overseas Workers Welfare Administration (OWWA)",
        "summary": "OWWA provides social protection package for 2.2M registered OFWs: life insurance, disability benefits, repatriation assistance, education loans for dependents, skills training. Funded by USD 25 membership fee per contract. Coverage gaps: undocumented workers excluded, benefits modest (death benefit only PHP 200,000 / USD 3,600), long claims processing. OWWA reserves: PHP 20B+.",
        "source": "OWWA / Philippines DMW",
    },
    # ── Unemployment and Retrenchment ───────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Migrant Worker Vulnerability During Economic Downturns",
        "summary": "Migrant workers first to lose employment during economic crises but last to receive social protection. Patterns: mass layoffs without notice or severance (GCC 2020), wage arrears accumulate, workers stranded without return ticket, visas cancelled creating undocumented status, shelters overwhelmed. COVID-19 left 100,000+ workers stranded in Gulf states without income or repatriation assistance.",
        "source": "IOM / Migrant Forum in Asia / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Retrenchment Without Protection for Migrant Workers",
        "sector": "manufacturing",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": "Malaysian Employment Act (1955) does not provide unemployment insurance for migrant workers. Employment Insurance System (EIS, 2018) explicitly excludes foreign workers. During retrenchments (electronics sector 2022-2023), migrant workers received no severance, no notice period, and were required to leave Malaysia within 30 days. Workers who stayed became undocumented, subject to arrest.",
        "source": "Malaysian Trades Union Congress / MTUC-ITUC",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Remittance Dependence and Social Protection Trade-off",
        "metric": "remittance_share_of_gdp",
        "value": "up to 37%",
        "summary": "Remittances exceed 10% of GDP in 30+ countries, reaching 37% in Tonga and 27% in Nepal. Workers accept exploitative conditions to maintain remittance flows because family survival depends on it. Lack of social protection at home (no unemployment insurance, no pension) increases pressure to stay in abusive employment abroad. Creates structural vulnerability to forced labour.",
        "source": "World Bank Migration and Remittances Data / KNOMAD",
    },
]
