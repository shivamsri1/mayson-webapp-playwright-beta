import pytest
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from data.testdata import (
    LOGIN_VALID,
    LOGIN_WRONG_PASSWORD,
    LOGIN_UNREGISTERED_EMAIL,
    LOGIN_EMPTY,
    LOGIN_INVALID_EMAIL_FORMAT,
)


class TestLogin:

    def test_login_with_valid_credentials(self, page):
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_VALID["email_id"],
            password=LOGIN_VALID["password"],
        )
        expect(page).not_to_have_url(re.compile(r".*/auth/login.*"))

    # ─── TC-02: NEGATIVE - Wrong Password ────────────────

    def test_login_with_wrong_password(self, page):
        """
        NEGATIVE TEST
        Steps:
          1. Go to login page
          2. Enter valid email but WRONG password
          3. Click Login
        Expected:
          - An error message is displayed
          - User stays on the login page
        """
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_WRONG_PASSWORD["email_id"],
            password=LOGIN_WRONG_PASSWORD["password"],
        )

        # Should show an error message
        login_page.expect_error_visible()

    # ─── TC-03: NEGATIVE - Unregistered Email ─────────────

    def test_login_with_unregistered_email(self, page):
        """
        NEGATIVE TEST
        Steps:
          1. Go to login page
          2. Enter email that is NOT registered
          3. Enter any password
          4. Click Login
        Expected:
          - An error message is displayed
          - User stays on the login page
        """
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_UNREGISTERED_EMAIL["email_id"],
            password=LOGIN_UNREGISTERED_EMAIL["password"],
        )

        # Should show an error message
        login_page.expect_error_visible()

    # ─── TC-04: NEGATIVE - Empty Fields ──────────────────

    def test_login_with_empty_fields(self, page):
        """
        NEGATIVE TEST
        Steps:
          1. Go to login page
          2. Leave email and password EMPTY
          3. Click Login
        Expected:
          - Form validation prevents submission
          - An error message is shown OR form stays on login page
        """
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_EMPTY["email_id"],
            password=LOGIN_EMPTY["password"],
        )

        # After clicking login with empty fields:
        # The URL should still be the login page
        expect(page).to_have_url(re.compile(r".*/auth/login.*"))

    # ─── TC-05: NEGATIVE - Invalid Email Format ──────────

    def test_login_with_invalid_email_format(self, page):
        """
        NEGATIVE TEST
        Steps:
          1. Go to login page
          2. Enter an invalid email format (e.g. 'not-an-email')
          3. Enter a password
          4. Click Login
        Expected:
          - Form validation catches the bad email
          - An error message is shown OR form stays on login page
        """
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_INVALID_EMAIL_FORMAT["email_id"],
            password=LOGIN_INVALID_EMAIL_FORMAT["password"],
        )

        # Should either show an error or remain on login page
        expect(page).to_have_url(re.compile(r".*/auth/login.*"))
