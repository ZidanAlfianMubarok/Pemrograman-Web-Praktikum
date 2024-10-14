from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Mengambil konfigurasi dari file config
app.config.from_object(Config)

# Inisialisasi SQLAlchemy dan Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes dan models untuk digunakan dalam aplikasi
from app import routes, models
