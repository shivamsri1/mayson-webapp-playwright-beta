"""
Signup Page Object
==================
Contains all locators and actions for the Signup / Register page.
"""

from playwright.sync_api import Page, expect
from config import settings
from locators.signup_locators import SignupLocators


class SignupPage:
    """Page Object for the Signup page."""

    def __init__(self, page: Page):
        self.page = page

    # ─── ACTIONS ──────────────────────────────────────────

    def navigate(self):
        """Go to the signup page."""
        self.page.goto(settings.signup_url())
        self.page.wait_for_load_state("networkidle")

    def fill_first_name(self, first_name: str):
        """Type first name into the first name field."""
        self.page.locator(SignupLocators.FIRST_NAME_INPUT).first.fill(first_name)

    def fill_last_name(self, last_name: str):
        """Type last name into the last name field."""
        self.page.locator(SignupLocators.LAST_NAME_INPUT).first.fill(last_name)

    def fill_email(self, email: str):
        """Type email into the email field."""
        self.page.locator(SignupLocators.EMAIL_INPUT).first.fill(email)

    def fill_password(self, password: str):
        """Type password into the password field."""
        self.page.locator(SignupLocators.PASSWORD_INPUT).first.fill(password)

    def fill_confirm_password(self, confirm_password: str):
        """Type confirm password into the confirm password field."""
        self.page.locator(SignupLocators.CONFIRM_PASSWORD_INPUT).first.fill(confirm_password)

    def click_signup(self):
        """Click the signup / submit button."""
        self.page.locator(SignupLocators.SIGNUP_BUTTON).first.click()

    def signup(self, first_name: str, last_name: str, email: str, password: str, confirm_password: str):
        """Complete signup flow: fill all fields and click submit."""
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_confirm_password(confirm_password)
        # Handle the form submission by pressing Enter, as the button click might not trigger correctly
        self.page.locator(SignupLocators.CONFIRM_PASSWORD_INPUT).first.press("Enter")

    # ─── ASSERTIONS / GETTERS ─────────────────────────────

    def get_error_message(self) -> str:
        """Return the text of the error message (if visible)."""
        error = self.page.locator(SignupLocators.ERROR_MESSAGE).first
        error.wait_for(state="visible", timeout=10000)
        return error.inner_text()

    def is_error_visible(self) -> bool:
        """Check if any error message is visible on the page."""
        return self.page.locator(SignupLocators.ERROR_MESSAGE).first.is_visible()

    def is_success_visible(self) -> bool:
        """Check if a success message is visible on the page."""
        return self.page.locator(SignupLocators.SUCCESS_MESSAGE).first.is_visible()
