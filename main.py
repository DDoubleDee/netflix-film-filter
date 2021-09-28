import pandas
from flask import Flask
from config import dbconn
from sqlalchemy import create_engine
from typefilter import typefilter
from sortdate import sortdate
from searchengine import search
from csvtosql import csvtosql

#engine = create_engine(dbconn())
#csvtosql(engine)  # Check for table, if doesn't exist, write a new one
usertype = 0  # user input. 0 = No filter, 1 = Movie, 2 = TV Show.
#mlist = typefilter(engine, usertype)  # Filtering by type and forming the list for further manipulations
userdate = 0  # user input. 0 = unsorted, 1 = condescending, 2 = ascending
#mlist = sortdate(mlist, userdate)  # Sorting by release date
usersearch = 'transformers'  # user input. Search bar contents. If empty = do nothing
s1 = True  # Search by title /user input. All of these are toggles
s2 = True  # Search by country
s3 = True  # Search by genre
s4 = True  # Search by actor
s5 = True  # Search by description
#if usersearch != '':
    #mlist = search(mlist, usersearch, s1, s2, s3, s4, s5)  # Execute search
#output = mlist
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello world!"
@app.route("/test")
def test():
    return "TEST"
if __name__ == "__main__":
    app.run(debug=True)
