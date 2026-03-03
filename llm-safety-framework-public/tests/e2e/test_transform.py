"""
Transform workbench tests — tab switching, section rendering.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages import TransformPage


class TestTransform:
    """Test the transform workbench through the UI."""

    def test_transform_section_loads(self, browser, live_server):
        """Navigate to transform — section becomes visible."""
        page = TransformPage(browser, live_server)
        page.open()
        page.navigate()
        assert page.section_loaded()

    def test_transform_has_tabs(self, browser, live_server):
        """Transform section has multiple tabs."""
        page = TransformPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        tabs = page.get_tab_names()
        assert len(tabs) >= 3, f"Expected ≥3 transform tabs, got {len(tabs)}: {tabs}"

    def test_tab_switching(self, browser, live_server):
        """Clicking different tabs changes the active panel."""
        page = TransformPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)

        tabs = page.get_tab_names()
        if len(tabs) < 2:
            pytest.skip("Not enough tabs to test switching")

        first_tab = tabs[0]
        second_tab = tabs[1]

        page.switch_tab(second_tab)
        time.sleep(0.3)
        # Active tab text should have changed
        active = page.get_active_tab()
        assert active.lower() == second_tab.lower(), f"Expected '{second_tab}' to be active, got '{active}'"

    def test_transform_has_textareas(self, browser, live_server):
        """Transform section has textarea inputs for prompts."""
        page = TransformPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        textareas = browser.find_elements(By.CSS_SELECTOR, "#section-transform textarea")
        assert len(textareas) >= 1, "Expected at least 1 textarea in transform section"

    def test_transform_has_action_buttons(self, browser, live_server):
        """Transform section has action buttons."""
        page = TransformPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        buttons = browser.find_elements(By.CSS_SELECTOR, "#section-transform button")
        assert len(buttons) >= 1, "Expected at least 1 button in transform section"

    def test_transform_no_js_errors(self, browser, live_server):
        """No JS errors when navigating to transform."""
        page = TransformPage(browser, live_server)
        page.open()
        time.sleep(1)
        page.get_browser_errors()  # Clear
        page.navigate()
        time.sleep(1)
        errors = page.get_browser_errors()
        real = [e for e in errors if "favicon" not in e.lower()]
        assert len(real) == 0, f"JS errors in transform: {real}"
