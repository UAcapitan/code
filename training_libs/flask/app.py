from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer)
    decription = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/product/<int:id>')
def product(id):
    return render_template('product.html')

if __name__ == '__main__':
    app.run()