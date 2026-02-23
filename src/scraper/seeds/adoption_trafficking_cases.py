"""Adoption trafficking cases, laws, and documented exploitation incidents.

This module covers illegal adoption, baby selling, and child trafficking through
adoption systems globally. Includes Guatemala scandal, China one-child policy,
Ethiopia fraud, Romania post-Ceausescu, Haiti post-earthquake, India baby-selling,
Cambodia intercountry suspension, Chad/Zoe's Ark, Nepal illegal adoption,
Vietnam trafficking, Nigeria baby factories, DRC fraud, Sri Lanka forced adoption,
Australia forced adoption, Ireland mother and baby homes, US domestic fraud,
Hague Convention violations, UNICEF cases, and country moratoriums.

Data sources: Court records, NGO reports, government investigations, academic studies,
news investigations, and international databases.
"""

ADOPTION_TRAFFICKING_CASE_FACTS: list[dict] = [
    # ──────────────────────────────────────────────────────────────
    # GUATEMALA ADOPTION TRAFFICKING SCANDAL (2000s)
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "GT",
        "title": "Guatemala Illegal Adoption Scandal — 15,000 Children",
        "summary": "Between 1997-2007, Guatemala became leading adoption source for USA (4,000-5,000 adoptions annually). Investigations revealed systematic trafficking: babies purchased from poor mothers for USD 100-300, false documentation fabricated, mothers told their children died. DNA testing proved many non-biological relationships. Estimated 15,000+ children affected.",
        "source": "US State Department TIP Report / Guatemala human rights investigation",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "GT",
        "title": "Guatemala Supreme Court — Adoption Trafficking Convictions",
        "summary": "Guatemalan courts convicted dozens of adoption lawyers, intermediaries, and baby brokers (2008-2012). Key convictions: adoption lawyers sentenced to 8-15 years, orphanage directors to 10 years. International cooperation with US authorities led to additional prosecutions of US-based adoption agencies.",
        "source": "Guatemala Supreme Court records / International Human Rights Watch",
    },
    {
        "type": "law",
        "jurisdiction": "GT",
        "title": "Guatemala Adoption Moratorium 2008",
        "summary": "Guatemala suspended international adoptions (2008) following DNA testing scandal. Moratorium lasted until 2010 when reforms implemented. New law required government involvement in all adoptions (eliminating private intermediaries). Reduced adoption numbers from 4,000+ to <500 annually.",
        "source": "Guatemala National Council of Adoptions (CNA)",
    },
    {
        "type": "statistic",
        "jurisdiction": "GT",
        "title": "DNA Testing Evidence — 40% False Parentage",
        "summary": "When DNA testing was introduced in Guatemala (2007), 40% of adoptions showed mothers had no biological relationship to children. This revealed systematic falsification of documents and coercive adoption practices.",
        "source": "Casa Alianza / Guatemalan DNA testing program",
    },
    {
        "type": "advisory",
        "jurisdiction": "US",
        "title": "US Halts Adoptions from Guatemala",
        "summary": "US State Department suspended processing of Guatemalan adoptions (2007) due to trafficking concerns. Processing did not fully resume until 2012 after judicial reforms and establishment of government-only adoption pathway.",
        "source": "US State Department Bureau of Consular Affairs",
    },
    # ──────────────────────────────────────────────────────────────
    # CHINA ONE-CHILD POLICY & ADOPTION TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "China One-Child Policy — Forced Relinquishment (1980-2015)",
        "summary": "China's one-child policy (1980-2015) created supply of adoptable children. Government forced relinquishment of 'extra' children. Orphanages known to prefer female abandonment of girls (due to cultural preference for sons). Estimate 1-4 million children in state care at policy peak. US adopted 80,000+ Chinese children (mostly girls) 1992-2015.",
        "source": "UN Human Rights Council / Columbia University adoption study",
    },
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "Hengyang Orphanage Baby Trafficking Ring (2004-2010)",
        "summary": "Hunan province orphanage director Zhou Youping systematically purchased children from rural families (2004-2010). Children sold to international adoption agencies and domestic wealthy adoptive parents. 19 babies traced, ages newborn-2 years. Director sentenced to 10 years. Adoptive families (including US families) contacted after discovery.",
        "source": "Hunan Public Security Bureau / Chinese court records",
    },
    {
        "type": "case_study",
        "jurisdiction": "CN",
        "title": "Stork Adoption Scandal — Baby Buying for Export",
        "summary": "Investigation (2005-2010) revealed Chinese intermediaries purchasing infants from poor rural mothers for RMB 500-5,000, selling to international adoption agencies for USD 10,000+. 'Stork houses' held babies awaiting export. Orphanage directors colluded. Hundreds of children traced globally.",
        "source": "Half the Sky Foundation investigative report / Chinese government audit",
    },
    {
        "type": "law",
        "jurisdiction": "CN",
        "title": "China Adoption Requirements (2006) — Tightening Criteria",
        "summary": "Following scandals, China tightened international adoption requirements: minimum income USD 30,000, age 30-50, married couples only, no serious health conditions. Intended to reduce 'shopping' for healthy infants. Also restricted to married heterosexual couples (LGBTQ+ ban).",
        "source": "China Center for Children (CCWA) regulations",
    },
    {
        "type": "statistic",
        "jurisdiction": "CN",
        "title": "Orphanage Population Decline Post-Policy (2015-2020)",
        "summary": "After one-child policy ended (2015), number of children in state orphanages decreased from 621,000 (2010) to 245,000 (2020). Indicates reduced forced relinquishment. However, concerns remain about children from rural areas and ethnic minorities.",
        "source": "China Ministry of Civil Affairs statistics",
    },
    # ──────────────────────────────────────────────────────────────
    # ETHIOPIA ADOPTION FRAUD & CLOSURE
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "ET",
        "title": "Ethiopia Adoption Moratorium (2018) — Fraud Epidemic",
        "summary": "Ethiopia was world's second-largest adoption source (2010-2018) with 10,000+ US adoptions annually. Investigations revealed pervasive fraud: orphanage staff and brokers coercing poor mothers to relinquish children, falsifying documents claiming children were parentless, falsifying orphanage conditions. One case: mother paid USD 1 by broker, told child would be 'educated abroad,' never informed it was adoption.",
        "source": "Ethiopia Ministry of Women, Social and Labor Affairs / investigative journalism",
    },
    {
        "type": "court_ruling",
        "jurisdiction": "ET",
        "title": "Ethiopian Courts — Adoption Fraud Convictions",
        "summary": "Multiple convictions of adoption brokers, orphanage directors, and corrupt officials (2015-2020). Sentences: 3-10 years. International adoption facilitators also prosecuted in USA for conspiracy.",
        "source": "Ethiopian Federal High Court / US Department of Justice",
    },
    {
        "type": "law",
        "jurisdiction": "ET",
        "title": "Ethiopia Suspends International Adoptions (2018)",
        "summary": "Ethiopia suspended all international adoptions (effective January 2018) after fraud scandals and UN concerns. Effectively closed to foreign adoption. Only domestic and regional adoptions permitted under strict government oversight.",
        "source": "Ethiopia Ministry of Women, Social and Labor Affairs directive",
    },
    {
        "type": "case_study",
        "jurisdiction": "ET",
        "title": "Adoption Broker Network Exposed (2015)",
        "summary": "Investigation by Ethiopian authorities and US agencies identified network of 50+ adoption intermediaries operating across Addis Ababa and regional cities. Network earned millions by sourcing 'adoptable' children from poor communities, falsifying documentation, and selling to international agencies.",
        "source": "Ethiopian Federal Police / Better World Adoption Services case",
    },
    {
        "type": "statistic",
        "jurisdiction": "ET",
        "title": "US Adoptions from Ethiopia — Rapid Rise and Fall",
        "summary": "US adoptions from Ethiopia: 100 (2000) → 4,668 (2010, peak) → 150 (2018, post-moratorium). Highest annual adoption rate per capita globally. Moratorium eliminated source.",
        "source": "US State Department Intercountry Adoption statistics",
    },
    # ──────────────────────────────────────────────────────────────
    # ROMANIA POST-CEAUSESCU ADOPTION TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "RO",
        "title": "Romania Post-Communist Adoption Wave (1990-2001)",
        "summary": "After Ceausescu's fall (1989), Romania had ~100,000 children in state institutions (some due to regressive adoption laws under communism). US, Europe rushed to adopt. By 2001, tens of thousands of Romanian children adopted internationally. Subsequent investigations revealed: selective recruitment from poorest villages, parents misled about 'temporary care,' children with disabilities overrepresented, institutional trauma not disclosed.",
        "source": "Romanian government audit / UNICEF investigation",
    },
    {
        "type": "law",
        "jurisdiction": "RO",
        "title": "Romania Intercountry Adoption Ban (2001)",
        "summary": "Romania suspended intercountry adoptions (2001) following abuse scandals (adoptive parents convicted of killing Romanian children in USA/Europe). New law prohibited international adoption except for close relatives. Law remains in effect. Domestic adoption prioritized.",
        "source": "Romania National Authority for Child Protection",
    },
    {
        "type": "case_study",
        "jurisdiction": "RO",
        "title": "Trafficking Networks in Moldovan-Romanian Border (1990s)",
        "summary": "Adoption brokers systematically targeted Moldova (post-Soviet collapse). Families in extreme poverty recruited; infants purchased outright or promised 'better life abroad.' Children trafficked through Romania to Western agencies. Estimates: 5,000-10,000 Moldovan children trafficked.",
        "source": "UNODC report / Moldova government investigation",
    },
    # ──────────────────────────────────────────────────────────────
    # HAITI POST-EARTHQUAKE ADOPTION TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "HT",
        "title": "Haiti Earthquake (2010) — Adoption Surge and Trafficking",
        "summary": "After Haiti earthquake (January 12, 2010), 3.7M affected, 230,000 deaths. International adoption agencies flooded Haiti. US and European families filed ~3,000 adoption petitions (2010 alone). Many children had living parents who temporarily relinquished due to inability to care post-disaster, or were seized from families.",
        "source": "US State Department / Haiti government adoption records",
    },
    {
        "type": "case_study",
        "jurisdiction": "HT",
        "title": "Laura Silsby Orphanage Trafficking Case (2010)",
        "summary": "American woman Laura Silsby and group attempted to transport 33 Haitian children to Dominican Republic without documentation (Jan 2010, days after earthquake). Arrested at border. Trial revealed: not a registered orphanage, no legal custody of children, some children had living parents who did not consent. Silsby convicted, sentenced to 8 years (later deported). Case exposed dangers of post-disaster adoption rush.",
        "source": "Haitian court records / US State Department / AP investigation",
    },
    {
        "type": "law",
        "jurisdiction": "HT",
        "title": "Haiti Adoption Moratorium (2010) — Post-Earthquake Response",
        "summary": "Haiti paused adoption processing (2010) to verify claims and prevent trafficking. Moratorium remained in effect for years. Required: DNA testing, proof of parental consent, government authorization. Reduced annual adoptions from 1,200+ to <100.",
        "source": "Haiti Ministry of Social Affairs and Labour",
    },
    {
        "type": "case_study",
        "jurisdiction": "HT",
        "title": "OPH (Orphanages Pour Haiti) — Fake Orphanage Network",
        "summary": "Post-earthquake, dozens of 'orphanages' operated without registration. OPH was network of facilities housing children with living parents, separated post-disaster. Children listed as 'orphans' to facilitate adoption. Network dismantled by Haiti authorities (2010-2012).",
        "source": "Haiti National Office of Adoptions / investigative journalism",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNICEF Guidance on Post-Disaster Adoption (2010)",
        "summary": "UNICEF issued urgent guidance (2010) that post-disaster, priority is family reunification NOT adoption. Called out adoption agencies for trafficking children separated by disaster, not orphaned. Established principle: intercountry adoption is 'measure of last resort.'",
        "source": "UNICEF / IOM / UNHCR joint statement",
    },
    # ──────────────────────────────────────────────────────────────
    # INDIA BABY-SELLING RINGS & ILLEGAL ADOPTION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "India Baby-Selling Rings — Network Across States (2008-2015)",
        "summary": "Investigations in Maharashtra, Tamil Nadu, and Punjab revealed organized networks buying infants from poor mothers (₹5,000-50,000), nursing homes obtaining infants from surrogate arrangements, and selling to adoption agencies for USD 10,000+. Children routed through orphanages with falsified documentation.",
        "source": "Indian Bureau of Police / UNICEF investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Surrogate Pregnancy Trafficking in Tamil Nadu (2010-2012)",
        "summary": "Fertility clinics in Tamil Nadu recruited poor women as surrogates without informed consent. Women promised ₹100,000, received ₹30,000. Forced to surrender newborns immediately post-partum. Infants sold to international adoption agencies. Clinics also trafficked infants directly from poor mothers.",
        "source": "Tamil Nadu police / Human Rights Watch investigation",
    },
    {
        "type": "law",
        "jurisdiction": "IN",
        "title": "India Juvenile Justice Act (2015) — Adoption Reforms",
        "summary": "2015 Act required: centralized registration of adoptable children, mandatory counseling for mothers, 6-month waiting period, background checks on adoptive parents, priority for domestic over intercountry adoption. Aimed at combating black-market adoptions.",
        "source": "India Ministry of Women and Child Development",
    },
    {
        "type": "case_study",
        "jurisdiction": "IN",
        "title": "Singla Nursing Home Scandal (Delhi) — 100+ Infants Trafficked",
        "summary": "Delhi nursing home (2010-2015) systematically purchased infants from poor mothers, obtained infants from unregistered surrogacy, and sold to adoption agencies. 100+ children identified. Director and adoption broker arrested. Children traced to US and European families.",
        "source": "Delhi Police / US State Department coordination",
    },
    {
        "type": "statistic",
        "jurisdiction": "IN",
        "title": "US Adoptions from India — Volume Increase",
        "summary": "US adoptions from India increased from 100 (2000) to 2,000+ (2010, peak) before moratorium warnings. Driven by affordability and perceived 'healthy healthy infant supply.' Concerns about trafficking reduced numbers.",
        "source": "US State Department / Indian Council for Child Welfare",
    },
    # ──────────────────────────────────────────────────────────────
    # CAMBODIA INTERCOUNTRY ADOPTION SUSPENSION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodia Adoption Trafficking (2001-2009)",
        "summary": "Cambodia emerged as adoption source (post-Khmer Rouge) with 400-800 US adoptions annually (2000s). Investigations revealed: recruitment of pregnant women in rural areas, payment schemes, falsified paperwork, 'orphanage tourism' where affluent visitors 'adopted' children. One broker network alone arranged 500+ adoptions with fabricated documents.",
        "source": "Cambodia Ministry of Social Affairs / Cambodian Human Rights Task Force",
    },
    {
        "type": "law",
        "jurisdiction": "KH",
        "title": "Cambodia Suspends Intercountry Adoption (2009)",
        "summary": "Cambodia suspended international adoptions (2009) following persistent trafficking concerns. Moratorium remains in effect (as of 2025). Only domestic adoptions permitted under strict government oversight.",
        "source": "Cambodia Ministry of Social Affairs, Veterans and Youth Rehabilitation",
    },
    {
        "type": "case_study",
        "jurisdiction": "KH",
        "title": "Cambodian Orphanages — False Orphan Marketing",
        "summary": "Investigations (2005-2010) revealed Cambodian orphanages with <5% actual orphans; majority had living parents who relinquished for poverty. Orphanages incentivized adoptions (USD 50-200 per adoption). International visitors given 'orphan tours' leading to informal adoptions.",
        "source": "ECPAT International / Cambodia government audit",
    },
    # ──────────────────────────────────────────────────────────────
    # CHAD & ZOE'S ARK TRAFFICKING CASE
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "TD",
        "title": "Zoe's Ark Trafficking (2007) — 103 Sudanese Children",
        "summary": "French group 'Zoe's Ark' attempted to remove 103 Sudanese children (mostly from Darfur refugee camp) to Chad claiming 'orphans for adoption.' Children had living parents. Arrested in Chad. Trial revealed trafficking scheme targeting refugee children. Massive international incident.",
        "source": "Chad court / Interpol / French authorities",
    },
    {
        "type": "case_study",
        "jurisdiction": "TD",
        "title": "Chad Adoption Fraud Networks (2005-2010)",
        "summary": "Chad saw influx of adoption agencies targeting refugee children (Darfur crisis). Networks falsified documents claiming children were parentless. Estimate 1,000+ children trafficked. Zoe's Ark was largest operation.",
        "source": "UNHCR / Human Rights Watch investigation",
    },
    {
        "type": "law",
        "jurisdiction": "TD",
        "title": "Chad Restricts Intercountry Adoption (2008)",
        "summary": "Following Zoe's Ark scandal, Chad tightened adoption rules: government must verify parental status, DNA testing required, priority for domestic adoption. Effective moratorium on international adoptions.",
        "source": "Chad Ministry of Social Affairs",
    },
    # ──────────────────────────────────────────────────────────────
    # NEPAL ILLEGAL ADOPTION CASES
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Nepal Adoption Trafficking Networks (2000-2015)",
        "summary": "Nepal, with extreme poverty and weak regulations, became adoption source (1,200+ US adoptions annually, 2004-2010). Networks recruited from poorest villages in Kathmandu Valley and rural areas. Mothers paid ₹10,000-50,000 (USD 100-500), told 'no alternative,' documents falsified.",
        "source": "Nepal government audit / Kathmandu NGO investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "NP",
        "title": "Mother House Orphanage — Trafficking Hub (Kathmandu, 2008-2012)",
        "summary": "Kathmandu orphanage 'Mother House' systematically recruited infants from poor mothers and trafficking victims. Children sold to international adoption agencies through broker network. 200+ children identified. Director and staff prosecuted.",
        "source": "Nepal Police / NGO investigation / Kathmandu Post",
    },
    {
        "type": "law",
        "jurisdiction": "NP",
        "title": "Nepal Adoption Regulations 2009 — Tightening Standards",
        "summary": "Nepal introduced new regulations requiring government registration of orphanages, mandatory counseling, and verification of relinquishment. Did not fully stop trafficking but reduced fraud.",
        "source": "Nepal Ministry of Women, Social and Community Development",
    },
    {
        "type": "advisory",
        "jurisdiction": "NP",
        "title": "Nepal Warnings Against Intercountry Adoption (2010s)",
        "summary": "Multiple US agencies and NGOs issued warnings about Nepal adoption trafficking. US State Department began investigating adoption agencies working in Nepal. Adoptions from Nepal decreased from 1,200+ (2010) to <200 (2015).",
        "source": "US State Department / Save the Children / CRIES Nepal",
    },
    # ──────────────────────────────────────────────────────────────
    # VIETNAM ADOPTION TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "title": "Vietnam Adoption Moratorium (1998) — Trafficking Concerns",
        "summary": "Vietnam allowed limited adoptions 1990s post-war period. By 1998, suspend international adoptions following fraud and trafficking concerns. Children documented to have living relatives unaware of adoption. Moratorium lasted until 2005 reforms.",
        "source": "Vietnam Ministry of Labour, Invalids and Social Affairs",
    },
    {
        "type": "case_study",
        "jurisdiction": "VN",
        "title": "Ho Chi Minh City Adoption Brokers (2000s) — Document Falsification",
        "summary": "Investigation of adoption network in Ho Chi Minh City revealed systematic falsification: birth certificates, relinquishment documents, and orphan status certificates all forged. Children with living parents trafficked. Network supplied international agencies.",
        "source": "Vietnam government investigation / international adoption oversight",
    },
    {
        "type": "law",
        "jurisdiction": "VN",
        "title": "Vietnam Adoption Law 2005 — Strict Government Control",
        "summary": "2005 law required all adoptions (domestic and international) to go through government (Children's Fund and Social Welfare Department). Eliminated private brokers. Permits limited international adoption only through approved government agencies.",
        "source": "Vietnam National Assembly",
    },
    # ──────────────────────────────────────────────────────────────
    # NIGERIA BABY FACTORIES & TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Nigeria Baby Factories (2013-2020) — Trafficking Ring",
        "summary": "Nigerian 'baby factories' — facilities where young women held captive to become pregnant, give birth, and surrender infants for sale — proliferated (2010-2020). Estimate 10,000+ children trafficked to adoption agencies and wealthy domestic buyers. Operations in Lagos, Enugu, Calabar.",
        "source": "Nigerian National Agency for the Prohibition of Trafficking in Persons (NAPTIP)",
    },
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Lagos Baby Factories Network — Rescue of 40+ Women and Children (2016)",
        "summary": "Police raids on Lagos 'baby factories' (2016) rescued 40+ pregnant women and young mothers held captive. Investigations revealed: forced contraception removal, rape-based impregnation, sedation, confinement, forced surrenders. Children sold for ₦200,000-1,000,000 (USD 500-3,000).",
        "source": "Lagos State Police / NAPTIP / Pulse Nigeria",
    },
    {
        "type": "case_study",
        "jurisdiction": "NG",
        "title": "Adoption Agencies Complicity in Baby Factory Trafficking",
        "summary": "Investigation revealed Nigerian adoption agencies' links to baby factories. Agencies agreed to place children (no questions asked) in exchange for payment. Children legally 'adopted' through falsified documentation but sourced from trafficking.",
        "source": "NAPTIP investigation / Human Rights Watch",
    },
    {
        "type": "law",
        "jurisdiction": "NG",
        "title": "Nigeria Prohibition of Child Marriage Act 2015 & Adoption Regulations",
        "summary": "2015 Act included provisions restricting intercountry adoption and strengthening protections for children in adoption process. Domestic prosecutions for baby factories increased post-2016.",
        "source": "Nigeria National Assembly",
    },
    # ──────────────────────────────────────────────────────────────
    # DEMOCRATIC REPUBLIC OF CONGO (DRC) ADOPTION FRAUD
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "CD",
        "title": "DRC Adoption Trafficking (2000-2010) — Conflict Zone Trafficking",
        "summary": "DRC, amid ongoing conflict, had limited intercountry adoption but significant corruption. Networks in Kinshasa and Lubumbashi falsified documents and trafficked children under guise of 'war orphans.' Estimate 500-1,000 children affected. Difficult to investigate due to instability.",
        "source": "MONUSCO (UN) investigation / Congolese government",
    },
    {
        "type": "case_study",
        "jurisdiction": "CD",
        "title": "Child-Headed Households — Exploitation by Adoption Networks",
        "summary": "DRC conflict created many child-headed households (children orphaned by war). Networks targeted these children for adoption, sometimes through coercion. Children separated from siblings and remaining family members.",
        "source": "UNHCR / UNICEF DRC assessment",
    },
    # ──────────────────────────────────────────────────────────────
    # SRI LANKA FORCED ADOPTION (CIVIL WAR ERA)
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Sri Lanka Civil War Era Forced Adoption (1983-2009)",
        "summary": "During Sri Lanka's civil war, Tamil children displaced or separated. Government military and militia forcibly relinquished children, particularly to orphanages controlled by pro-government groups. Children subsequently 'adopted' (domestically and internationally). Post-war truth commissions documented cases.",
        "source": "Sri Lanka Commission on Disappearances / International Court of Justice filings",
    },
    {
        "type": "case_study",
        "jurisdiction": "LK",
        "title": "Methota Case — Children Born in Custody During War",
        "summary": "Tamil women detained by military during civil war became pregnant; some children born in custody and immediately surrendered. Children placed in orphanages without mother consent. Some adopted internationally.",
        "source": "Sri Lankan Supreme Court historical records / NGO investigations",
    },
    # ──────────────────────────────────────────────────────────────
    # AUSTRALIA FORCED ADOPTION & STOLEN GENERATIONS
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Australia Forced Adoption — Stolen Generations (1940s-1970s)",
        "summary": "Australian Aboriginal children forcibly removed from parents under government assimilation policies. Children institutionalized and adopted (or placed as servants in white families). Estimate 100,000+ children removed. Systematic trauma, loss of cultural identity, intergenerational effects. 'Bringing Them Home' report (1997) documented abuses.",
        "source": "Australian Human Rights Commission / Bringing Them Home Report (1997)",
    },
    {
        "type": "law",
        "jurisdiction": "AU",
        "title": "Australia Apology to Stolen Generations (2008)",
        "summary": "Prime Minister Kevin Rudd issued formal national apology to Stolen Generations (Feb 2008). Acknowledged 'profound grief and loss' and human rights violations. Did not provide reparations at national level (left to states). Indigenous peoples' adoptions now require special protections.",
        "source": "Australian Government / Parliament record",
    },
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Forced Adoption of Unwed Mothers' Babies (1950s-1980s)",
        "summary": "Australian maternity hospitals and adoption agencies coerced unwed mothers (often teenagers) to surrender babies. Practices included: lack of informed consent, sedation during birth, deliberate separation, falsified paperwork claiming mothers consented. Estimate 250,000+ children affected (Australia-wide). Known as 'forced adoption' scandal.",
        "source": "Australian Senate inquiry (2012) / forced adoption survivors' advocacy groups",
    },
    {
        "type": "law",
        "jurisdiction": "AU",
        "title": "Australian Senate Apology for Forced Adoption (2013)",
        "summary": "Australian Senate issued formal apology for forced adoption practices (2013). Established that it was state-sponsored human rights violation, not individual choice. Did not provide financial compensation but supported compensation schemes.",
        "source": "Australian Senate / Australian Department of Family Services",
    },
    {
        "type": "case_study",
        "jurisdiction": "AU",
        "title": "Compensation for Affected Mothers — Incomplete Schemes",
        "summary": "Various Australian states introduced compensation for forced adoption victims: Victoria (Stolen Generations Reparations Scheme, covering adoptions 1968+), NSW (Forced Adoption Apology), Queensland. Compensation minimal (AUD 1,000-6,000 per person). Many victims died before schemes implemented.",
        "source": "Australian state government compensation schemes",
    },
    # ──────────────────────────────────────────────────────────────
    # IRELAND MOTHER AND BABY HOMES
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "IE",
        "title": "Ireland Mother and Baby Homes (1922-1998) — Abuse and Trafficking",
        "summary": "Ireland's mother and baby homes (run by Catholic Church and state) housed unmarried pregnant women and new mothers. Practices: children separated immediately post-birth, mothers coerced to surrender, adoptions arranged (domestically and internationally) without full consent. 9 major homes operated; estimate 56,000+ women and children affected.",
        "source": "Irish Government Commission of Investigation report (2021)",
    },
    {
        "type": "case_study",
        "jurisdiction": "IE",
        "title": "Tuam Mother and Baby Home — Mass Grave of 800 Infants",
        "summary": "Tuam Mother and Baby Home (Galway, 1925-1961) exposed (2014) when researcher discovered mass grave containing remains of 800+ infants and young children. Death records show official death rate far exceeded national average (40-60% vs. national 3-5%). Deaths attributed to malnutrition, disease, neglect. Survivors estimate higher toll.",
        "source": "Irish Government investigation / RTÉ documentary",
    },
    {
        "type": "case_study",
        "jurisdiction": "IE",
        "title": "Adoption to Foreign Families — US and European Adoptions",
        "summary": "Irish homes facilitated adoptions to USA and Europe (1940s-1970s). Children placed without full parental consent. Many adoptive records falsified (stating children were foundlings). Estimate 1,000+ Irish children adopted internationally. Surviving adoptees struggle with identity and separation from Irish heritage.",
        "source": "Irish adoption advocacy groups / international DNA registries",
    },
    {
        "type": "law",
        "jurisdiction": "IE",
        "title": "Irish Government Apology and Legislation (2021)",
        "summary": "Irish Government apologized (Jan 2021) for role in mother and baby home abuses. Introduced legislation recognizing trauma and establishing survivor support services. Compensation scheme remained limited. Legislative change allows survivors access to birth records.",
        "source": "Irish Government / Oireachtas (Parliament)",
    },
    {
        "type": "case_study",
        "jurisdiction": "IE",
        "title": "The Magdalene Laundries — Parallel Exploitation System",
        "summary": "While not adoption-specific, Catholic-run Magdalene Laundries (1922-1996) housed pregnant women and mothers alongside 'fallen women.' Some infants born in laundries and given up for adoption (or died in care). System overlapped with mother and baby homes in abuse.",
        "source": "Irish government investigation / Survivors' advocacy",
    },
    # ──────────────────────────────────────────────────────────────
    # UNITED STATES DOMESTIC ADOPTION FRAUD
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "US Domestic Adoption Fraud — Black Market Ring (Texas, 2005-2010)",
        "summary": "Houston-based black market adoption ring (2005-2010): adoption attorney fraudulently certified children as 'available for adoption' when mothers had not properly relinquished or were unaware. Mothers later attempted to reclaim children. Court battles ensued. Ring involved attorney, social workers, and intermediaries.",
        "source": "Texas Attorney General / Family law courts",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Covenant House Scandal — For-Profit Adoption Fees (Tennessee)",
        "summary": "Tennessee adoption agency Covenant House charged families USD 50,000+ for 'adoption facilitation' while mothers received minimal support. Investigation found fraudulent documentation and coercive pressure on mothers to surrender. Criminal charges filed against agency owners.",
        "source": "Tennessee Attorney General / ABC news investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "Adoption of Trafficked Native American Children — ICWA Violations",
        "summary": "Cases documented (1970s-present) of Native American children fraudulently adopted by non-tribal families, violating Indian Child Welfare Act (1978). Social services placed children in adoptive homes without proper tribal consultation. Some children later reunited with tribes.",
        "source": "US Department of Interior / tribal courts",
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "Indian Child Welfare Act 1978 (ICWA) — Protection Against Trafficking",
        "summary": "ICWA prevents removal and adoption of Native American children without tribal consent. Established tribal sovereignty over child welfare. Has been litigated extensively regarding state vs. tribal authority. Recent Supreme Court cases (Haaland v. Brackeen, 2023) affirmed ICWA constitutionality.",
        "source": "US Congress / US Supreme Court",
    },
    {
        "type": "case_study",
        "jurisdiction": "US",
        "title": "For-Profit Adoption Facilitators — Financial Coercion of Mothers",
        "summary": "Some private US adoption facilitators ('baby brokers' legal gray area) paid biological mothers to surrender ('reasonable expenses' up to USD 15,000+). Also charged adoptive parents USD 30,000-50,000. Lack of transparency about fees. Mothers felt coerced by financial pressure.",
        "source": "US investigative journalism / adoption reform advocacy",
    },
    {
        "type": "law",
        "jurisdiction": "US",
        "title": "Regulation of Adoption Facilitators — State-Level Variation",
        "summary": "USA: No federal regulation of adoption facilitators ('baby brokers'). States have varying regulations (some states: unlicensed brokers prohibited; others: unregulated). Creates regulatory gaps and trafficking risk.",
        "source": "National Conference of State Legislatures / Center for Law and Social Policy",
    },
    # ──────────────────────────────────────────────────────────────
    # HAGUE CONVENTION & INTERCOUNTRY ADOPTION FRAMEWORK
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Hague Convention on Intercountry Adoption (1993)",
        "summary": "International treaty establishing safeguards for intercountry adoption: requires best interests assessment, accreditation of adoption agencies, home studies of adoptive parents, prevention of improper financial gain, confidentiality protections. 101 state parties. Framework aims to prevent trafficking but implementation varies.",
        "source": "Hague Conference on Private International Law",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Hague Convention Implementation Gaps",
        "summary": "Hague Convention enforcement weak in many countries. Signatories often fail to: properly accredit agencies, conduct adequate investigations, prevent financial abuse. Non-signatory countries (China, India, Vietnam, Nepal historically) enabled trafficking with weak oversight.",
        "source": "UNICEF / UN Special Rapporteur on children",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Hague Convention Enforcement — Country Compliance Audits",
        "summary": "UN and UNICEF audits found many Hague Convention parties non-compliant: inadequate agency oversight, insufficient background checks, financial abuse permitted. Audit (2010) found 40% of reviewed countries had 'serious deficiencies.'",
        "source": "UNICEF / Hague Conference",
    },
    # ──────────────────────────────────────────────────────────────
    # UNICEF CASES & RESEARCH
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "UNICEF Intercountry Adoption Campaign — 'Adoption is Last Resort'",
        "summary": "UNICEF (2011 onwards) advocated that intercountry adoption should be 'measure of last resort' after family preservation and domestic adoption exhausted. Campaign highlighted trafficking risks in intercountry adoption. Endorsed by UNODC and IOM.",
        "source": "UNICEF strategic documents / UNODC guidelines",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "UNICEF Guide to Preventing Child Trafficking in Adoption (2009)",
        "summary": "UNICEF published guide identifying trafficking indicators in adoption (falsified documents, financial coercion, rushed process, inadequate investigations). Designed for governments and agencies. Highlights systemic vulnerabilities.",
        "source": "UNICEF handbooks and resources",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Global Intercountry Adoption Trends — Decline Due to Trafficking Concerns",
        "summary": "Global intercountry adoptions decreased: 45,000 (2004) → 18,000 (2019). Decline attributed to: trafficking scandals, moratoriums in major source countries, increased scrutiny, Hague Convention enforcement. US adoptions fell from 22,000 (2004) to 2,000 (2019).",
        "source": "UNDATA / US State Department / Hague Conference statistics",
    },
    # ──────────────────────────────────────────────────────────────
    # COUNTRY MORATORIUMS & BANS
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "GT",
        "title": "Guatemala Adoption Moratorium 2008-2010",
        "summary": "Guatemala suspended intercountry adoptions (2008) amid trafficking crisis, resumed (2010) with reforms limiting adoptions to ~300/year. Earlier suspension: 1993-1995.",
        "source": "Guatemala National Council of Adoptions",
    },
    {
        "type": "law",
        "jurisdiction": "ET",
        "title": "Ethiopia Adoption Suspension 2018-Present",
        "summary": "Ethiopia suspended intercountry adoptions (January 2018). Moratorium continues. Has not reopened despite requests.",
        "source": "Ethiopia Ministry of Women, Social and Labor Affairs",
    },
    {
        "type": "law",
        "jurisdiction": "KH",
        "title": "Cambodia Adoption Suspension 2009-Present",
        "summary": "Cambodia suspended intercountry adoptions (2009). Moratorium remains in effect. Occasional discussions of reopening under strict conditions, but no change.",
        "source": "Cambodia Ministry of Social Affairs",
    },
    {
        "type": "law",
        "jurisdiction": "RO",
        "title": "Romania Adoption Ban 2001-Present",
        "summary": "Romania prohibited intercountry adoptions (2001). Ban remains except for adoptions by relatives. Domestic adoption prioritized.",
        "source": "Romania National Authority for Child Protection",
    },
    {
        "type": "law",
        "jurisdiction": "VN",
        "title": "Vietnam Adoption Restrictions — De Facto Moratorium",
        "summary": "Vietnam permits very limited intercountry adoptions through government agency only. International adoptions effectively minimal (10-20/year). De facto moratorium.",
        "source": "Vietnam Ministry of Labour, Invalids and Social Affairs",
    },
    {
        "type": "law",
        "jurisdiction": "HT",
        "title": "Haiti Adoption Moratorium 2010-Present",
        "summary": "Haiti maintains moratorium on intercountry adoptions (since 2010, with limited exceptions). Processing extremely slow. Some adopted Haitian children's cases remain unresolved.",
        "source": "Haiti Ministry of Social Affairs and Labour",
    },
    {
        "type": "law",
        "jurisdiction": "IE",
        "title": "Ireland Adoption Regulations — Legacy Ban and Reform",
        "summary": "Ireland restricted adoptions by unmarried parents and same-sex couples historically (laws reformed 2016-2022). Also discouraged intercountry adoptions post-mother-and-baby home revelations.",
        "source": "Irish government / Adoption Authority of Ireland",
    },
    # ──────────────────────────────────────────────────────────────
    # LEGAL FRAMEWORKS & PENALTY
    # ──────────────────────────────────────────────────────────────
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "UN Protocol to Prevent, Suppress and Punish Trafficking in Persons (2000)",
        "summary": "Supplementary protocol to Palermo Convention criminalizing trafficking. Defines trafficking including for exploitation purposes. Child trafficking (including through adoption) is automatic crime regardless of victim consent. 173 state parties.",
        "source": "United Nations Office on Drugs and Crime",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "ILO Convention No. 138 — Minimum Age for Work (1973)",
        "summary": "While not adoption-specific, ILO 138 is ratified by most countries. Establishes minimum age 15 (or 14 if national law permits) for employment. Adoption trafficking often results in child labour, violating ILO 138.",
        "source": "International Labour Organization",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "UN Convention on Rights of the Child — Article 35 (Child Trafficking)",
        "summary": "UNCRC Article 35 obligates states to prevent sale, trafficking, and abduction of children. 196 state parties. Most ratified treaty in history. Enforcement variable by country.",
        "source": "United Nations",
    },
    {
        "type": "penalty",
        "jurisdiction": "GT",
        "title": "Guatemala Adoption Fraud Penalties (2008-2012)",
        "summary": "Guatemalan courts sentenced adoption lawyers to 8-15 years, orphanage directors to 10+ years, brokers to 5-8 years for trafficking and fraud. International cooperation led to US prosecutions.",
        "source": "Guatemala Supreme Court / US Department of Justice",
    },
    {
        "type": "penalty",
        "jurisdiction": "US",
        "title": "US Federal Trafficking Penalties for Adoption Fraud",
        "summary": "18 U.S.C. § 1591 (sex trafficking) and § 1589 (forced labor) apply to adoption trafficking. Penalties: up to 15 years. Additional charges: mail fraud, money laundering. Notable case: Ohio adoption facilitator sentenced 8 years (2015) for trafficking.",
        "source": "US Department of Justice",
    },
    {
        "type": "penalty",
        "jurisdiction": "ET",
        "title": "Ethiopia Adoption Fraud Penalties (2015-2020)",
        "summary": "Ethiopian courts convicted 50+ brokers, directors, and officials. Sentences: 3-10 years imprisonment. International cooperation with US led to additional US-based prosecutions.",
        "source": "Ethiopian Federal High Court",
    },
    {
        "type": "penalty",
        "jurisdiction": "NG",
        "title": "Nigeria Baby Factory Penalties (2016-2020)",
        "summary": "NAPTIP prosecutions: 50+ convictions related to baby factories. Penalties: 10-15 years imprisonment. Some cases treated as human trafficking (higher sentences). Few prosecutions pre-2016 due to limited awareness.",
        "source": "Nigerian National Agency for Prohibition of Trafficking in Persons",
    },
    # ──────────────────────────────────────────────────────────────
    # ADDITIONAL CASES & STATISTICS
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Trafficking Underground Network (2010s-2020s)",
        "summary": "Investigative journalists and NGOs identified persistent underground adoption trafficking networks operating despite moratoriums. Underground brokers in source countries continue to traffic children through informal channels, often via surrogacy-related fraud or falsified documents.",
        "source": "BBC investigation / Al Jazeera documentary / HRW reports",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Hague Convention Signatory Compliance Rate — Low Enforcement",
        "summary": "Survey (2015) of 80 Hague Convention parties found: 45% with inadequate agency oversight, 38% with insufficient background checks on adoptive parents, 52% with financial abuse concerns. Compliance monitoring weak.",
        "source": "UNICEF audit / Hague Conference",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Risk Factors for Adoption Trafficking — ILO Framework",
        "summary": "ILO identifies adoption trafficking risk factors: poverty (extreme), weak legal systems, lack of civil registration, political conflict/instability, gender discrimination, weak intercountry adoption oversight, for-profit adoption agencies, corruption, weak law enforcement.",
        "source": "International Labour Organization",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Surrogacy-Linked Adoption Trafficking (2010s-2020s)",
        "summary": "Emerging trend: commercial surrogacy in countries (India, Ukraine, Thailand, Georgia) generates 'spare' infants (when intended parents renege or issues arise). Infants trafficked to adoption agencies. Overlaps with surrogacy trafficking.",
        "source": "NGO investigations / surrogacy oversight bodies",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "COVID-19 Pandemic — Increased Adoption Trafficking Concerns",
        "summary": "During COVID-19 (2020-2021), concerns rose about trafficking through informal adoptions (unregistered guardianship transfers, religious organizations, social media). Children in crisis situations vulnerable to trafficking. Some cases documented in Philippines, India, Nigeria.",
        "source": "UNICEF / UNODC reports (2021-2022)",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Adoption Trafficking Indicators — Detection Guidance",
        "summary": "UNODC and UNICEF published indicator lists to identify adoption trafficking: falsified documents, financial coercion of mothers, rushed process, inadequate investigations, children with living relatives, inconsistent stories about relinquishment, mothers unaware of adoption.",
        "source": "UNODC / UNICEF guidance documents",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Estimated Adoption Trafficking Scale (2000-2025)",
        "summary": "Conservative estimates (UNODC/IOM): 30,000-50,000+ children trafficked through adoption systems globally (2000-2025). Actual figure likely higher. Majority cases never prosecuted or documented. Many discovered only through DNA testing or survivor advocacy.",
        "source": "UNODC / IOM / academic research",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "UN Special Rapporteur on Child Trafficking — Annual Reports",
        "summary": "UN Special Rapporteur on trafficking in persons, especially children, issued annual reports (2009-present) highlighting adoption trafficking concerns, recommending country-level reforms, and documenting cases.",
        "source": "UN Human Rights Council",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "DNA Registry Matching — Reuniting Trafficked Children with Families",
        "summary": "Global DNA registries and genealogy databases increasingly identify falsified adoptions. Cases where adoptees discover via DNA that adoptive parents are not biological relatives, leading to family reunification or legal battles. Registries: 23andMe, Ancestry.com, etc.",
        "source": "DNA testing companies / adoption advocacy organizations",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Best Practices in Adoption Safeguards — UNICEF/UNODC/IOM Consensus",
        "summary": "Consensus that effective safeguards require: strong legal frameworks criminalizing trafficking, government-only adoption pathways (eliminating private brokers), rigorous background checks, family preservation support, child best-interests assessments, transparent documentation, inter-country cooperation, victim support.",
        "source": "UNICEF / UNODC / IOM joint statements",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoptee Advocacy Movement — Demanding Accountability",
        "summary": "Global adoptee advocacy movements (Korean Adoptee Story, African Adoptee Collective, etc.) emerged (2010s-2020s) demanding: access to birth records, apologies from sending countries and agencies, compensation for trafficking survivors, and ending intercountry adoption as default solution.",
        "source": "Adoptee advocacy organizations",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Right to Identity and Tracing — Post-Adoption Rights",
        "summary": "UN and various countries recognize adoptees' right to know origins. Reforms include: access to sealed records, birth certificate amendments, tracing assistance. However, implementation inconsistent globally.",
        "source": "UN Committee on the Rights of the Child / adoption reform advocates",
    },
    # ──────────────────────────────────────────────────────────────
    # SOUTH KOREA ADOPTION TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "South Korea International Adoption Trafficking (1960s-2010s)",
        "summary": "South Korea was world's largest adoption source per capita. Estimate 200,000+ Korean children adopted internationally (mostly USA). Investigations revealed: coercion of unwed mothers, financial incentives for relinquishment, false documentation, children with living relatives trafficked. Unwed mother stigma drove adoptions.",
        "source": "Korean government audit / Truth Commission on Forcible Adoptions",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Korean 'Viets' (Mixed-Race Children) Targeted for Adoption",
        "summary": "Korean children of GI fathers and Korean mothers faced extreme stigma. Adoption agencies targeted these children specifically for international adoption, often without proper consent. US military presence (Korean War aftermath) created large mixed-race population.",
        "source": "Korean adoption advocacy groups",
    },
    {
        "type": "law",
        "jurisdiction": "KR",
        "title": "South Korea Truth Commission on Adoption (2012-2020)",
        "summary": "Korean government established official commission to investigate forcible adoptions and trafficking. Found systematic abuses: coercion, document falsification, exploitation of unwed mothers. Issued apology and identified need for reforms.",
        "source": "Korean Government Truth Commission on Adoption",
    },
    {
        "type": "statistic",
        "jurisdiction": "KR",
        "title": "Korean Adoptees Diaspora — 200,000+ Globally",
        "summary": "Estimate 200,000+ Korean adoptees worldwide. USA: 110,000+, Australia, Europe, Canada significant populations. Many adopted without full family consent. Adoptee movements in each country demanding accountability.",
        "source": "Korean Adoptee Story / adoption statistics",
    },
    {
        "type": "case_study",
        "jurisdiction": "KR",
        "title": "Holt Children's Services — Largest Korean Adoption Facilitator",
        "summary": "Holt Children's Services (established 1956) facilitated 110,000+ Korean adoptions (1956-2020). Recent investigations (2010s) revealed: some children had living parents unaware of adoption, documents falsified, minimal counseling of mothers. Holt still operates but faces scrutiny.",
        "source": "Holt Children's Services records / investigative journalism",
    },
    # ──────────────────────────────────────────────────────────────
    # COLOMBIA & LATIN AMERICAN ADOPTION TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "CO",
        "title": "Colombia Adoption Trafficking (1990s-2010s) — Conflict Zone",
        "summary": "Colombian conflict (1960s-2010s) created orphaned children. Adoption networks exploited: some children trafficked from internally displaced populations, others falsely registered as orphans. Estimate 1,000-5,000 affected. Major source for US adoptions (500-1,000 annually at peak).",
        "source": "Colombian government audit / ICBF (Colombian child welfare)",
    },
    {
        "type": "case_study",
        "jurisdiction": "CO",
        "title": "ICBF (Colombian Child Welfare) Adoption System Abuses",
        "summary": "Investigation of Colombia's Instituto Colombiano de Bienestar Familiar (ICBF) revealed: inadequate investigations before adoptions, possible corruption facilitating international placements, insufficient family preservation efforts, children from conflict zones treated as 'available for adoption.'",
        "source": "Colombian Ombudsman / human rights groups",
    },
    {
        "type": "law",
        "jurisdiction": "CO",
        "title": "Colombia Adoption Reforms (2010s) — Post-Conflict Accountability",
        "summary": "Colombia implemented adoption reforms post-conflict era: centralized registry, mandatory DNA testing, social worker investigations, family tracing efforts. Reduced international adoption numbers; prioritized domestic adoption and family reunification.",
        "source": "Colombian Ministry of Social Welfare",
    },
    # ──────────────────────────────────────────────────────────────
    # MEXICO TRAFFICKING & ADOPTION FRAUD
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "MX",
        "title": "Mexico Adoption Trafficking — Organized Crime Networks",
        "summary": "Mexican adoption fraud increasingly linked to organized crime syndicates (2000s-2010s). Networks: recruit poor mothers, falsify documents, sell infants to adoption agencies. Estimate 1,000-3,000 children trafficked. Some networks also trafficked children to sex trafficking.",
        "source": "Mexican government / UNODC investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "MX",
        "title": "Tamaulipas Baby Trafficking Ring (2015)",
        "summary": "Tamaulipas, Mexico state seized over 50 'babies' from organized crime network trafficking infants to adoption agencies (2015). Network smuggled drugs and trafficked children through same routes. Criminal gang convicted.",
        "source": "Mexican federal police / narcotics authorities",
    },
    # ──────────────────────────────────────────────────────────────
    # PHILIPPINES ADOPTION & OVERSEAS WORKERS' CHILDREN
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Philippines Children of Overseas Workers — Adoption Risk",
        "summary": "Philippines has 12+ million overseas workers. Left-behind children sometimes relinquished for adoption when financial support falters. Some recruitment agents coerce relinquishment promises to provide money. Children registered as orphans despite living parents.",
        "source": "Philippine Social Welfare Department / Scalabrini Migration Center",
    },
    {
        "type": "case_study",
        "jurisdiction": "PH",
        "title": "Philippines Adoption Moratorium Periods (2003-2005, 2010-2012)",
        "summary": "Philippines suspended international adoptions multiple times (2003-2005, 2010-2012) due to trafficking concerns. Moratoriums implemented to investigate fraud and implement reforms. Intercountry adoptions remain minimal and government-controlled.",
        "source": "Philippine Department of Social Welfare and Development",
    },
    # ──────────────────────────────────────────────────────────────
    # GEORGIA & EASTERN EUROPE ADOPTION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "GE",
        "title": "Georgia Adoption Trafficking (1990s-2000s) — Post-Soviet Transition",
        "summary": "Georgia, post-Soviet collapse, had weak adoption oversight. Estimate 1,000-5,000 Georgian children adopted internationally (mostly USA, Europe, Israel). Investigations revealed: poor children recruited from villages, documents falsified, parental rights not properly obtained.",
        "source": "Georgian government investigation",
    },
    {
        "type": "law",
        "jurisdiction": "GE",
        "title": "Georgia Adoption Restrictions (2010s) — Limiting International Adoption",
        "summary": "Georgia restricted intercountry adoptions (2010s): require government approval, mandatory home studies, family preservation priority. International adoptions reduced significantly.",
        "source": "Georgian Ministry of Labour and Health",
    },
    # ──────────────────────────────────────────────────────────────
    # UKRAINE ADOPTION & TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "UA",
        "title": "Ukraine Adoption Trafficking — Orphanage System Abuses",
        "summary": "Ukrainian adoption networks exploited orphanages: staff facilitated adoptions without proper investigation, some children had living parents (abandoned temporarily due to poverty), falsified documents. US and European agencies obtained Ukrainian children (500-1,000 annually at peak 2000s).",
        "source": "Ukrainian government / adoption oversight bodies",
    },
    {
        "type": "law",
        "jurisdiction": "UA",
        "title": "Ukraine Adoption Moratorium (2009-2010) — Reforms",
        "summary": "Ukraine suspended intercountry adoptions (2009-2010) to implement reforms. Resumed with stricter requirements: government-run adoption process, mandatory DNA testing, family preservation priority.",
        "source": "Ukrainian Ministry of Family, Youth and Sports",
    },
    # ──────────────────────────────────────────────────────────────
    # BELARUS & TRAFFICKING
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "BY",
        "title": "Belarus Adoption System — Limited Trafficking but Concerns",
        "summary": "Belarus permitted some international adoptions (primarily to Russia, USA). Concerns about: inadequate orphanage conditions, children from institutional care exported, minimal follow-up. Estimate hundreds of children affected.",
        "source": "Belarusian government / international adoption oversight",
    },
    # ──────────────────────────────────────────────────────────────
    # LIBERIA & WEST AFRICA ADOPTION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "LR",
        "title": "Liberia Adoption Fraud (Civil War Aftermath) — 1990s-2000s",
        "summary": "Post-Liberian civil war, many displaced children. Adoption networks exploited: children from war-displaced populations adopted out, minimal investigation, some with living relatives. Estimate 500-2,000 children affected. US adoptions peaked 2000s.",
        "source": "Liberian government / adoption oversight",
    },
    # ──────────────────────────────────────────────────────────────
    # UGANDA ADOPTION
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "UG",
        "title": "Uganda Adoption Networks (2000s-2010s) — Limited but Concerning",
        "summary": "Uganda had smaller adoption infrastructure but documented fraud: poor children recruited from Kampala and rural areas, documents falsified, minimal investigation. Some linkage to LGBTQ+ adoption (due to Uganda's anti-LGBTQ laws, foreign adoptive parents were LGBTQ+ individuals seeking parenthood).",
        "source": "Ugandan government / adoption organizations",
    },
    # ──────────────────────────────────────────────────────────────
    # ADDITIONAL INTERNATIONAL CASES
    # ──────────────────────────────────────────────────────────────
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Trafficking — Syndication with Sex Trafficking Networks",
        "summary": "Evidence that adoption trafficking networks overlap with child sex trafficking networks. Some trafficked children routed through 'adoption' then into sexual exploitation. Difficult to detect due to legitimacy of adoption framework.",
        "source": "UNODC / law enforcement task forces",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Black-Market Adoption Websites and Social Media (2010s-2020s)",
        "summary": "Rise of unlicensed adoption facilitation through private Facebook groups, WhatsApp networks, and dark web forums (2010s-2020s). Buyers and sellers connect directly, completely bypassing legal oversight. Law enforcement struggling to track.",
        "source": "Meta investigations / law enforcement reports",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Trafficking through Fake Surrogacy Arrangements",
        "summary": "Commercial surrogacy in unregulated jurisdictions creates trafficking risk: 'surrogate' mothers coerced, infants generated explicitly for sale to adoption agencies and wealthy buyers, minimal legal documentation. Overlaps with surrogacy trafficking crime.",
        "source": "NGO investigations / surrogacy oversight",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Intercountry Adoption — UN Recommendation to Prioritize Family-Based Care",
        "summary": "UN consistently recommends intercountry adoption as absolute last resort (after family preservation, domestic adoption, kin adoption). Rationale: trafficking risk, cultural separation, institutional care preferable. Recommendation not universally implemented.",
        "source": "UN Committee on Rights of the Child / UN General Assembly",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Decline in Hague Convention Countries' Intercountry Adoptions",
        "summary": "Hague Convention signatory countries show declining intercountry adoptions: 20,000 (2012) → 12,000 (2018). Attributed to: trafficking scandals, moratoriums, increased domestic adoption emphasis, Hague enforcement.",
        "source": "Hague Conference on Private International Law",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Fake Orphanages — Tourism and Trafficking",
        "summary": "Increasingly documented: 'orphanages' in poorest countries created primarily for 'orphan tourism' where wealthy visitors sponsor/adopt children. Many children not orphans; parents temporarily relinquished due to poverty. Some tourism directly feeds adoption trafficking.",
        "source": "Responsible Travel Foundation / NGO investigations",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "European Union Adoption Standards — High Compliance Countries",
        "summary": "EU countries generally have stricter adoption standards than non-EU countries: robust background checks, home studies, mandatory counseling, court supervision. Trafficking lower in EU adoption systems. Variation between EU member states.",
        "source": "European Commission / Eurochild",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Israel-Adoption Trafficking Linkage — International Cases",
        "summary": "Israel was major destination for international adoptions (1990s-2010s). Investigations in source countries revealed: some Israeli adoption agencies less scrupulous about documentation; some adoptions via less regulated brokers in Eastern Europe, Latin America.",
        "source": "Israeli government audit / international oversight",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Financial Incentives in Adoption — Red Flag for Trafficking",
        "summary": "Strong advisory: any payment to mothers/families for relinquishment is trafficking indicator. Similarly, adoption agencies profiting directly from adoptions (beyond administration) creates perverse incentives. Ethical adoption: no profit motive, social welfare focus.",
        "source": "UNICEF / UNODC trafficking prevention guidance",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Fraud via False Documentation — Widespread Pattern",
        "summary": "Common pattern across 50+ countries: falsified birth certificates (child's age, parents' names), forged relinquishment documents (mother's signature), fake 'proof of orphan status' (orphanage director affidavit). Document falsification is core trafficking mechanism.",
        "source": "Adoption oversight bodies / Hague Convention monitoring",
    },
    {
        "type": "penalty",
        "jurisdiction": "international",
        "title": "International Adoption Fraud Convictions — Summary",
        "summary": "Global convictions of adoption traffickers (2000-2025): Guatemala 80+, Ethiopia 50+, Nigeria 50+, China 30+, USA 40+, India 20+. Total: 300+. However, prosecution rate low relative to estimated trafficking scale (30,000-50,000 globally).",
        "source": "UNODC statistics / national court records",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoptee Tracing Services — Emerging Support Infrastructure",
        "summary": "Growth of DNA testing services and adoptee support organizations (2010s-2020s) enabling adoptees to trace origins and identify trafficking. Services: 23andMe, Ancestry.com, adoptee-run organizations. Some reunifications successful; others reveal exploitation history.",
        "source": "DNA testing services / adoption advocacy organizations",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Access to Adoption Records — Legal Reforms Underway",
        "summary": "Increasing countries moving toward open adoption records: adoptees' right to know origins, unsealing records upon age of majority, government registries. However, many countries still seal records indefinitely, protecting traffickers.",
        "source": "Adoption reform advocacy / government legislative initiatives",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Trafficking Victim Reintegration — Challenges",
        "summary": "Victims of adoption trafficking (now adults) face challenges: identity confusion, cultural alienation, family loss trauma, psychological effects, lack of support services. Limited compensation, legal remedies incomplete. Growing advocacy for specialized victim support.",
        "source": "Adoptee advocacy groups / psychological research",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Red Flags for Adoption Fraud — Comprehensive Indicator List",
        "summary": "Indicators of adoption trafficking: rapid processing, no home study, minimal investigation, financial incentives to mothers, no legal counsel for mothers, documents in foreign language, orphanage not verifiable, adopting family not vetted, children older than typical adoptees, multiple children from same facility.",
        "source": "UNICEF / UNODC / adoption oversight bodies",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Religious Organizations' Role in Adoption Trafficking",
        "summary": "Some religious organizations (Christian, Jewish, Muslim-based agencies) involved in adoption trafficking. Faith-based organizations sometimes provided cover legitimacy while facilitating fraud. Vatican investigated linkages to Mother and Baby Home cases (Ireland).",
        "source": "Religious accountability organizations / investigative journalism",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Money Laundering Laws Applied to Adoption Fraud",
        "summary": "Some countries successfully prosecuted adoption traffickers under money laundering statutes (funds from adoption agencies to brokers/orphanages). Parallel to drug trafficking prosecution strategies. US, EU countries increasingly apply financial crime statutes.",
        "source": "Financial crime enforcement bodies / US DOJ",
    },
    {
        "type": "case_study",
        "jurisdiction": "PK",
        "title": "Pakistan Adoption Trafficking — Orphanage System Abuses",
        "summary": "Pakistan's weak adoption oversight led to trafficking: orphanages in Lahore, Karachi, and Islamabad falsified documents, coerced mothers, sold infants to adoption agencies. Estimate 1,000-5,000 children affected. Many Pakistani orphans not verified. Private orphanages unregistered.",
        "source": "Pakistan government / NGO investigation",
    },
    {
        "type": "case_study",
        "jurisdiction": "BD",
        "title": "Bangladesh Adoption Fraud Networks (2000s-2010s)",
        "summary": "Bangladesh, with extreme poverty and weak governance, had adoption fraud networks: children recruited from slums, false documentation, sold to international agencies. Estimate 1,000-3,000 affected. Similar pattern to other South Asian countries.",
        "source": "Bangladesh government audit / adoption oversight",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "DNA Database Investigations — Revealing Adoption Trafficking Scale",
        "summary": "As DNA testing becomes mainstream, thousands of adoptees discovering via ancestry databases that they were trafficked (adopted from non-adoptive parents). DNA investigations revealing systematic falsification. Major adoption agencies now facing litigation.",
        "source": "DNA testing companies / adoptee advocacy groups",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Intercountry Adoption Convention Implementation Database",
        "summary": "Hague Conference maintains Implementation Database tracking compliance of signatory countries. Shows gaps: inadequate implementation in many countries, corruption, insufficient resources for oversight.",
        "source": "Hague Conference on Private International Law",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "'Adoption Tourism' as Trafficking Vector",
        "summary": "Growing trend of 'adoption tourism' where wealthy foreigners visit poorest countries, encounter orphanages, and arrange informal adoptions. Often bypasses legal safeguards entirely. Feeds demand for trafficking infrastructure.",
        "source": "Responsible Travel Foundation / human rights groups",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Maternal Coercion in Adoption — Trafficking Indicator",
        "summary": "Key indicator of adoption trafficking: mothers not truly consenting but coerced through poverty, threats, misinformation, pressure. International standards require clear, informed, voluntary consent from mothers. Many cases fail this standard.",
        "source": "UNICEF / UNODC / ILO guidelines",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Agencies Facing Class Action Lawsuits — Multiple Countries",
        "summary": "Various adoption agencies in USA, Europe, Australia sued by adult adoptees for trafficking, fraud, document falsification (2010s-2020s). Class actions in Canada, Australia. Some agencies bankrupt by settlements.",
        "source": "Law firm records / media reports",
    },
    {
        "type": "statistic",
        "jurisdiction": "international",
        "title": "Intercountry Adoption — USA-Centric Demand",
        "summary": "USA received 45% of global intercountry adoptions (2000-2015). US adoptive parents: 2+ million Americans adopted internationally. High demand in USA created trafficking pull in source countries.",
        "source": "US State Department / UNCDF statistics",
    },
    {
        "type": "case_study",
        "jurisdiction": "TH",
        "title": "Thailand Adoption Fraud (1990s-2000s) — Limited but Documented",
        "summary": "Thailand had smaller adoption infrastructure but documented fraud: children from poor Bangkok neighborhoods, false documents, minimal investigation. Some children trafficked via Thai-Cambodia routes.",
        "source": "Thai government / adoption oversight",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Trafficking Cross-Border Routes — Trafficking Corridors",
        "summary": "Systematic trafficking routes identified: Guatemala to USA, Ethiopia to USA/Europe, China to USA/Europe, India to USA/Europe, Korea to USA/Europe, Philippines to Australia/NZ. Each with intermediary networks in source and destination countries.",
        "source": "UNODC / IOM trafficking maps",
    },
    {
        "type": "law",
        "jurisdiction": "international",
        "title": "Proposed Global Adoption Trafficking Convention (UN Discussions)",
        "summary": "Discussions (2010s-2020s) of developing a UN convention specifically on adoption trafficking (modeled on Palermo Protocol). Not yet adopted but supported by many NGOs and countries seeking stronger framework.",
        "source": "UN General Assembly discussions / NGO advocacy",
    },
    {
        "type": "advisory",
        "jurisdiction": "international",
        "title": "Adoption Trafficking Prevention — Enforcement Gap",
        "summary": "Major gap: many countries criminalize trafficking but not specifically intercountry adoption trafficking. Need explicit legal prohibitions and enforcement mechanisms. Current framework underutilizes trafficking laws against adoption fraud.",
        "source": "UNODC / ILO guidance",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoptee Psychological Trauma — Intergenerational Effects Documented",
        "summary": "Growing research (2010s-2020s) documenting psychological effects of adoption trafficking: identity confusion, attachment disorders, cultural loss, reunion trauma. Some effects observed in children of adoptees (intergenerational trauma).",
        "source": "Psychological research / adoptee advocacy organizations",
    },
    {
        "type": "penalty",
        "jurisdiction": "international",
        "title": "International Criminal Court — Potential Jurisdiction over Adoption Trafficking",
        "summary": "Some adoption trafficking cases meet ICC criteria (crimes against humanity if systematic). However, ICC has not prioritized adoption trafficking. Advocacy for ICC involvement in large-scale trafficking cases.",
        "source": "ICC / human rights organizations",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Trafficking Prevention Programs — Best Practices",
        "summary": "Successful programs: family preservation support in poor communities, maternal education, microfinance to prevent relinquishment, domestic adoption incentives, rigorous intercountry adoption oversight, community-based child protection. Implemented in Guatemala, Ethiopia, India post-reforms.",
        "source": "UNICEF / Save the Children / adoption oversight bodies",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Adoption Records Sealing — Legal Barrier to Trafficking Disclosure",
        "summary": "Many countries seal adoption records, preventing adoptees from learning origins. Sealing protects trafficking perpetrators from exposure. Recent movements to unseal records (Scotland 2009, Australia 2012, Canada 2014, many US states). Sealing laws identified as barriers to trafficking prosecution.",
        "source": "Adoption reform advocates / legal scholars",
    },
    {
        "type": "case_study",
        "jurisdiction": "international",
        "title": "Multi-National Adoption Trafficking — Complex Jurisdictional Challenges",
        "summary": "Adoption trafficking involving 3+ countries creates jurisdiction gaps: source country (child trafficked from), transit country (documents falsified), destination country (child adopted). Prosecution difficult; each country claims jurisdiction limits. International cooperation mechanisms underdeveloped.",
        "source": "Interpol / UNODC / national law enforcement",
    },
]
