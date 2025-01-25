from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error":"Username and password are required"}), 400

    users.append({"username":username, "password":password})
    return jsonify({"message": f"User {username} registered sucessfully!"}), 201


if __name__ == "__main__":
    app.run(debug=True)
