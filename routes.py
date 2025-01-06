from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from models import Todo, User
from extension import db


def init_routes(app):
    @app.route('/tasks', methods=['POST'])
    @jwt_required()
    def create_todo():
        data = request.get_json()
        new_todo = Todo(
            title=data['title'],
            description=data['description']
        )
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({"message": "Todo created successfully"}), 201

    @app.route('/tasks', methods=['GET'])
    @jwt_required()
    def get_todos():
        todos = Todo.query.all()

        for todo in todos:
            print(todo.id, todo.title, todo.status)
        return jsonify([todo.to_dict() for todo in todos])

    @app.route('/tasks/<int:id>', methods=['GET'])
    @jwt_required()
    def get_todo_by_id(id):
        todo = Todo.query.get_or_404(id)
        return jsonify(todo.to_dict())

    @app.route('/tasks/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_todo(id):
        todo = Todo.query.get_or_404(id)
        data = request.get_json()
        print(f"Incoming Data: {data}")  # Debugging input data
        todo.title = data.get('title', todo.title)
        todo.description = data.get('description', todo.description)
       
        todo.status = data.get('status', todo.status)
        print(f"Updated Todo: {todo.to_dict()}")  # Debugging updated object
        db.session.commit()
        return jsonify(todo.to_dict()), 200
        #return jsonify({"message": "Todo updated successfully"})


    @app.route('/tasks/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_todo(id):
        todo = Todo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Todo deleted successfully"})

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            access_token = create_access_token(identity=str(user.id))
            return jsonify({"access_token": access_token}), 200
        return jsonify({"msg": "Invalid credentials"}), 401

    @app.route('/')
    def home():
        return "Welcome to the To-Do API!"
