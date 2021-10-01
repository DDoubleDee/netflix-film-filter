from flask_login import UserMixin


def getuser(input, engine):
    return engine.execute("SELECT * FROM users WHERE email = '{0}'".format(input)).fetchone()
def adduser(name, email, password, engine, i):
    print(engine.execute("SELECT * FROM users".format(name)).fetchall())
    if engine.execute("SELECT COUNT(nickname) FROM users WHERE nickname LIKE '{0}'".format(name)).fetchone()[0] > 0:
        return False
    elif engine.execute("SELECT COUNT(email) FROM users WHERE email LIKE '{0}'".format(email)).fetchone()[0] > 0:
        return False
    else:
        engine.execute("INSERT INTO users (id,email,nickname,password) VALUES ('{0}','{1}', '{2}', '{3}')".format(i, name, email, password))
        return True
class User(UserMixin):
    def getdb(self, user_id, engine):
        self.__user = engine.execute("SELECT * FROM users WHERE id = {0}".format(user_id)).fetchone()
        return self
    def create(self, user):
        self.__user = user
        return self
