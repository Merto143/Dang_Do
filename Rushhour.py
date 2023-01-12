from typing import Any, List
from sys import argv

class Car:

    def __init__(self, name: str, orientation: str, col: int, row: int, length: int) -> None:
            self.name = name
            self.orientation = orientation
            self.coordinates = [row, col]
            self.length = length

class Board:

    def __init__(self, dim: int, filename: str) -> None:
        self.dim = dim
        self.load_cars(filename)
        #self.grid = [["_"] * self.dim for row in range(self.dim)]

    def load_cars(self, filename) -> List[Car]:

        cars: List[Car] = []
        with open(filename) as f:
            line = f.readline()
            line # Skipt eerste line
            while line.strip() != "\n":
                line = line.split(",")
                car = Car(line[0], line[1], line[2], line[3], line[4], line[5])
                self.cars.append(car)

        return cars

    def grid(self) -> List[List[str]]:
        for item in cars:
            if item.orientation == "H":
                for j in range(item.col - 1, item.col + item.length - 2, 1):
                    self.grid[item.row][j] = item.name
            else:
                for i in range(item.row - 1, item.row + item.length - 2, 1):
                    self.grid[i][item.col] = item.name


    def __repr__(self) -> str:

        return f"{self.grid}" # Fix dat 'ie t als een grid format

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 representation.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    grid = Board(6, filename)
