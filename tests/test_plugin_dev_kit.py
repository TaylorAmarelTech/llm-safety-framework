"""
Tests for the Plugin Development Kit.

Validates:
1. create_plugin generates all expected files
2. Generated files have correct placeholder substitution
3. Generated __init__.py has a valid manifest structure
4. Generated routes.py has a router
5. Generated HTML/JS fragments are valid
6. Custom parameters work (api_prefix, nav_group, order)
7. Duplicate detection (FileExistsError)
"""

import pytest

from src.web.plugin_dev_kit.create_plugin import create_plugin


# ═══════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════


@pytest.fixture
def generated_plugin(tmp_path):
    """Generate a test plugin and return its path."""
    plugin_path = create_plugin(
        "test_attack",
        display_name="Test Attack Plugin",
        api_prefix="/test-attack",
        nav_group="TRANSFORM",
        order=750,
        output_dir=tmp_path / "test_attack",
    )
    return plugin_path


# ═══════════════════════════════════════════════════════════════════════
# 1. File Generation
# ═══════════════════════════════════════════════════════════════════════


class TestFileGeneration:
    def test_creates_directory(self, generated_plugin):
        assert generated_plugin.is_dir()

    def test_creates_init(self, generated_plugin):
        assert (generated_plugin / "__init__.py").exists()

    def test_creates_routes(self, generated_plugin):
        assert (generated_plugin / "routes.py").exists()

    def test_creates_fragment_html(self, generated_plugin):
        assert (generated_plugin / "static" / "fragment.html").exists()

    def test_creates_fragment_js(self, generated_plugin):
        assert (generated_plugin / "static" / "fragment.js").exists()

    def test_all_files_non_empty(self, generated_plugin):
        for path in [
            generated_plugin / "__init__.py",
            generated_plugin / "routes.py",
            generated_plugin / "static" / "fragment.html",
            generated_plugin / "static" / "fragment.js",
        ]:
            assert path.stat().st_size > 50, f"File too small: {path}"


# ═══════════════════════════════════════════════════════════════════════
# 2. Placeholder Substitution
# ═══════════════════════════════════════════════════════════════════════


class TestPlaceholderSubstitution:
    def test_init_contains_plugin_id(self, generated_plugin):
        text = (generated_plugin / "__init__.py").read_text()
        assert 'id="test_attack"' in text

    def test_init_contains_display_name(self, generated_plugin):
        text = (generated_plugin / "__init__.py").read_text()
        assert 'name="Test Attack Plugin"' in text

    def test_init_contains_api_prefix(self, generated_plugin):
        text = (generated_plugin / "__init__.py").read_text()
        assert 'api_prefix="/test-attack"' in text

    def test_init_contains_nav_group(self, generated_plugin):
        text = (generated_plugin / "__init__.py").read_text()
        assert 'group="TRANSFORM"' in text

    def test_init_contains_order(self, generated_plugin):
        text = (generated_plugin / "__init__.py").read_text()
        assert "order=750" in text

    def test_routes_contains_plugin_id(self, generated_plugin):
        text = (generated_plugin / "routes.py").read_text()
        assert "test_attack" in text

    def test_html_contains_section_id(self, generated_plugin):
        text = (generated_plugin / "static" / "fragment.html").read_text()
        assert 'id="section-test_attack"' in text

    def test_js_contains_api_prefix(self, generated_plugin):
        text = (generated_plugin / "static" / "fragment.js").read_text()
        assert "/api/test-attack" in text

    def test_js_contains_section_loader(self, generated_plugin):
        text = (generated_plugin / "static" / "fragment.js").read_text()
        assert "SECTION_LOADERS" in text

    def test_no_unresolved_placeholders(self, generated_plugin):
        """No $PLACEHOLDER_NAME should remain after substitution."""
        for path in [
            generated_plugin / "__init__.py",
            generated_plugin / "routes.py",
            generated_plugin / "static" / "fragment.html",
            generated_plugin / "static" / "fragment.js",
        ]:
            text = path.read_text()
            # $PLUGIN_ID etc. should have been replaced
            assert "$PLUGIN_ID" not in text, f"Unresolved $PLUGIN_ID in {path.name}"
            assert "$DISPLAY_NAME" not in text, f"Unresolved $DISPLAY_NAME in {path.name}"
            assert "$API_PREFIX" not in text, f"Unresolved $API_PREFIX in {path.name}"


# ═══════════════════════════════════════════════════════════════════════
# 3. Generated Code Structure
# ═══════════════════════════════════════════════════════════════════════


class TestGeneratedStructure:
    def test_init_has_manifest(self, generated_plugin):
        text = (generated_plugin / "__init__.py").read_text()
        assert "manifest = PluginManifest" in text

    def test_init_has_router_import(self, generated_plugin):
        text = (generated_plugin / "__init__.py").read_text()
        assert "from .routes import router" in text

    def test_routes_has_router(self, generated_plugin):
        text = (generated_plugin / "routes.py").read_text()
        assert "router = APIRouter()" in text

    def test_routes_has_status_endpoint(self, generated_plugin):
        text = (generated_plugin / "routes.py").read_text()
        assert "@router.get" in text
        assert "/status" in text

    def test_routes_has_crud(self, generated_plugin):
        text = (generated_plugin / "routes.py").read_text()
        assert "/items" in text

    def test_html_has_section_div(self, generated_plugin):
        text = (generated_plugin / "static" / "fragment.html").read_text()
        assert 'class="section"' in text

    def test_js_has_eschtml(self, generated_plugin):
        text = (generated_plugin / "static" / "fragment.js").read_text()
        assert "escHtml" in text


# ═══════════════════════════════════════════════════════════════════════
# 4. Custom Parameters
# ═══════════════════════════════════════════════════════════════════════


class TestCustomParameters:
    def test_default_display_name(self, tmp_path):
        path = create_plugin("my_cool_attack", output_dir=tmp_path / "my_cool_attack")
        text = (path / "__init__.py").read_text()
        assert "My Cool Attack" in text

    def test_default_api_prefix(self, tmp_path):
        path = create_plugin("my_plugin", output_dir=tmp_path / "my_plugin")
        text = (path / "__init__.py").read_text()
        assert "/my-plugin" in text

    def test_custom_nav_group(self, tmp_path):
        path = create_plugin(
            "test_eval",
            nav_group="EVALUATE",
            output_dir=tmp_path / "test_eval",
        )
        text = (path / "__init__.py").read_text()
        assert 'group="EVALUATE"' in text
        assert 'workflow_stage="evaluate"' in text


# ═══════════════════════════════════════════════════════════════════════
# 5. Error Handling
# ═══════════════════════════════════════════════════════════════════════


class TestErrorHandling:
    def test_duplicate_raises(self, tmp_path):
        create_plugin("dupe", output_dir=tmp_path / "dupe")
        with pytest.raises(FileExistsError):
            create_plugin("dupe", output_dir=tmp_path / "dupe")
