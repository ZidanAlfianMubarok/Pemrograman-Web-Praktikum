from flask import request
from app import app
from app.controller import UserController
from app.controller import ProductController, CategoryProductController
from app.controller import TodoController

# Route untuk melihat dan menambah todo
@app.route('/todo', methods=['POST', 'GET'])
def todo():
    if request.method == 'GET':
        return TodoController.index()
    return TodoController.store()

# Route untuk melihat, mengupdate, dan menghapus todo berdasarkan ID
@app.route('/todo/<id>', methods=['PUT', 'GET', 'DELETE'])
def todoDetail(id):
    if request.method == 'GET':
        return TodoController.show(id)
    elif request.method == 'PUT':
        return TodoController.update(id)
    elif request.method == 'DELETE':
        return TodoController.delete(id)

@app.route('/login', methods=['POST'])
def login():
    return UserController.login()


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

@app.route('/products/<id>', methods=['GET', 'PUT', 'DELETE'])
def product_detail(id):
    if request.method == 'GET':
        return ProductController.show(id)
    elif request.method == 'PUT':
        return ProductController.update(id)
    elif request.method == 'DELETE':
        return ProductController.delete(id)


# Category routes
# CategoryProduct routes
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        return CategoryProductController.index()
    else:
        return CategoryProductController.store()

@app.route('/categories/<id>', methods=['GET', 'PUT', 'DELETE'])
def category_detail(id):
    if request.method == 'GET':
        return CategoryProductController.show(id)  # Menampilkan kategori berdasarkan ID
    elif request.method == 'PUT':
        return CategoryProductController.update(id)
    elif request.method == 'DELETE':
        return CategoryProductController.delete(id)

@app.route('/refresh', methods=['POST'])
def refresh():
    return UserController.refresh()
