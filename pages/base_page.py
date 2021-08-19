from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base functions of Complex App pages"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element(self, xpath: str, timeout=0) -> WebElement:
        """Returns element after searching by xpath with timeout"""

        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def verify_element_presence(self, xpath: str, timeout=0) -> bool:
        """Returns True if can find element in timeout"""

        try:
            self.element(xpath, timeout)
            return True
        except TimeoutException:
            return False

    def verify_message(self, message: str, timeout=0) -> bool:
        """Returns True if can find element containing message in timeout"""

        return self.verify_element_presence(f'.//div[contains(text(),"{message}")]', timeout)

    @staticmethod
    def fill_input(element: WebElement, value=''):
        """Sets value of input"""

        element.clear()
        element.send_keys(value)
