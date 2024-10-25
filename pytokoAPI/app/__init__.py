from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager



# Initialize Flask app
app = Flask(__name__)

jwt = JWTManager(app)  # Inisialisasi JWT
# Load configuration
app.config.from_object(Config)

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy()
migrate = Migrate()

# Import models only after initializing db and migrate
from app.model import user, todo

# Bind the db and migrate to the app
db.init_app(app)
migrate.init_app(app, db)

# Import routes after models and db are initialized
from app import routes
