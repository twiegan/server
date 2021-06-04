import json

from CharacterTypes import Player, NonPlayer
from Item import Weapon, Armour, WTypes, ATypes
from Map import Map, Tile


def create_player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos):
    return Player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos)


def create_nonplayer(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
    return NonPlayer(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)


def create_weapon(name, value, durability, type, damage):
    return Weapon(name, value, durability, type, damage)


def create_armour(name, value, durability, type, defense):
    return Armour(name, value, durability, type, defense)


def create_map(rows, cols, disc_char, player, description):
    all_rows = []
    for i in range(rows):
        curr_row = []
        for j in range(cols):
            tile = create_tile(j, i, disc_char, description)
            curr_row.append(tile)
        all_rows.append(curr_row)
    all_rows[player.ypos][player.xpos].hasPlayer = True
    return Map(rows, cols, all_rows)


def create_tile(row, col, disc_char, description):
    return Tile(row, col, disc_char, description)


def get_inventory_json(player):
    inventory = {}
    for i, item in enumerate(player.inventory):
        inventory[i] = item.toJson()
    return json.dumps(inventory)


def get_map_json(map):
    return map.toJson()


def get_stats_json(player):
    return json.dumps(player.statsJson())


def get_move_json(direction, player, map):
    old_tile = map.map[player.ypos][player.xpos]
    new_tile = Tile(-1, -1, "error", "error")
    if direction == 'north':
        if player.ypos - 1 < 0:
            return new_tile.toJson()
        new_tile = map.map[player.ypos - 1][player.xpos]
        player.ypos -= 1
    elif direction == 'east':
        if player.xpos + 1 == map.cols:
            return new_tile.toJson()
        new_tile = map.map[player.ypos][player.xpos + 1]
        player.xpos += 1
    elif direction == 'south':
        if player.ypos + 1 == map.rows:
            return new_tile.toJson()
        new_tile = map.map[player.ypos + 1][player.xpos]
        player.ypos += 1
    elif direction == 'west':
        if player.xpos - 1 < 0:
            return new_tile.toJson()
        new_tile = map.map[player.ypos][player.xpos - 1]
        player.xpos -= 1
    old_tile.hasPlayer = False
    old_tile.disc = True
    new_tile.hasPlayer = True
    return new_tile.toJson()


