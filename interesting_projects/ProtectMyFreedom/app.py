
import os
import hashlib
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()

app.secret_key = "1234"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(512))

def encrypte_password(password):
    return hashlib.md5(password.encode("utf_8")).hexdigest()

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

        username_exist = User.query.filter_by(username=username).first()
        if username_exist != None:
            return 'Username is already used'

        email_exist = User.query.filter_by(email=email).first()
        if email_exist != None:
            return 'Email is already used'

        password = encrypte_password(password)

        try:
            db.session.add(User(username=username, email=email, password=password))
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

        password = encrypte_password(password)

        user = User.query.filter_by(email=email).first()

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
    return render_template("main.html")


if __name__ == "__main__":
    if not os.path.isfile("db.sqlite"):
        with app.app_context():
            db.create_all()

    app.run()
