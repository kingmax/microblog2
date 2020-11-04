from theApp import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    # return 'Hello, World!'
    user = {'username': 'Jason'}
    return render_template('index.html', title='Home', user=user)