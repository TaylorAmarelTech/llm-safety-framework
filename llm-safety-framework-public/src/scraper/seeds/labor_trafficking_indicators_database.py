"""Labor trafficking indicators database covering 11 ILO indicators, UNODC framework, Polaris Project typology, and international screening tools."""

LABOR_TRAFFICKING_INDICATORS_DATABASE_FACTS: list[dict] = [
    # ─────────────────────────────────────────────────────────────────────────
    # ILO 11 FORCED LABOR INDICATORS - DETAILED BREAKDOWN
    # ─────────────────────────────────────────────────────────────────────────

    # 1. ABUSE OF VULNERABILITY - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 1.1: Targeting Vulnerable Groups for Recruitment",
        "summary": "Recruiters specifically target individuals from low-income areas, disaster-affected regions, post-conflict zones, or discriminated communities. Targeting refugees, stateless persons, undocumented migrants, persons with disabilities, or isolated groups indicates abuse of vulnerability. High youth unemployment and illiteracy increase risk.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 1.2: Exploitation of Poverty and Lack of Alternatives",
        "summary": "Workers accept exploitative conditions due to extreme poverty, lack of employment alternatives, or no livelihood options. Debt bondage schemes exploit this by offering loans at high interest. Seasonal workers and agricultural laborers particularly vulnerable.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 1.3: Targeting Individuals with Unstable Migrant Status",
        "summary": "Employers and recruiters target irregular migrants, visa overstayers, undocumented workers, or those on tourist visas. Inability to contact authorities or seek legal protection makes them ideal victims. Status misrepresentation during recruitment is common.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 1.4: Lack of Awareness and Language Barriers",
        "summary": "Workers unfamiliar with destination laws, labor rights, or remedies cannot recognize abuse. Language barriers prevent communication with authorities. Illiteracy prevents reading contracts. Recruiters provide false information about rights and conditions.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 1.5: Discrimination as Recruitment Tool",
        "summary": "Discrimination based on ethnicity, caste, gender, religion, or disability makes individuals vulnerable. Marginalised groups including Dalits, indigenous peoples, ethnic minorities, and LGBTQ+ persons face reduced labor market access and are targeted by traffickers.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 2. DECEPTION - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 2.1: False Promises in Recruitment",
        "summary": "Recruiters promise high wages, specific job titles, or favorable conditions that do not materialize. Common lies: USD 2,000/month becomes USD 300; hospitality job becomes domestic work; 8-hour days become 16-hour days; promised benefits never provided. Usually discovered upon arrival.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 2.2: Non-Disclosure or Misrepresentation of Job Terms",
        "summary": "Job descriptions omit or conceal essential terms: hours of work, wage calculation, deductions, accommodation costs, living conditions, contract duration, or termination clauses. Verbal contracts replaced by written contracts with different terms. Job location differs from promised.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 2.3: Misrepresentation of Working Conditions",
        "summary": "Workers promised safe, clean, modern workplaces find extreme heat, hazardous chemicals, lack of protective equipment, or disease exposure. Safety training withheld. Injury rates not disclosed. Environmental conditions not mentioned (dusty quarries, extreme temperatures, toxic fumes).",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 2.4: Concealment of Recruitment and Employment Fees",
        "summary": "Workers told jobs are fee-free, then discover deductions for placement, visa processing, medical exams, training, housing, or 'administrative costs'. Fees compound through multiple agents. Workers inherited pre-existing debt from previous workers.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 2.5: Contract Substitution at Destination",
        "summary": "Workers sign one contract at origin, receive different contract at destination. Original terms replaced: salary reduced, hours extended, responsibilities changed, job location different, employer changed, or duration extended. Workers unable to return to origin country due to sunk costs.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 3. RESTRICTION OF MOVEMENT - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 3.1: Confinement to Workplace or Living Quarters",
        "summary": "Workers prohibited from leaving workplace except for essential errands. Doors locked, guards posted, or movement tracked. Living on employer's premises with no keys to rooms/compound. Required to request permission for all movements. Confinement at night is standard.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 3.2: Isolation from Support Networks",
        "summary": "Employer houses multiple workers in isolated accommodations far from communities or services. No access to transportation, markets, or shops. Reliance on employer for all supplies creates dependency. Workers unable to visit family, friends, or organizations outside work.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 3.3: Restriction of Movement by Threats or Debt",
        "summary": "Debt used to prevent departure: 'leaving incurs penalty' or 'debt adds interest'. Threats of arrest, deportation, violence, or family harm if worker attempts to leave. Promises of freedom of movement at contract end never honored. Constant debt increases make departure impossible.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 3.4: Restriction of Movement Through Document Confiscation",
        "summary": "Passports, visas, work permits, or identity documents confiscated on arrival by employer, agent, labor contractor, or sponsor. Kept in locked safe or with third party. Workers cannot travel without documents. Confiscation often claimed as 'safekeeping' but never returned.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 3.5: Restriction of Movement Through Dependency",
        "summary": "Workers dependent on employer for housing, food, transportation, and all basic services. Living in employer-provided accommodation, eating employer-provided meals, commuting via employer transport. No alternative sources means any restriction is movement control.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 4. ISOLATION - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 4.1: Linguistic Isolation",
        "summary": "Workers placed in locations where their language is not spoken. No workers from their ethnic/cultural background. No interpreters available. Unable to communicate with authorities, lawyers, NGOs, or support organizations. Prevents reporting of abuse or seeking help.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 4.2: Denial of Communication Access",
        "summary": "Mobile phones confiscated or blocked. Internet access prohibited or monitored. No access to phone calls. Restricted mail. Monitored messaging. Employer screens communication with family. Prevented from using public phones. Communication attempts result in punishment.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 4.3: Denial of Rest Days and Private Time",
        "summary": "Workers not given rest days or days off. No time alone or with family. Continuous supervision or expectation to be available. Sleep time minimal or interrupted. No privacy in accommodations (multiple workers per room, no lockable doors). Denied time to contact anyone.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 4.4: Exclusion from Community and Social Activities",
        "summary": "Prevented from participating in community activities, religious gatherings, or social events. Forbidden from attending schools, community centers, or public spaces. No social interaction with non-family members. Complete separation from normal community life.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 5. PHYSICAL AND SEXUAL VIOLENCE - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 5.1: Physical Violence and Punishment",
        "summary": "Beatings, slapping, kicking, or physical punishment for mistakes, slowness, or non-compliance. Punishment methods: whipping, caning, hitting with tools, or forcing into painful positions. Visible bruises or injuries. Collective punishment for one worker's actions.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 5.2: Sexual Violence and Exploitation",
        "summary": "Sexual harassment, assault, or rape by employers, supervisors, or coworkers. Sexual coercion for wages, accommodation, or protection. Sex work demands. Nonconsensual intimate contact. Particularly prevalent in domestic work, hospitality, and agriculture sectors.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 5.3: Medical and Reproductive Coercion",
        "summary": "Forced contraception, sterilization, or reproductive decisions. Denying medical care during pregnancy/childbirth. Forced abortions or miscarriage-inducing work conditions. Medical information used to control workers. Reproductive history used as punishment.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 5.4: Violence as Coercion Mechanism",
        "summary": "Violence used strategically to enforce compliance: beatings after disobedience, punishments for escape attempts, witness to others' beatings creating fear. Violence establishes clear hierarchy and removes any thought of resistance.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 6. INTIMIDATION AND THREATS - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 6.1: Threats to Worker or Family",
        "summary": "Explicit threats of violence, harm, or death to worker or family members. Threats of kidnapping children. Threats against family members in home country. Demonstrated capacity to carry out threats (previous violence, connections to criminal networks). Threats escalate refusal attempts.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 6.2: Threats of Immigration Status Changes",
        "summary": "Threats to cancel visa, report to immigration, arrange deportation, or file false charges. In irregular migration: threats to call police or detention authorities. Threats exploit fear of arrest, detention, or forced return. Particularly effective against irregular migrant workers.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 6.3: Threats of Economic Harm",
        "summary": "Threats to withhold all wages, increase debt, file false claims, charge penalties, or seize assets. Threats to cancel benefits, pensions, or employment history. Threats to destroy savings or prevent remittance of earnings. Economic threats create dependency.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 6.4: Threats of Reputational Harm",
        "summary": "Threats to spread rumors, damage reputation, publish false information, or ostracize from community. In collectivist cultures: threats of family shame or dishonor. Threats to report to community leaders. Threatens social standing and marriage prospects.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 7. RETENTION OF IDENTITY DOCUMENTS - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 7.1: Document Confiscation on Arrival",
        "summary": "Passports, visas, work permits, national IDs, or other travel/identity documents confiscated immediately on arrival. Claimed justifications: 'bank safekeeping', 'visa processing', 'security', 'simplifying administration'. Documents never returned. Workers made undocumented by employer action.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 7.2: Document Retention Creating Dependency",
        "summary": "Employer holds documents claiming they will be returned on contract completion or debt repayment. Document release becomes leverage: 'Follow orders or stay longer.' Without documents, workers cannot travel, change jobs, access services, or claim identity. Dependency mechanism.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 7.3: Document Destruction or Loss",
        "summary": "Employer 'loses' or destroys documents, making workers undocumented. Prevents departure (unable to travel without documents). Prevents reporting (undocumented status means arrest risk). Destroys evidence of right to work. Document destruction used as excuse for wage non-payment.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 7.4: False Document Procurement",
        "summary": "Employer obtains fraudulent visas, work permits, or identity documents for workers. Fake documents used to control workers ('I got you illegal docs, you must obey'). Documents used to bind workers to employer. Criminal record created by false document use.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 8. WITHHOLDING OF WAGES - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 8.1: Wage Non-Payment or Partial Payment",
        "summary": "Employer fails to pay wages on scheduled dates or pays only partial amounts. Common justifications: 'money not yet received', 'accounting issues', 'penalty for mistakes', 'will pay later', or complete denial of payment obligation. Workers receive nothing for weeks or months of work.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 8.2: Systematic Wage Deductions",
        "summary": "Employer deducts large portions of wages for: accommodation (20-40%), food (10-20%), utilities, transportation, 'breakage', 'mistakes', fines, penalties, tools, uniforms, or undefined 'charges'. Deductions not agreed in writing. Take-home pay becomes minimal or zero.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 8.3: Wage Deception and Calculation Fraud",
        "summary": "Employer manipulates wage calculations: pays at piece-rate but pieces counted incorrectly, pays daily rate but days calculated differently, adds false deductions, or keeps duplicate ledgers. Workers unable to verify calculations. Underpayment disguised as correct payment.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 8.4: Wages Held Until Contract End or Departure",
        "summary": "Employer withholds all or significant portion of wages until contract completion or worker departure. Justification: 'security deposit', 'preventing runaway', or 'final payment'. Workers receive minimal monthly payments, with bulk owed at end. Creates debt-like bondage.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 9. DEBT BONDAGE - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 9.1: Excessive or Fabricated Recruitment Debt",
        "summary": "Workers charged high fees for recruitment: USD 1,000-5,000 or equivalent. Fees for visa processing (gov't fee + agent mark-up), medical exams, training, document certification, or undefined 'placement services'. Fees paid to multiple agents in chain, each adding markup. Debt often exceeds several months of wages.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 9.2: Debt Accumulation and Compounding",
        "summary": "Initial recruitment debt grows through: compound interest (10-30% monthly), charges for accommodation/food, transportation costs, medical treatment, tool provision, uniform costs, contract renewal fees, or 'administrative charges'. Debt increases faster than wages can repay. Contractually indefinite repayment period.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 9.3: Debt Used as Bondage Mechanism",
        "summary": "Debt explicitly used to control workers: 'You cannot leave until debt is repaid.' Debt creates binding obligation to continue work. Debt transferred between employers, preventing job changes. Debt used as justification for wage withholding or poor conditions ('You owe us, you take what we give').",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 9.4: Debt Unpayability and Intergenerational Transfer",
        "summary": "Debt structured to be mathematically unpayable: compounds exceed earnings, deductions eliminate payments, or duration extended repeatedly. Debt passed to family members or next generation if worker cannot repay. Debt used as long-term control mechanism across years or decades.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 10. ABUSIVE WORKING CONDITIONS - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 10.1: Excessive Hours and No Rest Days",
        "summary": "Workers required to work 12-18+ hours daily, 6-7 days per week, with no scheduled rest days. Overtime mandatory with no additional compensation. Sleep hours minimal (4-5 hours). No time for personal hygiene, meals, or family contact. Continuous work cycles create exhaustion.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 10.2: Hazardous Working Conditions and Exposure",
        "summary": "Workers exposed to hazards without protection: extreme heat (construction, agriculture), toxic chemicals (manufacturing, agriculture), dust or fumes, dangerous machinery, biological hazards, or unsafe working heights. No protective equipment, training, or safety protocols. High injury/illness/death rates.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 10.3: Denial of Medical Care and Benefits",
        "summary": "Employers refuse to provide medical treatment for work-related injuries or illnesses. Workers forced to continue work while injured. Insurance or compensation denied. Medical costs deducted from wages. Workers unable to access external medical care (isolation, expense, or threat).",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 10.4: Substandard Living Conditions",
        "summary": "Accommodations overcrowded, unsanitary, or unsafe: 10-20 people per room, no toilets, no clean water, no electricity, leaking roofs, or structural hazards. Food inadequate in quantity/quality or contaminated. No healthcare facilities. Living conditions constitute punishment or degradation.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # 11. EXCESSIVE OVERTIME - ILO Indicator Set
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 11.1: Mandatory Overtime Without Consent or Compensation",
        "summary": "Overtime work required without worker consent or option to refuse. Refusal results in wage deduction, harassment, or punishment. Overtime often unpaid or paid at base rate (not premium rate). No maximum hours regulations enforced. Systematic overtime from contract start.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ILO Indicator 11.2: Excessive Overtime Cumulative Effect",
        "summary": "Overtime hours accumulate to 15-25+ hours daily or 90-100+ hours weekly. Sustained over months or years causing chronic exhaustion, health deterioration, and inability to resist employer demands. Excessive hours prevent sleep, proper nutrition, or family contact.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicator 11.3: Overtime as Control and Debt Mechanism",
        "summary": "Overtime structured as penalty ('Extra hours for mistakes'), trap ('overtime to repay debt'), or control ('continue or lose job'). Overtime wages kept by employer as debt repayment. Excessive overtime used as punishment for resistance or escape attempts.",
        "source": "ILO Forced Labour Convention, 1930 (No. 29) - Indicator Manual",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # UNODC TRAFFICKING INDICATORS FRAMEWORK
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "UNODC Indicator: Use of Manipulation and False Promises",
        "summary": "Recruitment through deception: fake job interviews, false testimonials from previous workers, manipulation through personal relationships, false documentation, or impersonation of legitimate recruitment agencies. UNODC identifies as primary indicator.",
        "source": "UNODC Indicators of Trafficking in Persons",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "UNODC Indicator: Isolation and Control Through Confinement",
        "summary": "UNODC identifies confinement to compound/facility, guards at entrances, locks on rooms/buildings, and inability to leave without supervision. Isolation combined with control creates trafficking environment regardless of formal consent.",
        "source": "UNODC Indicators of Trafficking in Persons",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNODC Indicator: Financial Exploitation and Debt Dependency",
        "summary": "UNODC emphasizes debt bondage as primary control mechanism: unmanageable debt, compounding charges, debt transfers between employers, debt inheritance by family. Debt used to justify confinement and wage withholding.",
        "source": "UNODC Indicators of Trafficking in Persons",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNODC Indicator: Abuse, Violence, and Threat Demonstration",
        "summary": "UNODC identifies active violence (beatings, sexual assault), visible injuries, threats delivered in person or through intermediaries, and demonstration of capacity to harm (witnessed violence on others). Establishes coercion through fear.",
        "source": "UNODC Indicators of Trafficking in Persons",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNODC Indicator: Document Confiscation and Identity Control",
        "summary": "UNODC identifies document confiscation as nearly universal trafficking indicator: confiscation on arrival, documents locked in safe, held 'for safekeeping', or claimed as 'insurance'. Creates undocumented status enabling control.",
        "source": "UNODC Indicators of Trafficking in Persons",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "UNODC Indicator: Irregular Employment and Cash-Only Payment",
        "summary": "UNODC identifies: no written contracts, payment in cash with no record-keeping, no payslips, cash payment to employers not workers, payment withheld regularly, or payment only when employer chooses.",
        "source": "UNODC Indicators of Trafficking in Persons",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "UNODC Indicator: Structural Labor Conditions Incompatible with Human Dignity",
        "summary": "UNODC identifies: extreme working hours (16+ hour days), no time off or rest days, dangerous conditions without protection, no healthcare, inadequate food, unsanitary housing, child labor indicators, or work-related injuries.",
        "source": "UNODC Indicators of Trafficking in Persons",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNODC Indicator: Recruitment by Organized Networks",
        "summary": "UNODC identifies trafficking via: organized recruitment agencies operating across borders, multiple agents in chain each taking fees, recruitment targeting specific vulnerable groups, organized housing/transport, and coordination with employers.",
        "source": "UNODC Indicators of Trafficking in Persons",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # POLARIS PROJECT TRAFFICKING TYPOLOGY FRAMEWORK
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Polaris Project: Domestic Work Trafficking Typology",
        "summary": "Polaris identifies domestic work as high-trafficking sector: passport confiscation (95% of cases), confinement (92%), wage theft (91%), sleep deprivation (83%). Vulnerability factors: gender (primarily women), migration status, and employer-controlled housing.",
        "source": "Polaris Project Typology Research",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Polaris Project: Labor Trafficking in Construction and Manufacturing",
        "summary": "Polaris identifies construction/manufacturing trafficking indicators: overcrowded housing, extreme heat exposure, debt bondage averaging USD 3,000-10,000, wage theft ranging 40-80% of promised salary, and subcontracting chains obscuring employer accountability.",
        "source": "Polaris Project Typology Research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Polaris Project: Agricultural Labor Trafficking",
        "summary": "Polaris identifies agricultural trafficking: seasonal workers most vulnerable, extreme hours during harvest, pesticide exposure without protection, housing in isolated camps, limited communication access, and wage theft through piece-rate fraud.",
        "source": "Polaris Project Typology Research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Polaris Project: Sex Trafficking Overlaps with Labor Trafficking",
        "summary": "Polaris identifies overlap: economic coercion used in both labor and sex trafficking, recruitment tactics similar, debt bondage mechanism identical, isolation and document control universal. Often sequential (labor trafficking leads to sexual exploitation).",
        "source": "Polaris Project Typology Research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Polaris Project: Vulnerability Factors Framework",
        "summary": "Polaris identifies primary vulnerability factors: poverty, migration status, gender discrimination, family separation, limited education, language barriers, prior abuse/trauma, LGBTQ+ status, and disability. Traffickers systematically target these populations.",
        "source": "Polaris Project Typology Research",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Polaris Project: Trafficker Control Mechanisms",
        "summary": "Polaris identifies three control layers: economic (debt, wage theft), physical (confinement, document confiscation), and psychological (isolation, threats, violence). Multiple layers simultaneously applied for maximum control.",
        "source": "Polaris Project Typology Research",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # US DOL LIST OF GOODS PRODUCED BY CHILD/FORCED LABOR
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "US DOL: 155 Goods from 77 Countries Produced with Child/Forced Labor",
        "summary": "US Department of Labor identifies 155 goods from 77 countries as produced with child or forced labor. Categories include: agriculture (cocoa, coffee, sugar, cotton, palm oil), mining (cobalt, gold, diamond), textiles, manufacturing, fishing, and construction materials.",
        "source": "US DOL List of Goods Produced by Child Labor or Forced Labor (2023)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "US DOL: Cobalt Mining in Democratic Republic of Congo",
        "summary": "US DOL lists cobalt mining in DRC as produced with child labor (ages 5-17) and forced labor. Conditions: dangerous underground mining, minimal safety equipment, exploitation of artisanal miners and children, debt bondage to mines.",
        "source": "US DOL List of Goods Produced by Child Labor or Forced Labor (2023)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "US DOL: Cocoa Production in Cote d'Ivoire and Ghana",
        "summary": "US DOL documents child labor in cocoa farming: 900,000+ children in cocoa labor, hazardous pesticide exposure, forced labor of adult migrants, and debt bondage. Children as young as 5 perform harvesting and processing.",
        "source": "US DOL List of Goods Produced by Child Labor or Forced Labor (2023)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "US DOL: Fishing Labor Trafficking in Southeast Asia",
        "summary": "US DOL identifies forced labor in fishing across Thailand, Myanmar, Cambodia: workers on vessels 3-10 years without shore leave, debt bondage, wage theft (0-10% of promised), violence, and documented deaths.",
        "source": "US DOL List of Goods Produced by Child Labor or Forced Labor (2023)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "US DOL: Sugarcane Labor in Central America",
        "summary": "US DOL identifies forced labor in sugarcane across Guatemala, Honduras, El Salvador: debt bondage averaging USD 1,000-3,000, wages withheld 50-80%, heat exhaustion deaths, and workers locked in fields during harvest.",
        "source": "US DOL List of Goods Produced by Child Labor or Forced Labor (2023)",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # EU TRAFFICKING INDICATORS AND DIRECTIVE 2011/36/EU
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Directive 2011/36/EU Trafficking Definition and Exploitation Indicators",
        "summary": "EU Directive defines trafficking as use of force, fraud, or coercion to obtain labor/services. Indicators include: deception in recruitment, document confiscation, confinement, debt bondage, isolation, wage theft, hazardous conditions, and violence.",
        "source": "EU Directive 2011/36/EU on Preventing and Combating Trafficking in Human Beings",
    },
    {
        "type": "advisory",
        "jurisdiction": "EU",
        "title": "EU Victim Identification: Behavioral and Situational Indicators",
        "summary": "EU identifies behavioral markers: fear of authorities, hesitant/vague answers, lack of control over documents/money, signs of physical abuse, controlled appearance/clothing, absence of personal items, dependency on handler. Situational: living at workplace, isolation, excessive hours.",
        "source": "EU Action on Identifying and Supporting Trafficking Victims",
    },
    {
        "type": "advisory",
        "jurisdiction": "EU",
        "title": "EU Sector-Specific Indicators: Domestic Work",
        "summary": "EU identifies domestic work trafficking: employment exclusively in homes, no written contracts, confinement to residence, isolation from services, document confiscation, all-hours availability, wage control, and vulnerability to sexual abuse.",
        "source": "EU Anti-Trafficking Training Materials",
    },
    {
        "type": "advisory",
        "jurisdiction": "EU",
        "title": "EU Sector-Specific Indicators: Agricultural Labor",
        "summary": "EU identifies agricultural trafficking: seasonal workers in isolated locations, extreme hours during harvest, minimal living facilities, wage theft through piece-rate manipulation, debt bondage for seasonal housing, and minimal legal protection.",
        "source": "EU Anti-Trafficking Training Materials",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # UK NATIONAL REFERRAL MECHANISM (NRM) INDICATORS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Modern Slavery Act 2015 and NRM Trafficking Indicators",
        "summary": "UK NRM identifies trafficking via: false promises of employment, use of force/coercion/deception, debt bondage, passport confiscation, isolation, wage theft, extreme working hours, unsanitary accommodation, and exploitation by organized networks.",
        "source": "UK NRM: Competent Authority Guidance and Indicator Lists",
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "UK NRM: First Responder Behavioral Indicators",
        "summary": "UK NRM trains first responders to identify: signs of physical abuse, anxious/fearful demeanor, inadequate clothing for weather, inability to answer basic questions, lack of independence, controlled communication, absence of personal documents.",
        "source": "UK NRM: First Responder Training Materials",
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "UK NRM: Labor Trafficking in Nail Salons",
        "summary": "UK documents nail salon trafficking: women on visas or irregular status, living and working in single location, 10-14 hour days, minimal wages or none, debt bondage for visa/transport, isolation from services.",
        "source": "UK Modern Slavery Inspection Reports",
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "UK NRM: Car Wash and Cleaning Service Labor Trafficking",
        "summary": "UK identifies trafficking in car wash/cleaning: vulnerable migrants (Eastern European, Vietnamese), living on premises, extreme hours, wage theft, minimal pay, work imposed by debt or family ties, organized gang control.",
        "source": "UK Modern Slavery Reports",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # AUSTRALIAN FEDERAL POLICE TRAFFICKING INDICATORS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "AU",
        "title": "Australian Federal Police: Workplace Trafficking Indicators",
        "summary": "AFP identifies trafficking in agricultural work, domestic service, hospitality: workers on dependent visas, document confiscation, wage theft (50-90% of promised), confinement to workplace, restriction of movement, debt bondage.",
        "source": "Australian Federal Police - Trafficking in Persons Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "AU",
        "title": "Australian Federal Police: Debt Bondage Mechanism Breakdown",
        "summary": "AFP documents debt bondage cycle: recruitment debt (AUD 5,000-20,000), compounding interest, charges for accommodation/food/transport, debt transferred between employers, initial promised repayment (6 months) extended indefinitely.",
        "source": "Australian Federal Police - Trafficking Case Analysis",
    },
    {
        "type": "advisory",
        "jurisdiction": "AU",
        "title": "Australian Federal Police: Vulnerability Factors in Visa-Based Trafficking",
        "summary": "AFP identifies visa restrictions as trafficking enabler: 457 visa (now TSS) tied to employer, Work and Holiday visa restrictions, student visa limitations on hours. Visa dependence creates leverage for exploitation.",
        "source": "Australian Federal Police - Visa Trafficking Analysis",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # CANADIAN IRCC TRAFFICKING SCREENING TOOLS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "CA",
        "title": "Canadian IRCC: Temporary Foreign Worker Program Trafficking Indicators",
        "summary": "Canadian IRCC identifies TFW trafficking: job placement fees, contract substitution, wage theft, accommodations in employer compounds, passport confiscation, isolation, financial control, and recruitment through deception.",
        "source": "IRCC TFW Program Trafficking Prevention Materials",
    },
    {
        "type": "advisory",
        "jurisdiction": "CA",
        "title": "Canadian IRCC: Trafficking Risk Assessment Framework",
        "summary": "IRCC uses risk assessment: sectoral risks (agricultural, domestic, hospitality highest), employer compliance history, migration pathway (especially Philippines, Mexico, India), worker vulnerability factors, and employer housing control.",
        "source": "IRCC Trafficking Risk Assessment Guidance",
    },
    {
        "type": "advisory",
        "jurisdiction": "CA",
        "title": "Canadian IRCC: Occupational Health and Safety as Trafficking Indicator",
        "summary": "IRCC identifies unsafe conditions as trafficking indicator: absence of WSIB registration, no safety training, failure to report injuries, unsafe housing, exposure to hazards without protection, and worker fear of reporting injuries.",
        "source": "IRCC and WSIB Trafficking Prevention Guidelines",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ECPAT CHILD TRAFFICKING INDICATORS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ECPAT: Child Trafficking Indicators in Labor Sector",
        "summary": "ECPAT identifies child labor trafficking: children ages 5-18 in hazardous work (fishing, agriculture, mining, construction), no school attendance, malnourished appearance, scars/injuries indicating abuse, fearfulness of adults, and separation from family.",
        "source": "ECPAT Child Trafficking Indicators",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ECPAT: Sex Trafficking Indicators Relevant to Labor Exploitation",
        "summary": "ECPAT identifies overlap: economic exploitation in labor trafficking becomes transition to sexual exploitation, debt bondage used in both, isolation and control mechanisms identical, children particularly vulnerable to multiple trafficking types.",
        "source": "ECPAT Trafficking Prevention Manual",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ECPAT: Protective Systems and Institutional Responses",
        "summary": "ECPAT identifies institutional failures enabling trafficking: lack of child labor enforcement, inadequate labor inspection, no trafficking-specific law enforcement training, insufficient victim support services, and gaps in inter-agency coordination.",
        "source": "ECPAT Protective Systems Assessment",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # FATF MONEY LAUNDERING INDICATORS RELATED TO TRAFFICKING PROCEEDS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "FATF: Trafficking Proceeds Money Laundering Typologies",
        "summary": "FATF identifies trafficking proceeds laundering: bulk cash smuggling, informal money transfer (hawala), commingling with legitimate business revenue, rapid movement through multiple jurisdictions, use of cryptocurrency, and shell company structures.",
        "source": "FATF Report on Money Laundering in Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "FATF: Recruitment Agency Financial Indicators",
        "summary": "FATF identifies suspicious financial patterns in recruitment: excessive fee collection (USD 1,000-10,000 per worker), short intervals between fee collection and worker departure, concentration of payments at month-end, and movement of funds between agencies.",
        "source": "FATF Guidance on Counter-Financing of Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "FATF: Migrant Remittance Manipulation and Debt Bondage",
        "summary": "FATF identifies trafficking element in remittance systems: fees reducing remittances received, promises of high exchange rates not delivered, funds diverted to debt repayment, family members manipulated via remittance manipulation.",
        "source": "FATF Migrant Remittance and Trafficking Report",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HEALTHCARE PROVIDER TRAFFICKING INDICATORS (HEAL)
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "HEAL Trafficking: Healthcare Provider Physical Indicators",
        "summary": "HEAL identifies trafficking via healthcare: injuries inconsistent with explanation, repeated injuries suggesting pattern abuse, signs of untreated infections/STIs, malnutrition/vitamin deficiencies, signs of drug/alcohol coercion, and gynecological trauma.",
        "source": "HEAL Trafficking - Healthcare Provider Training (health-care-for-human-trafficking.org)",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "HEAL Trafficking: Behavioral and Social Indicators",
        "summary": "HEAL identifies behavioral trafficking indicators: scripted/vague responses to questions, apparent fear of authorities, avoidance of eye contact, extreme deference to companion, lack of knowledge about identity/location, apparent lack of decision-making power.",
        "source": "HEAL Trafficking - Healthcare Provider Training",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "HEAL Trafficking: Occupational Health Screening for Labor Trafficking",
        "summary": "HEAL recommends screening for: chemical/pesticide exposure (agricultural workers), repetitive strain injuries (manufacturing), heat exhaustion/dehydration (outdoor laborers), lack of protective equipment, and untreated occupational injuries.",
        "source": "HEAL Occupational Health and Trafficking Prevention",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # TRANSPORTATION SECTOR INDICATORS (TRUCKERS AGAINST TRAFFICKING)
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Truckers Against Trafficking: Transportation as Exploitation Vector",
        "summary": "TAT identifies trafficking in/via transportation: workers transported for placement, drivers used to move victims, truck stops as trafficking sites, driver vulnerability to exploitation, and transportation industry as trafficking conduit.",
        "source": "Truckers Against Trafficking Education Materials",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Truckers Against Trafficking: Labor Trafficking in Freight/Transport Services",
        "summary": "TAT documents trafficking in transport: driver debt bondage (vehicle cost, fuel advances), vehicle ownership bondage, wage theft via mileage manipulation, mandatory rental (owner-operator scheme trap), and isolation during long hauls.",
        "source": "Truckers Against Trafficking - Labor Exploitation Cases",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # HOTEL/HOSPITALITY INDUSTRY INDICATORS (ECPAT CODE)
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "ECPAT Code of Conduct: Hospitality Labor Trafficking Indicators",
        "summary": "ECPAT Code identifies hospitality trafficking: workers living on premises, confinement to facility, wage theft (tips withheld, piece-rate fraud), sexual harassment/assault, document confiscation, and vulnerability of migrant/undocumented workers.",
        "source": "ECPAT Code of Conduct for the Protection of Children in Hospitality",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ECPAT Code: Staff Screening for Trafficking Indicators",
        "summary": "ECPAT recommends hotel staff training: recognize workers unable to move freely, those lacking personal documents, individuals showing signs of abuse, workers unable to speak freely, and situations where handlers control communications/money.",
        "source": "ECPAT Code Training Materials",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # LEGAL PROFESSION INDICATORS (AMERICAN BAR ASSOCIATION)
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "US",
        "title": "ABA: Legal Professionals' Role in Identifying Labor Trafficking",
        "summary": "ABA identifies legal system barriers to trafficking detection: immigration lawyers seeing undocumented workers unable to describe employment, employment lawyers seeing wage theft patterns, family law attorneys seeing domestic servitude cases, and criminal defense seeing trafficked victims charged with crimes.",
        "source": "ABA Human Trafficking Resource Guide",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "ABA: Document Confiscation and Legal Consequences",
        "summary": "ABA identifies document confiscation as evidence of control: passport confiscation creates immigration violations, prevents worker access to legal representation, and becomes element in criminal trafficking prosecution. Legal intervention requires document recovery.",
        "source": "ABA Legal Response to Labor Trafficking",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # FAITH-BASED ORGANIZATION INDICATORS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Faith-Based Organization Indicator: Spiritual Coercion and Control",
        "summary": "Faith leaders identify trafficking involving: misuse of religious teachings to justify exploitation, spiritual leaders as traffickers or enabling, religious isolation (required religious services), spiritual threats (damnation for escape), and religiously-motivated servitude or debt.",
        "source": "Faith Trust Institute - Religious Response to Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Faith-Based Vulnerability Factor: Religious Minority Targeting",
        "summary": "Faith-based organizations identify trafficking patterns targeting religious minorities: traffickers exploit discrimination, isolation from mainstream society, concentrated communities, and tendency to seek help within faith communities rather than secular authorities.",
        "source": "Various Faith-Based Anti-Trafficking Organizations",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # SUPPLY CHAIN AUDIT INDICATORS (SEDEX, SA8000)
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "SEDEX and SA8000: Supply Chain Forced Labor Audit Indicators",
        "summary": "SEDEX/SA8000 audits identify trafficking via: worker interviews (private/confidential), document examination, payroll analysis, recruitment practice review, contract verification, housing inspection, and freedom of movement assessment. Covers all 11 ILO indicators.",
        "source": "SEDEX (Supplier Ethical Data Exchange) Standards and SA8000 Labor Standards",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "SEDEX: Recruitment Fee Audit Indicators",
        "summary": "SEDEX audits identify excessive recruitment: documented worker fees, recruitment agent fees, visa processing costs, medical exam costs, training fees, and transport costs. Evidence of fee deduction from wages or debt arrangements.",
        "source": "SEDEX Recruitment Practice Auditing Standards",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "SA8000: Working Hours and Overtime Documentation",
        "summary": "SA8000 audits identify excessive hours: payroll records showing systematic overtime, time-tracking systems revealing 12+ hour days, worker interviews confirming excessive hours, lack of rest day documentation, and absence of proper overtime compensation.",
        "source": "SA8000 Working Hours Certification Standards",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # IOM SCREENING AND IDENTIFICATION TOOLS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "IOM Screening Tool: Border and Reception Point Identification",
        "summary": "IOM uses standardized screening at borders: identification of migrant profile (age, travel method, documentation status), interviewer assessment of understanding of employment, verification of recruitment information, detection of pressure/fear indicators, and referral for further assessment.",
        "source": "IOM Screening Procedures for Identification of Trafficked Persons",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "IOM Vulnerability Assessment: Pre-Trafficking Risk Factors",
        "summary": "IOM identifies pre-trafficking vulnerability: economic desperation, single-parent households, prior migration experience (positive for second migration), family migration history, lack of education, and awareness of destination conditions.",
        "source": "IOM Vulnerability Assessment Framework",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "IOM Psychosocial Assessment: Trauma and Trafficking",
        "summary": "IOM identifies trauma markers in trafficking survivors: PTSD symptoms, suicidal ideation, depression/anxiety, shame/stigma, distrust of authorities, difficulty recounting exploitation, and dissociation. Guides support service provision.",
        "source": "IOM Psychosocial Assessment Standards",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # OSCE ANTI-TRAFFICKING FRAMEWORK AND INDICATORS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "OSCE: National Referral Mechanism Victim Identification Standards",
        "summary": "OSCE standards establish national referral mechanisms with standardized victim identification: first responder training, confidential screening, safe accommodation referral, legal assistance, and trauma-informed approach. Covers labor and sexual trafficking equally.",
        "source": "OSCE National Referral Mechanism Handbook",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "OSCE: Labour Inspectorate as Anti-Trafficking First Line",
        "summary": "OSCE identifies labour inspectors as critical anti-trafficking professionals: trained to identify forced labor, make victim referrals, document evidence, coordinate with law enforcement, and support worker-reported violations.",
        "source": "OSCE Labour Inspection and Trafficking Prevention",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "OSCE: Institutional Accountability and Multi-Stakeholder Coordination",
        "summary": "OSCE emphasizes institutional response: labor ministry, law enforcement, health services, NGOs, and social services must coordinate. Single-agency response insufficient. Accountability mechanisms must hold institutions responsible for victim support.",
        "source": "OSCE Good Practices in Counter-Trafficking",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ADDITIONAL SPECIALIZED FRAMEWORKS AND RECENT DEVELOPMENTS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO Global Estimates 2021: Forced Labor Scale and Scope",
        "summary": "ILO 2021 estimates: 27.6 million people in forced labor (16.9 million women, 10.7 million children). 17.3 million in private sector exploitation, 6.3 million in state-imposed labor. Economic value: USD 236+ billion annually stolen from workers.",
        "source": "ILO Global Estimates of Modern Slavery 2021",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO Female Representation in Trafficking: 72% of Trafficked Persons",
        "summary": "ILO data shows 72% of identified trafficking victims are women and girls. Sectors: domestic work (23% of all trafficking), sexual exploitation (48%), manufacturing/agriculture (28%). Gender dimensions crucial to victim identification.",
        "source": "ILO Global Estimates of Modern Slavery 2021",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Digital Labor Trafficking and Online Exploitation Indicators",
        "summary": "Emerging indicators include: online recruitment with job misrepresentation, livestream sexual exploitation of trafficked workers, remote monitoring/control via app/GPS, cryptocurrency payment concealment, fake freelance platforms, and online debt accumulation.",
        "source": "International Labour Organization - Emerging Trafficking Patterns",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Supply Chain Labor Trafficking: Structural Indicators",
        "summary": "Structural trafficking in supply chains: pressure to reduce costs drives wage suppression, subcontracting chains hide employer accountability, suppliers recruit vulnerable workers to meet quotas, and auditing systems fail to detect systemic exploitation.",
        "source": "Various Supply Chain Labor Rights Organizations",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Bonded Labor System Across Sectors and Regions",
        "summary": "Bonded labor indicators universal across contexts: debt as binding mechanism, intergenerational debt transfer, debt expansion through charges, mathematical unpayability, debt inheritance preventing departure. Documented in agriculture, mining, manufacturing, domestic work globally.",
        "source": "International Labour Organization - Forced Labour Indicators",
    },

    # ─────────────────────────────────────────────────────────────────────────
    # ADDITIONAL FRAMEWORKS: BANKING, WORKPLACE RIGHTS, RECRUITMENT AUDITS
    # ─────────────────────────────────────────────────────────────────────────

    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Banking Sector Indicators: Account Control and Wage Management",
        "summary": "Banks can identify trafficking when: employer controls worker's bank account, account holder is not account controller, unusual wage deposits (large bulk then zero), frequent transfers to third parties, or pattern inconsistent with legitimate employment.",
        "source": "International Labour Organization and Banking Association Guidelines",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Workplace Rights Auditing: Freedom of Association Violations",
        "summary": "Freedom of association denial is trafficking indicator: prohibited union membership, prevented from discussing working conditions, retaliation for attempting to organize, isolated from peer workers, and prevented from attending worker meetings.",
        "source": "ILO Conventions 87 and 98 - Freedom of Association",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Recruitment Audit Baseline: ILO Standards Assessment",
        "summary": "ILO recruitment standards audit identifies trafficking risk: recruiter licensing status, fee transparency, contract clarity, consent verification, medical exam standards, and pre-departure information provision. Absence of standards indicates trafficking likelihood.",
        "source": "ILO Recruitment Convention, 1997 (No. 181)",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Occupational Health and Safety as Compliance Violation",
        "summary": "Labor trafficking often accompanied by complete absence of occupational health systems: no safety training, no protective equipment provided, no incident reporting, no medical surveillance, no hazard assessment. Safety violations indicate labor control.",
        "source": "ILO Occupational Safety and Health Convention, 1981 (No. 155)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO Technical Note: Forced Labor and Descent into Debt",
        "summary": "ILO research shows 40-60% of migrant workers with recruitment debt report downward wage spiral: promised wage higher than received, deductions increase over time, promised benefits never materialize. Debt design mathematically ensures entrapment.",
        "source": "ILO Technical Note on Recruitment and Debt",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Wage Calculation Manipulation: Piece-Rate Fraud",
        "summary": "Piece-rate fraud indicators: inconsistent counting systems, disputes over piece completion, employer-controlled scales or measurements, rounding down, deduction for 'defects', and worker inability to verify payment calculation.",
        "source": "International Labour Organization - Wage Theft Mechanisms",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Labor Broker Liability and Trafficking Facilitation",
        "summary": "Labor brokers facilitate trafficking through: recruiting vulnerable workers, charging multiple agencies, providing contradictory information, selecting complicit employers, disappearing after placement, and preventing worker recourse.",
        "source": "ILO Labour Broker Convention and Protocols",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Subcontractor Chain Trafficking Enablement",
        "summary": "Multi-level subcontracting enables trafficking by: obscuring employer identity, creating deniability of direct employment, fragmenting accountability, passing through fees at each level, and isolating workers from responsibility chains.",
        "source": "Global Supply Chain Studies",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Irregular Work Status as Trafficking Enabler",
        "summary": "Irregular work status strengthens trafficking control: workers fearful of deportation, unable to access legal protections, prevented from reporting abuse, unable to seek health services, and targeted for exploitation due to legal vulnerability.",
        "source": "International Labour Organization - Irregular Migrant Workers",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Housing as Control Mechanism and Living Condition Indicator",
        "summary": "Housing-based trafficking indicators: overcrowded accommodations (10-20 per room), substandard conditions (no ventilation, sanitation), employer-controlled housing (workers cannot leave), housing costs deducted from wages, and unsanitary cooking/hygiene facilities.",
        "source": "ILO Trafficking and Forced Labour Research",
    },

    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Gender-Based Violence as Trafficking Indicator",
        "summary": "Disproportionate gender-based violence in trafficking: sexual harassment normalized, sexual assault by supervisors, reproductive coercion, pregnancy discrimination, and gender-specific threats (threats against children or family status).",
        "source": "International Labour Organization - Gender and Trafficking",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Migrant Worker Vulnerability Amplification Through Documents",
        "summary": "Document confiscation creates compound vulnerability: undocumented status prevents help-seeking, employer-mediated legal status creates fear, document destruction prevents return home, and vulnerability increases after document loss.",
        "source": "International Labour Organization - Migrant Workers and Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Age Verification Gaps in Recruitment and Child Labor Trafficking",
        "summary": "Child trafficking indicators: no age verification during recruitment, no birth certificate verification, use of forged documents, age misrepresentation by recruiter, and youthful appearance despite stated age.",
        "source": "International Labour Organization - Child Labour Identification",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Work-Life Balance Absence and Control Indicators",
        "summary": "Absence of work-life balance indicates control: required availability 24/7, no personal time, mandatory social events, monitored personal relationships, controlled personal spending, and isolation from personal pursuits.",
        "source": "Workplace Rights Monitoring Organizations",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Skill Level Mismatch and Job Title Fraud",
        "summary": "Trafficking often involves false skill requirements: high skill job promised becomes low skill work, specialized training promised but no skills required, overqualified workers in unrelated roles, and job change without consent.",
        "source": "Recruitment Fraud Research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Advancement Denial and Career Stagnation",
        "summary": "Trafficking characterized by: promised promotions never materialized, training promised withheld, skill development opportunities denied, wage stagnation despite performance, and deliberate career blocking.",
        "source": "Labor Rights Organizations",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Global Migrant Worker Population: 281 Million and Trafficking Vulnerability",
        "summary": "IOM estimates 281 million international migrants globally. Estimated 3-5% engaged in forced labor situations (8.5-14 million). Higher vulnerability among: women in domestic work, agricultural workers, construction workers, and manufacturing sector employees.",
        "source": "IOM World Migration Report 2022 and Labour Statistics",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Identity-Based Discrimination as Targeting Mechanism",
        "summary": "Traffickers target marginalized identities: LGBTQ+ individuals, religious minorities, ethnic minorities, people with disabilities, stateless persons, and indigenous populations. Discrimination creates vulnerability and isolation.",
        "source": "International Labour Organization - Discrimination and Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Mental Health Deterioration as Prolonged Trafficking Indicator",
        "summary": "Prolonged trafficking characterized by: depression, anxiety, suicidal ideation, dissociation, panic attacks, sleep disturbances, and cognitive decline. Mental health status tracks trafficking duration and severity.",
        "source": "IOM and WHO Mental Health in Trafficking",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Forced Savings and Asset Control as Trafficking Mechanism",
        "summary": "Some traffickers employ forced savings schemes: claiming to 'save' worker wages, worker unable to access accumulated savings, wages released only at contract end, or savings confiscated on departure.",
        "source": "Trafficking Finance Research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Repatriation Denial and Entrapment Perpetuation",
        "summary": "Trafficking perpetuated through repatriation denial: employer refuses to provide return transport despite contract completion, workers stranded without funds, refusal to process final documents, and threats if worker attempts self-repatriation.",
        "source": "International Labour Organization - Migrant Worker Protections",
    },

    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Communication Language Control and Selective Translation",
        "summary": "Traffickers control communication through: providing only partial translations, mistranslating key terms, using unfamiliar dialects, preventing writing (illiteracy), and selective interpretation of information.",
        "source": "Language Access and Trafficking Prevention",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Surveillance Technology as Modern Trafficking Control",
        "summary": "Contemporary trafficking includes: GPS tracking of workers, geofencing of work locations, surveillance cameras in living areas, spyware on phones, location-sharing apps, and biometric time-tracking systems for control.",
        "source": "Technology and Labor Trafficking Research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Peer Pressure and Workforce Exploitation Normalization",
        "summary": "Traffickers normalize exploitation through: having experienced workers reinforce compliance, creating hierarchy with certain workers as supervisors, using peer pressure to prevent escape, and shared suffering creating acceptance.",
        "source": "Trafficking Psychology Research",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Contract Language and Ambiguity as Control Tool",
        "summary": "Intentionally ambiguous contracts contain: vague job descriptions, undefined working hours, conditional wage clauses, penalty language, termination provisions with financial consequences, and provisions in incomprehensible language.",
        "source": "Contract Analysis and Labor Rights",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Emergency Services Access Denial and Dependency Reinforcement",
        "summary": "Trafficking perpetuated through: preventing access to police, medical services blocked, social services access restricted, and workers dependent on employer for all emergencies. Emergency avoidance reinforces control.",
        "source": "Victim Support Services Research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Legal Status Manipulation and Irregular Document Creation",
        "summary": "Traffickers manipulate legal status by: providing irregular visas, creating undocumented status intentionally, threatening deportation for minor violations, and making legal status conditioned on continued work.",
        "source": "Immigration Status and Trafficking",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Skill Degradation and De-Professionalization Strategy",
        "summary": "Traffickers may deliberately degrade skilled workers: placing engineers in construction labor, healthcare workers in domestic service, accounting professionals in hospitality. Prevents recognition of qualification, reduces escape likelihood.",
        "source": "Trafficking of Skilled Migrant Workers",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Recruitment Information Asymmetry and Intentional Deception",
        "summary": "Asymmetrical information systems hide: true employer identity, actual job location and description, actual wages and deductions, true working hours and conditions, accommodation reality, and actual duration of contract.",
        "source": "Information Asymmetry in Labor Trafficking",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Employer-Imposed Isolation from Co-Ethnic Communities",
        "summary": "Some trafficking includes: deliberately isolating from cultural/ethnic communities, preventing participation in community institutions, breaking family connections, and preventing workers from understanding their legal rights in community language.",
        "source": "Ethnic Community and Trafficking Prevention",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Incremental Exploitation Escalation and Normalization",
        "summary": "Trafficking characterized by gradual escalation: minor contract violations normalized, conditions worsen gradually, new requirements introduced incrementally, and worker adaptation prevents recognition of trafficking.",
        "source": "Trafficking Escalation Pattern Research",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Vulnerability Exploitation Through Addiction and Substance Dependence",
        "summary": "Traffickers deliberately create chemical dependencies: substance provision, addiction development, dependency as control mechanism, and withdrawal threats to ensure compliance. Substance use also conceals abuse indicators.",
        "source": "Substance Abuse and Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Employment Legitimacy Facade and Document Falsification",
        "summary": "Traffickers create false legitimacy through: fake employment documents, fraudulent tax registration, forged business licenses, fake permits, and employment records that don't match reality.",
        "source": "Document Fraud in Labor Trafficking",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Exit Barrier Creation and Deliberate Entrapment Architecture",
        "summary": "Traffickers architect exit barriers: distance from home country, language barriers, no savings, location unfamiliarity, legal vulnerability, absent documentation, and created debt. Each barrier reinforces others.",
        "source": "Exit Barrier Theory in Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Employment Verification Impossibility and Anonymity Provision",
        "summary": "Traffickers prevent verification by: using cash payments without records, multiple employer names, contract destruction, witness elimination, and worker isolation preventing verification from external sources.",
        "source": "Employment Verification and Fraud Prevention",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Skill Suppression and Artificial Incompetence Induction",
        "summary": "Traffickers suppress skills by: denying access to tools/equipment, preventing skill practice, public humiliation for performance, punishment for demonstrating competence, and deliberate mis-assignment to prevent success.",
        "source": "Trafficking and Worker Agency",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Economic Dependency Loop and Financial Vulnerability Reinforcement",
        "summary": "Traffickers create permanent financial vulnerability: all income withheld, all expenses employer-controlled, savings prevented, and economic skills deliberately underdeveloped preventing independence.",
        "source": "Economic Dependency in Trafficking",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Recruitment Referral Network Exploitation and Community Infiltration",
        "summary": "Traffickers exploit community trust through: using previous workers to recruit, community reputation building, infiltrating ethnic business networks, establishing credibility through trusted members, and expanding network through family/social ties.",
        "source": "Network Exploitation in Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Multiple Document Sets and Identity Confusion as Control",
        "summary": "Some traffickers maintain multiple identity documents for workers: one for work, one for residence, one withheld from worker, one with police. Document confusion prevents worker understanding of legal status.",
        "source": "Identity Document Exploitation",
    },
    {
        "type": "training_material",
        "jurisdiction": "international",
        "title": "Post-Escape Support System Gaps and Re-Trafficking Risk",
        "summary": "Victims face re-trafficking risks due to: inadequate victim support services, economic desperation continuing post-escape, stigma preventing normal employment, and traumatic bonds complicating recovery.",
        "source": "Victim Support and Re-trafficking Prevention",
    },
]
