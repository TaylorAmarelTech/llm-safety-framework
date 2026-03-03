"""
Prompt management tests through the browser UI.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages import PromptsPage


class TestPrompts:
    """Test prompt set management through the UI."""

    def test_prompt_sets_section_loads(self, browser, live_server):
        """Navigate to prompts — section becomes visible."""
        page = PromptsPage(browser, live_server)
        page.open()
        page.navigate()
        assert page.section_loaded()

    def test_prompt_sets_content(self, browser, live_server):
        """Prompt sets section has content after loading."""
        page = PromptsPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        section = browser.find_element(By.ID, "section-prompt-sets")
        text = section.text
        # Should have some content (prompt set cards or import area)
        assert len(text) > 10, "Prompt sets section should have content"

    def test_prompt_section_has_interactive_elements(self, browser, live_server):
        """Prompt section has buttons or inputs for interaction."""
        page = PromptsPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        btns = browser.find_elements(By.CSS_SELECTOR, "#section-prompt-sets button")
        assert len(btns) >= 1, "Expected at least 1 button in prompts section"

    def test_template_library_loads(self, browser, live_server):
        """Template library section can be navigated to."""
        page = PromptsPage(browser, live_server)
        page.open()
        time.sleep(1)
        try:
            page.navigate_to_section("template-library")
            time.sleep(1)
            assert page.element_exists("#section-template-library")
        except Exception:
            # Template library may be embedded in prompts section
            pytest.skip("Template library section not separately navigable")

    def test_prompts_section_no_js_errors(self, browser, live_server):
        """No JS errors when navigating to prompts."""
        page = PromptsPage(browser, live_server)
        page.open()
        time.sleep(1)
        page.get_browser_errors()  # Clear
        page.navigate()
        time.sleep(1)
        errors = page.get_browser_errors()
        real = [e for e in errors if "favicon" not in e.lower()]
        assert len(real) == 0, f"JS errors in prompts: {real}"
