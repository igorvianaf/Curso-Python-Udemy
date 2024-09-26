class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(x, y):
        return x + y

# c1 = Connection()
# c1.set_user('Igor')
# c1.set_password(345)
# print(c1.user)
# print(c1.password)

c1 = Connection.create_auth('Joao', '2345')
print(Connection.soma(4, 6))
print(c1.user)
print(c1.password)
