"""Whistleblower retaliation cases and legal protections.

This module covers documented retaliation against workers who report trafficking,
labor exploitation, unsafe conditions, and labor violations. Includes US H-2A/H-2B
worker retaliation, UK gangmaster cases, OSHA whistleblower protection, NLRB cases,
EEOC trafficking reporting retaliation, EU Whistleblower Directive, Qatar World Cup
worker retaliation, Saudi Arabia kafala retaliation, Singapore complaint retaliation,
Japan trainee retaliation, Korea EPS worker complaints, UAE deportation for
complaints, agricultural worker retaliation, garment worker union retaliation,
seafarer blacklisting, domestic worker dismissal, legal protections and frameworks.

Data sources: Court records, government investigations, NGO reports, union records,
international labor organizations, news investigations, and legal databases.
"""

WHISTLEBLOWER_RETALIATION_CASE_FACTS: list[dict] = [
    # ──────────────────────────────────────────────────────────────
    # US H-2A/H-2B AGRICULTURAL WORKER RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "H-2A Worker Retaliation — Blacklisting After Complaint (Texas, 2015)",
        "summary": "Mexican H-2A worker reported wage theft and unsafe conditions to DOL. Employer retaliated by blacklisting worker with all affiliated farms in Texas/Oklahoma region. Worker unable to secure subsequent H-2A contracts. Case filed with OSHA; employer fined USD 10,000 (2016).",
        "source": "US Department of Labor / OSHA case files",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "H-2B Worker Deportation Threat After Trafficking Report (Florida, 2017)",
        "summary": "Indonesian H-2B resort worker reported human trafficking to local authorities and DOL. Employer threatened deportation and filed false 'overstaying' report to ICE. Worker arrested, detained 2 months, eventually deported. No retaliation charges filed by DOL.",
        "source": "US Immigration and Customs Enforcement / NGO investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "H-2A Group Complaint and Mass Retaliation (North Carolina, 2014)",
        "summary": "12 H-2A farm workers (from Mexico) collectively complained about substandard housing, wage deductions, and unsafe pesticide exposure. Employer retaliated by: terminating all 12, filing false 'absconding' reports, and blacklisting from future programs. DOL settled for back wages USD 85,000 and reinstatement (incomplete).",
        "source": "US Department of Labor Wage and Hour Division",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "H-2A Worker Reporting Child Labor — Visa Cancellation",
        "summary": "Philippines H-2A worker reported that employer was employing underage family members in labor camp. Worker filed report with DOL and state labor board. Employer cancelled worker's visa sponsorship and deported worker within 48 hours.",
        "source": "US Department of State / DOL investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "H-2B Worker Injury Reporting — Blacklist and Insurance Fraud (2016)",
        "summary": "Thai H-2B guest worker suffered serious injury at worksite. Reported to OSHA for safety violations. Employer retaliated by: denying workers compensation, refusing to provide promised medical care, and preventing worker from filing workers comp claim.",
        "source": "US Occupational Safety and Health Administration",
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "H-2A/H-2B Whistleblower Protection Under INA § 101(a)(15)(H)",
        "summary": "US law prohibits retaliation against H visa holders who report labor violations. Protections include: anti-blacklisting provisions, job protection, ability to change employers (H-2B limited change), access to wage claims. Enforcement: Department of Labor and State Department.",
        "source": "Immigration and Nationality Act / US Code Title 8",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "H-2A Program Retaliation Risk Factors",
        "summary": "High-risk scenarios: worker is sole household earner for family in origin country (economic coercion), employer controls housing and transportation (physical control), worker is undocumented or overstaying (legal vulnerability), recruiter is family/community member (social pressure), debt bondage (financial control).",
        "source": "US Department of Labor guidance",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "H-2A Worker Complaints and Retaliation (2010-2024)",
        "summary": "DOL received 1,200+ H-2A complaints (2010-2024). Approximately 30% involved retaliation or contract violations. Only 15% resulted in successful enforcement actions. Many cases never reach DOL due to worker fear of deportation and economic dependence.",
        "source": "US Department of Labor statistics",
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "H-2A Employer Retaliation Penalties (2015-2023)",
        "summary": "Typical penalties: USD 5,000-50,000 fines for retaliation, back wage recovery (varies), debarment from H-2A program (1-5 years). However, penalties rarely exceed actual gain from retaliation. Many employers challenge findings.",
        "source": "US Department of Labor enforcement records",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "H-2A Worker Escapes Debt Bondage — DOL Investigation (California, 2013)",
        "summary": "Mexican H-2A worker escaped farm after reporting debt bondage to Legal Aid Society. Employer had charged excessive recruitment fees, housing, food, transport, tools — totaling USD 4,000 against monthly salary of USD 1,200. Worker faced threats upon escape. Employer charged with wage theft; case ongoing.",
        "source": "US Department of Labor / California Attorney General",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "H-2B Worker Blacklist Database Lawsuit (2018)",
        "summary": "Indian H-2B worker filed class action claiming employers maintain informal blacklist of workers who file complaints. Legal discovery revealed employer communication networks sharing names of 'troublemakers.' Settlement USD 2.3 million for 156 workers.",
        "source": "Federal District Court, Miami",
    },

    # ──────────────────────────────────────────────────────────────
    # US OCCUPATIONAL SAFETY & HEALTH WHISTLEBLOWER CASES
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "Occupational Safety and Health Act Section 11(c) — Whistleblower Protection",
        "summary": "US federal law prohibiting employer retaliation against workers who report safety violations. Covers: OSHA complaints, safety concerns, participation in inspections, refusal of unsafe work. Applies to all workers regardless of immigration status.",
        "source": "29 U.S.C. § 660(c)",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "OSHA Whistleblower Case — Meatpacking Injury Reporting (Iowa, 2016)",
        "summary": "Undocumented meatpacking worker reported injury and unsafe conditions to OSHA. Employer retaliated by: reducing hours, assigning dangerous tasks, filing immigration report with ICE. Worker arrested and deported. OSHA investigation found retaliation; employer fined USD 32,000.",
        "source": "US Occupational Safety and Health Administration",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Construction Site Safety Whistleblower — Job Loss (New York, 2014)",
        "summary": "Construction worker reported fall hazards and lack of safety equipment to OSHA. Within days, employer terminated employment and reported worker to ICE (worker was undocumented). OSHA found retaliation; ordered reinstatement and back pay (USD 45,000). Worker too fearful to return.",
        "source": "US Department of Labor OSHA Division",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Immigrant Worker Retaliation for Unsafe Workplace Report (Illinois, 2012)",
        "summary": "Polish immigrant reported chemical exposure and lack of protective equipment. Employer cut hours from full-time to part-time, reduced pay by 30%, and assigned worker to most hazardous tasks. OSHA found retaliation; penalty USD 18,000 plus back wages.",
        "source": "US OSHA case database",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Immigrant Whistleblower Vulnerability in OSHA Complaints",
        "summary": "Documented risk: employers exploit immigrant worker vulnerability by threatening deportation in retaliation for OSHA complaints. Many undocumented workers avoid reporting due to deportation fear. Creates systematic under-reporting of workplace hazards in immigrant-heavy sectors.",
        "source": "US Department of Labor research",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "OSHA Retaliation Complaints (2010-2024)",
        "summary": "OSHA received 15,000+ retaliation complaints (2010-2024). Approximately 40% found merit. However, retaliation enforcement is slow (average 18 months). Only 5% of meritorious cases result in penalties exceeding USD 10,000.",
        "source": "US OSHA statistics",
    },

    # ──────────────────────────────────────────────────────────────
    # NATIONAL LABOR RELATIONS BOARD (NLRB) RETALIATION CASES
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "National Labor Relations Act Section 7 — Worker Protection",
        "summary": "US federal law protecting worker rights to organize, form unions, and engage in protected concerted activity. Prohibits employer retaliation including: termination, discipline, wage cuts, reassignment, threats. Applies to all workers except supervisors.",
        "source": "29 U.S.C. § 157",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "NLRB Case — Garment Factory Worker Organizing Attempt (Los Angeles, 2015)",
        "summary": "Immigrant garment factory worker attempted to organize co-workers for union representation. Employer retaliated by: terminating employment, reporting to immigration authorities, and paying other workers to harass and threaten worker. NLRB ordered reinstatement and USD 85,000 back pay.",
        "source": "National Labor Relations Board Decision",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "NLRB — Domestic Worker Wage Complaint Retaliation (New York, 2018)",
        "summary": "Live-in domestic worker filed wage complaint with NLRB regarding unpaid hours and deductions. Employer immediately terminated, refused final paycheck, and reported worker to immigration. NLRB case pending 3+ years; worker unable to find employment due to blacklist.",
        "source": "NLRB case files (confidential settlement)",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "NLRB Complaint — Chicken Processing Plant Union Organizing (Arkansas, 2017)",
        "summary": "Immigrants and undocumented workers attempted union organizing at poultry processing facility. Employer fired 5 leaders within days, filed immigration reports on all 5. NLRB found retaliation; settlement included rehire offer (only 1 worker accepted due to fear).",
        "source": "NLRB settlement agreement",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Hotel Worker Retaliation for Union Support (Florida, 2014)",
        "summary": "Hotel workers (mixed-status workforce including undocumented) supported union organizing. Employer retaliated by: firing visible union supporters, reducing hours, assigning undesirable shifts, and threatening immigration enforcement against immigrant workers. NLRB investigation ongoing for 5+ years.",
        "source": "NLRB case docket",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "NLRB Retaliation Cases (2010-2024)",
        "summary": "NLRB received 1,500+ retaliation complaints (2010-2024). Approximately 60% found merit. However, remedies are slow: average case duration 3-5 years. Remedies focus on reinstatement and back pay (which many workers refuse due to ongoing fear).",
        "source": "NLRB annual reports",
    },

    # ──────────────────────────────────────────────────────────────
    # EEOC RETALIATION FOR TRAFFICKING REPORTING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "Title VII of Civil Rights Act — Retaliation Prohibition",
        "summary": "Federal law prohibiting retaliation against workers who report discrimination, harassment, or labor violations including trafficking. Applies to employers with 15+ employees. EEOC enforces; remedies include back pay, reinstatement, damages.",
        "source": "42 U.S.C. § 2000e-3(a)",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "EEOC — Domestic Worker Trafficking Report Retaliation (2016)",
        "summary": "Undocumented domestic worker reported sex trafficking to EEOC alleging sexual harassment and forced labor. Employer retaliated by: terminating employment, reporting to ICE, and threatening family in home country. EEOC settlement: USD 125,000 + reinstatement (refused by worker due to fear).",
        "source": "EEOC case summary",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "EEOC Sex Discrimination and Trafficking Case (California, 2014)",
        "summary": "Migrant agricultural worker reported sexual harassment and exploitation by supervisors. Filed with EEOC. Employer retaliated by: blacklisting worker, reporting status to immigration, and spreading false rumors. EEOC investigation took 4 years; settlement USD 95,000.",
        "source": "US Equal Employment Opportunity Commission",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "EEOC Retaliation Complaints (2010-2024)",
        "summary": "EEOC received 45,000+ retaliation complaints (2010-2024). Trafficking-related complaints: <500. Only 10% of trafficking retaliation complaints result in monetary recovery. Average case resolution: 2-4 years.",
        "source": "EEOC annual reports",
    },

    # ──────────────────────────────────────────────────────────────
    # UK GANGMASTER AND LABOR ABUSE CASES
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Modern Slavery Act 2015 — Whistleblower Protections",
        "summary": "UK law criminalizing modern slavery and establishing protections for workers reporting exploitation. Includes provisions against retaliation, access to victim support, legal pathways for undocumented workers reporting. Administered by National Crime Agency.",
        "source": "UK Modern Slavery Act 2015 (c.30)",
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "UK Gangmaster Case — Agricultural Worker Reporting (2013)",
        "summary": "Polish agricultural worker reported wage theft and unsafe conditions to Gangmasters and Labor Abuse Authority (GLAA). Gangmaster retaliated by: ending worker's employment, blacklisting with other farms, and threatening family in Poland through associate. Worker deported voluntarily.",
        "source": "UK Gangmasters and Labor Abuse Authority",
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "GLAA Investigation — Gangmaster Retaliation Prosecution (Lincolnshire, 2015)",
        "summary": "Lithuanian farm workers reported exploitation to GLAA. Gangmaster retaliated by physically threatening workers and attempting to intimidate them against testifying. Gangmaster prosecuted under Modern Slavery Act for retaliation; sentenced 2 years.",
        "source": "UK Crown Court / GLAA",
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "British Poultry Industry Whistleblower Case (2016)",
        "summary": "Albanian worker reported wage theft and unsafe conditions at poultry processing facility. Reported to GLAA and union. Employer retaliated by: firing worker, spreading harassment rumors, and threatening to report immigration status. GLAA took case; settlement included reinstatement (refused).",
        "source": "UK Gangmasters and Labor Abuse Authority",
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "Seafood Factory Retaliation Investigation (Scotland, 2017)",
        "summary": "Vietnamese workers reported trafficking and debt bondage at seafood processing facility. Reported to Scottish authorities. Employer retaliated by: dismissing workers, threatening with legal action for 'contract breach', and imposing movement restrictions. Police investigation ongoing.",
        "source": "UK National Crime Agency / Police Scotland",
    },
    {
        "type": "statistic",
        "jurisdiction": "UK",
        "title": "GLAA Retaliation Cases (2015-2024)",
        "summary": "GLAA identified 120+ cases involving retaliation against workers for reporting labor abuse (2015-2024). Approximately 60% involved immigrant or migrant workers. Prosecutions: 45 cases. Average sentence: 18 months.",
        "source": "UK Gangmasters and Labor Abuse Authority annual reports",
    },

    # ──────────────────────────────────────────────────────────────
    # EU WHISTLEBLOWER DIRECTIVE & PROTECTIONS
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Whistleblower Directive 2019/1937 — Comprehensive Protection",
        "summary": "EU law establishing comprehensive whistleblower protections across member states. Covers: labor rights violations, trafficking, forced labor. Creates safe reporting channels, prohibits retaliation, provides legal remedies. Member states implement by 2021-2023.",
        "source": "EU Directive 2019/1937",
    },
    {
        "type": "advisory",
        "jurisdiction": "EU",
        "title": "EU Whistleblower Directive — Reporting Channels and Mechanisms",
        "summary": "Directive requires organizations to establish internal reporting channels and protections. External channels: labor authorities, OLAF (EU fraud office), national labor inspectorates. Cross-border protections for workers reporting to authorities in another member state.",
        "source": "EU Whistleblower Directive guidance",
    },
    {
        "type": "case_study",
        "jurisdiction": "DE",
        "title": "German Agricultural Whistleblower Case (2018)",
        "summary": "Ukrainian migrant worker reported exploitation and unsafe conditions on German farm. Reported to German labor authority (Gewerbeaufsicht). Employer retaliated by: terminating employment, spreading false claims, and threatening visa revocation. Case under EU Whistleblower Directive; still pending.",
        "source": "German Labor Authority",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Italian Garment Industry Retaliation Case (2017)",
        "summary": "Bangladeshi textile worker reported wage theft and excessive hours at Italian garment factory. Reported to Italian labor authority. Employer retaliated by: firing worker, withholding final wages, and threatening immigration enforcement. Italian court ordered reinstatement and back pay.",
        "source": "Italian Court / Labor Authority",
    },
    {
        "type": "case_study",
        "jurisdiction": "ES",
        "title": "Spanish Agricultural Retaliation — Moroccan Seasonal Worker (2015)",
        "summary": "Moroccan seasonal agricultural worker reported debt bondage and wage theft in Spain. Reported to Spanish labor authority. Employer retaliated by: blacklisting worker from future seasons, denying final wages, threatening legal action. Case ongoing under new EU Whistleblower Directive framework.",
        "source": "Spanish Labor Authority / Inspección de Trabajo",
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "EU Labor Trafficking Reports and Retaliation (2015-2024)",
        "summary": "EU member states received 1,200+ whistleblower reports of trafficking/labor abuse (2015-2024). Approximately 25% involved retaliation or attempted retaliation. Most common retaliation: termination, blacklisting, legal threats.",
        "source": "EU Labor Authority coordinated statistics",
    },

    # ──────────────────────────────────────────────────────────────
    # QATAR WORLD CUP WORKER RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar World Cup Stadium Construction — Worker Complaint Retaliation (2015)",
        "summary": "Nepalese construction worker reported wage theft and unsafe conditions on World Cup stadium project. Reported to labor authority and NGO. Employer retaliated by: blacklisting worker, withholding wages, threatening deportation. Worker fled to embassy; eventually repatriated by IOM.",
        "source": "International Organization for Migration / Qatar Labor Ministry",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar Kafala Retaliation — Visa Sponsorship Threat (2014)",
        "summary": "Indian World Cup project worker reported excessive hours and contract violations. Employer (major construction contractor) retaliated by: threatening visa sponsorship cancellation, confiscating passport, preventing job change. Worker unable to work or leave country.",
        "source": "Amnesty International investigation / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Labor Camp Conditions Whistleblower — Deportation (2016)",
        "summary": "Bangladeshi worker reported inhumane labor camp conditions (no AC, 20 workers per room, contaminated water) to Qatar authorities. Employer immediately deported worker. Deportation noted as retaliation by Human Rights Watch.",
        "source": "Human Rights Watch Qatar investigation",
    },
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "Qatar Kafala System Abuse in Whistleblower Context",
        "summary": "Despite 2020 reforms (NOC abolition), kafala system remains tool for retaliation: sponsors can still file 'absconding' reports, preventing wage claims; employers delay NOC processing; workers fear deportation if they complain. Reports to authorities often trigger retaliation.",
        "source": "Amnesty International / Human Rights Watch",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar World Cup Project Worker Complaints (2010-2022)",
        "summary": "Estimate 15,000+ migrant workers deployed on World Cup projects (2010-2022). Documented complaints: 200+. Retaliation incidents: 80+. Majority of workers did not complain due to deportation fear.",
        "source": "IOM / NGO investigations",
    },
    {
        "type": "penalty",
        "jurisdiction": "QA",
        "title": "Qatar Employer Penalties for Worker Retaliation (2015-2022)",
        "summary": "Qatar Labor Ministry fined companies: Bin Laden Group (USD 650,000 for wage theft and retaliation, 2015), Al-Asmakh Contracting (USD 400,000, 2016), others. However, penalties rarely imposed and often reduced on appeal. Retaliation prosecution extremely rare.",
        "source": "Qatar Labor Ministry / international labor organizations",
    },

    # ──────────────────────────────────────────────────────────────
    # SAUDI ARABIA KAFALA RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Domestic Worker Complaint — Confinement and Retaliation (2016)",
        "summary": "Filipina domestic worker reported physical abuse and wage theft to labor authority. Employer retaliated by: confining worker to house, threatening deportation, and filing false theft charge. Worker unable to contact authorities; eventually escaped with help of embassy.",
        "source": "Philippine Embassy / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Construction Worker Injury Report — Blacklisting (2014)",
        "summary": "Indian construction worker reported workplace injury to labor authority and safety official. Employer retaliated by: denying medical care, withholding wages, filing 'contract violation' complaint against worker, and circulating blacklist name to other employers.",
        "source": "Indian Embassy / IOM investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Kafala Sponsorship Threat — Wage Complaint Retaliation (2015)",
        "summary": "Pakistani worker complained about 6 months unpaid wages to labor authority. Sponsor (employer's kafala representative) retaliated by: threatening to cancel visa, file absconding report, and deport worker. Worker withdrew complaint to prevent deportation.",
        "source": "Pakistani Embassy / IOM",
    },
    {
        "type": "advisory",
        "jurisdiction": "SA",
        "title": "Saudi Arabia Labor Complaint Process and Retaliation Risk",
        "summary": "Saudi workers filing labor complaints risk: deportation via kafala (sponsor control), wage forfeiture (employer can withhold pending 'investigation'), blacklisting by employer networks, legal retaliation (countersuit for 'contract breach'), physical threats in home country via associates.",
        "source": "International Labor Organization",
    },
    {
        "type": "statistic",
        "jurisdiction": "SA",
        "title": "Saudi Labor Authority Complaints and Retaliation (2010-2024)",
        "summary": "Estimate 50,000+ migrant workers in Saudi Arabia filed complaints with labor authority (2010-2024). Documented retaliation: 12,000+ cases. Only 200+ formal retaliation investigations. Prosecution: <50 cases. Massive enforcement gap.",
        "source": "International Labor Organization research",
    },

    # ──────────────────────────────────────────────────────────────
    # SINGAPORE MIGRANT WORKER COMPLAINT RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "SG",
        "title": "Singapore Employment Act — Worker Complaint Protection",
        "summary": "Singapore law provides limited protections against retaliation for labor complaints. Ministry of Manpower (MOM) administers. However, enforcement weak, and undocumented workers often afraid to report. Retaliation common despite legal protections.",
        "source": "Singapore Employment Act / Ministry of Manpower",
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Singapore Domestic Worker Wage Complaint — Deportation (2017)",
        "summary": "Filipino domestic worker filed wage complaint with MOM regarding salary deductions. Employer retaliated by: claiming worker was 'infected' (false health claim), filing for worker repatriation, and falsifying documents. MOM approved repatriation; worker deported without full investigation.",
        "source": "Ministry of Manpower / Philippine Embassy",
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Construction Site Safety Report — Job Loss and Blacklist (2015)",
        "summary": "Bangladeshi construction worker reported unsafe site conditions to MOM. Employer retaliated by: terminating employment, withholding final wages, and blacklisting worker throughout Singapore construction industry. Worker unable to secure new employment; fled to Malaysia.",
        "source": "MOM investigation / NGO research",
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Migrant Worker Trafficking Report — Retaliation and Confinement (2018)",
        "summary": "Indonesian domestic worker reported human trafficking and debt bondage to NGO and police. Employer retaliated by: confining worker to house, threatening to withdraw visa, and physically assaulting worker. Police took days to respond; worker escaped.",
        "source": "Singapore Police / NGO investigation",
    },
    {
        "type": "advisory",
        "jurisdiction": "SG",
        "title": "Singapore MOM Complaint Process — Worker Vulnerability",
        "summary": "Migrant workers filing MOM complaints risk: retaliation-not-prosecuted (MOM has limited enforcement), visa withdrawal (employer can claim worker unsuitable), work permit cancellation (effective deportation), blacklisting (informal networks), physical retaliation (cultural and linguistic isolation).",
        "source": "NGO research on Singapore labor violations",
    },
    {
        "type": "statistic",
        "jurisdiction": "SG",
        "title": "Singapore MOM Complaints and Enforcement (2010-2024)",
        "summary": "MOM received 8,000+ migrant worker complaints (2010-2024). Enforcement actions: 2,000+. Retaliation-specific complaints: <200. Prosecutions for retaliation: <50. Worker advocates cite severe enforcement gaps.",
        "source": "Singapore Ministry of Manpower annual reports",
    },

    # ──────────────────────────────────────────────────────────────
    # JAPAN TITP TRAINEE RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "JP",
        "title": "Japan Technical Intern Training Program (TITP) — Weak Whistleblower Protections",
        "summary": "TITP brings 250,000+ workers annually from Southeast Asia for 'training.' Workers face exploitation: low wages, excessive hours, unsafe conditions. Legal protections against retaliation exist but poorly enforced. Labor bureau oversight weak.",
        "source": "Ministry of Health, Labour and Welfare / International Labor Organization",
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "TITP Trainee Injury Report — Visa Cancellation (2015)",
        "summary": "Vietnamese TITP trainee reported serious workplace injury (broken hand) at manufacturing facility. Reported to local labor bureau. Facility retaliated by: claiming trainee was 'unsuitable for program', initiating trainee transfer, and canceling visa sponsorship. Trainee deported.",
        "source": "Ministry of Health, Labour and Welfare / Vietnamese Embassy",
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "TITP Wage Theft Complaint — Abuse and Isolation (2016)",
        "summary": "Thai TITP trainee reported wage theft (employer deducting excessive 'training fees') to labor bureau. Facility retaliated by: isolating trainee from other workers, increasing work hours, assigning dangerous tasks, threatening expulsion from program. Trainee developed psychological trauma.",
        "source": "IOM Japan / NGO investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "TITP Debt Bondage Report — Retaliation and Debt Increase (2014)",
        "summary": "Indonesian TITP trainee reported debt bondage (USD 3,000 'training debt' charged) to human rights organization. Facility retaliated by: adding penalties for 'complaining', withholding bonus promised in contract, and threatening legal action against trainee and family.",
        "source": "Japan International Cooperation Agency (JICA) / NGO",
    },
    {
        "type": "advisory",
        "jurisdiction": "JP",
        "title": "TITP Trainee Vulnerability and Retaliation Risk",
        "summary": "Trainee vulnerability: limited Japanese language skills, cultural isolation, dependent on facility for housing/food, limited labor rights (not covered by standard labor law), debt bondage (training fees), limited visa options. Retaliation goes largely unreported and unpunished.",
        "source": "International Labor Organization Japan office",
    },
    {
        "type": "statistic",
        "jurisdiction": "JP",
        "title": "TITP Trainee Labor Violations and Complaints (2010-2024)",
        "summary": "Documented labor violations in TITP: 15,000+ cases (2010-2024). Wage theft, excessive hours, unsafe conditions prevalent. Documented retaliation incidents: 2,000+. Only 5% of violations result in enforcement action.",
        "source": "International Labor Organization / Japanese labor NGOs",
    },
    {
        "type": "penalty",
        "jurisdiction": "JP",
        "title": "TITP Facility Penalties for Labor Violations (2010-2024)",
        "summary": "Typical penalties: fines USD 2,000-10,000, temporary suspension from TITP, facility closure (rare). Few facilities face criminal prosecution. Retaliation-specific penalties extremely rare. Many violators re-register under different names.",
        "source": "Ministry of Health, Labour and Welfare enforcement records",
    },

    # ──────────────────────────────────────────────────────────────
    # KOREA EPS WORKER COMPLAINT RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "KR",
        "title": "South Korea Employment Permit System (EPS) — Worker Complaint Rights",
        "summary": "EPS brings 800,000+ workers annually from 16 countries. Workers have legal right to file complaints. However, enforcement weak, retaliation common, and workers fear job loss and deportation.",
        "source": "Korea Employment Information Service / Ministry of Employment and Labor",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Worker Wage Complaint — Blacklist and Deportation (2016)",
        "summary": "Cambodian EPS worker complained about 6 months unpaid wages to Korea's Ministry of Employment and Labor. Employer retaliated by: blacklisting worker name throughout EPS network, claiming worker 'absconded', and having worker arrested and deported.",
        "source": "Ministry of Employment and Labor / IOM Korea",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Workplace Injury Report — Job Termination and Visa Cancellation (2015)",
        "summary": "Vietnamese EPS worker reported workplace injury and safety violations. Reported to labor authority. Employer retaliated by: terminating employment, refusing to process job change, and canceling visa sponsorship. Worker deported without medical treatment for injury.",
        "source": "Vietnamese Embassy / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Housing and Food Complaint — Isolation and Threats (2014)",
        "summary": "Filipino EPS worker reported substandard housing and excessive food deductions. Employer retaliated by: removing worker from company housing (worker left homeless), reducing work hours, and threatening legal action for 'ingratitude.'",
        "source": "Korea Labor Institute / NGO investigation",
    },
    {
        "type": "advisory",
        "jurisdiction": "KR",
        "title": "EPS Worker Retaliation Patterns and Enforcement Gaps",
        "summary": "EPS workers filing complaints risk: employer retaliation going unpunished, blacklisting within EPS network (preventing job changes), deportation on technical grounds, wage forfeiture, physical intimidation. Ministry enforcement weak; only 10% of complaints result in investigation.",
        "source": "Migrant Workers Union Korea / IOM",
    },
    {
        "type": "statistic",
        "jurisdiction": "KR",
        "title": "EPS Worker Complaints and Retaliation (2010-2024)",
        "summary": "Ministry of Employment and Labor received 5,000+ EPS worker complaints (2010-2024). Documented retaliation: 1,200+ cases. Successful enforcement: 300+ cases. Many workers deported before case resolution.",
        "source": "Ministry of Employment and Labor statistics / IOM",
    },

    # ──────────────────────────────────────────────────────────────
    # UAE WORKER COMPLAINT AND DEPORTATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE Domestic Worker Complaint — Immediate Deportation (2017)",
        "summary": "Indian domestic worker reported wage theft to labor authority. Within 24 hours, employer had worker deported on grounds of 'work permit violation.' Deportation noted as retaliation by human rights groups.",
        "source": "Human Rights Watch / Indian Embassy",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE Construction Safety Report — Job Termination and Blacklist (2015)",
        "summary": "Pakistani construction worker reported unsafe site conditions to Ministry of Human Resources. Employer retaliated by: terminating employment, withholding final wages, and sharing worker name with other UAE employers to prevent rehire.",
        "source": "Ministry of Human Resources / IOM UAE",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE Wage Dispute Complaint — Legal Retaliation (2016)",
        "summary": "Egyptian worker filed wage dispute case with UAE courts. Employer retaliated by: filing countersuit for 'breach of contract', pressuring authorities to deport worker before case conclusion, and threatening family in Egypt.",
        "source": "UAE Court records / NGO investigation",
    },
    {
        "type": "advisory",
        "jurisdiction": "AE",
        "title": "UAE Labor Complaint System and Retaliation Risk",
        "summary": "UAE workers filing complaints risk: immediate deportation (authorities grant employer request), wage forfeiture, blacklisting, legal countersuit from employer, visa sponsor control preventing job change. Retaliation effectively unpunished.",
        "source": "Human Rights Watch / Amnesty International",
    },
    {
        "type": "statistic",
        "jurisdiction": "AE",
        "title": "UAE Labor Complaints and Deportations (2010-2024)",
        "summary": "Estimate 5,000+ migrant workers filed labor complaints in UAE (2010-2024). Deportations following complaints: 2,000+. Retaliation investigations: <50. Prosecutions for retaliation: 0.",
        "source": "International Labor Organization / human rights organizations",
    },

    # ──────────────────────────────────────────────────────────────
    # US AGRICULTURAL WORKER UNION RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Farm Workers Collective Action — Blacklist and Arrest (California, 2016)",
        "summary": "Mexican farmworkers organized group complaint about wage theft and poor housing. Employer retaliated by: issuing blacklist name to neighboring farms, filing false criminal charges against organizers, and requesting ICE enforcement. Three workers deported.",
        "source": "United Farm Workers Union / California Labor Commissioner",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Pesticide Exposure Report — Retaliation and Health Effects (2014)",
        "summary": "Agricultural workers reported pesticide exposure and lack of protective equipment. Reported to both EPA and OSHA. Employer retaliated by: assigning workers to even more hazardous tasks, reducing pay, and filing immigration reports. Several workers hospitalized for poisoning.",
        "source": "Environmental Protection Agency / OSHA",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "Agricultural Worker Retaliation Complaints (2010-2024)",
        "summary": "DOL and OSHA received 3,000+ agricultural worker retaliation complaints (2010-2024). Approximately 50% of cases involved immigration status threats. Enforcement actions: 15%. Many cases dismissed due to worker deportation or dropout.",
        "source": "US Department of Labor / National Agricultural Workers Survey",
    },

    # ──────────────────────────────────────────────────────────────
    # GARMENT INDUSTRY UNION AND WHISTLEBLOWER RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Garment Factory Union Activist Retaliation (2015)",
        "summary": "Bangladeshi garment worker and union activist reported wage theft and unsafe conditions (factory safety not improved post-Rana Plaza). Employer retaliated by: terminating employment, filing criminal charges for 'labor unrest', and physically assaulting worker. Worker fled to India.",
        "source": "Bangladesh Garment Workers Federation / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Dhaka Garment Factory Safety Committee Member — Dismissal (2016)",
        "summary": "Worker elected to safety committee reported fire hazards to management. Factory retaliated by: firing worker, pressuring union to remove worker from committee, and preventing worker from finding employment in other factories.",
        "source": "ILO Better Work Bangladesh / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia Garment Factory Whistleblower — Termination and Blacklist (2014)",
        "summary": "Cambodian garment worker reported excessive overtime (16+ hours daily) and wage theft. Reported to labor ministry. Factory retaliated by: terminating employment, spreading false rumors about worker, and circulating name to prevent rehire in similar facilities.",
        "source": "Cambodia Labor Ministry / Better Work Cambodia",
    },
    {
        "type": "statistic",
        "jurisdiction": "BD",
        "title": "Bangladesh Garment Worker Complaints and Retaliation (2010-2024)",
        "summary": "Bangladesh Garment Workers Federation received 2,000+ complaints (2010-2024) including wage theft, unsafe conditions, retaliation. Documented retaliation: 600+ cases. Enforcement: weak. Many complainants unable to find employment.",
        "source": "Bangladesh Garment Workers Federation / ILO",
    },

    # ──────────────────────────────────────────────────────────────
    # SEAFARER WHISTLEBLOWER AND BLACKLISTING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Seafarer Wage Complaint — Flag State Dismissal (2016)",
        "summary": "Filipino seafarer reported unpaid wages (USD 50,000 owed) to ship owner. Reported to flag state (Marshall Islands). Employer retaliated by: dismissing seafarer, circulating blacklist name through maritime networks, and preventing reassignment. Seafarer unable to secure employment.",
        "source": "International Labour Organization (maritime)",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Seafarer Safety Report — Blacklist and Career Damage (2015)",
        "summary": "Seafarer reported dangerous working conditions and safety violations to International Maritime Organization. Employer retaliated by: dismissing worker, spreading negative work record, and ensuring worker unable to work on major vessel lines. Informal blacklist effective.",
        "source": "International Maritime Organization / ILO",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Convention 188 — Work in Fishing Convention (2007)",
        "summary": "ILO convention providing protections for fishing workers including whistleblower protections. However, enforcement weak, especially in developing flag states. Fishing industry known for extreme exploitation and retaliation.",
        "source": "International Labour Organization",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Maritime Blacklisting and Whistleblower Vulnerability",
        "summary": "Seafarers reporting labor violations face: informal blacklisting by shipping companies, difficulty finding employment due to negative references, career damage (retaliation recorded in work record), economic dependence (family in home country), isolation at sea (no support during retaliation).",
        "source": "International Transport Workers Federation / ILO",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Seafarer Wage and Condition Complaints (2010-2024)",
        "summary": "ILO received 3,000+ seafarer complaints (2010-2024) regarding wage theft, unsafe conditions, retaliation. Documented blacklisting: 800+ cases. Enforcement: ILO flags flag states but legal action slow. Many seafarers unable to find work.",
        "source": "ILO Maritime Labour Convention monitoring",
    },

    # ──────────────────────────────────────────────────────────────
    # DOMESTIC WORKER DISMISSAL FOR COMPLAINTS
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "US Domestic Worker Wage Complaint — Immediate Dismissal (2016)",
        "summary": "Undocumented domestic worker reported unpaid wages and excessive hours to labor board. Employer retaliated by: immediately terminating employment, refusing final paycheck, and reporting immigration status to ICE. Worker arrested and deported.",
        "source": "US Department of Homeland Security / NGO investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Hong Kong Domestic Worker Complaint — Contract Cancellation (2015)",
        "summary": "Filipina domestic worker reported physical abuse to Hong Kong authorities. Employer (expat family) retaliated by: terminating contract, withholding final wages, and reporting to immigration authorities claiming worker 'unsuitable.' Worker faced deportation.",
        "source": "Hong Kong Labour Department / Helpers for Domestic Helpers",
    },
    {
        "type": "case_study",
        "jurisdiction": "TW",
        "title": "Taiwan Domestic Worker Abuse Report — Deportation (2017)",
        "summary": "Indonesian domestic worker reported sexual harassment and abuse to Taiwan authorities. Employer retaliated by: claiming worker was 'unsuitable', initiating repatriation, and preventing worker from seeking alternative employment.",
        "source": "Taiwan Council of Labor Affairs / IOM Taiwan",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Domestic Worker Vulnerability and Whistleblower Risk",
        "summary": "Domestic workers face extreme vulnerability: isolated in employer homes, economically dependent (wages sent to family), documented or undocumented status concerns, language barriers, no witnesses to abuse, power imbalance with employer. Reporting virtually guarantees dismissal.",
        "source": "International Labour Organization / ILO Convention 189",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Domestic Worker Complaints and Dismissals (2010-2024)",
        "summary": "ILO estimates 250,000+ domestic workers filed complaints globally (2010-2024). Dismissal rate following complaint: 85%+. Wage recovery: <10%. Retaliation prosecution: <1% of cases.",
        "source": "International Labour Organization Convention 189 monitoring",
    },

    # ──────────────────────────────────────────────────────────────
    # T-VISA AND U-VISA FRAMEWORKS (US)
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "T-Visa — Trafficking Victims Protection Act Visa",
        "summary": "US immigration visa for trafficking victims in exchange for cooperation with law enforcement. Provides: legal status, work authorization, social services, protection from deportation. However, only 5,000 annually available; 90% go to foreign nationals (not US citizens).",
        "source": "8 U.S.C. § 1101(a)(15)(T) / US Department of State",
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "U-Visa — Victims of Crime and Cooperation Visa",
        "summary": "US visa for victims of crimes (including trafficking, labor violations, witness intimidation) who cooperate with law enforcement. Provides legal status, work authorization, social services. However, limited availability (10,000 annually); backlog of applications.",
        "source": "8 U.S.C. § 1101(a)(15)(U) / US Department of Homeland Security",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "T-Visa Case — Agricultural Worker Trafficked and Retaliated (2015)",
        "summary": "Mexican agricultural worker reported trafficking to DOL and federal agents. Employer retaliated by: threatening family in Mexico, attempting to intimidate worker against cooperation, and hiding worker from law enforcement. Worker eventually received T-visa and relocation assistance.",
        "source": "US Department of Homeland Security / ICE Homeland Security Investigations",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "U-Visa Domestic Worker Case — Delayed Adjudication and Vulnerability (2016)",
        "summary": "Undocumented domestic worker reported trafficking and abuse to police. Filed U-visa petition. Visa processing took 3 years during which worker remained undocumented and vulnerable to employer retaliation. Eventually granted U-visa but psychological trauma persistent.",
        "source": "US Department of Homeland Security / USCIS",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "T-Visa and U-Visa Processing Delays and Vulnerability",
        "summary": "Major issue: T and U visa applicants wait years for adjudication while remaining vulnerable to retaliation. During waiting period: no work authorization, at risk of deportation, subject to continued employer retaliation, witnesses may be intimidated or killed.",
        "source": "US Trafficking in Persons Report / NGO analysis",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "T-Visa and U-Visa Issuance (2010-2024)",
        "summary": "T-visas issued: 2,000-3,000 annually (below 5,000 cap). U-visas issued: 6,000-8,000 annually (below 10,000 cap). Estimated trafficking victims in US: 100,000+. Coverage rate: 2-3%. High demand, very limited supply.",
        "source": "US Department of State / USCIS annual reports",
    },

    # ──────────────────────────────────────────────────────────────
    # EMPLOYER RETALIATORY REPORTING TO IMMIGRATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Retaliatory Immigration Report — ICE Enforcement Consequence (2015)",
        "summary": "Undocumented worker reported wage theft to DOL. Employer retaliated by reporting worker's immigration status to ICE. Worker arrested at home, detained 60 days, eventually deported. No retaliation prosecution against employer.",
        "source": "US Immigration and Customs Enforcement / DOL investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Multiple Workers — Immigration Threat for Union Organizing (2014)",
        "summary": "Restaurant workers (mixed-status workforce) attempted union organizing. Employer threatened to report undocumented workers to ICE if organizing continued. Workers abandoned efforts. NLRB could not prosecute employer because threat of reporting immigration status not covered by NLRA.",
        "source": "National Labor Relations Board / labor advocacy group",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Immigration Status as Retaliation Tool — Employer Leverage",
        "summary": "Major enforcement gap: employers use threat of immigration enforcement as retaliation tool against undocumented workers who report labor violations. US law prohibits retaliation but immigration reporting creates secondary consequence (deportation) beyond employment.",
        "source": "US Department of Labor / NGO research",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "Retaliatory Immigration Reports (Estimated, 2010-2024)",
        "summary": "Estimates suggest employers make 10,000-20,000+ retaliatory immigration reports annually when workers file labor complaints. Actual documented cases: <500. Massive underreporting and enforcement gap.",
        "source": "NGO research / US Department of Labor advocacy",
    },

    # ──────────────────────────────────────────────────────────────
    # PALESTINE AND MIGRANT WORKER RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PS",
        "title": "Palestinian Authority Migrant Worker Complaint — Retaliation (2016)",
        "summary": "Filipino worker reported wage theft to Palestinian Labor Authority. Employer retaliated by: terminating employment, withholding wages, and reporting to immigration authorities. Worker deported within days.",
        "source": "Palestinian Ministry of Labor / IOM",
    },
    {
        "type": "advisory",
        "jurisdiction": "PS",
        "title": "Palestinian Authority Migrant Worker Protections — Limited Enforcement",
        "summary": "Palestinian Authority has labor laws protecting workers including whistleblower protections. However, enforcement weak, retaliation common, and deported workers rarely receive justice or compensation.",
        "source": "International Labour Organization / Palestinian Authority",
    },

    # ──────────────────────────────────────────────────────────────
    # LEBANON DOMESTIC WORKER RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "LB",
        "title": "Lebanon Domestic Worker Wage Complaint — Confinement and Abuse (2017)",
        "summary": "Ethiopian domestic worker reported wage theft to labor authority. Employer retaliated by: confining worker to house, denying food, threatening violence, and preventing worker from contacting embassy. Worker escaped with help of NGO.",
        "source": "Lebanon Ministry of Labour / Human Rights Watch",
    },
    {
        "type": "advisory",
        "jurisdiction": "LB",
        "title": "Lebanon Kafala System and Domestic Worker Vulnerability",
        "summary": "Lebanon kafala system (sponsorship) ties worker to specific employer. Domestic workers excluded from labor law. Complaint to authorities often triggers retaliation, confinement, and deportation.",
        "source": "Amnesty International / Human Rights Watch",
    },

    # ──────────────────────────────────────────────────────────────
    # CANADA AGRICULTURAL WORKER RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "CA",
        "title": "Canadian Agricultural Worker — Retaliation for Safety Complaint (2015)",
        "summary": "Mexican temporary agricultural worker reported workplace injury and unsafe conditions to provincial labor ministry. Employer retaliated by: terminating employment, not paying final wages, and blacklisting worker for future seasons.",
        "source": "Canadian Labour Standards / Provincial Labour Ministry",
    },
    {
        "type": "law",
        "jurisdiction": "CA",
        "title": "Canada Labour Code — Whistleblower Protection Part 2",
        "summary": "Canadian federal law prohibiting retaliation against workers reporting safety violations or engaging in protected activity. Covers federal jurisdiction industries. Provincial variations less protective.",
        "source": "Canada Labour Code, Part II",
    },

    # ──────────────────────────────────────────────────────────────
    # AUSTRALIA SEASONAL WORKER RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australian Seasonal Worker Program Retaliation (2016)",
        "summary": "Vanuatu seasonal worker reported wage theft to Australian authorities. Employer retaliated by: terminating employment, preventing job transfer, and blacklisting from future seasons.",
        "source": "Australian Department of Home Affairs / Fair Work Commission",
    },
    {
        "type": "law",
        "jurisdiction": "AU",
        "title": "Australia Fair Work Act — Whistleblower and Adverse Action Protections",
        "summary": "Australian law prohibiting adverse action (including retaliation) against workers for engaging in protected activity. Covers: union activity, safety reports, work conditions complaints. Applies to all workers including temporary visa holders.",
        "source": "Fair Work Act 2009 (Cth)",
    },

    # ──────────────────────────────────────────────────────────────
    # NEW ZEALAND MIGRANT WORKER RETALIATION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NZ",
        "title": "New Zealand Migrant Worker Wage Complaint — Visa Threat (2015)",
        "summary": "Filipino seasonal worker complained to Labor Inspectorate about unpaid wages. Employer retaliated by: threatening work visa cancellation, preventing job transfer, and imposing conditions on continued employment.",
        "source": "New Zealand Labour Inspectorate",
    },

    # ──────────────────────────────────────────────────────────────
    # LEGAL FRAMEWORKS AND INTERNATIONAL STANDARDS
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Convention 87 — Freedom of Association and Right to Organize (1948)",
        "summary": "ILO convention guaranteeing workers' right to form organizations and engage in labor activity without retaliation. 157 state parties. Foundation for whistleblower protections in labor disputes.",
        "source": "International Labour Organization",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Convention 98 — Right to Organize and Bargain Collectively (1949)",
        "summary": "ILO convention requiring states to ensure protection against anti-union discrimination and retaliation. Includes protection for workers who report violations. 161 state parties.",
        "source": "International Labour Organization",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "UN Convention Against Torture — Protection from Retaliation",
        "summary": "UNCAT Article 13 requires states to provide victim access to complaint procedures. Applies to whistleblowers reporting torture/abuse. Limited effectiveness due to enforcement gaps.",
        "source": "UN Convention Against Torture",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Forced Labor Convention 29 — Whistleblower Protections Implicit",
        "summary": "ILO C29 (1930) requires states to suppress forced labor. Implies whistleblower protections for those reporting forced labor conditions. However, explicit protections limited.",
        "source": "International Labour Organization",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Global Whistleblower Protection Gap — Summary",
        "summary": "Significant enforcement gap globally: legal protections exist but enforcement weak. Common issues: retaliation prosecution rare, remedies insufficient (back pay only), no deterrent effect, worker unable/unwilling to follow up, deportation prevents case completion.",
        "source": "International Labour Organization / Transparency International",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Retaliation as Percentage of All Labor Violations (2010-2024)",
        "summary": "ILO research suggests retaliation accounts for 20-30% of documented labor violations globally. However, retaliation often goes unreported due to fear. Estimated true retaliation rate: 50%+ of cases.",
        "source": "International Labour Organization research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Whistleblower Protection Effectiveness Factors",
        "summary": "Effective protections require: clear legal prohibitions, independent enforcement agency, whistleblower legal aid, employer penalties exceeding retaliation benefit, worker confidentiality, immigration status protection, international cooperation, victim support services.",
        "source": "International Labour Organization best practices",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Systemic Retaliation — Employer Cooperation Networks",
        "summary": "Documented pattern: employers cooperate to share names of 'troublemakers' (whistleblowers) to prevent rehire across industry. Common in agriculture, construction, domestic work. Creates effective blacklist preventing employment.",
        "source": "NGO investigations / labor advocacy groups",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Retaliation as Forced Labor Indicator",
        "summary": "ILO Forced Labor Indicator 10 (Excessive Overtime/Abusive Conditions): retaliation for refusing excessive work is indicator of forced labor. Similarly, retaliation for reporting is control mechanism characteristic of trafficking.",
        "source": "International Labour Organization Forced Labor Indicators",
    },
    {
        "type": "penalty",
        "jurisdiction": "international",
        "title": "Retaliation Penalties — Global Inadequacy",
        "summary": "Globally, retaliation penalties typically: fines USD 1,000-50,000 (often reduced on appeal), wage recovery only, rarely criminal prosecution, extremely rare imprisonment. Penalty does not deter when potential gain from exploitation is USD 100,000+.",
        "source": "ILO case law analysis",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Whistleblower Case Duration and Dropout Rate",
        "summary": "Global average: retaliation cases take 2-5 years to resolve. Worker dropout rate: 40-60% (due to deportation, economic need, fear, lack of legal aid). Cases completed to resolution: <50%.",
        "source": "International Labour Organization / NGO research",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Deportation Before Case Resolution — Systematic Gap",
        "summary": "Common pattern: worker files complaint, employer retaliates with deportation, worker deported before case adjudication. Employer wins by default. Documented in US, Gulf states, Asia, Europe.",
        "source": "Multiple NGO investigations",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Whistleblower Psychological Trauma and Health Effects",
        "summary": "Retaliation creates psychological harm: anxiety, depression, PTSD, inability to trust authority, family separation trauma. Support services rare. Long-term effects: workers unable to continue employment even if reinstated.",
        "source": "Psychological research / NGO victim support organizations",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Successful Whistleblower Protection Case — Rare Example (EU)",
        "summary": "Hungarian farmworker reported exploitation, pursued case through EU Whistleblower Directive. Employer convicted of retaliation, sentenced to probation. Worker received reinstatement and compensation. Rare success case highlighting importance of robust legal framework.",
        "source": "EU Court records",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Migrant Worker-Specific Retaliation Vulnerabilities",
        "summary": "Migrant workers face compounded retaliation vulnerability: language barriers, legal status uncertainty, cultural unfamiliarity, isolation from support networks, economic dependence, family obligations, fear of deportation, limited knowledge of rights.",
        "source": "International Labour Organization / IOM research",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Estimated Global Whistleblower Retaliation Cases (2010-2024)",
        "summary": "Estimate: 2,000,000+ migrant workers experienced retaliation for reporting labor violations globally (2010-2024). Formal complaints filed: <50,000. Enforcement actions: <10,000. Prosecution rate: <1%.",
        "source": "ILO / IOM / NGO research compilation",
    },

    # ──────────────────────────────────────────────────────────────
    # ADDITIONAL REGIONAL AND SECTOR-SPECIFIC CASES
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia Domestic Worker Trafficking Report — Agency Retaliation (2016)",
        "summary": "Bangladeshi domestic worker reported exploitation to Malaysian labor authority. Recruitment agency retaliated by: blacklisting worker name, preventing job changes, and threatening legal action. Worker remained in situation unable to exit.",
        "source": "Malaysian Ministry of Human Resources / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand Seafood Factory Worker Escape and Retaliation (2017)",
        "summary": "Cambodian worker escaped seafood factory after reporting conditions to NGO. Factory retaliated by: circulating worker's name as 'thief', filing false theft charges, and threatening family in Cambodia. Legal case pending 4+ years.",
        "source": "Thai Labor Ministry / NGO investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "India Garment Factory Union Organizer — Threat and Intimidation (2015)",
        "summary": "Indian garment worker attempted to organize factory employees for union recognition. Factory retaliated by: assigning dangerous tasks, reducing pay, physically assaulting worker, and threatening family members.",
        "source": "Indian labor authority / union records",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Brick Kiln Worker Debt Report — Confinement and Violence (2016)",
        "summary": "Pakistani brick kiln worker reported debt bondage to authorities. Employer retaliated by: physically assaulting worker, confining worker and family, increasing debt through penalties, and threatening lethal violence.",
        "source": "Pakistan's Labour Department / NGO investigation",
    },
    {
        "type": "law",
        "jurisdiction": "MX",
        "title": "Mexico Labor Protections Against Retaliation — Limited Enforcement",
        "summary": "Mexico has labor laws prohibiting retaliation against workers reporting violations. However, enforcement extremely weak, corruption common, and workers often unaware of protections.",
        "source": "Mexican Labor Ministry",
    },
    {
        "type": "case_study",
        "jurisdiction": "MX",
        "title": "Mexico Sugarcane Worker Complaint — Family Intimidation (2015)",
        "summary": "Guatemalan guest worker reported labor violations on Mexican sugarcane plantation. Employer retaliated by: threatening to report worker to immigration, visiting family in Guatemala to threaten them, and preventing worker exit.",
        "source": "Mexican labor authority / human rights group",
    },
    {
        "type": "case_study",
        "jurisdiction": "GT",
        "title": "Guatemala Coffee Plantation Worker — Deportation for Organizing (2014)",
        "summary": "Worker attempted to organize plantation employees for better conditions. Employer coordinated with government to deport worker as 'agitator.' Worker deported; organizing collapsed.",
        "source": "Guatemalan Ministry of Labor / union records",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Employer-State Coordination in Retaliation",
        "summary": "Documented pattern: employers coordinate with government immigration authorities to deport whistleblowing workers. Government officials incentivized by employer payments or threats. Employer uses state apparatus for retaliation.",
        "source": "International Labour Organization / NGO investigations",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal Migrant Worker (Gulf-Bound) Complaint — Agent Retaliation (2016)",
        "summary": "Worker reported recruitment fraud to Nepali authorities before departure. Recruitment agent retaliated by: refusing to process worker visa (blocking opportunity), spreading rumors about worker, and blocking worker access to other agencies.",
        "source": "Nepal Ministry of Foreign Employment / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Philippines Overseas Worker Trafficking Report — Agency Retaliation (2015)",
        "summary": "Filipino overseas worker reported human trafficking to POEA (Philippine Overseas Employment Administration). Recruitment agency retaliated by: blacklisting worker, spreading negative references, and preventing future overseas employment.",
        "source": "POEA / Philippine labor authority",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia Domestic Worker Complaint to Embassy — Arrest on Return (2017)",
        "summary": "Indonesian domestic worker reported abuse to embassy while employed overseas. Upon return to Indonesia, police arrested worker on fabricated charges filed by employer through diplomatic channels. Workers rights organization assisted in case.",
        "source": "Indonesian Ministry of Overseas Workers / IOM",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Protocol to Convention 29 — Supplementary Whistleblower Language",
        "summary": "2014 ILO protocol to C29 (Forced Labor) includes stronger whistleblower protections language. States should ensure workers reporting forced labor can do so safely without retaliation.",
        "source": "International Labour Organization",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Recruitment Agent Role in Retaliation",
        "summary": "Recruitment agencies functioning as intermediary layer enabling retaliation: they blacklist workers, control job matching, spread negative information. Agency retaliation may prevent worker access to entire labor market segment.",
        "source": "IOM / ILO research on recruitment systems",
    },
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Hong Kong Migrant Worker Paid Leave Demand — Dismissal (2016)",
        "summary": "Indonesian domestic worker requested unpaid leave to handle family emergency (per labor law). Employer retaliated by: refusing request, then firing worker on fabricated charges, and reporting worker to immigration.",
        "source": "Hong Kong Labour Department / NGO",
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Singapore Construction Worker Safety — Retaliation and Injury Non-Payment (2015)",
        "summary": "Worker reported near-miss safety incident to Singapore MOM. Employer retaliated by: reassigning worker to more hazardous duties, reducing pay, and (when worker was injured) refusing to pay compensation.",
        "source": "Singapore Ministry of Manpower / workers rights organization",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Unreported Retaliation — Estimated Hidden Cases",
        "summary": "For every documented retaliation case, estimated 10-20 go unreported. Reasons: fear, language barriers, legal status, lack of knowledge of rights, distrust of authorities, economic dependence, isolation.",
        "source": "International Labour Organization / NGO research",
    },
    {
        "type": "case_study",
        "jurisdiction": "KZ",
        "title": "Kazakhstan Oil Industry Worker — Retaliation for Safety Report (2015)",
        "summary": "Russian migrant worker reported safety violations at oil facility. Employer retaliated by: terminating employment, canceling work visa, and circulating name to prevent employment at other facilities.",
        "source": "Kazakhstan Ministry of Labour / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "title": "Kuwait Domestic Worker Abuse Report — Embassy Deportation (2016)",
        "summary": "Female migrant worker reported sexual harassment and physical abuse to home country embassy. Employer retaliated by: reporting worker to Kuwait authorities as 'violating contract', leading to immediate deportation.",
        "source": "Kuwaiti Ministry of Interior / home country embassy",
    },
    {
        "type": "case_study",
        "jurisdiction": "BH",
        "title": "Bahrain Construction Complaint — Job Loss and Visa Cancellation (2015)",
        "summary": "Nepali construction worker reported wage theft and dangerous working conditions. Employer retaliated by: terminating employment, canceling visa, and filing complaint with labor ministry against worker for 'breach of contract.'",
        "source": "Bahrain Ministry of Labour / IOM",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Visa Sponsorship as Retaliation Tool — Systemic Issue",
        "summary": "Kafala and sponsorship systems make visa status dependent on single employer. This creates systemic retaliation vulnerability: employer can terminate visa instantly, converting lawful status to illegal, triggering deportation.",
        "source": "International Labour Organization / human rights organizations",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Third-Country Retaliation — Family Threats Across Borders",
        "summary": "Documented pattern: employers/agents retaliate against whistleblowing workers by threatening/harming family members in home country. Involves corruption of local authorities in origin countries.",
        "source": "IOM / NGO investigations",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Retaliation Severity — Physical Harm and Psychological Trauma",
        "summary": "Retaliation severity escalates: 30% verbal threats, 25% job loss, 20% wage forfeiture, 15% physical harm, 10% family threats. Multiple forms common. Psychological impact severe in 60%+ of cases.",
        "source": "International Labour Organization research compilation",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Palermo Protocol — Trafficking Definition and Whistleblower Implications",
        "summary": "UN Palermo Protocol defines trafficking including elements triggered by whistleblower retaliation (coercion, threat, abuse of power). Retaliation against trafficking victim whistleblowers may itself constitute trafficking crime.",
        "source": "UN Office on Drugs and Crime",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Intersectional Vulnerability in Retaliation",
        "summary": "Certain workers face compounded retaliation risk: women (gender-based violence), undocumented (deportation), trafficking victims (fear), minorities (discrimination), disabled (job loss), LGBTQ+ (persecution). Single-identity protections inadequate.",
        "source": "International Labour Organization / human rights research",
    },
]
