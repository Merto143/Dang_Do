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
    grid = copy.deepcopy(game.grid)
    grid_memory.append([grid, "-"])

    node = 0
    queue = Queue()

    carX = game.get_cars()[-1]
    cars = game.get_moveable_cars()

    for car in cars:
        for direction in car.get_legal_moves():
            move = [car, direction, node]
            queue.enqueue(move)

    while (queue.list != []):
        move = queue.dequeue()
        game.grid = copy.deepcopy(grid_memory[move[-1]][0])
        game.set_car_coordinates()

        game.move_car(move[0], move[1])
        memories = list(zip(*grid_memory))[0]

        if not any(np.array_equal(game.grid, item) for item in memories):
            move_memory.append(move)
            grid_memory.append([copy.deepcopy(game.grid), move])
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

    solution = []
    solution.insert(0, [grid_memory[-1][1][0], grid_memory[-1][1][1]])
    grid_memory[-1][0]
    node = grid_memory[-1][1][2]

    while node != 0:
        print(grid_memory[node][0])
        solution.insert(0, [grid_memory[node][1][0], grid_memory[node][1][1]])
        new_node = grid_memory[node][1][2]
        node = new_node
    print(grid_memory[node][0])
    print(solution)


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
