import json
import random

from Character import Player
from Map import Map
from ListItem import *
from ListLocation import *
from ListTile import *
from ListEnemy import *
from ListAlly import *
from Constants import *


def create_player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos):
    return Player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos)


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


def create_enemy(type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
    if type == 'Bandit':
        return Bandit(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)
    elif type == 'Ogre':
        return Ogre(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)
    elif type == 'Goblin':
        return Goblin(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)


def create_ally(type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
    if type == 'Thomas':
        return Thomas(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)


def create_map(rows, cols, player):
    all_rows = []
    for i in range(rows):
        curr_row = []
        for j in range(cols):
            if j < cols / 2:
                tile = create_tile(xpos=j, ypos=i, location=None, weight=GRASSLAND_WEIGHT, type='Grassland')
            else:
                tile = create_tile(xpos=j, ypos=i, location=None, weight=DESERT_WEIGHT, type='Desert')
            if j == 0 and i == 0:
                tile.location = Town()
            curr_row.append(tile)
        all_rows.append(curr_row)
    all_rows[player.ypos][player.xpos].hasPlayer = True
    return Map(rows, cols, all_rows)


def create_tile(xpos, ypos, location, weight, type):
    if type == 'Desert':
        return Desert(xpos, ypos, location, weight)
    elif type == 'Grassland':
        return Grassland(xpos, ypos, location, weight)


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
    combat_json = {'combat': False}
    if curr_tile.location is None:
        if random.randrange(100) < curr_tile.weight:
            # basic info
            combat_json['combat'] = True
            combat_json['player_char'] = PLAYER_CHAR

            # player
            combat_json['player'] = player.toJson()

            # enemies
            possible_enemies = ENEMY_TILE[curr_tile.type]
            enemy_weights = ENEMY_TILE_CUM_WEIGHTS[curr_tile.type]
            num_enemies = random.randint(MIN_TEAM, MAX_TEAM)
            combat_json['num_enemies'] = num_enemies
            enemies = {}
            for i in range(num_enemies):
                curr_enemy_type = random.choices(possible_enemies, enemy_weights, k=1)
                enemies[f'enemy{i}'] = create_enemy(curr_enemy_type[0], 1, 1, 1, 1, 1, 1, create_weapon("testWeapon", 1, 1, 1, 'Knife').toJson(), create_weapon("testLoot", 1, 1, 1, 'Sword').toJson()).toJson()
            combat_json['enemies'] = enemies

            # allies
            combat_json['allies'] = {f'ally0': create_ally('Thomas', 10, 10, 10, 10, 10, 10, create_weapon("testWeapon", 1, 1, 1, 'Knife').toJson(), create_weapon("testLoot", 1, 1, 1, 'Sword').toJson()).toJson()}

    return combat_json


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
