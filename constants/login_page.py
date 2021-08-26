class LoginPageConstants:
    """Store constants related to Login Page"""

    # Sign Up
    SIGN_UP_USERNAME_XPATH = './/input[@id="username-register"]'
    SIGN_UP_EMAIL_XPATH = './/input[@id="email-register"]'
    SIGN_UP_PASSWORD_XPATH = './/input[@id="password-register"]'
    SIGN_UP_BUTTON_XPATH = './/form[@id="registration-form"]//button[@type="submit"]'

    # Log In
    LOG_IN_USERNAME_XPATH = './/form[@action="/login"]//input[@name="username"]'
    LOG_IN_PASSWORD_XPATH = './/form[@action="/login"]//input[@name="password"]'
    LOG_IN_BUTTON_XPATH = './/form[@action="/login"]//button'

    # Messages
    INVALID_LOGIN_MESSAGE_TEXT = "Invalid username / password"
    USERNAME_IS_TAKEN_MESSAGE_TEXT = "That username is already taken."
    USERNAME_IS_INVALID_MESSAGE_TEXT = "Username can only contain letters and numbers."
    USERNAME_IS_SHORT_MESSAGE_TEXT = "Username must be at least 3 characters."
    USERNAME_IS_LONG_MESSAGE_TEXT = "Username cannot exceed 30 characters."
    EMAIL_IS_TAKEN_MESSAGE_TEXT = "That email is already being used."
    EMAIL_IS_INVALID_MESSAGE_TEXT = "You must provide a valid email address."
    PASSWORD_IS_SHORT_MESSAGE_TEXT = "Password must be at least 12 characters."

    # User data
    REGISTERED_USERNAME = "user333"
    REGISTERED_EMAIL = "user333@example.com"
    REGISTERED_PASSWORD = "369369369369"
    INVALID_USERNAME = "qwertyu?io"
    INVALID_EMAIL = "qwerty"
    SHORT_PASSWORD = "1234"
    SHORT_USERNAME = "qw"
    LONG_USERNAME = "q" * 31
