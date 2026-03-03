"""Brazil modern slavery -- trabalho escravo enforcement, dirty list, and sector exploitation."""

BRAZIL_MODERN_SLAVERY_FACTS: list[dict] = [
    # ════════════════════════════════════════════════════════════════════
    #  PART 1 — ARTICLE 149 AND LEGAL FRAMEWORK
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Article 149 of the Brazilian Penal Code — Reducing a Person to a Condition Analogous to Slavery",
        "summary": (
            "Article 149 criminalizes reducing someone to a condition analogous "
            "to slavery (trabalho escravo). Amended by Law 10.803/2003, it defines "
            "four constituent elements: (1) forced labour, (2) exhausting working "
            "hours, (3) degrading working conditions, and (4) restriction of "
            "movement by any means. Penalties range from 2 to 8 years imprisonment "
            "plus a fine. The 2003 amendment was critical because it expanded the "
            "definition beyond physical restraint to include degrading conditions "
            "and exhausting hours, aligning with ILO forced labour indicators."
        ),
        "source": "Brazilian Penal Code (Decreto-Lei 2.848/1940, amended by Lei 10.803/2003)",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Constitutional Amendment 81/2014 — Expropriation of Properties Using Slave Labour",
        "summary": (
            "PEC do Trabalho Escravo (Constitutional Amendment 81) amended Article "
            "243 of the Federal Constitution to allow expropriation without "
            "compensation of rural and urban properties where slave labour is "
            "found. Expropriated properties are to be used for agrarian reform or "
            "social housing. Approved by Congress in June 2014 after 15 years of "
            "legislative debate. Still awaits enabling legislation to define "
            "the precise criteria for expropriation, limiting its practical "
            "application."
        ),
        "source": "Senado Federal / Emenda Constitucional 81/2014",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Law 10.803/2003 — Modernization of Article 149",
        "summary": (
            "Law 10.803 of December 2003 replaced the vague original text of "
            "Article 149 with a precise enumeration of four indicators of slave-like "
            "conditions. Before 2003, courts required proof of physical coercion; "
            "the reform allowed conviction based on degrading conditions alone "
            "(lack of sanitation, potable water, or adequate shelter). This law "
            "dramatically increased successful prosecutions from fewer than 10 per "
            "year pre-2003 to over 50 per year by 2010."
        ),
        "source": "Lei 10.803/2003 / Diario Oficial da Uniao",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "STF RE 459.510 — Competence of Federal Courts for Article 149",
        "summary": (
            "The Supreme Federal Tribunal (STF) ruled that criminal prosecution "
            "under Article 149 falls under federal jurisdiction when the offence "
            "violates the organized labour system or fundamental rights protected "
            "by the Constitution. This resolved a jurisdictional dispute between "
            "state and federal courts that had caused delays in prosecutions. "
            "Federal jurisdiction ensures specialized prosecutors and judges handle "
            "slave labour cases."
        ),
        "source": "Supremo Tribunal Federal (STF)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "STF Inquerito 3.412/AL (2012) — Degrading Conditions Sufficient for Conviction",
        "summary": (
            "The STF confirmed that degrading conditions alone, without proof of "
            "physical coercion or restriction of movement, are sufficient for "
            "conviction under Article 149. The case involved a senator from "
            "Alagoas whose fazenda workers lacked potable water, sanitary "
            "facilities, and adequate shelter. This landmark ruling cemented the "
            "broad interpretation of trabalho escravo under Brazilian law."
        ),
        "source": "STF / Inquerito 3.412/AL",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Portaria Interministerial MTE/SDH 2/2011 — Dirty List Regulation",
        "summary": (
            "This inter-ministerial regulation established the legal framework for "
            "the Cadastro de Empregadores (Lista Suja / Dirty List), specifying "
            "procedures for inclusion and exclusion. Employers remain on the list "
            "for two years. Inclusion occurs after administrative proceedings by "
            "the Ministry of Labour confirm slave-like conditions. Employers can "
            "be removed early if they pay all labour obligations and adopt "
            "preventive measures. Financial institutions use the list for credit "
            "screening."
        ),
        "source": "MTE / SDH / Portaria Interministerial 2/2011",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Portaria Interministerial MTPS/MMIRDH 4/2016 — Updated Dirty List Rules",
        "summary": (
            "Updated regulation for the Dirty List after the STF temporarily "
            "suspended the original list in 2014. The new portaria introduced "
            "enhanced due process protections: employers must be notified before "
            "inclusion, given 30 days to respond, and provided appeal mechanisms. "
            "The updated rules survived legal challenges and the list was "
            "republished in March 2017."
        ),
        "source": "MTPS / MMIRDH / Portaria Interministerial 4/2016",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "STF ADI 5.209 (2014) — Temporary Suspension of the Dirty List",
        "summary": (
            "In December 2014, STF Justice Ricardo Lewandowski issued an "
            "injunction suspending publication of the Dirty List in response to "
            "a challenge by the Brazilian Association of Real Estate Developers "
            "(ABRAINC). The suspension lasted over two years and was widely "
            "criticized by the ILO, anti-slavery NGOs, and the MPT. The list "
            "was eventually republished in March 2017 under updated rules."
        ),
        "source": "STF / ADI 5.209",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "National Plan for the Eradication of Slave Labour — First Plan (2003)",
        "summary": (
            "Launched by President Lula in 2003, the First National Plan "
            "established 76 targets across prevention, enforcement, victim "
            "assistance, and institutional coordination. Key measures included "
            "strengthening the Grupo Especial de Fiscalizacao Movel (GEFM), "
            "creating the Dirty List, and establishing CONATRAE. The plan was "
            "recognized by the ILO as a model for other countries in the region."
        ),
        "source": "Presidencia da Republica / ILO / CONATRAE",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Second National Plan for the Eradication of Slave Labour (2008)",
        "summary": (
            "Building on the 2003 plan, the Second National Plan introduced 66 "
            "new targets including supply chain accountability measures, enhanced "
            "victim reintegration programs, and educational campaigns. It "
            "emphasized the role of the private sector through the National Pact "
            "for the Eradication of Slave Labour (Pacto Nacional). The plan "
            "acknowledged that eradication required addressing root causes: "
            "poverty, lack of education, and land concentration."
        ),
        "source": "CONATRAE / OIT Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 2 — GEFM (MOBILE INSPECTION GROUP) OPERATIONS
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Grupo Especial de Fiscalizacao Movel (GEFM) — Creation and Operations",
        "summary": (
            "Established in 1995 under the Ministry of Labour, the GEFM conducts "
            "surprise inspections on properties suspected of using slave labour. "
            "Teams comprise labour inspectors (Auditores-Fiscais do Trabalho), "
            "federal police officers, and MPT prosecutors. Between 1995 and 2023, "
            "GEFM operations rescued over 60,000 workers from slave-like "
            "conditions across all Brazilian states."
        ),
        "source": "MTE / GEFM / OIT Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "GEFM Rescue Statistics 1995-2023",
        "summary": (
            "From 1995 through 2023, the GEFM conducted over 6,000 inspections "
            "and rescued approximately 62,000 workers from conditions analogous "
            "to slavery. Peak rescue years include 2003 (5,223 workers), 2007 "
            "(5,999 workers), and 2008 (5,016 workers). Rescues declined after "
            "2015 due to budget cuts and reduced staffing, with fewer than 1,000 "
            "workers rescued annually in some recent years."
        ),
        "source": "MTE / Subsecretaria de Inspecao do Trabalho / InPACTO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "GEFM Operation in Southern Para (2003) — 1,108 Workers Rescued",
        "summary": (
            "In a single operation in Sao Felix do Xingu, Para, the GEFM rescued "
            "1,108 workers from cattle ranches and charcoal kilns. Workers had "
            "been recruited from Maranhao and Piaui with false promises of good "
            "wages. They were held by armed guards, forced to buy food and "
            "supplies from the ranch store at inflated prices (truck system / "
            "sistema de barracoes), and had no access to medical care."
        ),
        "source": "MTE / Comissao Pastoral da Terra (CPT)",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "GEFM Operation Araguaia (2004) — Cattle Ranches in Tocantins",
        "summary": (
            "Multi-day GEFM operation targeting cattle ranches along the Araguaia "
            "River in Tocantins. Inspectors found 260 workers clearing pasture "
            "under degrading conditions: sleeping in open-air shelters made of "
            "plastic sheeting, drinking untreated river water, and working 12-hour "
            "days without rest. Workers were paid below minimum wage and forced "
            "to repay inflated transport costs."
        ),
        "source": "MTE / MPT Tocantins",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "GEFM Budget and Staffing Decline (2014-2022)",
        "summary": (
            "The GEFM budget was cut by approximately 50% between 2014 and 2022. "
            "The number of active labour inspectors in Brazil fell from 3,644 in "
            "2012 to approximately 2,093 in 2022, well below the ILO-recommended "
            "ratio. This decline coincided with reduced rescue numbers: from over "
            "3,000 workers per year in the 2000s to under 1,500 in some recent "
            "years. Civil society groups denounced the cuts as a deliberate "
            "weakening of enforcement."
        ),
        "source": "MTE / SINAIT / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "GEFM Operation at Fazenda Cabaceiras, Mato Grosso (2005)",
        "summary": (
            "Labour inspectors found 1,003 workers in slave-like conditions on a "
            "soy and cattle farm in Mato Grosso. Workers had been recruited from "
            "Maranhao by intermediaries (gatos). They were forced to clear forest "
            "for pasture expansion, provided no protective equipment against "
            "pesticides, and housed in makeshift shelters. The farm owner was "
            "placed on the Dirty List and fined BRL 2.3 million."
        ),
        "source": "MTE / CPT / Reporter Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 3 — LISTA SUJA (DIRTY LIST)
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Lista Suja (Dirty List) — Mechanism and Impact",
        "summary": (
            "The Cadastro de Empregadores que tenham submetido trabalhadores a "
            "condicoes analogas a de escravo (Dirty List) is a public register "
            "of employers found using slave labour. Created in 2003, it is "
            "updated biannually. Inclusion triggers financial consequences: the "
            "National Monetary Council (Resolution 3.876/2010) instructs banks "
            "to deny credit to listed employers. Over 900 employers have been "
            "listed since inception. The Pacto Nacional encourages over 500 "
            "signatory companies to cut supply chain ties with listed entities."
        ),
        "source": "MTE / Pacto Nacional pela Erradicacao do Trabalho Escravo",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Dirty List — Zara/Inditex Supply Chain Inclusion (2011)",
        "summary": (
            "In 2011, labour inspectors found 15 Bolivian and Peruvian workers "
            "in slave-like conditions at a Sao Paulo workshop producing garments "
            "for Zara (Inditex). Workers laboured 16-hour days in locked rooms, "
            "earned BRL 274/month (below minimum wage), and had movement "
            "restricted. Inditex's Brazilian subsidiary was placed on the Dirty "
            "List. Inditex subsequently signed a TAC (conduct adjustment term) "
            "with the MPT, paying BRL 20 million and agreeing to monitor its "
            "supply chain."
        ),
        "source": "MTE / MPT-SP / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Dirty List — Major Rancher Cases in Para",
        "summary": (
            "Multiple large-scale cattle ranchers in Para have appeared on the "
            "Dirty List, including operations linked to major meatpacking companies. "
            "Between 2003 and 2020, over 150 farms in Para were listed, making it "
            "the state with the highest number of Dirty List entries. The "
            "connection between deforestation, cattle ranching, and slave labour "
            "in Para has been documented by the CPT and Reporter Brasil."
        ),
        "source": "MTE / CPT / Reporter Brasil / Greenpeace Brazil",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Banco Central Resolution 3.876/2010 — Credit Denial for Dirty List Employers",
        "summary": (
            "Resolution 3.876 of the National Monetary Council instructs banks "
            "and financial institutions to deny rural credit to employers on "
            "the Dirty List. This economic sanction is considered the most "
            "effective deterrent: landowners dependent on subsidized agricultural "
            "credit (through BNDES, Banco do Brasil, etc.) risk losing access to "
            "financing critical for their operations. The resolution applies to "
            "all public banks and is voluntarily adopted by many private banks."
        ),
        "source": "Banco Central do Brasil / Conselho Monetario Nacional",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Dirty List — Cosan/Raizen Sugar Group (2009)",
        "summary": (
            "Cosan, Brazil's largest sugar and ethanol producer (later merged "
            "into Raizen with Shell), had several supplying farms placed on the "
            "Dirty List after workers were found in degrading conditions during "
            "sugarcane harvesting. The listing generated international attention "
            "given Cosan's role in biofuel exports to the EU. Cosan committed to "
            "mechanization of sugarcane harvesting and supply chain monitoring."
        ),
        "source": "MTE / Reporter Brasil / MPT",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Dirty List Statistics — Cumulative Entries",
        "summary": (
            "Between 2003 and 2023, over 900 employers were included on the "
            "Dirty List. Approximately 40% are from the cattle ranching sector, "
            "followed by agriculture (sugarcane, coffee, soy) at 25%, charcoal "
            "production at 10%, construction at 8%, and textiles/garments at 7%. "
            "Para, Mato Grosso, and Minas Gerais account for the highest number "
            "of listed employers. Many listed employers are repeat offenders who "
            "reappear after their two-year exclusion period ends."
        ),
        "source": "MTE / InPACTO / Reporter Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 4 — CATTLE RANCHING FORCED LABOUR
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Cattle Ranching Slave Labour in Para — Systemic Pattern",
        "summary": (
            "Para state accounts for the highest number of slave labour rescues "
            "in Brazil. The pattern involves gatos (labour intermediaries) "
            "recruiting desperate workers from Maranhao and Piaui to clear forest "
            "for cattle pasture. Workers arrive in debt for transport and "
            "equipment costs, are held by armed guards, and buy food from "
            "overpriced fazenda stores (sistema de barracao). Between 1995 and "
            "2020, over 15,000 workers were rescued from cattle ranches in Para."
        ),
        "source": "CPT / MTE / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Fazenda Brasil Verde, Para — Emblematic Slave Labour Case",
        "summary": (
            "Fazenda Brasil Verde in Sapucaia, Para was inspected multiple times "
            "between 1988 and 2000, with repeated findings of slave labour. In "
            "March 2000, inspectors rescued 85 workers including adolescents. "
            "Workers cleared forest by hand, were guarded by armed men, received "
            "no wages, and were threatened with death if they tried to leave. "
            "Two adolescents who escaped reported the conditions to the CPT. "
            "The case was eventually taken to the Inter-American Court."
        ),
        "source": "CPT / MTE / Inter-American Commission on Human Rights",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Cattle-Deforestation-Slave Labour Nexus in Mato Grosso",
        "summary": (
            "Mato Grosso, Brazil's largest cattle state, has a documented nexus "
            "between illegal deforestation and slave labour. Workers are recruited "
            "to clear Amazon and Cerrado vegetation for pasture expansion. "
            "Between 2003 and 2020, over 8,000 workers were rescued in Mato "
            "Grosso, predominantly from cattle and soy operations. Reporter "
            "Brasil and Greenpeace have traced slave-labour cattle to major "
            "meatpackers JBS, Marfrig, and Minerva."
        ),
        "source": "Reporter Brasil / Greenpeace / MTE / IBAMA",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Goias Cattle Ranch Rescues — Persistent Pattern",
        "summary": (
            "Goias state consistently ranks among the top states for slave "
            "labour rescues. In 2017, 79 workers were rescued from a single "
            "ranch in Porangatu clearing pasture. Workers slept in hammocks "
            "under trees, drank water from streams shared with cattle, and had "
            "wages withheld for months. The ranch supplied cattle to a regional "
            "slaughterhouse linked to national distribution chains."
        ),
        "source": "MTE / MPT Goias / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "JBS Supply Chain — Links to Slave Labour Ranches",
        "summary": (
            "JBS, the world's largest meatpacker, has been repeatedly linked to "
            "cattle ranches on the Dirty List through indirect suppliers (cattle "
            "laundering). Cattle are moved from Dirty List ranches to clean "
            "intermediary ranches before sale to JBS slaughterhouses, making "
            "traceability difficult. The Federal Prosecution Service (MPF) filed "
            "suits against JBS for purchasing from embargoed ranches in Para. "
            "JBS committed to full supply chain traceability by 2025."
        ),
        "source": "MPF / Reporter Brasil / Greenpeace / Mighty Earth",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 5 — SUGARCANE HARVEST EXPLOITATION
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Sugarcane Harvest Deaths in Sao Paulo — Exhaustion-Related Fatalities",
        "summary": (
            "Between 2004 and 2009, at least 21 sugarcane cutters died of "
            "exhaustion (morte por exaustao) during harvest in Sao Paulo state. "
            "Workers cut 12 to 15 tons of cane per day in temperatures exceeding "
            "35C, paid by piece rate, with no rest breaks enforced. The deaths "
            "prompted congressional investigations and MPT actions. The Pastoral "
            "do Migrante documented workers collapsing in fields after 10-hour "
            "cutting shifts."
        ),
        "source": "Pastoral do Migrante / MPT-SP / CPI do Trabalho Escravo",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Sugarcane Workers from Minas Gerais Northeast — Migrant Exploitation",
        "summary": (
            "Thousands of workers migrate annually from northeastern Minas "
            "Gerais (Vale do Jequitinhonha) and Bahia to cut sugarcane in Sao "
            "Paulo. Recruitment by gatos who charge transport fees creates "
            "immediate debt bondage. Workers are housed in overcrowded alojamentos "
            "(barracks), charged for accommodation, food, and equipment, often "
            "ending the harvest season with no net earnings. The pattern is "
            "termed 'modern-day slavery by exhaustion' by the CPT."
        ),
        "source": "CPT / Pastoral do Migrante / MTE / OIT Brasil",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Compromisso Nacional para Aperfeicoar as Condicoes de Trabalho na Cana-de-Acucar (2009)",
        "summary": (
            "The National Commitment to Improve Working Conditions in Sugarcane, "
            "signed by the federal government, industry (UNICA), and workers' "
            "unions, established minimum standards: provision of drinking water "
            "and shade, mandatory rest breaks every 90 minutes, transportation "
            "standards, and end to payment systems encouraging overwork. While "
            "voluntary, compliance is monitored by the MTE. Adherence improved "
            "conditions at major mills but small and medium producers often "
            "remain non-compliant."
        ),
        "source": "UNICA / MTE / Presidencia da Republica",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Sugarcane Mechanization and Worker Displacement",
        "summary": (
            "The Sao Paulo state law phasing out manual cane burning (2014 "
            "deadline for flat land) accelerated mechanization, reducing the "
            "number of manual cutters from 170,000 in 2007 to under 60,000 by "
            "2015 in Sao Paulo. While mechanization reduced exhaustion-related "
            "deaths, displaced workers — primarily low-skilled migrants from the "
            "northeast — faced unemployment and vulnerability to other forms of "
            "exploitation, including in urban construction and textile sectors."
        ),
        "source": "UNICA / DIEESE / Pastoral do Migrante",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Usina Santa Helena, Goias (2007) — 1,058 Workers in Degrading Conditions",
        "summary": (
            "GEFM inspectors found 1,058 sugarcane workers at Usina Santa Helena "
            "in Goias living in overcrowded barracks without sanitation, drinking "
            "contaminated water, and working up to 14-hour days. Workers were "
            "transported in open trucks designed for cargo. The mill was fined "
            "BRL 1.2 million and placed on the Dirty List."
        ),
        "source": "MTE / MPT-GO / Reporter Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 6 — COFFEE SUPPLY CHAIN FORCED LABOUR
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Coffee Farm Slave Labour in Minas Gerais — Sul de Minas Region",
        "summary": (
            "The Sul de Minas region produces roughly 25% of Brazil's arabica "
            "coffee. Multiple GEFM operations have found slave-like conditions "
            "on coffee farms: workers sleeping in barns alongside livestock, "
            "drinking water from irrigation channels contaminated with pesticides, "
            "and earning below minimum wage. Between 2003 and 2022, over 800 "
            "workers were rescued from coffee operations in Minas Gerais."
        ),
        "source": "MTE / Reporter Brasil / CPT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Nestle Supply Chain — Coffee Farms Linked to Slave Labour (2016)",
        "summary": (
            "A 2016 investigation by Reporter Brasil and the Danish documentary "
            "team Danwatch found slave-like conditions on coffee farms in Minas "
            "Gerais supplying Nestle through intermediaries. Workers on fazendas "
            "in Campos Gerais were found without employment contracts, housed in "
            "degrading conditions, and exposed to pesticides without PPE. Nestle "
            "acknowledged the findings and committed to enhanced supply chain "
            "due diligence through its Responsible Sourcing program."
        ),
        "source": "Reporter Brasil / Danwatch / Nestle CSR Report 2016",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Starbucks Supply Chain — Coffee Linked to Forced Labour (2016)",
        "summary": (
            "Reporter Brasil investigations found that farms certified by "
            "sustainability programs supplying Starbucks were implicated in "
            "slave-like labour practices. Workers on certified farms in Minas "
            "Gerais experienced wage theft, excessive hours, and degrading "
            "housing. Starbucks conducts C.A.F.E. Practices audits but critics "
            "argue that audits are pre-announced and fail to detect exploitation "
            "of seasonal workers."
        ),
        "source": "Reporter Brasil / Starbucks C.A.F.E. Practices / ILO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Coffee Harvest Slave Labour in Bahia",
        "summary": (
            "Western Bahia's expanding coffee frontier (Barreiras, Luis Eduardo "
            "Magalhaes) has seen repeated slave labour rescues. In 2019, 18 "
            "workers were rescued from a coffee farm where they slept on the "
            "ground in open sheds, had no potable water, and were paid per "
            "basket with deductions for food and tools that exceeded earnings. "
            "The recruitment pattern involves gatos from Maranhao targeting "
            "indigenous and quilombola communities."
        ),
        "source": "MTE / MPT-BA / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "ILO-Brazil Coffee Sector Partnership",
        "summary": (
            "The ILO Brazil office has partnered with the Brazilian Specialty "
            "Coffee Association (BSCA) and exporters to develop forced labour "
            "monitoring protocols for coffee supply chains. The partnership "
            "includes training for auditors on ILO forced labour indicators, "
            "worker grievance mechanisms, and traceability from farm to port. "
            "Despite these efforts, seasonal coffee workers remain vulnerable "
            "due to informal employment relationships and piece-rate payment."
        ),
        "source": "OIT Brasil / BSCA / Reporter Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 7 — CHARCOAL PRODUCTION / PIG IRON SUPPLY CHAIN
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Charcoal Kiln Slave Labour — Carajas Corridor, Para/Maranhao",
        "summary": (
            "The Carajas industrial corridor in Para and Maranhao hosts pig iron "
            "smelters that use charcoal as fuel. Charcoal is produced in "
            "rudimentary kilns deep in the forest where workers, including "
            "children, endure extreme heat, smoke inhalation, and degrading "
            "living conditions. Between 1995 and 2015, over 4,000 workers were "
            "rescued from charcoal operations in the Carajas corridor. Many "
            "operations are linked to illegal deforestation."
        ),
        "source": "CPT / MTE / Reporter Brasil / Greenpeace",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Pig Iron-Steel Supply Chain — Connection to US and EU Markets",
        "summary": (
            "Brazilian pig iron produced with slave-labour charcoal has been "
            "traced to steel mills in the US and EU. A 2012 Bloomberg investigation "
            "found that charcoal from operations using slave labour fed smelters "
            "in Maranhao whose pig iron was exported to US steelmakers. The "
            "revelations led to congressional hearings in both Brazil and the "
            "US, and several pig iron companies were placed on the Dirty List."
        ),
        "source": "Bloomberg / US Congressional Research Service / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Child Labour in Charcoal Production — Minas Gerais",
        "summary": (
            "Minas Gerais is Brazil's largest charcoal-producing state, supplying "
            "the steel and iron ore industries. The ILO and UNICEF have documented "
            "persistent child labour in charcoal kilns, with children as young as "
            "8 loading and unloading kilns, exposed to toxic smoke and burns. "
            "The PETI program (Programme for the Eradication of Child Labour) has "
            "reduced but not eliminated the practice. In 2018, 32 children were "
            "found working at charcoal operations in the Jequitinhonha valley."
        ),
        "source": "OIT Brasil / UNICEF / PETI / MTE",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Charcoal Workers in Mato Grosso do Sul — Indigenous Exploitation",
        "summary": (
            "Indigenous Guarani-Kaiowa workers in Mato Grosso do Sul have been "
            "found in slave-like conditions producing charcoal for the steel "
            "industry. Displaced from ancestral lands by agribusiness expansion, "
            "indigenous communities accept charcoal work out of desperation. "
            "In 2015, 17 Guarani workers were rescued from kilns where they "
            "worked 7 days a week without rest, earning BRL 15 per cubic metre "
            "of charcoal produced."
        ),
        "source": "MTE / FUNAI / MPT-MS / CPT",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 8 — CONSTRUCTION SECTOR FORCED LABOUR
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "World Cup 2014 — Construction Worker Exploitation",
        "summary": (
            "Construction of stadiums and infrastructure for the 2014 FIFA World "
            "Cup involved widespread labour violations. At least 11 workers died "
            "during stadium construction. Workers at the Arena Corinthians in "
            "Sao Paulo and the Manaus Arena reported excessive overtime (up to "
            "16 hours/day before deadlines), unsafe conditions, and wage theft. "
            "The MPT filed multiple actions against contractors. FIFA and the "
            "Brazilian government were criticized by Building and Wood Workers' "
            "International (BWI) for inadequate labour protections."
        ),
        "source": "MPT / BWI / Reporter Brasil / FIFA",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Olympics 2016 — Rio Construction Labour Violations",
        "summary": (
            "Construction for the 2016 Rio Olympics involved over 40,000 workers, "
            "many recruited from the northeast. Reports documented 16-hour shifts, "
            "unsafe scaffolding, and at least 11 worker deaths. Workers at the "
            "Olympic Park in Barra da Tijuca reported wage delays of up to 3 "
            "months. Subcontracting chains of 4-5 layers obscured employer "
            "responsibility. The MPT secured BRL 18 million in settlements from "
            "contractors for labour violations."
        ),
        "source": "MPT-RJ / BWI / Reporter Brasil / IOC",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Construction Worker Slave Labour — Nordeste Migrants in Sao Paulo",
        "summary": (
            "Migrant construction workers from Bahia, Maranhao, and Piaui "
            "working in Sao Paulo's residential construction sector are "
            "vulnerable to slave-like conditions. In 2013, 111 workers were "
            "rescued from a luxury condominium construction site in Sao Paulo "
            "where they lived in containers without ventilation, were charged "
            "for accommodation and food, and had wages withheld. The contractor "
            "was placed on the Dirty List."
        ),
        "source": "MTE / MPT-SP / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Belo Monte Dam — Construction Labour Exploitation",
        "summary": (
            "The Belo Monte hydroelectric dam in Para, one of the world's largest, "
            "employed over 25,000 workers during peak construction (2012-2015). "
            "The MPT documented excessive overtime, unsafe conditions, inadequate "
            "housing, and at least 5 worker deaths. A 2014 strike by 7,000 "
            "workers protested dangerous conditions and delayed wages. The Norte "
            "Energia consortium was fined BRL 34 million for labour violations."
        ),
        "source": "MPT-PA / Norte Energia / ISA / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Construction Sector — MRV Engenharia Supply Chain",
        "summary": (
            "MRV Engenharia, one of Brazil's largest homebuilders, was placed "
            "on the Dirty List in 2013 after GEFM inspectors found 31 workers "
            "at a subcontractor site in Minas Gerais in degrading conditions. "
            "Workers lacked employment contracts, had no access to drinking "
            "water or toilets, and slept at the construction site. MRV challenged "
            "its listing, arguing subcontractor responsibility, but courts upheld "
            "the joint liability doctrine."
        ),
        "source": "MTE / TRT-3 Minas Gerais / Reporter Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 9 — TEXTILE/GARMENT SWEATSHOPS IN SAO PAULO
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Bolivian Garment Workers in Sao Paulo — Systematic Exploitation",
        "summary": (
            "An estimated 300,000 Bolivian migrants work in Sao Paulo's garment "
            "industry, many in conditions analogous to slavery. Workers are "
            "recruited in Bolivia with promises of good wages and legal status. "
            "Upon arrival, passports are confiscated, workers are locked in "
            "workshops 16-18 hours/day, and debts for transport and housing make "
            "departure impossible. Products enter supply chains of major Brazilian "
            "and international brands."
        ),
        "source": "Reporter Brasil / MPT-SP / CPI do Trabalho Escravo / OIT Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Peruvian Workers in Sao Paulo Garment Workshops",
        "summary": (
            "Alongside Bolivians, Peruvian migrants are exploited in Sao Paulo's "
            "garment workshops, particularly in the Bras and Bom Retiro "
            "neighbourhoods. In 2014, MTE rescued 28 Peruvian workers from a "
            "workshop producing clothing for a major Brazilian retailer. Workers "
            "lived and worked in the same room, slept on fabric piles, and were "
            "paid BRL 0.05-0.20 per garment sewn."
        ),
        "source": "MTE / MPT-SP / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "C&A Supply Chain — Slave Labour in Sao Paulo Workshops (2014)",
        "summary": (
            "Labour inspectors found Bolivian workers in slave-like conditions at "
            "a workshop producing garments for C&A in Sao Paulo. Workers laboured "
            "14-hour days with one day off per month, were locked in the workshop "
            "at night, and earned below minimum wage. C&A signed a TAC with the "
            "MPT worth BRL 3.4 million. The case highlighted how multi-layered "
            "subcontracting obscures brand accountability."
        ),
        "source": "MTE / MPT-SP / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Renner Supply Chain — Garment Workshop Rescues (2014)",
        "summary": (
            "Lojas Renner, one of Brazil's largest fashion retailers, was linked "
            "to slave-labour workshops in Sao Paulo when inspectors found "
            "Bolivian workers producing Renner garments in degrading conditions. "
            "Workers in the Bom Retiro district worked 16 hours/day, shared "
            "mattresses in shifts, and had wages withheld. Renner signed a TAC "
            "with the MPT and implemented a supply chain audit program."
        ),
        "source": "MTE / MPT-SP / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Riachuelo/Guararapes Supply Chain — Repeated Violations",
        "summary": (
            "Riachuelo (Guararapes Confeccoes), a major Brazilian fashion "
            "retailer, was linked to slave-labour workshops multiple times "
            "between 2012 and 2017. In 2017, 38 Bolivian and Paraguayan workers "
            "were rescued from workshops in Sao Paulo's Zona Norte producing "
            "Riachuelo garments. Workers were paid per piece with deductions "
            "that often left them in debt. Guararapes was fined BRL 5 million."
        ),
        "source": "MTE / MPT-SP / Reporter Brasil / TRT-2",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Sao Paulo Municipal Law on Garment Industry Labour Standards",
        "summary": (
            "The Sao Paulo municipal government enacted regulations requiring "
            "garment companies to maintain registers of all subcontractors and "
            "submit to random inspections. The regulations were prompted by "
            "repeated findings of slave labour in the Bras, Bom Retiro, and "
            "Pari neighbourhoods. Compliance remains low, with estimates that "
            "80% of small garment workshops in the city operate informally."
        ),
        "source": "Prefeitura de Sao Paulo / MPT-SP / SINDITEXTIL",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 10 — DOMESTIC WORKER EXPLOITATION
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "PEC das Domesticas — Constitutional Amendment 72/2013",
        "summary": (
            "Constitutional Amendment 72 (Emenda Constitucional 72/2013), known "
            "as PEC das Domesticas, extended labour rights to domestic workers "
            "including: maximum 44-hour work week, overtime pay, FGTS (severance "
            "fund) deposits, night differential, and transportation vouchers. "
            "Regulated by Complementary Law 150/2015, which also established "
            "mandatory registration in the eSocial system. Brazil has an "
            "estimated 5.9 million domestic workers, the largest domestic worker "
            "population globally."
        ),
        "source": "Senado Federal / EC 72/2013 / Lei Complementar 150/2015",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Complementary Law 150/2015 — Domestic Worker Regulation",
        "summary": (
            "Law 150 implements EC 72/2013 by regulating domestic work contracts. "
            "Key provisions: mandatory written contract, 8-hour work day, "
            "mandatory FGTS contributions (8%), unemployment insurance for "
            "domestic workers, prohibition of minors under 18 as domestic "
            "workers, and inclusion in the eSocial digital payroll system. "
            "Despite the law, informal domestic work remains prevalent: an "
            "estimated 70% of domestic workers lacked formal contracts in 2022."
        ),
        "source": "Lei Complementar 150/2015 / DIEESE / IBGE PNAD",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Domestic Servitude Case — Minas Gerais Woman Held 38 Years",
        "summary": (
            "In 2017, a woman was rescued in Minas Gerais after being held in "
            "domestic servitude for 38 years. Taken as a child from a poor "
            "family in the interior, she worked without pay, was denied "
            "education, was not allowed to leave the house, and was physically "
            "abused. The case exemplifies a historically common pattern in "
            "Brazil where poor rural children, especially Black girls, are "
            "taken by wealthier families as 'crias da casa' (household "
            "children) and exploited as unpaid servants."
        ),
        "source": "MPT-MG / Reporter Brasil / OIT Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Domestic Worker Demographics and Vulnerability",
        "summary": (
            "Brazil's 5.9 million domestic workers are predominantly women "
            "(92%) and Black (63%). Average monthly earnings are BRL 1,084, "
            "below the minimum wage. Only 27% have formal employment contracts. "
            "Domestic work accounts for the third-highest number of slave "
            "labour rescues in Brazil. The legacy of slavery — Brazil was the "
            "last country in the Americas to abolish slavery (1888) — directly "
            "shapes the demographics and conditions of domestic work."
        ),
        "source": "IBGE / PNAD Continua / DIEESE / OIT Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Domestic Worker Trafficking — Maranhao to Sao Paulo Pipeline",
        "summary": (
            "A persistent trafficking pipeline brings girls and young women "
            "from rural Maranhao to work as domestic servants in Sao Paulo. "
            "Recruited by intermediaries who promise education and good wages, "
            "victims are placed in households where they work 16+ hours/day, "
            "are not paid, are denied schooling, and often suffer sexual abuse. "
            "The MPT in Maranhao has prosecuted multiple trafficking networks "
            "operating this pipeline."
        ),
        "source": "MPT-MA / Policia Federal / Reporter Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 11 — BRAZILIAN WORKERS EXPLOITED ABROAD
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Brazilian Workers in US Agriculture — Florida Tomato Farms",
        "summary": (
            "Brazilian workers have been victims of forced labour on Florida "
            "tomato farms. In the 2007 case US v. Navarrete, Brazilian workers "
            "were held in debt bondage, locked in trucks, and threatened with "
            "violence. The case contributed to the development of the Fair Food "
            "Program by the Coalition of Immokalee Workers. Brazilian consulates "
            "in Florida have assisted in identifying and repatriating victims."
        ),
        "source": "US DOJ / CIW / Brazilian Consulate Miami",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Brazilian Workers Exploited in Portugal — Construction and Agriculture",
        "summary": (
            "Portuguese authorities have identified Brazilian workers in forced "
            "labour in construction and agriculture, particularly in the Alentejo "
            "region. Workers recruited in Brazil arrive with tourist visas, have "
            "documents confiscated, and work in olive and berry harvesting for "
            "below-minimum wages. In 2021, Portuguese police rescued 20 Brazilian "
            "workers from an agricultural operation in Odemira where they lived "
            "in containers without running water."
        ),
        "source": "SEF Portugal / Brazilian Embassy Lisbon / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Brazilian Dekasegi Workers in Japan — Labour Exploitation",
        "summary": (
            "Over 180,000 Brazilians of Japanese descent (dekasegi) work in "
            "Japan, primarily in manufacturing. Labour brokers (empreiteiras) "
            "charge excessive fees and control housing, creating debt bondage. "
            "Workers report 12-hour shifts, unsafe factory conditions, and "
            "retaliation for complaints. The 2008 financial crisis left "
            "thousands of dekasegi unemployed with no social safety net. "
            "Brazil and Japan signed a bilateral social security agreement "
            "in 2012 to improve protections."
        ),
        "source": "MRE Brasil / Brazilian Consulate Nagoya / OIT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Brazilian Workers in US Cleaning Industry — J-1 Visa Exploitation",
        "summary": (
            "Brazilian students on J-1 cultural exchange visas in the US have "
            "been exploited in cleaning and hospitality work. Recruitment agencies "
            "in Brazil charge USD 3,000-5,000 for placement, creating debt. "
            "Workers in New Jersey and Connecticut reported being forced to "
            "work 70+ hours/week in janitorial services, paid below minimum "
            "wage, and threatened with deportation if they complained. The "
            "State Department has tightened J-1 sponsor oversight in response."
        ),
        "source": "US State Department / Brazilian Consulate New York / NELP",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 12 — INTER-AMERICAN COURT: FAZENDA BRASIL VERDE
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "Fazenda Brasil Verde v. Brazil (IACtHR, 2016) — Landmark Slavery Ruling",
        "summary": (
            "The Inter-American Court of Human Rights ruled that Brazil violated "
            "the American Convention on Human Rights (Article 6, prohibition of "
            "slavery) by failing to prevent, investigate, and punish slave "
            "labour at Fazenda Brasil Verde in Para. The Court found that the "
            "State knew about slave labour at the farm since 1988 but failed to "
            "act effectively. Brazil was ordered to pay USD 5 million in "
            "compensation to 128 victims and adopt measures to prevent "
            "recurrence. This was the first IACtHR ruling on contemporary "
            "slavery in the Americas."
        ),
        "source": "Inter-American Court of Human Rights / Case of the Hacienda Brasil Verde Workers v. Brazil (2016)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "Fazenda Brasil Verde — Inter-American Commission Proceedings (2011)",
        "summary": (
            "The Inter-American Commission on Human Rights referred the Brasil "
            "Verde case to the Court in 2015 after Brazil failed to comply with "
            "the Commission's 2011 merits report. The Commission found that "
            "Brazil violated the rights of 85 workers rescued in 2000 and two "
            "adolescents who had escaped in 1997. The Commission noted that "
            "despite multiple inspections, no criminal convictions were obtained "
            "against the farm owners — illustrating systemic impunity."
        ),
        "source": "IACHR / Report No. 169/11 / Case 12.066",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "Fazenda Brasil Verde — Compliance Monitoring (2017-2023)",
        "summary": (
            "Brazil's compliance with the IACtHR judgment has been partial. "
            "Compensation to victims was paid by 2020, but structural measures "
            "(strengthening the Dirty List, ensuring criminal prosecution of "
            "slave labour offenders, preventing impunity) remain incomplete. "
            "Civil society groups report that many structural reforms ordered "
            "by the Court have stalled, and they continue to submit monitoring "
            "reports to the Court documenting non-compliance."
        ),
        "source": "IACtHR / Reporter Brasil / ANAMATRA / OIT Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 13 — CONATRAE
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "CONATRAE — National Commission for the Eradication of Slave Labour",
        "summary": (
            "Created by Presidential Decree in 2003, CONATRAE coordinates "
            "federal anti-slavery policy. It is composed of government agencies "
            "(MTE, MPT, Policia Federal, IBAMA), civil society organizations "
            "(CPT, Reporter Brasil), employer associations, and workers' unions. "
            "CONATRAE developed both National Plans for the Eradication of "
            "Slave Labour and monitors their implementation. It also coordinates "
            "state-level commissions (COETRAEs) in 25 of 27 states."
        ),
        "source": "Presidencia da Republica / CONATRAE / SDH",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "State-Level Commissions (COETRAEs) — Decentralized Enforcement",
        "summary": (
            "CONATRAE promoted the creation of state-level commissions for the "
            "eradication of slave labour (COETRAEs) in all 27 Brazilian states. "
            "COETRAEs coordinate local enforcement, victim assistance, and "
            "prevention programs. Effectiveness varies widely: Para, Mato "
            "Grosso, and Maranhao have active commissions with dedicated "
            "budgets, while smaller states often have commissions that exist "
            "only on paper."
        ),
        "source": "CONATRAE / SDH / OIT Brasil",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "CONATRAE — Monitoring the National Plans",
        "summary": (
            "CONATRAE publishes biannual monitoring reports tracking progress "
            "on the National Plans for the Eradication of Slave Labour. As of "
            "2023, approximately 68% of the Second Plan's 66 targets have been "
            "fully or partially achieved. Key gaps include: insufficient victim "
            "reintegration programs, inadequate funding for the GEFM, and the "
            "continued legal vulnerability of the Dirty List to court challenges."
        ),
        "source": "CONATRAE / OIT Brasil / Reporter Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 14 — SEGURO-DESEMPREGO FOR RESCUED WORKERS
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Seguro-Desemprego for Rescued Workers — Law 10.608/2002",
        "summary": (
            "Law 10.608/2002 grants rescued slave labour victims the right to "
            "three monthly payments of the minimum wage (seguro-desemprego "
            "especial). This was the first law in the world to provide "
            "unemployment insurance specifically for freed slave labour victims. "
            "Between 2003 and 2022, over 55,000 workers received the benefit. "
            "Critics argue that three payments are insufficient for "
            "reintegration and that many workers are re-trafficked after the "
            "benefit period expires."
        ),
        "source": "Lei 10.608/2002 / MTE / DIEESE / OIT Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Recidivism Among Rescued Workers",
        "summary": (
            "Studies by Reporter Brasil and the ILO estimate that 30-40% of "
            "workers rescued from slave-like conditions are found in similar "
            "conditions again within 5 years. The high recidivism rate reflects "
            "inadequate reintegration: workers receive only three months of "
            "minimum-wage payments and are returned to the same conditions of "
            "poverty and lack of opportunity that made them vulnerable. The "
            "ILO recommends vocational training, land reform, and extended "
            "social protection to break the cycle."
        ),
        "source": "Reporter Brasil / OIT Brasil / MTE",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Proposed Enhancement of Rescued Worker Benefits",
        "summary": (
            "Multiple legislative proposals have sought to extend benefits for "
            "rescued workers beyond three months. PL 5.016/2005 proposed "
            "extending the seguro-desemprego to six months and adding "
            "vocational training. The bill passed the Senate but stalled in "
            "the House. Civil society advocates for a comprehensive "
            "reintegration package including housing assistance, skills "
            "training, psychosocial support, and priority access to Bolsa "
            "Familia and land reform programs."
        ),
        "source": "Senado Federal / PL 5.016/2005 / OIT Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 15 — TRT (REGIONAL LABOUR COURT) DECISIONS
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TRT-8 Para — Landmark Forced Labour Compensation Award",
        "summary": (
            "The Regional Labour Court of the 8th Region (Para/Amapa) has "
            "issued numerous decisions awarding collective moral damages "
            "(dano moral coletivo) in slave labour cases. In a 2012 ruling "
            "against a cattle rancher in Maraба, the court awarded BRL 2 "
            "million in collective damages plus individual compensation for "
            "each of 47 rescued workers. The decision established that slave "
            "labour constitutes an injury to society as a whole, justifying "
            "collective damages."
        ),
        "source": "TRT-8 / MPT-PA",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TRT-15 Campinas — Sugarcane Sector Compensation",
        "summary": (
            "The TRT-15 (Campinas, covering interior Sao Paulo) has ruled on "
            "multiple sugarcane cases. In a 2010 decision, the court ordered a "
            "sugar mill in Ribeirao Preto to pay BRL 1.5 million in collective "
            "damages after workers were found in degrading conditions: unsafe "
            "transportation, lack of toilets in the field, and piece-rate "
            "payment encouraging exhausting hours. The court held that "
            "agricultural employers bear strict liability for subcontractor "
            "violations under the rural labour code."
        ),
        "source": "TRT-15 Campinas / MPT-SP",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TRT-2 Sao Paulo — Garment Industry Joint Liability",
        "summary": (
            "The TRT-2 (Sao Paulo) has developed extensive jurisprudence on "
            "brand liability for slave labour in garment supply chains. In "
            "multiple decisions, the court held that fashion brands are jointly "
            "liable (responsabilidade solidaria) for labour violations at "
            "subcontractor workshops when the brand exerts economic control "
            "over production. Damages have ranged from BRL 500,000 to BRL 20 "
            "million depending on the scale of exploitation."
        ),
        "source": "TRT-2 Sao Paulo / MPT-SP",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TRT-3 Minas Gerais — Coffee Farm Decisions",
        "summary": (
            "The TRT-3 (Minas Gerais) has adjudicated numerous coffee farm "
            "slave labour cases. In a 2015 decision, the court awarded BRL "
            "800,000 in collective damages against a farm in the Sul de Minas "
            "region where 23 workers were found without employment contracts, "
            "housed in a barn, and exposed to pesticides. The court noted that "
            "coffee's global supply chain creates an obligation for enhanced "
            "due diligence."
        ),
        "source": "TRT-3 Minas Gerais / MPT-MG",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 16 — MPT (MINISTRY OF PUBLIC LABOUR) ENFORCEMENT
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "MPT — Role in Combating Slave Labour",
        "summary": (
            "The Ministerio Publico do Trabalho (MPT) is the prosecutorial arm "
            "for labour rights enforcement. Its Coordenadoria Nacional de "
            "Erradicacao do Trabalho Escravo (CONAETE) coordinates slave "
            "labour prosecutions across all 24 regional offices. The MPT "
            "participates in GEFM operations, files civil public actions "
            "(acoes civis publicas) for collective damages, and negotiates "
            "TACs (Termos de Ajustamento de Conduta) requiring employers to "
            "adopt corrective measures."
        ),
        "source": "MPT / CONAETE / OIT Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "MPT Enforcement Statistics on Slave Labour",
        "summary": (
            "Between 2003 and 2023, the MPT filed over 2,500 civil public "
            "actions related to slave labour and negotiated over 4,000 TACs. "
            "Total collective damages awarded and TAC payments exceed BRL 1.5 "
            "billion. The largest single TAC was BRL 100 million against a "
            "major construction consortium. The MPT also operates the Disque "
            "100 hotline for slave labour denunciations, receiving over 3,000 "
            "complaints annually."
        ),
        "source": "MPT / CONAETE / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "MPT Action Against Vale S.A. — Mining Sector",
        "summary": (
            "The MPT filed civil public actions against Vale S.A. and its "
            "subcontractors for labour violations at mining operations in "
            "Para and Minas Gerais. Workers at subcontractor sites reported "
            "12-hour shifts without overtime pay, inadequate safety equipment "
            "in underground operations, and housing in containers without "
            "ventilation. The MPT secured a TAC requiring Vale to audit all "
            "subcontractors quarterly and assume joint liability for violations."
        ),
        "source": "MPT-PA / MPT-MG / Vale S.A.",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "MPT TAC with H&M — Supply Chain Accountability (2019)",
        "summary": (
            "Following GEFM findings of Bolivian workers in slave-like conditions "
            "at workshops producing for H&M in Sao Paulo, the MPT negotiated a "
            "TAC requiring H&M to: map its complete Brazilian supply chain, "
            "conduct unannounced audits, remediate all identified violations "
            "within 90 days, and contribute BRL 5 million to a worker "
            "reintegration fund. The TAC served as a model for subsequent "
            "brand accountability agreements."
        ),
        "source": "MPT-SP / Reporter Brasil / H&M Sustainability Report",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 17 — TST (SUPERIOR LABOUR COURT) LANDMARK RULINGS
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TST RR-178000 — Constitutionality of the Dirty List",
        "summary": (
            "The Tribunal Superior do Trabalho (TST) upheld the constitutionality "
            "of the Dirty List in multiple decisions, ruling that publication "
            "of employer names does not violate the presumption of innocence "
            "because listing follows an administrative (not criminal) proceeding "
            "with full due process. The TST emphasized that the list serves a "
            "legitimate public interest in combating slave labour."
        ),
        "source": "TST / MPT",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TST — Supply Chain Liability Doctrine",
        "summary": (
            "The TST has consolidated jurisprudence holding that companies at "
            "the top of supply chains bear subsidiary liability (responsabilidade "
            "subsidiaria) for slave labour found at supplier operations. In "
            "cases involving major retailers and agribusiness companies, the TST "
            "ruled that economic dependence between the brand and the "
            "subcontractor creates a duty of oversight that, when breached, "
            "triggers liability for damages and unpaid wages."
        ),
        "source": "TST / MPT / ANAMATRA",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TST E-RR 92900 — Collective Moral Damages for Slave Labour",
        "summary": (
            "The TST Plenary Section (Subseção I Especializada em Dissídios "
            "Individuais) ruled that slave labour constitutes a violation of the "
            "social order justifying collective moral damages (dano moral "
            "coletivo) independent of individual claims. The court held that "
            "slavery-analogous conditions harm the dignity of the entire working "
            "class and society, permitting the MPT to seek damages on behalf of "
            "the collectivity even beyond individual worker compensation."
        ),
        "source": "TST / SBDI-1 / MPT",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TST — Burden of Proof in Rural Slave Labour Cases",
        "summary": (
            "The TST has ruled that in rural slave labour cases, the burden of "
            "proof shifts to the employer to demonstrate compliance with labour "
            "standards once the MPT presents prima facie evidence of degrading "
            "conditions. This reversed the traditional burden requiring workers "
            "to prove each element of exploitation, recognizing the extreme "
            "power asymmetry and information inequality in rural employment."
        ),
        "source": "TST / MPT / ANAMATRA",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 18 — MINING SECTOR EXPLOITATION
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Illegal Gold Mining (Garimpo) — Forced Labour in the Amazon",
        "summary": (
            "Illegal gold mining (garimpo) in the Amazon involves widespread "
            "forced labour. Workers, often recruited from indigenous communities "
            "and impoverished towns, are transported to remote mining sites where "
            "they work waist-deep in mercury-contaminated water. Escape is "
            "nearly impossible due to remoteness. In 2020, the Policia Federal "
            "dismantled a garimpo operation in Roraima holding 45 workers in "
            "slave-like conditions, controlled by armed guards."
        ),
        "source": "Policia Federal / MTE / IBAMA / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Iron Ore Mining Supply Chain — Subcontractor Exploitation",
        "summary": (
            "Brazil's iron ore mining sector (Carajas, Quadrilatero Ferrifero) "
            "relies on layers of subcontractors for excavation, transport, and "
            "processing. The MPT has documented slave-like conditions at "
            "subcontractor operations: workers in open-pit mines without safety "
            "harnesses, 14-hour shifts in extreme heat, and housing in shipping "
            "containers. Major miners (Vale, CSN, Usiminas) have been held "
            "subsidiarily liable for subcontractor violations."
        ),
        "source": "MPT / MTE / SINAIT / BWI",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Gemstone Mining in Minas Gerais — Informal Exploitation",
        "summary": (
            "Small-scale gemstone mining in Minas Gerais (emeralds, tourmaline, "
            "topaz) involves informal workers who receive no employment "
            "contracts, safety equipment, or social security. In Teofilo Otoni, "
            "the MTE found miners working in unstable tunnels without "
            "ventilation, earning only a share of found stones (meia-praca "
            "system). Tunnel collapses kill an estimated 10-20 miners per year, "
            "though most deaths go unreported."
        ),
        "source": "MTE / MPT-MG / CPT / DNPM",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Cassiterite (Tin Ore) Mining — Amazonas and Rondonia",
        "summary": (
            "Cassiterite mining in the Amazon basin has been linked to forced "
            "labour. Workers in remote mines in Amazonas and Rondonia are "
            "recruited with advance payments that become debts. Access to "
            "mining sites requires days of river travel, preventing workers "
            "from leaving. In 2016, the GEFM rescued 23 workers from a "
            "cassiterite operation in Rondonia controlled by armed overseers. "
            "Brazilian tin enters global electronics supply chains."
        ),
        "source": "MTE / Policia Federal / Reporter Brasil / IPAM",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 19 — AGRICULTURAL FRONTIER AND DEFORESTATION-LINKED ABUSE
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Soy Expansion and Slave Labour — MATOPIBA Region",
        "summary": (
            "The MATOPIBA agricultural frontier (Maranhao, Tocantins, Piaui, "
            "Bahia) has experienced rapid soy expansion accompanied by slave "
            "labour. Workers clear native Cerrado vegetation for soy planting, "
            "often in conditions analogous to slavery. Between 2010 and 2022, "
            "over 1,200 workers were rescued from soy and associated operations "
            "in MATOPIBA. Land grabbing (grilagem) from traditional communities "
            "exacerbates the vulnerability of displaced populations."
        ),
        "source": "CPT / MTE / Reporter Brasil / IBAMA",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Deforestation-Slave Labour Correlation — Para and Mato Grosso",
        "summary": (
            "Academic studies (by Theresa Williamson, Sakamoto et al.) have "
            "established a strong correlation between deforestation rates and "
            "slave labour rescues in the Amazon. Municipalities with the highest "
            "deforestation rates consistently show the highest numbers of rescued "
            "workers. The deforestation-cattle-slave labour nexus is driven by "
            "economic incentives: cheap land plus cheap labour maximizes profit "
            "from pasture expansion."
        ),
        "source": "Reporter Brasil / Leonardo Sakamoto / INPE / CPT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Palm Oil Expansion in Para — Indigenous Land and Labour Exploitation",
        "summary": (
            "Palm oil plantations in northeastern Para have expanded onto "
            "indigenous and quilombola territories. Workers from Maranhao "
            "recruited for plantation work report degrading conditions: "
            "pesticide exposure without PPE, 12-hour days, and housing in "
            "open-sided barracks. In 2014, the GEFM rescued 48 workers from "
            "a palm oil operation in Tome-Acu where wages had not been paid "
            "for 4 months."
        ),
        "source": "MTE / CPT / FASE / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Cotton Production in Western Bahia — Seasonal Worker Exploitation",
        "summary": (
            "Western Bahia's cotton farms rely on seasonal migrant workers for "
            "planting and harvesting. The MPT has documented cases of workers "
            "transported 1,000+ km from Maranhao and Piaui, housed in "
            "improvised shelters in the field, provided no drinking water "
            "separate from irrigation channels, and paid below minimum wage "
            "with illegal deductions. In 2018, 62 workers were rescued from "
            "a cotton operation in Barreiras."
        ),
        "source": "MTE / MPT-BA / Reporter Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Geographic Distribution of Slave Labour Rescues — Origin States",
        "summary": (
            "Analysis of GEFM data reveals that rescued workers predominantly "
            "originate from the poorest states: Maranhao (23% of all rescued "
            "workers), Bahia (12%), Piaui (10%), Tocantins (8%), and Para (7%). "
            "These states have the lowest HDI scores in Brazil. Workers are "
            "recruited to work in destination states: Para, Mato Grosso, Goias, "
            "Sao Paulo, and Minas Gerais. The origin-destination pattern mirrors "
            "historical internal migration flows."
        ),
        "source": "MTE / DIEESE / OIT Brasil / IBGE",
    },
    # ════════════════════════════════════════════════════════════════════
    #  PART 20 — HAITIAN AND VENEZUELAN MIGRANT EXPLOITATION
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Haitian Migrants in Brazil — Post-2010 Earthquake Exploitation",
        "summary": (
            "Following the 2010 Haiti earthquake, over 100,000 Haitians migrated "
            "to Brazil. Many found work in construction, meatpacking, and "
            "services under exploitative conditions. In 2013, 100 Haitian "
            "workers were rescued from a construction site in Minas Gerais "
            "where they worked 14-hour days, received below minimum wage, and "
            "were housed in a warehouse. Language barriers and irregular "
            "immigration status exacerbated vulnerability."
        ),
        "source": "MTE / MPT / CONARE / OIM Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Haitian Workers in Brazilian Meatpacking Plants",
        "summary": (
            "Haitian workers in meatpacking plants in southern Brazil "
            "(Parana, Santa Catarina, Rio Grande do Sul) report excessive "
            "hours, repetitive strain injuries, racial discrimination, and "
            "below-standard wages compared to Brazilian co-workers. In 2015, "
            "the MPT investigated a JBS plant in Passo Fundo where Haitian "
            "workers on the processing line worked 10-hour shifts in "
            "near-freezing conditions without adequate protective clothing."
        ),
        "source": "MPT-RS / Reporter Brasil / CAMI",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Venezuelan Migrants in Roraima — Exploitation at the Border",
        "summary": (
            "Since 2017, over 400,000 Venezuelans have entered Brazil through "
            "Roraima. Many face exploitation in Boa Vista and Pacaraima: "
            "domestic work without pay, sex trafficking, street vending under "
            "control of intermediaries, and construction work for below "
            "minimum wage. In 2019, the GEFM rescued 18 Venezuelan workers "
            "from a construction site in Manaus where they were paid BRL "
            "20/day (one-fifth of minimum wage) and housed in an unfinished "
            "building without water or electricity."
        ),
        "source": "MTE / MPT-RR / ACNUR Brasil / OIM Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Venezuelan Women — Sex Trafficking in Northern Brazil",
        "summary": (
            "Venezuelan women and girls have been trafficked for sexual "
            "exploitation in Roraima, Amazonas, and Para. Criminal networks "
            "recruit women in Venezuelan border towns with promises of "
            "waitressing or domestic work. Victims are transported to "
            "brothels in Boa Vista, Manaus, and Belem, have documents "
            "confiscated, and are forced to repay fabricated debts. The "
            "Policia Federal dismantled 12 such networks between 2018 and 2022."
        ),
        "source": "Policia Federal / MPF / ACNUR / Reporter Brasil",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Operacao Acolhida — Venezuelan Refugee Relocation and Labour Integration",
        "summary": (
            "Operacao Acolhida (Operation Welcome), launched in 2018, is a "
            "federal program to manage Venezuelan migration. It includes "
            "temporary shelters in Roraima and a voluntary relocation program "
            "('interiorizacao') to cities across Brazil. While the program has "
            "relocated over 100,000 Venezuelans, relocated migrants remain "
            "vulnerable to exploitation in destination cities where they lack "
            "social networks. Labour market integration has been slow, with "
            "many qualified professionals working in informal, low-wage jobs."
        ),
        "source": "Casa Civil / ACNUR / OIM / Exercito Brasileiro",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Haitian and Senegalese Migrants — Poultry Processing Exploitation",
        "summary": (
            "Haitian and Senegalese migrants in poultry processing plants in "
            "southern Brazil face disproportionate injury rates and wage "
            "violations. A 2020 MPT investigation of BRF plants in Santa "
            "Catarina found that African and Haitian workers were concentrated "
            "in the most dangerous positions (deboning, evisceration) and "
            "suffered repetitive strain injuries at twice the rate of "
            "Brazilian workers. Language barriers prevented workers from "
            "reporting injuries or understanding safety protocols."
        ),
        "source": "MPT-SC / Reporter Brasil / CAMI / OIT Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  ADDITIONAL TOPICS — PACTO NACIONAL, CIVIL SOCIETY, STATISTICS
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Pacto Nacional pela Erradicacao do Trabalho Escravo (2005)",
        "summary": (
            "The National Pact for the Eradication of Slave Labour is a "
            "voluntary business initiative launched by the ILO, InPACTO, and "
            "the Ethos Institute. Over 500 companies have signed, committing "
            "to not purchase from Dirty List employers and to monitor supply "
            "chains. Signatories include Walmart Brazil, Carrefour, JBS, and "
            "major banks. The Pact is considered a model public-private "
            "anti-slavery initiative and has been replicated in other countries."
        ),
        "source": "InPACTO / OIT Brasil / Instituto Ethos",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Reporter Brasil — Investigative Journalism and Transparency",
        "summary": (
            "Reporter Brasil is a non-profit investigative journalism "
            "organization that has been central to exposing slave labour "
            "since 2001. Its investigations have linked major international "
            "brands to slave-labour supply chains, tracked Dirty List data, "
            "and provided evidence for MPT prosecutions. Reporter Brasil "
            "also operates the 'Slavery Monitor' database tracking rescues, "
            "prosecutions, and Dirty List entries. Leonardo Sakamoto, its "
            "founder, serves on CONATRAE."
        ),
        "source": "Reporter Brasil / OIT Brasil / CPT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Comissao Pastoral da Terra (CPT) — Denunciation and Victim Support",
        "summary": (
            "The CPT (Pastoral Land Commission), linked to the Catholic Church, "
            "has been the primary channel for slave labour denunciations since "
            "the 1970s. CPT agents in rural areas identify and report slave "
            "labour to the GEFM, provide initial assistance to rescued workers, "
            "and accompany victims through legal proceedings. The CPT's annual "
            "Conflitos no Campo report tracks slave labour, land conflicts, and "
            "violence against rural workers."
        ),
        "source": "CPT / CNBB / OIT Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Profile of Rescued Workers — Demographics",
        "summary": (
            "Analysis of 60,000+ rescued workers (1995-2023) shows: 95% male, "
            "72% Black or mixed race, average age 32, average education 4 years "
            "of schooling, 37% illiterate or functionally illiterate. The "
            "typical victim is a young Black man from Maranhao or Bahia with "
            "minimal education recruited for agricultural work in Para or Mato "
            "Grosso. Female victims are concentrated in domestic work and "
            "textile sectors."
        ),
        "source": "MTE / DIEESE / OIT Brasil / Reporter Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Slave Labour Rescues by Sector (1995-2023)",
        "summary": (
            "Cumulative rescue data by sector: cattle ranching 28%, sugarcane "
            "15%, charcoal 9%, construction 12%, coffee 6%, soy 5%, cotton 4%, "
            "textiles/garments 5%, domestic work 3%, mining 3%, other "
            "agriculture 7%, other 3%. Urban rescues have increased from 5% of "
            "the total in 2003 to over 35% in 2022, reflecting growing "
            "detection of exploitation in construction, garments, and services."
        ),
        "source": "MTE / DIEESE / Reporter Brasil / OIT Brasil",
    },
    {
        "type": "advisory",
        "jurisdiction": "BR",
        "title": "ILO Recognition of Brazil's Anti-Slavery Model",
        "summary": (
            "The ILO has consistently recognized Brazil as a global reference "
            "for combating forced labour. Key innovations cited: the expanded "
            "legal definition of slave labour (Article 149), the Dirty List "
            "as an economic deterrent, the GEFM mobile inspection model, and "
            "the seguro-desemprego for rescued workers. The ILO has facilitated "
            "knowledge transfer from Brazil to other countries including "
            "Argentina, Bolivia, Peru, and Mozambique."
        ),
        "source": "OIT / ILO Global Report on Forced Labour / ILO Brazil Office",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Uber and App-Based Delivery Worker Exploitation Debate",
        "summary": (
            "A growing debate in Brazil concerns whether app-based delivery and "
            "ride-hail workers (Uber, iFood, Rappi) experience conditions "
            "analogous to slave labour. The MPT has investigated cases of "
            "12-16 hour days, earnings below minimum wage after expenses, and "
            "algorithmic control constituting subordination. In 2022, a Sao "
            "Paulo labour judge controversially applied Article 149 concepts "
            "to a delivery platform case, though the decision was overturned "
            "on appeal."
        ),
        "source": "MPT-SP / TRT-2 / Reporter Brasil / DIEESE",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Lei 14.457/2022 — Employment and Opportunity for Women Program",
        "summary": (
            "While primarily addressing women's employment, Law 14.457/2022 "
            "includes provisions relevant to preventing domestic worker "
            "exploitation: mandatory harassment prevention programs at "
            "companies with 20+ employees, and strengthened protections for "
            "women returning from maternity leave. The law complements PEC "
            "das Domesticas by addressing gender-based vulnerabilities that "
            "facilitate labour exploitation of women."
        ),
        "source": "Lei 14.457/2022 / Diario Oficial da Uniao",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Onion Harvest Exploitation — Sao Paulo and Minas Gerais",
        "summary": (
            "Onion farming in the Piedade (SP) and Monte Azul (MG) regions "
            "relies on migrant workers in conditions frequently found analogous "
            "to slavery. In 2021, 25 workers were rescued from an onion farm "
            "in Piedade where they slept in a shed with no walls, cooked over "
            "open fires, and were paid BRL 3 per sack of onions harvested. "
            "The gato who recruited them from Bahia had charged BRL 200 for "
            "bus transport, creating initial debt."
        ),
        "source": "MTE / MPT-SP / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Acai Berry Harvesting — Forced Labour in Para",
        "summary": (
            "The booming global demand for acai has created exploitation in "
            "Para's acai groves. Workers climb 20-metre palm trees without "
            "safety equipment, work 12-hour days, and earn BRL 30-50/day with "
            "deductions. In 2019, the MTE found 17 acai harvesters in "
            "slave-like conditions near Abaetetuba: no employment contracts, "
            "no safety equipment (falls are the leading cause of worker death "
            "in acai harvesting), and wages paid in kind rather than cash."
        ),
        "source": "MTE / MPT-PA / Reporter Brasil / CPT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Tobacco Farming — Forced Labour in Rio Grande do Sul",
        "summary": (
            "Tobacco farming in southern Brazil involves integrated production "
            "systems where smallholders contract with multinational tobacco "
            "companies (Souza Cruz/BAT, Philip Morris, JTI). The system "
            "creates debt bondage: farmers take loans for inputs and must sell "
            "exclusively to the contracting company at company-set prices. "
            "Families, including children, work 12-hour days during harvest. "
            "The MPT has pursued tobacco companies for labour violations in "
            "their integrated supply chains."
        ),
        "source": "MPT-RS / Reporter Brasil / WHO FCTC / OIT Brasil",
    },
    {
        "type": "contact",
        "jurisdiction": "BR",
        "title": "Disque 100 — National Hotline for Human Rights Violations",
        "summary": (
            "Disque 100 (Dial 100) is Brazil's national hotline for reporting "
            "human rights violations, including slave labour and trafficking. "
            "Operated by the Ministry of Human Rights, it receives approximately "
            "3,000 slave labour denunciations annually. Calls are free, "
            "available 24/7, and can be made anonymously. Reports are forwarded "
            "to the MTE, MPT, and Policia Federal for investigation."
        ),
        "source": "Ministerio dos Direitos Humanos / SDH / MTE",
    },
    {
        "type": "contact",
        "jurisdiction": "BR",
        "title": "MPT Denunciation Channels — Reporting Slave Labour",
        "summary": (
            "The MPT accepts slave labour denunciations through: (1) online "
            "portal (mpt.mp.br), (2) MPT app (Pardal Trabalhista), (3) in-person "
            "at any of 24 regional offices, and (4) through partner "
            "organizations (CPT, unions, NGOs). The MPT guarantees anonymity "
            "for complainants and prioritizes cases with indicators of ongoing "
            "exploitation for immediate GEFM mobilization."
        ),
        "source": "MPT / CONAETE",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "COVID-19 Pandemic — Increased Vulnerability to Slave Labour",
        "summary": (
            "The COVID-19 pandemic exacerbated slave labour vulnerability in "
            "Brazil. GEFM inspections were suspended for 3 months in 2020, "
            "creating an enforcement gap. Economic crisis pushed more workers "
            "into informal employment. Rescued worker numbers dropped to 936 "
            "in 2020 (lowest since 2002), not due to reduced exploitation but "
            "reduced detection. Post-pandemic rescues surged: 1,937 in 2022 "
            "and over 3,000 in 2023, suggesting accumulated cases."
        ),
        "source": "MTE / Reporter Brasil / OIT Brasil / CONATRAE",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Vineyards in Rio Grande do Sul — Wine Sector Slave Labour (2023)",
        "summary": (
            "In February 2023, the GEFM rescued 207 workers from vineyards in "
            "Bento Goncalves, Rio Grande do Sul, in one of the largest rescue "
            "operations in recent years. Workers from Bahia harvested grapes "
            "for major wineries (Aurora, Salton, Garibaldi cooperatives). They "
            "were housed in cramped, unsanitary barracks, beaten by overseers, "
            "had wages withheld, and were pepper-sprayed when they protested. "
            "The case generated national outrage and led to arrests."
        ),
        "source": "MTE / MPT-RS / Policia Federal / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Winery Worker Rescue Aftermath — Industry Response (2023)",
        "summary": (
            "Following the Bento Goncalves vineyard rescue, the Brazilian wine "
            "industry faced boycott threats and international scrutiny. The "
            "Aurora cooperative, implicated as a buyer, lost export contracts "
            "in Europe. The Rio Grande do Sul government created an emergency "
            "task force. The MPT secured TACs worth BRL 7 million from "
            "implicated companies. The case reignited debate on implementing "
            "Constitutional Amendment 81 (property expropriation)."
        ),
        "source": "MPT-RS / Reporter Brasil / Cooperativa Aurora / TRT-4",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Criminal Prosecution Gap — Impunity for Slave Labour",
        "summary": (
            "Despite over 60,000 workers rescued since 1995, criminal "
            "convictions under Article 149 remain rare. As of 2023, fewer "
            "than 200 individuals have been criminally convicted. The MPT "
            "reports that the average time between rescue and criminal trial "
            "is 8-12 years, with many cases prescribed (statute of limitations). "
            "This impunity gap was a central finding in the IACtHR Brasil Verde "
            "judgment and remains the most critical weakness in Brazil's "
            "anti-slavery system."
        ),
        "source": "MPT / MPF / ANAMATRA / OIT Brasil / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Fishing Sector — Forced Labour in Amazonian Fisheries",
        "summary": (
            "Commercial fishing in the Amazon basin involves debt bondage "
            "patterns similar to land-based agriculture. Fishermen are advanced "
            "supplies (fuel, ice, nets) by boat owners and must repay from "
            "their catch. When catches are poor, debts accumulate across "
            "seasons. In 2017, the MTE found 34 fishermen on the Solimoes "
            "River working without contracts, living on boats for weeks, and "
            "earning below minimum wage after debt deductions."
        ),
        "source": "MTE / MPT-AM / CPT / Reporter Brasil",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "NR-31 — Occupational Safety in Agriculture and Livestock",
        "summary": (
            "Regulatory Norm 31 (NR-31) establishes mandatory occupational "
            "health and safety standards for agricultural and livestock work. "
            "Requirements include: potable water, sanitary facilities, shade "
            "for rest, PPE for pesticide handling, safe transportation, and "
            "first aid kits. Violations of NR-31 are central to GEFM findings "
            "of degrading conditions under Article 149. However, enforcement "
            "is undermined by the vast geographic area and limited number of "
            "labour inspectors."
        ),
        "source": "MTE / NR-31 / SINAIT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Yerba Mate Harvesting — Exploitation in Mato Grosso do Sul",
        "summary": (
            "Yerba mate harvesting in Mato Grosso do Sul involves indigenous "
            "workers (Guarani-Kaiowa, Terena) in conditions analogous to "
            "slavery. In 2015, 27 indigenous workers were rescued from a yerba "
            "mate operation in Amambai where they worked 10-hour days, were "
            "paid BRL 10/day, and lived in makeshift shelters. The exploitation "
            "is linked to the dispossession of indigenous lands for "
            "agribusiness, forcing communities into dependent labour."
        ),
        "source": "MTE / FUNAI / MPT-MS / CIMI",
    },
    {
        "type": "advisory",
        "jurisdiction": "BR",
        "title": "US TIP Report Assessment of Brazil",
        "summary": (
            "The US State Department's Trafficking in Persons (TIP) Report has "
            "consistently placed Brazil on the Tier 2 Watch List or Tier 2. "
            "The report acknowledges Brazil's strong legal framework and the "
            "Dirty List as innovative, but criticizes low criminal prosecution "
            "rates, insufficient victim services, and the impact of budget "
            "cuts on enforcement. The 2023 report specifically noted concerns "
            "about Venezuelan migrant exploitation and impunity for sex "
            "trafficking offenders."
        ),
        "source": "US Department of State / TIP Report",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Paraguayan Workers in Brazilian Border Farms",
        "summary": (
            "Paraguayan workers are exploited on farms in Mato Grosso do Sul "
            "and Parana near the border. In 2018, the GEFM rescued 31 "
            "Paraguayan workers from a soy farm in Dourados where they entered "
            "Brazil without documentation, were promised BRL 80/day but paid "
            "BRL 30 after deductions, and were housed in a barn without "
            "electricity. Cross-border recruitment complicates enforcement "
            "as workers often return to Paraguay before investigations conclude."
        ),
        "source": "MTE / MPT-MS / Policia Federal / OIM",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "CLT Article 462 — Prohibition of Coercive Wage Deductions",
        "summary": (
            "Article 462 of the Consolidation of Labour Laws (CLT) prohibits "
            "employers from making deductions from wages except as authorized "
            "by law or collective agreement. This provision is critical in "
            "slave labour cases where the truck system (sistema de barracao) "
            "creates debt bondage through wage deductions for food, tools, "
            "and housing at inflated prices. Violation of Article 462 is a "
            "key indicator used by GEFM inspectors."
        ),
        "source": "CLT / Decreto-Lei 5.452/1943 / MTE",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Brick Kiln Slave Labour — Piaui and Maranhao",
        "summary": (
            "Artisanal brick kilns (olarias) in Piaui and Maranhao are "
            "persistent sites of slave labour. Workers, including entire "
            "families with children, produce bricks by hand in extreme heat, "
            "live adjacent to kilns in mud-brick shelters, and are paid per "
            "thousand bricks at rates that barely cover subsistence. In 2020, "
            "the GEFM rescued 14 workers including 3 adolescents from a brick "
            "kiln in Timon, Maranhao."
        ),
        "source": "MTE / MPT-MA / CPT / Reporter Brasil",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "BNDES Social Clause — Credit Conditionality",
        "summary": (
            "Brazil's National Development Bank (BNDES) incorporates a social "
            "clause in its financing agreements: borrowers found on the Dirty "
            "List may have loans recalled and become ineligible for future "
            "BNDES financing. Given that BNDES is the primary source of "
            "long-term industrial and agricultural credit in Brazil, this "
            "clause is a powerful deterrent. Between 2005 and 2023, BNDES "
            "denied or recalled over BRL 400 million in credit to Dirty List "
            "employers."
        ),
        "source": "BNDES / MTE / InPACTO",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Motorcycle Delivery Workers — Urban Forced Labour Expansion",
        "summary": (
            "Urban slave labour identification has expanded to include "
            "motorcycle delivery workers controlled by criminal networks. In "
            "Sao Paulo and Rio de Janeiro, workers are recruited to deliver "
            "goods (including drugs) under conditions of debt bondage: they "
            "must rent motorcycles at inflated rates, meet daily delivery "
            "quotas, and face violence for non-compliance. The MPT is "
            "developing legal frameworks to address this emerging form of "
            "forced labour."
        ),
        "source": "MPT-SP / MPT-RJ / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Chinese Workers in Brazilian Restaurants — Sao Paulo",
        "summary": (
            "Chinese migrants in Sao Paulo's Liberdade district have been "
            "found in slave-like conditions in restaurants and shops. In 2016, "
            "the MTE rescued 12 Chinese workers from a restaurant in the "
            "Liberdade neighbourhood where they worked 16-hour days, lived in "
            "the restaurant basement, had passports confiscated, and spoke no "
            "Portuguese. Recruitment networks in Fujian province facilitated "
            "their entry with tourist visas and placed them in debt bondage."
        ),
        "source": "MTE / MPT-SP / Policia Federal / Reporter Brasil",
    },
    # ════════════════════════════════════════════════════════════════════
    #  ADDITIONAL ENTRIES — REACHING 150+ FACTS
    # ════════════════════════════════════════════════════════════════════
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Lei 13.344/2016 — Brazilian Anti-Trafficking Law",
        "summary": (
            "Law 13.344/2016 replaced earlier anti-trafficking provisions and "
            "aligned Brazilian law with the Palermo Protocol. It criminalizes "
            "all forms of trafficking including for labour exploitation, with "
            "penalties of 4-8 years imprisonment (increased to 12 years with "
            "aggravating factors). The law also establishes victim assistance "
            "obligations, including shelter, health care, legal aid, and "
            "regularization of immigration status. It created the National "
            "Policy for Combating Trafficking in Persons."
        ),
        "source": "Lei 13.344/2016 / Diario Oficial da Uniao / UNODC",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TRF-1 — Federal Court Conviction for Cattle Ranch Slave Labour in Para",
        "summary": (
            "The Federal Regional Tribunal of the 1st Region (TRF-1) upheld "
            "the criminal conviction of a cattle rancher in southern Para for "
            "maintaining 67 workers in conditions analogous to slavery. The "
            "defendant received 6 years imprisonment under Article 149 plus "
            "fines. The TRF-1 affirmed that the rancher could not avoid "
            "liability by delegating recruitment to a gato, establishing that "
            "the landowner bears ultimate responsibility for conditions on the "
            "property."
        ),
        "source": "TRF-1 / MPF / Policia Federal",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Eucalyptus Plantation Slave Labour — Bahia and Minas Gerais",
        "summary": (
            "Eucalyptus plantations for cellulose and charcoal production in "
            "Bahia and Minas Gerais have been sites of repeated slave labour "
            "findings. Workers plant and harvest eucalyptus in degrading "
            "conditions: carrying heavy loads of seedlings over hilly terrain, "
            "exposed to herbicides, and housed in temporary camps without "
            "sanitation. In 2017, 42 workers were rescued from an eucalyptus "
            "operation in the Jequitinhonha Valley supplying a major cellulose "
            "company."
        ),
        "source": "MTE / MPT-MG / CPT / Reporter Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Annual Rescue Trends — 2020-2023 Recovery",
        "summary": (
            "After the pandemic low of 936 rescued workers in 2020, rescue "
            "numbers recovered sharply: 1,334 in 2021, 2,575 in 2022, and "
            "3,151 in 2023 — the highest number since 2009. The 2023 surge was "
            "driven by large operations in the wine sector (207 workers in "
            "Rio Grande do Sul), urban construction, and agriculture. The "
            "recovery reflects both accumulated exploitation during the "
            "pandemic and increased GEFM capacity under the Lula government."
        ),
        "source": "MTE / CONATRAE / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Sisal (Agave) Fibre Production — Child and Forced Labour in Bahia",
        "summary": (
            "Brazil is the world's largest sisal producer, concentrated in "
            "semi-arid Bahia. Sisal decorticating machines cause frequent "
            "hand and arm amputations among workers, including children. "
            "Families work 12-hour days for piece rates, earning BRL 20-40/day. "
            "The ILO and UNICEF estimate over 4,000 children worked in sisal "
            "production in the 2010s. The Programa de Erradicacao do Trabalho "
            "Infantil (PETI) has reduced but not eliminated the practice."
        ),
        "source": "OIT Brasil / UNICEF / MTE / PETI",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Instrucao Normativa 139/2018 — Procedures for GEFM Inspections",
        "summary": (
            "Normative Instruction 139/2018 from the MTE standardizes GEFM "
            "inspection procedures: teams must document all four Article 149 "
            "indicators, interview workers individually and confidentially, "
            "photograph conditions, and issue immediate release orders "
            "(autos de infracao) for workers in danger. The instruction also "
            "requires inspectors to calculate back wages and FGTS deposits "
            "owed to rescued workers on site."
        ),
        "source": "MTE / Instrucao Normativa 139/2018 / SINAIT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Recycling Cooperatives — Urban Slave Labour in Sao Paulo",
        "summary": (
            "Informal recycling workers (catadores) in Sao Paulo face "
            "conditions analogous to forced labour when controlled by "
            "intermediaries who monopolize access to recyclable materials. "
            "In 2018, the MTE found 22 recycling workers in the Zona Leste "
            "working 14-hour days sorting materials in a warehouse without "
            "ventilation, paid BRL 15/day, and unable to leave due to debt "
            "for housing provided by the warehouse owner."
        ),
        "source": "MTE / MPT-SP / MNCR / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Rice Cultivation Slave Labour — Rio Grande do Sul",
        "summary": (
            "Rice farms in Rio Grande do Sul's Campanha Gaucha region have been "
            "sites of slave labour. Workers from Maranhao and Bahia are recruited "
            "for planting and harvesting. In 2016, 38 workers were rescued from "
            "rice paddies near Uruguaiana where they worked knee-deep in flooded "
            "fields without rubber boots, lived in a derelict shed, and had "
            "wages withheld for the duration of the harvest."
        ),
        "source": "MTE / MPT-RS / CPT",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Statute of the Child and Adolescent (ECA) — Article 60 Prohibition of Child Labour",
        "summary": (
            "The Estatuto da Crianca e do Adolescente (Law 8.069/1990) prohibits "
            "all work for children under 14 and restricts work for adolescents "
            "14-16 to apprenticeship programs. Despite this, IBGE estimates "
            "1.8 million children aged 5-17 were working in Brazil in 2019, "
            "many in agriculture (sugarcane, coffee, charcoal, sisal) in "
            "conditions that constitute forced child labour under ILO "
            "Convention 182."
        ),
        "source": "ECA / Lei 8.069/1990 / IBGE / OIT Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Marfrig Supply Chain — Cattle Linked to Slave Labour Ranches",
        "summary": (
            "Marfrig, Brazil's second-largest meatpacker, has been linked to "
            "cattle sourced from Dirty List ranches through intermediary farms. "
            "In 2019, an audit by the MPF found that Marfrig slaughterhouses "
            "in Mato Grosso purchased cattle from farms that had recently "
            "acquired animals from properties with active slave labour "
            "findings. Marfrig committed to blockchain-based traceability "
            "for its entire supply chain by 2025."
        ),
        "source": "MPF / Reporter Brasil / Marfrig / Mighty Earth",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Domestic Worker Rescue — Bahia Elderly Woman Held 72 Years",
        "summary": (
            "In 2022, an elderly woman was identified in Lauro de Freitas, "
            "Bahia, who had been in domestic servitude since childhood — "
            "approximately 72 years. Taken from an orphanage as a small "
            "child, she cooked, cleaned, and cared for the family's children "
            "and grandchildren without ever receiving wages, education, or "
            "identity documents. The case was referred to the MPT and "
            "highlighted the deep historical roots of domestic servitude "
            "in Brazilian society."
        ),
        "source": "MPT-BA / Reporter Brasil / OIT Brasil",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Policia Federal — Specialized Anti-Trafficking Units (DELETRAFs)",
        "summary": (
            "The Brazilian Federal Police operates specialized anti-trafficking "
            "units (Delegacias de Repressao ao Trafico de Pessoas — DELETRAFs) "
            "in major cities. DELETRAFs investigate international and domestic "
            "trafficking for labour and sexual exploitation. Between 2018 and "
            "2023, DELETRAFs conducted over 200 operations, dismantling "
            "trafficking networks and arresting over 400 suspects. However, "
            "conviction rates remain low due to slow judicial proceedings."
        ),
        "source": "Policia Federal / MJ / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Meat Processing Workers — Excessive Overtime in Goias",
        "summary": (
            "Meatpacking plants in Goias have been cited for excessive overtime "
            "amounting to exhausting hours under Article 149. In 2018, the MPT "
            "found workers at a plant in Goiania working 16-hour shifts during "
            "peak demand, standing on cold concrete floors in temperatures below "
            "10C, with only one 15-minute break. Workers developed chronic "
            "musculoskeletal disorders. The MPT secured a TAC worth BRL 8 "
            "million and mandatory shift reductions."
        ),
        "source": "MPT-GO / MTE / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Carnival Float Construction — Slave Labour in Rio de Janeiro (2024)",
        "summary": (
            "In January 2024, GEFM inspectors found 16 workers in slave-like "
            "conditions constructing carnival floats in Rio de Janeiro's Cidade "
            "do Samba. Workers, recruited from the northeast, were welding and "
            "painting floats in shifts of 18+ hours without safety equipment, "
            "sleeping on the workshop floor, and paid below minimum wage. The "
            "case highlighted the exploitation hidden behind Brazil's most "
            "iconic cultural event."
        ),
        "source": "MTE / MPT-RJ / Reporter Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Gato (Labour Intermediary) Prosecution Rates",
        "summary": (
            "Gatos — informal labour recruiters — are central to the slave "
            "labour system but are rarely prosecuted. Of the estimated 5,000+ "
            "gatos active in Brazil, fewer than 300 have faced criminal charges "
            "since 2003. Gatos recruit workers with false promises, charge "
            "transport and advance fees that create debt, and deliver workers "
            "to exploitative employers. Their prosecution is complicated by "
            "their itinerant nature and the difficulty of proving their role "
            "beyond reasonable doubt."
        ),
        "source": "MPF / MTE / CPT / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Cashew Nut Processing — Forced Labour in Ceara and Rio Grande do Norte",
        "summary": (
            "Brazil's cashew processing industry, concentrated in Ceara and "
            "Rio Grande do Norte, relies on women workers who shell cashews "
            "by hand in small factories. Workers suffer from cashew shell "
            "liquid (CNSL) burns, earn piece rates of BRL 0.10-0.20 per kg, "
            "and work 10-12 hour days without PPE. In 2019, the MTE found "
            "degrading conditions at 5 processing plants in Mossoro, "
            "rescuing 28 workers."
        ),
        "source": "MTE / MPT-CE / Reporter Brasil / CPT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Flower Cultivation — Migrant Worker Exploitation in Sao Paulo",
        "summary": (
            "Flower farms in Holambra and Atibaia, Sao Paulo, employ migrant "
            "workers from the northeast in conditions that GEFM inspections "
            "have found analogous to slavery. Workers in greenhouses face "
            "extreme heat and pesticide exposure. In 2020, 19 workers from "
            "Bahia were rescued from a flower farm in Holambra where they "
            "lived in a shipping container, had no employment contracts, and "
            "earned BRL 25/day with deductions for accommodation."
        ),
        "source": "MTE / MPT-SP / Reporter Brasil",
    },
    {
        "type": "law",
        "jurisdiction": "BR",
        "title": "Decreto 9.440/2018 — National Policy to Combat Trafficking in Persons",
        "summary": (
            "Decree 9.440/2018 established the III National Plan to Combat "
            "Trafficking in Persons (2018-2022), with 58 targets across "
            "prevention, enforcement, victim assistance, and international "
            "cooperation. Key objectives include strengthening inter-agency "
            "coordination, improving victim identification protocols at "
            "borders, and expanding the network of specialized shelters. "
            "Implementation has been hampered by funding shortfalls and "
            "institutional turnover."
        ),
        "source": "Decreto 9.440/2018 / MJ / SNJ / OIM Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Shrimp Farming — Forced Labour in Northeastern Brazil",
        "summary": (
            "Shrimp farms (carcinicultura) in Rio Grande do Norte, Ceara, and "
            "Maranhao employ workers in conditions documented as analogous to "
            "slavery. Workers maintain shrimp ponds in remote coastal areas, "
            "work 12-hour shifts in standing water, and are exposed to "
            "chemicals. In 2017, the GEFM rescued 15 workers from a shrimp "
            "farm in Acarau, Ceara, where wages had been withheld for 2 "
            "months and workers were threatened with dismissal without pay "
            "if they complained."
        ),
        "source": "MTE / MPT-CE / Reporter Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Transgender Sex Trafficking — Sao Paulo to Europe Pipeline",
        "summary": (
            "Brazilian transgender women are trafficked to Europe (primarily "
            "Italy, Spain, and Portugal) for sexual exploitation. Networks "
            "promise gender-affirming procedures and modelling work. Victims "
            "arrive with debts for travel and silicone injections, and are "
            "forced into sex work in Milan, Madrid, and Lisbon to repay. "
            "The Policia Federal has dismantled several such networks, "
            "including Operacao Harpia (2019) which identified 47 victims."
        ),
        "source": "Policia Federal / MPF / OIM / Reporter Brasil",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "BR",
        "title": "Resolucao CNAS 109/2009 — Social Protection for Trafficking Victims",
        "summary": (
            "Resolution 109 of the National Social Assistance Council "
            "establishes the typology of social services including specialized "
            "shelters (abrigos) for trafficking victims. The resolution "
            "mandates psychosocial support, legal aid, vocational training, "
            "and family reunification services. Brazil operates approximately "
            "20 specialized shelters for trafficking victims, far below the "
            "estimated need. Most shelters are in state capitals, leaving "
            "rural victims without accessible services."
        ),
        "source": "CNAS / Resolucao 109/2009 / MDS / UNODC",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Manioc (Cassava) Processing — Forced Labour in Para",
        "summary": (
            "Manioc flour production (farinhadas) in rural Para involves "
            "families working in rudimentary processing houses under "
            "exploitative conditions. Workers peel, grate, and roast manioc "
            "over wood fires in enclosed spaces, suffering smoke inhalation "
            "and burn injuries. In 2018, the GEFM found 11 workers including "
            "4 adolescents at a farinhada in Braganca working 14-hour days "
            "for shared payment of BRL 50/day split among the entire group."
        ),
        "source": "MTE / MPT-PA / CPT",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Solar Panel Installation — Emerging Exploitation in Bahia",
        "summary": (
            "Brazil's expanding solar energy sector has generated new sites of "
            "labour exploitation. In 2022, the GEFM rescued 21 workers from a "
            "solar farm installation in Bom Jesus da Lapa, Bahia. Workers "
            "installed panels in 40C heat, worked 12-hour shifts without "
            "rest, and were housed in tents without potable water. The "
            "subcontracting chain had five layers between the workers and "
            "the energy company. This emerging sector mirrors exploitation "
            "patterns seen in construction."
        ),
        "source": "MTE / MPT-BA / Reporter Brasil",
    },
    {
        "type": "statistic",
        "jurisdiction": "BR",
        "title": "Dirty List — Economic Impact on Listed Employers",
        "summary": (
            "Studies by InPACTO estimate that Dirty List inclusion costs "
            "employers an average of BRL 2.5 million in lost credit access, "
            "supply chain exclusions, and reputational damage. For large "
            "agribusiness operations, the loss of BNDES credit and rural "
            "credit from Banco do Brasil can be existential. This economic "
            "pressure is considered the most effective deterrent: the rate "
            "of repeat offending among Dirty List employers who fully "
            "comply with remediation requirements is approximately 8%, "
            "compared to 35% for non-listed offenders."
        ),
        "source": "InPACTO / BNDES / Reporter Brasil / OIT Brasil",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Bolivian Community Self-Organization — CAMI Sao Paulo",
        "summary": (
            "The Centro de Apoio e Pastoral do Migrante (CAMI) in Sao Paulo "
            "has organized Bolivian garment workers to resist exploitation. "
            "CAMI provides Portuguese language classes, legal aid, and "
            "labour rights education. Through CAMI, Bolivian workers have "
            "formed cooperatives that negotiate directly with brands, "
            "cutting out exploitative workshop owners. The cooperative "
            "model has improved wages from BRL 0.10/garment to BRL 0.50 "
            "and provides social security registration."
        ),
        "source": "CAMI / Pastoral do Migrante / OIT Brasil",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "BR",
        "title": "TRT-4 Rio Grande do Sul — Vineyard Rescue Compensation (2023)",
        "summary": (
            "Following the 2023 Bento Goncalves vineyard rescue, the TRT-4 "
            "awarded individual compensation of BRL 100,000 per rescued "
            "worker for moral damages, plus back wages, FGTS deposits, and "
            "collective moral damages of BRL 5 million against the labour "
            "contractor. The court emphasized that the use of violence "
            "(beatings, pepper spray) elevated the case beyond degrading "
            "conditions to forced labour with physical coercion."
        ),
        "source": "TRT-4 / MPT-RS / Reporter Brasil",
    },
]
