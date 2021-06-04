import json


class Map:
    def __init__(self, rows, cols, map):
        self.player_char = "$"
        self.undisc_char = "_"
        self.rows = rows
        self.cols = cols
        self.map = map

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
        return json.dumps({'player_char': self.player_char, 'undisc_char': self.undisc_char, 'curr_map': [[ob.__dict__ for ob in lst] for lst in self.map]})


class Tile:
    def __init__(self, xpos, ypos, disc_char, description):
        self.disc = False
        self.hasPlayer = False
        self.xpos = xpos
        self.ypos = ypos
        self.disc_char = disc_char
        self.description = description

    def to_string(self):
        return f'{self.disc_char}'

    def print_object(self):
        print(
            'Tile Object:\n'
            f'Xpos: {self.xpos}, Ypos: {self.ypos} Disc: {self.disc}\n'
            f'Disc_Char: {self.disc_char}, hasPlayer: {self.hasPlayer}\n'
        )

    def toJson(self):
        return {'ypos': self.ypos, 'xpos': self.xpos, 'description': self.description}
