"""Tests for QA Complex App"""

import pytest

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants as LPConst
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLoginPage(BaseTest):

    @pytest.fixture(scope="function", autouse=True)
    def new_browser_session_setup(self, driver):
        """Opens start page at the beginning and clears cookie files after test"""
        driver.get(BaseConstants.START_PAGE_URL)
        self.log.info("Open page")
        yield
        driver.delete_all_cookies()

    @pytest.fixture(scope="function")
    def new_user_data(self):
        """Constructs field value's for new unique user"""
        rand_username = f'{LPConst.BASE_USER_DATA["username"]}{self.rand_part}'
        rand_email = f'{LPConst.BASE_USER_DATA["email"][0]}{self.rand_part}{LPConst.BASE_USER_DATA["email"][1]}'
        rand_password = f'{LPConst.BASE_USER_DATA["password"]}{self.rand_part}'
        yield {"username": rand_username, "email": rand_email, "password": rand_password}

    @pytest.fixture(scope="function")
    def login(self, driver, login_page):
        """Goes to Home Page"""
        login_page.login(LPConst.REGISTERED_USER_DATA["username"], LPConst.REGISTERED_USER_DATA["password"])
        self.log.info("Log In with registered user's data")

    @pytest.fixture(scope="function")
    def login_page(self, driver):
        """Returns Login Page object"""
        yield LoginPage(driver)

    @pytest.fixture(scope="function")
    def home_page(self, driver):
        """Returns Home Page object"""
        yield HomePage(driver)

    def test_empty_fields_login(self, driver, login_page):
        """
        - Login with cleared fields
        - Verify error message
        """
        login_page.login()
        self.log.info("Login with cleared fields")

        assert login_page.verify_message(LPConst.INVALID_LOGIN_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

    def test_invalid_fields_login(self, driver, login_page):
        """
        - Login with invalid field values
        - Verify error message
        """
        login_page.login(LPConst.INVALID_USERNAME, LPConst.SHORT_PASSWORD)
        self.log.info("Login with invalid field values")

        assert login_page.verify_message(LPConst.INVALID_LOGIN_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

    def test_successful_login(self, driver, login, home_page):
        """
        - Sign In with registered user's data
        - Verify Sign In
        """
        assert home_page.verify_page()
        self.log.info("Successful login")

    def test_logout(self, driver, login, home_page, login_page):
        """
        - Sign In
        - Sign Out
        - Verify Sign Out
        """
        home_page.log_out()
        assert login_page.verify_page()
        self.log.info("Successful logout")

    def test_signup_empty_fields(self, driver, login_page):
        """
        - Sign up with cleared fields
        - Check page
        """
        login_page.try_to_sign_up()
        self.log.info("Sign up with cleared fields")

        assert login_page.verify_page()
        self.log.info("Remain on start page")

    def test_signup_used_username(self, driver, login_page, new_user_data):
        """
        - Sign up with taken username
        - Check page
        - Verify error message
        """
        login_page.try_to_sign_up(LPConst.REGISTERED_USER_DATA["username"], new_user_data["email"],
                                  new_user_data["password"])
        self.log.info("Sign up with taken username")

        assert login_page.verify_page()
        self.log.info("Remain on start page")

        assert login_page.verify_message(LPConst.USERNAME_IS_TAKEN_MESSAGE_TEXT, 2)
        self.log.info("Error message match to expected")

    def test_username_error_messages(self, driver, login_page):
        """
        - Fill username with too short value
        - Verify error message
        - Fill username with too long value
        - Verify error message
        - Fill username with inappropriate value
        - Verify error message
        """
        login_page.fill_input(login_page.sign_up_username_input, LPConst.SHORT_USERNAME)
        self.log.info("Sign up with too short username")
        assert login_page.verify_message(LPConst.USERNAME_IS_SHORT_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

        login_page.fill_input(login_page.sign_up_username_input, LPConst.LONG_USERNAME)
        self.log.info("Sign up with too long username")
        assert login_page.verify_message(LPConst.USERNAME_IS_LONG_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

        login_page.fill_input(login_page.sign_up_username_input, LPConst.INVALID_USERNAME)
        self.log.info("Sign up with invalid username")
        assert login_page.verify_message(LPConst.USERNAME_IS_INVALID_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

    def test_signup_invalid_email(self, driver, login_page, new_user_data):
        """
        - Sign up with invalid email
        - Check page
        - Verify error message
        """
        login_page.try_to_sign_up(new_user_data["username"], LPConst.INVALID_EMAIL, new_user_data["password"])
        self.log.info("Sign up with invalid email")

        assert login_page.verify_page()
        self.log.info("Remain on start page")

        assert login_page.verify_message(LPConst.EMAIL_IS_INVALID_MESSAGE_TEXT, 2)
        self.log.info("Error message match to expected")

    def test_signup_invalid_password(self, driver, login_page, new_user_data):
        """
        - Sign up with invalid password
        - Check page
        - Verify error message
        """
        login_page.try_to_sign_up(new_user_data["username"], new_user_data["email"], LPConst.SHORT_PASSWORD)
        self.log.info("Sign up with invalid email")

        assert login_page.verify_page()
        self.log.info("Remain on start page")

        assert login_page.verify_message(LPConst.PASSWORD_IS_SHORT_MESSAGE_TEXT, 2)
        self.log.info("Error message match to expected")

    def test_successful_signup(self, driver, login_page, new_user_data, home_page):
        """
        - Sign Up with valid data
        - Verify Sign Up
        """
        login_page.sign_up(new_user_data["username"], new_user_data["email"], new_user_data["password"])
        self.log.info("Sign up with invalid email")

        assert home_page.verify_page()
        self.log.info("Successful Sign Up")
