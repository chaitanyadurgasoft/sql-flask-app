# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    course = db.Column(db.String(150), nullable=True)
    date_joined = db.Column(db.Integer, nullable=True)  # Change to Integer as MySQL does not have a native year type
def __repr__(self):
        return f"Student(name='{self.name}', course='{self.course}', date_joined='{self.date_joined}')"
