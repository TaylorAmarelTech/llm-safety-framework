"""
Base page object with shared helpers for all pages.
"""

from __future__ import annotations

import logging
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

_log = logging.getLogger("e2e.pages")


class BasePage:
    """Shared navigation, wait, and inspection helpers."""

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url

    # ── Navigation ───────────────────────────────────────────────

    def open(self) -> None:
        """Navigate to the app root."""
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#sidebar-nav"))
        )

    def navigate_to_section(self, section_id: str) -> None:
        """Click the sidebar nav item and wait for the section div."""
        # Use JS to call showSection directly — more reliable than clicking nav items
        self.driver.execute_script(f"showSection('{section_id}')")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"#section-{section_id}.active"))
        )

    # ── Waits ────────────────────────────────────────────────────

    def wait_for(self, locator: tuple, timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_visible(self, css: str, timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css))
        )

    def wait_for_text(self, css: str, text: str, timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, css), text)
        )

    def wait_until_gone(self, css: str, timeout: int = 10) -> bool:
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, css))
        )

    # ── Element Interaction ──────────────────────────────────────

    def fill_input(self, css: str, value: str) -> None:
        el = self.wait_for_visible(css)
        el.clear()
        el.send_keys(value)

    def click(self, css: str) -> None:
        el = self.wait_for_visible(css)
        el.click()

    def get_text(self, css: str) -> str:
        return self.wait_for_visible(css).text

    def find_elements(self, css: str) -> list[WebElement]:
        return self.driver.find_elements(By.CSS_SELECTOR, css)

    def element_exists(self, css: str) -> bool:
        return len(self.driver.find_elements(By.CSS_SELECTOR, css)) > 0

    # ── Toast ────────────────────────────────────────────────────

    def get_toast_message(self, timeout: int = 5) -> str:
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#toast.show"))
            )
            return el.text
        except Exception:
            return ""

    # ── Section / Sidebar ────────────────────────────────────────

    def get_visible_section_id(self) -> Optional[str]:
        """Return the ID (minus 'section-' prefix) of the currently active section."""
        els = self.driver.find_elements(By.CSS_SELECTOR, ".section.active")
        if els:
            full_id = els[0].get_attribute("id") or ""
            return full_id.replace("section-", "") if full_id.startswith("section-") else full_id
        return None

    def get_sidebar_items(self) -> list[dict]:
        items = self.driver.find_elements(By.CSS_SELECTOR, ".nav-item")
        result = []
        for el in items:
            result.append({
                "text": el.text.strip(),
                "active": "active" in (el.get_attribute("class") or ""),
            })
        return result

    def get_context_bar_values(self) -> dict:
        def _val(dom_id: str) -> str:
            els = self.driver.find_elements(By.ID, dom_id)
            return els[0].text if els else ""
        return {
            "endpoints": _val("ctx-val-endpoints"),
            "models": _val("ctx-val-models"),
            "prompts": _val("ctx-val-prompts"),
            "pipeline": _val("ctx-val-pipeline"),
            "runs": _val("ctx-val-runs"),
        }

    # ── Browser Console ──────────────────────────────────────────

    def get_browser_errors(self) -> list[str]:
        """Return SEVERE console log entries."""
        try:
            entries = self.driver.get_log("browser")
            return [e["message"] for e in entries if e.get("level") == "SEVERE"]
        except Exception:
            return []
