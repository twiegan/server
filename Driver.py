import json
import random

from Character import Player, NonPlayer
from Map import Map
from ListItem import *
from ListLocation import *
from ListTile import *


def create_player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos):
    return Player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos)


def create_nonplayer(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
    return NonPlayer(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)


def create_weapon(name, value, durability, damage, type):
    if type == 'Knife':
        return Knife(name, value, durability, damage)
    elif type == 'Sword':
        return Sword(name, value, durability, damage)
    elif type == 'Bow':
        return Bow(name, value, durability, damage)


def create_armour(name, value, durability, defense, type):
    if type == 'Helm':
        return Helm(name, value, durability, defense)
    elif type == 'Breastplate':
        return Breastplate(name, value, durability, defense)
    elif type == 'Gauntlets':
        return Gauntlets(name, value, durability, defense)
    elif type == 'Greaves':
        return Greaves(name, value, durability, defense)
    elif type == 'Boots':
        return Boots(name, value, durability, defense)


def create_map(rows, cols, player):
    all_rows = []
    for i in range(rows):
        curr_row = []
        for j in range(cols):
            tile = create_tile(xpos=j, ypos=i, location=None, weight=50, type='Desert')
            if j == 0 and i == 0:
                tile.location = Town()
            curr_row.append(tile)
        all_rows.append(curr_row)
    all_rows[player.ypos][player.xpos].hasPlayer = True
    return Map(rows, cols, all_rows)


def create_tile(xpos, ypos, location, weight, type):
    if type == 'Desert':
        return Desert(xpos, ypos, location, weight)


def get_inventory_json(player):
    inventory = {}
    for i, item in enumerate(player.inventory):
        inventory[i] = item.toJson()
    return json.dumps(inventory)


def get_map_json(map):
    return json.dumps(map.toJson())


def get_stats_json(player):
    return json.dumps(player.statsJson())


def get_combat_json(player, map):
    curr_tile = map.map[player.ypos][player.xpos]
    if random.randrange(100) < curr_tile.weight:
        return json.dumps({'text': "Combat Here"})
    else:
        return json.dumps({'text': "No Combat"})


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
