"""Qatar World Cup and GCC construction — worker deaths, kafala exploitation, and reform efforts."""

QATAR_WORLDCUP_GCC_FACTS: list[dict] = [
    # ========================================================================
    # 1. Qatar 2022 World Cup — Stadium Worker Deaths & Conditions
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Worker Deaths During World Cup Preparations (2010-2020)",
        "metric": "worker_deaths",
        "value": "6,500+",
        "summary": "The Guardian investigation using embassy data from India, Nepal, Pakistan, Bangladesh, and Sri Lanka documented 6,500+ migrant worker deaths in Qatar between 2010 and 2020 during the World Cup infrastructure build-out. Qatar government disputes the figure, citing only 37 'non-work-related' deaths on stadium sites. Many death certificates list 'natural causes' or 'cardiac arrest' without autopsy.",
        "source": "The Guardian / Qatar government statistics",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Nepali Worker Deaths (2010-2020)",
        "metric": "nepali_worker_deaths",
        "value": "1,641",
        "summary": "Nepali Embassy in Doha recorded 1,641 Nepali worker deaths in Qatar between 2010 and 2020. Nepal is one of the top labour-sending countries for Qatar construction. Leading listed causes: cardiac arrest (unexplained), workplace falls, road accidents. Nepali government demanded improved death investigation procedures but lacked diplomatic leverage.",
        "source": "Nepali Embassy Doha / The Guardian",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Indian Worker Deaths (2010-2020)",
        "metric": "indian_worker_deaths",
        "value": "2,711",
        "summary": "Indian Embassy in Doha reported 2,711 Indian worker deaths in Qatar over the decade preceding the 2022 World Cup. India's large construction workforce in Qatar faced heat exposure, overwork, and inadequate medical access. Indian government called for improved health screening and workplace safety standards.",
        "source": "Indian Embassy Doha / The Guardian",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Bangladeshi Worker Deaths (2010-2020)",
        "metric": "bangladeshi_worker_deaths",
        "value": "1,018",
        "summary": "Bangladesh Embassy in Doha recorded 1,018 Bangladeshi worker deaths in Qatar between 2010 and 2020. Bangladeshi workers concentrated in construction, cleaning, and infrastructure sectors. Death certificates overwhelmingly cited 'natural causes' even for workers in their 20s and 30s.",
        "source": "Bangladesh Embassy Doha / The Guardian",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Pakistani Worker Deaths (2010-2020)",
        "metric": "pakistani_worker_deaths",
        "value": "824",
        "summary": "Pakistan Embassy documented 824 Pakistani worker deaths in Qatar in the decade before the World Cup. Pakistani workers were employed in construction, hospitality, and transport infrastructure. Families in Pakistan reported difficulty obtaining death certificates and repatriation of remains.",
        "source": "Pakistan Embassy Doha / The Guardian",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Sri Lankan Worker Deaths (2010-2020)",
        "metric": "sri_lankan_worker_deaths",
        "value": "557",
        "summary": "Sri Lankan Embassy in Doha recorded 557 Sri Lankan worker deaths in Qatar between 2010 and 2020. Workers were primarily in construction and facility management. Sri Lankan government lobbied for improved working conditions and mandatory employer-provided life insurance.",
        "source": "Sri Lankan Embassy Doha / The Guardian",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Lusail Stadium — Worker Exploitation During Construction",
        "summary": "Lusail Stadium (80,000 capacity, hosted World Cup final) construction employed approximately 18,000 workers at peak. Amnesty International documented wage theft affecting hundreds of workers employed by subcontractors. Workers reported 10-12 hour shifts in summer heat, 3-month wage delays, and overcrowded camp housing. Supreme Committee acknowledged 'isolated cases' and required main contractor HBK Contracting to remediate.",
        "source": "Amnesty International / Supreme Committee for Delivery & Legacy",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Al Bayt Stadium — Worker Death and Conditions Report",
        "summary": "Al Bayt Stadium in Al Khor (60,000 capacity) saw at least one confirmed worker death during construction. Workers hired through multiple layers of subcontractors reported inconsistent pay schedules and inadequate safety equipment. ILO inspectors found violations of rest-period requirements during summer months. Stadium completed in 2021 for the FIFA Arab Cup.",
        "source": "ILO Qatar Office / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Al Janoub Stadium — Labour Rights Monitoring",
        "summary": "Al Janoub Stadium in Al Wakrah (designed by Zaha Hadid Architects, 40,000 capacity) was the first newly built World Cup venue completed (2019). Supreme Committee's Workers' Welfare Standards were piloted here. Despite enhanced monitoring, workers reported passport confiscation by sub-subcontractors and delayed repatriation flights after contract completion.",
        "source": "Supreme Committee for Delivery & Legacy / BWI",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Education City Stadium — Subcontractor Wage Theft",
        "summary": "Education City Stadium (40,000 capacity, completed 2020) construction involved multiple tiers of subcontracting. Workers employed by lower-tier subcontractors reported going 2-5 months without pay while main contractors were paid on time. Supreme Committee's Workers' Welfare team intervened in several cases but acknowledged systemic challenges with subcontractor compliance monitoring.",
        "source": "Amnesty International / Supreme Committee Audit Reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Ahmad Bin Ali Stadium — Worker Camp Conditions",
        "summary": "Workers building Ahmad Bin Ali Stadium in Al Rayyan (40,000 capacity) housed in Industrial Area labour camps. Rooms designed for 4 workers held 8-12. Shared bathroom facilities were inadequate. Temperature in non-air-conditioned camps exceeded 40 degrees Celsius in summer. Post-completion inspections found improved conditions on Supreme Committee-controlled sites but persistent issues in off-site worker housing.",
        "source": "HRW / Qatar Labour Inspectorate Reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Ras Abu Aboud (Stadium 974) — Modular Build Worker Conditions",
        "summary": "Stadium 974 (the modular, demountable stadium built from shipping containers) employed approximately 5,000 workers at peak. While marketed as innovative and sustainable, worker conditions mirrored other sites: long hours, heat exposure, and delayed wages among subcontractor employees. The stadium was dismantled after the World Cup as planned.",
        "source": "BWI / The Guardian",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Khalifa International Stadium — Renovation Worker Deaths",
        "summary": "Khalifa International Stadium renovation (expanded from 40,000 to 48,000 capacity) resulted in at least one confirmed worker death. The stadium, Qatar's oldest, underwent extensive renovation for the 2019 World Athletics Championships and 2022 World Cup. Workers reported inadequate fall protection during roof work at height.",
        "source": "ITUC / BWI",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar Supreme Committee — Official Worker Death Count on Stadium Sites",
        "metric": "official_stadium_deaths",
        "value": "3 work-related, 37 non-work-related",
        "summary": "The Supreme Committee for Delivery & Legacy reported only 3 work-related deaths and 37 'non-work-related' deaths among workers on its stadium projects. This narrow definition excludes deaths from heat stress classified as cardiac arrest, deaths on non-stadium World Cup infrastructure, and deaths of workers who returned home ill. Amnesty International and ITUC called the accounting misleading.",
        "source": "Supreme Committee for Delivery & Legacy / ITUC",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar World Cup Infrastructure — Non-Stadium Worker Deaths",
        "summary": "The majority of World Cup-related deaths occurred not on stadium sites but on roads, metro, hotels, and other infrastructure projects outside Supreme Committee oversight. Doha Metro (Red, Gold, Green Lines), Hamad International Airport expansion, Lusail City, and highway projects employed hundreds of thousands of workers without the welfare standards applied to stadium sites.",
        "source": "Amnesty International / ITUC / The Guardian",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Doha Metro Construction — Worker Conditions",
        "summary": "Doha Metro (3 lines, 37 stations) construction employed over 20,000 workers at peak. Main contractors included joint ventures with PORR, Salini-Impregilo, and Samsung. Workers reported long underground shifts with inadequate ventilation. At least 4 worker deaths confirmed during tunnelling operations. Contractor consortium established welfare committees but subcontractor workers had limited access.",
        "source": "BWI / Qatar Rail",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Lusail City — Mega-Development Worker Exploitation",
        "summary": "Lusail City, a planned city north of Doha built for 200,000 residents, employed over 40,000 construction workers at peak. Workers on residential, commercial, and entertainment district projects reported 3-7 month wage delays, passport confiscation, and threats of deportation for complaining. Multiple subcontractors went bankrupt, leaving workers stranded without pay or return flights.",
        "source": "Amnesty International / Migrant-Rights.org",
    },
    # ========================================================================
    # 2. The Guardian Investigation — 6,500 Deaths
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "The Guardian Investigation — Methodology for 6,500 Death Figure",
        "summary": "The Guardian compiled death toll by requesting official mortality data from embassies of India, Nepal, Pakistan, Bangladesh, and Sri Lanka in Doha. Data covered 2010-2020. The investigation noted deaths from other nationalities (Philippines, Kenya, Uganda) were excluded due to incomplete data, suggesting the true toll is higher. Qatar government challenged the methodology, stating most deaths were 'not work-related'.",
        "source": "The Guardian (February 2021)",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — 'Unexplained Deaths' and Lack of Autopsy",
        "summary": "Analysis of death certificates for migrant workers in Qatar found approximately 69 percent listed cause as 'acute cardiac failure' or 'natural causes' without further investigation. Autopsies are rarely performed. Lancet Planetary Health editorial (2019) stated this classification likely masks heat-related deaths. Workers' families receive minimal information about circumstances of death.",
        "source": "The Guardian / The Lancet Planetary Health",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Guardian Investigation — FIFA Response and Liability",
        "summary": "Following The Guardian's 6,500 deaths investigation, FIFA President Gianni Infantino stated death is 'a part of life' and that giving workers construction jobs was 'a form of dignity.' FIFA rejected calls for a USD 440 million compensation fund (equivalent to World Cup prize money) for workers' families. Human rights organizations condemned the response as callous and demanded accountability.",
        "source": "The Guardian / Amnesty International / FIFA press conference",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Death Certificate Practices — Cardiac Arrest as Default Cause",
        "summary": "Research by Vital Signs Partnership found that 'acute cardiac failure' was listed as cause of death for healthy young workers who died suddenly after outdoor work in extreme heat. Medical experts stated that heat stroke causes cardiac arrest, meaning the underlying cause was occupational heat exposure, not a pre-existing cardiac condition. Qatar introduced enhanced medical screening in 2021 but did not retroactively investigate previous deaths.",
        "source": "Vital Signs Partnership / British Journal of Sports Medicine",
    },
    # ========================================================================
    # 3. FIFA Responsibility and Human Rights Due Diligence
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "FIFA — Human Rights Due Diligence Failures",
        "summary": "The UN Guiding Principles on Business and Human Rights require companies to conduct human rights due diligence. FIFA awarded the 2022 World Cup to Qatar in 2010 without any human rights assessment. An internal FIFA evaluation in 2010 rated Qatar high risk for heat and labour rights but the bid was approved. John Ruggie's 2016 report recommended FIFA embed human rights in all tournament decisions.",
        "source": "UN Guiding Principles / Ruggie Report to FIFA (2016)",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "FIFA Profits vs Worker Compensation — The USD 440M Campaign",
        "summary": "Amnesty International led a campaign calling on FIFA to establish a USD 440 million compensation fund for World Cup workers — matching the total prize money for the tournament. FIFA earned USD 7.5 billion from the 2022 World Cup cycle. As of 2024, FIFA has not established such a fund. Amnesty estimated remediation costs at a minimum of USD 440M to cover unpaid wages, death compensation, and injury benefits.",
        "source": "Amnesty International / FIFA Financial Report 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Supreme Committee Workers' Welfare Standards — Scope Limitations",
        "summary": "The Supreme Committee for Delivery & Legacy established Workers' Welfare Standards in 2014 covering recruitment, accommodation, health, and safety for workers on its seven stadium projects. However, the standards applied only to an estimated 30,000 workers at peak — a fraction of the 1.5-2 million migrant workers in Qatar. Workers on hotels, roads, metro, and other World Cup infrastructure had no comparable protections.",
        "source": "Supreme Committee / ILO / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "FIFA Bidding Process — Corruption and Labour Oversight",
        "summary": "The 2010 bid process that awarded Qatar the 2022 World Cup was later investigated for corruption. US Department of Justice indictments implicated FIFA officials in bribery. The corruption investigations overshadowed labour rights concerns. Critics argued that had a proper human rights impact assessment been conducted, Qatar would have been required to demonstrate labour reform capacity before being awarded the tournament.",
        "source": "US Department of Justice / The Guardian / New York Times",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "European Parliament Resolution on FIFA and Qatar Workers",
        "summary": "The European Parliament adopted a resolution in November 2022 calling on FIFA to compensate migrant workers and their families for human rights abuses connected to the World Cup. The resolution also called on Qatar to fully implement labour reforms and conduct independent investigations into worker deaths. FIFA responded by highlighting Qatar's reform progress.",
        "source": "European Parliament Resolution 2022/2948(RSP)",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "ITUC Campaign — Re-Run the Vote for Qatar 2022",
        "summary": "The International Trade Union Confederation (ITUC) launched a 're-run the vote' campaign arguing the 2022 World Cup should be relocated due to worker exploitation and corruption. ITUC estimated that 4,000 workers could die before a ball was kicked. While the tournament was not relocated, the campaign contributed to pressure for kafala reforms.",
        "source": "ITUC",
    },
    # ========================================================================
    # 4. Qatar Kafala Reform Timeline (2017-2022)
    # ========================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Domestic Workers Law No. 15 of 2017",
        "summary": "Qatar passed Law No. 15 of 2017 granting domestic workers the right to a maximum 10-hour workday, weekly day off, 3 weeks annual leave, and end-of-service benefits. The law was the first comprehensive domestic worker legislation in the GCC. Enforcement remains weak due to the private household setting; workers must access complaint mechanisms through the employer's cooperation.",
        "source": "Qatar Official Gazette / ILO",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Workers' Support and Insurance Fund (Law No. 17 of 2018)",
        "summary": "Qatar established the Workers' Support and Insurance Fund via Law No. 17 of 2018. The fund pays workers owed wages when employers default, covering basic salary, end-of-service benefits, and return airfare. Funded by a 60 QAR/month/worker levy on employers. By 2023 it had disbursed over QAR 1.8 billion (USD 500 million) to 36,000+ workers.",
        "source": "Qatar Ministry of Labour / ILO Qatar Office",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Abolition of Exit Permit (Law No. 13 of 2018)",
        "summary": "Law No. 13 of 2018 abolished the exit permit (NOC for departure) for most workers, effective January 2019. Previously workers needed employer permission to leave Qatar. Domestic workers were initially excluded but included from 2020. In practice, some employers still confiscate passports or file absconding charges to prevent workers from leaving.",
        "source": "Qatar Ministry of Labour / ILO",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Removal of NOC for Job Changes (Law No. 19 of 2020)",
        "summary": "Law No. 19 of 2020 (effective September 2020) removed the No Objection Certificate requirement for changing employers. Workers can now change jobs after serving a notice period (1 month during probation, 2 months after). This was the most significant reform to Qatar's kafala system. Between September 2020 and December 2023, over 350,000 workers changed employers using the new system.",
        "source": "Qatar Ministry of Labour / ILO Qatar Office",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Non-Discriminatory Minimum Wage (Law No. 17 of 2020)",
        "summary": "Qatar introduced the first non-discriminatory minimum wage in the GCC: QAR 1,000/month basic salary, plus QAR 300 food allowance and QAR 500 housing allowance (if not provided by employer), totaling QAR 1,800. Effective March 2021. Applies to all nationalities and sectors including domestic workers. ILO praised the measure but noted QAR 1,000 is below living wage estimates.",
        "source": "Qatar Official Gazette / ILO",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Wage Protection System (WPS) Expansion",
        "summary": "Qatar's Wage Protection System, originally launched in 2015, requires all employers to pay wages electronically through approved banks. By 2021, WPS covered over 2 million workers. The system flags delayed payments automatically. Ministry of Labour blocks companies that delay wages by 2+ months from recruiting new workers. However, WPS does not cover domestic workers, and some employers use creative compliance methods (paying and demanding cash back).",
        "source": "Qatar Ministry of Labour / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar Kafala Reform — Implementation Gaps (ILO Assessment)",
        "summary": "ILO's closing assessment of its Qatar technical cooperation programme (2024) found: reforms are legally significant but implementation uneven. Key gaps include employers retaliating with absconding charges against workers who try to change jobs, processing delays for job transfers, WPS evasion, and limited access to justice for domestic workers. ILO recommended extending the programme and strengthening enforcement.",
        "source": "ILO Qatar Programme Progress Report 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Job Transfer Statistics Post-NOC Abolition (2020-2023)",
        "metric": "job_transfers",
        "value": "350,000+",
        "summary": "Over 350,000 workers changed employers in Qatar between September 2020 and December 2023 without requiring a No Objection Certificate. This represents a fundamental shift from the kafala system. However, ILO found that 30 percent of transfer requests faced delays or employer obstruction, and absconding charges were filed against some workers who attempted to change jobs.",
        "source": "ILO Qatar Office / Qatar Ministry of Labour",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Absconding Charges as Retaliation Tool Post-Reform",
        "summary": "Despite kafala reforms, employers continue to file 'absconding' charges against workers who leave without permission or attempt job transfers. Absconding converts the worker's status to illegal, making them subject to detention and deportation. ILO reported that absconding charges were filed against workers as retaliation for wage complaints in numerous documented cases. Qatar reduced penalties for absconding but has not fully decriminalized it.",
        "source": "ILO / Amnesty International",
    },
    # ========================================================================
    # 5. Wage Protection System and Evasion
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Wage Protection System Evasion Methods",
        "summary": "Employers have developed methods to evade the Wage Protection System: (1) paying minimum into bank accounts while demanding cash back, (2) registering workers at higher wages than actually paid, (3) requiring workers to sign for hours not worked, (4) delays in WPS registration for new hires. Ministry of Labour increased inspections but the scale of the workforce makes comprehensive monitoring difficult.",
        "source": "ILO / Migrant-Rights.org",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — WPS Coverage and Compliance Rates",
        "metric": "wps_coverage",
        "value": "2 million+ workers covered",
        "summary": "Qatar's Wage Protection System covered over 2 million workers by 2022. Compliance rates for on-time payment improved from 83 percent (2018) to 91 percent (2022). However, domestic workers remain excluded from WPS. The Ministry of Labour processed over 7,000 wage complaints in 2022 and blocked 400+ companies from recruiting for wage violations.",
        "source": "Qatar Ministry of Labour Annual Report 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Al Bandary Engineering Wage Theft Case",
        "summary": "Amnesty International documented hundreds of workers employed by Al Bandary Engineering and Contracting (subcontractor on World Cup hotel projects) who went 4-7 months without pay. Workers could not leave the country or change employers due to kafala restrictions (pre-reform). The company was blacklisted from Supreme Committee projects but continued operating on non-World Cup sites.",
        "source": "Amnesty International (2020)",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Qatar Meta Coats Worker Wage Withholding",
        "summary": "Qatar Meta Coats, a painting and coating subcontractor on stadium projects, withheld wages from over 100 workers for 3-5 months. Workers were threatened with deportation if they complained. Amnesty International intervention led to partial wage recovery through the Supreme Committee's grievance mechanism. Case illustrates vulnerability of workers employed through subcontracting chains.",
        "source": "Amnesty International / BWI",
    },
    # ========================================================================
    # 6. Workers' Support and Insurance Fund
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Workers' Support and Insurance Fund Disbursements",
        "metric": "wsif_disbursements",
        "value": "QAR 1.8 billion (USD 500 million)",
        "summary": "The Workers' Support and Insurance Fund (WSIF) disbursed QAR 1.8 billion (approximately USD 500 million) to over 36,000 workers between 2018 and 2023 for unpaid wages, end-of-service benefits, and return flights. The fund is a last-resort mechanism when employers default. Processing times average 3-6 months. ILO noted gaps in coverage for domestic workers and workers outside Qatar at time of claim.",
        "source": "ILO Qatar Office / Qatar Ministry of Labour",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar WSIF — Barriers to Access for Departed Workers",
        "summary": "Workers who have already left Qatar face significant barriers accessing the Workers' Support and Insurance Fund. Claims must be filed in Qatar, requiring workers to remain in-country during processing (3-6 months). Workers who were deported or left under 'absconding' status are effectively excluded. ILO recommended establishing post-departure claim mechanisms and embassy-based filing systems.",
        "source": "ILO / Migrant-Rights.org",
    },
    # ========================================================================
    # 7. Heat Stress and Working Hour Restrictions
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Heat-Related Worker Deaths from Lancet Study",
        "metric": "heat_attributable_deaths",
        "value": "571 (2009-2017)",
        "summary": "A Lancet Planetary Health study (2019) analyzed 1,300 Nepali migrant worker deaths in Qatar between 2009 and 2017, attributing 571 to heat stress. Deaths classified as cardiovascular on death certificates were actually caused by prolonged exposure to temperatures exceeding 45 degrees Celsius. Study concluded occupational heat exposure was responsible for 44 percent of Nepali worker deaths in Qatar.",
        "source": "The Lancet Planetary Health (2019)",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Ministerial Decision No. 17 of 2021 (Expanded Heat Protections)",
        "summary": "Qatar expanded outdoor work restrictions via Ministerial Decision No. 17 of 2021: outdoor work prohibited June 1 to September 15, 10:00am to 3:30pm (previously 11:30am-3:00pm, June 15-September 15). Added WBGT (Wet Bulb Globe Temperature) monitoring — all outdoor work must stop if WBGT exceeds 32.1 degrees Celsius regardless of time. Employers must provide shade, water, and rest areas. Penalty: temporary or permanent site closure.",
        "source": "Qatar Ministry of Labour / ILO Qatar",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — WBGT Monitoring Implementation Challenges",
        "summary": "Despite the 2021 heat regulation requiring WBGT monitoring, implementation faced challenges: many construction sites lacked monitoring equipment, supervisors were untrained in WBGT readings, and enforcement relied on worker complaints. ILO-provided WBGT stations covered major stadium sites but smaller construction projects had no coverage. Workers reported being asked to continue working when temperatures exceeded thresholds.",
        "source": "ILO / QRCS (Qatar Red Crescent Society)",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Summer Temperature Extremes on Construction Sites",
        "metric": "peak_construction_temperature",
        "value": "50+ degrees Celsius",
        "summary": "Surface temperatures on Qatar construction sites in July-August regularly exceed 50 degrees Celsius. WBGT measurements by ILO monitoring stations recorded values above 35 degrees Celsius — well beyond the 32.1-degree threshold — for 4-6 hours daily outside the midday ban period. Workers performing concrete pouring, steel work, and roofing face the highest exposure.",
        "source": "ILO Qatar / Qatar Meteorological Department",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Chronic Kidney Disease Among Construction Workers",
        "summary": "Research published in Environmental Research Letters found elevated rates of chronic kidney disease among migrant construction workers in Qatar, linked to chronic dehydration from outdoor work in extreme heat. Workers on 10-12 hour shifts in temperatures exceeding 45 degrees Celsius suffer repeated acute kidney injury episodes. Many return home with permanent kidney damage. Qatar's Worker Health Programme began screening in 2022 but retroactive cases are uncompensated.",
        "source": "Environmental Research Letters / ILO",
    },
    # ========================================================================
    # 8. Worker Accommodation and Living Conditions
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar Industrial Area — Labour Camp Conditions",
        "summary": "The Industrial Area south of Doha houses approximately 300,000+ migrant workers in labour camps. Investigations by HRW and Amnesty found overcrowded rooms (8-12 workers per room designed for 4), shared bathrooms (1 per 20-30 workers), inadequate kitchen facilities, poor ventilation, and insect infestations. New camps built after 2015 meet higher standards but older camps remain occupied.",
        "source": "HRW / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Labour City (Barwa Al Baraha) Model Housing",
        "summary": "Qatar developed Labour City (Barwa Al Baraha) as a model worker accommodation housing 53,000 workers in upgraded facilities with recreational areas, shops, and medical clinics. Completed in phases from 2015. While conditions are significantly better than Industrial Area camps, Labour City houses a small fraction of Qatar's 1.5 million+ construction workforce. Workers assigned to Labour City tend to be on Supreme Committee and government projects.",
        "source": "Qatar Ministry of Labour / Barwa Real Estate",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Post-World Cup Worker Displacement",
        "summary": "After the World Cup ended in December 2022, approximately 30,000 workers employed on tournament-specific projects faced sudden layoffs. Many were laid off without end-of-service benefits or return flights. Workers' Support and Insurance Fund processed thousands of claims. Some workers were stranded in Qatar for months awaiting resolution. Post-tournament economic slowdown in construction reduced overall demand for migrant labour.",
        "source": "Migrant-Rights.org / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Freedom of Movement Restrictions in Worker Camps",
        "summary": "Workers in many Qatar labour camps face de facto movement restrictions: camps are located far from urban centres with limited transport, employers enforce curfews, and workers who leave camps outside designated hours risk disciplinary action. Supreme Committee standards prohibit movement restrictions but apply only to project-specific sites. Workers in non-SC projects reported being confined to camps except during working hours.",
        "source": "Amnesty International / HRW",
    },
    # ========================================================================
    # 9. Specific Contractor Prosecutions
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Contractor Blacklisting for Labour Violations",
        "summary": "Qatar's Ministry of Labour maintains a blacklist of companies prohibited from recruiting new workers due to labour violations. By 2023, over 400 companies had been blacklisted for wage delays, unsafe conditions, or worker welfare violations. However, blacklisted companies can re-register under new names. Criminal prosecution of employers for wage theft or unsafe conditions remains rare.",
        "source": "Qatar Ministry of Labour / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — J&P (Joannou & Paraskevaides) Worker Complaints",
        "summary": "Workers employed by J&P, one of Qatar's largest construction contractors (involved in Lusail City and highway projects), filed hundreds of complaints about delayed wages, poor camp conditions, and excessive overtime. Labour dispute committees ruled in workers' favour in multiple cases. J&P faced partial recruitment ban. Case illustrates that even major contractors with established reputations engage in wage withholding practices.",
        "source": "Qatar Labour Dispute Committees / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — BK Gulf (HBK Contracting Group) — Stadium Main Contractor",
        "summary": "HBK Contracting Group and its subsidiary BK Gulf served as main contractor on multiple Supreme Committee stadium projects. While the company met most Workers' Welfare Standards requirements, subcontractors under its supervision were repeatedly cited for wage delays and passport confiscation. SC audits found that main contractor oversight of subcontractor welfare compliance was inadequate.",
        "source": "Supreme Committee Audit Reports / BWI",
    },
    # ========================================================================
    # 10. Recruitment Agency Fraud for GCC Construction
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Recruitment Fee Charging Despite Zero-Cost Policy",
        "summary": "Qatar's Law No. 21 of 2015 prohibits recruitment agencies from charging workers fees. In practice, workers continue to pay fees to agents in origin countries. ILO surveys found the average Nepali worker paid USD 1,600-2,500 in recruitment fees to work in Qatar, creating debt bondage situations. Fees are charged by sub-agents and intermediaries in origin countries where Qatari law has no jurisdiction.",
        "source": "ILO / Verité / Amnesty International",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Average Recruitment Fees Paid by Migrant Workers",
        "metric": "average_recruitment_fee",
        "value": "USD 1,600-2,500",
        "summary": "Despite Qatar's zero-recruitment-fee policy, ILO surveys found workers from Nepal, Bangladesh, and India paid USD 1,600-2,500 on average to secure construction jobs in Qatar. Fees are charged by intermediaries in origin countries. Workers borrow at high interest rates (20-36 percent annually), creating debt bondage that takes 6-18 months of wages to repay. Some workers reported paying up to USD 5,000.",
        "source": "ILO / Verité",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Contract Substitution — Promised vs Actual Terms in Qatar",
        "summary": "Workers recruited for Qatar construction regularly report contract substitution: they sign contracts in origin countries promising specific wages, job roles, and conditions, then are presented with different contracts upon arrival in Qatar. Common substitutions include lower wages (30-50 percent reduction), different job roles (e.g., recruited as electrician, employed as labourer), and longer working hours. Workers who refuse sign face deportation at their own expense.",
        "source": "Amnesty International / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Nepal — Recruitment Agency Fraud for Qatar Construction Jobs",
        "summary": "Nepali recruitment agencies charge workers USD 1,000-5,000 for Qatar construction jobs despite Nepal's legal cap on fees. Agents operate through unregistered sub-agents in rural districts. Workers mortgage family land or borrow from moneylenders at 36 percent annual interest. Nepal's Department of Foreign Employment has limited enforcement capacity. In 2022, 847 recruitment agencies were registered but an estimated 2,000+ unregistered agents operated.",
        "source": "Nepal Department of Foreign Employment / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Bangladesh — Dalal System Feeding GCC Construction Labour",
        "summary": "Bangladesh's informal 'dalal' (broker) system channels workers to Qatar and other GCC construction markets. Dalals operate in rural areas, promising lucrative jobs for fees of USD 2,000-7,000. Workers sell assets or borrow from informal lenders. Dalals are connected to licensed agencies in Dhaka that process official documentation. Bangladesh government's attempts to regulate the dalal system have been largely unsuccessful.",
        "source": "Amnesty International / BMET (Bangladesh Bureau of Manpower, Employment and Training)",
    },
    # ========================================================================
    # 11. Worker Protests, Strikes, and Deportations
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — 2022 Worker Protests Over Unpaid Wages",
        "summary": "In August 2022, hundreds of workers protested in Doha's Industrial Area over months of unpaid wages from construction and cleaning companies. Video footage circulated on social media. Qatari security forces dispersed the protest. Workers reported that some protest leaders were subsequently deported. The Ministry of Labour stated it would investigate wage complaints but protests are effectively illegal under Qatar law.",
        "source": "Migrant-Rights.org / Al Jazeera",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Deportation of Workers Who File Complaints",
        "summary": "Workers who file labour complaints in Qatar face risk of retaliatory deportation. Employers can report workers as 'absconding' (abandoning employment), converting their status to illegal. Workers in dispute with employers may be detained and deported before their case is resolved. ILO has documented this pattern and recommended that workers in active dispute proceedings be granted temporary work permits.",
        "source": "ILO / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — 2014 Labour Strike at Lusail Development",
        "summary": "In 2014, over 1,000 workers building Lusail City infrastructure went on strike over unpaid wages and poor living conditions. Qatari police arrested strike leaders and dozens of workers were deported. Strikes are illegal under Qatari law (Law No. 14 of 2004 prohibits work stoppages). The incident drew international media attention and contributed to pressure for kafala reform.",
        "source": "The Guardian / BBC / ITUC",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Restrictions on Worker Collective Action",
        "summary": "Qatar does not permit workers to form or join trade unions. Law No. 14 of 2004 allows only 'joint committees' of Qatari and non-Qatari workers in companies with 25+ employees, but migrant workers cannot serve as committee chairs. Strikes are prohibited. ILO Committee on Freedom of Association has repeatedly urged Qatar to allow genuine collective bargaining. Workers who attempt collective action face deportation.",
        "source": "ILO Committee on Freedom of Association / ITUC",
    },
    # ========================================================================
    # 12. ILO Technical Cooperation Programme in Qatar
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "ILO-Qatar Technical Cooperation Programme (2018-2024)",
        "summary": "Qatar signed a 3-year technical cooperation agreement with the ILO in 2017 (effective 2018, extended to 2024) to reform the labour system. Key outcomes: minimum wage, NOC abolition, exit permit reform, Labour Dispute Committees, enhanced WPS, improved accommodation standards. ILO stationed a project office in Doha with 20+ staff. Critics argued the ILO presence gave Qatar legitimacy cover while reforms remained unevenly implemented.",
        "source": "ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "ILO — Qatar Programme Closing Assessment (2024)",
        "summary": "ILO's closing assessment of the Qatar programme (2024) found significant legislative progress but noted persistent implementation challenges: WPS evasion, retaliatory absconding charges, limited domestic worker protections, inadequate death investigations, and continued passport confiscation. ILO recommended a successor programme focusing on enforcement, digital complaint systems, and domestic worker inclusion.",
        "source": "ILO Programme Progress Report 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "ILO — Labour Dispute Resolution Committees in Qatar",
        "summary": "ILO helped establish Labour Dispute Resolution Committees (LDRCs) in Qatar to provide rapid, accessible justice for migrant workers. Between 2018 and 2023, LDRCs processed over 35,000 cases, recovering QAR 1.8 billion in unpaid wages. Median resolution time: 3 weeks. Cases are free for workers to file. However, workers must be physically in Qatar to file, excluding deported or repatriated workers.",
        "source": "ILO Qatar Office",
    },
    # ========================================================================
    # 13. COVID-19 Impact on GCC Construction Workers
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — COVID-19 Impact on Migrant Construction Workers",
        "summary": "During COVID-19 lockdowns in 2020, Qatar's Industrial Area labour camps became hotspots due to overcrowding. Workers were confined to camps without pay during construction shutdowns. Qatar reported 40,000+ migrant worker COVID infections. Workers could not access testing or medical care in early months. Qatar eventually established dedicated field hospitals and testing for workers, but isolation protocols in cramped camps were impossible to implement effectively.",
        "source": "HRW / Amnesty International / Qatar Ministry of Public Health",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Industrial Area Lockdown and Worker Detention (2020)",
        "summary": "In March 2020, Qatar placed the Industrial Area (housing 300,000+ workers) under full lockdown, designating it a 'quarantine zone.' Workers were prohibited from leaving for work or any other reason. Many went weeks without income. Food distribution was initially inadequate. The lockdown highlighted the extreme vulnerability of densely housed migrant workers during a pandemic.",
        "source": "Amnesty International / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — COVID-19 and Migrant Worker Camp Outbreaks",
        "summary": "Dubai and Abu Dhabi labour camps experienced significant COVID-19 outbreaks in 2020. Workers in construction camps were unable to socially distance. Many companies stopped paying wages during construction shutdowns. Workers stranded without income could not afford food or repatriation. UAE government eventually organized free flights for some stranded workers and distributed food parcels in labour camps.",
        "source": "HRW / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — COVID-19 Crackdowns on Undocumented Workers",
        "summary": "Saudi Arabia used COVID-19 as a pretext for crackdowns on undocumented migrant workers. Ethiopian workers were rounded up and detained in overcrowded facilities before mass deportation. Reports from detention centres described inhumane conditions: 200+ workers per cell, insufficient food and water, physical abuse. Over 16,000 Ethiopian migrants were deported during the pandemic.",
        "source": "Amnesty International / Sunday Telegraph",
    },
    # ========================================================================
    # 14. Exit Permit Reforms and Implementation
    # ========================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Exit Permit History and Abolition",
        "summary": "Qatar's exit permit system required workers to obtain employer permission (NOC) before leaving the country. Abolished for most workers by Law No. 13 of 2018 (effective January 2019), extended to all workers including domestic workers by 2020. Prior to abolition, employers routinely withheld exit permits to prevent workers from leaving, even after contract completion. Post-reform, some employers use passport confiscation as a substitute restriction.",
        "source": "Qatar Ministry of Labour / ILO",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Exit/Re-Entry Visa Reform (2021)",
        "summary": "Saudi Arabia's March 2021 Labour Reform Initiative allows workers to obtain exit/re-entry visas without employer approval. Previously, the iqama (residency permit) system required employer sponsorship for all travel. Domestic workers remain excluded from this reform. Implementation has been uneven: some employers still physically withhold workers' iqamas, preventing travel.",
        "source": "Saudi Ministry of Human Resources and Social Development",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "AE",
        "title": "UAE — Abolition of Labour Ban on Job Changers",
        "summary": "The UAE's Federal Decree Law No. 33 of 2021 (effective February 2022) eliminated the 'labour ban' that previously prevented workers who left jobs from working in the UAE for 6-12 months. Workers can now change employers with 1-3 months' notice. However, workers terminated for 'absconding' still face bans. This reform reduced one major kafala restriction but left enforcement gaps.",
        "source": "UAE Ministry of Human Resources and Emiratisation",
    },
    # ========================================================================
    # 15. Minimum Wage Introduction Across GCC
    # ========================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — First GCC Minimum Wage (QAR 1,000/month, March 2021)",
        "summary": "Qatar's minimum wage of QAR 1,000/month basic salary (USD 275) applies to all workers regardless of nationality or sector, making it the first non-discriminatory minimum wage in the GCC. Plus QAR 300 food and QAR 500 housing allowances if not provided. ILO noted the minimum wage was below living wage calculations. Domestic workers are included, a significant step given their exclusion in other GCC states.",
        "source": "Qatar Official Gazette / ILO",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KW",
        "title": "Kuwait — Minimum Wage for Domestic Workers (2016)",
        "summary": "Kuwait introduced a minimum wage for domestic workers of KWD 60/month (approximately USD 200) in 2016. This was among the first domestic worker minimum wages in the GCC. Enforcement is limited due to the private household setting. Many workers report being paid below the minimum. Kuwait's overall minimum wage for other sectors is KWD 75/month (approximately USD 250), unchanged since 2016.",
        "source": "Kuwait Ministry of Interior / Migrant-Rights.org",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "AE",
        "title": "UAE — No National Minimum Wage for Private Sector",
        "summary": "The UAE has no statutory minimum wage for private sector workers as of 2025. Wages are set by market and determined in individual contracts. Some free zones set minimum salary thresholds for visa purposes. Construction workers frequently earn AED 800-1,500/month (USD 218-408) for 10-12 hour days. The absence of a minimum wage is a significant gap in worker protection.",
        "source": "UAE Ministry of Human Resources / Migrant-Rights.org",
    },
    # ========================================================================
    # 16. Worker Death Reporting and Compensation
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Worker Death Compensation Failures",
        "summary": "Families of workers who died in Qatar report receiving little or no compensation. Qatar law provides for death compensation equivalent to 3 years' wages, but many employers fail to pay. Workers' Support and Insurance Fund covers some cases but requires families to navigate complex claims processes from their home countries. Amnesty International documented cases where families received nothing despite confirmed workplace deaths.",
        "source": "Amnesty International / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Inadequate Death Investigation Procedures",
        "summary": "Qatar's death investigation procedures for migrant workers are inadequate. Autopsies are rarely performed. Death certificates commonly list 'acute cardiac failure' without determining whether heat stress, workplace injury, or occupational disease was the underlying cause. Families in origin countries receive death certificates in Arabic without translation. ILO and Amnesty have repeatedly called for mandatory autopsy protocols for all migrant worker deaths.",
        "source": "Amnesty International / ILO / The Lancet",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Amnesty Campaign for Worker Death Investigation Reform",
        "metric": "unexplained_deaths_percentage",
        "value": "69%",
        "summary": "Amnesty International analysis found that 69 percent of migrant worker deaths in Qatar are attributed to 'natural causes' or 'cardiac arrest' without further investigation. This classification effectively prevents families from claiming work-related death compensation. Amnesty called for mandatory, independent autopsy for every migrant worker death and publication of detailed mortality data by nationality, occupation, and cause.",
        "source": "Amnesty International",
    },
    # ========================================================================
    # 17. Saudi Arabia — NEOM Project
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi NEOM — USD 500 Billion Megaproject Worker Conditions",
        "summary": "NEOM, Saudi Arabia's USD 500 billion future city project in Tabuk Province, employed over 100,000 construction workers by 2023 across components including The Line, Trojena, Sindalah, and Oxagon. Workers reported 10-14 hour shifts in desert heat, 3-6 month wage delays, overcrowded camps in remote desert locations, and movement restrictions. Access for journalists and human rights monitors has been denied.",
        "source": "The Guardian / ALQST for Human Rights",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "NEOM — Nepali Worker Deaths (2022-2023)",
        "summary": "The Guardian reported at least 21 Nepali worker deaths on the NEOM project between 2022 and 2023. Death certificates listed 'natural causes' or 'cardiac arrest' despite workers being in their 20s-30s with no known health conditions. Temperatures at the site exceed 45 degrees Celsius in summer. Saudi authorities denied systemic issues and refused to allow independent investigation.",
        "source": "The Guardian (2023)",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "NEOM — The Line Project and Forced Displacement",
        "summary": "NEOM's flagship project The Line (a 170km linear city) required clearing of the Howeitat tribe's traditional lands. Tribal members who resisted displacement were arrested and sentenced to death (later commuted for some). Construction workers brought in to build The Line reported having no knowledge of the displacement or its circumstances. The project combines megaproject labour exploitation with indigenous rights violations.",
        "source": "ALQST for Human Rights / The Guardian / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "NEOM — Contractor Labour Practices",
        "summary": "Major NEOM contractors include Samsung C&T, Bechtel, Jacobs, and numerous Saudi and international subcontractors. Workers employed through multi-layered subcontracting report that main contractors' welfare standards do not extend to lower-tier subcontractor employees. Workers from South and Southeast Asia are recruited through agencies charging fees of USD 2,000-5,000 despite Saudi and origin-country prohibitions.",
        "source": "ALQST / Business & Human Rights Resource Centre",
    },
    # ========================================================================
    # 18. Saudi Vision 2030 Megaprojects
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Vision 2030 — Construction Megaproject Labour Demand",
        "summary": "Saudi Arabia's Vision 2030 programme includes mega-projects valued at over USD 1.2 trillion: NEOM, Red Sea Global, Qiddiya, Diriyah Gate, Jeddah Tower, Riyadh Metro, and Riyadh Season City. The construction boom requires an estimated 1.5 million additional migrant workers. Labour rights organizations warned that the pace of development incentivizes cutting corners on worker welfare.",
        "source": "Business & Human Rights Resource Centre / FairSquare Projects",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Red Sea Global — Tourism Resort Construction Workers",
        "summary": "The Red Sea Global mega-resort project on Saudi Arabia's west coast employs tens of thousands of workers across 50+ resort islands. Workers housed in remote desert camps reported limited access to medical care, delayed wages, and 12-hour shifts. The project claims to meet international sustainability standards but has not submitted to independent labour rights audits.",
        "source": "Business & Human Rights Resource Centre",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Qiddiya — Entertainment City Worker Conditions",
        "summary": "Qiddiya, a USD 8 billion entertainment mega-project near Riyadh, employed 40,000+ workers in construction of theme parks, sports venues, and residential areas. Workers from South and Southeast Asia reported standard GCC construction complaints: excessive overtime, wage delays, passport confiscation by subcontractors, and cramped camp housing. No independent monitoring has been permitted.",
        "source": "Business & Human Rights Resource Centre / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Riyadh Metro — Worker Safety and Death Reports",
        "summary": "Riyadh Metro (6 lines, 85 stations) construction employed 30,000+ workers at peak. Consortium contractors included Bechtel, Vinci, Samsung, and Salini-Impregilo. Worker deaths were reported during tunnelling operations but Saudi authorities did not publish comprehensive worker mortality data. BWI raised concerns about heat exposure for surface-level construction and the pace of the construction timeline creating safety risks.",
        "source": "BWI / Construction industry publications",
    },
    {
        "type": "statistic",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Migrant Worker Population in Construction",
        "metric": "construction_migrant_workers",
        "value": "5+ million",
        "summary": "Saudi Arabia's construction sector employs an estimated 5+ million migrant workers, predominantly from India, Pakistan, Bangladesh, Nepal, Philippines, and Egypt. The sector accounts for approximately 25 percent of Saudi GDP. Workers earn SAR 800-2,000/month (USD 213-533) for 10-12 hour days. Saudi nationals constitute less than 10 percent of the construction workforce.",
        "source": "Saudi General Authority for Statistics / IOM",
    },
    # ========================================================================
    # 19. UAE — Construction Sector Exploitation
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Dubai Expo 2020 Worker Exploitation",
        "summary": "Workers constructing the Dubai Expo 2020 site (delayed to 2021-2022) reported conditions mirroring the Qatar World Cup: wage delays of 2-5 months, passport confiscation, excessive overtime, and overcrowded labour camps. Expo organizers established worker welfare standards but enforcement was limited to the main Expo site. Hotels, transport, and support infrastructure were built without comparable oversight.",
        "source": "Equidem / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Dubai — Burj Khalifa Construction Worker Conditions",
        "summary": "During construction of the Burj Khalifa (2004-2010, 828m), workers earned approximately AED 800/month (USD 217) for 12-hour shifts at extreme heights. An estimated 3,000-4,000 South Asian workers were employed at peak. Contractor Samsung and Arabtec faced criticism for camp conditions and wage practices. The exact number of worker deaths during construction has never been officially disclosed.",
        "source": "HRW / Construction industry reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Arabtec Worker Strike (2013)",
        "summary": "In May 2013, thousands of Arabtec construction workers (one of the UAE's largest contractors) went on strike in Dubai demanding higher wages. Workers earned AED 650-800/month (USD 177-218) despite Arabtec reporting record profits. Police dispersed the strike. An estimated 70 workers were deported. Arabtec raised wages by AED 200/month following the strike but strike leaders were not reinstated.",
        "source": "The Guardian / Gulf News / ITUC",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — 2006 Construction Worker Protests",
        "summary": "In March 2006, approximately 2,500 workers constructing the Burj Khalifa went on a rampage in Dubai, damaging cars and offices, protesting about low wages and poor conditions. This was one of the largest worker protests in UAE history. The UAE subsequently introduced a midday work ban (12:30-3pm, July-August) but did not establish minimum wages or allow collective bargaining.",
        "source": "BBC / Reuters / HRW",
    },
    # ========================================================================
    # 20. UAE — Saadiyat Island Cultural District
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Abu Dhabi — Saadiyat Island Louvre Abu Dhabi Worker Exploitation",
        "summary": "Workers constructing the Louvre Abu Dhabi on Saadiyat Island (completed 2017) reported working 11-12 hour days, 6 days a week, in temperatures exceeding 50 degrees Celsius. Workers lived in camps 2 hours from the site. HRW documented passport confiscation, recruitment fee debt, and crowded housing. TDIC (Tourism Development and Investment Company) implemented welfare standards but enforcement gaps persisted with subcontractors.",
        "source": "HRW / The Guardian / Gulf Labor Coalition",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Abu Dhabi — Guggenheim Abu Dhabi Worker Rights Campaign",
        "summary": "The planned Guggenheim Abu Dhabi museum on Saadiyat Island (designed by Frank Gehry, construction repeatedly delayed) became a focal point for labour rights campaigning. The Gulf Labor Coalition organized artist boycotts and protests against worker exploitation on the island. Over 1,000 artists signed a pledge refusing to show work at the museum until worker conditions improved. Construction workers on the project had reported typical GCC conditions: debt bondage, passport confiscation, and wage theft.",
        "source": "Gulf Labor Coalition / HRW",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Abu Dhabi — NYU Abu Dhabi Campus Worker Exploitation",
        "summary": "New York University Abu Dhabi campus construction on Saadiyat Island drew scrutiny after an NYU-commissioned report (Nardello & Co., 2015) found evidence of recruitment fee payment, crowded labour camps, and wage discrepancies affecting workers. NYU had promised 'unprecedented' worker protections. The case illustrated the gap between corporate welfare policies and ground-level implementation through subcontracting chains in the GCC.",
        "source": "Nardello & Co. Report / New York Times / The Guardian",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Abu Dhabi — Saadiyat Island Employment Practices Policy (2014)",
        "summary": "Following sustained criticism, TDIC established an Employment Practices Policy (EPP) for Saadiyat Island cultural district projects requiring: zero recruitment fees, adequate housing, regular wage payments, and passport retention by workers. Compliance monitoring was contracted to PwC. However, PwC audits found persistent non-compliance among subcontractors and acknowledged their monitoring methodology had limitations.",
        "source": "TDIC / PwC Compliance Reports / HRW",
    },
    # ========================================================================
    # 21. Kuwait Construction Sector
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "title": "Kuwait — Construction Sector Worker Exploitation Patterns",
        "summary": "Kuwait's construction sector employs approximately 700,000 migrant workers, predominantly from India, Bangladesh, Egypt, and Sri Lanka. Common exploitation patterns include: 3-6 month wage delays, contract substitution, passport confiscation (despite legal prohibition since 2009), and overcrowded accommodation in Jleeb Al Shuyoukh and other industrial areas. Kuwait's kafala system remains largely unreformed compared to Qatar and UAE.",
        "source": "HRW / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "title": "Kuwait — Worker Suicide Linked to Exploitation",
        "summary": "Kuwait has seen a pattern of migrant worker suicides linked to unpaid wages, debt bondage, and abuse. Between 2018 and 2022, Indian Embassy in Kuwait reported over 500 Indian worker deaths per year, including suicides. Workers trapped in debt from recruitment fees and unable to leave due to kafala restrictions face acute mental health crises. Kuwait does not provide mental health services for migrant workers.",
        "source": "Indian Embassy Kuwait / Migrant-Rights.org",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KW",
        "title": "Kuwait — Ministerial Order No. 842/2015 Regulating Domestic Workers",
        "summary": "Kuwait passed Law No. 68/2015 for domestic workers, introducing minimum standards: weekly day off, 12-hour maximum workday, annual leave of 30 days, and end-of-service benefits. A Domestic Workers Department was established to handle complaints. While more comprehensive than domestic worker laws in some GCC states, enforcement remains weak. Kuwait also established Shuoon (government-run housemaid company) to reduce private agency abuses.",
        "source": "Kuwait Ministry of Interior / ILO",
    },
    # ========================================================================
    # 22. Bahrain Construction and Services
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "BH",
        "title": "Bahrain — Construction Sector Worker Exploitation",
        "summary": "Bahrain's construction sector employs approximately 150,000 migrant workers. While Bahrain was the first GCC state to reform the kafala system (2009 Labour Market Regulatory Authority), construction workers still report wage delays, excessive overtime, and inadequate safety equipment. Bahrain's relatively smaller construction market means fewer megaproject-scale issues but exploitation patterns persist at the subcontractor level.",
        "source": "Migrant-Rights.org / LMRA Bahrain",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BH",
        "title": "Bahrain — Labour Market Regulatory Authority (LMRA) Reforms",
        "summary": "Bahrain established the Labour Market Regulatory Authority (LMRA) in 2006, the first GCC state to create an independent labour market regulator. LMRA introduced a flexi-permit system allowing workers to sponsor themselves and work for any employer. By 2023, over 75,000 workers held flexi-permits. While this effectively abolished kafala for flexi-permit holders, regular work-visa holders remain tied to sponsors.",
        "source": "Bahrain LMRA / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BH",
        "title": "Bahrain — Free Visa Trading (Visa Trading Racket)",
        "summary": "Bahrain has struggled with 'free visa' trading, where sponsors bring workers into the country and then allow them to work for others in exchange for a monthly fee (typically BHD 30-50/month). Workers on free visas have no employment protections, cannot access labour courts, and are vulnerable to arrest for working outside their visa conditions. LMRA crackdowns have reduced but not eliminated the practice.",
        "source": "Migrant-Rights.org / LMRA Bahrain",
    },
    # ========================================================================
    # 23. Oman Construction Sector
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "OM",
        "title": "Oman — Construction Sector Migrant Worker Conditions",
        "summary": "Oman's construction sector employs approximately 400,000 migrant workers, primarily from India, Bangladesh, and Pakistan. Workers on road, housing, and infrastructure projects report standard GCC exploitation patterns: recruitment fee debt, wage delays, passport confiscation, and heat exposure. Oman's kafala system remains largely unchanged. The Muscat-Sohar highway and Duqm Special Economic Zone have been major employment sites.",
        "source": "Migrant-Rights.org / Business & Human Rights Resource Centre",
    },
    {
        "type": "case_study",
        "jurisdiction": "OM",
        "title": "Oman — Duqm Special Economic Zone Worker Exploitation",
        "summary": "The Duqm Special Economic Zone (SEZD) in central Oman, developed as a major industrial and port complex, employed thousands of workers in remote desert conditions. Workers reported extreme isolation (Duqm is 550km from Muscat), limited communication access, 6-month wage delays, and temperatures exceeding 45 degrees Celsius. The remote location makes labour inspection and worker complaint mechanisms practically inaccessible.",
        "source": "Business & Human Rights Resource Centre / Migrant-Rights.org",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "OM",
        "title": "Oman — Job Mobility Reforms (2021)",
        "summary": "Oman introduced limited job mobility reforms in 2021 allowing workers to change employers after 2 years or after contract expiry without employer NOC. Workers with unpaid wage complaints can also transfer. However, the system is bureaucratic and employers can file counter-claims. Domestic workers are excluded. The reform is less comprehensive than Qatar's 2020 changes.",
        "source": "Oman Ministry of Labour / Migrant-Rights.org",
    },
    # ========================================================================
    # 24. Passport Confiscation Across GCC
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Passport Confiscation Prevalence",
        "metric": "passport_confiscation_rate",
        "value": "Approximately 60%",
        "summary": "ILO surveys (2019-2020) found approximately 60 percent of migrant workers in Qatar had their passports held by their employer, despite Qatar criminalizing the practice in 2011 (Law No. 15, penalty QAR 25,000). Workers report passports kept in company offices with access only for travel or renewal. ILO recommended increased inspections and awareness campaigns. Enforcement of confiscation penalties remains rare.",
        "source": "ILO / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Systematic Passport Confiscation",
        "summary": "Passport confiscation by employers is widespread in Saudi Arabia despite being prohibited since 2009. Saudi Ministry of Labour estimates 70-80 percent of migrant workers do not retain their own passports. For domestic workers, the rate is higher. Workers without passports cannot change jobs, leave the country, or prove their identity. Confiscation is used as a mechanism of control and to prevent workers from seeking better employment.",
        "source": "HRW / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Passport Confiscation in Construction Sector",
        "summary": "Despite Ministerial Decree No. 788 of 2009 prohibiting passport confiscation, the practice remains endemic in the UAE construction sector. Employers justify confiscation as necessary to prevent workers from absconding. Workers interviewed by HRW reported being told their passports were held 'for safekeeping' with no access on request. The penalty for confiscation (AED 20,000 fine) is rarely imposed.",
        "source": "HRW / Migrant-Rights.org",
    },
    # ========================================================================
    # 25. Recruitment Fee Debt Across GCC Construction
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "GCC Construction — Recruitment Fee Debt Bondage Scale",
        "metric": "workers_in_fee_debt",
        "value": "Millions",
        "summary": "Across the GCC, an estimated majority of the 15+ million migrant workers arrived through fee-charging recruitment agents. Average fees range from USD 1,000 (close-country corridors) to USD 7,000 (long-distance corridors). Workers typically borrow at 20-36 percent annual interest. Debt repayment takes 6-18 months, during which workers cannot leave without forfeiting their investment. This constitutes debt bondage under ILO definitions.",
        "source": "ILO / Verité / FairSquare Projects",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Recruitment Fee Charging Despite Prohibition",
        "summary": "Saudi Arabia's Labour Law prohibits employers and recruitment agencies from charging workers fees. However, workers from South and Southeast Asia consistently report paying USD 2,000-6,000 to intermediaries for Saudi construction jobs. The fees are charged by sub-agents in origin countries and licensed agencies that share fees with Saudi counterparts. Saudi Ministry of Human Resources signed bilateral agreements with origin countries to address the issue but enforcement across borders is minimal.",
        "source": "HRW / ILO / Verité",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Recruitment Fee Debt Among Construction Workers",
        "summary": "Workers recruited for UAE construction report paying USD 2,000-4,000 in fees to agencies in India, Bangladesh, Nepal, and Pakistan. Upon arrival, many find wages are lower than promised (contract substitution), extending the debt repayment period. Workers earning AED 800-1,200/month (USD 218-327) may take 12-24 months to repay recruitment debt, during which they are effectively in bonded labour.",
        "source": "HRW / Migrant-Rights.org",
    },
    # ========================================================================
    # 26. Specific GCC Contractor Practices
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Arabtec — Largest UAE Contractor Worker Conditions and Collapse",
        "summary": "Arabtec Holding, once the UAE's largest construction company (built Burj Khalifa), collapsed into administration in 2020 owing AED 4.5 billion. Thousands of workers were left without wages or end-of-service benefits. Workers were stranded in the UAE unable to afford return flights. Arabtec's collapse exposed the vulnerability of migrant workers when large contractors fail: no safety net, no priority in creditor claims, and no government bailout for workers.",
        "source": "Reuters / The National / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Binladin Group — Worker Exploitation and Mass Layoffs",
        "summary": "Saudi Binladin Group, one of the kingdom's largest contractors (Grand Mosque expansion, King Abdullah Financial District), laid off tens of thousands of workers in 2015-2016 during an economic downturn. Workers went months without pay before being stranded. Some workers burned their buses in protest (2016). Saudi government eventually arranged repatriation flights. The case demonstrated the absence of worker protections during economic downturns.",
        "source": "The Guardian / Reuters / BBC",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Oger — 50,000 Workers Stranded Without Pay (2016-2017)",
        "summary": "Saudi Oger, a major construction and services conglomerate owned by the Hariri family, ceased operations in 2017 owing SAR 30+ billion. An estimated 50,000 workers went months without wages. Workers were stranded in camps without food, water, or electricity. The company's collapse was one of the largest worker abandonment cases in GCC history. Embassies organized emergency repatriation. Many workers never received owed wages.",
        "source": "Reuters / HRW / Amnesty International",
    },
    # ========================================================================
    # 27. Worker Death Statistics Across GCC
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Indian Worker Deaths (2018-2022)",
        "metric": "indian_worker_deaths_saudi",
        "value": "4,400+ over 5 years",
        "summary": "Indian Embassy in Riyadh reported over 4,400 Indian worker deaths in Saudi Arabia between 2018 and 2022. Leading causes include cardiac arrest (suspected heat-related), road accidents, and workplace falls. India is Saudi Arabia's largest labour-source country with 2.5+ million workers. Many deaths go unreported or are attributed to 'natural causes' without investigation.",
        "source": "Indian Embassy Riyadh / Indian Ministry of External Affairs",
    },
    {
        "type": "statistic",
        "jurisdiction": "AE",
        "title": "UAE — Migrant Worker Death Reporting Gaps",
        "metric": "migrant_worker_deaths_uae",
        "value": "No comprehensive data published",
        "summary": "The UAE does not publish comprehensive migrant worker death statistics. Embassy data from India, Pakistan, Bangladesh, and Nepal suggest hundreds of deaths annually. Most deaths attributed to 'natural causes' or 'cardiac arrest.' The absence of official data prevents accountability. HRW and Amnesty have called for transparent, publicly available mortality data for all migrant workers.",
        "source": "HRW / Amnesty International",
    },
    {
        "type": "statistic",
        "jurisdiction": "KW",
        "title": "Kuwait — Indian Worker Deaths (Annual)",
        "metric": "indian_worker_deaths_kuwait",
        "value": "500+ per year",
        "summary": "Indian Embassy in Kuwait reports over 500 Indian worker deaths per year, including suicides, cardiac arrests, road accidents, and workplace injuries. Kuwait's migrant worker population of 2.8 million faces limited occupational health and safety protections. Death investigation procedures are inadequate, with most cases closed as 'natural causes' without thorough inquiry.",
        "source": "Indian Embassy Kuwait",
    },
    # ========================================================================
    # 28. Heat-Related Regulations Across GCC
    # ========================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Midday Outdoor Work Ban",
        "summary": "Saudi Arabia's Royal Decree prohibits outdoor work from noon to 3pm during June, July, and August. Penalty: SAR 3,000-10,000 per violation. However, construction industry reports show widespread non-compliance, especially on smaller sites without government inspection. Workers report being required to work through the ban period with brief breaks. The ban does not use WBGT measurements, relying instead on fixed time periods.",
        "source": "Saudi Ministry of Labour / Migrant-Rights.org",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "AE",
        "title": "UAE — Midday Work Break (Ministerial Resolution No. 401 of 2015)",
        "summary": "UAE's midday work break prohibits outdoor work from 12:30pm to 3:00pm during July and August. Violating companies face fines of AED 5,000-50,000 per worker affected. The ban applies to construction, agriculture, and other outdoor work. Inspectors check compliance but the ban covers only 2 months and 2.5 hours daily — inadequate given that WBGT exceeds safe levels for many more hours. No WBGT-based regulation exists in the UAE.",
        "source": "UAE Ministry of Human Resources and Emiratisation",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "KW",
        "title": "Kuwait — Outdoor Work Ban During Summer",
        "summary": "Kuwait prohibits outdoor work from 11am to 4pm during June, July, and August — the longest ban period in the GCC. Kuwait regularly reaches the highest temperatures in the Gulf (54 degrees Celsius recorded in 2021). Penalty: KWD 100-200 per violation per worker. Compliance monitoring is limited. Construction workers report that some employers require make-up hours in the evening to compensate for the midday ban.",
        "source": "Kuwait Ministry of Social Affairs and Labour",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BH",
        "title": "Bahrain — Outdoor Work Ban and Heat Protections",
        "summary": "Bahrain prohibits outdoor work from noon to 4pm during July and August. Employers must provide water, shade, and rest areas. LMRA conducts inspections with fines of BHD 500-1,000 per violation. Bahrain is smaller than other GCC states, enabling more effective enforcement. However, the ban period is limited to 2 months and does not use WBGT monitoring.",
        "source": "Bahrain LMRA",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "OM",
        "title": "Oman — Summer Outdoor Work Ban",
        "summary": "Oman prohibits outdoor work from 12:30pm to 3:30pm during June, July, and August. Ministerial Decision No. 286/2008. Penalty: OMR 100-500 per violation. Construction workers in Oman's interior (where temperatures exceed 50 degrees Celsius) report limited enforcement. Workers on the Duqm SEZ and other remote projects are particularly vulnerable due to the absence of regular inspections.",
        "source": "Oman Ministry of Manpower",
    },
    # ========================================================================
    # 29. Specific Cases — Worker Abandonment
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Post-World Cup Worker Abandonment Pattern",
        "summary": "Following the December 2022 World Cup conclusion, thousands of workers were laid off by contractors whose projects ended. Workers reported: no end-of-service benefits, visa cancellation with 30-day departure notice, unpaid final months' wages, and no return flights. Workers' Support and Insurance Fund was overwhelmed with claims. Some workers remained in Qatar for months in legal limbo, unable to work or leave.",
        "source": "Migrant-Rights.org / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — 2009 Financial Crisis Worker Abandonment",
        "summary": "During the 2008-2009 global financial crisis, Dubai's construction boom collapsed. Thousands of workers were abandoned by bankrupt contractors: stranded in camps without food, wages, or flights home. Cars were famously abandoned at Dubai airport by fleeing expat employers. Workers had no recourse. The crisis demonstrated the extreme precarity of migrant workers in GCC construction economies.",
        "source": "HRW / The Guardian / New York Times",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Worker Abandonment During Oil Price Drop (2015-2016)",
        "summary": "When oil prices dropped from USD 100 to USD 30 per barrel in 2015-2016, Saudi construction companies faced liquidity crises. An estimated 100,000+ workers across multiple contractors (Saudi Binladin, Saudi Oger, others) went months without pay. Workers lived in camps without electricity or food supplies. Indian, Pakistani, and Bangladeshi embassies organized emergency food distribution and repatriation flights.",
        "source": "Reuters / Bloomberg / Embassy reports",
    },
    # ========================================================================
    # 30. FIFA and Corporate Accountability
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "FIFA World Cup 2022 — Corporate Sponsor Responsibility",
        "summary": "Major FIFA World Cup sponsors including Coca-Cola, Adidas, Visa, Hyundai, and Qatar Airways faced campaigns from labour rights organizations to use their leverage to improve worker conditions. Coca-Cola was the only sponsor to publicly call for a compensation fund. Most sponsors deflected responsibility to FIFA and Qatar authorities. The case highlighted gaps in corporate human rights responsibility for sporting mega-events.",
        "source": "Amnesty International / Sport & Rights Alliance",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "National Team Protests at Qatar 2022 World Cup",
        "summary": "Several national football teams planned protests during the 2022 World Cup. Denmark wore 'toned down' kits from Hummel. Germany players covered mouths before their opening match after FIFA banned 'OneLove' armbands. Australia's Socceroos released a video demanding worker compensation. England's Harry Kane planned to wear a OneLove armband but FIFA threatened yellow cards, forcing compliance. The protests raised global awareness but did not result in tangible remediation.",
        "source": "BBC / The Guardian / FIFA",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Amnesty International — Campaign for Qatar Worker Compensation Fund",
        "summary": "Amnesty International's flagship campaign for a Qatar worker compensation fund demanded FIFA and Qatar establish a minimum USD 440 million fund (matching World Cup prize money) to compensate workers and families for deaths, injuries, wage theft, and recruitment fees. Over 1 million people signed the petition. The campaign was backed by 26 Football Associations. As of 2025, no comprehensive fund has been established by FIFA.",
        "source": "Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Norwegian Football Association — Boycott Debate",
        "summary": "The Norwegian Football Association held a historic vote on whether to boycott the Qatar 2022 World Cup over worker deaths. The motion was narrowly defeated (68-58) at the 2021 extraordinary congress. Players wore 'Human Rights On and Off the Pitch' t-shirts during qualifiers. Norway ultimately failed to qualify. The debate set a precedent for sporting bodies engaging with host country human rights records.",
        "source": "Norwegian Football Association / BBC",
    },
    # ========================================================================
    # 31. ILO Forced Labour Indicators in GCC Construction
    # ========================================================================
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "ILO Forced Labour Indicators Present in GCC Construction",
        "summary": "ILO analysis found multiple forced labour indicators systematically present in GCC construction: (1) deception about working conditions, (2) restriction of movement via passport confiscation, (3) debt bondage through recruitment fees, (4) intimidation and threats of deportation, (5) withholding of wages, (6) abusive working conditions including heat exposure, (7) excessive overtime. The presence of multiple indicators simultaneously constitutes a strong case for forced labour under ILO definitions.",
        "source": "ILO Indicators of Forced Labour / ILO Qatar Office",
    },
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "Qatar — ILO Forced Labour Convention Ratification",
        "summary": "Qatar ratified the ILO Forced Labour Convention (C029) in 1998 and the Protocol of 2014 to the Forced Labour Convention in 2020 — the first Arab state to do so. Ratification commits Qatar to: suppress forced labour, ensure adequate penalties, ensure victims access justice and compensation, and develop a national action plan. ILO monitors implementation through the technical cooperation programme.",
        "source": "ILO NORMLEX / Qatar Ministry of Labour",
    },
    # ========================================================================
    # 32. Subcontracting Chains
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Multi-Tier Subcontracting and Labour Exploitation",
        "summary": "Construction in Qatar typically involves 3-5 tiers of subcontracting. Main contractors (e.g., Salini-Impregilo, Samsung, QDVC) subcontract to regional firms, which further subcontract to smaller companies. Workers at the bottom of the chain face the worst conditions: lowest wages, most delayed payments, no safety equipment, and no access to main contractor grievance mechanisms. Supreme Committee standards applied only to direct and first-tier subcontractors.",
        "source": "BWI / ILO / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Subcontracting and Labour Exploitation in Dubai Construction",
        "summary": "Dubai's construction boom (2000-present) operates through deep subcontracting chains. Main contractor profit margins are maintained by squeezing subcontractor costs, which are passed down to workers as lower wages and worse conditions. When disputes arise, main contractors deny responsibility for subcontractor labour practices. UAE law does not establish joint liability for main contractors over subcontractor workers.",
        "source": "HRW / Construction industry analysis",
    },
    # ========================================================================
    # 33. Gender and Construction
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Women Workers in World Cup Hospitality Infrastructure",
        "summary": "While construction sites were predominantly male, women workers from Philippines, India, and Nepal were employed in World Cup hospitality and cleaning services. These workers faced gender-specific exploitation: live-in accommodation requirements creating dependency, sexual harassment with no reporting mechanism, and wage theft. Women domestic workers cleaning World Cup hotels were governed by the weaker Domestic Workers Law rather than the Labour Law.",
        "source": "HRW / ILO",
    },
    # ========================================================================
    # 34. Legal Proceedings and International Cases
    # ========================================================================
    {
        "type": "court_ruling",
        "jurisdiction": "QA",
        "title": "Swiss Court Complaint Against FIFA for Worker Deaths (2016)",
        "summary": "In 2016, the Dutch trade union FNV filed a complaint to the OECD National Contact Point in Switzerland against FIFA for failing to address human rights abuses of migrant workers in Qatar. The Swiss NCP mediated and FIFA agreed to implement human rights commitments. However, enforceability of NCP recommendations is limited. Separately, a complaint under Swiss criminal law was filed but Swiss prosecutors declined to pursue the case.",
        "source": "OECD NCP Switzerland / FNV / BWI",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "QA",
        "title": "French Investigation into Vinci Construction's Qatar Operations",
        "summary": "French construction giant Vinci (through its Qatari subsidiary QDVC — Qatar Diar Vinci Construction) was investigated by French prosecutors for forced labour after a 2015 complaint by Sherpa and Comite Contre l'Esclavage Moderne. Workers alleged passport confiscation, excessive working hours, and cramped housing. French courts dismissed the case in 2018, finding insufficient evidence of Vinci parent company's direct involvement in subsidiary practices.",
        "source": "Sherpa / French judiciary / The Guardian",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "UK Parliament Report on Qatar World Cup Worker Rights",
        "summary": "UK Parliament's Business, Energy and Industrial Strategy Committee (2021) published a report on worker rights in Qatar, concluding that 'serious concerns remain about the treatment of migrant workers.' The report recommended that UK-listed companies operating in Qatar publish human rights due diligence assessments and that FIFA be held accountable for worker conditions. The report had no binding force.",
        "source": "UK Parliament BEIS Committee",
    },
    # ========================================================================
    # 35. Media Investigations and Reporting
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "DW Documentary — Qatar's Migrant Workers' Conditions (2022)",
        "summary": "Deutsche Welle produced a documentary in 2022 featuring undercover footage from Qatar labour camps and construction sites showing overcrowded rooms, unsafe working conditions, and workers describing wage theft and passport confiscation. The documentary was broadcast globally ahead of the World Cup, contributing to public awareness. Qatar's Government Communications Office disputed the documentary's framing.",
        "source": "Deutsche Welle (DW)",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "BBC Investigation — Qatar World Cup Worker Deaths (2021)",
        "summary": "BBC Panorama conducted an investigation into Qatar World Cup worker deaths, interviewing families of deceased workers in Nepal and Bangladesh. Families described receiving phone calls informing them of their relative's death with no explanation, bodies returned without autopsy reports, and minimal or no compensation. The programme highlighted the human cost behind the statistics and called for mandatory death investigation reform.",
        "source": "BBC Panorama",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Equidem Research — Worker Voices from Qatar (2022)",
        "summary": "Equidem, a labour rights research organization, conducted surveys of over 1,000 migrant workers in Qatar in 2022. Findings: 82 percent reported paying recruitment fees, 58 percent had passports confiscated, 41 percent experienced wage theft, 38 percent reported working during the outdoor work ban, and 25 percent had experienced threats of deportation for complaining. The survey provided quantitative evidence of exploitation patterns at scale.",
        "source": "Equidem",
    },
    # ========================================================================
    # 36. Post-World Cup Legacy and Reform Trajectory
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Post-World Cup Reform Backsliding Risk",
        "summary": "Human rights organizations expressed concern that Qatar's reform momentum would stall after the World Cup ended. The ILO technical cooperation programme was scheduled to conclude. International media attention shifted. Workers' organizations noted that enforcement of reforms depended on sustained international scrutiny. Migrant-Rights.org documented cases of reform rollback: increased processing times for job transfers, fewer labour inspections, and reduced WSIF claim approvals.",
        "source": "Amnesty International / Migrant-Rights.org / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Supreme Committee Dissolution (2023)",
        "summary": "The Supreme Committee for Delivery & Legacy — which oversaw worker welfare standards on stadium projects — was dissolved after the World Cup. Its Workers' Welfare team, which monitored conditions and responded to complaints, ceased operations. No comparable oversight body exists for Qatar's ongoing construction sector. The dissolution raised concerns about loss of institutional capacity for worker protection.",
        "source": "Supreme Committee / Migrant-Rights.org",
    },
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "Amnesty International — 2024 Assessment of Qatar Reforms",
        "summary": "Amnesty International's 2024 assessment found Qatar's reforms 'remain inadequate and unevenly implemented.' Key concerns: absconding charges still used as retaliation, domestic workers still face serious gaps in protection, death investigation reform has not materialized, no comprehensive compensation programme for workers or families, and WPS coverage excludes domestic workers. Amnesty called on Qatar to ensure reforms survive the post-World Cup era.",
        "source": "Amnesty International Annual Report 2024",
    },
    # ========================================================================
    # 37. Saudi Arabia — Specific Construction Cases
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Mecca Grand Mosque Crane Collapse (2015)",
        "summary": "In September 2015, a crane operated by Saudi Binladin Group collapsed onto the Grand Mosque in Mecca, killing 111 people and injuring 394 (mostly pilgrims, not workers). The incident raised questions about construction safety standards. Saudi Binladin Group was temporarily suspended from new government contracts. An investigation found the crane was not properly secured in high winds. The collapse occurred during a massive expansion project employing tens of thousands of workers.",
        "source": "Reuters / Saudi Gazette / BBC",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Jeddah Tower (Kingdom Tower) Worker Conditions",
        "summary": "Jeddah Tower, planned as the world's tallest building at 1km, employed thousands of workers before construction stalled in 2018 after the arrest of developer Prince Al-Waleed bin Talal. Workers reported standard GCC exploitation conditions: 12-hour shifts, 45+ degree heat, delayed wages, and crowded camps. Construction remained stalled as of 2024, leaving some project workers in contractual limbo.",
        "source": "Construction industry reports / Migrant-Rights.org",
    },
    # ========================================================================
    # 38. UAE — Additional Construction Cases
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Dubai — Palm Jumeirah Construction Worker Exploitation",
        "summary": "Palm Jumeirah, Dubai's iconic artificial island (2001-2006 construction), was built by approximately 40,000 workers from South Asia. Workers on the marine and land reclamation project faced extreme conditions: exposure to heat and humidity, long shifts on construction barges, and camp accommodation 1-2 hours from the site. Worker death toll during construction has never been officially disclosed. Contractor Nakheel faced labour complaints but the project predated modern scrutiny of GCC labour practices.",
        "source": "HRW / Construction industry reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Abu Dhabi — Al Reem Island Construction Worker Deaths",
        "summary": "Al Reem Island, a major Abu Dhabi development with 80+ residential towers, saw multiple worker deaths during construction from falls, crane accidents, and heat exposure. Workers reported unsafe scaffolding, missing harnesses, and pressure to meet tight deadlines. Abu Dhabi Department of Municipal Affairs conducted inspections but penalties for safety violations were minimal. No comprehensive worker death tally was published.",
        "source": "The National / Business & Human Rights Resource Centre",
    },
    # ========================================================================
    # 39. GCC-Wide Reform Assessment
    # ========================================================================
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "FairSquare Projects — GCC Labour Reform Comparison (2024)",
        "summary": "FairSquare Projects' 2024 comparative assessment ranked GCC labour reforms: Qatar leads on legislative reform (NOC abolished, minimum wage, WPS), Bahrain leads on worker mobility (flexi-permit), UAE improved job mobility (2022 law), Saudi Arabia's reforms are limited (exclude domestic workers), Kuwait and Oman lag significantly. All GCC states maintain prohibition on unions and collective bargaining for migrant workers.",
        "source": "FairSquare Projects",
    },
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "Business & Human Rights Resource Centre — GCC Construction Tracker",
        "summary": "The Business & Human Rights Resource Centre maintains a GCC Migrant Workers tracker documenting labour rights allegations against specific companies. As of 2024, the tracker contained over 400 entries involving major international and regional contractors. Companies are invited to respond to allegations, with response rates below 40 percent. The tracker provides the most comprehensive publicly available database of GCC construction labour rights cases.",
        "source": "Business & Human Rights Resource Centre",
    },
    # ========================================================================
    # 40. Worker Compensation and Remediation
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Death Compensation Under Labour Law",
        "summary": "Qatar Labour Law provides for death compensation (diya) equivalent to 3 years' basic salary for work-related deaths. However, the classification of most deaths as 'natural causes' means families cannot claim work-related compensation. For a worker earning minimum wage (QAR 1,000/month), 3 years equals QAR 36,000 (USD 9,890). For the 6,500+ worker deaths, estimated total compensation liability would exceed USD 60 million, which has never been paid comprehensively.",
        "source": "Qatar Labour Law / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Worker Families' Struggle for Information and Justice",
        "summary": "Families of workers who died in Qatar report extraordinary difficulty obtaining basic information: death certificates arrive in Arabic without translation, autopsy details are not provided, employers do not communicate, and embassies have limited capacity. The process of claiming compensation requires legal proceedings in Qatar, which families in Nepal, Bangladesh, or India cannot afford or access. Many families never learn how their relatives died.",
        "source": "Amnesty International / BBC Panorama",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar Workers' Support and Insurance Fund — Claims Statistics (2023)",
        "metric": "wsif_claims_processed",
        "value": "36,000+",
        "summary": "The Workers' Support and Insurance Fund processed over 36,000 claims from 2018 to 2023, disbursing QAR 1.8 billion. Average claim value: QAR 50,000 (USD 13,700). Fund covers unpaid wages and end-of-service benefits. Processing time: 3-6 months. Workers must file in Qatar, excluding those already repatriated. The fund represents an important mechanism but covers only a fraction of affected workers.",
        "source": "Qatar Ministry of Labour / ILO",
    },
    # ========================================================================
    # 41. GCC Construction Safety Standards
    # ========================================================================
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "Qatar — Construction Safety Regulations (Ministerial Decision No. 16 of 2007)",
        "summary": "Qatar's construction safety regulations require: fall protection for work above 2 metres, personal protective equipment provision, scaffolding inspection certificates, crane operator licensing, and excavation shoring. Penalties for violations range from project suspension to criminal prosecution. In practice, enforcement is inconsistent: major government and Supreme Committee projects are regularly inspected, while private construction sites see far fewer inspections.",
        "source": "Qatar Ministry of Labour / BWI",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Labour Inspection Capacity",
        "metric": "labour_inspectors",
        "value": "Approximately 400 inspectors for 2 million+ workers",
        "summary": "Qatar employs approximately 400 labour inspectors to oversee conditions for over 2 million migrant workers — a ratio of 1 inspector per 5,000 workers. ILO recommends 1 per 10,000 for developing economies, suggesting Qatar's ratio should be adequate. However, the complexity of multi-site construction, subcontracting chains, and remote camp locations means effective coverage is far lower than the ratio suggests.",
        "source": "Qatar Ministry of Labour / ILO",
    },
    # ========================================================================
    # 42. Bilateral Labour Agreements
    # ========================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Bilateral Labour Agreements with Source Countries",
        "summary": "Qatar has signed bilateral labour agreements with India, Nepal, Bangladesh, Sri Lanka, Pakistan, Philippines, Indonesia, and others. Agreements typically cover: recruitment fee prohibition, contract standardization, dispute resolution mechanisms, and worker welfare provisions. ILO analysis found implementation varies widely: agreements with strong enforcement provisions (Philippines-Qatar) produce better outcomes than those without (Nepal-Qatar).",
        "source": "ILO / Qatar Ministry of Labour",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Bilateral Agreements and Enforcement Gaps",
        "summary": "Saudi Arabia has bilateral labour agreements with over 20 source countries. However, enforcement is minimal: origin country embassies have limited consular capacity (Indian Embassy Riyadh has 6 labour attaches for 2.5 million workers), Saudi enforcement agencies prioritize employer interests, and workers are often unaware of protections under bilateral agreements. The agreements function more as diplomatic instruments than worker protection mechanisms.",
        "source": "Indian Embassy Riyadh / ILO / FairSquare Projects",
    },
    # ========================================================================
    # 43. Mental Health Impact
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Migrant Worker Mental Health Crisis",
        "summary": "Studies document severe mental health impacts on GCC construction workers: depression, anxiety, PTSD, and suicidal ideation linked to isolation, debt stress, heat exhaustion, homesickness, and exploitation. Qatar's Hamad Medical Corporation reported increasing mental health presentations among migrant workers. No dedicated mental health services for migrant workers existed during World Cup construction. Workers who report mental health issues risk being deemed 'unfit for work' and deported.",
        "source": "ILO / Hamad Medical Corporation / The Lancet",
    },
    # ========================================================================
    # 44. Supply Chain and Corporate Due Diligence
    # ========================================================================
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "UN Guiding Principles — Application to Mega-Event Construction",
        "summary": "The UN Guiding Principles on Business and Human Rights (2011) require companies to conduct human rights due diligence throughout their value chain. For mega-events like the Qatar World Cup, this extends to: event organizers (FIFA), sponsors, broadcasters, contractors, and subcontractors. The John Ruggie report (2016) recommended FIFA require human rights impact assessments for all future host bids. FIFA adopted a human rights policy in 2017 but enforcement for Qatar was retrospective and limited.",
        "source": "UN Guiding Principles / Ruggie Report (2016) / FIFA",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar World Cup — Supply Chain Audit Failures",
        "summary": "Third-party audits of World Cup construction supply chains (commissioned by the Supreme Committee) found persistent non-compliance among subcontractors despite remediation plans. PwC, AECOM, and Impactt conducted audits that identified: recruitment fee charging (78 percent of sampled workers paid fees), wage discrepancies (25 percent paid below contract rates), and passport confiscation (40 percent of subcontractor workers). Audit follow-up action was limited and rarely resulted in contract termination.",
        "source": "Supreme Committee Audit Reports / BWI / Amnesty International",
    },
    # ========================================================================
    # 45. Additional Qatar World Cup Specifics
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — World Cup Fan Zone and Temporary Infrastructure Workers",
        "summary": "Thousands of workers built temporary fan zones, training sites, and hospitality infrastructure for the World Cup that were dismantled after the tournament. These workers had no Supreme Committee welfare oversight. Many were employed on short-term contracts with no end-of-service benefits. Post-tournament, temporary infrastructure workers were among the first laid off, often without final salary payment.",
        "source": "Migrant-Rights.org / BWI",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Hamad International Airport Expansion Worker Conditions",
        "summary": "Hamad International Airport expansion for the World Cup employed over 15,000 workers. The project, managed by Qatar Airways and the New Doha International Airport Steering Committee, was outside Supreme Committee jurisdiction. Workers reported 12-hour shifts, wage delays, and cramped accommodation. At least 2 worker deaths were reported during the expansion phase but details were not publicly disclosed.",
        "source": "BWI / Construction industry reports",
    },
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Total Migrant Worker Population (2022)",
        "metric": "total_migrant_workers",
        "value": "2.0 million+",
        "summary": "Qatar's total migrant worker population at the time of the 2022 World Cup exceeded 2 million, constituting approximately 95 percent of the private sector workforce and 88 percent of the total population. Workers came from over 100 countries, with the largest contingents from India, Nepal, Bangladesh, Philippines, and Egypt. Migrant workers are excluded from citizenship regardless of length of residency.",
        "source": "Qatar Planning and Statistics Authority / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Security Guard Exploitation During World Cup",
        "summary": "Security guards deployed at World Cup venues worked 12-hour shifts for 30 consecutive days without rest. Many were recruited from Kenya, Uganda, and Nepal specifically for the tournament. Workers reported being told they would earn QAR 2,500/month but received QAR 1,200. Some guards had their phones confiscated during shifts to prevent documentation of conditions. Post-tournament, contracts were terminated without notice.",
        "source": "Equidem / The Guardian",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — FIFA World Cup Legacy Foundation Shortcomings",
        "summary": "FIFA established the FIFA World Cup Qatar 2022 Legacy Fund but allocated no funding to worker compensation or remediation. The fund focused on football development in the region. Amnesty International criticized this as a missed opportunity, noting that legacy programmes that ignore the human cost of construction are 'legacy-washing.' The fund's total allocation was not publicly disclosed.",
        "source": "FIFA / Amnesty International",
    },
    # ========================================================================
    # 46. Additional Saudi Arabia Cases
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Diriyah Gate Project Worker Conditions",
        "summary": "Diriyah Gate, a USD 20 billion heritage and entertainment district near Riyadh, employed 30,000+ workers at peak construction. Workers building luxury hotels, museums, and residences on the UNESCO heritage site reported familiar exploitation patterns: wage delays, 12-14 hour shifts, inadequate heat protection, and cramped temporary camps in desert locations far from medical facilities.",
        "source": "Business & Human Rights Resource Centre / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — King Abdullah Financial District Worker Exploitation",
        "summary": "The King Abdullah Financial District (KAFD) in Riyadh, a massive mixed-use development, saw repeated labour disputes during its protracted construction (2006-2023). Workers employed by multiple contractors including Saudi Binladin Group went months without pay during construction delays. The project changed hands multiple times, leaving workers in contractual uncertainty about which entity was responsible for their wages.",
        "source": "Reuters / Construction industry reports",
    },
    {
        "type": "statistic",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Nitaqat Saudization Impact on Migrant Workers",
        "metric": "saudization_displaced_workers",
        "value": "Hundreds of thousands",
        "summary": "Saudi Arabia's Nitaqat (Saudization) programme requires companies to employ minimum percentages of Saudi nationals. While not targeting construction (which is exempt), the programme affects service and hospitality workers. Workers displaced by Saudization requirements face deportation if they cannot find alternative sponsors within 60 days. The programme has resulted in mass deportation of undocumented workers, particularly Ethiopian and Yemeni nationals.",
        "source": "Saudi Ministry of Human Resources / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Ethiopian Worker Mass Deportation (2013, 2017, 2022)",
        "summary": "Saudi Arabia conducted mass deportation campaigns targeting undocumented Ethiopian workers in 2013 (160,000+ deported), 2017 (60,000+), and 2022 (100,000+). Workers were detained in overcrowded deportation centres where Amnesty International and HRW documented severe abuse: beatings, sexual violence, denial of food and water, and deaths in custody. Many deported workers had entered Saudi Arabia legally but lost status when employers failed to renew permits.",
        "source": "Amnesty International / HRW / IOM",
    },
    # ========================================================================
    # 47. Additional UAE Cases
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Dubai — World Islands and Maritime Construction Worker Deaths",
        "summary": "The World Islands, Dubai's artificial archipelago, required extensive marine construction with workers operating on barges, dredgers, and in water. Workers from South Asia reported dangerous conditions: lack of life jackets, 14-hour marine shifts, exposure to extreme sun on open water, and inadequate swimming training. Worker deaths from drowning and heat stroke during the 2003-2008 construction phase were not officially disclosed.",
        "source": "HRW / Construction industry reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Abu Dhabi — Etihad Towers and Corniche Development Worker Conditions",
        "summary": "Construction of Abu Dhabi's luxury Etihad Towers complex and wider Corniche development involved thousands of migrant workers facing standard UAE exploitation patterns. Workers were transported 1-2 hours each way from remote Mussafah labour camps to Corniche construction sites. 14-16 hour days including transport left workers with minimal rest. Contractor Arabtec (pre-collapse) faced repeated complaints.",
        "source": "Migrant-Rights.org / The National",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Free Zone Labour Exploitation",
        "summary": "Workers in UAE free zones (JAFZA, DAFZA, SAIF Zone, etc.) fall under different regulatory frameworks than mainland UAE. Some free zones have weaker labour protections or enforcement. Construction workers building free zone infrastructure reported confusion about which authority handles complaints. Free zone companies sometimes exploit this regulatory ambiguity to avoid compliance with mainland labour standards.",
        "source": "Migrant-Rights.org / Business & Human Rights Resource Centre",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Dubai — Museum of the Future Construction Worker Exploitation",
        "summary": "The Museum of the Future, Dubai's landmark torus-shaped building (completed 2022), required highly specialized construction techniques. While skilled workers were better paid, lower-tier labourers performing support roles reported standard exploitation: recruitment fee debt, contract substitution, and passport confiscation. The building was marketed as a symbol of innovation while being built under conditions common to GCC construction.",
        "source": "Equidem / Construction industry reports",
    },
    # ========================================================================
    # 48. Additional Kuwait and Bahrain Cases
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "title": "Kuwait — Jaber Al-Ahmad Al-Sabah Causeway Worker Deaths",
        "summary": "The Sheikh Jaber Al-Ahmad Al-Sabah Causeway (36km, completed 2019), one of the world's longest bridges, employed thousands of workers in marine and road construction. Workers reported harsh conditions on exposed sea platforms in extreme heat. At least 6 worker deaths were reported during construction. Workers employed by subcontractors had limited access to safety equipment and medical facilities.",
        "source": "Kuwait Times / Construction industry reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "title": "Kuwait — Free Visa System and Construction Sector",
        "summary": "Kuwait's 'free visa' (visa trading) system allows sponsors to bring workers into the country and then release them to work for others in exchange for monthly payments. An estimated 300,000 workers in Kuwait operate on free visas, many in construction. These workers have no formal employer, cannot access labour courts, and are vulnerable to arrest. Kuwait's government has struggled to eliminate the practice despite repeated crackdowns.",
        "source": "Migrant-Rights.org / Kuwait Times",
    },
    {
        "type": "case_study",
        "jurisdiction": "BH",
        "title": "Bahrain — Construction Worker Falls and Safety Standards",
        "summary": "Falls from height are the leading cause of construction worker deaths in Bahrain. The LMRA reported 15-20 construction worker deaths annually, predominantly from falls, crane accidents, and electrocution. Bahrain's Construction Safety Code (2016) requires fall protection above 1.8 metres but enforcement is inconsistent. Workers on smaller residential construction sites report no safety equipment or training.",
        "source": "Bahrain LMRA / Gulf Daily News",
    },
    # ========================================================================
    # 49. Additional Oman Cases
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "OM",
        "title": "Oman — Muscat International Airport Expansion Worker Conditions",
        "summary": "Muscat International Airport expansion (completed 2018, new terminal for 20 million passengers) employed thousands of workers. Contractors including Bechtel and Turkish firm TAV reported meeting international safety standards, but subcontractor workers described standard GCC exploitation: 12-hour shifts, shared accommodation for 8-10 workers per room, and wage delays. Oman's labour inspectorate conducted limited site visits.",
        "source": "Migrant-Rights.org / Construction industry reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "OM",
        "title": "Oman — Road Construction Worker Deaths in Interior Regions",
        "summary": "Workers building highways connecting Oman's interior regions (Muscat-Salalah highway, Adam-Haima road) face extreme isolation and heat. Summer temperatures in Oman's interior exceed 50 degrees Celsius. Workers housed in temporary camps in desert locations have minimal access to medical facilities. Road construction worker deaths are not systematically tracked. Workers from Bangladesh and India constitute the majority of Oman's road construction workforce.",
        "source": "Migrant-Rights.org / Oman construction sector data",
    },
    # ========================================================================
    # 50. COVID-19 Additional GCC Impact
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — COVID-19 Infections Among Migrant Workers (2020)",
        "metric": "migrant_worker_covid_infections",
        "value": "40,000+",
        "summary": "Qatar reported over 40,000 COVID-19 infections among migrant workers in the Industrial Area and labour camps during 2020. The infection rate among migrant workers was significantly higher than the general population due to overcrowded living conditions making social distancing impossible. Qatar converted field hospitals and deployed testing in camps but the initial response was criticized as slow.",
        "source": "Qatar Ministry of Public Health / HRW",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "title": "Kuwait — COVID-19 and Migrant Worker Detention",
        "summary": "During COVID-19, Kuwait detained thousands of irregular migrant workers in overcrowded facilities. Workers who lost jobs during lockdowns and could not afford return flights became undocumented. Detention centres in Talha and other locations held workers in conditions that HRW described as 'inhuman.' Kuwait organized some repatriation flights but workers from countries without bilateral agreements faced extended detention.",
        "source": "HRW / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "OM",
        "title": "Oman — COVID-19 Impact on Construction Workers",
        "summary": "Oman placed several industrial and labour camp areas under lockdown during COVID-19. Construction workers in Duqm SEZ and Sohar Industrial Zone were confined to camps without pay for weeks. Workers from India and Bangladesh reported being unable to contact embassies or access medical care. Oman organized limited repatriation flights but thousands of workers remained stranded for months.",
        "source": "Migrant-Rights.org / Times of Oman",
    },
    # ========================================================================
    # 51. Wage Theft Patterns
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Wage Theft Scale Estimation (Pre-Reform)",
        "metric": "estimated_wage_theft",
        "value": "USD 1.4 billion annually (pre-WPS estimate)",
        "summary": "FairSquare Projects estimated that wage theft in Qatar amounted to approximately USD 1.4 billion annually before the Wage Protection System was implemented. This includes: partial non-payment, delayed payment exceeding 2 months, deductions not authorized in contracts, and non-payment of overtime. Post-WPS implementation reduced the scale but did not eliminate the problem, particularly for workers outside WPS coverage.",
        "source": "FairSquare Projects / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Wage Theft in Dubai Construction During Economic Cycles",
        "summary": "Dubai's construction sector experiences cyclical wage theft patterns: during economic booms, contractors delay payments while pursuing new contracts; during downturns, contractors default entirely. Workers have no priority in bankruptcy proceedings. The UAE's Wage Protection System (introduced 2009) has improved on-time payment but does not cover all sectors and enforcement is inconsistent. Workers earning below AED 2,000/month are most vulnerable.",
        "source": "Migrant-Rights.org / UAE Ministry of Human Resources",
    },
    # ========================================================================
    # 52. International Pressure and Advocacy
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "ITUC — Annual Worst Countries List and GCC States",
        "summary": "The International Trade Union Confederation's Global Rights Index consistently rates GCC states among the world's worst for workers' rights. Qatar, Saudi Arabia, and the UAE are regularly classified as 'No Guarantee of Rights' (Category 5) or 'No Guarantee of Rights due to Breakdown of Rule of Law' (Category 5+). The ratings reflect: prohibition of trade unions, criminalization of strikes, kafala restrictions, and migrant worker exploitation.",
        "source": "ITUC Global Rights Index",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "US State Department TIP Report — GCC Country Ratings",
        "summary": "The US State Department's Trafficking in Persons (TIP) Report rates GCC states on a 4-tier system. Qatar: Tier 2 (does not fully meet minimum standards but making efforts). Saudi Arabia: Tier 2 Watch List. UAE: Tier 2. Kuwait: Tier 2. Bahrain: Tier 2. Oman: Tier 2. The TIP Report specifically identifies construction sector forced labour, debt bondage, and kafala-related exploitation in each country's assessment.",
        "source": "US State Department Trafficking in Persons Report",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "European Parliament — Resolution on Migrant Workers in GCC (2024)",
        "summary": "The European Parliament adopted a resolution in 2024 calling on GCC states to: fully abolish kafala systems, implement living wages, ensure freedom of association for migrant workers, establish transparent death reporting, and create effective remediation mechanisms. The resolution specifically referenced the Qatar World Cup deaths. EU member states were urged to raise labour rights in bilateral trade discussions with GCC states.",
        "source": "European Parliament",
    },
    # ========================================================================
    # 53. Insurance and Health Coverage
    # ========================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Mandatory Health Insurance for Migrant Workers",
        "summary": "Qatar requires employers to provide health insurance for all migrant workers covering basic medical care, emergency treatment, and hospitalization. The Supreme Committee required enhanced coverage including mental health screening for stadium workers. In practice, many workers report difficulty accessing healthcare: clinics are distant from camps, employers discourage time off for medical visits, and workers fear being deemed medically unfit and deported.",
        "source": "Qatar Ministry of Public Health / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — GOSI Work Injury Insurance Gaps",
        "summary": "Saudi Arabia's General Organization for Social Insurance (GOSI) provides work injury insurance, but coverage requires proper documentation that many workers lack. Workers injured on construction sites must prove the injury was work-related, which employers may dispute. Domestic workers are excluded from GOSI. Workers who are injured and cannot work are often terminated and deported before claims are processed.",
        "source": "Saudi GOSI / HRW",
    },
    # ========================================================================
    # 54. Accommodation Standards
    # ========================================================================
    {
        "type": "regulation_change",
        "jurisdiction": "QA",
        "title": "Qatar — Workers' Accommodation Standards (Ministerial Decision No. 18 of 2014)",
        "summary": "Qatar's Ministerial Decision No. 18 of 2014 sets accommodation standards: maximum 4 workers per room, minimum 6 sq meters per person, air conditioning, clean water, sanitation facilities (1 per 6 workers), kitchen, recreation areas, and fire safety. Compliance improved on new-build camps but existing Industrial Area camps remained below standard. Labour inspections found 40 percent of accommodation failed to meet at least one standard in 2021.",
        "source": "Qatar Ministry of Labour / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Sonapur Labour Camp Conditions in Dubai",
        "summary": "Sonapur ('City of Gold'), the largest labour camp in Dubai housing over 200,000 workers, has been documented by journalists and NGOs as overcrowded and poorly maintained. Workers share rooms designed for 6 among 12 people. The camp is located 30km from central Dubai. Basic amenities including consistent water supply and waste management have been issues. Dubai Municipality conducts inspections but the scale of the camp makes comprehensive monitoring difficult.",
        "source": "HRW / Vice News / The Guardian",
    },
    # ========================================================================
    # 55. Origin Country Perspectives
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Nepal — Families of Deceased Qatar Workers Seek Answers",
        "summary": "In rural Nepal, thousands of families lost breadwinners to unexplained deaths in Qatar. Many received bodies with death certificates in Arabic listing 'cardiac arrest' and no further explanation. Families who took loans for recruitment fees now face debt without income. Nepal's Foreign Employment Board compensation (NPR 700,000 / USD 5,300) requires proving the death was work-related, which most families cannot do. A class of 'World Cup widows' has emerged in districts like Kaski, Gorkha, and Jhapa.",
        "source": "Amnesty International / BBC / Nepali Times",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Bangladesh — Returnee Workers from Qatar with Occupational Injuries",
        "summary": "Workers returning to Bangladesh from Qatar construction jobs frequently report chronic health conditions: kidney disease from dehydration, respiratory issues from dust exposure, musculoskeletal injuries from heavy lifting, and PTSD. Bangladesh's healthcare system is ill-equipped to treat occupational diseases. Workers do not receive post-employment health coverage from Qatar employers. BRAC's Migration Programme documented hundreds of returnees requiring medical care they could not afford.",
        "source": "BRAC Migration Programme / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "India — Kerala Recruitment Agent Networks for Gulf Construction",
        "summary": "Kerala, a major labour-sending state, channels hundreds of thousands of workers to GCC construction through a network of licensed and unlicensed recruitment agents. Licensed agencies charge INR 50,000-150,000 (USD 600-1,800) despite the legal cap of INR 30,000. Unlicensed sub-agents in rural areas charge more. Workers from Malappuram, Thrissur, and Palakkad districts are particularly vulnerable. Kerala's NORKA-ROOTS programme assists returnees but cannot prevent recruitment fraud.",
        "source": "Kerala NORKA-ROOTS / Indian Ministry of External Affairs",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Philippines — POEA Pre-Deployment Briefing and Realities in Qatar",
        "summary": "The Philippine Overseas Employment Administration (POEA, now DMW) requires pre-departure orientation for workers going to Qatar. Briefings cover rights under Qatari law and the bilateral agreement. However, workers report that actual conditions upon arrival differ dramatically from briefings: lower wages, different job roles, and working conditions not matching promises. The Philippines' stronger diplomatic stance relative to other origin countries provides somewhat better protection for Filipino workers.",
        "source": "Philippine DMW (formerly POEA) / Migrant Forum in Asia",
    },
    # ========================================================================
    # 56. Construction Technology and Worker Safety
    # ========================================================================
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Technology Monitoring of Worker Health on Stadium Sites",
        "summary": "The Supreme Committee piloted wearable technology to monitor worker heart rate, body temperature, and hydration levels on stadium sites. The pilot covered 500 workers and successfully identified workers at risk of heat stress before collapse. However, the technology was not scaled to the full workforce. Privacy concerns were raised about employers accessing health data. Post-World Cup, no mandate exists for continued use of worker health monitoring technology.",
        "source": "Supreme Committee for Delivery & Legacy / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — AI and Drone Inspection on Construction Sites",
        "summary": "Some UAE construction projects have deployed AI-powered camera systems and drones to monitor safety compliance. While these technologies can detect workers without harnesses or in restricted zones, they are primarily used to increase productivity rather than protect worker welfare. Workers report that surveillance technology is used to monitor work speed and breaks rather than safety. The dual-use nature of construction technology raises questions about worker privacy and power dynamics.",
        "source": "Construction Technology Review / Migrant-Rights.org",
    },
    # ========================================================================
    # 57. Trade Union and Collective Action
    # ========================================================================
    {
        "type": "advisory",
        "jurisdiction": "QA",
        "title": "GCC-Wide — Prohibition of Trade Unions for Migrant Workers",
        "summary": "No GCC state allows migrant workers to form or join trade unions. Qatar allows 'joint committees' but migrants cannot chair them. Saudi Arabia prohibits all unions. UAE allows citizens-only unions in some sectors. Kuwait allows unions but excludes domestic workers and migrants in many sectors. Bahrain has the most permissive framework but still restricts migrant worker participation. The prohibition of collective bargaining is a fundamental structural barrier to worker protection.",
        "source": "ILO Committee on Freedom of Association / ITUC",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "BWI — Construction Workers' Union Advocacy for Qatar Reform",
        "summary": "Building and Wood Workers' International (BWI), the global union federation for construction workers, has been the most active international labour body on Qatar World Cup issues. BWI conducted multiple investigation missions, submitted complaints to the ILO, and engaged directly with the Supreme Committee and FIFA. BWI's advocacy contributed to the establishment of Workers' Welfare Standards and grievance mechanisms on stadium sites, though BWI assessed implementation as insufficient.",
        "source": "BWI",
    },
    # ========================================================================
    # 58. Environmental and Occupational Health
    # ========================================================================
    {
        "type": "statistic",
        "jurisdiction": "QA",
        "title": "Qatar — Occupational Injury Reporting on Construction Sites",
        "metric": "reported_injuries_annual",
        "value": "13,000+ (2022)",
        "summary": "Qatar's Ministry of Labour recorded over 13,000 occupational injuries on construction sites in 2022. Common injuries include falls from height (28 percent), struck-by-object (22 percent), equipment accidents (18 percent), and heat-related collapse (15 percent). Under-reporting is estimated at 40-60 percent due to workers fearing job loss or deportation for reporting injuries. Fatal injuries officially numbered 50 but the true toll is disputed.",
        "source": "Qatar Ministry of Labour / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Silicosis and Respiratory Disease in Construction Workers",
        "summary": "Construction workers in Qatar are exposed to silica dust from concrete cutting, sandblasting, and demolition without adequate respiratory protection. Long-term silica exposure causes silicosis, an irreversible lung disease. Workers on 2-year contracts may not develop symptoms until returning home, where the occupational link cannot be established. No GCC state conducts post-employment health screening or provides long-term occupational disease compensation for former migrant workers.",
        "source": "ILO / Journal of Occupational Medicine",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Future Mega-Event Construction and Continued Worker Risks",
        "summary": "Qatar's hosting of future international events including the 2030 Asian Games requires new sports venue and infrastructure construction. Labour rights organizations warned that without sustained reform enforcement, exploitation patterns from the World Cup era will repeat. The dissolution of the Supreme Committee removed the only dedicated worker welfare oversight body for mega-event construction. ILO recommended establishing a permanent independent labour monitoring body before the next wave of megaproject construction begins.",
        "source": "Amnesty International / ILO / Migrant-Rights.org",
    },
]
