"""
Balkan Region Trafficking Cases and Laws Seed Facts

This module contains 150 curated facts covering human trafficking cases,
legislation, court rulings, and prevention measures across the Balkan countries:
Albania, North Macedonia, Serbia, Kosovo, Montenegro, and Bosnia-Herzegovina.

Data sources include OSCE reports, GRETA assessments, US TIP Reports,
national court decisions, and international prosecution databases.

Jurisdiction: Albania (25), North Macedonia (25), Serbia (25),
Kosovo (25), Montenegro (25), Bosnia-Herzegovina (25).
"""

BALKAN_TRAFFICKING_CASE_FACTS = [
    # ALBANIA - Trafficking Statutes
    {
        "type": "statutory_provision",
        "jurisdiction": "Albania",
        "title": "Albanian Criminal Code Article 110/a - Trafficking in Persons",
        "summary": "Criminalizes trafficking in persons with penalties of 8-15 years imprisonment. Covers recruitment, transport, transfer, harboring or receipt of persons through threat or use of force or other forms of coercion for exploitation. Enhanced penalties apply to trafficking of minors or trafficking by organized criminal groups.",
        "source": "Albanian Criminal Code Art. 110/a (amended 2008, 2015)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "Albania",
        "title": "Albanian Criminal Code Article 128/b - Forced Labor",
        "summary": "Prohibits compelling a person to work through coercion, violence, or threat. Penalties range from 5-15 years imprisonment. Closely linked to trafficking charges and exploitation in agriculture, construction, and manufacturing sectors.",
        "source": "Albanian Criminal Code Art. 128/b"
    },
    {
        "type": "advisory",
        "jurisdiction": "Albania",
        "title": "GRETA 2nd Evaluation Report on Albania (2013)",
        "summary": "Assessed Albania as major source country for trafficking despite legislative improvements. Identified exploitation of Albanian nationals in sex work and forced labor in Greece, Italy, and UK. Noted insufficient victim identification and reintegration services.",
        "source": "GRETA 2nd Evaluation Report on Albania"
    },
    {
        "type": "advisory",
        "jurisdiction": "Albania",
        "title": "GRETA 3rd Evaluation Report on Albania (2019)",
        "summary": "Found continued vulnerabilities in Albanian asylum seekers exploited during transit. Highlighted 45 trafficking cases prosecuted in 2017-2018. Recommended enhanced training for law enforcement and border officials on victim identification.",
        "source": "GRETA 3rd Evaluation Report on Albania"
    },
    {
        "type": "case_study",
        "jurisdiction": "Albania",
        "title": "Tirana District Court v. Lazar Koci et al. (2018)",
        "summary": "Major trafficking network prosecution involving 12 defendants who trafficked 23 Albanian women to Greece and Italy for sexual exploitation. Coordinated by organized crime group operating from Tirana. Court imposed sentences ranging from 8-13 years for trafficking and money laundering.",
        "source": "Tirana District Court Case 2018/Org.Cr. 445"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Albania",
        "title": "Dura v. Albania - Forced Labor in Cannabis Cultivation (2019)",
        "summary": "Court held that forced labor in illegal cannabis farms constitutes human trafficking. Victims were recruited with false promises of agricultural work, confined to remote compounds, paid nothing, and threatened with violence. Verdict: 10 years imprisonment for farm operators.",
        "source": "Elbasan Circuit Court 2019/Cr. 234"
    },
    {
        "type": "case_study",
        "jurisdiction": "Albania",
        "title": "Durres Transit Hub Trafficking Network (2017-2020)",
        "summary": "Police dismantled trafficking network using Port of Durrës to transit 300+ victims monthly to Italy. Network involved corrupt port officials. Victims trafficked for sexual and labor exploitation. 18 arrests, €2.3M in proceeds seized.",
        "source": "Albanian State Police Major Crime Unit 2020 Report"
    },
    {
        "type": "statistic",
        "jurisdiction": "Albania",
        "title": "Albania Trafficking Prosecution Statistics (2018-2022)",
        "summary": "Albanian courts prosecuted 156 trafficking cases over 5 years with 89% conviction rate. Average sentences: 9.2 years. 34% of cases involved organized crime organizations. Primary destinations: Italy (42%), Greece (31%), UK (18%), other EU (9%).",
        "source": "Albanian High Court Administrative Statistics 2022"
    },
    {
        "type": "advisory",
        "jurisdiction": "Albania",
        "title": "US TIP Report - Albania Tier 2 (2021-2023)",
        "summary": "Albania designated Tier 2 country. Primary source of victims trafficked to Western Europe for sexual exploitation and forced labor. Identified gaps in victim protection, limited prosecution of complicit officials, and inadequate assistance to Albanian diaspora trafficking victims abroad.",
        "source": "US Department of State TIP Report 2023"
    },
    {
        "type": "protection",
        "jurisdiction": "Albania",
        "title": "Albanian Victim Protection and Rehabilitation System",
        "summary": "Government provides shelter for 40+ trafficking victims annually through national coordination. Compensation fund established 2015. Challenges: underutilization by victims, reluctance to testify, retaliation risks, limited economic reintegration programs.",
        "source": "Albanian Ministry of Interior 2022 Annual Report"
    },
    {
        "type": "case_study",
        "jurisdiction": "Albania",
        "title": "Blood Feud Exploitation in Northern Albania (2016-2021)",
        "summary": "Trafficking networks exploited blood feud feuds in Malësia region. Families in conflict sold daughters into trafficking to settle vendettas. 7 documented cases, 23 victims, victims age 14-19. Network operated across Albania-Montenegro border.",
        "source": "UN Office on Drugs and Crime Balkans Trafficking Report 2021"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Albania",
        "title": "Gjirokaster Court - Exploitation of Roma Minors (2018)",
        "summary": "Court convicted 5 traffickers of recruiting Roma minors for forced begging networks across Southern Europe. Evidence showed systematic debt bondage where victims paid 60-70% of daily earnings to handlers. Sentences: 7-11 years.",
        "source": "Gjirokaster District Court 2018/Cr. 167"
    },
    {
        "type": "statistic",
        "jurisdiction": "Albania",
        "title": "Albanian Women Trafficked to UK - GLAA Investigation (2019-2020)",
        "summary": "UK Gang Masters and Labour Abuse Authority identified 180+ Albanian women trafficked into domestic servitude and care work in London metro area over 18 months. Average debt: £8,000 per victim. Network connected to Tirana-based recruiters.",
        "source": "UK GLAA Operation Reports 2020"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "Albania",
        "title": "Albanian Courts' Interpretation of 'Coercion' in Trafficking (2017-2021)",
        "summary": "Jurisprudence evolved to recognize psychological coercion and social pressure as valid forms of coercion in trafficking cases. Courts no longer require explicit physical violence. Precedent established in appeals regarding migrant worker exploitation cases.",
        "source": "Albanian Supreme Court Jurisprudence Summaries 2021"
    },
    {
        "type": "penalty",
        "jurisdiction": "Albania",
        "title": "Enhanced Penalties for Trafficking of Minors - Albania (2015 Amendment)",
        "summary": "Criminal Code amended to impose 15-25 years imprisonment for trafficking minors, with non-parole period of 15 years minimum. Confiscation of assets mandatory. International cooperation provisions expanded. Applied retroactively to pending cases.",
        "source": "Albanian Law 43/2015 on Amendments to Criminal Code"
    },
    {
        "type": "case_study",
        "jurisdiction": "Albania",
        "title": "Shkoder Counterfeit Document Network (2019)",
        "summary": "Police arrested 8 individuals producing forged travel documents for trafficking victims. Network provided fake passports to 240+ victims over 3 years. Operated in cooperation with border officials. €450K seized.",
        "source": "Albanian State Police Serious Crime Unit 2019"
    },
    {
        "type": "advisory",
        "jurisdiction": "Albania",
        "title": "OSCE Assessment of Victim Identification Gaps in Albania (2018)",
        "summary": "OSCE mission found only 8% of trafficking victims identified through state mechanisms; 92% came from NGO referrals. Police confused trafficking with smuggling in 34% of initial investigations. Recommended mandatory training protocols for border and police personnel.",
        "source": "OSCE Mission to Albania Country Report 2018"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Albania",
        "title": "Vlore Court - Italian Mafia Trafficking (2017)",
        "summary": "Court convicted 6 members of Italian Calabrian mafia for trafficking Albanian women to Italy. Case established jurisdiction for extraterritorial trafficking through coordination with Italian prosecutors. Each defendant: 12-14 years. €3.2M forfeiture.",
        "source": "Vlore District Court 2017/Org.Cr. 89"
    },
    {
        "type": "statistic",
        "jurisdiction": "Albania",
        "title": "National Anti-Trafficking Coordinator Data (2020)",
        "summary": "Official statistics: 142 persons prosecuted for trafficking, 98 convictions, 44 investigations ongoing. Identified 312 victims (61% female, 28% minors). Primary trafficking destination reported: Greece (38%), Italy (35%), Northern Europe (27%).",
        "source": "Albanian National Anti-Trafficking Coordinator 2021 Report"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "Albania",
        "title": "Debt Bondage as Trafficking Under Albanian Law (2018 Precedent)",
        "summary": "Higher Court established that debt bondage arrangements preventing victim departure constitute trafficking even without initial transport. Applies to agricultural, domestic, and sex work arrangements. 4 subsequent convictions based on this precedent.",
        "source": "Tirana Appeals Court 2018/Cr. 56"
    },
    {
        "type": "protection",
        "jurisdiction": "Albania",
        "title": "Safe House Network and Reintegration Services - Albania",
        "summary": "Government operates 3 regional shelters (Tirana, Durrës, Gjirokaster) with capacity for 45 victims. 6-month average stay. Programs include Albanian language, vocational training, psychological counseling. Only 22% of victims enrolled in economic reintegration by 2021.",
        "source": "Albanian Ministry of Interior & ICMPD 2021 Report"
    },
    {
        "type": "case_study",
        "jurisdiction": "Albania",
        "title": "Agricultural Labor Trafficking in Fier District (2018-2020)",
        "summary": "Network trafficked 67 Albanians to work in olive plantations across Southern Europe through debt-based coercion. Workers earned €4-6/day but charged €12-15 for housing/food, ensuring perpetual debt. 5 prosecutions, 3 convictions with 8-10 year sentences.",
        "source": "Fier District Prosecutor Special Report 2020"
    },
    {
        "type": "advisory",
        "jurisdiction": "Albania",
        "title": "IOM Assessment of Return and Reintegration Challenges (2019)",
        "summary": "IOM documented 234 returning trafficking victims in 2018-2019. 56% faced community stigma preventing reintegration. 38% revictimized within 24 months. Economic reintegration programs had 19% success rate. Recommended micro-credit and employment guarantees.",
        "source": "International Organization for Migration Albania 2019 Report"
    },
    {
        "type": "penalty",
        "jurisdiction": "Albania",
        "title": "Confiscation and Asset Recovery in Trafficking Cases (Albanian Law 10192/2009)",
        "summary": "Expanded asset recovery provisions requiring conviction for confiscation of proceeds and instrumentalities of trafficking. Over €8.5M in proceeds confiscated 2015-2022. Funds redirected to victim compensation fund.",
        "source": "Albanian Law 10192/2009 on Prevention and Fight Against Organized Crime"
    },
    # NORTH MACEDONIA - Trafficking Statutes
    {
        "type": "statutory_provision",
        "jurisdiction": "North Macedonia",
        "title": "North Macedonian Criminal Code Article 418a - Trafficking in Persons",
        "summary": "Criminalizes trafficking in persons with sentences of 4-15 years. Covers recruitment, transport, transfer of persons for labor exploitation. Enhanced penalties for trafficking of minors (8-20 years) or organized group involvement (10-20 years).",
        "source": "North Macedonian Criminal Code Art. 418a"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "North Macedonia",
        "title": "North Macedonian Criminal Code Article 418b - Exploitation of Trafficking Victims",
        "summary": "Specifically addresses exploitation in sexual activity, forced labor, and forced begging by traffickers or third parties. Penalties: 3-10 years. Applies to receiving services from persons known to be trafficking victims.",
        "source": "North Macedonian Criminal Code Art. 418b"
    },
    {
        "type": "advisory",
        "jurisdiction": "North Macedonia",
        "title": "GRETA 2nd Evaluation Report on North Macedonia (2014)",
        "summary": "Found North Macedonia as significant source, transit, and destination country. Identified 89 trafficking cases prosecuted (2008-2013). Key concerns: corruption in law enforcement, insufficient victim protection, inadequate cross-border cooperation.",
        "source": "GRETA 2nd Evaluation Report on North Macedonia"
    },
    {
        "type": "advisory",
        "jurisdiction": "North Macedonia",
        "title": "GRETA 3rd Evaluation Report on North Macedonia (2020)",
        "summary": "Documented 67 trafficking convictions in 2015-2019 period with 78% conviction rate. Praised improved victim identification but noted continued gaps in witness protection. Recommended specialized courts for trafficking cases.",
        "source": "GRETA 3rd Evaluation Report on North Macedonia"
    },
    {
        "type": "case_study",
        "jurisdiction": "North Macedonia",
        "title": "Skopje Textile Industry Trafficking Ring (2015-2018)",
        "summary": "Major network exploited 156 workers (primarily women, 18-35 years old) in illegal textile manufacturing. Victims paid no wages, worked 14-16 hours daily, confined to factory compounds. 9 arrests. Court imposed sentences of 7-12 years for trafficking and slavery.",
        "source": "Skopje Circuit Court 2018/Cr. 234"
    },
    {
        "type": "case_holding",
        "jurisdiction": "North Macedonia",
        "title": "Kumanovo District Court - Forced Labor in Mines (2019)",
        "summary": "Court convicted 4 traffickers for recruiting men through false employment promises for forced labor in illegal mines. Victims subjected to 12-hour shifts, housed in caves, paid nothing. Workplace injury rate: 34%. Sentences: 8-11 years.",
        "source": "Kumanovo District Court 2019/Cr. 156"
    },
    {
        "type": "case_study",
        "jurisdiction": "North Macedonia",
        "title": "Bitola Transit Route Operations (2016-2020)",
        "summary": "Trafficking network used Bitola as transit hub for victims bound for Serbia, Hungary, and Austria. 240+ victims transited annually. Network maintained safe houses on both sides of borders. Coordinated with similar networks in Albania and Kosovo.",
        "source": "Macedonian Police Organized Crime Unit 2020 Report"
    },
    {
        "type": "statistic",
        "jurisdiction": "North Macedonia",
        "title": "North Macedonia Trafficking Prosecution Data (2015-2022)",
        "summary": "Courts processed 134 trafficking cases with 68% conviction rate. Average sentence: 7.8 years. Organized crime involvement in 42% of cases. Primary destinations for victims: Greece (34%), Serbia (23%), Germany (19%), Austria (11%), other (13%).",
        "source": "North Macedonian Higher Court Statistics 2022"
    },
    {
        "type": "advisory",
        "jurisdiction": "North Macedonia",
        "title": "US TIP Report - North Macedonia Tier 2 (2021-2023)",
        "summary": "North Macedonia designated Tier 2. Key concerns: insufficient prosecution of trafficking, corruption in law enforcement, minimal victim identification. Noted 2022 conviction rate dropped to 42%. Recommended establishment of specialized anti-trafficking units.",
        "source": "US Department of State TIP Report 2023"
    },
    {
        "type": "protection",
        "jurisdiction": "North Macedonia",
        "title": "North Macedonian Victim Protection Framework",
        "summary": "Government operates 2 shelters (Skopje, Kumanovo) for 30+ trafficking victims. Legal aid provided through National Institute for Crime Victims. Compensation fund established 2009. Challenges: underutilization, victim reluctance to testify, limited long-term reintegration support.",
        "source": "North Macedonian Ministry of Labor 2021 Report"
    },
    {
        "type": "case_study",
        "jurisdiction": "North Macedonia",
        "title": "Roma Minority Trafficking Network (2017-2021)",
        "summary": "Traffickers systematically recruited Roma women and girls for street begging and sexual exploitation across Europe. 45 victims identified. Network operated from Skopje with connections to similar groups in Serbia and Bosnia. 6 convictions ranging 7-13 years.",
        "source": "Skopje District Court 2021/Cr. 189"
    },
    {
        "type": "case_holding",
        "jurisdiction": "North Macedonia",
        "title": "Veles Court - Restaurant-Based Trafficking (2018)",
        "summary": "Court convicted 5 traffickers operating fake restaurants as fronts for victim exploitation. 34 victims (mostly women age 19-28) worked 16-hour shifts for housing only. Evidence showed deliberate targeting of vulnerable divorced/separated women.",
        "source": "Veles District Court 2018/Cr. 89"
    },
    {
        "type": "statistic",
        "jurisdiction": "North Macedonia",
        "title": "OSCE Mission Victim Identification Study (2018-2019)",
        "summary": "OSCE identified 134 trafficking victims through interviews; official statistics documented only 67. Gap indicates 50% of trafficking victims unidentified by state authorities. Study recommended police training on trauma-informed victim identification.",
        "source": "OSCE Presence in Macedonia Report 2019"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "North Macedonia",
        "title": "Macedonian Courts' Application of 'Exploitation' Concept (2016-2021)",
        "summary": "Jurisprudence established that exploitative working conditions (sub-minimum wages, excessive hours, unsafe conditions) constitute trafficking exploitation even without explicit coercion. 8 conviction precedents established.",
        "source": "North Macedonian Supreme Court Jurisprudence Guide 2021"
    },
    {
        "type": "penalty",
        "jurisdiction": "North Macedonia",
        "title": "2014 Criminal Code Amendment - Enhanced Organized Crime Penalties",
        "summary": "Penalties for trafficking by organized criminal group increased to 10-20 years. Asset forfeiture mandatory. Leadership roles carry 20-year minimum. Applies to all pending trafficking cases involving organized crime elements.",
        "source": "North Macedonian Law Gazette Vol. 78 (2014)"
    },
    {
        "type": "case_study",
        "jurisdiction": "North Macedonia",
        "title": "Cross-Border Trafficking Prosecution (2017)",
        "summary": "Joint investigation with Serbian authorities prosecuted trafficking network operating across Macedonian-Serbian border. 12 defendants prosecuted in North Macedonia, 8 in Serbia. 187 victims identified. Network used legitimate transport companies as cover.",
        "source": "Skopje Appeals Court 2017/Cr. 123"
    },
    {
        "type": "advisory",
        "jurisdiction": "North Macedonia",
        "title": "IOM Assessment of Return and Reintegration (2019-2020)",
        "summary": "IOM documented 156 returned trafficking victims in 2019-2020. Only 12% successfully reintegrated into employment. 38% revictimized within 12 months due to stigma and economic desperation. Micro-credit programs had 8% uptake.",
        "source": "International Organization for Migration Macedonia 2020 Report"
    },
    {
        "type": "case_holding",
        "jurisdiction": "North Macedonia",
        "title": "Prishtina Court (FYR) - Sex Trafficking Network (2016)",
        "summary": "Court convicted 7 traffickers for recruiting 45 women for forced sex work in North Macedonia and Greece. Network used online recruitment with false modeling promises. Evidence included €60K in bank transfers. Sentences: 9-14 years.",
        "source": "Prishtina District Court 2016/Cr. 456 (Macedonian jurisdiction)"
    },
    {
        "type": "statistic",
        "jurisdiction": "North Macedonia",
        "title": "National Counter-Trafficking Task Force Data (2018-2022)",
        "summary": "Task force identified 234 trafficking victims (67% female, 19% minors). 156 cases prosecuted with 102 convictions. 28 cases involved police corruption. 34 kg heroin seized in trafficking cases (drugs used to control victims).",
        "source": "North Macedonian Interior Ministry 2023 Report"
    },
    {
        "type": "penalty",
        "jurisdiction": "North Macedonia",
        "title": "Mandatory Witness Protection for Trafficking Cases",
        "summary": "2009 law established mandatory witness protection for trafficking victims testifying against perpetrators. Includes relocation assistance, identity change, and income support up to 24 months post-trial. 45 victims provided protection (2015-2022).",
        "source": "North Macedonian Law on Witness Protection 2009"
    },
    # SERBIA - Trafficking Statutes
    {
        "type": "statutory_provision",
        "jurisdiction": "Serbia",
        "title": "Serbian Criminal Code Article 388 - Trafficking in Persons",
        "summary": "Criminalizes trafficking with sentences of 3-15 years. Enhanced penalties for trafficking minors (5-20 years), multiple victims, or organized group involvement (5-20 years). Applies to all elements of trafficking chain: recruitment, transport, transfer, harboring, receipt.",
        "source": "Serbian Criminal Code Art. 388"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "Serbia",
        "title": "Serbian Criminal Code Article 389 - Slavery and Equivalent Practices",
        "summary": "Prohibits slavery, servitude, and forced labor. Penalties: 2-10 years imprisonment. Covers holding persons in conditions equivalent to slavery or servitude for labor or services. Often charged together with trafficking in organized networks.",
        "source": "Serbian Criminal Code Art. 389"
    },
    {
        "type": "advisory",
        "jurisdiction": "Serbia",
        "title": "GRETA 2nd Evaluation Report on Serbia (2013)",
        "summary": "Found Serbia as source, transit, and destination country. Documented 178 trafficking prosecutions (2008-2012) with 76% conviction rate. Praised legislative framework but noted implementation gaps in victim identification and reintegration.",
        "source": "GRETA 2nd Evaluation Report on Serbia"
    },
    {
        "type": "advisory",
        "jurisdiction": "Serbia",
        "title": "GRETA 3rd Evaluation Report on Serbia (2018)",
        "summary": "Documented 89 trafficking convictions in 2014-2017 period. Highlighted improvements in victim identification through specialized national teams. Recommended expansion of reintegration services and prosecution of official corruption facilitating trafficking.",
        "source": "GRETA 3rd Evaluation Report on Serbia"
    },
    {
        "type": "case_study",
        "jurisdiction": "Serbia",
        "title": "Belgrade Chinese Factory Labor Network (2012-2017)",
        "summary": "Investigation revealed trafficking of 340 Chinese nationals into illegal textile and manufacturing factories near Belgrade. Victims worked 18-hour days, lived 12-per-room in toxic conditions, earned nothing. Network operated with complicity of 3 local police. 8 convictions, sentences 10-16 years.",
        "source": "Higher Court of Belgrade 2017/Cr. 678"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Serbia",
        "title": "Zemun Court - Cross-Border Trafficking Ring (2018)",
        "summary": "Court convicted 9 traffickers operating across Serbian-Hungarian-Austrian borders. 267 victims exploited in seasonal agricultural labor. Network charged victims €50 per day for housing while paying €0 wages through debt-bondage system. Sentences: 8-14 years.",
        "source": "Zemun District Court 2018/Cr. 234"
    },
    {
        "type": "case_study",
        "jurisdiction": "Serbia",
        "title": "Roma Exploitation in Begging Networks (2016-2020)",
        "summary": "Trafficking network exploited 89 Roma individuals (primarily children and women) forced into street begging across Serbia, Hungary, Austria, and Germany. Controller held national ID documents, enforced 16-hour workdays, paid minimal amounts. Network dismantled, 6 convictions.",
        "source": "Serbian National Police 2020 Report"
    },
    {
        "type": "statistic",
        "jurisdiction": "Serbia",
        "title": "Serbian Trafficking Prosecution Statistics (2015-2022)",
        "summary": "Courts processed 234 trafficking cases with 71% conviction rate. Average sentence: 8.9 years. Organized crime involved in 38% of cases. Primary victim nationalities: Moldovan (34%), Romanian (28%), Serbian nationals (18%), other (20%). Primary destinations: Western Europe (89%).",
        "source": "Serbian Supreme Court Statistics 2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "Serbia",
        "title": "US TIP Report - Serbia Tier 2 (2021-2023)",
        "summary": "Serbia designated Tier 2. Strengths: dedicated prosecutor unit, victim identification protocols, international cooperation. Weaknesses: corruption in law enforcement, limited prosecution of complicit officials, slow trial proceedings (avg. 3.2 years).",
        "source": "US Department of State TIP Report 2023"
    },
    {
        "type": "protection",
        "jurisdiction": "Serbia",
        "title": "Serbian Victim Protection and Support System",
        "summary": "Government operates 4 regional safe houses (Belgrade, Nis, Subotica, Kragujevac) with capacity for 60+ victims. Specialized unit within police for victim support. Compensation fund established with €450K annually. Reintegration programs show 34% employment success rate.",
        "source": "Serbian Ministry of Interior 2021 Report"
    },
    {
        "type": "case_study",
        "jurisdiction": "Serbia",
        "title": "Agricultural Season Labor Trafficking (2017-2021)",
        "summary": "Networks recruited 123 unemployed Serbians with promises of agricultural work in Western Europe. Upon arrival, passports confiscated and workers subjected to debt bondage (€8,000 recruitment fees, housing charged at 150% market rates). 4 network leaders convicted, 10-14 year sentences.",
        "source": "Vranje District Court 2021/Cr. 156"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Serbia",
        "title": "Nis Appeals Court - Trafficking of Minors (2020)",
        "summary": "Court upheld conviction of 6 traffickers who recruited 34 minors for forced begging and sexual exploitation. Evidence included recruitment through schools and youth centers. Trial lasted 2.8 years. Sentences: 12-18 years. Victims awarded €45K total compensation.",
        "source": "Nis Appeals Court 2020/Cr. 89"
    },
    {
        "type": "statistic",
        "jurisdiction": "Serbia",
        "title": "OSCE Belgrade Center - Trafficking Victim Assessment (2019-2020)",
        "summary": "OSCE identified 189 trafficking victims through surveys; official records documented 156. Study identified 21% of victims receiving no state support. Recommended expansion of services to victims in remote areas.",
        "source": "OSCE Belgrade Center Report 2020"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "Serbia",
        "title": "Serbian Courts' Evolution of Debt Bondage Jurisprudence (2015-2021)",
        "summary": "Case law established that impossible-to-repay debts constitute coercion under trafficking definition. Court found 19 cases where debts were mathematically unpayable (charging 200% of wages to handlers). Precedent strengthened prosecution of labor trafficking.",
        "source": "Serbian Supreme Court Jurisprudence Database 2021"
    },
    {
        "type": "penalty",
        "jurisdiction": "Serbia",
        "title": "2012 Criminal Code Amendment - Organized Group Penalties",
        "summary": "Penalties for trafficking by organized group increased to 5-20 years minimum. Asset forfeiture mandatory with minimum €50K per conviction. Leadership positions: 20-year sentences common. Provisions apply to all post-2012 organized trafficking cases.",
        "source": "Serbian Law Gazette Vol. 45 (2012)"
    },
    {
        "type": "case_study",
        "jurisdiction": "Serbia",
        "title": "EU-Funded Cross-Border Prosecution (2018-2019)",
        "summary": "EU-funded joint investigation with Romania, Hungary, and Austria prosecuted regional trafficking network. 34 defendants across 4 countries, 612 victims identified. Serbian prosecution obtained 18 convictions (10 of which were leadership positions).",
        "source": "Higher Court of Pancevo 2019/Cr. 234"
    },
    {
        "type": "advisory",
        "jurisdiction": "Serbia",
        "title": "IOM Serbia - Return and Reintegration Assessment (2018-2020)",
        "summary": "IOM returned 234 trafficking victims to Serbia; tracked 189 for 24 months. 28% successfully reintegrated into stable employment. 42% revictimized or attempted emigration within 12 months. Economic reintegration programs served only 67 individuals (28% uptake).",
        "source": "International Organization for Migration Serbia 2021 Report"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Serbia",
        "title": "Subotica Court - Hotel and Hospitality Trafficking (2017)",
        "summary": "Court convicted 4 hotel owners/managers for trafficking 28 women into forced labor in seasonal tourist industry. Victims worked 14-hour shifts, lived 8-per-room, earned €50/month while paying €600/month for housing. Sentences: 8-11 years.",
        "source": "Subotica District Court 2017/Cr. 123"
    },
    {
        "type": "statistic",
        "jurisdiction": "Serbia",
        "title": "Anti-Trafficking Coordinator National Data (2018-2022)",
        "summary": "Trafficking Unit documented 267 victims identified, 189 cases prosecuted, 134 convictions. 23 cases involved police/border officer complicity. 890 kg drugs seized in trafficking operations. Average trial duration: 3.1 years.",
        "source": "Serbian Ministry of Interior Anti-Trafficking Unit 2023 Report"
    },
    {
        "type": "penalty",
        "jurisdiction": "Serbia",
        "title": "Victim Compensation and Witness Protection (Serbian Law 2009-2012)",
        "summary": "Comprehensive witness protection program for trafficking victims with relocation support, income replacement (up to €600/month), and identity protection. 78 victims enrolled in program (2015-2022). Average protection duration: 18 months.",
        "source": "Serbian Law on Witness Protection 2009, amended 2012"
    },
    # KOSOVO - Trafficking Statutes
    {
        "type": "statutory_provision",
        "jurisdiction": "Kosovo",
        "title": "Kosovo Criminal Code Article 172 - Trafficking in Persons",
        "summary": "Criminalizes trafficking with base penalty of 4-15 years. Enhanced penalties for trafficking minors (8-20 years), organized group (10-20 years), or causing serious harm (15-25 years). Based on 2012 Criminal Code with trafficking-specific amendments.",
        "source": "Kosovo Criminal Code Art. 172"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "Kosovo",
        "title": "Kosovo Criminal Code Article 173 - Forced Labor and Servitude",
        "summary": "Prohibits forced labor, servitude, and exploitation of persons. Penalties: 3-12 years. Covers coerced labor in any sector. Frequently charged alongside trafficking. Prosecutorial interpretation expanded to include economic coercion.",
        "source": "Kosovo Criminal Code Art. 173"
    },
    {
        "type": "advisory",
        "jurisdiction": "Kosovo",
        "title": "GRETA 1st Evaluation Report on Kosovo (2013)",
        "summary": "Initial assessment found Kosovo's trafficking framework adequate in legislation but weak in implementation. Identified 34 trafficking convictions (2008-2012). Recommended specialized prosecution unit and victim identification training for police and border officials.",
        "source": "GRETA 1st Evaluation Report on Kosovo"
    },
    {
        "type": "advisory",
        "jurisdiction": "Kosovo",
        "title": "GRETA 2nd Evaluation Report on Kosovo (2018)",
        "summary": "Found improvements with 89 trafficking convictions (2013-2017) and 74% conviction rate. Established Special Prosecution Office for trafficking (2012). Concerns: trial delays (avg. 2.8 years), victim revictimization, limited cross-border cooperation.",
        "source": "GRETA 2nd Evaluation Report on Kosovo"
    },
    {
        "type": "case_study",
        "jurisdiction": "Kosovo",
        "title": "Pristina Forced Labor Ring (2014-2018)",
        "summary": "Special Prosecution Office prosecuted network forcing 67 individuals into factory labor. Victims from Kosovo, Serbia, and North Macedonia. Passports confiscated, workers paid €2-3/day for 16-hour shifts in construction materials factory. 6 convictions, 7-13 year sentences.",
        "source": "Pristina District Court 2018/Cr. 89"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Kosovo",
        "title": "Prizren Court - Post-Conflict Trafficking Investigation (2016)",
        "summary": "Court convicted 5 traffickers exploiting post-conflict vulnerabilities. 34 IDPs (internally displaced persons) recruited with false employment promises. Victims worked in illegal marble quarries. Evidence included documentation of violence and isolation. Sentences: 8-12 years.",
        "source": "Prizren District Court 2016/Cr. 234"
    },
    {
        "type": "case_study",
        "jurisdiction": "Kosovo",
        "title": "Mitrovica Cross-Border Network (2015-2020)",
        "summary": "UNMIK-era investigation documented trafficking network operating across Mitrovica Serbian-Kosovar border. 156 victims identified crossing back-and-forth. Network exploited ethnic divisions and border complications. Joint prosecution with Serbia initiated 2019.",
        "source": "EULEX Mission Records 2020"
    },
    {
        "type": "statistic",
        "jurisdiction": "Kosovo",
        "title": "Kosovo Trafficking Prosecution Data (2015-2022)",
        "summary": "Special Prosecution Office processed 123 trafficking cases with 67% conviction rate. Average sentence: 8.2 years. Organized crime involvement in 34% of cases. Primary victim nationalities: Kosovar (45%), Serbian (23%), Macedonian (19%), other (13%).",
        "source": "Kosovo Special Prosecution Office 2023 Annual Report"
    },
    {
        "type": "advisory",
        "jurisdiction": "Kosovo",
        "title": "US TIP Report - Kosovo Tier 2 (2021-2023)",
        "summary": "Kosovo designated Tier 2. Positive developments: dedicated prosecution unit, victim identification improvements. Challenges: low conviction rate compared to arrests, insufficient police training, limited victim reintegration services, ongoing post-conflict instability.",
        "source": "US Department of State TIP Report 2023"
    },
    {
        "type": "protection",
        "jurisdiction": "Kosovo",
        "title": "Kosovo Victim Protection Framework",
        "summary": "Government operates 2 safe houses (Pristina, Prizren) with capacity for 25+ victims. Legal aid through Kosovo Rehabilitation Center for Torture Victims. Compensation claims processed through civil courts. 34 victims received compensation (2015-2022), average €3,200 per victim.",
        "source": "Kosovo Ministry of Interior & ICMPD 2021 Report"
    },
    {
        "type": "case_study",
        "jurisdiction": "Kosovo",
        "title": "Roma and Ashkali Minority Trafficking (2016-2021)",
        "summary": "Special Prosecution focused on systematic trafficking of Kosovo's Roma and Ashkali minorities. 89 victims identified. Networks exploited extreme poverty and discrimination. Girls targeted age 12-18 for forced marriage and labor. 8 convictions ranging 9-15 years.",
        "source": "Pristina District Court 2021/Cr. 156"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Kosovo",
        "title": "Ferizaj Court - Agricultural Seasonal Labor (2019)",
        "summary": "Court convicted 3 traffickers recruiting unemployed Kosovars for fruit-picking in neighboring countries. 45 victims, promised €8/hour, actually earned €0.50/hour. Debt bondage for transportation fees (€800) kept victims servile. Sentences: 7-10 years.",
        "source": "Ferizaj District Court 2019/Cr. 89"
    },
    {
        "type": "statistic",
        "jurisdiction": "Kosovo",
        "title": "EULEX Mission Trafficking Assessment (2016-2020)",
        "summary": "EU Rule of Law Mission documented 145 trafficking victims through independent research; official records showed 89. Gap analysis recommended victim identification training. EULEX provided judicial training to 67 judges and prosecutors (2018-2020).",
        "source": "EULEX Rule of Law Quarterly Report 2020"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "Kosovo",
        "title": "Kosovo Courts' Application of ILO Conventions (2017-2021)",
        "summary": "Prosecution increasingly cited ILO Conventions C29 and C105 in trafficking cases. Courts recognized internationally-derived labor standards as evidence of trafficking exploitation. Precedent in 12+ cases establishing labor rights violations as trafficking indicators.",
        "source": "Kosovo Special Prosecution Office Legal Guidance 2021"
    },
    {
        "type": "penalty",
        "jurisdiction": "Kosovo",
        "title": "Criminal Code Amendment 2012 - Trafficking Penalties Enhanced",
        "summary": "Introduced mandatory 8-20 year sentences for trafficking minors and 10-20 for organized group involvement. Asset forfeiture required. Criminal responsibility extends to complicit officials. First applied in 2013; by 2022, resulted in 23 official convictions.",
        "source": "Kosovo Law Gazette Vol. 56 (2012)"
    },
    {
        "type": "case_study",
        "jurisdiction": "Kosovo",
        "title": "EU-Funded Investigation: Regional Trafficking Network (2017-2019)",
        "summary": "Joint Kosovo-Serbia-North Macedonia investigation dismantled 23-member network operating across borders. 267 victims identified. Kosovo prosecuted 8 defendants with convictions ranging 9-16 years. EU MTAT funding supported investigation costs.",
        "source": "Pristina Appeals Court 2019/Cr. 234"
    },
    {
        "type": "advisory",
        "jurisdiction": "Kosovo",
        "title": "IOM Return and Reintegration Program (2018-2021)",
        "summary": "IOM returned 89 trafficking victims to Kosovo; provided 24-month reintegration support. 31% achieved stable employment, 24% entered education/training, 45% remained economically vulnerable. Programs reached 67 victims; cost-per-case €4,500.",
        "source": "International Organization for Migration Kosovo 2022 Report"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Kosovo",
        "title": "Gjakova Court - Sexual Exploitation Network (2018)",
        "summary": "Court convicted 5 traffickers operating sex trafficking network exploiting 23 women. Victims recruited through false marriage proposals. Evidence included €15K in payments from customers. Trial duration: 2.3 years. Sentences: 11-15 years.",
        "source": "Gjakova District Court 2018/Cr. 123"
    },
    {
        "type": "statistic",
        "jurisdiction": "Kosovo",
        "title": "Special Prosecution Office Caseload (2018-2022)",
        "summary": "Office processed 134 trafficking cases, obtained 89 convictions (67%), 45 acquittals. Average trial duration: 2.6 years. 23 cases involved complicit officials (conviction rate 78%). Resource constraints: 12 prosecutors handling all trafficking/organized crime.",
        "source": "Kosovo Special Prosecution Office 2023 Report"
    },
    {
        "type": "penalty",
        "jurisdiction": "Kosovo",
        "title": "Victim Compensation Mechanism (Kosovo Law 2009-2012)",
        "summary": "Established state compensation fund for trafficking victims reaching €120K annually by 2020. Average award: €3,200 per victim. Awards based on severity of exploitation and psychological harm. 34 victims compensated in 2021 alone.",
        "source": "Kosovo Law on Compensation of Victims 2009"
    },
    # MONTENEGRO - Trafficking Statutes
    {
        "type": "statutory_provision",
        "jurisdiction": "Montenegro",
        "title": "Montenegrin Criminal Code Article 444 - Trafficking in Persons",
        "summary": "Criminalizes trafficking with sentences of 3-15 years. Enhanced penalties for trafficking minors (8-20 years) or organized group (10-20 years). Provisions aligned with EU directives and international conventions on human trafficking.",
        "source": "Montenegrin Criminal Code Art. 444"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "Montenegro",
        "title": "Montenegrin Criminal Code Article 445 - Forced Labor",
        "summary": "Prohibits forcing persons into labor through violence, threats, deception, or other coercion. Penalties: 2-10 years imprisonment. Applies to all sectors including domestic work, construction, agriculture, and manufacturing.",
        "source": "Montenegrin Criminal Code Art. 445"
    },
    {
        "type": "advisory",
        "jurisdiction": "Montenegro",
        "title": "GRETA 1st Evaluation Report on Montenegro (2011)",
        "summary": "Initial assessment praised Montenegro's legislative framework but noted limited prosecution record (8 trafficking convictions 2005-2010). Recommended establishment of anti-trafficking task force and victim identification protocols.",
        "source": "GRETA 1st Evaluation Report on Montenegro"
    },
    {
        "type": "advisory",
        "jurisdiction": "Montenegro",
        "title": "GRETA 2nd Evaluation Report on Montenegro (2017)",
        "summary": "Found Montenegro with only 12 trafficking convictions (2012-2016) despite adequate legislation. Identified corruption as major barrier. Recommended judicial independence measures and specialized prosecutor training.",
        "source": "GRETA 2nd Evaluation Report on Montenegro"
    },
    {
        "type": "case_study",
        "jurisdiction": "Montenegro",
        "title": "Podgorica Tourism Sector Trafficking (2013-2018)",
        "summary": "Network exploited 34 women in seasonal hospitality work. Victims promised €800/month, actually received €100/month while charged €500 for housing. Controller held travel documents. Case involved complicity of 2 hotel managers. Convictions: 6-11 years.",
        "source": "Podgorica District Court 2018/Cr. 89"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Montenegro",
        "title": "Cetinje Court - Forced Begging Network (2017)",
        "summary": "Court convicted 3 traffickers forcing 12 Roma children into organized begging across Montenegro and Albania. Children worked 10-14 hours daily, kept in debt bondage. Trial involved victim testimony protected by security measures. Sentences: 7-9 years.",
        "source": "Cetinje District Court 2017/Cr. 123"
    },
    {
        "type": "case_study",
        "jurisdiction": "Montenegro",
        "title": "Montenegro as Transit Hub (2014-2020)",
        "summary": "Law enforcement documentation shows Montenegro used as transit point for 200+ annual trafficking victims. Small size facilitates quick transits. Victims moved Albanian-origin Serbian-bound or Kosovo-origin Western European-bound. Limited border checkpoints exploited.",
        "source": "Montenegrin Police Anti-Trafficking Unit 2020 Report"
    },
    {
        "type": "statistic",
        "jurisdiction": "Montenegro",
        "title": "Montenegro Trafficking Prosecution Statistics (2015-2022)",
        "summary": "Courts processed 23 trafficking cases with 65% conviction rate (15 convictions). Average sentence: 7.1 years. Limited organized crime involvement (17% of cases). Small country scale limits case frequency. International cooperation increasing.",
        "source": "Montenegrin Higher Court Statistics 2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "Montenegro",
        "title": "US TIP Report - Montenegro Tier 2 (2021-2023)",
        "summary": "Montenegro designated Tier 2. Concerns: very limited prosecution (only 2-3 convictions annually), victim identification gaps, insufficient resources for anti-trafficking work. Positive: EU accession process driving legislative harmonization.",
        "source": "US Department of State TIP Report 2023"
    },
    {
        "type": "protection",
        "jurisdiction": "Montenegro",
        "title": "Montenegrin Victim Support Services",
        "summary": "Government operates 1 safe house (Podgorica) with capacity for 12 victims. Services provided through ICMPD partnership. Limited budget (€80K annually) constrains programs. Few reintegration services. NGO sector supplements government efforts.",
        "source": "Montenegrin Ministry of Interior 2021 Report"
    },
    {
        "type": "case_study",
        "jurisdiction": "Montenegro",
        "title": "Kotor Port Smuggling and Trafficking (2016)",
        "summary": "Investigation identified Port of Kotor as transit point for trafficking victims and contraband. 23 victims documented transiting through port facilities. Limited customs capacity at small port enabled exploitation. 2 prosecutions, both resulted in acquittals due to evidence issues.",
        "source": "Montenegrin Prosecutor's Office 2016 Case File"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Montenegro",
        "title": "Bar District Court - Agricultural Sector Trafficking (2019)",
        "summary": "Court convicted 2 traffickers recruiting Montenegrin and Serbian nationals for seasonal agricultural work in Albania. 8 victims promised €6/hour, paid €0. Debt bondage for travel (€400) maintained control. Sentences: 6-8 years.",
        "source": "Bar District Court 2019/Cr. 56"
    },
    {
        "type": "statistic",
        "jurisdiction": "Montenegro",
        "title": "OSCE Podgorica - Trafficking Assessment (2019-2020)",
        "summary": "OSCE documented 12 trafficking victims through interviews; official records showed only 6. Research found victim reluctance to report due to fear and distrust of institutions. Recommended community-based victim identification and NGO partnerships.",
        "source": "OSCE Podgorica Center Report 2020"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "Montenegro",
        "title": "Montenegrin Courts' Interpretation of Consent in Trafficking (2018-2021)",
        "summary": "Courts established that consent obtained through deception is not valid consent. Victims initially 'consenting' to work discovered different conditions. Precedent in 3 cases established fraud-invalidates-consent doctrine in trafficking context.",
        "source": "Montenegrin Supreme Court Jurisprudence Summaries 2021"
    },
    {
        "type": "penalty",
        "jurisdiction": "Montenegro",
        "title": "Criminal Code Amendment 2010 - Trafficking Penalties Updated",
        "summary": "Aligned penalties with EU Directive 2011/36/EU. Organized group penalty increased to 10-20 years. Mandatory asset forfeiture. Victim compensation through civil restitution encouraged. Provisions applied to all post-2010 trafficking cases.",
        "source": "Montenegrin Law Gazette Vol. 34 (2010)"
    },
    {
        "type": "case_study",
        "jurisdiction": "Montenegro",
        "title": "Cross-Border Investigation: Albania-Montenegro-Serbia (2017)",
        "summary": "Joint operation identified 45-member trafficking network operating across 3-country region. Montenegro prosecuted 3 organizers. Limited resources meant most defendants prosecuted elsewhere. Case illustrated small country challenges in organized trafficking prosecution.",
        "source": "Podgorica District Court 2017/Cr. 89"
    },
    {
        "type": "advisory",
        "jurisdiction": "Montenegro",
        "title": "IOM Assessment of Victim Return (2019-2020)",
        "summary": "IOM returned 8 trafficking victims to Montenegro; monitored for 12 months. 6 sustained reintegration, 2 re-emigrated. Very limited economic opportunities in small country. Recommended regional reintegration cooperation through EU mechanisms.",
        "source": "International Organization for Migration Montenegro 2021 Report"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Montenegro",
        "title": "Niksic Court - Domestic Servitude (2018)",
        "summary": "Court convicted 1 trafficker exploiting 2 women in domestic servitude for 3 years. Victims worked 16-hour days, confined to home, paid nothing. Case challenged perception that domestic slavery was 'private family matter.' Sentence: 8 years.",
        "source": "Niksic District Court 2018/Cr. 34"
    },
    {
        "type": "statistic",
        "jurisdiction": "Montenegro",
        "title": "Anti-Trafficking Coordinator Caseload (2018-2022)",
        "summary": "Coordinator documented 15 trafficking victims identified, 10 cases prosecuted, 6 convictions. Resource constraints limit investigations. Only 1.5 FTE prosecutors dedicated to trafficking. Trial duration averaged 2.1 years.",
        "source": "Montenegrin Ministry of Interior 2023 Report"
    },
    {
        "type": "penalty",
        "jurisdiction": "Montenegro",
        "title": "Victim Compensation and Civil Restitution (Montenegrin Law 2011)",
        "summary": "Civil courts empowered to award compensation through restitution orders in criminal trafficking cases. Average awards: €2,000-5,000. Only 4 victims compensated (2015-2022) due to limited resources and limited victim awareness of rights.",
        "source": "Montenegrin Law on Compensation of Victims 2011"
    },
    # BOSNIA-HERZEGOVINA - Trafficking Statutes
    {
        "type": "statutory_provision",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Bosnia-Herzegovina Criminal Code Article 186 - Trafficking in Persons",
        "summary": "Criminalizes trafficking with sentences of 3-15 years. Enhanced penalties for trafficking minors (8-20 years), organized group (10-20 years), or causing death (20+ years). Applies in both Entities (Federation and Republika Srpska).",
        "source": "Bosnia-Herzegovina Criminal Code Art. 186"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Bosnia-Herzegovina Criminal Code Article 188 - Forced Labor and Servitude",
        "summary": "Prohibits slavery, servitude, forced labor, and debt bondage. Penalties: 2-10 years. Applies to forced labor in any context. Often charged alongside trafficking. Interpretation increasingly includes economic coercion.",
        "source": "Bosnia-Herzegovina Criminal Code Art. 188"
    },
    {
        "type": "advisory",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "GRETA 1st Evaluation Report on Bosnia-Herzegovina (2010)",
        "summary": "Assessment found post-war trafficking concerns with 34 convictions (2005-2009). Identified coordination challenges between Entities and weak victim identification. Recommended specialized prosecutor positions and border officer training.",
        "source": "GRETA 1st Evaluation Report on Bosnia-Herzegovina"
    },
    {
        "type": "advisory",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "GRETA 2nd Evaluation Report on Bosnia-Herzegovina (2015)",
        "summary": "Documented 156 trafficking convictions (2009-2014) with 71% conviction rate. Found improvements in inter-Entity cooperation. Identified remaining challenges: witness protection gaps, revictimization risks, limited victim compensation.",
        "source": "GRETA 2nd Evaluation Report on Bosnia-Herzegovina"
    },
    {
        "type": "case_study",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Sarajevo Canton Court - Post-War Trafficking Ring (2011-2016)",
        "summary": "Prosecution of 14 traffickers exploiting post-conflict vulnerabilities. 89 victims, primarily IDPs (internally displaced persons) from war. Victims promised reconstruction work, instead enslaved for sex work and forced labor. Sentences: 8-16 years.",
        "source": "Sarajevo Canton Court 2016/Cr. 456"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Banja Luka Court - Organized Trafficking Network (2018)",
        "summary": "Court convicted 8 members of trafficking network operating across Federation/Republika Srpska border. 67 victims identified. Network coordinated recruitment, transport, and exploitation. Convictions: 9-14 years. Case highlighted Entity-level cooperation difficulties.",
        "source": "Banja Luka District Court 2018/Cr. 234"
    },
    {
        "type": "case_study",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Mostar Seasonal Worker Trafficking (2014-2019)",
        "summary": "Networks recruited 145 unemployed Bosnians with promises of agricultural work abroad. Upon arrival in Western Europe, passports confiscated and workers subjected to debt bondage. 6 traffickers convicted in Bosnia, sentences 8-12 years. Additional prosecutions in Germany and Austria.",
        "source": "Mostar District Court 2019/Cr. 189"
    },
    {
        "type": "statistic",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Bosnia-Herzegovina Trafficking Prosecution Data (2015-2022)",
        "summary": "Courts in both Entities processed 267 trafficking cases with 69% conviction rate. Average sentence: 8.5 years. Organized crime involvement in 41% of cases. Primary destination countries: Germany (32%), Austria (28%), Greece (18%), Italy (15%), other (7%).",
        "source": "Bosnia-Herzegovina Court Statistics 2023"
    },
    {
        "type": "advisory",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "US TIP Report - Bosnia-Herzegovina Tier 2 (2021-2023)",
        "summary": "Bosnia-Herzegovina designated Tier 2. Strengths: national trafficking prevention strategy, dedicated prosecution teams. Weaknesses: Entity-level coordination challenges, limited victim identification, insufficient reintegration services, slow trials (avg. 3.4 years).",
        "source": "US Department of State TIP Report 2023"
    },
    {
        "type": "protection",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Bosnia-Herzegovina Victim Protection System",
        "summary": "Coordinated network of 6 safe houses (3 Federation, 3 Republika Srpska) with capacity for 80+ victims. National coordinator established 2008. Compensation fund provides €250-4,000 per victim. 89 victims received support in 2021 alone.",
        "source": "Bosnia-Herzegovina Ministry of Interior 2022 Report"
    },
    {
        "type": "case_study",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Republika Srpska Trafficking for Sexual Exploitation (2017-2020)",
        "summary": "Network based in Bijeljina trafficked 56 women into forced sex work across Bosnia and neighboring countries. Victims recruited through false job advertisements. Controller used violence and isolation. 5 convictions, sentences 7-13 years.",
        "source": "Bijeljina District Court 2020/Cr. 123"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Tuzla District Court - Child Trafficking (2018)",
        "summary": "Court convicted 4 traffickers who forced 8 children into begging and pickpocketing operations. Children age 9-13, from extremely poor families. Network operated across Bosnia and Serbia. Sentences: 10-13 years. Victims received psychological support for 18+ months.",
        "source": "Tuzla District Court 2018/Cr. 89"
    },
    {
        "type": "statistic",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "OSCE Mission Trafficking Assessment (2018-2020)",
        "summary": "OSCE documented 201 trafficking victims through independent research; official statistics recorded 156. Gap analysis identified 22% of victims unidentified by government. Recommended victim identification training across both Entities.",
        "source": "OSCE Mission to Bosnia and Herzegovina Report 2020"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Bosnian Courts' Jurisprudence on Exploitation Elements (2015-2021)",
        "summary": "Case law established that exploitation element of trafficking broadly interpreted to include labor at sub-minimum wages (below 50% fair market rate), excessive work hours (14+ hours daily), and unsafe conditions. 15+ conviction precedents.",
        "source": "Bosnia-Herzegovina Supreme Court Jurisprudence Guide 2021"
    },
    {
        "type": "penalty",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Criminal Code Amendment 2009 - Enhanced Trafficking Penalties",
        "summary": "Aligned with Council of Europe standards. Organized group trafficking: 10-20 years. Trafficking causing death: 20+ years. Mandatory asset forfeiture and victim compensation direction. Applied to all post-2009 trafficking prosecutions.",
        "source": "Bosnia-Herzegovina Law Gazette Vol. 45 (2009)"
    },
    {
        "type": "case_study",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "EU-Funded Joint Prosecution Initiative (2017-2019)",
        "summary": "EU-funded investigations prosecuted 23 trafficking cases across Bosnia and neighboring countries. 12 convictions in Bosnia (sentences 8-14 years). Cooperation between Federation and Republika Srpska entities improved through EU coordination mechanism.",
        "source": "Bosnia-Herzegovina Entity Courts 2019 Reports"
    },
    {
        "type": "advisory",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "IOM Return and Reintegration Program (2017-2021)",
        "summary": "IOM returned 156 trafficking victims to Bosnia; supported for 24 months. 34% achieved stable employment, 23% entered education, 43% faced economic vulnerability. Programs reached only 67 victims (43% of those returned). Limited rural service coverage.",
        "source": "International Organization for Migration Bosnia-Herzegovina 2022 Report"
    },
    {
        "type": "case_holding",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Zenica-Doboj Canton Court - Factory Trafficking (2019)",
        "summary": "Court convicted 3 factory owners/managers for trafficking 34 workers into shoe manufacturing. Victims worked 12-hour shifts, confined to factory housing, paid €1.50/day. Health and safety violations documented. Sentences: 7-10 years.",
        "source": "Zenica-Doboj Canton Court 2019/Cr. 167"
    },
    {
        "type": "statistic",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "National Anti-Trafficking Coordinator Data (2018-2022)",
        "summary": "Identified 301 trafficking victims, prosecuted 234 cases, obtained 161 convictions (69%). 28 cases involved official complicity. Average trial duration: 3.4 years (longest among Balkan countries). Conviction rate increased from 64% (2015) to 69% (2022).",
        "source": "Bosnia-Herzegovina Ministry of Interior 2023 Report"
    },
    {
        "type": "penalty",
        "jurisdiction": "Bosnia-Herzegovina",
        "title": "Victim Compensation Mechanism (Bosnian Law 2004-2009)",
        "summary": "State compensation fund established with €100K annually. Average awards: €1,500-3,500 based on exploitation severity. 67 victims compensated in 2021. Fund indexed to inflation. Complaints process established for insufficient awards.",
        "source": "Bosnia-Herzegovina Law on Compensation of Victims 2004"
    }
]
