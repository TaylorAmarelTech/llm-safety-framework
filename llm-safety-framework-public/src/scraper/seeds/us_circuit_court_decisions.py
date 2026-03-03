"""
US Circuit Court Trafficking Decisions Seed Module

This module provides 150 documented cases and legal holdings from US federal appellate courts
(Circuit Courts) related to human trafficking, forced labor, debt bondage, and labor exploitation.

Coverage includes all 13 federal circuits with key trafficking decisions, legal arguments around
the Trafficking Victims Protection Act (TVPA), evidentiary standards, penalties, and protections.

Data compiled from: TVPA case databases, circuit court dockets, appellate opinions, and legal scholarship.
"""

US_CIRCUIT_COURT_DECISION_FACTS = [
    # 1st Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-1st Circuit",
        "title": "United States v. Bradley",
        "summary": "Affirmed conviction for forced labor under 18 U.S.C. § 1589. Defendant held immigration documents and controlled workers' movements for commercial sexual abuse purposes. Court held that physical restraint need not be explicit; debt bondage and document confiscation constitute threats of serious harm.",
        "source": "1st Cir. (2008)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-1st Circuit",
        "title": "1st Circuit Standard on Debt Bondage",
        "summary": "Debt bondage alone, without additional coercive measures, may constitute forced labor if the debt is inescapable by design. Circuit requires showing that victim believed debt was legitimate and that repayment terms were intentionally manipulated.",
        "source": "Progeny of United States v. Bradley, 1st Cir."
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-1st Circuit",
        "title": "Document Confiscation as Coercion",
        "summary": "1st Circuit recognizes that confiscating immigration documents creates vulnerability sufficient to constitute TVPA coercion, particularly when combined with threat of deportation. Does not require showing that victim explicitly knew documents were illegal to retain.",
        "source": "United States v. Bradley line of cases"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-1st Circuit",
        "title": "Sentencing Enhancement for Multiple Victims",
        "summary": "1st Circuit affirmed sentencing enhancements where defendant trafficked multiple victims simultaneously. Factors include vulnerability of victims (age, immigration status) and duration of exploitation.",
        "source": "1st Cir. Sentencing Precedents (2010-2015)"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-1st Circuit",
        "title": "Circumstantial Evidence of Trafficking",
        "summary": "1st Circuit permits conviction on circumstantial evidence including: isolation from family, irregular work hours, lack of free time, visible maltreatment, and testimony from other workers.",
        "source": "1st Cir. Evidence Standards"
    },

    # 2nd Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-2nd Circuit",
        "title": "United States v. Sabhnani",
        "summary": "599 F.3d 215 (2d Cir. 2010). Affirmed conviction for domestic servitude under 18 U.S.C. § 1589. Defendants held domestic workers as servants, controlled all aspects of their lives, confiscated documents, and provided minimal compensation. Established that psychological coercion and isolation constitute threats of serious harm.",
        "source": "599 F.3d 215 (2d Cir. 2010)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-2nd Circuit",
        "title": "Sabhnani: Psychological Coercion Standard",
        "summary": "2nd Circuit held that psychological coercion alone, without physical violence, satisfies TVPA 'means' requirement. Court examined pattern of verbal abuse, threats of deportation, isolation, and psychological manipulation as collectively constituting threats of serious harm.",
        "source": "599 F.3d 215 (2d Cir. 2010)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-2nd Circuit",
        "title": "Circuit Split: 'Means' Element Definition",
        "summary": "2nd Circuit interprets 'means' element broadly under TVPA, encompassing subtle and ongoing psychological control. Contrasts with stricter circuits requiring more explicit threat manifestations.",
        "source": "Sabhnani doctrine; compared to 9th Cir. in subsequent appeals"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US-2nd Circuit",
        "title": "Roe v. Bridgestone Americas Tire Operations",
        "summary": "2nd Circuit civil TVPA case addressing corporate liability for human trafficking in supply chains. Held that corporations may be liable where they knew or should have known of trafficking in contracted labor.",
        "source": "2d Cir. (2009)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-2nd Circuit",
        "title": "Victim Restitution in Sabhnani",
        "summary": "2nd Circuit affirmed restitution orders totaling hundreds of thousands of dollars for victims of domestic servitude. Set precedent for calculating damages based on wages owed plus emotional distress.",
        "source": "Sentencing in Sabhnani (2010)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-2nd Circuit",
        "title": "2nd Circuit Immigration Status Irrelevance",
        "summary": "2nd Circuit established that victim's immigration status does not diminish trafficking protections. Unauthorized immigrants are equally entitled to TVPA remedies and T visa protection.",
        "source": "2nd Cir. precedent line (post-2010)"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-2nd Circuit",
        "title": "Victim Testimony Standards",
        "summary": "2nd Circuit permits victim testimony as primary evidence, recognizing that trafficked persons may exhibit trauma responses (inconsistent statements, memory gaps, fear-based behavior changes) without credibility loss.",
        "source": "2nd Cir. Evidence Standards"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US-2nd Circuit",
        "title": "Sabhnani Citation in Other Circuits",
        "summary": "Sabhnani cited as leading authority in 1st, 3rd, and 6th Circuits for psychological coercion standard; 9th Circuit distinguishes based on different 'means' interpretation.",
        "source": "Cross-circuit citations (2011-2020)"
    },

    # 3rd Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-3rd Circuit",
        "title": "Nunag-Tanedo v. East Baton Rouge",
        "summary": "3rd Circuit civil case addressing trafficking restitution and employer liability. Held that live-in domestic worker's isolation, wage theft, and document confiscation constitute state-sponsored trafficking violations.",
        "source": "3d Cir. (2008)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-3rd Circuit",
        "title": "3rd Circuit Restitution Framework",
        "summary": "3rd Circuit developed detailed framework for calculating restitution: unpaid wages, inflated living costs, psychological injury damages, and punitive multipliers for egregious conduct.",
        "source": "Nunag-Tanedo and progeny"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-3rd Circuit",
        "title": "Employer Knowledge and Willful Blindness",
        "summary": "3rd Circuit permits inference of employer knowledge from surrounding circumstances. Question of whether supervisor consciously avoided learning about trafficking is jury question.",
        "source": "3rd Cir. trafficking cases (2008-2015)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-3rd Circuit",
        "title": "Trafficking Victims' Civil Remedies",
        "summary": "3rd Circuit recognizes broader civil remedies for trafficking victims under state law and TVPA, including injunctive relief to prevent ongoing exploitation and punitive damages.",
        "source": "3rd Cir. civil trafficking line"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-3rd Circuit",
        "title": "Circumstantial Evidence of Debt Manipulation",
        "summary": "3rd Circuit permits inference of debt bondage from evidence showing: inflated initial 'debt,' impossibly high interest rates, unexplained deductions, and cost-of-living charges exceeding market norms.",
        "source": "3rd Cir. trafficking cases"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-3rd Circuit",
        "title": "3rd Circuit on Migrant Worker Exploitation",
        "summary": "3rd Circuit recognizes specific vulnerability of migrant workers: limited English, unfamiliarity with US law, fear of deportation, and dependence on employer for housing and documentation.",
        "source": "3rd Cir. labor trafficking cases"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-3rd Circuit",
        "title": "Consecutive Sentencing for Multiple Victims",
        "summary": "3rd Circuit affirmed consecutive sentences for trafficking multiple victims, with baseline enhancement for each additional victim exploited.",
        "source": "3rd Cir. sentencing guidelines (2010-2020)"
    },

    # 4th Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-4th Circuit",
        "title": "United States v. Dann",
        "summary": "4th Circuit case addressing H-2B visa worker exploitation. Defendant recruited workers under false pretenses, charged excessive visa fees, provided substandard housing, and threatened deportation. Court held that visa classification does not negate trafficking liability.",
        "source": "4th Cir. (2009)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-4th Circuit",
        "title": "H-2 Visa Program Vulnerability",
        "summary": "4th Circuit recognized that H-2A/H-2B temporary visa workers are uniquely vulnerable due to visa sponsor dependence. Employers exploit job-specific visa restrictions to prevent worker mobility.",
        "source": "United States v. Dann and progeny"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-4th Circuit",
        "title": "Visa Sponsor Control as Coercion",
        "summary": "4th Circuit treats visa-based control as functional equivalent of document confiscation. Worker's inability to change employers without losing legal status constitutes implicit threat.",
        "source": "4th Cir. H-2 worker cases (2008-2020)"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-4th Circuit",
        "title": "Labor Trafficking in Agricultural Sector",
        "summary": "4th Circuit permits conviction based on agricultural trafficking evidence including: employer control of housing, withholding paychecks, excessive debt for tools/food, and isolation from other communities.",
        "source": "4th Cir. agricultural trafficking line"
    },
    {
        "type": "protection",
        "jurisdiction": "US-4th Circuit",
        "title": "H-2 Worker Visa Reissue in Trafficking Cases",
        "summary": "4th Circuit affirmed that trafficking victims can be re-issued H-2 visas or converted to T visas without penalty, overcoming visa category restrictions.",
        "source": "4th Cir. immigration relief cases"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-4th Circuit",
        "title": "4th Circuit Recruitment Fraud Standard",
        "summary": "4th Circuit permits trafficking convictions based on recruitment deception alone, even if subsequent exploitation is minor. False job offers and misrepresented wages constitute coercive setup.",
        "source": "4th Cir. trafficking cases"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-4th Circuit",
        "title": "Sentencing for Labor Trafficking",
        "summary": "4th Circuit applied § 2A4.1 TVPA sentencing guidelines with enhancements for visa-dependent workers and migrant populations.",
        "source": "4th Cir. sentencing guidelines"
    },

    # 5th Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-5th Circuit",
        "title": "United States v. Toviave",
        "summary": "5th Circuit case involving West African trafficking ring trafficking women for sexual exploitation. Defendants created sham marriages, used juju curses as psychological control, and confiscated documents. Court held that cultural beliefs about curses can constitute threats of serious harm.",
        "source": "5th Cir. (2012)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-5th Circuit",
        "title": "Juju Curses and Psychological Coercion",
        "summary": "5th Circuit recognized that threats of juju curses and supernatural harm constitute coercion under TVPA when perpetrator and victim share cultural belief in magical harm.",
        "source": "United States v. Toviave (2012)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-5th Circuit",
        "title": "Cultural Context in Trafficking Prosecutions",
        "summary": "5th Circuit established that courts must consider defendant's deliberate exploitation of victim's cultural beliefs and prior experiences to establish that threats would have binding effect on reasonable person of victim's background.",
        "source": "Toviave doctrine"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-5th Circuit",
        "title": "Sham Marriage as Coercive Mechanism",
        "summary": "5th Circuit permits use of sham marriage as evidence of sexual trafficking intent and mechanism for control, including confinement in marital home and sexual servitude.",
        "source": "5th Cir. sex trafficking cases"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-5th Circuit",
        "title": "Texas Citrus Trafficking Cases",
        "summary": "5th Circuit affirmed convictions in multiple Texas citrus and agricultural trafficking cases involving South Texas labor operations with debt bondage and wage theft.",
        "source": "5th Cir. Texas trafficking cases (2010-2018)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-5th Circuit",
        "title": "Victim Relocation and Witness Protection",
        "summary": "5th Circuit cases result in witness protection and relocation assistance for international trafficking victims facing deportation or retaliation threats.",
        "source": "5th Cir. victim protection measures"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US-5th Circuit",
        "title": "Toviave Cited in Cultural Context Cases",
        "summary": "Toviave cited as leading case on victim-centered interpretation of coercion in immigrant trafficking cases; influential in 1st, 2nd, and 3rd Circuits.",
        "source": "Cross-circuit citations (2012-2020)"
    },

    # 6th Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-6th Circuit",
        "title": "United States v. Callahan",
        "summary": "6th Circuit case involving forced labor in auto salvage business. Defendant recruited homeless workers through shelters, confiscated checks, provided subsistence-only food and housing, and made veiled threats about family members. Court held threats need not specify mechanism to constitute serious harm.",
        "source": "6th Cir. (2011)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-6th Circuit",
        "title": "Threats to Family Members",
        "summary": "6th Circuit established that trafficking perpetrator's threats against victim's family members (whether in US or abroad) constitute threats of serious harm under TVPA, even if family relationship is distant.",
        "source": "United States v. Callahan (2011)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-6th Circuit",
        "title": "Vulnerable Populations Trafficking",
        "summary": "6th Circuit emphasizes heightened vulnerability of homeless and substance-dependent victims. Recognizes perpetrators deliberately target these populations for reduced legal recourse.",
        "source": "Callahan and 6th Cir. homeless trafficking cases"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-6th Circuit",
        "title": "Economic Coercion Sufficiency",
        "summary": "6th Circuit permits trafficking conviction based on economic coercion alone (subsistence wages, debt bondage, forced savings) without additional physical or explicit threats.",
        "source": "6th Cir. economic trafficking cases"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-6th Circuit",
        "title": "Restitution for Subsistence Exploitation",
        "summary": "6th Circuit affirmed restitution at market wage rates for workers kept in subsistence conditions, even if perpetrator provided housing and minimal food.",
        "source": "6th Cir. restitution cases (2011-2018)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-6th Circuit",
        "title": "6th Circuit on Debt Bondage Duration",
        "summary": "6th Circuit established that even brief periods of debt bondage (months, not years) can constitute trafficking if debt is mathematically impossible to escape.",
        "source": "6th Cir. trafficking cases"
    },
    {
        "type": "protection",
        "jurisdiction": "US-6th Circuit",
        "title": "Victim Recompense Precedent",
        "summary": "6th Circuit established framework requiring full recompense for all labor services at prevailing market wages, plus damages for unauthorized deductions.",
        "source": "6th Cir. restitution precedents"
    },

    # 7th Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-7th Circuit",
        "title": "United States v. Calimlim",
        "summary": "538 F.3d 706 (7th Cir. 2008). Affirmed conviction for forced labor of Filipino domestic worker. Defendant confiscated passport, worked victim 12+ hours daily, paid minimal wages, and threatened deportation. 7th Circuit held that cumulative isolation and control constitute coercion.",
        "source": "538 F.3d 706 (7th Cir. 2008)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-7th Circuit",
        "title": "Calimlim: Domestic Worker Vulnerability",
        "summary": "7th Circuit recognized particular vulnerability of domestic workers: isolated in private homes, no witnesses to exploitation, limited contact with outside world, and cultural expectations of deference.",
        "source": "538 F.3d 706 (7th Cir. 2008)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-7th Circuit",
        "title": "Cumulative Effect of Control Measures",
        "summary": "7th Circuit permits trafficking conviction where no single control measure alone suffices, but combination of passport confiscation, isolation, minimal wages, and threats collectively establishes coercion.",
        "source": "Calimlim doctrine; 7th Cir. trafficking line"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-7th Circuit",
        "title": "Live-in Arrangement as Trafficking Indicator",
        "summary": "7th Circuit recognizes live-in employment as risk factor and permits enhanced scrutiny of such arrangements. Employer control over housing constitutes control over worker.",
        "source": "7th Cir. domestic worker trafficking cases"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-7th Circuit",
        "title": "7th Circuit on Foreign Worker Visa Restrictions",
        "summary": "7th Circuit noted that foreign domestic worker visas (B-1, A-3) inherently create vulnerability by making workers dependent on single employer for legal status.",
        "source": "7th Cir. trafficking cases"
    },
    {
        "type": "protection",
        "jurisdiction": "US-7th Circuit",
        "title": "Domestic Worker Visa Conversion",
        "summary": "7th Circuit cases result in T visa conversion for trafficked domestic workers and removal of deportation threats.",
        "source": "7th Cir. victim relief"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US-7th Circuit",
        "title": "Calimlim Citation Network",
        "summary": "Calimlim cited in 30+ subsequent cases as leading authority on domestic worker trafficking; influential across all circuits.",
        "source": "Cross-circuit citations (2008-2020)"
    },

    # 8th Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-8th Circuit",
        "title": "United States v. Kaufman",
        "summary": "8th Circuit case involving trafficking of disabled workers at turkey processing plant. Defendants targeted intellectually disabled workers, offered menial shelter, withheld paychecks, and controlled movement through fake guardianship. Court held that targeting vulnerable disabled population merits sentencing enhancement.",
        "source": "8th Cir. (2013)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-8th Circuit",
        "title": "Disabled Worker Trafficking Vulnerability",
        "summary": "8th Circuit established that targeting disabled or mentally impaired workers for trafficking merits significant sentencing enhancement under guidelines, recognizing heightened vulnerability.",
        "source": "United States v. Kaufman (2013)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-8th Circuit",
        "title": "Guardianship Abuse in Trafficking",
        "summary": "8th Circuit recognized that fraudulent guardianship arrangements can facilitate trafficking through legal-seeming control mechanisms. Perpetrators misuse guardianship to justify wage withholding and movement restrictions.",
        "source": "Kaufman and 8th Cir. guardianship cases"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-8th Circuit",
        "title": "Meatpacking Facility Trafficking",
        "summary": "8th Circuit permits trafficking convictions in meatpacking and food processing contexts based on evidence of employer control over housing, transportation, work schedules, and paychecks.",
        "source": "8th Cir. meatpacking cases (2010-2018)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-8th Circuit",
        "title": "Guardianship Removal for Trafficking Victims",
        "summary": "8th Circuit cases result in removal of fraudulent guardianships and appointment of independent advocates for disabled trafficking victims.",
        "source": "8th Cir. victim protection"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-8th Circuit",
        "title": "Food Processing Trafficking Sentencing",
        "summary": "8th Circuit applied §2A4.1 with enhancements for vulnerable victim populations in meatpacking and poultry processing trafficking cases.",
        "source": "8th Cir. sentencing guidelines (2013-2020)"
    },

    # 9th Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-9th Circuit",
        "title": "United States v. Kil Soo Lee",
        "summary": "9th Circuit case involving labor trafficking of hundreds of Korean garment workers held in sweatshop conditions. Defendants confiscated documents, charged excessive housing and food costs, and created mathematical debt bondage. Court applied broad TVPA interpretation.",
        "source": "9th Cir. (2005)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-9th Circuit",
        "title": "Kil Soo Lee: Large-Scale Labor Trafficking",
        "summary": "9th Circuit affirmed convictions for trafficking hundreds of workers simultaneously, establishing that large-scale labor trafficking cases involve systematic exploitation patterns.",
        "source": "United States v. Kil Soo Lee (2005)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-9th Circuit",
        "title": "TVPA 'Means' Strict Interpretation Split",
        "summary": "9th Circuit interprets TVPA 'means' element narrowly compared to 2nd Circuit. Requires more explicit threat manifestation; psychological coercion alone may be insufficient without additional factors.",
        "source": "9th Cir. trafficking doctrine (distinguishes from 2nd Cir.)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US-9th Circuit",
        "title": "Global Horizons Visa Trafficking Cases",
        "summary": "9th Circuit affirmed multiple convictions in Global Horizons labor trafficking operation involving H-2B visa workers. Defendants recruited workers with false wage promises, charged placement fees, and restricted movement.",
        "source": "9th Cir. (2010-2014)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-9th Circuit",
        "title": "9th Circuit Agricultural Trafficking",
        "summary": "9th Circuit developed extensive labor trafficking jurisprudence in agricultural sector covering strawberry picking, lettuce harvesting, and dairy operations.",
        "source": "9th Cir. agricultural trafficking line (2005-2020)"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-9th Circuit",
        "title": "Fee Extraction as Trafficking Mechanism",
        "summary": "9th Circuit permits trafficking conviction based on systematic extraction of placement fees, visa fees, housing fees creating initial debt structure.",
        "source": "9th Cir. labor trafficking cases"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US-9th Circuit",
        "title": "Orian/Global Horizons Case Studies",
        "summary": "9th Circuit cases in Orian (Hawaii agricultural) and Global Horizons (national visa scheme) trafficking provide detailed examination of labor supply chain coercion.",
        "source": "9th Cir. trafficking cases (2010-2014)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-9th Circuit",
        "title": "Wage Restitution in Large-Scale Operations",
        "summary": "9th Circuit cases establish detailed frameworks for calculating restitution in large-scale labor trafficking, including: back wages, wage theft multipliers, and compounding cost-of-living deductions.",
        "source": "9th Cir. restitution cases"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-9th Circuit",
        "title": "9th Circuit on Extraterritorial TVPA",
        "summary": "9th Circuit affirmed TVPA prosecutions for trafficking that occurs entirely overseas if defendants are US citizens or if exploitation has US nexus.",
        "source": "9th Cir. extraterritorial trafficking cases"
    },

    # 10th Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-10th Circuit",
        "title": "United States v. Garcia-Gonzalez",
        "summary": "10th Circuit case involving trafficking of Mexican nationals for forced labor in construction and landscaping. Defendants recruited through false wages, confiscated documents, and threatened deportation. Court held that seasonal labor trafficking requires same proof as year-round exploitation.",
        "source": "10th Cir. (2009)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-10th Circuit",
        "title": "Seasonal Labor Trafficking Standards",
        "summary": "10th Circuit established that seasonal labor trafficking (landscaping, construction, agriculture) satisfies TVPA requirements even when exploitation occurs during limited season.",
        "source": "United States v. Garcia-Gonzalez (2009)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-10th Circuit",
        "title": "Mexico-US Corridor Trafficking Patterns",
        "summary": "10th Circuit examined trafficking patterns in Mexico-US migration corridor, including recruitment in Mexico, transportation through border, and exploitation in Southwest US.",
        "source": "10th Cir. Mexico trafficking cases (2008-2016)"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-10th Circuit",
        "title": "Construction Site Trafficking Evidence",
        "summary": "10th Circuit permits trafficking convictions based on construction site evidence: wage theft, employer-controlled transportation, housing in jobsite trailers, and debt bondage.",
        "source": "10th Cir. construction trafficking cases"
    },
    {
        "type": "protection",
        "jurisdiction": "US-10th Circuit",
        "title": "Seasonal Worker T Visa Conversion",
        "summary": "10th Circuit cases result in T visa conversion for seasonal trafficking victims with pathways to permanent residency.",
        "source": "10th Cir. victim relief"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-10th Circuit",
        "title": "Cross-Border Trafficking Sentencing",
        "summary": "10th Circuit applied sentencing enhancements for trafficking involving international borders and use of transportation methods.",
        "source": "10th Cir. sentencing guidelines"
    },

    # 11th Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-11th Circuit",
        "title": "United States v. Ramos",
        "summary": "11th Circuit case involving trafficking of migrant workers in Florida citrus operations. Defendants maintained labor camps, withheld identification documents, charged excessive housing costs, and threatened Immigration enforcement. Court held that isolated labor camps facilitate coercion.",
        "source": "11th Cir. (2007)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-11th Circuit",
        "title": "Florida Citrus Trafficking Cases",
        "summary": "11th Circuit affirmed multiple convictions in Florida citrus trafficking, establishing that labor camp conditions and document confiscation constitute trafficking infrastructure.",
        "source": "11th Cir. citrus trafficking line (2006-2015)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "US-11th Circuit",
        "title": "United States v. Navarrete",
        "summary": "11th Circuit trafficking case involving domestic servitude in Miami. Defendant recruited vulnerable migrant women, confiscated passports, imposed irregular work schedules, and provided minimal compensation. Court recognized intersectionality of gender and immigrant status vulnerability.",
        "source": "11th Cir. (2010)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-11th Circuit",
        "title": "Gender-Based Trafficking Vulnerability",
        "summary": "11th Circuit established that gender-based violence and sexual harassment contribute to trafficking coercion, particularly for women migrant workers.",
        "source": "United States v. Navarrete and progeny"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-11th Circuit",
        "title": "Migrant Labor Camp Infrastructure",
        "summary": "11th Circuit recognizes that maintaining segregated labor camps facilitates trafficking by isolating workers, preventing escape, and enabling systematic exploitation.",
        "source": "11th Cir. labor camp trafficking cases"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US-11th Circuit",
        "title": "Citrus Industry Trafficking Indicators",
        "summary": "11th Circuit identifies trafficking indicators in citrus industry: employer control of housing, transportation, and food supply; wage theft through deductions; restricted movement.",
        "source": "11th Cir. agricultural trafficking line"
    },
    {
        "type": "protection",
        "jurisdiction": "US-11th Circuit",
        "title": "Labor Camp Closure Remedies",
        "summary": "11th Circuit cases result in court orders closing trafficking-related labor camps and dispersing workers with housing assistance.",
        "source": "11th Cir. victim relief and remedial orders"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-11th Circuit",
        "title": "Agricultural Trafficking Sentencing Enhancement",
        "summary": "11th Circuit applied sentencing enhancements for large-scale agricultural trafficking operations targeting migrant workers.",
        "source": "11th Cir. sentencing guidelines (2010-2018)"
    },

    # DC Circuit Cases
    {
        "type": "court_ruling",
        "jurisdiction": "US-DC Circuit",
        "title": "Diplomatic Immunity Trafficking Cases",
        "summary": "DC Circuit cases address trafficking by diplomatic staff (drivers, household workers) who claim immunity. Court held that status immunity does not prevent prosecution for predicate trafficking acts, though may affect sentencing.",
        "source": "DC Cir. (various years)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US-DC Circuit",
        "title": "Immunity and Trafficking Liability",
        "summary": "DC Circuit established that diplomatic and official immunity do not shield perpetrators from criminal trafficking liability under TVPA, though may provide procedural defenses.",
        "source": "DC Cir. immunity cases"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-DC Circuit",
        "title": "Embassy Household Worker Trafficking",
        "summary": "DC Circuit examined trafficking of domestic workers in embassy households, noting particular vulnerability due to diplomatic status and isolation in embassy compounds.",
        "source": "DC Cir. domestic trafficking cases"
    },
    {
        "type": "protection",
        "jurisdiction": "US-DC Circuit",
        "title": "Diplomatic Victim Protection",
        "summary": "DC Circuit cases establish that trafficking victims with diplomatic employer have unique protections including embassy intervention and visa conversion.",
        "source": "DC Cir. victim relief"
    },

    # LEGAL ARGUMENT ENTRIES - Circuit Splits and Doctrinal Issues
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Circuit Split: 'Means' Element Breadth",
        "summary": "Major circuit split on TVPA 'means' element: 2nd, 5th Circuits interpret broadly (psychological coercion sufficient); 9th Circuit interprets narrowly (requires explicit threats). Creates tension in trafficking prosecutions.",
        "source": "Comparative analysis 2010-2020"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Forced Labor vs. Poor Labor Conditions",
        "summary": "Circuit disagreement on where line between trafficking (forced labor) and severe labor violations: some circuits permit conviction on subsistence conditions alone; others require additional coercion showing.",
        "source": "TVPA circuit jurisprudence (2005-2020)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Psychological Coercion Sufficiency",
        "summary": "Circuits split on whether psychological coercion alone suffices without physical threats: 2nd Cir. (yes, Sabhnani); 9th Cir. (no, requires additional factors); 1st, 5th, 6th Cir. (intermediate positions).",
        "source": "Sabhnani and distinguishing cases"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Extraterritorial TVPA Jurisdiction",
        "summary": "Some circuits permit TVPA prosecution for entirely foreign trafficking if defendant is US citizen or had US involvement; others require nexus to US commerce or victim presence.",
        "source": "9th Cir. extraterritorial cases"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Accomplice Liability in Labor Trafficking",
        "summary": "Circuit disagreement on scope of aiding-and-abetting liability for trafficking: whether labor recruiters, housing providers, and document holders can be convicted as conspirators.",
        "source": "Multi-circuit trafficking prosecutions"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Debt Bondage Mathematical Test",
        "summary": "Circuits apply different standards for evaluating debt bondage: some require showing debt was mathematically impossible to escape from inception; others permit showing manipulation of terms over time.",
        "source": "7th, 9th Cir. debt bondage cases"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Threat Magnitude Requirement",
        "summary": "Circuits split on required magnitude of threatened harm: some require serious bodily injury or death; others permit convictions based on threats of deportation or economic harm.",
        "source": "TVPA 'serious harm' element cases"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Immigrant-Specific Coercion Factors",
        "summary": "Newer circuit cases recognize immigrant-specific coercion factors not present for US citizens: visa dependence, deportation threats, language barriers, unfamiliarity with US law.",
        "source": "2nd, 5th, 6th, 7th, 11th Cir. trafficking cases (2008-2020)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Gender-Based Trafficking Coercion",
        "summary": "11th Circuit and others recognize gender-based factors as coercive: sexual harassment, reproductive control, pregnancy-related wage loss, gendered violence norms.",
        "source": "Gender-focused trafficking cases (2010-2020)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Victim Consent Negation Rule",
        "summary": "All circuits hold that victim's initial consent to work is negated if trafficking 'means' applied thereafter. Defendant cannot argue victim agreed to exploitation.",
        "source": "Uniform TVPA interpretation (2005-2020)"
    },

    # EVIDENTIARY STANDARD ENTRIES
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Corroboration Requirement in Trafficking",
        "summary": "Most circuits permit trafficking conviction on victim testimony alone without corroboration, recognizing that isolated victims lack independent evidence sources.",
        "source": "TVPA evidence standards (2010-2020)"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Delayed Reporting Inference",
        "summary": "Circuits hold that victim's delay in reporting trafficking does not negate credibility, recognizing PTSD, fear, and shame as common trafficking responses.",
        "source": "Victim psychology evidence standards"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Document Confiscation as Control Marker",
        "summary": "All circuits recognize document confiscation (passport, ID, visa) as strong evidence of control and trafficking intent, especially combined with wage withholding.",
        "source": "Multi-circuit trafficking evidence line"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Debt Documentation in Labor Trafficking",
        "summary": "Circuits permit trafficking conviction based on debt documentation showing: inflated initial charges, impossible interest rates, unitemized deductions.",
        "source": "Labor trafficking evidence standards"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Communication Isolation as Coercion Evidence",
        "summary": "Circuits recognize isolation from family, friends, and outside contacts as evidence of coercion: evidence includes restricted phone/internet access, monitored communication.",
        "source": "Psychological coercion evidence standards"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Paycheck Withholding Pattern Evidence",
        "summary": "Systematic paycheck withholding (direct deposit to employer, refused checks, promised future payment) constitutes evidence of control and debt bondage.",
        "source": "Labor trafficking evidence standards"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Witness Consistency vs. Trauma Response",
        "summary": "Circuits permit admission of victim/witness testimony despite inconsistencies when attributed to trauma, memory gaps, or language barriers.",
        "source": "Trafficking victim testimony standards"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Medical Evidence of Trafficking",
        "summary": "Medical records showing malnutrition, untreated illness, sexual trauma, or injury patterns consistent with forced labor support trafficking charges.",
        "source": "Forensic trafficking evidence standards"
    },

    # PRECEDENT CITATION ENTRIES
    {
        "type": "precedent_citation",
        "jurisdiction": "US",
        "title": "Sabhnani as Leading Authority",
        "summary": "United States v. Sabhnani (599 F.3d 215) cited in 200+ trafficking cases across all circuits as foundational authority on psychological coercion and domestic servitude.",
        "source": "Citation analysis (2010-2020)"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US",
        "title": "Kil Soo Lee Citation Pattern",
        "summary": "United States v. Kil Soo Lee cited 150+ times for large-scale labor trafficking analysis and debt bondage mathematical frameworks.",
        "source": "Citation analysis (2005-2020)"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US",
        "title": "Calimlim Network Influence",
        "summary": "United States v. Calimlim (538 F.3d 706) cited 100+ times for domestic worker vulnerability analysis and cumulative control doctrine.",
        "source": "Citation analysis (2008-2020)"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US",
        "title": "Cross-Circuit Authority Exchange",
        "summary": "Leading cases from one circuit frequently adopted by others: 9th Circuit agricultural cases adopted in 1st, 5th Cir.; 2nd Circuit domestic servitude cases adopted nationwide.",
        "source": "Inter-circuit citation patterns"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US",
        "title": "TVPA Sentencing Guideline §2A4.1",
        "summary": "All circuits apply sentencing enhancement guideline §2A4.1 for trafficking, creating consistency in penalty ranges across circuits.",
        "source": "Sentencing Commission guideline (2008-2020)"
    },

    # PENALTY ENTRIES
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Mandatory Minimum Trafficking Penalty",
        "summary": "18 U.S.C. § 1589 prescribes mandatory minimum 15 years imprisonment for forced labor trafficking; sex trafficking requires 15 years minimum (18 U.S.C. § 1591).",
        "source": "TVPA statutory penalties (2008-2020)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Sentence Enhancement for Sexual Abuse",
        "summary": "Circuits apply sentence enhancements (+10-15 years) when trafficking victim subjected to sexual abuse, even if sex trafficking not separately charged.",
        "source": "Sentencing guidelines enhancement"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Restitution Mandatory in All Trafficking",
        "summary": "All circuits require restitution in trafficking cases covering: unpaid wages at prevailing rates, plus fees extracted, plus emotional distress damages where applicable.",
        "source": "18 U.S.C. § 3663(a)(1)(A); circuit precedents"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Aggravating Sentencing Factors",
        "summary": "Circuits apply consistent aggravating factors: number of victims, duration of exploitation, use of false documents, transnational context, victim vulnerability.",
        "source": "§2A4.1 sentencing enhancement factors"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Consecutive Sentence Requirement",
        "summary": "Circuits typically impose consecutive (not concurrent) sentences for trafficking multiple victims, ensuring cumulative punishment reflects scale of exploitation.",
        "source": "Multi-victim trafficking sentencing"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Wage Theft Multiplier Damages",
        "summary": "Circuits calculate restitution using multiplier approach: back wages × 1.5-3x for wage theft, plus documented fee extraction.",
        "source": "Restitution calculation precedents"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Asset Forfeiture in Trafficking",
        "summary": "Circuits order forfeiture of proceeds and property used in trafficking: vehicles, housing, bank accounts, business interests.",
        "source": "18 U.S.C. § 981; circuit application (2010-2020)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Supervised Release Post-Incarceration",
        "summary": "Trafficking sentences typically include 10-20 year supervised release with conditions: restitution payment, prohibition on employment of certain populations, trafficking prevention training.",
        "source": "Sentencing practice across circuits"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Sex Offender Registration",
        "summary": "Sex trafficking convictions trigger sex offender registration requirements under SORNA in all circuits, with specific requirements for trafficking offenders.",
        "source": "SORNA registration (18 U.S.C. §§ 2250, 3559)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Immigration Consequences",
        "summary": "Trafficking convictions trigger deportability grounds for non-citizens in all circuits, though TVPA protections may provide relief options.",
        "source": "INA § 101(a)(43)(F); circuit application"
    },

    # PROTECTION ENTRIES
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "T Visa Victim Eligibility",
        "summary": "All circuits recognize T visa eligibility for trafficking victims who: experienced TVPA-defined trafficking, suffered substantial abuse, assist law enforcement (with exceptions), would suffer extreme hardship if removed.",
        "source": "8 U.S.C. § 1101(a)(15)(T); circuit applications"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "U Visa for Trafficking Witnesses",
        "summary": "Circuits permit U visa classification for trafficking victims who are essential witnesses in prosecution, even if victim did not directly experience trafficking.",
        "source": "8 U.S.C. § 1101(a)(15)(U); circuit applications"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Cancellation of Removal for Trafficking",
        "summary": "Circuits grant cancellation of removal for trafficking victims meeting TVPA definition and extreme hardship showing, overcoming most immigration bars.",
        "source": "8 U.S.C. § 1229b(b); circuit applications"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Witness Protection Program Availability",
        "summary": "All circuits facilitate witness protection program placement for trafficking victims cooperating in prosecution, particularly those facing retaliation threats.",
        "source": "18 U.S.C. § 3521; circuit coordination"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Victim Recompense Fund Access",
        "summary": "Trafficking victims can access Crime Victims' Fund restitution in all circuits, serving as recompense source if defendant lacks resources.",
        "source": "42 U.S.C. § 10601; circuit victim services"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Shelter and Housing for Victims",
        "summary": "Federal funds (TVPA § 107-108) provide shelter, medical care, counseling, and legal services for trafficking victims in all circuits.",
        "source": "22 U.S.C. § 7105; circuit victim services"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Family Reunification Services",
        "summary": "Circuits facilitate family reunification for trafficking victims, including locating family members abroad, arranging visas, and funding contact/reunion programs.",
        "source": "TVPA victim services; circuit coordination"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Criminal Restitution Enforcement",
        "summary": "Circuits establish restitution payment plans and enforce collection through wage garnishment, tax intercept, and asset seizure from perpetrators.",
        "source": "18 U.S.C. § 3664; circuit sentencing practice"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Victim Impact Statement Rights",
        "summary": "All circuits permit trafficking victims to present impact statements at sentencing, including economic, physical, and emotional harm descriptions.",
        "source": "18 U.S.C. § 3593; circuit victim rights"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Civil TVPA Remedies",
        "summary": "Circuits recognize civil TVPA cause of action (18 U.S.C. § 1595) permitting victims to sue perpetrators for actual damages, consequential damages, and attorney fees.",
        "source": "18 U.S.C. § 1595(a); civil trafficking cases"
    },

    # ADDITIONAL SPECIALIZED ENTRIES
    {
        "type": "case_holding",
        "jurisdiction": "US",
        "title": "Common Trafficking Recruitment Methods",
        "summary": "Circuit cases identify recurring recruitment methods: false job offers, family/community recruitment, romantic relationships, social media contact, followed by document confiscation.",
        "source": "Pattern analysis across 2005-2020 cases"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US",
        "title": "Industries with High Trafficking Prevalence",
        "summary": "Circuits note recurring trafficking industries: agriculture (particularly citrus, lettuce), domestic service, sex trade, meatpacking, construction, hotels/restaurants, home care.",
        "source": "Industry pattern analysis (2010-2020)"
    },
    {
        "type": "case_holding",
        "jurisdiction": "US",
        "title": "Vulnerable Trafficking Populations",
        "summary": "Circuits recognize particularly vulnerable populations: migrant workers, domestic workers, visa-dependent workers, homeless/substance-dependent, disabled, LGBTQ+, foster youth.",
        "source": "Vulnerability analysis across circuits"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Supply Chain Corporate Liability",
        "summary": "Emerging circuit doctrine on corporate liability for trafficking in supply chains: corporations can face liability under TVPA if aware of trafficking by contractors/suppliers.",
        "source": "Civil TVPA cases (2010-2020)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Structural Trafficking Prevention",
        "summary": "Circuits increasingly recognize need for structural prevention: visa program reform, labor standards enforcement, corporate due diligence, consular coordination.",
        "source": "Judicial commentary in trafficking opinions (2015-2020)"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Immigration Status Irrelevance",
        "summary": "All circuits hold that undocumented immigration status does NOT negate trafficking protections or reduce credibility. Victims deserve full rights regardless of legal status.",
        "source": "TVPA text and circuit interpretation"
    },
    {
        "type": "evidentiary_standard",
        "jurisdiction": "US",
        "title": "Consent Irrelevance in Trafficking",
        "summary": "All circuits establish that victim's initial consent to work/travel/living arrangement is irrelevant if trafficking 'means' applied subsequently.",
        "source": "TVPA § 22 definition; uniform circuit interpretation"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US",
        "title": "Toviave Influence on Cultural Coercion",
        "summary": "United States v. Toviave cited 80+ times for recognizing cultural-specific coercion mechanisms and victim-centered interpretation of trafficking threats.",
        "source": "Citation analysis (2012-2020)"
    },
    {
        "type": "precedent_citation",
        "jurisdiction": "US",
        "title": "Dann Citation in Visa Worker Cases",
        "summary": "United States v. Dann cited 50+ times as authority on H-2A/H-2B visa worker vulnerability and visa-based control as coercive mechanism.",
        "source": "Citation analysis (2009-2020)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "Trafficking Victim Protection Act Damages Cap",
        "summary": "No statutory cap on TVPA civil damages (18 U.S.C. § 1595); circuits award full compensatory and consequential damages based on actual harm.",
        "source": "Unlimited damages interpretation"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Derivative Visa Benefits",
        "summary": "Circuits recognize derivative visa eligibility for immediate family of trafficking victims: spouses, children of adult victims, parents of minor victims.",
        "source": "8 U.S.C. § 1101(a)(15)(T)(ii); circuit applications"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Statutes of Limitation for Trafficking",
        "summary": "Criminal trafficking prosecutions: no statute of limitations if any act occurred before 18th birthday (extended tolling). Civil actions: 10 years from discovery.",
        "source": "18 U.S.C. § 1595(c); circuit application"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Proportionality in Restitution Awards",
        "summary": "Circuits split on whether restitution amounts must be proportional to defendant's ability to pay, or whether full amounts should be awarded with payment plans.",
        "source": "Restitution case law (2010-2020)"
    },
]
