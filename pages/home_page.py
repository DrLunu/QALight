from constants.home_page import HomePageConstants
from entities.user import User
from pages.base_page import BasePage
from pages.profile_bar import ProfileBar


class HomePage(BasePage):
    """Representation of Home Page"""

    def __init__(self, driver, user: User):
        super().__init__(driver)
        self.constants = HomePageConstants
        self.profile_bar = ProfileBar(self.driver, user)
        self.user = user

    def verify_page(self, timeout=3) -> bool:
        """Returns True if current page is Home Page"""
        message_xpath = self.constants.HELLO_MESSAGE_XPATH.format(username_lower=self.user.username.lower())
        return self.element(message_xpath)
