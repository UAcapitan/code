from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/mr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    url = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return str(self.id)

@app.route('/')
def main():
    meme = Meme.query.get(random.randint(1, Meme.query.count()))

    context = {
        'meme':meme
    }

    return render_template('main_page.html', **context)

@app.route('/add-meme', methods=['POST', 'GET'])
def add_meme():
    if request.method == 'POST':
        title = request.form.get('title')
        url = request.form.get('url')
        db.session.add(Meme(title=title, url=url))
        db.session.commit()
        return redirect('/')
    return render_template('add_meme.html')

@app.route('/list-of-memes')
def list_of_memes():
    list_memes = Meme.query.order_by(desc(Meme.likes)).limit(10).all()
    context = {
        'list':list_memes
    }
    return render_template('list_of_memes.html', **context)

@app.route('/next')
def next():
    return redirect('/')

@app.route('/like/<int:id>')
def like(id):
    meme = Meme.query.get(id)
    meme.likes += 1
    db.session.add(meme)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)