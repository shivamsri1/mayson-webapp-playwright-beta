"""
Backwards-compatible test data module.

Tests/fixtures in this repo historically import constants from `data.testdata`.
We now generate those constants from `data/test_data.json` with env overrides
in `data.data_factory`, so dev/prod runs stay consistent.
"""

from .data_factory import (  # noqa: F401
    FORGOT_EMPTY,
    FORGOT_INVALID_FORMAT,
    FORGOT_MISMATCHED_PASSWORDS,
    FORGOT_UNREGISTERED,
    FORGOT_VALID,
    LOGIN_EMPTY,
    LOGIN_INVALID_EMAIL_FORMAT,
    LOGIN_UNREGISTERED_EMAIL,
    LOGIN_VALID,
    LOGIN_WRONG_PASSWORD,
    SIGNUP_EMPTY,
    SIGNUP_EXISTING_EMAIL,
    SIGNUP_MISMATCHED_PASSWORDS,
    SIGNUP_VALID,
    SIGNUP_WEAK_PASSWORD,
)

__all__ = [
    "LOGIN_VALID",
    "LOGIN_WRONG_PASSWORD",
    "LOGIN_UNREGISTERED_EMAIL",
    "LOGIN_EMPTY",
    "LOGIN_INVALID_EMAIL_FORMAT",
    "SIGNUP_VALID",
    "SIGNUP_EXISTING_EMAIL",
    "SIGNUP_MISMATCHED_PASSWORDS",
    "SIGNUP_EMPTY",
    "SIGNUP_WEAK_PASSWORD",
    "FORGOT_VALID",
    "FORGOT_UNREGISTERED",
    "FORGOT_EMPTY",
    "FORGOT_INVALID_FORMAT",
    "FORGOT_MISMATCHED_PASSWORDS",
]

