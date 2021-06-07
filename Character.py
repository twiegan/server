class Character:
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res):
        self.abilities = []
        self.name = name
        self.hp = hp
        self.dge = dge
        self.spd = spd
        self.phy_res = phy_res
        self.fire_res = fire_res
        self.frost_res = frost_res

    def print_object(self):
        print(
            'Character Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phy_res: {self.phy_res} fire_res: {self.fire_res}, frost_res: {self.frost_res}\n'
            f'abilities: {self.abilities}\n'
        )


class Player(Character):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, inventory, xpos, ypos):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res)
        self.inventory = inventory
        self.xpos = xpos
        self.ypos = ypos
        self.team = []

    def print_object(self):
        print(
            'Player Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phy_res: {self.phy_res} fire_res: {self.fire_res}, frost_res: {self.frost_res}\n'
            f'abilities: {self.abilities}\n'
            f'inventory: {self.inventory}\n'
            f'team: {self.team}\n'
        )

    def statsJson(self):
        return {'name': self.name, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd,
                'phy_res': self.phy_res, 'fire_res': self.fire_res, 'frost_res': self.frost_res}


class NonPlayer(Character):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res)
        self.weapon = weapon
        self.loot = loot

    def print_object(self):
        print(
            'NonPlayer Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phy_res: {self.phy_res} fire_res: {self.fire_res}, frost_res: {self.frost_res}\n'
            f'abilities: {self.abilities}\n'
            f'weapon: {self.weapon}\n'
            f'loot: {self.loot}\n'
        )


class Enemy(NonPlayer):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot, type, enemy_char):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot)
        self.type = type
        self.enemy_char = enemy_char

    def toJson(self):
        return {'name': self.name, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd, 'phy_res': self.phy_res,
                'fire_res': self.fire_res, 'frost_res': self.frost_res, 'weapon': self.weapon, 'loot': self.loot,
                'type': self.type, 'enemy_char': self.enemy_char}

