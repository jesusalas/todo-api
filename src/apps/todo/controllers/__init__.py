from flask import Blueprint
from flask_restful import Api
from .todo_controller import TodoController, TodoListController


todo = Blueprint('todo', __name__)
api = Api(todo)

api.add_resource(TodoListController, '/api/todo')
api.add_resource(TodoController, '/api/todo/<int:id>')