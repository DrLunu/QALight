import enum


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
