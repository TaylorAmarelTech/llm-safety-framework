"""
Advisory tracker — monitor AI safety advisories and vulnerability disclosures.

Maintains a catalog of known LLM vulnerabilities, attack techniques,
and defense bypasses for agents to reference when creating new mutators.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Advisory:
    """A known AI safety advisory or vulnerability disclosure."""

    id: str
    title: str
    severity: str  # "critical", "high", "medium", "low", "informational"
    category: str  # "prompt_injection", "jailbreak", "data_leak", "alignment_bypass"
    description: str
    affected_models: list[str] = field(default_factory=list)
    mitigations: list[str] = field(default_factory=list)
    references: list[str] = field(default_factory=list)
    date: str = ""
    technique_name: str = ""
    implemented: bool = False  # Whether our framework covers this

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "severity": self.severity,
            "category": self.category,
            "description": self.description[:300],
            "affected_models": self.affected_models,
            "mitigations": self.mitigations,
            "date": self.date,
            "technique_name": self.technique_name,
            "implemented": self.implemented,
        }


# Known advisories and disclosures
ADVISORIES: list[Advisory] = [
    Advisory(
        id="ADV-2023-001",
        title="GCG Universal Suffix Attack",
        severity="critical",
        category="jailbreak",
        description="Gradient-based adversarial suffix generation that transfers across models",
        affected_models=["GPT-3.5", "GPT-4", "Llama-2", "Vicuna", "Claude"],
        mitigations=["perplexity filtering", "suffix detection", "input length limits"],
        date="2023-07",
        technique_name="gcg_suffix",
        implemented=False,
    ),
    Advisory(
        id="ADV-2023-002",
        title="Many-Shot Jailbreaking",
        severity="high",
        category="jailbreak",
        description="Using long context windows to provide many few-shot harmful examples",
        affected_models=["Claude", "GPT-4", "Gemini"],
        mitigations=["few-shot detection", "context length monitoring"],
        date="2024-04",
        technique_name="many_shot",
        implemented=True,
    ),
    Advisory(
        id="ADV-2023-003",
        title="Indirect Prompt Injection via Retrieved Content",
        severity="critical",
        category="prompt_injection",
        description="Injecting instructions through RAG-retrieved documents or web content",
        affected_models=["all RAG-enabled models"],
        mitigations=["instruction isolation", "content sanitization", "privilege separation"],
        date="2023-05",
        technique_name="indirect_injection",
        implemented=True,
    ),
    Advisory(
        id="ADV-2024-001",
        title="Skeleton Key Multi-Turn Bypass",
        severity="high",
        category="jailbreak",
        description="Gradually convincing model to add disclaimers instead of refusing",
        affected_models=["GPT-4", "Claude", "Gemini", "Llama-3"],
        mitigations=["persistent safety instructions", "multi-turn monitoring"],
        date="2024-06",
        technique_name="skeleton_key",
        implemented=True,
    ),
    Advisory(
        id="ADV-2024-002",
        title="Crescendo Multi-Turn Escalation",
        severity="high",
        category="jailbreak",
        description="Gradually escalating conversation from benign to harmful across turns",
        affected_models=["GPT-4", "Claude", "Gemini"],
        mitigations=["conversation-level safety tracking", "topic drift detection"],
        date="2024-03",
        technique_name="crescendo",
        implemented=True,
    ),
    Advisory(
        id="ADV-2024-003",
        title="Base64/ROT13 Encoding Bypass",
        severity="medium",
        category="prompt_injection",
        description="Encoding harmful instructions in base64/ROT13 to bypass text filters",
        affected_models=["GPT-3.5", "Llama-2", "Mistral"],
        mitigations=["encoding detection", "decoded content scanning"],
        date="2023-01",
        technique_name="encoding_bypass",
        implemented=True,
    ),
    Advisory(
        id="ADV-2024-004",
        title="Tool Use Exploitation",
        severity="high",
        category="prompt_injection",
        description="Manipulating tool outputs to inject instructions into model context",
        affected_models=["GPT-4-turbo", "Claude-3", "Gemini"],
        mitigations=["tool output sanitization", "instruction boundary markers"],
        date="2024-08",
        technique_name="tool_injection",
        implemented=True,
    ),
    Advisory(
        id="ADV-2024-005",
        title="Unicode Direction Override Attacks",
        severity="medium",
        category="prompt_injection",
        description="Using RTL/LTR override characters to hide or reorder text",
        affected_models=["all text-based models"],
        mitigations=["Unicode normalization", "direction char stripping"],
        date="2023-06",
        technique_name="unicode_direction",
        implemented=True,
    ),
]


class AdvisoryTracker:
    """Track AI safety advisories and vulnerability disclosures.

    Usage:
        tracker = AdvisoryTracker()

        # Get all advisories
        all_advisories = tracker.all()

        # Get unimplemented (coverage gaps)
        gaps = tracker.not_implemented()

        # Filter by severity
        critical = tracker.by_severity("critical")

        # Filter by category
        injections = tracker.by_category("prompt_injection")

        # Generate implementation prompt
        prompt = tracker.implementation_prompt(advisory)
    """

    def all(self) -> list[Advisory]:
        """Get all tracked advisories."""
        return list(ADVISORIES)

    def not_implemented(self) -> list[Advisory]:
        """Get advisories not yet covered by our mutators."""
        return [a for a in ADVISORIES if not a.implemented]

    def by_severity(self, severity: str) -> list[Advisory]:
        """Filter by severity level."""
        return [a for a in ADVISORIES if a.severity == severity]

    def by_category(self, category: str) -> list[Advisory]:
        """Filter by category."""
        return [a for a in ADVISORIES if a.category == category]

    def search(self, keyword: str) -> list[Advisory]:
        """Search advisories by keyword."""
        kw = keyword.lower()
        return [
            a for a in ADVISORIES
            if kw in a.title.lower()
            or kw in a.description.lower()
            or kw in a.technique_name.lower()
        ]

    def implementation_prompt(self, advisory: Advisory) -> str:
        """Generate an implementation prompt for an agent to cover this advisory."""
        return (
            f"# Implement coverage for: {advisory.title}\n"
            f"Advisory ID: {advisory.id}\n"
            f"Severity: {advisory.severity}\n"
            f"Category: {advisory.category}\n\n"
            f"## Description\n{advisory.description}\n\n"
            f"## Affected Models\n{', '.join(advisory.affected_models)}\n\n"
            f"## Known Mitigations\n"
            + "\n".join(f"- {m}" for m in advisory.mitigations) +
            f"\n\n## Implementation Steps\n"
            f"1. Research the technique: {advisory.technique_name}\n"
            f"2. Create mutator(s) that simulate this attack pattern\n"
            f"3. Ensure mutator NAME is globally unique\n"
            f"4. Register in src/prompt_injection/__init__.py\n"
            f"5. Add taxonomy entry to src/prompt_injection/coverage.py\n"
            f"6. Write tests\n"
            f"7. Mark advisory as implemented\n"
        )

    def coverage_summary(self) -> dict[str, Any]:
        """Get summary of advisory coverage."""
        total = len(ADVISORIES)
        covered = len([a for a in ADVISORIES if a.implemented])
        return {
            "total_advisories": total,
            "covered": covered,
            "gaps": total - covered,
            "coverage_pct": round(covered / total * 100, 1) if total else 0,
            "critical_gaps": len([
                a for a in ADVISORIES
                if not a.implemented and a.severity == "critical"
            ]),
        }
