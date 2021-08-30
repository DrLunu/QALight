from entities.post import Post
from constants.post_edit_page import PostEditConstants
from pages.base_post_edit_page import BasePostEditPage


class CreatePostPage(BasePostEditPage):
    """Representation of Create Post Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostEditConstants

    def create_post(self, post: Post):
        self.fill_post_form(post)

        create_button = self.element(self.constants.CREATE_POST_BUTTON_XPATH)
        create_button.click()

        from pages.post_page import PostPage
        return PostPage(self.driver, post)
