from typing import Any, List
from sys import argv
from car import Car
from board import Board
import numpy as np


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 RushHour.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    game = Board(6, filename)
    carA = game.cars[0]
    carB = game.cars[1]
    carC = game.cars[2]
    carG = game.cars[6]
    
    game.move_car(carA, "E")
    print(game.grid)

    game.move_car(carA, "W")
    print(game.grid)
    game.move_car(carA, "E")
    print(game.grid)
    game.move_car(carA, "W")
    print(game.grid)
    game.move_car(carC, "W")
    print(game.grid)
    game.move_car(carG, "N")
    game.move_car(carG, "N")

    print(game.grid)
