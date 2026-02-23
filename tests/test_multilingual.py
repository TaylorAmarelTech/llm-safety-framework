"""
Tests for the multilingual attack module.
"""

import pytest

from src.spinning.multilingual import MultilingualAttacker


class TestLanguages:
    def test_language_count(self):
        assert len(MultilingualAttacker.LANGUAGES) == 21

    def test_all_languages_have_required_fields(self):
        for code, info in MultilingualAttacker.LANGUAGES.items():
            assert isinstance(code, str)
            assert "name" in info
            assert "resource_level" in info
            assert info["resource_level"] in ("high", "medium", "low")

    def test_high_resource_languages(self):
        high = [c for c, i in MultilingualAttacker.LANGUAGES.items() if i["resource_level"] == "high"]
        assert len(high) == 5

    def test_medium_resource_languages(self):
        medium = [c for c, i in MultilingualAttacker.LANGUAGES.items() if i["resource_level"] == "medium"]
        assert len(medium) == 7

    def test_low_resource_languages(self):
        low = [c for c, i in MultilingualAttacker.LANGUAGES.items() if i["resource_level"] == "low"]
        assert len(low) == 9

    def test_language_codes_unique(self):
        codes = list(MultilingualAttacker.LANGUAGES.keys())
        assert len(codes) == len(set(codes))


class TestMultilingualAttacker:
    def test_list_languages(self):
        langs = MultilingualAttacker.list_languages()
        assert isinstance(langs, list)
        assert len(langs) == 21
        for lang in langs:
            assert "code" in lang
            assert "name" in lang
            assert "resource_level" in lang

    def test_list_languages_structure(self):
        langs = MultilingualAttacker.list_languages()
        codes = [l["code"] for l in langs]
        # Should include some well-known codes
        assert "zh" in codes or "ar" in codes or "es" in codes

    def test_resource_level_distribution(self):
        langs = MultilingualAttacker.list_languages()
        by_level = {}
        for l in langs:
            level = l["resource_level"]
            by_level[level] = by_level.get(level, 0) + 1
        assert by_level["high"] == 5
        assert by_level["medium"] == 7
        assert by_level["low"] == 9
