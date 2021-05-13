import flask as fs
from flask import request
from test import *


app = fs.Flask(__name__, template_folder='templates')


@app.route('/')
def login():
    return fs.render_template('login.html')


@app.route('/<username>/menu')
def menu(username=None):
    return fs.render_template('menu.html', username=username)


@app.route('/game/<position>', methods=['POST', 'GET'])
def game(position=None):
    extra = None
    if position == "0":
        extra = "This is the start of the game."
    elif position == "1" or position == "2" or position == "3":
        extra = description(position)
    else:
        extra = input_fields()
    return fs.render_template('game.html', extra=extra, position=position)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)
