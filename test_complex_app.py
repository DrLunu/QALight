""""""
import time

import pytest
from conftest import BaseTest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLoginPage(BaseTest):
    LOGIN_PAGE_URL = "https://qa-complex-app-for-testing.herokuapp.com/"
    BASE_USER_DATA = {"username": "user", "email": ("user", "@example.com"), "password": "Password"}
    REGISTERED_USER_DATA = {"username": "user333", "email": "user333@example.com", "password": "369369369369"}

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome(r'C:\Users\DrLunu\PycharmProjects\QALight\drivers\chromedriver.exe')
        yield driver
        driver.close()

    @pytest.fixture(scope="function", autouse=True)
    def new_browser_session_setup(self, driver):
        """Opens start page at the beginning and clears cookie files after test"""

        driver.get(self.LOGIN_PAGE_URL)
        self.log.info("Open page")
        yield
        driver.delete_all_cookies()

    @pytest.fixture(scope="function")
    def new_user_data(self):
        """Constructs field value's for new unique user"""

        rand_username = f'{self.BASE_USER_DATA["username"]}{self.rand_part}'
        rand_email = f'{self.BASE_USER_DATA["email"][0]}{self.rand_part}{self.BASE_USER_DATA["email"][1]}'
        rand_password = f'{self.BASE_USER_DATA["password"]}{self.rand_part}'
        yield {"username": rand_username, "email": rand_email, "password": rand_password}

    def test_empty_fields_login(self, driver):
        """
        - Clear password and login fields
        - Click on Sign In button
        - Verify error message
        """

        username = driver.find_element_by_xpath('.//input[@placeholder="Username"]')
        username.clear()
        password = driver.find_element_by_xpath('.//input[@placeholder="Password"]')
        password.clear()
        self.log.info("Fields were cleared")

        sign_in_button = driver.find_element_by_xpath('.//form[@action="/login"]//button')
        sign_in_button.click()
        self.log.info("Click on button")

        message = driver.find_element_by_xpath('.//div[contains(text(),"Invalid username / password")]')
        assert message.text == "Invalid username / password"
        self.log.info("Error message match to expected")

    def test_invalid_fields_login(self, driver):
        """
        - Clear password and login fields
        - Fill cleared fields with invalid values
        - Click on Sign In button
        - Verify error message
        """

        username = driver.find_element_by_xpath('.//input[@placeholder="Username"]')
        username.clear()
        password = driver.find_element_by_xpath('.//input[@placeholder="Password"]')
        password.clear()
        self.log.info("Fields were cleared")

        username.send_keys("qwertyuio")
        password.send_keys("1234")
        self.log.info("Fields were filled with invalid values")

        sign_in_button = driver.find_element_by_xpath('.//form[@action="/login"]//button')
        sign_in_button.click()
        self.log.info("Click on button")

        massage = driver.find_element_by_xpath('.//div[contains(text(),"Invalid username / password")]')
        assert massage.text == "Invalid username / password"
        self.log.info("Error message match to expected")

    def test_successful_login(self, driver):
        """
        - Clear password and login fields
        - Fill fields with registered user's data
        - Click on Sign In button
        - Verify Sign In
        """

        username = driver.find_element_by_xpath('.//input[@placeholder="Username"]')
        username.clear()
        password = driver.find_element_by_xpath('.//input[@placeholder="Password"]')
        password.clear()
        self.log.info("Fields were cleared")

        username.send_keys(self.REGISTERED_USER_DATA["username"])
        password.send_keys(self.REGISTERED_USER_DATA["password"])
        self.log.info("Fields were filled with registered user's data")

        sign_in_button = driver.find_element_by_xpath('.//form[@action="/login"]//button')
        sign_in_button.click()
        self.log.info("Click on Sign In button")

        assert is_it_homepage(driver)
        self.log.info("Successful login")

    def test_logout(self, driver):
        """
        - Sign In
        - Click on Sign Out button
        - Check page
        """

        username = driver.find_element_by_xpath('.//input[@placeholder="Username"]')
        username.clear()
        password = driver.find_element_by_xpath('.//input[@placeholder="Password"]')
        password.clear()

        username.send_keys(self.REGISTERED_USER_DATA["username"])
        password.send_keys(self.REGISTERED_USER_DATA["password"])

        sign_in_button = driver.find_element_by_xpath('.//form[@action="/login"]//button')
        sign_in_button.click()
        assert is_it_homepage(driver)
        self.log.info("Successful login")

        sign_out_button = driver.find_element_by_xpath('.//form[@action="/logout"]//button')
        sign_out_button.click()
        assert is_it_startpage(driver)
        self.log.info("Successful logout")

    def test_signup_empty_fields(self, driver):
        """
        - Clear fields of registration form
        - Click on Sign Up button
        - Check page
        """

        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        email = driver.find_element_by_xpath('.//input[@id="email-register"]')
        email.clear()
        password = driver.find_element_by_xpath('.//input[@id="password-register"]')
        password.clear()
        self.log.info("Fields were cleared")

        sign_up_button = driver.find_element_by_xpath('.//form[@id="registration-form"]//button[@type="submit"]')
        sign_up_button.click()
        self.log.info("Click on Sign Up button")

        assert is_it_startpage(driver)
        self.log.info("Remain on start page")

    def test_signup_used_username(self, driver, new_user_data):
        """
        - Clear fields of registration form
        - Fill username with already taken value
        - Verify error message
        - Fill email and password with dynamic valid values
        - Click on Sign Up button
        - Check page
        """

        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        email = driver.find_element_by_xpath('.//input[@id="email-register"]')
        email.clear()
        password = driver.find_element_by_xpath('.//input[@id="password-register"]')
        password.clear()
        self.log.info("Fields were cleared")

        username.send_keys("user333")
        assert is_element_exists(driver, './/div[contains(text(),"That username is already taken")]')
        self.log.info("Error message match to expected")

        email.send_keys(new_user_data["email"])
        password.send_keys(new_user_data["password"])
        self.log.info("Fields were filled")

        sign_up_button = driver.find_element_by_xpath('.//form[@id="registration-form"]//button[@type="submit"]')
        sign_up_button.click()
        self.log.info("Click on Sign Up button")

        assert is_it_startpage(driver)
        self.log.info("Remain on start page")

    def test_signup_invalid_username(self, driver, new_user_data):
        """
        - Clear fields of registration form
        - Fill username with too short value
        - Verify error message
        - Fill username with too long value
        - Verify error message
        - Fill username with inappropriate value
        - Verify error message
        - Fill email and password with dynamic valid values
        - Click on Sign Up button
        - Check page
        """

        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        email = driver.find_element_by_xpath('.//input[@id="email-register"]')
        email.clear()
        password = driver.find_element_by_xpath('.//input[@id="password-register"]')
        password.clear()
        self.log.info("Fields were cleared")

        username.send_keys("us")
        assert is_element_exists(driver, './/div[contains(text(),"Username must be at least 3 characters")]')
        username.clear()
        username.send_keys("us" * 30)
        assert is_element_exists(driver, './/div[contains(text(),"Username cannot exceed 30 characters.")]')
        username.clear()
        username.send_keys("us@")
        assert is_element_exists(driver, './/div[contains(text(),"Username can only contain letters and numbers")]')
        username.clear()
        self.log.info("Error messages match to expected")

        email.send_keys(new_user_data["email"])
        password.send_keys(new_user_data["password"])
        self.log.info("Fields were filled")

        sign_up_button = driver.find_element_by_xpath('.//form[@id="registration-form"]//button[@type="submit"]')
        sign_up_button.click()
        self.log.info("Click on Sign Up button")

        assert is_it_startpage(driver)
        self.log.info("Remain on start page")

    def test_signup_invalid_email(self, driver, new_user_data):
        """
        - Clear fields of registration form
        - Fill email with invalid value
        - Verify error message
        - Fill username and password with dynamic valid values
        - Click on Sign Up button
        - Check page
        """

        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        email = driver.find_element_by_xpath('.//input[@id="email-register"]')
        email.clear()
        password = driver.find_element_by_xpath('.//input[@id="password-register"]')
        password.clear()
        self.log.info("Fields were cleared")

        email.send_keys("get_random_email()")
        assert is_element_exists(driver, './/div[contains(text(),"You must provide a valid email address")]')
        self.log.info("Error message match to expected")

        username.send_keys(new_user_data["username"])
        password.send_keys(new_user_data["password"])
        self.log.info("Fields were filled")

        sign_up_button = driver.find_element_by_xpath('.//form[@id="registration-form"]//button[@type="submit"]')
        sign_up_button.click()
        self.log.info("Click on Sign Up button")

        assert is_it_startpage(driver)
        self.log.info("Remain on start page")

    def test_signup_invalid_password(self, driver, new_user_data):
        """
        - Clear fields of registration form
        - Fill password with invalid value
        - Verify error message
        - Fill username and email with dynamic valid values
        - Click on Sign Up button
        - Check page
        """

        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        email = driver.find_element_by_xpath('.//input[@id="email-register"]')
        email.clear()
        password = driver.find_element_by_xpath('.//input[@id="password-register"]')
        password.clear()
        self.log.info("Fields were cleared")

        password.send_keys("123")
        assert is_element_exists(driver, './/div[contains(text(),"Password must be at least 12 characters")]')
        self.log.info("Error message match to expected")

        username.send_keys(new_user_data["username"])
        email.send_keys(new_user_data["email"])
        self.log.info("Fields were filled")

        sign_up_button = driver.find_element_by_xpath('.//form[@id="registration-form"]//button[@type="submit"]')
        sign_up_button.click()
        self.log.info("Click on Sign Up button")

        assert is_it_startpage(driver)
        self.log.info("Remain on start page")

    def test_successful_signup(self, driver, new_user_data):
        """
        - Clear fields of registration form
        - Fill fields with dynamic valid values
        - Click on Sign Up button
        - Verify successful registration
        """

        username = driver.find_element_by_xpath('.//input[@id="username-register"]')
        username.clear()
        email = driver.find_element_by_xpath('.//input[@id="email-register"]')
        email.clear()
        password = driver.find_element_by_xpath('.//input[@id="password-register"]')
        password.clear()
        self.log.info("Fields were cleared")

        username.send_keys(new_user_data["username"])
        email.send_keys(new_user_data["email"])
        password.send_keys(new_user_data["password"])
        self.log.info("Fields were filled with dynamic valid values")

        sign_up_button = driver.find_element_by_xpath('.//form[@id="registration-form"]//button[@type="submit"]')
        time.sleep(1)
        sign_up_button.click()
        self.log.info("Click on Sign Up button")

        assert is_it_homepage(driver)
        self.log.info("Successful registration")


def is_it_homepage(driver: WebDriver) -> bool:
    return is_element_exists(driver, './/form[@action="/logout"]//button')


def is_it_startpage(driver: WebDriver) -> bool:
    return is_element_exists(driver, './/form[@action="/login"]//button')


def is_element_exists(driver: WebDriver, xpath: str) -> bool:
    try:
        WebDriverWait(driver, 3).until(ec.presence_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False
