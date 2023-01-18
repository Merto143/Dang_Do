from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.classes.queue import Queue
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


def breadth_first(game):
    game.generate_moveability()
    cars = game.get_moveable_cars()
    memory = []
    memory.append(game.grid)

    queue = Queue()

    for car in cars:
        queue.enqueue(car)

    car = queue.dequeue()

    if len(car.legal_moves) == 1:
        direction = car.legal_moves[0]
        game.move_car(car, direction)





    print(memory)
    print(cars)
    print(queue.list)
