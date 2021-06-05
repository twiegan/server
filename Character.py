MAX_CURR_TEAM = 3


class Character:
    def __init__(self, name, hp, dge, spd, phyRes, fireRes, frostRes):
        self.abilities = []
        self.name = name
        self.hp = hp
        self.dge = dge
        self.spd = spd
        self.phyRes = phyRes
        self.fireRes = fireRes
        self.frostRes = frostRes

    def print_object(self):
        print(
            'Character Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phyRes: {self.phyRes} fireRes: {self.fireRes}, frostRes: {self.frostRes}\n'
            f'abilities: {self.abilities}\n'
        )


class Player(Character):
    def __init__(self, name, hp, dge, spd, phyRes, fireRes, frostRes, inventory, xpos, ypos):
        super().__init__(name, hp, dge, spd, phyRes, fireRes, frostRes)
        self.inventory = inventory
        self.xpos = xpos
        self.ypos = ypos
        self.team = []

    def print_object(self):
        print(
            'Player Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phyRes: {self.phyRes} fireRes: {self.fireRes}, frostRes: {self.frostRes}\n'
            f'abilities: {self.abilities}\n'
            f'inventory: {self.inventory}\n'
            f'team: {self.team}\n'
        )

    def statsJson(self):
        return {'name': self.name, 'hp': self.hp, 'dge': self.dge, 'spd': self.spd,
                'phyRes': self.phyRes, 'fireRes': self.fireRes, 'frostRes': self.frostRes}


class NonPlayer(Character):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res)
        self.weapon = weapon
        self.loot = loot

    def print_object(self):
        print(
            'NonPlayer Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phyRes: {self.phyRes} fireRes: {self.fireRes}, frostRes: {self.frostRes}\n'
            f'abilities: {self.abilities}\n'
            f'weapon: {self.weapon}\n'
            f'loot: {self.loot}\n'
        )
