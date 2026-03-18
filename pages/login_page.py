"""
Login Page Object
=================
Contains all locators and actions for the Login page.

This follows the PAGE OBJECT MODEL (POM) pattern:
  - Locators are defined in one place
  - Actions (click, fill, etc.) are wrapped as methods
  - Tests call these methods instead of using raw selectors
"""

from playwright.sync_api import Page, expect
from config import settings
from locators.login_locators import LoginLocators


class LoginPage:
    """Page Object for the Login page."""

    def __init__(self, page: Page):
        self.page = page

    # ─── ACTIONS ──────────────────────────────────────────

    def navigate(self):
        """Go to the login page."""
        self.page.goto(settings.login_url())
        self.page.wait_for_load_state("networkidle")

    def fill_email(self, email: str):
        """Type email into the email field."""
        self.page.locator(LoginLocators.EMAIL_INPUT).first.fill(email)

    def fill_password(self, password: str):
        """Type password into the password field."""
        self.page.locator(LoginLocators.PASSWORD_INPUT).first.fill(password)

    def click_login(self):
        """Click the login / submit button."""
        self.page.locator(LoginLocators.LOGIN_BUTTON).first.click()

    def login(self, email: str, password: str):
        """Complete login flow: fill email, password, and click login."""
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()

    # ─── ASSERTIONS / GETTERS ─────────────────────────────

    def get_error_message(self) -> str:
        """Return the text of the error message (if visible)."""
        error = self.page.locator(LoginLocators.ERROR_MESSAGE).first
        error.wait_for(state="visible", timeout=10000)
        return error.inner_text()

    def is_error_visible(self) -> bool:
        """Check if any error message is visible on the page."""
        return self.page.locator(LoginLocators.ERROR_MESSAGE).first.is_visible()

    def click_signup_link(self):
        """Click the link to go to the signup page."""
        self.page.locator(LoginLocators.SIGNUP_LINK).first.click()
