"""
Deprecated module.
Tests should import from `config.testdata` instead.
Keeping this file to avoid import breakage in external references.
"""

from .testdata import (  # noqa: F401
    LOGIN_VALID,
    LOGIN_WRONG_PASSWORD,
    LOGIN_UNREGISTERED_EMAIL,
    LOGIN_EMPTY,
    LOGIN_INVALID_EMAIL_FORMAT,
    SIGNUP_VALID,
    SIGNUP_EXISTING_EMAIL,
    SIGNUP_MISMATCHED_PASSWORDS,
    SIGNUP_EMPTY,
    SIGNUP_WEAK_PASSWORD,
    FORGOT_VALID,
    FORGOT_UNREGISTERED,
    FORGOT_EMPTY,
    FORGOT_INVALID_FORMAT,
    FORGOT_MISMATCHED_PASSWORDS,
)
