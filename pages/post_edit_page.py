from entities.post import Post
from constants.post import PostConstants
from pages.base_post_edit_page import BasePostEditPage


class EditPostPage(BasePostEditPage):
    """Representation of Post Edit Page"""

    def __init__(self, driver, target_post: Post):
        super().__init__(driver)
        self.constants = PostConstants
        self.target_post = target_post

    def edit_post(self, result_post: Post):
        self.fill_post_form(result_post)

        save_changes_button = self.element(self.constants.EDIT_POST_BUTTON_XPATH)
        save_changes_button.click()

    def go_to_post_page(self):
        self.element(self.constants.BACK_TO_POST_LINK_XPATH).click()
        from pages.post_details_page import PostDetailsPage
        return PostDetailsPage()
