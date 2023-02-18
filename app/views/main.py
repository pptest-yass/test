from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from app.forms import PostCreationForm
from app.models import Post, db
from flask_login import current_user, login_required


class AdminView(MethodView):
    decorators = [login_required]
    
    def get(self):
        return render_template('admin.html')

class Home(MethodView):
    decorators = [login_required]

    def get_context(self):
        form = PostCreationForm(request.form)
        posts = Post.query.filter_by(user_id=current_user.id)

        context = {
            "posts" : posts,
            "form" : form
        }

        return context

    def get(self):
        context = self.get_context()
        return render_template('home.html', **context)
    
    def post(self):
        context = self.get_context()
        if context['form'].validate_on_submit():
            post = Post(
                title = context['form'].title.data,
                user_id = current_user.id
            )
            db.session.add(post)
            db.session.commit()

        return render_template('home.html', **context)

class Detail(MethodView):
    decorators = [login_required]

    def get(self, id):
        form = PostCreationForm()
        post = Post.query.get_or_404(id)
        return render_template('detail.html', form=form, post=post)
    
    def post(self, id):
        form = PostCreationForm(request.form)
        if form.validate_on_submit():
            post = Post.query.get_or_404(id)
            post.title = form.title.data
            db.session.commit()
        return render_template('detail.html',form=form, post=post)

    def delete(self, id):
        post = Post.query.get(id)
        print("inside delete")
        print(post)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('home'))
