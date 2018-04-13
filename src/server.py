import os

from flask import Flask
from flask_cors import CORS

from .apps.todo.controllers import todo
from .db import db

app = Flask(__name__)
app.config.from_json(os.path.abspath(os.path.join('settings.json')))

CORS(app)
db.init_app(app)

@app.route("/")
def index():
    """ Retorna mensaje de bienvenida """
    return "Welcome to Todo Api"

app.register_blueprint(todo)
