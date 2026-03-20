"""
Dynamic test data factory.

This module is intentionally env-aware:
- pytest loads `.env.dev` / `.env.prod` via `--env`
- we then build the test-data dictionaries from `data/test_data.json`
- env values override the JSON defaults so dev/prod remains plug-and-play
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Dict

from core import config as settings


def _load_base_test_data() -> Dict[str, Any]:
    path = Path(__file__).resolve().parent / "test_data.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _override_from_env(base: Dict[str, Any]) -> Dict[str, Any]:
    # Login overrides
    base["LOGIN_VALID"]["email_id"] = settings.valid_email()
    base["LOGIN_VALID"]["password"] = settings.valid_password()

    base["LOGIN_WRONG_PASSWORD"]["email_id"] = settings.valid_email()
    base["LOGIN_WRONG_PASSWORD"]["password"] = settings.get("WRONG_PASSWORD", base["LOGIN_WRONG_PASSWORD"]["password"])

    base["LOGIN_UNREGISTERED_EMAIL"]["email_id"] = settings.get(
        "UNREGISTERED_EMAIL",
        base["LOGIN_UNREGISTERED_EMAIL"]["email_id"],
    )
    base["LOGIN_UNREGISTERED_EMAIL"]["password"] = settings.valid_password()

    # Signup overrides
    base["SIGNUP_EXISTING_EMAIL"]["email_id"] = settings.valid_email()
    base["SIGNUP_EXISTING_EMAIL"]["password"] = settings.valid_password()
    base["SIGNUP_EXISTING_EMAIL"]["password_repeat"] = settings.valid_password()

    base["SIGNUP_VALID"]["password"] = settings.valid_password()
    base["SIGNUP_VALID"]["password_repeat"] = settings.valid_password()

    base["SIGNUP_WEAK_PASSWORD"]["password"] = settings.get("WEAK_PASSWORD", base["SIGNUP_WEAK_PASSWORD"]["password"])
    base["SIGNUP_WEAK_PASSWORD"]["password_repeat"] = base["SIGNUP_WEAK_PASSWORD"]["password"]

    # Forgot password overrides
    new_password = settings.get("NEW_PASSWORD", base["FORGOT_VALID"]["password_repeat"])
    new_password_mismatch = settings.get(
        "NEW_PASSWORD_MISMATCH",
        base["FORGOT_MISMATCHED_PASSWORDS"]["password_repeat"],
    )

    base["FORGOT_VALID"]["email_id"] = settings.valid_email()
    base["FORGOT_VALID"]["password"] = settings.valid_password()
    base["FORGOT_VALID"]["password_repeat"] = new_password

    base["FORGOT_UNREGISTERED"]["email_id"] = settings.get(
        "UNREGISTERED_EMAIL",
        base["FORGOT_UNREGISTERED"]["email_id"],
    )
    base["FORGOT_UNREGISTERED"]["password"] = settings.valid_password()
    base["FORGOT_UNREGISTERED"]["password_repeat"] = new_password

    base["FORGOT_INVALID_FORMAT"]["password"] = settings.valid_password()
    base["FORGOT_INVALID_FORMAT"]["password_repeat"] = new_password

    base["FORGOT_MISMATCHED_PASSWORDS"]["email_id"] = settings.valid_email()
    base["FORGOT_MISMATCHED_PASSWORDS"]["password"] = new_password
    base["FORGOT_MISMATCHED_PASSWORDS"]["password_repeat"] = new_password_mismatch

    return base


def _build_test_data() -> Dict[str, Any]:
    base = _load_base_test_data()
    return _override_from_env(copy.deepcopy(base))


_TEST_DATA = _build_test_data()

LOGIN_VALID = _TEST_DATA["LOGIN_VALID"]
LOGIN_WRONG_PASSWORD = _TEST_DATA["LOGIN_WRONG_PASSWORD"]
LOGIN_UNREGISTERED_EMAIL = _TEST_DATA["LOGIN_UNREGISTERED_EMAIL"]
LOGIN_EMPTY = _TEST_DATA["LOGIN_EMPTY"]
LOGIN_INVALID_EMAIL_FORMAT = _TEST_DATA["LOGIN_INVALID_EMAIL_FORMAT"]

SIGNUP_VALID = _TEST_DATA["SIGNUP_VALID"]
SIGNUP_EXISTING_EMAIL = _TEST_DATA["SIGNUP_EXISTING_EMAIL"]
SIGNUP_MISMATCHED_PASSWORDS = _TEST_DATA["SIGNUP_MISMATCHED_PASSWORDS"]
SIGNUP_EMPTY = _TEST_DATA["SIGNUP_EMPTY"]
SIGNUP_WEAK_PASSWORD = _TEST_DATA["SIGNUP_WEAK_PASSWORD"]

FORGOT_VALID = _TEST_DATA["FORGOT_VALID"]
FORGOT_UNREGISTERED = _TEST_DATA["FORGOT_UNREGISTERED"]
FORGOT_EMPTY = _TEST_DATA["FORGOT_EMPTY"]
FORGOT_INVALID_FORMAT = _TEST_DATA["FORGOT_INVALID_FORMAT"]
FORGOT_MISMATCHED_PASSWORDS = _TEST_DATA["FORGOT_MISMATCHED_PASSWORDS"]
