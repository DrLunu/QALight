import time
from constants.login_page import LoginPageConstants as LPConst
from entities.user import User
from pages.base_page import BasePage
from pages.home_page import HomePage


class SignUpConfig:
    def __init__(self, is_home_page_expected: bool):
        self.is_home_page_expected = is_home_page_expected


class LoginPage(BasePage):
    """Representation of Login Page"""

    @property
    def sign_up_username_input(self):
        return self.element(LPConst.SIGN_UP_USERNAME_XPATH)

    def login(self, user=User()):
        """Fills login form, and click Log In button"""
        log_in_username = self.element(LPConst.LOG_IN_USERNAME_XPATH)
        log_in_password = self.element(LPConst.LOG_IN_PASSWORD_XPATH)
        log_in_button = self.element(LPConst.LOG_IN_BUTTON_XPATH)

        self.fill_input(log_in_username, user.username)
        self.fill_input(log_in_password, user.password)
        log_in_button.click()
        return HomePage(self.driver)

    def sign_up(self, user=User(), config=SignUpConfig(is_home_page_expected=False)):
        """Fills sign up form, click Sign Up button and check page"""
        sign_up_username = self.element(LPConst.SIGN_UP_USERNAME_XPATH)
        sign_up_email = self.element(LPConst.SIGN_UP_EMAIL_XPATH)
        sign_up_password = self.element(LPConst.SIGN_UP_PASSWORD_XPATH)
        sign_up_button = self.element(LPConst.SIGN_UP_BUTTON_XPATH)
        home_page = HomePage(self.driver)

        self.fill_input(sign_up_username, user.username)
        self.fill_input(sign_up_email, user.email)
        self.fill_input(sign_up_password, user.password)

        if config.is_home_page_expected:
            self.click_and_verify(sign_up_button, home_page.verify_page, 1)
        else:
            time.sleep(1)  # Verification of successful login makes impossible testing negative cases.
            sign_up_button.click()

        return home_page

    def verify_page(self, timeout=3) -> bool:
        """Returns True if current page is Login Page"""
        return self.is_element_presence(LPConst.LOG_IN_BUTTON_XPATH, timeout)
