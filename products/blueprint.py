from flask import Blueprint
from flask import render_template
from model import Product
from flask import request
from .forms import ProductForm
from app import db
from flask import redirect
from flask import url_for

products = Blueprint('products', __name__, template_folder='templates')


@products.route('/create', methods=['POST', 'GET'])
def create_product():

    if request.method=='POST':
        name = request.form['name']
        price = request.form['price']
        amount = request.form['amount']
        comment = request.form['comment']

        try:
            product = Product(name=name, price=price, amount=amount, comment=comment)
            db.session.add(product)
            db.session.commit()
        except:
            print('Wrong')

        return redirect(url_for('products.index'))
    else:
        form = ProductForm()
        return render_template('products/create_product.html', form=form)


@products.route('/<id>/edit', methods=['POST', 'GET'])
def edit(id):
    product = Product.query.filter(Product.id==id).first()

    if request.method=='POST':
        form = ProductForm(formdata=request.form, obj=product)
        form.populate_obj(product)
        db.session.commit()

        return redirect(url_for('products.product_details', id=product.id))

    form = ProductForm(obj=product)
    return render_template('products/edit.html', product=product, form=form)


@products.route('/delete/<id>')
def delete(id):
    product = Product.query.filter(Product.id==id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.index'))


@products.route('/')
def index():

    q = request.args.get('q')

    if q:
        all_products = Product.query.filter(Product.name.contains(q) | Product.comment.contains(q)).all()
    else:
        all_products = Product.query.all()
    return render_template('products/index.html', products=all_products)



@products.route('/<id>')
def product_details(id):
    product = Product.query.filter(Product.id==id).first()
    return render_template('products/product_details.html', product=product)
