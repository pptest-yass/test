from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask.views import MethodView
from flask_login import LoginManager, login_user
from app.models import User, db
from app.forms import AuthenticationForm
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
bcrypt = Bcrypt()
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Register(MethodView):
    def get(self):
        form = AuthenticationForm()
        return render_template('register.html', form=form)
    
    def post(self):
        form = AuthenticationForm(request.form)
        if form.validate_on_submit():
            print(form.data)
            user = User(
                username = form.username.data,
                password = form.password.data
            )
            print(user)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('login'))

class Login(MethodView):
    def get(self):
        form = AuthenticationForm()
        return render_template('register.html', form=form)
    
    def post(self):
        form = AuthenticationForm(request.form)
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                login_user(user)
                return redirect(url_for('home'))
            else:
                print('no such user')
                return render_template('register.html', form=form)