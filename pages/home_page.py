from selenium.webdriver.remote.webelement import WebElement
from constants.home_page import HomePageConstants
from pages.base_page import BasePage


class HomePage(BasePage):
    """Representation of Home Page"""

    # Elements
    __log_out_button: WebElement

    def log_out(self):
        """Clicks on Log Out button"""

        self.__log_out_button = self.find_element_by_xpath(HomePageConstants.LOG_OUT_BUTTON_XPATH, 3)
        self.__log_out_button.click()

    def verify_page(self) -> bool:
        """Returns True if current page is Home Page"""

        return self.verify_element_presence(HomePageConstants.LOG_OUT_BUTTON_XPATH, 3)
