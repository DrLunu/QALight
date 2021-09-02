from constants.profile_page import ProfilePageConstants
from pages.base_page import BasePage
from pages.profile_bar import ProfileBar


class ProfilePage(BasePage):
    """Representation of Profile Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_bar = ProfileBar(self.driver)
        self.constants = ProfilePageConstants

    def verify_last_post_title(self, title: str):
        text = self.driver.find_element_by_xpath(self.constants.LAST_POST_XPATH).text
        assert text == title
