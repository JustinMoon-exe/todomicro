from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

users = []

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error":"Username and password are required"}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    users.append({"username":username, "password":hashed_password})
    return jsonify({"message": f"User {username} registered sucessfully!"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    for user in users:
        if user["username"] == username:
            # Verify the password
            if bcrypt.checkpw(password.encode('utf-8'), user["password"]):
                return jsonify({"message": f"Welcome back, {username}!"}), 200

    return jsonify({"error": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(debug=True)
