from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.classes.queue import Queue
import random
import copy
import numpy as np

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
    grid_memory = []
    move_memory = []

    queue = Queue()
    grid = copy.deepcopy(game.grid)
    grid_memory.append(grid)
    node = 0
    carX = game.get_cars()[-1]
    carI = game.get_cars()[8]
    carJ = game.get_cars()[9]
    cars = game.get_moveable_cars()

    for car in cars:
        for direction in car.get_legal_moves():
            move = [car, direction, node]
            queue.enqueue(move)

    while (queue.list != []):
        move = queue.dequeue()
        game.grid = copy.deepcopy(grid_memory[move[-1]])
        game.set_car_coordinates()

        game.move_car(move[0], move[1])

        if not any(np.array_equal(game.grid, item) for item in grid_memory):
            move_memory.append(move)
            grid_memory.append(copy.deepcopy(game.grid))
            node += 1

            game.generate_moveability()
            cars = game.get_moveable_cars()

            for car in cars:
                for direction in car.get_legal_moves():
                    new_move = [car, direction, node]
                    queue.enqueue(new_move)


        if game.is_solved():
            print("game is solved")
            break

    print(len(grid_memory))


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
