import json
import random

from Character import Player
from Map import Map, Market
from ListItem import *
from ListLocation import *
from ListTile import *
from ListEnemy import *
from ListAlly import *
from Constants import *

# global storage of the current combat for reference in combat functions
curr_combat = {}


def create_player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos, weapon):
    return Player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos, weapon)


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
    if type == 'Joe':
        return Joe(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)


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
                tile.location = Town(market=Market(wares=[create_weapon("Market1", 250, 10, 10, "Bow"),
                                                          create_weapon("Market2", 750, 4, 4, "Sword"),
                                                          create_armour("Market3", 500, 6, 6, "Boots")]))
            if j == 0 and i == 1:
                tile.location = City()
            curr_row.append(tile)
        all_rows.append(curr_row)
    all_rows[player.ypos][player.xpos].hasPlayer = True
    return Map(rows, cols, all_rows)


def create_tile(xpos, ypos, location, weight, type):
    if type == 'Desert':
        return Desert(xpos, ypos, location, weight)
    elif type == 'Grassland':
        return Grassland(xpos, ypos, location, weight)


def get_equipment_json(player):
    to_send = {'weapon': player.weapon.toJson(),
               'armour': {}}
    for i, item in enumerate(player.armour):
        if player.armour[item] is not None:
            to_send['armour'][item] = player.armour[item].toJson()
        else:
            to_send['armour'][item] = None
    return to_send


def get_inventory_json(player):
    to_send = {'player': {'name': player.name,
                          'weight': player.weight,
                          'money': player.money,
                          'max_weight': MAX_WEIGHT},
               'inventory': {}}
    for i, item in enumerate(player.inventory):
        to_send['inventory'][i] = item.toJson()
    return json.dumps(to_send)


def get_map_json(map):
    return json.dumps(map.toJson())


def get_stats_json(player):
    return json.dumps(player.toStatsJson())


def show_combat():
    # allies -> json
    allies = {}
    for i in curr_combat['allies']:
        allies[i] = curr_combat['allies'][i].toCombatJson()

    # enemies -> json
    enemies = {}
    for i in curr_combat['enemies']:
        enemies[i] = curr_combat['enemies'][i].toCombatJson()

    return {
        'death_char': DEATH_CHAR,
        'player_char': curr_combat['player_char'],
        'allies': allies,
        'player': curr_combat['player'].toCombatJson(),
        'enemies': enemies
    }


def initiate_combat(player, map):
    curr_tile = map.map[player.ypos][player.xpos]
    if curr_tile.location is None:
        if random.randrange(100) < curr_tile.weight:  # determine if a combat should occur
            # basic info
            curr_combat['player_char'] = PLAYER_CHAR
            curr_combat['curr_attacker'] = 0

            # player
            curr_combat['player'] = player

            # enemies
            possible_enemies = ENEMY_TILE[curr_tile.type]
            enemy_weights = ENEMY_TILE_CUM_WEIGHTS[curr_tile.type]
            num_enemies = random.randint(MIN_TEAM, MAX_TEAM)
            curr_combat['num_enemies'] = num_enemies
            enemies = {}
            """
            for i in range(num_enemies):
                curr_enemy_type = random.choices(possible_enemies, enemy_weights, k=1)
                enemies[f'enemy{i}'] = create_enemy(curr_enemy_type[0], 1, 1, 1, 1, 1, 1, create_weapon("testWeapon", 1, 1, 1, 'Knife'), create_weapon("testLoot", 1, 1, 1, 'Sword'))
            curr_combat['enemies'] = enemies
            """
            curr_combat['enemies'] = {
                'enemy0': create_enemy('Bandit', 1, 3, 3, 3, 3, 3, create_weapon("testWeapon", 1, 1, 1, 'Knife'),
                                       create_weapon("testLoot", 1, 1, 1, 'Sword')),
                'enemy1': create_enemy('Ogre', 1, 3, 3, 3, 3, 3, create_weapon("testWeapon", 1, 1, 1, 'Knife'),
                                       create_weapon("testLoot", 1, 1, 1, 'Sword')),
                'enemy2': create_enemy('Goblin', 1, 3, 3, 3, 3, 3, create_weapon("testWeapon", 1, 1, 1, 'Knife'),
                                       create_weapon("testLoot", 1, 1, 1, 'Sword'))}

            # allies
            curr_combat['num_allies'] = 2
            curr_combat['allies'] = {
                'ally0': create_ally('Thomas', 10, 10, 10, 10, 10, 10, create_weapon("testWeapon", 1, 1, 1, 'Knife'),
                                     create_weapon("testLoot", 1, 1, 1, 'Sword')),
                'ally1': create_ally('Joe', 10, 10, 10, 10, 10, 10, create_weapon("testWeapon", 1, 1, 1, 'Knife'),
                                     create_weapon("testLoot", 1, 1, 1, 'Sword'))}
            return {'initiated': True}
    return {'initiated': False}


def calculate_combat(target_number):
    won = False
    if target_number == 4:
        target_name = 'enemy0'
    elif target_number == 5:
        target_name = 'enemy1'
    else:
        target_name = 'enemy2'

    for i in range(2):
        attacker = None
        if curr_combat['curr_attacker'] == 0:
            if 'player' in curr_combat:
                attacker = curr_combat['player']
            else:
                curr_combat['curr_attacker'] += 1
        if curr_combat['curr_attacker'] == 1:
            if 'enemy0' in curr_combat['enemies']:
                attacker = curr_combat['enemies']['enemy0']
            else:
                curr_combat['curr_attacker'] += 1
        if curr_combat['curr_attacker'] == 2:
            if 'ally0' in curr_combat['allies']:
                attacker = curr_combat['allies']['ally0']
            else:
                curr_combat['curr_attacker'] += 1
        if curr_combat['curr_attacker'] == 3:
            if 'enemy1' in curr_combat['enemies']:
                attacker = curr_combat['enemies']['enemy1']
            else:
                curr_combat['curr_attacker'] += 1
        if curr_combat['curr_attacker'] == 4:
            if 'ally1' in curr_combat['allies']:
                attacker = curr_combat['allies']['ally1']
            else:
                curr_combat['curr_attacker'] += 1
        if curr_combat['curr_attacker'] == 5:
            if 'enemy2' in curr_combat['enemies']:
                attacker = curr_combat['enemies']['enemy2']
            else:
                curr_combat['curr_attacker'] = 0

        if isinstance(attacker, Player) or isinstance(attacker, Ally):
            target = curr_combat['enemies'][target_name]
        else:
            target = curr_combat['player']
        target.hp -= attacker.weapon.damage
        if target.hp <= 0:
            if isinstance(attacker, Player) or isinstance(attacker, Ally):
                curr_combat['enemies'][target_name].isAlive = False
            else:
                curr_combat['player'].isAlive = False

        curr_combat['curr_attacker'] += 1
        if curr_combat['curr_attacker'] == 6:
            curr_combat['curr_attacker'] = 1
    if not curr_combat['enemies']['enemy0'].isAlive and not curr_combat['enemies']['enemy1'].isAlive and not \
            curr_combat['enemies']['enemy2'].isAlive:
        won = True
    return {'calculated': True, 'won': won}


def show_ally_stats():
    # allies -> json
    allies = {}
    for i in curr_combat['allies']:
        allies[i] = curr_combat['allies'][i].toStatsJson()
    return allies


def show_enemy_stats():
    # enemies -> json
    enemies = {}
    for i in curr_combat['enemies']:
        enemies[i] = curr_combat['enemies'][i].toStatsJson()
    return enemies


def get_location_json(player, map):
    curr_tile = map.map[player.ypos][player.xpos]
    location_json = {'location': False}
    if curr_tile.location is not None:
        location_json['location'] = True
        location_json['content'] = curr_tile.location.toJson()
    return location_json


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


def equip_item(player, slot):
    item = player.inventory.pop(slot)
    if isinstance(item, Weapon):
        if player.weapon is not None:
            temp = player.weapon
            player.inventory.append(temp)
        player.weapon = item
    elif isinstance(item, Armour):
        if player.armour[item.slot] is not None:
            temp = player.armour[item.slot]
            player.inventory.append(temp)
        player.armour[item.slot] = item
    return {'equipped': item.toJson()}


def drop_item(player, slot):
    return {'dropped': player.inventory.pop(slot).toJson()}


def sell_item(player, map, slot):
    curr_tile = map.map[player.ypos][player.xpos]
    item = player.inventory.pop(slot)
    player.money += item.value
    curr_tile.location.market.wares.append(item)
    return {'sold': item.toJson()}


def buy_item(player, map, slot):
    curr_tile = map.map[player.ypos][player.xpos]
    item = curr_tile.location.market.wares.pop(slot)
    player.money -= item.value
    player.inventory.append(item)
    return {'bought': item.toJson()}
