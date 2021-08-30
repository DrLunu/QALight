"""Tests for Login Page of QA Complex App"""

from conftest import BaseTest
from entities.user import User
from pages.login_page import SignUpConfig


class TestLoginPage(BaseTest):

    def test_empty_fields_login(self, login_page):
        """
        - Login with cleared fields
        - Verify error message
        """
        login_page.login()
        self.log.info("Login with cleared fields")

        assert login_page.verify_message(login_page.constants.INVALID_LOGIN_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

    def test_invalid_fields_login(self, login_page):
        """
        - Login with invalid field values
        - Verify error message
        """
        login_page.login(User())
        self.log.info("Login with invalid field values")

        assert login_page.verify_message(login_page.constants.INVALID_LOGIN_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

    def test_successful_login(self, home_page):
        """
        - Sign In with registered user's data
        - Verify Sign In
        """
        assert home_page.verify_page()
        self.log.info("Successful login")

    def test_logout(self, home_page):
        """
        - Sign In
        - Sign Out
        - Verify Sign Out
        """
        login_page = home_page.profile_bar.log_out()
        assert login_page.verify_page()
        self.log.info("Successful logout")

    def test_signup_empty_fields(self, login_page):
        """
        - Sign up with cleared fields
        - Check page
        """
        login_page.sign_up()
        self.log.info("Sign up with cleared fields")

        assert login_page.verify_page()
        self.log.info("Remain on start page")

    def test_signup_used_username(self, login_page, new_user, registered_user):
        """
        - Sign up with taken username
        - Check page
        - Verify error message
        """
        new_user.username = registered_user.username
        login_page.sign_up(new_user)
        self.log.info("Sign up with taken username")

        assert login_page.verify_page()
        self.log.info("Remain on start page")

        assert login_page.verify_message(login_page.constants.USERNAME_IS_TAKEN_MESSAGE_TEXT, 2)
        self.log.info("Error message match to expected")

    def test_username_error_messages(self, login_page):
        """
        - Fill username with too short value
        - Verify error message
        - Fill username with too long value
        - Verify error message
        - Fill username with inappropriate value
        - Verify error message
        """
        login_page.fill_input(login_page.sign_up_username_input, login_page.constants.SHORT_USERNAME)
        self.log.info("Sign up with too short username")
        assert login_page.verify_message(login_page.constants.USERNAME_IS_SHORT_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

        login_page.fill_input(login_page.sign_up_username_input, login_page.constants.LONG_USERNAME)
        self.log.info("Sign up with too long username")
        assert login_page.verify_message(login_page.constants.USERNAME_IS_LONG_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

        login_page.fill_input(login_page.sign_up_username_input, login_page.constants.INVALID_USERNAME)
        self.log.info("Sign up with invalid username")
        assert login_page.verify_message(login_page.constants.USERNAME_IS_INVALID_MESSAGE_TEXT, 3)
        self.log.info("Error message match to expected")

    def test_signup_invalid_email(self, login_page, new_user):
        """
        - Sign up with invalid email
        - Check page
        - Verify error message
        """
        new_user.email = login_page.constants.INVALID_EMAIL
        login_page.sign_up(new_user)
        self.log.info("Sign up with invalid email")

        assert login_page.verify_page()
        self.log.info("Remain on start page")

        assert login_page.verify_message(login_page.constants.EMAIL_IS_INVALID_MESSAGE_TEXT, 2)
        self.log.info("Error message match to expected")

    def test_signup_invalid_password(self, login_page, new_user):
        """
        - Sign up with invalid password
        - Check page
        - Verify error message
        """
        new_user.password = login_page.constants.SHORT_PASSWORD
        login_page.sign_up(new_user)
        self.log.info("Sign up with invalid password")

        assert login_page.verify_page()
        self.log.info("Remain on start page")

        assert login_page.verify_message(login_page.constants.PASSWORD_IS_SHORT_MESSAGE_TEXT, 2)
        self.log.info("Error message match to expected")

    def test_successful_signup(self, login_page, new_user):
        """
        - Sign Up with valid data
        - Verify Sign Up
        """
        home_page = login_page.sign_up(new_user, SignUpConfig(is_home_page_expected=True))
        self.log.info("Sign up with valid data")

        assert home_page.verify_page()
        self.log.info("Successful Sign Up")
