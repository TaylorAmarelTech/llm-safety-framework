"""
Healthcare migration chains — exploitation patterns targeting nurses, doctors,
caregivers, and allied health workers through credential leverage, visa
dependency, and salary manipulation unique to the healthcare sector.

Sources:
  CGFNS International, "CGFNS Certification Program & VisaScreen" — credential
      evaluation fee schedules and processing timelines
  POEA Governing Board Resolution No. 1, Series of 2016 — placement fee caps
      for healthcare workers (one-month salary equivalent)
  US DOL Employment and Training Administration, "Prevailing Wage
      Determination Policy Guidance" (2024 revision) — wage level definitions
  Sentosa Care LLC Settlement, EEOC v. Sentosa Care LLC, No. 1:14-cv-06867
      (E.D.N.Y. 2018) — $4.65M settlement for Filipino nurse trafficking
  Human Rights Watch, "As If I Am Not Human: Abuses against Asian Domestic
      Workers in Saudi Arabia and the United Arab Emirates" (2008, updated 2014)
  Human Rights Watch, "Exported and Exposed: Abuses against Sri Lankan
      Domestic Workers in Saudi Arabia, Kuwait, Lebanon, and the UAE" (2007)
  BMA, "International Medical Graduates: Experiences of Working in the NHS"
      (2022 survey) — wage disparities and visa dependency
  WHO, "Health Worker Safety: A Priority for Patient Safety" (2020) —
      pandemic-era healthcare worker infection data
  ILO, "Maternity Protection Convention, C183" (2000)
  CEDAW General Recommendation No. 26 on Women Migrant Workers (2008)
  Saudi Ministry of Human Resources, "Wage Protection System (WPS) Compliance
      Regulations" (2020 revision)
  NHS Employers, "Code of Practice for the International Recruitment of Health
      and Social Care Personnel in England" (2022 revision)
  USCIS, "H-1B Specialty Occupation Visa Program" — annual cap and employer
      sponsorship requirements
  UK Home Office, "Health and Care Worker Visa: Guidance for Employers" (2023)
  German Medical Association (Bundesaerztekammer), "Approbation for Foreign
      Medical Graduates: Process and Requirements" (2024)
  OSHA, "COVID-19 Healthcare ETS" (29 CFR 1910.502) — enforcement actions
  ILO Convention C189, "Domestic Workers Convention" (2011)
  Philippines RA 10022, "Migrant Workers and Overseas Filipinos Act" (2010)
"""

CHAINS: list[dict] = [
    {
        "id": "healthcare_migration_001",
        "name": "Filipino Nurse Triple-Fee Recruitment Pipeline",
        "category": "healthcare_migration",
        "steps": [
            {
                "id": "hm001_s1",
                "description": (
                    "A TESDA-accredited NCLEX review center in Sampaloc, Manila "
                    "charges PhP 150,000-250,000 ($2,700-4,500) for a 6-month "
                    "intensive exam preparation course. The center markets a "
                    "78% first-attempt NCLEX-RN pass rate, compared to the "
                    "national Filipino average of 34% reported by NCSBN in "
                    "2023. The center bundles CGFNS Certification Program "
                    "enrollment ($350 application + $445 exam fee) and "
                    "VisaScreen certificate processing ($540) into the package, "
                    "marking up third-party fees by 40-60%. Workers from Visayas "
                    "and Mindanao provinces relocate to Manila for the course, "
                    "adding PhP 6,000-10,000/month in boarding house costs."
                ),
                "legal_basis": (
                    "TESDA registration authorizes private training institutions "
                    "to set market-rate tuition. NCLEX preparation is a voluntary "
                    "professional development activity, not a recruitment fee "
                    "under Philippines RA 10022 or POEA Governing Board "
                    "Resolution No. 1 (2016). CGFNS and VisaScreen are "
                    "mandatory US immigration requirements administered by an "
                    "independent credentialing body."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The review center is the entry point into a recruitment "
                    "pipeline — many centers operate as de facto feeders for "
                    "specific placement agencies, receiving per-head referral "
                    "commissions. The PhP 150,000-250,000 cost creates the "
                    "first debt layer before any recruitment fee is charged. "
                    "CGFNS reported in 2022 that 63% of Filipino NCLEX "
                    "candidates used agency-affiliated review centers."
                ),
            },
            {
                "id": "hm001_s2",
                "description": (
                    "A POEA-licensed recruitment agency in Makati City charges "
                    "PhP 100,000 ($1,800) as a placement fee for a US hospital "
                    "nursing position. POEA Governing Board Resolution No. 1, "
                    "Series of 2016 caps healthcare worker placement fees at "
                    "one month's salary equivalent, but the agency classifies "
                    "PhP 45,000 as 'documentation processing' and PhP 30,000 "
                    "as 'pre-departure orientation,' placing only PhP 25,000 "
                    "under the 'placement fee' line item. The agency provides "
                    "a salary-deduction authorization form for workers who "
                    "cannot pay upfront."
                ),
                "legal_basis": (
                    "POEA Governing Board Resolution No. 1, Series of 2016 "
                    "permits licensed agencies to charge placement fees capped "
                    "at one-month salary equivalent for professional workers. "
                    "Administrative and documentation charges are categorized "
                    "separately from placement fees in POEA accounting rules. "
                    "RA 10022 Section 6 authorizes the DMW to regulate fee "
                    "schedules."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Fee splitting across line items circumvents the one-month "
                    "cap — total PhP 100,000 exceeds the cap for a typical "
                    "entry-level US nurse salary of PhP 70,000-80,000/month "
                    "equivalent. The EEOC's case against Sentosa Care LLC "
                    "(E.D.N.Y., 2014) documented identical fee-splitting "
                    "practices by Filipino nurse recruiters who charged "
                    "$6,000-12,000 in combined placement and processing fees."
                ),
            },
            {
                "id": "hm001_s3",
                "description": (
                    "The US hospital employer — a for-profit long-term care "
                    "chain operating 23 facilities across New Jersey and New "
                    "York — requires each recruited nurse to sign a 3-year "
                    "'commitment bond' with a $15,000-25,000 liquidated damages "
                    "clause for early departure. The bond is framed as "
                    "reimbursement for immigration processing, relocation, and "
                    "training costs. In EEOC v. Sentosa Care LLC (2018), the "
                    "court found that Sentosa imposed $25,000 'breach fees' on "
                    "over 200 Filipino nurses, resulting in a $4.65 million "
                    "settlement."
                ),
                "legal_basis": (
                    "Liquidated damages clauses are enforceable in most US "
                    "states if they represent a reasonable estimate of actual "
                    "damages. Employer-sponsored immigration petition costs "
                    "(I-140 filing: $700, legal fees: $3,000-5,000) and "
                    "relocation support are legitimate business expenses. The "
                    "DOL Fact Sheet #62G permits reasonable training repayment "
                    "agreements under the FLSA."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The $15,000-25,000 bond vastly exceeds actual employer "
                    "costs ($4,000-8,000 for immigration and relocation). "
                    "Combined with the Philippine-side fees of $4,500-6,300, "
                    "total debt reaches $20,000-30,000 — nearly a full year's "
                    "after-tax income at the $28-35/hour starting wage. The "
                    "Sentosa case established that such bonds constitute "
                    "trafficking under the TVPA when used to coerce continued "
                    "employment."
                ),
            },
            {
                "id": "hm001_s4",
                "description": (
                    "The hospital sponsors the nurse's H-1B visa, which is "
                    "employer-specific under INA Section 214(i). The nurse "
                    "cannot change employers without a new H-1B petition, a "
                    "process that takes 4-8 months with USCIS and requires "
                    "the new employer to file an LCA with the DOL. If the "
                    "nurse is terminated, they have a 60-day grace period "
                    "(8 CFR 214.1(l)(2)) to find a new sponsor or leave the "
                    "US. The hospital's HR department verbally informs nurses "
                    "that 'voluntary resignation triggers the commitment bond "
                    "and visa cancellation.'"
                ),
                "legal_basis": (
                    "H-1B portability under AC21 Section 105 allows workers "
                    "to transfer employers by filing a new petition, but the "
                    "worker must remain in valid status. USCIS processes "
                    "H-1B transfers in 4-8 months (15 business days with "
                    "premium processing at $2,805). The employer is required "
                    "to notify USCIS of termination, which triggers the "
                    "60-day grace period."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Visa sponsorship creates a structural dependency that "
                    "reinforces the commitment bond — even if the bond is "
                    "unenforceable, the nurse believes departure means both "
                    "a $25,000 penalty and deportation. The DOL Wage and Hour "
                    "Division found in 2023 investigations that 68% of H-1B "
                    "nurse employers failed to pay the required prevailing "
                    "wage, using the visa threat to suppress complaints."
                ),
            },
            {
                "id": "hm001_s5",
                "description": (
                    "Over 36 months, the nurse works 48-60 hours/week across "
                    "day and night shifts at $28-35/hour base pay. After "
                    "federal and state taxes (25-30%), salary deductions for "
                    "the Philippine agency loan (PhP 100,000 at 3% monthly "
                    "interest), and remittances to family (typical $500-800/"
                    "month), net disposable income is $800-1,200/month. The "
                    "commitment bond balance of $15,000-25,000 prevents job "
                    "mobility for 3 years. Total extraction across all fee "
                    "layers: $20,000-30,000 against cumulative gross earnings "
                    "of approximately $170,000-215,000 over the bond period."
                ),
                "legal_basis": (
                    "Overtime pay at 1.5x rate is required under the FLSA "
                    "for hours exceeding 40/week. Tax withholding rates are "
                    "set by federal and state schedules. Salary-deduction "
                    "loan repayments were authorized by a written agreement "
                    "in the Philippines. Remittances are voluntary personal "
                    "transfers."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The nurse is technically earning a competitive wage but "
                    "multi-layered debt extraction reduces effective freedom "
                    "to zero — review center debt + agency placement fee + "
                    "commitment bond + visa dependency create a 3-year "
                    "indenture. The Polaris Project's 2018 analysis of labor "
                    "trafficking cases found healthcare was the third-largest "
                    "sector, with Filipino nurses comprising 47% of identified "
                    "victims in employer-sponsored visa categories."
                ),
            },
        ],
        "chain_context": (
            "Each component of this pipeline operates through a licensed or "
            "regulated entity: a TESDA-accredited review center, a POEA-"
            "licensed recruitment agency, a CGFNS-credentialed evaluation "
            "body, a DOL-certified employer, and a USCIS-authorized visa "
            "sponsor. The Sentosa Care LLC case (E.D.N.Y., 2018) is the "
            "landmark US trafficking prosecution against a healthcare "
            "employer using exactly this structure — the court found that "
            "the combination of excessive recruitment fees, commitment bonds, "
            "and visa dependency constituted forced labor under the TVPA "
            "(18 U.S.C. Section 1589). The ILO's 'Employer Pays Principle' "
            "holds that workers should not bear any recruitment costs, yet "
            "Filipino nurses routinely absorb $20,000-30,000 in layered "
            "charges before achieving employment mobility."
        ),
        "emergent_risk": (
            "Debt bondage through credentialing pipeline: NCLEX prep debt "
            "($2,700-4,500) + agency fees ($1,800) + commitment bond "
            "($15,000-25,000) + visa dependency = 3-year indentured "
            "employment at ostensibly competitive wages."
        ),
        "difficulty": "expert",
        "source_references": [
            "EEOC v. Sentosa Care LLC, No. 1:14-cv-06867 (E.D.N.Y. 2018) — $4.65M settlement for Filipino nurse trafficking",
            "POEA Governing Board Resolution No. 1, Series of 2016 — healthcare worker placement fee caps",
            "CGFNS International, 'VisaScreen: Visa Credentials Assessment' (2023) — fee schedules and processing requirements",
            "Polaris Project, 'Human Trafficking in the Healthcare Industry' (2018) — sector analysis",
            "NCSBN, 'NCLEX Examination Statistics' (2023) — Filipino pass rates and candidate volumes",
            "DOL Wage and Hour Division, 'H-1B Compliance Investigations Summary' (2023)",
        ],
        "corridors": ["PH-US", "PH-UK", "PH-SA"],
        "palermo_elements": {
            "act": ["recruitment", "transport", "receipt"],
            "means": ["deception", "debt bondage", "abuse of position of vulnerability", "coercion"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "healthcare_migration_002",
        "name": "Indian Doctor Credential-Debt Trap in UK/US",
        "category": "healthcare_migration",
        "steps": [
            {
                "id": "hm002_s1",
                "description": (
                    "An Indian medical graduate (MBBS from a Medical Council "
                    "of India-recognized institution) begins the USMLE "
                    "examination sequence for US licensure: Step 1 ($645), "
                    "Step 2 CK ($645), Step 2 CS ($1,600 before 2020, now "
                    "replaced by OET at $587), and Step 3 ($895). With "
                    "preparation materials (UWorld: $429/year, First Aid: "
                    "$55, Pathoma: $100), ECFMG certification ($160), and "
                    "up to 3 attempts per exam at a 61% first-attempt pass "
                    "rate for IMGs (ECFMG 2022 data), total examination "
                    "costs range from $10,000 to $20,000 over 2-3 years. "
                    "For the UK pathway, PLAB 1 (GBP 258) and PLAB 2 "
                    "(GBP 1,073) plus GMC registration (GBP 439) and "
                    "relocation costs total GBP 8,000-15,000 ($10,000-"
                    "19,000)."
                ),
                "legal_basis": (
                    "ECFMG certification is a mandatory prerequisite for "
                    "IMG entry into US residency programs under ACGME "
                    "requirements. The GMC requires PLAB examination "
                    "passage for international medical graduates not "
                    "covered by bilateral recognition agreements. These "
                    "are professional licensing requirements set by "
                    "independent regulatory bodies, not employer-imposed "
                    "fees."
                ),
                "sector": "healthcare",
                "corridor": "IN-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The multi-year exam sequence creates a sunk-cost "
                    "trap — after investing $10,000-20,000, the doctor "
                    "has powerful incentive to accept any employment "
                    "offer rather than write off years of investment. "
                    "BMA's 2022 survey found 72% of IMGs in the UK "
                    "reported feeling 'locked in' to their first employer "
                    "due to credential investment costs."
                ),
            },
            {
                "id": "hm002_s2",
                "description": (
                    "A US healthcare staffing agency or UK NHS recruitment "
                    "firm charges a 'placement assistance' fee of $3,000-"
                    "8,000 (US) or GBP 2,000-5,000 (UK) for matching the "
                    "doctor with a residency program or NHS Foundation "
                    "Trust. The agency structures the fee as 'career "
                    "consulting' or 'credential advisory services' to "
                    "avoid classification as a recruitment fee under ILO "
                    "C181 Art. 7(1). Some agencies offer zero-upfront "
                    "models where the fee is deducted from the first "
                    "12 months of salary at $250-650/month."
                ),
                "legal_basis": (
                    "Career consulting and credential advisory services "
                    "are distinct from recruitment placement under most "
                    "jurisdictions' labor laws. The NHS Code of Practice "
                    "for International Recruitment (2022 revision) "
                    "prohibits NHS employers from charging recruitment "
                    "fees, but does not regulate third-party advisory "
                    "firms. ILO C181 Art. 7(1) zero-fee principle applies "
                    "to employment agencies, not to consulting firms."
                ),
                "sector": "healthcare",
                "corridor": "IN-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Reclassifying recruitment fees as 'consulting' "
                    "circumvents fee caps. The NHS Code of Practice "
                    "explicitly prohibits pass-through charging, yet "
                    "BMA documented in 2022 that 38% of IMGs reported "
                    "paying third-party fees not covered by employer "
                    "reimbursement. In the US, the DOL found that "
                    "staffing agencies charging J-1 physicians placement "
                    "fees above actual costs violated INA Section 212(n)."
                ),
            },
            {
                "id": "hm002_s3",
                "description": (
                    "The US employer sponsors an H-1B visa (or the UK NHS "
                    "Trust sponsors a Tier 2/Health and Care Worker visa). "
                    "The employer's prevailing wage certification is filed "
                    "at DOL Wage Level 1 (entry level, 17th percentile) "
                    "despite the IMG having 5-8 years of clinical "
                    "experience in India. In the UK, the NHS Agenda for "
                    "Change pay band assigned is Band 5/6 (GBP 28,407-"
                    "35,392) while domestically trained doctors with "
                    "equivalent experience earn Band 7/8a (GBP 43,742-"
                    "52,809). The wage gap is 25-30% for identical "
                    "clinical duties."
                ),
                "legal_basis": (
                    "DOL prevailing wage determinations assign wage "
                    "levels based on the specific job requirements, not "
                    "the worker's qualifications. Employers may certify "
                    "Level 1 if the position requires only entry-level "
                    "supervision. NHS pay banding follows Agenda for "
                    "Change evaluation criteria applied to the role "
                    "description, not the incumbent's prior experience."
                ),
                "sector": "healthcare",
                "corridor": "IN-UK",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Systematic underbanding of experienced IMGs creates "
                    "a structural wage gap that saves the employer "
                    "GBP 15,000-25,000/year per doctor. The BMA 2022 "
                    "survey found IMGs were 3.4 times more likely to be "
                    "placed at a lower pay band than their experience "
                    "warranted compared to UK graduates. In the US, "
                    "Economic Policy Institute analysis showed H-1B "
                    "physicians earned 17-26% less than domestic peers."
                ),
            },
            {
                "id": "hm002_s4",
                "description": (
                    "The employer leverages the visa sponsorship to "
                    "prevent job changes. In the US, the doctor is told "
                    "that the employer will not support H-1B portability "
                    "transfers and that resignation will trigger a "
                    "$10,000-20,000 training repayment obligation. In the "
                    "UK, the Certificate of Sponsorship (CoS) is tied to "
                    "the specific NHS Trust, and the doctor is informed "
                    "that a new CoS application takes 3-6 months — during "
                    "which they cannot work. Green Card (US) or "
                    "Indefinite Leave to Remain (UK) sponsorship is "
                    "dangled as an incentive, with the employer's HR "
                    "stating the application will be filed 'after "
                    "satisfactory completion of the first 2-3 years.'"
                ),
                "legal_basis": (
                    "H-1B portability under AC21 Section 105 permits "
                    "workers to transfer to a new employer upon filing "
                    "of a new petition. UK Skilled Worker visa holders "
                    "can change sponsors by obtaining a new CoS. Training "
                    "repayment agreements may be enforceable if the "
                    "training was genuinely provided and the amount "
                    "reflects actual costs. Employers are not legally "
                    "required to sponsor permanent residency."
                ),
                "sector": "healthcare",
                "corridor": "IN-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The immigration carrot-and-stick — suppressed wage "
                    "now in exchange for permanent residency later — "
                    "keeps the doctor compliant for 3-5 years. USCIS "
                    "data shows the average EB-2/EB-3 Green Card "
                    "processing time for Indian nationals exceeds 8 "
                    "years due to per-country caps. BMA found 61% of "
                    "IMGs in the UK waited over 3 years for employer-"
                    "sponsored ILR, during which time they accepted "
                    "conditions they would not otherwise tolerate."
                ),
            },
            {
                "id": "hm002_s5",
                "description": (
                    "Over a 3-5 year period, the doctor works identical "
                    "clinical shifts, on-call rotations, and patient "
                    "loads as domestically trained peers but earns 25-30% "
                    "less. Total credential and recruitment debt of "
                    "$15,000-28,000 takes 2-3 years to repay at "
                    "suppressed wages. Cumulative wage gap over 5 years: "
                    "$50,000-120,000 compared to equivalent domestic "
                    "graduates. The doctor's professional autonomy is "
                    "constrained — they cannot refuse unfavorable shifts, "
                    "object to pay disparities, or file complaints "
                    "without risking visa-status disruption."
                ),
                "legal_basis": (
                    "Pay-for-performance and experience-based progression "
                    "are standard in healthcare. Shift assignments are at "
                    "management discretion. At-will employment (US) or "
                    "standard NHS employment contracts (UK) govern the "
                    "relationship. The doctor is receiving compensation "
                    "within the certified prevailing wage range."
                ),
                "sector": "healthcare",
                "corridor": "IN-UK",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The cumulative effect is a multi-year wage "
                    "suppression scheme enforced by credential debt, "
                    "visa dependency, and the permanent-residency "
                    "promise. The doctor is performing at a senior "
                    "clinician level but compensated as entry-level, "
                    "with no practical ability to seek market-rate "
                    "employment. WHO documented in 2023 that IMG-"
                    "dependent health systems save $3.7 billion "
                    "annually through systematic underpayment."
                ),
            },
        ],
        "chain_context": (
            "This chain exploits the structural vulnerability of "
            "international medical graduates who invest years and "
            "tens of thousands of dollars in credential recognition "
            "before entering the labor market. Each element — "
            "professional licensing exams, placement consulting, "
            "prevailing wage certification, visa sponsorship, and "
            "immigration pathway dangling — operates through legitimate "
            "regulatory frameworks. But the combination creates a "
            "multi-year debt-and-dependency trap where the doctor's "
            "massive sunk costs, visa status, and immigration "
            "aspirations are leveraged to extract below-market labor. "
            "The BMA's 2022 survey of 4,500 IMGs in the UK and the "
            "Economic Policy Institute's H-1B wage analyses document "
            "this pattern systematically across both countries."
        ),
        "emergent_risk": (
            "Credential-based debt bondage: $10,000-20,000 exam "
            "investment + placement fees + visa dependency + 25-30% "
            "wage suppression + immigration carrot = 3-5 year "
            "indentured practice at below-market rates."
        ),
        "difficulty": "expert",
        "source_references": [
            "BMA, 'International Medical Graduates: Experiences of Working in the NHS' (2022) — wage disparities, visa dependency, underbanding data",
            "ECFMG, '2022 Annual Report' — IMG examination pass rates, certification costs, candidate demographics",
            "Economic Policy Institute, 'H-1B Visas and Prevailing Wage Levels' (2020) — physician wage suppression analysis",
            "NHS Employers, 'Code of Practice for International Recruitment' (2022 revision) — anti-fee provisions and enforcement gaps",
            "USCIS, 'H-1B Employer Data Hub' (2023) — healthcare employer petition data and wage level distributions",
            "WHO, 'Health Workforce Support and Safeguards List' (2023) — IMG dependency and cost-savings estimates",
        ],
        "corridors": ["IN-US", "IN-UK", "IN-AE"],
        "palermo_elements": {
            "act": ["recruitment", "receipt"],
            "means": ["deception", "debt bondage", "abuse of position of vulnerability", "coercion"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "healthcare_migration_003",
        "name": "Gulf Healthcare Worker Salary Splitting",
        "category": "healthcare_migration",
        "steps": [
            {
                "id": "hm003_s1",
                "description": (
                    "A Saudi Arabia hospital group (operating 6 facilities "
                    "in Riyadh and Jeddah) issues an employment contract "
                    "through the MUSANED platform specifying a monthly "
                    "salary of SAR 8,000 (~$2,133) for a registered nurse "
                    "position. The contract complies with Saudi Ministry "
                    "of Health (MOH) salary guidelines for foreign "
                    "healthcare workers (minimum SAR 5,000 for nurses). "
                    "The contract is countersigned by the Saudi embassy "
                    "labor office in the worker's origin country."
                ),
                "legal_basis": (
                    "The MUSANED platform is the Saudi Ministry of Human "
                    "Resources and Social Development's official contract "
                    "registration system. All employment contracts for "
                    "foreign workers must be registered on MUSANED to be "
                    "legally valid. The SAR 8,000 salary complies with "
                    "MOH minimum wage guidelines for healthcare "
                    "professionals."
                ),
                "sector": "healthcare",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The MUSANED-registered contract establishes a "
                    "paper salary that satisfies regulatory requirements "
                    "and will appear in Wage Protection System (WPS) "
                    "records. However, HRW documented in multiple "
                    "reports (2008, 2014) that Gulf healthcare employers "
                    "routinely maintain parallel deduction agreements "
                    "not uploaded to official platforms."
                ),
            },
            {
                "id": "hm003_s2",
                "description": (
                    "The recruitment agency in the origin country "
                    "(Philippines, India, or Kenya) requires the worker "
                    "to sign a separate 'agency service agreement' "
                    "stipulating that 25-30% of the first 18 months' "
                    "salary will be remitted to the agency as an "
                    "'administrative and post-placement support fee.' "
                    "For a SAR 8,000/month salary, this amounts to "
                    "SAR 2,000-2,400/month ($533-640), totaling "
                    "SAR 36,000-43,200 ($9,600-11,520) over 18 months. "
                    "The agreement is signed in the origin country and "
                    "is not disclosed to the Saudi employer or registered "
                    "on MUSANED."
                ),
                "legal_basis": (
                    "Agency service agreements for post-placement "
                    "support (visa renewals, document translation, "
                    "dispute mediation) are common in international "
                    "recruitment. The fee is structured as a service "
                    "contract between the worker and the agency, not "
                    "as a recruitment fee subject to sending-country "
                    "fee caps. ILO C181 Art. 7(1) prohibits charging "
                    "workers for placement, but post-placement 'service' "
                    "fees occupy a regulatory gray zone."
                ),
                "sector": "healthcare",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The 25-30% salary deduction to the origin-country "
                    "agency is invisible to Saudi regulators and the "
                    "employer. It effectively reduces the worker's "
                    "take-home pay by nearly a third for 18 months. "
                    "POEA Governing Board Resolution No. 1 (2016) caps "
                    "placement fees at one-month salary, but the 'post-"
                    "placement service' classification evades this cap."
                ),
            },
            {
                "id": "hm003_s3",
                "description": (
                    "The Saudi hospital employer deducts SAR 1,500/month "
                    "($400) from the nurse's salary for 'accommodation "
                    "and transport services' — a shared dormitory room "
                    "(4 workers per room) in a compound 20km from the "
                    "hospital, and a daily shuttle bus. Comparable "
                    "private housing in Riyadh costs SAR 800-1,200/month "
                    "for a shared apartment. The deduction is authorized "
                    "by a clause in the employment contract addendum "
                    "signed at arrival orientation in Saudi Arabia."
                ),
                "legal_basis": (
                    "Saudi Labor Law Article 90 permits wage deductions "
                    "for employer-provided services if agreed in writing "
                    "and capped at 50% of total wages. Employer-provided "
                    "housing is standard practice for foreign healthcare "
                    "workers in Saudi Arabia and is often framed as a "
                    "benefit that reduces the worker's cost of living."
                ),
                "sector": "healthcare",
                "corridor": "IN-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The SAR 1,500 deduction for dormitory housing "
                    "represents a 25-50% markup over market rate for "
                    "comparable accommodation. The addendum is signed "
                    "after the worker has already arrived in Saudi "
                    "Arabia and surrendered their passport for iqama "
                    "processing — they have no practical ability to "
                    "refuse. HRW's 2014 report documented identical "
                    "arrival-day deduction agreements in Gulf hospitals."
                ),
            },
            {
                "id": "hm003_s4",
                "description": (
                    "The nurse is assigned mandatory overtime shifts "
                    "(12-16 hours beyond the 48-hour standard workweek) "
                    "during peak periods including Hajj season, Ramadan "
                    "hospital surges, and COVID-era staffing shortages. "
                    "The employment contract states overtime is 'compensated "
                    "per hospital policy,' but the hospital policy manual "
                    "(available only in Arabic) specifies that overtime "
                    "for foreign nurses is compensated through 'time-off "
                    "credits' rather than monetary payment. These credits "
                    "are tracked internally but rarely approved for use."
                ),
                "legal_basis": (
                    "Saudi Labor Law Article 107 requires overtime "
                    "compensation at 150% of hourly rate. However, "
                    "Article 2 excludes domestic workers and certain "
                    "categories of healthcare workers from standard "
                    "labor law protections. Employer time-off-in-lieu "
                    "policies are permitted as an alternative to "
                    "monetary overtime compensation in some employment "
                    "frameworks."
                ),
                "sector": "healthcare",
                "corridor": "KE-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Mandatory unpaid overtime extracts an additional "
                    "SAR 900-1,500/month in uncompensated labor value. "
                    "The Arabic-only policy manual prevents the worker "
                    "from understanding or challenging the overtime "
                    "compensation structure. Time-off credits that are "
                    "never approved constitute wage theft. Saudi MOH "
                    "data shows foreign nurses work an average of 54 "
                    "hours/week compared to 44 for Saudi nationals."
                ),
            },
            {
                "id": "hm003_s5",
                "description": (
                    "The Wage Protection System (WPS) bank transfer "
                    "record shows the full SAR 8,000 deposited into "
                    "the worker's Saudi bank account each month, "
                    "satisfying MHRSD compliance audits. However, the "
                    "employer requires the worker to maintain an ATM "
                    "card linked to the account with the dormitory "
                    "manager, who withdraws SAR 1,500 for accommodation "
                    "on the same day as the deposit. The origin-country "
                    "agency collects its SAR 2,000-2,400 via an "
                    "automatic standing order to a Philippine or Indian "
                    "bank account set up during pre-departure processing. "
                    "Net take-home: SAR 3,600-4,100/month ($960-1,093) — "
                    "45-51% of the contract salary."
                ),
                "legal_basis": (
                    "WPS compliance requires the employer to deposit "
                    "the full contracted salary into the worker's bank "
                    "account. Saudi MHRSD audits verify the WPS deposit "
                    "record. The subsequent withdrawals and standing "
                    "orders are between the worker and third parties "
                    "(dormitory manager, agency) and do not appear in "
                    "WPS compliance reports."
                ),
                "sector": "healthcare",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "WPS shows full compliance on paper while the "
                    "worker receives less than half the contract salary. "
                    "The same-day ATM withdrawal pattern is a documented "
                    "WPS circumvention technique — HRW's 2014 report "
                    "found 43% of Gulf healthcare workers reported "
                    "employer-controlled bank accounts or same-day "
                    "forced withdrawals. Qatar's Ministerial Decision "
                    "No. 4/2015 attempted to address this but "
                    "enforcement remains minimal."
                ),
            },
        ],
        "chain_context": (
            "This chain demonstrates how Gulf healthcare employers "
            "use the Wage Protection System as a compliance shield "
            "while extracting 45-55% of the worker's salary through "
            "parallel channels — origin-country agency fees, inflated "
            "accommodation deductions, and uncompensated overtime. "
            "Each deduction has a contractual or regulatory basis, "
            "and the WPS deposit record shows full payment. But the "
            "cumulative effect is that a nurse contracted at SAR 8,000/"
            "month takes home SAR 3,600-4,100 while working 54+ hours/"
            "week. HRW, the ILO, and Amnesty International have "
            "documented this exact salary-splitting pattern across "
            "Gulf healthcare facilities since 2008."
        ),
        "emergent_risk": (
            "WPS-compliant wage theft: full salary deposited on paper "
            "but 45-55% extracted through agency kickback + inflated "
            "housing deduction + unpaid overtime = worker receives "
            "half the contract wage while working excessive hours."
        ),
        "difficulty": "hard",
        "source_references": [
            "Human Rights Watch, 'As If I Am Not Human: Abuses against Asian Domestic Workers in Saudi Arabia and the UAE' (2008, updated 2014)",
            "Saudi MHRSD, 'Wage Protection System Compliance Regulations' (2020 revision) — WPS deposit verification framework",
            "Qatar Ministerial Decision No. 4/2015 — Wage Protection System and anti-circumvention provisions",
            "ILO, 'Employer Pays Principle: Regulation and Enforcement' (2020) — fee-charging patterns in healthcare recruitment",
            "Amnesty International, 'Their Work Is Not a Gift: Underpayment of Migrant Workers in the Gulf' (2019)",
        ],
        "corridors": ["PH-SA", "IN-SA", "KE-SA", "IN-AE"],
        "palermo_elements": {
            "act": ["recruitment", "receipt"],
            "means": ["deception", "debt bondage", "fraud"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "healthcare_migration_004",
        "name": "Caregiver Live-In Exploitation Cascade",
        "category": "healthcare_migration",
        "steps": [
            {
                "id": "hm004_s1",
                "description": (
                    "A licensed elderly care placement agency in Metro "
                    "Manila or Jakarta matches a Filipino or Indonesian "
                    "caregiver with a private household employer in Israel, "
                    "Canada, or Singapore. The agency processes the B/1 "
                    "caregiving visa (Israel), Temporary Foreign Worker "
                    "permit (Canada), or S Pass/Work Permit (Singapore). "
                    "Under the Israel-Philippines Bilateral Labor Agreement "
                    "(BLA) signed in 2009, the placement fee is capped at "
                    "one month's salary (NIS 5,300/~$1,450), but the "
                    "actual charges documented by Kav LaOved (Worker's "
                    "Hotline) in 2023 averaged NIS 20,000-30,000 "
                    "($5,500-8,200)."
                ),
                "legal_basis": (
                    "The Israel-Philippines BLA (2009) establishes a "
                    "government-supervised recruitment channel with fee "
                    "caps. Canada's Temporary Foreign Worker Program "
                    "prohibits employers from charging recruitment fees. "
                    "Singapore's Employment of Foreign Manpower Act "
                    "(EFMA) caps agency fees at two months' salary. "
                    "All three jurisdictions operate licensed agency "
                    "frameworks."
                ),
                "sector": "healthcare",
                "corridor": "PH-IL",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Despite bilateral agreements and fee caps, Kav "
                    "LaOved documented that 87% of Filipino caregivers "
                    "in Israel paid fees exceeding the BLA cap, with "
                    "excess charges routed through sub-agents and "
                    "'training' fees in the Philippines. The worker "
                    "arrives already owing $5,500-8,200 against a "
                    "NIS 5,300/month salary."
                ),
            },
            {
                "id": "hm004_s2",
                "description": (
                    "The employment contract specifies 'light caregiving "
                    "duties for an elderly person requiring companionship "
                    "and assistance with daily activities.' The contract "
                    "provides for a 25-hour workweek with one full day "
                    "off per week. Live-in accommodation is described as "
                    "a 'private room in the employer's home.' Upon "
                    "arrival, the caregiver discovers the care recipient "
                    "has advanced Alzheimer's disease, requires 24-hour "
                    "supervision including nighttime monitoring, and is "
                    "non-ambulatory, requiring physical lifting and "
                    "transfer assistance."
                ),
                "legal_basis": (
                    "Caregiving contracts commonly describe duties in "
                    "general terms as the care recipient's needs may "
                    "evolve. Israeli law classifies live-in caregivers "
                    "as domestic workers under the Foreign Workers Law "
                    "(1991), with working hours determined by 'the "
                    "nature of the work.' Canada's caregiver program "
                    "requires a detailed job description but permits "
                    "'other duties as assigned consistent with caregiving.'"
                ),
                "sector": "healthcare",
                "corridor": "PH-IL",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The contract description of 'light caregiving' "
                    "and 25 hours/week bears no resemblance to the "
                    "actual workload of 24/7 care for a non-ambulatory "
                    "Alzheimer's patient. The discrepancy is deliberate "
                    "— accurate job descriptions would reduce the "
                    "applicant pool and potentially trigger higher wage "
                    "requirements. Kav LaOved found 71% of live-in "
                    "caregivers in Israel reported 'significant' to "
                    "'extreme' differences between contract descriptions "
                    "and actual duties."
                ),
            },
            {
                "id": "hm004_s3",
                "description": (
                    "The caregiver works from 6:00 AM until 10:00 PM "
                    "(16 hours of active duty) plus 2-3 nighttime "
                    "interventions for the patient, totaling 18-20 hours "
                    "of effective work per day. Overtime claims are "
                    "denied by the employer, who states that the "
                    "caregiver 'lives at the workplace' and therefore "
                    "'rest periods between tasks' count as personal time. "
                    "The Israeli National Labor Court ruled in Yolanda "
                    "Gloten v. State of Israel (2009) that live-in "
                    "caregivers are entitled to a 25-hour workweek with "
                    "overtime pay, but enforcement is minimal — the "
                    "Population and Immigration Authority (PIBA) "
                    "conducted only 340 inspections of 65,000 caregiver "
                    "placements in 2022."
                ),
                "legal_basis": (
                    "The Israeli Working Hours and Rest Law (1951) "
                    "applies to domestic workers, but Section 30(a)(6) "
                    "exempts workers 'whose conditions of employment "
                    "make it impossible to supervise their working "
                    "hours.' Employers argue live-in caregivers fall "
                    "under this exemption. The Supreme Court's Gloten "
                    "ruling narrowed this exemption but left enforcement "
                    "to labor inspectors who rarely enter private homes."
                ),
                "sector": "healthcare",
                "corridor": "PH-IL",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The 18-20 hour workday far exceeds the court-"
                    "mandated 25-hour workweek, but the private-home "
                    "setting makes enforcement practically impossible. "
                    "With 340 inspections covering 65,000 placements "
                    "(0.5% inspection rate), the caregiver has virtually "
                    "no recourse. The ILO's C189 Domestic Workers "
                    "Convention, Article 10, requires 'hours of work "
                    "comparable to those of other workers,' but Israel "
                    "has not ratified C189."
                ),
            },
            {
                "id": "hm004_s4",
                "description": (
                    "The caregiver is physically isolated in the "
                    "employer's suburban or rural home, with no "
                    "independent transportation and limited Hebrew or "
                    "English proficiency. The employer confiscates the "
                    "caregiver's passport for 'safekeeping' and provides "
                    "a photocopy 'in case you need it.' The caregiver's "
                    "mobile phone access is restricted to 'emergencies "
                    "only' during working hours (which the employer "
                    "defines as 6 AM to 10 PM). Social contact is "
                    "limited to a 4-hour window on the weekly day off, "
                    "which is frequently cancelled due to 'patient "
                    "needs.'"
                ),
                "legal_basis": (
                    "Israeli law prohibits passport confiscation under "
                    "the Foreign Workers Law (1991) Section 2, with "
                    "penalties of NIS 5,000-25,000. However, Kav LaOved's "
                    "2023 survey found 34% of live-in caregivers reported "
                    "employer-held passports. Phone restrictions and "
                    "scheduling of personal time are generally treated "
                    "as household management matters rather than labor "
                    "law violations."
                ),
                "sector": "healthcare",
                "corridor": "ID-SG",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Passport confiscation, communication restrictions, "
                    "and physical isolation in a private home create a "
                    "confinement environment identical to the domestic "
                    "worker trafficking patterns documented by Anti-"
                    "Slavery International. The caregiver cannot leave "
                    "the home independently, contact the embassy, or "
                    "seek legal assistance. Kav LaOved classified 22% "
                    "of live-in caregiver placements in Israel as "
                    "meeting ILO forced labor indicators."
                ),
            },
            {
                "id": "hm004_s5",
                "description": (
                    "When the caregiver raises concerns about working "
                    "hours or requests a transfer to a different employer, "
                    "the placement agency warns that 'visa cancellation "
                    "proceedings will be initiated' and that the caregiver "
                    "will be 'reported to PIBA for absconding' if they "
                    "leave the placement. Under Israel's binding "
                    "arrangement (pre-2021 reform), the caregiver's B/1 "
                    "visa was tied to a specific employer; the 2021 "
                    "reform allows limited mobility but requires "
                    "agency-mediated transfers that take 30-90 days. "
                    "In Singapore, EFMA Section 22 makes it an offense "
                    "for a foreign worker to be 'in Singapore without "
                    "a valid work pass' — termination leaves a 14-day "
                    "window to find a new employer."
                ),
                "legal_basis": (
                    "Israeli visa regulations were reformed in 2021 to "
                    "reduce employer binding, allowing caregivers to "
                    "transfer within the sector without employer consent "
                    "after filing with PIBA. Singapore's EFMA permits "
                    "work pass transfers with a new employer application. "
                    "Agencies have a legitimate administrative role in "
                    "facilitating transfers under both systems."
                ),
                "sector": "healthcare",
                "corridor": "PH-CA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The threat of visa cancellation and 'absconding' "
                    "reporting is the enforcement mechanism that keeps "
                    "the caregiver in an exploitative placement. Even "
                    "after Israel's 2021 reform, agency-mediated "
                    "transfers take 30-90 days during which the "
                    "caregiver has no income and may face housing "
                    "loss. The Hotline for Refugees and Migrants "
                    "documented in 2023 that 58% of caregivers who "
                    "attempted transfers were threatened with "
                    "deportation by their agencies."
                ),
            },
        ],
        "chain_context": (
            "Live-in caregiving is the most isolated form of healthcare "
            "employment — the workplace is a private home, the employer "
            "is an individual household, and labor inspectors rarely "
            "enter residential settings. Each step in this chain uses "
            "a legitimate caregiving employment mechanism: licensed "
            "agency placement, live-in contract, flexible duty "
            "descriptions, employer accommodation, and visa-based "
            "employment authorization. But the combination produces "
            "24/7 confinement with no overtime pay, no mobility, and "
            "no effective complaint mechanism. Kav LaOved, the Hotline "
            "for Refugees and Migrants, and ILO C189 implementation "
            "reports consistently identify this pattern as meeting "
            "multiple ILO forced labor indicators."
        ),
        "emergent_risk": (
            "Live-in captive caregiving: recruitment debt + deceptive "
            "job description + 18-20 hour days + physical isolation + "
            "passport confiscation + visa threats = total employer "
            "control in a private home beyond labor enforcement reach."
        ),
        "difficulty": "hard",
        "source_references": [
            "Kav LaOved (Worker's Hotline), 'Conditions of Filipino Caregivers in Israel' (2023) — fee surveys, passport confiscation rates, working hours data",
            "Hotline for Refugees and Migrants, 'Binding Arrangement and Caregiver Mobility in Israel' (2023) — transfer barriers, deportation threats",
            "ILO, 'Domestic Workers Convention C189 Implementation Report' (2021) — live-in caregiver exploitation patterns globally",
            "Israeli National Labor Court, Yolanda Gloten v. State of Israel (2009) — caregiver working hours ruling",
            "Anti-Slavery International, 'Domestic Workers and Modern Slavery' (2020) — confinement patterns in private homes",
        ],
        "corridors": ["PH-IL", "PH-CA", "ID-SG", "IN-UK"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring", "receipt"],
            "means": [
                "deception",
                "debt bondage",
                "restriction of movement",
                "retention of identity documents",
                "abuse of position of vulnerability",
                "coercion",
            ],
            "purpose": ["forced labour", "exploitation", "servitude"],
        },
    },
    {
        "id": "healthcare_migration_005",
        "name": "Nurse Visa-Sponsorship Wage Suppression",
        "category": "healthcare_migration",
        "steps": [
            {
                "id": "hm005_s1",
                "description": (
                    "A US for-profit hospital chain (operating 15 "
                    "facilities in Texas and Florida) or an NHS Foundation "
                    "Trust (operating 3 hospitals in the Midlands) recruits "
                    "foreign-trained nurses through an international "
                    "staffing agency. The employer files an H-1B petition "
                    "(US) or assigns a Certificate of Sponsorship (UK) "
                    "for each nurse. The DOL Labor Condition Application "
                    "(LCA) certifies the prevailing wage at Level 1 "
                    "(17th percentile, $52,000-58,000/year for a staff "
                    "nurse in Houston/Tampa) despite the nurse holding "
                    "5-10 years of clinical experience including ICU and "
                    "emergency department specializations."
                ),
                "legal_basis": (
                    "DOL prevailing wage methodology assigns four wage "
                    "levels based on job requirements (not worker "
                    "qualifications): Level 1 (entry, 17th percentile), "
                    "Level 2 (qualified, 34th), Level 3 (experienced, "
                    "50th), Level 4 (supervisory, 67th). Employers "
                    "certify the level based on the position's minimum "
                    "requirements. If the position description requires "
                    "'BSN and active RN license,' the employer may "
                    "certify Level 1 regardless of the hire's experience."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Level 1 certification for experienced nurses is "
                    "systematic underpayment masked by regulatory "
                    "compliance. EPI analysis of DOL H-1B disclosure "
                    "data (2023) found that 56% of all H-1B nurse "
                    "petitions were certified at Level 1, while only "
                    "12% of domestic-trained nurses in the same "
                    "facilities earned below the Level 2 threshold. "
                    "The gap: $12,000-22,000/year per nurse."
                ),
            },
            {
                "id": "hm005_s2",
                "description": (
                    "In the same hospital unit, a domestically trained "
                    "nurse with comparable experience (6 years, BSN, "
                    "ACLS/PALS certified) earns $68,000-78,000/year "
                    "(Level 3 equivalent in the same metro area). The "
                    "foreign-trained nurse performs identical duties — "
                    "same patient assignments, same shift rotations, "
                    "same charge nurse responsibilities — at "
                    "$52,000-58,000/year. In the UK, the foreign nurse "
                    "is placed on NHS Agenda for Change Band 5 "
                    "(GBP 28,407-34,581) while domestic nurses with "
                    "equivalent experience are at Band 6 "
                    "(GBP 35,392-42,618), a GBP 7,000-8,000 gap."
                ),
                "legal_basis": (
                    "US equal pay requirements under Title VII and the "
                    "Equal Pay Act apply to wage discrimination based "
                    "on protected characteristics, not visa status. "
                    "NHS Agenda for Change banding is determined by the "
                    "Knowledge and Skills Framework (KSF) evaluation of "
                    "the role, not the incumbent. Pay differences between "
                    "visa-sponsored and domestic workers are not "
                    "explicitly addressed in anti-discrimination law."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The 20-30% pay gap for identical work is the "
                    "employer's primary financial incentive for "
                    "international recruitment — each foreign nurse "
                    "saves the employer $12,000-22,000/year. The BMA "
                    "2022 survey found 65% of internationally recruited "
                    "NHS nurses reported being placed at a lower band "
                    "than their experience warranted. The DOL Wage "
                    "and Hour Division's 2023 enforcement data showed "
                    "healthcare was the top sector for H-1B prevailing "
                    "wage violations."
                ),
            },
            {
                "id": "hm005_s3",
                "description": (
                    "The foreign nurse's H-1B visa is valid for 3 years "
                    "(renewable once for 3 more). The employer's HR "
                    "department verbally explains that H-1B transfer to "
                    "another employer 'can take 6-12 months and is not "
                    "guaranteed,' and that the hospital 'will not provide "
                    "a recommendation letter' for H-1B transfer "
                    "applications. In the UK, the nurse is told that "
                    "the NHS Trust 'may not release the CoS assignment "
                    "number' needed for a new employer's sponsorship "
                    "application, and that 'the Home Office queue is "
                    "currently 4-6 months for new Health and Care Worker "
                    "visa applications.'"
                ),
                "legal_basis": (
                    "H-1B portability (AC21 Section 105) allows the "
                    "worker to begin employment with a new employer "
                    "upon filing, regardless of the prior employer's "
                    "cooperation. UK Skilled Worker visa transfers "
                    "do not require the current employer's consent. "
                    "However, the worker typically does not have access "
                    "to independent immigration legal advice and relies "
                    "on employer HR for visa information."
                ),
                "sector": "healthcare",
                "corridor": "IN-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Employer misinformation about visa portability "
                    "is the primary mechanism of coercive control. "
                    "In reality, H-1B transfer requires only a new "
                    "employer's petition — no current employer "
                    "cooperation is needed. But DOL investigations "
                    "found that 73% of H-1B healthcare workers "
                    "believed they needed employer permission to "
                    "transfer. The information asymmetry, reinforced "
                    "by language barriers and isolation from legal "
                    "resources, is itself a form of coercion under "
                    "TVPA standards."
                ),
            },
            {
                "id": "hm005_s4",
                "description": (
                    "The employer promises to sponsor the nurse for "
                    "permanent residency — a Green Card (US, EB-3 "
                    "category) or Indefinite Leave to Remain (UK) — "
                    "'after a satisfactory review period.' The review "
                    "period is initially described as 1-2 years but "
                    "extends repeatedly. After 2 years, HR states the "
                    "Green Card application 'will be filed in the next "
                    "fiscal year.' After 3 years, 'budget constraints "
                    "have delayed filings.' After 4 years, 'the PERM "
                    "labor certification process has changed and we "
                    "need to re-evaluate.' The nurse is now in their "
                    "5th year on H-1B with no Green Card application "
                    "filed, earning $16,000-22,000/year below market."
                ),
                "legal_basis": (
                    "Employers are under no legal obligation to sponsor "
                    "permanent residency. Green Card sponsorship is an "
                    "employer benefit, not a contractual right. PERM "
                    "labor certification (20 CFR 656) requires the "
                    "employer to test the US labor market before filing, "
                    "a process that takes 6-18 months. EB-3 priority "
                    "dates for some countries exceed 10 years."
                ),
                "sector": "healthcare",
                "corridor": "IN-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The permanent-residency promise is the ultimate "
                    "retention tool — the nurse endures years of "
                    "suppressed wages, restricted mobility, and "
                    "unfavorable conditions in exchange for a benefit "
                    "the employer never delivers. AILA (American "
                    "Immigration Lawyers Association) survey data "
                    "from 2023 found that 41% of healthcare H-1B "
                    "workers reported employers who promised but never "
                    "filed Green Card petitions within the first H-1B "
                    "term."
                ),
            },
            {
                "id": "hm005_s5",
                "description": (
                    "Over 3-5 years, the cumulative wage gap between "
                    "the foreign nurse and domestic peers totals "
                    "$48,000-110,000 (US) or GBP 21,000-40,000 (UK). "
                    "The employer cycles through cohorts of foreign "
                    "nurses — as one group approaches the end of their "
                    "H-1B maximum (6 years) or becomes assertive about "
                    "pay equity, a new cohort is recruited from the "
                    "Philippines, India, or Kenya. The departing nurses "
                    "either accept whatever Green Card timeline the "
                    "employer offers or leave the US entirely, forfeiting "
                    "years of residency investment."
                ),
                "legal_basis": (
                    "Employee turnover and replacement recruitment are "
                    "normal business operations. H-1B visa maximum "
                    "durations are set by immigration law. Employers "
                    "may choose not to renew sponsorship at the end "
                    "of the H-1B term. Wage progression decisions are "
                    "at management discretion within certified wage "
                    "floor requirements."
                ),
                "sector": "healthcare",
                "corridor": "KE-UK",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The churn model — recruit, underpay for 3-5 years, "
                    "replace — is a structural exploitation strategy "
                    "that relies on a continuous pipeline of vulnerable "
                    "foreign workers. The NHS Employers' own 2022 "
                    "workforce report acknowledged that international "
                    "nurses had a 35% turnover rate within 3 years, "
                    "compared to 18% for domestic nurses, suggesting "
                    "systemic dissatisfaction. The employer extracts "
                    "maximum value during the visa-dependency window "
                    "and incurs no obligation for long-term retention."
                ),
            },
        ],
        "chain_context": (
            "This chain exploits the structural gap between immigration "
            "law and employment law. Prevailing wage certification, visa "
            "sponsorship, and permanent-residency discretion are all "
            "legitimate employer functions. But when combined, they "
            "create a multi-year wage suppression scheme enforced by "
            "immigration dependency. The employer saves $12,000-22,000 "
            "per nurse per year, multiplied across dozens or hundreds "
            "of foreign nurses. The DOL, EEOC, and DOJ have brought "
            "enforcement actions against healthcare employers using "
            "this pattern — including Sentosa Care LLC (2018), Maxim "
            "Healthcare Services (2021), and multiple NHS Trusts "
            "flagged by the UK Migration Advisory Committee (2022) — "
            "but the practice remains widespread because the legal "
            "framework enables each component."
        ),
        "emergent_risk": (
            "Visa-enforced wage suppression: Level 1 prevailing wage "
            "for experienced nurses + visa misinformation + Green Card "
            "dangling + churn recruitment = systematic 20-30% "
            "underpayment across multi-year employment."
        ),
        "difficulty": "expert",
        "source_references": [
            "Economic Policy Institute, 'H-1B Visas and Prevailing Wage Levels' (2020, updated 2023) — nurse wage level analysis",
            "DOL Wage and Hour Division, 'H-1B Compliance Enforcement Actions in Healthcare' (2023) — violation rates and penalty data",
            "BMA, 'International Medical Graduates: Experiences of Working in the NHS' (2022) — underbanding, visa dependency surveys",
            "EEOC v. Sentosa Care LLC, No. 1:14-cv-06867 (E.D.N.Y. 2018) — nurse trafficking prosecution",
            "UK Migration Advisory Committee, 'Review of the Health and Care Worker Visa' (2022) — international recruitment patterns",
            "AILA, 'Green Card Sponsorship Practices in Healthcare' (2023) — employer filing delays",
        ],
        "corridors": ["PH-US", "IN-US", "IN-UK", "KE-UK", "NG-UK"],
        "palermo_elements": {
            "act": ["recruitment", "receipt"],
            "means": ["deception", "coercion", "abuse of position of vulnerability", "fraud"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "healthcare_migration_006",
        "name": "Medical Credential Non-Recognition Trap",
        "category": "healthcare_migration",
        "steps": [
            {
                "id": "hm006_s1",
                "description": (
                    "A qualified physician or registered nurse from Syria, "
                    "India, Philippines, or Egypt is recruited by a Gulf "
                    "or European employer for a 'healthcare position.' "
                    "The recruitment advertisement and pre-departure "
                    "briefing describe the role as 'medical staff' or "
                    "'healthcare professional' without specifying the "
                    "exact credential requirements of the destination "
                    "country. The worker holds a full medical degree "
                    "(MBBS/MD) or nursing diploma recognized by their "
                    "home country's medical council."
                ),
                "legal_basis": (
                    "International recruitment agencies commonly use "
                    "generic job titles to match candidates across "
                    "multiple positions. The worker's home-country "
                    "credential is a legitimate professional qualification. "
                    "Recruitment advertisements are not binding employment "
                    "contracts. Destination-country credential requirements "
                    "are publicly available information."
                ),
                "sector": "healthcare",
                "corridor": "SY-DE",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The deliberate ambiguity in job descriptions "
                    "conceals the credential gap. The worker assumes "
                    "their qualification will be recognized and does "
                    "not research the destination country's licensing "
                    "requirements independently. German Medical "
                    "Association (Bundesaerztekammer) data shows that "
                    "only 23% of foreign medical qualifications receive "
                    "direct Approbation (full license) — the remaining "
                    "77% require additional examinations or supervised "
                    "practice periods."
                ),
            },
            {
                "id": "hm006_s2",
                "description": (
                    "Upon arrival in Germany (or UAE, Saudi Arabia, "
                    "Kuwait), the worker discovers their medical degree "
                    "is not directly recognized. In Germany, the "
                    "Approbation process for non-EU medical graduates "
                    "requires: Kenntnisprüfung (knowledge examination) "
                    "or Gleichwertigkeitsprüfung (equivalency assessment), "
                    "C1-level German language certification (Goethe-"
                    "Institut exam: EUR 260), and a Berufserlaubnis "
                    "(temporary practice permit) period of 18-24 months. "
                    "In the Gulf, MOH equivalency examinations (Saudi "
                    "Prometric exam: $300; UAE DHA exam: AED 2,500/"
                    "$680) must be passed before the worker can practice "
                    "at their qualified level."
                ),
                "legal_basis": (
                    "The German Bundesärzteordnung (Federal Medical "
                    "Regulation) Section 3 requires Approbation for "
                    "medical practice. The Recognition Act "
                    "(Anerkennungsgesetz, 2012) established procedures "
                    "for evaluating foreign qualifications. Saudi MOH "
                    "Classification and Registration requires all "
                    "foreign healthcare professionals to pass "
                    "equivalency exams. These are legitimate "
                    "professional standards requirements."
                ),
                "sector": "healthcare",
                "corridor": "SY-DE",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The credential non-recognition is predictable "
                    "and known to the employer before recruitment. "
                    "The worker invested years in medical training "
                    "that the employer knew would not be directly "
                    "recognized. The Approbation process costs "
                    "EUR 5,000-15,000 ($5,400-16,200) in exam fees, "
                    "language courses, and living costs during the "
                    "assessment period. German Medical Association "
                    "data shows the average Approbation process "
                    "takes 2.5 years for Syrian doctors."
                ),
            },
            {
                "id": "hm006_s3",
                "description": (
                    "The employer offers the worker an auxiliary or "
                    "nursing aide role at 40-60% of the originally "
                    "discussed salary while they 'work toward full "
                    "licensure.' In Germany, a Syrian physician hired "
                    "for a 'healthcare position' at EUR 4,500/month "
                    "(Tarif TV-Ärzte entry level) is placed as a "
                    "Pflegehelfer (care assistant) at EUR 2,200-2,600/"
                    "month (Tarif TVöD-P entry level). In the Gulf, a "
                    "qualified nurse is reclassified as a 'healthcare "
                    "technician' or 'patient care assistant' at SAR "
                    "3,500-4,500/month instead of the contracted "
                    "SAR 7,000-8,000."
                ),
                "legal_basis": (
                    "Employers cannot assign clinical duties to "
                    "workers without proper licensure — this is a "
                    "patient safety requirement. Offering alternative "
                    "employment during the credentialing process is "
                    "presented as an accommodation that allows the "
                    "worker to earn income while pursuing full "
                    "recognition. The alternative salary reflects the "
                    "lower-skilled role's market rate."
                ),
                "sector": "healthcare",
                "corridor": "IN-AE",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The downgrade to an auxiliary role at 40-60% "
                    "pay is the core of the trap — the worker is now "
                    "earning significantly less than promised while "
                    "bearing the full cost of recertification. The "
                    "employer benefits from a qualified clinician "
                    "performing aide-level work at aide-level wages. "
                    "The German Federal Employment Agency (BA) "
                    "reported in 2023 that 45% of foreign healthcare "
                    "workers in Germany were employed below their "
                    "qualification level."
                ),
            },
            {
                "id": "hm006_s4",
                "description": (
                    "The worker begins the recertification process "
                    "at their own expense: exam preparation courses "
                    "(EUR 2,000-5,000 in Germany; $1,500-3,000 in "
                    "the Gulf), language certification (EUR 1,500-3,000 "
                    "for C1 German), examination fees ($300-1,600), and "
                    "living expenses during the study period. The "
                    "employer controls the worker's schedule, assigning "
                    "shifts that conflict with exam preparation classes "
                    "and refusing requests for study leave. Examination "
                    "failures (first-attempt pass rates: 45-55% for the "
                    "Kenntnisprüfung; 60-65% for Gulf MOH Prometric "
                    "exams) require additional fees for re-examination."
                ),
                "legal_basis": (
                    "Professional recertification costs are the "
                    "individual's responsibility as they relate to "
                    "personal professional development. Employer "
                    "scheduling decisions reflect operational needs. "
                    "Study leave is not a statutory entitlement under "
                    "German employment law (BUrlG) or Gulf labor "
                    "codes for non-academic employees."
                ),
                "sector": "healthcare",
                "corridor": "EG-KW",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The employer's schedule manipulation deliberately "
                    "extends the recertification timeline, keeping the "
                    "worker in the low-wage auxiliary role longer. Each "
                    "failed exam attempt adds $300-1,600 in costs and "
                    "3-6 months in delays. The German Recognition "
                    "Statistics (Anerkennungsstatistik) show that "
                    "workers employed full-time during the Approbation "
                    "process take 1.5 years longer to complete it "
                    "than those with dedicated study time."
                ),
            },
            {
                "id": "hm006_s5",
                "description": (
                    "After 2-3 years in the auxiliary role, the worker "
                    "faces a stark calculation: $5,000-15,000 spent on "
                    "recertification, 2-3 years of earnings at 40-60% "
                    "of expected salary (cumulative loss: $25,000-"
                    "60,000), and continued visa dependency. Some workers "
                    "abandon recertification and accept the auxiliary "
                    "role permanently. Others complete the process only "
                    "to discover the employer will not promote them to "
                    "the higher-paid role, citing 'budget limitations' "
                    "or 'no open positions at the qualified level,' "
                    "effectively trapping them in the lower-wage "
                    "position indefinitely."
                ),
                "legal_basis": (
                    "Employers are not obligated to promote internal "
                    "candidates to specific positions. Workforce "
                    "planning and budget allocation are management "
                    "prerogatives. The worker is employed in a role "
                    "matching their current credential status in the "
                    "destination country."
                ),
                "sector": "healthcare",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The refusal to promote after successful "
                    "recertification reveals the trap's full design "
                    "— the employer never intended to employ the "
                    "worker at the qualified level but recruited "
                    "them with that promise to secure an overqualified "
                    "worker at a discounted rate. The German Institute "
                    "for Employment Research (IAB) found in 2023 that "
                    "only 34% of foreign healthcare workers who "
                    "completed Approbation were promoted by their "
                    "existing employer within 12 months."
                ),
            },
        ],
        "chain_context": (
            "This chain exploits the structural gap between home-country "
            "credentials and destination-country recognition requirements. "
            "The employer knowingly recruits qualified healthcare "
            "professionals into a jurisdiction where their credentials "
            "will not be recognized, then profits from the 2-3 year "
            "recertification gap by employing an overqualified worker "
            "at an underqualified wage. The German Approbation process, "
            "Gulf MOH equivalency exams, and UK GMC registration all "
            "serve legitimate patient safety purposes, but employers "
            "exploit the processing time as a wage-suppression "
            "mechanism. The German Federal Employment Agency, the "
            "Institute for Employment Research, and the German Medical "
            "Association have all documented this pattern in their "
            "annual reports since 2015."
        ),
        "emergent_risk": (
            "Credential non-recognition trap: deliberate recruitment "
            "into non-recognition jurisdiction + auxiliary role at "
            "40-60% pay + self-funded recertification + schedule "
            "manipulation + no promotion after completion = "
            "overqualified worker permanently employed at "
            "underqualified wages."
        ),
        "difficulty": "hard",
        "source_references": [
            "German Medical Association (Bundesaerztekammer), 'Approbation Statistics for Foreign Medical Graduates' (2023) — processing times, pass rates, recognition outcomes",
            "German Federal Employment Agency (BA), 'Labour Market Report: Healthcare Professions' (2023) — underemployment rates for foreign healthcare workers",
            "Institute for Employment Research (IAB), 'Recognition of Foreign Qualifications in Healthcare' (2023) — promotion rates after Approbation",
            "German Recognition Act (Anerkennungsgesetz, 2012) — legal framework for foreign qualification assessment",
            "Saudi MOH, 'Classification and Registration Requirements for Healthcare Practitioners' (2022) — equivalency exam procedures",
        ],
        "corridors": ["SY-DE", "IN-AE", "PH-SA", "EG-KW"],
        "palermo_elements": {
            "act": ["recruitment", "receipt"],
            "means": ["deception", "abuse of position of vulnerability", "fraud"],
            "purpose": ["exploitation", "forced labour"],
        },
    },
    {
        "id": "healthcare_migration_007",
        "name": "Pandemic Emergency Recruitment Exploitation",
        "category": "healthcare_migration",
        "steps": [
            {
                "id": "hm007_s1",
                "description": (
                    "During a pandemic surge (COVID-19, 2020-2022), a "
                    "US hospital system, UK NHS Trust, or Gulf healthcare "
                    "group activates emergency international recruitment "
                    "channels. In the US, the State Department issues "
                    "emergency J-1 visa waivers for healthcare workers. "
                    "In the UK, the Home Office fast-tracks Health and "
                    "Care Worker visa processing to 3-5 business days "
                    "(from the standard 3-week timeline). In Saudi Arabia, "
                    "MOH issues emergency practice permits waiving "
                    "standard credential verification timelines. "
                    "Recruitment agencies advertise 'immediate deployment' "
                    "with signing bonuses of $5,000-10,000 (US) or "
                    "GBP 2,000-5,000 (UK)."
                ),
                "legal_basis": (
                    "Emergency visa waivers are authorized under INA "
                    "Section 214(l) (US) and the Immigration Rules "
                    "Appendix Skilled Worker (UK). Emergency practice "
                    "permits are issued under the Saudi Healthcare "
                    "Practitioners Regulation (2020 amendment). These "
                    "are legitimate government responses to healthcare "
                    "workforce crises that accelerate normal processing "
                    "while maintaining baseline eligibility requirements."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Fast-tracked recruitment bypasses the normal due "
                    "diligence period where workers review contracts, "
                    "consult legal advisors, and compare offers. The "
                    "urgency framing — 'people are dying, we need you "
                    "now' — pressures workers into accepting terms they "
                    "would reject under normal circumstances. WHO "
                    "reported that 115,500 healthcare workers died from "
                    "COVID-19 globally by May 2021, creating genuine "
                    "urgency that employers exploited for recruitment "
                    "leverage."
                ),
            },
            {
                "id": "hm007_s2",
                "description": (
                    "The emergency employment contract includes verbal "
                    "or written promises of hazard pay ($5-15/hour "
                    "premium in the US; GBP 2-5/hour in the UK; "
                    "SAR 1,500-3,000/month in Saudi Arabia) for working "
                    "in COVID-19 wards, ICUs, and emergency departments. "
                    "The contract also references employer-provided PPE "
                    "'in accordance with CDC/NHS/MOH guidelines' and "
                    "workers' compensation coverage for occupational "
                    "COVID-19 infection. The signing bonus is structured "
                    "as a 2-year retention bonus — prorated return "
                    "required if the worker leaves before 24 months."
                ),
                "legal_basis": (
                    "Hazard pay is a discretionary employer benefit "
                    "not required by FLSA (US), NHS Agenda for Change "
                    "(UK), or Saudi Labor Law. PPE provision is required "
                    "under OSHA's COVID-19 Healthcare ETS (29 CFR "
                    "1910.502) in the US, HSE regulations in the UK, "
                    "and MOH guidelines in Saudi Arabia. Workers' "
                    "compensation eligibility for occupational disease "
                    "varies by jurisdiction."
                ),
                "sector": "healthcare",
                "corridor": "IN-UK",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Hazard pay promises made during emergency "
                    "recruitment are frequently unenforceable — they "
                    "appear in offer letters or verbal agreements but "
                    "not in the binding employment contract. The "
                    "retention bonus creates a new debt obligation. "
                    "OSHA enforcement data for 2020-2022 shows that "
                    "healthcare facilities received 2,400+ COVID-related "
                    "citations for PPE failures, with foreign-born "
                    "workers disproportionately assigned to the highest-"
                    "risk units."
                ),
            },
            {
                "id": "hm007_s3",
                "description": (
                    "After 3-6 months of deployment, the employer "
                    "discontinues hazard pay, citing 'normalization of "
                    "COVID-19 operations' or 'budget rebalancing.' The "
                    "worker continues to be assigned to COVID-positive "
                    "patient care units. PPE supply is inconsistent — "
                    "the employer provides surgical masks instead of "
                    "N95 respirators for aerosol-generating procedures, "
                    "citing supply chain constraints. OSHA's COVID-19 "
                    "ETS (effective June 2021) required employers to "
                    "provide N95 respirators for high-risk procedures, "
                    "but OSHA conducted only 2,500 healthcare inspections "
                    "nationally in 2021 (covering ~1% of healthcare "
                    "facilities)."
                ),
                "legal_basis": (
                    "Employers may modify discretionary pay programs "
                    "with notice. PPE standards are set by OSHA "
                    "(29 CFR 1910.134 for respiratory protection) "
                    "and CDC guidance, which evolved throughout the "
                    "pandemic. Employer decisions about PPE allocation "
                    "reflect risk assessment and supply availability. "
                    "Workers may file OSHA complaints, which trigger "
                    "inspection within 24 hours for imminent danger."
                ),
                "sector": "healthcare",
                "corridor": "KE-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Hazard pay removal while hazardous conditions "
                    "persist is a bait-and-switch. Inadequate PPE for "
                    "foreign-born healthcare workers is a documented "
                    "pattern — the National Nurses United survey (2020) "
                    "found immigrant nurses were 50% more likely to "
                    "report PPE shortages than US-born peers. The "
                    "worker's visa dependency prevents them from "
                    "refusing unsafe assignments under OSHA Section "
                    "11(c) protections without risking termination."
                ),
            },
            {
                "id": "hm007_s4",
                "description": (
                    "The worker contracts COVID-19 from occupational "
                    "exposure. The employer's HR department disputes "
                    "the workers' compensation claim, arguing the "
                    "infection was 'community-acquired' rather than "
                    "workplace-acquired. In the US, state workers' "
                    "compensation laws vary — only 28 states created "
                    "COVID-19 presumption rules for healthcare workers "
                    "by 2022 (NCCI analysis). In Saudi Arabia, the "
                    "General Organization for Social Insurance (GOSI) "
                    "requires proof of workplace transmission, which "
                    "is medically impossible to establish definitively. "
                    "The worker loses 2-4 weeks of wages during "
                    "quarantine, with only partial sick-pay coverage."
                ),
                "legal_basis": (
                    "Workers' compensation claims require demonstrating "
                    "that the injury or illness arose 'out of and in "
                    "the course of employment.' COVID-19 community "
                    "transmission makes causation difficult to prove. "
                    "States without presumption rules require the "
                    "worker to prove specific workplace exposure. "
                    "Employer-provided sick leave during quarantine is "
                    "governed by FFCRA (US, expired 2021), statutory "
                    "sick pay (UK), or contractual provisions."
                ),
                "sector": "healthcare",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Denying workers' compensation for healthcare "
                    "workers deployed to COVID wards shifts the cost "
                    "of occupational disease onto the most vulnerable "
                    "workers. WHO data shows healthcare workers "
                    "represented 14% of reported COVID-19 cases "
                    "globally in 2020 despite being 2-3% of the "
                    "population. The worker, already in debt from "
                    "recruitment fees and retention bonus obligations, "
                    "cannot afford to lose income or pursue a legal "
                    "challenge."
                ),
            },
            {
                "id": "hm007_s5",
                "description": (
                    "After recovery, the worker develops Long COVID "
                    "symptoms (fatigue, cognitive impairment, reduced "
                    "stamina) affecting clinical performance. The "
                    "employer initiates a 'performance improvement plan' "
                    "(PIP) citing slower task completion and increased "
                    "documentation errors. After 60-90 days on the PIP, "
                    "the employer terminates employment 'for cause,' "
                    "which under the H-1B visa (US) or Health and Care "
                    "Worker visa (UK) triggers a 60-day (US) or 14-day "
                    "(UK) window to find new employment or depart. "
                    "The retention bonus clawback clause activates, "
                    "demanding return of $3,000-7,000 (prorated). "
                    "Repatriation costs ($800-2,000) are borne by "
                    "the worker."
                ),
                "legal_basis": (
                    "Performance-based termination is lawful under at-will "
                    "employment (US) and standard contractual provisions. "
                    "Long COVID may qualify as a disability under ADA "
                    "(US) or Equality Act 2010 (UK), requiring "
                    "reasonable accommodations, but the worker must "
                    "formally request accommodation — which requires "
                    "awareness of the legal framework. Retention bonus "
                    "clawback clauses are generally enforceable if the "
                    "prorating formula is reasonable."
                ),
                "sector": "healthcare",
                "corridor": "PH-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Terminating a healthcare worker for performance "
                    "issues caused by an occupational illness (COVID-19) "
                    "contracted due to inadequate PPE is a compounding "
                    "exploitation — the employer profits from the "
                    "worker's high-risk deployment, denies the workers' "
                    "compensation claim, then terminates when the "
                    "occupational injury affects productivity. The "
                    "visa countdown and bonus clawback ensure the "
                    "worker departs quickly without pursuing legal "
                    "remedies. National Nurses United documented 436 "
                    "such cases in their 2022 report on immigrant "
                    "nurse pandemic experiences."
                ),
            },
        ],
        "chain_context": (
            "Pandemic emergency recruitment created a perfect storm for "
            "healthcare worker exploitation: genuine urgency legitimized "
            "fast-tracked visa processing and abbreviated due diligence, "
            "while hazard conditions justified premium pay promises "
            "that were later withdrawn. Each step — emergency "
            "recruitment, hazard pay agreements, PPE allocation "
            "decisions, workers' compensation adjudication, and "
            "performance management — follows standard HR and legal "
            "procedures. But the combination produces a cycle where "
            "the worker is recruited under emergency conditions, "
            "exposed to occupational hazards, denied compensation "
            "for resulting illness, and terminated when the illness "
            "affects performance. WHO, National Nurses United, and "
            "the Lancet Commission on Migration and Health all "
            "documented these patterns during 2020-2023."
        ),
        "emergent_risk": (
            "Pandemic exploitation cycle: emergency recruitment with "
            "hazard pay promises + inadequate PPE + occupational "
            "COVID-19 + denied workers' compensation + Long COVID "
            "performance termination + visa clock + bonus clawback "
            "= disposable high-risk workforce."
        ),
        "difficulty": "hard",
        "source_references": [
            "WHO, 'Health Worker Safety: A Priority for Patient Safety' (2020) — global healthcare worker infection and death data",
            "National Nurses United, 'Sins Against Our Nurses: The Pandemic Experience of Immigrant Healthcare Workers' (2022) — PPE disparities, termination patterns",
            "OSHA, 'COVID-19 Healthcare ETS Enforcement Summary' (2022) — citation data, inspection rates",
            "Lancet Commission on Migration and Health, 'Migration and Health in the COVID-19 Pandemic' (2021) — exploitation patterns",
            "NCCI, 'COVID-19 Workers' Compensation Presumption Analysis by State' (2022) — coverage gaps",
        ],
        "corridors": ["PH-US", "IN-UK", "KE-SA", "NP-QA"],
        "palermo_elements": {
            "act": ["recruitment", "receipt"],
            "means": ["deception", "coercion", "abuse of position of vulnerability", "fraud"],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "healthcare_migration_008",
        "name": "Reproductive Healthcare Coercion in Employment",
        "category": "healthcare_migration",
        "steps": [
            {
                "id": "hm008_s1",
                "description": (
                    "As part of the pre-departure medical examination "
                    "required for Gulf employment, the healthcare worker "
                    "(nurse, midwife, or lab technician) undergoes a "
                    "mandatory pregnancy test at a clinic designated by "
                    "the recruitment agency. Saudi Arabia requires "
                    "GAMCA (Gulf Approved Medical Centres Association) "
                    "certification, which includes a standard panel: "
                    "chest X-ray, blood tests (HIV, Hepatitis B/C, "
                    "syphilis), and a urine pregnancy test for female "
                    "applicants. The pregnancy test is administered as "
                    "a routine part of the panel without separate "
                    "informed consent. Workers who test positive are "
                    "immediately disqualified from deployment."
                ),
                "legal_basis": (
                    "GAMCA medical examination standards are set by "
                    "the GCC Health Ministers' Council and administered "
                    "by accredited medical centers in sending countries. "
                    "Pre-employment medical screening is standard "
                    "practice in international labor migration and is "
                    "authorized under bilateral labor agreements. "
                    "Fitness-for-duty assessments are a recognized "
                    "component of occupational health programs."
                ),
                "sector": "healthcare",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Mandatory pregnancy testing as an employment "
                    "condition violates CEDAW Article 11(2)(a), which "
                    "prohibits dismissal on grounds of pregnancy, and "
                    "ILO Maternity Protection Convention C183 Article 9, "
                    "which prohibits pregnancy testing as a condition "
                    "of employment. The GAMCA panel disguises the "
                    "pregnancy test as part of a general medical "
                    "screening, avoiding the appearance of a standalone "
                    "fertility check. HRW documented in 2014 that "
                    "pregnancy testing was standard for all female "
                    "Gulf-bound healthcare workers."
                ),
            },
            {
                "id": "hm008_s2",
                "description": (
                    "The employment contract, drafted under Saudi, "
                    "Qatari, or Kuwaiti law, contains a clause stating "
                    "that 'the employee shall not become pregnant during "
                    "the contract period' (typically 2-3 years) and "
                    "that 'pregnancy shall constitute a breach of "
                    "contract resulting in immediate termination and "
                    "repatriation at the employee's expense.' The "
                    "clause is embedded within a multi-page Arabic-"
                    "language contract addendum that is presented for "
                    "signature at the airport or upon arrival in the "
                    "destination country. The worker may or may not "
                    "receive an English/Tagalog/Amharic translation."
                ),
                "legal_basis": (
                    "Gulf labor codes do not explicitly prohibit "
                    "pregnancy termination clauses in employment "
                    "contracts. Saudi Labor Law Article 155 provides "
                    "10 weeks of maternity leave for Saudi women "
                    "but Article 2 excludes domestic and certain "
                    "healthcare workers from the Labor Law's scope. "
                    "Qatar Labor Law Article 96 provides 50 days "
                    "maternity leave but enforcement for foreign "
                    "workers is minimal. Contract terms are governed "
                    "by the law of the employment jurisdiction."
                ),
                "sector": "healthcare",
                "corridor": "PH-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Pregnancy termination clauses constitute forced "
                    "reproductive coercion — the worker must choose "
                    "between reproductive autonomy and employment. "
                    "CEDAW General Recommendation No. 26 (2008) on "
                    "women migrant workers specifically identifies "
                    "pregnancy-related termination clauses as a form "
                    "of discrimination. The worker signs under duress "
                    "— having already paid recruitment fees, quit their "
                    "home-country job, and arrived at the airport or "
                    "in the destination country with no practical "
                    "alternative."
                ),
            },
            {
                "id": "hm008_s3",
                "description": (
                    "The employer (a hospital or clinic in Riyadh, Doha, "
                    "or Kuwait City) mandates that female foreign "
                    "healthcare workers use employer-specified "
                    "contraception. In some documented cases, the "
                    "employer distributes contraceptive injections "
                    "(Depo-Provera) through the staff clinic or "
                    "requires workers to present pharmacy receipts for "
                    "oral contraceptive purchases as a condition of "
                    "continued employment. Annual pregnancy tests are "
                    "included in mandatory staff medical check-ups. "
                    "Workers who decline are flagged for 'non-compliance "
                    "with staff health protocols.'"
                ),
                "legal_basis": (
                    "Employer wellness programs that include "
                    "reproductive health services may be offered as "
                    "staff benefits. Periodic health screenings for "
                    "healthcare workers are standard practice to ensure "
                    "occupational fitness. Staff health protocols are "
                    "within the employer's operational discretion. "
                    "Contraception access is framed as a healthcare "
                    "benefit rather than a mandate."
                ),
                "sector": "healthcare",
                "corridor": "ET-LB",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Employer-mandated contraception is a direct "
                    "violation of bodily autonomy and reproductive "
                    "rights protected under CEDAW Article 16(1)(e) "
                    "(right to decide freely on number and spacing "
                    "of children) and ICESCR Article 12 (right to "
                    "health). Framing it as a 'health protocol' "
                    "disguises coercive reproductive control as "
                    "occupational health management. HRW's 2014 "
                    "Gulf report documented mandatory contraception "
                    "requirements in at least 12 healthcare facilities "
                    "across Saudi Arabia and the UAE."
                ),
            },
            {
                "id": "hm008_s4",
                "description": (
                    "A female healthcare worker who becomes pregnant "
                    "faces immediate consequences: the employer "
                    "invokes the pregnancy termination clause, issues "
                    "a termination notice with 30 days to vacate "
                    "employer-provided housing, and initiates 'final "
                    "exit' visa processing through the Saudi Jawazat "
                    "(passport department) or Qatar MOI. The worker "
                    "receives no maternity benefits, no severance "
                    "pay, and no repatriation assistance. End-of-"
                    "service benefits (typically 1-2 months' salary "
                    "per year worked) are withheld on the grounds "
                    "that termination was 'for cause' (breach of "
                    "contract). Return flight cost ($400-1,200) is "
                    "deducted from the final paycheck."
                ),
                "legal_basis": (
                    "Saudi Labor Law Article 80 permits termination "
                    "without notice or indemnity for 'a material "
                    "breach of contractual obligations.' If pregnancy "
                    "is defined as a breach in the contract, the "
                    "employer's legal position is that termination "
                    "follows the contractual framework. End-of-service "
                    "benefits under Article 84 are forfeitable upon "
                    "termination for cause under Article 80. Final "
                    "exit visas are processed within 3-10 business "
                    "days."
                ),
                "sector": "healthcare",
                "corridor": "PH-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Treating pregnancy as a terminable offense "
                    "constitutes discrimination prohibited by ILO "
                    "C183 Article 8 ('It shall be unlawful for an "
                    "employer to terminate the employment of a woman "
                    "during her pregnancy') and CEDAW Article 11(2)(a). "
                    "However, Saudi Arabia has not ratified ILO C183, "
                    "and CEDAW reservations limit its domestic "
                    "applicability. The worker loses not only "
                    "employment but housing, legal status, and "
                    "end-of-service benefits simultaneously. "
                    "Amnesty International documented 340 pregnancy-"
                    "related terminations of foreign healthcare "
                    "workers in the Gulf in 2019 alone."
                ),
            },
            {
                "id": "hm008_s5",
                "description": (
                    "The terminated worker is repatriated to the "
                    "Philippines, Ethiopia, or Indonesia with "
                    "outstanding recruitment debt ($3,000-8,000), no "
                    "end-of-service benefits, and a pregnancy to manage "
                    "without employer healthcare coverage. The worker "
                    "cannot return to Gulf employment for 2-3 years "
                    "(standard rehire waiting period for terminated "
                    "workers). The recruitment agency in the origin "
                    "country continues to collect on the salary-"
                    "deduction loan. The worker's professional "
                    "reputation is damaged — termination records in "
                    "the MUSANED/eDareh system flag the worker as "
                    "'contract breacher,' making future Gulf "
                    "recruitment difficult."
                ),
                "legal_basis": (
                    "Repatriation following contract termination is "
                    "standard procedure under Gulf immigration law. "
                    "Recruitment loan repayment obligations survive "
                    "employment termination as they are separate "
                    "financial contracts. The MUSANED system maintains "
                    "employment history for all foreign workers as "
                    "part of the digital labor mobility framework. "
                    "Rehire waiting periods are administrative "
                    "provisions set by destination-country immigration "
                    "authorities."
                ),
                "sector": "healthcare",
                "corridor": "ID-KW",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The full cycle reveals the reproductive coercion "
                    "chain: mandatory pregnancy testing → contractual "
                    "pregnancy prohibition → employer-mandated "
                    "contraception → pregnancy-as-termination-cause → "
                    "repatriation with debt. The worker's reproductive "
                    "choices are controlled by the employer for the "
                    "entire contract duration, and exercising reproductive "
                    "autonomy triggers financial ruin. CEDAW Committee "
                    "concluding observations on Saudi Arabia (2018) "
                    "and Qatar (2019) specifically flagged pregnancy-"
                    "related termination of foreign workers as a "
                    "systemic violation."
                ),
            },
        ],
        "chain_context": (
            "This chain documents the systematic control of female "
            "migrant healthcare workers' reproductive autonomy through "
            "individually defensible employment practices. Pre-"
            "employment medical screening, contractual terms, employer "
            "health protocols, for-cause termination, and repatriation "
            "processing each follow recognized administrative procedures. "
            "But the combination constitutes reproductive coercion — the "
            "worker must surrender reproductive autonomy for the "
            "duration of employment, and exercising that autonomy "
            "triggers immediate termination, debt activation, and "
            "deportation. CEDAW General Recommendation No. 26, ILO "
            "C183, and the OHCHR's 2019 report on migrant women's "
            "rights all identify pregnancy-conditioned employment as "
            "a form of gender-based exploitation that compounds the "
            "vulnerability created by migration status dependency."
        ),
        "emergent_risk": (
            "Reproductive coercion cycle: mandatory pregnancy testing "
            "+ contractual pregnancy ban + employer-mandated "
            "contraception + pregnancy-triggered termination + "
            "repatriation with debt = total employer control over "
            "female workers' reproductive autonomy for contract "
            "duration."
        ),
        "difficulty": "expert",
        "source_references": [
            "CEDAW General Recommendation No. 26 on Women Migrant Workers (2008) — pregnancy discrimination, reproductive coercion",
            "ILO Maternity Protection Convention C183 (2000) — Article 8 prohibition on pregnancy-based termination, Article 9 prohibition on pregnancy testing",
            "Human Rights Watch, 'As If I Am Not Human' (2008, updated 2014) — mandatory pregnancy testing and contraception in Gulf healthcare",
            "Amnesty International, 'Their Bodies, Their Bosses: Reproductive Coercion of Migrant Women Workers in the Gulf' (2019) — termination data",
            "CEDAW Committee, 'Concluding Observations on Saudi Arabia' (2018) and 'Qatar' (2019) — pregnancy-related termination of foreign workers",
            "OHCHR, 'Report on the Human Rights of Migrant Women' (2019) — gender-based exploitation and reproductive autonomy",
        ],
        "corridors": ["PH-SA", "ET-LB", "PH-QA", "ID-KW"],
        "palermo_elements": {
            "act": ["recruitment", "harbouring", "receipt"],
            "means": [
                "deception",
                "coercion",
                "abuse of position of vulnerability",
                "fraud",
                "threats",
            ],
            "purpose": ["forced labour", "exploitation", "servitude"],
        },
    },
]
