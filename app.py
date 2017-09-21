from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    "todo": [
        {
            "item": "Procesador",
            "quantity": 2,
        },
        {
            "item": "Tarjeta madre",
            "quantity": 10,
        }
    ]
}


@app.route("/api/todo", methods=['GET'])
def list_item():
    return jsonify(data)


@app.route("/api/todo", methods=['POST'])
def create_item():
    item = request.form.to_dict()
    data["todo"].append(item)
    return jsonify(item)

# @app.route("/valid/<param>/")
# def is_valid(param):
#     print(request.is_secure)
#     print(request.data)
#     print(request.query_string)
#     args = request.args.to_dict()
#     print(args["go"])
#     print(param)
#     # print(request.user_agent)
#     return jsonify({"message": "Es valido"})

app.run(debug=True, port=3333, host="0.0.0.0")
