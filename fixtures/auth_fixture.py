"""
Authentication-related pytest fixtures.

These fixtures encapsulate login flows so tests that require an authenticated
user can start from a known "logged-in" state instead of repeating steps.
"""

from __future__ import annotations

from typing import Generator

import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from data.testdata import LOGIN_VALID


@pytest.fixture
def logged_in_page(page: Page) -> Generator[Page, None, None]:
    """
    Log in once using valid credentials and return an authenticated page.

    Adjust the assertions or post-login checks here as the application grows.
    """
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(
        email=LOGIN_VALID["email_id"],
        password=LOGIN_VALID["password"],
    )
    # Rely on application redirects; tests can assert final URL as needed.
    yield page

