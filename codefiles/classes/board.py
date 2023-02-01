from .car import Car
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math
from colorhash import ColorHash


class Board:

    def __init__(self, dim, filename):
        """ Initializer. """

        self.dim = dim
        self.cars = []
        self.grid = np.full((dim, dim), "-")
        self.moveable_cars = []
        self.visited_states = []
        self.color_dict = {}
        self.filename = filename
        self.depth = None
        self.load_cars(f"data/{filename}.csv")
        self.add_cars_to_grid()


    def get_dim(self):
        """ Return the dimension of the board. """

        return self.dim


    def get_cars(self):
        """ Return a list of the car opbjects on the Board. """

        return self.cars


    def get_color_dict(self):
        """ Returns the dictionary of colors of the cars. """

        return self.color_dict


    def load_cars(self, file):
        """ Load the cars in self.cars from the datastructure. """

        with open(file) as f:

            line = f.readline()
            line = f.readline()

            # read the lines untill we are at the end of the file
            while line != "":
                line = line.split(",")
                # make a car object for each line and add it to self.cars
                car = Car(line[0], line[1], line[2], line[3], line[4])
                self.cars.append(car)

                line = f.readline()

            # give each car a color
            for car in self.cars:
                self.color_dict[car.get_name()] = ColorHash(car.get_name()).hex
                self.color_dict["X"] = "r"


    def add_cars_to_grid(self):
        """ Add the cars in self.cars to the grid. """

        for car in self.cars:
            spaces = car.get_car_spaces()

            # change the grid spots of each of the car coordinates
            for i in range(car.get_length()):
                space = spaces[i]
                self.grid[space[0] - 1][space[1] - 1] = car.get_name()


    def get_moveable_cars(self):
        """ Return a list of moveable cars. """

        return self.moveable_cars


    def move_car(self, car, direction):
        """ Move a car in a given direction. """

        # check if the move is legal
        if self.car_is_movable(car, direction):
            # move the car on the grid in the given direction
            if direction == "E":
                self.grid[car.get_row() - 1][car.get_col() - 1] = "-"
                car.set_col(car.get_col() + 1)
                self.grid[car.get_row() - 1][car.get_col() + car.get_length() - 2] = car.get_name()

            elif direction == "W":
                car.set_col(car.get_col() - 1)
                self.grid[car.get_row() - 1][car.get_col() - 1] = car.get_name()
                self.grid[car.get_row() - 1][car.get_length() + car.get_col() - 1] = "-"

            elif direction == "N":
                car.set_row(car.get_row() - 1)
                self.grid[car.get_row() - 1][car.get_col() - 1] = car.get_name()
                self.grid[car.get_length() + car.get_row() - 1][car.get_col() - 1] = "-"

            elif direction == "S":
                self.grid[car.get_row() - 1][car.get_col() - 1] = "-"
                car.set_row(car.get_row() + 1)
                self.grid[car.get_row() + car.get_length() - 2][car.get_col() - 1] = car.get_name()
        # change the car coordinates
        car.set_coordinates(car.get_row(), car.get_col())


    def car_is_movable(self, car, direction):
        """ Return True if the car is able to go in the given direction. """

        # check if the adjacent tile is free for a given car and direction
        if direction == "E" and car.get_orientation() == "H":
            if car.get_col() + car.get_length() <= self.dim:
                if self.grid[car.get_row() - 1][car.get_col() + car.get_length() - 1] == "-":
                    return True

        elif direction == "W" and car.get_orientation() == "H":
            if car.get_col() != 1:
                if self.grid[car.get_row() - 1][car.get_col() - 2] == "-":
                    return True

        elif direction == "N" and car.get_orientation() == "V":
            if car.get_row() != 1:
                if self.grid[car.get_row() - 2][car.get_col() - 1] == "-":
                    return True

        elif direction == "S" and car.get_orientation() == "V":
            if car.get_row() + car.get_length() <= self.dim:
                if self.grid[car.get_row() + car.get_length() - 1][car.get_col() - 1] == "-":
                    return True

        return False


    def generate_moveability(self):
        """ Add cars that are moveable to self.moveable_cars. """
        self.moveable_cars = []

        # go through each car
        for car in self.cars:
            car.clear_legal_moves()

            # check if the cars stands horizontal or vertical
            if car.get_orientation() == "H":
                # check if a car is moveable for each direction
                for move in ["E", "W"]:
                    if self.car_is_movable(car, move):
                        car.add_legal_move(move)
                        if car not in self.moveable_cars:
                            self.moveable_cars.append(car)

            elif car.get_orientation() == "V":
                for move in ["N", "S"]:
                    if self.car_is_movable(car, move):
                        car.add_legal_move(move)
                        if car not in self.moveable_cars:
                            self.moveable_cars.append(car)


    def is_solved(self):
        """ Check if the game is solved. """
        # define the objective car
        red_car = self.cars[-1]

        # check if the car is on the exit tile
        if red_car.get_position() == [math.ceil(self.dim / 2), self.dim - 1]:
            return True
        return False


    def get_car(self, name):
        """ Get the car object from the car name. """

        for car in self.cars:
            if name == car.name:
                return car


    def set_car_coordinates(self):
        """ Using a given grid, set the cars to the right coordinates. """

        added_cars = []

        # go through each element of the board
        for row in range(self.dim):
            for col in range(self.dim):
                space = self.grid[row][col]
                # check if there is car on a gridspot when it is not in the added cars
                if  space != "-" and space not in added_cars:
                    car = self.get_car(space)
                    car.row = row + 1
                    car.col = col + 1
                    car.set_coordinates(row + 1, col + 1)
                    added_cars.append(space)


    def undo_move(self, car, direction):
        """ Moves the car in the opposite direction. """

        if direction == "E":
            self.move_car(car, "W")
        elif direction == "W":
            self.move_car(car, "E")
        elif direction == "N":
            self.move_car(car, "S")
        elif direction == "S":
            self.move_car(car, "N")


    def tiles_blocked(self):
        """ Returns the amount of tiles that are blocked in front of the red car. """

        red_car = self.cars[-1]
        blocking_cars = []
        position = self.cars[-1].get_col()
        for tile in range(position + 1, self.dim):
            # add 1 to occupied if
            if self.grid[red_car.get_row() - 1, tile] != "-":
                blocking_cars.append(self.get_car(self.grid[red_car.get_row() - 1, tile]))

        return blocking_cars


    def blocked_cars_blocked(self):
        """ Returns the amount of moves possible. """

        self.generate_moveability()

        blocking_cars = self.tiles_blocked()
        max_moves = 2*len(blocking_cars)
        moves = 0
        for car in blocking_cars:
            moves += len(car.get_legal_moves())

        return max_moves - moves


    def distance_away(self):
        """Return the distance between the red car and the exit. """

        position = self.cars[-1].get_col()
        distance = self.dim - (position + 1)

        return distance


    def object_function(self):
        """Determine a score for a given state. """

        score = -len(self.tiles_blocked()) - self.distance_away() - self.blocked_cars_blocked()

        return score


    def get_id(self):
        """Generate an unique id for the current board. """

        self.id = ""

        # add each item in the grid to a string which turns into an unique id
        for row in range(self.dim):
            for col in range(self.dim):
                item = self.grid[row][col]
                self.id += item

        return self.id


    def get_board_with_id(self):
        """Set the grid and car coordinates using the current board id. """

        # empty the grid
        self.grid = np.full((self.dim, self.dim), "-")
        item = 0
        # go through each element in the unique id and place it on the grid
        for row in range(self.dim):
            for col in range(self.dim):
                self.grid[row][col] = self.id[item]
                item += 1

        # reset the car coordinates
        self.set_car_coordinates()


    def number_of_cars_moveable(self):
        """ Returns the number of moveable cars. """

        return len(self.moveable_cars)
