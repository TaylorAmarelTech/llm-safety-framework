"""European migrant worker exploitation — EU framework, national cases, and enforcement."""

EUROPE_FACTS: list[dict] = [
    # ══════════════════════════════════════════════════════════════════════
    # EU-WIDE FRAMEWORK (30+ facts)
    # ══════════════════════════════════════════════════════════════════════

    # ── EU Anti-Trafficking Directive ────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Directive 2011/36/EU",
        "summary": "Establishes minimum rules for defining trafficking offences and penalties across EU Member States. Covers all forms of exploitation including labour exploitation, forced begging, and organ removal. Requires non-punishment of victims, provision of assistance and support, compensation mechanisms, and appointment of National Rapporteurs.",
        "source": "Official Journal of the European Union L 101/1",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "Revised EU Anti-Trafficking Directive 2024 — Expanded Scope",
        "summary": "European Parliament and Council agreed to revise Directive 2011/36/EU in 2024 to add forced marriage, illegal adoption, and exploitation of surrogacy as trafficking offences. Introduces mandatory penalties for knowingly using services of trafficking victims. Strengthens online recruitment prevention.",
        "source": "European Parliament legislative resolution 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Directive Transposition Status",
        "metric": "Member States fully transposing 2011/36/EU",
        "value": "27 of 27",
        "year": 2023,
        "summary": "All EU Member States have transposed the Anti-Trafficking Directive into national law, though implementation quality and enforcement vary significantly. European Commission infringement proceedings initiated against several states for incomplete transposition.",
        "source": "European Commission implementation reports",
    },

    # ── Employers' Sanctions Directive ───────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Employers' Sanctions Directive 2009/52/EC",
        "summary": "Prohibits employment of illegally staying third-country nationals. Requires employers to verify residence status before hiring. Establishes financial sanctions, criminal penalties for severe cases, and obligations to pay back wages to exploited workers. Member States must ensure complaint mechanisms exist.",
        "source": "Official Journal of the European Union L 168/24",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Employers' Sanctions Directive — Weak Enforcement Record",
        "summary": "European Commission evaluations found that most Member States rarely apply criminal penalties under the Directive. Labour inspections of sectors employing undocumented workers remain insufficient. Back-pay provisions are rarely enforced due to victims' fear of deportation, undermining the Directive's protective intent.",
        "source": "European Commission COM(2014) 286 final / FRA reports",
    },

    # ── CSDDD (Corporate Sustainability Due Diligence) ───────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Corporate Sustainability Due Diligence Directive (CSDDD) 2024",
        "summary": "Requires large EU companies and qualifying non-EU companies to identify, prevent, mitigate, and account for adverse human rights and environmental impacts in their operations and value chains. Covers forced labour, child labour, and exploitation. Establishes civil liability for failure to conduct adequate due diligence. Phased implementation starting 2027 for largest companies.",
        "source": "Directive (EU) 2024/1760",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "CSDDD — Scope and Thresholds",
        "summary": "CSDDD applies to EU companies with 1,000+ employees and EUR 450M+ net turnover (after political compromise reduced from original 500 employees / EUR 150M). Non-EU companies meeting turnover thresholds in EU markets also covered. Financial sector given transitional exclusion. SMEs affected indirectly through supply chain cascading requirements.",
        "source": "Council of the EU final text 2024",
    },

    # ── EU Forced Labour Import Ban ──────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Forced Labour Products Regulation 2024",
        "summary": "Prohibits placing on the EU market or exporting from it products made with forced labour, including state-imposed forced labour. Competent authorities can investigate and order withdrawal of products. Modelled partly on US Uyghur Forced Labor Prevention Act. Applies to all products regardless of origin, including EU-manufactured goods.",
        "source": "Regulation (EU) 2024/3015",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "EU Forced Labour Ban — Risk-Based Enforcement",
        "summary": "Regulation establishes a risk-based enforcement approach. Lead competent authority designated per Member State. European Commission to maintain a database of forced labour risk areas and products. Network of competent authorities coordinates cross-border investigations. Customs authorities empowered to detain suspected goods at EU borders. Full application expected from 2027.",
        "source": "European Commission guidance on Regulation 2024/3015",
    },

    # ── Seasonal Workers Directive ───────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Seasonal Workers Directive 2014/36/EU",
        "summary": "Establishes conditions of entry and residence for third-country nationals for seasonal employment (5-9 months in 12 months). Requires equal treatment with nationals on working conditions, pay, health and safety, and social security. Employers must provide evidence of adequate accommodation. Workers may change employer within the season.",
        "source": "Official Journal of the European Union L 94/375",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Seasonal Workers Directive — Implementation Gaps",
        "summary": "European Commission evaluation (2020) found significant shortcomings: many Member States failed to ensure equal treatment; accommodation standards rarely inspected; workers often tied to single employer in practice despite portability provisions; labour inspectorates lack resources to monitor agricultural sites. Exploitation remains systemic in agriculture across Southern and Central Europe.",
        "source": "European Commission COM(2020) 176 final",
    },

    # ── Eurostat Trafficking Statistics ───────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "Eurostat Registered Trafficking Victims (2021-2022)",
        "metric": "Registered victims of trafficking in EU Member States",
        "value": "7,217 (2022)",
        "year": 2022,
        "summary": "Eurostat data shows 7,217 registered victims in 2022 across EU-27. Labour exploitation accounts for approximately 28% of registered cases, sexual exploitation 56%. However, actual numbers estimated at 5-10 times higher due to underreporting. Women and girls constitute 68% of identified victims.",
        "source": "Eurostat / European Commission data collection on trafficking",
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "EU Labour Trafficking Convictions",
        "metric": "Convictions for labour trafficking across EU-27",
        "value": "Approximately 250-300 per year",
        "year": 2022,
        "summary": "Labour trafficking convictions remain extremely low relative to estimated victim numbers. Less than 2% of identified labour trafficking cases result in conviction. Average sentence across EU is 3-5 years. Impunity gap identified as critical by EU Anti-Trafficking Coordinator.",
        "source": "European Commission 4th Progress Report on Anti-Trafficking",
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "Intra-EU Trafficking — Internal Movement",
        "metric": "Share of trafficking victims who are EU citizens",
        "value": "Approximately 34%",
        "year": 2022,
        "summary": "One-third of registered trafficking victims in the EU are EU citizens, primarily from Romania, Bulgaria, and Hungary. Exploited within other EU states under free movement provisions. Labour trafficking of EU citizens concentrated in agriculture, construction, and domestic work. Schengen area facilitates movement but complicates cross-border investigations.",
        "source": "Eurostat / EU Anti-Trafficking Coordinator reports",
    },

    # ── Europol Operations ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Europol Joint Investigation Teams — Labour Trafficking",
        "summary": "Europol coordinates Joint Investigation Teams (JITs) across Member States for cross-border trafficking cases. Between 2019-2023, Europol supported over 40 JITs targeting labour trafficking networks, resulting in 500+ arrests. Key operations targeted construction, agriculture, and logistics exploitation networks spanning multiple EU countries.",
        "source": "Europol SOCTA 2021 / Europol annual reviews",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Operation Webmaster — Europol Cross-Border Trafficking",
        "summary": "Multi-country Europol-coordinated operation targeting online recruitment for labour exploitation. Dismantled networks using social media and job platforms to recruit workers from Eastern Europe for exploitation in Western European agriculture and food processing. Identified systematic document retention and wage theft patterns across five Member States.",
        "source": "Europol press releases / Eurojust coordination",
    },

    # ── EU Anti-Trafficking Coordinator ──────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Coordinator — Strategic Priorities 2024-2029",
        "summary": "EU Anti-Trafficking Coordinator sets strategic priorities including: strengthening identification of labour trafficking victims; addressing online recruitment; improving cross-border cooperation; enhancing data collection; mandatory due diligence enforcement. Reports highlight persistent gap between policy framework and on-the-ground implementation across Member States.",
        "source": "EU Anti-Trafficking Coordinator strategy documents",
    },
    {
        "type": "advisory",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Coordinator — Labour Exploitation Warning",
        "summary": "EU Anti-Trafficking Coordinator has repeatedly warned that labour trafficking is significantly underreported compared to sexual exploitation. Construction, agriculture, domestic work, food processing, and logistics identified as highest-risk sectors. Recommends increased labour inspectorate resources, whistleblower protection, and firewall between labour complaints and immigration enforcement.",
        "source": "EU Anti-Trafficking Coordinator annual reports",
    },

    # ── Schengen Vulnerabilities ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Schengen Free Movement — Exploitation Vulnerability",
        "summary": "Free movement within the Schengen area, while fundamental to EU integration, creates vulnerabilities for labour exploitation. Traffickers move victims between Member States to evade detection. Victims from Romania, Bulgaria, and Poland recruited under false promises and moved to Western European states. Lack of internal border controls means exploitation can occur across multiple jurisdictions without detection.",
        "source": "FRA / GRETA evaluations / Europol SOCTA",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Dublin Regulation and Trafficking Victim Identification",
        "summary": "Asylum seekers subject to Dublin transfers may be unidentified trafficking victims. GRETA reports note that trafficking indicators are frequently missed during Dublin proceedings. Some victims trafficked during or after transfer between Member States. European Court of Justice has ruled that Dublin transfers must consider trafficking risks.",
        "source": "GRETA evaluation reports / ECHR case law",
    },

    # ── Posted Workers Directive ─────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Posted Workers Directive 96/71/EC (Revised 2018/957)",
        "summary": "Regulates conditions for workers posted temporarily to another EU Member State by their employer. Revised in 2018 to establish equal pay for equal work principle. Workers posted for more than 12 months entitled to nearly all host-country employment conditions. Aims to prevent social dumping through exploitation of lower wage standards.",
        "source": "Directive (EU) 2018/957",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Posted Workers — Exploitation Through Subcontracting Chains",
        "summary": "Systematic exploitation of posted workers through multi-layered subcontracting. Workers from Romania, Poland, and Bulgaria posted to Western Europe through letterbox companies. Paid home-country wages while performing work alongside higher-paid local workers. Accommodation costs deducted, excessive hours required, and social security contributions unpaid. European Labour Authority (ELA) investigations reveal widespread violations.",
        "source": "European Labour Authority / European Trade Union Confederation reports",
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "Scale of Posted Worker Exploitation",
        "metric": "Estimated annual posted worker declarations in EU",
        "value": "Approximately 3 million",
        "year": 2023,
        "summary": "Around 3 million posting declarations per year across the EU. Labour inspectorates estimate 10-20% involve irregularities including underpayment, excessive hours, and poor accommodation. Construction, meat processing, and logistics are highest-risk sectors. Letterbox companies identified in up to 30% of investigated cases.",
        "source": "European Labour Authority / European Commission posting data",
    },

    # ── Additional EU-wide ───────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Victims' Rights Directive 2012/29/EU",
        "summary": "Establishes minimum standards for rights, support, and protection of victims of crime across EU Member States. Trafficking victims entitled to: individual assessment of protection needs; access to victim support services; right to compensation; protection during criminal proceedings; residence permit if cooperating with authorities (per Anti-Trafficking Directive).",
        "source": "Official Journal of the European Union L 315/57",
    },
    {
        "type": "advisory",
        "jurisdiction": "EU",
        "title": "FRA Report — Severe Labour Exploitation in EU",
        "summary": "EU Fundamental Rights Agency (FRA) report 'Severe labour exploitation: workers moving within or into the European Union' documents systemic exploitation patterns. Key findings: victims rarely report due to fear of losing employment/deportation; labour inspectorates under-resourced; criminal justice systems focus on sexual exploitation over labour trafficking; seasonal agriculture workers most vulnerable.",
        "source": "FRA 2015 / updated 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "European Labour Authority (ELA) — Cross-Border Enforcement",
        "summary": "ELA, established in 2019, coordinates joint inspections across Member States. Early operations targeted posted worker fraud in construction and road transport. Challenges include different national inspection protocols, language barriers, and limited enforcement powers. ELA can recommend but not mandate Member State action.",
        "source": "European Labour Authority annual activity reports",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "EU Single Permit Directive Revision 2024",
        "summary": "Revised Single Permit Directive strengthens protections for third-country workers. Introduces right to change employer without losing work permit, addressing a key vulnerability enabling exploitation. Workers can retain permits for up to three months while seeking new employment. Aims to reduce dependency on single employer that facilitates exploitation.",
        "source": "Directive (EU) 2024/1233",
    },
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "EU Agency for Fundamental Rights — COMPENDIUM on Labour Exploitation",
        "summary": "FRA maintains a compendium of promising practices to address severe labour exploitation across the EU. Covers: multi-agency cooperation; labour inspection methods; victim identification tools; access to justice and compensation; complaint mechanisms independent of immigration status. Updated regularly with Member State case studies.",
        "source": "FRA compendium on severe labour exploitation",
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "GRETA Evaluation Cycle Results — Labour Trafficking",
        "metric": "Council of Europe GRETA evaluations completed",
        "value": "47 states evaluated across 3 cycles",
        "year": 2024,
        "summary": "GRETA (Group of Experts on Action against Trafficking) evaluates Council of Europe states' compliance with the Anti-Trafficking Convention. Recurring findings: labour trafficking identification insufficient; victim compensation rarely awarded; National Referral Mechanisms need strengthening; labour inspectors require trafficking-specific training.",
        "source": "Council of Europe GRETA evaluation reports",
    },

    # ══════════════════════════════════════════════════════════════════════
    # ITALY (20+ facts)
    # ══════════════════════════════════════════════════════════════════════

    # ── Caporalato System ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Caporalato — Italian Gangmaster Exploitation System",
        "summary": "Caporalato is the illegal gangmaster system in Italian agriculture. Caporali (labour intermediaries) recruit migrant workers, transport them to farms, and extract fees from wages. Workers — primarily from Sub-Saharan Africa, Eastern Europe, and South Asia — are paid EUR 20-30 for 10-14 hour days. The caporale typically retains EUR 5-10 per worker per day. System is deeply embedded in Southern Italian agriculture, particularly tomato, citrus, and olive harvesting.",
        "source": "Ferrara & Ferrara (2017) / Oxfam Italy / FLAI-CGIL reports",
    },
    {
        "type": "law",
        "jurisdiction": "IT",
        "title": "Italian Anti-Caporalato Law 199/2016",
        "summary": "Law 199/2016 significantly strengthened penalties for caporalato and labour exploitation in agriculture. Criminalizes not only the gangmaster but also the employer who uses caporale-recruited labour. Penalties: 1-6 years imprisonment and fines of EUR 500-1,000 per exploited worker. Enables confiscation of assets and company administration by judicial commissioners. Applies to any sector, not limited to agriculture.",
        "source": "Gazzetta Ufficiale della Repubblica Italiana, Law 199/2016",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "IT",
        "title": "Anti-Caporalato Law — Implementation Challenges",
        "summary": "Despite Law 199/2016, enforcement remains inconsistent. By 2023, fewer than 200 convictions secured under the new provisions. Agricultural lobby resistance, insufficient labour inspectors (Italy has approximately 4,500 for 60+ million population), and complicity of local authorities cited as barriers. FLAI-CGIL reports that the caporalato system continues in Puglia, Calabria, and Sicily with near impunity in some areas.",
        "source": "FLAI-CGIL / Italian Ministry of Labour reports / GRETA Italy evaluation",
    },

    # ── Agricultural Exploitation Regions ────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Foggia Province — Migrant Ghetto Conditions",
        "summary": "Informal settlements (baraccopoli) around Foggia in Puglia house thousands of seasonal agricultural workers in extreme conditions. The former 'Gran Ghetto' of Rignano Garganico housed up to 3,000 workers in shacks without running water, electricity, or sanitation. Workers — primarily from Sub-Saharan Africa — pick tomatoes for EUR 3-4 per 300kg crate. Multiple deaths from fires in makeshift shelters. Italian government demolished settlements without providing adequate alternatives.",
        "source": "Médecins Sans Frontières / Caritas / MEDU reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Rosarno, Calabria — Exploitation and Racial Violence",
        "summary": "Town of Rosarno became international news in 2010 when African agricultural workers rioted after sustained exploitation and racially motivated shootings. Workers harvested oranges and clementines for Ndrangheta-controlled farms at EUR 1-2 per hour. Housed in abandoned factories. Racial attacks by locals. Post-riot, workers dispersed to other Southern Italian regions but exploitation patterns continued.",
        "source": "Italian media / European Parliament inquiry / Ndrangheta investigations",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Sicily Agricultural Exploitation — Romanian and African Workers",
        "summary": "Systematic exploitation in Sicilian greenhouses and open-field agriculture. Romanian workers recruited for vegetable harvesting in Ragusa province, paying EUR 15-25 per day for 12-hour shifts. African workers in citrus harvesting face similar conditions. Reports of sexual exploitation of Romanian women workers by employers. Limited access to healthcare and legal support in rural areas.",
        "source": "FLAI-CGIL Sicily / Ferrara (2017) / MSF",
    },
    {
        "type": "statistic",
        "jurisdiction": "IT",
        "title": "Scale of Agricultural Labour Exploitation in Italy",
        "metric": "Estimated exploited agricultural workers in Italy",
        "value": "Approximately 230,000",
        "year": 2023,
        "summary": "FLAI-CGIL estimates approximately 230,000 agricultural workers in Italy face conditions of severe exploitation, with around 55,000 in conditions meeting the ILO definition of forced labour. Exploitation concentrated in Puglia, Calabria, Sicily, Campania, and increasingly in Northern Italy (Piedmont vineyards, Trentino apple orchards). Workers from over 100 nationalities affected.",
        "source": "FLAI-CGIL 6th Agromafie Report / Ferrara University research",
    },

    # ── Chinese Textile Workers in Prato ─────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Prato Textile District — Chinese Worker Exploitation",
        "summary": "Prato, near Florence, has Europe's largest Chinese community with approximately 50,000 residents and 5,000+ Chinese-owned garment firms. Workers — often undocumented — operate in conditions of severe exploitation: 14-18 hour shifts, sleeping in factories, well below minimum wage. 'Made in Italy' label attached to goods produced in sweatshop conditions. December 2013 fire at Teresa Moda factory killed seven Chinese workers sleeping inside, sparking reform demands.",
        "source": "Italian investigative journalism / NYT / Guardian / Prato prosecutors",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Prato Post-Fire Reforms — Limited Progress",
        "summary": "After the 2013 Teresa Moda fire, Italian authorities conducted mass inspections in Prato. Found widespread fire safety violations, illegal dormitories in factories, and wage theft. Hundreds of firms temporarily closed. However, structural exploitation persists: subcontracting chains obscure responsibility, fast fashion demand drives price pressure, and immigration status makes workers vulnerable. Exploitation evolved rather than disappeared.",
        "source": "Prato Chamber of Commerce / Italian labour inspectorate reports",
    },

    # ── Ndrangheta and Trafficking ───────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Ndrangheta-Linked Labour Trafficking in Calabria",
        "summary": "Anti-mafia investigations have documented Ndrangheta involvement in labour trafficking, particularly in agriculture and construction in Calabria. Criminal networks control access to farm work, extract fees from migrant workers, and launder proceeds through agricultural cooperatives. Operation 'Nduja' (2019) arrested 14 people for caporalato linked to Ndrangheta clans. Workers from Gambia, Senegal, and Mali paid EUR 1-2 per hour picking citrus.",
        "source": "Italian Anti-Mafia Directorate / Catanzaro Prosecutor's Office",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Mafia Involvement in Italian Agricultural Supply Chains",
        "summary": "All four major Italian criminal organizations (Ndrangheta, Camorra, Cosa Nostra, Sacra Corona Unita) documented involvement in agricultural exploitation. Control wholesale food markets, logistics, and labour supply chains. FLAI-CGIL Agromafie report estimates mafia-linked agricultural fraud and exploitation generates EUR 24.5 billion annually. Workers exploited at the production end of chains supplying major European supermarkets.",
        "source": "FLAI-CGIL / Coldiretti / Eurispes Agromafie reports",
    },

    # ── Italian Victim Protection ────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "IT",
        "title": "Italy Article 18 Residence Permit for Trafficking Victims",
        "summary": "Article 18 of Italy's Immigration Act (Legislative Decree 286/1998) provides residence permits to trafficking victims, uniquely not requiring cooperation with criminal proceedings (social protection path). Victims can obtain permits based on their situation of danger alone. Permits last 6 months (renewable) and allow employment. Italy's approach considered a model by GRETA and OSCE for victim-centred protection.",
        "source": "Legislative Decree 286/1998, Art. 18 / GRETA Italy evaluation",
    },
    {
        "type": "statistic",
        "jurisdiction": "IT",
        "title": "Article 18 Permits Issued — Labour Trafficking",
        "metric": "Article 18 permits issued for labour exploitation victims annually",
        "value": "Approximately 120-150 per year",
        "year": 2023,
        "summary": "While Italy issues hundreds of Article 18 permits annually for trafficking victims overall, labour exploitation victims receive far fewer than sexual exploitation victims. Anti-trafficking hotline (800-290-290) receives increasing labour exploitation reports. NGOs report that agricultural workers are least likely to be identified and referred for protection despite high exploitation rates.",
        "source": "Italian Department for Equal Opportunities / anti-trafficking system reports",
    },

    # ── Additional Italian Cases ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Italian Logistics and Delivery Worker Exploitation",
        "summary": "Beyond agriculture, exploitation documented in Italian logistics sector. Migrant workers employed through subcontracting chains for major delivery and logistics companies face extreme conditions: 12-14 hour shifts, below minimum wage, no contracts, unsafe vehicles. Italian courts have found parent companies liable under Law 199/2016 for exploitation in their supply chains. Investigations in Lombardy and Emilia-Romagna exposed systematic underpayment through cooperative structures.",
        "source": "Italian labour courts / trade union (CGIL, CISL) investigations",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Satnam Singh Case — Exploitation Death in Latina (2024)",
        "summary": "Indian agricultural worker Satnam Singh died in June 2024 after his arm was severed by farm machinery in Latina province (Lazio). His employer allegedly dumped him on the roadside rather than calling emergency services. Case provoked national outrage and renewed calls for anti-exploitation enforcement. Highlighted exploitation of Indian Sikh community workers in Pontine Marshes (Agro Pontino) dairy and agriculture sector.",
        "source": "Italian media / Italian Parliament debates / trade union statements",
    },

    # ══════════════════════════════════════════════════════════════════════
    # GERMANY (15+ facts)
    # ══════════════════════════════════════════════════════════════════════

    # ── LkSG Supply Chain Act ────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "DE",
        "title": "German Supply Chain Due Diligence Act (LkSG) 2023",
        "summary": "Lieferkettensorgfaltspflichtengesetz (LkSG) requires companies with 1,000+ employees (from 2024) to conduct human rights and environmental due diligence across their supply chains. Covers forced labour, child labour, discrimination, and unsafe working conditions. Federal Office for Economic Affairs and Export Control (BAFA) enforces compliance. Fines up to 2% of global annual turnover. Does not establish civil liability (unlike French and EU equivalents).",
        "source": "Bundesgesetzblatt 2021 I p. 2959 / BAFA guidance",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "DE",
        "title": "LkSG — Early Implementation Findings",
        "summary": "BAFA reported that in the first year of LkSG enforcement (2023), over 900 companies submitted compliance reports. Significant variation in quality noted. Common weaknesses: risk assessments that fail to go beyond tier-1 suppliers; remediation plans that lack specificity; inadequate grievance mechanisms for affected workers. Several formal proceedings initiated against non-compliant companies.",
        "source": "BAFA annual report 2023 / German Federal Government evaluation",
    },

    # ── Meat Processing (Tonnies) ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "DE",
        "title": "Tonnies Meat Processing Scandal — Exploitation of Eastern European Workers",
        "summary": "Tonnies, Germany's largest meat processing company, employed thousands of Romanian and Bulgarian workers through subcontractors. Workers paid below minimum wage, housed in overcrowded dormitories with deductions for rent exceeding market rates, and forced into excessive overtime. COVID-19 outbreak (2020) infected over 1,500 workers, exposing living and working conditions. Triggered major legislative reform.",
        "source": "Der Spiegel / Robert Koch Institute / German Federal Labour Ministry",
    },
    {
        "type": "law",
        "jurisdiction": "DE",
        "title": "German Meat Industry Reform Act (Arbeitsschutzkontrollgesetz) 2021",
        "summary": "Enacted in response to the Tonnies scandal. Bans subcontracting of core activities (slaughtering, meat processing) in the meat industry from January 2021. Requires direct employment. Mandates electronic working time recording. Strengthens labour inspectorate powers for unannounced inspections. Limits dormitory density. Made Germany a European leader in sector-specific anti-exploitation legislation.",
        "source": "Bundesgesetzblatt 2020 I p. 3334",
    },
    {
        "type": "case_study",
        "jurisdiction": "DE",
        "title": "Post-Tonnies Reforms — Impact Assessment",
        "summary": "Following the Meat Industry Reform Act, approximately 25,000 previously subcontracted workers received direct employment contracts. Wages and conditions improved significantly. However, reports indicate some companies shifted operations to neighbouring countries (Poland, Netherlands) to avoid regulation. Remaining subcontracting in logistics and cleaning roles continues to present exploitation risks. Model studied by other EU states considering sector-specific bans.",
        "source": "Friedrich Ebert Stiftung / DGB trade union assessments",
    },

    # ── Construction Exploitation ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "DE",
        "title": "German Construction Sector — Subcontracting Exploitation",
        "summary": "Multi-layered subcontracting in German construction enables systematic exploitation of posted and migrant workers. Workers from Romania, Bulgaria, Poland, and increasingly Central Asian countries employed through chains of 4-6 subcontractors. Each layer extracts margin, driving down actual worker pay to EUR 5-8 per hour against minimum of EUR 12.41. Workers housed in construction site containers. IG BAU union documents hundreds of wage theft cases annually.",
        "source": "IG BAU / DGB Fair Mobility / European Migrant Workers Union",
    },
    {
        "type": "case_study",
        "jurisdiction": "DE",
        "title": "Berlin Construction Site Exploitation — Operation Cold Tower (2022)",
        "summary": "German customs (Finanzkontrolle Schwarzarbeit) raided construction sites in Berlin in 2022, identifying over 120 cases of illegal employment and wage fraud. Workers from Moldova, Ukraine, and Georgia employed without permits at EUR 4-6 per hour. Living in construction site basements. Passports retained by intermediaries. Twelve arrests made. Investigation revealed connections to organized networks operating across Berlin, Hamburg, and Munich.",
        "source": "German Federal Customs Service (Zoll) press releases / Berlin Prosecutor",
    },

    # ── BKA Trafficking Data ─────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "DE",
        "title": "BKA Federal Situation Report — Trafficking in Human Beings",
        "metric": "Identified trafficking victims in Germany (all forms)",
        "value": "513 (2022)",
        "year": 2022,
        "summary": "German Federal Criminal Police Office (BKA) registered 513 victims of trafficking in 2022 (Bundeslagebild Menschenhandel). Labour trafficking accounts for approximately 20-25% of identified cases. Main origin countries: Nigeria, Romania, Bulgaria, China, Vietnam. BKA acknowledges significant dark figure (Dunkelziffer). Construction, agriculture, gastronomy, and domestic work are highest-risk sectors.",
        "source": "BKA Bundeslagebild Menschenhandel 2022",
    },
    {
        "type": "statistic",
        "jurisdiction": "DE",
        "title": "German Labour Trafficking Prosecutions",
        "metric": "Completed criminal proceedings for labour exploitation",
        "value": "38 proceedings (2022)",
        "year": 2022,
        "summary": "Only 38 criminal proceedings for labour trafficking completed in Germany in 2022, with 15 convictions. Low conviction rate attributed to: difficulty proving coercion elements; victims' reluctance to testify; complex subcontracting structures obscuring responsibility; insufficient specialized training for prosecutors and judges. Advocacy groups argue criminal law thresholds are too high for typical exploitation patterns.",
        "source": "BKA / German Federal Ministry of Justice statistics",
    },

    # ── Counseling and Support ───────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "DE",
        "title": "KOK — German Nationwide Anti-Trafficking Coordination",
        "summary": "Bundesweiter Koordinierungskreis gegen Menschenhandel (KOK) is the umbrella organization for 46 counselling centres for trafficked persons across Germany. Provides specialized support for victims of labour exploitation including legal advice, accompaniment to authorities, safe housing referrals, and psychosocial support. Publishes annual reports on trafficking trends and policy recommendations.",
        "source": "KOK e.V. — www.kok-gegen-menschenhandel.de",
    },
    {
        "type": "contact",
        "jurisdiction": "DE",
        "title": "DGB Fair Mobility — Worker Support Centres",
        "summary": "DGB Fair Mobility (Faire Mobilitat) operates 13 counselling centres across Germany providing free, multilingual advice to mobile and migrant workers. Assists with wage recovery, employment rights, and identification of exploitation. Counselled over 22,000 workers in 2023. Reports that construction, logistics, cleaning, and gastronomy are sectors with highest exploitation complaints. Funded by German Federal Labour Ministry.",
        "source": "DGB Fair Mobility annual reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "DE",
        "title": "German Agriculture — Seasonal Worker Exploitation",
        "summary": "Germany employs approximately 275,000 seasonal agricultural workers annually, primarily from Romania, Poland, and Bulgaria, and increasingly from Georgia and Central Asia. Despite regulatory framework, exploitation persists: excessive hours (12-16 per day), below-minimum-wage piece rates, inadequate accommodation, and deductions for transport and tools. Deaths from heat exhaustion during asparagus and strawberry seasons have prompted increased inspections but limited systemic change.",
        "source": "DGB / Initiative Faire Landarbeit / IG BAU reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "DE",
        "title": "Vietnamese Workers in German Nail Salons",
        "summary": "German police and labour inspectors have identified exploitation of Vietnamese workers in nail salons across major cities. Workers trafficked through organized networks, often entering via Eastern Europe. Conditions include: 12-hour days, no days off, wages of EUR 200-400 per month, chemical exposure without protective equipment. Several police operations (2018-2023) dismantled trafficking networks in Berlin, Hamburg, and North Rhine-Westphalia.",
        "source": "BKA / Landeskriminalamt investigations / anti-trafficking NGOs",
    },

    # ══════════════════════════════════════════════════════════════════════
    # FRANCE (15+ facts)
    # ══════════════════════════════════════════════════════════════════════

    # ── Duty of Vigilance Law ────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "FR",
        "title": "French Duty of Vigilance Law (Loi de Vigilance) 2017",
        "summary": "Law No. 2017-399 requires French companies with 5,000+ employees in France (or 10,000+ worldwide) to establish, publish, and implement a vigilance plan covering human rights and environmental risks across their operations, subsidiaries, and supply chains. First mandatory human rights due diligence law globally. Establishes civil liability: victims can seek damages in French courts. Approximately 300 companies in scope.",
        "source": "Loi n 2017-399 du 27 mars 2017 / French Official Journal",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "Total Energies — Duty of Vigilance Litigation (Uganda Pipeline)",
        "summary": "French NGOs and Ugandan communities brought case under Duty of Vigilance Law against TotalEnergies regarding East African Crude Oil Pipeline (EACOP). Court ruled on procedural jurisdiction in 2023. First major test of corporate liability for supply chain impacts. Case examined forced displacement, environmental harm, and impacts on local communities. Set precedent for extraterritorial application of French human rights due diligence requirements.",
        "source": "Tribunal judiciaire de Paris / Sherpa / Friends of the Earth France",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "FR",
        "title": "Duty of Vigilance — Enforcement Trends",
        "summary": "By 2024, over 30 formal notices and 15 court cases filed under the Duty of Vigilance Law. Companies targeted include Total, Casino, Danone, Teleperformance, and McDonald's France. Cases focus on labour rights violations in supply chains, including forced labour in Xinjiang cotton, exploitation in Brazilian cattle supply chains, and inadequate monitoring of franchise operations. Courts developing jurisprudence on standard of care required.",
        "source": "CCFD-Terre Solidaire / Sherpa vigilance plan tracker",
    },

    # ── CNCDH Reports ────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "FR",
        "title": "CNCDH Trafficking Reports — Persistent Exploitation Patterns",
        "summary": "Commission nationale consultative des droits de l'homme (CNCDH) publishes biennial reports on trafficking in France, serving as France's National Rapporteur equivalent. Reports document: increasing labour trafficking identification (from 15% to 30% of cases over decade); exploitation in construction, agriculture, domestic work, and nail salons; inadequate protection for undocumented victims; need for stronger labour inspectorate mandate for trafficking detection.",
        "source": "CNCDH reports on combating human trafficking (biennial)",
    },
    {
        "type": "statistic",
        "jurisdiction": "FR",
        "title": "Trafficking Victims Identified in France",
        "metric": "Victims formally identified or presumed trafficking victims",
        "value": "Approximately 2,800-3,200 per year",
        "year": 2023,
        "summary": "France identifies approximately 3,000 trafficking victims annually through the National Referral Mechanism. Labour exploitation cases have tripled over the past decade but still represent a minority of identifications. Nigerian women in sexual exploitation remain the largest single group. Labour trafficking victims most commonly from Bangladesh, Pakistan, China, and West Africa. CNCDH estimates actual numbers significantly higher.",
        "source": "MIPROF / CNCDH / French Ministry of Interior statistics",
    },

    # ── Domestic Servitude ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "FR",
        "title": "Domestic Servitude of West African Women by Diplomats in Paris",
        "summary": "Multiple documented cases of West African women (primarily from Ivory Coast, Mali, and Guinea) held in domestic servitude by diplomats and wealthy families in Paris. Workers recruited in origin countries with false promises, passports confiscated on arrival, confined to homes, unpaid or grossly underpaid, subjected to verbal and physical abuse. Diplomatic immunity complicates prosecution. Committee against Modern Slavery (CCEM) has assisted over 1,000 domestic servitude victims in France since 1994.",
        "source": "Comite contre l'esclavage moderne (CCEM) / ECHR cases",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "FR",
        "title": "C.N. and V. v. France [2012] ECHR — Child Domestic Servitude",
        "summary": "ECHR ruled France violated Article 4 (prohibition of servitude) in case of two young girls from Burundi brought to France as domestic servants. Girls were forced to perform all household work, were not schooled, and received no payment. Court found French criminal law insufficiently specific to address servitude and forced labour at the time. Led to reforms in French criminal code (Articles 225-4-1 to 225-4-9).",
        "source": "ECHR Application no. 67724/09",
    },
    {
        "type": "law",
        "jurisdiction": "FR",
        "title": "French Criminal Code — Trafficking and Forced Labour Offences",
        "summary": "French criminal code Articles 225-4-1 to 225-4-9 (as amended 2013) criminalize trafficking in human beings and related exploitation. Article 225-14 specifically criminalizes subjecting a person to working and living conditions incompatible with human dignity, with enhanced penalties for vulnerable victims. Penalties: up to 7 years imprisonment for trafficking, 10 years for aggravated cases. Forced labour: up to 5 years and EUR 150,000 fine.",
        "source": "Code penal, Articles 225-4-1 to 225-14-2",
    },

    # ── Agricultural Exploitation ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "FR",
        "title": "Seasonal Agricultural Workers in Southern France",
        "summary": "Systematic exploitation of seasonal workers in French agriculture, particularly fruit and vegetable picking in Provence, Languedoc, and Corsica. Workers from Morocco, Tunisia, Poland, and Romania recruited through OFII (Office Francais de l'Immigration et de l'Integration) seasonal scheme or informally. Common abuses: piece-rate pay below SMIC minimum wage, housing in caravans without sanitation, excessive hours, and pesticide exposure. Labour inspectorate (Inspection du Travail) under-resourced for agricultural sector.",
        "source": "GISTI / Confederation Paysanne / French labour inspectorate reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "FR",
        "title": "Exploitation in French Wine Industry — Champagne and Bordeaux",
        "summary": "Investigations have documented exploitation of seasonal workers in prestigious French wine regions. Eastern European workers recruited through subcontractors for harvest work in Champagne and Bordeaux, paid piece rates translating to EUR 3-5 per hour. Accommodation in overcrowded mobile homes with excessive rent deductions. Several prosecutions in Bordeaux (2019-2023) resulted in convictions for trafficking for labour exploitation in viticulture.",
        "source": "France 2 investigations / Bordeaux Tribunal judiciaire / CGT-CFDT",
    },

    # ── Other French Cases ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "FR",
        "title": "Exploitation in French Construction — Paris Region",
        "summary": "Migrant workers from Mali, Senegal, and Romania exploited in construction and renovation projects in Ile-de-France. Workers recruited informally, paid EUR 30-50 per day (below minimum), no social security registration, and housed in squats or overcrowded apartments. Some workers reported working on public construction projects through subcontracting chains. CGT construction union has brought multiple cases to labour courts.",
        "source": "CGT-Construction / Inspection du Travail Ile-de-France",
    },
    {
        "type": "case_study",
        "jurisdiction": "FR",
        "title": "Chinese Workers in French Textile — Aubervilliers",
        "summary": "Chinese garment workshops in Aubervilliers (Seine-Saint-Denis) operate with conditions mirroring Prato, Italy. Workers — many undocumented — produce fast fashion in 14-16 hour shifts, sleeping in workshops. Raids have found fire safety violations, illegal dormitories, and wages of EUR 2-3 per hour. Criminal networks control labour supply. French authorities conduct periodic operations but structural exploitation persists due to demand from European fast fashion supply chains.",
        "source": "French police reports / Le Monde investigations / Inspection du Travail",
    },
    {
        "type": "case_study",
        "jurisdiction": "FR",
        "title": "Exploitation of Undocumented Workers in French Delivery Platforms",
        "summary": "Undocumented migrants rent accounts from registered delivery workers on platforms (Uber Eats, Deliveroo) in major French cities. Account renters (locataires) pay EUR 100-200 per week for access to the platform, earning below minimum wage after deductions. No employment protection, insurance, or accident coverage. Exploitation networks identified operating primarily among Malian, Guinean, and Ivorian communities. French labour courts ruling on platform accountability.",
        "source": "Le Monde / France Info investigations / CCEM",
    },

    # ══════════════════════════════════════════════════════════════════════
    # SPAIN (10+ facts)
    # ══════════════════════════════════════════════════════════════════════

    # ── Strawberry Picking (Huelva) ──────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ES",
        "title": "Huelva Strawberry Picking — Moroccan Women Worker Exploitation",
        "summary": "Spain recruits approximately 15,000-20,000 Moroccan women annually for strawberry harvesting in Huelva province under bilateral circular migration agreements. Workers have reported: sexual harassment and assault by supervisors; wage theft through piece-rate manipulation; overcrowded housing with excessive deductions; confiscation of passports by employers; threats of deportation for complaints. Complaints to Spanish authorities and Moroccan embassy largely unaddressed until German and Spanish media investigations (2018-2019).",
        "source": "BuzzFeed News / Correctiv / Spanish trade unions (CCOO, UGT)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ES",
        "title": "Huelva Strawberry Farm Prosecutions",
        "summary": "Following media exposure in 2018-2019, Spanish prosecutors initiated investigations into sexual abuse and labour exploitation on Huelva farms. Several farm owners prosecuted for sexual assault of Moroccan workers. Convictions obtained in 2021-2023 for rape and sexual abuse of seasonal workers. However, labour exploitation charges proved more difficult to prosecute. Cases highlighted intersection of gender-based violence and labour trafficking.",
        "source": "Spanish courts / Junta de Andalucia / Women's Link Worldwide",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "ES",
        "title": "Spain-Morocco Circular Migration Programme Reforms",
        "summary": "In response to exploitation scandals, Spain reformed its seasonal worker recruitment programme with Morocco. Changes include: pre-departure information sessions in Arabic; multilingual complaint hotlines; increased labour inspections during harvest season; employer blacklisting for violations. However, structural power imbalance remains: workers' return the following season depends on employer evaluation, creating dependency that inhibits reporting.",
        "source": "Spanish Ministry of Inclusion / ANAPEC (Morocco) / IOM",
    },

    # ── Almeria Greenhouses ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ES",
        "title": "Almeria Greenhouse Exploitation — Mar de Plastico",
        "summary": "Almeria province in southeastern Spain has 30,000+ hectares of plastic greenhouses (the 'sea of plastic' visible from space). Approximately 80,000-100,000 workers, primarily from Morocco, Sub-Saharan Africa, and Romania, work in extreme heat conditions (50°C+ inside greenhouses). Common abuses: EUR 30-35 per day for 10-12 hour shifts (below legal minimum); no contracts; no social security; pesticide exposure without protective equipment; housing in makeshift settlements (chabolas) without water or sanitation.",
        "source": "ECCHR / La Marea / SOC-SAT union / Greenpeace Spain",
    },
    {
        "type": "case_study",
        "jurisdiction": "ES",
        "title": "Almeria — Worker Deaths and Health Impacts",
        "summary": "Multiple migrant worker deaths from heat exhaustion and pesticide poisoning documented in Almeria greenhouses. Workers report chronic respiratory illness, skin conditions, and cancer concerns from daily pesticide exposure without masks or protective clothing. Limited access to healthcare for undocumented workers. NGOs (Medicos del Mundo, Caritas) provide basic health services but cannot address systemic occupational health violations.",
        "source": "Medicos del Mundo / SOC-SAT / Spanish occupational health reports",
    },
    {
        "type": "statistic",
        "jurisdiction": "ES",
        "title": "Spanish Agricultural Export and Labour Exploitation",
        "metric": "Annual value of Almeria agricultural exports",
        "value": "Approximately EUR 3.5 billion",
        "year": 2023,
        "summary": "Almeria's greenhouse sector exports EUR 3.5 billion annually, primarily to European supermarkets. Spain is Europe's largest exporter of fresh fruits and vegetables. Production relies heavily on exploited migrant labour. Consumer prices do not reflect fair wages. European Corporate Sustainability Due Diligence requirements expected to increase scrutiny of Spanish agricultural supply chains.",
        "source": "Spanish Ministry of Agriculture / Eurostat trade data",
    },

    # ── Other Spanish Cases ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ES",
        "title": "Exploitation of Undocumented Workers in Spanish Construction",
        "summary": "Spanish construction boom (pre-2008 and post-2015 recovery) relied heavily on undocumented migrant workers, particularly from Latin America, Romania, and Morocco. Workers employed without contracts at 50-70% of legal minimum wage. Fatal accidents disproportionately affected undocumented workers unable to report unsafe conditions. Labour inspectorate (Inspeccion de Trabajo) increased inspections but regularization pathways remain limited.",
        "source": "Spanish labour inspectorate / UGT / CCOO construction sector reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "ES",
        "title": "Chinese Workers in Spanish Garment Workshops",
        "summary": "Exploitation of Chinese workers in garment workshops documented in Madrid, Barcelona, and other Spanish cities. Workers — often brought to Spain through debt bondage arrangements — operate in conditions of severe exploitation: 16-hour days, no rest days, EUR 300-500 per month, sleeping in workshops. Spanish police operations have dismantled trafficking networks but exploitation continues through informal subcontracting to legitimate fashion brands.",
        "source": "Spanish National Police / Guardia Civil anti-trafficking units",
    },
    {
        "type": "law",
        "jurisdiction": "ES",
        "title": "Spanish Trafficking Legislation — Organic Law 1/2015",
        "summary": "Organic Law 1/2015 amended the Spanish Criminal Code (Article 177 bis) to strengthen trafficking provisions. Penalties of 5-8 years for trafficking, increased to 8-12 years for aggravated cases (minors, public officials, organized crime). Establishes comprehensive victim protection including residence permits, legal aid, and safe housing. Spain's legislation aligns with EU Directive 2011/36/EU but enforcement remains inconsistent across autonomous communities.",
        "source": "Boletin Oficial del Estado / Spanish Criminal Code Art. 177 bis",
    },

    # ══════════════════════════════════════════════════════════════════════
    # GREECE (10+ facts)
    # ══════════════════════════════════════════════════════════════════════

    # ── Manolada Case ────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Manolada Strawberry Picker Shooting (2013)",
        "summary": "In April 2013, supervisors at a strawberry farm in Manolada, Peloponnese, shot at approximately 200 Bangladeshi workers who demanded six months of unpaid wages. Twenty-eight workers hospitalized with gunshot wounds. Four Greek supervisors arrested and charged. Case became a landmark for migrant worker exploitation in Greek agriculture. Workers were undocumented, housed in makeshift tents, and paid EUR 22 per day (when paid). The shooting brought international attention to structural exploitation in Greek agriculture.",
        "source": "Greek media / Human Rights Watch / ECHR case file",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Manolada Shooting Trial — Controversial Acquittals (2014)",
        "summary": "Initial trial in 2014 resulted in acquittal of farm owner on trafficking and forced labour charges, with only supervisors receiving sentences (5-8 years, partially suspended). Verdict provoked international condemnation from GRETA, UNHCR, and European Parliament. One supervisor convicted of causing bodily harm received 14 years. Case criticized as reflecting systemic tolerance of agricultural exploitation in Greek justice system.",
        "source": "Patras Court of Assizes / GRETA urgent procedure on Greece",
    },

    # ── Chowdury v. Greece Aftermath ─────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "GR",
        "title": "Chowdury and Others v. Greece [2017] ECHR — Impact and Aftermath",
        "summary": "Following the ECHR judgment finding Greece violated Article 4 (forced labour) in the Manolada case, Greece was required to pay compensation to 42 Bangladeshi workers. However, structural reforms have been limited. Agricultural exploitation continues in Manolada and other regions. New recruitment patterns have shifted to workers from Pakistan, Egypt, and Albania. GRETA evaluations continue to criticize Greece's failure to implement systemic changes in agricultural labour oversight.",
        "source": "ECHR judgment 21884/15 / GRETA 3rd evaluation of Greece",
    },

    # ── Broader Greek Agricultural Exploitation ──────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Greek Agricultural Exploitation — Systemic Patterns",
        "summary": "Beyond Manolada, systematic exploitation of migrant workers documented across Greek agriculture: cotton picking in Thessaly; olive harvesting in Crete; fishing in Aegean islands; fruit orchards in Northern Greece. Workers primarily from Bangladesh, Pakistan, Egypt, Albania, and Bulgaria. Common pattern: workers recruited without contracts, housed in substandard conditions (shipping containers, tents), paid piece rates below minimum wage, and threatened with police reporting if they complain.",
        "source": "Greek Ombudsman reports / FRA / GRETA / Generation 2.0",
    },
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "South Asian Workers in Greek Agriculture — Recruitment Debt",
        "summary": "Bangladeshi and Pakistani workers arrive in Greece after paying EUR 4,000-8,000 to trafficking networks for transport and forged documents. Workers trapped in debt bondage upon arrival, forced to accept any work conditions to repay debt. Exploitation concentrated in Peloponnese (strawberries), Central Greece (cotton, watermelon), and Crete (olive oil). Circular pattern: workers unable to regularize status, making them permanently vulnerable to exploitation.",
        "source": "IOM Greece / Aitima (Greek Council for Refugees)",
    },
    {
        "type": "statistic",
        "jurisdiction": "GR",
        "title": "Greek Agricultural Workforce — Migrant Worker Dependence",
        "metric": "Estimated share of migrant workers in Greek agriculture",
        "value": "Approximately 60-70%",
        "year": 2023,
        "summary": "Migrant workers constitute 60-70% of Greek agricultural labour, primarily in seasonal crops. Estimated 30,000-50,000 undocumented workers in Greek agriculture at any time. Greek agricultural GDP of EUR 7.5 billion depends structurally on cheap migrant labour. Several regions have near-complete dependence on migrant workers for harvest operations.",
        "source": "Greek Ministry of Agricultural Development / IOM Greece / Eurostat",
    },
    {
        "type": "law",
        "jurisdiction": "GR",
        "title": "Greek Law 4251/2014 — Immigration and Social Integration Code",
        "summary": "Greek Immigration Code provides for residence permits based on employment, including seasonal agricultural work. Law 4636/2019 (International Protection Act) includes provisions for trafficking victim identification in asylum procedures. However, implementation criticized: work permits tied to specific employer facilitate exploitation; regularization pathways insufficient; undocumented workers have no practical access to labour rights enforcement.",
        "source": "Greek Official Gazette / GRETA evaluation / Greek Ombudsman",
    },
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Refugee and Migrant Exploitation on Greek Islands",
        "summary": "Asylum seekers on Greek islands (Lesbos, Samos, Chios) exploited in informal labour markets while awaiting asylum processing. Work in olive harvesting, tourism services, and construction without permits, at wages of EUR 15-20 per day. Vulnerability compounded by lengthy asylum procedures (average 2+ years) and restrictions on mainland movement. NGOs report cases meeting ILO forced labour indicators, particularly abuse of vulnerability and coercion.",
        "source": "UNHCR Greece / MSF / Greek Council for Refugees",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "GR",
        "title": "Greek Agricultural Work Permit Reforms (2023-2024)",
        "summary": "Greece introduced emergency provisions allowing undocumented agricultural workers to obtain temporary work permits, partly addressing the structural vulnerability enabling exploitation. Permits valid for 6 months in agriculture, renewable. While improving legal status, critics note permits remain employer-specific, maintaining power imbalance. GRETA welcomed the initiative but urged full decoupling of work authorization from specific employer sponsorship.",
        "source": "Greek Ministry of Migration and Asylum / GRETA recommendations",
    },
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Greek Fishing Sector — Exploitation of Egyptian Workers",
        "summary": "Egyptian workers recruited for Greek fishing fleet, particularly in Aegean Sea and Ionian Sea. Workers confined to vessels for extended periods, paid below agreed wages or not at all. Physical violence documented. Some workers reported being threatened with being thrown overboard. Cases investigated by Greek coast guard and labour inspectorate. Intersection with maritime labour Convention (MLC 2006) which Greece has ratified but enforcement on small fishing vessels is minimal.",
        "source": "Greek coast guard investigations / IOM / ITF (maritime union)",
    },

    # ══════════════════════════════════════════════════════════════════════
    # NETHERLANDS (6+ facts)
    # ══════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "NL",
        "title": "Dutch National Rapporteur Model — International Best Practice",
        "summary": "Netherlands established the first National Rapporteur on Trafficking in Human Beings (1997). The Rapporteur (Nationaal Rapporteur Mensenhandel) operates independently from government, publishes annual reports, analyzes trafficking data, and makes policy recommendations. Model adopted by EU Anti-Trafficking Directive as recommended structure. Rapporteur has repeatedly highlighted underreporting of labour trafficking compared to sexual exploitation.",
        "source": "Dutch National Rapporteur on Trafficking in Human Beings",
    },
    {
        "type": "statistic",
        "jurisdiction": "NL",
        "title": "Dutch Labour Trafficking Reporting",
        "metric": "Reported potential trafficking victims in the Netherlands",
        "value": "Approximately 900-1,100 per year",
        "year": 2023,
        "summary": "Dutch National Rapporteur receives approximately 1,000 reports of potential trafficking annually. Labour exploitation accounts for 25-30% of reports, up from 15% a decade ago. Main origin countries for labour exploitation victims: Poland, Romania, Hungary, Philippines, and India. Sectors: agriculture (greenhouses), food processing, logistics, cleaning, and construction. Conviction rates remain low despite advanced identification system.",
        "source": "Dutch National Rapporteur / CoMensha annual figures",
    },
    {
        "type": "case_study",
        "jurisdiction": "NL",
        "title": "Dutch Greenhouse Exploitation — Westland Region",
        "summary": "Westland greenhouse region near The Hague employs thousands of migrant workers, primarily from Poland, Romania, and Bulgaria, through temporary employment agencies. Workers report: excessive overtime, housing in overcrowded containers with inflated rent deductions, piece-rate systems resulting in below-minimum-wage pay, and threats of dismissal for complaining. Inspectorate SZW investigations found widespread violations. Several temporary agencies prosecuted for trafficking.",
        "source": "Inspectorate SZW / FNV union / Dutch media investigations",
    },
    {
        "type": "case_study",
        "jurisdiction": "NL",
        "title": "Dutch Meat Processing — Labour Agency Exploitation",
        "summary": "Following the German Tonnies model, Dutch meat processing relies heavily on temporary agency workers from Eastern Europe. Workers employed by agencies registered in Netherlands, Poland, or Romania. Investigations revealed: wage underpayment through illegal deductions; housing in company-provided accommodation with excessive charges; false self-employment constructs (schijnzelfstandigheid); unsafe working conditions including repetitive strain injuries at high line speeds.",
        "source": "Inspectorate SZW / FNV Uitzendbond / Brabants Dagblad investigations",
    },
    {
        "type": "law",
        "jurisdiction": "NL",
        "title": "Dutch Labour Exploitation Legislation — Article 273f Sr",
        "summary": "Article 273f of the Dutch Criminal Code (Wetboek van Strafrecht) criminalizes trafficking in human beings including labour exploitation. Maximum penalty: 12 years imprisonment (18 years for organized trafficking). Netherlands one of few EU states to explicitly include labour exploitation within trafficking framework. However, courts have interpreted exploitation narrowly, requiring conditions 'significantly below acceptable standards,' leading to acquittals in borderline cases.",
        "source": "Dutch Criminal Code Art. 273f / Dutch Supreme Court jurisprudence",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "NL",
        "title": "Dutch Temporary Employment Agency Regulation Reforms",
        "summary": "Netherlands tightened regulation of temporary employment agencies (uitzendbureaus) following widespread labour exploitation findings. SNA (Stichting Normering Arbeid) certification required for agencies. Labour inspectorate increased enforcement actions. Proposed legislation to introduce licensing system and holding parent companies liable for subsidiary agency violations. Aim: break cycle of exploitation through unregistered or fraudulent temporary agencies employing migrant workers.",
        "source": "Dutch Ministry of Social Affairs / Inspectorate SZW / Roemer Commission report",
    },

    # ══════════════════════════════════════════════════════════════════════
    # BELGIUM (4 facts)
    # ══════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "BE",
        "title": "Belgian Trafficking Cases — Construction and Domestic Work",
        "summary": "Belgium identifies approximately 600-700 potential trafficking victims annually through its specialized centres (PAG-ASA, Payoke, Surya). Labour exploitation cases concentrated in construction, restaurant/catering, domestic work, and car wash services. Workers primarily from Romania, Bulgaria, Morocco, and India. Belgium's referral system — offering residence permits and support to identified victims who cooperate with prosecution — considered among Europe's strongest.",
        "source": "Belgian Federal Migration Centre (Myria) annual trafficking reports",
    },
    {
        "type": "law",
        "jurisdiction": "BE",
        "title": "Belgian Anti-Trafficking Law 2005 (Amended 2013)",
        "summary": "Belgian Law of 10 August 2005 criminalizes trafficking for labour exploitation with penalties of 1-15 years and fines up to EUR 100,000. Amended in 2013 to broaden exploitation definition. Belgium's multi-disciplinary approach includes specialized prosecutors, labour inspectorate teams trained in trafficking detection, and NGO partnership for victim support. Victims granted temporary residence permits and access to social assistance during proceedings.",
        "source": "Belgian Federal Public Service Justice / Myria",
    },
    {
        "type": "case_study",
        "jurisdiction": "BE",
        "title": "Exploitation in Belgian Restaurant Sector — Chinese and South Asian Workers",
        "summary": "Belgian labour inspectorate and police have investigated exploitation in Chinese and South Asian restaurants across Brussels, Antwerp, and Liege. Workers recruited from China, Bangladesh, and India through informal networks. Conditions include: 80-hour work weeks, accommodation in restaurant premises, wages of EUR 400-600 per month, and threats of immigration reporting. Several restaurant owners convicted of trafficking under Belgian law.",
        "source": "Belgian Social Inspectorate / Payoke / Myria annual reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "BE",
        "title": "Belgian Diplomatic Immunity and Domestic Servitude",
        "summary": "Multiple cases of domestic servitude by diplomats posted to Brussels (hosting EU institutions, NATO). Workers from Philippines, Sri Lanka, and West Africa confined to diplomatic residences, passports confiscated, unpaid or grossly underpaid. Belgian authorities unable to prosecute due to diplomatic immunity. Belgium has negotiated bilateral agreements with some states allowing limited civil action. GRETA has urged Belgium to strengthen protections for domestic workers in diplomatic households.",
        "source": "GRETA Belgium evaluation / Belgian Senate reports / CCEM",
    },

    # ══════════════════════════════════════════════════════════════════════
    # POLAND / ROMANIA — POSTED WORKER EXPLOITATION (4 facts)
    # ══════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "PL",
        "title": "Polish Workers Posted to Western Europe — Exploitation Patterns",
        "summary": "Poland is one of the EU's largest sources of posted workers. Workers posted through agencies to Germany, Netherlands, Belgium, and Scandinavia frequently face exploitation: wages below host-country minimums (but above Polish levels, obscuring exploitation); excessive deductions for accommodation and transport; unsafe working conditions; threats of dismissal for injury claims. Construction, meat processing, and logistics are highest-risk sectors. PIP (State Labour Inspectorate) receives thousands of complaints annually.",
        "source": "Polish State Labour Inspectorate (PIP) / ETUC / DGB Fair Mobility",
    },
    {
        "type": "case_study",
        "jurisdiction": "RO",
        "title": "Romanian Workers Exploited in Western European Agriculture",
        "summary": "Romania supplies significant seasonal agricultural labour across the EU. Workers exploited in Italian tomato fields, Spanish greenhouses, French vineyards, and German asparagus farms. Recruitment through informal networks in rural Romania, exploiting economic desperation. Workers report wages 30-50% below host-country minimums, deductions for transport and housing, lack of contracts, and no social security registration. Romania's labour inspectorate has limited capacity for cross-border monitoring.",
        "source": "Romanian Inspectorate for Labour / IOM Romania / FRA",
    },
    {
        "type": "statistic",
        "jurisdiction": "EU",
        "title": "Romanian and Bulgarian Workers in EU Labour Market",
        "metric": "Romanian and Bulgarian citizens working in other EU Member States",
        "value": "Approximately 4 million",
        "year": 2023,
        "summary": "An estimated 4 million Romanians and Bulgarians work in other EU countries. While many work in fair conditions, disproportionate share face exploitation due to: language barriers; unfamiliarity with host-country rights; economic pressure to accept any conditions; recruitment through intermediaries with fraudulent promises. These workers constitute the largest group of intra-EU trafficking victims according to Eurostat data.",
        "source": "Eurostat / European Commission free movement reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Letterbox Companies and Posted Worker Fraud",
        "summary": "Fraudulent use of posted worker rules through letterbox companies (companies with no genuine economic activity in their registered country). Companies register in low-cost EU states (often Cyprus, Slovakia, or Slovenia) to post workers to high-wage states while paying social security at lower rates. Workers exploited through multiple layers of subcontracting. European Labour Authority and national authorities have dismantled several networks, but enforcement remains fragmented across Member States.",
        "source": "European Labour Authority / OLAF investigations / Eurojust",
    },

    # ══════════════════════════════════════════════════════════════════════
    # NORDIC COUNTRIES — BERRY PICKER EXPLOITATION (4 facts)
    # ══════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "SE",
        "title": "Thai Berry Pickers in Sweden — Systematic Exploitation",
        "summary": "Thailand sends 5,000-8,000 berry pickers to Sweden annually for wild berry harvesting (blueberries, lingonberries). Workers pay THB 100,000-200,000 (EUR 2,500-5,000) to Thai recruitment agencies for the opportunity. Earnings depend entirely on harvest volume, and poor berry seasons leave workers in debt. Reports of: overcrowded accommodation in forest camps; 12-16 hour picking days; minimal actual earnings; exploitation by Thai supervisors who control transport and food supply. Several workers have died in Sweden.",
        "source": "Swedish Work Environment Authority / LO (Swedish Trade Union) / IOM Thailand",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "SE",
        "title": "Swedish Berry Picker Cases — Trafficking Prosecutions",
        "summary": "Swedish courts have prosecuted several cases involving Thai berry picker exploitation. Notable case (2013): Thai company owner convicted of trafficking 16 workers who earned nothing and returned home in debt. Workers held in forest camps, passports retained. Courts found forced labour conditions despite victims having technically entered Sweden voluntarily. Sentences: 2-6 years imprisonment. Cases led to regulatory reforms for berry picking permits.",
        "source": "Swedish courts / Swedish Prosecution Authority / IOM",
    },
    {
        "type": "case_study",
        "jurisdiction": "FI",
        "title": "Finnish Berry Picking and Restaurant Exploitation",
        "summary": "Finland faces similar berry picker exploitation to Sweden, with Thai and Vietnamese workers recruited for wild berry harvesting. Additionally, exploitation documented in Finnish restaurant sector: Thai, Nepalese, and Vietnamese workers in ethnic restaurants face 70-80 hour work weeks at EUR 3-5 per hour. Finnish police and labour inspectors have conducted targeted operations, identifying trafficking in both sectors. National Assistance System for Victims of Human Trafficking referrals increasing annually.",
        "source": "Finnish National Assistance System / Finnish police / non-discrimination ombudsman",
    },
    {
        "type": "case_study",
        "jurisdiction": "NO",
        "title": "Norwegian Car Wash and Cleaning Exploitation",
        "summary": "Norwegian police have investigated labour exploitation in car wash services and cleaning companies employing migrant workers from Pakistan, Afghanistan, and Eastern Europe. Workers paid NOK 30-50 per hour (legal minimum approximately NOK 190 for cleaning). Housed in overcrowded accommodation. Tax fraud and social security evasion commonplace. Norwegian labour inspectorate (Arbeidstilsynet) increased inspections of high-risk sectors following GRETA recommendations.",
        "source": "Norwegian Arbeidstilsynet / KOM (Coordinating Unit for Trafficking) reports",
    },

    # ══════════════════════════════════════════════════════════════════════
    # IRELAND — FISHING AND OTHER SECTORS (4 facts)
    # ══════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "IE",
        "title": "Irish Fishing Fleet — Exploitation of Non-EEA Workers",
        "summary": "Systematic exploitation of non-EEA workers in the Irish fishing fleet documented by Migrant Rights Centre Ireland and the International Transport Workers' Federation. Workers from Ghana, Philippines, Egypt, and Indonesia employed through Atypical Worker Permission Scheme. Reports include: wages as low as EUR 2-3 per hour; 20+ hour shifts at sea; physical violence; document retention; workers locked in accommodation when vessel is in port. Guardian investigations (2015, 2018) brought international attention.",
        "source": "MRCI / ITF / Guardian investigations / GRETA Ireland evaluation",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "IE",
        "title": "Irish Atypical Worker Permission Scheme — Fishing Sector Reforms",
        "summary": "Following exposure of exploitation, Ireland reformed the Atypical Worker Permission Scheme for fishing in 2016. Workers given direct relationship with Department of Justice rather than being dependent on vessel owner. Minimum wage and employment law protections extended. However, implementation criticized: workers remain dependent on single employer for immigration status; changing vessel requires new application; remote locations impede inspection. Exploitation has continued post-reform.",
        "source": "Irish Department of Justice / MRCI / IHREC",
    },
    {
        "type": "case_study",
        "jurisdiction": "IE",
        "title": "Irish Meat Processing and Construction — Labour Exploitation",
        "summary": "Beyond fishing, labour exploitation documented in Irish meat processing plants and construction sites. Workers from Brazil, Romania, and Moldova employed through subcontractors at below-minimum-wage rates. Workplace Relations Commission and Health and Safety Authority increased inspections. National Referral Mechanism (established 2008) receives approximately 100 referrals annually but is criticized for low identification rates relative to estimated exploitation levels.",
        "source": "Irish Workplace Relations Commission / MRCI / IHREC",
    },
    {
        "type": "statistic",
        "jurisdiction": "IE",
        "title": "Irish Trafficking Identification Statistics",
        "metric": "Potential trafficking victims referred in Ireland",
        "value": "Approximately 75-100 per year",
        "year": 2023,
        "summary": "Ireland identifies approximately 75-100 potential trafficking victims annually. Labour trafficking accounts for roughly 30% of referrals. US TIP Report has consistently placed Ireland on Tier 2 Watch List or Tier 2, citing insufficient victim identification, lack of dedicated anti-trafficking legislation (addressed by Criminal Law (Human Trafficking) Act 2008, amended 2013), and limited access to compensation for victims.",
        "source": "Irish Department of Justice / US TIP Report / GRETA",
    },

    # ══════════════════════════════════════════════════════════════════════
    # PORTUGAL (3 facts)
    # ══════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "PT",
        "title": "Portuguese Agricultural Exploitation — Alentejo and Odemira",
        "summary": "Odemira municipality in Alentejo became a focus of exploitation concerns in 2021 when COVID-19 outbreaks exposed conditions of migrant workers in intensive horticulture. Workers from South Asia (Bangladesh, India, Nepal) and Thailand housed in overcrowded conditions (8-10 per room), employed through intermediaries at below-minimum-wage rates. Portuguese government declared Odemira a health emergency and deployed military to manage COVID outbreaks. Structural exploitation linked to rapid agricultural expansion.",
        "source": "Portuguese SEF / ACT / Observatorio do Trafico de Seres Humanos",
    },
    {
        "type": "case_study",
        "jurisdiction": "PT",
        "title": "Exploitation of South Asian Workers in Portuguese Agriculture",
        "summary": "Growing community of Bangladeshi, Indian, and Nepalese workers in Portuguese agriculture (Alentejo, Ribatejo). Workers recruited through transnational networks, paying EUR 3,000-8,000 for documents and transport. Employed in strawberry, blueberry, and raspberry cultivation at EUR 3-4 per hour (legal minimum EUR 4.85/hr in 2023). Accommodation provided by employers with excessive deductions. Language barriers and rural isolation impede access to support services.",
        "source": "ACT (Authority for Working Conditions) / IOM Portugal / Plataforma Portuguesa para os Direitos das Mulheres",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PT",
        "title": "Portuguese Labour Exploitation Reforms 2021-2024",
        "summary": "Following the Odemira crisis, Portugal implemented reforms: creation of inter-ministerial task force on agricultural exploitation; increased ACT (labour inspectorate) resources for Alentejo region; simplified regularization pathways for undocumented agricultural workers; mandatory employer-provided housing standards. However, enforcement capacity remains limited relative to rapidly growing migrant workforce, and temporary regularization may not address structural vulnerability.",
        "source": "Portuguese Council of Ministers / ACT / GRETA Portugal evaluation",
    },

    # ══════════════════════════════════════════════════════════════════════
    # UK (3 facts — complementing court_rulings.py)
    # ══════════════════════════════════════════════════════════════════════
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "Gangmasters Licensing Authority — UK Agricultural Labour Model",
        "summary": "UK established the Gangmasters Licensing Authority (GLA, now GLAA — Gangmasters and Labour Abuse Authority) in 2004 following the Morecambe Bay cockle pickers disaster that killed 23 Chinese workers. GLA licenses labour providers in agriculture, horticulture, shellfish, and food processing. Licensing model requires adherence to labour standards. GLAA expanded (2017) with police-like enforcement powers. Model studied internationally, including by Italy in designing anti-caporalato reforms.",
        "source": "GLAA / UK Home Office / Modern Slavery Act 2015 Annual Reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "UK Hand Car Wash Exploitation",
        "summary": "An estimated 10,000-20,000 hand car washes operate in the UK, many employing vulnerable and trafficked workers. Workers from Romania, Albania, and Vietnam paid GBP 2-3 per hour (below minimum wage of GBP 10.42). Operated by criminal networks. HMRC, GLAA, and police conduct joint operations (e.g., Operation Erebus) targeting car wash exploitation. Safe Car Wash app launched (2018) to enable public reporting. GLAA estimated up to 80% of car washes have labour compliance issues.",
        "source": "GLAA / Safe Car Wash App / UK Modern Slavery Annual Reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "Vietnamese Workers in UK Cannabis Cultivation and Nail Bars",
        "summary": "Vietnamese nationals, often trafficking victims (including children), exploited in UK cannabis farms and nail bars. Workers confined to cannabis grow houses, subjected to violence, and unpaid. Nail bar workers face conditions including: 12-hour days, minimal pay, chemical exposure, and debt bondage to trafficking networks. UK authorities have struggled to identify victims versus offenders. NCA (National Crime Agency) estimates Vietnamese trafficking as one of largest flows into the UK.",
        "source": "NCA / ECPAT UK / Anti-Slavery Commissioner annual reports",
    },

    # ══════════════════════════════════════════════════════════════════════
    # CROSS-CUTTING EUROPEAN THEMES (3 facts)
    # ══════════════════════════════════════════════════════════════════════
    {
        "type": "advisory",
        "jurisdiction": "EU",
        "title": "OSCE/ODIHR — National Referral Mechanism Best Practices in Europe",
        "summary": "OSCE Office for Democratic Institutions and Human Rights publishes guidance on National Referral Mechanisms (NRMs) for trafficking victims across European states. Key recommendations: formal identification procedures; unconditional assistance during reflection period; residence permits independent of cooperation with prosecution; access to compensation; specialized training for front-line officials. European NRMs vary significantly in quality, with Benelux and Nordic models generally rated highest.",
        "source": "OSCE/ODIHR NRM Handbook / GRETA evaluations",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "COVID-19 Impact on Migrant Worker Exploitation in Europe",
        "summary": "COVID-19 pandemic exacerbated exploitation of migrant workers across Europe. Agricultural workers declared essential but denied health protections. Lockdowns trapped workers with abusive employers. Border closures disrupted seasonal labour flows, creating new recruitment vulnerabilities when borders reopened. Multiple EU states organized emergency charter flights for seasonal workers (Romania-Germany, Morocco-Spain) with minimal exploitation safeguards. Pandemic revealed structural dependency on exploitable migrant labour in European food systems.",
        "source": "FRA / GRETA / European Migration Network COVID-19 reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "EU",
        "title": "Exploitation of Ukrainian Refugees in Europe (2022-Present)",
        "summary": "Mass displacement from Ukraine since February 2022 created new trafficking and exploitation risks across Europe. Over 4 million Ukrainians granted temporary protection in EU states. Reports of exploitation in: Polish and Czech construction and agriculture; German logistics and cleaning; Spanish hospitality. Vulnerable groups include unaccompanied women and children. EU Anti-Trafficking Coordinator issued specific guidance on preventing exploitation of Ukrainian refugees. National anti-trafficking agencies report increased referrals.",
        "source": "EU Anti-Trafficking Coordinator / UNHCR / La Strada International",
    },
]
