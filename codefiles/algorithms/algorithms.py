from codefiles.classes.car import Car
from codefiles.classes.board import Board
import random


def random_only_legal_moves_algorithm(game):
    cars = game.get_cars()
    carX = cars[len(cars) - 1]
    game.generate_moveability()
    total_moves = 0

    while not game.is_solved():
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

    while not game.is_solved():
        car = random.choice(cars)

        if car.get_orientation() == "H":
            direction = random.choice(["E", "W"])

        elif car.get_orientation() == "V":
            direction = random.choice(["N", "S"])

        game.move_car(car, direction)
        total_moves += 1
    return total_moves
