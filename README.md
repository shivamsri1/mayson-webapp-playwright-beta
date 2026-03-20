# 🧪 Mayson Playwright Framework

A **Python + Playwright + pytest** automation framework for the Mayson webapp, structured for long‑term maintainability and CI usage.

---

## 📁 Project Structure

```text
mayson-webapp-playwright-beta/
│
├── .github/
│   └── workflows/
│       └── playwright.yml        # CI pipeline to run tests & upload report
│
├── core/                         # Framework core (engine)
│   ├── base_page.py              # Common Playwright helpers & URL utilities
│   ├── browser_manager.py        # Browser helpers for CLI tools/scripts
│   ├── config.py                 # Env + settings loader (uses config/.env.*)
│   └── logger.py                 # Central logging configuration
│
├── pages/                        # Page Objects (POM with real locators)
│   ├── login_page.py
│   ├── signup_page.py
│   └── forgot_password_page.py
│
├── tests/                        # UI test cases
│   ├── test_login.py
│   ├── test_signup.py
│   └── test_forgot_password.py
│
├── data/                         # Test data layer
│   ├── test_data.json            # JSON placeholder for future data
│   ├── testdata.py               # Current source of named scenarios
│   ├── data_factory.py           # (stub) dynamic data generation
│   └── schemas.py                # (stub) validation schemas
│
├── fixtures/                     # Reusable pytest fixtures
│   ├── browser_fixture.py        # Wrapper around Playwright `page`
│   └── auth_fixture.py           # `logged_in_page` fixture
│
├── utils/                        # Reusable helpers (extension points)
│   ├── api_client.py             # (stub) API testing support
│   ├── wait_utils.py             # (stub) custom waiting strategies
│   ├── assertions.py             # (stub) higher-level assertions
│   └── file_utils.py             # (stub) file & JSON helpers
│
├── ai/                           # Future-ready AI QA layer (stubs)
│   ├── test_generator.py
│   ├── log_analyzer.py
│   └── flaky_test_detector.py
│
├── tools/                        # Debug & scraping scripts
│   ├── inspect_page.py
│   ├── inspect_signup.py
│   └── debug_login.py
│
├── artifacts/                    # Generated outputs (gitignored by default)
│   ├── reports/                  # HTML reports, traces, etc.
│   ├── logs/                     # Framework logs from core/logger.py
│   └── screenshots/              # Screenshots on failure
│
├── config/
│   ├── .env.dev                  # Dev env variables (local only)
│   ├── .env.prod                 # Prod env variables (local only)
│   ├── .env.dev.example          # Example dev config for cloning
│   ├── .env.prod.example         # Example prod config for cloning
│   └── env_loader.py             # Thin wrapper around core.config
│
├── conftest.py                   # Global pytest & pytest-playwright config
├── pytest.ini                    # Pytest discovery + markers
├── requirements.txt              # Python dependencies
├── README.md
└── .gitignore
```

---

## 🚀 Setup & Installation

### 1. Create & activate virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
# or
venv\Scripts\activate           # Windows
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
playwright install chromium
```

The CI workflow (`.github/workflows/playwright.yml`) runs the same steps in GitHub Actions.

---

## 🌐 Environments & Configuration

- Environment variables are loaded by `core.config.load_environment(env_name)` from:
  - `config/.env.dev`
  - `config/.env.prod`
- `conftest.py` wires this to a custom CLI flag:

```bash
pytest --env dev   # uses config/.env.dev  (default)
pytest --env prod  # uses config/.env.prod
```

### Required keys in `.env` files

```env
BASE_URL=...
LOGIN_URL=...
SIGNUP_URL=...
FORGOT_PASSWORD_URL=...

VALID_EMAIL=...
VALID_PASSWORD=...

HEADLESS=true
SLOW_MO=0
TIMEOUT=30000
```

- **Never commit real credentials.**
  - Check in only `.env.dev.example` / `.env.prod.example`.
  - For CI, secrets are injected through the GitHub Actions workflow.

---

## ▶️ Running Tests

### All tests (default dev environment)

```bash
pytest --env dev
```

### Specific suites

```bash
pytest tests/test_login.py --env dev
pytest tests/test_signup.py --env dev
pytest tests/test_forgot_password.py --env dev
```

### Visible (non-headless) browser

Set `HEADLESS=false` in `config/.env.dev`, then:

```bash
pytest --env dev
```

### HTML report

```bash
pytest --env dev --html=reports/report.html --self-contained-html
```

You can move reports under `artifacts/reports/` if you prefer; just update the path in the command and CI workflow.

---

## 📋 Test Coverage (Current Flow)

### Login (`tests/test_login.py`)

- **Valid Login**: redirects away from `/auth/login` when email/password are correct.
- **Wrong Password**: shows an error message (`LoginPage.expect_error_visible()`).
- **Unregistered Email**: shows an error message.
- **Empty Fields**: stays on login page (`/auth/login`).
- **Invalid Email Format**: stays on login page (`/auth/login`).

### Signup (`tests/test_signup.py`)

- **Valid Signup**: redirects away from `/auth/signup`.
- **Existing Email**: shows error via `SignupPage.expect_error_visible()`.
- **Mismatched Passwords**: stays on `/auth/signup`.
- **Empty Fields**: stays on `/auth/signup`.
- **Weak Password**: stays on `/auth/signup`.

### Forgot Password (`tests/test_forgot_password.py`)

- **Valid data**: success message visible via `ForgotPasswordPage.expect_success_msg_visible()`.
- **Unregistered email**: remains on `/auth/forget-password`.
- **Empty form**: remains on `/auth/forget-password`.
- **Invalid email**: remains on `/auth/forget-password`.
- **Mismatched passwords**: remains on `/auth/forget-password`.
- **Back to login link**: navigates to `/auth/login`.

---

## 🧩 Core Design Concepts

- **Page Object Model (POM)**:
  - All locators and flows live under `pages/`.
  - Each page wraps `playwright.sync_api.Page` with methods like `login(...)`, `signup(...)`, `submit_forgot_password(...)`.
- **BasePage (`core/base_page.py`)**:
  - Provides navigation helpers (`goto`, `open_path`) and URL assertions (`expect_url_matches`, `expect_url_not_matches`).
  - Supplies a shared logger via `core.logger.get_logger`.
- **Config (`core/config.py` + `config/env_loader.py`)**:
  - Loads env-specific `.env` files and exposes helpers like `base_url()`, `login_url()`, `timeout()`, `is_headless()`.
- **Logging (`core/logger.py`)**:
  - Framework logging to stdout and `artifacts/logs/framework.log` with consistent formatting.
- **Fixtures (`fixtures/` + `conftest.py`)**:
  - Uses `pytest-playwright` native `page` fixture with custom timeout and browser/context options.
  - Adds `logged_in_page` fixture for tests that need an authenticated session.

---

## 🔧 Extending the Framework

- **Add a new page**:
  1. Create `pages/<new_page>_page.py`.
  2. Implement a class with locators + actions (optionally inherit from `BasePage`).
  3. Use it from a new test file in `tests/`.

- **Add a new test suite**:
  1. Create `tests/test_<feature>.py`.
  2. Use the appropriate Page Object(s) and fixtures (`page`, `browser_page`, `logged_in_page`).

- **Data & AI layers**:
  - `data/` can be expanded with factories and schema validation.
  - `ai/` is reserved for future tooling like automated test generation, log analysis, and flaky-test detection.

---

## 🧱 Tech Stack

- **Python 3.10+**
- **Playwright** (`playwright`, `pytest-playwright`)
- **Pytest** (test runner)
- **python-dotenv** (environment management)
- **pytest-html** + **pytest-metadata** (HTML reporting & metadata)

This README reflects the **current folder layout and test flow** of the project. Update it alongside structural changes to keep it as the source of truth. 
