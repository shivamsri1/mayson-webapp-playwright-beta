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
from core import config


class LoginPage:
    """Page Object for the Login page."""

    # Locators
    EMAIL_INPUT = 'input[name="email"], input[type="email"], #email'
    PASSWORD_INPUT = 'input[name="password"], input[type="password"], #password'
    LOGIN_BUTTON = 'button[type="submit"], button:has-text("Login"), button:has-text("Sign in")'
    ERROR_MESSAGE = '.error-message, .alert-danger, [role="alert"], .text-danger'
    SIGNUP_LINK = 'a:has-text("Sign up"), a:has-text("Register"), a:has-text("Create account")'

    def __init__(self, page: Page):
        self.page = page

    # ─── ACTIONS ──────────────────────────────────────────

    def navigate(self):
        """Go to the login page."""
        self.page.goto(config.login_url())

    def fill_email(self, email: str):
        """Type email into the email field."""
        self.page.locator(self.EMAIL_INPUT).first.fill(email)

    def fill_password(self, password: str):
        """Type password into the password field."""
        self.page.locator(self.PASSWORD_INPUT).first.fill(password)

    def click_login(self):
        """Click the login / submit button."""
        self.page.locator(self.LOGIN_BUTTON).first.click()

    def login(self, email: str, password: str):
        """Complete login flow: fill email, password, and click login."""
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()

    # ─── ASSERTIONS / GETTERS ─────────────────────────────

    def get_error_message(self) -> str:
        """Return the text of the error message (if visible)."""
        error = self.page.locator(self.ERROR_MESSAGE).first
        error.wait_for(state="visible", timeout=10000)
        return error.inner_text()

    def expect_error_visible(self):
        """Verify that an error message is visible using Playwright expect."""
        expect(self.page.locator(self.ERROR_MESSAGE).first).to_be_visible()

    def click_signup_link(self):
        """Click the link to go to the signup page."""
        self.page.locator(self.SIGNUP_LINK).first.click()
