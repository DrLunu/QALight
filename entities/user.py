class User:

    def __init__(self, username='', email='', password=''):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def randomize(rand_part):
        username = "user" + str(rand_part)
        email = username + "@example.com"
        password = "Password" + str(rand_part)
        return User(username, email, password)
