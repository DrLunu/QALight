"""Posts related tests"""

from conftest import BaseTest
from entities.post import Post


class TestPost(BaseTest):

    def test_create_post(self, home_page):
        """
        - Login
        - Click to Create Post Button
        - Fill required fields
        - Click Create button
        - Verify message
        - Click on Profile Button
        - Verify access note
        - Verify last post
        """

        create_post_page = home_page.profile_bar.go_to_create_post()
        self.log.info("Go to Create Post Page")

        post = Post.randomize_content(self.rand_part)
        post_details_page = create_post_page.create_post(post)
        self.log.info("Create post")

        message_text = post_details_page.constants.CREATE_MESSAGE_TEXT
        assert create_post_page.verify_message(message_text, 1, "div")
        self.log.info("Message match to expected")

        note_text = post.access_type.value
        assert post_details_page.verify_message(note_text, 1, "u")
        self.log.info("Access note match to expected")

        profile_page = post_details_page.profile_bar.go_to_profile()
        profile_page.verify_last_post_title(post.title)
        self.log.info("Post was successfully added to profile")
