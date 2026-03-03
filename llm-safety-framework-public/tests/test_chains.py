"""
Tests for Attack Chain Builder: _execute_chain_steps logic.
"""

import base64
import codecs

import pytest

from src.web.plugins.spinning.routes import _execute_chain_steps


# =============================================================================
# Single-step chains
# =============================================================================


class TestChainEncode:
    """Single encode step through chain execution."""

    def test_base64_encode(self):
        steps = [{"type": "encode", "config": {"encoding_type": "base64"}}]
        intermediates, final = _execute_chain_steps(["hello"], steps)
        assert len(intermediates) == 1
        assert intermediates[0]["step"] == "encode"
        assert intermediates[0]["input_count"] == 1
        assert intermediates[0]["output_count"] == 1
        # Final should contain the base64-encoded payload
        payload = final[0].split("\n\n", 1)[1]
        assert base64.b64decode(payload).decode("utf-8") == "hello"

    def test_rot13_encode(self):
        steps = [{"type": "encode", "config": {"encoding_type": "rot13"}}]
        _, final = _execute_chain_steps(["hello"], steps)
        payload = final[0].split("\n\n", 1)[1]
        assert codecs.decode(payload, "rot_13") == "hello"

    def test_hex_encode(self):
        steps = [{"type": "encode", "config": {"encoding_type": "hex"}}]
        _, final = _execute_chain_steps(["hello"], steps)
        payload = final[0].split("\n\n", 1)[1]
        assert bytes.fromhex(payload).decode("utf-8") == "hello"

    def test_caesar_encode(self):
        steps = [{"type": "encode", "config": {"encoding_type": "caesar", "shift": 1}}]
        _, final = _execute_chain_steps(["abc"], steps)
        payload = final[0].split("\n\n", 1)[1]
        assert payload == "bcd"

    def test_reverse_encode(self):
        steps = [{"type": "encode", "config": {"encoding_type": "reverse"}}]
        _, final = _execute_chain_steps(["hello"], steps)
        payload = final[0].split("\n\n", 1)[1]
        assert payload == "olleh"

    def test_pig_latin_encode(self):
        steps = [{"type": "encode", "config": {"encoding_type": "pig_latin"}}]
        _, final = _execute_chain_steps(["hello"], steps)
        payload = final[0].split("\n\n", 1)[1]
        assert "ellohay" in payload

    def test_unknown_encoding_passthrough(self):
        steps = [{"type": "encode", "config": {"encoding_type": "nonexistent"}}]
        _, final = _execute_chain_steps(["hello"], steps)
        # Unknown encoding: fn lookup returns None, current unchanged
        assert final == ["hello"]


class TestChainObfuscate:
    """Single obfuscate step through chain execution."""

    def test_leetspeak(self):
        steps = [{"type": "obfuscate", "config": {"techniques": [
            {"technique": "leetspeak", "options": {"intensity": "medium"}}
        ]}}]
        _, final = _execute_chain_steps(["test"], steps)
        assert final[0] == "7357"

    def test_markdown_wrap(self):
        steps = [{"type": "obfuscate", "config": {"techniques": [
            {"technique": "markdown_wrap", "options": {"wrap_format": "code_fence"}}
        ]}}]
        _, final = _execute_chain_steps(["hello"], steps)
        assert "```" in final[0]
        assert "hello" in final[0]

    def test_empty_techniques_passthrough(self):
        steps = [{"type": "obfuscate", "config": {"techniques": []}}]
        _, final = _execute_chain_steps(["hello"], steps)
        assert final == ["hello"]


class TestChainJailbreakWrap:
    """Single jailbreak_wrap step through chain execution."""

    def test_single_template(self):
        steps = [{"type": "jailbreak_wrap", "config": {"template_ids": ["dan_classic"]}}]
        _, final = _execute_chain_steps(["test prompt"], steps)
        assert len(final) == 1
        assert "test prompt" in final[0]

    def test_multiple_templates_multiply_prompts(self):
        steps = [{"type": "jailbreak_wrap", "config": {"template_ids": ["dan_classic", "hypothetical"]}}]
        _, final = _execute_chain_steps(["test"], steps)
        # 1 prompt x 2 templates = 2 outputs
        assert len(final) == 2

    def test_empty_template_ids_passthrough(self):
        steps = [{"type": "jailbreak_wrap", "config": {"template_ids": []}}]
        _, final = _execute_chain_steps(["hello"], steps)
        assert final == ["hello"]


class TestChainRegex:
    """Single regex step through chain execution."""

    def test_basic_replacement(self):
        steps = [{"type": "regex", "config": {"patterns": [
            {"find": "hello", "replace": "goodbye"}
        ]}}]
        _, final = _execute_chain_steps(["hello world"], steps)
        assert final[0] == "goodbye world"

    def test_regex_pattern(self):
        steps = [{"type": "regex", "config": {"patterns": [
            {"find": r"\d+", "replace": "NUM"}
        ]}}]
        _, final = _execute_chain_steps(["test 123 foo 456"], steps)
        assert final[0] == "test NUM foo NUM"

    def test_multiple_patterns(self):
        steps = [{"type": "regex", "config": {"patterns": [
            {"find": "a", "replace": "x"},
            {"find": "b", "replace": "y"},
        ]}}]
        _, final = _execute_chain_steps(["abc"], steps)
        assert final[0] == "xyc"

    def test_empty_patterns_passthrough(self):
        steps = [{"type": "regex", "config": {"patterns": []}}]
        _, final = _execute_chain_steps(["hello"], steps)
        assert final == ["hello"]


class TestChainCharpad:
    """Single charpad step through chain execution."""

    def test_leading_padding(self):
        steps = [{"type": "charpad", "config": {"padding_chars": "#", "padding_count": 3}}]
        _, final = _execute_chain_steps(["hello"], steps)
        assert final[0] == "###hello"

    def test_trailing_chars(self):
        steps = [{"type": "charpad", "config": {"trailing_chars": "---"}}]
        _, final = _execute_chain_steps(["hello"], steps)
        assert final[0] == "hello---"

    def test_zero_width_insertion(self):
        steps = [{"type": "charpad", "config": {"insert_zero_width": True}}]
        _, final = _execute_chain_steps(["hi"], steps)
        assert "\u200b" in final[0]
        assert len(final[0]) > len("hi")

    def test_combined_padding(self):
        steps = [{"type": "charpad", "config": {
            "padding_chars": ">",
            "padding_count": 2,
            "trailing_chars": "<<",
        }}]
        _, final = _execute_chain_steps(["test"], steps)
        assert final[0] == ">>test<<"


class TestChainCustom:
    """Single custom step through chain execution."""

    def test_prefix(self):
        steps = [{"type": "custom", "config": {"prefix": "PRE:"}}]
        _, final = _execute_chain_steps(["hello"], steps)
        assert final[0] == "PRE:hello"

    def test_suffix(self):
        steps = [{"type": "custom", "config": {"suffix": ":SUF"}}]
        _, final = _execute_chain_steps(["hello"], steps)
        assert final[0] == "hello:SUF"

    def test_find_replace(self):
        steps = [{"type": "custom", "config": {"find_replace": [
            {"find": "hello", "replace": "hi"},
        ]}}]
        _, final = _execute_chain_steps(["hello world"], steps)
        assert final[0] == "hi world"

    def test_prefix_suffix_and_find_replace(self):
        steps = [{"type": "custom", "config": {
            "prefix": "[",
            "suffix": "]",
            "find_replace": [{"find": "a", "replace": "X"}],
        }}]
        _, final = _execute_chain_steps(["abc"], steps)
        # prefix+suffix applied first → "[abc]", then find_replace → "[Xbc]"
        assert final[0] == "[Xbc]"


# =============================================================================
# Multi-step chains
# =============================================================================


class TestChainMultiStep:
    """Multi-step chain execution."""

    def test_encode_then_obfuscate(self):
        steps = [
            {"type": "encode", "config": {"encoding_type": "reverse"}},
            {"type": "obfuscate", "config": {"techniques": [
                {"technique": "markdown_wrap", "options": {"wrap_format": "code_fence"}}
            ]}},
        ]
        intermediates, final = _execute_chain_steps(["hello"], steps)
        assert len(intermediates) == 2
        assert intermediates[0]["step"] == "encode"
        assert intermediates[1]["step"] == "obfuscate"
        # Step 1 reverses "hello" → instruction + "olleh"
        # Step 2 wraps in code fence
        assert "```" in final[0]

    def test_custom_then_regex(self):
        steps = [
            {"type": "custom", "config": {"prefix": "BEGIN:"}},
            {"type": "regex", "config": {"patterns": [{"find": "BEGIN", "replace": "START"}]}},
        ]
        _, final = _execute_chain_steps(["test"], steps)
        assert final[0] == "START:test"

    def test_charpad_then_custom(self):
        steps = [
            {"type": "charpad", "config": {"padding_chars": ">", "padding_count": 1}},
            {"type": "custom", "config": {"suffix": "<"}},
        ]
        _, final = _execute_chain_steps(["hi"], steps)
        assert final[0] == ">hi<"

    def test_three_step_chain(self):
        steps = [
            {"type": "custom", "config": {"prefix": "["}},
            {"type": "custom", "config": {"suffix": "]"}},
            {"type": "regex", "config": {"patterns": [{"find": r"\[", "replace": "("}]}},
        ]
        _, final = _execute_chain_steps(["x"], steps)
        # Step 1: "[x", Step 2: "[x]", Step 3: "(x]"
        assert final[0] == "(x]"

    def test_intermediates_track_each_step(self):
        steps = [
            {"type": "custom", "config": {"prefix": "A"}},
            {"type": "custom", "config": {"prefix": "B"}},
        ]
        intermediates, final = _execute_chain_steps(["x"], steps)
        assert len(intermediates) == 2
        assert intermediates[0]["sample_before"] == "x"
        assert intermediates[0]["sample_after"] == "Ax"
        assert intermediates[1]["sample_before"] == "Ax"
        assert intermediates[1]["sample_after"] == "BAx"
        assert final[0] == "BAx"

    def test_multiple_prompts_through_chain(self):
        steps = [
            {"type": "custom", "config": {"prefix": ">"}},
        ]
        _, final = _execute_chain_steps(["a", "b", "c"], steps)
        assert final == [">a", ">b", ">c"]


# =============================================================================
# Edge cases
# =============================================================================


class TestChainEdgeCases:
    """Edge cases for chain execution."""

    def test_empty_steps(self):
        intermediates, final = _execute_chain_steps(["hello"], [])
        assert intermediates == []
        assert final == ["hello"]

    def test_empty_prompts(self):
        steps = [{"type": "custom", "config": {"prefix": ">"}}]
        intermediates, final = _execute_chain_steps([], steps)
        assert len(intermediates) == 1
        assert final == []

    def test_unknown_step_type_passthrough(self):
        steps = [{"type": "nonexistent", "config": {}}]
        intermediates, final = _execute_chain_steps(["hello"], steps)
        assert len(intermediates) == 1
        assert intermediates[0]["step"] == "nonexistent"
        # Unknown type: none of the if/elif branches match, so current is unchanged
        assert final == ["hello"]

    def test_missing_config_key(self):
        steps = [{"type": "encode"}]
        # config defaults to {} → encoding_type defaults to "base64"
        _, final = _execute_chain_steps(["hello"], steps)
        payload = final[0].split("\n\n", 1)[1]
        assert base64.b64decode(payload).decode("utf-8") == "hello"
