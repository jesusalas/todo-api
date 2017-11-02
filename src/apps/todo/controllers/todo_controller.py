from flask import jsonify, request
from flask_restful import Resource

from ..models import Todo


class TodoListController(Resource):
    def get(self):
        todos = Todo.query.all()
        todo_list = []

        for todo in todos:
            todo_list.append(todo.to_dict())

        return jsonify({"todos": todo_list})

    def post(self):
        todo = Todo(request.form.to_dict().get("name")).save().to_dict()
        return jsonify({"todo": todo})


class TodoController(Resource):
    def get(self, id):
        todo = Todo.query.get(id).to_dict()
        return jsonify({"todo": todo})

    def delete(self, id):
        todo = Todo.query.get(id).delete().to_dict()
        return jsonify({"todo": todo})
