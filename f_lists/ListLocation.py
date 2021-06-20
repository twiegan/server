from f_core.Map import Location


class Town(Location):
    def __init__(self, market):
        super().__init__(name="Town",
                         description="Town description...",
                         loc_char="T",
                         options=["Leave", "Market", "Heal"])
        self.market = market

    def toJson(self):
        return {'name': self.name, 'description': self.description, 'loc_char': self.loc_char,
                'options': self.options, 'market': self.market.toJson()}


class City(Location):
    def __init__(self):
        super().__init__(name="City",
                         description="City description...",
                         loc_char="C",
                         options=["Leave", "Heal"])

    def toJson(self):
        return {'name': self.name, 'description': self.description, 'loc_char': self.loc_char,
                'options': self.options}
