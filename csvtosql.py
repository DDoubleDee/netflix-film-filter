import pandas


def csvtosql(engine):
    if not engine.has_table('netflixlist'):
        sheet = pandas.read_csv('netflix.csv', keep_default_na=False)  # There are 6234 entries in this list
        sheet.index.name = 'id'
        sheet.to_sql('netflixlist', con=engine, if_exists='replace')
    if not engine.has_table('users'):
        userlist = pandas.DataFrame([['root@root.root', 'root', 'root']], columns = ["email", "nickname", "password"])
        userlist.index.name = 'id'
        userlist.to_sql('users', con=engine, if_exists='replace')
