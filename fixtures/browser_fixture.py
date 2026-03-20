"""
Custom browser/page fixtures.

These build on top of pytest-playwright's built-in fixtures but allow you to
centralize any additional configuration or common setup that shouldn't live
directly in tests.
"""

from __future__ import annotations

from typing import Generator

import pytest
from playwright.sync_api import Page


@pytest.fixture
def browser_page(page: Page) -> Generator[Page, None, None]:
    """
    Thin wrapper around the native `page` fixture.

    Use this in tests instead of `page` if you ever need to add extra
    per-test setup/teardown logic (cookies, storage state, etc.).
    """
    yield page

