from playwright.sync_api import Page, expect
from config import settings
from locators.forgot_password_locators import ForgotPasswordLocators

class ForgotPasswordPage:
    """Page Object for the Forgot Password page."""

    def __init__(self, page: Page):
        self.page = page

    # ─── ACTIONS ──────────────────────────────────────────

    def navigate(self):
        self.page.goto(settings.forgot_password_url())
        self.page.wait_for_load_state("networkidle")

    def fill_form(self, email: str, new_password: str, confirm_password: str):
        if email:
            self.page.locator(ForgotPasswordLocators.EMAIL_INPUT).first.fill(email)
        if new_password:
            self.page.locator(ForgotPasswordLocators.NEW_PASSWORD_INPUT).first.fill(new_password)
        if confirm_password:
            self.page.locator(ForgotPasswordLocators.CONFIRM_PASSWORD_INPUT).first.fill(confirm_password)

    def click_continue(self):
        self.page.locator(ForgotPasswordLocators.CONTINUE_BUTTON).first.click()

    def submit_forgot_password(self, email: str, new_password: str, confirm_password: str):
        self.fill_form(email, new_password, confirm_password)
        self.click_continue()

    def click_login_link(self):
        self.page.locator(ForgotPasswordLocators.BACK_TO_LOGIN_LINK).first.click()

    # ─── ASSERTIONS / GETTERS ─────────────────────────────

    def is_error_msg_visible(self) -> bool:
        try:
            return self.page.locator(ForgotPasswordLocators.ERROR_MESSAGE).first.is_visible(timeout=3000)
        except:
            return False

    def is_success_msg_visible(self) -> bool:
        try:
            return self.page.locator(ForgotPasswordLocators.SUCCESS_MESSAGE).first.is_visible(timeout=3000)
        except:
            return False
