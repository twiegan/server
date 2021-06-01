MAX_CURR_TEAM = 3


class Character:
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res):
        self.ns_abilities = []
        self.name = name
        self.hp = hp
        self.dge = dge
        self.spd = spd
        self.phyRes = phy_res
        self.fireRes = fire_res
        self.frostRes = frost_res

    def print_object(self):
        print(
            'Character Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phyRes: {self.phyRes} fireRes: {self.fireRes}, frostRes: {self.frostRes}\n'
            f'abilities: {self.ns_abilities}\n'
        )


class Player(Character):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, inventory):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res)
        self.ns_inventory = inventory
        self.ns_team = []

    def print_object(self):
        print(
            'Player Object:\n'
            f'Name: {self.name}, HP: {self.hp}, dge: {self.dge}, spd: {self.spd}\n'
            f'phyRes: {self.phyRes} fireRes: {self.fireRes}, frostRes: {self.frostRes}\n'
            f'abilities: {self.ns_abilities}\n'
            f'inventory: {self.ns_inventory}\n'
            f'team: {self.ns_team}\n'
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
            f'abilities: {self.ns_abilities}\n'
            f'weapon: {self.weapon}\n'
            f'loot: {self.loot}\n'
        )
