class Character:
    def __init__(self, hp, dge, spd, phy_res, fire_res, frost_res):
        self.abilities = {}
        self.hp = hp
        self.dge = dge
        self.spd = spd
        self.phy_res = phy_res
        self.fire_res = fire_res
        self.frost_res = frost_res
        self.max_hp = hp
        self.isAlive = True

    def print_object(self):
        print(
            'Character Object:\n'
            f'HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phy_res: {self.phy_res} fire_res: {self.fire_res}, frost_res: {self.frost_res}\n'
            f'abilities: {self.abilities}\n'
        )


class Player(Character):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos, weapon):
        super().__init__(hp, dge, spd, phy_res, fire_res, frost_res)
        self.name = name
        self.inventory = inventory
        self.xpos = xpos
        self.ypos = ypos
        self.weapon = weapon
        self.team = {}
        self.weight = 0
        self.money = 0
        self.armour = {'Head': None,
                       'Chest': None,
                       'Hands': None,
                       'Legs': None,
                       'Feet': None}
        self.quests = {}

    def print_object(self):
        print(
            'Player Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phy_res: {self.phy_res} fire_res: {self.fire_res}, frost_res: {self.frost_res}\n'
            f'inventory: {self.inventory}\n'
            f'team: {self.team}\n'
        )

    def toJson(self):
        return {'name': self.name, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd,
                'phy_res': self.phy_res, 'fire_res': self.fire_res, 'frost_res': self.frost_res}

    def toCombatJson(self):
        return {'isAlive': self.isAlive}

    def toStatsJson(self):
        return {'name': self.name, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd,
                'phy_res': self.phy_res, 'fire_res': self.fire_res, 'frost_res': self.frost_res}


class NonPlayer(Character):
    def __init__(self, type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(hp, dge, spd, phy_res, fire_res, frost_res)
        self.type = type
        self.weapon = weapon
        self.loot = loot

    def print_object(self):
        print(
            'NonPlayer Object:\n'
            f'type: {self.type}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phy_res: {self.phy_res} fire_res: {self.fire_res}, frost_res: {self.frost_res}\n'
            f'abilities: {self.abilities}\n'
            f'weapon: {self.weapon}\n'
            f'loot: {self.loot}\n'
        )


class Enemy(NonPlayer):
    def __init__(self, type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot, enemy_char):
        super().__init__(type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)
        self.enemy_char = enemy_char

    def toJson(self):
        return {'type': self.type, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd, 'phy_res': self.phy_res,
                'fire_res': self.fire_res, 'frost_res': self.frost_res, 'weapon': self.weapon, 'loot': self.loot,
                'enemy_char': self.enemy_char}

    def toCombatJson(self):
        return {'type': self.type, 'enemy_char': self.enemy_char, 'isAlive': self.isAlive}

    def toStatsJson(self):
        return {'type': self.type, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd, 'phy_res': self.phy_res,
                'fire_res': self.fire_res, 'frost_res': self.frost_res, 'isAlive': self.isAlive}


class Ally(NonPlayer):
    def __init__(self, type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot, ally_char):
        super().__init__(type, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)
        self.ally_char = ally_char

    def toJson(self):
        return {'type': self.type, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd, 'phy_res': self.phy_res,
                'fire_res': self.fire_res, 'frost_res': self.frost_res, 'weapon': self.weapon, 'loot': self.loot,
                'ally_char': self.ally_char}

    def toCombatJson(self):
        return {'type': self.type, 'ally_char': self.ally_char, 'isAlive': self.isAlive}

    def toStatsJson(self):
        return {'type': self.type, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd, 'phy_res': self.phy_res,
                'fire_res': self.fire_res, 'frost_res': self.frost_res, 'isAlive': self.isAlive}
