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
    def __init__(self, name, value, durability, damage, type, one_handed):
        super().__init__(name, value)
        self.durability = durability
        self.damage = damage
        self.type = type
        self.one_handed = one_handed

    def print_object(self):
        print(
            'Weapon Object:\n'
            f'Name: {self.name}, Value: {self.value}\n'
            f'Durability: {self.durability}, Damage: {self.damage}\n'
            f'Type: {self.type}, One-Handed: {self.one_handed}\n'
        )

    def toJson(self):
        return {'name': self.name, 'value': self.value, 'durability': self.durability, 'damage': self.damage,
                'type': self.type, 'one_handed': self.one_handed}


class Armour(Item):
    def __init__(self, name, value, durability, defense, type, slot):
        super().__init__(name, value)
        self.durability = durability
        self.defense = defense
        self.type = type
        self.slot = slot

    def print_object(self):
        print(
            'Armour Object:\n'
            f'Name: {self.name}, Value: {self.value}\n'
            f'Durability: {self.durability}, Defense: {self.defense}\n'
            f'Type: {self.type}, Slot: {self.slot}\n'
        )

    def toJson(self):
        return {'name': self.name, 'value': self.value, 'durability': self.durability, 'defense': self.defense,
                'type': self.type, 'slot': self.slot}
