"""
Analytics and testing section tests through the browser UI.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages import AnalyticsPage


class TestAnalytics:
    """Test testing and analytics sections through the UI."""

    def test_testing_section_loads(self, browser, live_server):
        """Navigate to testing — section becomes visible."""
        page = AnalyticsPage(browser, live_server)
        page.open()
        page.navigate_to_testing()
        assert page.testing_section_loaded()

    def test_analytics_section_loads(self, browser, live_server):
        """Navigate to analytics — section becomes visible."""
        page = AnalyticsPage(browser, live_server)
        page.open()
        page.navigate_to_analytics()
        assert page.analytics_section_loaded()

    def test_testing_has_content(self, browser, live_server):
        """Testing section has content after loading."""
        page = AnalyticsPage(browser, live_server)
        page.open()
        page.navigate_to_testing()
        time.sleep(1)
        section = browser.find_element(By.ID, "section-testing")
        text = section.text
        assert len(text) > 20, "Testing section should have content"

    def test_analytics_has_content(self, browser, live_server):
        """Analytics section has content after loading."""
        page = AnalyticsPage(browser, live_server)
        page.open()
        page.navigate_to_analytics()
        time.sleep(1)
        section = browser.find_element(By.ID, "section-analytics")
        text = section.text
        assert len(text) > 20, "Analytics section should have content"

    def test_analytics_no_js_errors(self, browser, live_server):
        """No JS errors when navigating to analytics."""
        page = AnalyticsPage(browser, live_server)
        page.open()
        time.sleep(1)
        page.get_browser_errors()  # Clear
        page.navigate_to_analytics()
        time.sleep(1)
        errors = page.get_browser_errors()
        real = [e for e in errors if "favicon" not in e.lower() and "chart.js" not in e.lower()]
        assert len(real) == 0, f"JS errors in analytics: {real}"
