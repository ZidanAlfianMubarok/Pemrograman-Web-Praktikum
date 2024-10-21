from app.model.user import Users
from app import response, app, db
from flask import request
from werkzeug.security import generate_password_hash

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

def singleTransform(user):
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
    }

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
