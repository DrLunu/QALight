import logging
import pytest
from random import randint
from selenium import webdriver
from constants.base import BaseConstants
from entities.user import User
from pages.login_page import LoginPage
from constants.login_page import LoginPageConstants as LPConst


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)
    item.cls.rand_part = randint(100000, 999999)


class BaseTest:
    log = logging.getLogger(__name__)
    rand_part = randint(100000, 999999)


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH, options=options)
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def registered_user():
    """Returns registered user"""
    user = User(LPConst.REGISTERED_USERNAME, LPConst.REGISTERED_EMAIL, LPConst.REGISTERED_PASSWORD)
    yield user


@pytest.fixture(scope="function")
def login_page(driver):
    """Opens start page at the beginning, returns Login Page object and clears cookie files after test"""
    driver.get(BaseConstants.START_PAGE_URL)
    yield LoginPage(driver)
    driver.delete_all_cookies()


@pytest.fixture(scope="function")
def home_page(login_page, registered_user):
    """Returns Home Page"""
    home_page = login_page.login(registered_user)
    yield home_page
