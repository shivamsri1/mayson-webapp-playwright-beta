"""
Conftest - Pytest Configuration
================================
This file is automatically loaded by pytest.
It sets up:
  1. The --env command-line option (dev / prod)
  2. A shared Playwright browser instance
  3. A fresh page for each test
"""

import pytest
from playwright.sync_api import sync_playwright
from config import settings


# ─── COMMAND LINE OPTIONS ─────────────────────────────────

def pytest_addoption(parser):
    """Add custom command-line options to pytest."""
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=["dev", "prod"],
        help="Environment to run tests against: dev or prod",
    )


from datetime import datetime

def pytest_html_report_title(report):
    report.title = "Mayson Report"


def pytest_configure(config):
    """Update pytest-html report environment metadata."""
    env_name = config.getoption("--env")
    env_display = "Pro" if env_name == "prod" else "Dev"
    
    if hasattr(config, "stash"):
        from pytest_metadata.plugin import metadata_key
        # Clear the default metadata (Python version, Packages, etc) to match requested format
        config.stash[metadata_key].clear()
        
        # Add the specific fields asked for
        config.stash[metadata_key]["Date"] = datetime.now().strftime("%d-%B-%Y %H:%M:%S")
        config.stash[metadata_key]["Sanity"] = "Completed" # You can adjust this value!
        config.stash[metadata_key]["Environment"] = env_display


# ─── FIXTURES ─────────────────────────────────────────────

@pytest.fixture(scope="session", autouse=True)
def load_env(request):
    """Load the correct .env file based on --env flag."""
    env_name = request.config.getoption("--env")
    settings.load_environment(env_name)


@pytest.fixture(scope="session")
def browser():
    """Launch ONE browser for the entire test session (faster)."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=settings.is_headless(),
            slow_mo=settings.slow_mo(),
            args=["--start-maximized"],
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Create a NEW page (tab) for each test function (clean state)."""
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.set_default_timeout(settings.timeout())
    yield page
    context.close()
