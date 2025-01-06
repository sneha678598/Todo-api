from werkzeug.security import generate_password_hash, check_password_hash
from extension import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), nullable=False, default="Pending")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status  # Include status in the response
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # Password hashing
    def set_password(self, password):
        self.password = generate_password_hash(password)  # Hash the password

    # Password checking (compare hash)
    def check_password(self, password):
        return check_password_hash(self.password, password)  # Compare hashed password

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }
