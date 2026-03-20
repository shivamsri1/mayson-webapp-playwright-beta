"""
Signup Test Cases
=================
5 test cases covering POSITIVE and NEGATIVE signup scenarios.

Test Case Summary:
  ✅ TC-01: Successful signup with valid details              (POSITIVE)
  ❌ TC-02: Signup with an already registered email            (NEGATIVE)
  ❌ TC-03: Signup with mismatched passwords                   (NEGATIVE)
  ❌ TC-04: Signup with empty required fields                  (NEGATIVE)
  ❌ TC-05: Signup with a weak password                        (NEGATIVE)
"""

import pytest
import re
from playwright.sync_api import expect
from pages.signup_page import SignupPage
from data.testdata import (
    SIGNUP_VALID,
    SIGNUP_EXISTING_EMAIL,
    SIGNUP_MISMATCHED_PASSWORDS,
    SIGNUP_EMPTY,
    SIGNUP_WEAK_PASSWORD,
)


class TestSignup:
    """Test class for Signup functionality."""

    # ─── TC-01: POSITIVE - Valid Signup ───────────────────

    def test_signup_with_valid_details(self, page):
        """
        POSITIVE TEST
        Steps:
          1. Go to signup page
          2. Enter first name, last name, email, password, confirm password
          3. Click Signup
        Expected:
          - User is redirected (e.g. to login page or dashboard)
          - URL changes from /auth/signup
        """
        signup_page = SignupPage(page)
        signup_page.navigate()

        signup_page.signup(
            first_name=SIGNUP_VALID['first_name'],
            last_name=SIGNUP_VALID['last_name'],
            email=SIGNUP_VALID["email_id"],
            password=SIGNUP_VALID["password"],
            confirm_password=SIGNUP_VALID["password_repeat"],
        )

        # After signup, user should be redirected
        expect(page).not_to_have_url(re.compile(r".*/auth/signup.*"))

    # ─── TC-02: NEGATIVE - Already Registered Email ──────

    def test_signup_with_existing_email(self, page):
        """
        NEGATIVE TEST
        Steps:
          1. Go to signup page
          2. Enter an email that is ALREADY registered
          3. Fill other fields correctly
          4. Click Signup
        Expected:
          - An error message like "Email already exists" is shown
        """
        signup_page = SignupPage(page)
        signup_page.navigate()

        signup_page.signup(
            first_name=SIGNUP_EXISTING_EMAIL['first_name'],
            last_name=SIGNUP_EXISTING_EMAIL['last_name'],
            email=SIGNUP_EXISTING_EMAIL["email_id"],
            password=SIGNUP_EXISTING_EMAIL["password"],
            confirm_password=SIGNUP_EXISTING_EMAIL["password_repeat"],
        )

        signup_page.expect_error_visible()

    # ─── TC-03: NEGATIVE - Password Mismatch ─────────────

    def test_signup_with_mismatched_passwords(self, page):
        """
        NEGATIVE TEST
        Steps:
          1. Go to signup page
          2. Enter different password and confirm password
          3. Click Signup
        Expected:
          - An error about password mismatch is shown
          - User stays on signup page
        """
        signup_page = SignupPage(page)
        signup_page.navigate()

        signup_page.signup(
            first_name=SIGNUP_MISMATCHED_PASSWORDS['first_name'],
            last_name=SIGNUP_MISMATCHED_PASSWORDS['last_name'],
            email=SIGNUP_MISMATCHED_PASSWORDS["email_id"],
            password=SIGNUP_MISMATCHED_PASSWORDS["password"],
            confirm_password=SIGNUP_MISMATCHED_PASSWORDS["password_repeat"],
        )

        expect(page).to_have_url(re.compile(r".*/auth/signup.*"))

    # ─── TC-04: NEGATIVE - Empty Fields ──────────────────

    def test_signup_with_empty_fields(self, page):
        """
        NEGATIVE TEST
        Steps:
          1. Go to signup page
          2. Leave all fields empty
          3. Click Signup
        Expected:
          - Form validation prevents submission
          - Error message is shown OR user stays on page
        """
        signup_page = SignupPage(page)
        signup_page.navigate()

        signup_page.signup(
            first_name=SIGNUP_EMPTY['first_name'],
            last_name=SIGNUP_EMPTY['last_name'],
            email=SIGNUP_EMPTY["email_id"],
            password=SIGNUP_EMPTY["password"],
            confirm_password=SIGNUP_EMPTY["password_repeat"],
        )

        expect(page).to_have_url(re.compile(r".*/auth/signup.*"))

    # ─── TC-05: NEGATIVE - Weak Password ─────────────────

    def test_signup_with_weak_password(self, page):
        """
        NEGATIVE TEST
        Steps:
          1. Go to signup page
          2. Enter a very weak password (e.g. '123')
          3. Click Signup
        Expected:
          - An error about password strength is shown
          - User stays on signup page
        """
        signup_page = SignupPage(page)
        signup_page.navigate()

        signup_page.signup(
            first_name=SIGNUP_WEAK_PASSWORD['first_name'],
            last_name=SIGNUP_WEAK_PASSWORD['last_name'],
            email=SIGNUP_WEAK_PASSWORD["email_id"],
            password=SIGNUP_WEAK_PASSWORD["password"],
            confirm_password=SIGNUP_WEAK_PASSWORD["password_repeat"],
        )

        expect(page).to_have_url(re.compile(r".*/auth/signup.*"))
