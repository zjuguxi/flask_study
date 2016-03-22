#! python3
# -*- coding:utf-8 -*-

from flask import Flask, request, redirect, make_response,abort
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is {}</p>'.format(user_agent)

# @app.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400

# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response

@app.route('/')
def index():
    return redirect('http://www.baidu.com')

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s!</h1>' % name

# if __name__ == '__main__':
#     app.run(debug = True)

if __name__ == '__main__':
    manager.run()