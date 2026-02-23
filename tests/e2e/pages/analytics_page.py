"""
Analytics page object — stats, charts, run viewer.
"""

from __future__ import annotations

from selenium.webdriver.common.by import By

from .base_page import BasePage


class AnalyticsPage(BasePage):

    def navigate_to_testing(self) -> None:
        self.navigate_to_section("testing")

    def navigate_to_analytics(self) -> None:
        self.navigate_to_section("analytics")

    def testing_section_loaded(self) -> bool:
        return self.element_exists("#section-testing.active")

    def analytics_section_loaded(self) -> bool:
        return self.element_exists("#section-analytics.active")

    def get_run_history_elements(self) -> list:
        return self.driver.find_elements(By.CSS_SELECTOR, "#run-history table, #run-history .empty-state, #run-history")

    def is_chart_rendered(self, chart_id: str) -> bool:
        return self.element_exists(f"#{chart_id}")
