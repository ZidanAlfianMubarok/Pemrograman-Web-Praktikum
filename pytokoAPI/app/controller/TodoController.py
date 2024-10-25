from app.model.todo import Todos as Todo
from flask import request
from app import response, db
from app.controller import UserController
from flask_jwt_extended import jwt_required
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

@jwt_required()
def index():
    try:
        user_id = request.args.get('user_id')
        todos = Todo.query.filter_by(user_id=user_id).all()
        data = transform(todos)
        return response.ok(data, "")
    except Exception as e:
        print(e)


# Menyimpan todo baru
def store():
    try:
        todo = request.json['todo']
        desc = request.json['description']
        user_id = request.json['user_id']
        new_todo = Todo(user_id=user_id, todo=todo, description=desc)
        db.session.add(new_todo)
        db.session.commit()
        return response.ok('', 'Successfully created todo!')
    except Exception as e:
        print(e)

# Mengupdate todo berdasarkan ID
def update(id):
    try:
        todo = request.json['todo']
        desc = request.json['description']
        todo_item = Todo.query.filter_by(id=id).first()
        todo_item.todo = todo
        todo_item.description = desc
        db.session.commit()
        return response.ok('', 'Successfully updated todo!')
    except Exception as e:
        print(e)

# Menampilkan todo berdasarkan ID
def show(id):
    try:
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            return response.badRequest([], 'Empty....')
        data = singleTransform(todo)
        return response.ok(data, "")
    except Exception as e:
        print(e)

# Menghapus todo berdasarkan ID
def delete(id):
    try:
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            return response.badRequest([], 'Empty....')
        db.session.delete(todo)
        db.session.commit()
        return response.ok('', 'Successfully deleted data!')
    except Exception as e:
        print(e)

# Transform banyak todos
def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array

# Transform satu todo
def singleTransform(todo):
    data = {
        'id': todo.id,
        'user_id': todo.user_id,
        'todo': todo.todo,
        'description': todo.description,
        'created_at': todo.created_at,
        'updated_at': todo.updated_at,
        'user': UserController.singleTransform(todo.users, withTodo=False)
    }
    return data



@jwt_required(refresh=True)
def refresh():
    user = get_jwt_identity()
    try:
        # Buat access token baru
        new_token = create_access_token(identity=user, fresh=False)
        return response.ok({
            "token_access": new_token
        }, "")
    except Exception as e:
        print(e)
