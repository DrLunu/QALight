class PostConstants:
    """Store constants related to Post Edit Page"""

    TITLE_INPUT_XPATH = './/input[@id="post-title"]'
    BODY_CONTENT_INPUT_XPATH = './/textarea[@id="post-body"]'
    UNIQUE_POST_INPUT_XPATH = './/input[@id="”UniquePost”"]'

    ACCESS_TYPE_SELECT_XPATH = './/select[@id="select1"]'
    SELECTED_OPTION_XPATH = './/option[@value="{}"]'

    CREATE_POST_BUTTON_XPATH = './/form[@action="/create-post"]//button'
    EDIT_POST_BUTTON_XPATH = './/button[contains(text(), "Save Updates")]'

    BACK_TO_POST_LINK_XPATH = './/a[contains(text(), "Back to post permalink")]'

    CREATE_MESSAGE_TEXT = "New post successfully created."
    UPDATE_MESSAGE_TEXT = "Post successfully updated."


