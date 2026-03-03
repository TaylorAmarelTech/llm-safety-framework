"""
Transform workbench page object — tab switching, spintax, regex.
"""

from __future__ import annotations

from selenium.webdriver.common.by import By

from .base_page import BasePage


class TransformPage(BasePage):

    def navigate(self) -> None:
        self.navigate_to_section("transform")

    def get_tab_names(self) -> list[str]:
        tabs = self.driver.find_elements(By.CSS_SELECTOR, "#section-transform .tab-btn, #section-transform .tw-tab")
        return [t.text.strip() for t in tabs if t.text.strip()]

    def get_active_tab(self) -> str:
        els = self.driver.find_elements(By.CSS_SELECTOR, "#section-transform .tab-btn.active, #section-transform .tw-tab.active")
        return els[0].text.strip() if els else ""

    def switch_tab(self, tab_text: str) -> None:
        tabs = self.driver.find_elements(By.CSS_SELECTOR, "#section-transform .tab-btn, #section-transform .tw-tab")
        for t in tabs:
            if t.text.strip().lower() == tab_text.lower():
                t.click()
                return

    def section_loaded(self) -> bool:
        return self.element_exists("#section-transform.active")
