import os

from flask import Flask

from .apps.todo.controllers import todo
from .db import db

app = Flask(__name__)
app.config.from_json(os.path.abspath(os.path.join('settings.json')))

db.init_app(app)

app.register_blueprint(todo)
