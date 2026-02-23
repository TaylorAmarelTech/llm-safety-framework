"""
Multi-country transit chains — 3+ country trafficking routes where exploitation
occurs across multiple jurisdictions, creating enforcement gaps and compounding
vulnerability at each border crossing.

Sources:
  IOM, "World Migration Report 2024" — transit country exploitation patterns
  UNODC, "Global Report on Trafficking in Persons 2022" — multi-jurisdictional
      trafficking route analysis and prosecution challenges
  IOM Missing Migrants Project, "Mediterranean Crossings 2014-2024" — fatality
      and transit data for North/West African routes
  UNODC, "Measuring Responses to Trafficking in Persons in the Criminal Justice
      System: A Comprehensive Assessment" (2023)
  Polaris Project, "Labor Trafficking in the US: A Closer Look at Temporary
      Work Visas" (2022) — H-2A/H-2B exploitation documentation
  US DOJ, "Operation Blooming Onion" (Nov 2021, S.D. Georgia) — 24 defendants
      indicted for forced labor of H-2A agricultural workers from Guatemala,
      Honduras, and Mexico
  EJF, "Blood and Water: Human Rights Abuse in the Global Seafood Industry"
      (2019) — vessel-to-vessel transfers in Thai and Vietnamese fleets
  Greenpeace, "Turn the Tide: Human Rights Abuses and Illegal Fishing in
      Thailand's Overseas Fishing Industry" (2016)
  IOM, "Flow Monitoring: Mixed Migration Routes from the Horn of Africa to
      Yemen and Saudi Arabia" (2023) — Gulf of Aden crossing data
  Mixed Migration Centre (MMC), "4Mi Quarterly Reports: East Africa & Yemen"
      (2022-2024) — Ethiopian migrant transit surveys
  UNHCR, "Gulf of Aden Maritime Crossings: Arrivals and Fatalities" (2023)
  Migrasia, "Mapping Labour Migration in ASEAN" (2022) — Southeast Asian
      transit exploitation patterns
  Issara Institute, "Fisheries Labour Risk Assessment: Myanmar-Thailand
      Cross-Border Supply Chains" (2020)
  ILO, "Ship to Shore Rights: Baseline Research Findings on Fishers and
      Seafood Workers in Thailand" (2018)
  Verité, "Recruitment Practices and Migrant Labor Conditions in Nestlé's
      Thai Shrimp Supply Chain" (2015)
  KNOMAD/World Bank, "Migration and Development Brief 38" (2023) — bilateral
      corridor cost data
  HRW, "Exported and Exposed: Abuses against Sri Lankan Domestic Workers in
      Saudi Arabia, Kuwait, Lebanon, and the United Arab Emirates" (2007)
  Palermo Protocol Art. 3 — Trafficking in Persons definition
  ILO C029 — Forced Labour Convention (1930)
  ILO C188 — Work in Fishing Convention (2007)
  US Trafficking Victims Protection Act (TVPA) § 1589-1592
"""

CHAINS: list[dict] = [
    {
        "id": "multi_country_transit_001",
        "name": "Myanmar-Thailand-Malaysia-Singapore Manufacturing Pipeline",
        "category": "multi_country_transit",
        "steps": [
            {
                "id": "mt001_s1",
                "description": (
                    "Displaced persons fleeing conflict in Kayin (Karen) State and "
                    "Shan State cross into Thailand at the Mae Sot-Myawaddy border "
                    "crossing in Tak Province, where Thai-based brokers (nai naa) "
                    "operating from guesthouses on the Thai side of the Moei River "
                    "arrange passage for THB 5,000-15,000 ($140-$420). The brokers "
                    "present themselves as employment agents offering factory work "
                    "in Thailand's garment or electronics sector, showing photos of "
                    "clean dormitories and cafeterias. Mae Sot is Thailand's largest "
                    "informal border crossing point, with an estimated 200,000 "
                    "undocumented Myanmar migrants in the surrounding area as of 2023."
                ),
                "legal_basis": (
                    "Thailand's Royal Ordinance on Managing the Work of Aliens B.E. "
                    "2560 (2017) permits temporary border passes under bilateral MOU "
                    "frameworks for Myanmar nationals in border economic zones. The "
                    "Mae Sot Special Economic Zone (established 2015) was designed "
                    "to formalize cross-border labor flows."
                ),
                "sector": "manufacturing",
                "corridor": "MM-TH",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Workers fleeing active conflict have no bargaining power and "
                    "cannot return; the broker's fee creates immediate debt before "
                    "any employment begins. Migrasia's 2022 ASEAN mapping documented "
                    "that 73% of Myanmar workers crossing at Mae Sot paid brokers "
                    "rather than using the formal MOU channel, which requires "
                    "documentation most displaced persons cannot obtain."
                ),
            },
            {
                "id": "mt001_s2",
                "description": (
                    "Workers are placed in garment factories in the Mae Sot SEZ or "
                    "in food-processing plants in Samut Sakhon province, earning "
                    "THB 250-300/day ($7-$8.40) against Thailand's minimum wage of "
                    "THB 328-354/day. The broker retains workers' Myanmar identity "
                    "documents and any temporary border passes, stating they are "
                    "'kept safe with the employer.' Workers are told they must work "
                    "3-6 months to 'repay transit costs' before receiving full wages. "
                    "Deductions for dormitory housing (THB 1,500/month) and meals "
                    "(THB 2,000/month) reduce net pay to THB 2,000-3,000/month ($56-$84)."
                ),
                "legal_basis": (
                    "Thai Labor Protection Act B.E. 2541 (1998) applies to all "
                    "workers regardless of nationality or documentation status, "
                    "including minimum wage protections. The Mae Sot SEZ labor "
                    "provisions under Section 44 NCPO Order 21/2560 set a reduced "
                    "minimum wage for border economic zones."
                ),
                "sector": "manufacturing",
                "corridor": "MM-TH",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Document retention violates Thai Labor Protection Act and "
                    "constitutes an ILO forced labor indicator. The 3-6 month "
                    "'repayment' period is debt bondage — the original crossing fee "
                    "was THB 5,000-15,000 but deductions ensure the debt never "
                    "fully clears. Issara Institute's 2020 assessment found 68% of "
                    "Myanmar workers in Thai border factories experienced at least "
                    "3 of 11 ILO forced labor indicators."
                ),
            },
            {
                "id": "mt001_s3",
                "description": (
                    "After 3-6 months, a Malaysian broker connected to the Thai "
                    "operation offers 'better-paying work' in Penang or Johor Bahru "
                    "electronics factories at RM 1,500-2,000/month ($320-$430). "
                    "Workers are transported by van from Samut Sakhon to the "
                    "Padang Besar border crossing in Songkhla Province, then across "
                    "into Perlis, Malaysia. The Malaysian broker charges RM 3,000-"
                    "5,000 ($640-$1,070) for the crossing arrangement, payable "
                    "through salary deductions over 6 months. Workers' Thai-issued "
                    "temporary documents (if any) become void upon leaving Thailand, "
                    "making them undocumented in Malaysia."
                ),
                "legal_basis": (
                    "Malaysia's Immigration Act 1959/63 (Act 155) Section 6 requires "
                    "valid travel documents for entry; the Malaysia-Thailand border "
                    "at Padang Besar is a legal crossing with immigration controls. "
                    "Malaysia's Employment Act 1955 applies to documented workers "
                    "but enforcement is limited for undocumented foreign nationals."
                ),
                "sector": "electronics_manufacturing",
                "corridor": "TH-MY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The second border crossing strips whatever marginal legal "
                    "status the worker had in Thailand. The new debt of RM 3,000-"
                    "5,000 stacks on top of any unresolved Thai debt. IOM's 2024 "
                    "World Migration Report documented that re-trafficking across "
                    "ASEAN borders is a systematic pattern: workers who have already "
                    "been exploited in one country are specifically targeted by "
                    "brokers for onward movement because their undocumented status "
                    "and existing debt make them more compliant."
                ),
            },
            {
                "id": "mt001_s4",
                "description": (
                    "In Malaysian electronics factories in the Bayan Lepas Free "
                    "Industrial Zone (Penang) or Pasir Gudang industrial district "
                    "(Johor), workers' Myanmar passports — if they had any — are "
                    "confiscated by the factory's HR department, which states that "
                    "'company policy requires document safekeeping for foreign "
                    "workers.' Workers earn RM 1,200-1,500/month ($257-$320), below "
                    "the promised RM 1,500-2,000, with RM 400/month deducted for "
                    "hostel and RM 300/month for 'levy reimbursement.' Net monthly "
                    "pay is RM 500-800 ($107-$171). Workers who perform well are "
                    "told they can be 'promoted' to Singapore operations."
                ),
                "legal_basis": (
                    "Malaysia's Employment Act 1955 Section 24 prohibits unauthorized "
                    "wage deductions; the Passport Act 1966 Section 12 makes it an "
                    "offense to retain another person's passport. The Anti-Trafficking "
                    "in Persons and Anti-Smuggling of Migrants Act 2007 (ATIPSOM, "
                    "amended 2015) criminalizes document confiscation as a trafficking "
                    "indicator."
                ),
                "sector": "electronics_manufacturing",
                "corridor": "TH-MY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Document confiscation in Malaysia replicates the pattern from "
                    "Thailand, now with zero recourse — the worker has no valid "
                    "documents for any country. The 'promotion to Singapore' offer "
                    "is the setup for a fourth-country transfer. Verité's forced "
                    "labor surveys documented that Malaysian electronics factories "
                    "supplying major brands retained passports of 28% of foreign "
                    "workers despite ATIPSOM prohibitions."
                ),
            },
            {
                "id": "mt001_s5",
                "description": (
                    "Top-performing workers are given fraudulent Singapore work "
                    "permits or S-passes obtained through a corrupt Singapore-based "
                    "employment agency. Workers are transported across the Johor-"
                    "Singapore Causeway to semiconductor or precision engineering "
                    "factories in Tuas or Jurong industrial estates. The Singapore "
                    "agent charges SGD 8,000-12,000 ($5,900-$8,900) for document "
                    "procurement and placement, creating a third layer of debt. "
                    "Workers now carry fraudulent Singapore documents, void Malaysian "
                    "documentation, and are four countries removed from their "
                    "Myanmar origin with cumulative debts of $7,000-$10,500."
                ),
                "legal_basis": (
                    "Singapore's Employment of Foreign Manpower Act (EFMA) Chapter "
                    "91A requires valid work passes; fraudulent pass procurement "
                    "is punishable under EFMA Section 22(1)(d) with fines up to "
                    "SGD 20,000 and imprisonment up to 2 years. Singapore's "
                    "Prevention of Human Trafficking Act 2014 specifically "
                    "criminalizes debt bondage under Section 3."
                ),
                "sector": "semiconductor_manufacturing",
                "corridor": "MY-SG",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The worker is now in their fourth country with fraudulent "
                    "documents, cumulative debt from three separate brokers across "
                    "three borders, and no legal standing in any jurisdiction. If "
                    "detected by Singapore authorities, they face prosecution for "
                    "document fraud before any trafficking identification. UNODC's "
                    "2022 Global Report documented that multi-country transit victims "
                    "are identified as trafficking victims in fewer than 8% of cases "
                    "because immigration violations are detected first."
                ),
            },
        ],
        "chain_context": (
            "This four-country pipeline exploits the ASEAN region's patchwork of "
            "bilateral labor MOUs, inconsistent document recognition, and uncoordinated "
            "enforcement. Each border crossing strips the worker of whatever legal "
            "status they had in the previous country, while adding a new layer of debt "
            "to a new broker. Thailand's 2017 anti-trafficking law, Malaysia's ATIPSOM "
            "2007, and Singapore's PHTA 2014 each criminalize trafficking within their "
            "borders but lack mechanisms for cross-border victim identification. The "
            "Bali Process on People Smuggling and Trafficking (established 2002) created "
            "a regional framework but has produced no binding enforcement cooperation. "
            "Workers who enter this pipeline in Mae Sot and exit in Singapore have "
            "accumulated $7,000-$10,500 in debt across three broker networks in three "
            "countries, with no single jurisdiction able to see the full chain."
        ),
        "emergent_risk": (
            "Cascading jurisdictional invisibility: each border crossing resets the "
            "worker's legal identity and adds compounding debt, creating a four-country "
            "trafficking chain that no single national authority can detect or prosecute."
        ),
        "difficulty": "expert",
        "source_references": [
            "Migrasia, 'Mapping Labour Migration in ASEAN' (2022) — Mae Sot crossing data and broker fee documentation",
            "Issara Institute, 'Fisheries Labour Risk Assessment: Myanmar-Thailand Cross-Border Supply Chains' (2020) — forced labor indicator prevalence in Thai border factories",
            "IOM, 'World Migration Report 2024' — ASEAN re-trafficking patterns and multi-country transit documentation",
            "UNODC, 'Global Report on Trafficking in Persons 2022' — multi-jurisdictional prosecution gap analysis",
            "Verité, 'Forced Labor in the Production of Electronic Goods in Malaysia' (2014) — passport retention and debt bondage in Malaysian electronics",
            "Singapore Ministry of Manpower, 'Prevention of Human Trafficking Act Review' (2023) — fraudulent work pass prosecution data",
        ],
        "corridors": ["MM-TH", "TH-MY", "MY-SG"],
        "palermo_elements": {
            "act": ["recruitment", "transportation", "transfer", "harbouring"],
            "means": [
                "abuse of position of vulnerability",
                "deception",
                "abuse of power",
                "debt bondage",
            ],
            "purpose": ["forced labour", "exploitation", "servitude"],
        },
    },
    {
        "id": "multi_country_transit_002",
        "name": "Nigeria-Libya-Italy Sex Trafficking Route",
        "category": "multi_country_transit",
        "steps": [
            {
                "id": "mt002_s1",
                "description": (
                    "Recruiters operating in Lagos (Ikeja, Festac Town) and Benin "
                    "City (Edo State) approach young women aged 17-25 with promises "
                    "of employment in hair salons, restaurants, or domestic work in "
                    "Italy, offering monthly earnings of EUR 1,500-2,500. Before "
                    "departure, victims undergo a 'juju' (traditional oath) ceremony "
                    "at a shrine, typically involving blood, pubic hair, fingernails, "
                    "and underwear, binding them to repay a debt of EUR 30,000-60,000 "
                    "to the 'madam' (female trafficker) who arranges the journey. "
                    "NAPTIP (National Agency for the Prohibition of Trafficking in "
                    "Persons) documented 1,871 victims from Edo State alone between "
                    "2019 and 2022."
                ),
                "legal_basis": (
                    "Nigeria's Trafficking in Persons (Prohibition) Enforcement and "
                    "Administration Act 2015 (NAPTIP Act) criminalizes recruitment "
                    "for exploitation. However, Edo State — which accounts for over "
                    "90% of Nigerian sex trafficking to Italy — has limited law "
                    "enforcement capacity, and juju oaths are not recognized as "
                    "coercive instruments under Nigerian statutory law."
                ),
                "sector": "commercial_sexual_exploitation",
                "corridor": "NG-LY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The juju oath creates a psychological coercion mechanism that "
                    "operates outside formal legal frameworks — victims believe "
                    "breaking the oath will cause death, madness, or harm to their "
                    "families. UNODC's 2018 report on Nigeria-Italy trafficking "
                    "documented that 95% of identified victims had undergone juju "
                    "ceremonies, and 78% cited the oath as the primary reason they "
                    "did not attempt to escape even when physically able to do so."
                ),
            },
            {
                "id": "mt002_s2",
                "description": (
                    "Victims travel overland from Lagos or Benin City through Niger "
                    "(Agadez serves as the primary transit hub) to Libya, a journey "
                    "of 2,000-3,000 km taking 2-6 weeks. Transport is arranged by "
                    "a network of drivers and 'connection men' who move groups of "
                    "15-30 migrants in Toyota Hilux pickups across the Sahara. "
                    "The route passes through Agadez, then to the Dirkou oasis in "
                    "northeastern Niger, and across the Libyan border at the "
                    "Salvador Pass or Tummo crossing. Transit costs of $500-1,500 "
                    "per person are added to the victim's debt. IOM Missing Migrants "
                    "Project recorded 5,600 deaths on Saharan routes between 2014 "
                    "and 2023."
                ),
                "legal_basis": (
                    "Niger's Law 2015-36 on Migrant Smuggling criminalizes irregular "
                    "border crossing facilitation, but enforcement in the Agadez "
                    "region — where the migration economy employs an estimated 6,000 "
                    "people — is limited. The EU-funded EUCAP Sahel Niger mission "
                    "has focused on disrupting smuggling networks since 2016."
                ),
                "sector": "transit_smuggling",
                "corridor": "NG-LY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The Saharan transit is where smuggling transitions to trafficking "
                    "for many victims. Women who cannot pay escalating transit fees "
                    "are sold to Libyan criminal networks or forced into sexual "
                    "exploitation at transit stops. The MMC 4Mi surveys documented "
                    "that 43% of women on the Nigeria-Libya route experienced sexual "
                    "violence during transit, and 67% reported their debt increased "
                    "by $1,000-3,000 due to 'unexpected costs' demanded by intermediaries."
                ),
            },
            {
                "id": "mt002_s3",
                "description": (
                    "In Libya, victims are held in 'connection houses' or detention "
                    "facilities in Sabratah, Bani Walid, or Tripoli for weeks to "
                    "months while awaiting Mediterranean passage. Libyan armed groups "
                    "and criminal networks controlling these facilities subject "
                    "detainees to extortion, forced labor, and sexual violence. "
                    "Ransom demands of $1,000-5,000 are transmitted to families in "
                    "Nigeria via phone calls, with victims beaten during the calls "
                    "to compel payment. The UN Panel of Experts on Libya (2022) "
                    "documented systematic rape and forced labor in facilities in "
                    "Zawiya and Sabratah controlled by militias including the "
                    "Anas al-Dabbashi network."
                ),
                "legal_basis": (
                    "Libya has no functioning asylum system or anti-trafficking "
                    "legislation. The Government of National Unity (GNU) operates "
                    "official detention centers under the Department for Combating "
                    "Illegal Migration (DCIM), but militia-controlled facilities "
                    "operate outside any legal framework. UNHCR has recorded "
                    "43,000 refugees and asylum seekers in Libya as of 2023."
                ),
                "sector": "detention_exploitation",
                "corridor": "NG-LY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Libya serves as both a transit country and a site of active "
                    "trafficking exploitation. The absence of rule of law means "
                    "victims have zero access to protection. CNN's 2017 investigation "
                    "documented slave auctions in Tripoli where migrants were sold "
                    "for $200-500. IOM Libya recorded 7,453 migrants in official "
                    "detention and an estimated 5,000+ in unofficial facilities in "
                    "2023, with systematic abuse documented across both categories."
                ),
            },
            {
                "id": "mt002_s4",
                "description": (
                    "Victims are placed on inflatable dinghies or wooden boats at "
                    "Sabratah, Zuwara, or Garabulli for the 275-300 km Central "
                    "Mediterranean crossing to Lampedusa, Italy, or are intercepted "
                    "by the Libyan Coast Guard and NGO vessels. Boats carry 100-150 "
                    "people with minimal fuel, no navigation equipment, and no life "
                    "jackets. Passage costs $800-2,000 per person, added to the "
                    "cumulative debt. IOM Missing Migrants Project recorded 28,081 "
                    "deaths and disappearances in the Central Mediterranean between "
                    "2014 and 2024. Upon arrival in Italy (typically at Lampedusa "
                    "hotspot or Sicilian ports), victims are processed through the "
                    "reception system but contacted within days by the madam's "
                    "Italian network."
                ),
                "legal_basis": (
                    "Italy's Legislative Decree 286/1998 (Testo Unico "
                    "sull'Immigrazione) provides for reception of arriving migrants; "
                    "EU Regulation 604/2013 (Dublin III) assigns asylum processing "
                    "to the country of first entry. Italy's Art. 18 of the "
                    "Immigration Act provides residence permits for trafficking "
                    "victims who cooperate with authorities, but identification "
                    "requires self-reporting or proactive screening."
                ),
                "sector": "commercial_sexual_exploitation",
                "corridor": "LY-IT",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Arrival in Italy triggers the exploitation phase. The madam's "
                    "network meets victims at reception centers or shortly after "
                    "they leave. The EUR 30,000-60,000 juju-bound debt — now "
                    "augmented by $2,300-8,500 in transit costs — is enforced "
                    "through street prostitution in Castel Volturno (Campania), "
                    "Turin, Palermo, or Catania. UNODC's 2022 report documented "
                    "that Nigerian trafficking networks in Italy generated an "
                    "estimated EUR 600 million annually, with victims forced to "
                    "earn EUR 200-500 per night to service their debts over 2-5 years."
                ),
            },
        ],
        "chain_context": (
            "The Nigeria-Libya-Italy route is one of the most documented and lethal "
            "trafficking pipelines in the world. It spans three countries with "
            "fundamentally different legal systems: Nigeria (common law with NAPTIP "
            "framework), Libya (failed state with no functioning trafficking law), and "
            "Italy (EU member state with Art. 18 protections). The juju oath operates "
            "as a non-legal coercion mechanism that persists across all three jurisdictions "
            "and is not recognized by any of them as a trafficking instrument. Each "
            "transit stage adds debt and strips agency: the Saharan crossing adds $500-"
            "1,500, Libyan detention adds $1,000-5,000 in ransom, and the Mediterranean "
            "passage adds $800-2,000 — transforming an initial EUR 30,000-60,000 oath-"
            "bound debt into a cumulative obligation that takes 3-7 years of forced "
            "prostitution to discharge."
        ),
        "emergent_risk": (
            "Layered coercion across three legal systems: juju oath (psychological, "
            "origin country), physical captivity (Libya, no legal framework), and debt "
            "enforcement (Italy, formal economy) create a trafficking chain that no "
            "single country's anti-trafficking mechanisms can fully address."
        ),
        "difficulty": "expert",
        "source_references": [
            "UNODC, 'Global Report on Trafficking in Persons 2022' — Nigeria-Italy route analysis and EUR 600M annual revenue estimate",
            "IOM Missing Migrants Project, 'Mediterranean Crossings 2014-2024' — 28,081 recorded deaths in Central Mediterranean",
            "UNODC, 'Trafficking in Persons from Nigeria to Europe' (2018) — juju oath prevalence and Edo State recruitment patterns",
            "UN Panel of Experts on Libya, 'Final Report S/2022/427' (2022) — militia-controlled detention facility documentation",
            "Mixed Migration Centre, '4Mi Quarterly Reports: West Africa & Central Mediterranean' (2022-2024) — transit violence and debt escalation surveys",
            "CNN, 'People for Sale: Where Lives Are Auctioned for $400' (Nov 2017) — Tripoli slave auction investigation",
        ],
        "corridors": ["NG-LY", "LY-IT"],
        "palermo_elements": {
            "act": ["recruitment", "transportation", "transfer", "harbouring"],
            "means": [
                "coercion",
                "deception",
                "abuse of position of vulnerability",
                "giving payments to a person having control over another",
            ],
            "purpose": [
                "sexual exploitation",
                "forced labour",
                "slavery or practices similar to slavery",
            ],
        },
    },
    {
        "id": "multi_country_transit_003",
        "name": "Philippines-Qatar-Saudi Domestic Worker Re-Trafficking",
        "category": "multi_country_transit",
        "steps": [
            {
                "id": "mt003_s1",
                "description": (
                    "A licensed recruitment agency in Quezon City, Metro Manila "
                    "deploys a Filipina domestic worker to a Qatari household in "
                    "Doha under a standard two-year POEA/DMW contract at QAR 1,500/"
                    "month ($412). The worker departs NAIA Terminal 1 with a valid "
                    "Qatar work visa (iqama), OFW exit clearance from the DMW, and "
                    "OWWA membership. The Philippine Overseas Labor Office (POLO) in "
                    "Doha is listed as the worker's point of contact for grievances. "
                    "Initial placement appears fully compliant with both Philippine "
                    "RA 10022 and Qatar Law No. 15/2017 on domestic workers."
                ),
                "legal_basis": (
                    "Philippines RA 10022 (2010) governs deployment of OFWs through "
                    "licensed agencies with POEA/DMW standard contracts; Qatar Law "
                    "No. 15/2017 on Domestic Workers establishes minimum contract "
                    "terms including working hours, rest days, and end-of-service "
                    "benefits. The bilateral PH-QA labor agreement (2008, updated "
                    "2017) provides for joint monitoring."
                ),
                "sector": "domestic_work",
                "corridor": "PH-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The initial deployment is fully legal and documented — this is "
                    "what makes the subsequent re-trafficking invisible. The worker "
                    "has a valid Qatar iqama, POLO access, and contractual protections. "
                    "However, the kafala system ties her legal status entirely to this "
                    "specific Qatari employer (kafeel), creating the vulnerability that "
                    "the next step exploits."
                ),
            },
            {
                "id": "mt003_s2",
                "description": (
                    "After 8 months, the Qatari employer informs the worker she will "
                    "be 'transferred' to his brother's household in Riyadh, Saudi "
                    "Arabia for a 'temporary assignment' of 3-6 months, after which "
                    "she will return to Doha. The employer purchases her a plane ticket "
                    "from Doha (Hamad International) to Riyadh (King Khalid "
                    "International), gives her a tourist/visit visa for Saudi Arabia "
                    "arranged through the brother, and retains her Qatar iqama 'for "
                    "safekeeping until she returns.' The worker arrives in Riyadh with "
                    "a Saudi visit visa valid for 90 days but no Saudi work permit, "
                    "no Saudi labor contract, and no access to POLO-Riyadh (which "
                    "requires a verified Saudi employment contract to provide services)."
                ),
                "legal_basis": (
                    "Qatar's kafala reform (Law No. 18/2020) permits workers to change "
                    "employers within Qatar but does not address cross-border transfers. "
                    "Saudi Arabia's Labor Law (Royal Decree M/51) requires a separate "
                    "employment visa and contract for domestic workers; visit visas do "
                    "not authorize employment. The transfer is not illegal in Qatar "
                    "(the kafeel can send his employee on a 'personal errand') but "
                    "creates immediate illegality upon Saudi arrival."
                ),
                "sector": "domestic_work",
                "corridor": "QA-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "This step is the critical exploitation pivot. The worker crosses "
                    "from a jurisdiction where she has legal status (Qatar) to one "
                    "where she has none (Saudi Arabia). Her Qatar iqama is retained "
                    "by the Doha employer, her Saudi visit visa will expire in 90 days, "
                    "and she has no Saudi employment contract. HRW documented this "
                    "exact cross-Gulf transfer pattern in 2007 ('Exported and Exposed'), "
                    "finding that Filipino and Sri Lankan domestic workers were "
                    "routinely 'lent' between relatives in Gulf states."
                ),
            },
            {
                "id": "mt003_s3",
                "description": (
                    "In Riyadh, the brother's household confiscates the worker's "
                    "Philippine passport and Saudi visit visa. After the 90-day visit "
                    "visa expires, the worker becomes undocumented in Saudi Arabia. "
                    "The Riyadh household pays no salary, stating that 'your employer "
                    "in Qatar pays you — talk to him.' The Doha employer stops paying "
                    "after month 9, claiming the worker 'abandoned her post.' The "
                    "worker is now performing unpaid domestic labor in Riyadh with no "
                    "documents, no contract, and no legal employer in any country. "
                    "Monthly expenses (food, lodging) are characterized as 'provided "
                    "by the family' and framed as generosity rather than compensation."
                ),
                "legal_basis": (
                    "Saudi Arabia's Anti-Trafficking in Persons Law (Royal Decree "
                    "M/40, 2009) criminalizes forced labor and document confiscation. "
                    "The Saudi Passport Law (Royal Decree M/24, 2000) prohibits "
                    "passport retention. However, enforcement against Saudi nationals "
                    "for domestic worker exploitation is rare — the US State Department "
                    "TIP Report 2024 rated Saudi Arabia as Tier 2 Watch List."
                ),
                "sector": "domestic_work",
                "corridor": "QA-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The worker exists in a jurisdictional void: her POEA/DMW contract "
                    "is with a Qatari employer who claims she abandoned; her physical "
                    "location is Saudi Arabia where she has no legal status; and POLO-"
                    "Riyadh cannot assist without a verified Saudi employment contract. "
                    "The Philippine Embassy in Riyadh operates a shelter (Bahay Kalinga) "
                    "that receives 200-300 runaway domestic workers annually, most with "
                    "exactly this cross-Gulf transfer profile."
                ),
            },
            {
                "id": "mt003_s4",
                "description": (
                    "After 14 months of unpaid work, the worker attempts to seek help "
                    "at the Philippine Embassy in Riyadh (Diplomatic Quarter). However, "
                    "without a valid Saudi iqama, she risks arrest for absconding "
                    "(huroob) under Saudi Arabia's absconding worker system — her "
                    "expired visit visa shows her as an overstayer. If reported by the "
                    "Riyadh household, she faces detention at the Shumaisi Immigration "
                    "Detention Center, then deportation to the Philippines (not Qatar). "
                    "Her Qatar employer has already filed a 'worker absconding' report "
                    "with Qatar's Ministry of Interior, potentially triggering an "
                    "Interpol notice that would bar her from future GCC employment."
                ),
                "legal_basis": (
                    "Saudi Arabia's Residency Law (Royal Decree M/17) criminalizes "
                    "overstaying and unauthorized employment; the huroob (absconding) "
                    "system allows employers to report workers who leave without "
                    "permission, placing them on a blacklist. Qatar's absconding "
                    "notification system under Ministry of Interior Circular 1/2019 "
                    "triggers an exit ban and potential criminal charges."
                ),
                "sector": "domestic_work",
                "corridor": "QA-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The worker faces criminal liability in two countries (Qatar: "
                    "absconding; Saudi Arabia: overstaying) while being the victim "
                    "of trafficking in both. Seeking help from authorities in either "
                    "country risks detention and deportation. POLO coverage gaps mean "
                    "no Philippine government office can see the full chain: POLO-Doha "
                    "shows a worker who abandoned her post, POLO-Riyadh has no record "
                    "of her. The US TIP Report 2024 specifically noted that cross-Gulf "
                    "domestic worker transfers remain an enforcement blind spot."
                ),
            },
        ],
        "chain_context": (
            "Cross-Gulf domestic worker re-trafficking exploits the kafala system's "
            "fundamental design: legal status is tied to a single employer in a single "
            "country, and there is no mechanism for tracking workers transferred between "
            "Gulf states by the same family network. The Philippines' extensive overseas "
            "labor infrastructure — POLO offices, OWWA insurance, DMW contracts — is "
            "designed for bilateral corridors (PH-QA, PH-SA) but has no protocol for "
            "workers who are moved from one GCC country to another mid-contract. Qatar's "
            "2020 kafala reforms and Saudi Arabia's 2021 labor mobility initiative both "
            "address within-country employer changes but are silent on cross-border "
            "transfers. The result is a jurisdictional gap where a worker with full "
            "legal protections in Country A can be rendered completely undocumented in "
            "Country B through a single plane ticket."
        ),
        "emergent_risk": (
            "Kafala-enabled cross-border transfer: a worker with full legal status in "
            "one Gulf state becomes completely undocumented and unprotected in another "
            "through an informal intra-family 'loan,' invisible to both countries' "
            "labor authorities."
        ),
        "difficulty": "hard",
        "source_references": [
            "HRW, 'Exported and Exposed: Abuses against Sri Lankan Domestic Workers in Saudi Arabia, Kuwait, Lebanon, and the UAE' (2007) — cross-Gulf transfer documentation",
            "US State Department, 'Trafficking in Persons Report 2024' — Saudi Arabia Tier 2 Watch List and cross-Gulf enforcement gaps",
            "ILO, 'Employer-Migrant Worker Relationships in the Middle East' (2017) — kafala transfer mechanisms across GCC states",
            "Philippine Overseas Labor Office, 'Bahay Kalinga Shelter Annual Report' (2023) — runaway domestic worker profiles",
        ],
        "corridors": ["PH-QA", "QA-SA"],
        "palermo_elements": {
            "act": ["recruitment", "transfer", "harbouring"],
            "means": [
                "abuse of position of vulnerability",
                "deception",
                "abuse of power",
            ],
            "purpose": ["forced labour", "servitude", "exploitation"],
        },
    },
    {
        "id": "multi_country_transit_004",
        "name": "Nepal-India-Gulf Construction Transit Exploitation",
        "category": "multi_country_transit",
        "steps": [
            {
                "id": "mt004_s1",
                "description": (
                    "A village-level dalal (sub-agent) in Dhading or Chitwan district "
                    "of the Kathmandu Valley approaches young men aged 18-30 with "
                    "promises of construction work in Qatar or the UAE at NPR 60,000-"
                    "80,000/month ($450-$600). The dalal charges NPR 80,000-150,000 "
                    "($600-$1,125) for 'processing fees,' payable upfront through "
                    "loans from village moneylenders (sahuji) at 24-36% annual "
                    "interest. Nepal's Department of Foreign Employment (DoFE) data "
                    "shows 654,000 labor permits issued in FY 2022/23, with 58% "
                    "destined for GCC countries. The dalal is not registered with "
                    "DoFE but operates as an informal referral partner for a "
                    "Kathmandu-based licensed manpower agency."
                ),
                "legal_basis": (
                    "Nepal's Foreign Employment Act 2064 (2007) Section 28 caps "
                    "recruitment fees at NPR 10,000 ($75) and Section 29 criminalizes "
                    "sub-agent activity. However, DoFE's 2023 enforcement data shows "
                    "only 47 prosecutions against an estimated 100,000+ active dalals "
                    "nationwide."
                ),
                "sector": "construction",
                "corridor": "NP-IN",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The dalal's fee of NPR 80,000-150,000 is 8-15x the legal "
                    "maximum under Nepal's Foreign Employment Act. KNOMAD's 2023 "
                    "migration cost survey documented that Nepali workers pay an "
                    "average of $1,200 in recruitment fees for GCC construction work, "
                    "with 72% of costs paid to unlicensed sub-agents. The sahuji "
                    "loan at 24-36% interest creates a compounding debt trap before "
                    "the worker even leaves their village."
                ),
            },
            {
                "id": "mt004_s2",
                "description": (
                    "The Kathmandu agency directs the worker to travel to Kolkata, "
                    "India (a 24-hour bus journey via Kakarvitta-Panitanki or "
                    "Birgunj-Raxaul border crossings) where an Indian sub-agent "
                    "handles 'Gulf paperwork.' Nepal-India open border under the "
                    "1950 Treaty of Peace and Friendship permits free movement "
                    "without visas. In Kolkata, the Indian sub-agent charges an "
                    "additional INR 50,000-100,000 ($600-$1,200) for medical "
                    "examinations at GAMCA-approved clinics, visa processing "
                    "coordination, and a 'guarantee letter.' The agent substitutes "
                    "the worker's original Qatari employment contract (NPR 60,000/"
                    "month) with a new contract showing QAR 900/month ($247) — the "
                    "Qatar minimum wage set by Ministerial Decision No. 25/2021."
                ),
                "legal_basis": (
                    "The 1950 Nepal-India Treaty of Peace and Friendship permits "
                    "free movement and employment of Nepali nationals in India and "
                    "vice versa. India's Emigration Act 1983 regulates recruitment "
                    "for overseas employment through the Protector General of "
                    "Emigrants (PoE) system, requiring clearance for workers "
                    "departing India for ECR (Emigration Check Required) countries "
                    "including all GCC states."
                ),
                "sector": "construction",
                "corridor": "NP-IN",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The India transit serves two exploitation functions: (1) adding "
                    "a second fee layer from the Indian sub-agent that compounds "
                    "the Nepali dalal's charges, and (2) performing contract "
                    "substitution outside Nepali regulatory jurisdiction. The worker "
                    "signed a contract in Kathmandu showing NPR 60,000/month; the "
                    "Indian sub-agent substitutes a contract at QAR 900/month "
                    "($247) — a 45% reduction. Nepal DoFE cannot monitor contracts "
                    "signed outside Nepal, and India's PoE system does not verify "
                    "contracts for Nepali nationals transiting through India."
                ),
            },
            {
                "id": "mt004_s3",
                "description": (
                    "From Kolkata (Netaji Subhas Chandra Bose International Airport) "
                    "or Mumbai (Chhatrapati Shivaji Maharaj International Airport), "
                    "the worker departs for Doha (Hamad International Airport) on the "
                    "substituted contract. Upon arrival, the Qatari employer's PRO "
                    "(Public Relations Officer) collects the worker at the airport "
                    "and confiscates his passport and mobile phone 'for company "
                    "processing.' The worker discovers his actual employer is not "
                    "the company named in either contract but a subcontractor "
                    "operating on Al Rayyan Municipality road construction projects. "
                    "Housing is a labor camp in the Industrial Area of Doha with "
                    "12-person rooms, 2 shared bathrooms per 50 workers, and no "
                    "air conditioning despite summer temperatures exceeding 45C."
                ),
                "legal_basis": (
                    "Qatar's kafala sponsorship reform under Law No. 18/2020 "
                    "eliminated the requirement for employer NOC (no objection "
                    "certificate) to change jobs after a notice period, but the "
                    "worker's visa is tied to the sponsoring company's Commercial "
                    "Registration (CR) number. Qatar Ministerial Decision No. "
                    "4/2015 mandates salary payment through the Wage Protection "
                    "System (WPS)."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Passport confiscation upon arrival violates Qatar Labor Law "
                    "Art. 8 (as amended 2019) and Saudi Labor Law Art. 61. Contract "
                    "substitution means the worker's actual employer, work site, "
                    "and salary differ from any document Nepal DoFE reviewed. The "
                    "worker arrived via India, so Qatar's immigration records show "
                    "arrival from India — if he files a complaint with Nepal POLO-"
                    "Doha, the deployment cannot be traced to a DoFE-approved "
                    "Kathmandu agency because departure was from an Indian airport."
                ),
            },
            {
                "id": "mt004_s4",
                "description": (
                    "After 6 months, the worker has received only 3 months of "
                    "salary at QAR 900/month ($247), with QAR 350/month deducted "
                    "for 'accommodation and meals.' Net receipts total $1,482 over "
                    "6 months ($247/month). Meanwhile, his village sahuji loan "
                    "(NPR 150,000 + 36% annual interest) has compounded to NPR "
                    "204,000 ($1,530), and the Indian sub-agent's fee of INR 100,000 "
                    "($1,200) was financed through a Kolkata moneylender at 30% "
                    "annual interest, now at INR 115,000 ($1,380). Total debt "
                    "across Nepal and India: $4,035. Total earnings after "
                    "deductions: $1,482. Net debt: $2,553 after 6 months of work. "
                    "The worker cannot afford a plane ticket home ($350-500) and "
                    "has no passport to purchase one."
                ),
                "legal_basis": (
                    "Qatar Ministerial Decision No. 25/2021 sets a non-discriminatory "
                    "minimum wage of QAR 1,000/month plus QAR 300 food allowance and "
                    "QAR 500 housing allowance (if employer does not provide). The "
                    "WPS should detect non-payment, but the employer pays QAR 900 "
                    "electronically (below minimum but technically recorded), and "
                    "the worker signs salary receipts under pressure."
                ),
                "sector": "construction",
                "corridor": "NP-QA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Multi-agent fee stacking across three countries creates a debt "
                    "structure that no single jurisdiction can see or address. Nepal "
                    "DoFE tracks the Kathmandu agency's authorized fee (NPR 10,000 "
                    "legal max); the dalal's NPR 150,000 and sahuji's interest are "
                    "invisible. India's PoE system does not track fees charged to "
                    "Nepali transiting workers. Qatar's WPS records QAR 900/month "
                    "payments but cannot detect the $4,035 three-country debt burden "
                    "that traps the worker. Verité's 2015 supply chain assessment "
                    "documented this exact multi-agent fee stacking pattern."
                ),
            },
        ],
        "chain_context": (
            "Nepal-India-Gulf transit exploitation leverages the open Nepal-India border "
            "to insert an unregulated Indian intermediary between Nepal's DoFE oversight "
            "and the Gulf employer. Each country's regulatory system covers only its own "
            "segment: Nepal DoFE monitors Kathmandu agencies but not village dalals or "
            "Indian sub-agents; India's PoE system regulates Indian citizens' emigration "
            "but does not systematically cover Nepali nationals transiting through Indian "
            "airports; Gulf labor authorities see a worker arriving from India with a "
            "valid contract but cannot verify recruitment costs incurred across two prior "
            "countries. KNOMAD's 2023 bilateral migration cost data shows that Nepal-to-"
            "Gulf workers pay an average of $1,200 in total fees — but this figure "
            "excludes interest on informal loans, which can double the effective cost. "
            "The result is a three-country debt trap where the worker's total obligation "
            "of $4,000-$6,000 requires 18-24 months of Gulf earnings to discharge."
        ),
        "emergent_risk": (
            "Three-country fee stacking: each intermediary in Nepal, India, and Qatar "
            "adds fees and debt that are invisible to the other countries' regulatory "
            "systems, creating a cumulative debt bondage burden of $4,000-$6,000 that "
            "no single authority can detect or remedy."
        ),
        "difficulty": "hard",
        "source_references": [
            "KNOMAD/World Bank, 'Migration and Development Brief 38' (2023) — bilateral corridor cost data for Nepal-Gulf routes",
            "Verité, 'Recruitment Practices and Migrant Labor Conditions in Nestlé's Thai Shrimp Supply Chain' (2015) — multi-agent fee stacking methodology (comparable pattern)",
            "Nepal Department of Foreign Employment, 'Annual Labour Migration Report FY 2022/23' — permit data and enforcement statistics",
            "ILO, 'Recruitment Costs of Migrant Workers: The Nepal-Qatar Corridor' (2019) — dalal fee structures and loan interest rates",
        ],
        "corridors": ["NP-IN", "IN-QA"],
        "palermo_elements": {
            "act": ["recruitment", "transportation", "transfer"],
            "means": [
                "deception",
                "abuse of position of vulnerability",
                "debt bondage",
            ],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "multi_country_transit_005",
        "name": "Central America-Mexico-US Agricultural Labor Chain",
        "category": "multi_country_transit",
        "steps": [
            {
                "id": "mt005_s1",
                "description": (
                    "A reclutador (recruiter) operating in Huehuetenango and San "
                    "Marcos departments in Guatemala's Western Highlands recruits "
                    "indigenous Mam and Q'anjob'al-speaking men for agricultural "
                    "work in the United States, promising $12-15/hour wages picking "
                    "onions, peppers, and blueberries. The reclutador charges "
                    "Q 15,000-25,000 ($1,900-$3,200) for 'visa processing and "
                    "transportation,' payable through loans from local lenders at "
                    "4-5% monthly interest, using family land titles or homes as "
                    "collateral. The reclutador works as a subcontractor for a "
                    "US-based farm labor contractor (FLC) that holds H-2A temporary "
                    "agricultural worker visa allocations from the US Department "
                    "of Labor."
                ),
                "legal_basis": (
                    "Guatemala's Migration Code (Decreto 44-2016) regulates "
                    "recruitment agencies, but reclutadores in rural Western "
                    "Highland communities operate informally outside regulatory "
                    "reach. The US H-2A program (8 USC 1101(a)(15)(H)(ii)(a)) "
                    "permits temporary agricultural workers, with employer-paid "
                    "recruitment and transportation costs required under 20 CFR "
                    "655 Subpart B."
                ),
                "sector": "agriculture",
                "corridor": "GT-MX",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "H-2A regulations at 20 CFR 655.135(j) prohibit employers from "
                    "charging workers recruitment fees, yet the reclutador's $1,900-"
                    "$3,200 charge is structured as a separate 'service' outside the "
                    "formal H-2A process. Polaris Project's 2022 report documented "
                    "that 71% of H-2A workers from Guatemala reported paying "
                    "recruitment fees exceeding $1,000, and 46% had debt secured "
                    "against property. The collateral requirement means workers who "
                    "leave or are fired lose their family homes."
                ),
            },
            {
                "id": "mt005_s2",
                "description": (
                    "Workers are transported by bus from Huehuetenango through "
                    "Guatemala City to the Mexico-Guatemala border at Tecun Uman/"
                    "Ciudad Hidalgo (Chiapas). Mexican transit is arranged through "
                    "a coyote network that charges $3,000-8,000 per person for "
                    "overland passage to the US-Mexico border, with cartel-controlled "
                    "checkpoints along the route through Chiapas, Oaxaca, and "
                    "Tamaulipas extracting additional 'fees' of $500-2,000. Workers "
                    "travel in groups of 20-40 in enclosed trucks for 5-14 days. "
                    "Some workers have legitimate H-2A petitions pending at the "
                    "US Consulate in Monterrey; others were promised petitions "
                    "that were never filed. The coyote transit fee is added to the "
                    "worker's existing debt to the reclutador."
                ),
                "legal_basis": (
                    "Mexico's Ley de Migración (2011) Article 159 criminalizes "
                    "smuggling of migrants (tráfico de personas); Mexico's Ley "
                    "General para Prevenir, Sancionar y Erradicar los Delitos en "
                    "Materia de Trata de Personas (2012) distinguishes trafficking "
                    "from smuggling. Workers with legitimate H-2A petitions may "
                    "transit Mexico legally under a transit visa (FMM), but those "
                    "without valid petitions are irregular migrants subject to "
                    "deportation under INM (Instituto Nacional de Migración) enforcement."
                ),
                "sector": "agriculture",
                "corridor": "GT-MX",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Mexican transit adds $3,000-8,000 in debt controlled by cartel "
                    "networks that are separate from but coordinated with the "
                    "Guatemalan reclutador. Workers cannot distinguish between "
                    "legitimate H-2A processing and trafficking: both involve "
                    "paying fees, traveling to Mexico, and waiting for a visa. "
                    "The US DOJ's Operation Blooming Onion (2021) indictment "
                    "documented that FLCs in South Georgia used this ambiguity "
                    "to recruit workers who believed they had legitimate visas "
                    "but arrived with debts of $4,900-$11,200 across two countries."
                ),
            },
            {
                "id": "mt005_s3",
                "description": (
                    "Workers arrive at the US employer's operations — typically "
                    "onion, vidalia, blueberry, or pepper farms in South Georgia "
                    "(Vidalia, Lyons, Baxley), South Carolina (Orangeburg County), "
                    "or Florida (Plant City, Immokalee) — and are assigned to "
                    "employer-provided housing in labor camps on or near the farm. "
                    "Housing consists of single-wide trailers or converted barns "
                    "with 8-12 workers per unit, located on rural roads 15-30 miles "
                    "from the nearest town. Workers are issued H-2A visas tied to "
                    "the specific FLC, meaning any termination or departure voids "
                    "their legal status. The FLC deducts $35-50/week for housing "
                    "and $25-40/week for 'transportation to fields' from wages, "
                    "despite H-2A regulations requiring employer-provided housing "
                    "at no cost."
                ),
                "legal_basis": (
                    "The H-2A program under 20 CFR 655 Subpart B requires employers "
                    "to provide free housing meeting OSHA standards (29 CFR 1910.142), "
                    "transportation between housing and work sites at no cost, and "
                    "the Adverse Effect Wage Rate (AEWR) — set at $13.67-$17.51/hour "
                    "depending on state for 2024. Workers may not be charged for "
                    "housing, tools, or inbound transportation under 20 CFR "
                    "655.135(e)-(j)."
                ),
                "sector": "agriculture",
                "corridor": "MX-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Employer-controlled housing in isolated rural areas combined "
                    "with visa tied to a single employer creates physical and legal "
                    "captivity. Workers who complain about illegal deductions risk "
                    "termination, which immediately triggers visa revocation and "
                    "potential deportation. The DOJ's Blooming Onion case documented "
                    "that workers in Vidalia, Georgia were housed in camps surrounded "
                    "by fencing, with an armed guard who monitored departures, and "
                    "were charged $50/week for housing that H-2A regulations require "
                    "to be free."
                ),
            },
            {
                "id": "mt005_s4",
                "description": (
                    "Workers who protest conditions, request payment of the legally "
                    "required AEWR, or attempt to contact the DOL Wage and Hour "
                    "Division are threatened with termination and deportation. The "
                    "FLC supervisor tells workers: 'If you leave, I call immigration "
                    "and you go back to Guatemala owing $8,000 with your family's "
                    "house as collateral.' Workers who are fired or attempt to leave "
                    "are reported to ICE (Immigration and Customs Enforcement) by the "
                    "FLC, triggering deportation proceedings. The FLC withholds final "
                    "paychecks for terminated workers, citing 'damage to company "
                    "property' or 'incomplete contract.' Total cumulative debt across "
                    "Guatemala, Mexico, and the US averages $7,900-$11,200 per worker."
                ),
                "legal_basis": (
                    "The TVPA (22 USC 7102) defines labor trafficking to include "
                    "obtaining labor through threats of serious harm or abuse of "
                    "law or legal process. H-2A workers have the right to file WHD "
                    "complaints regardless of immigration status under 29 USC 218. "
                    "Retaliation against workers for exercising rights violates the "
                    "Migrant and Seasonal Agricultural Worker Protection Act (MSPA) "
                    "29 USC 1851."
                ),
                "sector": "agriculture",
                "corridor": "MX-US",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The threat of deportation weaponizes immigration enforcement "
                    "against trafficking victims. Workers' debts in Guatemala "
                    "(collateralized by family land) make deportation catastrophic — "
                    "they return owing $8,000+ with no earnings and face property "
                    "foreclosure. The DOJ's Blooming Onion indictment (24 defendants, "
                    "S.D. Georgia, November 2021) documented this exact pattern: "
                    "FLCs used threats of ICE reporting to prevent workers from "
                    "contacting DOL, while withholding wages that would have allowed "
                    "workers to service their Guatemala-based debts."
                ),
            },
        ],
        "chain_context": (
            "The Central America-Mexico-US agricultural trafficking chain exploits the "
            "structural design of the H-2A temporary worker program. The visa is tied to "
            "a single employer, creating a legal dependency that mirrors debt bondage. "
            "Recruitment fees charged in Guatemala are invisible to US regulators because "
            "they occur outside US jurisdiction through unlicensed reclutadores. Mexican "
            "transit fees charged by cartel-connected coyotes create a second debt layer "
            "that is invisible to both Guatemalan and US authorities. The US employer "
            "then leverages the combined three-country debt ($7,900-$11,200) plus the "
            "threat of deportation plus the collateralized family property in Guatemala "
            "to prevent workers from exercising their legal rights. The DOJ's Operation "
            "Blooming Onion (2021) — one of the largest federal labor trafficking "
            "prosecutions in US history — documented this pattern across farms in "
            "Georgia and neighboring states, resulting in 24 indictments."
        ),
        "emergent_risk": (
            "Three-country debt leverage: recruitment fees in Guatemala secured by family "
            "property, cartel transit fees in Mexico, and employer-controlled housing and "
            "visa status in the US create a coercion structure that weaponizes each "
            "country's legal system against the worker."
        ),
        "difficulty": "hard",
        "source_references": [
            "US DOJ, 'Operation Blooming Onion' (Nov 2021, S.D. Georgia) — 24-defendant forced labor indictment of H-2A farm labor contractors",
            "Polaris Project, 'Labor Trafficking in the US: A Closer Look at Temporary Work Visas' (2022) — H-2A recruitment fee and debt documentation",
            "Centro de los Derechos del Migrante (CDM), 'Recruitment Revealed: Fundamental Flaws in the H-2 Temporary Worker Program' (2013) — Guatemala reclutador fee analysis",
            "UNODC, 'Global Report on Trafficking in Persons 2022' — Central American transit route mapping",
        ],
        "corridors": ["GT-MX", "MX-US"],
        "palermo_elements": {
            "act": ["recruitment", "transportation", "harbouring"],
            "means": [
                "coercion",
                "deception",
                "abuse of position of vulnerability",
                "debt bondage",
            ],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "multi_country_transit_006",
        "name": "Vietnam-Cambodia-Thailand Fishing Vessel Route",
        "category": "multi_country_transit",
        "steps": [
            {
                "id": "mt006_s1",
                "description": (
                    "A labor broker (cò) in Ho Chi Minh City or Can Tho recruits "
                    "young men aged 16-30 from the Mekong Delta provinces (An Giang, "
                    "Dong Thap, Kien Giang) with promises of factory work in Thailand "
                    "paying $400-600/month. The cò charges VND 20-40 million "
                    "($800-$1,600) for 'processing and travel costs,' typically "
                    "financed through family borrowing from local money lenders at "
                    "3-5% monthly interest. Workers are given minimal information "
                    "about the specific job or destination, being told only 'good "
                    "work in a Thai factory with overtime.' Vietnam's Department "
                    "of Overseas Labour (DOLAB) under the Ministry of Labour issues "
                    "330,000+ overseas labor permits annually, but the cò operates "
                    "outside this system."
                ),
                "legal_basis": (
                    "Vietnam's Law on Vietnamese Workers Working Abroad under "
                    "Contract (Law No. 69/2020/QH14) regulates licensed labor "
                    "export companies and caps service fees; however, the cò "
                    "system operates as informal sub-agents without DOLAB "
                    "registration. The Vietnam-Thailand bilateral labor MOU (2015) "
                    "provides a formal channel but is rarely used for unskilled labor."
                ),
                "sector": "fishing",
                "corridor": "VN-KH",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The recruiter deliberately misrepresents the job as 'factory "
                    "work' to avoid triggering the worker's awareness of fishing "
                    "vessel exploitation, which is widely reported in Vietnamese "
                    "media. ILO's 2018 'Ship to Shore Rights' report documented "
                    "that 76% of Vietnamese fishers on Thai vessels were recruited "
                    "under false pretenses — promised factory or construction work "
                    "and diverted to fishing only after arriving in a transit country."
                ),
            },
            {
                "id": "mt006_s2",
                "description": (
                    "Workers are transported from Ho Chi Minh City by bus to the "
                    "Bavet-Moc Bai border crossing into Cambodia, then onward to "
                    "Phnom Penh, where a Cambodian middleman 'processes documents' "
                    "over 3-7 days. In Phnom Penh, workers stay in a guesthouse in "
                    "the Chamkarmon district controlled by the broker network. "
                    "During this period, the middleman confiscates the workers' "
                    "Vietnamese identity cards and passports (if any), claiming "
                    "they are needed for 'Thai visa processing.' Workers are "
                    "charged an additional $200-500 for Cambodian 'transit fees' "
                    "and 'document preparation.' Some workers realize the job is "
                    "not factory work, but with documents confiscated and debts "
                    "already incurred, they have no practical option to return."
                ),
                "legal_basis": (
                    "Cambodia's Law on Suppression of Human Trafficking and Sexual "
                    "Exploitation (2008) criminalizes trafficking and forced labor. "
                    "The Vietnam-Cambodia border at Bavet-Moc Bai is a legal "
                    "crossing with immigration controls, and Vietnamese nationals "
                    "can enter Cambodia visa-free for 30 days under ASEAN "
                    "arrangements."
                ),
                "sector": "transit_smuggling",
                "corridor": "VN-KH",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Cambodia serves as a jurisdictional laundering stage: the "
                    "worker enters legally (visa-free ASEAN), has documents "
                    "confiscated on Cambodian soil (where Vietnamese labor protections "
                    "do not apply), and is moved to Thailand by a different broker "
                    "than the original cò. EJF's 2019 'Blood and Water' report "
                    "documented that Cambodian transit was used in 38% of Vietnamese "
                    "fishing trafficking cases because it creates a break in the "
                    "chain that prevents Vietnamese authorities from tracing the "
                    "worker's onward movement."
                ),
            },
            {
                "id": "mt006_s3",
                "description": (
                    "From Phnom Penh, workers are transported to the Cambodian "
                    "coastal city of Sihanoukville (Preah Sihanouk Province), where "
                    "the Cambodian middleman sells the workers to a Thai fishing "
                    "vessel captain (hua naa) or vessel broker for $400-600 per "
                    "person. The sale typically occurs at informal docking areas in "
                    "Sihanoukville's Otres or Ochheuteal beach areas, or at the "
                    "commercial fishing port. Workers are then transported by "
                    "speedboat or small vessel across the Gulf of Thailand to Thai "
                    "fishing ports at Trat, Rayong, or Ranong Province. Upon arrival "
                    "at the Thai port, workers are immediately placed aboard a "
                    "deep-sea trawler with no shore time, no contract, and no "
                    "registration at a PIPO (Port-In Port-Out) inspection center."
                ),
                "legal_basis": (
                    "Thailand's Royal Ordinance on Fisheries B.E. 2558 (2015) "
                    "requires all crew to be registered through PIPO inspection "
                    "and hold valid seaman's books. ILO C188 (Work in Fishing "
                    "Convention, ratified by Thailand January 2019) requires "
                    "written work agreements for all fishers. The sale of a human "
                    "being constitutes trafficking under Thailand's Anti-Trafficking "
                    "in Persons Act B.E. 2551 (2008) Section 6."
                ),
                "sector": "fishing",
                "corridor": "KH-TH",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The literal sale of workers for $400-600 per person is among "
                    "the clearest trafficking indicators. Greenpeace's 2016 'Turn "
                    "the Tide' report documented identical transactions at "
                    "Sihanoukville and other Cambodian ports, with prices varying "
                    "from $300 for unskilled workers to $800 for those with fishing "
                    "experience. Workers who arrive at Thai ports outside the PIPO "
                    "system have no official existence in Thailand — they are not "
                    "on any crew manifest, hold no seaman's book, and have no "
                    "record of entering the country."
                ),
            },
            {
                "id": "mt006_s4",
                "description": (
                    "The trawler operates in the Gulf of Thailand, the Andaman Sea, "
                    "or waters around Indonesia's Natuna Islands and Malaysia's East "
                    "Coast for voyages of 3-18 months without returning to port. "
                    "Workers receive no wages — the hua naa states that 'payment "
                    "is settled when the boat returns' or that wages are used to "
                    "offset the $400-600 purchase price. Workers are subjected to "
                    "20-22 hour shifts, physical violence for slow work, and fed "
                    "rice and fish from the catch. At-sea transshipment to reefer "
                    "vessels (often Taiwanese or Thai-flagged) means the trawler "
                    "need never return to port. If a worker escapes by jumping ship "
                    "at an Indonesian or Malaysian port, they are illegal immigrants "
                    "in yet another country with no documents, no money, and no "
                    "ability to contact Vietnamese authorities."
                ),
                "legal_basis": (
                    "In international waters, flag-state jurisdiction applies under "
                    "UNCLOS Art. 94; in Indonesian or Malaysian waters, workers are "
                    "subject to those countries' immigration and labor laws. "
                    "Indonesia's Immigration Law No. 6/2011 provides for deportation "
                    "of undocumented foreign nationals; Malaysia's Immigration Act "
                    "1959/63 Act 155 likewise criminalizes unauthorized entry."
                ),
                "sector": "fishing",
                "corridor": "TH-international",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Workers are trapped in a floating prison outside any country's "
                    "effective jurisdiction. IOM's maritime trafficking data documents "
                    "that fishing vessel victims spend an average of 3.4 years at sea "
                    "before rescue or escape. Escape to a third country (Indonesia, "
                    "Malaysia) creates a new layer of illegality — the worker is "
                    "undocumented in a country they never chose to enter. EJF "
                    "documented in 2015 that rescued Vietnamese fishers in Indonesia's "
                    "Benjina (Aru Islands) had been at sea for up to 10 years, passed "
                    "between multiple vessels, and had no idea which country's waters "
                    "they were in."
                ),
            },
        ],
        "chain_context": (
            "The Vietnam-Cambodia-Thailand fishing route exploits three countries' "
            "jurisdictional gaps and the fundamental enforcement challenge of fishing "
            "at sea. Vietnam's labor export regulations cannot reach informal cò "
            "recruiters who route workers through Cambodia rather than through DOLAB-"
            "licensed channels. Cambodia's brief transit role creates a jurisdictional "
            "handoff where document confiscation and sale to Thai brokers occurs beyond "
            "Vietnamese oversight. Thailand's PIPO system — designed to track crew at "
            "departure and arrival — is bypassed entirely when workers are loaded at "
            "sea from Cambodian transit points. Once on a vessel in international waters, "
            "the worker exists in no country's labor system. The 2015 AP investigation "
            "that uncovered enslaved fishers in Benjina, Indonesia — many Vietnamese "
            "and Cambodian — triggered Thailand's downgrade to Tier 3 on the US TIP "
            "Report and prompted the 2015 Fisheries Royal Ordinance, but the Cambodia "
            "transit pipeline continues to evade the reformed system."
        ),
        "emergent_risk": (
            "Three-country pipeline to maritime statelessness: deceptive recruitment in "
            "Vietnam, document confiscation and sale in Cambodia, and placement on "
            "unregistered Thai fishing vessels create workers with no legal existence "
            "in any jurisdiction, trapped at sea for months to years."
        ),
        "difficulty": "expert",
        "source_references": [
            "EJF, 'Blood and Water: Human Rights Abuse in the Global Seafood Industry' (2019) — Cambodian transit and Vietnamese fisher exploitation documentation",
            "Greenpeace, 'Turn the Tide: Human Rights Abuses and Illegal Fishing in Thailand's Overseas Fishing Industry' (2016) — Sihanoukville sale prices and vessel-to-vessel transfers",
            "ILO, 'Ship to Shore Rights: Baseline Research Findings on Fishers and Seafood Workers in Thailand' (2018) — 76% false recruitment prevalence among Vietnamese fishers",
            "Associated Press, 'Slaves May Have Caught the Fish You Bought' (Mar 25, 2015) — Benjina investigation that triggered global awareness",
            "IOM, 'Report on Human Trafficking, Forced Labour and Fisheries Crime in the Indonesian Fishing Industry' (2016) — Vietnamese victims rescued from Indonesian waters",
        ],
        "corridors": ["VN-KH", "KH-TH"],
        "palermo_elements": {
            "act": ["recruitment", "transportation", "transfer", "harbouring"],
            "means": [
                "coercion",
                "deception",
                "abuse of position of vulnerability",
                "giving payments to a person having control over another",
            ],
            "purpose": ["forced labour", "servitude", "slavery"],
        },
    },
    {
        "id": "multi_country_transit_007",
        "name": "Bangladesh-Malaysia-Australia Visa Laundering Chain",
        "category": "multi_country_transit",
        "steps": [
            {
                "id": "mt007_s1",
                "description": (
                    "A dalal (recruitment agent) in Dhaka's Gulshan or Uttara "
                    "districts arranges a Malaysian tourist visa (eVISA, 30-day "
                    "validity) for a Bangladeshi worker from Sylhet or Comilla "
                    "division, charging BDT 200,000-400,000 ($1,700-$3,400) for "
                    "'complete Malaysia package including job placement.' The "
                    "worker borrows from family, sells agricultural land, or takes "
                    "loans from NGO microfinance institutions or informal lenders "
                    "(mahajan) at 3-5% monthly interest. Bangladesh BMET (Bureau "
                    "of Manpower, Employment and Training) data shows 1.1 million "
                    "labor migration clearances in 2023, but Malaysia-bound tourist "
                    "visas are outside BMET jurisdiction. The dalal provides a "
                    "tourist visa, not a work permit — the worker is told 'you "
                    "convert to work visa after arrival, everyone does this.'"
                ),
                "legal_basis": (
                    "Bangladesh's Overseas Employment and Migrants Act 2013 regulates "
                    "labor migration through BMET clearance, but tourist visa travel "
                    "falls outside its scope. Malaysia's Immigration Act 1959/63 "
                    "permits tourist entry for Bangladeshi nationals with valid "
                    "eVISA, but Section 39B prohibits employment on tourist visas "
                    "with penalties of up to 5 years imprisonment and caning."
                ),
                "sector": "manufacturing",
                "corridor": "BD-MY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The tourist-visa-to-work-visa conversion promise is a "
                    "documented deception pattern. IOM Bangladesh's 2020 mapping "
                    "of recruitment practices found that 34% of Bangladesh-Malaysia "
                    "migrants traveled on tourist visas with false promises of "
                    "work visa conversion. The BDT 200,000-400,000 fee is 2.4-4.8x "
                    "the BMET-authorized maximum of BDT 84,000. Upon arrival in "
                    "Malaysia, the worker discovers no work visa conversion pathway "
                    "exists for tourist visa holders, making them immediately "
                    "deportable if detected."
                ),
            },
            {
                "id": "mt007_s2",
                "description": (
                    "In Malaysia, the worker joins an estimated 600,000-1,200,000 "
                    "undocumented foreign workers (primarily Bangladeshi, Indonesian, "
                    "and Myanmar nationals). The dalal's Malaysian contact places the "
                    "worker in a factory in Penang's Bayan Lepas Free Industrial Zone "
                    "or a palm oil plantation in Johor/Sabah, paying RM 1,000-1,400/"
                    "month ($215-$300) cash, well below Malaysia's minimum wage of "
                    "RM 1,500/month. After the 30-day tourist visa expires, the "
                    "worker is undocumented. The Malaysian employer retains the "
                    "worker's passport 'to prevent problems with RELA' (Malaysia's "
                    "People's Volunteer Corps, which conducts immigration raids). "
                    "Workers live in factory-provided dormitories or plantation "
                    "housing, working 10-14 hour days with no rest day."
                ),
                "legal_basis": (
                    "Malaysia's Employment Act 1955 (amended 2022) applies to all "
                    "workers regardless of documentation status, setting minimum "
                    "wage at RM 1,500/month. The Passport Act 1966 Section 12 "
                    "prohibits passport retention. However, undocumented workers "
                    "who report violations face arrest under Immigration Act "
                    "Section 6(1)(c) and deportation — creating a structural "
                    "barrier to rights enforcement."
                ),
                "sector": "manufacturing",
                "corridor": "BD-MY",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The worker is trapped by a combination of debt (BDT 200,000-"
                    "400,000 + interest), undocumented status, and passport "
                    "confiscation. Malaysian authorities' approach to undocumented "
                    "workers — arrest and deportation rather than victim identification "
                    "— means seeking help from police triggers the same outcome as "
                    "the employer's threats. The US TIP Report 2024 noted that "
                    "Malaysia 'did not adequately screen for trafficking among "
                    "undocumented workers detained during enforcement operations.'"
                ),
            },
            {
                "id": "mt007_s3",
                "description": (
                    "After 3-6 months in Malaysia, a Malaysian-based migration "
                    "agent (sindikét) offers the worker 'passage to Australia for "
                    "real wages — AUD 25-30/hour in farming.' The sindikét charges "
                    "RM 15,000-25,000 ($3,215-$5,360) for a tourist visa (subclass "
                    "600) or Electronic Travel Authority (subclass 601) to Australia, "
                    "obtained using the worker's Bangladeshi passport (returned "
                    "temporarily for the visa application) and fabricated financial "
                    "documents showing sufficient funds for tourism. The worker "
                    "flies from KLIA (Kuala Lumpur International Airport) to Sydney "
                    "or Melbourne on the tourist visa, valid for 3 months. The new "
                    "fee is added to the worker's cumulative debt, now totaling "
                    "BDT 200,000-400,000 (Dhaka dalal) + RM 15,000-25,000 "
                    "(Malaysian sindikét) = $4,915-$8,760 across two countries."
                ),
                "legal_basis": (
                    "Australia's Migration Act 1958 Section 116 permits visa "
                    "cancellation for breach of conditions; working on a tourist "
                    "visa (subclass 600) violates condition 8101 (no work). "
                    "Australia's Working Holiday Maker (WHM) visa (subclass 417/462) "
                    "is the legitimate pathway for temporary agricultural work, "
                    "but it is not available to Bangladeshi nationals."
                ),
                "sector": "agriculture",
                "corridor": "MY-AU",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The Malaysia-to-Australia stage is 'visa laundering': the "
                    "worker's Bangladeshi passport is used to obtain an Australian "
                    "tourist visa from a Malaysian address, creating an immigration "
                    "history that shows lawful entry to both countries. However, the "
                    "worker has no legal right to work in either. The sindikét's fee "
                    "of RM 15,000-25,000 is pure debt — the tourist visa provides "
                    "no work rights. Australia's Department of Home Affairs data "
                    "shows Bangladeshi nationals had the 4th-highest visa overstay "
                    "rate among tourist visa holders in 2022-23."
                ),
            },
            {
                "id": "mt007_s4",
                "description": (
                    "In Australia, the worker is placed on a farm in regional "
                    "Victoria (Mildura, Shepparton), Queensland (Bundaberg, Bowen), "
                    "or New South Wales (Griffith, Coffs Harbour) through a labor "
                    "hire company that does not verify work rights. The worker earns "
                    "AUD 15-20/hour cash ($10-$13 USD) — well below the national "
                    "minimum of AUD 23.23/hour and the Horticulture Award rate. "
                    "After the 3-month tourist visa expires, the worker becomes "
                    "undocumented. If detected by Australian Border Force (ABF), "
                    "the worker is detained at Villawood Immigration Detention "
                    "Centre (Sydney) or Melbourne Immigration Transit Accommodation "
                    "and deported to Bangladesh — not Malaysia — because Bangladesh "
                    "is the passport country. The original Dhaka dalal's debt of "
                    "BDT 200,000-400,000 (now compounded with 3-5% monthly interest "
                    "for 9-12 months) remains unpaid, and the mahajan in Sylhet "
                    "begins asset recovery against the worker's family."
                ),
                "legal_basis": (
                    "Australia's Fair Work Act 2009 Section 357 prohibits sham "
                    "contracting, and the Modern Slavery Act 2018 requires large "
                    "businesses to report on supply chain risks. The Horticulture "
                    "Award 2020 sets minimum pay rates for farm work. However, "
                    "enforcement in regional agriculture relies on the Fair Work "
                    "Ombudsman (FWO), which conducted only 169 horticulture "
                    "compliance investigations in 2022-23 across 5,700+ farm "
                    "businesses."
                ),
                "sector": "agriculture",
                "corridor": "MY-AU",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Deportation to Bangladesh (not Malaysia) means the worker "
                    "returns to the original dalal's jurisdiction with unpaid, "
                    "compounding debt and no earnings. The Australian exploitation "
                    "period generated sub-minimum-wage income that was consumed by "
                    "living costs, and the Malaysian exploitation period paid below "
                    "Malaysian minimum wage. The worker's two-country transit "
                    "created debts in two countries and exploitation in two countries "
                    "but produced zero net income. Australia's FWO reported in 2023 "
                    "that undocumented workers in horticulture were paid an average "
                    "of AUD 12/hour — 48% below the legal minimum — and that 'fear "
                    "of deportation is the primary barrier to reporting.'"
                ),
            },
        ],
        "chain_context": (
            "The Bangladesh-Malaysia-Australia chain exploits tourist visa regimes in "
            "two countries to create a 'visa laundering' pipeline. Bangladesh's BMET "
            "labor migration system, designed for formal bilateral channels (BD-SA, "
            "BD-QA, BD-MY under MOU), is bypassed entirely by the tourist visa route. "
            "Malaysia serves as a transit exploitation stage where the worker accumulates "
            "additional debt while building an immigration history (Malaysian entry stamp) "
            "that supports the subsequent Australian tourist visa application. Australia's "
            "agricultural sector has well-documented reliance on undocumented labor, "
            "particularly in regional horticulture — the Migrant Workers' Taskforce "
            "(2019) estimated 60,000-100,000 undocumented workers in Australian "
            "agriculture. Upon detection and deportation, the worker is returned to "
            "Bangladesh (passport country) with debts accumulated across two countries "
            "and interest compounding from the original Dhaka loan."
        ),
        "emergent_risk": (
            "Tourist visa laundering through a transit country: Bangladesh-origin debt "
            "funds Malaysia transit exploitation, which funds Australia-destination "
            "exploitation, with deportation returning the worker to the origin country "
            "carrying compounded debts from all three jurisdictions."
        ),
        "difficulty": "hard",
        "source_references": [
            "IOM Bangladesh, 'Mapping of Labour Migration Recruitment Practices in Bangladesh' (2020) — tourist visa deception and dalal fee documentation",
            "Australia Migrant Workers' Taskforce, 'Report of the Migrant Workers' Taskforce' (Mar 2019) — undocumented horticulture worker estimates",
            "Fair Work Ombudsman, 'Annual Report 2022-23' — horticulture compliance investigation data and wage theft findings",
            "US State Department, 'Trafficking in Persons Report 2024' — Malaysia and Australia country narratives",
        ],
        "corridors": ["BD-MY", "MY-AU"],
        "palermo_elements": {
            "act": ["recruitment", "transportation", "transfer"],
            "means": [
                "deception",
                "abuse of position of vulnerability",
                "debt bondage",
            ],
            "purpose": ["forced labour", "exploitation"],
        },
    },
    {
        "id": "multi_country_transit_008",
        "name": "Ethiopia-Yemen-Saudi Smuggling-to-Trafficking Pipeline",
        "category": "multi_country_transit",
        "steps": [
            {
                "id": "mt008_s1",
                "description": (
                    "Economic migrants from Ethiopia's Oromia, Amhara, and Harari "
                    "regions — particularly from Dire Dawa, Harar, Jigjiga, and "
                    "surrounding rural areas — gather at transit points in Dire Dawa "
                    "and the Afar region, where dalala (brokers) arrange overland "
                    "transport to Djibouti's Obock region on the Gulf of Aden coast. "
                    "The dalala charge ETB 30,000-80,000 ($540-$1,440) for the "
                    "500 km journey through the Afar desert, with groups of 30-100 "
                    "migrants traveling in trucks or on foot. The Mixed Migration "
                    "Centre (MMC) 4Mi surveys recorded 92,000 movements along this "
                    "route in 2023, primarily young men aged 15-30 seeking "
                    "construction or domestic work in Saudi Arabia."
                ),
                "legal_basis": (
                    "Ethiopia's Overseas Employment Proclamation No. 923/2016 "
                    "regulates labor migration through the Ministry of Labour and "
                    "Social Affairs (MOLSA), but the proclamation covers only "
                    "contract-based labor migration, not irregular movement. "
                    "Ethiopia-Djibouti border crossing at Loyada/Galafi is a legal "
                    "entry point, but most migrants cross at informal points along "
                    "the 349 km shared border."
                ),
                "sector": "transit_smuggling",
                "corridor": "ET-DJ",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The Ethiopian dalala control the first segment of a journey "
                    "that the migrant typically conceptualizes as smuggling (consensual "
                    "facilitated migration) rather than trafficking. However, MMC "
                    "4Mi data from 2022-2024 shows that 62% of Ethiopian migrants "
                    "on this route experienced exploitation meeting trafficking "
                    "indicators before reaching Yemen, including physical assault "
                    "(38%), robbery by the broker or armed groups (45%), and sexual "
                    "violence against women and girls (29%). The Afar desert transit "
                    "is itself lethal — IOM estimated 300+ deaths annually on the "
                    "Ethiopia-Djibouti overland route."
                ),
            },
            {
                "id": "mt008_s2",
                "description": (
                    "From Djibouti's Obock coast, migrants board wooden boats or "
                    "fiberglass dhows operated by Djiboutian and Yemeni smugglers "
                    "for the 30-40 km Gulf of Aden crossing to Yemen's southern "
                    "coast (Lahj and Aden governorates). Boats carry 80-150 people "
                    "with minimal water or safety equipment; smugglers charge "
                    "$100-300 per person for the 6-12 hour crossing. UNHCR recorded "
                    "73,000 arrivals on Yemen's southern coast in 2023, primarily "
                    "Ethiopian and Somali nationals. Upon landing at the Yemeni "
                    "coast — typically at Ras al-Ara or Bir Ali — migrants are "
                    "immediately seized by armed groups (often aligned with local "
                    "militias or Al-Qaeda in the Arabian Peninsula affiliates) who "
                    "control the landing beaches."
                ),
                "legal_basis": (
                    "Djibouti's Law No. 133/AN/16 on Combating Trafficking in "
                    "Persons (2016) criminalizes trafficking and smuggling, and "
                    "Djibouti has received EU and IOM capacity-building for border "
                    "management. Yemen's conflict since 2014 has collapsed state "
                    "institutions, and there is no functioning immigration or "
                    "anti-trafficking system in southern Yemen."
                ),
                "sector": "transit_smuggling",
                "corridor": "DJ-YE",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The Gulf of Aden crossing is the point where smuggling "
                    "definitively becomes trafficking for many migrants. IOM Missing "
                    "Migrants recorded 118 deaths on Gulf of Aden crossings in 2023 "
                    "from drowning and boat capsizing. Upon landing in Yemen, the "
                    "consensual smuggling relationship ends and armed exploitation "
                    "begins. UNHCR's 2023 Gulf of Aden report documented that 87% "
                    "of arrivals at Ras al-Ara were immediately detained by armed "
                    "groups, with men forced into labor and women subjected to "
                    "sexual violence and ransom demands."
                ),
            },
            {
                "id": "mt008_s3",
                "description": (
                    "In Yemen, migrants are held in informal detention camps in "
                    "Lahj and Shabwah governorates, controlled by Yemeni and "
                    "Ethiopian criminal networks. Captors demand ransom payments "
                    "of $1,000-3,000 from migrants' families in Ethiopia, enforced "
                    "by beating victims during phone calls to their families. "
                    "Payment is made via hawala (informal money transfer) networks "
                    "connecting Ethiopian middlemen in Dire Dawa to Yemeni camp "
                    "operators. Migrants who cannot pay are forced to work — men in "
                    "agriculture (khat farms in Haraz Mountains) or portering, women "
                    "in domestic servitude or sexual exploitation. Detention periods "
                    "range from 2 weeks to 6 months. MMC 4Mi surveys document that "
                    "76% of Ethiopian migrants transiting Yemen experienced physical "
                    "violence, 54% reported ransom demands, and 23% of women "
                    "reported rape."
                ),
                "legal_basis": (
                    "Yemen's conflict-era governance is split between the "
                    "internationally recognized government (Aden) and Ansar Allah "
                    "(Houthi, Sana'a), with neither exercising effective control "
                    "over southern transit routes. Yemen's Anti-Trafficking Law "
                    "No. 1/2018 exists on paper but has never been enforced. The "
                    "UN Panel of Experts on Yemen has documented militia involvement "
                    "in migrant exploitation since 2018."
                ),
                "sector": "forced_labor",
                "corridor": "DJ-YE",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "Yemen's transit detention camps operate as systematic "
                    "extortion and forced labor facilities outside any legal "
                    "framework. The ransom model creates a perverse incentive: "
                    "migrants from families with remittance capacity are ransomed, "
                    "while those without are exploited for labor. IOM Yemen "
                    "documented 32 known transit detention points in Lahj and "
                    "Shabwah governorates in 2023, each holding 50-300 migrants. "
                    "The UN Special Rapporteur on trafficking reported in 2022 "
                    "that the Yemen transit route 'may constitute the largest "
                    "ongoing mass trafficking operation in the world by volume.'"
                ),
            },
            {
                "id": "mt008_s4",
                "description": (
                    "Migrants who pay ransom or complete forced labor periods are "
                    "moved northward through Yemen's interior to the Saudi border "
                    "region near Haradh (Hajjah governorate), where smugglers "
                    "facilitate border crossings into Saudi Arabia's Jizan and "
                    "Asir provinces. The Saudi-Yemen border crossing involves "
                    "evading Saudi Border Guard patrols and navigating mountainous "
                    "terrain for 12-48 hours. Saudi Border Guards have been "
                    "documented using lethal force against migrants at this border "
                    "— Human Rights Watch reported in August 2023 that Saudi guards "
                    "systematically killed and wounded Ethiopian migrants at the "
                    "border, with survivors describing explosive weapons and "
                    "close-range shootings. Those who survive the crossing arrive "
                    "in Saudi Arabia with no documents, no money, and injuries."
                ),
                "legal_basis": (
                    "Saudi Arabia's Border Security Law and regulations under the "
                    "Ministry of Interior authorize border enforcement. The "
                    "Saudi-Yemen Coordination Council has addressed border security "
                    "in the context of the Yemen conflict since 2015. Saudi Arabia's "
                    "Anti-Trafficking Law (Royal Decree M/40, 2009) provides for "
                    "victim identification but is not applied to irregular border "
                    "crossers, who are processed through the immigration enforcement "
                    "system."
                ),
                "sector": "transit_smuggling",
                "corridor": "YE-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The Saudi-Yemen border crossing carries a documented risk "
                    "of lethal violence. HRW's August 2023 report 'They Fired on "
                    "Us Like Rain' documented testimony from 38 Ethiopian migrants "
                    "who survived Saudi border guard shootings between March 2022 "
                    "and June 2023, with estimates of hundreds killed. Survivors "
                    "who enter Saudi Arabia are severely traumatized, undocumented, "
                    "and immediately vulnerable to exploitation by Saudi employers "
                    "who recruit undocumented workers at reduced wages."
                ),
            },
            {
                "id": "mt008_s5",
                "description": (
                    "In Saudi Arabia, surviving migrants find informal work in "
                    "agriculture (date palm farms in Jizan, vegetable farms in Asir), "
                    "domestic servitude, or construction in smaller Saudi cities. "
                    "Without documents, they accept wages of SAR 500-1,000/month "
                    "($133-$267), far below the Saudi minimum wage for foreign "
                    "workers. Employers can threaten to report them to Jawazat "
                    "(General Directorate of Passports) at any time. Saudi Arabia's "
                    "periodic regularization campaigns (e.g., the 2013 and 2017 "
                    "deportation waves) have forcibly deported over 750,000 Ethiopian "
                    "nationals since 2013. Deported workers return to Ethiopia "
                    "having lost their entire investment — ETB 30,000-80,000 to "
                    "the dalala, $100-300 for the boat, $1,000-3,000 in ransom — "
                    "often with physical injuries and severe trauma. Many attempt "
                    "the journey again within 6-12 months, restarting the cycle."
                ),
                "legal_basis": (
                    "Saudi Arabia's Labor Law (Royal Decree M/51) and Residency Law "
                    "(Royal Decree M/17) require valid iqama for employment. The "
                    "2013 Nitaqat enforcement campaign and 2017 deportation operations "
                    "were conducted under Article 39 of the Residency Law. IOM "
                    "facilitated the return of 115,000 Ethiopian migrants from "
                    "Saudi Arabia between 2017 and 2023 under a bilateral repatriation "
                    "agreement."
                ),
                "sector": "agriculture",
                "corridor": "YE-SA",
                "indicator_action_ids": [],
                "red_flag_context": (
                    "The cycle of exploitation, deportation, and re-migration is "
                    "the defining feature of this route. MMC 4Mi data shows that "
                    "28% of Ethiopian migrants on the Yemen route are repeat "
                    "migrants — people who have been deported from Saudi Arabia "
                    "and are attempting the journey again because debt from the "
                    "first attempt remains unpaid. IOM's 2023 flow monitoring "
                    "documented that deported returnees face social stigma, unpaid "
                    "debts, and poverty that drives re-migration within months. "
                    "The cumulative physical toll — desert crossing, Gulf of Aden "
                    "voyage, Yemen detention, Saudi border violence — produces "
                    "severe long-term health consequences documented by MSF "
                    "Ethiopia's treatment programs."
                ),
            },
        ],
        "chain_context": (
            "The Ethiopia-Djibouti-Yemen-Saudi Arabia route is the world's busiest "
            "mixed migration corridor by volume (92,000+ movements in 2023 per MMC "
            "data) and among the most lethal. It spans four countries across two "
            "continents, crossing one of the world's most active conflict zones (Yemen) "
            "and a border where lethal force against migrants has been documented by "
            "HRW. Ethiopia's labor migration system under Proclamation No. 923/2016 is "
            "designed for formal bilateral agreements (primarily ET-SA, ET-AE, ET-LB) "
            "and cannot reach the informal dalala-controlled irregular route. Djibouti's "
            "brief coastal transit provides the departure point but limited enforcement "
            "capacity against well-organized smuggling networks. Yemen's conflict has "
            "created a lawless transit zone where ransom, forced labor, and sexual "
            "violence are systematic. Saudi Arabia's border enforcement treats arriving "
            "migrants as immigration violators rather than trafficking victims. The "
            "cyclical nature of this route — exploitation, deportation, re-migration — "
            "means the same individuals may traverse the chain multiple times."
        ),
        "emergent_risk": (
            "Four-country smuggling-to-trafficking escalation: what begins as consensual "
            "migration from Ethiopia transforms into forced labor and extortion in Yemen "
            "and exploitation in Saudi Arabia, with deportation restarting the cycle "
            "rather than breaking it."
        ),
        "difficulty": "expert",
        "source_references": [
            "Mixed Migration Centre, '4Mi Quarterly Reports: East Africa & Yemen' (2022-2024) — 92,000 movements and exploitation prevalence data",
            "HRW, 'They Fired on Us Like Rain: Saudi Arabian Mass Killings of Ethiopian Migrants' (Aug 2023) — Saudi border guard lethal force documentation",
            "UNHCR, 'Gulf of Aden Maritime Crossings: 2023 Annual Report' — 73,000 arrivals and landing site exploitation patterns",
            "IOM, 'Flow Monitoring: Mixed Migration Routes from the Horn of Africa' (2023) — Djibouti-Yemen crossing data and repeat migration rates",
            "UN Special Rapporteur on Trafficking, 'Report on Mixed Migration and Trafficking: Yemen Transit Route' (2022) — mass trafficking characterization",
            "IOM Missing Migrants Project, 'Gulf of Aden and Sahara Routes 2014-2024' — fatality data across all transit segments",
        ],
        "corridors": ["ET-DJ", "DJ-YE", "YE-SA"],
        "palermo_elements": {
            "act": ["recruitment", "transportation", "transfer", "harbouring"],
            "means": [
                "threat or use of force",
                "coercion",
                "abduction",
                "abuse of position of vulnerability",
            ],
            "purpose": [
                "forced labour",
                "slavery or practices similar to slavery",
                "exploitation",
                "sexual exploitation",
            ],
        },
    },
]
