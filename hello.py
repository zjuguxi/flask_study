from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://www.baidu.com')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)