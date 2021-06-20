import random
from f_drivers.DriverCreate import *

# global storage of the current combat for reference in combat functions
curr_combat = {}


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
