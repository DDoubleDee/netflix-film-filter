def typefilter(engine, usertype):
    if usertype == 0:
        mlist = engine.execute("SELECT * FROM netflixlist").fetchall()
    elif usertype == 1:
        mlist = engine.execute("SELECT * FROM netflixlist WHERE type = 'Movie'").fetchall()
    elif usertype == 2:
        mlist = engine.execute("SELECT * FROM netflixlist WHERE type = 'TV Show'").fetchall()
    return mlist
