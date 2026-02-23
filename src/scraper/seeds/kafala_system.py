"""Kafala (sponsorship) system — structure, reforms, and impacts across Gulf states."""

KAFALA_SYSTEM_FACTS: list[dict] = [
    # ── System Structure ────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Kafala System — Core Legal Structure",
        "summary": "Kafala (sponsorship) ties a migrant worker's legal residency to a specific employer-sponsor (kafeel). Worker cannot enter, leave, or change employment without sponsor's consent. Origins in 1950s-60s Gulf state labour laws to manage temporary migration. Creates structural power imbalance enabling exploitation.",
        "source": "ILO / Migrant Forum in Asia",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Kafala System — Exploitation Mechanisms",
        "summary": "Kafala enables exploitation through: (1) employer controls immigration status, (2) worker cannot leave without exit permit/NOC, (3) changing jobs requires sponsor release, (4) 'absconding' charges criminalise workers who flee abuse, (5) sponsor can cancel visa unilaterally. UN Special Rapporteur called kafala 'inherently abusive'.",
        "source": "UN Special Rapporteur on Contemporary Forms of Slavery",
    },
    # ── Qatar ───────────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Law No. 19 of 2020 Removing NOC Requirement",
        "summary": "Qatar abolished No Objection Certificate (NOC) requirement for changing employers (Law No. 19 of 2020, effective Sep 2020). Workers can change jobs after notice period without employer consent. Also introduced non-discriminatory minimum wage of QAR 1,000/month. Hailed as most significant Gulf reform. Implementation challenges: employers file counter-complaints, delays in processing.",
        "source": "Qatar Ministry of Labour / ILO Qatar Office",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Abolition of Exit Permit (2018)",
        "summary": "Qatar abolished exit permit requirement for most workers via Law No. 13 of 2018 (effective Jan 2019). Workers no longer need employer permission to leave the country. Domestic workers excluded initially, included from 2020. Grievance committees established for disputes. Some employers still withhold passports to prevent departure despite legal changes.",
        "source": "Qatar Government Communications Office / ILO",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Post-Reform Job Mobility Statistics",
        "metric": "job_transfers_post_reform",
        "value": "242,870",
        "summary": "Between Sep 2020 and Dec 2022, 242,870 workers changed jobs in Qatar without NOC under the new system — a 70% increase over pre-reform transfer rates. However, ILO monitoring found 30% of transfer requests faced delays or obstruction. Workers in construction and cleaning sectors reported highest employer resistance.",
        "source": "ILO Qatar / Qatar Ministry of Labour",
    },
    # ── Saudi Arabia ────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Labour Reforms Initiative (March 2021)",
        "summary": "Saudi Arabia's Labour Reform Initiative (Mar 2021) allows workers to transfer between employers without sponsor consent after: completing 1 year of contract, or if employer fails to pay salary for 3+ months, or if employer does not renew work permit. Also introduces exit/re-entry visa without employer approval. Domestic workers excluded from these reforms.",
        "source": "Saudi Ministry of Human Resources and Social Development",
    },
    {
        "type": "statistic",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Migrant Worker Population Under Kafala",
        "metric": "migrant_workers_under_kafala",
        "value": "10.6M",
        "summary": "Saudi Arabia hosts approximately 10.6 million migrant workers (2023), making it the third-largest migrant destination globally. Workers predominantly from India, Pakistan, Bangladesh, Philippines, Indonesia, Nepal, Ethiopia. Domestic workers (estimated 3.7M) remain under traditional kafala with minimal labour law protections.",
        "source": "Saudi General Authority for Statistics / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Domestic Worker Exclusion from Labour Reform",
        "sector": "domestic_work",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": "Saudi domestic workers (est. 3.7M, predominantly female) excluded from 2021 Labour Reform Initiative and main Labour Law. Governed instead by Decision No. 310 of 2013 with weaker protections: no overtime limits, no guaranteed weekly rest day until 2023, no access to labour courts. Transfers require current employer's NOC. Creates two-tier protection system.",
        "source": "Human Rights Watch / Migrant-Rights.org",
    },
    # ── UAE ──────────────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "AE",
        "title": "UAE — Federal Decree Law No. 33 of 2021 (Labour Relations)",
        "summary": "UAE's new labour law (effective Feb 2022) allows workers to change employers during contract with 1-3 months' notice. Eliminates employer consent requirement for job transfers. Work permits tied to Ministry of Human Resources, not individual sponsor. Applies to private sector; domestic workers covered under separate Federal Law No. 10 of 2017.",
        "source": "UAE Ministry of Human Resources / WAM News Agency",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Post-Reform Implementation Gaps",
        "sector": "construction",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": "Despite 2022 reforms, Human Rights Watch (2024) documented ongoing exploitation: employers filing absconding complaints against workers who resign, labour ban imposed on workers who leave before contract end, wage theft during notice period, refusal to provide end-of-service benefits. Workers unaware of new rights. Enforcement capacity of 400 inspectors for 5M+ workers.",
        "source": "Human Rights Watch / ITUC",
    },
    # ── Kuwait ──────────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "KW",
        "title": "Kuwait — Law No. 6 of 2010 (Private Sector Labour Law)",
        "summary": "Kuwait allows workers to transfer employers after 3 years of service with same sponsor (reduced from 5 years in 2016 amendment). Domestic Workers Law No. 68 of 2015 grants limited protections: 12-hour workday cap, weekly day off, 30 days annual leave. However, employer must still sign release for domestic worker transfer, maintaining kafala leverage.",
        "source": "Kuwait National Assembly / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "title": "Kuwait — Domestic Worker Shelter System",
        "sector": "domestic_work",
        "exploitation_type": "restriction_of_movement",
        "summary": "Kuwait operates government-run domestic worker shelters housing 600-800 workers fleeing abuse at any given time. Workers wait 3-6 months for case resolution. Cannot work during wait. Absconding charges may be pending. Some shelters operate as de facto detention with restricted movement. Recruitment agencies may charge 'replacement fees' to sponsors, passed to next worker.",
        "source": "Kuwait Society for Human Rights / HRW",
    },
    # ── Bahrain ─────────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "BH",
        "title": "Bahrain — Flexi-Permit System (2017)",
        "summary": "Bahrain introduced Flexi-Permit allowing irregular workers to regularise status and work independently without a sponsor. Workers pay BHD 79/year for permit. Can work for multiple employers. 68,000+ workers used the system by 2023. Praised as most progressive Gulf reform but limited to workers already in Bahrain. New entrants still require sponsor.",
        "source": "Bahrain LMRA / ILO",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BH",
        "title": "Bahrain — Electronic Wage Protection System",
        "summary": "Bahrain mandated electronic wage payment through banking system (LMRA Decision 2021). All employers must pay wages through bank transfers within 7 days of due date. System allows real-time monitoring of non-payment. Penalties for violations: BHD 200-500 per worker. Covers private sector; domestic workers included from 2023.",
        "source": "Bahrain LMRA / Central Bank of Bahrain",
    },
    # ── Oman ─────────────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "OM",
        "title": "Oman — Royal Decree 53/2023 (Labour Law Reform)",
        "summary": "Oman's new labour law (Royal Decree 53/2023) introduced limited reforms: workers can change employer after 1 year, employer no longer controls exit visa. However, employer must be notified 30 days in advance and can object based on 'legitimate business reasons'. Domestic workers covered by separate Ministerial Decision 189/2004 with weaker protections.",
        "source": "Oman Ministry of Labour / Muscat Daily",
    },
    # ── Broader Analysis ────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Kafala Reform Assessment — Structural vs. Cosmetic Changes",
        "summary": "Reform typology: (1) Cosmetic: rename kafala while keeping sponsor control (Oman, Kuwait), (2) Partial: remove exit permit but keep transfer restrictions (SA pre-2021), (3) Substantial: remove NOC for transfers (Qatar 2020, UAE 2022), (4) Structural: allow independent work permits (Bahrain Flexi-Permit). No Gulf state has achieved full structural reform. Domestic workers excluded from most reforms.",
        "source": "Migrant-Rights.org / Gulf Labour Markets and Migration (GLMM)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "GCC Total Migrant Worker Population Under Kafala Variants",
        "metric": "gcc_migrant_workers",
        "value": "30M+",
        "summary": "Combined GCC migrant workforce exceeds 30 million: Saudi Arabia 10.6M, UAE 8.7M, Kuwait 3.1M, Qatar 2.2M, Oman 1.9M, Bahrain 0.8M. Migrants comprise 35-90% of total population depending on state. Kafala reforms vary significantly by country but all retain some form of employer-linked status for new arrivals.",
        "source": "Gulf Labour Markets and Migration (GLMM) / IOM",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Absconding Charges as Kafala Enforcement Tool",
        "summary": "In all GCC states, employers can file 'absconding' (huroob) reports against workers who leave without permission. Consequences: visa cancelled, worker becomes undocumented, subject to arrest/detention/deportation, banned from re-entry. Used as retaliation against workers who complain. Qatar (2021) and UAE (2022) introduced protections but employers still file preemptive reports.",
        "source": "ITUC / Amnesty International / Gulf Centre for Human Rights",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Kafala and FIFA World Cup 2022 — Reform Catalyst",
        "sector": "construction",
        "exploitation_type": "multiple",
        "summary": "FIFA World Cup 2022 in Qatar catalysed unprecedented kafala reforms under international scrutiny. ILO Technical Cooperation Programme established 2018. Reforms included: NOC abolition, minimum wage, exit permit removal, dispute resolution committees, heat work ban expansion. However, Guardian investigation documented 6,500+ migrant worker deaths in Qatar since World Cup awarded (2010-2020). Legacy of reforms uncertain post-tournament.",
        "source": "ILO / The Guardian / Amnesty International",
    },
]
