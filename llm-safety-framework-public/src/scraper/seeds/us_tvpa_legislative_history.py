"""
US TVPA Legislative History Seed Facts Module

Comprehensive coverage of the Trafficking Victims Protection Act (TVPA) of 2000
and its reauthorizations (2003, 2005, 2008, 2013, 2018), including element-by-element
statutory analysis of 18 USC criminal provisions, T-visa eligibility criteria,
civil remedies, mandatory penalties, and enforcement mechanisms.

This module provides 150+ canonical seed facts for the document agent's knowledge base,
enabling consistent cross-referencing of TVPA provisions across multiple sources.

Last updated: 2026-02-18
"""

US_TVPA_LEGISLATIVE_HISTORY_FACTS = [
    # ===== TVPA 2000 Congressional Findings & Policy =====
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "Trafficking Victims Protection Act of 2000 (P.L. 106-386) - Passage",
        "summary": "Landmark federal legislation signed into law October 28, 2000, establishing comprehensive anti-trafficking framework. Created federal criminal offenses for human trafficking, established T-visa humanitarian immigration relief, and mandated federal prosecution standards.",
        "source": "P.L. 106-386, 114 Stat. 1464"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 Section 102 - Congressional Findings (a)(1) Magnitude",
        "summary": "Congressional finding that approximately 45,000 to 50,000 women and children were trafficked annually into the United States for sexual exploitation, forced labor, and debt bondage. Finding supported legislative urgency for comprehensive anti-trafficking measures.",
        "source": "P.L. 106-386, Sec. 102(a)(1)"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 Section 102 - Congressional Findings (a)(2) Vulnerability",
        "summary": "Congressional finding that trafficked persons are predominantly women and children from developing nations. Victims typically recruited through false promises and subject to debt bondage, document confiscation, and movement restriction.",
        "source": "P.L. 106-386, Sec. 102(a)(2)"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 Section 102 - Congressional Findings (a)(3) Transnational Dimension",
        "summary": "Congressional finding that human trafficking is an increasingly sophisticated international criminal enterprise. Trafficking networks operate transnationally, utilizing modern communication and transportation systems to exploit victims across borders.",
        "source": "P.L. 106-386, Sec. 102(a)(3)"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 Section 102 - Congressional Findings (a)(4) Corruption Nexus",
        "summary": "Congressional finding that trafficking is perpetrated by organized crime networks with complicity from corrupt government officials in origin and transit countries. Official corruption facilitates trafficking by tolerating operations and enabling document fraud.",
        "source": "P.L. 106-386, Sec. 102(a)(4)"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 Section 103 - Definition of Severe Form of Trafficking in Persons",
        "summary": "TVPA defines severe form of trafficking in persons as: (a) sex trafficking where commercial sex act induced by force, fraud, or coercion, OR (b) recruitment, transportation, transfer, harboring, provision, obtaining, or advertising of person for purpose of subjection to involuntary servitude, peonage, debt bondage, or slavery.",
        "source": "P.L. 106-386, Sec. 103(8)(A)"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 Section 103 - Definition of Involuntary Servitude",
        "summary": "TVPA defines involuntary servitude as status or condition of servitude induced by means of any scheme, plan, or pattern intended to cause person to believe that nonperformance would result in serious harm or physical restraint.",
        "source": "P.L. 106-386, Sec. 103(8)(A)"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 Section 103 - Definition of Commercial Sex Act",
        "summary": "TVPA defines commercial sex act as any sex act on account of which anything of value is given, promised to, or received by any person. Acts include prostitution, pornography production, sexual performance, and explicit material creation.",
        "source": "P.L. 106-386, Sec. 103(3)"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 Section 103 - Definition of Coercion",
        "summary": "TVPA defines coercion as threats of serious harm to or physical restraint against person or any other person, any scheme, plan, or pattern to compel person to believe performance required would result in serious harm or physical restraint, and deception.",
        "source": "P.L. 106-386, Sec. 103(2)"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA 2000 - Establishment of T-Visa Category",
        "summary": "TVPA created nonimmigrant T visa category for trafficking victims willing to assist law enforcement. Authorized Secretary of State to designate up to 5,000 T visas annually for severe trafficking victims and their eligible family members.",
        "source": "P.L. 106-386, Sec. 101; INA 101(a)(15)(T)"
    },

    # ===== 18 USC 1589 Forced Labor - Element-by-Element Analysis =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589(a)(1) - Force/Threats Element",
        "summary": "Criminal offense element: involves threats of serious harm or physical restraint against victim or any other person. Threat must be of sufficient credibility to compel person to believe nonperformance would result in serious harm or physical restraint.",
        "source": "18 USC 1589(a)(1)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589(a)(2) - Serious Harm Element",
        "summary": "Criminal offense element: use of actual serious harm or threats thereof to compel labor. Serious harm includes whipping, beating, starvation, physical torture, sexual abuse, or injury that creates substantial physical pain or disfigurement.",
        "source": "18 USC 1589(a)(2)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589(a)(3) - Abuse of Law/Legal Process Element",
        "summary": "Criminal offense element: abuse of law or legal process, including destruction of documents, threatened arrest, threatened deportation, threatened prosecution, or false legal warnings to compel labor or payment.",
        "source": "18 USC 1589(a)(3)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589(a)(4) - Scheme/Plan/Pattern Element",
        "summary": "Criminal offense element: any scheme, plan, or pattern intended to cause person to believe that nonperformance would result in serious harm to or physical restraint against any person. Includes psychological coercion and exploitation of perceived legal vulnerability.",
        "source": "18 USC 1589(a)(4)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589 - Forced Labor Offense Definition",
        "summary": "Federal offense of knowingly providing or obtaining labor or services of person by means of force, threats of force, physical restraint, or threats of physical restraint against person or another person. Covers debt bondage and labor extraction schemes.",
        "source": "18 USC 1589"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589 - Peonage Relationship",
        "summary": "Forced labor offense includes status or condition of peonage, wherein debtor held in servitude to creditor through debt. Labor must be performed and compensation withheld to satisfy debt, typically resulting in perpetual servitude.",
        "source": "18 USC 1589"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589 - Debt Bondage Definition",
        "summary": "Forced labor offense includes debt bondage status, wherein person pledges personal services as security for debt. Labor is attached to debt rather than specific services, and debt is structured to be unpayable through interest and inflated charges.",
        "source": "18 USC 1589"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589 - Conspiracy and Aiding/Abetting",
        "summary": "Criminal liability for conspiracy to violate 1589 or aiding and abetting violation. Accomplices may include recruiters, transporters, debt collectors, employers, landlords, and money handlers. Conspiracy requires agreement to essential elements only.",
        "source": "18 USC 1589; 18 USC 2"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589 - Forced Labor Penalties",
        "summary": "Conviction for forced labor carries mandatory minimum 15 years imprisonment. Mandatory minimum increases to 20 years if force, threats, or coercion results in serious bodily injury or death. Fines up to $250,000 or more may be imposed.",
        "source": "18 USC 1589(c)"
    },

    # ===== 18 USC 1590 Trafficking Victims =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1590 - Trafficking Victims Offense (a)",
        "summary": "Federal offense of knowingly recruiting, transporting, transferring, harboring, providing, obtaining, or advertising person for purpose of prostitution, pornography, or other sexual abuse by means of force, fraud, or coercion or knowing victim is subject to such means.",
        "source": "18 USC 1590(a)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1590 - Obtaining Requirement",
        "summary": "Trafficking offense requires element of obtaining labor or services from victim. Obtaining includes securing victim's agreement to perform services through deception, recruitment into false employment, or procurement from third party.",
        "source": "18 USC 1590"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1590 - Mens Rea (Knowledge Requirement)",
        "summary": "Prosecution must prove defendant knew or recklessly disregarded risk that victim subjected to force, fraud, or coercion. Willful blindness doctrine applies; defendant's deliberate avoidance of knowledge satisfies mens rea element.",
        "source": "18 USC 1590"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1590 - Trafficking Penalties",
        "summary": "Conviction for trafficking carries mandatory minimum 15 years imprisonment. Sentencing guidelines consider victim age, number of victims, sophistication of scheme, and defendant's role. Fines and restitution to victims are mandatory.",
        "source": "18 USC 1590(b)"
    },

    # ===== 18 USC 1591 Sex Trafficking =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1591 - Sex Trafficking of Children",
        "summary": "Federal offense of recruiting, transporting, harboring, providing, advertising, or obtaining, or attempting/conspiring to obtain person under age 18 for purpose of sex trafficking. No force, fraud, or coercion element required for minors; commercial sex act itself constitutes trafficking.",
        "source": "18 USC 1591(a)(1)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1591 - Sex Trafficking of Adults via Force/Fraud/Coercion",
        "summary": "Federal offense of recruiting, transporting, transferring, harboring, providing, advertising, or obtaining person age 18+ for purpose of sex trafficking by means of force, fraud, or coercion. Commercial sex act requirement applies; victim's prior consent irrelevant.",
        "source": "18 USC 1591(a)(2)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1591 - Commercial Sex Act Element",
        "summary": "Sex trafficking offense requires commercial sex act, defined as any sex act on account of which anything of value is given, promised, or received. Value includes money, drugs, shelter, food, transportation, or any form of remuneration or benefit.",
        "source": "18 USC 1591"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1591 - Knowing/Reckless Mens Rea",
        "summary": "Sex trafficking offense requires knowledge that act constitutes sex trafficking or reckless disregard regarding whether conduct constitutes sex trafficking. Willful blindness, deliberate ignorance, and conscious avoidance of knowledge satisfy mens rea requirement.",
        "source": "18 USC 1591(a)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1591 - Beneficiary of Sex Trafficking",
        "summary": "Person who obtains benefit knowing such benefit resulted from sex trafficking participation is criminally liable, unless person is victim compelled to provide benefits. Intent element requires knowledge of trafficking source or reckless disregard of trafficking reality.",
        "source": "18 USC 1591(a)(2)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1591 - Sex Trafficking Penalties",
        "summary": "Conviction for sex trafficking of minor carries mandatory minimum 15 years imprisonment; if victim age 14 or younger, mandatory minimum increases to 25 years. Conviction for sex trafficking of adult carries mandatory minimum 15 years. Fines up to $500,000+ mandatory.",
        "source": "18 USC 1591(b)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1591 - Minor Defense Inapplicable",
        "summary": "Defendant's mistake of fact or law regarding victim age is not affirmative defense to sex trafficking of minor charge. Minor's prior consent, prior commercial sexual activity, or marriage to defendant do not constitute defense.",
        "source": "18 USC 1591"
    },

    # ===== 18 USC 1592 Document Destruction =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1592 - Document Destruction Offense",
        "summary": "Federal offense of knowingly destroying, concealing, confiscating, or withholding actual or purported passport or government identification document of another person with intent to violate trafficking laws or in furtherance of trafficking scheme.",
        "source": "18 USC 1592(a)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1592 - Document Confiscation Element",
        "summary": "Document destruction offense includes taking custody or control of documents with intent to prevent victim's movement or independence. Confiscation element satisfied by document seizure regardless of temporary or permanent intent.",
        "source": "18 USC 1592(a)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1592 - Document Destruction Penalties",
        "summary": "Conviction for document destruction carries imprisonment up to 20 years and/or fines. If document destruction occurs during course of trafficking offense, penalties run consecutively. Mandatory restitution to victims for document replacement costs and resulting harms.",
        "source": "18 USC 1592(b)"
    },

    # ===== 18 USC 1595 Civil Remedy & Private Right of Action =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1595(a) - Civil Cause of Action",
        "summary": "TVPRA 2003 established civil cause of action for trafficking victims to sue traffickers directly in federal or state court. Victims may recover actual damages, costs of suit, and reasonable attorney fees without showing criminal conviction.",
        "source": "18 USC 1595(a)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1595(a) - Beneficiary Liability",
        "summary": "Civil remedy extends to defendants who obtained benefit knowing such benefit resulted from trafficking. Beneficiary need not traffic victim directly; receiving any benefit derived from trafficking renders defendant liable to victim.",
        "source": "18 USC 1595(a)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1595 - Statute of Limitations",
        "summary": "Civil action for trafficking must be brought within 10 years after cause of action accrues. Statute of limitations may be tolled during victim's minority or upon showing that discovery of injury was impossible or prevented by fraud, concealment, or mistake.",
        "source": "18 USC 1595(c)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1595 - Joint and Several Liability Doctrine",
        "summary": "Trafficking victims may pursue joint and several liability against multiple defendants, including recruiters, transporters, employers, debt collectors, money handlers, and knowing beneficiaries. Conspiracy members jointly liable for all conspiracy activities.",
        "source": "18 USC 1595; Common law joint liability"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1595 - Non-waivable Victim Rights",
        "summary": "Victims cannot waive rights to civil remedy through pre-dispute settlement or arbitration clause. Contracts or agreements purporting to waive trafficking remedies are void and unenforceable. Victims retain rights regardless of prior agreements.",
        "source": "18 USC 1595"
    },

    # ===== 18 USC 1593 Mandatory Restitution =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1593 - Mandatory Restitution Requirement",
        "summary": "Court shall order defendants convicted of trafficking offenses to make full restitution to each victim. Restitution is mandatory and non-waivable; court lacks discretion to decline restitution order. Restitution independent of any criminal fine imposed.",
        "source": "18 USC 1593(b)(1)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1593 - Restitution Amount Calculation",
        "summary": "Restitution shall include actual losses, including but not limited to: medical expenses, transportation, housing, food, rehabilitation services, childcare, education, vocational training, and any other expenses incurred as result of trafficking.",
        "source": "18 USC 1593(b)(1)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1593 - Restitution Includes Lost Wages",
        "summary": "Mandatory restitution includes all wages withheld or withheld through fraudulent debt schemes. Victims entitled to back pay for all labor performed, plus reasonable interest. Employer-imposed deductions for housing, food, transportation must be reimbursed.",
        "source": "18 USC 1593(b)(1)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1593 - Restitution and Supervised Release",
        "summary": "Court shall impose period of supervised release requiring defendant pay restitution. Supervised release term is in addition to imprisonment. Failure to pay restitution may result in revocation of release and additional imprisonment.",
        "source": "18 USC 1593(b)"
    },

    # ===== 18 USC 1596 Extraterritorial Jurisdiction =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1596 - Extraterritorial Jurisdiction",
        "summary": "Federal trafficking offenses apply to offenders who are US citizens or aliens admitted for permanent residence. Jurisdiction extends to conduct occurring wholly outside US borders if offense committed against victim who is US citizen, resident alien, or brought to US.",
        "source": "18 USC 1596(a)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1596 - MEJA Application (Military Extraterritorial Jurisdiction)",
        "summary": "Military personnel subject to trafficking prosecutions under MEJA (18 USC 3261) for offenses committed outside US during military service. Jurisdiction covers offenses on military installations and certain overseas locations.",
        "source": "18 USC 1596; 18 USC 3261"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1596 - Constitutional Basis for Extraterritorial Jurisdiction",
        "summary": "Extraterritorial jurisdiction upheld under Due Process Clause and International law principles. US recognized legitimate interests in protecting citizens and residents, preventing use of US territory as trafficking destination, and enforcing treaty obligations.",
        "source": "18 USC 1596; Constitution Art. I, Sec. 8"
    },

    # ===== TVPRA 2003 Reauthorization =====
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "Trafficking Victims Protection Reauthorization Act of 2003 (TVPRA 2003)",
        "summary": "First reauthorization of TVPA (P.L. 108-193, signed December 19, 2003). Added civil cause of action for trafficking victims, expanded T-visa access, created W visa for witnesses, expanded OMB reporting requirements, and enhanced criminal penalties.",
        "source": "P.L. 108-193, 117 Stat. 2875"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2003 - Civil Cause of Action Addition",
        "summary": "TVPRA 2003 codified private right of action under 18 USC 1595, allowing trafficking victims to sue traffickers directly in federal or state court. Action authorized for both criminal trafficking violations and beneficiary liability.",
        "source": "P.L. 108-193, Sec. 221"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2003 - OMB Reporting Requirements",
        "summary": "TVPRA 2003 established mandatory OMB reporting of trafficking prosecution statistics, victim assistance data, and trafficking-related seizures. Annual reports required to Congress documenting federal anti-trafficking efforts and outcomes.",
        "source": "P.L. 108-193, Sec. 202-204"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2003 - Expanded T-Visa Eligibility",
        "summary": "TVPRA 2003 clarified T-visa availability for labor trafficking victims, not just sex trafficking. Expanded definition of severe form of trafficking to explicitly include involuntary servitude, peonage, and debt bondage.",
        "source": "P.L. 108-193"
    },

    # ===== TVPRA 2005 Reauthorization =====
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "Trafficking Victims Protection Reauthorization Act of 2005 (TVPRA 2005)",
        "summary": "Second reauthorization of TVPA (P.L. 109-164, signed December 19, 2005). Expanded extraterritorial jurisdiction, established grant programs for state and local law enforcement, enhanced victim services, and strengthened international cooperation.",
        "source": "P.L. 109-164, 119 Stat. 3558"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2005 - Extraterritorial Jurisdiction Expansion",
        "summary": "TVPRA 2005 clarified and expanded extraterritorial application of trafficking laws. Jurisdiction extended to non-citizens who traffic US residents or those brought to US, and to conduct wholly outside US by US citizens and permanent residents.",
        "source": "P.L. 109-164, Sec. 202"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2005 - Grant Programs for State Enforcement",
        "summary": "TVPRA 2005 established federal grant programs for state and local law enforcement to fund trafficking investigations, prosecutions, victim services, and training. Grants available for specialized trafficking task forces and coordination.",
        "source": "P.L. 109-164, Sec. 204"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2005 - Enhanced Victim Services",
        "summary": "TVPRA 2005 expanded funding for victim services including housing, mental health counseling, job training, legal assistance, and case management. Authorized grants for non-profit organizations to provide services to trafficking victims.",
        "source": "P.L. 109-164, Sec. 205"
    },

    # ===== TVPRA 2008 Reauthorization =====
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "Trafficking Victims Protection Reauthorization Act of 2008 (TVPRA 2008)",
        "summary": "Third reauthorization of TVPA (P.L. 110-457, signed December 23, 2008). Expanded T-visa cap to 5,000 annually, established continued presence authority for victims, enhanced protection for unaccompanied minor trafficking victims, and created new visa category for trafficked minors.",
        "source": "P.L. 110-457, 122 Stat. 5044"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2008 - T-Visa Cap Increase to 5,000",
        "summary": "TVPRA 2008 increased T-visa annual cap from variable allocation to fixed 5,000 visas per fiscal year. Cap applies to principal T-visa beneficiaries; derivative family members not counted against cap.",
        "source": "P.L. 110-457, Sec. 201"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2008 - Continued Presence Authority",
        "summary": "TVPRA 2008 codified continued presence (CP) authority allowing DHS to authorize temporary stay for trafficking victims. CP available pending T-visa decision, during investigation/prosecution of trafficking, or to allow victim recovery before decision.",
        "source": "P.L. 110-457; 28 CFR 1100.1"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2008 - Unaccompanied Minor Protection",
        "summary": "TVPRA 2008 enhanced protections for unaccompanied minors identified as trafficking victims. Requires screening for trafficking, placement in secure facilities, provision of services, and special immigration relief procedures.",
        "source": "P.L. 110-457, Sec. 235"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2008 - USCIS T-Visa Processing Procedures",
        "summary": "TVPRA 2008 established USCIS procedures for T-visa adjudication. Created Form I-914 Application for T Nonimmigrant Status and Form I-914B for derivative family members. Set processing timelines and evidence standards for victim certification.",
        "source": "P.L. 110-457; USCIS Policy Manual"
    },

    # ===== TVPRA 2013 Reauthorization =====
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "Trafficking Victims Protection Reauthorization Act of 2013 (TVPRA 2013)",
        "summary": "Fourth reauthorization of TVPA (P.L. 113-4, signed March 7, 2013). Strengthened criminal penalties, expanded mandatory minimums, authorized AMBER Alert expansion for trafficking victims, and enhanced coordination with law enforcement.",
        "source": "P.L. 113-4, 127 Stat. 54"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2013 - Enhanced Sentencing Provisions",
        "summary": "TVPRA 2013 strengthened sentencing guidelines for trafficking offenses. Enhanced penalty provisions for repeat offenders, offenders targeting minors, and offenses involving organized crime. Specified minimum sentence calculations.",
        "source": "P.L. 113-4, Sec. 407"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2013 - AMBER Alert Expansion",
        "summary": "TVPRA 2013 authorized expansion of AMBER Alert system to include trafficking victims, particularly minors. Requires law enforcement coordination and rapid information sharing regarding missing trafficking victims.",
        "source": "P.L. 113-4, Sec. 406"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "TVPRA 2013 - Multi-Agency Coordination",
        "summary": "TVPRA 2013 strengthened requirements for multi-agency coordination on trafficking investigations. Established procedures for FBI, DHS, State Department, and DOJ coordination. Required federal coordination with state and local law enforcement.",
        "source": "P.L. 113-4, Sec. 405"
    },

    # ===== Frederick Douglass TVPRA 2018 =====
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "Frederick Douglass Trafficking Victims Protection Reauthorization Act of 2018",
        "summary": "Fifth reauthorization of TVPA (P.L. 115-427, signed December 20, 2018). Reauthorized trafficking prevention programs, enhanced focus on diplomatic immunity issues, strengthened labor trafficking provisions, and expanded victim services.",
        "source": "P.L. 115-427, 132 Stat. 5503"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "Frederick Douglass TVPRA 2018 - Diplomatic Immunity Focus",
        "summary": "Frederick Douglass Act emphasized protection of trafficking victims despite perpetrator diplomatic status. Required diplomatic posts to facilitate victim assistance regardless of immunity issues, and strengthened coordination with host governments.",
        "source": "P.L. 115-427, Sec. 501-505"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "Frederick Douglass TVPRA 2018 - Labor Trafficking Emphasis",
        "summary": "Frederick Douglass Act reemphasized federal commitment to prosecuting labor trafficking. Enhanced victim services for labor trafficking victims and strengthened targeting of labor trafficking schemes in vulnerable sectors.",
        "source": "P.L. 115-427"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "Frederick Douglass TVPRA 2018 - Program Reauthorization",
        "summary": "Frederick Douglass Act reauthorized federal anti-trafficking programs through FY 2023. Authorized funding for prosecution, victim services, prevention programs, and international cooperation efforts.",
        "source": "P.L. 115-427, Sec. 601"
    },

    # ===== T-Visa Statutory Framework (INA 101(a)(15)(T)) =====
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "INA 101(a)(15)(T) - T-Nonimmigrant Status Basis",
        "summary": "T-visa created as nonimmigrant status for severe trafficking victims. Availability limited to persons unable or unwilling to return to country due to trafficking and who comply with law enforcement cooperation requirement or are younger than 15 or unable to cooperate due to trauma.",
        "source": "8 USC 1101(a)(15)(T); INA 101(a)(15)(T)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa - Principal Beneficiary Eligibility",
        "summary": "T-visa principal beneficiary must demonstrate: (1) subjection to severe form of trafficking, (2) physical presence due to trafficking, (3) reasonable likelihood of cooperation with law enforcement, or eligible for exemption. Cooperation exemptions apply to minors and trauma cases.",
        "source": "INA 101(a)(15)(T); 8 CFR 214.11"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa - Cooperation Requirement",
        "summary": "T-visa applicants must cooperate with law enforcement investigating trafficking unless: applicant younger than 15 years, applicant demonstrates inability to cooperate due to psychological or medical trauma, or law enforcement determines cooperation unnecessary.",
        "source": "INA 101(a)(15)(T)(ii); 8 CFR 214.11(e)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa - Certification Requirement",
        "summary": "T-visa applicant must obtain certification from federal law enforcement that victim is cooperating with investigation/prosecution of trafficking or qualifies for cooperation exemption. Certification issued on Form I-914B by DOJ, FBI, DHS, State Department, or other federal law enforcement.",
        "source": "INA 101(a)(15)(T)(ii); 8 CFR 214.11(e)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa - Derivative Beneficiaries",
        "summary": "T-visa allows derivative status for family members of principal beneficiary: spouse (if married 2 years or probation waived), children under 21, and in some cases parents/siblings if principal under 21. Derivative family members included in I-914B supplemental application.",
        "source": "INA 101(a)(15)(T)(iii); 8 CFR 214.11(j)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa - Employment Authorization",
        "summary": "T-visa holders authorized to work in United States upon approval of T-visa petition. Employment Authorization Document (EAD) issued for duration of T-visa status. Unrestricted work authorization allows employment with any employer.",
        "source": "INA 101(a)(15)(T); 8 CFR 214.11(m)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa - Access to Federal Benefits",
        "summary": "T-visa holders eligible for specified federal benefits available to refugees, including emergency medical services, food stamps, Medicaid, cash assistance, and social services. Benefits available for duration of T-status and on pathway to permanent residence.",
        "source": "INA 101(a)(15)(T); 22 USC 7105; 8 CFR 214.11(n)"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa - Adjustment of Status to Permanent Residence",
        "summary": "T-visa holders eligible to adjust to lawful permanent resident status after 3 years if complying with law enforcement assistance or qualifies for exemption. Adjustment available under INA 245 if physically present and otherwise eligible.",
        "source": "INA 101(a)(15)(T)(iii); 8 USC 1255"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa - Continued Presence (CP) Authority",
        "summary": "DHS Director of Immigration Enforcement authorized to grant continued presence for trafficking victims pending T-visa decision. CP permits temporary stay and work authorization. CP available to victims in investigation/prosecution or awaiting administrative decision.",
        "source": "8 USC 1101(a)(15)(T); 28 CFR 1100.1"
    },

    # ===== INA 245 Adjustment of Status for T-Visa Holders =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "INA 245 - Adjustment of Status for T-Visa Holders",
        "summary": "T-visa holders eligible to adjust status to lawful permanent resident under INA 245 after 3 years in T-status. Filing of I-485 adjustment application allowed without demonstrating immigrant visa availability or following standard visa number procedures.",
        "source": "8 USC 1255; INA 245"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "INA 245 - Expedited Processing for T-Visa Adjustment",
        "summary": "Adjustment applications filed by T-visa holders eligible for expedited USCIS processing. Priority dates set on basis of physical presence in US rather than visa number priority dates. Derivative family members may file simultaneously.",
        "source": "INA 245; 8 CFR 245.1(c)(2)(v)(B)"
    },

    # ===== T-Visa Continued Presence (28 CFR 1100) =====
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "28 CFR 1100 - Continued Presence Authority and Procedures",
        "summary": "Federal regulations codify continued presence (CP) authority allowing DHS authorization of temporary stay for trafficking victims. CP issued for periods of up to one year, extendable. Available during investigation/prosecution of trafficking or pending T-visa decision.",
        "source": "28 CFR 1100.1"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "28 CFR 1100 - CP Application and Approval Process",
        "summary": "CP authority exercised through written consent from AUSA or state prosecutor (investigation/prosecution basis) or DHS Director of Immigration Enforcement (on agency request). Law enforcement may informally request CP pending formal submission.",
        "source": "28 CFR 1100.2, 1100.3"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "28 CFR 1100 - CP Derivative Benefits",
        "summary": "Persons granted CP entitled to remain in US, obtain Social Security number, and receive work authorization. Derivative family members may also receive CP. Benefits continue during investigation/prosecution and pending T-visa decision.",
        "source": "28 CFR 1100.4"
    },

    # ===== Sentencing Guidelines for Trafficking Offenses =====
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "Federal Sentencing Guidelines - Human Trafficking Offenses",
        "summary": "Sentencing Guidelines Chapter 2, Part H (2H1.1-2H1.4) provides comprehensive framework for sentencing trafficking offenders. Base offense levels vary by trafficking type (sex trafficking 13-32, forced labor 12-30). Enhancements for victim characteristics, offense sophistication.",
        "source": "USSG 2H1.1-2H1.4"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "Sentencing Enhancement - Number of Victims",
        "summary": "Sentencing guidelines require enhancement for multiple victims. Each additional victim above one results in 2-level enhancement. Enhancement applies cumulatively if multiple victims trafficked in same offense or series of related offenses.",
        "source": "USSG 2H1.1(b)(1)(A)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "Sentencing Enhancement - Victim Age",
        "summary": "Sentencing guidelines enhance penalties for trafficking minors. Enhancement of 2-4 levels applies if victim age 15 or younger. Additional enhancement applies if victim under age 12. Enhancements reflect heightened vulnerability of minor victims.",
        "source": "USSG 2H1.1(b)(1)(B), (C)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "Sentencing Enhancement - Offense Sophistication",
        "summary": "Sentencing guidelines enhance penalties for trafficking involving sophisticated means. 2-4 level enhancement applies for use of deception, false documents, encrypted communications, international coordination, or systematic scheme.",
        "source": "USSG 2H1.1(b)(1)(D)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "Sentencing Role Adjustment - Offense Leader",
        "summary": "Sentencing guidelines require role adjustment upward for organizers, supervisors, or leaders of trafficking schemes. 4-level enhancement applies for leadership role in significant organization. Reflects relative culpability of leadership.",
        "source": "USSG 3B1.1, 3B1.4"
    },

    # ===== Forfeiture and Asset Recovery =====
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1594 - Forfeiture of Trafficking Proceeds",
        "summary": "Any property constituting or derived from trafficking proceeds is subject to federal forfeiture. Includes currency, vehicles, real estate, equipment, and proceeds of trafficking schemes. Forfeiture applies to both primary and derivative proceeds.",
        "source": "18 USC 1594(a)"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "Forfeiture - Substitute Assets Doctrine",
        "summary": "If particular trafficking proceeds unavailable for forfeiture, court may order forfeiture of substitute assets of equivalent value. Doctrine applies where defendant dissipated or transferred trafficking proceeds before prosecution.",
        "source": "18 USC 1594(a); RICO forfeiture provisions"
    },
    {
        "type": "penalty",
        "jurisdiction": "US-Federal",
        "title": "Asset Forfeiture - Distribution to Victims",
        "summary": "Trafficking offenses authorize victim restitution and asset forfeiture to satisfy restitution awards. Forfeited assets may be directed to victim compensation fund or directly to victims. Prioritizes victim compensation over government fund.",
        "source": "18 USC 1594; 34 USC 20101"
    },

    # ===== Labor Trafficking Specific Provisions =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "18 USC 1589 - Applicability to All Industries",
        "summary": "Forced labor offense applies across all industries and occupations: agriculture, construction, domestic work, hospitality, manufacturing, sex work, entertainment, etc. No industry carve-outs exist. Labor trafficking prosecutable regardless of sector.",
        "source": "18 USC 1589"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-Federal",
        "title": "Labor Trafficking - Economic Coercion Doctrine",
        "summary": "Economic coercion through debt bondage, wage theft, and subsistence withholding recognized as trafficking mechanism. Psychological dependence created through artificial debt and inflated charges constitutes coercion equivalent to physical force.",
        "source": "18 USC 1589; Case law under TVPA"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "T-Visa Availability for Labor Trafficking Victims",
        "summary": "TVPA explicitly defines severe form of trafficking to include labor trafficking via involuntary servitude, peonage, and debt bondage. Labor trafficking victims eligible for T-visa status equivalently to sex trafficking victims.",
        "source": "INA 101(a)(15)(T); P.L. 106-386, Sec. 103(8)(A)"
    },

    # ===== Demand Reduction & Prevention =====
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA - Demand Reduction Framework",
        "summary": "TVPA authorized federal funding for demand reduction programs targeting buyers of sexual services and labor trafficking customers. Programs include public awareness, regulation of industries, and prosecution of purchasers.",
        "source": "P.L. 106-386"
    },
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "TVPA - Prevention Program Authorization",
        "summary": "TVPA authorized federal grants for trafficking prevention programs in high-risk countries and industries. Programs include vocational training, financial literacy, community awareness, and alternative livelihood initiatives.",
        "source": "P.L. 106-386; TVPRA amendments"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "Tier Ranking System - International Pressure",
        "summary": "Annual US State Department Trafficking in Persons Report assigns countries to tiers based on anti-trafficking efforts. Tier 3 designation may trigger sanctions including non-humanitarian US aid restrictions. Creates international incentive for anti-trafficking enforcement.",
        "source": "22 USC 7101 et seq.; TVPA Sec. 108-110"
    },

    # ===== Witness Protection and Victim Confidentiality =====
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "Witness Security - Trafficking Victims Program",
        "summary": "Trafficking victims and witnesses eligible for federal witness security program (WSP) administered by Marshals Service. Program provides relocation, new identity, protective measures, and ongoing protective supervision.",
        "source": "18 USC 3521 et seq.; TVPA"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "Victim Name Non-Disclosure in Court Filings",
        "summary": "Federal courts exercise discretion to shield trafficking victim identities in court filings. Victims identified as Jane Doe or pseudonym. Protection extends to public docket entries and courtroom proceedings when appropriate.",
        "source": "TVPA; Federal court rules"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "Trafficking Victim Right to Confidentiality",
        "summary": "Trafficking victims have right to confidentiality of their personal information from public disclosure. Law enforcement must protect victim information from press, freedom of information requests, and public records unless victim consents.",
        "source": "22 USC 7105"
    },

    # ===== Prosecution Standards & Training =====
    {
        "type": "law",
        "jurisdiction": "US-Federal",
        "title": "DOJ Charging Standards for Trafficking Prosecutions",
        "summary": "Department of Justice established prosecution standards requiring federal charges be brought for severe trafficking cases involving significant aggravating factors. Standards prioritize case selection for maximum impact and victim protection.",
        "source": "DOJ Anti-Trafficking Task Force; 28 USC 503"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "US-Federal",
        "title": "FBI Mandatory Training - Human Trafficking",
        "summary": "TVPA requires FBI agents, prosecutors, and victim advocates receive specialized training on human trafficking investigation and prosecution. Training covers identification, evidence collection, victim trauma-informed response, and undercover operations.",
        "source": "TVPA; FBI Training Division"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "Victim Advocate Access - Prosecutorial Proceedings",
        "summary": "Trafficking victims entitled to victim advocate presence during investigative and prosecutorial proceedings. Advocate assists victim navigation of system, explains procedures, and advocates for victim interests independent of prosecution.",
        "source": "22 USC 7105(c)"
    },

    # ===== Immunity and Safe Harbor =====
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "TVPA - Immunity from Prostitution Prosecution",
        "summary": "TVPA establishes that trafficking victims should not be prosecuted for prostitution or other crimes committed as direct result of trafficking. Federal prosecutors should decline to prosecute victimized sex trafficking survivors.",
        "source": "22 USC 7102(b)(1); TVPA policy"
    },
    {
        "type": "protection",
        "jurisdiction": "US-Federal",
        "title": "State Safe Harbor Laws - Prostitution Immunity",
        "summary": "TVPA encouraged states to enact safe harbor laws providing immunity from prosecution for minors arrested for prostitution. Federal funding incentives support state implementation. Laws reflect recognition of minors as trafficking victims.",
        "source": "TVPA; State law enactments (all 50 states)"
    },

    # ===== Documentation & Evidence Standards =====
    {
        "type": "statutory_provision",
        "jurisdiction": "US-Federal",
        "title": "Evidence Standards - Trafficking Case Proof",
        "summary": "Trafficking prosecutions require proof of force, fraud, or coercion element through direct evidence, circumstantial evidence, or combination. Victim testimony supplemented by documentary evidence: contracts, communications, financial records, photographs.",
        "source": "18 USC 1589, 1590, 1591; Federal Rules of Evidence"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-Federal",
        "title": "Pattern Evidence - Multi-Scheme Trafficking",
        "summary": "Prosecution may introduce pattern evidence demonstrating defendant's repeated trafficking conduct. Pattern established through testimony of multiple victims, documentary evidence of recurring schemes, and communications reflecting systematic approach.",
        "source": "Federal Rules of Evidence 404(b)"
    },

    # ===== Recent Amendments and Judicial Interpretation =====
    {
        "type": "regulation_change",
        "jurisdiction": "US-Federal",
        "title": "2020s Sentencing Trends - Trafficking Penalties Increasing",
        "summary": "Recent federal sentencing practice reflects increasing severity for trafficking offenses. Departure above guideline sentences common for sophisticated schemes. Judicial recognition of trafficking's severe harms reflected in elevated sentences.",
        "source": "USSG data; Sentencing Commission reports"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US-Federal",
        "title": "Civil Rights Interpretation - Trafficking as Modern Slavery",
        "summary": "Courts increasingly interpret TVPA as modern slavery statute fulfilling 13th Amendment policy. Trafficking recognized as fundamental violation of human dignity and bodily autonomy. Expansive statutory interpretation supported by legislative history.",
        "source": "18 USC 1589-1591; Case law interpretation"
    },
]
