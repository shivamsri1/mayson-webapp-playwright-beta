from playwright.sync_api import Page, expect
from core import config

class ForgotPasswordPage:
    """Page Object for the Forgot Password page."""

    # Locators
    EMAIL_INPUT = 'input[name="email"]'
    NEW_PASSWORD_INPUT = 'input[name="password"]'
    CONFIRM_PASSWORD_INPUT = 'input[name="password_repeat"]'
    CONTINUE_BUTTON = 'button:has-text("Continue")'
    BACK_TO_LOGIN_LINK = 'a:has-text("Login"), a:has-text("Sign In"), a:has-text("Back to login"), a[href*="/auth/login"]'
    ERROR_MESSAGE = '.error-message, .alert-danger, [role="alert"], .text-danger, .Toastify__toast--error'
    SUCCESS_MESSAGE = '.success-message, .alert-success, [role="status"], .toast, .Toastify__toast--success'

    def __init__(self, page: Page):
        self.page = page

    # ─── ACTIONS ──────────────────────────────────────────

    def navigate(self):
        self.page.goto(config.forgot_password_url())

    def fill_form(self, email: str, new_password: str, confirm_password: str):
        if email:
            self.page.locator(self.EMAIL_INPUT).first.fill(email)
        if new_password:
            self.page.locator(self.NEW_PASSWORD_INPUT).first.fill(new_password)
        if confirm_password:
            self.page.locator(self.CONFIRM_PASSWORD_INPUT).first.fill(confirm_password)

    def click_continue(self):
        self.page.locator(self.CONTINUE_BUTTON).first.click()

    def submit_forgot_password(self, email: str, new_password: str, confirm_password: str):
        self.fill_form(email, new_password, confirm_password)
        self.click_continue()

    def click_login_link(self):
        self.page.locator(self.BACK_TO_LOGIN_LINK).first.click()

    # ─── ASSERTIONS / GETTERS ─────────────────────────────

    def expect_error_msg_visible(self):
        expect(self.page.locator(self.ERROR_MESSAGE).first).to_be_visible()

    def expect_success_msg_visible(self):
        expect(self.page.locator(self.SUCCESS_MESSAGE).first).to_be_visible()
