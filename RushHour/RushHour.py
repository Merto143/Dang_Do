from typing import Any, List
from sys import argv
from car import Car
from board import Board
import numpy as np
import random


def random_algorithm():
    carX = game.cars[len(game.cars) - 1]
    iterations = 0
    direction = ""

    while carX.coordinates != [3, 5]:
        car = random.choice(game.cars)

        if car.get_orientation() == "H":
            direction = random.choice(["E", "W"])

        elif car.get_orientation() == "V":
            direction = random.choice(["N", "S"])

        print([car, direction])
        game.move_car(car, direction)
        iterations += 1
    print(iterations)

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 RushHour.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    game = Board(6, filename)


    random_algorithm()
