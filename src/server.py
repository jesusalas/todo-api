import os

from flask import Flask

from .apps.todo.controllers import todo
from .db import db, DB_CONNECTION

app = Flask(__name__)
app.config.from_json(os.path.abspath(os.path.join('settings.json')))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION

db.init_app(app)

@app.route("/")
def index():
    return "Welcome to Todo Api"

app.register_blueprint(todo)
