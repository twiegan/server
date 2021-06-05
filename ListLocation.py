from Map import Location


class Town(Location):
    def __init__(self):
        super().__init__(name="Town", description="Town description...", loc_char="T")
