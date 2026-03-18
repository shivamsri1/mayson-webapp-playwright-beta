class ForgotPasswordLocators:
    EMAIL_INPUT = 'input[name="email"]'
    NEW_PASSWORD_INPUT = 'input[name="password"]'
    CONFIRM_PASSWORD_INPUT = 'input[name="password_repeat"]'
    CONTINUE_BUTTON = 'button:has-text("Continue")'
    BACK_TO_LOGIN_LINK = 'a:has-text("Login"), a:has-text("Sign In"), a:has-text("Back to login"), a[href*="/auth/login"]'
    ERROR_MESSAGE = '.error-message, .alert-danger, [role="alert"], .text-danger, .Toastify__toast--error'
    SUCCESS_MESSAGE = '.success-message, .alert-success, [role="status"], .toast, .Toastify__toast--success'
