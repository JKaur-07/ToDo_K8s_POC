from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

todos = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/config")
def config():
    return {
        "app_name": os.getenv("APP_NAME", "Todo SPA"),
        "environment": os.getenv("ENVIRONMENT", "dev")
    }

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.json
    todo = {
        "id": len(todos) + 1,
        "task": data.get("task")
    }
    todos.append(todo)
    return jsonify(todo), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)