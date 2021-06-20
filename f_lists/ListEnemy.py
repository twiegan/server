from f_core.Character import Enemy


class Bandit(Enemy):
    def __init__(self, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(type="Bandit", hp=hp, dge=dge, spd=spd, phy_res=phy_res, fire_res=fire_res,
                         frost_res=frost_res, weapon=weapon, loot=loot, enemy_char="B")


class Ogre(Enemy):
    def __init__(self, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(type="Ogre", hp=hp, dge=dge, spd=spd, phy_res=phy_res, fire_res=fire_res,
                         frost_res=frost_res, weapon=weapon, loot=loot, enemy_char="O")


class Goblin(Enemy):
    def __init__(self, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(type="Goblin", hp=hp, dge=dge, spd=spd, phy_res=phy_res, fire_res=fire_res,
                         frost_res=frost_res, weapon=weapon, loot=loot, enemy_char="G")
