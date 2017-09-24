from flask import Blueprint, jsonify, request
from .models import Todo

todo = Blueprint('simple_page', __name__)


@todo.route("/api/todo", methods=['GET'])
def list_item():
    todos = Todo.query.all()
    todo_list = []

    for todo in todos:
        todo_list.append(todo.to_dict())

    return jsonify({"todos": todo_list})


@todo.route("/api/todo", methods=['POST'])
def create_item():
    todo = Todo(request.form.to_dict().get("name"))
    return jsonify({"todo": todo.to_dict()})
