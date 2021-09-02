from entities.post import Post
from constants.post import PostConstants
from pages.base_post_edit_page import BasePostEditPage
from pages.profile_bar import ProfileBar


class PostCreatePage(BasePostEditPage):
    """Representation of Create Post Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_bar = ProfileBar(self.driver)

    def create_post(self, post: Post):
        self.fill_post_form(post)

        create_button = self.element(self.constants.CREATE_POST_BUTTON_XPATH)
        create_button.click()

        from pages.post_details_page import PostDetailsPage
        return PostDetailsPage(self.driver)
