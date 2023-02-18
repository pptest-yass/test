from functools import wraps
from flask import g, request, redirect, url_for, flash
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("admin decorator")
        print(current_user.role.name)
        if current_user.role.name != "admin":
            flash("you need to be an admin to access this view")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
