from flask import jsonify, request
from flask_restful import Resource

from ..models import Todo


class TodoListController(Resource):
    def get(self):
        todos = Todo.fetch_all()
        return jsonify({"todos": todos})

    def post(self):
        todo = Todo.create(request.form.to_dict().get("name"))
        return jsonify({"todo": todo})


class TodoController(Resource):
    def get(self, id):
        todo = Todo.find_by_id(id)
        return jsonify({"todo": todo})

    def delete(self, id):
        todo = Todo.remove_by_id(id)
        return jsonify({"todo": todo})
