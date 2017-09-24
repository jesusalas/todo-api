from flask import Flask
from .apps.todo.api import todo
from .db import db

app = Flask(__name__)
app.config.from_object('src.config.DevelopmentConfig')

db.init_app(app)

app.register_blueprint(todo)
