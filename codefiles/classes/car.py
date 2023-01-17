class Car:

    def __init__(self, name: str, orientation: str, col: str, row: str, length: str) -> None:
        self.name = name
        self.orientation = orientation
        self.row = int(row)
        self.col = int(col)
        self.coordinates = [self.row, self.col]
        self.length = int(length)
        self.legal_moves: list[str] = []

    def __repr__(self) -> str:
        return self.name

    def get_name(self) -> str:
        return self.name

    def get_col(self) -> int:
        return self.col

    def set_col(self, col: int) -> None:
        self.col = col

    def get_row(self) -> int:
        return self.row

    def set_row(self, row: int) -> None:
        self.row = row

    def get_position(self) -> list[int]:
        return self.coordinates

    def set_coordinates(self, row: int, col: int) -> None:
        self.coordinates = [row, col]

    def get_orientation(self) -> str:
        return self.orientation

    def get_length(self) -> int:
        return self.length

    def get_car_spaces(self) -> list[list[int]]:
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

    def add_legal_move(self, direction: str) -> None:
        self.legal_moves.append(direction)

    def clear_legal_moves(self) -> None:
        self.legal_moves = []
