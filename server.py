import flask as fs
from flask import request
import Driver


player = Driver.create_player("Basic Bitch", 0, 0, 0, 0, 0, 0, 0, 0, [])
curr_map = [["@ ", "@ ", "@ ", "@"],
            ["@ ", "@ ", "@ ", "@"],
            ["@ ", "@ ", "@ ", "@"],
            ["@ ", "@ ", "@ ", "@"]]

app = fs.Flask(__name__, template_folder='templates')


@app.route('/')
def game():
    return fs.render_template('game.html')


@app.route('/inventory', methods=['POST'])
def game_inventory():
    print(request.get_json())
    inventory_json = Driver.get_inventory(player)
    player.inventory = ["Sword", "Knife"]
    return inventory_json


@app.route('/map', methods=['POST'])
def game_map():
    print(request.get_json())
    map_json = Driver.get_map(curr_map)
    return map_json


@app.route('/stats', methods=['POST'])
def game_stats():
    print(request.get_json())
    stats_json = Driver.get_stats(player)
    return stats_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
