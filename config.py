def dbconn():
    i =open('database.ini','r')
    db = i.read()
    i.close()
    return db
