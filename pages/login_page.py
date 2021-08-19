import time
from constants.login_page import LoginPageConstants as LPConst
from pages.base_page import BasePage

from pages.home_page import HomePage


class LoginPage(BasePage):
    """Representation of Login Page"""

    @property
    def sign_up_username_input(self):
        return self.element(LPConst.SIGN_UP_USERNAME_XPATH)

    def login(self, username='', password=''):
        """Fills login form, and click Log In button"""

        log_in_username = self.element(LPConst.LOG_IN_USERNAME_XPATH)
        log_in_password = self.element(LPConst.LOG_IN_PASSWORD_XPATH)
        log_in_button = self.element(LPConst.LOG_IN_BUTTON_XPATH)

        self.fill_input(log_in_username, username)
        self.fill_input(log_in_password, password)
        log_in_button.click()

    def try_to_sign_up(self, username='', email='', password=''):
        """Fills sign up form, and click Sign Up button"""

        sign_up_username = self.element(LPConst.SIGN_UP_USERNAME_XPATH)
        sign_up_email = self.element(LPConst.SIGN_UP_EMAIL_XPATH)
        sign_up_password = self.element(LPConst.SIGN_UP_PASSWORD_XPATH)
        sign_up_button = self.element(LPConst.SIGN_UP_BUTTON_XPATH)

        self.fill_input(sign_up_username, username)
        self.fill_input(sign_up_email, email)
        self.fill_input(sign_up_password, password)
        time.sleep(1)  # Verification of successful login makes impossible testing negative cases.
        sign_up_button.click()

    def sign_up(self, username, email, password):
        """Fills sign up form, click Sign Up button and check page"""

        sign_up_username = self.element(LPConst.SIGN_UP_USERNAME_XPATH)
        sign_up_email = self.element(LPConst.SIGN_UP_EMAIL_XPATH)
        sign_up_password = self.element(LPConst.SIGN_UP_PASSWORD_XPATH)
        sign_up_button = self.element(LPConst.SIGN_UP_BUTTON_XPATH)
        home_page = HomePage(self.driver)

        self.fill_input(sign_up_username, username)
        self.fill_input(sign_up_email, email)
        self.fill_input(sign_up_password, password)
        self.click_and_verify(sign_up_button, home_page.verify_page, 1)

    def verify_page(self, timeout=3) -> bool:
        """Returns True if current page is Login Page"""

        return self.verify_element_presence(LPConst.LOG_IN_BUTTON_XPATH, timeout)
