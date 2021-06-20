# General Constants
PLAYER_CHAR = "$"  # displayed character for the player
DEATH_CHAR = "_"
UNDISCOVERED_CHAR = "_"  # displayed character pre discovery
MAX_TEAM = 3
MIN_TEAM = 1
MAX_WEIGHT = 10


# Tile Constants
ENEMY_TILE = {  # tiles and their corresponding enemy possibilities
    'Desert': ['Bandit', 'Ogre'],
    'Grassland': ['Ogre', 'Goblin']
}
ENEMY_TILE_CUM_WEIGHTS = {  # chance of tiles' respective enemies /100
    'Desert': [50, 50],
    'Grassland': [50, 50]
}
DESERT_WEIGHT = 50  # chance of combat in desert /100
GRASSLAND_WEIGHT = 50  # chance of combat in grassland /100
