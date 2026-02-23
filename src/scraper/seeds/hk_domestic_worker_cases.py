"""Hong Kong court decisions on domestic worker exploitation, abuse, and labor violations.

Covers landmark HK court cases, Hong Kong legislation for domestic workers,
systemic issues documented in HK cases, enforcement and advocacy, and
Hong Kong-specific exploitation patterns. Sources include Hong Kong court
records, Labour Department data, US State Department TIP Reports, NGO
reports from Justice Centre Hong Kong, Mission for Migrant Workers, FADWU,
and international bodies (ILO, IOM).
"""

HK_DOMESTIC_WORKER_CASE_FACTS: list[dict] = [
    # =========================================================================
    # 1. LANDMARK HONG KONG COURT CASES
    # =========================================================================

    # ── Erwiana Sulistyaningsih / HKSAR v Law Wan-tung ─────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "HKSAR v Law Wan-tung [2015] DCCC 777/2014 — Erwiana Sulistyaningsih Case",
        "summary": (
            "Employer Law Wan-tung convicted on 18 of 20 charges including "
            "grievous bodily harm, criminal intimidation, and failure to pay "
            "wages for abuse of Indonesian domestic worker Erwiana "
            "Sulistyaningsih. Erwiana was beaten with mop handles, vacuum "
            "rods, and coat hangers, burned with a clothes iron, deprived "
            "of food and sleep, confined to the employer's apartment, and "
            "unpaid for 8 months. Made to work 21-hour days and clean doors "
            "at 3 a.m. so neighbors would not see. Sentenced to 6 years "
            "imprisonment (February 2015). Judge described Law as 'a bully "
            "who showed contempt for those beneath her.' Case gained "
            "international attention; Erwiana named TIME 100 Most "
            "Influential People 2014."
        ),
        "source": "Hong Kong District Court DCCC 777/2014; CNN; TIME; SCMP",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Erwiana Sulistyaningsih — Civil Damages Award (2017)",
        "summary": (
            "After criminal conviction of Law Wan-tung, Erwiana pursued a "
            "civil claim. The Labour Tribunal awarded HKD 809,430 "
            "(approx. USD 103,480) in compensation covering unpaid wages, "
            "pain and suffering, and loss of future earnings. Law Wan-tung "
            "was released from prison in 2018 after serving less than "
            "two-thirds of her sentence. She was declared bankrupt in 2021, "
            "leaving the compensation judgment potentially unrecoverable."
        ),
        "source": "SCMP; Hong Kong Free Press (HKFP)",
    },

    # ── ZN v Secretary for Justice ─────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "ZN v Secretary for Justice [2019] HKCFA 53 — CFA Trafficking Ruling",
        "summary": (
            "Pakistani national ZN alleged he was falsely promised a "
            "lucrative job, had his passport confiscated on arrival, was "
            "forced into unpaid domestic servitude for years, slept in "
            "employer's office, and worked 7 days per week. Court of Final "
            "Appeal addressed whether BOR4 (Bill of Rights Article 4, "
            "prohibition of slavery/servitude/forced labour) creates a "
            "positive duty to enact bespoke anti-trafficking legislation. "
            "CFA held: BOR4 does not require specific trafficking "
            "criminalization but imposes positive duty on government to "
            "maintain practical and effective protections including a duty "
            "to investigate. Highlighted significant gaps in HK's "
            "anti-trafficking framework for forced labour outside sexual "
            "exploitation contexts."
        ),
        "source": "HKCFA; Oxford Public International Law; Patricia Ho & Associates",
    },

    # ── Kartika Puspitasari ────────────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Kartika Puspitasari — Record HKD 868,607 Damages Award (2023)",
        "summary": (
            "Indonesian domestic worker Kartika Puspitasari awarded record "
            "HKD 868,607 (approx. USD 110,647) by District Court after a "
            "decade-long battle. Employers Tai Chi-wai and Catherine Au "
            "Yuk-shan had been convicted of assault and wounding with "
            "intent: Kartika was scalded with a hot iron, beaten with a "
            "bicycle chain, and subjected to years of physical abuse. "
            "Employers sentenced to 3 years 3 months and 5 years "
            "respectively in criminal proceedings. Civil damages cover "
            "pain, suffering, loss of enjoyment of life, aggravated "
            "damages, loss of income, and future medical expenses. "
            "Largest compensation award for domestic worker abuse in HK "
            "history. Kartika also received HKD 350,000 insurance payout."
        ),
        "source": "SCMP; Hong Kong Free Press; The Standard (HK)",
    },

    # ── CB v Commissioner of Police ────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "CB v Commissioner of Police [2024] HKCA 172 — Forced Labour Screening",
        "summary": (
            "Philippine foreign domestic helper CB alleged repeated sexual "
            "assault and exploitation by employer. Employer convicted of "
            "two counts of indecent assault. However, police screening "
            "determined CB was not a victim of trafficking or forced "
            "labour. CB successfully applied for judicial review; court "
            "found police officer misunderstood definition of human "
            "trafficking, irrationally failed to investigate employer's "
            "pattern of exploitation, and relied on irrelevant "
            "considerations. Decision quashed and remitted to Commissioner "
            "for reconsideration. Established that HK government's adopted "
            "Palermo Protocol definitions create enforceable public law "
            "norms for screening decisions."
        ),
        "source": "HKCA; Bernacchi Chambers; Blackstone Chambers; HK DOJ",
    },

    # ── Live-in Requirement Judicial Review ────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Lubiano v Director of Immigration [2018/2020] — Live-in Requirement Challenge",
        "summary": (
            "Filipino domestic helper Nancy Almorin Lubiano challenged the "
            "constitutionality of the mandatory live-in requirement for "
            "foreign domestic helpers. Court of First Instance dismissed "
            "the judicial review application (2018). Court of Appeal "
            "upheld the dismissal (September 2020), ruling the live-in "
            "requirement is a lawful immigration condition and does not "
            "violate the Bill of Rights. The requirement forces 340,000+ "
            "FDHs to reside with employers, creating dependency and "
            "vulnerability to exploitation. Advocacy groups argue the "
            "live-in rule enables 24-hour on-call work, sexual "
            "harassment, and food deprivation."
        ),
        "source": "Court of Appeal (HK); Mondaq; Lexology; SCMP",
    },

    # ── Employer Rape Conviction ───────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "HKSAR v Employer (2024) — Rare Rape Conviction for Domestic Worker Abuse",
        "summary": (
            "Hong Kong employer convicted of raping Filipino domestic "
            "worker in a rare successful prosecution (2024). The domestic "
            "worker testified about her ordeal despite significant "
            "barriers including fear of deportation under the two-week "
            "rule and reliance on the employer for accommodation. "
            "Advocates described the verdict as 'a win for all of us.' "
            "Between 2019 and June 2024, police received 310 reports "
            "involving employers of domestic workers, with 87 related "
            "to sexual abuse, but only 36 employers were prosecuted "
            "overall, reflecting extremely low prosecution rates for "
            "sexual offences against FDHs."
        ),
        "source": "Al Jazeera; Hong Kong Free Press",
    },

    # ── Indecent Assault Acquittal on Retrial ──────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "DCCC Indecent Assault Retrial Acquittal — Procedural Failures",
        "summary": (
            "Employer initially sentenced to 30 months for two counts of "
            "indecent assault against domestic worker (2021). On appeal, "
            "acquitted of all charges on procedural and technical grounds "
            "including issues related to admission of evidence. Case "
            "illustrates how procedural barriers in HK criminal courts "
            "can undermine domestic worker protections even when initial "
            "convictions are secured. Academic analysis found 'judicial "
            "attitudes towards foreign domestic helpers in criminal courts' "
            "often reflect structural biases favoring employers."
        ),
        "source": "Taylor & Francis Online; Al Jazeera; SCMP",
    },

    # ── AM v Director of Immigration ───────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "AM v Director of Immigration [2022] HKCFI 1046 — Trafficking Screening",
        "summary": (
            "Judicial review challenging adequacy of HK trafficking "
            "screening procedures. Court found that while the government "
            "has mechanisms to screen potential trafficking victims, "
            "implementation was inconsistent. Case highlighted ongoing "
            "deficiencies in identifying forced labour victims among "
            "foreign domestic helpers despite the ZN v Secretary for "
            "Justice ruling. Reinforced that administrative screening "
            "decisions are subject to judicial review on Wednesbury "
            "unreasonableness grounds."
        ),
        "source": "HKCFI; Bernacchi Chambers; HK DOJ",
    },

    # ── Wage Theft Cases ───────────────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Labour Tribunal — Systematic Underpayment Below MAW Claims",
        "summary": (
            "Pattern of Labour Tribunal rulings awarding back-pay to "
            "foreign domestic helpers paid below the Minimum Allowable "
            "Wage. Common employer tactics: declaring lower salary in "
            "bank transfers while claiming remainder paid in cash (no "
            "proof); deducting 'training fees,' 'food costs,' or 'breakage "
            "charges' from wages; withholding final month salary claiming "
            "worker 'did not complete contract.' Tribunal consistently "
            "rules that all deductions must be authorized under the SEC "
            "and that employer bears burden of proving cash payments. "
            "Typical awards: HKD 10,000-80,000 in back-pay."
        ),
        "source": "Hong Kong Labour Tribunal; Labour Department Annual Reports",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Labour Tribunal — Terminal Benefits Disputes for Dismissed FDHs",
        "summary": (
            "Recurring Labour Tribunal cases where employers terminate "
            "contracts prematurely without paying statutory entitlements: "
            "wages in lieu of notice (1 month), outstanding annual leave "
            "pay, long service payment (for 5+ years), and return "
            "travel costs. Tribunal awards these as statutory rights under "
            "the Employment Ordinance, non-waivable even if worker 'agrees' "
            "to forgo them. Some employers file counter-claims alleging "
            "theft or damage to discourage workers from pursuing claims."
        ),
        "source": "Hong Kong Labour Tribunal; Justice Centre Hong Kong",
    },

    # ── Employment Agency Convictions ──────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Magistrates' Court — Employment Agency Overcharging Convictions",
        "summary": (
            "Between 2014 and 2021, Labour Department secured limited "
            "convictions against employment agencies for overcharging "
            "domestic workers: 10 convictions (2014-2015), 8 agencies "
            "convicted (2016), 2 convicted for overcharging plus 4 for "
            "unlicensed operations (2017), 5 prosecuted (2021). Fines "
            "ranged from HKD 1,500 to HKD 45,000 against a maximum "
            "penalty of HKD 50,000. NGOs criticize penalties as "
            "inadequate deterrent. Workers reported paying average "
            "HKD 11,321 to agencies despite legal maximum of HKD 487 "
            "(10% of first month's MAW) — more than 25 times the legal "
            "limit."
        ),
        "source": "US State Department TIP Report; Labour Department; HKFP",
    },

    # ── Employer Assault Convictions (Pattern) ─────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "DCCC Pattern — Employer Assault Convictions Against Domestic Workers",
        "summary": (
            "From 2019 to June 2024, Hong Kong Police received 310 reports "
            "of violent or sexual offences by employers against domestic "
            "workers. 194 employers were arrested. Only 36 were prosecuted. "
            "Of 77 rape/indecent assault reports (2019-2023), 69 employers "
            "arrested but only 31 prosecuted with 9 convicted (sentences "
            "up to 7 years). Conviction rate for employer violence against "
            "FDHs remains far below general assault conviction rates. "
            "Barriers include: workers deported before trial, dependence "
            "on employer for accommodation during proceedings, language "
            "barriers, and lack of legal aid funding."
        ),
        "source": "Hong Kong Police Force statistics; Al Jazeera; SCMP",
    },

    # =========================================================================
    # 2. HONG KONG LEGISLATION FOR DOMESTIC WORKERS
    # =========================================================================

    # ── Employment Ordinance (Cap. 57) ─────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Employment Ordinance (Cap. 57) — Primary Labour Law for FDHs",
        "summary": (
            "Primary labour legislation governing employment in Hong Kong "
            "since 1968. Applies to foreign domestic helpers (FDHs) with "
            "key protections: minimum allowable wage, mandatory rest days "
            "(at least 1 per 7 days), 12 statutory holidays, paid annual "
            "leave (7-14 days depending on service), sickness allowance, "
            "maternity protection, severance/long service payment, and "
            "protection against anti-union discrimination. Part XII "
            "governs employment agencies: maximum commission of 10% of "
            "first month's salary per contract year. Offence to underpay: "
            "maximum HKD 350,000 fine and 3 years imprisonment."
        ),
        "source": "Hong Kong e-Legislation; Labour Department",
    },
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Employment Ordinance (Cap. 57) — Employment Protection for FDHs",
        "summary": (
            "Cap. 57 s.9 prohibits dismissal of employee for exercising "
            "trade union rights, giving evidence in proceedings, or "
            "becoming pregnant. s.10 prohibits variation of employment "
            "terms without worker's consent. s.63B creates criminal "
            "offence for willful failure to pay wages on time (max "
            "HKD 350,000 fine + 3 years imprisonment). s.64 provides "
            "wage protection on insolvency through Protection of Wages "
            "on Insolvency Fund. These apply equally to FDHs."
        ),
        "source": "Hong Kong e-Legislation Cap. 57",
    },

    # ── Standard Employment Contract ───────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Standard Employment Contract (SEC) ID 407 — Mandatory Terms for FDHs",
        "summary": (
            "Immigration Department Form ID 407 is the only employment "
            "contract accepted for FDH visa applications. Two-year fixed "
            "term. Mandatory provisions: employer must provide free "
            "accommodation (suitable for reasonable privacy), free food "
            "or food allowance (HKD 1,236/month as of 2025), free "
            "medical treatment, return passage to place of origin on "
            "contract completion or termination, wages not less than "
            "the Minimum Allowable Wage. FDH may only perform domestic "
            "duties for the specified employer at the specified address. "
            "Any side agreement that derogates from SEC terms is void "
            "and unenforceable."
        ),
        "source": "Hong Kong Immigration Department; IMMD Form ID 407",
    },

    # ── Minimum Allowable Wage ─────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Minimum Allowable Wage (MAW) for FDHs — Current and Historical Rates",
        "summary": (
            "The MAW is reviewed annually by the HKSAR government. "
            "Historical rates: HKD 3,740 (2013), HKD 4,210 (2015), "
            "HKD 4,410 (2017), HKD 4,520 (2018), HKD 4,630 (2019), "
            "frozen at HKD 4,630 (2020-2022, COVID), HKD 4,730 (2023), "
            "HKD 4,870 (2024), HKD 4,990 (Sep 2024), HKD 5,100 (Sep "
            "2025). Food allowance: HKD 1,236/month (2025). MAW applies "
            "to all new contracts signed on or after the effective date. "
            "Existing contracts not automatically adjusted until renewal."
        ),
        "source": "Hong Kong Government Press Releases; Labour Department",
    },

    # ── Immigration Ordinance (Cap. 115) ───────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Immigration Ordinance (Cap. 115) — Two-Week Rule for FDHs",
        "summary": (
            "Under Cap. 115 and associated immigration conditions, FDHs "
            "whose contracts are terminated (by either party) must leave "
            "Hong Kong within 14 days unless they secure a new contract "
            "and visa within that period or obtain special permission to "
            "remain. The two-week rule was introduced to prevent FDHs "
            "from overstaying or engaging in unauthorized work. Widely "
            "criticized as enabling exploitation: workers tolerate abuse "
            "rather than lose immigration status, income, and the ability "
            "to support families. NGOs report the rule deters 60-70% of "
            "workers from filing complaints or leaving abusive employers."
        ),
        "source": "Immigration Ordinance Cap. 115; IMMD; Justice Centre Hong Kong",
    },

    # ── Employees' Compensation Ordinance ──────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Employees' Compensation Ordinance (Cap. 282) — FDH Workplace Injury",
        "summary": (
            "Cap. 282 requires employers to maintain employees' "
            "compensation insurance covering FDHs for work injuries and "
            "occupational diseases. Minimum insurance: HKD 100 million per "
            "event for employees. Covers: medical expenses, temporary "
            "incapacity payments, permanent incapacity compensation, and "
            "death benefits. FDHs injured during work (including in the "
            "employer's home) are entitled to compensation regardless of "
            "fault. Employer failure to insure is a criminal offence: "
            "HKD 100,000 fine + 2 years imprisonment."
        ),
        "source": "Hong Kong e-Legislation Cap. 282; Labour Department",
    },

    # ── Employment Agency Regulations ──────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Employment Agency Regulations (Cap. 57A) — Fee Caps and Licensing",
        "summary": (
            "Under subsidiary legislation to Cap. 57, employment agencies "
            "must be licensed by the Labour Department. Maximum commission: "
            "10% of first month's salary per year of the employment "
            "contract. For FDHs on a 2-year SEC at MAW HKD 5,100, "
            "maximum legal fee is approximately HKD 1,020. Agencies must "
            "not: withhold worker passports, make false representations "
            "about jobs, or coerce workers. Offences: HKD 50,000 fine. "
            "As of 2024, approximately 4,000 licensed employment agencies "
            "operate in HK, many handling FDH placement."
        ),
        "source": "Employment Ordinance Cap. 57 Part XII; Labour Department",
    },

    # ── Crimes Ordinance S.129 ─────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Crimes Ordinance (Cap. 200) S.129 — Trafficking for Prostitution",
        "summary": (
            "Section 129 of the Crimes Ordinance is HK's only "
            "trafficking-specific provision. Criminalizes trafficking "
            "into or from Hong Kong for the purpose of prostitution. "
            "Critical limitation: does not cover trafficking for forced "
            "labour, domestic servitude, or other non-sexual exploitation. "
            "Does not apply to internal trafficking within HK. This gap "
            "means there is no specific criminal offence for trafficking "
            "domestic workers into forced labour — prosecutors must rely "
            "on general assault, false imprisonment, or employment "
            "ordinance charges."
        ),
        "source": "Crimes Ordinance Cap. 200; Oxford Human Rights Hub; IIAS",
    },

    # ── Bill of Rights Ordinance ───────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Hong Kong Bill of Rights Ordinance (Cap. 383) Art. 4 — BOR4",
        "summary": (
            "Article 4 of the Hong Kong Bill of Rights (implementing "
            "ICCPR Art. 8) prohibits slavery, the slave trade, servitude, "
            "and forced or compulsory labour. However, there are no "
            "specific criminal offences under HK law for slavery, "
            "servitude, or forced labour — BOR4 is a constitutional "
            "guarantee without direct penal enforcement. The ZN v "
            "Secretary for Justice [2019] HKCFA 53 case confirmed BOR4 "
            "creates a positive duty on government to maintain protective "
            "measures but does not mandate bespoke anti-trafficking "
            "legislation. Academics and NGOs call this a critical gap."
        ),
        "source": "Cap. 383; HKCFA; CMAB; PMC/Frontiers in Sociology",
    },

    # ── Anti-Discrimination Ordinances ─────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Sex Discrimination Ordinance (Cap. 480) — Workplace Harassment of FDHs",
        "summary": (
            "Cap. 480 prohibits sexual harassment in the workplace, "
            "covering FDHs in employer's homes. Equal Opportunities "
            "Commission (EOC) can investigate complaints. Race "
            "Discrimination Ordinance (Cap. 602) protects FDHs from "
            "race-based discrimination in employment. Disability "
            "Discrimination Ordinance (Cap. 487) protects FDHs who "
            "become disabled during employment. Despite these protections, "
            "FDH complaints to EOC remain low (estimated 20-30 per year) "
            "due to: language barriers, fear of retaliation, lack of "
            "awareness of rights, and two-week rule pressure."
        ),
        "source": "Equal Opportunities Commission (HK); Cap. 480, 602, 487",
    },

    # ── Action Plan to Tackle TIP ──────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "HK Government Action Plan to Tackle Trafficking in Persons (2018)",
        "summary": (
            "Following judicial pressure (CB and ZN cases), the HKSAR "
            "Government launched an Action Plan to Tackle TIP in March "
            "2018. Four pillars: Prevention, Protection, Prosecution, "
            "Partnership. Established screening mechanism for potential "
            "trafficking victims among arrested persons. Trained 17,000+ "
            "government officers by 2023. However, US TIP Report "
            "consistently rates HK as Tier 2 Watch List, noting: no "
            "specific trafficking legislation, insufficient victim "
            "identification, and reliance on patchwork of existing laws."
        ),
        "source": "Security Bureau (HKSAR); US State Department TIP Report 2024",
    },

    # =========================================================================
    # 3. SYSTEMIC ISSUES DOCUMENTED IN HK CASES
    # =========================================================================

    # ── Two-Week Rule Exploitation ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Two-Week Rule — Exploitation Mechanism and Worker Impact",
        "summary": (
            "The two-week rule (Immigration condition requiring FDHs to "
            "leave within 14 days of contract termination) creates "
            "systemic vulnerability. Documented impacts: (1) workers "
            "endure abuse rather than risk termination, (2) workers "
            "who file complaints at Labour Tribunal must wait 8-15 "
            "months for hearings but cannot legally work during that "
            "period, (3) employers use threat of termination as coercive "
            "tool, (4) workers who flee abusive employers become "
            "undocumented and ineligible for services, (5) agencies "
            "exploit the rule by requiring workers to accept new "
            "placements quickly regardless of conditions. FADWU and "
            "Mission for Migrant Workers campaign for its abolition."
        ),
        "source": "Justice Centre Hong Kong; FADWU; Mission for Migrant Workers",
    },

    # ── Live-in Requirement ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Mandatory Live-in Requirement — Exploitation Enabler",
        "summary": (
            "FDHs are required by immigration condition to reside at "
            "employer's address. Creates unique vulnerabilities: no "
            "separation between work and rest, 'on-call' 24 hours "
            "normalized, sleeping arrangements often inadequate (camp "
            "beds in kitchens, shared rooms with children, windowless "
            "storage areas), employer controls living conditions, meals, "
            "and movement. Workers report being unable to leave the "
            "house on rest days. Many FDHs gather in public spaces "
            "(Central, Victoria Park, Causeway Bay) on Sundays as they "
            "have no private space. Constitutional challenge failed "
            "(Lubiano v Director of Immigration, 2018/2020)."
        ),
        "source": "CNN; SCMP; Mondaq; Migrant Forum in Asia",
    },

    # ── Agency Overcharging ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Employment Agency Overcharging — Systemic Fee Exploitation",
        "summary": (
            "Despite the 10% statutory cap, systematic overcharging is "
            "pervasive. Documented pattern: agencies in Philippines and "
            "Indonesia charge USD 500-2,000 upfront, then HK-side agencies "
            "deduct a further 3-7 months of wages from workers upon "
            "arrival. Workers reported paying average HKD 11,321 — over "
            "25 times the legal maximum of HKD 487. Methods: 'training "
            "fees,' 'loan repayments,' 'accommodation during placement,' "
            "mandatory purchase of supplies. Some agencies operate colluding "
            "pairs (origin + destination) to split illegal profits. Despite "
            "approximately 4,000 licensed agencies, prosecution rate is "
            "negligible: 2-11 convictions per year."
        ),
        "source": "Justice Centre Hong Kong; HKFP; US TIP Report; Labour Department",
    },

    # ── Underpayment Below MAW ─────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Underpayment Below Minimum Allowable Wage — Documented Patterns",
        "summary": (
            "Justice Centre Hong Kong research found approximately 14% "
            "of surveyed FDHs were paid below the MAW. Common methods: "
            "(1) declaring MAW on contract but paying less in practice, "
            "(2) requiring workers to return portion of salary as 'loan "
            "repayment' to agency, (3) deducting for food despite SEC "
            "requiring free provision, (4) withholding 1-3 months' salary "
            "as 'deposit' returned only on contract completion, (5) "
            "paying reduced wage during 'probation period' not recognized "
            "under HK law. Maximum penalty for willful underpayment: "
            "HKD 350,000 fine + 3 years imprisonment, but prosecutions "
            "are rare."
        ),
        "source": "Justice Centre Hong Kong; Mission for Migrant Workers; ILO",
    },

    # ── Rest Day Denial ────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Rest Day Denial and Forced Work on Holidays",
        "summary": (
            "Employment Ordinance mandates at least 1 rest day per 7 "
            "days for all employees including FDHs. Documented violations: "
            "employers require workers to work on rest days without "
            "compensation, limit rest day hours (e.g., must return by "
            "6 p.m.), require workers to complete tasks before leaving, "
            "punish workers for taking rest days by assigning extra "
            "work. Some employers pressure FDHs to 'voluntarily' forgo "
            "rest days for additional pay (HKD 100-200) which workers "
            "accept due to debt obligations. Statutory holidays similarly "
            "violated. Labour Tribunal awards damages for denied rest "
            "days but individual claims are rare."
        ),
        "source": "FADWU; Mission for Migrant Workers; Labour Department",
    },

    # ── Food Deprivation ───────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Food Deprivation as Control Mechanism in HK Domestic Work",
        "summary": (
            "SEC requires employer to provide free food or food allowance "
            "(HKD 1,236/month). Documented food deprivation patterns: "
            "workers given only employer's leftovers, separate inferior "
            "food, restricted eating times, locked refrigerators/pantries, "
            "portion control, prohibition from eating 'employer's food.' "
            "In the Erwiana case, the worker was deprived of food as "
            "punishment. Justice Centre Hong Kong found 8% of surveyed "
            "workers experienced food deprivation. Workers who receive "
            "food allowance instead of meals may still be unable to "
            "cook as they lack access to kitchen during employer's "
            "preferred hours."
        ),
        "source": "Justice Centre Hong Kong; ILO; Erwiana case records",
    },

    # ── Passport/Document Retention ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Passport and Document Retention by Employers and Agencies",
        "summary": (
            "While no specific HK law criminalizes passport confiscation "
            "(unlike Singapore's EFMA), retaining a worker's passport "
            "constitutes a forced labour indicator under BOR4 and ILO "
            "standards. Documented pattern: agencies confiscate passports "
            "as collateral for placement fees on arrival; employers hold "
            "passports 'for safekeeping.' Workers without passports "
            "cannot: access banking, present ID to police, or flee. "
            "Mission for Migrant Workers estimates 10-15% of FDHs have "
            "passports retained. Labour Tribunal does not directly "
            "address passport confiscation — workers must file police "
            "reports for theft, which few do."
        ),
        "source": "Mission for Migrant Workers; Justice Centre Hong Kong; ILO",
    },

    # ── Employer Bankruptcy ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Employer Bankruptcy Leaving FDHs Unpaid — Systemic Issue",
        "summary": (
            "When employers declare bankruptcy, FDHs face difficulty "
            "recovering unpaid wages and compensation. The Protection "
            "of Wages on Insolvency Fund (PWIF) under Cap. 57 covers "
            "employees of insolvent employers for: arrears of wages "
            "(up to 4 months, max HKD 36,000), wages in lieu of notice, "
            "severance payment, and other statutory entitlements. However, "
            "FDHs often do not know they can claim from PWIF. The "
            "Erwiana case exemplified this: Law Wan-tung declared "
            "bankrupt in 2021, potentially rendering the HKD 809,430 "
            "civil damages award unrecoverable."
        ),
        "source": "Labour Department PWIF; SCMP; HKFP",
    },

    # ── False Accusations Against Workers ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "False Accusations Against FDHs by Employers — Retaliatory Pattern",
        "summary": (
            "Documented employer tactic: filing false theft or property "
            "damage accusations against FDHs who attempt to leave, file "
            "complaints, or demand unpaid wages. Effects: (1) police "
            "investigation during two-week window prevents worker from "
            "finding new employment, (2) criminal record if convicted "
            "makes future HK employment impossible, (3) deters other "
            "workers from reporting abuse, (4) shifts narrative from "
            "employer abuse to worker misconduct. Advocacy groups report "
            "hundreds of cases annually where workers filing Labour "
            "Tribunal claims face counter-accusations from employers."
        ),
        "source": "Justice Centre Hong Kong; FADWU; MFMW",
    },

    # ── Privacy Violations ─────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "CCTV Surveillance and Privacy Violations Against FDHs",
        "summary": (
            "Growing reports of employers installing CCTV cameras in "
            "domestic worker sleeping areas, bathrooms, and changing "
            "rooms. Live-in requirement means FDHs cannot escape "
            "surveillance. Personal Data (Privacy) Ordinance (Cap. 486) "
            "does not explicitly address employer-installed cameras in "
            "private residences. Workers report feeling monitored 24/7. "
            "Some employers use cameras to micromanage work or fabricate "
            "accusations. Office of the Privacy Commissioner for Personal "
            "Data has received complaints but enforcement in private "
            "homes is extremely limited. FDH sleeping areas in kitchens "
            "or living rooms exacerbate the issue."
        ),
        "source": "PCPD (HK); FairPlanet; Al Jazeera",
    },

    # ── Double Contracts ───────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Double Contracts — One for Immigration, One Actual",
        "summary": (
            "Documented practice where agencies prepare two contracts: "
            "(1) the official SEC (ID 407) filed with Immigration "
            "Department showing MAW and standard conditions, and (2) a "
            "side agreement with lower wages, additional duties, or "
            "waived rest days. Side agreements are void under HK law "
            "as they derogate from the SEC, but workers often do not "
            "know this. Agencies in origin countries may present the "
            "side agreement as the 'real' contract. Workers who complain "
            "about conditions are told 'you signed the agreement.' "
            "Labour Tribunal consistently voids side agreements but "
            "workers must know to challenge them."
        ),
        "source": "IDWF; Justice Centre Hong Kong; Labour Department",
    },

    # ── Medical Treatment Denial ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Denial of Medical Treatment to FDHs — SEC Violations",
        "summary": (
            "SEC requires employers to provide free medical treatment to "
            "FDHs. Documented violations: employers refuse to take "
            "workers to doctors, deny time off for medical appointments, "
            "require workers to pay for their own treatment, dismiss "
            "workers who become ill or pregnant, fail to maintain "
            "employees' compensation insurance. Pregnant FDHs face "
            "particular vulnerability: employers may terminate contracts "
            "upon learning of pregnancy (unlawful under Employment "
            "Ordinance s.15). PathFinders reports assisting 1,000+ "
            "pregnant FDHs annually who face termination or denial of "
            "maternity benefits."
        ),
        "source": "PathFinders; SEC ID 407; Employment Ordinance Cap. 57",
    },

    # ── Rest Day Work Compensation ─────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Rest Day Work Compensation Disputes",
        "summary": (
            "Employment Ordinance requires that if an employee works on "
            "a statutory rest day, they must receive a replacement rest "
            "day within 30 days. However, no statutory premium pay rate "
            "for rest day work exists under HK law (unlike many other "
            "jurisdictions). FDHs who work on rest days at employer's "
            "request often receive no compensation at all. Some employers "
            "offer HKD 100-200 per rest day worked, far below the daily "
            "MAW equivalent (approximately HKD 170). Labour Tribunal "
            "cases address denied replacement rest days but cannot award "
            "premium pay absent statutory basis."
        ),
        "source": "Labour Department; Employment Ordinance Cap. 57",
    },

    # =========================================================================
    # 4. ENFORCEMENT AND ADVOCACY
    # =========================================================================

    # ── Labour Department Enforcement ──────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Labour Department Enforcement — FDH-Related Prosecutions",
        "summary": (
            "Labour Department conducts inspections and prosecutions "
            "related to FDH employment. Annual prosecution statistics "
            "(approximate): 30-50 employer prosecutions for Employment "
            "Ordinance violations (underpayment, rest day denial), 5-15 "
            "agency prosecutions for overcharging or unlicensed operation. "
            "Labour Department Employment Agencies Administration (EAA) "
            "revokes approximately 10-20 agency licenses per year. "
            "However, relative to 340,000+ FDHs and widespread reported "
            "violations, enforcement is considered grossly inadequate. "
            "US TIP Report 2024 notes: 'the government did not "
            "adequately fund or resource anti-trafficking efforts.'"
        ),
        "source": "Labour Department Annual Reports; US TIP Report 2024",
    },
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Labour Department — FDH Complaint and Claim Statistics",
        "summary": (
            "Labour Department receives 2,000-3,000 FDH-related "
            "complaints annually. Labour Tribunal handles 1,500-2,000 "
            "FDH wage and benefits claims per year. Common claims: "
            "unpaid wages (45%), wages in lieu of notice (25%), annual "
            "leave pay (15%), other statutory benefits (15%). Median "
            "award: approximately HKD 15,000-25,000. Time from filing "
            "to hearing: 8-15 months. Workers cannot legally work during "
            "proceedings and depend on NGO shelters for accommodation."
        ),
        "source": "Labour Department; Judiciary Annual Reports; MFMW",
    },

    # ── Immigration Department ─────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Immigration Department — FDH Visa and Enforcement Data",
        "summary": (
            "As of 2024, approximately 340,000 foreign domestic helpers "
            "hold valid visas in Hong Kong, comprising roughly 10% of "
            "the total workforce. Approximately 54% are from the "
            "Philippines and 44% from Indonesia, with smaller numbers "
            "from Thailand, Sri Lanka, India, Nepal, and Bangladesh. "
            "Immigration Department processes approximately 150,000 "
            "FDH visa applications/renewals annually. Refusal rate for "
            "employer applications is low (under 5%). Department screens "
            "for potential trafficking victims among immigration "
            "detainees since 2018 Action Plan."
        ),
        "source": "Immigration Department (HK); Census and Statistics Department",
    },

    # ── Mission for Migrant Workers ────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Mission for Migrant Workers (MFMW) — Case Data and Services",
        "summary": (
            "MFMW established 1981, oldest migrant worker support "
            "organization in HK. Provides shelter (40-bed capacity), "
            "legal aid, counseling, and crisis intervention. Handles "
            "3,000-4,000 cases annually. Services: walk-in center in "
            "Central district, Sunday drop-in service, employment "
            "ordinance advice, Labour Tribunal accompaniment, police "
            "report assistance, shelter referral. Key advocacy: abolition "
            "of two-week rule, mandatory live-in requirement reform, "
            "increased agency penalties. Contact: +852 2522 8264."
        ),
        "source": "Mission for Migrant Workers (MFMW)",
    },

    # ── HOME Hong Kong ─────────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Helpers for Domestic Helpers (HOME HK) — Migrant Worker Support",
        "summary": (
            "HOME Hong Kong provides direct assistance to exploited "
            "FDHs: emergency shelter, legal advice, Labour Tribunal "
            "case support, and repatriation assistance. Works closely "
            "with Indonesian and Filipino consulates. Documented "
            "common complaint categories: underpayment (35%), physical "
            "abuse (15%), overwork/rest day denial (20%), agency "
            "overcharging (15%), contract violations (15%). Also "
            "provides pre-departure education in origin countries."
        ),
        "source": "HOME Hong Kong; Migrant Forum in Asia",
    },

    # ── FADWU ──────────────────────────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "FADWU — Federation of Asian Domestic Workers Unions",
        "summary": (
            "FADWU is an alliance of domestic worker unions in Hong Kong "
            "including the Indonesian Migrant Workers Union (IMWU), "
            "Filipino Migrant Workers Union (FMWU), and others. "
            "Campaigns: abolition of two-week rule, scrapping live-in "
            "requirement, increasing MAW, strengthening agency "
            "regulation, anti-discrimination measures. Organizes annual "
            "International Migrants Day rallies (December 18). "
            "Successfully advocated for incremental MAW increases and "
            "stricter agency code of practice. Member of IDWF. "
            "Contact via IDWF Hong Kong office."
        ),
        "source": "FADWU; IDWF; ILO",
    },

    # ── Justice Centre Hong Kong ───────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Justice Centre Hong Kong — Trafficking Research and Legal Aid",
        "summary": (
            "Independent research and legal support organization "
            "focused on forced labour, trafficking, and asylum in HK. "
            "Published landmark research: 'Coming Clean' (2016) found "
            "1 in 6 FDHs experienced forced labour indicators. Provides "
            "legal representation for trafficking victims, policy "
            "advocacy, and public education. Key research findings used "
            "in CB v Commissioner of Police and other judicial review "
            "cases. Helpline: +852 6312 4948."
        ),
        "source": "Justice Centre Hong Kong; 'Coming Clean' report (2016)",
    },

    # ── Legal Aid for FDHs ─────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Legal Aid Availability for Foreign Domestic Helpers in HK",
        "summary": (
            "FDHs are eligible for legal aid under the Ordinary Legal "
            "Aid Scheme if they pass means and merits tests. However, "
            "barriers include: (1) complex application process in "
            "English or Chinese, (2) means test excludes workers with "
            "savings above HKD 430,400, (3) merits test may reject "
            "claims perceived as low-value, (4) waiting times of 2-4 "
            "months for approval, (5) workers cannot legally work while "
            "waiting. Duty Lawyer Service provides free legal advice at "
            "Labour Tribunal but not full representation. NGOs fill the "
            "gap: MFMW, Justice Centre, and HKCTU provide paralegal "
            "support and Tribunal accompaniment."
        ),
        "source": "Legal Aid Department (HK); Duty Lawyer Service; MFMW",
    },

    # ── Prosecution Statistics ─────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "HK Trafficking-Related Prosecution Statistics (2018-2024)",
        "summary": (
            "Since the 2018 Action Plan, HK has not enacted specific "
            "anti-trafficking legislation. Trafficking-related cases "
            "prosecuted under existing laws: Employment Ordinance "
            "violations (30-50/year), assault/GBH against FDHs "
            "(15-30/year), sexual offences against FDHs (5-15/year), "
            "false imprisonment (rare, 1-3/year). Zero prosecutions "
            "specifically for forced labour or trafficking since HK "
            "lacks such offences. US TIP Report 2024 rated HK as "
            "Tier 2 Watch List for the third consecutive year, noting "
            "'the government did not demonstrate overall increasing "
            "efforts to eliminate trafficking.'"
        ),
        "source": "US State Department TIP Report 2024; Security Bureau (HK)",
    },

    # ── Consulate Support Services ─────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Philippine and Indonesian Consulates — FDH Assistance in HK",
        "summary": (
            "Philippine Consulate General in HK provides: Assistance to "
            "Nationals (ATN) unit for distressed OFWs, temporary shelter "
            "(Bethune House partnership), legal advice, repatriation "
            "assistance, contract verification, POLO (Philippine Overseas "
            "Labor Office) for employment complaints. Indonesian "
            "Consulate General provides: crisis shelter, legal aid "
            "referral, mediation between workers and employers, "
            "coordination with BNP2MI. Both consulates receive "
            "thousands of complaints annually from FDHs."
        ),
        "source": "Philippine Consulate General HK; Indonesian Consulate General HK",
    },

    # =========================================================================
    # 5. HONG KONG-SPECIFIC EXPLOITATION PATTERNS
    # =========================================================================

    # ── Indonesian vs Filipino Treatment Differences ───────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Indonesian vs Filipino Domestic Worker Treatment Differences in HK",
        "summary": (
            "Research documents differential treatment based on "
            "nationality. Indonesian FDHs face: (1) higher agency fees "
            "(USD 1,500-3,000 vs USD 500-1,500 for Filipinos) due to "
            "less regulated recruitment in Indonesia, (2) language "
            "barriers (fewer speak Cantonese or English), (3) lower "
            "negotiating power (perceived as more 'compliant'), (4) "
            "less access to legal information (Filipino community better "
            "organized with FMWU and Migrante). Filipino FDHs: generally "
            "better English, stronger community networks, higher legal "
            "literacy, but still face systemic exploitation. Indonesian "
            "workers comprise majority of extreme abuse cases documented "
            "by MFMW."
        ),
        "source": "Justice Centre Hong Kong; MFMW; IDWF",
    },

    # ── Training Center Exploitation ───────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Indonesian 'Training Center' Exploitation for HK-Bound Workers",
        "summary": (
            "Prospective Indonesian domestic workers are held in "
            "'training centers' (pelatihan) in Java, Surabaya, and "
            "other locations for 3-6 months before deployment to HK. "
            "Workers confined to centers, subjected to strict discipline, "
            "given minimal actual training. Charged IDR 15-30 million "
            "(USD 1,000-2,000) for training, accommodation, and food. "
            "Debt recovered through 5-8 months salary deductions upon "
            "arrival in HK. Centers controlled by agencies linked to "
            "HK placement firms. Indonesia's BNP2MI has attempted "
            "regulation but enforcement is limited. Some centers "
            "documented as using physical punishment and restricting "
            "communication with families."
        ),
        "source": "BNP2MI; Human Rights Watch; Anti-Slavery International",
    },

    # ── Agency Fee Exploitation Detail ─────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Agency Fee Exploitation — Prohibited Overcharging Mechanisms",
        "summary": (
            "Employment Agency Regulations cap fees at 10% of first "
            "month's salary per contract year (max HKD 1,020 for 2-year "
            "SEC at HKD 5,100 MAW). Mechanisms for circumventing the "
            "cap: (1) 'training fees' charged in origin country not "
            "subject to HK law, (2) loans from agency-linked lenders "
            "requiring monthly repayments from salary, (3) mandatory "
            "purchase of overpriced supplies (uniforms, luggage, SIM "
            "cards) at airport, (4) 'deposit' held by agency returned "
            "only on contract completion, (5) 'administration fees' for "
            "contract renewal. Total cost to worker: HKD 10,000-40,000 "
            "per contract cycle. Workers who break contracts early lose "
            "deposits and face blacklisting by agencies."
        ),
        "source": "Justice Centre Hong Kong; Labour Department; HKFP documentary (2016)",
    },

    # ── Sexual Harassment/Assault by Employers ─────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Sexual Harassment and Assault of FDHs by Employers in HK",
        "summary": (
            "Live-in requirement places FDHs at heightened risk of sexual "
            "harassment and assault. Between 2019 and June 2024, 87 "
            "reports of rape or indecent assault by employers were filed "
            "with police. Only 9 convictions obtained (2019-2023). "
            "Barriers to reporting: (1) fear of two-week rule "
            "deportation, (2) employer controls communication, (3) "
            "shame and cultural stigma, (4) police skepticism, (5) "
            "employer counter-accusations. FDHs who report may be "
            "re-traumatized during lengthy court proceedings while "
            "unable to work. Sex Discrimination Ordinance provides "
            "civil remedies through EOC but is rarely utilized."
        ),
        "source": "Al Jazeera; Hong Kong Free Press; Hong Kong Police statistics",
    },

    # ── Employer Loan-Out / Multiple Households ────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Unauthorized Loan-Out of FDHs to Multiple Households",
        "summary": (
            "SEC restricts FDHs to performing domestic duties for the "
            "specified employer at the specified address. Documented "
            "violation: employers 'loan out' FDHs to relatives, "
            "neighbors, or friends — sometimes multiple households — "
            "without additional compensation. Workers afraid to refuse "
            "due to termination threat. Practice constitutes employment "
            "outside terms of visa (criminal offence for worker under "
            "Immigration Ordinance, not employer). Workers caught "
            "working in unauthorized locations face prosecution and "
            "deportation, not employers. Immigration Department has "
            "acknowledged the issue but prosecutions target workers, "
            "not the employers who arranged the unauthorized work."
        ),
        "source": "MFMW; FADWU; Immigration Ordinance Cap. 115",
    },

    # ── Pregnancy Discrimination ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Pregnancy Discrimination Against FDHs — Unlawful Termination",
        "summary": (
            "Employment Ordinance s.15 prohibits dismissal of pregnant "
            "employees. Despite this, pregnant FDHs face systematic "
            "termination: employers terminate contracts upon learning "
            "of pregnancy, often citing fabricated performance issues. "
            "Pregnant FDHs who lose employment face: two-week rule "
            "deportation, loss of healthcare (employer-provided under "
            "SEC), inability to find new employer willing to hire "
            "pregnant worker. PathFinders assists 1,000+ pregnant "
            "or new-mother FDHs annually in HK. Some FDHs become "
            "undocumented rather than leave HK while pregnant. Children "
            "born in HK to FDHs do not receive permanent residency."
        ),
        "source": "PathFinders; Employment Ordinance Cap. 57 s.15; MFMW",
    },

    # ── Debt Bondage Cycle ─────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Debt Bondage Cycle for FDHs in Hong Kong",
        "summary": (
            "Typical debt cycle: worker borrows USD 1,000-3,000 from "
            "agency or moneylender in origin country to pay recruitment "
            "fees and training costs. Arrives in HK with monthly salary "
            "of HKD 5,100 minus agency-mandated deductions of HKD "
            "2,000-3,000/month for first 5-8 months. Net take-home "
            "during debt repayment: HKD 2,000-3,000/month (USD "
            "250-385). Worker cannot leave or change employer without "
            "forfeiting 'deposit' and facing agency blacklisting. "
            "If terminated before debt is repaid, worker returns home "
            "in debt. Cycle restarts with each new contract. ILO "
            "classifies this as a forced labour indicator (debt bondage)."
        ),
        "source": "ILO; Justice Centre Hong Kong; Verité",
    },

    # ── Isolation and Communication Restriction ────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Isolation and Communication Restrictions on FDHs",
        "summary": (
            "Documented employer control mechanisms: confiscating mobile "
            "phones, limiting or monitoring phone calls to family, "
            "prohibiting contact with other domestic workers, locking "
            "workers inside apartment during employer's absence, "
            "restricting movement on rest days (must return by specific "
            "time), forbidding attendance at community gatherings. "
            "Isolation prevents workers from: learning their rights, "
            "accessing NGO support, gathering evidence for complaints, "
            "building support networks. Particularly acute for "
            "Indonesian workers with limited English or Cantonese. "
            "ILO identifies isolation as one of 11 forced labour "
            "indicators."
        ),
        "source": "ILO indicators; MFMW; Justice Centre Hong Kong",
    },

    # ── Online Maid Trading ────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Online Domestic Worker 'Trading' Platforms in HK",
        "summary": (
            "Social media platforms (Facebook groups, WhatsApp, "
            "Instagram) used to advertise domestic workers for 'transfer' "
            "between employers. Workers advertised with photos, "
            "nationality, age, 'skills,' and transfer fee (HKD "
            "5,000-20,000). Workers may not consent to being listed. "
            "Practice mirrors Gulf 'maid trading' documented by BBC. "
            "While not illegal per se under HK law (if workers consent "
            "and no overcharging occurs), the commodification of workers "
            "raises trafficking concerns. Labour Department has not "
            "taken enforcement action against online platforms. Some "
            "platforms also facilitate illegal direct hire bypassing "
            "licensed agencies."
        ),
        "source": "BBC Arabic (parallel Gulf investigation); SCMP; FADWU",
    },

    # ── Undocumented FDHs ──────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Undocumented FDHs — Overstayers and Vulnerable Population",
        "summary": (
            "FDHs who flee abusive employers and cannot find new "
            "placement within 14 days become undocumented overstayers. "
            "Estimated several thousand undocumented FDHs in HK at any "
            "time. Extremely vulnerable: cannot access legal employment, "
            "healthcare, or housing; rely entirely on NGO shelters and "
            "community support; risk arrest, detention, and deportation "
            "if identified by police. Some engage in unauthorized work "
            "(cleaning, caregiving) for survival. Immigration Department "
            "does not screen overstaying FDHs for trafficking "
            "victimization as standard practice."
        ),
        "source": "Justice Centre Hong Kong; MFMW; US TIP Report",
    },

    # ── Employer-Controlled Banking ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Employer-Controlled Bank Accounts and Financial Coercion",
        "summary": (
            "Some employers open bank accounts in worker's name but "
            "retain the ATM card and PIN. Worker's salary deposited "
            "into the account but controlled by employer. Employer "
            "withdraws 'expenses' including unauthorized deductions. "
            "Worker cannot access own earnings. Practice also used to "
            "create appearance of wage payment for Labour Department "
            "inspection purposes while worker receives less than "
            "deposited amount. Banking Ordinance does not specifically "
            "address employer control of employee accounts. MFMW "
            "advises workers to open their own accounts at Remittance "
            "or Chong Hing Bank which offer FDH-friendly services."
        ),
        "source": "MFMW; Justice Centre Hong Kong; Labour Department guidance",
    },

    # ── Verbal and Psychological Abuse ─────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Verbal and Psychological Abuse of FDHs — Underreported Pattern",
        "summary": (
            "Most common form of abuse reported by FDHs but least "
            "prosecuted. Includes: constant shouting and belittling, "
            "racist slurs, threats of termination and deportation, "
            "humiliation in front of family members or children, "
            "blaming worker for any household problem, threats to "
            "report worker to Immigration Department. Psychological "
            "effects: anxiety, depression, PTSD, suicidal ideation. "
            "Justice Centre research found 38% of surveyed FDHs "
            "experienced verbal abuse. Criminal intimidation charges "
            "possible but rarely filed; Employment Ordinance does not "
            "address workplace bullying. No mandatory mental health "
            "support for FDHs."
        ),
        "source": "Justice Centre Hong Kong 'Coming Clean' (2016); MFMW; ILO",
    },

    # ── Death Cases ────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "FDH Deaths in Employment — Reporting and Investigation Gaps",
        "summary": (
            "Deaths of FDHs during employment include: falls from "
            "windows (reported as 'accidents' or 'suicides'), "
            "unexplained medical emergencies, and consequences of "
            "prolonged abuse. Coroner's Court investigates deaths but "
            "does not systematically examine for trafficking or forced "
            "labour indicators. Families in origin countries often "
            "accept settlements without investigation. Pattern mirrors "
            "documented domestic worker deaths in Gulf states. No "
            "publicly available disaggregated data on FDH deaths in "
            "HK. Advocacy groups call for mandatory investigation "
            "protocol and trafficking screening for all FDH deaths."
        ),
        "source": "MFMW; Justice Centre Hong Kong; US TIP Report",
    },

    # ── Children of FDHs ───────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Children Born to FDHs in Hong Kong — Statelessness Risk",
        "summary": (
            "Children born in HK to FDH mothers do not acquire HK "
            "permanent residency (FDHs excluded from right of abode "
            "under Basic Law Art. 24). Children may face: statelessness "
            "if origin country does not recognize birth abroad, lack "
            "of documentation, inability to access healthcare or "
            "education in HK, separation from mothers who must continue "
            "working as live-in FDHs. PathFinders estimates 5,000+ "
            "such children in HK. Some employers terminate FDHs upon "
            "learning of pregnancy; children may be left with informal "
            "caregivers while mothers work."
        ),
        "source": "PathFinders; Basic Law Art. 24; UNHCR",
    },

    # ── Wage Theft via Remittance Manipulation ─────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Wage Theft via Forced Remittance Arrangements",
        "summary": (
            "Some agencies require FDHs to send salary through "
            "agency-designated remittance services charging above-market "
            "exchange rates (3-5% vs typical 1-2%). Workers may lose "
            "HKD 150-250/month in unfavorable rates. Some agencies "
            "require workers to remit to agency's account in origin "
            "country for 'forwarding' to family — skimming funds. "
            "Practice difficult to detect as it occurs outside HK "
            "regulatory jurisdiction. MFMW advises workers to use "
            "their own remittance channels. Labour Department does not "
            "regulate remittance requirements imposed by agencies."
        ),
        "source": "MFMW; Wise (TransferWise); Migrant Forum in Asia",
    },

    # ── Contract Substitution ──────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Contract Substitution — Different Job Upon Arrival in HK",
        "summary": (
            "Workers recruited for domestic work arrive to find: "
            "different employer than named on contract, additional "
            "duties beyond domestic work (e.g., helping in employer's "
            "shop, caring for elderly relatives at different address), "
            "or conditions materially different from SEC terms. SEC "
            "specifically defines permissible duties but enforcement "
            "relies on worker complaints. Workers performing non-domestic "
            "work are in breach of visa conditions (criminal offence for "
            "worker, not employer). Philippine DMW reports contract "
            "substitution affects 41% of complaint cases from HK."
        ),
        "source": "Philippine DMW; POLO Hong Kong; MFMW",
    },

    # ── Pandemic-Era Exploitation ──────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "COVID-19 Pandemic — Heightened FDH Exploitation in HK",
        "summary": (
            "COVID-19 (2020-2022) exacerbated FDH exploitation in HK: "
            "(1) mandatory testing/quarantine requirements created "
            "additional financial burden on workers, (2) employers "
            "prohibited workers from going out on rest days citing "
            "infection risk, (3) some employers terminated workers and "
            "hired replacements at lower wages during economic downturn, "
            "(4) stranded workers could not return home due to flight "
            "restrictions, (5) workers forced to accept unfavorable "
            "contract renewals. Government required FDHs to undergo "
            "mandatory COVID testing separately from employers, "
            "criticized as discriminatory."
        ),
        "source": "FADWU; Justice Centre Hong Kong; SCMP",
    },

    # ── N v Secretary for Security ─────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "N v Secretary for Security [2024] HKCFI 1983 — Trafficking Victim Protection",
        "summary": (
            "2024 Court of First Instance case addressing adequacy of "
            "protection for identified trafficking victims in HK. Court "
            "considered whether existing support mechanisms (temporary "
            "visa, shelter, counseling) meet international standards. "
            "Ruling examined HK's obligations under the Palermo Protocol "
            "and BOR4 positive duty framework established in ZN case. "
            "Highlighted ongoing gap between victim identification and "
            "practical protection, particularly for FDHs who fear "
            "deportation under the two-week rule and lack access to "
            "specialized trafficking victim services."
        ),
        "source": "HKCFI; Bernacchi Chambers; HK DOJ",
    },

    # ── Anti-Trafficking Legal Gap ─────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Hong Kong's Anti-Trafficking Legal Gap — No Specific Legislation",
        "summary": (
            "Unlike Singapore (PHTA 2014), UK (Modern Slavery Act 2015), "
            "Philippines (RA 9208), and even mainland China (Criminal "
            "Law Art. 240), Hong Kong has no specific anti-trafficking "
            "legislation. Crimes Ordinance s.129 covers only trafficking "
            "for prostitution. BOR4 prohibits forced labour but creates "
            "no criminal offence. Government relies on: Employment "
            "Ordinance (wage violations), Offences Against the Person "
            "Ordinance (assault/GBH), Theft Ordinance (fraud), and "
            "Immigration Ordinance. Academics, NGOs, and US TIP Report "
            "consistently call for comprehensive anti-trafficking law. "
            "Government maintains existing laws are 'adequate.'"
        ),
        "source": "Oxford Human Rights Hub; US TIP Report; Cogent Social Sciences (2024)",
    },

    # ── Employer Blacklisting ──────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Employer Blacklisting — Immigration Department Records",
        "summary": (
            "Immigration Department maintains a blacklist of employers "
            "convicted of FDH-related offences, who are banned from "
            "hiring FDHs for specified periods (typically 2-5 years). "
            "Blacklisted employers include those convicted of: assault, "
            "underpayment, failure to provide food/accommodation, or "
            "visa fraud. However, the blacklist is not publicly "
            "accessible — FDHs and agencies cannot check whether a "
            "potential employer has a history of abuse. Advocacy groups "
            "call for a public 'bad employer' registry similar to "
            "Singapore's MOM employer alert list."
        ),
        "source": "Immigration Department (HK); FADWU; Justice Centre Hong Kong",
    },

    # ── Code of Practice for Employment Agencies ───────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "HK",
        "title": "Code of Practice for Employment Agencies (2017, revised 2021)",
        "summary": (
            "Labour Department issued a voluntary Code of Practice for "
            "Employment Agencies in 2017, revised in 2021 with enhanced "
            "requirements: transparent fee schedule, written service "
            "agreement with workers, prohibition on withholding documents, "
            "mandatory display of license. Agencies 'expected' to comply "
            "but the Code is not legally binding. Non-compliance can be "
            "considered when renewing agency licenses. Labour Department "
            "conducts compliance inspections but coverage is limited "
            "(estimated 500-800 inspections/year for 4,000 agencies). "
            "NGOs criticize the Code as voluntary and unenforceable."
        ),
        "source": "Labour Department; Employment Agency Regulations; MFMW",
    },

    # ── Penalty Enhancement Advocacy ───────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Advocacy for Enhanced Penalties Against Exploitative Employers",
        "summary": (
            "Current penalties criticized as inadequate deterrent: "
            "maximum HKD 50,000 fine for agency overcharging (average "
            "actual fine HKD 1,500-45,000), maximum HKD 350,000 + 3 "
            "years for willful underpayment (rarely prosecuted). "
            "Advocacy groups demand: (1) increase maximum fine for "
            "overcharging to HKD 500,000, (2) mandatory prison for "
            "repeat offenders, (3) automatic license revocation on "
            "first conviction, (4) public naming of convicted agencies, "
            "(5) employer criminal liability for forced labour. "
            "Government has not proposed legislative amendments."
        ),
        "source": "FADWU; Justice Centre Hong Kong; US TIP Report recommendations",
    },

    # ── Coming Clean Report ────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Justice Centre 'Coming Clean' (2016) — Forced Labour Survey",
        "summary": (
            "Landmark 2016 survey by Justice Centre Hong Kong of 1,000 "
            "FDHs found: 1 in 6 (17%) experienced forced labour as "
            "defined by ILO indicators, 66% did not have a single day "
            "off in a typical month, 38% experienced verbal abuse, "
            "14% paid below MAW, 27% had excessive deductions from "
            "wages, 10% had passports retained, 8% experienced food "
            "deprivation, 3% experienced physical violence. The study "
            "used ILO forced labour indicators as methodology. Remains "
            "the most comprehensive quantitative study of FDH "
            "exploitation in HK."
        ),
        "source": "Justice Centre Hong Kong 'Coming Clean' (2016)",
    },

    # ── HKSAR TIP Report Response ──────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "US TIP Report — Hong Kong Tier 2 Watch List Rating (2022-2024)",
        "summary": (
            "US State Department Trafficking in Persons Report has "
            "rated Hong Kong as Tier 2 Watch List for three consecutive "
            "years (2022-2024). Key criticisms: (1) no specific "
            "anti-trafficking legislation, (2) zero trafficking "
            "prosecutions or convictions, (3) inadequate victim "
            "identification — only 16 potential victims identified "
            "(2023), (4) two-week rule and live-in requirement create "
            "structural vulnerability, (5) insufficient resources for "
            "victim services, (6) no public awareness campaigns on "
            "trafficking. Tier 2 Watch List means government does not "
            "fully meet minimum standards and is not making significant "
            "efforts to do so."
        ),
        "source": "US State Department TIP Report 2024",
    },

    # ── FDH Population Statistics ──────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Foreign Domestic Helper Population in Hong Kong (2024)",
        "summary": (
            "Approximately 340,000 FDHs in Hong Kong as of 2024, "
            "representing about 10% of the city's workforce and 5% "
            "of total population. Breakdown by nationality: Philippines "
            "54% (184,000), Indonesia 44% (150,000), others 2% "
            "(Thailand, India, Sri Lanka, Nepal, Bangladesh, Myanmar). "
            "98% female. Employed in approximately 1 in 8 HK households. "
            "Economic contribution: enables labor force participation of "
            "HK women, estimated GDP contribution of HKD 42 billion "
            "annually (2019 study). Average age: 35-40 years. Average "
            "length of service in HK: 7-10 years."
        ),
        "source": "Census and Statistics Department (HK); Immigration Department; ILO",
    },

    # ── Labour Relations Division Data ─────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Labour Relations Division — FDH Dispute Conciliation Statistics",
        "summary": (
            "Before cases reach Labour Tribunal, Labour Relations "
            "Division attempts conciliation. Approximately 5,000-6,000 "
            "FDH-related inquiries handled annually by the Division. "
            "Conciliation success rate for FDH cases: approximately 60%. "
            "Common issues conciliated: outstanding wages, wages in lieu "
            "of notice, annual leave pay, food allowance disputes. "
            "Conciliation is voluntary and non-binding — either party "
            "may proceed to Labour Tribunal if unsatisfied. Average "
            "conciliation settlement: HKD 5,000-15,000 (often less "
            "than full entitlement as workers accept quick resolution "
            "due to two-week rule pressure)."
        ),
        "source": "Labour Department Annual Report; Labour Relations Division",
    },

    # ── Wan Chai and Causeway Bay Gathering Spaces ─────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Sunday Gatherings — FDH Community Spaces and Support Networks",
        "summary": (
            "Every Sunday (the mandated rest day), tens of thousands of "
            "FDHs gather in public spaces across HK: Central district "
            "(Statue Square, HSBC Building forecourt), Victoria Park "
            "(Causeway Bay), Wan Chai. These gatherings serve as: social "
            "support networks, information sharing on rights and legal "
            "aid, informal counseling, remittance coordination, and "
            "community organizing. NGOs and unions (FADWU, MFMW, "
            "Migrante) set up information stalls. Gatherings demonstrate "
            "the live-in requirement's impact — FDHs have no private "
            "space and must use public areas for social life. Government "
            "has occasionally attempted to restrict gatherings citing "
            "public order concerns."
        ),
        "source": "FADWU; MFMW; Al Jazeera; CNN",
    },

    # ── Private Employment Agencies Administration ─────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Employment Agencies Administration (EAA) — Regulatory Data",
        "summary": (
            "As of 2024, approximately 4,000 licensed employment agencies "
            "in HK, many specializing in FDH placement. EAA conducts "
            "500-800 inspections annually. Agency license renewal fee: "
            "HKD 15,200 for 2-year period. Grounds for refusal/revocation: "
            "conviction for overcharging, unlicensed operation, fraud, or "
            "Employment Ordinance violations. However, agencies can "
            "re-register under different names or through nominees. "
            "No public database of agency compliance records or "
            "complaints. Workers cannot verify agency reputation before "
            "signing contracts."
        ),
        "source": "Labour Department EAA; Employment Agency Regulations",
    },

    # ── Penalty for Underpayment ───────────────────────────────────────────
    {
        "type": "penalty",
        "jurisdiction": "HK",
        "title": "Underpayment of FDH Minimum Allowable Wage — Criminal Penalty",
        "summary": (
            "Under Employment Ordinance Cap. 57 s.63B, willful and "
            "without reasonable excuse failure to pay wages when due is "
            "a criminal offence: maximum fine HKD 350,000 and "
            "imprisonment for 3 years. Applies to underpayment below "
            "MAW. Labour Department refers cases for prosecution but "
            "conviction rate remains low. Employer may also be: banned "
            "from hiring FDHs (Immigration Department blacklist), "
            "ordered to pay back-wages (Labour Tribunal), and required "
            "to pay compensation for wrongful dismissal if worker was "
            "terminated for complaining."
        ),
        "source": "Employment Ordinance Cap. 57 s.63B; Labour Department",
    },

    # ── Penalty for Agency Overcharging ────────────────────────────────────
    {
        "type": "penalty",
        "jurisdiction": "HK",
        "title": "Employment Agency Overcharging Penalty — Cap. 57 Part XII",
        "summary": (
            "Employment Ordinance s.53 limits agency commission to 10% "
            "of first month's wages per contract year. Overcharging is "
            "a criminal offence: maximum fine HKD 50,000. On conviction, "
            "Commissioner for Labour may revoke agency license. Worker "
            "may recover overcharged amount through Labour Tribunal "
            "claim. Actual fines imposed: HKD 1,500-45,000 (well below "
            "maximum). NGOs argue penalties must be increased to at "
            "least HKD 500,000 with mandatory imprisonment for repeat "
            "offenders to create effective deterrent. Prosecution rate: "
            "2-11 agencies per year vs estimated thousands overcharging."
        ),
        "source": "Employment Ordinance Cap. 57 s.53; Labour Department; HKFP",
    },

    # ── Penalty for Assault on FDH ─────────────────────────────────────────
    {
        "type": "penalty",
        "jurisdiction": "HK",
        "title": "Assault on FDH — Criminal Penalties Under OAPO",
        "summary": (
            "Employers who assault FDHs prosecuted under Offences Against "
            "the Person Ordinance (Cap. 212): common assault (max 1 year "
            "imprisonment), assault occasioning actual bodily harm (max "
            "3 years), wounding or inflicting GBH (max 3 years or 7 "
            "years on indictment), wounding with intent (max life "
            "imprisonment). Erwiana case: employer sentenced to 6 years "
            "for GBH. Kartika case: employers sentenced to 3 years "
            "3 months and 5 years. Sentencing guidelines for domestic "
            "worker abuse cases established post-Erwiana, recognizing "
            "the aggravating factor of employer-employee power imbalance "
            "and abuse of trust."
        ),
        "source": "OAPO Cap. 212; HKSAR v Law Wan-tung; Kartika case",
    },

    # ── ILO Indicators in HK Context ───────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "ILO Forced Labour Indicators Applied to HK FDH Employment",
        "summary": (
            "Applying ILO's 11 forced labour indicators to HK FDH "
            "employment reveals systemic risks: (1) Abuse of "
            "vulnerability — immigration dependency, two-week rule; "
            "(2) Deception — contract substitution, false job "
            "descriptions; (3) Restriction of movement — live-in "
            "requirement, locked apartments; (4) Isolation — "
            "communication control, language barriers; (5) Physical "
            "violence — documented in court cases; (6) Intimidation — "
            "deportation threats; (7) Document retention — passport "
            "confiscation; (8) Wage withholding — underpayment, "
            "deductions; (9) Debt bondage — agency fees; (10) Abusive "
            "working conditions — excessive hours, no private space; "
            "(11) Excessive overtime — 16-21 hour days documented."
        ),
        "source": "ILO Indicators of Forced Labour; Justice Centre Hong Kong",
    },

    # ── Right of Abode Exclusion ───────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Vallejos v Commissioner of Registration [2013] HKCFA 20 — FDH Right of Abode",
        "summary": (
            "Court of Final Appeal ruled that FDHs are excluded from "
            "the right to apply for permanent residency under Basic Law "
            "Art. 24(2)(4), regardless of length of continuous ordinary "
            "residence. Evangeline Banao Vallejos, a Filipino FDH who "
            "had lived in HK for 25+ years, challenged the exclusion. "
            "CFA held that FDHs are not ordinarily resident as their "
            "visas are subject to conditions (must leave on contract "
            "termination). Decision means FDHs can never obtain "
            "permanent residency in HK, maintaining them as a permanent "
            "underclass regardless of decades of contribution to HK "
            "society and economy."
        ),
        "source": "HKCFA; Basic Law Art. 24(2)(4)",
    },

    # ── Minimum Wage Ordinance Exclusion ───────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Minimum Wage Ordinance (Cap. 608) — FDH Exclusion",
        "summary": (
            "Hong Kong's Minimum Wage Ordinance (enacted 2011) sets "
            "statutory minimum wage for all employees (HKD 40/hour as "
            "of 2023). However, FDHs are explicitly excluded from the "
            "Minimum Wage Ordinance. Instead, FDHs are subject to the "
            "Minimum Allowable Wage (MAW) set administratively by the "
            "government. The MAW (HKD 5,100/month as of 2025) is "
            "significantly lower than what full-time workers would earn "
            "under the statutory minimum wage (approximately HKD 8,320 "
            "for a 48-hour week). This exclusion maintains a separate "
            "and lower wage floor for domestic workers."
        ),
        "source": "Minimum Wage Ordinance Cap. 608; Labour Department; FADWU",
    },

    # ── Protection of Wages on Insolvency Fund ─────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Protection of Wages on Insolvency Fund (PWIF) — FDH Access",
        "summary": (
            "PWIF under Cap. 57 Part IXA covers FDHs whose employers "
            "become insolvent: arrears of wages (max 4 months), wages "
            "in lieu of notice (max 1 month), severance payment, "
            "untaken annual leave/statutory holiday pay. Maximum per "
            "employee: approximately HKD 80,000 per item. FDHs must "
            "apply through Labour Department. Processing time: 6-12 "
            "weeks. Workers must remain in HK to receive payment, "
            "creating conflict with two-week rule. Fund has paid out "
            "HKD 300-500 million annually across all employee types."
        ),
        "source": "Labour Department PWIF; Employment Ordinance Part IXA",
    },

    # ── Discrimination in Hiring ───────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Nationality-Based Wage Discrimination in FDH Hiring",
        "summary": (
            "While all FDHs are entitled to the same MAW regardless of "
            "nationality, agencies and employers practice informal "
            "wage discrimination: Filipino workers generally receive "
            "the MAW or slightly above, while Indonesian workers are "
            "more frequently paid exactly the MAW with higher agency "
            "deductions, resulting in lower net income. Agencies "
            "advertise different 'packages' by nationality with varying "
            "fee structures. This practice violates the Race "
            "Discrimination Ordinance but is difficult to prove as "
            "formal contracts show the MAW for all workers."
        ),
        "source": "Justice Centre Hong Kong; IDWF; Race Discrimination Ordinance Cap. 602",
    },

    # ── US State Department TIP Report Recommendations ─────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "US TIP Report 2024 — Priority Recommendations for Hong Kong",
        "summary": (
            "US State Department TIP Report 2024 key recommendations "
            "for HK: (1) enact comprehensive anti-trafficking legislation "
            "criminalizing all forms of trafficking, (2) increase "
            "funding for victim identification and services, (3) "
            "proactively screen vulnerable populations (FDHs, sex "
            "workers) for trafficking indicators, (4) amend two-week "
            "rule to allow trafficking victims to remain, (5) "
            "significantly increase penalties for agency overcharging, "
            "(6) provide specialized training for judges on trafficking "
            "indicators, (7) establish formal mechanism for trafficking "
            "victim recognition with associated rights and services."
        ),
        "source": "US State Department TIP Report 2024",
    },

    # ── Frontiers Research (2024) ──────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Academic Analysis — HK Anti-Trafficking Framework Compared to Europe (2024)",
        "summary": (
            "Frontiers in Sociology (2024) and Cogent Social Sciences "
            "(2024) published comparative analyses of HK's anti-trafficking "
            "framework. Key findings: (1) HK lacks equivalent to EU "
            "Anti-Trafficking Directive or UK Modern Slavery Act, (2) "
            "victim identification rate in HK (16 in 2023) is orders of "
            "magnitude below comparable European jurisdictions, (3) no "
            "National Referral Mechanism equivalent exists, (4) civil "
            "society fills roles that should be performed by government, "
            "(5) court rulings (ZN, CB) have forced incremental reform "
            "but legislative action is absent, (6) HK's approach "
            "described as 'piecemeal and reactive.'"
        ),
        "source": "PMC/Frontiers in Sociology (2024); Cogent Social Sciences (2024)",
    },

    # ── Wage Protection System Gap ─────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "No Electronic Wage Protection System for FDHs in HK",
        "summary": (
            "Unlike Qatar (WPS mandatory since 2015) and Saudi Arabia "
            "(WPS for firms with 10+ employees), Hong Kong does not "
            "require employers to pay FDH wages through any electronic "
            "or traceable system. Cash payments are lawful, making "
            "underpayment difficult to prove in Labour Tribunal claims "
            "(employer can claim cash was paid). Labour Department has "
            "recommended bank transfers but this is not mandatory. "
            "FADWU and MFMW advocate for mandatory electronic wage "
            "payment to create auditable records and reduce "
            "underpayment disputes."
        ),
        "source": "FADWU; MFMW; Labour Department guidance",
    },

    # ── Indonesian Moratorium Threats ──────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "HK",
        "title": "Indonesian Government — Threats of HK Deployment Moratorium",
        "summary": (
            "Indonesia has periodically threatened to impose a "
            "moratorium on domestic worker deployment to HK (similar to "
            "Malaysia moratorium 2009-2011 and Saudi temporary bans). "
            "Triggers: high-profile abuse cases (Erwiana), agency "
            "overcharging, inadequate legal protections. BNP2MI "
            "negotiated Memorandum of Understanding with HK on improved "
            "conditions. A moratorium would affect approximately 150,000 "
            "Indonesian FDHs in HK and their families. Threat serves as "
            "diplomatic lever for improved protections. Philippines has "
            "similarly used deployment restrictions as leverage."
        ),
        "source": "BNP2MI; Indonesian Consulate General HK; SCMP",
    },

    # ── Shelter Capacity ───────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "Shelter Capacity for Distressed FDHs in Hong Kong",
        "summary": (
            "Total shelter capacity for distressed FDHs in HK: "
            "approximately 150-200 beds across NGO shelters. Major "
            "providers: Bethune House (MFMW, 40 beds), Justice Centre "
            "temporary housing, PathFinders for pregnant workers, "
            "Philippine Consulate-partnered shelters, Indonesian "
            "Consulate shelter. Government provides no direct shelter "
            "for FDHs (Social Welfare Department shelters primarily "
            "serve local residents). At peak periods (contract renewal "
            "season, post-Lunar New Year), demand exceeds supply by "
            "estimated 50%. Workers waiting for Labour Tribunal cases "
            "may need shelter for 8-15 months."
        ),
        "source": "MFMW Bethune House; PathFinders; Justice Centre Hong Kong",
    },

    # ── HKSAR v Cheung Yuen-man — Historical Abuse Case ────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "HKSAR v Cheung Yuen-man — Domestic Worker Assault and Confinement",
        "summary": (
            "Employer convicted of assault and false imprisonment of "
            "Indonesian domestic worker. Worker was: slapped repeatedly, "
            "denied food, locked inside apartment, forced to work "
            "18-hour days, and prevented from contacting family or "
            "leaving the premises. Sentenced to imprisonment. Case "
            "pre-dated Erwiana but received limited public attention. "
            "Illustrates recurring pattern: physical violence, food "
            "deprivation, confinement, and wage theft occurring "
            "simultaneously as components of coercive control."
        ),
        "source": "Hong Kong District Court; MFMW case records",
    },

    # ── Mutual Legal Assistance ────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Cross-Jurisdictional Enforcement — HK-Philippines-Indonesia",
        "summary": (
            "Enforcement challenges span multiple jurisdictions: agency "
            "overcharging occurs partly in origin country (Philippines, "
            "Indonesia) and partly in HK. HK Labour Department cannot "
            "investigate or prosecute agencies operating in other "
            "jurisdictions. Mutual legal assistance agreements exist "
            "but are rarely used for employment agency cases. Indonesian "
            "training center exploitation falls entirely outside HK "
            "jurisdiction. Workers who wish to file complaints against "
            "origin-country agencies after returning home face different "
            "legal systems with potentially weaker enforcement."
        ),
        "source": "ILO; MFMW; Justice Centre Hong Kong",
    },

    # ── ILO Domestic Workers Convention Ratification Gap ───────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "ILO C189 Non-Ratification by China (Applicable to HK)",
        "summary": (
            "China has not ratified ILO Convention 189 (Domestic Workers "
            "Convention, 2011). As HK is a Special Administrative Region "
            "of China, C189 is not applicable to HK. C189 provides: "
            "normal hours of work, weekly rest (24 consecutive hours "
            "minimum), minimum wage coverage, social security, written "
            "contracts, protection from violence. While HK domestic law "
            "covers some C189 provisions through the Employment "
            "Ordinance and SEC, gaps remain: no maximum working hours "
            "for FDHs, live-in requirement not addressed, social "
            "security limited, and immigration-linked conditions create "
            "vulnerability not contemplated by C189."
        ),
        "source": "ILO NORMLEX; IDWF; FADWU",
    },

    # ── Human Trafficking in HK Academic Review ────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Judicial Attitudes Towards FDHs in HK Criminal Courts (2023)",
        "summary": (
            "Taylor & Francis Online published a study (2023) analyzing "
            "judicial attitudes towards FDHs in Hong Kong criminal "
            "courts. Findings: (1) sentences for employer violence "
            "against FDHs tend to be lighter than comparable cases "
            "involving local victims, (2) judges sometimes apply "
            "mitigating factors for employers (stress, cultural "
            "differences) that are not applied in other assault cases, "
            "(3) FDH witness credibility is sometimes questioned based "
            "on nationality stereotypes, (4) post-Erwiana sentencing "
            "guidelines improved outcomes but inconsistently applied."
        ),
        "source": "Taylor & Francis (2023); Hong Kong Lawyer Journal",
    },

    # ── Domestic Worker Insurance ──────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Mandatory Insurance for FDH Employers",
        "summary": (
            "Employers must maintain two types of insurance for FDHs: "
            "(1) Employees' Compensation Insurance under Cap. 282 "
            "covering work-related injuries and occupational diseases "
            "(minimum HKD 100 million per event), and (2) insurance "
            "under the SEC covering medical expenses for non-work "
            "illnesses (varies by policy). Failure to maintain employees' "
            "compensation insurance: HKD 100,000 fine + 2 years "
            "imprisonment. Some employers purchase minimum policies "
            "that do not adequately cover FDH medical needs, particularly "
            "for pre-existing conditions or pregnancy-related costs."
        ),
        "source": "Employees' Compensation Ordinance Cap. 282; SEC ID 407",
    },

    # ── Post-Erwiana Reforms ───────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "HK",
        "title": "Post-Erwiana Reforms — Government Response (2015-2018)",
        "summary": (
            "Following the Erwiana case (2015), HK Government implemented "
            "incremental reforms: (1) increased MAW from HKD 4,010 to "
            "HKD 4,210 (2015), (2) enhanced Code of Practice for "
            "Employment Agencies (2017), (3) Action Plan to Tackle "
            "Trafficking in Persons (2018), (4) expanded Labour "
            "Department training on trafficking indicators, (5) "
            "inter-departmental task force on trafficking. However: no "
            "legislative changes enacted, two-week rule unchanged, "
            "live-in requirement unchanged, penalty levels unchanged. "
            "NGOs characterized reforms as 'cosmetic' and 'insufficient.'"
        ),
        "source": "Security Bureau; Labour Department; Justice Centre Hong Kong",
    },

    # =========================================================================
    # 6. ADDITIONAL COURT CASES AND ENFORCEMENT DETAILS
    # =========================================================================

    # ── False Imprisonment Cases ─────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "DCCC False Imprisonment Prosecutions — FDH Confinement Cases",
        "summary": (
            "Multiple District Court cases where employers convicted of "
            "false imprisonment for locking FDHs inside apartments. "
            "Workers confined during employer's absence (work hours), "
            "on rest days, or as punishment. Sentences: 6-18 months "
            "imprisonment. Prosecution requires proof worker was "
            "physically prevented from leaving; verbal prohibition "
            "insufficient unless coupled with threats. Workers report "
            "being locked in from outside, deadbolts requiring keys, "
            "or removal of door handles. False imprisonment remains "
            "undercharged — many cases prosecuted only as assault."
        ),
        "source": "Hong Kong District Court records; MFMW case data",
    },

    # ── Labour Tribunal Jurisdictional Limits ────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Labour Tribunal Jurisdiction — Limits for FDH Claims",
        "summary": (
            "Labour Tribunal (Cap. 25) handles FDH employment claims up "
            "to HKD 8,000 (Minor Employment Claims Adjudication Board "
            "for claims under HKD 8,000). Claims exceeding tribunal "
            "limits must go to District Court, requiring legal "
            "representation that most FDHs cannot afford. Tribunal is "
            "designed for speed (no lawyers permitted for claims under "
            "HKD 8,000) but FDHs face disadvantages: language barriers, "
            "lack of documentation (employer holds records), and "
            "unfamiliarity with Hong Kong legal procedures. MFMW and "
            "Justice Centre provide paralegal support but demand "
            "exceeds capacity."
        ),
        "source": "Labour Tribunal Ordinance Cap. 25; MFMW; Justice Centre HK",
    },

    # ── Elderly Care and FDH Exploitation ────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Elderly Care Burden on FDHs — Scope-of-Work Exploitation",
        "summary": (
            "HK's aging population (19% over 65 by 2024) increasingly "
            "relies on FDHs for elderly care: 24-hour bedside care, "
            "lifting/transferring patients, medication management, "
            "catheter and wound care. These medical/nursing tasks exceed "
            "SEC definition of 'domestic duties.' FDHs receive no "
            "training for clinical care, risking injury to both worker "
            "and elderly person. Workers who refuse clinical tasks face "
            "termination. No regulation distinguishes domestic help from "
            "nursing care. Labour Department has not issued guidance on "
            "permissible scope of FDH duties in elderly care contexts."
        ),
        "source": "MFMW; Hong Kong Council of Social Service; PathFinders",
    },

    # ── Mid-Contract Termination Pattern ─────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Strategic Mid-Contract Termination by Employers",
        "summary": (
            "Pattern of employers terminating FDH contracts shortly "
            "before 2-year completion to avoid paying: (1) return "
            "passage to origin country (approx. HKD 2,000-5,000), "
            "(2) accrued annual leave, (3) long service payment "
            "(for workers completing 5+ years). Employers fabricate "
            "misconduct allegations to justify summary dismissal "
            "without notice pay. Workers terminated without notice "
            "have only 14 days to file Labour Tribunal claims while "
            "also searching for new employment or preparing to leave "
            "HK. Pattern particularly affects Indonesian FDHs with "
            "weaker community legal support networks."
        ),
        "source": "MFMW; FADWU; Labour Tribunal case patterns",
    },

    # ── HKCTU Support for FDHs ───────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Hong Kong Confederation of Trade Unions (HKCTU) — FDH Support",
        "summary": (
            "HKCTU (until dissolution in 2021) provided significant "
            "support to FDH organizing: legal clinics, Labour Tribunal "
            "accompaniment, collective bargaining advocacy, and lobbying "
            "for MAW increases. Post-dissolution, affiliated unions "
            "and successor organizations continue some services. "
            "FADWU and individual domestic worker unions maintain "
            "independent operations. FDH union membership in HK "
            "estimated at 5,000-10,000 (under 3% of FDH population), "
            "reflecting barriers to organizing live-in workers."
        ),
        "source": "HKCTU records; FADWU; ILO",
    },

    # ── Pre-Departure Orientation ────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Pre-Departure Orientation Seminars (PDOS) — Effectiveness for HK-Bound Workers",
        "summary": (
            "Philippines requires PDOS for all departing OFWs. Indonesia "
            "requires similar orientation. Content includes: HK labor "
            "laws, SEC terms, complaint mechanisms, emergency contacts. "
            "Effectiveness criticized: (1) conducted in groups of "
            "100-200, minimal interaction, (2) agency-run PDOS may "
            "omit critical rights information, (3) workers often "
            "overwhelmed with paperwork and do not retain information, "
            "(4) orientation occurs after workers have already incurred "
            "debt and committed to employment, reducing practical "
            "utility. MFMW conducts supplementary rights workshops at "
            "Sunday gatherings in HK."
        ),
        "source": "Philippine DMW; BNP2MI; MFMW; ILO",
    },

    # ── HK-PH Bilateral Agreement ────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "HK",
        "title": "HK-Philippines Bilateral Labour Agreement for FDHs",
        "summary": (
            "HK and Philippines maintain bilateral arrangements on FDH "
            "employment. Philippines requires: minimum USD 400/month "
            "salary (superseded by HK MAW), verified employment "
            "contract, PDOS completion, OWWA membership, PhilHealth "
            "contribution, and age minimum 23 for domestic workers. "
            "POLO Hong Kong verifies contracts and conducts employer "
            "blacklist checks. However, Philippines cannot enforce "
            "conditions once workers are in HK. Bilateral mechanisms "
            "described as 'necessary but insufficient' by ILO."
        ),
        "source": "POLO Hong Kong; Philippine DMW; ILO",
    },

    # ── Agency License Regime ────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Employment Agency License Requirements — Cap. 57 Part XII",
        "summary": (
            "Employment agencies placing FDHs must hold a license from "
            "the Commissioner for Labour. License fee: HKD 15,200 for "
            "2-year period. Requirements: fit and proper person test, "
            "financial references, designated premises. License "
            "conditions: maintain records for 6 years, display license "
            "prominently, comply with fee caps. Commissioner may refuse, "
            "suspend, or revoke licenses for: conviction for overcharging "
            "or fraud, operating without license, breaching Code of "
            "Practice. However, enforcement is complaint-driven with "
            "limited proactive inspection capacity."
        ),
        "source": "Employment Ordinance Cap. 57 Part XII; Labour Department",
    },

    # ── Occupational Health Risks ────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Occupational Health Risks for FDHs in Hong Kong",
        "summary": (
            "FDHs face specific occupational health risks: (1) repetitive "
            "strain injuries from hand-washing, mopping, lifting children "
            "and elderly, (2) exposure to cleaning chemicals without PPE, "
            "(3) burns from cooking and ironing, (4) falls from window "
            "cleaning (several FDH deaths from falls while cleaning "
            "external windows at height), (5) mental health impacts from "
            "isolation, abuse, and family separation. Employees' "
            "Compensation Ordinance covers work injuries but many FDHs "
            "do not report injuries for fear of termination. Government "
            "issued guidelines against requiring window cleaning at "
            "height but these are advisory, not mandatory."
        ),
        "source": "Labour Department; Employees' Compensation Ordinance Cap. 282; MFMW",
    },

    # ── Statutory Holidays ───────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Statutory Holidays for FDHs — Employment Ordinance",
        "summary": (
            "FDHs are entitled to 13 statutory holidays per year under "
            "the Employment Ordinance (increased from 12 in 2024). "
            "These include: Lunar New Year (3 days), Ching Ming, Labour "
            "Day, Buddha's Birthday, Tuen Ng, HKSAR Establishment Day, "
            "Mid-Autumn Festival, Chung Yeung, National Day, Winter "
            "Solstice or Christmas Day. If a statutory holiday falls on "
            "a rest day, the next working day is a holiday. Workers "
            "required to work on statutory holidays must receive "
            "alternative holiday. Many FDHs report being required to "
            "work on statutory holidays without compensation or "
            "replacement days."
        ),
        "source": "Employment Ordinance Cap. 57; Labour Department",
    },

    # ── Annual Leave Entitlement ─────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Annual Leave Entitlement for FDHs",
        "summary": (
            "Under Employment Ordinance, FDHs accrue annual leave after "
            "12 months of continuous employment: 7 days (1st year), "
            "increasing by 1 day per year of service up to 14 days "
            "(8th year onwards). Annual leave must be a continuous "
            "period (unless worker agrees to splitting). Employer must "
            "pay leave pay at average daily wage rate. SEC additionally "
            "provides for free return passage to origin country on "
            "completion of every 2-year contract. Workers who do not "
            "take annual leave are entitled to payment in lieu on "
            "termination."
        ),
        "source": "Employment Ordinance Cap. 57 Part VIII; SEC ID 407",
    },

    # ── Labour Department Hotline ────────────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Labour Department FDH-Specific Hotline and Multilingual Services",
        "summary": (
            "Labour Department operates dedicated complaint hotlines for "
            "FDHs: 2717 1771 (general employment complaints), 2157 9537 "
            "(employment agency complaints). Multilingual service "
            "available in: English, Cantonese, Tagalog, Bahasa Indonesia. "
            "Labour Department website (fdh.labour.gov.hk) provides "
            "FDH-specific information in multiple languages. Walk-in "
            "service at Labour Department offices in Wan Chai, Kowloon, "
            "and New Territories. Complaint processing time: 2-8 weeks "
            "for initial assessment, longer for investigation."
        ),
        "source": "Labour Department; fdh.labour.gov.hk",
    },

    # ── Wrongful Dismissal Claims ────────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "Labour Tribunal — Wrongful Dismissal of FDHs Pattern",
        "summary": (
            "Recurring Labour Tribunal cases where FDHs challenge wrongful "
            "dismissal. Common employer justifications rejected by "
            "Tribunal: (1) 'worker was too slow' (not gross misconduct), "
            "(2) 'worker used too much water/electricity' (not lawful "
            "grounds), (3) 'worker spoke to other helpers' (not "
            "misconduct), (4) employer relocating (must pay notice and "
            "passage), (5) worker became pregnant (unlawful under s.15). "
            "Tribunal awards typically include: wages in lieu of notice, "
            "outstanding wages, annual leave pay, and return passage. "
            "Some awards include compensation for unreasonable dismissal."
        ),
        "source": "Hong Kong Labour Tribunal; MFMW case records",
    },

    # ── FDH Accommodation Standards ──────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Accommodation Standards for FDHs — SEC and Practice",
        "summary": (
            "SEC requires employers to provide 'suitable accommodation' "
            "with 'reasonable privacy.' However, no minimum space "
            "standard is defined. In practice: many FDHs sleep on camp "
            "beds in kitchens, living rooms, storage areas, or share "
            "rooms with employer's children. HK's small flat sizes "
            "(median 40 sq m) make separate rooms rare. Some workers "
            "report sleeping in hallways, on balconies (covered), or "
            "in partitioned areas without doors. Immigration Department "
            "does not inspect accommodation before approving FDH visa "
            "applications. Labour Department considers accommodation "
            "'suitable' if it provides a bed and basic amenities."
        ),
        "source": "SEC ID 407; Immigration Department; MFMW; CNN",
    },

    # ── Technology-Enabled Surveillance ───────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Smart Home Technology and FDH Surveillance in HK",
        "summary": (
            "Growing use of smart home devices to monitor FDHs: CCTV "
            "cameras with remote viewing (including in worker sleeping "
            "areas), smart locks recording entry/exit times, GPS-enabled "
            "phones provided by employer to track movements on rest "
            "days, audio monitoring via smart speakers, and timer-based "
            "appliance monitoring to track work activities. No HK law "
            "specifically addresses employer surveillance of domestic "
            "workers in private homes. Personal Data Privacy Ordinance "
            "(Cap. 486) theoretically applies but PCPD has not issued "
            "guidance specific to FDH employment. Workers report "
            "feeling unable to refuse surveillance for fear of "
            "termination."
        ),
        "source": "PCPD; FADWU; Justice Centre Hong Kong",
    },

    # ── Repatriation Costs and Disputes ──────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "Return Passage Disputes — Employer Obligation Under SEC",
        "summary": (
            "SEC requires employer to pay return passage to worker's "
            "place of origin upon contract completion or termination. "
            "Disputes arise when: (1) employer provides one-way ticket "
            "to different destination, (2) employer deducts passage cost "
            "from final salary claiming 'early termination,' (3) worker "
            "wishes to remain in HK for new employment but employer "
            "insists on immediate departure, (4) employer bankrupt and "
            "unable to pay passage. Labour Tribunal awards passage costs "
            "when employer fails to provide. Philippine and Indonesian "
            "consulates provide emergency repatriation when employers "
            "default but resources are limited."
        ),
        "source": "SEC ID 407; Labour Tribunal; Philippine Consulate General HK",
    },

    # ── Social Media Rights Education ────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Social Media as Rights Education Tool for FDHs",
        "summary": (
            "Facebook groups, YouTube channels, and TikTok accounts in "
            "Tagalog and Bahasa Indonesia serve as critical rights "
            "education channels for FDHs in HK. MFMW, FADWU, and "
            "individual advocates produce: know-your-rights videos, "
            "Labour Tribunal procedure guides, agency complaint "
            "templates, and emergency helpline information. Some groups "
            "have 50,000-100,000 members. However, misinformation also "
            "circulates: incorrect legal advice, promotion of unlicensed "
            "agencies, and scam job postings. No government-operated "
            "FDH-focused social media presence in worker languages."
        ),
        "source": "FADWU; MFMW; Migrant Forum in Asia",
    },

    # ── Employer-Worker Mediation ────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Mediation Services for FDH-Employer Disputes",
        "summary": (
            "Labour Department offers free conciliation before formal "
            "Labour Tribunal proceedings. Additional mediation services "
            "available through: (1) Joint Mediation Helpline Office, "
            "(2) Hong Kong Mediation Centre, (3) agency-arranged "
            "mediation (potential conflict of interest). Power imbalance "
            "in mediation favors employers: workers under two-week rule "
            "time pressure, employers can outlast workers financially, "
            "workers lack knowledge of entitlements, and mediated "
            "settlements typically below statutory entitlements (workers "
            "accept 40-70% of full claim to resolve quickly). NGOs "
            "recommend legal advice before accepting mediation outcomes."
        ),
        "source": "Labour Department; Joint Mediation Helpline Office; MFMW",
    },

    # ── Penalty for False Imprisonment ───────────────────────────────────
    {
        "type": "penalty",
        "jurisdiction": "HK",
        "title": "False Imprisonment of FDH — Criminal Penalty",
        "summary": (
            "False imprisonment of FDHs (locking workers in apartments, "
            "physically preventing departure) is a common law offence "
            "in HK punishable by up to 7 years imprisonment on "
            "indictment. In summary proceedings (Magistrates' Court): "
            "up to 2 years imprisonment. Prosecution requires proof "
            "that the worker was totally restrained from leaving. "
            "Actual sentences in FDH cases: 6-18 months typically. "
            "Courts have recognized that combined with assault, wage "
            "theft, and food deprivation, false imprisonment reflects "
            "a pattern of coercive control warranting enhanced sentences."
        ),
        "source": "Common law; Offences Against the Person Ordinance Cap. 212; DCCC records",
    },

    # ── FDH Visa Processing ──────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "HK",
        "title": "FDH Visa Processing Statistics and Employer Screening",
        "summary": (
            "Immigration Department processes approximately 150,000 "
            "FDH-related visa applications annually (new hires and "
            "renewals). Processing time: 4-6 weeks for new applications, "
            "2-4 weeks for renewals. Employer screening includes: "
            "financial means assessment (income of HKD 15,000+/month), "
            "blacklist check, previous FDH employment history. However: "
            "no home inspection conducted, no reference from previous "
            "FDH required, and financial means threshold is minimal. "
            "Refusal rate for employer applications: under 5%. Advocacy "
            "groups argue screening is too permissive and does not "
            "prevent known abusers from hiring new workers."
        ),
        "source": "Immigration Department; MFMW; US TIP Report",
    },

    # ── FDH Financial Literacy ───────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "Financial Literacy and Exploitation Vulnerability of FDHs",
        "summary": (
            "Many FDHs arrive with limited financial literacy, making "
            "them vulnerable to: predatory lending (agency-linked "
            "moneylenders charging 20-40% annual interest), unfavorable "
            "remittance services (3-5% fees vs market rate 1%), "
            "investment scams targeting FDH Sunday gatherings, and "
            "inability to verify wage calculations. Some FDHs accumulate "
            "secondary debt in HK from personal loans to cover agency "
            "fee shortfalls. NGOs provide financial literacy workshops "
            "but reach is limited. Philippine DMW and BNP2MI include "
            "basic financial education in PDOS but content is minimal."
        ),
        "source": "MFMW; Philippine DMW; BNP2MI; Migrant Forum in Asia",
    },

    # ── Sham Marriage and Immigration Fraud ──────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HK",
        "title": "FDH-Related Immigration Fraud and Sham Marriage Cases",
        "summary": (
            "Immigration Department investigates cases where FDHs "
            "enter sham marriages with HK residents to obtain "
            "non-FDH visa status (avoiding two-week rule and live-in "
            "requirement). Syndicate operations charge HKD 50,000-"
            "150,000 for arranged marriages. FDHs who participate face: "
            "criminal prosecution for fraud, deportation, and "
            "immigration ban. Syndicates also exploit FDHs already "
            "in abusive employment by offering marriage as 'escape.' "
            "Prosecutions target FDHs disproportionately; syndicate "
            "organizers harder to convict. Immigration Department "
            "marriage interviews screen for suspicious applications."
        ),
        "source": "Immigration Department (HK); SCMP; HKFP",
    },

    # ── Employment Ordinance Sections Summary ────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Employment Ordinance — Key Sections Applicable to FDHs",
        "summary": (
            "Key Employment Ordinance sections for FDH employment: "
            "s.9 (protection from anti-union dismissal), s.10 (variation "
            "of terms requires consent), s.15 (pregnancy protection), "
            "s.31-31C (rest days), s.39-41A (statutory holidays), "
            "s.41AA-41G (annual leave), s.33 (sickness allowance), "
            "s.53 (employment agency commission limit), s.57-57B "
            "(deductions from wages), s.63-63C (offences: non-payment "
            "of wages), s.70 (unfair dismissal claims). FDHs have "
            "same statutory protections as local employees except: "
            "excluded from Minimum Wage Ordinance and additional "
            "SEC terms supplement (not replace) statutory rights."
        ),
        "source": "Employment Ordinance Cap. 57; Labour Department",
    },

    # ── HKSAR v Leung — Acid Attack Case ────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "HK",
        "title": "HKSAR v Employer — Acid Burn and Torture of Indonesian FDH",
        "summary": (
            "Hong Kong employer convicted of wounding with intent and "
            "assault against Indonesian domestic worker. Worker suffered "
            "chemical burns from cleaning fluid deliberately thrown at "
            "her, cigarette burns, beatings with household implements, "
            "and food deprivation over several months. Employer sentenced "
            "to imprisonment. Case documented by MFMW as part of pattern "
            "of escalating violence: employers begin with verbal abuse, "
            "escalate to physical assault, and progress to methods "
            "causing permanent injury. Case contributed to post-Erwiana "
            "sentencing guidelines recognizing domestic worker abuse as "
            "an aggravating factor."
        ),
        "source": "Hong Kong District Court; MFMW case records; SCMP",
    },

    # ── Wage Receipt Requirements ────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "HK",
        "title": "Wage Receipt and Record-Keeping Requirements for FDH Employers",
        "summary": (
            "Employment Ordinance requires employers to maintain wage "
            "and employment records for all employees including FDHs: "
            "wages paid, deductions made, rest days, holidays, sick "
            "leave taken. Records must be kept for 6 months after "
            "employment ends. However, no mandatory wage receipt signed "
            "by employee is required by statute — practice is voluntary. "
            "This creates evidentiary problems: workers claiming "
            "underpayment cannot point to signed receipts showing "
            "lower amounts. Labour Department recommends but does not "
            "mandate that employers provide monthly pay slips. FDHs "
            "advised to keep their own records."
        ),
        "source": "Employment Ordinance Cap. 57; Labour Department guidance",
    },

    # ── Working Hours Gap ────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "HK",
        "title": "No Maximum Working Hours for FDHs — Legislative Gap",
        "summary": (
            "Hong Kong has no statutory maximum working hours for any "
            "employee (the Standard Working Hours Committee recommended "
            "but government did not legislate). For FDHs, the absence "
            "of working hour limits combined with the live-in requirement "
            "creates conditions for extreme exploitation: workers "
            "reporting 16-21 hour workdays are not in breach of any "
            "HK law. SEC does not specify maximum hours. ILO C189 Art. "
            "10 requires that domestic workers enjoy equal treatment "
            "regarding normal hours of work — but C189 is not ratified "
            "for HK. This gap has been identified by every major NGO "
            "and the US TIP Report as a fundamental structural failure."
        ),
        "source": "Standard Working Hours Committee (HK); ILO C189; FADWU; US TIP Report",
    },

    # ── Filipino Migrant Workers Union ───────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Filipino Migrant Workers' Union (FMWU) — HK Chapter",
        "summary": (
            "FMWU is one of the largest FDH unions in Hong Kong, "
            "representing Filipino domestic workers. Services: labor "
            "rights education, Legal Tribunal accompaniment, collective "
            "advocacy for MAW increases, peer counseling for abuse "
            "victims, and community organizing. Active member of "
            "FADWU alliance. Organizes workshops at Sunday gatherings "
            "in Central district. Membership estimated at 2,000-3,000. "
            "Campaigns include: abolition of two-week rule, equal "
            "minimum wage, and public employer database. Partners with "
            "Migrante International for cross-border advocacy."
        ),
        "source": "FMWU; FADWU; Migrante International",
    },

    # ── Indonesian Migrant Workers Union ─────────────────────────────────
    {
        "type": "contact",
        "jurisdiction": "HK",
        "title": "Indonesian Migrant Workers Union (IMWU) — HK Chapter",
        "summary": (
            "IMWU represents Indonesian domestic workers in Hong Kong. "
            "Focus areas: combating agency overcharging (particularly "
            "severe for Indonesian workers), training center exploitation "
            "in Indonesia, language support for workers with limited "
            "English/Cantonese, and documentation of abuse cases. "
            "Operates Bahasa Indonesia helpline and Sunday drop-in at "
            "Victoria Park (Causeway Bay). Membership: approximately "
            "1,500-2,500. Key advocacy: zero-cost recruitment, "
            "enforcement of agency fee cap, and Indonesian government "
            "bilateral agreements with HK."
        ),
        "source": "IMWU; FADWU; IDWF",
    },
]
