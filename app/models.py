from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String)

class Admin(User):
    pass

class Client(User):
    pass

class Article(db.Model):
    id = db.Column(db.Integer , primary_key=True)

class History(db.Model):
    id = db.Column(db.Integer , primary_key=True)
