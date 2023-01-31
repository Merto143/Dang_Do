from .car import Car
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math
from colorhash import ColorHash


# COLORS = {"X" : "#DC3C32", "A" : "#9BC88C", "B" : "#E68C41", "C" : "#5AB9EB", "D" : "#E182A0", "E" : "#6964AA", "F" : "#45966E", "G" : "#AFAFB4", "H" : "#FAE6C8", "I" : "#FFF56E", "J" : "#8C645A", "K" : "#8C8C2D", "L" : "k", "O" : "#FAD24B", "P" : "#9682BE", "Q" : "#3778B4", "R" : "#50AA9B"}


class Board:

    def __init__(self, dim: int, filename: str) -> None:
        self.dim = dim
        self.cars: list[Car] = []
        self.grid = np.full((dim, dim), "-")
        self.moveable_cars: list[Car] = []
        self.visited_states = []
        self.color_dict = {}
        self.filename = filename
        self.load_cars(f"data/{filename}.csv")
        self.add_cars_to_grid()

    def get_dim(self):
        return self.dim

    def get_cars(self):
        return self.cars

    def get_color_dict(self):
        return self.color_dict

    def load_cars(self, file: str) -> None:
        with open(file) as f:

            line = f.readline()
            line = f.readline()

            while line != "":
                line = line.split(",")
                car = Car(line[0], line[1], line[2], line[3], line[4])
                self.cars.append(car)

                line = f.readline()

            for car in self.cars:
                self.color_dict[car.get_name()] = ColorHash(car.get_name()).hex
                self.color_dict["X"] = "r"


    def add_cars_to_grid(self) -> None:
        for car in self.cars:
            spaces = car.get_car_spaces()

            for i in range(car.get_length()):
                space = spaces[i]
                self.grid[space[0] - 1][space[1] - 1] = car.get_name()


    def get_cars(self) -> list[Car]:
        return self.cars


    def get_moveable_cars(self) -> list[Car]:
        return self.moveable_cars


    def move_car(self, car: Car, direction: str) -> None:
        if self.car_is_movable(car, direction):

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

        car.set_coordinates(car.get_row(), car.get_col())


    def car_is_movable(self, car: Car, direction: str) -> bool:
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


    def generate_moveability(self) -> None:
        self.moveable_cars = []
        for car in self.cars:
            car.clear_legal_moves()
            if car.get_orientation() == "H":
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


    def is_solved(self) -> bool:
        red_car = self.cars[-1]
        if red_car.get_position() == [math.ceil(self.dim / 2), self.dim - 1]:
            return True
        return False

    def get_car(self, name):
        for car in self.cars:
            if name == car.name:
                return car


    def set_car_coordinates(self):
        added_cars = []
        for row in range(self.dim):
            for col in range(self.dim):
                space = self.grid[row][col]
                if  space != "-" and space not in added_cars:
                    car = self.get_car(space)
                    car.row = row + 1
                    car.col = col + 1
                    car.set_coordinates(row + 1, col + 1)
                    added_cars.append(space)


    def undo_move(self, car, direction):
        if direction == "E":
            self.move_car(car, "W")
        elif direction == "W":
            self.move_car(car, "E")
        elif direction == "N":
            self.move_car(car, "S")
        elif direction == "S":
            self.move_car(car, "N")


    def get_all_moves(self) -> list[list[Car,str]]:
        moves = []
        self.generate_moveability()
        print(f"We have {len(self.moveable_cars)} moveable cars")
        for car in self.get_moveable_cars():
            print(car)
            for direction in car.get_legal_moves():
                print(direction)
                move = [car, direction]
                moves.append(move)
        print(f"this turn has options: {moves}")
        return moves


    def tiles_blocked(self):
        red_car = cars[-1]
        occupied = 0
        position = self.cars[-1].get_col()
        for tile in range(position + 1, self.dim):
            if self.grid[red_car.get_row() - 1, tile] != "-":
                occupied += 1

        return occupied


    def distance_away(self):
        position = self.cars[-1].get_col()
        distance = self.dim - (position + 1)

        return distance


    def object_function(self):
        score = self.tiles_blocked() + self.distance_away()

        return score

    def get_id(self):
        self.id = ""
        for row in range(self.dim):
            for col in range(self.dim):
                item = self.grid[row][col]
                if item == "-":
                    self.id += "0"
                else:
                    self.id += item
        return self.id
