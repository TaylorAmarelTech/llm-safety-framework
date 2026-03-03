"""
Shell page object — sidebar, mode switch, workflow bar, context bar.
"""

from __future__ import annotations

from selenium.webdriver.common.by import By

from .base_page import BasePage


class ShellPage(BasePage):

    def get_workflow_stages(self) -> list[dict]:
        """Return workflow stage elements with their state."""
        els = self.driver.find_elements(By.CSS_SELECTOR, ".workflow-stage")
        return [
            {
                "stage": el.get_attribute("data-stage") or "",
                "text": el.text.strip(),
                "active": "active" in (el.get_attribute("class") or ""),
                "completed": "completed" in (el.get_attribute("class") or ""),
            }
            for el in els
        ]

    def switch_mode(self, mode: str) -> None:
        """Switch between 'streamlined' and 'advanced'."""
        self.driver.execute_script(f"switchMode('{mode}')")

    def get_current_mode(self) -> str:
        active = self.driver.find_elements(By.CSS_SELECTOR, ".mode-btn.active")
        if active:
            return active[0].get_attribute("data-mode") or ""
        return ""

    def get_module_cards(self) -> list[dict]:
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".module-tile")
        return [
            {"title": c.find_element(By.CSS_SELECTOR, ".mt-title").text}
            for c in cards
        ]

    def open_pipeline_drawer(self) -> None:
        self.driver.execute_script("togglePipelineDrawer()")

    def close_pipeline_drawer(self) -> None:
        self.driver.execute_script("togglePipelineDrawer()")

    def is_pipeline_drawer_open(self) -> bool:
        els = self.driver.find_elements(By.CSS_SELECTOR, "#pipeline-drawer.open")
        return len(els) > 0
