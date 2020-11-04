from theApp import app
from flask import render_template


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
