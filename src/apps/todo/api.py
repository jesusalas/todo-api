from flask import Blueprint, jsonify

todo = Blueprint('simple_page', __name__)


@todo.route("/api/todo", methods=['GET'])
def list_item():
    return jsonify({"message": "Obtener lista"})


@todo.route("/api/todo", methods=['POST'])
def create_item():
    return jsonify({"message": "Crear elemento de lista"})
