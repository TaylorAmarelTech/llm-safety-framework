"""
Endpoint CRUD tests through the browser UI.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages import EndpointsPage


class TestEndpoints:
    """Test endpoint management through the UI."""

    def test_endpoints_section_loads(self, browser, live_server):
        """Navigate to endpoints — section becomes visible."""
        page = EndpointsPage(browser, live_server)
        page.open()
        page.navigate()
        assert page.section_loaded()

    def test_endpoints_list_present(self, browser, live_server):
        """Endpoints list container exists after navigating."""
        page = EndpointsPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        # Should have an endpoints list area
        assert page.element_exists("#endpoints-list") or page.element_exists("#section-endpoints")

    def test_endpoints_section_has_content(self, browser, live_server):
        """Endpoints section renders content (form, list, or empty state)."""
        page = EndpointsPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        section = browser.find_element(By.ID, "section-endpoints")
        inner = section.get_attribute("innerHTML")
        # Should have substantial HTML content from the plugin fragment
        assert len(inner) > 100, "Endpoints section should have rendered fragment content"

    def test_endpoint_section_has_form_elements(self, browser, live_server):
        """Endpoints section has form inputs for creating/editing."""
        page = EndpointsPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        # Should have some input elements
        inputs = browser.find_elements(By.CSS_SELECTOR, "#section-endpoints input")
        assert len(inputs) >= 1, "Expected at least 1 input in endpoints section"

    def test_context_bar_shows_endpoints(self, browser, live_server):
        """Context bar shows endpoint count."""
        page = EndpointsPage(browser, live_server)
        page.open()
        time.sleep(2)  # Let context bar refresh
        ctx = page.get_context_bar_values()
        # Endpoints value should be present (may be 0 or more)
        assert ctx["endpoints"] is not None

    def test_endpoints_section_no_js_errors(self, browser, live_server):
        """No JS errors when navigating to endpoints."""
        page = EndpointsPage(browser, live_server)
        page.open()
        time.sleep(1)
        page.get_browser_errors()  # Clear initial
        page.navigate()
        time.sleep(1)
        errors = page.get_browser_errors()
        real = [e for e in errors if "favicon" not in e.lower()]
        assert len(real) == 0, f"JS errors in endpoints: {real}"
