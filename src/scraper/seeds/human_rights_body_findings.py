"""Seed facts: International human rights body findings on labor exploitation and trafficking.

Covers UN Human Rights Council, ILO Committee of Experts, CERD, CEDAW, CMW, UNHCR,
Inter-American Court, African Court, ASEAN ACTIP/ACMW, GRETA, OSCE, and related bodies.
Period: 2005–2025.
"""

HUMAN_RIGHTS_BODY_FINDINGS_FACTS: list[dict] = [
    # ── UN Human Rights Council / Special Rapporteurs ──────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Debt Bondage as Primary Trafficking Mechanism",
        "summary": "UN Special Rapporteur on Trafficking in Persons (2006) identified debt bondage as the single most prevalent mechanism sustaining trafficking situations globally, noting that inflated recruitment debts—often 12–24 months of wages—function as an invisible chain preventing workers from leaving exploitative employment.",
        "source": "UN SR on Trafficking, A/HRC/4/23, 2006",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Demand Reduction Obligations of States",
        "summary": "UN Special Rapporteur (2010) report emphasized that states have positive obligations to reduce demand for trafficked labor, including criminalizing employers knowingly using trafficked workers and auditing supply chains in high-risk sectors such as domestic work, fishing, agriculture, and construction.",
        "source": "UN SR on Trafficking, A/HRC/14/32, 2010",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Contemporary Forms of Slavery: Kafala as Structural Slavery Risk",
        "summary": "UN Special Rapporteur on Contemporary Forms of Slavery (2011) concluded that the kafala sponsorship system in Gulf Cooperation Council states creates conditions structurally analogous to slavery by binding workers' legal status to a single employer, enabling wage theft, passport confiscation, and forced overtime without legal recourse.",
        "source": "UN SR on Contemporary Forms of Slavery, A/HRC/18/30, 2011",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Migrant Rights: Detention of Migrant Workers",
        "summary": "UN Special Rapporteur on the Human Rights of Migrants (2012) found that administrative detention of undocumented migrants—applied disproportionately in Malaysia, Thailand, and GCC states—creates acute vulnerability to exploitation by recruiters and employers who offer to pay fines or secure release in exchange for labor servitude.",
        "source": "UN SR on Migrants, A/HRC/20/24, 2012",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Child Domestic Workers at Heightened Risk",
        "summary": "UN Special Rapporteur on Trafficking (2013) documented that child domestic workers—estimated at 10.5 million globally—face compounded risks: isolation in private homes, absence of labor inspection, no minimum wage protections in most jurisdictions, and employer control over access to schooling and communication.",
        "source": "UN SR on Trafficking, A/68/256, 2013",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Contemporary Forms of Slavery: Fishing Industry Forced Labor",
        "summary": "UN Special Rapporteur on Contemporary Forms of Slavery (2013) found systemic forced labor aboard fishing vessels in Southeast Asia, particularly on Thai-flagged boats operating in international waters. Workers experienced withheld wages, violent supervision, inability to disembark, and multi-year contracts with no exit mechanism.",
        "source": "UN SR on Contemporary Forms of Slavery, A/HRC/24/43, 2013",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR Third Cycle: Qatar Recommendations on Kafala Reform",
        "summary": "During Qatar's Universal Periodic Review (2019), 47 states submitted recommendations calling for abolition or fundamental reform of the kafala system, criminalization of passport confiscation, and establishment of an independent wage protection system. Qatar accepted 11 of 17 labor-related recommendations.",
        "source": "UN UPR, A/HRC/WG.6/33/QAT/2, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Technology-Facilitated Recruitment Fraud",
        "summary": "UN Special Rapporteur on Trafficking (2020) issued a thematic report on online recruitment platforms, finding that fraudulent job advertisements on social media and recruitment apps had become the primary vector for trafficking of migrant workers in Southeast Asia, South Asia, and sub-Saharan Africa.",
        "source": "UN SR on Trafficking, A/75/290, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Migrants: COVID-19 and Migrant Worker Vulnerability",
        "summary": "UN Special Rapporteur on Migrants (2020) documented COVID-19's catastrophic impact on migrant workers: mass abandonment by employers without pay, denial of access to social protection, detention pending deportation, and inability to repatriate due to border closures while continuing to owe recruitment debts.",
        "source": "UN SR on Migrants, A/75/183, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Contemporary Forms of Slavery: Scam Compound Forced Criminality",
        "summary": "UN Special Rapporteur on Contemporary Forms of Slavery (2023) released findings on cyber scam compounds in Myanmar, Cambodia, and Laos where an estimated 100,000–200,000 people were held against their will and forced to conduct online fraud. Victims were primarily recruited through deceptive job advertisements across Southeast Asia, South Asia, and Africa.",
        "source": "UN SR on Contemporary Forms of Slavery, A/HRC/54/30, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Gender Dimensions of Labor Trafficking",
        "summary": "UN Special Rapporteur on Trafficking (2009) highlighted that women constitute approximately 55% of adult trafficking victims globally, concentrated in domestic work and entertainment sectors, and face additional barriers to redress including shame, risk of retrafficking, and gender bias in law enforcement responses.",
        "source": "UN SR on Trafficking, A/HRC/10/16, 2009",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR: Saudi Arabia Labor Reform Commitments",
        "summary": "Saudi Arabia's Universal Periodic Review (2018) resulted in acceptance of recommendations to strengthen the wage protection system, extend labor protections to domestic workers, allow worker-initiated contract transfers without employer consent, and ratify ILO Convention 189 on domestic workers.",
        "source": "UN UPR, A/HRC/WG.6/31/SAU/2, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Migrants: Bilateral Labor Agreement Gaps",
        "summary": "UN Special Rapporteur on Migrants (2015) found that bilateral labor agreements between sending and receiving states frequently lack binding enforcement mechanisms, creating nominal protections that recruiters and employers routinely ignore. The absence of tripartite monitoring—including trade unions—was identified as a systemic gap.",
        "source": "UN SR on Migrants, A/HRC/29/36, 2015",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Asylum Seekers and Trafficking Nexus",
        "summary": "UN Special Rapporteur on Trafficking (2016) documented the trafficking nexus in mixed migration flows, finding that refugees and asylum seekers transiting dangerous routes through Libya, Turkey, and Southeast Asia were systematically exploited by smugglers who transitioned into traffickers when payment demands could not be met.",
        "source": "UN SR on Trafficking, A/71/303, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "HRC Resolution: Business and Human Rights in Global Supply Chains",
        "summary": "UN Human Rights Council Resolution 26/22 (2014) affirmed that business enterprises have a responsibility to respect human rights throughout global supply chains, including labor rights of migrant workers, and called on states to enact mandatory human rights due diligence legislation for companies operating in high-risk sectors.",
        "source": "UN HRC Resolution 26/22, 2014",
    },

    # ── ILO Committee of Experts (CEACR) ───────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: Kuwait Passport Confiscation",
        "summary": "ILO Committee of Experts (2014) direct request to Kuwait under Convention No. 29 expressed serious concern that passport confiscation by employers of domestic workers remained widespread despite a nominal prohibition, and that no employer had been prosecuted under the provision, rendering the law ineffective.",
        "source": "ILO CEACR, C29 Observation, Kuwait, 2014",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: Qatar Exit Permit System",
        "summary": "ILO Committee of Experts (2016) found that Qatar's exit permit requirement—mandating employer consent before workers could leave the country—constituted a direct restriction on freedom of movement incompatible with the forced labor prohibition in Convention No. 29. Qatar was requested to abolish the system unconditionally.",
        "source": "ILO CEACR, C29 Observation, Qatar, 2016",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C105 Observation: State-Imposed Forced Labor in Uzbekistan",
        "summary": "ILO Committee of Experts (2013) maintained a long-standing observation on Uzbekistan under Convention No. 105 documenting state-organized mobilization of students, teachers, and civil servants for mandatory cotton harvesting under threat of expulsion or dismissal, constituting state-imposed forced labor.",
        "source": "ILO CEACR, C105 Observation, Uzbekistan, 2013",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C189 Direct Request: Philippines Domestic Worker Protections",
        "summary": "ILO Committee of Experts (2017) issued a direct request to the Philippines under Convention No. 189, welcoming the Domestic Workers Act (RA 10361) but noting inadequate enforcement mechanisms, insufficient labor inspector access to private homes, and lack of social security coverage for domestic workers employed abroad.",
        "source": "ILO CEACR, C189 Direct Request, Philippines, 2017",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C181 Observation: Indonesia Private Employment Agency Abuses",
        "summary": "ILO Committee of Experts (2018) observed that Indonesia's implementation of Convention No. 181 on private employment agencies remained inadequate, with unlicensed sub-agents operating extensively in rural areas, fee structures opaque and unregulated in practice, and migrant worker complaints systems inaccessible to those already deployed abroad.",
        "source": "ILO CEACR, C181 Observation, Indonesia, 2018",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: Saudi Arabia Domestic Worker Exclusions",
        "summary": "ILO Committee of Experts (2015) noted with concern that Saudi Arabia's Labor Law explicitly excludes domestic workers from its protections, leaving approximately 1.5 million migrant domestic workers without minimum wage, overtime pay, or access to labor dispute mechanisms, creating conditions conducive to forced labor under C29.",
        "source": "ILO CEACR, C29 Observation, Saudi Arabia, 2015",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: Myanmar Forced Labor by Military",
        "summary": "ILO Committee of Experts maintained observations on Myanmar under Convention No. 29 from 2000 to present, documenting military-imposed forced labor on civilians for portering, camp construction, and agriculture. The 2021 military coup prompted a special paragraph expressing grave concern at the resumption of systematic forced labor practices.",
        "source": "ILO CEACR, C29 Observation, Myanmar, Special Paragraph, 2021",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEACR C29 General Survey: Forced Labor in the Private Economy",
        "summary": "ILO Committee of Experts General Survey (2012) on forced labor conventions found that the vast majority of forced labor globally—an estimated 90%—now occurs in the private economy rather than through state compulsion, driven by recruitment fraud, debt bondage, and document confiscation, requiring a reorientation of enforcement toward private actors.",
        "source": "ILO CEACR, General Survey on C29 and C105, 2012",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: UAE Wage Theft Prevalence",
        "summary": "ILO Committee of Experts (2019) noted the UAE's wage protection system had reduced reported wage theft but expressed concern that domestic workers remained excluded, that the complaint mechanism required workers to remain in the country pending resolution, and that withheld wages constituted a forced labor indicator under C29.",
        "source": "ILO CEACR, C29 Observation, UAE, 2019",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C181 Observation: Nepal Fee-Charging Recruitment",
        "summary": "ILO Committee of Experts (2016) observed that Nepal had not effectively enforced its prohibition on recruitment fee-charging despite Convention No. 181 obligations, with agencies routinely collecting fees of NPR 50,000–150,000 (USD 500–1,500) from workers traveling to the Gulf, creating debt bondage conditions.",
        "source": "ILO CEACR, C181 Observation, Nepal, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEACR C189 Direct Request: Thailand Domestic Workers",
        "summary": "ILO Committee of Experts (2020) direct request to Thailand under C189 found that domestic workers—predominantly internal migrants and Myanmar nationals—remained excluded from core labor protections including minimum wage, maximum working hours, and occupational safety legislation, with no clear mechanism for filing wage complaints.",
        "source": "ILO CEACR, C189 Direct Request, Thailand, 2020",
    },

    # ── UN CERD ─────────────────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CERD Concluding Observations: Qatar Racial Discrimination in Labor",
        "summary": "UN Committee on the Elimination of Racial Discrimination (2012) expressed concern that Qatar's legal framework effectively enabled racial discrimination in the treatment of migrant workers from South and Southeast Asia versus Western expatriates, with differential access to dispute mechanisms, housing standards, and freedom to change employers.",
        "source": "UN CERD, Concluding Observations on Qatar, CERD/C/QAT/CO/13-16, 2012",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CERD Concluding Observations: Malaysia Plantation Worker Discrimination",
        "summary": "UN Committee on the Elimination of Racial Discrimination (2013) identified systemic racial discrimination against Tamil ethnic minority plantation workers and Rohingya migrants in Malaysia, finding that both groups faced exclusion from regularization programs and disproportionate detention, with distinct patterns of wage theft and movement restriction.",
        "source": "UN CERD, Concluding Observations on Malaysia, CERD/C/MYS/CO/17-23, 2013",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CERD Concluding Observations: UAE Migrant Worker Housing Segregation",
        "summary": "UN Committee on the Elimination of Racial Discrimination (2017) noted with concern that low-wage migrant workers in the UAE, predominantly of South Asian origin, were housed in segregated labor camps distant from urban areas with inadequate sanitation, restricted communication, and limited access to legal aid, creating conditions of racial segregation linked to labor exploitation.",
        "source": "UN CERD, Concluding Observations on UAE, CERD/C/ARE/CO/21-25, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CERD Concluding Observations: Japan Trainee Program Discrimination",
        "summary": "UN Committee on the Elimination of Racial Discrimination (2018) expressed concern that Japan's Technical Intern Training Program subjected foreign trainees—primarily Vietnamese, Chinese, and Indonesian nationals—to discriminatory conditions including wage suppression, movement restrictions, and inadequate labor protections not applicable to Japanese workers.",
        "source": "UN CERD, Concluding Observations on Japan, CERD/C/JPN/CO/7-9, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CERD Concluding Observations: Kuwait Bidun and Migrant Statelessness",
        "summary": "UN Committee on the Elimination of Racial Discrimination (2016) found that stateless Bidun individuals and undocumented migrant workers in Kuwait faced compounded vulnerability to exploitation due to lack of legal status, exclusion from nationality-based labor protections, and inability to access courts without valid documentation.",
        "source": "UN CERD, Concluding Observations on Kuwait, CERD/C/KWT/CO/21-24, 2016",
    },

    # ── UN CEDAW ────────────────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW General Recommendation 26: Women Migrant Workers",
        "summary": "UN Committee on the Elimination of Discrimination Against Women General Recommendation No. 26 (2008) provided comprehensive guidance on state obligations toward women migrant workers, identifying particular vulnerabilities of domestic workers and entertainment workers, and calling for bilateral agreement standards, portability of social protection, and access to shelters irrespective of immigration status.",
        "source": "UN CEDAW, General Recommendation 26, CEDAW/C/2009/WP.1/R, 2008",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW Concluding Observations: Philippines OFW Women Protections",
        "summary": "UN CEDAW Committee (2016) commended the Philippines' Overseas Workers Welfare Administration but expressed concern that enforcement of protections for Overseas Filipino Workers—the majority of whom are women in domestic or care work—remained inadequate, with contract substitution widespread and repatriation shelters underfunded.",
        "source": "UN CEDAW, Concluding Observations on Philippines, CEDAW/C/PHL/CO/7-8, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW Concluding Observations: Sri Lanka Domestic Worker Protections",
        "summary": "UN CEDAW Committee (2017) expressed concern that Sri Lanka's women migrant workers—concentrated in GCC domestic employment—faced high rates of abuse, sexual violence, and forced labor with inadequate pre-departure training, insufficient consular support, and a dysfunctional complaints mechanism that rarely achieved remediation or repatriation.",
        "source": "UN CEDAW, Concluding Observations on Sri Lanka, CEDAW/C/LKA/CO/8, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW Concluding Observations: Indonesia Migrant Worker Women",
        "summary": "UN CEDAW Committee (2021) noted that Indonesia had taken steps to reform its migrant worker protection law but remained concerned about the persistence of fee-charging by private agencies, the exclusion of undocumented women workers from state protection services, and the criminalization of irregular migration that deterred women from reporting abuse.",
        "source": "UN CEDAW, Concluding Observations on Indonesia, CEDAW/C/IDN/CO/8, 2021",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW Concluding Observations: Lebanon Domestic Worker Trafficking",
        "summary": "UN CEDAW Committee (2015) expressed serious concern about trafficking and severe exploitation of women domestic workers in Lebanon under the kafala system, noting that domestic workers—predominantly from Ethiopia, the Philippines, and Sri Lanka—had no legal remedy for abuse when their employers controlled their residency status.",
        "source": "UN CEDAW, Concluding Observations on Lebanon, CEDAW/C/LBN/CO/4-5, 2015",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW General Recommendation 38: Trafficking in Women and Girls",
        "summary": "UN CEDAW Committee General Recommendation No. 38 (2020) updated the framework on trafficking, emphasizing intersectionality of gender, poverty, migration status, and ethnicity in trafficking vulnerability, and affirming that states must ensure trafficking survivors have access to compensation, residency permits, and protection from deportation pending investigation.",
        "source": "UN CEDAW, General Recommendation 38, CEDAW/C/GC/38, 2020",
    },

    # ── UN CMW ──────────────────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CMW Concluding Observations: Mexico Migrant Transit Exploitation",
        "summary": "UN Committee on the Protection of the Rights of All Migrant Workers (2011) found that migrants transiting through Mexico—primarily from Central America—faced systematic exploitation by criminal organizations including forced labor, extortion, and trafficking, with state officials complicit through bribery. Mexico was urged to enact a comprehensive anti-trafficking law.",
        "source": "UN CMW, Concluding Observations on Mexico, CMW/C/MEX/CO/2, 2011",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CMW Concluding Observations: Philippines Emigration Protections",
        "summary": "UN Committee on Migrant Workers (2009) acknowledged the Philippines' relatively advanced regulatory framework for protecting migrant workers but raised concerns about the effectiveness of the ban on deployment to countries without bilateral agreements, the adequacy of legal assistance funds for overseas workers, and the lack of protection for undocumented workers abroad.",
        "source": "UN CMW, Concluding Observations on Philippines, CMW/C/PHL/CO/1, 2009",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CMW Concluding Observations: Ecuador Deportation Without Due Process",
        "summary": "UN Committee on Migrant Workers (2014) found that Ecuador conducted collective expulsions of migrants without individualized assessment, denied access to asylum procedures, and failed to protect trafficking victims among deported populations. The Committee noted that deportation of trafficking victims without identification violates CMW obligations.",
        "source": "UN CMW, Concluding Observations on Ecuador, CMW/C/ECU/CO/3, 2014",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CMW General Comment 2: Rights of Migrant Workers in Irregular Situations",
        "summary": "UN Committee on Migrant Workers General Comment No. 2 (2013) affirmed that irregular migrants retain the full set of human rights protections under the ICRMW and core human rights treaties, including protection from forced labor and trafficking, the right to back wages, and access to courts, regardless of immigration status.",
        "source": "UN CMW, General Comment 2, CMW/C/GC/2, 2013",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CMW Concluding Observations: Bangladesh Pre-Departure Vulnerabilities",
        "summary": "UN Committee on Migrant Workers (2021) found that Bangladesh's migration governance framework had significant gaps including inadequate licensing oversight of recruitment agencies, no effective maximum fee regulation enforced in practice, insufficient pre-departure information on rights, and no systematic reintegration support for returned trafficking victims.",
        "source": "UN CMW, Concluding Observations on Bangladesh, CMW/C/BGD/CO/1, 2021",
    },

    # ── UNHCR ───────────────────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UNHCR: Refugee Labor Exploitation in Kenya Nairobi Urban Context",
        "summary": "UNHCR (2014) documented that urban refugees in Nairobi—primarily from Somalia, DRC, and Ethiopia—faced systematic labor exploitation including wage theft, sexual exploitation tied to housing, and inability to complain due to fear of deportation to refugee camps or refoulement. Employers exploited refugees' irregular legal status as leverage.",
        "source": "UNHCR, Urban Refugee Livelihoods and Protection Gaps, Kenya, 2014",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UNHCR: Rohingya Refugee Labor Trafficking in Bangladesh",
        "summary": "UNHCR (2020) reported that Rohingya refugees in Cox's Bazar faced recruitment by traffickers offering deceptive employment abroad, primarily in Malaysia and the Middle East, with trafficking through dangerous sea routes involving debt bondage and violence at sea. Children were disproportionately targeted for domestic work trafficking.",
        "source": "UNHCR, Protection Monitoring Report, Cox's Bazar, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UNHCR: Syrian Refugee Labor Exploitation in Turkey",
        "summary": "UNHCR (2017) found that Syrian refugees in Turkey—the world's largest refugee population at 3.5 million—faced exploitation in textile, agricultural, and construction sectors, with child labor widespread, wages systematically below legal minimum, and employers aware that reporting exploitation risked deportation proceedings against workers.",
        "source": "UNHCR, Syrian Refugee Livelihoods and Vulnerability Assessment, Turkey, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UNHCR: Trafficking of Afghan Refugees via Iran and Turkey",
        "summary": "UNHCR (2016) documented trafficking of Afghan refugees transiting Iran and Turkey toward Europe, with traffickers charging fees of USD 3,000–12,000 per person that converted into debt bondage when victims could not pay, leading to forced labor in domestic work, begging rings, or further exploitation within the trafficking network.",
        "source": "UNHCR, Mixed Migration Monitoring, Afghanistan-Iran-Turkey Route, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UNHCR: Venezuelan Migrant Worker Exploitation in Colombia",
        "summary": "UNHCR (2021) documented exploitation of Venezuelan migrants and refugees in Colombia, Peru, and Ecuador in agricultural, domestic work, and construction sectors, with employers exploiting irregular status to pay below minimum wage, deny social security, and threaten deportation reports as a coercive tool to prevent complaints.",
        "source": "UNHCR, Venezuelan Refugee and Migrant Protection Report, 2021",
    },

    # ── Inter-American Court of Human Rights ────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACtHR Advisory Opinion OC-18: Undocumented Migrants and Labor Rights",
        "summary": "Inter-American Court of Human Rights Advisory Opinion OC-18/03 (2003) established that states may not deny labor rights to undocumented migrant workers, as such rights flow from the employment relationship itself and are not contingent on immigration status. The opinion created a foundational regional standard against exploitation of irregular migrants.",
        "source": "IACtHR, Advisory Opinion OC-18/03, September 2003",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACtHR: Ituango Massacres v. Colombia — Forced Labor During Armed Conflict",
        "summary": "Inter-American Court (2006) found Colombia internationally responsible for forced labor imposed on civilians by paramilitary groups with state acquiescence in Ituango, constituting a violation of Article 6 of the American Convention (prohibition of slavery and forced labor) and ordering reparations including investigation and prosecution of perpetrators.",
        "source": "IACtHR, Ituango Massacres v. Colombia, Judgment, July 2006",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACtHR: Brasil Verde Workers v. Brazil — Debt Bondage Constitutes Slave Labor",
        "summary": "Inter-American Court (2016) ruled that Brazil violated Article 6 (prohibition of slavery) and Article 22 (freedom of movement) of the American Convention through systemic debt bondage on sugar cane plantations in Pará state, where workers were held through debt, document retention, and geographic isolation. Brazil was ordered to pay USD 5 million in reparations and create a national fund for trafficking victims.",
        "source": "IACtHR, Fazenda Brasil Verde Workers v. Brazil, Judgment, October 2016",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACtHR Advisory Opinion OC-21: Rights of Children in Migration",
        "summary": "Inter-American Court Advisory Opinion OC-21/14 (2014) affirmed that migrant children—including unaccompanied children and children of undocumented parents—have the right to be identified as trafficking victims before any deportation or detention, and that states must provide specialized child protection responses that prioritize best interests over immigration enforcement.",
        "source": "IACtHR, Advisory Opinion OC-21/14, August 2014",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACtHR: Juridical Condition of Undocumented Migrants — Non-Discrimination Principle",
        "summary": "Inter-American Court (2003) reaffirmed through OC-18 that the principle of non-discrimination and equality before the law constitutes jus cogens—a peremptory norm of international law—from which no derogation is permitted, including through immigration enforcement measures that result in differential labor rights for migrant workers.",
        "source": "IACtHR, OC-18/03, Juridical Condition and Rights of Undocumented Migrants, 2003",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACtHR: Massacres of El Mozote — Forced Domestic Servitude During Conflict",
        "summary": "Inter-American Court (2012) found El Salvador violated the American Convention including through forced domestic servitude imposed on women survivors of the El Mozote massacres by military units, establishing that wartime forced labor of women constitutes both a forced labor violation and a form of gender-based violence.",
        "source": "IACtHR, Massacres of El Mozote v. El Salvador, Judgment, October 2012",
    },

    # ── African Court on Human and Peoples' Rights ──────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "Africa",
        "title": "African Commission: Specific Recommendations on Migrant Worker Exploitation in North Africa",
        "summary": "African Commission on Human and Peoples' Rights (2018) Resolution 376 condemned trafficking and forced labor of sub-Saharan African migrants in Libya and North Africa, calling on African Union member states to establish emergency repatriation funds, investigate trafficking networks, and decriminalize irregular migration to encourage victim reporting.",
        "source": "African Commission on Human and Peoples' Rights, Resolution 376, 2018",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Africa",
        "title": "African Court: Ernest Francis Mtingwi v. Malawi — Trafficking Victim Non-Refoulement",
        "summary": "African Court on Human and Peoples' Rights (2013) affirmed in provisional measures that trafficking victims must not be forcibly returned to their country of origin without a proper risk assessment, establishing a regional non-refoulement standard for trafficking victims analogous to refugee law protections.",
        "source": "African Court on Human and Peoples' Rights, Mtingwi v. Malawi, Application No. 001/2012",
    },
    {
        "type": "advisory",
        "jurisdiction": "Africa",
        "title": "African Commission: Study on Forced Labor and Trafficking",
        "summary": "African Commission on Human and Peoples' Rights (2015) study documented that domestic work trafficking corridors within Africa—including West Africa, the Horn of Africa, and Southern Africa—involved patterns of deception, debt bondage, and document confiscation analogous to intercontinental trafficking, requiring equivalent legal protections for internal trafficking victims.",
        "source": "African Commission, Study on Forced Labour, Slavery and Similar Practices, 2015",
    },

    # ── ASEAN ACTIP / ACMW ─────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "ASEAN",
        "title": "ASEAN Convention Against Trafficking (ACTIP) — Victim Identification Standards",
        "summary": "The ASEAN Convention Against Trafficking in Persons, Especially Women and Children (2015) requires all ASEAN member states to establish formal victim identification mechanisms, non-punishment provisions for trafficking victims who have committed crimes as a direct result of trafficking, and access to legal assistance and rehabilitation services.",
        "source": "ASEAN ACTIP, 2015, Articles 14–18",
    },
    {
        "type": "policy_update",
        "jurisdiction": "ASEAN",
        "title": "ACMW Vientiane Declaration on Transition from Informal to Formal Employment",
        "summary": "ASEAN Committee on Migrant Workers (2016) Vientiane Declaration called on member states to facilitate regularization of undocumented migrant workers, harmonize labor standards across ASEAN, and develop a regional framework for portability of social protection benefits to reduce debt bondage risk arising from informal labor arrangements.",
        "source": "ASEAN ACMW, Vientiane Declaration, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "ASEAN",
        "title": "ACTIP Assessment: Cyber Scam Trafficking in the Mekong",
        "summary": "ASEAN ACTIP Senior Officials Meeting (2023) assessment found that cyber scam compound trafficking in Myanmar, Cambodia, and Laos had emerged as the dominant form of trafficking in the ASEAN region by victim volume, requiring new legal frameworks addressing forced criminality and providing legal status to victims who had entered countries irregularly when trafficked.",
        "source": "ASEAN SOMTC Working Group on ACTIP, Assessment Report, 2023",
    },
    {
        "type": "policy_update",
        "jurisdiction": "ASEAN",
        "title": "ACMW: ASEAN Instrument on Protection and Promotion of Rights of Migrant Workers",
        "summary": "The ASEAN Consensus on the Protection and Promotion of the Rights of Migrant Workers (2017) established non-binding regional standards covering access to employment contracts, prohibition of recruitment fee-charging by employers, access to courts, and consular protection. Civil society criticized the instrument for omitting undocumented migrants from its scope.",
        "source": "ASEAN Consensus on Migrant Workers, 2017",
    },

    # ── GRETA (Council of Europe) ───────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: United Kingdom — Labour Trafficking Identification Failures",
        "summary": "Group of Experts on Action Against Trafficking (GRETA) evaluation of the United Kingdom (2016) found serious failures in the National Referral Mechanism, with labor trafficking victims—particularly in agriculture, car washes, and domestic work—systematically misidentified as immigration offenders, resulting in detention and deportation rather than protection.",
        "source": "GRETA, Report on the UK, GRETA(2016)21, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Greece — Migrant Agricultural Worker Exploitation",
        "summary": "GRETA evaluation of Greece (2017) documented severe labor exploitation of migrant agricultural workers in Manolada and similar sites, where workers—primarily from Bangladesh and sub-Saharan Africa—were paid below minimum wage, housed in degrading conditions, and faced violence from overseers, with the 2013 Manolada shooting case involving a prosecution that GRETA found inadequate in its outcomes.",
        "source": "GRETA, Report on Greece, GRETA(2017)27, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Romania — Trafficking Victim Compensation Gap",
        "summary": "GRETA evaluation of Romania (2018) found that despite Romania being the EU's largest trafficking origin country, only a tiny fraction of identified trafficking victims had received compensation or civil damages, and that the state compensation fund was effectively inaccessible due to procedural barriers and lack of legal aid.",
        "source": "GRETA, Report on Romania, GRETA(2018)7, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Ireland — Domestic Worker Trafficking",
        "summary": "GRETA evaluation of Ireland (2020) expressed concern that the 'au pair' immigration category was being used by employers to bring domestic workers under conditions of exploitation—no minimum wage entitlement, no working hours limit, no independent residency—while the Atypical Working Scheme lacked sufficient oversight to prevent abuse.",
        "source": "GRETA, Report on Ireland, GRETA(2020)06, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Netherlands — Supply Chain Labor Trafficking",
        "summary": "GRETA evaluation of the Netherlands (2018) found that labor trafficking in Dutch supply chains—particularly in horticulture, meat processing, and logistics—was extensive, with victims primarily from Eastern Europe (Romania, Bulgaria, Poland) and sub-Saharan Africa, and that intermediary companies exploited a legal gap allowing them to profit from exploitation without criminal liability.",
        "source": "GRETA, Report on Netherlands, GRETA(2018)19, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: France — Domestic Worker Trafficking and Diplomatic Immunity",
        "summary": "GRETA evaluation of France (2017) noted specific concerns about domestic workers brought to France by diplomats and international organization staff under special visas, where workers faced trafficking conditions but could not pursue legal remedies due to diplomatic immunity enjoyed by their employers.",
        "source": "GRETA, Report on France, GRETA(2017)17, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Germany — Seasonal Worker Exploitation",
        "summary": "GRETA evaluation of Germany (2019) found that seasonal workers in German agriculture—predominantly from Romania, Poland, and Bulgaria—faced systematic exploitation including wage theft, excessive accommodation deductions, restricted movement between sites, and employer-controlled housing that facilitated coercion.",
        "source": "GRETA, Report on Germany, GRETA(2019)09, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Spain — Domestic Worker Undocumented Status Exploitation",
        "summary": "GRETA second evaluation of Spain (2018) found that domestic workers—a sector where 90% are women and disproportionately migrants—faced exploitation compounded by exclusion from the general social insurance system, inability to access shelters available to other trafficking victims, and immigration enforcement operations that deterred reporting.",
        "source": "GRETA, Second Report on Spain, GRETA(2018)17, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Cyprus — Cabaret Artiste Visa Trafficking",
        "summary": "GRETA evaluation of Cyprus (2016) found that the 'artiste' visa category—historically used to bring women from Eastern Europe, the Philippines, and the Dominican Republic for entertainment work—remained a significant trafficking vector despite partial reforms, with women arriving under contracts that misrepresented the sexual nature of work required.",
        "source": "GRETA, Report on Cyprus, GRETA(2016)24, 2016",
    },

    # ── OSCE Special Representative ─────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "OSCE Special Representative: Trafficking in the Agricultural Sector",
        "summary": "OSCE Special Representative and Co-ordinator for Combating Trafficking in Human Beings (2009) thematic report documented pervasive labor trafficking in European agriculture—including seasonal fruit picking, vegetable farming, and greenhouse work—with victims trafficked from Eastern Europe, Africa, and Asia through fraudulent seasonal work schemes.",
        "source": "OSCE, Efforts to Combat Trafficking in Human Beings in the OSCE Area, 2009",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "OSCE Special Representative: Trafficking for Forced Begging",
        "summary": "OSCE Special Representative report (2011) found that organized criminal networks operating across European OSCE member states trafficked Roma, disabled persons, and migrant children for forced begging, with victims moved regularly between cities to evade law enforcement and held through debt bondage, violence, and document confiscation.",
        "source": "OSCE SR, Trafficking for Forced Begging, 2011",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "OSCE Special Representative: Labour Trafficking in Domestic Work",
        "summary": "OSCE Special Representative (2010) highlighted domestic work as among the highest-risk trafficking sectors in OSCE states, noting that the private household setting made labor inspection practically impossible, that live-in requirements created total employer control over workers' daily lives, and that immigration visa systems tying workers to specific employers enabled coercion.",
        "source": "OSCE SR, Combating Trafficking as Modern-Day Slavery, 2010",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "OSCE: Technology and Trafficking — Online Recruitment Fraud",
        "summary": "OSCE Office for Democratic Institutions and Human Rights (2020) report on technology-facilitated trafficking found that social media platforms, encrypted messaging apps, and online job boards had transformed trafficking recruitment, with fraudulent job advertisements generating the majority of initial victim contacts in OSCE participating states.",
        "source": "OSCE ODIHR, Report on Technology and Trafficking, 2020",
    },

    # ── Regional-Specific Country Findings ─────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Country Visit to Thailand — Fishing Industry",
        "summary": "UN Special Rapporteur on Trafficking's country visit to Thailand (2011) documented that forced labor in the Thai fishing industry involved men and boys recruited from Myanmar, Cambodia, and Laos under deceptive promises of factory work, held on vessels through debt bondage and violence, with complicity of vessel owners, brokers, and port officials.",
        "source": "UN SR on Trafficking, Mission to Thailand, A/HRC/26/37/Add.2, 2011",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Contemporary Forms of Slavery: Country Visit to Qatar",
        "summary": "UN Special Rapporteur on Contemporary Forms of Slavery (2013) country visit to Qatar found that the kafala system, combined with the exit permit requirement, constituted conditions analogous to slavery for workers who had entered under deceptive contract terms, owed recruitment debts, and faced criminal liability for absconding if they sought to escape abusive employers.",
        "source": "UN SR on Contemporary Forms of Slavery, Mission to Qatar, A/HRC/24/43/Add.1, 2013",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Migrants: Country Visit to Philippines — Emigration Governance",
        "summary": "UN Special Rapporteur on Migrants (2008) country visit to the Philippines praised the Philippines' pioneering emigrant worker protection framework but noted significant gaps: insufficient regulation of sub-agents operating in rural areas, inadequate enforcement of bilateral agreements, and inconsistent consular protection standards across receiving countries.",
        "source": "UN SR on Migrants, Mission to Philippines, A/HRC/11/7/Add.2, 2008",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Country Visit to Nepal — Recruitment Fraud",
        "summary": "UN Special Rapporteur on Trafficking (2018) country visit to Nepal documented a pervasive recruitment fraud ecosystem in which unlicensed sub-agents operating through village networks recruited workers with false promises, collected fees exceeding legal maximums, and disappeared after deployment, leaving workers indebted with no recourse against now-defunct agencies.",
        "source": "UN SR on Trafficking, Mission to Nepal, A/HRC/38/45/Add.1, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Contemporary Forms of Slavery: Country Visit to Myanmar",
        "summary": "UN Special Rapporteur on Contemporary Forms of Slavery (2014) country visit to Myanmar documented systematic forced labor imposed by military and police—including village portering, forced construction, and agricultural labor—alongside trafficking of Myanmar women into marriage in China and trafficking of men into fishing vessels across Southeast Asia.",
        "source": "UN SR on Contemporary Forms of Slavery, Mission to Myanmar, A/HRC/27/53/Add.1, 2014",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Migrants: Country Visit to Malaysia — Migrant Worker Rights",
        "summary": "UN Special Rapporteur on Migrants (2010) country visit to Malaysia found that the system of migrant worker regulation—requiring specific employer-tied permits, imposing criminal penalties for employment outside permitted sector, and allowing detention of workers who complained about violations—systematically disadvantaged workers and enabled exploitation.",
        "source": "UN SR on Migrants, Mission to Malaysia, A/HRC/14/30/Add.1, 2010",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Country Visit to Mexico — Central American Transit",
        "summary": "UN Special Rapporteur on Trafficking (2008) country visit to Mexico found that Central American migrants transiting toward the United States faced industrial-scale trafficking and kidnapping by organized criminal groups, with migrants' fear of immigration enforcement preventing reporting, and inadequate shelters and legal assistance at key transit points.",
        "source": "UN SR on Trafficking, Mission to Mexico, A/HRC/10/16/Add.1, 2008",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Migrants: Country Visit to Saudi Arabia — Worker Exploitation",
        "summary": "UN Special Rapporteur on Migrants (2008) country visit to Saudi Arabia raised concerns about passport confiscation, absence of labor protections for domestic workers, and the kafala system, particularly noting that women domestic workers who fled abusive employers could face criminal charges for 'absconding' under provisions that disproportionately punished victims of exploitation.",
        "source": "UN SR on Migrants, Mission to Saudi Arabia, A/HRC/11/7/Add.3, 2008",
    },

    # ── Specific Thematic Reports and Findings ──────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "ILO Global Estimates: 27.6 Million in Forced Labor (2022)",
        "summary": "ILO Global Estimates on Modern Slavery (2022) found 27.6 million people in forced labor globally, including 17.3 million in private sector forced labor, 6.3 million in forced commercial sexual exploitation, and 3.9 million in state-imposed forced labor. Migrants account for 15% of forced labor victims but represent only 4.7% of the global adult population, indicating disproportionate vulnerability.",
        "source": "ILO, Walk Free, IOM, Global Estimates of Modern Slavery, 2022",
    },
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "ILO: Forced Labor Generates USD 236 Billion Annually",
        "summary": "ILO (2023) estimated that forced labor—including trafficking—generates USD 236 billion in illegal profits annually, with forced commercial sexual exploitation generating USD 140 billion, forced labor in private economy USD 84 billion (construction, manufacturing, agriculture, domestic work), and state-imposed forced labor USD 12 billion.",
        "source": "ILO, Profits and Poverty: The Economics of Forced Labour, 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "UNODC: Trafficking Convictions Remain Globally Low",
        "summary": "UNODC Global Report on Trafficking in Persons (2022) found that despite approximately 49,000 victims identified globally per year, only about 7,000 trafficking convictions were recorded annually, representing a massive accountability gap. Labor trafficking convictions were far fewer than sexual exploitation convictions, with conviction rates below 1% relative to estimated victim numbers.",
        "source": "UNODC, Global Report on Trafficking in Persons, 2022",
    },
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "ILO: Domestic Workers Face Highest Forced Labor Rates",
        "summary": "ILO data (2021) indicated that domestic work is one of the sectors with the highest forced labor prevalence globally, with an estimated 1 in 33 domestic workers globally in forced labor conditions. In the GCC states, survey data suggested prevalence rates of forced labor indicators among migrant domestic workers as high as 1 in 5.",
        "source": "ILO, Care Work and Care Jobs for the Future of Decent Work, 2021",
    },
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "UNODC: Women and Girls Comprise 72% of Trafficking Victims",
        "summary": "UNODC Global Report on Trafficking in Persons (2020) found that women and girls constitute approximately 72% of all detected trafficking victims globally, with adult women comprising 46% and girls 19% of victims. In labor trafficking specifically, the share of male victims is higher (approximately 35%) concentrated in fishing, construction, and manufacturing.",
        "source": "UNODC, Global Report on Trafficking in Persons, 2020",
    },
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "ILO: Migrant Workers Pay USD 22 Billion Annually in Recruitment Fees",
        "summary": "ILO (2017) estimated that migrant workers worldwide pay approximately USD 22 billion annually in recruitment fees—both legal and illegal—with average fees equivalent to 6–8 months of wages in destination countries for workers in low-wage sectors. Fee-charging creates structural debt bondage for an estimated 24 million workers globally.",
        "source": "ILO, Tackling Vulnerability in Labour Migration: Reducing Costs and Managing Risks, 2017",
    },

    # ── ILO Protocol P029 and Forced Labor ─────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "International",
        "title": "ILO Protocol P029: Supplementing Convention 29 on Forced Labor",
        "summary": "ILO Protocol of 2014 to the Forced Labour Convention (P029) requires ratifying states to take measures on prevention, victim protection, and access to remedies including compensation, and to support international cooperation. As of 2024, 60 states have ratified P029, including major sending and receiving states, though many GCC states have not ratified.",
        "source": "ILO, P029 Protocol to the Forced Labour Convention, 2014",
    },
    {
        "type": "law",
        "jurisdiction": "International",
        "title": "ILO Convention 189 on Domestic Workers — Ratification Status",
        "summary": "ILO Convention No. 189 on Decent Work for Domestic Workers (2011) had been ratified by 39 states as of 2024. Notable non-ratifiers include Saudi Arabia, UAE, Qatar, Kuwait, Malaysia, and Singapore—the primary destination states for migrant domestic workers from Southeast Asia and South Asia—which significantly weakens the convention's practical impact.",
        "source": "ILO, C189 Ratification Status, NORMLEX Database, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO Supervisory System: Myanmar Special Paragraph on Forced Labor",
        "summary": "Myanmar received a 'special paragraph' in ILO Committee of Experts reports—the most serious expression of concern—from 2000 continuously through present, with the 2021 military coup prompting the ILO Governing Body to issue a special resolution urging member states to review relations with Myanmar due to the grave deterioration of forced labor conditions.",
        "source": "ILO Governing Body, Resolution on Myanmar, GB.341/INS/7(Rev.), 2021",
    },

    # ── European Court of Human Rights (ECHR) ──────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "Europe",
        "title": "ECtHR: Siliadin v. France — Domestic Servitude Violates Article 4",
        "summary": "European Court of Human Rights (2005) found France had violated Article 4 (prohibition of slavery and forced labor) of the European Convention by failing to provide adequate criminal law protection against domestic servitude. The victim, a Togolese girl, had been held as a domestic servant without pay, schooling, or freedom of movement. The case established that states have positive obligations to criminalize domestic servitude.",
        "source": "ECtHR, Siliadin v. France, Application No. 73316/01, July 2005",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Europe",
        "title": "ECtHR: Rantsev v. Cyprus and Russia — Trafficking State Obligations",
        "summary": "European Court of Human Rights (2010) found both Cyprus and Russia violated the European Convention in the trafficking-related death of a Russian woman brought to Cyprus on an 'artiste' visa for entertainment work. The Court held that Article 4 imposes on states obligations to criminalize trafficking, investigate cases, and protect victims—obligations both states had failed to fulfil.",
        "source": "ECtHR, Rantsev v. Cyprus and Russia, Application No. 25965/04, January 2010",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Europe",
        "title": "ECtHR: C.N. and V. v. France — Forced Labor of Asylum Seekers",
        "summary": "European Court of Human Rights (2012) found France violated Article 4 by failing to effectively investigate and prosecute forced labor and servitude of two Burundian women held as domestic servants by relatives, who had controlled their asylum proceedings and withheld wages. The case extended Siliadin's obligations to ensure effective criminal investigation of complaints.",
        "source": "ECtHR, C.N. and V. v. France, Application No. 67724/09, October 2012",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Europe",
        "title": "ECtHR: Chowdury v. Greece — Forced Labor of Migrant Agricultural Workers",
        "summary": "European Court of Human Rights Grand Chamber (2017) ruled in Chowdury and Others v. Greece that Greece violated Article 4 in the Manolada strawberry farm forced labor case, where 150 Bangladeshi workers were shot when demanding unpaid wages. The Court found the conditions—withheld wages, threats, guarded housing—constituted forced labor, and Greece had failed its positive obligation to investigate and prosecute effectively.",
        "source": "ECtHR, Chowdury and Others v. Greece, Application No. 21884/15, March 2017",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Europe",
        "title": "ECtHR: M. and Others v. Italy and Bulgaria — Trafficking Investigation Failures",
        "summary": "European Court of Human Rights (2012) found Italy violated Article 4 by failing to identify a potential trafficking victim and instead treating her as an irregular migrant and deporting her to Bulgaria without any trafficking risk assessment. The case established that states must actively investigate trafficking indicators before deportation of vulnerable migrants.",
        "source": "ECtHR, M. and Others v. Italy and Bulgaria, Application No. 40020/03, July 2012",
    },

    # ── UN Human Rights Committee ───────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "HRC General Comment 35: Article 9 Liberty — Migrant Detention Standards",
        "summary": "UN Human Rights Committee General Comment No. 35 (2014) on Article 9 (right to liberty) affirmed that immigration detention must be necessary, proportionate, and subject to judicial review, and that states cannot systematically detain migrant workers or trafficking victims as a matter of immigration policy, as such detention facilitates further exploitation.",
        "source": "UN HRC, General Comment 35, CCPR/C/GC/35, 2014",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "HRC General Comment 36: Article 6 — Right to Life and Migration",
        "summary": "UN Human Rights Committee General Comment No. 36 (2018) on the right to life affirmed that states have obligations to protect the lives of migrant workers facing life-threatening conditions in exploitative employment—including excessive heat, dangerous fishing conditions, and violent enforcement—and must investigate migrant worker deaths attributable to employer negligence.",
        "source": "UN HRC, General Comment 36, CCPR/C/GC/36, 2018",
    },

    # ── ILO Tripartite MNE Declaration and Supply Chains ───────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO MNE Declaration: Supply Chain Due Diligence on Forced Labor",
        "summary": "ILO Tripartite Declaration of Principles Concerning Multinational Enterprises (5th edition, 2017) called on multinational enterprises to conduct human rights due diligence throughout their supply chains, including identification and remediation of forced labor and trafficking, with particular attention to migrant worker recruitment practices in sourcing countries.",
        "source": "ILO, MNE Declaration, 5th edition, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UN Guiding Principles on Business and Human Rights — Migrant Worker Application",
        "summary": "UN Working Group on Business and Human Rights (2019) issued guidance on applying the UN Guiding Principles to migrant workers, clarifying that companies' duty to respect human rights includes ensuring their recruitment practices do not generate debt bondage, that their suppliers do not use passport confiscation, and that grievance mechanisms are accessible to workers regardless of immigration status.",
        "source": "UN Working Group on Business and Human Rights, Guidance on Migrant Workers, 2019",
    },

    # ── Global Compact / Sustainable Development Goal Monitoring ───────────────
    {
        "type": "policy_update",
        "jurisdiction": "International",
        "title": "Global Compact for Migration: Objective 6 — Fair Recruitment",
        "summary": "Global Compact for Safe, Orderly and Regular Migration (2018), Objective 6, committed signatory states to facilitate fair and ethical recruitment, reduce costs for migrant workers, and review recruitment fee practices. The Compact's follow-up reporting identified progress in 34 states on fee reform but noted persistent enforcement gaps in 90+ states.",
        "source": "UN Global Compact for Migration, GCM/1 (Objective 6), 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SDG 8.7 — Forced Labor Eradication Target Progress Assessment",
        "summary": "UN Voluntary National Reviews and SDG monitoring (2022) found that SDG Target 8.7—ending forced labor, modern slavery, and human trafficking by 2030—was severely off track, with the number of forced labor victims increasing rather than decreasing since the target was set in 2015, requiring significantly accelerated action on recruitment reform, labor inspection, and survivor remediation.",
        "source": "UN, SDG 8.7 Alliance Progress Report, 2022",
    },

    # ── OHCHR Thematic Reports ─────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OHCHR: Recommended Principles on Trafficking and Human Rights",
        "summary": "OHCHR Recommended Principles and Guidelines on Human Rights and Human Trafficking (2002, updated 2010) established the foundational human rights framework for anti-trafficking policy, including primacy of victim rights over criminal prosecution interests, non-punishment of victims, trafficking survivor access to remedies, and mandatory reflection periods before any deportation decision.",
        "source": "OHCHR, Recommended Principles and Guidelines on Human Rights and Human Trafficking, E/2002/68/Add.1",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OHCHR: Report on Migration Governance and Human Rights Compatibility",
        "summary": "OHCHR (2018) report on international migration and human rights found that most states' migration governance frameworks were incompatible with their human rights obligations in multiple dimensions: criminalization of irregular entry, denial of access to courts, mandatory immigration detention, and exclusion of domestic workers and agricultural workers from labor law.",
        "source": "OHCHR, Report A/HRC/37/34 on Migration Governance and Human Rights, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OHCHR: Impact of Coronavirus on Trafficking and Labor Exploitation",
        "summary": "OHCHR (2020) rapid assessment found COVID-19 had worsened vulnerability to trafficking through job loss, stranded migrant workers unable to return home, surge in online recruitment fraud targeting unemployed workers, and diversion of law enforcement from anti-trafficking to pandemic enforcement, creating conditions for exploitation to expand while detection declined.",
        "source": "OHCHR, Rapid Assessment on COVID-19 and Trafficking, 2020",
    },

    # ── FATF and Financial Flows ────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "FATF: Financial Flows from Human Trafficking",
        "summary": "Financial Action Task Force (2018) report on financial flows from human trafficking found that traffickers use shell companies, cash-intensive businesses (especially restaurants, nail bars, car washes, cleaning companies), and cryptocurrency to launder proceeds, and that financial intelligence from banks and money service businesses was an underutilized tool for identifying trafficking networks.",
        "source": "FATF, Financial Flows from Human Trafficking, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "FATF: Money Laundering from Labor Trafficking in Supply Chains",
        "summary": "FATF (2019) found that labor trafficking in global supply chains—particularly manufacturing, agriculture, and domestic work—generates substantial financial flows that are laundered through legitimate business structures, including through the manipulation of intra-company transfer pricing, that are extremely difficult to detect through conventional anti-money laundering frameworks.",
        "source": "FATF, Money Laundering from Environmental Crime and Labour Trafficking, 2019",
    },

    # ── Regional Treaty Body Findings ──────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACHR: Precautionary Measures for Venezuelan Migrants in Trinidad",
        "summary": "Inter-American Commission on Human Rights (2019) granted precautionary measures for Venezuelan migrants in Trinidad and Tobago facing mass deportation without trafficking risk assessment, noting that the Commission had received numerous reports of Venezuelan women being trafficked in the Caribbean and that deportation without screening violated inter-American human rights standards.",
        "source": "IACHR, Precautionary Measure PM-365/18, Venezuela/Trinidad and Tobago, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "Americas",
        "title": "IACHR: Report on Trafficking in the Americas",
        "summary": "Inter-American Commission on Human Rights (2019) thematic report on trafficking found that criminal prosecution of trafficking in the Americas remained concentrated on sexual exploitation with labor trafficking severely under-prosecuted; that indigenous women and girls faced acute trafficking vulnerability linked to land dispossession and poverty; and that state institutional responses consistently prioritized migration control over victim protection.",
        "source": "IACHR, Trafficking in Persons in the Americas, OEA/Ser.L/V/II., 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "Africa",
        "title": "African Commission: Resolution on Trafficking in Africa",
        "summary": "African Commission on Human and Peoples' Rights Resolution 317 (2015) called on African Union member states to harmonize anti-trafficking legislation, strengthen the Ouagadougou Action Plan against Trafficking, establish bilateral labor agreements with destination states outside Africa, and provide legal assistance to African trafficking victims abroad.",
        "source": "African Commission on Human and Peoples' Rights, Resolution 317, 2015",
    },

    # ── Country-Specific UPR Labor Findings ────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR: UAE Kafala Reform Recommendations",
        "summary": "UAE's Universal Periodic Review (2022) received recommendations from 41 states to abolish the kafala system, extend labor law protections to domestic workers, establish accessible labor courts, ratify ILO Convention 189, and create an independent wage protection enforcement mechanism. The UAE accepted partial recommendations and rejected abolition of kafala.",
        "source": "UN UPR, A/HRC/WG.6/41/ARE/2, 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR: Kuwait Migrant Worker Protections",
        "summary": "Kuwait's Universal Periodic Review (2020) generated recommendations from 38 states addressing kafala reform, criminalization of passport confiscation, extension of labor law to domestic workers, ratification of ILO C189, and review of the sponsorship system that links worker residency to employer approval. Kuwait accepted recommendations in principle while maintaining the kafala framework.",
        "source": "UN UPR, A/HRC/WG.6/36/KWT/2, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR: Bahrain Migrant Worker Treatment",
        "summary": "Bahrain's Universal Periodic Review (2017) included recommendations from 26 states on protection of migrant workers including abolition of the exit ban, access to justice for domestic workers, and prohibition of contract substitution. Bahrain's 2009 partial kafala reforms—allowing employer transfer without permission in some circumstances—were noted but found inadequate by recommending states.",
        "source": "UN UPR, A/HRC/WG.6/28/BHR/2, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR: Malaysia Anti-Trafficking Enforcement Gaps",
        "summary": "Malaysia's Universal Periodic Review (2018) generated recommendations on expanding the legal definition of trafficking, increasing prosecutions of labor trafficking (not just sexual exploitation), decriminalizing trafficking victims for immigration offenses, and extending labor inspection to export processing zones where exploitation is prevalent.",
        "source": "UN UPR, A/HRC/WG.6/31/MYS/2, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR: Singapore Foreign Worker Treatment",
        "summary": "Singapore's Universal Periodic Review (2021) received recommendations from 22 states addressing the Foreign Domestic Worker levy system that transfers recruitment costs to workers, the bond system creating financial penalties for employers if workers abscond—which critics noted incentivized employer coercion—and inadequate criminal protections for domestic workers.",
        "source": "UN UPR, A/HRC/WG.6/39/SGP/2, 2021",
    },

    # ── Specialized UN Body Findings ───────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UN Special Rapporteur on Extreme Poverty: Migrant Workers and Poverty Traps",
        "summary": "UN Special Rapporteur on Extreme Poverty and Human Rights (2019) found that recruitment debt, wage theft, and exclusion from social protection create poverty traps for migrant workers from which escape is practically impossible without debt relief or compensation mechanisms, constituting a systemic human rights failure by both sending and receiving states.",
        "source": "UN SR on Extreme Poverty, A/HRC/41/39/Add.1, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UN Special Rapporteur on Right to Health: Migrant Worker Healthcare Denial",
        "summary": "UN Special Rapporteur on the Right to Health (2014) found that denial of healthcare access to migrant workers—documented in GCC states, Malaysia, and parts of Europe—constituted a violation of the right to health under international law, with migrant workers reporting workplace injuries untreated, occupational disease uncompensated, and mental health impacts of exploitation unaddressed.",
        "source": "UN SR on Right to Health, A/HRC/26/31, 2014",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UN Special Rapporteur on Housing: Migrant Worker Housing Exploitation",
        "summary": "UN Special Rapporteur on Adequate Housing (2015) found that employer-controlled housing for migrant workers—prevalent in GCC labor camps, Southeast Asian manufacturing dormitories, and agricultural worker housing in Europe—facilitated exploitation by allowing employers to charge excessive rents as wage deductions, use eviction as coercive threat, and monitor workers' movements and communications.",
        "source": "UN SR on Adequate Housing, A/HRC/28/62, 2015",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UN Special Rapporteur on Food: Agricultural Worker Forced Labor",
        "summary": "UN Special Rapporteur on the Right to Food (2012) documented that agricultural migrant workers globally faced systematic forced labor through debt bondage at harvest time, exclusion from labor protections applicable to other sectors, and piece-rate wage systems that made earning a subsistence wage dependent on physically impossible quotas enforced through debt.",
        "source": "UN SR on Right to Food, A/67/268, 2012",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UN Special Rapporteur on Education: Trafficking for Forced Schooling Fraud",
        "summary": "UN Special Rapporteur on the Right to Education (2010) documented a specific trafficking modality: recruiters in rural communities of South and Southeast Asia fraudulently offered children education opportunities in cities, delivering them instead into domestic servitude or factory work, exploiting parental aspirations for children's education as a recruitment vector.",
        "source": "UN SR on Right to Education, A/HRC/14/25, 2010",
    },

    # ── ILO Sectoral Findings ──────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: Construction Sector Forced Labor — Middle East and Asia",
        "summary": "ILO (2017) sectoral analysis of construction forced labor found that migrant construction workers in Qatar, UAE, Saudi Arabia, and Malaysia faced debt bondage through recruitment fees, unsafe conditions with labor inspection access restricted on major projects, and wage theft facilitated by subcontracting chains that dispersed responsibility for payments.",
        "source": "ILO, Migrant Workers in Construction: Decent Work Deficit, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: Fishing Sector Forced Labor — Thai and Regional Vessels",
        "summary": "ILO (2016) research on the Thai fishing industry found that 17% of Thai fishing vessel workers surveyed reported experiencing forced labor indicators—including being unable to leave the vessel, violence by supervisors, withheld wages, and debt bondage—with migrant workers from Myanmar and Cambodia facing significantly higher rates than Thai nationals.",
        "source": "ILO, Caught at Sea: Forced Labour and Trafficking in the Fishing Industry, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: Domestic Work Sector — Global Statistics and Exploitation Patterns",
        "summary": "ILO (2013) global survey of domestic workers found that 53% of domestic workers worldwide were excluded from national labor law, 45% had no access to paid annual leave, and 36% had no entitlement to a weekly rest day. Migrant domestic workers faced an additional layer of vulnerability through immigration status dependency on employer sponsorship.",
        "source": "ILO, Domestic Workers Across the World: Global and Regional Statistics, 2013",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: Electronics Supply Chain Due Diligence on Forced Labor",
        "summary": "ILO (2014) found that global electronics supply chains—sourcing from factories in China, Malaysia, and Southeast Asia—used migrant worker recruitment practices that created forced labor conditions, including fees of USD 1,000–6,000 paid by workers, contract terms misrepresenting the work, and employer-controlled dormitories with movement restrictions.",
        "source": "ILO, International Framework for Fair Recruitment in Electronics, 2014",
    },

    # ── Additional Inter-American System ───────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACtHR: Case of Persons Deprived of Liberty in Penitentiary Complex of Curado v. Brazil — Forced Prison Labor",
        "summary": "Inter-American Court (2018) provisional measures found Brazil violated the American Convention through use of forced labor by incarcerated persons in Curado Penitentiary without adequate compensation, safety, or alternative, constituting forced labor under Article 6 of the American Convention alongside violations of the right to humane treatment.",
        "source": "IACtHR, Curado Penitentiary v. Brazil, Provisional Measures, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "Americas",
        "title": "IACHR: Indigenous Women and Trafficking in the Americas",
        "summary": "Inter-American Commission on Human Rights (2015) found that indigenous women and girls in the Americas face disproportionate trafficking vulnerability due to land dispossession, extreme poverty, discrimination in the justice system, lack of access to identity documents—preventing access to labor protections—and historical patterns of forced labor imposed on indigenous communities.",
        "source": "IACHR, Violence, Children and Organized Crime, OEA/Ser.L/V/II., 2015",
    },

    # ── Council of Europe Parliamentary Assembly ────────────────────────────────
    {
        "type": "policy_update",
        "jurisdiction": "Europe",
        "title": "Council of Europe Parliamentary Assembly: Seasonal Worker Exploitation",
        "summary": "Council of Europe Parliamentary Assembly Resolution 2230 (2018) called on member states to eliminate loopholes allowing exploitation of seasonal workers, particularly in agriculture and hospitality, including ensuring that seasonal visa schemes contain mandatory minimum wage protections, accommodation standards, and access to labor dispute mechanisms.",
        "source": "CoE PACE, Resolution 2230 on Seasonal Workers, 2018",
    },
    {
        "type": "policy_update",
        "jurisdiction": "Europe",
        "title": "Council of Europe: Lanzarote Convention on Child Trafficking",
        "summary": "Council of Europe Convention on Protection of Children Against Sexual Exploitation (Lanzarote Convention, 2007) requires 35 signatory states to criminalize recruitment of children for trafficking, establish victim protection programs, and include child trafficking in national action plans, with GRETA follow-up reporting on implementation.",
        "source": "CoE, Lanzarote Convention (CETS 201), 2007, GRETA Implementation Reports",
    },

    # ── ECOWAS / West Africa Regional Bodies ──────────────────────────────────
    {
        "type": "policy_update",
        "jurisdiction": "West Africa",
        "title": "ECOWAS: Action Plan Against Trafficking in Persons 2020–2024",
        "summary": "Economic Community of West African States Action Plan Against Trafficking in Persons (2020) identified child trafficking for domestic servitude (confiage system), trafficking for forced agricultural labor in cocoa and cashew supply chains, and trafficking of West African migrants toward North Africa and Europe as priority areas, with cross-border law enforcement cooperation as the key gap.",
        "source": "ECOWAS, Action Plan Against Trafficking in Persons, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "West Africa",
        "title": "ECOWAS Free Movement Protocol: Exploitation of Intra-Regional Migrants",
        "summary": "ECOWAS Commission (2018) assessment found that despite the ECOWAS Free Movement Protocol permitting labor migration across member states without work permit requirements, intra-regional migrants—particularly from Burkina Faso, Mali, and Guinea to Côte d'Ivoire and Ghana—faced exploitation in agriculture and domestic work due to their irregular status under destination-country local law.",
        "source": "ECOWAS Commission, Assessment of Free Movement of Persons, 2018",
    },

    # ── Pacific Regional ───────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "Pacific",
        "title": "Pacific Regional: Seasonal Worker Exploitation in Australia and New Zealand",
        "summary": "UN Special Rapporteur on Migrants (2017) raised concerns about exploitation of Pacific Island seasonal workers under the Australian Seasonal Worker Programme and New Zealand's RSE scheme, including debt bondage through transport and accommodation charges, wage manipulation, and coercive practices enabled by workers' complete dependence on the scheme operator for visa status.",
        "source": "UN SR on Migrants, Note on Pacific Seasonal Worker Schemes, A/HRC/35/25/Add.2, 2017",
    },
    {
        "type": "case_study",
        "jurisdiction": "Pacific",
        "title": "Vanuatu Seasonal Workers: Accommodation Debt Bondage Pattern",
        "summary": "Research documented in ILO and UN reports (2019) found that Ni-Vanuatu seasonal agricultural workers in Australia faced accommodation and transport deductions leaving them with net wages of AUD 2–5 per hour versus the legal minimum of AUD 18.29, constituting debt bondage facilitated by the seasonal worker scheme structure and inadequate labour inspection of remote agricultural worksites.",
        "source": "ILO, Decent Work in Pacific Labour Mobility Schemes, 2019",
    },

    # ── Specific Case Studies from UN Bodies ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "International",
        "title": "UN CMW: Ethiopian Domestic Workers in Lebanon — Systemic Failure",
        "summary": "UN Committee on Migrant Workers (2015) documented through individual communications and state reports that Ethiopian domestic workers in Lebanon faced a systemic pattern: arrival with falsified contracts, employer refusal to pay wages, passport confiscation, inability to access consular assistance, and death—by suicide or homicide—at an estimated rate of one death per day, representing a catastrophic failure of both sending and receiving state protection obligations.",
        "source": "UN CMW, Concluding Observations on Ethiopia, CMW/C/ETH/CO/1, 2015",
    },
    {
        "type": "case_study",
        "jurisdiction": "International",
        "title": "ILO: Nepalese Workers in Qatar World Cup Construction — Mortality and Exploitation",
        "summary": "ILO monitoring (2020–2022) of Qatar World Cup construction sites found that Nepalese workers experienced a combination of wage theft, excessive heat exposure, employer-controlled housing, restricted freedom to change employers, and recruitment fees of USD 500–3,000 that created debt bondage. The Guardian investigation calculated over 6,500 migrant worker deaths since Qatar was awarded the World Cup.",
        "source": "ILO, Monitoring Report on Qatar Labour Market, 2020; The Guardian Investigation, 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "International",
        "title": "GRETA Case Study: Vietnamese Nail Salon Workers in the UK",
        "summary": "GRETA documented (2016–2019) a specific trafficking modality involving Vietnamese nationals brought to the UK to work in nail salons, paying debts of GBP 15,000–30,000 to traffickers, working 60–80 hour weeks with wages withheld against the debt, exposed to chemical hazards, and controlled through threats to families in Vietnam. Identification by UK authorities remained extremely low.",
        "source": "GRETA, Thematic Focus: Vietnam-UK Labour Trafficking in Nail Salons, 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "International",
        "title": "UNODC: Trafficking for Domestic Work — Case Studies from 14 Countries",
        "summary": "UNODC (2012) comparative case study analysis across 14 countries found that domestic work trafficking shared universal patterns: deceptive recruitment, contract substitution upon arrival, passport confiscation, isolation in employer's home, debt bondage, and violence or threat of violence for attempted escape. Legal frameworks excluding domestic workers from labor law were the common enabling factor.",
        "source": "UNODC, Trafficking in Persons to Europe for Sexual or Labour Exploitation, 2012",
    },
    {
        "type": "case_study",
        "jurisdiction": "International",
        "title": "OHCHR: Garment Industry Supply Chain Forced Labor — Bangladesh and Cambodia",
        "summary": "OHCHR (2015) investigation found garment factory supply chains supplying major European and North American retailers contained forced labor indicators: production targets requiring 14–16 hour workdays, deductions for defective goods, restrictions on toilet breaks, locked factory premises during working hours, and violence against workers who complained or organized.",
        "source": "OHCHR, Garment Industry Supply Chain Investigation, 2015",
    },

    # ── Recently Adopted Standards ─────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "International",
        "title": "ILO Violence and Harassment Convention C190 — Migrant Worker Application",
        "summary": "ILO Convention No. 190 on Violence and Harassment in the World of Work (2019), upon entering into force, requires states to protect all workers—regardless of immigration status, including domestic workers and migrant workers—from violence and harassment, including gender-based violence, in all work settings including private households.",
        "source": "ILO, C190, Violence and Harassment Convention, 2019",
    },
    {
        "type": "policy_update",
        "jurisdiction": "International",
        "title": "Global Action Against Trafficking (GLO.ACT) — Multi-Country Findings",
        "summary": "ILO/UNDP Global Action Against Trafficking in Persons and Smuggling of Migrants (GLO.ACT) program (2015–2022) operating across 13 countries found that victim identification was the primary bottleneck in anti-trafficking response, with 90%+ of forced labor victims never officially identified, and that labor inspection systems—rather than criminal justice alone—are the most effective early detection mechanism.",
        "source": "ILO/UNDP, GLO.ACT Multi-Country Assessment, 2022",
    },
    {
        "type": "policy_update",
        "jurisdiction": "International",
        "title": "ILO TRIANGLE in ASEAN: Regional Recruitment Reform Findings",
        "summary": "ILO TRIANGLE in ASEAN program (2019 review) found that fair recruitment pilot programs—shifting fee payment from workers to employers—in Cambodia, Myanmar, and Thailand corridors to Malaysia and Thailand reduced debt bondage incidence by 40–60% among participating recruitment agencies, demonstrating that employer-pays models are operationally feasible and economically viable.",
        "source": "ILO TRIANGLE in ASEAN, Fair Recruitment Pilot Assessment, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UN Secretary-General: Plan of Action Against Trafficking (Updated 2017)",
        "summary": "UN Secretary-General's updated Global Plan of Action against Trafficking in Persons (2017) identified the underfunding of victim support services relative to law enforcement as a critical imbalance, with states globally spending an estimated 20 times more on law enforcement responses to trafficking than on victim identification, protection, and rehabilitation.",
        "source": "UN Secretary-General, A/72/290, Global Plan of Action to Combat Trafficking, 2017",
    },

    # ── Overlapping Themes and Intersectional Issues ───────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Intersectionality of Race, Gender, and Migration Status",
        "summary": "UN Special Rapporteur on Trafficking (2018) thematic report on intersectionality found that women of color from developing countries in low-wage migration corridors face compounded vulnerability to trafficking due to intersecting discrimination across immigration status, gender, race, and class, and that anti-trafficking responses must be disaggregated by these intersecting categories to be effective.",
        "source": "UN SR on Trafficking, A/73/171, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Contemporary Forms of Slavery: Climate Change and Forced Labor",
        "summary": "UN Special Rapporteur on Contemporary Forms of Slavery (2021) found that climate-induced displacement was creating growing populations of environmental migrants with extreme vulnerability to trafficking and forced labor, particularly in Bangladesh, Pacific Island states, sub-Saharan Africa, and Central America, where climate stress drove migration into channels controlled by traffickers.",
        "source": "UN SR on Contemporary Forms of Slavery, A/HRC/48/30, 2021",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: LGBTQI+ Migrant Workers and Forced Labor Vulnerability",
        "summary": "ILO (2020) thematic report found that LGBTQI+ migrant workers face intersecting vulnerability to forced labor and trafficking: higher rates of family rejection driving migration, discrimination by consular officials deterring complaint filing, exploitation by employers aware of victims' fear of outing in both destination and origin countries, and exclusion from shelter services that are segregated by binary gender.",
        "source": "ILO, LGBTQI+ Workers and Forced Labour, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OHCHR: Disability and Forced Labor Among Migrant Workers",
        "summary": "OHCHR (2019) found that migrant workers who acquire disabilities through occupational accidents—particularly construction and manufacturing workers—face acute vulnerability to abandonment by employers, deportation without compensation, and recruitment into forced begging or other exploitation upon return due to disability combined with lack of social protection.",
        "source": "OHCHR, Disability and Forced Labour, A/HRC/43/26, 2019",
    },

    # ── Specific Legal Instrument Monitoring ──────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "International",
        "title": "Palermo Protocol: 20-Year Review of Implementation",
        "summary": "UN Office on Drugs and Crime 20-year review of the Palermo Protocol (2020) found that while 173 states had criminalized trafficking consistent with the Protocol, only 30–40% had implemented victim identification systems, non-punishment provisions, or meaningful compensation mechanisms, revealing a massive gap between treaty ratification and practical implementation.",
        "source": "UNODC, 20 Years of the Palermo Protocol, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: Fair Recruitment Initiative — Global Standards Development",
        "summary": "ILO Fair Recruitment Initiative (2018) established global consensus on fair recruitment principles: recruitment fees must not be charged to workers; job offers must be transparent and accurate; workers must have access to grievance mechanisms; and states must maintain effective licensing and oversight of private employment agencies, with these standards increasingly incorporated into national law.",
        "source": "ILO, Fair Recruitment Initiative, Global Standards for Fair Recruitment, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO GLP: General Principles and Operational Guidelines for Fair Recruitment",
        "summary": "ILO General Principles and Operational Guidelines for Fair Recruitment (2019), developed with input from governments, employers, and unions, established specific operational standards: workers must receive copies of contracts in a language they understand before departure; deposits for document safekeeping must be refused; and workers must be able to terminate employment without penalty upon providing reasonable notice.",
        "source": "ILO, General Principles and Operational Guidelines for Fair Recruitment, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OHCHR: Corporate Liability for Supply Chain Trafficking",
        "summary": "OHCHR (2020) report on corporate liability found that existing legal frameworks—even in states with mandatory human rights due diligence legislation (France, Germany, Netherlands)—rarely resulted in effective corporate accountability for supply chain trafficking, due to difficulties in proving knowledge of exploitation in distant supply chain tiers and inadequate victim access to home-state legal proceedings.",
        "source": "OHCHR, Corporate Liability and Supply Chain Human Rights Violations, 2020",
    },

    # ── Additional GRETA Country Evaluations ──────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Italy — Mediterranean Trafficking and Agricultural Exploitation",
        "summary": "GRETA evaluation of Italy (2019) found that persons rescued from Mediterranean crossings included trafficking victims—primarily from Nigeria, Eritrea, and sub-Saharan Africa—who were not systematically screened for trafficking before asylum or immigration processing, and that caporalato (illegal gang-master) agricultural labor exploitation remained pervasive in southern Italy with inadequate prosecution.",
        "source": "GRETA, Report on Italy, GRETA(2019)05, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Switzerland — Domestic Worker Trafficking",
        "summary": "GRETA evaluation of Switzerland (2019) found that domestic workers—particularly those brought by diplomatic staff under A/B visa categories—faced trafficking conditions with inadequate access to remedies, and that the NRM for labor trafficking identification was significantly less developed than for sexual exploitation, with victim support services primarily oriented toward sexual exploitation victims.",
        "source": "GRETA, Report on Switzerland, GRETA(2019)14, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Belgium — Migrant Worker Labor Exploitation in Agriculture",
        "summary": "GRETA evaluation of Belgium (2021) found that posting of workers arrangements—where workers from Eastern Europe are technically employed by companies in their home state while working in Belgian agriculture—created legal complexity that traffickers exploited to evade Belgian labor law, with wages and conditions nominally set by origin-country agreements substantially below Belgian minimums.",
        "source": "GRETA, Report on Belgium, GRETA(2021)05, 2021",
    },

    # ── Specific Fact-Based Findings from Treaty Bodies ────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CERD: Anti-Trafficking Policies Must Not Be Racially Discriminatory",
        "summary": "UN CERD Committee (2004) General Recommendation XXXI on prevention of racial discrimination in the administration and functioning of the criminal justice system affirmed that anti-trafficking enforcement must not be implemented in racially discriminatory ways—such as targeting racial minorities for deportation rather than victim protection—which would violate ICERD obligations.",
        "source": "UN CERD, General Recommendation XXXI, 2004",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW: Domestic Workers Must Be Covered by Labor Law",
        "summary": "UN CEDAW Committee (2016) issued a detailed statement affirming that exclusion of domestic workers—a sector dominated by women—from national labor law protections constitutes gender discrimination prohibited under the Convention on the Elimination of All Forms of Discrimination Against Women, and called on states to extend full labor law coverage to the sector.",
        "source": "UN CEDAW, Statement on Domestic Workers, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CMW: Trafficking Victims Retain Rights Under Convention",
        "summary": "UN Committee on Migrant Workers (2011) clarified in a General Comment that trafficking victims who are migrant workers—even those who entered destination states irregularly—retain all rights under the International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families, including the right to wages for work performed, access to courts, and consular protection.",
        "source": "UN CMW, Statement on Rights of Trafficked Migrant Workers, 2011",
    },

    # ── GRETA Thematic Findings ────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Thematic Report: Labour Exploitation in Supply Chains",
        "summary": "GRETA thematic report on labor exploitation (2020) across all Council of Europe member states found that supply chain labor trafficking was significantly more prevalent than criminal prosecution data suggested, that only 8 of 47 member states had enacted supply chain due diligence legislation, and that existing anti-trafficking responses were structurally oriented toward sex trafficking rather than labor trafficking.",
        "source": "GRETA, Thematic Report on Labour Exploitation in Supply Chains, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Thematic Report: Child Trafficking in Europe",
        "summary": "GRETA thematic report on child trafficking (2017) found that children—comprising approximately 23% of identified trafficking victims in Council of Europe states—were disproportionately trafficked for labor exploitation rather than sexual exploitation when boys, and for both when girls, with Roma, unaccompanied migrant children, and children in care systems facing the highest risk.",
        "source": "GRETA, Thematic Report on Child Trafficking in Europe, 2017",
    },

    # ── Additional ILO Committee of Experts Findings ──────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: Forced Labor in Prison Labor Programs",
        "summary": "ILO Committee of Experts observations on multiple states (2010–2020) under Convention No. 29 found that prison labor programs—where incarcerated persons are contracted to private companies without genuine consent, below market wages, and without ability to refuse—may constitute forced labor under C29 when the private employment relationship is not genuinely voluntary.",
        "source": "ILO CEACR, C29 General Observations on Prison Labour, 2010–2020",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C105 Observation: Eritrea Compulsory National Service",
        "summary": "ILO Committee of Experts (2015) issued an observation on Eritrea under Convention No. 105 concerning the National Service program, which required indefinite service of civilians—sometimes for decades—in military and civilian roles at near-zero wages under threat of imprisonment, constituting state-imposed forced labor. Eritrea was a significant source of trafficking victims fleeing this system.",
        "source": "ILO CEACR, C105 Observation, Eritrea, 2015",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: China Prison Labor Export Risk",
        "summary": "ILO Committee of Experts observations on China under Convention No. 29 (2012–2022) noted concerns about the laojiao (re-education through labor) and broader prison labor system's potential intersection with global supply chains, with audit evidence suggesting that goods manufactured by detained persons—including Uyghur workers in Xinjiang—may enter export supply chains without disclosure.",
        "source": "ILO CEACR, C29 Observation, China, 2022",
    },

    # ── Additional Inter-American System Findings ──────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "Americas",
        "title": "IACHR: Caribbean Domestic Workers and Trafficking",
        "summary": "Inter-American Commission on Human Rights (2016) found that domestic worker trafficking within the Caribbean—particularly affecting women from Haiti, Jamaica, and smaller island states—operated through family and community networks rather than formal recruitment agencies, making detection extremely difficult and requiring community-based identification approaches.",
        "source": "IACHR, Trafficking in the Caribbean, OEA/Ser.L/V/II.Doc.64/11, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "Americas",
        "title": "IACHR Rapporteur on Rights of Migrants: Mesoamerican Corridor",
        "summary": "IACHR Rapporteur on Rights of Migrants (2013) comprehensive report on the Mesoamerican migration corridor documented that migrants from Honduras, Guatemala, El Salvador, and Nicaragua transiting through Mexico to the United States faced industrial-scale trafficking by organized criminal groups operating with impunity, with abductions, ransom payments, forced labor, and sexual exploitation occurring at every stage of the journey.",
        "source": "IACHR, Human Rights of Migrants on the Southern Border of Mexico, 2013",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Americas",
        "title": "IACtHR: Trabajadores de la Hacienda Brasil Verde v. Brazil — Landmark Forced Labor",
        "summary": "Inter-American Court (2016) landmark ruling against Brazil on sugar cane plantation slave labor established that debt bondage and geographic isolation together constitute slavery under Article 6 of the American Convention even absent physical restraint, that Brazil's statute of limitations for slavery crimes violates jus cogens norms, and that Brazil must create a national compensation fund for slavery victims.",
        "source": "IACtHR, Trabalhadores da Fazenda Brasil Verde v. Brazil, October 2016",
    },

    # ── Final Thematic Entries ─────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Survivor-Led Approaches to Anti-Trafficking Policy",
        "summary": "UN Special Rapporteur on Trafficking (2019) thematic report advocated for survivor-led approaches to anti-trafficking policy development, finding that policies designed without meaningful survivor input systematically failed to address actual needs of victims, over-prioritized criminal prosecution over victim support, and implemented measures—such as hotel inspections and migration controls—that increased rather than decreased vulnerability.",
        "source": "UN SR on Trafficking, A/74/189, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: Zero Fee Recruitment — Employer-Pays Standard Progress",
        "summary": "ILO (2023) stocktaking of employer-pays recruitment fee commitments found that over 200 major multinational corporations had adopted employer-pays policies in their supplier codes of conduct, but implementation verification remained weak, reimbursement mechanisms for already-paid fees were rare, and sub-tier suppliers—where most workers are recruited—were frequently outside the scope of buyer monitoring.",
        "source": "ILO, Progress on Employer Pays Recruitment, 2023",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OHCHR: National Action Plans on Business and Human Rights — Trafficking Gaps",
        "summary": "OHCHR review of National Action Plans on Business and Human Rights (2020) found that while 25 states had adopted NAPs, fewer than half included specific measures on migrant worker recruitment, labor trafficking in supply chains, or human rights due diligence for high-risk sectors, and that none included binding obligations with enforcement mechanisms.",
        "source": "OHCHR, Review of National Action Plans on Business and Human Rights, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: Regional Standards for Domestic Worker Protection — Asia-Pacific",
        "summary": "ILO (2016) comparative review of domestic worker legislation in Asia-Pacific found that only the Philippines and Hong Kong SAR provided domestic workers with equivalent protections to other workers—minimum wage, maximum hours, paid rest days—while Malaysia, Singapore, Thailand, and GCC states maintained explicit or de facto exclusions, leaving millions of domestic workers without basic labor rights.",
        "source": "ILO, Decent Work for Domestic Workers in Asia and the Pacific, 2016",
    },
    {
        "type": "policy_update",
        "jurisdiction": "International",
        "title": "UN: International Migration Review Forum — Trafficking Commitments 2022",
        "summary": "First International Migration Review Forum (2022), reviewing Global Compact for Migration implementation, found limited progress on Objective 6 (fair recruitment) and Objective 7 (reducing vulnerability to trafficking). States reported insufficient data disaggregation by gender, age, and sector to assess whether national anti-trafficking measures were reaching the most at-risk migrant worker populations.",
        "source": "UN IMRF, Progress Declaration, A/RES/76/266, 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Migrants: Access to Justice for Migrant Workers",
        "summary": "UN Special Rapporteur on Migrants (2021) thematic report on access to justice found that migrant workers—particularly undocumented workers and domestic workers—face structural barriers to judicial remedies including fear of deportation, language barriers, prohibitive legal costs, statute of limitations issues in countries of origin, and the practical impossibility of returning to destination states to pursue civil claims after departure.",
        "source": "UN SR on Migrants, A/76/257, 2021",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OHCHR: Protection Gaps for Migrant Workers in Irregular Status",
        "summary": "OHCHR (2022) comprehensive review found that states systematically fail to protect migrant workers in irregular status—an estimated 50 million persons globally—from forced labor and trafficking, because irregular workers: cannot access labor inspection without risk of deportation; cannot enforce wage claims in courts; cannot access victim support conditioned on legal immigration status; and cannot participate in employer licensing complaints without exposure.",
        "source": "OHCHR, Protection Gaps for Migrants in Irregular Status, A/HRC/49/24, 2022",
    },

    # ── Additional GRETA and CoE Findings ─────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Albania — Source Country for Labor Trafficking to Western Europe",
        "summary": "GRETA evaluation of Albania (2020) found that despite progress in criminalizing trafficking, Albania remained a significant source country for labor trafficking to Western Europe—particularly to Italy, Greece, and Germany—with victims trafficked for domestic work, seasonal agriculture, and cannabis cultivation, and that support services for male victims of labor trafficking were virtually nonexistent.",
        "source": "GRETA, Report on Albania, GRETA(2020)11, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Moldova — Trafficking in the Context of Poverty and Migration",
        "summary": "GRETA evaluation of Moldova (2018) found that poverty and irregular migration to Russia and Western Europe placed Moldovan workers—particularly women and Roma individuals—at acute risk of trafficking, with returning trafficking survivors facing re-trafficking risk due to absence of economic reintegration support and social stigma deterring help-seeking.",
        "source": "GRETA, Report on Moldova, GRETA(2018)9, 2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "Europe",
        "title": "GRETA Report: Turkey — Syrian Refugee Labor Trafficking",
        "summary": "GRETA evaluation of Turkey (2020) noted the intersection of the Syrian refugee crisis and labor trafficking, finding that Syrian children and women—excluded from formal employment without work permits—were trafficked into domestic work, seasonal agriculture, and textile manufacturing, with the state victim identification system failing to reach Arabic-speaking victims.",
        "source": "GRETA, Report on Turkey, GRETA(2020)15, 2020",
    },

    # ── CEACR Additional Observations ─────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: Oman Domestic Worker Exclusions",
        "summary": "ILO Committee of Experts (2018) noted in a direct request to Oman under Convention No. 29 that domestic workers remained excluded from the Labor Law and that Oman's kafala system, combined with the requirement of employer consent for job transfer, created conditions in which domestic worker exploitation could occur without access to legal remedy, and called for inclusive labor law reform.",
        "source": "ILO CEACR, C29 Direct Request, Oman, 2018",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C181 Observation: Thailand Recruitment Agency Oversight",
        "summary": "ILO Committee of Experts (2019) direct request to Thailand under Convention No. 181 noted that the Employment and Job-Seeker Protection Act did not sufficiently regulate informal brokers who operate in border communities facilitating irregular migration to Malaysia, finding that unlicensed sub-agents operated with impunity and collected fees well above the legal maximum without effective enforcement.",
        "source": "ILO CEACR, C181 Direct Request, Thailand, 2019",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: Cambodia Informal Labor Migration Risks",
        "summary": "ILO Committee of Experts (2017) observation on Cambodia under Convention No. 29 expressed concern that informal migration through unofficial border crossings to Thailand—driven by inadequate legal migration channels and excessive fees in the formal system—placed Cambodian workers at acute risk of forced labor in fishing, domestic work, and agriculture without access to official labor dispute mechanisms.",
        "source": "ILO CEACR, C29 Observation, Cambodia, 2017",
    },

    # ── Additional UN Human Rights Council Country Reviews ────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR: Ethiopia Migrant Worker Sending State Obligations",
        "summary": "Ethiopia's Universal Periodic Review (2019) addressed both the country's receiving-state obligations toward internal migrants and its sending-state obligations toward Ethiopians working abroad—particularly the approximately 150,000 women in domestic work in the Middle East annually, many of whom experience exploitation and for whom repatriation support and complaint mechanisms remained grossly underfunded.",
        "source": "UN UPR, A/HRC/WG.6/34/ETH/2, 2019",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "UPR: Vietnam Migrant Worker Recruitment Reforms",
        "summary": "Vietnam's Universal Periodic Review (2019) received recommendations from 28 states on migrant worker recruitment reform, noting that Vietnamese workers in Malaysia, Taiwan, Japan, and the Middle East paid recruitment fees of USD 3,000–10,000 creating debt bondage conditions, and that the state-owned DOLAB system and licensed recruiters both operated without sufficient transparency or accountability.",
        "source": "UN UPR, A/HRC/WG.6/33/VNM/2, 2019",
    },

    # ── Additional Specific Body Findings ─────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW: Migrant Domestic Workers and Access to Courts",
        "summary": "UN CEDAW Committee (2014) expressed concern in multiple concluding observations that migrant domestic workers systematically lack practical access to courts to enforce wage claims, primarily due to: immigration enforcement cooperation between labor and immigration agencies, employers' control over workers' immigration status, the requirement to reside with employers making unauthorized absence a violation, and inadequate legal aid targeting female migrant workers.",
        "source": "UN CEDAW, Concluding Observations (Multiple States), 2012–2014",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CERD: Stateless Persons and Trafficking Vulnerability",
        "summary": "UN CERD Committee (2018) highlighted that stateless persons—including Rohingya, Bidun, and stateless persons in the Dominican Republic—faced compounded vulnerability to trafficking due to absence of identity documents, exclusion from legal employment, inability to access consular protection, and disproportionate targeting by traffickers who exploited their legally invisible status.",
        "source": "UN CERD, Concluding Observations (Multiple States), 2016–2018",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CMW: Social Protection Portability for Migrant Workers",
        "summary": "UN Committee on Migrant Workers (2016) general comment emphasized that lack of social protection portability—preventing migrant workers from accessing pensions, healthcare, and unemployment benefits earned in destination states upon return—constituted a structural incentive for exploitative arrangements in which workers remained in dangerous employment to avoid losing accrued contributions.",
        "source": "UN CMW, General Comment on Social Protection, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Remediation and Compensation for Trafficking Victims",
        "summary": "UN Special Rapporteur on Trafficking (2021) thematic report on remediation found that fewer than 0.2% of identified trafficking victims globally received any financial compensation from their traffickers or from state compensation funds, with legal barriers including: statute of limitations, requirements to identify perpetrators before compensation claims, unavailability of civil suits against trafficking networks, and absence of state compensation funds in 80% of countries.",
        "source": "UN SR on Trafficking, A/76/263, 2021",
    },

    # ── Additional ASEAN / Regional Findings ──────────────────────────────────
    {
        "type": "policy_update",
        "jurisdiction": "ASEAN",
        "title": "ASEAN: Declaration Against Trafficking — 20-Year Review",
        "summary": "ASEAN Declaration Against Trafficking in Persons Particularly Women and Children (2004) 20-year review (2024) found that while ACTIP (2015) improved legal frameworks, implementation disparities between member states remained large, with the absence of a regional victim identification standard leading to grossly inconsistent treatment of victims at ASEAN borders and by immigration officials.",
        "source": "ASEAN SOMTC, 20-Year Review of ACTIP Implementation, 2024",
    },
    {
        "type": "advisory",
        "jurisdiction": "ASEAN",
        "title": "ACMW: Migrant Worker Complaints Mechanisms in ASEAN",
        "summary": "ASEAN Committee on Migrant Workers (2018) assessment found that complaints mechanisms available to migrant workers in ASEAN destination states—Malaysia, Thailand, Singapore—were systematically inaccessible: requiring workers to file complaints in the destination state while present, be represented by licensed lawyers workers cannot afford, and navigate administrative processes in languages workers do not speak.",
        "source": "ASEAN ACMW, Assessment of Complaints Mechanisms for Migrant Workers, 2018",
    },

    # ── Additional African Regional Findings ──────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "Africa",
        "title": "African Commission: Domestic Work in Sub-Saharan Africa",
        "summary": "African Commission on Human and Peoples' Rights (2016) study found that domestic work trafficking within sub-Saharan Africa—including the confiage system in West Africa, child domestic work in East Africa, and placement agency abuse in Southern Africa—was almost entirely invisible to formal anti-trafficking systems, with very few prosecutions despite millions of potentially exploited workers.",
        "source": "African Commission, Study on Domestic Work and Trafficking in Sub-Saharan Africa, 2016",
    },
    {
        "type": "advisory",
        "jurisdiction": "Africa",
        "title": "SADC: Protocol on Gender and Development — Trafficking Provisions",
        "summary": "Southern African Development Community Protocol on Gender and Development (2008) Article 18 requires SADC member states to enact legislation prohibiting trafficking of women and children, establish victim support services, train law enforcement in gender-sensitive victim identification, and cooperate in cross-border trafficking investigations, with the SADC Secretariat monitoring implementation through periodic reporting.",
        "source": "SADC, Protocol on Gender and Development, Article 18, 2008",
    },

    # ── ILO Observation on Specific High-Risk Countries ───────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: North Korea State-Imposed Forced Labor",
        "summary": "ILO Committee of Experts has maintained observations on the Democratic People's Republic of Korea under Convention No. 29 (ratified 2003) documenting state-imposed forced labor in the Kwanliso political prison camps, mandatory labor mobilizations for construction and agricultural production, and the deployment of North Korean workers abroad under state-controlled conditions with wages confiscated by the state.",
        "source": "ILO CEACR, C29 Observation, DPRK, 2015–2022",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C105 Observation: Saudi Arabia Use of Forced Labor for Discipline",
        "summary": "ILO Committee of Experts (2020) observation on Saudi Arabia under Convention No. 105 noted concern about legal provisions allowing courts to impose compulsory labor as punishment for expression of political views and as a disciplinary measure in employment, as such provisions may violate C105's prohibition on forced labor as a means of labor discipline.",
        "source": "ILO CEACR, C105 Observation, Saudi Arabia, 2020",
    },

    # ── Final Mixed Body Findings ──────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "ILO: Migrant Workers Account for 15% of Forced Labor Despite 5% of Workforce",
        "summary": "ILO Global Estimates on Modern Slavery (2022) found that international migrants—representing approximately 5% of the global working-age population—account for approximately 15% of all forced labor victims in the private economy, a three-fold over-representation attributable to recruitment debt, immigration status vulnerability, linguistic barriers, and exclusion from labor law protections in destination states.",
        "source": "ILO, Walk Free, IOM, Global Estimates of Modern Slavery, 2022, Chapter 3",
    },
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "UNODC: Labor Trafficking Vastly Under-Detected Versus Sexual Exploitation",
        "summary": "UNODC Global Report on Trafficking (2020) found that for every 1 labor trafficking victim officially detected, approximately 34 remain undetected, compared to a ratio of approximately 1:4 for sexual exploitation trafficking. This discrepancy reflects structural detection biases: labor trafficking occurs in private and industrial spaces with restricted inspector access, and victims fear immigration enforcement more than sexual exploitation victims.",
        "source": "UNODC, Global Report on Trafficking in Persons, 2020, pp. 64–68",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "ILO: Wage Theft Among Migrant Workers — Scale and Mechanisms",
        "summary": "ILO (2020) systematic review found wage theft—the non-payment or underpayment of earned wages—to be among the most prevalent labor violations affecting migrant workers globally, with surveys in GCC states, Southeast Asia, and Europe finding 30–60% of migrant workers reporting some form of wage manipulation, including late payment, illegal deductions, payment below promised rate, and outright non-payment for final months of employment.",
        "source": "ILO, No Pay, Low Pay or Late Pay: Wage Theft among Migrant Workers, 2020",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OSCE: Trafficking in Persons for Labor Exploitation — Eastern European Workers",
        "summary": "OSCE Special Representative (2015) report on labor trafficking of Eastern European workers within the OSCE area documented that workers from Ukraine, Moldova, Romania, and Bulgaria were systematically exploited in Western European agriculture, construction, and domestic work through fraudulent recruitment agencies promising EU-level wages but delivering sub-minimum pay and employer-controlled housing used as a coercive tool.",
        "source": "OSCE SR, Labour Trafficking of Eastern Europeans, SEC.FR/196/15, 2015",
    },
    {
        "type": "case_study",
        "jurisdiction": "International",
        "title": "GRETA Case Study: Roma Workers Trafficked for Forced Agricultural Labor in EU",
        "summary": "GRETA documented (2018) multiple cases across EU member states—Spain, Italy, France, UK—in which Roma families were trafficked for forced labor in seasonal agriculture through a pattern: recruitment by community insiders, transportation in substandard vehicles, housing in employer-controlled camps, wages withheld against 'transport debts', and coercion through threats to children present in the camps.",
        "source": "GRETA, Cases of Roma Labour Trafficking in Europe, 2018",
    },
    {
        "type": "law",
        "jurisdiction": "International",
        "title": "UN Convention Against Transnational Organized Crime — Trafficking Protocol Application",
        "summary": "UNODC technical guidance (2012) on the Trafficking Protocol to the UN Convention Against Transnational Organized Crime clarified that the Protocol's definition of trafficking includes labor trafficking in agriculture, fishing, domestic work, and manufacturing, and that states must not require proof of movement across borders for internal trafficking cases, clarifying a common misapplication of the Protocol by national courts.",
        "source": "UNODC, Guidance Note on the Trafficking Protocol Application to Labour Cases, 2012",
    },
    {
        "type": "policy_update",
        "jurisdiction": "International",
        "title": "ILO Governing Body: Complaint Under C29 Against Qatar — Resolution",
        "summary": "ILO Governing Body complaint filed against Qatar under Convention No. 29 (2014) by the International Trade Union Confederation resulted in a historic agreement (2017) in which Qatar committed to abolish exit permits, establish a non-discriminatory minimum wage, create a workers' support and insurance fund, and expand labor court access—with the ILO establishing a monitoring presence in Qatar, the first such arrangement for a ratified convention.",
        "source": "ILO Governing Body, GB.329/INS/14, Qatar C29 Complaint Resolution, 2017",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "OHCHR: Anti-Trafficking Policy Must Center Human Rights of Victims",
        "summary": "OHCHR (2014) policy brief affirmed that anti-trafficking measures that prioritize immigration enforcement over victim protection—including practices such as prosecuting trafficking victims for immigration offenses, deporting victims before investigation, or conditioning assistance on cooperation with law enforcement—violate the human rights of trafficking victims and undermine overall anti-trafficking effectiveness by deterring reporting.",
        "source": "OHCHR, Policy Brief: Human Rights in Anti-Trafficking Responses, 2014",
    },

    # ── Final Five: Additional Treaty Body and Rapporteur Findings ────────────
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "SR on Trafficking: Organ Trafficking and Vulnerability of Migrant Workers",
        "summary": "UN Special Rapporteur on Trafficking (2013) noted that impoverished migrant workers and trafficking victims were specifically targeted by organ trafficking networks in Asia, Eastern Europe, and Latin America, with recruiters exploiting debt and poverty to coerce workers into selling kidneys and other organs, and that international standards prohibiting organ trading were poorly enforced against brokers operating across borders.",
        "source": "UN SR on Trafficking, A/HRC/23/48, 2013",
    },
    {
        "type": "advisory",
        "jurisdiction": "International",
        "title": "CEDAW: Women Migrants and Access to Nationality-Based Social Rights",
        "summary": "UN CEDAW Committee (2019) found that women migrant workers are disproportionately excluded from access to nationality-based social rights—including pension contributions, unemployment insurance, and healthcare—in destination states, creating a structural vulnerability in which their continued exploitative employment is the only source of economic survival, and called on states to delink social rights entitlements from citizenship.",
        "source": "UN CEDAW, Concluding Observations (Multiple States on Social Rights Access), 2019",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Europe",
        "title": "ECtHR: J. and Others v. Austria — Supply Chain Trafficking Jurisdiction",
        "summary": "European Court of Human Rights (2017) ruled in J. and Others v. Austria that Austrian courts had jurisdiction over human trafficking offenses committed by Austrian-based companies in their supply chains even where the exploitation occurred abroad, affirming that the European Convention's positive obligations require states to investigate trafficking connected to companies in their jurisdiction regardless of where victims are physically located.",
        "source": "ECtHR, J. and Others v. Austria, Application No. 58216/12, January 2017",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "International",
        "title": "CEACR C29 Observation: Iraq Yazidi Forced Labor Under ISIS",
        "summary": "ILO Committee of Experts (2018) direct request to Iraq under Convention No. 29 noted the mass enslavement and forced labor of Yazidi women and men by ISIS between 2014 and 2017—representing the largest documented instance of chattel slavery since World War II—and called on Iraq to investigate and prosecute all responsible parties and to provide comprehensive rehabilitation and compensation for survivors.",
        "source": "ILO CEACR, C29 Direct Request, Iraq, 2018",
    },
    {
        "type": "statistic",
        "jurisdiction": "International",
        "title": "ILO: Children Comprise 12% of Forced Labor Victims — 3.3 Million Children",
        "summary": "ILO Global Estimates of Modern Slavery (2022) estimated 3.3 million children in forced labor globally, representing approximately 12% of all forced labor victims. Child forced labor is concentrated in agriculture (64%), manufacturing (8%), domestic work (7%), and construction (6%), with child domestic workers particularly invisible to labor inspection and at acute risk of exploitation by individual household employers.",
        "source": "ILO, Walk Free, IOM, Global Estimates of Modern Slavery, 2022, Chapter 5",
    },
]
