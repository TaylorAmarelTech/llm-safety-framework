"""Anti-trafficking organizations, hotlines, and resources worldwide.

Covers International IGOs, USA federal and NGO resources, UK organizations,
European networks, Asian civil society, African agencies, and Americas-based
organizations working to combat human trafficking and migrant worker exploitation.
"""

ANTI_TRAFFICKING_ORGANIZATION_FACTS: list[dict] = [

    # ── International Organizations (IOM) ──────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "INTL",
        "title": "International Organization for Migration — Global Anti-Trafficking Program",
        "summary": "IOM operates counter-trafficking programs in over 100 countries, providing direct assistance to trafficking victims including safe shelter, medical care, legal aid, and voluntary return and reintegration. IOM's Global Victim of Trafficking Identification and Reintegration program has assisted over 100,000 identified victims since 2000. Contact: iom.int/counter-trafficking, headquarters Geneva +41 22 717 9111.",
        "source": "IOM, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "IOM — Migrants in Vulnerable Situations: Principles and Guidelines",
        "summary": "IOM guidelines establish minimum standards for identification of trafficking victims among migrant populations, including indicators of labor trafficking, sexual exploitation, and debt bondage. Advises front-line responders to apply a non-punitive, trauma-informed approach. Guidelines adopted by 173 IOM member states as operational framework.",
        "source": "IOM, 2018",
    },
    {
        "type": "statistic",
        "jurisdiction": "INTL",
        "title": "IOM — Missing Migrants Project: Deaths on Migration Routes 2014-2024",
        "summary": "IOM's Missing Migrants Project has recorded over 63,000 migrant deaths and disappearances globally between 2014 and 2024, with the Mediterranean accounting for over 30,000. The project documents cases where trafficking vulnerability intersects with dangerous migration routes. Data underpins policy advocacy for legal migration pathways as anti-trafficking tools.",
        "source": "IOM Missing Migrants Project, 2024",
    },
    {
        "type": "policy_update",
        "jurisdiction": "INTL",
        "title": "IOM — The IRIS Standard for Ethical Recruitment",
        "summary": "IOM's International Recruitment Integrity System (IRIS) launched in 2015 certifies recruitment agencies that meet ethical standards including no fees charged to workers, transparency in contracts, and access to grievance mechanisms. By 2024, over 70 agencies across 30 countries hold IRIS certification. Employers can verify certified agencies at iomiris.org.",
        "source": "IOM IRIS, 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "INTL",
        "title": "IOM — Labor Migration and Forced Labor: Scale Estimates 2023",
        "summary": "IOM estimates that of approximately 169 million international migrant workers, an estimated 27.6 million (16%) are in forced labor conditions. The highest absolute numbers are in Asia-Pacific (15.1 million), with the highest prevalence rates in Arab states (52 per 1,000 people). Agricultural, construction, domestic work, and manufacturing sectors account for 70% of cases.",
        "source": "IOM / ILO Joint Estimate, 2022",
    },

    # ── International Organizations (UNODC) ────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "UNODC — Blue Heart Campaign Against Human Trafficking",
        "summary": "UNODC's Blue Heart Campaign raises awareness about human trafficking globally. Provides training to law enforcement and border officials in 140+ countries on victim identification using the UNODC Human Trafficking Case Law Database. Partners can access training modules at unodc.org/blueheart. Campaign has reached over 500 million people through media partnerships.",
        "source": "UNODC Blue Heart Campaign, 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "INTL",
        "title": "UNODC — Global Report on Trafficking in Persons 2022",
        "summary": "UNODC's 2022 Global Report found 49,105 detected trafficking victims globally, a 11% decrease from 2019 attributable partly to COVID-19 disruptions in detection. Women and girls account for 72% of detected victims. Forced labor comprises 38% of detected forms. Conviction rates remain abysmally low: only 0.1% of estimated victims result in a trafficking conviction.",
        "source": "UNODC, 2022",
    },
    {
        "type": "law",
        "jurisdiction": "INTL",
        "title": "UNODC — Model Law Against Trafficking in Persons (2009)",
        "summary": "UNODC's Model Law provides a legislative template for states implementing the Palermo Protocol. Covers definitions of trafficking, victim identification procedures, victim protection measures, criminalization standards, and international cooperation provisions. Used as the basis for national legislation in over 50 countries, including amendments to existing penal codes.",
        "source": "UNODC, 2009",
    },
    {
        "type": "case_study",
        "jurisdiction": "INTL",
        "title": "UNODC — Case Law Database: Landmark Trafficking Convictions",
        "summary": "UNODC maintains a publicly searchable database of over 1,200 trafficking court cases across 100+ countries at sherloc.unodc.org. Database enables comparative analysis of prosecution strategies, victim identification methods, and sentencing patterns. Notable cases include convictions in supply chain labor trafficking and state-facilitated forced labor.",
        "source": "UNODC SHERLOC Database, 2024",
    },

    # ── International Organizations (ILO) ──────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "ILO — Operational Indicators of Trafficking in Human Beings (2009, updated 2023)",
        "summary": "ILO's operational indicators provide front-line responders with concrete signs of labor and sexual trafficking. The 11 forced labor indicators include: abuse of vulnerability, deception, restriction of movement, isolation, physical/sexual violence, intimidation, document retention, wage withholding, debt bondage, abusive conditions, and excessive overtime. Free at ilo.org/trafficking.",
        "source": "ILO, 2009, updated 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "INTL",
        "title": "ILO — Global Estimates of Modern Slavery 2022",
        "summary": "ILO's 2022 global estimates found 49.6 million people in modern slavery: 27.6 million in forced labor and 22 million in forced marriage. Of those in forced labor, 17.3 million are exploited in the private economy, 6.3 million in forced commercial sexual exploitation, and 3.9 million in state-imposed forced labor. Migrant workers are three times more likely to be in forced labor than non-migrants.",
        "source": "ILO, Walk Free Foundation, IOM, 2022",
    },
    {
        "type": "policy_update",
        "jurisdiction": "INTL",
        "title": "ILO — Fair Recruitment Initiative (2014-present)",
        "summary": "ILO's Fair Recruitment Initiative promotes laws, policies, and enforcement mechanisms that protect workers during recruitment. Key elements: no recruitment fees charged to workers (employer-pays model), transparent and enforceable contracts, access to justice, and portability of skills credentials. Implemented across 30+ countries in partnership with governments and employers.",
        "source": "ILO Fair Recruitment Initiative, 2024",
    },
    {
        "type": "law",
        "jurisdiction": "INTL",
        "title": "ILO Convention No. 181 on Private Employment Agencies (1997)",
        "summary": "ILO C181 requires states to prohibit private employment agencies from charging fees to workers, ensure contract transparency, and establish licensing and enforcement mechanisms. By 2024, 41 countries have ratified C181. Key provision Article 7: private employment agencies shall not charge workers any fees or costs for their services.",
        "source": "ILO C181, 1997",
    },

    # ── International Organizations (OHCHR) ────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "OHCHR — Recommended Principles and Guidelines on Human Rights and Human Trafficking",
        "summary": "OHCHR's 2002 Recommended Principles established that anti-trafficking measures must not adversely affect the rights of migrants, and that victims must not be prosecuted for offenses committed as a direct result of their trafficking. These principles underpin non-criminalization policies adopted in 80+ countries. Available at ohchr.org/trafficking.",
        "source": "OHCHR, 2002",
    },
    {
        "type": "policy_update",
        "jurisdiction": "INTL",
        "title": "OHCHR — UN Special Rapporteur on Trafficking in Persons",
        "summary": "The UN Special Rapporteur on Trafficking in Persons conducts country visits, receives individual complaints, and publishes thematic reports to the Human Rights Council and General Assembly. The mandate has addressed: trafficking in conflict zones (2016), trafficking of children (2019), technology-facilitated trafficking (2020), climate change and trafficking (2022), and corporate supply chains (2023).",
        "source": "OHCHR, 2024",
    },

    # ── International Organizations (OSCE) ─────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "EUROPE",
        "title": "OSCE — Office of the Special Representative and Co-ordinator for Combating Trafficking in Human Beings",
        "summary": "The OSCE's anti-trafficking mandate covers 57 participating states across Europe, Central Asia, and North America. The Office monitors implementation of commitments, provides technical assistance to national referral mechanisms, and publishes reports on labor trafficking, trafficking in conflict, and demand reduction. Contact: osce.org/secretariat/trafficking.",
        "source": "OSCE, 2024",
    },
    {
        "type": "policy_update",
        "jurisdiction": "EUROPE",
        "title": "OSCE — National Referral Mechanisms: Implementation Report 2023",
        "summary": "OSCE surveyed national referral mechanisms (NRMs) across 46 participating states. Found that 39 states have formal NRMs but only 22 have legally binding NRM frameworks. Key gaps: victim identification in labor settings, access to compensation funds, and legal stay provisions during recovery periods. Recommended binding legal frameworks and multi-agency cooperation protocols.",
        "source": "OSCE, 2023",
    },

    # ── Walk Free Foundation / Global Slavery Index ─────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "INTL",
        "title": "Walk Free Foundation — Global Slavery Index 2023",
        "summary": "The Walk Free Foundation's 2023 Global Slavery Index estimated 49.6 million people in modern slavery globally, with North Korea, Eritrea, Mauritania, Saudi Arabia, and Turkey having the highest prevalence rates. The index found G20 nations import USD 468 billion worth of at-risk goods annually. India has the highest absolute number of people in modern slavery at 11 million.",
        "source": "Walk Free Foundation, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Walk Free Foundation — Ending Modern Slavery: Government Responses Index 2023",
        "summary": "Walk Free's Government Response Index scores 160 governments on survivor support, policy coordination, supply chain laws, prosecution rates, and international cooperation. Netherlands, UK, and Australia ranked highest. Gap analysis found that even high-scoring governments fail on survivor-centered support. Report calls for mandatory corporate reporting and survivor inclusion in policy design.",
        "source": "Walk Free Foundation, 2023",
    },

    # ── GAATW (Global Alliance Against Traffic in Women) ───────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "GAATW — Collateral Damage: The Impact of Anti-Trafficking Measures on Human Rights Around the World",
        "summary": "GAATW's landmark 2007 report documented how anti-trafficking policies often harm migrant workers and sex workers rather than helping them. Found that border enforcement in the name of anti-trafficking resulted in increased deportations of irregular migrants and criminalization of migration. Recommended rights-based approaches centering migrant worker agency and access to justice.",
        "source": "GAATW, 2007",
    },
    {
        "type": "policy_update",
        "jurisdiction": "INTL",
        "title": "GAATW — Labour Migration and Trafficking: Ensuring Labour Migrants' Access to Justice (2018)",
        "summary": "GAATW analysis of 10 destination countries found labor migrants face structural barriers to justice including immigration status fears, language barriers, high legal costs, and retaliation risks. Recommended decoupling immigration enforcement from labor law enforcement, providing temporary legal status to complainants, and funding migrant worker legal aid organizations.",
        "source": "GAATW, 2018",
    },
    {
        "type": "contact",
        "jurisdiction": "TH",
        "title": "GAATW International Secretariat — Bangkok",
        "summary": "GAATW's international secretariat is based in Bangkok, Thailand and coordinates a network of 120+ member organizations across 40 countries. Provides advocacy tools, legal analyses, and capacity building for member organizations. Contact: gaatw.org, gaatw@gaatw.org, +66 2 864 1427-8.",
        "source": "GAATW, 2024",
    },

    # ── La Strada International ──────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "EUROPE",
        "title": "La Strada International — European Anti-Trafficking Network",
        "summary": "La Strada International is a European NGO platform combating trafficking in human beings with member organizations in Belarus, Bosnia-Herzegovina, Bulgaria, Czech Republic, Moldova, North Macedonia, Netherlands, Poland, and Ukraine. Provides direct victim support, advocacy, and training. European office: The Hague. Contact: lastradainternational.org.",
        "source": "La Strada International, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "EUROPE",
        "title": "La Strada International — Preventing Trafficking of Migrant Workers in Agriculture in Europe",
        "summary": "La Strada's 2020 report documented exploitation of seasonal agricultural workers across EU member states, particularly in Germany, Netherlands, Spain, and Italy. Found seasonal workers from Romania, Bulgaria, Ukraine, and Morocco subjected to debt bondage via accommodation charges, restricted movement, and wage theft. Recommended EU-wide standards for seasonal worker accommodation and recruitment.",
        "source": "La Strada International, 2020",
    },

    # ── ECPAT ────────────────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "ECPAT International — Global Monitoring on Child Sexual Exploitation and Trafficking",
        "summary": "ECPAT International conducts monitoring of child trafficking and sexual exploitation across 48 countries. Its Country Status Reports assess legal frameworks, prosecution, victim identification, and survivor support. ECPAT's Child-Friendly Complaints Mechanism guidance has been adopted by 35 countries for child victims of trafficking. Contact: ecpat.org, Bangkok headquarters.",
        "source": "ECPAT International, 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "INTL",
        "title": "ECPAT — Disrupting Harm: Evidence on Online Child Sexual Exploitation and Abuse (2022)",
        "summary": "ECPAT's multi-country study found that online platforms are increasingly used for trafficking of minors for sexual exploitation. In six Asian countries studied (Cambodia, Indonesia, Malaysia, Nepal, Philippines, Vietnam), 13-54% of children who experienced sexual exploitation reported it occurred partly or entirely online. Platforms used included social media, dating apps, and live streaming services.",
        "source": "ECPAT, UNICEF, Interpol, 2022",
    },

    # ── USA: National Human Trafficking Hotline (Polaris) ──────────────────
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "National Human Trafficking Hotline — Polaris Project",
        "summary": "The National Human Trafficking Hotline (1-888-373-7888 / text 233733) operated by Polaris Project is available 24/7 in 200+ languages. Connects callers with local service providers, law enforcement, and emergency assistance. Between 2007 and 2023, the hotline received contacts about 73,000+ cases involving 196,000+ victims in the United States. Also available via chat at humantraffickinghotline.org.",
        "source": "Polaris Project, 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "Polaris Project — 2022 US Trafficking Data Report",
        "summary": "Polaris's 2022 annual data report found 10,360 trafficking situations reported to the National Hotline, involving 16,552 individual survivors. Labor trafficking comprised 43% of cases, sex trafficking 48%, and both forms 9%. Top industries for labor trafficking: domestic work, agriculture, landscaping, construction, and food services. Foreign nationals comprised 44% of labor trafficking survivors.",
        "source": "Polaris Project, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Polaris Project — Labor Trafficking in the US: A Closer Look at Temporary Work Visas (2015)",
        "summary": "Polaris analysis of 2,000+ labor trafficking cases found visa dependency among the most common control mechanisms. Traffickers exploit H-2A (agriculture), H-2B (non-agriculture seasonal), and J-1 (exchange visitor) visa holders by confiscating passports, threatening deportation, and imposing inflated debt for visa fees. Recommended visa portability reforms and expanded labor inspection authority.",
        "source": "Polaris Project, 2015",
    },
    {
        "type": "policy_update",
        "jurisdiction": "US",
        "title": "Polaris Project — Polaris Trafficking Assessment Tool for Businesses",
        "summary": "Polaris developed a corporate assessment tool to help businesses identify and respond to trafficking in their operations and supply chains. The tool covers supplier auditing, worker voice mechanisms, grievance procedures, and remediation. Adopted by companies in the hospitality, agriculture, and manufacturing sectors as part of corporate anti-trafficking pledges.",
        "source": "Polaris Project, 2022",
    },

    # ── USA: DOJ Human Trafficking Prosecution Unit ─────────────────────────
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "DOJ Civil Rights Division — Human Trafficking Prosecution Unit (HTPU)",
        "summary": "HTPU prosecutes federal trafficking violations under the Trafficking Victims Protection Act (TVPA). Comprises specialized prosecutors experienced in labor and sex trafficking cases. Coordinates with FBI, HSI, and local law enforcement. Victim-witness coordinators ensure survivors receive assistance throughout prosecution. Contact: justice.gov/crt/human-trafficking, 202-514-2151.",
        "source": "US DOJ, 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "DOJ HTPU — Labor Trafficking Prosecutions: Agricultural and Domestic Work Cases 2000-2023",
        "summary": "DOJ HTPU has secured over 2,000 federal trafficking convictions since TVPA enactment in 2000. Notable labor cases include prosecutions of domestic worker trafficking rings from the Philippines and Guatemala, agricultural forced labor operations in Florida and California, and restaurant worker debt bondage schemes targeting Thai and Chinese nationals. Maximum sentences have reached life imprisonment under TVPA.",
        "source": "US DOJ Annual Report, 2023",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US",
        "title": "DOJ — Final Rule: Protections for Trafficking Victims in Immigration Proceedings (2016)",
        "summary": "DOJ rule established that immigration judges must consider whether a respondent may be a trafficking victim before ordering removal. Requires immigration courts to apply non-criminalization principles: victims shall not be prosecuted for immigration violations directly resulting from their trafficking. Enhanced the T Visa and U Visa certification process for law enforcement to report victim cooperation.",
        "source": "US DOJ / DHS, 2016",
    },

    # ── USA: FBI Civil Rights Unit ───────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "FBI Civil Rights Unit — Human Trafficking Investigation Program",
        "summary": "The FBI's Civil Rights Unit investigates federal human trafficking violations with specialized agents in all 56 field offices. FBI Innocence Lost National Initiative focuses on domestic child sex trafficking and has recovered over 6,000 children since 2003. For reporting: tips.fbi.gov or 1-800-CALL-FBI. FBI also operates undercover operations targeting trafficking networks.",
        "source": "FBI, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "FBI — Labor Trafficking Indicators for Financial Investigators",
        "summary": "FBI advisory identifies financial red flags for labor trafficking operations: large cash deposits inconsistent with business type, rapid transfers to foreign accounts, multiple payroll accounts with same owner, workers cashing checks at same locations, and payments to unregistered labor contractors. Shared with FinCEN for bank compliance training programs.",
        "source": "FBI / FinCEN Advisory, 2020",
    },

    # ── USA: DHS Blue Campaign ───────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "DHS Blue Campaign — National Strategy to Combat Human Trafficking",
        "summary": "DHS Blue Campaign coordinates the department's anti-trafficking efforts across CBP, ICE/HSI, USCIS, and TSA. Blue Campaign's training has reached over 10 million people in the transportation, hospitality, and healthcare sectors. Free training at bluecampaign.dhs.gov. Provides victim identification toolkits, public awareness materials, and first-responder certification.",
        "source": "DHS Blue Campaign, 2024",
    },
    {
        "type": "policy_update",
        "jurisdiction": "US",
        "title": "DHS Blue Campaign — Forced Labor in Supply Chains: CBP Withhold-Release Orders",
        "summary": "DHS Customs and Border Protection (CBP) can issue Withhold-Release Orders (WROs) banning imports from specific producers where reasonable cause exists for forced labor. As of 2024, CBP has issued 62 WROs affecting goods from China, Mexico, Brazil, Malaysia, and other countries. Industries affected: polysilicon, seafood, cotton, tobacco, and rubber. WROs enforced at all US ports of entry.",
        "source": "DHS CBP, 2024",
    },

    # ── USA: Office for Victims of Crime ────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "Office for Victims of Crime (OVC) — Human Trafficking Capacity Building Center",
        "summary": "OVC's Human Trafficking Capacity Building Center provides training, technical assistance, and funding to organizations serving trafficking survivors. Operates OVC TTAC (Training and Technical Assistance Center). Funds 150+ Enhanced Collaborative Model task forces across the US. Contact: ovc.ojp.gov/program/human-trafficking, 1-800-851-3420.",
        "source": "US DOJ OVC, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "OVC — Trauma-Informed Care for Trafficking Survivors: Best Practices Guide",
        "summary": "OVC's guidance emphasizes that effective survivor services must be trauma-informed, culturally competent, and survivor-centered. Key principles: safety, trust, choice, collaboration, and empowerment. Providers should avoid re-traumatization through repeated interviews, avoid mandatory reporting requirements that deter help-seeking, and ensure access to legal status protections during recovery.",
        "source": "OVC, 2020",
    },

    # ── USA: CAST (Coalition to Abolish Slavery and Trafficking) ─────────────
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "Coalition to Abolish Slavery and Trafficking (CAST) — Los Angeles",
        "summary": "CAST provides comprehensive services to trafficking survivors in the Los Angeles area including legal aid, mental health services, shelter, workforce development, and survivor leadership programs. CAST's legal team has secured T visas, civil litigation recoveries, and criminal restitution for hundreds of survivors. Contact: castla.org, 213-365-1906. Serves all genders and trafficking types.",
        "source": "CAST LA, 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "CAST — Survivor Leader Program: Lived Experience in Policy Advocacy",
        "summary": "CAST's Survivor Leader program trains trafficking survivors to become advocates, public speakers, and policy consultants. Survivor leaders have testified before Congress, participated in federal rule-making processes, and contributed to California's anti-trafficking legislation. Model demonstrates value of survivor-centered policy development and peer support services.",
        "source": "CAST LA, 2022",
    },

    # ── USA: Shared Hope International ──────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Shared Hope International — Protected Innocence Challenge: State Report Cards 2023",
        "summary": "Shared Hope International annually evaluates all 50 US states on child sex trafficking laws across six categories: criminalization, criminal provisions, protection, prevention, prosecution tools, and continuum of care. In 2023, all 50 states received a 'pass' grade for the first time, reflecting significant legislative progress. Report cards guide state-level advocacy campaigns.",
        "source": "Shared Hope International, 2023",
    },
    {
        "type": "policy_update",
        "jurisdiction": "US",
        "title": "Shared Hope International — Demand Abolition Initiative",
        "summary": "Shared Hope's Demand Abolition initiative focuses on reducing the demand for commercial sexual exploitation of children by increasing prosecution of buyers. Has supported passage of 'buyer' statutes in 32 states increasing criminal penalties for purchasing sex with minors. Partners with local prosecutors' offices on case development and training.",
        "source": "Shared Hope International, 2022",
    },

    # ── USA: International Justice Mission (IJM) ────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "International Justice Mission (IJM) — Global Headquarters",
        "summary": "IJM is an international human rights organization with offices in 17 countries. Works with governments to strengthen law enforcement and justice systems to combat trafficking, forced labor, and sexual exploitation. IJM's public justice system reform approach has contributed to documented reductions in forced labor prevalence in target regions. Contact: ijm.org, 703-465-5495.",
        "source": "IJM, 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "INTL",
        "title": "IJM — Effectiveness of Justice System Strengthening in Reducing Forced Labor: Philippines Study",
        "summary": "IJM's randomized controlled evaluation in the Philippines found that communities with IJM justice system strengthening programs experienced a 76% reduction in commercial sexual exploitation of minors compared to control areas over five years. The study demonstrated that sustained engagement with police, prosecutors, and courts produces measurable protection outcomes.",
        "source": "IJM / Notre Dame JMRI, 2019",
    },

    # ── USA: Free the Slaves ─────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Free the Slaves — Community-Based Liberation Approach to Forced Labor",
        "summary": "Free the Slaves implements community-based anti-slavery programs in India, Congo, Ghana, Nepal, and other high-prevalence countries. Their liberation model focuses on community vigilance groups, economic alternatives, and survivor support rather than criminal prosecution alone. Research shows community mobilization reduces forced labor vulnerability by 70% in program areas.",
        "source": "Free the Slaves, 2022",
    },
    {
        "type": "statistic",
        "jurisdiction": "INTL",
        "title": "Free the Slaves — The Congo Report: Slavery and Sexual Violence in the Mining Sector",
        "summary": "Free the Slaves documented forced labor and sexual slavery in artisanal mining in eastern Congo, finding 75% of conflict minerals production zones had documented forced labor indicators. Report contributed to US Dodd-Frank Section 1502 conflict minerals disclosure requirements and subsequent EU Conflict Minerals Regulation. Evidence basis for supply chain due diligence advocacy.",
        "source": "Free the Slaves, 2011",
    },

    # ── USA: T'ruah ──────────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "T'ruah — Rabbis and Cantors Against Trafficking: Faith Community Engagement",
        "summary": "T'ruah mobilizes Jewish clergy and communities to combat human trafficking through education, advocacy, and direct service partnerships. Has engaged over 2,000 rabbis and cantors in anti-trafficking campaigns, trained 500+ Jewish institutions on survivor-centered responses, and advocates for asylum seeker and migrant worker protections. Partners with CAST, Polaris, and Hebrew Immigrant Aid Society (HIAS).",
        "source": "T'ruah, 2023",
    },

    # ── USA: National Survivor Network ──────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "National Survivor Network — Policy Priorities Platform for Trafficking Survivors",
        "summary": "The National Survivor Network (NSN) is a survivor-led organization with 2,000+ survivor members that advocates for policies centering survivor voices. NSN's policy platform includes: vacatur of trafficking-related convictions, expanded housing and benefits access for survivors, immigration relief for survivor-witnesses, and meaningful survivor inclusion in anti-trafficking policy-making at all levels of government.",
        "source": "National Survivor Network, 2023",
    },

    # ── UK: Anti-Slavery International ──────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "UK",
        "title": "Anti-Slavery International — London",
        "summary": "Founded in 1839, Anti-Slavery International is the world's oldest human rights organization. Works globally on forced labor, child slavery, descent-based slavery, and forced marriage through research, advocacy, and partner support. Contact: antislavery.org, +44 20 7501 8920. Operates programs in Mauritania, Ghana, India, Brazil, Morocco, and Europe.",
        "source": "Anti-Slavery International, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Anti-Slavery International — Putting People First: Report on Survivor Support Failures",
        "summary": "Anti-Slavery International's 2023 report found that trafficking survivors in 12 countries routinely face re-traumatization through law enforcement encounters, immigration detention, and inadequate support services. Found 68% of interviewed survivors were detained by immigration authorities at some point after trafficking. Recommended decriminalization of survivors' immigration violations and unconditional access to support.",
        "source": "Anti-Slavery International, 2023",
    },

    # ── UK: Kalayaan ─────────────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "UK",
        "title": "Kalayaan — Migrant Domestic Workers' Rights Organization, London",
        "summary": "Kalayaan advocates for and supports migrant domestic workers in the UK, particularly those on the tied Overseas Domestic Worker visa. Documents exploitation, provides legal advice, and campaigns for visa reforms. Contact: kalayaan.org.uk, +44 20 7243 2942. Has supported over 14,000 domestic workers since 1987, documenting systematic wage theft, document confiscation, and isolation.",
        "source": "Kalayaan, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "Kalayaan — Tied and Vulnerable: Impact of the Tied Overseas Domestic Worker Visa on Migrant Workers (2022)",
        "summary": "Kalayaan's 2022 analysis found 68% of domestic workers registering with them reported not being allowed outside alone, 56% reported not being paid, and 30% reported being physically abused. Workers on the tied ODW visa face deportation if they leave abusive employers. Kalayaan advocates for return to the pre-2012 visa model that allowed workers to change employers.",
        "source": "Kalayaan, 2022",
    },

    # ── UK: GLAA (Gangmasters and Labour Abuse Authority) ───────────────────
    {
        "type": "contact",
        "jurisdiction": "UK",
        "title": "Gangmasters and Labour Abuse Authority (GLAA) — Reporting Line",
        "summary": "GLAA is the UK regulator and law enforcement agency combating labor exploitation in agriculture, horticulture, shellfish gathering, and associated processing and packaging. Licensing authority for labor providers in those sectors. Report labor abuse at gla.gov.uk or call 0800 432 0804. GLAA officers investigate labor trafficking, forced labor, and exploitation across the UK.",
        "source": "GLAA, 2024",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "UK",
        "title": "GLAA — Statutory Code of Practice for Responsible Recruitment (2023)",
        "summary": "Following consultation, GLAA issued a statutory code requiring licensed gangmasters to follow ethical recruitment practices including no worker-paid fees, transparent contracts in workers' languages, and access to accommodation not tied to employment. Violators face license revocation. Code covers an estimated 50,000 seasonal agricultural workers in the UK.",
        "source": "GLAA / UK Department for Business, 2023",
    },

    # ── UK: The Salvation Army ───────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "UK",
        "title": "The Salvation Army — UK Modern Slavery Victim Care Contract",
        "summary": "The Salvation Army holds the UK government contract to provide support to adult victims of modern slavery identified through the National Referral Mechanism (NRM). Services include safe accommodation, financial support, legal advice, counseling, and access to health services for up to 45 days (extendable). Contact: modern.slavery@salvationarmy.org.uk, 0300 303 8151.",
        "source": "The Salvation Army, 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "UK",
        "title": "Salvation Army — NRM Victim Support Statistics 2022-2023",
        "summary": "In 2022-23, The Salvation Army supported 4,731 potential modern slavery victims through the UK NRM contract. 58% were victims of labor exploitation, 28% sexual exploitation, and 14% other forms. Top nationalities: Albanian, Eritrean, Vietnamese, Indian, and Nigerian. Average support duration was 64 days. 92% of service users reported feeling safer after receiving support.",
        "source": "The Salvation Army, 2023",
    },

    # ── UK: Unseen ───────────────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "UK",
        "title": "Unseen — UK Modern Slavery Helpline",
        "summary": "Unseen operates the Modern Slavery Helpline (08000 121 700), a 24/7 confidential resource for reporting modern slavery concerns in the UK. Also provides support and advice to potential victims. In 2023, the helpline received 8,000+ contacts. Unseen also provides safe houses in the southwest of England and corporate training through its business services arm.",
        "source": "Unseen, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "Unseen — Modern Slavery and UK Businesses: Transparency in Supply Chains Report 2023",
        "summary": "Unseen's analysis of UK business compliance with Modern Slavery Act Section 54 transparency requirements found 40% of large companies still produce non-compliant statements. Common failures: no risk assessment methodology, no due diligence actions, and no measurable key performance indicators. Recommended mandatory format requirements and financial penalties for non-compliance.",
        "source": "Unseen, 2023",
    },

    # ── UK: Hope for Justice ─────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "UK",
        "title": "Hope for Justice — UK and International Programs",
        "summary": "Hope for Justice operates trafficking identification, rescue, and survivor support services in the UK, Norway, Uganda, Cambodia, and other countries. Their Lighthouse safe houses provide long-term specialist accommodation. Beacon program offers therapeutic support and advocacy. Contact: hopeforjustice.org, +44 300 008 8000. Also provides corporate training and investigative services.",
        "source": "Hope for Justice, 2024",
    },

    # ── UK: ECPAT UK ─────────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "ECPAT UK — Heading Back to Harm: Young People Trafficked to and within the UK",
        "summary": "ECPAT UK's research found that unaccompanied asylum-seeking children are at high risk of trafficking after going missing from local authority care. Found 69% of children suspected of trafficking had gone missing at least once while in care. Recommended mandatory trafficking assessments for all missing unaccompanied children and specialized foster care placements.",
        "source": "ECPAT UK, 2018",
    },
    {
        "type": "policy_update",
        "jurisdiction": "UK",
        "title": "ECPAT UK — Child Trafficking Advocates Program",
        "summary": "ECPAT UK's Child Trafficking Advocates scheme provides independent advocates to child trafficking victims in the UK NRM process. Advocates ensure children's voices are heard in welfare decisions and NRM assessments, provide information about rights, and support access to services. Program expanded to cover all 10 regions of England following successful pilot evaluation.",
        "source": "ECPAT UK, 2022",
    },

    # ── Europe: KOK Germany ─────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "DE",
        "title": "KOK — German NGO Network Against Trafficking in Human Beings",
        "summary": "KOK (Bundesweiter Koordinierungskreis gegen Menschenhandel) is a nationwide network of 45 counseling centers and NGOs in Germany combating trafficking for sexual exploitation and forced labor. Provides nationwide counseling center finder at kok-gegen-menschenhandel.de. KOK advocates for victim-centered NRM reform, access to welfare benefits for trafficking survivors, and decriminalization of migration.",
        "source": "KOK, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "DE",
        "title": "KOK — Labor Trafficking in Germany: Agricultural and Domestic Work Sectors",
        "summary": "KOK's 2021 report documented forced labor in German agriculture, particularly affecting Romanian and Bulgarian seasonal workers, and domestic worker exploitation through au pair and live-in care worker arrangements. Found enforcement gaps: labor inspectors rarely investigate private households, and undocumented domestic workers fear deportation. Recommended expanded labor inspection authority and sector-specific awareness campaigns.",
        "source": "KOK, 2021",
    },

    # ── Europe: CoMensha Netherlands ────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "NL",
        "title": "CoMensha — Netherlands Coordination Centre for Human Trafficking",
        "summary": "CoMensha is the Dutch registration center for trafficking victims, coordinating bed, bath, and bread facilities for identified trafficking survivors. Maintains national trafficking statistics, provides professional training, and coordinates with Stichting KOMPAS and other service providers. Contact: comensha.nl, +31 33 448 1186. Reports annually to the Dutch National Rapporteur.",
        "source": "CoMensha, 2024",
    },

    # ── Europe: GRETA ───────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "EUROPE",
        "title": "GRETA — Group of Experts on Action against Trafficking in Human Beings (Council of Europe)",
        "summary": "GRETA monitors implementation of the Council of Europe Convention on Action against Trafficking in Human Beings (ECAT) by 46 member states. Country evaluation reports assess legal frameworks, victim identification, NRM functioning, compensation, and prosecution. GRETA's Third Evaluation Round (2020-2025) focuses on trafficking in conflict, online trafficking, and climate-related displacement.",
        "source": "Council of Europe / GRETA, 2024",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EUROPE",
        "title": "GRETA — Recommendation on Non-Punishment of Trafficking Victims",
        "summary": "GRETA's 2024 thematic report found only 28 of 46 ECAT member states have explicit legal non-punishment clauses for trafficking victims. GRETA recommended all states enact explicit non-prosecution provisions, train prosecutors on victim identification, and establish presumption of victim status for individuals charged with offenses commonly associated with trafficking exploitation.",
        "source": "GRETA, 2024",
    },

    # ── Europe: Caritas ─────────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "EUROPE",
        "title": "Caritas Internationalis — Anti-Trafficking Network",
        "summary": "Caritas operates anti-trafficking programs through its 162 national member organizations. Programs include prevention in origin communities, victim support, legal aid, shelter, and reintegration. Active in Philippines, Bangladesh, Ethiopia, Nigeria, Ukraine, and many EU countries. Caritas's BE AWARE global campaign (2015-2025) has reached 10 million people with trafficking awareness messaging.",
        "source": "Caritas Internationalis, 2024",
    },

    # ── Europe: ASTRA Serbia ─────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "RS",
        "title": "ASTRA — Anti-Trafficking Action, Serbia",
        "summary": "ASTRA operates Serbia's primary SOS hotline for trafficking victims (0800 100 600, 24/7, free) and provides comprehensive survivor support including counseling, legal aid, and reintegration assistance. ASTRA research documents trafficking patterns in the Western Balkans route and advocates for victim compensation funds and legal aid access. Contact: astra.rs.",
        "source": "ASTRA, 2024",
    },

    # ── Asia: GAATW Bangkok / MAP Foundation Thailand ──────────────────────
    {
        "type": "advisory",
        "jurisdiction": "TH",
        "title": "MAP Foundation — Migrant Workers' Rights Organization, Chiang Mai",
        "summary": "MAP Foundation provides legal aid, shelter, and advocacy for migrant workers from Myanmar, Cambodia, and Laos in northern Thailand. Documents exploitation in agriculture, construction, and fisheries. Has assisted over 50,000 migrant workers since 1996. Operates Migrant Workers Assistance Center providing rights information and complaint referral in Thai, Burmese, and Shan languages.",
        "source": "MAP Foundation, 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "MAP Foundation — Fishing Industry Labour Rights in Thailand: Documentation 2014-2020",
        "summary": "MAP Foundation's multi-year documentation of Thai fishing industry found widespread forced labor indicators including debt bondage, restriction of movement at sea, physical violence, and non-payment of wages affecting primarily Burmese, Cambodian, and Lao workers. Findings contributed to Thai government reforms including the Seafood Task Force and GPS monitoring of fishing vessels.",
        "source": "MAP Foundation, 2020",
    },

    # ── Asia: Tenaganita Malaysia ────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "MY",
        "title": "Tenaganita — Migrant Worker and Trafficking Support, Malaysia",
        "summary": "Tenaganita is Malaysia's leading migrant worker rights NGO, providing legal aid, shelter, advocacy, and documentation for exploitation victims. Operates migrant worker resource centers and a trafficking survivor safe house. Documents systematic exploitation in electronics, palm oil, construction, and domestic work sectors. Contact: tenaganita.net, +60 3-7784 3525.",
        "source": "Tenaganita, 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Tenaganita — Migrant Worker Exploitation in Malaysian Palm Oil: Systematic Documentation (2019-2023)",
        "summary": "Tenaganita's multi-year research found forced labor indicators in palm oil plantations affecting Bangladeshi, Indonesian, and Nepali workers including debt bondage from recruitment fees of USD 2,000-5,000, passport confiscation, substandard housing tied to employment, and wage theft through inflated deductions. Evidence contributed to US CBP Withhold-Release Orders on palm oil from major Malaysian producers.",
        "source": "Tenaganita, 2023",
    },

    # ── Asia: Migrant CARE Indonesia ────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "ID",
        "title": "Migrant CARE — Indonesian Migrant Worker Advocacy Network",
        "summary": "Migrant CARE is Indonesia's leading migrant worker advocacy coalition, coordinating 50+ civil society organizations. Operates migrant service centers in major origin provinces and at Soekarno-Hatta airport. Conducts policy advocacy, legal aid, and reintegration support. Contact: migrantcare.net, +62 21 788 42580. Documents exploitation of Indonesian workers in Malaysia, Saudi Arabia, Singapore, and Taiwan.",
        "source": "Migrant CARE, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "ID",
        "title": "Migrant CARE — Indonesia's Moratorium on Sending Domestic Workers to Middle East: Assessment",
        "summary": "Migrant CARE's 2023 evaluation of Indonesia's intermittent moratoriums on sending domestic workers to Middle Eastern countries found moratoriums pushed workers into irregular channels without protection. Recommended replacing moratoriums with mandatory bilateral agreements including specific labor standards, pre-departure orientation, and post-arrival monitoring by Indonesian labor attaches.",
        "source": "Migrant CARE, 2023",
    },

    # ── Asia: MFMW Hong Kong ─────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Mission for Migrant Workers (MFMW) — Hong Kong",
        "summary": "MFMW provides shelter, legal aid, counseling, and advocacy for migrant domestic workers in Hong Kong since 1981. Walk-in service center in Central, HK. Operates a shelter for workers fleeing abuse. Documents wage theft, passport confiscation, and illegal confinement. Contact: mfmw.org, +852 2522 8264. Conducts annual survey on exploitation patterns affecting Filipino and Indonesian workers.",
        "source": "MFMW Hong Kong, 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "MFMW — Annual Survey on Migrant Domestic Worker Exploitation in Hong Kong 2023",
        "summary": "MFMW's 2023 survey of 2,500 migrant domestic workers in Hong Kong found 23% experienced salary underpayment, 18% reported passport confiscation, 15% reported being refused rest days, and 8% reported physical abuse. 41% reported not receiving food or living allowance as required by law. Only 12% knew how to file a complaint with the Labour Department.",
        "source": "MFMW, 2023",
    },

    # ── Asia: National Commission for Women India ────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "IN",
        "title": "National Commission for Women (NCW) — Anti-Trafficking Cell, India",
        "summary": "NCW's Anti-Trafficking Cell receives complaints, monitors rehabilitation of trafficking survivors, and coordinates with state governments and NGOs. NCW conducts awareness campaigns in high-trafficking origin states (West Bengal, Assam, Odisha, Bihar, Jharkhand). For complaints: ncw.nic.in/complaint, 7827170170. NCW has reviewed over 1,000 trafficking cases since 2000.",
        "source": "NCW India, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "IN",
        "title": "NCW India — Trafficking of Women and Girls in India: Comprehensive Study (2020)",
        "summary": "NCW's 2020 comprehensive study found trafficking for sexual exploitation and domestic labor concentrated in inter-state routes from West Bengal, Odisha, Bihar, and Jharkhand to Delhi, Mumbai, and Goa. Found 68% of survivors had no access to education before trafficking. Recommended integration of anti-trafficking programs into school curricula and community-based prevention programs in origin districts.",
        "source": "NCW India, 2020",
    },

    # ── Asia: POEA / DMW Philippines ─────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "Department of Migrant Workers (DMW) / POEA — Philippines Illegal Recruitment Hotline",
        "summary": "DMW (formerly POEA) regulates overseas employment from the Philippines and prosecutes illegal recruitment. Report illegal recruiters at dmw.gov.ph/report, 8722-1144, or through POLO offices in 34 countries. DMW maintains a blacklist of banned agencies. Illegal recruitment can carry life imprisonment under Republic Act 8042 as amended by RA 10022.",
        "source": "DMW Philippines, 2024",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW — Mandatory Pre-Departure Orientation Seminar (PDOS) for OFWs",
        "summary": "All overseas Filipino workers must complete a Pre-Departure Orientation Seminar covering: worker rights in destination countries, Philippine laws on illegal recruitment and trafficking, emergency contact procedures, and remittance management. PDOS includes destination-specific information and anti-trafficking indicators. Administered at POLO offices and accredited providers in 34 countries.",
        "source": "DMW Philippines, 2023",
    },

    # ── Africa: NAPTIP Nigeria ───────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "NG",
        "title": "National Agency for the Prohibition of Trafficking in Persons (NAPTIP) — Nigeria",
        "summary": "NAPTIP is Nigeria's primary counter-trafficking agency with offices in 15 states. Investigates and prosecutes trafficking cases, rescues victims, and provides shelter and rehabilitation. NAPTIP hotline: 0800-NAPTIP-1 (0800-627847-1). Since 2003, NAPTIP has prosecuted over 3,000 trafficking cases and rescued 19,000+ victims. Operates reintegration centers in Lagos, Benin City, and other states.",
        "source": "NAPTIP Nigeria, 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "NG",
        "title": "NAPTIP — Annual Report on Trafficking Patterns in Nigeria 2022",
        "summary": "NAPTIP's 2022 annual report recorded 1,247 suspected trafficking cases, 893 prosecutions, and 312 convictions. Primary destination countries for Nigerian trafficking victims: Libya, Italy, Spain, Germany, United Kingdom, and Saudi Arabia. Internal trafficking (Edo to Lagos) also documented. Root causes identified: poverty, lack of education, family pressure, and fraudulent recruitment.",
        "source": "NAPTIP, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "NG",
        "title": "NAPTIP — Edo State Anti-Trafficking Initiative: Origin Community Prevention",
        "summary": "NAPTIP partnered with Edo State government on the Edo State Task Force on Human Trafficking, targeting Benin City and surrounding communities that are major origin areas for Nigerian trafficking victims in Europe. Community sensitization, school programs, and 'returnee' support programs reduced first-time irregular departures by an estimated 30% over three years according to IOM monitoring data.",
        "source": "NAPTIP / IOM, 2022",
    },

    # ── Africa: Terre des Hommes ─────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "INTL",
        "title": "Terre des Hommes — Child Trafficking Prevention International",
        "summary": "Terre des Hommes (TdH) works in 40 countries to prevent child trafficking and protect child rights. Programs focus on origin community prevention, school-based awareness, legal aid for child survivors, and policy advocacy. TdH operates ECPAT-affiliate programs in West Africa, Southeast Asia, and Eastern Europe. Contact: terredeshommes.org, +41 21 654 6666.",
        "source": "Terre des Hommes, 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "INTL",
        "title": "Terre des Hommes — Child Trafficking in West Africa: Conakry Process and Ouagadougou Action Plan Assessment",
        "summary": "TdH's assessment of the Ouagadougou Action Plan (2006-2023) against trafficking and smuggling of migrants in West Africa found improved bilateral cooperation but persistent gaps in victim identification, child-specific referral pathways, and reintegration support. Recommended dedicated child protection funds within bilateral labor agreements and mandatory child trafficking screening at border crossings.",
        "source": "Terre des Hommes / Conakry Process, 2023",
    },

    # ── Africa: HAART Kenya ──────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "KE",
        "title": "HAART Kenya — Awareness Against Human Trafficking",
        "summary": "HAART Kenya provides survivor support, prevention education, and policy advocacy on human trafficking. Programs target Kenyan workers trafficked to Gulf states, domestic worker exploitation in Nairobi, and internal trafficking of minors. Contact: haartkenya.org, +254 20 232 3404. HAART operates Kenya's primary trafficking survivor safe house and provides psychosocial support and legal aid.",
        "source": "HAART Kenya, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "KE",
        "title": "HAART Kenya — Domestic Worker Exploitation in Gulf States: Kenyan Cases (2019-2023)",
        "summary": "HAART documented over 400 cases of Kenyan domestic workers trafficked to Saudi Arabia, Kuwait, and UAE during 2019-2023. Common patterns: recruitment through informal networks, false job promises, confiscated documents on arrival, and physical abuse. HAART's advocacy contributed to Kenya's enhanced bilateral agreements requiring employer background checks and mandatory insurance for domestic workers.",
        "source": "HAART Kenya, 2023",
    },

    # ── Americas: CDM Mexico ─────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "MX",
        "title": "Centro de los Derechos del Migrante (CDM) — Migrant Rights Center, Mexico/USA",
        "summary": "CDM is a binational organization (Mexico City and Baltimore offices) that provides legal services to Mexican migrant workers in the United States. Documents labor trafficking and exploitation in H-2 visa programs, advocates for visa portability reforms, and files complaints with US DOL and NLRB. Contact: cdmigrante.org, +1 410 783 0236 (Baltimore), +52 55 5207 3640 (Mexico City).",
        "source": "CDM, 2024",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "CDM — Unseen Workers: H-2 Visa Program Abuses in US Agriculture and Forestry (2023)",
        "summary": "CDM's investigation of H-2A and H-2B visa workers found systemic employer violations including overcrowded housing, illegal deductions for transportation and tools, passport withholding, and blacklisting of workers who complain. Found that the visa's employer-tied structure gives employers near-total control. Recommended worker-portable visas, expanded DOL enforcement, and anonymous complaint mechanisms.",
        "source": "CDM, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "MX",
        "title": "CDM — Fuerza Migrante: Worker-Led Anti-Trafficking Monitoring in Mexican Communities",
        "summary": "CDM's Fuerza Migrante initiative trains returned Mexican migrant workers as community monitors to identify fraudulent job offers, illegal fee collection, and trafficking indicators in origin communities. Monitors report to CDM's legal team and Mexican SENATP (National Anti-Trafficking System). Program active in Hidalgo, Tlaxcala, Puebla, and Oaxaca states, covering over 50,000 people.",
        "source": "CDM, 2022",
    },

    # ── Americas: Verité ─────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Verité — Strengthening Protections Against Trafficking in Persons in Federal and Corporate Supply Chains",
        "summary": "Verité conducted the first comprehensive research on trafficking risk in US government and Fortune 500 supply chains. Found labor trafficking indicators in US federal procurement supply chains for electronics, textiles, and food. Research led to Executive Order 13627 (2012) on Strengthening Protections Against Trafficking in Persons in Federal Contracts and subsequent FAR rule.",
        "source": "Verité, 2012",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Verité — Commodity Atlas: Labor Rights Risk in Global Supply Chains",
        "summary": "Verité's Commodity Atlas maps forced labor and child labor risks across 43 commodities in 130 countries based on government data, research literature, and original fieldwork. High-risk commodities include electronics from Malaysia and China, palm oil from Indonesia and Malaysia, shrimp from Thailand, and garments from Bangladesh and Cambodia. Available at verite.org/commodity-atlas.",
        "source": "Verité, 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Verité — Labor Conditions in Malaysia's Electronics Industry: Forced Labor Risk Assessment",
        "summary": "Verité's landmark 2014 assessment of Malaysian electronics supply chains found 28% of electronics workers surveyed showed indicators of forced labor, with migrant workers significantly more at risk. Practices included recruitment fee debt (USD 800-2,000), passport confiscation (32%), and threat of deportation as control mechanism. Report contributed to major brand supplier code reforms and Malaysian government action.",
        "source": "Verité, 2014",
    },

    # ── Americas: Global Fund to End Modern Slavery (GFEMS) ─────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Global Fund to End Modern Slavery (GFEMS) — Evidence-Based Anti-Trafficking Programs",
        "summary": "GFEMS (funded by US Congress) invests in evidence-based programs to reduce prevalence of modern slavery in high-burden countries. Grant portfolio covers labor migration reform in Nepal and Bangladesh, survivor support in Philippines and Vietnam, financial inclusion in India, and law enforcement training in Nigeria and Southeast Asia. Evidence standards require rigorous impact evaluation.",
        "source": "GFEMS, 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "INTL",
        "title": "GFEMS — What Works to Combat Modern Slavery: Portfolio Evidence Review 2024",
        "summary": "GFEMS's 2024 evidence review of 47 anti-trafficking interventions found strongest evidence for: worker-pays fee elimination programs (labor trafficking), economic empowerment combined with awareness (prevention), and integrated survivor support with legal services (recovery). Weakest evidence for: awareness-only campaigns, prosecution-focused interventions without survivor support, and supply chain auditing alone.",
        "source": "GFEMS, 2024",
    },

    # ── Cross-cutting: Hotlines and Referral Networks ───────────────────────
    {
        "type": "contact",
        "jurisdiction": "AU",
        "title": "Australian Federal Police — National Policing Support for Trafficking",
        "summary": "AFP's Human Trafficking Team investigates human trafficking and slavery offenses. Report trafficking at afp.gov.au/humantrafficking or 131 AFP. AFP coordinates with the Support for Trafficked People Program (STPP) operated by Australian Red Cross. Trafficking hotline available 24/7. AFP has offices in Southeast Asia and Pacific to address trafficking at origin.",
        "source": "AFP Australia, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "CA",
        "title": "Canadian Centre to End Human Trafficking — Canadian Human Trafficking Hotline",
        "summary": "The Canadian Human Trafficking Hotline (1-833-900-1010) operated by the Canadian Centre to End Human Trafficking provides 24/7 multilingual support, safety planning, and referrals to local services. Available in 200 languages. The Centre also provides training for healthcare workers, transportation workers, and educators. Contact: canadiancentretoendhumantrafficking.ca.",
        "source": "Canadian Centre to End Human Trafficking, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "EU",
        "title": "European Anti-Trafficking Coordinator — EU Strategy Against Trafficking 2021-2025",
        "summary": "The European Commission's anti-trafficking strategy focuses on prevention, victim identification, prosecution, and international cooperation. The EU Anti-Trafficking Coordinator monitors implementation across 27 member states. EU emergency number for trafficking reports: 116 006 (victim support). Strategy includes Europol's Joint Investigation Teams for cross-border trafficking networks.",
        "source": "European Commission, 2021",
    },
    {
        "type": "contact",
        "jurisdiction": "ZA",
        "title": "South Africa Counter-Trafficking in Persons Resources — National Hotline",
        "summary": "The South African Department of Social Development coordinates counter-trafficking resources. Report trafficking at the National Human Trafficking Hotline: 0800 222 777 (24/7, free). The Salvation Army South Africa and SAPS Family Violence, Child Protection, and Sexual Offences (FCS) units co-respond to trafficking cases. National Prosecuting Authority has dedicated trafficking prosecutors.",
        "source": "South Africa DSD / SAPS, 2024",
    },

    # ── Cross-cutting: Research and Advocacy Organizations ──────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Humanity United — Philanthropic Strategy to End Human Trafficking",
        "summary": "Humanity United funds anti-trafficking organizations, policy advocacy, and research globally. Focus areas: labor migration reform, supply chain accountability, survivor leadership, and technology innovation. Grantees include Verité, Polaris, IJM, GAATW, and CDM. Humanity United's labor migration work has contributed to fee elimination policies affecting an estimated 10 million workers.",
        "source": "Humanity United, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Liberty Asia — Legal and Digital Tools Against Human Trafficking in Asia",
        "summary": "Liberty Asia provides legal and technology tools to combat trafficking in Southeast and South Asia. Programs include trafficking legal database (StopTheTraffik), supply chain risk screening tools, and legal aid for survivors. Partners with major companies on supply chain due diligence in Thailand, Cambodia, and Malaysia. Contact: libertyasia.org.",
        "source": "Liberty Asia, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Winrock International — Trafficking Survivor Support and Workforce Development",
        "summary": "Winrock International implements USAID and USDOL-funded counter-trafficking programs in Cambodia, Vietnam, Laos, and Nepal. Programs combine survivor support with livelihood training, worker rights education, and community prevention. Winrock's signature work-based learning approach integrates labor rights into vocational training for at-risk workers.",
        "source": "Winrock International, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Solidarity Center (AFL-CIO) — Migrant Worker Rights and Anti-Trafficking Programs",
        "summary": "Solidarity Center, the AFL-CIO's international arm, supports workers' rights organizations and trade unions that combat trafficking and forced labor. Active in 60+ countries. Programs focus on organizing domestic workers, seafarers, and agricultural workers. Has trained 100,000+ union leaders on identifying trafficking indicators. Contact: solidaritycenter.org.",
        "source": "Solidarity Center, 2024",
    },

    # ── Cross-cutting: International Policy Frameworks ───────────────────────
    {
        "type": "law",
        "jurisdiction": "INTL",
        "title": "UN Trafficking in Persons Protocol (Palermo Protocol) — Article 6: Assistance and Protection for Victims",
        "summary": "Article 6 of the Palermo Protocol (2000) requires states to ensure the physical, psychological, and social recovery of trafficking victims. Measures include appropriate housing, counseling, legal information, medical assistance, and employment/educational opportunities. 180+ states have ratified the Protocol, making victim protection an international legal obligation.",
        "source": "UNODC / UNGA, 2000",
    },
    {
        "type": "law",
        "jurisdiction": "INTL",
        "title": "ILO Forced Labour Protocol (P029) 2014 — Victim Protection and Compensation Requirements",
        "summary": "The 2014 Protocol to ILO Convention No. 29 on Forced Labour requires states to protect victims from prosecution for unlawful acts committed as a direct result of forced labor, provide access to remedies including compensation, and offer rehabilitation and social integration. By 2024, 60 states have ratified P029. Implementing states must develop national action plans.",
        "source": "ILO, 2014",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Directive 2011/36/EU — Minimum Standards on Victim Support",
        "summary": "The EU Anti-Trafficking Directive establishes minimum standards for victim support across all 27 member states: unconditional assistance regardless of cooperation with authorities, reflection and recovery period, legal residency during proceedings, free legal counsel, access to compensation, and specific measures for child victims. Member states must transpose all provisions into national law.",
        "source": "European Parliament and Council, 2011",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "EU Corporate Sustainability Due Diligence Directive (CS3D) — Forced Labor Provisions (2024)",
        "summary": "The EU CS3D (Directive 2024/1760) requires companies with 1,000+ employees and EUR 450M+ turnover to conduct human rights due diligence across their value chains, including identifying and addressing forced labor and trafficking risks. Companies must have grievance mechanisms, remediation plans, and civil liability for harm. Anti-trafficking organizations recognized as qualified entities to file complaints.",
        "source": "European Parliament and Council, 2024",
    },

    # ── Cross-cutting: Survivor-Led Organizations ────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "ARISE — Advocates for Survivors of Labor Trafficking and Exploitation",
        "summary": "ARISE is a survivor-led advocacy organization focused specifically on labor trafficking survivors. Develops policy recommendations on T visa processing delays, restitution enforcement, labor law remedies, and survivor-centered service models. Participates in federal advisory processes and trains legal practitioners. Emphasizes labor rights framework over criminal justice approach.",
        "source": "ARISE, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Global Modern Slavery Directory — First Survivor-Curated Resource Hub (2023)",
        "summary": "The Global Modern Slavery Directory (globalmodernslavery.org) is the first survivor-curated database of 2,000+ anti-trafficking organizations, hotlines, and legal resources worldwide. Compiled with survivor input to ensure relevance and accuracy. Searchable by country, service type (legal aid, shelter, hotline, advocacy), and population served. Free access for service providers and survivors.",
        "source": "Global Modern Slavery Directory, 2023",
    },

    # ── Cross-cutting: Healthcare and Identification ─────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Dignity Health — HEAL Trafficking Protocol for Healthcare Providers",
        "summary": "HEAL Trafficking (Health, Education, Advocacy, Linkage) developed evidence-based clinical protocols for healthcare providers to identify and respond to trafficking victims. Protocol covers trauma-informed intake, privacy protections, mandatory reporting considerations, and referral pathways. Adopted by 300+ hospitals across the United States. Free training at healtrafficking.org.",
        "source": "HEAL Trafficking, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "WHO — Health Sector Response to Human Trafficking: Clinical Guidelines (2023)",
        "summary": "WHO's 2023 guidelines for health workers provide standardized protocols for identifying trafficking victims in healthcare settings, conducting trauma-informed assessments, managing health consequences including reproductive health, mental health, and occupational injuries, and making safe referrals. Emphasizes patient confidentiality and non-judgmental care regardless of immigration status.",
        "source": "WHO, 2023",
    },

    # ── Cross-cutting: Corporate and Financial Sector ────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "UN Global Compact — Business Against Trafficking Initiative",
        "summary": "The UN Global Compact's Business Against Trafficking initiative engages companies in preventing trafficking through supply chain due diligence, worker recruitment reform, and survivor employment programs. 400+ companies have signed the initiative's principles. Provides practical tools including self-assessment checklists, supplier code of conduct templates, and migrant worker fee reimbursement program models.",
        "source": "UN Global Compact, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Luxor Protocol — Preventing Sex Trafficking in the Tourism Sector (2018)",
        "summary": "The Luxor Implementation Guidelines to the Athens Ethical Principles provide the hospitality sector with specific protocols to combat trafficking including staff training, procurement standards, customer reporting mechanisms, and engagement with local anti-trafficking organizations. Adopted by 500+ hotels across 60 countries. ECPAT's Code (The Code) hotels implement similar child protection standards.",
        "source": "Luxor Protocol / ECPAT, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Issara Institute — Worker Voice Tools for Labor Trafficking Prevention in Asia",
        "summary": "Issara Institute's Golden Gate worker voice platform enables migrant workers in Thailand, Myanmar, Bangladesh, and India to report labor violations confidentially via hotline, SMS, and mobile app. Platform has collected 20,000+ worker contacts since 2014, identifying patterns of debt bondage, document confiscation, and wage theft at factory and farm level. Data shared with brand customers for remediation.",
        "source": "Issara Institute, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "FinCEN — Financial Crimes Enforcement Network: Guidance on Identifying Human Trafficking (2014, updated 2021)",
        "summary": "FinCEN issued guidance to US financial institutions on suspicious activity reporting related to human trafficking. Key red flags: bulk cash payments to businesses not normally cash-intensive, wire transfers to high-prevalence trafficking countries, hotel and motel charges with associated escort services, and labor contractors paying workers by cash without payroll records. Banks must file SARs for suspected trafficking-related transactions.",
        "source": "FinCEN / US Treasury, 2021",
    },

    # ── Additional USA Organizations ─────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "Los Angeles County HART (Human Anti-Trafficking Response Team) — Multi-Agency Task Force",
        "summary": "Los Angeles HART is a multi-agency anti-trafficking task force coordinating LAPD, LASD, LA County Probation, OVC-funded service providers, and DA's office. Provides 24/7 victim services through CAST LA, represents the model Enhanced Collaborative Model task force. Since 2017, HART has identified 1,200+ trafficking victims and served 800+ survivors with comprehensive services.",
        "source": "LA County HART, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "Covenant House — Youth Trafficking Services Across North America",
        "summary": "Covenant House operates shelters and services for homeless and trafficked youth in 31 cities across the US, Canada, and Latin America. Anti-trafficking services include immediate crisis care, legal advocacy, trauma-informed counseling, and transitional housing. Covenant House's research found 1 in 5 homeless youth in the US are trafficking victims. Contact: covenanthouse.org.",
        "source": "Covenant House, 2024",
    },
    {
        "type": "policy_update",
        "jurisdiction": "US",
        "title": "US President's Interagency Task Force (PITF) — National Action Plan to Combat Human Trafficking 2021",
        "summary": "The Biden Administration's 2021 National Action Plan established a survivor-centered, trauma-informed, and racially equitable approach to anti-trafficking. Key commitments: survivor inclusion in policy-making, expanded immigration relief, labor protections for visa workers, supply chain due diligence requirements, and increased OVC funding for survivor services. PITF coordinates 20+ federal agencies.",
        "source": "US PITF, 2021",
    },

    # ── Additional Asian and Pacific Organizations ───────────────────────────
    {
        "type": "contact",
        "jurisdiction": "TW",
        "title": "Garden of Hope Foundation — Anti-Trafficking Services, Taiwan",
        "summary": "Garden of Hope (GoH) provides shelter, legal aid, and advocacy for trafficking survivors in Taiwan, including migrant workers trafficked from Vietnam, Indonesia, Philippines, and Thailand. GoH's legal team has filed complaints against licensed labor brokers and won landmark cases establishing broker liability. Contact: goh.org.tw, +886 2 2577 1234.",
        "source": "Garden of Hope Foundation, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "JP",
        "title": "Solidarity Network with Migrants Japan — Anti-Trafficking and Migrant Worker Rights",
        "summary": "SMJ (Solidarity Network with Migrants Japan) advocates for migrant worker rights and anti-trafficking measures in Japan. Documents exploitation in the Technical Intern Training Program (TITP) and its successor, the Specified Skilled Worker program. Provides legal consultations to migrant workers. Contact: migrants.jp. SMJ contributed to the Japanese government's 2020 TITP reform process.",
        "source": "SMJ Japan, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "SG",
        "title": "TWC2 (Transient Workers Count Too) — Singapore Migrant Worker Advocacy",
        "summary": "TWC2 assists low-wage migrant workers in Singapore facing salary non-payment, injury claims, and trafficking situations. Operates weekly meal program reaching 1,000+ workers and provides case management services. Documents exploitation in construction, marine, and process sectors. Advocacy contributed to Singapore's Foreign Employee Dormitories Act (2015) on housing standards. Contact: twc2.org.sg.",
        "source": "TWC2, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "Visayan Forum Foundation — Anti-Trafficking and Domestic Worker Support, Philippines",
        "summary": "Visayan Forum operates transit homes and safe houses at Manila's North Harbor, South Harbor, and NAIA airport to intercept trafficking victims. Provides overnight assistance to at-risk women and children in transit. Community organizing in Visayas region addresses root causes of trafficking vulnerability. Serves 10,000+ beneficiaries annually. Contact: visayanforum.org.",
        "source": "Visayan Forum, 2024",
    },

    # ── Additional European and Middle East Organizations ────────────────────
    {
        "type": "contact",
        "jurisdiction": "IT",
        "title": "PIAM Onlus — Anti-Trafficking and Migrant Support, Italy",
        "summary": "PIAM Onlus in Asti, Italy provides anti-trafficking services to migrant workers in northern Italian agriculture, particularly Nigerian and Romanian women in sex trafficking and Romanian agricultural workers in forced labor. Operates the Article 18 path (Italian anti-trafficking law) for victim regularization. Partners with Italian NRM authorities. Contact: piamasti.it.",
        "source": "PIAM Onlus, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "QA",
        "title": "ILO Qatar — Worker Support Center",
        "summary": "ILO's Worker Support Center in Doha (opened 2020) provides confidential advice, referrals, and complaint filing assistance to migrant workers in Qatar. Services available in Arabic, English, Hindi, Tagalog, Sinhala, and other languages. Part of the ILO-Qatar partnership on labor reform. Contact: +974 4040 6050, workersc@ilo.org. Center handles wage complaints, employer abuse, and contract violations.",
        "source": "ILO Qatar, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "LB",
        "title": "Caritas Lebanon — Migrant Domestic Worker Support Program",
        "summary": "Caritas Lebanon operates migrant worker shelters and legal aid in Beirut, serving primarily Ethiopian, Bangladeshi, Sri Lankan, and Filipino domestic workers. Documents exploitation under Lebanon's kafala system and advocates for domestic worker labor law coverage. Program has supported 5,000+ workers since 2010. Contact: caritas-lb.org. Escalating caseloads due to Lebanon's economic collapse and deportation of workers.",
        "source": "Caritas Lebanon, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "AE",
        "title": "Migrant-Rights.org — Gulf Migrant Worker Watchdog",
        "summary": "Migrant-Rights.org is an independent media and research organization monitoring the rights of migrant workers in the Gulf states (UAE, Qatar, Saudi Arabia, Kuwait, Bahrain, Oman). Documents worker rights violations, tracks legal reforms, and publishes worker stories. Partners with HRW, AI, and academic institutions. Provides resources in Arabic, English, and other migrant languages. Contact: migrant-rights.org.",
        "source": "Migrant-Rights.org, 2024",
    },

    # ── Additional Latin American and Africa Organizations ───────────────────
    {
        "type": "contact",
        "jurisdiction": "BR",
        "title": "Repórter Brasil — Investigative Journalism on Modern Slavery",
        "summary": "Repórter Brasil is a Brazilian investigative journalism outlet specializing in modern slavery documentation. Manages the Dirty List Monitor (Lista Suja) database of Brazilian employers found guilty of forced labor. Investigations have exposed forced labor in cattle ranching, sugarcane, charcoal production, and garments. Contact: reporterbrasil.org.br. Investigations have been cited in international brand accountability campaigns.",
        "source": "Repórter Brasil, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "GH",
        "title": "International Needs Ghana — Anti-Trafficking and Child Protection",
        "summary": "International Needs Ghana (ING) works to eliminate child trafficking in fishing communities on Lake Volta, where children are trafficked to work as fishermen. ING's liberation and reintegration program has freed over 2,000 children from trafficking situations since 2002. Community-based prevention reduces vulnerability through economic support for families. Contact: internationalneedsghana.org.",
        "source": "International Needs Ghana, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "ET",
        "title": "Agar Ethiopia — Anti-Trafficking Services and Reintegration",
        "summary": "Agar Ethiopia provides shelter, reintegration services, and vocational training for women and girls trafficked domestically and internationally (particularly from Middle East routes). Documents exploitation of Ethiopian domestic workers abroad and internal trafficking of minors. Operates in Addis Ababa and Dire Dawa. Partners with MoLSA on National Referral Mechanism for trafficking survivors.",
        "source": "Agar Ethiopia, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "MX",
        "title": "Casa Alianza Mexico — Anti-Trafficking Services for Street Children and Youth",
        "summary": "Casa Alianza Mexico provides shelter, rehabilitation, and advocacy for trafficking victims among street children and youth in Mexico City, Guadalajara, and Cancun. Documents exploitation in sex tourism, forced begging, and agricultural labor. Casa Alianza has legal teams pursuing civil and criminal cases against traffickers. Part of the global Casa Alianza/Covenant House network.",
        "source": "Casa Alianza Mexico, 2024",
    },

    # ── Hotline and Technology Resources ─────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "INTL",
        "title": "Unseen's Global Modern Slavery Helpline Directory",
        "summary": "Unseen maintains a global directory of human trafficking and modern slavery helplines at modernslavery.co.uk/helplines. Includes hotlines in 60+ countries with language support information, operating hours, and service types. Directory is used by transportation workers, hotel staff, and first responders to connect potential victims with local resources.",
        "source": "Unseen, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Polaris Project — TraffickCam: Crowdsourced Hotel Room Image Database for Victim Identification",
        "summary": "TraffickCam is a mobile app that allows hotel guests to photograph hotel rooms, building a database of 1.5 million+ room images used by law enforcement to identify locations in trafficking evidence photos. Developed in partnership with Washington University in St. Louis. Database has helped identify locations in over 1,000 trafficking investigations across the United States.",
        "source": "Polaris / Washington University, 2020",
    },
    {
        "type": "policy_update",
        "jurisdiction": "INTL",
        "title": "Tech Coalition — Voluntary Principles to Counter Online Child Sexual Exploitation and Abuse",
        "summary": "The Tech Coalition (Apple, Google, Meta, Microsoft, Twitter, and others) adopted voluntary principles in 2020 to combat online child sexual exploitation including trafficking of minors. Principles cover: child safety by design, detection and reporting, information sharing, and survivor-centered approaches. Implementation monitored by Internet Watch Foundation and NCMEC.",
        "source": "Tech Coalition, 2020",
    },

    # ── Additional International Bodies ─────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Interpol — Stop Trafficking of People (STOP) Operations",
        "summary": "Interpol coordinates multi-country law enforcement operations against trafficking networks. Operation Liberterra (2021) resulted in 1,400+ arrests across 86 countries and identified 8,600+ victims. Interpol's STOP trafficking initiative provides member countries with intelligence sharing, training, and operational support. Contact: interpol.int/crimes/trafficking.",
        "source": "Interpol, 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "EUROPE",
        "title": "Europol — European Platform Against Trafficking Operations (EMPACT THB)",
        "summary": "Europol's EMPACT (European Multidisciplinary Platform Against Criminal Threats) Human Trafficking cycle coordinates anti-trafficking law enforcement across EU member states and partner countries. Focuses on trafficking networks exploiting migrants in labor and sex trafficking. Joint Investigation Teams have dismantled 30+ major trafficking networks since 2012.",
        "source": "Europol, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "FATF — Financial Action Task Force: Money Laundering from Human Trafficking (2011, updated 2018)",
        "summary": "FATF's guidance on financial flows from trafficking identifies typologies including cash-intensive front businesses (nail salons, car washes, massage parlors), cryptocurrency transactions, and remittance abuse. FATF's 2018 update addresses virtual assets and professional money laundering services used by trafficking networks. Standard applied by 39 member jurisdictions in AML/CFT compliance.",
        "source": "FATF, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "UNHCR — Refugee Protection and Human Trafficking: Joint Guidelines with IOM and UNHCR",
        "summary": "UNHCR and IOM's joint guidelines address the intersection of refugee displacement and trafficking risk, noting that refugees and asylum seekers are disproportionately vulnerable to trafficking. Guidelines cover identification and referral at border points, non-detention of trafficking victim asylum seekers, and durable solutions that address trafficking root causes. Essential resource for border agencies.",
        "source": "UNHCR / IOM, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Global Action Against Trafficking in Persons and the Smuggling of Migrants (GLO.ACT) — UNODC/IOM/EU",
        "summary": "GLO.ACT is a global initiative jointly implemented by UNODC and IOM with EU funding to strengthen national systems against trafficking and migrant smuggling. Active in 13 countries including Egypt, Kyrgyzstan, Morocco, Peru, South Africa, Thailand, and Ukraine. Provides technical assistance for NRM development, law enforcement training, victim services, and legal reform.",
        "source": "UNODC / IOM / EU, 2023",
    },

    # ── USA: Additional Federal and NGO Resources ──────────────────────────
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "US Department of Labor — Bureau of International Labor Affairs (ILAB) Child Labor and Forced Labor Reports",
        "summary": "ILAB publishes annual reports on child labor and forced labor in over 130 countries, the List of Goods Produced by Child Labor or Forced Labor (TVPRA List), and the List of Products of Forced or Indentured Child Labor (EO 13126 List). These reports inform US trade policy and import restrictions. Available at dol.gov/agencies/ilab. ILAB also funds counter-trafficking programs in over 50 countries.",
        "source": "US DOL ILAB, 2024",
    },
    {
        "type": "policy_update",
        "jurisdiction": "US",
        "title": "USCIS — T Nonimmigrant Status (T Visa) for Trafficking Survivors",
        "summary": "The T visa provides immigration protection to trafficking survivors who assist law enforcement, capping at 5,000 visas annually. T visa holders receive work authorization, public benefits access, and a path to permanent residency. Derivatives available for family members. Average processing time in 2023 was 23 months. Advocacy organizations work to expand annual cap and reduce processing delays.",
        "source": "USCIS, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "National Center for Missing and Exploited Children (NCMEC) — CyberTipline for Online Trafficking",
        "summary": "NCMEC's CyberTipline receives reports of online child sexual exploitation including trafficking. In 2023, NCMEC received over 36 million CyberTipline reports, predominantly from electronic service providers. Reports are forwarded to ICAC task forces and Interpol. NCMEC also operates a 24/7 hotline (1-800-THE-LOST) for missing children, including trafficking victims.",
        "source": "NCMEC, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "US",
        "title": "Mosaic Family Services — Dallas Trafficking Survivor Support",
        "summary": "Mosaic Family Services provides comprehensive services to trafficking and domestic violence survivors in Dallas, Texas, including emergency shelter, legal aid, counseling, and economic empowerment. Serves survivors from over 40 countries. Mosaic operates a dedicated trafficking survivor program and has served 800+ trafficking victims since 2007. Contact: mosaicfamilyservices.org, 214-821-5393.",
        "source": "Mosaic Family Services, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Freedom Network USA — Training Standards for Anti-Trafficking Service Providers",
        "summary": "Freedom Network USA (FNUSA) is the largest national network of anti-trafficking service providers and survivors in the US, with 60+ member organizations. Publishes training standards and best practices for trauma-informed, survivor-centered services. Advocates for human rights approaches to anti-trafficking policy. Annual conference brings together practitioners and survivors. Contact: freedomnetworkusa.org.",
        "source": "Freedom Network USA, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Truckers Against Trafficking (TAT) — Transportation Sector Anti-Trafficking Program",
        "summary": "Truckers Against Trafficking trains commercial truck drivers, bus drivers, and other transportation workers to identify and report trafficking. TAT has trained over 1.6 million truckers and distributed 2 million wallet cards with the National Human Trafficking Hotline. TAT's model has been replicated in 24 countries. Drivers call the hotline when they spot trafficking indicators at truck stops.",
        "source": "Truckers Against Trafficking, 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "US",
        "title": "US Department of State — Trafficking in Persons Report 2023: Tier Placements and Global Overview",
        "summary": "The 2023 TIP Report evaluated 188 governments on anti-trafficking efforts, placing 29 on Tier 1 (fully compliant), 78 on Tier 2, 30 on Tier 2 Watch List, and 11 on Tier 3 (not compliant). Tier 3 countries include Burma, China, Cuba, North Korea, and Russia. Tier 3 designation can trigger US foreign assistance restrictions. Report covers labor and sex trafficking across all regions.",
        "source": "US Department of State, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Human Trafficking Institute — Prosecutor Training and Court Capacity Building",
        "summary": "The Human Trafficking Institute trains federal and state prosecutors on trafficking case development, victim-centered prosecution, and trauma-informed evidentiary approaches. Has trained 5,000+ prosecutors across 47 US states. Also operates international programs in Uganda and Honduras. Research arm produces data on federal and state trafficking prosecutions. Contact: traffickinginstitute.org.",
        "source": "Human Trafficking Institute, 2024",
    },

    # ── UK and Europe: Additional Organizations ───────────────────────────
    {
        "type": "contact",
        "jurisdiction": "UK",
        "title": "Migrant Help — UK Asylum Seeker and Trafficking Support",
        "summary": "Migrant Help holds UK government contracts to support asylum seekers and trafficking survivors. Operates the Advice, Issue Reporting and Eligibility (AIRE) service providing information and advice to asylum seekers. Also provides support to modern slavery victims in Scotland and Northern Ireland. Contact: migranthelpuk.org, 01304 203977. Available in over 100 languages.",
        "source": "Migrant Help, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "Focus on Labour Exploitation (FLEX) — Labor Trafficking Policy Research UK",
        "summary": "FLEX conducts research and advocacy on labor trafficking in the UK, focusing on the policy conditions that create vulnerability including immigration enforcement, employment law gaps, and lack of labor inspection. Publishes briefings for parliamentarians, trade unions, and employers. Key campaigns: strengthening the Gangmasters and Labour Abuse Authority, protecting migrant workers' employment rights. Contact: labourexploitation.org.",
        "source": "FLEX, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "ATLEU (Anti-Trafficking and Labour Exploitation Unit) — Legal Services for Trafficking Survivors",
        "summary": "ATLEU provides specialist legal representation to trafficking and labor exploitation survivors in the UK, covering immigration, employment, and public law. Has represented 1,500+ clients since 2005. Key areas: challenging negative Conclusive Grounds decisions, securing compensation, and ensuring access to support services. Trains other legal practitioners on trafficking law. Contact: atleu.org.uk.",
        "source": "ATLEU, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "FR",
        "title": "ALC / Côte d'Azur Association — Anti-Trafficking Services France",
        "summary": "ALC (Association pour la protection et l'aide aux personnes en difficulté) operates France's primary dedicated anti-trafficking shelter network. Manages 15 specialist accommodations across France for trafficking survivors under the French National Referral Mechanism. Provides legal aid, psychosocial support, and reintegration services. Partners with the French anti-slavery unit (OCRTEH). Contact: alc.asso.fr.",
        "source": "ALC France, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "NL",
        "title": "Humanitas — Netherlands Trafficking Survivor Support",
        "summary": "Humanitas provides shelter, counseling, and social work services to trafficking survivors in the Netherlands through its dedicated anti-trafficking program. Works in partnership with CoMensha, municipal authorities, and the Dutch National Rapporteur. Advocates for access to social benefits for trafficking survivors regardless of immigration status. Contact: humanitas.nl.",
        "source": "Humanitas Netherlands, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "DE",
        "title": "Terre des Femmes — Violence Against Migrant Women and Trafficking, Germany",
        "summary": "Terre des Femmes Germany advocates for elimination of violence against women including trafficking, forced marriage, and honor-based violence. Produces annual report on trafficking in Germany, including analysis of source countries and exploitation patterns. Advocates for residence permit for trafficking survivors independent of prosecution cooperation. Contact: frauenrechte.de.",
        "source": "Terre des Femmes Germany, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "RO",
        "title": "ADPARE — Romanian Anti-Trafficking NGO Network",
        "summary": "ADPARE (Association for the Development of Alternative Practices for Reintegration and Education) operates Romania's largest NGO anti-trafficking network with 12 member organizations. Romania is a major EU source country for trafficking victims. ADPARE coordinates victim identification, referral, and reintegration programs in partnership with ANITP (National Agency Against Trafficking). Contact: adpare.ro.",
        "source": "ADPARE Romania, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "EUROPE",
        "title": "PICUM — Platform for International Cooperation on Undocumented Migrants",
        "summary": "PICUM advocates for rights of undocumented migrants in Europe, including access to justice for trafficking victims without fear of immigration enforcement. Reports document how conflation of migration control and anti-trafficking measures harms vulnerable migrants. Recommends firewall between immigration enforcement and labor/criminal justice for trafficking cases. Contact: picum.org.",
        "source": "PICUM, 2024",
    },

    # ── Asia: Additional Organizations ───────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "KH",
        "title": "LICADHO — Cambodian Anti-Trafficking and Human Rights Monitoring",
        "summary": "LICADHO (Cambodian League for the Promotion and Defense of Human Rights) monitors trafficking and human rights violations in Cambodia. Documents domestic trafficking for sexual exploitation, labor trafficking to Thailand and Malaysia, and trafficking from online scam compounds. Operates a legal aid clinic and victim support program. Contact: licadho-cambodia.org.",
        "source": "LICADHO Cambodia, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "MM",
        "title": "All Burma Students' Democratic Front (ABSDF) — Myanmar Anti-Trafficking Documentation",
        "summary": "ABSDF and partner organizations document trafficking of Myanmar nationals to scam compound operations in Cambodia, Laos, and Myanmar's border regions. Documents forced criminality in cybercrime compounds, sexual exploitation, and forced labor affecting tens of thousands of people. Coordinates with Fortify Rights and other organizations on advocacy for rescue operations.",
        "source": "ABSDF / Fortify Rights, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "VN",
        "title": "ECPAT Vietnam / Pacific Links — Anti-Trafficking Prevention in Origin Communities",
        "summary": "Pacific Links Foundation works with ECPAT Vietnam to prevent trafficking of Vietnamese women and children to China, Europe, and Gulf states. Community-based prevention programs in Ha Giang, Lao Cai, and Quang Binh provinces have reached 50,000 people. Also provides reintegration support for survivors returned from China via Operation Return Home cooperation with Vietnamese police.",
        "source": "Pacific Links Foundation / ECPAT Vietnam, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "NP",
        "title": "Shakti Samuha — Nepal's First Survivor-Led Anti-Trafficking Organization",
        "summary": "Shakti Samuha (Power Group), founded in 1996 by trafficking survivors, is Nepal's first survivor-led anti-trafficking organization. Provides legal aid, shelter, advocacy, and economic empowerment. Has supported 5,000+ survivors and advocated for Nepal's Human Trafficking and Transportation (Control) Act. Runs awareness campaigns in high-trafficking source districts including Sindhupalchok and Makwanpur.",
        "source": "Shakti Samuha, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "BD",
        "title": "BNWLA — Bangladesh National Women Lawyers Association Anti-Trafficking Program",
        "summary": "BNWLA provides legal aid to trafficking victims and survivors in Bangladesh, advocates for anti-trafficking law reform, and runs community prevention programs in high-trafficking areas including Cox's Bazar and border districts. Has handled 1,500+ trafficking cases in Bangladeshi courts. Partner organization of the UN Voluntary Trust Fund for Victims of Trafficking in Persons.",
        "source": "BNWLA Bangladesh, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "IN",
        "title": "Prajwala — Anti-Trafficking and Survivor Rehabilitation, Hyderabad India",
        "summary": "Prajwala rescues women and children from sex trafficking and exploitation in Andhra Pradesh and Telangana, operating a comprehensive survivor rehabilitation program including safe houses, education, vocational training, and reintegration. Has rescued over 9,000 women and girls and reintegrated 4,500+ into mainstream society. Pioneered 'Exit and Reintegration' model. Contact: prajwalaindia.com.",
        "source": "Prajwala India, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "LK",
        "title": "FOCAL (Forum for Grassroots Action and Learning) — Sri Lanka Migrant Worker Rights",
        "summary": "FOCAL advocates for rights of Sri Lankan migrant workers, particularly women in domestic work in Middle Eastern countries. Documents trafficking and exploitation patterns in the Sri Lanka-Gulf corridor. Partners with Sri Lanka Bureau of Foreign Employment (SLBFE) on pre-departure training and post-arrival monitoring. Advocates for employer accountability and reduced recruitment fees.",
        "source": "FOCAL Sri Lanka, 2023",
    },
    {
        "type": "contact",
        "jurisdiction": "PK",
        "title": "Bedari — Pakistan Anti-Trafficking and Child Rights NGO",
        "summary": "Bedari works on child trafficking, child labor, and violence against women in Pakistan, particularly in Punjab province. Documents trafficking from rural areas to urban centers and from Pakistan to Gulf states. Operates legal aid clinic and survivor support center in Lahore. Advocates for implementation of Pakistan's Prevention of Trafficking in Persons Act 2018. Contact: bedari.org.pk.",
        "source": "Bedari Pakistan, 2024",
    },

    # ── Africa: Additional Organizations ─────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "CM",
        "title": "ALVF — Association de Lutte Contre les Violences Faites aux Femmes, Cameroon",
        "summary": "ALVF provides anti-trafficking services in Cameroon including victim identification, shelter, legal aid, and reintegration. Documents trafficking of Cameroonian women to Gulf states and Europe, and internal trafficking of children for domestic work and agriculture. Partners with UNICEF and IOM on prevention campaigns. Contact: alvfcameroun.org.",
        "source": "ALVF Cameroon, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "ML",
        "title": "WILDAF Mali — Women in Law and Development in Africa: Anti-Trafficking Advocacy",
        "summary": "WiLDAF Mali works on women's rights and anti-trafficking in West Africa, documenting trafficking of Malian women and children to Gabon, Ivory Coast, and Europe. Advocates for legal reform and enforcement of Mali's Law No. 2012-023 against trafficking. Community-based prevention programs target high-trafficking regions including Mopti and Sikasso. Contact: wildaf-ao.org.",
        "source": "WiLDAF Mali, 2023",
    },
    {
        "type": "contact",
        "jurisdiction": "SN",
        "title": "OFAD-NAFOORE — Senegal Anti-Trafficking and Street Children Organization",
        "summary": "OFAD-NAFOORE provides services to child trafficking victims and street children in Dakar and Saint-Louis, Senegal. Documents exploitation of talibé children in religious schools (daaras), internal trafficking for begging, and external trafficking to France and Spain. Operates rehabilitation centers and works with Senegalese authorities on Quranic school reform. Contact: ofad.sn.",
        "source": "OFAD-NAFOORE Senegal, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "MR",
        "title": "SOS Esclaves — Anti-Slavery and Descent-Based Slavery Organization, Mauritania",
        "summary": "SOS Esclaves documents and combats descent-based slavery and trafficking in Mauritania, one of the last countries where traditional slavery practices persist. Provides legal aid to slavery survivors, advocates for enforcement of Mauritania's 2015 anti-slavery law, and monitors treatment of enslaved communities (Haratine and sub-Saharan Africans). Receives threats and faces legal harassment for its work.",
        "source": "SOS Esclaves Mauritania, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "TZ",
        "title": "KIWOHEDE — Kivulini Women's Rights Organization: Tanzania Anti-Trafficking Program",
        "summary": "KIWOHEDE (Kiota Women Health and Development) provides anti-trafficking services in Tanzania including victim identification, shelter, legal aid, and economic reintegration. Documents trafficking of Tanzanian women and children to Gulf states, South Africa, and within East Africa. Operates a trafficking survivor shelter in Dar es Salaam and prevention programs in Mwanza and Mbeya regions.",
        "source": "KIWOHEDE Tanzania, 2023",
    },

    # ── Americas: Additional Organizations ───────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "CO",
        "title": "Corporación Espacios de Mujer — Colombia Anti-Trafficking Services",
        "summary": "Corporación Espacios de Mujer provides anti-trafficking services in Colombia's Antioquia region, including victim identification, safe houses, legal aid, and psychosocial support. Documents internal trafficking and trafficking to Ecuador, Spain, and Brazil. Partners with Ruta Pacífica de las Mujeres on conflict-related trafficking. Contact: espaciosdemujer.org, Medellín.",
        "source": "Corporación Espacios de Mujer, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "PE",
        "title": "Capital Humano y Social Alternativo (CHS Alternativo) — Peru Anti-Trafficking Research",
        "summary": "CHS Alternativo monitors trafficking in Peru through annual reports and policy advocacy. Documents internal trafficking in Madre de Dios mining region, trafficking of indigenous women and girls, and transnational trafficking to Ecuador, Chile, and Spain. Has contributed to Peru's anti-trafficking legislation and national action plan. Contact: chsalternativo.org.",
        "source": "CHS Alternativo Peru, 2024",
    },
    {
        "type": "contact",
        "jurisdiction": "HT",
        "title": "Restavek Freedom — Child Domestic Servitude Anti-Trafficking Program, Haiti",
        "summary": "Restavek Freedom combats the restavek system in Haiti, in which children (estimated 400,000-500,000) are sent to work as domestic servants in other families' homes, constituting a form of child trafficking and exploitation. Programs combine child rescue, family reintegration, community education, and policy advocacy for law reform. Contact: restavekfreedom.org.",
        "source": "Restavek Freedom, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "GT",
        "title": "Asociación para la Prevención, Asistencia y Liberación (APAL) — Guatemala Anti-Trafficking",
        "summary": "APAL provides anti-trafficking services in Guatemala including victim identification, shelter, legal aid, and reintegration for women and children exploited in sex trafficking and domestic servitude. Documents trafficking routes from Guatemala to Mexico and the United States, and internal trafficking from rural Maya communities. Partners with SVET (Secretariat Against Sexual Violence, Exploitation and Trafficking).",
        "source": "APAL Guatemala, 2023",
    },

    # ── Cross-cutting: Investigative and Monitoring Organizations ────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Organised Crime and Corruption Reporting Project (OCCRP) — Trafficking Network Investigations",
        "summary": "OCCRP investigates organized crime groups involved in human trafficking, including European sex trafficking networks, forced labor in supply chains, and trafficking facilitated by corrupt officials. Published landmark investigations on trafficking through Libya and traffickers using encrypted communications. OCCRP partners include 60+ investigative outlets across 6 continents.",
        "source": "OCCRP, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Global Initiative Against Transnational Organized Crime (GI-TOC) — Trafficking and Smuggling Analysis",
        "summary": "GI-TOC produces research and analysis on criminal networks involved in human trafficking and migrant smuggling. Operates the Global Organized Crime Index, which ranks countries by organized crime levels including trafficking. Research has exposed trafficking networks in the Sahel, Balkans route, and Southeast Asia scam compound operations. Contact: globalinitiative.net.",
        "source": "GI-TOC, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Know The Chain — Supply Chain Forced Labor Benchmarking",
        "summary": "Know The Chain benchmarks the largest companies in food and beverage, information and communications technology, and apparel sectors on their efforts to address forced labor in supply chains. Evaluates commitment, traceability, supply chain auditing, procurement practices, worker voice, and remedy. 2023 benchmarks found average scores below 40/100 across all sectors, indicating significant gaps.",
        "source": "Know The Chain, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Responsible Business Alliance (RBA) — Audit Standards for Labor Trafficking in Electronics",
        "summary": "The RBA (formerly Electronic Industry Citizenship Coalition) Responsible Business Alliance Code of Conduct prohibits forced labor, trafficking, and debt bondage in member company supply chains. RBA Validated Audit Process (VBAP) covers 1,500+ factories annually. Audit findings are shared among member companies. RBA tools include Responsible Labor Initiative (RLI) for migrant worker protection.",
        "source": "Responsible Business Alliance, 2024",
    },

    # ── International Legal Frameworks and Monitoring Bodies ─────────────
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "Trafficking Victims Protection Act (TVPA) 2000 and Reauthorizations — US Federal Anti-Trafficking Law",
        "summary": "The TVPA (P.L. 106-386) established the US federal legal framework to combat trafficking. Key provisions: definition of severe forms of trafficking (sex trafficking of minors; force, fraud, or coercion for adult sex or labor trafficking); victim protection through T visa and benefits; mandatory minimum sentences; annual TIP Report on global efforts; and PITF coordination. Reauthorized in 2003, 2005, 2008, 2013, and 2022.",
        "source": "US Congress, 2000, 2022",
    },
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "UK Modern Slavery Act 2015 — Comprehensive Anti-Slavery Legislation",
        "summary": "The UK Modern Slavery Act consolidated and extended anti-slavery laws, creating offenses of slavery, servitude, forced labor, and human trafficking with penalties up to life imprisonment. Section 54 requires commercial organizations with UK turnover over GBP 36 million to publish annual transparency in supply chains statements. Established the Independent Anti-Slavery Commissioner role and Slavery and Trafficking Risk Orders.",
        "source": "UK Parliament, 2015",
    },
    {
        "type": "law",
        "jurisdiction": "AU",
        "title": "Australia Modern Slavery Act 2018 — Mandatory Reporting Requirements",
        "summary": "Australia's Modern Slavery Act requires entities with consolidated revenue of AUD 100 million or more to submit annual modern slavery statements covering risks in operations and supply chains, actions taken, and effectiveness assessment. 3,000+ entities are covered. Australian Border Force assesses compliance. Act also funds the Forced Labour Unit at DFAT and the Support for Trafficked People program.",
        "source": "Australian Parliament, 2018",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US",
        "title": "Uyghur Forced Labor Prevention Act (UFLPA) 2021 — Rebuttable Presumption of Forced Labor in Xinjiang",
        "summary": "The UFLPA establishes a rebuttable presumption that all goods produced in whole or in part in China's Xinjiang region are made with forced labor and are banned from import. Importers must provide clear and convincing evidence that goods are not tainted by forced labor to obtain entry. By 2024, CBP had blocked over USD 1 billion in goods. Law is administered by the UFLPA Entity List Steering Committee.",
        "source": "US Congress, 2021",
    },
    {
        "type": "policy_update",
        "jurisdiction": "INTL",
        "title": "OECD — Due Diligence Guidance for Responsible Business Conduct: Forced Labor Chapter",
        "summary": "OECD's Due Diligence Guidance provides sector-specific tools for identifying, preventing, and addressing forced labor and trafficking in supply chains. Sector supplements for garment/footwear, minerals, agriculture, and financial sector include specific guidance on recruitment practices, worker voice, and remedy. Adopted by 48 OECD and non-OECD states as the international reference standard for business and human rights due diligence.",
        "source": "OECD, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "UN Working Group on Business and Human Rights — Trafficking in Supply Chains Report (2021)",
        "summary": "The UN Working Group on Business and Human Rights issued a 2021 report finding trafficking in persons pervasive in global supply chains and calling for mandatory human rights due diligence laws. Report documented cases in agricultural, manufacturing, construction, and domestic work supply chains across 40+ countries. Recommended states adopt binding due diligence laws with trafficking-specific provisions and worker-led audit mechanisms.",
        "source": "UN Working Group on Business and Human Rights, 2021",
    },

    # ── Education, Training, and Awareness Resources ──────────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "DHS — iDecide: Interactive Training on Human Trafficking for Educators",
        "summary": "DHS Blue Campaign's iDecide interactive training series provides age-appropriate anti-trafficking education for middle and high school students. Covers recognition of trafficking warning signs, safe help-seeking behaviors, and online safety. Available free at bluecampaign.dhs.gov. Adopted by school districts in 38 states. Teacher professional development module accompanies student curriculum.",
        "source": "DHS Blue Campaign, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "ILO — Worker Education on Forced Labor and Trafficking: E-Learning Module",
        "summary": "ILO's free e-learning module 'Combating Forced Labour: A Handbook for Employers and Business' covers recognition of forced labor indicators, employer responsibilities under ILO conventions, and corrective action procedures. Available at ilo.org/forcedlabour in 10 languages. Module used by 500+ companies to train procurement and HR staff on forced labor risks in supply chains.",
        "source": "ILO, 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Mekong Club — Hong Kong Business Anti-Slavery Network",
        "summary": "The Mekong Club engages Hong Kong businesses in combating modern slavery and trafficking through training, supply chain tools, and advocacy. Produces the Worker Voice Toolkit for migrant workers in Hong Kong supply chains. Training has reached 50,000+ business professionals. Advocates for stronger Modern Slavery Act-equivalent reporting requirements in Hong Kong. Contact: themekongclub.org.",
        "source": "Mekong Club, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Stop the Traffik — Community-Based Prevention Coalition",
        "summary": "Stop the Traffik is a global coalition of 1,500+ organizations and businesses in 100 countries raising awareness about human trafficking and implementing prevention programs. Their STOP app enables community reporting of trafficking indicators. Trafficking Awareness Training (TAT) has trained over 300,000 people. Data from community reports helps identify trafficking hotspots and patterns.",
        "source": "Stop the Traffik, 2024",
    },

    # ── National Referral Mechanisms and Compensation ─────────────────────
    {
        "type": "policy_update",
        "jurisdiction": "INTL",
        "title": "OSCE / Council of Europe — National Referral Mechanism Handbook: Standards for Victim Identification",
        "summary": "The joint OSCE/Council of Europe NRM Handbook provides operational standards for national referral mechanisms to identify, refer, and support trafficking victims. Key standards: presumption of victim status, multi-agency first responder protocols, non-punitive approach to immigration violations, reflection and recovery periods, and legal aid access. Adopted as reference framework by 40+ countries.",
        "source": "OSCE / Council of Europe, 2004, updated 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "UN Voluntary Trust Fund for Victims of Trafficking in Persons — Direct Assistance Grants",
        "summary": "The UN Voluntary Trust Fund for Victims of Trafficking in Persons (UNVTF) provides grants to NGOs delivering direct assistance to trafficking survivors. Since 2010, UNVTF has supported 50,000+ survivors in 70 countries through grants to 140+ organizations. Grant cycles prioritize underserved populations including male victims, labor trafficking survivors, and survivors in conflict-affected settings. Apply at unodc.org/unvtf.",
        "source": "UNODC / UNVTF, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "IOM — Compensation and Restitution for Trafficking Victims: Global Assessment of Access to Justice",
        "summary": "IOM's 2022 assessment found only 1 in 10 trafficking victims receive any form of compensation despite legal entitlements in most jurisdictions. Barriers include: failure to identify as victim, lack of legal representation, asset seizure processes that exclude survivors, and long criminal justice timelines. Recommended civil remedies, confiscation-based compensation funds, and legal aid mandates as priority reforms.",
        "source": "IOM, 2022",
    },

    # ── Survivor Voice and Lived Experience Organizations ─────────────────
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "Survivor Alliance — Survivor-Led Organizations Network and Capacity Building",
        "summary": "Survivor Alliance is a network of survivor-led and survivor-serving organizations working to amplify survivor voices in anti-trafficking policy. Provides organizational capacity building grants and training to survivor-led groups. Maintains the Survivor Inclusion Index, which evaluates whether organizations have meaningful survivor inclusion in leadership, programming, and evaluation. Contact: survivoralliance.org.",
        "source": "Survivor Alliance, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Voices for Dignity — Survivor-Informed Anti-Trafficking Research Network",
        "summary": "Voices for Dignity (V4D) is an international network that integrates survivor expertise into anti-trafficking research design, data collection, and dissemination. Projects span Cambodia, Uganda, UK, and the US. V4D publishes survivors' own analyses of what interventions they find helpful and what they consider harmful. Network members are compensated researchers and paid advisory board members.",
        "source": "Voices for Dignity, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "GAATW — Who Is Responsible? A Toolkit on Rights, Remedies, and Corporate Accountability",
        "summary": "GAATW's toolkit guides trafficking survivors and their advocates in understanding how to pursue remedy from corporations whose supply chains enabled exploitation. Covers civil litigation, national contact point complaints under OECD guidelines, and corporate social responsibility mechanisms. Available in English, Thai, and Spanish at gaatw.org. Based on case studies from Thailand, Malaysia, and Qatar.",
        "source": "GAATW, 2021",
    },

    # ── Regional Monitoring and Reporting Bodies ──────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Asian Development Bank — Addressing Human Trafficking in Transport and Corridor Projects",
        "summary": "ADB's transport and infrastructure projects include anti-trafficking safeguards following documented cases of trafficking facilitated by road and rail construction corridors in the Mekong region. ADB's safeguard policies require trafficking risk assessment for large infrastructure projects, worker protection codes of conduct, and reporting mechanisms for construction workers. Technical assistance programs train border officials in transit countries.",
        "source": "Asian Development Bank, 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Arab League — Convention on Combating Trafficking in Persons (2012)",
        "summary": "The Arab League Convention on Combating Trafficking in Persons (adopted 2012) provides a regional framework for 22 Arab League member states. Covers prevention, prosecution, victim protection, and international cooperation. Convention specifically addresses kafala system reforms and trafficking of domestic workers. Technical assistance provided through UNODC's GLOTIP regional program for Arab states.",
        "source": "League of Arab States, 2012",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "ASEAN Convention Against Trafficking in Persons (ACTIP) — Regional Anti-Trafficking Framework",
        "summary": "ACTIP (2015) is the first binding anti-trafficking agreement among ASEAN member states, covering the 10 countries (Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Vietnam) of the region. Establishes obligations on criminalization, victim protection, and mutual legal assistance. Implementation monitored through ASEAN SOMTC (Senior Officials Meeting on Transnational Crime).",
        "source": "ASEAN, 2015",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "African Union — Ouagadougou Action Plan to Combat Trafficking in Human Beings 2006-2023: Final Review",
        "summary": "The African Union's Ouagadougou Action Plan established a 17-year framework for African states to combat trafficking and smuggling. Final 2023 review found improvements in national legislation (40 African states now have trafficking-specific laws) but persistent gaps in law enforcement capacity, victim services, and cross-border cooperation. Successor framework under development with stronger accountability mechanisms.",
        "source": "African Union, 2023",
    },
    {
        "type": "policy_update",
        "jurisdiction": "INTL",
        "title": "UN Global Compact for Safe, Orderly and Regular Migration (GCM) — Anti-Trafficking Provisions 2018",
        "summary": "The Global Compact for Migration (GCM), adopted by 164 UN member states in 2018, includes anti-trafficking provisions within its 23 objectives: eliminating recruitment fees charged to workers (Objective 6), providing legal identity and documentation (Objective 4), and ensuring access to justice and compensation for trafficking victims (Objective 7). Implementation monitoring by the International Migration Review Forum (IMRF).",
        "source": "UN General Assembly, 2018",
    },

    # ── Final Three Entries ───────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "Inter-Agency Council Against Trafficking (IACAT) — Philippines National Anti-Trafficking Coordination",
        "summary": "IACAT is the primary Philippine government body coordinating anti-trafficking efforts, chaired by the DOJ Secretary and composed of 19 member agencies. Operates the 1343 Action Line (24/7 tip line). Certifies NGOs for victim assistance, monitors implementation of the Anti-Trafficking in Persons Act (RA 9208 as amended by RA 10364), and produces annual trafficking statistics. Contact: iacat.gov.ph.",
        "source": "IACAT Philippines, 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "INTL",
        "title": "ILO — Profits and Poverty: The Economics of Forced Labour (2014, updated 2024)",
        "summary": "ILO's updated economic analysis found that forced labor generates approximately USD 236 billion in illegal profits annually: USD 73 billion from forced commercial sexual exploitation, USD 84 billion from forced labor in private economy excluding domestic work, USD 16 billion from state-imposed forced labor, and USD 63 billion from forced domestic work. Asia-Pacific generates the highest regional profits at USD 89 billion annually.",
        "source": "ILO, 2014, updated 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "INTL",
        "title": "Fortify Rights — Evidence-Based Human Rights Monitoring in Southeast Asia",
        "summary": "Fortify Rights conducts rigorous human rights investigations and advocacy in Southeast Asia, documenting trafficking of Rohingya, Myanmar nationals in scam compounds, and exploitation of Cambodian fishing workers. Evidence submitted to UN human rights mechanisms and used in international criminal accountability processes. Fortify Rights contributed to ICC referral documentation on Myanmar. Contact: fortifyrights.org.",
        "source": "Fortify Rights, 2024",
    },
]
