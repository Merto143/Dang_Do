from sys import argv
from codefiles.classes.car import Car
from codefiles.classes.board import Board
import numpy as np
import random
from tqdm import tqdm


def random_only_legal_moves_algorithm(game):
    cars = game.get_cars()
    carX = cars[len(cars) - 1]
    game.generate_moveability()
    total_moves = 0

    while carX.get_position() != [3, 5]:
        car = random.choice(game.get_moveable_cars())
        direction = random.choice(car.legal_moves)
        game.move_car(car, direction)
        total_moves += 1
        game.generate_moveability()

    return total_moves


def random_all_moves_algorithm(game):
    cars = game.get_cars()
    carX = cars[len(cars) - 1]
    total_moves = 0
    direction = ""

    while carX.get_position() != [3, 5]:
        car = random.choice(cars)

        if car.get_orientation() == "H":
            direction = random.choice(["E", "W"])

        elif car.get_orientation() == "V":
            direction = random.choice(["N", "S"])

        # print([car, direction])
        game.move_car(car, direction)
        total_moves += 1
    return total_moves
