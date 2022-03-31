from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from password import password_admin
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    tech = db.Column(db.String(300), nullable=False)
    img_1 = db.Column(db.String(300), nullable=False)
    img_2 = db.Column(db.String(300), nullable=True)
    img_3 = db.Column(db.String(300), nullable=True)
    text = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return self.id

@app.route('/')
def main():
    articles = Article.query.order_by(desc(Article.id)).all()
    return render_template('main.html', articles=articles)

@app.route('/article/<int:id>')
def page(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)

@app.route('/add-article', methods=['POST', 'GET'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        tech = request.form['tech']
        img_1 = request.form['img_1']
        img_2 = request.form['img_2']
        img_3 = request.form['img_3']
        text = request.form['text']
        link = request.form['link']
        password = request.form['password']

        if password == password_admin:
            article = Article(title=title, tech=tech, img_1=img_1, img_2=img_2, img_3=img_3, text=text, link=link)
            try:
                db.session.add(article)
                db.session.commit()
                return redirect('/')
            except:
                return render_template('error.html', error='Error')
        else:
            return render_template('error.html', error='Incorrect password')
    return render_template('add_article.html')

@app.route('/article/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.tech = request.form['tech']
        article.img_1 = request.form['img_1']
        article.img_2 = request.form['img_2']
        article.img_3 = request.form['img_3']
        article.text = request.form['text']
        article.link = request.form['link']
        password = request.form['password']

        if password == password_admin:
            try:
                db.session.commit()
                return redirect('/')
            except:
                return render_template('error.html', error='Error')
        else:
            return render_template('error.html', error='Incorrect password')
    return render_template('edit.html', article=article)

@app.route('/article/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        password = request.form['password']
        if password == password_admin:
            try:
                db.session.delete(article)
                db.session.commit()
                return redirect('/')
            except:
                return render_template('error.html', error='Error')
        else:
            return render_template('error.html', error='Incorrect password')     
    return render_template('delete.html', article=article)

if __name__ == '__main__':
    app.run(debug='True')