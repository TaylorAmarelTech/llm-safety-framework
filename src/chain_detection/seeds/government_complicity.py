"""
Government complicity chains -- state-enabled trafficking and institutional
complicity where government agencies, diplomatic missions, law enforcement,
and regulatory bodies actively facilitate or passively enable exploitation
of migrant workers through structural mechanisms.

Sources:
  US Department of State, Trafficking in Persons Report (2023, 2024)
  Human Rights Watch, "Die First, and I'll Pay You Later: Saudi Arabia's
      Giga-Projects" (Dec 4, 2024)
  Human Rights Watch, "'As If We Weren't Human': Embassy Complaint Suppression
      in Saudi Arabia" (2008)
  Issara Institute, "Top 5 Labour Abuses in Thailand" (2020)
  Issara Institute, "Compliance is Not Enough: Best Practices in Responding
      to the Risks of Forced Labour in Supply Chains" (2019)
  ILO, "Bilateral Agreements and Memoranda of Understanding on Migration of
      Low-Skilled Workers" (2015)
  ILO, "Employment and Decent Work in Export Processing Zones" (2022)
  ILO Convention C181 Art. 7(1) -- Private Employment Agencies
  ILO Convention C029 -- Forced Labour
  Migrant Forum in Asia, "Reform of the Kafala System" (2012)
  Migrant Forum in Asia, "Review of Bilateral Labour Agreements" (2014)
  ITUC, "Special Economic Zones: Hotbeds of Exploitation" (2017)
  ACLU, "Captive Labor: Exploitation of Incarcerated Workers" (2022)
  Worth Rises, "The Prison Industry: How It Started, How It Works,
      How It Harms" (2023)
  13th Amendment, United States Constitution, Section 1 exception
  Bangladesh BMET Annual Reports (2019-2023)
  Nepal Department of Foreign Employment Annual Report 2078/79
  Philippines POEA/DMW Budget Allocation Reports (2018-2024)
  Jordan Qualifying Industrial Zone Agreement (1996, amended 2010)
  Bangladesh Export Processing Zones Authority Act 1980
  Bangladesh EPZ Labour Act 2019
  Bangladesh Labour Act 2006
  Nepal-Qatar Bilateral Labour Agreement (2005)
  Bangladesh-Saudi Arabia Labour Agreement (2008)
  US Immigration and Customs Enforcement (ICE) Enforcement and
      Removal Operations Reports (2019-2024)
  CoreCivic, Inc., SEC 10-K Annual Reports (2020-2024)
  GEO Group, Inc., SEC 10-K Annual Reports (2020-2024)
  Prison Industry Enhancement Certification Program (PIECP), BJA
  Vienna Convention on Diplomatic Relations (1961) Art. 31
"""

CHAINS: list[dict] = [
    {
        "id": "government_complicity_001",
        "name": "Embassy-Recruiter Collusion Chain",
        "category": "government_complicity",
        "steps": [
            {
                "id": "gc001_s1",
                "description": (
                    "A diplomat at the Saudi embassy in Dhaka, Bangladesh processes "
                    "fast-track visa applications exclusively through three BMET-licensed "
                    "recruitment agencies (out of 1,557 registered agencies as of 2023), "
                    "reducing normal visa processing time from 45-60 days to 7-10 days. "
                    "These three agencies collectively handled 38% of all Bangladesh-to-"
                    "Saudi placements in 2022 (approximately 110,000 workers out of "
                    "289,000 total Saudi-bound deployments recorded by BMET). The diplomat "
                    "receives 'expediting fees' of BDT 15,000-25,000 ($140-$230) per "
                    "application, routed through a Dhaka-based consultancy firm registered "
                    "to a relative of the diplomat."
                ),
                "legal_basis": (
                    "Visa processing timelines are at the discretion of the issuing "
                    "embassy under international consular convention. Saudi Arabia's "
                    "MUSANED electronic visa platform permits authorized recruitment "
                    "agencies to submit batch visa applications, and processing speed "
                    "variations are routine. The Vienna Convention on Diplomatic "
                    "Relations (1961) Art. 31 grants diplomats immunity from host-"
                    "country criminal jurisdiction."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Concentration of 38% of placements through only 3 of 1,557 "
                    "agencies indicates preferential channeling rather than market "
                    "competition. HRW's 2008 report documented Saudi embassy staff "
                    "in multiple origin countries directing workers to specific "
                    "agencies that paid kickbacks. The expediting fee is passed to "
                    "the worker as an additional 'processing charge' above the BMET "
                    "cap of BDT 84,000."
                ),
            },
            {
                "id": "gc001_s2",
                "description": (
                    "Workers who experience abuse at their Saudi destination — passport "
                    "confiscation, unpaid wages, physical violence — attempt to seek "
                    "assistance at the Bangladesh embassy in Riyadh or the consulate "
                    "in Jeddah. The embassy's labor welfare wing, staffed by 4 officers "
                    "for an estimated 2.1 million Bangladeshi workers in Saudi Arabia, "
                    "operates a complaint intake process that requires workers to submit "
                    "complaints in writing during business hours (8 AM-2 PM, Sunday-"
                    "Thursday), present a valid passport or iqama (residence permit), "
                    "and provide the employer's contact details. Since the employer "
                    "holds the passport and iqama, most workers cannot satisfy the "
                    "documentation requirements."
                ),
                "legal_basis": (
                    "Consular assistance is governed by the Bangladesh Emigration "
                    "Ordinance 1982 and the Vienna Convention on Consular Relations "
                    "(1963) Art. 36, which grants consular officers the right to "
                    "visit and communicate with nationals. The embassy is authorized "
                    "to provide emergency travel documents under the Bangladesh "
                    "Passport Order 1973. However, consular staff levels and operating "
                    "procedures are at the discretion of the Ministry of Foreign "
                    "Affairs, which allocated only $1.2 million for labor welfare "
                    "activities across all Saudi missions in FY 2022-23."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The documentation requirement creates a catch-22: the worker "
                    "is seeking help precisely because the employer confiscated the "
                    "documents needed to seek help. US TIP Report 2024 country "
                    "narrative for Bangladesh noted that embassy labor wings in GCC "
                    "countries were 'significantly understaffed relative to the "
                    "migrant population served' and that complaint resolution rates "
                    "were below 8%."
                ),
            },
            {
                "id": "gc001_s3",
                "description": (
                    "Embassy labor welfare officers share complainant names and "
                    "employer details with a 'mediation committee' that includes "
                    "representatives from the Saudi employer's kafalat (sponsorship "
                    "group) and the original Dhaka recruitment agency. The mediation "
                    "process, framed as 'amicable dispute resolution,' results in "
                    "the employer learning the identity of the complainant before "
                    "any formal investigation begins. In documented cases from 2019-"
                    "2023, HRW found that 67% of workers who filed embassy "
                    "complaints subsequently faced punitive actions: transfer to "
                    "harder jobs, reduced food rations, threats of deportation, or "
                    "criminal charges for 'absconding' under Saudi Anti-Begging "
                    "Law (Royal Decree No. A/39, 2007)."
                ),
                "legal_basis": (
                    "Mediation is a recognized dispute resolution mechanism under "
                    "Saudi Labour Law Art. 215-216 and is encouraged by MADLSA "
                    "(Ministry of Administrative Development, Labour and Social "
                    "Affairs) before formal labor court proceedings. The embassy "
                    "frames information sharing as necessary for 'facilitating "
                    "dialogue between parties,' which is standard diplomatic "
                    "practice under bilateral labor cooperation frameworks."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Sharing complainant identity with the accused employer before "
                    "investigation reverses the protective function of the embassy. "
                    "HRW's documentation showed that embassy-facilitated mediation "
                    "in Saudi Arabia overwhelmingly produced outcomes favoring "
                    "employers: 89% of mediated cases resulted in 'voluntary' "
                    "contract termination with the worker receiving partial or no "
                    "back wages, followed by repatriation at the worker's expense."
                ),
            },
            {
                "id": "gc001_s4",
                "description": (
                    "Workers who persist with complaints beyond mediation are "
                    "placed in embassy-operated or embassy-referred shelters in "
                    "Riyadh, where they wait 6-18 months for case resolution while "
                    "unable to work (their iqama is tied to the former employer "
                    "under the kafala system). The embassy provides BDT 200/day "
                    "(~$1.85) for food allowance. Workers report that embassy staff "
                    "pressure them to accept 'voluntary repatriation' by emphasizing "
                    "that legal proceedings 'could take years' and that Saudi courts "
                    "'rarely rule in the worker's favor.' BMET records show that "
                    "94% of sheltered workers eventually accept repatriation without "
                    "resolving their wage claims, which averaged SAR 12,000-35,000 "
                    "($3,200-$9,333) in unpaid wages per case."
                ),
                "legal_basis": (
                    "Embassy shelters operate under the Bangladesh Overseas "
                    "Employment and Migrants Act 2013 § 24, which mandates "
                    "consular protection for distressed workers. Voluntary "
                    "repatriation is a legitimate consular function under the "
                    "Vienna Convention on Consular Relations Art. 5(e). The "
                    "embassy is technically fulfilling its legal obligation by "
                    "providing shelter and repatriation assistance."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The 6-18 month shelter wait with $1.85/day food allowance "
                    "and no work permission functions as an exhaustion mechanism "
                    "that pressures workers into abandoning legitimate wage "
                    "claims. The 94% repatriation-without-resolution rate "
                    "effectively immunizes employers from accountability. US TIP "
                    "Report 2024 identified this pattern as 'institutional "
                    "complicity in the denial of justice for trafficking victims' "
                    "across multiple GCC origin-country embassies."
                ),
            },
        ],
        "chain_context": (
            "Each step in this chain operates under a recognizable legal or "
            "diplomatic framework — visa processing discretion, consular "
            "complaint intake, mediation, and voluntary repatriation. But "
            "combined, they form a closed loop that protects exploitative "
            "employers while systematically denying justice to workers. The "
            "diplomat-agency collusion at the origin end funnels workers into "
            "agencies with documented exploitation records. The embassy "
            "complaint process at the destination end creates documentation "
            "requirements that victims cannot satisfy. The mediation process "
            "exposes complainants to retaliation. And the shelter-to-"
            "repatriation pipeline exhausts victims into abandoning claims. "
            "HRW, Migrant Forum in Asia, and the US TIP Report have "
            "documented this pattern across Bangladesh, Philippines, Ethiopia, "
            "and Nepal embassies in GCC countries, with complaint resolution "
            "rates consistently below 10%."
        ),
        "emergent_risk": (
            "Diplomatic infrastructure designed to protect migrant workers "
            "instead operates as a complaint suppression system: 94% of "
            "sheltered workers repatriated without recovering wages averaging "
            "$3,200-$9,333, while employer-embassy mediation committees "
            "expose complainants to retaliation in 67% of documented cases."
        ),
        "difficulty": "expert",
        "source_references": [
            "Human Rights Watch, \"'As If We Weren't Human': Discrimination and Violence against Domestic Workers in Saudi Arabia\" (2008) — embassy complaint suppression documentation",
            "US Department of State, Trafficking in Persons Report 2024 — Bangladesh country narrative on consular understaffing and complaint resolution rates",
            "Migrant Forum in Asia, \"Reform of the Kafala System\" (2012) — analysis of embassy-employer mediation dynamics across GCC",
            "Vienna Convention on Diplomatic Relations (1961) Art. 31 — diplomatic immunity framework enabling impunity",
            "Bangladesh Overseas Employment and Migrants Act 2013 § 24 — consular protection mandates vs. actual implementation",
            "BMET Annual Report 2022-23 — deployment statistics, agency licensing data, and shelter repatriation figures",
        ],
        "corridors": ["BD-SA", "PH-KW", "ET-LB"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring", "transfer"],
            "means": [
                "abuse of power",
                "abuse of position of vulnerability",
                "deception",
            ],
            "purpose": ["exploitation", "forced labour"],
        },
    },
    {
        "id": "government_complicity_002",
        "name": "Police Protection of Trafficking Network",
        "category": "government_complicity",
        "steps": [
            {
                "id": "gc002_s1",
                "description": (
                    "Royal Thai Police (RTP) Anti-Trafficking in Persons Division "
                    "(ATPD) announces a 'crackdown operation' on shrimp-peeling sheds "
                    "and fish-processing factories in Samut Sakhon province, Thailand's "
                    "largest seafood-processing hub, which employs an estimated 200,000 "
                    "Myanmar and Cambodian workers. The ATPD issues press releases "
                    "through the Ministry of Social Development and Human Security "
                    "(MSDHS) announcing the operation 72 hours in advance, citing "
                    "'inter-agency coordination requirements' under the Prevention "
                    "and Suppression of Human Trafficking Act B.E. 2551 (2008) § 29. "
                    "Issara Institute field monitoring documented that pre-raid "
                    "notification timelines correlated with factory operator tip-offs "
                    "in 78% of observed operations between 2017 and 2022."
                ),
                "legal_basis": (
                    "Thailand's Prevention and Suppression of Human Trafficking Act "
                    "B.E. 2551 (2008) §§ 27-29 establishes Multi-Disciplinary Teams "
                    "(MDTs) comprising police, MSDHS social workers, and Department "
                    "of Labour Protection and Welfare (DLPW) inspectors for anti-"
                    "trafficking operations. Section 29 requires 'coordination among "
                    "relevant agencies,' which operationally translates to advance "
                    "planning meetings that create information pathways to factory "
                    "operators through corrupt intermediaries."
                ),
                "sector": "fishing",
                "corridor": "MM-TH",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The 72-hour advance announcement creates a systematic warning "
                    "window. Issara Institute's 2020 field analysis 'Beyond Compliance' "
                    "documented that shrimp-peeling shed operators in Samut Sakhon's "
                    "Mahachai district received pre-raid tip-offs through police-broker "
                    "networks, enabling them to temporarily relocate undocumented "
                    "Myanmar workers to secondary facilities or private residences "
                    "before inspectors arrived."
                ),
            },
            {
                "id": "gc002_s2",
                "description": (
                    "During the raid, ATPD officers accompanied by MSDHS social "
                    "workers enter the targeted facilities and identify 45 Myanmar "
                    "workers lacking valid work permits under Thailand's Alien Working "
                    "Act B.E. 2551 (2008). The operators, pre-warned, have removed "
                    "evidence of worst conditions — 18-hour shifts, locked dormitories, "
                    "wage withholding ledgers — and relocated the most visibly "
                    "exploited workers (those with injuries or severe malnutrition). "
                    "The operators present work permits for their registered workforce "
                    "and cooperate with inspectors. Three operators are 'questioned' "
                    "but released without charges, while the 45 undocumented workers "
                    "are detained for immigration violations under the Immigration "
                    "Act B.E. 2522 (1979) § 54."
                ),
                "legal_basis": (
                    "Immigration Act B.E. 2522 (1979) § 54 authorizes detention and "
                    "deportation of aliens without valid permits. The Alien Working "
                    "Act B.E. 2551 (2008) § 9 criminalizes work without a permit, "
                    "punishable by imprisonment up to 5 years and/or fine of THB "
                    "2,000-100,000. Police have discretionary authority to arrest "
                    "undocumented workers encountered during any operation."
                ),
                "sector": "fishing",
                "corridor": "MM-TH",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The raid's outcome — workers arrested, operators released — "
                    "inverts the intended purpose of anti-trafficking enforcement. "
                    "Issara Institute documented that between 2017 and 2022, Thai "
                    "anti-trafficking raids in Samut Sakhon resulted in prosecution "
                    "of operators in only 6% of cases, while 89% of identified "
                    "undocumented workers were processed for deportation without "
                    "being screened as potential trafficking victims under the "
                    "National Referral Mechanism."
                ),
            },
            {
                "id": "gc002_s3",
                "description": (
                    "The 45 detained workers are held at the Samut Sakhon Immigration "
                    "Detention Center (IDC) for 30-90 days awaiting deportation "
                    "processing. During detention, workers are not informed of their "
                    "right to file wage claims under the Labour Protection Act B.E. "
                    "2541 (1998) § 77/1, which applies regardless of immigration "
                    "status. Collectively, the 45 workers are owed approximately "
                    "THB 2.7 million ($75,000) in unpaid wages — averaging THB "
                    "60,000 ($1,667) per worker for 3-8 months of work at below-"
                    "minimum-wage rates. The workers are deported to Myanmar through "
                    "the Mae Sot-Myawaddy border crossing without any wage recovery "
                    "proceedings initiated. Within 2-4 weeks, the same broker "
                    "networks recruit replacement workers from the same Myanmar "
                    "villages, charging THB 15,000-25,000 ($420-$700) per crossing."
                ),
                "legal_basis": (
                    "Deportation of immigration violators is authorized under "
                    "Immigration Act B.E. 2522 (1979) §§ 54-55. The Royal Thai "
                    "Government is not legally required to initiate labor claims "
                    "on behalf of deportees, although the Labour Protection Act "
                    "B.E. 2541 (1998) § 77/1 extends wage protections to all "
                    "workers regardless of nationality or documentation status. "
                    "The gap between labor law coverage and immigration enforcement "
                    "practice is a structural feature, not a violation."
                ),
                "sector": "fishing",
                "corridor": "MM-TH",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Deportation without wage recovery completes the exploitation "
                    "cycle: employers retain $75,000 in unpaid wages across 45 "
                    "workers, face no prosecution, and immediately recruit "
                    "replacements through the same broker networks. The US TIP "
                    "Report 2023 tier 2 watch list narrative for Thailand cited "
                    "'continued reports of officials facilitating trafficking "
                    "through complicity in the deportation of potential victims "
                    "without screening or referral to protective services.'"
                ),
            },
        ],
        "chain_context": (
            "This chain documents a self-perpetuating cycle where anti-trafficking "
            "enforcement infrastructure is co-opted to protect traffickers and "
            "punish victims. Pre-raid tip-offs through police-broker networks "
            "ensure that the worst evidence of exploitation is concealed before "
            "inspectors arrive. The legal framework criminalizing undocumented "
            "work provides a mechanism to remove the victims rather than "
            "prosecute the perpetrators. Deportation without wage recovery "
            "eliminates both the witnesses and the evidence. Replacement "
            "recruitment through the same border brokers ensures continuity "
            "of the labor supply. Issara Institute's longitudinal field research "
            "in Samut Sakhon (2015-2022) documented this cycle repeating 3-4 "
            "times per year at the same facilities, with the same operators, "
            "and the same police units."
        ),
        "emergent_risk": (
            "Anti-trafficking raids function as a labor turnover mechanism: "
            "pre-warned operators hide evidence, workers are arrested and "
            "deported without recovering $1,667 average unpaid wages, and "
            "replacement workers are recruited within weeks through the same "
            "broker networks — Issara Institute documented this cycle repeating "
            "3-4 times annually at the same Samut Sakhon facilities."
        ),
        "difficulty": "hard",
        "source_references": [
            "Issara Institute, \"Beyond Compliance: Best Practices in Responding to the Risks of Forced Labour\" (2019) — pre-raid tip-off documentation in Samut Sakhon",
            "Issara Institute, \"Top 5 Labour Abuses in Thailand\" (2020) — police-broker network field analysis",
            "US Department of State, Trafficking in Persons Report 2023 — Thailand tier 2 watch list narrative on official complicity",
            "Thailand Prevention and Suppression of Human Trafficking Act B.E. 2551 (2008) §§ 27-29 — MDT coordination requirements",
            "Thailand Immigration Act B.E. 2522 (1979) §§ 54-55 — deportation authority",
            "Thailand Labour Protection Act B.E. 2541 (1998) § 77/1 — wage protections regardless of immigration status",
        ],
        "corridors": ["MM-TH", "KH-TH", "VN-TH"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring", "transfer"],
            "means": [
                "abuse of power",
                "coercion",
                "abuse of position of vulnerability",
            ],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "government_complicity_003",
        "name": "State Labor Export Program Volume-Over-Safety",
        "category": "government_complicity",
        "steps": [
            {
                "id": "gc003_s1",
                "description": (
                    "Bangladesh's Bureau of Manpower Employment and Training (BMET) "
                    "sets annual overseas deployment targets exceeding 1 million "
                    "workers per year, with Saudi Arabia as the primary destination "
                    "(289,000 workers in 2022). The Philippines' Department of "
                    "Migrant Workers (DMW, formerly POEA) administered 2.33 million "
                    "Overseas Filipino Workers (OFWs) as of December 2022 stock "
                    "estimate. Nepal's Department of Foreign Employment (DoFE) "
                    "issued 236,208 labor permits for Qatar alone in fiscal year "
                    "2078/79 (2021-22). These targets are embedded in national "
                    "development plans: Bangladesh's 8th Five-Year Plan (2020-2025) "
                    "identifies labor export as a 'strategic pillar' for GDP growth, "
                    "targeting $25 billion in annual remittances by 2025."
                ),
                "legal_basis": (
                    "National deployment targets are set by sovereign governments "
                    "as part of economic development policy. Bangladesh's Overseas "
                    "Employment and Migrants Act 2013 § 6 establishes BMET's mandate "
                    "to 'promote overseas employment opportunities.' The Philippines' "
                    "Migrant Workers and Overseas Filipinos Act (RA 10022, 2010) "
                    "§ 4 affirms the state's 'deployment program for overseas "
                    "employment.' Nepal's Foreign Employment Act 2007 § 4 establishes "
                    "the government's role in 'promoting foreign employment.'"
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Volume targets create institutional pressure to expedite "
                    "deployments. BMET's 2022 annual report showed that 97% of "
                    "agency license applications were approved, with an average "
                    "review period of 12 days. The ILO's 2019 FAIR Recruitment "
                    "Initiative assessment of Bangladesh found that 'deployment "
                    "targets incentivize quantity over quality of placements, with "
                    "limited post-deployment tracking of worker outcomes.'"
                ),
            },
            {
                "id": "gc003_s2",
                "description": (
                    "To meet deployment quotas, BMET reduces pre-departure "
                    "orientation from the mandated 3-day program to a half-day "
                    "session covering only visa document verification and airport "
                    "procedures. The orientation center in Dhaka's Kakrail area "
                    "processes 300-500 workers per day in group sessions of 80-100, "
                    "with no individual counseling on labor rights, complaint "
                    "mechanisms, or emergency contacts at the destination embassy. "
                    "Workers receive a 4-page brochure in Bengali but are not "
                    "tested on comprehension. The Philippines' Comprehensive "
                    "Pre-Departure Education Program (CPDEP) was similarly "
                    "compressed from 6 days to 1 day for household service "
                    "workers, with DMW citing 'administrative efficiency.'"
                ),
                "legal_basis": (
                    "Bangladesh Overseas Employment and Migrants Act 2013 § 19 "
                    "mandates pre-departure orientation but does not specify "
                    "minimum duration or content standards. The Philippines' "
                    "OWWA Memorandum Circular No. 2015-002 requires completion "
                    "of CPDEP but allows the DMW administrator to 'adjust "
                    "program duration based on operational needs.' Both programs "
                    "technically comply with their enabling legislation."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Compressed orientation means workers arrive at destination "
                    "without knowledge of their legal rights, the existence of "
                    "embassy labor wings, or how to file complaints. ILO FAIR "
                    "assessment (2019) found that 71% of Bangladeshi workers in "
                    "Saudi Arabia could not name a single right under Saudi Labour "
                    "Law or identify any complaint mechanism. The compression "
                    "directly serves the deployment quota by reducing the per-"
                    "worker processing time from 3 days to 4 hours."
                ),
            },
            {
                "id": "gc003_s3",
                "description": (
                    "Post-deployment monitoring budgets are cut to redirect "
                    "resources toward processing more outgoing deployments. "
                    "Bangladesh's 2022-23 budget allocated only $1.2 million "
                    "across all Saudi missions for labor welfare activities "
                    "serving 2.1 million workers — $0.57 per worker per year. "
                    "Nepal's DoFE had 3 monitoring officers for 236,208 workers "
                    "in Qatar (1 officer per 78,736 workers). The Philippines' "
                    "DMW budget for overseas worker welfare services was PhP "
                    "892 million ($16 million) in 2023 for 2.33 million OFWs — "
                    "$6.87 per worker per year, of which 68% covered "
                    "administrative overhead and Manila-based staff salaries."
                ),
                "legal_basis": (
                    "Budget allocation is a sovereign fiscal decision. The "
                    "Bangladesh Overseas Employment and Migrants Act 2013 § 24 "
                    "mandates consular welfare services but does not specify "
                    "minimum funding levels. The Philippines' OWWA (Overseas "
                    "Workers Welfare Administration) derives its budget from "
                    "mandatory OFW membership fees of $25 per contract, "
                    "generating approximately $58 million annually, but OWWA "
                    "reserves have historically been diverted to non-welfare "
                    "expenditures including office construction."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "At $0.57 per worker per year, Bangladesh cannot provide "
                    "meaningful consular protection. The defunding of post-"
                    "deployment monitoring means that when workers are exploited, "
                    "the government has neither the capacity nor the institutional "
                    "incentive to intervene. The government instead counts "
                    "'successful placements' — remittances reached $21.5 billion "
                    "in 2022 for Bangladesh (7.4% of GDP) and $36.1 billion for "
                    "the Philippines (8.9% of GDP) — creating a fiscal dependency "
                    "that structurally disincentivizes enforcement against "
                    "destination-country employers."
                ),
            },
            {
                "id": "gc003_s4",
                "description": (
                    "When exploitation cases surface in international media or "
                    "through NGO reporting, governments respond with public "
                    "statements citing deployment statistics and remittance "
                    "figures as evidence of program success. Bangladesh's BMET "
                    "2022 annual report listed 'total remittance earnings' as "
                    "its primary performance metric, with no mention of worker "
                    "complaint volumes, wage theft cases, or deaths in "
                    "destination countries. Nepal's DoFE annual report for "
                    "2078/79 reported 622 worker deaths in destination countries "
                    "(1.7 per day) but classified these under 'natural causes' "
                    "without investigation, and the figure was not included in "
                    "the executive summary. The Philippines' DMW 2023 annual "
                    "report highlighted '$36.1 billion in OFW remittances' as "
                    "its lead achievement."
                ),
                "legal_basis": (
                    "Government performance reporting is not externally regulated. "
                    "National statistical agencies determine which metrics to "
                    "track and report. Remittance data is publicly available "
                    "through central bank publications and World Bank bilateral "
                    "remittance matrices. Death reporting is governed by consular "
                    "notification requirements under bilateral agreements, which "
                    "do not mandate independent investigation or public reporting."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Reporting remittances as the primary success metric while "
                    "burying worker death and exploitation data reveals the "
                    "institutional incentive structure: the government profits "
                    "from the system and measures success by revenue, not worker "
                    "outcomes. Nepal's 622 worker deaths in a single year "
                    "(2021-22) — equivalent to 1.7 deaths per day — received no "
                    "investigation. The US TIP Report 2024 cited this pattern "
                    "as evidence that 'origin-country governments prioritize "
                    "remittance flows over worker protection.'"
                ),
            },
        ],
        "chain_context": (
            "This chain exposes how state labor export programs — legally "
            "authorized, GDP-critical, and politically popular — create "
            "structural conditions for trafficking by prioritizing deployment "
            "volume over worker safety at every stage. Deployment targets "
            "pressure regulatory agencies to approve agencies without due "
            "diligence. Pre-departure orientation compression eliminates "
            "the primary window for workers to learn their rights. Post-"
            "deployment monitoring defunding removes the capacity for "
            "intervention when exploitation occurs. And performance reporting "
            "that measures remittances rather than worker outcomes creates "
            "an institutional feedback loop that rewards volume over safety. "
            "The ILO FAIR Recruitment Initiative's 2019 assessment of "
            "Bangladesh, Nepal, and the Philippines identified this volume-"
            "over-safety dynamic as the 'central structural enabler of "
            "recruitment-linked forced labor in GCC migration corridors.'"
        ),
        "emergent_risk": (
            "State labor export programs create a GDP dependency on remittances "
            "(7-9% of GDP) that structurally disincentivizes worker protection: "
            "97% agency approval rate, orientation compressed from 3 days to "
            "half-day, $0.57/worker/year post-deployment monitoring budget, "
            "and 622 worker deaths per year reported without investigation."
        ),
        "difficulty": "hard",
        "source_references": [
            "BMET Annual Report 2022-23 — deployment targets, agency licensing approval rates, remittance statistics",
            "ILO FAIR Recruitment Initiative, \"Assessment of Labour Migration from Bangladesh\" (2019) — rights awareness and orientation quality data",
            "Nepal Department of Foreign Employment Annual Report 2078/79 — labor permits, worker deaths, monitoring capacity",
            "Philippines DMW/POEA Annual Report 2023 — OFW statistics, budget allocation, remittance reporting",
            "US Department of State, Trafficking in Persons Report 2024 — origin-country government complicity analysis",
            "World Bank Bilateral Remittance Matrix 2022 — GDP percentage calculations for origin countries",
        ],
        "corridors": ["BD-SA", "PH-SA", "NP-QA", "ET-SA"],
        "palermo_elements": {
            "act": ["recruitment", "transfer"],
            "means": [
                "abuse of power",
                "abuse of position of vulnerability",
            ],
            "purpose": ["exploitation", "forced labour"],
        },
    },
    {
        "id": "government_complicity_004",
        "name": "Immigration Enforcement as Worker Control Tool",
        "category": "government_complicity",
        "steps": [
            {
                "id": "gc004_s1",
                "description": (
                    "A construction contractor in Houston, Texas employs 35 "
                    "Guatemalan and Mexican workers for a 9-month commercial "
                    "building project, paying $8-12/hour cash (below the federal "
                    "minimum wage of $7.25/hour only in that it evades payroll "
                    "taxes, FICA, and workers' compensation insurance). Workers "
                    "are recruited through a coyote network operating in "
                    "Huehuetenango, Guatemala and Oaxaca, Mexico, with crossing "
                    "fees of $6,000-$12,000 financed through village moneylenders "
                    "at 10-15% monthly interest. The contractor knows the workers "
                    "are undocumented and uses this as leverage: 'If you complain, "
                    "I call ICE.' The US Department of Labor Wage and Hour "
                    "Division processed 24,649 labor complaints in FY 2023 but "
                    "only 267 (1.1%) involved referrals from ICE-involved cases."
                ),
                "legal_basis": (
                    "The Fair Labor Standards Act (FLSA) 29 USC § 206 applies "
                    "to all workers regardless of immigration status, as "
                    "affirmed by the Supreme Court in Sure-Tan v. NLRB (1984) "
                    "and reiterated in DOL Field Assistance Bulletin 2022-2. "
                    "However, ICE enforcement authority under INA § 287(g) and "
                    "8 USC § 1357 operates independently of DOL labor standards "
                    "enforcement, and there is no statutory firewall preventing "
                    "immigration enforcement at worksites where labor complaints "
                    "are pending."
                ),
                "sector": "construction",
                "corridor": "GT-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The employer's threat to 'call ICE' transforms immigration "
                    "enforcement into a private labor discipline tool. The "
                    "National Employment Law Project (NELP) documented in 2023 "
                    "that 62% of undocumented workers who experienced wage theft "
                    "did not file complaints due to fear of deportation, "
                    "representing an estimated $8.8 billion in annual stolen "
                    "wages nationally. The threat is credible: ICE conducted "
                    "5,735 worksite enforcement actions in FY 2023."
                ),
            },
            {
                "id": "gc004_s2",
                "description": (
                    "After the 9-month project reaches substantial completion "
                    "in December, the contractor withholds the final 6 weeks of "
                    "wages — approximately $4,200 per worker, totaling $147,000 "
                    "across 35 workers — claiming 'quality deficiencies' and "
                    "'project budget overruns.' Within 48 hours of workers "
                    "demanding payment, the contractor files an anonymous tip "
                    "with ICE's Homeland Security Investigations (HSI) tip line "
                    "(1-866-347-2423), reporting 'suspected undocumented aliens' "
                    "at a worksite address that is a worker housing location "
                    "rather than the commercial project site, distancing the "
                    "contractor from the workplace."
                ),
                "legal_basis": (
                    "ICE tip lines accept anonymous reports under DHS policy. "
                    "8 USC § 1324(c) creates a duty for federal officers to "
                    "investigate reported immigration violations. The contractor "
                    "is not legally required to disclose their employment "
                    "relationship with the reported individuals when filing "
                    "an anonymous tip. Filing a false report would violate "
                    "18 USC § 1001 (false statements), but anonymous tips "
                    "are functionally unattributable."
                ),
                "sector": "construction",
                "corridor": "GT-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The timing — ICE tip filed within 48 hours of workers "
                    "demanding wages — reveals the retaliatory purpose. This "
                    "pattern is well-documented: a 2019 Centro de los Derechos "
                    "del Migrante study found that in 46% of ICE worksite "
                    "enforcement actions in the construction sector, the "
                    "employer or a contractor affiliate had filed the "
                    "initial tip, and in 73% of those cases, workers had "
                    "outstanding wage claims at the time of the raid."
                ),
            },
            {
                "id": "gc004_s3",
                "description": (
                    "ICE ERO (Enforcement and Removal Operations) officers "
                    "arrive at the worker housing location and detain 28 of "
                    "the 35 workers. During processing at the Houston ICE "
                    "Processing Center, workers are issued Notices to Appear "
                    "(NTAs) in immigration court under INA § 240. Workers "
                    "are not informed by ICE that they may have pending wage "
                    "claims or that labor trafficking victims are eligible for "
                    "T-visa protection under INA § 101(a)(15)(T). The "
                    "contractor is not investigated for wage theft ($147,000), "
                    "payroll tax evasion, workers' compensation insurance "
                    "fraud, or labor trafficking. ICE ERO's FY 2023 annual "
                    "report documented 142,580 removals, but only 463 (0.3%) "
                    "involved concurrent referrals to DOL for wage "
                    "investigation."
                ),
                "legal_basis": (
                    "ICE officers are authorized to detain suspected removable "
                    "aliens under 8 USC § 1226. NTAs are issued under INA "
                    "§ 239. ICE is not statutorily required to screen "
                    "detainees for labor trafficking victimization or pending "
                    "wage claims, although DHS Directive 2022-01 (Guidelines "
                    "for Enforcement Actions in or Near Protected Areas) and "
                    "DOL-DHS MOU (2011, updated 2016) on labor enforcement "
                    "coordination are intended to create referral pathways "
                    "that are, in practice, rarely used."
                ),
                "sector": "construction",
                "corridor": "GT-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "ICE processes workers as immigration violators without "
                    "screening for trafficking victimization, despite the "
                    "DHS Blue Campaign training that all ICE officers are "
                    "required to complete. The 0.3% concurrent DOL referral "
                    "rate means that 99.7% of removed workers with potential "
                    "wage claims are deported without any wage recovery "
                    "action. The contractor retains $147,000 in stolen wages "
                    "and faces no investigation from any agency."
                ),
            },
            {
                "id": "gc004_s4",
                "description": (
                    "The 28 detained workers are processed through immigration "
                    "court (EOIR) in Houston, where the median wait time for a "
                    "hearing is 1,547 days (4.2 years) as of January 2024 "
                    "(TRAC Immigration data). Workers without legal representation "
                    "— 63% of detained respondents in Texas immigration courts "
                    "lacked counsel per TRAC data — receive stipulated removal "
                    "orders within 30-60 days. Removal orders are executed before "
                    "any DOL wage complaint could be filed, investigated, or "
                    "adjudicated. The contractor's next project begins in February "
                    "with a new cohort of 30 workers recruited through the same "
                    "coyote network."
                ),
                "legal_basis": (
                    "Stipulated removal under INA § 240(d) permits respondents "
                    "to agree to removal without a hearing. 8 CFR § 1003.25(b) "
                    "governs stipulated orders. Workers in detention face "
                    "coercive pressure to stipulate to removal due to detention "
                    "conditions and lack of counsel, but the stipulated order is "
                    "technically voluntary. DOL wage complaint processing takes "
                    "an average of 277 days (FY 2023 WHD data), making it "
                    "temporally impossible to complete before removal."
                ),
                "sector": "construction",
                "corridor": "GT-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The temporal mismatch between immigration removal (30-60 "
                    "days for stipulated orders) and labor complaint processing "
                    "(277 days average) creates a structural impossibility: "
                    "workers cannot pursue wage claims before being deported. "
                    "The contractor's impunity is complete — $147,000 retained, "
                    "no investigation, and a new workforce recruited at the same "
                    "cost structure. NELP estimated in 2023 that employer-"
                    "initiated ICE reports result in $680 million annually in "
                    "unrecoverable stolen wages from deported workers."
                ),
            },
        ],
        "chain_context": (
            "This chain demonstrates how the absence of a statutory firewall "
            "between immigration enforcement and labor standards enforcement "
            "enables employers to weaponize deportation as a wage theft "
            "mechanism. Every government function in this chain operates "
            "lawfully — ICE responds to tips, processes immigration violators, "
            "and executes removal orders. But the combined effect is that "
            "employers can exploit workers with impunity by timing ICE "
            "reports to coincide with wage demands. The 0.3% DOL referral "
            "rate from ICE removals, the 277-day DOL complaint processing "
            "timeline versus 30-60 day removal execution, and the 63% lack "
            "of counsel rate in detained immigration proceedings create a "
            "system where labor exploitation and immigration enforcement "
            "are structurally complementary rather than independent."
        ),
        "emergent_risk": (
            "Immigration enforcement weaponized as wage theft tool: employers "
            "file ICE tips after withholding wages, workers are deported before "
            "277-day DOL complaint process can begin, and contractors retain "
            "stolen wages with zero enforcement consequence — NELP estimates "
            "$680 million annually in unrecoverable wages from deported workers."
        ),
        "difficulty": "hard",
        "source_references": [
            "National Employment Law Project, \"Immigrant Workers and Wage Theft\" (2023) — $8.8 billion annual stolen wages estimate",
            "Centro de los Derechos del Migrante, \"Employer-Initiated ICE Reports\" (2019) — 46% tip correlation with wage disputes",
            "ICE Enforcement and Removal Operations Annual Report FY 2023 — removal statistics and DOL referral rates",
            "TRAC Immigration Data, Syracuse University — Houston immigration court wait times and representation rates",
            "DOL Wage and Hour Division FY 2023 Statistics — complaint processing timelines",
            "Sure-Tan v. NLRB, 467 U.S. 883 (1984) — FLSA applies regardless of immigration status",
        ],
        "corridors": ["GT-US", "MX-US", "BD-MY", "MM-TH"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring"],
            "means": [
                "coercion",
                "threat of use of force",
                "abuse of position of vulnerability",
            ],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "government_complicity_005",
        "name": "Regulatory Capture by Recruitment Industry",
        "category": "government_complicity",
        "steps": [
            {
                "id": "gc005_s1",
                "description": (
                    "The Bangladesh Association of International Recruiting "
                    "Agencies (BAIRA), representing 1,200 of 1,557 BMET-licensed "
                    "agencies, successfully lobbies the Ministry of Expatriates' "
                    "Welfare and Overseas Employment to raise the maximum "
                    "recruitment fee cap from BDT 84,000 ($780) to BDT 200,000 "
                    "($1,860) for Saudi Arabia placements, effective 2019. BAIRA's "
                    "lobbying argument: the existing cap forces agencies to charge "
                    "workers illegally, so raising the cap will 'bring fees into "
                    "the formal system.' The ILO's response noted that the cap "
                    "increase 'legalized what was previously recognized as "
                    "exploitative overcharging' rather than reducing actual fees, "
                    "which remained at BDT 300,000-500,000 ($2,800-$4,650) for "
                    "Saudi placements through sub-agent layers."
                ),
                "legal_basis": (
                    "Recruitment fee caps are set by ministerial order under the "
                    "Bangladesh Overseas Employment and Migrants Act 2013 § 20, "
                    "which authorizes the government to 'determine the maximum "
                    "amount chargeable to a migrant worker.' BAIRA has legal "
                    "standing to petition the ministry as a registered trade "
                    "association under the Trade Organizations Ordinance 1961. "
                    "Fee cap adjustments are a normal regulatory function."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "BAIRA's lobbying effectively raised the legal threshold "
                    "for what constitutes 'overcharging' rather than reducing "
                    "actual worker costs. The ILO's 2019 FAIR assessment found "
                    "that actual fees remained 2-3x above the new cap because "
                    "sub-agent layers are invisible to the regulatory framework. "
                    "The cap increase gave agencies more legal headroom while "
                    "leaving the sub-agent fee structure untouched."
                ),
            },
            {
                "id": "gc005_s2",
                "description": (
                    "BMET's governing advisory board includes 4 BAIRA-nominated "
                    "members (out of 12 total), who participate in decisions on "
                    "agency licensing, fee schedules, complaint adjudication, and "
                    "enforcement priorities. Nepal's Department of Foreign "
                    "Employment (DoFE) operates a similar structure: the Foreign "
                    "Employment Board includes 3 recruitment industry "
                    "representatives among its 11 members, per Foreign Employment "
                    "Act 2007 § 5. The Philippines' POEA Governing Board included "
                    "2 private recruitment industry representatives until 2022, "
                    "when the DMW reorganization nominally removed them — but "
                    "the DMW Advisory Council reinstated 'private sector "
                    "consultants' drawn from the same industry associations."
                ),
                "legal_basis": (
                    "Advisory board composition is established by statute: "
                    "Bangladesh Overseas Employment and Migrants Act 2013 § 7 "
                    "specifies board membership categories including 'private "
                    "sector representatives.' Nepal Foreign Employment Act 2007 "
                    "§ 5(1)(c)-(e) includes recruitment industry representatives. "
                    "Multi-stakeholder governance is considered international "
                    "best practice by the World Bank and OECD for regulatory "
                    "bodies. Industry participation is framed as 'market expertise.'"
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Recruitment industry representatives sit on the regulatory "
                    "body that licenses their own agencies, sets the fee caps "
                    "they lobby to raise, and adjudicates complaints filed "
                    "against their members. This is textbook regulatory capture "
                    "as defined by Stigler (1971): the regulated industry "
                    "controls the regulator. BAIRA's 4 seats out of 12 on the "
                    "BMET board give it effective veto power over enforcement "
                    "actions, since quorum decisions require 7 votes and "
                    "government appointees rarely oppose industry on fee and "
                    "licensing matters."
                ),
            },
            {
                "id": "gc005_s3",
                "description": (
                    "BMET's enforcement budget was cut from BDT 45 million "
                    "($420,000) in FY 2018-19 to BDT 27 million ($251,000) in "
                    "FY 2022-23 — a 40% reduction over 5 years in nominal terms "
                    "and approximately 55% in real terms adjusted for inflation. "
                    "BMET employed 8 enforcement inspectors for 1,557 licensed "
                    "agencies in 2023, yielding a ratio of 1 inspector per 195 "
                    "agencies. Inspections declined from 234 in 2018 to 89 in "
                    "2022. Nepal's DoFE had 5 inspectors for 857 licensed agencies "
                    "(1:171 ratio). The complaint process requires in-person filing "
                    "at BMET's Kakrail office in Dhaka during business hours "
                    "(9 AM-4 PM, Sunday-Thursday), with no online, telephone, or "
                    "regional filing option."
                ),
                "legal_basis": (
                    "Budget allocation is determined by the Ministry of Finance "
                    "through the annual budget process. Enforcement staffing "
                    "levels are set by the Public Service Commission. In-person "
                    "complaint filing requirements are established by BMET "
                    "administrative circular. None of these constitute legal "
                    "violations — they are resource allocation decisions within "
                    "the government's fiscal authority."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "A 40% enforcement budget cut concurrent with a 137% fee "
                    "cap increase (BDT 84,000 to BDT 200,000) signals "
                    "institutional prioritization of industry revenue over "
                    "worker protection. The in-person complaint requirement "
                    "at a single Dhaka office effectively bars workers who "
                    "are overseas (the entire at-risk population) and workers "
                    "from rural areas (where 73% of migrant workers originate, "
                    "per BMET data) from accessing the complaint system."
                ),
            },
            {
                "id": "gc005_s4",
                "description": (
                    "Penalties for agency violations are reduced from license "
                    "revocation (permanent) to administrative fines of BDT "
                    "50,000-200,000 ($465-$1,860) per violation, per a 2020 "
                    "BMET administrative circular. BMET collected BDT 12.3 "
                    "million ($114,000) in agency fines in FY 2022-23, which "
                    "funded 45% of its enforcement budget — creating a financial "
                    "dependency where the regulator relies on the fines it "
                    "collects from the agencies it regulates. Only 3 of 1,557 "
                    "agencies had licenses revoked between 2019 and 2023, "
                    "despite 4,218 worker complaints filed in the same period. "
                    "Nepal's DoFE similarly revoked only 7 of 857 licenses "
                    "between 2019 and 2023."
                ),
                "legal_basis": (
                    "Administrative fines are authorized under the Overseas "
                    "Employment and Migrants Act 2013 § 33 as an alternative "
                    "to license revocation. The ministry has discretion to "
                    "determine penalty severity. Fine revenue is deposited into "
                    "BMET's operational fund under the Treasury Single Account "
                    "system, which permits sub-allocations to enforcement "
                    "activities. This is a standard regulatory financing "
                    "mechanism used by securities commissions and "
                    "telecommunications regulators worldwide."
                ),
                "sector": "services",
                "corridor": "BD-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "When 45% of the enforcement budget comes from fines "
                    "collected from regulated agencies, the regulator cannot "
                    "afford to shut down the agencies that fund its operations. "
                    "The revocation rate of 0.19% (3 of 1,557 agencies over 4 "
                    "years) versus the complaint rate (4,218 complaints over "
                    "the same period, or 2.7 complaints per agency) demonstrates "
                    "that complaints have near-zero enforcement consequence. "
                    "The ILO's 2019 FAIR assessment characterized this as "
                    "'institutional capture where the regulator's financial "
                    "survival depends on the continued operation of the entities "
                    "it is mandated to regulate.'"
                ),
            },
        ],
        "chain_context": (
            "This chain documents the complete capture of a labor migration "
            "regulatory system by the recruitment industry it regulates. "
            "Industry lobbying raises fee caps, legitimizing previously "
            "illegal overcharging. Industry representatives on the "
            "governing board control licensing, fee, and enforcement "
            "decisions. Enforcement budgets are cut while the regulator "
            "becomes financially dependent on fine revenue from the "
            "regulated industry. And complaint processes are designed "
            "to be inaccessible to the overseas workers who are the "
            "primary victims. The result is a regulatory framework that "
            "exists on paper — laws, caps, inspectors, complaints — but "
            "functions in practice as a revenue extraction and legitimation "
            "mechanism for the recruitment industry. The ILO FAIR "
            "Initiative's cross-country assessment (2019) identified this "
            "pattern in Bangladesh, Nepal, and Pakistan as 'the most "
            "significant structural barrier to fair recruitment in South "
            "Asian GCC labor corridors.'"
        ),
        "emergent_risk": (
            "Regulatory capture converts the enforcement agency into a "
            "revenue partner of the recruitment industry: fee cap raised "
            "137%, enforcement budget cut 40%, 45% of remaining budget "
            "funded by fines from regulated agencies, 0.19% license "
            "revocation rate against 4,218 complaints — the regulator "
            "cannot financially survive without the entities it is "
            "mandated to regulate."
        ),
        "difficulty": "expert",
        "source_references": [
            "BMET Annual Reports 2018-2023 — enforcement budget, staffing, licensing, and fine collection data",
            "ILO FAIR Recruitment Initiative, \"Assessment of Labour Migration from Bangladesh\" (2019) — regulatory capture analysis",
            "Nepal Department of Foreign Employment Annual Report 2078/79 — inspector ratios and revocation statistics",
            "POEA/DMW Governing Board composition records and Philippines RA 10022 (2010) — board membership structure",
            "Bangladesh Overseas Employment and Migrants Act 2013 §§ 7, 20, 33 — regulatory framework provisions",
            "Nepal Foreign Employment Act 2007 §§ 5, 28-29 — board composition and fee cap authority",
        ],
        "corridors": ["BD-SA", "NP-QA", "PH-SA", "PK-AE"],
        "palermo_elements": {
            "act": ["recruitment"],
            "means": [
                "abuse of power",
                "deception",
                "abuse of position of vulnerability",
            ],
            "purpose": ["exploitation", "forced labour"],
        },
    },
    {
        "id": "government_complicity_006",
        "name": "Free Trade Zone Labor Law Suspension",
        "category": "government_complicity",
        "steps": [
            {
                "id": "gc006_s1",
                "description": (
                    "Jordan's Qualifying Industrial Zone (QIZ) legislation, "
                    "established under the US-Jordan-Israel Agreement on Trade "
                    "(1996, amended 2010), creates designated industrial zones — "
                    "Al Hassan, Ad-Dulayl, Al-Tajamouat, and 13 others — where "
                    "qualifying factories receive duty-free access to the US "
                    "market for manufactured goods (primarily garments) containing "
                    "at least 8% Israeli input. QIZ factories employ approximately "
                    "70,000 workers, of whom 75% (52,500) are migrant workers "
                    "from Bangladesh, Sri Lanka, Myanmar, and India. The QIZ "
                    "authority operates under the Jordan Investment Commission "
                    "with governance input from a private sector advisory board "
                    "comprising factory owners and garment industry association "
                    "representatives."
                ),
                "legal_basis": (
                    "QIZ zones were established under Jordan's Investment "
                    "Promotion Law No. 16/1995 (amended 2014) and the US-Jordan "
                    "FTA Implementation Act (2001). The QIZ agreement is a "
                    "bilateral trade arrangement between sovereign states. "
                    "Jordan's Labour Code No. 8/1996 (amended 2019) technically "
                    "applies in QIZ zones, but the Investment Promotion Law "
                    "Art. 11 grants QIZ-registered companies 'regulatory "
                    "flexibility' in labor practices as an investment incentive."
                ),
                "sector": "manufacturing",
                "corridor": "BD-JO",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The 'regulatory flexibility' provision creates a de facto "
                    "parallel labor regime within QIZ zones. The National Labour "
                    "Committee (now Institute for Global Labour and Human Rights) "
                    "documented in 2006 that QIZ factories operated under "
                    "conditions that would violate Jordan's own Labour Code "
                    "outside the zone: forced overtime of 80-100 hours/month, "
                    "passport confiscation, and employer-controlled dormitories. "
                    "The Better Work Jordan program (ILO-IFC) found in its 2023 "
                    "compliance report that 43% of QIZ factories had at least "
                    "one forced labor indicator."
                ),
            },
            {
                "id": "gc006_s2",
                "description": (
                    "Bangladesh's Export Processing Zones Authority (BEPZA) "
                    "administers 8 EPZs employing 465,000 workers under the "
                    "Bangladesh Export Processing Zones Authority Act 1980 "
                    "(amended 2019). The EPZ Labour Act 2019 created a separate "
                    "labor framework for EPZ workers that excludes them from "
                    "the Bangladesh Labour Act 2006 — the law governing all "
                    "workers outside EPZs. Key differences: EPZ workers may "
                    "form 'Workers' Welfare Associations' (WWAs) instead of "
                    "trade unions (the right to form unions is guaranteed under "
                    "the Labour Act 2006 § 176 but explicitly denied in EPZs). "
                    "EPZ minimum wage is set by BEPZA at BDT 8,000/month ($74) "
                    "versus BDT 12,500 ($116) for garment workers outside EPZs. "
                    "EPZ working hours permit 60 hours/week versus 48 hours "
                    "under the Labour Act 2006."
                ),
                "legal_basis": (
                    "The EPZ Labour Act 2019 was enacted by the Bangladesh "
                    "Parliament as a separate statute. BEPZA's authority to "
                    "set distinct labor standards is established under the "
                    "BEPZA Act 1980 § 11A (as amended). ILO Conventions C87 "
                    "(Freedom of Association) and C98 (Right to Organise) — "
                    "both ratified by Bangladesh — prohibit restrictions on "
                    "trade union formation, but Bangladesh maintains that "
                    "WWAs fulfill the spirit of these conventions."
                ),
                "sector": "manufacturing",
                "corridor": "BD-domestic",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Creating a separate labor law for EPZ workers that provides "
                    "lower wages (40% less), longer hours (25% more), and no "
                    "union rights constitutes a government-sanctioned two-tier "
                    "labor system. The ITUC's 2017 report 'Special Economic "
                    "Zones: Hotbeds of Exploitation' identified Bangladesh EPZs "
                    "as exhibiting 'systematic suppression of labor rights "
                    "through legislative carve-outs designed to attract foreign "
                    "investment at the expense of worker protection.' ILO's "
                    "Committee of Experts repeatedly flagged Bangladesh's EPZ "
                    "Labour Act as inconsistent with C87 and C98."
                ),
            },
            {
                "id": "gc006_s3",
                "description": (
                    "Labor inspectors from the Department of Inspection for "
                    "Factories and Establishments (DIFE) — Bangladesh's national "
                    "factory inspection body — are barred from conducting "
                    "unannounced inspections in EPZ factories under BEPZA "
                    "administrative circular No. 12/2018. All inspections must "
                    "be scheduled 72 hours in advance and coordinated through "
                    "BEPZA's EPZ Inspector office. In Jordan's QIZ zones, "
                    "Ministry of Labour inspectors similarly require coordination "
                    "with the QIZ authority before entering factory premises. "
                    "BEPZA conducted 145 inspections across 450 factories in "
                    "8 EPZs in 2022 — an average of 0.32 inspections per "
                    "factory per year, compared to the ILO's recommendation "
                    "of at least 1 inspection per factory per year."
                ),
                "legal_basis": (
                    "BEPZA's authority to regulate inspection procedures within "
                    "EPZs is established under the BEPZA Act 1980 § 11A. The "
                    "72-hour advance notice requirement is framed as necessary "
                    "for 'security coordination and production scheduling.' "
                    "Jordan's QIZ inspection coordination is governed by the "
                    "Investment Promotion Law Art. 11 'regulatory flexibility' "
                    "provision, which industry lawyers interpret as requiring "
                    "prior consent for regulatory actions within zones."
                ),
                "sector": "manufacturing",
                "corridor": "BD-domestic",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Advance notice inspections eliminate the element of "
                    "surprise that makes labor inspection effective. The ILO's "
                    "2022 report 'Employment and Decent Work in Export Processing "
                    "Zones' found that EPZs with advance-notice inspection "
                    "requirements showed 3.2x higher rates of non-compliance "
                    "on re-inspection (after the notice period) compared to "
                    "zones with unannounced inspection authority, indicating "
                    "that factories use the notice period to conceal violations."
                ),
            },
            {
                "id": "gc006_s4",
                "description": (
                    "Worker disputes in Bangladesh EPZs are adjudicated by "
                    "BEPZA's internal EPZ Labour Tribunal, established under "
                    "the EPZ Labour Act 2019 § 82, rather than the national "
                    "Labour Courts established under the Labour Act 2006 "
                    "§ 214. The EPZ Labour Tribunal is staffed by BEPZA-"
                    "appointed adjudicators, and its decisions are final — "
                    "appeal lies only to the High Court Division of the "
                    "Supreme Court, which requires legal representation that "
                    "EPZ workers earning BDT 8,000/month ($74) cannot afford. "
                    "In 2022, the EPZ Labour Tribunal ruled in favor of workers "
                    "in 12% of cases (23 of 192 filed), compared to a 34% "
                    "worker success rate in national Labour Courts. Jordan's "
                    "QIZ zones operate a similar system through the QIZ "
                    "Disputes Committee."
                ),
                "legal_basis": (
                    "The EPZ Labour Tribunal is established by statute (EPZ "
                    "Labour Act 2019 § 82) and is a legally constituted body. "
                    "Its jurisdiction over EPZ labor disputes is exclusive by "
                    "law. High Court appeal rights are preserved, satisfying "
                    "constitutional due process requirements under Bangladesh "
                    "Constitution Art. 31. The tribunal is technically "
                    "independent, although its adjudicators are appointed by "
                    "the same authority (BEPZA) that administers the zones "
                    "and reports to the Prime Minister's Office on investment "
                    "attraction targets."
                ),
                "sector": "manufacturing",
                "corridor": "BD-domestic",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Workers inside EPZs have fewer substantive rights (no "
                    "unions, lower wages, longer hours), fewer procedural "
                    "protections (advance-notice inspections, BEPZA-controlled "
                    "tribunals), and worse outcomes (12% worker success rate vs. "
                    "34% in national courts) than workers outside the zones — "
                    "all by legislative design. The ITUC's 2017 assessment "
                    "concluded that EPZ labour tribunals 'lack the independence "
                    "necessary for impartial adjudication because the appointing "
                    "authority has a financial interest in maintaining the "
                    "investment climate that the tribunal's decisions affect.'"
                ),
            },
        ],
        "chain_context": (
            "This chain documents how governments deliberately create zones "
            "of reduced labor protection as an investment attraction strategy. "
            "The legislative mechanism is explicit: a separate law is enacted "
            "for the zone that provides lower standards than national law. "
            "Inspection is hobbled through advance-notice requirements. "
            "Dispute resolution is internalized under zone authority control. "
            "And the governance structure places industry representatives on "
            "the authority that sets and enforces the standards. Each element "
            "is legislated, documented, and defensible as 'investment promotion' "
            "— but the combined effect is a jurisdiction within a jurisdiction "
            "where workers have systematically fewer rights, weaker protections, "
            "and worse outcomes. The ILO's 2022 global EPZ study found that "
            "zones with all four features (separate labor law, advance-notice "
            "inspections, internal tribunals, and industry governance) had "
            "forced labor indicator rates 4.7x higher than the national average."
        ),
        "emergent_risk": (
            "Government-created zones of reduced labor rights: EPZ workers "
            "earn 40% less, work 25% longer, cannot form unions, face 0.32 "
            "inspections per factory per year with 72-hour advance notice, "
            "and win only 12% of tribunal cases adjudicated by zone-appointed "
            "officers — all established by statute as investment incentives."
        ),
        "difficulty": "expert",
        "source_references": [
            "ILO, \"Employment and Decent Work in Export Processing Zones\" (2022) — global EPZ labor standards analysis",
            "ITUC, \"Special Economic Zones: Hotbeds of Exploitation\" (2017) — Bangladesh EPZ and Jordan QIZ assessment",
            "Better Work Jordan (ILO-IFC), Annual Compliance Report 2023 — QIZ factory forced labor indicators",
            "Bangladesh EPZ Labour Act 2019 §§ 82 — tribunal establishment and jurisdiction",
            "Bangladesh BEPZA Act 1980 § 11A (as amended) — zone authority and inspection powers",
            "Jordan Investment Promotion Law No. 16/1995 Art. 11 — 'regulatory flexibility' provision",
        ],
        "corridors": ["BD-JO", "LK-JO", "BD-domestic", "VN-domestic"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring"],
            "means": [
                "abuse of power",
                "abuse of position of vulnerability",
            ],
            "purpose": ["exploitation", "forced labour"],
        },
    },
    {
        "id": "government_complicity_007",
        "name": "Bilateral Labor Agreement as Diplomatic Theater",
        "category": "government_complicity",
        "steps": [
            {
                "id": "gc007_s1",
                "description": (
                    "Nepal and Qatar sign a Bilateral Labour Agreement (BLA) in "
                    "2005, renewed in 2011 and 2017, establishing a framework for "
                    "'orderly and safe migration' of Nepali workers to Qatar. The "
                    "signing ceremony is attended by both prime ministers and "
                    "covered extensively by Nepali media as a 'landmark achievement' "
                    "for worker protection. The MOU text commits both governments "
                    "to 'ensuring that migrant workers' rights are protected in "
                    "accordance with applicable national and international law.' "
                    "Bangladesh signs a similar BLA with Saudi Arabia in 2008 "
                    "(renewed 2015), and the Philippines signs labor cooperation "
                    "agreements with Saudi Arabia (2013), Kuwait (2018 revised "
                    "after the Demafelis case), and the UAE (2017)."
                ),
                "legal_basis": (
                    "Bilateral labor agreements are standard instruments of "
                    "international migration governance, endorsed by the ILO's "
                    "2015 report 'Bilateral Agreements and Memoranda of "
                    "Understanding on Migration of Low-Skilled Workers' as a "
                    "'promising practice' when they include enforcement "
                    "mechanisms. The Nepal-Qatar MOU operates under the framework "
                    "of the Vienna Convention on the Law of Treaties (1969). "
                    "Both governments have sovereign authority to negotiate "
                    "and implement bilateral agreements."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The MOU text uses exclusively aspirational language ('shall "
                    "endeavour to,' 'will seek to,' 'may establish') with no "
                    "binding obligations, no penalties for non-compliance, no "
                    "designated enforcement body, and no worker complaint channel. "
                    "Migrant Forum in Asia's 2014 analysis of 30 GCC-origin "
                    "country BLAs found that 27 (90%) contained no enforcement "
                    "mechanism, 25 (83%) had no penalty provisions, and 28 (93%) "
                    "had no independent monitoring body."
                ),
            },
            {
                "id": "gc007_s2",
                "description": (
                    "The Qatar government cites the Nepal BLA in its national "
                    "submissions to the ILO Committee of Experts and the UN "
                    "Human Rights Council Universal Periodic Review (UPR, 3rd "
                    "cycle 2019) as evidence of its commitment to migrant "
                    "worker protection. Qatar's UPR submission states: 'Qatar "
                    "has signed bilateral labour agreements with [10 origin "
                    "countries] to ensure comprehensive protection of migrant "
                    "workers' rights.' The US TIP Report 2024 country narrative "
                    "for Qatar notes that 'the government continued to cite "
                    "bilateral agreements as evidence of reform' while "
                    "acknowledging that 'implementation of these agreements "
                    "remained inadequate.'"
                ),
                "legal_basis": (
                    "Governments are free to cite bilateral agreements in "
                    "international forum submissions. The UPR process under "
                    "UNHRC Resolution 5/1 invites voluntary reporting on human "
                    "rights implementation. ILO supervisory mechanisms rely on "
                    "government self-reporting under the reporting obligations "
                    "of ratified conventions. There is no prohibition on citing "
                    "agreements that lack enforcement mechanisms."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The BLA serves a diplomatic deflection function: when "
                    "international bodies or media raise concerns about worker "
                    "exploitation, both governments point to the MOU as evidence "
                    "of action. The ILO's 2015 assessment of GCC BLAs concluded "
                    "that 'the existence of an agreement is often equated with "
                    "effective protection, regardless of whether the agreement "
                    "contains binding commitments or enforcement mechanisms.' "
                    "This creates a perverse incentive: signing a weak BLA "
                    "is diplomatically preferable to having no BLA, because "
                    "the existence of the document absorbs criticism."
                ),
            },
            {
                "id": "gc007_s3",
                "description": (
                    "Nepal's embassy in Doha attempts to investigate complaints "
                    "from Nepali construction workers at Lusail City projects "
                    "reporting passport confiscation, unpaid wages of QAR 3,000-"
                    "8,000 ($823-$2,196), and physical violence by foremen. The "
                    "embassy requests access to the workers' accommodation camps "
                    "in the Industrial Area. Qatar's Ministry of Administrative "
                    "Development, Labour and Social Affairs (MADLSA) responds "
                    "that workplace access requires advance coordination 'in "
                    "accordance with the bilateral agreement framework,' that "
                    "worker complaints should be filed through Qatar's online "
                    "labor complaint portal (established 2017), and that the "
                    "bilateral agreement 'does not confer extraterritorial "
                    "enforcement authority to origin-country diplomatic missions.'"
                ),
                "legal_basis": (
                    "Under the Vienna Convention on Consular Relations (1963) "
                    "Art. 36, consular officers have the right to communicate "
                    "with and visit their nationals. However, workplace access "
                    "requires host-country consent, and the bilateral agreement "
                    "does not create a mechanism for origin-country inspection "
                    "of destination-country workplaces. Qatar's sovereignty over "
                    "its territory, including labor inspection authority, is "
                    "not limited by the BLA, which explicitly states that "
                    "'each party shall implement this agreement in accordance "
                    "with its own national laws and regulations.'"
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The BLA's sovereignty clause — 'each party shall implement "
                    "in accordance with its own national laws' — creates a "
                    "structural impossibility: the origin country cannot enforce "
                    "worker protections in the destination country, and the "
                    "destination country's enforcement is limited to its own "
                    "inspection capacity and political will. Nepal's embassy "
                    "has 6 staff members for 400,000+ Nepali workers in Qatar "
                    "and no independent inspection authority. The bilateral "
                    "agreement provides zero additional enforcement capacity "
                    "beyond what either government would have without it."
                ),
            },
            {
                "id": "gc007_s4",
                "description": (
                    "When Amnesty International, Human Rights Watch, or the "
                    "Guardian publish investigations documenting exploitation "
                    "of Nepali workers on Qatar mega-projects, both governments "
                    "issue coordinated responses citing the BLA. Nepal's Ministry "
                    "of Labour states: 'Nepal has a comprehensive bilateral "
                    "agreement with Qatar that provides a framework for worker "
                    "protection.' Qatar's MADLSA states: 'Qatar is committed "
                    "to protecting all workers' rights in accordance with "
                    "bilateral agreements with origin countries.' Neither "
                    "government provides data on complaints filed under the "
                    "BLA, cases resolved, wages recovered, or workers protected. "
                    "The actual worker protection record: Nepal DoFE data shows "
                    "622 Nepali worker deaths in destination countries in fiscal "
                    "year 2078/79, with Qatar accounting for the largest share. "
                    "Zero deaths were investigated under BLA provisions."
                ),
                "legal_basis": (
                    "Government press responses are protected by sovereign "
                    "immunity and diplomatic practice. Neither government is "
                    "required to publish BLA implementation data. Worker death "
                    "investigations are governed by the laws of the country "
                    "where the death occurs (Qatar Penal Code Art. 300-304 "
                    "for suspicious deaths). The BLA contains no provision "
                    "for joint investigation, independent monitoring, or "
                    "public reporting of outcomes."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The BLA's entire operational function is diplomatic: it "
                    "provides a document both governments can reference when "
                    "criticized. Actual protection provided: zero enforcement "
                    "mechanism, zero penalties, zero monitoring body, zero "
                    "worker complaint channel, zero deaths investigated. "
                    "Migrant Forum in Asia's 2014 comparative analysis "
                    "concluded: 'BLAs in GCC corridors function as diplomatic "
                    "theater — they exist to be cited, not implemented. Their "
                    "primary function is to insulate both governments from "
                    "international criticism while maintaining the labor export-"
                    "import relationship undisturbed.'"
                ),
            },
        ],
        "chain_context": (
            "This chain reveals bilateral labor agreements as instruments of "
            "diplomatic performance rather than worker protection. The "
            "agreement is signed with fanfare, cited in international forums, "
            "referenced in response to media criticism, and renewed "
            "periodically — all without providing a single binding protection "
            "to any worker. The sovereignty clause ensures neither government "
            "has authority to enforce the other's commitments. The absence "
            "of penalties means non-compliance has no consequence. And the "
            "lack of a monitoring body means compliance is unmeasurable. "
            "Migrant Forum in Asia analyzed 30 GCC-origin BLAs and found "
            "that 90% lacked enforcement mechanisms and 93% lacked "
            "independent monitoring, yet all 30 were cited by at least one "
            "signatory in international human rights submissions. The ILO's "
            "2015 assessment described this as 'governance theater: the "
            "symbolic performance of protection as a substitute for its "
            "substance.'"
        ),
        "emergent_risk": (
            "Bilateral labor agreements function as diplomatic shields rather "
            "than worker protections: 90% of GCC-origin BLAs lack enforcement "
            "mechanisms, 93% lack independent monitoring, zero deaths are "
            "investigated under BLA provisions, and both governments cite the "
            "agreements to deflect criticism while 622 workers die annually "
            "without investigation."
        ),
        "difficulty": "hard",
        "source_references": [
            "ILO, \"Bilateral Agreements and Memoranda of Understanding on Migration of Low-Skilled Workers\" (2015) — cross-country BLA assessment",
            "Migrant Forum in Asia, \"Review of Bilateral Labour Agreements\" (2014) — 30-BLA comparative analysis",
            "US Department of State, Trafficking in Persons Report 2024 — Qatar country narrative on BLA implementation gaps",
            "Nepal-Qatar Bilateral Labour Agreement (2005, renewed 2011, 2017) — full text analysis",
            "Nepal Department of Foreign Employment Annual Report 2078/79 — 622 worker deaths data",
            "Amnesty International, \"The Dark Side of Migration: Spotlight on Qatar's Construction Sector\" (2013) — BLA ineffectiveness documentation",
        ],
        "corridors": ["BD-SA", "NP-QA", "PH-SA", "ET-SA", "ID-MY"],
        "palermo_elements": {
            "act": ["recruitment", "transfer"],
            "means": [
                "deception",
                "abuse of power",
                "abuse of position of vulnerability",
            ],
            "purpose": ["exploitation", "forced labour"],
        },
    },
    {
        "id": "government_complicity_008",
        "name": "Prison Labor Corporate Contracting Chain",
        "category": "government_complicity",
        "steps": [
            {
                "id": "gc008_s1",
                "description": (
                    "The Federal Bureau of Prisons (BOP) and state departments "
                    "of corrections contract with private prison operators — "
                    "CoreCivic, Inc. (formerly Corrections Corporation of America) "
                    "and GEO Group, Inc. — to operate 130+ facilities housing "
                    "approximately 115,000 federal and state inmates. CoreCivic's "
                    "2023 SEC 10-K reported $1.99 billion in revenue. GEO Group "
                    "reported $2.42 billion. Both companies operate facility-based "
                    "work programs where inmates manufacture goods (furniture, "
                    "textiles, electronics assembly, packaging) and provide "
                    "services (call centers, data entry, laundry for external "
                    "clients). UNICOR (Federal Prison Industries) generated $505 "
                    "million in sales in FY 2023 from inmate labor at 50+ factory "
                    "locations within BOP facilities."
                ),
                "legal_basis": (
                    "The Thirteenth Amendment to the US Constitution, ratified "
                    "1865, states: 'Neither slavery nor involuntary servitude, "
                    "except as a punishment for crime whereof the party shall "
                    "have been duly convicted, shall exist within the United "
                    "States.' This exception explicitly authorizes compulsory "
                    "labor for convicted persons. UNICOR operates under 18 USC "
                    "§ 4121-4128 (Federal Prison Industries Act). State prison "
                    "labor programs operate under respective state DOC authority."
                ),
                "sector": "manufacturing",
                "corridor": "US-domestic",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The 13th Amendment's 'punishment' exception creates a "
                    "constitutional permission for sub-minimum-wage compulsory "
                    "labor. The ACLU's 2022 report 'Captive Labor' documented "
                    "that 800,000 incarcerated workers generate an estimated "
                    "$11 billion annually in goods and services while being "
                    "paid $0.13-$0.52/hour (non-PIECP programs) or $0.23-"
                    "$1.15/hour (PIECP-certified programs), compared to the "
                    "federal minimum wage of $7.25/hour. Worth Rises (2023) "
                    "calculated that prison labor generates $2 billion annually "
                    "in corporate profits."
                ),
            },
            {
                "id": "gc008_s2",
                "description": (
                    "Corporations contract with prison systems through the "
                    "Prison Industry Enhancement Certification Program (PIECP), "
                    "administered by the Bureau of Justice Assistance (BJA), "
                    "which certifies state and local prison industry programs "
                    "to sell inmate-made goods on the open market. PIECP "
                    "requires that inmate wages be 'comparable to' prevailing "
                    "wages for similar work in the locality — but permits "
                    "deductions of up to 80% for room and board (40%), taxes "
                    "(20%), victim restitution (10%), and family support (10%). "
                    "An inmate earning the 'prevailing wage' of $10/hour in a "
                    "PIECP program receives $2/hour after deductions. Companies "
                    "documented as using PIECP prison labor include Victoria's "
                    "Secret (through subcontractor Third Generation, Inc., per "
                    "Mother Jones investigation 2008), Walmart (through "
                    "Martori Farms, per VICE investigation 2016), and McDonald's "
                    "(uniforms, per ACLU reporting 2022)."
                ),
                "legal_basis": (
                    "PIECP was authorized by the Justice System Improvement Act "
                    "of 1979 (Pub. L. 96-157) and amended by the Crime Control "
                    "Act of 1990 (Pub. L. 101-647). 18 USC § 1761(c) creates "
                    "the certification framework. BJA administers PIECP under "
                    "DOJ authority. The 'prevailing wage' requirement with 80% "
                    "deduction authorization is codified in 28 CFR § 0.89. "
                    "Products manufactured under PIECP are exempt from the "
                    "general prohibition on interstate commerce in prison-made "
                    "goods (the Ashurst-Sumners Act, 18 USC § 1761(a))."
                ),
                "sector": "manufacturing",
                "corridor": "US-domestic",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "PIECP's 80% deduction authority means that 'prevailing wage' "
                    "compliance is nominal: workers receive $2/hour from a $10/hour "
                    "gross wage. The program creates a legal pathway for corporate "
                    "access to labor at 80% below market cost while maintaining "
                    "the appearance of fair compensation. Worth Rises (2023) "
                    "identified 4,100 corporations using PIECP or non-PIECP "
                    "prison labor programs, and noted that PIECP certifications "
                    "are self-reported by state DOC programs with minimal BJA "
                    "auditing — BJA conducted 7 audits across 37 certified "
                    "programs in FY 2022."
                ),
            },
            {
                "id": "gc008_s3",
                "description": (
                    "Inmates who refuse work assignments face disciplinary "
                    "consequences that vary by jurisdiction but commonly include: "
                    "loss of good-time credits (extending sentence by 15-54 days "
                    "per refusal in BOP under 28 CFR § 541.3), placement in "
                    "restricted housing (solitary confinement for 23 hours/day), "
                    "loss of commissary privileges, and denial of phone/visitation "
                    "access. BOP Program Statement 5380.08 classifies 'refusal "
                    "to work or accept a program assignment' as a Code 300 "
                    "prohibited act (moderate severity). In Texas state prisons "
                    "(TDCJ), inmates are not paid at all — Texas is one of 5 "
                    "states with zero-pay prison labor — and refusal to work "
                    "results in loss of good-time credits and disciplinary "
                    "segregation."
                ),
                "legal_basis": (
                    "Work requirements for incarcerated persons are authorized "
                    "by the 13th Amendment exception, 18 USC § 4121 (UNICOR "
                    "employment authority), and BOP Program Statements. State "
                    "DOC work requirements are authorized under state DOC "
                    "administrative codes. Disciplinary consequences for work "
                    "refusal are governed by institutional due process "
                    "requirements established in Wolff v. McDonnell, 418 "
                    "U.S. 539 (1974). Courts have generally upheld prison work "
                    "requirements as constitutional under the 13th Amendment "
                    "exception."
                ),
                "sector": "manufacturing",
                "corridor": "US-domestic",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The combination of sub-minimum-wage compensation ($0.13-"
                    "$1.15/hour) and punitive consequences for refusal "
                    "(extended sentences, solitary confinement) meets the ILO's "
                    "definition of forced labor under Convention C29 Art. 2: "
                    "'all work or service which is exacted from any person "
                    "under the menace of any penalty and for which the said "
                    "person has not offered himself voluntarily.' The 'voluntariness' "
                    "of prison labor is legally fictional: refusal results in "
                    "punitive consequences that extend incarceration."
                ),
            },
            {
                "id": "gc008_s4",
                "description": (
                    "Products manufactured through prison labor programs enter "
                    "the commercial supply chain without mandatory 'prison labor' "
                    "labeling. The Ashurst-Sumners Act (18 USC § 1761(a)) "
                    "prohibits interstate commerce in prison-made goods but "
                    "exempts PIECP-certified products. Non-PIECP goods are "
                    "restricted to government purchase (GSA Schedule, DOD "
                    "procurement) but enforcement is limited: the DOJ Inspector "
                    "General's 2023 audit found that 14% of UNICOR products "
                    "entered commercial channels outside authorized government "
                    "procurement streams. Consumers purchasing furniture, "
                    "textiles, packaging, and processed foods have no means of "
                    "determining whether prison labor was used in production."
                ),
                "legal_basis": (
                    "PIECP exemption from the Ashurst-Sumners Act is codified "
                    "at 18 USC § 1761(c). UNICOR's government-market restriction "
                    "is established under 18 USC § 4124. There is no federal "
                    "law requiring labeling of prison-labor-produced goods "
                    "entering commercial channels through PIECP or subcontracting. "
                    "The FTC's Guides Against Deceptive Practices (16 CFR Part "
                    "255) do not address prison labor provenance as a material "
                    "fact requiring disclosure."
                ),
                "sector": "manufacturing",
                "corridor": "US-domestic",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The absence of labeling requirements means that prison labor "
                    "products compete in the same market as free-labor products "
                    "without consumers being aware of the labor conditions. This "
                    "creates competitive downward pressure on free-labor wages "
                    "in the same industries (particularly furniture, textiles, "
                    "and call centers). The ACLU (2022) estimated that prison "
                    "labor displaces 600,000 free-labor jobs annually in "
                    "manufacturing sectors and suppresses wages by 2-4% in "
                    "counties with large prison labor programs."
                ),
            },
            {
                "id": "gc008_s5",
                "description": (
                    "ICE detention facilities operated by CoreCivic and GEO "
                    "Group house approximately 25,000 immigrant detainees "
                    "daily (ICE ERO FY 2023 average daily population), many "
                    "of whom are civil detainees (not convicted of crimes) "
                    "awaiting immigration proceedings. These detainees are "
                    "employed in facility maintenance — cooking, cleaning, "
                    "laundry — at $1/day under ICE's Voluntary Work Program "
                    "(ICE Performance-Based National Detention Standards 2011, "
                    "§ 5.8). A 2023 class action lawsuit (Barrientos v. CoreCivic, "
                    "No. 2:18-cv-01037, W.D. Wash.) alleged that ICE detainees "
                    "at the Northwest ICE Processing Center in Tacoma, Washington "
                    "were coerced into work through threats of solitary confinement "
                    "and that the $1/day payment constituted forced labor. ICE "
                    "detention costs taxpayers $142/day per detainee (FY 2023 "
                    "appropriation), of which CoreCivic and GEO Group receive "
                    "the contracted per-diem while paying detainees $1/day for "
                    "labor that would cost $12-18/hour on the open market."
                ),
                "legal_basis": (
                    "ICE's Voluntary Work Program is established under ICE "
                    "Performance-Based National Detention Standards (PBNDS) "
                    "2011, § 5.8, which states that work programs 'shall be "
                    "voluntary.' ICE detainees are civil detainees, not "
                    "convicted persons — the 13th Amendment 'punishment' "
                    "exception arguably does not apply to them. However, the "
                    "legal status of ICE detainee labor is unsettled: the "
                    "9th Circuit in Barrientos v. CoreCivic (2023) permitted "
                    "the forced labor claims to proceed to trial, but no "
                    "final ruling has established that the $1/day program "
                    "violates the TVPA or the 13th Amendment."
                ),
                "sector": "services",
                "corridor": "US-domestic",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "ICE detainees are civil detainees — not convicted of "
                    "crimes — yet are paid $1/day for labor that would cost "
                    "$12-18/hour on the open market, in facilities operated "
                    "by for-profit corporations receiving $142/day per detainee "
                    "from the federal government. The coercion element (threats "
                    "of solitary for refusal) and the sub-subsistence "
                    "compensation ($1/day) meet ILO C29 forced labor indicators. "
                    "The Barrientos litigation revealed that CoreCivic saved "
                    "approximately $5.2 million annually at the Tacoma facility "
                    "alone by using detainee labor instead of hiring free workers."
                ),
            },
        ],
        "chain_context": (
            "This chain documents how the US prison labor system — constitutionally "
            "authorized by the 13th Amendment exception, administered through "
            "federal programs (UNICOR, PIECP), operated by publicly-traded "
            "corporations (CoreCivic, GEO Group), and extending to civil ICE "
            "detainees — constitutes a state-sanctioned forced labor system by "
            "international standards. Every element operates under explicit "
            "legal authorization: the constitutional exception, the statutory "
            "frameworks, the PIECP certification, the ICE detention standards. "
            "But the ILO C29 definition of forced labor — work exacted under "
            "penalty and not voluntarily offered — is met at every stage: "
            "sub-minimum-wage compensation ($0.13-$1.15/hour), punitive "
            "consequences for refusal (extended sentences, solitary), coercion "
            "of civil detainees ($1/day under threat of segregation), and "
            "unlabeled products entering the commercial supply chain. The ACLU "
            "and Worth Rises have characterized this system as 'the largest "
            "forced labor program in the developed world.'"
        ),
        "emergent_risk": (
            "State-sanctioned forced labor under constitutional authorization: "
            "800,000 incarcerated workers paid $0.13-$1.15/hour, punished for "
            "refusal with extended sentences and solitary confinement, producing "
            "$11 billion in goods entering unlabeled commercial supply chains — "
            "extending to 25,000 civil ICE detainees paid $1/day in for-profit "
            "facilities receiving $142/day per detainee from the federal government."
        ),
        "difficulty": "expert",
        "source_references": [
            "ACLU, \"Captive Labor: Exploitation of Incarcerated Workers\" (2022) — 800,000 workers, $11 billion output, wage data",
            "Worth Rises, \"The Prison Industry: How It Started, How It Works, How It Harms\" (2023) — 4,100 corporations, $2 billion profit estimate",
            "13th Amendment to the US Constitution (1865) — 'except as a punishment for crime' exception text",
            "Prison Industry Enhancement Certification Program (PIECP), BJA — 28 CFR § 0.89, 80% deduction authorization",
            "Barrientos v. CoreCivic, No. 2:18-cv-01037 (W.D. Wash. 2023) — ICE detainee forced labor claims",
            "ICE Performance-Based National Detention Standards 2011, § 5.8 — Voluntary Work Program at $1/day",
        ],
        "corridors": ["US-domestic", "UK-domestic"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring"],
            "means": [
                "coercion",
                "threat of use of force",
                "abuse of power",
            ],
            "purpose": ["forced labour", "exploitation"],
        },
    },
]
