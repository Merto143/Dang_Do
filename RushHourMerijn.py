from typing import Any, List
from sys import argv

j

class Board:
    def __init__(self, dim: int, filename: str) -> None:
        self.dim = dim
        self.load_cars(f"gameboards/{filename}.csv")

    def load_cars(self, file):
        cars = []
        with open(file) as f:
            line = f.readline()
            line # Skipt eerste line
            while line.strip() != "\n":
                print(line)
                line = line.split(",")
                car = Car(line[0], line[1], line[2], line[3], line[4], line[5])
                self.cars.append(car)

        return cars



if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 representation.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    grid = Board(6, filename)
