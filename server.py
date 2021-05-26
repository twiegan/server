import flask as fs
from flask import request
from test import *
from game import *
import Driver


app = fs.Flask(__name__, template_folder='templates')


@app.route('/')
def login():
    # return fs.render_template('test.html')
    # return fs.render_template('login.html')
    return fs.render_template('game.html', username='user', extra="This is the start of the game.", position=0)


@app.route('/<username>/menu')
def menu(username=None):
    return fs.render_template('menu.html', username=username)


@app.route('/<username>/game', methods=['POST', 'GET'])
def game(username=None, position=None):
    extra = None
    if position == "0":
        extra = "This is the start of the game.\n"
    elif position == "1" or position == "2" or position == "3":
        extra = description(position)
    else:
        p1 = Driver.create_player("Thomas", 10, 11, 12, 1, 2, 3, 4, 5, ["Sword", "Knife", "Dagger"])
        extra = p1.inventory
    return fs.render_template('game.html', username=username, extra=extra)


@app.route('/<username>/game/<position>/inventory')
def game_inventory(username=None, position=None):
    return fs.render_template('inventory.html', username=username, position=position)


@app.route('/<username>/game/<position>/map')
def game_map(username=None, position=None):
    return fs.render_template('map.html', username=username, position=position, player_map=generate_map())


@app.route('/<username>/game/<position>/stats')
def game_stats(username=None, position=None):
    return fs.render_template('stats.html', username=username, position=position)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
