from f_core.Map import Map, Market
from f_lists.ListTile import *
from f_lists.ListLocation import *
from f_lists.ListEnemy import *
from f_core.Constants import *
from f_core.Character import Player
from f_lists.ListItem import *
from f_lists.ListAlly import *


def create_player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos, weapon):
    return Player(name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos, weapon)


def create_ally(type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
    if type == 'Thomas':
        return Thomas(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)
    if type == 'Joe':
        return Joe(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)


def create_enemy(type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
    if type == 'Bandit':
        return Bandit(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)
    elif type == 'Ogre':
        return Ogre(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)
    elif type == 'Goblin':
        return Goblin(hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)


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


def create_tile(xpos, ypos, location, weight, type):
    if type == 'Desert':
        return Desert(xpos, ypos, location, weight)
    elif type == 'Grassland':
        return Grassland(xpos, ypos, location, weight)


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
