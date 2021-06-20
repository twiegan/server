from f_core.Character import Ally


class Thomas(Ally):
    def __init__(self, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(type="Thomas", hp=hp, dge=dge, spd=spd, phy_res=phy_res, fire_res=fire_res,
                         frost_res=frost_res, weapon=weapon, loot=loot, ally_char="T")


class Joe(Ally):
    def __init__(self, hp, dge, spd, phy_res, fire_res, frost_res, weapon, loot):
        super().__init__(type="Joe", hp=hp, dge=dge, spd=spd, phy_res=phy_res, fire_res=fire_res,
                         frost_res=frost_res, weapon=weapon, loot=loot, ally_char="J")