import logging
from random import randint


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)
    item.cls.rand_part = randint(100000, 999999)


class BaseTest:
    log = logging.getLogger(__name__)
    rand_part = randint(100000, 999999)
