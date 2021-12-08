from flask import Flask, render_template, request
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

@app.route('/', methods=['post', 'get'])
def main_page():
    if request.method == 'post':
        db.session.add(Article(text=request.form.get('text')))
        db.session.commit()

    articles = Article.query.order_by(desc(Article.id)).all()
    context = {
        'articles':articles
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)