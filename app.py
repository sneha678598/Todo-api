from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from datetime import timedelta

from extension import db, jwt, migrate  # Import db and extensions
from models import Todo, User  # Import models for initialization
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    # App configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
    
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Set token expiry to 1 hour


    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Import and register routes
    from routes import init_routes
    init_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()

    # App context mein user create karne ka code
    with app.app_context():
        db.create_all()
        existing_user = User.query.filter_by(username="Sneha").first()  # Username should be "Sneha"
        if not existing_user:
            new_user = User(username="Sneha")
            new_user.set_password("mypassword123")  # Set password with hashing
            db.session.add(new_user)
            db.session.commit()
            print("User created successfully!")
        else:
            print("User already exists!")


        new_todo = Todo(title="Sample Task", description="This is a test task.")
        db.session.add(new_todo)
        db.session.commit()
        print("Sample task added!")

    app.run(debug=True)



#
# # (venv) C:\Users\acer\todo_api>curl -X POST http://127.0.0.1:5000/tasks -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNTgwNjI2NiwianRpIjoiMzEzYTYzYmQtNmQ5YS00MDI0LWEyYzctMTYzMGIxMWU1YjUwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjIiLCJuYmYiOjE3MzU4MDYyNjYsImNzcmYiOiI0ODdkOTIyOC1jYTY1LTRkOTMtYWU1Ny05OGMwNDdhY2FjNjAiLCJleHAiOjE3MzU4MDk4NjZ9.34Kpxiy-dNjEPNBy7YY0kxyDD2Np7w1CzNPS6rl57_o" -H "Content-Type: application/json" -d "{\"title\": \"New Task\"
# , \"description\": \"This is a sample task description.\"}
# {