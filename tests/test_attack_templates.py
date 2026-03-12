"""
Tests for the standardized attack template registry.

Validates:
1. AttackTemplate dataclass
2. AttackTemplateRegistry CRUD, filtering, search, stats
3. YAML load/export round-trip
4. extract_templates_from_mutator helper
5. auto_register_all_templates integration
6. Community template loading
"""

from pathlib import Path

import pytest

from src.prompt_injection.attack_templates import (
    TEMPLATE_REGISTRY,
    AttackTemplate,
    AttackTemplateRegistry,
    auto_register_all_templates,
    extract_templates_from_mutator,
)


# ═══════════════════════════════════════════════════════════════════════
# 1. AttackTemplate Dataclass
# ═══════════════════════════════════════════════════════════════════════


class TestAttackTemplate:
    def test_create_minimal(self):
        t = AttackTemplate(
            id="test__v1",
            name="Test Template v1",
            template_str="Preamble {prompt} postamble",
            category="test_category",
        )
        assert t.id == "test__v1"
        assert t.defense_layers == []
        assert t.tags == []

    def test_render(self):
        t = AttackTemplate(
            id="t1",
            name="T1",
            template_str="Before {prompt} After",
            category="c",
        )
        result = t.render("payload")
        assert result == "Before payload After"

    def test_render_multiple_placeholders(self):
        t = AttackTemplate(
            id="t2",
            name="T2",
            template_str="{prompt} and again {prompt}",
            category="c",
        )
        result = t.render("X")
        assert result == "X and again X"

    def test_render_no_placeholder(self):
        t = AttackTemplate(
            id="t3",
            name="T3",
            template_str="No placeholder here",
            category="c",
        )
        result = t.render("X")
        assert result == "No placeholder here"

    def test_to_dict(self):
        t = AttackTemplate(
            id="t4",
            name="T4",
            template_str="T {prompt}",
            category="c",
            defense_layers=["alignment"],
            tags=["tag1"],
        )
        d = t.to_dict()
        assert d["id"] == "t4"
        assert d["defense_layers"] == ["alignment"]
        assert d["tags"] == ["tag1"]


# ═══════════════════════════════════════════════════════════════════════
# 2. AttackTemplateRegistry CRUD
# ═══════════════════════════════════════════════════════════════════════


@pytest.fixture
def fresh_registry():
    return AttackTemplateRegistry()


class TestRegistryCRUD:
    def test_register_and_get(self, fresh_registry):
        t = AttackTemplate(id="r1", name="R1", template_str="T {prompt}", category="c")
        fresh_registry.register(t)
        assert fresh_registry.get("r1") is t

    def test_get_nonexistent_raises(self, fresh_registry):
        with pytest.raises(KeyError):
            fresh_registry.get("nonexistent")

    def test_get_optional_returns_none(self, fresh_registry):
        assert fresh_registry.get_optional("nonexistent") is None

    def test_register_many(self, fresh_registry):
        templates = [
            AttackTemplate(id=f"rm_{i}", name=f"RM{i}", template_str=f"T{i} {{prompt}}", category="c")
            for i in range(5)
        ]
        count = fresh_registry.register_many(templates)
        assert count == 5
        assert len(fresh_registry) == 5

    def test_all_templates(self, fresh_registry):
        for i in range(3):
            fresh_registry.register(
                AttackTemplate(id=f"a{i}", name=f"A{i}", template_str=f"T {{prompt}}", category="c")
            )
        assert len(fresh_registry.all_templates()) == 3

    def test_overwrite_duplicate(self, fresh_registry):
        t1 = AttackTemplate(id="dup", name="V1", template_str="old {prompt}", category="c")
        t2 = AttackTemplate(id="dup", name="V2", template_str="new {prompt}", category="c")
        fresh_registry.register(t1)
        fresh_registry.register(t2)
        assert fresh_registry.get("dup").name == "V2"
        assert len(fresh_registry) == 1


# ═══════════════════════════════════════════════════════════════════════
# 3. Filtering and Search
# ═══════════════════════════════════════════════════════════════════════


@pytest.fixture
def populated_registry():
    reg = AttackTemplateRegistry()
    reg.register(AttackTemplate(
        id="f1__v1", name="Fallacy V1", template_str="T {prompt}",
        category="logical_fallacy",
        defense_layers=["reasoning"],
        technique_classes=["cognitive"],
        tags=["fallacy", "academic"],
    ))
    reg.register(AttackTemplate(
        id="f1__v2", name="Fallacy V2", template_str="T {prompt}",
        category="logical_fallacy",
        defense_layers=["reasoning", "alignment"],
        technique_classes=["cognitive", "social_engineering"],
        tags=["fallacy"],
    ))
    reg.register(AttackTemplate(
        id="e1__v1", name="Encoding V1", template_str="T {prompt}",
        category="encoding_format",
        defense_layers=["input_filter"],
        technique_classes=["encoding"],
        tags=["encoding", "base64"],
    ))
    return reg


class TestFiltering:
    def test_list_by_category(self, populated_registry):
        results = populated_registry.list_by_category("logical_fallacy")
        assert len(results) == 2

    def test_list_by_category_empty(self, populated_registry):
        results = populated_registry.list_by_category("nonexistent")
        assert len(results) == 0

    def test_list_by_defense_layer(self, populated_registry):
        results = populated_registry.list_by_defense_layer("reasoning")
        assert len(results) == 2

    def test_list_by_technique_class(self, populated_registry):
        results = populated_registry.list_by_technique_class("encoding")
        assert len(results) == 1

    def test_list_by_tag(self, populated_registry):
        results = populated_registry.list_by_tag("fallacy")
        assert len(results) == 2

    def test_search_by_name(self, populated_registry):
        results = populated_registry.search("fallacy")
        assert len(results) == 2

    def test_search_by_tag(self, populated_registry):
        results = populated_registry.search("base64")
        assert len(results) == 1

    def test_search_case_insensitive(self, populated_registry):
        results = populated_registry.search("FALLACY")
        assert len(results) == 2


class TestStats:
    def test_stats_structure(self, populated_registry):
        s = populated_registry.stats()
        assert "total" in s
        assert "by_category" in s
        assert "by_defense_layer" in s
        assert "by_technique_class" in s

    def test_stats_total(self, populated_registry):
        assert populated_registry.stats()["total"] == 3

    def test_stats_by_category(self, populated_registry):
        assert populated_registry.stats()["by_category"]["logical_fallacy"] == 2


# ═══════════════════════════════════════════════════════════════════════
# 4. YAML Load/Export
# ═══════════════════════════════════════════════════════════════════════


class TestYAMLIO:
    def test_load_yaml(self, fresh_registry, tmp_path):
        yaml_file = tmp_path / "templates.yaml"
        yaml_file.write_text(
            "templates:\n"
            "  - id: yaml_t1\n"
            "    name: YAML Template 1\n"
            "    template_str: 'Before {prompt} after'\n"
            "    category: test_yaml\n"
            "    defense_layers: [alignment]\n"
            "    tags: [yaml, test]\n",
            encoding="utf-8",
        )
        count = fresh_registry.load_yaml(yaml_file)
        assert count == 1
        t = fresh_registry.get("yaml_t1")
        assert t.category == "test_yaml"
        assert "alignment" in t.defense_layers

    def test_load_yaml_missing_file(self, fresh_registry, tmp_path):
        count = fresh_registry.load_yaml(tmp_path / "nonexistent.yaml")
        assert count == 0

    def test_load_yaml_empty(self, fresh_registry, tmp_path):
        yaml_file = tmp_path / "empty.yaml"
        yaml_file.write_text("", encoding="utf-8")
        count = fresh_registry.load_yaml(yaml_file)
        assert count == 0

    def test_export_yaml_round_trip(self, populated_registry, tmp_path):
        export_path = tmp_path / "export.yaml"
        count = populated_registry.export_yaml(export_path)
        assert count == 3

        # Reload into fresh registry
        fresh = AttackTemplateRegistry()
        loaded = fresh.load_yaml(export_path)
        assert loaded == 3

    def test_export_yaml_filtered(self, populated_registry, tmp_path):
        export_path = tmp_path / "filtered.yaml"
        count = populated_registry.export_yaml(export_path, category="logical_fallacy")
        assert count == 2

    def test_load_community_templates(self):
        """Load the bundled community sample templates."""
        reg = AttackTemplateRegistry()
        sample_path = Path(__file__).parent.parent / "templates" / "community" / "sample_templates.yaml"
        if sample_path.exists():
            count = reg.load_yaml(sample_path)
            assert count >= 3
            t = reg.get("community__academic_review_framing")
            assert "{prompt}" in t.template_str


# ═══════════════════════════════════════════════════════════════════════
# 5. extract_templates_from_mutator
# ═══════════════════════════════════════════════════════════════════════


class TestExtractTemplates:
    def test_extract_from_class_with_templates(self):
        class FakeMutator:
            NAME = "fake_test"
            CATEGORY = "test"
            DESCRIPTION = "Test mutator"
            TEMPLATES = [
                ("v1", "Template 1 {prompt}"),
                ("v2", "Template 2 {prompt}"),
            ]

        results = extract_templates_from_mutator(FakeMutator, "test")
        assert len(results) == 2
        assert results[0].id == "fake_test__v1"
        assert results[1].id == "fake_test__v2"
        assert "{prompt}" in results[0].template_str

    def test_extract_from_class_without_templates(self):
        class NoTemplates:
            NAME = "no_tmpl"
        results = extract_templates_from_mutator(NoTemplates, "test")
        assert len(results) == 0

    def test_extracted_templates_have_category(self):
        class FakeMutator:
            NAME = "fake"
            TEMPLATES = [("v1", "T {prompt}")]
        results = extract_templates_from_mutator(FakeMutator, "my_category")
        assert results[0].category == "my_category"

    def test_extracted_templates_have_tags(self):
        class FakeMutator:
            NAME = "fake"
            TEMPLATES = [("v1", "T {prompt}")]
        results = extract_templates_from_mutator(FakeMutator, "cat")
        assert "fake" in results[0].tags
        assert "v1" in results[0].tags


# ═══════════════════════════════════════════════════════════════════════
# 6. auto_register_all_templates Integration
# ═══════════════════════════════════════════════════════════════════════


class TestAutoRegister:
    def test_auto_register_populates_registry(self):
        count = auto_register_all_templates()
        # Many mutators have TEMPLATES attributes
        assert count >= 50, f"Expected >= 50 auto-registered templates, got {count}"

    def test_registry_has_templates_after_auto_register(self):
        auto_register_all_templates()
        assert len(TEMPLATE_REGISTRY) >= 50

    def test_fallacy_templates_registered(self):
        auto_register_all_templates()
        fallacy = TEMPLATE_REGISTRY.list_by_category("logical_fallacy")
        assert len(fallacy) >= 10, f"Expected >= 10 fallacy templates, got {len(fallacy)}"

    def test_stats_after_auto_register(self):
        auto_register_all_templates()
        stats = TEMPLATE_REGISTRY.stats()
        assert stats["total"] >= 50
        assert len(stats["by_category"]) >= 3
