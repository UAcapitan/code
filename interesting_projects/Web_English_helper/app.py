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
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
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
            today = date.today()
            t = today.strftime("%m/%d/%y")
            exists = db.session.query(Date.id).filter_by(date=t).first() is not None
            if not exists:
                db.session.add(Date(date=t, points=1))
            else:
                day = Date.query.filter_by(date=t).first()
                day.points += 1
            db.session.commit()
        else:
            post['right'] = [rus, eng]
            post['wrong'] = [rus, answer]

    
    word = random.choice(Words.query.all())
    context = {
        'eng': word.english,
        'rus': word.russian
    }

    if request.method == 'POST':
        return render_template('to_eng.html', **context, **post)
    return render_template('to_eng.html', **context)

if __name__ == "__main__":
    # db.session.add(Words(english='try', russian='TRY'))
    # db.session.add(Words(english='video', russian='VIDEO'))
    # db.session.add(Words(english='task', russian='TASK'))
    # db.session.commit()
    app.run(debug=True, port=5002)