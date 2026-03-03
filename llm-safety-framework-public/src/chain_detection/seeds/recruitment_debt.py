"""
Recruitment-debt chains — multi-layered fee structures that create debt bondage.

Sources:
  ILO, "Recruitment Costs of Migrant Workers from the Philippines" (2019)
  KNOMAD/World Bank, "Migration and Remittances Data" — recruitment cost surveys
  IOM Bangladesh, "Mapping of Labour Migration Recruitment Practices" (Jan 2020)
  HRW, "Die First, and I'll Pay You Later: Saudi Arabia's Giga-Projects" (Dec 4, 2024)
  ICIJ, "Philippine Lenders and Labor Agents Fleece Workers Seeking Overseas Jobs"
      (Trafficking Inc. series)
  US State Department TIP Report 2024 — country narratives
  Issara Institute, "Top 5 Labour Abuses: A Field-Based Analysis" (2020)
  Liberty Shared, "Out of Sight: Modern Slavery in Pacific Supply Chains" (2023)
  EJF, "Blood and Water: Human Rights Abuse in the Global Seafood Industry" (2019)
  Taiwan Control Yuan, "Investigation Report on Distant Water Fisheries
      Labor Rights" (2023)
  ILO Convention 181 Art. 7(1) — Private Employment Agencies
  Nepal Foreign Employment Act 2007 §§ 28-29
  Philippines RA 10022 (2010) — Migrant Workers and Overseas Filipinos Act
  Bangladesh BMET fee schedule (BDT 84,000 cap) and 2023 sub-agent amendment
  Japan Technical Intern Training Act 2017 (OTIT supervisory framework)
  Korea Employment Permit Act 2003 (government-to-government channel)
  Saudi Labor Law Art. 61 (document retention prohibition, SAR 15,000 fine)
  Qatar Ministerial Decision No. 4/2015 (Wage Protection System)
"""

CHAINS: list[dict] = [
    {
        "id": "recruitment_debt_001",
        "name": "Gulf Domestic Worker Multi-Agency Fee Spiral",
        "category": "recruitment_debt",
        "steps": [
            {
                "id": "rd001_s1",
                "description": (
                    "A DMW-licensed recruitment agency (formerly POEA-accredited) "
                    "in Quezon City, Metro Manila charges a placement fee of PhP 25,000 "
                    "(~$450) for a Saudi Arabia domestic worker contract, citing the "
                    "DMW Standard Employment Contract fee schedule. The ILO's 2019 "
                    "study found Filipino migrants collectively paid PhP 100 billion "
                    "in recruitment costs between 2016 and 2019, averaging ~$1,000 per "
                    "worker for GCC destinations."
                ),
                "legal_basis": (
                    "Philippines RA 10022 (2010) § 6 authorizes the DMW (formerly POEA) "
                    "to set and enforce fee schedules for licensed agencies. Under POEA "
                    "Governing Board Resolution No. 6, Series of 2006, placement fees "
                    "for domestic workers are capped at one month's salary. ILO C181 "
                    "Art. 7(1) states: 'Private employment agencies shall not charge "
                    "directly or indirectly, in whole or in part, any fees or costs to "
                    "workers.'"
                ),
                "sector": "domestic_work",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Fee appears within the DMW ceiling but is only the first of four "
                    "layers. ICIJ's Trafficking Inc. investigation documented agencies "
                    "in Quezon City that split fees across affiliated entities to stay "
                    "within per-entity caps while total worker cost reached $1,000-$1,500."
                ),
            },
            {
                "id": "rd001_s2",
                "description": (
                    "The same agency mandates a 21-day Comprehensive Pre-Departure "
                    "Education Program (CPDEP) at a DMW-accredited training center in "
                    "Pasay City, billing the worker PhP 44,000 (~$800) for tuition, "
                    "lodging, and materials. The agency offers a salary-deduction plan: "
                    "60% of the first three months' wages will be auto-remitted to "
                    "cover the training cost."
                ),
                "legal_basis": (
                    "OWWA Memorandum Circular No. 2015-002 requires all departing OFWs "
                    "for household service to complete a pre-departure training program. "
                    "RA 10022 § 23 mandates compulsory insurance coverage at no cost to "
                    "the worker and declares all fees refundable if deployment fails."
                ),
                "sector": "domestic_work",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Training fee is 2-3x the actual cost of the government-mandated "
                    "program. The salary-deduction option, while framed as worker-friendly, "
                    "creates a pre-departure debt instrument. RA 10022 requires all fees "
                    "to be refundable, but ICIJ documented that only 3% of failed-deployment "
                    "workers ever recovered fees."
                ),
            },
            {
                "id": "rd001_s3",
                "description": (
                    "Before reaching the Quezon City agency, the worker paid PhP 66,000 "
                    "(~$1,200) to a provincial sub-agent ('recruiter-for-a-fee') in "
                    "Leyte, Eastern Visayas, who arranged document gathering, NBI "
                    "clearance, medical exams in Tacloban, and bus fare to Manila. "
                    "The sub-agent is not DMW-licensed and operates under an informal "
                    "referral arrangement with the Manila agency."
                ),
                "legal_basis": (
                    "RA 10022 § 6(l) and POEA Rules Part II, Rule I, § 1 prohibit "
                    "non-licensed individuals from engaging in recruitment, punishable "
                    "by 12-20 years imprisonment and PhP 1-2 million fine. However, "
                    "the 2019 ILO Philippines study found that 60% of workers used "
                    "provincial sub-agents, and fewer than 1% of sub-agents face "
                    "prosecution."
                ),
                "sector": "domestic_work",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Sub-agent fees are invisible to DMW oversight and unrecoverable "
                    "under RA 10022. The ILO 2019 study found sub-agent fees average "
                    "PhP 40,000-80,000 in Visayas and Mindanao provinces, constituting "
                    "the single largest cost component. ICIJ documented sub-agent "
                    "networks in 47 Philippine provinces funneling workers to 12 Manila "
                    "agencies."
                ),
            },
            {
                "id": "rd001_s4",
                "description": (
                    "The worker borrows PhP 137,500 (~$2,500) from a micro-lending "
                    "company co-located with the Quezon City agency — same building, "
                    "separate corporate registration — at 5% monthly interest (60% APR), "
                    "using her family's rice-farm lease in Leyte as collateral. ICIJ's "
                    "Trafficking Inc. found Philippine lending companies affiliated "
                    "with recruitment agencies issued over $240 million in migration "
                    "loans in 2018 alone."
                ),
                "legal_basis": (
                    "BSP Circular No. 1133 (2021) regulates lending companies at up "
                    "to 6% monthly interest. The loan is technically within the legal "
                    "ceiling. However, the SEC Anti-Dummy Act and BSP beneficial-"
                    "ownership rules should flag the agency-lender corporate overlap. "
                    "RA 10022 § 6(i) declares all recruitment fees refundable, but "
                    "the loan contract is classified as a 'personal loan' rather than "
                    "a 'recruitment fee.'"
                ),
                "sector": "domestic_work",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Agency-affiliated lender creates a circular debt trap: the agency "
                    "generates the debt and its affiliate profits from the interest. "
                    "At 5%/month compounding, the PhP 137,500 principal grows to "
                    "PhP 220,000 (~$4,000) within 10 months. The worker departs "
                    "owing ~$4,000 against a $400/month Saudi salary."
                ),
            },
            {
                "id": "rd001_s5",
                "description": (
                    "The Saudi employer's signed contract (processed through the "
                    "Saudi MUSANED platform) specifies SAR 1,500/month (~$400) for "
                    "a 2-year term. A side agreement — not uploaded to MUSANED — "
                    "authorizes 60% salary deduction for the first 6 months to "
                    "'reimburse the employer's recruitment investment of SAR 7,500.' "
                    "The worker receives SAR 600/month ($160) during this period."
                ),
                "legal_basis": (
                    "Saudi Labor Law Art. 61 prohibits employers from retaining "
                    "worker documents (SAR 15,000 fine). Art. 90 caps wage deductions "
                    "at 50% of total wages. The 60% deduction violates Art. 90 but "
                    "is enforced through the side agreement, which the worker signed "
                    "in Manila in English/Arabic without independent translation. The "
                    "MUSANED-registered contract shows the full SAR 1,500 salary."
                ),
                "sector": "domestic_work",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Worker receives $160/month while owing ~$4,000 with compounding "
                    "interest. At $160/month net pay (minus food/phone costs = ~$100 "
                    "remittable), it takes 40 months to clear the debt — exceeding "
                    "the 24-month contract. HRW's 2024 giga-projects report documented "
                    "identical dual-contract structures at NEOM and Riyadh MODON "
                    "Industrial Cities."
                ),
            },
        ],
        "chain_context": (
            "Each fee layer is individually defensible — a DMW-scheduled placement "
            "fee, a mandatory OWWA training program, a licensed lending transaction, "
            "a MUSANED-registered contract. But the ILO 2019 Philippines study found "
            "the total cost to Filipino domestic workers bound for Saudi Arabia "
            "averaged ~$1,000 in direct fees, with loan interest pushing effective "
            "cost to $2,500-$4,000. The Migrasia Agency-MSO-ML (Metropolitan "
            "Sub-agent Office to Micro-Lender) model shows how corporate overlap "
            "between agencies and lenders generates compound extraction while each "
            "entity's books appear compliant. The ICIJ Trafficking Inc. series "
            "documented 23 Manila agencies operating this exact structure."
        ),
        "emergent_risk": (
            "Debt bondage through legal intermediary layering: sub-agent ($1,200) + "
            "agency ($450) + training ($800) + loan interest (60% APR on $2,500) + "
            "Saudi-side salary deduction (60% for 6 months) = worker earns $160/month "
            "against $4,000+ debt. Mathematically unpayable within the 2-year contract."
        ),
        "difficulty": "hard",
        "source_references": [
            "ILO, 'Recruitment Costs of Migrant Workers from the Philippines' (2019) — PhP 100 billion total, $1,000 average per GCC worker",
            "ICIJ, 'Philippine Lenders and Labor Agents Fleece Workers Seeking Overseas Jobs' (Trafficking Inc. series) — 23 agencies, $240M in loans",
            "ILO Convention 181 Art. 7(1) — zero-fee principle for workers",
            "Philippines RA 10022 (2010) §§ 6, 23 — fee schedules, refund mandates, sub-agent prohibition",
            "POEA Governing Board Resolution No. 6, Series of 2006 — placement fee caps",
            "Saudi Labor Law Art. 61 (document retention), Art. 90 (50% deduction cap)",
            "HRW, 'Die First, and I'll Pay You Later: Saudi Arabia's Giga-Projects' (Dec 4, 2024) — dual-contract structures",
        ],
        "corridors": ["PH-SA", "PH-AE", "PH-KW"],
        "palermo_elements": {
            "act": ["recruitment", "transfer"],
            "means": ["deception", "abuse of position of vulnerability"],
            "purpose": ["exploitation", "forced labour"],
        },
    },
    {
        "id": "recruitment_debt_002",
        "name": "Nepal-Qatar Construction Worker Salary Advance Trap",
        "category": "recruitment_debt",
        "steps": [
            {
                "id": "rd002_s1",
                "description": (
                    "A licensed manpower agency clustered in Thamel district, "
                    "Kathmandu, advertises construction jobs in Lusail City, Qatar "
                    "at QAR 1,800/month (~$495) under Nepal's Free Visa Free Ticket "
                    "(FVFT) policy. The ad promises 'zero cost to worker — employer "
                    "pays all.' Nepal's Department of Foreign Employment (DoFE) "
                    "records show 236,208 labor permits issued for Qatar in fiscal "
                    "year 2078/79 (2021-2022). The legal service charge ceiling is "
                    "NPR 10,000 (~$75) for GCC countries under the Foreign Employment "
                    "Act 2007 § 28."
                ),
                "legal_basis": (
                    "Nepal Foreign Employment Act 2007 § 28 sets a maximum service "
                    "charge of NPR 10,000 for GCC countries under the FVFT policy. "
                    "§ 29 makes it an offense to charge fees exceeding the prescribed "
                    "amount, punishable by 3-7 years imprisonment and NPR 300,000-"
                    "500,000 fine. The FVFT policy (implemented 2015) requires the "
                    "employer to bear visa costs, airfare, and medical examination "
                    "fees."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "KNOMAD/World Bank recruitment cost surveys found Nepali workers "
                    "actually paid $600-$1,200 for Qatar placements — 7 to 16 times "
                    "the NPR 10,000 legal maximum. The zero-cost FVFT promise is the "
                    "hook; actual costs are shifted to categories not covered by the "
                    "FVFT definition (language training, medical re-tests, 'orientation')."
                ),
            },
            {
                "id": "rd002_s2",
                "description": (
                    "The manpower agency provides a NPR 100,000 (~$750) 'salary "
                    "advance' to the worker's family in Morang district, Terai "
                    "lowlands, documented as a personal loan between the agency "
                    "director (as an individual, not the licensed company) and the "
                    "worker. A village-level dalal (informal broker) who referred "
                    "the worker to the Kathmandu agency separately collected NPR "
                    "80,000 (~$600) as a 'service charge' — bringing actual total "
                    "cost to ~$1,350, or 18x the legal NPR 10,000 cap."
                ),
                "legal_basis": (
                    "Personal loans between individuals are governed by the Nepal "
                    "Contracts Act 2056 (2000) and are not subject to the Foreign "
                    "Employment Act fee cap. The dalal operates outside DoFE licensing "
                    "entirely. The Foreign Employment Act 2007 § 12 requires all "
                    "recruitment to occur through licensed agencies, but the 2024 "
                    "US TIP Report notes Nepal has 862 licensed agencies and an "
                    "estimated 50,000+ unlicensed dalals."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Salary advance transforms a zero-cost migration promise into a "
                    "debt obligation before the worker boards the plane. The dalal fee "
                    "is completely invisible to DoFE. Family in Morang becomes collateral: "
                    "the agency director holds a signed promissory note against the family's "
                    "property. KNOMAD surveys found 73% of Nepali workers for Qatar "
                    "borrowed to cover fees, with 29% using family land as collateral."
                ),
            },
            {
                "id": "rd002_s3",
                "description": (
                    "The worker signs a 'service agreement' at the Kathmandu agency "
                    "committing to 24 months of employment with the agency's partner "
                    "construction company (a sub-contractor on the Lusail City stadium "
                    "and infrastructure projects). The agreement includes a QAR 12,000 "
                    "(~$3,300) early termination penalty — equivalent to 6.7 months "
                    "of the promised salary — plus forfeiture of return airfare."
                ),
                "legal_basis": (
                    "Qatar Labour Law No. 14 of 2004, Art. 51 allows fixed-term "
                    "contracts with notice provisions. Termination penalty clauses "
                    "are not prohibited under Qatari law for fixed-term contracts "
                    "ended before term. However, Qatar's 2020 labour reforms "
                    "(Ministerial Decision No. 51/2020) eliminated the NOC "
                    "(No Objection Certificate) requirement, theoretically allowing "
                    "job mobility — but the termination penalty in the Nepali-side "
                    "service agreement operates outside Qatari jurisdiction."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Termination penalty ($3,300) exceeds 6 months' salary and is "
                    "enforced through the Nepali-side contract, not the Qatari-side "
                    "employment contract. This effectively nullifies Qatar's 2020 "
                    "job-mobility reform for this worker. HRW visited 6 labor camps "
                    "in Al Khor and Doha Industrial Area and found 78% of Nepali "
                    "construction workers had signed similar penalty clauses with "
                    "origin-country agencies."
                ),
            },
            {
                "id": "rd002_s4",
                "description": (
                    "Upon arrival at the Al Khor labor camp (housing 3,200 workers "
                    "across 8 dormitory blocks), the worker discovers the actual "
                    "salary is QAR 1,200/month (~$330), not QAR 1,800 as advertised. "
                    "Monthly deductions include QAR 400 ($110) for 'accommodation and "
                    "meals' in the employer-provided camp. Net take-home: QAR 800 "
                    "(~$220)/month. Qatar's Wage Protection System (Ministerial "
                    "Decision No. 4/2015) requires electronic salary payment, but "
                    "the WPS-registered amount is QAR 1,200, not QAR 1,800."
                ),
                "legal_basis": (
                    "Qatar Ministerial Decision No. 4/2015 (Wage Protection System) "
                    "mandates all wages be paid electronically through approved banks, "
                    "creating a verifiable record. The WPS contract shows QAR 1,200 — "
                    "the substituted amount, not the originally promised QAR 1,800. "
                    "Qatar Labour Law Art. 68 prohibits deductions exceeding 50% of "
                    "wages without court order. The QAR 400 accommodation deduction "
                    "represents 33% of the already-reduced salary."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Contract substitution: Kathmandu agency showed a QAR 1,800 "
                    "offer letter; the WPS-registered contract is QAR 1,200. The $165 "
                    "difference per month ($3,960 over the contract) is captured by "
                    "the intermediary chain. At $220/month net pay and $1,350 in "
                    "debt plus potential $3,300 penalty, the worker needs 21 months "
                    "of full net salary just to break even — leaving 3 months of "
                    "the 24-month contract for actual earnings."
                ),
            },
            {
                "id": "rd002_s5",
                "description": (
                    "The Kathmandu agency director's representative in Doha collects "
                    "QAR 200 (~$55)/month directly from the worker at the Al Khor "
                    "camp as 'loan repayment' for the salary advance, paid in cash "
                    "outside the WPS system. The representative visits the camp "
                    "bi-weekly and also offers additional micro-loans for workers "
                    "needing to send emergency remittances home. The worker's net "
                    "disposable income after all deductions: QAR 600 (~$165)/month."
                ),
                "legal_basis": (
                    "Cash collections outside the WPS are not visible to Qatar's "
                    "Ministry of Administrative Development, Labour and Social "
                    "Affairs (MADLSA). The arrangement operates under the Nepali "
                    "personal loan agreement, which Qatar has no jurisdiction to "
                    "regulate. Nepal's Foreign Employment Act 2007 § 32 requires "
                    "agencies to ensure workers receive their full contracted salary, "
                    "but enforcement requires a complaint filed in Kathmandu while "
                    "the worker is in Qatar."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Worker nets $165/month. Total debt: $1,350 (advance + dalal) + "
                    "potential $3,300 penalty = $4,650 maximum exposure. At $55/month "
                    "repayment, the salary advance alone takes 14 months to clear. "
                    "The offer of additional micro-loans at the camp deepens the "
                    "dependency. US TIP Report 2024 Qatar narrative identified this "
                    "exact pattern of origin-country agency representatives operating "
                    "informal collection networks inside labor camps."
                ),
            },
        ],
        "chain_context": (
            "Nepal's FVFT policy is circumvented through three mechanisms documented "
            "by KNOMAD and the US TIP Report 2024: (1) dalal fees outside DoFE "
            "oversight (average $600), (2) salary advances structured as personal "
            "loans from agency directors (average $750), and (3) service agreements "
            "with termination penalties enforced under Nepali, not Qatari, law. "
            "Each document is individually legal — a personal loan, an employment "
            "contract registered in Qatar's WPS, a service agreement under Nepal's "
            "Contracts Act — but combined they create a trap where the worker's "
            "actual earnings ($165/month) cannot repay total obligations ($1,350 "
            "debt + $3,300 potential penalty) within the 24-month contract period."
        ),
        "emergent_risk": (
            "Debt bondage through legal instruments spanning two jurisdictions: "
            "dalal fee ($600) + salary advance ($750) + contract substitution "
            "(QAR 1,800→1,200) + accommodation deduction ($110/month) + termination "
            "penalty ($3,300) + agency cash collection ($55/month) = worker trapped "
            "at $165/month net pay for 24 months, unable to leave without forfeiting "
            "family property in Morang."
        ),
        "difficulty": "hard",
        "source_references": [
            "KNOMAD/World Bank, 'Migration and Remittances Data' — recruitment cost surveys: Nepal-Qatar $600-$1,200 actual vs. NPR 10,000 legal max",
            "Nepal Foreign Employment Act 2007 §§ 12, 28, 29, 32 — licensing, fee caps, penalties, salary protection",
            "Qatar Ministerial Decision No. 4/2015 — Wage Protection System (electronic salary payment)",
            "Qatar Ministerial Decision No. 51/2020 — NOC elimination for job mobility",
            "HRW, 'Die First, and I'll Pay You Later' (Dec 4, 2024) — Al Khor labor camps, termination penalty clauses",
            "US State Department TIP Report 2024, Qatar narrative — origin-country collection networks in camps",
            "ILO, 'Employer-Migrant Worker Relationships in the Middle East' (2017) — contract substitution patterns",
            "Issara Institute, 'Top 5 Labour Abuses: A Field-Based Analysis' (2020) — dalal network mapping",
        ],
        "corridors": ["NP-QA", "NP-SA", "NP-AE"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring"],
            "means": ["deception", "debt bondage"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "recruitment_debt_003",
        "name": "Korean EPS Agricultural Worker Broker Fee Layering",
        "category": "recruitment_debt",
        "steps": [
            {
                "id": "rd003_s1",
                "description": (
                    "A Cambodian worker registers through the official Korean "
                    "Employment Permit System (EPS) at the MRC (Manpower Registration "
                    "Center) in Phnom Penh. The government-to-government channel, "
                    "established under Korea's Employment Permit Act 2003, sets an "
                    "official processing fee of approximately $950 (KHR 3.8 million) "
                    "covering EPS-TOPIK language test registration, medical examination, "
                    "skills verification, and visa processing. Korea's HRD Korea "
                    "administers the program with Cambodia's Ministry of Labour and "
                    "Vocational Training (MLVT)."
                ),
                "legal_basis": (
                    "Korea Employment Permit Act 2003, Art. 12 establishes the "
                    "government-to-government recruitment channel to eliminate private "
                    "intermediaries. The Memorandum of Understanding between Korea's "
                    "Ministry of Employment and Labor (MOEL) and Cambodia's MLVT "
                    "(renewed 2023) fixes the official processing fee. ILO C181 "
                    "Art. 7(1) zero-fee principle is partially implemented through "
                    "the EPS structure, which caps fees at cost-recovery levels."
                ),
                "sector": "agriculture",
                "corridor": "KH-KR",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The $950 official fee is reasonable and transparent, but the "
                    "US TIP Report 2024 Cambodia narrative notes that 'despite the "
                    "EPS's government-to-government design, workers reported paying "
                    "$2,000-$5,000 total through informal intermediaries who claim "
                    "to guarantee selection.' Only 5,000-7,000 Cambodian workers "
                    "are selected annually from 30,000+ applicants, creating a "
                    "scarcity that brokers exploit."
                ),
            },
            {
                "id": "rd003_s2",
                "description": (
                    "A local broker in Battambang province who helped the worker "
                    "pass the EPS-TOPIK Korean language proficiency test and navigate "
                    "the MLVT application process charges $3,000 as a 'consulting and "
                    "test preparation' fee. The broker claims to have 'connections' "
                    "at the MLVT and HRD Korea offices in Phnom Penh that can "
                    "influence the computerized lottery selection. The total worker "
                    "cost is now ~$3,950 — over 4x the official $950."
                ),
                "legal_basis": (
                    "Private tutoring and educational consulting are legal businesses "
                    "under Cambodia's Law on Commercial Enterprises (2005). The broker "
                    "is not registered with the MLVT as a licensed recruitment agency "
                    "(which would subject them to the MRC fee schedule). The Employment "
                    "Permit Act Art. 12 explicitly prohibits private intermediary "
                    "involvement in EPS recruitment, but enforcement jurisdiction is "
                    "Korean — Cambodia has no domestic law criminalizing EPS-specific "
                    "broker activity as of 2024."
                ),
                "sector": "agriculture",
                "corridor": "KH-KR",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Broker fee of $3,000 is 3.2x the official cost and represents "
                    "approximately 5 months of the expected Korean agricultural wage "
                    "(KRW 2,060,740/month minimum wage, 2024). The claim of 'connections' "
                    "to influence computerized selection exploits the worker's inability "
                    "to verify the claim. IOM Cambodia's 2020 recruitment mapping "
                    "found 78% of EPS workers used brokers, paying 2-5x official fees."
                ),
            },
            {
                "id": "rd003_s3",
                "description": (
                    "The worker sells 0.5 hectares of family rice paddy in "
                    "Battambang for $2,000 and borrows the remaining $1,950 from "
                    "a village moneylender at 3% monthly interest (36% APR), using "
                    "the family's remaining 1 hectare as collateral. The loan "
                    "agreement is witnessed by the village chief (mekhum) and "
                    "stamped by the commune office, giving it local legal force. "
                    "At 3% monthly compounding, the $1,950 principal grows to "
                    "$2,844 within 12 months."
                ),
                "legal_basis": (
                    "Cambodia's Law on Financial Institutions (2016) regulates "
                    "licensed microfinance institutions but does not cover informal "
                    "village moneylenders. The National Bank of Cambodia has no "
                    "jurisdiction over individual lending. Interest rates for "
                    "informal loans have no legal cap. Land used as collateral is "
                    "governed by the Land Law 2001, Art. 247 (hypothec), but "
                    "informal commune-witnessed agreements often lead to extrajudicial "
                    "land seizure. LICADHO (Cambodian human rights organization) "
                    "documented 5,300 families losing land to microfinance debt "
                    "between 2020-2023."
                ),
                "sector": "agriculture",
                "corridor": "KH-KR",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Family asset liquidation (sold half the farmland) + high-interest "
                    "collateralized loan on the remaining land = catastrophic financial "
                    "risk. If the worker loses the Korean job or is forced to return "
                    "early, the family loses its entire agricultural livelihood. The "
                    "KNOMAD bilateral labor agreements database notes that EPS "
                    "agricultural placements have a 12% early-termination rate due "
                    "to employer changes or workplace injuries."
                ),
            },
            {
                "id": "rd003_s4",
                "description": (
                    "Upon arrival in Chungcheongnam-do province, the worker is "
                    "placed on a remote greenhouse farm growing cherry tomatoes "
                    "with 12 other Cambodian and Vietnamese migrant workers. The "
                    "Korean employer collects all workers' Alien Registration Cards "
                    "(ARCs) and stores them in the farm office, claiming it prevents "
                    "'loss in the fields.' Under EPS rules (Employment Permit Act "
                    "Art. 25), a worker may change employers up to 3 times in a "
                    "4 year 10 month period, but only with the current employer's "
                    "consent or a finding of employer fault by the local Employment "
                    "Center."
                ),
                "legal_basis": (
                    "Korea's Immigration Act Art. 33 requires foreign nationals to "
                    "carry their ARC at all times; employer retention violates this "
                    "provision. The Employment Permit Act Art. 25 allows employer "
                    "changes, but the 2024 US TIP Report Korea narrative states: "
                    "'Workers reported difficulty obtaining employer consent for "
                    "transfer, particularly in agricultural settings where labor "
                    "shortages are acute.' The Korean National Human Rights "
                    "Commission recommended in 2022 that ARC retention be explicitly "
                    "criminalized, but the recommendation has not been enacted."
                ),
                "sector": "agriculture",
                "corridor": "KH-KR",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "ARC retention restricts physical mobility: without the ARC, "
                    "the worker cannot open a bank account, access healthcare, or "
                    "report labor violations to the Employment Center. Combined with "
                    "the remote farm location in Chungcheongnam-do (limited public "
                    "transport), the 3-change limit under Art. 25, and $3,950 in "
                    "debt back in Cambodia, the worker has no practical exit. The "
                    "US TIP Report 2024 identified document retention as the top "
                    "reported abuse in EPS agricultural placements."
                ),
            },
        ],
        "chain_context": (
            "Korea's EPS is recognized by the ILO as a model government-to-government "
            "program that eliminates private intermediaries — in theory. In practice, "
            "the KNOMAD bilateral labor agreements database and US TIP Report 2024 "
            "document a parallel broker ecosystem that adds $2,000-$4,000 to the "
            "official $950 fee. The combination of Battambang-province land collateral, "
            "36% APR village loans, EPS's 3-change employer mobility limit (Art. 25), "
            "and physical ARC retention on remote farms creates a debt-bondage trap "
            "within one of the world's most regulated migration programs. IOM Cambodia "
            "found that the government-to-government channel handled only 22% of "
            "actual recruitment contacts; 78% began with informal brokers."
        ),
        "emergent_risk": (
            "Debt bondage within a regulated program: broker fees 4.2x official cost "
            "($3,950 total vs. $950 official) + family farmland as loan collateral "
            "(36% APR) + restricted employer mobility (3 changes in 4.8 years, "
            "employer consent required) + ARC retention on remote farm = structurally "
            "trapped worker despite EPS's protective design."
        ),
        "difficulty": "expert",
        "source_references": [
            "Korea Employment Permit Act 2003, Art. 12 (government-to-government channel), Art. 25 (employer change limits)",
            "KNOMAD/World Bank, 'Bilateral Labor Agreements Database' — EPS fee surveys, 12% early-termination rate",
            "US State Department TIP Report 2024, Cambodia and Korea narratives — broker fees, ARC retention, employer consent barriers",
            "IOM Cambodia, 'Mapping of Labour Migration Recruitment Practices' (2020) — 78% broker involvement",
            "Korea National Human Rights Commission, 'Recommendation on Migrant Worker Document Retention' (2022)",
            "LICADHO, 'Collateral Damage: Land Loss and Abuses in Cambodia's Microfinance Sector' (2019-2023)",
            "ILO, 'Review of the Employment Permit System in the Republic of Korea' (2023) — structural assessment",
        ],
        "corridors": ["KH-KR", "VN-KR", "MM-KR", "TH-KR"],
        "palermo_elements": {
            "act": ["recruitment"],
            "means": ["abuse of position of vulnerability", "debt bondage"],
            "purpose": ["exploitation", "forced labour"],
        },
    },
    {
        "id": "recruitment_debt_004",
        "name": "Taiwan Fishing Crew Multi-Jurisdiction Fee Splitting",
        "category": "recruitment_debt",
        "steps": [
            {
                "id": "rd004_s1",
                "description": (
                    "An Indonesian fishing crew member from Tegal, Central Java "
                    "pays Rp 7.5 million (~$500) to a local manning agency (P3MI, "
                    "formerly known as PPTKIS) supervised by Indonesia's BP2MI "
                    "(Badan Pelindungan Pekerja Migran Indonesia) for a distant "
                    "water fishing (DWF) vessel contract through Taiwan. The P3MI "
                    "is licensed under Indonesia's Law No. 18/2017 on the Protection "
                    "of Indonesian Migrant Workers. The worker signs a Bahasa "
                    "Indonesia contract in Tegal specifying a $400/month base salary "
                    "for a Kaohsiung-registered tuna longliner operating in the "
                    "Indian Ocean."
                ),
                "legal_basis": (
                    "Indonesia Law No. 18/2017 Art. 30 requires P3MI agencies to be "
                    "licensed by BP2MI and caps placement fees. BP2MI Regulation "
                    "No. 9/2020 sets fee schedules for maritime workers. The $500 "
                    "Indonesia-side fee is within the prescribed schedule. However, "
                    "Taiwan's Fisheries Agency classifies DWF crew under the 'Regulations "
                    "on the Authorization and Management of Overseas Employment of "
                    "Foreign Crew Members' (2017), which operate OUTSIDE Taiwan's "
                    "Labour Standards Act — creating a jurisdictional gap that the "
                    "Taiwan Control Yuan's 2023 investigation specifically flagged."
                ),
                "sector": "fishing",
                "corridor": "ID-TW",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The $500 Indonesia-side fee is compliant, but DWF vessels "
                    "registered in Kaohsiung and Keelung operate under Taiwan's "
                    "Fisheries Agency, not the Ministry of Labor. This means "
                    "Taiwan's Employment Service Act protections (minimum wage, "
                    "document retention prohibition, working hour limits) do not "
                    "apply. EJF's 'Blood and Water' (2019) documented that 92% of "
                    "Indonesian DWF crew paid fees to both origin and destination "
                    "agencies."
                ),
            },
            {
                "id": "rd004_s2",
                "description": (
                    "The P3MI's Taiwan partner company — a Kaohsiung-based manning "
                    "agent registered with Taiwan's Fisheries Agency — charges an "
                    "additional $2,000 'vessel assignment fee' upon the worker's "
                    "arrival at Kaohsiung port. This fee is deducted at $167/month "
                    "over 12 months from the worker's $400/month salary. The Taiwan "
                    "Control Yuan's 2023 investigation found that Kaohsiung and "
                    "Keelung-based manning agents charged DWF crew an average of "
                    "NT$60,000-80,000 ($1,900-$2,500) in destination-side fees not "
                    "reported to BP2MI."
                ),
                "legal_basis": (
                    "Taiwan's Regulations on the Authorization and Management of "
                    "Overseas Employment of Foreign Crew Members (2017) Art. 7 "
                    "requires manning agents to register with the Fisheries Agency "
                    "but does not cap fees charged to foreign crew. Indonesia's "
                    "BP2MI regulates origin-side P3MI fees but has no enforcement "
                    "mechanism for Taiwan-side charges. ILO C188 (Work in Fishing "
                    "Convention, 2007) Art. 22 prohibits fee-charging to fishers, "
                    "but neither Indonesia nor Taiwan has ratified C188."
                ),
                "sector": "fishing",
                "corridor": "ID-TW",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Fee splitting across jurisdictions: Indonesia's BP2MI sees $500; "
                    "Taiwan's Fisheries Agency sees a $2,000 'vessel assignment fee' "
                    "that is legal under its own regulations. Neither regulator sees "
                    "the combined $2,500 burden. Liberty Shared's 'Out of Sight' (2023) "
                    "documented this exact jurisdictional arbitrage in 34 Taiwanese "
                    "DWF manning agencies operating between Kaohsiung and Indonesian "
                    "P3MI networks."
                ),
            },
            {
                "id": "rd004_s3",
                "description": (
                    "The worker signs a USD-denominated contract at Kaohsiung port "
                    "that includes a 'completion bonus' clause: 30% of monthly wages "
                    "($120/month) is withheld and payable only upon completing the "
                    "full 2-year contract. If the worker leaves for any reason — "
                    "including injury, vessel sinking, or abuse — the accumulated "
                    "bonus ($2,880 over 24 months) is forfeited entirely. The "
                    "contract is in Mandarin with no Bahasa Indonesia translation. "
                    "The worker's net monthly pay: $400 - $167 (fee deduction) - "
                    "$120 (bonus withholding) = $113."
                ),
                "legal_basis": (
                    "Completion bonuses in maritime contracts are addressed by ILO "
                    "Maritime Labour Convention 2006, Reg. 2.2 (wages), but MLC 2006 "
                    "applies to merchant shipping, not fishing vessels. The Taiwan "
                    "Fisheries Agency's DWF crew regulations do not prohibit "
                    "completion bonus withholding. The contract's Mandarin-only "
                    "language violates Indonesia's BP2MI Regulation No. 9/2020 "
                    "Art. 15, which requires bilingual contracts — but enforcement "
                    "requires a complaint filed in Jakarta while the worker is at sea."
                ),
                "sector": "fishing",
                "corridor": "ID-TW",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Worker receives $113/month actual cash — 28% of the nominal $400 "
                    "salary. The completion bonus ($2,880 over 2 years) functions as "
                    "a forfeiture penalty: leaving for any reason, including documented "
                    "abuse, triggers total loss. The Taiwan Control Yuan's 2023 "
                    "investigation found that 67% of DWF crew contracts contained "
                    "completion bonus clauses, and only 41% of crew completed full "
                    "contracts — meaning 59% forfeited bonuses worth $1,400-$2,900."
                ),
            },
            {
                "id": "rd004_s4",
                "description": (
                    "Once at sea (Indian Ocean tuna longlining, 200-400 nautical "
                    "miles from the nearest port), the Taiwanese vessel captain "
                    "controls satellite phone access and determines when salary "
                    "transfers are processed through the Kaohsiung manning agent's "
                    "shore office. Remittances to the worker's family in Tegal are "
                    "contingent on the captain's monthly 'performance evaluation' — "
                    "workers rated 'unsatisfactory' have transfers delayed 30-60 days. "
                    "The vessel returns to port approximately every 3-6 months for "
                    "transshipment at sea or brief Kaohsiung/Keelung docking."
                ),
                "legal_basis": (
                    "There is no regulatory framework governing captain-controlled "
                    "wage disbursement on DWF vessels. Taiwan's Fisheries Agency "
                    "Regulations Art. 10 require 'timely payment of wages' but do "
                    "not define a schedule or independent disbursement mechanism. "
                    "ILO C188 Art. 23 (unpaid wages should bear interest) and Art. 24 "
                    "(payment at regular intervals) would address this, but neither "
                    "Taiwan nor Indonesia has ratified C188."
                ),
                "sector": "fishing",
                "corridor": "ID-TW",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Physical isolation at sea + captain-controlled wages = total "
                    "coercive control. EJF's 'Blood and Water' (2019) documented "
                    "cases where Indonesian DWF crew went 4-8 months without receiving "
                    "any payment, with captains citing 'poor catch performance.' "
                    "Liberty Shared (2023) found that 23% of Indonesian DWF crew "
                    "reported being physically prevented from disembarking during "
                    "port calls. The worker's $113/month actual pay, $2,500 in fees, "
                    "and $2,880 forfeitable bonus make reporting abuse financially "
                    "catastrophic."
                ),
            },
        ],
        "chain_context": (
            "Distant water fishing exploits a specific jurisdictional gap: Taiwan's "
            "Fisheries Agency regulates DWF vessels separately from the Ministry of "
            "Labor, so the Employment Service Act's protections (minimum wage NTD 27,470, "
            "document retention prohibition, working hour limits) do not apply to "
            "foreign crew. Indonesia's BP2MI regulates origin-side fees but cannot "
            "enforce Taiwan-side charges or monitor at-sea conditions. The Taiwan "
            "Control Yuan's 2023 investigation examined 1,200 DWF vessels and found "
            "systemic fee-splitting, completion-bonus forfeiture, and captain-controlled "
            "wages across the fleet. EJF documented 24 deaths of Indonesian crew on "
            "Taiwanese DWF vessels between 2015-2019, with families unable to recover "
            "withheld wages or completion bonuses."
        ),
        "emergent_risk": (
            "Multi-jurisdictional debt bondage at sea: Indonesia-side fee ($500) + "
            "Taiwan-side vessel assignment fee ($2,000) + completion bonus withholding "
            "($120/month, $2,880 over 2 years, forfeited on early departure) + "
            "captain-controlled wage disbursement on vessels 200-400nm from shore = "
            "worker receives $113/month actual cash (28% of nominal salary) with "
            "no exit mechanism that doesn't trigger total financial loss."
        ),
        "difficulty": "expert",
        "source_references": [
            "EJF, 'Blood and Water: Human Rights Abuse in the Global Seafood Industry' (2019) — 92% dual-fee payment, 24 crew deaths",
            "Taiwan Control Yuan, 'Investigation Report on Distant Water Fisheries Labor Rights' (2023) — 1,200 vessels examined, 67% completion bonus clauses",
            "Liberty Shared, 'Out of Sight: Modern Slavery in Pacific Supply Chains' (2023) — 34 manning agents, 23% prevented disembarkation",
            "Indonesia Law No. 18/2017 Art. 30 — P3MI licensing and fee caps",
            "Taiwan Fisheries Agency, 'Regulations on the Authorization and Management of Overseas Employment of Foreign Crew Members' (2017) Art. 7, 10",
            "ILO C188, Work in Fishing Convention (2007) Art. 22-24 — not ratified by Taiwan or Indonesia",
            "BP2MI Regulation No. 9/2020 Art. 15 — bilingual contract requirement",
        ],
        "corridors": ["ID-TW", "PH-TW", "VN-TW"],
        "palermo_elements": {
            "act": ["recruitment", "transfer", "harbouring"],
            "means": ["deception", "abuse of position of vulnerability", "debt bondage"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "recruitment_debt_005",
        "name": "Bangladesh-Malaysia Electronics Factory Fee Cascade",
        "category": "recruitment_debt",
        "steps": [
            {
                "id": "rd005_s1",
                "description": (
                    "A BMET-registered recruiting agent (Bureau of Manpower, "
                    "Employment and Training, under Bangladesh's Ministry of "
                    "Expatriates' Welfare) in Dhaka's Eskaton area charges BDT "
                    "350,000 (~$3,200) for a factory job in Malaysia's Penang "
                    "Free Trade Zone. The BMET fee cap is BDT 84,000 (~$770) "
                    "under the Emigration Ordinance 1982 schedule. The worker "
                    "initially contacted a dalal (informal broker) in Comilla "
                    "district who collected BDT 100,000 (~$910) before referring "
                    "him to the Dhaka agent. Total cost: ~$4,100 — 5.3x the legal "
                    "cap. The worker's family takes a loan from a Grameen-model "
                    "MFI at 23% flat annual interest."
                ),
                "legal_basis": (
                    "Bangladesh Emigration Ordinance 1982 § 20, as amended, caps "
                    "recruiting agent fees at BDT 84,000 for Malaysia placements. "
                    "The 2023 amendment to the Overseas Employment and Migrants Act "
                    "requires dalals to register as sub-agents of licensed companies, "
                    "but IOM Bangladesh's January 2020 'Mapping of Labour Migration "
                    "Recruitment Practices' found fewer than 2% of dalals had "
                    "formalized. BMET has 1,200+ registered agents; the government "
                    "estimates 20,000-100,000 active dalals."
                ),
                "sector": "manufacturing",
                "corridor": "BD-MY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Fee is 5.3x the BMET legal cap. IOM Bangladesh (2020) found "
                    "the average cost for BD-MY migration was $3,000-$4,000, with "
                    "dalal networks accounting for 30-40% of total cost. The 2023 "
                    "sub-agent licensing law has had minimal impact: US TIP Report "
                    "2024 Bangladesh narrative states 'the government did not "
                    "prosecute any licensed recruiting agencies or sub-agents for "
                    "excessive fee charging.' Family MFI loan at 23% flat interest "
                    "on $4,100 adds $943 annually."
                ),
            },
            {
                "id": "rd005_s2",
                "description": (
                    "Upon arrival in Penang, the outsourcing company (a Malaysian "
                    "contractor licensed under the Private Employment Agencies Act "
                    "1981) that manages foreign workers for a multinational "
                    "electronics factory charges an additional RM 2,800 (~$600) "
                    "'levy advance.' Under Malaysia's Foreign Workers Act, the "
                    "annual levy (RM 1,850 for manufacturing sector) is the "
                    "employer's legal obligation, but outsourcing companies "
                    "routinely pass this cost to workers as a 'reimbursable advance.' "
                    "The Johor Bahru Labour Court case (2022) ordered RM 1.1 million "
                    "back wages for 733 Bangladeshi workers whose outsourcing company "
                    "had deducted levy costs — approximately $240,000 (RM 240,000 per "
                    "worker average = ~$327 each)."
                ),
                "legal_basis": (
                    "Malaysia Employment Act 1955 § 24(1) prohibits deductions not "
                    "authorized by the Act. The Immigration Act 1959/63 § 55E assigns "
                    "levy liability to the employer, not the worker. However, the "
                    "Private Employment Agencies Act 1981 allows outsourcing companies "
                    "to operate as 'employers' of foreign workers, creating a legal "
                    "grey zone where the outsourcing company (not the factory) is the "
                    "worker's de jure employer and can structure 'reimbursable advances.' "
                    "The 2024 US TIP Report Malaysia narrative identifies levy pass-"
                    "through as the most common forced labor indicator."
                ),
                "sector": "manufacturing",
                "corridor": "BD-MY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Levy pass-through adds $600 to existing $4,100 debt. Total: "
                    "$4,700. The Johor Bahru case (733 workers, RM 1.1 million "
                    "judgment) demonstrated the practice is widespread and illegal "
                    "but rarely prosecuted — the case was a civil action initiated "
                    "by an NGO (Tenaganita), not government enforcement. Verité's "
                    "forced labor in electronics supply chain report found 32% of "
                    "Malaysian electronics factory foreign workers had levy costs "
                    "passed through by outsourcing companies."
                ),
            },
            {
                "id": "rd005_s3",
                "description": (
                    "The Penang FTZ electronics factory provides worker dormitory "
                    "housing — 12 workers per room (6 double-decker bunks) in a "
                    "converted warehouse adjacent to the factory — with mandatory "
                    "monthly deduction of RM 350 (~$75) from the worker's RM 1,500 "
                    "(~$325) base salary for 'accommodation, utilities, and meals' "
                    "(two meals per day from a centralized canteen). The worker "
                    "cannot opt out of company housing because the work permit (Visit "
                    "Pass for Temporary Employment) is tied to the employer's "
                    "registered address."
                ),
                "legal_basis": (
                    "Malaysia Employment Act 1955 § 24(2)(e) permits deductions for "
                    "'the provision of food, fuel, water, light, medical attendance or "
                    "rent' with worker agreement. The Workers' Minimum Standards of "
                    "Housing and Amenities Act 1990 (Act 446) sets minimum standards "
                    "(36 sq ft per person, adequate ventilation) but enforcement "
                    "inspections in Penang FTZ housing averaged once per 4 years "
                    "according to the 2024 US TIP Report Malaysia supplementary data."
                ),
                "sector": "manufacturing",
                "corridor": "BD-MY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Housing deduction (RM 350) represents 23% of base salary on top "
                    "of $4,700 debt. Net monthly pay after housing: RM 1,150 (~$250). "
                    "The tied work-permit/housing arrangement means the worker cannot "
                    "choose cheaper housing or live independently. Issara Institute's "
                    "'Top 5 Labour Abuses' (2020) ranked mandatory employer housing "
                    "with above-market deductions as the #2 reported abuse in Malaysian "
                    "electronics, after excessive overtime."
                ),
            },
            {
                "id": "rd005_s4",
                "description": (
                    "The outsourcing company holds all 733 Bangladeshi workers' "
                    "passports in a locked cabinet in the company's Penang office, "
                    "described in the employment handbook as a 'centralized document "
                    "storage system for worker protection against theft.' Workers "
                    "must submit a written request 7 days in advance to retrieve "
                    "their passport, with approval at the 'discretion of the HR "
                    "manager.' The 2024 US TIP Report Malaysia narrative states: "
                    "'Passport confiscation remains the most pervasive indicator "
                    "of forced labor, affecting an estimated 30-50% of migrant "
                    "workers in manufacturing.'"
                ),
                "legal_basis": (
                    "Malaysia's Passports Act 1966 § 12 makes it an offense to "
                    "retain another person's passport, punishable by fine up to "
                    "RM 10,000. The Anti-Trafficking in Persons and Anti-Smuggling "
                    "of Migrants Act 2007 (ATIPSOM) § 13A specifically lists "
                    "document retention as a trafficking indicator. However, the "
                    "2024 US TIP Report notes that 'the government did not report "
                    "any prosecutions under § 12 of the Passports Act for employer "
                    "retention of migrant worker documents.'"
                ),
                "sector": "manufacturing",
                "corridor": "BD-MY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Triple lock on worker mobility: (1) passport retained by "
                    "outsourcing company, (2) $4,700 debt with 23% interest accruing "
                    "in Bangladesh, (3) work permit tied to this specific employer. "
                    "Leaving means losing the passport (no way to leave Malaysia), "
                    "defaulting on the debt (family's MFI loan in Comilla), and "
                    "becoming undocumented (visa cancellation). The Johor Bahru "
                    "case documented identical conditions for 733 workers at a "
                    "single outsourcing company — suggesting systematic rather "
                    "than isolated practice."
                ),
            },
        ],
        "chain_context": (
            "Malaysia's outsourcing company model inserts a legal intermediary between "
            "the multinational electronics factory (which passes brand audits) and the "
            "migrant worker (who experiences the actual conditions). IOM Bangladesh "
            "(2020) documented 4 layers in the BD-MY corridor: (1) village dalal in "
            "Comilla ($910), (2) BMET-registered Dhaka agent ($3,200), (3) Malaysian "
            "outsourcing company levy pass-through ($600), (4) mandatory housing "
            "deduction ($75/month). Supply chain auditors inspect the factory floor "
            "but not the outsourcing company's dormitories or financial practices. "
            "Verité found that 47% of electronics factories in Penang FTZ used "
            "outsourcing companies for foreign worker management, and none of the "
            "factories' published supplier responsibility reports mentioned outsourcing "
            "company fee practices."
        ),
        "emergent_risk": (
            "Debt bondage through outsourcing intermediary: dalal fee ($910) + "
            "BMET agent fee ($3,200, 5.3x legal cap) + levy pass-through ($600) + "
            "housing deduction ($75/month) + passport retention + tied work permit "
            "= worker trapped at ~$250/month net pay against $4,700 debt with 23% "
            "annual interest. Outsourcing company structure shields the brand factory "
            "from liability."
        ),
        "difficulty": "medium",
        "source_references": [
            "IOM Bangladesh, 'Mapping of Labour Migration Recruitment Practices' (Jan 2020) — $3,000-$4,000 average cost, 4-layer chain",
            "Issara Institute, 'Top 5 Labour Abuses: A Field-Based Analysis of Worker Reporting' (2020) — mandatory housing #2 abuse",
            "US State Department TIP Report 2024, Malaysia and Bangladesh narratives — levy pass-through, passport retention, prosecution gaps",
            "Verité, 'Forced Labor in the Production of Electronic Goods in Malaysia' — 32% levy pass-through, 47% outsourcing use in Penang FTZ",
            "Bangladesh Emigration Ordinance 1982 § 20 — BDT 84,000 fee cap; 2023 sub-agent licensing amendment",
            "Malaysia Employment Act 1955 § 24; Passports Act 1966 § 12; ATIPSOM 2007 § 13A",
            "Johor Bahru Labour Court (2022) — 733 workers, RM 1.1 million back wages, Tenaganita-initiated",
            "ILO, 'Triangle in ASEAN Programme: Quarterly Briefing Note on Malaysia' (2023)",
        ],
        "corridors": ["BD-MY", "NP-MY", "MM-MY", "ID-MY"],
        "palermo_elements": {
            "act": ["recruitment", "transfer", "harbouring"],
            "means": ["deception", "debt bondage", "retention of identity documents"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "recruitment_debt_006",
        "name": "Ethiopia-Lebanon Domestic Worker Kafala Debt Spiral",
        "category": "recruitment_debt",
        "steps": [
            {
                "id": "rd006_s1",
                "description": (
                    "An Ethiopian domestic worker pays ETB 120,000 (~$1,000) to a "
                    "licensed employment agency in the Bole sub-city area of Addis "
                    "Ababa, plus ETB 60,000 (~$500) for mandatory medical tests "
                    "(GAMCA/GCC Approved Medical Centers Association), document "
                    "authentication at the Ministry of Foreign Affairs, and a PCC "
                    "(Police Clearance Certificate) for a Lebanon domestic worker "
                    "placement. Total: ~$1,500. Ethiopia's Overseas Employment "
                    "Proclamation No. 923/2016 requires agencies to be licensed by "
                    "the Ministry of Labour and Social Affairs (MOLSA) and caps "
                    "service charges, but the US TIP Report 2024 Ethiopia narrative "
                    "states 'the government did not effectively enforce fee limits.'"
                ),
                "legal_basis": (
                    "Ethiopia Proclamation No. 923/2016 Art. 18 regulates private "
                    "employment agencies and requires licensing. Art. 19 sets fee "
                    "schedules based on destination country. However, the 2018 ban "
                    "on domestic worker migration to Middle East (following multiple "
                    "worker deaths in Lebanon and Saudi Arabia) was partially lifted "
                    "in 2022 with new bilateral agreements — creating a period where "
                    "agencies operated in a regulatory grey zone. ILO C181 Art. 7(1) "
                    "zero-fee principle applies but Ethiopia has not ratified C181."
                ),
                "sector": "domestic_work",
                "corridor": "ET-LB",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Total $1,500 represents 8-10 months of expected Lebanese salary "
                    "($150-$200/month for domestic workers). The worker is already in "
                    "debt before departure. Anti-Slavery International's 2024 Kafala "
                    "reform analysis found that Ethiopian agencies in Bole sub-city "
                    "charged 2-3x more than the Proclamation No. 923/2016 schedule, "
                    "with MOLSA conducting only 12 agency inspections nationwide "
                    "in 2023."
                ),
            },
            {
                "id": "rd006_s2",
                "description": (
                    "The Lebanese kafeel (sponsor/employer) in the Achrafieh district "
                    "of Beirut paid the Lebanese recruitment agency $2,000 for the "
                    "worker's placement and expects to 'recover this investment' "
                    "through the worker's first year of employment. Under Lebanon's "
                    "kafala system, the sponsor holds legal responsibility for the "
                    "worker's immigration status — and views the $2,000 fee as a "
                    "sunk cost that the worker must 'earn back.' The General "
                    "Security office processes the worker's visa with the sponsor "
                    "as guarantor; the worker cannot change employers without the "
                    "sponsor's written release (naqal kafala)."
                ),
                "legal_basis": (
                    "Lebanon has no comprehensive labor law covering domestic "
                    "workers — they are explicitly excluded from the Lebanese Labour "
                    "Code (1946) Art. 7(1). The kafala system operates under General "
                    "Security regulations, not labor law. The 2009 Unified Standard "
                    "Contract for domestic workers sets a minimum salary and basic "
                    "conditions but is poorly enforced. The ILO's 'Intertwined' "
                    "report (2021) found that 60% of Lebanese employers viewed "
                    "recruitment fees as a 'purchase price' entitling them to "
                    "control the worker."
                ),
                "sector": "domestic_work",
                "corridor": "ET-LB",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Dual debt structure: worker owes $1,500 to the Addis Ababa "
                    "agent; sponsor considers $2,000 an 'investment' to be recovered "
                    "through the worker's labor. The kafala tie means the worker "
                    "cannot leave the sponsor without a release document (naqal "
                    "kafala), which the sponsor has no incentive to grant during "
                    "the 'recovery period.' Anti-Slavery International documented "
                    "63% of Ethiopian domestic workers in Lebanon unable to leave "
                    "their employer within the first year due to fee-recovery claims."
                ),
            },
            {
                "id": "rd006_s3",
                "description": (
                    "The worker's contract (processed through General Security in "
                    "Beirut) specifies $200/month for a 2-year term. However, the "
                    "sponsor imposes a 3-month 'probation period' during which no "
                    "salary is paid — only room and board in the sponsor's Achrafieh "
                    "apartment. The sponsor states this is to 'test suitability' "
                    "and to recoup recruitment costs. The worker lives in a converted "
                    "storage room (no window, no lock) and works 16-18 hours per day "
                    "caring for 3 children and cleaning the household."
                ),
                "legal_basis": (
                    "Lebanon's 2009 Unified Standard Contract for domestic workers "
                    "Art. 5 sets a 3-month probation period but does NOT authorize "
                    "withholding salary during probation. The contract requires "
                    "payment from day one. However, the 2024 US TIP Report Lebanon "
                    "narrative states: 'The government did not investigate or "
                    "prosecute any cases of wage theft from domestic workers. General "
                    "Security officers routinely returned workers to abusive sponsors "
                    "rather than pursuing complaints.' The ILO's 2021 Lebanon study "
                    "found 88% of domestic workers reported wage irregularities in "
                    "the first 6 months."
                ),
                "sector": "domestic_work",
                "corridor": "ET-LB",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Three months of unpaid labor ($600 in withheld wages) effectively "
                    "subsidizes the sponsor's $2,000 recruitment 'investment.' The "
                    "worker has no resources, no mobility (passport held by sponsor), "
                    "and no recourse (domestic workers excluded from Labour Code). "
                    "HRW's 2020 Lebanon investigation documented that 74% of Ethiopian "
                    "domestic workers had salaries withheld for 1-6 months after arrival."
                ),
            },
            {
                "id": "rd006_s4",
                "description": (
                    "After the 3-month probation, the sponsor pays $150/month (not "
                    "the contracted $200), claiming $50/month is deducted for 'agency "
                    "loan repayment' sent directly to the Addis Ababa agent's account "
                    "via Western Union. The sponsor also withholds $15/month for "
                    "'phone calls to Ethiopia' (the worker is allowed one 10-minute "
                    "call per week on the sponsor's phone). Net pay: $135/month. "
                    "At $50/month repayment, the $1,500 Ethiopian-side debt takes "
                    "30 months to clear — 6 months beyond the 24-month contract."
                ),
                "legal_basis": (
                    "Lebanon's 2009 Unified Standard Contract Art. 7 prohibits "
                    "deductions not specified in the original contract. The $50 "
                    "monthly deduction for agency loan repayment is based on a "
                    "separate agreement signed in Addis Ababa, outside Lebanese "
                    "jurisdiction. Ethiopia's Proclamation No. 923/2016 Art. 22 "
                    "requires agencies to ensure workers receive their full "
                    "contracted salary, but enforcement requires a complaint filed "
                    "at MOLSA in Addis Ababa — which the worker, confined in "
                    "Achrafieh with no passport, cannot access."
                ),
                "sector": "domestic_work",
                "corridor": "ET-LB",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Net pay $135/month while total debt was $1,500 to the Ethiopian "
                    "agent (30-month repayment exceeds 24-month contract) plus the "
                    "sponsor's $2,000 'investment' claim enforced through kafala tie. "
                    "Combined: 3 months unpaid ($600 wage theft) + 21 months at "
                    "$135/month = $2,835 total earnings over 2 years, minus $1,500 "
                    "debt repayment = $1,335 net for 24 months of work. The sponsor's "
                    "$2,000 is 'recovered' through $600 unpaid labor + $50/month "
                    "salary differential × 21 months = $1,650 total extraction."
                ),
            },
        ],
        "chain_context": (
            "The kafala system creates a legal architecture where both the Ethiopian "
            "sending side and the Lebanese receiving side extract fees from the worker "
            "through separate legal instruments operating under different jurisdictions. "
            "The Addis Ababa agency (Proclamation 923/2016), the Beirut General "
            "Security office (kafala regulations), and the Unified Standard Contract "
            "each appear independently lawful. But the ILO's 'Intertwined' report "
            "(2021) found the combined effect is that Ethiopian domestic workers in "
            "Lebanon earn an average of $1,200 in the first year (against $2,400 "
            "contracted) — a 50% extraction rate across the intermediary chain. "
            "Anti-Slavery International tracked 200 Ethiopian domestic workers in "
            "Beirut and found 91% experienced at least one indicator of forced labor "
            "in the first 12 months."
        ),
        "emergent_risk": (
            "Bilateral debt bondage under kafala: Ethiopian agency fee ($1,500) + "
            "Lebanese sponsor 'investment recovery' ($2,000 via 3-month unpaid "
            "probation + salary deductions) + kafala-tied visa (no employer mobility "
            "without naqal kafala) + passport retention + domestic worker exclusion "
            "from Lebanese Labour Code = 13+ months before any real earnings, with "
            "debt mathematically exceeding contract period."
        ),
        "difficulty": "medium",
        "source_references": [
            "Anti-Slavery International, 'Kafala Reform Analysis: Lebanon, Qatar, Saudi Arabia' (2024) — 63% immobility rate, Bole sub-city agency practices",
            "ILO, 'Intertwined: A Study of Employers of Migrant Domestic Workers in Lebanon' (2021) — 60% 'purchase price' perception, 50% extraction rate",
            "US State Department TIP Report 2024, Lebanon and Ethiopia narratives — prosecution gaps, General Security practices",
            "Ethiopia Proclamation No. 923/2016 Art. 18, 19, 22 — agency licensing, fee schedules, salary protection",
            "Lebanon Unified Standard Contract for Domestic Workers (2009) Art. 5, 7 — probation, deduction prohibitions",
            "Lebanese Labour Code (1946) Art. 7(1) — domestic worker exclusion",
            "HRW, 'Without Protection: How the Lebanese Justice System Fails Migrant Domestic Workers' (2020) — 74% salary withholding",
        ],
        "corridors": ["ET-LB", "ET-SA", "ET-KW", "ET-AE"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring"],
            "means": ["debt bondage", "abuse of position of vulnerability"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "recruitment_debt_007",
        "name": "Vietnam-Japan Technical Intern Training Program Fee Trap",
        "category": "recruitment_debt",
        "steps": [
            {
                "id": "rd007_s1",
                "description": (
                    "A Vietnamese worker from Nghe An province enrolls in a DOLAB-"
                    "licensed dispatch organization (to chuc phai cu) in Hanoi that "
                    "sends workers to Japan under the Technical Intern Training Program "
                    "(TITP, gino jisshu seido). The dispatch organization charges "
                    "$5,000-$8,000 in combined fees: Japanese language training (N4 "
                    "level, 6-12 months), skills pre-assessment, medical examination, "
                    "passport processing, and 'program management.' DOLAB (Department "
                    "of Overseas Labour, under Vietnam's Ministry of Labour, Invalids "
                    "and Social Affairs) licenses approximately 500 dispatch "
                    "organizations. The fee equals 3-4 years of the worker's current "
                    "income in Nghe An (average VND 4-5 million/month, ~$160-$200)."
                ),
                "legal_basis": (
                    "Vietnam's Law on Vietnamese Workers Working Abroad under Contract "
                    "(Law No. 69/2020/QH14) Art. 7 regulates dispatch organization "
                    "fees. DOLAB Circular No. 21/2007/TT-BLDTBXH (amended 2020) caps "
                    "service fees at 'one month's salary per year of contract' — i.e., "
                    "~$1,200 for a 3-year TITP placement. The $5,000-$8,000 actual "
                    "charge is 4-7x the legal cap. Japan's Technical Intern Training "
                    "Act 2017 established OTIT (Organization for Technical Intern "
                    "Training) to supervise the program, but OTIT has no jurisdiction "
                    "over Vietnamese dispatch organization fees."
                ),
                "sector": "manufacturing",
                "corridor": "VN-JP",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Fees of $5,000-$8,000 are 4-7x the DOLAB legal cap and represent "
                    "3-4 years of Vietnamese wages. KNOMAD recruitment cost surveys "
                    "rank the VN-JP TITP corridor as one of the 5 most expensive "
                    "migration routes globally. The US TIP Report 2024 Japan narrative "
                    "states: 'Vietnamese technical interns reported the highest "
                    "recruitment fees among all TITP nationalities, driven by "
                    "dispatch organization overcharging in Hanoi and Ho Chi Minh City.'"
                ),
            },
            {
                "id": "rd007_s2",
                "description": (
                    "The worker's family in Nghe An pledges their house (valued at "
                    "VND 500 million, ~$20,000) as collateral for a loan from a "
                    "local bank to cover the $7,000 dispatch fee. The family also "
                    "signs a 'performance bond' (giay cam ket) with the dispatch "
                    "organization imposing a VND 120 million (~$5,000) penalty if "
                    "the worker leaves the TITP program before completing the 3-year "
                    "term — for any reason, including documented abuse. The dispatch "
                    "organization holds the original performance bond; the family "
                    "keeps a copy. Total financial exposure: $12,000 ($7,000 fee + "
                    "$5,000 penalty) against a Japanese monthly salary of ~$1,000-$1,200."
                ),
                "legal_basis": (
                    "Vietnam Civil Code 2015 Art. 317-325 governs hypothec (mortgage) "
                    "transactions and collateral requirements. The bank loan secured "
                    "by the house is a standard consumer credit product. The "
                    "performance bond, however, violates Vietnam's Law No. 69/2020 "
                    "Art. 7(3) which prohibits dispatch organizations from 'collecting "
                    "deposits or requiring collateral from workers.' But enforcement "
                    "requires a complaint to DOLAB, and the dispatch organization's "
                    "local influence in Nghe An — where it is often the largest "
                    "employer in the district — deters reporting."
                ),
                "sector": "manufacturing",
                "corridor": "VN-JP",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Family home at risk + $5,000 penalty creates impossibility of "
                    "leaving the TITP program regardless of conditions. Total exposure "
                    "$12,000 on ~$1,000-$1,200/month Japanese salary. The US TIP "
                    "Report 2024 Japan narrative documented that 'Vietnamese interns "
                    "reported performance bonds averaging $3,000-$7,000, with family "
                    "homes as collateral, as the primary barrier to reporting abuse.' "
                    "OTIT's 2023 annual report recorded 9,753 TITP runaways (mostly "
                    "Vietnamese), many of whom cited fear of penalty bond enforcement "
                    "as the reason for absconding rather than filing a formal complaint."
                ),
            },
            {
                "id": "rd007_s3",
                "description": (
                    "In Japan, the supervising organization (kanri dantai) in Aichi "
                    "prefecture's manufacturing belt — which partners with the Hanoi "
                    "dispatch organization — deducts JPY 30,000 (~$200)/month from "
                    "the worker's gross salary of JPY 170,000 (~$1,130) as 'management "
                    "and support fees' (kanri hi). The worker receives a pre-loaded "
                    "Suica-type IC card instead of cash or bank transfer for the "
                    "remaining JPY 140,000 (~$930). From this, the worker remits "
                    "~$500/month to service the bank loan in Vietnam and support "
                    "the family, leaving ~$430/month for living expenses in one of "
                    "the world's most expensive countries."
                ),
                "legal_basis": (
                    "Japan's Technical Intern Training Act 2017 Art. 28 authorizes "
                    "supervising organizations to charge 'necessary expenses' but "
                    "does not cap the amount. OTIT's implementation guidelines state "
                    "fees should be 'reasonable' without defining a number. Japan's "
                    "Labour Standards Act Art. 24 requires wages to be paid 'in full, "
                    "directly to the worker, in currency' — the pre-loaded IC card "
                    "potentially violates the 'currency' requirement, but OTIT has "
                    "issued no enforcement action on electronic payment methods for "
                    "TITP workers as of 2024."
                ),
                "sector": "manufacturing",
                "corridor": "VN-JP",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "JPY 30,000/month management fee ($200) on top of $7,000 origin-"
                    "country debt creates continuous financial drain: over 3 years, "
                    "the supervising organization extracts $7,200. The pre-loaded IC "
                    "card can be restricted to specific merchants and does not build "
                    "a bank transaction history the worker can use as wage evidence in "
                    "a dispute. The US TIP Report 2024 Japan narrative identified "
                    "supervising organization fees and pre-loaded cards as indicators "
                    "of forced labor in TITP. OTIT received 11,032 consultations from "
                    "TITP workers in fiscal year 2023, the majority regarding fee and "
                    "wage disputes."
                ),
            },
        ],
        "chain_context": (
            "Japan's TITP has been consistently criticized by the US State Department "
            "(Tier 2 Watch List placement in 2024, partly due to TITP), the ILO, and "
            "the UN Special Rapporteur on contemporary forms of slavery. While each "
            "component is technically legal — DOLAB-licensed dispatch organizations, "
            "OTIT-registered supervising organizations, bank-originated housing loans "
            "— the total fee burden ($7,000 dispatch fee + $5,000 penalty bond + "
            "$7,200 in supervising organization fees over 3 years = $19,200 total "
            "extraction) against a $1,130/month salary creates mathematical debt "
            "bondage. Japan's own TITP Review Panel (2022) recommended abolishing "
            "the program, and the June 2024 reform bill renamed it the 'Skilled Worker "
            "Training Program' (ikusei shuro seido) — but retained the supervising "
            "organization fee structure."
        ),
        "emergent_risk": (
            "Structural debt bondage through a legal training program: DOLAB dispatch "
            "fee ($5,000-$8,000, 4-7x legal cap) + family home as bank loan collateral "
            "+ $5,000 performance bond (forfeited on early departure for any reason) + "
            "JPY 30,000/month supervising organization fee in Aichi + pre-loaded IC "
            "card wage payment = 3-year debt trap where the worker nets ~$430/month "
            "for living expenses in Japan while $12,000+ in obligations ensure "
            "compliance regardless of working conditions."
        ),
        "difficulty": "hard",
        "source_references": [
            "US State Department TIP Report 2024, Japan narrative — TITP Tier 2 Watch List, Vietnamese intern fees, performance bonds",
            "Japan Technical Intern Training Act 2017 Art. 28 — supervising organization fee authorization",
            "OTIT Annual Report Fiscal Year 2023 — 9,753 runaways, 11,032 consultations",
            "Vietnam Law No. 69/2020/QH14 Art. 7 — dispatch organization fee caps, deposit prohibition",
            "DOLAB Circular No. 21/2007/TT-BLDTBXH (amended 2020) — one-month-salary-per-year fee cap",
            "KNOMAD/World Bank, 'Migration and Remittances Data' — VN-JP ranked top-5 most expensive corridor",
            "Japan TITP Review Panel (2022) — recommendation to abolish the program",
            "ILO, 'Assessment of the Technical Intern Training Programme in Japan' (2023)",
        ],
        "corridors": ["VN-JP", "CN-JP", "PH-JP", "ID-JP"],
        "palermo_elements": {
            "act": ["recruitment", "transfer"],
            "means": ["debt bondage", "abuse of position of vulnerability", "coercion"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "recruitment_debt_008",
        "name": "Central America to US H-2A Agricultural Visa Fee Chain",
        "category": "recruitment_debt",
        "steps": [
            {
                "id": "rd008_s1",
                "description": (
                    "A Guatemalan agricultural worker from Huehuetenango department "
                    "pays Q 16,000 (~$2,100) to a local recruiter ('reclutador') for "
                    "an H-2A seasonal visa position picking blueberries on a farm in "
                    "southeast Georgia. The reclutador is an informal intermediary who "
                    "works on commission from a US-based farm labor contractor (FLC) "
                    "registered with the US Department of Labor. Under 20 CFR § 655.135(j), "
                    "H-2A employers are prohibited from seeking or receiving payment "
                    "'of any kind' from workers for any activity related to obtaining "
                    "H-2A labor certification — making the $2,100 fee illegal under "
                    "US law, though the reclutador operates in Guatemala beyond DOL "
                    "enforcement reach."
                ),
                "legal_basis": (
                    "Immigration and Nationality Act § 218, implemented through "
                    "20 CFR § 655.135(j): 'The employer and its agents have not "
                    "sought or received payment of any kind from the worker for any "
                    "activity related to obtaining H-2A labor certification.' The "
                    "TVPA (Trafficking Victims Protection Act) of 2000, as amended "
                    "2008, § 1589 defines 'forced labor' to include obtaining labor "
                    "'by means of serious harm or threats of serious harm to any "
                    "person, or by means of any scheme, plan, or pattern intended to "
                    "cause the person to believe that failure to perform such labor "
                    "would result in serious harm.' DOL WHD (Wage and Hour Division) "
                    "has jurisdiction but conducts ~2,400 H-2A investigations "
                    "annually against 11,000+ certified employers."
                ),
                "sector": "agriculture",
                "corridor": "GT-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Fee is 100% illegal under US H-2A regulations but enforcement "
                    "does not reach Guatemalan reclutadores. Centro de los Derechos "
                    "del Migrante (CDM) surveys found 63% of Mexican and Central "
                    "American H-2A workers paid recruitment fees averaging $590-$2,400, "
                    "despite the explicit zero-fee requirement. The worker borrowed "
                    "from a local coyote-affiliated lender in Huehuetenango at 10% "
                    "monthly interest. Polaris Project's H-2A analysis found that "
                    "Guatemalan workers paid the highest average fees among H-2A "
                    "nationalities ($1,800-$2,500)."
                ),
            },
            {
                "id": "rd008_s2",
                "description": (
                    "The worker travels to Guatemala City for the US Embassy visa "
                    "interview, then to the US consulate in Monterrey, Mexico (a "
                    "common secondary processing location for H-2A applicants when "
                    "Guatemala City appointment slots are unavailable). Total travel "
                    "costs: Q 4,000 (~$520) for intercity buses, 3 nights' lodging, "
                    "meals, MRV visa fee ($190), and a 'consulate preparation package' "
                    "($125) sold by the reclutador's associate in Monterrey who "
                    "coaches workers on interview responses."
                ),
                "legal_basis": (
                    "The MRV (Machine Readable Visa) fee of $190 is a US government "
                    "charge that 20 CFR § 655.135(j) classifies as a 'worker expense' "
                    "the employer need not reimburse. Travel to the consulate is "
                    "similarly classified. However, the DOL Office of Inspector "
                    "General's 2023 audit found that 'the distinction between "
                    "reimbursable recruitment costs and non-reimbursable consulate "
                    "travel costs creates a loophole exploited by labor contractors "
                    "who route workers through distant consulates to inflate travel "
                    "expenses.' The 'consulate preparation' service is unregulated."
                ),
                "sector": "agriculture",
                "corridor": "GT-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Monterrey routing adds $200-$300 in unnecessary travel costs "
                    "over a Guatemala City appointment. The 'consulate preparation "
                    "package' ($125) exploits the worker's fear of visa denial — "
                    "which would mean $2,100 in non-recoverable recruitment fees. "
                    "Total debt now: $2,620 ($2,100 + $520) at 10% monthly interest "
                    "from a Huehuetenango lender. CDM documented that 41% of H-2A "
                    "workers were routed through consulates other than their nearest "
                    "embassy, adding an average $350 in travel costs."
                ),
            },
            {
                "id": "rd008_s3",
                "description": (
                    "Upon arrival at the southeast Georgia blueberry farm, the "
                    "farm labor contractor (FLC) places the worker in a shared "
                    "single-wide trailer with 11 other workers (6 bunks in a "
                    "3-bedroom unit), deducting $50/week ($200/month) from the "
                    "worker's piece-rate earnings for 'housing and transportation.' "
                    "Under 20 CFR § 655.122(d), H-2A employers must provide free "
                    "housing or a housing allowance at no cost to the worker. The "
                    "FLC claims the $50/week covers 'optional upgraded amenities' "
                    "(air conditioning, weekly town shuttle) that exceed the H-2A "
                    "minimum housing standard."
                ),
                "legal_basis": (
                    "20 CFR § 655.122(d)(1): H-2A employers must provide housing "
                    "at no cost to workers who are 'not reasonably able to return "
                    "to their residence within the same day.' ETA Form 790 housing "
                    "inspection certifies the dwelling meets OSHA standards (29 CFR "
                    "§ 1910.142). The FLC's '$50/week for optional upgrades' framing "
                    "has been rejected in DOL enforcement actions — WHD v. Vasquez "
                    "Citrus & Hauling (2019) ruled that any housing charges to H-2A "
                    "workers violate the regulation regardless of 'upgrade' labeling."
                ),
                "sector": "agriculture",
                "corridor": "GT-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Housing deduction ($200/month) directly violates H-2A regulations "
                    "per WHD v. Vasquez Citrus precedent. Worker is in a remote rural "
                    "area of southeast Georgia with no personal vehicle, no public "
                    "transit, and no knowledge of the local area. The $50/week town "
                    "shuttle is the only way to access a store, Western Union, or "
                    "phone — and it is controlled by the FLC. DOL WHD's 2023 H-2A "
                    "enforcement data shows housing violations in 38% of investigated "
                    "cases, with average back wages of $1,247 per affected worker."
                ),
            },
            {
                "id": "rd008_s4",
                "description": (
                    "The worker's piece-rate pay for blueberry picking averages "
                    "$300-$350/week. The H-2A Adverse Effect Wage Rate (AEWR) for "
                    "Georgia in 2024 is $13.67/hour; at a 40-hour week, the AEWR "
                    "guarantee is $546.80/week. The FLC's payroll records show the "
                    "AEWR supplement ('guarantee make-up') but the supervisor tells "
                    "workers that accepting the guarantee payment 'will cause problems "
                    "with your visa next year — we only bring back the fast pickers.' "
                    "Workers who request the AEWR make-up are assigned the poorest "
                    "rows (already picked over) the following week, effectively "
                    "reducing their future piece-rate earnings."
                ),
                "legal_basis": (
                    "20 CFR § 655.122(l): H-2A employers must guarantee the AEWR "
                    "as a minimum regardless of piece-rate earnings. The 'three-"
                    "fourths guarantee' (20 CFR § 655.122(i)) requires employers to "
                    "guarantee at least 75% of the total work hours stated in the "
                    "contract. The supervisor's implicit threat about future visa "
                    "eligibility constitutes potential 'abuse of the legal process' "
                    "under TVPA § 1589(c)(2) — using the worker's immigration "
                    "status as a coercion tool. The DOL OIG 2023 report found that "
                    "'threats related to future visa eligibility were the most "
                    "commonly reported form of coercion in H-2A complaints.'"
                ),
                "sector": "agriculture",
                "corridor": "GT-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Implicit threat to future visa eligibility weaponizes the worker's "
                    "need to return next season to repay the $2,620 debt (now $2,882 "
                    "with one month of 10% interest). The FLC controls both the current "
                    "season's earnings and the 'named request' for next season's H-2A "
                    "petition. CDM found that 78% of H-2A workers reported that fear "
                    "of not being re-hired prevented them from reporting wage "
                    "violations. The AEWR guarantee avoidance pattern ($546.80 "
                    "guaranteed vs. $300-$350 actual piece rate) costs this worker "
                    "~$200/week in unclaimed wages over a 20-week season = $4,000."
                ),
            },
        ],
        "chain_context": (
            "The H-2A program has extensive worker protections on paper — zero "
            "recruitment fees (20 CFR § 655.135(j)), free housing (§ 655.122(d)), "
            "AEWR guarantee (§ 655.122(l)), three-fourths guarantee (§ 655.122(i)). "
            "But the enforcement gap between US-regulated employer obligations and "
            "unregulated Guatemalan reclutadores creates a structural debt burden. "
            "CDM's surveys of 600+ H-2A workers found: 63% paid illegal recruitment "
            "fees, 38% had illegal housing deductions, 52% earned below the AEWR "
            "guarantee without receiving make-up pay, and 78% feared retaliation "
            "for complaints. The DOL WHD conducted 2,400 H-2A investigations in "
            "FY2023 but covers only ~22% of the 11,000+ certified H-2A employers. "
            "Polaris Project identified H-2A as the #1 visa type associated with "
            "labor trafficking hotline calls in 2023."
        ),
        "emergent_risk": (
            "Seasonal debt bondage: illegal recruitment fee ($2,100 via reclutador "
            "in Huehuetenango) + Monterrey consulate routing ($520 inflated travel) "
            "+ illegal housing deduction ($200/month, $800/season) + sub-AEWR piece "
            "rates ($200/week unclaimed guarantee × 20 weeks = $4,000 underpayment) "
            "+ implicit visa-eligibility threat = worker cannot leave, cannot complain, "
            "and needs next season's visa to service 10%-monthly-interest debt."
        ),
        "difficulty": "medium",
        "source_references": [
            "Centro de los Derechos del Migrante (CDM), 'Recruitment Abuses and Fee Charging in H-2 Visa Programs' — 63% paid fees, 78% fear retaliation",
            "Polaris Project, 'Labor Trafficking and the H-2A/H-2B Visa Programs' — #1 visa type in trafficking hotline calls (2023)",
            "US DOL Wage and Hour Division, 'H-2A Enforcement Data FY2023' — 2,400 investigations, 38% housing violations",
            "DOL Office of Inspector General, 'Audit of H-2A Program Employer Compliance' (2023) — consulate routing, visa-threat coercion",
            "20 CFR § 655.122(d) (free housing), § 655.122(l) (AEWR guarantee), § 655.135(j) (zero-fee requirement)",
            "TVPA 2000/2008 § 1589 — forced labor definition including 'abuse of the legal process'",
            "WHD v. Vasquez Citrus & Hauling (2019) — housing charge prohibition precedent",
        ],
        "corridors": ["GT-US", "MX-US", "HN-US"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring"],
            "means": ["deception", "abuse of position of vulnerability", "intimidation"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
]
