from typing import Any, List
from sys import argv

class Board:

    def __init__(self, dim: int, filename: str) -> None:
        self.dim = dim
        self.cars = []
        self.grid = []
        self.load_cars(f"gameboards/{filename}.csv")


    def load_cars(self, file):
        with open(file) as f:

            line = f.readline()
            line = f.readline()

            while line != "":
                line = line.split(",")
                car = Car(line[0], line[1], line[2], line[3], line[4])
                self.cars.append(car)

                line = f.readline()


class Car:

    def __init__(self, name: str, orientation: str, col: int, row: int, length: int):
        self.name = name
        self.orientation = orientation
        self.coordinates = [row, col]
        self.length = length

    def __repr__(self):
        return self.name

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 representation.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    grid = Board(6, filename)
