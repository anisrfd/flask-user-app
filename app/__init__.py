from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

logging.basicConfig(filename='debug.log',level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controller import user_controller
from app.model import user_model

