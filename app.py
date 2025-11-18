from flask import Flask, jsonify, request

app = Flask(__name__)


users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]


def get_next_id():
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    new_data = request.get_json()
    
    if not new_data or 'name' not in new_data or 'email' not in new_data:
        return jsonify({"error": "Invalid data"}), 400

    new_user = {
        "id": get_next_id(),
        "name": new_data['name'],
        "email": new_data['email']
    }
    
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)