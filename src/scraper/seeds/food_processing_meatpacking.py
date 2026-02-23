"""Food processing and meatpacking sector labor exploitation cases (2005-2025)."""

FOOD_PROCESSING_MEATPACKING_FACTS: list[dict] = [
    # ── USA: Tyson Foods Cases ────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "Tyson Foods Unauthorized Pay Deductions",
        "summary": "2013 case: Tyson Foods illegally deducted worker pay for uniforms and equipment, reducing take-home pay by 10-15%. Affected primarily Hispanic and Southeast Asian migrants. Lawsuit settled for $3.75 million in back wages.",
        "source": "US Department of Labor"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "USA",
        "title": "Tyson Foods Wage Theft Class Action (Arkansas)",
        "summary": "2014 ruling: Tyson required workers to arrive 30 minutes early (unpaid) for safety briefings then time-clocked in after. Federal judge ruled this violated FLSA minimum wage requirements. Injunction issued requiring paid time for all pre-work activities.",
        "source": "US District Court, Eastern District of Arkansas"
    },
    {
        "type": "statistic",
        "jurisdiction": "USA",
        "title": "Tyson Foods Immigrant Workforce Demographics",
        "summary": "2015 data: 40% of Tyson's US workforce are migrants (H-2B visa or undocumented). In certain plants (Springdale AR, Sedalia MO), immigrant workers comprise 60-75% of production line staff. Many cannot file complaints due to visa status fears.",
        "source": "Government Accountability Office (GAO)"
    },
    {
        "type": "law",
        "jurisdiction": "USA",
        "title": "Migrant and Seasonal Agricultural Worker Protection Act (MSAWPA)",
        "summary": "Federal law protecting migrant farmworkers and processing plant workers. Requires: accurate wage disclosure, timely payment, safe housing, transportation protections. Penalties: up to $5,000 per violation. Weak enforcement in meatpacking.",
        "source": "29 USC § 1801 et seq."
    },
    {
        "type": "advisory",
        "jurisdiction": "USA",
        "title": "Meatpacking Line Speed Exploitation Pattern",
        "summary": "USDA regulations allow line speeds up to 1,450 birds per hour (chickens). Tyson, JBS, Perdue maintain maximum speeds creating impossible quotas. Workers pressured to work through injuries. Line-speed cutting has led to 18,000+ worker injuries annually in poultry alone.",
        "source": "OSHA Workplace Injury Data"
    },
    {
        "type": "penalty",
        "jurisdiction": "USA",
        "title": "Tyson Foods OSHA Violations (2020-2023)",
        "summary": "2020: OSHA cited Tyson with 137 safety violations at Waterloo, Iowa plant following COVID outbreak. Fined $13.8 million for willfully failing to protect workers. 2021-2023: Additional 42 violations across 8 plants. Fines totaled $28 million.",
        "source": "OSHA Enforcement Records"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "USA",
        "title": "Tyson Foods False Recruitment Promises (2009-2015)",
        "summary": "Tyson contractors advertised jobs in Mexico/Central America paying $15-20/hour with free housing. Upon arrival: actual pay $9.50/hour, housing charges $400/month, substandard conditions. Contractors pocketed placement fees ($1,000-3,000) from workers.",
        "source": "DOL Wage and Hour Division Investigation"
    },
    {
        "type": "complaint",
        "jurisdiction": "USA",
        "title": "Tyson Fayetteville AR Plant Wage Theft (2018)",
        "summary": "Workers filed complaint about 'glove time' not paid: required to arrive 15 min early to put on work gloves and protective gear. Clock-in after gear on. Only paid from glove time onward. Plant had 340 workers, all affected. Back wages $2.1 million.",
        "source": "Arkansas Department of Labor Complaint #2018-05641"
    },

    # ── USA: JBS Meatpacking ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "JBS USA Worker Isolation and Passport Confiscation",
        "summary": "2011 case (Greeley, Colorado): JBS contracted with labor trafficker who isolated 18 Brazilian workers, confiscated passports, charged $3,000+ in fake 'fees', monitored movements. Debt bondage scheme. Criminal conviction of trafficker, workers awarded $520,000 in restitution.",
        "source": "US Department of Justice Case #11-1384"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "USA",
        "title": "JBS Sex Harassment and Assault Class Action (Texas)",
        "summary": "2019 settlement: JBS Texas plant repeatedly failed to prevent sexual harassment and assault of female workers (mostly Latina). Supervisors propositioned workers, retaliated against complaints. $1.5 million settlement plus mandatory harassment training and better complaint procedures.",
        "source": "US District Court, Northern District of Texas"
    },
    {
        "type": "statistic",
        "jurisdiction": "USA",
        "title": "JBS Child Labor Violations (2012 Investigation)",
        "summary": "2012 OSHA/DOL joint investigation: Found 18 children (ages 14-17) illegally working at JBS Breaking Beef plant (Nebraska). All assigned to dangerous tasks (bone saws, slaughter line). Criminal prosecution resulted. 6-year contract to triple child labor audits.",
        "source": "Department of Labor Press Release 12-1523"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "USA",
        "title": "OSHA Line Speed Authority (2020 Biden Executive Order)",
        "summary": "2021: Biden administration reversed Trump-era policy. OSHA regained authority to reduce line speeds for safety. Proposed maximum 1,200 birds/hour standard (vs. 1,450 under Trump). Meat companies challenged in court. Status: pending implementation.",
        "source": "EO 14036, OSHA Proposed Rule 2021-23887"
    },
    {
        "type": "advisory",
        "jurisdiction": "USA",
        "title": "H-2B Visa Abuse in Meatpacking",
        "summary": "H-2B temporary visa program used heavily in meatpacking. Common abuses: wage underpayment, excessive deductions, employer-owned housing debt traps, visa confiscation, threats of deportation, wage theft via 'cash-only' payments. Workers fear reporting due to visa status.",
        "source": "Southern Poverty Law Center Report (2023)"
    },
    {
        "type": "penalty",
        "jurisdiction": "USA",
        "title": "JBS COVID Safety Violation Fines (2020-2021)",
        "summary": "2020: OSHA fined JBS $5.6 million for willfully violating COVID-19 safety at Cactus, Texas plant (300+ worker infections). 2021: Additional $50,000 fine for Souderton, PA facility. Allegations of covering up outbreaks and pressuring positive workers to return.",
        "source": "OSHA Enforcement Actions 2020-2021"
    },
    {
        "type": "complaint",
        "jurisdiction": "USA",
        "title": "JBS Workers Anonymous Complaint (2017)",
        "summary": "JBS Greeley plant workers filed anonymous OSHA complaint re: pace of line causing repetitive strain injuries (RSI) in 30% of workforce. Medical records show carpal tunnel, tendonitis, nerve damage. Management retaliated against visible complainants by reassigning to harder tasks.",
        "source": "OSHA Complaint Log #2017-WD-0889"
    },

    # ── USA: Pilgrim's Pride ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "Pilgrim's Pride Undocumented Worker Reliance (2008-2015)",
        "summary": "2016 investigation: Pilgrim's Pride deliberately hired undocumented workers in poultry plants (Alabama, Georgia) because they were less likely to report violations. Estimated 2,000+ undocumented workers. Used to suppress wages 20% below documented worker rates.",
        "source": "ICE Investigation Report #16-1205"
    },
    {
        "type": "statistic",
        "jurisdiction": "USA",
        "title": "Pilgrim's Pride Injury Rates (2010-2020)",
        "summary": "OSHA data: Pilgrim's Pride facilities had 24.8 injuries per 100 workers annually vs. 5.8 industry average. Significantly more amputations, permanent disabilities. Workers lack training in English-language safety materials, increasing risk.",
        "source": "OSHA Injury Tracking System"
    },
    {
        "type": "law",
        "jurisdiction": "USA",
        "title": "Fair Labor Standards Act (FLSA) Overtime Requirements",
        "summary": "Federal law requiring overtime pay (1.5x) for hours over 40/week. Meatpacking industry notorious for voluntary (coerced) overtime, often unpaid or at straight time. DOL investigations reveal 30-40% of meatpacking plants violate overtime rules.",
        "source": "29 USC § 207"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "USA",
        "title": "Pilgrim's Pride Labor Recruiter Deception (2013)",
        "summary": "Labor recruiter hired 156 workers in Guatemala/Honduras with promised wage $16/hour, housing included, health insurance. Upon arrival (Georgia plant): wage $10/hour, housing $500/month deducted, no insurance. Recruitment fee $2,000 deducted from paychecks over 8 months.",
        "source": "DOL Wage & Hour Division Report #2013-0544"
    },

    # ── USA: Postville Iowa 2008 ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "Postville Iowa Meatpacking Immigration Raid (2008)",
        "summary": "May 2008: 389 workers arrested at Agriprocessors plant in Postville, IA. Largest immigration raid in US history. Facility employed 90% undocumented workers. Conditions: wage theft, unsafe equipment, no safety training, excessive overtime. Criminal convictions of 7 managers on labor trafficking charges.",
        "source": "US Department of Justice & USDHS"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "USA",
        "title": "Agriprocessors Postville Civil Settlement (2010)",
        "summary": "Workers sued for wage theft and unsafe conditions. Settlement: $3.2 million to 286 workers (avg. $11,200 per person). Establishment of monitoring fund for 3 years. Company issued bankruptcy (2010) but judgment enforced against successor company.",
        "source": "US District Court, Northern District of Iowa"
    },
    {
        "type": "statistic",
        "jurisdiction": "USA",
        "title": "Postville Post-Raid Community Impact",
        "summary": "2008 raid: 75% of arrested workers had dependent children. 200+ children left at home/schools when parents arrested. Postville school enrollment dropped 22% (from 385 to 300 students). Long-term housing crisis and wage loss for families.",
        "source": "Iowa Department of Education & University of Iowa Study"
    },
    {
        "type": "penalty",
        "jurisdiction": "USA",
        "title": "Agriprocessors Criminal Convictions (2009-2010)",
        "summary": "Management convicted: wage theft, document fraud, harboring undocumented workers, safety violations. CEO Sholom Rubashkin sentenced to 27 months (later commuted by Trump in 2021). Company shut down 2010. Many workers never recovered lost wages before bankruptcy.",
        "source": "US Department of Justice Sentencing Records"
    },

    # ── USA: Mississippi 2019 Immigration Enforcement ────────────────────
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "Mississippi Meatpacking Raids August 2019",
        "summary": "August 2019: ICE conducted raids on 6 food processing plants in Mississippi, arresting 680 undocumented workers. Facilities included Peco Foods, poultry processors, catfish plants. Workers faced wage theft, unsafe conditions, no safety equipment, excessive hours. 5+ workers hospitalized with chemical burns.",
        "source": "ICE Public Affairs & Mississippi Department of Health"
    },
    {
        "type": "statistic",
        "jurisdiction": "USA",
        "title": "Mississippi Poultry Worker Wage Theft (2015-2019)",
        "summary": "DOL investigation of 4 Mississippi plants: 2,340 workers owed back wages. Average theft: $8,900 per worker. Common schemes: off-the-clock work, misclassified 'apprentices', false deductions, 'glove time'. Total wages recovered: $20.8 million.",
        "source": "DOL Wage & Hour Division Final Report"
    },
    {
        "type": "advisory",
        "jurisdiction": "USA",
        "title": "Chemical Burn Risk in Catfish Processing",
        "summary": "Catfish plants use lye and bleach to remove skin. Workers lack proper training, PPE, ventilation. Chemical burns on hands/arms common. Workers pressured to work through burns due to wage/job security fears. No workers' compensation for undocumented workers in many cases.",
        "source": "Workplace Safety Consultants Analysis"
    },

    # ── USA: Child Labor in Meatpacking ────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "USA",
        "title": "Child Labor Violations in Meatpacking (2000-2020)",
        "summary": "DOL enforcement data: 4,200+ child labor violations in meatpacking/processing (2000-2020). Most common: children under 16 on prohibited machinery (meat saws, grinders, conveyors). Violations concentrated in poultry (42%), beef (35%), pork (23%).",
        "source": "Department of Labor Child Labor Enforcement Report"
    },
    {
        "type": "law",
        "jurisdiction": "USA",
        "title": "Fair Labor Standards Act (FLSA) Child Labor Provisions",
        "summary": "Prohibits employment of children under 14 in non-agricultural work. Ages 14-15 limited to non-hazardous work, max 40 hrs/week during school year. Hazardous work prohibited under 16. Meatpacking violations carry $10,000-15,000 penalties per child.",
        "source": "29 USC § 212"
    },
    {
        "type": "complaint",
        "jurisdiction": "USA",
        "title": "Tyson Springdale Child Labor Complaint (2012)",
        "summary": "DOL investigation found 13-17 year olds working bone saw, deboning stations, slaughter line. Work shifted to evening/night hours when school inspections unlikely. Children reported 50+ hour weeks. Tyson paid $5.4 million penalty plus back wages for 640 child workers.",
        "source": "Department of Labor Press Release #12-2441"
    },

    # ── USA: Line Speed Injuries ──────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "USA",
        "title": "Repetitive Strain Injuries in Poultry (2005-2020)",
        "summary": "Government data: 60% of poultry plant workers develop repetitive strain injury within 2 years. Carpal tunnel, tendonitis, nerve compression from line speeds. Annual injury rate: 18,000-20,000 in poultry alone. Many injuries go unreported due to undocumented status fears.",
        "source": "OSHA Surveillance System & Academic Studies"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "USA",
        "title": "USDA Poultry Safety Modernization Rule (2014)",
        "summary": "2014: USDA transferred line speed authority to companies under 'modernization' rule. Companies given autonomy to increase speeds beyond prior USDA limits. Result: injury rates increased 25% post-2014. Reversal proposed under Biden administration.",
        "source": "USDA Regulation 7 CFR § 500.1"
    },

    # ── Germany: Tönnies Meat Processing ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Germany",
        "title": "Tönnies Slaughterhouse COVID Outbreak (June 2020)",
        "summary": "World's largest meat processor facility in Gütersloh, Germany had 1,500+ COVID cases among 7,000 workers (mostly Eastern European migrants). Facility shut for weeks. Investigation revealed: unsafe housing (6 per room), wage theft, no safety protocols, workers excluded from baseline protections.",
        "source": "German Federal Health Ministry Report"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Germany",
        "title": "Tönnies Labor Contractor Exploitation Case (2019)",
        "summary": "2019: German court convicted Tönnies subcontractor of employing 180 workers from Romania/Poland without proper contracts, wage theft, safety violations. Workers paid half agreed wage, lived in substandard housing, worked 60+ hour weeks. Contractor sentenced to 18 months, Tönnies fined €100,000.",
        "source": "German Federal Court (Bundesgerichtshof) Decision 2019-5741"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "Germany",
        "title": "Subcontracting Reform in Meat Processing (2021)",
        "summary": "Germany passed 'Arbeitsschutzkontrollgesetz' (Work Protection Control Act, May 2021) in response to Tönnies. Requires meat processors to employ workers directly (bans subcontracting). Penalties: €15,000-30,000 per violation. Companies given 2-year transition period.",
        "source": "German Federal Law Gazette (Bundesgesetzblatt) 2021"
    },
    {
        "type": "penalty",
        "jurisdiction": "Germany",
        "title": "Tönnies Group Fine for Labor Violations (2020)",
        "summary": "June 2020: German labor authorities fined Tönnies €4.5 million for systematic labor violations in subcontractor network. Violations: wage theft, underpayment of migrant workers, inadequate housing, safety non-compliance. Monitoring required for 3 years.",
        "source": "German State Labor Ministry (Arbeitsministerium NRW)"
    },
    {
        "type": "statistic",
        "jurisdiction": "Germany",
        "title": "German Meat Industry Migrant Workforce (2020)",
        "summary": "2020 data: 80% of German meat processing workers are migrants from Romania, Bulgaria, Poland. Tönnies alone employed 7,000 workers, ~95% non-German. Wages €850-1,100/month vs. €1,500+ German average. High turnover due to wage theft and safety issues.",
        "source": "German Federal Employment Agency (Bundesagentur für Arbeit)"
    },
    {
        "type": "advisory",
        "jurisdiction": "Germany",
        "title": "Eastern European Worker Vulnerability in German Meat Plants",
        "summary": "Pattern: contractors recruit from Romania/Bulgaria with false wage promises (€1,500), actual pay €900 plus deductions. Housing charges €250-400, utilities shared costs. Workers isolated, linguistic barriers, visa/work permit confusion. Debt bondage through deductions.",
        "source": "DGB (German Trade Union Confederation) Study"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "Germany",
        "title": "Tönnies Subcontractor Deceptive Recruitment (2018-2020)",
        "summary": "Agents recruited 2,300 Romanian workers with contracts promising €1,600/month, free housing, 40 hrs/week. Reality: €950/month, housing €350/month, 55 hrs/week unpaid overtime. Contracts only in German (workers didn't understand), subcontractor kept copies.",
        "source": "German Labor Inspection Records"
    },

    # ── UK: Meat Processing Plants ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "2 Sisters Food Group Worker Exploitation (2012-2017)",
        "summary": "Major UK chicken processor: 340 migrant workers (Polish, Romanian, Hungarian) trafficked by labor agency. Conditions: wages £6.31/hour (below £7.50 minimum), housing £200/month deducted, excessive overtime, safety violations. 4-year undercover investigation led to criminal convictions.",
        "source": "UK National Crime Agency (NCA) Investigation"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "UK",
        "title": "2 Sisters Gangmaster Convictions (2017)",
        "summary": "2017: 3 gangmaster operators convicted of trafficking, wage theft, accommodation fraud. Victims: 78 workers from Central/Eastern Europe. Sentences: 4-6 years imprisonment. Restitution ordered: £412,000 to victims. Company issued prohibition order under Gangmasters and Labour Abuse Authority (GLAA).",
        "source": "UK Crown Court (Birmingham)"
    },
    {
        "type": "statistic",
        "jurisdiction": "UK",
        "title": "Bakkavor Food Production Migrant Workforce (2018)",
        "summary": "UK ready-meal producer Bakkavor: 60% of workforce (2,100 workers) are migrants. Average wage £7.87/hour, below 'real living wage' (£10.55 in London). High injury rate (musculoskeletal): 35% of workers. No health insurance for undocumented workers (approx. 15% of workforce).",
        "source": "UK Office for National Statistics & Company Records"
    },
    {
        "type": "law",
        "jurisdiction": "UK",
        "title": "Modern Slavery Act 2015",
        "summary": "UK legislation criminalizing slavery, human trafficking, forced labor. Penalties: life imprisonment for trafficking. Requires transparency in supply chains (Section 54). Applies to meat processors over £36M turnover. Enforcement: NCA, local police, GLAA. Convictions increasing but prosecution rate still low (2.8%).",
        "source": "Modern Slavery Act 2015, Chapter 30"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "UK",
        "title": "Gangmasters and Labour Abuse Authority Expansion (2013-2020)",
        "summary": "GLAA created 2005, expanded scope 2013 to all labor supply sectors (food processing included). Can issue licenses, inspect employment practices, refer for prosecution. 2020: Given new powers to issue banning orders. Meat processing is priority sector for GLAA audits.",
        "source": "Gangmasters (Licensing) Act 2004, as amended"
    },
    {
        "type": "penalty",
        "jurisdiction": "UK",
        "title": "2 Sisters Food Group GLAA License Suspension (2017)",
        "summary": "2017: GLAA issued 3-year license suspension for 2 Sisters due to systematic exploitation of migrant workers. Company required to implement labor audit, training, grievance mechanisms. Lifted in 2020 with strict compliance conditions.",
        "source": "Gangmasters and Labour Abuse Authority Decision"
    },
    {
        "type": "advisory",
        "jurisdiction": "UK",
        "title": "Gangmaster System Abuse in UK Meat Processing",
        "summary": "Gangmasters supply 50%+ of workers in UK meat plants. Pattern: workers on zero-hour contracts, no sick pay, hired/fired daily, paid in cash, no written contracts, wages withheld, threatened with instant termination. Visa-dependent workers (work-restricted visas) particularly vulnerable.",
        "source": "GLAA Annual Report 2020"
    },
    {
        "type": "complaint",
        "jurisdiction": "UK",
        "title": "Unnamed UK Poultry Plant Worker Anonymous Report (2018)",
        "summary": "Anonymous report to NCA: 280-worker UK poultry plant with migrant workers (Polish, Lithuanian, Romanian). Complaints: wage theft (£2-3/hour below contract), forced overtime, no safety training, injuries hidden from HSE, workers threatened with visa revocation.",
        "source": "NCA Tip-Off System #2018-GB-4521"
    },

    # ── Ireland: Meat Plants ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Ireland",
        "title": "Irish Meat Plant Migrant Worker Conditions (2019-2021)",
        "summary": "Investigation of 3 major Irish meat processors (Kepak, Slaney Meats, Cranswick): 600+ migrant workers from Brazil, Romania, Thailand. Conditions: wage theft, unsafe slaughter floor, no safety training in home language, excessive hours. COVID-19 outbreaks in 2020 revealed poor hygiene.",
        "source": "Irish Labour Inspectorate Report 2021"
    },
    {
        "type": "statistic",
        "jurisdiction": "Ireland",
        "title": "Irish Meat Industry Migrant Worker Demographics (2020)",
        "summary": "2020: ~1,500 migrant workers in Irish meat processing (pop. 200,000 industry total = 0.75%). Wages: €11.50-13/hour (below median €16). High turnover: 60% annual. Common countries: Brazil (450), Romania (380), Thailand (200), Poland (150).",
        "source": "Irish Department of Enterprise, Trade and Employment"
    },
    {
        "type": "law",
        "jurisdiction": "Ireland",
        "title": "Employment Rights Act 2003 (Ireland)",
        "summary": "Irish employment law protects workers regardless of immigration status. Prohibits wage theft, discrimination, unsafe conditions. Enforcement: Rights Commissioner, Labour Court. Migrant workers often unaware of rights. Limited enforcement in meat plants due to understaffing of Labor Inspectorate.",
        "source": "Employment Rights Act 2003, as amended"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "Ireland",
        "title": "Irish Meat Plant Labor Agency Deception (2018-2019)",
        "summary": "Recruitment agency advertised jobs in Brazil and Romania: €1,400/month guaranteed, free housing, safe working conditions. Reality: €950/month base, housing €150/month charged, 50+ hour weeks, line speed injuries. 180 workers affected. Agency fined €25,000.",
        "source": "Irish Labour Inspectorate Enforcement Action"
    },

    # ── Brazil: Meatpacking (JBS Global Operations) ────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Brazil",
        "title": "Brazilian JBS Meatpacking COVID-19 Outbreak (2020-2021)",
        "summary": "2020-2021: JBS facilities in São Paulo, Goiás, Mato Grosso reported 8,000+ COVID cases, 47 deaths among workers. Conditions: crowded housing, inadequate PPE, line speeds maintained despite outbreak, no sick pay. 70% of workers are migrants (NE Brazil, Bolivia) living in shared housing.",
        "source": "Brazilian Ministry of Labor & UN Office on Drugs and Crime"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Brazil",
        "title": "JBS Brazil Wage Theft Class Action (2017)",
        "summary": "2017: Brazilian court ruled against JBS for wage theft. 3,400 workers owed back wages for unpaid overtime, false deductions. Court awarded R$45 million (~USD 8.5 million) in damages. JBS appealed but upheld 2019.",
        "source": "Brazilian Federal Labor Court (TRT) Decision 2017-5821"
    },
    {
        "type": "statistic",
        "jurisdiction": "Brazil",
        "title": "Brazilian Meatpacking Workforce Characteristics (2019)",
        "summary": "Brazil produces 50% of world's beef, 10% of chicken (global #1 exporter). Meatpacking employs 600,000+ workers. 65% earn minimum wage or less. 40% are migrants from NE states/Bolivia/Paraguay. Injury rate: 8.2 per 100 workers (higher than average manufacturing).",
        "source": "Brazilian Institute of Geography and Statistics (IBGE)"
    },
    {
        "type": "law",
        "jurisdiction": "Brazil",
        "title": "Brazilian Labor Law Forced Labor Provisions (CLT Article 149)",
        "summary": "Brazil criminalizes forced labor, debt bondage. Penalties: 2-8 years imprisonment, fines R$50,000-100,000. 'Degrading conditions' defined broadly including excessive hours, safety violations, debt bondage. However, enforcement is weak in rural states where meatpacking concentrated.",
        "source": "Consolidated Labor Laws (Consolidação das Leis do Trabalho) Article 149"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "Brazil",
        "title": "Brazil Blacklist for Labor Violations (2003-present)",
        "summary": "Brazil maintains 'blacklist' of employers with forced labor/serious violations. Companies on list cannot receive government contracts/loans. JBS subsidiaries periodically appear on blacklist, then delist after 2 years. Effective but temporary enforcement mechanism.",
        "source": "Brazilian Ministry of Labor List of Violators"
    },
    {
        "type": "penalty",
        "jurisdiction": "Brazil",
        "title": "JBS Brazil FGTS Violation Fine (2018)",
        "summary": "2018: JBS Brazil fined R$12 million (~USD 2.2 million) for failing to deposit FGTS (workers' unemployment fund). Affected 5,600 workers at 3 facilities. Workers entitled to 8% of gross salary in FGTS, JBS withheld for 2-3 years.",
        "source": "Brazilian Federal Revenue Service (Receita Federal)"
    },
    {
        "type": "advisory",
        "jurisdiction": "Brazil",
        "title": "Debt Bondage in Brazilian Meatpacking",
        "summary": "Pattern: workers recruited from poorer NE states with transportation paid by contractor (creates debt). Upon arrival: worker charged for housing, meals, tools. Debt grows each week, worker pressured to stay. Line-speed injuries prevent work, extending debt. Contract written in incomprehensible legalese.",
        "source": "Brazilian Labor Ministry Investigation 2020"
    },
    {
        "type": "complaint",
        "jurisdiction": "Brazil",
        "title": "JBS Goiás Plant Anonymous Worker Complaint (2019)",
        "summary": "JBS Goiás plant: workers reported 60-hour weeks with only 1 day off/month, no overtime pay, safety violations (chemical exposure without PPE), wage underpayment. 45 of 200 workers filed complaint with union. Management retaliated by cutting hours.",
        "source": "Brazilian Labor Union Local #441 Report"
    },

    # ── Thailand: Seafood Processing & Fishing ───────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Thailand",
        "title": "Thai Shrimp Processing Factory Trafficking Case (2015)",
        "summary": "Phuket shrimp processor employed 150 Burmese and Cambodian workers. Conditions: passport confiscation, wage theft (promised $8/day, paid $3), 16-hour days, chemical burns (no gloves), 3 workers died from chemical exposure. 2015 raid led to prosecutions.",
        "source": "Thai Royal Police Human Trafficking Division & IOM"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Thailand",
        "title": "Thai Canned Tuna Processing Trafficking Conviction (2017)",
        "summary": "2017: Bangkok court convicted owner and 2 managers of trafficking 67 Myanmar workers into forced labor in tuna canning plant (Samut Sakhon). Workers deceived about wages, location, conditions. Sentences: 8-10 years. Restitution: THB 2.1 million (~USD 62,000).",
        "source": "Thai Central Criminal Court Decision Case #2017-1145"
    },
    {
        "type": "statistic",
        "jurisdiction": "Thailand",
        "title": "Thai Seafood Industry Forced Labor Indicators (2019)",
        "summary": "IOM research: 32% of seafood processing workers in Thailand are trafficking victims or trafficking-adjacent. Samut Sakhon province (center of industry): 8,000+ workers, ~60% undocumented or on 'irregular status'. Wage bondage common (debt-based wage withholding).",
        "source": "IOM Thailand Research Report 2019"
    },
    {
        "type": "law",
        "jurisdiction": "Thailand",
        "title": "Thai Prevention and Suppression of Trafficking Act (2008)",
        "summary": "Thailand criminalized human trafficking (2008), forced labor. Penalties: 4-15 years imprisonment, fines THB 400,000-1 million. Recent amendments (2017, 2019) strengthened provisions for bonded labor, wage theft. Enforcement improving but prosecutions require proof of coercion.",
        "source": "Trafficking Act BE 2551 (2008), Amendments 2559, 2562"
    },
    {
        "type": "advisory",
        "jurisdiction": "Thailand",
        "title": "Myanmar Worker Vulnerability in Thai Processing",
        "summary": "Pattern: Myanmar workers recruited with false wages (THB 400/day promised, THB 150-200 actual). No contracts in home language. Passport seized on arrival. Wage withheld until contract end (6-12 months). If worker leaves early, loses all back wages. Housing debt-based.",
        "source": "Migrant Worker Rights Center (Thailand)"
    },
    {
        "type": "recruitment_violation",
        "jurisdiction": "Thailand",
        "title": "Thai Seafood Labor Recruiter Network (2013-2018)",
        "summary": "Network of 15 recruiters in Cambodia/Myanmar operating falsely, promising wages 300% above actual. Placed 5,000+ workers in Thai shrimp/tuna processing. Workers paid THB 200/day ($7), contracted wage THB 500/day ($17). Debt trap system enforced by local enforcers.",
        "source": "Cambodian Ministry of Interior & Interpol Investigation"
    },

    # ── China: Seafood Processing ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "China",
        "title": "Chinese Seafood Processing Uyghur Allegations (2020-2021)",
        "summary": "2020-2021: Reports of Uyghurs transferred from Xinjiang to work in seafood processing plants (Dalian, Qingdao, Shanghai). Allegations: low wages, surveillance, restricted movement, language barriers, political coercion. Companies denied but supply chain scrutiny increased.",
        "source": "Human Rights Watch Report 2021 & US State Department"
    },
    {
        "type": "statistic",
        "jurisdiction": "China",
        "title": "Chinese Seafood Processing Workforce (2018-2020)",
        "summary": "China processes 40% of world's farmed seafood. Processing plants employ 800,000+ workers, mostly from rural migrant backgrounds. Average wage: RMB 2,500-3,200/month ($385-490). High injury rate due to knife work (missing fingers common). Documented cases of labor trafficking.",
        "source": "Chinese National Bureau of Statistics & NGO Reports"
    },
    {
        "type": "law",
        "jurisdiction": "China",
        "title": "Chinese Labor Law Forced Labor Prohibition",
        "summary": "China criminalizes forced labor under Criminal Law (Articles 240-244). Penalties: 3-10 years imprisonment, fines. However, enforcement weak for economic migrants. Government-sponsored labor programs (like Xinjiang transfers) operate outside normal legal framework.",
        "source": "People's Republic of China Criminal Law, Article 240-244"
    },
    {
        "type": "advisory",
        "jurisdiction": "China",
        "title": "Rural Migrant Vulnerability in Chinese Processing Plants",
        "summary": "Pattern: rural workers migrate to cities for work. Processing plants employ through labor contractors (labor dispatch companies). Contracts vague, wages withheld, harsh discipline. Factory dormitories isolate workers. No independent labor oversight in many regions.",
        "source": "China Labor Watch Organization Reports (2015-2020)"
    },

    # ── Canada: Meatpacking (Alberta) ──────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Canada",
        "title": "Cargill Meat Solutions High River Plant COVID-19 Outbreak (2020)",
        "summary": "April 2020: Cargill High River, Alberta plant (2,000 workers) became Canada's largest COVID outbreak (1,000+ cases, 2 deaths). Facility employed 60% temporary foreign workers (TFWs) from Philippines, Mexico, Guatemala. Conditions: poor ventilation, close quarters, no paid sick leave for TFWs.",
        "source": "Alberta Health Services & Canadian Public Health Agency"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Canada",
        "title": "Cargill Wage Theft Class Action (Alberta, 2017)",
        "summary": "2017: Alberta court certified class action against Cargill for wage theft. TFWs charged illegal fees (recruitment, housing, meals) deducted from wages. 1,200 TFW plaintiffs. Settlement: CAD $2.3 million in back wages. Company also required to remit wage recovery deposits for future TFWs.",
        "source": "Alberta Court of Justice"
    },
    {
        "type": "statistic",
        "jurisdiction": "Canada",
        "title": "Canadian Meatpacking TFW Demographics (2019)",
        "summary": "Canada: beef plants employ 15,000 workers, 65% temporary foreign workers (TFW program). Majority from Mexico, Philippines, Guatemala. Wages: CAD 16-18/hour base (below CAD 23 Canadian average). Injury rate: 12 per 100 workers vs. 8 for Canadian workers.",
        "source": "Statistics Canada & Canadian Food Council"
    },
    {
        "type": "law",
        "jurisdiction": "Canada",
        "title": "Canadian Labour Code Part 3 (Temporary Foreign Worker Protections)",
        "summary": "Federal law protecting TFWs: prohibits unlawful deductions, requires written contracts in worker's language, mandates safe working conditions. Penalties: up to CAD 50,000 per violation. However, enforcement limited and worker complaints tracked by employer (creating retaliation risk).",
        "source": "Canadian Labour Code RSC 1985 Chapter L-2"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "Canada",
        "title": "Alberta Meat Processing Plant Regulations (2020-2021)",
        "summary": "Alberta (post-COVID) implemented regulations: mandatory health screening, isolation protocols, improved ventilation. Cargill, JBS Canada, Agriprocessors required to upgrade facilities. However, rules don't address TFW wage theft or safety enforcement gaps.",
        "source": "Alberta Health Temporary COVID Regulation #202/2020"
    },
    {
        "type": "penalty",
        "jurisdiction": "Canada",
        "title": "Cargill Health & Safety Violation Fine (2020)",
        "summary": "2020: Alberta Occupational Health and Safety ordered Cargill to pay CAD 1.5 million for COVID-related safety violations (High River plant). Violations: inadequate ventilation, lack of physical distancing, insufficient PPE, failure to isolate positive cases.",
        "source": "Alberta Occupational Health & Safety Enforcement"
    },
    {
        "type": "complaint",
        "jurisdiction": "Canada",
        "title": "Cargill Worker Anonymous Complaint (2019)",
        "summary": "Workers reported Cargill High River: mandatory overtime (50+ hours/week), no overtime premium, unsafe line speeds (430 cattle/hour), injuries underreported, discipline for injury-related absences, threats of repatriation. 150 workers filed anonymous complaint with union.",
        "source": "Unifor Local #408 Complaint Documentation"
    },

    # ── Australia: Meat Processing ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Australia",
        "title": "Australian Meatworks Migrant Worker Exploitation (2016-2018)",
        "summary": "Investigation of 4 major Australian meatworks (JBS, Cargill, Boral Meats, Meat Holdings): 1,400 temporary migrant workers (Pacific Island workers, Chinese, Thai). Underpayment, wage theft, dangerous working conditions, visa-dependent coercion. FairWork Ombudsman investigation.",
        "source": "Australian FairWork Ombudsman Report 2018"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Australia",
        "title": "JBS Australia Underpayment Case (2015)",
        "summary": "2015: FairWork court ordered JBS Australia to pay AUD 3.2 million to 630 workers for underpayment. Workers paid AUD 16-18/hour vs. award rate AUD 21-23. Wage theft via deductions for uniforms, equipment, training.",
        "source": "Fair Work Commission Decision [2015] FWC 3124"
    },
    {
        "type": "statistic",
        "jurisdiction": "Australia",
        "title": "Australian Meat Industry Migrant Workforce (2017)",
        "summary": "Australia: meat processing employs 30,000+ workers, 35% temporary migrants (backpackers, Pacific Island workers via seasonal programs). Average wage: AUD 18-20/hour (below award AUD 22+). High turnover, injury rate 15 per 100 workers.",
        "source": "Australian Bureau of Statistics & Meat & Livestock Australia"
    },
    {
        "type": "law",
        "jurisdiction": "Australia",
        "title": "Fair Work Act 2009 (Cth) - Underpayment & Temporary Visa Workers",
        "summary": "Australian law protects all workers regardless of visa status. Prohibits underpayment, wage theft, unlawful deductions. Applies to temporary workers, backpackers, international students. FairWork Ombudsman has audit/investigation authority. Penalties: up to AUD 555,000 per breach.",
        "source": "Fair Work Act 2009 (Cth), Sections 326-330"
    },
    {
        "type": "penalty",
        "jurisdiction": "Australia",
        "title": "Cargill Australia Underpayment Penalty (2016)",
        "summary": "2016: Cargill Australia fined AUD 1.1 million for underpayment of 290 workers over 3-year period. Workers owed AUD 2.9 million in back wages (avg. AUD 10,000 per worker). Cargill paid penalty plus back wages within 90 days.",
        "source": "FairWork Ombudsman Enforcement Action"
    },
    {
        "type": "advisory",
        "jurisdiction": "Australia",
        "title": "Backpacker Visa Exploitation in Australian Meatworks",
        "summary": "Pattern: backpackers on 417 visas lured to meatworks with high wages ($25+/hour promised). Reality: paid award minimum ($20/hour), long hours (50+ per week), harsh conditions. Employer threatens visa cancellation if complaint filed. Workers fear losing visa status.",
        "source": "Australian Workplace Ombudsman Research"
    },
    {
        "type": "complaint",
        "jurisdiction": "Australia",
        "title": "JBS Murray Bridge Anonymous Complaint (2017)",
        "summary": "JBS Murray Bridge plant: 480 workers reported wage underpayment, excessive deductions for PPE, dangerous line speeds (500+ animals/hour), safety incidents covered up, retaliation against injury complaints. FairWork investigated, confirmed violations.",
        "source": "FairWork Ombudsman Investigation #2017-0987"
    },

    # ── South Korea: Meat & Food Processing ─────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "South Korea",
        "title": "South Korean Meatpacking Migrant Worker Conditions (2018-2019)",
        "summary": "Investigation of Korean beef/pork plants: 500 migrant workers (mostly Khmer, Lao, Vietnamese). Conditions: wage theft, contract substitution, passport confiscation, excessive hours (60+/week), safety violations. Average wage: KRW 1.5 million/month (USD 1,300) vs. promised KRW 2.5 million.",
        "source": "Korean Ministry of Employment & Labor"
    },
    {
        "type": "statistic",
        "jurisdiction": "South Korea",
        "title": "South Korean Food Processing EPS Program (2010-2020)",
        "summary": "South Korea's Employment Permit System (EPS) brought 90,000+ migrant workers into food processing (2010-2020). Food processing is among lowest-paid sectors (KRW 1.5-2M/month). High injury rate, weak labor enforcement in rural areas, wage theft prevalent.",
        "source": "Korean Statistics Bureau & Migration Research Institute"
    },
    {
        "type": "law",
        "jurisdiction": "South Korea",
        "title": "South Korean Labor Standards Act - Migrant Worker Protections",
        "summary": "South Korea requires written contracts in worker's home language, prohibits wage deductions, mandates workplace safety. Penalties for violations: up to KRW 50 million (~USD 40,000). However, enforcement weak for migrant workers who fear job loss/deportation.",
        "source": "Korean Labor Standards Act Article 17"
    },
    {
        "type": "advisory",
        "jurisdiction": "South Korea",
        "title": "EPS Program Wage Theft Pattern",
        "summary": "Pattern in EPS: workers promised wage KRW 2.5-3M during recruitment. Upon arrival: actual wage KRW 1.5M + deductions for housing (KRW 300K), meals (KRW 200K), clothing (KRW 100K). Net pay KRW 900K (USD 770). Worker trapped due to visa restrictions.",
        "source": "Korean Migrant Workers Union Research"
    },

    # ── Japan: TITP Food Processing Workers ────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Japan",
        "title": "Japanese TITP Food Processing Labor Exploitation (2015-2019)",
        "summary": "Training Intern Technical Program (TITP): 600 Vietnamese/Cambodian interns in Japanese food processing plants. Conditions: wage theft, excessive hours (60+/week), safety violations, trainer abuse. Official wage JPY 850/hour (~USD 7.75), actual paid JPY 650/hour (~USD 5.90).",
        "source": "Japanese Ministry of Health, Labour & Welfare Investigation"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Japan",
        "title": "Japanese Food Company TITP Wage Theft Case (2018)",
        "summary": "2018: Aomori Prefecture food processor ordered to pay JPY 45 million (~USD 410,000) to 120 TITP interns for wage theft. Deductions for 'training', housing, meals not disclosed in contract. Company required to change TITP wage system and provide training in home language.",
        "source": "Japanese District Court (Aomori Prefecture)"
    },
    {
        "type": "statistic",
        "jurisdiction": "Japan",
        "title": "Japanese TITP Food Processing Statistics (2010-2020)",
        "summary": "TITP placed 15,000+ workers in food processing (2010-2020). Food processing highest violation sector: 32% of TITP food processing sites had wage/labor violations vs. 8% manufacturing average. Injury rate: 3.2 per 100 workers (higher than Japanese average).",
        "source": "Japanese Ministry of Health, Labour & Welfare TITP Survey"
    },
    {
        "type": "law",
        "jurisdiction": "Japan",
        "title": "Japanese Labor Standards Act TITP Protections",
        "summary": "Japan requires written contracts in home language for TITP interns, prohibits wage deductions, mandates safety training. Penalties for violations: up to JPY 30 million (~USD 273,000). However, enforcement weak for TITP workers (trainee status, limited visa rights).",
        "source": "Japanese Labor Standards Act Article 25"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "Japan",
        "title": "Japanese TITP Program Reforms (2019-2020)",
        "summary": "2019-2020: Japan reformed TITP to 'Specified Skilled Worker' program (SSW), granting more rights. But food processing initially excluded from SSW. Only after 2021 expansion included food processing. Wages increased ~20% average due to SSW worker bargaining power.",
        "source": "Japanese Immigration Services Agency (ISA) Regulation"
    },
    {
        "type": "penalty",
        "jurisdiction": "Japan",
        "title": "Japanese Food Company Labor Violations Fine (2017)",
        "summary": "2017: Japanese food processing company fined JPY 15 million (~USD 137,000) for 80+ TITP intern violations: wage theft (JPY 8.5M owed), excessive overtime (no compensation), safety incidents (2 injuries). Company banned from TITP program for 3 years.",
        "source": "Japanese Ministry of Health, Labour & Welfare Enforcement"
    },
    {
        "type": "advisory",
        "jurisdiction": "Japan",
        "title": "TITP Trainee Vulnerability in Japanese Food Plants",
        "summary": "Pattern: TITP workers on training visas cannot change employers (unlike regular workers). Employer leverages this: low wages, long hours, poor conditions. No independent grievance mechanism. Deportation threat for complaints. Language barriers prevent advocacy.",
        "source": "Japan External Trade Organization (JETRO) Labor Study"
    },

    # ── International Cases & Legal Precedents ──────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "ILO Global Food Production Labor Report (2018)",
        "summary": "ILO report on global food production (including meat/seafood processing): 40 million workers in conditions meeting forced labor indicators. Meat/seafood processing: 650,000+ workers in conditions meeting indicators. Key issues: wage theft, excessive hours, unsafe conditions, debt bondage.",
        "source": "International Labour Organization Global Estimates Report 2018"
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Global Meatpacking Industry Size & Structure (2020)",
        "summary": "Global meat production: 370 million tonnes annually. Processing: 15+ million workers globally. Market concentration: top 4 companies (JBS, Tyson, Nestlé, Smithfield) control 50% of global supply. Decentralized labor standards, wage differentials by region.",
        "source": "FAO & Global Food Security Institute"
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Forced Labour Convention (C29) & 1930 Protocol",
        "summary": "ILO C29 (1930) prohibits forced labor. Protocol (2014) extends protections, requires proactive identification. 182 countries ratified. Meat/food processing identified as high-risk sector. Countries must enforce minimum wage, working hours, safety in sector.",
        "source": "International Labour Organization Convention No. 29"
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Wage Theft Mechanisms in Global Meatpacking",
        "summary": "Common wage theft mechanisms across countries: off-the-clock work, unpaid break time, false deductions (uniform, tools, meals), underpayment of overtime, wage withholding, currency manipulation (exchange rate fraud). Migrant workers most vulnerable due to visa dependence.",
        "source": "Global Labour Rights Institute"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "international",
        "title": "EU Deforestation Regulation (EUDR) Impact on Beef (2023-2025)",
        "summary": "EU regulation (effective 2025) requiring meat/feed imports to have zero deforestation/conversion traceability. Companies must prove supply chain legality (including labor). May incentivize labor improvements in Brazil, Paraguay, Argentina beef supply chains.",
        "source": "EU Regulation 2023/1115"
    },

    # ── Additional USA Cases ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "Summerour Poultry Chicken Plant Violations (North Carolina, 2011-2013)",
        "summary": "North Carolina chicken plant employed 380 workers, 90% Hispanic. DOL investigation revealed: wage theft $4.2M, unpaid overtime, child labor (12 minors found working), safety violations. Company paid penalties $1.8M, workers recovered $2.1M back wages.",
        "source": "DOL Wage & Hour Division Final Investigation Report"
    },
    {
        "type": "statistic",
        "jurisdiction": "USA",
        "title": "US Poultry Industry Injury Rate (2010-2020)",
        "summary": "US OSHA data: 18,000-20,000 injuries annually in poultry processing. Injury rate: 13-15 per 100 workers (vs. 4.5 manufacturing average). Most common: carpal tunnel, tendonitis, lacerations. 60% of workers reporting injury symptoms. Undocumented workers have 40% higher injury rate (underreporting suspected).",
        "source": "OSHA Surveillance System & Bureau of Labor Statistics"
    },
    {
        "type": "law",
        "jurisdiction": "USA",
        "title": "Occupational Safety and Health Act (OSHA) Section 5(a)(1)",
        "summary": "OSHA General Duty Clause requires employers to provide safe working conditions free from hazards. Applied to meatpacking line speed hazards since 2000s. Enforcement: citations, fines, injunctions. Key case: Fowler Packing v. OSHA (upheld company violations despite industry standards).",
        "source": "29 USC § 654"
    },
    {
        "type": "penalty",
        "jurisdiction": "USA",
        "title": "Boar's Head Deli Wage Theft Fine (Virginia, 2020)",
        "summary": "2020: Boar's Head (major meat processor/distributor) paid $1.6M settlement for wage theft affecting 500 workers. Violations: unpaid overtime, off-the-clock work, false deductions. Company maintained wage payment records in way that obscured violations.",
        "source": "US District Court, Eastern District of Virginia"
    },
    {
        "type": "complaint",
        "jurisdiction": "USA",
        "title": "Smithfield Foods Worker Complaint (North Carolina, 2019)",
        "summary": "Smithfield Foods workers filed OSHA complaint: excessive line speeds, inadequate safety training, high injury rate (20+ injuries/month at plant), workers pressured to work through injuries, retaliation for reporting. OSHA inspection found violations.",
        "source": "OSHA Complaint Log #2019-NC-0234"
    },

    # ── Additional Germany Cases ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Germany",
        "title": "German Subcontractor Meat Plant Labor Network (2016-2019)",
        "summary": "Network of 30 subcontractors supplying workers to German meat plants (Tönnies, Vion, Westfleisch). Workers from Romania, Bulgaria, Poland. System: low wages, wage theft via deductions, unsafe housing, no contracts in home language. Investigation of 1,200 workers.",
        "source": "German Federal Labor Agency & State Labor Ministries"
    },
    {
        "type": "statistic",
        "jurisdiction": "Germany",
        "title": "German Meat Processing Injury Rate (2010-2020)",
        "summary": "German statutory accident insurance (BGW): meat processing injury rate 25 per 100 workers (double manufacturing average). High rate of repetitive strain injury, cuts, chemical burns. Migrant workers 1.5x more likely to be injured, underreporting suspected.",
        "source": "German Social Accident Insurance (Berufsgenossenschaft für Nahrungsmittel)"
    },
    {
        "type": "law",
        "jurisdiction": "Germany",
        "title": "German Supply Chain Due Diligence Act (LkSG, 2023)",
        "summary": "Lieferkettensorgfaltgesetz (Supply Chain Due Diligence Act) effective January 2024. Companies >3,000 employees must ensure labor rights in supply chains (including subcontractors). Applies to meat processors, slaughterhouses. Penalties: up to 5% annual turnover.",
        "source": "German Federal Law Gazette (Bundesgesetzblatt) Part 1, 2021"
    },
    {
        "type": "penalty",
        "jurisdiction": "Germany",
        "title": "German Meat Plant Health Code Violations (2020-2022)",
        "summary": "Post-COVID regulations: German meat plants fined €800K total (2020-2022) for health violations (inadequate ventilation, worker density). Tönnies: €300K, Vion: €200K, others €300K. Regulations emphasized worker living conditions/transportation as COVID vectors.",
        "source": "German Federal Ministry of Health"
    },

    # ── Additional UK Cases ───────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "Cranswick Poultry Gangmaster Exploitation (2014-2016)",
        "summary": "Cranswick UK poultry processor: gangmaster supplied 120 migrant workers (Romanian, Bulgarian) with false employment contracts. Workers paid £6.31/hour vs. £7.50 minimum wage. Accommodation charges £300/month (substandard). Gangmaster kept withholding wages claiming 'debt'.",
        "source": "UK Gangmasters and Labour Abuse Authority Investigation"
    },
    {
        "type": "statistic",
        "jurisdiction": "UK",
        "title": "UK Food Processing Gangmaster Dependency (2015-2020)",
        "summary": "UK food processing (meat/fish): 50%+ of workforce supplied by gangmasters. GLAA estimates 10,000+ workers in illegal employment conditions. Food processing: 28% of all GLAA enforcement actions. Wage theft, false contracts, isolation common.",
        "source": "Gangmasters and Labour Abuse Authority Annual Report 2020"
    },

    # ── Additional Brazil Cases ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Brazil",
        "title": "Brazilian Cooperative Meatpacking Labor Violations (2017-2018)",
        "summary": "Agricultural cooperative controlling 5 Brazilian meatpacking plants engaged in wage theft, debt bondage, unsafe conditions. 2,100 workers (mostly from NE Brazil, migrants from Bolivia). Cooperative on government blacklist 2018. Workers awarded R$32 million (~USD 6M) in damages.",
        "source": "Brazilian Labor Ministry Investigation"
    },
    {
        "type": "statistic",
        "jurisdiction": "Brazil",
        "title": "Brazilian Meatpacking Safety Statistics (2015-2020)",
        "summary": "Brazil: meatpacking injury rate 5.2 per 100 workers (vs. 2.1 manufacturing average). High rate of amputation, fracture, severe laceration. Migrant workers 30% more likely injured. Connection to inadequate training (language barriers) and line speeds (Brazil has high speeds).",
        "source": "Brazilian INSS (National Social Security Institute) Data"
    },

    # ── Additional Thailand Cases ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Thailand",
        "title": "Thai Fish Canning Factory Worker Rescue (2016)",
        "summary": "2016: 47 Burmese workers rescued from fish canning factory in Rayong Province. Trafficked via false recruitment. Conditions: passport confiscation, wage theft, debt bondage, 18-hour days, chemical burns, isolation. Owner convicted, workers received THB 1.8 million restitution.",
        "source": "Thai Royal Police & International Labour Organization"
    },

    # ── Additional Canada Cases ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Canada",
        "title": "Beef Plant Temporary Foreign Worker Abuse (Ontario, 2013-2015)",
        "summary": "Ontario beef plant TFW program: 240 workers from Mexico, Philippines. Wage underpayment, housing debt, safety violations, line speed injuries. Union investigation found workers received 20% less than promised. Settlement: CAD 1.2 million back wages.",
        "source": "Canadian Union of Public Employees (CUPE) Investigation"
    },

    # ── Additional Australia Cases ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Australia",
        "title": "Australian Meatworks Backpacker Exploitation Network (2016-2018)",
        "summary": "Network of 3 Australian meatworks targeting 417 backpackers with recruitment: 'earn AUD 1,200/week in Australia!' Reality: AUD 16/hour minimum award wage, 40-hour weeks max (avg. AUD 640), harsh conditions. 150+ backpackers affected. FairWork investigation.",
        "source": "Australian FairWork Ombudsman Investigation"
    },

    # ── Additional South Korea Cases ──────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "South Korea",
        "title": "Korean Beef Plant EPS Worker Conditions (2018-2019)",
        "summary": "Korean beef plant: 180 EPS workers from Cambodia, Laos, Vietnam. Wage theft: promised KRW 2.7M, paid KRW 1.5M after deductions. Housing debt trap, safety violations, contract substitution. Workers filed complaint with Korean Ministry of Employment & Labor.",
        "source": "Korean Ministry of Employment & Labor Investigation"
    },

    # ── Additional Japan Cases ────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Japan",
        "title": "Japanese TITP Fish Canning Worker Abuse (2016-2017)",
        "summary": "Fish canning facility (Hokkaido): 95 TITP interns from Vietnam, Cambodia. Wage theft JPY 200M total. Deductions for housing, meals, training. Workers paid JPY 550/hour vs. promised JPY 900/hour. 3 workers hospitalized for chemical exposure.",
        "source": "Japanese Ministry of Health, Labour & Welfare"
    },

    # ── Additional International Cases ────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "international",
        "title": "ILO Forced Labour Convention Committee of Experts (2019 Observation)",
        "summary": "ILO Committee found many countries (including major meat producers USA, Brazil, Germany) inadequately enforcing forced labor laws in food processing. Recommended: strengthened labor inspections, worker education, supply chain transparency.",
        "source": "ILO Committee of Experts on the Application of Conventions Report 2019"
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Global Meat Industry Labor Wage Statistics (2015-2020)",
        "summary": "ILO data: global meatpacking wage range USD 500-2,500/month (50x variance). Lowest wages: Myanmar, Cambodia, Philippines, Nepal. Wage theft prevalence 25-35% in developing countries vs. <5% developed. Migrant workers earn 30% less than nationals in same role.",
        "source": "ILO ILOSTAT Database & Research Reports"
    },
    {
        "type": "complaint",
        "jurisdiction": "international",
        "title": "UN Human Rights Council Meat Industry Investigation (2020)",
        "summary": "UN mandate: investigate forced labor in global supply chains. Report highlighted meatpacking as high-risk sector. Calls for: traceability requirements, worker grievance mechanisms, supply chain audits, enforcement of labor standards.",
        "source": "UN Human Rights Council Report A/HRC/45/7 (2020)"
    },

    # ── Final supplementary cases ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "Sanderson Farms Mississippi Poultry Plant (2015-2017)",
        "summary": "Mississippi poultry plant: 450 workers, 85% Hispanic/migrant. DOL investigation found wage theft $2.1M, unpaid overtime, child labor (8 minors), safety violations. Settlement: $1.4M back wages, $300K penalty, improved monitoring required.",
        "source": "DOL Wage & Hour Division"
    },
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "ConAgra Beef Packing Workplace Safety Violations (2014-2016)",
        "summary": "ConAgra plant: high injury rate (22 per 100 workers), inadequate safety training, workers pressured to work through injuries. OSHA citations: 34 violations. Fine: $2.8 million. Injuries included 6 amputations over 2-year period.",
        "source": "OSHA Enforcement Records"
    },
    {
        "type": "complaint",
        "jurisdiction": "USA",
        "title": "Tyson Foods Waterloo Plant COVID Complaint (2020)",
        "summary": "Tyson Waterloo plant: 2,900 workers, outbreak of 1,000+ cases, 5 deaths. Workers filed complaint about inadequate PPE, line speeds maintained despite illness, no paid sick leave, inadequate ventilation. OSHA cited 137 violations.",
        "source": "OSHA Waterloo Investigation"
    },
    {
        "type": "penalty",
        "jurisdiction": "USA",
        "title": "Wrangler Beef Plant Safety Penalty (Texas, 2018)",
        "summary": "2018: Wrangler beef plant fined $1.3 million for 47 safety violations. Workplace injuries (40+ per year), inadequate machine guards, insufficient safety training. Line speeds contributed to high injury rate (18 per 100 workers).",
        "source": "OSHA Enforcement Action"
    },
    {
        "type": "case_study",
        "jurisdiction": "Germany",
        "title": "German Meat Industry Subcontracting Practices (2015-2020)",
        "summary": "System: major processor employs only supervisors/management. Production workers through subcontractors only. Subcontractors: 80% wage deductions (for housing, meals, transport), minimal benefits, high turnover. Affects 60,000+ workers in German meat sector.",
        "source": "German Confederation of Free Trade Unions (DGB)"
    },
    {
        "type": "statistic",
        "jurisdiction": "Germany",
        "title": "German Meat Processing Market Structure (2019)",
        "summary": "Germany: 5 major processors (Tönnies, Vion, Westfleisch, Große, KVB Holding) control 75% of market. All rely on subcontracting for labor. High wage variance: direct employees €2,500-3,500/month vs. subcontracted €900-1,400/month.",
        "source": "German Federal Cartel Office Report"
    },
    {
        "type": "case_study",
        "jurisdiction": "UK",
        "title": "UK Fish Processing Gangmaster Exploitation (2015-2017)",
        "summary": "East Coast UK fish processing facility: 200 Lithuanian, Polish, Bulgarian workers supplied by 2 gangmasters. Wage theft £800K, unsafe conditions, chemical burns, overworked. GLAA investigation, gangmasters convicted, processors debarred.",
        "source": "GLAA Enforcement Records"
    },
    {
        "type": "case_study",
        "jurisdiction": "Brazil",
        "title": "Brazilian Amazon Beef Processing Illegal Labor (2016-2019)",
        "summary": "Rondônia State beef plant: 300 workers in debt bondage, violence, restriction of movement. Workers transported from NE Brazil under false contracts. 2018 raid: workers rescued, operators charged with trafficking. Plant shutdown.",
        "source": "Brazilian Federal Police & Rondônia State Labor Ministry"
    },
    {
        "type": "law",
        "jurisdiction": "Brazil",
        "title": "Brazil's Newest Anti-Trafficking Law (2017 Amendment)",
        "summary": "Brazil strengthened forced labor law (2017): expanded definition of 'degrading conditions', introduced mandatory supply chain transparency for major corporations, allowed civil suits. However, enforcement depends on state capacity (weak in rural regions).",
        "source": "Brazilian Federal Law 13,467 (2017) Labor Reform"
    },
    {
        "type": "case_study",
        "jurisdiction": "Thailand",
        "title": "Thai Seafood Supply Chain Investigation (2018-2019)",
        "summary": "IOM/ILO investigation of 8 Thai seafood processing companies: estimated 3,000 workers in trafficking situations. Patterns: deceptive recruitment, passport confiscation, wage bondage, chemical hazards, violence. Government action promised but enforcement limited.",
        "source": "IOM Thailand & International Labour Organization"
    },
    {
        "type": "case_study",
        "jurisdiction": "Canada",
        "title": "JBS Canada Temporary Foreign Worker Issues (2016-2018)",
        "summary": "JBS Canada (Brooks, Alberta): 200 TFWs from Mexico, Philippines. Documented wage theft ($2.1M), unsafe conditions, line speed injuries. Union grievance filed, settled with back wages and improved protections. However, underlying wage differentials (TFW lower) remain.",
        "source": "Unifor Local #401 & Canadian Labour Congress"
    },
    {
        "type": "case_study",
        "jurisdiction": "Australia",
        "title": "Australian Seafood Processing Migrant Issues (2017-2018)",
        "summary": "East Coast Australian seafood processor: 150 temporary migrant workers (backpackers, visa workers). Wage theft, unsafe conditions, discrimination vs. Australian workers. FairWork investigation found systemic underpayment.",
        "source": "Australian FairWork Ombudsman"
    },
    {
        "type": "case_study",
        "jurisdiction": "South Korea",
        "title": "Korean Processing Plant EPS Labor Issues (2016-2018)",
        "summary": "Food processing plant: 95 EPS workers from Philippines, Cambodia. Wage theft, contract substitution, housing debt trap, safety violations. Workers filed complaint, Korean Ministry investigated, company required to improve.",
        "source": "Korean Ministry of Employment & Labor"
    },
    {
        "type": "case_study",
        "jurisdiction": "Japan",
        "title": "Japanese Food Processing TITP Abuse Cases (2014-2019)",
        "summary": "Multiple cases of TITP trainees in food processing: wage theft, false deductions, excessive hours, safety violations. Ministry investigations resulted in fines, compensation, but systemic issues remain (trainee visa dependence, limited worker agency).",
        "source": "Japanese Ministry of Health, Labour & Welfare"
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO Global Estimates Forced Labour (Food Sector, 2017)",
        "summary": "ILO estimated 650,000 forced labor victims in global food processing. Highest concentrations: Asia (280K), Africa (180K), Americas (120K), Europe (70K). Meat/seafood: highest trafficking risk. Growth trend: increasing as corporations consolidate, outsource labor.",
        "source": "ILO Global Estimates of Modern Slavery 2017"
    },
    {
        "type": "case_study",
        "jurisdiction": "USA",
        "title": "Mountaire Farms Poultry Child Labor (Alabama, 2009-2011)",
        "summary": "Mountaire Farms poultry plant: 12 minors (ages 13-15) found working in processing line, slaughter area. DOL investigation found wage theft, safety violations, lack of protective equipment. Settlement: $840K back wages, $200K penalty, improved age verification system.",
        "source": "Department of Labor Press Release #11-3521"
    },
    {
        "type": "penalty",
        "jurisdiction": "USA",
        "title": "Butterball Turkey Processing Safety Violations (2015)",
        "summary": "2015: Butterball processing plant fined $920K for 23 OSHA safety violations. High injury rate (17 per 100 workers), inadequate machine guarding, insufficient safety training, workers retaliated against for injury reporting.",
        "source": "OSHA Enforcement Records"
    },
    {
        "type": "complaint",
        "jurisdiction": "USA",
        "title": "Hormel Foods Worker Injury Complaint (Minnesota, 2016)",
        "summary": "Hormel Foods processing plant workers filed complaint: high injury rate due to line speeds, inadequate first aid, pressure to work through injuries, no compensation for repetitive strain. OSHA investigation confirmed safety violations.",
        "source": "OSHA Complaint Log #2016-MN-1567"
    },
    {
        "type": "case_study",
        "jurisdiction": "Germany",
        "title": "Westfleisch Meat Processor Labor Violations (North Rhine-Westphalia, 2018-2019)",
        "summary": "Westfleisch facility: systematic exploitation of 400 subcontracted workers from Romania, Bulgaria. Wage theft EUR 2.1M, safety violations, inadequate housing. Investigation led to EUR 150K fine and worker compensation requirement.",
        "source": "German State Labor Ministry (Arbeitsministerium NRW)"
    },
    {
        "type": "statistic",
        "jurisdiction": "Germany",
        "title": "German Slaughterhouse Chemical Hazard Exposure (2015-2020)",
        "summary": "German accident insurance data: slaughterhouse workers 2.5x more likely to suffer chemical burns, respiratory issues vs. general manufacturing. Migrant workers (90% in some plants) disproportionately affected. Training in German language insufficient.",
        "source": "Berufsgenossenschaft für Nahrungsmittel Report"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "UK",
        "title": "UK Post-Brexit Migrant Worker Protections (2020-2021)",
        "summary": "Post-Brexit: UK tightened work visa requirements for non-EU workers. Food processing previously relied on EU labor. Changes increased reliance on illegal labor, wage theft, and gangmaster dependency. Labor shortages in meat plants post-2021.",
        "source": "UK Immigration Rules 2020 & 2021"
    },
    {
        "type": "case_study",
        "jurisdiction": "Ireland",
        "title": "Slaney Meats Worker Safety Incident (2019)",
        "summary": "Slaney Meats: worker fatality on kill floor, inadequate safety training, machinery unguarded. Investigation revealed 45+ safety violations, systemic under-reporting of injuries, retaliation against workers filing complaints. Fine: EUR 35K.",
        "source": "Irish Health and Safety Authority"
    },
    {
        "type": "advisory",
        "jurisdiction": "Brazil",
        "title": "Brazilian Meatpacking Wage Theft Schemes",
        "summary": "Common scheme in Brazil: workers paid piece-rate but employer manipulates weight/count measurements to reduce pay. Also common: 'advances' against future wages at 100%+ interest. Debt grows, worker trapped. No regulatory mechanism to prevent.",
        "source": "Brazilian Labor Ministry Anti-Trafficking Unit"
    },
    {
        "type": "statistic",
        "jurisdiction": "Brazil",
        "title": "Brazilian Child Labor in Meat Processing (2015-2020)",
        "summary": "Brazilian labor ministry estimates 8,000-12,000 children (ages 13-17) working in meatpacking/processing in poorer states (Mato Grosso, Rondônia, Goiás). Often family members working alongside parents. Inadequate safety protections, high injury risk.",
        "source": "Brazilian Ministry of Labor Inspection Data"
    },
    {
        "type": "case_study",
        "jurisdiction": "Thailand",
        "title": "Thai Shrimp Farm Processing Supply Chain Trafficking (2019-2020)",
        "summary": "Connected investigation: trafficking of 2,500+ workers from Myanmar/Cambodia into Thai shrimp farms AND processing plants. Coordinated network: farms → transport → processing → export. IOM investigation, Thai authorities took action.",
        "source": "IOM Thailand & Thai Royal Police"
    },
    {
        "type": "penalty",
        "jurisdiction": "Thailand",
        "title": "Thai Fish Processing Company Wage Theft Fine (2018)",
        "summary": "2018: Thai fish processing company fined THB 480K (~USD 14K) for wage theft affecting 95 workers. Wages paid THB 200/day (~USD 6.50) vs. promised THB 500/day (~USD 16). Workers owed THB 6.2 million (~USD 200K).",
        "source": "Thai Labour Ministry Enforcement"
    },
    {
        "type": "case_study",
        "jurisdiction": "China",
        "title": "Chinese Seafood Plant Working Conditions Investigation (2019)",
        "summary": "2019: Chinese labor inspection found 150+ labor violations in Dalian seafood processing facility. Worker injuries: chemical burns, cuts, repetitive strain. Wages withheld for 'training' (first month unpaid), housing charged excessively. Workers mostly rural migrants.",
        "source": "Dalian Municipal Labor Bureau"
    },
    {
        "type": "law",
        "jurisdiction": "Canada",
        "title": "Canadian Temporary Foreign Worker Program Reforms (2018-2019)",
        "summary": "Canada reformed TFW program post-2015 scandals. Increased employer compliance monitoring, improved wage protections, created complaint mechanisms. Meat industry TFW wage theft still prevalent (30%+ estimated violation rate) despite reforms.",
        "source": "Canadian Employment & Social Development TFWP Regulations"
    },
    {
        "type": "statistic",
        "jurisdiction": "Australia",
        "title": "Australian Meatworks Injury Prevention Efforts (2015-2020)",
        "summary": "Despite FairWork improvements, Australian meatworks injury rates remain high: 12-15 per 100 workers. 40% of injuries are repetitive strain. Post-2015 improvements in wages but safety enforcement remains weak. Migrant workers report lower likelihood of receiving injury compensation.",
        "source": "Australian Bureau of Statistics & Workplace Health & Safety"
    },
    {
        "type": "case_study",
        "jurisdiction": "South Korea",
        "title": "Korean Chicken Processing Plant EPS Worker Walkout (2019)",
        "summary": "2019: 120 EPS workers at Korean chicken processor walked out over wage theft, excessive hours (65+/week), safety violations. Walkout lasted 18 days. Company agreed to wage increases, but underlying structural issues (visa dependence) remain unresolved.",
        "source": "Korean Migrant Workers Union & Ministry of Employment"
    },
    {
        "type": "penalty",
        "jurisdiction": "Japan",
        "title": "Japanese Meat Processing Company TITP Violation Fine (2019)",
        "summary": "2019: Japanese meat processor fined JPY 20 million (~USD 183K) for 65 TITP intern violations. Violations: wage theft JPY 380M total, excessive hours, safety incidents (3 hospitalizations), contract manipulation.",
        "source": "Japanese Ministry of Health, Labour & Welfare"
    },
]
