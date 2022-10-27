
import os
import models
import functional as fn
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()

app.secret_key = "1234"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reg", methods=['GET', 'POST'])
def reg():
    # TODO do validation later
    # TODO make page for errors
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re_password']
        
        if password != re_password:
            return "Password are not similar"

        username_exist = models.User.query.filter_by(username=username).first()
        if username_exist != None:
            return 'Username is already used'

        email_exist = models.User.query.filter_by(email=email).first()
        if email_exist != None:
            return 'Email is already used'

        password = fn.encrypte_password(password)

        try:
            # fn.add_to_db(models.User(username=username, email=email, password=password))
            db.session.add(models.User(username=username, email=email, password=password))
            db.session.commit()
            return redirect("/login")
        except:
            return "Error while registration"
    return render_template("reg.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # TODO validation
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        password = fn.encrypte_password(password)

        user = models.User.query.filter_by(email=email).first()

        if user.password == password:
            session['loggedin'] = True
            session['id'] = user.id
            session['username'] = user.username
            return redirect('/main')
        else:
            return "Unsuccessful login on site"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect("/")

@app.route("/main")
def main():
    if session['loggedin']:
        return render_template("main.html")
    else:
        return redirect("/login")

@app.route("/blog")
def blog():
    if session['loggedin']:
        return render_template("blog.html")
    return redirect("/login")

@app.route("/ask")
def ask():
    return render_template("ask.html")

if __name__ == "__main__":
    if not os.path.isfile("db.sqlite"):
        with app.app_context():
            db.create_all()

    app.run()
