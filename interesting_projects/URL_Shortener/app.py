# --------------------------------------
# Development start date: 1 Aug 2021
# --------------------------------------

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

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

        url_page = Page.query.filter_by(short=short).all()

        if len(url_page) == 1:
            return render_template('error.html')
        else:
            article = Page(full=full, short=short)
            try:
                db.session.add(article)
                db.session.commit()

                return render_template('success.html', data = {
                    'full': full,
                    'short': short
                })
            except:
                return 'Error'
    else:
        return render_template('main.html')

@app.route('/list')
def list_page():
    pages = Page.query.order_by(desc(Page.id)).limit(10).all()
    print(pages[0].full)
    return render_template('list_page.html', data = {
        'pages': pages
    })

@app.route('/<string:url>')
def open_page(url):
    try:
        url_page = Page.query.filter_by(short=url).first()
        return redirect(url_page.full)
    except:
        return render_template('no_page.html')

if __name__ == '__main__':
    app.run(debug=True)