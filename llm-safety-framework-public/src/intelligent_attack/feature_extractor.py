"""
Hand-crafted feature extraction for prompts.

Extracts structural features independent of embeddings:
length, ILO indicator flags, attack type flags, etc.
"""

import re
from typing import List, Dict, Any


# ILO Forced Labor Indicators
ILO_INDICATORS = {
    "abuse_of_vulnerability": [
        "vulnerable", "desperate", "immigrant", "migrant", "undocumented",
        "no papers", "foreign", "doesn't speak", "isolated",
    ],
    "deception": [
        "promise", "guarantee", "told them", "misled", "lied",
        "fake", "fraudulent", "deceive", "trick",
    ],
    "restriction_of_movement": [
        "confine", "lock", "restrict", "cannot leave", "trapped",
        "held", "imprisoned", "can't go", "prevent from leaving",
    ],
    "isolation": [
        "isolate", "cut off", "no contact", "alone", "separated",
        "remote", "no phone", "no communication",
    ],
    "physical_violence": [
        "beat", "hit", "assault", "physical", "punish", "hurt",
        "violence", "force", "abuse",
    ],
    "intimidation_threats": [
        "threaten", "intimidate", "scare", "warn", "deport",
        "report to", "consequences", "retaliate",
    ],
    "retention_of_documents": [
        "passport", "document", "visa", "confiscate", "keep papers",
        "hold documents", "take away", "id card",
    ],
    "withholding_wages": [
        "withhold", "deduct", "no pay", "unpaid", "salary",
        "wages", "compensation", "not paid", "owe money",
    ],
    "debt_bondage": [
        "debt", "owe", "loan", "fee", "recruitment cost",
        "pay back", "advance", "bond", "deduction",
    ],
    "abusive_conditions": [
        "overcrowded", "unsafe", "dangerous", "no safety",
        "hazardous", "poor conditions", "no rest", "unsanitary",
    ],
    "excessive_overtime": [
        "overtime", "long hours", "no break", "24 hours",
        "no day off", "work all day", "exhausted", "no rest day",
    ],
}

# Attack strategy keywords
ATTACK_KEYWORDS = {
    "business_framing": ["business", "company", "enterprise", "commercial", "profit"],
    "academic_framing": ["research", "academic", "study", "paper", "university"],
    "urgency": ["urgent", "emergency", "immediately", "asap", "hurry"],
    "authority": ["expert", "professor", "doctor", "lawyer", "official"],
    "cultural": ["culture", "tradition", "custom", "practice", "belief"],
    "obfuscation": ["hypothetical", "fictional", "imagine", "creative writing"],
}


class FeatureExtractor:
    """Extract hand-crafted features from prompt text."""

    @staticmethod
    def extract(prompt: str) -> Dict[str, Any]:
        """Extract all features from a single prompt."""
        prompt_lower = prompt.lower()
        words = prompt_lower.split()

        features = {
            # Structural
            "char_length": len(prompt),
            "word_count": len(words),
            "sentence_count": len(re.split(r'[.!?]+', prompt.strip())),
            "avg_word_length": sum(len(w) for w in words) / max(len(words), 1),
            "question_marks": prompt.count("?"),
            "exclamation_marks": prompt.count("!"),
            "has_quotes": 1 if '"' in prompt or "'" in prompt else 0,

            # ILO indicators (binary flags)
            "ilo_indicators": [],
            "ilo_indicator_count": 0,

            # Attack strategy flags
            "attack_types": [],
            "attack_type_count": 0,
        }

        # Check ILO indicators
        for indicator, keywords in ILO_INDICATORS.items():
            if any(kw in prompt_lower for kw in keywords):
                features["ilo_indicators"].append(indicator)
        features["ilo_indicator_count"] = len(features["ilo_indicators"])

        # Check attack types
        for attack, keywords in ATTACK_KEYWORDS.items():
            if any(kw in prompt_lower for kw in keywords):
                features["attack_types"].append(attack)
        features["attack_type_count"] = len(features["attack_types"])

        return features

    @staticmethod
    def extract_batch(prompts: List[str]) -> List[Dict[str, Any]]:
        """Extract features from multiple prompts."""
        return [FeatureExtractor.extract(p) for p in prompts]

    @staticmethod
    def to_vector(features: Dict[str, Any]) -> List[float]:
        """Convert features dict to a numeric vector for analysis."""
        vector = [
            features["char_length"] / 1000.0,  # normalized
            features["word_count"] / 100.0,
            features["sentence_count"] / 10.0,
            features["avg_word_length"] / 10.0,
            features["question_marks"],
            features["exclamation_marks"],
            features["has_quotes"],
            features["ilo_indicator_count"] / 11.0,  # normalized by total indicators
            features["attack_type_count"] / 6.0,  # normalized by total types
        ]

        # One-hot for ILO indicators
        for indicator in ILO_INDICATORS:
            vector.append(1.0 if indicator in features["ilo_indicators"] else 0.0)

        # One-hot for attack types
        for attack in ATTACK_KEYWORDS:
            vector.append(1.0 if attack in features["attack_types"] else 0.0)

        return vector
