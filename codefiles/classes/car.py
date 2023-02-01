class Car:

    def __init__(self, name, orientation, col, row, length):
        """ Initializer. """

        self.name = name
        self.orientation = orientation
        self.row = int(row)
        self.col = int(col)
        self.coordinates = [self.row, self.col]
        self.length = int(length)
        self.legal_moves = []


    def __repr__(self):
        """Represent the board as its name. """

        return self.name


    def get_name(self):
        """Return the name of the car. """

        return self.name


    def get_col(self):
        """Return the column of the car. """


        return self.col


    def set_col(self, col):
        """Set the column of the car. """

        self.col = col


    def get_row(self):
        """Return the row of the car. """

        return self.row


    def set_row(self, row):
        """Set the row of the car. """

        self.row = row


    def get_position(self):
        """Return the coordinates of the car. """

        return self.coordinates


    def set_coordinates(self, row, col):
        """Set the coordinates of the car. """

        self.coordinates = [row, col]


    def get_orientation(self):
        """Run if the car stands horizontal or vertical. """

        return self.orientation


    def get_length(self):
        """Return the length of the car. """

        return self.length


    def get_legal_moves(self):
        """Return the legal moves of a car."""

        return self.legal_moves


    def get_car_spaces(self):
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


    def add_legal_move(self, direction):
        """Add a move to self.legal_moves. """

        self.legal_moves.append(direction)


    def clear_legal_moves(self):
        """Empty the legal moves of the car. """

        self.legal_moves = []
