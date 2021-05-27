import json

MAX_CURR_TEAM = 3


class Character:
    def __init__(self, name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res):
        self.abilities = []
        self.frostRes = frost_res
        self.fireRes = fire_res
        self.phyRes = phy_res
        self.mgkStr = mgk_str
        self.phyStr = phy_str
        self.spd = spd
        self.dge = dge
        self.hp = hp
        self.name = name

    def print_object(self):
        print(
            f'Name: {self.name}\n'
            f'HP: {self.hp}\n'
            f'dge: {self.dge}\n'
            f'spd: {self.spd}\n'
            f'phyStr: {self.phyStr}\n'
            f'mgkStr: {self.mgkStr}\n'
            f'phyRes: {self.phyRes}\n'
            f'fireRes: {self.fireRes}\n'
            f'frostRes: {self.frostRes}\n'
            f'abilities: {self.abilities}\n'
        )


class Player(Character):
    def __init__(self, name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, inventory):
        super().__init__(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res)
        self.inventory = inventory
        self.curr_team = []
        self.full_team = []

    def print_object(self):
        super().print_object()
        f'inventory: {self.inventory}\n'
        f'curr_team: {self.curr_team}\n'
        f'full_team: {self.full_team}\n'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class NonPlayer(Character):
    def __init__(self, name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, weapon):
        super().__init__(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res)
        self.weapon = weapon

    def print_object(self):
        super().print_object()
        f'weapon: {self.weapon}\n'
