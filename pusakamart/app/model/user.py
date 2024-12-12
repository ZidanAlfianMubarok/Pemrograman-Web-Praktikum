from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Ubah panjang menjadi 255
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Method for setting password with hash
    def setPassword(self, password):
        self.password = generate_password_hash(password)

    # Method for checking hashed password
    def checkPassword(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return f'<User {self.name}>'
