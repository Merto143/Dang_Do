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
        """Represent the board as its name. """
        return self.name

    def get_name(self) -> str:
        """Return the name of the car. """
        return self.name

    def get_col(self) -> int:
        """Return the column of the car. """
        return self.col

    def set_col(self, col: int) -> None:
        """Set the column of the car. """
        self.col = col

    def get_row(self) -> int:
        """Return the row of the car. """
        return self.row

    def set_row(self, row: int) -> None:
        """Set the row of the car. """
        self.row = row

    def get_position(self) -> list[int]:
        """Return the coordinates of the car. """
        return self.coordinates

    def set_coordinates(self, row: int, col: int) -> None:
        """Set the coordinates of the car. """
        self.coordinates = [row, col]

    def get_orientation(self) -> str:
        """Run if the car stands horizontal or vertical. """
        return self.orientation

    def get_length(self) -> int:
        """Return the length of the car. """
        return self.length

    def get_legal_moves(self):
        """Return the legal moves of a car."""
        return self.legal_moves

    def get_car_spaces(self) -> list[list[int]]:
        """Return the coordinates of the spaces the car stands on. """
        spaces = []

        # check the orientation of the car
        if self.orientation == "H":
            # append the coordinates of all the tiles the car stands on
            for i in range(self.length):
                space = [self.row, self.col + i]
                spaces.append(space)
        else:
            for i in range(self.length):
                space = [self.row + i, self.col]
                spaces.append(space)

        return spaces

    def add_legal_move(self, direction: str) -> None:
        """Add a move to self.legal_moves. """
        self.legal_moves.append(direction)

    def clear_legal_moves(self) -> None:
        """Empty the legal moves of the car. """
        self.legal_moves = []
