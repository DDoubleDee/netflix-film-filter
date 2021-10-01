from flask_login import UserMixin


def getuser(input, engine):
    if "@" in input:
        return engine.execute("SELECT * FROM users WHERE email = {0}".format(input)).fetchone()
    else:
        return engine.execute("SELECT * FROM users WHERE nickname = {0}".format(input)).fetchone()
    return False

class User(UserMixin):
    def getdb(self, user_id, engine):
        self.__user = engine.execute("SELECT * FROM users WHERE id = {0}".format(user_id)).fetchone()
        return self
    def create(self, user):
        self.__user = user
        return self
