from entities.post import Post
from pages.base_page import BasePage
from pages.profile_bar import ProfileBar


class PostPage(BasePage):
    """Representation of Post Page"""

    def __init__(self, driver, post: Post):
        super().__init__(driver)
        self.profile_bar = ProfileBar(self.driver)
        self.post = post
