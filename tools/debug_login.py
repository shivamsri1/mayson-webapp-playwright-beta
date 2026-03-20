from __future__ import annotations

import argparse
import re

import os
from playwright.sync_api import sync_playwright, expect

from core import config as settings
from pages.login_page import LoginPage


def run(env_name: str) -> None:
    settings.load_environment(env_name)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=settings.is_headless(),
            args=["--start-maximized"],
        )
        page = browser.new_page()
        page.set_default_timeout(settings.timeout())
        expect.set_options(timeout=settings.timeout())

        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(email=settings.valid_email(), password=settings.valid_password())

        # Successful login should navigate away from /auth/login
        expect(page).not_to_have_url(re.compile(r".*/auth/login.*"))
        print(f"Login OK for env={env_name}. Current URL: {page.url}")

        browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a single login flow for debugging.")
    parser.add_argument("--env", default="dev", choices=["dev", "prod"], help="Environment to use")
    parser.add_argument("--headed", action="store_true", default=False, help="Run visible browser (non-headless).")
    args = parser.parse_args()

    if args.headed:
        os.environ["HEADLESS"] = "false"
    run(args.env)
