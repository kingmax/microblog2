from theApp import app
from flask import render_template
from .forms import LoginForm
from flask import flash, redirect


@app.route('/')
@app.route('/index')
def index():
    # return 'Hello, World!'
    user = {'username': 'Jason'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in China!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, '
              f'remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
