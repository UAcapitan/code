from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/to_do.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % str(self.id)

class DeletedArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_article = db.Column(db.Integer)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % str(self.id)

@app.route('/', methods=['post', 'get'])
def main_page():
    if request.method == 'POST':
        db.session.add(Article(text=request.form.get('text')))
        db.session.commit()

    articles = Article.query.order_by(desc(Article.id)).all()
    context = {
        'articles':articles
    }
    return render_template('index.html', **context)

@app.route('/delete/<int:id>')
def delete_article(id):
    article = Article.query.filter_by(id=id).all()
    db.session.add(DeletedArticle(id_article=id, text=article[0].text))
    Article.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/')

@app.route('/deleted')
def deleted_list():
    articles = DeletedArticle.query.all()
    context = {
        'articles': articles
    }
    return render_template('deleted_list.html', **context)

if __name__ == '__main__':
    app.run(debug=True)