from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/to-eng/set')
def to_eng_set():
    return render_template('to_eng_set.html')

@app.route('/to-eng')
def to_eng():
    return render_template('to_eng.html')

if __name__ == "__main__":
    app.run(debug=True)