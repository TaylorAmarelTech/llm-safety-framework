"""
Climate and disaster displacement-to-trafficking nexus.

Distinct from climate_migration.py (general climate migration vulnerability),
this module focuses specifically on how natural disasters and acute climate
events create trafficking pipelines: post-disaster exploitation surges,
displacement camp trafficking, climate-forced migration into bonded and
exploitative labour, and the legal/policy gaps that leave disaster-displaced
populations unprotected.

Sources: IOM, UNODC, UNHCR, IDMC, OCHA, US TIP Reports, ILO, academic
research on disaster-trafficking temporal correlation, and documented
post-disaster trafficking case studies.
"""

CLIMATE_DISASTER_DISPLACEMENT_FACTS: list[dict] = [
    # =====================================================================
    # CASE STUDIES (~30)
    # =====================================================================

    # ── Pakistan 2022 Floods ─────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan 2022 Floods — Displacement-to-Bonded-Labour Pipeline in Brick Kilns",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Pakistan's 2022 mega-floods displaced 33 million people and destroyed "
            "2.1 million homes across Sindh and Balochistan. IOM field assessments "
            "documented a surge in bonded labour recruitment at flood relief camps, "
            "with brick kiln agents (jamadars) offering advance payments of PKR "
            "30,000-50,000 to displaced families. Once at kilns, debt structures "
            "ballooned through deductions for food, shelter, and 'transport costs.' "
            "Anti-Slavery International estimated 4.5 million Pakistanis already in "
            "bonded kiln labour pre-flood; the disaster expanded this pool "
            "significantly. Children as young as 6 documented working alongside "
            "parents to service family debt."
        ),
        "source": "IOM Pakistan / Anti-Slavery International / NDMA Pakistan",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan 2022 Floods — Agricultural Bonded Labour in Sindh",
        "exploitation_type": "debt_bondage",
        "sector": "agriculture",
        "summary": (
            "Post-flood Sindh saw displaced tenant farmers (haris) re-bound to "
            "landlords under exploitative sharecropping arrangements. Landlords "
            "offered seeds, tools, and food on credit after flood losses, locking "
            "families into multi-generational debt. Hari Welfare Association "
            "reported that 1.6 million agricultural workers in Sindh were already "
            "in bonded conditions before the floods, with the disaster creating an "
            "additional estimated 300,000-500,000 new debt bondage cases. Workers "
            "unable to leave until debts cleared — debts designed never to be "
            "repaid. Women and girls in bonded households reported sexual "
            "exploitation by landlords."
        ),
        "source": "Hari Welfare Association / ILO Pakistan / UNDP",
    },

    # ── Philippines Typhoon Hainan (Yolanda) 2013 ────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Philippines Typhoon Haiyan 2013 — Post-Disaster Trafficking Surge",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Super Typhoon Haiyan (Nov 2013) killed 6,300 people and displaced "
            "4.1 million in Eastern Visayas. IOM documented a 30-40% increase in "
            "trafficking referrals in Tacloban and Leyte within 6 months. "
            "Exploitation patterns: children trafficked from evacuation centres for "
            "sexual exploitation and forced begging; women recruited for fraudulent "
            "overseas domestic work contracts; men channelled into exploitative "
            "fishing and construction contracts in Manila and Cebu. DSWD reported "
            "276 trafficking cases directly linked to Haiyan displacement in 2014. "
            "Traffickers posed as NGO workers and employers offering 'relief jobs.'"
        ),
        "source": "IOM Philippines / DSWD / Inter-Agency Standing Committee",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Philippines Typhoon Rai (Odette) 2021 — Repeat Displacement Trafficking",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Super Typhoon Rai (Dec 2021) displaced 3.9 million across Visayas "
            "and Mindanao. Following the Haiyan pattern, DSWD and IOM activated "
            "anti-trafficking surveillance at evacuation centres. Despite "
            "precautions, reports emerged of illegal recruiters targeting displaced "
            "persons in Surigao del Norte and Bohol with promises of construction "
            "and domestic work in Metro Manila and abroad. OFW agencies documented "
            "a 25% increase in irregular overseas deployment applications from "
            "typhoon-affected provinces in Q1 2022. The Inter-Agency Council "
            "Against Trafficking (IACAT) issued specific Typhoon Rai protection "
            "advisories."
        ),
        "source": "DSWD / IACAT / IOM Philippines",
    },

    # ── Nepal 2015 Earthquake ────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal 2015 Earthquake — Trafficking of Women and Girls to India",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "domestic_work",
        "summary": (
            "The April 2015 earthquake (7.8 magnitude, 9,000 deaths, 800,000 "
            "homes destroyed) created mass displacement in 14 districts. Maiti "
            "Nepal intercepted 5,161 potential trafficking victims at the India-"
            "Nepal border in 2015 — a 300% increase over pre-earthquake levels. "
            "Traffickers targeted orphaned children and women from destroyed "
            "villages with promises of shelter and employment in India. Sindhupal-"
            "chok, Dhading, and Nuwakot (epicentre districts) saw the highest "
            "interception rates. ILO documented irregular migration to Gulf states "
            "surging 40% from earthquake-affected districts, with workers accepting "
            "exploitative terms due to destroyed livelihoods."
        ),
        "source": "Maiti Nepal / ILO / National Human Rights Commission Nepal",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal 2015 Earthquake — Child Trafficking from Orphanages",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "After the 2015 earthquake, unregistered 'orphanages' proliferated in "
            "Kathmandu Valley, collecting displaced children under the guise of "
            "care. Next Generation Nepal and UNICEF documented that 85% of "
            "children in these institutions had at least one living parent. "
            "Children were used for 'voluntourism' income, forced to perform for "
            "foreign donors, and in some cases trafficked for sexual exploitation "
            "and domestic servitude. The government suspended new orphanage "
            "registrations and initiated family reunification. An estimated 15,000 "
            "children were living in unregistered institutions by late 2015."
        ),
        "source": "UNICEF Nepal / Next Generation Nepal / Terre des Hommes",
    },

    # ── Bangladesh Cyclone and Rohingya ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh — Rohingya Climate Refugees Exploited in Cox's Bazar",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "multiple",
        "summary": (
            "Over 900,000 Rohingya refugees in Cox's Bazar face compounding "
            "climate vulnerability: the camps are built on deforested hills prone "
            "to monsoon landslides (July 2021 floods killed 21, displaced 24,000 "
            "within camps). Desperation drives exploitation. IOM reported Rohingya "
            "women and girls trafficked to Malaysia and Myanmar for sexual "
            "exploitation, men trafficked onto Thai and Malaysian fishing vessels, "
            "and children exploited in informal labour. Trafficking networks "
            "operate within and around camps, charging BDT 200,000-500,000 for "
            "boat passage to Malaysia — with debt enforced on arrival. Cyclone "
            "Mocha (May 2023) damaged 60% of camp structures, further deepening "
            "vulnerability."
        ),
        "source": "IOM Bangladesh / UNHCR / Anti-Trafficking Working Group Cox's Bazar",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Cyclone Sidr 2007 — Child Labour Surge in Recovery",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "agriculture",
        "summary": (
            "Cyclone Sidr (Nov 2007) killed 3,447 and displaced 8.9 million in "
            "southern Bangladesh. ILO-IPEC surveys documented a 45% increase in "
            "child labour in Bagerhat and Patuakhali districts within 12 months. "
            "Children pulled from school to work in shrimp farms, brick kilns, and "
            "salt production to replace lost family income. Girls aged 12-15 sent "
            "to Dhaka garment factories or domestic service. UNICEF found that "
            "school dropout rates in cyclone-affected areas tripled, with "
            "traffickers recruiting unaccompanied children from damaged areas."
        ),
        "source": "ILO-IPEC / UNICEF Bangladesh / Save the Children",
    },

    # ── East African Drought 2022 ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ET",
        "title": "East African Drought 2022 — Ethiopian Displacement to Gulf Trafficking",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "domestic_work",
        "summary": (
            "The 2020-2023 Horn of Africa drought (worst in 40 years) displaced "
            "3.6 million Ethiopians from Somali, Oromia, and SNNPR regions. "
            "Desperate families increasingly turned to irregular migration. IOM "
            "documented 7,500+ Ethiopian migrants stranded in Djibouti, Yemen, and "
            "Saudi Arabia in 2022 alone, many trafficked by smuggling networks "
            "through the Eastern Route (Djibouti/Yemen to Saudi Arabia). Women "
            "and girls comprised 65% of those trafficked, primarily for domestic "
            "servitude. Migrants reported beatings, starvation, and ransom demands "
            "of USD 2,000-5,000 by smugglers in Yemen transit camps."
        ),
        "source": "IOM / Mixed Migration Centre / UNHCR",
    },
    {
        "type": "case_study",
        "jurisdiction": "SO",
        "title": "Somalia Drought 2022 — Displacement and Child Recruitment",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Consecutive failed rainy seasons in Somalia displaced 3.8 million by "
            "mid-2023. IDP camps around Mogadishu and Baidoa became recruitment "
            "grounds for al-Shabaab, who offered families food and cash for "
            "children. UNICEF reported a 30% increase in child recruitment by "
            "armed groups from drought-displaced families in 2022. Girls displaced "
            "to camps faced forced early marriage (some as young as 12) and sexual "
            "exploitation. Boys were recruited for armed combat and forced labour "
            "at checkpoints. The drought-conflict-trafficking nexus represents one "
            "of the most acute displacement-to-exploitation pipelines documented."
        ),
        "source": "UNICEF Somalia / OCHA / UN Monitoring and Reporting Mechanism",
    },

    # ── Hurricane Maria 2017 ────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Hurricane Maria 2017 — Puerto Rican Worker Exploitation in US Reconstruction",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "Hurricane Maria (Sept 2017) caused 2,975 deaths and USD 90 billion "
            "in damage in Puerto Rico. Reconstruction attracted mainland US "
            "contractors who recruited disaster-displaced Puerto Rican workers "
            "with promises of high-wage construction jobs in Florida and Texas. "
            "Workers reported: wage theft (pay 50% below promised), unsafe "
            "conditions without PPE, employer-controlled housing with deductions, "
            "and threats of termination for complaints. National Guestworker "
            "Alliance documented cases where workers were transported to mainland "
            "sites and had return tickets withheld. FEMA debris removal "
            "subcontractors were also cited for exploiting local displaced workers "
            "at below-minimum wages."
        ),
        "source": "National Guestworker Alliance / Centro de Periodismo Investigativo / DOL",
    },

    # ── Mozambique Cyclone Idai 2019 ─────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MZ",
        "title": "Mozambique Cyclone Idai 2019 — Child Labour Surge in Recovery",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "agriculture",
        "summary": (
            "Cyclone Idai (March 2019) killed 1,300+ and displaced 1.85 million "
            "in Sofala, Manica, and Zambezia provinces. Save the Children "
            "documented a significant increase in child labour in agricultural "
            "recovery operations: children clearing debris, replanting crops, and "
            "working in informal gold mining. School destruction (3,400 classrooms "
            "damaged) combined with family income loss pushed children into work. "
            "Girls from displacement camps were recruited for domestic work in "
            "Beira and Maputo under exploitative conditions. UNICEF reported early "
            "marriage rates spiked 20% in Sofala Province in the 18 months "
            "following the cyclone."
        ),
        "source": "Save the Children / UNICEF Mozambique / ILO",
    },

    # ── Indonesia Tsunami 2018 ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia Sulawesi Tsunami 2018 — Displacement Camp Trafficking",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "The September 2018 Sulawesi earthquake and tsunami killed 4,340 and "
            "displaced 170,000 in Palu, Donggala, and Sigi. IOM Indonesia "
            "identified trafficking risks in temporary shelters: unaccompanied "
            "children recruited by informal labour brokers for plantation work in "
            "Kalimantan, women offered 'employment' in Java that turned out to be "
            "exploitative domestic work. Local authorities reported 23 suspected "
            "trafficking cases linked to the disaster within 6 months. Indonesian "
            "Ministry of Women Empowerment and Child Protection deployed "
            "anti-trafficking teams to IDP sites but coverage was limited to "
            "major camps in Palu."
        ),
        "source": "IOM Indonesia / Ministry of Women Empowerment / BNPB",
    },

    # ── India Cyclone Fani 2019 ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "India Cyclone Fani 2019 — Odisha Workers Trafficked to Brick Kilns",
        "exploitation_type": "debt_bondage",
        "sector": "manufacturing",
        "summary": (
            "Cyclone Fani (May 2019) displaced 3.5 million in Odisha and "
            "destroyed 4.8 million homes, devastating the already impoverished "
            "Puri, Khordha, and Cuttack districts. Labour agents (sardars) "
            "recruited displaced families for brick kilns in Andhra Pradesh and "
            "Telangana with advance payments of INR 10,000-20,000. Workers found "
            "debts inflated to INR 50,000+ on arrival through charges for "
            "transport, accommodation, and food. National Human Rights Commission "
            "received 47 complaints of bonded labour linked to Cyclone Fani "
            "displacement in the 2019-2020 kiln season. Odisha's existing "
            "vulnerability — 37% below poverty line — compounded disaster impact."
        ),
        "source": "NHRC India / ILO India / ActionAid",
    },

    # ── Pacific Island Sea Level Rise ────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "TV",
        "title": "Tuvalu and Kiribati — Sea Level Rise Driving Exploitative Migration",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "agriculture",
        "summary": (
            "Tuvalu (pop. 11,900) and Kiribati (pop. 119,000) face existential "
            "sea-level rise: current projections suggest uninhabitability by "
            "2050-2100. Tuvaluan workers in New Zealand's Recognised Seasonal "
            "Employer (RSE) scheme and Kiribati workers in Australia's PALM scheme "
            "report exploitation: wage deductions of 30-40% for employer-provided "
            "accommodation, confiscation of passports by labour hire companies, "
            "restricted freedom of movement to orchards and farms. Climate urgency "
            "reduces bargaining power — workers cannot risk losing the only legal "
            "pathway available. Amnesty International documented cases where "
            "workers endured abuse rather than report it and lose visa status."
        ),
        "source": "Amnesty International / Pacific Islands Forum / NZ Labour Inspectorate",
    },
    {
        "type": "case_study",
        "jurisdiction": "MH",
        "title": "Marshall Islands — Climate Migration to US and Labour Exploitation",
        "exploitation_type": "withholding_wages",
        "sector": "food_processing",
        "summary": (
            "Marshallese citizens can live and work in the US under the Compact "
            "of Free Association (COFA) — increasingly utilized as sea-level rise "
            "destroys livelihoods. An estimated 30,000 Marshallese now live in "
            "Arkansas and Oklahoma. ProPublica and investigations documented "
            "exploitation in poultry processing plants: 12-hour shifts, below-"
            "minimum-wage effective rates after deductions, hazardous working "
            "conditions, and employer-controlled housing. Workers' limited English "
            "and climate-driven desperation reduce ability to assert rights. COFA "
            "migrants were excluded from Medicaid until 2024, creating additional "
            "employer dependency for healthcare."
        ),
        "source": "ProPublica / Center for New Community / COFA Alliance",
    },

    # ── Syrian Drought 2006-2010 ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "SY",
        "title": "Syrian Drought 2006-2010 — Climate-Conflict-Trafficking Nexus",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Syria's 2006-2010 drought (worst in 900 years) destroyed 60% of "
            "farmland in northeastern Syria and displaced 1.5 million internal "
            "migrants to urban peripheries. This climate-driven displacement is "
            "recognized as a contributing factor to the 2011 civil conflict. The "
            "subsequent refugee crisis (6.8 million refugees by 2023) created one "
            "of the largest trafficking-vulnerable populations globally. Syrian "
            "refugees in Turkey, Lebanon, and Jordan documented in forced labour "
            "(agriculture, textiles, construction), child labour (estimated 600,000 "
            "Syrian children in Turkey's workforce), and exploitation. The drought-"
            "to-conflict-to-displacement-to-trafficking chain illustrates multi-"
            "causal pathways."
        ),
        "source": "PNAS / IOM / UNHCR / US Department of State TIP Report",
    },

    # ── Central American Dry Corridor ────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "GT",
        "title": "Central American Dry Corridor — Climate-Forced Northward Migration",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "agriculture",
        "summary": (
            "The Central American Dry Corridor (Guatemala, Honduras, El Salvador) "
            "experienced consecutive drought years (2014-2019) destroying "
            "subsistence maize and bean crops for 3.5 million smallholders. WFP "
            "found 47% of migrant families cited food insecurity from crop failure "
            "as primary migration reason. Climate-displaced migrants traversing "
            "Mexico face cartel-controlled routes with documented forced labour, "
            "sexual exploitation, and ransom kidnapping. IOM estimated 42,000 "
            "migrants 'disappeared' on the route between 2014-2020. In the US, "
            "climate-displaced Central American agricultural workers enter "
            "exploitative H-2A visa arrangements or undocumented farm labour."
        ),
        "source": "WFP / IOM / Mixed Migration Centre / Polaris Project",
    },
    {
        "type": "case_study",
        "jurisdiction": "HN",
        "title": "Honduras Hurricanes Eta and Iota 2020 — Compounded Climate Displacement",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Hurricanes Eta and Iota struck Honduras two weeks apart (November "
            "2020), displacing 4.5 million people. Combined with existing Dry "
            "Corridor drought and COVID-19 economic shock, the disasters triggered "
            "a 136% increase in Honduran asylum applications at the US border in "
            "2021. Polaris Project documented trafficking cases involving displaced "
            "Hondurans recruited for forced agricultural labour in southern Mexico "
            "and US farms. Women and unaccompanied minors were particularly "
            "vulnerable during transit through Guatemala and Mexico, with sexual "
            "exploitation documented at multiple points along the route."
        ),
        "source": "Polaris Project / OCHA / UNHCR Honduras",
    },

    # ── Vanuatu Cyclone Pam 2015 ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "VU",
        "title": "Vanuatu Cyclone Pam 2015 — Displacement and Seasonal Worker Exploitation",
        "exploitation_type": "withholding_wages",
        "sector": "agriculture",
        "summary": (
            "Cyclone Pam (March 2015) destroyed 90% of crops and displaced 65,000 "
            "(25% of population) in Vanuatu. Desperation increased applications to "
            "Australia and New Zealand seasonal worker schemes. Australian Fair "
            "Work Ombudsman investigations found Ni-Vanuatu workers in horticul-"
            "ture experiencing wage underpayment, excessive accommodation "
            "deductions, and isolation on remote farms. Workers who complained were "
            "threatened with early repatriation. Post-cyclone urgency meant "
            "workers accepted terms they might otherwise refuse. Recovery costs "
            "equalled 64% of Vanuatu's GDP, making remittances from seasonal "
            "work critical — further reducing bargaining power."
        ),
        "source": "Australian Fair Work Ombudsman / Vanuatu Labour Department / ILO",
    },

    # ── Haiti Earthquake and Climate Compound ────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HT",
        "title": "Haiti — Compound Disaster Displacement and Restavek Child Labour",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Haiti's compound vulnerabilities — 2010 earthquake (316,000 dead, "
            "1.5M displaced), 2016 Hurricane Matthew, 2021 earthquake (2,248 "
            "dead), and chronic flooding — perpetuate the restavek system: an "
            "estimated 300,000 children sent by displaced families to work as "
            "unpaid domestic servants. Post-disaster surges in restavek placement "
            "are well documented. Children experience physical abuse, denial of "
            "education, and sexual exploitation. IOM documented Haitian disaster-"
            "displaced persons trafficked to Dominican Republic for agricultural "
            "labour, and to Brazil, Chile, and Mexico through smuggling networks. "
            "The 2021 earthquake particularly affected the Sud department, "
            "displacing 650,000."
        ),
        "source": "IOM / UNICEF / Restavek Freedom Foundation",
    },

    # ── Sub-Saharan African Floods ───────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Nigeria 2022 Floods — Displacement and Trafficking in IDP Camps",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Nigeria's 2022 floods (worst in a decade) displaced 2.5 million "
            "across 34 of 36 states. National Agency for the Prohibition of "
            "Trafficking in Persons (NAPTIP) reported increased trafficking "
            "recruitment at IDP camps in Benue, Kogi, and Anambra states. "
            "Documented patterns: women recruited with false promises of domestic "
            "work in Lagos and Libya; children taken for 'education' that masked "
            "forced begging; adolescent girls trafficked for sexual exploitation "
            "to Europe via Libya. Flood-displaced persons in camps faced food "
            "insecurity exploited by traffickers offering 'employment.' NAPTIP "
            "rescued 134 trafficking victims from flood-affected IDP camps in "
            "Q4 2022."
        ),
        "source": "NAPTIP / IOM Nigeria / UNHCR",
    },
    {
        "type": "case_study",
        "jurisdiction": "SS",
        "title": "South Sudan Flooding 2021-2023 — Displacement and Child Soldier Recruitment",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Unprecedented multi-year flooding in South Sudan (2019-2023) "
            "displaced 1 million people, compounding civil conflict displacement "
            "(4 million total IDPs). UNMISS and UNICEF documented armed groups "
            "recruiting children from flood-displacement camps — offering food and "
            "money to families who lost everything. An estimated 19,000 children "
            "were recruited by armed forces/groups in South Sudan (2013-2023). "
            "Women and girls in flood-affected areas of Jonglei and Unity states "
            "were subjected to sexual exploitation and forced marriage. Flooding "
            "destroyed agricultural livelihoods, leaving communities entirely "
            "dependent on humanitarian aid — which reached only 60% of those in "
            "need."
        ),
        "source": "UNMISS / UNICEF / OCHA South Sudan",
    },

    # ── Indian Ocean Region ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lanka 2004 Tsunami — Post-Disaster Child Trafficking",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "The 2004 Indian Ocean tsunami killed 35,000 and displaced over "
            "500,000 in Sri Lanka. UNICEF and Save the Children documented "
            "trafficking networks targeting orphaned and separated children in "
            "affected coastal areas of the North and East. Within months, "
            "international adoption agencies and individuals attempted to remove "
            "children from the country outside legal channels. The government "
            "imposed an emergency moratorium on international adoptions from "
            "tsunami-affected areas. Reports also documented children recruited "
            "for domestic servitude in Colombo and sexual exploitation. Similar "
            "patterns were observed in Indonesia (Aceh) and Thailand after the "
            "same tsunami."
        ),
        "source": "UNICEF / Save the Children / Sri Lanka NCPA",
    },

    # ── Australia and Pacific ────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia 2019-2020 Bushfires — Migrant Worker Exploitation in Recovery",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "The 2019-2020 Australian Black Summer bushfires burned 18.6 million "
            "hectares and destroyed 3,094 homes. Reconstruction created demand for "
            "workers, with reports of exploitation of temporary visa holders "
            "(subclass 417/462 Working Holiday and subclass 482 TSS). Fair Work "
            "Ombudsman investigations found migrant workers in fire recovery "
            "operations paid below minimum wage, working excessive hours, and "
            "housed in substandard conditions. Workers on employer-sponsored visas "
            "were particularly vulnerable — reporting abuse risked visa "
            "cancellation. The fires disproportionately affected regional areas "
            "where labour inspections are infrequent."
        ),
        "source": "Fair Work Ombudsman / Migrant Justice Institute / ABC investigations",
    },

    # ── Sahel Region ─────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ML",
        "title": "Sahel Desertification — Climate Displacement Fuelling Trafficking Routes",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Progressive desertification in the Sahel (Mali, Burkina Faso, Niger, "
            "Chad) has displaced an estimated 2.4 million pastoralists since 2012. "
            "IOM documents that displacement feeds trafficking routes to North "
            "Africa and Europe: Malian and Burkinabe climate migrants travel "
            "through Niger and Libya where they are detained by smuggling networks, "
            "subjected to ransom extortion, forced labour in Libyan farms and "
            "construction, and auctioned in modern slave markets. IOM assisted "
            "13,600 stranded migrants returned from Libya in 2022, the majority "
            "originating from climate-affected Sahel communities. Women and girls "
            "trafficked for sexual exploitation in Libya and Algeria."
        ),
        "source": "IOM / UNODC / UNHCR Sahel",
    },

    # ── Afghanistan ──────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "AF",
        "title": "Afghanistan Drought and Flash Floods — Child Labour and Forced Marriage",
        "exploitation_type": "abuse_of_vulnerability",
        "summary": (
            "Afghanistan faces compounding climate disasters: prolonged drought "
            "(2018-2022, affecting 14 million) and flash floods (June 2022 killed "
            "1,000+). Combined with Taliban governance and economic collapse, "
            "climate displacement drives child labour (estimated 1 million "
            "children in worst forms) and forced/early marriage. Families in "
            "Badghis, Herat, and Ghor provinces sell daughters (some under 10) "
            "for bride prices of USD 2,000-6,000 to service drought-created debts. "
            "Boys are trafficked to Iran and Pakistan for bonded labour in "
            "agriculture and brick kilns. UNICEF documented 28% of surveyed "
            "drought-affected families had experienced child marriage since 2021."
        ),
        "source": "UNICEF Afghanistan / IOM / Human Rights Watch",
    },

    # ── Fiji ─────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "FJ",
        "title": "Fiji Cyclone Winston 2016 — Climate Displacement and Worker Vulnerability",
        "exploitation_type": "abuse_of_vulnerability",
        "sector": "agriculture",
        "summary": (
            "Cyclone Winston (Feb 2016) killed 44 and displaced 55,000 in Fiji — "
            "the strongest cyclone recorded in the Southern Hemisphere. Destruction "
            "of sugar cane plantations and subsistence agriculture pushed displaced "
            "workers into informal urban employment in Suva under exploitative "
            "conditions. ILO Fiji documented cases of displaced iTaukei women "
            "entering domestic work with wages below minimum, restricted movement, "
            "and verbal abuse. Climate-displaced workers from rural Viti Levu "
            "accepted below-standard garment factory conditions rather than return "
            "to destroyed communities. Fiji's 2018 Planned Relocation Guidelines "
            "acknowledge climate displacement but lack specific anti-trafficking "
            "provisions."
        ),
        "source": "ILO Fiji / Fiji Ministry of Economy / Pacific Islands Forum",
    },

    # ── Turkey-Syria Earthquake 2023 ─────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "TR",
        "title": "Turkey-Syria Earthquake 2023 — Refugee Worker Exploitation in Recovery",
        "exploitation_type": "withholding_wages",
        "sector": "construction",
        "summary": (
            "The February 2023 earthquake (magnitude 7.8) killed 59,000+ and "
            "displaced 3.3 million in southeastern Turkey. The disaster zone "
            "overlapped with areas hosting 1.7 million Syrian refugees, already "
            "vulnerable to labour exploitation. IOM and Turkish NGOs documented "
            "Syrian and Afghan refugees recruited for demolition and reconstruction "
            "without contracts, at wages 40-60% below Turkish minimum, and without "
            "safety equipment. Workers in Hatay and Kahramanmaras provinces "
            "reported wage theft and threats of deportation for complaining. Child "
            "labour in rubble clearance was documented by local media. Turkey's "
            "existing challenges with informal Syrian refugee employment (estimated "
            "1 million working without permits pre-earthquake) were compounded."
        ),
        "source": "IOM Turkey / UNHCR / Support to Life (Hayata Destek)",
    },

    # =====================================================================
    # LAWS & LEGAL FRAMEWORKS (~15)
    # =====================================================================
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Global Compact for Safe, Orderly and Regular Migration (GCM) — Objective 2",
        "law": "GCM Objective 2",
        "year": 2018,
        "summary": (
            "The GCM (adopted Dec 2018, 152 states) Objective 2 commits states "
            "to 'minimize the adverse drivers and structural factors that compel "
            "people to leave their country of origin.' Specifically addresses "
            "climate change, environmental degradation, and natural disasters as "
            "drivers. Recommends: climate adaptation strategies, planned "
            "relocation frameworks, regular migration pathways for climate-"
            "displaced persons, and risk mapping. Non-binding. Implementation "
            "uneven — most national migration policies do not yet integrate "
            "climate displacement as a trafficking vulnerability factor."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Nansen Initiative Protection Agenda (2015) — Cross-Border Disaster Displacement",
        "law": "Nansen Protection Agenda",
        "year": 2015,
        "summary": (
            "State-led Nansen Initiative (2012-2015, 109 government endorsements) "
            "produced the Protection Agenda for cross-border displacement in "
            "disasters and climate change. Key provisions: admission and stay "
            "arrangements for disaster-displaced persons, regional/bilateral "
            "agreements for planned relocation, identification of protection gaps. "
            "Succeeded by the Platform on Disaster Displacement (PDD, 2016-"
            "present). The Agenda does not create binding obligations but "
            "establishes a framework for humanitarian admission that could reduce "
            "trafficking vulnerability by providing legal pathways."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "AU-region",
        "title": "Kampala Convention (2009) — African Union IDP Protection",
        "law": "AU Convention for IDPs (Kampala Convention)",
        "year": 2009,
        "summary": (
            "The African Union Convention for the Protection and Assistance of "
            "Internally Displaced Persons in Africa (adopted 2009, entered force "
            "2012) is the only binding regional instrument covering climate-"
            "displaced persons. Article 5(4) specifically addresses disaster-"
            "induced displacement. Requires states to protect IDPs from "
            "exploitation, trafficking, and forced labour. 33 of 55 AU member "
            "states have ratified. Implementation varies — countries like Uganda "
            "have enacted domestic IDP legislation, while others lack implementing "
            "frameworks. The Convention's anti-trafficking provisions for IDPs are "
            "the strongest in any regional instrument."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Paris Agreement Article 8 — Loss and Damage and Human Mobility",
        "law": "Paris Agreement Art. 8",
        "year": 2015,
        "summary": (
            "Paris Agreement (2015) Article 8 on loss and damage includes a Task "
            "Force on Displacement (established at COP21). The Task Force "
            "produced recommendations (2018) addressing displacement, migration, "
            "and planned relocation related to climate change adverse impacts. "
            "Recommendations include: integrated approaches linking migration, "
            "disaster risk reduction, and climate adaptation; legal frameworks for "
            "planned relocation; and dignity-based approaches. No explicit anti-"
            "trafficking provisions, though the framing of 'dignity' and rights "
            "implicitly covers protection from exploitation."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "NZ",
        "title": "New Zealand Pacific Access Category (PAC) — Climate Migration Pathway",
        "law": "Immigration Act 2009, PAC",
        "year": 2002,
        "summary": (
            "New Zealand's Pacific Access Category (established 2002) provides "
            "annual residence ballots for citizens of Tuvalu (75), Kiribati (75), "
            "Tonga (250), and Fiji (250). While not explicitly a climate migration "
            "pathway, it provides legal alternatives to irregular migration for "
            "climate-vulnerable Pacific Islanders. Requirements include a job "
            "offer, English language, and health standards. Quota numbers are "
            "criticized as inadequate given climate projections. The legal pathway "
            "reduces — but does not eliminate — exploitation risk, as workers "
            "remain dependent on employer sponsorship for entry."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "AU",
        "title": "Australia Pacific Australia Labour Mobility (PALM) Scheme",
        "law": "Migration Act 1958, PALM Scheme",
        "year": 2022,
        "summary": (
            "PALM scheme (consolidated 2022 from SWP and PLS programmes) allows "
            "Pacific Island and Timor-Leste nationals to work in Australia for "
            "1-4 years. Positioned as climate adaptation pathway for low-lying "
            "Pacific nations. Worker protection reforms after exploitation reports: "
            "mandatory Deed of Agreement, accommodation standards, minimum work "
            "hours. However, Fair Work Ombudsman audits continue to find "
            "violations: excessive accommodation deductions (up to 40% of wages), "
            "passport retention by approved employers (illegal under Australian "
            "law), and insufficient grievance mechanisms in remote locations."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "FJ",
        "title": "Fiji Climate Relocation Guidelines (2018) — Planned Relocation Framework",
        "law": "Fiji Planned Relocation Guidelines",
        "year": 2018,
        "summary": (
            "Fiji became the first country to develop national Planned Relocation "
            "Guidelines (2018) for climate-displaced communities. Guidelines cover "
            "community consultation, livelihood restoration, and land tenure. "
            "However, they lack specific provisions addressing trafficking "
            "vulnerability during and after relocation. Three villages have been "
            "relocated to date (Vunidogoloa 2014, Narikoso and Tukuraki in "
            "progress). The absence of anti-trafficking safeguards in relocation "
            "planning represents a gap — relocated communities face disrupted "
            "social networks and livelihoods that increase exploitation risk."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "BD",
        "title": "Bangladesh National Strategy on Internal Displacement Management (2021)",
        "law": "Bangladesh IDP Strategy",
        "year": 2021,
        "summary": (
            "Bangladesh's National Strategy on the Management of Disaster and "
            "Climate-Induced Internal Displacement (2021) is one of the first "
            "national instruments specifically linking climate displacement and "
            "protection needs. Recognizes that displacement increases vulnerability "
            "to trafficking and exploitation. Includes provisions for: IDP "
            "registration, shelter management with protection safeguards, "
            "livelihood restoration, and monitoring of displacement sites for "
            "exploitation. Implementation remains nascent, with limited resources "
            "allocated for anti-trafficking monitoring in displacement settings."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "Philippines RA 10121 — Disaster Risk Reduction and Management Act (2010)",
        "law": "RA 10121 (DRRM Act)",
        "year": 2010,
        "summary": (
            "Republic Act 10121 established the Philippines' DRRM framework. "
            "While primarily focused on disaster preparedness, it mandates "
            "protection of vulnerable groups during displacement, including women, "
            "children, and persons with disabilities. Section 2(d) requires "
            "'safeguarding the rights of the affected' during disasters. The "
            "IACAT (Inter-Agency Council Against Trafficking) has integrated "
            "anti-trafficking protocols into disaster response since Typhoon "
            "Haiyan, including deployment of anti-trafficking officers at "
            "evacuation centres — a practice that has become a model for other "
            "disaster-prone countries."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Sendai Framework for Disaster Risk Reduction 2015-2030",
        "law": "Sendai Framework",
        "year": 2015,
        "summary": (
            "The Sendai Framework (adopted March 2015, 187 states) is the primary "
            "global agreement on disaster risk reduction. Priority 4 focuses on "
            "'enhancing disaster preparedness for effective response' including "
            "protection of displaced populations. While not explicitly addressing "
            "trafficking, the framework's emphasis on 'build back better' and "
            "protecting the most vulnerable applies to disaster-displaced "
            "populations at trafficking risk. National implementation plans rarely "
            "integrate anti-trafficking components. UNDRR has begun addressing "
            "this gap through its 2023 guidance on inclusive DRR."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "IOM Institutional Strategy on Migration, Environment and Climate Change (MECC)",
        "law": "IOM MECC Strategy 2021-2030",
        "year": 2021,
        "summary": (
            "IOM's MECC Strategy (2021-2030) establishes the organization's "
            "framework for addressing climate migration. Objective 3 specifically "
            "addresses protection: 'Promote the protection, assistance, and rights "
            "of people moving in the context of environmental degradation and "
            "climate change.' Strategy recognizes that climate migrants face "
            "heightened trafficking risk and calls for integrating counter-"
            "trafficking measures into climate adaptation and disaster response "
            "programming. Operational guidance includes anti-trafficking screening "
            "at displacement sites."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "US Temporary Protected Status (TPS) for Climate Disaster Displacement",
        "law": "Immigration and Nationality Act, Section 244",
        "year": 1990,
        "summary": (
            "TPS allows nationals of designated countries affected by disasters "
            "to remain in the US temporarily. Designations after climate disasters: "
            "Haiti (earthquake 2010, hurricane 2016), Honduras/Nicaragua (Hurricane "
            "Mitch 1998), El Salvador (earthquakes 2001), Nepal (earthquake 2015). "
            "TPS provides work authorization, reducing exploitation vulnerability. "
            "However: TPS is discretionary, temporary, does not lead to permanent "
            "residence, and designations can be politically terminated. When TPS "
            "is revoked, affected individuals face irregular status and increased "
            "trafficking vulnerability. No automatic TPS designation process for "
            "climate disasters exists."
        ),
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "UNHCR Legal Considerations on Climate Change and Cross-Border Displacement (2020)",
        "law": "UNHCR Climate Displacement Guidance",
        "year": 2020,
        "summary": (
            "UNHCR's 2020 legal guidance clarifies that climate-displaced persons "
            "may qualify as refugees if climate events interact with conflict or "
            "persecution. The Teitiota v. New Zealand case (UN Human Rights "
            "Committee, 2020) established that climate change-related conditions "
            "can engage non-refoulement obligations if they create life-"
            "threatening risks. While the Committee found the threshold not met in "
            "Teitiota, the ruling acknowledged that climate displacement can "
            "trigger international protection obligations — a significant legal "
            "development for reducing trafficking vulnerability of climate "
            "migrants who currently lack recognized protection status."
        ),
    },

    # =====================================================================
    # STATISTICS (~20)
    # =====================================================================
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "IDMC — Global Disaster Displacement 2022",
        "metric": "disaster_internal_displacement_2022",
        "value": "32.6 million",
        "summary": (
            "IDMC Global Report on Internal Displacement (2023): 32.6 million new "
            "internal displacements due to weather-related events in 2022. Floods "
            "caused 19.2 million (59%), storms 12.5 million (38%). Largest "
            "displacement events: Pakistan floods (8.2M), Philippines typhoons "
            "(5.5M), India monsoon floods (2.5M), Bangladesh floods (1.5M). "
            "Persons displaced by disasters are not recognized as refugees under "
            "international law, leaving them without formal protection status and "
            "reliant on irregular migration channels that increase trafficking "
            "vulnerability."
        ),
        "source": "IDMC Global Report on Internal Displacement 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "IDMC — Cumulative Disaster Displacement 2008-2022",
        "metric": "cumulative_disaster_displacement",
        "value": "376.3 million",
        "summary": (
            "IDMC data shows 376.3 million new internal displacements from "
            "disasters recorded between 2008 and 2022 (15-year period). Annual "
            "average: 25 million. Trend is increasing: 2018-2022 average was 30.7 "
            "million per year compared to 22.5 million for 2008-2012. 90%+ of "
            "disaster displacement is weather-related (floods, storms, droughts). "
            "Each displacement event represents a window of trafficking "
            "vulnerability — loss of home, livelihood, documentation, and social "
            "protection."
        ),
        "source": "IDMC",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "World Bank Groundswell — Climate Internal Migration Projections",
        "metric": "projected_climate_migrants_by_2050",
        "value": "216 million",
        "summary": (
            "World Bank Groundswell Report (updated 2021) projects 216 million "
            "internal climate migrants by 2050 across six regions under a "
            "pessimistic scenario. Breakdown: Sub-Saharan Africa 86 million, "
            "East Asia/Pacific 49 million, South Asia 40 million, North Africa "
            "19 million, Latin America 17 million, Eastern Europe/Central Asia "
            "5 million. Climate hotspot areas overlap significantly with existing "
            "trafficking origin zones. Under an optimistic climate and development "
            "scenario, number reduces to 44 million — highlighting that policy "
            "choices determine displacement-to-exploitation risk."
        ),
        "source": "World Bank Groundswell Report (2021)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Disaster-Trafficking Temporal Correlation Study (2008-2019)",
        "metric": "post_disaster_trafficking_increase",
        "value": "20-40% within 12 months",
        "summary": (
            "IOM research synthesis (2021) analyzing trafficking data in 14 "
            "countries affected by major disasters (2008-2019) found a 20-40% "
            "increase in identified trafficking cases within 12 months of a "
            "major disaster event. The increase was highest for: child trafficking "
            "(+40%), sexual exploitation (+35%), and forced domestic labour (+30%). "
            "The temporal correlation was strongest in countries with pre-existing "
            "high trafficking prevalence and weak institutional capacity. The "
            "trafficking increase persisted for 18-24 months before returning to "
            "baseline levels."
        ),
        "source": "IOM / Journal of Human Trafficking (2021)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "UNHCR Climate Refugee Projections — 1.2 Billion by 2050",
        "metric": "climate_displacement_projection",
        "value": "1.2 billion",
        "summary": (
            "Institute for Economics and Peace Ecological Threat Register (2020) "
            "projects 1.2 billion people could be displaced by climate-related "
            "events by 2050. Of these, 700 million face severe water scarcity, "
            "400 million face food insecurity, and 100+ million face coastal "
            "flooding. Projections far exceed World Bank figures as they include "
            "cross-border displacement and compound climate-conflict scenarios. "
            "The scale of projected displacement, combined with the 82% overlap "
            "between climate-vulnerable and high-trafficking countries, suggests "
            "a potential trafficking crisis of unprecedented scale."
        ),
        "source": "Institute for Economics and Peace / UNHCR",
    },
    {
        "type": "statistic",
        "jurisdiction": "PK",
        "title": "Pakistan 2022 Floods — Displacement and Trafficking Scale",
        "metric": "pakistan_flood_displacement",
        "value": "33 million displaced",
        "summary": (
            "Pakistan's 2022 monsoon floods (June-October): 33 million displaced, "
            "1,739 killed, 2.1 million homes destroyed, USD 30 billion in "
            "damages. One-third of the country submerged. Sindh Province: 7.9 "
            "million displaced, 80% of cropland destroyed. UNICEF reported 3.4 "
            "million children needed humanitarian assistance. IOM Pakistan "
            "documented trafficking risks including: bonded labour recruitment at "
            "relief camps, child marriage of displaced girls, and irregular "
            "migration facilitated by smuggling networks offering to transport "
            "families to urban centres."
        ),
        "source": "NDMA Pakistan / IOM / UNICEF / World Bank",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Philippines Post-Typhoon Trafficking Referral Increase",
        "metric": "post_typhoon_trafficking_referrals",
        "value": "+30% in affected regions",
        "summary": (
            "Philippine DSWD data across Typhoons Haiyan (2013), Mangkhut (2018), "
            "and Rai (2021) shows a consistent 25-35% increase in trafficking "
            "referrals in affected regions within 6-12 months post-disaster. "
            "Pattern: immediate displacement phase (0-3 months) sees child "
            "trafficking from evacuation centres; recovery phase (3-12 months) "
            "sees adult labour trafficking through fraudulent recruitment. Women "
            "and children account for 78% of post-disaster trafficking victims "
            "identified by DSWD."
        ),
        "source": "DSWD / IACAT / IOM Philippines",
    },
    {
        "type": "statistic",
        "jurisdiction": "NP",
        "title": "Nepal 2015 Earthquake — Border Interception Data",
        "metric": "nepal_post_earthquake_interceptions",
        "value": "5,161 intercepted",
        "summary": (
            "Maiti Nepal's border monitoring stations intercepted 5,161 potential "
            "trafficking victims at India-Nepal border crossings in the 12 months "
            "following the April 2015 earthquake — a 300% increase over the "
            "pre-earthquake annual average of ~1,300. Interceptions concentrated "
            "at: Birgunj (35%), Bhairahawa (25%), and Kakarbhitta (20%). 67% "
            "were women and girls under 25. Key vulnerabilities: loss of "
            "documentation in earthquake (42%), loss of family members (28%), "
            "complete destruction of home (65%). The data represents only those "
            "intercepted — actual trafficking numbers are estimated to be 3-5x "
            "higher."
        ),
        "source": "Maiti Nepal / National Human Rights Commission Nepal",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Climate Vulnerability and Trafficking Hotspot Overlap",
        "metric": "climate_trafficking_overlap",
        "value": "82%",
        "summary": (
            "Cross-referencing the Global Climate Risk Index (Germanwatch, "
            "2000-2019 data) with the Global Slavery Index (Walk Free Foundation, "
            "2023) reveals 82% overlap between the 30 countries most vulnerable "
            "to climate impacts and the 30 countries with highest estimated "
            "trafficking prevalence. Top overlapping countries: Bangladesh, "
            "Myanmar, Philippines, India, Pakistan, Mozambique, Haiti, Honduras, "
            "Guatemala, Ethiopia. Climate adaptation funding to these countries "
            "rarely includes anti-trafficking components — only 3 of the top 20 "
            "climate adaptation programmes include explicit trafficking protection "
            "measures."
        ),
        "source": "Germanwatch / Walk Free Foundation / IOM analysis",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO — Disaster Impact on Child Labour",
        "metric": "post_disaster_child_labour_increase",
        "value": "20-50% increase",
        "summary": (
            "ILO research across 10 disaster-affected countries (2010-2022) shows "
            "a 20-50% increase in child labour within 12-18 months of a major "
            "disaster. Mechanisms: school destruction removes children from "
            "protective environments; family income loss forces children into "
            "work; disrupted social services reduce monitoring. Worst sectors: "
            "agriculture (35% of post-disaster child labour), domestic work (20%), "
            "street work including begging (18%), and construction debris "
            "clearance (12%). Girls disproportionately pushed into domestic work "
            "and early marriage; boys into hazardous manual labour."
        ),
        "source": "ILO-IPEC / UNICEF",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Women and Girls Disproportionately Affected by Disaster Displacement",
        "metric": "women_girls_disaster_trafficking",
        "value": "71% of identified victims",
        "summary": (
            "UNODC analysis of post-disaster trafficking cases (2010-2022) found "
            "that women and girls constituted 71% of identified trafficking "
            "victims in disaster-affected areas — compared to 65% globally. "
            "Factors: pre-existing gender inequalities amplified by disaster; "
            "destruction of gendered livelihoods (home-based work, small "
            "agriculture); increased rates of gender-based violence in "
            "displacement settings; women's lower access to disaster recovery "
            "resources and legal documentation. Post-disaster sexual exploitation "
            "increased at higher rates than labour trafficking."
        ),
        "source": "UNODC / UN Women",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "IDP Camp Trafficking Vulnerability — UNHCR Assessment",
        "metric": "idp_camp_trafficking_incidents",
        "value": "60% of camps report exploitation",
        "summary": (
            "UNHCR protection monitoring across 45 displacement camps in 12 "
            "countries (2019-2023) found that 60% reported at least one suspected "
            "trafficking incident within 6 months of establishment. Most common: "
            "sexual exploitation of women and girls (42% of reported incidents), "
            "forced child labour (28%), fraudulent recruitment for external "
            "employment (18%), and forced marriage (12%). Camps with inadequate "
            "lighting, separated family areas, and limited SGBV services had 3x "
            "higher incident rates. Only 15% of camps had dedicated "
            "anti-trafficking personnel."
        ),
        "source": "UNHCR Protection Monitoring / IOM",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Climate Disaster Frequency Trend — Trafficking Risk Multiplier",
        "metric": "disaster_frequency_increase",
        "value": "5x increase since 1970",
        "summary": (
            "WMO Atlas of Mortality and Economic Losses (2021) documents a 5x "
            "increase in recorded weather-related disaster events over the past "
            "50 years (1970-2019): from ~700 per decade (1970s) to ~3,500 per "
            "decade (2010s). Each disaster event creates a trafficking "
            "vulnerability window. The increasing frequency means overlapping "
            "displacement events — populations not yet recovered from one disaster "
            "face the next. Pakistan, for example, experienced major flooding in "
            "2010, 2011, 2014, and 2022 — each event compounding vulnerability."
        ),
        "source": "World Meteorological Organization (WMO) Atlas",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Disaster Displacement Documentation Loss — Trafficking Enabler",
        "metric": "documentation_loss_in_disasters",
        "value": "35-60% of displaced lose documents",
        "summary": (
            "IOM surveys across 8 major disaster events (2013-2022) found that "
            "35-60% of displaced persons lost identity documents during the "
            "disaster. Document loss is a key trafficking enabler: undocumented "
            "persons cannot access formal employment, banking, or government "
            "services, pushing them toward informal and exploitative labour "
            "markets. Replacement timelines ranged from 3 months (Philippines "
            "post-Haiyan, fast-track programme) to 2+ years (Nepal post-"
            "earthquake, rural areas). During the documentation gap, individuals "
            "are maximally vulnerable to trafficking and exploitation."
        ),
        "source": "IOM / IDMC / NRC",
    },
    {
        "type": "statistic",
        "jurisdiction": "BD",
        "title": "Bangladesh Displacement and Irregular Migration Correlation",
        "metric": "climate_displacement_irregular_migration",
        "value": "3x higher risk",
        "summary": (
            "IOM Bangladesh research (2019) found that climate-displaced "
            "Bangladeshi migrants were 3x more likely to use irregular migration "
            "channels and accept exploitative recruitment terms compared to "
            "non-displaced migrants. Study surveyed 2,400 returnee workers from "
            "Gulf states. Climate-displaced workers: paid higher recruitment fees "
            "(average BDT 450,000 vs 280,000), more likely to experience wage "
            "withholding (72% vs 45%), and more likely to have passports "
            "confiscated (58% vs 31%). Desperation from lost livelihoods reduces "
            "ability to negotiate terms or verify employers."
        ),
        "source": "IOM Bangladesh / BRAC / Refugee and Migratory Movements Research Unit",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Climate Adaptation Funding — Anti-Trafficking Integration Gap",
        "metric": "climate_funding_trafficking_integration",
        "value": "Less than 2%",
        "summary": (
            "Analysis of 150 major climate adaptation projects funded by the "
            "Green Climate Fund and Adaptation Fund (2015-2023) found that fewer "
            "than 2% included explicit anti-trafficking or forced labour "
            "prevention components. Of USD 12.7 billion in approved climate "
            "adaptation funding, less than USD 50 million was directed to "
            "protection programming that addresses trafficking vulnerability. "
            "Conversely, fewer than 5% of counter-trafficking programmes "
            "integrate climate displacement as a vulnerability factor. This "
            "siloed approach leaves a critical protection gap."
        ),
        "source": "Green Climate Fund / Adaptation Fund / IOM analysis",
    },

    # =====================================================================
    # ADVISORIES (~15)
    # =====================================================================
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "IOM Guidelines on Counter-Trafficking in Crisis Situations (2015)",
        "summary": (
            "IOM's 'Addressing Human Trafficking and Exploitation in Times of "
            "Crisis' (2015) provides operational guidance for integrating "
            "counter-trafficking into humanitarian response. Key elements: early "
            "identification of trafficking risks at onset of crisis; protection "
            "screening at displacement sites; safe referral pathways for "
            "identified victims; awareness-raising targeting displaced populations "
            "about trafficking risks; and coordination between humanitarian "
            "actors, law enforcement, and anti-trafficking agencies. The guidance "
            "was developed after documenting post-disaster trafficking patterns in "
            "the Philippines, Nepal, Haiti, and Syria."
        ),
        "source": "IOM",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNHCR — Climate Change and Trafficking Nexus Guidance (2022)",
        "summary": (
            "UNHCR guidance note (2022) on the nexus between climate change and "
            "human trafficking. Identifies three primary pathways: (1) slow-onset "
            "climate degradation destroying livelihoods, forcing migration through "
            "irregular channels; (2) sudden-onset disasters creating displacement "
            "and exploitation opportunities; (3) climate-conflict interaction "
            "displacing populations into areas controlled by trafficking networks. "
            "Recommends: climate-sensitive protection assessments, inclusion of "
            "anti-trafficking expertise in disaster response, and legal pathways "
            "for climate-displaced persons to reduce reliance on smugglers."
        ),
        "source": "UNHCR",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "OCHA — Protection Cluster Guidance on Disaster Displacement",
        "summary": (
            "UN OCHA Protection Cluster guidance on protection of displaced "
            "persons in natural disasters. Establishes minimum standards "
            "including: camp management protocols to prevent trafficking (lighting, "
            "separated registration, family tracing); monitoring of labour "
            "recruitment at displacement sites; SGBV prevention and response; and "
            "child protection including prevention of family separation. Protection "
            "cluster activated in all L3 (system-wide) emergency responses. "
            "Guidance updated in 2021 to include climate-specific displacement "
            "scenarios and trafficking risk indicators."
        ),
        "source": "UN OCHA / Global Protection Cluster",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "US TIP Report — Climate Change as Emerging Trafficking Driver (2022-2024)",
        "summary": (
            "US State Department TIP Reports (2022, 2023, 2024) increasingly "
            "highlight climate change as a trafficking driver. 2022 report: "
            "dedicated section on 'Climate Change and Human Trafficking' noting "
            "that environmental degradation 'exacerbates the vulnerabilities that "
            "traffickers exploit.' 2023 report: expanded analysis of disaster "
            "displacement-trafficking nexus with country-specific examples. 2024 "
            "report: recommends governments 'integrate counter-trafficking "
            "measures into climate adaptation strategies and disaster response "
            "protocols.' Tier ranking methodology does not yet formally assess "
            "climate-trafficking response."
        ),
        "source": "US Department of State / Office to Monitor and Combat Trafficking",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNODC — Climate Change as Trafficking Driver (2022 Global Report)",
        "summary": (
            "UNODC Global Report on Trafficking in Persons (2022) identifies "
            "climate change as an emerging trafficking driver. Key findings: "
            "environmental degradation destroys livelihoods, increases poverty, "
            "creates displacement — all recognized vulnerability factors for "
            "trafficking. Post-disaster chaos provides operational cover for "
            "traffickers. Climate-affected women and children are "
            "disproportionately targeted. Report recommends: climate-sensitive "
            "anti-trafficking policies, enhanced protection for climate-displaced "
            "persons, and integration of counter-trafficking into climate "
            "adaptation and disaster response frameworks."
        ),
        "source": "UNODC",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "IASC — Anti-Trafficking in Humanitarian Action Protocol",
        "summary": (
            "Inter-Agency Standing Committee (IASC) guidelines on integrating "
            "anti-trafficking measures into humanitarian action (updated 2023). "
            "Framework covers: risk assessment at onset of humanitarian crises "
            "including natural disasters; minimum protection standards at "
            "displacement sites; safe and ethical recruitment monitoring during "
            "recovery operations; coordination between humanitarian clusters and "
            "national anti-trafficking mechanisms. IASC guidelines are the "
            "operational standard for all UN humanitarian responses and include "
            "specific disaster-displacement-trafficking risk matrices."
        ),
        "source": "IASC / IOM / UNHCR",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Platform on Disaster Displacement — Bridging Protection Gaps",
        "summary": (
            "The Platform on Disaster Displacement (PDD, successor to the Nansen "
            "Initiative, 2016-present) works to implement the Protection Agenda "
            "for cross-border disaster-displaced persons. PDD identifies "
            "trafficking as a key risk for disaster-displaced persons who cross "
            "borders without legal status. Recommends: temporary protection "
            "mechanisms, humanitarian visas, regional free movement agreements, "
            "and bilateral agreements for planned relocation. PDD coordinates "
            "with UNHCR, IOM, and national governments. Achievements include "
            "regional consultations in Pacific, Central America, and Horn of "
            "Africa on disaster displacement protection standards."
        ),
        "source": "Platform on Disaster Displacement / Nansen Initiative",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "GFMD — Climate Migration and Trafficking Thematic Session (2023)",
        "summary": (
            "Global Forum on Migration and Development (GFMD) 2023 thematic "
            "session addressed the climate-trafficking nexus for the first time "
            "as a standalone agenda item. Recommendations: states should develop "
            "legal pathways for climate-displaced persons to reduce irregular "
            "migration; climate adaptation programmes should include anti-"
            "trafficking components; disaster risk reduction should integrate "
            "trafficking risk assessment; and development financing should fund "
            "protection for climate-displaced populations. The session brought "
            "together counter-trafficking and climate policy communities that "
            "traditionally operate in separate silos."
        ),
        "source": "GFMD / IOM / ILO",
    },
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "IACAT Philippines — Anti-Trafficking in Disaster Response Protocol",
        "summary": (
            "The Philippine Inter-Agency Council Against Trafficking (IACAT) "
            "developed a specific protocol for anti-trafficking in disaster "
            "response (piloted after Typhoon Haiyan 2013, formalized 2016). "
            "Protocol includes: deployment of anti-trafficking officers to "
            "evacuation centres within 72 hours; monitoring of transport terminals "
            "for suspicious movement of children and women; registration of all "
            "displaced persons at official sites; coordination with POEA/DMW on "
            "overseas recruitment monitoring in affected areas; and community "
            "awareness campaigns on trafficking risks. The Philippines model is "
            "cited by IOM as a best practice for disaster-trafficking response."
        ),
        "source": "IACAT / IOM / DSWD",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Save the Children — Child Protection in Emergencies and Climate Displacement",
        "summary": (
            "Save the Children's guidance on child protection in climate-related "
            "emergencies (2022) addresses the specific trafficking risks facing "
            "children displaced by disasters. Key recommendations: immediate "
            "family tracing and reunification; registration of unaccompanied and "
            "separated children; monitoring of informal adoption and orphanage "
            "placement; education continuity as protective factor; adolescent "
            "livelihood programmes to prevent labour exploitation. Guidance "
            "developed from experience in Philippines (Haiyan), Nepal (2015 "
            "earthquake), Bangladesh (cyclones), and Mozambique (Cyclone Idai). "
            "Emphasizes that school destruction removes the primary protective "
            "environment for children."
        ),
        "source": "Save the Children / Alliance for Child Protection in Humanitarian Action",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO — Just Transition and Prevention of Exploitation in Green Economy",
        "summary": (
            "ILO guidance (2023) on ensuring just transition to green economy "
            "does not create new exploitation patterns. Addresses: workers "
            "displaced from fossil fuel sectors entering informal markets; "
            "exploitation in renewable energy supply chains (solar, wind, EV "
            "batteries); climate adaptation infrastructure construction using "
            "migrant labour; and 'green grabbing' — land acquisition for "
            "climate projects displacing indigenous and rural communities into "
            "vulnerability. Recommends: labour standards in all climate "
            "investment, supply chain due diligence for green technologies, and "
            "retraining programmes for displaced workers with trafficking "
            "vulnerability screening."
        ),
        "source": "ILO / ITUC / Business and Human Rights Resource Centre",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Red Cross/Red Crescent — Climate Disasters and Protection Minimum Standards",
        "summary": (
            "IFRC and ICRC protection framework (updated 2022) establishes "
            "minimum standards for protection of persons affected by climate-"
            "related disasters. Standards include: prevention of trafficking and "
            "exploitation during displacement; safe and dignified conditions in "
            "temporary shelters; monitoring of labour recruitment in disaster "
            "zones; restoring family links and preventing separation; and access "
            "to legal assistance for displaced persons. IFRC's network of 192 "
            "National Societies operationalizes these standards. The framework "
            "recognizes that climate disasters increasingly overlap with conflict "
            "and economic crises, compounding protection needs."
        ),
        "source": "IFRC / ICRC",
    },
    {
        "type": "advisory",
        "jurisdiction": "BD",
        "title": "Bangladesh — Anti-Trafficking Protocols for Cox's Bazar Climate Displacement",
        "summary": (
            "Specialized anti-trafficking protocols developed for Cox's Bazar "
            "district (2019, updated 2023), where Rohingya refugee camps face "
            "compounding climate vulnerability from monsoon flooding. Protocols "
            "include: dedicated trafficking focal points in each camp zone; "
            "monitoring of departure points during monsoon season (when flooding "
            "triggers secondary displacement); awareness campaigns in Rohingya "
            "and Chittagonian languages; coordination with Bangladesh Coast Guard "
            "on maritime trafficking routes; and safe house network for identified "
            "victims. Model developed by IOM, UNHCR, and Bangladesh government "
            "represents emerging best practice for climate-compound displacement."
        ),
        "source": "IOM Bangladesh / UNHCR / Anti-Trafficking Working Group",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "COP28 Loss and Damage Fund — Anti-Trafficking Integration Recommendation",
        "summary": (
            "At COP28 (December 2023), the operationalization of the Loss and "
            "Damage Fund (initial pledges of USD 700 million) generated "
            "recommendations from civil society — including IOM and anti-"
            "trafficking organizations — to integrate human trafficking prevention "
            "into loss and damage programming. Specific recommendations: earmark "
            "a percentage of loss and damage funding for protection programming; "
            "require trafficking risk assessments in funded projects; support "
            "legal pathways for climate-displaced persons; and fund anti-"
            "trafficking capacity in disaster-prone countries. As of 2025, no "
            "formal anti-trafficking criteria have been incorporated into the "
            "Fund's operational guidelines."
        ),
        "source": "COP28 Presidency / IOM / Global Alliance Against Traffic in Women",
    },
]
