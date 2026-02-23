"""
Seed facts: Migrant Detention Cases and Immigration Detention as Exploitation Enabler.

Covers: immigration detention as exploitation enabler, Malaysia detention centers,
Libya detention torture, GCC deportation centers, US ICE detention labor,
Thailand IDCs, Australia offshore processing, Greece Moria camp, Japan detention
centers, Saudi deportation camps, detention of trafficking victims, non-punishment
principle violations, alternatives to detention, UNHCR standards, and specific
detention deaths and abuse cases.
"""

MIGRANT_DETENTION_CASE_FACTS: list[dict] = [
    # -----------------------------------------------------------------------
    # Malaysia Detention Centers
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Immigration Detention Centre Deaths (2017-2023)",
        "summary": (
            "Malaysian immigration detention centres held 20,000-40,000 detainees at any "
            "time, including trafficking victims. SUHAKAM documented overcrowding at "
            "300-400% capacity, 527 deaths between 2017-2023, inadequate medical care, and "
            "separation of families. Rohingya refugees and undocumented workers detained "
            "together without screening for trafficking indicators."
        ),
        "source": "SUHAKAM / Human Rights Watch / UNHCR Malaysia",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Lenggeng Immigration Depot Abuse Allegations (2020)",
        "summary": (
            "Detainees at Lenggeng Immigration Depot reported systematic beatings by guards, "
            "denial of medical treatment for skin infections and respiratory illness, and "
            "extortion demands for food and water. Footage leaked in 2020 showed guards "
            "forcing detainees to perform stress positions. More than 30 nationalities were "
            "held, complicating consular access."
        ),
        "source": "Amnesty International Malaysia / Fortify Rights 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Rohingya Boat People Detention and UNHCR Access (2020-2021)",
        "summary": (
            "Following COVID-19 border closures, Malaysia intercepted Rohingya vessels and "
            "detained arrivals in Belantik and other depots without UNHCR access for weeks. "
            "Boats were pushed back without screening for trafficking victims or refugees. "
            "Detained individuals reported being forced to call relatives abroad to pay "
            "informal 'release fees' to agents connected to guards."
        ),
        "source": "UNHCR Malaysia / Fortify Rights 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Operation Benteng Mass Detention (2021)",
        "summary": (
            "Operation Benteng (2021) swept undocumented migrants in Kuala Lumpur, detaining "
            "more than 2,700 people in two days including UNHCR-registered refugees and "
            "trafficking victims mid-rescue. Civil society organizations reported that "
            "trafficking survivors in shelter homes were re-detained during follow-up raids. "
            "No trafficking screening protocol was applied at point of arrest."
        ),
        "source": "UNHCR Malaysia / Amnesty International 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Sabah Detention Centre Overcrowding and Disease (2019)",
        "summary": (
            "Sabah state detention facilities in Keningau and Papar held Indonesian and "
            "Filipino migrants at up to 500% capacity. Tuberculosis outbreaks in 2018-2019 "
            "killed at least 12 detainees. Access by medical NGOs was denied for months. "
            "Trafficking victims from the fishing sector were commingled with general "
            "immigration violators, destroying chain-of-custody evidence needed for prosecution."
        ),
        "source": "Human Rights Watch / Sabah AIDS Action Committee 2019",
    },
    {
        "type": "statute",
        "jurisdiction": "MY",
        "title": "Malaysia — Immigration Act 1959/63: Detention Without Time Limit",
        "summary": (
            "Section 34 of Malaysia's Immigration Act 1959/63 permits administrative "
            "detention of undocumented migrants without a court order and without statutory "
            "time limit, pending deportation. Courts have held that habeas corpus is "
            "unavailable where deportation orders are pending. This legal gap enables "
            "indefinite detention and removes safeguards against detaining trafficking victims."
        ),
        "source": "Immigration Act 1959/63 s.34; Subramaniam v. Pengurus IDC [2019] MLJ",
    },

    # -----------------------------------------------------------------------
    # Libya Detention Torture
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "LY",
        "title": "Libya — DCIM Detention Centres: Systematic Torture (2017-2023)",
        "summary": (
            "Migrants held by Libya's Department for Combating Illegal Migration (DCIM) "
            "endured torture, sexual violence, and ransom extortion. OHCHR documented "
            "crimes against humanity in Zintan, Abu Salim, and Al-Kararim. Detention was "
            "indefinite, conditions fatal; at least 2,000 deaths documented 2017-2023. "
            "EU-funded Coast Guard returns delivered migrants directly to these facilities."
        ),
        "source": "OHCHR Libya / Amnesty International 2023 / MSF",
    },
    {
        "type": "case_study",
        "jurisdiction": "LY",
        "title": "Libya — Zawiya Detention Centre and Militia Profiteering",
        "summary": (
            "Zawiya detention centre, nominally under DCIM authority, was controlled by the "
            "Nasr trafficking network. Detainees were sold to smugglers, subjected to ransom "
            "calls extorted via phone at gunpoint, and made to perform forced labor on "
            "fishing boats and farms. ICC investigations named specific militia commanders "
            "for crimes including enslavement."
        ),
        "source": "UN Panel of Experts Libya 2021 / ICC OTP Preliminary Examination 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "LY",
        "title": "Libya — Tajoura Detention Centre Airstrike (2019)",
        "summary": (
            "An airstrike on Tajoura detention centre on 2 July 2019 killed at least 53 "
            "migrants. UNHCR had repeatedly requested the evacuation of refugees from the "
            "facility, which was adjacent to a weapons depot. Survivors reported that guards "
            "prevented escape by firing on detainees fleeing. The incident was characterized "
            "by OHCHR as a potential war crime."
        ),
        "source": "UNHCR / OHCHR July 2019 / Human Rights Watch",
    },
    {
        "type": "case_study",
        "jurisdiction": "LY",
        "title": "Libya — EU-Funded Interception and Return to Detention (2016-2023)",
        "summary": (
            "Italian and EU funding under Operation Sophia and subsequent arrangements "
            "trained and equipped the Libyan Coast Guard, which intercepted 80,000+ migrants "
            "2017-2021 and returned them to DCIM detention. OHCHR concluded these returns "
            "violated the non-refoulement principle. Intercepted persons included recognized "
            "trafficking victims, unaccompanied children, and pregnant women."
        ),
        "source": "OHCHR 2021 / EU Parliament Resolution 2022/2024(INI)",
    },
    {
        "type": "case_study",
        "jurisdiction": "LY",
        "title": "Libya — Open Markets for Enslaved Migrants (2017)",
        "summary": (
            "CNN footage broadcast in November 2017 showed Nigerian men being auctioned as "
            "agricultural laborers outside Tripoli for USD 400. The CNN investigation traced "
            "victims to migrants who had been processed through DCIM detention, where brokers "
            "purchased persons directly from guards. The footage precipitated an AU-EU "
            "emergency summit but structural conditions remained unchanged."
        ),
        "source": "CNN Investigation November 2017 / AU-EU Valletta Taskforce Report 2018",
    },
    {
        "type": "case_study",
        "jurisdiction": "LY",
        "title": "Libya — Female Detainees: Sexual Violence and Trafficking in Detention",
        "summary": (
            "OHCHR documented that female detainees in Sheba, Bani Walid, and Al-Nasr "
            "facilities were systematically sexually assaulted by guards and trafficked to "
            "informal brothels under guard escort, then returned to detention. Women who "
            "became pregnant were denied abortion and medical care. Witnesses testified "
            "before the HRC in 2021 and 2023."
        ),
        "source": "OHCHR HRC46 2021 / Médecins Sans Frontières Libya Report 2022",
    },

    # -----------------------------------------------------------------------
    # GCC Deportation Centers
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Deportation Camps: Ethiopian Worker Mass Detention (2022-2023)",
        "summary": (
            "Human Rights Watch documented Ethiopian migrants held in Saudi deportation "
            "holding centers in conditions it characterized as inhumane — overcrowding, "
            "violence by guards, and insufficient food. Over 30,000 Ethiopians were held "
            "as of mid-2023 in facilities near Riyadh and Jeddah. Deaths were documented "
            "and bodies returned without cause-of-death documentation."
        ),
        "source": "Human Rights Watch April 2023 / IOM Ethiopia 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Al-Shumaisi Detention Facility Conditions (2013-2020)",
        "summary": (
            "Al-Shumaisi facility in Riyadh held tens of thousands of undocumented Ethiopian "
            "and Somali migrants. Survivors described mass beatings, forced labor cleaning "
            "the compound, and denial of medical care for injuries sustained during arrest. "
            "UNHCR was denied systematic access. Trafficking victims fleeing kafala employers "
            "were detained as immigration violators without screening."
        ),
        "source": "Human Rights Watch 2020 / IOM Voluntary Humanitarian Return Reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "AE",
        "title": "UAE — Al Wathba Deportation Centre and Labour Migrant Detention",
        "summary": (
            "Al Wathba deportation centre in Abu Dhabi held construction and domestic workers "
            "who had overstayed or been abandoned by sponsors. Detainees were held for "
            "90-270 days awaiting deportation. Human rights groups documented denial of "
            "communication with consulates, debt bondage continuation as detainees signed "
            "waivers of unpaid wages as condition of release, and physical abuse."
        ),
        "source": "Migrant-Rights.org 2018 / ILO GCC Labour Migration Report 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "QA",
        "title": "Qatar — Al-Duhail Detention Centre and Kafala Victim Detention",
        "summary": (
            "Workers who fled abusive kafala employers and reported to labour authorities "
            "were detained at Al-Duhail pending employer 'release'. Those without employer "
            "consent faced indefinite detention despite Qatar's 2020 kafala reform. "
            "Amnesty International documented cases of trafficking victims detained alongside "
            "immigration violators; no trafficking screening procedure existed at the centre."
        ),
        "source": "Amnesty International Qatar 2021 / Migrant-Rights.org",
    },
    {
        "type": "case_study",
        "jurisdiction": "KW",
        "title": "Kuwait — Talha Deportation Centre: Domestic Worker Confinement",
        "summary": (
            "Domestic workers who fled employers were held in Talha deportation centre, "
            "sometimes for more than six months, because deportation required employer "
            "consent under kafala rules. Workers reported theft of personal documents by "
            "guards, forced labor within the facility, and sexual assault. Philippine and "
            "Indonesian embassies documented cases but lacked authority to secure release."
        ),
        "source": "Philippine Overseas Labour Office Kuwait 2019 / Human Rights Watch 2020",
    },

    # -----------------------------------------------------------------------
    # US ICE Detention Labor
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Forced Labor in ICE Detention: Adelanto Class Action (2017-2023)",
        "summary": (
            "A federal class-action lawsuit (Novoa v. The GEO Group) alleged that private "
            "prison operator GEO Group paid detainees at Adelanto ICE Processing Centre "
            "USD 1-3 per day for maintenance work under threat of solitary confinement, "
            "in violation of the Trafficking Victims Protection Act. A jury found GEO liable "
            "for unjust enrichment in 2023, awarding USD 23.5 million in back pay."
        ),
        "source": "Novoa v. GEO Group, No. 5:17-cv-02514 (C.D. Cal. 2023) / ACLU",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Irwin County Detention Centre: Medical Abuse and Forced Hysterectomies (2020)",
        "summary": (
            "A whistleblower complaint filed in September 2020 alleged that a gynaecologist "
            "at Irwin County Detention Centre performed unnecessary hysterectomies on "
            "immigrant women without informed consent. DHS OIG confirmed multiple procedural "
            "violations. The facility, operated by LaSalle Corrections, was closed in 2021. "
            "Congress introduced the CARE Act in response but it was not enacted."
        ),
        "source": "DHS OIG Report OIG-21-46 / Project South Whistleblower Complaint 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — ICE Detention Deaths: 200+ Deaths 2004-2023",
        "summary": (
            "ICE reported 240 deaths in immigration detention 2004-2023, with advocacy groups "
            "documenting additional deaths not on official lists. Recurring causes: delayed "
            "medical care, inadequate mental health treatment, and COVID-19 (34 deaths "
            "2020-2021). DHS OIG repeatedly found systemic inadequacy of medical care at "
            "privately operated facilities. No guard has been criminally prosecuted for a "
            "detainee death."
        ),
        "source": "ACLU / Freedom for Immigrants / ICE Detainee Death Reports 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Northwest Detention Centre Hunger Strike and Forced Labour (2014-2017)",
        "summary": (
            "Detainees at the Northwest Detention Centre in Tacoma (operated by GEO Group) "
            "conducted hunger strikes in 2014, 2015, and 2017 to protest USD 1/day 'voluntary' "
            "work program labor, inadequate food, and deportation conditions. Washington State "
            "later passed a law prohibiting forced labor in private detention facilities "
            "(SB 5432, enacted 2021), the first such state law in the US."
        ),
        "source": "Community Justice Project / Washington SB 5432 (2021) / NWDC Resistance",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Trafficking Victims Detained Despite T-Visa Applications",
        "summary": (
            "The Government Accountability Office (GAO-18-223) found that ICE detained "
            "persons with pending T-visa (trafficking victim) applications, including cases "
            "where detention lasted more than 90 days post-certification. DHS lacked a "
            "centralized mechanism to flag T-visa applicants for release. Advocates documented "
            "cases where traffickers' continued control over victims was facilitated by "
            "victim detention."
        ),
        "source": "GAO-18-223 (2018) / National Immigrant Justice Center 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Hutto Immigration Detention Centre: Families in Prison Conditions (2006-2009)",
        "summary": (
            "T. Don Hutto Residential Centre (operated by CCA, now CoreCivic) held asylum-"
            "seeking families including children as young as infants in prison-like conditions: "
            "uniforms, 12-hour lockdowns, inadequate schooling, and punitive treatment of "
            "children who cried. A 2007 ACLU settlement forced reforms. The facility later "
            "became an all-female adult detention centre. The case established baseline "
            "standards for family detention."
        ),
        "source": "ACLU Settlement Flores v. Reno / Hutto Reports 2007 / HRW 2007",
    },

    # -----------------------------------------------------------------------
    # Thailand Immigration Detention Centres (IDCs)
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand — Immigration Detention Centre Bangkok: Protracted Rohingya Detention",
        "summary": (
            "Rohingya men, women, and children intercepted at sea were held in Bangkok IDC "
            "for periods exceeding three years without charge or access to asylum procedures. "
            "UNHCR was denied access until 2016. Overcrowding reached 700% in 2015; "
            "detainees reported guards selling food, extorting money for phone access, and "
            "forcing male detainees to clean holding areas without pay. At least 14 deaths "
            "documented 2014-2019."
        ),
        "source": "Human Rights Watch 2016 / UNHCR Thailand / Fortify Rights 2015",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand — IDC System: Indefinite Detention Without Legal Basis",
        "summary": (
            "Thailand's Immigration Act B.E. 2522 (1979) permits detention of undocumented "
            "migrants without time limit. In practice, stateless persons and those without "
            "travel documents have been held for 5-10 years. The UN Working Group on "
            "Arbitrary Detention issued opinions finding Thailand in violation in multiple "
            "cases. No independent judicial review mechanism exists for IDC detention orders."
        ),
        "source": "WGAD Opinions A/HRC/WGAD/2018/31; 2019/14; 2022/8 / UNHCR Thailand",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand — Trafficking Victims Re-Detained After Rescue (2014-2019)",
        "summary": (
            "Following Operation Liberator (2014) and subsequent anti-trafficking raids, "
            "trafficking victims rescued from fishing vessels and broiler farms were held "
            "in Ministry of Social Development shelters that functioned as closed detention: "
            "locked gates, no freedom of movement, and testimony recorded only in Thai. "
            "Victims who sought to leave before legal proceedings concluded were reclassified "
            "as immigration violators and transferred to IDCs."
        ),
        "source": "Environmental Justice Foundation 2015 / Fortify Rights 2016",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand — Nong Khai IDC: COVID-19 Outbreak and Deaths (2021)",
        "summary": (
            "A COVID-19 outbreak at Nong Khai IDC in 2021 infected 300+ detainees held in "
            "shared dormitories without adequate ventilation. Two detainees died. UNHCR "
            "urged the release of vulnerable persons but Thai authorities declined, citing "
            "public health containment. No detainees were vaccinated during the initial "
            "outbreak period."
        ),
        "source": "UNHCR Thailand Press Release 2021 / Human Rights Watch August 2021",
    },

    # -----------------------------------------------------------------------
    # Australia Offshore Processing
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia — Manus Island Detention: PNG Supreme Court Ruling (2016)",
        "summary": (
            "The Papua New Guinea Supreme Court ruled in April 2016 that Australia's detention "
            "of asylum seekers on Manus Island violated PNG's constitution. Australia "
            "announced closure of the centre but continued detention for two more years. "
            "At least four detainees died 2014-2017, including Reza Barati (killed by guards "
            "in 2014) and Hamid Khazaei (died of sepsis after preventable wound). Coroner's "
            "inquest found systemic medical failures."
        ),
        "source": "PNG Supreme Court SCR No. 1 of 2016 / Queensland Coroner's Court 2016",
    },
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia — Nauru Offshore Processing: Child Abuse and Mental Health Crisis",
        "summary": (
            "The Nauru Files (leaked to The Guardian in 2016) contained 2,000+ incident "
            "reports documenting sexual assault, self-harm, attempted suicide, and child "
            "abuse in Australian-operated offshore processing. The Australian Human Rights "
            "Commission (The Forgotten Children, 2014) found that prolonged detention caused "
            "irreversible mental harm to children. Australia paid AUD 70 million in a class "
            "settlement to 1,905 former Manus/Nauru detainees in 2017."
        ),
        "source": "AHRC 2014 / The Guardian Nauru Files 2016 / Leeuwangh v. Commonwealth 2017",
    },
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia — Operation Sovereign Borders: Illegal Maritime Turnbacks",
        "summary": (
            "Since 2013, Australia's Operation Sovereign Borders has turned back or towed "
            "asylum seeker vessels to Indonesia and Sri Lanka. The UN Special Rapporteur on "
            "Torture found that turnbacks without screening constitute collective expulsion "
            "and refoulement. Trafficking victims on intercepted vessels could not access "
            "asylum procedures. At least two people died during turnback operations."
        ),
        "source": "UNHCR / UNSR Torture Report A/HRC/28/68/Add.1 2015 / HRLC 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia — Transfield (Broadspectrum) Contractor Accountability: Nauru (2015-2017)",
        "summary": (
            "ASX-listed Broadspectrum (formerly Transfield Services) managed Nauru detention "
            "under contract and was implicated in failure to report abuse and prevent harm. "
            "Shareholder activism led to a 50%+ protest vote at its 2015 AGM. The company "
            "exited the contract in 2017 after reputational damage. The incident established "
            "that corporate contractors bear responsibility for conditions in outsourced "
            "immigration detention."
        ),
        "source": "Transfield AGM Protest Reports 2015 / Asylum Seeker Resource Centre 2017",
    },

    # -----------------------------------------------------------------------
    # Greece — Moria Camp
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Greece — Moria Camp: Collapse of Humanitarian Standards (2019-2020)",
        "summary": (
            "By September 2020, Moria camp on Lesbos held 12,700 people in facilities "
            "designed for 3,000. MSF described conditions as a public health emergency: "
            "one toilet per 72 people, open sewage, and violence including rape. At least "
            "20 deaths in the camp 2016-2020. A fire destroyed Moria in September 2020, "
            "leaving 13,000 refugees homeless overnight. No individual accountability was "
            "established for conditions leading to the fire."
        ),
        "source": "MSF Moria Reports 2019-2020 / UNHCR Greece / Human Rights Watch 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Greece — Evros Pushbacks and Detention: ECHR Provisional Measures Ignored",
        "summary": (
            "The European Court of Human Rights issued Rule 39 provisional measures in "
            "multiple Evros cases requiring Greece not to expel applicants, but documented "
            "cases showed continued pushbacks. Migrants detained at Fylakio pre-removal "
            "centre reported violence by masked officers and deportation to Turkey without "
            "asylum screening. The Council of Europe's CPT found inhuman treatment in 2020."
        ),
        "source": "ECHR Rule 39 Applications 2020-2022 / CPT/Inf(2020)17 / HRW 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Greece — Kleidi Pre-Departure Centre: Trafficking Victims Among Detainees",
        "summary": (
            "A 2021 GRETA (Council of Europe anti-trafficking body) report found that Greek "
            "authorities detained potential trafficking victims at Kleidi and Corinth "
            "pre-departure centres without systematic screening. Victims who self-identified "
            "were not always referred to NRM procedures. Detention disrupted ongoing "
            "trafficking investigations by removing witnesses from investigator access."
        ),
        "source": "GRETA(2021)01 Third Evaluation Round: Greece / CoE Anti-Trafficking Division",
    },
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Greece — Petrou Ralli Detention Centre: Human Rights Violations (2012-2021)",
        "summary": (
            "Petrou Ralli, Athens' main adult pre-removal centre, was documented by CPT (2013, "
            "2016, 2019) as holding detainees in overcrowded, dirty, poorly ventilated cells "
            "with inadequate outdoor exercise and no meaningful access to legal aid. Suicides "
            "and suicide attempts were frequent. Individuals with mental illness were detained "
            "rather than referred to psychiatric services."
        ),
        "source": "CPT/Inf(2014)26; CPT/Inf(2016)4; CPT/Inf(2020)15 / Médecins du Monde",
    },

    # -----------------------------------------------------------------------
    # Japan Detention Centers
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "Japan — Immigration Detention: Deaths from Medical Neglect (2019-2021)",
        "summary": (
            "A Sri Lankan woman, Ratnayake Liyanage Wishma Sandamali, died in Nagoya Regional "
            "Immigration Services Bureau in March 2021 after 2.5 months of detention despite "
            "multiple requests for medical release. Footage released by a court order showed "
            "guards dismissing her symptoms. Japan subsequently amended the Immigration "
            "Control Act (2023) but critics argued reforms fell short of addressing indefinite "
            "detention."
        ),
        "source": "Ministry of Justice Investigation Report 2021 / Nyukan Mondai Forum 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "Japan — Indefinite Detention: UN Working Group on Arbitrary Detention Opinions",
        "summary": (
            "The UN Working Group on Arbitrary Detention issued multiple opinions against "
            "Japan for detaining persons with denied asylum applications for periods of "
            "2-10+ years without judicial review (Opinions 2016/18, 2018/42, 2021/31). "
            "Japan's detention lacks a statutory time limit and judicial authorization "
            "requirement. Hunger strikes by long-term detainees were documented at Tokyo, "
            "Osaka, Omura, and Higashi-Hiroshima facilities."
        ),
        "source": "WGAD Opinions / Japan Federation of Bar Associations 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "Japan — Trafficking Victim Detention: Failed NRM Integration",
        "summary": (
            "Japan's National Plan of Action on Trafficking acknowledged that trafficking "
            "victims could be detained as immigration violators, but screening at Regional "
            "Immigration Services Bureaus remained inadequate. JNATIP documented cases where "
            "Vietnamese technical intern trainees who had escaped forced labor were detained "
            "and deported before trafficking cases could be investigated."
        ),
        "source": "JNATIP / US TIP Report Japan 2022 / IOM Japan",
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "Japan — Omura Immigration Centre: Forced Feeding Controversy (2019)",
        "summary": (
            "A Nigerian asylum seeker was forcibly tube-fed at Omura Immigration Centre after "
            "a prolonged hunger strike in 2019. UNHCR and medical ethicists objected that "
            "forced feeding in this context constituted ill-treatment. The individual had been "
            "detained for over three years. Public attention to this case contributed to "
            "parliamentary debate on detention reform."
        ),
        "source": "UNHCR Japan Statement 2019 / Asahi Shimbun Investigation 2019",
    },

    # -----------------------------------------------------------------------
    # Saudi Arabia Deportation Camps
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — Ethiopian Deportation: 'Spider Warehouses' Abuse (2013)",
        "summary": (
            "Human Rights Watch documented in 2013 that Ethiopian migrants held in Saudi "
            "deportation holding areas called 'spider houses' (due to multiple interconnected "
            "cells) experienced beatings, sexual assault by guards, and theft. More than "
            "160,000 Ethiopians were deported in a six-month period; deportation flights "
            "were reported as dangerously overcrowded. Trafficking victims were not screened "
            "before deportation, destroying ongoing criminal investigations."
        ),
        "source": "Human Rights Watch 'Saudi Arabia: Migrant Workers at Risk' 2013",
    },
    {
        "type": "case_study",
        "jurisdiction": "SA",
        "title": "Saudi Arabia — 2023 Mass Deportation of Ethiopians: Scale and Conditions",
        "summary": (
            "Saudi Arabia deported approximately 150,000 Ethiopian migrants between January "
            "and June 2023 in what HRW called the largest Ethiopian deportation in history. "
            "Deportees reported holding conditions in Jizan and Najran border areas with "
            "no food for 48 hours, violence, and forced signing of deportation documents "
            "in Arabic they could not read. Multiple deaths were documented during transport."
        ),
        "source": "Human Rights Watch April 2023 / IOM Ethiopia / Addis Standard 2023",
    },

    # -----------------------------------------------------------------------
    # Detention of Trafficking Victims
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "GLOBAL",
        "title": "Global — Trafficking Victim Detention: UNODC Prevalence Data",
        "summary": (
            "UNODC's Global Report on Trafficking in Persons (2020, 2022) found that in "
            "surveyed countries, between 20-40% of identified trafficking victims had prior "
            "immigration detention records, suggesting significant rates of victim-perpetrator "
            "confusion by authorities. States with mandatory detention policies showed higher "
            "victim under-identification rates. The report recommended integrating NRM "
            "referral into all immigration detention intake procedures."
        ),
        "source": "UNODC Global Report on Trafficking in Persons 2020 / 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "GB",
        "title": "UK — Home Office Detained Trafficking Victims: Shaw Review Findings (2016)",
        "summary": (
            "The Shaw Review (2016) commissioned by the UK Home Office found that the NRM "
            "was systematically failing to identify trafficking victims in immigration "
            "detention, that victims were detained for extended periods after identification, "
            "and that the 'Adults at Risk' policy was not functioning as intended. The review "
            "recommended time limits on detention; the government accepted recommendations "
            "in principle but implementation was slow."
        ),
        "source": "Shaw Review 'Review into the Welfare in Detention of Vulnerable Persons' 2016",
    },
    {
        "type": "case_study",
        "jurisdiction": "GB",
        "title": "UK — Yarl's Wood: Trafficking Victim Detention and Sexual Exploitation (2015)",
        "summary": (
            "A Channel 4 undercover investigation at Yarl's Wood Immigration Removal Centre "
            "(2015) documented a guard engaged in sexual activity with a detainee. Subsequent "
            "investigation found that trafficking victims had been held at Yarl's Wood for "
            "months after NRM positive conclusive grounds decisions. Serco (the operator) "
            "was subsequently warned for contract violations. The facility became a focal "
            "point for UK immigration detention reform advocacy."
        ),
        "source": "Channel 4 Dispatches 2015 / HMIP Yarl's Wood Report 2015",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Italy — CPR Detention Centres: Trafficking Victim Non-Identification",
        "summary": (
            "GRETA's 2023 evaluation of Italy found that persons held in Centri di Permanenza "
            "per i Rimpatri (CPR) were rarely screened for trafficking indicators, that "
            "legal aid provision was inadequate, and that several persons with NRM referrals "
            "were deported before reflection-period decisions were issued. The CPT's 2023 "
            "visit documented violence by guards in at least three CPRs."
        ),
        "source": "GRETA(2023)10 Third Evaluation Round: Italy / CPT/Inf(2023)37",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Trafficking Victims in ICE Custody: T-Visa Detention Problem",
        "summary": (
            "The Polaris Project documented in 2018 that ICE detention of potential trafficking "
            "victims prevented timely T-visa certification by law enforcement agencies, because "
            "certifying agencies could not access detainees without ICE facilitation. ICE "
            "policy required detainees to be released only to verified shelter, creating a "
            "circular barrier for those without NGO placement. Congress investigated but "
            "did not legislate a fix."
        ),
        "source": "Polaris Project 2018 / ATEST Congressional Testimony 2018",
    },

    # -----------------------------------------------------------------------
    # Non-Punishment Principle Violations
    # -----------------------------------------------------------------------
    {
        "type": "statute",
        "jurisdiction": "INTERNATIONAL",
        "title": "Palermo Protocol — Non-Punishment Principle: Article 7 Obligations",
        "summary": (
            "While the Palermo Protocol does not explicitly codify a non-punishment provision, "
            "UNODC, OHCHR, and the UNCTOC Conference of Parties have interpreted Article 7 "
            "(status of victims) and Article 8 (repatriation) as implicitly prohibiting "
            "criminalization and detention of trafficking victims for acts committed as a "
            "direct result of trafficking. The Model Law against Trafficking (UNODC 2009) "
            "includes an explicit non-punishment clause in Section 10."
        ),
        "source": "UNODC Model Law 2009 / OHCHR Commentary on the Palermo Protocol",
    },
    {
        "type": "statute",
        "jurisdiction": "EU",
        "title": "EU Anti-Trafficking Directive 2011/36/EU — Non-Prosecution Provision",
        "summary": (
            "Article 8 of EU Directive 2011/36/EU requires Member States to take measures "
            "to establish the possibility of not prosecuting or imposing penalties on victims "
            "of trafficking for their involvement in criminal activities they were compelled "
            "to commit. GRETA's monitoring has found widespread non-implementation, with "
            "multiple states still prosecuting victims for document offences, irregular "
            "migration, and prostitution-related offences."
        ),
        "source": "Directive 2011/36/EU Art.8 / GRETA Evaluation Rounds 2014-2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "GB",
        "title": "UK — Section 45 Modern Slavery Act 2015: Non-Punishment Defence in Practice",
        "summary": (
            "Section 45 of the Modern Slavery Act 2015 provides a statutory defence for "
            "trafficking victims who committed an offence as a direct consequence of being "
            "trafficked. But HMICFRS (2017) and the Independent Anti-Slavery Commissioner "
            "(2019) found police frequently failed to consider the defence before charging. "
            "The majority of s.45 defences were raised by defendants in criminal proceedings "
            "rather than identified by prosecutors pre-charge."
        ),
        "source": "Modern Slavery Act 2015 s.45 / HMICFRS 2017 / IASC Annual Report 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand — Fishing Vessel Trafficking Victims Prosecuted for Document Offences",
        "summary": (
            "Following the 2014 forced labor and trafficking exposés in the Thai fishing "
            "industry, some Cambodian and Burmese victims rescued from fishing boats were "
            "charged with illegal entry under Thailand's Immigration Act. NGOs including "
            "Environmental Justice Foundation documented cases where charging decisions were "
            "made before trafficking screening was completed, violating the non-punishment "
            "principle and chilling victim cooperation with investigators."
        ),
        "source": "Environmental Justice Foundation 2015 / Fortify Rights 2016",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Sex Trafficking Victims Prosecuted for Prostitution: GEMS Data (2012-2019)",
        "summary": (
            "Girls Educational and Mentoring Services (GEMS) documented that trafficking "
            "victims in New York were routinely arrested and prosecuted for prostitution "
            "offences despite state law requiring diversion of minors. Human Trafficking "
            "Courts (established 2013) were intended to address this but adult trafficking "
            "victims continued to face criminal records for survival crimes. ATAVIST "
            "model statutes and Survivors' Justice Acts were subsequently proposed in "
            "multiple states."
        ),
        "source": "GEMS 2012 / Human Trafficking Intervention Courts Report 2019 / ATEST",
    },

    # -----------------------------------------------------------------------
    # Alternatives to Detention
    # -----------------------------------------------------------------------
    {
        "type": "policy_update",
        "jurisdiction": "INTERNATIONAL",
        "title": "UNHCR — Alternatives to Detention: Community Supervision Models",
        "summary": (
            "UNHCR's 2012 Detention Guidelines and 2019 guidance on alternatives to detention "
            "(ATD) outline community supervision, case management, reporting obligations, "
            "electronic monitoring, and shelter-based alternatives. UNHCR's global ATD pilot "
            "programmes in Hungary, Canada, Malaysia, and Kenya showed 90%+ compliance rates "
            "compared to 65-75% for detained groups in managing asylum procedures, at "
            "significantly lower cost per person."
        ),
        "source": "UNHCR Detention Guidelines 2012 / ATD Pilot Programme Evaluations 2019",
    },
    {
        "type": "policy_update",
        "jurisdiction": "AU",
        "title": "Australia — Community Detention: IMAs on Bridging Visas (2011-2013)",
        "summary": (
            "Between 2011 and 2013, Australia released thousands of asylum seekers from "
            "immigration detention into community detention and onto bridging visas with "
            "work rights and basic income support. Compliance with reporting obligations "
            "exceeded 95%. The incoming government reversed community release in 2013. "
            "Cost comparison showed community detention cost AUD 31/day vs. AUD 346/day "
            "for closed detention."
        ),
        "source": "AHRC 2013 / DIBP Community Detention Evaluation 2013 / RCOA",
    },
    {
        "type": "policy_update",
        "jurisdiction": "EU",
        "title": "EU — Reception Conditions Directive 2013/33/EU: Detention as Last Resort",
        "summary": (
            "Article 8 of the recast Reception Conditions Directive requires that Member "
            "States do not detain asylum seekers solely on the basis of their asylum claim "
            "and that detention be used as a last resort. Article 9 requires prompt judicial "
            "review. ECRE and UNHCR have documented widespread Member State non-compliance. "
            "Belgium, France, and Greece were found in violation by the CJEU and ECHR in "
            "multiple cases."
        ),
        "source": "Directive 2013/33/EU Arts. 8-9 / CJEU C-601/15 PPU / MSS v. Belgium",
    },
    {
        "type": "policy_update",
        "jurisdiction": "CA",
        "title": "Canada — CBSA Community Case Management Programme (2018-2023)",
        "summary": (
            "Canada's Canada Border Services Agency piloted the National Alternatives to "
            "Detention Programme, using case management and community supervision for "
            "immigration detainees. An evaluation showed 99% compliance in attending "
            "hearings. The programme reduced average daily detention from 10,700 to 7,900 "
            "beds. Trafficking victim identification improved because case managers had "
            "sustained contact and rapport with participants."
        ),
        "source": "CBSA ATD Evaluation 2022 / Canadian Council for Refugees 2023",
    },
    {
        "type": "policy_update",
        "jurisdiction": "US",
        "title": "USA — ICE Intensive Supervision Appearance Programme (ISAP)",
        "summary": (
            "ICE's ISAP programme uses electronic monitoring and case management as an "
            "alternative to detention. A 2020 Government Accountability Office report "
            "(GAO-20-384) found 99.6% appearance rates for ISAP participants at immigration "
            "hearings. ISAP cost USD 4.50/day per person vs. USD 134/day for detention. "
            "Critics noted ISAP's electronic monitoring could enable trafficker surveillance "
            "of victims if location data was not protected."
        ),
        "source": "GAO-20-384 2020 / DHS ICE ISAP Statistics / AILA 2021",
    },

    # -----------------------------------------------------------------------
    # UNHCR Standards
    # -----------------------------------------------------------------------
    {
        "type": "regulation",
        "jurisdiction": "INTERNATIONAL",
        "title": "UNHCR — Detention Guidelines (2012): Ten Grounds for Permissible Detention",
        "summary": (
            "UNHCR's 2012 Guidelines on Applicable Criteria and Standards relating to "
            "Detention of Asylum-Seekers define detention as permissible only to verify "
            "identity/documentation, to determine claim elements not obtainable otherwise, "
            "where persons absconded or evaded proceedings, or for national security "
            "reasons. All ten permissible grounds include proportionality and necessity "
            "tests. The guidelines explicitly state that trafficking victims should not be "
            "detained pending status determination."
        ),
        "source": "UNHCR Detention Guidelines, February 2012, Rev. 1",
    },
    {
        "type": "regulation",
        "jurisdiction": "INTERNATIONAL",
        "title": "UNHCR — Global Action Plan to End Statelessness 2014-2024: Detention",
        "summary": (
            "Action 7 of UNHCR's Global Action Plan specifically addresses preventing "
            "stateless persons from being arbitrarily detained. Stateless migrants, common "
            "in many trafficking corridors, face indefinite detention because no state will "
            "accept deportation. UNHCR estimated 3.9 million stateless persons globally "
            "as of 2022, with a significant proportion at risk of prolonged detention."
        ),
        "source": "UNHCR Global Action Plan 2014-2024 Action 7 / UNHCR Statelessness Report 2022",
    },
    {
        "type": "regulation",
        "jurisdiction": "INTERNATIONAL",
        "title": "UNHCR — Guidelines on Child Detention: Zero-Tolerance Position (2020)",
        "summary": (
            "UNHCR's 2020 guidelines reiterated that the detention of asylum-seeking and "
            "refugee children is never in a child's best interests and called on states to "
            "adopt a zero-tolerance approach. The guidelines listed reception centres with "
            "movement restrictions as functional detention and therefore covered by the "
            "prohibition. Multiple EU states were found in violation of this standard by "
            "ECHR and GRETA in 2021-2023."
        ),
        "source": "UNHCR Guidelines on Child Detention 2020 / ECHR M.B. and Others v. Slovakia",
    },
    {
        "type": "regulation",
        "jurisdiction": "INTERNATIONAL",
        "title": "UN Nelson Mandela Rules (2015): Minimum Standards for Detention",
        "summary": (
            "The 2015 revised UN Standard Minimum Rules for the Treatment of Prisoners "
            "(Mandela Rules), while drafted for criminal detention, are applied by monitoring "
            "bodies to immigration detention. Key provisions: maximum cell size standards, "
            "access to daylight, medical care by trained personnel, right to communicate "
            "with counsel, prohibition of collective punishment, and ban on prolonged "
            "solitary confinement (>15 days). CPT reports routinely find immigration "
            "detention in violation of these standards."
        ),
        "source": "UNGA Res. 70/175 (2015) Mandela Rules / CPT Standards CPT/Inf/E(2002)1",
    },
    {
        "type": "regulation",
        "jurisdiction": "INTERNATIONAL",
        "title": "OPCAT — Subcommittee on Prevention of Torture: Immigration Detention Mandate",
        "summary": (
            "The Optional Protocol to the Convention Against Torture (OPCAT) established "
            "the SPT and requires states to establish National Preventive Mechanisms (NPMs) "
            "with access to all places of deprivation of liberty, including immigration "
            "detention. As of 2023, 91 states have ratified OPCAT. SPT reports on Libya "
            "(2011) and other states found systemic torture in immigration detention. "
            "Several states have excluded immigration detention from NPM mandates, which "
            "the SPT has found impermissible."
        ),
        "source": "OPCAT Art. 4(1) / SPT Annual Reports 2019-2022 / SPT-Libya Report 2011",
    },

    # -----------------------------------------------------------------------
    # Specific Detention Deaths and Abuse Cases
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "GB",
        "title": "UK — Alois Dvorzac Death in Immigration Removal (2013)",
        "summary": (
            "Alois Dvorzac, a 84-year-old Canadian citizen with dementia, died after being "
            "detained at Harmondsworth Immigration Removal Centre in 2013. He had been held "
            "for six weeks while authorities processed his removal. The subsequent inquest "
            "found the detention was disproportionate and that medical staff failed to "
            "adequately communicate his deteriorating condition. HMIP cited Harmondsworth "
            "for failing to protect elderly and vulnerable detainees."
        ),
        "source": "Harmondsworth Inquest 2014 / HMIP Report Harmondsworth 2014",
    },
    {
        "type": "case_study",
        "jurisdiction": "GB",
        "title": "UK — Jimmy Mubenga Death During Deportation (2010)",
        "summary": (
            "Angolan asylum seeker Jimmy Mubenga died during a deportation flight from the "
            "UK in October 2010 after being restrained by G4S guards. An inquest jury "
            "returned a verdict of unlawful killing in 2013. Three G4S guards were tried "
            "for manslaughter but acquitted. The case led to reform of restraint techniques "
            "used during deportation and increased scrutiny of private security contractors "
            "in immigration enforcement."
        ),
        "source": "Mubenga Inquest 2013 / IPCC Investigation 2012 / HMIP 2011",
    },
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia — Reza Barati Death on Manus Island (2014)",
        "summary": (
            "Iranian asylum seeker Reza Barati was beaten to death by guards and local staff "
            "at the Manus Island Regional Processing Centre on 17 February 2014, during a "
            "riot that authorities had advance warning of. A Papua New Guinea court convicted "
            "two men for the killing but Australian officials overseeing the facility faced "
            "no prosecution. The coroner found the Australian government bore responsibility "
            "for conditions that led to the riot."
        ),
        "source": "PNG National Court Conviction 2016 / Australian Senate Inquiry 2014",
    },
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia — Hamid Khazaei Death from Preventable Sepsis (2014)",
        "summary": (
            "Hamid Khazaei, a 24-year-old Iranian asylum seeker, died in Brisbane in "
            "September 2014 after medical transfer from Manus Island was delayed. He developed "
            "a leg infection that progressed to septicaemia. The Queensland coroner found "
            "that medical care on Manus was inadequate and that transfer delay caused his "
            "death. The coroner made 12 recommendations; the Australian government accepted "
            "seven. No prosecution of responsible officials followed."
        ),
        "source": "Queensland Coroner's Report 2016 / Senate Estimates 2014",
    },
    {
        "type": "case_study",
        "jurisdiction": "JP",
        "title": "Japan — Wishma Sandamali Death in Nagoya Immigration Detention (2021)",
        "summary": (
            "Sri Lankan national Wishma Sandamali died in Nagoya Regional Immigration "
            "Services Bureau on 6 March 2021 after weeks of vomiting and inability to eat. "
            "Footage showed staff dismissing her requests for medical attention. Immigration "
            "authorities initially refused to release CCTV footage; a court order compelled "
            "partial disclosure. The case prompted Japan to pass 2023 amendments to the "
            "Immigration Control Act, though critics argued reforms were insufficient."
        ),
        "source": "MoJ Investigation Report August 2021 / Tokyo District Court 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "LY",
        "title": "Libya — Tajoura Airstrike Mass Death (2019) — Full Circumstances",
        "summary": (
            "53 migrants (confirmed; estimated 60-70) were killed when an airstrike hit a "
            "warehouse within the Tajoura detention compound on 2 July 2019. Survivors "
            "reported that guards fired at detainees who tried to flee after the strike. "
            "The weapons depot adjacent to the detention compound had been flagged by UNHCR "
            "and IOM as an unacceptable risk factor for the preceding year. The UN attributed "
            "the airstrike to the Libyan National Army but no accountability followed."
        ),
        "source": "OHCHR Press Release July 2019 / UN Panel of Experts S/2020/360",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Marcos Aguilar-Orduño Death from Medical Neglect in ICE Detention (2019)",
        "summary": (
            "Mexican citizen Marcos Aguilar-Orduño died in CoreCivic-operated facility in "
            "Arizona after medical staff failed to diagnose and treat his deteriorating "
            "condition. DHS OIG found 'significant deficiencies' in medical care. His case "
            "was one of 13 deaths in ICE custody in 2019, the highest annual total in a "
            "decade. DHS OIG recommended mandatory compliance inspections, which were "
            "partially implemented under the Biden administration."
        ),
        "source": "DHS OIG OIG-20-45 2020 / ACLU National Prison Project 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "GR",
        "title": "Greece — Moria Fire: Arson After Intolerable Conditions (2020)",
        "summary": (
            "Fires destroyed Moria camp on Lesbos on 8-9 September 2020, leaving 12,700 "
            "people homeless. Greek authorities arrested six Afghans in connection with the "
            "fire. Advocacy groups noted the fire occurred in the context of prolonged "
            "confinement under COVID-19 lockdown that denied any movement outside camp "
            "boundaries. The replacement facility, Mavrovouni, was criticized by MSF as "
            "equally inadequate."
        ),
        "source": "MSF 2020 / Refugee Support Aegean 2020 / Human Rights Watch 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "MY",
        "title": "Malaysia — Semenyih Immigration Detention Centre Riots (2019)",
        "summary": (
            "Detainees at Semenyih Immigration Detention Centre rioted in March 2019, with "
            "one guard killed and 11 officers injured. Subsequent inquiry found conditions "
            "included 600 detainees in space designed for 200, minimal outdoor access, and "
            "food rations below WHO minimum standards. SUHAKAM called for an independent "
            "investigation into systemic conditions. Government instead announced enhanced "
            "security measures without addressing root causes."
        ),
        "source": "SUHAKAM Statement March 2019 / Malay Mail / The Star 2019",
    },

    # -----------------------------------------------------------------------
    # Additional Cross-Cutting Themes and Regional Cases
    # -----------------------------------------------------------------------
    {
        "type": "case_study",
        "jurisdiction": "MX",
        "title": "Mexico — Siglo XXI Detention Centre: Largest in Western Hemisphere",
        "summary": (
            "Mexico's Siglo XXI (Station Migratoria) in Tapachula is the largest immigration "
            "detention centre in Latin America, designed for 960 but regularly holding "
            "2,000-4,000. CNDH documented at least 9 deaths 2019-2022, abuse by guards, "
            "and denial of asylum information. Central American trafficking victims were "
            "regularly detained without NRM referral. UNHCR noted that asylum seekers were "
            "pressured to accept voluntary return in lieu of processing."
        ),
        "source": "CNDH Siglo XXI Reports 2019-2022 / Human Rights Watch Mexico 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "TR",
        "title": "Turkey — Foreigners' Removal Centres: EU Externalization and Conditions",
        "summary": (
            "Turkey holds up to 20,000 migrants in Removal Centres (GGMs) at any time, "
            "including Syrians, Afghans, and Pakistanis. Returnees from Greece under the "
            "EU-Turkey Deal were placed in GGMs rather than being released. CPT's 2020 "
            "visit documented overcrowding, inadequate access to legal aid, and violence "
            "by staff at Edirne and Pehlivanköy. BMMYK (UNHCR Turkey) documented cases of "
            "trafficking victims deportd to Syria without screening."
        ),
        "source": "CPT Report Turkey 2020 / BMMYK / Human Rights Watch 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "ET",
        "title": "Ethiopia — Returnee Reception: Trafficking Re-Victimization Post-Detention",
        "summary": (
            "Ethiopians deported from Saudi Arabia and other GCC states arrived at Addis "
            "Ababa Bole airport often traumatized, without funds, and with no ID documents. "
            "IOM operated an Assisted Voluntary Return programme but limited capacity meant "
            "many were processed through transit shelters with insufficient security. "
            "Recruiters known to be fraudulent were documented operating inside these "
            "reception points, re-recruiting recently deported migrants."
        ),
        "source": "IOM Ethiopia Return Reports 2018-2022 / Migrant Forum in Asia",
    },
    {
        "type": "case_study",
        "jurisdiction": "KE",
        "title": "Kenya — Dadaab and Kakuma: Refugees Criminalized for Camp Departure",
        "summary": (
            "Kenya's Encampment Policy requires all refugees to live in Dadaab or Kakuma "
            "camps, criminalizing refugees found in Nairobi or other urban areas. Refugees "
            "leaving camps for work, medical care, or family reunion were arrested and "
            "detained in Nairobi immigration cells. Trafficking victims were unable to "
            "report to authorities in Nairobi without risking detention. The High Court "
            "in 2021 found the encampment policy unconstitutional (Kituo cha Sheria v. "
            "Attorney General)."
        ),
        "source": "Kituo cha Sheria v. AG [2021] KEHC 5826 / UNHCR Kenya / HRW 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh — Returnee Migrant Workers: Detention-Like Holding at Airport",
        "summary": (
            "Bangladeshi migrants deported from Malaysia and Saudi Arabia faced informal "
            "holding at Hazrat Shahjalal International Airport that Refugee and Migratory "
            "Movements Research Unit described as unlawful detention. Workers who owed "
            "money to recruitment agents were held by private security contracted by "
            "recruitment association BAIRA, preventing them from leaving until debts were "
            "settled or relatives paid. No legal authority existed for this holding."
        ),
        "source": "RMMRU Bangladesh 2019 / Migrant Forum in Asia / ILO Bangladesh",
    },
    {
        "type": "case_study",
        "jurisdiction": "TN",
        "title": "Tunisia — Racially-Motivated Detention of Sub-Saharan Africans (2023)",
        "summary": (
            "Following President Saied's February 2023 speech linking sub-Saharan migrants "
            "to demographic conspiracy, Tunisian security forces conducted mass arrests of "
            "Black African migrants and asylum seekers, detaining thousands in informal "
            "sites without food or water. UNHCR documented cases of detention in desert "
            "border zones without water access, resulting in deaths. EU-Tunisia Memorandum "
            "of Understanding signed July 2023 was condemned by OHCHR for facilitating "
            "these practices."
        ),
        "source": "UNHCR Tunisia 2023 / Amnesty International 2023 / OHCHR Statement July 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan — Afghan Refugee Crackdown: Mass Detention and Deportation (2023)",
        "summary": (
            "Pakistan's November 2023 deadline for undocumented Afghans to leave or face "
            "detention resulted in more than 450,000 Afghans returning to Afghanistan within "
            "weeks. Those who did not leave were detained in holding centres in KPK province. "
            "UNHCR and HRW documented that registered refugees with valid UNHCR cards were "
            "detained despite their protected status. Trafficking victims returning to "
            "Afghanistan faced extreme risk of re-trafficking."
        ),
        "source": "UNHCR Pakistan October-November 2023 / Human Rights Watch November 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "MA",
        "title": "Morocco — Sub-Saharan African Migrants: Arbitrary Detention and Forest Camps",
        "summary": (
            "Moroccan authorities conducted regular sweeps detaining sub-Saharan African "
            "migrants from Rabat and Casablanca, transporting them to forest camps near "
            "Oujda on the Algerian border without food, water, or shelter. Médecins sans "
            "Frontières documented violence during arrest operations. Women in these camps "
            "reported sexual violence and solicitation for prostitution. GADEM documented "
            "1,700+ collective expulsions 2018-2020."
        ),
        "source": "MSF Morocco Reports 2018-2021 / GADEM Rapports / Amnesty International 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "RS",
        "title": "Serbia — Transit Country Detention: Informal Pushbacks from EU Border",
        "summary": (
            "Migrants pushed back from Croatia and Hungary into Serbia were held in Reception "
            "Centres in Preševo and Šid described by CPT as having prison-like conditions. "
            "NGOs documented secondary pushbacks by Serbian authorities to North Macedonia "
            "and Bulgaria, sometimes involving violence by police. Trafficking screening "
            "was absent. The Commissioner for Refugees documented individuals being held "
            "without access to asylum procedures."
        ),
        "source": "CPT Serbia Report 2020 / Belgrade Centre for Human Rights 2021 / UNHCR Serbia",
    },
    {
        "type": "case_study",
        "jurisdiction": "HU",
        "title": "Hungary — Röszke Transit Zone: CJEU Finds Unlawful Detention (2020)",
        "summary": (
            "The Court of Justice of the EU ruled in Case C-924/19 PPU (FMS) that Hungary's "
            "transit zone detention of asylum seekers at Röszke constituted unlawful "
            "deprivation of liberty under Directive 2013/33/EU because it was neither "
            "justified by a formal detention order nor subject to judicial review. Hungary "
            "closed the transit zones in May 2020 after the ruling but subsequently removed "
            "asylum procedures entirely from its territory."
        ),
        "source": "CJEU C-924/19 PPU FMS v. Hungary 2020 / UNHCR Hungary",
    },
    {
        "type": "case_study",
        "jurisdiction": "MV",
        "title": "Maldives — Migrant Worker Detention as Immigration Enforcement Tool",
        "summary": (
            "Maldivian authorities detained Bangladeshi and Indian workers whose employers "
            "had absconded or failed to pay wages, classifying them as immigration violators "
            "because their work permits were linked to non-compliant employers. Workers in "
            "the Dhoonidhoo Detention Centre reported paying informal fees to guards for "
            "food. The ILO noted that the system incentivized employers to neglect workers "
            "knowing the state would detain them as violators."
        ),
        "source": "ILO Maldives Country Report 2020 / Migrant Forum in Asia",
    },
    {
        "type": "case_study",
        "jurisdiction": "BH",
        "title": "Bahrain — Jaw Prison: Migrant Workers Held With Criminal Detainees",
        "summary": (
            "Migrants detained for immigration offences at Jaw Prison in Bahrain were held "
            "alongside criminal detainees. BHRN documented physical abuse and exploitation "
            "of migrant detainees by both guards and other prisoners. Domestic workers who "
            "fled abusive employers were charged with 'absconding' under kafala rules and "
            "detained for months before deportation. UNHCR was denied systematic access."
        ),
        "source": "Bahrain Institute for Rights and Democracy 2019 / Migrant-Rights.org 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "MM",
        "title": "Myanmar — Repatriated Migrants: Border Detention and Exploitation (2020-2022)",
        "summary": (
            "Burmese migrants deported from Thailand during COVID-19 were held in quarantine "
            "facilities at the border that functioned as detention. Facilities in Myawaddy "
            "and Tachileik were overcrowded and controlled by military-affiliated groups "
            "following the 2021 coup. IOM and civil society documented cases where detainees "
            "were forced to pay release fees. Trafficking victims were unable to access "
            "reintegration services."
        ),
        "source": "IOM Myanmar 2021 / Fortify Rights 2021 / Thailand Migration Report 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "ID",
        "title": "Indonesia — Rudenim Detention Centres: Protracted Asylum Seeker Detention",
        "summary": (
            "Indonesia's Rumah Detensi Imigrasi (Rudenim) centres held asylum seekers for "
            "3-10 years pending UNHCR resettlement determination. Australia's refusal to "
            "accept resettlement from Indonesia created a bottleneck. Suicide attempts and "
            "self-harm were documented at Tanjung Pinang and Pontianak Rudenim. UNHCR "
            "Indonesia documented that trafficking victims were held in the same facilities "
            "as other immigration detainees without differentiated protection."
        ),
        "source": "UNHCR Indonesia 2018 / Human Rights Watch 2017 / Asylum Access Indonesia",
    },
    {
        "type": "case_study",
        "jurisdiction": "ZA",
        "title": "South Africa — Lindela Repatriation Centre: Systemic Rights Violations",
        "summary": (
            "Lindela Repatriation Centre in Krugersdorp (operated by Bosasa/African Global "
            "Operations) has faced sustained criticism since 1996. Court findings have "
            "included unlawful detention beyond 120 days, denial of legal representation, "
            "and failure to identify asylum seekers before detention. Deaths from "
            "tuberculosis and other preventable conditions were documented. UNHCR noted "
            "trafficking victims from Zimbabwe and Mozambique were detained without referral."
        ),
        "source": "Lawyers for Human Rights v. Minister of Home Affairs / HRW South Africa 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "BR",
        "title": "Brazil — Venezuelan Migrants: Pacaraima Border Detention and Violence (2019)",
        "summary": (
            "Thousands of Venezuelan migrants in Roraima state were periodically rounded up "
            "and held in improvised centres near the Pacaraima border crossing. A 2018 riot "
            "by local residents destroyed migrant camps; subsequent detention was framed as "
            "protective but lacked legal basis. UNHCR and IOM documented that trafficking "
            "networks operated in the border area, recruiting from holding facilities."
        ),
        "source": "UNHCR Brazil 2019 / IOM DTM Venezuela 2019 / Conectas Human Rights",
    },
    {
        "type": "case_study",
        "jurisdiction": "CL",
        "title": "Chile — Colchane Border Crisis: Arbitrary Detention of Haitians (2021)",
        "summary": (
            "During the 2021 migration surge at Colchane (Bolivia-Chile border), Chilean "
            "authorities detained Haitian and Venezuelan migrants in temporary facilities "
            "without access to asylum procedures. The Constitutional Tribunal found aspects "
            "of the 2021 Migration Law's deportation provisions unconstitutional. Reports "
            "documented children in overcrowded facilities; an eight-month-old infant died "
            "in a detention transfer van in January 2022."
        ),
        "source": "INDH Chile 2021 / Human Rights Watch 2021 / Tribunal Constitucional 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "EC",
        "title": "Ecuador — Darién Gap Migrants Transiting to US: Panamanian Detention Issues",
        "summary": (
            "Migrants crossing the Darién Gap (Colombia-Panama) including Ecuadorians, "
            "Haitians, and Venezuelans were detained at Lajas Blancas and other Panamanian "
            "reception stations in conditions UNHCR described as inadequate. Trafficking "
            "victims among the flow were not identified before detention. Reports documented "
            "exploitation of women and girls in the camps by criminal networks who entered "
            "with impunity."
        ),
        "source": "UNHCR Panama 2022 / Human Rights Watch 2023 / IOM Darién Reports 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Family Separation Policy (Zero Tolerance): Child Detention (2018)",
        "summary": (
            "The Trump administration's Zero Tolerance Policy (2018) resulted in 5,500+ "
            "children being separated from parents at the US-Mexico border and held in "
            "separate detention facilities. ORR shelters were found to hold children for "
            "longer than the 72-hour limit. ACLU documented cases of trafficking victims "
            "separated from NGO-identified traffickers (a protective use) but also from "
            "legitimate parents. A class action (Ms. L v. ICE) required reunification."
        ),
        "source": "Ms. L v. ICE, 302 F.Supp.3d 1149 (S.D. Cal. 2018) / ACLU / HHS OIG",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — Clint Border Patrol Station: Filthy Conditions for Children (2019)",
        "summary": (
            "In June 2019, legal observers and journalists documented that Clint Border Patrol "
            "Station (Texas) held 300+ migrant children without adequate food, water, "
            "sanitation, or adult supervision. Children described caring for infants without "
            "formula. DHS OIG confirmed findings. The revelations prompted congressional "
            "hearings. Trafficking vulnerability was high given the unaccompanied status "
            "of many children."
        ),
        "source": "DHS OIG OIG-19-46 2019 / ProPublica / NYT June 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "GLOBAL",
        "title": "Global — COVID-19 and Immigration Detention: Mass Release vs. Continued Detention",
        "summary": (
            "In response to COVID-19, many states released immigration detainees in early 2020 "
            "due to outbreak risk: Canada (2,000+ released), UK (900+ released), Australia "
            "(partial releases). Others including the US, Greece, and Malaysia did not. "
            "ICE documented 8,000+ detainee COVID-19 cases by mid-2021. The differential "
            "response demonstrated that detention was a policy choice, not an operational "
            "necessity, undermining the stated rationale for indefinite detention."
        ),
        "source": "IDC COVID-19 Tracker 2020-2021 / UNHCR COVID Release Advocacy",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia — Trafficking Victims Detained in 'Social Affairs' Centres",
        "summary": (
            "Cambodia's Ministry of Social Affairs operated 'social affairs centres' that "
            "functioned as closed detention for trafficking victims, sex workers, and "
            "homeless persons swept up in police operations. Human Rights Watch documented "
            "that detainees included verified trafficking victims who were held without "
            "consent, subjected to forced labor within the centres, and denied access to "
            "NGOs. The practice violated both the non-punishment principle and ASEAN "
            "trafficking guidelines."
        ),
        "source": "Human Rights Watch 'They Prey on Us' 2010; 'At Your Own Risk' 2019 / LICADHO",
    },
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "China — Detention and Deportation of North Korean Escapees",
        "summary": (
            "China systematically detains and deports North Korean nationals who cross into "
            "Jilin and Liaoning provinces, classifying them as economic migrants rather than "
            "refugees despite UNHCR's position that they qualify for refugee protection. "
            "Many North Korean women detained are trafficking victims purchased by Chinese "
            "families. Their deportation returns them to a country where they face "
            "persecution, execution, or labour camp imprisonment, constituting refoulement."
        ),
        "source": "UNHCR 2002 Advisory on North Koreans / HRW North Korea Reports 2002-2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "ASEAN",
        "title": "Andaman Sea Crisis — Boat People Detention After Push-Backs (2015)",
        "summary": (
            "During the May 2015 Andaman Sea migration crisis, Thailand, Malaysia, and "
            "Indonesia initially turned back boats with Rohingya and Bangladeshi migrants. "
            "After international pressure, vessels were allowed to land. Those rescued were "
            "placed in overcrowded temporary centres in Langkawi and Penang; no trafficking "
            "screening occurred. Trafficking networks were documented recruiting from these "
            "centres within days of arrival."
        ),
        "source": "Fortify Rights 2015 / UNHCR 2015 / Human Rights Watch May 2015",
    },
    {
        "type": "case_study",
        "jurisdiction": "YE",
        "title": "Yemen — Migrant Detention by Houthi and Government Forces During Conflict",
        "summary": (
            "Ethiopian and Somali migrants transiting Yemen toward Saudi Arabia were detained "
            "by both Houthi forces and Yemeni government entities in facilities without "
            "humanitarian access. IOM documented migrants held in repurposed warehouses and "
            "schools. Ransom demands were made to families. Some detainees were forced to "
            "fight for armed factions. The conflict rendered consular protection effectively "
            "unavailable."
        ),
        "source": "IOM Yemen Migration Response 2019-2022 / UNHCR Yemen / OCHA 2021",
    },
    {
        "type": "regulation",
        "jurisdiction": "EU",
        "title": "EU Returns Directive 2008/115/EC — 18-Month Maximum Detention Limit",
        "summary": (
            "The EU Returns Directive sets a maximum detention period of 6 months, extendable "
            "to 18 months in specific circumstances (lack of cooperation or delay in "
            "obtaining travel documents). Multiple Member States routinely extend to the "
            "18-month maximum. ECRE documented cases where persons were re-detained after "
            "release to circumvent the 18-month limit. The CJEU ruled in Mahdi (C-146/14 PPU) "
            "that automatic extension without case-by-case review violates the Directive."
        ),
        "source": "Directive 2008/115/EC / CJEU C-146/14 PPU Mahdi 2014 / ECRE 2022",
    },
    {
        "type": "statute",
        "jurisdiction": "INTERNATIONAL",
        "title": "International Convention on Migrant Workers (CMW) — Article 17: Detention Rights",
        "summary": (
            "Article 17 of the ICRMW (1990) requires that migrant workers in immigration "
            "detention be held separately from convicted persons, treated with humanity and "
            "respect for dignity, informed of reasons for detention, and given effective "
            "consular access. The CMW Committee's General Comment 2 (2013) reinforces that "
            "detention of undocumented migrants must be a last resort and subject to "
            "proportionality review. Only 59 states have ratified the CMW (as of 2023)."
        ),
        "source": "ICRMW Art. 17 / CMW General Comment No. 2, CMW/C/GC/2 (2013)",
    },
    {
        "type": "case_study",
        "jurisdiction": "FR",
        "title": "France — Centre de Rétention Administrative Detention Deaths and Escapes",
        "summary": (
            "France's Centres de Rétention Administrative (CRA) hold migrants for up to "
            "90 days pending deportation. La Cimade documented 8 deaths in CRAs 2008-2020, "
            "numerous hunger strikes, and 400+ detainee self-harm incidents. Anafé documented "
            "trafficking victims including Nigerian women detained without NRM referral. "
            "The 2018 asylum and immigration law (Loi ASILE-IMMIGRATION) extended maximum "
            "detention from 45 to 90 days despite NGO opposition."
        ),
        "source": "La Cimade CRA Annual Reports / Anafé 2019 / Loi 2018-778",
    },
    {
        "type": "case_study",
        "jurisdiction": "DE",
        "title": "Germany — Pre-Deportation Detention: Abschiebehaft and Trafficking Victims",
        "summary": (
            "Germany's Abschiebehaft (pre-deportation detention) has been subject to "
            "constitutional challenge. The Federal Constitutional Court found in multiple "
            "decisions (2015, 2018) that conditions in facilities used for Abschiebehaft "
            "violated the requirement that administrative detention be distinguishable from "
            "criminal incarceration. UNHCR documented cases of trafficking victims held in "
            "Abschiebehaft without BAMF referral for NRM processing."
        ),
        "source": "BVerfG 2 BvR 1803/14 (2015) / UNHCR Germany / Pro Asyl 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Philippines — Departure-Banned OFWs: Airport Detention Without Due Process",
        "summary": (
            "Filipino overseas workers (OFWs) attempting to leave on contracts flagged by "
            "POEA as non-standard were stopped by the Overseas Workers Welfare Administration "
            "at departure airports and held in the airport lounge for hours or days without "
            "formal detention orders. Workers who refused repatriation were not charged but "
            "could not leave. NGOs documented cases of bona fide workers stranded because "
            "employers were on blacklists they were not informed of."
        ),
        "source": "Migrante International 2019 / IBON Foundation / POEA Departure Protocols",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal — Women Detained at Tribhuvan Airport Under 'Protective' Restrictions",
        "summary": (
            "Nepal's policy of restricting women under 40 from travelling to GCC states "
            "without male guardian consent resulted in women being stopped at Tribhuvan "
            "International Airport and held in DOFE offices for hours pending verification. "
            "The Supreme Court struck down the restriction in 2020 as unconstitutional. "
            "Trafficking advocates noted the restriction was ostensibly protective but "
            "was counterproductive, pushing recruitment underground where trafficking "
            "risk was higher."
        ),
        "source": "Supreme Court of Nepal Writ No. 069-WO-0702 (2020) / NHRC Nepal",
    },
    {
        "type": "case_study",
        "jurisdiction": "SG",
        "title": "Singapore — Foreign Domestic Workers: 'Employer's Address' Tied Residency as Informal Confinement",
        "summary": (
            "Singapore's Employment of Foreign Manpower Act requires foreign domestic workers "
            "to reside at their employer's address. Workers who left employer premises were "
            "technically in violation of their work permit conditions, enabling employers "
            "to report them as absconders. IOM and HOME documented cases where workers "
            "were unable to access police to report abuse without risking detention. "
            "Singapore amended the Act in 2012 and 2019 to provide some protective provisions."
        ),
        "source": "HOME Singapore 2019 / IOM Singapore / MOM Foreign Domestic Worker Policy",
    },
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Hong Kong — Castle Peak Bay IRC: Refugee Detention and NRM Failures",
        "summary": (
            "Castle Peak Bay Immigration Centre in Hong Kong held asylum seekers whose "
            "claims were rejected for up to 18 months pending deportation. UNHCR documented "
            "that Vietnamese trafficking victims among detainees were not referred to "
            "Hong Kong's anti-trafficking screening procedure. The Immigration Department "
            "maintained that Hong Kong was not bound by the Refugee Convention. Detainees "
            "had extremely limited legal aid access."
        ),
        "source": "UNHCR Hong Kong / Christian Action Hong Kong / HK Bar Association 2018",
    },
    {
        "type": "case_study",
        "jurisdiction": "GLOBAL",
        "title": "Global — Private Prison Industry and Immigration Detention: Profit Motive",
        "summary": (
            "Companies including GEO Group, CoreCivic (formerly CCA), and Serco generate "
            "billions annually from immigration detention contracts. Academic research (Doty "
            "and Wheatley 2013; Fernandes 2007) documented lobbying by private prison "
            "companies for mandatory detention policies and minimum bed guarantees. The "
            "IMDEx database found positive correlation between private operator presence "
            "and average detention length, raising concerns about structural incentives "
            "to extend detention regardless of individual necessity."
        ),
        "source": "Global Detention Project / IMDEx Database / Doty & Wheatley, Journal of "
            "Political Power 2013",
    },
    {
        "type": "case_study",
        "jurisdiction": "IT",
        "title": "Italy — Lampedusa Hotspot: Unlawful Detention Without Legal Order (2015-2022)",
        "summary": (
            "Italy's Lampedusa hotspot held arrivals from North Africa without formal "
            "detention orders, sometimes for weeks. The European Court of Human Rights found "
            "in J.A. and Others v. Italy (2021) that the confinement violated Article 5 "
            "(right to liberty) because it lacked a legal basis. Trafficking victims "
            "identified within the hotspot were sometimes not transferred to safe "
            "accommodation before deportation proceedings commenced."
        ),
        "source": "ECHR J.A. and Others v. Italy (App. 21329/18) 2021 / ASGI Italy / MSF",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "USA — San Diego Family Residential Centres: Dilley and Berks County",
        "summary": (
            "Family detention at Dilley (South Texas Family Residential Centre, operated by "
            "CoreCivic) and Berks County held asylum-seeking families including those with "
            "trafficking claims. A 2020 complaint to DHS OIG documented COVID-19 spread "
            "in Dilley. The Biden administration closed Berks in 2021 citing inhumane "
            "conditions but maintained Dilley. Courts repeatedly found family detention "
            "violated the Flores settlement requiring children's release within 20 days."
        ),
        "source": "Flores v. Barr 828 F.3d 898 (9th Cir. 2016) / DHS OIG 2020 / RAICES Texas",
    },
    {
        "type": "case_study",
        "jurisdiction": "GLOBAL",
        "title": "Global — Stateless Persons: Indefinite Detention Due to Deportability Gap",
        "summary": (
            "Stateless persons, including Bidun in Kuwait/UAE, Palestinians in multiple "
            "states, and ethnic Nepalis in Bhutan, face potentially indefinite immigration "
            "detention because no state accepts their deportation. The UNHCR documented "
            "stateless detainees held for 10+ years in Malaysia, Hong Kong, and the US. "
            "The ICRMW's Article 17, UNHCR's Detention Guidelines, and the 1954 Convention "
            "on Statelessness all require alternatives to detention in such cases."
        ),
        "source": "UNHCR / Global Detention Project Statelessness Briefing 2020 / UNHCR 1954 Conv.",
    },
    {
        "type": "case_study",
        "jurisdiction": "PG",
        "title": "Papua New Guinea — Lombrum Naval Base: Post-Closure Detention (2017-2021)",
        "summary": (
            "After PNG closed the Manus Island detention facility in October 2017, 400+ "
            "refugees refused to leave, and Australia continued food and water supply "
            "under pressure. PNG moved them to East Lorengau Refugee Transit Centre "
            "and Hillside Haus, which operated as de facto closed detention despite "
            "being officially designated as open centres. Refugees reported harassment "
            "by PNG nationals and threats by police. Australia was found by the Federal "
            "Court to have duty of care obligations to the detainees."
        ),
        "source": "Australian Federal Court ABT18 v. Minister for Home Affairs [2020] / UNHCR",
    },
    {
        "type": "case_study",
        "jurisdiction": "BV",
        "title": "Bolivia/Peru — Andean Migrant Women: Police Detention and Trafficking Exposure",
        "summary": (
            "Research by the Inter-American Commission on Human Rights documented that "
            "indigenous Bolivian and Peruvian women migrating informally through border "
            "areas who were detained by police faced heightened trafficking risk from "
            "detention officials who referred them to brothels in exchange for releases. "
            "Absence of anti-trafficking NRM protocols in Bolivian and Peruvian border "
            "police units was identified as a structural gap."
        ),
        "source": "IACHR Trafficking in Persons Report 2016 / IOM Andean Region 2018",
    },
    {
        "type": "policy_update",
        "jurisdiction": "US",
        "title": "USA — Biden Administration: ICE Enforcement Priorities Memo (2021)",
        "summary": (
            "The Biden administration's September 2021 ICE Enforcement Priorities Memorandum "
            "directed ICE to focus on national security threats, recent border crossers, "
            "and those with serious criminal convictions, de-emphasizing arrest of long-term "
            "residents and trafficking victims cooperating with law enforcement. The memo "
            "reduced ICE detention to approximately 22,000 daily (from 55,000 in 2019). "
            "Advocacy groups noted the memo did not create legally enforceable protections "
            "and could be reversed by a subsequent administration."
        ),
        "source": "ICE Memorandum September 30, 2021 / ACLU / CLINIC 2021",
    },
    {
        "type": "policy_update",
        "jurisdiction": "AU",
        "title": "Australia — AHRC National Inquiry: Children in Immigration Detention (2014)",
        "summary": (
            "The AHRC's 'The Forgotten Children' inquiry (2014) found 233 children who had "
            "been in detention for more than two years, documented 128 assault incidents "
            "and 33 sexual assaults involving children in detention, and found that "
            "prolonged detention caused serious harm to children's mental health. The "
            "inquiry recommended immediate release of all children from closed detention; "
            "the government rejected this recommendation."
        ),
        "source": "AHRC 'The Forgotten Children' February 2014",
    },
    {
        "type": "policy_update",
        "jurisdiction": "GB",
        "title": "UK — Stephen Shaw Review: Immigration Detention Reform (2018)",
        "summary": (
            "Stephen Shaw's 2018 follow-up review (to his 2016 report) found that the UK "
            "government's Adults at Risk (AAR) policy was not working as intended, that "
            "vulnerable people including trafficking victims were still being detained for "
            "lengthy periods, and that Home Office culture was not sufficiently focused on "
            "welfare. Shaw recommended a 28-day time limit on immigration detention; the "
            "government refused to implement a statutory time limit."
        ),
        "source": "Shaw Review 2018 'Assessment of Government Progress in Implementing the Report'",
    },
    {
        "type": "regulation",
        "jurisdiction": "INTERNATIONAL",
        "title": "Global Compact for Safe, Orderly and Regular Migration (GCM) — Objective 13",
        "summary": (
            "Objective 13 of the 2018 Global Compact for Migration calls on states to use "
            "immigration detention only as a measure of last resort and to pursue non-"
            "custodial alternatives. The GCM is non-binding but provides a framework "
            "endorsed by 164 states. The UN Network on Migration monitors implementation "
            "through the International Migration Review Forum. Progress has been described "
            "by UNHCR as 'limited' in its 2022 GCM implementation overview."
        ),
        "source": "GCM A/RES/73/195 Objective 13 / UN Network on Migration IMRF 2022",
    },
    {
        "type": "regulation",
        "jurisdiction": "INTERNATIONAL",
        "title": "UN Special Rapporteur on Torture: Detention in Migration Context (2012)",
        "summary": (
            "The UN Special Rapporteur on Torture's report A/HRC/20/24 (2012) stated that "
            "immigration detention per se does not constitute torture but that conditions "
            "in many immigration detention facilities — including overcrowding, lack of "
            "access to healthcare, and ill-treatment — may rise to the level of torture or "
            "CIDT under CAT Article 1 and 16. The report called for alternatives to "
            "detention and a global ban on indefinite detention."
        ),
        "source": "UN SR Torture Report A/HRC/20/24 2012",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lanka — Returnee Trafficking Victims: Boossa Detention (2019-2021)",
        "summary": (
            "Sri Lankan women returned from the Middle East who had been trafficking victims "
            "were sometimes held at Boossa Detention Centre (originally a high-security "
            "prison) pending documentation. NGO Kantha Shakthi documented cases where "
            "women who self-identified as trafficking victims to immigration officers "
            "were treated as irregular migrants rather than referred to the National "
            "Anti-Trafficking Hotline, in violation of the Prevention of Trafficking in "
            "Persons Act 2015."
        ),
        "source": "Kantha Shakthi / Sri Lanka Bureau of Foreign Employment 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "GH",
        "title": "Ghana — DOVVSU Shelters: Trafficking Victims in Closed Facilities",
        "summary": (
            "Ghana's Domestic Violence and Victim Support Unit operated shelters for "
            "trafficking victims that functioned as closed detention: gate-locked, no "
            "freedom of movement, and with mandatory police accompaniment for external "
            "appointments. HAART Ghana documented that victims detained in these shelters "
            "reported feeling re-victimized by the loss of autonomy, deterring future "
            "reporting by potential victims."
        ),
        "source": "HAART Ghana 2018 / IOM Ghana / US TIP Report Ghana 2020",
    },
    {
        "type": "case_study",
        "jurisdiction": "RU",
        "title": "Russia — Migrant Detention Centres: Central Asian Workers Without Consular Access",
        "summary": (
            "Russia's Temporary Detention Centres for Foreign Citizens (TDFG) held Central "
            "Asian workers (Uzbek, Tajik, Kyrgyz) for overstaying visas or working without "
            "permits. Memorial (before its forced closure) documented denial of consular "
            "access, corruption in the deportation process, and cases where trafficking "
            "victims with pending criminal cases against employers were deported, destroying "
            "evidence. Detention periods extended beyond 2 years in documented cases."
        ),
        "source": "Memorial Human Rights Centre (Russia) 2017-2021 / Civic Assistance Committee",
    },
    {
        "type": "case_study",
        "jurisdiction": "IL",
        "title": "Israel — Holot Detention Facility: African Asylum Seeker Open Prison (2013-2018)",
        "summary": (
            "Holot Detention Facility in the Negev desert, nominally an 'open' facility, "
            "required Eritrean and Sudanese asylum seekers to sleep there nightly and check "
            "in three times daily, effectively preventing any employment or normal life. "
            "The Israeli Supreme Court struck down indefinite detention under the Prevention "
            "of Infiltration Law three times (2013, 2014, 2015). Holot was closed in 2018. "
            "Trafficking victims among the Eritrean population could not access ACRP referrals "
            "while in Holot."
        ),
        "source": "HCJ 7385/13 Adam v. Knesset (2013) / UNHCR Israel / Hotline for Refugees",
    },
    {
        "type": "case_study",
        "jurisdiction": "HU",
        "title": "Hungary — Transit Zone Conditions: Children Starved as Coercion (2019)",
        "summary": (
            "The ECHR issued interim measures in R.R. and Others v. Hungary (2019) requiring "
            "Hungary to provide food to asylum-seeking families in transit zones after "
            "authorities cut food to adult men to pressure families to withdraw asylum claims. "
            "The Grand Chamber found in Ilias and Ahmed v. Hungary (2019) that transit zone "
            "conditions amounted to degrading treatment under Article 3. This case was "
            "central to the CJEU's subsequent ruling that transit zones constituted unlawful "
            "detention."
        ),
        "source": "ECHR R.R. v. Hungary App. 36037/17 (2019) / Ilias and Ahmed v. Hungary GC 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "LB",
        "title": "Lebanon — Syrian Refugee Detention: Security Forces and Arbitrary Arrest (2019-2023)",
        "summary": (
            "Lebanese security forces (ISF and Army) conducted raids on Syrian refugee "
            "settlements, detaining those without legal status in Roumieh Prison alongside "
            "criminal detainees. UN agencies documented that trafficking victims who reported "
            "to LECORVAW were sometimes re-detained when security forces conducted follow-up "
            "operations. Syria-bound deportations were documented violating non-refoulement "
            "obligations. Lebanon is not party to the Refugee Convention."
        ),
        "source": "UNHCR Lebanon / Human Rights Watch Lebanon 2020 / Amnesty International 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "JO",
        "title": "Jordan — Syrian Refugees: Cyber-Tracked Re-Entry and Detention",
        "summary": (
            "Jordanian authorities used biometric data and the Bawabat Al-Urdun digital "
            "platform to track Syrian refugee re-entry after deportation orders. Syrians "
            "who re-entered without authorization were detained in Cyber City Deportation "
            "Centre. UNHCR documented cases where trafficking victims removed from Jordan "
            "attempted re-entry and were detained on return rather than receiving protection. "
            "Jordan ratified the 1951 Convention but has not enacted domestic refugee law."
        ),
        "source": "UNHCR Jordan 2021 / Human Rights Watch Jordan 2020 / Refworld",
    },
    {
        "type": "case_study",
        "jurisdiction": "SD",
        "title": "Sudan — Khartoum Deportation Prisons: East African Migrants (2017-2023)",
        "summary": (
            "Sudan detained Ethiopian, Eritrean, and Somali migrants attempting to reach "
            "Libya or Egypt in Khartoum's deportation prisons, including Omdurman. Human "
            "rights groups documented overcrowding, abuse by security forces, and sale of "
            "detainees to smuggling networks by prison officials. EU-funded Sudan border "
            "management operations were criticized for contributing to detentions. The "
            "2019 revolution temporarily improved conditions but the 2021 coup reversed gains."
        ),
        "source": "Amnesty International 2018 / Refugees International 2019 / HRW Sudan 2021",
    },
    {
        "type": "case_study",
        "jurisdiction": "MR",
        "title": "Mauritania — Sub-Saharan African Migrants: Detention Without Interpretation",
        "summary": (
            "Mauritanian gendarmerie detained Malian, Guinean, and Senegalese migrants "
            "in Nouakchott holding cells without Arabic or Bamanankan/Pular interpretation, "
            "making it impossible for detainees to communicate with authorities. MSF "
            "documented medical neglect in these holding cells. IOM arranged Assisted "
            "Voluntary Return for many, but trafficking victims received no screening before "
            "return, enabling re-trafficking."
        ),
        "source": "MSF West Africa 2019 / IOM Mauritania / Mixed Migration Centre West Africa",
    },
    {
        "type": "case_study",
        "jurisdiction": "NI",
        "title": "Niger — Agadez: Migration Criminalization and Detention Post-Law 036 (2015)",
        "summary": (
            "Niger's Law 036 of 2015 criminalized migrant smuggling but had the effect of "
            "criminalizing traditional migration through Agadez. Migrants attempting the "
            "Niger-Libya route were arrested and held in the Centre de Transit et de Retour "
            "in Agadez operated jointly by IOM and Niger authorities. Civil society groups "
            "noted that conditions were inadequate and that the effect of criminalizing the "
            "migration route increased migrant reliance on and vulnerability to smugglers."
        ),
        "source": "Clingendael Institute 2017 / Mixed Migration Centre 2018 / IOM Niger",
    },
    {
        "type": "case_study",
        "jurisdiction": "SN",
        "title": "Senegal — Ziguinchor Youth Detention: Child Migrants Without Guardians",
        "summary": (
            "Senegalese children attempting to migrate to Europe via the Atlantic route "
            "were detained in Ziguinchor and Dakar in conditions that UNICEF described as "
            "child rights violations. Many were separated from families; child trafficking "
            "victims including forced marabout disciples (talibés) were detained alongside "
            "voluntary migrants. No specialized reception or identification mechanism "
            "existed for child trafficking victims at detention facilities."
        ),
        "source": "UNICEF Senegal 2019 / Plan International Senegal / Human Rights Watch 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "CD",
        "title": "DRC — Mining Region Detention: Artisanal Miners Held by Armed Groups",
        "summary": (
            "Armed groups in eastern DRC (North Kivu, South Kivu) detained artisanal "
            "miners as forced labor in a form of debt bondage detention. Miners were charged "
            "for tools, food, and 'protection' against their earnings, creating debts that "
            "made departure impossible. MONUSCO and IPIS documented this practice across "
            "multiple mine sites. While not immigration detention, the structure mirrors "
            "immigration detention exploitation dynamics."
        ),
        "source": "IPIS DRC Mining Reports 2018-2021 / UN Group of Experts DRC S/2021/560",
    },
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Nigeria — Returnees from Libya: NAPTIP and Detention Post-Rescue (2017-2022)",
        "summary": (
            "Nigerians repatriated from Libya by IOM were received at Lagos airport with "
            "NAPTIP (National Agency for the Prohibition of Trafficking in Persons) screening. "
            "But those who could not be placed in NGO shelters were transferred to government "
            "correctional facilities if they had pending criminal records in Nigeria. "
            "NAPTIP data showed 60-70% of Libyan returnees were potential trafficking victims; "
            "the correctional transfer represented a non-punishment principle violation."
        ),
        "source": "NAPTIP Annual Reports 2018-2022 / IOM Nigeria / HRW 2018",
    },
    {
        "type": "case_study",
        "jurisdiction": "TZ",
        "title": "Tanzania — Nyarugusu Camp: Detention of Burundian Refugees for Security Screening",
        "summary": (
            "Tanzania detained Burundian refugees in Nyarugusu camp under security screening "
            "protocols following the 2015 Burundian crisis, restricting freedom of movement "
            "for extended periods. IOM documented Burundian women in the camp were targeted "
            "by traffickers recruiting for domestic labor in Dar es Salaam. The restriction "
            "of movement — intended as a security measure — increased trafficking vulnerability "
            "by creating economic desperation and limiting access to legitimate employment."
        ),
        "source": "UNHCR Tanzania 2017 / IOM Tanzania / HRW Burundi Crisis Reports 2016",
    },
]
