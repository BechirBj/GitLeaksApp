from flask import Flask, request, jsonify

app = Flask(__name__)

allowed_commands = {
    "date": ["date"],
    "whoami": ["whoami"],
}

@app.route("/", methods=["POST"])
def command():
    user_input = request.get_json().get("command")

    if user_input in allowed_commands:
        return jsonify({"message": "Command allowed"})
    else:
        return jsonify({"message": "Command not allowed"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
