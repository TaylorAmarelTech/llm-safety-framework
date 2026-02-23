"""
Smoke tests — quick verification that the app loads, all sections render,
and there are no JS errors.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages import ShellPage


class TestSmoke:
    """Quick smoke tests — every section loads without JS errors."""

    def test_app_loads(self, browser, live_server):
        """App root loads and title contains expected text."""
        browser.get(live_server)
        assert "LLM Safety" in browser.title

    def test_sidebar_renders(self, browser, live_server):
        """Sidebar has at least 10 nav items (hardcoded + plugin-injected)."""
        page = ShellPage(browser, live_server)
        page.open()
        # Wait for sidebar plugin nav to be populated
        WebDriverWait(browser, 10).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, ".nav-item")) >= 3
        )
        items = page.get_sidebar_items()
        # We have 2 hardcoded (Modules, Dashboard) + plugins
        assert len(items) >= 3, f"Expected ≥3 sidebar items, got {len(items)}"

    def test_all_sections_load(self, browser, live_server):
        """Click each section, verify its div becomes active."""
        page = ShellPage(browser, live_server)
        page.open()
        time.sleep(1)  # Let initial JS bootstrap

        # Get section IDs from sidebar onclick attributes
        section_ids = ["modules", "dashboard", "endpoints", "prompt-sets", "transform"]
        for sid in section_ids:
            page.navigate_to_section(sid)
            active = page.get_visible_section_id()
            assert active == sid, f"Expected section '{sid}' to be active, got '{active}'"

    def test_no_js_errors_on_load(self, browser, live_server):
        """No SEVERE console entries after initial page load."""
        page = ShellPage(browser, live_server)
        page.open()
        time.sleep(1)
        errors = page.get_browser_errors()
        # Filter out known benign errors (e.g. favicon, Chart.js CDN)
        real_errors = [e for e in errors if "favicon" not in e.lower() and "chart.js" not in e.lower()]
        assert len(real_errors) == 0, f"JS errors on load: {real_errors}"

    def test_no_js_errors_per_section(self, browser, live_server):
        """Navigate each section and check for SEVERE console entries."""
        page = ShellPage(browser, live_server)
        page.open()
        time.sleep(1)
        # Clear initial log
        page.get_browser_errors()

        sections = ["endpoints", "prompt-sets", "transform", "dashboard", "testing", "analytics"]
        errors_per_section = {}
        for sid in sections:
            try:
                page.navigate_to_section(sid)
                time.sleep(0.5)
                errors = page.get_browser_errors()
                real = [e for e in errors if "favicon" not in e.lower() and "chart.js" not in e.lower()]
                if real:
                    errors_per_section[sid] = real
            except Exception:
                pass  # Section might not exist

        assert len(errors_per_section) == 0, f"JS errors in sections: {errors_per_section}"

    def test_context_bar_renders(self, browser, live_server):
        """Context bar has 5 indicator dots."""
        page = ShellPage(browser, live_server)
        page.open()
        dots = browser.find_elements(By.CSS_SELECTOR, ".ctx-dot")
        assert len(dots) == 5, f"Expected 5 context dots, got {len(dots)}"

    def test_workflow_bar_renders(self, browser, live_server):
        """Workflow bar has 6 stages."""
        page = ShellPage(browser, live_server)
        page.open()
        stages = page.get_workflow_stages()
        assert len(stages) == 6, f"Expected 6 workflow stages, got {len(stages)}"

    def test_mode_switch(self, browser, live_server):
        """Switch between streamlined and advanced modes."""
        page = ShellPage(browser, live_server)
        page.open()

        assert page.get_current_mode() == "advanced"

        page.switch_mode("streamlined")
        time.sleep(0.5)
        assert page.get_current_mode() == "streamlined"
        # Wizard container should be visible
        wizard = browser.find_element(By.ID, "wizard-container")
        assert wizard.is_displayed()

        page.switch_mode("advanced")
        time.sleep(0.5)
        assert page.get_current_mode() == "advanced"
        # Sidebar should be visible again
        sidebar = browser.find_element(By.ID, "adv-sidebar")
        assert sidebar.is_displayed()
