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


class BaseTest:
    log = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(BaseConstants.DRIVER_PATH)
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def new_user():
    """Returns new unique user"""
    rand_part = randint(100000, 999999)
    user = User.randomize(rand_part)
    yield user


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
