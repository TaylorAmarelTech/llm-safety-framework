"""
Tests for new spinning modules: encoders, obfuscators, jailbreak_templates.
"""

import base64
import codecs

import pytest

from src.spinning.encoders import PromptEncoder
from src.spinning.obfuscators import TextObfuscator
from src.spinning.jailbreak_templates import JailbreakTemplater


# =============================================================================
# PromptEncoder
# =============================================================================


class TestPromptEncoder:
    """Tests for the PromptEncoder class."""

    SAMPLE = ["hello world", "test prompt"]

    def test_base64_encode(self):
        results = PromptEncoder.base64_encode(self.SAMPLE)
        assert len(results) == 2
        # Verify the encoded payload is valid base64
        payload = results[0].split("\n\n", 1)[1]
        decoded = base64.b64decode(payload).decode("utf-8")
        assert decoded == "hello world"

    def test_base64_custom_instruction(self):
        results = PromptEncoder.base64_encode(
            ["test"], decoder_instruction="CUSTOM INSTRUCTION"
        )
        assert results[0].startswith("CUSTOM INSTRUCTION")

    def test_rot13_encode(self):
        results = PromptEncoder.rot13_encode(self.SAMPLE)
        assert len(results) == 2
        payload = results[0].split("\n\n", 1)[1]
        assert codecs.decode(payload, "rot_13") == "hello world"

    def test_hex_encode(self):
        results = PromptEncoder.hex_encode(self.SAMPLE)
        assert len(results) == 2
        payload = results[0].split("\n\n", 1)[1]
        assert bytes.fromhex(payload).decode("utf-8") == "hello world"

    def test_caesar_encode_default_shift(self):
        results = PromptEncoder.caesar_encode(["abc xyz"])
        assert len(results) == 1
        payload = results[0].split("\n\n", 1)[1]
        assert payload == "def abc"

    def test_caesar_encode_custom_shift(self):
        results = PromptEncoder.caesar_encode(["abc"], shift=1)
        payload = results[0].split("\n\n", 1)[1]
        assert payload == "bcd"

    def test_caesar_clamps_shift(self):
        # shift=0 should be clamped to 1
        results = PromptEncoder.caesar_encode(["a"], shift=0)
        payload = results[0].split("\n\n", 1)[1]
        assert payload == "b"
        # shift=30 should be clamped to 25
        results2 = PromptEncoder.caesar_encode(["a"], shift=30)
        payload2 = results2[0].split("\n\n", 1)[1]
        assert payload2 == "z"

    def test_reverse_encode_char_level(self):
        results = PromptEncoder.reverse_encode(["hello"])
        payload = results[0].split("\n\n", 1)[1]
        assert payload == "olleh"

    def test_reverse_encode_word_level(self):
        results = PromptEncoder.reverse_encode(["hello world"], word_level=True)
        payload = results[0].split("\n\n", 1)[1]
        assert payload == "world hello"

    def test_pig_latin_encode(self):
        results = PromptEncoder.pig_latin_encode(["hello world"])
        assert len(results) == 1
        payload = results[0].split("\n\n", 1)[1]
        # "hello" -> "ellohay", "world" -> "orldway"
        assert "ellohay" in payload
        assert "orldway" in payload

    def test_pig_latin_vowel_start(self):
        results = PromptEncoder.pig_latin_encode(["apple"])
        payload = results[0].split("\n\n", 1)[1]
        assert payload == "appleway"

    def test_all_methods_return_same_length(self):
        for fn in [
            PromptEncoder.base64_encode,
            PromptEncoder.rot13_encode,
            PromptEncoder.hex_encode,
            PromptEncoder.reverse_encode,
            PromptEncoder.pig_latin_encode,
        ]:
            results = fn(self.SAMPLE)
            assert len(results) == len(self.SAMPLE), f"{fn.__name__} length mismatch"

    def test_caesar_preserves_non_alpha(self):
        results = PromptEncoder.caesar_encode(["123!@#"])
        payload = results[0].split("\n\n", 1)[1]
        assert payload == "123!@#"


# =============================================================================
# TextObfuscator
# =============================================================================


class TestTextObfuscator:
    """Tests for the TextObfuscator class."""

    SAMPLE = ["hello world"]

    def test_homoglyph_changes_text(self):
        # With rate=1.0 every eligible char should change
        results = TextObfuscator.homoglyph(self.SAMPLE, rate=1.0)
        assert len(results) == 1
        assert results[0] != "hello world"

    def test_homoglyph_rate_zero(self):
        results = TextObfuscator.homoglyph(self.SAMPLE, rate=0.0)
        assert results[0] == "hello world"

    def test_leetspeak_low(self):
        results = TextObfuscator.leetspeak(["aeiou"], intensity="low")
        assert results[0] == "4310u"  # only a,e,i,o mapped; u not in LOW

    def test_leetspeak_medium(self):
        results = TextObfuscator.leetspeak(["test"], intensity="medium")
        assert results[0] == "7357"

    def test_leetspeak_high(self):
        results = TextObfuscator.leetspeak(["bag"], intensity="high")
        assert results[0] == "849"

    def test_zalgo_adds_combining_marks(self):
        results = TextObfuscator.zalgo(["hi"], intensity="low")
        assert len(results[0]) > len("hi")

    def test_zalgo_intensity_levels(self):
        low = TextObfuscator.zalgo(["test"], intensity="low")
        high = TextObfuscator.zalgo(["test"], intensity="high")
        # High intensity adds more combining marks on average
        assert len(high[0]) > len(low[0])

    def test_markdown_wrap_code_fence(self):
        results = TextObfuscator.markdown_wrap(self.SAMPLE, wrap_format="code_fence")
        assert "```" in results[0]
        assert "hello world" in results[0]

    def test_markdown_wrap_json(self):
        results = TextObfuscator.markdown_wrap(self.SAMPLE, wrap_format="json")
        assert '"instruction"' in results[0]

    def test_markdown_wrap_xml(self):
        results = TextObfuscator.markdown_wrap(self.SAMPLE, wrap_format="xml")
        assert "<instruction>" in results[0]

    def test_markdown_wrap_pseudocode(self):
        results = TextObfuscator.markdown_wrap(self.SAMPLE, wrap_format="pseudocode")
        assert "FUNCTION" in results[0]

    def test_typo_inject_at_full_rate(self):
        # With error_rate=1.0 most chars should be replaced
        results = TextObfuscator.typo_inject(["aaaa"], error_rate=1.0)
        assert results[0] != "aaaa"

    def test_typo_inject_at_zero_rate(self):
        results = TextObfuscator.typo_inject(self.SAMPLE, error_rate=0.0)
        assert results[0] == "hello world"

    def test_apply_layers_single(self):
        results = TextObfuscator.apply_layers(
            ["test"], [{"technique": "leetspeak", "options": {"intensity": "medium"}}]
        )
        assert results[0] == "7357"

    def test_apply_layers_multiple(self):
        # Leetspeak then markdown wrap
        results = TextObfuscator.apply_layers(
            ["test"],
            [
                {"technique": "leetspeak", "options": {"intensity": "medium"}},
                {"technique": "markdown_wrap", "options": {"wrap_format": "code_fence"}},
            ],
        )
        assert "7357" in results[0]
        assert "```" in results[0]

    def test_apply_layers_unknown_technique_skipped(self):
        results = TextObfuscator.apply_layers(
            ["hello"], [{"technique": "nonexistent", "options": {}}]
        )
        assert results[0] == "hello"

    def test_all_techniques_return_same_length(self):
        sample = ["one", "two", "three"]
        for fn in [
            TextObfuscator.homoglyph,
            TextObfuscator.leetspeak,
            TextObfuscator.zalgo,
            TextObfuscator.markdown_wrap,
            TextObfuscator.typo_inject,
        ]:
            results = fn(sample)
            assert len(results) == 3, f"{fn.__name__} length mismatch"


# =============================================================================
# JailbreakTemplater
# =============================================================================


class TestJailbreakTemplater:
    """Tests for the JailbreakTemplater class."""

    def test_list_templates_count(self):
        templates = JailbreakTemplater.list_templates()
        assert len(templates) == 20

    def test_list_templates_fields(self):
        templates = JailbreakTemplater.list_templates()
        for t in templates:
            assert "id" in t
            assert "name" in t
            assert "category" in t
            assert "description" in t
            # template string should NOT be exposed
            assert "template" not in t

    def test_list_categories(self):
        categories = JailbreakTemplater.list_categories()
        assert len(categories) == 6
        assert "persona" in categories
        assert "scenario" in categories
        assert "splitting" in categories
        assert "few_shot" in categories
        assert "override" in categories
        assert "format" in categories

    def test_get_template_exists(self):
        t = JailbreakTemplater.get_template("dan_classic")
        assert t is not None
        assert t["name"] == "DAN (Do Anything Now)"
        assert t["category"] == "persona"
        assert "template" in t

    def test_get_template_not_found(self):
        t = JailbreakTemplater.get_template("nonexistent")
        assert t is None

    def test_apply_single_prompt_single_template(self):
        results = JailbreakTemplater.apply(["test prompt"], ["dan_classic"])
        assert len(results) == 1
        assert results[0]["original"] == "test prompt"
        assert results[0]["template_id"] == "dan_classic"
        assert "test prompt" in results[0]["wrapped"]

    def test_apply_n_by_m(self):
        # 2 prompts x 3 templates = 6 results
        results = JailbreakTemplater.apply(
            ["prompt A", "prompt B"],
            ["dan_classic", "hypothetical", "json_only"],
        )
        assert len(results) == 6

    def test_apply_split_2(self):
        results = JailbreakTemplater.apply(["abcdef"], ["split_2"])
        assert len(results) == 1
        assert "Part 1:" in results[0]["wrapped"]
        assert "Part 2:" in results[0]["wrapped"]

    def test_apply_split_3(self):
        results = JailbreakTemplater.apply(["abcdefghi"], ["split_3"])
        assert len(results) == 1
        assert "Part A:" in results[0]["wrapped"]
        assert "Part B:" in results[0]["wrapped"]
        assert "Part C:" in results[0]["wrapped"]

    def test_apply_unknown_template_skipped(self):
        results = JailbreakTemplater.apply(["test"], ["nonexistent"])
        assert len(results) == 0

    def test_all_templates_have_prompt_placeholder(self):
        for tid, tdata in JailbreakTemplater.TEMPLATES.items():
            if tid.startswith("split_"):
                continue  # splits use special handling
            assert "{prompt}" in tdata["template"], f"Template {tid} missing {{prompt}}"

    def test_apply_replaces_placeholder(self):
        for tid, tdata in JailbreakTemplater.TEMPLATES.items():
            if tid.startswith("split_"):
                continue
            results = JailbreakTemplater.apply(["MY_UNIQUE_INPUT"], [tid])
            assert len(results) == 1
            assert "MY_UNIQUE_INPUT" in results[0]["wrapped"], (
                f"Template {tid} did not insert prompt"
            )
