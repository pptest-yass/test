from flask import Flask, blueprints
from dotenv import load_dotenv
import os 
from .views.main import main
from .views.auth import auth
from flask_migrate import Migrate
from .models import db


load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'project.db')
    
    # database related configuration
    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
