import json
from f_drivers.DriverCreate import *


def get_move_json(direction, player, map):
    old_tile = map.map[player.ypos][player.xpos]
    new_tile = ErrorTile()
    if direction == 'north':
        if player.ypos - 1 < 0:
            return json.dumps(new_tile.toJson())
        new_tile = map.map[player.ypos - 1][player.xpos]
        player.ypos -= 1
    elif direction == 'east':
        if player.xpos + 1 == map.cols:
            return json.dumps(new_tile.toJson())
        new_tile = map.map[player.ypos][player.xpos + 1]
        player.xpos += 1
    elif direction == 'south':
        if player.ypos + 1 == map.rows:
            return json.dumps(new_tile.toJson())
        new_tile = map.map[player.ypos + 1][player.xpos]
        player.ypos += 1
    elif direction == 'west':
        if player.xpos - 1 < 0:
            return json.dumps(new_tile.toJson())
        new_tile = map.map[player.ypos][player.xpos - 1]
        player.xpos -= 1
    old_tile.hasPlayer = False
    old_tile.disc = True
    new_tile.hasPlayer = True
    if new_tile.location is None:
        return json.dumps({'description': new_tile.description})
    else:
        return json.dumps({'description': new_tile.location.description})
