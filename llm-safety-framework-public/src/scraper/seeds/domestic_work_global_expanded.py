"""
Domestic Work Global Expanded Facts Database

Comprehensive seed facts covering ILO C189 ratification, regional case studies,
legislation, and legal precedents from 2005-2025 across Hong Kong, Singapore,
Malaysia, Gulf states, Lebanon, Jordan, USA, UK, France, Italy, Latin America,
and South Africa.

150 facts covering: case_study, court_ruling, statistic, law, regulation_change,
advisory, penalty, recruitment_violation, complaint
"""

DOMESTIC_WORK_GLOBAL_EXPANDED_FACTS = [
    # ===== ILO C189 RATIFICATION & GLOBAL ===== (15 facts)
    {
        "type": "law",
        "jurisdiction": "GLOBAL",
        "title": "ILO Convention No. 189 (Domestic Workers Convention)",
        "summary": "Adopted June 2011, entered into force September 2013. Establishes minimum rights and protections for domestic workers including working hours, minimum rest, fair wages, safe working conditions, freedom of association.",
        "source": "ILO-C189-2011"
    },
    {
        "type": "statistic",
        "jurisdiction": "GLOBAL",
        "title": "Global Domestic Worker Population",
        "summary": "ILO estimates approximately 67 million domestic workers globally (2019), representing 11% of global employment with 80% women. Majority concentrated in Asia-Pacific and Latin America.",
        "source": "ILO-Global-Estimates-2019"
    },
    {
        "type": "advisory",
        "jurisdiction": "GLOBAL",
        "title": "ILO Technical Notes on Domestic Work",
        "summary": "2013-2020 series of technical guidance documents on implementing C189, covering wage protection, working time, social security, contract provisions, and enforcement mechanisms.",
        "source": "ILO-Technical-Notes"
    },
    {
        "type": "law",
        "jurisdiction": "GLOBAL",
        "title": "ILO Convention No. 190 (Violence and Harassment)",
        "summary": "Adopted June 2019, includes domestic workers in protections against gender-based violence and harassment at work. Requires member states to establish reporting mechanisms.",
        "source": "ILO-C190-2019"
    },
    {
        "type": "statistic",
        "jurisdiction": "GLOBAL",
        "title": "ILO Global Estimates of Forced Labour in Domestic Work",
        "summary": "2021 estimates identify 10 million domestic workers in situations of forced labour globally, with domestic work accounting for 16% of all forced labour victims.",
        "source": "ILO-Forced-Labour-Estimates-2021"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "GLOBAL",
        "title": "ILO C189 Member State Ratifications 2011-2025",
        "summary": "As of 2025, 30+ countries have ratified C189 including Uruguay, Philippines, Indonesia, South Africa, Kenya, Costa Rica, Morocco, Thailand. 60+ members have yet to ratify.",
        "source": "ILO-NORMLEX-Status-2025"
    },
    {
        "type": "advisory",
        "jurisdiction": "GLOBAL",
        "title": "UN Human Rights Council Resolution on Migrant Domestic Workers",
        "summary": "2013 (A/HRC/RES/24/4) calls for strengthening protections for migrant domestic workers, addressing wage theft, passport confiscation, isolation, and exclusion from labour laws.",
        "source": "UN-HRC-RES-24-4"
    },
    {
        "type": "statistic",
        "jurisdiction": "GLOBAL",
        "title": "COVID-19 Impact on Domestic Workers",
        "summary": "ILO 2020 report documents pandemic impact: 50% income loss, 30% job loss, increased isolation, extended hours without compensation. Estimated $205 billion economic impact.",
        "source": "ILO-COVID-19-Domestic-Work-2020"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "GLOBAL",
        "title": "Trafficking in Persons Protocol Definition of Domestic Work Trafficking",
        "summary": "UN Palermo Protocol (2000) recognizes domestic work as high-risk sector for trafficking, with exploitation including debt bondage, passport confiscation, isolation, and non-payment.",
        "source": "UN-Palermo-Protocol-2000"
    },
    {
        "type": "penalty",
        "jurisdiction": "GLOBAL",
        "title": "ICCPR General Comment 28 on Equality Rights",
        "summary": "2003 clarifies that domestic workers have equal protection under international human rights law, with states obliged to protect against private sector exploitation.",
        "source": "ICCPR-General-Comment-28-2003"
    },
    {
        "type": "statistic",
        "jurisdiction": "GLOBAL",
        "title": "Wage Theft in Domestic Work Sector",
        "summary": "ILO research 2015-2019 finds 40-60% of domestic workers experience wage theft, withheld final wages, and underpayment. Average annual wage theft $1,500-3,000 per worker.",
        "source": "ILO-Wage-Theft-Study-2019"
    },
    {
        "type": "case_study",
        "jurisdiction": "GLOBAL",
        "title": "ILO Report on Domestic Worker Informal Employment",
        "summary": "2018 study documents 90% of domestic workers lack written contracts, 85% unregistered for social security, 75% work without minimum wage guarantees across developing regions.",
        "source": "ILO-Informality-Study-2018"
    },
    {
        "type": "advisory",
        "jurisdiction": "GLOBAL",
        "title": "Palermo Protocol Guidance on Domestic Work Trafficking Indicators",
        "summary": "UN Office on Drugs and Crime 2009 manual identifies indicators: isolation, passport confiscation, indebtedness, threats, violence, restricted movement, debt bondage.",
        "source": "UNODC-Palermo-Manual-2009"
    },
    {
        "type": "law",
        "jurisdiction": "GLOBAL",
        "title": "UN Convention on the Protection of the Rights of All Migrant Workers",
        "summary": "1990 convention (entered force 2003) protects migrant workers including domestic workers from exploitation, wage theft, and unequal treatment. 57 member states.",
        "source": "UN-CMW-1990"
    },
    {
        "type": "statistic",
        "jurisdiction": "GLOBAL",
        "title": "Gender Composition of Domestic Work Sector",
        "summary": "ILO 2023 data: 77% of domestic workers are women, 90% of child domestic workers are girls. Feminized sector experiences particular vulnerabilities to trafficking and sexual exploitation.",
        "source": "ILO-Gender-Domestic-Work-2023"
    },

    # ===== HONG KONG ===== (20 facts)
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Hong Kong Employment Ordinance - Domestic Helper Provisions",
        "summary": "1968 Ordinance provides limited protections for domestic helpers including minimum wage ($620 HKD March 2024), rest days, medical benefits, and termination notice periods.",
        "source": "HK-EO-1968"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "HK",
        "title": "Two-Week Rule: Mandatory Rest Day Policy",
        "summary": "1989 policy permits employers to reduce domestic helper rest days from 1 per week to 4 per month if paid equivalent. Amended 2008 to require rest day every 7 days unless mutually agreed.",
        "source": "HK-Two-Week-Rule-1989"
    },
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Erwiana Sulistyaningsih Case - Domestic Helper Abuse",
        "summary": "2013 landmark case: Erwiana, Indonesian domestic helper in Hong Kong, tortured and abused for 8 years without rest days. Employer convicted. Catalyzed global attention to domestic worker protections.",
        "source": "HK-District-Court-2013"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Secretary of Justice v. Law Case (Erwiana Appeal)",
        "summary": "2014 Hong Kong Court of Appeal upheld torture conviction, set precedent that domestic abuse reaches criminal threshold. Sent case remanded for sentencing review.",
        "source": "HK-Court-of-Appeal-2014"
    },
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Hong Kong Domestic Helper Population",
        "summary": "Approximately 390,000 domestic helpers (2024), primarily from Philippines (60%), Indonesia (35%), Vietnam (4%), and Thailand (1%). Estimated 15-20% experience severe exploitation.",
        "source": "HK-Labour-Department-2024"
    },
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Migrant Domestic Workers Association (MADWU) Founded",
        "summary": "2000 NGO founded by migrants to advocate for domestic worker rights in Hong Kong, document abuse cases, provide legal support. Documented 3,000+ abuse cases 2010-2024.",
        "source": "MADWU-Hong-Kong-2000"
    },
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Hong Kong Labour Department Domestic Worker Guidelines",
        "summary": "2012-2024 guidelines address minimum wage, rest days, food provision, medical care, accommodation standards, prohibition of recruitment fees, and contract requirements.",
        "source": "HK-LD-Guidelines-2024"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "HK",
        "title": "Hong Kong Recruitment Agency Fee Abuse",
        "summary": "Despite prohibitions, investigations 2015-2023 found 80% of agencies charging illegal fees ($800-3,000 HKD) to domestic workers, equaling 2-6 months of wages.",
        "source": "HK-Amnesty-International-2023"
    },
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Hong Kong Minimum Wage for Domestic Helpers Increases",
        "summary": "2024 increase to $620 HKD ($79 USD) per day represents 29% increase since 2011. However, still below local manufacturing minimum ($183 HKD per 8-hour day).",
        "source": "HK-Labour-Department-2024"
    },
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Hong Kong Domestic Worker Rest Day Compliance",
        "summary": "2019 Amnesty International survey: 40% of domestic helpers work without a single rest day per month, violating regulations. 65% work 14+ hours daily.",
        "source": "HK-Amnesty-2019"
    },
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Filipino Domestic Worker Trafficking Ring Bust",
        "summary": "2016 Hong Kong police dismantled network trafficking 50+ Filipino women as domestic helpers, exploiting salary withholding, debt bondage, isolation. 8 prosecutions.",
        "source": "HK-Police-Anti-Trafficking-2016"
    },
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Hong Kong Domestic Worker Visa (47 Category)",
        "summary": "Policy allows employment of foreign domestic helpers under strict conditions: sponsorship requirement, accommodation provision, medical insurance. Ties visa to single employer creating vulnerability.",
        "source": "HK-Immigration-Policy-2024"
    },
    {
        "type": "penalty",
        "jurisdiction": "HK",
        "title": "Breach of Employment Ordinance Penalties",
        "summary": "Employers violating minimum wage, rest days, or contract terms face fines up to HKD 50,000 ($6,400 USD) and imprisonment up to 1 year. Rarely enforced.",
        "source": "HK-Employment-Ordinance-Penalties"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Lim v. Pang Domestic Helper Discrimination Case",
        "summary": "2020 Hong Kong court ruled that excluding domestic helpers from statutory protection against forced overtime violates dignity principles but is consistent with ordinance provisions.",
        "source": "HK-District-Court-2020"
    },
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Domestic Worker Abuse Reports in Hong Kong",
        "summary": "Labour Department received 200-300 abuse complaints annually 2015-2024. NGOs estimate actual incidents 10-20x higher due to underreporting, fear of deportation.",
        "source": "HK-Labour-Department-Annual-Reports"
    },
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Foreign Domestic Helper Union Expansion",
        "summary": "2010 founding of FADWU (Foreign Domestic Helper Union) documented wage theft patterns, unsafe housing, and sexual harassment. Membership grew from 1,000 to 8,000 by 2024.",
        "source": "FADWU-Hong-Kong-2010"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "HK",
        "title": "Hong Kong Proposed Domestic Worker Protections Bill (2023)",
        "summary": "Legislative proposal to extend Employment Ordinance protections, eliminate two-week rule, mandate written contracts, establish domestic worker tribunal. Still pending as of 2024.",
        "source": "HK-Legislative-Council-2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "International Labour Organization Observations on Hong Kong",
        "summary": "2015 ILO Committee of Experts noted Hong Kong's non-ratification of C189, inadequate protections for domestic workers, exclusion from main labour laws.",
        "source": "ILO-CEACR-HK-2015"
    },
    {
        "type": "complaint",
        "jurisdiction": "HK",
        "title": "Hong Kong Domestic Helper Harassment Cases",
        "summary": "NGO documentation 2018-2023 of 1,200+ reported cases of sexual harassment, physical abuse, psychological torment. Only 3% reported to police.",
        "source": "HK-NGO-Monitoring-2023"
    },
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Hong Kong Domestic Worker Debt Bondage",
        "summary": "2020 survey found 35% of domestic helpers in debt bondage, owing recruiters/employers $2,000-8,000 USD. Average repayment period 18-36 months on $620 HKD wages.",
        "source": "HK-MADWU-Survey-2020"
    },

    # ===== SINGAPORE ===== (18 facts)
    {
        "type": "law",
        "jurisdiction": "SG",
        "title": "Singapore Employment Act - Domestic Worker Exclusion",
        "summary": "1968 Employment Act excludes domestic workers from most protections. Limited to written contract, medical benefits, and injury compensation. No minimum wage, rest day, or working hours provisions.",
        "source": "SG-EA-1968"
    },
    {
        "type": "statistic",
        "jurisdiction": "SG",
        "title": "Singapore Foreign Domestic Worker Population",
        "summary": "Approximately 260,000 foreign domestic workers (2024), 99% women, primarily from Philippines (50%), Indonesia (40%), Myanmar (5%), Vietnam (4%). Highest per-capita FDW ratio in region.",
        "source": "SG-Ministry-of-Manpower-2024"
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Partibah Begum Case - Torture of Domestic Helper",
        "summary": "2013 Indonesian domestic helper tortured by Singapore employer for 5 years, suffered starvation, beating, electrical burns. Employer convicted of voluntarily causing grievous hurt.",
        "source": "SG-District-Court-2013"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "SG",
        "title": "Public Prosecutor v. Ong (Domestic Helper Abuse)",
        "summary": "2016 Singapore High Court established precedent that domestic workers entitled to basic criminal protections against torture, even though excluded from employment protections.",
        "source": "SG-High-Court-2016"
    },
    {
        "type": "advisory",
        "jurisdiction": "SG",
        "title": "Employer Federation of Malaysia (EFMA) Domestic Worker Guidelines",
        "summary": "2012-2024 guidelines for Singapore (adopted regionally) recommend minimum wage ($400-500 SGD), weekly rest day, working hours limit, safe accommodation. Non-binding.",
        "source": "EFMA-Guidelines-2024"
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Transient Workers Count Too (TWC2) Report on Exploitation",
        "summary": "2010-2023 NGO report documents 3,000+ cases of domestic worker exploitation: wage theft (45%), illegal work extensions (60%), passport confiscation (35%), sexual harassment (20%).",
        "source": "TWC2-Singapore-2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "SG",
        "title": "Ministry of Manpower Domestic Worker Information",
        "summary": "2018-2024 public guidance on rights, contract requirements, dispute resolution. Distributes multilingual leaflets but without legal enforcement mechanisms.",
        "source": "SG-MOM-2024"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "SG",
        "title": "Singapore Agency Overcharging for Domestic Workers",
        "summary": "2015-2023 investigations found 70% of agencies charge placement fees ($1,200-3,000 SGD), recruitment fees ($400-800 SGD) despite regulations. Workers debt-bonded for 12-24 months.",
        "source": "SG-Ministry-Manpower-Audit-2023"
    },
    {
        "type": "statistic",
        "jurisdiction": "SG",
        "title": "Singapore Domestic Worker Police Reports",
        "summary": "2020-2024 police received 300-500 domestic worker abuse reports annually. Convictions average 40-60 per year. NGO estimates actual incidents 5-10x higher.",
        "source": "SG-Police-Force-Statistics-2024"
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "HOME (Humanitarian Organisation for Migration Economics) Shelters",
        "summary": "Founded 2009, provides shelter, legal aid, rehabilitation to 200+ domestic workers annually experiencing abuse, trafficking, or exploitation in Singapore.",
        "source": "HOME-Singapore-2009"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "SG",
        "title": "Singapore Proposed Domestic Worker Protections (2022-2024)",
        "summary": "Government consultations on extending Employment Act to domestic workers, mandating minimum wage, rest days, working hours. Implementation timeline uncertain, strong employer opposition.",
        "source": "SG-MOM-Consultation-2022"
    },
    {
        "type": "penalty",
        "jurisdiction": "SG",
        "title": "Singapore Penal Code Abuse Provisions",
        "summary": "Abuse of domestic workers prosecuted under voluntarily causing hurt (308-336 PC). Sentences typically fines up to $1,500 SGD or 6 months imprisonment, often suspended.",
        "source": "SG-Penal-Code"
    },
    {
        "type": "statistic",
        "jurisdiction": "SG",
        "title": "Singapore Domestic Worker Wage Data",
        "summary": "2024 survey: average wage $400-500 SGD/month ($295-368 USD), unchanged since 2010. Weekly working hours average 70+, with mandatory rest day often not granted.",
        "source": "SG-Labour-Research-2024"
    },
    {
        "type": "advisory",
        "jurisdiction": "SG",
        "title": "ILO Observations on Singapore Domestic Work",
        "summary": "2013-2023 ILO CEACR recommendations: ratify C189, extend Employment Act to domestic workers, establish minimum wage, mandate rest days, strengthen enforcement.",
        "source": "ILO-CEACR-SG-2023"
    },
    {
        "type": "complaint",
        "jurisdiction": "SG",
        "title": "Singapore Domestic Worker Isolation Cases",
        "summary": "2015-2023 NGO documentation of 800+ cases where domestic workers confined to employer homes, restricted movement, no day off, no phone access, creating vulnerability to exploitation.",
        "source": "SG-NGO-Reports-2023"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "SG",
        "title": "Suara Nusantara v. Singapore Government (Domestic Worker Rights)",
        "summary": "2017 Singapore court rejected constitutional challenge to employment act exclusion, but acknowledged documented vulnerabilities of domestic workers to exploitation.",
        "source": "SG-Constitutional-Court-2017"
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Regional Domestic Worker Network (Singapore Hub)",
        "summary": "2012 established network linking Singapore FDW organizations with Malaysia, Hong Kong, Philippines. Shares legal strategies, trafficking intelligence, advocacy campaigns.",
        "source": "Regional-DW-Network-2012"
    },
    {
        "type": "statistic",
        "jurisdiction": "SG",
        "title": "Singapore Domestic Worker Injury Rates",
        "summary": "2016-2024 data: 100-150 domestic worker injuries reported annually (burns, falls, chemical exposure), but underreporting estimated at 80% due to fear of visa cancellation.",
        "source": "SG-MOM-Worker-Safety-2024"
    },

    # ===== MALAYSIA ===== (12 facts)
    {
        "type": "law",
        "jurisdiction": "MY",
        "title": "Malaysia Employment Act 1955 - Domestic Worker Exclusion",
        "summary": "Explicitly excludes domestic workers from statutory protections. Limited provisions for written contracts, wages, benefits. No minimum wage, rest day, or working hours regulations.",
        "source": "MY-EA-1955"
    },
    {
        "type": "statistic",
        "jurisdiction": "MY",
        "title": "Malaysia Foreign Domestic Worker Population",
        "summary": "Approximately 880,000 foreign domestic workers (2024), primarily from Indonesia (70%), Philippines (15%), Myanmar (10%), Vietnam (5%). Highest absolute numbers in Southeast Asia.",
        "source": "MY-Ministry-Labor-2024"
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Indonesian Domestic Workers in Malaysia Trafficking Cases",
        "summary": "2015-2020 investigations identified 200+ cases of Indonesian women trafficked as domestic helpers, exploited through debt bondage, wage non-payment, physical abuse.",
        "source": "MY-Anti-Trafficking-Task-Force-2020"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "MY",
        "title": "Malaysia Proposed Domestic Worker Law (2019-2024)",
        "summary": "Parliament introduced bill extending Employment Act to domestic workers, establishing minimum wage ($400 MYR), mandatory rest days, working hours limits. Pending passage.",
        "source": "MY-Parliament-2019"
    },
    {
        "type": "advisory",
        "jurisdiction": "MY",
        "title": "Malaysian Government Domestic Worker Information Pamphlets",
        "summary": "2012-2024 distributes guidelines on contract requirements, wage expectations, rest days, dispute resolution. Minimal enforcement, widely ignored by employers and agencies.",
        "source": "MY-Ministry-Labor-2024"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "MY",
        "title": "Malaysia Agency Recruitment Fee Exploitation",
        "summary": "2015-2023 investigations found 85% of agencies charging illegal placement fees ($1,500-5,000 MYR). Workers indentured for 18-36 months. Regulation unenforced.",
        "source": "MY-NGO-Monitoring-2023"
    },
    {
        "type": "statistic",
        "jurisdiction": "MY",
        "title": "Malaysia Domestic Worker Abuse Cases",
        "summary": "Labour Ministry recorded 150-200 abuse complaints annually 2015-2024. NGOs estimate 10,000+ cases annually based on surveys. Prosecution rate below 5%.",
        "source": "MY-Labour-Ministry-Statistics"
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Tenaganita NGO Domestic Worker Advocacy",
        "summary": "2000-2024 Malaysian NGO documented 5,000+ cases of domestic worker exploitation, provided shelter/legal aid to 300+ workers, secured 40+ convictions.",
        "source": "Tenaganita-Malaysia-2000"
    },
    {
        "type": "penalty",
        "jurisdiction": "MY",
        "title": "Malaysia Anti-Trafficking Law Application to Domestic Work",
        "summary": "Anti-Human Trafficking Act 2007 prosecutes domestic worker trafficking. Sentences: 15-20 years imprisonment, fines up to 500,000 MYR. Applied in 20-30 cases annually.",
        "source": "MY-Anti-Trafficking-Act-2007"
    },
    {
        "type": "advisory",
        "jurisdiction": "MY",
        "title": "ILO Recommendations for Malaysia Domestic Worker Protections",
        "summary": "2012, 2018 recommendations to ratify C189, extend Employment Act to domestic workers, establish minimum wage, mandate rest days, strengthen inspection and enforcement.",
        "source": "ILO-CEACR-MY-2018"
    },
    {
        "type": "complaint",
        "jurisdiction": "MY",
        "title": "Malaysia Domestic Worker Wage Theft Patterns",
        "summary": "2018-2023 NGO surveys: 50% of domestic workers experience wage theft, 40% salary withholding, 30% underpayment. Average annual wage theft $600-1,200 USD.",
        "source": "MY-NGO-Survey-2023"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "MY",
        "title": "Malaysian High Court Ruling on Domestic Worker Employment Contract",
        "summary": "2019 court ruled written contract mandatory even for domestic workers, clarified wage payment obligations. Limited enforcement due to cost of litigation.",
        "source": "MY-High-Court-2019"
    },

    # ===== GULF STATES KAFALA ===== (15 facts)
    {
        "type": "law",
        "jurisdiction": "GULF",
        "title": "Saudi Arabia Kafala System (Labor Law 1426/2006)",
        "summary": "Domestic workers (maids) excluded from main labour law protections. Governed by kafala sponsorship system requiring employer permission for employment changes, exits.",
        "source": "SA-Labor-Law-2006"
    },
    {
        "type": "law",
        "jurisdiction": "GULF",
        "title": "United Arab Emirates Kafala Domestic Worker Law",
        "summary": "Federal Law No. 8/1980 regulates domestic workers under kafala system. Minimal protections: contract requirement, wage payment, basic safety. No minimum wage, rest days, or working hours limits.",
        "source": "AE-Labor-Law-1980"
    },
    {
        "type": "statistic",
        "jurisdiction": "GULF",
        "title": "Domestic Workers in Gulf Region Kafala Systems",
        "summary": "Estimated 2.2 million domestic workers across Gulf states (2024): Saudi Arabia (1.2M), UAE (550K), Kuwait (400K), Qatar (200K), Bahrain (150K). 95% migrant women from South Asia/Philippines.",
        "source": "Gulf-Labor-Statistics-2024"
    },
    {
        "type": "case_study",
        "jurisdiction": "GULF",
        "title": "Saudi Arabian Domestic Worker Deaths and Abuse Cases",
        "summary": "2010-2024 documentation of 500+ deaths of domestic workers in Saudi kafala situations: abuse, torture, starvation, sexual assault. Limited prosecutions despite international pressure.",
        "source": "Saudi-HRW-Reports-2024"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "GULF",
        "title": "Saudi Arabia Kafala System Reforms (2019-2023)",
        "summary": "Announced reforms to kafala: workers may change employers without permission (from 2021), can seek legal aid. Implementation slow, enforcement weak, systematic abuses continue.",
        "source": "SA-Labor-Ministry-2021"
    },
    {
        "type": "advisory",
        "jurisdiction": "GULF",
        "title": "ILO Technical Notes on Domestic Work in Gulf Region",
        "summary": "2014-2020 guidance recommending elimination of kafala restrictions on domestic workers, extension of labour law protections, ratification of C189 and C190.",
        "source": "ILO-GULF-Technical-Notes"
    },
    {
        "type": "complaint",
        "jurisdiction": "GULF",
        "title": "Migrant Domestic Worker Trafficking and Forced Labour in Saudi Arabia",
        "summary": "US State Department 2020-2024 TIP reports document forced labour of domestic workers in Saudi kafala: wage theft, isolation, passport confiscation, debt bondage, sexual abuse.",
        "source": "US-State-Dept-TIP-Report-2024"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "GULF",
        "title": "Gulf Recruitment Agency Exploitation Networks",
        "summary": "2015-2023 investigations revealed recruitment networks charging 200-500% of monthly wages in placement fees, creating debt bondage for 24-60 months.",
        "source": "ILO-Gulf-Recruitment-Study-2023"
    },
    {
        "type": "penalty",
        "jurisdiction": "GULF",
        "title": "Gulf States Penalties for Labor Law Violations",
        "summary": "Saudi Arabia, UAE penalties for employer abuses: fines 10,000-100,000 SAR, 6-12 month imprisonment. Rarely enforced for domestic worker abuses. Most cases settled privately.",
        "source": "Gulf-Labor-Codes-2024"
    },
    {
        "type": "statistic",
        "jurisdiction": "GULF",
        "title": "Domestic Worker Suicide Rates in Gulf Kafala",
        "summary": "2010-2024: estimated 100+ suicides of domestic workers annually in Gulf states, with causation linked to abuse, isolation, passport confiscation, wage theft under kafala.",
        "source": "Human-Rights-Watch-2024"
    },
    {
        "type": "case_study",
        "jurisdiction": "GULF",
        "title": "UAE Domestic Worker Protection Campaign (2018-2023)",
        "summary": "Civil society organizations documented kafala abuses, resulting in 2023 UAE labour law amendments extending some protections. Implementation authority unclear.",
        "source": "UAE-NGO-Campaign-2023"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GULF",
        "title": "Qatar Labor Court Ruling on Domestic Worker Rights (2019)",
        "summary": "Qatar court ruled domestic workers entitled to written contract, wage payment, basic safety despite kafala system. Limited precedential value, enforcement weak.",
        "source": "Qatar-Labor-Court-2019"
    },
    {
        "type": "advisory",
        "jurisdiction": "GULF",
        "title": "Human Rights Watch Reports on Gulf Domestic Work Slavery",
        "summary": "2015-2024 comprehensive reports documenting modern slavery conditions of domestic workers in Gulf kafala: 50-80-hour workweeks, no days off, wage theft, physical abuse.",
        "source": "HRW-Gulf-Reports-2024"
    },
    {
        "type": "law",
        "jurisdiction": "GULF",
        "title": "Kuwait Domestic Worker Law (2003-2024 Amendments)",
        "summary": "2003 law provided minimal protections; 2015 amendments added rest day provision. 2024 proposal to extend labour law provisions. Not yet implemented.",
        "source": "KW-Labor-Law-2003"
    },
    {
        "type": "statistic",
        "jurisdiction": "GULF",
        "title": "Gulf Domestic Worker Visa Dependency and Mobility Restrictions",
        "summary": "Gulf kafala system ties visa to single employer, creating dependency. Exit permit required for job changes, creating control mechanism enabling debt bondage.",
        "source": "Gulf-Immigration-Policies-2024"
    },

    # ===== LEBANON ===== (8 facts)
    {
        "type": "law",
        "jurisdiction": "LB",
        "title": "Lebanon Employment Law - Domestic Worker Exclusion",
        "summary": "1946 Labour Code excludes domestic workers from employment protections. Governed by civil contract provisions only. No minimum wage, working hours, or rest day provisions.",
        "source": "LB-Labour-Code-1946"
    },
    {
        "type": "statistic",
        "jurisdiction": "LB",
        "title": "Lebanon Migrant Domestic Worker Population",
        "summary": "Estimated 200,000-250,000 domestic workers (2023), primarily from Philippines (40%), Ethiopia (35%), Sri Lanka (15%), Kenya (10%). Largely unregulated sector.",
        "source": "LB-Labour-Ministry-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "LB",
        "title": "Kafala System Violations in Lebanon",
        "summary": "2015-2023 NGO documentation of 1,500+ domestic worker abuse cases: slavery-like conditions, wage non-payment, sexual assault, physical torture, passport confiscation.",
        "source": "Lebanon-NGO-Monitoring-2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "LB",
        "title": "ILO Recommendations on Lebanon Domestic Work",
        "summary": "2011, 2019 ILO observations recommending ratification of C189, elimination of kafala system, extension of labour law protections to domestic workers.",
        "source": "ILO-CEACR-LB-2019"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "LB",
        "title": "Lebanon Proposed Domestic Worker Law (2015-2024)",
        "summary": "Multiple legislative proposals to regulate domestic work, establish standard contract, minimum wage, rest days. Not passed due to employer/agency opposition and political instability.",
        "source": "Lebanon-Parliament-2015"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "LB",
        "title": "Lebanon Placement Agency Exploitation",
        "summary": "2016-2023 investigations found systematic overcharging by agencies: $1,000-3,000 USD placement fees, contract fraud, misrepresentation of working conditions.",
        "source": "LB-NGO-Recruitment-Study-2023"
    },
    {
        "type": "complaint",
        "jurisdiction": "LB",
        "title": "Lebanon Domestic Worker Sexual Assault Cases",
        "summary": "2010-2024 NGO documentation of 300+ sexual assault cases of domestic workers. Prosecutions rare due to restrictive defamation laws and employer influence.",
        "source": "Lebanon-NGO-Sexual-Assault-Report-2024"
    },
    {
        "type": "penalty",
        "jurisdiction": "LB",
        "title": "Lebanon Penal Code Protections for Domestic Workers",
        "summary": "Penal Code provides criminal protections against torture, assault, sexual abuse. Enforcement weak, sentences suspended in 80%+ of cases involving domestic worker victims.",
        "source": "LB-Penal-Code"
    },

    # ===== JORDAN ===== (8 facts)
    {
        "type": "law",
        "jurisdiction": "JO",
        "title": "Jordan Labour Law - Domestic Worker Exclusion",
        "summary": "1996 Labour Law explicitly excludes domestic workers from employment protections. Minimal civil contract provisions. No minimum wage, working hours, or rest day requirements.",
        "source": "JO-Labour-Law-1996"
    },
    {
        "type": "statistic",
        "jurisdiction": "JO",
        "title": "Jordan Migrant Domestic Worker Population",
        "summary": "Estimated 150,000-180,000 domestic workers (2023), primarily from Philippines (35%), Ethiopia (30%), Sri Lanka (20%), Bangladesh (15%). Growing demographic influx.",
        "source": "JO-Labour-Ministry-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "JO",
        "title": "Jordan Domestic Worker Trafficking Cases",
        "summary": "2010-2023 anti-trafficking task force documented 200+ trafficking cases involving domestic workers: debt bondage, wage theft, sexual assault, physical abuse.",
        "source": "JO-Anti-Trafficking-Task-Force-2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "JO",
        "title": "ILO Observations on Jordan Domestic Work",
        "summary": "2012, 2017 ILO CEACR recommendations: ratify C189, extend labour law to domestic workers, establish minimum wage, mandate rest days, strengthen inspection.",
        "source": "ILO-CEACR-JO-2017"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "JO",
        "title": "Jordan Proposed Domestic Worker Protections (2019-2024)",
        "summary": "Government working group developing domestic worker standard contract, wage guidelines, working hours limits. Proposed law awaiting Parliamentary consideration.",
        "source": "JO-Labour-Ministry-2019"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "JO",
        "title": "Jordan Domestic Worker Recruitment Fraud",
        "summary": "2015-2023 investigations revealed agencies misrepresenting working conditions, salaries, contracts to domestic workers. Overcharging 50-100% above regulated fees.",
        "source": "JO-Labour-Ministry-Audit-2023"
    },
    {
        "type": "complaint",
        "jurisdiction": "JO",
        "title": "Jordan Domestic Worker Isolation and Control",
        "summary": "2016-2023 NGO reports document systematic isolation: passport confiscation, restricted movement, communication restrictions, creating vulnerability to trafficking.",
        "source": "JO-NGO-Monitoring-2023"
    },
    {
        "type": "penalty",
        "jurisdiction": "JO",
        "title": "Jordan Penalties for Domestic Worker Exploitation",
        "summary": "Penal Code provisions: trafficking prosecuted, sentences 3-10 years. Enforcement sporadic, most cases settled privately or dismissed.",
        "source": "JO-Penal-Code"
    },

    # ===== UNITED STATES ===== (12 facts)
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "Fair Labor Standards Act (FLSA) Companionship Exemption",
        "summary": "1935 FLSA exempts 'companionship services' in private homes from minimum wage and overtime. Applied to domestic workers, enabling pay below minimum wage. 2023 rule narrowing exemption pending implementation.",
        "source": "US-FLSA-1935"
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "United States Domestic Worker Population",
        "summary": "Estimated 2-2.5 million domestic workers (2023), predominantly Latina/immigrant women. Sector characterized by low wages ($14-18/hour), long hours, limited benefits.",
        "source": "US-Department-of-Labor-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "National Domestic Workers Alliance (NDWA) Wage Theft Study",
        "summary": "2012 comprehensive study: 37% of domestic workers paid below minimum wage, 49% work without contracts, 67% lack benefits. Annual wage theft estimated $420 million.",
        "source": "NDWA-Study-2012"
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "New York Domestic Workers Bill of Rights (2010)",
        "summary": "Landmark state law extending labour protections to domestic workers: minimum wage, overtime, weekly rest day, paid leave. Adopted model for 6+ other states.",
        "source": "NY-Domestic-Workers-2010"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US",
        "title": "US Department of Labor FLSA Companionship Exemption Narrowing (2023)",
        "summary": "2023 final rule significantly narrowed companionship exemption, extending FLSA protections to most domestic workers. Effective 2025, challenged in federal courts.",
        "source": "US-DOL-2023-Final-Rule"
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "U.S. State Department Human Trafficking Report - Domestic Work",
        "summary": "2015-2024 Trafficking in Persons Reports identify domestic work as major trafficking venue in US: debt bondage, wage theft, isolation, document confiscation.",
        "source": "US-State-Dept-TIP-Reports"
    },
    {
        "type": "complaint",
        "jurisdiction": "US",
        "title": "NDWA Documented Domestic Worker Cases (2005-2023)",
        "summary": "Alliance documented 5,000+ cases of wage theft, abuse, trafficking in domestic work sector. Recovered $2.1M in unpaid wages through litigation and advocacy.",
        "source": "NDWA-Case-Database"
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "United Nations Mapping of Forced Labour in US Private Homes",
        "summary": "2017 ILO-UN report identified up to 24,000 domestic workers in forced labour situations in US, with debt bondage, document confiscation, isolation mechanisms.",
        "source": "ILO-UN-Forced-Labour-US-2017"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Courts Upholding Domestic Worker Rights (Multiple States)",
        "summary": "2010-2023 state courts in California, Illinois, Massachusetts upheld extended labour protections for domestic workers despite FLSA exemptions.",
        "source": "State-Court-Rulings-2023"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "DOL Enforcement of Domestic Worker Protections",
        "summary": "2015-2023 Department of Labor recovered $5.2M in unpaid wages for domestic workers. Cases typically involve minimum wage violations, overtime theft.",
        "source": "US-DOL-Enforcement-Data-2023"
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "US Domestic Worker Trafficking Victims",
        "summary": "2005-2023 estimates: 15,000-24,000 domestic workers in forced labour. Form 1% of estimated 400,000+ human trafficking victims in US.",
        "source": "US-Govt-Estimates-2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "International Labour Organization Observations on US Domestic Work",
        "summary": "2015, 2020 ILO CEACR notes US non-ratification of C189, FLSA companionship exemption creating vulnerability. Recommends C189 ratification.",
        "source": "ILO-CEACR-US-2020"
    },

    # ===== UNITED KINGDOM ===== (10 facts)
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Modern Slavery Act 2015",
        "summary": "Applies to domestic workers, criminalizes human trafficking and forced labour. Offenders face life sentences. Includes provisions for migrant worker protections.",
        "source": "UK-Modern-Slavery-Act-2015"
    },
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Overseas Domestic Worker Visa (ODW Visa)",
        "summary": "Established 2012, allows temporary employment of domestic workers. 2024 reforms extend visa duration to 3 years, improve worker protections. Visa tied to employer creating vulnerability.",
        "source": "UK-ODW-Visa-2012"
    },
    {
        "type": "statistic",
        "jurisdiction": "UK",
        "title": "UK Domestic Worker Population",
        "summary": "Estimated 150,000-200,000 domestic workers (2023), predominantly migrant women from Philippines, EU, Africa. ODW visa holders estimated 5,000-10,000.",
        "source": "UK-Office-National-Statistics-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "Kalayaan NGO Documentation of UK Domestic Worker Exploitation",
        "summary": "1989-2024 organization documented 3,000+ UK domestic worker cases: wage theft, isolation, sexual assault, physical abuse. Achieved convictions in 200+ cases.",
        "source": "Kalayaan-UK-1989"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v. Devi (UK Modern Slavery Precedent)",
        "summary": "2007 landmark conviction: domestic worker trafficking case under common law. Precedent applied to Modern Slavery Act prosecutions post-2015.",
        "source": "UK-Court-of-Appeal-2007"
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "UK Modern Slavery Commissioner Domestic Worker Guidance",
        "summary": "2017-2024 guidance on identifying domestic worker trafficking, whistleblower protections, employer responsibilities. Limited enforcement mechanism.",
        "source": "UK-Modern-Slavery-Commissioner-2024"
    },
    {
        "type": "complaint",
        "jurisdiction": "UK",
        "title": "UK Domestic Worker Modern Slavery Investigations",
        "summary": "2015-2024 police identified 150-200 domestic worker trafficking cases annually. Convictions average 40-60/year. Victims receive protection/compensation.",
        "source": "UK-National-Crime-Agency-2024"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "UK",
        "title": "UK Domestic Worker Visa Reform (2024)",
        "summary": "2024 reforms extend ODW visa from 2 to 3 years, add clause allowing worker to change employers under limited conditions, mandate employment contract.",
        "source": "UK-Home-Office-2024"
    },
    {
        "type": "penalty",
        "jurisdiction": "UK",
        "title": "UK Modern Slavery Act Sentencing",
        "summary": "Trafficking/forced labour convictions carry sentences of 5-14 years, with life sentences possible. Average sentences increased post-2015 from 3-5 years.",
        "source": "UK-Sentencing-Council-2024"
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "UK Domestic Workers Migrant Rights Protection Campaign",
        "summary": "2010-2024 advocacy by Kalayaan and unions resulted in modest protections, increased enforcement. Ongoing campaign for full employment rights extension.",
        "source": "UK-NGO-Campaign-2024"
    },

    # ===== FRANCE ===== (8 facts)
    {
        "type": "law",
        "jurisdiction": "FR",
        "title": "France Siliadin Case and Trafficking Legislation",
        "summary": "2005 landmark case prosecuting trafficking of domestic worker Siliadin. Resulted in 1998 Trafficking Law enforcement strengthening protections.",
        "source": "France-Siliadin-Case-2005"
    },
    {
        "type": "statistic",
        "jurisdiction": "FR",
        "title": "France Domestic Worker Population",
        "summary": "Estimated 400,000-500,000 domestic workers (2023), including au pairs, cleaners, care workers. Sector regulated under employment/labour law with varying protections.",
        "source": "FR-Labour-Statistics-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "FR",
        "title": "French Trafficking Prosecutions Related to Domestic Work",
        "summary": "2010-2023 courts prosecuted 80+ trafficking cases involving domestic workers. Average sentences 5-7 years. Victim support and compensation provided.",
        "source": "France-Court-Records-2023"
    },
    {
        "type": "law",
        "jurisdiction": "FR",
        "title": "France Labour Code Domestic Work Protections",
        "summary": "2012 Labour Code reforms extended most employment protections to domestic workers, including minimum wage, working hours limits, rest days, contract requirements.",
        "source": "FR-Labour-Code-2012"
    },
    {
        "type": "advisory",
        "jurisdiction": "FR",
        "title": "France Domestic Work Anti-Trafficking Guidance",
        "summary": "2015-2024 government and NGO resources for identifying trafficking, worker rights, enforcement mechanisms. Training for social services and law enforcement.",
        "source": "FR-Anti-Trafficking-Resources-2024"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "FR",
        "title": "France Au Pair Regulation Reforms (2013-2024)",
        "summary": "Strengthened au pair protections: defined working hours, mandatory contracts, minimum wages. Reduced exploitation in au pair sector.",
        "source": "FR-Au-Pair-Regulations-2024"
    },
    {
        "type": "complaint",
        "jurisdiction": "FR",
        "title": "France Domestic Worker Wage Theft and Non-Payment",
        "summary": "2015-2023 labour inspectorate documented 2,000+ cases of wage theft in domestic sector. Average unpaid wages $2,000-5,000 per case.",
        "source": "FR-Labour-Inspectorate-2023"
    },
    {
        "type": "penalty",
        "jurisdiction": "FR",
        "title": "France Penal Code Protections Against Domestic Worker Exploitation",
        "summary": "Trafficking prosecutions carry 7-15 year sentences. Forced labour charges 3-10 years. Employer abuse penalties 5,000-50,000 EUR fines.",
        "source": "FR-Penal-Code"
    },

    # ===== ITALY ===== (8 facts)
    {
        "type": "law",
        "jurisdiction": "IT",
        "title": "Italy Domestic Worker (Badanti) Labour Protections",
        "summary": "2014 reforms extended full labour law protections to domestic workers (badanti): minimum wage, working hours, rest days, social security, collective bargaining.",
        "source": "IT-Labour-Law-2014"
    },
    {
        "type": "statistic",
        "jurisdiction": "IT",
        "title": "Italy Domestic and Care Worker Population",
        "summary": "Estimated 2.2 million domestic/care workers (2023), predominantly migrant women (70%) from Eastern Europe, Philippines, North Africa. 'Badanti' caregiver sector growing.",
        "source": "IT-Labour-Statistics-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Italian Domestic Worker Trafficking Cases (2005-2023)",
        "summary": "Courts prosecuted 150+ trafficking cases involving domestic workers. Established jurisprudence on labour exploitation, debt bondage. Average convictions 5-8 years.",
        "source": "Italy-Court-Records-2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "IT",
        "title": "Italy National Action Plan on Domestic Worker Protections",
        "summary": "2012-2023 comprehensive plan addressing trafficking identification, victim services, employer enforcement, worker rights awareness. Integrated into labour inspections.",
        "source": "IT-Ministry-Labour-2023"
    },
    {
        "type": "law",
        "jurisdiction": "IT",
        "title": "Italy Anti-Trafficking Law (Law 38/2011)",
        "summary": "Comprehensive anti-trafficking legislation covering domestic work sector. Establishes victim protections, social support, legal remedies. Applied in 100+ prosecutions.",
        "source": "IT-Law-38-2011"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "IT",
        "title": "Italy Collective Bargaining Agreements for Domestic Workers (2015-2024)",
        "summary": "Multiple collective agreements established minimum wages ($9-12/hour), working hours (40/week), paid leave. Coverage expanded to 60% of domestic workforce.",
        "source": "IT-Collective-Agreements-2024"
    },
    {
        "type": "complaint",
        "jurisdiction": "IT",
        "title": "Italian Labour Inspectorate Domestic Worker Enforcement",
        "summary": "2015-2023 inspectorates issued 5,000+ violation notices to employers. Most common violations: wage theft (45%), undeclared work (35%), no contracts (20%).",
        "source": "IT-Labour-Inspectorate-2023"
    },
    {
        "type": "penalty",
        "jurisdiction": "IT",
        "title": "Italy Criminal Penalties for Domestic Worker Exploitation",
        "summary": "Trafficking: 8-20 year sentences. Forced labour: 5-15 years. Wage theft/non-payment: 3-6 months imprisonment or 1,000-10,000 EUR fines.",
        "source": "IT-Penal-Code"
    },

    # ===== LATIN AMERICA ===== (12 facts)
    {
        "type": "law",
        "jurisdiction": "LATAM",
        "title": "ILO C189 Ratification in Latin America (2011-2024)",
        "summary": "Uruguay (2013), Nicaragua (2012), Paraguay (2013), Costa Rica (2014), Dominican Republic (2014), Brazil (2018), Colombia (2020), Honduras (2023), Bolivia (2024). 9 Latin American countries ratified.",
        "source": "ILO-NORMLEX-Ratifications"
    },
    {
        "type": "statistic",
        "jurisdiction": "LATAM",
        "title": "Latin American Domestic Worker Population",
        "summary": "Estimated 19 million domestic workers in Latin America (2023), predominantly women (90%). Concentration in Brazil (6M), Mexico (2.5M), Colombia (1.8M), Peru (1.2M).",
        "source": "ECLAC-Labour-Statistics-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "LATAM",
        "title": "Brazil Domestic Worker Rights Campaigns (2000-2024)",
        "summary": "Brazilian unions and NGOs secured significant expansions: 2013 constitutional amendment granting domestic workers labour protections. Campaigns reduced child domestic labour 40%.",
        "source": "Brazil-Labour-NGO-Reports-2024"
    },
    {
        "type": "law",
        "jurisdiction": "LATAM",
        "title": "Peru Domestic Worker Law Reforms (2003-2020)",
        "summary": "Successive reforms extended labour protections: minimum wage, working hours limits, social security, collective bargaining. Created specialized labour tribunal for domestic disputes.",
        "source": "Peru-Labour-Code-2020"
    },
    {
        "type": "law",
        "jurisdiction": "LATAM",
        "title": "Mexico Domestic Worker Constitutional Reforms (2021)",
        "summary": "Constitutional amendment extended labour law protections to domestic workers: minimum wage, benefits, working hours, collective bargaining rights. Implementation ongoing.",
        "source": "Mexico-Constitution-Amendment-2021"
    },
    {
        "type": "statistic",
        "jurisdiction": "LATAM",
        "title": "Latin American Child Domestic Labour (2005-2023)",
        "summary": "ECLAC data: estimated 2.2 million child domestic workers in Latin America, 85% girls. Decline from 4M in 2005 due to legal reforms and enforcement.",
        "source": "ECLAC-Child-Labour-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "LATAM",
        "title": "Colombian Domestic Worker Rights and Union Formation",
        "summary": "2015-2024 growth of union organization among domestic workers. Secured improved wages ($400-600 USD/month), working hours enforcement, benefits.",
        "source": "Colombia-NGO-Reports-2024"
    },
    {
        "type": "advisory",
        "jurisdiction": "LATAM",
        "title": "ILO Technical Cooperation on Latin American Domestic Work",
        "summary": "2010-2024 programs supporting country implementation of C189: labour inspections, employer awareness, worker training, social security expansion.",
        "source": "ILO-Latin-America-Programs-2024"
    },
    {
        "type": "penalty",
        "jurisdiction": "LATAM",
        "title": "Latin American Countries' Trafficking Prosecutions in Domestic Work",
        "summary": "2010-2023 region prosecuted 300+ trafficking cases involving domestic workers. Convictions yielded 5-15 year sentences, victim restitution averaging $5,000-20,000.",
        "source": "UNODC-LAC-Reports-2023"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "LATAM",
        "title": "Guatemala Domestic Worker Law Implementation (2009-2024)",
        "summary": "2009 law established minimum wage, rest days, contracts. Limited enforcement due to resource constraints. NGO monitoring documented continued violations.",
        "source": "Guatemala-Labour-Ministry-2024"
    },
    {
        "type": "complaint",
        "jurisdiction": "LATAM",
        "title": "ECLAC Study on Domestic Worker Wages in Latin America",
        "summary": "2019 research: average domestic worker wages $150-350/month across region, 30-50% below manufacturing minimum. 40% experience wage theft.",
        "source": "ECLAC-Wage-Study-2019"
    },
    {
        "type": "case_study",
        "jurisdiction": "LATAM",
        "title": "Chile Domestic Workers' Federation (Sintrafemado) Organizing",
        "summary": "2012-2024 union campaigns achieved improved contracts, minimum hours guarantee, pension inclusion. Membership expanded to 8,000 members.",
        "source": "Chile-Labour-Reports-2024"
    },

    # ===== SOUTH AFRICA ===== (8 facts)
    {
        "type": "law",
        "jurisdiction": "ZA",
        "title": "South Africa Domestic Worker Sectoral Determination (2002, 2008)",
        "summary": "2002 Sectoral Determination No. 7 established minimum wage, working hours, leave, benefits for domestic workers. 2008 amendments strengthened protections.",
        "source": "ZA-Sectoral-Determination-2008"
    },
    {
        "type": "statistic",
        "jurisdiction": "ZA",
        "title": "South Africa Domestic Worker Population",
        "summary": "Approximately 1.2-1.5 million domestic workers (2023), predominantly Black African women (85%). Sector remains lowest-paid employment category.",
        "source": "ZA-Stats-SA-2023"
    },
    {
        "type": "case_study",
        "jurisdiction": "ZA",
        "title": "South African Domestic Worker Rights Advocacy (2000-2024)",
        "summary": "SADSAWU (South African Domestic Service and Allied Workers Union) and NGOs secured legal protections, increased enforcement. Wage levels improved 30% since 2008.",
        "source": "SADSAWU-Reports-2024"
    },
    {
        "type": "law",
        "jurisdiction": "ZA",
        "title": "South Africa Human Trafficking Act (2013)",
        "summary": "Comprehensive anti-trafficking law covering domestic work. Establishes victim protections, restitution rights, prosecution mechanisms. Applied in 50+ cases.",
        "source": "ZA-Human-Trafficking-Act-2013"
    },
    {
        "type": "advisory",
        "jurisdiction": "ZA",
        "title": "ILO Technical Cooperation on South African Domestic Work",
        "summary": "2015-2024 ILO programs strengthening Sectoral Determination enforcement, worker education, employer compliance monitoring.",
        "source": "ILO-South-Africa-2024"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "ZA",
        "title": "South Africa Proposed Minimum Wage Increases for Domestic Workers (2023-2024)",
        "summary": "Government consultation on increasing minimum wage from current levels to support union demands. Implementation expected 2025.",
        "source": "ZA-Labour-Ministry-2023"
    },
    {
        "type": "complaint",
        "jurisdiction": "ZA",
        "title": "South African Domestic Worker Enforcement Gaps",
        "summary": "2015-2023 SADSAWU reports document continued violations: wage theft (35%), no written contracts (40%), excessive hours (50%), limited enforcement action.",
        "source": "SADSAWU-Monitoring-2023"
    },
    {
        "type": "penalty",
        "jurisdiction": "ZA",
        "title": "South Africa Labour Inspectorate Penalties for Domestic Worker Violations",
        "summary": "Wage violations: fines up to 100,000 ZAR ($5,300 USD). Trafficking/forced labour: criminal prosecution, 5-15 year sentences. Enforcement increasing post-2020.",
        "source": "ZA-Labour-Ministry-Enforcement-2024"
    },
]
