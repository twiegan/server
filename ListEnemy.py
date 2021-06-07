from Character import Enemy


class Bandit(Enemy):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot,
                         type="Bandit", enemy_char="B")


class Ogre(Enemy):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot,
                         type="Ogre", enemy_char="O")


class Goblin(Enemy):
    def __init__(self, name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(name, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot,
                         type="Goblin", enemy_char="G")
