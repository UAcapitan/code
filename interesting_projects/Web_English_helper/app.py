from flask import Flask, redirect, render_template, request, session
from datetime import date
import random
import sqlite3

app = Flask(__name__)

KEY = 'password'

with sqlite3.connect('english.db') as con:
    cur = con.cursor()
    cur.execute("CREATE TABLE if not exists words (english text, russian text)")

with sqlite3.connect('english.db') as con:
    cur = con.cursor()
    cur.execute("CREATE TABLE if not exists date (id integer, date text, points integer)")

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/to-eng/set')
def to_eng_set():
    return render_template('to_eng_set.html')

@app.route('/from-eng/set')
def from_eng_set():
    return render_template('from_eng_set.html')

def set_points():
    today = date.today()
    t = today.strftime("%m/%d/%y")

    with sqlite3.connect('english.db') as con:
        cur = con.cursor()
        cur.execute(f"SELECT date, points FROM date WHERE date='{t}'")
        points = 1
        for i in cur.fetchall():
            points = i[1] + 1

        if points == 1:
            cur.execute("SELECT * FROM date")
            list_ = cur.fetchall()
            list_.pop(0)
            cur.execute("DELETE FROM date")
            for i in range(len(list_)):
                cur.execute(f"INSERT INTO date (id, date, points) VALUES ({str(i)}, '{list_[i][1]}', 1)")
            cur.execute(f"INSERT INTO date (id, date, points) VALUES (7, '{t}', 1)")
            con.commit()
        else:
            if points <= 250:
                cur.execute(f"UPDATE date SET points={str(points)} WHERE date = '{t}'")

def get_points():
    today = date.today()
    t = today.strftime("%m/%d/%y")

    with sqlite3.connect('english.db') as con:
        cur = con.cursor()
        cur.execute(f"SELECT date, points FROM date WHERE date='{t}'")
        points = 0
        for i in cur.fetchall():
            points = i[1]
    return points

def get_goal():
    points = get_points()

    if points < 50:
        goal = 50
    elif points >= 50 and points < 150:
        goal = 150
    elif points >= 150 and points <= 250:
        goal = 250
    return goal
        
        
@app.route('/to-eng', methods=['GET', 'POST'])
def to_eng(limit=0):
    today = date.today()
    t = today.strftime("%m/%d/%y")

    if request.method == 'POST':
        answer = request.form['answer'].strip()
        eng = request.form['eng']
        rus = request.form['rus']
        post = {
            'exist': True,
            'post': answer.lower() == eng.lower(),
        }
        if answer.lower() == eng.lower():
            post['right'] = [rus, answer if eng == answer else answer.lower()]
            set_points()
        else:
            post['right'] = [rus, eng]
            post['wrong'] = [rus, answer if eng == answer else answer.lower()]

    with sqlite3.connect('english.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM words")
        words = cur.fetchall()
        words.reverse()

        if limit == 0:
                word = random.choice(words)
        else:
            word = random.choice(words[:limit])

    if '`' in word[0]:
        word[0] = word[0].replace("`", "'")

    points = get_points()
    goal = get_goal()

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
        answer = request.form['answer'].strip()
        eng = request.form['eng']
        rus = request.form['rus']
        post = {
            'exist': True,
            'post': answer.lower() == rus.lower(),
        }
        if answer.lower() == rus.lower():
            post['right'] = [eng, answer if rus == answer else answer.lower()]
            set_points()
        else:
            post['right'] = [eng, rus]
            post['wrong'] = [eng, answer if rus == answer else answer.lower()]

    with sqlite3.connect('english.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM words")
        words = cur.fetchall()
        words.reverse()

        if limit == 0:
                word = random.choice(words)
        else:
            word = random.choice(words[:limit])

    if '`' in word[0]:
        word[0] = word[0].replace("`", "'")

    points = get_points()
    goal = get_goal()

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
        try:
            if request.form['password'] == KEY:
                eng = [i.strip() for i in request.form["english"].split(',')]
                rus = [i.strip() for i in request.form["russian"].split(',')]
                if len(eng) == len(rus):
                    new = zip(eng, rus)
                    with sqlite3.connect('english.db') as con:
                        cur = con.cursor()
                        for i in new:
                            if "'" in i[0]:
                                i[0] = i[0].replace("'", "`")
                            cur.execute(f"INSERT INTO words VALUES ('{i[0]}','{i[1]}')")
                        con.commit()
                    context['success'] = True
                    context['text'] = f"Success. Was added {str(len(eng))} words"
                else:
                    context['success'] = False
                    context['text'] = 'Error'
            else:
                context['success'] = False
                context['text'] = 'Incorrect password'
        except:
            context['success'] = False
            context['text'] = 'Error'
    return render_template('add_words.html', **context)

@app.route('/words')
def words():
    with sqlite3.connect('english.db') as con:
        cur = con.cursor()
        history = [[i[0], i[1]] for i in cur.execute("SELECT date, points FROM date")]
        cur.execute("SELECT * FROM words")
        words = cur.fetchall()
        words.reverse()

    context = {
        'words': words[:300],
        'history': history
    }
    return render_template('words.html', **context)

@app.route('/word/<string:eng>/<string:rus>')
def word(eng, rus):

    context = {
        'eng': eng,
        'rus': rus
    }

    return render_template('word.html', **context)

@app.route('/edit/<string:eng>/<string:rus>', methods=['GET', 'POST'])
def edit(eng, rus):

    context = {
        'eng': eng,
        'rus': rus
    }

    if request.method == 'POST':
        if request.form['password'] == KEY:
            english = request.form['english']
            russian = request.form['russian']

            try:
                with sqlite3.connect('english.db') as con:
                    cur = con.cursor()

                    cur.execute(f'''UPDATE words SET english = "{english}", russian = "{russian}"
                                WHERE english = "{eng}" AND russian = "{rus}"''')
                return redirect(f"/word/{english}/{russian}")
            except:
                context['error'] = 'Error'
                return render_template('edit.html', **context)

    return render_template('edit.html', **context)

@app.route('/delete/<string:eng>/<string:rus>', methods=['GET', 'POST'])
def delete(eng, rus):

    context = {
        'eng': eng,
        'rus': rus
    }

    if request.method == 'POST':
        if request.form['password'] == KEY:
            try:
                with sqlite3.connect('english.db') as con:
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM words WHERE english = '{eng}' AND russian = '{rus}'")
                context['success'] = 'Success'
            except:
                context['error'] = 'Error'

    return render_template('delete.html', **context)

if __name__ == "__main__":
    app.run(debug=True)