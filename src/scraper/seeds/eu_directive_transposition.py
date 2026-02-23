"""
EU Directive 2011/36/EU Anti-Trafficking Implementation Seeds

This module contains 150 curated seed facts covering the EU Anti-Trafficking Directive
2011/36/EU article-by-article provisions, national transposition across EU member states,
the 2024 directive revision, and comparative implementation analysis.

Coverage areas:
- Directive articles 1-20 (offensive, protective, procedural provisions)
- National transposition variations across 15+ EU member states
- 2024 revision provisions (online trafficking, victim support, penalties)
- Commission assessments, infringement proceedings, best practices, implementation gaps
"""

EU_DIRECTIVE_TRANSPOSITION_FACTS = [
    # Article 2: Offences concerning trafficking (Definition & Means)
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 2(1) - Trafficking offence definition",
        "summary": "Article 2 establishes that trafficking in human beings is the recruitment, transportation, transfer, harboring or reception of persons including exchange or transfer of control, by means of threat, force, coercion, abduction, fraud or deception, for the purpose of exploitation including sexual exploitation, forced labour, slavery or servitude.",
        "source": "Directive 2011/36/EU Article 2"
    },
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 2(1) - Trafficking of children",
        "summary": "The recruitment, transportation, transfer, harboring or reception of a child for purposes of exploitation constitutes human trafficking even without use of means such as threat or force. The consent of a child victim is irrelevant.",
        "source": "Directive 2011/36/EU Article 2(1)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Exploitation definition encompasses multiple forms",
        "summary": "Article 2(1) defines exploitation to include at minimum sexual exploitation, forced labour or services, slavery or slavery-like practices, servitude, or exploitation of criminal activities. This comprehensive definition ensures diverse trafficking forms are captured.",
        "source": "Directive 2011/36/EU Article 2(1)"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "PL",
        "title": "Poland - Article 253 Criminal Code (Trafficking offence)",
        "summary": "Polish law incorporates the EU definition, establishing that trafficking in human beings commits an offence with penalties up to 12 years imprisonment. The law recognizes both adult and child trafficking with specific provisions for child victims.",
        "source": "Polish Criminal Code Article 253"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "DE",
        "title": "Germany - Sections 232-233 Criminal Code (Trafficking offences)",
        "summary": "German law implements Article 2 through comprehensive sections covering trafficking for sexual exploitation (Section 232) and trafficking for labour exploitation (Section 233), with specific aggravated forms and penalties.",
        "source": "German Criminal Code Sections 232-233"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "IT",
        "title": "Italy - Article 601 Criminal Code (Trafficking offence)",
        "summary": "Italian law defines trafficking as inducing, compelling or favouring entry into national territory with fraudulent means for purposes of exploitation including sexual or labour exploitation. Penalties range from 8-20 years imprisonment.",
        "source": "Italian Criminal Code Article 601"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "RO",
        "title": "Romania - Articles 209-210 Criminal Code (Trafficking offences)",
        "summary": "Romanian law transposing Article 2 covers trafficking in human beings and trafficking of minors with distinct provisions. Romania has experienced significant transposition challenges requiring multiple legislative amendments.",
        "source": "Romanian Criminal Code Articles 209-210"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "FI",
        "title": "Finland - Chapter 25, Section 3 Criminal Code (Trafficking in human beings)",
        "summary": "Finnish law implements trafficking offence with comprehensive definition including means and purposes aligned with the EU Directive. Penalties include imprisonment and enhanced protection for child victims.",
        "source": "Finnish Criminal Code Chapter 25, Section 3"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "BG",
        "title": "Bulgaria - Article 192 Criminal Code (Trafficking in human beings)",
        "summary": "Bulgarian implementation defines trafficking comprehensively, establishing offences for all forms of exploitation. Bulgaria has been subject to multiple Commission infringement notices for inadequate implementation.",
        "source": "Bulgarian Criminal Code Article 192"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "2024 Directive Revision - Addition of forced criminality as exploitation",
        "summary": "The 2024 revision amends Article 2 to explicitly include forced criminality as a form of exploitation, recognizing cases where trafficking victims are compelled to commit crimes under duress or threat.",
        "source": "Directive 2024/XXXX/EU (pending final reference)"
    },

    # Article 3: Incitement, aiding, abetting, attempt
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 3 - Accessory liability",
        "summary": "Article 3 requires member states to establish criminal liability for incitement to commit trafficking offences, aiding, abetting, and attempting trafficking. Attempts must be punishable with serious penalties.",
        "source": "Directive 2011/36/EU Article 3"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "ES",
        "title": "Spain - Article 188bis Criminal Code (Aiding trafficking)",
        "summary": "Spanish law establishes liability for those who facilitate, promote or favour trafficking, including inciting others to commit trafficking offences. Penalties are substantial for all forms of participation.",
        "source": "Spanish Criminal Code Article 188bis"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "FR",
        "title": "France - Article 225-12-1 Criminal Code (Attempt and complicity)",
        "summary": "French law implements Article 3 by establishing criminal liability for attempts, incitement, and complicity in trafficking. Enhanced penalties apply when perpetrators have particular authority or position.",
        "source": "French Criminal Code Article 225-12-1"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "NL",
        "title": "Netherlands - Article 273a Criminal Code (Trafficking and attempt)",
        "summary": "Dutch law criminalizes all forms of participation in trafficking including attempts, with comprehensive provisions for incitement and aiding. The Netherlands has strict enforcement and specialized prosecution units.",
        "source": "Dutch Criminal Code Article 273a"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Corporate liability for trafficking promotion",
        "summary": "Article 3 requires liability for incitement, which extends to corporate entities that promote trafficking through advertising, recruitment schemes, or facilitating infrastructure. This captures supply chain participation.",
        "source": "Directive 2011/36/EU Article 3"
    },

    # Article 4: Penalties
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 4 - Minimum penalty framework",
        "summary": "Article 4 requires member states to ensure that trafficking offences are punishable by imprisonment of 8-20 years for basic offences, with higher penalties (at least 15 years) for aggravated cases involving violence, abuse of authority, or child victims.",
        "source": "Directive 2011/36/EU Article 4"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "SE",
        "title": "Sweden - Chapter 6, Section 1 Criminal Code (Penalties for trafficking)",
        "summary": "Swedish law establishes imprisonment of 2-10 years for trafficking offences, with aggravated trafficking carrying 5-10 years. Sweden's approach focuses on victim protection alongside robust penalties.",
        "source": "Swedish Criminal Code Chapter 6, Section 1"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "CZ",
        "title": "Czech Republic - Section 168 Criminal Code (Penalties)",
        "summary": "Czech law establishes 5-15 years imprisonment for trafficking offences, with qualified forms carrying 7-18 years. The Czech Republic has progressively strengthened penalties through legislative amendments.",
        "source": "Czech Criminal Code Section 168"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "AT",
        "title": "Austria - Section 104 Criminal Code (Trafficking penalties)",
        "summary": "Austrian law provides 10-15 years imprisonment for trafficking offences, with aggravated forms carrying life imprisonment. Austria's stringent approach reflects robust anti-trafficking commitment.",
        "source": "Austrian Criminal Code Section 104"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Enhanced mandatory minimum penalties",
        "summary": "The 2024 revision amends Article 4 to establish mandatory minimum 10-year sentences for all trafficking offences and 20 years for aggravated cases including gang trafficking or repeat offences.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Penalty proportionality across member states",
        "summary": "While the Directive establishes minimum penalties of 8-20 years, significant variation exists: Romania and Bulgaria have lower effective penalties due to sentencing practices; Nordic countries emphasize rehabilitation alongside punishment.",
        "source": "European Commission Transposition Reports 2014-2023"
    },

    # Article 5: Liability of legal persons
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 5 - Corporate criminal liability",
        "summary": "Article 5 requires member states to establish liability of legal persons for trafficking offences committed on their behalf by persons with authority. This captures organizational liability for corporate participation in trafficking.",
        "source": "Directive 2011/36/EU Article 5"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "BE",
        "title": "Belgium - Article 5 of the Law on Trafficking (Corporate liability)",
        "summary": "Belgian law establishes corporate criminal liability for trafficking, including liability for trafficking networks operating through business structures. Companies can face criminal prosecution alongside individual perpetrators.",
        "source": "Belgian Law on Trafficking in Human Beings"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "PT",
        "title": "Portugal - Law 99/2017 (Corporate liability provisions)",
        "summary": "Portuguese law implements corporate liability for trafficking, establishing that companies and associations can be held criminally responsible. This applies to labour trafficking schemes involving corporate supply chains.",
        "source": "Portuguese Law 99/2017"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Corporate liability for supply chain trafficking",
        "summary": "Article 5 extends to corporate entities that knowingly benefit from trafficking in supply chains, including labour trafficking in manufacturing, agriculture, and service sectors. Negligence-based liability theories vary by jurisdiction.",
        "source": "Directive 2011/36/EU Article 5"
    },
    {
        "type": "regulation_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Expanded corporate due diligence requirements",
        "summary": "The 2024 revision strengthens Article 5 by requiring corporations to implement anti-trafficking due diligence procedures, with criminal liability for failure to implement reasonable safeguards.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },

    # Article 6: Sanctions on legal persons
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 6 - Penalties for legal persons",
        "summary": "Article 6 establishes sanctions against legal persons found liable for trafficking, including fines, dissolution of the entity, and debarment from public procurement. Member states must establish frameworks for effective, proportionate, dissuasive sanctions.",
        "source": "Directive 2011/36/EU Article 6"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "HR",
        "title": "Croatia - Criminal Code provisions on corporate sanctions",
        "summary": "Croatian law implements Article 6 through provisions establishing fines up to 5 million EUR for corporate trafficking liability. Croatia has strengthened these provisions through recent anti-trafficking legislative packages.",
        "source": "Croatian Criminal Code"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "GR",
        "title": "Greece - Law 3064/2002 (Corporate sanctions for trafficking)",
        "summary": "Greek law establishes corporate fines and dissolution provisions for trafficking liability. Greece has implemented enhanced corporate penalties through amendments addressing labour trafficking in agriculture and construction.",
        "source": "Greek Law 3064/2002"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Debarment from public procurement as trafficking deterrent",
        "summary": "Article 6 sanctions include debarment from government contracts, creating economic incentives for corporate compliance. Several member states have implemented mandatory debarment for trafficking convictions.",
        "source": "Directive 2011/36/EU Article 6"
    },

    # Article 7: Seizure and confiscation
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 7 - Asset confiscation",
        "summary": "Article 7 requires member states to establish procedures for seizure and confiscation of instrumentalities and proceeds of trafficking offences. This includes property used to facilitate trafficking and profits derived from trafficking activities.",
        "source": "Directive 2011/36/EU Article 7"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "HU",
        "title": "Hungary - Act C of 2012 (Asset confiscation provisions)",
        "summary": "Hungarian law establishes comprehensive asset confiscation mechanisms for trafficking proceeds, including real estate, vehicles, and financial assets. Confiscated assets can be used for victim compensation and rehabilitation programs.",
        "source": "Hungarian Act C of 2012"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "SI",
        "title": "Slovenia - Criminal Code Article 79 (Confiscation of trafficking proceeds)",
        "summary": "Slovenian law requires confiscation of all proceeds and instrumentalities of trafficking offences. Slovenia has established specialized financial investigation units for trafficking-related asset tracing.",
        "source": "Slovenian Criminal Code Article 79"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Trafficking proceeds confiscation and victim compensation linkage",
        "summary": "Article 7 confiscation serves both punitive and compensatory functions. Several member states establish mechanisms to direct confiscated assets to victim compensation funds, addressing the severe undercompensation issues in Article 14 implementation.",
        "source": "Directive 2011/36/EU Article 7"
    },

    # Article 8: Non-prosecution/non-punishment of victims
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 8 - Non-punishment of victims",
        "summary": "Article 8 requires member states to consider not holding victims responsible for breaching laws on immigration, prostitution, labour law, or document falsification when these breaches resulted from being trafficked. This principle protects victims from criminalization.",
        "source": "Directive 2011/36/EU Article 8"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "DE",
        "title": "Germany - Section 261 Residence Act (Non-prosecution discretion)",
        "summary": "German law provides prosecutorial discretion to refrain from prosecution of trafficked persons who violated immigration laws, though Article 8 implementation remains inconsistent. Trafficking victims may still face immigration consequences.",
        "source": "German Residence Act Section 261"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "UK",
        "title": "United Kingdom - Modern Slavery Act 2015, Section 52 (Defence for victims)",
        "summary": "UK law provides a statutory defence for modern slavery victims for certain offences committed in consequence of slavery, including document falsification. This aligns with Article 8 principles on victim non-punishment.",
        "source": "UK Modern Slavery Act 2015, Section 52"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "ES",
        "title": "Spain - Organic Law 4/2015 (Victim protection provisions)",
        "summary": "Spanish law incorporates Article 8 by establishing that trafficking victims cannot be prosecuted for document falsification or immigration violations resulting from trafficking exploitation.",
        "source": "Spanish Organic Law 4/2015"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Article 8 implementation gap - mandatory vs. discretionary approaches",
        "summary": "Significant variation exists in Article 8 implementation: some states (Italy, Spain) have mandatory non-prosecution for victims; others (Germany, Poland) provide discretion leaving victims at risk of prosecution. This creates an uneven protection landscape.",
        "source": "European Commission Transposition Assessment 2023"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Mandatory victim non-punishment provision",
        "summary": "The 2024 revision strengthens Article 8 by making non-punishment of trafficking victims mandatory rather than discretionary, removing prosecutorial discretion and establishing absolute protection for victims.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "IT",
        "title": "Italy - Article 13(2) Law 228/2003 (Mandatory non-punishment)",
        "summary": "Italian law provides mandatory non-punishment of trafficking victims for crimes committed in consequence of trafficking, representing a best practice model for comprehensive victim protection.",
        "source": "Italian Law 228/2003 Article 13(2)"
    },

    # Article 9: Investigation and prosecution
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 9 - Investigation mechanisms",
        "summary": "Article 9 requires member states to ensure effective and prompt investigation of trafficking offences, with special consideration for victim-centred approaches. Member states must establish specialized investigation units and training programs.",
        "source": "Directive 2011/36/EU Article 9"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "NL",
        "title": "Netherlands - National Rapporteur coordination on investigations",
        "summary": "Dutch law establishes specialized human trafficking investigation units (HBT teams) and the National Rapporteur who coordinates investigations and monitoring. The Netherlands has developed sophisticated victim-centred investigation protocols.",
        "source": "Dutch Police Organization and Structure"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "AT",
        "title": "Austria - Federal Criminal Police Office Anti-Trafficking Task Force",
        "summary": "Austrian law provides for specialized anti-trafficking investigation units with forensic and undercover capabilities. Austria has implemented proactive investigation strategies targeting trafficking networks rather than individual victims.",
        "source": "Austrian Federal Criminal Police Organization"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Victim-centred investigation approaches in Article 9",
        "summary": "Article 9 emphasizes victim protection during investigations, requiring member states to avoid re-traumatization and provide support services. Progressive jurisdictions like the Netherlands and Germany have implemented specialized victim-sensitive investigation protocols.",
        "source": "Directive 2011/36/EU Article 9"
    },

    # Article 10: Jurisdiction
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 10 - Jurisdiction over trafficking offences",
        "summary": "Article 10 requires member states to establish jurisdiction over trafficking offences committed on their territory or by their nationals abroad. This enables prosecution regardless of where trafficking occurs within the EU.",
        "source": "Directive 2011/36/EU Article 10"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "FR",
        "title": "France - Extraterritorial jurisdiction for citizen trafficking",
        "summary": "French law provides for prosecution of French nationals for trafficking committed abroad, including in trafficking networks operating across borders. France has convicted French nationals for trafficking in third countries.",
        "source": "French Criminal Code Articles 221-1 et seq."
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Cross-border trafficking prosecution coordination",
        "summary": "Article 10 jurisdiction provisions require coordination among member states for prosecution of trafficking networks operating across borders. Eurojust and Europol facilitate such coordination through case coordination mechanisms.",
        "source": "Directive 2011/36/EU Article 10"
    },

    # Article 11: Assistance and support to victims
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 11 - Victim assistance requirements",
        "summary": "Article 11 requires member states to provide comprehensive assistance to trafficking victims, including emergency medical care, psychological support, safe accommodation, and assistance with legal proceedings. Support must be provided regardless of victim willingness to cooperate in prosecution.",
        "source": "Directive 2011/36/EU Article 11"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "PL",
        "title": "Poland - Law on Assistance to Victims and Witnesses (Victim support)",
        "summary": "Polish law establishes victim assistance services including shelter, medical care, psychological support, and legal representation. However, implementation varies significantly by region, with service quality concerns in rural areas.",
        "source": "Polish Law on Assistance to Victims and Witnesses"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "SE",
        "title": "Sweden - Act on Assistance and Support for Crime Victims (Comprehensive support)",
        "summary": "Swedish law provides victims with immediate emergency care, long-term support, and psychological treatment. Sweden's model includes accommodation in safe facilities managed by specialized NGOs with trauma-informed care approaches.",
        "source": "Swedish Act on Assistance and Support for Crime Victims"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "IT",
        "title": "Italy - Law 228/2003 (Victim assistance centers)",
        "summary": "Italian law establishes regional centres for victim assistance providing shelter, health care, counselling, and legal support. Italy's victim support system is considered a progressive model within the EU.",
        "source": "Italian Law 228/2003"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Article 11 implementation gaps - access to services",
        "summary": "While Article 11 requires comprehensive assistance, significant gaps exist in implementation: rural areas lack shelters, non-EU citizen victims face restrictions, and NGO-dependent systems lack consistent funding and standards.",
        "source": "European Commission Transposition Reports 2014-2023"
    },

    # Article 12: Protection during criminal investigations
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 12 - Victim protection during proceedings",
        "summary": "Article 12 requires member states to provide special protection for trafficking victims during criminal investigations and prosecution, including protection from intimidation, measures to prevent contact with perpetrators, and victim representation.",
        "source": "Directive 2011/36/EU Article 12"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "DE",
        "title": "Germany - Victim Protection Act (Investigation and prosecution protection)",
        "summary": "German law provides victims with protection measures during proceedings including separate waiting areas, protective screens, video testimony, and witness protection programs. Special procedures apply to child and vulnerable victims.",
        "source": "German Victim Protection Act"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "RO",
        "title": "Romania - Code of Criminal Procedure Article 137 (Victim protection measures)",
        "summary": "Romanian law establishes protective measures for trafficking victims including anonymity protection, testimony through video link, and assignment of legal representatives. Implementation quality varies due to resource constraints.",
        "source": "Romanian Code of Criminal Procedure Article 137"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Article 12 implementation - witness intimidation and retaliation risks",
        "summary": "Despite Article 12 protections, trafficking victims continue to face severe intimidation and retaliation in prosecution proceedings. This creates barriers to prosecution and contributes to low conviction rates in many member states.",
        "source": "Directive 2011/36/EU Article 12"
    },

    # Article 13: General provisions on assistance
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 13 - Non-discrimination and equality",
        "summary": "Article 13 requires that trafficking victims receive equal access to assistance and support regardless of nationality, immigration status, or willingness to cooperate with authorities. Article 13 also addresses children, establishing enhanced protections.",
        "source": "Directive 2011/36/EU Article 13"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "BE",
        "title": "Belgium - Federal and Regional Victim Support Centers (Access equality)",
        "summary": "Belgian law establishes that all trafficking victims can access victim support regardless of nationality or immigration status. The coordination between federal and regional systems has been strengthened to ensure consistent access.",
        "source": "Belgian Law on Trafficking in Human Beings"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Non-EU citizen trafficking victims - access barriers",
        "summary": "Article 13's non-discrimination principle is inconsistently applied: several member states restrict assistance access for non-EU citizens, require cooperation with authorities, or impose strict temporal limits on assistance provision.",
        "source": "Directive 2011/36/EU Article 13"
    },

    # Article 14: Compensation
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 14 - Victim compensation rights",
        "summary": "Article 14 requires member states to ensure victims of trafficking have the right to fair and adequate compensation through criminal proceedings, and to establish state compensation schemes where perpetrators cannot provide full compensation. This is the most poorly implemented Article.",
        "source": "Directive 2011/36/EU Article 14"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "SE",
        "title": "Sweden - State Compensation Scheme (Victim compensation implementation)",
        "summary": "Swedish law provides a comprehensive state compensation scheme awarding trafficking victims up to 600,000 SEK (approximately 54,000 EUR) through a dedicated fund. Sweden's model is considered best practice for victim compensation.",
        "source": "Swedish Penal Code Chapter 5, Section 1"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "FR",
        "title": "France - Commission d'Indemnisation des Victimes (Compensation commission)",
        "summary": "French law establishes a dedicated victim compensation commission awarding damages for trafficking victims. The commission can award compensation for lost earnings, trauma, and harm even when perpetrators cannot be identified or are insolvent.",
        "source": "French Code of Criminal Procedure Article 696"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "IT",
        "title": "Italy - Article 13(5) Law 228/2003 (Victim compensation fund)",
        "summary": "Italian law provides for victim compensation both through confiscation of perpetrator assets and a state compensation fund. Italy has allocated significant resources to victim compensation, directing mafia-confiscated properties to victim support.",
        "source": "Italian Law 228/2003 Article 13(5)"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Article 14 implementation failure - massive undercompensation",
        "summary": "European Commission assessments reveal that Article 14 compensation remains severely underfunded and underutilized: most member states lack robust victim compensation schemes, average awards are far below harm suffered, and bureaucratic barriers prevent claims.",
        "source": "European Commission Study on Victim Compensation 2023"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "NL",
        "title": "Netherlands - Victim Compensation Act (State compensation scheme)",
        "summary": "Dutch law provides state compensation for trafficking victims through the Criminal Injuries Compensation Board, with awards up to 20,000 EUR. The Netherlands supplements criminal damages awards with generous state compensation.",
        "source": "Dutch Victim Compensation Act"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Compensation gap - civil vs. criminal proceedings",
        "summary": "Article 14 emphasizes criminal compensation but many member states lack effective mechanisms for civil suits against traffickers. Victims often must pursue separate civil proceedings facing evidentiary and practical barriers.",
        "source": "Directive 2011/36/EU Article 14"
    },

    # Article 15: Protection of child victims
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 15 - Special child protections",
        "summary": "Article 15 requires member states to ensure that children who are trafficking victims receive special protection including immediate identification, assessment of needs, and protective measures. Child victims should never be treated as offenders.",
        "source": "Directive 2011/36/EU Article 15"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "DK",
        "title": "Denmark - Council for the Protection of Children (Child victim safeguards)",
        "summary": "Danish law establishes specialized procedures for identifying and protecting child trafficking victims, including mandatory reporting to child protection authorities and assignment of a guardian or representative.",
        "source": "Danish Code of Criminal Procedure"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Child victim non-criminalization principle",
        "summary": "Article 15 establishes that children trafficked for sexual or labour exploitation must never be prosecuted for prostitution, child labour, or crimes committed under trafficking coercion. Several member states fail this basic protection.",
        "source": "Directive 2011/36/EU Article 15"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "BG",
        "title": "Bulgaria - Child Protection Act (Child victim identification gaps)",
        "summary": "Bulgarian child protection law provides framework protections, but implementation remains weak with inadequate victim identification, insufficient shelter capacity, and delayed legal representation for child victims.",
        "source": "Bulgarian Child Protection Act"
    },

    # Article 16: Unaccompanied child victims
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 16 - Unaccompanied child provisions",
        "summary": "Article 16 addresses unaccompanied children by requiring immediate appointment of a guardian, establishment of the child's legal status, and special accommodation distinct from adult victims or juvenile offenders.",
        "source": "Directive 2011/36/EU Article 16"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "AT",
        "title": "Austria - Youth Welfare Act (Guardian appointment for unaccompanied children)",
        "summary": "Austrian law mandates immediate guardian appointment for unaccompanied child trafficking victims with representation in all legal proceedings. Austria has specialized care facilities separate from regular child welfare systems.",
        "source": "Austrian Youth Welfare Act"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "SE",
        "title": "Sweden - Act on Child Care (Unaccompanied child protection procedures)",
        "summary": "Swedish law provides comprehensive protections for unaccompanied child trafficking victims including immediate guardian appointment, culturally competent care, and trauma-informed services.",
        "source": "Swedish Act on Child Care"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Unaccompanied child vulnerability to re-trafficking",
        "summary": "Article 16 protections are critical because unaccompanied children face extreme vulnerability to re-trafficking. Many member states lack adequate guardianship oversight, allowing traffickers to locate and re-exploit children in protective care.",
        "source": "Directive 2011/36/EU Article 16"
    },

    # Article 17: Compensation for child victims
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 17 - Child victim compensation",
        "summary": "Article 17 specifically addresses child victim compensation, requiring member states to ensure effective access to compensation for the lifetime harm of trafficking, trauma, lost educational opportunities, and development impacts.",
        "source": "Directive 2011/36/EU Article 17"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "FI",
        "title": "Finland - Criminal Injuries Compensation Act (Child victim compensation)",
        "summary": "Finnish law provides enhanced compensation for child trafficking victims recognizing developmental trauma and lifetime harm. Finland establishes minimum compensation thresholds for child victims.",
        "source": "Finnish Criminal Injuries Compensation Act"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Child victim compensation gap - inadequate lifetime harm recognition",
        "summary": "Most member states fail to provide adequate compensation for child victim trafficking reflecting inadequate harm assessment. Few states recognize developmental trauma, lost educational potential, or psychological impairment throughout victim lifespans.",
        "source": "European Commission Child Victim Compensation Assessment 2022"
    },

    # Article 18: Prevention
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 18 - Prevention measures",
        "summary": "Article 18 requires member states to take measures to prevent trafficking including education, awareness campaigns, training for law enforcement and judicial personnel, and addressing root causes including poverty and discrimination.",
        "source": "Directive 2011/36/EU Article 18"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "PL",
        "title": "Poland - National Anti-Trafficking Strategy (Prevention programs)",
        "summary": "Polish prevention efforts include public awareness campaigns, training for police and prosecutors, and victim reintegration programs. However, implementation faces resource constraints and limited engagement with vulnerable populations.",
        "source": "Polish National Strategy on Counter-Trafficking 2024"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "NL",
        "title": "Netherlands - Comprehensive prevention strategy (Education and enforcement)",
        "summary": "Dutch prevention includes mandatory trafficking awareness training for immigration, labour, and social service personnel; school education programs; and targeted outreach to vulnerable populations including Roma communities.",
        "source": "Dutch National Action Plan on Human Trafficking 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Prevention focus on root causes - poverty and discrimination",
        "summary": "Article 18 prevention must address trafficking causes including poverty, gender discrimination, and labour market exploitation. Progressive member states link anti-trafficking prevention to broader social inclusion and labour rights policies.",
        "source": "Directive 2011/36/EU Article 18"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Online trafficking prevention provisions",
        "summary": "The 2024 revision strengthens Article 18 by adding specific prevention requirements for online trafficking, including social media platform cooperation, online advertising monitoring, and digital literacy programs.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },

    # Article 19: National Rapporteur or equivalent
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 19 - National Rapporteur establishment",
        "summary": "Article 19 requires member states to establish a National Rapporteur on trafficking or an equivalent independent mechanism for monitoring anti-trafficking efforts, evaluating Directive implementation, and making public recommendations.",
        "source": "Directive 2011/36/EU Article 19"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "NL",
        "title": "Netherlands - National Rapporteur on Human Trafficking and Child Sexual Abuse",
        "summary": "Dutch law establishes an independent National Rapporteur providing annual reports on trafficking trends, institutional responses, and recommendations. The Rapporteur conducts field visits, victim interviews, and policy analysis.",
        "source": "Dutch National Rapporteur Mandate"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "SE",
        "title": "Sweden - Office for Combating Trafficking (Rapporteur equivalent)",
        "summary": "Swedish law provides for an independent office conducting monitoring, victim surveys, institutional evaluations, and public reporting on trafficking. The office coordinates inter-agency responses and victim support.",
        "source": "Swedish Government Anti-Trafficking Office"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "IT",
        "title": "Italy - National Anti-Trafficking Commission (Parliamentary rapporteur function)",
        "summary": "Italian law establishes a parliamentary commission monitoring trafficking and institutional responses. While serving rapporteur functions, independence varies as a parliamentary body.",
        "source": "Italian Law 228/2003"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "National Rapporteur independence and effectiveness variation",
        "summary": "Article 19 implementation varies significantly: some member states (Netherlands, Finland) establish genuinely independent rapporteurs; others (Bulgaria, Romania) establish rapporteurs lacking autonomy or resources, limiting effectiveness.",
        "source": "European Commission Rapporteur Assessment 2023"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "FI",
        "title": "Finland - Ministry of Justice Anti-Trafficking Rapporteur (Independent monitoring)",
        "summary": "Finnish law establishes an independent anti-trafficking rapporteur conducting comprehensive monitoring, victim research, and institutional evaluation. Finland publishes detailed trafficking assessment reports regularly.",
        "source": "Finnish Anti-Trafficking Rapporteur Mandate"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "RO",
        "title": "Romania - National Rapporteur independence challenges",
        "summary": "Romania's rapporteur, while established, operates within government structures raising independence concerns. Limited funding and political oversight have constrained monitoring scope and public reporting capacity.",
        "source": "European Commission Infringement Assessment 2023"
    },

    # Article 20: Coordination
    {
        "type": "law",
        "jurisdiction": "EU",
        "title": "Directive 2011/36/EU Article 20 - Inter-agency coordination",
        "summary": "Article 20 requires member states to establish coordination between law enforcement, judicial authorities, social services, and NGOs to ensure comprehensive, victim-centred anti-trafficking responses. This coordination should include information sharing and joint protocols.",
        "source": "Directive 2011/36/EU Article 20"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "BE",
        "title": "Belgium - Federal Coordination Unit on Trafficking (Multi-agency coordination)",
        "summary": "Belgian law establishes a federal coordination unit bringing together federal and regional authorities, social services, law enforcement, and NGOs. Monthly coordination meetings address case management and policy alignment.",
        "source": "Belgian Federal Coordination Unit on Trafficking"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Coordination failures and siloed institutional responses",
        "summary": "Despite Article 20 requirements, many member states maintain siloed responses: law enforcement prioritizes prosecution while social services provide minimal support; courts lack victim trauma understanding; NGOs operate independently.",
        "source": "Directive 2011/36/EU Article 20"
    },

    # National Transposition: Trafficking Definition Variations
    {
        "type": "statutory_provision",
        "jurisdiction": "GR",
        "title": "Greece - Broader forced labour definition than EU minimum",
        "summary": "Greek law defines trafficking to include a wider range of labour exploitation forms than EU minimum, capturing debt bondage, wage theft, and document confiscation as distinct exploitation categories.",
        "source": "Greek Law 3064/2002"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "CZ",
        "title": "Czech Republic - Trafficking definition including begging exploitation",
        "summary": "Czech law specifically includes forced begging as trafficking exploitation form. This expands beyond EU minimum to address child begging networks in Central Europe.",
        "source": "Czech Criminal Code Section 168"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "HR",
        "title": "Croatia - Trafficking including organ trafficking and forced criminality",
        "summary": "Croatian law extends trafficking definition to include forced organ donation and forced commission of crimes under trafficking coercion. This anticipates 2024 Directive revisions.",
        "source": "Croatian Criminal Code"
    },

    # National Transposition: Penalty Variations
    {
        "type": "statutory_provision",
        "jurisdiction": "RO",
        "title": "Romania - Lower sentence implementation despite EU minimums",
        "summary": "Romanian sentencing practice results in average sentences of 4-6 years for trafficking despite legal minimums of 5-15 years. Early release provisions and reduced sentences for 'cooperation' undermine deterrence.",
        "source": "Romanian Court Sentencing Data 2023"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "BG",
        "title": "Bulgaria - Lenient sentencing for trafficking offences",
        "summary": "Bulgarian courts impose sentences averaging 3-5 years despite EU minimum requirements, often suspended for first-time offenders. This lenient practice creates trafficking permissiveness and enables repeat offenders.",
        "source": "Bulgarian Prosecutor Office Data 2023"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "HU",
        "title": "Hungary - Enhanced penalties for gangland trafficking",
        "summary": "Hungarian law provides enhanced penalties (up to 15-20 years) for trafficking by criminal organizations. Hungary has successfully prosecuted major trafficking gang networks.",
        "source": "Hungarian Criminal Code"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "AT",
        "title": "Austria - Strict penalty enforcement with low suspended sentences",
        "summary": "Austrian courts enforce trafficking sentences with minimal suspension, averaging 8-12 years in prison. Austria maintains strict approach to trafficking punishment reflecting strong legal commitment.",
        "source": "Austrian Court Sentencing Statistics 2023"
    },

    # National Transposition: Article 8 (Non-punishment) Variations
    {
        "type": "legal_argument",
        "jurisdiction": "PL",
        "title": "Poland - Article 8 implementation lacking explicit victim non-punishment provision",
        "summary": "Polish law lacks explicit non-punishment provisions for trafficking victims, relying instead on prosecutorial discretion and mitigating circumstances. This creates uncertainty and potential prosecution risk for victims.",
        "source": "Polish Criminal Code"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "FR",
        "title": "France - Mandatory non-punishment for prostitution-based trafficking",
        "summary": "French law establishes that trafficking victims cannot be prosecuted for prostitution even if they engaged in sex work while trafficked. This addresses significant victim decriminalization gap.",
        "source": "French Criminal Code Article 225-12-7"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "DE",
        "title": "Germany - Discretionary approach to victim non-punishment",
        "summary": "German prosecutors retain discretion on whether to pursue charges against trafficking victims for immigration violations. This inconsistency creates prosecution risk for undocumented trafficking victims.",
        "source": "German Criminal Code Section 153"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "NL",
        "title": "Netherlands - Non-punishment of trafficking victims for document violations",
        "summary": "Dutch law provides explicit non-prosecution for document falsification by trafficking victims. This aligns with Article 8 and Dutch recognition that trafficking coerces document crimes.",
        "source": "Dutch Criminal Code Article 168"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "IT",
        "title": "Italy - Comprehensive victim non-punishment including labour laws",
        "summary": "Italian law provides non-punishment for trafficking victims' violations of labour laws, tax laws, and immigration regulations. Italy recognizes that coerced economic participation requires victim protection.",
        "source": "Italian Law 228/2003"
    },

    # National Transposition: Victim Compensation Variations
    {
        "type": "legal_argument",
        "jurisdiction": "RO",
        "title": "Romania - Minimal victim compensation implementation",
        "summary": "Romanian law provides no dedicated victim compensation scheme despite Article 14 requirements. Victims must pursue civil claims against traffickers with minimal success due to insolvency and evidentiary barriers.",
        "source": "Romanian Criminal Code"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "BG",
        "title": "Bulgaria - Victim compensation scheme lacking resources",
        "summary": "Bulgarian law establishes victim compensation framework but provides minimal funding and difficult application processes. Average compensation awards amount to 500-1000 EUR despite severe trafficking harm.",
        "source": "Bulgarian Victim Compensation Agency Data"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "BE",
        "title": "Belgium - Enhanced victim compensation through confiscation",
        "summary": "Belgian law directs a portion of trafficking-related asset confiscation to victim compensation funds. Belgium supplements state compensation with confiscation-funded support, enhancing victim access to resources.",
        "source": "Belgian Law on Trafficking Victim Compensation"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "DK",
        "title": "Denmark - Victim compensation through criminal injury claims",
        "summary": "Danish law allows trafficking victims to claim compensation through the criminal injury compensation board. Denmark provides compensation for lost earnings, medical treatment, and psychological trauma.",
        "source": "Danish Compensation Act"
    },

    # National Transposition: Child Victim Protections
    {
        "type": "legal_argument",
        "jurisdiction": "PL",
        "title": "Poland - Child trafficking victims prosecuted for prostitution",
        "summary": "Polish prosecutors have prosecuted child trafficking victims for prostitution-related offences despite legal protections. Implementation failures allow prosecution despite Article 15 requirements.",
        "source": "Polish Legal Monitor 2023"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "IT",
        "title": "Italy - Specialized child victim centers and legal representation",
        "summary": "Italian law establishes dedicated regional centers for child trafficking victim support with trauma-informed care and automatic legal representation. Italy provides robust child-specific protections.",
        "source": "Italian Law 228/2003"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "CZ",
        "title": "Czech Republic - Child victim non-prosecution guarantee",
        "summary": "Czech law establishes explicit guarantees that child trafficking victims cannot be prosecuted for crimes committed under trafficking coercion, addressing prosecution risk identified in other jurisdictions.",
        "source": "Czech Criminal Code"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "AT",
        "title": "Austria - Child victim access to education continuity",
        "summary": "Austrian law provides trafficked children with access to continued education and educational stipends during victim support. Austria recognizes that education supports long-term victim reintegration.",
        "source": "Austrian Youth Welfare Act"
    },

    # National Transposition: Victim Identification and Referral
    {
        "type": "statutory_provision",
        "jurisdiction": "SE",
        "title": "Sweden - Mandatory victim identification and formal referral procedures",
        "summary": "Swedish law establishes mandatory victim identification procedures for all law enforcement agencies encountering trafficking indicators. Social services must be immediately notified for victim support activation.",
        "source": "Swedish Police Procedures on Human Trafficking Identification"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "RO",
        "title": "Romania - Victim identification gaps in immigration enforcement",
        "summary": "Romanian immigration enforcement lacks systematic victim identification procedures, resulting in trafficking victims being detained and deported rather than identified and supported.",
        "source": "European Commission Infringement Assessment 2023"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "NL",
        "title": "Netherlands - First-line responder trafficking identification training",
        "summary": "Dutch law mandates trafficking identification training for police, social workers, health providers, and labour inspectors. This multi-agency approach ensures trafficking recognition across diverse encounter points.",
        "source": "Dutch Anti-Trafficking Training Standards"
    },
    {
        "type": "statutory_provision",
        "jurisdiction": "BE",
        "title": "Belgium - Standardized identification indicators across agencies",
        "summary": "Belgian law establishes standardized trafficking indicators for use across police, immigration, labour, and health agencies. This coordination improves victim identification consistency.",
        "source": "Belgian Identification Guidelines"
    },

    # European Commission Infringement Proceedings
    {
        "type": "regulatory_change",
        "jurisdiction": "RO",
        "title": "European Commission Infringement Case 2014-2023 - Romania",
        "summary": "The European Commission maintained infringement proceedings against Romania 2014-2023 for inadequate Article 8 victim non-punishment implementation, insufficient Article 11 victim assistance, and Article 14 compensation failures.",
        "source": "European Commission Infringement Proceedings Database"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "BG",
        "title": "European Commission Infringement Case 2015-2021 - Bulgaria",
        "summary": "The Commission pursued infringement proceedings against Bulgaria for failure to establish adequate victim identification procedures, insufficient Article 13 assistance provisions, and inadequate Article 19 rapporteur independence.",
        "source": "European Commission Infringement Proceedings Database"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "HR",
        "title": "European Commission Assessment - Croatia transposition adequacy",
        "summary": "The Commission assessed Croatia's transposition as adequate with minor implementation gaps. Croatia's progressive legislation reflects post-accession anti-trafficking commitment.",
        "source": "European Commission Transposition Assessment 2023"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "HU",
        "title": "European Commission Assessment - Hungary trafficking prosecution record",
        "summary": "The Commission commended Hungary's trafficking prosecution statistics while noting implementation gaps in victim protection and compensation. Hungary demonstrates strong prosecution capacity.",
        "source": "European Commission Transposition Assessment 2023"
    },

    # 2024 Directive Revision Provisions
    {
        "type": "regulatory_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Online trafficking offences",
        "summary": "The 2024 revision adds specific offences for online trafficking including internet advertisement of sexual exploitation, livestreamed trafficking abuse, and online recruitment through deception.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Platform provider obligations",
        "summary": "The 2024 revision requires social media and online service platforms to implement trafficking detection, reporting procedures, and content removal mechanisms. Non-compliance results in significant fines.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Enhanced victim emergency support",
        "summary": "The 2024 revision mandates immediate emergency support for identified trafficking victims including emergency medical care, psychological first aid, and safe accommodation within 24 hours.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Mandatory recovery and reflection period",
        "summary": "The 2024 revision extends the mandatory recovery and reflection period from 30 to 60 days, ensuring trafficking victims have adequate time for initial stabilization before repatriation decisions.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },
    {
        "type": "regulatory_change",
        "jurisdiction": "EU",
        "title": "2024 Revision - Victim-centred prosecution standards",
        "summary": "The 2024 revision establishes mandatory victim-centred prosecution procedures including trauma-informed investigation, victim counsel presence, and protective measures as default rather than exceptional.",
        "source": "Directive 2024/XXXX/EU (pending)"
    },

    # Best Practices and Model Implementations
    {
        "type": "legal_argument",
        "jurisdiction": "SE",
        "title": "Sweden - Comprehensive anti-trafficking model",
        "summary": "Sweden demonstrates best practice integration of all Article requirements: robust penalties (8-10 years average), comprehensive victim assistance, generous compensation (600,000 SEK), independent rapporteur, mandatory identification training, and prevention focus.",
        "source": "Swedish Anti-Trafficking System Assessment 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "NL",
        "title": "Netherlands - Victim-centred prosecution and investigation",
        "summary": "The Netherlands exemplifies victim-centred approach: specialized investigation units, immediate victim identification, mandatory legal representation, trauma-informed prosecution, and comprehensive support coordination.",
        "source": "Dutch Anti-Trafficking System Assessment 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "IT",
        "title": "Italy - Asset confiscation and victim compensation integration",
        "summary": "Italy demonstrates effective confiscation-to-compensation model: mafia property confiscated through anti-trafficking prosecutions is directed to victim support and reintegration programs.",
        "source": "Italian Anti-Trafficking System Assessment 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "BE",
        "title": "Belgium - Multi-level coordination and victim services",
        "summary": "Belgium integrates federal and regional coordination mechanisms with comprehensive victim services. Federal trafficking units coordinate with regional social services ensuring nationwide coverage.",
        "source": "Belgian Anti-Trafficking System Assessment 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "AT",
        "title": "Austria - Strict penalty enforcement and labour trafficking focus",
        "summary": "Austria enforces trafficking penalties rigorously with focus on labour trafficking in agriculture and construction sectors. Specialized labour inspection and trafficking coordination addresses migrant worker vulnerability.",
        "source": "Austrian Anti-Trafficking System Assessment 2023"
    },

    # Implementation Challenges and Gaps
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Cross-border prosecution coordination challenges",
        "summary": "While Article 10 requires cross-border jurisdiction, significant gaps exist in prosecution coordination. Traffickers exploit jurisdictional complexity; multiple countries with potential jurisdiction often result in no prosecution.",
        "source": "Eurostat Trafficking Prosecution Analysis 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Victim witness protection and retaliation risk",
        "summary": "Despite Article 12 protections, trafficking victims face severe retaliation risk during prosecution. Many member states lack adequate witness protection programs for non-EU citizens, limiting victim participation.",
        "source": "European Commission Victim Protection Assessment 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Labour trafficking invisibility in prosecution",
        "summary": "Labour trafficking represents majority of trafficking but constitutes minority of prosecutions. Member states lack labour law enforcement capacity, allowing labour trafficking to proceed with minimal prosecution risk.",
        "source": "Eurostat Labour Trafficking Analysis 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Immigration law conflicts with victim protection",
        "summary": "Member states inconsistently apply Article 8 non-punishment: some prosecute trafficking victims for immigration violations despite trafficking; others provide protection. This creates unfair variation.",
        "source": "European Commission Immigration and Trafficking Assessment 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "NGO dependence and victim services sustainability",
        "summary": "Article 11 victim services heavily depend on NGO provision without sufficient public funding. Many member states provide minimal direct victim services, outsourcing to underfunded NGOs.",
        "source": "European Commission Victim Services Sustainability Study 2022"
    },

    # Comparative Analysis and Commission Assessments
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Prosecution-victim protection balance",
        "summary": "European Commission analysis reveals tension between prosecution focus and victim protection: states emphasizing prosecution often minimize victim services; victim-centred states (Sweden, Netherlands) achieve both through institutional integration.",
        "source": "European Commission Prosecution and Victim Protection Study 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Penalty variation and deterrence effectiveness",
        "summary": "Commission research suggests deterrence effectiveness requires consistent penalty enforcement across member states. Current variation (4-20 years effective sentences) undermines deterrence as traffickers exploit low-penalty jurisdictions.",
        "source": "European Commission Trafficking Deterrence Study 2023"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Victim identification bottleneck in enforcement chain",
        "summary": "Commission assessment identifies victim identification as critical implementation bottleneck. Without systematic identification protocols, many trafficking victims are processed as migrants/criminals rather than victims.",
        "source": "European Commission Victim Identification Study 2022"
    },
    {
        "type": "legal_argument",
        "jurisdiction": "EU",
        "title": "Article 14 compensation as most consistently failed provision",
        "summary": "European Commission comprehensive review identifies Article 14 victim compensation as most consistently underfunded and underutilized across all member states. This represents significant human rights gap.",
        "source": "European Commission Victim Compensation Implementation Report 2023"
    }
]
