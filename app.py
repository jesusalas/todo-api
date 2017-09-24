from flask import Flask
from src.apps.todo.api import todo
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('src.config.DevelopmentConfig')

db = SQLAlchemy(app)

app.register_blueprint(todo)

app.run(debug=True, port=3333, host="0.0.0.0")
