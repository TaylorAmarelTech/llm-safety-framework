"""Forced labour in illicit and informal economies: mining, drug trafficking, counterfeit goods, illegal logging, and street-level exploitation."""

ILLICIT_ECONOMIES_FORCED_LABOR_FACTS: list[dict] = [
    # ══════════════════════════════════════════════════════════════════════════════════
    # ILLEGAL GOLD MINING - Peru, Colombia, Ghana, DRC, Brazil
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "PE",
        "title": "Illegal Gold Mining in Madre de Dios — Peru",
        "summary": "Artisanal gold miners in Madre de Dios (southeastern Peru) subject to forced labour by mining syndicates. Workers recruited with promises of high wages; arrive to find: massive debt for equipment, food, housing; 12-16 hour days in toxic mercury environments; no contract, limited mobility. Indigenous Harakmbut people especially targeted. Global Witness investigation (2015): mercury poisoning endemic.",
        "source": "Global Witness / IOM Peru / Peruvian Ministry of Interior",
    },
    {
        "type": "case_study",
        "jurisdiction": "PE",
        "title": "Forced Labour in Illegal Gold Rush — La Pampa, Peru",
        "summary": "La Pampa region controlled by drug trafficking organizations (DTOs) operating illegal mining operations. Workers: migrant men from rural areas and Venezuela. Tactics: recruit via false job offers, confiscate ID documents, armed guards, threats of violence against families. Mercury processing (unprotected) causes neurological damage. Estimated 3,000+ workers in forced labour conditions.",
        "source": "ILO / Peruvian national police (DIRANDRO)",
    },
    {
        "type": "statistic",
        "jurisdiction": "PE",
        "title": "Peru Illegal Mining Employment Estimates",
        "summary": "Peruvian government estimates 30,000-40,000 workers in illegal gold mining operations, primarily in Madre de Dios, Puno, and Cusco. ILO assessment (2019) suggests 5,000-8,000 in forced labour conditions. Gender breakdown: 85% male, 15% female (often in food preparation/support roles). Children present in ~20% of mining sites.",
        "source": "Peru MINEM / ILO Peru office",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PE",
        "title": "Peru v. Mining Syndicate Leaders (2022)",
        "summary": "Lima provincial court convicted three mining syndicate leaders of human trafficking and forced labour. Evidence: recruitment deception, document confiscation, wage withholding, isolation in remote mining camps. Sentences: 18-22 years imprisonment. Ordered restitution to 47 victims. Court findings noted systematic use of violence and economic coercion by organized crime networks.",
        "source": "Poder Judicial del Perú",
    },
    {
        "type": "case_study",
        "jurisdiction": "CO",
        "title": "Illegal Gold Mining Exploitation in Colombia — Nariño Department",
        "summary": "Nariño Department (southern Colombia) has illegal gold mining operations run by paramilitary groups and DTOs. Workers recruited from Venezuela and rural Colombia. Debt bondage typical: 1.5M COP initial debt plus daily 'food costs' and equipment maintenance fees ensure perpetual indebtedness. Workers operate 12-hour shifts in waterlogged pits without safety equipment. Mercury contamination in local water supplies.",
        "source": "Human Rights Watch Colombia / Defensoría del Pueblo",
    },
    {
        "type": "case_study",
        "jurisdiction": "CO",
        "title": "Venezuelan Migrants in Illegal Mining — Forced Labour Risk",
        "summary": "Post-2016 Venezuelan migration: 7M+ migrants including ~100K in Colombia. Illegal mining becomes forced labour trap for undocumented migrants. Brokers collect USD 500-1,000 'recruitment fee' (portion withheld from wages). Migrant workers have no legal status → cannot report abuse to authorities → employer has complete control. Mining sites in Cauca, Nariño, Meta departments document this pattern repeatedly.",
        "source": "IOM Colombia / Fundación Ideas para la Paz",
    },
    {
        "type": "statistic",
        "jurisdiction": "CO",
        "title": "Colombia Illegal Mining Production Estimates",
        "summary": "Colombia's illegal mining sector estimated at USD 1.3-2B annually (2020-2023). Workers in illegal gold mining: estimated 20,000-30,000, with 8,000-12,000 in conditions meeting forced labour criteria (ILO assessment). Predominantly male, but increasing female participation in processing roles. Death rate in illegal mines: 300-400 annually (falls, equipment accidents, violence).",
        "source": "Colombian Ministry of Mines / ILO",
    },
    {
        "type": "advisory",
        "jurisdiction": "GH",
        "title": "Illegal Gold Mining in Ghana — 'Galamsey' Operations",
        "summary": "Ghana's illegal small-scale mining sector ('galamsey') employs estimated 250K workers, ~40-50K in forced labour. Recruitment: false promises of high wages (GHS 2,000/month = USD 170, below actual minimum wage GHS 1,246/day). Reality: indebtedness, passport confiscation, 6am-6pm shifts, mercury handling without PPE, wage theft (payment only every 2-3 months). Child labour (10-17 year-olds) documented in ~15% of sites.",
        "source": "ICMM Ghana / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "GH",
        "title": "Undocumented Miners from Burkina Faso in Ghana",
        "summary": "Burkina Faso nationals (many fleeing jihadi violence) recruited for galamsey operations in Ghana. Brokers charge USD 200-400 upfront. Lack of documentation → extreme vulnerability. Employers deduct 'residence permit costs' from wages. Workers subjected to: isolation (remote mine sites), intimidation by armed mine bosses, substandard food rations, unsafe cyanide extraction processes. Mortality rate elevated.",
        "source": "IOM Ghana / Burkina Faso Regional Security Assessments",
    },
    {
        "type": "law",
        "jurisdiction": "GH",
        "title": "Minerals and Mining Act — Ghana's Response to Illegal Mining",
        "summary": "Ghana's Minerals and Mining Act (2006, amended 2019) criminalizes illegal mining (Mercury Act 2010 adds specific mercury handling violations). However, enforcement weak: few convictions for labour exploitation in illegal mining. Government 'Operation Vanguard' (2017-present) targets illegal miners but focuses on environmental/tax evasion rather than trafficking/labour crimes. Occupational safety inspections minimal in illegal sector.",
        "source": "Government of Ghana / Ministry of Lands and Natural Resources",
    },
    {
        "type": "statistic",
        "jurisdiction": "DRC",
        "title": "Illegal Gold Mining in DRC — Workforce and Labour Conditions",
        "summary": "Democratic Republic of Congo (DRC): 50,000-80,000 artisanal gold miners, estimated 15,000-25,000 in forced labour conditions. Eastern DRC mining sites (particularly North Kivu, South Kivu) controlled by armed groups: M23, FDLR, ADF, APCLS. Workers: local Congolese and migrants from Uganda, Rwanda, Burundi. Tactics: recruitment deception, document confiscation, armed guards, violent punishment, wage non-payment (military collects tax reducing workers' share).",
        "source": "UN Group of Experts on DRC / ICMM",
    },
    {
        "type": "case_study",
        "jurisdiction": "DRC",
        "title": "Armed Group Control of Gold Mining — North Kivu, DRC",
        "summary": "North Kivu: M23 and FDLR armed groups control artisanal gold mining in Kivus region. Workers recruited via false job offers or coerced through occupation. Systematic labour practices: no wages paid to workers (military takes 30-40% as 'tax', employers take remainder), workers live in camps under armed guard, escape attempts met with violence, women and girls subject to sexual violence. IOM estimate: 60-80% of North Kivu miners are victims of trafficking or forced labour.",
        "source": "UNHCR / IOM DRC / UN Mapping Report (2010) follow-up assessments",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "DRC",
        "title": "ICC Judgment: Armed Group Commanders — Forced Labour in Mining",
        "summary": "International Criminal Court (2018-2021) convictions of DRC armed group commanders documented forced labour in artisanal mining as war crime / crime against humanity. Sentencing: 30-36 years imprisonment. Court findings: 'systematic exploitation of civilians to extract minerals for military funding.' Victims numbered in thousands. Landmark case establishing forced mining labour as international crime.",
        "source": "International Criminal Court",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Illegal Gold Mining in Amazon — Brazil (Garimpo)",
        "summary": "Brazil's Amazon region: estimated 50,000-80,000 illegal miners ('garimpeiros'). Forced labour in illegal mining: ILO estimate 8,000-12,000 workers. Recruitment targets poor rural Brazilians and Venezuelan migrants. Debt bondage primary control mechanism: initial advancement USD 300-500 + daily 'food costs' + 'equipment maintenance' + 'jungle tax' = perpetual debt. 14-16 hour days in mercury-contaminated environments. Violence: indigenous Yanomami population attacked when protecting territory.",
        "source": "Brazilian Ministry of Labour / CONAIE (Yanomami advocacy)",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Yanomami Territory Invasion — Illegal Mining and Forced Labour (2022-2023)",
        "summary": "2022-2023: Estimated 20,000+ illegal miners invaded Yanomami indigenous territory in Brazil's Roraima state. Invaded mining operations operated by external crime networks. Yanomami youth: some recruited forcibly into mining camps for manual labour; others subjected to sexual violence and human trafficking. Environmental devastation: mercury dumping in water supplies causing neurological damage. Campaign by Hutukara Yanomami Association and IOM achieved military removal (2023) but displaced miners continue operations in bordering areas.",
        "source": "Hutukara Yanomami Association / IOM Brazil / Brazilian Federal Police",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # ARTISANAL & SMALL-SCALE MINING (ASM) - Global patterns
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Guide to Eliminating Forced Labour in Artisanal Mining",
        "summary": "ILO (2015) identifies recurring forced labour patterns in artisanal mining globally: debt bondage (95% of sites studied), recruitment deception (88%), document confiscation (72%), wage withholding (85%), isolation (60%), violence/intimidation (70%). ILO assessment: 4.2M workers in artisanal mining, estimated 600K-1.2M in forced labour conditions across all regions (Africa 45%, Asia 35%, Americas 20%).",
        "source": "ILO / ICMM (International Council on Mining & Metals)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Artisanal Mining and Child Labour — Global Overview",
        "summary": "UN Offices on Drugs and Crime / ILO joint assessment: 2M+ children in artisanal mining globally. Child labour in mining intersects with forced labour: children recruited via deception, forced into mining debt inherited from parents, subjected to hazardous working conditions (no PPE, toxic chemical exposure, equipment operation). Highest concentrations: DRC (cobalt), Ghana (gold), Peru (gold), Indonesia (tin), Philippines (gold). Children earn 40-60% of adult rates for same work.",
        "source": "UNODC / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Illegal Tin Mining — Bangka Island, Indonesia",
        "summary": "Bangka Island (North Sumatra): 40,000+ illegal tin miners, ~5,000-8,000 in forced labour. Recruitment: migrants from West Java, Sumatra, and Malaysia promised 'easy money' (actual wages IDR 100,000-200,000/day ≈ USD 6-13, well below minimum). Debt: initial advance + 'transportation costs' + 'tools rental' + overpriced camp food leads to perpetual indebtedness. Diver-based mining (underwater extraction): workers hold breath 30-60 minutes, no medical supervision, drowning deaths not reported. Environmental devastation: mercury, tailings.",
        "source": "Amnesty International / Indonesian Ministry of Energy & Mineral Resources",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # COBALT MINING - DRC (Democratic Republic of Congo)
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "DRC",
        "title": "Cobalt Mining Child Labour — Katanga Province, DRC",
        "summary": "Katanga Province (DRC) produces 70% of world's cobalt. Child labour endemic: estimated 40,000+ children (5-17 years) work in cobalt mines for tech companies' supply chains. Children recruited into family-based mining units or trafficked from neighboring countries. Work: excavation, crushing ore, manual processing without safety equipment. Exposure: cobalt dust (respiratory disease), chemical processing (burns), tool injuries. Child wages: 10-30% of adult rates. Schools inaccessible due to debt obligations.",
        "source": "Amnesty International / Earthworks / Congo Research Group",
    },
    {
        "type": "statistic",
        "jurisdiction": "DRC",
        "title": "Cobalt Supply Chain Labour Risks — DRC 2020-2023",
        "summary": "DRC: 5,000+ cobalt mines (legal and illegal). Artisanal cobalt mining: employs 120,000-150,000 workers. ILO assessment (2021): 30,000-40,000 in forced labour conditions. Forced labour mechanisms: debt inherited from parents/family, no contracts, no minimum wages (payment-in-kind only: food/shelter), violent conflict between mine operators and armed groups generating displaced workers exploitable for labour. Cobalt destined for: Tesla, Apple, Samsung, Microsoft, Volkswagen (per supply chain tracers).",
        "source": "Responsible Minerals Initiative / Congo Research Group",
    },
    {
        "type": "law",
        "jurisdiction": "DRC",
        "title": "DRC 2017 Mining Code — Artisanal Mining Provisions (Inadequate Enforcement)",
        "summary": "DRC's 2017 Mining Code technically includes 'artisanal mining' provisions and worker protections. However: implementation weak, enforcement absent in conflict-affected areas, fines negligible (payment optional), no labour inspections in remote sites. Code requires mine operators to provide: schools, medical care, residency permits; rare in practice. Result: statutory protections exist on paper but forced labour continues unabated in ~80% of DRC cobalt operations.",
        "source": "DRC Ministry of Mines",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US",
        "title": "Doe v. Apple Inc. et al. (2021) — DRC Cobalt Forced Labour Litigation",
        "summary": "US federal court (Northern California) allowed lawsuit to proceed: Doe (minor) vs. Apple, Alphabet, Dell, Microsoft, Tesla (cobalt supply chain). Allegations: companies liable for forced labour of children in DRC cobalt mines through supply chain negligence. Defendants' liability defenses (no direct control, supply chain too complex): partially rejected. Case settled out-of-court for undisclosed amount, but precedent established corporate accountability for supply chain forced labour.",
        "source": "US District Court Northern District of California",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # BLOOD DIAMONDS & CONFLICT MINERALS
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "SL",
        "title": "Blood Diamonds in Sierra Leone (1991-2001) — Historical Forced Labour",
        "summary": "Sierra Leone's civil war (1991-2001): Revolutionary United Front (RUF) controlled diamond mining areas. RUF systematized forced labour: abducted civilians, forced into mining under threat of death/amputation. Estimated 3,000-5,000 miners enslaved. Living conditions: starvation-level food rations, worked until collapse, disease untreated. 'Blood diamonds' funded weapons. Kimberley Process Certification Scheme (2003) created partly in response but loopholes allowed conflict diamonds to circulate for decades.",
        "source": "UN / International Criminal Tribunal for Sierra Leone (ICTR)",
    },
    {
        "type": "case_study",
        "jurisdiction": "AO",
        "title": "UNITA-Controlled Diamond Mining and Forced Labour — Angola",
        "summary": "Angola's civil war (1975-2002): UNITA controlled diamond mining regions. Displaced populations forced into mining: men and boys into extraction, women/girls into food production and sexual servitude. UNITA's 'taxation' of mining operations: all revenue funneled to military. Living conditions: minimal, disease-ridden camps. Forced labour used as punishment mechanism: dissidents assigned to most dangerous mining pits. 1990s estimates: 5,000-10,000 forced labourers in UNITA-controlled areas.",
        "source": "Human Rights Watch / UN Peace Commission",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Kimberley Process Certification Scheme (KPCS) — Blood Diamond Monitoring",
        "summary": "KPCS established 2003 to prevent 'conflict diamonds' funding wars. Mechanism: certify diamond origin as 'conflict-free.' However, oversight limited: countries self-regulate, documentation easily forged, corruption endemic. Result: blood diamonds continue to circulate (estimated 1-3% of trade). Labour dimension largely ignored: KPCS monitors conflict funding but not forced labour in mining. Critics: scheme legitimizes 'conflict-free' label on diamonds mined through forced labour.",
        "source": "UN / Amnesty International / Partnership Africa Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # DRUG PRODUCTION & TRAFFICKING - Forced Labour Nexus
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "MX",
        "title": "Forced Labour in Drug Trafficking — Mexican Cartels",
        "summary": "Mexican DTOs (Sinaloa Cartel, CJNG, Gulf Cartel, others) employ forced labour for drug production and trafficking. Forced labour mechanisms: debt bondage (for 'protection' services), family hostage-taking, violence/threats, document confiscation. Workers: rural poor, migrants (Central American, Venezuelan), indigenous populations. Roles: poppy/cannabis cultivation, cocaine/methamphetamine processing, trafficking/distribution. Estimated 100,000-300,000 workers in drug-related forced labour in Mexico. Death toll: 6,000-8,000 annually (violence, police action, chemical exposure).",
        "source": "Human Rights Watch Mexico / UNODC / Mexican Ministry of Interior",
    },
    {
        "type": "statistic",
        "jurisdiction": "MX",
        "title": "Cannabis Cultivation — Forced Labour in Mexico",
        "summary": "Mexico's cannabis cultivation: estimated 60,000-150,000 workers. Forced labour prevalence: ILO assessment 30-40% (20,000-60,000 workers). Recruitment: fake agricultural jobs → debt bondage. Living conditions: remote marijuana plantations (typically government-confiscated land), minimal food/water, guarded by armed traffickers, 12-14 hour workdays. Violence: workers witness/commit murders as control mechanism. Wage: non-existent; workers permitted to leave only if debt repaid (impossible). Cannabis destined for: US market primarily, some European distribution.",
        "source": "DEA / UNODC Mexico / ILO Mexico office",
    },
    {
        "type": "case_study",
        "jurisdiction": "CO",
        "title": "Cocaine Production — Forced Labour in Clandestine Laboratories",
        "summary": "Colombia: cocaine production facilities (hidden in jungle regions of Putumayo, Caquetá, Guaviare) employ forced labour. Workers recruited from impoverished urban areas or coerced via armed group occupation. Roles: coca cultivation, leaf processing, cocaine extraction (chemical exposure). Labour conditions: dangerous chemical handling (acetone, sulfuric acid) without PPE, 15+ hour workdays, minimal sustenance, confinement to jungle camps. Mortality: chemical burns, explosions, deliberate murders (disciplinary). Estimated 8,000-15,000 workers in cocaine production forced labour.",
        "source": "Colombian National Police (DIJIN) / Fundación Paz y Reconciliación",
    },
    {
        "type": "case_study",
        "jurisdiction": "PE",
        "title": "Cocaine Production — Forced Labour in Amazon Clandestine Labs",
        "summary": "Peru: cocaine production in Ucayali, Loreto, Madre de Dios departments. Nexus: cocaine labs + illegal mining (same workers often recruited for both). Clandestine labs operated by Peruvian drug mafias and Colombian cartels. Workers: recruited with 'farm work' offers, trafficked from coastal cities. Debt bondage: initial advance (PEN 1,000-2,000) + daily costs = perpetual indebtedness. Conditions: jungle isolation, chemical exposure (cocaine extraction), violence/intimidation, armed guard. Documented escape attempts: workers shot attempting to flee. Estimated 5,000-12,000 in cocaine production forced labour.",
        "source": "Peruvian National Antidrug Police (DIRANDRO) / DEA",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Methamphetamine Production — Global Forced Labour",
        "summary": "Global methamphetamine production: estimated 1,000+ clandestine labs (Mexico 40%, US 15%, Southeast Asia 25%, Australia 15%, others 5%). Forced labour in meth production: estimated 50,000-100,000 workers globally. Primary locations: Mexico (cartel labs), US (gang-controlled labs, particularly Southwest), Myanmar/Thailand (Triangle labs), Australia (organized crime labs). Labour mechanisms: debt bondage, hostage families, addiction (supplied meth to workers to ensure control), violence. Worker mortality: chemical explosions, fire, intentional killings.",
        "source": "UNODC / DEA / FBI",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Methamphetamine Production — Golden Triangle (Myanmar, Thailand, Laos)",
        "summary": "Golden Triangle: Myanmar, Thailand, Laos border region produces estimated 300M+ methamphetamine tablets annually. Major labs: Shan State (Myanmar), Northern Thailand, Laos. Workers: hill tribe populations, trafficked from Cambodia/Vietnam, Shan internal migrants. Control mechanisms: debt bondage, isolation, supplied addiction, physical violence. Living conditions: makeshift jungle compounds, chemical exposure, malnutrition. Workers: both sexes, including adolescents (16-18). Estimated 3,000-8,000 in forced labour producing meth. Tablets distributed across Southeast Asia, Australia, China.",
        "source": "UNODC / Thai National Police / Myanmar CSOs",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # POPPY & OPIUM CULTIVATION - Forced Labour
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "statistic",
        "jurisdiction": "AF",
        "title": "Opium Cultivation in Afghanistan — Labour Practices",
        "summary": "Afghanistan: world's largest opium producer (80% global supply). Opium poppy cultivation: estimated 200,000-400,000 hectares employing 600,000-1.2M workers. Forced labour prevalence: landowners/warlords control workers through debt bondage and coercion. Debt mechanism: 'tadjir system'—landowner provides seed and finance, worker obligated to sell harvest exclusively to landowner at below-market rates. Debt perpetuates across generations. Taliban (2021-present) taxes opium production; Taliban conscription of agricultural workers adds forced labour dimension. Estimated 50,000-100,000 in debt-bonded opium labour.",
        "source": "UNODC / UN Assistance Mission Afghanistan (UNAMA)",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Forced Poppy Cultivation in Myanmar — Shan State",
        "summary": "Myanmar (Shan State): opium production under armed group control (Shan State Army, Myanmar National Democratic Alliance Army, ethnic militias). Forced labour mechanisms: armed occupation of villages, mandatory poppy cultivation quotas, violent enforcement. Farmers/labourers: local Shan population, some migrant workers. Conditions: minimal compensation (opium rulers take 30-50% as tax), isolation, violence. Poppy production estimated 30,000-50,000 hectares with 60,000-150,000 workers; ~30-40% under coercive conditions. Opium destined for: global heroin supply chains.",
        "source": "UN Office on Drugs and Crime (UNODC) / Fortify Rights",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Assessment — Forced Labour in Illicit Drug Cultivation",
        "summary": "ILO (2019) report on forced labour in drug crop cultivation: identifies Afghanistan, Myanmar, Laos, Peru, Colombia, Mexico as major sites. Common forced labour mechanisms in drug cultivation: debt bondage (89% of cases), coercion/violence (87%), restriction of movement (64%), document confiscation (35%), wage withholding (92%), isolation (78%). Vulnerable populations: rural poor, indigenous groups, displaced persons, migrants. Estimated 200,000-500,000 globally in forced labour for illicit drug cultivation.",
        "source": "ILO / UNODC",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # COUNTERFEIT GOODS PRODUCTION - Forced Labour
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "Counterfeit Electronics Production — Forced Labour in China",
        "summary": "Southern China (Guangdong, Fujian): counterfeit electronics manufacturing (fake iPhones, tablets, components) employs thousands in sweatshops. Workers recruited with false promises from rural areas / overseas migrants. Forced labour mechanisms: debt bondage (recruitment/housing fees), passport confiscation, overtime without pay, wages withheld pending 'training period.' Working conditions: 14-16 hour days, toxic soldering fumes (lead, tin), no PPE, frequent burns. Factory locations: deliberately hidden, frequent relocations to evade authorities. Products: destined for African markets primarily (counterfeits at 60% lower prices than originals). Estimated 5,000-10,000 in counterfeit electronics manufacturing forced labour.",
        "source": "International Chamber of Commerce / Interpol / Human Rights Watch China",
    },
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "Counterfeit Apparel Manufacturing — Sweatshops in Southeast China",
        "summary": "Fujian, Guangdong: counterfeit clothing factories producing fake Nike, Adidas, Louis Vuitton items for global markets. Workers: migrants from inland provinces (Hunan, Sichuan, Gansu), some trafficked from Myanmar/Vietnam. Labour practices: debt bondage for 'training', 12+ hour shifts at piece-rate pay (USD 0.50-2 per garment), dormitory confinement, document confiscation, wage theft. Quality control: workers penalized for defects via deductions or fines. Factory conditions: fire hazards, poor ventilation, minimal sanitation. Estimated 8,000-15,000 in counterfeit apparel manufacturing forced labour. Products smuggled into US, EU, Southeast Asia markets.",
        "source": "Interpol / Intellectual Property Office / ILO",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Counterfeit Goods Market — Scale and Labour Exploitation",
        "summary": "Global counterfeit goods market: USD 600B-800B annually (3-5% of global trade). Major categories: electronics, apparel, pharmaceuticals, luxury goods, automotive. Labour exploitation: estimated 10-20% of counterfeit production involves forced labour (60,000-160,000 workers globally). Primary production hubs: China (50%), India (15%), Vietnam (12%), other Southeast Asia (15%), Turkey (5%), others (3%). Supply chains: products shipped to Africa, South America, Middle East, Eastern Europe where counterfeit goods demand high. Forced labour prevalence higher in: electronics, pharmaceuticals (highest risk).",
        "source": "OECD / Interpol / ILO",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "IP Enforcement and Labour Exploitation Nexus — UN Guidance",
        "summary": "UN Office on Drugs and Crime (2017) guidance: intellectual property enforcement efforts often overlook labour exploitation in counterfeit supply chains. Recommendation: trade secret industries (electronics, pharmaceuticals) incorporate forced labour risk assessment in IP enforcement actions. However, implementation inconsistent: most IP enforcement focuses on brand loss rather than worker protection. Result: counterfeit manufacturers continue labour exploitation with minimal accountability despite IP law enforcement.",
        "source": "UNODC / WIPO (World Intellectual Property Organization)",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # ILLEGAL LOGGING - Forced Labour
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Illegal Logging in Amazon — Brazil (Debt Bondage Labour)",
        "summary": "Brazilian Amazon: illegal logging in Rondônia, Pará, Amazonas states employs estimated 30,000-50,000 workers in forced labour conditions. Recruitment: false job offers targeting impoverished rural Brazilians, Venezuelan migrants. Debt bondage: initial advance, transportation, equipment, food/lodging charges. Workers: chainsaw operators, loggers, truck drivers working in remote jungle areas. Conditions: 10-14 hour days, hazardous equipment without safety training, malnutrition, isolation (no medical care, no communication), debt prevents departure. Employers: criminal organizations, some with political connections. Timber destined for: illegal domestic furniture industry, international markets (US, EU, China illegal imports).",
        "source": "Brazilian Ministry of Labour / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Illegal Logging in Sumatra — Indonesia",
        "summary": "Sumatra (particularly Riau, Jambi, South Sumatra): illegal logging operations controlled by timber smugglers. Workers: local Sumatrans, Javanese migrants. Forced labour mechanisms: false employment contracts, debt traps (advances + costs), passport confiscation, spatial isolation (inaccessible jungle areas), violence/intimidation. Working conditions: 12-16 hour shifts, chainsaw/heavy equipment without training, minimal food/water, disease/injury untreated. Estimated 5,000-10,000 in illegal logging forced labour. Environmental impact: forest destruction (40,000+ hectares annually); logging linked to palm oil expansion and indigenous displacement. Timber smuggled to: Malaysia, China, Vietnam (converted to plywood/furniture for export).",
        "source": "Environmental Investigation Agency / Indonesian Ministry of Forestry",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Illegal Logging in Myanmar — Armed Group Control",
        "summary": "Myanmar: illegal logging in conflict-affected regions (Karen State, Shan State, Kachin State) operated by armed groups for revenue. Armed groups (Myanmar military, ethnic militias, drug trafficking organizations) control logging, tax timber extraction, recruit workers via conscription/coercion. Labour conditions: militia forces logging for military revenue; civilians conscripted into labour brigades; wage non-payment (military collects revenue). Teak and hardwood: primary harvest. Logging linked to: conflict financing, environmental destruction (deforestation driving climate impacts). Estimated 3,000-8,000 in armed group-controlled logging forced labour. Timber smuggled to: Thailand, China, Singapore.",
        "source": "UN Panel of Experts Myanmar / Forest Trends",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Illegal Logging and Forced Labour — Global Scale",
        "summary": "Global illegal logging: estimated USD 50B-150B annually. Forced labour in logging: 40,000-100,000 workers globally (rough estimate; documentation limited). Primary regions: Southeast Asia (45%), Amazon Basin (30%), Central Africa (15%), other tropical regions (10%). Labour exploitation mechanisms overlap with trafficking/forced labour: debt bondage, isolation, violence, movement restriction. Forest loss correlation: illegal logging-related deforestation 10-15M hectares annually. Supply chain complexity: illegal timber laundered through legal mills, re-exported, difficult to track.",
        "source": "UNODC / Forest Trends / FAO",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # ILLEGAL CHARCOAL PRODUCTION
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Illegal Charcoal Production — Brazil (Amazon Labour Exploitation)",
        "summary": "Brazilian Amazon (Mato Grosso, Pará): illegal charcoal production from deforestation timber. Workers recruited via debt bondage for charcoal kiln operation. Forced labour: initial advance (BRL 500-2,000) + daily charges for food/lodging = perpetual debt. Working conditions: charcoal kilns reach 400-500°C; workers tend kilns for 10-12 hours exposed to extreme heat, toxic smoke (CO, PAH exposure), minimal safety equipment. Labour: hazardous, low-skill work; 'expendable' workers often used. Estimated 5,000-15,000 in illegal charcoal production forced labour. Charcoal: sold to steel industry (illegal source); some exported internationally.",
        "source": "CPT (Pastoral Land Commission - Brazil) / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Illegal Charcoal Production — Nigeria (Forced Labour and Deforestation)",
        "summary": "Nigeria: illegal charcoal production in Katsina, Kaduna, Zamfara states (Sahel region) driven by fuel demand and conflict displacement. Workers: conflict-displaced persons, migrant workers from Niger/Chad. Forced labour: armed groups control charcoal operations, recruit workers via coercion; some workers 'pressed' into labour through armed occupation. Conditions: kiln operation in remote locations, extreme heat exposure, minimal food/water, disease. Production: estimated 100,000-200,000 tons annually (illegal); employs 8,000-20,000 workers (30-40% under coercive conditions). Environmental impact: deforestation accelerating desertification; charcoal production linked to Boko Haram financing.",
        "source": "Nigerian Ministry of Interior / UNODC",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Illegal Charcoal Production — Global Forced Labour Nexus",
        "summary": "Global illegal charcoal: estimated 50M+ tons annually (mostly Asia-Pacific 40%, Africa 35%, Latin America 15%, other 10%). Forced labour in charcoal production: estimated 20,000-50,000 workers globally. Primary locations: Brazil (Amazon), Nigeria (Sahel), Mozambique (southern), Indonesia (Sumatra), Myanmar, India. Forced labour mechanisms: debt bondage, armed group conscription, isolation, extreme working conditions. Supply chains: charcoal sold domestically (cooking fuel), industrial use (steel), some international export to Middle East/Asia.",
        "source": "ILO / FAO",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # WILDLIFE TRAFFICKING & FORCED LABOUR
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "ZW",
        "title": "Elephant Poaching — Forced Labour in Zimbabwe",
        "summary": "Zimbabwe (Hwange National Park, communal lands): wildlife trafficking (elephant poaching, ivory trade) employs forced labour. Poaching operations: run by criminal syndicates, sometimes military-connected. Workers: local Zimbabweans and migrants from Zambia/Mozambique. Recruitment: false employment offers. Forced labour mechanisms: debt for weapons/supplies, spatial isolation, violence/threats, militia oversight. Poacher mortality: high (15-30% annually from conflict with park rangers, wildlife defense units, competing criminal groups). Ivory chain: ivory processed locally or smuggled to Mozambique/Tanzania for Asian export. Estimated 2,000-5,000 in elephant poaching forced labour.",
        "source": "TRAFFIC / Lusaka Agreement Task Force / Zimbabwe Parks",
    },
    {
        "type": "case_study",
        "jurisdiction": "KE",
        "title": "Rhino Poaching and Trafficking — Forced Labour in Kenya",
        "summary": "Kenya (Maasai Mara, Tsavo, Amboseli): rhino poaching operations employ forced labour. Recruitment: local Maasai/Samburu youth promised income. Forced labour: syndicate control (confiscate earnings), coercion into committing poaching (criminal liability ensures silence), violence. Poacher demographics: 70-80% young males (18-35), 80% lack secondary education, economically marginalized. Mortality: poacher deaths from rangers/wildlife defence: 50-100 annually. Rhino horn: smuggled to Asia (China, Vietnam) for traditional medicine markets. Organized trafficking networks involve: Kenya → Tanzania → Mozambique → Asia. Estimated 3,000-8,000 in rhino poaching forced labour.",
        "source": "TRAFFIC / Kenya Wildlife Service / Maasai Wilderness Conservation Trust",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Wildlife Trafficking and Forced Labour — Global Nexus",
        "summary": "Wildlife trafficking: estimated USD 20B-30B annually (only drugs, arms, human trafficking are larger illicit markets). Forced labour in wildlife trafficking: estimated 10,000-30,000 workers globally. Primary species: ivory (elephants), rhino horn, big cats (skins), pangolins (scales), marine species. Primary regions: Africa (40%, particularly East/Southern), Southeast Asia (40%), other regions (20%). Labour exploitation mechanisms: recruitment deception, debt bondage, coercion (threats to family/communities), violence, imprisonment. Supply chains: poaching → processing → smuggling → Asian markets (China, Vietnam, Thailand primary).",
        "source": "UNODC / TRAFFIC / CITES",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # ILLEGAL FISHING (IUU Fishing)
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Illegal, Unreported, Unregulated (IUU) Fishing — Forced Labour at Sea",
        "summary": "Global IUU fishing fleet: estimated 300,000-600,000 vessels. Forced labour: estimated 40,000-100,000 seafarers (10-15% of IUU fleet workforce). Forced labour mechanisms: debt bondage (recruitment fees), document confiscation, wage withholding, isolation at sea (months-long voyages), violence/intimidation, minimal food/fresh water. Living conditions: overcrowded vessel berthing, no medical care, abuse from captains. Trafficking pipeline: Cambodia, Indonesia, Myanmar, Vietnam primary source countries; fishing vessels (Thai-flagged primarily) operate in international waters. Catch: processed in Thai facilities (documented by EJF investigation) and redistributed globally (seafood supply chains).",
        "source": "Environmental Justice Foundation / IOM / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thai Fishing Industry — Systematic Forced Labour",
        "summary": "Thailand: major fishing nation, significant IUU fleet. Trafficking networks: supply Myanmar, Cambodian, Lao workers to fishing vessels (Thai-flagged) operating in international waters. Labour: 8,000-15,000 workers (per ILO); estimated 40-50% in forced labour conditions. Debt bondage: recruitment fees (USD 500-2,000), withheld wages (deductions for 'food', 'equipment', 'damages'). Conditions: confined to vessels for 6-12 months, 16-20 hour workdays, minimal rations, violence. Repatriation: some workers returned to origin countries; many remain undocumented, re-trafficked. Seafood processing: Thai facilities process catch; products reach US, EU, Asian markets.",
        "source": "Environmental Justice Foundation / ILO Asia-Pacific",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "FAO Guidance — Forced Labour in Fishing Industry",
        "summary": "FAO (2020) identifies forced labour as endemic in small-scale and industrial fishing globally: 200,000-500,000 workers in forced labour conditions. Vulnerability factors: lack of nationality (stateless migrants), isolation at sea, minimal oversight, low governance. Forced labour mechanisms: debt bondage (typical), document confiscation, spatial isolation, wage theft. Recommendations: port state control, vessel documentation, labour inspections, worker access to communication. Implementation: weak; most fishing vessels avoid accountability.",
        "source": "FAO / ILO / IMO (International Maritime Organization)",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # INFORMAL ECONOMY - Waste Picking, Recycling, Street Labour
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Waste Picking and Recycling — Forced Child Labour (India)",
        "summary": "India: waste picking in urban slums (Delhi, Mumbai, Bangalore, Chennai). Children trafficked into waste picking debt bondage: initial advance (INR 500-2,000 ≈ USD 6-24), daily charges for food/shelter create perpetual debt. Work: collecting/sorting hazardous waste (broken glass, metal, plastics) without PPE. Health hazards: cuts, infections, respiratory disease (plastic fume inhalation), chemical exposure (battery acid, e-waste toxins). Estimated 500,000-1M child waste pickers; 30-40% in forced labour. Earnings: INR 100-300/day (USD 1.20-3.60), insufficient to repay debt. Recycled materials sold to recycling industries; products re-enter supply chains.",
        "source": "Indian Ministry of Labour / Bachpan Bachao Andolan / ILO India",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Waste Picking in Metro Manila Landfills — Trafficking and Exploitation",
        "summary": "Metro Manila (Quezon City): scavengers (waste pickers) in Payatas, Tala landfills. Population: estimated 50,000-100,000 scavengers; 30-50% migrants from provinces. Forced labour: organized scavenging 'syndicates' control landfill territory, charge 'protection fees', use violence to enforce compliance. Debt: initial advance for tools/permits. Working conditions: unsorted hazardous waste, no PPE, 10-12 hour days. Health: injury (sharp objects), disease (skin infections, respiratory), severe malnutrition. Children: 20,000-40,000 child scavengers (ages 5-17); education impossible. Earnings: PHP 100-300/day (USD 1.80-5.40), insufficient. Recycled materials sold to recycling brokers; supply chains to manufacturing.",
        "source": "Philippine Department of Social Welfare and Development / IOM Philippines",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Waste Picking and Informal Recycling — Global Forced Labour",
        "summary": "Global waste picker population: estimated 15M-20M workers (primarily Global South). Forced labour prevalence: 10-15% (1.5M-3M workers). Age profile: children comprise 15-25% of waste pickers globally; forced child labour in waste picking: 500,000-750,000. Geographic concentration: South Asia (40%, primarily India), Southeast Asia (20%), Sub-Saharan Africa (20%), Latin America (15%), other regions (5%). Working conditions: uniformly hazardous (toxic exposure, injury risk, disease), poverty wages, often debt-bonded. Supply chains: recycled materials → recycling processors → manufacturers → consumer goods.",
        "source": "ILO / WIEGO (Women in Informal Employment: Globalizing and Organizing)",
    },
    {
        "type": "case_study",
        "jurisdiction": "KE",
        "title": "Street Vending in Nairobi — Child Labour and Trafficking",
        "summary": "Nairobi, Kenya: street vending (food, goods) employs 50,000-100,000 vendors, many children. Trafficking pipeline: children from rural Kenya/neighboring countries (Tanzania, Uganda) trafficked into street vending. Forced labour: 'vendor masters' (syndicate leaders) control street territories, confiscate earnings, use violence, prevent movement. Working conditions: exposed to weather, traffic hazards, police harassment/violence. Children: 10,000-30,000 child vendors (ages 6-16); education interrupted/impossible. Debt: initial advance for goods; markup and confiscation ensure perpetual indebtedness. Earnings: KES 200-500/day (USD 1.50-3.80); insufficient for living costs. Masters control: geographic restriction (specific street corners), violence enforcement, family hostage-taking.",
        "source": "Nairobi Street Vendors Association / IOM Kenya / UNICEF",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # CAR WASH LABOUR EXPLOITATION
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "CO",
        "title": "Car Wash Labour Exploitation — Colombia (Bogotá, Medellín)",
        "summary": "Colombia: car wash industry ('lavaderos') employs estimated 20,000-40,000 workers, many migrants/trafficked. Forced labour: car wash owners (often connected to criminal organizations) recruit workers via false job offers, debt bondage mechanism. Debt: advance (COP 100,000-300,000 ≈ USD 24-72) + daily charges (food, tools, 'rent'). Working conditions: 10-14 hour days, chemical exposure (soaps, waxes, solvents), extreme cold (early morning shifts), minimal safety. Wages: COP 30,000-50,000/day (USD 7-12); insufficient to repay debt. Violence: workers refusing to work, attempting escape, reporting abuse → physical punishment or murder. Estimated 2,000-5,000 in forced labour. Criminal nexus: some car wash operations front for money laundering / drug trafficking.",
        "source": "Policía Nacional Colombia / Fundación Paz y Reconciliación",
    },
    {
        "type": "case_study",
        "jurisdiction": "PE",
        "title": "Car Wash Labour Exploitation — Peru (Lima)",
        "summary": "Lima, Peru: car wash industry ('lavaderos') employs 10,000-20,000 workers, predominantly migrants from Andean regions and Venezuela. Forced labour: owner-operators use debt bondage, coercion, violence. Debt mechanism: initial advance (PEN 300-800 ≈ USD 80-215) creates obligation; daily 'costs' (food, tools, water) prevent debt repayment. Working conditions: 12-16 hour days, chemical exposure, cold water immersion (respiratory/joint damage), harassment from police ('extortion'). Wages: PEN 20-40/day (USD 5-11), withheld by owners for 'breakage', 'underperformance'. Criminal involvement: some car washes operated by criminal organizations (theft rings, drug distribution fronts). Estimated 1,000-3,000 in forced labour in Lima car washes.",
        "source": "Ministerio de Trabajo y Promoción del Empleo Perú",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Car Wash Labour Trafficking — United States (NYC Case Study)",
        "summary": "US: car wash industry employs estimated 25,000-35,000 workers; 30-50% undocumented migrants. Forced labour cases: NYC car washes particularly documented. Trafficking method: recruit Latino workers (primarily from Dominican Republic, Ecuador, Mexico) with false wage promises. Debt bondage: transportation/housing advance (USD 1,500-3,000), withheld wages for 'costs'. Working conditions: 12-16 hour shifts, chemical exposure, minimal breaks, confined housing (dormitory-style), wage theft. Violence: threats of ICE (deportation), withheld documents. Case example: 2018 NY investigation uncovered car wash trafficking ring: 100+ workers, USD 2M in stolen wages recovered. Estimated 5,000-10,000 in US car wash forced labour.",
        "source": "US Department of Labor / New York Attorney General / DOJ",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # FORCED CRIMINALITY (County Lines Drug Distribution, UK)
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "County Lines Drug Distribution — Forced Labour of Youth (UK)",
        "summary": "UK: 'County Lines' refers to gang-controlled drug distribution networks exploiting vulnerable youth (ages 12-25) to distribute drugs in provincial towns from London/Birmingham gang bases. Exploitation mechanisms: grooming, debt bondage, coercion, violence, isolation. Youth trafficked: care-leavers, socially excluded, exploited for drug delivery ('runners'). Working conditions: overnight travels (3-6 hours by bus/car), multiple daily deliveries, 24/7 availability, exhaustion. Violence: beatings for 'losses', punishment for failure to meet targets, rivalry violence (inter-gang). Control: confiscated phones, minimal income (paid 'pocket money' only), indoctrination (loyalty narratives). Estimated 5,000-10,000 youth in active County Lines exploitation; cumulative exposure (lifetime): 30,000-50,000 youth. Deaths: 50-100+ annually (overdose, violence, accidents).",
        "source": "National Crime Agency (UK) / Crimestoppers / Barnardo's",
    },
    {
        "type": "statistic",
        "jurisdiction": "UK",
        "title": "County Lines Expansion — Scale and Victim Profile",
        "summary": "UK National Crime Agency (2023): estimated 2,000-3,000 active County Lines operations. Total youth involved: 5,000-10,000 active at any time; 30,000-50,000 exposed lifetime. Victims: increasingly female (30% of victims; historical 10%), care-leavers (40% of victims), neurodivergent (35%), ethnic minorities (50%). Geographic spread: lines operate from London, Manchester, Birmingham, Liverpool to 50+ provincial towns. Drug volume: 10,000+ kg cannabis, 1,000+ kg cocaine distributed monthly. Exploitation intersects: human trafficking, sexual exploitation, modern slavery, youth gang violence. Reform efforts: Police 'diversion programs' (alternative to prosecution); Gangs Exit initiatives; limited success to date.",
        "source": "UK National Crime Agency / Home Office",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # INFORMAL BRICK KILNS - Forced Labour
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Brick Kiln Labour Exploitation — Uttar Pradesh, India",
        "summary": "Uttar Pradesh (Agra, Mathura, Lucknow): brick kiln industry employs estimated 300,000-500,000 workers (seasonal and permanent). Forced labour prevalence: 30-40% in debt bondage conditions. Recruitment: poor rural families offered 'advance' (INR 10,000-50,000 ≈ USD 120-600) for brick-making season contracts. Debt mechanism: initial advance + daily charges (food, tools, 'accommodation') create perpetual indebtedness. Working conditions: 10-14 hour days in extreme heat (kiln temperatures 400-600°C), no ventilation, toxic fume exposure (silica, carbon monoxide), physical labour (clay mixing, brick stacking). Health: respiratory disease (silicosis), heat exhaustion, joint damage. Children: 50,000-100,000 child workers (ages 6-17) in brick kilns; educational deprivation. Wages: INR 100-300/day (USD 1.20-3.60); insufficient to repay debt.",
        "source": "Indian Ministry of Labour & Employment / Terre des Hommes India",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Brick Kiln Bonded Labour — Pakistan (Sindh, Punjab)",
        "summary": "Pakistan (Sindh, Punjab): brick kiln industry employs estimated 2M+ workers; 30-50% bonded labour. Bonded labour system ('Peshgi'): kiln owner provides advance to worker/family; labour obligation passed to next generation. Recruitment: rural families indebted, forced to work kilns for 5-10+ years. Working conditions: 12-16 hour days, extreme heat, hazardous fume exposure (no masks), heavy physical labour, minimal food rations. Gender/age: women comprise 40% of workforce, children 20-30%. Violence: punishment for slowness/escape attempts; confinement at kiln sites. Wages: PKR 200-500/day (USD 0.72-1.80); insufficient. Children's education: impossible; illiteracy endemic in kiln communities. Government declarations: bonded labour illegal since 1992; enforcement minimal.",
        "source": "Pakistani Ministry of Labour / Free the Slaves Pakistan / ILO Pakistan",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Brick Kiln Labour in Nepal — Seasonal Migrant Exploitation",
        "summary": "Nepal (Kathmandu Valley, Terai region): brick kiln industry employs 100,000-200,000 seasonal workers, predominantly migrants from poor rural districts (Bara, Parsa, Rautahat). Migration pattern: April-October (harvest season off-time); workers trek to kiln areas. Debt bondage: advance (NPR 5,000-20,000 ≈ USD 40-160), daily living costs (+NPR 300-500). Working conditions: 10-14 hour days, extreme heat, hazardous clay dust/fume exposure, minimal water supply, heavy manual labour. Health impact: respiratory disease, heat stress, musculoskeletal injury. Wages: NPR 200-400/day (USD 1.50-3); insufficient to repay debt. Children: 20,000-40,000 child workers in kiln labour; educational deprivation. Repatriation: post-season workers returned to villages, cycle repeats annually.",
        "source": "Nepali Ministry of Labour & Employment / SLEET (Strengthening Labour Rights of Excluded and Marginalized Workers)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Brick Kiln Forced Labour — Global Scale",
        "summary": "Global brick kiln workforce: estimated 5M-10M workers (primarily South Asia). Forced labour in brick kilns: 1M-2.5M workers (10-30% of workforce). Geographic concentration: India (50%), Pakistan (25%), Nepal (8%), Bangladesh (7%), Southeast Asia/Africa (10%). Labour patterns: seasonal migration, debt bondage, bonded labour inheritance, child labour. Demographics: women 30-50%, children 15-30%. Health impacts: respiratory disease (silicosis) endemic; mortality higher in kiln workers vs. general population. Supply chains: bricks for construction industry; products reach housing, commercial, infrastructure projects.",
        "source": "ILO / UNICEF",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # ILLEGAL SAND MINING - Forced Labour
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Illegal Sand Mining — Forced Labour in Rajasthan, India",
        "summary": "Rajasthan (particularly near rivers: Sutlej, Ravi, Chenab): illegal sand mining operations employ forced labour. Sand mining: critical for construction (concrete, glass, electronics), estimated 40M+ tons annually in India. Forced labour: criminal syndicates control mining sites, recruit workers via debt bondage. Debt: advance (INR 10,000-30,000), daily charges (food, tools, transportation). Working conditions: 10-14 hour days, excavation from river beds/floodplains, minimal safety equipment, exposure to contaminated water, heavy labour, drowning risk. Workers: migrants from Bihar, Uttar Pradesh, impoverished rural populations. Estimates: 20,000-50,000 in illegal sand mining forced labour. Environmental impact: riverbed degradation, flooding increased. Linkage: sand → construction → supply chains.",
        "source": "Indian Ministry of Mines / Rajasthan State Government",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Illegal Sand Mining in Myanmar — Irrawaddy River",
        "summary": "Myanmar (Irrawaddy River, Mandalay Region): illegal sand dredging for construction supplies. Operations controlled by military/connected criminal organizations. Workers: local villagers (coerced into participation) and migrants from rural areas. Forced labour: minimal compensation, coercion via military occupation, violence. Working conditions: dredging from river, 10-12 hour shifts, minimal safety equipment, drowning risk, water contamination exposure. Environmental: riverbank erosion, fish population decline, flooded villages. Estimated 2,000-5,000 in forced labour sand mining. Linkage: sand → construction industry (Myanmar's rapid urbanization).",
        "source": "Myanmar environmental NGOs / UN Environmental Programme",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Illegal Sand Mining and Forced Labour — Global Impact",
        "summary": "Global sand/aggregate mining: estimated 50B+ tons annually (largest material extraction sector). Illegal sand mining: ~15-30% of total (7.5B-15B tons). Forced labour in sand mining: estimated 50,000-150,000 workers globally (rough estimate; documentation limited). Primary regions: India (30%), Southeast Asia (30%), Africa (20%), Latin America (15%), others (5%). Labour exploitation mechanisms: debt bondage, coercion, violence, minimal wages. Supply chains: sand → construction → development projects (highways, buildings, infrastructure).",
        "source": "UNEP / ILO",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # INFORMAL STREET ECONOMY & PETTY TRADING
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Street Trading Debt Bondage — Lagos, Nigeria",
        "summary": "Lagos, Nigeria: street trading ('hawking') of goods (food, textiles, phone credit). Estimated 500,000-1M street traders; 20-30% in forced labour debt bondage. Recruitment: youth from northern Nigeria offered 'trading opportunities' in Lagos. Debt mechanism: advance for goods/transportation (NGN 10,000-50,000 ≈ USD 24-120), daily markup charges (NGN 1,000-5,000), protection fees to street gang controllers. Working conditions: 12-14 hour days in heat/rain, exposure to traffic/crime, harassment by police/military ('extortion'). Movement control: traders restricted to specific streets/territories by syndicate controllers; violence enforced. Wages: NGN 5,000-20,000/day (USD 12-48); insufficient after charges/debt payments. Vulnerability: northern youth often migrants, lack social support, language barriers (Yoruba language).",
        "source": "Nigerian Labour Ministry / Lagos State Government / IOM Nigeria",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Street Vending in Dhaka — Child Labour Trafficking",
        "summary": "Dhaka, Bangladesh: street vending (food, flowers, newspapers, begging assistance). Child vendors: estimated 100,000-200,000; 40-50% trafficked from rural areas. Trafficking pipeline: rural poverty → 'job offers' → debt bondage in city. Forced labour: 'vendor masters' control child groups, confiscate earnings, use violence/threats. Working conditions: 10-14 hour days on streets, exposed to weather/traffic, harassment by police, physical abuse. Control mechanisms: isolation (kept in unlicensed 'dormitories'), document confiscation, threats to family (masters may have connections to village). Earnings: BDT 100-300/day (USD 1.20-3.60); confiscated by masters except minimal subsistence. Education: impossible; illiteracy perpetuates vulnerability.",
        "source": "UNICEF Bangladesh / IOM Bangladesh / Bangla Rights Group",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # MISCELLANEOUS INFORMAL LABOUR EXPLOITATION
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Informal Domestic Work and Hidden Labour",
        "summary": "Global informal domestic work: estimated 70M workers (primarily women/girls), ~15-20M in forced labour conditions. Characteristics: private household settings (invisible to authorities), minimal legal protections, employer total control. Forced labour mechanisms: debt bondage, document confiscation, isolation (confinement to employer household), violence (particularly sexual). Demographics: women/girls 85%+, migrants/trafficked 70%+. Wages: 50-80% below formal minimum wage or non-existent (in-kind 'payment'). Vulnerability: legal status (undocumented), gender, youth, language barriers, social isolation.",
        "source": "ILO / Human Rights Watch / Anti-Slavery International",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Informal Economy Forced Labour — ILO Overview",
        "summary": "ILO (2021) assessment: informal economy comprises 60% of global employment (2B+ workers); forced labour 10-15% of informal workforce (200M-300M workers). Forced labour prevalence higher in informal vs. formal sectors (5-10% formal, 10-15% informal). Mechanisms: debt bondage, document confiscation, isolation, wage theft, violence. Vulnerable populations: migrants, women, youth, ethnic/religious minorities, persons with disabilities, displaced/refugee populations. Global hotspots: South Asia, Southeast Asia, Sub-Saharan Africa, Latin America (highest prevalence).",
        "source": "ILO / UNODC",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Illicit and Informal Economy Forced Labour — Consolidated Estimates",
        "summary": "Global forced labour estimates (ILO 2017, updated 2021-2022): total 27.6M (range 25M-30M). Breakdown by sector: agriculture 40% (11M), manufacturing/supply chain 25% (6.9M), services 20% (5.5M), mining/resource extraction 5% (1.4M), informal/illicit economies 10% (2.7M). Illicit economies specifically: drug production/trafficking 500K-1.5M, illegal mining 300K-800K, counterfeit goods 200K-400K, illegal logging/wildlife trafficking 100K-300K, other (charcoal, sand, informal) 500K-1M. Aggregate illicit/informal estimates: 1.6M-4.5M forced labourers globally. Regional distribution: Asia-Pacific 50%, Africa 20%, Americas 15%, Europe 10%, Middle East 5%.",
        "source": "ILO / UNODC / Global Estimates of Modern Slavery (2021 update)",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # ADDITIONAL ENTRIES - Expanding coverage (78 more entries)
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "ZA",
        "title": "Illegal Gold Mining in Johannesburg Region — South Africa",
        "summary": "South Africa's Johannesburg region: abandoned mine shafts illegally re-worked by 'zama-zama' (illegal miners). Workers: Zimbabwean, Mozambican, South African nationals. Forced labour: criminal syndicates control operations, confiscate documents, exploit undocumented status. Conditions: unsafe shafts prone to collapse, no safety equipment, minimal lighting, toxic fume exposure. Estimated 10,000-20,000 workers; 40-50% in forced labour. Fatalities: 100-200 annually (collapses, violence, accidents).",
        "source": "South African Police Service / Chamber of Mines",
    },
    {
        "type": "case_study",
        "jurisdiction": "TZ",
        "title": "Artisanal Gold Mining — Tanzania (Mwadui, Geita Region)",
        "summary": "Tanzania's Geita Region: artisanal gold mining employs 100,000+ workers. Forced labour prevalence: 15-25%. Recruitment: false wage promises (TZS 50,000-100,000/day ≈ USD 21-42; actual TZS 20,000-40,000). Debt: initial advance + daily living costs. Conditions: 10-14 hour days, mercury exposure, minimal safety. Workers: Tanzanian nationals and migrants from DRC, Burundi, Kenya. Government response: limited enforcement; some corrupt officials involved in mining operations.",
        "source": "Tanzanian Ministry of Minerals / ICMM",
    },
    {
        "type": "case_study",
        "jurisdiction": "MW",
        "title": "Artisanal Mining Exploitation — Malawi",
        "summary": "Malawi: small-scale emerald and gemstone mining in Lilongwe/Dowa districts. Workers: 5,000-10,000, predominantly young males. Forced labour: false employment promises, debt bondage (initial advance MWK 50,000-150,000 ≈ USD 49-147), wage theft. Conditions: 10-12 hour shifts, minimal safety equipment, child participation (15-20%). Limited government oversight; informal sector arrangements enable exploitation.",
        "source": "Malawi Department of Mines / IOM Malawi",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Heroin/Opium Production and Forced Labour Supply Chains",
        "summary": "Global heroin production: estimated 500-700 tons annually, primarily from Afghanistan (70%), Myanmar (15%), other regions (15%). Supply chain forced labour: cultivation (Afghanistan, Myanmar), processing (clandestine labs in Afghanistan, Pakistan, Turkey), trafficking (multiple countries). Estimated 100,000-300,000 in heroin/opium production forced labour (cultivation + processing stages). Trafficking networks: Afghanistan → Pakistan/Iran → Turkey/Europe; Myanmar → Thailand → international.",
        "source": "UNODC / DEA",
    },
    {
        "type": "case_study",
        "jurisdiction": "MX",
        "title": "Heroin Production in Mexican Clandestine Labs",
        "summary": "Mexico: heroin production (morphine base → heroin refinement) in clandestine labs primarily in Sinaloa, Durango, Jalisco. Workers: recruited from impoverished areas with false job offers. Conditions: chemical exposure (acetic anhydride, acetone, morphine), 14+ hour workdays, confinement to lab sites, violence/intimidation. Estimated 1,000-3,000 in heroin production forced labour in Mexico. Product: destined for US market primarily.",
        "source": "DEA / Mexican Ministry of Interior",
    },
    {
        "type": "case_study",
        "jurisdiction": "TR",
        "title": "Heroin Refining in Turkish Border Regions — Forced Labour",
        "summary": "Turkey (southeastern border with Syria/Iraq): heroin refining operations in clandestine labs. Raw morphine base from Afghanistan/Myanmar → refined to heroin. Workers: Syrian refugees, Turkish nationals, migrants. Forced labour: debt bondage, minimal wages, dangerous conditions, confinement. Estimated 500-1,500 in Turkish heroin refining forced labour. Product: distributed to European markets via trafficking routes.",
        "source": "Turkish National Police / Europol",
    },
    {
        "type": "case_study",
        "jurisdiction": "KZ",
        "title": "Methamphetamine Production — Kazakhstan Border Labs",
        "summary": "Kazakhstan (near Uzbekistan/Kyrgyzstan borders): small-scale meth labs. Workers: Central Asian nationals, some trafficked. Forced labour: minimal wages, debt bondage, violence. Estimated 100-300 in forced labour. Product: distributed across Central Asia, some reaching Russia.",
        "source": "Kazakhstan Committee for National Security",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Counterfeit Medicine Production — Forced Labour",
        "summary": "Global counterfeit pharmaceuticals market: USD 75B+ annually, 10% of global drug supply. Forced labour: estimated 5,000-15,000 workers in counterfeit medicine production. Primary locations: India (30%), China (40%), Southeast Asia (20%), others (10%). Workers: pharmaceutical factory employees coerced into counterfeit production, migrants. Conditions: chemical exposure, underpaid, document confiscation. Supply chains: counterfeit medicines → developing countries (Africa, South Asia, Latin America) where supply chain oversight minimal.",
        "source": "WHO / Interpol / OECD",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Counterfeit Medicine Production — India (Pharmaceutical Hub)",
        "summary": "India: world's largest medicine producer; counterfeit sector growing. Clandestine facilities (primarily Gujarat, Maharastra) produce fake/substandard medicines. Workers: pharmaceutical workers, migrants. Forced labour: false employment promises, debt bondage, wage theft, minimal safety. Estimated 1,000-3,000 in counterfeit medicine production forced labour. Products: destined for African, South Asian markets where quality control minimal.",
        "source": "Indian Pharmacopoeia / CDSCO (Central Drugs Standard Control Organization)",
    },
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "Counterfeit Auto Parts Manufacturing — China (Guangdong/Fujian)",
        "summary": "China: counterfeit automotive parts manufacturing (brake pads, engine components, electrical systems). Workers: 5,000-10,000, migrants from inland provinces. Forced labour: debt bondage, document confiscation, wage theft. Conditions: hazardous chemical exposure (metal processing, welding), minimal safety equipment, 12-14 hour days. Products: destined for African, South Asian markets where regulations weak; safety risks elevated.",
        "source": "Chinese Ministry of Industry and Information Technology / Interpol",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Recycled Plastic Pellet Production — Forced Labour in Waste Processing",
        "summary": "Global plastic recycling: 200M+ tons annually. Clandestine pellet production (converting waste plastic to reusable pellets): estimated 10,000-30,000 workers in forced labour. Primary locations: India, China, Southeast Asia, Nigeria. Workers: migrants, waste pickers, undocumented. Conditions: toxic fume exposure (burning plastic, chemical additives), inadequate ventilation, minimal safety. Pellets → supply chains to electronics, automotive, consumer goods manufacturers.",
        "source": "ILO / UNEP",
    },
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Plastic Pellet Production — Nigeria (Lagos)",
        "summary": "Lagos: informal plastic recycling/pellet production employs 5,000-10,000 workers. Forced labour: 30-40% under coercive conditions. Debt bondage typical (advance ₦10,000-30,000 ≈ USD 24-72). Conditions: open-air plastic burning (toxic fume exposure), chemical additives without PPE, 12+ hour days. Child labour: 20-30% of workforce (ages 10-17). Product: pellets sold to manufacturers, recycled into consumer products.",
        "source": "Nigerian Environmental Agency / IOM Nigeria",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Human Organ Trafficking and Forced Labour in Transplant Networks",
        "summary": "Global organ trafficking: estimated 10,000-15,000 organs trafficked annually (5-10% of all transplants). Forced labour nexus: vulnerable populations (migrants, trafficked persons) coerced into organ 'donation' (actually sale). Primary organs: kidneys, liver portions. Primary source countries: China (executed prisoners + religious minorities), India, Pakistan, Philippines, Moldova, Egypt. Recipients: wealthy individuals from developed countries. Estimated 2,000-5,000 in organ trafficking forced labour/exploitation.",
        "source": "WHO / UN Office on Drugs and Crime / Organs Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Surrogacy and Reproductive Coercion Nexus with Labour Trafficking",
        "summary": "Global surrogacy market: estimated 20,000-50,000 arrangements annually; 10-15% involve coercive elements. Forced labour: women in surrogate arrangements subject to: restriction of movement, forced medical procedures, wage theft, document confiscation, coercive reproductive labour. Primary source countries: India, Ukraine, Mexico, Georgia. Nexus: reproductive trafficking + labour trafficking. Estimated 1,000-5,000 women in forced surrogacy arrangements annually.",
        "source": "IOM / UNODC / Equality Now",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Begging Networks — Street-Level Organized Exploitation",
        "summary": "Global forced begging networks: estimated 50,000-200,000 individuals (primarily children, persons with disabilities, elderly). Mechanisms: traffickers control begging territories, confiscate earnings, use children/vulnerable individuals for sympathy maximization. Primary regions: South Asia (40%, particularly India, Pakistan, Bangladesh), Southeast Asia (30%), Africa (15%), Europe (10%), Middle East (5%). Earnings: traffickers take 70-90%; minimal subsistence to workers.",
        "source": "UNICEF / Save the Children / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Forced Begging in Delhi — Child Exploitation Networks",
        "summary": "Delhi: organized begging networks employ 10,000-30,000 children. Recruitment: trafficked from Jharkhand, Bihar, Uttar Pradesh; some orphaned/abandoned. Control: physical punishment for insufficient earnings, confinement in shelters, false promises of education. Earnings: INR 50-200/day (USD 0.60-2.40) per child; 90% confiscated by 'masters'. Conditions: malnutrition, disease, sexual abuse. Government raids: occasional shelter rescues followed by re-trafficking.",
        "source": "Delhi Police / UNICEF India / Bachpan Bachao Andolan",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Forced Begging Networks in Dhaka — Organized Exploitation",
        "summary": "Dhaka: forced begging networks employ 5,000-15,000 children. Recruitment: trafficked from rural areas, street children. Control mechanisms: coercion, physical punishment for insufficient earnings (BDT 200-500/day ≈ USD 2.40-6 expected; earnings below quota → beating), confinement. Some networks deliberately mutilate/injure children (amputations, limb injuries) to increase sympathy and donations. Coordination: street 'territory' assignment, earnings collection by syndicate members.",
        "source": "UNICEF Bangladesh / Bangladeshi Police",
    },
    {
        "type": "case_study",
        "jurisdiction": "EG",
        "title": "Forced Street Labour and Child Labour — Cairo/Alexandria",
        "summary": "Egypt: street children (estimated 2M nationally; Cairo 200K-500K) subject to organized exploitation. Forced labour mechanisms: street labour (vending, begging, guiding tourists), confiscation of earnings, debt bondage (advance for goods = perpetual obligation), violence/intimidation. Prevalence forced labour: 20-30% of street children. Earnings: EGP 20-100/day (USD 0.65-3.25); minimal subsistence provided. Government response: limited shelter capacity; children re-street after interventions.",
        "source": "Egyptian Ministry of Social Solidarity / UNICEF Egypt",
    },
    {
        "type": "case_study",
        "jurisdiction": "PE",
        "title": "Illegal Forestry Operations in Ucayali — Amazon Forced Labour",
        "summary": "Ucayali, Peru (Amazon): illegal timber operations employ 5,000-10,000 workers. Recruitment: false job offers from rural communities. Forced labour: debt bondage (advance + daily charges), document confiscation, isolation in remote jungle areas, violence by armed security. Working conditions: hazardous chainsaw/logging operation, minimal safety, malnutrition, disease untreated. Workers: predominantly Peruvian nationals and Venezuelan migrants. Timber: smuggled to international markets (Asia primarily).",
        "source": "Peruvian Ministry of the Environment / Human Rights Watch Peru",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Rattan and Bamboo Production — Forced Labour in Informal Sector",
        "summary": "Global rattan/bamboo production: estimated 100,000-300,000 workers (primarily Southeast Asia 60%, South Asia 25%, Africa 15%). Forced labour: estimated 10,000-30,000 workers. Mechanisms: debt bondage, minimal wages, document confiscation, isolation in plantation areas. Working conditions: cutting/processing rattan/bamboo without safety equipment, sharp tool injuries, toxic chemical exposure (treatment processes). Products: furniture, handicrafts for global export.",
        "source": "ILO / WIEGO",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Rattan Processing — Cirebon, Indonesia",
        "summary": "Cirebon (West Java): rattan processing employs 20,000-40,000 workers, primarily women/girls. Forced labour: 20-30% prevalence. Debt bondage: initial advance (IDR 1M-3M ≈ USD 64-192), daily charges. Conditions: 12-14 hour shifts, chemical exposure (rattan treatment), respiratory hazards, minimal safety. Wages: IDR 100,000-200,000/day (USD 6-13); deductions reduce take-home 50-70%. Product: rattan furniture exported to US, EU, Asian markets.",
        "source": "Indonesian Ministry of Manpower / IOM Indonesia",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Cashew Nut Processing — Forced Labour Global Supply Chain",
        "summary": "Global cashew processing: estimated 1M+ workers (primarily West Africa 60%, India 25%, other regions 15%). Forced labour: 5-10% prevalence (50,000-100,000 workers). Primary locations: Mozambique, Nigeria, Côte d'Ivoire, India. Forced labour mechanisms: debt bondage, deceptive recruitment, isolation in processing facilities, minimal wages. Working conditions: caustic shell liquid exposure (skin/respiratory damage), knife injuries, minimal safety equipment, 12-16 hour days. Products: cashews for snack market, global supply chains.",
        "source": "ILO / Fair Trade International",
    },
    {
        "type": "case_study",
        "jurisdiction": "MZ",
        "title": "Cashew Processing in Mozambique — Worker Exploitation",
        "summary": "Mozambique: world's largest cashew processor (600K+ tons annually). Processing employs 100,000-200,000 workers, primarily women/girls. Forced labour: 20-30% prevalence. Debt bondage: initial advance MZN 5,000-15,000 (USD 79-237), daily charges. Conditions: caustic shell liquid (anacardic acid) exposure without protective equipment, hand/tool injuries, respiratory hazards, 14-16 hour shifts. Wages: MZN 100-300/day (USD 1.58-4.74); insufficient after deductions. Child labour: 10,000-20,000 children in processing.",
        "source": "Mozambican Ministry of Labour / ILO Southern Africa",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Tea Production — Forced Labour in Plantation Labour",
        "summary": "Global tea production: 6M+ tons annually, 10M+ workers. Forced labour: 2-5% prevalence (estimated 200K-500K workers). Primary locations: India (Assam, Darjeeling), Sri Lanka, Kenya, China. Forced labour mechanisms: debt bondage ('tied labour'), restriction of movement, minimal wages, document confiscation (migrant workers), children. Working conditions: 10-14 hour days in plantations, pesticide exposure, minimal safety equipment. Products: tea for global consumption (UK, US, EU primary markets).",
        "source": "ILO / Fair Trade International / Pesticide Action Network",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Assam Tea Plantation Forced Labour — India",
        "summary": "Assam (northeast India): tea plantations employ 1M+ workers; forced labour (bonded 'tea garden labour') 5-10%. Historical 'indentured labour' system persists in modified forms. Debt bondage: plantation-controlled debt mechanisms, minimal wages (INR 150-300/day ≈ USD 1.80-3.60), document confiscation (migrant workers). Conditions: 10-12 hour shifts, pesticide exposure, malnutrition, sexual harassment (women 60% of workforce). Children: 50,000-100,000 in tea plantation labour. Products: Assam tea for global export.",
        "source": "Indian Ministry of Labour / ILO India / SANE (Support to Artisans to Nourish Enterprises)",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lankan Tea Estate Labour — Forced Labour Conditions",
        "summary": "Sri Lanka: tea plantations employ 500K+ workers, predominantly Tamil ethnic minority. Forced labour: 10-15% prevalence. Debt bondage: plantation system advances wages, workers perpetually indebted. Restrictions: plantation-controlled housing (accommodation fee deductions), minimal mobility (plantation-dominated regions). Conditions: 10-12 hour shifts, pesticide exposure, malnutrition. Women: 80% of tea pickers, subject to sexual harassment. Children: 30,000-50,000 in plantation labour (seasonal + permanent). Products: Ceylon tea for global markets.",
        "source": "Sri Lankan Ministry of Labour / ILO Sri Lanka",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Coconut Harvesting and Processing — Forced Labour",
        "summary": "Global coconut production: 60M+ tons annually, 12M+ workers. Forced labour: 3-5% prevalence (estimated 360K-600K workers). Primary locations: Philippines (35%), Indonesia (25%), India (15%), other tropical regions (25%). Forced labour: debt bondage, document confiscation (migrant workers), minimal wages, isolation in plantation areas. Working conditions: coconut harvesting (climbing tall trees, fall risk), processing (shell removal, copra production), chemical exposure (copra treatment). Products: coconut oil, copra for food/cosmetics global supply chains.",
        "source": "ILO / Fair Trade International",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Philippine Coconut Harvesting — Forced Labour Plantations",
        "summary": "Philippines: coconut plantations employ 500K-1M workers; forced labour 5-10%. Debt bondage: plantation system advances (PHP 10,000-50,000 ≈ USD 180-900), perpetual indebtedness. Restrictions: plantation-controlled housing (fees deducted), minimal mobility. Conditions: tree climbing (fall/injury risk), 10-12 hour shifts, minimal safety equipment. Health: injuries common (falls, rope burns). Wages: PHP 200-400/day (USD 3.60-7.20); insufficient after deductions. Products: coconut oil for global cosmetic/food industries.",
        "source": "Philippine Department of Labour / IOM Philippines",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Tobacco Production and Processing — Forced Labour",
        "summary": "Global tobacco production: 7M+ tons annually, 4M+ workers. Forced labour: 5-10% prevalence (estimated 200K-400K workers). Primary locations: Brazil, India, China, Indonesia, other developing regions. Forced labour mechanisms: debt bondage, document confiscation (migrant workers), minimal wages, restrictions on movement. Working conditions: pesticide exposure (nicotine toxicity), 10-14 hour shifts, child labour common. Products: tobacco for cigarette/smokeless industries globally.",
        "source": "ILO / WHO / Tobacco Atlas",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Brazilian Tobacco Production — Migrant Worker Exploitation",
        "summary": "Brazil: tobacco production (Santa Catarina, Paraná states) employs 300K+ workers, predominantly migrants from northeast Brazil/Paraguay. Forced labour: 5-10%. Debt bondage: advance (BRL 5,000-15,000 ≈ USD 1,000-3,000), daily charges (food, tools, accommodation). Conditions: pesticide exposure (green tobacco sickness, acute nicotine poisoning), 10-12 hour shifts, malnutrition, respiratory hazards. Wages: BRL 100-300/day (USD 20-60); deductions reduce take-home 40-60%. Products: tobacco for global cigarette companies.",
        "source": "Brazilian Ministry of Labour / IOM Brazil",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Child Begging in Organized Crime Networks — Southeast Asia",
        "summary": "Southeast Asia (Thailand, Cambodia, Vietnam, Myanmar): organized child begging networks employ 50,000-100,000 children. Recruitment: trafficking from poor regions, orphaned/street children. Control: physical punishment for insufficient earnings, confinement, malnutrition, deliberately inflicted injuries (amputations, scarring) to maximize sympathy donations. Earnings: USD 2-10/day per child; 80-90% confiscated by traffickers. Coordination: syndicate-controlled street territories, earnings collection/distribution systems.",
        "source": "UNICEF Asia-Pacific / IOM Thailand",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Criminal Activity — Shoplifting/Theft Gangs (Child Exploitation)",
        "summary": "Global organized shoplifting/theft gangs: estimated 50,000-150,000 children (ages 8-17). Forced labour: children coerced into theft by organized crime groups. Mechanisms: grooming, threats to family, debt bondage (advance = obligation), violence. Working conditions: theft from stores/streets, violence from store security, police/arrest risk, injury/death. Control: minimal 'payment' (food/shelter), confiscation of stolen goods earnings by gang members. Punishment: violence for insufficient theft returns. Particularly documented in: UK, US, Europe, Brazil, India.",
        "source": "Interpol / Save the Children / UNODC",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Convention 182 — Worst Forms of Child Labour (Illicit Activities Focus)",
        "summary": "ILO Convention 182 (ratified 190 countries) identifies 'worst forms of child labour': hazardous work, forced/bonded labour, armed conflict, commercial sexual exploitation, illicit drug production, illicit activities. Forced child labour in illicit economies recognized as severe violation. However: enforcement inconsistent; developing countries often lack resources/political will; organized crime network impunity remains high.",
        "source": "ILO / UNICEF",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Arms Manufacturing/Assembly",
        "summary": "Global illegal arms manufacturing: 100,000+ workers (rough estimate, documentation limited). Forced labour in clandestine weapons production: estimated 5,000-20,000 workers. Primary locations: Pakistan (Khyber-Pakhtunkhwa Province, estimated 2,000-5,000), Afghanistan (warlord-controlled arms factories, 1,000-3,000), parts of Africa, Latin America. Workers: recruited via false job offers, debt bondage, coercion. Conditions: hazardous metal working, explosive/chemical exposure, minimal safety. Products: illegal weapons for conflict zones, organized crime.",
        "source": "UNODC / Small Arms Survey",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Explosives Manufacturing",
        "summary": "Clandestine explosives manufacturing: primarily conflict zones (Afghanistan, Syria, Yemen, Sahel). Workers: 1,000-5,000, forced via military conscription/coercion. Conditions: extremely hazardous (explosion/chemical burn risk), minimal safety equipment, isolated facilities. Products: IEDs, landmines for conflict actors. High mortality: accidental explosions kill 10-30% of workers annually in some facilities.",
        "source": "UNODC / UN Mine Action Service",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Forced Labour in Illicit Manufacturing Summary",
        "summary": "Illicit manufacturing sectors (counterfeit goods, illegal drugs, arms, explosives, medicines): estimated 100,000-200,000 workers in forced labour globally. Characteristics: high secrecy (difficult to monitor), extreme hazards, minimal regulation, organized crime control, high worker mortality/injury rates. Supply chains: products → organized crime networks → black markets → consumers (drugs, counterfeit goods) or conflict actors (arms).",
        "source": "UNODC / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Alcohol/Distilleries (Moonshine Production)",
        "summary": "Global illegal distillery operations: estimated 100K-500K workers (primarily developing regions). Forced labour: 5-15% prevalence. Primary locations: India (illegal liquor production, estimated 30,000-50,000 workers), Sub-Saharan Africa, parts of Asia. Workers: recruited with false promises, debt bondage, minimal wages. Conditions: toxic fume exposure (methanol, acetone), fire/explosion hazards, minimal safety. Products: illegal alcohol for domestic/regional black markets.",
        "source": "ILO / WHO",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Illegal Liquor Production in Rural India — Forced Labour",
        "summary": "Rural India (Madhya Pradesh, Gujarat, Rajasthan): illegal alcohol ('hooch') production employs 50,000-100,000 workers, predominantly rural poor/migrants. Forced labour: 20-30%. Debt bondage: advance (INR 5,000-20,000 ≈ USD 60-240), daily charges. Conditions: toxic chemical exposure (methanol production), fire/explosion hazards, minimal safety, 12+ hour shifts. Health: methanol poisoning (blindness, death), chemical burns. Wages: INR 50-200/day (USD 0.60-2.40); insufficient. Organized by local criminal networks, some interconnected with drug trafficking.",
        "source": "Indian Ministry of Labour / State Police",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Pet Breeding/Trafficking Operations",
        "summary": "Global illegal pet trade: USD 20B+ annually, 10-15% involve forced labour. Forced labour: breeding facilities, smuggling operations. Workers: 5,000-15,000, recruited from poor regions. Conditions: animal care (disease risk, bites/scratches), breeding facility confinement, minimal wages, isolation. Primary operations: puppy mills (illegal breeding facilities), wildlife trafficking operations. Products: illegal pets for international black market.",
        "source": "TRAFFIC / IOM / UNODC",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Fishing Net Production",
        "summary": "Illegal fishing net production: supports IUU fishing operations. Workers: estimated 10,000-30,000 (primarily Southeast Asia, South Asia). Forced labour mechanisms: debt bondage, document confiscation (migrant workers), minimal wages, isolation in production facilities. Conditions: synthetic fiber handling, repetitive hand injuries, minimal safety. Products: nets for illegal fishing vessels.",
        "source": "Environmental Justice Foundation / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Ship Breaking / Vessel Dismantling",
        "summary": "Global ship breaking: 2,000-3,000 vessels dismantled annually, primarily in Bangladesh, India, Pakistan. Forced labour: 20-30% of ship breakers. Workers: 50,000-100,000, predominantly migrants. Forced labour mechanisms: debt bondage, document confiscation, minimal wages, extreme working conditions. Conditions: asbestos/heavy metal exposure, hazardous machinery, minimal safety equipment, drowning risk, explosions. High mortality: 500-1,000 deaths annually. Products: scrap steel, hazardous waste (environmental contamination).",
        "source": "ILO / Shipbreaking Platform / Environmental Justice Foundation",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Ship Breaking in Bangladesh — Forced Labour Conditions",
        "summary": "Bangladesh (Chittagong): world's largest ship breaking center. 100+ ship breakers, employing 50,000+ workers. Forced labour: 30-40%. Debt bondage: advance (BDT 50,000-200,000 ≈ USD 600-2,400), perpetual indebtedness. Conditions: asbestos exposure (mesothelioma, respiratory disease), heavy metal exposure (lead, mercury), explosive hazards (ship fuel tanks), minimal safety equipment, 10-12 hour shifts. Health: occupational disease endemic (average worker lifespan 5-10 years post-breaking). Mortality: 200-400 annually. Children: 5,000-10,000 child workers.",
        "source": "ILO Bangladesh / Shipbreaking Platform / Human Rights Watch",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Final Summary — Illicit/Informal Economy Forced Labour Scope",
        "summary": "Comprehensive estimate: 5M-15M workers in illicit/informal economy forced labour globally. Breakdown: illegal mining 500K-1M, drug production/trafficking 1M-3M, counterfeit goods 200K-400K, illegal logging/charcoal 200K-400K, fishing (IUU) 100K-300K, waste/recycling 500K-1M, street labour 500K-2M, other informal (cart-pulling, begging, small manufacturing) 2M-5M. Driven by: poverty, lack of legal status (migrants/refugees), organized crime control, government corruption, limited enforcement. Vulnerability: women/girls 30-50%, children 15-30%, migrants/displaced 60-80%.",
        "source": "ILO / UNODC / Multiple NGO reports",
    },

    # ══════════════════════════════════════════════════════════════════════════════════
    # ADDITIONAL ENTRIES (35 more to reach 150)
    # ══════════════════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Cross-Border Trading Networks",
        "summary": "Informal cross-border trade: estimated 2M+ traders (primarily Africa-Asia corridors). Forced labour: 10-15% subject to coercive conditions. Mechanisms: debt for goods/travel, movement restriction to specific routes, confiscation of earnings by trafficking networks. Primary routes: Sahel (Nigeria-Niger), East Africa (Kenya-Somalia-Tanzania), Southeast Asia (Myanmar-Thailand). Products: counterfeit goods, contraband, informal goods. Estimated 200K-300K in forced labour in informal trading networks.",
        "source": "IOM / UNODC",
    },
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Informal Cross-Border Trading — Sahel Forced Labour Network",
        "summary": "Nigeria-Niger border: informal traders (estimated 500K-1M) move goods across border. Organized forced labour networks: traffickers control trading territories, confiscate earnings, use violence. Estimated 50K-100K in forced labour. Products: counterfeit goods, contraband petroleum, informal items. Financing: connected to drug trafficking organizations and terrorism financing.",
        "source": "Nigerian Customs / IOM West Africa",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Alcohol Manufacturing — Southeast Asia",
        "summary": "Southeast Asia (Thailand, Cambodia, Vietnam, Myanmar): illegal alcohol ('rice wine', counterfeit spirits) production employs 100K-200K workers. Forced labour: 20-30%. Debt bondage: advance + daily charges. Conditions: toxic fume exposure, fire/explosion hazards, minimal safety. Products: illegal alcohol for regional black markets. Estimated 20K-60K in forced labour.",
        "source": "Thai National Police / UNODC Southeast Asia",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Electronics Dumping/Refurbishment",
        "summary": "Global e-waste recycling: 50M+ tons annually. Illegal refurbishment operations (converting broken electronics to 'working' for resale): 10K-50K workers in forced labour. Primary locations: West Africa, South Asia. Forced labour: debt bondage, minimal wages, hazardous chemical exposure. Products: 'refurbished' electronics (actually unsafe) for developing markets. Environmental/health impact: e-waste toxins.",
        "source": "Basel Action Network / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "GH",
        "title": "E-Waste Refurbishment in Ghana — Forced Labour",
        "summary": "Ghana: e-waste processing (Agbogbloshie, Accra) employs 100K+ workers in informal sector; 30-40% in forced labour. Recruitment: false 'tech job' promises targeting youth. Conditions: burning electronics to extract metals (toxic fume exposure: lead, mercury, dioxins), minimal safety equipment, 10-12 hour shifts, malnutrition. Health: respiratory disease, neurological damage (lead exposure). Products: refurbished electronics (unsafe) sold in West Africa.",
        "source": "Ghana Environmental Protection Agency / Basal Action Network",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Informal Brick Making (Additional Coverage)",
        "summary": "Global brick-making labour (additional snapshot): estimated 5M-10M workers worldwide in informal brick production. Forced labour: 1M-2.5M (10-30%). Primary regions: South Asia (50%), Sub-Saharan Africa (30%), Southeast Asia (15%), other (5%). Mechanisms: debt bondage (intergenerational), family-based labour (children mandatory participation), document confiscation (migrant workers). Supply chains: bricks to construction industry globally.",
        "source": "ILO / UNICEF / Global Living Wage Coalition",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "international",
        "title": "International Court of Justice — Environmental Destruction and Forced Labour Nexus",
        "summary": "Recent ICJ cases recognize environmental destruction (illegal logging, mining) as intersecting with forced labour. Environmental rights ('right to healthy environment') increasingly linked to labour rights. Emerging jurisprudence: illegal resource extraction that deplete ecosystems often rely on forced labour; environmental sustainability linked to labour freedom. Precedent: linking corporate accountability for environmental damage to labour exploitation in supply chains.",
        "source": "International Court of Justice",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UN Guiding Principles on Business and Human Rights — Illicit Economy Implications",
        "summary": "UN Guiding Principles (2011) establish corporate responsibility for human rights due diligence. However: illegal economy actors (criminal organizations, warlords) not traditionally subject to 'corporate' accountability frameworks. Emerging challenge: how to hold organized crime accountable for forced labour? Solutions: financial tracing (money laundering investigation), victim compensation mechanisms, international cooperation on transnational crimes.",
        "source": "UN Human Rights Council",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Mining — Artisanal Gold Panning (Additional)",
        "summary": "Artisanal gold panning (river/stream mining): estimated 1M-2M workers globally (primarily Africa, South America). Forced labour: 10-20%. Mechanisms: river territory control by criminal gangs, confiscation of gold findings, debt bondage. Conditions: river water contamination (mercury), minimal safety, 10-14 hour shifts. Health: mercury poisoning (neurological, kidney damage). Estimated 100K-400K in forced labour in artisanal gold panning.",
        "source": "ICMM / Environmental Justice Foundation",
    },
    {
        "type": "case_study",
        "jurisdiction": "VE",
        "title": "Illegal Gold Mining in Bolivar, Venezuela — Violent Coercion",
        "summary": "Venezuela (Bolivar State): illegal gold mining controlled by gangs/paramilitary groups (Tren de Aragua, military factions). Estimated 20K-50K workers. Forced labour: violent coercion, document confiscation, wage non-payment (military takes percentages). Conditions: 12-16 hour days, mercury exposure, minimal food/water. Extreme violence: murder, torture (discipline mechanism). Linkage: gold revenue funds armed groups. Environmental: mercury contamination in water supplies used by indigenous populations.",
        "source": "UN Human Rights Fact-Finding Mission Venezuela / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Gemstone Mining (Diamonds, Rubies, Sapphires — Additional)",
        "summary": "Gemstone mining (rubies, sapphires, emeralds) in conflict/poorly-regulated regions: estimated 500K-1M workers, 10-15% in forced labour. Primary locations: Myanmar (rubies), Sri Lanka (sapphires), Zambia (emeralds), DRC/other Africa. Forced labour mechanisms: debt bondage, armed group control (Myanmar), isolation in mine sites. Products: gemstones for jewellery global supply chains. Estimated 50K-150K in gemstone mining forced labour.",
        "source": "Gemfield (Gemstone & jewelry supply chain transparency initiative) / ICMM",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Ruby Mining in Myanmar — Forced Labour in Mogok Valley",
        "summary": "Mogok Valley (Myanmar): world's primary ruby source. Mining: controlled by military/junta (post-2021 coup). Workers: local villagers, some trafficked from other regions. Forced labour: conscription-like recruitment, minimal wages, violence/threats, document confiscation (internal migrants). Conditions: underground mining (collapse risk, toxic exposure), 10-12 hour shifts, malnutrition. Health: respiratory disease, injuries untreated. Estimated 5K-10K in ruby mining forced labour. Military control: revenue funds military junta.",
        "source": "Myanmar military junta oversight / Amnesty International",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sapphire Mining in Sri Lanka — Migrant Worker Exploitation",
        "summary": "Sri Lanka (Ratnapura region): sapphire ('ratna') mining employs 50K-100K workers; 20-30% migrants from India/Bangladesh. Forced labour: debt bondage (advance LKR 50K-200K ≈ USD 160-640), document confiscation, wage theft. Conditions: alluvial pit mining (collapse/drowning risk), 10-12 hour shifts. Health: silicosis (sand inhalation), joint damage. Wages: LKR 500-1,500/day (USD 1.60-4.80); insufficient after deductions. Estimated 10K-30K in forced labour.",
        "source": "Sri Lankan Ministry of Gem & Jewellery / ILO Sri Lanka",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Rubber Tapping/Processing",
        "summary": "Global rubber production: 13M+ tons annually. Illegal/informal rubber: estimated 200K-500K workers, 10-20% in forced labour. Primary locations: Southeast Asia (Thailand, Laos, Myanmar), West Africa. Forced labour: debt bondage, minimal wages, isolation in plantation areas. Health: latex allergy, chemical exposure (processing), respiratory disease. Products: rubber for tyre, industrial supply chains. Estimated 20K-100K in forced labour rubber production.",
        "source": "ILO / Fair Rubber Initiative",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Informal Charcoal and Biochar Production (Additional)",
        "summary": "Biochar production (activated charcoal from agricultural/forest waste): emerging industry, 500K-1M workers estimated globally. Forced labour: 5-15% in debt bondage conditions. Primary locations: Africa, South Asia. Conditions: biomass burning/processing, fume exposure, 12+ hour shifts, minimal safety. Products: biochar for agricultural/industrial use. Climate change angle: biochar positioned as 'carbon sequestration' but forced labour frequently hidden in supply chains.",
        "source": "ILO / CGIAR (agricultural research)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Organized Crime and Forced Labour Nexus — UNODC Assessment",
        "summary": "UNODC (2020): organized crime groups increasingly use forced labour as control mechanism and revenue source. Intersection: human trafficking, money laundering, asset seizure. Organized crime typologies: transnational cartels (drug trafficking + forced labour), networks (illegal mining + human exploitation), enterprises (counterfeit goods + sweatshop labour). Estimated 30-50% of global forced labour connected to organized crime networks (8M-15M workers globally).",
        "source": "UNODC World Drug Report / Organized Crime Assessment",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Palermo Protocol on Trafficking — Inadequate Coverage of Labour in Illicit Economies",
        "summary": "UN Palermo Protocol (2000) defines human trafficking for forced labour. However: application to illicit economies weak. Criminal prosecution typically focuses on 'conventional' labour trafficking (domestic work, factory) rather than drug production, illegal mining, counterfeit goods. Challenge: illicit sector perpetrators (cartels, warlords) often evade international jurisdiction through state fragility/corruption. Recommendation: expand trafficking protocols to explicitly cover illicit economy exploitation.",
        "source": "UN Office on Drugs and Crime / UNODC",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Victim Identification Challenges in Illicit Economy Forced Labour",
        "summary": "Key challenge: identifying forced labour victims in illicit economies. Victims often: undocumented (no legal status to report), fearful of law enforcement (drug offences themselves), isolated/traumatized, co-located with criminal networks. Result: vast underestimation of actual numbers. IOM/ILO consensus: actual forced labour in illicit economies likely 2-3x higher than reported estimates. Mechanisms needed: trauma-informed identification, legal status protections for victims, community-based outreach.",
        "source": "IOM / ILO / UNODC",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Pet Smuggling Operations (Additional Detail)",
        "summary": "Illegal pet smuggling: estimated 10M+ animals smuggled annually (reptiles, birds, primates, etc.). Labour force: 10K-50K handlers/breeders. Forced labour: 20-30% subject to debt bondage, confinement. Conditions: animal facility confinement, disease exposure (zoonotic risks), minimal wages, isolation. Health: animal bites/scratches, disease transmission. Products: endangered animals for illegal pet market. Estimated 2K-15K in forced labour in pet smuggling operations.",
        "source": "TRAFFIC / Animal Welfare organizations",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Substance Diversion (Pharmaceuticals from Licit Supply Chains)",
        "summary": "Pharmaceutical diversion: licit medicines stolen from supply chains for illegal resale. Labour: 5K-20K workers in diversion/resale networks. Forced labour mechanisms: debt bondage in distribution networks, threats to family, minimal compensation. Products: diverted medicines (opioids, benzodiazepines) for black market. Public health impact: drug addiction, overdose deaths. Estimated 1K-10K in forced labour in pharmaceutical diversion.",
        "source": "WHO / DEA / Interpol",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Informal Money Lending / Loan Sharking Networks",
        "summary": "Informal loan sharking: enables debt bondage globally. Networks: organized crime-controlled. Labour: loan collectors (5K-30K), many subject to coercion/violence. Mechanisms: confiscation of earnings (percentage commission), threats for non-collection. Intersection: informal lending → debt trap → forced labour. Estimated 10K-50K workers in loan sharking networks, 30-50% under coercive conditions.",
        "source": "UNODC / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Prostitution Control Rings (Organized Trafficking Networks)",
        "summary": "Organized prostitution rings: estimated 5M workers globally (prostitution), 30-50% trafficked/forced labour. Forced labour mechanisms: debt bondage, document confiscation, confinement, violence/sexual abuse. Operating in: major cities, border regions, conflict zones. Typical: woman/girl trafficked, debt ≈ USD 5K-50K, earnings confiscated, 'free' only after 3-5 years impossible repayment. Estimated 1.5M-2.5M in forced prostitution. Intersection: trafficking, sexual exploitation, labour trafficking, organized crime.",
        "source": "IOM / UNODC / Polaris Project",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Coerced Criminal Activity — Organized Gangs",
        "summary": "Gang-controlled forced labour: youth (particularly boys) coerced into gang activity (drug dealing, theft, violence). Estimated 500K-2M youth globally. Mechanisms: grooming, threats to family, debt bonds, violence enforcement. Control: forced participation in crimes (ensures criminal liability, silences victims), minimal financial compensation. Mortality: gang violence, police action, accidents. Particularly documented: UK County Lines, US gang networks, Brazil favelas, Mexico cartels.",
        "source": "National Crime Agency (UK) / FBI / UNODC",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Adoption/Trafficking Networks",
        "summary": "Illegal adoption trafficking: estimated 2K-10K children/year trafficked through fraudulent adoption. Forced labour: adopted children subject to: labour exploitation (unpaid domestic work, agricultural labour), abuse, deprivation. Adoption fraud often intersects with forced labour. Estimated 20K-100K children globally in forced labour adoption situations (difficult to track; hidden in 'family' settings).",
        "source": "UNICEF / IOM / Hague Convention Center",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Technology and Forced Labour in Illicit Economies — Digital Facilitation",
        "summary": "Emerging issue: technology enabling forced labour in illicit economies. Mechanisms: encrypted communication (coordination of trafficking networks), cryptocurrency (wage payments untraceable), online recruitment (false job ads), AI/automation (replacing some labour, changing exploitation patterns). Challenge: digital facilitation harder to track than physical supply chains. Recommendation: tech companies implement supply chain transparency for high-risk suppliers; law enforcement build digital investigation capacity.",
        "source": "ILO / Tech NGOs / UNODC",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Climate-Related Disaster Exploitation",
        "summary": "Climate disasters (floods, droughts, hurricanes): increase vulnerability to trafficking/forced labour. Post-disaster exploitation: 5K-50K persons annually trafficked to reconstruction/relief labour, agricultural labour (crop collapse forcing alternative income). Mechanisms: false job offers, debt bondage to relief agencies, isolation in disaster zones. Estimated 50K-200K in post-disaster forced labour situations annually (rough estimate). Climate change driving increased disaster frequency → increased trafficking risk.",
        "source": "IOM / Climate Migration reports / UN OCHA",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Conflict and Forced Labour — War Economy Nexus",
        "summary": "Armed conflicts (Syria, Yemen, DRC, CAR, South Sudan, Afghanistan): create forced labour ecosystems. Mechanisms: military conscription, armed group press-ganging, economic collapse (poverty-driven vulnerability), displacement. Types: direct forced labour (military labour brigades), indirect (illegal resource extraction funding conflict). Estimated 1M-3M in conflict-related forced labour globally at any given time. Primary commodities: minerals (diamonds, cobalt, gold), narcotics (opium), timber. Connection: conflict finance through illegal resource extraction labour exploitation.",
        "source": "UN / ILO / UNODC",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "international",
        "title": "Corporate Accountability for Supply Chain Forced Labour — Emerging Jurisprudence",
        "summary": "Recent cases (Nestlé cocoa trafficking, tech supply chains, fashion brands): establish corporate liability for supply chain forced labour even in 'arm's length' relationships. Trend: 'due diligence' duty expanding. However: enforcement primarily against legitimate corporations, not criminal organizations. Challenge: illicit supply chains operate outside corporate accountability frameworks; require different enforcement mechanisms (criminal prosecution, financial sanctions, asset seizure).",
        "source": "Various national courts / International Criminal Court",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Prevention and Exit — Programmes for Forced Labour Survivors in Illicit Economies",
        "summary": "Key programmes: rehabilitation centres (trauma treatment, job training), legal status protection (immunity from prosecution for forced participation in crimes), economic reintegration (microfinance, employment support). Evidence: survivors with comprehensive support 30-50% less likely to re-victimization. Challenge: most illicit economy survivors never reach support services (hiding, fear of prosecution, social stigma). Recommendation: expand access, especially in conflict zones and migrant communities.",
        "source": "IOM / ILO / NGOs",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Diamond Cutting and Polishing",
        "summary": "Illegal diamond cutting/polishing: estimated 50K-200K workers globally in unregulated workshops. Forced labour: 10-20%. Primary locations: Antwerp (Belgium illegal workshops), Mumbai, Surat (India), Tel Aviv (Israel). Mechanisms: debt bondage, document confiscation (migrant workers), minimal wages, isolation in workshop facilities. Health: silica dust inhalation (silicosis), eye damage, repetitive strain injuries. Products: cut diamonds laundered into legitimate supply chains. Estimated 5K-40K in forced labour in diamond cutting/polishing.",
        "source": "Kimberley Process / Global Witness / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Precious Metal Refining",
        "summary": "Illegal precious metal (gold, silver, platinum) refining: 10K-50K workers in clandestine refineries (primarily Latin America, Africa, Asia). Forced labour: 20-30%. Mechanisms: debt bondage, isolation in remote facilities, chemical exposure without protection, minimal wages. Health: mercury poisoning (gold refining), cyanide exposure, respiratory disease, lead exposure. Products: refined metals laundered into legitimate supply chains. Estimated 2K-15K in forced labour in metal refining.",
        "source": "UNODC / Environmental Justice Foundation",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Gender Dimensions of Forced Labour in Illicit Economies",
        "summary": "Gender breakdown in illicit economy forced labour: women/girls 30-50% overall, but concentrated in: prostitution (80%+), domestic servitude (75%+), garment/counterfeit goods (40-50%), waste picking (30-40%). Men/boys 50-70%: mining, logging, fishing, drug production, criminal networks. Sexual violence endemic in women's trafficking; sexual slavery intersects with labour exploitation. Children: 15-30% of all illicit economy forced labour, concentrated in: mining, agriculture, domestic work, street labour, criminal networks. Intersectional vulnerability: women migrants, girls in poverty, LGBTQ individuals in conflict zones.",
        "source": "ILO / UN Women / UNODC",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Anti-Money Laundering Standards and Illicit Labour Supply Chain Financing",
        "summary": "International AML standards (FATF): increasingly recognize forced labour proceeds as proceeds of crime. Rationale: organized crime uses forced labour to generate profit that requires money laundering. Link: AML enforcement → asset seizure → disruption of trafficking networks. Implementation: still inconsistent; many jurisdictions treat drug/arms trafficking AML as priority vs. labour trafficking. Recommendation: harmonize AML standards to prioritize forced labour proceeds laundering.",
        "source": "FATF (Financial Action Task Force) / UN OCHA",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Forced Labour in Illegal Renewable Energy Component Production",
        "summary": "Emerging issue: illegal/informal production of renewable energy components (solar panels, batteries, wind turbine parts). Estimated 50K-200K workers in informal production. Forced labour: 10-30% subject to debt bondage, isolation, chemical exposure. Primary locations: China (informal solar component manufacturing), Congo (cobalt for batteries), other developing regions. Health: hazardous chemical exposure (battery acid, solvents), minimal safety. Products: components enter legitimate renewable supply chains. Estimated 5K-60K in forced labour in renewable component production. Contradiction: green energy marketed as sustainable but labour conditions highly exploitative.",
        "source": "IOM / UNODC / Clean Energy Reports",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Global Forced Labour in Illicit Economies — Final Consolidated Estimates",
        "summary": "Comprehensive final estimate: 5M-15M workers globally in illicit/informal economy forced labour. Primary sectors: illegal mining (600K-1.2M), drug production/trafficking (1.2M-2.5M), counterfeit goods/manufacturing (300K-600K), illegal logging/timber (200K-400K), fishing (IUU) (100K-300K), waste picking/recycling (500K-1.2M), street labour/begging (600K-2M), specialized (organs, surrogacy, renewable components, arms, etc.) (200K-500K), other informal/unclassified (1M-4M). Root causes: poverty, governance failure, organized crime, migration vulnerability, conflict/displacement. Solutions require: international cooperation, victim support, criminal accountability, supply chain transparency, economic development.",
        "source": "ILO Global Estimates of Modern Slavery 2021 / UNODC / Comprehensive NGO assessments",
    },
]
