from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): 
        return '<User {}>'.format(self.name)

class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))

    def __repr__(self):
        return '<Todo {}>'.format(self.todo)

# Class untuk tabel CategoryProduct
class CategoryProduct(db.Model):
    __tablename__ = 'category_product'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relasi satu ke banyak dengan Product
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return f"<CategoryProduct {self.name}>"

# Class untuk tabel Product
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key untuk relasi dengan CategoryProduct
    category_id = db.Column(db.BigInteger, db.ForeignKey('category_product.id'), nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"
