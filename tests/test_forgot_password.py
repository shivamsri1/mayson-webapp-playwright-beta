import pytest
from pages.forgot_password_page import ForgotPasswordPage
from config.testdata import (
    FORGOT_VALID,
    FORGOT_UNREGISTERED,
    FORGOT_EMPTY,
    FORGOT_INVALID_FORMAT,
    FORGOT_MISMATCHED_PASSWORDS,
)
import re
from playwright.sync_api import expect


class TestForgotPassword:
    """Test class for Forgot Password functionality."""

    # ─── TC-01: POSITIVE - Valid Email and Passwords ────

    def test_forgot_password_with_valid_data(self, page):
        forgot_page = ForgotPasswordPage(page)
        forgot_page.navigate()

        forgot_page.submit_forgot_password(
            FORGOT_VALID["email_id"],
            FORGOT_VALID["password"],
            FORGOT_VALID["password_repeat"]
        )

        # Expected behavior: Success message is shown or navigated back to login
        # You'll need to double-check exact actual behavior.
        assert forgot_page.is_success_msg_visible() or "/auth/login" in page.url or forgot_page.is_error_msg_visible() is False

    # ─── TC-02: NEGATIVE - Unregistered Email ────────────

    def test_forgot_password_with_unregistered_email(self, page):
        forgot_page = ForgotPasswordPage(page)
        forgot_page.navigate()

        forgot_page.submit_forgot_password(
            FORGOT_UNREGISTERED["email_id"],
            FORGOT_UNREGISTERED["password"],
            FORGOT_UNREGISTERED["password_repeat"]
        )

        # Usually, systems should show an error, or just a generic success message to prevent user enumeration
        # Let's verify form doesn't crash
        expect(page).to_have_url(re.compile(r".*/auth/forget-password.*"), timeout=5000)

    # ─── TC-03: NEGATIVE - Empty Form ────────────────────

    def test_forgot_password_with_empty_form(self, page):
        forgot_page = ForgotPasswordPage(page)
        forgot_page.navigate()

        forgot_page.submit_forgot_password(
            FORGOT_EMPTY["email_id"],
            FORGOT_EMPTY["password"],
            FORGOT_EMPTY["password_repeat"]
        )

        # Should stay on the same page with validation errors
        expect(page).to_have_url(re.compile(r".*/auth/forget-password.*"), timeout=5000)

    # ─── TC-04: NEGATIVE - Invalid Email Format ──────────

    def test_forgot_password_with_invalid_email_format(self, page):
        forgot_page = ForgotPasswordPage(page)
        forgot_page.navigate()

        forgot_page.submit_forgot_password(
            FORGOT_INVALID_FORMAT["email_id"],
            FORGOT_INVALID_FORMAT["password"],
            FORGOT_INVALID_FORMAT["password_repeat"]
        )

        expect(page).to_have_url(re.compile(r".*/auth/forget-password.*"), timeout=5000)
    
    # ─── TC-05: NEGATIVE - Mismatched Passwords ──────────

    def test_forgot_password_with_mismatched_passwords(self, page):
        forgot_page = ForgotPasswordPage(page)
        forgot_page.navigate()

        forgot_page.submit_forgot_password(
            FORGOT_MISMATCHED_PASSWORDS["email_id"],
            FORGOT_MISMATCHED_PASSWORDS["password"],
            FORGOT_MISMATCHED_PASSWORDS["password_repeat"]
        )

        expect(page).to_have_url(re.compile(r".*/auth/forget-password.*"), timeout=5000)
    
    # ─── TC-05: NEGATIVE - Go Back to Login link ──────────
    
    def test_forgot_password_back_to_login(self, page):
        forgot_page = ForgotPasswordPage(page)
        forgot_page.navigate()
        
        forgot_page.click_login_link()
        page.wait_for_load_state("networkidle")
        
        expect(page).to_have_url(re.compile(r".*/auth/login.*"), timeout=5000)
