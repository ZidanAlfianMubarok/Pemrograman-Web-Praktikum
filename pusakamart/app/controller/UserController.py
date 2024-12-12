from app.model.user import Users
from app import response, app, db
from flask import request
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

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


def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while retrieving users.')

def transform(users):
    array = []
    for user in users:
        array.append({
            'id': user.id,
            'name': user.name,
            'email': user.email
        })
    return array

def show(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user: 
            return response.badRequest([], 'User not found')
        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred')

def singleTransform(users, withTodo=True):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    if withTodo:
        todos = []
        for i in users.todos:
            todos.append({
                'id': i.id,
                'todo': i.todo,
                'description': i.description,
            })
        data['todos'] = todos
    return data

# Method for creating a new user
def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        # Buat user baru
        new_user = Users(name=name, email=email)
        new_user.setPassword(password)

        # Simpan user ke database
        db.session.add(new_user)
        db.session.commit()

        return response.ok('', 'Successfully created data!')
    except Exception as e:
        # Tampilkan error yang lebih rinci
        print(f"Error: {e}")
        return response.badRequest([], f'An error occurred while creating user: {str(e)}')

# Metode untuk update user
def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        user = Users.query.filter_by(id=id).first()

        if not user:
            return response.badRequest([], 'User not found')

        user.name = name
        user.email = email
        user.setPassword(password)

        db.session.commit()
        return response.ok('', 'Successfully updated data!')

    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while updating user.')

# Metode untuk delete user
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()

        if not user:
            return response.badRequest([], 'User not found')

        db.session.delete(user)
        db.session.commit()
        return response.ok('', 'Successfully deleted data!')

    except Exception as e:
        print(e)
        return response.badRequest([], 'An error occurred while deleting user.')

from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

def login():
    try:
        email = request.json['email']
        password = request.json['password']
        
        user = Users.query.filter_by(email=email).first()
        
        if not user:
            return response.badRequest([], 'User not found')

        if not user.checkPassword(password):
            return response.badRequest([], 'Invalid credentials')

        # Data user untuk token
        data = singleTransform(user, withTodo=False)

        # Token dengan durasi berlaku
        expires = timedelta(days=1)
        expires_refresh = timedelta(days=3)

        # Buat access token dan refresh token
        access_token = create_access_token(identity=data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(identity=data, expires_delta=expires_refresh)

        return response.ok({
            "data": data,
            "token_access": access_token,
            "token_refresh": refresh_token,
        }, "Login successful")

    except Exception as e:
        print(e)
