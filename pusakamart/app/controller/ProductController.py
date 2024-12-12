from flask import request
from app.model.product import Product
from app import response, db
from flask_jwt_extended import jwt_required

@jwt_required()  # Protect index with JWT
def index():
    try:
        products = Product.query.all()
        data = transform(products)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while retrieving products.')

def transform(products):
    array = []
    for product in products:
        array.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'category_id': product.category_id,
            'description': product.description
        })
    return array

@jwt_required()  # Protect store with JWT
def store():
    try:
        name = request.json['name']
        price = request.json['price']
        category_id = request.json['category_id']
        description = request.json.get('description', '')

        product = Product(name=name, price=price, category_id=category_id, description=description)
        db.session.add(product)
        db.session.commit()

        return response.ok('', 'Successfully created product!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while creating product.')

@jwt_required()  # Protect update with JWT
def update(id):
    try:
        product = Product.query.get(id)
        if not product:
            return response.badRequest([], 'Product not found.')

        name = request.json.get('name', product.name)
        price = request.json.get('price', product.price)
        category_id = request.json.get('category_id', product.category_id)
        description = request.json.get('description', product.description)

        product.name = name
        product.price = price
        product.category_id = category_id
        product.description = description

        db.session.commit()

        return response.ok('', 'Successfully updated product!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while updating product.')

@jwt_required()  # Protect delete with JWT
def delete(id):
    try:
        product = Product.query.get(id)
        if not product:
            return response.badRequest([], 'Product not found.')

        db.session.delete(product)
        db.session.commit()

        return response.ok('', 'Successfully deleted product!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while deleting product.')

@jwt_required()  # Protect show with JWT
def show(id):
    try:
        product = Product.query.get(id)
        if not product:
            return response.badRequest([], 'Product not found.')

        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'category_id': product.category_id,
            'description': product.description
        }
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while retrieving product.')
