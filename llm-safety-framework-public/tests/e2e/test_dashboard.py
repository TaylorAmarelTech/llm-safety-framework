"""
Dashboard tests through the browser UI.
"""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .pages import DashboardPage


class TestDashboard:
    """Test the dashboard section through the UI."""

    def test_dashboard_loads(self, browser, live_server):
        """Navigate to dashboard — section becomes visible."""
        page = DashboardPage(browser, live_server)
        page.open()
        page.navigate()
        assert page.section_loaded()

    def test_readiness_checklist(self, browser, live_server):
        """Dashboard has readiness checklist items."""
        page = DashboardPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(2)  # Allow async data loading
        items = page.get_readiness_items()
        assert len(items) >= 1, "Expected at least 1 readiness checklist item"

    def test_dashboard_chart_canvases(self, browser, live_server):
        """Dashboard has chart canvas elements."""
        page = DashboardPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        assert page.is_chart_rendered("chart-safety"), "chart-safety canvas should exist"
        assert page.is_chart_rendered("chart-categories"), "chart-categories canvas should exist"

    def test_dashboard_recent_runs_area(self, browser, live_server):
        """Dashboard has a recent runs area."""
        page = DashboardPage(browser, live_server)
        page.open()
        page.navigate()
        time.sleep(1)
        runs_area = page.get_recent_runs_area()
        assert len(runs_area) >= 1, "Recent runs area should exist"
