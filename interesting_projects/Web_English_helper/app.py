from flask import Flask, render_template, request, session
import random
from datetime import date
import sqlite3
from key import KEY

app = Flask(__name__)
app.secret_key = 'web'

with sqlite3.connect('english.db') as con:
    cur = con.cursor()
    cur.execute("CREATE TABLE if not exists words (english text, russian text)")

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/to-eng/set')
def to_eng_set():
    return render_template('to_eng_set.html')

@app.route('/from-eng/set')
def from_eng_set():
    return render_template('from_eng_set.html')

@app.route('/to-eng', methods=['GET', 'POST'])
def to_eng(limit=0):
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
            if 'points' not in session or 'date' not in session:
                session["points"] = 1
                session["date"] = t
            else:
                if session["date"] != t:
                    session["points"] = 1
                    session["date"] = t
                else:
                    session["points"] += 1

        else:
            post['right'] = [rus, eng]
            post['wrong'] = [rus, answer]

    with sqlite3.connect('english.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM words")
        words = cur.fetchall()
        words.reverse()

        if limit == 0:
                word = random.choice(words)
        else:
            word = random.choice(words[:limit])

    points = session["points"]
    
    if points < 50:
        goal = 50
    elif points >= 50 and points < 150:
        goal = 150
    elif points >= 150 and points < 250:
        goal = 250

    context = {
        'eng': word[0],
        'rus': word[1],
        'points': points,
        'goal': goal
    }

    if request.method == 'POST':
        return render_template('to_eng.html', **context, **post)
    return render_template('to_eng.html', **context)

@app.route('/to-eng/<int:limit>', methods=['GET', 'POST'])
def to_eng_limit(limit):
    return to_eng(limit)

@app.route('/from-eng', methods=['GET', 'POST'])
def from_eng(limit=0):
    today = date.today()
    t = today.strftime("%m/%d/%y")

    if request.method == 'POST':
        answer = request.form['answer']
        eng = request.form['eng']
        rus = request.form['rus']
        post = {
            'exist': True,
            'post': answer == rus,
        }
        if answer == rus:
            post['right'] = [eng, answer]
            if 'points' not in session or 'date' not in session:
                session["points"] = 1
                session["date"] = t
            else:
                if session["date"] != t:
                    session["points"] = 1
                    session["date"] = t
                else:
                    session["points"] += 1

        else:
            post['right'] = [eng, rus]
            post['wrong'] = [eng, answer]

    with sqlite3.connect('english.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM words")
        words = cur.fetchall()
        words.reverse()

        if limit == 0:
                word = random.choice(words)
        else:
            word = random.choice(words[:limit])

    points = session["points"]
    
    if points < 50:
        goal = 50
    elif points >= 50 and points < 150:
        goal = 150
    elif points >= 150 and points < 250:
        goal = 250

    context = {
        'eng': word[0],
        'rus': word[1],
        'points': points,
        'goal': goal
    }

    if request.method == 'POST':
        return render_template('from_eng.html', **context, **post)
    return render_template('from_eng.html', **context)

@app.route('/from-eng/<int:limit>', methods=['GET', 'POST'])
def from_eng_limit(limit):
    return from_eng(limit)

@app.route('/add-words', methods=['GET', 'POST'])
def add_words():
    context = {
        'success': True,
        'text': ''
    }
    if request.method == 'POST':
        if request.form['password'] == KEY:
            eng = [i.strip() for i in request.form["english"].split(',')]
            rus = [i.strip() for i in request.form["russian"].split(',')]
            if len(eng) == len(rus):
                new = zip(eng, rus)
                with sqlite3.connect('english.db') as con:
                    cur = con.cursor()
                    for i in new:
                        cur.execute(f"INSERT INTO words (english, russian) values ('{i[0]}','{i[1]}')")
                    con.commit()
                context['text'] = 'Success'
            else:
                context['text'] = 'Error'
        else:
            context['text'] = 'Incorrect password'
    return render_template('add_words.html', **context)

if __name__ == "__main__":
    app.run(debug=True, port=5012)