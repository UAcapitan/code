from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full = db.Column(db.String(300), nullable=False)
    short = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.short

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        full = request.form['link']
        short = request.form['short']

        article = Page(full=full, short=short)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error'
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)