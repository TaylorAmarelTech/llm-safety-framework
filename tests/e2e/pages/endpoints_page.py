"""
Endpoints page object — CRUD, model management.
"""

from __future__ import annotations

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage


class EndpointsPage(BasePage):

    def navigate(self) -> None:
        self.navigate_to_section("endpoints")

    def get_endpoint_cards(self) -> list[dict]:
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".endpoint-card")
        result = []
        for c in cards:
            title_els = c.find_elements(By.CSS_SELECTOR, ".ep-name, h4, .ep-title")
            title = title_els[0].text if title_els else c.text[:40]
            result.append({"element": c, "title": title})
        return result

    def create_endpoint(self, ep_id: str, name: str, url: str, key: str) -> None:
        """Fill the create-endpoint form and submit."""
        self.fill_input("#new-ep-id", ep_id)
        self.fill_input("#new-ep-name", name)
        self.fill_input("#new-ep-url", url)
        self.fill_input("#new-ep-key", key)
        self.click("#btn-create-endpoint")
        time.sleep(0.5)

    def get_endpoint_list_element(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "#endpoints-list")

    def section_loaded(self) -> bool:
        return self.element_exists("#section-endpoints.active")
