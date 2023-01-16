from typing import Any, List
from sys import argv
from car import Car
from board import Board
import numpy as np
import random
from tqdm import tqdm


def random_only_legal_moves_algorithm():
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

def random_all_moves_algorithm():
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

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 RushHour.py [filename]")
        exit(1)
    else:
        filename = argv[1]

    game = Board(6, filename)
    game.visual()
    all_moves = random_all_moves_algorithm()
    game = Board(6, filename)
    legal_moves = random_only_legal_moves_algorithm()

    print(f"All moves: {all_moves} try's to solve the problem")
    print(f"Legal moves: {legal_moves} try's to solve the problem")
    # all_iterations = []
    # for i in tqdm(range(100)):
    #     all_iterations.append(random_algorithm())
    #     game = Board(6, filename)
    #
    # print(all_iterations)
