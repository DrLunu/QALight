from entities.user import User
from pages.base_page import BasePage
from constants.profile_bar import ProfileBarConstants


class ProfileBar(BasePage):
    """Representation of Profile Bar"""

    def __init__(self, driver, user: User):
        super().__init__(driver)
        self.constants = ProfileBarConstants
        self.user = user

    def log_out(self):
        """Clicks on Log Out button"""
        self.element(self.constants.LOG_OUT_BUTTON_XPATH, 3).click()
        from pages.login_page import LoginPage
        return LoginPage(self.driver)

    def go_to_create_post(self):
        self.element(self.constants.CREATE_POST_BUTTON_XPATH).click()
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    def go_to_profile(self):
        """"""
        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver)
