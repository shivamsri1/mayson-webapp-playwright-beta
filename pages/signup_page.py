"""
Signup Page Object
==================
Contains all locators and actions for the Signup / Register page.
"""

from playwright.sync_api import Page, expect
from core import config


class SignupPage:
    """Page Object for the Signup page."""

    # Locators
    FIRST_NAME_INPUT = 'input[name="first_name"]'
    LAST_NAME_INPUT = 'input[name="last_name"]'
    EMAIL_INPUT = 'input[name="email"]'
    PASSWORD_INPUT = 'input[name="password"]'
    CONFIRM_PASSWORD_INPUT = 'input[name="password_repeat"]'
    SIGNUP_BUTTON = 'button:has-text("Sign Up")'
    ERROR_MESSAGE = '.error-message, .alert-danger, [role="alert"], .text-danger'
    SUCCESS_MESSAGE = '.success-message, .alert-success, [role="status"]'
    LOGIN_LINK = 'a:has-text("Login"), a:has-text("Sign in"), a:has-text("Already have")'

    def __init__(self, page: Page):
        self.page = page

    # ─── ACTIONS ──────────────────────────────────────────

    def navigate(self):
        """Go to the signup page."""
        self.page.goto(config.signup_url())

    def fill_first_name(self, first_name: str):
        """Type first name into the first name field."""
        self.page.locator(self.FIRST_NAME_INPUT).first.fill(first_name)

    def fill_last_name(self, last_name: str):
        """Type last name into the last name field."""
        self.page.locator(self.LAST_NAME_INPUT).first.fill(last_name)

    def fill_email(self, email: str):
        """Type email into the email field."""
        self.page.locator(self.EMAIL_INPUT).first.fill(email)

    def fill_password(self, password: str):
        """Type password into the password field."""
        self.page.locator(self.PASSWORD_INPUT).first.fill(password)

    def fill_confirm_password(self, confirm_password: str):
        """Type confirm password into the confirm password field."""
        self.page.locator(self.CONFIRM_PASSWORD_INPUT).first.fill(confirm_password)

    def click_signup(self):
        """Click the signup / submit button."""
        self.page.locator(self.SIGNUP_BUTTON).first.click()

    def signup(self, first_name: str, last_name: str, email: str, password: str, confirm_password: str):
        """Complete signup flow: fill all fields and click submit."""
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_confirm_password(confirm_password)
        # Handle the form submission by pressing Enter, as the button click might not trigger correctly
        self.page.locator(self.CONFIRM_PASSWORD_INPUT).first.press("Enter")

    # ─── ASSERTIONS / GETTERS ─────────────────────────────

    def get_error_message(self) -> str:
        """Return the text of the error message (if visible)."""
        error = self.page.locator(self.ERROR_MESSAGE).first
        error.wait_for(state="visible", timeout=10000)
        return error.inner_text()

    def expect_error_visible(self):
        """Verify if any error message is visible on the page."""
        expect(self.page.locator(self.ERROR_MESSAGE).first).to_be_visible()

    def expect_success_visible(self):
        """Verify if a success message is visible on the page."""
        expect(self.page.locator(self.SUCCESS_MESSAGE).first).to_be_visible()
