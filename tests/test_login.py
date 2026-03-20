import re
from playwright.sync_api import expect

from data.testdata import (
    LOGIN_EMPTY,
    LOGIN_INVALID_EMAIL_FORMAT,
    LOGIN_UNREGISTERED_EMAIL,
    LOGIN_VALID,
    LOGIN_WRONG_PASSWORD,
)
from pages.login_page import LoginPage


class TestLogin:

    def test_login_with_valid_credentials(self, page):
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_VALID["email_id"],
            password=LOGIN_VALID["password"],
        )
        login_page.expect_redirected_from_login()

    # ─── TC-02: NEGATIVE - Wrong Password ────────────────

    def test_login_with_wrong_password(self, page):
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_WRONG_PASSWORD["email_id"],
            password=LOGIN_WRONG_PASSWORD["password"],
        )

        login_page.expect_error_visible()
        login_page.expect_on_login_page()

    # ─── TC-03: NEGATIVE - Unregistered Email ─────────────

    def test_login_with_unregistered_email(self, page):
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_UNREGISTERED_EMAIL["email_id"],
            password=LOGIN_UNREGISTERED_EMAIL["password"],
        )

        login_page.expect_error_visible()
        login_page.expect_on_login_page()

    # ─── TC-04: NEGATIVE - Empty Fields ──────────────────

    def test_login_with_empty_fields(self, page):
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_EMPTY["email_id"],
            password=LOGIN_EMPTY["password"],
        )

        login_page.expect_on_login_page()

    # ─── TC-05: NEGATIVE - Invalid Email Format ──────────

    def test_login_with_invalid_email_format(self, page):
        login_page = LoginPage(page)
        login_page.navigate()

        login_page.login(
            email=LOGIN_INVALID_EMAIL_FORMAT["email_id"],
            password=LOGIN_INVALID_EMAIL_FORMAT["password"],
        )

        login_page.expect_on_login_page()
