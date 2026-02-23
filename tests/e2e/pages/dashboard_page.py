"""
Dashboard page object — stats, readiness, heatmap.
"""

from __future__ import annotations

from selenium.webdriver.common.by import By

from .base_page import BasePage


class DashboardPage(BasePage):

    def navigate(self) -> None:
        self.navigate_to_section("dashboard")

    def get_stat_cards(self) -> list:
        return self.driver.find_elements(By.CSS_SELECTOR, "#dashboard-stats .stat-card")

    def get_readiness_items(self) -> list:
        return self.driver.find_elements(By.CSS_SELECTOR, "#dashboard-readiness .readiness-item")

    def is_chart_rendered(self, chart_id: str) -> bool:
        return self.element_exists(f"#{chart_id}")

    def get_recent_runs_area(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "#dashboard-recent-runs")

    def section_loaded(self) -> bool:
        return self.element_exists("#section-dashboard.active")
