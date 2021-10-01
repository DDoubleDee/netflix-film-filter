import pandas
from sqlalchemy import Table, Column, Integer, String, MetaData


def csvtosql(engine):
    if not engine.has_table('netflixlist'):
        sheet = pandas.read_csv('netflix.csv', keep_default_na=False)  # There are 6234 entries in this list
        sheet.index.name = 'id'
        sheet.to_sql('netflixlist', con=engine, if_exists='replace')
    if not engine.has_table('users'):
        meta = MetaData()
        users = Table(
            'users', meta,
            Column('id', Integer, primary_key=True),
            Column('email', String),
            Column('nickname', String),
            Column('password', String)
        )
        meta.create_all(engine)
