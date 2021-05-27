import flask as fs
from flask import request
from Driver import *


player = create_player("Basic Bitch", 0, 0, 0, 0, 0, 0, 0, 0, [])
curr_map = create_map(rows=3, cols=3, disc_char="o", undisc_char="X")
curr_map.print_object()

app = fs.Flask(__name__, template_folder='templates')


@app.route('/')
def game():
    return fs.render_template('game.html')


@app.route('/inventory', methods=['POST'])
def game_inventory():
    print(request.get_json())
    inventory_json = get_inventory(player)
    return inventory_json


@app.route('/map', methods=['POST'])
def game_map():
    print(request.get_json())
    map_json = get_map(curr_map)
    return map_json


@app.route('/stats', methods=['POST'])
def game_stats():
    print(request.get_json())
    stats_json = get_stats(player)
    return stats_json


@app.route('/move', methods=['POST'])
def game_move():
    response = request.get_json()
    print(response['direction'])
    move_json = move(response['direction'], player, curr_map)
    return move_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
