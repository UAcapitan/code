
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(512))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reg", methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re_password']
        if password != re_password:
            return "Password are not similar"
        User(username=username, email=email, password=password)
    return render_template("reg.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/main")
def main():
    return render_template("main.html")


if __name__ == "__main__":
    if not os.path.isfile("db.sqlite"):
        with app.app_context():
            db.create_all()

    app.run()
