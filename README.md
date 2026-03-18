# 🧪 Mayson Webapp - Playwright Test Framework

A **Python + Playwright** test automation framework for the Mayson webapp.

---

## 📁 Project Structure

```
mayson-webapp-playwright-beta/
│
├── config/                     # Configuration module
│   ├── __init__.py
│   └── settings.py             # Loads .env files & provides helper functions
│
├── pages/                      # Page Object Model (POM)
│   ├── __init__.py
│   ├── login_page.py           # Login page locators & actions
│   └── signup_page.py          # Signup page locators & actions
│
├── tests/                      # Test cases
│   ├── __init__.py
│   ├── test_login.py           # 5 Login test cases (1 positive + 4 negative)
│   └── test_signup.py          # 5 Signup test cases (1 positive + 4 negative)
│
├── .env.dev                    # Dev environment config
├── .env.prod                   # Prod environment config
├── conftest.py                 # Pytest fixtures & setup
├── pytest.ini                  # Pytest settings
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers

```bash
playwright install chromium
```

### 3. Update Credentials

Edit `.env.dev` and `.env.prod` files with **real test credentials**:

```env
VALID_EMAIL=your_test_email@example.com
VALID_PASSWORD=your_test_password
```

---

## ▶️ Running Tests

### Run against DEVELOPMENT environment (default)

```bash
pytest --env dev
```

### Run against PRODUCTION environment

```bash
pytest --env prod
```

### Run only Login tests

```bash
pytest tests/test_login.py --env dev
```

### Run only Signup tests

```bash
pytest tests/test_signup.py --env dev
```

### Run with visible browser (non-headless)

Edit `.env.dev` → set `HEADLESS=false`, then:

```bash
pytest --env dev
```

### Generate HTML report

```bash
pytest --env dev --html=reports/report.html --self-contained-html
```

---

## 📋 Test Cases

### Login Tests (`tests/test_login.py`)

| #  | Test Case                        | Type     | Description                          |
|----|----------------------------------|----------|--------------------------------------|
| 01 | Valid Login                      | ✅ Positive | Login with correct email & password |
| 02 | Wrong Password                   | ❌ Negative | Valid email, incorrect password     |
| 03 | Unregistered Email               | ❌ Negative | Email not in the system             |
| 04 | Empty Fields                     | ❌ Negative | Submit with empty email & password  |
| 05 | Invalid Email Format             | ❌ Negative | Bad email format like 'not-email'   |

### Signup Tests (`tests/test_signup.py`)

| #  | Test Case                        | Type     | Description                          |
|----|----------------------------------|----------|--------------------------------------|
| 01 | Valid Signup                     | ✅ Positive | Register with all valid details     |
| 02 | Already Registered Email         | ❌ Negative | Use email that already exists       |
| 03 | Mismatched Passwords             | ❌ Negative | Password ≠ Confirm Password         |
| 04 | Empty Fields                     | ❌ Negative | Submit with all fields empty        |
| 05 | Weak Password                    | ❌ Negative | Password too short/simple           |

---

## 🌐 Environments

| Environment | URL                                          | Config File |
|-------------|----------------------------------------------|-------------|
| Development | https://app.beemerbenzbentley.site/auth/login | `.env.dev`  |
| Production  | https://app.mayson.dev/                       | `.env.prod` |

---

## 🔧 Customization

### Adding New Pages
1. Create a new file in `pages/` (e.g., `dashboard_page.py`)
2. Define locators and action methods
3. Import and use in your tests

### Adding New Tests
1. Create a new file in `tests/` (e.g., `test_dashboard.py`)
2. Import the relevant Page Object
3. Write test functions following the `test_` prefix convention

---

## 🏗 Tech Stack

- **Python 3.10+**
- **Playwright** - Browser automation
- **Pytest** - Test runner
- **python-dotenv** - Environment management
- **pytest-html** - HTML reports

---

## 🔒 Secrets and Test Data

- Do NOT commit real credentials. Use `.env.dev` / `.env.prod` locally and set real values in CI secrets.
- Non-sensitive defaults are stored in `config/testdata.json.example`. Create `config/testdata.json` locally to override.
- Tests now import data from `config.testdata` (not `config.data`).
