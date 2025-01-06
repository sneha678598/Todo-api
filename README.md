# Todo API

This project implements a simple Todo API with CRUD (Create, Read, Update, Delete) operations using Flask and SQLite. The API allows users to manage tasks such as creating new tasks, viewing tasks, updating task details, and deleting tasks.

## Features

- **Create Task**: Add new tasks with a title and description.
- **Read Tasks**: Fetch all tasks or a specific task by ID.
- **Update Task**: Update task details by task ID.
- **Delete Task**: Remove a task by task ID.

## Technologies Used

- **Flask**: Web framework for building the API.
- **SQLite**: Database for storing task data.
- **JWT (JSON Web Token)**: Authentication mechanism to secure API endpoints.

## Setup Instructions

### Prerequisites

1. Python 3.x
2. SQLite (for local database)

### Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd todo_api

2. Create and activate a virtual environment:

  ```bash
  python -m venv venv
  source venv/bin/activate  # For Linux/MacOS
  venv\Scripts\activate     # For Windows

3. Install the required dependencies:

  ```bash
  pip install -r requirements.txt

4. Set up the SQLite database by running the following command to create the necessary tables:

  ```bash
  python create_db.py

5. Run the application:

  ```bash
  python app.py


### API Endpoints

## Authentication
1. Login:

  POST /login
  Request:
  json
  {
    "username": "your-username",
    "password": "your-password"
  }
Response: Returns a JWT token for authentication.
Example:
  curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "your-username", "password": "your-password"}'

2. Task Management
   Create Task:

  POST /tasks
  Headers: Authorization: Bearer <JWT_TOKEN>

  Request:
  json
  {
    "title": "Task Title",
    "description": "Task description"
  }
  Response: Confirmation message for task creation.
  Example:
  curl -X POST http://localhost:5000/tasks -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/json" -d '{"title": "New Task", "description": "Task description"}'

3. Get All Tasks:

  GET /tasks
  Headers: Authorization: Bearer <JWT_TOKEN>
  Response: Returns a list of all tasks.
  Example:
  curl -X GET http://localhost:5000/tasks -H "Authorization: Bearer <JWT_TOKEN>"

4. Get Task by ID:

  GET /tasks/{id}
  Headers: Authorization: Bearer <JWT_TOKEN>
  Response: Returns the task details for the given ID.
  Example:

  curl -X GET http://localhost:5000/tasks/1 -H "Authorization: Bearer <JWT_TOKEN>"

5. Update Task:

  PUT /tasks/{id}
  Headers: Authorization: Bearer <JWT_TOKEN>
  Request:
  json
  {
    "title": "Updated Task Title",
    "description": "Updated task description"
  }
  Response: Confirmation message for task update.
  Example:
  curl -X PUT http://localhost:5000/tasks/1 -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/json" -d '{"title": "Updated Task", "description": "Updated task description"}'

6. Delete Task:

  DELETE /tasks/{id}
  Headers: Authorization: Bearer <JWT_TOKEN>
  Response: Confirmation message for task deletion.
  Example:
  curl -X DELETE http://localhost:5000/tasks/1 -H "Authorization: Bearer <JWT_TOKEN>"

### Database Schema
  The tasks table in the SQLite database has the following columns:

  id: Integer (Primary Key, Auto-increment)
  title: Text (Task title)
  description: Text (Task description)

