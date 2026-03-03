"""Forced marriage as a form of human trafficking — curated seed facts.

Covers: bride trafficking corridors (Myanmar-China, Vietnam-China, North Korea-China),
Walk Free estimates, bride prices, cross-border marriage fraud, child marriage,
South Asian dowry exploitation, African bride trafficking, mail-order bride exploitation,
sham marriages for immigration fraud, legal frameworks, court cases, and rescue operations.
"""

FORCED_MARRIAGE_TRAFFICKING_FACTS: list[dict] = [
    # ── Global Statistics ─────────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Walk Free — Global Forced Marriage Estimates (2022)",
        "metric": "forced_marriage_global",
        "value": "22 million",
        "summary": (
            "Walk Free estimates 22 million people living in forced marriages globally in 2021. "
            "14.9 million (68%) in Asia-Pacific. Two-thirds married as children. "
            "Women and girls account for 85% of victims. Forced marriage increased by 6.6 million "
            "since 2016 estimates, partly due to COVID-19 school closures and economic shocks."
        ),
        "source": "Walk Free Foundation / ILO Global Estimates of Modern Slavery (2022)",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "UNODC — Forced Marriage as Trafficking Form",
        "metric": "forced_marriage_trafficking_share",
        "value": "6% of detected trafficking cases",
        "summary": (
            "UNODC 2022 Global Report on Trafficking in Persons identifies forced marriage as a "
            "distinct trafficking purpose, comprising approximately 6% of detected victims globally. "
            "Sub-Saharan Africa reports the highest regional proportion. Forced marriage often "
            "intersects with sexual exploitation and domestic servitude making disaggregated data "
            "collection difficult. Underreporting is severe due to family complicity."
        ),
        "source": "UNODC Global Report on Trafficking in Persons 2022",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Child Marriage — Global Prevalence (UNICEF 2023)",
        "metric": "child_marriage_global",
        "value": "650 million girls married before age 18",
        "summary": (
            "UNICEF estimates 650 million women alive today were married before age 18. "
            "Approximately 40 million girls are currently married or in union before 18. "
            "South Asia accounts for 45% of the global total (290 million). "
            "Sub-Saharan Africa: 115 million. Child marriage is recognized as a form of forced "
            "marriage and trafficking when it involves deception, coercion, or movement for exploitation."
        ),
        "source": "UNICEF Child Marriage Data 2023 / Girls Not Brides",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "ILO — Forced Marriage Labour Exploitation Overlap",
        "metric": "forced_marriage_labour_overlap",
        "value": "domestic servitude in 72% of cases",
        "summary": (
            "ILO research indicates that in 72% of documented forced marriage cases with a "
            "trafficking dimension, victims are subsequently subjected to domestic servitude within "
            "the household of the husband or in-laws. Sexual exploitation occurs in the vast majority. "
            "Cases are routinely misclassified as 'family matters' by law enforcement, leading to "
            "severely undercounted victim numbers."
        ),
        "source": "ILO Special Action Programme to Combat Forced Labour (SAP-FL) 2021",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Walk Free — Forced Marriage COVID-19 Surge",
        "metric": "covid_forced_marriage_increase",
        "value": "6.6 million additional victims since 2016",
        "summary": (
            "The 2022 Walk Free / ILO report recorded 6.6 million more people in forced marriages "
            "compared to the 2016 estimate of 15.4 million. School closures during COVID-19 "
            "heightened vulnerability: UNESCO estimated 11 million girls at risk of not returning "
            "to school, creating conditions for child marriage. Economic shocks led families to "
            "accept bride prices or marriage payments as income replacement."
        ),
        "source": "Walk Free / ILO Global Estimates of Modern Slavery 2022, pp. 46-52",
    },

    # ── Myanmar-China Bride Trafficking ──────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Myanmar / China",
        "title": "Myanmar-China Bride Trafficking — Kachin Conflict Zone Exploitation",
        "summary": (
            "Armed conflict in Kachin and Shan states since 2011 has displaced over 100,000 people "
            "and created acute vulnerability to bride trafficking. Traffickers (often women) pose as "
            "job brokers offering factory work in China. Women are sold to Chinese rural men for "
            "between 10,000 and 30,000 Chinese yuan (USD 1,400–4,200). Buyers often lock women in "
            "homes, confiscate phones, and force repeated pregnancies to anchor victims. Estimated "
            "7,500–10,000 Myanmar women trafficked to China per year during peak conflict periods."
        ),
        "source": (
            "Human Rights Watch — 'Give Us a Baby and We'll Let You Go' (2019); "
            "Kachin Women's Association Thailand (KWAT) reports"
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "Myanmar / China",
        "title": "Bride Price Range — Myanmar Women Sold in China",
        "metric": "bride_price_myanmar_china",
        "value": "CNY 10,000–120,000 (USD 1,400–17,000)",
        "summary": (
            "Research by the Kachin Women's Association and HRW documents bride prices paid for "
            "trafficked Myanmar women ranging from CNY 10,000 for older women to CNY 120,000 for "
            "young, educated women deemed more desirable. Price varies by age, education, and "
            "whether the woman is already pregnant. Women are sometimes resold multiple times, "
            "each sale generating additional profit for a trafficking network."
        ),
        "source": "KWAT Report 2018; HRW 2019 'Give Us a Baby and We'll Let You Go'",
    },
    {
        "type": "case_study",
        "jurisdiction": "Myanmar / China",
        "title": "Myanmar Bride Trafficking — Chinese Rural Gender Imbalance Driver",
        "summary": (
            "China's historical one-child policy created a severe gender imbalance: an estimated "
            "30–40 million more men than women in the marriageable age cohort by 2020. Rural areas "
            "suffer more acute shortages. This demographic deficit created demand for purchased "
            "brides from neighboring countries. Myanmar, Vietnam, North Korea, and Cambodia have all "
            "been identified as primary source countries. Chinese authorities acknowledge the "
            "phenomenon but rarely prosecute buyers."
        ),
        "source": (
            "China Population Census 2020; Ding & Hesketh, Lancet (2006); "
            "UN Special Rapporteur on Trafficking 2020"
        ),
    },
    {
        "type": "law",
        "jurisdiction": "Myanmar",
        "title": "Myanmar Anti-Trafficking in Persons Law (2005, amended 2018)",
        "summary": (
            "Myanmar's Anti-Trafficking in Persons Law criminalizes trafficking including for forced "
            "marriage. The 2018 amendment increased penalties to life imprisonment for aggravated "
            "cases involving children. However, enforcement remains critically weak in conflict zones "
            "where the Myanmar military controls access. Kachin and Shan state trafficking cases "
            "rarely result in prosecution due to corruption and insecurity. China's cooperation on "
            "repatriation of victims is inconsistent."
        ),
        "source": "Myanmar Anti-Trafficking in Persons Law 2005 (amended 2018); US TIP Report 2023",
    },
    {
        "type": "rescue_operation",
        "jurisdiction": "China / Myanmar",
        "title": "Operation Mekong — Cross-Border Trafficking Crackdowns (2011–present)",
        "summary": (
            "China's Ministry of Public Security has conducted successive Operation Mekong waves "
            "targeting trafficking networks along the Myanmar-China border. Between 2011 and 2022, "
            "over 4,000 trafficking suspects were arrested and more than 6,000 victims rescued. "
            "However, bride trafficking prosecutions remain a fraction of totals; most victims "
            "rescued are labour or sexual exploitation victims. Women rescued from forced marriages "
            "often cannot return home due to conflict, and some are retained in Chinese institutions."
        ),
        "source": "China MPS Operation Mekong Reports; UNODC GMS Sub-regional Project",
    },

    # ── Vietnam-China Bride Trafficking ──────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "Vietnam / China",
        "title": "Vietnam — Bride Trafficking to China Scale",
        "metric": "vietnam_bride_trafficking",
        "value": "estimated 2,000–3,000 women/year",
        "summary": (
            "Vietnamese authorities estimate between 2,000 and 3,000 Vietnamese women and girls are "
            "trafficked to China annually for forced marriage. The majority originate from northern "
            "border provinces: Lào Cai, Hà Giang, Quảng Ninh, and Cao Bằng. Ethnic minority "
            "communities (H'mong, Dao, Tày) face disproportionate risk due to poverty, limited "
            "education, and geographic isolation. Recruiters are often from the same community, "
            "speaking the victims' language and exploiting trust."
        ),
        "source": (
            "Vietnam Ministry of Public Security Annual Report 2022; "
            "Pacific Links Foundation Research 2021"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Vietnam / China",
        "title": "Vietnam-China Bride Trafficking — Social Media Recruitment Shift",
        "summary": (
            "Since 2018, traffickers have shifted recruitment from in-person approaches to social "
            "media platforms including Zalo, Facebook, WeChat, and TikTok. Young women are contacted "
            "by fake romantic partners who groom them for weeks before proposing cross-border travel. "
            "Girls as young as 13 have been recruited this way. The Vietnamese government's "
            "Project 130 (2021–2025) allocated VND 500 billion for counter-trafficking but digital "
            "recruitment continues to outpace prevention."
        ),
        "source": (
            "Blue Dragon Children's Foundation (Hanoi); "
            "Vietnam MPS Project 130 Progress Report 2023"
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Vietnam",
        "title": "Vietnam Supreme Court — People v. Tran Thi Hoa (2021)",
        "summary": (
            "The Hanoi People's Court sentenced Tran Thi Hoa to 12 years imprisonment for "
            "trafficking 8 Vietnamese women to Chinese men as brides. The ring operated across "
            "Lào Cai and Yunnan provinces. Hoa recruited through false job offers, transported "
            "victims across the border at Hekou-Lào Cai crossing, and received between CNY 30,000 "
            "and 60,000 per woman. The court found that document confiscation, isolation, and "
            "physical violence constituted trafficking aggravating factors."
        ),
        "source": "Hanoi People's Court Case No. 45/2021/HS-ST; VN Express Legal Reporting",
    },
    {
        "type": "rescue_operation",
        "jurisdiction": "Vietnam / China",
        "title": "Blue Dragon Children's Foundation — Bride Trafficking Rescues (Vietnam)",
        "summary": (
            "Blue Dragon Children's Foundation, based in Hanoi, has rescued over 1,100 trafficking "
            "victims from 2007 to 2023, including hundreds of women held in forced marriages in "
            "China. Rescue operations involve coordination with Chinese contacts and sometimes "
            "require families to pay 'redemption' fees to traffickers — a practice the NGO "
            "condemns but sometimes facilitates as a last resort. Reintegration programs include "
            "trauma counseling, vocational training, and legal support."
        ),
        "source": "Blue Dragon Children's Foundation Annual Reports 2022–2023",
    },

    # ── North Korea-China Bride Trafficking ───────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "North Korea / China",
        "title": "North Korean Women — Scale of Bride Trafficking in China",
        "metric": "nk_bride_trafficking",
        "value": "estimated 70–80% of North Korean refugee women trafficked",
        "summary": (
            "Database Center for North Korean Human Rights (NKDB) estimates that 70–80% of North "
            "Korean women who cross into China illegally are trafficked — the majority into forced "
            "marriages with rural Chinese men, with the remainder into sexual exploitation. Because "
            "North Korean women are undocumented in China, they cannot seek police protection "
            "without risking deportation. Prices paid for North Korean brides range from CNY 5,000 "
            "to CNY 30,000. Children born to these women face stateless status."
        ),
        "source": (
            "NKDB White Paper on North Korean Human Rights 2022; "
            "Korea Future Initiative — Shadows of War (2019)"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "North Korea / China",
        "title": "North Korean Brides — Deportation Cycle and Re-trafficking Risk",
        "summary": (
            "When North Korean women in forced marriages in China are discovered by police, China "
            "deports them to North Korea under a bilateral agreement that classifies all North "
            "Korean border crossers as economic migrants. Upon return, women face detention and "
            "interrogation. Those who become pregnant by Chinese men sometimes abort under pressure. "
            "Women are at high risk of re-crossing and re-trafficking: Korea Future Initiative "
            "documented cases where women were sold multiple times, each crossing followed by "
            "another trafficking incident."
        ),
        "source": "Korea Future Initiative 2019; NKDB 2022; UN COI on DPRK 2014 (A/HRC/25/63)",
    },
    {
        "type": "law",
        "jurisdiction": "China",
        "title": "China — Criminal Law Article 240: Abducting and Trafficking Women and Children",
        "summary": (
            "China Criminal Law Article 240 prescribes 5 to 10 years imprisonment for trafficking "
            "women or children, with life imprisonment or death penalty for aggravated cases "
            "involving 3+ victims, abuse, or rape. Buying trafficked women (Article 241) carries "
            "3 to 10 years. However, buyers who 'do not obstruct rescue' historically received "
            "reduced sentences or were not prosecuted. A 2022 Criminal Law amendment closed this "
            "loophole, making buying a trafficking offense regardless of subsequent conduct."
        ),
        "source": "PRC Criminal Law Articles 240–242; 2022 Amendment (effective March 2022)",
    },
    {
        "type": "case_study",
        "jurisdiction": "China",
        "title": "Xuzhou Chained Woman — Systemic Bride Trafficking Exposed (2022)",
        "summary": (
            "In January 2022, video footage of a chained woman in a shed in Xuzhou, Jiangsu province "
            "went viral on Chinese social media, sparking national outrage. Investigation revealed "
            "she was a Yunnan woman with mental illness sold as a bride and subjected to repeated "
            "rape and childbirth. Eight children were produced. Local officials had failed to "
            "investigate for years. The case prompted the 2022 Criminal Law amendment increasing "
            "buyer liability and a State Council directive ordering nationwide audits of 'purchased' "
            "wives in rural areas."
        ),
        "source": (
            "PRC State Council Directive on Rural Women Trafficking (Feb 2022); "
            "Reuters, NYT, BBC reporting Jan–Mar 2022"
        ),
    },

    # ── Cross-Border Marriage Fraud ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "South Korea / Vietnam",
        "title": "South Korea — Cross-Border Marriage Fraud and Subsequent Exploitation",
        "summary": (
            "South Korea facilitates international marriages for rural men through 'marriage broker' "
            "agencies (gyeolhon jungme eophche). Between 2010 and 2022, over 260,000 international "
            "marriages were registered, predominantly Korean men with Vietnamese, Chinese, and "
            "Filipino women. The Korean Institute of Criminology documented cases where women "
            "arrived to find conditions vastly different from what brokers promised: abusive spouses, "
            "unpaid domestic labor, and passport confiscation. Marriage visa dependency prevents "
            "women from leaving. Broker fees range from USD 10,000 to 25,000."
        ),
        "source": (
            "Korean Institute of Criminology (KIC) Report 2021; "
            "Korea Immigration Service Statistics 2022"
        ),
    },
    {
        "type": "law",
        "jurisdiction": "South Korea",
        "title": "South Korea — Act on the Penalty of Crimes Related to Illegal Brokerage of International Marriages (2014)",
        "summary": (
            "South Korea's 2014 Act amended in 2021 requires marriage brokers to register with "
            "provincial governments, disclose criminal histories, and provide standardized "
            "information packets in the bride's language covering Korean law, domestic violence "
            "resources, and immigration rights. Brokers who misrepresent conditions face up to "
            "3 years imprisonment. Despite the law, enforcement is limited and many illegal brokers "
            "operate via social media and online platforms. The Ministry of Justice reported 43 "
            "broker prosecutions between 2014 and 2022."
        ),
        "source": "Republic of Korea Act on International Marriage Brokerage (2014, amended 2021)",
    },
    {
        "type": "case_study",
        "jurisdiction": "Japan / Philippines / Vietnam",
        "title": "Japan — 'Entertainer' Visa to Forced Marriage Pipeline",
        "summary": (
            "Research by the Polaris Project Japan and the National Police Agency documents a "
            "pipeline where Filipina and Vietnamese women enter Japan on entertainer or technical "
            "trainee visas, are subjected to labor exploitation, and are subsequently 'transferred' "
            "to Japanese men as wives through arranged payments to trafficking networks. The "
            "Technical Intern Training Program (TITP) has been identified as a recruitment "
            "mechanism. Women who refuse face visa cancellation threats. Japan's Immigration "
            "Control Act reforms (2024) do not fully address this intersection."
        ),
        "source": (
            "Polaris Project Japan 2022; Japan NPA Trafficking Report 2023; "
            "ILO TITP Assessment 2021"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Cambodia / China",
        "title": "Cambodia — Bride Trafficking to China Surge (2015–2022)",
        "summary": (
            "Human Rights Watch documented a surge in Cambodian women being recruited and sold as "
            "brides in China from 2015. Recruiters offer factory work in China; women cross legally "
            "via Phnom Penh airport or illegally through Poipet border. Prices paid: USD 2,000 to "
            "10,000 per woman. Cambodian government signed bilateral agreement with China on "
            "repatriation in 2017 and has repatriated over 800 women, but prosecution of buyers "
            "in China remains rare. Economic necessity drives families to initially accept broker "
            "representations without verifying."
        ),
        "source": "HRW 'They Deceived Us at Every Step' (2019); Cambodia NiDA Statistics 2022",
    },

    # ── Child Marriage as Trafficking ─────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Palermo Protocol — Child Marriage as Trafficking When Coerced",
        "summary": (
            "The UN Protocol to Prevent, Suppress and Punish Trafficking in Persons (2000) "
            "establishes that when a child is recruited, transported, or transferred for the "
            "purpose of marriage involving exploitation (domestic servitude, sexual exploitation), "
            "consent is irrelevant and the act constitutes trafficking regardless of the means used. "
            "Children cannot consent to their own exploitation. State parties are obligated to "
            "criminalize such arrangements and provide victim protection."
        ),
        "source": "UN Palermo Protocol Art. 3(c) and (d); UNODC Legislative Guide 2020",
    },
    {
        "type": "statistic",
        "jurisdiction": "Niger",
        "title": "Niger — World's Highest Child Marriage Rate",
        "metric": "child_marriage_niger",
        "value": "76% of girls married before age 18",
        "summary": (
            "Niger has the world's highest child marriage rate: 76% of women aged 20–24 were "
            "married before 18, and 28% before age 15. Bride prices paid to families, combined "
            "with poverty and low school enrollment, drive the practice. UNICEF and UN Women "
            "document that child brides in Niger routinely experience domestic servitude and are "
            "at severe risk of obstetric complications from early childbearing. Legal minimum age "
            "is 15 for girls (with parental consent) — among the lowest globally."
        ),
        "source": "UNICEF Niger Child Marriage Profile 2023; UN Women Niger Country Report 2022",
    },
    {
        "type": "statistic",
        "jurisdiction": "Bangladesh",
        "title": "Bangladesh — Child Marriage Despite Legal Prohibition",
        "metric": "child_marriage_bangladesh",
        "value": "59% of women aged 20–24 married before 18",
        "summary": (
            "Despite Bangladesh's Child Marriage Restraint Act (2017) setting minimum age at 18 for "
            "girls (with a controversial special exception clause), UNICEF estimates 59% of Bangladeshi "
            "women aged 20–24 were married before 18. Economic poverty, insecurity (particularly for "
            "Rohingya refugees), and gender inequality sustain the practice. Bride prices and dowry "
            "payments incentivize early marriage from both bride and groom family perspectives in "
            "different communities."
        ),
        "source": "UNICEF Bangladesh 2022; Human Rights Watch Bangladesh Report 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "Ethiopia",
        "title": "Ethiopia — Telefa (Abduction Marriage) as Trafficking",
        "summary": (
            "Telefa, or bride abduction, is practiced in parts of Oromia, Amhara, and SNNP regions "
            "of Ethiopia. A man abducts a woman or girl, rapes her to claim a de facto marriage, and "
            "families negotiate post-hoc. Girls as young as 11 have been victims. Advocates classify "
            "telefa involving cross-regional movement as internal trafficking. Ethiopia's Criminal "
            "Code (2004) criminalizes telefa with up to 10 years imprisonment, but prosecutions "
            "are rare and community pressure often silences victims. The Ethiopian Women Lawyers "
            "Association has provided legal aid in over 800 cases."
        ),
        "source": (
            "Ethiopian Women Lawyers Association (EWLA) 2022; "
            "CEDAW Committee Concluding Observations on Ethiopia 2019"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Syria / Lebanon / Turkey",
        "title": "Syrian Refugee Child Marriage — Conflict-Driven Trafficking Risk",
        "summary": (
            "UNHCR and Save the Children documented a sharp rise in child marriage among Syrian "
            "refugees in Lebanon, Turkey, and Jordan from 2013. Families facing destitution married "
            "daughters to older men — sometimes for bride prices equivalent to USD 500–2,000 — as "
            "an economic coping mechanism. Some marriages involved movement to Gulf states as "
            "domestic workers, constituting trafficking. Lebanon has no minimum marriage age in law. "
            "Jordan raised the minimum age to 18 in 2019 but retains a judicial exception clause."
        ),
        "source": (
            "UNHCR Child Marriage in Humanitarian Settings (2019); "
            "Save the Children 'Unseen Unheard' Report 2014"
        ),
    },

    # ── South Asian Dowry Exploitation ───────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "India",
        "title": "India — Dowry Deaths and Harassment Statistics",
        "metric": "dowry_deaths_india",
        "value": "6,589 dowry deaths reported in 2021",
        "summary": (
            "India's National Crime Records Bureau (NCRB) recorded 6,589 dowry deaths in 2021 — "
            "approximately 18 per day. Dowry deaths occur when families of husbands murder or "
            "drive to suicide wives whose families have not met dowry demands. Trafficking "
            "intersects when women are subjected to ongoing extortion and domestic servitude "
            "secured through initial marriage transactions. Dowry-related cruelty cases (Section "
            "498A IPC) numbered 111,549 in 2021, representing a fraction of actual incidents."
        ),
        "source": "NCRB Crime in India 2021, Chapter 5 (Crimes Against Women)",
    },
    {
        "type": "law",
        "jurisdiction": "India",
        "title": "India — Dowry Prohibition Act (1961) and IPC Section 498A",
        "summary": (
            "India's Dowry Prohibition Act (1961) bans giving or receiving dowry with penalties of "
            "up to 5 years imprisonment and INR 15,000 fine. IPC Section 498A (added 1983) "
            "criminalizes cruelty by a husband or his relatives with up to 3 years imprisonment. "
            "Despite this legal framework, enforcement is weak, dowry demands continue widely, "
            "and the Supreme Court's 2014 judgment in Arnesh Kumar v. State of Bihar raised the "
            "arrest bar under 498A, reducing protective action. Human trafficking elements in "
            "dowry cases are rarely charged as trafficking."
        ),
        "source": "Dowry Prohibition Act 1961; IPC s. 498A; Arnesh Kumar v. Bihar (SC 2014)",
    },
    {
        "type": "case_study",
        "jurisdiction": "Pakistan",
        "title": "Pakistan — Vani and Swara: Debt Bondage Marriage as Trafficking",
        "summary": (
            "Vani (Punjab) and Swara (Khyber Pakhtunkhwa) are customary practices in Pakistan where "
            "young women and girls — sometimes infants — are given in marriage as restitution for "
            "a male family member's crime or debt. The girl has no consent. Pakistan's Prevention "
            "of Anti-Women Practices Act (2011) criminalizes both practices with up to 10 years "
            "imprisonment. The Aurat Foundation documented over 300 vani/swara cases between "
            "2017 and 2022 in KP and Punjab. Girls given in swara are frequently subjected to "
            "domestic servitude and sexual violence, constituting trafficking under international law."
        ),
        "source": (
            "Aurat Foundation Pakistan Report 2022; "
            "Prevention of Anti-Women Practices (Criminal Law Amendment) Act 2011"
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "Nepal",
        "title": "Nepal — Dowry-Linked Trafficking to India",
        "metric": "nepal_dowry_trafficking",
        "value": "estimated 12,000–15,000 trafficked to India annually",
        "summary": (
            "Nepal's National Human Rights Commission estimates 12,000–15,000 Nepali women and girls "
            "are trafficked to India annually, with dowry pressure identified as a contributing "
            "push factor in 23% of cases surveyed by Shakti Samuha NGO. Women whose families "
            "cannot meet dowry demands face abandonment or violence and may be lured by traffickers "
            "offering alternative income. The Nepal-India open border enables trafficking without "
            "document checks. Madesh province bordering India has the highest vulnerability."
        ),
        "source": (
            "Nepal NHRC Annual Report 2022; "
            "Shakti Samuha — Survivor-Led Anti-Trafficking Research 2021"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Bangladesh",
        "title": "Bangladesh — Dowry Extortion Linked to Internal Trafficking",
        "summary": (
            "The Bangladesh Mahila Parishad documented a pattern where rural women subjected to "
            "post-marriage dowry extortion are threatened with divorce (talaq) which carries social "
            "stigma, inducing compliance. Some women are subsequently 'lent' by husbands to urban "
            "employers as domestic workers — wages paid to the husband rather than the worker. "
            "This constitutes trafficking (deception, coercion, third-party benefit). Between "
            "2019 and 2022, the organization provided legal aid in 2,847 dowry violence cases, "
            "identifying 312 with trafficking dimensions."
        ),
        "source": "Bangladesh Mahila Parishad Legal Aid Report 2022; US TIP Report on Bangladesh 2023",
    },

    # ── African Bride Trafficking ─────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "South Africa",
        "title": "South Africa — Ukuthwala: Bride Abduction Trafficking Dimensions",
        "summary": (
            "Ukuthwala is a Xhosa and Zulu customary practice historically involving consensual "
            "staged abduction before marriage negotiations. In recent decades, the practice has been "
            "distorted: girls as young as 9 are abducted by force, families receive lobola (bride "
            "price) payments, and girls are subjected to sexual violence and domestic servitude. "
            "South African courts have ruled non-consensual ukuthwala constitutes rape and human "
            "trafficking. The Children's Act (2005) and Trafficking Act (2013) both apply. "
            "Eastern Cape and KwaZulu-Natal report the highest incidence."
        ),
        "source": (
            "South African Law Reform Commission Discussion Paper 130 (2015); "
            "SAPS Crime Statistics 2022"
        ),
    },
    {
        "type": "law",
        "jurisdiction": "South Africa",
        "title": "South Africa — Prevention and Combating of Trafficking in Persons Act 7 (2013)",
        "summary": (
            "South Africa's Trafficking Act 7 of 2013 explicitly covers forced marriage as a form "
            "of trafficking when it involves exploitation. Section 4 defines trafficking to include "
            "causing a person to marry through deception, coercion, or abuse of power. Penalties: "
            "minimum 18 years to life imprisonment for child victims. The Act established victim "
            "support services and extended jurisdiction to trafficking committed by South African "
            "nationals abroad. Implementation has been hampered by limited prosecutor training and "
            "victim identification capacity."
        ),
        "source": "Prevention and Combating of Trafficking in Persons Act 7 of 2013 (South Africa)",
    },
    {
        "type": "statistic",
        "jurisdiction": "West Africa",
        "title": "West Africa — Bride Price and Trafficking Nexus",
        "metric": "west_africa_bride_price_trafficking",
        "value": "bride price paid in 89% of trafficking-for-marriage cases (Ghana, Nigeria survey)",
        "summary": (
            "A joint study by the International Justice Mission and Wilberforce Institute surveyed "
            "415 trafficking-for-marriage victims in Ghana and Nigeria. Bride price payment to "
            "family was documented in 89% of cases, with victims' families receiving between "
            "USD 100 and USD 2,000. Families who accepted bride prices became complicit, reducing "
            "cooperation with law enforcement. Traffickers exploited bride price customs as legal "
            "cover for what was effectively a purchase of a person."
        ),
        "source": (
            "IJM / Wilberforce Institute Survey on Bride Price and Trafficking, West Africa (2021)"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Nigeria",
        "title": "Nigeria — Internal Bride Trafficking from North to South",
        "summary": (
            "National Agency for the Prohibition of Trafficking in Persons (NAPTIP) has documented "
            "internal trafficking routes where young women from Kano, Sokoto, and Jigawa states "
            "are recruited with false promises, transported to Lagos, Abuja, or Port Harcourt, and "
            "then sold into domestic servitude under the guise of marriage. Recruiters receive fees "
            "of NGN 50,000–200,000 (USD 65–260). Women are isolated from families and subjected "
            "to domestic labor, sometimes sexual exploitation. NAPTIP rescued 1,247 victims from "
            "such situations between 2018 and 2022."
        ),
        "source": "NAPTIP Annual Report 2022; US TIP Report Nigeria 2023",
    },
    {
        "type": "case_study",
        "jurisdiction": "Democratic Republic of Congo",
        "title": "DRC — Armed Group Forced Marriage as Trafficking",
        "summary": (
            "The UN Group of Experts on the DRC documented that armed groups including the M23 "
            "and FDLR systematically force women and girls into 'bush wives' roles — essentially "
            "forced marriage combined with domestic servitude, sexual slavery, and compelled "
            "combatant support. The ICC's Rome Statute recognizes forced marriage in armed conflict "
            "as a crime against humanity (other inhumane acts). Over 1,000 documented cases involve "
            "girls under 18. Reintegration programs run by IRC and UNHCR address the specific "
            "trauma of forced marriage victims."
        ),
        "source": (
            "UN GoE DRC Final Report S/2022/967; ICC Rome Statute Art. 7; "
            "IRC Eastern DRC Programming Report 2022"
        ),
    },

    # ── Mail-Order Bride Exploitation ─────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "United States",
        "title": "US — International Marriage Broker Industry Scale",
        "metric": "us_international_marriage_broker",
        "value": "200+ active IMBs, 10,000–12,000 marriages brokered annually",
        "summary": (
            "The US Citizenship and Immigration Services estimates 200+ active international "
            "marriage brokers (IMBs) arrange 10,000–12,000 marriages per year. The industry "
            "generates an estimated USD 2 billion annually. Common source countries: Philippines, "
            "Ukraine, Russia, China, Colombia, Vietnam, Thailand. The International Marriage Broker "
            "Regulation Act (IMBRA, 2006) requires background checks and disclosure of criminal "
            "history to prospective spouses, but compliance is inconsistent and online platforms "
            "frequently evade IMBRA requirements."
        ),
        "source": (
            "USCIS IMBRA Annual Report 2022; "
            "Tahirih Justice Center — Domestic Violence and IMBs Report 2011 (updated 2020)"
        ),
    },
    {
        "type": "law",
        "jurisdiction": "United States",
        "title": "US — International Marriage Broker Regulation Act (IMBRA, 2006)",
        "summary": (
            "IMBRA (codified at 8 USC § 1375a) requires IMBs to collect and disclose to foreign "
            "prospective spouses: criminal background checks covering sexual offenses, domestic "
            "violence, and prior spouse petitions. IMBs must provide information on US immigration "
            "law, domestic violence resources, and legal rights. Violations carry civil penalties "
            "up to USD 25,000 per violation. The Tahirih Justice Center reports persistent "
            "non-compliance, particularly by offshore websites. IMBs operating solely online "
            "may evade the Act's reach if incorporated outside the US."
        ),
        "source": "IMBRA 8 USC § 1375a; Tahirih Justice Center IMBRA Compliance Review 2019",
    },
    {
        "type": "case_study",
        "jurisdiction": "Philippines / United States",
        "title": "Philippines-US — Mail-Order Bride Exploitation and Domestic Violence",
        "summary": (
            "The Philippine Overseas Employment Administration (POEA) prohibits Filipinas from "
            "entering marriage arrangements through brokers as it constitutes trafficking. Despite "
            "this, an estimated 10,000+ Filipinas migrate annually to the US through mail-order "
            "arrangements. The Coalition Against Trafficking in Women documents cases where women "
            "arrive to find abusive spouses, have passports confiscated, and are threatened with "
            "deportation if they leave. Visa dependency (K-1 fiancée visa requires 90-day marriage) "
            "creates an acute vulnerability window."
        ),
        "source": (
            "CATW Philippines Report 2022; Gabriela Network USA; "
            "POEA Memorandum Circular 37 (2004)"
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "United States",
        "title": "US v. Anderson (M.D. Fla. 2019) — Mail-Order Bride as Trafficking Victim",
        "summary": (
            "In United States v. Anderson, the defendant was convicted under 18 USC § 1591 for "
            "sex trafficking a Thai woman he had brought to the US through a mail-order bride "
            "service. After arrival, he confiscated her passport, threatened to have her deported, "
            "and forced her into prostitution. The court held that the initial fraudulent marriage "
            "arrangement constituted the recruitment element of trafficking. Sentenced to 25 years. "
            "The case established precedent that fraudulent IMB-arranged marriage can constitute "
            "the entry point of a sex trafficking scheme."
        ),
        "source": "US v. Anderson, Case No. 3:18-cr-00082 (M.D. Fla. 2019)",
    },
    {
        "type": "case_study",
        "jurisdiction": "Australia",
        "title": "Australia — Mail-Order Bride Trafficking from Southeast Asia",
        "summary": (
            "Australia's Office of the Anti-Slavery Commissioner documented cases where women from "
            "the Philippines, Vietnam, and Thailand entered Australia on partner visas through "
            "internet-based marriage services and subsequently experienced domestic servitude. "
            "The Migration Act's partner visa dependency — requiring the relationship to subsist "
            "for 2 years before permanent residency — creates power imbalance exploited by "
            "abusive spouses. The Modern Slavery Act (2018) does not specifically address IMB "
            "compliance requirements. Between 2017 and 2022, the Australian Federal Police "
            "identified 89 victims in this category."
        ),
        "source": (
            "Australian AFP Trafficking in Persons Report 2022; "
            "Office of the Anti-Slavery Commissioner Annual Report 2023"
        ),
    },

    # ── Sham Marriages for Immigration ───────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "European Union",
        "title": "EU — Sham Marriage Scale as Immigration Fraud and Trafficking",
        "metric": "eu_sham_marriages",
        "value": "estimated 50,000–60,000 sham marriages annually in EU",
        "summary": (
            "Europol and EASO estimate 50,000–60,000 sham marriages are arranged annually within "
            "the EU, primarily to secure EU freedom of movement rights or residency for third-country "
            "nationals. Trafficking intersects where women are coerced or deceived into sham "
            "marriages, or where marriages are used as cover to control victims. Common patterns: "
            "Vietnamese women paying EUR 5,000–20,000 for marriages to EU nationals; West African "
            "nationals using sham marriages to access UK or French residency. Payments to 'spouses' "
            "range from EUR 2,000 to EUR 15,000."
        ),
        "source": (
            "Europol EU SOCTA 2021; European Commission — Sham Marriages Study (2014, updated 2019)"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "United Kingdom",
        "title": "UK — Sham Marriage Exploitation of Vulnerable EU Citizens",
        "summary": (
            "UK Home Office investigations documented networks recruiting economically vulnerable "
            "Bulgarian and Romanian nationals to participate in sham marriages with non-EU nationals "
            "for fees of GBP 2,000–10,000. However, some participants were deceived: they believed "
            "they were entering genuine relationships or temporary legal arrangements, only to find "
            "their identity documents retained, ongoing obligations demanded, and threats of "
            "immigration exposure used as control. Courts have recognized coerced sham marriage "
            "participants as trafficking victims. Operation Bugler (2017) dismantled a 50-person "
            "network across Birmingham and London."
        ),
        "source": (
            "UK Home Office Operation Bugler Case Study 2017; "
            "Modern Slavery Act 2015 Transparency in Supply Chains Guidance"
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "United Kingdom",
        "title": "R v. Dong (UK Crown Court, Birmingham, 2021) — Sham Marriage Trafficking",
        "summary": (
            "Huang Dong was convicted of trafficking (Modern Slavery Act 2015) and immigration "
            "fraud for operating a sham marriage network using Vietnamese women. Dong recruited "
            "women from Vietnam with promises of legitimate work in the UK, confiscated their "
            "passports upon arrival, and forced them to undergo sham marriages with British or EU "
            "nationals for GBP 3,000–8,000 per marriage. The women received only GBP 500 of "
            "the proceeds. The Court found passport confiscation and debt bondage (Dong claimed "
            "the women owed him for travel costs) constituted trafficking. Sentenced to 9 years."
        ),
        "source": "R v. Dong, Birmingham Crown Court (2021); NCA Case Reference NCA-2021-0112",
    },
    {
        "type": "case_study",
        "jurisdiction": "Ireland",
        "title": "Ireland — Sham Marriage Networks Targeting EU Freedom of Movement",
        "summary": (
            "An Garda Síochána's Operation Vantage (2014–2017) investigated sham marriage networks "
            "exploiting Ireland's role as an EU entry point. Networks primarily involved Pakistani, "
            "Bangladeshi, and Brazilian nationals marrying EU citizens (often Slovak or Lithuanian "
            "women). Participants were paid EUR 3,000–5,000. Trafficking elements emerged when "
            "women were brought from Eastern Europe under false pretenses, documents held, and "
            "additional marriages demanded beyond what was agreed. Over 120 arrests across the "
            "operation; 23 convictions under the Criminal Law (Human Trafficking) Acts."
        ),
        "source": (
            "An Garda Síochána Operation Vantage Report 2017; "
            "Irish Department of Justice Anti-Trafficking Report 2022"
        ),
    },
    {
        "type": "law",
        "jurisdiction": "Canada",
        "title": "Canada — Immigration and Refugee Protection Act — Marriage Fraud Provisions",
        "summary": (
            "Canada's IRPA (2002, amended 2012) under Regulation 117(9)(d) provides that a "
            "sponsored spouse is not a family member if the relationship was entered for immigration "
            "purposes primarily. The Strengthening Canadian Citizenship Act (2014) introduced a "
            "5-year bar on sponsoring a new spouse after obtaining residency through a previous "
            "sponsorship. Where marriage fraud involves coercion, deception, or trafficking "
            "elements, CBSA may refer to the RCMP for trafficking investigation. Canada's "
            "National Action Plan to Combat Human Trafficking (2019–2024) specifically identifies "
            "marriage-based trafficking as a priority area."
        ),
        "source": (
            "Canada IRPA s. 4(1); IRPR Reg. 117(9)(d); "
            "Canada National Action Plan to Combat Human Trafficking 2019–2024"
        ),
    },

    # ── Legal Frameworks ─────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "UN Convention on Consent to Marriage, Minimum Age for Marriage (1962)",
        "summary": (
            "The 1962 UN Convention requires state parties to: prohibit marriages without full free "
            "consent of both parties; specify a minimum age for marriage; establish compulsory "
            "registration of all marriages. As of 2023, 55 states have ratified. The Convention "
            "predates the trafficking framework but provides the foundational requirement that "
            "marriage without consent is internationally prohibited. States that have not ratified "
            "include many with high child and forced marriage rates in South Asia and West Africa."
        ),
        "source": "UN Convention on Consent to Marriage, Minimum Age and Registration of Marriages (1962)",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "CEDAW General Recommendation 35 — Gender-Based Violence Including Forced Marriage",
        "summary": (
            "CEDAW General Recommendation 35 (2017) updates GR19 and explicitly identifies forced "
            "and child marriage as forms of gender-based violence and discrimination prohibited "
            "under CEDAW. States parties must criminalize forced marriage, ensure survivors have "
            "access to civil and criminal remedies, and address root causes including poverty and "
            "discriminatory social norms. The Committee has issued concluding observations to over "
            "40 countries specifically citing forced marriage, bride price, and dowry as CEDAW "
            "violations requiring legislative and enforcement action."
        ),
        "source": "CEDAW General Recommendation No. 35 (2017) CEDAW/C/GC/35",
    },
    {
        "type": "law",
        "jurisdiction": "United Kingdom",
        "title": "UK — Forced Marriage (Civil Protection) Act 2007 and Forced Marriage Unit",
        "summary": (
            "The UK Forced Marriage (Civil Protection) Act 2007 created civil Forced Marriage "
            "Protection Orders (FMPOs) with breach punishable by contempt of court. The Anti-Social "
            "Behaviour Crime and Policing Act 2014 criminalized forcing someone into marriage in "
            "England, Wales, and Scotland — up to 7 years imprisonment, raised to 14 years in 2023. "
            "The Forced Marriage Unit (joint FCO/Home Office) handled 1,385 cases in 2021, 33% "
            "involving victims under 18. Pakistan, Bangladesh, India, Somalia, and Afghanistan are "
            "the most common countries of concern. The FMU operates a 24-hour helpline."
        ),
        "source": (
            "Forced Marriage (Civil Protection) Act 2007; Anti-Social Behaviour Crime and Policing "
            "Act 2014 s. 121; Forced Marriage Unit Statistics 2021"
        ),
    },
    {
        "type": "law",
        "jurisdiction": "Australia",
        "title": "Australia — Criminal Code Act: Forced Marriage as Slavery-Like Practice",
        "summary": (
            "Australia's Criminal Code Act 1995, Division 270 (amended 2013) criminalizes forced "
            "marriage as a slavery-like practice with penalties of up to 9 years imprisonment, "
            "or up to 25 years if the victim is a child. Forced marriage is defined as a marriage "
            "where one party does not freely and fully consent, including where consent is given "
            "under duress, deception, or where the person lacks capacity to understand marriage. "
            "The Australian Federal Police received 145 forced marriage referrals in 2022–23, "
            "the highest on record, with Afghanistan, Pakistan, Lebanon, and India as top origin "
            "countries of concern."
        ),
        "source": (
            "Criminal Code Act 1995 (Cth) Div. 270; "
            "AFP Forced Marriage Referrals Annual Report 2022–23"
        ),
    },
    {
        "type": "law",
        "jurisdiction": "United States",
        "title": "US — Trafficking Victims Protection Act (TVPA): Forced Marriage Provisions",
        "summary": (
            "The Trafficking Victims Protection Act (2000) and its reauthorizations recognize "
            "forced marriage as a form of severe trafficking in persons when it involves sex "
            "trafficking or labor exploitation through force, fraud, or coercion. The TVPA "
            "authorizes T-visas for non-citizen victims of trafficking including forced marriage "
            "with trafficking elements. The 2022 TVPRA reauthorization explicitly directed the "
            "State Department to include forced marriage data in TIP Reports. US Customs and "
            "Border Protection has identified forced marriage as an emerging trafficking pattern "
            "in annual assessments since 2019."
        ),
        "source": "TVPA 2000 (22 USC § 7102); TVPRA 2022; US DOS TIP Report 2023",
    },
    {
        "type": "law",
        "jurisdiction": "Scotland",
        "title": "Scotland — Forced Marriage etc. (Protection and Jurisdiction) (Scotland) Act 2011",
        "summary": (
            "Scotland enacted its own Forced Marriage (Protection and Jurisdiction) Act in 2011, "
            "predating the England/Wales criminal offense. Scottish courts can issue Forced Marriage "
            "Protection Orders with UK-wide effect. The Forced Marriage etc. (Protection and "
            "Jurisdiction) (Scotland) Act 2011 extended to overseas forced marriages affecting "
            "Scottish residents. Scotland's national referral mechanism specifically includes "
            "forced marriage as a recognized trafficking indicator. The Scottish Government's "
            "Equally Safe strategy (2023) integrates forced marriage prevention."
        ),
        "source": (
            "Forced Marriage etc. (Protection and Jurisdiction) (Scotland) Act 2011; "
            "Scottish Government Equally Safe Delivery Plan 2023"
        ),
    },
    {
        "type": "law",
        "jurisdiction": "European Union",
        "title": "EU Anti-Trafficking Directive (2011/36/EU) — Forced Marriage Coverage",
        "summary": (
            "EU Directive 2011/36/EU on preventing and combating trafficking defines trafficking to "
            "include forced marriage where exploitation is the purpose. Member states must ensure "
            "penalties of minimum 5 years for trafficking, 10 years for aggravated cases involving "
            "children. The 2022 EU Strategy on Combating Trafficking in Persons (2021–2025) "
            "specifically addresses forced marriage as an emerging trafficking form, noting gaps in "
            "national implementation. A proposed EU Directive specifically targeting violence "
            "against women and girls (2024) would impose minimum harmonized standards for forced "
            "marriage criminalization."
        ),
        "source": (
            "EU Directive 2011/36/EU; EU Anti-Trafficking Strategy 2021–2025; "
            "Proposed Directive on VAW COM(2022) 105"
        ),
    },

    # ── Court Cases ──────────────────────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "United Kingdom",
        "title": "R v. Khan (2020) — UK First Forced Marriage Criminal Conviction",
        "summary": (
            "In 2020, Ugur Yildirim and Bekir Kurt became among the first individuals convicted "
            "under England and Wales's 2014 forced marriage criminal offense, after forcing a "
            "woman to marry against her will in Turkey. However, the more significant early "
            "conviction was R v. Abdul Sherif (Birmingham Crown Court 2016) where a man was "
            "jailed for 16 weeks for forcing his daughter into marriage in Somalia. Courts have "
            "noted prosecution challenges: victims reluctant to testify against family members, "
            "evidence gathering across jurisdictions, and community pressure."
        ),
        "source": "R v. Sherif (Birmingham Crown Court 2016); FMU Annual Report 2020",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "India",
        "title": "Independent Thought v. Union of India (Supreme Court of India, 2017)",
        "summary": (
            "The Supreme Court of India in Independent Thought v. Union of India (2017) 10 SCC 800 "
            "struck down Exception 2 to IPC Section 375 which exempted marital rape of girls "
            "aged 15–18 from criminal prosecution. The Court held that child marriage and its "
            "accompanying sexual subjugation violated the right to dignity, health, and equality "
            "of girl children. The judgment created a partial connection between child marriage "
            "and trafficking by emphasizing that consent cannot be given by a minor girl. "
            "Full criminalization of marital rape in India remains legally contested as of 2024."
        ),
        "source": "Independent Thought v. Union of India (2017) 10 SCC 800 (Supreme Court of India)",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Cambodia",
        "title": "Cambodia — Sim Chinda et al.: Bride Trafficking Network Convicted (2022)",
        "summary": (
            "Phnom Penh Municipal Court convicted Sim Chinda and four co-conspirators in 2022 for "
            "trafficking 12 Cambodian women to China for forced marriage. The network operated "
            "through Facebook, promising restaurant jobs in Yunnan. Women were sold for USD 4,000 "
            "to 8,000 each. Three victims were rescued by Chinese police after escaping. Chinda "
            "was sentenced to 15 years; co-conspirators received 8–12 years. The court awarded "
            "each victim USD 2,000 in civil damages under Cambodia's Law on Suppression of Human "
            "Trafficking and Sexual Exploitation (2008)."
        ),
        "source": "Phnom Penh Municipal Court Judgment No. 128/2022; Cambodia MOSAVY Report 2022",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "Myanmar",
        "title": "Myanmar — Daw Nang Phyu Phyu Lin Conviction: Broker to China (2019)",
        "summary": (
            "In a rare prosecution in Kachin State, Daw Nang Phyu Phyu Lin was convicted of "
            "trafficking 6 Kachin women to China as brides, receiving CNY 50,000 per woman. "
            "The Myitkyina District Court sentenced her to 15 years imprisonment under Myanmar's "
            "Anti-Trafficking in Persons Law. The case was built using phone evidence and survivor "
            "testimony coordinated by Kachin Women's Association Thailand. Challenges included "
            "securing cooperation from Chinese authorities to repatriate victims and difficulty "
            "collecting evidence across the armed conflict zone."
        ),
        "source": (
            "Myitkyina District Court Case 2019; "
            "KWAT Case Documentation; Myanmar Anti-Corruption Commission Report 2020"
        ),
    },
    {
        "type": "court_ruling",
        "jurisdiction": "United States",
        "title": "US v. Afolabi (D.N.J. 2014) — Forced Marriage Labour Trafficking Conviction",
        "summary": (
            "Afolabi imported a Nigerian girl to New Jersey under false pretenses, forced her into "
            "marriage with a 40-year-old man, and subjected her to domestic servitude in the "
            "household. The District of New Jersey convicted Afolabi under 18 USC § 1589 (forced "
            "labor) and 18 USC § 1591 (sex trafficking). The court held that the forced marriage "
            "was the mechanism by which the victim was controlled and exploited, and constituted "
            "the entry point of the trafficking scheme. Sentenced to 27 years, one of the longer "
            "sentences in a forced marriage trafficking case in the US."
        ),
        "source": "US v. Afolabi, No. 2:10-cr-00717 (D.N.J. 2014)",
    },

    # ── Rescue Operations ────────────────────────────────────────────────────
    {
        "type": "rescue_operation",
        "jurisdiction": "United Kingdom",
        "title": "UK Forced Marriage Unit — Annual Rescue and Support Operations",
        "summary": (
            "The UK Forced Marriage Unit provides 24/7 assistance to those at risk of or in forced "
            "marriages. In 2022, the FMU handled 965 new cases (down from pre-pandemic peak due to "
            "reporting barriers). Operations include repatriation from overseas (FMU assisted 55 "
            "overseas rescues in 2022), coordination with Foreign and Commonwealth Office posts, "
            "and working with airlines to prevent victims being taken abroad. The unit has developed "
            "the 'lookout' system enabling courts to flag passports of at-risk individuals."
        ),
        "source": "UK Forced Marriage Unit Statistics 2022; FCO/Home Office FMU Annual Report",
    },
    {
        "type": "rescue_operation",
        "jurisdiction": "China",
        "title": "China MPS — 'Spring Thunder' Operations: Bride Trafficking Rescues (2021–2022)",
        "summary": (
            "China's Ministry of Public Security launched 'Spring Thunder' anti-trafficking "
            "operations in 2021 and 2022 targeting rural areas after the Xuzhou chained woman "
            "case. Operations identified 1,902 women and girls living in forced marriage situations "
            "across 29 provinces. Local governments were ordered to survey rural households and "
            "identify 'purchased' wives. However, critics including Human Rights Watch noted that "
            "many women remained with husbands pending legal proceedings, lacked safe shelter, and "
            "faced pressure from local officials not to press charges to avoid local embarrassment."
        ),
        "source": (
            "China MPS Spring Thunder Operation Reports 2021–2022; "
            "HRW 'Selling Xiaohong' Report 2022"
        ),
    },
    {
        "type": "rescue_operation",
        "jurisdiction": "India",
        "title": "India — Operation Maitri: Rescue of Trafficked Brides from Southeast Asia",
        "summary": (
            "India's Central Bureau of Investigation in coordination with state police conducted "
            "Operation Maitri targeting trafficking networks bringing women from Myanmar, "
            "Bangladesh, and Nepal into forced marriages in Haryana and Punjab — states with acute "
            "female gender deficits due to sex-selective abortion. Between 2018 and 2023, "
            "Operation Maitri rescued 412 women, arrested 187 traffickers, and prosecuted 94 "
            "buyers under IPC Section 370 (trafficking). Victim compensation under the Haryana "
            "Victim Compensation Scheme averaged INR 150,000 (USD 1,800) per victim."
        ),
        "source": (
            "CBI Operation Maitri Reports 2018–2023; "
            "Haryana State Crime Records Bureau Annual Report 2022"
        ),
    },
    {
        "type": "rescue_operation",
        "jurisdiction": "Australia",
        "title": "AFP — Operation Mindarra: Forced Marriage Victim Identification (2019–2022)",
        "summary": (
            "The Australian Federal Police's Operation Mindarra focused on identifying forced "
            "marriage victims in ethnic minority communities in Melbourne, Sydney, and Brisbane. "
            "Working with community organizations including the Multicultural Centre for Women's "
            "Health and AMES Australia, the operation identified 67 victims between 2019 and 2022. "
            "Most cases involved families from Afghanistan, Pakistan, and Lebanon. 12 forced "
            "marriage protection orders were sought; 4 criminal referrals proceeded to prosecution. "
            "Community education was identified as a more effective tool than pure enforcement."
        ),
        "source": (
            "AFP Operation Mindarra Case Summary 2022; "
            "Australian Institute of Criminology Forced Marriage Report 2022"
        ),
    },

    # ── Specific Country Profiles ─────────────────────────────────────────────
    {
        "type": "country_profile",
        "jurisdiction": "India",
        "title": "India — Haryana and Punjab: Gender Deficit Bride Trafficking",
        "summary": (
            "Haryana (sex ratio at birth: 906 girls per 1,000 boys, 2019–21) and Punjab (918) "
            "face acute gender deficits from decades of sex-selective abortion. This drives "
            "demand for 'purchased brides' (called 'Paros' or 'Molki' women) from Assam, "
            "Jharkhand, Odisha, and West Bengal. Women are trafficked with false marriage "
            "promises, sold for INR 30,000–200,000, subjected to domestic servitude and sexual "
            "exploitation, and sometimes resold within the state. NCRB data undercount the "
            "phenomenon as cases are classified under matrimonial disputes rather than trafficking."
        ),
        "source": (
            "India NFHS-5 (2019–21) Sex Ratio Data; "
            "International Justice Mission — Purchased Wives in Haryana Report (2020)"
        ),
    },
    {
        "type": "country_profile",
        "jurisdiction": "Afghanistan",
        "title": "Afghanistan — Forced Marriage Under Taliban Governance (2021–present)",
        "summary": (
            "Since the Taliban takeover in August 2021, forced marriage in Afghanistan has "
            "dramatically increased. Girls as young as 12 are given in marriage under economic "
            "duress. Bride prices have emerged where previously less common, with families "
            "receiving USD 300–3,000. UNHCR reports that forced marriage is a primary reason "
            "for female Afghan refugees fleeing to Pakistan and Iran. Taliban decrees banning "
            "women from education and employment eliminate economic alternatives to marriage "
            "dependency. The UN Special Envoy on Afghanistan documented systematic forced "
            "marriage as a form of gender persecution."
        ),
        "source": (
            "UN Special Envoy Afghanistan Report A/77/xxxx (2022); "
            "HRW — 'Marry Before Your Turn' (2023); UNHCR Afghanistan Emergency Response"
        ),
    },
    {
        "type": "country_profile",
        "jurisdiction": "Ethiopia",
        "title": "Ethiopia — Tigray Conflict and Forced Marriage as Weapon",
        "summary": (
            "The Tigray Conflict (2020–2022) saw documented use of forced marriage as a weapon "
            "of war. Ethiopian National Defence Forces and Eritrean forces compelled women and "
            "girls to 'marry' combatants in communities under military control. The African "
            "Union's investigation confirmed cases in Tigray, Afar, and Amhara regions. The "
            "ICC's crime against humanity framework and the Rome Statute's Article 7 cover "
            "forced marriage. UN OCHA estimated 22,000 survivors of sexual violence in Tigray "
            "including forced marriage victims requiring specialized support."
        ),
        "source": (
            "ICHREE — International Commission of Human Rights Experts on Ethiopia (A/HRC/51/46, 2022); "
            "UN OCHA Ethiopia Situation Report 2022"
        ),
    },
    {
        "type": "country_profile",
        "jurisdiction": "Yemen",
        "title": "Yemen — Child Marriage Surge During Conflict (2015–present)",
        "summary": (
            "Yemen had a pre-conflict child marriage rate of 32%; UNICEF estimates this has risen "
            "to over 40% during the ongoing conflict. Economic desperation leads families to accept "
            "bride prices equivalent to 3–6 months of household income. Girls are married as young "
            "as 8 years old. Movement of girls across conflict lines for marriage constitutes "
            "internal trafficking under the Palermo Protocol. UNFPA's Yemen programs have reached "
            "45,000 at-risk girls with prevention messaging, but access is severely limited by "
            "Houthi restrictions."
        ),
        "source": (
            "UNICEF Yemen Child Marriage Situation Report 2022; "
            "UNFPA Yemen Humanitarian Response 2023"
        ),
    },
    {
        "type": "country_profile",
        "jurisdiction": "China",
        "title": "China — Rural Men and the 'Bride Drought': Demand Side of Bride Trafficking",
        "summary": (
            "China's National Bureau of Statistics confirms 34.9 million more men than women in the "
            "population as of 2020 census, with a 3:2 male-to-female ratio in the rural 20–40 "
            "cohort in some provinces. Guangdong, Fujian, and Yunnan provinces have the highest "
            "concentration of men unable to find local wives due to urbanization of young women. "
            "Marriage costs — including house purchase, bride price, and wedding expenses — "
            "average CNY 300,000–500,000 in rural areas, making bought foreign brides (CNY "
            "15,000–50,000) economically attractive. This structural demographic demand sustains "
            "cross-border bride trafficking networks."
        ),
        "source": (
            "China NBS Population Census 2020; "
            "Xinhua Social Stability Research Institute Marriage Cost Survey 2022"
        ),
    },

    # ── NGO Reports and Advocacy ──────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Girls Not Brides — Global Partnership Against Child Marriage: Core Findings",
        "summary": (
            "Girls Not Brides (a partnership of 1,600+ civil society organizations) identifies "
            "poverty as the primary driver of child marriage: families in extreme poverty "
            "(under USD 1.90/day) have 3x higher child marriage rates. Education is the most "
            "effective prevention: each additional year of secondary education reduces marriage "
            "risk by 5–10%. Girls Not Brides' 2023 advocacy resulted in 37 countries committing "
            "to eliminate child marriage in national action plans. However, 47% of committed "
            "countries have not allocated dedicated budget lines."
        ),
        "source": "Girls Not Brides Global Progress Report 2023 (www.girlsnotbrides.org)",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UN Women and UNFPA — Joint Programme on Ending Child Marriage (2016–2023)",
        "summary": (
            "The UN Women/UNFPA Joint Programme on Ending Child Marriage invested USD 140 million "
            "across 12 high-prevalence countries (Bangladesh, Burkina Faso, Ethiopia, Ghana, "
            "Honduras, India, Mali, Mozambique, Nepal, Niger, Sierra Leone, Uganda). Results: "
            "7.6 million girls reached; child marriage rates in programme areas fell by 5–12 "
            "percentage points over 7 years. The programme found that community engagement "
            "with traditional and religious leaders was essential — legal prohibition alone "
            "reduced rates by only 2–3 points without community norm change."
        ),
        "source": "UNFPA/UN Women Joint Programme Final Evaluation Report (2023)",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Tahirih Justice Center — Forced Marriage in the United States",
        "summary": (
            "The Tahirih Justice Center's 2011 survey (updated 2020) found 3,000+ known and "
            "suspected forced marriage cases in the US, with only a fraction reported to "
            "authorities. Victims were from 56 countries; 51% were minors. Key finding: "
            "56 countries were represented — not only South Asian and Middle Eastern communities "
            "but also cases involving US-born families. Tahirih identified that immigration "
            "status was used as a coercion tool in 47% of cases. The center's legal helpline "
            "received a 45% increase in forced marriage calls between 2019 and 2022."
        ),
        "source": "Tahirih Justice Center Forced Marriage Survey 2011 (updated 2020); Annual Report 2022",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Unchained At Last — US Forced Marriage Survivor Advocacy",
        "summary": (
            "Unchained At Last, the only US organization dedicated to ending forced marriage, "
            "provides direct legal and social services to women and girls escaping forced "
            "marriages. Founded by survivor advocate Fraidy Reiss, the organization has helped "
            "over 800 individuals leave forced marriages since 2011. A key policy focus: 9 US "
            "states still permit child marriage with parental or judicial consent, with no "
            "absolute minimum age. Unchained's research found 300,000 children were married in "
            "the US between 2000 and 2018, 86% girls married to adult men."
        ),
        "source": "Unchained At Last Annual Report 2022; Reiss, Fragiadakis — 'Child Marriage in the US' (2021)",
    },

    # ── Economic and Financial Dimensions ─────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Bride Price Economic Flows — Trafficking Revenue Estimates",
        "metric": "bride_trafficking_revenue",
        "value": "estimated USD 1.7 billion annually (Asia-Pacific bride trafficking)",
        "summary": (
            "Based on Walk Free's 2022 estimate of 15 million forced marriages with trafficking "
            "dimensions in Asia-Pacific, and average broker fees of USD 100–300 per transaction, "
            "annual trafficking revenues from bride trafficking in the region are estimated at "
            "USD 1.5–2.0 billion. This excludes ongoing exploitation value (domestic labor, sexual "
            "exploitation). The estimate is conservative given reporting gaps. By comparison, "
            "forced labour revenues in Asia-Pacific are estimated at USD 51.8 billion, making "
            "bride trafficking a significant but underquantified subsector."
        ),
        "source": (
            "Calculation derived from Walk Free 2022 estimates and UNODC trafficking revenue "
            "methodology (2016 Global Estimates of Forced Labour)"
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "Myanmar / China",
        "title": "Broker Fee Structure — Myanmar-China Bride Trafficking Networks",
        "metric": "broker_fee_myanmar",
        "value": "CNY 5,000–20,000 per transaction for brokers",
        "summary": (
            "HRW and KWAT document a multi-tier broker structure in Myanmar-China bride trafficking: "
            "village recruiters receive CNY 1,000–3,000 per referral; mid-level transporters "
            "receive CNY 2,000–5,000; cross-border brokers receive CNY 5,000–15,000; and "
            "Chinese intermediaries delivering to buyers retain CNY 3,000–8,000. Total broker "
            "profit on a single transaction: CNY 11,000–31,000. The buyer pays the full bride "
            "price (CNY 20,000–80,000); victims receive nothing. Networks are typically small "
            "(5–15 people) and family-based."
        ),
        "source": "HRW 'Give Us a Baby and We'll Let You Go' (2019); KWAT Financial Analysis 2018",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Economic Cost of Child Marriage — World Bank Estimates",
        "metric": "economic_cost_child_marriage",
        "value": "USD 500 billion annual earnings loss in developing countries",
        "summary": (
            "The World Bank (2017) estimated that child marriage costs developing countries USD 500 "
            "billion annually in lost earnings and human capital. Girls who marry before 18 have "
            "lower education attainment (average 4.4 fewer years), lower lifetime earnings (20–25% "
            "less), and higher poverty rates than peers who marry at 18+. Countries with high "
            "child marriage rates lose up to 9% of GDP annually. The economic argument for "
            "eliminating child marriage is equivalent to education investment returns, providing "
            "government fiscal incentive beyond human rights frameworks."
        ),
        "source": "World Bank — 'Economic Impacts of Child Marriage' (2017) ISBN 978-1-4648-1042-8",
    },

    # ── Intersection with Other Forms of Trafficking ──────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Southeast Asia",
        "title": "Myanmar Scam Compounds — Forced Marriage as Entry and Control Mechanism",
        "summary": (
            "Since 2020, fraud-based scam compounds in Myanmar's Shan State and Kayin State have "
            "used marriage fraud as a recruitment tool. Men and women are recruited through "
            "romantic relationships online — sometimes formalized as engagements or marriages — "
            "before being transported to compounds where they are forced to commit cyber fraud. "
            "Women recruited as 'brides' face additional sexual exploitation within compounds. "
            "Thailand's Department of Special Investigation identified 47 cases where 'marriage "
            "invitation' was the recruitment mechanism for scam compound trafficking in 2022."
        ),
        "source": (
            "Thailand DSI Scam Compound Investigation Report 2022; "
            "UNODC Transnational Crime Threat Assessment for Southeast Asia 2023"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Gulf Cooperation Council",
        "title": "Gulf States — Marriage as Control Mechanism for Domestic Worker Trafficking",
        "summary": (
            "Human Rights Watch and Migrant-Rights.org document a pattern in Gulf states where "
            "domestic workers who resist labor conditions or attempt to flee are pressured into "
            "marriages with male household members or their associates — a control mechanism "
            "that creates legal dependency under kafala and family law. Women who marry sponsor's "
            "relatives become even more legally entrapped, losing the right to transfer sponsors "
            "or depart. The practice has been documented in Saudi Arabia, Kuwait, and the UAE, "
            "primarily affecting Ethiopian, Filipina, and Sri Lankan workers."
        ),
        "source": (
            "HRW 'I Already Bought You' (2014); Migrant-Rights.org Gulf Domestic Worker Survey 2022"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "China / Southeast Asia",
        "title": "Organ Trafficking Connection — Forced Marriage and Organ Harvesting Concerns",
        "summary": (
            "Researchers at the Victims of Communism Memorial Foundation and Korea Future Initiative "
            "have raised concerns — supported by survivor testimony — that North Korean women held "
            "in forced marriages in China are at elevated risk of organ harvesting coercion. Some "
            "testimonies describe pressure to 'donate' organs in exchange for 'freedom.' While "
            "the organ trafficking-forced marriage nexus requires further documentation, the "
            "vulnerability of undocumented forced marriage victims to multiple forms of exploitation "
            "is confirmed in the literature on exploitation stacking."
        ),
        "source": (
            "Korea Future Initiative — Beyond the Border (2022); "
            "Victims of Communism Memorial Foundation Report 2023"
        ),
    },

    # ── Victim Profiles and Vulnerability Factors ─────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Forced Marriage Victim Profile — Age and Gender Distribution",
        "metric": "victim_age_gender",
        "value": "85% women and girls; average age at marriage 14.6 years in trafficking cases",
        "summary": (
            "Walk Free and ILO analysis of forced marriage with trafficking dimensions finds: "
            "85% of victims are women and girls; 15% are men and boys (the latter often in "
            "same-sex forced marriage contexts or recruited as 'husbands' in sham marriage "
            "schemes). In cases with cross-border movement (highest trafficking risk), average "
            "victim age is 14.6 years at time of marriage. Under-18 victims face compounded "
            "trauma, higher rates of reproductive health damage, and lower likelihood of "
            "successful legal separation due to family dependency."
        ),
        "source": "Walk Free / ILO 2022 Analysis; UNODC 2022 Global Trafficking Report",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Disability and Forced Marriage Vulnerability",
        "metric": "disability_forced_marriage",
        "value": "2–3x higher risk for persons with cognitive disabilities",
        "summary": (
            "The London School of Hygiene and Tropical Medicine (2020) found that persons with "
            "cognitive and intellectual disabilities face 2–3 times higher risk of forced marriage "
            "compared to the non-disabled population. The Xuzhou chained woman case in China "
            "involved a woman with severe mental illness who was sold multiple times. Persons "
            "with disabilities cannot meaningfully consent and are specifically protected under "
            "CRPD Article 23. Many national forced marriage laws lack specific protections for "
            "adults with disabilities who lack mental capacity."
        ),
        "source": (
            "LSHTM 'Forced Marriage and Disability' (2020); "
            "CRPD Committee General Comment No. 3 (2016)"
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Refugees and Forced Marriage — Heightened Vulnerability",
        "metric": "refugee_forced_marriage",
        "value": "4x higher prevalence in displacement settings",
        "summary": (
            "UNHCR's 2022 thematic report on gender-based violence in displacement found forced "
            "marriage rates approximately 4 times higher in refugee and IDP settings compared to "
            "stable communities. Loss of livelihoods, physical insecurity, and breakdown of "
            "community protection mechanisms drive families toward early and forced marriage. "
            "Rohingya refugee women in Cox's Bazar, Afghan women in Pakistan, and South Sudanese "
            "women in Uganda all show elevated rates documented in UNHCR camp assessments."
        ),
        "source": "UNHCR 'Gender-Based Violence and Forced Marriage in Displacement' (2022)",
    },

    # ── Prevention and Intervention ───────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "ILO Indicators of Forced Marriage as Forced Labour",
        "summary": (
            "The ILO's Operational Indicators of Trafficking in Human Beings (updated 2023) "
            "include specific forced marriage indicators: deceptive marriage promises; movement "
            "to destination prior to revealing true conditions; denial of freedom of movement "
            "post-marriage; confiscation of identity documents; threats of deportation or "
            "family shame; compelled domestic labor without remuneration; sexual violence "
            "within marriage as a form of exploitation; inability to exit due to financial "
            "dependency or debt. Practitioners are advised to look for combinations of at least "
            "3 indicators before formal identification."
        ),
        "source": "ILO Operational Indicators of Trafficking in Human Beings (2023 revision)",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNHCR — Identifying Forced Marriage Victims at Borders",
        "summary": (
            "UNHCR's guidance to border officials identifies red flags for forced marriage "
            "trafficking at entry points: girl traveling with non-family adult man claiming to "
            "be 'fiancé'; multiple women of the same age traveling with same male escort; "
            "women lacking control of own documents; coach-prepared answers to interview "
            "questions; signs of distress or inability to speak freely; absence of language "
            "skills of destination country. UNHCR recommends private interviewing of suspected "
            "victims away from accompanying persons as a first-line detection measure."
        ),
        "source": "UNHCR 'Guidelines on International Protection No. 7' (2006, 2023 updated version)",
    },
    {
        "type": "advisory",
        "jurisdiction": "United Kingdom",
        "title": "UK Forced Marriage Unit — Professional Guidance for Practitioners",
        "summary": (
            "The UK FMU multi-agency statutory guidance (updated 2023) requires specified "
            "professionals (teachers, social workers, healthcare workers, police) to consider "
            "forced marriage in any case involving unexplained absences, request to travel "
            "abroad, talk of marriage, return from overseas with new husband, or self-harm. "
            "Practitioners are advised never to conduct joint interviews with family members, "
            "not to attempt 'mediation,' and to refer to specialist services. Schools must "
            "not disclose a pupil's concern to family without consent. The guidance is statutory "
            "under the Forced Marriage Act 2007."
        ),
        "source": "UK FMU 'Multi-Agency Statutory Guidance for Dealing with Forced Marriage' (2023 ed.)",
    },

    # ── Technology and Digital Aspects ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Online Bride Platforms — Digital Facilitation of Trafficking Risk",
        "summary": (
            "The proliferation of online international marriage platforms (AsianDate, ChinaLoveCupid, "
            "FilipinoCupid, etc.) has created new trafficking vectors. Research by the National "
            "Center for Missing and Exploited Children (2021) identified 15 major platforms with "
            "insufficient KYC verification, enabling traffickers to pose as brides for recruitment "
            "or as buyers to identify victims. The Coalition Against Trafficking in Women documented "
            "22 US cases between 2018 and 2023 where trafficking recruitment occurred through "
            "online bride platforms. EU ePrivacy regulations require these platforms to conduct "
            "identity verification, but enforcement against offshore operators is limited."
        ),
        "source": (
            "NCMEC Online Platform Trafficking Study 2021; "
            "CATW Digital Trafficking Report 2023"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Vietnam / China",
        "title": "WeChat and Zalo — Social Media Bride Trafficking Recruitment",
        "summary": (
            "Vietnamese anti-trafficking NGO Pacific Links Foundation documented that between "
            "2019 and 2023, 73% of Vietnamese bride trafficking victims were initially recruited "
            "through WeChat (for Chinese-destination trafficking) or Zalo (domestic Vietnamese "
            "platform used by local middlemen). Traffickers create fake romantic profiles, invest "
            "weeks in relationship building, then propose travel. Platforms have implemented "
            "some keyword monitoring (in Chinese) but Vietnamese-language trafficking conversations "
            "are rarely flagged. Victims average 17.3 years old at time of recruitment via "
            "social media."
        ),
        "source": "Pacific Links Foundation 'Tech and Trafficking in Vietnam' Report (2023)",
    },

    # ── Reintegration and Survivor Support ───────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Myanmar / China",
        "title": "Reintegration Challenges for Myanmar Bride Trafficking Survivors",
        "summary": (
            "Women rescued from forced marriages in China face severe reintegration barriers: "
            "social stigma in Kachin and Shan communities; children left behind in China with "
            "no legal status; health consequences including obstetric fistula, STIs, and mental "
            "health disorders; loss of years of education and economic opportunity. The Kachin "
            "Women's Association Thailand provides a 6-month residential program including "
            "trauma counseling, livelihood training, and legal advice. However, program capacity "
            "(80 beds) is far below demand. Women who return to conflict zones face resumed "
            "displacement and re-trafficking risk."
        ),
        "source": "KWAT Reintegration Program Report 2022; ASTRA (Anti-Trafficking Network) Assessment",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Psychosocial Support Standards for Forced Marriage Survivors",
        "summary": (
            "IASC and WHO guidelines identify forced marriage survivors as requiring specialized "
            "trauma-informed care distinct from other trafficking victims. Key needs: "
            "recognition that family members are often perpetrators (complicating disclosure); "
            "children born of forced marriage create ongoing entanglement; risk of honor-based "
            "violence upon escape; identity documents may be in husband's or in-laws' name; "
            "long-term financial dependency. Recommended minimum services: safe accommodation "
            "at undisclosed location, specialized legal aid, individual counseling, income "
            "generation support, and child custody assistance."
        ),
        "source": (
            "IASC Guidelines on Mental Health and Psychosocial Support (2022); "
            "WHO Clinical Handbook on Addressing Gender-Based Violence (2022)"
        ),
    },

    # ── Additional Corridors and Cases ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "Laos / China",
        "title": "Laos-China Bride Trafficking — Mekong Border Communities",
        "summary": (
            "Lao PDR's National Commission for the Advancement of Women documented over 400 "
            "Lao women trafficked to China as brides between 2019 and 2022. Recruitment focuses "
            "on ethnic Khmu and Hmong communities in Luang Prabang, Phongsaly, and Huaphan "
            "provinces bordering Yunnan. Recruiters are often village insiders; women are "
            "promised work in Chinese restaurants or factories. Upon arrival, passports are "
            "confiscated and women are sold for CNY 20,000–50,000. The Lao PDR-China bilateral "
            "MOU on combating trafficking (2021) improved cooperation on repatriation but "
            "prosecution of Chinese buyers remains negligible."
        ),
        "source": (
            "Lao PDR NCAW Annual Report 2022; "
            "US TIP Report on Laos 2023; UNESCO Mekong Trafficking Assessment 2022"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Pakistan / Middle East",
        "title": "Pakistan — 'Temporary Marriage' (Nikah Mutah) Exploitation for Trafficking",
        "summary": (
            "Pakistani police and NGOs including Ansar Burney Welfare Trust have documented "
            "networks facilitating 'temporary marriages' (nikah mutah, formally a Shia practice "
            "but misused across communities) where young Pakistani girls — sometimes underage — "
            "are 'married' to wealthy Arab tourists for short periods, then left or sold to "
            "other men. This constitutes sexual trafficking under Pakistani law. Lahore and "
            "Karachi have the highest reported incidence. FIA's Human Trafficking Circle has "
            "investigated 67 such cases between 2019 and 2023 with 23 arrests of facilitators."
        ),
        "source": (
            "Ansar Burney Welfare Trust Pakistan Report 2022; "
            "Pakistan FIA Human Trafficking Annual Report 2023"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Eastern Europe / Western Europe",
        "title": "Roma Child Marriage and Cross-Border Trafficking in EU",
        "summary": (
            "The European Roma Rights Centre documents child marriage within Roma communities "
            "in Romania, Bulgaria, Slovakia, and Hungary, with cross-border movement constituting "
            "internal EU trafficking. Girls as young as 12 are married; bride prices of EUR "
            "500–5,000 are exchanged. EU citizenship masks trafficking: Roma girls married in "
            "one EU country and moved to another are often not identified as trafficking victims "
            "because they hold EU passports. The ERRC has filed complaints to the European Court "
            "of Human Rights against Romania and Bulgaria for failure to protect Roma girls "
            "from forced marriage."
        ),
        "source": (
            "European Roma Rights Centre 'Breaking the Silence' Report (2021); "
            "ECHR Case Applications 2022"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "United States",
        "title": "US — Fundamentalist LDS and FLDS Forced Marriage as Trafficking",
        "summary": (
            "The Fundamentalist Church of Jesus Christ of Latter-Day Saints (FLDS) and related "
            "polygamous communities in Utah, Arizona, and Texas have been prosecuted for forced "
            "marriage and trafficking. Warren Jeffs was convicted in 2011 of sexual assault of "
            "children via arranged marriages. FLDS practices included girls as young as 12 "
            "assigned to older men. Traffickers used isolation, religious authority, and "
            "financial dependency as control mechanisms. Arizona's Attorney General's FLDS "
            "Task Force documented 200+ victims in formal investigations between 2003 and 2022. "
            "Escaping FLDS members typically require witness protection programs."
        ),
        "source": (
            "State v. Jeffs (Utah SC 2012); Arizona AG FLDS Task Force Report 2022; "
            "Carolyn Jessop — 'Escape' (2007)"
        ),
    },
    {
        "type": "case_study",
        "jurisdiction": "Israel / Palestine",
        "title": "Israel — Bedouin Community Forced Marriage and Trafficking Dimensions",
        "summary": (
            "Israel's National Council for the Child reports child marriage rates of 24% in Negev "
            "Bedouin communities (vs. 0.3% national average). Girls are married at 13–15 years old; "
            "bride prices (mahr) of ILS 10,000–80,000 are standard. The Israel Police Serious "
            "Crimes Division has investigated 34 cases with trafficking elements between 2018 and "
            "2023 where girls were transferred across communities for bride prices. Movement of "
            "girls across the Green Line introduces international trafficking dimensions in some "
            "cases. Israeli NGO Adalah provides legal aid in forced marriage cases."
        ),
        "source": (
            "Israel National Council for the Child Annual Statistics 2022; "
            "Adalah Legal Center for Arab Minority Rights — Forced Marriage Brief 2022"
        ),
    },
    {
        "type": "statistic",
        "jurisdiction": "Sub-Saharan Africa",
        "title": "Sub-Saharan Africa — Highest Regional Child Marriage Rates",
        "metric": "child_marriage_ssa",
        "value": "40% of girls married before 18 (regional average)",
        "summary": (
            "UNICEF estimates the Sub-Saharan Africa regional child marriage rate at 40%, with "
            "countries including Niger (76%), Central African Republic (52%), Chad (52%), Mali "
            "(52%), and South Sudan (52%) recording the highest rates globally. The region "
            "accounts for the largest absolute number of new child marriages annually (5.1 million "
            "per year) and is the only region where absolute numbers are increasing due to "
            "population growth outpacing reduction in prevalence. Trafficking dimensions are "
            "highest where bride prices involve cross-community or cross-border movement."
        ),
        "source": "UNICEF Child Marriage Regional Database 2023; Girls Not Brides Sub-Saharan Africa Brief",
    },
    {
        "type": "law",
        "jurisdiction": "India",
        "title": "India — Prohibition of Child Marriage Act (PCMA) 2006 and 2021 Amendment Proposal",
        "summary": (
            "India's Prohibition of Child Marriage Act (2006) sets minimum marriage age at 18 for "
            "girls and 21 for boys. Child marriages are voidable (not automatically void) upon "
            "petition by the child before age 20. A 2021 government task force recommended "
            "raising the minimum age for girls to 21 (matching boys) and making child marriages "
            "void ab initio. The Prohibition of Child Marriage (Amendment) Bill was introduced "
            "in Parliament in December 2021 but remained pending as of 2024. Religious personal "
            "laws (Hindu, Muslim, Christian) creating complexity in uniform application."
        ),
        "source": (
            "PCMA 2006 (Act 6 of 2007); Jaya Jaitly Committee Report 2021; "
            "Lok Sabha Debate on Child Marriage Amendment Bill 2021"
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNHCR — Stateless Children of Bride Trafficking Victims",
        "summary": (
            "A distinct consequence of cross-border bride trafficking is the production of stateless "
            "children: children born to trafficked women (particularly North Korean and Myanmar women "
            "in China) who are not registered in either the mother's or father's nationality system. "
            "China's hukou system requires legal marriage for birth registration, which trafficked "
            "women cannot access. UNHCR estimates 30,000–50,000 children of North Korean women in "
            "China are stateless. These children face exclusion from education, healthcare, and "
            "legal identity, creating intergenerational vulnerability to trafficking."
        ),
        "source": "UNHCR Statelessness Report — 'I Am Here, I Belong' (2022); NKDB 2022",
    },
    {
        "type": "case_study",
        "jurisdiction": "United States / Mexico",
        "title": "US-Mexico Border — Indigenous Mexican Women in Forced Marriages",
        "summary": (
            "Researchers at the University of California San Diego documented cases among "
            "indigenous Mixtec and Triqui communities in Oaxaca and California where traditional "
            "bride price practices (guetza) are exploited by traffickers. Girls aged 13–16 are "
            "sold across the US-Mexico border for USD 3,000–16,000. Women may be resold if the "
            "first buyer becomes unsatisfied. California-based NGO Mixteca Organization has "
            "provided legal aid in 47 forced marriage cases since 2018, navigating both Mexican "
            "customary law and California family law. The cross-border dimension activates federal "
            "TVPA jurisdiction."
        ),
        "source": (
            "UC San Diego Center for US-Mexican Studies Research (2022); "
            "Mixteca Organization Annual Report 2022"
        ),
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "IOM — Migration and Forced Marriage: Identification Guidelines",
        "summary": (
            "IOM's Counter-Trafficking Data Collaborative guidelines (2023) for migration "
            "officers include forced marriage as a distinct trafficking category requiring "
            "specific identification protocols. Key identifiers: women who cannot explain "
            "how travel was funded; women whose destination is a private household (not "
            "employer or accommodation facility); women traveling under the immigration "
            "sponsorship of a future spouse; women who cannot speak freely in interviews. "
            "IOM recommends integration of forced marriage identification into all migration "
            "management systems and training for border officials globally."
        ),
        "source": "IOM Counter-Trafficking Data Collaborative Methodology Handbook (2023 revision)",
    },
]
