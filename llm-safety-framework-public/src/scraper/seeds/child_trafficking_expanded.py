"""Expanded child trafficking and worst-forms child labour facts (150 entries).

Covers: ILO C182, Lake Volta fishing, cocoa (Cote d'Ivoire/Ghana), cobalt (DRC),
mica (India/Madagascar), tobacco (Malawi), carpet weaving (Nepal/Afghanistan),
brick kilns (South Asia), child domestic workers, Almajiri/talibe exploitation,
restavek (Haiti), camel jockeys (historical), child soldiers, OSEC,
unaccompanied minors trafficking, child begging networks, baby factories,
surrogacy trafficking, and child marriage as trafficking.
"""

CHILD_TRAFFICKING_EXPANDED_FACTS: list[dict] = [
    # ── Global Statistics ─────────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO — Child Labour Global Estimates (2020)",
        "metric": "child_labour_global",
        "value": "160 million",
        "summary": (
            "ILO estimates 160 million children in child labour globally (2020), with "
            "79 million in hazardous work. First increase in 20 years (up 8.4 million "
            "since 2016). Sub-Saharan Africa has highest prevalence (23.9%). Agriculture "
            "accounts for 70%. Boys slightly more affected than girls (97M vs 63M). "
            "COVID-19 projected to push 8.9 million more children into labour by end of "
            "2022."
        ),
        "source": "ILO-UNICEF Global Estimates of Child Labour (2021)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "UNODC — Children as Share of Trafficking Victims (2022)",
        "metric": "child_trafficking_share",
        "value": "27% of detected victims",
        "summary": (
            "Children constitute 27% of all detected human trafficking victims globally "
            "(UNODC 2022). Girls account for 19% and boys 8% of total victims. Children "
            "are trafficked for forced labour, sexual exploitation, begging, organ removal, "
            "and child soldiers. Conflict zones and disaster-affected areas show five-fold "
            "elevated trafficking risk for children. Detection rates for child victims remain "
            "substantially lower than for adults due to recruitment within family or community "
            "networks."
        ),
        "source": "UNODC Global Report on Trafficking in Persons 2022",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "WeProtect — Online Child Sexual Exploitation Scale (2023)",
        "metric": "osec_reports",
        "value": "32 million CSAM reports in 2022",
        "summary": (
            "NCMEC received over 32 million CyberTipline reports in 2022, a 329% increase "
            "over 2018. WeProtect Global Alliance estimates 300 million children have been "
            "subject to online sexual exploitation or abuse. Live-streaming abuse (OSEC) is "
            "growing fastest: children directed in real time by paying offenders overseas. "
            "Philippines, Thailand, and Eastern Europe are primary production hubs. AI-generated "
            "CSAM now a significant and emerging enforcement challenge."
        ),
        "source": "NCMEC CyberTipline 2022 / WeProtect Global Threat Assessment 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO — Children in Hazardous Work (2020)",
        "metric": "hazardous_child_labour",
        "value": "79 million children",
        "summary": (
            "79 million children aged 5–17 are engaged in hazardous work globally (ILO 2020). "
            "Agriculture accounts for 71% (56.6 million). Industry: 10.3 million. Services: "
            "12.1 million. Boys: 56%. Children under 12 in hazardous conditions: 6.4 million. "
            "ILO C182 defines hazardous work as that likely to harm health, safety, or morals, "
            "including night work, toxic exposure, heavy loads, underground work, and sexual "
            "exploitation."
        ),
        "source": "ILO-UNICEF Child Labour: Global Estimates 2020",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Child Soldiers — Global Estimates (2023)",
        "metric": "child_soldiers_verified",
        "value": "22,000+ verified cases in 2022",
        "summary": (
            "UN verified 22,677 cases of recruitment and use of children by armed forces and "
            "groups in 2022. Actual numbers believed to be far higher. DRC, Somalia, Myanmar, "
            "Yemen, Nigeria, Mali, and CAR are most-affected conflicts. Children recruited as "
            "fighters, porters, spies, and sexual slaves ('bush wives'). Reintegration programs "
            "reach fewer than 30% of demobilized child soldiers. Former child soldiers face "
            "stigma, trauma, and acute re-trafficking risk."
        ),
        "source": "UN Secretary-General Annual Report on Children and Armed Conflict 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Child Marriage — Trafficking Intersection (2023)",
        "metric": "child_marriage_prevalence",
        "value": "650 million women married before 18",
        "summary": (
            "UNICEF estimates 650 million women alive today were married before age 18. "
            "About 12 million girls are married each year. Niger has the highest rate (76% of "
            "girls). Child marriage meets Palermo Protocol definition of trafficking when "
            "deception, force, or abuse of vulnerability is present, and the person is under 18. "
            "Girls from poor families are frequently sold for bride prices, constituting "
            "trafficking. Child marriage ends girls' education, perpetuating intergenerational "
            "poverty and exploitation cycles."
        ),
        "source": "UNICEF State of the World's Children 2023 / Girls Not Brides",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Unaccompanied Minors — Trafficking Risk at Borders (2022)",
        "metric": "unaccompanied_minors_global",
        "value": "300,000+ annually",
        "summary": (
            "An estimated 300,000 unaccompanied children cross international borders each year "
            "(IOM/UNHCR). US border encounters of unaccompanied children reached 147,000 in "
            "FY2022. EU: 40,000 unaccompanied minors in 2022. These children face acute "
            "trafficking risk at each border crossing and while in transit. UNICEF reports that "
            "75% of unaccompanied children in Central America and Mexico travel with strangers, "
            "dramatically elevating trafficking risk."
        ),
        "source": "IOM / UNHCR / UNICEF 2022",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Child Domestic Workers — Global Prevalence",
        "metric": "child_domestic_workers",
        "value": "11.5 million",
        "summary": (
            "ILO estimates 11.5 million children work as domestic workers globally, with girls "
            "constituting the overwhelming majority (71%). Most are under 15, often starting "
            "work as young as 8. Child domestic workers work 10–16 hours a day with no days "
            "off, no pay, and no access to education. Physical and sexual abuse is documented "
            "across all regions. Because they work in private homes, they are largely invisible "
            "to labour inspectors and legal protections are frequently absent."
        ),
        "source": "ILO Domestic Workers Across the World 2013 / Anti-Slavery International",
    },

    # ── Legal Frameworks ──────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Convention 182 — Worst Forms of Child Labour (1999)",
        "summary": (
            "First ILO convention to achieve universal ratification (187 member states by 2020). "
            "Defines 'worst forms' as: (a) all forms of slavery and slavery-like practices "
            "including trafficking, debt bondage, serfdom, forced recruitment into armed conflict; "
            "(b) use, procuring, or offering of a child for prostitution, CSAM production, or "
            "drug trafficking; (c) work likely to harm health, safety, or morals. Requires "
            "immediate, time-bound programmes of action. National hazardous work lists must be "
            "established and reviewed regularly. Companion to C138 (minimum age)."
        ),
        "source": "ILO C182 (1999) — ratified universally June 2020",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Convention 138 — Minimum Age for Employment (1973)",
        "summary": (
            "Sets minimum working age at 15 (14 for developing countries). Light work permitted "
            "from 13 (12 in developing countries). Hazardous work minimum: 18 in all cases. "
            "175 ratifications. Domestic work, family agriculture, and informal sectors remain "
            "major enforcement gaps in most jurisdictions. ILO NORMLEX tracks ratification "
            "and implementation reports country by country."
        ),
        "source": "ILO C138 (1973)",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "UN Convention on the Rights of the Child — Arts. 32, 34–36 (1989)",
        "summary": (
            "Most widely ratified human rights treaty (196 parties). Art. 32: right to protection "
            "from economic exploitation and work harmful to health or development. Art. 34: "
            "protection from sexual exploitation and abuse. Art. 35: states must take all "
            "appropriate national, bilateral, and multilateral measures to prevent abduction, "
            "sale, or trafficking. Art. 36: protection from all other forms of exploitation. "
            "Optional Protocol on Sale of Children (2000) adds obligations on criminalization, "
            "victim support, extradition, and international cooperation."
        ),
        "source": "UNCRC (1989) / OP-SC (2000)",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Palermo Protocol — Child-Specific Provisions (2000)",
        "summary": (
            "UN Protocol to Prevent, Suppress and Punish Trafficking in Persons (Palermo Protocol) "
            "Art. 3(c) provides that consent of a child victim is irrelevant: recruitment, "
            "transportation, transfer, harbouring, or receipt of a child for exploitation "
            "constitutes trafficking regardless of means used. 'Child' means any person under 18. "
            "Art. 6 requires victim support including child-specific reintegration. 178 states "
            "parties as of 2023."
        ),
        "source": "UN Protocol to Prevent Trafficking (Palermo Protocol) 2000, Art. 3(c)",
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "Trafficking Victims Protection Act — Child-Specific Standards (2000/2008)",
        "summary": (
            "TVPA (2000) established that any minor induced to perform commercial sex is a "
            "trafficking victim regardless of force, fraud, or coercion. TVPRA (2008) added "
            "civil cause of action for victims against beneficiaries. Section 307 of the Tariff "
            "Act (19 USC §1307) bans import of goods made with child or forced labour. US DOL "
            "ILAB publishes annual TDA list and biennial TVPRA list of goods produced with child "
            "labour. Tier placements in State Dept TIP Report carry diplomatic and aid consequences."
        ),
        "source": "22 USC §7102 (TVPA 2000); TVPRA 2008; 19 USC §1307",
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "US — Unaccompanied Alien Children (UAC) Protection Framework",
        "summary": (
            "Flores Settlement Agreement (1997) requires humane conditions and release within "
            "20 days for detained children. Trafficking Victims Protection Reauthorization Act "
            "(2008) mandates HHS/ORR care for unaccompanied alien children, including trafficking "
            "screening. TVPRA (2008) Sec. 235 requires DHS to transfer UAC to HHS custody within "
            "72 hours. 2021 HHS Inspector General found ORR placed 34,000+ children with sponsors "
            "without adequate background checks; subsequent trafficking exploitation documented "
            "in sponsor home networks."
        ),
        "source": "Flores v. Reno (1997); TVPRA (2008) Sec. 235; HHS OIG 2023",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "Philippines — Anti-Child Pornography Act and OSEC Law (2009/2022)",
        "summary": (
            "Republic Act 9775 (Anti-Child Pornography Act, 2009) criminalizes production, "
            "possession, and distribution of CSAM. RA 11930 (Anti-OSAEC Law, 2022) specifically "
            "addresses Online Sexual Abuse and Exploitation of Children, including live-streaming. "
            "Penalties: 20 years to life imprisonment for production and trafficking. ISPs must "
            "report and block. Philippines enacted first dedicated OSEC law in Asia due to scale "
            "of domestic production; estimated 500,000 Filipino children at risk annually."
        ),
        "source": "Republic Act 9775 (2009); Republic Act 11930 (2022)",
    },
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "India — Child Labour (Prohibition and Regulation) Amendment Act (2016)",
        "summary": (
            "Completely prohibits employment of children under 14 in any occupation (amended from "
            "hazardous-only prohibition). Children aged 14–18 banned from hazardous occupations. "
            "Family enterprise exception criticized by ILO and child rights groups as enabling "
            "abuse. Bonded Labour System (Abolition) Act 1976 remains enforceable for child "
            "bonded labour. NCLP (National Child Labour Project) provides 'special schools' for "
            "rescued children. Enforcement by state labour departments; penalties remain low "
            "(INR 50,000 / USD 600 maximum fine)."
        ),
        "source": "Child Labour (Prohibition and Regulation) Amendment Act 2016",
    },

    # ── Lake Volta Fishing (Ghana) ─────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "GH",
        "title": "Lake Volta — Child Trafficking for Fishing (Ghana)",
        "summary": (
            "Lake Volta (Ghana) is one of the world's most documented sites of child labour "
            "trafficking for fishing. Estimates range from 15,000 to 21,000 children working "
            "on the lake. Children as young as 5 are purchased or 'rented' from impoverished "
            "parents in northern Ghana and Togo for USD 20–200 per season. They dive to "
            "untangle nets from tree stumps on the lake floor — drowning deaths are frequent. "
            "Children work 14-hour days, receive no education, and are subject to physical "
            "abuse. IJM and local NGOs have conducted rescue operations but scale of problem "
            "persists."
        ),
        "source": "IJM / US DOL ILAB / UNICEF Ghana",
    },
    {
        "type": "case_study",
        "jurisdiction": "GH",
        "title": "Lake Volta — Debt Bondage Mechanisms in Child Fishing",
        "summary": (
            "Parents on Lake Volta receive a small cash advance ('asika') from fishermen — "
            "typically GHS 300–1,000 (USD 25–85) — in exchange for a child's labour for a "
            "season or longer. The advance functions as debt bondage: the child cannot leave "
            "until the debt is 'repaid' through labour, though the accounting is never "
            "transparent. Children are sometimes re-sold between fishermen, with the debt "
            "transferred. Rescue organizations note that parents are often themselves "
            "trafficking victims of poverty and misinformation about conditions."
        ),
        "source": "IJM Lake Volta Report 2019 / Environmental Justice Foundation",
    },
    {
        "type": "advisory",
        "jurisdiction": "GH",
        "title": "Ghana — Government Response to Lake Volta Child Labour",
        "summary": (
            "Ghana ratified ILO C182 in 2000 and its Children's Act (Act 560, 1998) prohibits "
            "child trafficking and hazardous child labour. Ghana's Human Trafficking Act (Act "
            "694, 2005) criminalizes trafficking with 5-year minimum sentences. The Ghana "
            "Anti-Human Trafficking Unit and IOM operate reintegration programs on Lake Volta. "
            "Free Compulsory Universal Basic Education (FCUBE) aims to reduce supply-side "
            "vulnerability. Persistent challenges: poverty in Volta region, weak enforcement "
            "in remote lakeside communities, cultural normalization of child labour in fishing."
        ),
        "source": "Ghana Anti-Human Trafficking Act 694 (2005) / IOM Ghana",
    },

    # ── Cocoa (Cote d'Ivoire / Ghana) ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "CI",
        "title": "Child Labour in Cote d'Ivoire Cocoa — Harkin-Engel Protocol Failure",
        "summary": (
            "Cote d'Ivoire produces approximately 40% of global cocoa. US DOL estimates "
            "1.56 million children in child labour in cocoa farming in Cote d'Ivoire and "
            "Ghana (2019 survey). Despite the Harkin-Engel Protocol (2001) — a voluntary "
            "industry pledge to eliminate worst forms by 2005 — child labour actually "
            "increased 14% between 2009 and 2019. Children use machetes, apply pesticides, "
            "and carry heavy loads. Some are trafficked from Burkina Faso and Mali. Chocolate "
            "companies (Nestlé, Mars, Hershey, etc.) have faced class action suits and "
            "Congressional scrutiny."
        ),
        "source": "US DOL 2020 Report on Child Labour in West African Cocoa / Harkin-Engel Protocol",
    },
    {
        "type": "case_study",
        "jurisdiction": "GH",
        "title": "Child Labour in Ghana Cocoa — Brong-Ahafo and Western Regions",
        "summary": (
            "US DOL 2020 survey found 770,000 children in child labour in Ghana's cocoa sector, "
            "primarily in Brong-Ahafo, Western, and Ashanti regions. Children as young as 5 work "
            "on family farms — a legal grey area in Ghana's Children's Act. However, trafficked "
            "children from northern Ghana and Burkina Faso are also found on cocoa farms: working "
            "without pay, confined, and denied education. Ghana's COCOBOD has a child labour "
            "monitoring system, but coverage remains below 30% of cocoa-growing communities."
        ),
        "source": "US DOL ILAB 2020 / COCOBOD / Fairtrade Foundation",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Nestlé USA v. Doe — Supreme Court on Corporate Liability for Child Labour (2021)",
        "summary": (
            "In Nestlé USA v. Doe (2021), six Malian nationals who alleged they were trafficked "
            "as children to work on Ivorian cocoa farms sued Nestlé and Cargill under the Alien "
            "Tort Statute. US Supreme Court ruled 8-1 that federal courts lacked jurisdiction "
            "because corporate conduct (purchasing decisions) occurred primarily in US, not abroad "
            "where harm happened. Case highlights accountability gap for supply chain child "
            "trafficking. Congress has not enacted legislation closing this gap."
        ),
        "source": "Nestlé USA, Inc. v. Doe, 593 U.S. 369 (2021)",
    },

    # ── Cobalt Mining (DRC) ────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "CD",
        "title": "DRC Cobalt — Child Labour in Artisanal Mining (Katanga)",
        "summary": (
            "Democratic Republic of Congo produces approximately 70% of global cobalt, essential "
            "for lithium-ion batteries in EVs and consumer electronics. Amnesty International "
            "and researcher Siddharth Kara estimate 40,000+ children work in artisanal cobalt "
            "mining (ASM) in Lualaba and Haut-Katanga provinces. Children as young as 6 wash, "
            "sort, and carry ore in open pits. Tunnel collapses kill dozens annually. Chronic "
            "cobalt dust exposure causes pulmonary disease. ASM cobalt enters supply chains via "
            "intermediary traders (négociants) who sell to Glencore-owned Umicore and Chinese "
            "smelters supplying Apple, Samsung, Tesla, and others."
        ),
        "source": "Amnesty International 2016, 2023 / Siddharth Kara 'Cobalt Red' (2023)",
    },
    {
        "type": "case_study",
        "jurisdiction": "CD",
        "title": "DRC Cobalt — Supply Chain Traceability and Corporate Accountability",
        "summary": (
            "OECD Due Diligence Guidance for Responsible Mineral Supply Chains requires companies "
            "sourcing from conflict-affected areas to map supply chains to the mine level. "
            "Responsible Minerals Initiative (RMI) created Cobalt Reporting Template. Despite "
            "these mechanisms, IPIS mapping shows only 1 in 5 artisanal mining sites in DRC "
            "receives any monitoring visit. Apple and Tesla claim RMAP-compliant sourcing, but "
            "independent verification of child-labour-free ASM cobalt is largely absent. "
            "DRC government enacted child labour prohibition in mining (2017) but enforcement "
            "capacity is near-zero."
        ),
        "source": "OECD Due Diligence Guidance 2016 / IPIS 2022 / RMI",
    },

    # ── Mica (India / Madagascar) ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Child Labour in Indian Mica Mining — Jharkhand and Bihar",
        "summary": (
            "India produces approximately 25% of global mica. Jharkhand and Bihar are major "
            "production states where most mines are illegal and unregistered. Kailash Satyarthi "
            "Children's Foundation (KSCF) and Terre des Hommes estimate 22,000 children work "
            "in mica mining in these two states. Children crawl into narrow mine shafts to "
            "collect mica flakes. Cave-ins are frequent and rarely reported. Mica enters cosmetics "
            "(eye shadow, lipstick), automotive paint, and electronics supply chains. "
            "Major cosmetics brands including L'Oréal and Estée Lauder have pledged "
            "child-labour-free sourcing through the Responsible Mica Initiative (RMI)."
        ),
        "source": "KSCF / Terre des Hommes / Responsible Mica Initiative 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "MG",
        "title": "Child Labour in Madagascar Mica — Southern Highlands",
        "summary": (
            "Madagascar is the world's second-largest mica producer. ActionAid and Terre des "
            "Hommes investigations found children as young as 6 working in mica mining in "
            "Betafo and Ambatofinandrahana districts of the central highlands. Children carry "
            "heavy sacks of mica flakes, cutting hands on sharp edges. Families earn USD 0.50–"
            "1.50/day combined — entirely dependent on child labour contributions. Mine sites "
            "have no safety equipment, no sanitation. Unlike India, Madagascar has almost no "
            "NGO presence at mining sites and no Responsible Mica Initiative membership."
        ),
        "source": "ActionAid / Terre des Hommes Madagascar Report 2019",
    },

    # ── Tobacco (Malawi) ──────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MW",
        "title": "Child Labour in Malawi Tobacco — Tenancy System and Nicotine Poisoning",
        "summary": (
            "US DOL estimates 78,000 children work in Malawi's tobacco sector. The tenancy "
            "system places entire families on estate land owned by landlords; children work "
            "alongside parents to meet labour quotas. Green Tobacco Sickness — acute nicotine "
            "absorption through skin contact with wet tobacco leaves — causes vomiting, "
            "headaches, and neurological symptoms in child workers. Children work without "
            "protective equipment. Malawi's tobacco exports are worth USD 400M annually; "
            "major buyers include Philip Morris International, British American Tobacco, "
            "and Japan Tobacco International."
        ),
        "source": "US DOL ILAB / Plan International / HRW 'Tobacco's Hidden Children' (2014)",
    },
    {
        "type": "advisory",
        "jurisdiction": "MW",
        "title": "Malawi — Tobacco Industry Self-Regulation Outcomes",
        "summary": (
            "Tobacco companies operating in Malawi committed to child labour elimination through "
            "the Eliminating Child Labour in Tobacco Growing (ECLT) Foundation. Third-party "
            "audits of ECLT member farms showed partial improvements in areas with direct "
            "company training programs. However, HRW (2023) found child labour persisting on "
            "contractor farms supplying ECLT members. Gap between company commitments and ground "
            "reality remains large. Malawi ratified ILO C182 in 1999 but enforcement capacity "
            "is severely limited — one labour inspector per 17,000 workers nationally."
        ),
        "source": "ECLT Foundation / HRW 2023 Malawi Update",
    },

    # ── Carpet Weaving (Nepal / Afghanistan) ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Child Labour in Nepal Carpet Weaving — Kathmandu Valley",
        "summary": (
            "Nepal is a major exporter of hand-knotted carpets (primarily to Germany and USA). "
            "Kathmandu valley carpet factories historically employed large numbers of children, "
            "many trafficked from rural hill districts. US DOL and UNICEF interventions in the "
            "1990s–2000s reduced the practice significantly: child carpet workers fell from "
            "estimated 150,000 (1995) to under 30,000 (2010). However, ILO's 2020 Nepal Child "
            "Labour Survey found 1.1 million children still in child labour nationally, with "
            "the carpet and handicraft sector still implicated. Bonded labour of child carpet "
            "weavers tied to advances to parents persists in smaller workshops."
        ),
        "source": "US DOL ILAB / ILO Nepal / UNICEF Nepal Child Labour Survey 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "AF",
        "title": "Child Labour in Afghanistan Carpet Weaving — Under Taliban Rule",
        "summary": (
            "Afghanistan produces some of the world's finest hand-knotted carpets (Mazar-i-Sharif, "
            "Herat, Kabul regions). UNICEF estimated 500,000 children in carpet weaving before "
            "2021 Taliban takeover. Under Taliban rule, girls above age 12 are banned from school "
            "— dramatically increasing their availability for home-based carpet weaving. Boys "
            "work in workshop settings, sometimes trafficked from rural provinces with advances "
            "to parents. Carpet exports continue via Pakistan intermediaries; Western importers "
            "face challenges verifying child-labour-free sourcing under current access restrictions."
        ),
        "source": "UNICEF Afghanistan / ILO / US DOL ILAB Afghanistan Profile 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Carpet Weaving — Goodweave Certification System",
        "summary": (
            "GoodWeave International (formerly RUGMARK) is the leading certification scheme for "
            "child-labour-free hand-knotted carpets. Operates in India, Nepal, and Afghanistan. "
            "Unannounced factory inspections and community monitoring. GoodWeave-certified exports "
            "represent less than 5% of global carpet trade. When child workers are found, they "
            "are placed in GoodWeave-supported education programs. Limitations: cannot certify "
            "Afghan carpets under current access conditions; home-based weaving difficult to inspect."
        ),
        "source": "GoodWeave International Annual Report 2022",
    },

    # ── Brick Kilns (South Asia) ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Brick Kiln Child Labour and Bonded Labour — India",
        "summary": (
            "India's brick kiln industry employs an estimated 10–23 million workers seasonally, "
            "including large numbers of bonded families from Scheduled Caste and Adivasi "
            "communities. Entire families — including children — are bonded via advance payments "
            "(peshgi) by kiln contractors. Children from ages 5 upward mold bricks, carry loads, "
            "and tend fires. The migrant nature of kiln work (seasonal movement across state lines) "
            "places children outside the reach of local child welfare officials. Heat stress, "
            "burns, respiratory disease from coal dust and smoke are endemic."
        ),
        "source": "India NHRC / ILO / Bachpan Bachao Andolan / Anti-Slavery International",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Brick Kiln Bonded Child Labour — Pakistan (Punjab and Sindh)",
        "summary": (
            "Pakistan's brick kilns are among the most extensively documented sites of bonded "
            "child labour in the world. The Bonded Labour Liberation Front (BLLF) estimates "
            "4.5 million bonded workers in Pakistan, with children comprising a substantial "
            "minority. Peshgi advances of PKR 5,000–50,000 (USD 18–180) bind families for "
            "seasons or years. Children work 10–12 hours daily, seven days a week during the "
            "kiln season (October–May). Pakistan's Bonded Labour System (Abolition) Act 1992 "
            "is rarely enforced at the provincial level; magistrates routinely release "
            "employers without penalties."
        ),
        "source": "BLLF / ILO Pakistan / US DOL ILAB Pakistan Report",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Brick Kiln Child Labour — Bangladesh",
        "summary": (
            "Bangladesh has approximately 8,000 registered brick kilns (and thousands more "
            "unregistered), clustered around Dhaka, Chittagong, and Rajshahi. UNICEF estimates "
            "10% of kiln workers are children, primarily from rural northern districts. Children "
            "are trafficked or migrated with families from char (river island) areas particularly "
            "vulnerable to flood displacement. Child brick workers suffer burns, musculoskeletal "
            "injuries, and high rates of respiratory illness from coal smoke. Kiln brick "
            "production drives Dhaka's construction boom, linking child exploitation to real "
            "estate development."
        ),
        "source": "UNICEF Bangladesh / Dhaka Tribune investigations 2021",
    },

    # ── Child Domestic Workers ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Child Domestic Workers — Worst Forms Across Regions",
        "summary": (
            "Child domestic workers are among the most hidden and least protected child labourers. "
            "Globally concentrated in South and Southeast Asia (India, Indonesia, Philippines), "
            "Sub-Saharan Africa (Tanzania, DRC, West Africa), Latin America (Bolivia, Haiti, "
            "Brazil), and the Middle East. Girls from rural areas are sent to urban employers "
            "by parents with promises of education and better opportunities — a common deception. "
            "Deprivation of liberty (locked in employers' homes), denial of food, physical "
            "violence, and sexual abuse are documented in all regions. ILO C189 (Domestic "
            "Workers Convention, 2011) calls for equal labour protections but has only 38 "
            "ratifications."
        ),
        "source": "ILO / Anti-Slavery International / Human Rights Watch regional reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Child Domestic Workers and PRT Perempuan Exploitation",
        "summary": (
            "Indonesia's domestic worker sector is estimated at 4–10 million workers, including "
            "a significant proportion of girls under 18. Indonesia enacted Government Regulation "
            "No. 78/2015 on wages, but domestic workers are excluded from the Manpower Act "
            "entirely. Girls from Central Java, East Java, and Nusa Tenggara Timur are trafficked "
            "to Surabaya, Jakarta, and Bali. Common abuses: salary withheld for months, passports "
            "confiscated, prohibited from leaving. JALA PRT (domestic worker network) documents "
            "hundreds of cases annually. Draft Law on Domestic Workers has stalled in parliament "
            "since 2010."
        ),
        "source": "JALA PRT / ILO Indonesia / HRW 'Swept Under the Rug' 2023",
    },

    # ── Almajiri / Talibe Exploitation ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Almajiri System — Nigeria (Northern States)",
        "summary": (
            "The Almajiri system in northern Nigeria involves sending boys (often aged 5–10) "
            "from rural families to urban Quranic schools (tsangaya) under the care of a "
            "malam (teacher). While rooted in Islamic educational tradition, the system has "
            "been documented by HRW and UNICEF as a form of forced child begging. Malams "
            "require boys to beg for food and money to support the school. Children sleep in "
            "overcrowded, unsanitary conditions, receive no formal education, and face physical "
            "punishment. Nigeria has an estimated 10–15 million Almajiri children; the northwest "
            "and northeast states have the highest concentrations."
        ),
        "source": "HRW 'Almajiri System' 2022 / UNICEF Nigeria / Nigeria CLEEN Foundation",
    },
    {
        "type": "case_study",
        "jurisdiction": "SN",
        "title": "Talibe System — Senegal and West Africa",
        "summary": (
            "An estimated 100,000 talibé children (Quranic students, primarily boys aged 5–15) "
            "in Senegal are forced to beg by their marabout (Quranic teacher). Children must "
            "bring daily quotas of CFA 300–500 (USD 0.50–0.85) or face beatings. Most live "
            "in overcrowded daraas (Quranic schools) with inadequate food, water, and sanitation. "
            "HRW documented that children are trafficked from Guinea, Guinea-Bissau, Mali, and "
            "Gambia to daraas in Dakar and Saint-Louis. Senegalese Penal Code Art. 245 prohibits "
            "child begging; enforcement is near-zero due to religious and political sensitivity."
        ),
        "source": "HRW 'Off the Backs of Children' 2010, 2023 update / UNICEF Senegal",
    },
    {
        "type": "case_study",
        "jurisdiction": "GN",
        "title": "Cross-Border Talibe Trafficking — Guinea to Senegal",
        "summary": (
            "Children from Guinea (particularly Fouta Djallon region) are trafficked across "
            "the border to daraas in Senegal's Dakar, Thiès, and Saint-Louis regions. Parents "
            "often pay a small sum to marabouts who promise religious education. Children are "
            "then forced to beg full-time with no or minimal Quranic instruction. IOM documented "
            "significant cross-border movement: children found in Dakar speaking only Pular "
            "(Guinean Fulani dialect), indicating recent trafficking. Repatriation programs "
            "operate but are under-resourced; children often return to the same daraas."
        ),
        "source": "IOM Guinea / Senegal / HRW cross-border child trafficking documentation",
    },

    # ── Restavek (Haiti) ──────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HT",
        "title": "Restavek System — Child Domestic Servitude in Haiti",
        "summary": (
            "The restavek ('one who stays with') system in Haiti involves poor rural families "
            "sending children — typically girls aged 8–15 — to urban or better-off households "
            "as domestic servants. The Restavek Freedom Foundation estimates 300,000–500,000 "
            "children in the system. Children receive no pay, attend school infrequently (if "
            "at all), work 12+ hour days, and face high rates of physical and sexual abuse. "
            "Restavek is normalized across class lines — even lower-middle-class families "
            "employ restaveks. Haiti's Children's Institute (IBESR) has limited capacity; "
            "restavek is technically prohibited under Haitian law but prosecutions are rare."
        ),
        "source": "Restavek Freedom Foundation / UNICEF Haiti / IJM Haiti",
    },
    {
        "type": "case_study",
        "jurisdiction": "HT",
        "title": "Restavek Post-Earthquake Trafficking Surge (2010)",
        "summary": (
            "After the January 2010 Haiti earthquake (230,000 deaths, 1.5 million displaced), "
            "child trafficking including restavek placement surged. IOM documented children "
            "moving across the border into Dominican Republic in restavek arrangements. "
            "Traffickers exploited displacement camps, posing as relatives or NGO workers. "
            "UNICEF established child-friendly spaces in camps but trafficking of earthquake-"
            "affected children was documented for years post-disaster. The 2010 earthquake "
            "demonstrated that humanitarian crises dramatically amplify child trafficking "
            "vulnerability and the need for immediate child protection interventions."
        ),
        "source": "IOM / UNICEF Haiti Earthquake Response / Save the Children 2011",
    },

    # ── Camel Jockeys (Historical) ─────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "Child Camel Jockeys — UAE, Qatar, Saudi Arabia (Historical, 1970s–2005)",
        "summary": (
            "Children — some as young as 2–4 years old — from Pakistan, Bangladesh, Sudan, "
            "and Mauritania were trafficked to Gulf states to serve as camel jockeys. Children "
            "were kept deliberately underweight (starvation used to maintain low weight). Falls "
            "from camels caused fractures and deaths; children were crushed under camel hooves. "
            "They were isolated on camel farms with no access to education or family contact. "
            "UAE banned the practice (2005); Qatar (2005); Saudi Arabia (2007). All three "
            "transitioned to robotic jockeys. UNICEF's Qatar and UAE programs repatriated "
            "over 1,000 children and provided rehabilitation support."
        ),
        "source": "UNICEF / HRW 'Small Change' 2003 / Anti-Slavery International",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Camel Jockey Legacy — Lessons for Technology-Based Elimination",
        "summary": (
            "The elimination of child camel jockeys is cited as a model case study for combining "
            "legal prohibition, technology substitution (robotic jockeys), and victim repatriation. "
            "Key lessons: (1) legislative bans are ineffective without enforcement and victim "
            "identification programs; (2) technology substitution removes economic demand for "
            "child labour; (3) repatriation and rehabilitation must be adequately funded "
            "and sustained; (4) bilateral agreements between origin and destination countries "
            "are essential. The model has been proposed for other sectors (child mining, fishing) "
            "but technology substitution is not always feasible."
        ),
        "source": "ILO / UNICEF / Anti-Slavery International post-intervention analysis",
    },

    # ── Child Soldiers ─────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "CD",
        "title": "Child Soldiers in DRC — Armed Group Recruitment",
        "summary": (
            "DRC has consistently had among the highest verified child soldier recruitment globally. "
            "UN Group of Experts and MONUSCO document recruitment by at least 20 armed groups "
            "operating in eastern DRC (North Kivu, South Kivu, Ituri). Children as young as 7 "
            "are recruited — some voluntarily seeking protection, others abducted. Girls serve "
            "as fighters and 'bush wives' (sexual slaves). Former child soldiers face acute "
            "stigma and re-recruitment risk upon demobilization. UNICEF supports DDR (Disarmament, "
            "Demobilization, Rehabilitation) programs but funding gaps leave thousands without "
            "reintegration support."
        ),
        "source": "UN Group of Experts on DRC / UNICEF MARA Database 2022 / MONUSCO",
    },
    {
        "type": "case_study",
        "jurisdiction": "ML",
        "title": "Child Soldiers in Sahel — Mali, Niger, Burkina Faso",
        "summary": (
            "The Sahel crisis (expanding jihadist insurgency since 2012) has produced a dramatic "
            "increase in child soldier recruitment across Mali, Niger, and Burkina Faso. Groups "
            "including JNIM and ISWAP recruit children as young as 10 with promises of money and "
            "protection. Children are used as fighters, lookouts, suicide bombers, and in sexual "
            "servitude. UN Security Council Working Group on Children and Armed Conflict listed "
            "15 parties in Mali alone as of 2023. Regional DDR capacity is critically insufficient; "
            "fewer than 5% of child soldiers in the Sahel receive formal reintegration support."
        ),
        "source": "UN SGACC Annual Report 2023 / UNICEF Sahel / Geneva Call",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Child Soldiers in Myanmar — Tatmadaw and Armed Groups Post-Coup",
        "summary": (
            "Myanmar's military (Tatmadaw) has been listed on the UN Secretary-General's 'List "
            "of Shame' for child recruitment since 2002. Post-2021 coup, recruitment of children "
            "by both the Tatmadaw and People's Defence Forces (PDF) has been documented. UN "
            "verified 250+ cases of child recruitment in 2022. Children abducted from displacement "
            "camps and recruited at military checkpoints. Tatmadaw has signed five Action Plans "
            "with the UN since 2012 but continues to appear on the List of Shame. PDF is a new "
            "actor; child protection mechanisms largely non-functional under military government."
        ),
        "source": "UN SGACC 2023 / UNICEF Myanmar / Fortify Rights",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Optional Protocol on the Involvement of Children in Armed Conflict (2000)",
        "summary": (
            "OPAC (Optional Protocol to the CRC on Children in Armed Conflict) raised the minimum "
            "age for direct participation in hostilities to 18. States parties must set a minimum "
            "voluntary recruitment age of at least 16. 170 states parties. Armed groups (non-state "
            "actors) are prohibited from any recruitment or use of under-18s. Requires criminalization "
            "of recruitment of under-18s. Implementation monitored through CRC Committee reviews. "
            "International Criminal Court jurisdiction includes child recruitment under 15 as a "
            "war crime (Rome Statute Art. 8(2)(b)(xxvi))."
        ),
        "source": "OPAC (2000); Rome Statute Art. 8(2)(b)(xxvi)",
    },

    # ── Online Sexual Exploitation of Children (OSEC) ─────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Philippines — OSEC (Online Sexual Exploitation of Children) Production Hub",
        "summary": (
            "The Philippines has been identified as the world's leading OSEC production hub. "
            "IJM estimates 500,000 Filipino children at risk of OSEC annually. Live-streaming "
            "abuse is orchestrated from residential areas, often by family members or relatives "
            "of the child. Offenders pay USD 20–100 per live-streaming session from the US, UK, "
            "Australia, and other Western countries. Payment via remittance services, PayPal, "
            "and cryptocurrency. IJM's Philippines operations have resulted in 900+ child "
            "rescues and 70+ offender convictions since 2011. Philippine National Police and "
            "NBI-ACES are primary law enforcement agencies."
        ),
        "source": "IJM Philippines OSEC Report 2022 / NBI-ACES / ECPAT Philippines",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "OSEC — Family-Facilitated Abuse in the Philippines",
        "summary": (
            "IJM found that in 62% of Philippines OSEC cases, a parent or sibling was the "
            "primary perpetrator. Extreme poverty (household income below USD 2/day) is the "
            "primary driver; OSEC is perceived as 'victimless' because no physical contact "
            "occurs. Children are typically told they are performing for money to help the "
            "family. Trauma responses in OSEC survivors include depression, PTSD, and "
            "normalization of abuse. Survivor-centered jurisprudence requires child-friendly "
            "courts and camera testimony. Philippine Star Report (2022) found OSEC cases "
            "correlated with internet penetration in provincial areas, not just urban centers."
        ),
        "source": "IJM Philippines / ECPAT / Philippine Supreme Court child witness rules",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "OSEC — Technology Facilitation and Platform Responsibility",
        "summary": (
            "Online child sexual exploitation is facilitated by encrypted messaging apps (Telegram, "
            "WhatsApp, Signal), dark web forums, and commercial payment platforms. NCMEC "
            "CyberTipline received 32.6 million reports in 2022, 98% from Meta platforms. "
            "Apple delayed CSAM detection tool deployment after privacy criticism (2021). "
            "EU's proposed CSAM detection regulation (Child Sexual Abuse Regulation, CSAR) "
            "remained contested in 2024 due to encryption concerns. WeProtect's Technology "
            "Coalition members include Google, Microsoft, Twitter/X, but dark web platforms "
            "remain largely unaddressed."
        ),
        "source": "NCMEC 2022 / WeProtect Global Alliance / EU CSAR Proposal 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "OSEC — Survivor Reintegration and Secondary Victimization Risks",
        "summary": (
            "OSEC survivors face unique reintegration challenges distinct from contact sexual "
            "abuse survivors. CSAM of the child remains in circulation online indefinitely, "
            "creating lifelong risk of re-identification and re-victimization. ECPAT recommends: "
            "(1) digital removal programs (NCMEC PhotoDNA hashing, Thorn's technology); "
            "(2) psychosocial support addressing shame and family betrayal trauma; "
            "(3) economic support to families to reduce re-exploitation risk; "
            "(4) child-friendly judicial processes preventing re-traumatization. "
            "Survivor compensation via offender proceeds is available in some jurisdictions (US, "
            "Australia) but rarely implemented in Global South contexts."
        ),
        "source": "ECPAT / IJM / UNICEF survivor-centered approaches guidance 2022",
    },

    # ── Unaccompanied Minors Trafficking ──────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Unaccompanied Migrant Children — HHS/ORR Sponsor Network Trafficking",
        "summary": (
            "US HHS Office of Inspector General (2023) and New York Times investigation (2023) "
            "found that thousands of unaccompanied minors released by HHS Office of Refugee "
            "Resettlement (ORR) to sponsors were subsequently exploited for labour. Children "
            "from Guatemala, Honduras, and El Salvador placed with sponsors (often distant "
            "acquaintances or community members) were found working in meat-processing plants "
            "(Hyundai supplier SMART Alabama), roofing, tobacco farming, and food delivery "
            "in violation of US child labour laws. DOL investigations issued USD 1.5M in "
            "penalties to companies employing migrant children (2023)."
        ),
        "source": "HHS OIG Report 2023 / NYT 'Alone and Exploited' Feb 2023 / US DOL",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Unaccompanied Minors — Trafficking Risk in EU Reception Systems",
        "summary": (
            "ECRE (European Council on Refugees and Exiles) and Missing Children Europe report "
            "that 18,000 unaccompanied minors were recorded as missing from EU reception "
            "facilities in 2021–2022. Many disappear into trafficking networks. Children from "
            "Afghanistan, Morocco, and Eritrea are most frequently missing. Greece, Italy, and "
            "France face the highest case loads. Missing children are most vulnerable in the "
            "first 48 hours after reception. Trafficking recruiters target transit points "
            "(Calais, Ventimiglia, Idomeni border areas)."
        ),
        "source": "Missing Children Europe 2022 / ECRE / Europol trafficking reports",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Best Practices — Protecting Unaccompanied Minors from Trafficking",
        "summary": (
            "UNHCR and UNICEF guidelines recommend: (1) immediate appointment of a legal guardian "
            "within 24 hours of identification; (2) age-appropriate trafficking screening within "
            "72 hours; (3) best-interests determination before any placement decision; (4) "
            "small-group residential care or vetted foster care (not congregate camps); (5) "
            "regular welfare checks within 30/60/90 days of placement; (6) secure family "
            "tracing protocols that do not expose child to return trafficking risk. Guatemala, "
            "El Salvador, and Honduras lack guardian systems — a primary driver of post-release "
            "exploitation in US sponsor networks."
        ),
        "source": "UNHCR / UNICEF Guidelines on Unaccompanied and Separated Children (2022)",
    },

    # ── Child Begging Networks ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "RO",
        "title": "Organised Child Begging Networks — Romania to Western Europe",
        "summary": (
            "Europol and national law enforcement have documented organised Romanian Roma networks "
            "trafficking children to beg in Germany, France, the UK, and Italy. Children aged "
            "4–14 are forced to beg on streets, in metros, and at tourist sites. Parents receive "
            "a daily quota payment; children are punished (sometimes physically harmed) if they "
            "fail to meet targets. In some cases children are deliberately maimed to increase "
            "begging income. Operation Webmaster (Europol, 2019) dismantled a network operating "
            "in 5 EU countries, rescuing 47 children."
        ),
        "source": "Europol Operation Webmaster 2019 / La Strada International",
    },
    {
        "type": "case_study",
        "jurisdiction": "MA",
        "title": "Child Begging Networks — Morocco (Marrakech and Fes Medinas)",
        "summary": (
            "Save the Children and INSAF (Morocco) document organised child begging networks "
            "in Marrakech, Fes, and Casablanca medinas. Children trafficked from rural Souss-"
            "Massa and Atlas mountain areas to tourist centres. Boys aged 8–15 beg near mosques, "
            "souks, and riads; some are sexually exploited by foreign tourists ('sex tourism "
            "begging circuits'). Networks controlled by adult males who collect daily earnings. "
            "Moroccan Kafala child guardianship system has been misused to place unrelated children "
            "with controlling adults."
        ),
        "source": "Save the Children Morocco / INSAF / US TIP Report Morocco",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Child Begging Networks — Bangladesh (Dhaka Syndicates)",
        "summary": (
            "Dhaka is documented to have organised child begging networks controlled by adult "
            "gang members who recruit, transport, and deploy children from Char (river island) "
            "areas and Rohingya refugee camps. Children pay a daily cut to the network controller. "
            "Some children are deliberately disabled (limbs broken or burned) to increase "
            "begging income. Dhaka's Kamalapur railway station and Sadarghat river terminal "
            "are primary trafficking and deployment points. Bangladesh National Women Lawyers "
            "Association (BNWLA) operates a shelter near Kamalapur with legal aid."
        ),
        "source": "BNWLA / UNICEF Bangladesh / US DOL ILAB Bangladesh Report",
    },

    # ── Baby Factories ─────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Baby Factories — Nigeria (Anambra, Imo, Delta States)",
        "summary": (
            "Baby factories are clandestine facilities where girls and women are held to produce "
            "babies for sale. Documented extensively in southeastern Nigeria (Anambra, Imo, Delta, "
            "Rivers states). Young women — often recruited with false promises of employment or "
            "education — are imprisoned, repeatedly impregnated (sometimes by rape), and their "
            "babies sold for USD 200–5,000. Babies are sold for adoption, ritual purposes, or "
            "trafficking. Nigeria police have raided 20+ baby factories since 2011. Operation "
            "Baruna (NAPTIP, 2017) rescued 39 women and 11 newborns from a single facility "
            "in Imo State."
        ),
        "source": "NAPTIP Nigeria / UNODC Nigeria / Thomson Reuters Foundation investigations",
    },
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Baby Factory Supply Chain — Ritual Use and International Trafficking",
        "summary": (
            "Nigerian law enforcement investigations have linked baby factory output to: "
            "(1) illegal domestic adoption market (infertile couples paying USD 2,000–5,000); "
            "(2) 'juju' ritual practices (infants used in traditional belief-based ceremonies); "
            "(3) international trafficking networks moving infants to Europe (Italy, UK) under "
            "fraudulent adoption papers. Italian anti-mafia units documented Nigerian-Italian "
            "trafficking of infants via Libya and Morocco. NAPTIP estimates baby factory "
            "operations netted NGN 50M–300M (USD 30,000–200,000) annually per facility before "
            "disruption."
        ),
        "source": "NAPTIP / Guardia di Finanza Italy / UNODC Nigeria baby factory report 2019",
    },

    # ── Surrogacy Trafficking ──────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Surrogacy Trafficking — Exploitation of Women and Children",
        "summary": (
            "The global commercial surrogacy industry is estimated at USD 14 billion annually "
            "but is largely unregulated. Trafficking patterns include: (1) recruitment of poor "
            "women with deceptive promises (Thailand, India, Cambodia, Ukraine, Georgia); "
            "(2) coercive control during pregnancy (passport confiscation, confined movement); "
            "(3) sale of children born to trafficked surrogates; (4) 'baby farming' — women "
            "repeatedly used as surrogates without informed consent. India banned commercial "
            "surrogacy for foreign nationals (2015), Cambodia banned all surrogacy (2016), "
            "Thailand banned commercial surrogacy (2015) after the Baby Gammy case."
        ),
        "source": "UNODC / Hague Conference on Private International Law (HCCH) 2023 / IJM",
    },
    {
        "type": "case_study",
        "jurisdiction": "UA",
        "title": "Ukraine — Surrogacy Industry and Trafficking Vulnerability Post-2022",
        "summary": (
            "Ukraine was one of the world's largest commercial surrogacy markets before the "
            "2022 Russian invasion. Biotexcom, the largest Ukrainian surrogacy agency, faced "
            "trafficking allegations for exploiting economically desperate women with incomplete "
            "information. Post-invasion, surrogacy contracts were disrupted; hundreds of newborns "
            "were stranded in Ukrainian maternity facilities. La Strada Ukraine documented cases "
            "of surrogates being displaced mid-pregnancy. War conditions dramatically increase "
            "surrogacy trafficking risk: women fleeing conflict are targeted by recruiters at "
            "EU borders with surrogacy-as-employment offers."
        ),
        "source": "La Strada Ukraine / HCCH Study 2023 / Biotexcom investigations",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "HCCH — Parentage and Surrogacy Project (Draft Convention 2023)",
        "summary": (
            "The Hague Conference on Private International Law (HCCH) is developing a draft "
            "convention on international surrogacy arrangements to address legal parentage "
            "uncertainty and trafficking risks. The 2023 draft proposes: (1) minimum standards "
            "for surrogacy agreements (informed consent, independent legal advice, minimum age "
            "25 for surrogate); (2) prohibition of commercial surrogacy as an option states "
            "may implement; (3) child's right to know origins; (4) trafficking safeguards in "
            "cross-border recognition of parentage. Convention not yet open for signature."
        ),
        "source": "HCCH Parentage and Surrogacy Project — Draft Convention 2023",
    },

    # ── Child Marriage as Trafficking ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Child Marriage as Trafficking — Bride Price and Sale",
        "summary": (
            "Child marriage meets the Palermo Protocol trafficking definition when: a child under "
            "18 is transferred in exchange for payment (bride price), with deception about what "
            "the marriage entails, involving exploitation (forced domestic labour, sexual servitude, "
            "reproductive exploitation). This pattern is documented in Ethiopia (Amhara region), "
            "South Sudan, Niger, Mali, Somalia, Bangladesh (acid attack threat to force consent), "
            "and among displaced populations globally. Bride prices of USD 50–500 function as "
            "purchase price; girls as young as 8 are affected. GirlsNotBrides and UNICEF "
            "document the trafficking-marriage nexus across 50+ countries."
        ),
        "source": "Girls Not Brides / UNICEF / UNODC Trafficking and Child Marriage Nexus 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "YE",
        "title": "Child Marriage Surge in Yemen War — Trafficking Dimension",
        "summary": (
            "UNICEF reports that child marriage in Yemen increased dramatically with the ongoing "
            "conflict (since 2015). Pre-war rate: 32%. UNICEF's 2021 assessment found rates "
            "approaching 70% in some war-affected governorates. Girls as young as 8 are being "
            "married to older men — sometimes to reduce the family's financial burden, sometimes "
            "for reported bride prices. Families displaced by conflict are particularly "
            "vulnerable. Some girls are married to fighters or trafficked across borders "
            "to Saudi Arabia, Oman, and Djibouti under the guise of marriage."
        ),
        "source": "UNICEF Yemen / Save the Children Yemen / Girls Not Brides 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Child Marriage in Bangladesh — COVID-19 Regression",
        "summary": (
            "Bangladesh has the highest rate of child marriage in Asia and the fourth highest "
            "globally (59% of women married before 18). The Child Marriage Restraint Act (2017) "
            "retained an unexplained 'special circumstances' exception allowing marriage below "
            "18 with parental consent and court approval — widely criticised as a loophole. "
            "UNICEF estimates COVID-19 pushed 500,000 additional girls into early marriage in "
            "Bangladesh (2020–2021) due to school closures and economic shock. Girls Not Brides "
            "Bangladesh documented dowry threats, acid attack fears, and perceived safety-through-"
            "marriage dynamics driving families to arrange early marriages."
        ),
        "source": "UNICEF Bangladesh / Girls Not Brides / Child Marriage Restraint Act 2017",
    },

    # ── Orphanage Trafficking and Voluntourism ─────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Orphanage Trafficking — Cambodia (Siem Reap and Phnom Penh)",
        "summary": (
            "UNICEF Cambodia estimates 75% of children in Cambodian orphanages have at least "
            "one living parent. Orphanage operators in Siem Reap and Phnom Penh recruit children "
            "from rural families with promises of free education, then use children to attract "
            "foreign donor funding and volunteer tourist fees (USD 20–50/week volunteering). "
            "Children are kept in deliberately poor conditions to elicit sympathy and donations. "
            "Sexual abuse of children by volunteer tourists has been documented by ECPAT. "
            "Cambodia enacted the Child Care Law (2021) to strengthen deinstitutionalisation, "
            "but enforcement lags behind the commercial incentive structure."
        ),
        "source": "UNICEF Cambodia / Lumos Foundation / ECPAT Cambodia",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Orphanage Trafficking — Nepal Post-Earthquake (2015)",
        "summary": (
            "After the 2015 Nepal earthquake (9,000 deaths), a surge in orphanage openings in "
            "Kathmandu was documented by Lumos Foundation and Terre des Hommes Nepal. Children "
            "recruited from rural earthquake-affected districts to Kathmandu 'orphanages' "
            "designed to capture Western volunteer tourist spending. US State Dept TIP Report "
            "2019 placed Nepal on Watch List partly due to orphanage trafficking. Nepal's "
            "Children Act (2018) requires family-based alternative care but orphanage "
            "deinstitutionalisation has been slow due to donor funding incentives favouring "
            "residential care."
        ),
        "source": "Lumos Foundation Nepal / Terre des Hommes Nepal / US TIP Report 2019",
    },
    {
        "type": "law",
        "jurisdiction": "AU",
        "title": "Australia — Orphanage Trafficking Criminal Offence (2019)",
        "summary": (
            "Australia's Criminal Code Amendment (Protecting Minors Online) Act 2018 and "
            "subsequent regulations (effective 2019) criminalised 'conduct relating to child "
            "protection tourism' including voluntourism at fraudulent orphanages. Australian "
            "Federal Police (AFP) Operation Render targeted Australian nationals financing "
            "and visiting exploitative orphanages in Cambodia and Nepal. Maximum sentence: "
            "12 years imprisonment. Australia is the first country to specifically criminalise "
            "orphanage trafficking as a category. The approach is recommended as a model by "
            "UNICEF and Lumos for other Western donor countries."
        ),
        "source": "Criminal Code Amendment Act 2018 (Australia) / AFP Operation Render",
    },

    # ── Debt Bondage and Advance Payment Systems Specific to Children ──────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Advance Payment — How Child Debt Bondage Works",
        "summary": (
            "Child debt bondage typically operates through an advance payment (peshgi, kamaiya, "
            "asika, system wage) paid to parents in exchange for a child's labour. The advance "
            "functions as a debt the child 'owes' the employer; the child cannot leave until "
            "it is repaid, but wages are so low, deductions so frequent, and interest so high "
            "that repayment is practically impossible. This mechanism is documented identically "
            "across brick kilns (South Asia), fishing (Lake Volta), agriculture (sub-Saharan "
            "Africa), domestic work (Southeast Asia), and carpet weaving (Central Asia). It is "
            "distinct from adult debt bondage only in that the child had no agency in incurring "
            "the debt."
        ),
        "source": "ILO Forced Labour and Debt Bondage / Anti-Slavery International",
    },

    # ── Education Deprivation as Trafficking Indicator ─────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Education Deprivation — Key Trafficking Identification Indicator",
        "summary": (
            "ILO and UNICEF use school non-attendance as a primary child labour and trafficking "
            "indicator. 28% of child labourers aged 5–11 do not attend school at all. 40% of "
            "those aged 12–14 in child labour are out of school. Trafficked children in domestic "
            "service, fishing, agriculture, and brick kilns typically receive zero schooling. "
            "Child protection referral systems in schools (school welfare officers) are recommended "
            "by UNICEF as a primary identification mechanism. Conditional cash transfer programs "
            "linking poverty alleviation to school attendance (Brazil Bolsa Família, Mexico "
            "Progresa/Oportunidades) have demonstrated effectiveness in reducing child labour."
        ),
        "source": "ILO-UNICEF 2021 / UNICEF Education and Child Labour Guidelines",
    },

    # ── Identification and Screening ──────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Trafficking Identification — Key Indicators",
        "summary": (
            "UNODC and IOM joint guidelines identify the following primary indicators of child "
            "trafficking: (1) child appears malnourished, fatigued, or unkempt; (2) does not "
            "know address where living; (3) is accompanied by a controlling adult who answers "
            "on their behalf; (4) carries documents belonging to another person; (5) shows "
            "signs of physical abuse or sexual abuse; (6) is not in school during school hours; "
            "(7) has tattoos or branding (commercial sexual exploitation); (8) describes "
            "working excessively long hours; (9) expresses fear of deportation or authority; "
            "(10) does not speak the local language. A child need not show all indicators."
        ),
        "source": "UNODC / IOM Child Trafficking Indicators Tool 2009 (updated 2020)",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Age Assessment — Best Practices for Unaccompanied Children",
        "summary": (
            "When a child's age is disputed, UNICEF and UNHCR recommend: (1) benefit of the "
            "doubt — treat as a child if doubt exists; (2) multi-disciplinary holistic assessment "
            "(psychosocial, documentary, medical) rather than medical-only; (3) medical assessments "
            "(bone density, dental X-ray) have wide age ranges (±2–3 years) and should not be "
            "used as the sole determinant; (4) cultural and nutritional factors affecting physical "
            "development must be considered; (5) assessments must be conducted in a language "
            "the child understands, with an independent interpreter. Wrongly classifying a "
            "child as an adult removes all child-specific protections."
        ),
        "source": "UNICEF / UNHCR Age Assessment Guidelines / Council of Europe 2014",
    },

    # ── Prosecution and Accountability ────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "US v. Hyundai Metia / SMART Alabama — Child Labour (2023)",
        "summary": (
            "In 2023, US Department of Labour and Department of Justice investigated SMART Alabama "
            "(a Hyundai supplier producing parts for Hyundai and Kia vehicles) following NYT "
            "investigations revealing migrant children — some as young as 13 — working overnight "
            "shifts in violation of US child labour laws. DOL found children employed through "
            "staffing agencies; assessed USD 300,000 in civil penalties against SMART. Hyundai "
            "terminated the supplier relationship. DOJ did not file criminal charges against "
            "corporate officers. Case highlighted gaps in US child labour enforcement in "
            "automotive supply chains."
        ),
        "source": "US DOL WHD / DOJ / NYT investigation 2023",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "international",
        "title": "ICC — Child Soldier Prosecutions (Lubanga, Ntaganda, Ongwen)",
        "summary": (
            "Three landmark ICC convictions for use of child soldiers: (1) Thomas Lubanga Dyilo "
            "(DRC): convicted 2012 for conscripting/enlisting children under 15 — first ICC "
            "conviction, 14-year sentence; (2) Bosco Ntaganda (DRC): convicted 2019 for child "
            "soldier use and sexual violence against child soldiers — 30-year sentence; "
            "(3) Dominic Ongwen (Uganda/LRA): convicted 2021 for forced marriage, sexual "
            "enslavement, and use of child soldiers — 25-year sentence. These cases established "
            "that child soldier recruitment is a war crime prosecutable at international level."
        ),
        "source": "ICC Lubanga (2012) / ICC Ntaganda (2019) / ICC Ongwen (2021)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Philippines — OSEC Landmark Conviction (People v. Ejercito, 2020)",
        "summary": (
            "Philippines Regional Trial Court convicted Benjamin Ejercito under RA 9775 "
            "(Anti-Child Pornography Act) for facilitating live-streaming sexual abuse of his "
            "own children to foreign offenders via webcam. Sentenced to reclusion perpetua "
            "(life imprisonment). Case was prosecuted with digital evidence provided by "
            "Australian Federal Police and IJM Philippines. Represents the first conviction "
            "under the expanded OSEC provisions and set precedent for family-perpetrator "
            "OSEC cases. AFP-IJM collaboration model was subsequently adopted by NBI-ACES "
            "as standard operating procedure."
        ),
        "source": "People v. Ejercito, RTC Manila (2020) / IJM Philippines",
    },

    # ── Supply Chain Due Diligence for Child Labour ───────────────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Corporate Sustainability Due Diligence Directive — Child Labour (2024)",
        "summary": (
            "CSDDD (EU Directive 2024/1760) requires companies with 1,000+ employees and EUR "
            "450M+ global turnover to conduct human rights and environmental due diligence "
            "across their supply chains. Child labour is explicitly listed as a covered harm. "
            "Companies must: identify risks, implement prevention/remediation measures, "
            "establish grievance mechanisms, and report annually. Penalties: up to 5% of global "
            "net turnover. Civil liability for harm. Phased implementation 2027–2029. Covers "
            "cocoa, cobalt, mica, garments, and other high-risk sectors. Complements the "
            "EU Forced Labour Regulation (2024) which bans import of forced-labour goods."
        ),
        "source": "EU CSDDD Directive 2024/1760 / EU Forced Labour Regulation 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Labour Due Diligence — Sector-Specific Monitoring Tools",
        "summary": (
            "Key sector-specific monitoring tools for child labour due diligence: "
            "(1) Cocoa: Cocoa & Forests Initiative CLMRS (Child Labour Monitoring and Remediation "
            "System) — survey-based, covers 40% of farms in Cote d'Ivoire/Ghana; "
            "(2) Cobalt: OECD/RMI Cobalt Reporting Template + IPIS mine-level mapping; "
            "(3) Mica: Responsible Mica Initiative third-party audits; "
            "(4) Garments: Better Work program (ILO/IFC) in Vietnam, Bangladesh, Cambodia; "
            "(5) Carpets: GoodWeave unannounced inspections; "
            "(6) Agriculture generally: SMETA (Sedex Members Ethical Trade Audit) — widely used "
            "but criticism of audit-shopping and limited unannounced visits."
        ),
        "source": "ILO / Responsible Mica Initiative / GoodWeave / Better Work / Sedex",
    },

    # ── Reintegration and Rehabilitation ──────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Trafficking Survivors — Reintegration Best Practices",
        "summary": (
            "UNICEF, IOM, and ILO recommend a child-centred reintegration approach: "
            "(1) safety assessment before return to family of origin; "
            "(2) trauma-informed psychosocial support from a trained child psychologist; "
            "(3) family strengthening — address poverty drivers to prevent re-trafficking; "
            "(4) accelerated education or vocational training appropriate to age; "
            "(5) economic support to family (cash transfer or livelihood program); "
            "(6) follow-up visits at 30, 90, and 180 days post-reintegration; "
            "(7) community sensitisation to reduce stigma. "
            "Without economic intervention, re-trafficking rates in the first year exceed 30% "
            "in high-risk corridors (IJM data)."
        ),
        "source": "UNICEF / IOM / ILO Child Reintegration Guidelines / IJM",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Soldier Reintegration — DDR Best Practices",
        "summary": (
            "UNICEF's guidelines on Disarmament, Demobilisation, and Reintegration (DDR) for "
            "children: (1) formal weapons surrender should not be required for children — they "
            "are victims, not combatants; (2) interim care centres rather than cantonment with "
            "adults; (3) family tracing within 72 hours; (4) education or vocational training "
            "as primary reintegration pathway; (5) psychosocial support for trauma, grief, and "
            "perpetrator guilt; (6) community reconciliation processes (traditional justice "
            "where appropriate); (7) economic support to receiving families. Girls (often "
            "former 'bush wives') require gender-specific support and face additional "
            "stigmatisation challenges."
        ),
        "source": "UNICEF Paris Principles (2007) / UNDPKO DDR Guidelines / Geneva Call",
    },

    # ── Technology and Child Trafficking ──────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Social Media Recruitment of Minors for Sex Trafficking",
        "summary": (
            "US DOJ and NCMEC report that social media platforms are the primary recruitment "
            "tool for domestic minor sex trafficking in the United States. Instagram, Snapchat, "
            "and TikTok are most frequently cited in law enforcement cases. Traffickers use "
            "romantic relationships ('loverboy/romeo pimp' model) or friendship to establish "
            "trust before exploitation. Average age at recruitment: 15 (Polaris Project). "
            "FBI Operation Cross Country (2022) rescued 200+ minors across 30 US cities, "
            "with social media recruitment documented in 80% of cases. EU Europol reports "
            "similar patterns in Netherlands, Belgium, and Germany."
        ),
        "source": "US DOJ / NCMEC / Polaris Project / FBI Operation Cross Country 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Child Trafficking via Gaming Platforms and Discord",
        "summary": (
            "NCMEC and Thorn (2023) identified gaming platforms (Fortnite, Roblox, Minecraft) "
            "and Discord as emerging child trafficking recruitment channels. Traffickers build "
            "relationships with minors over weeks, then migrate communication to encrypted apps. "
            "Children are offered money, gaming credits, or gifts in exchange for sexual images "
            "— a gateway to CSAM production and in-person trafficking. Roblox reported 25M "
            "safety incidents in 2022. Discord added CSAM reporting tools in 2021 following "
            "investigative journalism exposing the platform's use in child exploitation networks."
        ),
        "source": "Thorn 'Survivor Insights' 2023 / NCMEC / Roblox Safety Report 2022",
    },

    # ── Regional Specifics ────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Child Labour in Brazil — Sugarcane and Domestic Work",
        "summary": (
            "Brazil has made significant progress reducing child labour (from 8M in 1992 to "
            "1.8M in 2019) through Bolsa Família conditional cash transfers and PETI (Child "
            "Labour Eradication Program). However, 1.8 million children remain in child labour, "
            "concentrated in family agriculture (sugarcane, tobacco, orange, coffee), domestic "
            "work, and street work. Amazonian Quilombola and Indigenous communities face "
            "highest rates. Brazil Penal Code Art. 149 criminalises slavery-like conditions; "
            "the 'dirty list' (lista suja) publicly identifies employers using slave/child labour "
            "and triggers credit restrictions."
        ),
        "source": "ILO Brazil / IBGE Child Labour Survey 2019 / Ministry of Labour Dirty List",
    },
    {
        "type": "case_study",
        "jurisdiction": "ET",
        "title": "Child Trafficking in Ethiopia — Domestic Work and Almajiri-Like Systems",
        "summary": (
            "Ethiopia has an estimated 1.1 million child domestic workers under 18, many "
            "trafficked from rural Oromia, Amhara, and SNNPR regions to Addis Ababa. The "
            "'deresha' system (sending a child to a relative or employer in the city) parallels "
            "the Haitian restavek pattern. Children receive minimal or no wages; education "
            "is denied. Ethiopian Women Lawyers Association (EWLA) provides legal aid for "
            "child trafficking survivors. Ethiopia's anti-trafficking law (Proclamation 909/2015) "
            "criminalises trafficking with 5–25 year sentences but domestic child labour "
            "trafficking prosecutions remain rare."
        ),
        "source": "EWLA / ILO Ethiopia / US TIP Report Ethiopia 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Child Trafficking in India — Inter-State Domestic Work",
        "summary": (
            "India has one of the world's largest child domestic worker populations: estimates "
            "range from 300,000 to 2 million. Children trafficked from Jharkhand, Odisha, "
            "Chhattisgarh, and West Bengal to Delhi, Mumbai, and Chennai. Traffickers pose as "
            "labour agents, charging families fees and promising schooling. Children are confined "
            "in employers' homes, salaries withheld, passports not applicable (domestic), but "
            "ration cards and identity documents withheld. Indian Ministry of Women and Child "
            "Development's CHILDLINE 1098 helpline handles 35+ million calls annually, with "
            "child labour and trafficking comprising a major category."
        ),
        "source": "CHILDLINE India Foundation / CRY / ILO India / National Crime Records Bureau",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Child Trafficking in Thailand — Cross-Border from Myanmar and Laos",
        "summary": (
            "Thailand's border with Myanmar (Mae Sot, Mae Hong Son, Ranong) and Laos (Chiang "
            "Khong, Nong Khai) are major child trafficking entry points. Children trafficked "
            "into fishing (especially Gulf of Thailand), agriculture (sugarcane, rubber), "
            "domestic work, and commercial sexual exploitation. Myanmar conflict since 2021 "
            "dramatically increased cross-border child trafficking. Thailand's Anti-Trafficking "
            "in Persons Act (2008, amended 2017) covers children; Thailand moved to Tier 2 "
            "Watch List in US TIP Report 2020. ECPAT Thailand documents sexual exploitation "
            "of children in Pattaya and Phuket tourist areas."
        ),
        "source": "ECPAT Thailand / IOM Thailand / US TIP Report Thailand 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "SO",
        "title": "Al-Shabaab Child Soldier Recruitment — Somalia and Kenya",
        "summary": (
            "Al-Shabaab recruits children from internally displaced persons (IDP) camps in "
            "southern Somalia and from Dadaab refugee camp in Kenya. Children as young as "
            "10 are recruited through forced conscription or economic inducement (payments "
            "of USD 50–100 to families). Children are used as fighters, bombers, and "
            "intelligence gatherers. Former Al-Shabaab child soldiers face terrorism stigma "
            "preventing reintegration. UNICEF and UNHCR report that rescued children are "
            "sometimes detained in adult prison conditions pending prosecution — a secondary "
            "rights violation. UN Security Council Resolution 2444 (2018) calls for specialised "
            "child-sensitive DDR for Al-Shabaab affected children."
        ),
        "source": "UN SGACC / UNICEF Somalia / HRW Somalia",
    },

    # ── COVID-19 and Climate — Child Trafficking Vulnerability ────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "COVID-19 — Impact on Child Labour and Trafficking (2020–2022)",
        "summary": (
            "UNICEF and ILO estimate COVID-19 pushed 8.9 million additional children into "
            "child labour between 2020 and 2022. Drivers: school closures (1.6 billion students "
            "affected), household income loss, collapse of family livelihoods in tourism and "
            "informal sectors. Child marriage surged in sub-Saharan Africa, South Asia, and "
            "Latin America during lockdowns. Online child sexual exploitation increased "
            "substantially with children home alone and online. Food insecurity pushed families "
            "in Ethiopia, Malawi, and Bolivia to withdraw children from school for labour. "
            "Child protection funding cuts in humanitarian operations compounded vulnerability."
        ),
        "source": "UNICEF / ILO COVID-19 and Child Labour Impact Assessment 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Climate Migration — Child Trafficking Risk in Climate-Displaced Populations",
        "summary": (
            "IOM estimates 216 million internal climate migrants by 2050, disproportionately "
            "affecting children. Climate-related displacement dramatically increases child "
            "trafficking risk: families separated in floods and cyclones, children in "
            "displacement camps outside school, households with destroyed livelihoods. "
            "Bangladesh char island children displaced by erosion are trafficked to Dhaka "
            "brick kilns and garment factories. Pacific island children displaced by sea-level "
            "rise to Fiji and Papua New Guinea face exploitation risks. UNODC recommends "
            "child protection mainstreaming in all climate adaptation and disaster response plans."
        ),
        "source": "IOM / UNODC / World Bank 'Groundswell' 2021",
    },

    # ── Kafala and Child Exploitation in Gulf ─────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Child Domestic Workers Under Kafala in Saudi Arabia",
        "summary": (
            "Saudi Arabia has no minimum age for domestic workers in law, creating conditions "
            "for child domestic worker trafficking. Girls as young as 14 from Indonesia, "
            "Philippines, Ethiopia, and Kenya have been documented in Saudi households. Kafala "
            "system ties domestic workers (including children) to their employer sponsor, "
            "making escape legally and practically impossible. Saudi Arabia enacted partial "
            "domestic worker regulations (2013) but domestic workers remain excluded from the "
            "Labour Law. US TIP Report 2022 ranked Saudi Arabia Tier 2, noting continued "
            "failure to investigate employers of trafficked children."
        ),
        "source": "US TIP Report Saudi Arabia 2022 / HRW / Migrant-Rights.org",
    },

    # ── Further Sector-Specific Facts ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Child Labour in Gold Mining — West Africa and Latin America",
        "summary": (
            "US DOL identifies gold mining as a top child labour commodity, present in 13 "
            "countries. Artisanal and small-scale gold mining (ASGM) in Ghana, Mali, Burkina "
            "Faso, Tanzania, DRC, Peru, Bolivia, and Philippines employs children. Children "
            "dive into flooded pits, carry heavy ore, and use mercury amalgamation (causing "
            "neurological damage from mercury vapour exposure). In Burkina Faso's Sahel region, "
            "ASGM sites are directly adjacent to Al-Qaïda and JNIM controlled territory, "
            "adding forced recruitment risk. Fairtrade and RJC (Responsible Jewellery Council) "
            "certification do not adequately cover ASGM in conflict-affected areas."
        ),
        "source": "US DOL ILAB / Levin Sources / RJC / Fairtrade International",
    },
    {
        "type": "case_study",
        "jurisdiction": "PE",
        "title": "Child Labour in Peru — Artisanal Gold Mining (Madre de Dios)",
        "summary": (
            "Madre de Dios region in the Peruvian Amazon has the largest illegal gold mining "
            "operation in Latin America, employing an estimated 30,000 miners including "
            "children. Children work in mercury processing and carry sacks of ore in open "
            "mines. The same mining camps are associated with commercial sexual exploitation "
            "of women and girls (documented by ILO and Peru's MINJUS). Peru enacted Law "
            "30309 (2015) offering tax benefits to companies investing in anti-trafficking "
            "programs. Illegal mining deforestation also destroys Indigenous communities' "
            "food security, indirectly pushing children into labour."
        ),
        "source": "ILO Peru / US DOL ILAB / Peru Ministry of Justice Anti-Trafficking Report",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Child Labour in India — Cotton Seed Pollination (Andhra Pradesh)",
        "summary": (
            "Hybrid cotton seed production in Andhra Pradesh and Telangana employs an estimated "
            "450,000 children (primarily girls) aged 7–14 in cross-pollination of cotton plants. "
            "Children perform the delicate manual task (removing stamens, applying pollen) more "
            "cheaply than adults. Pesticide exposure is severe — children spray organophosphates "
            "without protective equipment. CRY (Child Rights and You) and US DOL have documented "
            "the practice for over two decades. Some cotton seed companies (Mahyco, Bayer-"
            "subsidiary Nunhems) established monitoring programs after international NGO pressure; "
            "independent audits show partial compliance."
        ),
        "source": "CRY India / US DOL ILAB / Bayer Crop Science audit reports / ILO India",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Child Labour in Tea Estates — India, Sri Lanka, Kenya",
        "summary": (
            "Tea estate child labour is documented in Darjeeling and Assam (India), central "
            "highlands of Sri Lanka, and Kericho region (Kenya). Estate Tamil communities in "
            "Sri Lanka face statelessness-related vulnerability: without citizenship, parents "
            "have reduced legal standing to protect children. Children pluck tea alongside "
            "parents to help meet weight quotas. Fairtrade-certified estates have measurably "
            "lower child labour rates, but Fairtrade covers only 3% of global tea production. "
            "ETI (Ethical Trading Initiative) Base Code requires member companies to assess "
            "child labour in tea supply chains."
        ),
        "source": "ILO / ETI / Fairtrade International Tea Sector Report 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Child Labour in Philippine Sugarcane — Negros Occidental",
        "summary": (
            "Negros Occidental in the Philippines is a major sugar-producing province with "
            "documented child labour. Children of sugarcane workers (sacadas) accompany parents "
            "to hacienda farms and work cutting, loading, and hauling cane. Minimum age law: "
            "15 (Philippines RA 7658). DOLE (Dept of Labour) reports enforcement is practically "
            "absent on private haciendas. Children exposed to machete injuries, pesticide "
            "exposure, and extreme heat. Philippine government's ELCAC (End Local Communist "
            "Armed Conflict) program in Negros has a child protection component but focuses "
            "primarily on counterinsurgency."
        ),
        "source": "DOLE Philippines / Philippine Statistics Authority / US DOL ILAB Philippines",
    },
    {
        "type": "case_study",
        "jurisdiction": "UZ",
        "title": "Cotton Harvest Child Labour — Uzbekistan (Post-Reform Period)",
        "summary": (
            "Uzbekistan historically mobilised students and public-sector workers (including "
            "children) en masse for cotton harvest via state coercion. Under sustained pressure "
            "from the Cotton Campaign coalition and international buyers threatening trade "
            "sanctions, Uzbekistan significantly reduced child labour in cotton: verified cases "
            "fell from hundreds of thousands to near-zero in 2022 (Cotton Campaign 2022 report). "
            "Forced adult labour persists. The Uzbek case is a model of how coordinated "
            "international pressure (consumer boycotts, diplomatic engagement, monitoring) "
            "can achieve rapid improvement in child labour metrics."
        ),
        "source": "Cotton Campaign / ILO Third-Party Monitoring Uzbekistan 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Child Labour in Tobacco — Indonesia and Zimbabwe",
        "summary": (
            "Beyond Malawi, child tobacco labour is documented in Indonesia (Lombok, East Java) "
            "and Zimbabwe. In Indonesia, an estimated 1.5 million children work in tobacco "
            "farming (Human Rights Watch 2016). Green Tobacco Sickness from wet leaf handling "
            "is prevalent. Philip Morris International's Indonesia operations drew HRW attention "
            "for failing to address child labour among independent farmers supplying the company "
            "despite having contractual leverage. Zimbabwe's tobacco sector employs children "
            "on communal land farms and on commercial estates in seasonal labour arrangements."
        ),
        "source": "HRW 'The Harvest is In My Blood' 2016 / US DOL Zimbabwe Tobacco Report",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO IPEC / IPEC+ — Child Labour Elimination Programs",
        "summary": (
            "ILO's International Programme on the Elimination of Child Labour (IPEC, 1992–2013) "
            "was succeeded by IPEC+ (2019–present), targeting elimination of child labour by "
            "2025 (SDG 8.7). IPEC+ operates in 16 countries with USD 150M+ in programming. "
            "Key approaches: (1) legislative reform and enforcement capacity building; "
            "(2) conditional cash transfers to poor families; (3) accelerated education for "
            "child labour survivors; (4) awareness campaigns; (5) social protection systems. "
            "SDG 8.7 target of ending child labour by 2025 is widely assessed as off-track "
            "given COVID-19 setbacks and the 2020 increase in global child labour figures."
        ),
        "source": "ILO IPEC+ / SDG 8.7 Alliance / UN SDG Progress Report 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Labour and Armed Conflict — Nexus and Overlap",
        "summary": (
            "Armed conflict is a primary driver of child labour and child trafficking. UNICEF's "
            "Monitoring and Reporting Mechanism (MRM) documents six grave violations including "
            "recruitment and use in armed conflict, sexual violence, killing and maiming. "
            "Conflict displaces families, destroys livelihoods, collapses school systems, "
            "and removes state protection capacity. Children in conflict-affected areas are "
            "significantly more likely to be in child labour (3x in active conflict zones "
            "per UNICEF 2021). DRC, Yemen, South Sudan, Afghanistan, and the Sahel have the "
            "worst overlap of conflict and child labour."
        ),
        "source": "UNICEF MRM / Save the Children 'Stop the War on Children' 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Trafficking and Disability — Double Vulnerability",
        "summary": (
            "Children with disabilities face compounded trafficking vulnerability: (1) traffickers "
            "deliberately disable children (break limbs, blind with chemicals) to increase "
            "begging income — documented in Bangladesh, Nigeria, and Eastern Europe; (2) children "
            "with existing disabilities are targeted for exploitation precisely because families "
            "are more likely to accept economic exploitation offers; (3) deaf and mute children "
            "are specifically targeted as CSAM victims because they cannot report abuse verbally. "
            "UNICEF estimates children with disabilities face 3–4x greater risk of violence "
            "and 10x greater risk of sexual abuse than non-disabled peers."
        ),
        "source": "UNICEF / WHO / Global Campaign for Equal Citizenship disability and trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Stateless Children — Extreme Vulnerability to Trafficking",
        "summary": (
            "Stateless children (without citizenship documentation) face the most acute "
            "trafficking vulnerability. Unable to enrol in school, access healthcare, or "
            "obtain identity documents, stateless children are outside all protective systems. "
            "Groups at risk: Rohingya (Myanmar/Bangladesh), Tamil estate workers (Sri Lanka), "
            "Haitian descendants in Dominican Republic, Bidun (Kuwait/UAE), Nubians (Kenya). "
            "UNHCR estimates 4 million stateless children globally. Without birth registration, "
            "age cannot be verified — enabling age falsification to deploy children as adults. "
            "UNHCR's #IBelong Campaign (2014–2024) aimed to end statelessness but target is "
            "off-track."
        ),
        "source": "UNHCR / UNICEF Birth Registration / UNHCR #IBelong Campaign 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Trafficking — Prosecution Challenges and Accountability Gaps",
        "summary": (
            "UNODC data show that fewer than 15% of countries reported more than 10 trafficking "
            "convictions per year (2022). Child trafficking cases face specific prosecution "
            "barriers: (1) child witnesses require special measures (video testimony, child-"
            "friendly courts) that many justice systems lack; (2) child survivors often "
            "recant testimony due to family pressure or trauma; (3) traffickers within families "
            "are rarely prosecuted due to cultural norms; (4) digital evidence in OSEC cases "
            "requires specialist technical capacity; (5) international cooperation for cross-"
            "border child trafficking cases is slow and under-resourced. Impunity remains "
            "the norm globally."
        ),
        "source": "UNODC Global Report on Trafficking 2022 / ECPAT / Interpol",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Trafficking Prevention — Community-Based Models",
        "summary": (
            "Evidence-based community prevention programs for child trafficking include: "
            "(1) Community Child Protection Committees (CPC) — village-level monitoring "
            "of school attendance and child movements (effective in Ghana, Tanzania, Cambodia); "
            "(2) community women's savings groups linked to child labour monitoring (BRAC "
            "model in Bangladesh); (3) male engagement programs challenging norms that "
            "normalize child labour and child marriage; (4) mobile birth registration campaigns "
            "providing identity documents as protection against trafficking; (5) community-based "
            "reintegration support for child labour survivors (ECPAT, IJM). Prevention is "
            "consistently more cost-effective than rescue and rehabilitation."
        ),
        "source": "ILO IPEC+ / UNICEF / IJM / ECPAT Community Prevention Toolkit",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Trafficking — Financing and Economic Scale",
        "summary": (
            "ILO estimates forced child labour generates USD 150 billion in illegal profits "
            "annually (as part of the USD 236 billion total forced labour economy). Commercial "
            "sexual exploitation of children accounts for USD 99 billion of this total. "
            "Domestic child trafficking (within national borders) is harder to quantify but "
            "is believed to exceed cross-border child trafficking in most regions. The "
            "economic model of child trafficking relies on low acquisition costs (advance "
            "payments to families), high control leverage (isolation, debt, threats), and "
            "zero or sub-minimum wages. Disruption requires both enforcement and addressing "
            "poverty-driven supply."
        ),
        "source": "ILO Profits and Poverty: The Economics of Forced Labour 2014 / UNODC",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Child Labour — Regional Distribution (2020)",
        "metric": "child_labour_by_region",
        "value": "Sub-Saharan Africa: 86.6M; Asia-Pacific: 48.7M; Central/Southern Asia: 5.5M",
        "summary": (
            "ILO-UNICEF 2020 regional breakdown of child labour: Sub-Saharan Africa: 86.6M "
            "(23.9% of children — highest prevalence); Asia and the Pacific: 48.7M; "
            "Central and Southern Asia: 5.5M (distinct from Asia-Pacific); Americas: 10.5M; "
            "Europe and Central Asia: 5.5M; Northern Africa and Western Asia: 8.2M. "
            "Sub-Saharan Africa saw 16.6M increase since 2012 despite global decline. "
            "Population growth in Sub-Saharan Africa means even constant rates produce "
            "more absolute child labourers. Africa is the only region where child labour "
            "in absolute numbers is increasing."
        ),
        "source": "ILO-UNICEF Child Labour: Global Estimates 2020",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Child Marriage — Annual New Cases (Global)",
        "metric": "child_marriage_annual",
        "value": "12 million girls per year",
        "summary": (
            "UNICEF and Girls Not Brides estimate 12 million girls are married before age 18 "
            "each year — approximately 33,000 per day. If current trends continue, 150 million "
            "additional girls will marry before 18 by 2030. Progress is being made in some "
            "regions (South Asia: rate fell from 40% to 28% over the past decade) but "
            "Sub-Saharan Africa shows slower progress. Niger, Central African Republic, Chad, "
            "Mali, and Bangladesh have the highest rates. Child marriage is both a consequence "
            "of and a driver for trafficking — particularly cross-border 'marriage migration' "
            "that masks trafficking."
        ),
        "source": "UNICEF / Girls Not Brides State of Child Marriage 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "OSEC — Philippines Scale Estimate",
        "metric": "osec_philippines_children_at_risk",
        "value": "500,000 children at risk",
        "summary": (
            "IJM's 2020 baseline assessment estimated 500,000 children in the Philippines are "
            "at risk of Online Sexual Exploitation of Children (OSEC) annually. Philippine "
            "Internet Crime Against Children (PICACC) unit recorded 18,000+ OSEC-related reports "
            "in 2022. Live-streaming abuse generates USD 20–100 per session; Philippine families "
            "in areas of high poverty and high internet penetration (Cebu, Pampanga, Batangas) "
            "are most affected. Reduction efforts require simultaneous demand-side action "
            "(prosecution of foreign offenders) and supply-side action (economic support to "
            "families, community awareness)."
        ),
        "source": "IJM Philippines / PICACC / DSWD Philippines",
    },
    {
        "type": "statistic",
        "jurisdiction": "NG",
        "title": "Nigeria — Almajiri Population Estimate",
        "metric": "almajiri_children",
        "value": "10–15 million",
        "summary": (
            "Nigerian government and UNICEF estimates place the Almajiri population at 10–15 "
            "million boys, concentrated in the northwest (Kano, Kaduna, Zamfara, Sokoto) and "
            "northeast (Borno, Yobe) states. President Goodluck Jonathan launched Integrated "
            "Almajiri Education Program (2012) to provide formal schooling alongside Quranic "
            "education; 158 schools were built. Program was largely abandoned post-2015. "
            "President Buhari's 2020 COVID-19 repatriation of 200,000 Almajiri children "
            "to home states created humanitarian crisis due to lack of receiving infrastructure. "
            "Almajiri system intersects with Boko Haram recruitment in northeast states."
        ),
        "source": "UNICEF Nigeria / HRW Nigeria Almajiri Report 2022 / National Population Commission",
    },
    {
        "type": "statistic",
        "jurisdiction": "HT",
        "title": "Haiti — Restavek Population Estimate",
        "metric": "restavek_children",
        "value": "300,000–500,000",
        "summary": (
            "The Restavek Freedom Foundation and UNICEF estimate 300,000 to 500,000 children "
            "are in restavek (child domestic servitude) arrangements in Haiti — approximately "
            "1 in 10 Haitian children. Girls account for 75–80% of restavek children. Most "
            "are aged 8–15. The system is legally prohibited under Haitian law (Articles "
            "327, 333 of Haitian Penal Code) but prosecutions are near-zero. Post-2010 "
            "earthquake and 2021 earthquake displacement dramatically increased restavek "
            "placements. Gang activity controlling Port-au-Prince neighborhoods since 2022 "
            "has further reduced child protection system functioning."
        ),
        "source": "Restavek Freedom Foundation / UNICEF Haiti / IBESR",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO C189 — Domestic Workers Convention (2011) and Child Protection",
        "summary": (
            "ILO Convention 189 (Domestic Workers Convention, 2011) Art. 4 requires states to "
            "establish a minimum working age for domestic workers consistent with ILO C138 and "
            "C182. Art. 9 requires domestic workers to be free to reach agreement on whether "
            "to reside in the employer's household. Art. 17 calls for effective complaints "
            "mechanisms accessible to domestic workers. Only 38 ratifications as of 2024 — "
            "many major sending and receiving countries have not ratified. Countries that have "
            "ratified: Philippines, Indonesia (no), Sri Lanka, Uruguay, Belgium, Germany, UK. "
            "Non-ratification leaves child domestic workers without international legal protection "
            "in most jurisdictions where they work."
        ),
        "source": "ILO C189 (2011) / ILO NORMLEX Ratification Database 2024",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Optional Protocol on the Sale of Children — CRC-OP-SC (2000)",
        "summary": (
            "The Optional Protocol on the Sale of Children (CRC-OP-SC, 2000) obligates states "
            "parties to criminalise: transfer of a child for sexual exploitation, forced labour, "
            "or organ removal; unlawful adoption; and offering, delivering, or accepting a child "
            "for any of these purposes. 178 states parties. Requires extraterritorial jurisdiction "
            "so offenders can be prosecuted in their home country for crimes committed abroad. "
            "CRC Committee monitors implementation through state party reports. Baby factories, "
            "illegal adoption networks, and orphanage trafficking all fall within its scope."
        ),
        "source": "CRC-OP-SC (2000) / CRC Committee Guidelines on Optional Protocol",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Labour Monitoring Systems — Design and Effectiveness",
        "summary": (
            "ILO and US DOL ILAB document that effective child labour monitoring systems share: "
            "(1) community-based monitors with local legitimacy; (2) real-time reporting "
            "mechanisms (mobile apps increasingly used); (3) integration with social protection "
            "referral (cash transfer, school enrolment); (4) independent third-party verification "
            "of corporate self-reporting; (5) transparent grievance mechanisms accessible to "
            "children and parents. The Cocoa CLMRS covers 315,000 cocoa-farming households "
            "in Cote d'Ivoire and Ghana — the largest commodity-specific child labour monitoring "
            "system in the world, though critics note self-reported data quality concerns."
        ),
        "source": "ILO IPEC+ / US DOL ILAB / Cocoa CLMRS Annual Report 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Child Trafficking and Tourism — Sex Tourism and 'Voluntourism'",
        "summary": (
            "ECPAT and UN Tourism document two distinct tourism-linked child trafficking patterns: "
            "(1) Child sex tourism: foreign nationals travel to countries with lower enforcement "
            "for sexual exploitation of minors. Primary destinations: Thailand, Cambodia, "
            "Philippines, Colombia, Kenya, Brazil. ECPAT's Code of Conduct for Tourism "
            "has 3,000+ signatory businesses. (2) Voluntourism/orphanage tourism: foreign "
            "volunteers pay to work in orphanages housing trafficked children. Demand from "
            "well-intentioned Western volunteers directly funds child trafficking. UNICEF "
            "campaigns #EndOrphanageVolunteering have raised awareness but practice continues."
        ),
        "source": "ECPAT / UN Tourism / UNICEF #EndOrphanageVolunteering / LUMOS",
    },
    {
        "type": "case_study",
        "jurisdiction": "KE",
        "title": "Baby Factories in Kenya — Nairobi and Mombasa (2019–2023)",
        "summary": (
            "Kenya's Directorate of Criminal Investigations (DCI) dismantled baby factory "
            "operations in Nairobi (Eastlands, Kibera) and Mombasa (2019–2023). Vulnerable "
            "women — often from western Kenya — were recruited with false employment or housing "
            "offers, then held and impregnated. Babies were sold for KES 50,000–300,000 "
            "(USD 380–2,300) to infertile couples, illegal adoption networks, and reportedly "
            "to witchcraft practitioners. Kenya's Counter-Trafficking in Persons Act (2010) "
            "provides a legal basis for prosecution; convictions have resulted in 5–10 year "
            "sentences. NGO Trace Kenya operates safe houses for survivors."
        ),
        "source": "Kenya DCI / Trace Kenya / Counter-Trafficking in Persons Act 2010",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Child Marriage Migration — Cross-Border Trafficking via Marriage",
        "summary": (
            "Child marriage migration involves the transfer of girls across borders under the "
            "guise of marriage, where the 'marriage' constitutes trafficking: the girl is "
            "deceived about conditions, forced into domestic servitude or sexual exploitation, "
            "and cannot leave. Documented corridors: (1) Bangladesh-India (girls sold as "
            "wives in Indian states); (2) Ethiopia-Gulf States ('temporary marriages' as "
            "trafficking cover); (3) Mozambique-South Africa; (4) Syria-Jordan/Lebanon "
            "post-war marriage migration. The Palermo Protocol Art. 3(c) makes consent "
            "irrelevant for under-18s, but most countries prosecute under general trafficking "
            "or child marriage statutes rather than trafficking-specific laws."
        ),
        "source": "UNODC / Girls Not Brides / UNICEF / IOM Child Marriage Migration report 2021",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Survivor-Led Advocacy — Children's Voices in Anti-Trafficking Policy",
        "summary": (
            "ECPAT, IJM, and Terre des Hommes increasingly incorporate survivor-led advocacy "
            "in policy design. Former child trafficking survivors advise governments on "
            "identification barriers, shelter quality, and reintegration gaps. ECPAT's "
            "Youth Pathways Program trains survivor advocates aged 18–25 in 30+ countries. "
            "Key survivor-identified policy gaps: (1) shelters that function as detention "
            "rather than rehabilitation; (2) judicial processes that re-traumatize through "
            "repetitive testimony; (3) absence of long-term economic support post-shelter; "
            "(4) lack of mental health services in native language; (5) family reunification "
            "without safety assessment leading to re-trafficking."
        ),
        "source": "ECPAT Youth Pathways / IJM Survivor Advisory Boards / Terre des Hommes",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Data Gaps in Child Trafficking — Measurement Challenges",
        "summary": (
            "UNODC, ILO, and UNICEF acknowledge significant data gaps in child trafficking "
            "measurement: (1) detection-based data reflect law enforcement capacity more than "
            "prevalence; (2) family-facilitated trafficking (restavek, OSEC, camel jockeys, "
            "baby factories) is severely undercounted; (3) cross-border trafficking data "
            "depend on bilateral information sharing, which is inconsistent; (4) informal "
            "sector child labour (agriculture, domestic work) evades official surveys; "
            "(5) conflict zones produce no reliable data. The ILO recommends multiplier "
            "methods and respondent-driven sampling for hidden child trafficking populations. "
            "The true scale of child trafficking globally is likely 3–5x detected figures."
        ),
        "source": "UNODC / ILO / UNICEF Joint Note on Data Gaps in Trafficking Statistics 2021",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "National Action Plans on Child Labour — Effectiveness Review",
        "summary": (
            "ILO IPEC+ reviewed national action plans (NAPs) on child labour in 24 countries "
            "(2022). Effective NAPs share: (1) time-bound, measurable targets with budget "
            "allocations; (2) inter-ministerial coordination mechanisms (labour, education, "
            "social protection, justice); (3) designated focal points at sub-national level; "
            "(4) integration with broader social protection systems; (5) civil society "
            "and private sector participation. Weak NAPs: aspirational language without "
            "resources, no coordination mechanism, no accountability. Ghana, Brazil, and "
            "Vietnam were cited as positive examples; DRC, Chad, and Niger as countries "
            "with urgent gaps."
        ),
        "source": "ILO IPEC+ National Action Plans Review 2022",
    },
]
