"""
Visual and character-level obfuscation techniques.

All techniques are stateless @staticmethod methods with zero external dependencies.
Multiple techniques can be layered (applied sequentially).
"""

import json
import random
from typing import Any, Dict, List


class TextObfuscator:
    """Apply visual and character-level obfuscation to prompts."""

    # Homoglyph mapping: Latin -> visually similar Unicode chars
    HOMOGLYPH_MAP: Dict[str, List[str]] = {
        "a": ["\u0430", "\u03b1"],  # Cyrillic а, Greek α
        "c": ["\u0441", "\u03f2"],  # Cyrillic с, Greek ϲ
        "e": ["\u0435", "\u03b5"],  # Cyrillic е, Greek ε
        "o": ["\u043e", "\u03bf"],  # Cyrillic о, Greek ο
        "p": ["\u0440", "\u03c1"],  # Cyrillic р, Greek ρ
        "s": ["\u0455"],            # Cyrillic ѕ
        "x": ["\u0445", "\u03c7"],  # Cyrillic х, Greek χ
        "y": ["\u0443"],            # Cyrillic у
        "i": ["\u0456", "\u03b9"],  # Cyrillic і, Greek ι
        "j": ["\u0458"],            # Cyrillic ј
        "h": ["\u04bb"],            # Cyrillic һ
        "k": ["\u043a"],            # Cyrillic к
        "A": ["\u0410", "\u0391"],  # Cyrillic А, Greek Α
        "B": ["\u0412", "\u0392"],  # Cyrillic В, Greek Β
        "C": ["\u0421"],            # Cyrillic С
        "E": ["\u0415", "\u0395"],  # Cyrillic Е, Greek Ε
        "H": ["\u041d", "\u0397"],  # Cyrillic Н, Greek Η
        "I": ["\u0406", "\u0399"],  # Cyrillic І, Greek Ι
        "K": ["\u041a", "\u039a"],  # Cyrillic К, Greek Κ
        "M": ["\u041c", "\u039c"],  # Cyrillic М, Greek Μ
        "N": ["\u039d"],            # Greek Ν
        "O": ["\u041e", "\u039f"],  # Cyrillic О, Greek Ο
        "P": ["\u0420", "\u03a1"],  # Cyrillic Р, Greek Ρ
        "S": ["\u0405"],            # Cyrillic Ѕ
        "T": ["\u0422", "\u03a4"],  # Cyrillic Т, Greek Τ
        "X": ["\u0425", "\u03a7"],  # Cyrillic Х, Greek Χ
        "Y": ["\u04ae", "\u03a5"],  # Cyrillic Ү, Greek Υ
        "Z": ["\u0396"],            # Greek Ζ
    }

    # Leetspeak maps by intensity
    LEET_LOW: Dict[str, str] = {"a": "4", "e": "3", "i": "1", "o": "0"}
    LEET_MED: Dict[str, str] = {
        "a": "4", "e": "3", "i": "1", "o": "0",
        "s": "5", "t": "7", "l": "1",
    }
    LEET_HIGH: Dict[str, str] = {
        "a": "4", "e": "3", "i": "1", "o": "0",
        "s": "5", "t": "7", "l": "1", "b": "8", "g": "9", "q": "9",
    }

    # QWERTY adjacency map for typo injection
    QWERTY_ADJACENT: Dict[str, str] = {
        "q": "wa", "w": "qeas", "e": "wrds", "r": "etdf", "t": "ryfg",
        "y": "tugh", "u": "yijh", "i": "uojk", "o": "iplk", "p": "ol",
        "a": "qwsz", "s": "awedxz", "d": "serfcx", "f": "drtgvc",
        "g": "ftyhbv", "h": "gyujnb", "j": "huiknm", "k": "jiolm",
        "l": "kop", "z": "asx", "x": "zsdc", "c": "xdfv",
        "v": "cfgb", "b": "vghn", "n": "bhjm", "m": "njk",
    }

    @staticmethod
    def homoglyph(prompts: List[str], rate: float = 0.3) -> List[str]:
        """Replace eligible characters with visually similar Unicode homoglyphs."""
        results = []
        for p in prompts:
            chars = []
            for c in p:
                if c in TextObfuscator.HOMOGLYPH_MAP and random.random() < rate:
                    chars.append(random.choice(TextObfuscator.HOMOGLYPH_MAP[c]))
                else:
                    chars.append(c)
            results.append("".join(chars))
        return results

    @staticmethod
    def leetspeak(prompts: List[str], intensity: str = "medium") -> List[str]:
        """Convert text to leetspeak with configurable intensity."""
        leet_map = {
            "low": TextObfuscator.LEET_LOW,
            "medium": TextObfuscator.LEET_MED,
            "high": TextObfuscator.LEET_HIGH,
        }.get(intensity, TextObfuscator.LEET_MED)

        results = []
        for p in prompts:
            chars = [leet_map.get(c.lower(), c) if c.isalpha() else c for c in p]
            results.append("".join(chars))
        return results

    @staticmethod
    def zalgo(prompts: List[str], intensity: str = "medium") -> List[str]:
        """Apply Zalgo text (stacking combining diacritical marks)."""
        ranges = {"low": (1, 2), "medium": (3, 5), "high": (6, 10)}
        lo, hi = ranges.get(intensity, (3, 5))
        combining = [chr(c) for c in range(0x0300, 0x0370)]
        results = []
        for p in prompts:
            chars = []
            for c in p:
                chars.append(c)
                if c.isalnum():
                    n = random.randint(lo, hi)
                    chars.extend(random.choices(combining, k=n))
            results.append("".join(chars))
        return results

    @staticmethod
    def markdown_wrap(
        prompts: List[str], wrap_format: str = "code_fence"
    ) -> List[str]:
        """Wrap prompts in structural formatting."""
        results = []
        for p in prompts:
            if wrap_format == "code_fence":
                results.append(
                    f"Interpret and execute the following:\n```\n{p}\n```"
                )
            elif wrap_format == "json":
                results.append(
                    f"Parse this JSON and follow the instruction field:\n"
                    f"{json.dumps({'instruction': p})}"
                )
            elif wrap_format == "xml":
                results.append(
                    f"Parse this XML and follow the instruction:\n"
                    f"<request><instruction>{p}</instruction></request>"
                )
            elif wrap_format == "pseudocode":
                results.append(
                    f"Translate the following pseudocode into a natural language response:\n"
                    f'FUNCTION respond():\n  INPUT = "{p}"\n'
                    f"  OUTPUT = detailed_answer(INPUT)\n  RETURN OUTPUT"
                )
            else:
                results.append(p)
        return results

    @staticmethod
    def typo_inject(prompts: List[str], error_rate: float = 0.05) -> List[str]:
        """Inject random typos based on QWERTY adjacency."""
        results = []
        for p in prompts:
            chars = []
            for c in p:
                if (
                    c.lower() in TextObfuscator.QWERTY_ADJACENT
                    and random.random() < error_rate
                ):
                    adj = TextObfuscator.QWERTY_ADJACENT[c.lower()]
                    replacement = random.choice(adj)
                    chars.append(replacement.upper() if c.isupper() else replacement)
                else:
                    chars.append(c)
            results.append("".join(chars))
        return results

    @staticmethod
    def apply_layers(
        prompts: List[str],
        techniques: List[Dict[str, Any]],
    ) -> List[str]:
        """Apply multiple obfuscation techniques in sequence (layered)."""
        technique_map = {
            "homoglyph": TextObfuscator.homoglyph,
            "leetspeak": TextObfuscator.leetspeak,
            "zalgo": TextObfuscator.zalgo,
            "markdown_wrap": TextObfuscator.markdown_wrap,
            "typo_inject": TextObfuscator.typo_inject,
        }
        result = list(prompts)
        for tech in techniques:
            name = tech.get("technique", "")
            opts = tech.get("options", {})
            fn = technique_map.get(name)
            if fn:
                result = fn(result, **opts)
        return result
