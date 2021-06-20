import json
from f_drivers.DriverCreate import *


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


def drop_item(player, slot):
    return {'dropped': player.inventory.pop(slot).toJson()}


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


def sell_item(player, map, slot):
    curr_tile = map.map[player.ypos][player.xpos]
    item = player.inventory.pop(slot)
    player.money += item.value
    curr_tile.location.market.wares.append(item)
    return {'sold': item.toJson()}