from pages.base_post_edit_page import BasePostEditPage
from pages.profile_bar import ProfileBar


class PostDetailsPage(BasePostEditPage):
    """Representation of Post Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_bar = ProfileBar(self.driver)


