from CharacterTypes import Player, NonPlayer


def create_player(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, inventory):
    return Player(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, inventory)


def create_nonplayer(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, weapon):
    return NonPlayer(name, hp, dge, spd, phy_str, mgk_str, phy_res, fire_res, frost_res, weapon)
