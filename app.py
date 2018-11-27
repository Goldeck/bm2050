
from flask import (
    Flask, render_template, redirect, request, url_for, session
)

from models import model
from models.account import Account


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/test')
def hello_test():
    return 'Hello, TEST!'

@app.route('/template')
def templates():
    return render_template('sample.html', title='template test')

@app.route('/account')
def account():
    a = Account()
    return repr(a)

if __name__ == '__main__':
    app.run()
