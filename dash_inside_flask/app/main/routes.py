from app.main import bp
from flask import render_template
from flask_login import login_required

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }]
    return render_template('index.html', title='Home', posts=posts)

