"""Philippine legislation, regulations, and institutional framework for migrant worker protection."""

PH_LEGISLATION_FACTS: list[dict] = [
    # ══════════════════════════════════════════════════════════════════════
    #  MAJOR LEGISLATION
    # ══════════════════════════════════════════════════════════════════════

    # ── RA 8042 — Migrant Workers and Overseas Filipinos Act (1995) ─────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 — Migrant Workers and Overseas Filipinos Act (1995)",
        "summary": (
            "Landmark legislation establishing the state policy on overseas employment. "
            "Declares that the state does not promote overseas employment as a means to "
            "sustain economic growth, and that the existence of the overseas employment "
            "program rests solely on the assurance that the dignity and fundamental rights "
            "of Filipino workers shall not be compromised at any point in the migration cycle."
        ),
        "source": "Official Gazette of the Philippines",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 Sec. 6 — Definition of Illegal Recruitment",
        "summary": (
            "Defines illegal recruitment as any act of canvassing, enlisting, contracting, "
            "transporting, utilizing, hiring, or procuring workers without the proper license "
            "or authority from DOLE or POEA. Includes 13 prohibited practices: charging "
            "excessive fees, contract substitution, withholding documents, publishing false "
            "notices, furnishing false information, inducing workers to quit for re-deployment, "
            "influencing applicants to obtain loans, and imposing compulsory savings. Illegal "
            "recruitment by a syndicate (3+ persons) or in large scale (3+ victims) is "
            "considered economic sabotage with penalty of life imprisonment and PHP 500K-1M fine."
        ),
        "source": "RA 8042 Sec. 6, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 Sec. 7 — Penalties for Illegal Recruitment",
        "summary": (
            "Simple illegal recruitment: 6-12 years imprisonment and PHP 200K-500K fine. "
            "Illegal recruitment constituting economic sabotage (large scale or by syndicate): "
            "life imprisonment and PHP 500K-1M fine. Non-licensee who commits any prohibited "
            "act: 6-12 years and PHP 200K-500K fine."
        ),
        "source": "RA 8042 Sec. 7, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 Sec. 10 — Money Claims",
        "summary": (
            "In case of termination of overseas employment without just, valid, or authorized "
            "cause, the worker is entitled to full reimbursement of placement fee plus "
            "interest at 12% per annum, salaries for the unexpired portion of the contract "
            "or three months for every year of the unexpired term (whichever is less), and "
            "all other benefits. The recruitment/placement agency and employer are jointly "
            "and severally liable."
        ),
        "source": "RA 8042 Sec. 10, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 Sec. 15 — Repatriation of Workers",
        "summary": (
            "Mandates that repatriation of workers in cases of war, epidemic, disasters, "
            "or other similar events shall be the primary responsibility of the agency that "
            "recruited or deployed the worker. If the agency fails, the responsibility falls "
            "on the Overseas Workers Welfare Administration (OWWA). Costs borne by the "
            "principal/employer."
        ),
        "source": "RA 8042 Sec. 15, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 Sec. 16 — Mandatory Remittance",
        "summary": (
            "Requires overseas Filipino workers to remit a portion of their foreign exchange "
            "earnings to their families, dependents, or beneficiaries in the Philippines. "
            "Amount not less than a percentage determined by the BSP (Bangko Sentral ng Pilipinas). "
            "Enforcement has been largely symbolic; compliance is voluntary in practice."
        ),
        "source": "RA 8042 Sec. 16, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 Sec. 23 — Composition of the Migrant Workers Fund",
        "summary": (
            "Establishes the Migrant Workers and Overseas Filipinos Resource Center in countries "
            "where there are large concentrations of Filipino migrant workers. Centers provide "
            "counseling, legal services, welfare assistance, and information on labor and "
            "employment conditions. Staffed by POLO officers and social workers."
        ),
        "source": "RA 8042 Sec. 23, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8042 Sec. 29 — Non-Transferability of License",
        "summary": (
            "Recruitment/manning agency licenses are non-transferable. Transfer, sale, or "
            "conveyance of license to any person shall result in automatic revocation. "
            "Prevents proliferation of paper agencies and shell-company licensing evasion."
        ),
        "source": "RA 8042 Sec. 29, Official Gazette",
    },

    # ── RA 10022 — Amended Migrant Workers Act (2010) ──────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10022 — Amended Migrant Workers and Overseas Filipinos Act (2010)",
        "summary": (
            "Amends RA 8042 to strengthen protections. Key changes: higher penalties for "
            "illegal recruitment, mandatory compulsory insurance for OFWs, deployment only "
            "to countries with existing labor agreements or guarantees of migrant worker "
            "protection, and prohibition of direct hiring except by certain entities."
        ),
        "source": "RA 10022, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10022 Sec. 6(m) — Compulsory Insurance for OFWs",
        "summary": (
            "Mandates that recruitment agencies provide compulsory insurance coverage for "
            "every OFW covering: accidental death, natural death, permanent total disability, "
            "repatriation cost, subsistence allowance during litigation, money claims arising "
            "from employer-employee relationship, compassionate visit, medical evacuation, "
            "and medical repatriation. Minimum benefit of USD 10,000 for death/disability."
        ),
        "source": "RA 10022 Sec. 6(m), Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10022 — Enhanced Penalties for Illegal Recruitment",
        "summary": (
            "Increases penalties: illegal recruitment as economic sabotage punishable by life "
            "imprisonment and fine of not less than PHP 2M but not more than PHP 5M. Simple "
            "illegal recruitment: 12-20 years imprisonment and PHP 1M-2M fine. Significantly "
            "higher than RA 8042 original penalties."
        ),
        "source": "RA 10022, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10022 — Deployment Country Certification Requirement",
        "summary": (
            "Prohibits deployment to countries that do not have existing labor and social "
            "legislation protecting migrant workers, or have not entered into a bilateral "
            "agreement/arrangement with the Philippines. DFA must certify that the host "
            "government has taken positive and concrete measures to protect Filipino workers. "
            "Exception: deployment may proceed upon worker's informed and voluntary consent "
            "if no viable alternative exists."
        ),
        "source": "RA 10022, Official Gazette",
    },

    # ── RA 9208 — Anti-Trafficking in Persons Act (2003) ───────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9208 — Anti-Trafficking in Persons Act (2003)",
        "summary": (
            "Institutes policies to eliminate trafficking in persons. Defines trafficking "
            "as the recruitment, obtaining, hiring, providing, offering, transportation, "
            "transfer, maintaining, harboring, or receipt of persons with or without the "
            "victim's consent by means of threat, force, coercion, abduction, fraud, "
            "deception, abuse of power/position, or taking advantage of vulnerability, "
            "for the purpose of exploitation including forced labor, slavery, servitude, "
            "or removal/sale of organs."
        ),
        "source": "RA 9208, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9208 Sec. 4 — Acts of Trafficking",
        "summary": (
            "Enumerates trafficking acts: (a) recruitment for prostitution or pornography; "
            "(b) introduction of person for prostitution; (c) maintaining a den/dive for "
            "prostitution; (d) economic exploitation through force/coercion/intimidation; "
            "(e) recruitment for forced labor, slavery, or servitude; (f) adoption of persons "
            "for exploitation; (g) recruitment for armed activities. Penalty: 20 years "
            "imprisonment and PHP 1M-2M fine."
        ),
        "source": "RA 9208 Sec. 4, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9208 Sec. 5 — Qualified Trafficking",
        "summary": (
            "Life imprisonment and PHP 2M-5M fine when: victim is a child; committed by "
            "syndicate (3+ persons); offender is ascendant, parent, sibling, guardian, or "
            "person with authority over victim; trafficking is committed in large scale (3+ "
            "victims); offender is member of military/law enforcement; results in death, "
            "insanity, mutilation, or HIV infection."
        ),
        "source": "RA 9208 Sec. 5, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9208 Sec. 7 — Confidentiality of Trafficking Proceedings",
        "summary": (
            "Requires all stages of investigation, rescue, prosecution, and trial to be "
            "conducted with utmost confidentiality. Identity of victims shall not be "
            "disclosed to the media. Court records and proceedings shall be sealed. "
            "Violation of confidentiality is punishable by 6 months-1 year imprisonment "
            "and PHP 50K-100K fine."
        ),
        "source": "RA 9208 Sec. 7, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9208 Sec. 16 — Programs for Trafficked Persons",
        "summary": (
            "Mandates the DSWD and other agencies to implement recovery and reintegration "
            "programs including: emergency shelter, counseling, free legal services, medical "
            "and psychological rehabilitation, skills training, educational assistance, and "
            "livelihood and self-employment assistance. Victims treated as offended parties "
            "and not subjected to criminal prosecution for acts committed as consequence "
            "of being trafficked."
        ),
        "source": "RA 9208 Sec. 16, Official Gazette",
    },

    # ── RA 10364 — Expanded Anti-Trafficking Act (2012) ─────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10364 — Expanded Anti-Trafficking in Persons Act (2012)",
        "summary": (
            "Amends RA 9208 to expand coverage. Adds attempted trafficking as a punishable "
            "offense (15 years imprisonment, PHP 500K-1M fine). Penalizes accomplices and "
            "accessories. Strengthens IACAT mandate. Creates anti-trafficking database and "
            "inter-agency cooperation protocols."
        ),
        "source": "RA 10364, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10364 — Strengthened IACAT Mandate",
        "summary": (
            "Expands the Inter-Agency Council Against Trafficking (IACAT) composition and "
            "powers. IACAT formulates national action plan against trafficking, monitors "
            "implementation, coordinates interagency efforts, and establishes anti-trafficking "
            "task forces. Chaired by DOJ Secretary with DSWD Secretary as co-chair. "
            "Members include DFA, DOLE, POEA (now DMW), NBI, PNP, DILG, and NGO representatives."
        ),
        "source": "RA 10364, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10364 — Witness Protection for Trafficking Cases",
        "summary": (
            "Trafficking victims and witnesses automatically covered by the Witness Protection "
            "Program (RA 6981). Witnesses may be provided secure housing, livelihood assistance, "
            "and change of identity documents. No trafficking case may be dismissed solely on "
            "the ground of the desistance of the complainant or failure of victim to testify."
        ),
        "source": "RA 10364, Official Gazette",
    },

    # ── RA 11862 — Further Expanded Anti-Trafficking Act (2022) ─────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11862 — Expanded Anti-Trafficking in Persons Act (2022)",
        "summary": (
            "Further amends RA 9208 and RA 10364. Adds online sexual exploitation of "
            "children (OSAEC) as a form of trafficking. Covers trafficking committed through "
            "digital means, including social media platforms and messaging applications. "
            "Introduces financial investigation provisions to trace trafficking proceeds. "
            "Strengthens asset forfeiture and anti-money laundering coordination."
        ),
        "source": "RA 11862, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11862 — Digital Trafficking Provisions",
        "summary": (
            "Specifically criminalizes trafficking committed using information and "
            "communications technology. Covers online sexual exploitation, livestreaming "
            "of abuse, and digital recruitment for forced labor. Internet service providers "
            "and platforms required to cooperate with law enforcement in removing "
            "trafficking-related content. DICT and NBI Anti-Cybercrime Group coordinate "
            "digital enforcement."
        ),
        "source": "RA 11862, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11862 — Financial Investigation Provisions",
        "summary": (
            "Mandates AMLC (Anti-Money Laundering Council) coordination with IACAT. "
            "Trafficking proceeds considered as unlawful activity under AMLA. Enables "
            "freezing of assets linked to trafficking within 24 hours upon court order. "
            "Forfeited assets channeled to trafficking survivors' fund."
        ),
        "source": "RA 11862, Official Gazette",
    },

    # ── RA 11641 — DMW Act (2021) ──────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11641 — Department of Migrant Workers Act (2021)",
        "summary": (
            "Creates the Department of Migrant Workers (DMW) as the primary policy, "
            "regulatory, and adjudicatory government body for overseas employment and "
            "migrant worker affairs. Absorbs the Philippine Overseas Employment Administration "
            "(POEA), overseas operations of OWWA, and migrant worker functions of DOLE. "
            "DMW Secretary is a cabinet-level position. Signed February 2022, operationalized "
            "in phases through 2023."
        ),
        "source": "RA 11641, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11641 — DMW Powers and Functions",
        "summary": (
            "DMW functions include: regulation of private recruitment agencies, processing "
            "and verification of employment contracts, adjudication of recruitment violation "
            "complaints, pre-departure orientation, assistance to OFWs in distress, "
            "repatriation assistance, anti-illegal recruitment enforcement, and formulation "
            "of deployment policies. Maintains the One-Stop Service Centers for OFWs."
        ),
        "source": "RA 11641, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11641 — Transition from POEA to DMW",
        "summary": (
            "All functions, powers, assets, records, equipment, and personnel of POEA "
            "transferred to DMW. POEA ceased to exist as a separate agency. Existing POEA "
            "rules and regulations remain in effect until superseded by DMW issuances. "
            "Licensed recruitment agencies continue under existing licenses until renewal "
            "cycle under DMW."
        ),
        "source": "RA 11641, Official Gazette",
    },

    # ── RA 8239 — Philippine Passport Act ──────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8239 — Philippine Passport Act (1996)",
        "summary": (
            "Governs the issuance and cancellation of Philippine passports. Prohibits "
            "confiscation of passports by any person, employer, or agency. Section 12 "
            "penalizes tampering, falsification, and unauthorized possession of another "
            "person's passport with 6-12 years imprisonment. Passport remains the property "
            "of the Philippine government."
        ),
        "source": "RA 8239, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 8239 — Passport Confiscation Prohibition",
        "summary": (
            "Section 4 in relation to DFA Department Order No. 37-03 prohibits any person, "
            "employer, or recruitment agency from confiscating or withholding a Filipino "
            "worker's passport. Employers who confiscate passports may be charged with "
            "violation of RA 8239 (unauthorized possession of government-issued document) "
            "and potentially RA 9208 (trafficking, if for exploitative purpose). POLOs "
            "assist workers in passport recovery."
        ),
        "source": "RA 8239 / DFA DO 37-03",
    },

    # ── RA 7610 — Protection of Children ───────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 7610 — Special Protection of Children Against Abuse, Exploitation (1992)",
        "summary": (
            "Provides special protection against child abuse, exploitation, and "
            "discrimination. Section 12 prohibits employment of children below 15 years, "
            "and below 18 in hazardous work. Sections 5-6 penalize child trafficking and "
            "prostitution with reclusion temporal to reclusion perpetua. Applies to Filipino "
            "children trafficked domestically or abroad."
        ),
        "source": "RA 7610, Official Gazette",
    },

    # ── RA 9262 — Anti-VAWC Act ────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9262 — Anti-Violence Against Women and Their Children Act (2004)",
        "summary": (
            "Defines and criminalizes violence against women and children including "
            "physical, sexual, psychological, and economic abuse. Economic abuse includes "
            "depriving or threatening to deprive a woman of financial resources, controlling "
            "finances, and destroying household property. Used in conjunction with RA 9208 "
            "when trafficking involves domestic violence. Provides for protection orders."
        ),
        "source": "RA 9262, Official Gazette",
    },

    # ── Labor Code — Overseas Employment ───────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "Labor Code Book I Title II — Recruitment and Placement of Workers",
        "summary": (
            "Articles 13-39 of the Labor Code (PD 442) govern recruitment and placement. "
            "Art. 18 prohibits direct hiring by employers of Filipino workers for overseas "
            "employment (except members of diplomatic corps and international organizations). "
            "Art. 25 sets requirements for obtaining a recruitment license. Art. 34 lists 13 "
            "prohibited practices. Art. 38 imposes penalties for illegal recruitment."
        ),
        "source": "Presidential Decree 442 (Labor Code), as amended",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "Labor Code Art. 34 — Prohibited Practices in Recruitment",
        "summary": (
            "Lists 13 prohibited practices: (a) charging fees greater than prescribed; "
            "(b) furnishing false notice or information; (c) giving false information to "
            "the DOLE Secretary; (d) inducing workers to quit employment for redeployment; "
            "(e) influencing workers to obtain loans with excessive interest; (f) engaging "
            "in recruitment without proper license; (g) failing to reimburse fees when "
            "deployment fails; (h) contract substitution; (i) withholding worker documents."
        ),
        "source": "PD 442 Art. 34, as amended",
    },

    # ── Executive Orders on Migration ──────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "Executive Order 247 (1995) — Reorganization of POEA",
        "summary": (
            "Reorganized the Philippine Overseas Employment Administration to align with "
            "RA 8042. Consolidated regulation, adjudication, and worker assistance functions. "
            "Established the POEA Governing Board. Created the Adjudication Branch for "
            "expeditious resolution of recruitment violation cases."
        ),
        "source": "EO 247 (1995), Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "Executive Order 1022 (1985) / EO 226 (1995) — OWWA Reorganization",
        "summary": (
            "Established and reorganized OWWA to provide welfare services to OFWs and "
            "their families. OWWA functions include: skills training, scholarship programs, "
            "repatriation assistance, insurance, death and disability benefits, loan programs, "
            "and pre-departure orientation. Funded by mandatory USD 25 membership fee per "
            "deployment contract."
        ),
        "source": "EO 1022 / EO 226, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "Executive Order 203 (2016) — Inter-Agency Council Against Trafficking",
        "summary": (
            "Reconstituted and strengthened IACAT. Added new member agencies including "
            "the Cybercrime Investigation and Coordination Center (CICC), National Prosecution "
            "Service, and CSO representatives. Directed the establishment of anti-trafficking "
            "task forces at local government level."
        ),
        "source": "EO 203 (2016), Official Gazette",
    },

    # ── DOLE Department Orders ─────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DOLE DO 174 Series of 2017 — Rules on Contracting and Subcontracting",
        "summary": (
            "Prohibits labor-only contracting. Defines legitimate contracting arrangements. "
            "Requires contractors to be registered with DOLE. Protects workers from "
            "exploitative subcontracting arrangements that evade employer-employee "
            "relationship obligations. Relevant to OFW supply chain exploitation."
        ),
        "source": "DOLE Department Order 174-17",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POEA Memorandum Circular 04-2019 — Placement Fee Cap",
        "summary": (
            "Reiterates that placement fees for overseas workers shall not exceed one month's "
            "basic salary as specified in the employment contract. Any fees in excess are "
            "considered overcharging and constitute illegal recruitment. Agency must provide "
            "official receipt for all fees collected."
        ),
        "source": "POEA MC 04-2019",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW Department Circular 01-2023 — Updated Licensing Requirements",
        "summary": (
            "Sets new requirements for land-based and sea-based recruitment agencies under "
            "DMW. Minimum capitalization: PHP 5M for land-based, PHP 7.5M for manning. "
            "Cash bond: PHP 1M (land-based), PHP 1.5M (manning). Surety bond: PHP 100K "
            "per worker (land-based). Annual license renewal with compliance review."
        ),
        "source": "DMW DC 01-2023",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW Department Circular 02-2023 — Anti-Illegal Recruitment Enforcement",
        "summary": (
            "Establishes DMW Anti-Illegal Recruitment Branch operations. Provides for "
            "entrapment operations against illegal recruiters. Coordinates with NBI, PNP, "
            "and IACAT. Mandates that all POLOs report illegal recruitment patterns in host "
            "countries back to DMW for enforcement action in the Philippines."
        ),
        "source": "DMW DC 02-2023",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POEA Rules on Overseas Employment (2016, as amended)",
        "summary": (
            "Comprehensive rules governing: processing of overseas employment contracts, "
            "accreditation of foreign employers, worker documentation requirements, PDOS "
            "and PEOS attendance, medical examination protocols, deployment restrictions, "
            "and administrative sanctions for erring agencies. Replaced by DMW issuances "
            "but remain operative where DMW has not yet promulgated replacement rules."
        ),
        "source": "POEA 2016 Revised Rules / DMW",
    },

    # ══════════════════════════════════════════════════════════════════════
    #  INSTITUTIONAL FRAMEWORK
    # ══════════════════════════════════════════════════════════════════════

    # ── Department of Migrant Workers (DMW) ────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW Organizational Structure",
        "summary": (
            "DMW is headed by a Secretary with 4 Undersecretaries (Policy and International "
            "Cooperation, Overseas Employment, Migrant Workers Affairs, Management) and "
            "8 Assistant Secretaries. Major offices: Overseas Employment Policy Board, "
            "National Maritime Polytechnic, Anti-Illegal Recruitment Branch, One-Stop Service "
            "Centers (25+ nationwide), and Philippine Overseas Labor Offices (36+ worldwide)."
        ),
        "source": "RA 11641 / DMW official structure",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW Adjudication Branch — Recruitment Violation Cases",
        "summary": (
            "Inherited from POEA. Hears and decides cases involving recruitment violations, "
            "disciplinary actions against agencies, and money claims of OFWs against agencies. "
            "Compulsory arbitration. Decisions appealable to NLRC. Average case resolution "
            "time: 6-12 months. Significant backlog of 5,000+ pending cases."
        ),
        "source": "DMW / former POEA Adjudication Branch",
    },

    # ── OWWA ───────────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "OWWA — Overseas Workers Welfare Administration",
        "summary": (
            "Attached agency of DMW providing welfare services to OFWs. Membership mandatory "
            "for all land-based and sea-based OFWs. Membership fee: USD 25 per contract, "
            "valid for 2 years. Fund used for: repatriation, death and disability benefits, "
            "education and training, insurance, and social services. OWWA fund assets: "
            "approximately PHP 200 billion (2023)."
        ),
        "source": "EO 247 / RA 11641 / OWWA",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "OWWA Programs and Benefits",
        "summary": (
            "Key programs: (1) Repatriation Assistance — free transport and airport assistance; "
            "(2) Death Benefits — PHP 200K to beneficiaries; (3) Disability Benefits — PHP 100K-200K; "
            "(4) EDSP (Education and Training) — skills training, scholarship, TESDA partnership; "
            "(5) OFW Enterprise Development — PHP 50K-100K start-up capital loans; "
            "(6) Balik-Pinas Balik-Hanapbuhay — livelihood for repatriated OFWs; "
            "(7) DOLE-AKAP — financial assistance during emergencies (COVID, war, disaster)."
        ),
        "source": "OWWA Annual Report / DMW",
    },

    # ── IACAT ──────────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "IACAT — Inter-Agency Council Against Trafficking",
        "summary": (
            "Created by RA 9208, strengthened by RA 10364 and EO 203. Chaired by DOJ "
            "Secretary, co-chaired by DSWD Secretary. 13 member agencies including DFA, "
            "DMW, NBI, PNP, DILG, POEA (now DMW), DOLE, CFO. Functions: formulate NAP, "
            "coordinate interagency efforts, monitor compliance, manage trafficking database, "
            "conduct capacity building for law enforcement and prosecutors."
        ),
        "source": "RA 9208 / RA 10364 / IACAT",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "IACAT Task Forces and Regional Committees",
        "summary": (
            "IACAT operates through: (1) National Task Force — law enforcement operations, "
            "rescue missions, intelligence; (2) Regional Anti-Trafficking Committees in all "
            "17 regions; (3) Local Anti-Trafficking Committees in provinces and cities. "
            "Task forces conduct surveillance, entrapment operations, and victim rescue. "
            "International coordination through ASEAN-ACTIP and bilateral MOUs with "
            "destination countries."
        ),
        "source": "IACAT / DOJ",
    },

    # ── POLOs ──────────────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Philippine Overseas Labor Offices (POLOs) — Global Network",
        "summary": (
            "DMW maintains 36+ POLOs across 28 countries. Key locations: Riyadh, Jeddah, "
            "Al-Khobar (Saudi Arabia); Abu Dhabi, Dubai (UAE); Doha (Qatar); Kuwait City; "
            "Hong Kong; Singapore; Taipei; Seoul; Tokyo; Osaka; Kuala Lumpur; Manama; "
            "Amman; Beirut; Tel Aviv; Rome; London; Washington DC; New York; Ottawa. "
            "Functions: contract verification, complaint resolution, case assistance, "
            "employer accreditation, anti-trafficking coordination with host government."
        ),
        "source": "DMW / POLO directory",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POLO Functions — Frontline OFW Protection Abroad",
        "summary": (
            "Each POLO handles: (1) verification and authentication of employment contracts "
            "before deployment; (2) assistance to workers with employer disputes; (3) rescue "
            "of distressed workers; (4) repatriation coordination; (5) conciliation/mediation "
            "of labor cases; (6) monitoring of working and living conditions; (7) cooperation "
            "with host country labor authorities on enforcement; (8) monthly reporting to "
            "DMW on case data and trends."
        ),
        "source": "DMW / POLO mandate",
    },

    # ── One-Stop Service Centers ───────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "One-Stop Service Centers for OFWs",
        "summary": (
            "DMW operates 25+ One-Stop Service Centers nationwide (main: Manila, Cebu, "
            "Davao, Cagayan de Oro, Pampanga). Centers co-locate DMW, OWWA, DFA-OCA, "
            "POEA adjudication, NBI clearance, Pag-IBIG, PhilHealth, SSS, and private "
            "insurance under one roof. Workers complete all pre-departure requirements "
            "in a single visit. Average processing time reduced from 3-5 days to 1 day."
        ),
        "source": "DMW / One-Stop Service Centers",
    },

    # ── Assistance-to-Nationals Fund ───────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Assistance-to-Nationals Fund (ATN Fund)",
        "summary": (
            "Managed by DFA for emergency assistance to Filipinos in distress abroad. "
            "Covers: repatriation costs, legal assistance, emergency shelter, medical "
            "treatment, and subsistence allowance. Annual budget: approximately PHP 1 billion. "
            "Disbursed through Philippine embassies and consulates. Complements OWWA "
            "assistance for non-OFW Filipinos abroad."
        ),
        "source": "DFA / ATN Fund annual report",
    },

    # ── Migrant Workers Resource Centers ───────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Migrant Workers and Overseas Filipinos Resource Centers (MWOFRCs)",
        "summary": (
            "Mandated by RA 8042 Sec. 19. Established in countries with at least 20,000 "
            "Filipino workers. Provide: counseling and legal services, welfare assistance, "
            "information on labor and employment conditions, registration services, "
            "and gender-responsive programs. Staffed by DMW, OWWA, and DFA officers. "
            "Currently operational in Saudi Arabia, UAE, Kuwait, Hong Kong, and Singapore."
        ),
        "source": "RA 8042 Sec. 19 / DMW",
    },

    # ── Repatriation Assistance Program ────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "National Reintegration Center for OFWs (NRCO)",
        "summary": (
            "Under DMW. Provides reintegration services for returning OFWs: psychosocial "
            "support, skills assessment and training, livelihood assistance, cooperative "
            "development, and financial literacy programs. OFW Reintegration through Skills "
            "and Entrepreneurship (OFW RISE) program provides PHP 20K-100K capital assistance. "
            "Sa Pinas program for distressed returnees."
        ),
        "source": "DMW / NRCO",
    },

    # ── Legal Assistance Fund ──────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Legal Assistance Fund (LAF) for Migrant Workers",
        "summary": (
            "Mandated by RA 8042 as amended. Provides free legal representation to OFWs "
            "in both Philippine and foreign courts/tribunals. Covers: illegal recruitment "
            "cases, labor disputes, criminal cases where OFW is victim, trafficking cases. "
            "Administered by DMW. Budget: PHP 100 million annually. Augmented by "
            "Assistance-to-Nationals Fund for overseas litigation."
        ),
        "source": "RA 8042 / RA 10022 / DMW",
    },

    # ── Anti-Illegal Recruitment Branch ────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW Anti-Illegal Recruitment Branch (AIRB)",
        "summary": (
            "Specialized enforcement unit under DMW. Conducts surveillance and intelligence "
            "gathering on suspected illegal recruiters. Performs entrapment operations in "
            "coordination with NBI and PNP. Processes complaints and builds cases for "
            "prosecution. Maintains registry of suspended and revoked agencies. Coordinates "
            "with IACAT on trafficking-related illegal recruitment cases."
        ),
        "source": "DMW / AIRB",
    },

    # ══════════════════════════════════════════════════════════════════════
    #  RECRUITMENT REGULATION
    # ══════════════════════════════════════════════════════════════════════

    # ── Licensing Requirements ─────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW Licensing Requirements for Recruitment Agencies",
        "summary": (
            "Land-based agencies require: PHP 5M minimum capitalization, PHP 1M cash bond "
            "deposited with DMW, surety bond of PHP 100K per worker, minimum 200 sqm office "
            "space, compliance with POEA/DMW rules. License valid for 4 years, renewable. "
            "Manning (sea-based) agencies require PHP 7.5M capitalization, PHP 1.5M cash bond. "
            "Total licensed agencies: approximately 1,200 land-based, 400 manning (2023)."
        ),
        "source": "POEA Rules / DMW DC 01-2023",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Manning Agency Regulation (Sea-Based Workers)",
        "summary": (
            "Filipino seafarers constitute one of the world's largest seafarer populations "
            "(approximately 400,000 deployed annually). Manning agencies must be licensed by "
            "DMW and accredited by MARINA (Maritime Industry Authority). Strict compliance "
            "with MLC 2006 (Maritime Labour Convention). Standard Employment Contract for "
            "seafarers mandated by POEA. Manning agencies must maintain escrow funds for "
            "unpaid wages in case of vessel abandonment."
        ),
        "source": "POEA Rules / DMW / MARINA",
    },

    # ── Placement Fee Cap ──────────────────────────────────────────────
    {
        "type": "fee_cap",
        "jurisdiction": "PH",
        "title": "Philippine Placement Fee Cap — One Month Salary Rule",
        "summary": (
            "POEA/DMW rules cap placement fees at one month's basic salary as specified "
            "in the POEA-approved employment contract. For domestic workers deployed to "
            "countries with bilateral agreements (e.g., Saudi Arabia, Kuwait): zero placement "
            "fee to the worker (employer-pays). Agencies caught overcharging face suspension "
            "or revocation of license and criminal prosecution for illegal recruitment."
        ),
        "source": "POEA MC 04-2019 / RA 8042 / RA 10022",
    },

    # ── Prohibited Recruitment Practices ───────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "13 Prohibited Recruitment Practices under Philippine Law",
        "summary": (
            "(1) Charging fees exceeding prescribed amount; (2) furnishing false notice, "
            "information, or document to DOLE/DMW; (3) giving false information/documents "
            "to a recruited worker; (4) inducing workers to quit employment for redeployment; "
            "(5) influencing workers to obtain loans at excessive interest; (6) engaging in "
            "recruitment without license; (7) failing to reimburse worker upon non-deployment; "
            "(8) contract substitution; (9) withholding travel documents; (10) failing to "
            "actually deploy the worker without valid reason; (11) charging fees for services "
            "normally furnished by the SSS/OWWA/POEA; (12) recruitment by a syndicate; "
            "(13) recruitment in large scale."
        ),
        "source": "RA 8042 Sec. 6 / Labor Code Art. 34",
    },

    # ── PDOS and PEOS ──────────────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "PDOS — Pre-Departure Orientation Seminar",
        "summary": (
            "Mandatory for all OFWs before deployment. Conducted by OWWA-accredited PDOS "
            "providers (NGOs, training centers). Covers: employment contract provisions, "
            "country of destination (laws, culture, climate), airport procedures, health "
            "and safety, financial literacy, and available government services. Duration: "
            "6-8 hours. Certificate required for OEC (Overseas Employment Certificate) "
            "issuance. Over 2 million workers attend annually."
        ),
        "source": "OWWA / DMW PDOS guidelines",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "PEOS — Pre-Employment Orientation Seminar",
        "summary": (
            "Free seminar for prospective OFWs BEFORE they engage a recruitment agency. "
            "Covers: risks of overseas employment, rights and obligations, legal processes, "
            "how to verify agency legitimacy, warning signs of illegal recruitment, and "
            "available government services. Offered by DMW One-Stop Centers and partner "
            "LGUs. Aims to prevent recruitment fraud at the earliest stage."
        ),
        "source": "DMW / PEOS program",
    },

    # ── Country Team Approach ──────────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Country Team Approach for OFW Protection",
        "summary": (
            "Philippine diplomatic missions use the Country Team Approach: Ambassador "
            "leads a coordinated team of POLO, OWWA, DFA consular officers, and when "
            "available, ATN officers and social workers. Monthly Country Team meetings "
            "review OFW case data, deployment trends, and policy issues. Approach ensures "
            "unified response to major incidents (mass termination, repatriation, abuse cases)."
        ),
        "source": "DFA / DMW Country Team framework",
    },

    # ── Bilateral Labor Agreements ─────────────────────────────────────
    {
        "type": "bilateral_agreement",
        "jurisdiction": "PH",
        "title": "Philippine Bilateral Labor Agreements — Complete List",
        "summary": (
            "Philippines has bilateral labor agreements or MOUs with 20+ countries: "
            "Saudi Arabia (2017), UAE (2017), Kuwait (2018 reformed), Qatar, Bahrain, "
            "Oman, Jordan, Lebanon, Israel, South Korea (EPS), Japan (JPEPA, TITP, SSW), "
            "Taiwan (MECO-TECO), Hong Kong (standard contract), Singapore, Canada "
            "(seasonal agricultural), UK (NHS recruitment), Germany (Triple Win), "
            "Papua New Guinea, Palau, Northern Mariana Islands, Libya (pre-2011), Iraq "
            "(Kurdistan region). Agreements cover contract verification, worker protection, "
            "dispute resolution, and in some cases employer-pays recruitment."
        ),
        "source": "DMW / DFA bilateral agreement registry",
    },

    # ── Deployment Bans ────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "Philippine Deployment Bans — Historical Record",
        "summary": (
            "Major deployment bans: Lebanon (2006, 2014-2018 partial), Saudi Arabia "
            "(2011 domestic workers, temporary), Syria (2011 onwards, ongoing), Libya "
            "(2011 onwards, ongoing), Iraq (2003-2005, partial lift), Yemen (2015 onwards), "
            "Kuwait (2018 total ban after OFW murder, lifted after bilateral agreement reform), "
            "Afghanistan (2021 evacuation), Qatar (2011 temporary over abuse cases, quickly "
            "lifted), Jordan (2012 temporary). Bans imposed by POEA/DMW upon recommendation "
            "of DFA when security situation or worker protection concerns warrant."
        ),
        "source": "POEA / DMW deployment advisory records",
    },
    {
        "type": "advisory",
        "jurisdiction": "PH",
        "title": "Kuwait Deployment Ban and Reform (2018)",
        "summary": (
            "Total deployment ban to Kuwait imposed in February 2018 following the death of "
            "OFW Joanna Demafelis, found dead in a freezer. Ban lasted until May 2018 when "
            "Philippines and Kuwait signed a new bilateral labor agreement with reforms: "
            "workers keep their own passports, workers have the right to keep personal phone, "
            "workers provided food and suitable housing, employers cannot reassign workers to "
            "another employer, Philippine embassy given access to shelters. The agreement "
            "was a landmark in Philippine bilateral labor protection."
        ),
        "source": "DMW / DFA / Kuwait bilateral agreement 2018",
    },

    # ── Direct Hiring and Name Hire ────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Direct Hiring Prohibition and Exceptions",
        "summary": (
            "Labor Code Art. 18 and POEA/DMW rules prohibit direct hiring of Filipino "
            "workers for overseas employment. Exceptions: (1) members of the diplomatic "
            "corps; (2) international organizations; (3) professionals and skilled workers "
            "with duly executed, government-verified contracts; (4) name-hire (worker "
            "specifically requested by a foreign employer by name, not through an agency). "
            "Direct hiring bypasses agency protections, so exceptions are narrowly construed."
        ),
        "source": "Labor Code Art. 18 / POEA Rules Part III",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Name Hire Processing under DMW",
        "summary": (
            "Name hire: foreign employer directly requests a specific worker by name. "
            "Worker applies directly at DMW with verified employment contract. DMW processes "
            "the name hire application, verifies employer legitimacy and contract terms. "
            "No recruitment agency involvement. Worker pays no placement fee. Processing "
            "time: 3-5 working days. Safeguards: DMW contract verification, PDOS attendance, "
            "OEC issuance. Accounts for approximately 5-10% of new hires."
        ),
        "source": "DMW / POEA Name Hire guidelines",
    },

    # ══════════════════════════════════════════════════════════════════════
    #  ENFORCEMENT AND DATA
    # ══════════════════════════════════════════════════════════════════════

    # ── Deployment Statistics ──────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Annual OFW Deployment Volume",
        "metric": "New hires and rehires deployed per year",
        "value": "2.33 million (2023)",
        "year": 2023,
        "details": (
            "2023 deployment: approximately 2.33 million (new hires + rehires). Land-based: "
            "1.57 million. Sea-based: 530,000. Recovered from COVID low of 550,000 (2020). "
            "Pre-COVID average: 2.0-2.3 million per year. Historical peak: 2.33 million (2019). "
            "New hires approximately 30% of total; rehires 70%."
        ),
        "source": "DMW / PSA Survey on Overseas Filipinos",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OFW Stock Estimate — Filipinos Abroad",
        "metric": "Total Filipino workers abroad at any time",
        "value": "10.2 million (2023 estimate)",
        "year": 2023,
        "details": (
            "Estimated 10.2 million OFWs deployed worldwide at any given time. Approximately "
            "55% are permanent migrants/immigrants and 45% are temporary contract workers. "
            "Largest populations: Saudi Arabia (~1.5M), UAE (~700K), US (workers, not immigrants, "
            "~600K), Hong Kong (~200K), Singapore (~200K), Kuwait (~240K), Qatar (~270K), "
            "Japan (~300K), South Korea (~60K), Taiwan (~160K). Commission on Filipinos "
            "Overseas (CFO) estimates total Filipino diaspora at 12+ million."
        ),
        "source": "CFO / DMW / PSA",
    },

    # ── Top Destination Countries ──────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Top Destination Countries for Filipino Workers (2023)",
        "metric": "New hires by destination",
        "value": "Saudi Arabia, UAE, Kuwait, Hong Kong, Singapore, Qatar, Taiwan, Japan, Bahrain, Oman",
        "year": 2023,
        "details": (
            "Top 10 destinations by new hire deployment (2023): (1) Saudi Arabia — 28%; "
            "(2) UAE — 12%; (3) Kuwait — 10%; (4) Hong Kong — 9%; (5) Singapore — 7%; "
            "(6) Qatar — 6%; (7) Taiwan — 5%; (8) Japan — 5%; (9) Bahrain — 3%; "
            "(10) Oman — 3%. Gulf Cooperation Council (GCC) countries account for approximately "
            "60% of total land-based deployment. East Asian destinations growing rapidly."
        ),
        "source": "DMW deployment statistics 2023",
    },

    # ── Remittance Data ────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OFW Remittances to the Philippines",
        "metric": "Total personal remittances from OFWs",
        "value": "USD 37.2 billion (2023)",
        "year": 2023,
        "details": (
            "Personal remittances reached USD 37.2 billion in 2023, up from USD 36.1B "
            "(2022) and USD 34.9B (2021). Constitutes approximately 8-9% of Philippine GDP. "
            "Top remittance sources: US (35%), Saudi Arabia (13%), UAE (8%), Singapore (5%), "
            "Japan (5%), UK (4%), Hong Kong (4%), Qatar (3%). Philippines is the 4th largest "
            "remittance recipient globally after India, Mexico, and China."
        ),
        "source": "BSP (Bangko Sentral ng Pilipinas) / World Bank",
    },

    # ── Agency Enforcement Data ────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Recruitment Agency Suspension and Closure Data",
        "metric": "Agencies suspended, canceled, or revoked per year",
        "value": "~80-120 adverse actions per year",
        "year": 2023,
        "details": (
            "DMW/POEA annual adverse actions against agencies: approximately 80-120 per year "
            "including suspensions (30-50), cancellations (15-25), and preventive suspensions "
            "(30-40). Common violations: overcharging, non-deployment, contract substitution, "
            "and deploying to non-accredited employers. Total licensed agencies: ~1,600. "
            "Adverse action rate: approximately 5-7% of licensed agencies per year."
        ),
        "source": "DMW / POEA annual report",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Illegal Recruitment Case Filing and Prosecution",
        "metric": "Illegal recruitment cases filed and resolved",
        "value": "~300-500 cases filed per year",
        "year": 2023,
        "details": (
            "Approximately 300-500 illegal recruitment cases filed annually (NBI + PNP + DMW "
            "referrals). Conviction rate: approximately 30-40% of cases that reach trial. "
            "Many cases dismissed due to complainant desistance, settlement, or evidentiary "
            "issues. Average case duration: 2-5 years in trial courts. Large-scale illegal "
            "recruitment cases (economic sabotage): approximately 30-50 filed per year. "
            "NBI Anti-Human Trafficking Division handles trafficking-related recruitment cases."
        ),
        "source": "DOJ / NBI / DMW prosecution data",
    },

    # ── IACAT Conviction Data ──────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "IACAT Trafficking Conviction Data",
        "metric": "Trafficking convictions per year",
        "value": "40-70 convictions per year (2019-2023)",
        "year": 2023,
        "details": (
            "IACAT reports approximately 40-70 trafficking convictions per year (2019-2023). "
            "Total convictions since RA 9208 enactment (2003-2023): approximately 500+. "
            "Cases pending at trial courts: approximately 1,200 at any given time. Average "
            "trial duration: 3-7 years. Conviction rate for cases reaching trial: approximately "
            "70%. US TIP Report (2023) ranked Philippines as Tier 1 — fully meeting minimum "
            "standards for trafficking elimination."
        ),
        "source": "IACAT / DOJ / US TIP Report 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Philippines TIP Tier Rating History",
        "metric": "US Trafficking in Persons Report tier ranking",
        "value": "Tier 1 (2023-2024)",
        "year": 2024,
        "details": (
            "Philippines TIP tier history: Tier 2 (2001-2005), Tier 2 Watch List (2004 briefly), "
            "Tier 2 (2005-2015), Tier 1 (2016-2024). Achieving and maintaining Tier 1 "
            "reflects significant prosecutorial effort, victim services, and prevention "
            "programs. Philippines is one of only 2 ASEAN countries at Tier 1 (alongside "
            "Singapore in some years). Key factors: strong anti-trafficking legal framework, "
            "IACAT coordination, and high conviction rate."
        ),
        "source": "US State Department TIP Report",
    },

    # ── Hotline Data ───────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "1343 Action Line — Anti-Trafficking Hotline Data",
        "metric": "Calls and tips received via 1343 hotline",
        "value": "~15,000-20,000 calls per year",
        "year": 2023,
        "details": (
            "IACAT 1343 Action Line receives approximately 15,000-20,000 calls per year. "
            "Types: trafficking reports (~20%), illegal recruitment reports (~35%), requests "
            "for assistance (~25%), information inquiries (~20%). Referrals to law enforcement "
            "for investigation: approximately 1,500-2,500 per year. Hotline operates 24/7. "
            "Multi-agency response: NBI, PNP, DSWD rescue teams."
        ),
        "source": "IACAT / 1343 Action Line annual report",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "7166 DMW Hotline — OFW Assistance Data",
        "metric": "OFW assistance calls via DMW 8722-1144/1155",
        "value": "~50,000 calls per year",
        "year": 2023,
        "details": (
            "DMW complaint and action center receives approximately 50,000 calls/contacts "
            "per year. Types: contract verification inquiries (~30%), complaint against "
            "recruitment agencies (~20%), distress calls from OFWs abroad (~15%), illegal "
            "recruitment reports (~10%), information on deployment requirements (~25%). "
            "DMW also operates online complaint portal at dmw.gov.ph."
        ),
        "source": "DMW Action Center",
    },

    # ── NLRC Case Data ─────────────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "NLRC-DOLE OFW Labor Cases",
        "metric": "OFW-related cases filed at NLRC",
        "value": "~5,000-8,000 per year",
        "year": 2023,
        "details": (
            "National Labor Relations Commission receives approximately 5,000-8,000 "
            "OFW-related cases per year. Types: money claims for unpaid wages (~40%), "
            "illegal termination (~25%), recruitment violation appeals (~15%), death/disability "
            "benefits (~10%), other (~10%). Average resolution time: 6-18 months. Cases "
            "involving joint and several liability of agency and employer constitute majority. "
            "Special OFW sections at NLRC main office and regional offices."
        ),
        "source": "NLRC / DOLE annual report",
    },

    # ── Embassy Case Assistance ────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Philippine Embassy/POLO Case Assistance Volume",
        "metric": "OFW cases handled by embassies and POLOs",
        "value": "~25,000-35,000 cases per year",
        "year": 2023,
        "details": (
            "Philippine embassies, consulates, and POLOs handle approximately 25,000-35,000 "
            "OFW distress and assistance cases per year. Case types: labor disputes (~30%), "
            "maltreatment/abuse (~15%), unpaid wages (~15%), contract violations (~12%), "
            "runaway workers (~10%), repatriation (~8%), death cases (~3%), trafficking "
            "rescue (~2%), other (~5%). Highest caseload: Saudi Arabia (Riyadh, Jeddah, "
            "Al-Khobar) collectively handling ~10,000 cases per year."
        ),
        "source": "DFA / DMW / POLO case data",
    },

    # ── Repatriation Statistics ────────────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OFW Repatriation Statistics by Year",
        "metric": "Emergency and distress repatriations per year",
        "value": "~5,000-15,000 distress repatriations per year (non-COVID)",
        "year": 2023,
        "details": (
            "Normal year distress repatriations: approximately 5,000-15,000. COVID-19 "
            "repatriation (2020-2021): over 500,000 OFWs repatriated. Major repatriation "
            "events: Lebanon war (2006: 30,000+), Libya crisis (2011: 13,000+), Syria "
            "(2011-2012: 3,000+), Kuwait mass termination (2018: 5,000+), COVID-19 "
            "(2020-2021: 500,000+), Ukraine/Russia (2022: 300+), Israel-Gaza (2023: 5,000+). "
            "OWWA and ATN Fund cover repatriation costs. DFA charters aircraft for mass "
            "repatriations."
        ),
        "source": "OWWA / DFA / DMW repatriation reports",
    },

    # ── Additional Statistic Entries ───────────────────────────────────
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Filipino Seafarer Global Market Share",
        "metric": "Share of global seafarer workforce",
        "value": "~25% of world's seafarers",
        "year": 2023,
        "details": (
            "Filipino seafarers constitute approximately 25% of the world's 1.89 million "
            "seafarers. Approximately 400,000-530,000 deployed annually on international "
            "vessels. Manning agencies in the Philippines: approximately 400 licensed. "
            "Average monthly salary: USD 800-3,500 depending on rank and vessel type. "
            "Key concern: vessel abandonment cases where crew are left without pay in "
            "foreign ports. ITF (International Transport Workers' Federation) assists in "
            "wage recovery."
        ),
        "source": "DMW / MARINA / BIMCO-ICS Manpower Report",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OFW Sector Distribution",
        "metric": "Distribution of deployed OFWs by sector",
        "value": "Service workers 35%, production workers 25%, professionals 15%",
        "year": 2023,
        "details": (
            "Land-based OFW deployment by occupation group (2023): (1) service workers "
            "(domestic workers, caregivers, cleaners) — 35%; (2) production workers "
            "(construction, manufacturing, welding) — 25%; (3) professionals (nurses, "
            "engineers, IT, teachers) — 15%; (4) clerical workers — 8%; (5) plant/machine "
            "operators — 7%; (6) technicians — 5%; (7) other — 5%. Domestic workers "
            "constitute approximately 120,000-150,000 new hires per year, predominantly "
            "female (>95%), deployed mainly to Gulf states and Hong Kong."
        ),
        "source": "DMW / PSA Survey on Overseas Filipinos 2023",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Gender Breakdown of Filipino OFWs",
        "metric": "Male-female ratio of deployed OFWs",
        "value": "54% male, 46% female (2023)",
        "year": 2023,
        "details": (
            "Overall gender breakdown approximately 54% male, 46% female. However, in "
            "new hire domestic worker category: >95% female. In seafaring: >98% male. "
            "In professional categories (nursing, teaching): approximately 60% female. "
            "In construction and manufacturing: approximately 90% male. Vulnerability "
            "assessment: female domestic workers in private households face highest risk "
            "of isolation, abuse, and trafficking. Philippine migration policy increasingly "
            "gender-responsive per RA 10022 amendments."
        ),
        "source": "DMW / PSA / ILO Manila",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "OWWA Membership and Fund Status",
        "metric": "Active OWWA members and fund balance",
        "value": "~2.3 million active members, PHP ~200 billion fund",
        "year": 2023,
        "details": (
            "OWWA has approximately 2.3 million active contributing members (2023). "
            "Membership fee: USD 25 per deployment contract. Fund balance: approximately "
            "PHP 200 billion (cumulative). Annual benefits disbursed: approximately "
            "PHP 8-12 billion. Death benefits paid: approximately 2,000-3,000 cases per "
            "year. Disability benefits: approximately 500-1,000 cases. Scholarship grants: "
            "approximately 40,000 beneficiaries (dependents of OFWs) per year."
        ),
        "source": "OWWA annual report 2023",
    },

    # ══════════════════════════════════════════════════════════════════════
    #  ADDITIONAL LEGISLATION AND REGULATIONS
    # ══════════════════════════════════════════════════════════════════════

    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10706 — Overseas Filipino Bank Act (2015)",
        "summary": (
            "Mandated the establishment of a government bank (under Land Bank) to provide "
            "affordable financial services to OFWs and their beneficiaries. Services include: "
            "low-cost remittance, savings accounts, micro-enterprise loans, and financial "
            "literacy programs. Aimed at reducing OFW reliance on informal money transfer "
            "systems and predatory lending."
        ),
        "source": "RA 10706, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10801 — OWWA Act (2016)",
        "summary": (
            "Codifies OWWA as an agency attached to DMW (formerly DOLE). Mandates: welfare "
            "services, repatriation assistance, and reintegration programs. Establishes "
            "OWWA Board of Trustees with OFW representation. Requires OWWA fund to be used "
            "exclusively for OFW welfare. Caps administrative expenses at 10% of annual "
            "collections. Provides for OWWA regional welfare offices."
        ),
        "source": "RA 10801, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11227 — OFW E-Card Act (2019)",
        "summary": (
            "Mandates issuance of an Overseas Filipino Worker Electronic Card (OFW E-Card) "
            "as a unified identification document. Serves as valid ID for government "
            "transactions, OFW ID for discounts and benefits, and ATM/debit card for "
            "remittances. Integrates OWWA, PhilHealth, SSS, and Pag-IBIG membership data. "
            "DMW is the lead implementing agency."
        ),
        "source": "RA 11227, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9422 — An Act Strengthening the POEA (2007)",
        "summary": (
            "Strengthened POEA by increasing penalties for recruitment violations, "
            "expanding the scope of prohibited acts, and enhancing POEA's quasi-judicial "
            "authority. Required posting of escrow deposits for worker protection. Now "
            "superseded by DMW creation under RA 11641 but penalty provisions remain "
            "operative."
        ),
        "source": "RA 9422, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10173 — Data Privacy Act (2012) — OFW Data Protection",
        "summary": (
            "Applies to personal data of OFWs held by government agencies and recruitment "
            "agencies. DMW, OWWA, and DFA bound to protect OFW personal information. "
            "Recruitment agencies must comply with data processing principles for worker "
            "biodata, medical records, and employment history. National Privacy Commission "
            "oversight. Relevant to cross-border data sharing with foreign employers."
        ),
        "source": "RA 10173, Official Gazette / NPC",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 11199 — Social Security Act of 2018 — OFW Provisions",
        "summary": (
            "Mandates SSS coverage for all OFWs. Voluntary self-employed classification "
            "for land-based OFWs; mandatory for sea-based through manning agency. Benefits: "
            "sickness, maternity, disability, retirement, death, funeral, and "
            "unemployment/involuntary separation. Monthly contribution: based on declared "
            "earnings (PHP 2,400-30,000 bracket). SSS benefits complement OWWA coverage."
        ),
        "source": "RA 11199 / SSS",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 7882 — Benefits for Women OFWs (1995)",
        "summary": (
            "Provides additional benefits for women in overseas employment: gender-sensitive "
            "pre-departure orientation, legal assistance specific to gender-based violence, "
            "rescue and repatriation priority for women in distress, skills training for "
            "returning women OFWs, and livelihood programs. Implemented through DOLE (now DMW) "
            "and OWWA in coordination with the Philippine Commission on Women."
        ),
        "source": "RA 7882, Official Gazette",
    },

    # ── Additional DOLE/DMW Orders ─────────────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POEA Governing Board Resolution 06-2012 — Domestic Worker Minimum Wage",
        "summary": (
            "Set minimum monthly salary for newly hired Filipino domestic workers: "
            "USD 400 (all destinations). Superseded by bilateral agreement rates where "
            "applicable (e.g., Hong Kong HKD 4,870, Saudi Arabia SAR 1,500, Kuwait "
            "KWD 120). Agencies prohibited from deploying domestic workers at salary "
            "below DMW-prescribed minimum."
        ),
        "source": "POEA GBR 06-2012 / DMW",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POEA MC 08-2018 — Mandatory Insurance for OFWs",
        "summary": (
            "Implements RA 10022 compulsory insurance provision. Minimum coverage: "
            "accidental death (USD 15,000), natural death (USD 10,000), permanent total "
            "disability (USD 7,500), repatriation cost (actual), subsistence allowance "
            "(USD 100/month for up to 6 months during medico-legal cases), medical evacuation "
            "(USD 5,000). Insurance premium borne by the agency, NOT the worker. "
            "Non-compliant agencies face suspension."
        ),
        "source": "POEA MC 08-2018",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW MC 11-2022 — OFW Welfare Assistance at Ports of Entry",
        "summary": (
            "Establishes welfare desks at all Philippine international airports (NAIA "
            "Terminals 1-3, Clark, Mactan-Cebu, Davao). Provides: airport assistance for "
            "departing OFWs, counseling for distressed arriving OFWs, coordination with "
            "OWWA and DSWD for repatriated workers requiring shelter, and referral to "
            "IACAT for suspected trafficking victims identified at the airport."
        ),
        "source": "DMW MC 11-2022",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DOLE DO 183-17 — Revised POEA Rules on Manning",
        "summary": (
            "Comprehensive rules for sea-based recruitment: manning agency licensing, "
            "principal/employer accreditation, Standard Employment Contract for seafarers "
            "(SEC), crew complement requirements, MLC 2006 compliance, port State control "
            "preparation. Requires manning agencies to maintain escrow fund of USD 50,000 "
            "for crew wage claims in case of vessel arrest or abandonment."
        ),
        "source": "DOLE DO 183-17 / POEA",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POEA MC 02-2016 — Standard Employment Contract Provisions",
        "summary": (
            "Mandates minimum contract provisions for all OFWs: guaranteed wages in specific "
            "currency, free food and accommodation (or allowance), transportation to/from "
            "worksite, free medical/dental services, personal accident insurance, overtime "
            "pay, rest days, vacation leave, end-of-contract benefits, and repatriation. "
            "Contract must be verified and approved by POEA/DMW before deployment."
        ),
        "source": "POEA MC 02-2016 / DMW",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "DMW DC 05-2023 — Anti-Illegal Recruitment Operations Protocol",
        "summary": (
            "Updates protocol for DMW anti-illegal recruitment operations: intelligence "
            "gathering from social media monitoring, coordination with NBI cybercrime, "
            "entrapment procedures, evidence preservation, and case referral to DOJ. "
            "Addresses emerging threats: online recruitment scams, crypto-based payment "
            "schemes, and social media-based illegal recruitment."
        ),
        "source": "DMW DC 05-2023",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "EO 57 (2018) — Strengthening Protection of Filipino Migrant Workers",
        "summary": (
            "Directed POEA, OWWA, and DFA to strengthen OFW protection mechanisms. "
            "Key provisions: expedited processing of OFW complaints, immediate repatriation "
            "of distressed workers, enhanced monitoring of compliance by recruitment agencies, "
            "and deployment of additional labor attaches to high-volume destinations. Issued "
            "in aftermath of Kuwait deployment crisis."
        ),
        "source": "EO 57 (2018), Official Gazette",
    },

    # ── Additional Institutional Framework Facts ───────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "National Maritime Polytechnic (NMP)",
        "summary": (
            "Government training institution under DMW providing competency-based training "
            "and assessment for Filipino seafarers. Offers courses in compliance with STCW "
            "(International Convention on Standards of Training, Certification and Watchkeeping). "
            "Located in Tacloban City. Annual trainees: approximately 15,000-20,000 seafarers. "
            "NMP ratings and certifications recognized by major flag states."
        ),
        "source": "NMP / DMW",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "Commission on Filipinos Overseas (CFO)",
        "summary": (
            "Advisory body under the Office of the President. Provides guidance and policy "
            "advice on Filipino migration issues. Conducts pre-departure orientation for "
            "emigrant spouses, fiancees, and adopted children (CPDEP and GCG programs). "
            "Maintains comprehensive database on Philippine emigration. Administers the "
            "Balikbayan program for returning overseas Filipinos."
        ),
        "source": "CFO / RA 8042",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "TESDA — OFW Skills Training Programs",
        "summary": (
            "Technical Education and Skills Development Authority administers OFW-targeted "
            "training programs. TESDA certifications accepted for overseas employment: "
            "caregiver, household service worker, welding, automotive, electrical installation, "
            "and food and beverage services. OFW TESDA scholarship: free training for "
            "intending OFWs and returning OFWs seeking reintegration. Certificates aligned "
            "with Philippine TVET Qualifications Framework."
        ),
        "source": "TESDA / DMW partnership programs",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "PhilHealth — OFW Program Coverage",
        "summary": (
            "PhilHealth provides mandatory health insurance for OFWs. OFW Program: covers "
            "inpatient and outpatient care in the Philippines for OFW and qualified dependents. "
            "Monthly contribution: PHP 900 (2023). Benefits include: case rate packages for "
            "common procedures, Z-Benefits for catastrophic illness, and primary care benefit. "
            "Complements OWWA insurance and employer-provided overseas health coverage."
        ),
        "source": "PhilHealth / RA 11223 (Universal Health Care Act)",
    },

    # ── Specialized Legislation ────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10361 — Kasambahay (Domestic Workers) Act (2013)",
        "summary": (
            "Protects domestic workers (kasambahay) in the Philippines. While primarily "
            "covering domestic employment, establishes standards used as benchmarks for "
            "overseas domestic worker contracts. Provisions: minimum wage, SSS/PhilHealth/ "
            "Pag-IBIG coverage, 13th month pay, rest days, and prohibition of debt bondage "
            "through salary advances. Informs Philippine government standards for bilateral "
            "agreements covering domestic workers abroad."
        ),
        "source": "RA 10361, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9710 — Magna Carta of Women (2009)",
        "summary": (
            "Comprehensive women's rights law. Section 24 specifically addresses women in "
            "overseas employment: guarantees non-discriminatory recruitment, gender-responsive "
            "pre-departure orientation, protection from trafficking and exploitation, and "
            "gender-specific welfare services. Mandates government to provide special "
            "attention to needs of women migrant workers."
        ),
        "source": "RA 9710, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9775 — Anti-Child Pornography Act (2009)",
        "summary": (
            "Criminalizes production, distribution, and possession of child pornography. "
            "Relevant to anti-trafficking framework: RA 11862 (2022) linked online sexual "
            "exploitation of children to trafficking. ISPs required to report and block "
            "child exploitation material. NBI and PNP cybercrime units enforce. Penalties: "
            "reclusion temporal to reclusion perpetua."
        ),
        "source": "RA 9775, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 10592 — Good Conduct Time Allowance Act (2013)",
        "summary": (
            "Provides credit for preventive imprisonment and good conduct time allowance. "
            "Controversial application to trafficking and illegal recruitment convicts: "
            "some high-profile illegal recruiters released early under GCTA provisions. "
            "Led to calls for excluding trafficking and large-scale illegal recruitment "
            "from GCTA eligibility. RA 10592 was amended by RA 11752 (2022) to address "
            "heinous crime exclusions."
        ),
        "source": "RA 10592 / RA 11752, Official Gazette",
    },
    {
        "type": "law",
        "jurisdiction": "PH",
        "title": "RA 9160 — Anti-Money Laundering Act (as amended) — Trafficking Provisions",
        "summary": (
            "Trafficking in persons and illegal recruitment are predicate crimes under "
            "the AMLA. AMLC may freeze and forfeit assets linked to trafficking proceeds. "
            "Financial institutions required to report suspicious transactions related to "
            "trafficking patterns (large cash deposits from recruitment agencies, unusual "
            "remittance patterns). AMLC coordinates with IACAT on financial investigations "
            "of trafficking networks."
        ),
        "source": "RA 9160 as amended / AMLC / IACAT",
    },

    # ── Additional Enforcement and Contact Data ────────────────────────
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "DMW Online Complaint Portal",
        "organization": "Department of Migrant Workers",
        "contact_type": "online_portal",
        "details": (
            "DMW online complaint portal at dmw.gov.ph. Workers and families can file "
            "complaints against recruitment agencies, report illegal recruitment, request "
            "assistance, and track case status. Integrated with DMW action center hotline "
            "8722-1144 / 8722-1155. Available in Filipino and English."
        ),
        "source": "DMW website",
    },
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "NBI Anti-Human Trafficking Division Hotline",
        "organization": "National Bureau of Investigation",
        "contact_type": "hotline",
        "details": (
            "NBI Anti-Human Trafficking Division: (02) 8523-8231 to 38 local 307. "
            "Handles: trafficking complaints, illegal recruitment investigation referrals, "
            "entrapment operations, cross-border trafficking intelligence. Works with "
            "INTERPOL, FBI, and destination country law enforcement."
        ),
        "source": "NBI / IACAT",
    },
    {
        "type": "contact",
        "jurisdiction": "PH",
        "title": "PNP Women and Children Protection Center (WCPC)",
        "organization": "Philippine National Police",
        "contact_type": "hotline",
        "details": (
            "PNP WCPC hotline: 117 (DSWD/PNP joint) or (02) 8532-6690. Handles: rescue "
            "operations for trafficking victims, investigation of trafficking cases, "
            "protection of witnesses, and enforcement of anti-trafficking laws. Operates "
            "Women and Children Protection Desks in all PNP stations nationwide."
        ),
        "source": "PNP WCPC / IACAT",
    },

    # ── Case Law and Court Rulings ─────────────────────────────────────
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Casio (G.R. No. 211465, 2014) — Trafficking Conviction Standard",
        "summary": (
            "Supreme Court affirmed trafficking conviction even without testimony from the "
            "victim. Established that trafficking may be proven through circumstantial "
            "evidence, testimony of law enforcement, and documentary evidence. Victim's "
            "consent is irrelevant where means of trafficking (threat, force, coercion, "
            "deception, abuse of vulnerability) are established."
        ),
        "source": "Supreme Court of the Philippines / IACAT case compilation",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. Lalli (G.R. No. 195419, 2012) — Trafficking for Forced Labor",
        "summary": (
            "Supreme Court upheld conviction for trafficking for forced labor (RA 9208 "
            "Sec. 4(a)). Affirmed that recruitment of a person for employment under "
            "exploitative conditions through deception constitutes trafficking. Victim was "
            "recruited as waitress but subjected to forced labor as domestic worker. Court "
            "awarded moral and exemplary damages plus actual damages for lost wages."
        ),
        "source": "Supreme Court of the Philippines",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "Serrano v. Gallant Maritime (G.R. No. 167614, 2009) — OFW Money Claims",
        "summary": (
            "Supreme Court landmark ruling striking down the clause in RA 8042 Sec. 10 "
            "that limited money claims to 3 months per year of unexpired contract. Held "
            "that OFWs are entitled to full salaries for the entire unexpired portion of "
            "the contract. Led to amendment under RA 10022 restoring full salary entitlement."
        ),
        "source": "Supreme Court of the Philippines",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "PH",
        "title": "People v. XXX (G.R. No. 235652, 2019) — Online Trafficking",
        "summary": (
            "Supreme Court affirmed conviction for online trafficking of children. "
            "Established that live-streaming of child sexual abuse for foreign clients "
            "constitutes trafficking under RA 9208 as amended. Conviction applied even "
            "when the victims were related to the offender (parent-offender case). "
            "Aggravated penalty: reclusion perpetua."
        ),
        "source": "Supreme Court of the Philippines / IJM Philippines",
    },

    # ── Additional Bilateral Agreements ────────────────────────────────
    {
        "type": "bilateral_agreement",
        "jurisdiction": "PH-DE",
        "corridor": "PH-DE",
        "title": "Philippines-Germany Triple Win Program",
        "summary": (
            "Government-to-government program deploying Filipino nurses to Germany. "
            "Managed by DMW and German GIZ. Zero placement fee. German language training "
            "provided (B1-B2 level). Employer-paid relocation. Nurses must pass German "
            "nursing qualification recognition. Annual quota: approximately 500-1,000. "
            "Considered a model ethical recruitment program."
        ),
        "source": "DMW / GIZ / German Federal Employment Agency",
    },
    {
        "type": "bilateral_agreement",
        "jurisdiction": "PH-UK",
        "corridor": "PH-UK",
        "title": "Philippines-UK Government-to-Government Healthcare Worker Agreement",
        "summary": (
            "Bilateral framework for ethical recruitment of Filipino nurses and healthcare "
            "workers to the UK National Health Service (NHS). Complies with WHO Global Code "
            "of Practice on International Recruitment of Health Personnel. Zero fee to "
            "workers. IELTS English proficiency and NMC registration required. Managed by "
            "DMW and NHS England."
        ),
        "source": "DMW / NHS England / DFA",
    },
    {
        "type": "bilateral_agreement",
        "jurisdiction": "PH-CA",
        "corridor": "PH-CA",
        "title": "Philippines-Canada Seasonal Agricultural Worker Agreement",
        "summary": (
            "Allows deployment of Filipino agricultural workers to Canada under the "
            "Seasonal Agricultural Worker Program (SAWP) and Temporary Foreign Worker "
            "Program (TFWP). Standard employment contract with minimum wage compliance. "
            "Employer provides housing and transportation. Workers may apply for permanent "
            "residency through Provincial Nominee Programs after qualifying period."
        ),
        "source": "DMW / IRCC Canada / ESDC",
    },
    {
        "type": "bilateral_agreement",
        "jurisdiction": "PH-TW",
        "corridor": "PH-TW",
        "title": "Philippines-Taiwan (MECO-TECO) Labor Agreement",
        "summary": (
            "Managed through the Manila Economic and Cultural Office (MECO) and Taipei "
            "Economic and Cultural Office (TECO). Covers manufacturing, construction, "
            "caregiving, and domestic work. Placement fee cap for Taiwan: NTD 40,000 "
            "(first year), NTD 30,000 (second year), NTD 25,000 (third year). Taiwan "
            "requires workers to pass skills assessment and Chinese language training. "
            "Approximately 160,000 Filipino workers in Taiwan."
        ),
        "source": "MECO / TECO / DMW",
    },

    # ── Historical and Notable Regulations ─────────────────────────────
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POEA Governing Board Resolution 02-2019 — Household Service Worker Age Requirement",
        "summary": (
            "Sets minimum deployment age for household service workers (domestic workers) "
            "at 23 years old. Intended to ensure greater maturity and ability to assert "
            "rights while working in isolated private households abroad. Lower minimum "
            "of 18 years applies to other occupational categories. Age requirement has "
            "been criticized for limiting employment options for younger workers while "
            "supporters argue it reduces vulnerability to abuse."
        ),
        "source": "POEA GBR 02-2019 / DMW",
    },
    {
        "type": "regulation_change",
        "jurisdiction": "PH",
        "title": "POEA MC 10-2010 — Deployment of Filipino Workers to Conflict Zones",
        "summary": (
            "Prohibits deployment to conflict-affected areas unless: (1) DFA issues "
            "clearance certifying security measures are in place; (2) employer provides "
            "comprehensive insurance; (3) evacuation plan exists; (4) worker gives informed "
            "consent after comprehensive briefing. Alert levels: 1 (precaution), 2 "
            "(restriction), 3 (voluntary repatriation), 4 (mandatory evacuation). "
            "Currently Level 4: Libya, Syria, Yemen, parts of Iraq and Afghanistan."
        ),
        "source": "POEA MC 10-2010 / DFA",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Illegal Recruitment Victim Demographics",
        "metric": "Profile of illegal recruitment victims in the Philippines",
        "value": "~70% female, median age 28, 60% from rural provinces",
        "year": 2023,
        "details": (
            "IACAT and DMW data show illegal recruitment victims are predominantly: "
            "female (~70%), aged 20-35 (median 28), from rural provinces in Visayas and "
            "Mindanao, with secondary education, and first-time OFWs (65% of victims). "
            "Common deception: promise of high-paying jobs in UAE, Saudi Arabia, or Kuwait. "
            "Average amount lost: PHP 80,000-200,000 per victim. Family members (particularly "
            "mothers and spouses) are often the initial contact point for illegal recruiters."
        ),
        "source": "IACAT / DMW AIRB data",
    },
    {
        "type": "statistic",
        "jurisdiction": "PH",
        "title": "Licensed Recruitment Agencies in the Philippines",
        "metric": "Number of DMW-licensed recruitment agencies",
        "value": "~1,600 total (1,200 land-based, 400 manning)",
        "year": 2023,
        "details": (
            "As of 2023: approximately 1,200 licensed land-based agencies and 400 licensed "
            "manning agencies. Geographic concentration: ~80% based in Metro Manila. "
            "Top agencies by deployment volume deploy 5,000-20,000 workers per year. "
            "Average agency deploys 200-500 per year. Agencies must renew license every "
            "4 years. DMW publishes directory of licensed agencies and suspended/revoked "
            "agencies on its website."
        ),
        "source": "DMW agency registry",
    },
]
