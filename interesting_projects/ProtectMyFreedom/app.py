
import os
import re
import random
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
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(512))
    date_of_reg = db.Column(db.DateTime())

class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    question = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("User", backref="author")
    date = db.Column(db.DateTime())

class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), unique=True)

class Question__Tag(db.Model):
    __tablename__ = "question__tag"
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))
    tag = db.relationship("Tag", backref="tags")
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    question = db.relationship("Question", backref="question_obj")

class QuestionAnswer(db.Model):
    __tablename__ = "question_answer"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    question = db.relationship("Question", backref="question_answer_obj")
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("User", backref="author_answer")
    date = db.Column(db.DateTime())

class UserAvatar(db.Model):
    __tablename__ = "user_avatar"
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="user_avatar")


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
    # TODO make page for errors
    if request.method == 'POST':

        username = request.form['username']
        if not re.match(r"^[a-zA-Z0-9_]{1,100}$", username): 
            return "Username is wrong"

        email = request.form['email']
        if not re.match(r"^[a-zA-Z0-9.]{1,20}@[a-z]{1,10}\.[a-z]{1,5}$", email): 
            return "Email is wrong"

        password = request.form['password']
        if not re.match(r"^[a-zA-Z0-9_\-\.]{8,20}$", password):
            return "Password is wrong"

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
            user = User(
                username=username, 
                email=email, 
                password=password,
                date_of_reg=datetime.now().replace(second=0, microsecond=0)
            )
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

    if request.method == "POST":

        email = request.form['email']
        if not re.match(r"^[a-zA-Z0-9.]{1,20}@[a-z]{1,10}\.[a-z]{1,5}$", email): 
            return "Email is wrong"

        password = request.form['password']
        if not re.match(r"^[a-zA-Z0-9_\-\.]{8,20}$", password):
            return "Password is wrong"

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
    page = request.args.get('page', 1, type=int)
    
    tags_count = Tag.query.count()
    rand = list(range(1, tags_count + 1))
    random.shuffle(rand)

    if tags_count > 15:
        n = 15
    else:
        n = tags_count

    data = {
        "questions": Question.query.order_by(Question.id.desc()).paginate(page=page, per_page=10),
        "tags": [Tag.query.filter_by(id=rand.pop(0)).first() for _ in range(n)]
    }

    return render_template("main.html", **data)

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
                    author_id=session["id"],
                    date=datetime.now().replace(second=0, microsecond=0))
                db.session.add(q)
                db.session.commit()

                if tags:
                    for tag in tags.strip().split(","):
                        tag_obj = Tag.query.filter_by(tag=tag).first()
                        if tag_obj:
                            tag_id = tag_obj.id
                        else:
                            try:
                                t = Tag(tag=tag.strip())
                                db.session.add(t)
                                db.session.commit()
                            except:
                                continue
                            tag_id = t.id
                        db.session.add(Question__Tag(tag_id=tag_id, question_id=q.id))
                    db.session.commit()
                return redirect("/main")
        return render_template("ask.html")
    return redirect("/login")

@app.route("/question/<int:id>")
def question(id):
    data = {
        "question": Question.query.filter_by(id=id).first(),
        "popular_answers": [],
        "new_answers": QuestionAnswer.query.filter_by(question_id=id).order_by(QuestionAnswer.id.desc()).limit(4).all(),
        "other_questions": Question.query.order_by(Question.id.desc()).limit(7).all()
    }

    return render_template("question.html", **data)

@app.route("/question/answer", methods=["GET", "POST"])
def question_answer():
    if request.method == "POST":
        answer = request.form["answer"]
        question_id = request.form["question_id"]

        db.session.add(QuestionAnswer(
            text=answer,
            question_id=question_id,
            author_id=session["id"],
            date=datetime.now().replace(second=0, microsecond=0))
        )
        db.session.commit()
        return redirect(f"/question/{question_id}")
    return redirect("/main")

@app.route("/profile/<int:id>")
def profile(id):
    if session.get('loggedin', False):
        if id == 0:
            id = session.get("id")
        user = User.query.filter_by(id=id).first()
        questions = Question.query.filter_by(author_id=id).order_by(Question.id.desc()).limit(3).all()

        data = {
            "user": user,
            "questions": questions,
        }

        return render_template("profile.html", **data)
    return redirect("/login")

@app.route("/tag/<int:id>")
def tag(id):
    page = request.args.get('page', 1, type=int)

    data = {
        "tag": Question__Tag.query.filter_by(tag_id=id).order_by(Question__Tag.id.desc()).all()
    }

    return render_template("tags.html", **data)

@app.route("/profile/avatar", methods=["POST",])
def upload_avatar():
    if session.get('loggedin', False):
        file = request.files["file"]
        if file and fn.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            date_time = datetime.now().strftime("%a_%-m_%y-%H_%M_%S_")
            path = os.path.join(app.config["UPLOAD_FOLDER"], date_time + filename)
            file.save(path)
            if UserAvatar.query.filter_by(user_id=session.get("id")).first():
                print("There is avatar")
                UserAvatar.query.filter_by(user_id=session.get("id")).delete()
                db.session.commit()
            db.session.add(UserAvatar(path=path, user_id=session.get("id")))
            db.session.commit()

    return redirect("/profile/0")

@app.route("/question/answers/<int:id>")
def answers(id):
    page = request.args.get('page', 1, type=int)

    data = {
        "id": id,
        "answers": QuestionAnswer.query.filter_by(question_id=id).order_by(QuestionAnswer.id.desc()).paginate(page=page, per_page=3)
    }

    return render_template("all_answers.html", **data)

if __name__ == "__main__":
    app.run(debug=True)
