from flask import Flask
from src.apps.todo.api import todo

app = Flask(__name__)
app.config.from_object('src.config.DevelopmentConfig')
app.register_blueprint(todo)

# data = {
#     "todo": [
#         {
#             "item": "Procesador",
#             "quantity": 2,
#         },
#         {
#             "item": "Tarjeta madre",
#             "quantity": 10,
#         }
#     ]
# }

# @app.before_request
# def before_request():
#   response = jsonify({ 'message': 'Error'})
#   response.status_code = 422
#   return response

app.run(debug=True, port=3333, host="0.0.0.0")
