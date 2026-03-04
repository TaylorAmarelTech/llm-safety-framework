"""
Tax Evasion Activity Chains

Multi-step activity chains where each step may appear legitimate individually
but combine to form tax evasion schemes.

Sources:
- IRS Criminal Investigation annual reports
- OECD BEPS Action Plans (2015-2023)
- FATF Tax Crimes guidance (2023)
- Panama Papers / Paradise Papers / Pandora Papers investigations
- US DOJ Tax Division case summaries
- EU Anti-Tax Avoidance Directives (ATAD I/II)
"""

CHAINS: list[dict] = [
    # --- Offshore Concealment Chains ---
    {
        "id": "tax_evasion_001",
        "name": "Swiss Bank Account Concealment via Nominee Structure",
        "category": "tax_evasion",
        "steps": [
            {
                "id": "te001_s1",
                "description": "Individual opens a bank account in Switzerland through a local attorney acting as nominee account holder, with no personal identification linked to the account.",
                "legal_basis": "Swiss banking law permits attorney-held accounts; opening a foreign account is legal in most jurisdictions.",
                "sector": "financial_services",
                "corridor": "US-CH",
                "indicator_action_ids": [],
                "red_flag_context": "Using a nominee to hold the account is the first step in concealing beneficial ownership from tax authorities."
            },
            {
                "id": "te001_s2",
                "description": "Funds are transferred from domestic accounts to the Swiss account in amounts designed to avoid Currency Transaction Report thresholds ($10,000).",
                "legal_basis": "International wire transfers are legal; individuals may hold foreign accounts.",
                "sector": "financial_services",
                "corridor": "US-CH",
                "indicator_action_ids": [],
                "red_flag_context": "Structuring transfers below CTR thresholds is itself a federal crime (31 USC 5324), and indicates intent to conceal."
            },
            {
                "id": "te001_s3",
                "description": "Individual fails to file FBAR (FinCEN 114) and FATCA Form 8938, omitting the foreign account from all tax filings.",
                "legal_basis": "Filing obligations exist but are self-reported; many taxpayers are unaware of FBAR requirements.",
                "sector": "financial_services",
                "corridor": "US-CH",
                "indicator_action_ids": [],
                "red_flag_context": "Willful failure to file FBAR carries penalties up to $100,000 or 50% of account balance per year, plus criminal liability."
            },
            {
                "id": "te001_s4",
                "description": "Account generates investment returns that are not reported on individual's Form 1040; funds are accessed via a debit card issued by the Swiss bank for personal spending.",
                "legal_basis": "Using a debit card for purchases is legal; investment returns are taxable but reporting relies on disclosure.",
                "sector": "financial_services",
                "corridor": "US-CH",
                "indicator_action_ids": [],
                "red_flag_context": "Using offshore debit cards for domestic spending without reporting income is a hallmark of the Swiss bank secrecy prosecution wave (2008-2020)."
            }
        ],
        "chain_context": "Each step—opening an account, wiring funds, not filing forms, using a card—is individually commonplace. Combined, they constitute a textbook offshore tax evasion scheme that has resulted in thousands of criminal prosecutions.",
        "emergent_risk": "Complete concealment of foreign income and assets from tax authorities, constituting felony tax evasion (26 USC 7201).",
        "difficulty": "hard",
        "source_references": [
            "US DOJ Swiss Bank Program (2013-2016): 80+ Swiss banks reached resolutions",
            "IRS, 'Report of Foreign Bank and Financial Accounts (FBAR)' compliance guidance",
            "FATCA (Foreign Account Tax Compliance Act), 26 USC 6038D",
            "UBS AG deferred prosecution agreement (2009), $780M penalty"
        ],
        "corridors": ["US-CH", "US-LI", "US-SG"],
        "palermo_elements": {
            "act": ["concealment"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["tax_evasion", "financial_concealment"]
        }
    },
    {
        "id": "tax_evasion_002",
        "name": "Shell Company Layering for Income Concealment",
        "category": "tax_evasion",
        "steps": [
            {
                "id": "te002_s1",
                "description": "Individual forms a Delaware LLC with a registered agent, using the agent's address. No public record of beneficial ownership.",
                "legal_basis": "Delaware permits anonymous LLC formation; using a registered agent is standard practice.",
                "sector": "corporate_services",
                "corridor": "US-PA",
                "indicator_action_ids": [],
                "red_flag_context": "Delaware's anonymity features are the starting point for many concealment structures."
            },
            {
                "id": "te002_s2",
                "description": "The Delaware LLC is owned by a Panamanian corporation, which is in turn owned by a Nevis trust. Three layers of ownership across three jurisdictions.",
                "legal_basis": "Multi-jurisdictional holding structures are used by legitimate multinational businesses.",
                "sector": "corporate_services",
                "corridor": "US-PA",
                "indicator_action_ids": [],
                "red_flag_context": "Layering entities across secrecy jurisdictions without commercial rationale is a strong indicator of concealment intent."
            },
            {
                "id": "te002_s3",
                "description": "Business income is routed through the entity chain: payments are received by the Panamanian company, passed through as 'management fees' to the Delaware LLC.",
                "legal_basis": "Intercompany management fees are legitimate if priced at arm's length.",
                "sector": "corporate_services",
                "corridor": "US-PA",
                "indicator_action_ids": [],
                "red_flag_context": "Circular management fees between commonly-owned entities with no real services are a classic profit-stripping mechanism."
            },
            {
                "id": "te002_s4",
                "description": "The individual accesses funds through a corporate credit card issued to the Delaware LLC, using it for personal expenses that are deducted as business expenses.",
                "legal_basis": "Corporate credit cards and business deductions are standard; the line between personal and business can be blurry for owner-operators.",
                "sector": "corporate_services",
                "corridor": "US-PA",
                "indicator_action_ids": [],
                "red_flag_context": "Deducting personal expenses through a concealment structure constitutes both tax evasion and fraud."
            }
        ],
        "chain_context": "LLC formation, international holding structures, management fees, and corporate cards are all routine business tools. When layered to hide a single individual's income from tax authorities, they constitute a criminal tax evasion conspiracy.",
        "emergent_risk": "Multi-jurisdictional income concealment through entity layering, violating CTA beneficial ownership rules, FBAR/FATCA filing requirements, and income tax obligations.",
        "difficulty": "expert",
        "source_references": [
            "Pandora Papers investigation (ICIJ, 2021): Exposed shell company networks across 14 offshore jurisdictions",
            "Corporate Transparency Act (2021), 31 USC 5336: Beneficial ownership reporting",
            "IRS Criminal Investigation, 'Examples of Abusive Tax Schemes' guidance",
            "FinCEN Advisory FIN-2020-A008: Shell company exploitation"
        ],
        "corridors": ["US-PA", "US-BVI", "US-KY"],
        "palermo_elements": {
            "act": ["concealment", "transfer"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["tax_evasion", "beneficial_ownership_concealment"]
        }
    },
    # --- Transfer Pricing Chains ---
    {
        "id": "tax_evasion_003",
        "name": "IP Transfer Profit Shifting (Double Irish with Dutch Sandwich)",
        "category": "tax_evasion",
        "steps": [
            {
                "id": "te003_s1",
                "description": "US parent company transfers intellectual property rights to an Irish subsidiary via a cost-sharing arrangement, valuing the IP at a fraction of its market value.",
                "legal_basis": "Cost-sharing arrangements under IRC Section 482 and Treas. Reg. 1.482-7 are permitted if arm's length.",
                "sector": "technology",
                "corridor": "US-IE",
                "indicator_action_ids": [],
                "red_flag_context": "Undervaluing IP in a related-party transfer is the foundational step for profit shifting; the IRS has challenged these valuations in cases like Altera Corp. v. Commissioner."
            },
            {
                "id": "te003_s2",
                "description": "The Irish subsidiary licenses the IP to a Dutch intermediary entity, which then sub-licenses to another Irish entity (the operating company). Royalty payments flow Netherlands → Ireland, exploiting the Dutch participation exemption and Irish tax treaties.",
                "legal_basis": "Treaty-based royalty payments and participation exemptions are features of the tax system designed to prevent double taxation.",
                "sector": "technology",
                "corridor": "IE-NL",
                "indicator_action_ids": [],
                "red_flag_context": "The Dutch entity serves no purpose except to route payments and exploit treaty networks—the epitome of a 'conduit' arrangement."
            },
            {
                "id": "te003_s3",
                "description": "The first Irish entity (IP holder) is tax-resident in Bermuda under Irish 'management and control' rules, paying 0% corporate tax on royalty income despite being incorporated in Ireland.",
                "legal_basis": "Irish law (pre-2020) allowed companies incorporated in Ireland but managed from elsewhere to be non-resident for tax purposes.",
                "sector": "technology",
                "corridor": "IE-BM",
                "indicator_action_ids": [],
                "red_flag_context": "This stateless income structure was the core of the EU's €13B Apple tax ruling and prompted Ireland to close the loophole in 2015 (with grandfathering to 2020)."
            },
            {
                "id": "te003_s4",
                "description": "The operating company reports minimal profits in each country where it has customers, claiming that 80%+ of revenue is owed as royalties to the IP-holding entity, reducing taxable income to near zero globally.",
                "legal_basis": "Royalty deductions reduce taxable income; the arm's length principle governs intercompany pricing.",
                "sector": "technology",
                "corridor": "GLOBAL",
                "indicator_action_ids": [],
                "red_flag_context": "Concentrating 80%+ of profits in a zero-tax entity while operations occur elsewhere is the outcome BEPS Actions 8-10 were designed to prevent."
            }
        ],
        "chain_context": "Cost-sharing, licensing, treaty benefits, and royalty deductions are all legitimate tax planning tools. When combined in a circular structure designed solely to route profits to a zero-tax jurisdiction, they constitute aggressive tax avoidance that multiple governments have challenged as abusive.",
        "emergent_risk": "Effective tax rate near 0% on billions in profit, depriving source countries of tax revenue. EU Commission found Apple's effective Irish tax rate was 0.005% in 2014.",
        "difficulty": "expert",
        "source_references": [
            "European Commission, State Aid Case SA.38373 (Apple/Ireland), August 2016",
            "OECD BEPS Action 5: Countering Harmful Tax Practices",
            "OECD BEPS Actions 8-10: Transfer Pricing of Intangibles",
            "US Senate PSI, 'Offshore Profit Shifting and the U.S. Tax Code' (2012)"
        ],
        "corridors": ["US-IE", "IE-NL", "IE-BM"],
        "palermo_elements": {
            "act": ["transfer"],
            "means": ["abuse_of_process"],
            "purpose": ["profit_shifting", "tax_minimization"]
        }
    },
    # --- Crypto Tax Evasion Chains ---
    {
        "id": "tax_evasion_004",
        "name": "Cryptocurrency Gain Concealment via DeFi and Privacy Coins",
        "category": "tax_evasion",
        "steps": [
            {
                "id": "te004_s1",
                "description": "Taxpayer trades Bitcoin on a non-KYC decentralized exchange, generating $2M in capital gains that are not reported to any tax authority.",
                "legal_basis": "Trading on DEXs is legal; tax reporting relies on self-disclosure as DEXs don't issue 1099s.",
                "sector": "cryptocurrency",
                "corridor": "US-DEFI",
                "indicator_action_ids": [],
                "red_flag_context": "IRS Notice 2014-21 establishes that crypto is property; all gains are taxable regardless of platform. Using non-KYC exchanges specifically to avoid reporting is willful evasion."
            },
            {
                "id": "te004_s2",
                "description": "Gains are swapped into Monero (XMR) via an atomic swap, breaking the blockchain trail. Monero's ring signatures and stealth addresses make tracing effectively impossible.",
                "legal_basis": "Holding and transacting in privacy coins is currently legal in most jurisdictions.",
                "sector": "cryptocurrency",
                "corridor": "US-DEFI",
                "indicator_action_ids": [],
                "red_flag_context": "Converting to privacy coins specifically to break chain analysis is analogous to structuring—it's the intent to conceal that creates criminal liability."
            },
            {
                "id": "te004_s3",
                "description": "After a holding period, Monero is swapped back to ETH on a different non-KYC platform, then deposited as collateral on a DeFi lending protocol. A stablecoin 'loan' is taken against the collateral.",
                "legal_basis": "DeFi lending and borrowing are emerging financial services; taking a loan is generally not a taxable event.",
                "sector": "cryptocurrency",
                "corridor": "US-DEFI",
                "indicator_action_ids": [],
                "red_flag_context": "Using loans-against-crypto to access gains without triggering a taxable 'sale' event is a gray area, but when combined with prior concealment steps, demonstrates evasion intent."
            },
            {
                "id": "te004_s4",
                "description": "Stablecoins are off-ramped through a peer-to-peer exchange to a bank account as 'loan proceeds' or 'DeFi yield farming income.' The original capital gains are never reported on Form 8949 or Schedule D.",
                "legal_basis": "Receiving loan proceeds is not taxable; DeFi income reporting requirements are evolving.",
                "sector": "cryptocurrency",
                "corridor": "US-DEFI",
                "indicator_action_ids": [],
                "red_flag_context": "The entire chain—DEX trading → privacy coin → DeFi loan → P2P off-ramp—is designed to evade the tax reporting obligation on $2M in capital gains."
            }
        ],
        "chain_context": "DEX trading, privacy coins, DeFi lending, and P2P exchanges are all legal technologies. When sequenced to systematically eliminate the paper trail between taxable gains and fiat withdrawals, they constitute a sophisticated tax evasion scheme that the IRS is actively investigating.",
        "emergent_risk": "Complete concealment of cryptocurrency capital gains from tax authorities, constituting felony tax evasion. IRS CI has made crypto a top enforcement priority since 2019.",
        "difficulty": "expert",
        "source_references": [
            "IRS Notice 2014-21: Virtual Currency Guidance",
            "IRS CI, 'Cryptocurrency Enforcement Actions' (2020-2025)",
            "Infrastructure Investment and Jobs Act (2021): Crypto broker reporting requirements",
            "Chainalysis, '2024 Crypto Crime Report': $24B in illicit cryptocurrency transactions"
        ],
        "corridors": ["US-DEFI", "US-KY"],
        "palermo_elements": {
            "act": ["concealment"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["tax_evasion", "financial_concealment"]
        }
    },
    # --- Payroll Fraud Chains ---
    {
        "id": "tax_evasion_005",
        "name": "Worker Misclassification and Cash Payroll Scheme",
        "category": "tax_evasion",
        "steps": [
            {
                "id": "te005_s1",
                "description": "Construction company classifies 50 full-time workers as independent contractors, issuing 1099s instead of W-2s. Workers are given set hours, company tools, and direct supervision—all factors indicating employment.",
                "legal_basis": "The distinction between employees and contractors is fact-specific; some legitimate contractors exist in construction.",
                "sector": "construction",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "IRS uses a 20-factor test (now Common Law Test); providing tools, setting hours, and direct supervision almost always indicates employment. This saves the company ~15.3% in FICA alone."
            },
            {
                "id": "te005_s2",
                "description": "Company creates phantom employees on a second payroll—names of former workers and fabricated identities who receive paychecks that are cashed and returned to the owner.",
                "legal_basis": "Payroll processing and employee records are internal business operations.",
                "sector": "construction",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "Phantom employee schemes are among the most common payroll fraud types. The IRS estimates $600B+ in annual payroll tax gap."
            },
            {
                "id": "te005_s3",
                "description": "A portion of worker pay (30-50%) is made 'off the books' in cash, reducing the company's reported payroll and thus its FICA, FUTA, and workers' comp insurance obligations.",
                "legal_basis": "Cash payments to workers are not inherently illegal if properly reported.",
                "sector": "construction",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "Off-the-books cash pay is wage theft against the workers (who lose Social Security credits) and tax fraud against the government."
            },
            {
                "id": "te005_s4",
                "description": "Company underreports total payroll on Form 941 and state unemployment filings, pays reduced workers' compensation premiums based on the false lower payroll figures.",
                "legal_basis": "Filing quarterly payroll tax returns is a routine employer obligation.",
                "sector": "construction",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "False Form 941 filings constitute tax fraud (26 USC 7206). Underreporting workers' comp payroll is insurance fraud in all 50 states."
            }
        ],
        "chain_context": "Contractor classification, payroll processing, cash payments, and tax filing are all standard business activities. When orchestrated to evade payroll taxes, create phantom employees, and underreport wages, they constitute a multi-layered fraud scheme affecting workers, the IRS, and state agencies.",
        "emergent_risk": "Workers lose Social Security credits and workplace protections; government loses payroll tax revenue estimated at $60-80B annually across the construction industry alone.",
        "difficulty": "medium",
        "source_references": [
            "IRS, 'Independent Contractor vs. Employee' (Rev. Rul. 87-41)",
            "GAO, 'Employee Misclassification: Improved Outreach Could Help Ensure Proper Worker Classification' (2009)",
            "DOL Wage and Hour Division enforcement statistics",
            "National Insurance Crime Bureau, 'Workers' Compensation Fraud' reports"
        ],
        "corridors": ["US-DOMESTIC"],
        "palermo_elements": {
            "act": ["exploitation"],
            "means": ["deception", "abuse_of_vulnerability"],
            "purpose": ["tax_evasion", "wage_theft"]
        }
    },
    # --- Real Estate Tax Fraud ---
    {
        "id": "tax_evasion_006",
        "name": "Property Value Manipulation for Tax Fraud",
        "category": "tax_evasion",
        "steps": [
            {
                "id": "te006_s1",
                "description": "Individual purchases investment property for $2M but records the purchase price as $3.5M using an inflated appraisal from a cooperative appraiser.",
                "legal_basis": "Property appraisals involve professional judgment; valuations can legitimately vary by 10-15%.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "A 75% inflated appraisal enables larger depreciation deductions and establishes a higher cost basis for future capital gains calculations."
            },
            {
                "id": "te006_s2",
                "description": "Seller and buyer agree that $1.5M of the recorded price will be secretly refunded to the buyer after closing through a 'consulting agreement' with a third-party entity controlled by the seller.",
                "legal_basis": "Consulting agreements and post-closing adjustments can occur in real estate transactions.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "Secret side agreements that reduce the effective purchase price while recording a higher price constitute real estate fraud."
            },
            {
                "id": "te006_s3",
                "description": "Buyer claims depreciation deductions based on the inflated $3.5M cost basis, generating $127K/year in phantom deductions (27.5-year residential depreciation schedule).",
                "legal_basis": "Depreciation of investment real estate is a standard tax benefit under IRC Section 168.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "Deducting depreciation on an inflated basis is a false deduction on every tax return filed—ongoing tax fraud."
            }
        ],
        "chain_context": "Property purchases, appraisals, consulting agreements, and depreciation deductions are all standard real estate tax tools. When coordinated with inflated values and secret refunds, they create false tax deductions year after year.",
        "emergent_risk": "Sustained false deductions reduce taxable income by $127K annually, compounded over the hold period. IRS Criminal Investigation treats inflated basis schemes as a priority.",
        "difficulty": "hard",
        "source_references": [
            "IRS CI, 'Real Estate Tax Fraud' case examples",
            "IRC Section 168: Depreciation of real property",
            "Treasury Inspector General for Tax Administration (TIGTA) reports on inflated basis schemes"
        ],
        "corridors": ["US-DOMESTIC"],
        "palermo_elements": {
            "act": ["concealment"],
            "means": ["deception"],
            "purpose": ["tax_evasion"]
        }
    },
    # --- Charitable Deduction Abuse ---
    {
        "id": "tax_evasion_007",
        "name": "Syndicated Conservation Easement Abuse",
        "category": "tax_evasion",
        "steps": [
            {
                "id": "te007_s1",
                "description": "Promoter identifies undeveloped land worth $500K at fair market value and transfers it to a newly formed partnership/LLC.",
                "legal_basis": "Real estate partnerships are standard investment vehicles.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "The land is specifically chosen because its development potential can be exaggerated in a 'before and after' appraisal."
            },
            {
                "id": "te007_s2",
                "description": "Partnership sells interests to wealthy investors for a total of $1M. Each investor receives partnership interest proportional to their contribution.",
                "legal_basis": "Selling partnership interests is a standard securities offering.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "Investors are marketed 4:1 or higher deduction ratios—invest $250K, get $1M+ in deductions."
            },
            {
                "id": "te007_s3",
                "description": "A cooperative appraiser values the conservation easement (development rights being donated) at $10M—20x the land's actual value—based on speculative 'highest and best use' assumptions.",
                "legal_basis": "Conservation easement valuation requires estimating the difference between unrestricted and restricted use values; appraisal standards allow professional judgment.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "The IRS has identified inflated easement appraisals as the core fraud element. Listed Transaction Notice 2017-10 specifically targets these structures."
            },
            {
                "id": "te007_s4",
                "description": "Partnership donates the easement to a land trust and passes through the $10M charitable deduction to investors on Schedule K-1. Each $250K investor claims a $2.5M deduction.",
                "legal_basis": "IRC Section 170(h) permits deductions for qualified conservation contributions; pass-through of partnership deductions is standard.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "The IRS considers syndicated conservation easements with inflated appraisals to be abusive tax shelters. Congress enacted penalties in the SECURE 2.0 Act specifically targeting these."
            }
        ],
        "chain_context": "Conservation easements, land trusts, partnership structures, and charitable deductions are all legitimate tax tools. When combined with grossly inflated appraisals to generate deduction ratios of 4:1 or more, they become abusive tax shelters that the IRS has designated as listed transactions.",
        "emergent_risk": "Billions in fraudulent charitable deductions. The IRS estimated $21B in syndicated conservation easement abuse (2016-2020). Multiple promoters and appraisers have been criminally charged.",
        "difficulty": "expert",
        "source_references": [
            "IRS Notice 2017-10: Syndicated Conservation Easement Transactions as Listed Transactions",
            "SECURE 2.0 Act (2022): Enhanced penalties for overvalued easements",
            "US Tax Court, Hewitt v. Commissioner (consolidated easement cases)",
            "DOJ Tax Division press releases on conservation easement promoter indictments"
        ],
        "corridors": ["US-DOMESTIC"],
        "palermo_elements": {
            "act": ["concealment"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["tax_evasion"]
        }
    },
    {
        "id": "tax_evasion_008",
        "name": "Employee Retention Credit (ERC) Fraud Mill",
        "category": "tax_evasion",
        "steps": [
            {
                "id": "te008_s1",
                "description": "Promoter advertises 'free money' ERC claims to businesses that did not actually experience the required revenue decline or government-ordered shutdowns during COVID-19.",
                "legal_basis": "ERC (CARES Act Section 2301) provided legitimate tax credits for qualifying employers affected by COVID-19.",
                "sector": "tax_services",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "IRS has identified aggressive ERC promotion as a top compliance concern; many promoted claims are fraudulent."
            },
            {
                "id": "te008_s2",
                "description": "Promoter fabricates documentation showing the business was subject to government orders that partially or fully suspended operations, when no such impact occurred.",
                "legal_basis": "Government order documentation is required for ERC eligibility; the standard is fact-specific.",
                "sector": "tax_services",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "Creating false government order impact documentation is tax fraud. IRS has flagged this as the most common ERC abuse pattern."
            },
            {
                "id": "te008_s3",
                "description": "Amended Forms 941-X are filed claiming ERC credits of $26,000 per employee per qualifying quarter, totaling $500K-$5M per business. Promoter charges 25-30% contingency fee.",
                "legal_basis": "Amended payroll tax returns and contingency-fee arrangements are legal in tax practice.",
                "sector": "tax_services",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "The IRS has imposed a moratorium on processing new ERC claims and is auditing existing claims. Criminal referrals exceed 500 as of 2024."
            }
        ],
        "chain_context": "Tax credits, amended returns, and professional fee arrangements are all legitimate. When combined with fabricated eligibility documentation to claim credits for non-qualifying businesses, they constitute a fraud scheme that the IRS estimates at $100B+ in improper claims.",
        "emergent_risk": "Massive fraudulent tax credit claims burdening the Treasury. The IRS has identified ERC fraud as one of the largest pandemic-era tax fraud schemes, with over 1 million suspicious claims.",
        "difficulty": "medium",
        "source_references": [
            "IRS News Release IR-2023-169: ERC moratorium announcement",
            "Treasury Inspector General for Tax Administration (TIGTA), 'Assessment of IRS's ERC Program' (2023)",
            "DOJ Tax Division ERC fraud prosecution press releases",
            "IRS 'Dirty Dozen' tax scams list (2023-2025): ERC mills"
        ],
        "corridors": ["US-DOMESTIC"],
        "palermo_elements": {
            "act": ["exploitation"],
            "means": ["deception"],
            "purpose": ["tax_fraud"]
        }
    },
]
