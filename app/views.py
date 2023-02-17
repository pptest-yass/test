from flask import Blueprint

views = Blueprint('views', __name__, url_prefix='/')

@views.route('/')
def hello():
    return '<h1>hello world</h1>'

