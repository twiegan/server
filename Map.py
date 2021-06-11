from Constants import PLAYER_CHAR, UNDISCOVERED_CHAR


class Map:
    def __init__(self, rows, cols, map):
        self.player_char = PLAYER_CHAR  # displayed character for the player
        self.undisc_char = UNDISCOVERED_CHAR  # displayed character pre discovery
        self.rows = rows
        self.cols = cols
        self.map = map  # 2D list of Tiles

    def to_string(self):
        to_return = ''
        for i in range(self.rows):
            for j in range(self.cols):
                to_return += self.map[i][j].to_string() + " "
            to_return += "\n"
        return to_return

    def print_object(self):
        print('Map Object:')
        for i in range(self.rows):
            to_print = f'Map[{i}]: '
            for j in range(self.cols):
                to_print += self.map[i][j].to_string() + " "
            print(f'{to_print}')

    def toJson(self):
        return {'player_char': self.player_char, 'undisc_char': self.undisc_char,
                'curr_map': [[ob.toJson() for ob in lst] for lst in self.map]}


class Tile:
    def __init__(self, xpos, ypos, disc_char, description, location, weight, type):
        self.disc = False
        self.hasPlayer = False
        self.xpos = xpos
        self.ypos = ypos
        self.disc_char = disc_char  # displayed character after discovery
        self.description = description  # displayed description on entry if no location
        self.location = location  # point of interest
        self.weight = weight  # weight out of 100
        self.type = type

    def to_string(self):
        return f'{self.disc_char}'

    def print_object(self):
        print(
            'Tile Object:\n'
            f'Xpos: {self.xpos}, Ypos: {self.ypos} Disc: {self.disc}\n'
            f'Disc_Char: {self.disc_char}, hasPlayer: {self.hasPlayer}\n'
        )

    def toJson(self):
        return {'disc': self.disc, 'hasPlayer': self.hasPlayer, 'xpos': self.xpos, 'ypos': self.ypos,
                'disc_char': self.disc_char, 'description': self.description,
                'location': None if self.location is None else self.location.toJson(),
                'weight': self.weight, 'type': self.type}


class Location:
    def __init__(self, name, description, loc_char, options):
        self.name = name
        self.description = description  # displayed description on entry
        self.loc_char = loc_char  # displayed character after discovery
        self.options = options

    def print_object(self):
        print(
            'Location Object:\n'
            f'Name: {self.name}, Description: {self.description}, Loc_char: {self.loc_char}, Options:{self.options}\n'
        )

