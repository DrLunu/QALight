import enum
import  random

from constants.text_base import TEXT_BASE_UKR


class PostAccessType(enum.Enum):
    PUBLIC = "All Users"
    PRIVATE = "One Person"
    GROUP = "Group Message"


class Post:

    def __init__(self, title: str, body: str, is_unique=False, access_type=PostAccessType.PUBLIC):
        self.title = title
        self.body = body
        self.is_unique = is_unique
        self.access_type = access_type

    @staticmethod
    def randomize_content(rand_part, word_count=10):
        title = "Title" + str(rand_part)
        body = Post.gen_random_text(word_count)
        return Post(title, body)

    @staticmethod
    def gen_random_text(word_count):
        words_list = TEXT_BASE_UKR.replace('\n', ' ').split(' ')
        generated_text_list = []
        for _ in range(word_count):
            generated_text_list.append(random.choice(words_list))
        result_text = ' '.join(generated_text_list)
        return result_text
