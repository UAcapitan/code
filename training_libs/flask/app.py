from os import error
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from password import adminPassword
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/products')
def products():
    product = Product.query.order_by(desc(Product.id)).all()
    return render_template('products.html', products=product)

@app.route('/product/<int:id>')
def product(id):
    product = Product.query.get(id)
    return render_template('product.html', product=product)

@app.route('/basket')
def basket():
    return render_template('basket.html')

@app.route('/create-product', methods=['POST', 'GET'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        cost = request.form['cost']
        description = request.form['description']
        image = request.form['image']
        password = request.form['password']

        if password == adminPassword:
            product = Product(name=name, cost=cost, description=description, image=image)

            try:
                db.session.add(product)
                db.session.commit()
                return redirect('/')
            except:
                return render_template('error.html', error='Error')
        else:
            return render_template('error.html', error='Incorect password')

    return render_template('create_product.html')

if __name__ == '__main__':
    app.run()