"""Gray area legal practices — the boundary between legitimate employment and exploitation.

This module catalogs documented cases, laws, court rulings, and academic research
on practices that are TECHNICALLY LEGAL but create conditions ripe for exploitation
of migrant and vulnerable workers. These are the hardest cases for LLM safety
systems to evaluate because they sit at the intersection of lawful business
practices and trafficking indicators.

Categories covered:
  - Unpaid internship exploitation (Glatt v. Fox Searchlight, DOL Fact Sheet #71)
  - Visa sponsorship wage suppression (H-1B under-leveling, Tier 2 dependency)
  - "Voluntary" overtime culture (karoshi, TITP overtime, ILO conventions)
  - Tied accommodation (H-2A housing, UK gangmaster provisions, Qatar WPS)
  - Apprenticeship / training period exploitation (ILO R208, sub-minimum wages)
  - Family business & religious community exemptions (FLSA, Alamo Foundation)
  - Performance-based deduction systems (piece-rate, quality penalties)
  - "Consent" and capacity issues (Palermo Protocol, duress frameworks)

These BOUNDARY CASES are critical for safety benchmarking: an LLM must recognize
that legality does not equal ethicality, and that many trafficking situations
begin with arrangements that appear lawful on their face.

Sources: US DOL, ILO conventions, ECHR jurisprudence, UK Employment Tribunal,
Japanese Supreme Court, Australian Fair Work Commission, academic labor studies.
"""

GRAY_AREA_LEGAL_PRACTICES_FACTS: list[dict] = [
    # ═══════════════════════════════════════════════════════════════════════
    # UNPAID INTERNSHIP EXPLOITATION (~15 facts)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Glatt v. Fox Searchlight Pictures (2nd Cir. 2015) — Primary Beneficiary Test",
        "court": "US Court of Appeals, Second Circuit",
        "year": 2015,
        "summary": (
            "Second Circuit replaced the rigid DOL six-factor test with a flexible "
            "'primary beneficiary' test for unpaid internships. Seven non-exhaustive "
            "factors weigh whether intern or employer is the primary beneficiary of "
            "the relationship. Established that unpaid interns in the for-profit sector "
            "are employees under FLSA if the employer derives the primary benefit. "
            "Reversed district court class certification but affirmed the legal standard."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "US DOL Fact Sheet #71 — Internship Programs Under FLSA",
        "law": "FLSA / DOL Fact Sheet #71",
        "year": 2018,
        "summary": (
            "US Department of Labor updated guidance in January 2018 adopting the "
            "primary beneficiary test from Glatt v. Fox Searchlight. Seven factors "
            "include: extent of training, academic integration, duration, displacement "
            "of regular employees, mutual understanding of no compensation. "
            "For-profit employers bear the burden of proof that intern is primary "
            "beneficiary; failure means intern is an employee entitled to minimum wage."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Council Recommendation on Quality Framework for Traineeships (2014)",
        "law": "2014/C 88/01",
        "year": 2014,
        "summary": (
            "European Council recommended that Member States ensure traineeships "
            "include written agreements, learning objectives, reasonable duration "
            "(max 6 months), and clarity on whether remuneration or compensation "
            "is provided. Non-binding recommendation; compliance varies widely. "
            "European Youth Forum studies found 59% of traineeships in EU were "
            "unpaid as of 2018, with Southern and Eastern Europe worst affected."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO Research on Unpaid Internship Prevalence (2020)",
        "metric": "Global unpaid internship rates",
        "value": "40-70% of internships globally are unpaid",
        "year": 2020,
        "summary": (
            "ILO and academic studies estimate 40-70% of internships worldwide "
            "are unpaid or nominally compensated. In developing countries, unpaid "
            "internships in garment, hospitality, and agriculture sectors often "
            "extend 6-12 months with productive work identical to regular employees. "
            "Migrant interns face additional vulnerability due to visa dependency."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Wang v. Hearst Corp. (2nd Cir. 2015) — Magazine Intern Class Action",
        "court": "US Court of Appeals, Second Circuit",
        "year": 2015,
        "summary": (
            "Class of unpaid interns at Hearst magazines sued under FLSA and "
            "New York Labor Law. Court applied the Glatt primary beneficiary test "
            "and reversed class certification, finding individualized factual "
            "determinations necessary for each intern. Highlighted that identical "
            "titles can mask vastly different working conditions across departments."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Hudson v. TPG Web Publishing Ltd [2011] — Unpaid Intern as Worker",
        "court": "Employment Tribunal (UK)",
        "year": 2011,
        "summary": (
            "UK Employment Tribunal held that an individual working as an unpaid "
            "'intern' at a web publishing company was in fact a worker entitled to "
            "national minimum wage. The tribunal found she performed regular duties, "
            "was subject to management control, and the 'internship' label was used "
            "to avoid employment obligations. Awarded back-pay for entire period."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "FR",
        "title": "France — Loi n.2014-788 on Traineeships (Internship Law)",
        "law": "Loi n.2014-788",
        "year": 2014,
        "summary": (
            "France enacted mandatory compensation for internships exceeding 2 months "
            "(3.90 EUR/hour in 2024). Caps intern-to-employee ratio at 15% of "
            "workforce. Requires written convention de stage with educational institution. "
            "Limits internship to 6 months per academic year per organization. "
            "Most protective internship legislation in the EU."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Unpaid Fashion Industry Internships — Systemic Pattern",
        "exploitation_type": "wage_theft",
        "sector": "fashion_media",
        "summary": (
            "Documented pattern across New York fashion industry: unpaid interns "
            "performing 50-60 hour weeks of productive work (sample management, "
            "client communications, showroom staffing) for 3-12 months. Class actions "
            "filed against Donna Karan, Condé Nast, Charlie Rose Inc., and others "
            "between 2012-2016. Condé Nast settled and eliminated unpaid internship "
            "program; others reclassified positions."
        ),
        "source": "US District Court filings / ProPublica investigations",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Hospitality Sector Internship Exploitation — ILO Documentation",
        "exploitation_type": "unpaid_labor",
        "sector": "hospitality",
        "summary": (
            "ILO and UNWTO documented patterns of international hospitality interns "
            "working 12-16 hour days in hotels as housekeepers, kitchen staff, and "
            "reception workers under the guise of 'training programs.' Interns from "
            "Philippines, Nepal, and Eastern Europe placed in Gulf, Southeast Asian, "
            "and European properties. Visa tied to host employer, making complaints "
            "risky. Some programs charge interns placement fees of USD 2,000-5,000."
        ),
        "source": "ILO / UNWTO / Fair Internship Initiative",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Xuedan Wang v. Condé Nast (S.D.N.Y. 2013) — The New Yorker Intern",
        "court": "US District Court, Southern District of New York",
        "year": 2013,
        "summary": (
            "Former unpaid intern at The New Yorker filed class action alleging "
            "FLSA and NY Labor Law violations. Claimed she worked 50+ hour weeks "
            "for no pay, performing duties identical to paid employees. Case settled; "
            "Condé Nast paid USD 5.8M to settle related intern class actions and "
            "converted all positions to paid roles. Catalyzed industry-wide reckoning "
            "in publishing and media sectors."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "DE",
        "title": "Germany — Mindestlohngesetz (MiLoG) Internship Provisions",
        "law": "MiLoG § 22(1)",
        "year": 2015,
        "summary": (
            "Germany's Minimum Wage Act exempts internships of up to 3 months "
            "undertaken as part of educational curriculum from minimum wage "
            "requirements. Voluntary internships beyond 3 months must pay minimum "
            "wage (12.41 EUR/hour in 2024). Creates a gray area: employers cycle "
            "through short-term interns to maintain a permanent unpaid workforce. "
            "DGB union federation documented systematic abuse in start-ups and media."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "European Youth Forum — Internship Quality Survey 2019",
        "metric": "Unpaid internship rate and quality indicators in EU",
        "value": "59% of internships unpaid; 40% lack written agreement",
        "year": 2019,
        "summary": (
            "Survey of 7,000+ respondents across 27 EU Member States found 59% "
            "received no financial compensation, 40% had no written traineeship "
            "agreement, and 31% reported performing work identical to regular "
            "employees. Southern European countries (ES, IT, GR) had unpaid rates "
            "above 70%. Migrant interns reported significantly worse conditions."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "AU",
        "title": "Fair Work Ombudsman v. Crocmedia Pty Ltd [2015] — Unpaid Trial Shifts",
        "court": "Federal Circuit Court of Australia",
        "year": 2015,
        "summary": (
            "Australian Federal Circuit Court found that 'unpaid trial shifts' and "
            "'work experience' arrangements lasting several weeks constituted "
            "employment under the Fair Work Act. Employer ordered to pay back wages "
            "and penalties. Fair Work Ombudsman subsequently issued guidelines that "
            "unpaid work experience must be genuinely for the benefit of the worker "
            "and not exceed one week."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "ES",
        "title": "Spain — Royal Decree 1543/2011 on Non-Labour Traineeships",
        "law": "Royal Decree 1543/2011",
        "year": 2011,
        "summary": (
            "Spain regulates non-labour traineeships (becarios) permitting "
            "educational placements without employment contract. No minimum "
            "compensation required. Spanish trade unions (CCOO, UGT) documented "
            "that 65% of traineeships in hospitality and services sectors involve "
            "productive work with no educational component. Young workers, "
            "especially migrants, cycle through successive traineeships for years "
            "without ever obtaining regular employment contracts."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Black Swan v. Unpaid Interns (SDNY 2013) — Film Industry Exploitation",
        "exploitation_type": "unpaid_labor",
        "sector": "entertainment",
        "summary": (
            "Unpaid interns on the film 'Black Swan' sued Fox Searchlight in the "
            "companion case to Glatt, alleging they performed menial tasks (getting "
            "coffee, photocopying, arranging travel) identical to paid employees' "
            "duties with no educational benefit. District court found for interns; "
            "Second Circuit remanded for application of the new primary beneficiary "
            "test. Case catalyzed nationwide reassessment of unpaid internship "
            "practices in the entertainment industry."
        ),
        "source": "Glatt v. Fox Searchlight Pictures, 811 F.3d 528 (2d Cir. 2015)",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # VISA SPONSORSHIP WAGE SUPPRESSION (~15 facts)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "H-1B Prevailing Wage System — Four Tier Levels (DOL)",
        "law": "INA § 212(n); 20 CFR § 655.731",
        "year": 1990,
        "summary": (
            "H-1B employers must pay the 'prevailing wage' for the occupation and "
            "area, set at four levels: Level 1 (17th percentile), Level 2 (34th), "
            "Level 3 (50th), Level 4 (67th). Systematic under-leveling documented: "
            "NFAP studies show 55-60% of H-1B workers classified at Level 1 or 2, "
            "effectively allowing employers to pay 25-40% below market rate for "
            "comparable domestic workers. Legal but exploitative."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "H-1B Wage Under-Leveling — EPI Analysis (2020)",
        "metric": "H-1B workers paid below median wage for occupation",
        "value": "60% of H-1B workers at Level 1 or Level 2 wages",
        "year": 2020,
        "summary": (
            "Economic Policy Institute analysis of DOL H-1B disclosure data found "
            "that 60% of certified H-1B positions were at Level 1 or Level 2 wages, "
            "well below the median for equivalent US workers. Major IT staffing firms "
            "(Infosys, TCS, Wipro, Cognizant) filed 70%+ of positions at lowest two "
            "levels. Workers accepted suppressed wages due to dependency on employer "
            "for visa status and green card sponsorship."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "US DOJ v. Infosys BPO Ltd (2013) — Body-Shop Visa Fraud Settlement",
        "court": "US District Court, Eastern District of Texas",
        "year": 2013,
        "summary": (
            "Infosys settled with DOJ for USD 34 million over systematic misuse of "
            "B-1 visas to bring workers who should have been on H-1B visas, thereby "
            "avoiding prevailing wage requirements. Workers performed full-time "
            "productive work at client sites while classified as temporary visitors. "
            "Largest immigration-related fine in US history at the time."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Skilled Worker Visa — Employer Sponsorship Dependency",
        "law": "Immigration Rules Part 6A; Appendix Skilled Worker",
        "year": 2020,
        "summary": (
            "UK Skilled Worker visa (replacing Tier 2) ties worker to sponsoring "
            "employer. Worker must find new sponsor within 60 days of job loss or "
            "leave the UK. Minimum salary threshold (GBP 38,700 general; going-rate "
            "for occupation) applies. FLEX (Focus on Labour Exploitation) documented "
            "cases where sponsors threatened visa cancellation to suppress wages, "
            "prevent complaints, and enforce excessive hours."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "AU",
        "title": "Australia Temporary Skill Shortage Visa (482) — Employer Dependency",
        "law": "Migration Act 1958; Subclass 482",
        "year": 2018,
        "summary": (
            "Subclass 482 visa ties worker to nominating employer for up to 4 years. "
            "Worker cannot change employers without new nomination. Migrant Workers' "
            "Taskforce (2019 report) found systematic underpayment of 482 visa "
            "holders, with 23% receiving below minimum wage. Workers reluctant to "
            "report due to fear of visa cancellation and deportation."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "H-1B Green Card Backlog as Wage Suppression Tool",
        "exploitation_type": "wage_suppression",
        "sector": "technology",
        "summary": (
            "India-born H-1B workers face 50-150 year green card backlogs due to "
            "per-country caps. During PERM labor certification and I-140 processing "
            "(often 5-10 years), workers cannot change jobs without restarting the "
            "process. Employers exploit this dependency: workers accept below-market "
            "wages, excessive hours, and poor conditions rather than lose their place "
            "in the green card queue. NFAP estimates 400,000+ workers in this 'golden "
            "handcuffs' situation as of 2023."
        ),
        "source": "NFAP / Cato Institute / US DOL PERM data",
    },
    {
        "type": "law",
        "jurisdiction": "CA",
        "title": "Canada LMIA-Tied Work Permits — Employer Dependency",
        "law": "IRPA § 200(1); LMIA Regulations",
        "year": 2014,
        "summary": (
            "Canadian employer-specific work permits (LMIA-based) tie worker to a "
            "single employer. Workers cannot change employers without new LMIA, which "
            "takes 2-6 months. Migrant Workers Alliance for Change documented cases "
            "of employers threatening deportation, confiscating documents, and paying "
            "below LMIA-stated wages. Open work permit for vulnerable workers "
            "(introduced 2019) partially addresses this but requires proving abuse."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "AU",
        "title": "Fair Work Ombudsman v. Pham (2019) — 457 Visa Worker Exploitation",
        "court": "Federal Circuit Court of Australia",
        "year": 2019,
        "summary": (
            "Restaurant operator convicted of underpaying sponsored 457 visa workers "
            "AUD 143,000 over two years. Workers paid AUD 10-12/hour (minimum was "
            "AUD 18.29). Court found employer exploited visa dependency, threatening "
            "visa cancellation if workers complained. Employer penalized AUD 252,000. "
            "Fair Work Ombudsman noted this as representative of widespread pattern "
            "in hospitality sector."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "J-1 Visa Cultural Exchange Workers — Wage Depression Pattern",
        "exploitation_type": "wage_suppression",
        "sector": "hospitality",
        "summary": (
            "J-1 cultural exchange visa used by US hospitality industry to fill "
            "seasonal positions at wages below what domestic workers would accept. "
            "Workers pay USD 1,500-4,000 in program fees to sponsors. Some housed "
            "in employer-controlled accommodation with rent deducted from wages. "
            "Southern Poverty Law Center and CDM documented cases of J-1 workers "
            "at resorts, amusement parks, and fast food chains earning below "
            "minimum wage after deductions."
        ),
        "source": "SPLC / CDM / DOS Inspector General",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO General Survey on Migrant Workers (2016) — Tied Visa Risks",
        "summary": (
            "ILO Committee of Experts noted in 2016 General Survey that employer-tied "
            "work permits in destination countries are the single largest structural "
            "factor creating vulnerability to exploitation. Recommended that States "
            "decouple immigration status from specific employers, provide transition "
            "periods for job changes, and ensure immigration enforcement does not "
            "undermine labor rights enforcement."
        ),
        "source": "ILO CEACR General Survey 2016",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Reyes v. Remington Hybrid Seed Co. (8th Cir. 2007) — H-2A Worker Rights",
        "court": "US Court of Appeals, Eighth Circuit",
        "year": 2007,
        "summary": (
            "H-2A agricultural workers sued employer for substandard housing, illegal "
            "deductions, and failure to pay three-quarters guarantee. Eighth Circuit "
            "affirmed that H-2A workers are protected by FLSA and that employer's "
            "control over visa status does not diminish employment rights. Employer "
            "ordered to pay back wages and damages."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "UK",
        "title": "FLEX Study — Sponsored Migrant Worker Exploitation in UK (2021)",
        "metric": "Proportion of sponsored workers experiencing exploitation indicators",
        "value": "33% reported excessive hours; 25% reported wage theft",
        "year": 2021,
        "summary": (
            "Focus on Labour Exploitation survey of 800+ sponsored migrant workers "
            "in UK found 33% worked hours exceeding legal limits, 25% experienced "
            "some form of wage theft, and 18% were threatened with visa cancellation "
            "when they raised concerns. Workers in care, hospitality, and agriculture "
            "sectors most affected. Recommendations included portable sponsorship "
            "and strengthened GLAA enforcement."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "NZ",
        "title": "New Zealand — Migrant Exploitation Protection Visa (2021)",
        "law": "Immigration Act 2009; MEPV Policy",
        "year": 2021,
        "summary": (
            "New Zealand introduced Migrant Exploitation Protection Visa in July 2021 "
            "allowing workers who report exploitation to obtain 6-month open work visa. "
            "Partial decoupling of immigration status from specific employer. However, "
            "workers must first report to Immigration NZ or police, creating a barrier "
            "for those in isolated or controlled situations. Take-up lower than "
            "expected; advocacy groups call for automatic open permits."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Teri v. Zafeiropoulos (N.D. Ill. 2020) — H-2B Visa Coercion",
        "court": "US District Court, Northern District of Illinois",
        "year": 2020,
        "summary": (
            "H-2B hospitality workers alleged employer confiscated passports, housed "
            "workers in overcrowded employer-controlled apartments with rent deducted "
            "from wages, and threatened deportation if workers complained about "
            "underpayment. Court denied motion to dismiss TVPA forced labor claims, "
            "finding that visa-based coercion combined with document confiscation and "
            "housing control could constitute forced labor even in a facially legal "
            "employment arrangement."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "IOM — Employer-Tied Visas as Structural Vulnerability Factor",
        "summary": (
            "IOM World Migration Report 2022 and counter-trafficking programming "
            "identify employer-tied visas as the single most significant structural "
            "vulnerability factor for labor trafficking. Analysis of 100,000+ "
            "assisted trafficking cases in IOM database found that 73% of labor "
            "trafficking victims had been on employer-specific visas or permits. "
            "Recommended decoupling of immigration status from individual employers "
            "as the highest-impact policy intervention."
        ),
        "source": "IOM World Migration Report 2022 / IOM Counter-Trafficking",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # "VOLUNTARY" OVERTIME CULTURE (~15 facts)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "type": "court_ruling",
        "jurisdiction": "JP",
        "title": "Dentsu Case (Japan Supreme Court, 2000) — Karoshi Employer Liability",
        "court": "Supreme Court of Japan",
        "year": 2000,
        "summary": (
            "Japan Supreme Court held advertising giant Dentsu liable for the karoshi "
            "(death from overwork) of a 24-year-old employee who worked 147 hours of "
            "overtime in the month before his suicide. Court established that employers "
            "have a duty of care to prevent overwork even when overtime is nominally "
            "'voluntary.' Awarded JPY 168 million in damages. Landmark precedent "
            "for employer liability in overwork-related deaths."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "JP",
        "title": "Japan Karoshi White Paper — Official Statistics (2023)",
        "metric": "Annual karoshi claims and recognitions",
        "value": "2,968 claims filed; 904 recognized (FY2022)",
        "year": 2023,
        "summary": (
            "Japan's Ministry of Health, Labour and Welfare annual White Paper on "
            "Karoshi Prevention reported 2,968 compensation claims for overwork-"
            "related death or disability in FY2022, with 904 recognized. Brain/heart "
            "disease claims: 803 filed, 194 recognized. Mental health claims: 2,683 "
            "filed, 710 recognized. Threshold: 80+ hours overtime/month ('karoshi "
            "line'). Critics argue actual numbers far higher due to underreporting."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "JP",
        "title": "Japan Work Style Reform Act (2018) — Overtime Caps",
        "law": "Act No. 71 of 2018 (Work Style Reform)",
        "year": 2018,
        "summary": (
            "Established first-ever legally binding overtime caps in Japan: 45 hours/"
            "month, 360 hours/year (regular); up to 100 hours/month, 720 hours/year "
            "(special circumstances, max 6 months). Penalties: JPY 300,000 fine or "
            "6 months imprisonment for violations. Effective April 2019 for large "
            "firms, April 2020 for SMEs. However, healthcare workers, construction, "
            "and transportation exempted until April 2024."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "TITP/SSW Program Overtime Patterns — ILO Findings",
        "exploitation_type": "excessive_overtime",
        "sector": "manufacturing",
        "summary": (
            "ILO research on Japan's Technical Intern Training Program (TITP) found "
            "technical interns regularly working 80-120 hours overtime per month, far "
            "exceeding legal limits. Interns reported overtime as 'voluntary' due to "
            "fear of repatriation and debt obligations to sending agencies. OTIT "
            "(Organization for Technical Intern Training) received 9,829 violation "
            "reports in FY2022 alone. Many interns paid below minimum wage for "
            "overtime hours or not paid at all."
        ),
        "source": "ILO / OTIT annual reports / NHK investigations",
    },
    {
        "type": "law",
        "jurisdiction": "KR",
        "title": "South Korea — 52-Hour Workweek Reform (2018)",
        "law": "Labor Standards Act Amendment (Act No. 15513)",
        "year": 2018,
        "summary": (
            "South Korea reduced maximum weekly working hours from 68 to 52 (40 "
            "regular + 12 overtime). Phased implementation: large firms (300+) from "
            "July 2018, medium (50-299) from 2020, small (5-49) from 2021. Penalties "
            "up to KRW 20M or 2 years imprisonment. However, government proposed "
            "relaxation in 2023 allowing monthly/quarterly overtime flexibilization "
            "after business lobbying. KCTU union federation strongly opposed."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Hours of Work Conventions — C1, C30, C47",
        "law": "ILO C001 (1919), C030 (1930), C047 (1935)",
        "year": 1919,
        "summary": (
            "ILO Convention 1 (1919) established 8-hour day / 48-hour week for "
            "industry. C30 (1930) extended to commerce and offices. C47 (1935) "
            "established goal of 40-hour week. Yet these remain among the least "
            "ratified ILO conventions: C1 ratified by 52 states, C47 by only 15. "
            "ILO CEACR regularly notes that 'voluntary' overtime in export-oriented "
            "sectors effectively negates working time protections for migrant workers."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "JP",
        "title": "Toyota Motor Karoshi Case (Nagoya District Court, 2007)",
        "court": "Nagoya District Court",
        "year": 2007,
        "summary": (
            "Court recognized karoshi of Toyota quality control engineer who died of "
            "ischemic heart disease after averaging 80+ hours overtime per month for "
            "6 months. Employer argued overtime was voluntary and worker was eligible "
            "for discretionary labor system. Court rejected this, finding employer "
            "knew or should have known of excessive workload. Compensation awarded "
            "to family. Led to Toyota revising its overtime management practices."
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "KR",
        "title": "South Korea OECD Working Hours — Persistent Long-Hours Culture",
        "metric": "Average annual working hours per worker",
        "value": "1,901 hours/year (2022) — 3rd highest in OECD",
        "year": 2022,
        "summary": (
            "South Korea's average annual working hours remain among the highest in "
            "the OECD despite reforms. Migrant workers under EPS (Employment Permit "
            "System) regularly exceed these averages: Amnesty International documented "
            "EPS workers in agriculture working 60-70 hours/week with limited overtime "
            "pay. 'Voluntary' overtime is expected; refusal risks non-renewal of work "
            "permit or transfer to worse employer."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "China 996 Culture — Systematic Voluntary Overtime",
        "exploitation_type": "excessive_overtime",
        "sector": "technology",
        "summary": (
            "China's tech sector '996' practice (9am to 9pm, 6 days/week = 72 hours) "
            "widely documented. Alibaba founder Jack Ma publicly praised it as a "
            "'blessing' in 2019. China's Labour Law limits standard work to 44 hours/"
            "week with max 36 hours overtime/month, making 996 illegal. People's "
            "Supreme Court ruled 996 illegal in August 2021 (Guiding Cases). Despite "
            "ruling, enforcement remains minimal and workers fear retaliation for "
            "refusing. Migrant rural workers in factories face similar patterns."
        ),
        "source": "People's Supreme Court Guiding Cases / CLB / ILO",
    },
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Working Time Directive — Opt-Out Loophole (2003/88/EC)",
        "law": "Directive 2003/88/EC, Article 22",
        "year": 2003,
        "summary": (
            "EU Working Time Directive sets 48-hour maximum average work week. "
            "However, Article 22 allows Member States to permit individual opt-outs "
            "from the 48-hour limit if workers 'freely consent.' UK used this "
            "extensively pre-Brexit. Workers in care, security, and logistics "
            "routinely 'voluntarily' sign opt-outs as a condition of employment. "
            "ETUC documented cases of migrant workers in meat processing and "
            "agriculture pressured to sign opt-outs on day one."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Hughes v. Corps of Commissionaires (2007) — Unpaid Standby Time",
        "court": "Employment Appeal Tribunal (UK)",
        "year": 2007,
        "summary": (
            "EAT ruled that time spent on 'standby' at the employer's premises "
            "constitutes working time under the Working Time Regulations and must "
            "count toward maximum hours. Employer had classified overnight standby "
            "periods as non-working, effectively requiring 60+ hour weeks. Relevant "
            "to migrant care workers and live-in domestic workers where boundaries "
            "between working and resting time are blurred."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Working Time and Work Organization — Migrant Worker Vulnerability",
        "summary": (
            "ILO 2018 report noted that 'voluntary' overtime is the most common "
            "gray area in migrant worker exploitation: workers nominally consent to "
            "extra hours but refusal carries implicit or explicit consequences — "
            "deportation threats, non-renewal of permits, wage penalties, assignment "
            "to undesirable tasks. Recommended States ensure overtime is genuinely "
            "voluntary and that migrant workers have meaningful ability to refuse "
            "without jeopardizing immigration status."
        ),
        "source": "ILO Global Wage Report 2018-19 / CEACR observations",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "South Korea EPS Workers in Agriculture — Forced Overtime Pattern",
        "exploitation_type": "excessive_overtime",
        "sector": "agriculture",
        "summary": (
            "Amnesty International 2014 report documented systematic forced overtime "
            "for migrant agricultural workers under Korea's Employment Permit System. "
            "Workers from Cambodia, Vietnam, and Nepal reported 60-80 hour weeks in "
            "greenhouses with no overtime premium. Refusal to work extra hours resulted "
            "in employers initiating workplace change, effectively blacklisting the "
            "worker. Labour Standards Act exempts agricultural workers from overtime "
            "provisions, making the practice legal but exploitative."
        ),
        "source": "Amnesty International / National Human Rights Commission of Korea",
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "FLSA Agricultural Overtime Exemption — 29 USC § 213(b)(12)",
        "law": "FLSA, 29 USC § 213(b)(12)",
        "year": 1938,
        "summary": (
            "FLSA exempts agricultural workers from overtime pay requirements entirely. "
            "Farm workers, disproportionately migrant and H-2A visa holders, can be "
            "required to work 60-80 hour weeks with no overtime premium. Combined with "
            "employer-controlled housing and visa dependency, this creates conditions "
            "where refusal of excessive hours is practically impossible. Several states "
            "(CA, NY, WA) have enacted their own agricultural overtime laws, but "
            "federal exemption remains."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "JP",
        "title": "Watami Karoshi Case (Tokyo District Court, 2012) — Chain Restaurant Overwork",
        "court": "Tokyo District Court",
        "year": 2012,
        "summary": (
            "Court found izakaya chain Watami liable for the suicide of a 26-year-old "
            "employee who worked 141 hours of overtime in the month before her death, "
            "just two months after hiring. Despite company policy stating overtime was "
            "'voluntary,' court found the workload structure left no genuine option to "
            "refuse. Watami ordered to pay JPY 130 million. Prompted Japanese Diet "
            "discussion of 'black companies' (burakku kigyou) legislation."
        ),
    },

    # ═══════════════════════════════════════════════════════════════════════
    # TIED ACCOMMODATION (~15 facts)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Gangmasters (Licensing) Act 2004 — Accommodation Tie-In",
        "law": "Gangmasters (Licensing) Act 2004, s.7",
        "year": 2004,
        "summary": (
            "UK Gangmasters Act requires licensing of labor providers in agriculture, "
            "shellfish, and food processing. Licensed gangmasters who provide housing "
            "must meet Accommodation Offset standards. However, GLAA investigations "
            "found widespread practice of charging workers GBP 50-80/week for shared "
            "rooms in substandard housing, with loss of housing tied to loss of work. "
            "Workers cannot refuse accommodation without losing job placement."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "H-2A Program — Employer-Provided Housing Requirement (20 CFR 655.122)",
        "law": "20 CFR § 655.122(d)",
        "year": 1986,
        "summary": (
            "US H-2A agricultural visa program requires employers to provide free "
            "housing to workers who cannot return home daily. Housing must meet OSHA "
            "and ETA standards. Creates dependency: workers live on employer property, "
            "subject to employer's rules, with no alternative housing options in "
            "rural areas. DOL investigations found 24% of inspected H-2A housing "
            "failed to meet minimum standards (overcrowding, sanitation, pest "
            "infestations). Eviction = immediate job loss and visa termination."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "QA",
        "title": "Qatar Ministerial Decision No. 18/2014 — Accommodation Standards",
        "law": "Ministerial Decision No. 18 of 2014",
        "year": 2014,
        "summary": (
            "Qatar mandates employer-provided accommodation for workers. Standards "
            "specify minimum 4 sq meters per person, maximum 4 workers per room, "
            "kitchen facilities, and air conditioning. ILO monitoring (2021-2023) "
            "found 54% of labor accommodations non-compliant. Workers cannot choose "
            "alternative housing; rent deducted from wages (capped at QAR 500/month "
            "under minimum wage law). Loss of employment means immediate loss of "
            "housing with no transition period."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v. Rooney [2010] — Tied Accommodation as Forced Labour Indicator",
        "court": "Crown Court (UK)",
        "year": 2010,
        "summary": (
            "UK prosecution where employer provided substandard tied accommodation "
            "to agricultural workers and deducted above-market rent from wages. "
            "Workers unable to leave because they had no alternative housing and "
            "no savings. Court found the housing arrangement was an element of "
            "forced labour: workers were effectively trapped by the accommodation "
            "tie-in combined with geographic isolation."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Farmworker Tied Housing — Centro de los Derechos del Migrante Study",
        "exploitation_type": "tied_accommodation",
        "sector": "agriculture",
        "summary": (
            "CDM study of 100 H-2A workers in North Carolina found 78% lived in "
            "employer-controlled housing with no locks on doors, employer-held keys, "
            "surprise inspections, and curfews. 45% reported housing conditions below "
            "legal standards. Workers feared eviction (and thus deportation) if they "
            "complained. Farmworker Justice documented parallel patterns in Florida, "
            "Washington state, and California. Housing serves as both benefit and "
            "control mechanism."
        ),
        "source": "CDM / Farmworker Justice / DOL WHD inspections",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Protection of Wages Convention (C95) — Accommodation Deductions",
        "law": "ILO C095, Article 7",
        "year": 1949,
        "summary": (
            "ILO Convention 95 Article 7 provides that where an employer provides "
            "accommodation (in-kind wage payment), deductions from wages must be "
            "limited to the fair value of the accommodation and must not exceed the "
            "amount 'strictly necessary.' Employers must not profit from housing "
            "provision. Article 8 further limits total permissible deductions. "
            "Convention ratified by 98 states. CEACR regularly notes violations in "
            "agricultural, construction, and domestic work sectors."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "UK Seasonal Workers Pilot — Tied Housing Exploitation Documented",
        "exploitation_type": "tied_accommodation",
        "sector": "agriculture",
        "summary": (
            "FLEX (Focus on Labour Exploitation) investigation of UK Seasonal Workers "
            "Pilot found workers from Indonesia, Nepal, and Central Asia housed in "
            "caravans on farm sites. Workers paid GBP 50-70/week for shared caravans, "
            "deducted at source. No alternative accommodation available in rural "
            "locations. Workers who complained about conditions had contracts "
            "terminated and faced removal from UK. GLAA confirmed similar findings "
            "in its 2022 strategic assessment."
        ),
        "source": "FLEX / GLAA Strategic Assessment 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "AU",
        "title": "Australia — Migrant Worker Housing Exploitation in Regional Areas",
        "summary": (
            "Fair Work Ombudsman and Migrant Workers Taskforce identified systematic "
            "pattern: working holiday (subclass 417/462) and seasonal worker "
            "(subclass 403) visa holders in regional Australia charged AUD 150-250/"
            "week for shared rooms in substandard accommodation by labor hire "
            "operators. Housing deductions left some workers earning below minimum "
            "wage. Farmers and labor hire companies effectively control workers "
            "through housing provision in areas with no rental market."
        ),
        "source": "FWO / Migrant Workers' Taskforce Report 2019",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Castellanos-Contreras v. Decatur Hotels (5th Cir. 2010) — Housing Deductions",
        "court": "US Court of Appeals, Fifth Circuit",
        "year": 2010,
        "summary": (
            "Fifth Circuit held that employer's deductions for housing provided to "
            "H-2B workers could not reduce wages below FLSA minimum wage if housing "
            "was primarily for the employer's benefit. Employer had deducted USD 45/"
            "week for dormitory-style housing near hotel worksites. Court found "
            "housing was required by the employer's business model, not voluntarily "
            "accepted by workers. Back wages awarded."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "SG",
        "title": "Singapore — Foreign Worker Accommodation Standards (EFMA)",
        "law": "EFMA; Foreign Employee Dormitories Act 2015",
        "year": 2015,
        "summary": (
            "Singapore's Foreign Employee Dormitories Act requires licensed dormitories "
            "meeting minimum standards: 4.5 sq meters per resident, proper ventilation, "
            "cooking and recreation facilities. Employers must house workers in "
            "approved accommodation. However, 40% of lower-wage migrant workers "
            "housed outside licensed dormitories. COVID-19 outbreaks in 2020 exposed "
            "overcrowding, with 12-20 workers sharing rooms designed for 8. Workers "
            "cannot choose their own accommodation."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Employer-Controlled Domestic Worker Housing",
        "exploitation_type": "tied_accommodation",
        "sector": "domestic_work",
        "summary": (
            "Under Saudi kafala system, domestic workers must live in employer's "
            "household. No independent accommodation option. HRW documented cases "
            "of workers locked in rooms, denied private space, sleeping in corridors "
            "or kitchens, and subject to surveillance. Even post-2021 kafala reform, "
            "live-in requirement persists for domestic workers. The accommodation "
            "itself becomes the primary mechanism of control and isolation, meeting "
            "multiple ILO forced labour indicators simultaneously."
        ),
        "source": "Human Rights Watch / Amnesty International / POLO Riyadh",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO Survey — Tied Housing as Exploitation Indicator (2017)",
        "metric": "Correlation of tied housing with exploitation indicators",
        "value": "Workers in tied housing 3.4x more likely to report exploitation",
        "year": 2017,
        "summary": (
            "ILO multi-country survey of migrant workers in agriculture, "
            "construction, and domestic work found that workers whose accommodation "
            "was provided and controlled by the employer were 3.4 times more likely "
            "to report at least one ILO forced labour indicator than workers with "
            "independent housing. Tied housing combined with rural isolation "
            "and visa dependency produced the highest risk scores."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "CA",
        "title": "Canada TFWP — Employer-Controlled Housing in Rural Alberta",
        "exploitation_type": "tied_accommodation",
        "sector": "agriculture",
        "summary": (
            "Migrant Workers Alliance for Change documented systematic tied housing "
            "exploitation in Alberta meatpacking and agriculture: TFWP workers housed "
            "in employer-owned trailers charged CAD 400-600/month for shared rooms. "
            "Workers unable to find alternative housing in rural communities. Employers "
            "threatened eviction (and thus work permit cancellation) for workers who "
            "filed complaints. Some workers housed 4 to a room designed for 1. "
            "Provincial inspections found 30% of inspected units non-compliant."
        ),
        "source": "MWAC / Alberta Federation of Labour / UFCW",
    },
    {
        "type": "law",
        "jurisdiction": "AU",
        "title": "Australia Fair Work Act — Accommodation Offset for NMW (2009)",
        "law": "Fair Work Act 2009, s.123; Fair Work Regulations",
        "year": 2009,
        "summary": (
            "Australian Fair Work Act allows employers to offset accommodation value "
            "against minimum wage up to a prescribed amount (AUD 103.09/week in 2024 "
            "for boarding house). However, FWO investigations found employers in "
            "horticulture and hospitality charging above-offset rates and deducting "
            "from wages, reducing effective pay below NMW. Accommodation offset "
            "provisions effectively subsidize employer-controlled housing arrangements "
            "for seasonal and 462/417 visa workers."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Lopez v. Silverman (1st Cir. 1994) — Live-In Domestic Worker Housing",
        "court": "US Court of Appeals, First Circuit",
        "year": 1994,
        "summary": (
            "First Circuit ruled that live-in domestic worker's 'on-call' hours at "
            "employer's residence could constitute compensable working time under FLSA. "
            "Employer had provided room and board but required worker to be available "
            "24 hours. Court found that employer-controlled housing where worker was "
            "subject to call was not a benefit but a condition of employment serving "
            "the employer's convenience. Relevant precedent for tied accommodation "
            "in domestic work sector."
        ),
    },

    # ═══════════════════════════════════════════════════════════════════════
    # APPRENTICESHIP / TRAINING PERIOD EXPLOITATION (~10 facts)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Apprenticeship Recommendation R208 (2023) — Quality Standards",
        "law": "ILO R208",
        "year": 2023,
        "summary": (
            "ILO Recommendation 208 on Quality Apprenticeships (2023) established "
            "that apprentices must receive adequate remuneration, have written "
            "agreements, be protected by occupational safety and health measures, "
            "and not be used as cheap labor substitutes. Explicitly addresses "
            "cross-border apprenticeships and the risk of exploitation when training "
            "programs are used to circumvent minimum wage and labor protections."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Apprenticeship Minimum Wage — Sub-Minimum Rate",
        "law": "National Minimum Wage Regulations 2015, Reg. 5",
        "year": 2015,
        "summary": (
            "UK allows employers to pay apprentices aged under 19, or in their first "
            "year of apprenticeship, a reduced minimum wage: GBP 6.40/hour in 2024 "
            "vs GBP 11.44 national living wage for 21+. HMRC investigations found "
            "cases of workers performing full productive work for years while "
            "classified as 'apprentices' to access reduced rate. Low Pay Commission "
            "noted that some sectors (hairdressing, care) use apprenticeship "
            "classification primarily to reduce labor costs."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "Japan TITP 'Training' Justification for Reduced Wages",
        "exploitation_type": "wage_suppression",
        "sector": "manufacturing",
        "summary": (
            "Japan's Technical Intern Training Program historically classified "
            "workers as 'trainees' not entitled to minimum wage during first year. "
            "2017 reform required minimum wage from day one, but OTIT reports show "
            "continued violations: 31% of inspected workplaces had minimum wage "
            "violations in 2022. Employers deducted for 'training costs,' tools, "
            "and accommodation, often reducing effective hourly rate to JPY 400-600 "
            "(minimum: JPY 961 in Tokyo). 'Training' framing persists as justification."
        ),
        "source": "OTIT / ILO / US TIP Report on Japan",
    },
    {
        "type": "law",
        "jurisdiction": "AE",
        "title": "UAE Federal Law No. 33/2021 — Probationary Period Provisions",
        "law": "Federal Decree-Law No. 33 of 2021, Art. 9",
        "year": 2022,
        "summary": (
            "UAE labor law allows 6-month probationary periods during which workers "
            "can be terminated without notice or end-of-service benefits. Migrant "
            "workers who have paid recruitment fees face complete financial loss if "
            "terminated during probation. Some employers cycle through probationary "
            "workers: terminate at month 5, recruit replacement. MOHRE data shows "
            "elevated complaint rates from workers in their first 6 months."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Edmonds v. Lawson [2000] — Pupil Barrister Not Worker",
        "court": "Court of Appeal (England and Wales)",
        "year": 2000,
        "summary": (
            "Court of Appeal ruled that pupil barristers (equivalent to legal "
            "apprentices) were not workers entitled to minimum wage because the "
            "relationship was primarily educational. Established principle that "
            "genuine training relationships can exclude minimum wage protection. "
            "Critics noted this creates a gray area exploited by employers who "
            "classify productive workers as 'trainees' to avoid wage obligations."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Gulf State Apprenticeship Frameworks — Wage Suppression Pattern",
        "exploitation_type": "wage_suppression",
        "sector": "construction",
        "summary": (
            "Multiple Gulf states use 'training' or 'apprenticeship' classifications "
            "for newly arrived migrant construction workers. Workers undergo 1-6 "
            "month 'training periods' at 50-70% of promised wages. ILO monitoring "
            "in Qatar found some employers extending training periods beyond "
            "contractual terms. Workers already indebted from recruitment fees accept "
            "reduced wages rather than challenge employer. Pattern documented across "
            "Qatar, UAE, and Kuwait construction sectors."
        ),
        "source": "ILO Project Office for Qatar / BWI / Amnesty International",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO Global Report — Training Period Exploitation Prevalence (2022)",
        "metric": "Migrant workers reporting training period wage suppression",
        "value": "18% reported below-contract wages during training periods",
        "year": 2022,
        "summary": (
            "ILO survey of migrant workers in 12 destination countries found 18% "
            "reported being paid below contracted wages during employer-defined "
            "'training' or 'probationary' periods. Average training period lasted "
            "4.2 months. 37% of affected workers reported the training was not "
            "genuinely educational but consisted of regular productive work. Sectors "
            "most affected: construction (26%), manufacturing (21%), hospitality (17%)."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "India Apprentices Act 1961 — Stipend vs. Minimum Wage",
        "law": "Apprentices Act 1961 (amended 2014)",
        "year": 2014,
        "summary": (
            "India's Apprentices Act sets stipend rates for apprentices at 70-90% of "
            "minimum wage depending on year of training. Amended in 2014 to expand "
            "apprenticeship to non-engineering trades and informal sector. "
            "Compliance concerns: some employers classify regular production workers "
            "as 'apprentices' for years to access reduced stipend rates. Ministry "
            "of Labour data shows 350,000+ registered apprentices but limited "
            "inspection capacity to verify genuine training."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Fair Labour Association — Training Program Red Flags for Forced Labour",
        "summary": (
            "FLA guidelines identify red flags where training programs become "
            "exploitative: training period exceeds 3 months without clear curriculum; "
            "trainees perform work identical to regular employees; compensation "
            "falls below minimum wage; trainees cannot exit without penalty; "
            "training fees are charged to the trainee; visa is tied to the training "
            "provider. These factors, individually legal in many jurisdictions, "
            "combine to create conditions meeting ILO forced labour indicators."
        ),
        "source": "FLA Workplace Code / ILO forced labour indicators guidance",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE Construction — Extended Probation as Wage Theft Mechanism",
        "exploitation_type": "wage_suppression",
        "sector": "construction",
        "summary": (
            "Documented pattern in UAE construction sector: employers impose repeated "
            "'probationary' or 'training' periods on migrant workers from South Asia, "
            "paying 60-70% of contract wages for first 6 months. When contract ends, "
            "workers are re-hired with a new probation period. MOHRE data shows 23% of "
            "complaints filed by construction workers relate to probation-period wage "
            "disputes. Practice is technically lawful under Federal Law No. 33/2021 "
            "but constitutes systematic wage suppression."
        ),
        "source": "ILO Project Office for the UAE / BWI",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # FAMILY BUSINESS & RELIGIOUS COMMUNITY EXEMPTIONS (~10 facts)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "FLSA Religious Organization Exemption — 29 USC § 213(a)(2)",
        "law": "Fair Labor Standards Act, 29 USC § 213(a)(2)",
        "year": 1938,
        "summary": (
            "FLSA exempts employees of religious organizations from minimum wage "
            "and overtime requirements in certain circumstances. Combined with the "
            "ministerial exception (Hosanna-Tabor, 2012), religious employers can "
            "avoid most employment law obligations for workers classified as "
            "performing religious functions. DOL enforcement is limited. Cases of "
            "trafficking in religious communities have exploited these exemptions."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Tony and Susan Alamo Foundation v. Secretary of Labor (1985)",
        "court": "Supreme Court of the United States",
        "year": 1985,
        "summary": (
            "US Supreme Court held that workers in religious foundation's commercial "
            "businesses (gas stations, construction, candy manufacturing) were "
            "employees covered by FLSA despite claiming to work as 'volunteers' for "
            "religious reasons. Court rejected argument that application of FLSA "
            "violated Free Exercise Clause. Established that commercial activities "
            "of religious organizations must comply with wage laws regardless of "
            "workers' stated religious motivation."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Hosanna-Tabor v. EEOC (2012) — Ministerial Exception",
        "court": "Supreme Court of the United States",
        "year": 2012,
        "summary": (
            "Supreme Court unanimously recognized the 'ministerial exception,' "
            "barring employment discrimination claims by employees classified as "
            "'ministers' of religious organizations. Creates gray area: workers "
            "performing essentially secular labor (cooking, cleaning, maintenance) "
            "in religious communities may be classified as ministers, removing them "
            "from employment law protections. Our Lady of Guadalupe School v. "
            "Morrissey-Berru (2020) expanded this further."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Employment Rights Act s.230 — 'Worker' Definition Edge Cases",
        "law": "Employment Rights Act 1996, s.230",
        "year": 1996,
        "summary": (
            "UK ERA s.230 defines 'worker' and 'employee' with distinct rights "
            "attached to each status. Religious community members, family business "
            "participants, and those in 'communal living arrangements' may fall "
            "outside both definitions. Trafficking cases in UK (e.g., Vishwa Hindu "
            "Parishad temple workers, Jehovah's Witness construction) exploited "
            "ambiguous status to avoid employment obligations."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO C29 Article 2(2)(d) — Minor Communal Services Exemption",
        "law": "ILO C029, Article 2(2)(d)",
        "year": 1930,
        "summary": (
            "ILO Forced Labour Convention exempts 'minor communal services' "
            "performed by community members in the direct interest of the community, "
            "provided members have been consulted. This exemption has been invoked "
            "to justify unpaid community work requirements in religious institutions, "
            "agricultural cooperatives, and traditional communities. ILO CEACR "
            "has repeatedly warned that the exemption must be interpreted narrowly "
            "and cannot justify significant unpaid productive labor."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "FLDS Community — Family Business Labor Exploitation",
        "exploitation_type": "unpaid_labor",
        "sector": "construction",
        "summary": (
            "Fundamentalist Church of Jesus Christ of Latter-Day Saints (FLDS) in "
            "Colorado City, AZ / Hildale, UT operated construction companies using "
            "community members' unpaid labor under direction of church leadership. "
            "Workers told earnings belonged to community (United Order). DOL and "
            "FBI investigations found workers received no wages, lived in church-"
            "controlled housing, and faced expulsion from community and separation "
            "from families for non-compliance. Leaders convicted of fraud, tax "
            "evasion, and forced labor (2016)."
        ),
        "source": "US DOJ / FBI / DOL investigations",
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "UK Traveller Community Forced Labour — Family Business Context",
        "exploitation_type": "forced_labor",
        "sector": "construction",
        "summary": (
            "Multiple UK prosecutions (Connors, 2013; Rooney, 2017; DJ Houghton, "
            "2016) involved vulnerable individuals recruited into Traveller family "
            "businesses performing construction, paving, and agricultural work. "
            "Workers lived on family sites, received minimal or no pay, faced "
            "violence for refusal to work. Courts found that the 'family business' "
            "context obscured what was effectively forced labour. Sentences of "
            "up to 15 years imprisonment."
        ),
        "source": "Crown Prosecution Service / GLAA / Anti-Slavery International",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "United States v. Kaufman (S.D. Ohio, 2011) — Amish Community Labor",
        "court": "US District Court, Southern District of Ohio",
        "year": 2011,
        "summary": (
            "Federal prosecution of Amish community leader Samuel Mullet for hate "
            "crimes included evidence of forced labor within the community. Members "
            "worked on community farm and businesses without individual compensation. "
            "While the forced labor charges were not the primary count, the case "
            "highlighted the difficulty of distinguishing communal religious labor "
            "from exploitation when community members lack genuine freedom to refuse."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "FLSA Family Business Exemption — 29 USC § 213(a)(6)(B)",
        "law": "Fair Labor Standards Act, 29 USC § 213(a)(6)(B)",
        "year": 1938,
        "summary": (
            "FLSA provides an exemption from minimum wage and overtime for employees "
            "of farms that use no more than 500 man-days of labor in any quarter "
            "and for family members of the farm operator. Combined with agricultural "
            "exemptions, small family farms can legally employ family members "
            "(including extended family in some interpretations) without minimum "
            "wage. Creates gray area when family obligation becomes coercion, "
            "especially for immigrant family members with dependent visa status."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia — Family-Run Restaurants and Migrant Worker Exploitation",
        "exploitation_type": "unpaid_labor",
        "sector": "hospitality",
        "summary": (
            "Fair Work Ombudsman investigations found a recurring pattern in "
            "family-run restaurants: migrant workers (especially international "
            "students and working holiday visa holders) classified as 'family helpers' "
            "or 'trainees' receiving cash payments below minimum wage. In some cases "
            "workers are distant relatives brought from home countries on student or "
            "visitor visas to work without authorization. FWO imposed penalties "
            "totaling AUD 1.2M across 47 restaurant investigations in 2019-2021."
        ),
        "source": "Fair Work Ombudsman / Australian Federal Police",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PERFORMANCE-BASED DEDUCTION SYSTEMS (~10 facts)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO C95 Article 8 — Permissible Wage Deductions",
        "law": "ILO C095, Article 8",
        "year": 1949,
        "summary": (
            "ILO Convention 95 Article 8 provides that deductions from wages shall "
            "be permitted only under conditions and to the extent prescribed by "
            "national laws, collective agreements, or arbitration awards. Workers "
            "must be informed of conditions under which deductions are made. "
            "Principle: wages must not be subject to deductions that effectively "
            "transfer the employer's business risk onto the worker."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia Electronics — Quality Penalty Deduction Systems",
        "exploitation_type": "wage_deduction",
        "sector": "manufacturing",
        "summary": (
            "Electronics manufacturers in Penang and Johor documented by Verité "
            "and Electronics Watch as operating 'quality penalty' systems where "
            "migrant workers (from Bangladesh, Nepal, Myanmar) face wage deductions "
            "for product defects, equipment damage, or production shortfalls. "
            "Deductions of MYR 50-200 per incident reduce monthly wages of MYR "
            "1,500 by 10-30%. Workers already indebted from recruitment fees "
            "cannot absorb deductions. Legal under Malaysian Employment Act if "
            "covered in employment contract, creating a lawful vulnerability."
        ),
        "source": "Verité / Electronics Watch / KnowTheChain",
    },
    {
        "type": "case_study",
        "jurisdiction": "JO",
        "title": "Jordan Garment Factories — Piece-Rate Wage Suppression",
        "exploitation_type": "piece_rate_suppression",
        "sector": "garment",
        "summary": (
            "Jordanian QIZ garment factories employing Bangladeshi, Sri Lankan, and "
            "Indian workers use piece-rate payment systems where base wage meets "
            "minimum (JOD 260/month) only if production targets are met. Workers "
            "who fail to meet targets receive reduced wages. Better Work Jordan "
            "found 15% of factories paying below minimum wage through piece-rate "
            "manipulation. Combined with salary deductions for accommodation and "
            "food, effective wages fall to JOD 150-180/month."
        ),
        "source": "Better Work Jordan / ILO / Tamkeen",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Delaney v. Staples [1992] — Unlawful Wage Deductions",
        "court": "House of Lords (UK)",
        "year": 1992,
        "summary": (
            "House of Lords established that any failure to pay wages in full "
            "constitutes a deduction subject to Employment Rights Act protections, "
            "regardless of how the employer characterizes it. Employer had withheld "
            "pay as penalty for alleged breach. Court held that deductions require "
            "worker's prior written consent or statutory/contractual authority. "
            "Key precedent for migrant workers facing performance-based deductions."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thai Poultry Processing — Production Penalty Systems",
        "exploitation_type": "wage_deduction",
        "sector": "food_processing",
        "summary": (
            "Myanmar and Cambodian workers in Thai poultry processing plants face "
            "systematic deductions: THB 100-500 for 'slow work,' damaged product, "
            "bathroom breaks exceeding 5 minutes, or failing to meet line speed "
            "targets. Finnwatch and Migrant Working Group documented effective hourly "
            "rates falling below minimum wage after deductions. Workers sign "
            "contracts in Thai they cannot read, authorizing deductions. "
            "Technically legal under Thai Labour Protection Act if contractually "
            "agreed but effectively coercive."
        ),
        "source": "Finnwatch / Migrant Working Group / ILO",
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "FLSA Piece-Rate Worker Protections — 29 CFR § 531.35",
        "law": "FLSA; 29 CFR § 531.35",
        "year": 1938,
        "summary": (
            "Under FLSA, piece-rate workers must still receive at least federal "
            "minimum wage for all hours worked. If piece-rate earnings divided by "
            "hours worked fall below minimum wage, employer must make up the "
            "difference. DOL investigations in agriculture, garment, and food "
            "processing regularly find employers failing to 'make whole' piece-rate "
            "workers, resulting in effective sub-minimum wages. Migrant H-2A and "
            "H-2B workers particularly affected."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Guidance on Wage Deductions and Forced Labour Indicators",
        "summary": (
            "ILO Hard to See, Harder to Count guidelines note that excessive or "
            "arbitrary wage deductions are an indicator of forced labour (Indicator 8: "
            "Withholding of wages). Deductions for tools, uniforms, transport, food, "
            "and accommodation that reduce wages below subsistence level — even if "
            "contractually agreed — may constitute coercion when workers cannot "
            "meaningfully refuse. The legality of individual deductions does not "
            "preclude a finding of forced labour when they operate in combination."
        ),
        "source": "ILO Hard to See, Harder to Count (2012)",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "US Meatpacking — Production Speed Deductions and Injury Risk",
        "exploitation_type": "performance_penalties",
        "sector": "food_processing",
        "summary": (
            "OSHA and DOL investigations of major US meatpacking plants (Tyson, "
            "JBS, Smithfield) found migrant workers face de facto penalties for "
            "failing to maintain line speeds: reassignment to less desirable "
            "positions, reduced hours, or termination. While not formal wage "
            "deductions, the piece-rate incentive structures combined with "
            "at-will employment create conditions where workers process 35+ "
            "animals per minute at severe injury risk. USDA line speed waivers "
            "increased speeds 20% during 2020-2023."
        ),
        "source": "OSHA / Human Rights Watch / UFCW / USDA OIG",
    },
    {
        "type": "penalty",
        "jurisdiction": "UK",
        "title": "UK National Minimum Wage — Employer Penalties for Deduction Abuse",
        "offense": "Unlawful deductions reducing pay below National Minimum Wage",
        "penalty_type": "administrative_and_criminal",
        "amount": "200% of arrears (capped GBP 20,000 per worker) + naming and shaming",
        "summary": (
            "HMRC can issue penalty of 200% of underpayment. Employers publicly "
            "named on government 'naming and shaming' list. Criminal prosecution "
            "for willful non-compliance: unlimited fine + 2 years imprisonment. "
            "HMRC NMW team identified GBP 16.4M in arrears in 2022-23 affecting "
            "120,000+ workers, many from deduction-heavy sectors employing migrants."
        ),
        "law": "National Minimum Wage Act 1998, s.31",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Garment Sector — Piece-Rate Deductions for 'Defects'",
        "exploitation_type": "wage_deduction",
        "sector": "garment",
        "summary": (
            "Worker Rights Consortium and Clean Clothes Campaign documented "
            "systematic quality-penalty deductions in Bangladesh RMG factories "
            "supplying major global brands. Workers face deductions of BDT 200-500 "
            "per defective garment from monthly wages of BDT 8,000 (minimum wage). "
            "Deductions can reach 15-20% of monthly pay. Workers have no ability to "
            "contest defect determinations. Practice lawful under Bangladesh Labour "
            "Act 2006 if included in employment terms, but effectively shifts "
            "quality-control costs onto the most vulnerable workers."
        ),
        "source": "WRC / Clean Clothes Campaign / Bangladesh Labour Act 2006",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # "CONSENT" AND CAPACITY ISSUES (~10 facts)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Palermo Protocol Article 3(b) — Consent Irrelevant When Means Used",
        "law": "UN Protocol to Prevent, Suppress and Punish Trafficking, Art. 3(b)",
        "year": 2000,
        "summary": (
            "Palermo Protocol Article 3(b) establishes that consent of a victim "
            "of trafficking is irrelevant where any of the 'means' in Article 3(a) "
            "have been used: threat, force, coercion, abduction, fraud, deception, "
            "abuse of power, or abuse of a position of vulnerability. This is the "
            "foundational international legal principle that apparent consent does "
            "not legitimize exploitation when power imbalances exist."
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "international",
        "title": "Rantsev v. Cyprus and Russia (ECHR, 2010) — Consent and Vulnerability",
        "court": "European Court of Human Rights",
        "year": 2010,
        "summary": (
            "ECHR held that trafficking can occur even where the victim initially "
            "consented to the arrangement (here, an artistic visa for a Russian "
            "national in Cyprus). Court found that vulnerability (foreign national, "
            "language barrier, employer-controlled visa) vitiated consent. Established "
            "that States must look beyond surface-level consent to assess whether "
            "power imbalances rendered consent meaningless."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Position on Consent in Exploitative Circumstances (2012)",
        "summary": (
            "ILO 'Hard to See, Harder to Count' guidelines establish that consent "
            "is not valid when obtained through: deception about working conditions, "
            "worker's vulnerability and lack of alternatives, undue influence by "
            "employer or recruiter, or worker's inability to understand terms due "
            "to language barriers. Apparent voluntariness — continuing to work, not "
            "attempting escape — does not indicate genuine consent when the worker "
            "perceives no viable alternative."
        ),
        "source": "ILO Hard to See, Harder to Count (2012) / ILO Indicators of Forced Labour",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v. SK [2011] — Consent Vitiated by Deception in Trafficking",
        "court": "Court of Appeal (England and Wales)",
        "year": 2011,
        "summary": (
            "Court of Appeal held that a trafficking victim's initial agreement to "
            "travel to the UK did not constitute consent to subsequent exploitation. "
            "Victim had been deceived about the nature of work. Court established "
            "that consent given based on false information is no consent at all, "
            "and that the prosecution need not prove complete absence of consent "
            "where deception or abuse of vulnerability is established."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Directive 2011/36/EU — Consent Provisions",
        "law": "Directive 2011/36/EU, Article 2(4)",
        "year": 2011,
        "summary": (
            "EU Directive Article 2(4) provides that consent of a victim of "
            "trafficking is irrelevant where any of the prohibited means have been "
            "used. Article 2(5) further provides that where the victim is a child, "
            "consent is irrelevant even in the absence of prohibited means. "
            "Transposed into all 27 Member States' national law. Interpretation "
            "varies: some courts still scrutinize victim behavior for signs of "
            "'voluntary' participation."
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Debt-Induced 'Consent' — IOM Documentation of Consent Coercion",
        "exploitation_type": "debt_bondage",
        "sector": "multiple",
        "summary": (
            "IOM counter-trafficking cases across Southeast Asia and Gulf document "
            "consistent pattern: workers 'consent' to exploitative conditions because "
            "they owe recruitment debts of USD 2,000-15,000 and face social/financial "
            "ruin if they return home without repaying. Workers technically free to "
            "leave but economically unable to do so. Legal frameworks in many "
            "destination countries treat departure as 'consent' to conditions, "
            "ignoring the coercive debt structure."
        ),
        "source": "IOM Counter-Trafficking Data Portal / CTDC",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "United States v. Kozminski (1988) — Coercion Beyond Physical Force",
        "court": "Supreme Court of the United States",
        "year": 1988,
        "summary": (
            "US Supreme Court held that involuntary servitude under the 13th "
            "Amendment requires proof of coercion through physical force, threat of "
            "physical force, or threat of legal coercion. Narrowly interpreted, this "
            "excluded psychological coercion. Congress responded by enacting the TVPA "
            "(2000) which explicitly covers 'serious harm' including psychological "
            "coercion, reputational threats, and abuse of legal process. The case "
            "demonstrates how narrow consent frameworks fail to capture modern "
            "exploitation."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "TVPA Definition of Coercion — 22 USC § 7102(3)",
        "law": "Trafficking Victims Protection Act, 22 USC § 7102(3)",
        "year": 2000,
        "summary": (
            "TVPA defines coercion broadly: (A) threats of serious harm (including "
            "non-physical), (B) physical restraint, (C) abuse or threatened abuse "
            "of the legal process. 'Serious harm' includes psychological, financial, "
            "or reputational harm. Specifically designed to address situations where "
            "workers 'consent' to exploitative conditions due to non-physical "
            "coercion — a direct response to the narrow Kozminski holding."
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Bellagio-Harvard Guidelines on Legal Parameters of Human Trafficking (2015)",
        "summary": (
            "Academic-policy guidelines drafted by international trafficking experts "
            "at Harvard/Bellagio. Key principles: (1) consent is a continuing "
            "condition that can be withdrawn at any time; (2) consent obtained "
            "through any form of coercion — physical, psychological, economic, "
            "social — is not valid consent; (3) structural vulnerability (poverty, "
            "immigration status, language barriers) creates conditions where free "
            "consent is impossible. Guidelines widely cited in ECHR, UK, and "
            "Australian jurisprudence."
        ),
        "source": "Journal of International Criminal Justice / Gallagher (2015)",
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "UK Modern Slavery Act — 'Consent' Defense Limitations in Practice",
        "exploitation_type": "consent_under_duress",
        "sector": "multiple",
        "summary": (
            "Analysis of UK Modern Slavery Act prosecutions (2015-2023) shows courts "
            "increasingly rejecting consent defenses where structural vulnerability "
            "is present. In R v. Zielinski [2017], court found that Eastern European "
            "workers who 'agreed' to exploitative conditions on UK farms did not "
            "provide meaningful consent because they lacked language skills, knowledge "
            "of rights, and economic alternatives. Anti-Slavery International notes "
            "this as a positive trend but inconsistently applied across jurisdictions."
        ),
        "source": "CPS / Anti-Slavery International / Independent Anti-Slavery Commissioner",
    },
]
