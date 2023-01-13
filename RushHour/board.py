from car import Car
import numpy as np

#comment
class Board:

    def __init__(self, dim: int, filename: str) -> None:
        self.dim = dim
        self.cars = []
        self.grid = np.full((dim, dim), "-")
        self.load_cars(f"gameboards/{filename}.csv")
        self.add_cars_to_grid()


    def load_cars(self, file):
        with open(file) as f:

            line = f.readline()
            line = f.readline()

            while line != "":
                line = line.split(",")
                car = Car(line[0], line[1], line[2], line[3], line[4])
                self.cars.append(car)

                line = f.readline()


    def add_cars_to_grid(self):
        for car in self.cars:
            spaces = car.get_car_spaces()

            for i in range(car.get_length()):
                space = spaces[i]
                self.grid[space[0] - 1][space[1] - 1] = car.name

        # print(self.grid)

    def get_cars(self):
        return self.cars

    def move_car(self, car, direction):
        if self.car_is_movable(car, direction):

            if direction == "E":
                self.grid[car.row - 1][car.col - 1] = "-"
                car.col += 1
                self.grid[car.row - 1][car.col + car.length - 2] = car.name


            elif direction == "W":
                car.col -= 1
                self.grid[car.row - 1][car.col - 1] = car.name
                self.grid[car.row - 1][car.length + car.col - 1] = "-"

            elif direction == "N":
                car.row -= 1
                self.grid[car.row - 1][car.col - 1] = car.name
                self.grid[car.length + car.row - 1][car.col - 1] = "-"

            elif direction == "S":
                self.grid[car.row - 1][car.col - 1] = "-"
                car.row += 1
                self.grid[car.row + car.length - 2][car.col - 1] = car.name

            # print(self.grid)

        car.coordinates = [car.row, car.col]


    def car_is_movable(self, car, direction):
        if direction == "E" and car.get_orientation() == "H":
            if car.col + car.length  <=  6:
                if self.grid[car.row - 1][car.col + car.length - 1] == "-":
                    return True

        elif direction == "W" and car.get_orientation() == "H":
            if car.col != 1:
                if self.grid[car.row - 1][car.col - 2] == "-":
                    return True

        elif direction == "N" and car.get_orientation() == "V":
            if car.row != 1:
                if self.grid[car.row - 2][car.col - 1] == "-":
                    return True

        elif direction == "S" and car.get_orientation() == "V":
            if car.row + car.length <= 6:
                if self.grid[car.row + car.length - 1][car.col - 1] == "-":
                    return True

        return False
