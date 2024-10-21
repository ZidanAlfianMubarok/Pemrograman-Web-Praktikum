from flask import request
from app import app
from app.controller import UserController
from app.controller import ProductController, CategoryProductController

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)

# Product routes
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return ProductController.index()
    else:
        return ProductController.store()

@app.route('/products/<id>', methods=['PUT', 'DELETE'])
def product_detail(id):
    if request.method == 'PUT':
        return ProductController.update(id)
    elif request.method == 'DELETE':
        return ProductController.delete(id)

# Category routes
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        return CategoryProductController.index()
    else:
        return CategoryProductController.store()

@app.route('/categories/<id>', methods=['PUT', 'DELETE'])
def category_detail(id):
    if request.method == 'PUT':
        return CategoryProductController.update(id)
    elif request.method == 'DELETE':
        return CategoryProductController.delete(id)