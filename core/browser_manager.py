"""
Optional browser manager helpers.

Most tests should rely on `pytest-playwright`'s native fixtures. This module
is intended for CLI tools or scripts that need a quick way to spin up a
Playwright browser using the same configuration as the tests.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from core import config


@contextmanager
def launch_playwright() -> Generator[Playwright, None, None]:
    with sync_playwright() as p:
        yield p


@contextmanager
def launch_browser(headless: bool | None = None) -> Generator[Browser, None, None]:
    with launch_playwright() as p:
        browser = p.chromium.launch(
            headless=config.is_headless() if headless is None else headless,
            slow_mo=config.slow_mo(),
            args=["--start-maximized"],
        )
        try:
            yield browser
        finally:
            browser.close()


@contextmanager
def browser_page() -> Generator[Page, None, None]:
    with launch_browser() as browser:
        context: BrowserContext = browser.new_context(no_viewport=True)
        page = context.new_page()
        try:
            yield page
        finally:
            context.close()

