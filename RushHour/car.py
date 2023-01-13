class Car:

    def __init__(self, name: str, orientation: str, col: int, row: int, length: int):
        self.name = name
        self.orientation = orientation
        self.row = int(row)
        self.col = int(col)
        self.coordinates = [self.row, self.col]
        self.length = int(length)
        self.legal_moves = []

    def __repr__(self):
        return self.name

    def get_position(self):
        return self.coordinates

    def get_orientation(self):
        return self.orientation

    def get_length(self):
        return self.length

    def get_car_spaces(self):
        spaces = []

        if self.orientation == "H":
            for i in range(self.length):
                space = [self.row, self.col + i]
                spaces.append(space)
        else:
            for i in range(self.length):
                space = [self.row + i, self.col]
                spaces.append(space)

        return spaces

    def add_legal_move(self, direction):
        self.legal_moves.append(direction)

    def clear_legal_moves(self):
        self.legal_moves = []
