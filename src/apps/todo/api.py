from flask import Blueprint, jsonify, request
from .models import Todo

todo = Blueprint('todo', __name__)


# fetch the todo's
@todo.route("/api/todo", methods=['GET'])
def list_item():
    todos = Todo.query.all()
    todo_list = []

    for todo in todos:
        todo_list.append(todo.to_dict())

    return jsonify({"todos": todo_list})


# create new todo
@todo.route("/api/todo", methods=['POST'])
def create_item():
    todo = Todo(request.form.to_dict().get("name")).save().to_dict()
    return jsonify({"todo": todo})


# get todo by id
@todo.route("/api/todo/<int:id>")
def get_item(id):
    todo = Todo.query.get(id).to_dict()
    return jsonify({"todo": todo})


# delete todo by id
@todo.route("/api/todo/<int:id>", methods=['DELETE'])
def delete_item(id):
    todo = Todo.query.get(id).delete().to_dict()
    return jsonify({"todo": todo})
