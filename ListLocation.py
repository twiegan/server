from Map import Location


class Town(Location):
    def __init__(self):
        super().__init__(name="Town",
                         description="Town description...",
                         loc_char="T",
                         options=["Trade", "Leave"])

    def toJson(self):
        return {'name': self.name, 'description': self.description, 'loc_char': self.loc_char,
                'options': self.options}


class City(Location):
    def __init__(self):
        super().__init__(name="City",
                         description="City description...",
                         loc_char="C",
                         options=["Loot the City", "Leave"])

    def toJson(self):
        return {'name': self.name, 'description': self.description, 'loc_char': self.loc_char,
                'options': self.options}
