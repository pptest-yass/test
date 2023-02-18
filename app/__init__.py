from flask import Flask
import os 
from .views.main import Home, Detail, AdminView
from .views.auth import login_manager, Register, Login
from flask_migrate import Migrate
from .models import db


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dfsqf"
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'project.db')
    
    # database related configuration
    db.init_app(app)
    Migrate(app, db)

    # flask login
    login_manager.init_app(app)

    # routes
    app.add_url_rule('/register', view_func=Register.as_view('register'))
    app.add_url_rule('/login', view_func=Login.as_view('login'))
    app.add_url_rule('/home', view_func=Home.as_view('home'))
    app.add_url_rule('/detail/<int:id>', view_func=Detail.as_view('detail'), methods=['GET', 'POST'])
    app.add_url_rule('/admin', view_func=AdminView.as_view('admin'))

    return app
