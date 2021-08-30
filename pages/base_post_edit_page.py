from entities.post import Post
from pages.base_page import BasePage
from constants.post_edit_page import PostEditConstants
from pages.profile_bar import ProfileBar


class BasePostEditPage(BasePage):
    """Base functions of post editing"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostEditConstants
        self.profile_bar = ProfileBar(self.driver)

    def fill_post_form(self, post: Post):
        """Fills required inputs"""

        title_input = self.element(self.constants.TITLE_INPUT_XPATH)
        body_input = self.element(self.constants.BODY_CONTENT_INPUT_XPATH)
        is_unique_input = self.element(self.constants.UNIQUE_POST_INPUT_XPATH)

        access_type_select = self.element(self.constants.ACCESS_TYPE_SELECT_XPATH)
        selected_option = self.element(self.constants.SELECTED_OPTION_XPATH.format(post.access_type.value))

        self.fill_input(title_input, post.title)
        self.fill_input(body_input, post.body)

        if is_unique_input.is_selected() != post.is_unique:
            is_unique_input.click()

        access_type_select.click()
        selected_option.click()
