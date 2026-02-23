"""
Prompts page object — list, toggle, import.
"""

from __future__ import annotations

import time

from selenium.webdriver.common.by import By

from .base_page import BasePage


class PromptsPage(BasePage):

    def navigate(self) -> None:
        self.navigate_to_section("prompt-sets")

    def get_prompt_set_cards(self) -> list:
        return self.driver.find_elements(By.CSS_SELECTOR, ".prompt-set-card, .ps-card")

    def section_loaded(self) -> bool:
        return self.element_exists("#section-prompt-sets.active")

    def has_template_library_section(self) -> bool:
        return self.element_exists("#section-template-library") or self.element_exists("[id*='template']")
