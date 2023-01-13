from typing import Any, List
from sys import argv
from car import Car
from board import Board
import numpy as np
import random
from tqdm import tqdm


def random_algorithm():
    cars = game.get_cars()
    carX = cars[len(cars) - 1]
    iterations = 0
    direction = ""

    while carX.get_position() != [3, 5]:
        car = random.choice(cars)

        if car.get_orientation() == "H":
            direction = random.choice(["E", "W"])

        elif car.get_orientation() == "V":
            direction = random.choice(["N", "S"])

        # print([car, direction])
        game.move_car(car, direction)
        iterations += 1
    return iterations

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 RushHour.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    game = Board(6, filename)

    all_iterations = []
    for i in tqdm(range(10)):
        all_iterations.append(random_algorithm())
        game = Board(6, filename)

    print(all_iterations)
