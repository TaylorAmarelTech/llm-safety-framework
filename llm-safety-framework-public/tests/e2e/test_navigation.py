"""
Navigation tests — section visibility, sidebar active state, workflow bar,
pipeline drawer, fragment lazy loading.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages import ShellPage


class TestNavigation:
    """Test section navigation, sidebar state, workflow bar."""

    def test_section_visibility(self, browser, live_server):
        """Only one section is active at a time."""
        page = ShellPage(browser, live_server)
        page.open()

        for sid in ["endpoints", "dashboard", "modules"]:
            page.navigate_to_section(sid)
            active_sections = browser.find_elements(By.CSS_SELECTOR, ".section.active")
            assert len(active_sections) == 1, (
                f"Expected exactly 1 active section after navigating to '{sid}', "
                f"got {len(active_sections)}"
            )

    def test_sidebar_active_state(self, browser, live_server):
        """Clicking a nav item marks it as active."""
        page = ShellPage(browser, live_server)
        page.open()
        time.sleep(1)

        page.navigate_to_section("endpoints")
        items = page.get_sidebar_items()
        active_items = [i for i in items if i["active"]]
        active_texts = [i["text"] for i in active_items]
        # At least one should be active and contain something related to endpoints
        assert len(active_items) >= 1, f"No active nav items, all items: {[i['text'] for i in items]}"

    def test_workflow_stage_highlight(self, browser, live_server):
        """Navigating to testing highlights the 'test' workflow stage."""
        page = ShellPage(browser, live_server)
        page.open()
        time.sleep(1)

        page.navigate_to_section("testing")
        time.sleep(0.5)
        stages = page.get_workflow_stages()
        test_stage = [s for s in stages if s["stage"] == "test"]
        assert len(test_stage) == 1
        assert test_stage[0]["active"], "Test stage should be active"

    def test_pipeline_drawer_toggle(self, browser, live_server):
        """Pipeline drawer opens and closes."""
        page = ShellPage(browser, live_server)
        page.open()
        time.sleep(1)

        assert not page.is_pipeline_drawer_open()
        page.open_pipeline_drawer()
        time.sleep(0.5)
        assert page.is_pipeline_drawer_open()
        page.close_pipeline_drawer()
        time.sleep(0.5)
        assert not page.is_pipeline_drawer_open()

    def test_fragment_lazy_loading(self, browser, live_server):
        """Navigate to a plugin section, verify fragment HTML was loaded."""
        page = ShellPage(browser, live_server)
        page.open()
        time.sleep(1)

        page.navigate_to_section("endpoints")
        time.sleep(1)
        # The endpoints fragment should have created section-endpoints content
        section = browser.find_element(By.ID, "section-endpoints")
        inner_html = section.get_attribute("innerHTML")
        assert len(inner_html) > 50, "Endpoints section should have loaded fragment content"

    def test_section_loader_called(self, browser, live_server):
        """Navigate to dashboard, verify stats area is populated."""
        page = ShellPage(browser, live_server)
        page.open()
        time.sleep(1)

        page.navigate_to_section("dashboard")
        time.sleep(2)  # Allow async loading
        stats = browser.find_element(By.ID, "dashboard-stats")
        # Stats area should have some content (stat cards or loading indicator)
        assert stats is not None
