from __future__ import annotations

from typing import Optional, Pattern, Union

from playwright.sync_api import Locator, Page, expect

from core import config
from core.logger import get_logger


UrlPattern = Union[str, Pattern[str]]


class BasePage:
    """Common Playwright helpers shared by all Page Objects."""

    def __init__(self, page: Page, name: Optional[str] = None) -> None:
        self.page = page
        self.log = get_logger(name or self.__class__.__name__)

    # ─── Navigation ─────────────────────────────────────────

    def goto(self, url: str, wait_until: str = "networkidle") -> None:
        self.log.info("Navigating to %s", url)
        self.page.goto(url, wait_until=wait_until)

    def open_path(self, path: str, wait_until: str = "networkidle") -> None:
        base = config.base_url()
        full_url = base.rstrip("/") + "/" + path.lstrip("/")
        self.goto(full_url, wait_until=wait_until)

    # ─── Element helpers ────────────────────────────────────

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click_first(self, selector: str) -> None:
        self.log.debug("Clicking first element for selector=%s", selector)
        self.locator(selector).first.click()

    def fill_first(self, selector: str, value: str) -> None:
        self.log.debug("Filling selector=%s with value=%s", selector, value)
        self.locator(selector).first.fill(value)

    # ─── URL helpers ────────────────────────────────────────

    def expect_url_matches(self, pattern: UrlPattern) -> None:
        self.log.info("Expecting URL to match %s", pattern)
        expect(self.page).to_have_url(pattern)

    def expect_url_not_matches(self, pattern: UrlPattern) -> None:
        self.log.info("Expecting URL NOT to match %s", pattern)
        expect(self.page).not_to_have_url(pattern)

