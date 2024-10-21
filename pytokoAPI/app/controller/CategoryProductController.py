from flask import request
from app.model.category_product import CategoryProduct
from app import response, db

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
