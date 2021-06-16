import flask as fs
from flask import request
from Driver import *

player = create_player(name="Test",
                       hp=25,
                       dge=10,
                       spd=10,
                       phy_res=10,
                       fire_res=10,
                       frost_res=10,
                       inventory=[create_weapon("TestKnife", 500, 1, 1, type='Knife'),
                                  create_weapon("TestBow", 1000, 2, 2, type='Bow'),
                                  create_armour("TestHelm", 1500, 3, 3, type='Helm'),
                                  create_armour("test4", 1500, 3, 3, type='Gauntlets'),
                                  create_armour("test50000", 15000, 3, 3, type='Breastplate')],
                       xpos=2,
                       ypos=1,
                       weapon=create_weapon("TestW", 500, 2, 2, type='Sword'))
curr_map = create_map(rows=17, cols=25, player=player)


app = fs.Flask(__name__, template_folder='templates')


@app.route('/')
def game():
    return fs.render_template('game.html')


@app.route('/info', methods=['POST'])
def game_info():
    print(request.get_json())
    info_json = None
    if request.get_json()['info'] == 'info/equipment':
        info_json = get_equipment_json(player)
    elif request.get_json()['info'] == 'info/inventory':
        info_json = get_inventory_json(player)
    elif request.get_json()['info'] == 'info/map':
        info_json = get_map_json(curr_map)
    elif request.get_json()['info'] == 'info/stats':
        info_json = get_stats_json(player)
    elif request.get_json()['info'] == 'info/drop':
        info_json = drop_item(player, request.get_json()['slot'])
    elif request.get_json()['info'] == 'info/equip':
        info_json = equip_item(player, request.get_json()['slot'])
    return info_json


@app.route('/combat', methods=['POST'])
def game_combat():
    print(request.get_json())
    combat_json = None
    if request.get_json()['info'] == 'combat/initiate':
        combat_json = initiate_combat(player, curr_map)
    elif request.get_json()['info'] == 'combat/show':
        combat_json = show_combat()
    elif request.get_json()['info'] == 'combat/calculate':
        combat_json = calculate_combat(request.get_json()['target'])
    elif request.get_json()['info'] == 'combat/showAllyStats':
        combat_json = show_ally_stats()
    elif request.get_json()['info'] == 'combat/showEnemyStats':
        combat_json = show_enemy_stats()
    return combat_json


@app.route('/location', methods=['POST'])
def game_location():
    print(request.get_json())
    location_json = None
    if request.get_json()['info'] == 'location/show':
        location_json = get_location_json(player, curr_map)
    elif request.get_json()['info'] == 'location/selectOption':
        location_json = get_location_json(player, curr_map)
    return location_json


@app.route('/move', methods=['POST'])
def game_move():
    print(request.get_json())
    move_json = get_move_json(request.get_json()['direction'], player, curr_map)
    return move_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
