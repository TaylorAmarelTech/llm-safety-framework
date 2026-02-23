"""Philippine trafficking in persons cases and OFW labor exploitation decisions."""

PH_TRAFFICKING_FACTS: list[dict] = [
    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 1: TRAFFICKING IN PERSONS ACT CASES (RA 9208 / RA 10364)
    # ═══════════════════════════════════════════════════════════════════════

    # ── Qualified Trafficking (minors, public officials, syndicates) ─────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Casio, G.R. No. 211465 (2015) — Consent Irrelevant in Trafficking",
        "court": "Supreme Court of the Philippines",
        "year": 2015,
        "summary": (
            "Supreme Court affirmed conviction for qualified trafficking under "
            "RA 9208. Established that victim's consent is irrelevant when means "
            "of trafficking (deception, coercion, abuse of vulnerability) are "
            "present. Even if the victim voluntarily went with the accused, the "
            "use of fraudulent promises vitiates consent. Landmark ruling "
            "strengthening Philippine anti-trafficking jurisprudence."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 211465",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Lalli, G.R. No. 195419 (2012) — Trafficking of Minor for Prostitution",
        "court": "Supreme Court of the Philippines",
        "year": 2012,
        "summary": (
            "Accused recruited a 16-year-old girl from Zamboanga del Sur with "
            "promise of employment as a domestic helper in Malaysia but delivered "
            "her to a prostitution den. Supreme Court upheld qualified trafficking "
            "conviction. Means element (fraud/deception) not required when victim "
            "is a minor under Sec. 4(a) of RA 9208. Life imprisonment and "
            "PHP 2 million fine imposed."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 195419",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Hirang, G.R. No. 223528 (2017) — Syndicate Trafficking Conviction",
        "court": "Supreme Court of the Philippines",
        "year": 2017,
        "summary": (
            "Three or more persons acting in concert recruited victims from "
            "Visayas provinces for domestic work abroad. Victims subjected to "
            "debt bondage and physical abuse at destination. Convicted of "
            "qualified trafficking committed by a syndicate under Sec. 6(c) "
            "of RA 9208 as amended by RA 10364. Each accused sentenced to "
            "life imprisonment."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 223528",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Rodriguez, G.R. No. 211721 (2015) — Public Official Complicity",
        "court": "Supreme Court of the Philippines",
        "year": 2015,
        "summary": (
            "Local government official convicted of qualified trafficking for "
            "facilitating recruitment of minors for sexual exploitation. The "
            "involvement of a public officer automatically qualifies the "
            "offense under Sec. 6(a) of RA 9208. Court emphasized that public "
            "officers who participate in, or turn a blind eye to, trafficking "
            "face maximum penalties."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 211721",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, G.R. No. 234017 (2018) — Parent as Trafficker",
        "court": "Supreme Court of the Philippines",
        "year": 2018,
        "summary": (
            "Mother convicted of qualified trafficking for selling her own "
            "children for sexual exploitation. Supreme Court ruled that "
            "parental authority does not shield a parent from trafficking "
            "liability. The offense is qualified when committed by an ascendant "
            "under Sec. 6(a). Life imprisonment and PHP 2 million fine. Court "
            "ordered DSWD custody of children and mandatory counseling."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 234017",
    },

    # ── Simple Trafficking Cases ─────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Ramirez, G.R. No. 217978 (2018) — Bar Waitress Trafficking",
        "court": "Supreme Court of the Philippines",
        "year": 2018,
        "summary": (
            "Accused recruited young women from rural Leyte for 'waitressing' "
            "jobs in Manila bars. Victims were instead forced into commercial "
            "sexual exploitation. Convicted of simple trafficking under "
            "Sec. 4(a) of RA 9208: recruitment through deception for the "
            "purpose of exploitation. Twenty years imprisonment and fine imposed."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 217978",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Ejercito, G.R. No. 229861 (2020) — Labor Trafficking of Adults",
        "court": "Supreme Court of the Philippines",
        "year": 2020,
        "summary": (
            "Accused recruited adult workers from Mindanao promising factory "
            "jobs in Cavite. Workers found deplorable conditions: 16-hour days, "
            "wages withheld, locked dormitories, confiscated IDs. Court found "
            "all elements of trafficking under Sec. 4(a): act (recruitment), "
            "means (deception and coercion), and purpose (forced labor). "
            "Convicted and sentenced to twenty years imprisonment."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 229861",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Spouses Ong, RTC Cebu (2019) — Domestic Servitude",
        "court": "Regional Trial Court, Cebu City",
        "year": 2019,
        "summary": (
            "Married couple convicted of trafficking for keeping a young woman "
            "from a poor Visayan family as unpaid domestic servant for over "
            "three years. Victim was confined to the household, denied education, "
            "beaten for disobedience. Court applied RA 9208 Sec. 4(a) finding "
            "that domestic servitude constitutes trafficking when accomplished "
            "through abuse of vulnerability and coercion."
        ),
        "source": "Regional Trial Court, Cebu City Branch 58",
    },

    # ── Attempted Trafficking Cases ──────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Dela Cruz, RTC Manila (2020) — Attempted Trafficking at Airport",
        "court": "Regional Trial Court, Manila",
        "year": 2020,
        "summary": (
            "Immigration officer at NAIA flagged suspicious travel of three "
            "young women recruited by accused for 'tourism jobs' in Malaysia. "
            "Investigation revealed no legitimate employer. Accused convicted "
            "of attempted trafficking under Sec. 4(a) in relation to "
            "Sec. 26 of RA 9208 as amended. Court held that departure from "
            "the Philippines is not necessary to consummate the offense; "
            "recruitment with intent to exploit is sufficient."
        ),
        "source": "Regional Trial Court, Manila Branch 35",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Santos, RTC Pasay (2021) — Attempted Trafficking via Social Media",
        "court": "Regional Trial Court, Pasay City",
        "year": 2021,
        "summary": (
            "Accused used Facebook to recruit women with offers of high-paying "
            "overseas jobs. NBI cyber-trafficking unit conducted entrapment "
            "operation. Convicted of attempted trafficking. Court held that "
            "solicitation and recruitment through social media platforms "
            "constitutes a direct overt act of trafficking, punishable "
            "even when no victim actually travels."
        ),
        "source": "Regional Trial Court, Pasay City Branch 117",
    },

    # ── Online Sexual Exploitation of Children (OSEC) ────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Brozoto, RTC Iligan (2022) — OSEC Live-Streaming",
        "court": "Regional Trial Court, Iligan City",
        "year": 2022,
        "summary": (
            "Accused facilitated live-streaming sexual abuse of children to "
            "foreign buyers via encrypted messaging apps. Convicted under "
            "RA 9208 as amended (trafficking), RA 9775 (Anti-Child Pornography), "
            "and RA 10175 (Cybercrime Prevention). Court imposed life "
            "imprisonment. OSEC cases in the Philippines increased 264% "
            "between 2017 and 2021 per IJM data."
        ),
        "source": "Regional Trial Court, Iligan City; IJM Philippines",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, RTC Lapu-Lapu (2023) — Mother as OSEC Facilitator",
        "court": "Regional Trial Court, Lapu-Lapu City",
        "year": 2023,
        "summary": (
            "Mother convicted of qualified trafficking for facilitating OSEC "
            "of her own children aged 5-10 for foreign customers paying via "
            "money transfer services. Joint IACAT-AHTRAD-IJM rescue operation. "
            "Life imprisonment imposed. Court emphasized that OSEC constitutes "
            "one of the 'worst forms of trafficking' and that familial "
            "relationship aggravates the offense."
        ),
        "source": "Regional Trial Court, Lapu-Lapu City; PNP WCPC; IJM",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OSEC Prevalence in the Philippines — IJM/ECPAT Data",
        "metric": "Online Sexual Exploitation of Children referrals to PH authorities",
        "value": "Over 3 million unique images/videos reported annually",
        "year": 2023,
        "summary": (
            "The Philippines is identified as the global epicenter of OSEC. "
            "NCMEC CyberTipline reported 4.1 million reports involving the "
            "Philippines in 2022. IJM has assisted in the rescue of over "
            "1,300 OSEC victims since 2011. Key drivers: widespread internet "
            "access, poverty, English proficiency enabling interaction with "
            "foreign buyers, and money transfer accessibility."
        ),
        "source": "IJM Philippines / NCMEC / ECPAT / US State Dept TIP Report 2023",
    },

    # ── Labor Trafficking Cases ──────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, RTC Quezon City (2019) — Factory Worker Trafficking",
        "court": "Regional Trial Court, Quezon City",
        "year": 2019,
        "summary": (
            "Operators of a garment factory in Quezon City convicted of "
            "trafficking under RA 9208 for recruiting workers from Samar "
            "and Leyte under false promises. Workers confined to factory "
            "compound, forced to work 14-hour days, wages withheld for months, "
            "IDs confiscated. DOLE inspection triggered IACAT investigation. "
            "Sentences of 20 years to life imprisonment."
        ),
        "source": "Regional Trial Court, Quezon City; DOLE / IACAT",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, RTC Davao (2021) — Banana Plantation Forced Labor",
        "court": "Regional Trial Court, Davao City",
        "year": 2021,
        "summary": (
            "Plantation supervisor convicted of trafficking for recruiting "
            "indigenous Lumad workers through debt bondage. Workers advanced "
            "money for transport and supplies, then forced to repay through "
            "labor at below-minimum wages. Movement restricted to plantation "
            "compound. NCIP intervention led to IACAT case filing."
        ),
        "source": "Regional Trial Court, Davao City; NCIP / IACAT",
    },

    # ── Recruitment for Overseas Forced Labor ────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, G.R. No. 238835 (2020) — Large-Scale Illegal Recruitment",
        "court": "Supreme Court of the Philippines",
        "year": 2020,
        "summary": (
            "Agency operators convicted of large-scale illegal recruitment "
            "(economic sabotage) under RA 8042 as amended by RA 10022 for "
            "deploying over 50 OFWs to Saudi Arabia with fraudulent contracts. "
            "Workers arrived to find different employers, lower salaries, and "
            "confiscated passports. Sentenced to life imprisonment and "
            "PHP 5 million fine. Court ordered solidary liability with "
            "foreign principal for money claims."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 238835",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Bautista, RTC Pasay (2022) — Deployment to Non-Verified Employer",
        "court": "Regional Trial Court, Pasay City",
        "year": 2022,
        "summary": (
            "Licensed recruitment agency officer convicted for deploying "
            "Filipino workers to a construction company in UAE that was not "
            "verified by POLO Dubai. Workers experienced wage withholding "
            "and document confiscation. Court applied the principle that "
            "deployment to a non-accredited or non-verified employer "
            "constitutes illegal recruitment even by a licensed agency."
        ),
        "source": "Regional Trial Court, Pasay City; DMW enforcement records",
    },

    # ── OFW Victims in Gulf States ───────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-SA",
        "title": "OFW Domestic Workers in Saudi Arabia — Systemic Exploitation Pattern",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Recurring pattern documented by POLO Riyadh and Migrante: "
            "Filipina domestic workers in Saudi Arabia face contract "
            "substitution (lower salary than promised), 18-20 hour workdays, "
            "no rest days, physical and sexual abuse, food deprivation, and "
            "salary withholding for months. Kafala system prevents workers "
            "from leaving employer. An average of 5-7 distressed OFWs per "
            "day seek shelter at POLO-OWWA facilities in KSA."
        ),
        "source": "POLO Riyadh / OWWA / Migrante International",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-KW",
        "title": "Joanna Demafelis Case — Filipina Found Dead in Freezer in Kuwait (2018)",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Filipina domestic worker Joanna Demafelis found dead in a freezer "
            "in an abandoned apartment in Kuwait in February 2018. She had been "
            "missing for over a year. Employers (Lebanese-Syrian couple) fled "
            "Kuwait. The case triggered President Duterte's total deployment "
            "ban to Kuwait and prompted the bilateral labor agreement between "
            "the Philippines and Kuwait signed in May 2018. One of the most "
            "prominent OFW abuse cases in Philippine history."
        ),
        "source": "DFA / DMW / CNN Philippines / Philippine Star",
    },

    # ── Filipino Fishermen Trafficked to Foreign Vessels ──────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-TW",
        "title": "Filipino Fishermen on Taiwanese Distant-Water Fishing Vessels",
        "exploitation_type": "restriction_of_movement",
        "sector": "fishing",
        "summary": (
            "Filipino fishermen recruited through manning agencies for "
            "Taiwanese-flagged long-line tuna vessels. Workers report being "
            "at sea for 12-18 months without shore leave, 20-hour work days, "
            "physical abuse by vessel captains, inadequate food and water, "
            "wages withheld until contract end. ILO Work in Fishing Convention "
            "(C188) provisions violated. Greenpeace and EJF investigations "
            "documented cases. Philippines and Taiwan lack formal bilateral "
            "protections due to diplomatic status."
        ),
        "source": "Greenpeace / EJF / ILO / Center for Migrant Advocacy",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-KR",
        "title": "Filipino Fishermen on Korean Distant-Water Vessels — Death at Sea",
        "exploitation_type": "physical_sexual_violence",
        "sector": "fishing",
        "summary": (
            "Multiple cases of Filipino fishermen dying or being seriously "
            "injured aboard Korean distant-water fishing vessels. Workers "
            "report beatings by Korean captains, 18-22 hour work days, "
            "confiscated documents, and no access to medical care. Deaths "
            "investigated by NFMW (National Federation of Mission for "
            "Filipino Migrant Workers). South Korea's Distant-Water "
            "Fisheries Development Act reformed in 2021 to address abuses."
        ),
        "source": "NFMW / Advocates for Public Interest Law (APIL, Korea) / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Filipino Fishermen Trafficked via Indonesia — Tual/Benjina Cases",
        "exploitation_type": "restriction_of_movement",
        "sector": "fishing",
        "summary": (
            "Filipino fishermen recruited through informal brokers deployed "
            "to fishing vessels operating out of Indonesian ports (Tual, "
            "Benjina, Ambon). Workers confined to vessels, forced to work "
            "in hazardous conditions, denied adequate food. Some held for "
            "years. Repatriation complicated by lack of documentation. "
            "DFA and MARINA coordinated rescue of stranded Filipino fishermen."
        ),
        "source": "DFA / MARINA / Associated Press / ILO",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 2: KEY OFW PROTECTION DECISIONS
    # ═══════════════════════════════════════════════════════════════════════

    # ── Illegal Dismissal of OFWs ────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Sameer Overseas v. Cabiles, G.R. No. 170139 (2014) — Illegal Dismissal Damages",
        "court": "Supreme Court of the Philippines",
        "year": 2014,
        "summary": (
            "Supreme Court declared the clause in RA 8042 Sec. 10 limiting "
            "illegally dismissed OFW's money claims to three months salary "
            "for every year of unexpired contract as UNCONSTITUTIONAL. Ruled "
            "that OFWs are entitled to the same protection as local workers "
            "and the full unexpired portion of the contract. Landmark "
            "decision equalizing OFW rights with domestic workers."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 170139",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Serrano v. Gallant Maritime, G.R. No. 167614 (2009) — Equal Protection for OFWs",
        "court": "Supreme Court of the Philippines, En Banc",
        "year": 2009,
        "summary": (
            "En banc decision ruling that the 3-month salary cap in RA 8042 "
            "Sec. 10 for illegally dismissed OFWs with contracts of one year "
            "or more is unconstitutional for violating the equal protection "
            "clause. OFWs entitled to salary for the entire unexpired "
            "portion of contract, same as local workers under the Labor Code. "
            "Seminal case in OFW labor rights jurisprudence."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 167614",
    },

    # ── Money Claims Against Recruitment Agencies ────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Becmen Service Exporter v. Spouses Cuaresma, G.R. No. 182978 (2009)",
        "court": "Supreme Court of the Philippines",
        "year": 2009,
        "summary": (
            "Supreme Court affirmed that recruitment agencies and their "
            "foreign principals are jointly and solidarily liable for all "
            "claims arising from employer-employee relationship, including "
            "death and disability benefits. Agency cannot escape liability "
            "by claiming it was merely a placement agency. The solidary "
            "liability under RA 8042 is designed to protect OFWs."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 182978",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Philippine Transmarine Carriers v. Aligway, G.R. No. 201792 (2016)",
        "court": "Supreme Court of the Philippines",
        "year": 2016,
        "summary": (
            "Manning agency held jointly and solidarily liable with foreign "
            "principal for disability benefits of Filipino seafarer who "
            "contracted illness during employment. Court emphasized that "
            "manning agencies are not merely conduits but are co-employers "
            "with the foreign principal under Philippine maritime labor law."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 201792",
    },

    # ── Repatriation Rights ──────────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Eastern Shipping Lines v. POEA, G.R. No. 76633 (1987) — Mandatory Repatriation",
        "court": "Supreme Court of the Philippines",
        "year": 1987,
        "summary": (
            "Supreme Court upheld POEA's authority to order immediate "
            "repatriation of OFWs at employer's expense. The obligation to "
            "repatriate is mandatory and cannot be waived by contract. "
            "Employer must bear all costs of return transportation regardless "
            "of cause of termination."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 76633",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10022 Sec. 15 — Mandatory Repatriation of OFWs",
        "summary": (
            "The repatriation of the worker and transport of personal "
            "belongings shall be the primary responsibility of the agency "
            "which recruited or deployed the worker and the foreign "
            "principal/employer. Failure to repatriate constitutes illegal "
            "recruitment. Emergency repatriation due to war, epidemic, or "
            "natural disaster funded by OWWA and the Assistance-to-Nationals "
            "Fund. DMW coordinates repatriation through POLO offices."
        ),
        "source": "RA 10022 (Amended Migrant Workers Act), Section 15",
    },

    # ── Joint and Solidary Liability ─────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Sunace International v. NLRC, G.R. No. 161757 (2006) — Solidary Liability Scope",
        "court": "Supreme Court of the Philippines",
        "year": 2006,
        "summary": (
            "Court clarified that the solidary liability of the recruitment "
            "agency with the foreign employer covers the entire duration of "
            "the original employment contract, including any extensions agreed "
            "to by the worker and the foreign employer, provided the agency "
            "was aware of or consented to the extension. If the extension "
            "was without the agency's knowledge, liability is limited to the "
            "original contract period."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 161757",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Sto. Tomas v. Salac, G.R. No. 152642 (2012) — Agency Liability for All Claims",
        "court": "Supreme Court of the Philippines",
        "year": 2012,
        "summary": (
            "Supreme Court upheld that recruitment agencies are solidarily "
            "liable with the foreign principal for all monetary claims "
            "including unpaid wages, overtime pay, underpayment, illegal "
            "deductions, refund of placement fees, and damages. This "
            "liability cannot be negated by contractual stipulations between "
            "the agency and the foreign employer. Workers need only file "
            "claims against the local agency."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 152642",
    },

    # ── Jurisdiction: NLRC vs Regular Courts ─────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Santiago v. CF Sharp Crew Management, G.R. No. 162419 (2007)",
        "court": "Supreme Court of the Philippines",
        "year": 2007,
        "summary": (
            "Supreme Court ruled that the NLRC (through Labor Arbiters) has "
            "original and exclusive jurisdiction over all claims arising from "
            "employer-employee relationships involving OFWs, including "
            "claims for actual, moral, and exemplary damages. Regular courts "
            "have no jurisdiction over these claims. This ensures OFWs have "
            "access to expedited labor dispute resolution."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 162419",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Cadalin v. POEA, G.R. No. 104776 (1996) — Prescriptive Period for OFW Claims",
        "court": "Supreme Court of the Philippines",
        "year": 1996,
        "summary": (
            "Supreme Court ruled that money claims of OFWs prescribe in "
            "three years from the time the cause of action accrued, applying "
            "Article 291 of the Labor Code rather than the 10-year "
            "prescription under the Civil Code. The prescriptive period "
            "begins to run from the date of illegal dismissal or last "
            "salary payment, whichever is applicable."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 104776",
    },

    # ── Contract Substitution ────────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "EDI-Staffbuilders v. NLRC, G.R. No. 145587 (2007) — Contract Substitution Void",
        "court": "Supreme Court of the Philippines",
        "year": 2007,
        "summary": (
            "Supreme Court declared that any alteration or substitution of "
            "the POEA-approved employment contract is void and shall not be "
            "the basis of any claim or cause of action to the prejudice of "
            "the OFW. The POEA-approved contract governs the employment "
            "relationship. If the foreign employer imposes different "
            "conditions, the worker is entitled to the benefits under the "
            "POEA-approved contract or the actual contract, whichever is "
            "more favorable."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 145587",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-SA",
        "title": "Contract Substitution Pattern — Saudi Arabia Domestic Workers",
        "exploitation_type": "deception",
        "sector": "domestic_work",
        "summary": (
            "Widespread pattern documented by DMW and POLO Riyadh: "
            "OFWs sign POEA-approved contract in Manila specifying SAR 1,500 "
            "monthly salary, one rest day per week, and defined duties. Upon "
            "arrival in Saudi Arabia, employer presents new contract in Arabic "
            "with lower salary (SAR 800-1,000), no rest day, and expanded "
            "duties (multiple households). Workers sign under duress as "
            "passports have been taken. DMW records over 2,000 contract "
            "substitution complaints annually from KSA alone."
        ),
        "source": "DMW / POLO Riyadh / Migrante International",
    },

    # ── Wage Theft Cases from Gulf States ────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-SA",
        "title": "Wage Theft in Saudi Arabia — POLO-Assisted Recovery",
        "exploitation_type": "withholding_wages",
        "sector": "multiple",
        "summary": (
            "POLO Riyadh and Jeddah process an average of 3,500-4,000 labor "
            "cases annually involving Filipino workers, the majority relating "
            "to non-payment or underpayment of wages. Common pattern: "
            "employers withhold 3-8 months of salary, then terminate the "
            "worker and arrange immediate departure. Workers who file claims "
            "through POLO face 6-18 month resolution timelines through "
            "Saudi labor courts. Recovery rate is approximately 40-50% of "
            "total claims filed."
        ),
        "source": "POLO Riyadh / POLO Jeddah / DMW Annual Reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-QA",
        "title": "Filipino Construction Workers in Qatar — Wage Withholding",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "Filipino construction workers in Qatar report systematic wage "
            "withholding through subcontracting chains. Pattern: main "
            "contractor pays sub-contractor, sub-contractor delays payment "
            "to labor supplier, labor supplier withholds wages for 2-4 months. "
            "Workers cannot file complaints without employer's NOC (No "
            "Objection Certificate) until Qatar's 2020 labor reforms. "
            "POLO Doha assisted 800+ wage claim cases in 2022."
        ),
        "source": "POLO Doha / DMW / OWWA Qatar",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 3: MIGRATION CORRIDOR-SPECIFIC CASES
    # ═══════════════════════════════════════════════════════════════════════

    # ── PH-SA (Saudi Arabia) ─────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-SA",
        "title": "Death of OFW in Riyadh — Employer Abuse (2022)",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Filipina domestic worker died in employer's home in Riyadh "
            "under suspicious circumstances. Autopsy revealed signs of "
            "physical abuse and malnutrition. Philippine embassy requested "
            "investigation from Saudi authorities. Case highlighted the "
            "continuing vulnerability of domestic workers under the kafala "
            "system despite Saudi labor reforms. DFA issued diplomatic "
            "representations to the Kingdom."
        ),
        "source": "DFA / Philippine Embassy Riyadh / Inquirer.net",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "corridor": "PH-SA",
        "title": "OFW Distressed Cases in Saudi Arabia — Annual Data",
        "metric": "Annual distressed OFW cases handled by POLO KSA",
        "value": "4,500-5,000 cases annually",
        "year": 2023,
        "summary": (
            "POLO offices in Saudi Arabia (Riyadh, Jeddah, Al Khobar) handle "
            "4,500-5,000 distressed OFW cases annually. Breakdown: non-payment "
            "of wages (35%), physical abuse (15%), contract substitution (12%), "
            "sexual abuse (8%), illegal termination (20%), other (10%). "
            "OWWA shelters in KSA accommodate 200-300 distressed workers "
            "at any given time awaiting repatriation or case resolution."
        ),
        "source": "DMW / POLO KSA / OWWA Annual Report 2023",
    },

    # ── PH-AE (UAE) ─────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-AE",
        "title": "OFW Hospitality Workers in Dubai — Contract Substitution",
        "exploitation_type": "deception",
        "sector": "hospitality",
        "summary": (
            "Filipino workers recruited for hotel positions in Dubai at "
            "AED 2,500-3,000 per month arrive to find employment with "
            "cleaning or catering subcontractors at AED 1,200-1,500. "
            "Passport confiscated by employer despite UAE's 2020 ban on "
            "document retention. Workers housed in overcrowded labor camps "
            "far from city center. POLO Abu Dhabi and POLO Dubai handle "
            "over 1,200 contract substitution cases per year."
        ),
        "source": "POLO Abu Dhabi / POLO Dubai / DMW",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-AE",
        "title": "Filipino Nurses in UAE — Underpayment and Excessive Hours",
        "exploitation_type": "excessive_overtime",
        "sector": "healthcare",
        "summary": (
            "Filipino nurses deployed to private clinics in UAE report being "
            "assigned to work 60-72 hours per week despite contracts specifying "
            "48 hours. Overtime not compensated. Nurses fear termination and "
            "deportation if they refuse. Employment visa tied to sponsoring "
            "clinic. POLO Dubai notes healthcare worker complaints have "
            "increased 30% since 2020."
        ),
        "source": "POLO Dubai / Philippine Nurses Association-UAE / DMW",
    },

    # ── PH-KW (Kuwait) ──────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "corridor": "PH-KW",
        "title": "Philippines-Kuwait Bilateral Labor Agreement (2018)",
        "summary": (
            "Signed May 2018 following the Joanna Demafelis case. Key "
            "provisions: workers retain possession of passports, workers "
            "have right to a mobile phone, workers entitled to adequate "
            "food and housing, no transfer of workers without consent, "
            "24-hour hotline for distressed workers, and a joint committee "
            "to monitor implementation. Kuwait subsequently enacted domestic "
            "worker law (Law No. 68 of 2015). Compliance remains inconsistent."
        ),
        "source": "DFA / DMW / Kuwait Ministry of Interior",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-KW",
        "title": "Runaway OFWs in Kuwait — Shelter Statistics",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Philippine Embassy shelter in Kuwait accommodates 200-250 "
            "runaway domestic workers at any given time. Common reasons for "
            "fleeing: non-payment of wages (40%), physical abuse (25%), "
            "sexual harassment (15%), excessive working hours with no rest "
            "day (20%). Workers face absconding charges under Kuwaiti law "
            "if they leave their employer, creating a deterrent against "
            "reporting abuse. Embassy facilitates amicable settlement or "
            "repatriation."
        ),
        "source": "Philippine Embassy Kuwait / OWWA / Migrante-Kuwait",
    },

    # ── PH-QA (Qatar) ───────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-QA",
        "title": "Filipino Workers in Qatar World Cup Infrastructure Projects",
        "exploitation_type": "debt_bondage",
        "sector": "construction",
        "summary": (
            "Filipino workers deployed to Qatar for FIFA World Cup 2022 "
            "infrastructure projects reported paying PHP 80,000-150,000 in "
            "recruitment fees despite the no-placement-fee policy. Workers "
            "employed through subcontracting chains with limited oversight. "
            "Post-reform Qatar allowed workers to change employers without "
            "NOC from 2020, but Filipino workers reported difficulty "
            "exercising this right due to employer pressure and housing "
            "tied to employment."
        ),
        "source": "POLO Doha / BWI / Amnesty International",
    },

    # ── PH-HK (Hong Kong) ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-HK",
        "title": "Underpayment of Filipino Domestic Helpers in Hong Kong",
        "exploitation_type": "withholding_wages",
        "sector": "domestic_work",
        "summary": (
            "Filipino domestic helpers in Hong Kong systematically underpaid "
            "below the Minimum Allowable Wage (HKD 4,870/month as of 2023). "
            "Agencies in Manila and HK collude: worker signs contract at MAW "
            "but receives HKD 3,000-3,500 after agency fee deductions for "
            "8-10 months. Two-week rule (must find new employer within 14 days "
            "of contract termination or leave HK) deters workers from "
            "reporting underpayment. Mission for Migrant Workers assists "
            "500+ underpayment complaints annually."
        ),
        "source": "Mission for Migrant Workers HK / Justice Centre HK / POLO HK",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-HK",
        "title": "Erwiana Sulistyaningsih Abuse Case — Impact on Filipino FDHs",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Although Erwiana was an Indonesian domestic worker, her 2014 "
            "abuse case in Hong Kong had direct impact on Filipino domestic "
            "helpers. The case — employer Law Wan-tung convicted of grievous "
            "bodily harm and sentenced to 6 years — led to enhanced "
            "protections for all FDHs including Filipinos: mandatory rest "
            "days enforcement, increased labor inspections, and the HKSAR "
            "government's review of the two-week rule. APMM and Migrante-HK "
            "used the case to advocate for Filipino FDH protections."
        ),
        "source": "APMM / Migrante-HK / South China Morning Post",
    },

    # ── PH-SG (Singapore) ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-SG",
        "title": "Filipino Domestic Workers in Singapore — Agency Fee Debt",
        "exploitation_type": "debt_bondage",
        "sector": "domestic_work",
        "summary": (
            "Filipino domestic workers in Singapore charged SGD 4,000-8,000 "
            "in agency fees despite regulations capping fees at 2 months' "
            "salary. Debt recovered through 6-10 months of salary deductions. "
            "MOM (Ministry of Manpower) has capped agency fees for employers "
            "but enforcement on worker-side fees in the Philippines is weak. "
            "HOME Singapore assists Filipino domestic workers with salary "
            "claims and debt-related exploitation cases."
        ),
        "source": "HOME Singapore / TWC2 / MOM / POLO Singapore",
    },

    # ── PH-MY (Malaysia) ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-MY",
        "title": "Filipino Workers in Sabah — Undocumented and Vulnerable",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "agriculture",
        "summary": (
            "An estimated 800,000 Filipinos reside in Sabah, Malaysia, many "
            "undocumented. Workers in palm oil plantations and fishing "
            "industries face exploitation: wages below minimum, no labor "
            "protections, vulnerability to arbitrary arrest and deportation. "
            "IMM13 document holders have limited work rights. Philippine "
            "consulate in Kota Kinabalu handles 1,000+ distress cases annually "
            "but access to justice is limited for undocumented workers."
        ),
        "source": "Philippine Consulate Kota Kinabalu / IOM / Migrante-Sabah",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-MY",
        "title": "Filipino Factory Workers in Malaysian Electronics — Forced Labor Indicators",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Filipino workers deployed to Malaysian electronics factories "
            "through Philippine recruitment agencies report: recruitment fees "
            "of PHP 50,000-100,000, passport confiscation upon arrival, "
            "crowded dormitories (12-20 per room), mandatory overtime of "
            "60-72 hours per week, and deductions for housing and food "
            "exceeding Malaysian legal limits. Several Malaysian electronics "
            "companies subject to US CBP Withhold Release Orders for forced "
            "labor indicators."
        ),
        "source": "Verité / US CBP / POLO Kuala Lumpur / DMW",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 4: ENFORCEMENT AND INSTITUTIONAL FACTS
    # ═══════════════════════════════════════════════════════════════════════

    # ── IACAT Operations and Statistics ──────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "IACAT Trafficking Convictions — Annual Statistics",
        "metric": "Annual trafficking conviction rate",
        "value": "281 convictions (2005-2023 cumulative)",
        "year": 2023,
        "summary": (
            "The Inter-Agency Council Against Trafficking (IACAT) has secured "
            "281 trafficking convictions from 2005 to 2023. Annual convictions "
            "have increased from 3-5 per year (2005-2010) to 30-45 per year "
            "(2019-2023). Conviction rate improved from 10% to approximately "
            "35% of cases filed. IACAT coordinates 18 government agencies "
            "including DOJ, DSWD, NBI, PNP, DFA, and DMW. Cases pending: "
            "over 700 as of 2023."
        ),
        "source": "IACAT / DOJ / US State Dept TIP Report 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "IACAT Rescue Operations — 2022-2023",
        "metric": "Victims rescued through IACAT-coordinated operations",
        "value": "1,247 victims rescued (2022); 1,389 victims rescued (2023)",
        "year": 2023,
        "summary": (
            "IACAT-coordinated operations rescued 1,247 trafficking victims "
            "in 2022 and 1,389 in 2023. Operations include: airport "
            "interceptions (NAIA Task Force Against Trafficking), entrapment "
            "operations (NBI-AHTRAD), and community-based rescue (DSWD). "
            "Approximately 60% of victims are minors. OSEC victims account "
            "for the fastest-growing category."
        ),
        "source": "IACAT / PNP WCPC / NBI-AHTRAD / DSWD",
    },

    # ── NBI Anti-Trafficking Operations ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "NBI-AHTRAD Major Operations — Cybersex Den Raids",
        "exploitation_type": "sexual_exploitation",
        "sector": "cybercrime",
        "summary": (
            "The NBI Anti-Human Trafficking Division (AHTRAD) conducts "
            "regular raids on cybersex dens nationwide. In 2022-2023, "
            "NBI-AHTRAD conducted 78 operations resulting in 156 arrests "
            "and rescue of 423 victims including 187 minors. Operations "
            "coordinated with IJM, FBI, Homeland Security Investigations "
            "(HSI), and Australian Federal Police (AFP). Key areas: "
            "Pampanga, Cebu, Davao, and Metro Manila."
        ),
        "source": "NBI-AHTRAD / IJM Philippines / US DOJ",
    },
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "NBI Anti-Human Trafficking Division (AHTRAD)",
        "organization": "National Bureau of Investigation",
        "contact_type": "enforcement",
        "summary": (
            "NBI-AHTRAD is the primary investigative body for trafficking "
            "cases in the Philippines. Handles complex cases involving "
            "syndicates, OSEC operations, and cross-border trafficking. "
            "24/7 hotline for trafficking reports. Coordinates with "
            "international law enforcement through INTERPOL and bilateral "
            "mutual legal assistance treaties (MLATs)."
        ),
        "source": "NBI / IACAT",
    },

    # ── PNP Women and Children Protection Center ─────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "PNP-WCPC Anti-Trafficking Operations — Nationwide Enforcement",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "PNP Women and Children Protection Center (WCPC) maintains "
            "17 regional anti-trafficking task forces. In 2023, WCPC "
            "conducted 234 anti-trafficking operations, arrested 312 "
            "suspects, and rescued 876 victims. WCPC operates the "
            "Anti-Trafficking in Persons (ATIP) database tracking cases "
            "nationwide. Specialized units include: Anti-OSEC Group, "
            "Anti-Illegal Recruitment Group, and Anti-Child Labor Group."
        ),
        "source": "PNP WCPC / IACAT / Philippine Star",
    },
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "PNP Women and Children Protection Center (WCPC)",
        "organization": "Philippine National Police",
        "contact_type": "enforcement",
        "summary": (
            "PNP-WCPC is the frontline enforcement unit for trafficking cases. "
            "Operates WCPC hotline (02-532-5765) and coordinates with "
            "barangay-level Women and Children Protection Desks (WCPDs). "
            "WCPC officers receive specialized training on victim "
            "identification, trauma-informed interviewing, and evidence "
            "preservation for trafficking cases."
        ),
        "source": "PNP / IACAT",
    },

    # ── DSWD Rescue Operations ───────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "DSWD Recovery and Reintegration for Trafficking Victims",
        "metric": "Trafficking victims served by DSWD programs",
        "value": "2,100+ victims served annually",
        "year": 2023,
        "summary": (
            "DSWD's Recovery and Reintegration Program for Trafficked "
            "Persons (RRPTP) served 2,134 victims in 2023. Services include: "
            "temporary shelter (36 residential care facilities nationwide), "
            "psychosocial counseling, medical assistance, legal aid, "
            "livelihood assistance, and educational support. DSWD operates "
            "Haven for Women centers as specialized shelters for trafficked "
            "women and children."
        ),
        "source": "DSWD / IACAT Annual Report 2023",
    },
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "DSWD Anti-Trafficking Programs and Hotlines",
        "organization": "Department of Social Welfare and Development",
        "contact_type": "victim_support",
        "summary": (
            "DSWD operates multiple services for trafficking victims: "
            "Hotline 163 (Bantay Bata for child trafficking/abuse), "
            "DSWD Crisis Intervention Section, Haven for Women centers, "
            "and the Recovery and Reintegration Program. DSWD social workers "
            "are mandated to accompany trafficking victims during "
            "investigation and prosecution proceedings."
        ),
        "source": "DSWD / IACAT",
    },

    # ── One-Stop Service Centers for OFWs ────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW One-Stop Service Centers for OFWs — Establishment",
        "summary": (
            "DMW (Department of Migrant Workers, created by RA 11641 in 2021) "
            "operates One-Stop Service Centers (OSSCs) in NAIA and other "
            "international airports. OSSCs provide: pre-departure orientation "
            "seminars (PDOS), OFW information and assistance, anti-trafficking "
            "screening, and coordination with IACAT. NAIA OSSC screens "
            "departing OFWs for trafficking indicators and has intercepted "
            "over 3,000 potential trafficking victims since 2018."
        ),
        "source": "DMW / IACAT / OWWA",
    },

    # ── Assistance-to-Nationals (ATN) Fund ───────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "Assistance-to-Nationals (ATN) Fund — RA 8042 / RA 10022",
        "summary": (
            "The ATN Fund provides financial assistance to distressed OFWs "
            "abroad. Sources: PHP 100 million annual Congressional "
            "appropriation, fines from illegal recruitment cases, and "
            "contributions from OWWA. Used for: legal assistance, "
            "repatriation costs, medical treatment, temporary shelter, and "
            "burial assistance for deceased OFWs. DFA and Philippine embassies "
            "administer the fund through Philippine Overseas Labor Offices "
            "(POLOs). In 2022, ATN Fund disbursed PHP 1.2 billion assisting "
            "over 12,000 distressed OFWs."
        ),
        "source": "DFA / DMW / RA 8042 Sec. 25 / RA 10022",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "ATN Fund Disbursements — Annual Data",
        "metric": "Annual ATN Fund disbursements for distressed OFWs",
        "value": "PHP 1.2 billion (2022); PHP 1.4 billion (2023)",
        "year": 2023,
        "summary": (
            "ATN Fund disbursements have steadily increased: PHP 800 million "
            "(2019), PHP 950 million (2020, COVID repatriation surge), "
            "PHP 1.1 billion (2021), PHP 1.2 billion (2022), PHP 1.4 billion "
            "(2023). Largest expenditure categories: repatriation (35%), "
            "legal assistance (25%), medical (20%), and burial/death claims "
            "(15%). Middle East posts account for 60% of total disbursements."
        ),
        "source": "DFA / DMW Annual Reports",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 5: LEGAL PRINCIPLES FROM PHILIPPINE JURISPRUDENCE
    # ═══════════════════════════════════════════════════════════════════════

    # ── Consent Irrelevant in Trafficking of Minors ──────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, G.R. No. 244047 (2021) — Consent of Minor Irrelevant",
        "court": "Supreme Court of the Philippines",
        "year": 2021,
        "summary": (
            "Supreme Court reiterated that in trafficking cases involving "
            "minors, the prosecution need not prove the means element "
            "(threat, use of force, coercion, abduction, fraud, deception, "
            "abuse of power). Under RA 9208 Sec. 3(a), trafficking of "
            "children is established merely by showing the act (recruitment, "
            "transportation, harboring) and the purpose (exploitation). "
            "The child's apparent consent is absolutely irrelevant."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 244047",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9208 Sec. 3(a) — Means Element Not Required for Child Victims",
        "summary": (
            "Section 3(a) of the Anti-Trafficking in Persons Act explicitly "
            "provides that the 'means' element (threat, use of force, "
            "coercion, abduction, fraud, deception, abuse of power or "
            "vulnerability, giving/receiving of payments) is NOT required "
            "when the victim is a child under 18 years of age. The "
            "prosecution need only prove: (1) the act of trafficking "
            "(recruitment, transportation, transfer, harboring, provision, "
            "or receipt of persons), and (2) the purpose of exploitation. "
            "This aligns with the Palermo Protocol Art. 3(c)."
        ),
        "source": "RA 9208 (Anti-Trafficking in Persons Act of 2003), Sec. 3(a)",
    },

    # ── Attempted Trafficking is Punishable ──────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10364 Sec. 4-A — Attempted Trafficking Punishable",
        "summary": (
            "RA 10364 (Expanded Anti-Trafficking Act of 2012) added "
            "Sec. 4-A making attempted trafficking a separate offense "
            "punishable by 15 years imprisonment and PHP 500,000 to "
            "PHP 1 million fine. Attempted trafficking includes: hiring "
            "or recruiting persons for trafficking by means of force, "
            "fraud, or deception but before the act of trafficking is "
            "consummated. This closes the gap that previously required "
            "actual exploitation to occur before prosecution."
        ),
        "source": "RA 10364 (Expanded Anti-Trafficking in Persons Act of 2012)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, CA-G.R. CR-HC No. 13568 (2022) — Airport Interception Conviction",
        "court": "Court of Appeals of the Philippines",
        "year": 2022,
        "summary": (
            "Court of Appeals upheld conviction for attempted trafficking "
            "of three young women intercepted at NAIA by the IACAT Task "
            "Force. Accused had arranged travel documents, airline tickets, "
            "and contact persons at destination but victims were intercepted "
            "before departure. Court ruled that the completion of travel "
            "is not necessary; the preparatory acts combined with intent "
            "to exploit constitute attempted trafficking."
        ),
        "source": "Court of Appeals of the Philippines, CA-G.R. CR-HC No. 13568",
    },

    # ── Financial Assistance to Victims During Proceedings ───────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10364 Sec. 17-A — Mandatory Services for Trafficking Victims",
        "summary": (
            "RA 10364 mandates that trafficking victims shall be provided "
            "the following during investigation and prosecution: (a) emergency "
            "shelter and appropriate housing, (b) counseling, (c) free legal "
            "services, (d) medical and psychological care, (e) livelihood "
            "support, (f) educational assistance, and (g) skills training. "
            "These services are provided through DSWD, DOJ, CHED, and TESDA. "
            "Failure of government agencies to provide mandated services "
            "is subject to administrative sanctions."
        ),
        "source": "RA 10364, Sec. 17-A; DSWD Administrative Order No. 10-2010",
    },

    # ── Victim Protection Program ────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 6981 — Witness Protection, Security, and Benefit Act",
        "summary": (
            "Trafficking victims who serve as witnesses may be admitted to "
            "the DOJ Witness Protection Program under RA 6981. Benefits: "
            "secure housing, monthly subsistence allowance, livelihood "
            "assistance, free medical and dental services, and new identity "
            "documents when necessary. The program is administered by the "
            "DOJ Witness Protection, Security, and Benefit Program (WPSBP). "
            "Trafficking victims are given priority admission due to the "
            "severity of threats they face."
        ),
        "source": "RA 6981; DOJ Department Circular No. 58-2010",
    },

    # ── Non-Punishment Principle ─────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9208 Sec. 17 — Non-Punishment of Trafficked Persons",
        "summary": (
            "Section 17 of RA 9208 provides that trafficked persons shall "
            "not be penalized for crimes directly related to acts of "
            "trafficking or obedience to the order or command of the "
            "trafficker. This includes violations of immigration laws, "
            "labor laws, and other regulations committed as a direct result "
            "of being trafficked. Trafficked persons are recognized as "
            "victims, not offenders. This implements the international "
            "non-punishment principle from the Council of Europe Convention."
        ),
        "source": "RA 9208, Sec. 17; IACAT Guidelines on Non-Punishment",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Non-Punishment Applied — Trafficking Victim Cleared of Prostitution Charges",
        "court": "Regional Trial Court, Cebu City",
        "year": 2020,
        "summary": (
            "RTC Cebu dismissed prostitution charges against a trafficking "
            "victim applying the non-punishment principle under Sec. 17 "
            "of RA 9208. The accused was originally arrested during a raid "
            "on a bar but was subsequently identified as a trafficking "
            "victim. Court ruled that acts committed by the victim as a "
            "direct consequence of being trafficked cannot form the basis "
            "of criminal charges against the victim."
        ),
        "source": "Regional Trial Court, Cebu City; IACAT",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 6: ADDITIONAL COMPREHENSIVE FACTS
    # ═══════════════════════════════════════════════════════════════════════

    # ── Key Philippine Anti-Trafficking Legislation ──────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9208 — Anti-Trafficking in Persons Act of 2003",
        "summary": (
            "Comprehensive anti-trafficking statute criminalizing all forms "
            "of trafficking: labor trafficking, sex trafficking, organ "
            "trafficking, and child trafficking. Defines trafficking "
            "consistent with the Palermo Protocol. Created the Inter-Agency "
            "Council Against Trafficking (IACAT). Penalties: 20 years to "
            "life imprisonment and PHP 1-2 million fine for simple "
            "trafficking; life imprisonment and PHP 2-5 million fine for "
            "qualified trafficking."
        ),
        "source": "Republic Act No. 9208 (2003)",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10364 — Expanded Anti-Trafficking in Persons Act of 2012",
        "summary": (
            "Amended RA 9208 to expand the definition of trafficking, "
            "add the offense of attempted trafficking, increase penalties, "
            "strengthen victim protection, and create the IACAT secretariat. "
            "Key additions: criminalization of buying or engaging services "
            "of trafficked persons, expanded acts constituting trafficking "
            "(including OSEC), mandatory reporting by internet service "
            "providers, and establishment of the anti-trafficking trust fund."
        ),
        "source": "Republic Act No. 10364 (2012)",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 — Migrant Workers and Overseas Filipinos Act of 1995",
        "summary": (
            "Foundation law for OFW protection. Establishes the state "
            "policy of deploying Filipino workers only to countries where "
            "their rights are protected. Creates the legal framework for "
            "licensing of recruitment agencies, regulation of overseas "
            "employment, and establishment of welfare programs for OFWs. "
            "Defines illegal recruitment and provides penalties including "
            "life imprisonment when committed as economic sabotage "
            "(large-scale or by a syndicate)."
        ),
        "source": "Republic Act No. 8042 (1995)",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10022 — Amended Migrant Workers Act (2009)",
        "summary": (
            "Amended RA 8042 to strengthen OFW protections: mandatory "
            "insurance for OFWs, enhanced pre-departure orientation, "
            "establishment of National Reintegration Center for OFWs "
            "(NRCO), compulsory repatriation bonds, anti-illegal "
            "recruitment provisions expanded, and increased penalties for "
            "violating agencies. Also established the Legal Assistance "
            "Fund for OFWs and mandated the DMW to ensure only verified "
            "employers receive Filipino workers."
        ),
        "source": "Republic Act No. 10022 (2009)",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11641 — Department of Migrant Workers Act (2021)",
        "summary": (
            "Created the Department of Migrant Workers (DMW) as a "
            "cabinet-level department consolidating all OFW-related "
            "government functions. Absorbed POEA (Philippine Overseas "
            "Employment Administration), OWWA (Overseas Workers Welfare "
            "Administration), and OFW-related functions of DFA, DOLE, "
            "and other agencies. DMW is now the primary government body "
            "for migrant worker protection, deployment regulation, and "
            "welfare services. Became fully operational in 2022."
        ),
        "source": "Republic Act No. 11641 (2021)",
    },

    # ── Philippine Anti-Trafficking Institutional Framework ──────────────
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "Inter-Agency Council Against Trafficking (IACAT)",
        "organization": "IACAT / Department of Justice",
        "contact_type": "coordination",
        "summary": (
            "IACAT is the coordinating body for the Philippine government's "
            "anti-trafficking efforts. Chaired by DOJ Secretary with "
            "DSWD Secretary as co-chair. Members: DFA, DOLE/DMW, DILG, "
            "PNP, NBI, CHED, TESDA, CFO, CWC, and NEDA. Functions: "
            "policy formulation, program coordination, monitoring of "
            "anti-trafficking efforts, and review of implementing rules. "
            "IACAT Secretariat manages the Anti-Trafficking Database and "
            "coordinates law enforcement operations."
        ),
        "source": "RA 9208 Sec. 20; IACAT",
    },
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "Department of Migrant Workers (DMW) — OFW Hotline",
        "organization": "Department of Migrant Workers",
        "contact_type": "assistance",
        "summary": (
            "DMW operates the 1348 OFW Hotline for distressed migrant "
            "workers. Available 24/7. Services: case referral to POLO "
            "offices abroad, legal assistance coordination, repatriation "
            "coordination, and emergency assistance. DMW maintains 34 "
            "Philippine Overseas Labor Offices (POLOs) in 28 countries "
            "and Migrant Workers Offices (MWOs) to provide on-site "
            "assistance to distressed OFWs."
        ),
        "source": "DMW / RA 11641",
    },
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "OWWA — Overseas Workers Welfare Administration",
        "organization": "OWWA (under DMW)",
        "contact_type": "welfare",
        "summary": (
            "OWWA administers welfare programs for OFWs and their families. "
            "Programs: OFW Emergency Loan (up to PHP 50,000), OWWA "
            "Scholarship for OFW dependents, Reintegration Program "
            "(livelihood grants up to PHP 100,000), Balik-Pinas Balik-Hanapbuhay "
            "program, on-site services (counseling, shelter), and death "
            "and disability benefits. OWWA membership fee: USD 25 per "
            "contract. Over 2.3 million active members as of 2023."
        ),
        "source": "OWWA / DMW / RA 10801",
    },

    # ── Additional Corridor-Specific Cases ───────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-JO",
        "title": "Filipino Garment Workers in Jordan QIZ Factories",
        "exploitation_type": "excessive_overtime",
        "sector": "garment",
        "summary": (
            "Filipino workers in Jordan Qualifying Industrial Zone (QIZ) "
            "garment factories report mandatory overtime of 60-80 hours "
            "per week during peak seasons, failure to pay overtime premiums, "
            "confiscation of passports, and cramped dormitory housing. "
            "Better Work Jordan program has improved conditions in some "
            "factories but violations persist in smaller subcontracting "
            "operations. POLO Amman handles 150+ cases annually."
        ),
        "source": "POLO Amman / Better Work Jordan / DMW",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-LB",
        "title": "Filipino Domestic Workers in Lebanon — Kafala and Economic Crisis",
        "exploitation_type": "withholding_wages",
        "sector": "domestic_work",
        "summary": (
            "Lebanon's economic crisis (2019-present) severely impacted "
            "Filipino domestic workers. Employers unable to pay salaries "
            "due to currency devaluation (LBP lost 90% of value). Workers "
            "stranded without pay for months. Philippine Embassy Beirut "
            "facilitated repatriation of over 800 distressed OFWs in "
            "2020-2021. Philippines maintains deployment ban to Lebanon "
            "for domestic workers since 2014, but illegal deployment "
            "continues through third-country routing."
        ),
        "source": "Philippine Embassy Beirut / DFA / Migrante-Lebanon",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-BH",
        "title": "Filipino Workers in Bahrain — Positive Reform Example",
        "exploitation_type": "none",
        "sector": "multiple",
        "summary": (
            "Bahrain's labor reforms have been relatively positive for "
            "Filipino workers. Abolition of kafala system for most workers "
            "(2009), Labour Market Regulatory Authority (LMRA) permits "
            "worker mobility, and Wage Protection System ensures electronic "
            "salary payments. POLO Manama reports lower distress case rates "
            "compared to other Gulf posts. However, domestic workers "
            "remain under a separate regulatory framework with fewer "
            "protections."
        ),
        "source": "POLO Manama / LMRA Bahrain / ILO",
    },

    # ── Additional Enforcement and Penalty Facts ─────────────────────────
    {
        "type": "penalty",
        "jurisdiction": "PH",
        "title": "Qualified Trafficking Penalties — RA 9208/10364",
        "offense": "Qualified trafficking in persons (involving minors, syndicates, public officials)",
        "penalty_type": "criminal",
        "amount": "Life imprisonment + PHP 2,000,000 to PHP 5,000,000 fine",
        "summary": (
            "Qualified trafficking carries the maximum penalty of life "
            "imprisonment and fine of PHP 2-5 million. Qualifying "
            "circumstances: (a) victim is a child, (b) committed by a "
            "syndicate of three or more, (c) offender is an ascendant, "
            "parent, sibling, guardian, or person exercising authority, "
            "(d) committed by a public officer or employee, (e) victim "
            "dies, becomes insane, suffers mutilation, or is afflicted "
            "with HIV/AIDS."
        ),
        "source": "RA 9208 Sec. 6; RA 10364",
    },
    {
        "type": "penalty",
        "jurisdiction": "PH",
        "title": "Large-Scale Illegal Recruitment — Economic Sabotage",
        "offense": "Illegal recruitment involving 3 or more victims",
        "penalty_type": "criminal",
        "amount": "Life imprisonment + PHP 2,000,000 to PHP 5,000,000 fine",
        "summary": (
            "Large-scale illegal recruitment (3 or more victims) is "
            "classified as economic sabotage under RA 8042/10022. Penalty: "
            "life imprisonment and fine of PHP 2-5 million. Agency license "
            "permanently revoked. All assets used in the offense subject "
            "to forfeiture. Recruitment agency's surety bond forfeited in "
            "favor of victims. Criminal and civil liability of agency "
            "officers and directors is personal."
        ),
        "source": "RA 8042 Sec. 6; RA 10022",
    },
    {
        "type": "penalty",
        "jurisdiction": "PH",
        "title": "OSEC Penalties — RA 9775 / RA 10175 / RA 9208",
        "offense": "Online sexual exploitation of children",
        "penalty_type": "criminal",
        "amount": "Life imprisonment + PHP 2,000,000 to PHP 5,000,000 fine (trafficking); reclusion temporal + PHP 500,000 to PHP 1,000,000 (cybercrime)",
        "summary": (
            "OSEC offenders face charges under multiple laws: RA 9208/10364 "
            "(trafficking — life imprisonment), RA 9775 (Anti-Child "
            "Pornography — reclusion temporal and fine), RA 10175 "
            "(Cybercrime — one degree higher penalty), and RA 7610 "
            "(Special Protection of Children). Courts typically impose "
            "the highest penalty for the most serious offense. Foreign "
            "buyers can be prosecuted under cybercrime law."
        ),
        "source": "RA 9208; RA 9775; RA 10175; DOJ-IACAT prosecution guidelines",
    },

    # ── DMW Administrative Enforcement ───────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW Agency License Cancellations — 2022-2023 Enforcement",
        "summary": (
            "DMW cancelled or suspended the licenses of 89 recruitment "
            "agencies in 2022 and 112 in 2023 for violations including: "
            "excessive fee collection, deployment to non-verified employers, "
            "contract substitution, failure to assist distressed workers, "
            "and operating without license renewal. DMW also issued closure "
            "orders against 34 illegal recruitment operations. Total monetary "
            "fines imposed: PHP 45 million (2023). Enhanced enforcement "
            "attributed to DMW's centralized regulatory authority under "
            "RA 11641."
        ),
        "source": "DMW / IACAT Annual Report 2023",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POEA/DMW Blacklisted Employers Registry",
        "summary": (
            "DMW maintains a registry of blacklisted foreign employers "
            "prohibited from hiring Filipino workers. As of 2023, over "
            "2,800 foreign employers are blacklisted. Grounds: non-payment "
            "of wages, physical/sexual abuse, contract violations, "
            "unauthorized salary deductions, and refusal to repatriate. "
            "Blacklisted employers are shared with host country labor "
            "authorities through POLO offices. Recruitment agencies that "
            "deploy to blacklisted employers face license cancellation."
        ),
        "source": "DMW / former POEA database",
    },

    # ── Seafarer-Specific Jurisprudence ──────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Magsaysay Maritime v. NLRC — Seafarer Rights Landmark",
        "court": "Supreme Court of the Philippines",
        "year": 2014,
        "summary": (
            "Supreme Court ruled that Filipino seafarers covered by "
            "POEA-SEC (Standard Employment Contract) are entitled to "
            "disability benefits when illness is work-related, regardless "
            "of pre-existing conditions. Manning agency and foreign "
            "shipowner jointly and solidarily liable. Court applied the "
            "liberal interpretation principle in favor of seafarers. "
            "This case strengthened the protection framework for the "
            "estimated 400,000+ Filipino seafarers deployed annually."
        ),
        "source": "Supreme Court of the Philippines; AMOSUP / POEA-SEC",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Filipino Seafarers on Foreign-Flag Vessels — Wage Theft Pattern",
        "exploitation_type": "withholding_wages",
        "sector": "maritime",
        "summary": (
            "Pattern documented by AMOSUP and POEA/DMW: Filipino seafarers "
            "on foreign-flag vessels experience wage withholding when "
            "shipowner faces financial difficulty. Vessel abandonment "
            "cases (crew stranded without pay) average 15-20 per year "
            "involving Filipino seafarers. ITF (International Transport "
            "Workers' Federation) assists with wage recovery through "
            "port state control. Philippines accounts for 25% of the "
            "global seafarer supply (1.96 million registered)."
        ),
        "source": "AMOSUP / ITF / DMW / MARINA",
    },

    # ── US TIP Report Philippine Rankings ────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "US State Department TIP Report — Philippines Rankings",
        "summary": (
            "The Philippines has been consistently placed on Tier 1 "
            "(fully meeting minimum standards) of the US State Department "
            "Trafficking in Persons Report since 2016, except for 2024 "
            "when it was downgraded to the Tier 2 Watch List. Tier 1 "
            "placement reflects strong legal framework, increased "
            "prosecutions, victim services, and inter-agency coordination "
            "through IACAT. The 2024 downgrade cited insufficient "
            "convictions relative to the scale of the problem and "
            "concerns about complicity of government officials."
        ),
        "source": "US State Department TIP Reports 2016-2024",
    },

    # ── IACAT Task Force Against Trafficking (NAIA) ──────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "NAIA Task Force Against Trafficking — Airport Interceptions",
        "exploitation_type": "multiple",
        "sector": "multiple",
        "summary": (
            "The IACAT-NAIA Task Force screens departing passengers at "
            "Ninoy Aquino International Airport for trafficking indicators. "
            "In 2023, the task force intercepted 3,247 potential trafficking "
            "victims (offloaded passengers exhibiting trafficking red flags): "
            "incomplete documentation, inconsistent travel histories, "
            "presence of suspected recruiters, and minors traveling with "
            "non-relatives. Intercepted passengers are referred to NBI "
            "or PNP-WCPC for investigation and DSWD for services."
        ),
        "source": "IACAT / DOJ / NAIA Operations Report 2023",
    },

    # ── Cybercrime-Enabled Trafficking ───────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "POGO Hubs and Trafficking — Chinese and Filipino Victims",
        "exploitation_type": "restriction_of_movement",
        "sector": "online_gaming",
        "summary": (
            "Philippine Offshore Gaming Operators (POGOs) linked to "
            "trafficking of Chinese, Vietnamese, and Filipino workers. "
            "Workers lured with high-salary job offers, then confined to "
            "POGO compounds, forced to conduct online scams (pig butchering, "
            "romance scams). Passports confiscated, physical abuse for "
            "non-compliance. PAGCOR and PNP raided 40+ POGO operations "
            "in 2023-2024, rescuing over 4,000 workers. President Marcos "
            "ordered total POGO ban effective December 2024."
        ),
        "source": "PAGCOR / PNP-CIDG / IACAT / Senate Committee on Public Order",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POGO Ban — Executive Order and Legislative Action (2024)",
        "summary": (
            "President Marcos Jr. ordered a total ban on Philippine "
            "Offshore Gaming Operators (POGOs) in July 2024 following "
            "Senate investigations revealing widespread trafficking, "
            "kidnapping, and scam operations linked to POGO hubs. "
            "PAGCOR directed all POGOs to cease operations by December "
            "31, 2024. Over 300 POGO operations affected. The ban aimed "
            "to eliminate a key vector for cross-border trafficking into "
            "the Philippines. Immigration enforcement increased at ports "
            "of entry to prevent POGO-related arrivals."
        ),
        "source": "Office of the President / PAGCOR / Senate Resolution No. 173",
    },

    # ── Recruitment Regulation ───────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW Zero Placement Fee Policy — Implementation Status",
        "summary": (
            "The Philippines enforces a zero placement fee policy for "
            "domestic workers and a one-month salary cap for skilled "
            "workers under RA 10022. In practice, compliance is inconsistent: "
            "DMW estimates that 60-70% of domestic workers still pay fees "
            "exceeding authorized amounts through informal channels, "
            "intermediaries, and pre-departure loan schemes. Enhanced "
            "enforcement includes: mandatory pre-departure briefing on "
            "fee limits, anonymous fee reporting hotline, and partnerships "
            "with destination-country labor ministries."
        ),
        "source": "DMW / ILO Fair Recruitment Initiative / Verité",
    },

    # ── Bilateral Labor Agreements ───────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "corridor": "PH-SA",
        "title": "Philippines-Saudi Arabia Bilateral Labor Agreement",
        "summary": (
            "The Philippines and Saudi Arabia have signed multiple bilateral "
            "labor agreements (most recent: 2013, supplementary protocol "
            "2017). Key provisions: standardized employment contracts, "
            "verification of employers by POLO Riyadh/Jeddah, mandatory "
            "bank account salary payment, and joint committee for dispute "
            "resolution. Implementation challenges: Saudi courts apply "
            "local law which may override bilateral protections, and "
            "domestic workers are covered by a separate regulatory "
            "framework with weaker protections."
        ),
        "source": "DFA / DMW / Saudi Ministry of Human Resources",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "corridor": "PH-AE",
        "title": "Philippines-UAE Bilateral Labor Agreement (2017)",
        "summary": (
            "The 2017 Philippines-UAE agreement on employment of domestic "
            "workers establishes: minimum wage, rest periods, maximum "
            "working hours, right to retain personal documents, and "
            "dispute resolution mechanisms. The agreement also requires "
            "both countries to exchange information on licensed recruitment "
            "agencies and verified employers. Implementation monitored "
            "by a Joint Technical Committee that meets annually."
        ),
        "source": "DFA / DMW / UAE Ministry of Human Resources",
    },

    # ── Specific High-Profile OFW Cases ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-SA",
        "title": "Flor Contemplacion Case (1995) — OFW Watershed Moment",
        "exploitation_type": "multiple",
        "sector": "domestic_work",
        "summary": (
            "Filipina domestic worker Flor Contemplacion was executed by "
            "hanging in Singapore on March 17, 1995, for the murder of "
            "a fellow domestic worker and her ward. The case sparked massive "
            "public outrage in the Philippines. Allegations that Contemplacion "
            "herself was a trafficking victim who acted under duress were "
            "never fully resolved. The case directly led to the enactment "
            "of RA 8042 (Migrant Workers Act of 1995) and fundamental "
            "reforms in Philippine overseas employment policy."
        ),
        "source": "DFA / Philippine Congress records / RA 8042 legislative history",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-KW",
        "title": "Jennifer Dalquez Case (2022) — OFW Self-Defense in Kuwait",
        "exploitation_type": "physical_sexual_violence",
        "sector": "domestic_work",
        "summary": (
            "Filipina domestic worker Jennifer Dalquez sentenced to death "
            "by Kuwait court for killing her employer, whom she claimed "
            "had been sexually assaulting her. Philippine government "
            "provided legal assistance through ATN Fund. DFA mounted "
            "diplomatic campaign. Dalquez was pardoned and repatriated "
            "in 2022 after diplomatic negotiations. Case highlighted "
            "the intersection of trafficking, domestic violence, and "
            "self-defense rights of OFWs."
        ),
        "source": "DFA / DMW / Inquirer.net / ABS-CBN",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-SY",
        "title": "OFWs Stranded in Syria — Conflict Zone Repatriation (2011-2012)",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "multiple",
        "summary": (
            "Approximately 2,500 Filipino workers were stranded in Syria "
            "when the civil war began in 2011. Many domestic workers were "
            "abandoned by employers who fled. Workers trapped in conflict "
            "zones without food, shelter, or documents. DFA conducted "
            "emergency repatriation through Lebanon and Jordan borders. "
            "OWWA and ATN Fund covered repatriation costs. Case prompted "
            "creation of the Crisis Alert System for OFW deployment "
            "countries classified by threat level."
        ),
        "source": "DFA / DMW / OWWA / CNN Philippines",
    },

    # ── Additional Court Rulings and Legal Principles ────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, G.R. No. 225642 (2019) — Trafficking via Social Media",
        "court": "Supreme Court of the Philippines",
        "year": 2019,
        "summary": (
            "Supreme Court upheld conviction for trafficking committed "
            "through social media recruitment. Accused used Facebook to "
            "recruit minors for sexual exploitation. Court ruled that "
            "online recruitment falls squarely within the acts of "
            "trafficking under RA 9208 and is further aggravated by the "
            "use of information and communications technology under "
            "RA 10175 (Cybercrime Prevention Act). The cyber element "
            "increases the penalty by one degree."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 225642",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, G.R. No. 231983 (2020) — Entrapment Operations Valid",
        "court": "Supreme Court of the Philippines",
        "year": 2020,
        "summary": (
            "Supreme Court upheld the validity of NBI entrapment operations "
            "in trafficking cases. Accused challenged conviction arguing "
            "that the entrapment operation amounted to instigation. Court "
            "ruled that when law enforcement agents merely provide an "
            "opportunity for the commission of a crime that the accused "
            "was predisposed to commit, it is a valid entrapment, not "
            "instigation. NBI-AHTRAD and IJM joint operations specifically "
            "endorsed as proper anti-trafficking methodology."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 231983",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX, G.R. No. 227363 (2019) — Private Complainant Not Required",
        "court": "Supreme Court of the Philippines",
        "year": 2019,
        "summary": (
            "Supreme Court ruled that trafficking cases may proceed even "
            "without a private complainant (victim's sworn statement). "
            "The State, as represented by the People of the Philippines, "
            "may prosecute trafficking as a public offense. Law enforcement "
            "testimony, documentary evidence, and expert testimony may "
            "substitute for victim testimony when the victim is unavailable, "
            "minor, or traumatized. This prevents traffickers from "
            "escaping prosecution through victim intimidation."
        ),
        "source": "Supreme Court of the Philippines, G.R. No. 227363",
    },

    # ── IACAT Special Operations ─────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "IACAT Conviction Statistics — Breakdown by Offense Type",
        "metric": "Trafficking convictions by type (2005-2023)",
        "value": "281 total: 142 sex trafficking, 68 labor trafficking, 52 OSEC, 19 other",
        "year": 2023,
        "summary": (
            "Of 281 trafficking convictions secured by IACAT from 2005-2023: "
            "sex trafficking cases account for 51%, labor trafficking 24%, "
            "OSEC 18%, and other forms 7%. OSEC convictions are the "
            "fastest-growing category, increasing from 2 convictions in "
            "2015 to 15 in 2023. Average case duration from filing to "
            "conviction: 3.5 years. Conviction rate improved from 10% "
            "(2005-2010) to 35% (2019-2023)."
        ),
        "source": "IACAT / DOJ / US State Dept TIP Report 2023",
    },

    # ── Repatriation Statistics ──────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Emergency Repatriation of OFWs — Annual Data",
        "metric": "OFWs repatriated through government assistance annually",
        "value": "12,000-15,000 annually (non-pandemic years); 327,511 (2020 COVID)",
        "year": 2023,
        "summary": (
            "DMW/DFA repatriate 12,000-15,000 distressed OFWs annually "
            "under normal conditions. During COVID-19, the Philippines "
            "repatriated 327,511 OFWs in 2020 under the National "
            "Repatriation Program. Repatriation covered by: employer "
            "(contractual obligation), recruitment agency (solidary "
            "liability), OWWA trust fund, and ATN Fund. Top repatriation "
            "origins: Saudi Arabia, UAE, Kuwait, Qatar, and Lebanon."
        ),
        "source": "DMW / DFA / OWWA Annual Reports",
    },

    # ── International Cooperation ────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "Philippines Participation in ASEAN ACTIP Convention",
        "summary": (
            "The Philippines ratified the ASEAN Convention Against "
            "Trafficking in Persons, Especially Women and Children (ACTIP) "
            "in 2017. ACTIP provides for: regional cooperation in "
            "investigation and prosecution, mutual legal assistance, "
            "victim identification and protection, and information sharing. "
            "The Philippines participates in the ASEAN Plan of Action "
            "Against TIP and the Bali Process on People Smuggling, "
            "Trafficking, and Related Transnational Crime."
        ),
        "source": "DFA / ASEAN / DOJ",
    },
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "IJM Partnership with Philippine Government — OSEC Impact",
        "summary": (
            "International Justice Mission (IJM) has partnered with the "
            "Philippine government since 2001, focusing on OSEC since 2016. "
            "IJM provides: casework support (investigations, rescues, "
            "prosecutions), capacity building for law enforcement and "
            "prosecutors, aftercare program funding, and systemic reform "
            "advocacy. IJM-supported operations have resulted in 160+ "
            "OSEC-related arrests and rescue of 700+ children. Philippine "
            "deterrence study showed 60% reduction in OSEC prevalence in "
            "target areas (Cebu) between 2016 and 2022."
        ),
        "source": "IJM Philippines / IACAT / US State Dept TIP Report",
    },

    # ── Filipino Diaspora and Trafficking Vulnerabilities ────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OFW Deployment Statistics — Annual Data",
        "metric": "Annual deployment of new-hire OFWs",
        "value": "1.96 million deployed (2022); 2.16 million (2023)",
        "year": 2023,
        "summary": (
            "The Philippines deploys approximately 2 million OFWs annually "
            "across land-based and sea-based categories. Breakdown (2023): "
            "1.43 million land-based workers (domestic workers, healthcare, "
            "construction, services) and 0.73 million sea-based workers "
            "(seafarers). Top destinations: Saudi Arabia (23%), UAE (12%), "
            "Hong Kong (8%), Kuwait (6%), Singapore (5%), Qatar (5%). "
            "Remittances: USD 37.2 billion (2023), approximately 9% of GDP."
        ),
        "source": "DMW / PSA / BSP (Bangko Sentral ng Pilipinas)",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OFW Remittances — Economic Impact",
        "metric": "Annual OFW remittances to the Philippines",
        "value": "USD 37.2 billion (2023)",
        "year": 2023,
        "summary": (
            "OFW remittances represent approximately 9% of Philippine GDP "
            "and are the single largest source of foreign exchange. "
            "Growth: USD 28.9 billion (2019), USD 29.9 billion (2020), "
            "USD 31.4 billion (2021), USD 36.1 billion (2022), USD 37.2 "
            "billion (2023). The economic dependence on remittances creates "
            "a structural incentive for deployment that can override "
            "worker protection concerns, contributing to the persistence "
            "of trafficking and exploitation despite strong legal frameworks."
        ),
        "source": "BSP / PSA / World Bank",
    },

    # ── Training and Capacity Building ───────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "PDOS and PEOS — Pre-Departure Programs for OFWs",
        "summary": (
            "All departing OFWs are required to attend Pre-Departure "
            "Orientation Seminar (PDOS) covering: employment contract "
            "provisions, labor laws of destination country, cultural "
            "orientation, health and safety, financial literacy, and "
            "mechanisms for filing complaints. Pre-Employment Orientation "
            "Seminar (PEOS) targets prospective OFWs before they engage "
            "recruitment agencies. DMW conducts PDOS through accredited "
            "training centers. Country-specific modules developed for "
            "top destination countries."
        ),
        "source": "DMW / OWWA / IOM",
    },

    # ── Specific Investigation Outcomes ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "NBI Operation Against Online Trafficking Syndicate — Pampanga (2023)",
        "exploitation_type": "sexual_exploitation",
        "sector": "cybercrime",
        "summary": (
            "NBI-AHTRAD dismantled an online trafficking syndicate operating "
            "from a compound in Pampanga. The syndicate recruited victims "
            "through social media, luring them with job offers. Victims "
            "were forced to perform sexual acts on live-stream for foreign "
            "customers. Operation rescued 47 victims including 19 minors. "
            "10 suspects arrested. Coordination with Australian Federal "
            "Police led to arrest of 3 foreign buyers. PHP 15 million in "
            "assets seized."
        ),
        "source": "NBI-AHTRAD / AFP / IJM / IACAT",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "IACAT-PNP Operation Against Labor Trafficking — Cavite (2022)",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "IACAT and PNP-WCPC raided a garment manufacturing facility in "
            "Cavite where 35 workers from Mindanao were subjected to forced "
            "labor. Workers recruited with promise of PHP 15,000 monthly "
            "salary but received PHP 3,000-5,000 after deductions for "
            "housing, food, and 'training fees.' Movement restricted, "
            "documents confiscated. Factory owner and 3 supervisors charged "
            "with trafficking. Workers provided with DSWD services and "
            "assisted in returning to home provinces."
        ),
        "source": "PNP-WCPC / IACAT / DSWD / DOLE",
    },

    # ── Legal Aid and Access to Justice ──────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10364 Sec. 16 — Legal Assistance for Trafficking Victims",
        "summary": (
            "Section 16 of RA 10364 mandates that the DOJ shall provide "
            "free legal assistance to trafficking victims through the "
            "Public Attorney's Office (PAO) or through IACAT-accredited "
            "NGOs. Legal assistance includes: representation in criminal "
            "proceedings, filing of civil claims for damages, and assistance "
            "in claiming restitution. IACAT also provides Pro Bono legal "
            "assistance through partnerships with law schools and the "
            "Integrated Bar of the Philippines."
        ),
        "source": "RA 10364 Sec. 16; IACAT; PAO",
    },
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "OFW Legal Assistance — NLRC Migrant Workers Branch",
        "summary": (
            "The NLRC (National Labor Relations Commission) has designated "
            "specific labor arbiters and branches to handle OFW cases for "
            "expedited resolution. OFWs may file complaints against "
            "recruitment agencies and foreign employers at the NLRC. "
            "DMW Legal Assistance Division provides free legal representation. "
            "The Single Entry Approach (SEnA) allows for 30-day mandatory "
            "conciliation-mediation before formal case filing. In 2023, "
            "NLRC resolved 4,200+ OFW cases with a settlement rate of 65%."
        ),
        "source": "NLRC / DMW / DOLE",
    },

    # ── Emerging Issues ──────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "Trafficking Risks in Online Freelancing and Gig Economy",
        "summary": (
            "IACAT has identified emerging trafficking risks in the "
            "Philippines' growing online freelancing and BPO sectors. "
            "Patterns include: fraudulent job postings for 'virtual "
            "assistants' that lead to OSEC facilitation, cryptocurrency "
            "scam operations targeting Filipino workers, and unregulated "
            "online platforms recruiting for overseas domestic work. DMW "
            "is developing regulatory frameworks for digitally recruited "
            "workers. ILO Technical Cooperation with PH includes digital "
            "labor platform governance."
        ),
        "source": "IACAT / DMW / ILO Manila",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Cryptocurrency Scam Hub Trafficking — Clark/Angeles City (2023-2024)",
        "exploitation_type": "restriction_of_movement",
        "sector": "cybercrime",
        "summary": (
            "Multiple raids on cryptocurrency and investment scam operations "
            "in Clark Freeport Zone and Angeles City rescued Filipino and "
            "foreign workers trafficked into scam call centers. Workers "
            "recruited through social media job ads promising PHP 50,000+ "
            "monthly salary for 'customer service.' Victims confined to "
            "compounds, passports taken, forced to run romance and crypto "
            "scams. CIDG and immigration conducted joint operations "
            "arresting Chinese and Filipino operators."
        ),
        "source": "PNP-CIDG / BI (Bureau of Immigration) / IACAT",
    },

    # ── Anti-Trafficking Infrastructure ──────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Philippine Anti-Trafficking Infrastructure — Resource Summary",
        "metric": "Government anti-trafficking resource allocation",
        "value": "PHP 1.8 billion total budget (2023) across IACAT member agencies",
        "year": 2023,
        "summary": (
            "Philippine government anti-trafficking resources (2023): "
            "DOJ/IACAT Secretariat (PHP 120M), PNP-WCPC (PHP 350M), "
            "NBI-AHTRAD (PHP 180M), DSWD RRPTP (PHP 450M), DMW enforcement "
            "(PHP 280M), DFA ATN Fund (PHP 1.4B shared with other consular "
            "assistance). Total dedicated anti-trafficking personnel: "
            "approximately 2,500 across all agencies. 17 Regional "
            "Anti-Trafficking Task Forces operational."
        ),
        "source": "DBM / IACAT / US State Dept TIP Report 2023",
    },

    # ── Worker Death Abroad Statistics ───────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OFW Deaths Abroad — Annual Data",
        "metric": "Reported deaths of OFWs abroad annually",
        "value": "Approximately 800-1,200 reported annually",
        "year": 2023,
        "summary": (
            "DFA and DMW report 800-1,200 OFW deaths abroad annually. "
            "Causes: natural causes/illness (40%), workplace accidents "
            "(25%), homicide/violence (10%), suicide (8%), vehicular "
            "accidents (7%), unexplained (10%). Highest fatality rates: "
            "Saudi Arabia, UAE, Kuwait, and Qatar. Many deaths attributed "
            "to 'cardiac arrest' may be related to heat stress, overwork, "
            "or abuse. Incomplete reporting means actual figures are "
            "likely higher. OWWA provides PHP 200,000 death benefit "
            "to beneficiaries."
        ),
        "source": "DFA / DMW / OWWA / Migrante International",
    },

    # ── Indigenous Peoples and Internal Trafficking ──────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Internal Trafficking of Lumad and IP Communities in Mindanao",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Indigenous peoples (Lumad, Mangyan, Aeta) in the Philippines "
            "are disproportionately vulnerable to internal trafficking. "
            "Patterns include: recruitment for plantation labor through "
            "debt advances, domestic servitude of indigenous girls in urban "
            "households, and recruitment of IP youth for begging syndicates "
            "in Metro Manila. NCIP and DSWD report that IP communities "
            "account for 15-20% of internal trafficking victims. Lack of "
            "birth certificates and documentation compounds vulnerability."
        ),
        "source": "NCIP / DSWD / ILO Philippines / IACAT",
    },

    # ── Maritime Manning Agency Regulation ───────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "MARINA Manning Agency Accreditation and Monitoring",
        "summary": (
            "The Maritime Industry Authority (MARINA) regulates approximately "
            "400 licensed manning agencies deploying 400,000+ Filipino seafarers "
            "annually. MARINA requires: financial capability (minimum PHP 5M "
            "paid-up capital), bonding (escrow deposits), POEA-SEC compliance, "
            "and annual compliance audits. Agencies that fail to assist "
            "distressed seafarers face suspension or cancellation. In 2023, "
            "MARINA suspended 23 manning agencies for violations. "
            "Philippines is the world's largest supplier of seafarers."
        ),
        "source": "MARINA / DMW / ITF",
    },

    # ── Child Trafficking Rescue and Aftercare ───────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Child Trafficking Victims — DSWD Aftercare Statistics",
        "metric": "Children served through DSWD trafficking aftercare programs",
        "value": "1,340 child victims served (2023)",
        "year": 2023,
        "summary": (
            "DSWD provided residential care and aftercare services to "
            "1,340 child trafficking victims in 2023. Services include: "
            "temporary shelter (average 3-6 months), trauma-focused "
            "cognitive behavioral therapy, educational reintegration, "
            "family tracing, and community-based aftercare monitoring. "
            "DSWD operates 7 specialized shelters for child trafficking "
            "victims. Average age of child victims: 13-15 years. "
            "OSEC victims are now the majority of child referrals."
        ),
        "source": "DSWD / IACAT / UNICEF Philippines",
    },

    # ── Anti-Money Laundering in Trafficking Cases ───────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "AMLA Application to Trafficking Proceeds — RA 9160",
        "summary": (
            "Trafficking in persons is a predicate offense under the "
            "Anti-Money Laundering Act (RA 9160 as amended by RA 10365). "
            "The Anti-Money Laundering Council (AMLC) can freeze and "
            "forfeit assets derived from trafficking. AMLC has issued "
            "freeze orders in 45+ trafficking cases since 2015, recovering "
            "over PHP 200 million. Financial intelligence from AMLC "
            "suspicious transaction reports assists NBI and PNP in "
            "identifying trafficking networks, especially OSEC operations "
            "that receive payments through remittance services."
        ),
        "source": "AMLC / RA 9160 / RA 10365 / IACAT",
    },

    # ── DOLE Enforcement Against Internal Forced Labor ───────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "DOLE Labor Inspections — Forced Labor Indicators Found",
        "metric": "Establishments found with forced labor indicators during DOLE inspections",
        "value": "327 establishments flagged (2022-2023)",
        "year": 2023,
        "summary": (
            "DOLE labor inspectors flagged 327 establishments for forced "
            "labor indicators during routine and complaint-based inspections "
            "in 2022-2023. Sectors: manufacturing (35%), agriculture (25%), "
            "fishing (15%), construction (10%), services (15%). Common "
            "indicators: document retention, wage deductions exceeding "
            "legal limits, child labor, restriction of movement, and "
            "excessive working hours. Establishments referred to IACAT "
            "for trafficking investigation. DOLE compliance orders issued "
            "for non-trafficking labor violations."
        ),
        "source": "DOLE / IACAT / ILO",
    },

    # ── Deployment Bans and Suspensions ──────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Philippine Deployment Bans — History and Current Status",
        "summary": (
            "The Philippines has deployed strategic deployment bans to "
            "protect OFWs. Notable bans: Kuwait total ban (February-May "
            "2018, Demafelis case), Saudi Arabia partial ban for domestic "
            "workers (2011-2012, Rizana Nafeek execution), Lebanon domestic "
            "worker ban (2014-present, kafala abuse), Libya total ban (2011-present, "
            "conflict), Syria total ban (2011-present, civil war), and Iraq "
            "total ban (2014-2017, ISIS). DMW applies Alert Level System: "
            "Level 1 (precaution), Level 2 (restriction), Level 3 "
            "(repatriation), Level 4 (total ban). As of 2024, total bans "
            "remain for Libya, Syria, and several conflict zones."
        ),
        "source": "DMW / DFA / OWWA",
    },

    # ── Prosecution of Foreign Buyers in OSEC Cases ──────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "OSEC Foreign Buyer Prosecutions — Cross-Border Cooperation",
        "court": "Various Courts (Philippines + foreign jurisdictions)",
        "year": 2023,
        "summary": (
            "Philippine anti-trafficking authorities coordinate with foreign "
            "law enforcement to prosecute OSEC buyers in their home countries. "
            "Since 2016, IJM and IACAT referrals have led to prosecutions "
            "of foreign buyers in: Australia (47 cases), United States (31), "
            "United Kingdom (18), Germany (12), and other countries. "
            "Australian Federal Police (AFP) and US HSI maintain permanent "
            "liaisons with PNP-WCPC for OSEC investigations. Mutual Legal "
            "Assistance Treaties (MLATs) facilitate evidence sharing."
        ),
        "source": "IJM / IACAT / AFP / US HSI / PNP-WCPC",
    },

    # ── Civil Society Anti-Trafficking Organizations ─────────────────────
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "Key Philippine Anti-Trafficking NGOs and Civil Society",
        "organization": "Multiple NGOs",
        "contact_type": "civil_society",
        "summary": (
            "Leading Philippine anti-trafficking NGOs: Visayan Forum "
            "Foundation (pioneer in port-based trafficking prevention), "
            "International Justice Mission (OSEC investigations and "
            "aftercare), Migrante International (OFW advocacy network "
            "with chapters in 22 countries), Center for Migrant Advocacy "
            "(policy advocacy), Blas F. Ople Policy Center (migrant worker "
            "welfare), Coalition Against Trafficking in Women - Asia Pacific "
            "(CATW-AP), and Kanlungan Centre Foundation (direct services "
            "for distressed migrants). These organizations complement "
            "government efforts and provide critical victim services."
        ),
        "source": "IACAT / Philippine NGO registry / US State Dept TIP Report",
    },

    # ── Mary Jane Veloso Case ────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "corridor": "PH-ID",
        "title": "Mary Jane Veloso Case (2010-present) — OFW Drug Mule Trafficking",
        "exploitation_type": "deception",
        "sector": "domestic_work",
        "summary": (
            "Filipina domestic worker Mary Jane Veloso sentenced to death "
            "in Indonesia for drug smuggling in 2010. Veloso claimed she was "
            "an unwitting drug mule — recruited by a trafficking syndicate "
            "that hid heroin in her suitcase. Her recruiter Maria Cristina "
            "Sergio was convicted of illegal recruitment and human trafficking "
            "in the Philippines in 2016. Veloso's execution was stayed in "
            "2015 following intense Philippine diplomatic intervention. "
            "As of 2024, she remains on death row but her case continues to "
            "be a symbol of OFW vulnerability to trafficking-related crimes."
        ),
        "source": "DFA / DOJ / Supreme Court (Sergio case) / Amnesty International",
    },
]
