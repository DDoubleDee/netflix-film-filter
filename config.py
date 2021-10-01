def dbconn():
    i =open('database.ini','r')
    db = i.read()
    i.close()
    return db
def skey():
    i =open('skey.ini','r')
    db = i.read()
    i.close()
    return db
