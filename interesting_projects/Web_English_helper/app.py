from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///english.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Words(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english = db.Column(db.String(255), nullable=False)
    russian = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return 'word'
    
    def __repr__(self):
        return 'word'

class Date(db.Model):
    date = db.Column(db.String(50), primary_key=True)
    points = db.Column(db.Integer, default=1)

    def __str__(self):
        return 'points'
    
    def __repr__(self):
        return 'points'

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/to-eng/set')
def to_eng_set():
    return render_template('to_eng_set.html')

@app.route('/to-eng', methods=['GET', 'POST'])
def to_eng():

    today = date.today()
    t = today.strftime("%m/%d/%y")

    if request.method == 'POST':
        answer = request.form['answer']
        eng = request.form['eng']
        rus = request.form['rus']
        post = {
            'exist': True,
            'post': answer == eng,
        }
        if answer == eng:
            post['right'] = [rus, answer]
            exists = Date.query.filter_by(date=t).first() is not None
            if not exists:
                db.session.add(Date(date=t))
            else:
                day = Date.query.filter_by(date=t).first()
                day.points += 1
                db.session.add(day)
            db.session.commit()
        else:
            post['right'] = [rus, eng]
            post['wrong'] = [rus, answer]

    # if id == 0:
    word = random.choice(Words.query.all())
    # else:
    #     word = random.choice(Words.query.all()[:id])

    try:
        points = Date.query.filter_by(date=t).first()
        points = points.points
    except:
        points = 0
    
    if points < 50:
        goal = 50
    elif points >= 50 and points < 150:
        goal = 150
    elif points >= 150 and points < 250:
        goal = 250

    context = {
        'eng': word.english,
        'rus': word.russian,
        'points': points,
        'goal': goal
    }

    if request.method == 'POST':
        return render_template('to_eng.html', **context, **post)
    return render_template('to_eng.html', **context)

@app.route('/from-eng', methods=['GET', 'POST'])
def from_eng():
    pass

if __name__ == "__main__":
    # db.session.add(Words(english='try', russian='TRY'))
    # db.session.add(Words(english='video', russian='VIDEO'))
    # db.session.add(Words(english='task', russian='TASK'))
    # db.session.commit()
    app.run(debug=True, port=5007)