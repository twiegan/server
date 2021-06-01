import json

WTypes = {
    'Knife': {
        'name': 'Knife',
        'one-handed': True
    },
    'Sword': {
        'name': 'Sword',
        'one-handed': True
    },
    'Bow': {
        'name': 'Bow',
        'one-handed': False
    }
}  # WTypes
ATypes = {
    'Helm': {
        'name': 'Helm',
        'slot': 'Head'
    },
    'Breastplate': {
        'name': 'Breastplate',
        'slot': 'Chest'
    },
    'Gauntlets': {
        'name': 'Gauntlets',
        'slot': 'Legs'
    },
    'Greaves': {
        'name': 'Greaves',
        'slot': 'Hands'
    },
    'Boots': {
        'name': 'Boots',
        'slot': 'Feet'
    }
}  # ATypes


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def print_object(self):
        print(
            'Item Object:\n'
            f'Name: {self.name}, Value: {self.value}\n'
        )


class Weapon(Item):
    def __init__(self, name, value, durability, type, damage):
        super().__init__(name, value)
        self.durability = durability
        self.type = type
        self.damage = damage

    def print_object(self):
        print(
            'Weapon Object:\n'
            f'Name: {self.name}, Value: {self.value}\n'
            f'Durability: {self.durability}, Type: {self.type}, Damage: {self.damage}\n'
        )

    def toJson(self):
        return {'name': self.name, 'value': self.value, 'durability': self.durability, 'type': self.type, 'damage': self.damage}


class Armour(Item):
    def __init__(self, name, value, durability, type, defense):
        super().__init__(name, value)
        self.durability = durability
        self.type = type
        self.defense = defense

    def print_object(self):
        print(
            'Armour Object:\n'
            f'Name: {self.name}, Value: {self.value}\n'
            f'Durability: {self.durability}, Type: {self.type}, Defense: {self.defense}\n'
        )

    def toJson(self):
        return {'name': self.name, 'value': self.value, 'durability': self.durability, 'type': self.type, 'defense': self.defense}
