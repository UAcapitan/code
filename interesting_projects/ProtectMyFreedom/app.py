
import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

import functional as fn


# App settings
app = Flask(__name__)
db = SQLAlchemy()
app.secret_key = "1234"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pmf.db'
app.config['UPLOAD_FOLDER'] = 'static/files'


# Models
# TODO do it with foreign keys
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(512))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    question = db.Column(db.Text)
    author = db.Column(db.String(100))
    date = db.Column(db.DateTime())

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), unique=True)

class Question__Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    author = db.Column(db.String(100))
    date = db.Column(db.DateTime())

class Blog__Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer)

class BlogArticleImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer)
    path = db.Column(db.String(255))


# DB init
db.init_app(app)
with app.app_context():
    db.create_all()


# Views
@app.route("/")
def index():
    if session.get('loggedin', False):
        return redirect("/main")
    return render_template("index.html")

@app.route("/reg", methods=['GET', 'POST'])
def reg():
    if session.get('loggedin', False):
        return render_template("main.html")
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
        if username_exist:
            return 'Username is already used'

        email_exist = User.query.filter_by(email=email).first()
        if email_exist != None:
            return 'Email is already used'

        password = fn.encrypte_password(password)

        try:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            session['loggedin'] = True
            session['id'] = user.id
            session['username'] = user.username
            return redirect('/main')
        except Exception as e:
            print(e)
            return "Error while registration"
    return render_template("reg.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('loggedin', False):
        return render_template("main.html")
    # TODO validation
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        password = fn.encrypte_password(password)

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                session['loggedin'] = True
                session['id'] = user.id
                session['username'] = user.username
                return redirect('/main')
            else:
                return "Unsuccessful login on site"
        else:
            return f"You're not registered with this email: {email}"

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

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/ask", methods=["GET", "POST"])
def ask():
    if session.get('loggedin', False):
        if request.method == "POST":
            title = request.form["title"]
            question = request.form["question"]
            tags = request.form["tags"]

            if title:
                q = Question(
                    title=title, 
                    question=question, 
                    author=session["username"],
                    date=datetime.now())
                db.session.add(q)
                db.session.commit()

                if tags:
                    for tag in tags.strip().split(","):
                        tag_obj = Tag.query.filter_by(tag=tag).first()
                        if tag_obj:
                            tag_id = tag_obj.id
                        else:
                            t = Tag(tag=tag.strip())
                            db.session.add(t)
                            db.session.commit()
                            tag_id = t.id
                        db.session.add(Question__Tags(tag_id=tag_id, article_id=q.id))
                    db.session.commit()
        return render_template("ask.html")
    return redirect("/login")

@app.route("/blog/create", methods=["GET", "POST"])
def blog_create():
    if session.get('loggedin', False):
        if request.method == "POST":
            title = request.form["title"]
            text = request.form["text"]
            tags = request.form["tags"]
            
            if title:
                b = Blog(
                    title=title, 
                    text=text, 
                    author=session["username"],
                    date=datetime.now())
                db.session.add(b)
                db.session.commit()

                if tags:
                    for tag in tags.strip().split(","):
                        tag_obj = Tag.query.filter_by(tag=tag).first()
                        if tag_obj:
                            tag_id = tag_obj.id
                        else:
                            t = Tag(tag=tag.strip())
                            db.session.add(t)
                            db.session.commit()
                            tag_id = t.id
                        db.session.add(Blog__Tags(tag_id=tag_id, article_id=b.id))
                    db.session.commit()

                if "file" in request.files:
                    files = request.files.getlist("file")
                    for file in files:
                        if file.filename == '':
                            pass
                        if file and fn.allowed_file(file.filename):
                            filename = secure_filename(file.filename)
                            date_time = datetime.now().strftime("%a_%-m_%y-%H_%M_%S_")
                            path = os.path.join(app.config["UPLOAD_FOLDER"], date_time + filename)
                            file.save(path)
                            db.session.add(BlogArticleImage(article_id=b.id, path=path))
                            db.session.commit()

        return render_template("blog_create.html")
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
