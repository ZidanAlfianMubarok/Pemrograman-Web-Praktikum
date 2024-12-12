from flask import request
from app.model.category_product import CategoryProduct
from app import response, db
from flask_jwt_extended import jwt_required

@jwt_required()  # Melindungi fungsi index dengan JWT
def index():
    try:
        categories = CategoryProduct.query.all()
        data = transform(categories)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while retrieving categories.')

def transform(categories):
    array = []
    for category in categories:
        array.append({
            'id': category.id,
            'name': category.name,
            'description': category.description
        })
    return array

@jwt_required()  # Melindungi fungsi store dengan JWT
def store():
    try:
        name = request.json['name']
        description = request.json.get('description', '')

        category = CategoryProduct(name=name, description=description)
        db.session.add(category)
        db.session.commit()

        return response.ok('', 'Successfully created category!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while creating category.')

@jwt_required()  # Melindungi fungsi update dengan JWT
def update(id):
    try:
        category = CategoryProduct.query.get(id)
        if not category:
            return response.badRequest([], 'Category not found.')

        name = request.json.get('name', category.name)
        description = request.json.get('description', category.description)

        category.name = name
        category.description = description

        db.session.commit()

        return response.ok('', 'Successfully updated category!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while updating category.')

@jwt_required()  # Melindungi fungsi delete dengan JWT
def delete(id):
    try:
        category = CategoryProduct.query.get(id)
        if not category:
            return response.badRequest([], 'Category not found.')

        db.session.delete(category)
        db.session.commit()

        return response.ok('', 'Successfully deleted category!')
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while deleting category.')

@jwt_required()  # Melindungi fungsi show dengan JWT
def show(id):
    try:
        category = CategoryProduct.query.get(id)
        if not category:
            return response.badRequest([], 'Category not found.')

        data = {
            'id': category.id,
            'name': category.name,
            'description': category.description
        }
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while retrieving category.')
