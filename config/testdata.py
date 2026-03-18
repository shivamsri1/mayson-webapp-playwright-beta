"""
Test Data Loader (no secrets in code)
=====================================
Loads non-secret test data (names, template emails) from JSON and combines it
with sensitive values (passwords, real emails) from environment variables.

Rules:
- Do NOT commit secrets here. Put passwords/emails in .env.* files.
- Non-secret defaults live in config/testdata.json (or .example fallback).
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict

from . import settings


def _project_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load_json() -> Dict[str, Any]:
    """
    Load testdata JSON:
    - Prefer config/testdata.json if present (local overrides, not committed)
    - Fallback to config/testdata.json.example (committed defaults)
    """
    config_dir = os.path.join(_project_root(), "config")
    primary_path = os.path.join(config_dir, "testdata.json")
    fallback_path = os.path.join(config_dir, "testdata.json.example")

    source_path = primary_path if os.path.exists(primary_path) else fallback_path
    with open(source_path, "r", encoding="utf-8") as f:
        return json.load(f)


_DATA = _load_json()

# Helper getters for env secrets (with sane defaults for CI/local)
_VALID_EMAIL = settings.get("VALID_EMAIL", _DATA["login"]["valid_email"])
_VALID_PASSWORD = settings.get("VALID_PASSWORD", "ChangeMe@123")
_WRONG_PASSWORD = settings.get("WRONG_PASSWORD", "DefinitelyWrong@999")

_NEW_PASSWORD = settings.get("NEW_PASSWORD", "NewPassword@123")
_NEW_PASSWORD_MISMATCH = settings.get("NEW_PASSWORD_MISMATCH", "DifferentPassword@123")

# ─── LOGIN TEST DATA ───────────────────────────────────────────────
LOGIN_VALID = {
    "email_id": _VALID_EMAIL,
    "password": _VALID_PASSWORD,
}

LOGIN_WRONG_PASSWORD = {
    "email_id": _VALID_EMAIL,
    "password": _WRONG_PASSWORD,
}

LOGIN_UNREGISTERED_EMAIL = {
    "email_id": _DATA["login"]["unregistered_email"],
    "password": _VALID_PASSWORD,
}

LOGIN_EMPTY = {
    "email_id": "",
    "password": "",
}

LOGIN_INVALID_EMAIL_FORMAT = {
    "email_id": _DATA["login"]["invalid_email_format"],
    "password": _VALID_PASSWORD,
}

# ─── SIGNUP TEST DATA ─────────────────────────────────────────────
SIGNUP_VALID = {
    "first_name": _DATA["signup"]["first_name"],
    "last_name": _DATA["signup"]["last_name"],
    "email_id": _DATA["signup"]["valid_email"],
    "password": _VALID_PASSWORD,
    "password_repeat": _VALID_PASSWORD,
}

SIGNUP_EXISTING_EMAIL = {
    "first_name": _DATA["signup"]["first_name"],
    "last_name": _DATA["signup"]["last_name"],
    "email_id": _VALID_EMAIL,  # already registered
    "password": _VALID_PASSWORD,
    "password_repeat": _VALID_PASSWORD,
}

SIGNUP_MISMATCHED_PASSWORDS = {
    "first_name": _DATA["signup"]["first_name"],
    "last_name": _DATA["signup"]["last_name"],
    "email_id": _DATA["signup"]["mismatch_email"],
    "password": _VALID_PASSWORD,
    "password_repeat": _NEW_PASSWORD_MISMATCH,
}

SIGNUP_EMPTY = {
    "first_name": "",
    "last_name": "",
    "email_id": "",
    "password": "",
    "password_repeat": "",
}

SIGNUP_WEAK_PASSWORD = {
    "first_name": _DATA["signup"]["first_name"],
    "last_name": _DATA["signup"]["last_name"],
    "email_id": _DATA["signup"]["weak_email"],
    "password": _DATA["signup"]["weak_password"],  # intentionally weak for validation test
    "password_repeat": _DATA["signup"]["weak_password"],
}

# ─── FORGOT PASSWORD TEST DATA ────────────────────────────────────
FORGOT_VALID = {
    "email_id": _VALID_EMAIL,
    "password": _NEW_PASSWORD,
    "password_repeat": _NEW_PASSWORD,
}

FORGOT_UNREGISTERED = {
    "email_id": _DATA["forgot"]["unregistered_email"],
    "password": _NEW_PASSWORD,
    "password_repeat": _NEW_PASSWORD,
}

FORGOT_EMPTY = {
    "email_id": "",
    "password": "",
    "password_repeat": "",
}

FORGOT_INVALID_FORMAT = {
    "email_id": _DATA["forgot"]["invalid_email_format"],
    "password": _NEW_PASSWORD,
    "password_repeat": _NEW_PASSWORD,
}

FORGOT_MISMATCHED_PASSWORDS = {
    "email_id": _VALID_EMAIL,
    "password": _NEW_PASSWORD,
    "password_repeat": _NEW_PASSWORD_MISMATCH,
}

