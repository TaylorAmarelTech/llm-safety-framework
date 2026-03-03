"""
Money Laundering Activity Chains

Multi-step activity chains representing the three stages of money laundering
(placement, layering, integration) and modern variants.

Sources:
- FATF 40 Recommendations (2012, updated 2023)
- FinCEN Advisories and Suspicious Activity Report trends
- UNODC World Drug Report money laundering estimates
- US DOJ Money Laundering and Asset Recovery Section (MLARS) case summaries
- EU Anti-Money Laundering Directives (AMLD 4/5/6)
- Wolfsberg Group guidance on correspondent banking
"""

CHAINS: list[dict] = [
    # --- Placement Stage Chains ---
    {
        "id": "money_laundering_001",
        "name": "Cash-Intensive Business Commingling (Structuring + Smurfing)",
        "category": "money_laundering",
        "steps": [
            {
                "id": "ml001_s1",
                "description": "Criminal organization establishes a network of cash-intensive businesses (laundromats, car washes, restaurants) that naturally handle large volumes of currency.",
                "legal_basis": "Owning multiple cash businesses is legal; many legitimate entrepreneurs operate in cash-heavy industries.",
                "sector": "retail",
                "corridor": "MX-US",
                "indicator_action_ids": [],
                "red_flag_context": "Acquiring multiple cash businesses that chronically underperform yet remain open is a classic placement vehicle. FinCEN SAR data shows car washes and restaurants are among the top reported business types."
            },
            {
                "id": "ml001_s2",
                "description": "Illicit cash ($50K-$200K/week) is commingled with legitimate business receipts, inflating reported revenue by 30-50%. Daily deposits include both real and illicit cash.",
                "legal_basis": "Making bank deposits of business receipts is a routine commercial activity.",
                "sector": "retail",
                "corridor": "MX-US",
                "indicator_action_ids": [],
                "red_flag_context": "Revenue significantly exceeding industry norms for the business size/location is a key BSA/AML red flag. Banks are trained to monitor for this via 'expected activity' profiles."
            },
            {
                "id": "ml001_s3",
                "description": "Multiple employees ('smurfs') deposit portions of the excess cash at different bank branches and different banks, keeping individual deposits under $10,000 CTR threshold.",
                "legal_basis": "Having multiple employees make bank deposits is normal for multi-location businesses.",
                "sector": "retail",
                "corridor": "MX-US",
                "indicator_action_ids": [],
                "red_flag_context": "Structuring deposits to avoid CTR filings is a federal crime (31 USC 5324) regardless of whether the underlying funds are legal or illegal."
            },
            {
                "id": "ml001_s4",
                "description": "Once deposited, funds are wire-transferred to accounts in Mexico as 'supplier payments' and 'franchise fees' using fabricated invoices.",
                "legal_basis": "International business payments for goods and services are routine cross-border commerce.",
                "sector": "retail",
                "corridor": "MX-US",
                "indicator_action_ids": [],
                "red_flag_context": "Wire transfers to Mexico documented with fabricated invoices constitute money laundering (18 USC 1956). The Mexico-US corridor is the highest-volume illicit finance route globally."
            }
        ],
        "chain_context": "Each step—owning cash businesses, making deposits, employing multiple banking relationships, paying international suppliers—is individually unremarkable. Combined in this sequence, they represent a classic three-stage laundering operation through cash commingling, structuring, and cross-border wire transfers.",
        "emergent_risk": "Successful integration of drug trafficking proceeds into the legitimate financial system. FinCEN estimates $300B+ in drug money is laundered through the US annually.",
        "difficulty": "hard",
        "source_references": [
            "FinCEN Advisory FIN-2014-A005: Funnel Accounts and Structuring",
            "FATF, 'Money Laundering Through the Physical Transportation of Cash' (2015)",
            "US Treasury, '2024 National Money Laundering Risk Assessment'",
            "DOJ MLARS, 'Black Market Peso Exchange' prosecution summaries"
        ],
        "corridors": ["MX-US", "CO-US"],
        "palermo_elements": {
            "act": ["transfer", "concealment"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["money_laundering", "proceeds_concealment"]
        }
    },
    # --- Layering Stage Chains ---
    {
        "id": "money_laundering_002",
        "name": "Mirror Trading and Correspondent Banking Layering",
        "category": "money_laundering",
        "steps": [
            {
                "id": "ml002_s1",
                "description": "Russian clients deposit rubles with a Moscow brokerage, purchasing shares of a blue-chip stock (e.g., a dual-listed company) in rubles.",
                "legal_basis": "Purchasing securities through a licensed broker is standard market activity.",
                "sector": "financial_services",
                "corridor": "RU-CY",
                "indicator_action_ids": [],
                "red_flag_context": "The buy-side of a mirror trade appears as normal securities trading. The Deutsche Bank mirror trading scandal (2011-2015) involved $10B+ in Russian capital flight."
            },
            {
                "id": "ml002_s2",
                "description": "Simultaneously, a related entity at the same brokerage's London office sells the identical quantity of the same stock for USD or GBP. The buy and sell orders are matched internally.",
                "legal_basis": "Legitimate brokerages handle both buy and sell orders for the same securities across offices globally.",
                "sector": "financial_services",
                "corridor": "RU-UK",
                "indicator_action_ids": [],
                "red_flag_context": "Matched 'mirror' trades that convert currency without an actual foreign exchange transaction are a layering technique. The matching of counterparties is the key red flag."
            },
            {
                "id": "ml002_s3",
                "description": "USD/GBP proceeds from the London sale are wired to bank accounts in Cyprus through correspondent banking channels. Multiple intermediary banks process the wire, adding transaction complexity.",
                "legal_basis": "International wire transfers through correspondent banking networks are the backbone of global finance.",
                "sector": "financial_services",
                "corridor": "UK-CY",
                "indicator_action_ids": [],
                "red_flag_context": "Cyprus's historical role as a conduit for Russian capital is well-documented. Correspondent banks may not see the full picture of the mirror trade scheme."
            },
            {
                "id": "ml002_s4",
                "description": "Funds in Cyprus are used to purchase real estate, yachts, or invested in EU businesses, creating a legitimate-appearing wealth portfolio with an explainable origin story ('investment gains from securities trading').",
                "legal_basis": "Investing in real estate and businesses in the EU is legal for foreign nationals.",
                "sector": "real_estate",
                "corridor": "CY-EU",
                "indicator_action_ids": [],
                "red_flag_context": "Integration of laundered funds through asset purchases completes the laundering cycle. The source-of-funds narrative ('trading profits') is plausible but fabricated."
            }
        ],
        "chain_context": "Securities trading, international wire transfers, correspondent banking, and real estate investment are all pillars of the legitimate global financial system. When orchestrated as matched mirror trades specifically to convert currency and move capital without proper AML scrutiny, they constitute a sophisticated laundering scheme.",
        "emergent_risk": "Large-scale capital flight and money laundering disguised as securities trading. Deutsche Bank was fined $630M for facilitating $10B+ in Russian mirror trades.",
        "difficulty": "expert",
        "source_references": [
            "DFS/FCA/DOJ, Deutsche Bank mirror trading enforcement actions (2017)",
            "FATF, 'Money Laundering and Terrorist Financing Through the Securities Sector' (2009)",
            "Wolfsberg Group, 'Correspondent Banking Due Diligence Questionnaire'",
            "FinCEN Advisory FIN-2017-A003: DPRK-related financial activity"
        ],
        "corridors": ["RU-CY", "RU-UK", "CY-EU"],
        "palermo_elements": {
            "act": ["transfer", "concealment"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["money_laundering", "capital_flight"]
        }
    },
    # --- Trade-Based Money Laundering ---
    {
        "id": "money_laundering_003",
        "name": "Over-Invoicing Trade-Based Money Laundering (TBML)",
        "category": "money_laundering",
        "steps": [
            {
                "id": "ml003_s1",
                "description": "A Colombian exporter ships $100K of textiles to a US importer. The shipment is genuine and contains real goods at actual market value.",
                "legal_basis": "International trade in textiles is a legitimate commercial activity.",
                "sector": "import_export",
                "corridor": "CO-PA",
                "indicator_action_ids": [],
                "red_flag_context": "The legitimate shipment provides the cover for the value transfer. Customs sees real goods crossing the border."
            },
            {
                "id": "ml003_s2",
                "description": "The invoice accompanying the shipment values the goods at $500K—5x the actual value. The US importer pays the inflated $500K to the Colombian exporter's bank account.",
                "legal_basis": "Pricing in international trade can vary; commodity price verification is limited at most customs offices.",
                "sector": "import_export",
                "corridor": "CO-US",
                "indicator_action_ids": [],
                "red_flag_context": "The $400K difference between actual and invoiced value is the laundered amount. FATF identifies over-invoicing as the most common TBML technique."
            },
            {
                "id": "ml003_s3",
                "description": "The Colombian exporter retains the $400K 'excess' payment and delivers it to the narcotics organization, minus a 5-8% commission. The drug money has been effectively repatriated from the US to Colombia through a seemingly legitimate trade payment.",
                "legal_basis": "Receiving payment for exported goods is normal business; the exporter may not be aware of (or choose to ignore) the true nature of the funds.",
                "sector": "import_export",
                "corridor": "CO-PA",
                "indicator_action_ids": [],
                "red_flag_context": "This completes the value transfer: drug money in the US → trade payment → cash in Colombia. The Black Market Peso Exchange (BMPE) variant of this technique launders an estimated $5-10B annually."
            }
        ],
        "chain_context": "International trade, invoicing, and cross-border payments are the foundation of global commerce. When the invoicing is deliberately manipulated to transfer value unrelated to the goods, the trade transaction becomes a money laundering vehicle. TBML is considered the largest and most difficult-to-detect laundering methodology.",
        "emergent_risk": "Trade-based money laundering accounts for an estimated $2 trillion annually globally (GFI). It exploits the massive volume of legitimate trade to hide comparatively small illicit flows.",
        "difficulty": "expert",
        "source_references": [
            "FATF, 'Trade-Based Money Laundering' (2006, updated 2020)",
            "FinCEN Advisory FIN-2019-A002: TBML through trade in goods",
            "Global Financial Integrity, 'Illicit Financial Flows' annual reports",
            "US GAO, 'Anti-Money Laundering: Opportunities Exist to Increase Law Enforcement Use of Bank Secrecy Act Reports' (2020)"
        ],
        "corridors": ["CO-US", "CO-PA", "MX-US"],
        "palermo_elements": {
            "act": ["transfer", "concealment"],
            "means": ["deception"],
            "purpose": ["money_laundering", "drug_proceeds_repatriation"]
        }
    },
    # --- Crypto Laundering ---
    {
        "id": "money_laundering_004",
        "name": "Ransomware Proceeds Laundering via DeFi and Mixers",
        "category": "money_laundering",
        "steps": [
            {
                "id": "ml004_s1",
                "description": "Ransomware operator receives 50 BTC ($2.5M) in ransom payments to a fresh wallet. Payments come from multiple victims' cryptocurrency exchanges and OTC desks.",
                "legal_basis": "Receiving Bitcoin to a wallet address is a peer-to-peer transaction; the blockchain is public and permissionless.",
                "sector": "cryptocurrency",
                "corridor": "GLOBAL",
                "indicator_action_ids": [],
                "red_flag_context": "Ransomware wallets are quickly identified and flagged by blockchain analytics firms (Chainalysis, Elliptic). OFAC may sanction associated addresses."
            },
            {
                "id": "ml004_s2",
                "description": "BTC is sent through a mixing/tumbling service (or CoinJoin protocol) that pools funds from many users and redistributes them to new addresses, breaking the direct blockchain link.",
                "legal_basis": "Cryptocurrency mixing services exist as privacy tools; their use is not universally illegal (though the operator may face charges).",
                "sector": "cryptocurrency",
                "corridor": "GLOBAL",
                "indicator_action_ids": [],
                "red_flag_context": "OFAC sanctioned Tornado Cash (2022) and Blender.io (2022) specifically because they were used to launder ransomware and stolen cryptocurrency proceeds."
            },
            {
                "id": "ml004_s3",
                "description": "Post-mixing BTC is bridged to the Ethereum chain via a cross-chain bridge, swapped for stablecoins on a DEX, then deposited into a yield farming protocol. Multiple DeFi hops create transaction complexity.",
                "legal_basis": "Using DeFi protocols for yield farming and cross-chain bridging is a legitimate cryptocurrency activity.",
                "sector": "cryptocurrency",
                "corridor": "GLOBAL",
                "indicator_action_ids": [],
                "red_flag_context": "Each DeFi hop adds a layer of obfuscation. Cross-chain bridges are particularly effective at breaking analytics because different blockchains have independent ledgers."
            },
            {
                "id": "ml004_s4",
                "description": "Stablecoins are withdrawn from DeFi and sold for fiat currency through a nested exchange (a smaller exchange that uses a larger exchange's banking infrastructure) in a jurisdiction with weak AML enforcement.",
                "legal_basis": "Selling cryptocurrency for fiat on an exchange is standard; nested exchange arrangements exist throughout the industry.",
                "sector": "cryptocurrency",
                "corridor": "GLOBAL",
                "indicator_action_ids": [],
                "red_flag_context": "Nested exchanges often inherit the compliance reputation of their banking partner while conducting inadequate KYC themselves. FinCEN has identified nested exchange abuse as a priority concern."
            }
        ],
        "chain_context": "Cryptocurrency wallets, mixing services, DeFi protocols, and exchanges are all components of the crypto ecosystem used by millions of legitimate users. When sequenced to convert ransomware proceeds from traceable BTC to untraceable fiat, they constitute a modern money laundering pipeline.",
        "emergent_risk": "Conversion of ransomware proceeds to clean fiat currency, funding further cybercrime operations. Chainalysis reports $1.1B in ransomware payments in 2023.",
        "difficulty": "expert",
        "source_references": [
            "OFAC, Tornado Cash sanctions designation (August 2022)",
            "FinCEN, 'Advisory on Ransomware and the Use of the Financial System' (2021)",
            "Chainalysis, '2024 Crypto Crime Report'",
            "FATF, 'Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs' (2021)"
        ],
        "corridors": ["GLOBAL", "RU-AE", "KP-GLOBAL"],
        "palermo_elements": {
            "act": ["transfer", "concealment"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["money_laundering", "cybercrime_proceeds"]
        }
    },
    # --- Real Estate Laundering ---
    {
        "id": "money_laundering_005",
        "name": "All-Cash Luxury Real Estate Laundering with Anonymous LLCs",
        "category": "money_laundering",
        "steps": [
            {
                "id": "ml005_s1",
                "description": "Foreign PEP (Politically Exposed Person) establishes a chain of anonymous shell companies: a BVI IBC owns a Panamanian holding company, which owns a Delaware LLC.",
                "legal_basis": "Multi-jurisdictional holding structures are used by legitimate businesses and high-net-worth individuals globally.",
                "sector": "real_estate",
                "corridor": "NG-UK",
                "indicator_action_ids": [],
                "red_flag_context": "This entity chain is designed specifically to prevent anyone from connecting the property to the PEP. The Corporate Transparency Act now requires UBO disclosure but enforcement is evolving."
            },
            {
                "id": "ml005_s2",
                "description": "The Delaware LLC purchases a $15M luxury condominium in Manhattan with an all-cash payment. No mortgage means no lender conducting source-of-funds verification.",
                "legal_basis": "All-cash real estate purchases are legal and common in luxury markets; no law requires a mortgage.",
                "sector": "real_estate",
                "corridor": "NG-US",
                "indicator_action_ids": [],
                "red_flag_context": "FinCEN Geographic Targeting Orders (GTOs) now cover all-cash purchases over $300K by legal entities in major US metro areas, but enforcement gaps remain."
            },
            {
                "id": "ml005_s3",
                "description": "The property is held for 2-3 years, appreciating in value. It may be rented to generate 'legitimate' income, further integrating the laundered funds into the legal economy.",
                "legal_basis": "Owning and renting investment property is a standard wealth management strategy.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "The holding period creates distance between the illicit source of funds and the eventual sale. Rental income creates a legitimate revenue stream."
            },
            {
                "id": "ml005_s4",
                "description": "Property is sold for $18M. The sale proceeds are deposited into the LLC's US bank account as 'real estate capital gains'—now fully documented, tax-reported, and virtually untraceable to the original corrupt funds.",
                "legal_basis": "Selling property and depositing sale proceeds is a normal financial transaction; capital gains are reported on tax returns.",
                "sector": "real_estate",
                "corridor": "US-DOMESTIC",
                "indicator_action_ids": [],
                "red_flag_context": "The money has been fully laundered: corrupt funds → anonymous entity → all-cash property → sale proceeds. The wealth narrative is now 'real estate investment returns.'"
            }
        ],
        "chain_context": "Shell companies, all-cash property purchases, rental income, and property sales are all standard elements of real estate investment. When used by PEPs to convert corruption proceeds into seemingly legitimate real estate gains, they represent a textbook laundering cycle that FinCEN GTOs and the CTA are designed to disrupt.",
        "emergent_risk": "Laundered corruption proceeds integrated into the US financial system as legitimate real estate gains. NAR estimates $2.3B in laundered funds entered US real estate annually (pre-GTO).",
        "difficulty": "hard",
        "source_references": [
            "FinCEN Geographic Targeting Orders (GTOs): Real Estate, multiple renewals since 2016",
            "Global Financial Integrity, 'Acres of Money Laundering' (2021)",
            "Transparency International, 'Doors Wide Open: Corruption and Real Estate in Four Key Markets' (2017)",
            "FATF, 'Money Laundering and Terrorist Financing Vulnerabilities of Legal Professionals' (2013)"
        ],
        "corridors": ["NG-US", "RU-UK", "CN-CA", "VE-US"],
        "palermo_elements": {
            "act": ["transfer", "concealment"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["money_laundering", "corruption_proceeds"]
        }
    },
    # --- Hawala / Informal Value Transfer ---
    {
        "id": "money_laundering_006",
        "name": "Hawala Network Cross-Border Value Transfer",
        "category": "money_laundering",
        "steps": [
            {
                "id": "ml006_s1",
                "description": "Client delivers $500K cash to a hawaladar (informal money broker) in New York, receiving a code word as a receipt. No bank accounts, no wire transfers, no paper trail.",
                "legal_basis": "Money Service Businesses are legal if registered with FinCEN; hawala is a traditional remittance system used by millions for legitimate purposes.",
                "sector": "financial_services",
                "corridor": "AF-AE",
                "indicator_action_ids": [],
                "red_flag_context": "Unregistered hawala operations violate 18 USC 1960. Even registered MSBs must file CTRs and SARs. The absence of records is the defining feature."
            },
            {
                "id": "ml006_s2",
                "description": "The New York hawaladar contacts a counterpart in Dubai via encrypted messaging. No funds physically cross any border. The Dubai hawaladar releases the equivalent amount (minus commission) to the designated recipient from their own local cash pool.",
                "legal_basis": "Informal value transfer systems have operated for centuries across South Asia and the Middle East for legitimate remittances.",
                "sector": "financial_services",
                "corridor": "US-AE",
                "indicator_action_ids": [],
                "red_flag_context": "The value transfer occurs without any funds crossing a border, evading all customs, banking, and AML controls. FATF specifically identifies hawala as a typology for ML/TF."
            },
            {
                "id": "ml006_s3",
                "description": "The two hawaladars settle their accounts periodically through trade invoicing—the New York broker orders goods from the Dubai broker's import/export business at inflated prices, effectively transferring the debt through commercial channels.",
                "legal_basis": "Import/export businesses regularly settle accounts through trade; pricing can vary based on market conditions.",
                "sector": "import_export",
                "corridor": "US-AE",
                "indicator_action_ids": [],
                "red_flag_context": "The settlement layer combines hawala with trade-based laundering, creating a nearly impossible-to-detect value transfer system."
            }
        ],
        "chain_context": "Money service businesses, encrypted communications, and international trade are all legitimate. When combined in a hawala network that operates outside the regulated financial system, they create an untraceable value transfer mechanism used for both legitimate remittances and illicit finance.",
        "emergent_risk": "Unregulated cross-border value transfer that evades all AML controls. The Afghanistan-UAE hawala corridor alone moves an estimated $4-5B annually.",
        "difficulty": "hard",
        "source_references": [
            "FATF, 'The Role of Hawala and Other Similar Service Providers in Money Laundering and Terrorist Financing' (2013)",
            "FinCEN Advisory FIN-2003-A003: Informal Value Transfer Systems",
            "UNODC, 'Afghanistan Opium Survey' (annual): Hawala estimates",
            "9/11 Commission Report: Chapter on terrorist financing through hawala"
        ],
        "corridors": ["AF-AE", "PK-UK", "IN-US", "SO-KE"],
        "palermo_elements": {
            "act": ["transfer"],
            "means": ["deception", "abuse_of_process"],
            "purpose": ["money_laundering", "value_transfer"]
        }
    },
]
