import json

from CharacterTypes import Player, NonPlayer


def create_player(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, inventory):
    return Player(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, inventory)


def create_nonplayer(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, weapon):
    return NonPlayer(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, weapon)


def get_inventory(player):
    return json.dumps(player.inventory)


def get_map(map):
    return json.dumps(map)


def get_stats(player):
    stats = ["hp: {hp}\n".format(hp=player.hp),
             "dge: {dge}\n".format(dge=player.dge)]
    return json.dumps(stats)
