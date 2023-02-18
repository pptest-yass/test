from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AuthenticationForm(FlaskForm):
    username = StringField('username')
    password = StringField('password')

class PostCreationForm(FlaskForm):
    title = StringField('title')

