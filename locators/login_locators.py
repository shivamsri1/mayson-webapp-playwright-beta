class LoginLocators:
    EMAIL_INPUT = 'input[name="email"], input[type="email"], #email'
    PASSWORD_INPUT = 'input[name="password"], input[type="password"], #password'
    LOGIN_BUTTON = 'button[type="submit"], button:has-text("Login"), button:has-text("Sign in")'
    ERROR_MESSAGE = '.error-message, .alert-danger, [role="alert"], .text-danger'
    SIGNUP_LINK = 'a:has-text("Sign up"), a:has-text("Register"), a:has-text("Create account")'
