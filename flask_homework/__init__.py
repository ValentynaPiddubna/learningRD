from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import AppConfig


db = SQLAlchemy()
app = Flask(__name__)

app.config.from_object(AppConfig)

db.init_app(app)

from .main import *
from .models import *


with app.app_context():
    db.create_all()