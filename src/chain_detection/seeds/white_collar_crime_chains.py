"""
White Collar Crime Activity Chains

Multi-step activity chains where each step may appear as legitimate business
activity but combine to form securities fraud, corporate fraud, and
corruption schemes.

Sources:
- SEC Enforcement Division annual reports and litigation releases
- DOJ Criminal Division, Fraud Section case summaries
- PCAOB inspection reports and enforcement actions
- FCPA enforcement database (Stanford Law School)
- UK Serious Fraud Office case summaries
- Academic: Beasley et al., 'Fraudulent Financial Reporting' (COSO/Treadway)
"""

CHAINS: list[dict] = [
    # --- Securities Fraud Chains ---
    {
        "id": "white_collar_001",
        "name": "Micro-Cap Pump-and-Dump via Social Media Manipulation",
        "category": "white_collar_crime",
        "steps": [
            {
                "id": "wc001_s1",
                "description": "Group acquires controlling interest (5M+ shares) in a dormant shell company listed on OTC Markets, at prices below $0.01/share. Total cost: $10,000-$50,000.",
                "legal_basis": "Purchasing shares of publicly listed companies is legal; OTC Markets are a legitimate trading venue for smaller companies.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Acquiring control of dormant shell companies is the setup step for pump-and-dump schemes. SEC tracks 'blank check' shell company acquisitions."
            },
            {
                "id": "wc001_s2",
                "description": "The shell company announces a pivot to a trending sector (AI, cannabis, EV, crypto) through a press release, with no actual business operations, revenue, or employees.",
                "legal_basis": "Companies may change their business direction; press releases are a standard corporate communication tool.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Fraudulent press releases about non-existent business operations violate Section 10(b) and Rule 10b-5. SEC has brought hundreds of cases involving false press releases."
            },
            {
                "id": "wc001_s3",
                "description": "A coordinated social media campaign creates 100+ fake accounts on Reddit (WallStreetBets), Twitter/X, StockTwits, and Discord to post fabricated 'due diligence' and bullish price targets. Paid stock promoters send email blasts to 500K+ subscribers.",
                "legal_basis": "Discussing stocks on social media is protected speech; paid promoters must disclose compensation but many do not.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Coordinated campaigns using fake accounts and undisclosed paid promotion to inflate stock prices are market manipulation under 15 USC 78i(a)(2)."
            },
            {
                "id": "wc001_s4",
                "description": "As the stock price rises from $0.01 to $2.00+ on retail investor buying, the controlling group sells their shares into the artificially inflated demand. The stock collapses after selling is complete, leaving retail investors with losses.",
                "legal_basis": "Selling shares one owns is a normal market activity; the timing of sales is generally at the holder's discretion.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "The complete cycle—acquire, promote, sell into hype—is textbook pump-and-dump. The controlling group profits $1M-$10M+ while retail investors absorb the losses."
            }
        ],
        "chain_context": "Buying shares, issuing press releases, discussing stocks online, and selling holdings are all individually legal activities. When orchestrated as a coordinated scheme to artificially inflate a stock's price and sell into manufactured demand, they constitute securities fraud and market manipulation.",
        "emergent_risk": "Retail investors collectively lose millions; market integrity is undermined. SEC has made social media pump-and-dumps a top enforcement priority since 2021.",
        "difficulty": "hard",
        "source_references": [
            "SEC Litigation Release No. 25591 (social media pump-and-dump enforcement)",
            "SEC, 'Investor Alert: Social Media and Investing' (2023)",
            "DOJ, 'SEC Charges 16 Individuals in Scheme to Manipulate Stocks via Social Media' (2022)",
            "15 USC 78i(a)(2): Market manipulation prohibition"
        ],
        "corridors": ["US-SEC", "US-DOJ"],
        "palermo_elements": {
            "act": ["deception"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["securities_fraud", "market_manipulation"]
        }
    },
    # --- Insider Trading Chain ---
    {
        "id": "white_collar_002",
        "name": "Multi-Tipper Insider Trading Ring",
        "category": "white_collar_crime",
        "steps": [
            {
                "id": "wc002_s1",
                "description": "Corporate insider (VP of M&A at a pharmaceutical company) learns that the company will acquire a biotech target at a 60% premium. The deal will be announced in 3 weeks.",
                "legal_basis": "Employees routinely access material non-public information (MNPI) as part of their job duties.",
                "sector": "pharmaceutical",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "The insider has a duty not to trade or tip on MNPI. This is the origin of the information chain that SEC will trace."
            },
            {
                "id": "wc002_s2",
                "description": "Insider tips a close friend (Tippee 1) using a prepaid 'burner' phone. Tippee 1 buys $500K in call options on the target company. Insider expects to share in the profits.",
                "legal_basis": "Friends may discuss business and investments; purchasing call options is a standard trading activity.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Trading on a tip from an insider who expects a personal benefit violates Rule 10b-5 for both the tipper and tippee (Dirks v. SEC, Salman v. US)."
            },
            {
                "id": "wc002_s3",
                "description": "Tippee 1 passes the information to two additional friends (Tippees 2 and 3), who each buy shares and options. The trading pattern across all three accounts shows unusual pre-announcement activity in the target stock.",
                "legal_basis": "Individuals may recommend stocks to friends; sharing investment ideas is common.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Remote tippees are liable if they knew or should have known the information originated from an insider. SEC's EDGAR/MATS surveillance systems detect unusual options activity pre-announcement."
            },
            {
                "id": "wc002_s4",
                "description": "After the merger announcement, all three tippees sell their positions for combined profits of $3M. Profits are shared with the original insider through cash payments, gifts, and reciprocal tips on future deals.",
                "legal_basis": "Selling securities after a public announcement is standard; personal gifts between friends are normal.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "The profit-sharing completes the quid pro quo. SEC regularly traces tipping chains through phone records, trading records, and financial relationships."
            }
        ],
        "chain_context": "Learning about deals at work, having phone conversations with friends, buying stocks, and selling after news breaks are all everyday activities. When connected by MNPI flowing from insider to tippees with shared profits, they constitute an insider trading conspiracy.",
        "emergent_risk": "Undermining market fairness and investor confidence. The SEC brings 50+ insider trading cases annually, with penalties including disgorgement, civil fines (up to 3x profits), and criminal imprisonment (up to 20 years).",
        "difficulty": "hard",
        "source_references": [
            "Dirks v. SEC, 463 U.S. 646 (1983): Tipper-tippee liability framework",
            "Salman v. United States, 580 U.S. ___ (2016): Gift of MNPI to family/friends",
            "SEC v. Rajaratnam (Galleon Group): Largest insider trading case ($63.8M)",
            "SEC, 'Analysis of Insider Trading Patterns Preceding M&A Announcements' (2020)"
        ],
        "corridors": ["US-SEC", "US-DOJ"],
        "palermo_elements": {
            "act": ["deception"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["insider_trading", "securities_fraud"]
        }
    },
    # --- Corporate Accounting Fraud ---
    {
        "id": "white_collar_003",
        "name": "Revenue Recognition Fraud (Channel Stuffing)",
        "category": "white_collar_crime",
        "steps": [
            {
                "id": "wc003_s1",
                "description": "CFO determines the company will miss quarterly revenue consensus by $50M (15%). Missing estimates will trigger a stock price decline and potential analyst downgrades. CFO's compensation is tied to meeting targets.",
                "legal_basis": "Monitoring revenue against forecasts is a core CFO responsibility; performance-based compensation is standard.",
                "sector": "technology",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "The incentive structure creates the motive for fraud. COSO research shows CEO/CFO compensation pressure is present in 85% of financial reporting fraud cases."
            },
            {
                "id": "wc003_s2",
                "description": "Sales team is directed to offer distributors extended payment terms (180+ days), guaranteed return rights, and volume rebates to 'pull forward' next quarter's orders into the current quarter.",
                "legal_basis": "Extended payment terms and volume discounts are common commercial practices; trade loading exists in many industries.",
                "sector": "technology",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Side agreements granting return rights mean revenue should not be recognized under ASC 606 (GAAP) because control has not transferred. The side letters are typically hidden from auditors."
            },
            {
                "id": "wc003_s3",
                "description": "Secret side letters are signed with distributors guaranteeing full return/credit for any unsold product. These side letters are kept off the books and hidden from the external auditor. Revenue of $50M is recorded as if it were a final sale.",
                "legal_basis": "Sales agreements and side letters are standard business documents; revenue recognition follows accounting standards.",
                "sector": "technology",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Hidden side letters are the smoking gun in channel stuffing cases. They prove the company knew the revenue didn't meet recognition criteria. Cases: Sunbeam, Bristol-Myers, Monsanto."
            },
            {
                "id": "wc003_s4",
                "description": "Company reports earnings that meet consensus. Stock price holds steady. CFO and management receive performance bonuses. Next quarter, the stuffed product returns as credits, creating a growing hole that requires more aggressive stuffing to fill.",
                "legal_basis": "Reporting earnings, paying bonuses, and processing product returns are all normal business activities.",
                "sector": "technology",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "The accelerating nature of channel stuffing (each quarter requires more stuffing to cover the prior quarter's returns) mirrors a Ponzi scheme dynamic and inevitably collapses."
            }
        ],
        "chain_context": "Sales negotiations, payment terms, product returns, and quarterly reporting are all routine business. When combined with hidden side agreements that make recorded sales fictitious, they constitute accounting fraud that violates GAAP, SOX, and securities laws.",
        "emergent_risk": "Inflated financial statements mislead investors, inflate executive compensation, and inevitably collapse. Sunbeam recorded $60M+ in fictitious revenue via channel stuffing before restating and filing bankruptcy.",
        "difficulty": "expert",
        "source_references": [
            "SEC v. Sunbeam Corporation (2001): Landmark channel stuffing case",
            "SEC v. Bristol-Myers Squibb (2004): $150M channel stuffing settlement",
            "ASC 606 (Revenue from Contracts with Customers): Control transfer requirements",
            "COSO, 'Fraudulent Financial Reporting: 1998-2007' (Treadway Commission)"
        ],
        "corridors": ["US-SEC", "US-DOJ"],
        "palermo_elements": {
            "act": ["deception"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["securities_fraud", "accounting_fraud"]
        }
    },
    # --- Ponzi Scheme Chain ---
    {
        "id": "white_collar_004",
        "name": "Investment Fund Ponzi Scheme with Fabricated Returns",
        "category": "white_collar_crime",
        "steps": [
            {
                "id": "wc004_s1",
                "description": "Fund manager establishes a hedge fund promising 10-15% annual returns through a proprietary 'split-strike conversion' strategy. The fund is registered as a small advisor (under $150M) to avoid SEC examination requirements.",
                "legal_basis": "Starting a hedge fund with a proprietary strategy is standard; smaller advisors may be exempt from SEC registration (regulated by states instead).",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Deliberately structuring to avoid regulatory oversight is the first warning sign. Madoff similarly avoided SEC registration for years."
            },
            {
                "id": "wc004_s2",
                "description": "Fund generates fabricated monthly account statements showing consistent positive returns regardless of market conditions. An in-house, non-independent administrator produces the statements rather than a third-party fund administrator.",
                "legal_basis": "Producing investor statements is standard; fund administration can be done in-house or outsourced.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Consistent returns in all market conditions and in-house administration are two of the strongest Ponzi red flags. Madoff generated positive returns in 96% of months over 17 years."
            },
            {
                "id": "wc004_s3",
                "description": "New investor capital is used to pay 'returns' to existing investors and fund manager's lavish lifestyle. No actual trading occurs; funds are deposited into a single Chase bank account (not a brokerage account with DTCC custody).",
                "legal_basis": "Managing fund cash flows and paying returns to investors are normal fund operations.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "The absence of actual brokerage statements, DTCC custodial records, or counterparty confirmations is the definitive proof of fraud. Auditors who failed to verify custody enabled Madoff for decades."
            },
            {
                "id": "wc004_s4",
                "description": "When an investor requests a large redemption, the manager delays payment, recruits new investors to cover the withdrawal, or offers enhanced returns for keeping money in the fund. If net redemptions exceed new capital, the scheme collapses.",
                "legal_basis": "Fund managers may have legitimate lockup periods and redemption queues; recruiting new investors is standard marketing.",
                "sector": "financial_services",
                "corridor": "US-SEC",
                "indicator_action_ids": [],
                "red_flag_context": "Redemption delays and aggressive recruitment to cover withdrawals are the endgame indicators. When the 2008 financial crisis triggered simultaneous redemption requests, Madoff's $65B Ponzi collapsed within weeks."
            }
        ],
        "chain_context": "Starting a fund, generating statements, processing flows, and managing redemptions are all normal investment management activities. When returns are fabricated and investor capital is the only source of 'returns,' the fund is a Ponzi scheme that will inevitably collapse, devastating investors.",
        "emergent_risk": "Complete investor loss when the scheme collapses. Madoff: $65B in fabricated returns, $17.5B in actual investor losses. The SEC failed to detect the fraud despite multiple tips.",
        "difficulty": "hard",
        "source_references": [
            "SEC OIG, 'Investigation of Failure to Uncover Bernard Madoff's Ponzi Scheme' (2009)",
            "SEC v. Bernard L. Madoff Investment Securities LLC (2008)",
            "SEC, 'Ponzi Scheme Red Flags' investor education bulletin",
            "Markopolos, H., 'No One Would Listen' (2010): Warnings ignored by SEC"
        ],
        "corridors": ["US-SEC", "US-DOJ"],
        "palermo_elements": {
            "act": ["deception"],
            "means": ["deception", "abuse_of_vulnerability"],
            "purpose": ["investment_fraud"]
        }
    },
    # --- FCPA Bribery Chain ---
    {
        "id": "white_collar_005",
        "name": "Foreign Bribery via Sham Consulting Arrangement (FCPA)",
        "category": "white_collar_crime",
        "steps": [
            {
                "id": "wc005_s1",
                "description": "Defense contractor is bidding on a $200M military equipment contract with a foreign government. A local intermediary advises that a 10% 'commission' ($20M) to the procurement minister's family is expected.",
                "legal_basis": "Using local agents and intermediaries is standard practice in international defense procurement.",
                "sector": "defense_contracting",
                "corridor": "US-DOJ",
                "indicator_action_ids": [],
                "red_flag_context": "Third-party intermediaries are the most common FCPA violation vehicle. DOJ/SEC enforcement actions show 90%+ of FCPA cases involve intermediaries."
            },
            {
                "id": "wc005_s2",
                "description": "Company retains a 'consulting firm' owned by the minister's brother-in-law. The consulting agreement calls for $20M in 'market research and government relations advisory services' with vague deliverables.",
                "legal_basis": "Hiring local consultants for market intelligence and government relations is common in international business; consulting fees are legitimate expenses.",
                "sector": "defense_contracting",
                "corridor": "US-DOJ",
                "indicator_action_ids": [],
                "red_flag_context": "The DOJ/SEC FCPA Resource Guide specifically identifies family-connected consultants, disproportionate fees, and vague deliverables as the highest-risk third-party red flags."
            },
            {
                "id": "wc005_s3",
                "description": "The consulting firm produces a generic 20-page market report as its 'deliverable' and invoices $20M. The payment is approved by the regional VP after minimal due diligence. The consulting firm passes 90% of the payment to the minister's family through multiple bank accounts.",
                "legal_basis": "Paying invoices and processing vendor payments are routine business operations. The amount, while large, is proportional to the contract value.",
                "sector": "defense_contracting",
                "corridor": "US-DOJ",
                "indicator_action_ids": [],
                "red_flag_context": "The gap between a $20M payment and a 20-page report is the clearest evidence of a sham arrangement. DOJ guidelines require 'reasonable' relationship between payment and services."
            },
            {
                "id": "wc005_s4",
                "description": "The company wins the $200M contract. Internal accounting records the $20M consulting fee as 'business development expense.' Books and records do not reflect the true purpose of the payment.",
                "legal_basis": "Recording business expenses in accounting systems is a standard internal control requirement.",
                "sector": "defense_contracting",
                "corridor": "US-DOJ",
                "indicator_action_ids": [],
                "red_flag_context": "Mischaracterizing bribes as legitimate business expenses violates the FCPA's books-and-records provisions (15 USC 78m(b)) even if the anti-bribery provisions aren't charged."
            }
        ],
        "chain_context": "Hiring consultants, paying for market research, recording expenses, and winning contracts are all normal business activities in international defense procurement. When the consultant is connected to the decision-maker and the payment is a disguised bribe, the entire chain constitutes FCPA violations.",
        "emergent_risk": "FCPA violations carry severe penalties: criminal fines up to 2x the benefit obtained, disgorgement of profits, imprisonment (up to 5 years per count), and debarment from government contracts. Average FCPA settlement: $100M+.",
        "difficulty": "hard",
        "source_references": [
            "DOJ/SEC, 'A Resource Guide to the U.S. Foreign Corrupt Practices Act' (2020 2nd ed.)",
            "Stanford Law School FCPA Clearinghouse: Enforcement statistics",
            "DOJ FCPA enforcement actions: Siemens ($1.6B), Odebrecht ($3.5B), Ericsson ($1B)",
            "OECD, 'Foreign Bribery Report: Analysis of the Crime' (2014)"
        ],
        "corridors": ["US-DOJ", "UK-FCA"],
        "palermo_elements": {
            "act": ["corruption"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["bribery", "contract_procurement"]
        }
    },
    # --- Embezzlement Chain ---
    {
        "id": "white_collar_006",
        "name": "Non-Profit Executive Embezzlement via Ghost Vendors",
        "category": "white_collar_crime",
        "steps": [
            {
                "id": "wc006_s1",
                "description": "Executive director of a $10M/year non-profit creates a fictitious consulting company registered to a P.O. Box, using a name similar to a real vendor (e.g., 'Acme Consulting LLC' vs. the real 'Acme Consultants Inc.').",
                "legal_basis": "Forming an LLC is a standard business activity; using a P.O. Box for a registered address is common.",
                "sector": "nonprofit",
                "corridor": "US-DOJ",
                "indicator_action_ids": [],
                "red_flag_context": "Ghost vendor schemes rely on names close enough to real vendors that casual review won't catch them. The P.O. Box prevents physical verification."
            },
            {
                "id": "wc006_s2",
                "description": "Monthly invoices from the ghost vendor ($15K-$30K each, totaling $300K/year) are submitted for 'program consulting,' 'strategic advisory services,' and 'community outreach support.' The executive director approves all invoices under their spending authority.",
                "legal_basis": "Non-profits routinely engage consultants; invoice amounts below dual-approval thresholds can be approved by a single authorized signer.",
                "sector": "nonprofit",
                "corridor": "US-DOJ",
                "indicator_action_ids": [],
                "red_flag_context": "The lack of competitive bidding, vague service descriptions, and single-approver authority are the internal control weaknesses that enable the scheme."
            },
            {
                "id": "wc006_s3",
                "description": "Payments are made by check or ACH to the ghost vendor's bank account, which is controlled by the executive director using a separate personal bank account. Funds are then transferred to personal accounts for living expenses, luxury purchases, and vacations.",
                "legal_basis": "Processing vendor payments is a routine accounts payable function.",
                "sector": "nonprofit",
                "corridor": "US-DOJ",
                "indicator_action_ids": [],
                "red_flag_context": "The direct financial benefit to the authorizing executive is the core embezzlement. Non-profit fraud is estimated at 5-7% of organizational revenue (ACFE)."
            },
            {
                "id": "wc006_s4",
                "description": "Annual audit fails to detect the scheme because the auditor relies on management representations, doesn't independently verify vendor existence, and doesn't test for related-party transactions between the ghost vendor and the executive director.",
                "legal_basis": "External audits follow generally accepted auditing standards (GAAS); auditors are entitled to rely on management representations unless there is reason to suspect fraud.",
                "sector": "nonprofit",
                "corridor": "US-DOJ",
                "indicator_action_ids": [],
                "red_flag_context": "Auditor failure to verify vendor existence is a common audit deficiency in embezzlement cases. ACFE reports that external audits detect only 4% of occupational fraud."
            }
        ],
        "chain_context": "Forming companies, invoicing for services, processing payments, and conducting audits are all standard business activities. When an executive creates a fictitious vendor to divert organizational funds to themselves, it is embezzlement—a breach of fiduciary duty and criminal theft.",
        "emergent_risk": "Diversion of charitable funds from their intended purpose, undermining donor trust and organizational mission. Median non-profit fraud loss: $100K; schemes lasting 5+ years average $850K (ACFE).",
        "difficulty": "medium",
        "source_references": [
            "ACFE, 'Report to the Nations: Occupational Fraud and Abuse' (2024)",
            "IRS Form 990 governance and conflict-of-interest requirements",
            "DOJ Public Integrity Section: Non-profit fraud prosecutions",
            "AICPA, 'Audit Guide for Not-for-Profit Entities'"
        ],
        "corridors": ["US-DOJ"],
        "palermo_elements": {
            "act": ["exploitation"],
            "means": ["deception", "abuse_of_vulnerability"],
            "purpose": ["embezzlement", "fraud"]
        }
    },
]
