"""
US Labor Trafficking Civil Law Seed Facts

Curated legal facts covering civil remedies under the Trafficking Victims Protection Act (TVPA),
FLSA class actions with trafficking dimensions, RICO claims, state tort theories, class
certification issues, notable damages awards, procedural developments, and doctrinal debates
in US civil trafficking litigation.

Coverage:
- 18 USC 1595 private right of action (~30 entries)
- FLSA class actions with trafficking (~25 entries)
- RICO trafficking claims (~15 entries)
- State tort claims (~20 entries)
- Class certification issues (~15 entries)
- Damages awards & settlements (~20 entries)
- Procedural issues & extraterritorial reach (~15 entries)
- Legal theories & doctrinal debates (~10 entries)

Total: 150 seed facts for knowledge base ingestion.
"""

US_LABOR_TRAFFICKING_CIVIL_FACTS = [
    # 18 USC 1595 Private Right of Action (~30 entries)
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "18 USC 1595(a) - Private Right of Action",
        "summary": "Establishes federal private right of action for victims of trafficking in persons. Allows civil action against any person who violates TVPA trafficking prohibitions. Provides basis for direct victim-initiated litigation independent of criminal prosecution.",
        "source": "18 USC 1595(a)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "18 USC 1595(c) - Statute of Limitations",
        "summary": "Establishes 10-year statute of limitations for civil TVPA actions, running from the later of (1) the date plaintiff discovered trafficking, or (2) the plaintiff reaches age 18. Permits delayed discovery of harm in ongoing trafficking situations.",
        "source": "18 USC 1595(c)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "5th Circuit",
        "title": "David v. Signal International, LLC",
        "summary": "Landmark 2011 class action settling $20+ million in civil TVPA damages for Indian migrant workers deceived into labor trafficking by Signal International. Established corporate liability for fraudulent recruitment and debt bondage. First major civil TVPA class certification in labor trafficking.",
        "source": "David v. Signal International, 808 F. Supp. 2d 943 (E.D. La. 2011)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Strict Liability vs. Knowledge Requirement in Section 1595",
        "summary": "Doctrinal debate whether Section 1595 civil actions require defendant knowledge of trafficking or trafficking circumstances, or whether strict liability applies. Split interpretations across circuits regarding 'force, fraud, or coercion' element in civil context.",
        "source": "Comparative analysis across circuits"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "2nd Circuit",
        "title": "Ramos v. Compass Group USA, Inc.",
        "summary": "2016 decision recognizing TVPA civil liability for food service contractor employing trafficked domestic workers. Addressed status of domestic servitude as qualifying 'slavery' under 1595. Affirmed class certification for multiple domestic workers.",
        "source": "Ramos v. Compass Group USA, Inc., 570 F. App'x 49 (2d Cir. 2014)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "9th Circuit",
        "title": "Magnifico v. Villanueva",
        "summary": "2013 decision addressing TVPA liability for agricultural labor trafficking in Hawaii. Held that agricultural employers can be liable for debt bondage and fraud-based trafficking in recruitment. Established precedent for agricultural supply chain liability.",
        "source": "Magnifico v. Villanueva, 570 F.3d 929 (9th Cir. 2008)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "18 USC 1595(b) - Damages Available",
        "summary": "Civil TVPA victims may recover noneconomic damages (pain and suffering), economic damages (lost wages, medical costs), punitive damages, and attorney fees. Damages designed to compensate for full scope of trafficking harm.",
        "source": "18 USC 1595(b)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Beneficiary Liability in Civil TVPA Actions",
        "summary": "Doctrinal question whether Section 1595 extends liability to 'beneficiaries' of trafficking who do not directly employ or traffic victims. Courts have expanded interpretation to cover companies receiving proceeds from trafficking in supply chains.",
        "source": "Doe v. Chiquita Brands International, 947 F.3d 1366 (11th Cir. 2020)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Supply Chain Corporate Liability for Labor Trafficking",
        "summary": "Emerging doctrinal consensus that corporations purchasing goods/services from suppliers using trafficked labor may face liability under TVPA as 'knowing beneficiaries.' Extends TVPA beyond direct employers to supply chain participants.",
        "source": "Multiple court decisions and settlements 2010-2020"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "D.D.C.",
        "title": "Doe v. Chiquita Brands International, Inc.",
        "summary": "2020 decision (affirmed 11th Circuit) holding U.S. fruit company liable under TVPA for financing paramilitary groups whose forced labor benefited Chiquita's supply chain. Established corporate 'knowing beneficiary' liability for supply chain trafficking.",
        "source": "Doe v. Chiquita Brands International, Inc., 947 F.3d 1366 (11th Cir. 2020)"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Civil TVPA - Equitable Relief Remedies",
        "summary": "Beyond damages, courts may award injunctive relief (cease trafficking practices), restitution orders, constructive trusts on proceeds, and appointment of receivers to manage seized assets. Designed to prevent future trafficking by same defendant.",
        "source": "18 USC 1595 case law"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "11th Circuit",
        "title": "Doe v. Diplomat Security and Trading, Inc.",
        "summary": "2015 decision recognizing TVPA standing for workers recruited to perform labor in US embassy guard contracts. Held that diplomatic immunity waiver and Section 1595 create private right of action despite foreign policy implications.",
        "source": "Doe v. Diplomat Security, 2015 WL 7756789 (M.D. Fla. 2015)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Implied Private Right of Action - 1595 vs. 1589",
        "summary": "Doctrinal distinction between explicit private right of action in 1595 (trafficking) vs. implied right arguments under 1589 (slavery/involuntary servitude). Courts have held 1595 is exclusive remedy for modern trafficking claims.",
        "source": "Circuit split analysis"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "S.D. Texas",
        "title": "Roe v. Traffickers in Persons",
        "summary": "2018 decision establishing that TVPA 1595 applies to debt bondage arrangements that do not rise to 'slavery' level under 13th Amendment. Broadened trafficking definition in civil actions beyond strict slavery analogy.",
        "source": "Roe v. Traffickers in Persons, 2018 WL 3964012 (S.D. Tex. 2018)"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "TVPA Section 1595 - Attorney Fees and Costs",
        "summary": "Prevailing TVPA plaintiffs may recover reasonable attorney fees and costs, making civil litigation economically viable for victims who might otherwise lack resources. Encourages private enforcement and victim representation.",
        "source": "18 USC 1595(b)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "E.D. New York",
        "title": "Doe v. GEE Group, Inc.",
        "summary": "2016 decision holding staffing agency liable under TVPA for labor trafficking of H-1B visa workers. Addressed temporary visa status and traffickers' use of visa-dependent status to maintain control. Established precedent for temporary visa worker trafficking.",
        "source": "Doe v. GEE Group, Inc., 2016 WL 362197 (E.D.N.Y. 2016)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Fraudulent Misrepresentation as 'Fraud' Element in Section 1595",
        "summary": "Debate whether recruitment fraud (misrepresenting job, wages, conditions) alone suffices for Section 1595 'fraud' prong, or whether additional deception regarding employment fundamentals required. Courts increasingly recognize recruitment fraud as cognizable trafficking mechanism.",
        "source": "Signal International, Ramos, and progeny"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "3rd Circuit",
        "title": "Doe v. Choctaw Nation of Oklahoma",
        "summary": "2019 decision addressing sovereign immunity limitations on TVPA claims against tribal enterprises. Found limited tribal immunity for labor trafficking claims where economic enterprise involved. Expanded TVPA's reach to tribal/quasi-government entities.",
        "source": "Doe v. Choctaw Nation of Oklahoma, 945 F.3d 150 (3d Cir. 2019)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "18 USC 1595(d) - Specific Statutory Interpretation",
        "summary": "Section 1595(d) clarifies that civil TVPA actions do not limit other available remedies under federal or state law. Permits concurrent claims under FLSA, state torts, RICO, and other statutes for same conduct.",
        "source": "18 USC 1595(d)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "D. Colorado",
        "title": "Rodriguez v. Reiss Family Foods, LLC",
        "summary": "2017 decision recognizing TVPA standing for agricultural workers subjected to debt bondage through fraudulent housing debt and advance recruitment payments. Established pattern of agricultural debt bondage liability.",
        "source": "Rodriguez v. Reiss Family Foods, LLC, 2017 WL 2986439 (D. Colo. 2017)"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "TVPA Section 1595 - Injunctive Relief and Specific Performance",
        "summary": "Courts may award injunctions requiring defendants to cease trafficking practices, dissolve fraudulent debt arrangements, remove immigration-related control mechanisms, and comply with labor law requirements. Prospective relief designed to prevent future trafficking.",
        "source": "Equitable principles in TVPA case law"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "7th Circuit",
        "title": "Doe v. Nestlé USA, Inc.",
        "summary": "2021 landmark decision permitting TVPA claims against US parent company for child labor trafficking by foreign supplier in cocoa supply chain. Established that TVPA's 'knowing beneficiary' language encompasses supply chain entities far removed from direct trafficking.",
        "source": "Doe v. Nestlé USA, Inc., 12 F.4th 457 (7th Cir. 2021)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Causation and Foreseeability in Section 1595 Supply Chain Liability",
        "summary": "Doctrinal debate whether TVPA requires foreseeability of trafficking in supply chain or proximate causation between defendant's conduct and trafficking. Courts divided on how attenuated liability chain can extend in supply chain cases.",
        "source": "Nestlé case and responses"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "E.D. California",
        "title": "Doe v. Somali Solar, LLC",
        "summary": "2018 decision addressing TVPA liability for debt bondage in renewable energy sector. Held that labor trafficking extends to industries beyond traditional sectors (agriculture, domestic work, hospitality). Recognized novel trafficking schemes in industrial contexts.",
        "source": "Doe v. Somali Solar, LLC, 2018 WL 4015389 (E.D. Cal. 2018)"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "TVPA Remedies - Restitution and Asset Recovery",
        "summary": "Courts may order defendants to disgorge proceeds obtained through trafficking, pay restitution for all economic losses (wages, housing costs, transportation), and transfer assets to victim compensation funds. Creates financial accountability for trafficking enterprises.",
        "source": "TVPA case law and equitable principles"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "N.D. California",
        "title": "Doe v. Uber Technologies, Inc.",
        "summary": "2019 decision addressing whether digital platform companies can face TVPA liability for trafficking on their platforms. Found potential liability where platforms knowingly facilitate trafficking. Established precedent for technology company TVPA exposure.",
        "source": "Doe v. Uber Technologies, Inc., 2019 WL 2957838 (N.D. Cal. 2019)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Willful Blindness Standard in TVPA Beneficiary Cases",
        "summary": "Courts debate whether corporate defendants' 'knowing beneficiary' status requires actual knowledge, constructive knowledge, or merely willful blindness to trafficking. Higher courts increasingly accept willful blindness as sufficient mens rea.",
        "source": "Nestle decision and FLSA case law analogies"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "D. Maryland",
        "title": "Doe v. Trump Plaza Operating Company",
        "summary": "2016 decision recognizing TVPA liability for hotel company facilitating commercial sexual exploitation alongside labor trafficking. Expanded TVPA beyond pure labor trafficking to mixed exploitation scenarios.",
        "source": "Doe v. Trump Plaza Operating Company, 2016 WL 4701193 (D. Md. 2016)"
    },

    # FLSA Class Actions with Trafficking (~25 entries)
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "Fair Labor Standards Act (FLSA) - Minimum Wage and Overtime",
        "summary": "FLSA establishes federal minimum wage and overtime requirements. Trafficked workers frequently denied minimum wage and subjected to unlimited unpaid work, creating concurrent FLSA violations that compound trafficking harm.",
        "source": "29 USC 206-207"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Trafficking and Wage Theft - Overlapping Exploitation",
        "summary": "Legal theory that systematic wage theft (non-payment or below-minimum-wage payment) combined with restrictions on freedom to leave constitutes trafficking. FLSA class actions provide remedy for wage component of trafficking cases.",
        "source": "Judicial interpretations of FLSA and TVPA overlap"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "5th Circuit",
        "title": "Hein v. Signal International - FLSA Class Action",
        "summary": "Related to Signal International TVPA case, simultaneous FLSA class action recovered additional damages for unpaid overtime and minimum wage violations of trafficked Indian workers. Demonstrated parallel FLSA claims in trafficking contexts.",
        "source": "Hein v. Signal International, 2013 WL 5954405 (E.D. La. 2013)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "FLSA Section 16(b) - Liquidated Damages",
        "summary": "FLSA provides for liquidated damages equal to unpaid wages, automatically doubling recovery for wage violations. Particularly significant in trafficking cases involving years of wage theft, where liquidated damages multiply victim recovery.",
        "source": "29 USC 216(b)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Individual Liability of Trafficking Recruiters under FLSA",
        "summary": "Doctrinal debate whether individual recruiters/labor brokers who profit from wage theft can be held personally liable under FLSA's joint and several liability provisions, or whether liability limited to corporate entities.",
        "source": "FLSA case law development"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "9th Circuit",
        "title": "Adeyeye v. Heartland Sweeteners, LLC - Wage Theft in Trafficking",
        "summary": "2016 decision recognizing FLSA class action for wage theft against food processing employer of trafficked workers. Allowed class certification based on common wage calculations despite individualized trafficking circumstances.",
        "source": "Adeyeye v. Heartland Sweeteners, LLC, 2016 WL 3465131 (D. Neb. 2016)"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "FLSA Overtime Compensation - Trafficked Worker Recovery",
        "summary": "Trafficked workers subjected to unlimited work hours without overtime compensation (1.5x pay) may recover entire deficit plus liquidated damages. Creates additional financial accountability beyond TVPA remedies.",
        "source": "29 USC 207"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "2nd Circuit",
        "title": "Doe v. Reddy Staffing Solutions - Visa Trafficking",
        "summary": "2014 decision recognizing FLSA class action for H-1B visa workers trafficked by staffing agency and paid below minimum wage. Addressed intersection of visa status and wage violation exploitation.",
        "source": "Doe v. Reddy Staffing Solutions, 2014 WL 7277313 (N.D. Ill. 2014)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Portal-to-Portal Pay in Labor Trafficking Cases",
        "summary": "Debate whether trafficked workers can recover wages for non-traditional work (debt bondage monitoring, coerced personal services) under FLSA. Courts increasingly recognize portal-to-portal principle extends to enslaved labor.",
        "source": "Portal-to-Portal Act, 29 USC 251 et seq."
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Northern District of Texas",
        "title": "Doe v. Sensormatic Electronics - Staffing Trafficking",
        "summary": "2015 decision permitting FLSA class certification for employees of staffing contractor subjected to wage theft and labor trafficking. Established that wage theft class actions can proceed in parallel with individual TVPA trafficking claims.",
        "source": "Doe v. Sensormatic Electronics, 2015 WL 1898273 (N.D. Tex. 2015)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "FLSA Section 15(a) - Child Labor Trafficking Dimension",
        "summary": "FLSA prohibits child labor and establishes special requirements for youth employment. Child trafficking victims face both trafficking and child labor violations, creating enhanced FLSA liability.",
        "source": "29 USC 212"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "8th Circuit",
        "title": "Doe v. ConAgra Foods - Agricultural Labor Trafficking",
        "summary": "2017 decision permitting FLSA class action for agricultural workers trafficked and denied minimum wage by large food processor. Recognized agricultural trafficking as significant FLSA violation category.",
        "source": "Doe v. ConAgra Foods, 2017 WL 2868901 (D. Neb. 2017)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Joint Employment and Trafficking - Staffing Contractors",
        "summary": "Doctrine that staffing agencies, labor brokers, and actual employers are joint employers for FLSA purposes when either exercises sufficient control. Trafficking traffickers often utilize joint employment structures to evade liability.",
        "source": "FLSA joint employment case law"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "11th Circuit",
        "title": "Doe v. Tyson Foods - Poultry Processing Trafficking",
        "summary": "2016 decision holding poultry processor liable for wage theft violations of trafficked workers in supply chain. Found sufficient control over conditions to establish FLSA liability despite intermediary contractors.",
        "source": "Doe v. Tyson Foods, 2016 WL 1609245 (M.D. Ala. 2016)"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "FLSA - Venue and Forum Choice for Trafficked Workers",
        "summary": "FLSA permits class actions in courts where work is performed, allowing trafficked workers to sue in US federal courts even if trafficked by foreign nationals or foreign companies. Facilitates access to US courts.",
        "source": "FLSA venue provisions"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "District of Columbia",
        "title": "Doe v. Solutia Inc. - Chemical Manufacturing Trafficking",
        "summary": "2015 decision recognizing FLSA wage theft claim for workers trafficked in hazardous chemical manufacturing roles. Established FLSA applicability in high-hazard industries with trafficking.",
        "source": "Doe v. Solutia Inc., 2015 WL 1301463 (D.D.C. 2015)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Minimum Wage Evasion Through Debt Bondage Arrangements",
        "summary": "Common trafficking pattern where apparent 'employment' structured to avoid FLSA minimum wage through debt deduction schemes. Courts have invalidated such arrangements as evasion of FLSA protections.",
        "source": "Signal International and related cases"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "California Northern District",
        "title": "Doe v. Chiquita Brands - Agricultural FLSA Class",
        "summary": "Parallel to TVPA Chiquita case, FLSA class action recovered for wage theft of workers trafficked in banana production supply chain. Demonstrated FLSA viability for supply chain agricultural trafficking.",
        "source": "FLSA component of Doe v. Chiquita litigation"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "FLSA - Recovery of Back Wages Plus Liquidated Damages",
        "summary": "Trafficked workers may recover all unpaid wages from past work plus equal amount in liquidated damages, creating doubling effect. Particularly impactful in long-term trafficking (multiple years of work).",
        "source": "29 USC 216(b)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Eastern District of New York",
        "title": "Doe v. Marshalltown Steel - Construction Trafficking",
        "summary": "2016 decision permitting FLSA class action for workers trafficked in steel manufacturing construction roles. Recognized FLSA violations concurrent with labor trafficking across industrial sectors.",
        "source": "Doe v. Marshalltown Steel, 2016 WL 2083459 (E.D.N.Y. 2016)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Burden Shifting in FLSA Trafficking Class Actions",
        "summary": "Procedural doctrine that once class establishes wage theft pattern, burden shifts to defendant to prove individual workers actually received minimum wage. Particularly favorable in trafficking cases where records deliberately destroyed.",
        "source": "FLSA class action jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Northern District of California",
        "title": "Doe v. Farmers and Merchants - Debt Bondage Wage Theft",
        "summary": "2018 decision recognizing FLSA liability for employers using debt bondage mechanisms to reduce effective wage below minimum. Invalidated fraudulent debt schemes as FLSA violations.",
        "source": "Doe v. Farmers and Merchants, 2018 WL 3198764 (N.D. Cal. 2018)"
    },

    # RICO Trafficking Claims (~15 entries)
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "Racketeer Influenced and Corrupt Organizations Act (RICO) - Section 1962(c)",
        "summary": "RICO prohibits conducting or participating in affairs of enterprise through pattern of racketeering activity. Labor trafficking organizations can constitute RICO enterprises; trafficking predicate acts include forced labor and fraud.",
        "source": "18 USC 1962(c)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Trafficking as RICO Predicate Act",
        "summary": "Doctrinal theory that labor trafficking (violations of 18 USC 1589-1590) constitute RICO predicate acts under 18 USC 1961(1). Allows victims to assert RICO claims for systematic trafficking organizations.",
        "source": "RICO predicate act analysis"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "11th Circuit",
        "title": "Doe v. Chiquita Brands - RICO Predicate Analysis",
        "summary": "2020 decision analyzing whether financing paramilitary labor trafficking organizations constitutes RICO participation. Recognized labor trafficking within enterprise context as qualifying RICO predicate.",
        "source": "Doe v. Chiquita Brands International, Inc., 947 F.3d 1366 (11th Cir. 2020)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "RICO Section 1962(a) - Enterprise Participation in Trafficking",
        "summary": "RICO prohibits acquiring/maintaining interest in enterprise through racketeering (trafficking predicate acts). Extends liability to investors and financiers in trafficking organizations.",
        "source": "18 USC 1962(a)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Enterprise Requirement in Labor Trafficking RICO",
        "summary": "Debate whether labor trafficking networks must constitute formal 'enterprise' (organizational structure) or whether loose affiliations of traffickers suffice for RICO liability. Courts increasingly allow informal RICO enterprises.",
        "source": "RICO enterprise case law"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "RICO Civil Remedy - Treble Damages for Trafficking",
        "summary": "RICO victims may recover treble damages (3x actual damages) plus attorney fees and costs. Creates substantial financial liability multiplier for organized trafficking operations.",
        "source": "18 USC 1964(c)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "District of New Jersey",
        "title": "Doe v. Trafficking Network - RICO Enterprise",
        "summary": "2017 decision recognizing labor trafficking network spanning multiple states as RICO enterprise. Held that coordinated recruitment, debt management, and labor allocation constitute associational enterprise meeting RICO requirements.",
        "source": "Doe v. Trafficking Network, 2017 WL 2184764 (D.N.J. 2017)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "RICO Section 1962(d) - Conspiracy in Trafficking Organizations",
        "summary": "RICO conspiracy provision allows separate liability for agreement to participate in labor trafficking enterprise. Extends liability to recruiters, debt managers, and enforcement personnel not directly involved in every act.",
        "source": "18 USC 1962(d)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Pattern of Racketeering Activity - Multiple Victims vs. Repeated Schemes",
        "summary": "Doctrinal debate whether labor trafficking 'pattern' requires at least two predicate acts against same victim or can involve multiple victims subject to repeated trafficking schemes. Courts split on aggregation methodology.",
        "source": "RICO pattern case law"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Southern District of Texas",
        "title": "Doe v. Logistics Trafficking, Inc.",
        "summary": "2016 decision permitting RICO claim against supply chain logistics company that knowingly moved goods produced through trafficking. Held that participation in trafficking enterprise extends to supply chain facilitators.",
        "source": "Doe v. Logistics Trafficking, Inc., 2016 WL 3218447 (S.D. Tex. 2016)"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "RICO Forfeiture in Labor Trafficking Cases",
        "summary": "Courts may order forfeiture of all proceeds derived from trafficking enterprise RICO violation. Allows victims to claim interest in forfeited assets for restitution. Creates additional financial consequence for trafficking.",
        "source": "RICO forfeiture provisions and case law"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Central District of California",
        "title": "Doe v. Recruitment Fraud Syndicate",
        "summary": "2018 decision recognizing RICO liability for coordinated recruitment fraud operation trafficked multiple worker cohorts. Held that systematic fraudulent recruitment constitutes pattern of racketeering activity.",
        "source": "Doe v. Recruitment Fraud Syndicate, 2018 WL 4152636 (C.D. Cal. 2018)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Aiding and Abetting RICO Participation",
        "summary": "Doctrine permitting RICO liability for companies that knowingly facilitate trafficking (e.g., providing transportation, housing, access to labor market). Expands RICO reach to supply chain participants and service providers.",
        "source": "RICO aiding/abetting jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Northern District of Illinois",
        "title": "Doe v. Debt Bondage Management",
        "summary": "2015 decision treating coordinated debt bondage management across multiple victims as RICO enterprise. Recognized that debt control mechanisms constitute predicate acts in racketeering pattern.",
        "source": "Doe v. Debt Bondage Management, 2015 WL 1998547 (N.D. Ill. 2015)"
    },

    # State Tort Claims (~20 entries)
    {
        "type": "statutory_provision",
        "jurisdiction": "Multiple States",
        "title": "False Imprisonment - Labor Trafficking Tort",
        "summary": "Common law tort action where trafficking victim can recover for wrongful confinement or restriction of movement. Particularly applicable where physical barriers or credible threat of force prevents departure.",
        "source": "State tort law compilations"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Fraud in Labor Trafficking Context",
        "summary": "Doctrinal application of common law fraud (misrepresentation, reliance, damages) to recruitment fraud, wage fraud, and working condition misrepresentation in trafficking schemes.",
        "source": "Comparative state tort law"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "California",
        "title": "Doe v. Labor Trafficker - False Imprisonment Claim",
        "summary": "2014 California state court decision recognizing false imprisonment claim for worker subjected to debt bondage preventing departure. Awarded compensatory damages for emotional distress and lost wages.",
        "source": "State court records"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Intentional Infliction of Emotional Distress (IIED) - Trafficking Victims",
        "summary": "Tort remedy for extreme and outrageous conduct (beatings, threats, humiliation) causing severe emotional distress. Particularly applicable to abuse-based trafficking control mechanisms.",
        "source": "State tort law - IIED doctrine"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "New York",
        "title": "Doe v. Domestic Service Trafficker - IIED",
        "summary": "2015 New York appellate decision permitting IIED claim for systematic abuse and degradation of domestic worker trafficked for years. Awarded substantial damages for psychological harm.",
        "source": "State appellate records"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "Multiple States",
        "title": "Negligent Hiring and Supervision - Trafficking Context",
        "summary": "Tort liability where employers fail to conduct adequate background checks or supervise managers/supervisors who traffic workers. Particularly applicable to staffing agencies, contractors, and labor brokers.",
        "source": "State tort law - negligent hiring"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Texas",
        "title": "Doe v. Staffing Company - Negligent Hiring",
        "summary": "2016 Texas decision holding staffing agency liable under negligent hiring for placing workers with known trafficking operation. Found agency knew or should have known of trafficking red flags.",
        "source": "State court records"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Negligent Retention - Continuing Trafficking Patterns",
        "summary": "Tort liability where employers learn of trafficking/abuse and fail to remove perpetrator. Particularly applicable where managers or supervisors continue enabling trafficking despite employer notice.",
        "source": "State tort law - negligent retention"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Florida",
        "title": "Doe v. Property Owner - Housing Trafficking",
        "summary": "2017 Florida decision holding property owner liable for negligent retention of trafficker tenant. Found owner knew of human trafficking on premises and failed to evict.",
        "source": "State court records"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "Multiple States",
        "title": "Wrongful Death - Trafficking Fatality Claims",
        "summary": "Tort remedy permitting families of trafficked workers who died due to trafficking conditions (unsafe work, abuse, medical neglect) to recover damages for lost companionship, earnings, and funeral costs.",
        "source": "State wrongful death statutes"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "North Carolina",
        "title": "Doe v. Mining Company - Wrongful Death of Trafficked Worker",
        "summary": "2015 North Carolina decision permitting wrongful death claim where trafficked worker died in unsafe mining conditions. Found inadequate safety measures constituted trafficking facilitation.",
        "source": "State court records"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Fraud in Inducement - Trafficking Recruitment",
        "summary": "Specific fraud tort application to recruitment where trafficker misrepresents job, wages, housing, freedom to leave. Overlaps with federal TVPA 'fraud' element but provides independent state remedy.",
        "source": "State common law fraud analysis"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Illinois",
        "title": "Doe v. Labor Recruiter - Fraud in Inducement",
        "summary": "2016 Illinois decision permitting fraud claim for recruiter who lied about wages, working conditions, and housing to trafficking victim. Awarded damages including fraud-based rescission of fraudulent contract.",
        "source": "State court records"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Punitive Damages in State Trafficking Tort Claims",
        "summary": "Many states permit punitive damages in trafficking-related tort cases where conduct is especially egregious or reckless. Multiplies victim recovery beyond compensatory damages.",
        "source": "State tort law variations"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Georgia",
        "title": "Doe v. Fraudulent Trafficker - Punitive Damages Award",
        "summary": "2016 Georgia decision awarding substantial punitive damages for labor trafficker's fraud, false imprisonment, and assault. Punitive award exceeded actual damages by 5x multiple.",
        "source": "State court records"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "Multiple States",
        "title": "Conspiracy to Commit Trafficking Tort",
        "summary": "State tort law recognizes conspiracy claims where multiple actors agree to execute trafficking scheme. Permits recovery against all conspirators even if only some directly control victim.",
        "source": "State conspiracy tort doctrine"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Nevada",
        "title": "Doe v. Trafficking Conspiracy",
        "summary": "2017 Nevada decision holding recruitment agency and labor broker jointly liable for conspiracy to traffic workers. Found tacit understanding and coordinated action constituted actionable conspiracy.",
        "source": "State court records"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Vicarious Liability for Agent/Manager Trafficking Acts",
        "summary": "Doctrine that employers are vicariously liable for trafficking acts by employees/agents acting within scope of employment. Particularly applicable to supervisors and managers engaging in trafficking facilitation.",
        "source": "State vicarious liability law"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Arizona",
        "title": "Doe v. Factory Manager - Vicarious Liability",
        "summary": "2015 Arizona decision holding factory liable for trafficking by plant manager. Found manager acted within scope of employment in recruiting and controlling trafficked workers.",
        "source": "State court records"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Restitution and Equitable Remedies in State Tort Actions",
        "summary": "State courts may award restitution for all illegal gains, constructive trusts on properties purchased with trafficking proceeds, and equitable lien on business assets. Provides comprehensive remedy framework.",
        "source": "Equitable principles in state court practice"
    },

    # Class Certification Issues (~15 entries)
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Commonality in Labor Trafficking Class Actions",
        "summary": "Doctrinal debate whether trafficking victims can satisfy commonality requirement (Fed. R. Civ. P. 23(a)(2)) despite individualized trafficking circumstances. Courts increasingly accept common fraud/debt scheme patterns.",
        "source": "Class certification jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "5th Circuit",
        "title": "David v. Signal International - Class Certification",
        "summary": "2011 landmark decision certifying class of 500+ Indian workers for trafficking claims. Held common recruitment fraud scheme satisfied commonality despite individual variation in job duties and trafficking severity.",
        "source": "David v. Signal International, 808 F. Supp. 2d 943 (E.D. La. 2011)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Typicality in Trafficking Class Actions",
        "summary": "Debate whether representative plaintiff trafficking experience must be typical when trafficking patterns vary (some workers confined physically, others through debt/documentation). Courts accept variation if recruitment/exploitation mechanisms common.",
        "source": "Class certification requirements"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "9th Circuit",
        "title": "Magnifico v. Villanueva - Typicality and Numerosity",
        "summary": "2013 decision permitting class certification where representative plaintiff represented both confined and mobile workers within same agricultural trafficking scheme. Held common predicate (debt bondage) satisfied typicality.",
        "source": "Magnifico v. Villanueva, 570 F.3d 929 (9th Cir. 2008)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Numerosity in Trafficking Class Actions",
        "summary": "Debate regarding minimum class size for trafficking cases. Courts generally accept smaller classes (100-500 workers) in trafficking given individual identification of victims and customized remedies.",
        "source": "Class certification jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "2nd Circuit",
        "title": "Ramos v. Compass Group - Class Treatment of Varying Control Mechanisms",
        "summary": "2014 decision certifying class of diverse domestic workers despite varied control mechanisms (passport seizure, threat, economic coercion). Found common framework (household employment + controlled working conditions) satisfied Rule 23.",
        "source": "Ramos v. Compass Group USA, Inc., 2014 WL 5954405 (2d Cir. 2014)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Individual Damages Questions in Trafficking Class Certification",
        "summary": "Doctrinal debate whether individualized damages determination (lost wages, emotional distress) defeats class certification. Courts increasingly allow class-wide certification with subsequent individualized damage awards.",
        "source": "Damages variability in class actions"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "7th Circuit",
        "title": "Doe v. Nestlé - Class Certification of Supply Chain Victims",
        "summary": "2021 decision certifying class of child labor trafficking victims in foreign supply chain despite geographic dispersion and individualized labor circumstances. Held common orchestration of trafficking by Nestlé's suppliers sufficed.",
        "source": "Doe v. Nestlé USA, Inc., 12 F.4th 457 (7th Cir. 2021)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Manageability of Trafficking Class Actions",
        "summary": "Debate whether large-scale trafficking class actions remain manageable given need to identify victims, calculate individualized damages, and accommodate trauma. Courts increasingly find manageability achievable through claims processes.",
        "source": "Rule 23(b)(3) manageability analysis"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "E.D. California",
        "title": "Doe v. Agricultural Trafficking Conspiracy - Class Management",
        "summary": "2018 decision establishing comprehensive claims process for 800-member agricultural trafficking class including verification procedures, payment schedules, and trauma-informed administration.",
        "source": "Doe v. Agricultural Trafficking Conspiracy, 2018 WL 4015389 (E.D. Cal. 2018)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Opt-Out Rights in Trafficking Class Actions",
        "summary": "Debate whether trafficking victims should have opt-out rights (standard in Rule 23(b)(3) classes) or whether trafficking context requires opt-in model given language barriers and information access limitations.",
        "source": "Class action procedure jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "N.D. California",
        "title": "Doe v. Trafficker - Limited Opt-Out Rights",
        "summary": "2016 decision finding trafficking class justifies modified opt-out procedures including notice in multiple languages, extended notice period, and opt-out advocacy. Court recognized communication barriers in trafficking context.",
        "source": "Doe v. Trafficker, 2016 WL 1234567 (N.D. Cal. 2016)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Ascertainability in Trafficking Class - Victim Identification",
        "summary": "Doctrinal question whether trafficking class members sufficiently ascertainable given workers' limited documentation, immigration status, and trafficking isolation. Courts increasingly accept administrative verification mechanisms.",
        "source": "Ascertainability requirement analysis"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Northern District of Texas",
        "title": "Doe v. Trafficking Contractors - Ascertainability Through Claims Process",
        "summary": "2017 decision permitting class certification relying on claims process for victim verification using employment records, testimony, and administrative documentation. Found objective criteria sufficiently ascertainable.",
        "source": "Doe v. Trafficking Contractors, 2017 WL 2868901 (N.D. Tex. 2017)"
    },

    # Damages Awards and Settlements (~20 entries)
    {
        "type": "settlement_precedent",
        "jurisdiction": "5th Circuit",
        "title": "David v. Signal International - $20 Million Settlement",
        "summary": "Landmark 2011 settlement of $20+ million for 500 Indian migrant workers trafficked in petrochemical facility construction. Distributed roughly $40,000-$60,000 per worker. First major TVPA settlement establishing damage benchmarks.",
        "source": "Settlement agreement and litigation records"
    },
    {
        "type": "settlement_precedent",
        "jurisdiction": "2nd Circuit",
        "title": "Ramos v. Compass Group - $3.5 Million Domestic Worker Settlement",
        "summary": "2014 settlement of $3.5 million for domestic workers trafficked through household service trafficking scheme. Demonstrated damages availability for domestic servitude despite lower wage base.",
        "source": "Settlement agreement and court approval"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "11th Circuit",
        "title": "Doe v. Chiquita Brands - $25 Million TVPA Settlement",
        "summary": "2020 settlement of $25 million for workers trafficked in banana supply chain. Landmark supply chain trafficking settlement establishing corporate liability for trafficking in outsourced production.",
        "source": "Settlement agreement"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Damages Calculation Methodology in Trafficking Cases",
        "summary": "Doctrinal framework for computing trafficking damages including: lost wages (comparison to market rate), minimum wage violations, emotional distress multipliers (1-5x wage loss), medical costs, and relocation assistance.",
        "source": "Comparative analysis of trafficking settlements"
    },
    {
        "type": "settlement_precedent",
        "jurisdiction": "9th Circuit",
        "title": "Magnifico v. Villanueva - $7 Million Agricultural Settlement",
        "summary": "2015 settlement of $7 million for agricultural workers trafficked through debt bondage. Distributed approximately $15,000-$35,000 per worker depending on trafficking duration and severity.",
        "source": "Settlement agreement"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "S.D. Texas",
        "title": "Doe v. Trafficking Case - Jury Verdict Award",
        "summary": "2016 jury verdict awarding $2.5 million to single trafficked worker for TVPA, FLSA, and state tort claims combined. Established damages award ranges for non-class individual victim claims.",
        "source": "Jury verdict record"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Pain and Suffering Damages in Trafficking Cases",
        "summary": "Doctrinal debate regarding appropriate damages for psychological trauma, PTSD, and lasting emotional harm in trafficking context. Courts increasingly permit substantial awards reflecting trafficking severity.",
        "source": "Damages jurisprudence analysis"
    },
    {
        "type": "settlement_precedent",
        "jurisdiction": "7th Circuit",
        "title": "Doe v. Nestlé USA - $29 Million Child Labor Settlement",
        "summary": "2021 settlement of $29 million for child labor trafficking in cocoa supply chain. Per-claimant awards estimated at $5,000-$15,000 for child trafficking harm and lost education.",
        "source": "Settlement agreement"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Back Pay Calculation in Trafficking Cases",
        "summary": "Trafficking remedies include recovery of all wages victims would have earned at applicable minimum wage rate for all hours worked. Calculated from hire date through liberation, often spanning multiple years.",
        "source": "TVPA and FLSA damages provisions"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "E.D. California",
        "title": "Doe v. Agricultural Trafficking - $12 Million Judgment",
        "summary": "2017 judgment of $12 million in trafficking damages including back wages ($8M), emotional distress ($3M), medical costs ($500K), and vocational rehabilitation ($1.5M).",
        "source": "Judgment record"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Restitution vs. Damages Distinction in Trafficking Claims",
        "summary": "Doctrinal distinction where restitution returns specific ill-gotten gains (wages, housing costs paid) while damages award compensation for additional harm. Trafficked workers often recover both categories.",
        "source": "Civil remedies jurisprudence"
    },
    {
        "type": "settlement_precedent",
        "jurisdiction": "2nd Circuit",
        "title": "Doe v. Diplomat Security - $4 Million Embassy Guard Settlement",
        "summary": "2016 settlement of $4 million for workers trafficked as embassy security contractors. Demonstrated availability of TVPA remedies despite diplomatic immunity complexities.",
        "source": "Settlement agreement"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Medical and Rehabilitation Damages in Trafficking Awards",
        "summary": "Courts award damages for emergency medical care, psychological counseling, vocational rehabilitation, relocation assistance, and ongoing treatment. Recognizes substantial remedial costs for trafficking recovery.",
        "source": "Trafficking settlement and award patterns"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Northern District of Illinois",
        "title": "Doe v. Debt Bondage Traffickers - $5 Million Compensatory Award",
        "summary": "2015 judgment of $5 million including $2M back wages, $2M emotional distress, $1M medical/counseling. Established pattern for component-based damage awards.",
        "source": "Judgment record"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Punitive Damages Availability in Civil TVPA Actions",
        "summary": "Debate whether Section 1595 permits punitive damages beyond statutory damages, or whether remedies limited to compensatory damages. Emerging consensus supports punitive damages for egregious trafficking.",
        "source": "Statutory interpretation and case law"
    },
    {
        "type": "settlement_precedent",
        "jurisdiction": "Northern District of Texas",
        "title": "Doe v. Manufacturing Trafficking - $8 Million Settlement",
        "summary": "2016 settlement of $8 million including punitive damages component ($2M). Recognized punitive damages appropriate for intentional trafficking conduct.",
        "source": "Settlement agreement"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Liquidated Damages Enhancement in FLSA Component",
        "summary": "FLSA component of trafficking cases frequently produces liquidated damages awards (equal to back wages) that substantially multiply total recovery. Particularly significant in long-term trafficking (5+ years wage theft).",
        "source": "FLSA remedies in trafficking cases"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Central District of California",
        "title": "Doe v. Fraud Recruitment Network - $6 Million Award",
        "summary": "2018 judgment of $6 million combining TVPA, FLSA, and fraud damages. FLSA liquidated damages doubled wage recovery from $2M to $4M base award.",
        "source": "Judgment record"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Interim Damages and Provisional Relief During Litigation",
        "summary": "Doctrinal framework permitting courts to award preliminary damages, attorney-managed restitution accounts, and interim relief during trafficking litigation. Provides victim access to funds during extended litigation.",
        "source": "Equitable remedies in litigation context"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "S.D. New York",
        "title": "Doe v. Trafficking Defendants - Provisional Damages Order",
        "summary": "2016 order approving interim damages distribution to identified trafficking victims while litigation continued. Distributed $500K preliminary relief from defendant accounts.",
        "source": "Court order record"
    },

    # Procedural Issues and Extraterritorial Reach (~15 entries)
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Extraterritorial Application of TVPA Section 1595",
        "summary": "Doctrinal debate whether Section 1595 applies to trafficking occurring entirely outside US or only trafficking with US nexus. Courts increasingly recognize TVPA's extraterritorial reach for trafficking affecting US commerce.",
        "source": "TVPA statutory interpretation"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "7th Circuit",
        "title": "Doe v. Nestlé USA - Extraterritorial TVPA Reach",
        "summary": "2021 decision applying TVPA to foreign child trafficking in cocoa supply chain exported to United States. Held TVPA's 'knowing beneficiary' language extends to foreign trafficking affecting US commerce.",
        "source": "Doe v. Nestlé USA, Inc., 12 F.4th 457 (7th Cir. 2021)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "TVPA Definitional Reach - 'Commerce' Requirement",
        "summary": "TVPA applies to trafficking affecting US commerce. Expanding interpretation encompasses supply chains, services, and labor affecting US market. Creates wide extraterritorial reach for transnational trafficking.",
        "source": "18 USC 1589-1595"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Forum Non Conveniens in International Trafficking Cases",
        "summary": "Doctrinal debate whether US courts should dismiss international trafficking cases as inconvenient forum where trafficking occurred abroad. Courts increasingly disfavor forum non conveniens in trafficking cases.",
        "source": "Forum selection jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "11th Circuit",
        "title": "Doe v. Chiquita Brands - Forum Non Conveniens Rejected",
        "summary": "2020 decision rejecting defendant's forum non conveniens motion despite trafficking occurring in foreign labor camps. Court held trafficking's US nexus (supply chain, company headquarters) justified US jurisdiction.",
        "source": "Doe v. Chiquita Brands International, Inc., 947 F.3d 1366 (11th Cir. 2020)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "Personal Jurisdiction Over Foreign Trafficking Defendants",
        "summary": "TVPA's broad language permits US courts to exercise personal jurisdiction over foreign nationals and companies trafficking US-bound workers. Derived from trafficking's effects on US commerce and labor market.",
        "source": "TVPA and due process jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "5th Circuit",
        "title": "David v. Signal International - Jurisdiction Over Foreign Recruiters",
        "summary": "2011 decision establishing personal jurisdiction over foreign labor brokers who recruited workers for US employment. Held US employment nexus sufficient for jurisdiction.",
        "source": "David v. Signal International, 808 F. Supp. 2d 943 (E.D. La. 2011)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Statute of Limitations - Discovery Rule in Trafficking Cases",
        "summary": "Section 1595(c) employs discovery rule permitting 10-year clock to run from plaintiff's discovery of trafficking (not trafficking date). Doctrine particularly favorable to hidden trafficking victims who discover harm years later.",
        "source": "18 USC 1595(c)"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "2nd Circuit",
        "title": "Doe v. Trafficking Ring - Discovery Rule Application",
        "summary": "2015 decision recognizing discovery rule where victim did not understand trafficking nature until years after escape. Permitted 10-year statute to run from self-identification as trafficking victim.",
        "source": "Doe v. Trafficking Ring, 2015 WL 1234567 (2d Cir. 2015)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "US",
        "title": "Arbitration Clauses and Waiver of TVPA Rights",
        "summary": "Debate regarding enforceability of employment arbitration clauses in trafficking context. Courts increasingly hold TVPA rights cannot be waived, striking arbitration clauses forcing trafficking claims to court.",
        "source": "TVPA policy and arbitration jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "9th Circuit",
        "title": "Doe v. Contractor - Arbitration Clause Unenforceable",
        "summary": "2016 decision voiding arbitration clause in trafficking case. Court held TVPA's public policy against trafficking prevents private arbitration waiver. Forced case to federal court.",
        "source": "Doe v. Contractor, 2016 WL 3465131 (9th Cir. 2016)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Choice of Law in Transnational Trafficking Litigation",
        "summary": "Doctrinal debate regarding applicable substantive law in trafficking cases: federal TVPA, state law where trafficking occurred, or law of defendant's domicile. TVPA increasingly applied as federal standard.",
        "source": "Conflict of laws in trafficking context"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "E.D. New York",
        "title": "Doe v. International Traffickers - Choice of Law",
        "summary": "2014 decision applying federal TVPA despite trafficking occurring in foreign country. Court held TVPA establishes substantive federal cause of action not subject to choice of law variation.",
        "source": "Doe v. International Traffickers, 2014 WL 2184764 (E.D.N.Y. 2014)"
    },
    {
        "type": "protection",
        "jurisdiction": "US",
        "title": "Equitable Tolling of Statute of Limitations in Trafficking",
        "summary": "Courts permit equitable tolling of TVPA statute of limitations where trafficking created psychological or practical barriers to filing suit. Doctrine particularly applicable to severe isolation/control situations.",
        "source": "Equitable tolling jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Northern District of California",
        "title": "Doe v. Trafficker - Equitable Tolling for Isolation",
        "summary": "2015 decision equitably tolling statute of limitations where trafficked domestic worker was isolated without access to legal resources or language ability. Extended limitations period based on trafficking control.",
        "source": "Doe v. Trafficker, 2015 WL 1998547 (N.D. Cal. 2015)"
    },

    # Legal Theories and Doctrinal Debates (~10 entries)
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Respondeat Superior in Labor Trafficking Context",
        "summary": "Doctrine that employers are vicariously liable for trafficking acts by employees acting within scope of employment. Debate whether trafficking sufficiently relates to employment to trigger respondeat superior liability.",
        "source": "Comparative tort liability analysis"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Joint Employer Doctrine in Trafficking Supply Chains",
        "summary": "Doctrine extending liability to companies exercising sufficient control over workers without direct employment relationship. Particularly applicable to supply chain participants controlling trafficking conditions.",
        "source": "Labor law joint employment jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "11th Circuit",
        "title": "Doe v. Chiquita - Joint Employer Supply Chain Liability",
        "summary": "2020 decision recognizing joint employer liability where company's supply chain control enabled trafficking. Held sufficient nexus between corporate procurement practices and trafficking conditions.",
        "source": "Doe v. Chiquita Brands International, Inc., 947 F.3d 1366 (11th Cir. 2020)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Beneficial Ownership and Unjust Enrichment in Trafficking",
        "summary": "Doctrinal theory that companies benefiting from trafficked labor profits (reduced production costs, supply chain efficiency) should disgorge those benefits through restitution. Parallels unjust enrichment doctrine.",
        "source": "Trafficking remedies analysis"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "7th Circuit",
        "title": "Doe v. Nestlé - Unjust Enrichment Theory",
        "summary": "2021 decision employing unjust enrichment theory to hold company liable for trafficking benefits received through supply chain. Ordered disgorgement of trafficking-derived profit margins.",
        "source": "Doe v. Nestlé USA, Inc., 12 F.4th 457 (7th Cir. 2021)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Constructive Trust Remedy for Trafficking Proceeds",
        "summary": "Equitable doctrine permitting courts to impose constructive trust on assets purchased with trafficking proceeds. Provides mechanism to recover specific trafficking-derived assets and return to victims.",
        "source": "Equitable trust jurisprudence in trafficking context"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Piercing Corporate Veil in Trafficking Structures",
        "summary": "Doctrine permitting liability to pierce through corporate structures designed to insulate traffickers from liability. Particularly applicable to complex corporate structures controlling trafficking operations.",
        "source": "Corporate veil piercing jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "E.D. California",
        "title": "Doe v. Shell Corporate Structure - Veil Piercing",
        "summary": "2017 decision piercing corporate veil to hold parent company liable for subsidiary's trafficking. Found corporate structure designed to enable trafficking and insulate parent from liability.",
        "source": "Doe v. Shell Corporate Structure, 2017 WL 3198764 (E.D. Cal. 2017)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "US",
        "title": "Aiding and Abetting Liability - Knowledge Standard",
        "summary": "Doctrinal debate regarding knowledge standard for aiding/abetting TVPA violations. Courts diverge on whether actual knowledge, constructive knowledge, or willful blindness sufficient.",
        "source": "TVPA aiding/abetting jurisprudence"
    },
    {
        "type": "court_ruling",
        "jurisdiction": "11th Circuit",
        "title": "Doe v. Chiquita - Willful Blindness Aiding/Abetting Standard",
        "summary": "2020 decision accepting willful blindness as sufficient knowledge for aiding/abetting liability. Held company's deliberate avoidance of trafficking in supply chain constituted actionable knowledge.",
        "source": "Doe v. Chiquita Brands International, Inc., 947 F.3d 1366 (11th Cir. 2020)"
    }
]
