"""Gig economy and platform labor exploitation — ride-hailing (Uber, Grab, Bolt),
food delivery (Foodpanda, Deliveroo, DoorDash), data labeling (Scale AI, Appen),
content moderation (Accenture, Cognizant, Sama), and digital piecework platforms
(Amazon Mechanical Turk, Clickworker, Microworkers).

Sources:
- ILO World Employment and Social Outlook 2021: The Role of Digital Labour Platforms
- ILO Convention 181 (Private Employment Agencies, 1997)
- Fairwork Foundation Annual Ratings 2021-2025
- Uber BV v Aslam [2021] UKSC 5 (UK Supreme Court)
- Dynamex Operations West v. Superior Court, 4 Cal.5th 903 (2018)
- EU Directive 2024/2831 on Platform Work (adopted 14 Oct 2024)
- Spain Ley 12/2021 (Rider Law)
- FNV v. Deliveroo Netherlands, Hoge Raad (2023)
- TIME investigation: Inside Facebook's African Sweatshop (2022)
- Fairwork AI Ratings 2024 (data enrichment and AI training platforms)
- OECD Policy Brief: Platform Workers and the Future of Work (2023)
- World Bank Digital Economy for Africa (DE4A) data on gig labor
- ITF (International Transport Workers' Federation) ride-hailing guidance
- WHO/ILO Joint Estimates on Work-Related Burden of Disease (2021)
"""

GIG_ECONOMY_PLATFORM_LABOR_FACTS: list[dict] = [
    # =====================================================================
    # LAWS & REGULATIONS — EU
    # =====================================================================
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Platform Workers Directive 2024/2831 — Presumption of Employment",
        "summary": (
            "Directive 2024/2831, adopted 14 October 2024, establishes a rebuttable "
            "presumption of employment for platform workers when at least two of five "
            "control indicators are met (e.g., caps on pay, supervision of performance, "
            "restriction on working for competitors). Member States must transpose by "
            "December 2026. Covers an estimated 28.4 million platform workers across the EU."
        ),
        "law": "EU Directive 2024/2831",
        "year": 2024,
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "EU Platform Workers Directive — Algorithmic Management Transparency",
        "summary": (
            "Directive 2024/2831 mandates that platforms disclose automated decision-making "
            "systems affecting workers, including account deactivation criteria, performance "
            "rating algorithms, and task allocation logic. Workers gain the right to human "
            "review of algorithmic decisions. First EU-wide regulation of algorithmic "
            "management in employment."
        ),
    },
    # =====================================================================
    # LAWS & REGULATIONS — UNITED STATES
    # =====================================================================
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "California Assembly Bill 5 (AB5) — Gig Worker Classification 2019",
        "summary": (
            "AB5 codified the Dynamex ABC test for determining employee vs. independent "
            "contractor status. Under the ABC test, a worker is presumed an employee unless "
            "the hiring entity proves: (A) the worker is free from control, (B) performs "
            "work outside the usual course of the hiring entity's business, and (C) is "
            "engaged in an independently established trade. Directly targeted Uber, Lyft, "
            "DoorDash, and Instacart."
        ),
        "law": "California AB5 (Labor Code §2775)",
        "year": 2019,
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "California Proposition 22 — App-Based Drivers as Contractors 2020",
        "summary": (
            "Proposition 22, passed by California voters in November 2020, exempted app-based "
            "rideshare and delivery drivers from AB5, classifying them as independent "
            "contractors with limited benefits: guaranteed 120% of local minimum wage for "
            "engaged time only, $0.30/mile vehicle stipend, and healthcare subsidy for those "
            "averaging 25+ hours/week. Uber, Lyft, DoorDash, and Instacart spent USD 205 "
            "million supporting the ballot measure — the most expensive in California history."
        ),
        "law": "California Proposition 22",
        "year": 2020,
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Castellanos v. State of California [2024] — Prop 22 Partially Upheld",
        "court": "California Court of Appeal, First District",
        "year": 2024,
        "summary": (
            "The California Court of Appeal largely upheld Proposition 22 in March 2024, "
            "reversing a lower court ruling that had found it unconstitutional. The appeals "
            "court struck down only the provision requiring a seven-eighths supermajority of "
            "the legislature to amend the measure, preserving the core classification of "
            "app-based drivers as independent contractors."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "US Department of Labor Final Rule — Independent Contractor Status 2024",
        "summary": (
            "DOL final rule effective March 2024 replaced the Trump-era 2021 rule with a "
            "six-factor economic reality test for classifying workers under the Fair Labor "
            "Standards Act. Factors include opportunity for profit/loss, degree of control, "
            "investment, permanence, skill required, and integration into business. "
            "Expected to make it harder for gig platforms to classify workers as contractors."
        ),
        "law": "29 CFR Part 795 (DOL Final Rule, 89 FR 1638)",
        "year": 2024,
    },
    # =====================================================================
    # LAWS & REGULATIONS — UK
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Uber BV v Aslam [2021] UKSC 5 — Workers Not Self-Employed",
        "court": "Supreme Court of the United Kingdom",
        "year": 2021,
        "summary": (
            "The UK Supreme Court unanimously held that Uber drivers are 'workers' under "
            "the Employment Rights Act 1996, entitled to minimum wage, paid holidays, and "
            "whistleblower protections. The Court found that Uber set fares, imposed "
            "contractual terms, constrained drivers' ability to build relationships with "
            "passengers, and penalized low acceptance rates. Working time begins when the "
            "app is switched on and the driver is ready to accept trips."
        ),
    },
    # =====================================================================
    # LAWS & REGULATIONS — SPAIN
    # =====================================================================
    {
        "type": "law",
        "jurisdiction": "ES",
        "title": "Spain Ley 12/2021 (Rider Law) — Delivery Platform Employment Presumption",
        "summary": (
            "Ley 12/2021, effective 12 August 2021, established a legal presumption of "
            "employment for delivery platform workers. Platforms must also provide worker "
            "representatives with algorithmic parameters affecting working conditions. "
            "Spain was the first EU country to legislate specifically on platform worker "
            "status. Prompted Deliveroo to exit Spain and Glovo to hire 10,000+ riders "
            "as employees."
        ),
        "law": "Ley 12/2021 (Real Decreto-ley 9/2021)",
        "year": 2021,
    },
    # =====================================================================
    # LAWS & REGULATIONS — FRANCE
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Uber France SAS — Cour de Cassation Employment Reclassification 2020",
        "court": "Cour de Cassation (French Supreme Court)",
        "year": 2020,
        "summary": (
            "Cour de Cassation ruled in March 2020 that a former Uber driver was an employee, "
            "not a self-employed contractor. The Court found that Uber set fares, controlled "
            "itineraries, and could disconnect drivers who refused rides, creating a "
            "subordination relationship. First French Supreme Court ruling on platform worker "
            "employment status. Affected an estimated 30,000 Uber drivers in France."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "FR",
        "title": "France Loi El Khomri — Platform Worker Social Protections 2016",
        "summary": (
            "Articles L.7341-1 to L.7342-6 of the Labour Code, introduced by the Loi "
            "Travail (El Khomri Law) in 2016, gave platform workers the right to vocational "
            "training, accident insurance, and collective organization. However, it stopped "
            "short of reclassifying workers as employees, creating a 'third category' of "
            "platform-dependent workers."
        ),
        "law": "Loi 2016-1088 (Code du travail L.7341-1 to L.7342-6)",
        "year": 2016,
    },
    # =====================================================================
    # LAWS & REGULATIONS — SINGAPORE
    # =====================================================================
    {
        "type": "law",
        "jurisdiction": "SG",
        "title": "Singapore Platform Workers Act 2024",
        "summary": (
            "Enacted in September 2024, the Platform Workers Act extends workplace injury "
            "compensation and CPF (Central Provident Fund) contributions to platform workers "
            "in ride-hailing and delivery. Platform operators must co-contribute alongside "
            "workers. Does not reclassify workers as employees but creates a new 'platform "
            "worker' category with targeted protections. Applies to approximately 70,000 "
            "workers on Grab, Gojek, Foodpanda, and Deliveroo in Singapore."
        ),
        "law": "Platform Workers Act 2024 (No. 26 of 2024)",
        "year": 2024,
    },
    # =====================================================================
    # LAWS & REGULATIONS — INDIA, BRAZIL, SOUTH KOREA, AUSTRALIA
    # =====================================================================
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "India Code on Social Security 2020 — Gig and Platform Worker Provisions",
        "summary": (
            "The Code on Social Security 2020 is the first Indian legislation to define "
            "'gig worker' and 'platform worker' as distinct categories. Provides for social "
            "security fund contributions by aggregators at 1-2% of annual turnover. Covers "
            "life and disability insurance, health and maternity benefits, and old age "
            "protection. Implementation has stalled; central government rules not yet "
            "notified as of 2025. Affects an estimated 7.7 million gig workers in India."
        ),
        "law": "Code on Social Security 2020 (Chapter IX, Sections 113-114)",
        "year": 2020,
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "Brazil Superior Tribunal de Justica — Uber Driver Not Employee 2023",
        "court": "Superior Tribunal de Justica (STJ)",
        "year": 2023,
        "summary": (
            "The STJ ruled in May 2023 that Uber drivers are not employees under Brazilian "
            "labor law (CLT), finding insufficient subordination. However, Brazilian labor "
            "courts continue to issue conflicting rulings: the Sao Paulo Regional Labor "
            "Court recognized employment relationships in multiple cases in 2022-2023. "
            "The Supreme Federal Tribunal (STF) accepted the case for definitive ruling, "
            "still pending as of 2025."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "KR",
        "title": "South Korea Platform Workers Protection Act — Proposed 2023",
        "summary": (
            "Proposed legislation to guarantee platform workers minimum protections "
            "including transparent contract terms, advance notice of contract changes, "
            "accident insurance, and restrictions on unfair algorithmic deactivation. "
            "Debated in the National Assembly since 2022. South Korea has an estimated "
            "2.2 million platform workers, heavily concentrated in delivery (Coupang Eats, "
            "Baemin) and ride-hailing (Kakao T)."
        ),
        "law": "Platform Workers Protection Act (proposed)",
        "year": 2023,
    },
    {
        "type": "regulation_change",
        "jurisdiction": "AU",
        "title": "Australia Fair Work Amendment — Gig Economy Regulation 2024",
        "summary": (
            "The Fair Work Legislation Amendment (Closing Loopholes No. 2) Act 2024 gave "
            "the Fair Work Commission power to set minimum standards for 'employee-like' "
            "gig workers including minimum pay, maximum deductions, and dispute resolution. "
            "Covers ride-hailing and food delivery platforms. First orders expected to apply "
            "to workers on Uber, Ola, DoorDash, and Menulog from late 2025."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "CL",
        "title": "Chile Ley 21.431 — Plataformas Digitales (Digital Platform Workers) 2022",
        "summary": (
            "Chile enacted Ley 21.431 in March 2022, creating a legal framework for platform "
            "workers. Workers can be classified as dependent (employees) or independent "
            "(contractors), but platforms must provide accident insurance and transparent "
            "algorithmic information regardless of classification. Covers ride-hailing "
            "(Uber, Didi, Cabify) and delivery (Rappi, PedidosYa) workers."
        ),
        "law": "Ley 21.431",
        "year": 2022,
    },
    {
        "type": "law",
        "jurisdiction": "CO",
        "title": "Colombia Decreto 555 — Platform Worker Social Protection Pilot 2024",
        "summary": (
            "Colombia launched a pilot regulatory framework in 2024 requiring delivery and "
            "ride-hailing platforms (Rappi, Uber, DiDi, InDriver) to contribute to worker "
            "social protection including health insurance and pension. Platforms contribute "
            "a percentage of each transaction. Covers an estimated 120,000 platform workers "
            "in Bogota alone."
        ),
        "law": "Decreto 555 de 2024",
        "year": 2024,
    },
    # =====================================================================
    # COURT RULINGS — EUROPEAN NATIONAL COURTS
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "FNV v. Deliveroo Netherlands — Supreme Court Employment Ruling 2023",
        "court": "Hoge Raad (Dutch Supreme Court)",
        "year": 2023,
        "summary": (
            "The Dutch Supreme Court confirmed in March 2023 that Deliveroo riders in the "
            "Netherlands are employees, not independent contractors. The Hoge Raad applied "
            "a holistic assessment of the working relationship, finding that algorithmic "
            "control, performance monitoring, bonuses for working during peak times, and "
            "inability to build independent client relationships established employment. "
            "Deliveroo subsequently exited the Netherlands in November 2022."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Foodora/Deliveroo Italy — Corte di Cassazione Rider Employment 2020",
        "court": "Corte di Cassazione (Italian Supreme Court)",
        "year": 2020,
        "summary": (
            "The Italian Supreme Court ruled in January 2020 that food delivery riders "
            "for Foodora (later acquired by Deliveroo) are entitled to employee-equivalent "
            "protections under Article 2 of Legislative Decree 81/2015. The Court applied "
            "the 'hetero-organized collaboration' framework: when work is organized by the "
            "platform regarding time, place, and manner, workers enjoy full employment "
            "protections regardless of contractual label."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Uber Belgium — Brussels Labour Court 2023",
        "court": "Brussels Labour Court (Tribunal du travail)",
        "year": 2023,
        "summary": (
            "The Brussels Labour Court ruled in November 2023 that Uber drivers in Belgium "
            "are employees. The court found that Uber exercised authority over drivers "
            "through fare-setting, GPS tracking, driver ratings with deactivation risk, and "
            "algorithmic ride assignment. Uber appealed the decision."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Dynamex Operations West v. Superior Court [2018] — ABC Test",
        "court": "Supreme Court of California",
        "year": 2018,
        "summary": (
            "The California Supreme Court adopted the ABC test for determining worker "
            "classification, shifting the burden to hiring entities to prove independent "
            "contractor status. The test presumes employment unless all three prongs are "
            "satisfied. This landmark decision directly led to AB5 legislation and affected "
            "millions of gig workers across California's platform economy."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Roamler/Clickworker — German Federal Labour Court Crowdworker Ruling 2020",
        "court": "Bundesarbeitsgericht (Federal Labour Court of Germany)",
        "year": 2020,
        "summary": (
            "The German Federal Labour Court ruled in December 2020 that a crowdworker "
            "performing microtasks on the Roamler platform was an employee. The Court "
            "found that the platform's gamification system (levels, experience points, "
            "access to higher-paying tasks) created dependency and personal subordination. "
            "First German high court ruling recognizing digital platform worker as employee."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Glovo Spain — Tribunal Supremo Employment Ruling 2020",
        "court": "Tribunal Supremo (Spanish Supreme Court)",
        "year": 2020,
        "summary": (
            "The Spanish Supreme Court ruled in September 2020 that a Glovo delivery rider "
            "was an employee. The Court found that Glovo controlled essential elements of "
            "the service: the app determined pricing, assigned orders via algorithm, tracked "
            "GPS location, and penalized riders who rejected deliveries. This ruling preceded "
            "and catalyzed the Ley Rider legislation enacted in 2021."
        ),
    },
    # =====================================================================
    # COURT RULINGS — GLOBAL SOUTH
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "ZA",
        "title": "NUPSAW v. Uber South Africa — CCMA Jurisdiction Ruling 2018",
        "court": "Commission for Conciliation, Mediation and Arbitration (CCMA)",
        "year": 2018,
        "summary": (
            "South Africa's CCMA ruled that Uber drivers are employees, not independent "
            "contractors, granting the commission jurisdiction over unfair dismissal claims. "
            "Uber appealed to the Labour Court, which overturned the ruling in 2019 on "
            "procedural grounds. The substantive question of platform worker status remains "
            "unsettled in South African law."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KE",
        "title": "Uber Kenya — Employment and Labour Relations Court 2022",
        "court": "Employment and Labour Relations Court of Kenya",
        "year": 2022,
        "summary": (
            "Kenyan court ruled in 2022 that an Uber driver was in an employment "
            "relationship, ordering reinstatement and compensation after deactivation. "
            "The judge found that Uber's unilateral power to deactivate accounts, set "
            "fares, and impose behavioral requirements constituted employer authority. "
            "Decision not binding nationally but set persuasive precedent."
        ),
    },
    # =====================================================================
    # CASE STUDIES — RIDE-HAILING ACCOUNT RENTAL SCHEMES
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Uber/Grab Account Rental Schemes in Singapore — Migrant Driver Exploitation",
        "summary": (
            "Migrant workers in Singapore unable to obtain ride-hailing licenses rent "
            "activated Grab and former-Uber accounts from Singaporean citizens or PRs for "
            "SGD 500-1,500/month. Account 'owners' take 20-30% of gross earnings. Renters "
            "have no insurance coverage, no accident protection, and face deportation if "
            "caught. LTA enforcement in 2022 identified 127 cases; actual prevalence "
            "estimated at 5-10% of active drivers."
        ),
        "source": "Straits Times / Land Transport Authority Singapore 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Grab Account Brokerage in Malaysia — Indonesian and Bangladeshi Drivers",
        "summary": (
            "Malaysian intermediaries sell activated Grab driver accounts to undocumented "
            "Indonesian and Bangladeshi migrants for MYR 3,000-8,000. Workers drive 14-16 "
            "hours daily to recoup investment, earning below minimum wage after account "
            "rental fees, vehicle rental, and fuel. Grab's facial recognition checks are "
            "bypassed using photo spoofing. MTUC reported 300+ complaints in 2023."
        ),
        "source": "Malay Mail / MTUC Malaysia / Grab safety reports 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Grab Driver Recruitment Intermediaries in Indonesia — $2,000+ Activation Fees",
        "summary": (
            "In Jakarta and Surabaya, intermediaries charge aspiring Grab and Gojek drivers "
            "IDR 30-50 million (USD 2,000-3,300) for account activation, vehicle rental, "
            "and guaranteed onboarding. Drivers must work exclusively through the intermediary "
            "for 6-12 months to 'repay' the fee, receiving only 40-50% of ride earnings. "
            "Those who attempt to leave face threats and account deactivation. Pattern "
            "mirrors traditional debt bondage in digital form."
        ),
        "source": "Tirto.id / Fairwork Indonesia Report 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Bolt Drivers in Nigeria — Daily Fee Extraction by Account Owners",
        "summary": (
            "Bolt drivers in Lagos and Abuja commonly operate under 'car owner' arrangements "
            "where they pay NGN 8,000-15,000/day (USD 10-18) to vehicle/account owners "
            "regardless of earnings. Drivers report working 16+ hours to clear the daily "
            "fee and earn personal income. Account owners control deactivation and can "
            "replace drivers at will. A 2023 survey by the Nigeria Labour Congress found "
            "68% of sampled Bolt drivers earned below national minimum wage after fees."
        ),
        "source": "Nigeria Labour Congress / Premium Times 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "GB",
        "title": "Uber Eats Account Rental in UK — BBC Investigation 2021",
        "summary": (
            "A 2021 BBC investigation revealed widespread rental of Uber Eats delivery "
            "accounts to undocumented workers in London, Birmingham, and Manchester. "
            "Accounts sold for GBP 50-200/week. Workers had no right-to-work verification, "
            "no insurance, and no access to Uber's safety features. When one renter was "
            "killed in a traffic accident, the account holder's identity complicated "
            "investigation and insurance claims."
        ),
        "source": "BBC News Investigation / Uber Response Statement 2021",
    },
    # =====================================================================
    # CASE STUDIES — FOOD DELIVERY EXPLOITATION
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Foodpanda Rider Debt Bondage in Hong Kong — Account Intermediaries",
        "summary": (
            "Foodpanda riders in Hong Kong, predominantly South Asian asylum seekers "
            "legally barred from employment, purchase or rent activated rider accounts from "
            "intermediaries at HKD 4,000-12,000 (USD 500-1,500). Account holders take "
            "30-40% of weekly earnings. Riders work 10-14 hours daily with no accident "
            "insurance. Justice Centre Hong Kong documented 89 cases in 2022 where riders "
            "were trapped in debt cycles to account brokers."
        ),
        "source": "Justice Centre Hong Kong / SCMP / Foodpanda Investigations 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Foodpanda Riders in Pakistan — Algorithmic Wage Suppression",
        "summary": (
            "Foodpanda riders in Karachi and Lahore reported piece rates dropping from "
            "PKR 80/delivery (2020) to PKR 45/delivery (2023) — a 44% reduction — while "
            "delivery distances increased. Riders work 12-14 hours to earn PKR 800-1,200 "
            "(USD 2.80-4.20). Platform imposed 'incentive zones' requiring minimum 90% "
            "acceptance rate, effectively eliminating rider autonomy. Pakistani Riders "
            "Alliance organized protests in 2023 involving 3,000+ riders."
        ),
        "source": "Pakistan Riders Alliance / Dawn News / Fairwork Pakistan 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "DoorDash Tip Theft — Base Pay Adjustment Wage Manipulation",
        "summary": (
            "DoorDash's pre-2019 pay model used customer tips to subsidize base pay: a "
            "USD 10 tip on a delivery guaranteed USD 10 would result in DoorDash paying "
            "only USD 1 base instead of its standard USD 6-8. Worker advocacy led to a "
            "2019 pay model change, but a 2020 lawsuit by Washington DC Attorney General "
            "resulted in a USD 2.5 million settlement. Similar suits filed in 6 states."
        ),
        "source": "Washington DC Attorney General / New York Times 2019-2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Zomato/Swiggy Delivery Workers in India — 10-Minute Delivery Pressure",
        "summary": (
            "Indian food delivery platforms introduced '10-minute delivery' (Zomato Instant, "
            "Swiggy Instamart) in 2022, creating extreme time pressure. Indian Federation "
            "of App-based Transport Workers (IFAT) reported 14 delivery worker road deaths "
            "in Bengaluru alone during 2022-2023. Workers earn INR 15-25 (USD 0.18-0.30) per "
            "delivery, below vehicle operating costs. No workers' compensation for accidents."
        ),
        "source": "IFAT / Newslaundry / Rest of World 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "iFood Delivery Workers in Brazil — Breque dos Apps Strike 2020",
        "summary": (
            "Brazilian delivery workers launched the 'Breque dos Apps' (App Brake) strike "
            "in July 2020, the largest platform worker strike in Latin American history. "
            "Riders on iFood, Rappi, and Uber Eats demanded minimum per-delivery pay of "
            "BRL 5 (USD 1), end to unjust account blocks, and accident insurance. Over "
            "50,000 riders participated across 12 cities. iFood subsequently raised base "
            "pay by 15% but did not meet core demands."
        ),
        "source": "Reuters / Folha de Sao Paulo / UNICAMP Labour Studies 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "ES",
        "title": "Deliveroo Spain Exit — Post-Rider Law Market Withdrawal 2021",
        "summary": (
            "Deliveroo withdrew from Spain in November 2021 following the Ley Rider, which "
            "mandated employee classification for delivery riders. Deliveroo stated compliance "
            "costs made the Spanish market 'unviable.' Rival Glovo hired over 10,000 riders "
            "as employees. The Spanish Labour Inspectorate subsequently fined Glovo EUR 79 "
            "million in 2022 for historic misclassification of 10,600 riders."
        ),
        "source": "Financial Times / El Pais / Spanish Labour Inspectorate 2021-2022",
    },
    {
        "type": "penalty",
        "jurisdiction": "ES",
        "title": "Glovo Spain — EUR 79 Million Misclassification Fine 2022",
        "offense": "Systematic misclassification of 10,600 delivery riders as self-employed",
        "amount": "EUR 79 million",
        "summary": (
            "Spanish Labour Inspectorate fined Glovo EUR 79 million in September 2022 for "
            "employing 10,600 delivery riders as false self-employed (falsos autonomos) "
            "between 2018 and 2021, prior to the Rider Law. Fine covered unpaid social "
            "security contributions. Largest gig economy fine in European history."
        ),
    },
    # =====================================================================
    # CASE STUDIES — DATA LABELING AND AI TRAINING
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KE",
        "title": "Scale AI/Remotasks Data Labelers in Kenya — Below-Subsistence Pay",
        "summary": (
            "TIME (2023) investigation revealed Scale AI's Remotasks platform pays Kenyan "
            "data labelers USD 1-3/hour for AI training annotation tasks, including "
            "labeling images, categorizing text, and rating chatbot outputs for clients "
            "including OpenAI and Meta. Workers report unpaid tasks rejected by quality "
            "checks, account suspensions without explanation, and effective hourly rates "
            "dropping below USD 1 after unpaid work is factored in."
        ),
        "source": "TIME Magazine Investigation 2023 / Partnership on AI Report 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "KE",
        "title": "Sama (formerly Samasource) Content Moderators for ChatGPT — PTSD and Low Pay",
        "summary": (
            "TIME (2022) revealed that Sama employed Kenyan workers at USD 1.32-2.00/hour "
            "to label toxic content — including child sexual abuse, bestiality, murder, and "
            "suicide — for OpenAI's ChatGPT safety training. Workers developed PTSD, anxiety, "
            "and depression. Sama terminated its content moderation contract in February 2022 "
            "citing ethical concerns. Multiple former employees filed complaints."
        ),
        "source": "TIME Magazine 'Inside Facebook's African Sweatshop' 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "VE",
        "title": "Appen/Figure Eight Venezuelan Data Workers — Hyperinflation-Exploited Labor",
        "summary": (
            "Venezuelan workers on Appen (formerly Figure Eight/CrowdFlower) perform AI "
            "training tasks — image annotation, sentiment analysis, audio transcription — "
            "earning USD 1-4/day. Venezuela's hyperinflation makes even these rates "
            "attractive. Workers report tasks rejected without explanation, delayed payments "
            "of 30-90 days, and unilateral pay rate reductions. No grievance mechanism "
            "or labor protections apply across borders."
        ),
        "source": "Rest of World / Wired / MIT Technology Review 2022-2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Amazon Mechanical Turk Workers in India — Below Local Minimum Wage",
        "summary": (
            "Indian MTurk workers, estimated at 100,000+, earn a median of INR 100-200 "
            "(USD 1.20-2.40) per hour, below the Delhi minimum wage of INR 240/hour "
            "(USD 2.90). A 2023 Oxford Internet Institute study found 40% of Indian "
            "turkers earned below USD 1.50/hour after accounting for unpaid qualification "
            "tasks and rejected HITs. Amazon takes a 20-40% platform fee on all tasks."
        ),
        "source": "Oxford Internet Institute / iLabour Project 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Clickworker and Microworkers Filipino Labelers — Piecework Below Minimum Wage",
        "summary": (
            "Filipino workers on Clickworker, Microworkers, and Toloka perform microtasks "
            "(CAPTCHA solving, data categorization, image tagging) earning PHP 10-30 "
            "(USD 0.18-0.54) per task. Workers complete 50-100 tasks/day for daily earnings "
            "of PHP 500-1,500 (USD 9-27). No contracts, no benefits, no minimum wage "
            "protections. Tasks can be rejected retroactively with no payment. Estimated "
            "500,000+ Filipino crowdworkers across platforms."
        ),
        "source": "Fairwork Cloudwork Ratings 2023 / IBON Foundation Philippines",
    },
    {
        "type": "case_study",
        "jurisdiction": "UG",
        "title": "Data Annotation Workers in Uganda — AI Training for Western Companies",
        "summary": (
            "Ugandan workers in Kampala data annotation centers label images and text for "
            "self-driving car companies and facial recognition systems. Workers earn "
            "UGX 5,000-15,000 (USD 1.30-4.00) per day for 8-10 hour shifts. Labor "
            "rights organization Pollicy (2023) documented instances of workers being "
            "required to label graphic violence, self-harm, and sexual content without "
            "psychological support or content warnings."
        ),
        "source": "Pollicy Uganda / The Guardian / Data Workers' Inquiry 2023",
    },
    # =====================================================================
    # CASE STUDIES — CONTENT MODERATION
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Accenture/Cognizant Content Moderators in Philippines — PTSD and Mental Health",
        "summary": (
            "Content moderators employed by Accenture and Cognizant in Manila review "
            "5,000-8,000 posts daily for Facebook/Meta, including beheadings, child abuse, "
            "and torture. Employees earn PHP 25,000-35,000/month (USD 450-630). A 2023 class "
            "action in California (Motaung v. Meta) alleged negligent infliction of emotional "
            "distress. Meta settled with US content moderators for USD 52 million in 2020 but "
            "Philippine workers received no compensation."
        ),
        "source": "The Verge / Washington Post / Motaung v. Meta Platforms 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "KE",
        "title": "Majorel/Teleperformance Content Moderators in Nairobi — TikTok Moderation",
        "summary": (
            "Majorel (now Teleperformance) moderators in Nairobi reviewing content for "
            "TikTok earn KES 30,000-50,000/month (USD 200-330). Workers view 500+ graphic "
            "videos daily. A 2023 lawsuit (Motaung v. Meta) brought attention to Nairobi "
            "operations. Workers reported mandatory 'wellness breaks' of 5 minutes per hour "
            "insufficient for trauma exposure. Turnover rates exceed 70% annually."
        ),
        "source": "TIME / Bureau of Investigative Journalism / Foxglove Legal 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "CO",
        "title": "Content Moderation BPOs in Colombia — Spanish-Language Platform Workers",
        "summary": (
            "Bogota has become a hub for Spanish-language content moderation for Meta, "
            "Google, and TikTok through BPO firms (Teleperformance, TaskUs). Workers earn "
            "COP 2-3 million/month (USD 500-750), moderate for multiple brands, and face "
            "NDA-enforced silence about working conditions. Fairwork Colombia (2023) rated "
            "content moderation as the lowest-scoring gig work category for fair conditions."
        ),
        "source": "Fairwork Colombia Report 2023 / Cuestiones de Trabajo 2023",
    },
    # =====================================================================
    # STATISTICS
    # =====================================================================
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO Global Platform Worker Estimate 2021",
        "metric": "Number of workers earning income through digital labor platforms",
        "value": "777 million potential workers; active: approx. 163 million",
        "year": 2021,
        "details": (
            "ILO World Employment and Social Outlook 2021 estimated a fivefold increase "
            "in platform workers from 2010 to 2020. Web-based (crowdwork/freelance) "
            "platforms account for 60%, location-based (ride-hailing/delivery) 40%. "
            "Highest growth in South and Southeast Asia."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Fairwork Annual Platform Ratings 2024 — Global Working Conditions",
        "metric": "Average Fairwork score across rated platforms (out of 10)",
        "value": "3.2/10 global average",
        "year": 2024,
        "details": (
            "Fairwork rated 82 platforms across 38 countries in 2024 on five principles: "
            "fair pay, fair conditions, fair contracts, fair management, and fair "
            "representation. Global average was 3.2/10, down from 3.5/10 in 2023. Lowest "
            "scores in Sub-Saharan Africa (1.8/10 avg) and South Asia (2.1/10 avg). "
            "Highest in Northern Europe (6.4/10 avg)."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Platform Worker Earnings vs. Minimum Wage — Global Comparison 2023",
        "metric": "Percentage of platform workers earning below local minimum wage",
        "value": "58% of platform workers globally",
        "year": 2023,
        "details": (
            "ILO/Fairwork joint analysis (2023) found that 58% of platform workers in "
            "surveyed countries earned below local minimum wage after accounting for "
            "platform fees, waiting time, vehicle costs, and unpaid tasks. Rate was "
            "highest for crowdwork (71%) and food delivery (63%), lowest for ride-hailing "
            "(48%)."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "IN",
        "title": "India Gig Economy Size — NITI Aayog Estimate 2022",
        "metric": "Number of gig workers in India",
        "value": "7.7 million (2020-2021), projected 23.5 million by 2029-2030",
        "year": 2022,
        "details": (
            "NITI Aayog report (2022) estimated 7.7 million gig workers in India, "
            "constituting 1.5% of total workforce. 26.6% in transportation, 12.8% in "
            "retail and sales, 10.3% in manufacturing. Report recommended universal social "
            "security, occupational safety codes, and platform accountability for gig workers."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Delivery Rider Fatalities — Global Estimate 2021-2023",
        "metric": "Reported delivery rider work-related deaths globally",
        "value": "488 documented deaths (2021-2023, partial data)",
        "year": 2023,
        "details": (
            "The International Transport Workers' Federation compiled 488 documented "
            "delivery rider fatalities across 32 countries from 2021-2023, primarily from "
            "road traffic accidents. India (134), Brazil (97), China (71), and Indonesia "
            "(43) reported highest numbers. True figure likely much higher due to "
            "underreporting and classification as personal rather than work accidents."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "US Gig Economy Worker Estimate — Bureau of Labor Statistics 2023",
        "metric": "Workers in electronically mediated work arrangements",
        "value": "16.4 million (9.6% of employed adults)",
        "year": 2023,
        "details": (
            "BLS Contingent Worker Supplement (2023) found 16.4 million US workers in "
            "electronically mediated arrangements. 5.7 million as primary income source. "
            "Median earnings USD 510/week for app-based drivers, compared to USD 1,100/week "
            "for employee taxi/delivery drivers with benefits."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "EU Platform Economy Size — European Commission Impact Assessment 2024",
        "metric": "Number of platform workers in the European Union",
        "value": "28.4 million (up from 11 million in 2016)",
        "year": 2024,
        "details": (
            "European Commission estimated 28.4 million platform workers in the EU, "
            "projected to reach 43 million by 2025. Approximately 5.5 million are at "
            "risk of employment misclassification. Spain (3.2M), Germany (3.0M), France "
            "(2.8M), and Italy (2.5M) are the largest markets."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "KE",
        "title": "Data Labeling Worker Earnings in Kenya — TIME Investigation 2023",
        "metric": "Median hourly earnings for AI training data labelers in Nairobi",
        "value": "USD 1.32-2.00/hour",
        "year": 2023,
        "details": (
            "TIME investigation (2023) documented median earnings of USD 1.32-2.00/hour "
            "for Kenyan data labelers working for Scale AI, Sama, and CloudFactory. "
            "Workers labeled training data for OpenAI, Meta, Google, and Microsoft. "
            "Kenya minimum wage for Nairobi is KES 15,201/month (approx. USD 1.10/hour). "
            "Many workers earned near or below minimum wage after accounting for unpaid "
            "rejected tasks."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Fairwork AI Ratings 2024 — Data Enrichment Platform Scores",
        "metric": "Average Fairwork score for AI/data enrichment platforms (out of 10)",
        "value": "1.7/10 average across 15 rated platforms",
        "year": 2024,
        "details": (
            "Fairwork AI Ratings (2024) assessed 15 AI/data enrichment platforms including "
            "Scale AI (1/10), Appen (2/10), Toloka (1/10), Amazon Mechanical Turk (0/10), "
            "and Clickworker (2/10). Only Prolific (7/10) and Dynata (5/10) scored above "
            "5. Common failures: no guaranteed minimum wage, no appeal for task rejections, "
            "no worker consultation on algorithmic changes."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Content Moderator Mental Health Impact — Meta Settlement Data 2020",
        "metric": "Content moderators diagnosed with PTSD or related conditions",
        "value": "Estimated 11,000+ affected workers (2015-2020)",
        "year": 2020,
        "details": (
            "Meta's USD 52 million settlement (2020) with US content moderators provided "
            "for psychological screening and compensation for approximately 11,000 current "
            "and former workers. Individual payments of USD 1,000-50,000 based on diagnosis "
            "severity. Studies show content moderator PTSD rates comparable to combat "
            "veterans (12-28%)."
        ),
    },
    # =====================================================================
    # ADVISORIES — INTERNATIONAL ORGANIZATIONS
    # =====================================================================
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO World Employment and Social Outlook 2021 — Platform Labour Recommendations",
        "summary": (
            "ILO's 2021 report on digital labour platforms recommended: (1) extending "
            "labour protections to all platform workers regardless of classification, "
            "(2) ensuring platform earnings meet minimum wage standards including waiting "
            "time, (3) making platforms jointly liable for workplace injuries, (4) "
            "requiring algorithmic transparency, and (5) enabling platform workers to "
            "organize collectively. The report emphasized that platform work reproduces "
            "and amplifies existing labor market inequalities."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Fairwork Foundation Assessment Principles — Five Fair Work Standards",
        "summary": (
            "The Fairwork Foundation (Oxford Internet Institute) rates platforms on five "
            "principles: (1) Fair Pay — earnings above minimum wage after costs, "
            "(2) Fair Conditions — safety net for task-specific risks, "
            "(3) Fair Contracts — transparent, understandable terms without liability "
            "exclusions, (4) Fair Management — due process for deactivation, "
            "non-discriminatory algorithms, (5) Fair Representation — recognized worker "
            "voice. Each principle scored 0-2, total 0-10."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "OECD Policy Brief — Platform Workers and Future of Work 2023",
        "summary": (
            "OECD (2023) recommended extending core labor protections to platform workers "
            "by: (1) lowering the threshold for employment classification, (2) creating "
            "portable benefits decoupled from single employers, (3) mandating algorithmic "
            "transparency requirements, (4) strengthening labor inspection capacity for "
            "digital workplaces, (5) enabling collective bargaining without competition "
            "law barriers. Noted that current frameworks leave 55-65% of OECD platform "
            "workers without basic social protections."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ITF Guidance on Ride-Hailing Worker Rights 2022",
        "summary": (
            "International Transport Workers' Federation (2022) guidance called for: "
            "(1) guaranteed minimum earnings per hour including waiting time, "
            "(2) mandatory accident and health insurance paid by platforms, "
            "(3) transparent fare calculation and commission structures, "
            "(4) right to refuse rides without penalty, "
            "(5) due process before account deactivation, "
            "(6) recognition of driver unions and associations. "
            "ITF represents 18.5 million transport workers across 147 countries."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "WHO/ILO Joint Estimates — Delivery Worker Occupational Safety 2021",
        "summary": (
            "WHO and ILO joint estimates (2021) found that food delivery and ride-hailing "
            "workers face 3.4x higher risk of road traffic injuries than the general "
            "working population. Factors include time-pressure algorithms, piece-rate pay "
            "incentivizing speed, lack of safety training, and inadequate vehicle "
            "maintenance. Report recommended platform liability for worker safety "
            "outcomes and mandatory insurance coverage."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Partnership on AI — Responsible Sourcing of Data Enrichment Services 2024",
        "summary": (
            "Partnership on AI (2024) guidelines for responsible data enrichment recommended: "
            "(1) minimum hourly pay of at least living wage in worker's location, "
            "(2) transparent task rejection criteria with appeal mechanisms, "
            "(3) content warnings and mental health support for harmful content labeling, "
            "(4) limiting exposure to graphic content to 4 hours/day maximum, "
            "(5) providing benefits including health insurance for regular workers. "
            "Endorsed by Microsoft and Google but not Amazon or Meta."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO R198 Employment Relationship Recommendation — Application to Platforms 2023",
        "summary": (
            "ILO Committee of Experts (2023) interpreted Recommendation 198 (Employment "
            "Relationship, 2006) as applicable to platform work, advising that: digital "
            "control indicators (algorithmic management, GPS tracking, performance ratings) "
            "should be considered in determining employment status; contractual labels "
            "should not override factual working arrangements; the burden of proof should "
            "shift to platforms to demonstrate genuine self-employment."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "World Bank Pathways Report — Gig Economy in Developing Countries 2023",
        "summary": (
            "World Bank (2023) analysis of gig economy in 40 developing countries found: "
            "platform work provides entry to formal income for previously informal workers "
            "but typically without improvement in social protection. Average platform worker "
            "in Sub-Saharan Africa earns USD 3.40/day; in South Asia USD 4.80/day. "
            "Recommended conditional licensing of platforms based on worker protection "
            "standards."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UN Special Rapporteur on Contemporary Forms of Slavery — Digital Platforms 2022",
        "summary": (
            "UN Special Rapporteur Tomoya Obokata (2022) warned that certain platform work "
            "arrangements exhibit characteristics of forced labor under the ILO definition: "
            "menace of penalty (account deactivation, loss of ratings), involuntariness "
            "(debt to intermediaries, lack of alternative employment), and exploitation "
            "(below-subsistence pay). Called for platform accountability under UN Guiding "
            "Principles on Business and Human Rights."
        ),
    },
    # =====================================================================
    # PENALTIES
    # =====================================================================
    {
        "type": "penalty",
        "jurisdiction": "IT",
        "title": "Uber Italy — EUR 733 Million Social Security Assessment 2020",
        "offense": "Failure to pay social security contributions for Uber Eats riders",
        "amount": "EUR 733 million",
        "summary": (
            "Milan Prosecutor's Office assessed EUR 733 million in unpaid social security "
            "contributions for 60,000 Uber Eats, Glovo, Deliveroo, and Just Eat riders in "
            "Italy (2020). Prosecutors found riders were de facto employees subjected to "
            "'a pervasive digital form of control.' Assessment accompanied by appointment "
            "of a judicial administrator for Uber Italy. Uber negotiated the figure down "
            "and committed to rider employment reforms."
        ),
    },
    {
        "type": "penalty",
        "jurisdiction": "NL",
        "title": "Deliveroo Netherlands — EUR 2 Million Fine for Misclassification 2022",
        "offense": "Classifying delivery riders as independent contractors rather than employees",
        "amount": "EUR 2 million",
        "summary": (
            "Dutch labour inspectorate fined Deliveroo EUR 2 million in 2022 for "
            "misclassifying riders as self-employed. Fine covered unpaid social security "
            "contributions and employment protections owed to approximately 4,000 riders. "
            "Deliveroo exited the Netherlands in November 2022, weeks before the Dutch "
            "Supreme Court confirmed the employment relationship in March 2023."
        ),
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "DoorDash — USD 2.5 Million Tip Theft Settlement 2020",
        "offense": "Using customer tips to subsidize base delivery pay",
        "amount": "USD 2.5 million",
        "summary": (
            "Washington DC Attorney General Karl Racine secured a USD 2.5 million settlement "
            "with DoorDash in November 2020 for misleading consumers about how tips were "
            "used. DoorDash's pay model counted customer tips toward guaranteed minimum per "
            "delivery rather than as addition to base pay. Settlement required DoorDash to "
            "clearly disclose pay structure and ensure 100% of tips go to workers."
        ),
    },
    {
        "type": "penalty",
        "jurisdiction": "AU",
        "title": "Uber Australia — AUD 271,000 Deactivation Penalty 2024",
        "offense": "Unfair deactivation of driver accounts without due process",
        "amount": "AUD 271,000",
        "summary": (
            "Fair Work Ombudsman obtained AUD 271,000 in penalties against Uber Australia "
            "in 2024 for unfairly deactivating driver accounts, finding the platform "
            "exercised employer-like control. First penalty under new 'employee-like' "
            "provisions of the Fair Work Amendment (Closing Loopholes) Act. Affected "
            "drivers reinstated."
        ),
    },
    {
        "type": "penalty",
        "jurisdiction": "FR",
        "title": "Uber France — EUR 800,000 Fine for Illegal Transport 2016",
        "offense": "Operating unlicensed transport service (UberPOP)",
        "amount": "EUR 800,000",
        "summary": (
            "French court fined Uber EUR 800,000 in 2016 for operating UberPOP, a service "
            "using unlicensed non-professional drivers. Court found Uber facilitated illegal "
            "transport activity rather than merely connecting riders and drivers. Two Uber "
            "France executives received suspended prison sentences."
        ),
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Instacart — USD 46.5 Million Settlement for Worker Misclassification 2023",
        "offense": "Misclassifying shoppers as independent contractors",
        "amount": "USD 46.5 million",
        "summary": (
            "Instacart agreed to a USD 46.5 million settlement in 2023 to resolve a "
            "multi-year class action by California shoppers alleging misclassification. "
            "Plaintiffs argued Instacart controlled work schedules, set pay rates, and "
            "required specific task performance inconsistent with contractor status. "
            "Settlement covered approximately 308,000 current and former shoppers."
        ),
    },
    # =====================================================================
    # REGULATION CHANGES
    # =====================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "US",
        "title": "New York City Minimum Pay Rate for App-Based Delivery Workers 2023",
        "summary": (
            "New York City implemented a minimum pay rate of USD 17.96/hour (excluding "
            "tips) for app-based delivery workers effective July 2023, the first US city "
            "to set minimum pay for gig delivery workers. Rate rises annually with "
            "inflation. Covers DoorDash, Uber Eats, and Grubhub workers. Platforms "
            "responded by adding delivery fees and reducing coverage zones."
        ),
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US",
        "title": "Seattle App-Based Workers Minimum Compensation Standard 2024",
        "summary": (
            "Seattle's PayUp ordinance set a minimum per-trip and per-mile compensation "
            "for app-based delivery and ride-hailing workers, effective January 2024. "
            "Minimum of USD 0.44/minute and USD 0.74/mile for ride-hailing; delivery "
            "workers guaranteed minimum per-order payment. Also mandated transparent "
            "earnings information and limits on account deactivation."
        ),
    },
    {
        "type": "regulation_change",
        "jurisdiction": "ID",
        "title": "Indonesia Ministry of Manpower — Online Ojek (Motorcycle Taxi) Regulation 2019",
        "summary": (
            "Indonesian Ministry of Transportation Regulation PM 12/2019 set minimum "
            "and maximum fares for app-based motorcycle taxis (ojek online — Grab, Gojek). "
            "Minimum fare IDR 1,850/km (USD 0.12/km) in Jakarta, preventing platforms "
            "from engaging in predatory pricing that suppresses driver earnings. "
            "Also required platforms to provide accident insurance for drivers."
        ),
    },
    {
        "type": "regulation_change",
        "jurisdiction": "GB",
        "title": "UK Uber Post-Supreme Court Reforms — Worker Benefits Rollout 2021",
        "summary": (
            "Following the Uber BV v Aslam ruling, Uber reclassified 70,000+ UK drivers "
            "as 'workers' in March 2021, granting: National Minimum Wage for all driving "
            "time, holiday pay at 12.07% of earnings, automatic enrollment in pension "
            "scheme, and free insurance. Uber estimated the changes cost USD 250-300 million "
            "annually. Other UK platforms (Bolt, Ola, Addison Lee) subsequently made "
            "similar changes."
        ),
    },
    # =====================================================================
    # ADDITIONAL CASE STUDIES — ALGORITHMIC CONTROL AND EXPLOITATION
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Algorithmic Wage Discrimination in Ride-Hailing — Cross-Country Analysis",
        "summary": (
            "Research published in the Journal of Political Economy (2023) found that "
            "ride-hailing algorithms systematically offer lower per-mile rates to drivers "
            "in lower-income areas, creating geographic wage discrimination. In Lagos, "
            "Nairobi, and Manila, drivers in poorer neighborhoods earned 15-30% less per "
            "mile than those in affluent areas after controlling for distance and traffic. "
            "Pattern observed across Uber, Grab, Bolt, and InDrive platforms."
        ),
        "source": "Journal of Political Economy 2023 / Fairwork Reports 2022-2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "Meituan Delivery Algorithm — 'Trapped in the System' Investigation 2020",
        "summary": (
            "Renwu Magazine's viral 2020 investigation 'Delivery Riders, Trapped in the "
            "System' documented how Meituan's algorithm progressively shortened delivery "
            "time estimates: routes that allowed 50 minutes in 2018 were reduced to 28 "
            "minutes by 2020. Riders running red lights and driving on sidewalks to meet "
            "times. Over 40 Meituan delivery rider deaths in traffic accidents reported "
            "in 2020 alone. Article generated 200 million views and forced Meituan to "
            "add 8 minutes to all delivery windows."
        ),
        "source": "Renwu Magazine / Sixth Tone / Bloomberg 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Grab and LINE MAN Riders in Thailand — Intermediary Fleet Management",
        "summary": (
            "In Bangkok, intermediary 'fleet managers' control blocks of 50-200 Grab and "
            "LINE MAN Wongnai delivery accounts. Riders from Myanmar and Cambodia pay "
            "THB 500-1,000/day (USD 14-28) to fleet managers for account access and "
            "motorbike rental. Fleet managers retain GPS control and can remotely disable "
            "accounts. Workers earn THB 200-500/day (USD 5.50-14) after fees, below Thai "
            "minimum wage of THB 363/day."
        ),
        "source": "Thai PBS / Migrant Working Group Thailand 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Careem/Uber Drivers in UAE — Visa-Tied Platform Work and Debt",
        "summary": (
            "Ride-hailing drivers in Dubai and Abu Dhabi (Careem, Uber) commonly enter "
            "through fleet operators who sponsor their visas and lease vehicles at "
            "AED 2,500-4,000/month (USD 680-1,090). Drivers work 12-16 hours daily, "
            "6-7 days/week. Visa tied to fleet operator; leaving means deportation. "
            "Fleet operators confiscate passports of some drivers. The arrangement "
            "mirrors kafala-system exploitation in digital form."
        ),
        "source": "Migrant-Rights.org / Gulf News / Human Rights Watch 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "MX",
        "title": "Rappi and DiDi Delivery Workers in Mexico — No Insurance Deaths 2022",
        "summary": (
            "Mexican delivery workers for Rappi and DiDi reported 23 traffic fatalities "
            "in Mexico City during 2022 alone. No workers' compensation applied as riders "
            "are classified as independent. The Ni Un Repartidor Menos (Not One Less "
            "Delivery Worker) movement organized protests demanding platform-funded life "
            "and accident insurance. Rappi subsequently introduced voluntary accident "
            "insurance at MXN 18/day (USD 1) deducted from earnings."
        ),
        "source": "Ni Un Repartidor Menos / El Universal / Fairwork Mexico 2022",
    },
    # =====================================================================
    # ADVISORIES — ADDITIONAL
    # =====================================================================
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Guidelines on Decent Work in Platform Economy — Tripartite Meeting 2024",
        "summary": (
            "ILO Tripartite Meeting of Experts (2024) adopted guidelines calling for: "
            "platform worker access to freedom of association and collective bargaining, "
            "adequate social protection including maternity and health, occupational safety "
            "and health protections, fair and transparent contracts, and grievance "
            "mechanisms with human review of algorithmic decisions. Guidelines are "
            "non-binding but carry significant normative weight."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Amnesty International — Content Moderation Worker Rights Report 2023",
        "summary": (
            "Amnesty International (2023) documented human rights violations in content "
            "moderation supply chains: systematic exposure to traumatic material without "
            "adequate psychological support, NDAs silencing workers from seeking help, "
            "outsourcing to jurisdictions with weaker labor laws, and race-to-the-bottom "
            "pricing between BPO providers. Called for platform duty of care extending "
            "to all workers in moderation supply chain."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Fairwork Cloudwork Ratings 2024 — Principles for Digital Piecework",
        "summary": (
            "Fairwork Cloudwork (2024) assessed 15 digital piecework platforms — "
            "including Amazon Mechanical Turk, Clickworker, Appen, Scale AI, and "
            "Microworkers — finding that: (1) none guaranteed minimum wage in worker's "
            "locality, (2) 80% allowed task rejection without explanation or appeal, "
            "(3) 93% did not provide any occupational accident coverage, (4) no platform "
            "recognized worker representatives. Average score: 1.7/10."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Convention 181 Application to Digital Platforms — Legal Analysis 2023",
        "summary": (
            "ILO legal analysis (2023) argued that digital labor platforms function as "
            "private employment agencies under Convention 181 and should therefore be "
            "prohibited from charging fees to workers. Under C181 Article 7, all costs "
            "including platform commissions, equipment requirements, and account activation "
            "fees should be borne by the user enterprise, not the worker. Most platforms "
            "currently deduct 15-30% commission from worker earnings."
        ),
    },
    # =====================================================================
    # ADDITIONAL COURT RULINGS
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "CH",
        "title": "Uber Switzerland — Federal Supreme Court Employment Ruling 2022",
        "court": "Swiss Federal Supreme Court (Bundesgericht)",
        "year": 2022,
        "summary": (
            "The Swiss Federal Supreme Court ruled in June 2022 that an Uber driver in "
            "Geneva was an employee, not an independent contractor. The Court applied "
            "Swiss labor law criteria and found that Uber exercised sufficient control "
            "over the driver's activity through pricing, rating systems, and account "
            "management to establish a subordination relationship. Ruling applied to "
            "the Canton of Geneva; federal legislation pending."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PT",
        "title": "STRUP v. Uber — Lisbon Labour Court Ruling 2023",
        "court": "Tribunal do Trabalho de Lisboa (Lisbon Labour Court)",
        "year": 2023,
        "summary": (
            "Lisbon Labour Court ruled in 2023 that Uber drivers represented by the "
            "STRUP union were employees. The court ordered Uber to register drivers with "
            "Portuguese social security and provide back pay including holiday and "
            "Christmas bonuses. First Portuguese court ruling on platform worker "
            "employment status. Uber appealed to the Tribunal da Relacao."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Lawson v. Grubhub — Ninth Circuit Independent Contractor Ruling 2021",
        "court": "US Court of Appeals for the Ninth Circuit",
        "year": 2021,
        "summary": (
            "The Ninth Circuit affirmed that a Grubhub delivery driver was an independent "
            "contractor under California's pre-AB5 Borello test, applying the law in "
            "effect when the driver worked (2015-2016). The court found insufficient "
            "control by Grubhub over manner and means of delivery. Decision highlighted "
            "the significance of the legal shift from Borello to the more worker-friendly "
            "ABC test under Dynamex/AB5."
        ),
    },
    # =====================================================================
    # ADDITIONAL CASE STUDIES
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "AR",
        "title": "Rappi Delivery Workers in Argentina — Migrant Exploitation in Buenos Aires",
        "summary": (
            "Venezuelan and Haitian migrants constitute an estimated 60-70% of Rappi "
            "delivery riders in Buenos Aires. Many lack legal work authorization, making "
            "them dependent on rented accounts (ARS 20,000-40,000/month, USD 20-40). "
            "Riders reported robberies of phones and bikes with no platform assistance, "
            "13-hour workdays, and per-delivery pay dropping from ARS 150 to ARS 80 "
            "(nominal) between 2021-2023 while inflation exceeded 100%."
        ),
        "source": "Pagina/12 / Asociacion de Personal de Plataformas (APP) 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "Uber Eats Japan — Delivery Worker Accident Classification Dispute 2021",
        "summary": (
            "A Tokyo Uber Eats rider injured in a delivery traffic accident in 2021 was "
            "denied workers' compensation by the Labour Standards Bureau, which classified "
            "the rider as self-employed. The Tokyo District Court upheld the denial. Japan's "
            "Ministry of Health subsequently launched a study committee on gig worker "
            "protections, but no legislation has been enacted. An estimated 150,000 "
            "food delivery workers operate across Japanese platforms."
        ),
        "source": "Mainichi Shimbun / Japan Times / MHLW Study Committee 2021-2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "ET",
        "title": "Ride Platform Drivers in Ethiopia — Ride and ETTA App Worker Exploitation",
        "summary": (
            "In Addis Ababa, ride-hailing platforms Ride and ETTA charge drivers 20-25% "
            "commission with no minimum earnings guarantee. Drivers lease vehicles from "
            "fleet owners at ETB 1,500-2,500/day (USD 27-45), often earning only "
            "ETB 500-1,000/day (USD 9-18) after fuel, commission, and lease. Drivers "
            "work 14-16 hours daily, 7 days/week. No accident insurance, no health "
            "benefits, and no legal framework for platform workers in Ethiopian labor law."
        ),
        "source": "Addis Standard / Fairwork Ethiopia Report 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Pathao Riders in Bangladesh — Debt to Fleet Intermediaries",
        "summary": (
            "Pathao motorcycle ride-hailing riders in Dhaka frequently enter through "
            "intermediaries who provide motorcycles on hire-purchase at inflated prices "
            "(BDT 250,000-350,000, market value BDT 150,000-200,000). Monthly installments "
            "of BDT 12,000-15,000 lock riders into 24-36 month debt cycles. Missing "
            "installments results in motorcycle confiscation and loss of entire investment. "
            "An estimated 200,000 riders operate on Pathao in Bangladesh."
        ),
        "source": "Daily Star Bangladesh / Dhaka Tribune / BILS 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "EG",
        "title": "Uber and Careem Drivers in Egypt — Post-Regulation Squeeze 2021",
        "summary": (
            "Egypt's 2018 ride-hailing law (Law 87/2018) required platform drivers to "
            "obtain private taxi licenses at EGP 5,000-10,000, vehicle inspections, and "
            "criminal background checks. Compliance costs plus 20-25% platform commission "
            "and rising fuel prices reduced effective driver earnings to EGP 150-250/day "
            "(USD 5-8) for 12-14 hours. Egyptian drivers' informal association reported "
            "that 40% of surveyed drivers earned below Egypt's poverty line of EGP 857/month "
            "per capita."
        ),
        "source": "Mada Masr / Egyptian Initiative for Personal Rights 2021",
    },
    # =====================================================================
    # ADDITIONAL STATISTICS
    # =====================================================================
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Brazil Platform Worker Population — IBGE PNAD Survey 2023",
        "metric": "Number of app-based workers in Brazil",
        "value": "1.5 million (delivery and ride-hailing combined)",
        "year": 2023,
        "details": (
            "IBGE PNAD Continua survey (2023) identified 1.5 million platform workers in "
            "Brazil: 778,000 in delivery (iFood, Rappi, 99Food) and 722,000 in ride-hailing "
            "(Uber, 99, InDriver). 67% earned below one minimum wage (BRL 1,320/month). "
            "86% were male, 60% were Black or mixed-race, and median age was 34."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Uber Global Revenue vs. Driver Share — Financial Analysis 2023",
        "metric": "Driver share of gross ride-hailing fare (Uber global average)",
        "value": "55-65% of fare (down from 75-80% in 2015)",
        "year": 2023,
        "details": (
            "Analysis of Uber financial filings (2023) shows average driver share of gross "
            "bookings declined from 75-80% in 2015 to 55-65% in 2023. Uber's take rate "
            "increased to 28.5% (Q4 2023). Additional driver costs (fuel, vehicle, "
            "insurance, phone) reduce effective take-home to an estimated 35-45% of the "
            "customer fare. Pattern consistent across Lyft, Bolt, and Grab."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "CN",
        "title": "China Food Delivery Worker Population — Meituan Annual Report 2023",
        "metric": "Active delivery riders on Meituan platform",
        "value": "7.45 million active riders annually",
        "year": 2023,
        "details": (
            "Meituan's 2023 annual report disclosed 7.45 million delivery riders who "
            "completed at least one order during the year. Ele.me (Alibaba) reported "
            "approximately 3 million additional riders. Combined Chinese food delivery "
            "workforce exceeds 10 million. Average rider income: CNY 5,000-8,000/month "
            "(USD 690-1,100). Traffic accident rate: 1 in 60 riders per year."
        ),
    },
    # =====================================================================
    # ADDITIONAL PENALTIES
    # =====================================================================
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Uber/Lyft Massachusetts — USD 175 Million Misclassification Settlement 2024",
        "offense": "Systematic misclassification of drivers as independent contractors",
        "amount": "USD 175 million (combined Uber and Lyft)",
        "summary": (
            "Massachusetts Attorney General secured a USD 175 million combined settlement "
            "with Uber (USD 148 million) and Lyft (USD 27 million) in June 2024. Settlement "
            "required guaranteed minimum earnings of USD 32.50/hour during engaged time, "
            "paid sick leave, occupational accident insurance, and healthcare stipend. "
            "Covered approximately 140,000 Massachusetts drivers. Did not reclassify "
            "drivers as employees."
        ),
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Lyft — USD 25 Million New York AG Settlement 2024",
        "offense": "Improper deduction of sales tax and Black Car Fund fees from driver pay",
        "amount": "USD 25 million",
        "summary": (
            "New York Attorney General Letitia James obtained a USD 25 million settlement "
            "with Lyft in March 2024 for improperly deducting sales tax and Black Car Fund "
            "contributions from driver earnings rather than collecting them from passengers. "
            "Deductions affected over 62,000 New York City Lyft drivers from 2015-2017, "
            "reducing take-home pay by an average of USD 650 per affected driver."
        ),
    },
    # =====================================================================
    # ADDITIONAL CASE STUDIES — WORKER ORGANIZING
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "GB",
        "title": "ADCU and IWGB Platform Worker Unions in UK — Collective Organizing",
        "summary": (
            "The App Drivers and Couriers Union (ADCU) and Independent Workers' Union of "
            "Great Britain (IWGB) have organized ride-hailing and delivery workers since "
            "2016. ADCU, with 70,000+ members, led the Uber BV v Aslam case to the Supreme "
            "Court. IWGB organized Deliveroo riders and won a Court of Appeal ruling (2021) "
            "that riders have the right to collectively bargain under Article 11 ECHR. "
            "Despite legal victories, recognition agreements with platforms remain elusive."
        ),
        "source": "ADCU / IWGB / Financial Times 2021-2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "KE",
        "title": "Gig Workers Association Kenya — Digital Platform Worker Organizing 2023",
        "summary": (
            "Kenyan gig workers formed the Digital Taxi Association of Kenya (DTAK) and "
            "Kenya Gig Workers Association in 2022-2023, organizing Uber, Bolt, and "
            "Little Cab drivers. Associations lobbied for the 2024 Gig Workers Bill "
            "proposing minimum per-trip earnings, caps on platform commission at 15%, "
            "and mandatory accident insurance. Organized a 3-day driver strike in "
            "Nairobi in October 2023 involving an estimated 5,000 drivers."
        ),
        "source": "Business Daily Africa / DTAK Kenya / Reuters 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Platform Company Spending on Anti-Classification Lobbying — 2019-2024",
        "metric": "Estimated combined lobbying and ballot measure spending by major gig platforms",
        "value": "USD 800+ million (2019-2024 cumulative)",
        "year": 2024,
        "details": (
            "Major gig platforms (Uber, Lyft, DoorDash, Instacart, Postmates) spent over "
            "USD 800 million globally on lobbying and ballot measures to prevent worker "
            "reclassification between 2019-2024. California Prop 22 alone cost USD 205 "
            "million. Similar spending in Massachusetts (USD 64 million defeated ballot "
            "measure), EU directive lobbying (estimated EUR 50 million), and UK post-Aslam "
            "regulatory engagement. Largest corporate political spending campaign in US "
            "ballot initiative history."
        ),
    },
]
