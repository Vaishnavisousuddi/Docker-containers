from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
todos = []

@app.route('/')
def home():
    return jsonify({"message": "Welcome to To-Do API!"})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = {
        "id": len(todos) + 1,
        "task": data.get("task"),
        "done": False
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            return jsonify(todo)
    return jsonify({"error": "To-do not found"}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
