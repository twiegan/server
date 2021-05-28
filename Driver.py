import json

from CharacterTypes import Player, NonPlayer
from Item import Weapon, Armour, WTypes, ATypes
from Map import Map, Tile


def create_player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory):
    return Player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory)


def create_nonplayer(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
    return NonPlayer(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)


def create_weapon(name, value, durability, type, damage):
    return Weapon(name, value, durability, type, damage)


def create_armour(name, value, durability, type, defense):
    return Armour(name, value, durability, type, defense)


def create_map(rows, cols, disc_char, undisc_char):
    all_rows = []
    for i in range(rows):
        curr_row = []
        for j in range(cols):
            tile = create_tile(i, j, disc_char, undisc_char)
            curr_row.append(tile)
        all_rows.append(curr_row)
    return Map(rows, cols, all_rows)


def create_tile(row, col, disc_char, undisc_char):
    return Tile(row, col, disc_char, undisc_char)


def get_inventory(player):
    to_dump = []
    for item in player.inventory:
        to_dump.append(item.toJson())
    return json.dumps(to_dump, indent=4)


def get_map(map):
    return map.toJson()


def move(direction, player, map):
    return json.dumps([0, 1, 2])


def get_stats(player):
    stats = ["hp: {hp}\n".format(hp=player.hp),
             "dge: {dge}\n".format(dge=player.dge)]
    return json.dumps(stats)
