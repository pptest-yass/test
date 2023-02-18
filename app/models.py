from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref='user')
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class Post(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String)
    created_on = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Role(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String)
    users = db.relationship('User', backref='role')
