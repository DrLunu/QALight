import logging
import time

from selenium.common.exceptions import TimeoutException, WebDriverException


def retry_till_success(timeout=5, period=0.25):
    def act_decorator(target_func):
        logger = logging.getLogger(__name__)

        def wrapper(*args, **kwargs):
            must_end = time.time() + timeout
            while True:
                try:
                    return target_func(*args, **kwargs)
                except (WebDriverException, AssertionError, TimeoutException) as error:
                    error_name = error if str(error) else error.__class__.__name__
                    logger.debug("Catch %s. Left %s seconds", error_name, (must_end - time.time()))
                    logger.info(time.time())
                    logger.info(must_end)
                    if time.time() >= must_end:
                        logger.warning("Waiting time is out after %s seconds", timeout)
                        raise error
                    time.sleep(period)

        return wrapper

    return act_decorator
