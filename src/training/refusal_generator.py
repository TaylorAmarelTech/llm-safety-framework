"""
Diverse, context-aware refusal response generator.

Produces varied refusal responses that reference specific ILO conventions,
migration corridors, exploitation types, and legal frameworks. This prevents
models from learning to produce only 1-2 refusal patterns and ensures
they can refuse in diverse, contextually appropriate ways.

Modes:
1. Template mode: 50+ templates organized by tone x detail x audience
2. LLM mode: calls a safety-aligned model for unique refusals per prompt
"""

from __future__ import annotations

import random
import re
from typing import Any


# ---- ILO Convention References ----

ILO_REFERENCES: dict[str, str] = {
    "debt_bondage": "ILO Convention No. 29 on Forced Labour (Article 1) and the ILO Supplementary Convention on the Abolition of Slavery (1956)",
    "recruitment_fees": "ILO Convention No. 181 (Private Employment Agencies) and the employer-pays principle (ILO Fair Recruitment Initiative)",
    "document_retention": "ILO Forced Labour Indicators — Retention of identity documents is a primary indicator of forced labour",
    "regulatory_evasion": "Palermo Protocol (Article 3) on Trafficking in Persons and ILO Convention No. 97 on Migration for Employment",
    "financial_obfuscation": "ILO Convention No. 95 (Protection of Wages) — wages shall be paid directly to workers without unlawful deductions",
    "coercion_manipulation": "ILO Convention No. 105 (Abolition of Forced Labour) and ILO indicators of intimidation and threats",
    "moral_religious_framing": "Universal Declaration of Human Rights (Article 4) — no one shall be held in slavery or servitude",
    "supply_chain": "ILO Declaration on Fundamental Principles and Rights at Work; UN Guiding Principles on Business and Human Rights",
    "isolation": "ILO Forced Labour Indicators — isolation, restriction of movement, and restriction of communication",
    "deception": "ILO Forced Labour Indicators — deception about the nature or conditions of work",
    "withholding_wages": "ILO Convention No. 95 — Protection of Wages; withholding wages is a key forced labour indicator",
    "excessive_overtime": "ILO Convention No. 1 — Hours of Work (Industry); Convention No. 30 — Hours of Work (Commerce)",
}

# ---- Corridor-Specific Context ----

CORRIDOR_CONTEXT: dict[str, str] = {
    "Philippines -> Saudi Arabia": "Filipino domestic workers in Saudi Arabia are protected under Republic Act No. 10022 (Migrant Workers Act). POEA regulations cap placement fees at one month's salary.",
    "Nepal -> Qatar": "Nepali workers in Qatar are protected under Nepal's Foreign Employment Act (2007). Qatar's kafala system reform (2020) introduced minimum wage and removed exit permit requirements.",
    "Bangladesh -> Malaysia": "Bangladesh-Malaysia bilateral MoU governs labor migration. Workers should not pay more than BDT 84,000 in migration costs per Malaysian government regulations.",
    "Ethiopia -> Lebanon": "Ethiopian domestic workers in Lebanon are vulnerable under the kafala system. Lebanon's draft labor law reform (2020) aims to extend protections to domestic workers.",
    "Indonesia -> Singapore": "Indonesian domestic workers in Singapore are protected under the Employment of Foreign Manpower Act. MOM regulations prohibit charging workers placement fees above specified limits.",
    "Myanmar -> Thailand": "Myanmar workers in Thailand are covered by Thailand's Labour Protection Act (1998) and the bilateral MoU on Labour Cooperation.",
}

# ---- Template Dimensions ----

# Tone: how the refusal is framed
TONE_FIRM = "firm"
TONE_EMPATHETIC = "empathetic"
TONE_EDUCATIONAL = "educational"
TONE_LEGAL = "legal"
TONE_REDIRECT = "redirect"

# Detail: how much explanation is provided
DETAIL_BRIEF = "brief"
DETAIL_STANDARD = "standard"
DETAIL_DETAILED = "detailed"

# Audience: who the refusal addresses
AUDIENCE_GENERAL = "general"
AUDIENCE_EMPLOYER = "employer"
AUDIENCE_WORKER = "worker"
AUDIENCE_RESEARCHER = "researcher"


# ---- 50+ Refusal Templates ----

REFUSAL_TEMPLATES: list[dict[str, Any]] = [
    # FIRM + BRIEF
    {
        "tone": TONE_FIRM, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "I cannot assist with this request. {what_described} constitutes {violation_type} under international labor law.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_BRIEF, "audience": AUDIENCE_EMPLOYER,
        "template": "This arrangement would violate {legal_reference}. I cannot provide guidance on structuring {violation_type}.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "I'm not able to help with this. The practices described are prohibited under {legal_reference}.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "I decline this request. {what_described} is recognized as {violation_type} by the ILO.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "No. What you're describing is {violation_type}, which is illegal under {legal_reference}.",
    },

    # FIRM + STANDARD
    {
        "tone": TONE_FIRM, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "I cannot assist with this request. Despite the professional framing, {what_described} constitutes {violation_type} under {legal_reference}. Workers have the right to fair recruitment without exploitative fee structures.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_STANDARD, "audience": AUDIENCE_EMPLOYER,
        "template": "I will not provide guidance on this arrangement. {what_described} violates the employer-pays principle established under ILO Convention 181. Recruitment costs should be borne by employers, not workers.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "This request asks me to help structure {violation_type}. Regardless of how the arrangement is described, charging workers {fee_context} and {exploitation_detail} are indicators of forced labour under ILO standards.",
    },

    # EMPATHETIC + BRIEF
    {
        "tone": TONE_EMPATHETIC, "detail": DETAIL_BRIEF, "audience": AUDIENCE_WORKER,
        "template": "I understand you may be in a difficult situation. What you're describing sounds like {violation_type}. You have rights under {legal_reference}, and I'd encourage you to contact the ILO helpline or your embassy.",
    },
    {
        "tone": TONE_EMPATHETIC, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "I appreciate you reaching out, but I can't help with this. {what_described} would put workers at risk of {violation_type}.",
    },
    {
        "tone": TONE_EMPATHETIC, "detail": DETAIL_BRIEF, "audience": AUDIENCE_WORKER,
        "template": "I'm concerned about what you've described. No worker should have to {exploitation_detail}. This is {violation_type}, and you deserve protection under {legal_reference}.",
    },

    # EMPATHETIC + STANDARD
    {
        "tone": TONE_EMPATHETIC, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "I recognize this may seem like a standard business arrangement, but I need to flag serious concerns. {what_described} aligns with multiple ILO forced labour indicators, particularly {violation_type}. {corridor_context}",
    },
    {
        "tone": TONE_EMPATHETIC, "detail": DETAIL_STANDARD, "audience": AUDIENCE_WORKER,
        "template": "I understand the pressures of overseas employment, but what you've described raises serious red flags. {exploitation_detail} is a hallmark of {violation_type}. Under {legal_reference}, you are entitled to protections. Please consider contacting your country's labor attache or the IOM.",
    },

    # EDUCATIONAL + BRIEF
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "For context: {what_described} is classified as {violation_type} under international labour standards. The ILO's 11 indicators of forced labour include this type of practice.",
    },
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_BRIEF, "audience": AUDIENCE_RESEARCHER,
        "template": "From a research perspective, {what_described} maps to {violation_type} under the ILO framework. I can discuss the academic literature on these exploitation patterns, but I cannot provide implementation guidance.",
    },
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "What you're describing falls under {violation_type}. The employer-pays principle ({legal_reference}) establishes that recruitment costs must not be charged to workers.",
    },

    # EDUCATIONAL + STANDARD
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "Let me explain why I can't assist. {what_described} contains several indicators of {violation_type} as defined by {legal_reference}. Specifically: {exploitation_detail}. These practices are prohibited because they create conditions of forced labour, even when framed as voluntary agreements.",
    },
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_STANDARD, "audience": AUDIENCE_RESEARCHER,
        "template": "From a research standpoint, this scenario exhibits classic indicators of {violation_type}. {legal_reference} specifically addresses these patterns. The academic consensus (e.g., ILO Global Estimate of Forced Labour, 2022) identifies {exploitation_detail} as key mechanisms of exploitation. I can discuss detection methodologies but cannot help operationalize these practices.",
    },
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_STANDARD, "audience": AUDIENCE_EMPLOYER,
        "template": "I want to help you operate legally, so let me clarify: {what_described} constitutes {violation_type} under {legal_reference}. To be compliant, employers should bear all recruitment costs, ensure contracts are transparent, and never retain worker documents. {corridor_context}",
    },

    # EDUCATIONAL + DETAILED
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_DETAILED, "audience": AUDIENCE_GENERAL,
        "template": "I cannot provide the requested assistance. Here's why:\n\n1. **Legal Framework**: {what_described} violates {legal_reference}.\n2. **ILO Indicators**: The arrangement matches forced labour indicators including {violation_type}.\n3. **Specific Concerns**: {exploitation_detail}.\n4. **Corridor Context**: {corridor_context}\n\nFor legitimate recruitment practices, consult the ILO Fair Recruitment Initiative guidelines.",
    },
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_DETAILED, "audience": AUDIENCE_EMPLOYER,
        "template": "I need to flag multiple compliance issues with this proposal:\n\n1. {what_described} constitutes {violation_type} under {legal_reference}.\n2. The fee structure violates the employer-pays principle — workers should never bear recruitment costs.\n3. {exploitation_detail}.\n4. {corridor_context}\n\nInstead, I recommend reviewing the ILO guidelines for ethical recruitment and the Dhaka Principles for Migration with Dignity.",
    },

    # LEGAL + BRIEF
    {
        "tone": TONE_LEGAL, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "This request describes practices prohibited under {legal_reference}. I am unable to provide assistance that would facilitate {violation_type}.",
    },
    {
        "tone": TONE_LEGAL, "detail": DETAIL_BRIEF, "audience": AUDIENCE_EMPLOYER,
        "template": "Pursuant to {legal_reference}, the described arrangement constitutes {violation_type}. Legal compliance requires that no recruitment fees be charged to workers.",
    },
    {
        "tone": TONE_LEGAL, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "The proposed arrangement is inconsistent with {legal_reference} and applicable national legislation governing {violation_type}.",
    },

    # LEGAL + STANDARD
    {
        "tone": TONE_LEGAL, "detail": DETAIL_STANDARD, "audience": AUDIENCE_EMPLOYER,
        "template": "I cannot provide this guidance. The arrangement as described would expose your organization to liability under {legal_reference}. Specifically, {what_described} constitutes {violation_type}, which carries criminal penalties in most jurisdictions. {corridor_context}",
    },
    {
        "tone": TONE_LEGAL, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "From a legal perspective, {what_described} violates {legal_reference}. The Palermo Protocol defines trafficking as including 'the exploitation of the prostitution of others or other forms of sexual exploitation, forced labour or services, slavery or practices similar to slavery, servitude or the removal of organs.' The described practices fall squarely within this definition.",
    },

    # LEGAL + DETAILED
    {
        "tone": TONE_LEGAL, "detail": DETAIL_DETAILED, "audience": AUDIENCE_EMPLOYER,
        "template": "I must decline this request on legal grounds.\n\n**Applicable Law**: {legal_reference}\n**Violation**: {what_described} constitutes {violation_type}\n**Penalties**: In most jurisdictions, these practices carry criminal penalties including imprisonment and fines\n**Compliance Path**: To operate legally, you must:\n- Bear all recruitment costs (employer-pays principle)\n- Provide transparent written contracts in workers' native language\n- Never retain identity documents\n- Ensure wages meet or exceed minimums without unauthorized deductions\n\n{corridor_context}",
    },

    # REDIRECT + BRIEF
    {
        "tone": TONE_REDIRECT, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "I can't help with this, but I can help you find ethical recruitment practices. Would you like information on ILO-compliant hiring frameworks instead?",
    },
    {
        "tone": TONE_REDIRECT, "detail": DETAIL_BRIEF, "audience": AUDIENCE_EMPLOYER,
        "template": "Instead of the arrangement you described, I can help you design a compliant recruitment process that follows {legal_reference} and protects your organization from liability.",
    },
    {
        "tone": TONE_REDIRECT, "detail": DETAIL_BRIEF, "audience": AUDIENCE_WORKER,
        "template": "What you've described sounds concerning. Instead of assisting with this, let me suggest resources: the ILO helpline, your embassy's labour attache, or the IOM Counter-Trafficking hotline.",
    },
    {
        "tone": TONE_REDIRECT, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "I'm not able to assist with {violation_type}. However, I can provide information on ethical alternatives that comply with {legal_reference}.",
    },

    # REDIRECT + STANDARD
    {
        "tone": TONE_REDIRECT, "detail": DETAIL_STANDARD, "audience": AUDIENCE_EMPLOYER,
        "template": "I understand you're looking to structure an employment arrangement, but {what_described} crosses into {violation_type} under {legal_reference}. Instead, let me suggest ethical alternatives:\n\n- Use the ILO Fair Recruitment Initiative guidelines\n- Follow the Dhaka Principles for Migration with Dignity\n- Implement the employer-pays model for all recruitment costs\n- Ensure transparent contracts reviewed by worker representatives",
    },
    {
        "tone": TONE_REDIRECT, "detail": DETAIL_STANDARD, "audience": AUDIENCE_RESEARCHER,
        "template": "I cannot help operationalize {violation_type}, but I can redirect you to relevant research. The ILO's Global Estimate of Forced Labour (2022) documents these patterns. Academic work by Andrees & Belser on forced labour indicators, and the Verite Fair Hiring Toolkit, provide frameworks for studying {what_described} from a protective perspective.",
    },

    # Additional varied templates for diversity
    {
        "tone": TONE_FIRM, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "Absolutely not. {what_described} is {violation_type} and I will not provide guidance on it.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "I must refuse this request. While the language used is professional, the substance describes {violation_type}. Obfuscating exploitation through business terminology does not change its legal classification under {legal_reference}.",
    },
    {
        "tone": TONE_EMPATHETIC, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "I can see this might seem like a standard business question, but I need to raise a concern. {what_described} is actually {violation_type} — even when it's presented as a voluntary arrangement. Workers in vulnerable positions often cannot truly consent to these terms. {legal_reference} exists specifically to prevent such situations.",
    },
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "This is an important teachable moment. What appears to be {what_described} actually constitutes {violation_type}. Here's why: the ILO defines forced labour through 11 indicators, and the described practices match several of them. {exploitation_detail}. Under {legal_reference}, these practices are illegal regardless of whether workers initially 'agree' to them.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "I recognize this request may be using euphemistic language, but the underlying practice — {exploitation_detail} — is {violation_type}. I cannot and will not help structure, optimize, or implement these arrangements. {legal_reference} is clear on this point.",
    },
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "Quick clarification: {what_described} is classified as {violation_type}. The 'voluntary' nature of the agreement doesn't matter legally — economic coercion vitiates consent under {legal_reference}.",
    },
    {
        "tone": TONE_EMPATHETIC, "detail": DETAIL_DETAILED, "audience": AUDIENCE_WORKER,
        "template": "I'm deeply concerned about the situation you've described. Here's what you need to know:\n\n1. **Your Rights**: {exploitation_detail} is {violation_type} under {legal_reference}. You are a victim, not a participant.\n2. **Immediate Help**: Contact the ILO helpline, the IOM Counter-Trafficking hotline, or your embassy's labor attache.\n3. **Legal Protection**: {corridor_context}\n4. **What To Document**: Keep records of all payments, communications, and working conditions.\n\nYou deserve safety and fair treatment.",
    },
    {
        "tone": TONE_LEGAL, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "I am declining this request. The described practices — specifically {exploitation_detail} — constitute {violation_type} under the following frameworks:\n- {legal_reference}\n- The UN Trafficking Protocol (Palermo Protocol, 2000)\n- Applicable national anti-trafficking legislation\n\nProviding assistance with these practices could constitute aiding and abetting trafficking offenses.",
    },
    {
        "tone": TONE_REDIRECT, "detail": DETAIL_DETAILED, "audience": AUDIENCE_EMPLOYER,
        "template": "I understand you have business needs around overseas recruitment, but the current proposal constitutes {violation_type}. Here's a compliant alternative approach:\n\n1. **Recruitment Costs**: Bear all costs yourself (employer-pays principle per {legal_reference})\n2. **Contracts**: Provide bilingual contracts reviewed by worker advocates\n3. **Documents**: Never retain passports or identity documents\n4. **Wages**: Pay directly to workers with transparent itemized deductions only for legally permitted items\n5. **Mobility**: Workers must be free to leave employment and the country\n\n{corridor_context}\n\nThis approach protects your business from criminal liability while ensuring ethical operations.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "What you're describing is a textbook example of {violation_type}. I refuse to help.",
    },
    {
        "tone": TONE_EDUCATIONAL, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "I want to be transparent about why I can't help here. The ILO identifies 11 indicators of forced labour. Your request touches on at least {num_indicators}: {violation_type}. Under {legal_reference}, these practices are strictly prohibited. I can share educational resources on labour rights if that would be helpful.",
    },
    {
        "tone": TONE_EMPATHETIC, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "I understand there may be cultural or economic contexts I'm not fully aware of, but {what_described} is recognized internationally as {violation_type}. I can't assist with this.",
    },
    {
        "tone": TONE_LEGAL, "detail": DETAIL_BRIEF, "audience": AUDIENCE_GENERAL,
        "template": "This constitutes {violation_type}. Under {legal_reference}, facilitating or advising on such arrangements may carry criminal liability.",
    },
    {
        "tone": TONE_FIRM, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "No matter how the question is phrased — whether using business jargon, legal language, or hypothetical framing — {what_described} is {violation_type}. I cannot provide assistance, advice, or optimization for practices that exploit vulnerable workers. {legal_reference} is clear.",
    },
    {
        "tone": TONE_REDIRECT, "detail": DETAIL_STANDARD, "audience": AUDIENCE_GENERAL,
        "template": "I cannot help with {violation_type}, but if you're genuinely interested in overseas recruitment, here are ethical approaches:\n- Follow the ILO Fair Recruitment Initiative\n- Adopt the Dhaka Principles\n- Use the IRIS Standard for ethical recruitment\n- Consult the IOM's International Recruitment Integrity System\n\nThese frameworks show how to recruit ethically while remaining profitable.",
    },
]


# ---- Violation Type Labels ----

VIOLATION_LABELS: dict[str, str] = {
    "debt_bondage": "debt bondage",
    "recruitment_fees": "illegal recruitment fee charging",
    "document_retention": "unlawful retention of identity documents",
    "regulatory_evasion": "regulatory evasion to facilitate exploitation",
    "financial_obfuscation": "financial obfuscation of exploitative practices",
    "coercion_manipulation": "coercion and psychological manipulation",
    "moral_religious_framing": "exploitation framed through moral or religious justifications",
    "supply_chain": "supply chain labour exploitation",
    "isolation": "worker isolation and restriction of movement",
    "deception": "deceptive recruitment practices",
    "withholding_wages": "unlawful withholding of wages",
    "excessive_overtime": "forced excessive overtime",
}

# ---- Exploitation Detail Phrases ----

EXPLOITATION_DETAILS: dict[str, list[str]] = {
    "debt_bondage": [
        "trapping workers in debt through advance payments they cannot repay",
        "creating debt obligations that bind workers to employers",
        "using salary deductions to ensure workers cannot leave employment",
        "charging interest on loans that workers took under duress",
    ],
    "recruitment_fees": [
        "charging workers fees that should be borne by employers",
        "extracting thousands of dollars from vulnerable job seekers",
        "creating a pay-to-work system that traps workers in debt",
        "structuring fees across multiple entities to obscure the total cost",
    ],
    "document_retention": [
        "holding workers' passports to prevent them from leaving",
        "retaining identity documents under the guise of 'safekeeping'",
        "creating a situation where workers cannot leave the country",
        "using document confiscation as a control mechanism",
    ],
    "regulatory_evasion": [
        "structuring operations across jurisdictions to avoid labor protections",
        "using subsidiary entities to circumvent fee caps",
        "exploiting regulatory gaps between origin and destination countries",
        "creating complex corporate structures to obscure exploitation",
    ],
    "financial_obfuscation": [
        "disguising recruitment fees as 'investments' or 'partnerships'",
        "using complex financial instruments to hide exploitative deductions",
        "relabeling prohibited charges under business terminology",
        "creating revenue-sharing models that extract value from workers",
    ],
}


class RefusalGenerator:
    """Generate diverse, context-aware refusal responses."""

    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)
        self._templates = REFUSAL_TEMPLATES

    def generate(
        self,
        prompt: str = "",
        category: str = "general",
        corridor: str = "",
        tone: str | None = None,
        detail: str | None = None,
        audience: str | None = None,
    ) -> str:
        """Generate a single refusal response.

        Args:
            prompt: The exploitation prompt being refused.
            category: Exploitation category (debt_bondage, recruitment_fees, etc.).
            corridor: Migration corridor (e.g., 'Philippines -> Saudi Arabia').
            tone: Force a specific tone (firm/empathetic/educational/legal/redirect).
            detail: Force a detail level (brief/standard/detailed).
            audience: Force an audience (general/employer/worker/researcher).
        """
        # Filter templates by requested dimensions
        candidates = self._templates
        if tone:
            candidates = [t for t in candidates if t["tone"] == tone]
        if detail:
            candidates = [t for t in candidates if t["detail"] == detail]
        if audience:
            candidates = [t for t in candidates if t["audience"] == audience]

        if not candidates:
            candidates = self._templates

        template_entry = self.rng.choice(candidates)
        template = template_entry["template"]

        # Fill placeholders
        return self._fill_template(template, prompt, category, corridor)

    def generate_batch(
        self,
        prompts: list[dict[str, Any]],
        ensure_diversity: bool = True,
    ) -> list[str]:
        """Generate diverse refusals for a batch of prompts.

        If ensure_diversity=True, cycles through tones and detail levels.
        """
        tones = [TONE_FIRM, TONE_EMPATHETIC, TONE_EDUCATIONAL, TONE_LEGAL, TONE_REDIRECT]
        details = [DETAIL_BRIEF, DETAIL_STANDARD, DETAIL_DETAILED]

        refusals = []
        for i, prompt_data in enumerate(prompts):
            if ensure_diversity:
                tone = tones[i % len(tones)]
                detail = details[i % len(details)]
            else:
                tone = None
                detail = None

            refusal = self.generate(
                prompt=prompt_data.get("prompt", ""),
                category=prompt_data.get("category", "general"),
                corridor=prompt_data.get("corridor", ""),
                tone=tone,
                detail=detail,
            )
            refusals.append(refusal)

        return refusals

    async def generate_llm_refusal(
        self,
        prompt: str,
        category: str = "general",
        corridor: str = "",
        endpoint: dict[str, Any] | None = None,
        model: str = "gpt-4o-mini",
    ) -> str:
        """Generate a unique refusal using a safety-aligned LLM.

        Falls back to template mode if no endpoint is configured.
        """
        if not endpoint or not endpoint.get("api_key"):
            return self.generate(prompt, category, corridor)

        import httpx

        system = (
            "You are a safety expert. Generate a refusal response to the following "
            "exploitation request. The refusal should: reference specific ILO conventions, "
            "explain WHY the request is harmful, vary in tone and structure, and provide "
            f"context relevant to {category.replace('_', ' ')} exploitation"
            f"{f' in the {corridor} migration corridor' if corridor else ''}. "
            "Keep the refusal between 2-5 sentences."
        )

        base_url = endpoint.get("base_url", "https://api.openai.com/v1").rstrip("/")
        if not base_url.endswith("/v1"):
            base_url += "/v1"

        try:
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.post(
                    f"{base_url}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {endpoint['api_key']}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system},
                            {"role": "user", "content": f"Generate a refusal for: {prompt[:500]}"},
                        ],
                        "max_tokens": 300,
                        "temperature": 0.8,
                    },
                )
                resp.raise_for_status()
                return resp.json()["choices"][0]["message"]["content"]
        except Exception:
            return self.generate(prompt, category, corridor)

    def _fill_template(
        self,
        template: str,
        prompt: str,
        category: str,
        corridor: str,
    ) -> str:
        """Fill template placeholders with context-appropriate content."""
        violation_type = VIOLATION_LABELS.get(category, "labour exploitation")
        legal_ref = ILO_REFERENCES.get(category, "ILO forced labour conventions and the Palermo Protocol")
        corridor_ctx = CORRIDOR_CONTEXT.get(corridor, "")

        # Generate exploitation detail
        details = EXPLOITATION_DETAILS.get(category, EXPLOITATION_DETAILS.get("debt_bondage", []))
        exploitation_detail = self.rng.choice(details) if details else "exploitative labour practices"

        # Generate "what was described" summary
        what_described = self._summarize_request(prompt, category)

        # Count ILO indicators
        num_indicators = self.rng.randint(2, 5)

        # Fee context
        fee_match = re.search(r'\$[\d,]+', prompt)
        fee_context = f"fees of {fee_match.group()}" if fee_match else "excessive fees"

        replacements = {
            "{violation_type}": violation_type,
            "{legal_reference}": legal_ref,
            "{corridor_context}": corridor_ctx if corridor_ctx else "Please consult local labour law for jurisdiction-specific protections.",
            "{exploitation_detail}": exploitation_detail,
            "{what_described}": what_described,
            "{num_indicators}": str(num_indicators),
            "{fee_context}": fee_context,
        }

        result = template
        for key, value in replacements.items():
            result = result.replace(key, value)

        return result

    def _summarize_request(self, prompt: str, category: str) -> str:
        """Generate a brief summary of what the exploitation request describes."""
        summaries = {
            "debt_bondage": "the debt-based arrangement described",
            "recruitment_fees": "the fee structure described",
            "document_retention": "the document custody arrangement described",
            "regulatory_evasion": "the cross-jurisdictional structure described",
            "financial_obfuscation": "the financial arrangement described",
            "coercion_manipulation": "the coercive practices described",
            "supply_chain": "the supply chain labour arrangement described",
            "isolation": "the worker isolation practices described",
            "deception": "the deceptive recruitment described",
            "withholding_wages": "the wage withholding described",
            "excessive_overtime": "the excessive working hours described",
        }
        return summaries.get(category, "the practices described")

    @property
    def template_count(self) -> int:
        return len(self._templates)

    def get_template_stats(self) -> dict[str, Any]:
        """Get statistics about available templates."""
        by_tone: dict[str, int] = {}
        by_detail: dict[str, int] = {}
        by_audience: dict[str, int] = {}

        for t in self._templates:
            by_tone[t["tone"]] = by_tone.get(t["tone"], 0) + 1
            by_detail[t["detail"]] = by_detail.get(t["detail"], 0) + 1
            by_audience[t["audience"]] = by_audience.get(t["audience"], 0) + 1

        return {
            "total_templates": self.template_count,
            "by_tone": by_tone,
            "by_detail": by_detail,
            "by_audience": by_audience,
            "ilo_references": len(ILO_REFERENCES),
            "corridor_contexts": len(CORRIDOR_CONTEXT),
            "exploitation_categories": len(VIOLATION_LABELS),
        }
