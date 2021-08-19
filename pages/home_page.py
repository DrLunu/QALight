from constants.home_page import HomePageConstants
from pages.base_page import BasePage


class HomePage(BasePage):
    """Representation of Home Page"""

    def log_out(self):
        """Clicks on Log Out button"""
        self.element(HomePageConstants.LOG_OUT_BUTTON_XPATH, 3).click()

    def verify_page(self, timeout=3) -> bool:
        """Returns True if current page is Home Page"""
        return self.is_element_presence(HomePageConstants.LOG_OUT_BUTTON_XPATH, timeout)
