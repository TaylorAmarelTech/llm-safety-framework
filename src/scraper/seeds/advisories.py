"""Red flag advisories, exploitation patterns, and warning signs."""

ADVISORY_FACTS: list[dict] = [
    # ── Existing ──────────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Contract Substitution Warning Signs",
        "summary": "Worker signs contract in home country then receives different contract upon arrival. Changed terms include: lower salary, different job, longer hours, different employer, restricted movement. A primary indicator of trafficking.",
    },
    {
        "type": "advisory",
        "jurisdiction": "PH-SA",
        "corridor": "PH-SA",
        "title": "Salary Deduction Schemes in PH-SA Corridor",
        "summary": "Common schemes: 3-6 months salary deduction for 'placement fees', monthly deductions for 'accommodation/food' already provided by employer, charges for 'contract processing'. All illegal under DMW regulations.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Passport Confiscation Prevalence",
        "summary": "Reported in 80%+ of GCC domestic worker cases. Also prevalent in SG, MY, TH. Employers claim 'safekeeping.' Illegal in most jurisdictions but weakly enforced. Key indicator of forced labour.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Recruitment Agency Violation Patterns",
        "summary": "Common violations: charging excessive fees, contract substitution, misrepresentation of terms, deploying to non-verified employers, operating without license, using sub-agents. Sub-agent chains add fees at each layer.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Kafala System — Overview and Reform Status",
        "summary": "Sponsorship system in GCC countries tying worker legal status to employer. Reforms: Qatar (2020) abolished NOC for job change; SA (2021) allowed limited transferability; UAE (2023) worker-initiated transfer after 12 months. Kuwait, Bahrain partial reforms. Full abolition remains elusive.",
    },

    # ── New advisories ────────────────────────────────────────────────
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Pre-Departure Deception Indicators",
        "summary": "Warning signs before departure: vague job descriptions, verbal-only promises, pressure to sign quickly, requests for upfront payment, training at unlicensed centers, last-minute destination changes, confiscation of originals during 'processing'.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Arrival Document Confiscation Sequence",
        "summary": "Common pattern: airport pickup by employer/agent → passport collected 'for visa processing' → never returned. Variations: locked in safe 'for security', held by sponsor, or handed to labor camp supervisor. Creates total dependency.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Communication Isolation Tactics",
        "summary": "Methods: confiscate mobile phone, prohibit calls home, monitor/restrict internet access, deny rest days (no time to contact anyone), linguistic isolation (no speakers of worker's language), threaten family if worker complains.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Debt Escalation Mechanisms",
        "summary": "Initial recruitment debt grows through: compounding 'interest', charges for accommodation/food/transport, fines for 'mistakes', medical treatment costs deducted, fees for contract renewals, charges for tools/uniforms. Debt becomes unpayable.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Employer Transfer Denial as Control",
        "summary": "Under kafala: employer refuses to grant release letter/NOC, keeping worker in exploitative situation. Post-reform: employers find loopholes (filing 'absconding' reports, claiming financial obligations). Transfer denial is a coercion tool.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Training Fee Scams",
        "summary": "Unlicensed 'training centers' charge USD 500-3,000 for mandatory pre-departure training. Training often substandard or irrelevant. Fees added to worker debt. Some centers operate as holding facilities with restricted movement.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Visa Status Threats",
        "summary": "Employer threatens to cancel visa/work permit if worker complains or tries to leave. In irregular migration situations, threat of reporting to immigration authorities. Creates fear of arrest, detention, and deportation.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Food and Accommodation Deductions as Control",
        "summary": "Employer provides substandard food/housing then deducts 30-50% of salary for these 'services'. Workers cannot opt out or find alternatives. Creates a cycle where take-home pay is minimal despite contracted salary.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "False Criminal Charges as Intimidation",
        "summary": "Employer files false theft/assault charges against worker who complains or attempts to leave. In GCC: 'absconding' charge makes worker undocumented and subject to arrest. Used as retaliation and deterrent.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Family Threats in Home Country",
        "summary": "Agents or employers threaten to harm family members in origin country if worker runs away, reports to authorities, or fails to repay debt. Particularly effective when family members guaranteed the loan.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "'Runaway' Reporting as Retaliation",
        "summary": "Employer reports worker as 'absconding' to police before worker can file complaint. In GCC: absconding report makes worker's visa invalid, turning victim into criminal. Worker detained while employer faces no investigation.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Medical Expense Debt Traps",
        "summary": "Worker injuries or illnesses treated at employer-selected clinics at inflated prices. Costs deducted from salary or added to debt. Workers denied medical care unless they agree to continue working. Workplace injury costs shifted to worker.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Forced Overtime Refusal Consequences",
        "summary": "Workers who refuse excessive overtime face: salary reduction, physical punishment, threats of termination and deportation, denial of food, or transfer to worse conditions. Overtime often unpaid or at reduced rate.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Early Termination Penalties as Bondage",
        "summary": "Contracts include illegal early termination clauses: worker must pay 3-6 months salary penalty, repay all recruitment costs, or forfeit end-of-service benefits. Creates financial barrier to leaving exploitative situation.",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Social Media Recruitment Deception",
        "summary": "Recruiters use Facebook, TikTok, WhatsApp to advertise jobs with inflated salaries and false conditions. Victims recruited through trusted community members. Fake testimonials from 'successful' workers. Difficult to trace or prosecute.",
    },
]
