from codefiles.classes.car import Car
from codefiles.classes.board import Board
from codefiles.classes.queue import Queue
from codefiles.visualisations.visuals import *
import random
import copy

def random_only_legal_moves_algorithm(game):
    """Run the random algorithm with only legal moves on the given board. """
    total_moves = 0
    # get all moveable cars
    game.generate_moveability()

    # move a random car untill the game is solved
    while not game.is_solved():

        # get a random car that is able to move
        car = random.choice(game.get_moveable_cars())

        # get a random legal move and play the move
        direction = random.choice(car.legal_moves)
        game.move_car(car, direction)
        total_moves += 1

        # update the movebale cars
        game.generate_moveability()

    return total_moves


def random_only_legal_moves_memory_algorithm(game, times):
    """Run the random algorithm with only legal moves on the given board. Save
    the visited grid id's and repeat it a given amount of times to increase the
    total visited states"""
    # copy the game in the start state
    game0 = copy.copy(game)

    total_moves = 0
    random_memory = []

    # get all moveable cars
    game.generate_moveability()

    # add the start grid id to the memory
    random_memory.append(game.get_id())

    # repeat the random search a given amount of times.
    for time in range(times):
        game = Board(game0.dim, game0.filename)
        game.generate_moveability()

        # keep moving cars untill the game is solved
        while not game.is_solved():
            # choose a car that is able to move
            car = random.choice(game.get_moveable_cars())

            # choose a legal move and play that move
            direction = random.choice(car.get_legal_moves())

            game.move_car(car, direction)
            total_moves += 1
            game.generate_moveability()

            # if a state is not yet visited add the id to the random memory
            if not game.get_id() in random_memory:
                random_memory.append(game.get_id())

    return random_memory


def random_all_moves_algorithm(game):
    """Run the random all mnoves algorithm. The algorithm can pick a move that is
    not legal and then will not play that move """
    cars = game.get_cars()
    total_moves = 0
    direction = ""

    while not game.is_solved():
        # choose a random car
        car = random.choice(cars)

        # check if the position is horizontal of vertical
        if car.get_orientation() == "H":
            # choose random from East or West
            direction = random.choice(["E", "W"])

        elif car.get_orientation() == "V":
            # choose random from North or South
            direction = random.choice(["N", "S"])

        # apply the move (it might not be legal)
        game.move_car(car, direction)
        total_moves += 1

    return total_moves



def upperright_trucks_heur(game):
    totalscore = 0
    cars = game.get_cars()

    for car in cars:
        if car.get_length() == 3 and car.get_orientation() == "V":
            score = car.get_col() + (4 - car.get_row())
        totalscore += score

    return totalscore
