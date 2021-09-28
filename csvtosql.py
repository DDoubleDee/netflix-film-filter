import pandas


def csvtosql(engine):
    if not engine.has_table('netflixlist'):
        sheet = pandas.read_csv('netflix.csv', keep_default_na=False)  # There are 6234 entries in this list
        sheet.index.name = 'id'
        sheet.to_sql('netflixlist', con=engine, if_exists='replace')
