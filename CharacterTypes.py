MAX_CURR_TEAM = 3


class Character:
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res):
        self.abilities = []
        self.frostRes = frost_res
        self.fireRes = fire_res
        self.phyRes = phy_res
        self.spd = spd
        self.dge = dge
        self.hp = hp
        self.name = name

    def print_object(self):
        print(
            'Character Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phyRes: {self.phyRes} fireRes: {self.fireRes}, frostRes: {self.frostRes}\n'
            f'abilities: {self.abilities}\n'
        )


class Player(Character):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, inventory):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res)
        self.inventory = inventory
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
