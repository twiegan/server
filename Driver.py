import json

from CharacterTypes import Player, NonPlayer
from Map import Map, Tile


def create_player(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, inventory):
    return Player(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, inventory)


def create_nonplayer(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, weapon):
    return NonPlayer(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, weapon)


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
    return json.dumps(player.inventory)


def get_map(map):
    return map.toJson()


def move(direction, player, map):
    return json.dumps([0, 1, 2])


def get_stats(player):
    stats = ["hp: {hp}\n".format(hp=player.hp),
             "dge: {dge}\n".format(dge=player.dge)]
    return json.dumps(stats)
