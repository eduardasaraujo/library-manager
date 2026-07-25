from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    author = db.Column(db.String(100), nullable=False)

    isbn = db.Column(db.String(20), unique=True, nullable=False)

    category = db.Column(db.String(50), nullable=False)

    status = db.Column(db.String(20), default="Disponível")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)