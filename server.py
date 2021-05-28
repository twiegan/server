import flask as fs
from flask import request
from Driver import *

player = create_player(name="Basic Bitch",
                       hp=0,
                       dge=0,
                       spd=0,
                       phy_res=0,
                       fire_res=0,
                       frost_res=0,
                       inventory=[create_weapon("TestKnife", 500, 1, WTypes['Knife'], 1),
                                  create_weapon("TestBow", 1000, 2, WTypes['Bow'], 2),
                                  create_weapon("TestHelm", 1500, 3, ATypes['Helm'], 3)])
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
    # inventory_json = json.dumps([WType.KNIFE, WType.SWORD, WType.BOW])
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
    print(request.get_json())
    move_json = move(request.get_json()['direction'], player, curr_map)
    return move_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
