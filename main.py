from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
from werkzeug.security import check_password_hash
from config import dbconn, skey
from sqlalchemy import create_engine
from typefilter import typefilter
from sortdate import sortdate
from searchengine import search
from csvtosql import csvtosql
from user import User, getuser

engine = create_engine(dbconn())
csvtosql(engine)  # Check for both users and movielist table, if doesn't exist, write a new one
#usertype = 0  # user input. 0 = No filter, 1 = Movie, 2 = TV Show.
#mlist = typefilter(engine, usertype)  # Filtering by type and forming the list for further manipulations
#userdate = 0  # user input. 0 = unsorted, 1 = condescending, 2 = ascending, 3 = sort by name a-z, 4 = sort by name z-a
#mlist = sortdate(mlist, userdate)  # Sorting by release date
#usersearch = 'transformers'  # user input. Search bar contents. If empty = do nothing
#s1 = True  # Search by title /user input. All of these are toggles
#s2 = True  # Search by country
#s3 = True  # Search by genre
#s4 = True  # Search by actor
#s5 = True  # Search by description
#if usersearch != '':
    #mlist = search(mlist, usersearch, s1, s2, s3, s4, s5)  # Execute search
mlist = engine.execute("SELECT * FROM netflixlist WHERE id<10").fetchall()
login_manager = LoginManager()
SECRET_KEY = skey()
app = Flask(__name__)
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.getdb(user_id)
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html", mlist=mlist)
@app.route("/filter", methods=['GET', 'POST'])
def filter():
    if request.method == "POST":
        userdate = int(request.form.get('sorter'))
        usertype = int(request.form.get('filterer'))
        outlist = typefilter(engine, usertype)
        outlist2 = sortdate(outlist, userdate)
        usersearch = request.form.get('searchbar')
        s1 = request.form.get('titlecheck')
        s2 = request.form.get('countrycheck')
        s3 = request.form.get('genrecheck')
        s4 = request.form.get('castcheck')
        s5 = request.form.get('desccheck')
        if usersearch != '':
            outlist3 = search(outlist2, usersearch, s1, s2, s3, s4, s5)
        else:
            outlist3 = outlist2
        return render_template("home.html", mlist=outlist3)
    else:
        return render_template("home.html", mlist=mlist)
@app.route("/profile") #add /username later, if no session redirect to login
def profile():
    if current_user.is_authenticated:
        return render_template("profile.html")
@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
@app.route("/profile/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == "POST":
        user = getuser(request.form.get('inputfield'), engine)
        if user and check_password_hash(user[3], request.form.get('password')):
            userlogin = User().create(user)
            remain = True if request.form.get('remain') == 'on' else False
            login_user(userlogin, remember=remain)
            return redirect(url_for('profile'))
    return render_template("login.html")
@app.route("/profile/register")
def register():
    return render_template("register.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
if __name__ == "__main__":
    app.run(debug=True)
