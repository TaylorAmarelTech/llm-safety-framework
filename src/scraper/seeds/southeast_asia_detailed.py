"""Southeast Asian migrant worker exploitation — Thailand, Malaysia, Indonesia, Myanmar, Cambodia, Vietnam."""

SOUTHEAST_ASIA_FACTS: list[dict] = [
    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  THAILAND  (TH)  —  30+ facts                                      ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    # ── TH: Laws & Regulations ───────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "TH",
        "title": "Thailand Anti-Trafficking in Persons Act B.E. 2551 (2008)",
        "summary": (
            "Thailand's primary anti-trafficking statute. Criminalises trafficking "
            "for forced labour, sexual exploitation, slavery, and organ removal. "
            "Penalties: 4-10 years imprisonment and fines of THB 80,000-200,000 for "
            "basic offences; up to life imprisonment for offences against children "
            "under 15. Amended in 2015 (B.E. 2558) to broaden the definition of "
            "exploitation and increase penalties for officials involved in trafficking."
        ),
        "law": "Anti-Trafficking in Persons Act B.E. 2551",
        "year": 2008,
        "source": "Royal Thai Government Gazette / ILO",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "TH",
        "title": "Thailand — Royal Ordinance on Fisheries B.E. 2558 (2015)",
        "summary": (
            "Emergency decree overhauling fisheries governance after EU yellow card "
            "and AP slavery exposé. Key provisions: mandatory vessel registration and "
            "licensing, Vessel Monitoring System (VMS) for all commercial vessels over "
            "30 GT, Port-In Port-Out (PIPO) inspection centres at 32 ports, mandatory "
            "crew lists and employment contracts, criminalisation of IUU fishing with "
            "fines up to THB 30 million. Amended in 2017 to tighten transshipment "
            "controls."
        ),
        "source": "Thai Department of Fisheries / EU DG MARE",
    },
    {
        "type": "law",
        "jurisdiction": "TH",
        "title": "Thailand — Royal Ordinance on Foreign Workers Management B.E. 2560 (2017)",
        "summary": (
            "Consolidated law governing migrant worker employment in Thailand. "
            "Requires work permits for all foreign nationals. Introduced heavy fines "
            "for undocumented workers (THB 5,000-50,000) and employers hiring them "
            "(THB 10,000-100,000 per worker). Initially caused mass exodus of migrant "
            "workers; enforcement softened after criticism from ILO and civil society. "
            "Amended multiple times to extend registration deadlines."
        ),
        "law": "Royal Ordinance on Foreign Workers Management B.E. 2560",
        "year": 2017,
        "source": "Thailand Ministry of Labour / ILO",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "TH",
        "title": "Thailand — Labour Protection Act Amendments for Fishing (2019)",
        "summary": (
            "Extended Labour Protection Act coverage to fishing workers previously "
            "excluded. Guarantees: minimum rest of 10 hours per 24-hour period, "
            "minimum one day off per month at sea, employment contracts in worker's "
            "language, wage payment at least monthly via bank transfer. Implementing "
            "Ministerial Regulation B.E. 2557 on sea fishery work conditions."
        ),
        "source": "Thailand Ministry of Labour / ILO",
    },
    {
        "type": "law",
        "jurisdiction": "TH",
        "title": "Thailand — Section 312 Criminal Code (Forced Labour)",
        "summary": (
            "Section 312 of the Thai Criminal Code criminalises causing a person to "
            "work by means of force, threat, or deprivation of liberty. Penalty: "
            "imprisonment up to 3 years and fine up to THB 6,000. Rarely used "
            "compared to the Anti-Trafficking Act; prosecutors prefer the trafficking "
            "statute because it carries heavier penalties and allows asset forfeiture."
        ),
        "law": "Thai Criminal Code Section 312",
        "source": "Thai Criminal Code / IJM Thailand",
    },

    # ── TH: Fishing Sector ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "AP Benjina Investigation — 2,000 Slaves Freed (2015)",
        "exploitation_type": "restriction_of_movement",
        "sector": "fishing",
        "summary": (
            "Associated Press investigation traced Thai seafood supply chain to "
            "Benjina island, Indonesia, where over 2,000 men — mostly Myanmar and "
            "Cambodian nationals — were held in slave-like conditions on fishing "
            "vessels. Workers confined in cages, beaten, held at sea for years. "
            "Investigation led to rescue operations, criminal prosecutions, and "
            "a Pulitzer Prize. Product entered supply chains of major US retailers."
        ),
        "source": "Associated Press (2015) / Pulitzer Prize",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "Thailand — Broker Networks Selling Workers to Fishing Captains",
        "exploitation_type": "debt_bondage",
        "sector": "fishing",
        "summary": (
            "Myanmar workers recruited at border towns (Mae Sot, Ranong) by brokers "
            "promising factory jobs at THB 10,000-15,000/month. Sold to fishing boat "
            "captains for THB 10,000-30,000 per worker. Workers told they must repay "
            "the 'sale price' before receiving wages. Confined to vessels for 12-22 "
            "months. EJF documented physical violence reported by 59% of trafficked "
            "fishers."
        ),
        "source": "Environmental Justice Foundation / ILO",
    },
    {
        "type": "statistic",
        "jurisdiction": "TH",
        "title": "Thailand — PIPO Inspection System Data",
        "metric": "pipo_inspections",
        "value": "470,000+ inspections (2015-2022)",
        "summary": (
            "Thailand's 32 Port-In Port-Out (PIPO) centres conducted over 470,000 "
            "inspections of fishing vessels between 2015 and 2022. Identified "
            "approximately 4,200 labour violations. However, only 83 cases referred "
            "to criminal prosecution. Critics note inspections last 5-15 minutes, "
            "workers interviewed in front of employers, interpreters often absent, "
            "and inspectors lack training on trafficking indicators."
        ),
        "source": "Thai Department of Fisheries / ILO / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "KH-TH",
        "title": "Thai Ghost Fleet — Unregistered Fishing Vessels",
        "exploitation_type": "multiple",
        "sector": "fishing",
        "summary": (
            "An estimated 30,000-65,000 fishing vessels in Thailand remain "
            "unregistered and operate outside the VMS tracking system. These 'ghost "
            "fleet' vessels are disproportionately associated with forced labour, "
            "as they evade PIPO inspections. Crew — predominantly Myanmar and "
            "Cambodian — have no contracts, no documented employment, and no access "
            "to grievance mechanisms. EJF estimates unregistered vessels account for "
            "the majority of remaining forced labour in Thai fisheries."
        ),
        "source": "EJF / Greenpeace Southeast Asia",
    },

    # ── TH: Shrimp Processing ────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "Thailand — Shrimp Peeling Shed Exploitation in Samut Sakhon",
        "exploitation_type": "debt_bondage",
        "sector": "food_processing",
        "summary": (
            "Samut Sakhon province hosts hundreds of shrimp peeling sheds employing "
            "predominantly Myanmar migrant women and children. AP (2015) documented "
            "16-hour shifts, locked facilities, child labour (children as young as "
            "6), and wages of THB 100-200/day (below minimum wage of THB 300). "
            "Product entered supply chains of CP Foods, which supplied Walmart, "
            "Costco, and Tesco. CP Foods subsequently committed to supply chain "
            "audits."
        ),
        "source": "Associated Press / Guardian / US State Dept TIP Report",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand — Forced Labour in Shrimp Feed Supply Chain",
        "exploitation_type": "withholding_wages",
        "sector": "food_processing",
        "summary": (
            "Guardian investigation (2014) revealed forced labour in production of "
            "fishmeal used as shrimp feed. 'Trash fish' caught by slave-crewed "
            "vessels ground into fishmeal at processing plants in Samut Sakhon. "
            "Fishmeal sold to CP Foods shrimp farms. Workers at fishmeal plants "
            "earned below minimum wage, passports confiscated. Supply chain linked "
            "to major UK supermarkets including Tesco, Morrisons, and Aldi."
        ),
        "source": "The Guardian / EJF",
    },

    # ── TH: Agriculture ──────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "Thailand — Myanmar Workers in Sugarcane Harvesting",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Myanmar migrant workers in Thailand's sugarcane sector concentrated in "
            "Kanchanaburi, Udon Thani, and Nakhon Ratchasima provinces. Workers "
            "recruited through informal brokers, debt of THB 5,000-15,000 for "
            "transport and document fees. Piece-rate pay of THB 50-70 per tonne of "
            "cut cane, resulting in below-minimum-wage earnings. Heat exposure, "
            "machete injuries, and no access to healthcare documented by Migrant "
            "Working Group."
        ),
        "source": "Migrant Working Group Thailand / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "Thailand — Exploitation in Poultry Processing",
        "exploitation_type": "withholding_wages",
        "sector": "food_processing",
        "summary": (
            "Myanmar and Cambodian workers in chicken processing plants in central "
            "Thailand report systematic deductions: THB 1,000-3,000/month for "
            "dormitory, THB 500-800 for meals, THB 200-500 for 'equipment fees', "
            "reducing net wages below minimum wage. Workers on short-term contracts "
            "face deportation threats if they complain. Finnwatch investigation "
            "(2018) linked exploitation to European poultry imports."
        ),
        "source": "Finnwatch / ILO / Migrant Working Group",
    },

    # ── TH: Construction ─────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "Thailand — Construction Sector Debt Bondage",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "ILO survey (2017) of 434 construction workers in Bangkok found 38% "
            "paid recruitment fees averaging THB 16,600 (up to THB 70,000). 31% "
            "reported passport confiscation, 18% experienced wage deductions not "
            "agreed upon, 12% reported physical threats. Subcontracting chains of "
            "4-5 layers obscure employer liability. Workers fall through gaps in "
            "social security coverage and workers' compensation."
        ),
        "source": "ILO Baseline Survey (2017) / Verité",
    },

    # ── TH: Domestic Work ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "Thailand — Myanmar Domestic Workers in Bangkok",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "An estimated 300,000 domestic workers in Thailand, majority from "
            "Myanmar. Domestic workers excluded from Labour Protection Act until "
            "Ministerial Regulation 14 (2012) extended partial coverage (rest days, "
            "holidays). Still excluded from: minimum wage protection, working hours "
            "limits, social security, and workers' compensation. ILO documented "
            "24/7 availability demands, confiscation of phones, isolation in "
            "employer homes, and wages of THB 3,000-5,000/month."
        ),
        "source": "ILO / HomeNet Thailand / MAP Foundation",
    },

    # ── TH: TIP Report & Registration ────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "TH",
        "title": "Thailand — US TIP Report Tier History",
        "metric": "tip_tier_history",
        "value": "Tier 2 Watch List to Tier 3 to Tier 2",
        "summary": (
            "Thailand TIP Report history: Tier 2 Watch List (2010-2013), downgraded "
            "to Tier 3 (2014) after AP fishing slavery exposé and failure to address "
            "complicity. Upgraded to Tier 2 Watch List (2016) after Royal Ordinance "
            "on Fisheries reforms. Upgraded to Tier 2 (2018). Has remained Tier 2 "
            "since, with continued concerns about low prosecution rates and "
            "inadequate victim identification. In 2023, only 211 trafficking "
            "investigations and 96 convictions reported."
        ),
        "source": "US State Department TIP Reports (2010-2024)",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "TH",
        "title": "Thailand — Pink Card Migrant Registration System",
        "summary": (
            "Thailand's migrant worker registration uses a 'pink card' (Tor Ror 38/1) "
            "for workers from Myanmar, Cambodia, and Laos. Card ties worker to a "
            "specific employer, restricting job mobility. Workers must obtain "
            "employer consent to change jobs, creating dependency and vulnerability "
            "to exploitation. Nationality Verification (NV) process allows upgrade "
            "to full work permit but costs THB 9,000-12,000 and requires cooperation "
            "of origin-country embassy."
        ),
        "source": "Thailand Ministry of Labour / MAP Foundation",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "TH",
        "title": "Thailand — Nationality Verification (NV) Process",
        "summary": (
            "Nationality Verification requires migrant workers to obtain temporary "
            "passports from their embassies and then apply for Thai work permits. "
            "Process costs THB 9,000-12,000 (officially) but brokers charge THB "
            "15,000-25,000. Workers must travel to Bangkok-based embassies, losing "
            "wages. NV documents tied to single employer. Workers who change "
            "employers become undocumented, increasing trafficking vulnerability. "
            "System criticized by ILO as creating 'captive labour'."
        ),
        "source": "ILO / MAP Foundation / Migrant Working Group",
    },
    {
        "type": "statistic",
        "jurisdiction": "TH",
        "title": "Thailand — Social Security Coverage for Migrant Workers",
        "metric": "migrant_social_security",
        "value": "approx 1.1 million enrolled out of 3.9 million registered",
        "summary": (
            "As of 2023, approximately 1.1 million of 3.9 million registered "
            "migrant workers in Thailand enrolled in social security. Coverage "
            "provides healthcare, disability, and death benefits. Gaps: domestic "
            "workers, agricultural workers on small farms, and fishing workers "
            "excluded or under-covered. Undocumented workers (estimated 1-2 million "
            "additional) have no coverage. Many employers fail to register workers "
            "despite legal obligation."
        ),
        "source": "Thailand Social Security Office / ILO",
    },

    # ── TH: MOU Recruitment ──────────────────────────────────────────────
    {
        "type": "bilateral",
        "jurisdiction": "TH",
        "title": "Thailand — MOU-Based Recruitment from Myanmar, Cambodia, Laos",
        "summary": (
            "Thailand has bilateral MOUs with Myanmar (2003), Cambodia (2003), Laos "
            "(2002), and Vietnam (2015) for labour migration. MOU process: worker "
            "recruited in origin country, documents processed through government "
            "agencies, arrives with legal status. In practice: MOU process takes "
            "3-6 months and costs THB 15,000-25,000 per worker (mostly broker fees). "
            "Many workers bypass MOU via irregular border crossing (2-3 days, THB "
            "5,000-10,000) then register after arrival. MOU workers still tied to "
            "sponsoring employer."
        ),
        "source": "ILO / IOM / Thailand Ministry of Labour",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "Thailand — Rohingya Trafficking Through Southern Thailand",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "From 2012-2015, trafficking networks moved an estimated 100,000-170,000 "
            "Rohingya through Thailand en route to Malaysia. Victims held in jungle "
            "camps in Songkhla and Padang Besar, beaten, starved, and held for "
            "ransom (USD 1,500-2,500 per person). Those unable to pay sold into "
            "forced labour on Thai fishing vessels or plantations. In 2015, mass "
            "graves found in Wang Kelian (Malaysia) and Padang Besar (Thailand). "
            "Subsequent trial convicted 62 people including a Thai army general."
        ),
        "source": "Reuters / UNHCR / Thai Criminal Court",
    },

    # ── TH: Court Decisions ──────────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "TH",
        "title": "Thailand — Rohingya Trafficking Trial (2017)",
        "summary": (
            "Thailand Criminal Court convicted 62 of 103 defendants in the largest "
            "human trafficking trial in Thai history. Convicted included Lt. Gen. "
            "Manas Kongpan (highest-ranking military official ever convicted for "
            "trafficking in Thailand), police officers, politicians, and brokers. "
            "Sentences ranged from 4 to 94 years. Case involved trafficking of "
            "Rohingya through jungle camps in southern Thailand."
        ),
        "source": "Thai Criminal Court / Reuters",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "TH",
        "title": "Thailand — Labour Court Awards Compensation to Trafficked Fishers (2018)",
        "summary": (
            "Thailand Central Labour Court ruled in favour of 14 Myanmar fishers "
            "trafficked onto Thai fishing vessels. Court awarded THB 1.3 million in "
            "unpaid wages and compensation. Landmark because it was among the first "
            "Thai labour court decisions treating trafficked fishers as employees "
            "entitled to labour law protections rather than irregular migrants "
            "subject to deportation."
        ),
        "source": "Thai Central Labour Court / LPN Foundation",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand — Border Crossing Exploitation at Mae Sot",
        "exploitation_type": "deception",
        "sector": "multiple",
        "corridor": "MM-TH",
        "summary": (
            "Mae Sot (Tak province) is the primary crossing point for Myanmar "
            "workers entering Thailand. Brokers operate openly, charging THB "
            "5,000-15,000 for border crossing. Workers promised specific jobs and "
            "wages; upon arrival, documents confiscated and workers transported to "
            "different provinces. Some sold to fishing, agriculture, or factory "
            "employers. Thai authorities conduct periodic crackdowns but broker "
            "networks reconstitute rapidly. An estimated 200,000 Myanmar workers "
            "cross irregularly at Mae Sot annually."
        ),
        "source": "MAP Foundation / IOM Thailand",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "MM-TH",
        "title": "Thailand — Rubber Plantation Exploitation in Southern Thailand",
        "exploitation_type": "withholding_wages",
        "sector": "agriculture",
        "summary": (
            "Myanmar workers on rubber plantations in Surat Thani and Chumphon "
            "provinces paid on piece-rate basis: THB 3-5 per kg of rubber tapped. "
            "Average daily earnings THB 150-250, below minimum wage. Workers live in "
            "remote plantation housing, dependent on employer for food and transport. "
            "Limited access to healthcare or education for children. Debt commonly "
            "incurred for advance wages and housing deposits."
        ),
        "source": "ILO / Migrant Working Group Thailand",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  MALAYSIA  (MY)  —  30+ facts                                      ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    # ── MY: Laws & Regulations ───────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "MY",
        "title": "Malaysia — Anti-Trafficking in Persons and Anti-Smuggling of Migrants Act 2007 (ATIPSOM)",
        "summary": (
            "Malaysia's principal anti-trafficking law. Criminalises trafficking for "
            "forced labour and sexual exploitation. Penalties: 3-20 years imprisonment "
            "and fines. Amended in 2010 to increase penalties and allow victims "
            "to work during trial proceedings. Amended again in 2015 to include "
            "provisions for freedom of movement for victims. Enforcement criticized: "
            "convictions declined from 127 (2017) to 50 (2022). Victims still "
            "routinely detained in immigration facilities."
        ),
        "law": "ATIPSOM 2007",
        "year": 2007,
        "source": "Malaysian Government Gazette / US TIP Report",
    },
    {
        "type": "law",
        "jurisdiction": "MY",
        "title": "Malaysia — Employment Act 1955 and Migrant Worker Exclusions",
        "summary": (
            "Malaysia's Employment Act 1955 (amended 2022) covers most private "
            "sector workers. Key exclusion: domestic workers — specifically excluded "
            "from provisions on working hours, overtime pay, rest days, public "
            "holidays, and termination benefits. An estimated 250,000-350,000 "
            "domestic workers in Malaysia (mostly Indonesian and Filipino) lack "
            "these statutory protections. The 2022 amendment extended some "
            "protections to domestic workers for the first time but enforcement "
            "remains minimal."
        ),
        "law": "Employment Act 1955",
        "year": 1955,
        "source": "Malaysian Government / ILO / Tenaganita",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "MY",
        "title": "Malaysia — Mandatory Workers' Minimum Standards of Housing Act 2019 (Act 446)",
        "summary": (
            "Requires employers to provide minimum housing standards for workers: "
            "minimum 36 sq ft per person, adequate sanitation, ventilation, clean "
            "water. Penalties: fines up to MYR 200,000 and/or imprisonment up to "
            "3 years. Enacted after widespread COVID-19 outbreaks in overcrowded "
            "worker dormitories at Top Glove and other factories. Enforcement began "
            "September 2020; as of 2023, over 1,200 inspections conducted with "
            "347 compound notices issued."
        ),
        "source": "Malaysian Ministry of Human Resources / Amnesty International",
    },

    # ── MY: Palm Oil Sector ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "ID-MY",
        "title": "Malaysia — Forced Labour in Palm Oil Plantations",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Wall Street Journal (2015) and AP (2020) investigations documented "
            "forced labour on Malaysian palm oil plantations supplying major brands "
            "(Nestlé, Unilever, Procter & Gamble). Indonesian workers paid USD "
            "500-1,500 in recruitment fees. Passports confiscated. Housed in "
            "remote plantation camps with no freedom of movement. Piece-rate wages "
            "of MYR 0.15-0.50 per kg of fresh fruit bunches, resulting in below "
            "minimum-wage earnings. Children working alongside parents."
        ),
        "source": "AP / Wall Street Journal / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Sime Darby Palm Oil Forced Labour Findings",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "US Customs and Border Protection (CBP) issued a Withhold Release Order "
            "(WRO) against Sime Darby Plantation Berhad in December 2020 based on "
            "evidence of all 11 ILO forced labour indicators. Findings included: "
            "recruitment fees of USD 2,000-5,000, passport confiscation, restriction "
            "of movement, debt bondage, intimidation, and abusive working conditions. "
            "Sime Darby is world's largest palm oil company by planted area. WRO "
            "modified (not revoked) in February 2022 after remediation."
        ),
        "source": "US CBP / Sime Darby Sustainability Report",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — FGV Holdings Palm Oil WRO",
        "exploitation_type": "multiple",
        "sector": "agriculture",
        "summary": (
            "US CBP issued WRO against FGV Holdings Berhad (September 2020), "
            "Malaysia's largest palm oil company by production. Evidence of: forced "
            "labour, child labour, debt bondage, retention of identity documents, "
            "and restriction of movement on plantations in Sabah and Peninsular "
            "Malaysia. RSPO suspended FGV's sustainability certification. As of "
            "2024, WRO remains in effect. FGV employs approximately 25,000 workers, "
            "majority Indonesian and Bangladeshi migrants."
        ),
        "source": "US CBP / RSPO / Verité",
    },

    # ── MY: Rubber Glove Manufacturing ───────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "BD-MY",
        "title": "Malaysia — Top Glove Forced Labour Investigation",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Top Glove Corporation, world's largest rubber glove manufacturer, "
            "subject to US CBP WRO (March 2021) for forced labour. Workers — "
            "predominantly Bangladeshi and Nepali — paid recruitment fees of USD "
            "2,000-5,000 to brokers. Passports confiscated. Housed in overcrowded "
            "dormitories (up to 25 per room). COVID-19 outbreak infected 5,000+ "
            "workers. Top Glove repaid USD 35 million in recruitment fees to 13,000 "
            "workers; WRO lifted July 2021."
        ),
        "source": "US CBP / Reuters / Guardian",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Hartalega Rubber Glove Forced Labour Allegations",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Hartalega Holdings, Malaysia's second-largest glove maker, investigated "
            "for forced labour indicators following worker complaints (2021). "
            "Allegations: Nepali workers paid NPR 100,000-200,000 in recruitment "
            "fees, dormitories overcrowded, wages below contracted amount after "
            "deductions. Hartalega committed to zero-recruitment-fee policy and "
            "repaid approximately MYR 50 million to workers. No CBP WRO issued "
            "but company placed on US Department of Labor's List of Goods Produced "
            "by Child or Forced Labor."
        ),
        "source": "Verité / US Dept of Labor ILAB / Reuters",
    },

    # ── MY: Electronics Sector ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "BD-MY",
        "title": "Malaysia — Forced Labour in Electronics Manufacturing",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Verité (2014) study found one-third of 501 surveyed electronics workers "
            "in Malaysia met ILO forced labour indicators. Bangladeshi, Nepali, and "
            "Indonesian workers paid USD 1,000-4,000 in recruitment fees. Passports "
            "confiscated by employers or outsourced labour suppliers. Debt repayment "
            "took 3-6 months of wages. Workers supplied to Intel, Samsung, Panasonic "
            "facilities through layers of subcontractors. Responsible Business "
            "Alliance adopted strengthened audit protocols in response."
        ),
        "source": "Verité / Responsible Business Alliance / ILO",
    },

    # ── MY: Construction ─────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "BD-MY",
        "title": "Malaysia — Construction Sector Exploitation of Bangladeshi Workers",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "An estimated 500,000-800,000 Bangladeshi workers in Malaysia's "
            "construction sector. Workers pay BDT 300,000-600,000 (USD 2,800-5,600) "
            "to recruitment agents in Bangladesh. Upon arrival: different employer "
            "than contracted, lower wages (MYR 800-1,200 vs. MYR 1,500-2,000 "
            "promised), forced overtime without pay, passport confiscated by "
            "outsourced labour companies. Workers housed at construction sites in "
            "makeshift shelters. Multi-layered subcontracting means principal "
            "employers disclaim responsibility."
        ),
        "source": "Tenaganita / ILO / Solidarity Center",
    },

    # ── MY: Domestic Work ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "ID-MY",
        "title": "Malaysia — Indonesian Domestic Workers Without Legal Protection",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Approximately 130,000 documented Indonesian domestic workers in Malaysia "
            "(total estimated 250,000+). Domestic workers excluded from Employment "
            "Act: no limits on working hours, no mandatory rest days, no minimum "
            "wage. Documented abuses: 18-20 hour workdays, wages of MYR 400-900/"
            "month (below minimum wage of MYR 1,500), passport confiscation by "
            "employers, physical and sexual abuse, confinement to employer's home. "
            "Indonesia imposed moratorium on domestic worker deployment to Malaysia "
            "2009-2011 after multiple deaths."
        ),
        "source": "Human Rights Watch / Tenaganita / BNP2MI",
    },

    # ── MY: Rohingya & Refugees ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Exploitation of Rohingya Refugees",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "Approximately 100,000-180,000 Rohingya in Malaysia (UNHCR registered: "
            "~105,000 as of 2023). Not recognized as refugees under Malaysian law; "
            "no right to work. Forced into informal economy at extreme vulnerability. "
            "Documented exploitation: construction work at MYR 30-50/day (below "
            "minimum wage), restaurant work for food and shelter only, trafficking "
            "for forced labour and sexual exploitation. Immigration detention "
            "centres hold Rohingya in overcrowded conditions; deaths in detention "
            "documented."
        ),
        "source": "UNHCR / Fortify Rights / Al Jazeera",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Immigration Detention Centre Conditions",
        "exploitation_type": "multiple",
        "sector": "n/a",
        "summary": (
            "Malaysia operates 19 immigration detention depots holding an estimated "
            "15,000-18,000 detainees at any time (capacity: ~12,000). Detainees "
            "include trafficking victims, asylum seekers, and undocumented workers. "
            "SUHAKAM (Malaysian human rights commission) documented: severe "
            "overcrowding, insufficient food and water, limited healthcare, deaths "
            "in custody (528 deaths in 2018-2022 per SUHAKAM). Detained trafficking "
            "victims often not identified and deported."
        ),
        "source": "SUHAKAM / Human Rights Watch / Fortify Rights",
    },

    # ── MY: TIP Report & Enforcement ─────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "MY",
        "title": "Malaysia — US TIP Report Tier History",
        "metric": "tip_tier_history",
        "value": "Tier 2 Watch List / Tier 3 / Tier 2 Watch List",
        "summary": (
            "Malaysia TIP tier history: Tier 2 Watch List (2010-2013), Tier 3 (2014) "
            "after mass graves of trafficking victims found at Wang Kelian border "
            "camps. Upgraded to Tier 2 Watch List (2015, controversial — coincided "
            "with TPP trade negotiations). Returned to Tier 3 (2021) citing failure "
            "to convict traffickers, punish complicit officials, and identify victims. "
            "Upgraded to Tier 2 Watch List (2022). Key concern: convictions dropped "
            "from 127 (2017) to 30 (2023)."
        ),
        "source": "US State Department TIP Reports (2010-2024)",
    },
    {
        "type": "statistic",
        "jurisdiction": "MY",
        "title": "Malaysia — ATIPSOM Enforcement Statistics",
        "metric": "atipsom_enforcement",
        "value": "1,372 investigations, 264 convictions (2008-2023)",
        "summary": (
            "Since ATIPSOM enactment (2007): 1,372 trafficking investigations opened "
            "(2008-2023), 576 prosecutions initiated, 264 convictions obtained. "
            "Conviction rate approximately 46% of prosecuted cases. Declining trend: "
            "50 convictions (2022), 30 convictions (2023). Average sentence: 5-8 "
            "years. No senior officials convicted for complicity despite documented "
            "corruption in immigration enforcement. Victim identification: 662 "
            "victims identified in 2023, down from 1,558 in 2019."
        ),
        "source": "US TIP Report / Malaysian Attorney General's Chambers",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Tenaganita Reports on Migrant Worker Exploitation",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "Tenaganita (Malaysian migrant rights NGO, founded 1991) documented "
            "systematic exploitation across sectors: 87% of migrant workers surveyed "
            "reported recruitment fees exceeding legal limits, 65% had passports "
            "confiscated, 43% experienced wage theft, 38% worked excessive overtime "
            "without pay. Tenaganita operates a crisis centre receiving 2,000-3,000 "
            "complaints annually. Director Irene Fernandez was prosecuted under "
            "Printing Presses Act for publishing detention centre abuses (acquitted "
            "after 13-year trial, 2008)."
        ),
        "source": "Tenaganita annual reports / Solidarity Center",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — SUHAKAM Inquiry into Trafficking",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "SUHAKAM (Malaysian National Human Rights Commission) conducted public "
            "inquiries into trafficking (2019-2020) finding: systemic failures in "
            "victim identification (potential victims deported as illegal immigrants), "
            "corruption among enforcement officers facilitating trafficking, "
            "inadequate shelter conditions for identified victims, victims forced to "
            "remain in shelters for years pending trials with restricted freedom of "
            "movement. Recommended overhaul of ATIPSOM victim identification process."
        ),
        "source": "SUHAKAM / Malaysian Bar Council",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  INDONESIA  (ID)  —  25+ facts                                     ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    # ── ID: Laws & Regulations ───────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "ID",
        "title": "Indonesia — Law No. 18 of 2017 on Protection of Indonesian Workers Abroad",
        "summary": (
            "Replaced Law No. 39/2004. Key improvements: zero placement-fee policy "
            "for domestic workers (costs borne by employers), mandatory pre-departure "
            "training, consular protection provisions, complaint mechanisms via "
            "BP2MI (replacing BNP2TKI). Gaps: enforcement of zero-fee policy is "
            "weak — workers still pay IDR 5-25 million to brokers. Law applies only "
            "to workers placed through official channels; informal recruitment "
            "(estimated 30-50% of total) falls outside scope."
        ),
        "law": "Law No. 18/2017",
        "year": 2017,
        "source": "Indonesian Government Gazette / ILO",
    },
    {
        "type": "law",
        "jurisdiction": "ID",
        "title": "Indonesia — Law No. 21 of 2007 on Eradication of Trafficking",
        "summary": (
            "Indonesia's primary anti-trafficking statute. Criminalises trafficking "
            "for forced labour, sexual exploitation, and organ removal. Penalties: "
            "3-15 years imprisonment and fines of IDR 120 million-600 million. "
            "Enhanced penalties for: trafficking of children (1/3 increase), "
            "government officials involved (additional 1/3), resulting in death "
            "(life imprisonment). Since enactment, approximately 2,600 trafficking "
            "convictions obtained (2007-2023)."
        ),
        "law": "Law No. 21/2007",
        "year": 2007,
        "source": "Indonesian Government Gazette / US TIP Report",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "ID",
        "title": "Indonesia — BP2MI (Agency for Protection of Indonesian Migrant Workers)",
        "summary": (
            "Badan Pelindungan Pekerja Migran Indonesia (BP2MI) replaced BNP2TKI "
            "in 2020 under Presidential Regulation 90/2019. Mandate shifted from "
            "'placement' to 'protection'. Functions: regulate private recruitment "
            "agencies, operate pre-departure training centres (BLK-LN), manage "
            "complaint hotline (dial 110 from abroad), coordinate repatriation. "
            "Placed approximately 165,000 workers through formal channels in 2023. "
            "Budget: IDR 1.2 trillion (2023). Criticized for insufficient "
            "monitoring of recruitment agencies."
        ),
        "source": "BP2MI / IOM Indonesia",
    },

    # ── ID: Moratoriums ──────────────────────────────────────────────────
    {
        "type": "policy_update",
        "jurisdiction": "ID",
        "title": "Indonesia — Moratorium on Domestic Worker Deployment (Various Countries)",
        "summary": (
            "Indonesia imposed deployment moratoriums due to worker exploitation: "
            "Saudi Arabia (2011-2013, 2015, resumed 2017 with conditions), Malaysia "
            "(2009-2011), Jordan (2010-2013), Syria (2011-present), Libya (2011-"
            "present), Kuwait (2009-2018). Each moratorium triggered by worker "
            "deaths and abuse cases. Effect: informal/undocumented migration "
            "increased during moratoriums, leaving workers without consular "
            "protection. Post-moratorium bilateral agreements included minimum wage "
            "guarantees and day-off provisions."
        ),
        "source": "BP2MI / ILO / Human Rights Watch",
    },

    # ── ID: Palm Oil & Internal Exploitation ─────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Internal Trafficking to Palm Oil Plantations",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Indonesian palm oil sector employs an estimated 4.2 million workers "
            "across 14.3 million hectares. Internal trafficking from Java and NTT "
            "to plantations in Sumatra and Kalimantan. Workers recruited with "
            "promises of IDR 3-5 million/month; arrive to find piece-rate pay of "
            "IDR 80-150 per kg of fresh fruit bunches, earning IDR 1.5-2.5 million. "
            "Debt for transport, housing, and equipment. Child labour (estimated "
            "58,000-75,000 children) documented in harvesting and spraying chemicals."
        ),
        "source": "Amnesty International / Rainforest Action Network / US DOL",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Indofood Palm Oil Child Labour Investigation",
        "exploitation_type": "multiple",
        "sector": "agriculture",
        "summary": (
            "RAN investigation (2016-2019) documented child labour and forced labour "
            "on Indofood Agri Resources plantations in North Sumatra. Children (ages "
            "8-14) carrying heavy loads, applying paraquat without protective "
            "equipment. Workers on 'daily casual' contracts with no benefits. RSPO "
            "suspended Indofood's membership (2019) — first major producer to lose "
            "certification. Indofood subsidiary supplies PepsiCo; PepsiCo ended "
            "sourcing relationship (2020)."
        ),
        "source": "Rainforest Action Network / RSPO / Bloomberg",
    },

    # ── ID: Fishing Sector ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Exploitation of Indonesian Crew on Foreign Fishing Vessels",
        "exploitation_type": "multiple",
        "sector": "fishing",
        "summary": (
            "An estimated 300,000 Indonesian nationals crew foreign fishing vessels "
            "(primarily Chinese, Taiwanese, Thai, South Korean). Documented abuses: "
            "wages of USD 0-150/month (contracted: USD 300-500), 18-22 hour shifts, "
            "physical violence, bodies of deceased stored in freezers, inadequate "
            "food and drinking water. Indonesian government repatriated 1,200 workers "
            "from Chinese fishing vessels (2020-2021) after widespread deaths "
            "reported. Manning agencies in Tegal and Benoa identified as key "
            "recruitment nodes."
        ),
        "source": "Tempo / Greenpeace / IOM Indonesia",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Death of Crew on Chinese Fishing Vessel Long Xin 629 (2020)",
        "exploitation_type": "multiple",
        "sector": "fishing",
        "summary": (
            "Four Indonesian crew members died aboard Chinese fishing vessel Long "
            "Xin 629 operating in the South Atlantic (2020). Crew reported: 20-hour "
            "shifts, drinking water contaminated with engine coolant, rotten food, "
            "physical beatings. Bodies kept in freezer for weeks before burial at "
            "sea. Korean MBC and Indonesian Tempo investigations triggered diplomatic "
            "complaints. China subsequently issued regulations on overseas fishing "
            "vessel labour conditions, but enforcement remains limited."
        ),
        "source": "Tempo / MBC Korea / Indonesian Ministry of Foreign Affairs",
    },

    # ── ID: Regional Trafficking ─────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "ID",
        "title": "Indonesia — Trafficking Hotspots: NTT, NTB, Java",
        "metric": "trafficking_source_regions",
        "value": "NTT, NTB, East Java highest source provinces",
        "summary": (
            "Nusa Tenggara Timur (NTT), Nusa Tenggara Barat (NTB), and East Java "
            "are Indonesia's highest-prevalence trafficking source regions. NTT: "
            "chronic poverty (27% below poverty line), limited education, and "
            "established broker networks to Malaysia and Gulf states. NTB: Lombok "
            "and Sumbawa — trafficking for domestic work and fishing. East Java: "
            "Surabaya as transit hub, recruitment of women for domestic work abroad. "
            "Collectively account for 45-55% of identified trafficking victims."
        ),
        "source": "IOM Indonesia / Ministry of Women's Empowerment",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Pre-Departure Training Centre Exploitation",
        "exploitation_type": "restriction_of_movement",
        "sector": "recruitment",
        "summary": (
            "Indonesian workers destined for overseas placement must complete "
            "pre-departure training at BLK-LN (Balai Latihan Kerja Luar Negeri) "
            "facilities. Documented abuses at private training centres: workers "
            "confined for 2-6 months, passports confiscated during training, "
            "physical punishment, sexual abuse of female trainees, charges of IDR "
            "8-15 million for 'training fees' despite government zero-fee policy. "
            "BP2MI revoked licences of 47 training centres (2019-2022) but many "
            "continue operating informally."
        ),
        "source": "BP2MI / Migrant CARE Indonesia / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "corridor": "ID-HK",
        "title": "Indonesia — Domestic Workers in Hong Kong (Exploitation Patterns)",
        "exploitation_type": "withholding_wages",
        "sector": "domestic_work",
        "summary": (
            "Approximately 160,000 Indonesian domestic workers in Hong Kong (2023). "
            "Despite Hong Kong's Minimum Allowable Wage (HKD 4,870/month in 2023), "
            "workers pay IDR 10-30 million to Indonesian recruitment agencies, "
            "repaid via salary deductions over 5-7 months (illegal under HK law). "
            "Live-in requirement creates isolation. APMM and Amnesty documented "
            "overwork (16+ hours/day), no rest days, physical abuse. Indonesian "
            "consulate receives approximately 1,500 complaints annually."
        ),
        "source": "Amnesty International / APMM / Indonesian Consulate Hong Kong",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "corridor": "ID-SG",
        "title": "Indonesia — Domestic Workers in Singapore",
        "exploitation_type": "debt_bondage",
        "sector": "domestic_work",
        "summary": (
            "Approximately 130,000 Indonesian domestic workers in Singapore. Workers "
            "pay IDR 10-20 million in recruitment fees, repaid via 3-7 months salary "
            "deduction. Singapore's Employment of Foreign Manpower Act excludes "
            "domestic workers from standard labour protections. HOME (NGO) documented: "
            "inadequate food, no days off, confinement to employer's home, and physical "
            "abuse. Singapore's MOM mandated days off from 2013 but allows 'voluntary' "
            "compensation in lieu (commonly coerced by employers)."
        ),
        "source": "HOME Singapore / TWC2 / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Village-Level Recruitment Exploitation",
        "exploitation_type": "deception",
        "sector": "recruitment",
        "summary": (
            "Recruitment in Indonesian source villages operates through informal "
            "brokers (calo) embedded in community networks. Calo approach families "
            "with promises of high wages overseas: IDR 5-10 million/month. Families "
            "sign loan documents (often not fully understood) securing debt against "
            "land or homes. Workers arrive abroad to find different conditions. "
            "Return with debt unpaid results in land seizure. IOM documented this "
            "pattern in NTT, NTB, and Indramayu (West Java). An estimated 60-70% "
            "of overseas placement from these regions involves informal brokers."
        ),
        "source": "IOM Indonesia / Migrant CARE / ILO",
    },
    {
        "type": "statistic",
        "jurisdiction": "ID",
        "title": "Indonesia — Returning Worker Reintegration Challenges",
        "metric": "returning_worker_problems",
        "value": "42% of returning workers report unpaid wages",
        "summary": (
            "IOM survey of 2,500 returning Indonesian migrant workers (2019): 42% "
            "reported unpaid wages, 37% experienced contract substitution, 28% had "
            "passports confiscated, 15% experienced physical violence. Government "
            "reintegration programmes (productive migrant village, DESMIGRATIF) reach "
            "only 3-5% of returnees. Remittances from 9 million overseas Indonesian "
            "workers totalled USD 12.4 billion (2023); exploitation reduces actual "
            "worker income by an estimated 20-35%."
        ),
        "source": "IOM Indonesia / World Bank / BP2MI",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  MYANMAR  (MM)  —  20+ facts                                       ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    # ── MM: Conflict & Displacement ──────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Post-Coup Trafficking Surge (2021 Onwards)",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "Following the military coup (February 2021), trafficking of Myanmar "
            "nationals surged. Economic collapse (GDP contracted 18% in 2021) pushed "
            "hundreds of thousands into irregular migration. IOM estimates 1.2 "
            "million newly displaced internally. Cross-border trafficking to Thailand "
            "increased 40-60% (2021-2022 vs. pre-coup). Scam compound trafficking "
            "to Cambodia, Laos, and Myanmar's border zones recruited heavily among "
            "newly desperate Myanmar youth. Junta's destruction of civil society "
            "eliminated most victim support networks."
        ),
        "source": "IOM / UNHCR / US TIP Report 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "MM",
        "title": "Myanmar — Internal Displacement and Trafficking Vulnerability",
        "metric": "internal_displacement",
        "value": "2.7 million IDPs (2024)",
        "summary": (
            "Myanmar has approximately 2.7 million internally displaced persons "
            "(IDPs) as of 2024, the highest in Southeast Asia. IDP camps in Kachin, "
            "Shan, Rakhine, Kayin, and Chin states have limited humanitarian access. "
            "IDPs — especially women and unaccompanied minors — are highly vulnerable "
            "to trafficking. UNHCR documented recruitment by traffickers operating "
            "around IDP camps, offering jobs in Thailand and China. Estimated 150,000 "
            "IDPs crossed into Thailand since the coup."
        ),
        "source": "UNHCR / OCHA Myanmar",
    },

    # ── MM: Cross-Border Trafficking to Thailand ─────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "corridor": "MM-TH",
        "title": "Myanmar — Cross-Border Trafficking to Thai Fishing and Agriculture",
        "exploitation_type": "debt_bondage",
        "sector": "multiple",
        "summary": (
            "An estimated 3-4 million Myanmar nationals work in Thailand, 1-2 million "
            "undocumented. Key trafficking routes: Myawaddy-Mae Sot (Tak province), "
            "Kawthaung-Ranong, Tachileik-Mae Sai. Workers pay MMK 200,000-500,000 "
            "to brokers. Upon arrival: debt bondage, passport confiscation, "
            "confinement. Sectors: fishing (Samut Sakhon, Songkhla), agriculture "
            "(sugarcane, rubber, poultry), construction (Bangkok), domestic work. "
            "Post-coup: crossing fees increased 50-100% as routes became more "
            "dangerous due to military checkpoints."
        ),
        "source": "IOM / MAP Foundation / Migrant Working Group Thailand",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "corridor": "MM-TH",
        "title": "Myanmar — Fishing Vessel Trafficking (Historical Pattern)",
        "exploitation_type": "restriction_of_movement",
        "sector": "fishing",
        "summary": (
            "Pre-2015 pattern: Myanmar men and boys recruited at border crossings "
            "with promises of factory work in Thailand. Transported to ports (Samut "
            "Sakhon, Songkhla, Pattani) and sold to fishing boat captains. Held at "
            "sea for months to years with no shore leave. Physical violence used "
            "for discipline — 50-59% of trafficked fishers reported beatings. "
            "Workers too sick to work thrown overboard. ILO estimated 17% of "
            "workers in Thai fishing sector in conditions of forced labour (2013 "
            "survey of 596 workers)."
        ),
        "source": "ILO / EJF / LPN Foundation Thailand",
    },

    # ── MM: China Bride Trafficking ──────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "corridor": "MM-CN",
        "title": "Myanmar — Bride Trafficking to China",
        "exploitation_type": "deception",
        "sector": "n/a",
        "summary": (
            "China's gender imbalance (estimated 30-40 million 'surplus' men) drives "
            "demand for trafficked brides from Myanmar, primarily Kachin and Shan "
            "states. Victims recruited with promises of jobs in China; sold to Chinese "
            "men for CNY 20,000-100,000 (USD 3,000-14,000). Johns Hopkins study "
            "(2018): 7,500 women and girls trafficked from Kachin/Shan to China "
            "annually. Victims confined, forced to bear children, subjected to "
            "sexual violence. Returns are rare — many victims cannot locate their "
            "families after years of captivity."
        ),
        "source": "Johns Hopkins / Human Rights Watch / Kachin Women's Association",
    },
    {
        "type": "statistic",
        "jurisdiction": "MM",
        "corridor": "MM-CN",
        "title": "Myanmar — Scale of Bride Trafficking to Yunnan and Beyond",
        "metric": "bride_trafficking_estimate",
        "value": "7,500 per year from Kachin/Shan alone",
        "summary": (
            "Johns Hopkins Bloomberg School of Public Health (2018) estimated 7,500 "
            "women and girls trafficked from Kachin and northern Shan states to "
            "China annually, based on household surveys in IDP camps and conflict "
            "zones. Total from all of Myanmar likely higher. Trafficking intensified "
            "post-coup as economic collapse increased vulnerability. Chinese "
            "provinces of Yunnan, Henan, Anhui, and Shandong identified as "
            "destinations. China launched 'Operation Reunion' but prosecutions "
            "focused on brokers rather than buyers."
        ),
        "source": "Johns Hopkins / KWAT / UNHCR",
    },

    # ── MM: Scam Compounds ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Scam Compound Trafficking to Myanmar Border Zones",
        "exploitation_type": "restriction_of_movement",
        "sector": "cybercrime",
        "summary": (
            "Scam compound operations in Myanmar's border areas (Myawaddy, Tachileik, "
            "Laukkaing) traffick workers from across Asia to conduct online fraud. "
            "Victims — many Myanmar nationals alongside Chinese, Vietnamese, Thai, "
            "and Indian workers — recruited via fake job ads for 'customer service' "
            "or 'tech support'. Compounds guarded, electrified fences, workers "
            "beaten for not meeting scam targets. Ransoms of USD 3,000-20,000 "
            "demanded for release. Compounds operated by Chinese organized crime "
            "with alleged collusion of local ethnic armed groups."
        ),
        "source": "UNODC / UN Human Rights Office / BBC / Al Jazeera",
    },
    {
        "type": "statistic",
        "jurisdiction": "MM",
        "title": "Myanmar — Estimated Scale of Scam Compound Operations",
        "metric": "scam_compound_victims",
        "value": "estimated 120,000 trapped in Myanmar compounds (2023)",
        "summary": (
            "UN Human Rights Office estimated approximately 120,000 people trapped "
            "in scam compound operations in Myanmar as of 2023 (separate from an "
            "estimated 100,000 in Cambodia). Operations concentrated in Myawaddy "
            "(Kayin State) along the Thai border and Laukkaing (Shan State) near "
            "the Chinese border. Revenue from scam operations estimated at USD "
            "billions annually. Victims include nationals from 40+ countries. "
            "Chinese military pressure on Kokang forces led to some compound "
            "closures in late 2023, but operations relocated."
        ),
        "source": "UN Human Rights Office / UNODC Southeast Asia",
    },

    # ── MM: Jade Mining ──────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Forced Labour in Jade Mining (Hpakant)",
        "exploitation_type": "debt_bondage",
        "sector": "mining",
        "summary": (
            "Hpakant jade mines in Kachin State employ an estimated 300,000-400,000 "
            "workers in conditions described by Global Witness as 'the biggest "
            "robbery you've never heard of'. Workers — many internally displaced — "
            "trapped in debt bondage to mine operators. Landslides kill 100+ annually "
            "(174 killed in single landslide, July 2020). Jade industry worth "
            "estimated USD 31 billion/year (2014), 90%+ controlled by military-linked "
            "companies. Workers paid USD 3-10/day; drug addiction (heroin, yaba) "
            "deliberately fostered to maintain control."
        ),
        "source": "Global Witness / Kachin Development Networking Group",
    },

    # ── MM: Rohingya ─────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Rohingya Statelessness and Trafficking Vulnerability",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "Approximately 600,000 Rohingya remain in Rakhine State under severe "
            "movement restrictions, denied citizenship under 1982 Citizenship Law. "
            "An additional 1 million in Bangladesh refugee camps. Statelessness "
            "creates extreme trafficking vulnerability: no legal identity documents, "
            "no right to work, no access to education or healthcare. Trafficking "
            "routes: by sea to Malaysia, Thailand, Indonesia (Andaman Sea route, "
            "peak 2012-2015); overland through Bangladesh to India. UNHCR documented "
            "increasing boat departures from Myanmar and Bangladesh (3,500+ in 2023)."
        ),
        "source": "UNHCR / Fortify Rights / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Rohingya at Sea: Andaman Sea Trafficking Route",
        "exploitation_type": "restriction_of_movement",
        "sector": "multiple",
        "summary": (
            "Rohingya sea crossings from Myanmar/Bangladesh to Malaysia/Indonesia "
            "operated by transnational smuggling-trafficking networks. Boats carry "
            "200-800 people in extreme overcrowding. Voyage lasts 2-4 weeks; "
            "passengers pay USD 800-2,500 (often borrowed from traffickers). "
            "Deaths from dehydration, starvation, and violence common — UNHCR "
            "estimated 1 in 8 died during 2022-2023 crossings. Survivors arriving "
            "in Malaysia held in jungle camps for ransom or sold into forced labour. "
            "2015 Andaman Sea crisis: 5,000+ stranded at sea when Thailand, "
            "Malaysia, and Indonesia refused landing."
        ),
        "source": "UNHCR / IOM / Fortify Rights",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Forced Conscription and Trafficking Post-Coup",
        "exploitation_type": "multiple",
        "sector": "military",
        "summary": (
            "Myanmar military junta (Tatmadaw) enacted conscription law (February "
            "2024) mandating military service for men 18-35 and women 18-27. Fear "
            "of conscription triggered mass emigration: 10,000+ crossed to Thailand "
            "within weeks. Fleeing youth targeted by scam compound recruiters at "
            "borders. Separately, Tatmadaw documented to forcibly recruit child "
            "soldiers (estimated 50,000-70,000 under-18 in armed forces, pre-coup). "
            "Post-coup: both junta and resistance forces documented using "
            "forced labour for porterage and construction."
        ),
        "source": "UN Special Rapporteur on Myanmar / Human Rights Watch / Fortify Rights",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  CAMBODIA  (KH)  —  20+ facts                                     ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    # ── KH: Laws & Regulations ───────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "KH",
        "title": "Cambodia — Law on Suppression of Human Trafficking and Sexual Exploitation (2008)",
        "summary": (
            "Cambodia's primary anti-trafficking statute. Criminalises trafficking "
            "for forced labour and sexual exploitation. Penalties: 7-15 years "
            "imprisonment for basic offences; 15-20 years for aggravated offences "
            "(involving children, officials, or resulting in serious injury). Cross-"
            "border trafficking carries additional penalties. Since 2008, "
            "approximately 1,800 trafficking prosecutions initiated. Conviction "
            "rate: approximately 55%. Critics note prosecutions focus on sex "
            "trafficking while forced labour cases remain underinvestigated."
        ),
        "law": "Law on Suppression of Human Trafficking (2008)",
        "year": 2008,
        "source": "Cambodian Government / US TIP Report",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KH",
        "title": "Cambodia — Sub-Decree 190 on Management of Sending Workers Abroad (2011)",
        "summary": (
            "Regulates private recruitment agencies sending Cambodian workers abroad. "
            "Requires licensing, deposit of USD 100,000 bond, and worker contracts. "
            "Caps placement fees at 10% of first year salary. In practice: workers "
            "pay USD 1,000-3,000 to agencies (far exceeding caps). Agencies operate "
            "sub-agents in rural provinces. Ministry of Labour suspended 30+ agencies "
            "(2014-2023) but suspensions rarely permanent. An estimated 1.2 million "
            "Cambodians work abroad (majority in Thailand and Malaysia)."
        ),
        "source": "Cambodia Ministry of Labour / ILO / LICADHO",
    },

    # ── KH: Scam Compounds ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Sihanoukville Scam Compound Operations",
        "exploitation_type": "restriction_of_movement",
        "sector": "cybercrime",
        "summary": (
            "Sihanoukville, Cambodia's coastal city, hosts dozens of scam compound "
            "operations in repurposed casino buildings and new construction. Workers "
            "trafficked from China, Vietnam, Indonesia, India, and African countries. "
            "Recruited via social media with fake tech job offers (salaries of USD "
            "2,000-5,000/month). Upon arrival: passports confiscated, forced to "
            "conduct crypto/romance scams targeting victims worldwide. Beatings, "
            "electrocution, and sale between compounds documented. Estimated 100,000 "
            "people trapped in Cambodian compounds (UN, 2023)."
        ),
        "source": "UN Human Rights Office / UNODC / BBC / Vice",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Poipet Border Zone Scam Operations",
        "exploitation_type": "multiple",
        "sector": "cybercrime",
        "summary": (
            "Poipet, on the Cambodia-Thailand border, hosts scam compound operations "
            "in the former casino district. Proximity to Thai border facilitates "
            "trafficking: workers lured across from Thailand or transited through "
            "Bangkok. Compounds operated by Chinese nationals with alleged local "
            "official protection. Workers forced to conduct 'pig butchering' "
            "cryptocurrency scams. Cambodian authorities raided some compounds "
            "(2022-2023), rescuing 2,000+ workers, but operations continue. "
            "Workers who escape face arrest for immigration violations."
        ),
        "source": "UNODC / Reuters / The Guardian",
    },
    {
        "type": "statistic",
        "jurisdiction": "KH",
        "title": "Cambodia — Scale of Scam Compound Trafficking",
        "metric": "scam_compound_scale",
        "value": "estimated 100,000 victims in Cambodia (2023)",
        "summary": (
            "UN Human Rights Office estimated 100,000 people trapped in scam "
            "compound operations across Cambodia as of 2023. Victims from 40+ "
            "countries. Scam operations generate estimated USD 7.5-12.5 billion "
            "annually in Cambodia alone. Despite government raids rescuing "
            "approximately 3,000 workers (2022-2023), operations relocate and "
            "expand. Rescued victims often face secondary trauma: detention, "
            "deportation without support, and debt to traffickers. China pressured "
            "Cambodia for crackdowns; Hun Sen government demolished some compounds."
        ),
        "source": "UN Human Rights Office / UNODC / US Institute of Peace",
    },

    # ── KH: Brick Kilns ─────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Debt Bondage in Brick Kilns",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "An estimated 10,000 families work in approximately 500 brick kilns "
            "across Cambodia, concentrated in Phnom Penh's outskirts (Kandal, Kampong "
            "Cham provinces). Families receive advance loans of USD 500-2,000 from "
            "kiln owners; interest rates of 20-30% per year trap families in "
            "perpetual debt. Work involves 12-14 hour days in extreme heat (kilns "
            "reach 1,000+ degrees). Children (estimated 15,000-20,000) work "
            "alongside parents. LICADHO documented families in debt bondage for 5-15 "
            "years. Cambodian courts have not prosecuted kiln owners under "
            "trafficking law."
        ),
        "source": "LICADHO / ILO-IPEC / LSCW",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Child Labour in Brick Kiln Sector",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "ILO-IPEC survey (2016) found 24% of brick kiln workers in Cambodia "
            "were children under 17. Children carry bricks (25-35 kg loads), work "
            "near extreme heat, exposed to dust. School attendance: less than 40% "
            "of brick kiln children attend school. Debt bondage transmits across "
            "generations — children inherit parents' debt. Government National Action "
            "Plan against child labour (2016-2025) targets brick kilns but "
            "enforcement limited: 2 inspectors assigned to 500+ kilns in 2022."
        ),
        "source": "ILO-IPEC / UNICEF / LICADHO",
    },

    # ── KH: Fishing & Thai Border ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "corridor": "KH-TH",
        "title": "Cambodia — Trafficking of Cambodians to Thai Fishing Industry",
        "exploitation_type": "multiple",
        "sector": "fishing",
        "summary": (
            "Cambodian men and boys trafficked to Thai fishing vessels from border "
            "provinces (Banteay Meanchey, Battambang, Poi Pet). Brokers offer THB "
            "10,000-20,000 advance; workers sold to boat captains. Confined at sea "
            "for 6-24 months. LSCW documented: physical violence, unpaid labour, "
            "food deprivation, disposal of sick workers at sea. Post-2015 reforms "
            "reduced but did not eliminate trafficking. An estimated 50,000 "
            "Cambodians remained in Thai fishing sector as of 2020."
        ),
        "source": "LSCW / ILO / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "corridor": "KH-TH",
        "title": "Cambodia — Thai Border Exploitation of Cambodian Workers",
        "exploitation_type": "debt_bondage",
        "sector": "multiple",
        "summary": (
            "An estimated 750,000-1,000,000 Cambodian workers in Thailand (2023), "
            "majority in agriculture, construction, food processing, and fishing. "
            "Border crossing via Poi Pet and O'Smach costs USD 200-500 through "
            "brokers. Workers arrive without documentation, subject to arrest and "
            "deportation. Exploitation pattern: initial debt, passport held by "
            "broker or employer, wages below Thai minimum, threats of deportation "
            "for complaints. Seasonal workers in agriculture most vulnerable due "
            "to short-term employment without contracts."
        ),
        "source": "IOM Cambodia / CLEC / Solidarity Center",
    },

    # ── KH: Domestic Work & Gulf ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "corridor": "KH-MY",
        "title": "Cambodia — Domestic Workers in Malaysia",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "An estimated 50,000-70,000 Cambodian domestic workers in Malaysia. "
            "Recruitment fees: USD 700-1,500 to Cambodian agencies. Workers report: "
            "contract substitution (different employer, lower salary), passport "
            "confiscation, 18-hour workdays, physical abuse, food deprivation. "
            "Cambodia imposed moratorium on domestic worker deployment to Malaysia "
            "(2011-2013) after reports of severe abuse. Post-moratorium bilateral "
            "agreement requires minimum salary of MYR 1,500/month, but enforcement "
            "is minimal. Many workers continue through irregular channels."
        ),
        "source": "LICADHO / IOM Cambodia / CLEC",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Child Trafficking for Begging and Domestic Work",
        "exploitation_type": "deception",
        "sector": "domestic_work",
        "summary": (
            "Children from rural Cambodian provinces trafficked to Phnom Penh, "
            "Siem Reap, and Vietnam for begging, flower/souvenir selling, and "
            "domestic work. Families paid USD 50-200 'advance' by brokers. Children "
            "forced to earn daily quotas (USD 5-15); punished for failure. ECPAT "
            "and UNICEF documented children (ages 5-15) working 10-14 hours daily. "
            "Siem Reap (Angkor Wat tourist area) identified as hotspot for child "
            "exploitation. Government task force rescued 1,200+ children (2018-2023) "
            "but conviction rates remain low."
        ),
        "source": "ECPAT / UNICEF Cambodia / LICADHO",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Fishing Sector Internal Exploitation",
        "exploitation_type": "debt_bondage",
        "sector": "fishing",
        "summary": (
            "Cambodia's Tonle Sap Lake fisheries employ an estimated 50,000 workers "
            "including Vietnamese ethnic minority communities and Khmer families in "
            "debt bondage to boat owners. Workers receive advances for fishing "
            "equipment and food; interest rates of 10-20% per month trap families "
            "across generations. Catch prices set by middlemen below market value. "
            "Children (estimated 30-40% of workforce on Tonle Sap) miss school "
            "during fishing season. Community Legal Education Centre documented "
            "multi-generational debt affecting 3,000+ families."
        ),
        "source": "CLEC / ILO / Cambodian Fisheries Administration",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  VIETNAM  (VN)  —  25+ facts                                       ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    # ── VN: Laws & Regulations ───────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "VN",
        "title": "Vietnam — Law on Vietnamese Workers Working Abroad Under Contract (2020)",
        "summary": (
            "Law No. 69/2020/QH14 replaced the 2006 law. Key improvements: caps "
            "service fees charged by recruitment agencies, requires transparent "
            "contracts in Vietnamese, establishes 'service fee fund' for worker "
            "support abroad, mandatory pre-departure training. Agencies must deposit "
            "VND 1-2 billion (USD 40,000-80,000). Gaps: broker fees at village "
            "level remain unregulated — workers still pay USD 5,000-15,000 to "
            "go to Japan, Korea, or Taiwan. Does not cover workers recruited "
            "informally (estimated 20-30% of outflow)."
        ),
        "law": "Law No. 69/2020/QH14",
        "year": 2020,
        "source": "Vietnamese National Assembly / ILO Vietnam",
    },
    {
        "type": "law",
        "jurisdiction": "VN",
        "title": "Vietnam — Penal Code Article 150 (Trafficking in Persons)",
        "summary": (
            "Vietnamese Penal Code (2015, amended 2017) Article 150 criminalises "
            "trafficking in persons. Penalties: 5-10 years (basic); 8-15 years "
            "(aggravated: organized, professional, 2+ victims, cross-border); "
            "12-20 years or life (resulting in death, 6+ victims). Article 151 "
            "specifically addresses trafficking of persons under 16: 7-12 years "
            "basic, up to life imprisonment for aggravated cases. Vietnam reported "
            "160-200 trafficking convictions annually (2019-2023)."
        ),
        "law": "Penal Code Article 150/151",
        "year": 2015,
        "source": "Vietnamese Penal Code / US TIP Report",
    },

    # ── VN: UK-Bound Trafficking ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-GB",
        "title": "Vietnam — Essex Lorry Tragedy: 39 Deaths (2019)",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "On 23 October 2019, 39 Vietnamese nationals — 31 men and 8 women, aged "
            "15-44 — found dead in a refrigerated trailer in Grays, Essex, UK. "
            "Victims suffocated from lack of oxygen and hyperthermia (temperature "
            "reached 38.5C). Victims had paid GBP 10,000-30,000 each to trafficking "
            "networks for passage from Vietnam to the UK. Route: Vietnam to China "
            "to France/Belgium to UK. Ring leader Gheorghe Nica sentenced to 27 "
            "years; driver Maurice Robinson to 13 years. Vietnamese organizers "
            "also prosecuted. Many victims were from Ha Tinh and Nghe An provinces."
        ),
        "source": "BBC / Old Bailey Trial / Essex Police / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-GB",
        "title": "Vietnam — Cannabis Cultivation Trafficking to UK",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Vietnamese nationals comprise the largest group of trafficking victims "
            "identified in UK National Referral Mechanism (NRM): 1,500+ referrals "
            "in 2022. Primary exploitation: forced labour in cannabis cultivation "
            "('farms') in residential properties. Victims — many minors — trafficked "
            "via China-Russia-Europe route, arrive with GBP 20,000-30,000 debt. "
            "Confined in sealed houses tending cannabis plants. Arrested by police, "
            "many prosecuted as criminals rather than identified as trafficking "
            "victims. Anti-Slavery Commissioner criticized CPS for prosecuting "
            "trafficking victims."
        ),
        "source": "UK Home Office NRM statistics / Anti-Slavery Commissioner / ECPAT UK",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-GB",
        "title": "Vietnam — Nail Salon Exploitation in the UK",
        "exploitation_type": "debt_bondage",
        "sector": "services",
        "summary": (
            "An estimated 100,000 people work in UK nail salons, significant "
            "proportion Vietnamese. Trafficking indicators: workers arrived with "
            "smuggling debts of GBP 20,000-30,000, paid below minimum wage (GBP "
            "2-4/hour, vs. minimum GBP 10.42), housed in overcrowded accommodation "
            "controlled by employers, passports confiscated. Guardian (2017) and "
            "Sky News investigations documented systematic exploitation. UK "
            "government Gangmasters and Labour Abuse Authority (GLAA) conducted "
            "operations rescuing 100+ workers from nail salons (2018-2022)."
        ),
        "source": "GLAA / The Guardian / Sky News / Anti-Slavery International",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-US",
        "title": "Vietnam — Nail Salon Exploitation in the United States",
        "exploitation_type": "withholding_wages",
        "sector": "services",
        "summary": (
            "New York Times investigation (2015) documented widespread exploitation "
            "of Vietnamese and other Asian workers in 2,000+ nail salons in New York "
            "City. Workers paid as little as USD 10/day (below minimum wage), "
            "tips confiscated by owners, health hazards from chemical exposure "
            "without protective equipment. Workers indebted for 'training' fees. "
            "Investigation prompted New York Governor to establish Nail Salon Task "
            "Force and require minimum wage and safety protections through emergency "
            "regulations."
        ),
        "source": "New York Times / NY State Dept of Labor",
    },

    # ── VN: Scam Compound Trafficking ────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "title": "Vietnam — Trafficking to Southeast Asian Scam Compounds",
        "exploitation_type": "restriction_of_movement",
        "sector": "cybercrime",
        "summary": (
            "Vietnamese nationals increasingly trafficked to scam compounds in "
            "Cambodia, Laos, and Myanmar since 2020. Victims recruited via social "
            "media (Zalo, Facebook) with offers of 'tech jobs' at USD 1,500-3,000/"
            "month. Vietnamese Ministry of Public Security reported rescuing 1,800+ "
            "nationals from Cambodian scam compounds (2022-2023). Victims included "
            "university graduates, IT workers, and students. Vietnamese government "
            "negotiated repatriation agreements with Cambodia; 10,000+ Vietnamese "
            "returned from Cambodia in 2023 (not all identified as trafficked)."
        ),
        "source": "Vietnamese Ministry of Public Security / UNODC / VnExpress",
    },

    # ── VN: Japan (TITP) ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-JP",
        "title": "Vietnam — Exploitation Under Japan's Technical Intern Training Programme (TITP)",
        "exploitation_type": "debt_bondage",
        "sector": "multiple",
        "summary": (
            "Vietnam is the largest source country for Japan's TITP, with "
            "approximately 200,000 Vietnamese interns in Japan (2023). Workers pay "
            "USD 5,000-10,000 in fees to Vietnamese sending organizations, creating "
            "debt bondage. Documented abuses: wages below contracted amount, "
            "excessive unpaid overtime, passport confiscation by supervising "
            "organizations, threats of deportation for complaints. US TIP Report "
            "(2023) identified TITP as a programme with significant forced labour "
            "risks. Japan announced replacement of TITP with new 'Ikusei Shuro' "
            "(Training and Employment) system in 2024."
        ),
        "source": "US TIP Report / Japan Times / ILO / Nihon Keizai Shimbun",
    },
    {
        "type": "statistic",
        "jurisdiction": "VN",
        "corridor": "VN-JP",
        "title": "Vietnam — TITP Runaway and Death Statistics",
        "metric": "titp_runaways_deaths",
        "value": "9,006 Vietnamese TITP runaways (2022), 40+ deaths annually",
        "summary": (
            "Japan Immigration Services Agency reported 9,006 Vietnamese technical "
            "interns 'went missing' (absconded) in 2022 — highest among all "
            "nationalities and 60% of total TITP abscondees. Workers flee abusive "
            "conditions but become undocumented, increasing exploitation risk. "
            "An estimated 40+ Vietnamese TITP interns die annually in Japan from "
            "workplace accidents, suicide, and untreated illness. NHK investigation "
            "documented 171 Vietnamese TITP deaths (2012-2021). Workers unable to "
            "change employers under TITP rules."
        ),
        "source": "Japan Immigration Services Agency / NHK / Mainichi Shimbun",
    },

    # ── VN: Korea (EPS) ─────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-KR",
        "title": "Vietnam — Korean Employment Permit System (EPS) Participation",
        "exploitation_type": "withholding_wages",
        "sector": "manufacturing",
        "summary": (
            "Approximately 50,000 Vietnamese workers in South Korea under the EPS "
            "programme (2023). EPS considered a 'model' government-to-government "
            "programme with low official fees (USD 800-1,000). However, Vietnamese "
            "workers report: brokerage fees of USD 3,000-5,000 to 'guarantee' "
            "selection, restricted workplace changes (maximum 3 in 4 years, requiring "
            "employer consent), agricultural and fishing workers excluded from "
            "standard labour protections, dormitory deductions reducing net wages. "
            "Undocumented Vietnamese in Korea estimated at 60,000-80,000."
        ),
        "source": "Korean Ministry of Employment / Amnesty International Korea / ILO",
    },

    # ── VN: Taiwan Fishing ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-TW",
        "title": "Vietnam — Fishing Vessel Exploitation in Taiwan",
        "exploitation_type": "multiple",
        "sector": "fishing",
        "summary": (
            "An estimated 35,000 migrant fishers work on Taiwanese fishing vessels, "
            "significant proportion Vietnamese and Indonesian. Greenpeace Taiwan "
            "(2020) documented: wages of USD 250-450/month (below Taiwanese minimum "
            "for fishers), 14-20 hour shifts, physical violence, passport "
            "confiscation by manning agencies, and one death per month on Taiwanese "
            "distant-water fleet. Key distinction: coastal fishers covered by "
            "Taiwanese labour law; distant-water fishers regulated under weaker "
            "Fisheries Act. Taiwan enacted Distant Water Fisheries Act (2017) but "
            "enforcement at sea is limited."
        ),
        "source": "Greenpeace Taiwan / EJF / Taiwan Control Yuan",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-TW",
        "title": "Vietnam — Forced Labour on Taiwanese Vessel Da Wang (2020)",
        "exploitation_type": "restriction_of_movement",
        "sector": "fishing",
        "summary": (
            "Greenpeace and EJF investigation of Taiwanese longliner Da Wang "
            "documented Vietnamese and Indonesian crew forced to work 20+ hours "
            "daily, wages unpaid for 6 months, crew beaten with metal pipes, sick "
            "crew denied medical care (one worker lost fingers to untreated "
            "infection). Vessel operated in Pacific for 11 months without port "
            "call. Taiwan Fisheries Agency suspended the vessel's licence and fined "
            "the operator, but crew received no compensation. Case highlighted gaps "
            "in flag-state enforcement of ILO Work in Fishing Convention (C188)."
        ),
        "source": "Greenpeace / EJF / Taiwan Fisheries Agency",
    },

    # ── VN: Construction in Gulf ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-AE",
        "title": "Vietnam — Construction Worker Exploitation in the Gulf States",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "Approximately 30,000-50,000 Vietnamese workers in Gulf states (UAE, "
            "Saudi Arabia, Qatar) in construction and manufacturing. Workers pay "
            "USD 2,000-5,000 in recruitment fees to Vietnamese agencies. Upon "
            "arrival: contract substitution (lower wages than agreed), passport "
            "confiscation, 12-hour shifts in extreme heat, crowded dormitories (8-12 "
            "per room). Vietnamese Embassy in UAE receives 500+ complaints annually. "
            "Wage theft common: workers report receiving 60-70% of contracted salary "
            "after deductions for food, accommodation, and 'insurance'."
        ),
        "source": "IOM Vietnam / Vietnamese DOLAB / ILO",
    },

    # ── VN: Recruitment ──────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "VN",
        "title": "Vietnam — Recruitment Fee Burden by Destination Country",
        "metric": "recruitment_fees_by_destination",
        "value": "USD 1,000-15,000 depending on destination",
        "summary": (
            "Average recruitment fees paid by Vietnamese workers: Japan (TITP) USD "
            "5,000-10,000, Taiwan USD 4,000-7,000, South Korea (EPS) USD 800-5,000, "
            "Saudi Arabia/UAE USD 2,000-5,000, Romania/Poland USD 3,000-6,000. ILO "
            "Fair Recruitment Initiative found Vietnamese workers pay among the "
            "highest fees globally relative to expected earnings. Fees financed via "
            "family savings, land mortgages, and high-interest loans (24-60% "
            "annually). Workers from Nghe An, Ha Tinh, and Thanh Hoa provinces "
            "most affected."
        ),
        "source": "ILO / IOM Vietnam / DOLAB",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "title": "Vietnam — Ha Tinh and Nghe An Province Trafficking Vulnerability",
        "exploitation_type": "deception",
        "sector": "multiple",
        "summary": (
            "Ha Tinh and Nghe An provinces in north-central Vietnam are the highest "
            "per-capita source regions for trafficked workers. Factors: poverty "
            "(income 40% below national average), limited local employment, "
            "established migration networks, and aggressive recruitment by brokers. "
            "Both provinces were home to the majority of Essex lorry victims (2019). "
            "Families mortgage homes for children's overseas passage. Province-level "
            "'labour export' targets create perverse incentives for local officials "
            "to facilitate recruitment regardless of conditions at destination."
        ),
        "source": "IOM Vietnam / Reuters / BBC",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-EU",
        "title": "Vietnam — Labour Trafficking to European Countries",
        "exploitation_type": "debt_bondage",
        "sector": "multiple",
        "summary": (
            "Vietnamese nationals trafficked to European countries (UK, Germany, "
            "Czech Republic, Poland, France) for forced labour in cannabis "
            "cultivation, nail salons, garment factories, and agriculture. Route: "
            "Vietnam to China to Russia (overland), then to Europe via Belarus/"
            "Poland or Turkey. Journey takes 2-6 months. Workers arrive with "
            "EUR 15,000-30,000 debt. European authorities struggle with victim "
            "identification: NRM referrals in UK show Vietnamese as #1 nationality, "
            "but many arrested as criminals (cannabis cultivation). ECPAT documented "
            "Vietnamese child victims in 14 European countries."
        ),
        "source": "ECPAT / Europol / UK NRM / La Strada International",
    },
    {
        "type": "statistic",
        "jurisdiction": "VN",
        "title": "Vietnam — Overseas Worker Deployment Statistics",
        "metric": "overseas_deployment",
        "value": "142,779 workers deployed (2023)",
        "summary": (
            "Vietnam's DOLAB (Department of Overseas Labour) reported 142,779 workers "
            "deployed through official channels in 2023: Japan 67,295 (47%), Taiwan "
            "58,620 (41%), South Korea 7,844 (5.5%), others 9,020 (6.5%). Total "
            "Vietnamese workers abroad: approximately 650,000 through formal channels "
            "(an estimated 200,000-300,000 additional through informal channels). "
            "Remittances: USD 14-18 billion/year (2022-2023), approximately 4-5% of "
            "GDP. Government targets 130,000-150,000 deployed annually, creating "
            "pressure on recruitment quality oversight."
        ),
        "source": "DOLAB / World Bank / IOM Vietnam",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  CROSS-CUTTING / REGIONAL FACTS                                    ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    {
        "type": "statistic",
        "jurisdiction": "ASEAN",
        "title": "ASEAN — Estimated Forced Labour in Southeast Asia",
        "metric": "regional_forced_labour",
        "value": "4.8 million victims in Asia-Pacific",
        "summary": (
            "ILO Global Estimates (2022) identified 15.1 million forced labour "
            "victims in Asia-Pacific, 4.8 million in Southeast Asia specifically. "
            "Highest-prevalence countries: Myanmar, Cambodia, and Thailand (rate per "
            "1,000 population). Key sectors: fishing, agriculture, construction, "
            "domestic work, manufacturing. Southeast Asia accounts for approximately "
            "32% of global forced labour in the private economy. ASEAN Convention "
            "Against Trafficking (ACTIP, 2015) ratified by all member states but "
            "implementation varies widely."
        ),
        "source": "ILO Global Estimates of Modern Slavery (2022) / ASEAN Secretariat",
    },
    {
        "type": "law",
        "jurisdiction": "ASEAN",
        "title": "ASEAN Convention Against Trafficking in Persons (ACTIP) — 2015",
        "summary": (
            "First legally binding regional instrument on trafficking in ASEAN. "
            "Signed by all 10 member states (2015), entered into force 2017. "
            "Requires: criminalisation of trafficking, victim protection measures, "
            "mutual legal assistance, and information sharing. Accompanied by ASEAN "
            "Plan of Action Against TIP (APA). Limitations: no independent "
            "monitoring mechanism, no enforcement body, no individual complaints "
            "mechanism. Implementation assessed by voluntary self-reporting."
        ),
        "law": "ACTIP 2015",
        "year": 2015,
        "source": "ASEAN Secretariat / IOM",
    },
    {
        "type": "statistic",
        "jurisdiction": "ASEAN",
        "title": "ASEAN — Intra-Regional Migration Scale",
        "metric": "intra_asean_migration",
        "value": "10.2 million intra-ASEAN migrant workers (2022)",
        "summary": (
            "ILO estimated 10.2 million intra-ASEAN migrant workers in 2022. "
            "Largest flows: Myanmar to Thailand (3-4 million), Indonesia to Malaysia "
            "(1.5-2.5 million), Cambodia to Thailand (750,000-1 million), Philippines "
            "to Malaysia (500,000-800,000), Vietnam to Taiwan/Japan (considered "
            "extra-ASEAN). ASEAN Declaration on the Protection and Promotion of "
            "Rights of Migrant Workers (Cebu Declaration, 2007) remains "
            "non-binding. No ASEAN-wide minimum standards for recruitment fees, "
            "contract terms, or worker protections."
        ),
        "source": "ILO / IOM / ASEAN Secretariat",
    },
    {
        "type": "case_study",
        "jurisdiction": "ASEAN",
        "title": "Southeast Asia — COVID-19 Impact on Migrant Worker Exploitation",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "COVID-19 pandemic intensified migrant worker exploitation across "
            "Southeast Asia: border closures trapped workers with abusive employers, "
            "mass layoffs left workers stranded without resources, factory outbreaks "
            "in overcrowded dormitories (Top Glove: 5,000+ infections, Singapore "
            "dorms: 54,000 infections). Migrant workers excluded from most government "
            "relief programmes. ILO estimated 81 million informal workers in ASEAN "
            "lost 60%+ of income. Post-pandemic: recruitment fees increased, "
            "documentation backlogs created new irregular migration, and scam "
            "compound trafficking surged."
        ),
        "source": "ILO / IOM / Amnesty International",
    },
    {
        "type": "advisory",
        "jurisdiction": "ASEAN",
        "title": "Bali Process — Southeast Asian Regional Framework Against People Smuggling and Trafficking",
        "summary": (
            "The Bali Process on People Smuggling, Trafficking in Persons and "
            "Related Transnational Crime (established 2002) involves 49 countries "
            "and 4 international organizations. Co-chaired by Australia and Indonesia. "
            "Outputs include: Policy Guides on criminalisation, victim identification, "
            "and return/reintegration; Support Office in Bangkok; Regional Support "
            "Offices for counter-trafficking. The Bali Process has facilitated "
            "operational collaboration but lacks binding commitments."
        ),
        "source": "Bali Process Secretariat / IOM",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  ADDITIONAL THAILAND  (TH)  FACTS                                  ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    {
        "type": "statistic",
        "jurisdiction": "TH",
        "title": "Thailand — Migrant Worker Registration Statistics (2023)",
        "metric": "registered_migrant_workers",
        "value": "3.9 million registered migrant workers",
        "summary": (
            "Thailand Ministry of Labour reported approximately 3.9 million "
            "registered migrant workers in 2023: Myanmar (2.5 million), Cambodia "
            "(800,000), Laos (350,000), Vietnam (50,000), others (200,000). "
            "Additional 1-2 million estimated undocumented. Registration "
            "provides work permit, healthcare access, and limited social security. "
            "However, registration is employer-tied, limiting job mobility and "
            "creating structural dependency."
        ),
        "source": "Thailand Ministry of Labour / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "corridor": "LA-TH",
        "title": "Thailand — Exploitation of Lao Workers in Agriculture and Services",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "An estimated 250,000-400,000 Lao workers in Thailand, concentrated "
            "in agriculture (sugarcane, cassava, corn) in northeastern provinces "
            "and domestic work/services in Bangkok. Cross-border movement through "
            "Nong Khai, Mukdahan, and Chiang Khong. Cultural and linguistic "
            "proximity facilitates movement but also exploitation by Thai employers "
            "who assume Lao workers will not access justice systems. Wages typically "
            "THB 200-250/day (below minimum wage), paid monthly with deductions."
        ),
        "source": "ILO / Lao Ministry of Labour / IOM",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "TH",
        "title": "Thailand — EU Yellow Card for IUU Fishing (2015-2019)",
        "summary": (
            "EU issued 'yellow card' warning to Thailand in April 2015 for "
            "insufficient action against IUU fishing, threatening ban on Thai "
            "seafood exports to the EU (worth EUR 650 million annually). Card "
            "prompted: Royal Ordinance on Fisheries, PIPO centres, VMS "
            "installation, crew registration, and labour inspections. Yellow "
            "card lifted January 2019 after reforms. However, labour rights groups "
            "argue reforms primarily addressed IUU concerns while forced labour "
            "protections remain inadequate."
        ),
        "source": "EU DG MARE / Thai Department of Fisheries / EJF",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand — Seafood Processing for Global Supply Chains",
        "exploitation_type": "withholding_wages",
        "sector": "food_processing",
        "summary": (
            "Thailand is the world's third-largest seafood exporter (USD 6.5 "
            "billion, 2022). An estimated 700,000 workers in seafood processing, "
            "80%+ migrants from Myanmar and Cambodia. Processing plants in Samut "
            "Sakhon, Songkhla, and Surat Thani. Labour violations documented: "
            "wages below minimum, forced overtime, locked facilities during shifts, "
            "children in processing sheds. Products exported to US, EU, Japan, and "
            "Australia. US State Department placed Thai seafood on TVPRA List of "
            "Goods Produced by Forced Labor."
        ),
        "source": "US State Dept / ILO / Humanity United",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "TH",
        "title": "Thailand — Thammakaset Chicken Farm Case (SLAPP Lawsuit Pattern)",
        "summary": (
            "Thammakaset Company (poultry farm) filed criminal defamation and "
            "computer crimes charges against 14 Myanmar workers and labour rights "
            "defenders (2016-2020) who reported forced labour violations. Workers "
            "had filed complaint with National Human Rights Commission documenting "
            "wages of THB 175/day (below minimum of THB 300), 20-hour shifts, and "
            "passport confiscation. Company used SLAPP (Strategic Lawsuits Against "
            "Public Participation) to silence critics. Cases against workers "
            "eventually dismissed; incident highlighted Thailand's inadequate "
            "anti-SLAPP protections."
        ),
        "source": "Fortify Rights / Amnesty International / Thai NHRC",
    },
    {
        "type": "contact",
        "jurisdiction": "TH",
        "title": "Thailand — Migrant Worker Hotlines and Support Organizations",
        "summary": (
            "Key support resources for migrant workers in Thailand: Ministry of "
            "Labour Hotline 1506 (Thai, Myanmar, Cambodian, Lao, English), MAP "
            "Foundation (Chiang Mai, migrant worker advocacy), LPN Foundation "
            "(Labour Protection Network, Bangkok/Samut Sakhon), Migrant Working "
            "Group (coalition of 30+ organizations), Foundation for Education "
            "and Development (migrant children's education). IOM Thailand operates "
            "assisted voluntary return programme."
        ),
        "source": "Thailand Ministry of Labour / MAP Foundation / LPN / IOM",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  ADDITIONAL MALAYSIA  (MY)  FACTS                                  ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "BD-MY",
        "title": "Malaysia — Bangladeshi Worker Exploitation in Plantations",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "An estimated 300,000-500,000 Bangladeshi workers in Malaysian "
            "plantations (palm oil, rubber, cocoa). Workers pay BDT 400,000-700,000 "
            "(USD 3,700-6,500) in recruitment fees through chain of dalals "
            "(brokers). Upon arrival: different job than contracted, wages of MYR "
            "800-1,100/month (below minimum of MYR 1,500), passport confiscated, "
            "housed in remote plantation quarters with no transport. Bangladeshi "
            "embassy in Kuala Lumpur handles 5,000+ complaints annually."
        ),
        "source": "Solidarity Center / Tenaganita / Bangladesh MoEWOE",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — WROs Against Malaysian Rubber Glove Companies (Summary)",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "US CBP issued multiple Withhold Release Orders against Malaysian "
            "rubber glove manufacturers: Top Glove (March 2021, modified July "
            "2021 after USD 35M repayment), Supermax (October 2021), Smart Glove "
            "(August 2021), Brightway Holdings (November 2021, revoked March "
            "2023). All based on evidence of ILO forced labour indicators including "
            "debt bondage, passport retention, and restriction of movement. The "
            "industry employed approximately 70,000 migrant workers, predominantly "
            "Bangladeshi and Nepali."
        ),
        "source": "US CBP / Malaysian Rubber Glove Manufacturers Association",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "MY",
        "title": "Malaysia — Employment Act 2022 Amendment (Forced Labour Provisions)",
        "summary": (
            "Malaysia amended the Employment Act 1955 (effective January 2023) with "
            "significant changes: expanded coverage to all employees regardless of "
            "wage threshold (previously MYR 2,000), added 'forced labour' as a "
            "criminal offence (new Section 90B, penalty: MYR 100,000 fine and/or 2 "
            "years imprisonment), extended some protections to domestic workers, "
            "introduced flexible working arrangements. First explicit criminalisation "
            "of forced labour under employment law. However, domestic worker "
            "protections remain weaker than for other workers."
        ),
        "source": "Malaysian Parliament / ILO / Malaysian Bar Council",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "corridor": "ID-MY",
        "title": "Malaysia — Indonesian Worker Deaths in Domestic Employment",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Between 2009-2023, an estimated 300+ Indonesian domestic worker deaths "
            "reported in Malaysia from abuse, workplace accidents, and suicide. "
            "High-profile cases: Nirmala Bonat (2004, burned with iron by employer, "
            "landmark prosecution), Siti Hajar (2012, starved and beaten), Adelina "
            "Lisao (2018, found sleeping with dog, died in hospital — employer "
            "acquitted of murder, convicted of lesser charge). Cases triggered "
            "Indonesian deployment moratoriums and bilateral negotiations."
        ),
        "source": "Tenaganita / BNP2MI / Migrant CARE Indonesia",
    },
    {
        "type": "statistic",
        "jurisdiction": "MY",
        "title": "Malaysia — Migrant Worker Population and Documentation",
        "metric": "migrant_worker_population",
        "value": "2.0 million documented, 2-4 million undocumented (est.)",
        "summary": (
            "Malaysia hosts approximately 2.0 million documented migrant workers "
            "(2023): Indonesia (600,000), Bangladesh (500,000), Nepal (350,000), "
            "Myanmar (200,000), India (150,000), others (200,000). An additional "
            "2-4 million estimated undocumented. Sectors: manufacturing (35%), "
            "construction (25%), agriculture (20%), domestic work (10%), services "
            "(10%). Migrant workers contribute approximately 15% of Malaysian GDP "
            "but excluded from most social protections."
        ),
        "source": "Malaysia Immigration Department / ILO / World Bank",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Outsourced Labour Companies and Exploitation",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Malaysia's outsourced labour model allows companies to hire migrant "
            "workers through licensed 'outsourcing agents' who retain legal "
            "employment status. Workers technically employed by agent, not factory. "
            "System creates accountability gaps: factories disclaim responsibility, "
            "agents control documents and housing. Verité (2020) found 94% of "
            "outsourced workers reported at least one ILO forced labour indicator. "
            "Approximately 40% of migrant workers in manufacturing employed through "
            "outsourced agents."
        ),
        "source": "Verité / ILO / Malaysia Ministry of Human Resources",
    },
    {
        "type": "penalty",
        "jurisdiction": "MY",
        "title": "Malaysia — US Import Bans on Malaysian Products",
        "summary": (
            "US CBP issued WROs against Malaysian companies based on forced labour "
            "evidence: FGV Holdings palm oil (2020, active), Sime Darby palm oil "
            "(2020, modified 2022), Top Glove rubber gloves (2021, revoked 2021), "
            "Supermax rubber gloves (2021, active), Brightway rubber gloves (2021, "
            "revoked 2023). Total trade impact estimated at USD 500 million-1 "
            "billion. WROs prompted industry-wide reforms including recruitment "
            "fee repayments exceeding USD 100 million across the rubber glove sector."
        ),
        "source": "US CBP / US International Trade Commission",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  ADDITIONAL INDONESIA  (ID)  FACTS                                 ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    {
        "type": "law",
        "jurisdiction": "ID",
        "title": "Indonesia — Presidential Instruction 6/2006 on Placement and Protection Reform",
        "summary": (
            "Presidential Instruction No. 6/2006 directed 13 ministries to improve "
            "protection of Indonesian overseas workers. Established inter-ministerial "
            "task force, strengthened pre-departure orientation, created dedicated "
            "legal aid at Indonesian embassies. Later superseded by Law 18/2017 but "
            "represented first high-level recognition of systemic exploitation in "
            "overseas labour placement. Prompted creation of one-stop service centres "
            "in major source provinces."
        ),
        "law": "Presidential Instruction 6/2006",
        "year": 2006,
        "source": "Indonesian Presidential Secretariat / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "corridor": "ID-MY",
        "title": "Indonesia — Trafficking of Indonesian Women to Malaysian Entertainment Sector",
        "exploitation_type": "deception",
        "sector": "services",
        "summary": (
            "Women from West Java, Central Java, and NTB recruited for 'waitress' "
            "or 'factory' jobs in Malaysia. Transported via Batam or direct flights "
            "to Kuala Lumpur. Upon arrival: passports confiscated, forced into "
            "entertainment and sex work in KL, Johor Bahru, and Penang. Debt of "
            "MYR 5,000-15,000 imposed for 'transport and documents'. Indonesian "
            "consulate in KL assisted 800+ trafficking victims (2018-2022). "
            "Joint Indonesia-Malaysia police operations disrupted several networks "
            "but demand-side enforcement minimal."
        ),
        "source": "BNP2MI / Indonesian Consulate KL / Tenaganita",
    },
    {
        "type": "statistic",
        "jurisdiction": "ID",
        "title": "Indonesia — Overseas Worker Deployment Statistics (2023)",
        "metric": "overseas_deployment",
        "value": "297,476 workers deployed (2023)",
        "summary": (
            "BP2MI reported 297,476 Indonesian workers deployed abroad through "
            "official channels in 2023. Top destinations: Hong Kong (64,000), Taiwan "
            "(57,000), Malaysia (45,000), Saudi Arabia (32,000), Singapore (28,000), "
            "South Korea (15,000), Japan (13,000). 60%+ are women, predominantly "
            "in domestic work. An estimated 30-40% of overseas workers deployed "
            "through informal/undocumented channels, outside BP2MI oversight and "
            "protection mechanisms."
        ),
        "source": "BP2MI Annual Report 2023 / World Bank",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Sumatra and Kalimantan Internal Labour Trafficking",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Internal trafficking within Indonesia from eastern islands (NTT, NTB, "
            "Maluku) and Java to plantations in Sumatra and Kalimantan. Workers "
            "recruited by calo (brokers) with advance payment to families of IDR "
            "2-5 million. Transported to remote palm oil and rubber plantations. "
            "Debt bondage for transport, food, and equipment. Workers unable to "
            "leave due to remoteness and debt. Women and girls also trafficked for "
            "domestic work and sexual exploitation in plantation communities. "
            "Ministry of Women's Empowerment identified 400+ cases annually."
        ),
        "source": "IOM Indonesia / Ministry of Women's Empowerment and Child Protection",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "corridor": "ID-SA",
        "title": "Indonesia — Saudi Arabia Domestic Worker Moratorium and Resumption",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Indonesia suspended domestic worker deployment to Saudi Arabia multiple "
            "times: 2009 (after beheading of Ruyati binti Satubi without consular "
            "notification), 2011-2013, 2015. Each moratorium prompted by high-profile "
            "abuse or execution cases. Bilateral agreement signed 2014 set minimum "
            "salary (SAR 1,500/month), mandatory bank account, phone ownership, and "
            "day off. Deployment resumed 2017 but conditions largely unchanged. "
            "An estimated 800,000 Indonesian domestic workers remain in Saudi Arabia. "
            "Saudi Arabia's kafala system limits recourse."
        ),
        "source": "BP2MI / Human Rights Watch / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Tegal and Benoa Manning Agencies (Fishing Crew Recruitment)",
        "exploitation_type": "debt_bondage",
        "sector": "fishing",
        "summary": (
            "Tegal (Central Java) and Benoa (Bali) are Indonesia's primary "
            "recruitment hubs for fishing vessel crew destined for Chinese, "
            "Taiwanese, Thai, and Korean distant-water fleets. Manning agencies "
            "charge workers IDR 5-15 million in fees. Contracts signed in "
            "Indonesian often differ from conditions at sea. Workers report: "
            "agencies withhold 2-3 months salary as 'deposit', passports held "
            "by agency or vessel captain, no insurance despite high mortality "
            "rates. Government suspended 12 manning agencies (2020-2022) but "
            "enforcement is inconsistent."
        ),
        "source": "Greenpeace / Tempo / Indonesian Ministry of Transportation",
    },

    {
        "type": "statistic",
        "jurisdiction": "ID",
        "title": "Indonesia — US TIP Report Tier History",
        "metric": "tip_tier_history",
        "value": "Tier 2 (2014-2024)",
        "summary": (
            "Indonesia TIP tier history: Tier 2 Watch List (2005-2010), Tier 2 "
            "(2011-2012), Tier 3 (2013, brief downgrade due to inadequate "
            "prosecution), Tier 2 (2014-2024). Ongoing concerns: inadequate "
            "prosecution of trafficking offenders (only 80-120 convictions annually), "
            "corruption among labour placement officials, low victim identification "
            "rates, and weak enforcement of zero-fee recruitment policies. "
            "Indonesia identified approximately 600-800 trafficking victims annually "
            "(2020-2023)."
        ),
        "source": "US State Department TIP Reports (2005-2024)",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Tin Mining Exploitation on Bangka-Belitung Islands",
        "exploitation_type": "multiple",
        "sector": "mining",
        "summary": (
            "Bangka and Belitung islands produce approximately 30% of global tin. "
            "An estimated 60,000-100,000 artisanal miners including internal migrants "
            "from Java and Sumatra. Conditions: unregulated mines, child labour "
            "(estimated 5,000-10,000 children), landslides and tunnel collapses "
            "killing 100+ annually, debt bondage to mine operators, no safety "
            "equipment. Tin enters supply chains for electronics (Apple, Samsung, "
            "Intel). Bloomberg investigation (2012) linked exploitation to "
            "solder used in smartphones."
        ),
        "source": "Bloomberg / Friends of the Earth / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "corridor": "ID-TW",
        "title": "Indonesia — Exploitation of Indonesian Fishers on Taiwanese Vessels",
        "exploitation_type": "multiple",
        "sector": "fishing",
        "summary": (
            "Taiwan's distant-water fishing fleet employs approximately 20,000 "
            "Indonesian crew members. Greenpeace (2020) documented systemic abuse: "
            "wages of USD 200-350/month (below contracted amounts), 16-22 hour "
            "shifts, physical violence by Taiwanese captains, passport confiscation "
            "by manning agencies, and deaths from unsafe conditions. Workers "
            "recruited through Indonesian manning agencies in Tegal and Benoa that "
            "charge IDR 5-15 million. No access to Taiwanese labour courts for "
            "distant-water fishers."
        ),
        "source": "Greenpeace / EJF / Tempo",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "corridor": "ID-KR",
        "title": "Indonesia — Korean EPS Workers and Undocumented Overstay",
        "exploitation_type": "withholding_wages",
        "sector": "manufacturing",
        "summary": (
            "Approximately 30,000 Indonesian workers in South Korea under EPS "
            "programme. An additional 25,000-35,000 estimated undocumented "
            "(overstayed visas). EPS workers report: restricted workplace changes, "
            "agricultural workers excluded from Labour Standards Act, dormitory "
            "deductions of KRW 200,000-400,000/month. Undocumented workers "
            "particularly vulnerable: no healthcare access, threat of arrest, "
            "reliance on informal employers. 48 Indonesian workers died in Korea "
            "(2019-2022), many from workplace accidents in small factories."
        ),
        "source": "Korean Ministry of Employment / Amnesty International / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Child Domestic Workers (Pekerja Rumah Tangga Anak)",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "ILO estimated 2.6 million children in domestic work in Indonesia "
            "(2017), many in conditions constituting trafficking. Children — "
            "predominantly girls aged 12-17 — recruited from rural villages to "
            "urban households in Jakarta, Surabaya, and Medan. Work involves: "
            "cooking, cleaning, childcare for 12-18 hours daily, wages of IDR "
            "300,000-800,000/month (USD 20-50), confinement to employer's home, "
            "no access to education. Indonesia has not ratified ILO Convention 189 "
            "on Domestic Workers."
        ),
        "source": "ILO / JALA PRT / UNICEF Indonesia",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  ADDITIONAL MYANMAR  (MM)  FACTS                                   ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    {
        "type": "law",
        "jurisdiction": "MM",
        "title": "Myanmar — Anti-Trafficking in Persons Law (2005)",
        "summary": (
            "Myanmar's primary anti-trafficking statute enacted in 2005. "
            "Criminalises trafficking for forced labour and sexual exploitation "
            "with penalties of 10-life imprisonment. In practice, enforcement has "
            "been minimal: fewer than 50 trafficking convictions per year (pre-coup). "
            "Post-coup (February 2021), the law enforcement apparatus collapsed in "
            "many areas. Myanmar Anti-Trafficking Task Force largely non-functional. "
            "UNODC reports that junta-controlled areas have effectively ceased "
            "anti-trafficking investigations."
        ),
        "law": "Anti-Trafficking in Persons Law 2005",
        "year": 2005,
        "source": "Myanmar Government Gazette / UNODC / US TIP Report",
    },
    {
        "type": "statistic",
        "jurisdiction": "MM",
        "title": "Myanmar — US TIP Report Tier History",
        "metric": "tip_tier_history",
        "value": "Tier 2 Watch List (pre-coup), Tier 3 (2023-2024)",
        "summary": (
            "Myanmar TIP tier history: Tier 2 Watch List (2012-2020), Special Case "
            "(2021, due to coup disruption), Tier 3 (2022-2024). Downgrade "
            "to Tier 3 cited: government complicity in trafficking (military-linked "
            "compounds), failure to investigate, failure to identify and protect "
            "victims, use of forced labour by military (porterage, construction), "
            "and collapse of anti-trafficking efforts post-coup."
        ),
        "source": "US State Department TIP Reports (2012-2024)",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "corridor": "MM-TH",
        "title": "Myanmar — Garment Sector Workers in Mae Sot Special Economic Zone",
        "exploitation_type": "withholding_wages",
        "sector": "manufacturing",
        "summary": (
            "Mae Sot Special Economic Zone on the Thai-Myanmar border hosts "
            "approximately 200 garment factories employing 60,000-80,000 Myanmar "
            "workers. Factories produce for global brands through subcontracting "
            "chains. Workers report: wages of THB 150-250/day (below Thai minimum "
            "of THB 328-354), 12-14 hour shifts, no overtime pay, factory gates "
            "locked during shifts, termination without severance. Workers in SEZ "
            "legally entitled to Thai minimum wage but enforcement is minimal."
        ),
        "source": "ILO / Action Network for Migrants / Clean Clothes Campaign",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Trafficking to Chinese Scam Compounds in Shan State",
        "exploitation_type": "restriction_of_movement",
        "sector": "cybercrime",
        "summary": (
            "Laukkaing in northern Shan State (Kokang Self-Administered Zone) "
            "hosts large-scale scam compound operations. Workers — many Myanmar "
            "nationals recruited domestically — forced to conduct online fraud. "
            "Chinese military operation 'Operation 1027' (October 2023) targeted "
            "these compounds, with Myanmar National Democratic Alliance Army (MNDAA) "
            "capturing Laukkaing. Approximately 44,000 scam workers repatriated to "
            "China (Nov 2023-Feb 2024). Operations partially relocated to "
            "Myawaddy and Tachileik in southern Shan and Kayin states."
        ),
        "source": "UNODC / Reuters / South China Morning Post",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Child Soldiers and Forced Recruitment by Tatmadaw",
        "exploitation_type": "multiple",
        "sector": "military",
        "summary": (
            "Myanmar's military (Tatmadaw) has been documented recruiting child "
            "soldiers since the 1990s. UN verified 8,000+ cases of child "
            "recruitment (2002-2019). Joint Action Plan with the UN (2012) "
            "resulted in discharge of 1,380 children. Post-coup: renewed forced "
            "recruitment including children. Boys as young as 14 taken from IDP "
            "camps, bus stations, and public places. Resistance forces (PDFs) also "
            "documented recruiting minors, though at lesser scale. Myanmar remains "
            "on UN Secretary-General's List of Parties using child soldiers."
        ),
        "source": "UN Special Representative for Children and Armed Conflict / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "corridor": "MM-CN",
        "title": "Myanmar — Kachin Women Trafficked as 'Brides' to China (HRW Investigation)",
        "exploitation_type": "deception",
        "sector": "n/a",
        "summary": (
            "Human Rights Watch report 'Give Us a Baby and We'll Let You Go' (2019) "
            "documented trafficking of Kachin women to China as forced brides. 37 "
            "cases investigated in detail: women and girls (14-40 years old) "
            "promised jobs in China, instead sold to Chinese families. Victims "
            "locked in rooms, raped, and forced to bear children. Those who bore "
            "sons were sometimes allowed to leave but forced to abandon children. "
            "Chinese police rarely investigated buyers. Myanmar police lacked "
            "resources and jurisdiction for cross-border cases."
        ),
        "source": "Human Rights Watch / KWAT",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Forced Labour in Military-Controlled Industries",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "Myanmar military (Tatmadaw) and its economic conglomerates (Myanmar "
            "Economic Corporation, Union of Myanmar Economic Holdings Ltd) use forced "
            "labour in mining, construction, and agriculture. ILO documented forced "
            "labour by military in: road and railway construction, porterage during "
            "military operations, maintenance of military installations, and jade/"
            "ruby mining in Kachin and Shan states. Myanmar was subject to ILO "
            "Article 33 sanctions (2000-2012, 2022-present) for systematic use of "
            "forced labour."
        ),
        "source": "ILO Commission of Inquiry / UN Fact-Finding Mission on Myanmar",
    },

    {
        "type": "case_study",
        "jurisdiction": "MM",
        "corridor": "MM-MY",
        "title": "Myanmar — Rohingya Exploitation in Malaysian Plantations and Construction",
        "exploitation_type": "debt_bondage",
        "sector": "multiple",
        "summary": (
            "Rohingya who reach Malaysia face severe exploitation due to lack of "
            "legal status. Without work permits (UNHCR cards do not grant work "
            "rights), Rohingya work in construction, restaurants, and palm oil "
            "plantations at MYR 30-50/day (below minimum of MYR 1,500/month). "
            "Employers threaten immigration reporting for complaints. Smuggling "
            "debts of MYR 10,000-20,000 create bondage. Fortify Rights documented "
            "Rohingya men held on plantations in Kedah and Kelantan for months "
            "without payment."
        ),
        "source": "Fortify Rights / UNHCR / Amnesty International",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  ADDITIONAL CAMBODIA  (KH)  FACTS                                  ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    {
        "type": "statistic",
        "jurisdiction": "KH",
        "title": "Cambodia — US TIP Report Tier History",
        "metric": "tip_tier_history",
        "value": "Tier 2 Watch List (multiple years)",
        "summary": (
            "Cambodia TIP tier history: Tier 2 Watch List (2012-2014, 2018-2024). "
            "Placed on Tier 2 Watch List for: inadequate prosecution of trafficking "
            "offenders, failure to address complicit officials, insufficient victim "
            "identification among scam compound victims, and treating rescued "
            "trafficking victims as immigration violators. In 2023, Cambodia "
            "investigated 55 trafficking cases and convicted 52 traffickers, an "
            "increase driven by scam compound raids."
        ),
        "source": "US State Department TIP Reports (2012-2024)",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Garment Sector Labour Exploitation",
        "exploitation_type": "withholding_wages",
        "sector": "manufacturing",
        "summary": (
            "Cambodia's garment sector employs approximately 700,000 workers (80% "
            "women) producing for H&M, Zara, Gap, and other global brands. While "
            "not typically classified as trafficking, exploitation is systemic: "
            "minimum wage of USD 200/month (2024) insufficient for basic needs, "
            "forced overtime (60+ hours/week), wage theft through piece-rate "
            "manipulation, fainting episodes due to heat and malnutrition (2,000+ "
            "mass fainting incidents reported 2010-2020), anti-union retaliation "
            "including dismissal and violence."
        ),
        "source": "Clean Clothes Campaign / BSCI / ILO BFC",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Trafficking of Cambodian Women to China as Brides",
        "exploitation_type": "deception",
        "sector": "n/a",
        "summary": (
            "Increasing trafficking of Cambodian women to China for forced marriage "
            "since 2015. Victims recruited from rural Prey Veng, Svay Rieng, and "
            "Kampong Cham provinces with promises of factory work in China. Sold "
            "to Chinese families for USD 10,000-20,000. Victims confined, forced "
            "to bear children, and subjected to domestic servitude. LICADHO "
            "documented 200+ cases (2016-2022). Cambodian authorities repatriated "
            "300+ women from China (2017-2023) through bilateral cooperation."
        ),
        "source": "LICADHO / Chab Dai / IOM Cambodia",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Forced Begging Operations in Phnom Penh",
        "exploitation_type": "restriction_of_movement",
        "sector": "services",
        "summary": (
            "Organized begging networks in Phnom Penh and Siem Reap exploit "
            "Cambodian children, disabled persons, and Vietnamese migrants. Children "
            "rented or purchased from impoverished families for USD 100-500. Forced "
            "to beg at tourist sites, temples, and markets. Daily quotas of USD "
            "5-20; failure results in beatings. Disability deliberately inflicted "
            "in some cases to increase earnings. Friends International and UNICEF "
            "documented networks with 500+ children. Government campaigns urge "
            "tourists not to give to child beggars."
        ),
        "source": "Friends International / UNICEF / ECPAT Cambodia",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "corridor": "KH-VN",
        "title": "Cambodia — Cross-Border Trafficking with Vietnam",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "Bidirectional trafficking between Cambodia and Vietnam. Cambodian women "
            "and girls trafficked to Vietnam for sexual exploitation (Ho Chi Minh "
            "City, Can Tho). Vietnamese men trafficked to Cambodia for construction "
            "and fishing on Tonle Sap. Vietnamese women trafficked to Phnom Penh "
            "entertainment sector. Border crossings at Bavet-Moc Bai and Phnom "
            "Penh-Chau Doc lack systematic screening for trafficking victims. "
            "Joint police operations have been sporadic."
        ),
        "source": "IOM Cambodia / UNIAP / LSCW",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Scam Compound Worker Conditions (Detailed)",
        "exploitation_type": "restriction_of_movement",
        "sector": "cybercrime",
        "summary": (
            "Detailed conditions in Cambodian scam compounds documented by rescued "
            "victims and undercover journalists: workers confined 24/7 in guarded "
            "buildings with CCTV, electrified fences, and armed guards. Working "
            "hours: 14-16 hours/day conducting online scams. Punishments: electric "
            "shocks, beatings, food deprivation, sale to another compound for USD "
            "5,000-15,000. Compound operators charge 'fines' for rule violations "
            "(using personal phone, speaking to outsiders). Some victims coerced "
            "into becoming guards or recruiters themselves."
        ),
        "source": "BBC / Vice / UN Human Rights Office",
    },
    {
        "type": "contact",
        "jurisdiction": "KH",
        "title": "Cambodia — Anti-Trafficking Support Organizations",
        "summary": (
            "Key anti-trafficking organizations in Cambodia: LICADHO (Cambodian "
            "League for the Promotion and Defence of Human Rights), Chab Dai "
            "(coalition of 60+ organizations), LSCW (Legal Support for Children "
            "and Women), IJM (International Justice Mission) Cambodia, Hagar "
            "International (victim rehabilitation), CLEC (Community Legal Education "
            "Centre), Friends International (street children), ECPAT Cambodia. "
            "National Committee for Counter-Trafficking (NCCT) coordinates "
            "government response. Hotline: 1288 (trafficking) and 1280 (child "
            "protection)."
        ),
        "source": "NCCT Cambodia / LICADHO / IJM Cambodia",
    },

    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Construction Sector Exploitation of Migrant and Internal Workers",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "Cambodia's construction boom (particularly Sihanoukville, 2017-2020, "
            "driven by Chinese investment) employed 250,000+ workers. Internal "
            "migrants from rural provinces and Vietnamese workers face: advance "
            "wage bondage, unsafe conditions (200+ workplace deaths reported "
            "2017-2020), wages of USD 8-12/day paid through subcontractors with "
            "deductions, no contracts or insurance. Building collapse at Sihanoukville "
            "construction site (June 2019) killed 28 workers — all internal migrants "
            "sleeping in the building. Labour inspections virtually non-existent."
        ),
        "source": "LICADHO / ILO / Phnom Penh Post",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  ADDITIONAL VIETNAM  (VN)  FACTS                                   ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    {
        "type": "statistic",
        "jurisdiction": "VN",
        "title": "Vietnam — US TIP Report Tier History",
        "metric": "tip_tier_history",
        "value": "Tier 2 Watch List to Tier 2",
        "summary": (
            "Vietnam TIP tier history: Tier 2 Watch List (2010-2013), Tier 2 "
            "(2014-2024). Key ongoing concerns: government-imposed forced labour "
            "(drug rehabilitation centres), inadequate victim identification, "
            "prosecution of trafficking victims (particularly Vietnamese arrested "
            "for cannabis cultivation in UK/Europe), insufficient regulation of "
            "recruitment agencies, and lack of protection for internal trafficking "
            "victims."
        ),
        "source": "US State Department TIP Reports (2010-2024)",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "title": "Vietnam — Forced Labour in Drug Rehabilitation Centres",
        "exploitation_type": "multiple",
        "sector": "manufacturing",
        "summary": (
            "Human Rights Watch documented forced labour in Vietnam's compulsory "
            "drug rehabilitation centres (2011, 2012). An estimated 40,000+ people "
            "detained in 123 centres without due process. Detainees forced to work "
            "in garment production, cashew processing, and other manufacturing "
            "for private companies. Working hours: 8-12 hours/day with no or "
            "minimal wages. Products entered global supply chains. US TIP Report "
            "cites these centres as state-imposed forced labour. Vietnam reduced "
            "number of centres but practice continues."
        ),
        "source": "Human Rights Watch / US TIP Report / ILO CEACR",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-CZ",
        "title": "Vietnam — Exploitation of Vietnamese Workers in Czech Republic",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Approximately 60,000-90,000 Vietnamese reside in Czech Republic, "
            "significant proportion undocumented. Trafficking pattern: workers "
            "recruited in Vietnam with promises of factory jobs at EUR 1,000-2,000/"
            "month. Pay USD 10,000-15,000 to recruiters. Arrive to find undocumented "
            "status, debt bondage, garment sweatshops paying EUR 2-3/hour. La "
            "Strada Czech Republic documented forced labour in nail salons, "
            "restaurants, and cannabis cultivation. Czech police conducted operations "
            "rescuing 100+ Vietnamese workers (2018-2022)."
        ),
        "source": "La Strada Czech Republic / IOM / Czech Police",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-RO",
        "title": "Vietnam — Labour Exploitation in Romania and Eastern Europe",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Vietnam emerged as a significant source of migrant labour to Romania, "
            "Poland, and Hungary (2018-2024). Workers recruited for garment and "
            "construction sectors. Recruitment fees of USD 5,000-8,000. Workers "
            "report: wages below EU minimum, excessive hours, passport retention "
            "by employers, and poor housing. Romanian authorities identified 200+ "
            "Vietnamese workers in exploitative conditions (2022-2023). Some workers "
            "use Romania as transit to higher-wage Western European countries, "
            "increasing trafficking vulnerability."
        ),
        "source": "La Strada Romania / IOM / Europol",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "title": "Vietnam — Internal Trafficking from Ethnic Minority Communities",
        "exploitation_type": "deception",
        "sector": "multiple",
        "summary": (
            "Ethnic minority communities in Vietnam's northern and central highlands "
            "(H'mong, Dao, Ede, Jarai) are disproportionately affected by "
            "trafficking. Vulnerability factors: poverty (minority poverty rate 3x "
            "national average), limited Vietnamese language proficiency, geographic "
            "isolation, lower educational attainment. Women and girls trafficked to "
            "China for forced marriage, urban areas for domestic work and sexual "
            "exploitation. IOM documented 60% of identified Vietnamese trafficking "
            "victims from ethnic minority backgrounds."
        ),
        "source": "IOM Vietnam / CEMA / Blue Dragon Children's Foundation",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "corridor": "VN-JP",
        "title": "Vietnam — Pregnant TITP Workers Forced to Choose: Abort or Return",
        "exploitation_type": "intimidation_and_threats",
        "sector": "multiple",
        "summary": (
            "Vietnamese women in Japan's TITP programme reported being forced to "
            "choose between abortion and deportation when becoming pregnant. "
            "Supervising organizations include pregnancy in 'prohibited activities' "
            "in contracts. NHK investigation (2022) documented cases of women "
            "hiding pregnancies, delivering alone, and abandoning newborns due to "
            "fear of deportation. Japanese law does not explicitly protect pregnant "
            "TITP interns. Several high-profile cases of abandoned infants led to "
            "criminal charges against Vietnamese mothers rather than systemic reform."
        ),
        "source": "NHK / Mainichi Shimbun / Japan Lawyers Network for Foreigners",
    },
    {
        "type": "contact",
        "jurisdiction": "VN",
        "title": "Vietnam — Anti-Trafficking Support Organizations",
        "summary": (
            "Key anti-trafficking organizations in Vietnam: Blue Dragon Children's "
            "Foundation (rescue and rehabilitation, 1,000+ victims assisted), "
            "Pacific Links Foundation (prevention, reintegration), Alliance Anti "
            "Trafic (border monitoring), IOM Vietnam (capacity building, direct "
            "assistance), Hagar International Vietnam (victim support services). "
            "Government hotline: 111 (national child protection and trafficking). "
            "MOLISA (Ministry of Labour) oversees overseas worker protection. "
            "Vietnamese Women's Union active in community-level prevention."
        ),
        "source": "Blue Dragon / Pacific Links / IOM Vietnam / MOLISA",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "title": "Vietnam — Online Recruitment and Social Media Trafficking",
        "exploitation_type": "deception",
        "sector": "cybercrime",
        "summary": (
            "Social media platforms (Facebook, Zalo, TikTok) increasingly used "
            "by traffickers to recruit Vietnamese victims. Fake job advertisements "
            "for 'IT support', 'online marketing', or 'casino customer service' "
            "in Cambodia, Laos, and Myanmar. Vietnamese Ministry of Public Security "
            "reported 4,600+ cases of Vietnamese trafficked via social media "
            "recruitment (2020-2023). Victims skew younger (18-30) and more educated "
            "than traditional trafficking victims. Government blocked 1,200+ "
            "fraudulent recruitment pages but new ones proliferate."
        ),
        "source": "Vietnamese Ministry of Public Security / UNODC / VnExpress",
    },

    # ╔══════════════════════════════════════════════════════════════════════╗
    # ║  ADDITIONAL CROSS-CUTTING / SUPPLY CHAIN FACTS                     ║
    # ╚══════════════════════════════════════════════════════════════════════╝

    {
        "type": "regulation_change",
        "jurisdiction": "ASEAN",
        "title": "ASEAN Consensus on the Protection of Migrant Workers (2017)",
        "summary": (
            "ASEAN Consensus on the Protection and Promotion of the Rights of "
            "Migrant Workers adopted in 2017, replacing non-binding 2007 Cebu "
            "Declaration. Despite being called a 'consensus', it is a non-legally "
            "binding instrument. Key provisions: fair recruitment, decent working "
            "conditions, access to justice, and social protection. Does not "
            "establish minimum wage standards, mandatory contracts, or zero-fee "
            "recruitment. No complaints mechanism or monitoring body. Receiving "
            "states (Thailand, Malaysia, Singapore) resisted binding commitments."
        ),
        "source": "ASEAN Secretariat / ILO / Migrant Forum in Asia",
    },
    {
        "type": "statistic",
        "jurisdiction": "ASEAN",
        "title": "Southeast Asia — Scam Compound Trafficking Regional Scale (2023)",
        "metric": "regional_scam_trafficking",
        "value": "estimated 220,000+ trapped across SEA (2023)",
        "summary": (
            "UNODC and UN Human Rights Office estimated 220,000+ people trapped in "
            "scam compound operations across Southeast Asia in 2023: Cambodia "
            "(100,000), Myanmar (120,000), with additional operations in Laos, "
            "Philippines, and Indonesia. Revenue from scam operations estimated at "
            "USD 40-60 billion annually. Victims from 50+ nationalities. Operations "
            "generate crypto-based 'pig butchering' scams, romance scams, and "
            "investment fraud. Interpol launched Operation Storm Makers II targeting "
            "transnational trafficking networks."
        ),
        "source": "UNODC / UN Human Rights Office / Interpol",
    },
    {
        "type": "case_study",
        "jurisdiction": "ASEAN",
        "title": "Southeast Asia — Seafood Supply Chain Traceability Failures",
        "exploitation_type": "multiple",
        "sector": "fishing",
        "summary": (
            "Despite reforms, forced labour-produced seafood from Southeast Asia "
            "continues entering global supply chains. Mechanisms: transshipment "
            "at sea mixes legal/illegal catch, processing plants co-mingle sourced "
            "fish, certification schemes (MSC, ASC) lack labour auditing capacity, "
            "vessel flags of convenience obscure ownership. Oceana investigation "
            "(2019) found 20%+ of US seafood mislabelled. Thai Union Group "
            "(owner of Chicken of the Sea) committed to blockchain traceability "
            "but implementation covers only 30% of supply chain."
        ),
        "source": "Oceana / EJF / FishWise",
    },
]
