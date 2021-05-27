import json


class Map:
    def __init__(self, rows, cols, map):
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
        return json.dumps([[ob.__dict__ for ob in lst] for lst in self.map])


class Tile:
    def __init__(self, row, col, disc_char, undisc_char):
        self.disc = False
        self.row = row
        self.col = col
        self.disc_char = disc_char
        self.undisc_char = undisc_char

    def to_string(self):
        if self.disc:
            return f'{self.disc_char}'
        else:
            return f'{self.undisc_char}'

    def print_object(self):
        print(
            'Tile Object:\n'
            f'Row: {self.row}, Col: {self.col} Disc: {self.disc}\n'
            f'Disc_Char: {self.disc_char}, Undisc_char: {self.undisc_char}\n'
        )
