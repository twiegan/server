from f_core.Item import Weapon, Armour


# Weapons
class Knife(Weapon):
    def __init__(self, name, value, durability, damage):
        super().__init__(name, value, durability, damage, type="Knife", one_handed=True)


class Sword(Weapon):
    def __init__(self, name, value, durability, damage):
        super().__init__(name, value, durability, damage, type="Sword", one_handed=True)


class Bow(Weapon):
    def __init__(self, name, value, durability, damage):
        super().__init__(name, value, durability, damage, type="Bow", one_handed=False)


# Armour
class Helm(Armour):
    def __init__(self, name, value, durability, defense):
        super().__init__(name, value, durability, defense, type="Helm", slot="Head")


class Breastplate(Armour):
    def __init__(self, name, value, durability, defense):
        super().__init__(name, value, durability, defense, type="Breastplate", slot="Chest")


class Gauntlets(Armour):
    def __init__(self, name, value, durability, defense):
        super().__init__(name, value, durability, defense, type="Gauntlets", slot="Hands")


class Greaves(Armour):
    def __init__(self, name, value, durability, defense):
        super().__init__(name, value, durability, defense, type="Helm", slot="Legs")


class Boots(Armour):
    def __init__(self, name, value, durability, defense):
        super().__init__(name, value, durability, defense, type="Helm", slot="Feet")
