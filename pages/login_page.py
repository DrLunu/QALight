import time
from selenium.webdriver.remote.webelement import WebElement
from constants.login_page import LoginPageConstants
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Representation of Login Page"""

    # Elements
    __log_in_username: WebElement
    __log_in_password: WebElement
    __log_in_button: WebElement

    __sign_up_username: WebElement
    __sign_up_email: WebElement
    __sign_up_password: WebElement
    __sign_up_button: WebElement

    # Elements init flags
    __log_in_form_is_ready = False
    __sign_up_form_is_ready = False

    @property
    def sign_up_username(self):
        self.__prepare_signup_form()
        return self.__sign_up_username

    def login(self, username='', password=''):
        """Fills login form, and click Log In button"""

        self.__prepare_login_form()

        self.fill_input(self.__log_in_username, username)
        self.fill_input(self.__log_in_password, password)
        self.__log_in_button.click()

    def sign_up(self, username='', email='', password=''):
        """Fills sign up form, and click Sign Up button"""

        self.__prepare_signup_form()

        self.fill_input(self.__sign_up_username, username)
        self.fill_input(self.__sign_up_email, email)
        self.fill_input(self.__sign_up_password, password)
        time.sleep(1)
        self.__sign_up_button.click()

    def __prepare_login_form(self):
        """Initialises elements of log in form if it had not be done before"""

        if self.__log_in_form_is_ready:
            return
        self.__log_in_username = self.find_element_by_xpath(LoginPageConstants.LOG_IN_USERNAME_XPATH)
        self.__log_in_password = self.find_element_by_xpath(LoginPageConstants.LOG_IN_PASSWORD_XPATH)
        self.__log_in_button = self.find_element_by_xpath(LoginPageConstants.LOG_IN_BUTTON_XPATH)
        self.__log_in_form_is_ready = True

    def __prepare_signup_form(self):
        """Initialises elements of sign up form if it had not be done before"""

        if self.__sign_up_form_is_ready:
            return
        self.__sign_up_username = self.find_element_by_xpath(LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        self.__sign_up_email = self.find_element_by_xpath(LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        self.__sign_up_password = self.find_element_by_xpath(LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        self.__sign_up_button = self.find_element_by_xpath(LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        self.__sign_up_form_is_ready = True

    def verify_page(self) -> bool:
        """Returns True if current page is Login Page"""

        return self.verify_element_presence(LoginPageConstants.LOG_IN_BUTTON_XPATH, 3)
