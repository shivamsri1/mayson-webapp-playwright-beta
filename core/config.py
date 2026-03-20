"""
Settings Module
===============
Loads environment-specific configuration from .env files.

Usage:
    pytest --env dev     → loads .env.dev
    pytest --env prod    → loads .env.prod
"""

import os
from dotenv import load_dotenv


def load_environment(env_name: str = "dev"):
    """Load the .env file for the given environment (dev or prod)."""
    # Find the project root (config and core are sibling directories)
    core_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(core_dir)
    env_file = os.path.join(project_root, "config", f".env.{env_name}")

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Environment file not found: {env_file}")

    # Load the .env file into os.environ
    load_dotenv(env_file, override=True)
    # Mark env as loaded so other modules/fixtures can avoid reloading.
    os.environ["_MAYSON_ENV_LOADED"] = env_name
    # Keep output ASCII-only for Windows consoles.
    print(f"\nLoaded environment: {env_name} ({env_file})")


def get(key: str, default: str = "") -> str:
    """Get a value from the loaded environment variables."""
    return os.getenv(key, default)


# --- Shortcut functions for common settings ---

def base_url() -> str:
    return get("BASE_URL")

def login_url() -> str:
    # Allow overriding per-env via LOGIN_URL, but fall back to a convention.
    url = get("LOGIN_URL")
    if url:
        return url
    return base_url().rstrip("/") + "/auth/login"

def signup_url() -> str:
    url = get("SIGNUP_URL")
    if url:
        return url
    return base_url().rstrip("/") + "/auth/signup"

def forgot_password_url() -> str:
    url = get("FORGOT_PASSWORD_URL")
    if url:
        return url
    return base_url().rstrip("/") + "/auth/forget-password"

def valid_email() -> str:
    return get("VALID_EMAIL")

def valid_password() -> str:
    return get("VALID_PASSWORD")

def is_headless() -> bool:
    return get("HEADLESS", "true").lower() == "true"

def slow_mo() -> int:
    return int(get("SLOW_MO", "0"))

def timeout() -> int:
    return int(get("TIMEOUT", "30000"))
