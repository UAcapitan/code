
import re
import random
import sqlite3
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

def query_to_db(query, commit=False):
    with sqlite3.connect('words.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)

        if commit:
            conn.commit()
        else:
            return cursor.fetchall()

query_to_db(
    '''CREATE TABLE IF NOT EXISTS words (
        word TEXT,
        translation TEXT,
        definition TEXT
    )''',
    commit=True
)


def get_word_definition(word):
    try:
        url = f"https://www.dictionary.com/browse/{word}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        definition_element = soup.find("div", {"data-type": "word-definition-content"}).find("p")

        if definition_element:
            definition = definition_element.get_text().split(";")[0].strip()
        else:
            definition = ""
        
        return definition
    except:
        return ""

def get_translated_word(word):
    try:
        translator = Translator()
        translation = translator.translate(word, src='en', dest='uk')
        return translation.text
    except:
        return ""

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/add-word')
def add_word():
    return render_template("add_word.html")

@app.route('/validate-word', methods=["POST"])
def validate_word():
    word = request.form.get("word", "")

    data = {
        "word": word.lower(),
        "translation": get_translated_word(word).lower(),
        "definition": get_word_definition(word)
    }
    return render_template("validate_word.html", **data)

@app.route('/save-word', methods=["POST"])
def save_word():
    word = request.form.get("word", "")
    translation = request.form.get("translation", "")
    definition = request.form.get("definition", "")

    query_to_db(
        f'''INSERT INTO words (word, translation, definition) 
        VALUES ('{word}', '{translation}', '{definition}')''',
        commit=True
    )

    data = {
        "success": True
    }
    return render_template("add_word.html", **data)

@app.route('/see-words')
def see_words():
    page = request.args.get('page', 1, type=int)
    items_per_page = 10
    offset = (page - 1) * items_per_page

    words = query_to_db(f"SELECT * FROM words LIMIT {items_per_page} OFFSET {offset};")
    total_items = query_to_db("SELECT COUNT(*) FROM words;")[0][0]
    total_pages = int(total_items / items_per_page) + (total_items % items_per_page > 0)

    data = {
        "words": words,
        "page": page,
        "total_pages": total_pages
    }
    
    return render_template("see_words.html", **data)

@app.route('/learn-words-levels')
def learn_words_levels():
    return render_template("learn_words_levels.html")

@app.route('/learn-words/<int:count>')
def learn_words(count):
    return redirect(
        random.choice([
            f"/learn-words/{count}/ua-eng",
        ])
    )

@app.route("/learn-words/<int:count>/check", methods=["POST",])
def learn_words_check(count):
    answer = request.form.get("answer", "")

    word = request.form.get("word", "")
    translation = request.form.get("translation", "")
    definition = request.form.get("definition", "")

    if answer == word:
        return redirect(f"/learn-words/{count}")
    
    data = {
        "word": [word, translation, definition],
        "count": count
    }
    return render_template("learn_words_mistake.html", **data)

@app.route('/learn-words/<int:count>/<string:mode>')
def learn(count, mode):
    if count == 0:
        word = query_to_db('''SELECT * FROM words ORDER BY RANDOM() LIMIT 1;''')[0]
    else:
        word = query_to_db(
            f'''SELECT * FROM (
            SELECT * FROM words ORDER BY ROWID DESC LIMIT {count}
            ) ORDER BY RANDOM() LIMIT 1;
            '''
        )[0]

    match mode:
        case "ua-eng":
            return render_template("learn_ua_eng.html", word=word, count=count)
        case "definition-ua":
            return render_template("learn_definition_ua.html", word=word, count=count)
        case "eng-ua":
            return render_template("learn_eng_ua.html", word=word, count=count)


if __name__ == '__main__':
    app.run(debug=True)

    # ua > eng
    # definition > eng
    # eng > ua

    # eng > 4 options ua
    # ua > 4 options eng
    # definition > 4 options eng

    # all information about word
