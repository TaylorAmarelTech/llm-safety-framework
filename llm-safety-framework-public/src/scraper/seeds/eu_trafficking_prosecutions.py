"""EU trafficking prosecutions — national court cases and anti-trafficking enforcement across Europe."""

EU_TRAFFICKING_PROSECUTION_FACTS: list[dict] = [
    # ======================================================================
    # UNITED KINGDOM (1-30)
    # ======================================================================

    # ── Landmark UK cases ─────────────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v SK [2011] — Domestic Servitude Landmark",
        "summary": "First successful prosecution under Section 71 of the Coroners and Justice Act 2009 for holding a person in servitude. A Tanzanian woman was kept as a domestic servant in London, working 18-hour days without pay, passport confiscated. Defendant convicted and sentenced to community order. Case exposed gaps in sentencing for modern slavery offences.",
        "source": "Crown Court (Harrow) / CPS case records",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v Connors and Others [2013] — Traveller Labour Exploitation",
        "summary": "Members of the Connors family convicted at Luton Crown Court for conspiracy to hold persons in servitude and require forced labour. Victims, many recruited from homeless shelters and soup kitchens, forced to work on driveways and building sites for little or no pay. Lived in squalid conditions on traveller sites. Sentences ranged from 3 to 8 years. Described as largest forced labour prosecution in UK at the time.",
        "source": "Crown Court (Luton) / GRETA UK Evaluation Report 2012",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v Connors Family — Appeal Judgment [2013] EWCA Crim 324",
        "summary": "Court of Appeal upheld convictions of the Connors family for servitude and forced labour offences. Confirmed that victims' vulnerability (homelessness, addiction, learning disabilities) was a key factor in establishing coercion. Sentences of some defendants increased on appeal by the Attorney General's reference as unduly lenient.",
        "source": "Court of Appeal (Criminal Division) / EWCA Crim 324",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Operation Fort — Largest UK Modern Slavery Case (2019)",
        "summary": "West Midlands Police Operation Fort resulted in convictions of a Polish trafficking network that exploited over 400 victims over 8 years. Victims recruited from Poland with promises of legitimate work, housed in overcrowded properties in Birmingham, wages stolen. Ringleaders Ignacy Brzezinski and Wojciech Nowakowski sentenced to 11 and 7.5 years respectively. Estimated GBP 2 million in stolen wages.",
        "source": "Birmingham Crown Court / West Midlands Police / NCA",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Operation Fort — Victim Compensation Orders (2020)",
        "summary": "Following the Operation Fort convictions, the court issued compensation orders totalling over GBP 500,000 for victims. Many victims had worked in recycling centres, agriculture, and food production across the West Midlands. The Modern Slavery Victim Care Contract provided support during and after trial proceedings.",
        "source": "Birmingham Crown Court / Salvation Army MSVCC",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Vietnamese Cannabis Farm Trafficking — R v N and Others [2012]",
        "summary": "Multiple Vietnamese nationals prosecuted for cultivating cannabis while being trafficked. Court of Appeal ruled that children and young people exploited in cannabis farms should be treated as victims, not criminals. Established the defence of compulsion under the non-punishment principle. Led to CPS guidance on identifying trafficking victims among cannabis cultivators.",
        "source": "Court of Appeal / CPS guidance on cannabis cultivation and trafficking",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v L and Others [2013] EWCA Crim 991 — Non-Punishment of Trafficking Victims",
        "summary": "Court of Appeal landmark ruling establishing that where trafficking victims commit criminal offences as a direct consequence of being trafficked, prosecutions should not proceed. Three Vietnamese teenagers convicted of cannabis cultivation had convictions quashed. Extended protection to adults in compelling circumstances.",
        "source": "Court of Appeal (Criminal Division) / EWCA Crim 991",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Nail Bar Trafficking — Operation Magnify (2016)",
        "summary": "Metropolitan Police investigation into Vietnamese trafficking network supplying workers to nail bars across London and the South East. Victims worked 12-14 hour days, living in overcrowded flats above salons. Debts of GBP 30,000-40,000 imposed for smuggling costs. Four defendants convicted of trafficking for labour exploitation.",
        "source": "Southwark Crown Court / Metropolitan Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Nail Bar Trafficking — Operation Cardinas (2018)",
        "summary": "NCA-led operation targeting Vietnamese nail bar trafficking across multiple UK regions. Investigation revealed victims recruited in Vietnam, smuggled via Russia and Eastern Europe, placed in nail bars where wages were seized. Victims exposed to harmful chemicals without protective equipment. Network dismantled with 9 convictions.",
        "source": "National Crime Agency / various Crown Courts",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Car Wash Exploitation — Kozani and Others [2017]",
        "summary": "Albanian nationals convicted of trafficking and labour exploitation at hand car washes in Kent. Workers paid as little as GBP 20 for 12-hour shifts, housed in caravans. Gangmasters Licensing Authority and police joint operation identified systematic wage theft and debt bondage across multiple car wash sites.",
        "source": "Canterbury Crown Court / GLAA / Kent Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Hand Car Wash Project — GLAA National Assessment (2018)",
        "summary": "Gangmasters and Labour Abuse Authority assessed over 250 hand car wash sites across England and Wales. Found indicators of labour exploitation in 49% of sites inspected. Common indicators included workers living on site, no employment contracts, below minimum wage payments, and cash-only operations. Led to the Safe Car Wash app for public reporting.",
        "source": "Gangmasters and Labour Abuse Authority (GLAA) / University of Nottingham",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Agricultural Gangmaster Case — Operation Pottery (2014)",
        "summary": "Lithuanian gangmaster Viktoras Margevicius convicted at Nottingham Crown Court for trafficking Lithuanian workers into agricultural labour in Lincolnshire. Workers harvested crops for major supermarket suppliers, earned below minimum wage after deductions for accommodation and transport. Sentenced to 5 years imprisonment.",
        "source": "Nottingham Crown Court / GLAA / Lincolnshire Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Morecambe Bay Cockle Pickers — R v Lin Liang Ren [2006]",
        "summary": "Chinese gangmaster Lin Liang Ren convicted of manslaughter of 21 Chinese cockle pickers who drowned in Morecambe Bay in February 2004. Workers were undocumented migrants controlled through debt bondage. Sentenced to 14 years. Tragedy led directly to the Gangmasters (Licensing) Act 2004 and creation of the GLA.",
        "source": "Preston Crown Court / HSE Investigation Report",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Agricultural Gang Labour — Operation Bramber (2017)",
        "summary": "Polish organised crime group convicted of trafficking Polish nationals into forced agricultural labour across East Anglia. Victims picked vegetables and worked in food processing plants supplying major supermarkets. Wages garnished through controlled bank accounts. Six defendants sentenced to combined 27 years.",
        "source": "Ipswich Crown Court / NCA / Suffolk Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v Rooney and Others [2017] — Traveller Slavery in Lincolnshire",
        "summary": "Members of the Rooney family convicted at Nottingham Crown Court for holding 18 victims in servitude on a caravan site in Lincolnshire over 25 years. Victims forced to perform hard labour including block-paving and landscaping. Longest-held victim exploited for over a decade. Lead defendants received sentences of 15 and 11 years.",
        "source": "Nottingham Crown Court / Lincolnshire Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Modern Slavery Act 2015 — First Slavery and Trafficking Prevention Order (2016)",
        "summary": "First Slavery and Trafficking Prevention Order issued under the Modern Slavery Act 2015 against a man convicted of labour trafficking in the construction sector. Order imposed restrictions on recruitment activities, contact with vulnerable persons, and international travel for 5 years. Breach carries imprisonment of up to 5 years.",
        "source": "Magistrates' Court / Home Office guidance on STROs/STPOs",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Operation Cardwell — Fishing Industry Trafficking (2019)",
        "summary": "Three men convicted at Truro Crown Court for trafficking Filipino and Ghanaian nationals to work on fishing vessels operating from Cornish ports. Workers paid as little as GBP 3 per hour, documents confiscated, denied shore leave. Police identified victims after sea rescue. Led to enhanced scrutiny of fishing industry labour practices.",
        "source": "Truro Crown Court / Devon and Cornwall Police / ITF",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v Zielinski [2017] — Poultry Processing Exploitation",
        "summary": "Polish gangmaster convicted of trafficking compatriots into poultry processing plants in Norfolk. Workers charged excessive rent for substandard housing, wages controlled via bank accounts held by the gangmaster. Workers processed poultry for a major UK supermarket supply chain. Sentenced to 4.5 years.",
        "source": "Norwich Crown Court / GLAA investigation",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Operation Melrose — Egg Production Trafficking (2020)",
        "summary": "Four Czech nationals convicted of labour exploitation in egg production facilities in Kent and Shropshire. Victims recruited from Czech Republic and Slovakia, controlled through debt for travel and accommodation. Worked in hazardous conditions handling chemicals without protection. GBP 1.2 million in wages withheld.",
        "source": "Birmingham Crown Court / GLAA / NCA",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Section 54 Modern Slavery Act — First Corporate Fine (2020)",
        "summary": "Independent Anti-Slavery Commissioner highlighted enforcement failures under Section 54 (transparency in supply chains). No company fined for non-compliance by 2020 despite widespread failure to publish adequate modern slavery statements. Calls for mandatory reporting, financial penalties, and director liability grew stronger.",
        "source": "IASC Annual Report 2020 / UK Parliament Joint Committee on Human Rights",
    },

    # ======================================================================
    # ITALY (31-60)
    # ======================================================================

    # ── Caporalato and Agricultural Exploitation ──────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Rosarno Riots and Subsequent Prosecutions (2010-2013)",
        "summary": "After African migrant workers in Rosarno, Calabria, rioted against exploitative conditions in January 2010, Italian authorities prosecuted farm owners and caporali (illegal gangmasters). Workers had earned EUR 25 per 12-hour day picking oranges, housed in abandoned factories. Several farm owners convicted of labour exploitation under Article 603-bis of the Penal Code.",
        "source": "Tribunale di Palmi / ILO Committee of Experts observations on Italy",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Puglia Caporalato — Operation Ferrara (2015)",
        "summary": "Carabinieri dismantled caporalato network exploiting Romanian and Bulgarian workers in tomato harvesting across Puglia (Foggia province). Workers paid EUR 2-3 per crate, charged for water and transport, housed in informal settlements (ghettos). 12 caporali arrested, charged under Art. 603-bis as amended by Law 199/2016.",
        "source": "Tribunale di Foggia / Carabinieri / Osservatorio Placido Rizzotto",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Law 199/2016 — Strengthened Anti-Caporalato Legislation",
        "summary": "Italy enacted Law 199/2016 after the death of migrant worker Paola Clemente in Puglia. Amended Art. 603-bis of the Penal Code to criminalise not only the caporale (intermediary) but also the employer who exploits workers. Introduced sentences of 1-6 years and fines of EUR 500-1000 per worker. Asset confiscation provisions added.",
        "source": "Gazzetta Ufficiale No. 257 / Italian Parliament Act 199/2016",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Death of Paola Clemente (2015) — Catalyst for Reform",
        "summary": "Paola Clemente, a 49-year-old Italian agricultural worker, died of heatstroke while harvesting grapes in Andria, Puglia, earning EUR 27 per day through a caporale. Her death sparked national outrage and directly led to Law 199/2016 strengthening anti-caporalato provisions. Prosecutors investigated the entire intermediary chain.",
        "source": "Procura della Repubblica di Trani / Italian media reporting",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Calabria Caporalato — Orange Harvest Exploitation (2018)",
        "summary": "Court in Cosenza convicted 7 defendants for caporalato offences exploiting sub-Saharan African workers in the orange harvest season. Workers paid EUR 1 per crate, deductions for transport and tools. Ndrangheta-linked agricultural businesses identified. Sentences ranged from 2 to 6 years. Assets of agricultural companies seized.",
        "source": "Tribunale di Cosenza / DDA Catanzaro",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Campania Agricultural Exploitation — Operation Terra Promessa (2019)",
        "summary": "Naples prosecutors charged 22 individuals with trafficking and caporalato in the agricultural sector across Campania. Indian and Pakistani workers exploited in dairy and agricultural operations in the Caserta area (Castel Volturno). Workers paid EUR 2-3 per hour, housed in overcrowded buildings controlled by gangmasters.",
        "source": "Procura della Repubblica di Napoli / Carabinieri",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Ragusa Greenhouse Exploitation — Romanian Workers (2017)",
        "summary": "Tribunale di Ragusa convicted agricultural employers and intermediaries for exploiting Romanian workers in greenhouse operations in Sicily. Workers cultivated tomatoes and vegetables in extreme heat, paid below minimum wage, housed in containers on farm properties. Female workers subjected to sexual harassment and exploitation.",
        "source": "Tribunale di Ragusa / CGIL Sicilia",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Saluzzo Fruit Harvest — West African Worker Exploitation (2020)",
        "summary": "Prosecutors in Cuneo investigated systematic exploitation of West African workers in the fruit harvest season in Saluzzo, Piedmont. Workers recruited through informal networks, paid EUR 3-4 per hour, housed in tents and abandoned buildings. Investigation led to 5 arrests and identification of 120 exploited workers.",
        "source": "Procura della Repubblica di Cuneo / Caritas Saluzzo",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Terracina Sikh Worker Case — Pontine Marshes (2019)",
        "summary": "Major prosecution in Latina province targeting exploitation of Indian Sikh workers in the Pontine Marshes agricultural sector. Over 400 Sikh workers exploited in greenhouses and fields, paid EUR 4 per hour, controlled through debt for travel costs. Some workers had substances added to drinks to increase productivity. Employers and caporali convicted.",
        "source": "Tribunale di Latina / FLAI-CGIL",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Foggia Ghetto Fires — Manslaughter Investigations (2018-2020)",
        "summary": "Multiple fires in informal migrant worker camps (ghettos) near Foggia killed several African agricultural workers. Prosecutors investigated employers and caporali for creating conditions of exploitation that forced workers into dangerous housing. The Borgo Mezzanone camp housed over 3,000 workers in peak season. Convictions for caporalato obtained alongside manslaughter charges.",
        "source": "Procura della Repubblica di Foggia / UNHCR Italy",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Basilicata Tomato Harvest — Operation Ndrangheta Roots (2021)",
        "summary": "Anti-mafia prosecutors in Potenza dismantled a network exploiting 200+ African workers in tomato harvesting across Basilicata and Puglia. The network was linked to Ndrangheta clans controlling agricultural supply chains. Workers paid EUR 20 for 10-hour days, with EUR 5 deducted for transport. 14 arrests made.",
        "source": "DDA Potenza / Guardia di Finanza",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "COVID-19 Regularisation and Exploitation — Post-Amnesty Prosecutions (2020-2021)",
        "summary": "Italy's 2020 COVID regularisation (Sanatoria) allowed undocumented agricultural workers to obtain temporary permits. Prosecutors subsequently investigated employers who exploited the process, charging workers EUR 5,000-7,000 for sponsorship while continuing exploitative conditions. Multiple caporalato prosecutions initiated across Southern Italy.",
        "source": "Ministero dell'Interno / IDOS Dossier Statistico Immigrazione 2021",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Vittoria Greenhouse Complex — Romanian Labour Trafficking (2016)",
        "summary": "Tribunale di Ragusa convicted 8 defendants for trafficking Romanian nationals to work in greenhouse complexes around Vittoria, Sicily. Workers housed in overcrowded, unheated structures on agricultural estates. Women subjected to sexual exploitation by employers in addition to labour exploitation. Sentences of 4-10 years imposed.",
        "source": "Tribunale di Ragusa / Direzione Distrettuale Antimafia",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Piana di Gioia Tauro — Migrant Worker Exploitation (2021)",
        "summary": "Prosecutors charged 25 individuals with organised caporalato in the Piana di Gioia Tauro plain, Calabria. Network exploited hundreds of African workers in citrus fruit harvesting over a decade. Workers housed in the Tendopoli camp of San Ferdinando, earning EUR 1-2 per crate. Assets worth EUR 3 million confiscated from agricultural businesses.",
        "source": "DDA Reggio Calabria / Prefettura di Reggio Calabria",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Satnam Singh Death — Latina Province (2024)",
        "summary": "Indian agricultural worker Satnam Singh died after his arm was severed by farm machinery in Latina, and his employer dumped him on a roadside instead of calling emergency services. The case shocked Italy and led to renewed calls for enforcement of anti-caporalato laws. The employer was charged with manslaughter and labour exploitation. Sparked national protests and legislative review.",
        "source": "Procura della Repubblica di Latina / Italian government response 2024",
    },

    # ======================================================================
    # SPAIN (61-85)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "El Ejido Agricultural Exploitation — Almeria Prosecutions (2012-2018)",
        "summary": "Spanish prosecutors brought multiple cases against greenhouse operators in El Ejido, Almeria, for exploiting migrant workers from Morocco and sub-Saharan Africa. Workers earned EUR 20-30 per day, housed in chabolas (shacks) made of plastic sheeting. Employers convicted of labour rights violations, though trafficking charges proved difficult under Spanish law at the time.",
        "source": "Juzgado de Instruccion de El Ejido / Guardia Civil",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Almeria Greenhouse Deaths — Heat Exposure Investigations (2019)",
        "summary": "Three migrant workers died of heatstroke while working in plastic greenhouses (invernaderos) in Almeria during a summer heatwave. Prosecutors investigated employers for failing to provide water, rest breaks, and ventilation. Two employers convicted of occupational safety violations, though penalties were fines rather than imprisonment.",
        "source": "Juzgado de lo Penal de Almeria / Inspecccion de Trabajo",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Strawberry Picker Cases — Huelva Province (2018-2020)",
        "summary": "Moroccan women recruited as seasonal strawberry pickers in Huelva under bilateral agreements reported sexual harassment, abuse, and exploitative working conditions. Spanish prosecutors investigated multiple farm operators. Some cases resulted in convictions for labour rights violations. The cases led to reforms in the seasonal worker programme between Morocco and Spain.",
        "source": "Juzgado de Instruccion de Huelva / Spanish Ombudsman / CEDAW Committee",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Operation Tundra — Strawberry Sector Trafficking (2019)",
        "summary": "Guardia Civil dismantled a trafficking network exploiting Eastern European workers in strawberry harvesting in Huelva. Workers from Romania and Bulgaria recruited with false promises, housed in containers, wages withheld. Network operated across multiple growing seasons. 8 arrests, 35 victims identified.",
        "source": "Guardia Civil / Juzgado de Instruccion de Moguer",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Chinese Textile Workshop Raids — Madrid and Barcelona (2015)",
        "summary": "Spanish National Police and Labour Inspectorate raided over 50 Chinese-owned textile workshops in Madrid's Usera district and Barcelona's Badalona. Workers, mainly undocumented Chinese nationals, worked 16-hour days stitching garments. Prosecution of 12 workshop operators for trafficking and labour exploitation. Convictions under Article 177 bis (trafficking) and Article 312 (illegal employment) of the Penal Code.",
        "source": "Policia Nacional / Audiencia Nacional",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Operation Kangra — Chinese Garment Sweatshop Network (2017)",
        "summary": "National Police operation targeting a Chinese trafficking network that brought workers from Wenzhou to work in garment factories across Catalonia. Victims worked up to 18 hours daily, slept in factory buildings, passports confiscated. Debts of EUR 20,000-30,000 imposed for smuggling. 15 arrests, EUR 2 million in assets seized.",
        "source": "Policia Nacional / Audiencia Provincial de Barcelona",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Murcia Agricultural Exploitation — Pakistani Workers (2020)",
        "summary": "Guardia Civil investigated exploitation of Pakistani migrant workers in Murcian agriculture (lettuce and broccoli harvesting). Workers earned EUR 15 per day, housed in abandoned rural buildings. Labour inspectors identified widespread violations including lack of contracts, non-payment of social security, and excessive working hours. Multiple employer sanctions imposed.",
        "source": "Guardia Civil Murcia / Inspeccion de Trabajo de Murcia",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Operation Aquiles — Olive Harvest Trafficking (2018)",
        "summary": "Guardia Civil dismantled a network trafficking Romanian workers for olive harvesting in Jaen province. Workers recruited in Romania with promises of EUR 50 per day, actual earnings EUR 15-20 after deductions. Housed in overcrowded cortijos (rural estates). 6 organisers arrested and charged under Art. 177 bis of the Penal Code.",
        "source": "Guardia Civil / Juzgado de Instruccion de Jaen",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Catalonia Meat Processing — Latin American Worker Exploitation (2021)",
        "summary": "Labour inspectors in Girona and Lleida investigated meat processing plants exploiting workers from Honduras, Ecuador, and Colombia. Workers recruited through subcontractors, paid below minimum wage, excessive overtime unpaid. Two companies fined over EUR 400,000 and required to regularise employment contracts for 90 workers.",
        "source": "Inspeccion de Trabajo de Cataluna / Sindic de Greuges de Catalunya",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Canary Islands Fishing Exploitation — Senegalese Workers (2019)",
        "summary": "Prosecutors in Las Palmas investigated exploitation of Senegalese and Ghanaian workers on fishing vessels operating from Canary Island ports. Workers paid EUR 200-300 per month for continuous work at sea, no employment contracts, dangerous conditions. Two vessel owners convicted of labour exploitation offences.",
        "source": "Juzgado de lo Penal de Las Palmas / ITF",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Spanish Anti-Trafficking Plan 2021-2023 — Implementation Assessment",
        "summary": "GRETA evaluated Spain's implementation of its national anti-trafficking plan. Found improvements in victim identification but persistent challenges in prosecuting labour trafficking. Of 277 trafficking investigations in 2020, only 12% concerned labour exploitation. Recommended strengthening labour inspectorate powers and increasing prosecutorial specialisation.",
        "source": "GRETA Second Evaluation Report on Spain (2022)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Lleida Fruit Harvest — Sub-Saharan African Workers (2021)",
        "summary": "Mass exploitation of seasonal fruit pickers in Lleida exposed by labour inspectors. Over 300 workers from Mali, Senegal, and Gambia identified living in abandoned buildings and encampments. Employers systematically avoided formal contracts, paid below minimum wage. Municipal and regional authorities criticised for inadequate housing provision. Multiple employer sanctions.",
        "source": "Inspeccion de Trabajo de Lleida / Sindicatura de Greuges",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Valencia Construction Sector — Romanian Trafficking Network (2016)",
        "summary": "Policia Nacional dismantled a trafficking network exploiting Romanian construction workers in Valencia and Alicante. Workers recruited with promises of EUR 60 per day, actual payment EUR 20 after deductions for housing and transport. Network also trafficked women for sexual exploitation. 14 defendants convicted, sentences of 5-9 years.",
        "source": "Audiencia Provincial de Valencia / Policia Nacional",
    },

    # ======================================================================
    # FRANCE (86-110)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Domestic Servitude — Cour de Cassation Landmark (2009)",
        "summary": "France's highest court upheld conviction for holding a person in conditions contrary to human dignity (Article 225-14 of the Penal Code). An Ivorian woman kept as a domestic servant in Paris for 4 years, working from 6am to midnight, sleeping on the floor, no days off, passport confiscated. Court affirmed that vulnerability of immigration status constitutes a form of coercion.",
        "source": "Cour de Cassation, Chambre Criminelle / GRETA France Report",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Comite Contre l'Esclavage Moderne (CCEM) — Domestic Servitude Cases (2005-2020)",
        "summary": "CCEM, France's primary anti-slavery NGO, supported over 800 domestic servitude cases between 2005 and 2020. Typical profile: West African or South Asian woman brought to France by employer (often diplomat or wealthy family), passport confiscated, unpaid labour. Conviction rate improved from under 10% to over 40% after legal reforms and ECHR Siliadin judgment.",
        "source": "CCEM annual reports / French Ministry of Justice statistics",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Post-Siliadin Reforms — Article 225-4-1 et seq. of the Penal Code (2013)",
        "summary": "France reformed trafficking and slavery provisions in the Penal Code following the ECHR Siliadin v. France judgment. Articles 225-4-1 to 225-4-9 now specifically criminalise trafficking in human beings with penalties of 7-10 years imprisonment. Forced labour and servitude carry 5-7 years. Reforms addressed the legal gap identified by Strasbourg.",
        "source": "Code Penal (Loi 2013-711) / GRETA France Evaluation",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Construction Sector — Romanian Workers on Paris Building Sites (2017)",
        "summary": "Tribunal Correctionnel de Paris convicted 6 members of a network exploiting Romanian construction workers on building sites in Ile-de-France. Workers recruited in Romania, housed in overcrowded squats in Seine-Saint-Denis, paid EUR 4-5 per hour. Network used false posting of workers certificates to avoid French labour laws. Sentences of 3-7 years.",
        "source": "Tribunal Correctionnel de Paris / OCLTI (Office Central de Lutte contre le Travail Illegal)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Operation Titan — Construction Worker Trafficking Ring (2019)",
        "summary": "Gendarmerie and OCLTI dismantled a large-scale trafficking network exploiting Eastern European workers in construction projects across multiple French regions. Workers from Moldova and Ukraine brought via Poland, employed through cascading subcontractors. EUR 10 million in unpaid wages and social contributions. 23 arrests, assets of EUR 5 million seized.",
        "source": "OCLTI / Tribunal Judiciaire de Lyon",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Agricultural Exploitation — Loire Valley Wine Harvest (2018)",
        "summary": "Prosecutors in Tours investigated systematic exploitation of Bulgarian workers during grape harvest in the Loire Valley. Workers recruited by Bulgarian intermediaries, paid EUR 300 per month for 12-hour days. Housed in caravans without sanitation. Labour inspectors identified 80 workers in conditions of exploitation across 15 vineyards.",
        "source": "Tribunal Correctionnel de Tours / Inspection du Travail",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Berry Harvest — Seasonal Worker Exploitation in Dordogne (2020)",
        "summary": "Labour inspectors investigated exploitation of Moroccan seasonal workers in strawberry and walnut harvesting in Dordogne. Workers brought under OFII (Office Francais de l'Immigration et de l'Integration) seasonal contracts but subjected to conditions exceeding contract terms. Three farm operators fined, one prosecuted for undeclared labour.",
        "source": "Inspection du Travail Dordogne / OFII",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Chinese Textile Workers — Aubervilliers Workshops (2015)",
        "summary": "Police raided 30 clandestine textile workshops in Aubervilliers (Seine-Saint-Denis) exploiting undocumented Chinese workers. Workers sewed garments for Parisian wholesale market (Sentier), sleeping in workshops, earning EUR 2-3 per hour. Five workshop operators convicted of trafficking. Investigation linked to broader Chinese immigration trafficking networks.",
        "source": "Tribunal Correctionnel de Bobigny / Prefecture de Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Diplomatic Immunity Cases — Domestic Workers of Diplomats (2011-2020)",
        "summary": "French courts dealt with multiple cases of domestic workers exploited by diplomats claiming immunity. In landmark rulings, courts held that diplomatic immunity does not extend to private employment relationships. Several former diplomats convicted in absentia. France reformed its approach to require embassies to register domestic workers and guarantee minimum wages.",
        "source": "Tribunal de Grande Instance de Paris / Ministry of Foreign Affairs protocol",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Bouches-du-Rhone Agricultural Exploitation (2021)",
        "summary": "Prosecutors in Marseille investigated exploitation of North African workers in market gardening around the Etang de Berre. Workers, many undocumented, paid EUR 3 per hour for physical labour in fields. One worker died of heatstroke, triggering investigation. Three agricultural operators convicted of employing unauthorised workers in degrading conditions.",
        "source": "Tribunal Judiciaire de Marseille / Inspection du Travail",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Nail and Hair Salon Exploitation — Vietnamese Workers in Paris (2019)",
        "summary": "OCLTI investigated a network of Vietnamese nail and hair salons in Paris exploiting trafficked workers. Victims brought from Vietnam through debt bondage arrangements (EUR 15,000-25,000 debts), worked 14 hours daily, wages seized. 4 salon operators convicted of trafficking for labour exploitation. 12 victims given temporary residence permits.",
        "source": "OCLTI / Tribunal Correctionnel de Paris",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Posted Workers Fraud — Cross-Border Construction Exploitation (2020)",
        "summary": "French and Portuguese authorities jointly prosecuted a network using fraudulent posted worker arrangements to exploit Portuguese construction workers in France. Workers officially employed by Portuguese shell companies to avoid French social contributions. Actual wages EUR 4-5 per hour. Eurojust coordinated the investigation involving EUR 12 million in social fraud.",
        "source": "Eurojust / Tribunal Judiciaire de Bordeaux / Ministerio Publico de Lisboa",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Provence Lavender Harvest — East European Worker Exploitation (2022)",
        "summary": "Labour inspectors in Alpes-de-Haute-Provence identified 60 Bulgarian workers exploited during lavender harvesting. Workers brought by Bulgarian intermediary, housed in barns, paid EUR 20 per day. Investigation revealed systematic use of intermediaries to distance employers from exploitation. Proceedings initiated against farm operator and intermediary.",
        "source": "Inspection du Travail / Procureur de la Republique de Digne-les-Bains",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "GRETA France Third Evaluation Report (2022)",
        "summary": "Council of Europe GRETA report on France noted improvements in legislation but persistent challenges in prosecuting labour trafficking. Labour trafficking represented only 15% of trafficking investigations despite evidence of widespread labour exploitation. Recommended: specialized prosecutors for labour trafficking, mandatory labour inspections in high-risk sectors, improved identification training.",
        "source": "GRETA Third Evaluation Report on France, GRETA(2022)09",
    },

    # ======================================================================
    # GERMANY (111-135)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Tonnies Meat Processing — COVID Outbreak and Labour Exploitation (2020)",
        "summary": "Major COVID-19 outbreak at Tonnies meat processing plant in Rheda-Wiedenbruck exposed systematic exploitation of Eastern European workers. Over 1,500 workers infected. Investigation revealed workers employed through subcontractors, housed in overcrowded flats, wages reduced by excessive deductions. Led to ban on subcontracting in meat industry (Arbeitsschutzkontrollgesetz 2021).",
        "source": "Amtsgericht Rheda-Wiedenbruck / Bundesministerium fur Arbeit und Soziales",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Arbeitsschutzkontrollgesetz 2021 — Meat Industry Subcontracting Ban",
        "summary": "Germany enacted the Occupational Health and Safety Inspection Act (Arbeitsschutzkontrollgesetz) directly in response to the Tonnies scandal. Banned subcontracting of core activities in meat processing from January 2021. Required meat companies to directly employ workers with full social insurance. Employers must provide adequate accommodation. Violations carry fines up to EUR 30,000.",
        "source": "Bundesgesetzblatt / Bundestag Drucksache 19/21978",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Bulgarian Agricultural Workers — Brandenburg Exploitation (2018)",
        "summary": "Prosecutors in Cottbus investigated exploitation of Bulgarian workers in asparagus harvesting in Brandenburg. Workers recruited in Bulgaria, charged EUR 200 monthly for overcrowded accommodation, paid below minimum wage after deductions. Labour inspectors found violations at 40% of farms inspected. Three farm operators prosecuted under Section 233 StGB (trafficking for labour exploitation).",
        "source": "Staatsanwaltschaft Cottbus / Bundespolizei",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Romanian Workers in Bavarian Slaughterhouses (2019)",
        "summary": "Investigation by Bavarian labour inspectors found systematic exploitation of Romanian workers in meat processing plants in Lower Bavaria. Workers employed through Romanian subcontractors, wages of EUR 4-5 per hour (below minimum wage), excessive overtime, dangerous working conditions. Five subcontractor bosses convicted of fraud and labour law violations.",
        "source": "Gewerbeaufsichtsamt Bayern / Staatsanwaltschaft Landshut",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Section 232-233a StGB — Federal Trafficking Prosecution Statistics (2021)",
        "summary": "Germany's Federal Criminal Office (BKA) reported 465 investigations for trafficking for labour exploitation under Sections 232-233a StGB in 2021. Of these, 64% involved male victims, predominantly from Romania, Bulgaria, and Poland. Main sectors: construction, meat processing, logistics, and cleaning. Conviction rate remained below 25% due to evidentiary challenges.",
        "source": "BKA Bundeslagebild Menschenhandel 2021",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "NRW Construction Trafficking — Operation Bau (2020)",
        "summary": "Joint operation by customs (Finanzkontrolle Schwarzarbeit) and police in North Rhine-Westphalia targeted labour trafficking in the construction sector. Network used Bulgarian and Serbian workers through cascading subcontractors on major construction projects. Workers housed in building site containers, paid EUR 3-4 per hour. 18 suspects arrested, EUR 8 million in evaded social contributions identified.",
        "source": "Zollfahndungsamt Essen / Staatsanwaltschaft Dusseldorf",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Asparagus Harvest Deaths — Lower Saxony (2020)",
        "summary": "Romanian seasonal worker died during asparagus harvest in Beelitz, Brandenburg, after collapse from exhaustion. Investigation revealed workers from Romania and Poland earned EUR 5 per hour after deductions, worked 12-hour shifts. Employer prosecuted for negligent homicide and labour exploitation. Case highlighted seasonal agricultural worker vulnerability during COVID-19 travel restrictions.",
        "source": "Staatsanwaltschaft Potsdam / Beratungsstelle fur mobile Beschaftigte",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Hamburg Port Logistics — Vietnamese Worker Trafficking (2017)",
        "summary": "Hamburg police investigated trafficking of Vietnamese nationals for exploitation in nail salons and restaurants in the Hamburg port area. Victims smuggled through Russia, debts of EUR 20,000-30,000 imposed. Three traffickers convicted under Section 232 StGB. Sentences of 3-5 years. Case linked to broader Vietnamese trafficking networks operating across Germany.",
        "source": "Landgericht Hamburg / BKA",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Berlin Hotel Cleaning — Filipino Worker Exploitation (2019)",
        "summary": "Prosecutors investigated exploitation of Filipino workers in hotel cleaning services in Berlin. Workers brought on tourist visas, employed through cleaning subcontractors, paid EUR 4 per hour. Passports held by employer. Labour court ordered back-payment of minimum wage to 15 workers. Two subcontractor managers convicted of trafficking for labour exploitation.",
        "source": "Arbeitsgericht Berlin / Beratungsstelle BEMA",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Lieferkettensorgfaltspflichtengesetz (2023) — Supply Chain Due Diligence",
        "summary": "Germany's Supply Chain Due Diligence Act entered into force in January 2023. Requires companies with 3,000+ employees (1,000+ from 2024) to identify and address human rights and environmental risks in supply chains, including forced labour and trafficking. Federal Office for Economic Affairs and Export Control (BAFA) designated as enforcement authority. Fines up to EUR 8 million or 2% of global turnover.",
        "source": "Bundesgesetzblatt / BAFA enforcement guidance",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Saxony Logistics Centre — Polish Worker Exploitation (2021)",
        "summary": "Court in Leipzig convicted operators of a logistics warehouse in Saxony for exploiting Polish temporary workers. Workers recruited through Polish agency, housed in overcrowded shipping containers, wages garnished for accommodation and transport. Labour inspectors found 60 workers in conditions meeting ILO forced labour indicators. Sentences of 2-4 years.",
        "source": "Landgericht Leipzig / Zoll Finanzkontrolle Schwarzarbeit",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "GRETA Germany Evaluation — Second Round (2019)",
        "summary": "GRETA report on Germany identified significant gaps in combating labour trafficking. Noted that Sections 232-233a StGB reforms of 2016 improved the legal framework but prosecution remained challenging. Recommended: establishing a National Rapporteur, improving victim identification in workplaces, strengthening cooperation between police and labour inspectors, and increasing specialised training.",
        "source": "GRETA Second Evaluation Report on Germany, GRETA(2019)07",
    },

    # ======================================================================
    # NETHERLANDS (136-155)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Westland Greenhouse Exploitation — Polish Workers (2016)",
        "summary": "Court in The Hague convicted operators of greenhouse businesses in Westland for exploiting Polish migrant workers. Workers picked tomatoes and cucumbers for 14 hours daily, housed in overcrowded portacabins. Wages below minimum after deductions for accommodation (EUR 100/week for shared room). Employment agency convicted of human trafficking under Article 273f of the Criminal Code.",
        "source": "Rechtbank Den Haag / Inspectie SZW",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Horticulture Sector — Systematic Labour Inspection Campaign (2018-2020)",
        "summary": "Dutch Labour Inspectorate (Inspectie SZW) conducted systematic inspections of 500 horticultural companies in Westland and Noord-Holland. Found labour violations in 38% of inspected companies. 45 cases referred for criminal investigation for suspected trafficking. Common violations: underpayment, excessive working hours, inadequate housing, document retention.",
        "source": "Inspectie SZW Annual Report 2020 / Ministry of Social Affairs",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Article 273f — Dutch Trafficking Prosecution Statistics (2020)",
        "summary": "Dutch National Rapporteur reported 160 suspected labour trafficking cases in 2020, with 45 prosecutions initiated. Conviction rate of approximately 60% for cases reaching trial. Main sectors: agriculture/horticulture, cleaning, food processing, and construction. Victims predominantly from Poland, Romania, Bulgaria, and the Philippines.",
        "source": "Nationaal Rapporteur Mensenhandel en Seksueel Geweld tegen Kinderen / Annual Report 2021",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Romanian Workers in Limburg Asparagus Farms (2019)",
        "summary": "Criminal court in Maastricht convicted a Dutch-Romanian network for trafficking Romanian workers into asparagus and mushroom farming in Limburg. Workers paid EUR 3-4 per hour after deductions, housed 8 to a room. Network operated through a legitimate temporary employment agency. Three defendants sentenced to 3-5 years under Art. 273f.",
        "source": "Rechtbank Maastricht / Inspectie SZW / FIOD",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Meat Processing Plant — Brazilian Workers (2021)",
        "summary": "Inspectie SZW investigated a meat processing company in Gelderland exploiting Brazilian workers brought through Portuguese employment agencies. Workers housed in overcrowded accommodation in Nijmegen, transport costs deducted from wages. Investigation found 120 workers earning below minimum wage. Company fined EUR 800,000 and employment agency licence revoked.",
        "source": "Inspectie SZW / Rechtbank Arnhem",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Cleaning Sector — Undocumented Worker Exploitation (2018)",
        "summary": "Amsterdam court convicted a cleaning company owner of trafficking 25 undocumented Filipino and Indonesian workers. Workers employed in office cleaning, paid EUR 3 per hour, threatened with deportation if they complained. Workers had no contracts, no social insurance. Owner sentenced to 30 months imprisonment.",
        "source": "Rechtbank Amsterdam / Inspectie SZW",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Mushroom Farm Exploitation — Horst aan de Maas (2020)",
        "summary": "Dutch court convicted operators of a mushroom farm in Limburg for labour exploitation of Polish workers. Workers lived on the farm premises, required to work 60+ hours per week, paid per kilogram harvested rather than hourly. Investigation revealed systematic underpayment of EUR 500,000 over 3 years. Operator sentenced to 2 years and ordered to pay back wages.",
        "source": "Rechtbank Limburg / Inspectie SZW / SNCU (Stichting Naleving CAO)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "GRETA Netherlands Evaluation — Third Round (2022)",
        "summary": "GRETA's third evaluation of the Netherlands praised the National Rapporteur system and multi-agency approach but raised concerns about declining prosecution numbers for labour trafficking. Recommended strengthening Inspectie SZW enforcement powers, improving access to compensation for victims, and addressing exploitation in temporary staffing agencies.",
        "source": "GRETA Third Evaluation Report on the Netherlands, GRETA(2022)12",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Temporary Employment Agency Fraud — Rosenbaum Case (2017)",
        "summary": "Major Dutch temporary employment agency convicted of systemic exploitation of over 300 Eastern European workers in distribution centres and food processing plants. Agency charged excessive fees for housing, health insurance, and transport, reducing net wages below minimum. Fined EUR 1.5 million. Led to reforms in temporary agency worker regulation (WAADI Act amendments).",
        "source": "Rechtbank Rotterdam / ABU (Algemene Bond Uitzendondernemingen)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Flower Auction Workers — Aalsmeer Exploitation (2019)",
        "summary": "Labour inspectors investigated exploitation of temporary workers at the Aalsmeer flower auction (Royal FloraHolland) and surrounding businesses. Polish and Romanian workers employed through agencies, working night shifts in cold storage. Deductions for accommodation and transport reduced wages to EUR 4 per hour. Two agencies penalised, one prosecuted for trafficking.",
        "source": "Inspectie SZW / Rechtbank Haarlem",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Ship Dismantling — African Workers in Rotterdam (2020)",
        "summary": "Prosecutors investigated exploitation of West African workers at a ship dismantling facility in Rotterdam harbour. Workers exposed to asbestos and toxic materials without protective equipment, paid EUR 5 per hour. Investigation revealed workers recruited in Ghana and Nigeria with false promises. Two company directors convicted of trafficking for labour exploitation.",
        "source": "Rechtbank Rotterdam / Inspectie SZW / Port of Rotterdam Authority",
    },

    # ======================================================================
    # BELGIUM (156-170)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Ghent Garment Sweatshop — Chinese Worker Exploitation (2016)",
        "summary": "Tribunal Correctionnel de Gand convicted operators of clandestine garment workshops exploiting undocumented Chinese workers. Workers sewed clothes for 16 hours daily in basement workshops, sleeping on factory floors. Wages of EUR 2-3 per hour, debts of EUR 15,000 imposed for passage. 5 defendants sentenced to 2-5 years under Article 433quinquies of the Penal Code.",
        "source": "Tribunal Correctionnel de Gand / Police Federale / Auditorat du Travail",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Construction Sector Exploitation — Brussels Region (2019)",
        "summary": "Belgian labour prosecution service (Auditorat du Travail) investigated exploitation of Brazilian and Moroccan workers on construction sites in Brussels. Workers employed through Portuguese and Spanish subcontractors, paid EUR 5-6 per hour. No social security registration. Investigation revealed 200 workers in conditions of exploitation across 30 construction sites.",
        "source": "Auditorat du Travail de Bruxelles / SIRS (Service d'Information et de Recherche Sociale)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Meat Processing — West Flanders Exploitation (2020)",
        "summary": "Court in Bruges convicted a meat processing company and its subcontractor for exploiting Romanian and Bulgarian workers. Workers housed in company-provided barracks in Roeselare, wages garnished for accommodation and transport. Labour inspectors found 40 workers earning below the sectoral minimum wage. Company fined EUR 200,000, subcontractor sentenced to 18 months.",
        "source": "Rechtbank van Eerste Aanleg West-Vlaanderen / Sociale Inspectie",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Belgian Social Criminal Code — Enhanced Trafficking Penalties (2016)",
        "summary": "Belgium strengthened penalties for human trafficking under the Social Criminal Code and Article 433quinquies of the Penal Code. Labour trafficking now carries sentences of 1-15 years. Specific aggravating factors include abuse of a person's vulnerable situation, use of deception regarding employment conditions, and confiscation of identity documents. Belgium recognised as having one of Europe's strongest legal frameworks by GRETA.",
        "source": "Belgisch Staatsblad / GRETA Belgium Evaluation",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Car Wash and Restaurant Chain — Kurdish Worker Trafficking (2018)",
        "summary": "Federal Police dismantled a Kurdish trafficking network exploiting compatriots in car washes and restaurants in Brussels and Liege. Workers employed illegally, housed in overcrowded apartments, threatened with violence. Network laundered profits through multiple businesses. 8 defendants convicted, combined sentences of 35 years, EUR 2 million in assets confiscated.",
        "source": "Tribunal Correctionnel de Bruxelles / Police Federale",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Domestic Servitude — Diplomatic Household Cases (2017)",
        "summary": "Belgian courts convicted two former employees of international organisations based in Brussels for exploiting domestic workers. Filipino and Ethiopian women worked 18-hour days without pay or rest. Courts rejected immunity claims as the employment relationship was private in nature. Victims awarded compensation of EUR 50,000-80,000 each.",
        "source": "Tribunal du Travail de Bruxelles / PAG-ASA (Belgian anti-trafficking NGO)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Belgian Multi-Agency Approach — Arrondissement Cells",
        "summary": "Belgium's system of multi-disciplinary arrondissement cells (arrondissementele cellen) cited as best practice by GRETA. These cells bring together prosecutors, police, labour inspectors, and social services to coordinate trafficking investigations. In 2020, arrondissement cells identified 452 potential victims of trafficking, 38% in labour exploitation. Antwerp and Brussels cells most active.",
        "source": "Belgian Federal Government Interdepartmental Coordination Platform / GRETA Belgium Report",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Antwerp Port — Container Transport Worker Exploitation (2021)",
        "summary": "Prosecutors investigated exploitation of Eastern European truck drivers and warehouse workers at the Port of Antwerp. Workers from Romania and Moldova employed through shell companies in Cyprus and Malta, paid below Belgian minimum wage. Investigation revealed EUR 15 million in unpaid social contributions. Six individuals and two companies prosecuted.",
        "source": "Arbeidsauditoraat Antwerpen / SIRS",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "GRETA Belgium Third Evaluation (2023)",
        "summary": "GRETA praised Belgium's comprehensive legal framework and multi-agency approach but identified challenges in prosecuting complex labour trafficking cases. Recommended improving access to justice for undocumented victims, strengthening financial investigations, and addressing exploitation of EU mobile workers in the gig economy.",
        "source": "GRETA Third Evaluation Report on Belgium, GRETA(2023)03",
    },

    # ======================================================================
    # GREECE (171-182)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Manolada Strawberry Picker Shooting — Landmark Case (2013-2017)",
        "summary": "In April 2013, farm supervisors in Manolada, Peloponnese, shot at Bangladeshi strawberry pickers who demanded six months of unpaid wages, injuring 30. Initial trial in 2014 acquitted the farm owner, causing international outrage. The case was taken to the European Court of Human Rights (Chowdury and Others v. Greece), which ruled in 2017 that Greece violated Article 4 (prohibition of forced labour). Greece subsequently retried and convicted the employer.",
        "source": "Areios Pagos (Greek Supreme Court) / ECtHR Chowdury v. Greece [2017]",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Chowdury and Others v. Greece [2017] — ECtHR Forced Labour Ruling",
        "summary": "European Court of Human Rights found Greece violated Article 4 of the Convention by failing to prevent forced labour of Bangladeshi migrant workers in Manolada. Court established that workers were in a situation of forced labour based on: unpaid wages, severe working conditions, no freedom to leave, abuse of vulnerability as undocumented migrants. Greece ordered to pay EUR 16,000 per applicant.",
        "source": "European Court of Human Rights, Application No. 21884/15",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Laconia Agricultural Exploitation — Egyptian Workers (2019)",
        "summary": "Greek police investigated exploitation of Egyptian migrant workers in olive harvesting in Laconia, Peloponnese. Workers recruited in Egypt with promises of EUR 40 per day, actual payment EUR 10-15 after deductions. Housed in abandoned buildings, documents confiscated. Four farm owners and two labour intermediaries arrested and charged with trafficking under Greek Law 4198/2013.",
        "source": "Eisangeleas Protodikon Sparti / Hellenic Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Greek Law 4198/2013 — Anti-Trafficking Framework",
        "summary": "Greece transposed EU Directive 2011/36/EU through Law 4198/2013, establishing the National Referral Mechanism and strengthening penalties for trafficking. Labour trafficking carries 10 years minimum imprisonment. The Office of the National Rapporteur coordinates identification and support. However, GRETA noted persistent low conviction rates for labour trafficking relative to the scale of exploitation.",
        "source": "Efimeris tis Kiverniseos (Government Gazette) / GRETA Greece Evaluation",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Thessaloniki Garment Workshops — Pakistani Worker Exploitation (2018)",
        "summary": "Police raids on garment workshops in Thessaloniki identified 45 Pakistani workers in conditions of trafficking. Workers produced garments for domestic market, working 14-hour shifts, sleeping in workshops. Debt bondage imposed for travel costs. Three workshop operators convicted of trafficking for labour exploitation. Victims provided with residence permits under Law 4198/2013.",
        "source": "Protodikeio Thessalonikis / Hellenic Police Anti-Trafficking Unit",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Crete Agricultural Exploitation — Albanian Workers (2020)",
        "summary": "Prosecutors in Heraklion investigated exploitation of Albanian workers in greenhouse agriculture on Crete. Workers employed without contracts, paid EUR 15-20 per day, exposed to pesticides without protection. Labour inspectors identified 90 workers in exploitative conditions across 25 farms. Proceedings initiated against 8 farm operators.",
        "source": "Eisangeleas Protodikon Irakliou / SEPE (Labour Inspectorate)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Fishing Industry Exploitation — Aegean Islands (2021)",
        "summary": "Greek coast guard and police investigated exploitation of Egyptian and Eritrean workers on fishing boats in the Aegean. Workers recruited through intermediaries, confined to vessels for weeks, paid EUR 200-300 per month. Three boat owners prosecuted for labour trafficking. Investigation highlighted link between irregular migration and labour exploitation in maritime sector.",
        "source": "Hellenic Coast Guard / Protodikeio Mytilinis",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "GRETA Greece Third Evaluation (2023)",
        "summary": "GRETA report identified significant challenges in Greece's anti-trafficking response. Labour exploitation vastly underreported; agricultural and domestic work sectors identified as highest risk. Recommended: proactive labour inspections, specialised training for prosecutors, regularisation pathways for trafficking victims, and addressing impunity for labour trafficking offences.",
        "source": "GRETA Third Evaluation Report on Greece, GRETA(2023)10",
    },

    # ======================================================================
    # POLAND (183-190)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "PL",
        "title": "Forced Labour in Agriculture — Lublin Province (2018)",
        "summary": "Polish prosecutors convicted a farming family in Lublin province for forcing Ukrainian workers into agricultural labour. Workers recruited through false advertisements, passports confiscated upon arrival, wages withheld. Workers harvested berries and vegetables for 14 hours daily. Three defendants sentenced to 2-4 years under Article 189a of the Polish Penal Code (trafficking).",
        "source": "Sad Okregowy w Lublinie / Polish Border Guard",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PL",
        "title": "Manufacturing Exploitation — Vietnamese Workers in Wroclaw (2019)",
        "summary": "ABW (Internal Security Agency) and police dismantled a network trafficking Vietnamese nationals to work in manufacturing plants in Lower Silesia. Workers brought through Russia, employed in electronics assembly and textile production. Debts of EUR 10,000-15,000 imposed. Passports held by network. 6 arrests, 40 victims identified. Prosecuted under Art. 189a of the Penal Code.",
        "source": "Prokuratura Okregowa we Wroclawiu / ABW",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PL",
        "title": "Polish Nationals Trafficked Abroad — Prosecution of Recruiters (2020)",
        "summary": "Warsaw prosecutors convicted a Polish labour recruitment network for trafficking compatriots to work in the Netherlands and Germany. Workers promised EUR 2,000 per month, subjected to exploitation in agriculture and food processing. Network controlled workers through debt for accommodation and transport. 5 defendants sentenced under Art. 189a and Art. 253 of the Penal Code.",
        "source": "Prokuratura Okregowa w Warszawie / Europol",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PL",
        "title": "Ukrainian Refugees — Labour Exploitation Risk Assessment (2022)",
        "summary": "Following the influx of Ukrainian refugees in 2022, Polish authorities identified increased risks of labour trafficking. Border Guard and labour inspectors reported cases of exploitative employment conditions. Prosecutors investigated 25 cases involving exploitation of Ukrainian nationals in construction, cleaning, and hospitality. Enhanced monitoring of employment agencies placing Ukrainian workers implemented.",
        "source": "Prokuratura Krajowa / Panstwowa Inspekcja Pracy / GRETA urgent report",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PL",
        "title": "North Korean Workers — Gdansk Shipyard Investigation (2017)",
        "summary": "Polish prosecutors investigated the use of North Korean workers at the Gdansk shipyard and related construction projects. Workers' wages were paid directly to the DPRK government. Investigation formed part of broader European scrutiny of North Korean labour exploitation. Poland ended North Korean worker permits following UN Security Council Resolution 2397 (2017).",
        "source": "Prokuratura Regionalna w Gdansku / UN Panel of Experts reports",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PL",
        "title": "Berry Picking Exploitation — Podlasie Region (2020)",
        "summary": "Labour inspectors investigated exploitation of Belarusian and Ukrainian seasonal workers in berry picking in Podlasie. Workers paid per kilogram harvested, earning below minimum wage. Housed in barns and sheds without sanitation. Three farm operators fined for labour law violations; one case referred for trafficking prosecution.",
        "source": "Panstwowa Inspekcja Pracy / Prokuratura Rejonowa w Bialymstoku",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PL",
        "title": "GRETA Poland Second Evaluation (2021)",
        "summary": "GRETA report noted Poland's growing role as both a destination and transit country for trafficking. Labour exploitation increasing, particularly of Ukrainian and Asian workers. Recommended: establishing a formal National Referral Mechanism, improving victim identification training, ensuring non-punishment of trafficking victims, and strengthening labour inspectorate cooperation with law enforcement.",
        "source": "GRETA Second Evaluation Report on Poland, GRETA(2021)11",
    },

    # ======================================================================
    # ROMANIA AND BULGARIA — SOURCE COUNTRY PROSECUTIONS (191-200)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "RO",
        "title": "DIICOT Trafficking Network Dismantlement — UK-Bound Workers (2019)",
        "summary": "Romania's Directorate for Investigating Organised Crime and Terrorism (DIICOT) dismantled a trafficking network recruiting Romanians for exploitation in the UK. Network operated from Bacau and Suceava counties, targeting vulnerable Roma communities. Victims exploited in car washes, agriculture, and street begging in England. 12 defendants convicted, sentences of 5-12 years.",
        "source": "DIICOT / Eurojust / Crown Prosecution Service UK",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "RO",
        "title": "Romanian Agricultural Trafficking Network — Italy-Bound (2020)",
        "summary": "DIICOT prosecuted a network trafficking Romanian workers to agricultural exploitation in Southern Italy. Recruiters targeted economically deprived areas in Teleorman and Olt counties. Workers exploited in tomato and fruit harvesting in Puglia and Calabria. Joint investigation with Italian DDA. 8 defendants convicted of trafficking under Art. 210-211 of the Romanian Penal Code.",
        "source": "DIICOT / DDA Bari / Eurojust",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "RO",
        "title": "Romania National Anti-Trafficking Strategy — ANITP Assessment (2021)",
        "summary": "National Agency Against Trafficking in Persons (ANITP) reported 647 trafficking victims identified in 2021, of whom 62% were trafficked for labour exploitation. Main destinations: Germany, Italy, UK, and Spain. ANITP noted increasing domestic labour trafficking. Prevention programmes targeted vulnerable Roma communities in rural areas.",
        "source": "ANITP Annual Report 2021 / GRETA Romania Report",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BG",
        "title": "Bulgarian Anti-Trafficking Commission — Network Prosecutions (2019)",
        "summary": "Bulgarian prosecutors dismantled 14 trafficking networks in 2019 targeting Bulgarian citizens for labour exploitation in Western Europe. Networks recruited from impoverished communities in Plovdiv, Montana, and Vidin provinces. Main destinations: UK (car washes, agriculture), Netherlands (horticulture), Germany (meat processing). Combined sentences exceeded 80 years.",
        "source": "National Commission for Combating Trafficking in Human Beings (NCCTHB) Bulgaria",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BG",
        "title": "Bulgaria-Germany JIT — Meat Processing Trafficking (2020)",
        "summary": "Joint Investigation Team (JIT) between Bulgaria and Germany targeted a network trafficking Bulgarian workers to meat processing plants in North Rhine-Westphalia. Workers recruited in Pazardzhik region, transported to Germany, housed in overcrowded apartments. Wages of EUR 3-4 per hour after deductions. JIT facilitated by Eurojust. 6 arrests in Bulgaria, 4 in Germany.",
        "source": "Eurojust / Prokuratura na Republika Bulgaria / Staatsanwaltschaft Bielefeld",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BG",
        "title": "Roma Community Exploitation — Internal Trafficking (2018)",
        "summary": "Sofia prosecutors convicted a network of Bulgarian nationals who trafficked members of Roma communities for exploitation within Bulgaria and to Greece. Victims forced into agricultural labour and begging. Network exploited extreme poverty and social exclusion. 5 defendants convicted under Art. 159a-159d of the Bulgarian Penal Code. Sentences of 3-8 years.",
        "source": "Spetsializirana Prokuratura / GRETA Bulgaria Report",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "RO",
        "title": "Romania-Spain JIT — Agricultural Trafficking Network (2021)",
        "summary": "Eurojust-facilitated Joint Investigation Team between Romania and Spain targeted a trafficking network exploiting Romanian workers in Spanish agriculture. Workers recruited from Vaslui and Galati counties, exploited in greenhouse agriculture in Almeria and Murcia. Network controlled workers through debt and threats. 10 arrests (6 in Romania, 4 in Spain). EUR 1.2 million in assets seized.",
        "source": "Eurojust / DIICOT / Guardia Civil",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BG",
        "title": "GRETA Bulgaria Third Evaluation (2021)",
        "summary": "GRETA evaluated Bulgaria's anti-trafficking response, noting the country remained a primary source of trafficking victims in Europe. Labour trafficking increasing as proportion of total. Recommended: improving identification of trafficking among Bulgarian nationals abroad, strengthening prosecution capacity, implementing a formal National Referral Mechanism, and ensuring victims' access to compensation.",
        "source": "GRETA Third Evaluation Report on Bulgaria, GRETA(2021)05",
    },

    # ======================================================================
    # IRELAND (201-208)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "IE",
        "title": "Atlantic Dawn Fishing Vessel — Egyptian Worker Exploitation (2016)",
        "summary": "Investigation into exploitation of Egyptian, Filipino, and Ghanaian workers on Irish fishing vessels, including those linked to the Atlantic Dawn fleet. Workers confined to vessels for months, paid below minimum wage, documents confiscated. Workplace Relations Commission and ITF investigations revealed widespread exploitation. Cases contributed to reforms in the Atypical Working Scheme for non-EEA fishing crew.",
        "source": "Workplace Relations Commission / ITF / MRCI (Migrant Rights Centre Ireland)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IE",
        "title": "Irish Fishing Industry — Atypical Working Scheme Reforms (2016-2020)",
        "summary": "Following revelations of widespread exploitation of non-EEA workers on Irish fishing vessels, Ireland introduced the Atypical Working Scheme for sea-fishing workers in 2016. Subsequent investigations found continued exploitation despite reforms. Guardian and ITF reports documented cases of workers earning EUR 2-3 per hour. Task Force established in 2019 to strengthen protections.",
        "source": "Department of Justice / Task Force on non-EEA workers in the fishing industry",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IE",
        "title": "Mushroom Farm Exploitation — Monaghan and Cavan (2017)",
        "summary": "Labour inspectors investigated exploitation of Eastern European workers on mushroom farms in counties Monaghan and Cavan. Workers (mainly Lithuanian and Latvian) earned below minimum wage after deductions, housed in employer-provided accommodation, and worked excessive hours during harvest. Workplace Relations Commission awarded back-pay to affected workers. Several employers sanctioned.",
        "source": "Workplace Relations Commission / MRCI",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IE",
        "title": "Meat Processing — Brazilian Workers in Midlands (2019)",
        "summary": "MRCI (Migrant Rights Centre Ireland) documented exploitation of Brazilian workers in meat processing plants in the Irish Midlands. Workers brought through employment agencies, housed in overcrowded accommodation, wages reduced by excessive deductions. WRC complaints resulted in significant back-pay awards. Investigation highlighted role of intermediary agencies in facilitating exploitation.",
        "source": "MRCI / Workplace Relations Commission",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IE",
        "title": "Criminal Law (Human Trafficking) Act 2008 — First Labour Trafficking Conviction (2020)",
        "summary": "Ireland secured its first conviction for labour trafficking under the Criminal Law (Human Trafficking) Act 2008. Case involved exploitation of a Middle Eastern national in a Dublin restaurant. Victim worked 80+ hours per week, paid EUR 2 per hour, housed in restaurant premises. Defendant convicted and sentenced to 2.5 years imprisonment. Landmark for Irish trafficking prosecution.",
        "source": "Dublin Circuit Criminal Court / DPP (Director of Public Prosecutions)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IE",
        "title": "GRETA Ireland Third Evaluation (2022)",
        "summary": "GRETA report on Ireland was critical of the low number of trafficking convictions and absence of a statutory National Referral Mechanism. Noted that Ireland had been on the US TIP Report Tier 2 Watch List. Recommended: enacting NRM legislation, establishing independent identification mechanism, increasing prosecutorial resources for trafficking, and improving support for victims in the criminal justice process.",
        "source": "GRETA Third Evaluation Report on Ireland, GRETA(2022)07",
    },

    # ======================================================================
    # PORTUGAL (209-215)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "PT",
        "title": "Alentejo Agricultural Exploitation — South Asian Workers (2019)",
        "summary": "Prosecutors in Beja investigated exploitation of Nepalese and Indian workers in intensive agriculture in the Alentejo region. Workers recruited through Portuguese intermediaries, housed in overcrowded containers, paid EUR 3-4 per hour. 80 workers identified in conditions of trafficking. Investigation led to 6 arrests and charges under Article 160 of the Portuguese Penal Code (trafficking).",
        "source": "Ministerio Publico de Beja / SEF (Servico de Estrangeiros e Fronteiras)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PT",
        "title": "Odemira Migrant Worker Crisis (2021)",
        "summary": "International attention focused on exploitative conditions of migrant workers in Odemira, Alentejo, during COVID-19. Over 10,000 workers (mainly from South and Southeast Asia) in berry and vegetable agriculture lived in overcrowded conditions facilitating virus spread. Area placed under security fence by authorities. Multiple investigations initiated. Employers and intermediaries prosecuted for labour exploitation.",
        "source": "Ministerio Publico de Beja / ACT (Autoridade para as Condicoes do Trabalho) / European Parliament resolution",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PT",
        "title": "Construction Sector — Moldovan Worker Trafficking (2018)",
        "summary": "Lisbon court convicted a construction subcontracting network for trafficking Moldovan workers to building sites in the Lisbon metropolitan area. Workers recruited in Moldova with promises of EUR 1,500 monthly, actual earnings EUR 400-500 after deductions. Network used fraudulent posted worker certificates. 4 defendants sentenced to 3-6 years under Art. 160.",
        "source": "Tribunal Criminal de Lisboa / SEF",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PT",
        "title": "Agricultural Intermediaries — Temporary Work Agency Prosecutions (2020)",
        "summary": "Portuguese labour inspectors (ACT) investigated 150 temporary work agencies placing workers in agriculture. Found 30% operating without proper licences. Workers from Bangladesh, Nepal, and Thailand employed through these agencies in Alentejo and Algarve. Multiple agencies fined, 5 operators prosecuted for trafficking. Led to stricter licensing requirements for agricultural labour intermediaries.",
        "source": "ACT / Ministerio Publico / GRETA Portugal Report",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PT",
        "title": "GRETA Portugal Second Evaluation (2021)",
        "summary": "GRETA noted increasing labour trafficking in Portuguese agriculture, particularly in the Alentejo region. Recommended: strengthening labour inspection capacity, improving identification of trafficking victims among migrant agricultural workers, regulating temporary work agencies, and ensuring access to regularisation for trafficking victims under Portuguese law.",
        "source": "GRETA Second Evaluation Report on Portugal, GRETA(2021)09",
    },

    # ======================================================================
    # NORDIC COUNTRIES (216-223)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "SE",
        "title": "Berry Picker Exploitation — Thai Workers in Norrland (2012-2020)",
        "summary": "Swedish prosecutors investigated systematic exploitation of Thai berry pickers recruited to harvest wild blueberries in northern Sweden. Workers charged EUR 3,000-5,000 for travel and accommodation, earnings dependent on harvest volume. Many workers earned less than costs, returning to Thailand in debt. Multiple prosecutions under Swedish trafficking provisions. Supreme Court (Hogsta Domstolen) addressed the issue in 2014.",
        "source": "Hogsta Domstolen / Rikskriminalpolisen / GRETA Sweden Report",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "SE",
        "title": "Swedish Berry Industry Reforms — Employer Guarantee System (2015)",
        "summary": "Following exploitation scandals, Sweden introduced requirements for berry companies to guarantee minimum earnings and provide insurance for recruited workers. Swedish Migration Agency (Migrationsverket) required companies to demonstrate capacity to pay workers before issuing work permits. System reduced but did not eliminate exploitation. Some companies evaded rules through complex subcontracting.",
        "source": "Migrationsverket / Arbetsformedlingen / LO (Swedish Trade Union Confederation)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "SE",
        "title": "Restaurant Sector — Bangladeshi Worker Trafficking (2019)",
        "summary": "Stockholm District Court convicted restaurant owners of trafficking for labour exploitation of Bangladeshi workers. Victims worked 14-hour days in restaurants, wages confiscated, housed in overcrowded accommodation. Workers brought on student visas, forced to work instead of studying. Two defendants sentenced to 4 and 3 years. Compensation of SEK 200,000 per victim ordered.",
        "source": "Stockholms Tingsratt / Swedish Police Anti-Trafficking Unit",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "SE",
        "title": "GRETA Sweden Third Evaluation (2023)",
        "summary": "GRETA praised Sweden's proactive approach to labour trafficking but noted challenges in the berry-picking, restaurant, and cleaning sectors. Recommended strengthening cooperation between police and the Work Environment Authority, improving identification of trafficking victims in asylum and migration processes, and ensuring effective investigation and prosecution of labour trafficking.",
        "source": "GRETA Third Evaluation Report on Sweden, GRETA(2023)15",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FI",
        "title": "Berry Picker Exploitation — Thai Workers in Lapland (2014-2019)",
        "summary": "Finnish police investigated exploitation of Thai berry pickers in Lapland, mirroring Swedish cases. Workers recruited through Thai agencies, charged significant fees, earnings dependent on wild berry harvest. Several companies investigated for trafficking. Helsinki District Court convicted a berry company director of exploitation (trafficking in Chapter 25 of the Criminal Code). Fines and compensation ordered.",
        "source": "Helsingin Karajaoikeus / KRP (National Bureau of Investigation)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FI",
        "title": "Restaurant Sector — Nepali and Vietnamese Workers (2020)",
        "summary": "Finnish police investigated trafficking of Nepali and Vietnamese nationals in the restaurant sector in Helsinki and Turku. Workers recruited with promises of EUR 2,000 monthly, paid EUR 500-800, worked 70+ hours weekly. Employers exploited workers' dependence on residence permits tied to employment. Three restaurant owners convicted of trafficking. Victims granted continuous residence permits.",
        "source": "KRP / Turun Karajaoikeus / Finnish National Rapporteur",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FI",
        "title": "Cleaning Sector — Estonian and Ukrainian Worker Exploitation (2021)",
        "summary": "Finnish prosecutors investigated exploitation of Estonian and Ukrainian cleaning workers by a Helsinki-based cleaning company. Workers employed without proper contracts, paid EUR 4-5 per hour, excessive deductions for equipment and uniforms. Labour inspectors identified 30 workers in exploitative conditions. Company owner convicted of extortionate work discrimination under Chapter 47 of the Criminal Code.",
        "source": "Helsingin Karajaoikeus / AVI (Regional State Administrative Agency)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FI",
        "title": "GRETA Finland Second Evaluation (2019)",
        "summary": "GRETA report identified increasing labour trafficking in Finland, particularly in the restaurant, cleaning, and construction sectors. Noted that many victims were non-EU nationals whose residence permits depended on their employer. Recommended: delinking work permits from specific employers, establishing specialised trafficking prosecutors, and improving victim identification training.",
        "source": "GRETA Second Evaluation Report on Finland, GRETA(2019)14",
    },

    # ======================================================================
    # CZECH REPUBLIC AND HUNGARY (224-231)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "CZ",
        "title": "Forestry Worker Exploitation — Vietnamese Workers (2016)",
        "summary": "Czech prosecutors convicted a network trafficking Vietnamese workers for exploitation in forestry and manufacturing in Moravia. Workers brought through Ukrainian border, charged EUR 8,000-12,000 for entry, documents confiscated. Workers planted trees and worked in factories for EUR 2 per hour. 5 defendants convicted under Section 168 of the Czech Criminal Code (trafficking). Sentences of 3-7 years.",
        "source": "Krajsky Soud v Brne / Czech Police (NCOZ)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "CZ",
        "title": "Automotive Industry — Ukrainian Worker Trafficking (2019)",
        "summary": "Czech organised crime unit (NCOZ) dismantled a network exploiting Ukrainian workers in automotive supply chain factories in Central Bohemia. Workers recruited through Ukrainian agencies, employed through Czech shell companies. Wages of CZK 50-60 per hour (EUR 2), deductions for accommodation and transport. 80 victims identified. 7 defendants prosecuted.",
        "source": "NCOZ (Narodni Centrala proti Organizovanemu Zlocinu) / Krajsky Soud v Praze",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "CZ",
        "title": "Meat Processing — Mongolian Worker Exploitation (2018)",
        "summary": "Prosecutors in Plzen investigated exploitation of Mongolian workers in meat processing plants in Western Bohemia. Workers recruited in Ulaanbaatar with promises of EUR 1,500 monthly, actual earnings EUR 400 after deductions. Employer controlled housing and bank accounts. Investigation identified 40 victims. Two company managers and one intermediary convicted.",
        "source": "Okresni Soud v Plzni / Czech Labour Inspectorate (SUIP)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "CZ",
        "title": "GRETA Czech Republic Third Evaluation (2020)",
        "summary": "GRETA noted that Czech Republic transitioned from source to destination country for labour trafficking. Vietnamese, Ukrainian, and Mongolian workers most at risk. Recommended: strengthening the National Referral Mechanism, improving cooperation between police and labour inspectors, ensuring adequate support for male trafficking victims, and addressing exploitation through temporary staffing agencies.",
        "source": "GRETA Third Evaluation Report on the Czech Republic, GRETA(2020)08",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HU",
        "title": "Roma Community Labour Trafficking — Domestic Prosecutions (2017)",
        "summary": "Hungarian prosecutors convicted a network of Hungarian nationals who exploited members of Roma communities in forced agricultural labour in Eastern Hungary. Victims recruited from impoverished settlements in Borsod-Abauj-Zemplen county, forced to work on farms and in construction. 6 defendants convicted under Section 192 of the Hungarian Criminal Code (trafficking). Sentences of 2-6 years.",
        "source": "Debreceni Torvenyszek / Rendorseg (Hungarian Police)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HU",
        "title": "Cross-Border Trafficking Network — Hungary to UK (2018)",
        "summary": "Hungarian police and NCA joint operation dismantled a network trafficking Hungarian Roma to the UK for labour exploitation. Victims exploited in egg processing and food production in the Midlands. Network controlled victims through debt and threats to family members in Hungary. 8 defendants convicted in Hungary and UK. Joint Investigation Team facilitated by Eurojust.",
        "source": "Nemzeti Nyomozo Iroda / NCA UK / Eurojust",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HU",
        "title": "Agricultural Exploitation — Serbian Border Region (2020)",
        "summary": "Prosecutors in Szeged investigated exploitation of Serbian nationals in agricultural work in Csongrad-Csanad county. Workers recruited at the border, employed without permits, paid HUF 500-800 per hour (EUR 1.50-2.50). Housed in barns on farm properties. 3 farm operators and 2 intermediaries charged with trafficking.",
        "source": "Szegedi Torvenyszek / Hungarian Border Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HU",
        "title": "GRETA Hungary Third Evaluation (2021)",
        "summary": "GRETA expressed concern about Hungary's anti-trafficking response, noting declining identification numbers and prosecution rates. Labour trafficking of vulnerable Hungarian nationals (particularly Roma) for exploitation within Hungary and in Western Europe remained significant. Recommended: strengthening the National Referral Mechanism, proactive identification, improved victim support, and addressing root causes in socially excluded communities.",
        "source": "GRETA Third Evaluation Report on Hungary, GRETA(2021)08",
    },

    # ======================================================================
    # EU-WIDE / CROSS-BORDER MECHANISMS (232-250)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Directive 2011/36/EU — Implementation Assessment (2020)",
        "summary": "European Commission Third Report on progress in the fight against trafficking found that labour trafficking accounted for 26% of registered victims in the EU (2017-2018). Of 11,788 registered victims, 6,163 were from EU Member States. Main sectors: agriculture, construction, hospitality, domestic work, and manufacturing. Commission found significant implementation gaps in multiple Member States.",
        "source": "European Commission COM(2020) 661 final",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Eurojust Joint Investigation Teams — Trafficking Cases (2019-2021)",
        "summary": "Eurojust supported 82 Joint Investigation Teams (JITs) targeting human trafficking between 2019 and 2021. Labour trafficking JITs increased by 40%. Most active bilateral combinations: Romania-UK, Romania-Germany, Bulgaria-Netherlands, Poland-UK. JITs enabled coordinated arrests, evidence sharing, and mutual legal assistance. Average JIT duration 18 months.",
        "source": "Eurojust Annual Report 2021 / Eurojust Casework on Trafficking in Human Beings",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Europol — EMPACT THB Operation Results (2020)",
        "summary": "Europol's European Multidisciplinary Platform Against Criminal Threats (EMPACT) priority on trafficking reported 369 arrests across 26 countries in joint action day in 2020. Labour trafficking arrests constituted 35% of total. Operations targeted networks exploiting workers in agriculture, construction, and food processing. 1,200 potential victims identified.",
        "source": "Europol EMPACT Annual Report / Europol Situation Report on THB 2021",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "EU Forced Labour Ban Regulation — Commission Proposal (2022)",
        "summary": "European Commission proposed regulation banning products made with forced labour from the EU market (COM(2022) 453). Modelled on US customs enforcement approach. Competent authorities in Member States empowered to investigate and withdraw products. Burden of proof on authorities, not importers. Applies to products manufactured within and outside the EU.",
        "source": "European Commission COM(2022) 453 final",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "EU Forced Labour Regulation — Final Adoption (2024)",
        "summary": "European Parliament and Council adopted the Forced Labour Regulation in 2024, banning products made with forced labour from the EU single market. Regulation establishes risk-based enforcement, database of high-risk areas and products, and cooperation between national authorities and the Commission. Three-year implementation period for full enforcement. Customs authorities to play key enforcement role.",
        "source": "Official Journal of the European Union / European Parliament resolution 2024",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "European Court of Justice — Posted Workers and Labour Exploitation (2020)",
        "summary": "ECJ ruled in multiple cases (C-784/19, C-620/18) on posted workers and the application of host country labour standards. Court affirmed that host Member State minimum wage and working conditions apply to all posted workers regardless of the law of the sending state. Rulings strengthened protections against exploitation through fraudulent posting arrangements.",
        "source": "Court of Justice of the European Union / Directive 2018/957 (revised Posted Workers Directive)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "GRETA General Report — Labour Trafficking Across Europe (2022)",
        "summary": "Council of Europe GRETA published its 11th General Report focusing on labour trafficking. Found that labour exploitation was consistently underreported and under-prosecuted across member states. Key barriers to prosecution: difficulty distinguishing trafficking from labour law violations, victim reluctance to cooperate with authorities, and lack of specialised investigators and prosecutors.",
        "source": "GRETA 11th General Report on GRETA's Activities, Council of Europe",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Revised EU Anti-Trafficking Directive 2024 — Strengthened Provisions",
        "summary": "The revised EU Anti-Trafficking Directive adopted in 2024 added: criminalisation of knowingly using services of trafficking victims, forced marriage and illegal adoption as trafficking purposes, enhanced online prevention measures, mandatory training for frontline professionals, and improved data collection. Member States given 2 years to transpose.",
        "source": "European Parliament and Council Directive 2024/xxx / European Commission",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Coordinator — Strategic Priorities (2021-2025)",
        "summary": "EU Anti-Trafficking Coordinator published the EU Strategy on Combating Trafficking in Human Beings 2021-2025. Identified five priorities: reducing demand, breaking the business model of traffickers, protecting and supporting victims, promoting international cooperation, and improving governance. Strategy explicitly addresses labour trafficking and supply chain accountability.",
        "source": "European Commission COM(2021) 171 final",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "ELA (European Labour Authority) — Cross-Border Inspections (2022)",
        "summary": "European Labour Authority coordinated its first cross-border labour inspections targeting exploitation of mobile workers in agriculture and construction. Inspections conducted simultaneously in 8 Member States. Identified 500+ workers in potentially exploitative conditions. ELA facilitated information exchange between national labour inspectorates and law enforcement.",
        "source": "European Labour Authority Annual Report 2022",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Europol — Vietnamese Trafficking Networks in Europe (2020)",
        "summary": "Europol intelligence assessment identified Vietnamese trafficking networks as one of the most significant THB threats in Europe. Networks facilitated exploitation in nail salons, cannabis cultivation, garment workshops, and restaurants across 15 Member States. Victims subjected to debt bondage of EUR 20,000-40,000. Annual profits estimated at EUR 200 million. Coordinated operations resulted in 150+ arrests across Europe.",
        "source": "Europol SOCTA 2021 / Europol Intelligence Notification",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Eurojust Coordination — Romanian-German Agricultural Trafficking (2021)",
        "summary": "Eurojust coordination centre facilitated simultaneous arrests in Romania and Germany targeting a network trafficking Romanian workers to Bavarian farms. Workers exploited in asparagus and berry harvesting. Network used legitimate temporary employment agencies to conceal trafficking. 12 arrests, 50 victims identified. Assets of EUR 2.5 million frozen through European Investigation Orders.",
        "source": "Eurojust Press Release / DIICOT / Staatsanwaltschaft Munchen",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Corporate Sustainability Due Diligence Directive (2024) — Anti-Trafficking Provisions",
        "summary": "The EU Corporate Sustainability Due Diligence Directive (CSDDD) adopted in 2024 requires large EU companies to identify and prevent adverse human rights impacts in their value chains, explicitly including forced labour and trafficking. Companies must establish grievance mechanisms and remediation processes. Applies to companies with 500+ employees and EUR 150 million turnover.",
        "source": "European Parliament and Council / Official Journal of the European Union",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "ECJ Preliminary Ruling — Trafficking Victim Residence Rights (2018)",
        "summary": "European Court of Justice ruled in Case C-331/16 that Member States must grant residence permits to trafficking victims who cooperate with authorities, irrespective of the outcome of criminal proceedings. Court interpreted the Residence Permit Directive 2004/81/EC to require effective protection. Ruling strengthened victims' willingness to cooperate with investigations.",
        "source": "Court of Justice of the European Union, Case C-331/16",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "EU Financial Intelligence Units — Trafficking Financial Flows (2020)",
        "summary": "EU FIU.net facilitated cross-border financial intelligence exchange on trafficking proceeds. Analysis of 2,500 suspicious transaction reports across 19 Member States identified EUR 300 million in suspected trafficking proceeds in a single year. Common laundering methods: cash-intensive businesses (car washes, restaurants, nail salons), cryptocurrency, and property investment. Led to enhanced anti-money laundering guidelines for trafficking.",
        "source": "Europol FIU.net / EU Financial Intelligence Units Platform",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Frontex — Trafficking Detection at EU Borders (2021)",
        "summary": "Frontex reported increased use of trafficking indicators at EU external borders. Border guards trained under Frontex anti-trafficking programme identified 1,200 potential trafficking victims at border crossings in 2021. Main indicators: control by accompanying person, inability to speak freely, inconsistent travel documentation. Western Balkans and Eastern Mediterranean routes identified as highest risk.",
        "source": "Frontex Risk Analysis 2022 / Frontex Anti-Trafficking Training Manual",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "OSCE Special Representative — Labour Trafficking in Supply Chains (2021)",
        "summary": "OSCE Special Representative and Co-ordinator for Combating Trafficking published guidance on addressing trafficking in global supply chains connected to the OSCE region. Report mapped trafficking risks in European agriculture, construction, manufacturing, and domestic work. Recommended mandatory human rights due diligence legislation, enhanced labour inspection, and cross-border cooperation.",
        "source": "OSCE Office of the Special Representative for Combating Trafficking",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Europol EMPACT — Operation Ciconia Alba (2021)",
        "summary": "Annual EMPACT operational action targeting trafficking networks across Europe. Operation Ciconia Alba 2021 involved 29 countries and resulted in 89 arrests for labour trafficking. Identified networks exploiting workers in agriculture (40%), construction (25%), hospitality (15%), and manufacturing (20%). 400+ potential victims identified and referred to national referral mechanisms.",
        "source": "Europol / EMPACT THB Priority / Participating national law enforcement",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "European Parliament Resolution on Migrant Worker Exploitation (2021)",
        "summary": "European Parliament adopted resolution on exploitation of migrant workers in the EU calling for enhanced enforcement of the Employers' Sanctions Directive, decoupling work permits from specific employers, establishing firewalls between labour inspectorates and immigration enforcement, and ensuring undocumented workers can access justice without fear of deportation.",
        "source": "European Parliament Resolution 2021/2085(INI)",
    },

    # ======================================================================
    # ADDITIONAL UK CASES (251-260)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v Asefa [2018] — Ethiopian Domestic Servitude",
        "summary": "London couple convicted of holding an Ethiopian woman in domestic servitude for over 5 years. Victim brought to the UK on a visitor visa, forced to clean, cook, and care for children 18 hours daily without pay. Passport confiscated, victim isolated from the community. Defendants convicted under Section 1 of the Modern Slavery Act 2015. Sentenced to 6 and 4 years respectively.",
        "source": "Isleworth Crown Court / Metropolitan Police Modern Slavery Unit",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Operation Endeavour — Roma Exploitation Network (2017)",
        "summary": "National Crime Agency operation targeting a network exploiting Czech and Slovak Roma in Bristol and South West England. Victims forced to work in egg packaging, car washes, and recycling plants. Wages paid into accounts controlled by traffickers. 10 defendants convicted, lead trafficker sentenced to 12 years. Largest NCA modern slavery operation in the South West.",
        "source": "Bristol Crown Court / NCA / Avon and Somerset Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Scottish Fishing Vessel Exploitation — Filipino Crew (2019)",
        "summary": "Investigation into exploitation of Filipino workers aboard Scottish fishing vessels operating from Fraserburgh and Peterhead. Workers paid GBP 3-4 per hour for gruelling 18-hour shifts, documents confiscated, confined to vessels. Police Scotland and GLAA joint investigation. Two skippers convicted of labour exploitation. Led to enhanced protections in the Scottish fishing industry.",
        "source": "Aberdeen Sheriff Court / GLAA / Police Scotland",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "R v Ofosu and Others [2016] — Ghanaian Domestic Workers",
        "summary": "A Ghanaian-British couple convicted at Southwark Crown Court of trafficking two Ghanaian women for domestic servitude. Victims worked as live-in domestic workers for 3 years, paid GBP 50 per month, forbidden from leaving the house unaccompanied. One victim had her travel documents hidden. Both defendants sentenced to 6 years.",
        "source": "Southwark Crown Court / Metropolitan Police",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "Car Wash Exploitation — National Strategic Assessment (2019)",
        "summary": "GLAA National Strategic Assessment found that hand car washes remained the highest-risk sector for labour exploitation in the UK. Estimated 10,000+ hand car washes operating, majority unlicensed. Intelligence suggested exploitation at scale, with workers earning GBP 3-5 per hour. Joint operations with HMRC, police, and local authorities intensified. 200+ operations conducted in 2019.",
        "source": "GLAA Strategic Assessment 2019 / HMRC / National Police Chiefs' Council",
    },

    # ======================================================================
    # ADDITIONAL ITALY CASES (261-267)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Nardo Tomato Processing — Nigerian Worker Exploitation (2019)",
        "summary": "Lecce prosecutors investigated exploitation of Nigerian women in tomato picking and packing in Nardo, Puglia. Women subjected to both labour and sexual exploitation by caporali. Worked 12-hour shifts in extreme heat for EUR 3.50 per hour, forced into sexual services to reduce debts. 6 defendants convicted under Art. 603-bis and Art. 600 (trafficking). Sentences of 4-10 years.",
        "source": "Tribunale di Lecce / DDA Lecce",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Veneto Tannery Exploitation — Bangladeshi Workers (2020)",
        "summary": "Prosecutors in Vicenza investigated exploitation of Bangladeshi workers in leather tanneries in the Veneto region. Workers recruited in Bangladesh with promises of EUR 1,200 monthly, actual earnings EUR 400 after deductions. Exposed to toxic chemicals without protection. 50 workers identified in conditions of trafficking. Three tannery operators and two intermediaries convicted.",
        "source": "Procura della Repubblica di Vicenza / Carabinieri Tutela Lavoro",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Prato Textile District — Chinese Garment Worker Exploitation (2014-2020)",
        "summary": "Multiple investigations in Prato's Chinese textile district, Europe's largest garment production cluster. Thousands of Chinese workers employed in over 5,000 Chinese-owned firms. In 2013, 7 workers died in a factory fire at Teresa Moda, sleeping in the factory. Subsequent prosecutions targeted workshop operators for labour exploitation, fire safety violations, and trafficking. Systematic inspections identified widespread violations.",
        "source": "Procura della Repubblica di Prato / Vigili del Fuoco / INAIL",
    },

    # ======================================================================
    # ADDITIONAL SPAIN CASES (268-273)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Basque Country Industrial Exploitation — Chinese Workers (2019)",
        "summary": "Ertzaintza (Basque police) investigated exploitation of Chinese workers in industrial laundries and food processing plants in Bizkaia. Workers brought from China through Portugal, employed without permits, wages of EUR 3-4 per hour. Housed in overcrowded factory dormitories. 3 operators arrested and charged with trafficking under Art. 177 bis.",
        "source": "Ertzaintza / Audiencia Provincial de Bizkaia",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Andalusia Olive Oil Industry — Moroccan Worker Exploitation (2021)",
        "summary": "Guardia Civil and labour inspectors investigated exploitation of Moroccan seasonal workers in olive oil production in Cordoba and Jaen. Workers employed through intermediaries, housed in abandoned cortijos, paid below minimum wage. Women workers particularly vulnerable. Proceedings initiated against 5 agricultural operators and 3 intermediaries.",
        "source": "Guardia Civil / Inspeccion de Trabajo de Andalucia",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Operation Yuletide — Hotel and Tourism Exploitation (2020)",
        "summary": "National Police dismantled a network exploiting Latin American workers in hotels and restaurants on the Costa del Sol. Workers from Colombia, Venezuela, and Peru employed without permits, paid EUR 600 per month for 60+ hour weeks. Network used debt bondage to control workers. 7 arrests, 50 victims identified across Malaga province.",
        "source": "Policia Nacional / Juzgado de Instruccion de Malaga",
    },

    # ======================================================================
    # ADDITIONAL FRANCE CASES (274-278)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Corsican Agricultural Exploitation — North African Workers (2019)",
        "summary": "Labour inspectors in Corsica investigated exploitation of Moroccan and Tunisian seasonal workers in clementine harvesting. Workers recruited through OFII programmes but subjected to conditions exceeding contract terms. Housed in shipping containers, paid below minimum wage. Three agricultural estates sanctioned, one operator prosecuted for undeclared employment and exploitation.",
        "source": "Inspection du Travail de Corse / Procureur de la Republique d'Ajaccio",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Pas-de-Calais Market Gardening — Romanian Worker Trafficking (2021)",
        "summary": "Gendarmerie investigated exploitation of Romanian workers in market gardening near Calais. Workers recruited in Romania, transported by van, housed in caravans on farm properties. Paid EUR 4 per hour, subjected to verbal abuse and threats. Investigation identified 35 victims across 8 farms. Three Romanian intermediaries and 2 French farm operators prosecuted.",
        "source": "Gendarmerie Nationale / Tribunal Judiciaire de Boulogne-sur-Mer",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Ile-de-France Cleaning Sector — West African Worker Exploitation (2018)",
        "summary": "OCLTI investigated exploitation of Malian and Senegalese workers by a Paris-based cleaning company servicing offices and government buildings. Workers employed without contracts, paid EUR 3-4 per hour for night shifts, threatened with denunciation to immigration authorities. 60 workers identified. Company director convicted of trafficking for labour exploitation. EUR 800,000 in unpaid wages ordered.",
        "source": "Tribunal Correctionnel de Paris / OCLTI",
    },

    # ======================================================================
    # ADDITIONAL GERMANY CASES (279-284)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Munich Restaurant Chain — Indian Worker Trafficking (2020)",
        "summary": "Munich prosecutors investigated a chain of Indian restaurants exploiting Indian workers on cook visas. Workers recruited in India with promises of EUR 2,500 monthly, actual take-home EUR 800 after illegal deductions. Forced to work 70+ hours weekly, housed in shared rooms above restaurants. Three restaurant owners convicted under Section 232 StGB. Compensation of EUR 50,000 per victim ordered.",
        "source": "Staatsanwaltschaft Munchen I / Zoll",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Baden-Wurttemberg Agricultural Exploitation — Season Workers (2019)",
        "summary": "Labour inspectors in Baden-Wurttemberg found systematic exploitation of seasonal agricultural workers during strawberry and asparagus harvests. Workers from Romania, Poland, and Georgia employed through subcontractors. Accommodation costs of EUR 10 per day deducted from piece-rate wages. Investigation across 60 farms found violations in 45%. Multiple employers fined, 3 prosecuted for trafficking.",
        "source": "Gewerbeaufsichtsamt Baden-Wurttemberg / Staatsanwaltschaft Stuttgart",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Bremen Shipyard — Subcontractor Exploitation Chain (2021)",
        "summary": "Customs and police investigated a chain of subcontractors exploiting workers at the Bremen shipyard. Workers from Croatia, Serbia, and Bosnia employed through a cascade of 4 subcontractors. Each layer took a cut of wages, leaving workers with EUR 4-5 per hour. 150 workers affected. Lead subcontractor convicted of tax fraud and labour exploitation.",
        "source": "Zollfahndungsamt Bremen / Staatsanwaltschaft Bremen",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "Thuringia Slaughterhouse — Romanian Worker Exploitation (2020)",
        "summary": "Following the Tonnies scandal, investigations expanded to other meat processing facilities. Thuringia prosecutors found Romanian workers in a slaughterhouse near Jena working 12-hour shifts, 6 days a week. Workers housed in overcrowded apartments provided by subcontractor, rent deducted at EUR 300 per bed per month. Subcontractor convicted, slaughterhouse company fined EUR 200,000.",
        "source": "Staatsanwaltschaft Gera / Thuringer Landesamt fur Verbraucherschutz",
    },

    # ======================================================================
    # ADDITIONAL NETHERLANDS CASES (285-289)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "E-Commerce Warehouse Exploitation — Distribution Centre Workers (2021)",
        "summary": "Inspectie SZW investigated exploitation of Eastern European workers in e-commerce distribution centres in Brabant. Workers recruited through Polish and Romanian temporary agencies, housed 6-8 per room in agency-provided housing. Net pay after deductions fell below minimum wage. Agency licence revoked, two agency directors prosecuted for trafficking under Art. 273f.",
        "source": "Inspectie SZW / Rechtbank Oost-Brabant",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Schiphol Airport Area — Logistics Worker Exploitation (2020)",
        "summary": "Investigation into exploitation of workers in logistics and cargo handling near Schiphol Airport. Polish and Romanian workers employed through chains of temporary agencies, deductions for housing, transport, and health insurance reduced wages below minimum. 80 workers identified. Two temporary agencies fined, one agency owner prosecuted. Led to enhanced Schiphol area labour inspections.",
        "source": "Inspectie SZW / Rechtbank Noord-Holland",
    },

    # ======================================================================
    # ADDITIONAL CROSS-BORDER AND MULTI-COUNTRY (290-300)
    # ======================================================================

    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Europol Operation Webmaster — Online Recruitment for Trafficking (2021)",
        "summary": "Europol-coordinated operation targeting online recruitment platforms used by traffickers. Investigation spanned 14 Member States, identified 117 suspects using social media and job platforms to recruit victims for labour exploitation. Platforms included fake employment agencies on Facebook and dedicated websites. Resulted in 45 arrests and identification of 300+ potential victims.",
        "source": "Europol / EC3 (European Cybercrime Centre)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "Eurojust — Multi-Country Garment Industry Investigation (2020)",
        "summary": "Eurojust coordinated investigation across Italy, Romania, and Bulgaria targeting a network exploiting workers in garment production. Workers recruited in Eastern Europe, brought to Italian textile workshops. Investigation revealed EUR 5 million in evaded social contributions. Simultaneous arrests in 3 countries. 15 defendants prosecuted, network's legitimate company front liquidated.",
        "source": "Eurojust / DDA Napoli / DIICOT / Spetsializirana Prokuratura",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "EU",
        "title": "GRETA — Compensation for Trafficking Victims Report (2022)",
        "summary": "GRETA thematic report found that fewer than 5% of identified trafficking victims across Council of Europe member states received compensation. Labour trafficking victims least likely to receive any redress. Main barriers: lack of legal aid, difficulty identifying perpetrator assets, inadequate state compensation schemes, and victims leaving the country before proceedings concluded.",
        "source": "GRETA Thematic Report on Access to Compensation, Council of Europe",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Lombardy Logistics — Egyptian and Ghanaian Worker Exploitation (2021)",
        "summary": "Milan prosecutors investigated exploitation of Egyptian and Ghanaian workers in logistics cooperatives supplying major Italian supermarket chains. Workers employed through cooperatives that systematically underpaid, with false payslips showing higher amounts. 200+ workers affected, EUR 3 million in underpaid wages. Four cooperative managers convicted under Art. 603-bis.",
        "source": "Procura della Repubblica di Milano / Guardia di Finanza",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IT",
        "title": "Naples Camorra-Linked Garment Exploitation (2019)",
        "summary": "DDA Naples prosecuted Camorra-linked enterprises exploiting Chinese and Pakistani workers in clandestine garment workshops producing counterfeit luxury goods. Workers confined to underground workshops, paid EUR 2-3 per hour, producing fake designer items. Investigation revealed links between counterfeiting and trafficking. 18 defendants convicted, assets of EUR 10 million confiscated.",
        "source": "DDA Napoli / Guardia di Finanza / Carabinieri",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DE",
        "title": "COVID-19 Impact on Labour Trafficking — BKA Assessment (2021)",
        "summary": "BKA assessment found that COVID-19 pandemic increased vulnerability of migrant workers to trafficking. Seasonal agricultural workers accepted worse conditions due to travel restrictions and economic pressure. Meat processing outbreaks exposed pre-existing exploitation. Remote working reduced labour inspections. BKA recorded 18% increase in reported labour exploitation cases from 2019 to 2021.",
        "source": "Bundeskriminalamt (BKA) Bundeslagebild Menschenhandel 2021",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BE",
        "title": "Zeebrugge Port — Lorry Transport Worker Exploitation (2019)",
        "summary": "Federal police investigated exploitation of Eastern European truck drivers operating from the Zeebrugge area. Drivers employed through letterbox companies in Slovakia and Malta, paid well below Belgian rates for hours worked in Belgium. Drivers confined to truck cabins for rest periods, no proper accommodation. Investigation linked to broader enforcement of EU rules on truck driver rest periods.",
        "source": "Police Federale / Auditorat du Travail de Bruges",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Athens Garment District — Pakistani and Bangladeshi Workers (2019)",
        "summary": "Hellenic Police raided 20+ garment workshops in the Metaxourgio district of Athens. Found Pakistani and Bangladeshi workers sewing garments in basement workshops for 14+ hours daily. Workers sleeping on workshop floors, paid EUR 2-3 per hour. 8 workshop operators arrested for trafficking. 65 victims identified and referred to the National Referral Mechanism.",
        "source": "Hellenic Police Anti-Trafficking Unit / Protodikeio Athinon",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PL",
        "title": "Wielkopolska Food Processing — Filipino Worker Exploitation (2021)",
        "summary": "Labour inspectors in Wielkopolska region investigated exploitation of Filipino workers in food processing plants. Workers recruited through a Philippine agency, paid PLN 10-12 per hour (below sectoral minimum), excessive overtime, deductions for employer-provided accommodation. 40 workers identified. Two plant managers and one recruitment agent prosecuted under Art. 189a.",
        "source": "Panstwowa Inspekcja Pracy / Prokuratura Okregowa w Poznaniu",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "NL",
        "title": "Dutch National Rapporteur — Gig Economy and Trafficking Risk (2022)",
        "summary": "Dutch National Rapporteur on Trafficking published analysis of trafficking risks in the gig economy and platform work. Found that platform companies' model of classifying workers as independent contractors increased vulnerability to exploitation. Recommended: platform accountability for worker conditions, mandatory identity verification, and monitoring of pay rates against minimum wage equivalents.",
        "source": "Nationaal Rapporteur Mensenhandel / Advisory report to Dutch Parliament",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "SE",
        "title": "Construction Sector — Posted Worker Fraud in Stockholm (2020)",
        "summary": "Swedish police and Work Environment Authority investigated exploitation of posted workers on construction sites in Stockholm. Workers from Lithuania and Latvia employed through shell companies registered in Estonia. Paid SEK 40-50 per hour (well below collective agreement rates of SEK 180). 70 workers identified. Investigation linked to EUR 4 million in tax fraud. Company directors convicted.",
        "source": "Polismyndigheten / Arbetsmiljoerket / Skatteverket",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FI",
        "title": "Construction Sector — Estonian Subcontractor Exploitation (2020)",
        "summary": "Finnish prosecutors investigated exploitation of Estonian construction workers on building sites in the Helsinki metropolitan area. Workers employed through Estonian companies under posted worker arrangements but paid EUR 6-7 per hour instead of Finnish collective agreement rates of EUR 16-18. 100+ workers affected. Company directors convicted of extortionate work discrimination and tax fraud.",
        "source": "Helsingin Karajaoikeus / AVI / Verohallinto (Tax Administration)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "IE",
        "title": "Horticultural Exploitation — Migrant Greenhouse Workers in Wexford (2020)",
        "summary": "WRC and MRCI investigated exploitation of Eastern European and South American workers in protected horticulture (greenhouses) in County Wexford. Workers paid per punnet of berries picked, earning below minimum wage during slow periods. Housed in mobile homes on farm property. Multiple WRC complaints upheld with back-pay awards. One employer referred for criminal investigation.",
        "source": "Workplace Relations Commission / MRCI / An Garda Siochana",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PT",
        "title": "Algarve Tourism Sector — Brazilian Worker Exploitation (2021)",
        "summary": "Portuguese labour inspectors investigated exploitation of Brazilian workers in hotels and restaurants in the Algarve during tourist season. Workers recruited in Brazil with promises of EUR 1,000 monthly, actual earnings EUR 400-500 after deductions. Housed in overcrowded apartments, threatened with deportation. ACT identified 60 workers in exploitative conditions. Three hotel operators sanctioned.",
        "source": "ACT / Ministerio Publico de Faro",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "RO",
        "title": "DIICOT — Internal Trafficking for Forced Begging (2020)",
        "summary": "DIICOT prosecuted a network forcing vulnerable individuals, including persons with disabilities, into begging on streets in Bucharest and Timisoara. Victims controlled through violence and deprivation. Network earned EUR 500,000 annually from begging proceeds. 9 defendants convicted under Art. 210-211 of the Penal Code. Sentences of 3-10 years. Victims provided with rehabilitation support.",
        "source": "DIICOT / ANITP / Tribunalul Bucuresti",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HU",
        "title": "Ukrainian Worker Exploitation in Hungarian Agriculture (2022)",
        "summary": "Following the Ukrainian refugee crisis, Hungarian prosecutors investigated exploitation of Ukrainian nationals in agriculture in Szabolcs-Szatmar-Bereg county. Workers recruited at the border, employed in vegetable and fruit harvesting, paid HUF 600 per hour (below minimum). Housing provided in farm buildings without heating. 4 farm operators and 2 intermediaries prosecuted under Section 192.",
        "source": "Szabolcs-Szatmar-Bereg Megyei Forgyeszseg / Rendorseg",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "CZ",
        "title": "Prague Hospitality Sector — Philippine Worker Exploitation (2021)",
        "summary": "Prague prosecutors investigated exploitation of Filipino workers in hotels and restaurants in the city centre. Workers recruited through a Manila-based agency, charged CZK 200,000 (EUR 8,000) in recruitment fees, wages below minimum after deductions. Employers held workers' passports. 25 workers identified. Two hotel managers and the agency representative convicted under Section 168.",
        "source": "Obodni Soud pro Prahu 1 / Czech Police (Cizinecka Policie)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BG",
        "title": "Sofia Construction Sector — Central Asian Worker Trafficking (2021)",
        "summary": "Bulgarian prosecutors investigated exploitation of Uzbek and Kyrgyz workers on construction sites in Sofia. Workers brought through intermediaries in Turkey, documents confiscated, housed in unfinished buildings. Paid EUR 10-15 per day for heavy manual labour. 30 workers identified. Investigation facilitated by IOM Bulgaria. 3 construction company managers and 2 intermediaries convicted.",
        "source": "Sofiyska Gradska Prokuratura / IOM Bulgaria / GDBOP (General Directorate for Combating Organised Crime)",
    },
]
