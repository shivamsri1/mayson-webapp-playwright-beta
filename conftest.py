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
from core import config as settings


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
def browser_type_launch_args(browser_type_launch_args):
    """Configure native playwright browser launch options."""
    return {
        **browser_type_launch_args,
        "headless": settings.is_headless(),
        "slow_mo": settings.slow_mo(),
        "args": ["--start-maximized"],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure native playwright context options (tracing, videos)."""
    return {
        **browser_context_args,
        "no_viewport": True,
    }


@pytest.fixture(autouse=True)
def _configure_timeouts(page):
    """Set custom timeouts on the native page fixture."""
    page.set_default_timeout(settings.timeout())
    from playwright.sync_api import expect
    expect.set_options(timeout=settings.timeout())

