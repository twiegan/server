from Map import Tile


class ErrorTile(Tile):
    def __init__(self):
        super().__init__(-1, -1, None, None, None, None, type="Error")


class Desert(Tile):
    def __init__(self, xpos, ypos, location, weight):
        super().__init__(xpos, ypos, ".", "Desert...", location, weight, type="Desert")


class Grassland(Tile):
    def __init__(self, xpos, ypos, location, weight):
        super().__init__(xpos, ypos, ",", "Grassland...", location, weight, type="Grassland")
