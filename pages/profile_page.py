from pages.base_page import BasePage
from pages.profile_bar import ProfileBar


class ProfilePage(BasePage):
    """Representation of Profile Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_bar = ProfileBar(self.driver)
