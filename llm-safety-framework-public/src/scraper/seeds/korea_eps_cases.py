"""South Korea EPS cases — Employment Permit System, agricultural exploitation, and worker rights."""

KOREA_EPS_CASE_FACTS: list[dict] = [
    # =====================================================================
    # 1. EPS PROGRAMME STRUCTURE AND PARTICIPATING COUNTRIES (16 MOUs)
    # =====================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "EPS Act on Foreign Workers' Employment — Foundation of Government-to-Government Recruitment",
        "summary": (
            "The Act on Foreign Workers' Employment, Etc. (Act No. 6967, 2003, effective August 2004) "
            "established the Employment Permit System replacing the Industrial Trainee System (ITS) "
            "which had been plagued by broker exploitation and runaway rates exceeding 50%. EPS is "
            "administered by the Ministry of Employment and Labor (MOEL) with HRD Korea handling "
            "overseas recruitment. Workers enter on E-9 (non-professional employment) visas for "
            "manufacturing, construction, agriculture/livestock, fishing, and service sectors."
        ),
        "source": "Korea Ministry of Employment and Labor / Act No. 6967",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "EPS 16-Country MOU Framework — Bilateral Labour Agreements",
        "summary": (
            "Korea has signed bilateral MOUs with 16 sending countries: Philippines (2004), "
            "Thailand (2004), Sri Lanka (2004), Vietnam (2004), Mongolia (2004), Indonesia (2004), "
            "Uzbekistan (2007), Pakistan (2008), Cambodia (2007), China (2007), Bangladesh (2008), "
            "Nepal (2007), Myanmar (2009), Timor-Leste (2009), Laos (2016), and Kyrgyzstan (2011). "
            "Each MOU designates a government sending agency. Korea periodically suspends MOUs "
            "with countries showing high overstay rates (e.g., Bangladesh was temporarily suspended)."
        ),
        "source": "Korea HRD Service / ILO MOU Registry",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "EPS Quota System — Annual Allocation by Country and Sector",
        "summary": (
            "MOEL sets annual EPS quotas (typically 50,000-60,000 workers/year) allocated across "
            "sending countries based on compliance metrics: overstay rate, selection transparency, "
            "and cost control. In 2023, the quota was raised to approximately 110,000 amid severe "
            "labour shortages in manufacturing and agriculture. Countries with high overstay rates "
            "see quota reductions. Sector allocation prioritises manufacturing (largest share), "
            "followed by agriculture/livestock, construction, fishing, and services."
        ),
        "source": "Korea Ministry of Employment and Labor / Foreign Workforce Policy Committee",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "EPS-TOPIK Korean Language Proficiency Requirement",
        "summary": (
            "All EPS applicants must pass the EPS-TOPIK (Employment Permit System Test of "
            "Proficiency in Korean) administered by HRD Korea in sending countries. The test "
            "covers listening and reading comprehension. Pass rates vary by country (20-40%). "
            "Official test fee is approximately USD 24. However, private tutoring industries "
            "in sending countries charge USD 200-2,000 for preparation courses, inflating true "
            "migration costs beyond the government-set caps."
        ),
        "source": "Korea HRD Service / IOM Assessment of EPS Recruitment Costs",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "EPS Permit Duration — 4 Years 10 Months Plus Re-Entry",
        "summary": (
            "E-9 visa holders receive an initial permit of up to 3 years, extendable by 1 year "
            "10 months (total 4 years 10 months). Since 2012, 'faithful worker' re-entry allows "
            "workers who completed their first term without violation to return after a brief "
            "departure for a second term of 4 years 10 months (total ~9 years 8 months). The "
            "requirement to leave and re-enter between terms was criticised as generating unnecessary "
            "costs and causing workers to lose employment continuity."
        ),
        "source": "Korea Ministry of Employment and Labor / EPS Handbook",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "EPS Departure Guarantee Insurance and Return Cost Insurance",
        "summary": (
            "EPS requires workers to enrol in Departure Guarantee Insurance (approx. KRW 400,000, "
            "refunded upon departure) and Return Cost Insurance (approx. KRW 600,000 covering "
            "repatriation airfare). Employers must purchase Wage Guarantee Insurance for each "
            "worker. These mandatory insurance schemes were designed to protect workers but have "
            "been criticised for slow refund processes—some workers wait 2-14 months post-departure "
            "for refunds, effectively functioning as forced savings confiscated during employment."
        ),
        "source": "Korea Ministry of Employment and Labor / Samsung Fire & Marine Insurance",
    },
    {
        "type": "statistic",
        "jurisdiction": "KR",
        "title": "EPS Worker Population — Scale of Programme",
        "summary": (
            "As of 2024, approximately 280,000-300,000 EPS (E-9 visa) workers are employed in "
            "South Korea. An estimated additional 350,000-400,000 undocumented migrant workers "
            "(many former EPS overstayers) also work in the country. The total registered foreign "
            "workforce exceeds 900,000. EPS workers comprise the single largest category of "
            "low-skilled migrant labour, concentrated in manufacturing (~60%), agriculture/livestock "
            "(~20%), construction (~10%), and fishing (~5%)."
        ),
        "source": "Korea Immigration Service / MOEL Statistics",
    },

    # =====================================================================
    # 2. EPS AS ILO-CITED ETHICAL RECRUITMENT MODEL VS REALITY
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "ILO Endorsement of EPS as Fair Recruitment Model",
        "summary": (
            "The ILO has repeatedly cited EPS as a best-practice model for ethical recruitment, "
            "noting its government-to-government structure eliminates private broker fees, caps "
            "total migration costs at approximately USD 927-1,100, and ensures equal labour law "
            "coverage for migrant workers. The 2010 ILO 'Good Practice' report and the 2014 "
            "UN Public Service Award recognised EPS. However, the ILO itself has acknowledged "
            "the gap between EPS design and implementation, particularly regarding workplace "
            "change restrictions and agricultural sector conditions."
        ),
        "source": "ILO Fair Recruitment Initiative / UN Public Service Awards 2011",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Gap Between EPS Design and Reality — Structural Critique",
        "summary": (
            "Despite ILO endorsement, researchers (Amnesty International 2014, NHRCK 2013) "
            "document significant gaps: (1) workplace change restrictions create employer power "
            "asymmetry approaching tied visa systems; (2) agricultural/fishing sectors lack "
            "Labour Standards Act coverage for working hours; (3) isolated rural workplaces "
            "prevent access to support services; (4) language barriers limit complaint filing; "
            "(5) 3-month re-employment deadline incentivises accepting poor conditions; "
            "(6) deportation threat silences undocumented workers."
        ),
        "source": "Amnesty International 'Bitter Harvest' 2014 / NHRCK / ILO CEACR",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Unofficial Recruitment Costs Exceed Official Caps",
        "summary": (
            "While official EPS migration costs are capped at ~USD 1,000, actual worker-borne "
            "costs in several sending countries reach USD 2,000-5,000 when accounting for: "
            "private EPS-TOPIK preparation courses (USD 200-2,000), medical examination fees, "
            "skills training, document authentication, and informal payments. Vietnamese workers "
            "reported costs of USD 3,000-5,000, Cambodian workers USD 2,000-3,500, and Nepali "
            "workers USD 1,500-3,000. These unofficial costs undermine the 'low-cost' model."
        ),
        "source": "IOM Migration Costs Survey / Mekong Migration Network",
    },

    # =====================================================================
    # 3. AGRICULTURAL SECTOR EXPLOITATION (GREENHOUSE, LIVESTOCK, SEASONAL)
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "South Korea — Agricultural Worker Deaths in Greenhouse Farming",
        "summary": (
            "Between 2015 and 2024, at least 50 migrant agricultural workers died in South "
            "Korea, many from hyperthermia or cardiac arrest in plastic greenhouses where "
            "temperatures exceed 50-60 degrees Celsius in summer. Greenhouse farms in regions "
            "such as Pocheon, Asan, Nonsan, and Haenam are staffed predominantly by EPS workers "
            "from Cambodia, Thailand, Vietnam, and Nepal. Workers report 12-16 hour days during "
            "peak season with no shade breaks and inadequate water provision."
        ),
        "source": "NHRCK / Asan Migrant Worker Center / ILO Korea",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Pocheon Greenhouse District — Systemic Exploitation Pattern",
        "summary": (
            "Pocheon-si in Gyeonggi Province is one of Korea's largest greenhouse farming "
            "areas, employing thousands of EPS workers. Documented conditions include: shipping "
            "container or vinyl greenhouse housing (no insulation, temperatures below -15C in "
            "winter and above 40C in summer), pesticide exposure without PPE, 14-16 hour "
            "workdays during harvest, wage deductions for food and housing exceeding legal "
            "limits, and employer confiscation of alien registration cards. Multiple worker "
            "deaths have been reported in Pocheon since 2018."
        ),
        "source": "NHRCK Site Inspection Report / Pocheon Migrant Worker Center",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Asan-si Greenhouse Worker Deaths — 2020-2023 Pattern",
        "summary": (
            "Asan-si in Chungcheongnam-do recorded multiple migrant worker deaths in "
            "agricultural greenhouses between 2020 and 2023. A Cambodian worker died of "
            "suspected heatstroke in July 2021 while working in a vinyl greenhouse. An "
            "investigation revealed the worker had been labouring 14 hours daily with no rest "
            "breaks during a heatwave (outdoor temperature 37C, greenhouse interior estimated "
            "50C+). The employer had not installed cooling equipment or provided electrolyte "
            "drinks as required by the Occupational Safety and Health Act."
        ),
        "source": "Asan Migrant Worker Counseling Center / MOEL Investigation Report",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Seasonal Agricultural Worker Programme — E-8 Visa Concerns",
        "summary": (
            "Korea's Seasonal Worker Programme (E-8 visa, expanded from 2015) brings workers "
            "for 3-5 month agricultural seasons through local government MOUs. By 2023, over "
            "20,000 seasonal workers entered annually. Concerns: workers are tied to a single "
            "farm employer with no transfer rights, housing is often on-farm (employer-controlled), "
            "wages may be below EPS rates, and the short-term nature discourages complaint-filing. "
            "Several provinces reported seasonal workers being used beyond agricultural work in "
            "food processing and packaging without authorisation."
        ),
        "source": "Korea Ministry of Justice / Rural Community Support Centers",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Agricultural Sector Labour Standards Act Exemption — Working Hours",
        "summary": (
            "Under the Korean Labour Standards Act (Article 63), agriculture and livestock "
            "workers are exempt from working hour regulations (weekly 52-hour cap), overtime "
            "premium, and rest day requirements. This exemption applies equally to EPS workers, "
            "meaning migrant agricultural workers can legally be required to work 14-18 hour "
            "days without overtime compensation. The NHRCK and labour advocates have repeatedly "
            "called for removing this exemption, arguing it creates a structural vulnerability "
            "for migrant workers in the most dangerous sector."
        ),
        "source": "Korea Labour Standards Act Art. 63 / NHRCK Recommendation 2015",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Nonsan Strawberry Farm Exploitation — Cambodian Worker Case (2019)",
        "summary": (
            "In 2019, a Nonsan strawberry farm employer was investigated after three Cambodian "
            "EPS workers reported working 16-18 hours daily during the December-May harvest "
            "season, receiving wages significantly below the minimum wage after deductions for "
            "food and housing. The workers were housed in an unheated container adjacent to the "
            "greenhouse. One worker sustained chemical burns from pesticide application without "
            "gloves. The employer was issued a corrective order but not criminally prosecuted."
        ),
        "source": "Chungnam Migrant Worker Center / MOEL Inspection Record",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Gimje Rice and Vegetable Farm — Nepali Worker Wage Theft (2022)",
        "summary": (
            "Three Nepali EPS workers on a Gimje farm in Jeollabuk-do filed complaints with "
            "the Jeonju Labour Office alleging 8 months of unpaid wages totalling approximately "
            "KRW 42 million. The employer claimed financial hardship and offered partial payment. "
            "Workers had continued working despite non-payment due to fear of losing workplace "
            "change eligibility. The Labour Office mediated a settlement of 70% of owed wages "
            "after 6 months, during which the workers could not seek alternative employment."
        ),
        "source": "Jeonju Regional Labour Office / Jeollabuk-do Migrant Worker Support Center",
    },

    # =====================================================================
    # 4. WORKER DEATHS IN AGRICULTURE (HEAT, PESTICIDE, ACCIDENTS)
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Heatstroke Deaths in Vinyl Greenhouses — Statistical Pattern (2015-2024)",
        "summary": (
            "NHRCK and civil society monitoring documented at least 22 migrant worker deaths "
            "attributed to heatstroke or heat-related cardiac arrest in vinyl greenhouses "
            "between 2015 and 2024. Victims were predominantly from Cambodia (8), Thailand (5), "
            "Vietnam (4), Nepal (3), and Myanmar (2). Deaths peaked in July-August during Korean "
            "heatwaves when greenhouse interior temperatures can reach 50-60C. Investigations "
            "consistently found: no cooling systems, inadequate rest breaks, no heat illness "
            "training, and housing inside or adjacent to greenhouses."
        ),
        "source": "NHRCK / Korean Confederation of Trade Unions (KCTU) Migrant Division",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Cambodian Worker Death from Hyperthermia — Haenam Greenhouse (2021)",
        "summary": (
            "A 32-year-old Cambodian EPS worker was found dead in employer-provided housing "
            "(a modified shipping container without air conditioning adjacent to a greenhouse) "
            "in Haenam-gun, Jeollanam-do in August 2021. Autopsy indicated hyperthermia. The "
            "worker had been working 14-hour shifts in a vinyl greenhouse during a heatwave. "
            "The container housing had no ventilation and recorded internal temperatures above "
            "42C at night. The case prompted MOEL to issue guidelines on agricultural worker "
            "housing standards, though compliance remains voluntary."
        ),
        "source": "NHRCK / Haenam-gun Labour Inspection / Cambodian Embassy Seoul",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Pesticide Poisoning Deaths Among Migrant Agricultural Workers",
        "summary": (
            "Between 2016 and 2023, at least 7 migrant agricultural workers died from acute "
            "pesticide poisoning and an estimated 200+ were hospitalised for pesticide-related "
            "illness. Common factors: employers provided no PPE (masks, gloves, protective "
            "clothing), no training on chemical handling was given in workers' languages, "
            "workers mixed and applied pesticides without understanding toxicity ratings, and "
            "re-entry intervals after spraying were not observed. Many incidents were not "
            "reported as occupational injuries due to employer pressure."
        ),
        "source": "Korea Occupational Safety and Health Agency (KOSHA) / Rural Development Administration",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Thai Worker Crushed by Agricultural Machinery — Yeongam (2020)",
        "summary": (
            "A Thai EPS worker was killed when caught in a rice combine harvester on a farm "
            "in Yeongam-gun, Jeollanam-do in October 2020. Investigation revealed the worker "
            "had received no safety training on machinery operation (training materials were "
            "only in Korean), the machinery lacked required safety guards, and the worker had "
            "been operating equipment alone without supervision. The Korea Occupational Safety "
            "and Health Agency (KOSHA) cited the employer for multiple safety violations. The "
            "employer received a fine of KRW 10 million."
        ),
        "source": "KOSHA Accident Investigation Report / Jeollanam-do Labour Office",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Vinyl Greenhouse Collapse Deaths — Structural Safety Failures",
        "summary": (
            "Multiple migrant workers have been killed or seriously injured in vinyl greenhouse "
            "collapses caused by heavy snowfall and typhoons. In January 2022, a Vietnamese "
            "EPS worker was trapped under a collapsed greenhouse structure in Chungcheongnam-do "
            "during heavy snowfall and died from crush injuries. Workers housed inside or "
            "adjacent to greenhouses are particularly vulnerable. Building codes for agricultural "
            "greenhouses are weaker than for residential structures, and employer-provided "
            "housing attached to greenhouses may lack emergency exits."
        ),
        "source": "KOSHA / National Fire Agency Incident Reports",
    },

    # =====================================================================
    # 5. MANUFACTURING SECTOR WORKER CONDITIONS
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Manufacturing Sector EPS Workers — General Conditions",
        "summary": (
            "Manufacturing employs approximately 60% of all EPS workers (~170,000), primarily "
            "in small and medium enterprises (SMEs) with fewer than 30 employees. Common issues: "
            "mandatory overtime without proper premium payment, exposure to industrial chemicals "
            "without adequate ventilation, noise-induced hearing loss, repetitive strain injuries, "
            "and employer-provided dormitory housing with shared rooms (6-8 workers). Many SMEs "
            "are in industrial estates in Ansan, Siheung, Gimpo, and Hwaseong where migrant "
            "worker communities have formed."
        ),
        "source": "MOEL Annual Labour Inspection Report / Ansan Migrant Worker Center",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Ansan Industrial Complex — Migrant Worker Exploitation Hub",
        "summary": (
            "Ansan-si's Banwol-Sihwa Industrial Complex is Korea's largest concentration of "
            "EPS workers, with an estimated 30,000+ migrant workers in manufacturing. Despite "
            "the presence of migrant support centres, documented issues include: below-minimum "
            "wage payment through timecard manipulation, forced overtime with threats of "
            "contract termination, industrial accident concealment to avoid insurance premium "
            "increases, and dormitory overcrowding (some factories house 8-10 workers in rooms "
            "designed for 4). The Ansan Migrant Worker Center receives over 3,000 complaints "
            "annually."
        ),
        "source": "Ansan Foreign Residents Support Center / KCTU",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Chemical Exposure in Manufacturing — Chronic Health Effects on EPS Workers",
        "summary": (
            "EPS workers in small-scale manufacturing (plastics, chemicals, plating, painting) "
            "face chronic chemical exposure. A 2019 KOSHA study found that 35% of inspected SMEs "
            "employing EPS workers had inadequate ventilation systems, and 48% lacked Material "
            "Safety Data Sheets in workers' languages. Cases of occupational lung disease, skin "
            "conditions, and neurological symptoms among returned EPS workers have been documented "
            "in sending countries. Workers are often unaware of their right to occupational health "
            "examinations under Korean law."
        ),
        "source": "KOSHA / Korean Society of Occupational and Environmental Medicine",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Furniture Factory Fire Deaths — EPS Workers Locked in Dormitory (2020)",
        "summary": (
            "In December 2020, a fire in a plastic container dormitory adjacent to a furniture "
            "factory in Pocheon killed a Cambodian EPS worker. The dormitory door was found "
            "to have an external lock, and the heating was an illegal electric blanket that "
            "caused the fire. Investigation revealed the factory employed 12 EPS workers, all "
            "housed in container units on the factory premises with no fire extinguishers, smoke "
            "detectors, or emergency lighting. The employer was prosecuted for negligent homicide "
            "and received a suspended sentence."
        ),
        "source": "Pocheon Police / Gyeonggi-do Fire Department / NHRCK",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Manufacturing Workplace Accidents — Under-reporting Pattern",
        "summary": (
            "Industrial accident statistics for EPS workers are significantly under-reported. "
            "KCTU estimates actual workplace injuries among EPS workers are 3-5 times the "
            "official figures. Reasons: employers pressure workers not to report (threatening "
            "contract non-renewal or workplace change denial), workers fear losing visa status, "
            "language barriers prevent filing with KOSHA, and small enterprises with fewer than "
            "5 employees are exempt from some safety regulations. In 2022, officially 2,847 EPS "
            "workers reported workplace injuries; actual figures may exceed 10,000."
        ),
        "source": "KCTU / KOSHA Industrial Accident Statistics / NHRCK",
    },

    # =====================================================================
    # 6. CONSTRUCTION SECTOR E-9 VISA HOLDER ISSUES
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Construction Sector EPS Workers — Subcontracting Exploitation",
        "summary": (
            "Construction employs ~10% of EPS workers. The multi-layered subcontracting system "
            "(prime contractor to 3rd/4th-tier subcontractors) creates accountability gaps. "
            "EPS workers are typically employed by the lowest-tier subcontractor, which may "
            "lack proper safety equipment, insurance, or stable finances. Workers report being "
            "moved between sites without updating employment records, receiving wages through "
            "intermediaries who skim payments, and being exposed to fall hazards on high-rise "
            "projects without adequate harness training in their languages."
        ),
        "source": "Korea Construction Workers' Union / MOEL Construction Safety Division",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Construction Worker Falls from Height — Recurring Fatalities",
        "summary": (
            "Falls from height are the leading cause of death among EPS construction workers. "
            "Between 2018 and 2023, at least 15 EPS workers died in construction falls, "
            "predominantly from scaffolding, rooftops, and elevator shafts. Contributing factors: "
            "safety training conducted only in Korean, safety harnesses not provided at small "
            "sites, pressure to work in unsafe conditions (rain, high winds), and workers' "
            "reluctance to refuse dangerous tasks due to fear of employer retaliation. KOSHA "
            "inspections found that 60% of small construction sites employing EPS workers "
            "had at least one critical safety violation."
        ),
        "source": "KOSHA Construction Accident Database / MOEL",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Unpaid Wages in Construction — Subcontractor Bankruptcy Pattern",
        "summary": (
            "EPS construction workers are particularly vulnerable to wage theft when "
            "subcontractors go bankrupt or disappear. In 2022, 340 EPS workers in Gyeonggi "
            "Province alone filed unpaid wage claims totalling KRW 2.8 billion against failed "
            "construction subcontractors. The Wage Guarantee Insurance system covers only up to "
            "KRW 2 million per worker, far below typical arrears. Workers must navigate the "
            "Korean legal system to claim additional amounts, a process that can take 1-2 years "
            "and often yields partial recovery."
        ),
        "source": "Korea Workers' Compensation & Welfare Service / Regional Labour Offices",
    },

    # =====================================================================
    # 7. FISHING SECTOR EXPLOITATION (COASTAL AND DWF)
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Coastal Fishing Sector — EPS Worker Exploitation on Korean Vessels",
        "summary": (
            "EPS workers in coastal fishing (E-9 visa) face some of the most severe conditions: "
            "18-20 hour workdays during fishing season, sleeping on the vessel, isolation from "
            "shore for weeks, physical abuse by Korean captains, and wages below minimum after "
            "deductions for food. Workers are typically the sole migrant on small vessels (5-20 "
            "tonnes) with Korean crew, limiting access to interpretation or support. Coastal "
            "fishing is exempt from the Labour Standards Act's working hour provisions."
        ),
        "source": "National Federation of Fisheries Cooperatives / Advocates for Public Interest Law",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Deep-Water Fishing (DWF) Fleet — Non-EPS Migrant Exploitation",
        "summary": (
            "Korean distant-water fishing vessels employ approximately 25,000 migrant workers "
            "(primarily Indonesian, Vietnamese, and Filipino) on E-10-2 visas under separate "
            "regulations from EPS. Conditions documented by ILO and civil society include: "
            "20+ hour workdays, physical violence by officers, food deprivation as punishment, "
            "wage withholding until contract completion, passport confiscation on boarding, and "
            "inability to leave vessels at foreign ports. At least 14 migrant fisher deaths on "
            "Korean DWF vessels were documented between 2018 and 2023."
        ),
        "source": "ILO / Environmental Justice Foundation / Korean Institute for Maritime Strategy",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Indonesian Fishers' Deaths on Korean Vessels — UN Investigation (2022)",
        "summary": (
            "In 2022, a UN Special Rapporteur investigation highlighted at least 5 Indonesian "
            "crew member deaths on Korean-flagged distant-water fishing vessels between 2019 "
            "and 2022. Cases included suspected murder, death from untreated illness due to "
            "refusal to dock for medical care, and death from overwork. Bodies were stored in "
            "fish freezers for weeks before repatriation. Indonesia's government issued a "
            "diplomatic protest and demanded improved monitoring of Korean fishing vessels. "
            "Korea's Ministry of Oceans and Fisheries (MOF) tightened vessel inspection protocols."
        ),
        "source": "UN Special Rapporteur on Trafficking / Indonesian Ministry of Foreign Affairs",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Korean Fishing Vessel Abuse — Vietnamese Worker Assault Case (2020)",
        "summary": (
            "Video footage released in 2020 showed Korean fishing vessel captains repeatedly "
            "punching and kicking Vietnamese crew members on a coastal fishing vessel off the "
            "coast of Jeju. The footage, filmed by another crew member, went viral and prompted "
            "a police investigation. Two captains were charged with assault. The case exposed "
            "the systemic nature of violence on Korean fishing vessels and the difficulty "
            "migrant workers face in reporting abuse while at sea with no phone access."
        ),
        "source": "Korea Coast Guard / Jeju Provincial Police / Korean media reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Wando-gun Fishing Village — Collective Exploitation of Migrant Fishers",
        "summary": (
            "An investigation by the Advocates for Public Interest Law in 2021 documented "
            "systematic exploitation of 18 Vietnamese EPS workers in Wando-gun fishing village: "
            "workers were paid approximately 60% of minimum wage, housed in shipping containers "
            "near the docks, worked 18-hour days during squid season, and were not enrolled in "
            "national health insurance despite legal requirements. Employers collectively agreed "
            "not to approve workplace transfers, effectively trapping workers in the area."
        ),
        "source": "Advocates for Public Interest Law / NHRCK Jeollanam-do",
    },

    # =====================================================================
    # 8. EMPLOYER CONSENT REQUIREMENT FOR WORKPLACE CHANGE
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Employer Consent for Workplace Change — Core Structural Abuse Mechanism",
        "summary": (
            "Under EPS regulations, workers seeking to change employers generally need the "
            "current employer's signed consent on the 'workplace change application.' While "
            "exceptions exist for documented abuse, bankruptcy, or serious safety violations, "
            "the burden of proof falls on the worker. NHRCK documented that many employers "
            "refuse consent as retaliation or to maintain control, knowing the worker will "
            "become undocumented if they leave. This mechanism has been compared to the kafala "
            "system's employer sponsorship tie by Amnesty International."
        ),
        "source": "NHRCK / Amnesty International 'Bitter Harvest' 2014",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Three-Transfer Limit — Exhaustion of Workplace Change Rights",
        "summary": (
            "EPS workers are limited to 3 workplace changes during their permit period (with "
            "additional changes allowed for non-attributable reasons like employer bankruptcy). "
            "Workers who exhaust their 3 transfers must remain with their final employer "
            "regardless of conditions or face departure from Korea. This creates a perverse "
            "incentive: workers tolerate increasingly poor conditions as they approach the limit. "
            "NHRCK reported cases where employers explicitly stated 'You have no more transfers "
            "left, so you must accept what I give you.'"
        ),
        "source": "NHRCK / Migrants' Trade Union (MTU)",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Workplace Change Denial — Vietnamese Worker Suicide Case (2018)",
        "summary": (
            "In 2018, a Vietnamese EPS worker in Gimhae-si was found dead by apparent suicide "
            "after his employer refused to sign a workplace change consent form. The worker "
            "had endured 6 months of verbal abuse and below-minimum-wage payment. His request "
            "for transfer was denied by the employer who claimed the worker was 'essential.' "
            "The Job Centre did not intervene because the abuse did not meet the threshold for "
            "a forced transfer. The case was cited by NHRCK in its recommendation to abolish "
            "the employer consent requirement."
        ),
        "source": "NHRCK / Gimhae Migrant Worker Counseling Center",
    },

    # =====================================================================
    # 9. "3 MONTHS RE-EMPLOYMENT" DEADLINE AND PRESSURE
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Three-Month Job Search Deadline — Structural Pressure on EPS Workers",
        "summary": (
            "When an EPS worker leaves an employer (for any reason), they must find a new "
            "employer within 3 months or lose their visa status and face deportation. During "
            "this period, the worker cannot legally work and must rely on savings. HRD Korea's "
            "Job Centre matches workers with employers, but options may be limited by sector, "
            "region, and language. The 3-month clock creates intense pressure to accept the "
            "first available position regardless of conditions, wages, or location. Workers "
            "in remote agricultural areas face particular difficulty due to limited local options."
        ),
        "source": "HRD Korea / MOEL / Migrant Worker Support Centers",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Job Centre Matching Failures — Workers Pushed into Exploitative Workplaces",
        "summary": (
            "The HRD Korea Job Centre matching system has been criticised for prioritising "
            "employer needs over worker safety. Workers report being offered only 1-2 employer "
            "choices, often in the same sector and region where they experienced abuse. A 2020 "
            "NHRCK investigation found that 45% of EPS workers who changed workplaces ended "
            "up in conditions similar to or worse than their previous employer. The system "
            "does not flag employers with prior complaints or labour law violations, effectively "
            "recycling workers through problematic workplaces."
        ),
        "source": "NHRCK Investigation Report 2020 / Migrant Worker Advocacy Groups",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Visa Expiry During Job Search — Forced Undocumented Status",
        "summary": (
            "Workers whose 3-month job search period expires become undocumented. Between 2018 "
            "and 2022, an estimated 15,000-20,000 EPS workers annually became undocumented "
            "during the job search process, not through absconding but through system failure. "
            "Once undocumented, they lose all labour law protections, health insurance, and "
            "access to complaint mechanisms. Many continue working in the informal economy at "
            "below-minimum wages, highly vulnerable to exploitation. Immigration enforcement "
            "raids target these workers rather than exploitative employers."
        ),
        "source": "Korea Immigration Service Statistics / Joint Committee with Migrants in Korea (JCMK)",
    },

    # =====================================================================
    # 10. WORKPLACE ACCIDENT AND DEATH COMPENSATION CASES
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Industrial Accident Compensation for EPS Workers — Legal Framework",
        "summary": (
            "EPS workers are covered by the Industrial Accident Compensation Insurance Act on "
            "the same basis as Korean workers. Coverage includes medical treatment, temporary "
            "disability benefits, permanent disability benefits, and survivor benefits for "
            "workplace deaths. However, obstacles to claiming include: employer failure to "
            "report accidents, language barriers in filing claims, workers not knowing their "
            "rights, and pressure to accept private settlements below legal entitlements. "
            "Undocumented workers are also legally covered but rarely claim due to deportation fear."
        ),
        "source": "Korea Workers' Compensation & Welfare Service (COMWEL)",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Worker Death Compensation — Systemic Under-Compensation Pattern",
        "summary": (
            "When EPS workers die in workplace accidents, families in home countries face "
            "extreme difficulty navigating Korean compensation systems. Documented patterns: "
            "employers offer families small 'consolation money' (KRW 5-20 million) far below "
            "legal entitlements (which can exceed KRW 100 million); families sign waivers in "
            "Korean they cannot read; embassies lack capacity to assist in all cases; and "
            "the 3-year statute of limitations expires before families learn of their rights. "
            "NGOs report that fewer than 30% of eligible families receive full statutory benefits."
        ),
        "source": "NHRCK / IOM Korea / Sending Country Embassy Reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Cambodian Worker Accident Case — Employer Settlement Pressure (2021)",
        "summary": (
            "A Cambodian EPS worker who lost three fingers in a press machine at a Hwaseong "
            "metal-stamping factory in 2021 was pressured by the employer to accept a private "
            "settlement of KRW 8 million (approximately USD 6,500) instead of filing an "
            "industrial accident claim that would have entitled them to approximately KRW 50-80 "
            "million in disability benefits. The employer threatened to deny the workplace "
            "change consent if the worker filed an official claim. With assistance from the "
            "Hwaseong Migrant Worker Center, the worker filed a COMWEL claim and received "
            "full statutory benefits after 14 months of processing."
        ),
        "source": "Hwaseong Migrant Worker Center / COMWEL",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Occupational Disease Claims — EPS Workers' Barriers to Diagnosis",
        "summary": (
            "EPS workers with occupational diseases (hearing loss, respiratory conditions, "
            "musculoskeletal disorders) face particular barriers: symptoms may not appear until "
            "after returning home, Korean medical records are difficult to obtain from abroad, "
            "occupational disease claims require proof of workplace causation (difficult without "
            "employer cooperation), and the Occupational Disease Adjudication Committee's "
            "proceedings are conducted entirely in Korean. Between 2018 and 2022, only 89 "
            "occupational disease claims were approved for E-9 visa holders, compared to an "
            "estimated actual prevalence of thousands."
        ),
        "source": "COMWEL / Korean Society of Occupational and Environmental Medicine",
    },

    # =====================================================================
    # 11. KOREAN SUPREME COURT DECISIONS ON EPS WORKER RIGHTS
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Korean Supreme Court 2007Da4995 — EPS Workers Entitled to Retirement Allowance",
        "court": "Supreme Court of Korea",
        "year": 2015,
        "summary": (
            "The Supreme Court held that EPS (E-9) workers are entitled to retirement allowance "
            "(severance pay) under the Labour Standards Act on the same basis as Korean workers, "
            "calculated as 30 days' average wage per year of continuous service. Employers had "
            "argued that the temporary and foreign nature of EPS employment excluded them from "
            "this entitlement. The Court confirmed that the Labour Standards Act applies without "
            "distinction based on nationality or visa status. This ruling established that all "
            "EPS workers completing 1+ years are owed severance."
        ),
        "source": "Supreme Court of Korea / Korean Law Information Center",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Supreme Court 2015Du36205 — Undocumented Worker Wage Rights (2015)",
        "court": "Supreme Court of Korea",
        "year": 2015,
        "summary": (
            "The Supreme Court reaffirmed that undocumented migrant workers retain full labour "
            "rights including minimum wage, overtime pay, and industrial accident compensation. "
            "An undocumented worker's employment contract is voidable but not void — the worker "
            "is entitled to wages for work already performed. The Court stated that immigration "
            "violations do not extinguish labour law protections. This ruling is critical for "
            "former EPS workers who overstayed and continued working in exploitative conditions."
        ),
        "source": "Supreme Court of Korea / NHRCK Legal Digest",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Supreme Court 2018Da200709 — Employer Liability for Agricultural Worker Death",
        "court": "Supreme Court of Korea",
        "year": 2020,
        "summary": (
            "The Supreme Court upheld employer liability for the death of a Thai EPS worker on "
            "a livestock farm in Chungcheongbuk-do who died from a pre-existing heart condition "
            "exacerbated by extreme working conditions (16-hour days, unventilated barn, "
            "heatwave). The Court found that even though the worker had a pre-existing condition, "
            "the employer's failure to provide adequate rest breaks, cooling, and medical access "
            "constituted a proximate cause. Survivor benefits and employer negligence damages "
            "were awarded to the family."
        ),
        "source": "Supreme Court of Korea / COMWEL Case Digest",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Supreme Court 2019Da207487 — Right to Change Workplace Without Employer Consent",
        "court": "Supreme Court of Korea",
        "year": 2021,
        "summary": (
            "In a significant ruling, the Supreme Court held that an EPS worker who was denied "
            "workplace change by the employer due to documented sexual harassment by a supervisor "
            "was entitled to a transfer without employer consent. The Court interpreted the "
            "workplace change provisions broadly, stating that 'reasons not attributable to the "
            "worker' include workplace harassment and abuse, and that the employer's refusal to "
            "consent in such cases does not prevent the transfer. This expanded the scope of "
            "non-consent workplace changes."
        ),
        "source": "Supreme Court of Korea / Migrants' Rights Legal Support Center",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Supreme Court — Minimum Wage Applies to All Foreign Workers Including EPS",
        "court": "Supreme Court of Korea",
        "year": 2012,
        "summary": (
            "The Supreme Court confirmed that Korea's Minimum Wage Act applies to all foreign "
            "workers regardless of visa status. Employers cannot set wages below the statutory "
            "minimum even by mutual agreement. Furthermore, deductions for employer-provided "
            "housing and meals cannot reduce actual received wages below the minimum wage. This "
            "ruling addressed the practice of agricultural employers deducting substantial "
            "amounts for room and board from already-low wages."
        ),
        "source": "Supreme Court of Korea / MOEL Legal Interpretation",
    },

    # =====================================================================
    # 12. CONSTITUTIONAL COURT DECISIONS ON WORKER PROTECTIONS
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Constitutional Court 2011Hun-Ma395 — EPS Workplace Change Restriction",
        "court": "Constitutional Court of Korea",
        "year": 2011,
        "summary": (
            "The Constitutional Court upheld the constitutionality of the EPS workplace change "
            "limitation (originally 3 times) but stated that the restriction must be interpreted "
            "in light of workers' fundamental rights. The Court noted that overly restrictive "
            "application could violate Article 32 (right to work) of the Constitution. This "
            "decision was seen as a partial victory — while not striking down the limitation, "
            "it established that administrative agencies must apply it with consideration for "
            "worker vulnerability. Subsequently, the number of permissible changes was increased."
        ),
        "source": "Constitutional Court of Korea / Korean Bar Association Analysis",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Constitutional Court 2007Hun-Ma1083 — Crackdown on Undocumented Workers",
        "court": "Constitutional Court of Korea",
        "year": 2012,
        "summary": (
            "In a challenge to the aggressive enforcement campaign against undocumented migrant "
            "workers, the Constitutional Court held that while the government may enforce "
            "immigration law, enforcement actions must respect fundamental human rights. The "
            "Court noted that undocumented status does not strip a person of constitutional "
            "protections including dignity, safety, and fair treatment. This decision limited "
            "the use of violent raid tactics against undocumented workers and required proper "
            "procedural protections during apprehension and detention."
        ),
        "source": "Constitutional Court of Korea / NHRCK",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Constitutional Court — Industrial Trainee System Unconstitutional Aspects (2007)",
        "court": "Constitutional Court of Korea",
        "year": 2007,
        "summary": (
            "The Constitutional Court found that aspects of the predecessor Industrial Trainee "
            "System (ITS) violated the Constitution's equal protection clause by denying "
            "'trainees' the same labour protections as 'employees.' This ruling effectively "
            "mandated the full transition to EPS, under which migrant workers are recognised as "
            "employees with full Labour Standards Act coverage. The decision was instrumental "
            "in dismantling the ITS framework that had facilitated systemic exploitation under "
            "the guise of 'training.'"
        ),
        "source": "Constitutional Court of Korea / Korean Labour Law Association",
    },

    # =====================================================================
    # 13. NHRCK (NATIONAL HUMAN RIGHTS COMMISSION) INVESTIGATIONS
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "NHRCK 2013 Recommendation — Agricultural Migrant Worker Human Rights",
        "summary": (
            "The NHRCK conducted a comprehensive investigation into migrant agricultural worker "
            "conditions and issued a formal recommendation to MOEL and the Ministry of "
            "Agriculture in 2013. Key findings: 70% of agricultural EPS workers worked more "
            "than 12 hours daily, 85% received no overtime premium, 60% lived in substandard "
            "housing (containers, greenhouses, barns), 45% experienced verbal abuse by employers, "
            "and 30% reported pesticide exposure without PPE. The NHRCK recommended: removing "
            "agricultural exemption from working hour limits, mandatory housing standards, and "
            "multilingual safety training."
        ),
        "source": "NHRCK Recommendation 13Jin0629400",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "NHRCK 2019 Investigation — EPS Worker Housing Conditions",
        "summary": (
            "A 2019 NHRCK site inspection of 200 EPS worker housing units across 8 provinces "
            "found: 32% of units failed to meet minimum legal space requirements (2 pyeong / "
            "6.6 sqm per person), 28% lacked heating in winter, 41% had no indoor plumbing, "
            "18% had structural safety issues, and 12% housed workers in agricultural "
            "structures (greenhouses, barns, sheds) not designed for human habitation. The NHRCK "
            "recommended mandatory housing inspections before EPS worker placement and "
            "enforcement of building code compliance for worker dormitories."
        ),
        "source": "NHRCK Housing Inspection Report 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "NHRCK 2021 Recommendation — Abolish Employer Consent for Workplace Change",
        "summary": (
            "In 2021, the NHRCK formally recommended that MOEL abolish the requirement for "
            "employer consent for EPS workplace changes, characterising it as a structural "
            "mechanism enabling labour exploitation. The NHRCK documented 854 cases over 3 "
            "years where employer consent refusal trapped workers in exploitative conditions. "
            "The recommendation also called for extending the 3-month job search period to "
            "6 months, removing the 3-transfer limit for abuse-related changes, and creating "
            "an independent workplace change adjudication body."
        ),
        "source": "NHRCK Policy Recommendation 21-4",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "NHRCK Investigation of Migrant Worker Deaths — Systemic Review (2022)",
        "summary": (
            "The NHRCK published a systemic review of migrant worker deaths in Korea (2017-2021), "
            "documenting 396 migrant worker deaths over 5 years, of which approximately 60% "
            "were EPS holders. Causes: workplace accidents (42%), health conditions exacerbated "
            "by working conditions (28%), suicide (12%), heatstroke (8%), and other (10%). "
            "The NHRCK found that 65% of workplace accident deaths involved safety violations "
            "by the employer, and 78% of deceased workers had never received safety training "
            "in their native language."
        ),
        "source": "NHRCK Special Report on Migrant Worker Deaths 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "NHRCK — Discrimination in COVID-19 Response Against Migrant Workers",
        "summary": (
            "During the COVID-19 pandemic, the NHRCK investigated discriminatory treatment of "
            "migrant workers including: mandatory segregated testing for EPS workers in "
            "agricultural areas, public disclosure of infected migrant workers' nationalities "
            "and workplaces (not done for Korean workers), employer-imposed quarantine in "
            "inadequate facilities (shipping containers, factory floors), and exclusion from "
            "government relief payments. Undocumented workers avoided testing and vaccination "
            "due to fear of arrest, contributing to outbreak clusters in migrant communities."
        ),
        "source": "NHRCK / JCMK / Korea Disease Control and Prevention Agency",
    },

    # =====================================================================
    # 14. UNDOCUMENTED WORKER EXPLOITATION
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Undocumented EPS Overstayers — Scale and Vulnerability",
        "summary": (
            "An estimated 350,000-400,000 undocumented migrant workers live in Korea, many "
            "of whom are former EPS workers who overstayed their visas. Primary reasons for "
            "overstaying: inability to find new employer within 3-month deadline, desire to "
            "continue earning (families depend on remittances), debt from migration costs not "
            "yet repaid, and fear of returning home without savings. Undocumented workers accept "
            "wages 20-40% below minimum wage, work in the most dangerous jobs (demolition, "
            "waste processing), and have no recourse against exploitation."
        ),
        "source": "Korea Immigration Service / JCMK / MTU",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Crackdown Raids — Immigration Enforcement Targeting Workers Not Employers",
        "summary": (
            "Korea Immigration Service conducts regular enforcement raids on workplaces and "
            "neighbourhoods with high migrant populations. Between 2018 and 2023, approximately "
            "30,000-40,000 undocumented workers were apprehended annually. Advocates note the "
            "asymmetry: employers hiring undocumented workers face only modest fines (KRW 2-4 "
            "million), while workers face detention and deportation. Employers have been "
            "documented threatening to report workers to immigration authorities as a coercion "
            "tool. Some employers call immigration after workers demand unpaid wages."
        ),
        "source": "Korea Immigration Service / MTU / JCMK",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Undocumented Worker Killed in Industrial Accident — Employer Concealment (2019)",
        "summary": (
            "An undocumented Myanmar worker was killed in a metal press accident at a small "
            "factory in Siheung in 2019. The employer attempted to conceal the death by moving "
            "the body and cleaning the machine before calling authorities, claiming the worker "
            "was an unknown trespasser. Co-workers (also undocumented) eventually reported the "
            "truth to the Ansan Migrant Worker Center. The employer was prosecuted for evidence "
            "destruction and labour law violations. The case highlighted how undocumented status "
            "enables employers to conceal workplace deaths."
        ),
        "source": "Ansan Migrant Worker Center / Gyeonggi Nambu Police",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Voluntary Departure Programme — Amnesty Periods for Undocumented Workers",
        "summary": (
            "Korea periodically offers voluntary departure programmes allowing undocumented "
            "workers to leave without penalties (entry ban reduction from 5 years to 1 year). "
            "However, advocates note that employers exploit the announcement periods by "
            "threatening to fire undocumented workers and hiring replacements at even lower "
            "wages. Workers who voluntarily depart often leave with significant unpaid wages, "
            "unable to file claims from abroad. The programmes address immigration enforcement "
            "statistics but do not address the exploitation that drove workers to overstay."
        ),
        "source": "Korea Immigration Service / IOM Korea",
    },

    # =====================================================================
    # 15. SPECIFIC FARM OWNER PROSECUTION CASES
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Yesan Farm Owner Prosecution — Assault and Confinement of Cambodian Workers (2019)",
        "court": "Daejeon District Court",
        "year": 2019,
        "summary": (
            "A Yesan-gun farm owner was prosecuted for physically assaulting three Cambodian "
            "EPS workers over a 2-year period, confining them to the farm premises by confiscating "
            "their alien registration cards, and paying wages approximately 40% below the minimum "
            "wage after illegal deductions. The workers escaped with assistance from a Cambodian "
            "community member who contacted the local migrant worker centre. The farm owner was "
            "convicted of assault, wage theft, and document confiscation, receiving a 1-year "
            "suspended prison sentence and KRW 5 million fine. Workers received back wages."
        ),
        "source": "Daejeon District Court / Chungnam Migrant Worker Center",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Hapcheon Garlic Farm Prosecution — Wage Theft and Abuse (2020)",
        "court": "Changwon District Court",
        "year": 2020,
        "summary": (
            "The owner of a garlic and onion farm in Hapcheon-gun was convicted after four "
            "Vietnamese EPS workers filed complaints for: 18 months of wage underpayment (paying "
            "KRW 1.2 million monthly instead of the minimum KRW 1.7 million), forcing workers "
            "to live in a barn with livestock, denying medical treatment for a worker who "
            "fractured a wrist, and refusing to sign workplace change forms. The court sentenced "
            "the owner to 10 months imprisonment (suspended) and ordered payment of KRW 38 "
            "million in back wages. The relatively light sentence was criticised by labour groups."
        ),
        "source": "Changwon District Court / Gyeongsangnam-do Labour Office",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Naju Greenhouse Owner Prosecution — Sexual Harassment and Wage Theft (2021)",
        "court": "Gwangju District Court",
        "year": 2021,
        "summary": (
            "A Naju-si greenhouse owner was prosecuted for sexually harassing a female Cambodian "
            "EPS worker over 8 months and systematically underpaying all four workers on the "
            "farm. The owner had threatened to refuse workplace change consent if the victim "
            "reported the harassment. The case came to light when the worker sought medical "
            "treatment for stress-related illness and disclosed the situation to a counsellor. "
            "The owner was convicted of sexual harassment under the Criminal Act and labour law "
            "violations, receiving 2 years imprisonment (not suspended)."
        ),
        "source": "Gwangju District Court / Women Migrants Human Rights Center Korea",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Boryeong Livestock Farm Prosecution — Forced Labour Conditions (2022)",
        "court": "Daejeon District Court, Seosan Branch",
        "year": 2022,
        "summary": (
            "A livestock farm owner in Boryeong-si was convicted after a Nepali EPS worker "
            "reported being forced to work 18-20 hours daily caring for 3,000 pigs with only "
            "4-5 hours of sleep, housed in a room attached to the pig barn with no heating in "
            "winter, denied days off for 11 consecutive months, and threatened with deportation "
            "if he complained. MOEL inspectors confirmed the conditions. The court found the "
            "employer guilty of Labour Standards Act violations and sentenced them to 8 months "
            "imprisonment (suspended) with back wage payment of KRW 24 million."
        ),
        "source": "Daejeon District Court / MOEL Investigation / NHRCK",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Gochang Watermelon Farm — Employer Convicted of Worker Abuse (2023)",
        "court": "Jeonju District Court",
        "year": 2023,
        "summary": (
            "A watermelon farm owner in Gochang-gun was convicted after investigation revealed "
            "systematic abuse of two Thai EPS workers: physical beatings when work pace was "
            "deemed insufficient, wages paid in cash with no pay stubs (actual payment ~60% "
            "of minimum wage), forced signing of false wage receipts showing full payment, and "
            "housing in a greenhouse storage room without sanitation facilities. The workers "
            "were discovered during a routine MOEL inspection prompted by an anonymous tip. "
            "The employer received 1 year imprisonment (actual) — a notably severe sentence "
            "for agricultural labour violations."
        ),
        "source": "Jeonju District Court / MOEL Inspection Division",
    },

    # =====================================================================
    # 16. ASAN AND POCHEON GREENHOUSE WORKER CASES
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Asan Greenhouse District — Concentration of Migrant Worker Exploitation",
        "summary": (
            "Asan-si in Chungcheongnam-do is one of Korea's major greenhouse farming districts, "
            "employing over 2,000 EPS workers (primarily Cambodian, Thai, and Vietnamese) in "
            "pepper, tomato, and chrysanthemum cultivation. The Asan Migrant Worker Counseling "
            "Center documented between 2018-2023: 180+ wage theft complaints, 45 workplace "
            "change denial complaints, 12 assault cases, 8 housing standard violations "
            "(container housing without utilities), and 3 worker deaths (2 heat-related, "
            "1 pesticide-related). Despite this volume, employer prosecution rates remained "
            "below 10% of documented violations."
        ),
        "source": "Asan Migrant Worker Counseling Center Annual Reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Asan — Cambodian Worker Found Dead in Container Housing (2020)",
        "summary": (
            "A 29-year-old Cambodian EPS worker was found dead in his container housing unit "
            "on a chrysanthemum farm in Asan in January 2020. The cause of death was determined "
            "to be hypothermia — the container had no heating and nighttime temperatures dropped "
            "to -18C. The worker's electric heater had been removed by the employer to reduce "
            "electricity costs. Investigation found that the container had gaps in the walls and "
            "no insulation. The employer claimed the worker was provided blankets. NHRCK took "
            "up the case and issued a recommendation for mandatory heating standards in worker "
            "housing. The employer was fined but not criminally charged."
        ),
        "source": "NHRCK / Asan Migrant Worker Counseling Center / Chungcheongnam-do Police",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Pocheon Container Housing Fire — Multiple Worker Casualties (2020)",
        "summary": (
            "In December 2020, a fire broke out in shipping container housing at a Pocheon "
            "strawberry farm, killing one Cambodian worker and injuring three others. The fire "
            "was caused by an overloaded electrical outlet powering makeshift heaters. "
            "Investigation revealed: containers housed 6 workers each (designed for storage), "
            "no fire extinguishers or smoke detectors were installed, the containers had only "
            "one exit door (which jammed), and the employer had not registered the containers "
            "as worker housing with local authorities. The case drew national media attention "
            "to the container housing conditions of migrant agricultural workers."
        ),
        "source": "Gyeonggi-do Fire Department / Pocheon Police / Korean Broadcasting System (KBS)",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Pocheon Mushroom Farm — Systematic Wage Theft and Overwork (2021)",
        "summary": (
            "Six Nepali EPS workers on a Pocheon mushroom farm filed a collective complaint "
            "with the Uijeongbu Labour Office in 2021, alleging: 15-16 hour workdays with "
            "no rest days during peak harvest (Oct-Apr), wages paid as a fixed monthly amount "
            "regardless of hours (effective hourly rate approximately 60% of minimum wage), "
            "deductions of KRW 400,000/month for housing (a shared container) and food (rice "
            "only), and employer refusal to provide pay stubs. The Labour Office inspection "
            "confirmed violations and ordered back wage payment of KRW 67 million across all "
            "six workers. The employer appealed, delaying payment by 18 months."
        ),
        "source": "Uijeongbu Regional Labour Office / Pocheon Migrant Worker Center",
    },

    # =====================================================================
    # 17. PLASTIC GREENHOUSE WORKER DEATHS (HYPERTHERMIA)
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Plastic Greenhouse Hyperthermia Deaths — Environmental Analysis",
        "summary": (
            "Korean agricultural greenhouses (typically single- or double-layer polyethylene "
            "plastic over steel frames) create extreme heat conditions. A 2020 study by the "
            "Rural Development Administration found greenhouse interior temperatures regularly "
            "exceed outdoor temperatures by 10-20C, reaching 50-60C in July-August. Even with "
            "ventilation panels open, interior temperatures remained above 40C during heatwaves. "
            "Most greenhouses lack mechanical cooling. Workers performing physical tasks inside "
            "(harvesting, spraying, transplanting) face severe heat stress. The study recommended "
            "mandatory 15-minute breaks every 2 hours when temperatures exceed 33C, but this "
            "remains advisory, not legally binding."
        ),
        "source": "Rural Development Administration / Korea Occupational Safety and Health Research Institute",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Thai Worker Heatstroke Death — Buyeo Paprika Greenhouse (2022)",
        "summary": (
            "A 38-year-old Thai EPS worker died of heatstroke while harvesting paprika in a "
            "Buyeo-gun greenhouse in August 2022, during a heatwave that pushed outdoor "
            "temperatures to 38C. Co-workers reported the greenhouse was 'like a sauna' and "
            "estimated interior temperatures above 55C. The worker collapsed around 2 PM and "
            "was not transported to hospital until 40 minutes later because the employer first "
            "tried to revive him with water. He was pronounced dead on arrival. KOSHA cited "
            "the employer for failing to implement heat illness prevention measures. The family "
            "in Thailand received COMWEL survivor benefits of approximately KRW 80 million "
            "after 10 months of processing."
        ),
        "source": "KOSHA / Buyeo Police / COMWEL",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Consecutive Greenhouse Deaths Prompt MOEL Guidelines (2021)",
        "summary": (
            "After three migrant worker heatstroke deaths in greenhouses within a single month "
            "(July 2021), MOEL issued emergency guidelines: agricultural employers must provide "
            "shaded rest areas, supply water and electrolytes, allow 15-minute breaks every "
            "2 hours above 33C, and stop outdoor/greenhouse work above 35C between 2-5 PM. "
            "However, the guidelines are advisory with no penalty for non-compliance. A follow-up "
            "inspection of 500 greenhouse farms found only 23% had implemented the rest area "
            "requirement and 15% had modified work schedules during heat warnings. Migrant "
            "workers reported that requesting heat breaks was met with hostility by employers."
        ),
        "source": "MOEL Emergency Guidelines 2021 / KOSHA Compliance Survey",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Nighttime Housing Deaths — Heat Not Limited to Daytime Work",
        "summary": (
            "Several migrant worker heat-related deaths occurred in housing units, not during "
            "work. Workers in container or greenhouse-attached housing face extreme nighttime "
            "temperatures in summer (containers retain heat, reaching 35-40C at night). A 2022 "
            "case in Yesan involved a Vietnamese worker found dead in a container at 5 AM with "
            "body temperature indicators consistent with prolonged heat exposure. The container "
            "had no air conditioning or fan. NHRCK investigations found that 40% of agricultural "
            "worker housing in Chungcheongnam-do and Jeollanam-do lacked any cooling equipment."
        ),
        "source": "NHRCK / Chungnam Migrant Worker Center",
    },

    # =====================================================================
    # 18. LIVESTOCK WORKER CONDITIONS (ISOLATION, HOUSING)
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Livestock Sector EPS Workers — Extreme Isolation and Working Hours",
        "summary": (
            "EPS workers in the livestock sector (pig, cattle, and poultry farms) face unique "
            "challenges: farms are typically in remote rural areas with no public transport, "
            "workers are often the sole migrant employee on a farm, housing is frequently on "
            "the farm premises (sometimes in rooms attached to animal barns), and the 24/7 "
            "nature of animal care means workers are expected to be available at all times "
            "including nights and weekends. A 2021 survey by the Korean Livestock Farmers' "
            "Association found that 70% of EPS livestock workers worked 7 days per week with "
            "no regular days off, averaging 14 hours daily."
        ),
        "source": "NHRCK / Korean Livestock Farmers' Association Survey",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Pig Farm Worker Isolation — Psychological Impact Documentation",
        "summary": (
            "Migrant Worker Health Research Centre (Asan Hospital) documented severe psychological "
            "impacts on isolated livestock workers: 62% of surveyed EPS livestock workers showed "
            "symptoms of depression, 48% reported anxiety, and 35% experienced insomnia. "
            "Contributing factors: geographic isolation (nearest town 10-30 km), language "
            "barrier with employer (sole daily contact), inability to access religious or "
            "community gatherings, limited phone/internet access in remote areas, and the "
            "psychologically draining nature of confined animal feeding operations. Workers "
            "described feeling 'imprisoned on the farm.'"
        ),
        "source": "Asan Hospital Migrant Worker Health Research / NHRCK",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Cattle Farm Worker — Forced to Sleep with Animals (Chungbuk, 2021)",
        "summary": (
            "A Cambodian EPS worker on a cattle ranch in Chungcheongbuk-do was found by NHRCK "
            "investigators to be sleeping on a raised platform inside the cattle barn, with no "
            "separate living quarters. The worker had been provided a mattress and blankets but "
            "no walls, door, or privacy. The barn was unheated, exposed to animal waste "
            "odours and dust, and lacked sanitation facilities (the worker used a field). The "
            "employer stated that 'the worker needs to be close to the animals for nighttime "
            "care.' NHRCK issued a corrective recommendation. The worker requested a transfer "
            "but was initially denied because the employer refused to sign consent."
        ),
        "source": "NHRCK On-Site Investigation Report / Chungbuk Migrant Worker Center",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Poultry Farm H5N1 Response — Migrant Worker Endangerment (2023)",
        "summary": (
            "During a 2023 avian influenza (H5N1) outbreak, EPS workers on poultry farms in "
            "Gyeonggi and Chungcheong provinces were required to participate in mass culling "
            "operations without adequate PPE. Workers reported being provided only basic masks "
            "(not N95) while handling potentially infected birds, working 20+ hour shifts during "
            "emergency culling, and not being informed about the zoonotic risks. Korean military "
            "personnel involved in the same operations received full hazmat suits. The disparity "
            "in PPE provision between Korean personnel and migrant workers was documented by "
            "the Korean Confederation of Trade Unions."
        ),
        "source": "KCTU / Korea Disease Control and Prevention Agency / Chungnam Migrant Center",
    },

    # =====================================================================
    # 19. KOREAN LABOUR STANDARDS ENFORCEMENT FOR EPS WORKERS
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "MOEL Labour Inspections — EPS Workplace Compliance Rates",
        "summary": (
            "MOEL conducts annual targeted inspections of workplaces employing EPS workers. "
            "The 2022 inspection of 3,200 workplaces found: 48% had at least one labour law "
            "violation, 32% violated minimum wage provisions (under-payment, illegal deductions), "
            "28% failed to provide required employment documents in workers' languages, 22% "
            "violated working hour regulations (in non-exempt sectors), and 15% had not enrolled "
            "workers in mandatory insurance. Agricultural workplaces had the highest violation "
            "rate (62%), followed by fishing (58%), manufacturing (42%), and construction (38%)."
        ),
        "source": "MOEL Annual Inspection Report / Korea Labour Institute",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Enforcement Gap — Penalties Too Low to Deter Exploitation",
        "summary": (
            "Labour advocates argue that enforcement penalties for EPS workplace violations are "
            "too low to deter exploitation. Standard penalties: minimum wage violations result "
            "in corrective orders (first offence) or fines of KRW 2-5 million; safety violations "
            "result in fines of KRW 5-10 million; document violations result in fines of KRW "
            "1-3 million. Criminal prosecution (imprisonment) is reserved for severe or repeated "
            "violations. KCTU analysis found that 80% of employers found violating EPS worker "
            "rights received only corrective orders with no financial penalty, and only 3% "
            "of documented violations resulted in criminal prosecution."
        ),
        "source": "KCTU / Korea Labour Institute Policy Brief",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Language Barriers in Complaint Filing — Systemic Access Issue",
        "summary": (
            "EPS workers seeking to file labour complaints face significant language barriers. "
            "Labour Office complaint forms are in Korean only. Interpretation services are "
            "available at regional labour offices but limited to major languages and appointment "
            "hours. The MOEL 1350 helpline offers interpretation in some languages but call "
            "wait times average 20-40 minutes. Workers in remote agricultural or fishing areas "
            "may have no physical access to a labour office. A 2020 survey found that 65% of "
            "EPS workers who experienced labour violations did not file complaints, with 'language "
            "barrier' and 'fear of employer retaliation' as the top two reasons."
        ),
        "source": "MOEL / Korea Legal Aid Corporation / Migrant Worker Support Centers",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "2021 Amendment — Strengthened Employer Penalties for EPS Violations",
        "summary": (
            "In 2021, the Act on Foreign Workers' Employment was amended to increase penalties "
            "for employers who: violate EPS workers' right to change workplaces (fine increased "
            "to KRW 30 million), confiscate workers' passports or alien registration cards "
            "(criminal penalty: up to 5 years imprisonment), or engage in forced labour "
            "(criminal penalty aligned with Trafficking in Persons Act). The amendment also "
            "mandated MOEL to establish a multilingual complaint hotline and provide real-time "
            "interpretation at all regional labour offices by 2023."
        ),
        "source": "Korea National Assembly / Act on Foreign Workers' Employment Amendment 2021",
    },

    # =====================================================================
    # 20. MOU COUNTRY-SPECIFIC EXPERIENCES
    # =====================================================================

    # ── Cambodia ──────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Cambodian EPS Workers — Highest Vulnerability Profile",
        "summary": (
            "Cambodian EPS workers are disproportionately concentrated in agriculture (estimated "
            "40-50% of Cambodian EPS workers vs. 20% overall), the sector with the weakest "
            "protections. Cambodia's sending agency (Ministry of Labour and Vocational Training) "
            "has been criticised for inadequate pre-departure orientation — only 2 weeks compared "
            "to Philippines' 3 weeks. Cambodian workers report the highest unofficial migration "
            "costs among EPS sending countries (USD 2,500-5,000 including language training and "
            "intermediary fees), creating debt pressure that inhibits complaint-filing."
        ),
        "source": "IOM Cambodia / Cambodia Ministry of Labour / Phnom Penh Post",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Cambodian Worker Deaths in Korea — Embassy Response Capacity",
        "summary": (
            "Between 2018 and 2023, the Cambodian Embassy in Seoul reported handling 28 cases "
            "of Cambodian worker deaths in Korea, the majority in agricultural settings. The "
            "Embassy's Labour Attache office has 2 staff members to serve approximately 50,000 "
            "Cambodian workers (documented and undocumented). Embassy officials acknowledged "
            "inability to attend all workplace accident sites, negotiate compensation for all "
            "families, or provide legal representation. Many families in Cambodia received only "
            "the employer's initial 'consolation payment' without learning about statutory "
            "entitlements."
        ),
        "source": "Royal Embassy of Cambodia in Seoul / Cambodian Association in Korea",
    },

    # ── Vietnam ───────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Vietnamese EPS Workers — Largest National Group and Overstay Challenges",
        "summary": (
            "Vietnam is the largest source country for EPS workers, with approximately 50,000-60,000 "
            "documented Vietnamese E-9 holders and an estimated 40,000-50,000 undocumented "
            "Vietnamese workers in Korea. Vietnam's Centre for Overseas Labour (COLAB/DOLAB) "
            "administers the programme but has faced criticism for allowing sub-agents to charge "
            "unofficial fees of USD 1,000-3,000. Vietnam periodically faces EPS quota reductions "
            "due to high overstay rates (historically 25-35%). Korean factories in Ansan and "
            "Gimpo have large Vietnamese worker communities with support networks."
        ),
        "source": "Vietnam DOLAB / Korea HRD Service / IOM Vietnam",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Vietnamese Worker Collective Complaint — Siheung Manufacturing (2022)",
        "summary": (
            "Twelve Vietnamese EPS workers at a Siheung plastics factory filed a collective "
            "complaint in 2022 alleging: systematic overtime without premium payment (average "
            "60 hours/week), mandatory Saturday work counted as regular hours, dormitory "
            "deductions of KRW 300,000/month for a shared room with 6 workers, and threats of "
            "contract termination for refusing overtime. The Ansan Labour Office investigation "
            "confirmed violations. Total back wages owed exceeded KRW 180 million. The employer "
            "negotiated a settlement paying 80% over 12 monthly instalments. Workers were "
            "subsequently transferred to different employers."
        ),
        "source": "Ansan Regional Labour Office / Vietnamese Workers' Association in Korea",
    },

    # ── Indonesia ─────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Indonesian EPS Workers — Fishing Sector Concentration",
        "summary": (
            "Indonesian EPS workers are heavily concentrated in Korea's fishing sector, both "
            "coastal (E-9) and distant-water (E-10-2). Indonesia's sending agency (BP2MI, "
            "formerly BNP2TKI) manages EPS recruitment. Indonesian fishers face the most extreme "
            "conditions: vessels at sea for weeks, physical violence documented on multiple "
            "vessels, separation from shore-based support services, and wages structured as "
            "catch-share rather than fixed monthly amounts (resulting in income volatility). "
            "Indonesian Embassy in Seoul handles more fisher exploitation complaints than any "
            "other nationality."
        ),
        "source": "Indonesian Embassy Seoul / BP2MI / ILO Fishing Sector Studies",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Indonesian Fisher Abuse — Witness Testimony on Korean DWF Vessel (2021)",
        "summary": (
            "An Indonesian crew member who escaped a Korean DWF vessel at Busan port in 2021 "
            "provided testimony to the National Fisheries Research and Development Institute "
            "and NGOs describing: daily physical beatings by the boatswain for slow work, "
            "sleeping in a 1.5m x 2m space shared with another worker in the engine room, "
            "wages of USD 200/month (contract stated USD 450), food consisting of rice and fish "
            "scraps, no shore leave during 8-month voyage, and seizure of passport and phone "
            "upon boarding. The vessel owner was investigated by the Ministry of Oceans and "
            "Fisheries but the case was settled privately."
        ),
        "source": "Advocates for Public Interest Law / Indonesian Embassy Seoul",
    },

    # ── Nepal ─────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Nepali EPS Workers — Manufacturing Sector and Community Support",
        "summary": (
            "Nepal sends approximately 8,000-10,000 workers annually to Korea under EPS, "
            "primarily for manufacturing. Nepal's Department of Foreign Employment (DoFE) "
            "administers recruitment. Official costs are capped at approximately NPR 80,000 "
            "(~USD 600), but actual costs including EPS-TOPIK preparation average NPR 150,000-"
            "250,000. Nepali communities in Ansan, Dongducheon, and Gimpo provide informal "
            "support networks. The Non-Resident Nepali Association Korea handles approximately "
            "500 labour complaints annually from both documented and undocumented Nepali workers."
        ),
        "source": "Nepal DoFE / Non-Resident Nepali Association Korea / IOM Nepal",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Nepali Worker Death on Livestock Farm — Manure Pit Drowning (2020)",
        "summary": (
            "A Nepali EPS worker drowned in a manure collection pit on a pig farm in "
            "Chungcheongnam-do in 2020. The pit lacked safety covers or guardrails. The worker "
            "was performing routine cleaning and was overcome by hydrogen sulfide gas before "
            "falling in. Investigation revealed: no gas detection equipment on the farm, no "
            "safety training on manure pit hazards provided in Nepali or English, and the worker "
            "was working alone (violating KOSHA guidelines for confined space entry). The employer "
            "was fined KRW 15 million and the worker's family received COMWEL survivor benefits "
            "of KRW 90 million after 8 months of processing."
        ),
        "source": "KOSHA / Chungnam Police / Nepal Embassy Seoul",
    },

    # ── Thailand ──────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Thai EPS Workers — Agricultural Sector Dominance",
        "summary": (
            "Thailand sends approximately 5,000-7,000 workers annually under EPS, with a high "
            "concentration in agriculture and livestock (estimated 45% of Thai EPS workers). "
            "Thailand's Department of Employment administers recruitment with relatively low "
            "unofficial costs (USD 500-1,500). Thai workers are concentrated in the southern "
            "agricultural provinces of Chungcheongnam-do, Jeollanam-do, and Jeollabuk-do. "
            "Language barriers are particularly severe for Thai workers as Korean-Thai "
            "interpretation services are scarce outside Seoul. Thai community organisations "
            "report that agricultural employers prefer Thai workers due to perceived diligence "
            "in hot conditions."
        ),
        "source": "Thailand Department of Employment / Thai Workers' Association in Korea",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Thai Agricultural Workers — Collective Walkout in Haenam (2021)",
        "summary": (
            "Eight Thai EPS workers collectively left a large-scale greenhouse complex in "
            "Haenam-gun in 2021 after enduring: 16-hour workdays during pepper harvest season "
            "with no overtime premium, employer-imposed 10 PM curfew in container housing, "
            "confiscation of motorbikes (their only transport in rural area), and verbal abuse "
            "including racial slurs. The workers sought assistance from the Gwangju Migrant "
            "Worker Center and filed a collective complaint. All eight were granted workplace "
            "changes without employer consent under the 'abuse' exception after the Labour "
            "Office investigation confirmed violations. The employer was issued corrective orders."
        ),
        "source": "Gwangju Migrant Worker Center / Jeollanam-do Labour Office",
    },

    # ── Myanmar ───────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Myanmar EPS Workers — Post-Coup Overstay and Vulnerability",
        "summary": (
            "Following Myanmar's military coup in February 2021, approximately 10,000-15,000 "
            "Myanmar EPS workers in Korea faced a dilemma: returning to a country in civil "
            "conflict or overstaying. Korea initially granted temporary visa extensions but "
            "later resumed enforcement against overstayers. Myanmar workers who lost documented "
            "status became highly vulnerable to exploitation, accepting below-minimum wages "
            "and dangerous conditions. The Myanmar community in Korea (estimated 30,000-40,000 "
            "including undocumented) reported increased wage theft as employers exploited "
            "workers' reluctance to engage with authorities."
        ),
        "source": "Myanmar Embassy Seoul / JCMK / IOM Korea",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Myanmar Worker Workplace Injury — Denied Medical Care (2022)",
        "summary": (
            "A Myanmar EPS worker in a Gimpo auto-parts factory suffered a crushed hand in a "
            "stamping press in 2022. The employer initially refused to call an ambulance, "
            "instead driving the worker to a small clinic that was not equipped for the injury. "
            "The worker lost two fingers and partial function of a third. The employer then "
            "pressured the worker to sign a document (in Korean) waiving further claims in "
            "exchange for KRW 5 million. A legal aid attorney intervened and filed an industrial "
            "accident claim. The worker eventually received KRW 65 million in disability "
            "benefits and medical cost coverage through COMWEL."
        ),
        "source": "Korea Legal Aid Corporation / COMWEL / Gimpo Migrant Worker Center",
    },

    # ── Bangladesh ────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Bangladeshi EPS Workers — Recurring Quota Suspension and Vulnerability",
        "summary": (
            "Bangladesh's EPS quota has been suspended multiple times (2006-2008, 2012) due to "
            "high overstay rates exceeding 50%. The Bureau of Manpower, Employment and Training "
            "(BMET) administers recruitment. Bangladeshi workers report among the highest "
            "unofficial migration costs (USD 3,000-7,000), driven by private intermediaries "
            "charging for EPS-TOPIK preparation and document processing despite the government-to-"
            "government structure. High migration costs create intense debt pressure, leading "
            "workers to accept exploitative conditions and overstay to repay debts rather than "
            "return home with insufficient savings."
        ),
        "source": "Bangladesh BMET / IOM Bangladesh / Korea HRD Service",
    },

    # ── Philippines ───────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Filipino EPS Workers — Strongest Sending Country Protections",
        "summary": (
            "The Philippines has the most robust worker protection infrastructure among EPS "
            "sending countries: the Philippine Overseas Labor Office (POLO) in Seoul provides "
            "legal assistance, the Overseas Workers Welfare Administration (OWWA) maintains "
            "emergency funds, and the Department of Migrant Workers (DMW) conducts pre-departure "
            "orientation covering Korean labour law. Filipino EPS workers report the lowest "
            "unofficial costs (~USD 1,000-1,500) and highest complaint-filing rates. However, "
            "Filipino workers still face exploitation particularly in fishing and agriculture "
            "where POLO's reach is limited."
        ),
        "source": "POLO Seoul / OWWA / Department of Migrant Workers Philippines",
    },

    # ── Mongolia ──────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Mongolian EPS Workers — Construction and Manufacturing Challenges",
        "summary": (
            "Mongolia sends approximately 3,000-5,000 workers annually under EPS, primarily "
            "for manufacturing and construction. The Mongolian Labour and Social Welfare Service "
            "Agency manages recruitment. Mongolian workers benefit from cultural and linguistic "
            "proximity to Korean (Altaic language family) but face specific challenges: "
            "construction sector subcontracting exploitation, high alcohol-related incidents "
            "(employers cite this as cause for dismissal), and difficulty accessing the Mongolian "
            "Embassy in Seoul from rural worksites. The Mongolian community in Dongducheon and "
            "Ansan provides informal support networks."
        ),
        "source": "Mongolian Embassy Seoul / Mongolia Labour and Social Welfare Service Agency",
    },

    # ── Uzbekistan ────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Uzbek EPS Workers — Rapid Growth and Integration Challenges",
        "summary": (
            "Uzbekistan has become one of the largest EPS sending countries, with approximately "
            "8,000-12,000 workers entering annually. The Agency for External Labour Migration "
            "under Uzbekistan's Ministry of Employment administers recruitment. Uzbek workers "
            "are concentrated in manufacturing, particularly in the Seoul-Gyeonggi industrial "
            "belt. Challenges include: limited Korean-Uzbek interpretation services, cultural "
            "adjustment issues (many workers are from rural areas with no industrial experience), "
            "and reports of Uzbek sub-agents charging unofficial fees of USD 2,000-4,000 despite "
            "government controls. The Uzbek community in Ansan has grown significantly since 2015."
        ),
        "source": "Uzbekistan Agency for External Labour Migration / Korea HRD Service",
    },

    # ── Sri Lanka ─────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Sri Lankan EPS Workers — Post-Economic Crisis Vulnerability",
        "summary": (
            "Following Sri Lanka's 2022 economic crisis, demand for Korean EPS positions surged. "
            "The Sri Lanka Bureau of Foreign Employment (SLBFE) reported a 300% increase in "
            "EPS-TOPIK registrations. Desperate economic conditions at home create pressure to "
            "accept any EPS placement regardless of sector or conditions. Sri Lankan workers "
            "have historically had lower overstay rates, maintaining good quota allocations. "
            "However, the post-crisis cohort faces higher debt levels from migration costs "
            "(families borrowing against property) and greater willingness to tolerate poor "
            "conditions to maintain remittance flows."
        ),
        "source": "Sri Lanka Bureau of Foreign Employment / IOM Sri Lanka / Korea HRD Service",
    },

    # ── Pakistan ──────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Pakistani EPS Workers — Construction Sector Focus and Wage Issues",
        "summary": (
            "Pakistan sends approximately 2,000-3,000 workers annually under EPS, with a "
            "significant concentration in construction. The Overseas Employment Corporation "
            "(OEC) administers recruitment. Pakistani workers report challenges including: "
            "construction sector subcontracting making employer accountability unclear, "
            "cultural dietary requirements not accommodated (halal food), limited Urdu "
            "interpretation services outside Seoul, and high unofficial costs (USD 2,000-4,000). "
            "The Pakistani Embassy in Seoul's labour wing handles approximately 200 complaints "
            "annually, primarily wage theft and workplace change denial."
        ),
        "source": "Pakistan OEC / Pakistani Embassy Seoul / Korea HRD Service",
    },

    # ── Timor-Leste ───────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Timorese EPS Workers — Smallest Contingent, Highest Vulnerability",
        "summary": (
            "Timor-Leste sends the fewest EPS workers (~500-1,000 annually), resulting in "
            "the smallest community support network. The Secretariat of State for Professional "
            "Training and Employment (SEFOPE) manages recruitment with limited capacity. "
            "Timorese workers face acute isolation: Tetum/Portuguese interpretation is virtually "
            "unavailable in Korea, the Timor-Leste Embassy has minimal labour attache capacity, "
            "and workers are dispersed across rural farms with no co-national community nearby. "
            "Pre-departure orientation is minimal. Reports indicate Timorese workers have among "
            "the lowest complaint-filing rates despite similar exploitation patterns."
        ),
        "source": "Timor-Leste SEFOPE / IOM Timor-Leste / Korea HRD Service",
    },

    # =====================================================================
    # ADDITIONAL CASES — Cross-Cutting Issues
    # =====================================================================
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Migrants' Trade Union (MTU) — Undocumented Workers' Right to Organise",
        "summary": (
            "The Seoul-Gyeonggi-Incheon Migrants' Trade Union (MTU), founded in 2005 by "
            "undocumented migrant workers, fought a decade-long legal battle for recognition. "
            "The Korean Supreme Court ruled in 2015 (2007Du4995) that undocumented workers have "
            "the constitutional right to form and join trade unions. Despite this ruling, the "
            "MTU's leadership has been repeatedly targeted by immigration enforcement — multiple "
            "MTU presidents were arrested and deported, which advocates characterise as "
            "retaliatory action aimed at suppressing migrant worker organising."
        ),
        "source": "Supreme Court of Korea 2007Du4995 / MTU / KCTU",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Worker Suicides — Under-Documented Crisis",
        "summary": (
            "NHRCK's 2022 review identified at least 47 migrant worker suicides in Korea "
            "between 2017 and 2021. Contributing factors documented in investigations include: "
            "workplace abuse with no escape mechanism (workplace change denial), isolation "
            "in rural areas, debt pressure from home, inability to communicate distress due to "
            "language barriers, and lack of access to mental health services in workers' "
            "languages. Only 3 of the 47 cases resulted in any legal action related to employer "
            "conduct. There is no dedicated mental health helpline for EPS workers."
        ),
        "source": "NHRCK Special Report 2022 / Korean Suicide Prevention Center",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Female EPS Workers — Sexual Harassment and Gender-Based Vulnerability",
        "summary": (
            "Female EPS workers (approximately 20% of total) face gender-specific exploitation: "
            "sexual harassment by employers or supervisors (particularly on isolated farms where "
            "the worker is the sole female), pregnancy-related dismissal (employers terminating "
            "contracts when workers become pregnant, despite legal protections), and lack of "
            "gender-sensitive complaint mechanisms. The Women Migrants Human Rights Center Korea "
            "receives approximately 300 sexual harassment and gender-based violence complaints "
            "annually from migrant women, with an estimated under-reporting rate of 80%."
        ),
        "source": "Women Migrants Human Rights Center Korea / NHRCK Gender Equality Division",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Worker Access to Healthcare — Systemic Barriers",
        "summary": (
            "While EPS workers are legally enrolled in National Health Insurance (NHI), "
            "practical barriers limit access: NHI premiums are deducted from wages but workers "
            "may not understand their coverage, hospitals in rural areas rarely have "
            "interpretation services, workers fear taking sick leave will anger employers, "
            "mental health services are virtually inaccessible in workers' languages, and "
            "undocumented workers (former EPS overstayers) lose NHI coverage entirely. A 2021 "
            "survey found that 55% of EPS workers needing medical care delayed or avoided "
            "treatment, with 'cannot take time off work' (60%) and 'language barrier at "
            "hospital' (45%) as primary reasons."
        ),
        "source": "Korea National Health Insurance Service / Migrant Health Association",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Alien Registration Card Confiscation — Ongoing Practice",
        "summary": (
            "Despite being illegal since the 2012 Act amendment, confiscation of EPS workers' "
            "Alien Registration Cards (ARC) by employers remains widespread. A 2023 survey by "
            "JCMK found that 22% of EPS workers reported their employer holding their ARC, "
            "down from 35% in 2018 but still prevalent. Employers claim they hold ARCs for "
            "'safekeeping' or to prevent workers from running away. Without their ARC, workers "
            "cannot access banking, healthcare, or file complaints with authorities. The 2021 "
            "amendment made ARC confiscation a criminal offence (up to 5 years imprisonment) "
            "but prosecution remains rare."
        ),
        "source": "JCMK Survey 2023 / NHRCK / Act on Foreign Workers' Employment",
    },
    {
        "type": "statistic",
        "jurisdiction": "KR",
        "title": "EPS Worker Wage Levels — Comparison with Korean Workers (2023)",
        "summary": (
            "In 2023, the average monthly wage for EPS workers was approximately KRW 2.2-2.5 "
            "million (including overtime), compared to the Korean average of KRW 3.5 million. "
            "Minimum wage for 2023 was KRW 9,620/hour (KRW 2,010,580/month for 209 hours). "
            "After employer deductions for housing (KRW 200,000-400,000) and meals (KRW "
            "100,000-200,000), actual take-home pay for agricultural workers can drop to KRW "
            "1.3-1.6 million. Workers typically remit 50-70% of earnings home, leaving minimal "
            "savings for personal expenses in Korea."
        ),
        "source": "MOEL Wage Statistics / Korea Labour Institute",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "COVID-19 Cluster Outbreaks in Migrant Worker Dormitories (2021)",
        "summary": (
            "Major COVID-19 outbreaks occurred in migrant worker dormitories in 2021, "
            "particularly in Dongducheon (manufacturing), Pocheon (agriculture), and Namyangju "
            "(logistics). Contributing factors: dormitories housing 6-10 workers per room made "
            "social distancing impossible, employers did not provide masks or sanitiser, "
            "workers feared testing because positive results meant quarantine without pay, and "
            "undocumented workers avoided testing entirely due to deportation risk. In Pocheon, "
            "an outbreak among agricultural workers was not reported for 2 weeks because the "
            "employer feared farm closure."
        ),
        "source": "Korea Disease Control and Prevention Agency / Gyeonggi-do Health Department",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Workers in Service Sector — Ethnic Restaurants and Hotels",
        "summary": (
            "A smaller proportion of EPS workers are employed in the service sector (food "
            "service, accommodation, social welfare). Service sector EPS workers face unique "
            "issues: unpredictable schedules, tip theft by employers, customer harassment, "
            "and employment in businesses operated by co-nationals who may exploit shared "
            "language and cultural ties to impose informal conditions outside the employment "
            "contract. Cases documented include Vietnamese EPS workers in Korean-Vietnamese "
            "restaurants working split shifts (11 AM-2 PM, 5 PM-midnight) that effectively "
            "prevent any personal time or community engagement."
        ),
        "source": "MOEL Service Sector Inspection / Migrant Worker Support Centers",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "2024 EPS Reform Proposals — National Assembly Debate",
        "summary": (
            "In 2024, the Korean National Assembly debated multiple EPS reform bills including: "
            "(1) eliminating the employer consent requirement for workplace changes entirely, "
            "(2) extending the job search period from 3 to 6 months, (3) removing the "
            "agricultural sector exemption from working hour limits, (4) mandating air-conditioned "
            "rest areas in greenhouses, (5) requiring bilingual employment contracts in the "
            "worker's language, and (6) creating a migrant worker ombudsman. As of late 2024, "
            "the bills remain in committee, with agricultural employer lobby groups opposing "
            "the working hour and housing provisions."
        ),
        "source": "National Assembly of Korea / MOEL / Korean media reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Migrant Worker Support Centres — Coverage Gap in Rural Areas",
        "summary": (
            "Korea operates approximately 45 publicly funded Migrant Worker Support Centres "
            "providing interpretation, legal counselling, and emergency shelter. However, 80% "
            "are located in urban areas (Seoul, Incheon, Gyeonggi), while migrant agricultural "
            "and fishing workers are concentrated in rural provinces. Chungcheongnam-do (major "
            "agricultural area) has only 3 centres for an estimated 15,000 EPS workers. Workers "
            "must travel 2-4 hours by bus to reach a centre, often impossible without employer "
            "cooperation for a day off. Mobile counselling services visit rural areas 1-2 times "
            "per month, insufficient for ongoing cases."
        ),
        "source": "MOEL / Korea Support Center for Foreign Workers",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Religious Organisations as De Facto Safety Net for EPS Workers",
        "summary": (
            "In the absence of adequate government services in rural areas, religious "
            "organisations (Buddhist temples, Catholic dioceses, Protestant churches, and "
            "mosques) serve as primary support networks for EPS workers. The Catholic Diocese "
            "of Daejeon operates migrant worker shelters and legal aid in Chungcheong provinces. "
            "Buddhist temples near agricultural areas provide weekend gathering spaces. Churches "
            "in Ansan and Gimpo offer Korean language classes and emergency food. While essential, "
            "this reliance on faith-based organisations means worker protection depends on "
            "volunteer capacity rather than systematic government provision."
        ),
        "source": "Catholic Bishops' Conference of Korea / Buddhist Social Welfare Foundation / NHRCK",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS-to-E-7 Skilled Worker Transition — Limited Pathway",
        "summary": (
            "Korea introduced a pathway for EPS workers to transition to E-7 (skilled worker) "
            "visas, allowing longer-term residence and family reunification. Eligibility requires: "
            "TOPIK Level 4 proficiency, employer sponsorship, designated occupation list, and "
            "minimum wage threshold. In practice, fewer than 2% of EPS workers successfully "
            "transition to E-7 — the Korean language requirement is extremely high, employers "
            "have little incentive to sponsor transitions (E-9 workers are cheaper due to "
            "departure guarantee), and the designated occupation list excludes agriculture and "
            "fishing. The pathway exists on paper but functions as a near-impossible benchmark."
        ),
        "source": "Korea Immigration Service / MOEL / Korea Labour Institute",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Debt Bondage Through EPS — Pre-Departure Loans in Sending Countries",
        "summary": (
            "Despite EPS cost caps, workers in several sending countries finance migration "
            "through high-interest loans. A 2022 IOM study found: Bangladeshi EPS workers "
            "borrowed at 25-60% annual interest, Cambodian workers at 18-36%, and Nepali "
            "workers at 15-24%. Loan repayment typically requires 6-12 months of Korean wages. "
            "During this period, workers are in effective debt bondage — they cannot leave "
            "Korea, cannot change to lower-paying jobs, and tolerate exploitation to maintain "
            "income. If deported before loan repayment, families face asset seizure by lenders."
        ),
        "source": "IOM Migration Costs Study 2022 / Mekong Migration Network / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Jeju Island Agricultural Workers — Special Vulnerability Context",
        "summary": (
            "Jeju Island's tangerine, green tea, and vegetable farms employ approximately "
            "3,000 EPS workers. Jeju's island geography creates additional vulnerability: "
            "limited migrant support infrastructure (1 support centre for the entire island), "
            "higher cost of living than mainland agricultural areas, and inability to physically "
            "leave the island for assistance without employer's cooperation for time off. "
            "Workers report that Jeju employers are aware of the geographic captivity effect "
            "and use it to discourage complaints. A 2022 NHRCK investigation of Jeju farms "
            "found violation rates comparable to mainland agricultural areas."
        ),
        "source": "NHRCK Jeju Investigation 2022 / Jeju Migrant Worker Center",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Return and Reintegration — Post-EPS Challenges in Home Countries",
        "summary": (
            "Returning EPS workers face reintegration challenges documented by IOM: physical "
            "injuries or occupational diseases acquired in Korea (often untreated), mental "
            "health impacts from years of isolation and exploitation, difficulty readjusting "
            "to home country wages after earning Korean wages, family tensions after years of "
            "separation, and loss of social networks. Former EPS workers who return with "
            "injuries report difficulty claiming compensation from Korea after departure. "
            "Some sending countries (Philippines, Nepal) have reintegration programmes, but "
            "most do not systematically track returned EPS worker welfare."
        ),
        "source": "IOM Return and Reintegration Studies / Sending Country Labour Ministries",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Hwaseong-si Industrial District — EPS Worker Exploitation Cluster",
        "summary": (
            "Hwaseong-si in Gyeonggi Province hosts a major industrial complex with significant "
            "EPS worker concentration in manufacturing and food processing. The Hwaseong Migrant "
            "Worker Center documented recurring patterns between 2019-2023: employers using "
            "CCTV to monitor dormitories, wage calculation disputes (employers using different "
            "hourly rates than contracted), forced purchase of meals from employer-designated "
            "vendors at inflated prices, and mandatory 'voluntary' overtime. In 2022, 15 EPS "
            "workers from three factories filed a joint complaint about coordinated wage "
            "suppression among neighbouring factory owners."
        ),
        "source": "Hwaseong Migrant Worker Center / Gyeonggi-do Labour Office",
    },
    {
        "type": "statistic",
        "jurisdiction": "KR",
        "title": "EPS Worker Industrial Accident Statistics — Annual Data (2022)",
        "summary": (
            "In 2022, COMWEL recorded 2,847 approved industrial accident claims for E-9 visa "
            "holders: 34 fatalities, 412 permanent disability cases, and 2,401 temporary "
            "disability cases. The fatality rate per 10,000 EPS workers (1.2) was approximately "
            "double the rate for Korean workers (0.6) in the same sectors. Agriculture/livestock "
            "had the highest fatality rate (3.1 per 10,000), followed by fishing (2.8), "
            "construction (2.2), and manufacturing (0.8). These figures are widely believed to "
            "undercount actual incidents by a factor of 3-5x due to under-reporting."
        ),
        "source": "COMWEL Industrial Accident Statistics 2022 / Korea Labour Institute",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Pre-Departure Orientation — Quality Varies by Sending Country",
        "summary": (
            "All EPS workers receive pre-departure orientation (PDO) in their home countries. "
            "Quality varies significantly: the Philippines provides 3 weeks covering Korean "
            "labour law, complaint mechanisms, and cultural orientation; Vietnam provides 2 "
            "weeks with Korean language focus; Cambodia provides 1-2 weeks with basic cultural "
            "content. A 2021 IOM evaluation found that only 35% of workers felt their PDO "
            "adequately prepared them for Korean workplace conditions, 20% understood their "
            "rights to change workplaces, and fewer than 10% knew the MOEL complaint hotline "
            "number upon arrival."
        ),
        "source": "IOM Pre-Departure Orientation Evaluation 2021 / Korea HRD Service",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Broker Networks Persist Despite Government-to-Government Model",
        "summary": (
            "Despite EPS eliminating formal private broker involvement, informal broker networks "
            "persist in several sending countries. Documented patterns: 'consultants' in Cambodia "
            "and Vietnam charge USD 1,000-3,000 for EPS-TOPIK preparation and 'guaranteed' job "
            "matching; 'agents' in Bangladesh and Nepal charge USD 2,000-5,000 for document "
            "preparation and connections to sending agency officials; and some sending agency "
            "officials themselves accept payments for priority processing. Korea HRD Service "
            "has limited ability to monitor recruitment practices within sovereign sending "
            "countries."
        ),
        "source": "ILO / Transparency International / Sending Country Investigative Media",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Workers and Freedom of Association — Right to Join Korean Unions",
        "summary": (
            "The 2015 Supreme Court ruling confirming undocumented workers' right to unionise "
            "implicitly extends to all EPS workers. However, practical barriers prevent "
            "unionisation: employer retaliation (contract non-renewal), workplace change denial "
            "for union members, union meetings conducted in Korean, geographic dispersal of "
            "agricultural/fishing workers, and the short-term (4-5 year) nature of EPS permits. "
            "KCTU's migrant division has approximately 2,000 EPS worker members (less than 1% "
            "of the EPS workforce). The MTU remains the primary voice for undocumented workers "
            "despite continued harassment of its leadership."
        ),
        "source": "KCTU / MTU / ILO Committee on Freedom of Association",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Racial Discrimination Against EPS Workers — NHRCK Cases",
        "summary": (
            "The NHRCK handles approximately 150-200 racial discrimination complaints from "
            "migrant workers annually. Documented patterns: employers using racial slurs "
            "('negro' for Southeast Asian workers), separate dining facilities for migrant and "
            "Korean workers, exclusion from company events, derogatory treatment by Korean "
            "co-workers, and public establishments refusing service. A 2020 NHRCK survey found "
            "that 68% of EPS workers experienced racial discrimination, with Cambodian (78%), "
            "Nepali (74%), and Thai (71%) workers reporting the highest rates. The NHRCK has "
            "issued multiple recommendations to MOEL for mandatory anti-discrimination training."
        ),
        "source": "NHRCK Annual Discrimination Report / Korea Human Rights Foundation",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Smart Factory Monitoring — Digital Surveillance of EPS Workers",
        "summary": (
            "The Korean government's 'Smart Factory' initiative to modernise SMEs has led to "
            "increased digital surveillance of EPS workers in manufacturing. Documented practices: "
            "CCTV in production areas tracking individual productivity, GPS tracking via "
            "employer-provided phones, biometric time clocks recording bathroom breaks, and "
            "production-linked wage systems where falling below targets reduces pay. While "
            "technology can improve safety, advocates note that surveillance intensity on EPS "
            "workers exceeds that applied to Korean employees in the same workplaces, reflecting "
            "a discriminatory control mindset."
        ),
        "source": "Korea Institute for Industrial Economics and Trade / KCTU Digital Rights Division",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Worker Children — Stateless and Undocumented Minors",
        "summary": (
            "Children born to EPS workers in Korea face legal limbo: they do not automatically "
            "receive Korean citizenship (jus sanguinis system) and may not be registered in the "
            "parent's home country if the parent is undocumented or unable to visit the embassy. "
            "An estimated 5,000-10,000 undocumented migrant children live in Korea, many born "
            "to former EPS parents. These children face barriers to: school enrolment (though "
            "legally permitted, schools may refuse), healthcare access, and eventual legal "
            "status. The NHRCK has recommended a pathway to legal status for long-term "
            "undocumented children."
        ),
        "source": "NHRCK / Save the Children Korea / JCMK",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "2023 Agricultural Worker Housing Standards — New Enforcement Measures",
        "summary": (
            "In response to continued worker deaths in substandard housing, MOEL issued "
            "strengthened guidelines in 2023 requiring: minimum 3.3 sqm per person, heating "
            "and cooling systems, separate kitchen and sanitation facilities, fire safety "
            "equipment, and prohibition of housing in agricultural structures (greenhouses, "
            "barns, sheds). Local governments must inspect worker housing before EPS worker "
            "placement. Non-compliant employers face EPS allocation suspension. However, "
            "implementation has been slow — a 2024 spot check found that 30% of newly inspected "
            "housing still failed to meet the standards."
        ),
        "source": "MOEL Housing Standards Guidelines 2023 / KOSHA",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "ILO CEACR Observations on Korea — Recurring Concerns (2023)",
        "summary": (
            "The ILO Committee of Experts on the Application of Conventions and Recommendations "
            "(CEACR) has issued repeated observations to Korea regarding EPS workers under the "
            "Forced Labour Convention (C029) and the Discrimination Convention (C111). Key "
            "concerns: (1) workplace change restrictions creating conditions analogous to forced "
            "labour indicators; (2) agricultural sector working hour exemption facilitating "
            "excessive overtime; (3) inadequate enforcement of labour standards for migrant "
            "workers; and (4) de facto discrimination in access to justice. Korea has responded "
            "with incremental reforms but has not addressed the structural issues."
        ),
        "source": "ILO CEACR Observations on Korea 2023 / ILO NORMLEX Database",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "US TIP Report Assessment of South Korea — Tier 1 with Concerns",
        "summary": (
            "The US Trafficking in Persons (TIP) Report has maintained South Korea at Tier 1 "
            "(full compliance) but with documented concerns about EPS worker exploitation. "
            "The 2023 TIP Report noted: 'Some migrant workers employed under the Employment "
            "Permit System experienced conditions indicative of forced labour, including "
            "excessive working hours, restriction of movement, and document confiscation.' "
            "Recommendations included: strengthening workplace change provisions, increasing "
            "labour inspections of agricultural and fishing workplaces, and providing "
            "multilingual victim identification training to labour inspectors."
        ),
        "source": "US Department of State Trafficking in Persons Report 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Amnesty International 'Bitter Harvest' — Comprehensive Korea Agricultural Exposé",
        "summary": (
            "Amnesty International's 2014 report 'Bitter Harvest: Exploitation of Migrant "
            "Workers in South Korea's Agricultural Sector' documented extensive rights violations "
            "based on interviews with 150 EPS agricultural workers across 8 provinces. Findings: "
            "85% worked excessive hours without overtime, 72% experienced wage deductions below "
            "legal limits, 60% lived in substandard housing, 48% experienced verbal or physical "
            "abuse, 40% had documents confiscated, and 100% reported fear of employer retaliation "
            "for complaints. The report compared EPS agricultural conditions to ILO forced "
            "labour indicators, finding multiple indicators present."
        ),
        "source": "Amnesty International 'Bitter Harvest' (ASA 25/004/2014)",
    },
    {
        "type": "statistic",
        "jurisdiction": "KR",
        "title": "EPS Workplace Change Statistics — Scale of Transfers (2022)",
        "summary": (
            "In 2022, approximately 38,000 EPS workers applied for workplace changes. Of these: "
            "65% were processed successfully within 3 months, 20% were delayed beyond 3 months "
            "(risking visa status), 10% resulted in the worker becoming undocumented due to "
            "failure to find a new employer, and 5% were denied. The most common reasons for "
            "workplace change: employer bankruptcy (28%), wage non-payment (22%), workplace "
            "closure (15%), employment condition violations (18%), abuse/harassment (10%), and "
            "other (7%). Agricultural sector workers had the lowest successful transfer rate "
            "(55%) due to limited alternative employers in rural areas."
        ),
        "source": "HRD Korea / MOEL Labour Market Statistics",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Gimpo Logistics District — EPS Workers in Warehouse Operations",
        "summary": (
            "Gimpo's logistics zone near Incheon Airport employs an increasing number of EPS "
            "workers in warehouse operations, packaging, and cold storage. Workers report: "
            "temperatures in cold storage facilities reaching -25C with inadequate thermal "
            "clothing, piece-rate pay systems that effectively reduce hourly rates below minimum "
            "wage, mandatory overtime during peak shipping seasons (November-January), and "
            "injuries from repetitive heavy lifting without ergonomic equipment. A 2023 MOEL "
            "inspection of Gimpo logistics facilities found 55% violated at least one "
            "occupational safety standard for temperature exposure."
        ),
        "source": "MOEL Gimpo Inspection Report 2023 / Gimpo Labour Office",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS 20th Anniversary Assessment — Progress and Persistent Gaps (2024)",
        "summary": (
            "As EPS marked its 20th anniversary in 2024, comprehensive assessments by the Korea "
            "Labour Institute, ILO, and civil society groups identified both progress and "
            "persistent gaps. Progress: eliminated most private broker fees, provided equal "
            "labour law coverage (in theory), built government-to-government infrastructure. "
            "Persistent gaps: workplace change restrictions still create employer power asymmetry, "
            "agricultural sector exemptions from working hours still enable extreme overwork, "
            "housing standards still inadequately enforced, and enforcement penalties remain "
            "too low to deter exploitation. The assessment concluded that EPS is a strong design "
            "weakened by implementation gaps."
        ),
        "source": "Korea Labour Institute / ILO / JCMK / NHRCK",
    },

    # =====================================================================
    # ADDITIONAL CASES — Prosecution, Detention, and Systemic Issues
    # =====================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Cheonan Poultry Farm Prosecution — Worker Confinement and Wage Theft (2020)",
        "court": "Daejeon District Court, Cheonan Branch",
        "year": 2020,
        "summary": (
            "A poultry farm owner in Cheonan was convicted of confining a Vietnamese EPS "
            "worker on the farm for 14 months by taking the worker's alien registration card "
            "and mobile phone, making travel to town impossible. The worker was paid KRW 800,000 "
            "monthly (approximately 40% of minimum wage) and housed in a shed attached to the "
            "chicken coop. The case came to light when the worker managed to contact a "
            "Vietnamese community member via a neighbour's phone. The court sentenced the owner "
            "to 18 months imprisonment (suspended) and ordered back wages of KRW 14 million."
        ),
        "source": "Daejeon District Court, Cheonan Branch / NHRCK",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "KR",
        "title": "Seosan Dairy Farm Prosecution — Physical Assault and Labour Violations (2021)",
        "court": "Daejeon District Court, Seosan Branch",
        "year": 2021,
        "summary": (
            "A dairy farm owner in Seosan-si was convicted of repeatedly striking a Nepali EPS "
            "worker with a shovel handle and kicking him when the worker failed to meet milking "
            "speed expectations. Medical evidence showed multiple healed fractures and scarring. "
            "The worker had endured 2 years of abuse, afraid to report because the employer "
            "was the sole source of workplace change consent. The employer was also found to "
            "have deducted KRW 500,000 monthly from wages for 'room and board' consisting of "
            "a mattress in the barn office and rice-only meals. Sentence: 2 years imprisonment "
            "(actual, not suspended) — one of the harshest for agricultural labour abuse."
        ),
        "source": "Daejeon District Court / Chungnam Migrant Worker Center",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Immigration Detention Conditions for Migrant Workers",
        "summary": (
            "Undocumented workers apprehended by Korea Immigration Service are held in "
            "immigration detention centres (Hwaseong, Cheongju, Yeosu). NHRCK inspections "
            "documented: overcrowding (20-30 detainees in rooms designed for 10), inadequate "
            "medical care (one doctor per 200+ detainees), no legal aid access for most "
            "detainees, indefinite detention with no maximum period (some detained for 12+ "
            "months), and detainees unable to communicate in Korean having no access to "
            "interpreters. Several suicides and attempted suicides in detention have been "
            "recorded. The NHRCK recommended a maximum detention period of 6 months."
        ),
        "source": "NHRCK Detention Center Inspections / IOM Korea",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Chungju Apple Orchard — Seasonal Worker Exploitation (2022)",
        "summary": (
            "An investigation into apple orchards in Chungju-si revealed systematic exploitation "
            "of E-8 seasonal workers from Thailand and Cambodia: workers arrived expecting "
            "agricultural work but were assigned to nearby food processing facilities (violating "
            "visa terms), wages were paid to a team leader who distributed reduced amounts, "
            "and workers were housed 12-per-room in a disused warehouse. When workers complained "
            "to the local government office that had arranged their entry, they were told the "
            "contract was between them and the farm owner. The local government denied "
            "responsibility. MOEL intervened after media coverage."
        ),
        "source": "MOEL / Chungcheongbuk-do Labour Office / Korean media reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Dongducheon Manufacturing Zone — Wage Theft Through Timecard Manipulation",
        "summary": (
            "A pattern of timecard manipulation affecting EPS workers was documented in "
            "Dongducheon's manufacturing zone in 2023. Multiple factories used electronic time "
            "clocks that could be retroactively adjusted by employers. Workers clocking 12-hour "
            "shifts would find their records showed 8 hours. When workers protested, employers "
            "pointed to the electronic records as proof. A Mongolian EPS worker who secretly "
            "photographed the wall clock alongside his timecard for 3 months provided evidence "
            "that led to a successful Labour Office complaint and back-wage orders against "
            "3 factories totalling KRW 120 million for 28 workers."
        ),
        "source": "Dongducheon Migrant Worker Center / Uijeongbu Labour Office",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Winter Deaths in Container Housing — Carbon Monoxide Poisoning",
        "summary": (
            "In addition to hypothermia, carbon monoxide poisoning from improvised heating in "
            "container housing has killed migrant workers. A 2019 case in Yeoju-si killed two "
            "Indonesian EPS workers who used a charcoal briquette heater in their sealed "
            "container unit. A 2021 case in Icheon-si hospitalised three Cambodian workers from "
            "carbon monoxide produced by a gas heater in an unventilated container. Employers "
            "had not provided safe heating systems and the containers lacked ventilation. KOSHA "
            "issued advisories on container heating safety after these incidents, but compliance "
            "monitoring in rural agricultural areas remains weak."
        ),
        "source": "KOSHA / National Fire Agency / Gyeonggi-do Fire Department",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Geoje Shipyard — EPS Workers in Heavy Industry Subcontracting",
        "summary": (
            "EPS workers employed by subcontractors at major shipyards in Geoje and Tongyeong "
            "face specific risks: welding in confined spaces without adequate ventilation, "
            "working at extreme heights on vessel hulls, exposure to asbestos during ship "
            "repair, and heat stress in engine compartments. A 2022 incident at a Geoje "
            "subcontractor saw a Vietnamese EPS welder hospitalised with manganese poisoning "
            "from welding fumes in an enclosed space. The prime contractor denied responsibility, "
            "the subcontractor had no safety officer, and the worker's compensation claim was "
            "initially rejected before COMWEL reversed the decision on appeal."
        ),
        "source": "COMWEL / Gyeongsangnam-do Labour Office / Korean Metalworkers' Union",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KR",
        "title": "Serious Accidents Punishment Act (2022) — Impact on Migrant Worker Safety",
        "summary": (
            "Korea's Serious Accidents Punishment Act (effective January 2022 for firms with "
            "50+ employees, January 2024 for smaller firms) imposes criminal liability on "
            "business owners and CEOs for worker deaths caused by safety failures. Maximum "
            "penalty: 1 year+ imprisonment and KRW 1 billion fine. While a landmark law, its "
            "impact on EPS worker safety is limited: most EPS employers are small firms (under "
            "30 employees) that were initially exempt, agricultural and fishing sectors have "
            "weaker application, and the law requires proving 'organisational' failures rather "
            "than individual negligence, making prosecution of small farm owners challenging."
        ),
        "source": "National Assembly of Korea / MOEL / Korea Labour Institute",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Yangju Pig Farm — Worker Confined and Assaulted for Three Years (2023)",
        "summary": (
            "One of Korea's most severe EPS exploitation cases came to light in 2023 when a "
            "Cambodian worker was rescued from a pig farm in Yangju-si after 3 years of "
            "confinement. The worker reported: being beaten with PVC pipes for perceived slow "
            "work, sleeping in the pig barn, eating leftover food, no days off for the entire "
            "period, wages of KRW 500,000/month (less than 25% of minimum wage), and being told "
            "he would be reported to immigration if he tried to leave (his visa had expired "
            "during the confinement). The farm owner was arrested and charged under the "
            "Trafficking in Persons Act — a rare use of trafficking charges in an EPS case."
        ),
        "source": "Gyeonggi Bukbu Police / NHRCK / Cambodian Embassy Seoul",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Migrant Worker Emergency Shelters — Capacity and Demand Mismatch",
        "summary": (
            "Korea operates 7 emergency shelters for migrant workers fleeing exploitation, "
            "with a total capacity of approximately 200 beds. In 2022, 3,500+ workers sought "
            "emergency shelter, meaning capacity could accommodate fewer than 6% of applicants. "
            "Workers turned away from shelters face homelessness, return to exploitative "
            "employers, or become undocumented. No shelter exists specifically for male "
            "agricultural workers (the largest exploited group). Existing shelters are urban-based "
            "and difficult for rural workers to reach. Shelter stays are typically limited to "
            "3 months, insufficient for complex legal cases."
        ),
        "source": "MOEL / Korea Support Center for Foreign Workers / NHRCK",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Laotian EPS Workers — Newest Programme Participants",
        "summary": (
            "Laos became the most recent EPS partner (MOU signed 2016, workers arriving from "
            "2017). As the newest and smallest contingent (~500-800 annually), Laotian workers "
            "face extreme isolation: virtually no Lao community in Korea, no Korean-Lao "
            "interpretation services, the Laotian Embassy has minimal consular capacity for "
            "labour issues, and pre-departure orientation is the shortest among all sending "
            "countries. Laotian workers are concentrated in agriculture and manufacturing in "
            "remote areas. No Lao-language support materials have been developed by MOEL. "
            "Complaint filing rates are effectively zero."
        ),
        "source": "Laos Ministry of Labour and Social Welfare / Korea HRD Service",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Kyrgyz EPS Workers — Central Asian Labour Migration to Korea",
        "summary": (
            "Kyrgyzstan signed its EPS MOU in 2011, sending 1,000-2,000 workers annually. "
            "The State Migration Service manages recruitment. Kyrgyz workers are predominantly "
            "employed in manufacturing in Gyeonggi Province. Specific challenges include: "
            "adaptation from predominantly pastoral/agricultural backgrounds to factory work, "
            "limited Russian-Korean or Kyrgyz-Korean interpretation, and cultural isolation "
            "(no established Kyrgyz community organisations). Kyrgyz workers report relying "
            "on Uzbek community networks due to linguistic proximity. The Kyrgyz Embassy in "
            "Seoul has one labour attache handling all worker issues."
        ),
        "source": "Kyrgyzstan State Migration Service / Korean HRD Service",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Food Processing Sector — EPS Workers in Kimchi and Seafood Factories",
        "summary": (
            "EPS workers in food processing (classified under manufacturing) face sector-specific "
            "hazards: repetitive knife injuries in seafood processing, chemical exposure from "
            "cleaning agents, cold-related injuries in refrigerated facilities, and skin "
            "conditions from prolonged contact with salt brine and marinades. A 2022 investigation "
            "of kimchi factories in Gwangju found that EPS workers performed the most physically "
            "demanding tasks (salt cabbage handling, heavy lifting) while Korean workers supervised. "
            "Workers reported salt burns on hands and arms because gloves provided were too thin "
            "and no protective arm coverings were issued."
        ),
        "source": "KOSHA / Gwangju Labour Office / Korea Food Safety Authority",
    },
    {
        "type": "statistic",
        "jurisdiction": "KR",
        "title": "EPS Overstay Rates by Sending Country (2023)",
        "summary": (
            "Korea HRD Service tracks overstay rates by sending country, using them to adjust "
            "quotas. As of 2023 (approximate rates): Bangladesh (38%), Vietnam (28%), Mongolia "
            "(22%), Nepal (20%), Indonesia (18%), Cambodia (16%), Thailand (15%), Myanmar (25% "
            "— elevated post-coup), Philippines (12%), Sri Lanka (10%), Uzbekistan (14%), "
            "Pakistan (20%), China (12%), Timor-Leste (18%), Kyrgyzstan (15%), Laos (12%). "
            "Countries exceeding 25% face quota reductions. However, overstay rates reflect "
            "workers' desperation to continue earning rather than a character flaw — countries "
            "with higher unofficial costs and lower home wages have higher overstay rates."
        ),
        "source": "Korea HRD Service / Korea Immigration Service Annual Statistics",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Workers' Remittance Dependency — Pressure to Tolerate Exploitation",
        "summary": (
            "IOM surveys consistently find that EPS workers' families in home countries are "
            "heavily dependent on remittances: 80% of workers send money monthly, average "
            "remittance is 50-70% of after-deduction wages (KRW 800,000-1,200,000/month), and "
            "remittances typically support 4-8 family members. This dependency creates extreme "
            "pressure to maintain employment at any cost. Workers who lose their jobs (through "
            "complaint-filing, workplace change, or deportation) immediately cut off the family "
            "income lifeline. This economic reality is the single greatest barrier to EPS "
            "workers reporting exploitation — the consequences of speaking up extend beyond "
            "the worker to entire families."
        ),
        "source": "IOM / World Bank Remittance Data / Sending Country Central Banks",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Chungnam Ginseng Farms — Heat and Chemical Double Exposure",
        "summary": (
            "Ginseng cultivation in Chungcheongnam-do requires intensive manual labour under "
            "shade structures that trap heat similar to greenhouses. EPS workers on ginseng "
            "farms face a double exposure: extreme heat (shade structures reach 45-50C in "
            "summer) and heavy pesticide/herbicide use (ginseng is highly susceptible to "
            "disease). A 2021 survey documented that 80% of ginseng farm EPS workers had no "
            "pesticide safety training, 70% applied chemicals without respiratory protection, "
            "and 60% reported chronic headaches and skin irritation they attributed to chemical "
            "exposure. No occupational health study of ginseng farm migrant workers has been "
            "conducted by KOSHA."
        ),
        "source": "Chungnam Migrant Worker Center / Rural Development Administration",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "EPS Faithful Worker Re-Entry — Second Term Vulnerability",
        "summary": (
            "Workers returning for a second EPS term under the 'faithful worker' programme "
            "face specific vulnerabilities: they may be assigned to a different employer than "
            "their first term, they arrive with higher expectations from families (who assume "
            "the worker is experienced), they are older (typically 30-45) and more susceptible "
            "to physical strain, and their re-entry is contingent on the original employer's "
            "recommendation — creating pressure to maintain good relations even with exploitative "
            "employers during the first term. A 2021 survey found that 30% of second-term "
            "workers reported worse conditions than their first term, with many placed in "
            "agricultural or fishing positions despite first-term manufacturing experience."
        ),
        "source": "Korea HRD Service / MOEL / Migrant Worker Support Centers",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Tongyeong Oyster Farms — Migrant Workers in Aquaculture",
        "summary": (
            "The Tongyeong and Geoje oyster farming region employs approximately 2,000 EPS "
            "workers in aquaculture operations. Working conditions include: standing in cold "
            "seawater for 10-12 hours during harvest season (November-March), repetitive "
            "shucking injuries (cuts, tendonitis), exposure to marine bacteria causing skin "
            "infections, and isolation on small islands where oyster beds are located. Workers "
            "on island-based operations may have no access to shore for weeks during peak season. "
            "In 2022, a Vietnamese worker died from septicaemia caused by an infected hand "
            "wound sustained during shucking — medical care had been delayed 5 days because "
            "the employer considered it a minor cut."
        ),
        "source": "Gyeongsangnam-do Fisheries Association / KOSHA / Tongyeong Labour Office",
    },
]
