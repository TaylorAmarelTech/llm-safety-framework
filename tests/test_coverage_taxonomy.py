"""
Tests for coverage taxonomy completeness.

Validates that CATEGORY_TAXONOMY in coverage.py is complete and correct:
1. Every actual mutator category is in the taxonomy
2. No orphan entries (taxonomy entries without matching mutators)
3. All defense layers and technique classes are valid enum values
4. Each taxonomy entry has at least one mutator
5. CoverageAnalyzer runs without error
"""

import pytest

from src.prompt_injection import list_mutators, get_mutators_by_category
from src.prompt_injection.coverage import (
    ALL_DEFENSE_LAYERS,
    ALL_TECHNIQUE_CLASSES,
    CATEGORY_TAXONOMY,
    CoverageAnalyzer,
    CoverageReport,
)


# ═══════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════


def _actual_categories() -> set[str]:
    """Categories that actually have registered mutators."""
    return set(m["category"] for m in list_mutators().values())


def _taxonomy_categories() -> set[str]:
    """Categories defined in CATEGORY_TAXONOMY."""
    return set(CATEGORY_TAXONOMY.keys())


# ═══════════════════════════════════════════════════════════════════════
# 1. Completeness
# ═══════════════════════════════════════════════════════════════════════


class TestTaxonomyCompleteness:
    def test_all_actual_categories_in_taxonomy(self):
        """Every category from list_mutators() must be in CATEGORY_TAXONOMY."""
        actual = _actual_categories()
        taxonomy = _taxonomy_categories()
        missing = actual - taxonomy
        assert not missing, (
            f"Categories with registered mutators but missing from "
            f"CATEGORY_TAXONOMY: {missing}"
        )

    def test_no_orphan_taxonomy_entries(self):
        """Every entry in CATEGORY_TAXONOMY should have at least one mutator."""
        actual = _actual_categories()
        taxonomy = _taxonomy_categories()
        orphans = taxonomy - actual
        assert not orphans, (
            f"CATEGORY_TAXONOMY entries without any registered mutators: {orphans}"
        )

    def test_taxonomy_has_at_least_48_entries(self):
        """Taxonomy should have entries for all 48 categories."""
        assert len(CATEGORY_TAXONOMY) >= 52

    def test_actual_categories_match_taxonomy_count(self):
        """Number of actual categories should equal taxonomy entries."""
        actual = _actual_categories()
        taxonomy = _taxonomy_categories()
        assert actual == taxonomy, (
            f"Mismatch: actual={actual - taxonomy}, taxonomy_only={taxonomy - actual}"
        )


# ═══════════════════════════════════════════════════════════════════════
# 2. Validity
# ═══════════════════════════════════════════════════════════════════════


class TestTaxonomyValidity:
    @pytest.mark.parametrize("category", list(CATEGORY_TAXONOMY.keys()))
    def test_defense_layers_valid(self, category):
        """All defense_layers in taxonomy entries are from ALL_DEFENSE_LAYERS."""
        layers = CATEGORY_TAXONOMY[category]["defense_layers"]
        for layer in layers:
            assert layer in ALL_DEFENSE_LAYERS, (
                f"Category '{category}' has invalid defense_layer: '{layer}'"
            )

    @pytest.mark.parametrize("category", list(CATEGORY_TAXONOMY.keys()))
    def test_technique_classes_valid(self, category):
        """All technique_classes in taxonomy entries are from ALL_TECHNIQUE_CLASSES."""
        classes = CATEGORY_TAXONOMY[category]["technique_classes"]
        for cls in classes:
            assert cls in ALL_TECHNIQUE_CLASSES, (
                f"Category '{category}' has invalid technique_class: '{cls}'"
            )

    @pytest.mark.parametrize("category", list(CATEGORY_TAXONOMY.keys()))
    def test_has_at_least_one_defense_layer(self, category):
        """Each taxonomy entry must have at least one defense layer."""
        assert len(CATEGORY_TAXONOMY[category]["defense_layers"]) >= 1

    @pytest.mark.parametrize("category", list(CATEGORY_TAXONOMY.keys()))
    def test_has_at_least_one_technique_class(self, category):
        """Each taxonomy entry must have at least one technique class."""
        assert len(CATEGORY_TAXONOMY[category]["technique_classes"]) >= 1

    @pytest.mark.parametrize("category", list(CATEGORY_TAXONOMY.keys()))
    def test_category_has_at_least_one_mutator(self, category):
        """Each taxonomy category must have >= 1 registered mutator."""
        mutators = get_mutators_by_category(category)
        assert len(mutators) >= 1, (
            f"Category '{category}' is in taxonomy but has 0 mutators"
        )


# ═══════════════════════════════════════════════════════════════════════
# 3. CoverageAnalyzer
# ═══════════════════════════════════════════════════════════════════════


class TestCoverageAnalyzer:
    def test_analyze_returns_report(self):
        analyzer = CoverageAnalyzer()
        report = analyzer.analyze()
        assert isinstance(report, CoverageReport)

    def test_total_mutators(self):
        analyzer = CoverageAnalyzer()
        report = analyzer.analyze()
        assert report.total_mutators >= 598

    def test_total_categories(self):
        analyzer = CoverageAnalyzer()
        report = analyzer.analyze()
        assert report.total_categories >= 52

    def test_defense_layer_coverage_all_present(self):
        analyzer = CoverageAnalyzer()
        report = analyzer.analyze()
        for layer in ALL_DEFENSE_LAYERS:
            assert layer in report.defense_layer_coverage

    def test_technique_class_coverage_all_present(self):
        analyzer = CoverageAnalyzer()
        report = analyzer.analyze()
        for cls in ALL_TECHNIQUE_CLASSES:
            assert cls in report.technique_class_coverage

    def test_coverage_score_between_0_and_1(self):
        analyzer = CoverageAnalyzer()
        report = analyzer.analyze()
        assert 0.0 <= report.coverage_score <= 1.0

    def test_cross_coverage_matrix_shape(self):
        analyzer = CoverageAnalyzer()
        report = analyzer.analyze()
        assert len(report.cross_coverage_matrix) == len(ALL_DEFENSE_LAYERS)
        for layer in ALL_DEFENSE_LAYERS:
            assert len(report.cross_coverage_matrix[layer]) == len(ALL_TECHNIQUE_CLASSES)

    def test_to_dict(self):
        analyzer = CoverageAnalyzer()
        report = analyzer.analyze()
        d = report.to_dict()
        assert "total_mutators" in d
        assert "coverage_score" in d

    def test_get_category_map(self):
        analyzer = CoverageAnalyzer()
        cat_map = analyzer.get_category_map()
        assert len(cat_map) >= 52
        for cat, info in cat_map.items():
            assert "defense_layers" in info
            assert "technique_classes" in info
            assert "mutator_count" in info

    def test_suggest_new_mutators(self):
        analyzer = CoverageAnalyzer()
        suggestions = analyzer.suggest_new_mutators()
        assert isinstance(suggestions, list)
        for s in suggestions:
            assert "defense_layer" in s
            assert "technique_class" in s
            assert "suggestion" in s
