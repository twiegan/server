import flask as fs
from flask import request
from Driver import *

player = create_player(name="Test",
                       hp=0,
                       dge=0,
                       spd=0,
                       phy_res=0,
                       fire_res=0,
                       frost_res=0,
                       inventory=[create_weapon("TestKnife", 500, 1, WTypes['Knife'], 1),
                                  create_weapon("TestBow", 1000, 2, WTypes['Bow'], 2),
                                  create_armour("TestHelm", 1500, 3, ATypes['Helm'], 3),
                                  create_armour("test4", 1500, 3, ATypes['Gauntlets'], 3),
                                  create_armour("test50000", 15000, 3, ATypes['Breastplate'], 3)],
                       xpos=12,
                       ypos=8)
curr_map = create_map(rows=17, cols=25, disc_char="o", player=player, description="This is a test")


app = fs.Flask(__name__, template_folder='templates')


@app.route('/')
def game():
    return fs.render_template('game.html')


@app.route('/inventory', methods=['POST'])
def game_inventory():
    print(request.get_json())
    inventory_json = get_inventory_json(player)
    return inventory_json


@app.route('/map', methods=['POST'])
def game_map():
    print(request.get_json())
    map_json = get_map_json(curr_map)
    return map_json


@app.route('/stats', methods=['POST'])
def game_stats():
    print(request.get_json())
    stats_json = get_stats_json(player)
    return stats_json


@app.route('/move', methods=['POST'])
def game_move():
    print(request.get_json())
    move_json = get_move_json(request.get_json()['direction'], player, curr_map)
    return move_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
