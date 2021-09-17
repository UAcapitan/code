from os import error
from flask import Flask, render_template, request, redirect, make_response
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
    tag = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id

class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    id_product = db.Column(db.Integer)

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/')
def main():
    product_tech = Product.query.filter_by(tag='Tech').order_by(desc(Product.id)).limit(3)
    product_food = Product.query.filter_by(tag='Food').order_by(desc(Product.id)).limit(3)
    product_books = Product.query.filter_by(tag='Books').order_by(desc(Product.id)).limit(3)
    return render_template('main.html', product_tech=product_tech, product_food=product_food, product_books=product_books)

@app.route('/products/<string:tag>')
def products(tag):
    product = Product.query.filter_by(tag=tag).order_by(desc(Product.id))
    return render_template('products.html', products=product)

@app.route('/product/<int:id>')
def product(id):
    product = Product.query.get(id)
    return render_template('product.html', product=product)

@app.route('/basket')
def basket():
    basket_list = request.cookies.get('basket')
    cost = 0
    if basket_list:
        basket_list = basket_list.split()
        basket_list.reverse()
        products = []
        for b in basket_list:
            products.append(Product.query.get(int(b)))
        for product in products:
            cost += int(product.cost)
        return render_template('basket.html', basket=products, cost=cost)
    else:
        return render_template('basket.html', basket=False)

@app.route('/add-in-basket/<int:id>')
def add_in_basket(id):
    basket_list = request.cookies.get('basket')
    if basket_list == None:
        basket_list = ''
    basket = str(basket_list) + ' ' + str(id)
    resp = make_response(render_template('add_in_basket.html'))
    resp.set_cookie('basket', basket)
    return resp

@app.route('/create-product', methods=['POST', 'GET'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        cost = request.form['cost']
        description = request.form['description']
        image = request.form['image']
        tag = request.form['tag']
        password = request.form['password']

        if password == adminPassword:
            product = Product(name=name, cost=cost, description=description, image=image, tag=tag)

            try:
                db.session.add(product)
                db.session.commit()
                return redirect('/')
            except:
                return render_template('error.html', error='Error')
        else:
            return render_template('error.html', error='Incorect password')

    return render_template('create_product.html')

@app.route('/clean-basket')
def clean_basket():
    resp = make_response(render_template('add_in_basket.html'))
    resp.set_cookie('basket', '', expires=0)
    return resp

@app.route('/buy-basket', methods=['POST', 'GET'])
def buy_basket():
    if request.method == 'POST':

        user = request.form['user']

        basket_list = request.cookies.get('basket')
        if basket_list:
            basket_list = basket_list.split()
            basket_list.reverse()
            for b in basket_list:

                basket = Basket(user=user, id_product=int(b))

                try:
                    db.session.add(basket)
                except:
                    return render_template('error.html', error='Error')
            try:
                    db.session.commit()
            except:
                return render_template('error.html', error='Error')

        
        resp = make_response(render_template('basket.html'))
        resp.set_cookie('basket', '', expires=0)
        return resp
    else:
        return render_template('buy_basket.html')

@app.route('/all-orders', methods=['POST', 'GET'])
def all_orders():
    if request.method == 'GET':
        return render_template('all_orders.html', admin=False)
    else:
        password = request.form['password']

        if password == adminPassword:

            products = Basket.query.order_by(desc(Basket.id)).all()

            products_name = []

            for p in products:
                products_name.append(Product.query.get(p.id_product))

            products_name.reverse()

            return render_template('all_orders.html', products=products, products_name=products_name, admin=True)
        else:
            return render_template('error.html', error='Incorect password')

@app.route('/admin')
def admin():
    return render_template('admin.html', admin=True)

if __name__ == '__main__':
    app.run()