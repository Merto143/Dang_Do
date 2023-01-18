from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.classes.queue import Queue
import random


def random_only_legal_moves_algorithm(game):
    cars = game.get_cars()
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
        for direction in car.get_legal_moves():
            move = [car, direction]

        queue.enqueue(move)

    move = queue.dequeue()

    game.move_car(move[0], move[1])
    memory.append(game.grid)
    print(memory)

    game.grid = memory[0]
    game.set_car_coordinates()
    print(game.cars[0].get_position())
    print(cars)
    print(queue.list)


def tiles_blocked_heur(game):
    cars = game.get_cars()
    game.generate_moveability()
    total_moves = 0

    while not game.is_solved():
        car = random.choice(game.get_moveable_cars())
        direction = random.choice(car.legal_moves)
        tiles = game.tiles_blocked()
        game.move_car(car, direction)
        if game.tiles_blocked() > tiles:
            game.undo_move(car, direction)
        else:
            total_moves += 1
        game.generate_moveability()

    return total_moves
